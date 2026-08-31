---
name: plan-feature
description: >
  Implementation-planning phase used by dev-workflow after a feature brief is
  complete. Maps approved success criteria to code changes, validation, and
  UI mockups before implementation begins.
disable-model-invocation: true
---

# Plan Feature

Require a complete discussion brief in `plans/<slug>/plan.md` with
`Status: planning`. Planning changes records and mockups only; do not modify
product code.

## Plan

1. Read the complete brief, project instructions, relevant code, current diff,
   and existing task conventions.
2. Use roles as needed:
   - `scout`: trace affected flows, callers, conventions, and tests;
   - `researcher`: answer an external platform, API, or standards question;
   - `oracle`: challenge a material technical tradeoff or risk;
   - `reviewer`: check that the plan covers the approved scope and success
     criteria.
3. Map every success criterion to affected code or data flow, implementation
   slices, checks, and the evidence that will prove it works.
4. Record the target environment, setup or seed data, user path, and screenshots
   required for validation. Resolve unknowns now; return to discussion when an
   unresolved product or scope decision remains.

## UI mockups

For every UI change, add one `mockups/<change>.html` file. It may contain the
multiple named screen states needed for that change.

Each mockup is a fixed canvas for the target device and uses the intended copy,
app colors, spacing, typography, assets, controls, and states. Reuse values
from the app design system. Add a short comment identifying the Swift view and
relevant tokens. The mockup is the approved visual target; a fresh simulator
render remains the final proof.

## Build gate

Update `plan.md` with an `## Implementation plan` section containing:

- affected flows and files;
- ordered implementation slices;
- success-criterion-to-validation mapping;
- validation commands, target environment, state setup, and required visual
  states;
- linked mockups, risks, and decisions.

Present the implementation plan and every UI mockup. On approval, set
`Status: approved`. On requested changes, remain `planning`. Do not implement
until approved.
