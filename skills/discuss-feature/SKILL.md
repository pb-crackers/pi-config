---
name: discuss-feature
description: >
  Discussion phase used by dev-workflow for new or unclear work. Defines the
  product brief, success criteria, and visual states before implementation
  planning.
disable-model-invocation: true
---

# Discuss Feature

The parent owns user-facing decisions. Do not implement during this phase.

## Understand

1. Read the request, project instructions, existing task records, and relevant
   code.
2. Use roles as needed:
   - `scout`: map current behavior, affected flows, conventions, and tests;
   - `researcher`: consult authoritative sources when external behavior matters;
   - `oracle`: challenge a material product or architecture tradeoff;
   - `reviewer`: critique a risky or broad brief.
3. Read load-bearing files, resolve conflicting evidence, and ask only the
   remaining product, scope, naming, risk, or visual questions.

## Record

Create `plans/<slug>/plan.md` and link it from `TODO.md`. Record:

```markdown
# Feature name

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

## Completion
- PR:
- Merge:
- Changelog:
```

Keep the brief about outcomes and constraints, not implementation details.
When discussion starts from a captured todo, preserve its description.

## Planning gate

Present the outcome, scope, success criteria, and visual states. Ask whether
the user approves the brief for planning.

- On approval, set `Status: planning` and continue to `plan-feature`.
- On requested changes, revise the brief and ask again.
- On pause, leave `Status: discussing`.
