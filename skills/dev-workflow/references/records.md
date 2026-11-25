# Project queues and task reports

Use the configured active vault and canonical project folder from dev-workflow.
These are indexes into task records, not additional copies of their reports.

## Resolve the project and offline writes

Use the active vault configured in dev-workflow, never a backup/former vault.
Derive the lowercase kebab-case slug from the canonical repository directory
(non-alphanumeric runs become hyphens), not a task worktree name. Reuse the one
vault project folder matching that normalized slug; ask if multiple match,
otherwise create it. Reuse its single `*-Features.md`, or create
`<slug>-Features.md` with Feature Ideas, Improvements, Brain Dump and Roadmap.
Keep small categories together; do not rename/split indexes without scope.
Use the queue/task/log layout below. Repository TODO/plan Markdown is legacy
history, not a second writable workflow source.

If the vault is unavailable, append every intended mutation to
`OBSIDIAN_OUTBOX.md` at the active task worktree root: timestamp, vault-relative
target path, operation and complete content. Repository writes require the
owned worktree, even for the outbox. On resume find the recorded worktree/outbox;
when access returns reconcile entries in order before further planning writes.
Preserve conflicting versions and ask when unsafe to merge. Delete the outbox
only after all entries are applied; a half-applied move is not complete.

| File | Purpose |
| --- | --- |
| `<project>-Features.md` | Open feature ideas, improvements, brain dump, roadmap |
| `bugs.md` | Active standalone bugs, one short table row each |
| `Tasks/<task-slug>.md` | Canonical report, investigation, plan, validation and history |
| `bugs-log.md` | Resolved bug rows with task link, resolved date and PR |
| `implementation-log.md` | Compact shipped-feature/improvement table linking to tasks |

## Groups, executable tasks and tickets

Use existing `Tasks/` paths, not a new tracker. A broad request containing
distinct outcomes may keep its original record as a lightweight coordination
group with `Record role: group` (separate from its existing Type). Executable
tasks omit that field or use `Record role: task`. Do not add group records for
ordinary single-task work or bulk-reorganize existing records without scope.

Group records preserve the original request, agreed included/excluded outcomes,
cross-task dependencies, applicable authorization sources and links to executable
tasks. They use `Status: tracking` while agreed tasks remain and `done` only
after all agreed outcomes have accepted, merged completion evidence. They do not
have their own implementation tickets, Build assignment or mandatory worktree.
Record intentional deferrals/cancellations explicitly with user authority; do
not disguise them as delivered outcomes. Group progress is a summary of linked
task evidence, not a second copy of task specs or invented phase transitions.

Each executable task stays at `Tasks/<task-slug>.md`, with optional
`Group: [[<group-slug>]]`, its own brief/design/criteria, phase, dependencies,
authorization and working copy when implementation starts. Group rows link to
the structure; executable tasks have their own matching queue rows. Tickets
remain at `Tasks/<task-slug>/<ticket-id>.md` with no queue row. Their engineering
steps/checklists are not additional tickets unless they deliver distinct outcomes.

Read the group summary and selected task, not every sibling. Do not migrate,
rename, delete or duplicate existing reports merely to adopt this hierarchy.
When deliberately splitting an existing record, preserve its original report,
type, dates and links, link the extracted tasks and put each requirement's
authoritative detail in one task. Preserve existing bug identity and priority;
splitting does not imply resolution or create duplicate bug reports.

Shipping a task completes only that task. Update its group's linked rollup,
leaving siblings untouched. A group is not shipped by association with one PR;
retain its active row until all agreed work is accounted for, then record the
aggregate completion and links without duplicating delivery log rows.

## Read progressively

Choose the queue for the work requested. Search an implementation/bug log by
title, date, PR or domain terms when past work is relevant; do not read whole
archives as routine preflight. A log row is a pointer, not a specification or
proof that every follow-up is complete.

Open the selected task's metadata, short record summary if present, and headings
first. Then read the sections needed: current scope, complete active plan and
criteria, applicable decisions/approvals, dependencies, validation or relevant
prior attempts. Follow child/evidence links only when needed. Read more whenever
an answer depends on it; context economy must not omit an active requirement,
constraint or approval boundary. Do not routinely ingest all historical sections,
all child tasks, raw logs, screenshots or archive contents.

For long records, maintain a short `Record summary` near the top with the current
outcome/status, completion PR/date when known, pointers to detailed sections,
and outstanding work or cleanup. Keep the full history below it, clearly
historical when superseded. Do not rename/move completed task files merely to
archive them; existing links must keep working.

## Active bug queue

```markdown
# Bugs

| Priority | Bug | Summary | Status | Reported |
| --- | --- | --- | --- | --- |
| P3 | Contact card overflow | Several linked properties expand the card | reported | 2026-11-18 |
```

Keep the summary to one meaningful sentence even after the title becomes a
task link. Never replace all explanatory text with a bare link. Use a task link
such as `[[Tasks/contact-card-property-overflow]]`; inside tables escape the
alias separator if using an alias (`\|`). Escape pipes and flatten newlines in
cells so pasted reports cannot corrupt table columns. Screenshots, long reports,
logs and implementation details belong in the task, not the queue.

Preserve user-assigned priority. Use `Untriaged` when none was supplied; do not
silently choose a P level or reprioritize. P0–P3 are scheduling priorities;
they are separate from workflow status. Recommend changes with impact evidence
and let the user decide. Use `YYYY-MM-DD` dates, preserving the original reported
date through edits, investigation and reopening. Do not invent a missing date.

## Capture and expansion

For a new bug, capture a plain-title row with `Status: reported`; a task file is
not required yet. If a long report cannot fit without losing details, preserve
it in a linked report-only task with `Status: reported` at capture time. Do not
create empty report files for one-line intake. Search for the same title/symptom or known task link before
adding a duplicate. Read only matching archived entries when checking whether
an issue is a reopen; do not load every completed report.

When the user selects the bug for investigation, create or reuse its one
`Tasks/<task-slug>.md` and replace the row's title with a link. Preserve the
original report verbatim in that task before shortening an existing description
in the queue. Record:

```markdown
# Bug title
Type: bug
Status: debugging
Priority: P3
Reported: 2026-11-18

## Original report
<the full original description, preserved>

## Expected behaviour
## Actual behaviour
## Reproduction
## History
```

Missing expected behaviour or reproduction stays unknown until established.
Debug adds its diagnosis and evidence to this same record, not a second report.
During an explicitly requested migration, a linked record may use `reported`
until investigation actually starts; reorganizing notes does not begin a fix.

After a task exists it owns the full report, current priority/status and dates;
the queue is its synchronized overview. Apply an explicit user edit in either
place to the task and matching row. If both copies conflict and intent is
unclear, preserve both and ask instead of choosing silently. On every phase
transition update the row to the task's recorded status. Before expansion, the
queue row itself is authoritative. Feature/improvement tasks stay in their
feature index even when a QA failure sends them through debugging. Child
implementation/decision tickets belong to the parent and have no queue row.

## Resolution and reopening

Create `bugs-log.md` with this table when first needed (or requested explicitly):

```markdown
# Resolved bugs

| Priority | Bug | Summary | Reported | Resolved | PR |
| --- | --- | --- | --- | --- | --- |
```

Only after required user acceptance and confirmed merge, move a standalone bug's
row from `bugs.md` into this log. Retain its priority, summary, reported date and
canonical task link; add the actual resolved date and PR when available. Set
the task to `done`, record `Resolved: YYYY-MM-DD` and the PR/completion evidence,
and synchronize the log from those values. Passing tests or awaiting UAT is
not resolution. An explicit dismissal/duplicate decision must be labelled as
such in task history; do not present an unimplemented dismissal as a shipped fix.

For an explicit reopen, preserve the previous resolved date, PR and evidence in
task history before moving its row back to `bugs.md`. Reuse the task and original
reported date; record the new report/reopen date and clear the current resolved
field. A reopened report starts as `reported` until investigation is requested.
Do not leave a duplicate current row in both queues or erase past resolution.

Features/improvements move from the feature index to `implementation-log.md`
after merge. Never create a bug row merely because a feature failed validation.

## Implementation log

Use one short row per shipped delivery, linking related parent tasks in the same
row when they shipped together. Do not duplicate rows for every child ticket.

```markdown
# Implementation log

| Completed | Work | Outcome | PR |
| --- | --- | --- | --- |
| 2026-11-18 | [[Tasks/photo-pipeline]] | Integrated durable photo processing | PR link |
```

`Completed` is the recorded completion date, `Work` links to canonical task
records, `Outcome` is one concise user-facing sentence, and `PR` links to the
merged change when available. Escape table pipes and keep cells on one line.
Do not invent a completion date/PR or claim unshipped work as complete.

Before writing or shortening a row, preserve the full completion details in its
task: acceptance, exact candidate/merge commits, checks/evidence, deployment
boundaries, limitations, cleanup and follow-ups. Keep the task `done` after
shipping and update its record summary; pending cleanup or a subsequent action
remains explicitly visible. Keep actionable follow-up pointers in the active
feature index when needed without reopening already shipped implementation.
Later cleanup updates belong in the task, not new paragraphs in the log.

When converting prose, first preserve every original detail in an appropriate
linked task and verify it before replacing the log. For a multi-task delivery,
put shared completion detail in the integration parent and link it from related
tasks rather than duplicating the narrative. Retain existing recorded dates,
PRs, statuses and task paths, and check known incoming section links before
removing old log headings. Do not rewrite unrelated history or create annual
archives until their size or a requested workflow actually warrants it.

## Candidate-specific UAT records

Adapt the resumable one-case-at-a-time pattern from
[GSD UAT](https://github.com/pb-crackers/gsd-nitty-gritty/blob/979843c0befc1de28a124a358abb8ad4de4cd4b6/templates/UAT.md)
to Obsidian and explicit user results; do not inherit automatic document commits.

Link the task's UAT record at `Tasks/<task-slug>/uat.md`; do not put test results
in queue rows. Planning defines case IDs, requirement links, setup, actions and
expected results. Build prepares the actual candidate and checks. UAT persists
responses one case at a time under `uat-feature`; no implicit Git commit is needed.
The canonical task retains the link, acceptance and eventual shipping evidence.

A compact record contains:
- Session state: `testing`, `review`, `awaiting-retest`, or `accepted`; active/next
  case; started/updated dates; source/dirty diff, integrated target and artifact ID.
- Case index: stable ID, feature/requirement, expected-result summary, latest
  result and tested candidate. Details/setup/steps live once under each case.
- Results: `pending`, `approved`, `failed`, `blocked`, `skipped`; user response
  verbatim, evidence and reason where relevant. Empty/ambiguous input is not pass.
- Failure review: agreed short correction/Debug/new-requirement route, linked
  task/ticket/RCA when appropriate, affected retest scope and user decisions.
- Attempt history: candidate, result, feedback and fix/retest evidence. Preserve
  prior failures and approvals instead of overwriting their history.

Resume the active case against its recorded candidate. On rebuild, record a new
candidate and reset only failed/affected cases to pending. Retain other acceptance
only with the integration reference's applicability evidence, not merely because
a case passed once. A diagnosed/fixed issue is not user-approved until retested.
Session `accepted` requires all required cases approved or explicit recorded
user scope adjustment; blocked/skipped/pending/failed never silently become pass.
UAT session state is separate from the task's workflow phase. Keep task
`awaiting-uat` during testing/review; repair routing updates its actual phase.

## Scoped migration and offline work

For a requested project migration, preserve all original reports, priorities,
dates, task paths and unrelated feature sections. Move active bugs into
`bugs.md`, resolved ones with evidence into `bugs-log.md`, and preserve detailed
descriptions in existing or report-only task records before shortening rows.
Leave a short Bugs link in the existing feature file so users and old links can
find the queue; never leave duplicate authoritative bug tables. Do not infer
resolution from a blank/missing field or split other feature categories by
default. Re-read before writing so concurrent note changes are not overwritten.

When offline, queue every intended row, task, log and index-link mutation in the
task worktree's `OBSIDIAN_OUTBOX.md`, with timestamp, target path, operation and
complete intended content. Do not treat one applied half as a completed move;
reconcile all parts under dev-workflow's conflict-preservation rules.
