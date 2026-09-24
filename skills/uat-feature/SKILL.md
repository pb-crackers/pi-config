---
name: uat-feature
description: >
  User acceptance phase used by dev-workflow after Build validates the current
  candidate. Presents it in Device Hub in the required state, records user
  approval, and returns failed work to implementation.
disable-model-invocation: true
---

# UAT Feature

Require an Obsidian task record with `Status: awaiting-uat`. The parent owns the
running app, evidence, and user questions.

## Prepare

1. Confirm Build recorded the candidate build, source revision, dedicated
   simulator device ID, state setup, commands, and required visual states.
2. Confirm the candidate still matches current source. If the prepared session
   is missing or stale, return to Build for a fresh candidate and dedicated
   simulator; do not use a shared simulator.
3. Configure device conditions in Device Hub. Prepare app state through the
   project's existing runtime seed or automation mechanism, or the normal user
   path. Do not alter product source merely to stage UAT.
4. Leave the app open at the first required test state.

## Acceptance gate

Exercise each success criterion through the real user-facing path where
practical. Present every criterion with its evidence, the captured screenshots,
and the running app. Ask the user to approve, request changes, or state that
they cannot verify it. A build, test, review, or screenshot is not approval.

- If approved, first shut down and delete the dedicated simulator by its
  recorded device ID, removing its data. Record cleanup and approval, set
  `Status: approved-to-ship`, then load `ship-feature` and complete shipping
  through merge without another question.
- If changes are requested, shut down and delete the dedicated simulator by
  its recorded device ID, record cleanup and the failed criterion, set
  `Status: building`, then return to `build-feature` for a fresh simulator,
  validation, and UAT.
- If the user cannot verify required behavior, remain `awaiting-uat`, keep the
  simulator available, and report the blocker.

Never erase or delete a shared or pre-existing simulator. If cleanup fails,
report the blocker and retry; do not advance to shipping or a new Build with
that simulator left behind.

UAT approval grants authority to commit, run the project-defined shipping gate,
push, open a pull request, and merge after required checks pass. Those actions
belong to `ship-feature`, not UAT. Ask again only for a blocker, failed gate, or
separate release or deployment.
