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

1. Read the confirmed brief, research, resolved decisions, affected code and
   current plan. If a blocking product decision is unresolved, return it to
   discussion rather than inventing a build ticket around an assumption.
2. Split larger work into bounded pieces that each fit one implementation
   session and deliver independently verifiable behaviour through the required
   layers. Avoid tickets that merely say "database", "backend", and "UI".
   Keep genuinely necessary preparation explicit. For wide mechanical changes,
   use compatible expand/migrate/contract steps; when intermediate steps cannot
   stay green, record the integration branch and final gate instead of claiming
   they can ship independently.
3. Create or update `<project>/Tasks/<task-slug>/<ticket-id>.md`. Link every
   child from the parent with its title, status and blockers. Use stable IDs
   across replans and resume. Store the full details once, in the child.
4. Map every parent success criterion to ticket acceptance criteria or an
   explicit whole-feature integration check. Check for omissions, duplicated
   work, cycles, nonexistent blockers and accidental scope additions. Dependencies
   must identify work genuinely needed before the ticket can start.
5. Present the breakdown as part of the implementation plan. The normal plan
   approval or recorded `--auto` authorization covers it; no separate gate.

Each child records:

```markdown
# Ticket title
Parent: [[../<task-slug>]]
Type: implementation
Status: pending
Blocked by: <stable ticket IDs, or None>

## Outcome
## Acceptance criteria
- [ ] Observable behaviour
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
