"""Research memory is advisory: exercise it without models or real campaign data."""
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from plan_store.offline_store import OfflinePlanGraph, STORE_NAME
from plan_store.research_checkpoint import ResearchCheckpoints


class ResearchCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp.name).resolve()
        self.data = self.workspace / "plan_data"
        self.graph = OfflinePlanGraph(self.data)
        for sid, deps in [("base", []), ("bridge", ["base"]), ("goal", ["bridge"]), ("unrelated", [])]:
            self.graph.add({"id": sid, "name": sid, "type": "Lemma",
                            "content": "original statement " + sid,
                            "anchor": "theorem " + sid + " : True",
                            "lean_path": sid + ".lean", "dependencies": deps})
            (self.workspace / (sid + ".lean")).write_text("-- candidate source for " + sid + "\n")
        self.graph.close()
        self.journal = ResearchCheckpoints(self.graph, self.workspace)

    def tearDown(self):
        self.temp.cleanup()

    def payload(self, sid="base", outcome="evidence_checkpoint"):
        name = sid + ".lean"
        return {"expected_fingerprint": self.journal.snapshot(sid)["fingerprint"],
                "outcome": outcome, "evidence": [{"path": name, "sha256": hashlib.sha256(
                    (self.workspace / name).read_bytes()).hexdigest()}],
                "note": "Operational evidence only; not a proof or grade.",
                "next_action": "Independent mathematical and intended-object review."}

    def test_checkpoint_and_proposal_never_mutate_theorem_or_grade(self):
        before = (self.data / STORE_NAME).read_bytes()
        record = self.journal.record("base", self.payload(outcome="counterexample_candidate"))
        self.journal.propose_revision("base", {
            "expected_fingerprint": self.journal.snapshot("base")["fingerprint"],
            "checkpoint_id": record["id"], "change": "Investigate a narrower conjecture.",
            "reason": "A suspected obstruction requires mathematical review.",
            "consumer_impact": "The original downstream claim remains unresolved."})
        self.journal.inspect()
        self.journal.ready(["goal"], mode="interface")
        self.graph.close()
        self.assertEqual((self.data / STORE_NAME).read_bytes(), before)
        self.assertIsNone(self.graph.get("base")["verification_grade"])
        self.assertEqual(self.graph.get("base")["status"], "pending")

    def test_unknown_fields_cannot_promote_grade_or_status(self):
        for field, value in [("verification_grade", "GOLD"), ("status", "completed"),
                             ("gold_audit", {}), ("open_assumptions", ["desired conclusion"])]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.journal.record("base", {**self.payload(), field: value})
        self.assertEqual(self.journal.inspect(), [])

    def test_target_revision_stales_descendants_but_retains_history(self):
        self.journal.record("base", self.payload())
        self.journal.record("bridge", self.payload("bridge"))
        self.journal.record("goal", self.payload("goal"))
        self.graph.update("base", content="a changed premise")
        rows = self.journal.inspect()
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(not row["current"] for row in rows))
        with self.assertRaises(ValueError):
            self.journal.record("goal", rows[-1]["payload"])

    def test_dependency_artifact_change_stales_downstream_evidence(self):
        self.journal.record("base", self.payload())
        self.journal.record("bridge", self.payload("bridge"))
        self.journal.record("goal", self.payload("goal"))
        (self.workspace / "base.lean").write_text("-- changed after checkpoint\n")
        self.assertTrue(all(not row["current"] for row in self.journal.inspect()))
        self.assertNotIn("goal", self.journal.ready(["goal"], mode="evidence")["ready"])

    def test_unrelated_note_and_metrics_do_not_invalidate_claim(self):
        self.journal.record("base", self.payload())
        self.graph.add({"id": "Note_route", "type": "Note", "content": "another route"})
        self.graph.record_metric("base", "worker", {"elapsed": 1})
        self.graph.set_status("base", "in_progress")
        self.assertTrue(self.journal.inspect("base")[0]["current"])

    def test_history_keeps_readable_original_statement_after_revision(self):
        self.journal.record("base", self.payload())
        original = self.graph.get("base")["content"]
        self.graph.update("base", content="a different research question")
        self.graph.close()
        row = ResearchCheckpoints(self.graph, self.workspace).inspect("base")[0]
        self.assertFalse(row["current"])
        self.assertEqual(row["target_snapshot"]["nodes"]["base"]["content"], original)

    def test_reject_evidence_escapes_missing_hash_and_symlinks(self):
        (self.workspace / "link.lean").symlink_to(self.workspace / "base.lean")
        for path in ["../outside.lean", str(self.workspace / "base.lean"), "missing.lean", "link.lean"]:
            payload = self.payload(outcome="progress")
            payload["evidence"][0]["path"] = path
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.journal.record("base", payload)
        payload = self.payload(); payload["evidence"][0]["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            self.journal.record("base", payload)
        self.assertEqual(self.journal.inspect(), [])

    def test_evidence_root_cannot_be_substituted(self):
        self.journal.record("base", self.payload())
        other = self.workspace / "other"; other.mkdir()
        (other / "base.lean").write_bytes((self.workspace / "base.lean").read_bytes())
        with self.assertRaises(ValueError):
            ResearchCheckpoints(self.graph, other).inspect()

    def test_interface_speculation_and_evidence_reuse_are_distinct(self):
        interfaces = self.journal.ready(["goal"], mode="interface")
        self.assertIn("goal", interfaces["ready"])
        self.assertNotIn("unrelated", interfaces["ready"])
        self.assertNotIn("bridge", self.journal.ready(["goal"], mode="evidence")["ready"])
        self.journal.record("base", self.payload())
        self.assertIn("bridge", self.journal.ready(["goal"], mode="evidence")["ready"])
        self.assertNotIn("goal", self.journal.ready(["goal"], mode="evidence")["ready"])
        self.graph.set_status("base", "completed_axiom")
        for mode in ["interface", "evidence"]:
            self.assertNotIn("goal", self.journal.ready(["goal"], mode=mode)["ready"])

    def test_missing_dependencies_and_cycles_fail_closed(self):
        self.graph.update("base", dependencies=["absent"])
        self.assertFalse(self.journal.snapshot("goal")["valid"])
        self.assertNotIn("goal", self.journal.ready(["goal"])["ready"])
        self.graph.update("base", dependencies=["goal"])
        self.assertFalse(self.journal.snapshot("goal")["valid"])
        with self.assertRaises(ValueError):
            self.journal.record("goal", self.payload("goal", "proof_failure"))

    def test_integration_failure_retains_current_mathematical_evidence(self):
        self.journal.record("base", self.payload())
        self.journal.record("base", self.payload(outcome="integration_failure"))
        self.assertIn("bridge", self.journal.ready(["goal"], mode="evidence")["ready"])
        self.journal.record("bridge", self.payload("bridge"))
        history = self.journal.inspect("base")
        self.assertEqual({r["payload"]["outcome"] for r in history},
                         {"evidence_checkpoint", "integration_failure"})
        (self.workspace / "base.lean").write_text("-- stale after source edit")
        self.assertNotIn("bridge", self.journal.ready(["goal"], mode="evidence")["ready"])

    def test_proposal_must_reference_current_same_node_checkpoint(self):
        record = self.journal.record("base", self.payload())
        payload = {"expected_fingerprint": self.journal.snapshot("bridge")["fingerprint"],
                   "checkpoint_id": record["id"], "change": "change", "reason": "reason",
                   "consumer_impact": "original goal still unresolved"}
        with self.assertRaises(ValueError):
            self.journal.propose_revision("bridge", payload)

    def run_cli(self, *args, data=None):
        return subprocess.run([sys.executable, str(ROOT / "src/offline_cli.py"),
                               "--data", str(data or self.data), *args], cwd=ROOT,
                              capture_output=True, text=True, timeout=30)

    def test_concurrent_cli_writes_preserve_all_events(self):
        payload = json.dumps(self.payload(outcome="proof_failure"))
        args = ["research-checkpoint", "base", "--evidence-root", str(self.workspace), "--json", payload]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda _: self.run_cli(*args), range(6)))
        self.assertTrue(all(r.returncode == 0 for r in results), [r.stderr for r in results])
        rows = ResearchCheckpoints(self.graph, self.workspace).inspect()
        self.assertEqual(len(rows), 6)
        self.assertEqual(len({r["id"] for r in rows}), 6)

    def test_cli_does_not_initialize_or_migrate_statement_only_plan(self):
        data = self.workspace / "legacy_data"; data.mkdir()
        source = data / "statements.json"; source.write_text('{"statements": []}\n')
        before = source.read_bytes()
        result = self.run_cli("research-snapshot", "goal", data=data)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((data / STORE_NAME).exists())
        self.assertEqual(source.read_bytes(), before)

    def test_corrupt_journal_is_not_replaced(self):
        self.journal.record("base", self.payload())
        path = self.data / ".merlean-research-checkpoints.json"
        path.write_text('{"version":1,"version":2}')
        with self.assertRaises(ValueError):
            ResearchCheckpoints(self.graph, self.workspace)
        self.assertEqual(path.read_text(), '{"version":1,"version":2}')

    def test_four_research_packages_share_safe_checkpoint_behavior(self):
        for provider in ["codex", "claude"]:
            for mode in ["lite", "heavy"]:
                package = ROOT / "plugins" / ("merlean-" + mode + "-" + provider)
                with self.subTest(provider=provider, mode=mode):
                    def run(*args):
                        return subprocess.run([sys.executable, str(package / "src/offline_cli.py"),
                                               "--data", str(self.data), *args], capture_output=True,
                                              text=True, timeout=30)
                    before = (self.data / STORE_NAME).read_bytes()
                    snap = run("research-snapshot", "base")
                    self.assertEqual(snap.returncode, 0, snap.stderr)
                    payload = self.payload(outcome="progress")
                    payload["expected_fingerprint"] = json.loads(snap.stdout)["fingerprint"]
                    args = ["research-checkpoint", "base", "--evidence-root", str(self.workspace), "--json"]
                    result = run(*args, json.dumps(payload))
                    self.assertEqual(result.returncode, 0, result.stderr)
                    result = run(*args, json.dumps({**payload, "verification_grade": "GOLD"}))
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual((self.data / STORE_NAME).read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
