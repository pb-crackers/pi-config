---
name: plan-feature
description: >
  Research and design an agreed task in engineering detail, map dependencies and
  validation, and create discrete implementation tickets before Build approval.
---

# Plan Feature

Require an executable task in `planning`. Read its confirmed brief/RCA, active
criteria, decisions, relevant code/current diff and project conventions. Follow
`../dev-workflow/references/records.md`. Planning edits records and mockups,
not production code; use `prototype` for a bounded experiment when needed.

## Investigate before designing

Inspect existing capabilities, dependencies, callers, state ownership and data
contracts. Trace the entire affected flow and dependent behavior, including
compatibility, migrations and regression risks. Read
`../dev-workflow/references/integration.md` and record the target/base and
before-UAT/premerge integration checkpoints; future merges cannot be predicted.

Research relevant platform features, maintained open source and proven methods
before choosing custom machinery. Use current primary sources for unfamiliar
or consequential technical choices. Record selected reuse/custom approach,
credible alternatives, sources, fit/gaps, compatibility and integration cost.
Reuse valid prior research; scale new research to uncertainty. Resolve factual
unknowns or define focused experiments before committing to an approach.

If evidence changes intended behavior, challenges an agreed constraint or
exposes a missing product decision, explain the finding, affected requirement,
options and recommendation. Set `discussing`, use `discuss-feature`, update the
same brief and resume Planning after the decision. Pure technical refinements
remain here under existing authority. Do not defer discoverable questions to Build.

## Engineering plan

Explain HOW this task will work, with concrete names, contracts and examples.
Include only applicable details:

| Area | Design |
| --- | --- |
| Database | Tables/columns/types, defaults, relationships, constraints, indexes, access rules, migrations/backfills |
| APIs | Operations/endpoints, request/response shapes, validation, authentication/authorization, errors and consumers |
| App | Screens/components, interactions/navigation, state ownership, data flow and existing integration |
| Background work | Triggers, processing, retries, duplicates and failure handling |
| Compatibility | Affected callers, shared contracts, dependent changes and rollout implications |

Use project conventions; identify inconsistent patterns rather than copying
them blindly. Explain consequential engineering choices in plain language for
co-engineering. A file list or vague "update the flow" is insufficient; writing
every function in advance is unnecessary. Link diagrams/examples when helpful.

For UI work, follow the planning/mockup section of
`../dev-workflow/references/ui-verification.md`.

## Tickets and validation

Confirm the task is one coherent capability. If distinct task-level outcomes
emerge, resolve their boundaries in Discussion. Load `../ticket-feature/SKILL.md`
for multiple deliverables or work larger than a fresh implementation context;
small changes remain in the task. Review size, coverage and blockers internally.
Present ticket count, deliverables and dependencies within the existing plan
review, not ticket-by-ticket approval.

Map every success criterion to affected flows, implementation slices and checks.
Define the UAT cases from agreed behavior: stable IDs, requirement links, setup,
actions and expected results. Include relevant failure paths and visual states.
Build will prepare the candidate and evidence; user UAT is not a substitute for
automatable checks. Record commands, test environment/data and dependent and
whole-task integration checks.

## Build gate

Record one implementation plan containing the design, affected files/flows,
reuse evidence, ordered slices/tickets/blockers, criterion-to-check mapping,
UAT cases, mockups where applicable, risks and unresolved assumptions. Another
agent must be able to implement without inventing consequential behavior or
contracts. Resolve blocking questions; assign verification to nonblocking ones.

Normally present the detailed design and concise breakdown for user approval;
on approval set `approved` and continue to Build. Corrections remain `planning`.
Recorded `--auto` authorizes the plan within confirmed scope under dev-workflow's
rules. Before initial auto Build, follow `../dev-workflow/references/auto.md`
for the task-specific read-only Codex/Ponytail engineering-plan exchange. The
main agent resolves findings with evidence and owns the plan; reviewer agreement
is not product approval. Revisit that exchange for substantial design flaws,
not routine technical fixes. Missing/failed review is a blocker, not a skipped gate.
In-scope technical recovery under existing Build authorization
also returns directly to Build. Neither path skips design/readiness work or
represents an internal revision as newly user-reviewed.
