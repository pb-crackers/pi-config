---
name: dev-workflow
description: >
  Coordinate task discussion, researched engineering plans and tickets, autonomous
  implementation/testing, user acceptance and shipping. Supports --auto within
  confirmed scope; keeps canonical Obsidian records and isolated worktrees.
---

# Development Workflow

The parent owns user decisions, integration, records and final verification.
Load the active phase skill; load its references when their conditions apply.
Questions and reviews stay conversational unless the user requests tracked work.

## Preflight and records

Read project instructions, relevant code, Git status/branch and recent history.
Find the canonical repository and any existing task, working copy and outbox.
Before repository edits, create or resume the owned worktree under
[working-copy rules](references/working-copies.md); preserve dirty work.
Use [integration rules](references/integration.md) for a fresh remote base and
combined-candidate validation before UAT and merge.

Use the active Obsidian Sync vault at
`/Users/phillipdougherty/obsidian-vault/notes-synced/`. Read
[record rules](references/records.md) to resolve the project, selected queue,
canonical task and outbox. Capture, task transitions, UAT and completion update
only matching records. Do not migrate unrelated history. Load Ponytail full
for code changes; use the working-copy reference if delegating.

## Task hierarchy and routing

Broad requests may group distinct outcome-based tasks. Each task owns its brief,
engineering plan, criteria and acceptance; its tickets deliver narrow complete
outcomes. Engineering steps are not automatically tickets. Follow record rules
for grouping, stable paths, progressive reading and rollups.

Check `Record role` before phase status. A group coordinates linked tasks; open
only the selected/authorized task, not all siblings. Record any group-derived
authorization with its actual source and bounded scope in the selected task.

| Entry or state | Next skill |
| --- | --- |
| Record an idea/bug without starting work | `../capture-todo/SKILL.md` |
| Reported bug selected for investigation, or substantive diagnosis | `../debug-feature/SKILL.md` |
| New/unclear outcome or `discussing` | `../discuss-feature/SKILL.md` |
| `planning` | `../plan-feature/SKILL.md` |
| `approved` / `building` | `../build-feature/SKILL.md` |
| `awaiting-uat` | `../uat-feature/SKILL.md` |
| `approved-to-ship` / `shipping` / `awaiting-merge` | `../ship-feature/SKILL.md` |
| `done` | Report recorded outcome; finish only preserved pending cleanup |

## Decisions and authority

Normal Discussion ends with the user's confirmation of the intended task in chat.
Planning researches/designs the work and tickets; new product discoveries loop
back into Discussion. Normal initial Build requires plan approval. Confirmed
scope and an approval source belong in `Build authorization`; recover that
history on resume, never infer authority from status or an unrelated task.

Approved Build covers in-scope diagnosis, fixes, technical replanning, ticket
revisions and repeated checks without renewed permission, including manual mode.
Only unresolved product/scope decisions, missing access, an unresolvable blocker
or user pause/revocation interrupt execution. Internal technical detours do not
restart user approval. Do not lower criteria or expand scope to pass checks.

A reported bug uses RCA → Discussion → Planning → Build → UAT. Routine failures
inside authorized Build stay in its implementation/test loop; use Debug for
uncertain, repeated or broader failures. In that internal recovery context,
Discussion is needed only for unsettled product behavior/scope. A reported bug
or UAT defect routed to RCA uses the reported-bug path instead; existing repair
authority survives its scope conversation and does not require a new fix permit.

Initial UAT is the user's acceptance, not agent testing. UAT records one result
at a time, then reviews failures before routing fixes. After acceptance, apply
integration rules to retain evidenced unchanged acceptance or request focused
retesting. Successful UAT grants commit/push/PR/merge authority; separate release
or deployment still requires its own authority. Shipping completes automatically
after local and required remote gates pass.

## Autonomous mode (`--auto`)

Explicit `--auto` delegates a minor task through prepared human UAT. Record
`Execution mode: auto` and the actual authorization source; follow
[auto procedure](references/auto.md). The main agent establishes the narrowest
product-consistent interpretation, researches/designs the plan and uses a
task-specific headless Codex/Ponytail engineering review. Codex supplies technical
questions/findings, not product-completeness or permission verdicts. Resolve
ordinary gaps autonomously; consequential product uncertainty still needs the user.

Auto satisfies routine brief/plan gates within that bounded scope, including
ticket breakdowns and applicable mockups. Build runs silently to prepared UAT;
human acceptance and existing Shipping authority remain unchanged. Auto does not
authorize new product scope or extra tool permissions. Persist it on resume until
disabled; never infer it from a quoted flag or unrelated task.
