#!/usr/bin/env bash
set -uo pipefail

ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
AGENT_DIR=${PI_CODING_AGENT_DIR:-"$HOME/.pi/agent"}
failed=0

check_link() {
  local source=$1 destination=$2
  if [[ ! -L "$destination" || ! "$destination" -ef "$source" ]]; then
    echo "FAIL: $destination is not linked to $source" >&2
    failed=1
  fi
}

check_link "$ROOT/AGENTS.md" "$AGENT_DIR/AGENTS.md"
check_link "$ROOT/settings.json" "$AGENT_DIR/settings.json"
check_link "$ROOT/themes/omarchy-system.json" "$AGENT_DIR/themes/omarchy-system.json"
for skill in dev-workflow capture-todo discuss-feature plan-feature build-feature uat-feature ship-feature supabase supabase-postgres-best-practices; do
  check_link "$ROOT/skills/$skill" "$AGENT_DIR/skills/$skill"
  if ! grep -q '^name:' "$ROOT/skills/$skill/SKILL.md" || ! grep -q '^description:' "$ROOT/skills/$skill/SKILL.md"; then
    echo "FAIL: invalid skill metadata: $skill" >&2
    failed=1
  fi
done

python3 - "$AGENT_DIR" "$ROOT/settings.json" <<'PY' || failed=1
import json, pathlib, sys
agent_dir, settings_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
settings = json.loads(settings_path.read_text())
for spec in settings["packages"]:
    package = spec[4:] if spec.startswith("npm:") else spec
    name, expected = package.rsplit("@", 1)
    package_file = agent_dir / "npm/node_modules" / name / "package.json"
    try:
        actual = json.loads(package_file.read_text())["version"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print(f"FAIL: package not installed: {name}", file=sys.stderr)
        raise SystemExit(1)
    if actual != expected:
        print(f"FAIL: {name} is {actual}, expected {expected}", file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: {name}@{actual}")
PY

if [[ -e "$AGENT_DIR/AGENT.md" || -L "$AGENT_DIR/AGENT.md" ]]; then
  echo "WARN: legacy $AGENT_DIR/AGENT.md still exists" >&2
fi

for directory in "$HOME/.agents/skills"/*; do
  [[ -e "$directory" ]] || continue
  case "$(basename "$directory")" in
    supabase|supabase-postgres-best-practices) ;;
    *) echo "WARN: Pi will also discover shared skill $directory" >&2 ;;
  esac
done

if (( failed )); then
  exit 1
fi
echo "Pi configuration verified."
