---
name: build-feature
description: >
  Implementation phase used by dev-workflow after an implementation or debug
  fix plan is approved. Builds the approved scope, reviews and fixes it, and
  always prepares the current build for UAT.
disable-model-invocation: true
---

# Build Feature

Require an approved implementation or debug fix plan at
`plans/<slug>/plan.md`. Set it to `building` before implementation.

## Implement

1. Read the complete task record, approved plan, affected flow, project
   instructions, and current diff.
2. State the validation contract: success criteria, commands, user flows,
   required visual states, and evidence.
3. Load and follow `ponytail` at full intensity.
4. Use roles as needed:
   - `scout`: fill a remaining code-context gap;
   - `worker`: implement approved scope as the sole writer;
   - `researcher`: resolve an external API or platform question;
   - `oracle`: advise when implementation exposes an unapproved tradeoff;
   - `reviewer`: independently check the implementation against the plan.
5. Keep writes single-threaded unless writers intentionally use isolated
   worktrees. The parent inspects all changes and keeps commit, scope, merge,
   release, and product decisions.

## Review and validation loop

Before UAT, use a fresh-context `reviewer` to check the diff against the
implementation plan and success criteria. Add a specialist review when the
change warrants it. Keep evidence-backed findings, send accepted fixes to the
sole writer, and re-review only substantial or high-risk fixes.

Run the narrowest useful checks after each logical slice and broader checks
when warranted. Add focused tests for changed behavior, not trivial edits.

For every UI change, before entering UAT:

1. Produce a fresh build from the current source.
2. Install and launch it in the target environment.
3. Reset or seed the exact state recorded in the plan.
4. Navigate every changed state and capture clear screenshots.
5. Compare the rendered app to the approved HTML mockup, fix meaningful
   differences, and repeat this loop after each UI fix.
6. Leave the fresh app open in the prepared state for the user.

For iOS, use the project's Xcode scheme, the target simulator, and XCTest or
XCUIAutomation where needed to reach the planned state. A passing test or
Xcode build alone is not visual validation.

## Handoff

When the review and validation loop is complete:

1. Record commands, results, state setup, screenshots, and limitations in
   `plan.md`.
2. Set the plan to `awaiting-uat`.
3. Continue directly to `uat-feature`; do not ask whether to begin UAT.

A passing build, review, or internal visual comparison is not user approval.
