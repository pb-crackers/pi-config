---
name: uat-feature
description: >
  User acceptance phase used by dev-workflow after Build has prepared a fresh
  validated build. Presents the app in its required test state, records user
  approval, and returns failed work to implementation.
disable-model-invocation: true
---

# UAT Feature

Require `plans/<slug>/plan.md` with `Status: awaiting-uat`. The parent owns
product operation, evidence collection, and user questions.

## Validate

1. Confirm Build recorded the fresh build, target environment, state setup,
   commands, and required visual states.
2. Exercise each success criterion through the real user-facing path where
   practical, not only tests or code inspection.
3. Use roles as needed:
   - specialist `reviewer`: inspect a specific SwiftUI, accessibility, security,
     or platform concern;
   - `researcher` or `oracle`: resolve an unexpected external or technical
     question without making product decisions.
4. Subagents provide evidence only. Route every fix through `build-feature`.

## Visual and acceptance gate

For UI work, the fresh app must already be open in the planned state. Present
the captured screenshots and the running app, then ask the user to approve,
request changes, or state that they cannot verify it. Do not treat a build,
test, or screenshot as user approval.

Present every success criterion with its evidence and ask the user to confirm
the expected behavior.

- If approved, record approval and set the plan to `approved-to-ship`.
- If changes are requested, record the failed criterion, set the plan to
  `building`, return to `build-feature`, and repeat its review and UI
  validation loop.
- If the user cannot verify required behavior, leave the plan at `awaiting-uat`
  and report the blocker.

Ask whether to continue to `ship-feature` only after all required behavior and
visual states are approved.
