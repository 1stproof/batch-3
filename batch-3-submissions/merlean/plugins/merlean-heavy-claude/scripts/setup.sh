#!/usr/bin/env bash
# Shared standalone installer. Code and runtime may live outside the Lean project.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_DIR="$PWD"
RUNTIME_DIR="${MERLEAN_RUNTIME:-$PLUGIN_ROOT}"
SKIP_VENV=0
SKIP_MATHLIB=0
NL_MODE=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --project|--runtime)
      [ "$#" -ge 2 ] && [ -n "$2" ] || { echo "Missing directory for $1" >&2; exit 2; }
      if [ "$1" = --project ]; then PROJECT_DIR="$2"; else RUNTIME_DIR="$2"; fi
      shift 2 ;;
    -NL|--nl) NL_MODE=1; SKIP_MATHLIB=1; shift ;;
    --skip-venv) SKIP_VENV=1; shift ;;
    --skip-mathlib) SKIP_MATHLIB=1; shift ;;
    --help)
      echo 'Usage: setup.sh [--project DIR] [--runtime DIR] [--skip-venv] [--skip-mathlib] [-NL|--nl]'
      echo 'Project defaults to cwd; runtime defaults to MERLEAN_RUNTIME or the plugin root.'
      exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
PROJECT_INPUT="$PROJECT_DIR"
mkdir -p "$PROJECT_DIR" "$RUNTIME_DIR"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd -P)"
RUNTIME_DIR="$(cd "$RUNTIME_DIR" && pwd -P)"
case "$PROJECT_DIR" in
  */.claude/plugins/*|*/.codex/plugins/cache/*)
    echo 'Choose a project outside the installed plugin cache with --project.' >&2; exit 2 ;;
esac

TPL="$PLUGIN_ROOT/templates"
VENV_DIR="$RUNTIME_DIR/.venv"
VENV_PY="$VENV_DIR/bin/python"
resolve_venv_py() {
  if [ -x "$VENV_DIR/bin/python" ]; then VENV_PY="$VENV_DIR/bin/python"
  elif [ -x "$VENV_DIR/Scripts/python.exe" ]; then VENV_PY="$VENV_DIR/Scripts/python.exe"
  else return 1; fi
}
find_host_python() {
  local candidate
  for candidate in python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 python3 python; do
    command -v "$candidate" >/dev/null 2>&1 || continue
    if "$candidate" -c 'import sys; raise SystemExit(sys.version_info < (3, 9))' >/dev/null 2>&1; then
      command -v "$candidate"; return 0
    fi
  done
  return 1
}
HOST_PY="$(find_host_python || true)"
if [ -n "$HOST_PY" ]; then
  if [ "$NL_MODE" = 1 ]; then
    POLICY_MODE="$("$HOST_PY" "$PLUGIN_ROOT/src/lean_capability.py" "$PROJECT_INPUT" --nl)"
  else
    POLICY_MODE="$("$HOST_PY" "$PLUGIN_ROOT/src/lean_capability.py" "$PROJECT_INPUT")"
  fi
  if [ "$POLICY_MODE" = nl ]; then NL_MODE=1; SKIP_MATHLIB=1; fi
else
  # Without a parser, any policy-shaped file in lexical/resolved ancestry is
  # unknown and therefore cannot authorize Lean setup. Preserve uv-only default
  # setup only for projects with no persisted capability evidence.
  POLICY_PRESENT=0
  for policy_start in "$PROJECT_INPUT" "$PROJECT_DIR" "$PWD" "$(pwd -P)"; do
    case "$policy_start" in /*) ;; *) policy_start="$PWD/$policy_start" ;; esac
    while :; do
      for policy_name in .merlean-capabilities.json host-config.json; do
        if [ -e "$policy_start/$policy_name" ] || [ -L "$policy_start/$policy_name" ]; then POLICY_PRESENT=1; fi
      done
      [ "$policy_start" = / ] && break
      policy_start="$(dirname "$policy_start")"
    done
  done
  if [ "$NL_MODE" = 1 ] || [ "$POLICY_PRESENT" = 1 ]; then
    echo 'Python is required to validate inherited capability before setup.' >&2; exit 1
  fi
fi
if { [ -e "$PROJECT_DIR/.merlean-workspace.json" ] || [ -L "$PROJECT_DIR/.merlean-workspace.json" ]; } && [ "$SKIP_MATHLIB" = 0 ]; then
  echo 'Shared workspace: use --skip-mathlib for runtime setup, then scripts/merlean-workspace build --project DIR.' >&2
  exit 2
fi
REQUIREMENTS="$PLUGIN_ROOT/src/requirements.txt"
if [ "$NL_MODE" = 1 ]; then REQUIREMENTS="$PLUGIN_ROOT/src/requirements-nl.txt"; fi
if [ "$SKIP_VENV" = 0 ]; then
  if [ -e "$VENV_DIR" ] || [ -L "$VENV_DIR" ]; then
    if ! resolve_venv_py || ! "$VENV_PY" -c 'import sys' >/dev/null 2>&1; then
      echo "Existing runtime is incomplete; preserved $VENV_DIR. Repair it or choose another --runtime." >&2
      exit 1
    fi
  elif [ -n "$HOST_PY" ]; then
    if ! "$HOST_PY" -m venv "$VENV_DIR" && ! "$HOST_PY" -m venv --without-pip "$VENV_DIR"; then
      if resolve_venv_py; then
        : # A usable interpreter can still receive dependencies through uv below.
      elif [ ! -e "$VENV_DIR" ] && command -v uv >/dev/null 2>&1; then
        uv venv --python 3.12 "$VENV_DIR"
      else
        echo "Runtime creation failed; preserved $VENV_DIR. Choose another --runtime or repair it." >&2
        exit 1
      fi
    fi
  elif command -v uv >/dev/null 2>&1; then
    uv venv --python 3.12 "$VENV_DIR"
  else
    echo 'Install Python with venv support or uv, then rerun setup.' >&2; exit 1
  fi
  resolve_venv_py || { echo "No runtime interpreter; preserved $VENV_DIR." >&2; exit 1; }
  if "$VENV_PY" -m pip --version >/dev/null 2>&1 || "$VENV_PY" -m ensurepip --upgrade; then
    "$VENV_PY" -m pip install -r "$REQUIREMENTS"
  elif command -v uv >/dev/null 2>&1; then
    uv pip install --python "$VENV_PY" -r "$REQUIREMENTS"
  else
    echo "pip is unavailable; preserved $VENV_DIR. Install uv or repair pip and rerun." >&2; exit 1
  fi
fi

# Exclusive writes preserve existing files, including dangling symlinks.
create_template() {
  local name="$1"
  if [ -e "$PROJECT_DIR/$name" ] || [ -L "$PROJECT_DIR/$name" ]; then
    printf 'Preserved %s\n' "$name"
  else
    (umask 077; set -o noclobber; cat "$TPL/$name" > "$PROJECT_DIR/$name")
    printf 'Created %s\n' "$name"
  fi
}
if [ ! -e "$PROJECT_DIR/.env" ] && [ ! -L "$PROJECT_DIR/.env" ] && [ -z "${OPENAI_API_KEY:-}" ]; then
  (umask 077; set -o noclobber; cat "$TPL/.env.example" > "$PROJECT_DIR/.env")
fi
echo 'Existing environment files are preserved. Configure keys outside the conversation, or use PLAN_OFFLINE=1.'
if [ "$NL_MODE" = 0 ]; then
if [ -e "$PROJECT_DIR/.mcp.json" ] || [ -L "$PROJECT_DIR/.mcp.json" ]; then
  echo 'Preserved .mcp.json'
elif resolve_venv_py; then
  "$VENV_PY" - "$PROJECT_DIR/.mcp.json" "$VENV_PY" "$TPL/mcp.json" <<'PY'
import json
import sys
from pathlib import Path
config = json.loads(Path(sys.argv[3]).read_text())
config['mcpServers']['lean-lsp']['command'] = sys.argv[2]
with open(sys.argv[1], 'x', encoding='utf-8') as stream:
    json.dump(config, stream, indent=2)
    stream.write('\n')
PY
else
  echo 'No runtime interpreter; .mcp.json creation deferred.'
fi
NEW_LAKE=0
NEW_TOOLCHAIN=0
if [ ! -e "$PROJECT_DIR/lakefile.toml" ] && [ ! -L "$PROJECT_DIR/lakefile.toml" ] && [ ! -e "$PROJECT_DIR/lakefile.lean" ] && [ ! -L "$PROJECT_DIR/lakefile.lean" ]; then
  create_template lakefile.toml
  create_template MerLeanExperiment.lean
  NEW_LAKE=1
fi
if [ ! -e "$PROJECT_DIR/lean-toolchain" ] && [ ! -L "$PROJECT_DIR/lean-toolchain" ]; then NEW_TOOLCHAIN=1; fi
create_template lean-toolchain
# Retain exact starter snapshots until dependency setup succeeds. This allows a
# skipped/failed first run to resume without updating an existing user's project.
SETUP_PENDING="$PROJECT_DIR/.merlean-setup-pending"
if [ "$NEW_LAKE" = 1 ]; then
  if [ -e "$SETUP_PENDING" ] || [ -L "$SETUP_PENDING" ]; then
    echo "Unexpected setup marker preserved: $SETUP_PENDING" >&2; exit 1
  fi
  mkdir "$SETUP_PENDING"
  cp "$PROJECT_DIR/lakefile.toml" "$SETUP_PENDING/lakefile.toml"
  if [ "$NEW_TOOLCHAIN" = 1 ]; then
    cp "$PROJECT_DIR/lean-toolchain" "$SETUP_PENDING/lean-toolchain"
  fi
fi
OWNED_LAKE=0
OWNED_TOOLCHAIN=0
if [ -d "$SETUP_PENDING" ] && [ ! -L "$SETUP_PENDING" ]; then
  if [ -f "$SETUP_PENDING/lakefile.toml" ] && [ ! -L "$SETUP_PENDING/lakefile.toml" ] \
    && [ ! -L "$PROJECT_DIR/lakefile.toml" ] \
    && [ ! -e "$PROJECT_DIR/lakefile.lean" ] && [ ! -L "$PROJECT_DIR/lakefile.lean" ] \
    && cmp -s "$SETUP_PENDING/lakefile.toml" "$TPL/lakefile.toml" \
    && cmp -s "$SETUP_PENDING/lakefile.toml" "$PROJECT_DIR/lakefile.toml"; then
    OWNED_LAKE=1
  fi
  if [ -f "$SETUP_PENDING/lean-toolchain" ] && [ ! -L "$SETUP_PENDING/lean-toolchain" ] \
    && [ ! -L "$PROJECT_DIR/lean-toolchain" ] \
    && cmp -s "$SETUP_PENDING/lean-toolchain" "$TPL/lean-toolchain" \
    && cmp -s "$SETUP_PENDING/lean-toolchain" "$PROJECT_DIR/lean-toolchain"; then
    OWNED_TOOLCHAIN=1
  fi
fi
if [ "$SKIP_MATHLIB" = 0 ]; then
  if command -v lake >/dev/null 2>&1; then
    (
      cd "$PROJECT_DIR"
      if [ "$OWNED_LAKE" = 1 ] && [ ! -e lake-manifest.json ] && [ ! -L lake-manifest.json ]; then
        lake update
      fi
      if [ "$OWNED_LAKE" = 1 ] && [ "$OWNED_TOOLCHAIN" = 1 ] && [ -f .lake/packages/mathlib/lean-toolchain ]; then
        cp .lake/packages/mathlib/lean-toolchain lean-toolchain
      fi
      lake exe cache get
      lake build
    )
    # Preserve the snapshots as provenance; rename the marker after success so
    # future setup cannot treat the project as an unfinished starter workspace.
    if [ "$OWNED_LAKE" = 1 ]; then
      SETUP_COMPLETE="$PROJECT_DIR/.merlean-setup-complete"
      if [ ! -e "$SETUP_COMPLETE" ] && [ ! -L "$SETUP_COMPLETE" ]; then
        mv "$SETUP_PENDING" "$SETUP_COMPLETE"
      else
        echo "Existing completion marker preserved; pending marker retained: $SETUP_PENDING" >&2
      fi
    fi
  else
    echo 'lake not found; install elan/Lean and rerun setup.'
  fi
fi
else
  echo 'NL capability persisted: no Lean templates, MCP configuration, Lean dependencies or lake commands.'
fi
printf 'Ready: project=%s runtime=%s\n' "$PROJECT_DIR" "$RUNTIME_DIR"
printf 'Use MERLEAN_RUNTIME="%s" with scripts/merlean when this is a separate runtime.\n' "$RUNTIME_DIR"
