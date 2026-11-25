---
name: ticket-feature
description: >
  Split a researched task plan into narrow complete Obsidian implementation
  tickets, checking size, dependencies and acceptance coverage during Planning.
---

# Ticket Feature

Use within Planning for one executable task, not a grouping record. Read the
confirmed brief, engineering design, research and criteria. Follow
`../dev-workflow/references/records.md`; child tickets have no separate queue row.

## Define the work graph

Each ticket has one narrow complete deliverable, independently demoable or
verifiable once its declared blockers pass. It must fit a fresh agent context
including relevant design, implementation and validation. Slice through every
layer needed for that outcome, not into "database", "API" and "UI" tickets.

Split separately useful outcomes with independent acceptance groups. Keep
supporting steps and relevant failure handling with the deliverable; do not
create a ticket per file, layer or edge case. A distinct capability needs a
task-boundary discussion, not a bigger ticket. No fixed ticket quota.

Make genuinely necessary preparation explicit. Wide mechanical migrations can
use expand → migrate bounded batches → contract, keeping intermediate changes
compatible. If batches cannot stay green independently, record the integration
branch and final integration gate rather than promising independent shipping.

Create/reuse `Tasks/<task-slug>/<ticket-id>.md` with stable IDs. Each records:
- Parent link, title, status and genuine blockers.
- One deliverable, demonstration, inclusions and excluded adjacent work.
- Parent criteria served and precise design/contract links; avoid copied specs.
- Concrete acceptance examples, validation setup/commands and evidence.
- Assigned writer/worktree/branch/ownership when claimed.

Map all parent criteria to ticket checks or explicit whole-task integration
checks. Check omissions, duplicates, cycles, missing blockers and accidental
scope growth. Present count, titles, deliverables and blockers in the plan;
existing plan/auto/recovery authority covers the breakdown, with no ticket gate.

## Execution state

Statuses: `pending`, `building`, `validated`, `blocked`. A ticket is ready only
when its blockers are validated against the current integrated candidate.
Record a single writer's claim before edits; independent concurrent writers
need owned worktrees. The parent integrates before releasing dependants.

Validate acceptance and record evidence before `validated`. On failure or
replanning, reopen only affected tickets and stale dependent evidence; preserve
stable IDs and useful completed work. All tickets passing still requires parent
integration checks, user UAT and merge. Keep queue/task state and offline changes
under the record rules.

Adapted from [Matt Pocock's to-tickets](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/to-tickets/SKILL.md).
