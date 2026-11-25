---
name: ship-feature
description: >
  Ship an accepted task through required checks, push/PR/merge, completion records
  and owned-worktree cleanup without asking again for shipping permission.
---

# Ship Feature

Require recorded UAT acceptance and `approved-to-ship`, `shipping` or
`awaiting-merge`. That acceptance grants commit/push/PR/merge authority, not
separate release/deployment authority. Follow
`../dev-workflow/references/integration.md` for before-gate integration, final
target freshness, required checks/queues and acceptance applicability.

1. Inspect approved scope and final diff. Prepare required changelog/docs, set
   `shipping` and commit only task files. Run every project-defined headless
   shipping gate before each push; never bypass a hook or silently ignore failure.
2. Push and open the PR automatically. Record commits, acceptance evidence,
   commands/results and PR. Wait for required remote checks; if none exist,
   successful local gates are the check evidence.
3. For failures needing code changes, use Build's silent diagnosis/fix/test loop
   under existing authority. Apply integration rules to retain acceptance for
   evidenced behavior-preserving repairs; changed/uncertain behavior needs focused
   UAT. New product decisions return to Discussion. Do not ask again merely
   because the source revision or main changed.
4. When gates and target-freshness requirements pass, merge without asking.
   Respect configured combined-result checks/queues. If pending work forces a
   stop, record `awaiting-merge` and the precise blocker; do not claim merge.
5. Verify merge preservation, then apply the record rules: resolve only this
   task, reconcile its queue and compact completion log, record checks/PR/merge,
   acceptance, limits and pending cleanup. Update group rollup without completing
   siblings or unshipped outcomes. Ship required missing repository docs through
   the same gates rather than leaving a stranded local commit.
6. Preserve assets/evidence and verify no writer/process still needs the worktree.
   Follow `../dev-workflow/references/working-copies.md` for safe cleanup, including
   squash/rebase preservation and dirty/ignored work. Never force-remove or delete
   another task's worktree. Report pending cleanup explicitly.

Report commit/PR/merge status and material check/cleanup limits. Never claim a
blocked or unaccepted step is complete.
