import importlib.util
import json
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'plan_review.py'
spec = importlib.util.spec_from_file_location('plan_review', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def events(session, *, complete=True, failed=False):
    data = [{'type': 'thread.started', 'thread_id': session},
            {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'Use the existing API.'}}]
    if complete:
        data.append({'type': 'turn.completed'})
    if failed:
        data.append({'type': 'turn.failed'})
    return '\n'.join(json.dumps(e) for e in data)


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.worktree = self.root / 'repo'
        self.worktree.mkdir()
        self.task = self.root / 'alpha.md'
        self.task.write_text('Task alpha')
        self.context = self.root / 'context.md'
        self.context.write_text('Original request: alpha; fixed scope: upload errors only.')
        self.ponytail = self.root / 'Ponytail SKILL.md'
        self.ponytail.write_text('PONYTAIL TEST: use the simplest complete design.')
        self.calls = []
        self.reply = None

    def cli(self, command, **kwargs):
        if command[0] == 'git':
            return subprocess.CompletedProcess(command, 0, str(self.worktree) + '\n', '')
        self.calls.append((command, kwargs))
        if self.reply:
            return self.reply(command, kwargs)
        session = command[command.index('resume') + 1] if 'resume' in command else str(uuid.uuid4())
        return subprocess.CompletedProcess(command, 0, events(session), '')

    def run_review(self, task=None, worktree=None):
        with patch.object(module.subprocess, 'run', side_effect=self.cli):
            return module.review(task or self.task, worktree or self.worktree, self.context, self.ponytail)

    def test_task_specific_stdin_and_exact_resume(self):
        marker = self.root / 'must-not-exist'
        payload = f'Original request: alpha $(touch {marker}); `echo unsafe`'
        self.context.write_text(payload)
        first, ok = self.run_review()
        self.assertTrue(ok)
        self.context.write_text('Answers for alpha; revised engineering plan.')
        second, ok = self.run_review()
        self.assertTrue(ok)
        self.assertEqual(first['session_id'], second['session_id'])
        self.assertEqual(second['round'], 2)
        initial, resumed = self.calls
        self.assertNotIn('resume', initial[0])
        self.assertEqual(resumed[0][resumed[0].index('resume') + 1], first['session_id'])
        for command, kwargs in self.calls:
            self.assertEqual(command[command.index('-s') + 1], 'read-only')
            self.assertNotIn('--last', command)
            self.assertFalse(kwargs.get('shell', False))
            self.assertIn('PONYTAIL TEST', kwargs['input'])
            self.assertIn(str(self.task), kwargs['input'])
            self.assertIn('not whether the product idea is complete', kwargs['input'])
        self.assertIn(payload, initial[1]['input'])
        self.assertFalse(marker.exists())
        self.assertTrue(Path(second['response']).is_file())
        self.assertFalse((Path(second['artifacts']) / 'running.lock').exists())

    def test_different_tasks_start_fresh_and_reject_copied_state(self):
        first, _ = self.run_review()
        beta = self.root / 'beta.md'
        beta.write_text('Task beta')
        self.context.write_text('Original request: beta; different plan.')
        second, ok = self.run_review(beta)
        self.assertTrue(ok)
        self.assertNotEqual(first['session_id'], second['session_id'])
        self.assertNotIn('resume', self.calls[-1][0])
        self.assertIn(str(beta), self.calls[-1][1]['input'])
        state = Path(second['artifacts']) / 'session.json'
        state.write_text((Path(first['artifacts']) / 'session.json').read_text())
        count = len(self.calls)
        with self.assertRaisesRegex(ValueError, 'another task/worktree'):
            self.run_review(beta)
        self.assertEqual(len(self.calls), count)

    def test_failed_or_incomplete_output_is_not_success(self):
        for output, code in [('not json\nnull\n', 0),
                             (json.dumps({'type': 'thread.started', 'thread_id': []}), 0),
                             (json.dumps({'type': 'item.completed', 'item': None}), 0),
                             (events(str(uuid.uuid4()), complete=False), 0),
                             (events(str(uuid.uuid4()), failed=True), 0),
                             (events(str(uuid.uuid4())), 1)]:
            with self.subTest(output=output):
                task = self.root / (str(uuid.uuid4()) + '.md')
                task.write_text('Failure case')
                self.reply = lambda cmd, kw: subprocess.CompletedProcess(cmd, code, output, 'failure details')
                result, ok = self.run_review(task)
                self.assertFalse(ok)
                self.assertEqual(result['status'], 'failed')
                self.assertTrue(list(Path(result['artifacts']).glob('*.events.jsonl')))

    def test_session_switch_is_rejected(self):
        first, _ = self.run_review()
        self.reply = lambda cmd, kw: subprocess.CompletedProcess(cmd, 0, events(str(uuid.uuid4())), '')
        result, ok = self.run_review()
        self.assertFalse(ok)
        self.assertEqual(result['session_id'], first['session_id'])

    def test_timeout_preserves_known_session_and_artifacts(self):
        session = str(uuid.uuid4())
        def timeout(cmd, kwargs):
            raise subprocess.TimeoutExpired(cmd, 300, output=events(session, complete=False).encode())
        self.reply = timeout
        result, ok = self.run_review()
        self.assertFalse(ok)
        self.assertEqual(result['session_id'], session)
        self.assertEqual(result['exit_code'], -1)
        self.assertIn('timed out', next(Path(result['artifacts']).glob('*.stderr.log')).read_text())

    def test_duplicate_launch_and_partial_round_do_not_overwrite(self):
        directory = self.task.with_suffix('') / 'auto-review'
        directory.mkdir(parents=True)
        lock = directory / 'running.lock'
        lock.write_text('existing owner')
        with self.assertRaises(FileExistsError):
            self.run_review()
        self.assertEqual(lock.read_text(), 'existing owner')
        lock.unlink()
        partial = directory / 'round-001.prompt.md'
        partial.write_text('preserve this')
        with self.assertRaisesRegex(ValueError, 'inspection/recovery'):
            self.run_review()
        self.assertEqual(partial.read_text(), 'preserve this')
        self.assertFalse(self.calls)

    def test_worktree_identity_change_is_rejected(self):
        first, _ = self.run_review()
        other = self.root / 'other-repo'
        other.mkdir()
        self.worktree = other
        with self.assertRaisesRegex(ValueError, 'another task/worktree'):
            self.run_review()
        self.assertTrue(Path(first['response']).exists())


if __name__ == '__main__':
    unittest.main()
