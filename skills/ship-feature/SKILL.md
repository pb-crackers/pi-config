---
name: ship-feature
description: >
  Shipping phase used by dev-workflow after UAT approval. Runs the project's
  headless gate, opens and merges a pull request automatically, and records
  completion.
---

# Ship Feature

Require an Obsidian task record with `Status: approved-to-ship`, `shipping`, or
`awaiting-merge` and recorded UAT approval. That approval grants the parent
shipping and merge authority; do not ask for either again.

1. Inspect the final diff and status; preserve unrelated work and confirm every
   approved criterion and visual state. Prepare approved repository changelog
   and documentation updates before the shipping commit so the PR includes them.
2. Set `Status: shipping`, commit only approved task files, and run every
   project-defined headless shipping command before each push, including any
   app-specific validation script named in project instructions. Do not open
   Device Hub merely to ship and never bypass a tracked hook.
3. When the gate passes, push and open the pull request without asking. Record
   the command, result, UAT approval, commits, and PR URL in the task record or
   outbox.
4. Wait for required remote checks. If none exist, the successful local gate is
   the build evidence. Never ignore a failed check without explicit approval.
5. If shipping uncovers a required code change or failed check, set
   `Status: debugging` and return to `debug-feature` for cause and impact
   assessment. Existing Build authority covers in-scope fixes/replanning without
   another fix-approval question; repeat Build validation and fresh user UAT
   before shipping a changed candidate. This never permits bypassing a gate.
6. When required checks pass, merge without asking. If checks are pending, wait;
   if the workflow must stop, set `Status: awaiting-merge` so a later invocation
   resumes here. Ask only when blocked. Release or deployment requires separate
   authority.
7. After merge, follow `../dev-workflow/references/records.md`. For `Type: bug`,
   move its active `bugs.md` row to the `bugs-log.md` table, preserving its
   priority, summary, reported date and canonical task link; add the actual
   resolved date and PR. For features/improvements, move the feature-index
   entry to `implementation-log.md` with completion evidence. A feature that
   passed through debugging remains a feature, not a new bug. Update only this
   task and matching row; preserve unrelated history. If required repository documentation remains,
   ship it through the same gate and a follow-up PR before marking the task
   `done`; do not strand a new local commit after merge. Otherwise set
   `Status: done` once completion records are reconciled.
8. After confirming merge preservation, record child-ticket completion and
   follow `dev-workflow`'s working-copy cleanup rules. Preserve external skill
   edits and needed evidence that are not in this PR. Leave owned worktrees
   before removing them; keep dirty, active, or unpreserved worktrees and report
   pending cleanup. Never use force removal or delete another task's branch.

Report the branch, commits, PR, checks, merge status, approval evidence, and any
remaining risk. Never claim completion for an unapproved or blocked step.
