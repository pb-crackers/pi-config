---
name: discuss-feature
description: >
  Interview the user to turn a short request or diagnosed bug into discrete tasks,
  agreed behavior, scope and success criteria before engineering/ticket planning.
---

# Discuss Feature

Enter from dev-workflow for intentional work; do not implement here. Read the
request, selected task, applicable RCA, project instructions and relevant code.
Preserve task type/report and follow `../dev-workflow/references/records.md`.

## Interview

Treat a short summary as intake, not a specification. Briefly reflect what you
understand, then uncover missing requirements with focused questions. Ask in
dependency order, wait for answers, and use them to choose the next follow-up.
Offer options and recommendations with tradeoffs; explore implications and
contradictions rather than silently choosing product behavior.

Work through concrete starting conditions, actions and expected outcomes;
relevant rules, exceptions, visual/failure/recovery states; included/excluded
functionality; and observable success criteria. These are investigation areas,
not a questionnaire or required audience/problem statement. Keep the developing
scope visible in chat. Look up facts instead of asking the user to research them.

Use code inspection, targeted primary-source research or a bounded `prototype`
when evidence would change a product decision. Detailed engineering/reuse
research belongs in Planning. If the user is unsure, help compare options or
investigate rather than pressing for an arbitrary choice.

Separate distinct capabilities into tasks using the record rules; shared
infrastructure does not make different outcomes one task. Confirm which tasks
are included now. RCA informs the bug's intended correction and boundaries;
reuse settled expected behavior rather than restarting the interview from zero.

## Readiness and handoff

Continue until discrete task outcomes, behavior, boundaries and criteria are
clear enough for engineering design and ticket decomposition without invented
product requirements. Clarity, not elapsed time, question count or a completed
document, ends exploration. Reuse existing answers; assess supplied briefs by
that standard. Respect explicit requests to skip exploration while keeping any
blocking unresolved decisions visible. Technical unknowns may enter Planning
with an investigation path; unsettled product choices determining scope may not.

Summarize directly in chat: what we will build, included functionality/examples
and relevant visual/failure states, exclusions, decisions/tradeoffs, success
criteria, and engineering questions left for Planning. Keep it short enough to
review and specific enough to correct without opening a file. Ask the user to
confirm this understanding using the existing Discussion → Planning gate.

On confirmation, update the same task brief and set `Status: planning`; continue
to `plan-feature`. A group stays `tracking`; transition only selected confirmed
tasks. On corrections, revise the affected understanding. On pause, remain
`discussing`. Planning discoveries reopen only the affected decision, then
update the same brief and resume Planning.

Record decisions as they emerge, with agreed versus proposed/unknown clearly
separated. The canonical brief contains outcome, behavior/examples, scope,
rules, criteria, applicable visual states, decisions, assumptions/open questions
and useful research evidence. Keep documentation proportional; it records the
conversation and never substitutes for it.
