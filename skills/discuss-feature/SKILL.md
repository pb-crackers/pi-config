---
name: discuss-feature
description: >
  Discussion phase used by dev-workflow for intentionally started new or
  unclear work. Collaboratively defines the intended functionality, scope,
  success criteria and visual states in conversation before implementation planning.
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

Make this a collaborative conversation. Start with a short reflection of what
you understand the user wants and the meaningful gaps to explore. Ask a small,
focused set of questions with options and recommendations, then wait for the
answers before treating those choices as settled. Respond to the answers:
explain implications, challenge conflicting requirements and walk through
concrete behaviour together. Surface consequential assumptions as proposals,
not decisions silently made on the user's behalf.

Let the exchange follow the uncertainty, without a minimum duration or number
of rounds. Reuse answers already given; a complete supplied brief or an explicit
request to skip exploration does not need a manufactured interview. Keep the
intended functionality and scope visible in chat as understanding develops.

Ask questions in dependency order once their prerequisites are settled and
look up factual answers yourself. The user decides product behaviour,
priorities, scope and consequential tradeoffs.

Describe the intended end-to-end experience: starting conditions, actions,
observable results and resulting state. Work through concrete examples, business
rules, constraints, included/excluded behaviour and relevant loading, empty,
error, retry, cancellation and recovery states. Scale this to the change;
skip irrelevant categories rather than inventing requirements. Distinguish
confirmed decisions, proposed assumptions and unresolved questions. Do not
require an audience description or problem statement.

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

## Separate outcomes before implementation tickets

Check whether a broad request contains capabilities with distinct behaviour,
rules, acceptance criteria or priorities. For example, "add logging" may mean
error monitoring and product usage analytics: separate tasks sharing a request,
not one oversized implementation ticket. Shared infrastructure alone does not
make them one task. Keep a genuinely coherent small request together.

Present the proposed task boundaries, included outcomes, dependencies and
exclusions within the existing brief confirmation. When the request is split,
retain its original description in a lightweight group and create/reuse linked
task records under the record rules. Each task owns its brief and success
criteria; decide detailed implementation tickets in Planning. Do not infer
that decomposition authorizes building every task or reclassify existing bugs.

## Record

Capture decisions as they emerge and keep documentation proportional to the
work. Avoid producing speculative documents ahead of the conversation. The
brief preserves shared understanding; the user should not need to open it to
understand what is proposed or correct the scope.

Read `../dev-workflow/references/records.md`. Create or update the canonical
`<project>/Tasks/<slug>.md` through `dev-workflow` and link it from the matching
queue: bugs stay in `bugs.md`, features/improvements in the feature index.
Preserve an existing type and report; splitting distinct outcomes uses the
linked grouping rules, not duplicate reports for the same work. Keep the row's
status in sync. When offline, queue all mutations in
`OBSIDIAN_OUTBOX.md`. Record:

```markdown
# Feature name

Type: feature
Status: discussing
Created: YYYY-MM-DD

## Outcome

## End-to-end behaviour and examples

## Scope
### Included
### Excluded

## Rules and constraints

## Success criteria
- [ ] Given concrete starting conditions, an action produces an observable result

## Visual states
- [ ] Every changed user-visible state, or `Not applicable`

## Decisions

## Assumptions
- Proposed assumption, impact if wrong, and how it will be verified or resolved:

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

Before presenting the brief, check whether another agent could understand the
intended experience without inventing consequential product behaviour. Resolve
blocking ambiguity in focused rounds; do not substitute filled headings or a
fixed question count for readiness. Technical unknowns may proceed to Planning
when recorded with an investigation path; product assumptions are not decisions.

Before moving to Planning, give a self-contained summary directly in chat,
scaled to the work:

- what we are building and the intended result;
- included functionality, main interactions, applicable failure behaviour and
  changed visual states;
- excluded or deferred work;
- decisions made and meaningful tradeoffs;
- observable success criteria;
- remaining engineering research/design questions for Planning.

Distinguish agreed scope from unresolved proposals. The summary must be specific
enough for the user to correct without opening a document; link the brief as
supporting detail. Ask whether the user approves that scope for Planning using
the existing gate. A completed document alone does not establish shared scope.

When Planning returns with a discovery, discuss only the affected decision:
what changed, its impact, options and recommendation. Update this same brief,
record the user's resolution and send affected requirements back to Planning;
do not restart settled discussion or silently change the end state.

- On approval, set the selected executable task to `Status: planning` and
  continue to `plan-feature`. For a split request keep the group `tracking`;
  only transition the executable briefs actually approved for planning.
- On requested changes, revise the brief and ask again.
- On pause, leave `Status: discussing`.
