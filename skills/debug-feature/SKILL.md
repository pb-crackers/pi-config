---
name: debug-feature
description: >
  Diagnosis phase used by dev-workflow for reported bugs. Produces a concise,
  evidence-backed root cause analysis and fix plan before implementation.
disable-model-invocation: true
---

# Debug Feature

Do not edit product code, commit, or begin Build during this phase. Set an
existing task record to `Status: debugging`. If none exists, create
`plans/<slug>/plan.md`, link it from `TODO.md`, and record the bug report.

## Report

Ask only for missing information:

- What should happen?
- What happens instead?
- How can it be reproduced, if known?

## Investigate

1. Reproduce the bug when practical.
2. Use `scout` to trace the relevant flow and likely shared code.
3. Use `researcher`, `oracle`, or `reviewer` only when an external behavior,
   competing explanation, or risk needs resolution.
4. Do not claim a root cause without evidence.

## Record

Add or update this section in `plan.md`:

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
```

Keep the fix plan within the approved bug scope. It must include a check that
proves the bug is fixed. For UI bugs, include the required user-facing state
and visual validation.

## Approval gate

Present the root cause analysis and fix plan. Ask whether to approve it for
Build.

- On approval, set `Status: approved` and continue to `build-feature`.
- On requested changes or unresolved evidence, remain `debugging`.

Build owns the implementation worker, review, fresh build, and UAT.
