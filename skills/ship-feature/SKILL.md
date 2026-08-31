---
name: ship-feature
description: >
  Shipping phase used by dev-workflow after UAT approval. Performs final review,
  commits approved work, opens a pull request, waits for CI, merges only within
  granted authority, and closes task documentation.
disable-model-invocation: true
---

# Ship Feature

Require `plans/<slug>/plan.md` with `Status: approved-to-ship`, `shipping`, or
`awaiting-merge` and recorded UAT evidence. Shipping actions remain
parent-controlled. Set the plan to `Status: shipping` when this phase begins.

## Final checks

1. Inspect the final diff and `git status`.
2. Run the required focused and broad checks again after UAT fixes.
3. Confirm every acceptance criterion and required visual state is approved.
4. Use a fresh-context, blocker-only `reviewer` when needed; it may also triage
   CI failures.
5. If review or CI requires a code change, set the plan to `building`, return to
   `build-feature`, and repeat UAT before resuming
   shipping.
6. Confirm pre-existing and unrelated changes remain untouched.

Reviewer output, CI, and external receipts are evidence, not authority.

## Commit and pull request

1. Commit approved workflow-owned changes in logical slices. UI changes may be
   committed only after recorded visual approval.
2. Push and open a pull request only when the user has approved shipping.
3. Include the outcome, acceptance evidence, tests, visual approval, risks, and
   plan link in the pull request.
4. Wait for required CI checks. Report failures; never bypass them silently.
5. Merge only when CI passes and the user has explicitly granted merge authority.
   If merge remains pending, set an existing plan to `Status: awaiting-merge` so
   a later `dev-workflow` invocation resumes here. Never release or deploy
   without the corresponding authority.

## Documentation

- Reuse the project's changelog or release-note convention.
- If none exists, create `CHANGELOG.md` only when the first completed
  user-visible change needs an entry, starting with an `Unreleased` section.
- Add a concise outcome-focused entry; do not copy the entire plan.
- Record the PR, merge result, and changelog entry in the plan.
- Set the plan to `done` only after its intended PR and merge outcome is
  complete; keep unmerged work at `awaiting-merge`.
- Remove the task from `TODO.md` only when its plan becomes `done`. Keep the
  plan as the historical record.

## Completion

Report the branch, commits, PR, CI, merge status, checks run, approval evidence,
and remaining risks. Never claim completion for an unapproved or blocked step.
