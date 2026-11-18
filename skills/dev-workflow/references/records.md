# Project queues and task reports

Use the configured active vault and canonical project folder from dev-workflow.
These are indexes into task records, not additional copies of their reports.

| File | Purpose |
| --- | --- |
| `<project>-Features.md` | Open feature ideas, improvements, brain dump, roadmap |
| `bugs.md` | Active standalone bugs, one short table row each |
| `Tasks/<task-slug>.md` | Canonical report, investigation, plan, validation and history |
| `bugs-log.md` | Resolved bug rows with task link, resolved date and PR |
| `implementation-log.md` | Shipped feature/improvement entries with task links |

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
