---
name: build-feature
description: >
  Silently implement and test approved task tickets, diagnose/fix/retest until
  the entire outcome is validated, then prepare the candidate for user UAT.
---

# Build Feature

Require a ready plan and recorded `Build authorization` under dev-workflow.
Set `building`; read the current brief/design, criteria, tickets, decisions,
project instructions and diff. Follow Ponytail full, the record rules and the
owned working copy. Give delegated writers bounded scope, design links and
Ponytail full; use dev-workflow's working-copy/delegation reference.

## Silent execution loop

Do the approved work without routine chat updates, ticket-completion messages
or "continue?" prompts. Record progress/evidence internally. Continue taking
authorized actions until the whole candidate is prepared for UAT, or the
integration rules permit return to Shipping. A completed slice, failed check or
internal technical replan is not a user handoff.

1. Take a ready ticket in dependency order, or the next slice for a small task.
   Keep the task's parent outcome, active slice, contracts and completion checks
   current internally. Claim the ticket before edits; integrate delegated work
   before starting dependants.
2. Implement the smallest complete slice through affected layers and callers.
   Verify its acceptance criteria and dependent behavior. Add meaningful checks
   for nontrivial logic using observable behavior and requirement-based examples,
   not assertions mirroring implementation. Test failures/error handling too.
   For fixes, show the original check failing then passing when practical;
   record limits rather than claiming an unobserved red/green result.
3. Diagnose a local failure proportionately, fix and rerun the original scenario
   plus affected checks. For uncertain/repeated failures or contradicted design,
   use `debug-feature` as **Build recovery**; research/replan technically within
   existing scope. Do not accumulate symptom patches or lower criteria.
4. Record results and mark a ticket `validated` only when checks pass. Split
   independent deliverables that outgrow a ticket through Planning under existing
   authority. Preserve IDs/evidence, reopen affected dependencies and resequence
   only for documented reasons. Distinct capabilities require a scope decision.
5. Repeat until all task criteria and whole-task integration checks pass. Review
   connected code for correctness, safety and scope fidelity: everything requested,
   nothing unrequested, no partial implementation. Independent review is optional
   for a concrete concern; fix accepted findings through the same writer/loop.

Use `../dev-workflow/references/integration.md` before final validation: fetch
and integrate current target, assess semantic impacts and rerun required gates.
Use `../dev-workflow/references/ui-verification.md` for UI craft, mockups and
conditional iOS build/device checks. Never claim unavailable checks passed.

Interrupt only for an unresolved product/scope decision, missing permission/access,
a blocker with no viable in-scope next approach, or explicit user pause/stop.
Investigate what can be resolved first; ask the precise question with evidence
and a recommendation. If an execution limit forces a stop, preserve the next
action and state the actual limit; do not imply work continues in the background.

## UAT handoff

Reconcile the planned UAT cases with the completed behavior and all active
criteria; add only justified coverage, never replace requested checks with what
happened to be built. Prepare `Tasks/<task-slug>/uat.md` under the record rules.
Record source revision/dirty diff, integrated target, artifact/build, environment,
setup, commands/results, evidence, limitations and applicable device ownership.
Keep evidence outside disposable interaction sessions.

For behavior-preserving post-acceptance integration, document retained acceptance
under the integration reference, set `shipping` and resume Shipping directly.
Otherwise prepare the actual running candidate/artifact, set `awaiting-uat` and
continue to `uat-feature`. The first user-facing handoff explains what is ready,
material limitations and the first UAT case. Do not ask whether to start UAT.
