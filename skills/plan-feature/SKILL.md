---
name: plan-feature
description: >
  Implementation-planning phase used by dev-workflow after a feature brief is
  complete. Maps approved success criteria to code changes, validation, and UI
  mockups before implementation begins.
---

# Plan Feature

Require an Obsidian task record with `Status: planning`. Planning changes the
record and repository mockups only; do not modify product code.

Follow `../dev-workflow/references/records.md`: read the selected task/queue
entry, preserve its type, and synchronize that entry when phase status changes.
Replanning a bug does not move it into the feature backlog.

## Plan

Read `../dev-workflow/references/integration.md`. Verify the recorded remote
target/base and inspect cross-feature contracts and known concurrent changes.
Plan integration against current target before final validation/UAT and a
freshness check before merge; initial planning cannot predict later merges.

1. Read the complete brief, project instructions, relevant code, current diff,
   and existing conventions.
2. Use a subagent only for a concrete context gap, external question, material
   tradeoff, or independent plan review that should save time.
3. Map every success criterion to affected code or data flow, implementation
   slices, checks, and evidence. Trace callers, consumers, data contracts, and
   other dependent behavior before changing or removing anything; include
   necessary follow-up changes and checks. Report technical impacts as progress;
   take unresolved product/scope decisions to the user before implementation.
4. For new code, follow established project conventions. In a greenfield project,
   choose simple, consistent API names and request/response/error shapes before
   the first endpoint; define how failures are validated, reported, and shown
   to users. Do not copy inconsistent legacy patterns without questioning them.
5. Record the target environment, setup or seed data, user path, and screenshots
   required for validation. Resolve unknowns now; return to discussion when a
   product or scope decision remains.

## Reuse and decomposition

Read Discussion's research. Before committing to a design, inspect existing
project capabilities and dependencies, then investigate relevant platform facilities, maintained open
source and established methods. Research unfamiliar or consequential choices
using current primary sources. Explain how findings shaped the design: selected
reuse/custom approach, credible alternatives, fit/gaps, compatibility,
integration cost and limits, with source links. Reuse settled evidence when still applicable; straightforward
familiar changes do not require a new research project. Record assumptions and
the focused experiment needed to verify uncertain technical claims; use the
bounded `prototype` skill when an artifact is needed, not production code here.
If evidence invalidates an assumption, reconsider the approach before detailing
the implementation; do not quietly expand the approved scope.

## Engineering design and collaboration

Explain HOW the change will work before Build, with concrete names, shapes and
examples appropriate to its complexity. A file list or "update the flow" is not
a design. Include only the applicable details:

| Area | Design to record |
| --- | --- |
| Database | Tables, columns and types, relationships, constraints, defaults, indexes, access rules, and migration/backfill approach where needed. |
| APIs | Endpoints/operations, request and response shapes, validation, authentication/authorization, errors and affected consumers. |
| App | Screens/components, interactions/navigation, state ownership, data flow, and integration with existing behaviour. |
| Background work | Triggers, processing steps, retries, failure handling and duplicate handling where relevant. |
| Existing behaviour | Compatibility, dependencies, affected contracts and migration implications. |

Describe observable behaviour and business rules alongside these contracts.
Use small diagrams or worked examples when they clarify the design. Do not
prewrite every function or inflate a small change with irrelevant sections.

Present the engineering design in plain language for co-engineering: explain
meaningful choices and tradeoffs, show the relevant schema/API/state details,
and allow focused refinement before normal plan approval. A short progress
summary does not replace the recorded design. Keep unresolved engineering
questions visible; investigate factual answers and request user input on
consequential choices that existing requirements do not settle. Do not invent
user decisions, require a fixed number of rounds or add a second approval gate.
Explicit `--auto` and existing Build authority retain their rules below.

Return to Discussion only when a discovery changes intended behaviour, exposes
a missing product decision or challenges an agreed constraint. State the finding,
affected requirement, options and recommendation; set `Status: discussing` and
resolve that decision. Then update the same brief, design, affected tickets and
validation mapping before proceeding. Purely technical refinements that fit
the confirmed outcome stay in Planning under existing authorization.

## Implementation slices

For work too large for one bounded implementation session or with distinct
dependencies, load `../ticket-feature/SKILL.md` to create or revise Obsidian
implementation tickets. Keep trivial work in the parent record. Include ticket
coverage, dependencies, and final integration checks in the existing plan gate;
do not add another approval gate. During recovery, read the diagnosis, revise
only affected plans/tickets, and invalidate stale validation evidence.

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

- affected flows and files, dependent behavior, and required follow-up changes;
- the concrete engineering design and contracts described above;
- ordered implementation slices;
- reuse decision and cited research, linked tickets and their blocking edges;
- success-criterion-to-validation mapping;
- validation commands, target environment, state setup, and visual states;
- linked mockups, risks, and decisions.

Check readiness before using any authorization path below: could another agent
implement this without inventing consequential product behaviour or engineering
contracts? Every active success criterion needs a concrete acceptance example
and validation path. Resolve blocking questions, reconcile research with the
brief, and label remaining nonblocking assumptions with their verification
steps. `--auto` skips plan approval, not this design/readiness work.

For same-task recovery with existing `Build authorization`, record the revised
technical plan/tickets and in-scope mockup corrections under that authority,
set `Status: approved`, and resume `build-feature` without renewed approval,
including in manual mode. This does not approve a new visual direction or
product scope. Recover authorization from prior approvals on resume; do not
infer it solely from a status value or an unrelated task.

Otherwise, when the task has active `--auto` authorization under `dev-workflow`,
record the plan and every UI mockup as authorized by `--auto`, set `Status: approved`, and
continue directly to `build-feature`. Revisions within the confirmed scope use
the same authorization; unresolved product or scope decisions still need the user.

Otherwise, present the implementation plan and every UI mockup. On approval, set
`Status: approved`. On requested changes, remain `planning`. Do not implement
until approved.
