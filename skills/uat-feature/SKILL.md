---
name: uat-feature
description: >
  Guide user acceptance one case at a time with persisted candidate-specific
  results; collect failures, review them after testing, and route corrections
  or diagnosed bugs before focused retesting and shipping.
---

# UAT Feature

Require `awaiting-uat` and Build's validated, prepared candidate. Follow
`../dev-workflow/references/records.md` for the UAT record and matching queue.
Confirm artifact/source/dirty diff, integrated target, setup, check evidence,
limitations and planned cases. If stale or unavailable, return to Build for
preparation; do not treat a missing environment as a product defect. For iOS,
follow the UAT/device section of `../dev-workflow/references/ui-verification.md`.

## Run the session

Open or resume `Tasks/<task-slug>/uat.md`; preserve prior results and identify
which candidate each applies to. Set session `testing` when presenting cases.
State briefly what is ready and any material
limits. Present **one test case at a time**: feature/case name, needed setup,
clear actions and expected observable result. Wait for the user's response
before recording a result or presenting the next case.

- Explicit approval/pass: record `approved`, the response and tested candidate.
- Failure: record `failed` and the user's report verbatim; preserve evidence.
- Cannot test or explicit skip: record `blocked`/`skipped` and reason. Neither
  counts as approval. Clarify an ambiguous response; silence/empty input is not pass.

Persist each response and the next case so interrupted sessions can resume.
Collect failures and continue independent cases without changing the candidate
mid-session. Mark dependent cases blocked when a failure prevents testing them;
do not abandon independent coverage. An explicit user request for an immediate
repair can interrupt testing, but preserve results and reassess candidate/retest
scope before resuming.

## Review failures after testing

Set session state `review`. Present failed/blocked/skipped items and review their
disposition with the user. Distinguish defects, misunderstandings and new requests:
- A clear bounded correction with understood impact can use the short edit path
  through Build, validate, and return for focused retest. Small diff or cosmetic
  wording alone is not proof it is safe; unclear cause/impact needs diagnosis.
- A defect requiring investigation uses Debug RCA → Discussion → Planning/tickets
  → Build → UAT. This reported-bug Discussion confirms the correction after RCA,
  even when existing Build authority already covers its implementation; it is
  not another request for fix permission. Reuse the current task/report; create
  a separate linked follow-up only for genuinely separate, explicitly scoped work.
- A changed requirement returns to Discussion. Do not silently broaden the task.

Agree the failed-item disposition here rather than asking separately before every
in-scope fix. Repairs remain under existing Build authority. After changes,
set session `awaiting-retest`, rebuild/revalidate and retest failed and affected
cases one at a time; keep attempt history. Use
`../dev-workflow/references/integration.md` for evidence-based
retention of unaffected acceptance. Never approve a repaired reported failure
solely from automated checks.

## Finish

Testing finished is not acceptance. Keep `awaiting-uat` while required cases are
failed, pending, blocked or skipped. Any explicit waiver/deferral must identify
the affected criteria and user decision; do not silently remove failures or call
unverified behavior passed. Scope changes follow Discussion/Planning.

When all required cases and changed visual states have user approval (or an
explicitly recorded accepted scope adjustment), summarize acceptance and limits,
record the accepted candidate, set session `accepted` and task `approved-to-ship`.
For iOS, complete the
owned-device cleanup in the UI reference first. User acceptance grants existing
commit/push/PR/merge authority; continue to `ship-feature` without another shipping
question. Keep bugs active until confirmed merge under the record rules.

If testing must pause, persist the active case, keep the candidate available,
close idle interaction sessions and state the actual blocker. Do not claim
acceptance because testing could not be completed.
