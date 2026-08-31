---
name: dev-workflow
description: >
  Parent-controlled workflow for discussing, planning, building, validating,
  and shipping development work. Preserves task records, prepares UI for direct
  user testing, and requires approval at product, plan, UAT, and release gates.
---

# Development Workflow

Load only the active phase skill and keep the parent responsible for decisions,
user questions, and final verification.

## Preflight

1. Read project instructions, relevant code, Git status, branch, recent commits,
   and existing task conventions.
2. Preserve uncommitted work. Never stash, discard, reset, or overwrite it
   without permission.
3. Load and follow `ponytail` at full intensity for code changes.
4. Identify the task from the request, `TODO.md`, and linked task records.
5. Before the first repository edit, create or reuse a non-default feature
   branch. Ask first when the working tree makes branching unsafe.

## Task records

Keep `TODO.md` as a short index and create one task record at
`plans/<slug>/plan.md` when discussion begins. Every work item that reaches
planning, build, or UAT requires this record.

`plan.md` is the source of truth for the brief, success criteria, decisions,
implementation plan, validation, approvals, and completion evidence. UI work
keeps its HTML mockups in `plans/<slug>/mockups/`.

## Routing

Load the matching sibling skill with `read` and follow it in this parent
session:

| Task state | Skill |
| --- | --- |
| Capture a named idea and description | `../capture-todo/SKILL.md` |
| New, unclear, or `discussing` | `../discuss-feature/SKILL.md` |
| `planning` | `../plan-feature/SKILL.md` |
| `approved` or `building` | `../build-feature/SKILL.md` |
| `awaiting-uat` | `../uat-feature/SKILL.md` |
| `approved-to-ship`, `shipping`, or `awaiting-merge` | `../ship-feature/SKILL.md` |
| `done` | Report the recorded outcome; do not restart work |


## Gates

1. Discussion → planning: confirm the brief, scope, and success criteria.
2. Planning → build: approve the implementation plan and every UI mockup.
3. Build → UAT: automatic after the required review and validation loop. For UI,
   UAT begins only with a fresh build installed, launched, and prepared in the
   required test state.
4. UAT → ship: approve behavior and every changed visual state.
5. Ship → merge or release: confirm authority not already granted.

On a later invocation, resume from `Status` rather than repeating completed
work.

## Subagents

At every phase, consider the available subagent roles and use the smallest
appropriate set for the actual context gap, implementation work, review, or
external question. Do not treat task size as a reason to skip useful
subagents. The parent owns orchestration and user approval; child output, CI,
and review bots are evidence only.

Load and follow `pi-subagents` when delegating. Keep one writer per worktree,
prefer async work, use fresh context for independent review, and do not let
ordinary children launch their own subagents.
