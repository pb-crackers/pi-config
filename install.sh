#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
AGENT_DIR=${PI_CODING_AGENT_DIR:-"$HOME/.pi/agent"}

command -v pi >/dev/null || { echo "pi is not installed" >&2; exit 1; }
command -v python3 >/dev/null || { echo "python3 is not installed" >&2; exit 1; }
mkdir -p "$AGENT_DIR/skills" "$AGENT_DIR/themes"

link_config() {
  local source=$1 destination=$2 backup
  if [[ -L "$destination" && "$destination" -ef "$source" ]]; then
    return
  fi
  if [[ -e "$destination" || -L "$destination" ]]; then
    backup="$destination.backup.$(date +%Y%m%d%H%M%S)"
    while [[ -e "$backup" || -L "$backup" ]]; do backup="$backup.1"; done
    mv -- "$destination" "$backup"
    echo "Backed up $destination to $backup"
  fi
  ln -s -- "$source" "$destination"
  echo "Linked $destination"
}

link_config "$ROOT/AGENTS.md" "$AGENT_DIR/AGENTS.md"
link_config "$ROOT/settings.json" "$AGENT_DIR/settings.json"
link_config "$ROOT/themes/omarchy-system.json" "$AGENT_DIR/themes/omarchy-system.json"
for skill in dev-workflow capture-todo discuss-feature build-feature uat-feature ship-feature supabase supabase-postgres-best-practices; do
  link_config "$ROOT/skills/$skill" "$AGENT_DIR/skills/$skill"
done

while IFS= read -r package; do
  pi install "$package"
done < <(python3 -c 'import json,sys; print(*json.load(open(sys.argv[1]))["packages"], sep="\n")' "$ROOT/settings.json")

"$ROOT/verify.sh"
