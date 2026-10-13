from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SUBMISSION_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SUBMISSION_ROOT))

from src import patch_humanize


class HumanizePatchTests(unittest.TestCase):
    def test_patch_accepts_provider_model_and_sets_review_compatibility(self) -> None:
        hook_source = '''CODEX_REVIEW_EFFORT="high"
if [[ ! "$CODEX_EXEC_MODEL" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    exit 1
fi
if [[ -n "$CODEX_REVIEW_EFFORT" ]]; then
    CODEX_REVIEW_ARGS+=("-c" "model_reasoning_effort=${CODEX_REVIEW_EFFORT}")
fi
'''
        setup_source = '''# Only alphanumeric, hyphen, underscore, dot allowed
if [[ ! "$CODEX_MODEL" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    echo "  Only alphanumeric, hyphen, underscore, dot allowed" >&2
fi
'''
        common_source = '''if [[ -n "$_cfg_codex_model" && ! "$_cfg_codex_model" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    _cfg_codex_model=""
elif [[ -n "$_cfg_codex_model" && ! "$_cfg_codex_model" =~ ^(gpt-|o[0-9]) ]]; then
    echo "Warning: Unsupported codex_model in merged config: $_cfg_codex_model" >&2
    echo "  Must start with a Codex model prefix: gpt- or o[0-9]" >&2
    _cfg_codex_model=""
fi
'''
        ask_source = '''# Validate codex model for safety (alphanumeric, hyphen, underscore, dot)
if [[ ! "$CODEX_MODEL" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    echo "  Only alphanumeric, hyphen, underscore, dot allowed" >&2
fi
'''
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hook = root / "hooks" / "loop-codex-stop-hook.sh"
            setup = root / "scripts" / "setup-rlcr-loop.sh"
            common = root / "hooks" / "lib" / "loop-common.sh"
            ask_codex = root / "scripts" / "ask-codex.sh"
            for path, source in (
                (hook, hook_source),
                (setup, setup_source),
                (common, common_source),
                (ask_codex, ask_source),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(source, encoding="utf-8")

            patch_humanize.patch(root)
            hook_result = hook.read_text(encoding="utf-8")
            patched_sources = "\n".join(
                path.read_text(encoding="utf-8")
                for path in (hook, setup, common, ask_codex)
            )

        qualified_pattern = r"^[a-zA-Z0-9._-]+(/[a-zA-Z0-9._-]+)*$"
        self.assertEqual(patched_sources.count(qualified_pattern), 4)
        self.assertIn('CODEX_REVIEW_EFFORT="$CODEX_EXEC_EFFORT"', hook_result)
        self.assertIn('sandbox_mode=danger-full-access', hook_result)
        self.assertIn("provider-qualified model", patched_sources)
        for model, accepted in (
            ("moonshotai/Kimi-k3", True),
            ("gpt-6-astra", True),
            ("/Kimi-k3", False),
            ("moonshotai/", False),
            ("moonshotai//Kimi-k3", False),
            ("moonshotai/Kimi-k3:max", False),
            ("moonshotai/Kimi K3", False),
        ):
            result = subprocess.run(
                ["bash", "-c", f'[[ "$1" =~ {qualified_pattern} ]]', "--", model],
                check=False,
            )
            self.assertEqual(result.returncode == 0, accepted, model)

    @unittest.skipUnless(
        Path(os.environ.get("HUMANIZE_INTEGRATION_ROOT", "/opt/humanize")).is_dir(),
        "requires the patched Humanize tree installed by the Docker build",
    )
    def test_real_humanize_setup_accepts_kimi_provider_model(self) -> None:
        humanize_root = Path(
            os.environ.get("HUMANIZE_INTEGRATION_ROOT", "/opt/humanize")
        )
        setup = humanize_root / "scripts" / "setup-rlcr-loop.sh"
        with tempfile.TemporaryDirectory() as directory:
            job = Path(directory) / "job"
            job.mkdir()
            plan = job / "plan.md"
            plan.write_text(
                "# Integration plan\n\n"
                "## Goal\n\nVerify provider-qualified model setup.\n\n"
                "## Acceptance Criteria\n\n"
                "- Humanize records the exact Kimi model.\n"
                "- Humanize records max effort.\n",
                encoding="utf-8",
            )
            for command in (
                ["git", "init", "-b", "main"],
                ["git", "config", "user.name", "Humanize Integration Test"],
                ["git", "config", "user.email", "humanize-test@localhost"],
                ["git", "add", "plan.md"],
                ["git", "commit", "-m", "Initialize integration fixture"],
                ["git", "checkout", "-b", "humanize-rlcr"],
            ):
                subprocess.run(
                    command,
                    cwd=job,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

            result = subprocess.run(
                [
                    str(setup),
                    "plan.md",
                    "--track-plan-file",
                    "--max",
                    "1",
                    "--codex-model",
                    "moonshotai/Kimi-k3:max",
                    "--codex-timeout",
                    "60",
                    "--base-branch",
                    "main",
                    "--yolo",
                    "--privacy",
                ],
                cwd=job,
                env={
                    **os.environ,
                    "CODEX_HOME": str(Path(directory) / "codex-home"),
                    "HUMANIZE_GIT_TIMEOUT_SECONDS": "60",
                },
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=60,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout)
            states = list((job / ".humanize" / "rlcr").glob("*/state.md"))
            self.assertEqual(len(states), 1, result.stdout)
            state = states[0].read_text(encoding="utf-8")

        self.assertIn("codex_model: moonshotai/Kimi-k3", state)
        self.assertIn("codex_effort: max", state)


if __name__ == "__main__":
    unittest.main()
