---
name: discuss-feature
description: >
  Discussion and planning phase used by dev-workflow for new or unclear work.
  Gathers local and external context, clarifies requirements, and creates one
  approved task plan with acceptance criteria before implementation.
disable-model-invocation: true
---

# Discuss Feature

The parent session owns this phase and all user-facing decisions.

## Understand

1. Read the request, relevant project instructions, and existing task records.
2. Load `pi-subagents` when delegation would improve understanding:
   - `scout`: map existing behavior, affected flows, conventions, and tests.
   - `researcher`: consult current authoritative sources only when external
     APIs, SDKs, standards, or platform behavior matter.
   - `oracle`: challenge a material architecture or technical tradeoff after
     context is gathered; keep it advisory.
   - `reviewer`: critique a large or risky plan before presenting it.
3. The parent reads load-bearing files, resolves conflicting evidence, and asks
   the user only the unanswered product, scope, naming, risk, or taste questions.

Skip subagents for small, obvious work. Run read-only context work in parallel
only when each child has a distinct question.

## Plan

Reuse the project's existing plan location. If none exists, create `plans/` and
use `plans/YYYY-MM-DD-<slug>.md`:

```markdown
# Feature name

Status: discussing
Created: YYYY-MM-DD

## Outcome

## Scope

### Included
### Excluded

## Acceptance criteria

- [ ] Observable behavior

## Visual approval

- [ ] List every user-visible state that must be approved, or `Not applicable`

## Validation

- Checks, user flows, builds, and evidence required

## Decisions

## Completion

- PR:
- Merge:
- Changelog:
```

Keep it succinct. Record outcomes and constraints, not speculative
implementation detail. When discussion starts from a captured todo, carry its
description into the outcome.

Update `TODO.md` so the item links to the plan while retaining its concise
description. If no task convention exists, create the minimal index described by
`dev-workflow`.

## Approval gate

Present the final outcome, scope, acceptance criteria, and validation plan. Ask
whether the user wants to approve it and continue to `build-feature`.

- On approval, set `Status: approved`.
- On requested changes, revise the plan and ask again.
- On pause, leave `Status: discussing`.

Do not implement during this phase.
