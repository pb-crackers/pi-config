---
name: build-feature
description: >
  Implementation phase used by dev-workflow after an implementation or debug
  fix plan is approved. Builds the approved scope, reviews and validates it,
  and prepares the current candidate for UAT.
disable-model-invocation: true
---

# Build Feature

Require an approved Obsidian implementation or debug plan. Set it to `building`
before implementation.

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
7. Keep writes single-threaded unless independent writers intentionally use
   isolated worktrees. The parent owns scope, decisions, verification, and Git
   operations.

## Review and validation

Use a fresh-context reviewer before UAT when independent review is useful. Add a
specialist review only for a specific concern. Route accepted fixes through the
sole writer and re-review only substantial or high-risk fixes.

Run focused checks after logical slices and broader project-defined checks when
warranted. Keep builds and tests headless when interaction is unnecessary.

For iOS UI changes, create a fresh, dedicated simulator with a task-specific
name and the required device/runtime. Record its device ID; never use a shared
or pre-existing simulator for this workflow. Keep it for UAT rather than
cleaning it up at Build handoff.

For every iOS UI change:

1. Produce a fresh build from current source.
2. Install and launch it in the dedicated simulator, using Device Hub for
   interactive simulator validation.
3. Configure device conditions such as appearance, text size, accessibility,
   location, and orientation in Device Hub.
4. Prepare app data with an existing launch argument, environment variable,
   fixture, debug seed path, UI automation, or the normal user path.
5. Navigate every changed state, capture screenshots, and compare them with the
   approved mockup. Fix meaningful differences and repeat after UI fixes.

Never edit product source or create alternate product behavior solely to force
a UAT state. Propose reusable debug-only seed support as separate approved scope
when repeated setup justifies it. If Build ends without a UAT handoff, shut down
and delete only the dedicated simulator it created.

## Handoff

1. Record commands, results, candidate build, simulator device ID, state setup,
   screenshots, and limitations in the Obsidian task record or outbox.
2. Set the task to `awaiting-uat`.
3. Continue directly to `uat-feature`; do not ask whether to begin UAT.

Build validation is evidence, not user approval.
