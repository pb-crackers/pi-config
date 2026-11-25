# Working copies and delegation


Follow [concurrent integration](integration.md) for remote-base
freshness, before-UAT integration, final merge checks and acceptance retention.
Fetch the intended target before creating new worktrees; do not start from a
stale local main. Record the remote, target branch and fetched base SHA.

For new repository-editing work, create a dedicated Git worktree and feature
branch from the intended base. Ordinary questions and read-only exploration do
not need one. Resume a recorded task in its existing worktree; do not nest a new
worktree on every invocation or phase transition. If the task depends on dirty
work elsewhere, identify that dependency and preserve it; do not silently omit,
copy, stash, reset, or commit it. Resolve an unsafe dependency with the user.

Record the canonical repository, base revision, absolute worktree path, branch,
and creation ownership. Check the path and branch before writes and Git actions.
Compare resolved paths so filesystem aliases do not create duplicate worktrees.
Use one writer per worktree; independent implementation writers need separate
owned worktrees. The parent integrates and verifies their changes. Worktrees
isolate files and branch checkouts, not databases, ports, or shared services:
use project-supported setup and isolated runtime resources when needed. Keep
secrets out of task records; preserve required ignored configuration and assets.

Keep the worktree through review and UAT. After confirmed merge, preserve
needed evidence and assets, confirm no process or agent still owns it, and
leave its directory before cleanup. Check tracked, untracked, and ignored work
and unmerged commits. Verify preservation against the recorded merged PR and
commits, including squash/rebase merges; ancestry alone is insufficient there.
If preservation is uncertain, retain the worktree and report what remains.
Remove only safe, task-owned worktrees with ordinary `git worktree remove`,
never force. Remove only owned local branches whose work is confirmed preserved;
never delete a default or another task's branch. Cleanup failure is recorded as
pending cleanup, not hidden behind a claim that all work is finished.


## Delegation


Default to the parent. Delegate only for a concrete context gap, implementation
slice, external question, or independent review that should reduce elapsed time.
Parallelize only independent bounded work. Do not launch subagents for simple
questions or ordinary discussion.

When delegating, load `pi-subagents` if available; otherwise use the current
environment's supported subagent tools and these ownership rules. Keep one
writer per worktree,
do not let ordinary children launch subagents, and give each child a bounded
assignment. Every implementation or review-fix writer must be explicitly told
to load and follow `ponytail` at full intensity in its own context.

If a run reports `running` without child activity or a live route, inspect it
once, then stop and relaunch it fresh rather than waiting indefinitely. The
parent inspects all changes and evidence directly. Authenticated remote commands
and hosted-service mutations remain parent-only.
