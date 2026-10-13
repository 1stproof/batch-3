"""First Proof container entrypoint. No model calls during healthy supervision.

The container owns one campaign clock. Credentials live outside collected output.
This module never treats a PDF's existence as paper acceptance.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
import pwd
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time

SOURCE = Path(__file__).resolve().parent
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}\Z")


def now():
    return datetime.now(timezone.utc)


def save(path, value):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2) + "\n")
    tmp.replace(path)


def load(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return {} if default is None else default


def read_problems(path):
    data = json.loads(Path(path).read_text())
    if not isinstance(data, dict) or not isinstance(data.get("problems"), list):
        raise ValueError("input requires a problems array")
    result = {}
    for item in data["problems"]:
        if not isinstance(item, dict):
            raise ValueError("problem must be an object")
        ident, latex = item.get("id"), item.get("latex")
        if not isinstance(ident, str) or not IDENTIFIER.fullmatch(ident) or ident in result:
            raise ValueError("problem IDs must be unique safe file names")
        if not isinstance(latex, str) or not latex.strip():
            raise ValueError("problem latex must be nonempty")
        result[ident] = latex
    return result


def authenticate(codex, runtime_home):
    """One explicit API login; stdout/stderr may contain key fragments, never log them."""
    key = os.environ.pop("OPENAI_API_KEY", "")
    os.environ.pop("CODEX_API_KEY", None)
    if not key.strip():
        raise ValueError("OPENAI_API_KEY must be injected at container launch")
    runtime_home.mkdir(mode=0o700, parents=True, exist_ok=False)
    os.environ["CODEX_HOME"] = str(runtime_home)
    os.environ["MERLEAN_CODEX_AUTH"] = "api"
    process = subprocess.run([codex, "login", "--with-api-key"], input=key + "\n",
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    del key
    if process.returncode:
        raise RuntimeError("API login failed; credential output intentionally omitted")


def publish(root, output, identifiers):
    """Export useful manuscripts even before final acceptance, with explicit status."""
    records = {}
    for ident in identifiers:
        folder = root / "exam" / "papers" / ident
        light = folder / "light-paper-ledger.json"
        ledger = load(light if light.exists() else folder / "paper-ledger.json")
        record = {"paper_status": ledger.get("status", "not_started"),
                  "stage": ledger.get("stage"), "artifacts": []}
        if light.exists():
            record["paper_status"] = "incomplete"
            if ledger.get("stage") == "complete":
                try:
                    from pilot_paper_light import verify_completed
                    verify_completed(folder, root / "host")
                    record["paper_status"] = "complete"
                except (OSError, ValueError, KeyError, TypeError):
                    record["paper_status"] = "verification_failed"
        destination = output / "solutions" / ident
        for name in ("final.pdf", "paper.tex", "manuscript.tex", "final.tex", "raw-source.tex", "references.bib"):
            src = folder / name
            if src.is_file() and not src.is_symlink():
                destination.mkdir(parents=True, exist_ok=True)
                dst = destination / name
                if not dst.exists() or src.stat().st_mtime_ns > dst.stat().st_mtime_ns:
                    shutil.copy2(src, dst)
                record["artifacts"].append(str(dst.relative_to(output)))
        records[ident] = record
    save(output / "solution-status.json", records)
    return records


def usage_index(output):
    """Index native evidence without recounting usage or querying any session DB."""
    stages = []
    for path in output.glob("run-*/host/runtime/*/*/stage.meta.json"):
        meta = load(path)
        evidence = path.with_name("stage.response-usage.json")
        stages.append({"stage": meta.get("name"), "session": meta.get("session_id"),
            "status": meta.get("status"), "metadata": str(path.relative_to(output)),
            "usage_evidence": str(evidence.relative_to(output)) if evidence.exists() else None,
            "metering": meta.get("accounting", {}).get("metering", "UNKNOWN")})
    operations = [str(p.relative_to(output)) for p in (output / "operations").glob("state/incidents/*/*/events.jsonl")]
    save(output / "token-usage-index.json", {"stages": stages, "operations_events": operations,
        "operations_usage_evidence": [str(p.relative_to(output)) for p in (output / "operations").glob("state/incidents/*/*/stage.response-usage.json")],
        "operations_accounting_receipts": [str(p.relative_to(output)) for p in (output / "operations").glob("state/incidents/*/*/accounting-receipt.json")],
        "counts": "Use exact authenticated response usage; this index does not sum inherited copies.",
        "missing_usage": "UNKNOWN", "actual_billed_usd": None})


def command(root, problem_map, codex, start):
    args = ["--problems", str(problem_map), "--exam", "--exam-research-hours", "22.75",
            "--exam-total-hours", "24", "--exam-start-utc", start.isoformat(),
            "--codex", codex, "--internet-browse", "on", "--watchdog",
            "--source-url", "https://1stproof.org/assets/docs/batch3-call-for-submissions.pdf",
            "--lean-executable", "/opt/lean/bin/lean"]
    libraries = load("/opt/environment/probe-libraries.json", [])
    for library in libraries:
        args += ["--lean-library", library]
    return args


def child(command, log):
    with Path(log).open("ab") as stream:
        return subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stream,
                                stderr=stream, start_new_session=True)


def run(input_path, output, codex, started):
    identifiers = read_problems(input_path)
    output.mkdir(parents=True, exist_ok=True)
    # A container retry must not silently start a second attempt.
    reservation = output / "container-start.json"
    with reservation.open("x") as stream:
        json.dump({"start_utc": started.isoformat(),
                   "research_close_utc": (started + timedelta(hours=22.75)).isoformat(),
                   "deadline_utc": (started + timedelta(hours=24)).isoformat()}, stream)
    if not identifiers:
        save(output / "progress.json", {"timestamp_utc": now().isoformat(), "status": "empty_input"})
        return 0
    runtime = Path("/tmp/merlean-runtime")
    runtime.mkdir(mode=0o700, exist_ok=True)
    authenticate(codex, runtime / "codex")
    maintenance = output / "maintenance" / "source"
    shutil.copytree(SOURCE.parent, maintenance,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git"))
    inputs = output / "original-inputs"
    inputs.mkdir()
    for ident, latex in identifiers.items():
        (inputs / (ident + ".tex")).write_text(latex)
    problem_map = inputs / "problems.json"
    save(problem_map, {ident: ident + ".tex" for ident in identifiers})
    root, operation = output / "run-01", output / "supervisor-01"
    args = command(root, problem_map, codex, started)
    import pilot_supervisor as supervisor
    supervisor.recipe(operation, root, args)
    keeper = child([sys.executable, "-B", str(SOURCE / "pilot_supervisor.py"), "keep", str(operation)],
                   output / "keeper.log")
    ops_state = output / "operations" / "state"
    ops_state.parent.mkdir()
    ops_workspace = output / "operations" / "workspace"
    ops_workspace.mkdir()
    (ops_workspace / "OPERATIONS_CONTEXT.md").write_text(
        "# Submission operations\n\n"
        "This is one autonomous First Proof exam. Never ask for human mathematical guidance.\n"
        "The writable maintained source and tests are at " + str(maintenance) + ".\n"
        "Current native routing is at " + str(ops_state / "route.json") + ".\n"
        "Investigate only actual operational failures; healthy checks need no models.\n"
        "Repair the maintenance copy, independently review/test, then resume saved progress "
        "through native continuation. Never patch active/frozen roots or replay completed research.\n"
        "Preserve the original clock, model identities, scientific gates and consumed review allowances.\n"
        "Do not inspect, copy or print credentials. All required login is already configured.\n")
    ops = None
    retry_after = 0.0
    next_usage = 0.0
    deadline = started + timedelta(hours=24)
    active = root
    stopped = False

    def stop(signum, frame):
        nonlocal stopped
        stopped = True

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        while not stopped and now() < deadline:
            if (operation / "launch.json").is_file() and (root / "host-config.json").is_file() and not (ops_state / "config.json").exists():
                from pilot_operations import initialize
                initialize(ops_state, operation, Path(codex), ops_workspace,
                           container_tools=True)
            if (ops_state / "config.json").is_file() and (ops is None or ops.poll() is not None) and time.monotonic() >= retry_after:
                report = load(ops_state / "watcher-status.json")
                if report.get("status") not in ("exited", "original_deadline_reached"):
                    ops = child([sys.executable, "-B", str(SOURCE / "pilot_operations.py"), "watch", str(ops_state)],
                                output / "operations" / "observer.log")
                    retry_after = time.monotonic() + 30
            route = load(ops_state / "route.json")
            active = Path(route.get("root", str(root)))
            current_operation = Path(route.get("operation", str(operation)))
            if not active.is_relative_to(output) or not current_operation.is_relative_to(output):
                raise ValueError("operations route must remain inside submission output")
            records = publish(active, output, identifiers)
            if time.monotonic() >= next_usage:
                usage_index(output)
                next_usage = time.monotonic() + 300
            status = load(current_operation / "status.json")
            save(output / "progress.json", {"timestamp_utc": now().isoformat(),
                "status": status.get("status", "starting"), "route": str(active), "papers": records,
                "research_close_utc": (started + timedelta(hours=22.75)).isoformat(),
                "deadline_utc": deadline.isoformat()})
            if records and all(x["paper_status"] in ("complete", "polished") for x in records.values()) and status.get("status") == "exited" and not status.get("issues"):
                usage_index(output)
                return 0
            if keeper.poll() is not None and active == root and status.get("status") == "running":
                # Observe the SAME launch reservation; never replay host creation.
                keeper = child([sys.executable, "-B", str(SOURCE / "pilot_supervisor.py"), "watch", str(operation)],
                               output / "keeper.log")
            time.sleep(5)
        publish(active, output, identifiers)
        usage_index(output)
        save(output / "container-result.json", {"status": "interrupted" if stopped else "deadline_reached",
             "completed": False, "timestamp_utc": now().isoformat()})
        return 130 if stopped else 2
    finally:
        # Docker destroys remaining container-owned descendants on PID 1 exit.
        for process in (ops, keeper):
            if process is not None and process.poll() is None:
                process.terminate()


def main():
    started = now()  # Captured before login, campaign setup, or model dispatch.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("/data/input/input.json"))
    parser.add_argument("--output", type=Path, default=Path("/data/output"))
    parser.add_argument("--validate-input", action="store_true")
    args = parser.parse_args()
    if args.validate_input:
        print(json.dumps({"valid": True, "problem_count": len(read_problems(args.input))}))
        return 0
    if os.getuid() == 0:
        args.output.mkdir(parents=True, exist_ok=True)
        os.chown(args.output, 10001, 10001)
        os.setgroups([])
        os.setgid(10001)
        os.setuid(10001)
        os.environ["HOME"] = pwd.getpwuid(10001).pw_dir
    codex = shutil.which("codex")
    if not codex:
        raise RuntimeError("pinned Codex executable unavailable")
    try:
        return run(args.input.resolve(), args.output.resolve(), str(Path(codex).resolve()), started)
    except Exception as error:
        args.output.mkdir(parents=True, exist_ok=True)
        # Do not serialize exceptions from authentication/subprocess output.
        save(args.output / "container-error.json", {"error_type": type(error).__name__,
             "status": "startup_or_runtime_failed", "timestamp_utc": now().isoformat()})
        print("Submission stopped: " + type(error).__name__, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
