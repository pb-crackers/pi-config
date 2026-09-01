# Add debug workflow

Status: shipping
Created: 2026-08-31

## Outcome

Let users invoke a debug skill that produces a concise, evidence-backed root
cause analysis and approved fix plan before any code is changed.

## Scope

### Included

- A diagnosis-only `debug-feature` workflow phase.
- A short bug report: expected behavior, actual behavior, and reproduction
  steps when known.
- Reproduction when practical, Scout-led tracing, and other advisors only when
  needed.
- Root cause analysis with symptom, root cause, and evidence.
- An explicit approval gate before handing the fix plan to `build-feature`.

### Excluded

- A second implementation or UAT workflow.
- Required version, device, account, frequency, or log fields.
- Required analysis of unrelated callers or flows.

## Success criteria

- [x] A bug report routes to `debug-feature` before Build.
- [x] The skill records the report, root cause, fix plan, and validation in the
  existing `plan.md`.
- [x] The skill makes no product-code edits or commits.
- [x] An approved diagnosis hands its fix plan to `build-feature`, which keeps
  the existing worker, review, UI validation, and UAT rules.
- [x] Installer and verifier manage the new skill.

## Visual states

- [ ] Not applicable

## Decisions

- Reuse `Status: approved` after diagnosis approval rather than introduce a
  second approval status.
- Use the existing task record; add a `## Debug` section rather than another
  file format.

## Implementation plan

1. Add `skills/debug-feature/SKILL.md`: collect the concise report; reproduce
   when practical; use Scout and other needed advisors; record root cause,
   evidence, smallest fix, and validation; require user approval; then set
   `Status: approved` and hand off to Build.
2. Update `dev-workflow` routing so explicit bug reports or `Status: debugging`
   load `debug-feature`; add the debug-to-Build approval gate.
3. Add the new skill to `install.sh`, `verify.sh`, `README.md`, and
   `CHANGELOG.md`.
4. Validate with `bash -n install.sh verify.sh`, `./verify.sh`, and
   `git diff --check`.

## Validation

- UAT: user approved shipping on 2026-08-31.
- Passed: `bash -n install.sh verify.sh`, `./verify.sh`, `git diff --check`.
- User flow: report a bug → receive RCA and fix plan → approve → existing Build
  workflow starts.

## Completion

- PR:
- Merge:
- Changelog:
