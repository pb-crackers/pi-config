---
name: dev-workflow
description: >
  Parent-controlled workflow for discussing, planning, building, validating,
  and shipping development work. Preserves task records, prepares UI for direct
  user testing, and requires approval at product, plan, UAT, and release gates.
---

# Development Workflow

Load only the active phase skill. The parent owns decisions, user questions,
record reconciliation, and final verification.

## Intent gate

Questions, reviews, and brainstorming stay conversational. Do not create a task
record, branch, edit, or subagent run unless the user asks to capture, debug,
plan, build, or ship work.

## Preflight

After work is requested:

1. Read project instructions, relevant code, Git status, branch, recent commits,
   and existing conventions.
2. Preserve uncommitted work. Never stash, discard, reset, or overwrite it
   without permission.
3. Resolve the project's Obsidian records and reconcile its outbox.
4. Before the first repository edit, create or reuse a non-default feature
   branch. Ask first when the working tree makes branching unsafe.
5. Load and follow `ponytail` at full intensity for code changes.

## Obsidian records

Obsidian is the primary source for backlogs, bugs, roadmaps, task records, and
shipped logs.

1. Inspect direct children of the platform's standard Obsidian documents
   location for `.obsidian`; do not recursively scan all iCloud files. Ask when
   multiple vaults are available.
2. Derive a lowercase kebab-case project slug from the repository directory,
   treating each run of non-alphanumeric characters as one hyphen.
3. Compare existing top-level project folders by normalized slug. Reuse the one
   matching folder; ask if multiple folders match. Otherwise create `<slug>/`.
4. Reuse the folder's single `*-Features.md`, or create
   `<slug>/<slug>-Features.md` with `Bugs`, `Feature Ideas`, `Improvements`,
   `Brain Dump`, `Roadmap`, and `Shipped Features` headings.
5. Store task records at `<slug>/Tasks/<task-slug>.md` and link them from the
   feature index. Repository TODO and Markdown plan files are legacy history,
   not writable workflow sources.

When the vault is unavailable, append every intended mutation to repository-root
`OBSIDIAN_OUTBOX.md`. Each entry must include a timestamp, target vault-relative
path, operation, and complete content. This file is a sync queue, not a second
backlog.

Whenever access returns, reconcile the outbox before other planning work. Apply
entries in order, preserve both versions and ask when a conflict cannot be
merged safely, then delete the outbox after every entry is applied.

## Task records

Create one task record when intentional discussion begins. It is the source of
truth for the brief, success criteria, decisions, implementation plan,
validation, approvals, and completion evidence. Keep HTML mockups in the
repository at `mockups/<task-slug>/` and link them from the task record.

## Routing

Load the matching sibling skill with `read` and follow it in this parent
session:

| Task state | Skill |
| --- | --- |
| Capture a named idea and description | `../capture-todo/SKILL.md` |
| Reported bug or `debugging` | `../debug-feature/SKILL.md` |
| New, unclear, or `discussing` | `../discuss-feature/SKILL.md` |
| `planning` | `../plan-feature/SKILL.md` |
| `approved` or `building` | `../build-feature/SKILL.md` |
| `awaiting-uat` | `../uat-feature/SKILL.md` |
| `approved-to-ship`, `shipping`, or `awaiting-merge` | `../ship-feature/SKILL.md` |
| `done` | Report the recorded outcome; do not restart work |

## Gates

1. Discussion → planning: confirm the brief, scope, and success criteria.
2. Debugging → build: approve the root cause analysis and fix plan.
3. Planning → build: approve the implementation plan and every UI mockup.
4. Build → UAT: automatic after review and validation. Build owns internal
   checks; UAT owns presenting the current candidate ready for user testing.
5. UAT → ship: approve behavior and every changed visual state.
6. Ship → merge: follow the authority and project-defined headless gate recorded
   in `ship-feature`; release or deployment still requires separate authority.

On a later invocation, resume from `Status` rather than repeating completed
work.

## Subagents

Default to the parent. Delegate only for a concrete context gap, implementation
slice, external question, or independent review that should reduce elapsed time.
Parallelize only independent bounded work. Do not launch subagents for simple
questions or ordinary discussion.

Load and follow `pi-subagents` when delegating. Keep one writer per worktree,
do not let ordinary children launch subagents, and give each child a bounded
assignment. Every implementation or review-fix writer must be explicitly told
to load and follow `ponytail` at full intensity in its own context.

If a run reports `running` without child activity or a live route, inspect it
once, then stop and relaunch it fresh rather than waiting indefinitely. The
parent inspects all changes and evidence directly. Authenticated remote commands
and hosted-service mutations remain parent-only.
