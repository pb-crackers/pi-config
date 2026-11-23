---
name: ticket-feature
description: >
  Decompose larger dev-workflow plans into dependent, verifiable Obsidian
  implementation tickets and check coverage before Build. Small tasks stay in
  their parent record. Use during planning or replanning, not ordinary chat.
---

# Ticket Feature

Read `dev-workflow` for the vault, canonical project, record and authorization
rules. Require a parent task in `planning`; do not change product code.
Preserve the parent's type and queue under
`../dev-workflow/references/records.md`; a bug's child tickets do not become
separate bug rows or feature entries.

1. Read the confirmed brief, research, resolved decisions, affected code and
   current plan. If a blocking product decision is unresolved, return it to
   discussion rather than inventing a build ticket around an assumption.
2. Split work into narrow but complete vertical slices: one coherent deliverable
   per ticket, demoable or verifiable on its own once declared blockers pass.
   Each must fit a single fresh agent context, including loading relevant design,
   implementation and validation; a long multi-context session is not the size
   limit. Cross every layer needed for that outcome. Avoid tickets that merely
   say "database", "backend", and "UI" or bundle independent capabilities.
   Keep genuinely necessary preparation explicit. For wide mechanical changes,
   use compatible expand/migrate/contract steps; when intermediate steps cannot
   stay green, record the integration branch and final gate instead of claiming
   they can ship independently.
3. Create or update `<project>/Tasks/<task-slug>/<ticket-id>.md`. Link every
   child from the parent with its title, status and blockers. Use stable IDs
   across replans and resume. Store the full details once, in the child.
   Carry the relevant engineering design/contracts into the child or link to
   precise canonical plan sections; do not duplicate shared designs. Identify
   which parent success criteria it serves and include concrete acceptance
   examples. A writer should not need to invent consequential behaviour or
   contracts to complete the ticket.
4. Map every parent success criterion to ticket acceptance criteria or an
   explicit whole-feature integration check. Check for omissions, duplicated
   work, cycles, nonexistent blockers and accidental scope additions. Dependencies
   must identify work genuinely needed before the ticket can start.
5. Review granularity before Build. Split separately useful/completable outcomes
   with independent acceptance groups. Keep supporting steps and relevant failure
   handling with their deliverable; do not turn every file, layer or edge case
   into a ticket. If it contains distinct task-level outcomes, return that boundary
   to Discussion. Check the complete graph's coverage, blockers and fresh-context
   size, then present count, titles, deliverables and blockers in the plan review.
   Correct the breakdown internally; no ticket-by-ticket approval. The existing
   plan approval, `--auto` or same-task recovery authority covers it.

Each child records:

```markdown
# Ticket title
Parent: [[../<task-slug>]]
Type: implementation
Status: pending
Blocked by: <stable ticket IDs, or None>

## Outcome
- One concrete deliverable and how to demonstrate it
## Scope boundaries
- Included behaviour and explicitly excluded adjacent work
## Parent criteria and engineering design
- Parent criteria served, relevant contracts/design links, and dependencies
## Acceptance criteria
- [ ] Concrete starting conditions, action and expected result
## Validation
- Commands, setup, and required evidence
## Working copy
- Assigned writer, absolute path, branch, and ownership when assigned
## Evidence
```

Statuses are `pending`, `building`, `validated`, and `blocked`. A pending ticket
is ready when its blockers are validated against the current candidate; use
`blocked` for an unresolved decision or external blocker and record the reason.
Only one writer may claim a ticket. Record the claim before editing and use the
task's assigned worktree; separate concurrent writers use separate worktrees.
The parent integrates their changes before treating downstream tickets as ready.

Build marks a child validated only when its acceptance checks pass and evidence
is recorded. On failure, reopen affected tickets and invalidate dependent
evidence; return parent status through `debugging` and `planning` as needed.
Do not reset unrelated completed work. Completing all children still requires
parent-level integration validation, UAT, and merge before the feature is done.
When the vault is unavailable, queue complete child and parent mutations in the
task worktree's `OBSIDIAN_OUTBOX.md` under `dev-workflow`'s rules.

These sizing rules adapt the vertical-slice and fresh-context guidance from
[Matt Pocock's to-tickets](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/to-tickets/SKILL.md).
Here, breakdown review stays within the existing planning gate.
