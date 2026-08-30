---
name: dev-workflow
description: >
  Development workflow for implementing, fixing, and refactoring code. Creates
  a feature branch, makes atomic Git commits, adds appropriate tests, uses the
  ponytail skill, and delegates scouting, implementation, or review to Pi
  subagents when useful.
---

# Development Workflow

Use this workflow for non-trivial development tasks. Keep the parent Pi session
as the decision-maker and use the smallest process that safely fits the task.

## Before editing

1. Read the relevant code and project instructions.
2. Inspect Git status, current branch, and recent commits.
3. Preserve existing uncommitted work. Never stash, discard, reset, or overwrite
   it without permission.
4. Load and follow the `ponytail` skill at full intensity.
5. If on the repository's default branch, create a branch named
   `feature/<short-description>`. Reuse an existing non-default feature branch
   unless the user asks for a new one. Ask before branching if the name is
   ambiguous or the working tree makes branching unsafe.
6. State the validation plan before making substantial changes.
7. Output a bulleted description of the feature as you understand it to confirm that you have it right, use markdown diagrams or otherwise to illustrate your understanding.

## Implementation

- Understand the whole affected flow before choosing the smallest fix.
- Add or update focused unit tests when behavior changes. Do not add tests for
  trivial changes or inflate coverage without a reason.
- Reuse existing helpers, patterns, dependencies, and test conventions.
- Make one logical change at a time.
- Commit each completed logical slice, including its tests, with a short,
  imperative commit message. Keep commits easy to revert or inspect.
- Run the narrowest useful test after each slice, then broader checks when the
  task warrants them.
- Do not amend, squash, rebase, push, merge, or rewrite history unless asked.
- Never commit credentials, generated junk, unrelated changes, or temporary
  files.

## Subagents

Use subagents when they reduce risk or save time, not for tiny edits:

- `scout`: map unfamiliar code, callers, and test conventions.
- `oracle`: advise when requirements, design, or tradeoffs are materially unclear,
  before or during implementation.
- `worker`: implement an approved, well-scoped task as the sole writer.
- `reviewer`: independently inspect the completed diff for correctness, tests,
  and unnecessary complexity.
- `researcher`: consult authoritative external documentation when local evidence
  is insufficient.

Keep the parent as decision-maker and one writer per worktree. Parallelize only
read-only work. Follow the `pi-subagents` skill when orchestrating subagents.
Escalate product, scope, architecture, merge, release, credential, and
destructive-action decisions to the user.

## Completion

Before finishing:

1. Run the required focused and broader checks.
2. Inspect the final diff and `git status`.
3. Confirm workflow-owned changes are committed and pre-existing changes remain
   untouched.
4. Report the branch, commits, tests run, and any remaining risks.
5. Leave pushing, merging, and release actions to the user unless explicitly
   requested.
