"""Fail-closed observations; no model calls or actual Lean/TeX builds."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import campaign_evidence as evidence
from paper_writing_codex import cli


class CampaignEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.answer = self.write("answer.md", "The complete answer.")
        self.data = {"grade": "SILVER", "provider": "codex", "manifest_author": "author", "implementers": ["worker"],
                     "final_answer": self.answer}
        self.manifest = self.base / "manifest.json"
        self.save()

    def write(self, name, value):
        path = self.base / name
        path.write_text(json.dumps(value) if isinstance(value, dict) else value)
        return {"path": name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    def save(self):
        self.manifest.write_text(json.dumps(self.data))

    def assess(self, **kwargs):
        return evidence.assess_evidence(self.manifest, mode=kwargs.pop("mode", "lite"), **kwargs)

    def silver(self):
        self.data["ledger"] = self.write("ledger.json", {"rows": [
            {"id": "S1", "closed": True, "triaged": True, "status": "lean-certified",
             "certificate": self.write("cert.lean", "theorem step : True := True.intro"),
             "axiom_report": self.write("axioms.txt", "step does not depend on any axioms"),
             "premise_manifest": self.write("premises.json", {"premises": []})}]})
        self.data["assumption_census"] = self.write("census.md", "No residual assumptions.")
        self.data["target_contract"] = self.write("target.json", {"statement": "True"})
        self.report = {"final_answer": self.answer, "reviewer": "skeptic", "implementers": ["worker"],
                       "verdict": "SILVER", "review_mode": "comprehensive", "triaged_rows": ["S1"],
                       "checks": {key: {"pass": True, "rationale": "The complete ledger and its inference boundaries were checked."}
                                  for key in evidence.SILVER_CHECKS},
                       "reviewer_provenance": self.write("dispatch.json", {"reviewer": "skeptic",
                                   "role": "lite_grade_review", "task_id": "independent-review",
                                   "provider": "codex", "model": "gpt-6-astra", "model_family": "astra",
                                   "final_answer_sha256": self.answer["sha256"],
                                   "ledger_sha256": self.data["ledger"]["sha256"]})}
        for key in ("ledger", "assumption_census", "target_contract"):
            self.report[key] = self.data[key]
        self.update_report()

    def update_report(self):
        self.data["silver_review"] = self.write("review.json", self.report)
        self.save()

    def test_bare_silver_grade_is_not_evidence(self):
        self.assertEqual(self.assess()["silver"]["status"], "pending")

    def test_silver_receipts_are_only_review_recorded(self):
        self.silver()
        observed = self.assess()["silver"]
        self.assertEqual(observed["status"], "review_recorded")
        self.assertIn("not independently replayed", observed["evidence_basis"])

    def test_silver_triaged_rows_requires_unique_nonempty_strings(self):
        self.silver()
        for value in (None, {}, 'S1', [{'id': 'S1'}, {'id': 'S2'}], ['S1', 1], [''], [' '], ['S1', 'S1']):
            with self.subTest(value=value):
                self.report['triaged_rows'] = value
                self.update_report()
                observed = self.assess()['silver']
                self.assertEqual(observed['status'], 'failed')
                self.assertIn('array of unique nonempty string row IDs', observed['details'][0])
        del self.report['triaged_rows']
        self.update_report()
        self.assertIn('array of unique nonempty string row IDs', self.assess()['silver']['details'][0])

    def test_silver_empty_census_only_matches_no_selected_rows(self):
        self.silver()
        self.report['triaged_rows'] = []
        self.update_report()
        self.assertIn('census differs', self.assess()['silver']['details'][0])
        ledger = {'rows': [{'id': 'S1', 'closed': True, 'triaged': False, 'status': 'proved'}]}
        self.data['ledger'] = self.write('ledger.json', ledger)
        self.report['ledger'] = self.data['ledger']
        provenance = json.loads((self.base / 'dispatch.json').read_text())
        provenance['ledger_sha256'] = self.data['ledger']['sha256']
        self.report['reviewer_provenance'] = self.write('dispatch.json', provenance)
        self.update_report()
        self.assertEqual(self.assess()['silver']['status'], 'review_recorded')
        self.report['triaged_rows'] = ['S1']
        self.update_report()
        self.assertIn('census differs', self.assess()['silver']['details'][0])

    def test_stale_transitive_silver_certificate_fails(self):
        self.silver()
        (self.base / "cert.lean").write_text("changed")
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_stale_answer_fails(self):
        (self.base / "answer.md").write_text("new answer")
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_same_reviewer_and_implementer_fails(self):
        self.silver()
        self.report["reviewer"] = "worker"
        self.update_report()
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_missing_substantive_check_fails(self):
        self.silver()
        self.report["checks"]["triage_complete"] = {"pass": True}
        self.update_report()
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_lite_never_runs_or_awards_gold(self):
        self.data["grade"] = "GOLD"
        self.save()
        with patch.object(evidence, "verify_kernel_runtime") as runtime, patch.object(evidence, "audit_manifest") as audit:
            self.assertEqual(self.assess()["gold"]["status"], "not_applicable")
            runtime.assert_not_called()
            audit.assert_not_called()

    def test_heavy_requires_runtime_and_full_audit(self):
        self.data["grade"] = "GOLD"
        self.save()
        with patch.object(evidence, "verify_kernel_runtime", return_value=["kernel failed"]), patch.object(evidence, "audit_manifest", return_value=[]) as audit:
            self.assertEqual(self.assess(mode="heavy")["gold"]["status"], "failed")
            self.assertFalse(audit.call_args.kwargs["kernel_runtime_verified"])
        with patch.object(evidence, "verify_kernel_runtime", return_value=[]), patch.object(evidence, "audit_manifest", return_value=[]):
            self.assertEqual(self.assess(mode="heavy")["gold"]["status"], "verified")

    def paper(self):
        ref = self.write("paper-state.json", {"final_answer": self.answer, "output": str(self.base / "answer.md"), "gates": {"final": {"status": "pass"}}})
        return self.base / ref["path"]

    def test_paper_gate_only_never_completes(self):
        state = self.paper()
        self.assertEqual(self.assess(paper_state=state)["paper"]["status"], "failed")

    def test_paper_full_audit_compile_and_page_limit(self):
        state = self.paper()
        with patch.object(evidence, "audit_paper", return_value={"pass": True, "errors": [], "compile": {"pass": True, "pdf_pages": 8}}) as audit:
            self.assertEqual(self.assess(paper_state=state, max_pages=8)["paper"]["status"], "complete")
            audit.assert_called_with(state.resolve(), require_all_gates=True)
            self.assertEqual(self.assess(paper_state=state, max_pages=7)["paper"]["status"], "failed")
        with patch.object(evidence, "audit_paper", return_value={"pass": True, "errors": []}):
            self.assertEqual(self.assess(paper_state=state)["paper"]["status"], "failed")

    def test_paper_different_answer_path_fails_before_audit(self):
        state = self.paper()
        copied = self.write("other-answer.md", "The complete answer.")
        state.write_text(json.dumps({"final_answer": copied}))
        with patch.object(evidence, "audit_paper") as audit:
            self.assertEqual(self.assess(paper_state=state)["paper"]["status"], "failed")
            audit.assert_not_called()

    def test_malformed_nested_paper_evidence_fails_closed(self):
        state = self.paper()
        state.write_text(json.dumps({"output": str(self.base / "answer.md"),
                                     "output_reservation": ["malformed"]}))
        result = self.assess(paper_state=state)["paper"]
        self.assertEqual(result["status"], "failed")
        self.assertIn("has no attribute", result["details"][0])

    def test_reference_escape_fails(self):
        self.data["final_answer"] = {"path": "../outside", "sha256": "0" * 64}
        self.save()
        self.assertIn("escapes", self.assess()["silver"]["details"][0])

    def test_silver_wrong_reviewer_model_fails(self):
        self.silver()
        self.report["reviewer_provenance"] = self.write("dispatch.json", {
            "reviewer": "skeptic", "role": "lite_grade_review", "task_id": "review",
            "provider": "codex", "model": "gpt-6-sol", "model_family": "sol"})
        self.update_report()
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_silver_dispatch_cannot_replay_another_answer_or_ledger(self):
        self.silver()
        for key in ("final_answer_sha256", "ledger_sha256"):
            provenance = json.loads((self.base / "dispatch.json").read_text())
            provenance[key] = "0" * 64
            self.report["reviewer_provenance"] = self.write("dispatch.json", provenance)
            self.update_report()
            result = self.assess()["silver"]
            self.assertEqual(result["status"], "failed")
            self.assertIn("dispatch provenance does not bind", result["details"][0])
            self.silver()

    def test_claude_silver_preserves_configured_model(self):
        self.silver()
        self.data["provider"] = "claude"
        provenance = json.loads((self.base / "dispatch.json").read_text())
        provenance.update(provider="claude", model="claude-opus-configured", model_family="opus")
        self.report["reviewer_provenance"] = self.write("dispatch.json", provenance)
        self.update_report()
        self.assertEqual(self.assess()["silver"]["status"], "review_recorded")
        provenance["model"] = ""
        self.report["reviewer_provenance"] = self.write("dispatch.json", provenance)
        self.update_report()
        self.assertEqual(self.assess()["silver"]["status"], "failed")

    def test_explicit_answer_ref_cannot_certify_different_output(self):
        state = self.paper()
        self.write("different.tex", "A different paper")
        state.write_text(json.dumps({"final_answer": self.answer, "output": str(self.base / "different.tex")}))
        with patch.object(evidence, "audit_paper") as audit:
            self.assertEqual(self.assess(paper_state=state)["paper"]["status"], "failed")
            audit.assert_not_called()

    def test_cli_preserves_output_and_failure_exit(self):
        from argparse import Namespace
        with patch.object(cli, "audit_paper", return_value={"pass": False}) as audit, patch.object(cli, "emit") as emit:
            with self.assertRaises(SystemExit) as caught:
                cli.cmd_audit(Namespace(state="paper.json", require_all_gates=False))
            self.assertEqual(caught.exception.code, 4)
            audit.assert_called_once_with(Path("paper.json"), require_all_gates=False)
            emit.assert_called_once_with({"pass": False})


if __name__ == "__main__":
    unittest.main()
