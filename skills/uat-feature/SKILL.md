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

1. Confirm Build recorded the candidate build, source revision, target
   simulator, state setup, commands, and required visual states.
2. Confirm the candidate still matches current source. If the prepared session
   is missing or stale, rebuild as needed, install, and launch the target
   simulator in Device Hub.
3. Configure device conditions in Device Hub. Prepare app state through the
   project's existing runtime seed or automation mechanism, or the normal user
   path. Do not alter product source merely to stage UAT.
4. Leave the app open at the first required test state.

## Acceptance gate

Exercise each success criterion through the real user-facing path where
practical. Present every criterion with its evidence, the captured screenshots,
and the running app. Ask the user to approve, request changes, or state that
they cannot verify it. A build, test, review, or screenshot is not approval.

- If approved, record approval and set `Status: approved-to-ship`.
- If changes are requested, record the failed criterion, set `Status: building`,
  return to `build-feature`, and repeat validation and UAT.
- If the user cannot verify required behavior, remain `awaiting-uat` and report
  the blocker.

Ask whether to continue to `ship-feature` only after all required behavior and
visual states are approved. Do not commit, push, open a pull request, merge, or
run shipping-only gates during UAT.
