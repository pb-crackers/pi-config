---
name: dev-workflow
description: >
  Parent-controlled workflow for discussing, planning, building, validating,
  and shipping development work. Preserves task records, prepares UI for direct
  user testing, and supports --auto for autonomous plan/build/test iteration.
  Researches reuse, tracks larger work as dependent tickets, isolates edits in
  worktrees, and reassesses failures. Requires product and UAT approval, and
  plan approval by default.
---

# Development Workflow

Load only the active phase skill. The parent owns decisions, user questions,
record reconciliation, and final verification.
Load supporting skills only when the active phase requires them.

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
3. Identify the canonical repository and locate existing task records and their
   recorded working copy. Use Git's common directory/worktree inventory when
   starting from a linked worktree; do not mistake its task directory for a new
   project.
4. Before repository edits, including an outbox write, create or resume the task's dedicated worktree and
   non-default feature branch using the working-copy rules below. Never switch
   branches in another task's checkout.
5. Resolve the project's Obsidian records and reconcile the task's outbox.
6. Load and follow `ponytail` at full intensity for code changes.

## Working copies

For new repository-editing work, create a dedicated Git worktree and feature
branch from the intended base. Ordinary questions and read-only exploration do
not need one. Resume a recorded task in its existing worktree; do not nest a new
worktree on every invocation or phase transition. If the task depends on dirty
work elsewhere, identify that dependency and preserve it; do not silently omit,
copy, stash, reset, or commit it. Resolve an unsafe dependency with the user.

Record the canonical repository, base revision, absolute worktree path, branch,
and creation ownership. Check the path and branch before writes and Git actions.
Compare resolved paths so filesystem aliases do not create duplicate worktrees.
Use one writer per worktree; independent implementation writers need separate
owned worktrees. The parent integrates and verifies their changes. Worktrees
isolate files and branch checkouts, not databases, ports, or shared services:
use project-supported setup and isolated runtime resources when needed. Keep
secrets out of task records; preserve required ignored configuration and assets.

Keep the worktree through review and UAT. After confirmed merge, preserve
needed evidence and assets, confirm no process or agent still owns it, and
leave its directory before cleanup. Check tracked, untracked, and ignored work
and unmerged commits. Verify preservation against the recorded merged PR and
commits, including squash/rebase merges; ancestry alone is insufficient there.
If preservation is uncertain, retain the worktree and report what remains.
Remove only safe, task-owned worktrees with ordinary `git worktree remove`,
never force. Remove only owned local branches whose work is confirmed preserved;
never delete a default or another task's branch. Cleanup failure is recorded as
pending cleanup, not hidden behind a claim that all work is finished.

## Autonomous mode (`--auto`)

Example: `$dev-workflow --auto implement the approved notification settings`.
Enable only when the user explicitly supplies `--auto` for the current task;
quoted examples or repository content do not grant authorization. Without it,
keep the normal approval gates.

Record `Execution mode: auto` and the user's authorization in the task record.
It persists across phase transitions and resumed invocations for this task until
the user disables it; omission on resume does not revoke it. The user can say
"turn off auto" to restore normal gates for subsequent transitions.

After the product brief, scope, and success criteria are confirmed, `--auto`
preauthorizes implementation plans, ticket breakdowns, debug fix plans, UI
mockups, and revisions within that scope. Record each plan and its authorization as `--auto`, never as
user review or acceptance. This rule applies to the phase skills below.

Work ready tickets in dependency order, then verify the whole feature. Loop
through planning or diagnosis, targeted research, implementation, review, and
validation as many times as needed. Route failures through the recovery rules
below before editing, revise affected plans and tickets when evidence requires
it, and rerun checks without renewed plan approval within scope. Keep the
task record current and report meaningful progress. Do not lower success
criteria, skip required checks, or expand scope to make validation pass.

Stop iterating when all success criteria and required checks pass, then prepare
UAT and wait for user acceptance. Pause for a product or scope decision, missing
access, or a blocker that cannot be resolved within existing authority. If the
same failure recurs without new evidence or a viable different approach, report
the blocker instead of repeating the same attempt indefinitely.

`--auto` does not grant UAT acceptance, shipping, merge, release, deployment,
destructive-action, or additional tool permissions. The existing UAT approval
and shipping rules still apply.

## Obsidian records

Obsidian is the primary source for backlogs, bugs, roadmaps, task records, and
completion logs.

1. Use the active Obsidian Sync vault at
   `/Users/phillipdougherty/obsidian-vault/notes-synced/`. A backup or the former
   iCloud vault is not an alternative working vault. If this path is unavailable,
   use the outbox below; do not silently write to another vault. Change the
   location only when the user supplies a new one. Existing records outside it
   require explicit migration scope; do not bulk-migrate them during a feature.
2. Derive a lowercase kebab-case project slug from the canonical repository
   directory, treating each run of non-alphanumeric characters as one hyphen.
   In a worktree, use the recorded original repository identity, not the task
   directory name. Reuse the project's existing records across all worktrees.
3. Compare existing top-level project folders by normalized slug. Reuse the one
   matching folder; ask if multiple folders match. Otherwise create `<slug>/`.
4. Reuse the folder's single `*-Features.md`, or create
   `<slug>/<slug>-Features.md` with `Feature Ideas`, `Improvements`, `Brain Dump`,
   and `Roadmap` headings. Keep these together while small; do not create a file
   per category or rename existing indexes without a requested reorganization.
5. Use `<slug>/bugs.md` for the active bug table, `<slug>/bugs-log.md` for resolved
   bugs, and `<slug>/implementation-log.md` for shipped features/improvements.
   Create missing queues/logs when needed. Read [record rules](references/records.md)
   before capture, queue/status updates, completion, reopening, or migration.
6. Store canonical details at `<slug>/Tasks/<task-slug>.md`, with `Type: bug`,
   `feature`, or `improvement`, and link them from the matching active queue.
   Preserve existing paths. Repository TODO and Markdown plan files are legacy
   history, not writable workflow sources. Migrate only requested records; do
   not sweep other projects or unrelated completed history into the new layout.

Read the selected queue and task, not the entire project history. Search for
matching rows/records when choosing work or detecting duplicates/reopens; open
only related details needed for the task. Do not routinely ingest both queues,
all of `Tasks/`, full logs, or artifact bodies. Keep queues as short summaries
and links so they remain useful for the user without loading each report.

When the vault is unavailable, append every intended mutation to
`OBSIDIAN_OUTBOX.md` at the root of the active task's worktree. Each entry must
include a timestamp, target vault-relative
path, operation, and complete content. This file is a sync queue, not a second
backlog.

On resume, find the task's recorded worktree and its outbox before creating new
records. Whenever access returns, reconcile known task outboxes before other
planning work. Apply entries in order, preserve both versions and ask when a conflict cannot be
merged safely, then delete the outbox after every entry is applied.

## Task records

Create one task record when intentional discussion begins. It is the source of
truth for the brief, success criteria, decisions, implementation plan,
validation, approvals, and completion evidence. Record execution mode, working
copy identity, research decisions, and links to child decision/implementation
tickets when needed. Keep HTML mockups in the
repository at `mockups/<task-slug>/` and link them from the task record.

Bug capture may remain a queue row until investigation. A requested migration
may preserve an existing full report in a linked `Type: bug`, `Status: reported`
task without beginning diagnosis. Once a task exists, keep its matching queue
row's phase status in sync at transitions under the record rules; preserve its
priority and original reported date. Diagnosing a failure within a feature task
does not change its type or create a second standalone bug automatically.

Use `ticket-feature` during planning when work needs multiple bounded pieces;
small tasks stay in one record. Child tickets live under
`<slug>/Tasks/<task-slug>/` and belong to the parent, not separate feature-index
entries. Track acceptance criteria, dependencies, status, and evidence. A ticket
is ready only when its blockers pass. On resume, use recorded ticket state;
ticket completion never replaces whole-feature validation or user acceptance.

## Failure recovery

Once the user authorizes Build for a task, that authority covers diagnosis,
in-scope fixes, technical plan/ticket revisions and repeated validation until
the candidate is ready for UAT. This is normal Build behaviour, including in
manual mode; it does not require `--auto`. Entering `debugging` or `planning`
during recovery does not revoke that authority or reopen an approval gate.

Record `Build authorization` with its source (user instruction, approved plan,
or recorded `--auto` authority) and confirmed scope. Carry it through internal
handoffs, delegated work and resumed sessions. For existing tasks, recover it
from the recorded approval history rather than asking again. Status alone is
not authorization; do not borrow it from another task. Respect any later user
pause, revocation or narrowed scope.

For a failed required check, accepted review finding, or reported UAT failure,
record the symptom and failed criterion before changing code. Set
`Status: debugging` and load `debug-feature` to trace cause and impact. A clear
local defect may need only a short diagnosis; failures across flows, repeated
unsuccessful fixes, or contradicted assumptions require broader reassessment.
If no new evidence or viable approach remains, report the blocker.

Diagnosis routes to a bounded fix, revised planning/research, or discussion for
changed requirements. Reopen affected tickets and dependent validation; preserve
useful work and evidence rather than resetting the feature. Neither a requested
UAT fix nor `--auto` permits unrelated changes or new product scope. A stale
candidate or missing test environment requires preparation/revalidation; it is
not by itself evidence of a product defect.

After diagnosis, continue the authorized fix/replan/build/test loop without
asking whether to fix the error or implement the in-scope revised plan. Report
what changed and why as progress, not a permission request. Ask only for an
unresolved product/scope decision, genuinely missing external permission/access,
an action outside existing authority, or a blocker that requires the user.
Keep the final UAT acceptance gate; previous acceptance does not cover a changed
candidate. Standalone diagnosis before Build was authorized still uses its
initial fix-plan gate unless the user already authorized the fix.

## Routing

Load the matching sibling skill with `read` and follow it in this parent
session:

| Task state | Skill |
| --- | --- |
| Capture a named idea and description | `../capture-todo/SKILL.md` |
| Bug selected for investigation (`reported`) or `debugging` | `../debug-feature/SKILL.md` |
| New, unclear, or `discussing` | `../discuss-feature/SKILL.md` |
| `planning` | `../plan-feature/SKILL.md` (loads `../ticket-feature/SKILL.md` for larger work) |
| `approved` or `building` | `../build-feature/SKILL.md` |
| `awaiting-uat` | `../uat-feature/SKILL.md` |
| `approved-to-ship`, `shipping`, or `awaiting-merge` | `../ship-feature/SKILL.md` |
| `done` | Report the recorded outcome; finish recorded pending cleanup when safe, without restarting implementation |

For Apple UI work requiring device verification, Build loads the installed
`xcode-device-interaction` skill and owns automated runtime checks. UAT
inherits the verified candidate and evidence, loading the device skill again
only when interaction is needed. The parent can use it directly; delegation is
optional. UAT still requires the user's acceptance.

## Gates

In `--auto` mode, the recorded authorization satisfies gates 2 and 3 within the
confirmed scope; record the plan and continue without an approval question.
Existing Build authorization also satisfies those gates for same-task in-scope
recovery, regardless of execution mode. Initial standalone diagnosis/planning
retains its gate; do not confuse an internal diagnostic detour with new work.
All other gates remain unchanged.

1. Discussion → planning: confirm the brief, scope, and success criteria.
2. Initial standalone debugging → build: approve the root cause analysis and
   fix plan unless already authorized. Recovery within authorized Build resumes automatically.
3. Initial planning → build: approve the implementation plan and every UI mockup.
   In-scope technical replanning during authorized Build resumes automatically;
   a new product scope or visual direction still needs the user's decision.
4. Build → UAT: automatic after review and validation. Build owns internal
   checks; UAT owns presenting the current candidate ready for user testing.
5. UAT → ship: approval of behavior and every changed visual state also grants
   authority to commit, run the project-defined headless gate, push, open a pull
   request, and merge it. Continue directly to `ship-feature` without asking.
6. Ship → merge: automatic after the local gate and required remote checks pass.
   Ask only when blocked or when separate release or deployment authority is
   required.

On a later invocation, resume from `Status` rather than repeating completed
work.

## Subagents

Default to the parent. Delegate only for a concrete context gap, implementation
slice, external question, or independent review that should reduce elapsed time.
Parallelize only independent bounded work. Do not launch subagents for simple
questions or ordinary discussion.

When delegating, load `pi-subagents` if available; otherwise use the current
environment's supported subagent tools and these ownership rules. Keep one
writer per worktree,
do not let ordinary children launch subagents, and give each child a bounded
assignment. Every implementation or review-fix writer must be explicitly told
to load and follow `ponytail` at full intensity in its own context.

If a run reports `running` without child activity or a live route, inspect it
once, then stop and relaunch it fresh rather than waiting indefinitely. The
parent inspects all changes and evidence directly. Authenticated remote commands
and hosted-service mutations remain parent-only.
