---
name: debug-feature
description: >
  Establish evidence-backed root cause and impact for reported bugs or uncertain
  Build failures; route reported bugs through Discussion and keep technical
  Build recovery inside existing execution authority.
---

# Debug Feature

Record the entry context: **reported bug** (including UAT failures routed here)
or **Build recovery**. Read the original symptom, expected behavior, candidate,
relevant brief/design/tickets and previous attempts. Follow
`../dev-workflow/references/records.md`; preserve the task/report identity and
update its matching row. Standalone selected bugs expand into canonical bug
records; feature QA failures stay attached to their existing task, not duplicate
standalone reports. Ask only for facts needed from the user that cannot be found.

## Root cause and impact

Set `debugging`. Establish a repeatable reproduction with expected/actual
results where possible. Trace the affected flow, callers, contracts, dependencies
and state. Distinguish product defects from changed requirements, stale builds,
test setup and missing access. Record evidence limits if reproduction fails;
do not claim a proven root cause without support.

For uncertainty, test predictions that distinguish plausible causes, changing
one variable at a time. Use targeted removable instrumentation without exposing
secrets; measure performance before altering it. Repeated failures, multiple
affected flows or contradicted assumptions require broader research/design
reassessment. A clear local defect needs only a short diagnosis and regression
check, not a mandatory architecture review.

Record symptom, root cause/evidence, affected behavior/criteria, previous failed
assumptions, smallest correction direction and validation, reopened tickets/stale
evidence, and next route with authority source. Preserve useful code; remove
temporary instrumentation after validation. Diagnose here; implementation belongs
to Build. Do not commit during diagnosis.

## Route

- **Reported bug:** after RCA set `discussing` and use `discuss-feature` to confirm
  the intended correction and task boundaries, then Planning/tickets → Build →
  UAT. Carry RCA evidence forward and reuse already agreed behavior. This is the
  normal workflow for fixing bugs, not an isolated fix-plan approval ceremony.
- **Build recovery:** a bounded fix returns to Build; a technical design issue
  uses Planning to revise affected contracts/tickets, then returns to Build.
  Existing Build authority covers both without a user question or progress report.
  Only a genuinely unresolved product/scope decision returns to Discussion.
- **Setup/candidate issue:** restore preparation and revalidate under existing
  authority; seek missing access rather than changing product behavior to hide it.
- **No viable evidence-backed next step:** preserve findings and report the
  precise user-dependent blocker. Do not repeat the same patch indefinitely.

Build reruns the original scenario and dependent checks. User-reported UAT
failures require focused user retesting after repairs; agent tests cannot accept
those failures on the user's behalf.
