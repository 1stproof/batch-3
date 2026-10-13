#!/usr/bin/env python3
"""Apply the Codex and provider-model compatibility changes used here."""

from __future__ import annotations

import sys
from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one match in {path}, found {count}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def patch(root: Path) -> None:
    hook = root / "hooks" / "loop-codex-stop-hook.sh"
    setup = root / "scripts" / "setup-rlcr-loop.sh"
    common = root / "hooks" / "lib" / "loop-common.sh"
    ask_codex = root / "scripts" / "ask-codex.sh"

    # Humanize's upstream allowlist accepts only bare Codex model names. Kimi's
    # public identifier is provider-qualified (moonshotai/Kimi-k3), so permit
    # slash-separated components while retaining a strict character allowlist.
    bare_model_pattern = r"^[a-zA-Z0-9._-]+$"
    qualified_model_pattern = r"^[a-zA-Z0-9._-]+(/[a-zA-Z0-9._-]+)*$"
    for path, variable in (
        (setup, "CODEX_MODEL"),
        (hook, "CODEX_EXEC_MODEL"),
        (common, "_cfg_codex_model"),
        (ask_codex, "CODEX_MODEL"),
    ):
        replace_once(
            path,
            f'"${variable}" =~ {bare_model_pattern}',
            f'"${variable}" =~ {qualified_model_pattern}',
        )

    replace_once(
        common,
        '''elif [[ -n "$_cfg_codex_model" && ! "$_cfg_codex_model" =~ ^(gpt-|o[0-9]) ]]; then
    echo "Warning: Unsupported codex_model in merged config: $_cfg_codex_model" >&2
    echo "  Must start with a Codex model prefix: gpt- or o[0-9]" >&2''',
        '''elif [[ -n "$_cfg_codex_model" && ! "$_cfg_codex_model" =~ ^(gpt-|o[0-9]|[a-zA-Z0-9._-]+/) ]]; then
    echo "Warning: Unsupported codex_model in merged config: $_cfg_codex_model" >&2
    echo "  Must be a Codex model or a provider-qualified model" >&2''',
    )
    replace_once(
        setup,
        'echo "  Only alphanumeric, hyphen, underscore, dot allowed" >&2',
        'echo "  Only slash-separated alphanumeric, hyphen, underscore, dot components allowed" >&2',
    )
    replace_once(
        ask_codex,
        'echo "  Only alphanumeric, hyphen, underscore, dot allowed" >&2',
        'echo "  Only slash-separated alphanumeric, hyphen, underscore, dot components allowed" >&2',
    )

    replace_once(
        hook,
        'CODEX_REVIEW_EFFORT="high"',
        'CODEX_REVIEW_EFFORT="$CODEX_EXEC_EFFORT"',
    )
    replace_once(
        hook,
        '''if [[ -n "$CODEX_REVIEW_EFFORT" ]]; then
    CODEX_REVIEW_ARGS+=("-c" "model_reasoning_effort=${CODEX_REVIEW_EFFORT}")
fi''',
        '''if [[ -n "$CODEX_REVIEW_EFFORT" ]]; then
    CODEX_REVIEW_ARGS+=("-c" "model_reasoning_effort=${CODEX_REVIEW_EFFORT}")
fi
if [[ "${HUMANIZE_CODEX_BYPASS_SANDBOX:-}" == "true" ]] || [[ "${HUMANIZE_CODEX_BYPASS_SANDBOX:-}" == "1" ]]; then
    CODEX_REVIEW_ARGS+=("-c" "sandbox_mode=danger-full-access")
fi''',
    )


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} HUMANIZE_ROOT", file=sys.stderr)
        return 2
    patch(Path(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
