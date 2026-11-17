---
name: build-feature
description: >
  Implementation phase used by dev-workflow after an implementation or debug
  fix plan is approved. Builds the approved scope, reviews and validates it,
  and prepares the current candidate for UAT.
---

# Build Feature

Require an approved Obsidian implementation or debug plan. Set it to `building`
before implementation. Recorded `--auto` authorization under `dev-workflow`
satisfies plan approval within the confirmed scope.

## Implement

1. Read the complete task record, approved plan, affected flow, project
   instructions, and current diff.
2. For UI work, open every approved repository mockup linked from the task
   record and give those paths to any implementing writer.
3. Use the approved plan to guide each implementation slice and its checks;
   verify dependent behavior and flag any newly discovered impact or scope
   change before departing from the plan.
4. State the validation contract: success criteria, commands, user flows,
   required visual states, and evidence. Cover failure paths as well as success:
   validate inputs, handle API errors without hiding them, and show actionable
   user-facing error, retry, or empty states where applicable. Follow project
   naming and response conventions; for greenfield work, establish consistent
   API names and request/response/error shapes rather than inventing them per
   endpoint.
5. Load and follow `ponytail` at full intensity.
6. Use a writer only when delegation should save time. Every implementation or
   review-fix writer prompt must explicitly require that child to load and
   follow `ponytail` at full intensity in its own context.
7. Work only in the task's recorded worktree. Keep one writer per worktree;
   independent concurrent writers each need a separate owned worktree. The
   parent owns integration, scope, decisions, verification, and Git operations.

When child tickets exist, work only ready tickets in dependency order. Record
the writer's claim and path before edits. Validate each ticket's acceptance
criteria and record evidence before marking it `validated`; integrate delegated
work before releasing its dependants. Resume existing ticket state. After all
children pass, verify the entire parent goal and cross-ticket behaviour.

## Review and validation

Use a fresh-context reviewer before UAT when independent review is useful. Add a
specialist review only for a specific concern. Route accepted fixes through the
sole writer and re-review only substantial or high-risk fixes.

Run focused checks after logical slices and broader project-defined checks when
warranted. Keep builds and tests headless when interaction is unnecessary.

Test observable behaviour through existing public interfaces, using expected
results from requirements or independently worked examples. Avoid assertions
that reproduce the implementation and mocks of internal collaborators. Prefer
real local dependencies when practical; mock external boundaries as needed.
For fixes, show a check failing on the bug before the fix when practical, then
passing afterward. Record limits instead of claiming an unobserved red/green.
Use small implementation/check cycles; do not impose TDD or new tests on trivial
edits. Follow Ponytail's requirement for meaningful checks on nontrivial logic.

Review both implementation quality and fidelity to the agreed goal. Trace every
parent and ticket success criterion to the actual behaviour and evidence. Ask:
did we implement everything requested, is any implementation incorrect or
partial, and did we add anything unrequested? Report missing criteria and scope
additions separately from correctness, safety and project-convention findings.
Inspect connected callers and data flow, not just the diff. Independent review
is optional when it adds confidence; two parallel reviewers are not mandatory.

Before fixing a required-check failure or accepted review finding, follow
`dev-workflow`'s failure recovery: record the symptom, set `Status: debugging`,
and load `debug-feature` for diagnosis and impact assessment. Do not accumulate
small patches without reconsidering the cause. A clear local defect can take
the short diagnosis path. Under `--auto`, continue diagnosis, research,
replanning and Build without renewed plan approval within confirmed scope.
Reopen affected tickets, rerun the original scenario and dependent checks, and
remove temporary instrumentation. Follow the scope and stopping rules; never
present failed or incomplete validation as ready for UAT.

For iOS UI changes, create a fresh, dedicated simulator with a task-specific
name and the required device/runtime using `xcrun simctl`. Record its device ID
and that this task created it; never use a shared
or pre-existing simulator for this workflow. Keep it for UAT rather than
cleaning it up at Build handoff.

For every iOS UI change:

1. Load the installed `xcode-device-interaction` skill. With Xcode MCP available, start a
   workspace-backed session targeting the dedicated simulator's exact UUID;
   verify the returned UUID matches before installing or interacting.
2. Produce a fresh build from current source, install, and launch it with
   `DeviceInteractionInstallAndRun`. Repeat after source changes. If Xcode MCP
   is unavailable or authorization is declined, use the project's existing
   build/install path and an available simulator interaction surface, recording
   the fallback and any checks that could not be completed.
3. Configure required device conditions such as appearance, text size,
   accessibility, location, and orientation with supported tools, simulator
   settings, or Device Hub when available.
4. Prepare app data with an existing launch argument, environment variable,
   fixture, debug seed path, UI automation, or the normal user path.
5. Exercise changed user flows and required success/failure states. Use current
   hierarchy hit points for Xcode interactions and inspect the resulting
   screenshots, hierarchy, app state, and logs. Compare screenshots with the
   approved mockup. Route meaningful differences through diagnosis before
   editing, then repeat verification after fixes.
6. Prepare the first UAT state and expose the dedicated device in Simulator or
   Device Hub for direct user testing. End idle MCP interaction sessions and
   verify the app remains open in that state; if ending the session stops the
   app, relaunch the same candidate and restore the state before handoff.

Never edit product source or create alternate product behavior solely to force
a UAT state. Propose reusable debug-only seed support as separate approved scope
when repeated setup justifies it. If Build ends without a UAT handoff, end its
MCP interaction sessions, then shut down and delete only the dedicated simulator
it created using its recorded UUID.

## Handoff

1. Record commands, results, candidate build, source revision and uncommitted
   source changes, workspace, scheme, simulator UUID and creation ownership,
   device/runtime, conditions, state setup, evidence paths (screenshots,
   hierarchy, and logs where available), session closure, presentation surface,
   and limitations in the Obsidian task record or outbox. Preserve evidence
   needed for acceptance outside temporary session files before ending sessions.
2. Confirm all parent and child criteria and required integration checks pass.
   Record the implemented plan, criterion-to-evidence mapping, deviations and
   limitations, and concrete user UAT steps. Set the task to `awaiting-uat`.
3. Continue directly to `uat-feature`; do not ask whether to begin UAT.

Build validation is evidence, not user approval.
