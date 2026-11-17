---
name: debug-feature
description: >
  Diagnosis and impact assessment for reported bugs, failed validation, and
  UAT feedback. Establishes evidence before routing to a bounded fix, renewed
  research/planning, or a product decision; prevents repeated symptom patches.
---

# Debug Feature

Do not apply product fixes or commit during this phase. Temporary reproductions
and targeted instrumentation are allowed within existing authority; record and
remove them when no longer needed. Set the
Obsidian task record to `Status: debugging`. If none exists, create
`<project>/Tasks/<slug>.md`, link it from the feature index, or queue both
mutations in `OBSIDIAN_OUTBOX.md` when offline.

## Report

Ask only for missing information:

- What should happen?
- What happens instead?
- How can it be reproduced, if known?

## Investigate

1. Read the parent brief, research, approved plan, relevant tickets, candidate,
   previous attempts and exact reported failure. Distinguish a product defect
   from a changed requirement, stale candidate, missing access or test setup.
2. Prefer a repeatable check that fails on this specific symptom: an existing
   test, a small command/harness, UI automation, or a documented manual path.
   Record the invocation, actual result and expected result. Minimise a complex
   reproduction without losing the original failure; raise the reproduction
   rate for intermittent bugs. If reproduction is unavailable, state what was
   tried and the evidence limit; do not claim a proven cause or fix.
3. Trace the full affected flow, callers, shared dependencies, state ownership,
   data contracts, and related success criteria. Ask whether the proposed fix
   would break dependent behaviour or whether the chosen approach is wrong.
   Repeated unsuccessful fixes, multiple affected flows, or contradicted design
   assumptions require broader research and planning, not another symptom patch.
4. For uncertain causes, compare falsifiable hypotheses and test the predictions
   that distinguish them, one variable at a time. Use targeted instrumentation
   with a unique removable marker; redact secrets in commands and evidence.
   For performance issues, measure a baseline before changing the implementation.
5. Revisit relevant primary sources and reuse options when evidence challenges
   the approach. Scale investigation to the failure; an obvious local defect
   needs a short evidence-backed diagnosis, not a mandatory architecture review.
   Use independent investigation only for a concrete gap that should save time.

## Record

Add or update this section in the task record:

```markdown
## Debug

### Report

### Root cause
- Symptom:
- Root cause:
- Evidence:

### Fix plan
- Smallest fix:
- Validation:

### Impact and route
- Affected flows, dependencies, and parent/ticket criteria:
- Previous attempts and invalidated assumptions:
- Local defect, implementation/design issue, changed requirement, or setup issue:
- Research/replanning needed and evidence:
- Reopened tickets and invalidated validation:
- Next phase and authorization:
```

Keep the fix within the reported scope and include a check that proves the bug
is fixed. For UI bugs, include the required user-facing state and visual
validation.

## Route before editing

- Local defect: record a bounded fix and its dependency/regression checks, then
  use the approval gate below.
- Implementation or architectural issue: record why the approach failed, set
  `Status: planning`, and return to `plan-feature` to research alternatives and
  revise affected tickets. A larger implementation change can remain within
  scope; new product behaviour or consequential unresolved tradeoffs cannot.
- Changed or unclear requirement: set `Status: discussing` and return to
  `discuss-feature` for the user's decision, including under `--auto`.
- Candidate/setup issue: record the cause and return to Build for preparation
  and required revalidation when authority permits; seek missing access rather
  than changing product behaviour to hide the problem.

Preserve useful code and evidence. Do not reset the feature, add unrelated
refactors, or lower success criteria. If no viable next approach remains,
record the blocker and stop the loop.

## Approval gate

When the task has active `--auto` authorization under `dev-workflow`, record the
evidence-backed root cause analysis and fix plan as authorized by `--auto`, set
`Status: approved`, and continue directly to `build-feature` within the confirmed
scope. Unresolved evidence requires more investigation or a blocker report.

Otherwise, present the root cause analysis and fix plan. Ask whether to approve
it for Build.

- On approval, set `Status: approved` and continue to `build-feature`.
- On requested changes or unresolved evidence, remain `debugging`.

Build owns implementation, review, fresh-build validation, and UAT handoff.
It must rerun the original user scenario and affected dependency checks, and
remove temporary instrumentation, before presenting a new candidate.
