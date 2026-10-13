#!/usr/bin/env python3
"""Run one autonomous Humanize RLCR workspace per First Proof problem."""

from __future__ import annotations

import concurrent.futures
import dataclasses
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit


INPUT_PATH = Path(os.environ.get("FIRST_PROOF_INPUT", "/data/input/input.json"))
OUTPUT_DIR = Path(os.environ.get("FIRST_PROOF_OUTPUT", "/data/output"))
WORK_DIR = Path(os.environ.get("FIRST_PROOF_WORK", "/work"))
HUMANIZE_ROOT = Path(os.environ.get("HUMANIZE_ROOT", "/opt/humanize"))
MODEL = "moonshotai/Kimi-k3"
MODEL_PROVIDER = "kimi_batch3"
EFFORT = "max"
DEFAULT_KIMI_UPSTREAM_URLS = (
    "http://38.9.57.183:30000",
    "http://38.9.57.184:30000",
)
DEFAULT_KIMI_PROXY_PORT = 18770
SERVING_NODE_COUNT = 2
KIMI_PROXY_START_SECONDS = 15
MAX_RLCR_ROUNDS = 42
REVIEW_TIMEOUT_SECONDS = 7200
HOOK_TIMEOUT_SECONDS = 2 * REVIEW_TIMEOUT_SECONDS + 600
DEFAULT_PARALLELISM = 10
DEFAULT_TRANSPORT_RESTARTS = 2
DEFAULT_RUN_SECONDS = 23 * 60 * 60
SHUTDOWN_GRACE_SECONDS = 10
HEARTBEAT_SECONDS = 60
LATEX_TIMEOUT_SECONDS = 120
PDFINFO_TIMEOUT_SECONDS = 30
MAX_SOLUTION_PAGES = 16
TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)


@dataclasses.dataclass(frozen=True)
class Problem:
    index: int
    problem_id: str
    latex: str
    slug: str
    output_name: str


@dataclasses.dataclass(frozen=True)
class ServingNode:
    index: int
    name: str
    upstream_url: str
    proxy_port: int
    api_key_env: str


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp"
    )
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def safe_slug(problem_id: str, index: int) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", problem_id).strip(".-")
    if not slug:
        slug = f"problem-{index + 1:03d}"
    return slug[:120]


def parse_input(path: Path) -> list[Problem]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read valid JSON from {path}: {exc}") from exc

    if not isinstance(payload, dict) or not isinstance(payload.get("problems"), list):
        raise ValueError("input must be an object with a 'problems' array")
    if not payload["problems"]:
        raise ValueError("input contains no problems")

    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    problems: list[Problem] = []
    for index, raw in enumerate(payload["problems"]):
        if not isinstance(raw, dict):
            raise ValueError(f"problem {index} must be an object")
        problem_id = raw.get("id")
        latex = raw.get("latex")
        if not isinstance(problem_id, str) or not problem_id.strip():
            raise ValueError(f"problem {index} has an invalid id")
        if not isinstance(latex, str) or not latex.strip():
            raise ValueError(f"problem {problem_id!r} has empty LaTeX")
        if problem_id in seen_ids:
            raise ValueError(f"duplicate problem id: {problem_id!r}")
        seen_ids.add(problem_id)

        base_slug = safe_slug(problem_id, index)
        slug = base_slug
        collision = 0
        while f"{slug}.tex" in seen_names:
            digest = hashlib.sha256(problem_id.encode("utf-8")).hexdigest()[:10]
            collision += 1
            slug = f"{base_slug[:96]}-{index + 1:04d}-{digest}-{collision}"
        output_name = f"{slug}.tex"
        seen_names.add(output_name)
        problems.append(Problem(index, problem_id, latex, slug, output_name))
    return problems


def authentication_available(nodes: Iterable[ServingNode] | None = None) -> bool:
    selected = tuple(nodes) if nodes is not None else serving_nodes()
    return all(os.environ.get(node.api_key_env, "").strip() for node in selected)


def kimi_proxy_port(node_index: int = 1) -> int:
    if not 1 <= node_index <= SERVING_NODE_COUNT:
        raise ValueError(f"serving node index must be between 1 and {SERVING_NODE_COUNT}")
    raw = os.environ.get(f"KIMI_PROXY_PORT_{node_index}")
    if raw is None:
        raw = os.environ.get("KIMI_PROXY_PORT", str(DEFAULT_KIMI_PROXY_PORT))
        try:
            raw = str(int(raw) + node_index - 1)
        except ValueError as exc:
            raise ValueError("KIMI_PROXY_PORT must be an integer") from exc
    try:
        port = int(raw)
    except ValueError as exc:
        raise ValueError(f"KIMI_PROXY_PORT_{node_index} must be an integer") from exc
    if not 1 <= port <= 65535:
        raise ValueError(
            f"KIMI proxy port for node {node_index} must be between 1 and 65535"
        )
    return port


def validate_kimi_upstream_url(value: str, variable: str) -> str:
    value = value.strip().rstrip("/")
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"{variable} must be an HTTP(S) origin")
    hostname = parsed.hostname.casefold()
    if hostname == "rust.cat" or hostname.endswith(".rust.cat"):
        raise ValueError("rust.cat endpoints are forbidden")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError(f"{variable} must not contain credentials")
    if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
        raise ValueError(f"{variable} must be an origin without a path")
    return value


def kimi_upstream_urls() -> tuple[str, str]:
    numbered = [os.environ.get(f"KIMI_UPSTREAM_URL_{index}") for index in (1, 2)]
    if any(value is not None for value in numbered):
        if not all(value and value.strip() for value in numbered):
            raise ValueError("set both KIMI_UPSTREAM_URL_1 and KIMI_UPSTREAM_URL_2")
        values = [str(value) for value in numbered]
        variables = ["KIMI_UPSTREAM_URL_1", "KIMI_UPSTREAM_URL_2"]
    else:
        combined = os.environ.get("KIMI_UPSTREAM_URLS")
        if combined is None:
            combined = os.environ.get("KIMI_UPSTREAM_URL")
        if combined is None:
            values = list(DEFAULT_KIMI_UPSTREAM_URLS)
        else:
            values = [value.strip() for value in combined.split(",") if value.strip()]
        if len(values) != SERVING_NODE_COUNT:
            raise ValueError(
                "KIMI_UPSTREAM_URLS must contain exactly two comma-separated origins"
            )
        variables = ["KIMI_UPSTREAM_URLS"] * SERVING_NODE_COUNT

    validated = tuple(
        validate_kimi_upstream_url(value, variable)
        for value, variable in zip(values, variables, strict=True)
    )
    if len(set(validated)) != SERVING_NODE_COUNT:
        raise ValueError("the two Kimi serving endpoints must be distinct")
    return validated[0], validated[1]


def kimi_upstream_url(node_index: int = 1) -> str:
    """Return one upstream URL; retained for callers that inspect a single node."""
    if not 1 <= node_index <= SERVING_NODE_COUNT:
        raise ValueError(f"serving node index must be between 1 and {SERVING_NODE_COUNT}")
    return kimi_upstream_urls()[node_index - 1]


def kimi_api_key_env(node_index: int) -> str:
    specific = f"KIMI_API_KEY_{node_index}"
    if os.environ.get(specific, "").strip():
        return specific
    if os.environ.get("KIMI_API_KEY", "").strip():
        return "KIMI_API_KEY"
    return specific


def serving_nodes() -> tuple[ServingNode, ServingNode]:
    urls = kimi_upstream_urls()
    nodes = tuple(
        ServingNode(
            index=index,
            name=f"node-{index}",
            upstream_url=urls[index - 1],
            proxy_port=kimi_proxy_port(index),
            api_key_env=kimi_api_key_env(index),
        )
        for index in (1, 2)
    )
    if len({node.proxy_port for node in nodes}) != SERVING_NODE_COUNT:
        raise ValueError("the two Kimi loopback proxy ports must be distinct")
    return nodes[0], nodes[1]


def assign_serving_nodes(
    problems: list[Problem], nodes: tuple[ServingNode, ServingNode]
) -> dict[str, ServingNode]:
    """Split the ordered input into two contiguous, near-equal node batches."""
    if not problems:
        return {}
    return {
        problem.problem_id: nodes[
            min(problem.index * len(nodes) // len(problems), len(nodes) - 1)
        ]
        for problem in problems
    }


def kimi_model_catalog() -> dict[str, Any]:
    return {
        "models": [
            {
                "slug": MODEL,
                "display_name": "Kimi K3",
                "description": (
                    "Kimi K3 through the submission's Chat Completions "
                    "compatibility bridge."
                ),
                "base_instructions": (
                    "You are Kimi K3 operating as an autonomous mathematical proof "
                    "agent. Follow the developer and user instructions exactly, use "
                    "tools serially, and continue until the proof and validation are "
                    "complete."
                ),
                "default_reasoning_level": "max",
                "supported_reasoning_levels": [
                    {"effort": level, "description": description}
                    for level, description in (
                        ("low", "Lighter reasoning"),
                        ("medium", "Balanced reasoning"),
                        ("high", "Deep reasoning"),
                        ("xhigh", "Extra-high reasoning"),
                        ("max", "Maximum reasoning"),
                    )
                ],
                "shell_type": "default",
                "visibility": "list",
                "supported_in_api": True,
                "priority": 1,
                "additional_speed_tiers": [],
                "service_tiers": [],
                "default_service_tier": None,
                "availability_nux": None,
                "upgrade": None,
                "include_skills_usage_instructions": False,
                "include_plugin_usage_instructions": False,
                "include_apps_usage_instructions": False,
                "default_reasoning_summary": "none",
                "support_verbosity": False,
                "default_verbosity": None,
                "apply_patch_tool_type": "freeform",
                "web_search_tool_type": "text_and_image",
                "truncation_policy": {"mode": "tokens", "limit": 10000},
                "supports_parallel_tool_calls": False,
                "supports_image_detail_original": False,
                "context_window": 262144,
                "max_context_window": 262144,
                "comp_hash": "first-proof-batch3-kimi-k3-serial-v1",
                "effective_context_window_percent": 95,
                "experimental_supported_tools": [],
                "input_modalities": ["text"],
                "supports_search_tool": False,
                "use_responses_lite": False,
            }
        ]
    }


def prepare_codex_home(codex_home: Path, hook_path: Path, node: ServingNode) -> None:
    codex_home.mkdir(parents=True, exist_ok=True)
    codex_home.chmod(0o700)
    model_catalog = codex_home / "kimi-model-catalog.json"
    atomic_write_json(model_catalog, kimi_model_catalog())
    proxy_url = f"http://127.0.0.1:{node.proxy_port}/v1"

    config = f'''model_provider = "{MODEL_PROVIDER}"
model = "{MODEL}"
review_model = "{MODEL}"
model_reasoning_effort = "{EFFORT}"
web_search = "disabled"
check_for_update_on_startup = false
model_catalog_json = "{model_catalog}"
approval_policy = "never"

[model_providers.{MODEL_PROVIDER}]
name = "First Proof Kimi K3 {node.name} endpoint"
base_url = "{proxy_url}"
env_key = "{node.api_key_env}"
requires_openai_auth = false
wire_api = "responses"

[features]
hooks = true
apps = false
plugins = false
remote_plugin = false
recommended_plugins = false
skill_search = false
multi_agent = false
multi_agent_v2 = false
browser_use = false
browser_use_external = false
browser_use_full_cdp_access = false
computer_use = false
in_app_browser = false
standalone_web_search = false
image_generation = false
daemon_auto_start = false

[shell_environment_policy]
inherit = "all"
exclude = ["KIMI_API_KEY", "KIMI_API_KEY_1", "KIMI_API_KEY_2", "OPENAI_API_KEY", "CODEX_API_KEY"]
'''
    atomic_write_text(codex_home / "config.toml", config)

    hooks = {
        "description": "Humanize RLCR Kimi K3 Stop hook for First Proof Batch 3",
        "hooks": {
            "Stop": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": str(hook_path),
                            "timeout": HOOK_TIMEOUT_SECONDS,
                            "statusMessage": "Humanize RLCR Kimi K3 review",
                        }
                    ]
                }
            ]
        },
    }
    atomic_write_json(codex_home / "hooks.json", hooks)


def start_kimi_proxy(log_dir: Path, node: ServingNode) -> subprocess.Popen[bytes]:
    """Start the local Responses-to-Chat-Completions bridge."""
    log_dir.mkdir(parents=True, exist_ok=True)
    proxy_script = Path(__file__).with_name("kimi_responses_proxy.py")
    port = node.proxy_port
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=0.25):
            pass
    except OSError:
        pass
    else:
        raise RuntimeError(f"Kimi proxy port {port} is already in use")

    stdout_path = log_dir / "kimi-proxy.stdout.log"
    stderr_path = log_dir / "kimi-proxy.stderr.log"
    event_path = log_dir / "kimi-proxy.jsonl"
    with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
        process = subprocess.Popen(
            [
                sys.executable,
                str(proxy_script),
                "--listen",
                "127.0.0.1",
                "--port",
                str(port),
                "--upstream",
                node.upstream_url,
                "--timeout",
                str(REVIEW_TIMEOUT_SECONDS),
                "--log",
                str(event_path),
            ],
            env=os.environ.copy(),
            stdout=stdout_file,
            stderr=stderr_file,
            start_new_session=True,
        )

    if not SHUTDOWN.register(process):
        terminate_process_session(process, grace_seconds=0)
        raise RuntimeError("external termination requested while starting Kimi proxy")

    deadline = time.monotonic() + KIMI_PROXY_START_SECONDS
    while time.monotonic() < deadline:
        if process.poll() is not None:
            SHUTDOWN.unregister(process)
            raise RuntimeError(
                f"Kimi compatibility proxy for {node.name} exited with code "
                f"{process.returncode}"
            )
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.25):
                return process
        except OSError:
            time.sleep(0.1)

    terminate_process_session(process, grace_seconds=0)
    SHUTDOWN.unregister(process)
    raise RuntimeError(f"Kimi compatibility proxy for {node.name} did not become ready")


def stop_kimi_proxy(process: subprocess.Popen[bytes]) -> None:
    terminate_process_session(process, grace_seconds=2)
    SHUTDOWN.unregister(process)


def run_checked(command: list[str], cwd: Path, env: dict[str, str]) -> None:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(command)}\n{result.stdout}"
        )


def initial_solution(problem: Problem) -> str:
    return f"""\\documentclass{{article}}
\\begin{{document}}
\\section*{{{latex_escape(problem.slug)}}}
Work in progress.
\\end{{document}}
"""


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(character, character) for character in text)


def job_agents_file() -> str:
    return f"""# First Proof autonomous solver policy

- Work only on the exact statement in `problem.tex`.
- Keep web search, browser tools, apps, plugins, and external research disabled.
- Do not read parent directories, sibling jobs, prior attempts, or canonical solutions.
- Do not spawn subagents or model subprocesses.
- Issue exactly one tool call at a time and wait for its result before the next.
- Use the active Humanize RLCR lifecycle exactly; do not edit its state files.
- The only final mathematical deliverable is `solution.tex`.
- The solution must be standalone LaTeX and no longer than 16 typeset pages.
- Prefer the article class with amsmath, amssymb, amsthm, mathtools, geometry,
  enumitem, hyperref, xcolor, graphicx, tikz, or tikz-cd; do not require
  external files, fonts, or shell commands.
- Worker and reviewer model: `{MODEL}` at `{EFFORT}` effort.
"""


def worker_prompt(problem: Problem) -> str:
    return f"""You are the sole worker for First Proof Batch 3 problem {problem.problem_id}.

A native Humanize RLCR loop is already active in this Git repository. Both the
worker and every independent reviewer are configured to use exactly {MODEL} at
{EFFORT} reasoning effort. Do not run setup again. Read the current
`.humanize/rlcr/*/round-0-prompt.md` and every later hook-generated prompt,
maintain the goal tracker, commit each completed round, write the required
round or finalize summary, and stop normally so the Humanize Stop hook reviews
the work. If the hook blocks exit, follow its feedback until it permits
completion.

Read all of `problem.tex`. Produce a rigorous, self-contained solution in
`solution.tex` that answers every part of the exact question. It must be one
standalone compilable LaTeX document beginning with `\\documentclass` and
ending with `\\end{{document}}`, use only standard packages, and fit within 16
typeset pages. Prefer the `article` class with `amsmath`, `amssymb`, `amsthm`,
`mathtools`, `geometry`, `enumitem`, `hyperref`, `xcolor`, `graphicx`, `tikz`,
or `tikz-cd`; do not require external files, fonts, or shell commands. Do not
put Markdown fences or workflow commentary in it.

This is one autonomous benchmark attempt. Web search, browser tools, internet
research, apps, plugins, subagents, model subprocesses, canonical outputs,
published solutions to this prompt, sibling jobs, and other attempts are
forbidden. Use only local files in this job and your own mathematical
reasoning. Issue exactly one tool call at a time and wait for its result before
issuing another. Do not modify `problem.tex`, `plan.md`, `AGENTS.md`, Humanize state
files, or hook configuration. Do not stop at a plan merely because the
mathematics is difficult; distinguish proven claims from conjecture and
resolve every reviewer finding.
"""


def setup_job(problem: Problem, job_root: Path, codex_home: Path) -> None:
    job_root.mkdir(parents=True, exist_ok=False)

    (job_root / "problem.tex").write_text(problem.latex, encoding="utf-8")
    shutil.copyfile(Path(__file__).with_name("plan.md"), job_root / "plan.md")
    (job_root / "solution.tex").write_text(initial_solution(problem), encoding="utf-8")
    (job_root / "AGENTS.md").write_text(job_agents_file(), encoding="utf-8")
    (job_root / "worker-prompt.md").write_text(worker_prompt(problem), encoding="utf-8")
    (job_root / ".gitignore").write_text(
        ".codex-home/\n.humanize/\nruntime/\nworker-prompt.md\n", encoding="utf-8"
    )

    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    env["HUMANIZE_CODEX_BYPASS_SANDBOX"] = "true"
    env["XDG_CACHE_HOME"] = str(job_root / "runtime" / "cache")

    run_checked(["git", "init", "-b", "main"], job_root, env)
    run_checked(
        ["git", "config", "user.name", "First Proof Humanize Worker"], job_root, env
    )
    run_checked(
        ["git", "config", "user.email", "humanize-rlcr@localhost"], job_root, env
    )
    run_checked(
        [
            "git",
            "add",
            ".gitignore",
            "AGENTS.md",
            "plan.md",
            "problem.tex",
            "solution.tex",
        ],
        job_root,
        env,
    )
    run_checked(
        ["git", "commit", "-m", f"Initialize First Proof problem {problem.problem_id}"],
        job_root,
        env,
    )
    run_checked(["git", "checkout", "-b", "humanize-rlcr"], job_root, env)

    setup_script = HUMANIZE_ROOT / "scripts" / "setup-rlcr-loop.sh"
    run_checked(
        [
            str(setup_script),
            "plan.md",
            "--track-plan-file",
            "--max",
            str(MAX_RLCR_ROUNDS),
            "--codex-model",
            f"{MODEL}:{EFFORT}",
            "--codex-timeout",
            str(REVIEW_TIMEOUT_SECONDS),
            "--base-branch",
            "main",
            "--yolo",
            "--privacy",
        ],
        job_root,
        env,
    )


def loop_directories(job_root: Path) -> list[Path]:
    root = job_root / ".humanize" / "rlcr"
    if not root.is_dir():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir())


def humanize_complete(job_root: Path) -> bool:
    return any(
        (loop_dir / "complete-state.md").is_file()
        and (loop_dir / "complete-state.md").stat().st_size > 0
        for loop_dir in loop_directories(job_root)
    )


def humanize_lifecycle(job_root: Path) -> str:
    loops = loop_directories(job_root)
    if not loops:
        return "missing"
    loop_dir = loops[-1]
    for name in ("methodology-analysis-state.md", "finalize-state.md", "state.md"):
        if (loop_dir / name).is_file():
            return "active"
    terminal = sorted(loop_dir.glob("*-state.md"))
    if terminal:
        return terminal[0].name.removesuffix("-state.md")
    return "missing"


def valid_solution(path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    return (
        bool(re.search(r"\\documentclass(?:\[[^]]*\])?\{[^}]+\}", text))
        and r"\begin{document}" in text
        and text.endswith(r"\end{document}")
    )


def compile_solution(path: Path, log_path: Path) -> tuple[bool, int | None, str | None]:
    """Compile a standalone solution and enforce the benchmark page limit."""
    compiler = shutil.which("latexmk")
    pdfinfo = shutil.which("pdfinfo")
    if compiler is None or pdfinfo is None:
        missing = "latexmk" if compiler is None else "pdfinfo"
        reason = f"{missing} is not installed"
        atomic_write_text(log_path, reason + "\n")
        return False, None, reason

    output = "=== latexmk ===\n"
    try:
        with tempfile.TemporaryDirectory(prefix="first-proof-latex-") as directory:
            return_code, command_output, stop_reason = run_captured_process(
                [
                    compiler,
                    "-norc",
                    "-pdf",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    f"-outdir={directory}",
                    "-pdflatex=pdflatex -no-shell-escape %O %S",
                    str(path.resolve()),
                ],
                path.parent,
                LATEX_TIMEOUT_SECONDS,
            )
            output += command_output
            if stop_reason is not None:
                reason = (
                    "solution typesetting timed out"
                    if stop_reason == "timeout"
                    else "solution typesetting was interrupted by container shutdown"
                )
                atomic_write_text(log_path, output + f"\n{reason}\n")
                return False, None, reason
            if return_code != 0:
                atomic_write_text(log_path, output)
                return (
                    False,
                    None,
                    f"LaTeX compilation failed with exit code {return_code}",
                )

            metadata_code, metadata_output, stop_reason = run_captured_process(
                [pdfinfo, str(Path(directory) / f"{path.stem}.pdf")],
                path.parent,
                PDFINFO_TIMEOUT_SECONDS,
            )
            output += "\n=== pdfinfo ===\n" + metadata_output
            if stop_reason is not None:
                reason = (
                    "PDF inspection timed out"
                    if stop_reason == "timeout"
                    else "PDF inspection was interrupted by container shutdown"
                )
                atomic_write_text(log_path, output + f"\n{reason}\n")
                return False, None, reason
    except OSError as exc:
        reason = f"could not run solution validation command: {exc}"
        atomic_write_text(log_path, reason + "\n")
        return False, None, reason

    atomic_write_text(log_path, output)
    if metadata_code != 0:
        return False, None, f"pdfinfo failed with exit code {metadata_code}"
    match = re.search(r"^Pages:\s*(\d+)\s*$", metadata_output, re.MULTILINE)
    if match is None:
        return False, None, "pdfinfo did not report a PDF page count"
    pages = int(match.group(1))
    if pages > MAX_SOLUTION_PAGES:
        return (
            False,
            pages,
            f"compiled solution has {pages} pages; maximum is {MAX_SOLUTION_PAGES}",
        )
    return True, pages, None


def codex_command(job_root: Path) -> list[str]:
    return [
        "codex",
        "--dangerously-bypass-hook-trust",
        "--strict-config",
        "--disable",
        "standalone_web_search",
        "--disable",
        "browser_use",
        "--disable",
        "browser_use_external",
        "--disable",
        "browser_use_full_cdp_access",
        "--disable",
        "computer_use",
        "--disable",
        "in_app_browser",
        "--disable",
        "apps",
        "--disable",
        "plugins",
        "--disable",
        "remote_plugin",
        "--disable",
        "recommended_plugins",
        "--disable",
        "skill_search",
        "--disable",
        "multi_agent",
        "--disable",
        "multi_agent_v2",
        "--disable",
        "image_generation",
        "exec",
        "--dangerously-bypass-approvals-and-sandbox",
        "--color",
        "never",
        "--json",
        "-C",
        str(job_root),
        "-m",
        MODEL,
        "-c",
        f'model_provider="{MODEL_PROVIDER}"',
        "-c",
        f'model="{MODEL}"',
        "-c",
        f'review_model="{MODEL}"',
        "-c",
        f'model_reasoning_effort="{EFFORT}"',
        "-c",
        'web_search="disabled"',
        "-o",
        str(job_root / "last-message.md"),
        "-",
    ]


def session_processes(session_id: int) -> dict[int, int]:
    """Return live PID -> process-group mappings for one Linux session."""
    processes: dict[int, int] = {}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            stat = (entry / "stat").read_text(encoding="utf-8")
            fields = stat[stat.rfind(")") + 2 :].split()
            state, process_group, process_session = fields[0], int(fields[2]), int(fields[3])
        except (OSError, ValueError, IndexError):
            continue
        if process_session == session_id and state != "Z":
            processes[int(entry.name)] = process_group
    return processes


def signal_process_session(session_id: int, requested_signal: signal.Signals) -> None:
    processes = session_processes(session_id)
    own_group = os.getpgrp()
    for process_group in sorted(set(processes.values())):
        if process_group <= 1 or process_group == own_group:
            continue
        try:
            os.killpg(process_group, requested_signal)
        except ProcessLookupError:
            pass
    for process_id in processes:
        if process_id == os.getpid():
            continue
        try:
            os.kill(process_id, requested_signal)
        except ProcessLookupError:
            pass


def terminate_process_session(
    process: subprocess.Popen[bytes], grace_seconds: float = 30
) -> None:
    """Terminate every process in the worker's session, including nested timeout groups."""
    session_id = process.pid
    signal_process_session(session_id, signal.SIGTERM)
    deadline = time.monotonic() + grace_seconds
    while time.monotonic() < deadline:
        if process.poll() is None:
            try:
                process.wait(timeout=min(0.2, max(0.01, deadline - time.monotonic())))
            except subprocess.TimeoutExpired:
                pass
        if not session_processes(session_id):
            return
        time.sleep(0.05)
    signal_process_session(session_id, signal.SIGKILL)
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        pass


def run_captured_process(
    command: list[str],
    cwd: Path,
    timeout_seconds: float,
    termination_grace_seconds: float = 5,
) -> tuple[int, str, str | None]:
    """Run a command in an isolated session and reap its entire descendant tree."""
    with tempfile.TemporaryFile() as capture:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdout=capture,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        continue_running = SHUTDOWN.register(process)
        stop_reason: str | None = None
        desired_exit_code: int | None = None
        try:
            if not continue_running:
                stop_reason = "shutdown"
                desired_exit_code = 128 + (SHUTDOWN.signal_number or signal.SIGTERM)
            else:
                deadline = time.monotonic() + timeout_seconds
                while True:
                    if SHUTDOWN.event.is_set():
                        stop_reason = "shutdown"
                        desired_exit_code = 128 + (
                            SHUTDOWN.signal_number or signal.SIGTERM
                        )
                        break
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        stop_reason = "timeout"
                        desired_exit_code = 124
                        break
                    try:
                        process.wait(timeout=min(0.5, remaining))
                    except subprocess.TimeoutExpired:
                        continue
                    if SHUTDOWN.event.is_set():
                        stop_reason = "shutdown"
                        desired_exit_code = 128 + (
                            SHUTDOWN.signal_number or signal.SIGTERM
                        )
                    break

            if stop_reason is None:
                # The wrapper may have exited while leaving a compiler child behind.
                terminate_process_session(process, grace_seconds=0)
            else:
                terminate_process_session(
                    process, grace_seconds=termination_grace_seconds
                )
            capture.flush()
            capture.seek(0)
            output = capture.read().decode("utf-8", errors="replace")
            exit_code = (
                desired_exit_code
                if desired_exit_code is not None
                else process.returncode if process.returncode is not None else 1
            )
            return exit_code, output, stop_reason
        finally:
            if process.poll() is None or session_processes(process.pid):
                terminate_process_session(process, grace_seconds=0)
            SHUTDOWN.unregister(process)


class ShutdownController:
    """Coordinate container termination with every live Codex session."""

    def __init__(self) -> None:
        self.event = threading.Event()
        self._lock = threading.Lock()
        self._processes: dict[int, subprocess.Popen[bytes]] = {}
        self.signal_number: int | None = None

    def reset(self) -> None:
        with self._lock:
            self._processes.clear()
            self.signal_number = None
            self.event.clear()

    def register(self, process: subprocess.Popen[bytes]) -> bool:
        with self._lock:
            self._processes[process.pid] = process
            return not self.event.is_set()

    def unregister(self, process: subprocess.Popen[bytes]) -> None:
        with self._lock:
            self._processes.pop(process.pid, None)

    def request(self, signal_number: int) -> None:
        with self._lock:
            if self.signal_number is None:
                self.signal_number = signal_number
            self.event.set()
            session_ids = list(self._processes)
        for session_id in session_ids:
            signal_process_session(session_id, signal.SIGTERM)


SHUTDOWN = ShutdownController()


def handle_termination_signal(signal_number: int, _frame: object | None) -> None:
    SHUTDOWN.request(signal_number)


def run_codex_attempt(
    job_root: Path,
    codex_home: Path,
    event_path: Path,
    stderr_path: Path,
    timeout_seconds: int,
) -> tuple[int, str | None]:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    env["HUMANIZE_CODEX_BYPASS_SANDBOX"] = "true"
    env["HUMANIZE_GIT_TIMEOUT_SECONDS"] = "600"
    env["XDG_CACHE_HOME"] = str(job_root / "runtime" / "cache")
    command = codex_command(job_root)

    with (job_root / "worker-prompt.md").open("rb") as prompt_file, event_path.open(
        "wb"
    ) as event_file, stderr_path.open("wb") as stderr_file:
        process = subprocess.Popen(
            command,
            cwd=job_root,
            env=env,
            stdin=prompt_file,
            stdout=event_file,
            stderr=stderr_file,
            start_new_session=True,
        )
        continue_running = SHUTDOWN.register(process)
        try:
            if not continue_running:
                terminate_process_session(process, grace_seconds=0)
                return 128 + (SHUTDOWN.signal_number or signal.SIGTERM), (
                    "external termination requested"
                )
            attempt_deadline = time.monotonic() + timeout_seconds
            while True:
                if SHUTDOWN.event.is_set():
                    terminate_process_session(
                        process, grace_seconds=SHUTDOWN_GRACE_SECONDS
                    )
                    return 128 + (SHUTDOWN.signal_number or signal.SIGTERM), (
                        "external termination requested"
                    )
                remaining = attempt_deadline - time.monotonic()
                if remaining <= 0:
                    terminate_process_session(process)
                    return 124, "worker exceeded the shared run deadline"
                try:
                    exit_code = process.wait(timeout=min(0.5, remaining))
                except subprocess.TimeoutExpired:
                    continue
                terminate_process_session(process, grace_seconds=0)
                if SHUTDOWN.event.is_set():
                    return 128 + (SHUTDOWN.signal_number or signal.SIGTERM), (
                        "external termination requested"
                    )
                return exit_code, None
        finally:
            SHUTDOWN.unregister(process)


def copy_humanize_audit(job_root: Path, destination: Path) -> None:
    source = job_root / ".humanize" / "rlcr"
    if not source.is_dir():
        return
    for path in source.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(path, target)
        except OSError:
            # A live heartbeat may race a hook's atomic state transition.
            continue


def copy_runtime_logs(job_root: Path, destination: Path) -> None:
    last_message = job_root / "last-message.md"
    if last_message.is_file() and not last_message.is_symlink():
        try:
            shutil.copyfile(last_message, destination / "last-message.md")
        except OSError:
            pass

    cache_root = job_root / "runtime" / "cache"
    if not cache_root.is_dir():
        return
    for path in cache_root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(cache_root)
        target = destination / "humanize-cache" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(path, target)
        except OSError:
            continue


def blank_solution(problem: Problem, reason: str) -> str:
    del reason  # The detailed failure remains in run_manifest.json and logs.
    return f"""\\documentclass{{article}}
\\begin{{document}}
\\section*{{{latex_escape(problem.slug)}}}
No solution is submitted because the autonomous run did not complete.
\\end{{document}}
"""


def iter_token_records(codex_home: Path) -> Iterable[dict[str, Any]]:
    sessions = codex_home / "sessions"
    if not sessions.is_dir():
        return
    for rollout in sorted(sessions.rglob("rollout-*.jsonl")):
        stage = "codex_exec"
        workspace: str | None = None
        try:
            with rollout.open(encoding="utf-8", errors="replace") as stream:
                for line_number, line in enumerate(stream, start=1):
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if event.get("type") == "session_meta":
                        payload = event.get("payload") or {}
                        if isinstance(payload.get("cwd"), str):
                            workspace = payload["cwd"]
                        source = payload.get("source") or {}
                        if isinstance(source, dict):
                            stage = str(source.get("subagent") or payload.get("originator") or stage)
                        continue
                    if event.get("type") != "token_usage_record":
                        continue
                    payload = event.get("payload") or {}
                    usage = payload.get("usage") or {}
                    if not isinstance(usage, dict):
                        continue
                    record = {
                        "timestamp_utc": event.get("timestamp"),
                        "stage": stage,
                        "thread_id": payload.get("thread_id"),
                        "turn_id": payload.get("turn_id"),
                        "session_id": payload.get("session_id"),
                        "response_id": payload.get("response_id"),
                        "workspace": workspace,
                        "source": f"{rollout.name}:{line_number}",
                    }
                    for field in TOKEN_FIELDS:
                        value = usage.get(field, 0)
                        record[field] = value if isinstance(value, int) and value >= 0 else 0
                    yield record
        except OSError:
            continue


def collect_token_usage(
    problems: list[Problem],
    job_roots: dict[str, Path],
    codex_homes: Path | Iterable[Path],
    generated_at: str | None = None,
) -> dict[str, Any]:
    steps: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    problem_by_workspace = {
        str(job_root.resolve()): problem_id for problem_id, job_root in job_roots.items()
    }
    homes = (codex_homes,) if isinstance(codex_homes, Path) else tuple(codex_homes)
    for codex_home in homes:
        for record in iter_token_records(codex_home):
            workspace = record.get("workspace")
            if not isinstance(workspace, str):
                continue
            problem_id = problem_by_workspace.get(str(Path(workspace).resolve()))
            if problem_id is None:
                continue
            response_id = str(record.get("response_id") or record["source"])
            key = (problem_id, response_id)
            if key in seen:
                continue
            seen.add(key)
            steps.append({"problem_id": problem_id, **record})
    steps.sort(key=lambda item: (str(item.get("timestamp_utc")), item["problem_id"]))

    totals = {field: 0 for field in TOKEN_FIELDS}
    per_problem: dict[str, dict[str, int]] = {}
    for step in steps:
        problem_totals = per_problem.setdefault(
            step["problem_id"], {field: 0 for field in TOKEN_FIELDS}
        )
        for field in TOKEN_FIELDS:
            totals[field] += step[field]
            problem_totals[field] += step[field]

    return {
        "schema_version": 1,
        "generated_at_utc": generated_at or utc_now(),
        "model": MODEL,
        "reasoning_effort": EFFORT,
        "counting_note": (
            "reasoning_output_tokens is the hidden-reasoning subset reported by Codex; "
            "it is already included in output_tokens and is not added again to total_tokens."
        ),
        "totals": totals,
        "per_problem": per_problem,
        "steps": steps,
    }


class RunState:
    def __init__(
        self,
        problems: list[Problem],
        output_dir: Path,
        serving_node_by_problem: dict[str, str] | None = None,
    ) -> None:
        self._lock = threading.Lock()
        self.output_dir = output_dir
        self.started_at = utc_now()
        self.status: dict[str, dict[str, Any]] = {
            problem.problem_id: {
                "id": problem.problem_id,
                "output_file": problem.output_name,
                "status": "pending",
                "attempts": 0,
                **(
                    {"serving_node": serving_node_by_problem[problem.problem_id]}
                    if serving_node_by_problem is not None
                    else {}
                ),
            }
            for problem in problems
        }

    def update(self, problem_id: str, **changes: Any) -> None:
        with self._lock:
            self.status[problem_id].update(changes)
            self._write_locked()

    def snapshot(self) -> dict[str, dict[str, Any]]:
        with self._lock:
            return json.loads(json.dumps(self.status))

    def _write_locked(self) -> None:
        atomic_write_json(
            self.output_dir / "run_manifest.json",
            {
                "schema_version": 1,
                "started_at_utc": self.started_at,
                "updated_at_utc": utc_now(),
                "model": MODEL,
                "reasoning_effort": EFFORT,
                "problems": list(self.status.values()),
            },
        )

    def write(self) -> None:
        with self._lock:
            self._write_locked()


def monitor(
    stop: threading.Event,
    problems: list[Problem],
    job_roots: dict[str, Path],
    state: RunState,
    codex_homes: tuple[Path, ...],
) -> None:
    while True:
        snapshot = state.snapshot()
        counts: dict[str, int] = {}
        for item in snapshot.values():
            status = str(item["status"])
            counts[status] = counts.get(status, 0) + 1
        atomic_write_json(
            OUTPUT_DIR / "progress.json",
            {
                "timestamp_utc": utc_now(),
                "status": ", ".join(f"{key}={value}" for key, value in sorted(counts.items())),
                "problems_total": len(problems),
                "counts": counts,
            },
        )
        atomic_write_json(
            OUTPUT_DIR / "token_usage.json",
            collect_token_usage(problems, job_roots, codex_homes),
        )
        if stop.wait(HEARTBEAT_SECONDS):
            return


def solve_problem(
    problem: Problem,
    job_roots: dict[str, Path],
    state: RunState,
    deadline: float,
    max_restarts: int,
    codex_home: Path,
) -> None:
    job_root = job_roots[problem.problem_id]
    log_dir = OUTPUT_DIR / "logs" / problem.slug
    audit_dir = OUTPUT_DIR / "humanize" / problem.slug
    log_dir.mkdir(parents=True, exist_ok=True)
    if SHUTDOWN.event.is_set():
        reason = "external termination requested before worker start"
        atomic_write_text(OUTPUT_DIR / problem.output_name, blank_solution(problem, reason))
        state.update(
            problem.problem_id,
            status="failed",
            error=reason,
            finished_at_utc=utc_now(),
        )
        return
    state.update(problem.problem_id, status="preparing", started_at_utc=utc_now())

    try:
        setup_job(problem, job_root, codex_home)
    except Exception as exc:  # noqa: BLE001 - preserve failure for benchmark audit
        reason = f"setup failed: {exc}"
        atomic_write_text(OUTPUT_DIR / problem.output_name, blank_solution(problem, reason))
        state.update(problem.problem_id, status="failed", error=reason, finished_at_utc=utc_now())
        return

    final_exit_code: int | None = None
    error: str | None = None
    total_attempts = 1 + max_restarts
    for attempt in range(1, total_attempts + 1):
        if SHUTDOWN.event.is_set():
            error = "external termination requested"
            break
        remaining = int(deadline - time.monotonic())
        if remaining <= 60:
            error = "shared run deadline reached"
            break
        state.update(problem.problem_id, status="running", attempts=attempt)
        event_path = log_dir / f"worker-attempt-{attempt:02d}.events.jsonl"
        stderr_path = log_dir / f"worker-attempt-{attempt:02d}.stderr.log"
        final_exit_code, timeout_error = run_codex_attempt(
            job_root, codex_home, event_path, stderr_path, remaining
        )
        copy_humanize_audit(job_root, audit_dir)
        copy_runtime_logs(job_root, log_dir)
        if timeout_error:
            error = timeout_error
        if SHUTDOWN.event.is_set():
            error = "external termination requested"
            break
        lifecycle = humanize_lifecycle(job_root)
        if lifecycle == "complete":
            break
        if lifecycle != "active":
            error = error or f"Humanize ended with lifecycle state {lifecycle}"
            break
        if attempt < total_attempts and time.monotonic() + 60 < deadline:
            state.update(problem.problem_id, status="transport-restart")
            if SHUTDOWN.event.wait(60):
                error = "external termination requested"
                break
        else:
            error = error or f"RLCR incomplete after Codex exit {final_exit_code}"

    complete = humanize_complete(job_root)
    solution_path = job_root / "solution.tex"
    solution_structure_valid = valid_solution(solution_path)
    solution_compiles = False
    solution_pages: int | None = None
    validation_error: str | None = None
    if solution_structure_valid:
        solution_compiles, solution_pages, validation_error = compile_solution(
            solution_path, log_dir / "solution-validation.log"
        )
    if solution_structure_valid and solution_compiles:
        target = OUTPUT_DIR / problem.output_name
        temporary = target.with_name(f".{target.name}.{threading.get_ident()}.tmp")
        shutil.copyfile(solution_path, temporary)
        os.replace(temporary, target)
        changes: dict[str, Any] = {
            "status": "complete" if complete else "incomplete-submitted",
            "exit_code": final_exit_code,
            "humanize_complete": complete,
            "solution_valid": True,
            "solution_compiles": True,
            "solution_pages": solution_pages,
            "finished_at_utc": utc_now(),
        }
        if not complete:
            changes["incomplete_reason"] = error or "Humanize did not complete"
        state.update(problem.problem_id, **changes)
    else:
        if error:
            reason = error
        elif not complete:
            reason = "Humanize did not complete"
        elif not solution_structure_valid:
            reason = "Humanize completed but solution.tex failed the standalone LaTeX check"
        else:
            reason = validation_error or "Humanize completed but solution.tex did not validate"
        atomic_write_text(OUTPUT_DIR / problem.output_name, blank_solution(problem, reason))
        state.update(
            problem.problem_id,
            status="failed",
            exit_code=final_exit_code,
            humanize_complete=complete,
            solution_valid=solution_structure_valid and solution_compiles,
            solution_compiles=solution_compiles,
            solution_pages=solution_pages,
            error=reason,
            finished_at_utc=utc_now(),
        )
    copy_humanize_audit(job_root, audit_dir)
    copy_runtime_logs(job_root, log_dir)


def validate_environment(
    problems: list[Problem], nodes: tuple[ServingNode, ServingNode]
) -> None:
    if not authentication_available(nodes):
        missing = sorted(
            {
                node.api_key_env
                for node in nodes
                if not os.environ.get(node.api_key_env, "").strip()
            }
        )
        raise RuntimeError(
            f"set Kimi credential environment variable(s): {', '.join(missing)}"
        )
    required = [
        HUMANIZE_ROOT / "scripts" / "setup-rlcr-loop.sh",
        HUMANIZE_ROOT / "hooks" / "loop-codex-stop-hook.sh",
        Path(__file__).with_name("plan.md"),
        Path(__file__).with_name("kimi_responses_proxy.py"),
    ]
    for path in required:
        if not path.is_file():
            raise RuntimeError(f"required runtime file is missing: {path}")
    for command, description in (
        ("codex", "codex CLI"),
        ("curl", "curl"),
        ("latexmk", "latexmk"),
        ("pdflatex", "pdflatex"),
        ("pdfinfo", "pdfinfo"),
    ):
        if shutil.which(command) is None:
            raise RuntimeError(f"{description} is not installed")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    probe = OUTPUT_DIR / ".write-probe"
    probe.write_text("ok", encoding="utf-8")
    probe.unlink()
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    work_probe = WORK_DIR / ".write-probe"
    work_probe.write_text("ok", encoding="utf-8")
    work_probe.unlink()
    if not problems:
        raise RuntimeError("no problems to run")


def bounded_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if not minimum <= value <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return value


def main() -> int:
    SHUTDOWN.reset()
    signal.signal(signal.SIGTERM, handle_termination_signal)
    signal.signal(signal.SIGINT, handle_termination_signal)
    try:
        problems = parse_input(INPUT_PATH)
        nodes = serving_nodes()
        validate_environment(problems, nodes)
        if os.environ.get("HARNESS_VALIDATE_ONLY") == "1":
            print(
                f"validated {len(problems)} problem(s), {len(nodes)} Kimi serving nodes, "
                "Codex, Humanize, authentication, and output"
            )
            return 0

        parallelism = bounded_int(
            "MAX_PARALLEL_PROBLEMS", min(DEFAULT_PARALLELISM, len(problems)), 1, 32
        )
        max_restarts = bounded_int(
            "MAX_TRANSPORT_RESTARTS", DEFAULT_TRANSPORT_RESTARTS, 0, 5
        )
        run_seconds = bounded_int(
            "HARNESS_RUN_SECONDS", DEFAULT_RUN_SECONDS, 300, DEFAULT_RUN_SECONDS
        )
    except Exception as exc:  # noqa: BLE001 - turn validation into clear container failure
        print(f"fatal validation error: {exc}", file=sys.stderr)
        return 2

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    work_root = Path(tempfile.mkdtemp(prefix="first-proof-humanize-", dir=WORK_DIR))
    codex_homes = {
        node.name: work_root / f".codex-home-{node.name}" for node in nodes
    }
    hook_path = HUMANIZE_ROOT / "hooks" / "loop-codex-stop-hook.sh"
    try:
        # Each five-problem group has isolated provider configuration and
        # session storage. API keys remain environment-only.
        for node in nodes:
            prepare_codex_home(codex_homes[node.name], hook_path, node)
    except Exception as exc:  # noqa: BLE001 - fail before starting partial attempts
        print(f"fatal credential setup error: {exc}", file=sys.stderr)
        return 2
    proxy_processes: list[subprocess.Popen[bytes]] = []
    try:
        for node in nodes:
            proxy_processes.append(
                start_kimi_proxy(OUTPUT_DIR / "logs" / "transport" / node.name, node)
            )
    except Exception as exc:  # noqa: BLE001 - fail before starting partial attempts
        for process in reversed(proxy_processes):
            stop_kimi_proxy(process)
        print(f"fatal Kimi proxy startup error: {exc}", file=sys.stderr)
        return 2

    job_roots = {
        problem.problem_id: work_root / f"{problem.index:03d}-{problem.slug}"
        for problem in problems
    }
    problem_nodes = assign_serving_nodes(problems, nodes)
    state = RunState(
        problems,
        OUTPUT_DIR,
        {
            problem_id: node.name
            for problem_id, node in problem_nodes.items()
        },
    )
    state.write()
    deadline = time.monotonic() + run_seconds
    stop_monitor = threading.Event()
    monitor_thread = threading.Thread(
        target=monitor,
        args=(stop_monitor, problems, job_roots, state, tuple(codex_homes.values())),
        name="first-proof-heartbeat",
        daemon=True,
    )
    monitor_thread.start()

    try:
        # Interleave submissions so both serving nodes begin work even when an
        # operator lowers the global parallelism below ten.
        grouped = {
            node.name: [
                problem
                for problem in problems
                if problem_nodes[problem.problem_id].name == node.name
            ]
            for node in nodes
        }
        scheduled_problems: list[Problem] = []
        for item_index in range(max(len(group) for group in grouped.values())):
            for node in nodes:
                group = grouped[node.name]
                if item_index < len(group):
                    scheduled_problems.append(group[item_index])
        with concurrent.futures.ThreadPoolExecutor(max_workers=parallelism) as executor:
            futures = {
                executor.submit(
                    solve_problem,
                    problem,
                    job_roots,
                    state,
                    deadline,
                    max_restarts,
                    codex_homes[problem_nodes[problem.problem_id].name],
                ): problem
                for problem in scheduled_problems
            }
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as exc:  # noqa: BLE001 - keep other independent jobs alive
                    problem = futures[future]
                    reason = f"unexpected worker failure: {exc}"
                    print(f"{problem.problem_id}: {reason}", file=sys.stderr)
                    atomic_write_text(
                        OUTPUT_DIR / problem.output_name, blank_solution(problem, reason)
                    )
                    state.update(
                        problem.problem_id,
                        status="failed",
                        error=reason,
                        finished_at_utc=utc_now(),
                    )
    finally:
        stop_monitor.set()
        monitor_thread.join(timeout=10)
        for process in reversed(proxy_processes):
            stop_kimi_proxy(process)
    state.write()
    atomic_write_json(
        OUTPUT_DIR / "token_usage.json",
        collect_token_usage(problems, job_roots, tuple(codex_homes.values())),
    )
    snapshot = state.snapshot()
    complete = sum(1 for item in snapshot.values() if item["status"] == "complete")
    incomplete_submitted = sum(
        1 for item in snapshot.values() if item["status"] == "incomplete-submitted"
    )
    failed = len(problems) - complete - incomplete_submitted
    atomic_write_json(
        OUTPUT_DIR / "progress.json",
        {
            "timestamp_utc": utc_now(),
            "status": (
                f"finished: {complete} complete, "
                f"{incomplete_submitted} incomplete submitted, {failed} failed"
            ),
            "problems_total": len(problems),
            "complete": complete,
            "incomplete_submitted": incomplete_submitted,
            "failed": failed,
        },
    )
    print(
        f"finished {len(problems)} problem(s): {complete} complete, "
        f"{incomplete_submitted} incomplete submitted, {failed} failed"
    )
    if SHUTDOWN.signal_number is not None:
        return 128 + SHUTDOWN.signal_number
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
