---
name: uat-feature
description: >
  User acceptance phase used by dev-workflow after implementation. Exercises
  acceptance criteria, requires direct visual approval for UI changes, records
  evidence, and returns failed behavior to implementation.
disable-model-invocation: true
---

# UAT Feature

Require a plan with `Status: awaiting-uat`, or the user-confirmed acceptance
summary for a trivial change. The parent owns product operation, evidence
collection, and every question to the user.

## Validate

1. Exercise each acceptance criterion through the real user-facing path where
   practical, not only unit tests or code inspection.
2. Record commands, results, screenshots, logs, and limitations in the plan or
   acceptance summary.
3. Load `pi-subagents` when useful:
   - fresh-context `reviewer`: validate the diff against the acceptance criteria;
   - skill-specialist `reviewer`: inspect relevant SwiftUI, accessibility,
     security, or platform concerns.
4. Subagents may provide evidence but cannot approve behavior or visuals. Route
   every fix back through `build-feature`.

## Visual gate

For any changed visual or UI state, the parent must:

1. Produce a fresh build from the current source.
2. Install and launch the product in its target test environment.
3. Navigate through every changed state and interaction.
4. Capture clear screenshots of those states.
5. Present the evidence and ask the user to approve, request changes, or state
   that they cannot verify it.

For iOS, build with the project's Xcode scheme, boot the appropriate simulator,
install and launch the new app build, and use XCTest/XCUIAutomation when needed
to reach changed states. A successful Xcode build is not visual approval.

Do not commit UI implementation or report completion before approval. Repeat the
build and visual gate after every requested UI change.

## Acceptance gate

Present the acceptance criteria with evidence and ask the user to confirm the
expected behavior.

- If approved, record the approval and, when a plan exists, set
  `Status: approved-to-ship`.
- If changes are requested, record the failed criterion, set an existing plan to
  `Status: building`, return to `build-feature`, then repeat UAT.
- If the user cannot verify required behavior, leave an existing plan at
  `Status: awaiting-uat` and report the blocker.

Ask whether to continue to `ship-feature` only after all required behavior and
visual states are approved.
