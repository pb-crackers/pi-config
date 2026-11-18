---
name: capture-todo
description: >
  Todo intake phase used by dev-workflow. Accepts a required name and
  description and records a concise undiscussed item in the project's Obsidian
  feature index or dedicated active bug queue, without starting implementation.
---

# Capture Todo

Use this when the user wants to record an idea or bug without discussing or
building it yet.

## Input

Require:

- **Name:** a short human-readable title.
- **Description:** a concise explanation of the desired outcome or problem.

Ask for whichever value is missing. Derive a lowercase hyphenated slug from the
name; do not make the user provide one.

## Record

Read `../dev-workflow/references/records.md` and resolve the project through
`dev-workflow`. Route bugs to `bugs.md`; route ideas/improvements to their
section in the existing feature index. Keep a concise summary. A feature entry:

```markdown
- [ ] **Offline mode** (`offline-mode`) — Let users access saved content without a connection.
```

When the vault is unavailable, queue the complete update in
`OBSIDIAN_OUTBOX.md`. Keep each item on one line and preserve the user's meaning.
For bugs, use the active table schema with `reported` status, the supplied
priority or `Untriaged`, and the known reported date. Keep the title unlinked
until investigation creates a task; do not create an empty report file merely
to capture a one-line bug. Preserve full supplied details if they exceed a row,
using a report-only task as described in the record rules rather than losing text.

If the title/symptom, slug or task link already exists, reuse the matching entry.
Apply an explicitly requested update or reopen under the record rules without
another approval question. Ask only when the target or intended change is
ambiguous; never add a silent duplicate.

## Finish

Show the exact recorded or queued entry. If the user already authorized a
commit or push, act within that authority; otherwise ask once. Todo capture does
not require implementation, UAT, a changelog entry, or subagents.
