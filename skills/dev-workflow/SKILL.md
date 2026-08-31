---
name: dev-workflow
description: >
  Single entry point for discussing, planning, building, validating, and shipping
  development work. Routes each task through the smallest appropriate phase,
  preserves project state, uses Pi subagents when useful, and requires user
  approval at product, visual, UAT, and release gates.
---

# Development Workflow

Use this as the parent-controlled entry point. Do not duplicate the phase
instructions here; load only the phase needed for the task.

## Preflight

1. Read project instructions and the relevant code.
2. Inspect Git status, branch, recent commits, and existing task conventions.
3. Preserve uncommitted work. Never stash, discard, reset, or overwrite it
   without permission.
4. Load and follow `ponytail` at full intensity for code changes.
5. Identify the current task from the request, `TODO.md`, and any linked plan.
6. Before the first repository edit, create or reuse a non-default feature
   branch. Ask first when the working tree makes branching unsafe.

## Documentation convention

Reuse the repository's existing task system. Otherwise, create `TODO.md` when
the first idea is captured and `plans/` when the first discussed task needs a
durable plan.

`TODO.md` is a short index. Undiscussed ideas are plain slugs; discussed work
links to one plan file:

```markdown
## Needs discussion
- [ ] **Offline mode** (`offline-mode`) — Let users access saved content offline.

## Planned
- [ ] [Improve sign-in flow](plans/2026-03-13-improve-sign-in-flow.md) — Reduce failed and confusing sign-in attempts.
```

Each plan is the durable source of truth for outcome, scope, acceptance
criteria, visual approval, validation, decisions, and completion evidence.
Remove completed entries from `TODO.md`; do not turn it into an archive.

## Routing

Load the matching sibling skill with `read` and follow it in this parent
session:

| Task state | Skill |
| --- | --- |
| Capture a named idea and description | `../capture-todo/SKILL.md` |
| New, unclear, or `discussing` | `../discuss-feature/SKILL.md` |
| `approved` or `building` | `../build-feature/SKILL.md` |
| `awaiting-uat` | `../uat-feature/SKILL.md` |
| `approved-to-ship`, `shipping`, or `awaiting-merge` | `../ship-feature/SKILL.md` |
| `done` | Report the recorded outcome; do not restart work |

For a trivial, already-clear change, use a user-confirmed acceptance summary in
place of a plan and briefly state why a separate document is unnecessary.

## Gates

The parent must ask the user before crossing these boundaries:

1. Discussion → build: approve the plan and acceptance criteria.
2. Build → UAT: confirm implementation is ready for user validation.
3. UAT → ship: approve behavior and every changed visual state.
4. Ship → merge/release: confirm any authority not already granted.

After a gate is approved, continue with the next phase in the same workflow.
On a later invocation, resume from the plan's `Status` instead of repeating
completed phases.

## Subagents

When delegation is useful, load and follow `pi-subagents`. The parent owns
orchestration, user questions, decisions, and final verification. Use one writer
per worktree, prefer async runs, use fresh context for independent reviewers,
and never let ordinary children launch their own subagents. Subagent output,
CI, and review bots are evidence, not user approval or merge authority.
