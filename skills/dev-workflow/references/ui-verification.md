# Conditional UI and device verification

Read the relevant sections during UI Planning, Build and UAT. Non-UI work uses
its actual artifact/service and checks; no simulator, scheme or screenshot is
required when inapplicable. Existing project design and platform skills govern.

## Planning and mockups

For SwiftUI, load `swiftui-pro` and relevant design/accessibility references.
Review hierarchy/primary action, density, adjacent/native patterns, Dynamic Type,
narrow/adaptive layouts and applicable empty/loading/error/disabled/populated states.
For each UI change, create `mockups/<task-slug>/<change>.html` in the repository;
it may contain multiple named states. Use intended copy, colors, tokens, assets,
controls, spacing and typography. Identify the Swift view/tokens where applicable.
Use a target-device canvas and describe adaptive behavior, not a mockup per device.
Link it from the plan as the visual target; runtime renders remain final proof.

## Build craft and runtime checks

Read `../../unslop/SKILL.md` for the bounded craft review of changed UI: spacing,
color, icons, copy, type, layout, details, visuals and motion. Inspect actual
renders; if unavailable, record limits and use project checks. Preserve approved
mockups/direction, brand/copy/tokens, native conventions and accessibility over
Unslop's web defaults. Make only observed in-scope corrections; a new direction,
feature or brand choice returns to Planning/Discussion. Existing plan/auto
approval covers bounded craft repairs, not unsolicited redesign.

This pass does not authorize dependencies, generated media, unrelated site
snapshots or story videos. Record findings and useful before/after evidence
internally; diagnose defects proportionately, fix, rebuild/rerender and rerun
affected behavior/accessibility/visual checks. Its quick-render budget never
limits required validation. Automated evidence is not user acceptance.

For every iOS UI change:
1. Create a fresh task-owned simulator with `xcrun simctl`, required device/runtime
   and a task-specific name. Record UUID and creation ownership; never use a shared
   or pre-existing simulator. Worktrees do not isolate devices or runtime data.
2. Load `xcode-device-interaction`. When Xcode MCP is available, start a workspace-
   backed session targeting that exact UUID and verify the returned UUID before
   install/interaction. Fresh-build current source and install/launch using
   `DeviceInteractionInstallAndRun`; repeat after source changes. If unavailable
   or authorization declined, use the project's available build/install and
   interaction surface and record fallback/unchecked behavior.
3. Configure appearance, text size, accessibility, location and orientation as
   applicable. Prepare data via existing launch arguments/env, fixtures/debug
   seeds, UI automation or the normal path. Never alter product behavior merely
   to force a test state. Reusable seed support needs separate approved scope.
4. Exercise success/failure flows; use current hierarchy hit points, screenshots,
   app state and logs. Compare required states with mockups and repeat checks
   after meaningful corrections. Preserve evidence outside temporary sessions.
5. Prepare the first UAT state and expose the dedicated device in Simulator or
   Device Hub when available. Close idle MCP interaction sessions and verify the
   app stays open; relaunch the same candidate/state if session closure stops it.
   Keep the simulator for user UAT, not cleanup at normal Build handoff.

## UAT device continuity and cleanup

Confirm Build recorded workspace/scheme, candidate, UUID/ownership, environment,
state setup and visual evidence. Reuse its dedicated simulator and candidate.
If interaction is needed, load the device skill and target the recorded UUID.
Restore conditions/state through supported tools or the normal user path; do not
change product code to stage UAT. A closed interaction session alone is not stale.
A stale artifact or missing device returns to Build for preparation, validated
fresh candidate and fresh task-owned simulator; never substitute a shared device.

Keep the app available across individual UAT cases and recorded failures. Close
idle interaction sessions. At acceptance, or after failure review before edits/
rebuild, end remaining sessions and shut down/delete only the task-created
simulator by recorded UUID with `xcrun simctl`; record cleanup. If Build ends
without a UAT handoff, perform the same owned-device cleanup. Never delete a
shared/pre-existing device. If cleanup fails, report/retry and do not advance
to Shipping or a new Build with that failed cleanup unresolved.
