# Changelog

## Unreleased

- Require concrete discussion briefs and collaborative engineering designs,
  connect research discoveries back to requirements, and keep implementation
  slices and tickets anchored to the agreed goal.

- Set the default model to GPT 6.2 Sol with medium thinking and configure the
  Pi image-generation extension; preserve current personal Pi preferences.

- Preserve Build authorization through in-scope diagnosis, fixes, replanning and
  validation retries in manual mode too; keep initial standalone and UAT gates.

- Use Pi's built-in MCP support with the existing personal server configuration.
- Upgrade web-access, subagents and ask-user-question to releases with host-provided
  TypeBox peer dependencies; pin the installed computer-use package version.
- Exclude duplicate shared Supabase skills in Pi without deleting them for other tools.

- Keep implementation logs as compact task-linked tables; preserve completion
  detail and follow-ups in canonical tasks and read long records progressively.

- Separate active bug queues and resolved bug logs from feature backlogs; keep
  full reports in linked task records and read only relevant records.

- Added Unslop as a UI craft review during Build, preserving approved designs,
  native patterns and accessibility, with fresh validation after cleanup.

- Research reusable solutions and clarify requirements before choosing a build approach.
- Track larger features as dependent Obsidian tickets with whole-feature validation.
- Reassess QA failures and dependent flows before patching; keep autonomous retries
  within approved scope until explicit user acceptance.
- Isolate task edits in owned worktrees and clean them up safely after merge.
- Use the Obsidian Sync vault at `~/obsidian-vault/notes-synced/` for task records.

- Added a root-cause-analysis and fix-planning workflow for reported bugs.
- Added a planning phase with task records and HTML UI mockups.
- Require Build to review, fresh-build, install, launch, and prepare UI changes
  before direct user acceptance.
- Updated subagent guidance to select roles by expected speed, bound parallel
  work, recover stalled runs, and require writer-side Ponytail.
- Moved editable project records to Obsidian with a repository outbox for
  temporary offline updates.
- Separated headless shipping validation from Device Hub-based iOS UAT.
- Added SwiftUI design and accessibility checks to UI planning.
