---
name: build-feature
description: >
  Implementation phase used by dev-workflow after a task plan is approved.
  Implements with one writer, focused tests, independent review, and a handoff
  to UAT without claiming user or visual approval.
disable-model-invocation: true
---

# Build Feature

Require an approved plan or a user-confirmed acceptance summary for a trivial
change. When a plan exists, set its status to `building` before implementation.

## Implement

1. Read the complete plan or acceptance summary, affected flow, project
   instructions, and current diff.
2. State the validation contract: acceptance criteria, commands, user flows, and
   evidence required.
3. Before choosing or writing the implementation, load and follow `ponytail` at
   full intensity. This is required for every build, not optional.
4. Load `pi-subagents` when delegation is useful:
   - `scout`: fill a specific remaining code-context gap.
   - `worker`: implement the approved scope as the sole writer.
   - `researcher`: resolve an unexpected external API or platform question.
   - `oracle`: advise when implementation exposes an unapproved architecture or
     scope tradeoff.
5. Prefer one async `worker` for non-trivial implementation. Pass it the
   `ponytail` skill explicitly, plus the plan path, scope, non-goals, validation
   contract, authority boundary, and required handoff. Every implementation and
   fix worker must follow Ponytail. It must report changed files, commands and
   exit codes, evidence, remaining work, and decisions needing approval.
6. Keep writes single-threaded. Parallelize only read-only work unless writers
   have intentionally isolated worktrees.

The parent inspects the worker's changes and remains responsible for decisions
and commits. Do not let a child commit, push, merge, release, or expand scope.

## Review loop

After implementation, use fresh-context `reviewer` agents when the change is
non-trivial. Keep the fanout proportional:

- correctness and regressions;
- tests and acceptance criteria;
- simplicity and maintainability;
- add security, accessibility, performance, or platform review only when
  relevant.

The parent keeps evidence-backed findings, rejects noise, and sends accepted
fixes to one worker. Re-review only substantial or high-risk fixes; stop instead
of polishing indefinitely.

## Tests and commits

- Run the narrowest useful check after each logical slice and broader checks when
  warranted.
- Add focused tests for changed behavior, not trivial edits or coverage theater.
- The parent may commit completed non-UI slices with short imperative messages.
- Leave UI implementation uncommitted until `uat-feature` records the user's
  visual approval.
- Never include credentials, generated junk, temporary reports, unrelated work,
  or pre-existing changes.

## Handoff

When implementation and internal review are ready:

1. Update validation evidence in the plan or acceptance summary.
2. When a plan exists, set `Status: awaiting-uat`.
3. Summarize what is ready and any known risks.
4. Ask whether to continue to `uat-feature`.

A passing build or reviewer result is not UAT or visual approval.
