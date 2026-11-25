# Integrating concurrent changes

Use the task's recorded remote and intended target branch (`origin/main` by
default), not whichever local branch happens to be checked out elsewhere.
The parent owns authenticated fetches and integration in the task's worktree.

## When to integrate

- Before a new worktree is created, fetch the target and start from its current
  remote-tracking revision. Record remote, target and base SHA. Respect a
  deliberately specified alternate base; do not silently change task lineage.
- During Planning, inspect affected callers, contracts, schemas/migrations and
  dependencies against that base. Note known concurrent work when available;
  do not assume other agents' unmerged work is present or predict future merges.
- Before final Build validation and UAT preparation, fetch and integrate the
  current target. Earlier integration is useful when overlapping changes land.
- Immediately before PR merge, fetch and check target freshness again. If the
  fetched target is not an ancestor of the candidate, integrate and revalidate
  before shipping; a clean PR conflict indicator alone is insufficient.

## How to integrate

Verify the owned worktree, feature branch and status first. Preserve task-owned
changes using permitted local checkpoints when necessary; never auto-stash,
discard, overwrite or commit unrelated work. Resolve an unsafe dirty-work
dependency before integration. Do not change another checkout or local main.
While blocked by unsafe dirty work, preserve the current phase and record the
blocker; resolving it does not revoke existing task authorization.

Default to merging the fetched remote target into the feature branch, preserving
published history; follow an explicit project rebase policy when applicable.
Do not force-push or rewrite another writer's branch. If already integrated,
skip a redundant merge. Missing fetch access is a blocker, not proof of freshness.

Inspect incoming changes since the previously integrated target, merge conflict
resolutions, and the combined behavior. Even a clean text merge can break API
consumers, data contracts, migration ordering, shared state or dependent flows.
Trace affected requirements and callers, diagnose failures and make necessary
in-scope compatibility repairs under existing Build authority. Update affected
plans/tickets and invalidate stale check evidence. Never resolve conflicts by
blindly keeping one side or removing another task's behavior.

Run affected regression/integration checks and the required project gate against
the combined candidate; rebuild/rerender where relevant. Record fetched target
SHA, resulting candidate SHA plus any dirty diff/artifact identity, incoming
impact, repairs and check results. A new source revision needs fresh validation,
even when existing user acceptance can be retained below.

## Acceptance after integration

Initial UAT remains required. After acceptance, a newer target or source SHA
alone does not revoke it or require shipping permission again.

- For unrelated incoming changes, or mechanical/compatibility repairs preserving
  accepted behavior, review the delta from the accepted candidate and record
  why the accepted criteria, interactions and visual states remain satisfied,
  with fresh evidence for affected paths. Retain the original acceptance and
  record its applicability to the new candidate; do not invent new user approval.
  Continue shipping automatically when all gates pass.
- If integration or fixes change an accepted outcome, interaction or visual
  state, or evidence cannot establish preservation, return the affected criteria
  for focused user UAT after Build validation. Carry forward unaffected criteria
  with evidence. A reported UAT failure requires new acceptance of the repaired
  behavior; tests alone cannot approve it.
- A new product/scope decision returns to Discussion. In-scope diagnosis, repair
  and technical replanning never need a separate "may I fix/ship?" question.

## Final merge race

Respect existing branch protection, required checks and configured merge queues.
Use combined-result checks/queue when available; do not change repository policy
as part of ordinary shipping. If the target advances while checks run, repeat
integration and affected validation unless the configured queue validates the
actual combined result. Without such enforcement, fetch immediately before
merge and record that this is a best-effort freshness check, not an atomic
guarantee. Do not retry indefinitely without progress; report a moving-target
blocker if a stable validated candidate cannot be reached.
