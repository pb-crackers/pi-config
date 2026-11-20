# pi-config

Portable personal configuration for [Pi](https://github.com/earendil-works/pi-mono).

## Install

Pi and Python 3 must already be available. Clone and run:

```sh
git clone https://github.com/pb-crackers/pi-config.git ~/.config/pi-config
~/.config/pi-config/install.sh
```

The installer:

- backs up conflicting managed paths;
- symlinks the global instructions, settings, theme, and selected skills;
- installs the exact configured Pi package versions;
- verifies the result.

It is safe to rerun. Git does not execute scripts automatically after cloning, so the explicit `install.sh` step is required.

## Update

```sh
git -C ~/.config/pi-config pull --ff-only
~/.config/pi-config/install.sh
```

Run `./verify.sh` at any time to check links, skills, and package versions. It warns when shared `~/.agents/skills` may also be discovered by Pi.

## Included

- `AGENTS.md` and `CHANGELOG.md`
- Pi settings and model preferences
- staged development workflow skills for todo capture, debugging, discussion,
  planning, dependent implementation tickets, building, UAT, and shipping
- `unslop` UI craft review during Build, bounded by the approved design
- Obsidian-backed feature backlog, separate active/resolved bug tables, canonical
  task reports with concise summaries, a compact implementation-log table, and a
  repository outbox for offline updates
- `supabase` and `supabase-postgres-best-practices` skills
- Omarchy system theme
- Pinned Pi package declarations
- Pi's built-in MCP support (personal servers stay in `~/.pi/agent/mcp.json`)
- Pi-only exclusions for duplicate shared Supabase skills; other tools keep their copies

## Deliberately excluded

Credentials, MCP configuration, sessions, history, caches, trust decisions, generated Herdr integration code, and operating-system-provided skills are not tracked.

The vendored Supabase skills come from [`supabase/agent-skills`](https://github.com/supabase/agent-skills) and retain their MIT license files.

The vendored [Unslop](https://github.com/heydamir/unslop) skill by Damir Sokolovsky retains its CC BY 4.0 attribution, license, and pinned source revision under `skills/unslop/`.
