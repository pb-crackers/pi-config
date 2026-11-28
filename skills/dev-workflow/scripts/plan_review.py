#!/usr/bin/env python3
"""Deliver a task-specific planning review and resume only its recorded session."""
import argparse
import hashlib
import json
import subprocess
import uuid
from pathlib import Path


def review(task, worktree, context, ponytail):
    task, worktree, context, ponytail = (Path(p).resolve() for p in (task, worktree, context, ponytail))
    if not task.is_file():
        raise ValueError('Canonical task file is required')
    top = subprocess.run(['git', '-C', str(worktree), 'rev-parse', '--show-toplevel'],
                         capture_output=True, text=True, check=True).stdout.strip()
    if Path(top).resolve() != worktree:
        raise ValueError('Worktree must be the repository working root')
    packet, skill = context.read_text(), ponytail.read_text()
    if not packet.strip() or not skill.strip():
        raise ValueError('Task context and Ponytail skill must be nonempty')
    rules = (Path(__file__).resolve().parents[1] / 'references' / 'plan-review.md').read_text()
    directory = task.with_suffix('') / 'auto-review'
    directory.mkdir(parents=True, exist_ok=True)
    lock = directory / 'running.lock'
    with lock.open('x'):
        pass
    try:
        state_path = directory / 'session.json'
        state = json.loads(state_path.read_text()) if state_path.exists() else {}
        if not isinstance(state, dict) or not isinstance(state.get('round', 0), int):
            raise ValueError('Invalid review session state; inspect before retry')
        identity = {'task': str(task), 'worktree': str(worktree)}
        if state and any(state.get(k) != v for k, v in identity.items()):
            raise ValueError('Session belongs to another task/worktree; do not reuse it')
        session = state.get('session_id')
        if session:
            if not isinstance(session, str):
                raise ValueError('Invalid reviewer session ID')
            uuid.UUID(session)
        number = state.get('round', 0) + 1
        prefix = directory / f'round-{number:03d}'
        prompt_path = prefix.with_suffix('.prompt.md')
        if prompt_path.exists():
            raise ValueError('Existing round artifacts need inspection/recovery before retry')
        prompt = (f'{rules}\n\n## This invocation\nCanonical task: {task}\n'
                  f'Working root: {worktree}\nRound: {number}\n'
                  f'Ponytail source: {ponytail}\n\n'
                  '## Ponytail skill — apply at full intensity to engineering planning\n'
                  f'{skill}\n\n## Task-specific context and current plan\n{packet}\n')
        prompt_path.write_text(prompt)
        command = ['codex', 'exec', '-C', str(worktree), '-s', 'read-only',
                   '-c', 'approval_policy="never"']
        if session:
            command += ['resume', session]
        command += ['--json', '-']
        try:
            completed = subprocess.run(command, input=prompt, text=True, capture_output=True, timeout=300)
            stdout, stderr, code = completed.stdout, completed.stderr, completed.returncode
        except subprocess.TimeoutExpired as exc:
            def decode(value):
                return value.decode(errors='replace') if isinstance(value, bytes) else value or ''
            stdout, stderr, code = decode(exc.stdout), decode(exc.stderr) + '\nReviewer timed out.', -1
        except OSError as exc:
            stdout, stderr, code = '', str(exc), -1
        prefix.with_suffix('.events.jsonl').write_text(stdout)
        prefix.with_suffix('.stderr.log').write_text(stderr)
        events = []
        for line in stdout.splitlines():
            try:
                event = json.loads(line)
                if isinstance(event, dict):
                    events.append(event)
            except json.JSONDecodeError:
                continue
        starts = [e.get('thread_id') for e in events if e.get('type') == 'thread.started']
        ids = {value for value in starts if isinstance(value, str)}
        mismatch = (any(not isinstance(value, str) for value in starts)
                    or len(ids) > 1 or bool(session and ids and ids != {session}))
        returned = next(iter(ids)) if len(ids) == 1 else None
        if returned:
            try:
                uuid.UUID(returned)
            except ValueError:
                mismatch = True
                returned = None
        messages = [e['item']['text'] for e in events if e.get('type') == 'item.completed'
                    and isinstance(e.get('item'), dict)
                    and e['item'].get('type') == 'agent_message'
                    and isinstance(e['item'].get('text'), str) and e['item']['text'].strip()]
        success = (code == 0 and not mismatch and bool(session or returned) and bool(messages)
                   and any(e.get('type') == 'turn.completed' for e in events)
                   and not any(e.get('type') in ('error', 'turn.failed') for e in events))
        response_path = prefix.with_suffix('.response.md')
        response_path.write_text(messages[-1] if messages else '')
        state = dict(identity, session_id=session or returned, round=number,
                     context_sha256=hashlib.sha256(packet.encode()).hexdigest(),
                     status='responded' if success else 'failed', response=str(response_path))
        temporary = state_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(state, indent=2) + '\n')
        temporary.replace(state_path)
        return dict(state, artifacts=str(directory), exit_code=code), success
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('task', 'worktree', 'context', 'ponytail'):
        parser.add_argument('--' + name, required=True, type=Path)
    args = parser.parse_args()
    try:
        result, success = review(args.task, args.worktree, args.context, args.ponytail)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Plan review not completed: {exc}\n')
    print(json.dumps(result))
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
