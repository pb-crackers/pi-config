---
name: discuss-feature
description: >
  Discussion phase used by dev-workflow for intentionally started new or
  unclear work. Defines the product brief, success criteria, and visual states
  before implementation planning.
---

# Discuss Feature

Use only after `dev-workflow` intentionally enters tracked work. An ordinary
question or brainstorming request does not create a task record. The parent
owns user-facing decisions; do not implement during this phase.

## Understand

1. Read the request, project instructions, selected queue entry and linked task
   record, and relevant code. Do not load unrelated project queues/history.
2. Use a subagent only for a concrete context gap or material independent
   challenge that should save time.
3. Read load-bearing files, resolve conflicting evidence, and ask only the
   remaining product, scope, naming, risk, or visual questions.

## Clarify and research before choosing a solution

Understand the user's problem before committing to an implementation. Ask
focused rounds of questions in dependency order, with a recommended answer and
its tradeoff. Ask only questions whose prerequisites are settled; don't repeat
answered questions or turn a clear request into an exhaustive interview. Look
up factual answers yourself. The user decides product behaviour, priorities,
scope, and consequential tradeoffs; do not answer those on their behalf.

Before approving an approach, check existing project capabilities, installed
dependencies and platform facilities, then relevant maintained open source and
established patterns. Use primary sources: official docs, source repositories,
specifications and first-party APIs. Record citations, fit and gaps, integration
effort, and relevant compatibility, license and maintenance limits. Compare
reuse with the smallest custom solution; a dependency is not automatically
cheaper. Scale research to the decision, and revisit it when new evidence
invalidates an assumption. Do not build custom machinery merely because the
initial request described it that way.

For large uncertain efforts, keep a decision map in the parent task: destination,
resolved decisions with evidence, precise open questions and their blockers,
in-scope unknowns not yet specific enough to investigate, and excluded work.
Create linked decision tickets under `<task-slug>/` when a question needs a
separate investigation. Record type (research, prototype, or user decision),
question, dependencies, resolution and evidence; never mark an unanswered user
decision resolved by inference. Resolve enough of the map to plan executable
work; don't invent implementation tickets for an approach still undecided.

Use `prototype` only when a small UI or logic artifact would settle a specific
question. Record the question and verdict; stop when it is answered. Exploration
does not authorize production integration. Keep reusable domain definitions and
consequential decision rationale in existing project docs when appropriate,
without creating a glossary or ADR for every task.

## Record

Read `../dev-workflow/references/records.md`. Create or update the canonical
`<project>/Tasks/<slug>.md` through `dev-workflow` and link it from the matching
queue: bugs stay in `bugs.md`, features/improvements in the feature index.
Preserve an existing type and report; Discussion does not reclassify a bug or
create a second task. Keep the row's status in sync. When offline, queue all mutations in
`OBSIDIAN_OUTBOX.md`. Record:

```markdown
# Feature name

Type: feature
Status: discussing
Created: YYYY-MM-DD

## Outcome

## Scope
### Included
### Excluded

## Success criteria
- [ ] Observable behavior

## Visual states
- [ ] Every changed user-visible state, or `Not applicable`

## Decisions

## Research and reuse
- Candidates, sources, fit/gaps, and selection rationale:

## Open decisions
- Question, blockers, owner, and resolution/evidence:

## Completion
- PR:
- Merge:
- Changelog:
```

Keep the brief about outcomes and constraints, not implementation details. When
discussion starts from a captured item, preserve its description. Use
`Type: improvement` for improvements and preserve `Type: bug` for bug work.

## Planning gate

Present the outcome, scope, success criteria, and visual states. Ask whether the
user approves the brief for planning.

- On approval, set `Status: planning` and continue to `plan-feature`.
- On requested changes, revise the brief and ask again.
- On pause, leave `Status: discussing`.
