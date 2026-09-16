---
name: ship-feature
description: >
  Shipping phase used by dev-workflow after UAT approval. Runs the project's
  headless gate, opens and merges a pull request within granted authority, and
  records completion.
disable-model-invocation: true
---

# Ship Feature

Require an Obsidian task record with `Status: approved-to-ship`, `shipping`, or
`awaiting-merge` and recorded UAT approval. Shipping remains parent-controlled.

1. Inspect the final diff and status; preserve unrelated work and confirm every
   approved criterion and visual state.
2. Set `Status: shipping`, commit only approved task files, and run the
   project-defined build/test gate headlessly before every push. Do not open
   Device Hub merely to ship and never bypass a tracked hook.
3. Push and open the pull request within granted authority. Record the command,
   result, UAT approval, commits, and PR URL in the task record or outbox.
4. Wait for required remote checks. If none exist, the successful local gate is
   the build evidence. Never ignore a failed check without explicit approval.
5. If shipping uncovers a required code change, set `Status: building`, return
   to `build-feature`, and repeat UAT before shipping again.
6. Merge only with the authority defined by the active workflow. If pending,
   set `Status: awaiting-merge` so a later invocation resumes here. Release or
   deployment requires separate authority.
7. After merge, set `Status: done`, update the Obsidian feature index and shipped
   log, record completion evidence, and commit any remaining approved repository
   documentation through the same headless gate.

Report the branch, commits, PR, checks, merge status, approval evidence, and any
remaining risk. Never claim completion for an unapproved or blocked step.
