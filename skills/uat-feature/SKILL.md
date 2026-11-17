---
name: uat-feature
description: >
  User acceptance phase used by dev-workflow after Build validates the current
  candidate. Presents the running app in the required state, records user
  approval, and returns failed work to implementation.
---

# UAT Feature

Require an Obsidian task record with `Status: awaiting-uat`. The parent owns the
running app, evidence, and user questions.

Apply simulator/session requirements and cleanup only to iOS UI candidates.
For other work, verify the current artifact or running service and its recorded
checks; do not require a simulator, scheme, or screenshot when inapplicable.

## Prepare

For every candidate, confirm Build recorded the artifact/build, source revision
including uncommitted changes, applicable setup, commands, criterion evidence,
limitations, and user test steps. Confirm it matches current source; if stale,
return to Build for fresh validation before acceptance. Present the artifact or
running service in the required state.

For iOS UI candidates, additionally:

1. Confirm Build recorded the workspace, scheme, dedicated simulator UUID and
   creation ownership, conditions, state setup, and required visual states.
2. Confirm the candidate still matches current source. If the candidate is stale
   or the dedicated simulator is missing, close remaining interaction sessions,
   clean up any surviving task-created simulator, and return to Build for a
   fresh candidate and dedicated simulator; do not use a shared simulator.
   A closed MCP interaction session alone does not invalidate the candidate.
3. Reuse the dedicated simulator and Build evidence. If automation is needed,
   load the installed `xcode-device-interaction` skill and reopen a session targeting its
   exact UUID. Restore required conditions and app state through supported tools,
   existing runtime seed or automation, or the normal user path. Do not alter
   product source merely to stage UAT. If a rebuild is needed, return to Build
   for validation of that candidate before acceptance.
4. Leave the app open at the first required test state in Simulator or Device
   Hub when available. End idle interaction sessions and confirm the app remains
   available; restore the same candidate and state if necessary. Tell the user
   which simulator to use and provide the test steps and expected results.

## Acceptance gate

Exercise each success criterion through the real user-facing path where
practical. Present every criterion with its evidence, the captured screenshots,
and the running app when applicable, or the actual non-app artifact. Ask the
user to approve, request changes, or state that
they cannot verify it. A build, test, review, or screenshot is not approval.

Summarise the implemented plan, reused solutions, validated tickets, final
integration checks, and deviations/limitations. Give concrete test steps and
expected results. For non-app work, present the actual artifact and appropriate
verification steps; simulator-specific requirements apply only to iOS UI work.

- If approved, record the user's acceptance for this exact candidate. For iOS
  UI, end remaining MCP interaction sessions, then use `xcrun simctl` to shut
  down and delete the task-created dedicated simulator by its recorded UUID,
  removing its data, and record cleanup. Set `Status: approved-to-ship`, then
  load `ship-feature` and complete shipping through merge without another question.
- If changes are requested, record the failed criterion. For iOS UI, end remaining
  MCP interaction sessions, shut down and delete the task-created dedicated
  simulator by its recorded UUID with `xcrun simctl`, and record cleanup. Set
  `Status: debugging`, then load `debug-feature` to assess the cause and affected
  dependencies before edits. Reopen affected tickets and invalidate stale
  evidence. Diagnosis may choose a bounded fix, renewed research/planning, or
  discussion for a changed requirement. Rebuild and validate before new UAT;
  prior acceptance never applies to a changed candidate.
- If the user cannot verify required behavior, remain `awaiting-uat`, keep the
  candidate available, end idle interaction sessions if any, and report the blocker.

Never erase or delete a shared or pre-existing simulator. If cleanup fails,
report the blocker and retry; do not advance to shipping or a new Build with
that simulator left behind.

UAT approval grants authority to commit, run the project-defined shipping gate,
push, open a pull request, and merge after required checks pass. Those actions
belong to `ship-feature`, not UAT. Ask again only for a blocker, failed gate, or
separate release or deployment.
