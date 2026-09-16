---
name: plan-feature
description: >
  Implementation-planning phase used by dev-workflow after a feature brief is
  complete. Maps approved success criteria to code changes, validation, and UI
  mockups before implementation begins.
disable-model-invocation: true
---

# Plan Feature

Require an Obsidian task record with `Status: planning`. Planning changes the
record and repository mockups only; do not modify product code.

## Plan

1. Read the complete brief, project instructions, relevant code, current diff,
   and existing conventions.
2. Use a subagent only for a concrete context gap, external question, material
   tradeoff, or independent plan review that should save time.
3. Map every success criterion to affected code or data flow, implementation
   slices, checks, and evidence.
4. Record the target environment, setup or seed data, user path, and screenshots
   required for validation. Resolve unknowns now; return to discussion when a
   product or scope decision remains.

## UI design and mockups

For SwiftUI work, load `swiftui-pro` and its relevant design and accessibility
references before designing or reviewing the plan.

Before approving a UI direction, evaluate:

- information hierarchy and the primary action;
- use of available space and content density;
- native iOS patterns and consistency with adjacent app screens;
- Dynamic Type, narrow devices, and adaptive layout;
- applicable empty, loading, error, disabled, and populated states.

For every UI change, add one repository file at
`mockups/<task-slug>/<change>.html`. It may contain multiple named states. Use a
primary target-device canvas and record adaptive behavior rather than creating a
mockup for every device.

Use intended copy, app colors, spacing, typography, assets, controls, and states.
Reuse the app design system and identify the Swift view and relevant tokens in a
short comment. Link the mockup from the Obsidian task record. The mockup is the
approved visual target; a fresh simulator render remains final proof.

## Build gate

Add an `## Implementation plan` section to the task record containing:

- affected flows and files;
- ordered implementation slices;
- success-criterion-to-validation mapping;
- validation commands, target environment, state setup, and visual states;
- linked mockups, risks, and decisions.

Present the implementation plan and every UI mockup. On approval, set
`Status: approved`. On requested changes, remain `planning`. Do not implement
until approved.
