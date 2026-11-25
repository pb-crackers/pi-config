---
name: capture-todo
description: >
  Capture a named task, idea or bug in the project's Obsidian queue without
  starting Discussion, implementation or Git shipping.
---

# Capture Todo

Require a short name and description; ask only for missing meaning and derive
the slug yourself. Follow dev-workflow's vault location and
`../dev-workflow/references/records.md` to find the project and matching queue.
Check title/symptom, slug and existing task links to reuse an item instead of
creating a silent duplicate; clarify only ambiguous identity or intent.

Record features/improvements in the existing feature index. Bugs use the active
table with `reported`, supplied priority or `Untriaged`, and known reported date.
Keep one-line intake concise and unlinked until investigation; preserve longer
reports in linked report-only tasks when needed. Explicit reopen/update requests
follow record rules without another approval question.

Use the task-worktree outbox if the vault is unavailable. Show the exact captured
or queued entry and finish. Vault capture relies on Obsidian persistence/sync;
no Git commit/push, changelog, UAT or subagent run is needed. Perform a separate
explicitly requested Git action only within that authorization; never solicit
one just because a task was captured.
