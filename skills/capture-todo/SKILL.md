---
name: capture-todo
description: >
  Todo intake phase used by dev-workflow. Accepts a required name and
  description, creates or reuses the project's todo index, and records a
  concise undiscussed item without prematurely creating a feature plan.
disable-model-invocation: true
---

# Capture Todo

Use this when the user wants to record an idea or task without discussing or
building it yet.

## Input

Require:

- **Name:** a short human-readable title.
- **Description:** a concise explanation of the desired outcome or problem.

Ask for whichever value is missing. Derive a lowercase hyphenated slug from the
name; do not make the user provide one.

## Record

Reuse the project's existing task system. Otherwise create `TODO.md` with:

```markdown
# TODO

## Needs discussion

- [ ] **Offline mode** (`offline-mode`) — Let users access saved content without a connection.
```

Keep each item on one line. Preserve the user's meaning while collapsing
multiline descriptions into a concise paragraph. Do not create a plan yet.

If the slug already exists, show the existing entry and ask whether to update
its name or description; never add a silent duplicate.

## Finish

Show the exact recorded entry. If the user already asked to persist it, commit
and push within that authority; otherwise ask once before those Git actions.
When the item is later discussed, `discuss-feature` creates its plan, carries the
description forward, and replaces the plain entry with a plan link.

Todo capture does not require implementation, UAT, a changelog entry, or
subagents.
