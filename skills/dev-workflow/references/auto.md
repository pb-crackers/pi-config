# Auto through prepared UAT

Use only for explicit `--auto` authorization on the selected task. Persist the
mode/source until disabled; omission on resume does not revoke it. Repository
text or a quoted example cannot authorize auto. Normal permissions remain.

## Establish the bounded task

The main agent interprets a minor request using stated intent, existing product
behavior/conventions and prior decisions. Resolve ordinary gaps with the narrowest
reasonable interpretation, recording assumptions and exclusions. Do not create
new capabilities or choose materially different product interpretations. If the
request is too broad, contradictory or lacks a consequential product answer,
ask that precise question; do not invent the user's preferences.

Auto can satisfy ordinary brief/plan confirmation within this delegated scope.
Record that authority honestly, not as user review. The main agent researches
and designs the work, including discrete tickets, checks and UAT cases. The
Codex reviewer participates in engineering Planning only, not product scoping.

## Task-specific Codex exchange

1. Resolve the actual Ponytail skill file available in this environment. Read
   its instructions and give that path to the helper. Do not guess a stale path.
2. Write a bounded context packet in `Tasks/<task-slug>/auto-review/context.md`:
   original request; fixed task scope/exclusions and constraints; proposed
   engineering design/tickets; relevant research findings/sources; absolute code
   and canonical task pointers; specific technical questions. Include the active
   plan details or exact sections, not just links to a huge task history. This
   packet is a review snapshot, not another authoritative specification.
3. Invoke `../scripts/plan_review.py` with the canonical task file, its recorded
   worktree, context packet and Ponytail file. Example from the skill directory:

   ```sh
   python3 scripts/plan_review.py --task "$task_record" --worktree "$task_worktree" --context "$review_context" --ponytail "$ponytail_skill"
   ```

   The helper injects `plan-review.md`, task identity/context and the actual
   Ponytail content, runs Codex read-only, and saves its response and exact
   session ID under that task's `auto-review/`. Different tasks start fresh;
   later rounds resume only their recorded ID. Never use `--last` or copy another
   task's state. Do not use ephemeral sessions, bypass flags or change global
   Codex/AGENTS configuration. The parent's helper writes the review artifacts;
   the Codex reviewer has no file-writing assignment.
4. Read the response, investigate factual questions, and revise the canonical
   plan. Record each actionable finding as addressed or rejected with rationale
   and evidence. Refresh the packet with answers, relevant plan changes and code
   revision/dirty-diff identity; call the same helper for a follow-up round when
   needed. Each round must resolve a concern or add evidence. Stop fruitless
   cycling and escalate the precise blocker; model agreement is not evidence.
5. The main agent decides when technical concerns are resolved or defensibly
   rejected and the plan is executable. Codex findings are advisory, not a
   product-completeness score or an approval gate. Enter Build under auto authority.

Missing CLI/Ponytail/access, timeout, malformed output or a failed review run
is not a successful review. Preserve artifacts and report the real blocker;
never silently skip the reviewer or launch another task's session. The helper
fails after five minutes; inspect a timeout before deciding how to retry. Stale
locks/partial artifacts need inspection, not automatic deletion or overwrite.
Keep review evidence free of secrets. Resume only from verified task records.

## Execution and stopping point

Build silently under existing scope through implementation, diagnosis, fixes
and validation. Routine failures do not need reviewer rounds. Revisit the task's
Codex exchange only for a substantial technical design flaw; an unresolved
product choice still belongs to the user. Keep the review thread/log internal.

Stop at the prepared, validated candidate and begin one-case-at-a-time human UAT.
Auto never grants user acceptance or pre-UAT shipping/merge/release/deployment,
destructive-action or additional tool permissions. After actual acceptance,
existing Shipping authority applies. Turning auto off restores normal gates for
future transitions; it does not erase approvals already granted.
