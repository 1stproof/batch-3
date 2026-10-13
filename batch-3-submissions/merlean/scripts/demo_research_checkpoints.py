#!/usr/bin/env python3
"""Exercise research memory through the CLI in a disposable synthetic campaign.

No LLM, Lean compiler, API, real campaign, or verification grade is involved.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix="merlean-checkpoint-demo-") as directory:
        workspace = Path(directory).resolve()
        data = workspace / "demo_data"

        def cli(*args):
            result = subprocess.run([sys.executable, str(ROOT / "src/offline_cli.py"),
                                     "--data", str(data), *args], check=True,
                                    capture_output=True, text=True, timeout=30)
            return json.loads(result.stdout)

        for sid, deps in [("local_fact", []), ("bridge", ["local_fact"]), ("research_goal", ["bridge"])]:
            cli("add", "--json", json.dumps({
                "id": sid, "content": "Synthetic obligation: " + sid,
                "anchor": "theorem " + sid + " : True", "dependencies": deps,
                "lean_path": sid + ".lean"}))
            (workspace / (sid + ".lean")).write_text("-- Synthetic candidate, not a certified proof.\n")
        initial_plan = (data / ".merlean-offline.json").read_bytes()

        def ready(mode):
            return cli("research-ready", "--root", "research_goal", "--mode", mode,
                       "--evidence-root", str(workspace))["ready"]

        before = {"interface": ready("interface"), "evidence": ready("evidence")}
        assert "research_goal" in before["interface"]
        assert "research_goal" not in before["evidence"]
        records = {}
        for sid in ["local_fact", "bridge", "research_goal"]:
            path = sid + ".lean"
            payload = {"expected_fingerprint": cli("research-snapshot", sid)["fingerprint"],
                       "outcome": "evidence_checkpoint", "evidence": [{"path": path,
                       "sha256": hashlib.sha256((workspace / path).read_bytes()).hexdigest()}],
                       "note": "Demonstrates byte identity only, not proof acceptance.",
                       "next_action": "Perform the actual research and grade audits."}
            records[sid] = cli("research-checkpoint", sid, "--evidence-root", str(workspace),
                               "--json", json.dumps(payload))
        after = ready("evidence")
        assert "research_goal" in after
        proposal = {"expected_fingerprint": cli("research-snapshot", "research_goal")["fingerprint"],
                    "checkpoint_id": records["research_goal"]["id"],
                    "change": "Explore a different representation before formalizing further.",
                    "reason": "The current route needs a relevance review.",
                    "consumer_impact": "Keep the original research question open; no assumptions changed."}
        cli("research-propose-revision", "research_goal", "--evidence-root", str(workspace),
            "--json", json.dumps(proposal))
        assert (data / ".merlean-offline.json").read_bytes() == initial_plan
        (workspace / "local_fact.lean").write_text("-- Changed dependency requires fresh review.\n")
        history = cli("research-checkpoints", "--evidence-root", str(workspace))
        assert all(not row["current"] for row in history)
        assert "research_goal" not in ready("evidence")
        assert (data / ".merlean-offline.json").read_bytes() == initial_plan
        print(json.dumps({"result": "PASS", "synthetic_workflow_only": True,
                          "before_checkpoints": before, "after_checkpoints_evidence_ready": after,
                          "after_dependency_edit_all_history_stale": True,
                          "retained_history_entries": len(history),
                          "target_status_and_grade_unchanged": True,
                          "model_calls": 0, "lean_proof_verification": False}, indent=2))


if __name__ == "__main__":
    main()
