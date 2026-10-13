from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.reader_rounds import reader_round_errors
from paper_writing_codex.reader_rounds import READER_POLICY, READER_RUBRIC, READER_AXES, isolated_manuscript
from paper_writing_codex.tex_inventory import inventory_tex
from paper_writing_codex.versioning import sha256_file
from paper_writing_codex.workflow import init_compose, mark_gate, resume_point


class ReaderRoundTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name).resolve()
        self.state = init_compose(root / "paper-v1.tex")
        self.state['reader_round_policy'] = 'two-fresh-astra-v1'
        self.output = Path(self.state["output"])
        self.work = Path(self.state["work_dir"])
        self.guideline = self.work / "guideline.md"
        self.guideline.write_text("Explain mathematical hypotheses and each necessary proof implication clearly.")
        self.ledger_path = self.work / "08-reader-rounds.json"

    def save(self, name, record):
        path = self.work / name
        path.write_text(json.dumps(record))
        return {"path": name, "sha256": sha256_file(path)}

    def patch_ref(self, reference, update):
        path = self.work / reference["path"]
        record = json.loads(path.read_text())
        update(record)
        path.write_text(json.dumps(record))
        reference["sha256"] = sha256_file(path)

    def write_ledger(self, ledger):
        self.ledger_path.write_text(json.dumps(ledger))

    def fixture(self, *, no_op=False):
        self.output.write_text("\\documentclass{article}\\begin{document}The conditional statement needs its premise.\\end{document}")
        guideline_hash = sha256_file(self.guideline)
        rounds = []
        disposition_hashes = []
        for index in (1, 2):
            before = inventory_tex(self.output)
            self.work.joinpath(f'input-{index}.tex').write_bytes(self.output.read_bytes())
            before_ref = self.save(f"before-{index}.json", before)
            report = {"reviewer_id": f"reader-{index}", "model": "gpt-6-astra",
                "provenance": {"kind": "fresh", "prior_context": False, "manuscript_and_guideline_only": True},
                "source_tree_sha256": before["source_tree_sha256"], "guideline_sha256": guideline_hash,
                "findings": "The synthetic reader inspected the stated premise and its explanation.",
                "issues": [{"id": f"issue-{index}", "severity": "substantive",
                            "finding": "Explain why the retained premise supplies the necessary implication."}]}
            reader_ref = self.save(f"reader-{index}.json", report)
            if not no_op:
                self.output.write_text(self.output.read_text().replace("\\end{document}",
                    f" Added the explicit explanation for premise {index}.\\end{{document}}"))
            after = inventory_tex(self.output)["source_tree_sha256"]
            disposition = {"writer_id": "writer", "reader_report_sha256": reader_ref["sha256"],
                "before_source_tree_sha256": before["source_tree_sha256"], "after_source_tree_sha256": after,
                "revision_summary": "The actual synthetic revision explains how the premise is used.",
                "responses": [{"issue_id": f"issue-{index}", "action": "justified-no-op" if no_op else "revised",
                               "reason": "The required explanation is already complete." if no_op else "Added the missing implication using the existing premise."}]}
            if no_op:
                disposition["no_change_reason"] = "The requested explanation was already explicit in the supplied synthetic text."
            disposition_ref = self.save(f"disposition-{index}.json", disposition)
            rounds.append({"reader_id": f"reader-{index}", "before_source_tree_sha256": before["source_tree_sha256"],
                "before_inventory": before_ref, "reader_report": reader_ref,
                "after_source_tree_sha256": after, "disposition_report": disposition_ref})
            disposition_hashes.append(disposition_ref["sha256"])
        verification = {"reviewer_id": "reader-2", "model": "gpt-6-astra",
            "provenance": {"kind": "post-revision-verification", "stylistic_round": False},
            "source_tree_sha256": rounds[-1]["after_source_tree_sha256"], "guideline_sha256": guideline_hash,
            "disposition_report_sha256s": disposition_hashes, "verdict": "PASS", "unresolved_substantive_issues": [],
            "findings": "Verified that both recorded issue dispositions are supported by the final manuscript."}
        ledger = {"schema_version": 1, "guideline": {"path": "guideline.md", "sha256": guideline_hash},
                  "writer_ids": ["writer"], "rounds": rounds,
                  "final_verification": self.save("verification.json", verification)}
        self.write_ledger(ledger)
        return ledger

    def isolated_fixture(self):
        ledger = self.fixture()
        self.state['reader_round_policy'] = READER_POLICY
        self.guideline.write_text(READER_RUBRIC)
        ledger['guideline']['sha256'] = sha256_file(self.guideline)
        ledger['schema_version'] = 2
        axes = {axis: {'verdict': 'PASS', 'findings': 'The synthetic manuscript supports this isolated axis assessment.',
                       'unresolved_findings': []} for axis in READER_AXES}
        for index, item in enumerate(ledger['rounds'], 1):
            path = self.work / f'input-{index}.tex'
            item['manuscript_input'] = {'path': path.name, 'sha256': sha256_file(path)}
            self.patch_ref(item['reader_report'], lambda report: report.update(
                guideline_sha256=ledger['guideline']['sha256'], axes=axes,
                manuscript_sha256=sha256_file(path), provenance={'kind': 'fresh', 'prior_context': False,
                'sole_scientific_input': 'manuscript', 'rubric_is_instruction': True},
                issues=[{**issue, 'axis': 'exposition', 'location': 'opening premise'} for issue in report['issues']]))
            self.patch_ref(item['disposition_report'], lambda report: report.update(
                reader_report_sha256=item['reader_report']['sha256']))
        path = self.work / 'final-input.tex'
        path.write_bytes(self.output.read_bytes())
        ledger['final_manuscript_input'] = {'path': path.name, 'sha256': sha256_file(path)}
        self.patch_ref(ledger['final_verification'], lambda report: report.update(
            guideline_sha256=ledger['guideline']['sha256'], manuscript_sha256=sha256_file(path), axes=axes,
            disposition_report_sha256s=[item['disposition_report']['sha256'] for item in ledger['rounds']]))
        self.write_ledger(ledger)
        return ledger

    def test_isolated_two_axis_paper_contract(self):
        self.isolated_fixture()
        self.assertEqual(reader_round_errors(self.state, required=True), [])

    def test_isolated_contract_rejects_relabeling_missing_axes_and_wrong_input(self):
        for mode in ('legacy', 'axis', 'location', 'input', 'final-axis', 'rubric'):
            with self.subTest(mode=mode):
                ledger = self.isolated_fixture()
                if mode == 'legacy':
                    ledger['schema_version'] = 1
                elif mode == 'axis':
                    self.patch_ref(ledger['rounds'][0]['reader_report'], lambda report: report['axes'].pop('attribution'))
                elif mode == 'location':
                    self.patch_ref(ledger['rounds'][0]['reader_report'], lambda report: report['issues'][0].pop('location'))
                elif mode == 'input':
                    path = self.work / ledger['rounds'][0]['manuscript_input']['path']
                    path.write_text(path.read_text() + 'Different source bytes')
                    ledger['rounds'][0]['manuscript_input']['sha256'] = sha256_file(path)
                elif mode == 'final-axis':
                    self.patch_ref(ledger['final_verification'], lambda report: report['axes']['exposition'].update(verdict='FAIL'))
                else:
                    self.guideline.write_text(READER_RUBRIC + 'Author says the proof is correct.')
                    ledger['guideline']['sha256'] = sha256_file(self.guideline)
                self.write_ledger(ledger)
                self.assertTrue(reader_round_errors(self.state, required=True))

    def test_single_tex_filter_preserves_inline_bibliography_and_normal_packages(self):
        text = r'\documentclass{article}\usepackage{amsmath,amssymb}\begin{document}\begin{thebibliography}{1}\bibitem{a} A. Author.\end{thebibliography}\end{document}'
        self.assertEqual(isolated_manuscript(text), text)
        for command in (r'\input{chapter}', r'\input chapter', r'\bibliography{refs}', r'\includegraphics{figure}', r'\csname input\endcsname'):
            with self.assertRaises(ValueError):
                isolated_manuscript(text.replace(r'\end{document}', command + r'\end{document}'))

    def test_two_actual_revision_cycles_and_final_verification(self):
        self.fixture()
        self.assertEqual(reader_round_errors(self.state, required=True), [])

    def test_justified_no_op_does_not_require_editorial_changes(self):
        self.fixture(no_op=True)
        self.assertEqual(reader_round_errors(self.state, required=True), [])

    def test_missing_cycles_legacy_inspection_and_late_gate(self):
        self.assertEqual(reader_round_errors(self.state), [])
        self.assertTrue(reader_round_errors(self.state, required=True))
        state = self.state
        state.pop("reader_round_policy")
        self.work.joinpath("00-run-state.json").write_text(json.dumps(state))
        self.assertEqual(resume_point(self.work / "00-run-state.json")["next_gate"], "critical-path")
        for gate in state["gates"]:
            state["gates"][gate]["status"] = "pass"
        # Other substantive checks remain active too; verify the round check itself
        # through its required release API without mocking trust evidence.
        self.assertTrue(reader_round_errors(state, required=True))

    def test_round_count_identity_and_continuity(self):
        for mode in ("one", "three", "same-reader", "writer-reader", "discontinuity"):
            with self.subTest(mode=mode):
                ledger = self.fixture()
                if mode == "one":
                    ledger["rounds"].pop()
                elif mode == "three":
                    ledger["rounds"].append(ledger["rounds"][1])
                elif mode == "same-reader":
                    ledger["rounds"][1]["reader_id"] = " READER-1 "
                elif mode == "writer-reader":
                    ledger["writer_ids"].append(" READER-1 ")
                else:
                    ledger["rounds"][1]["before_source_tree_sha256"] = "0" * 64
                self.write_ledger(ledger)
                self.assertTrue(reader_round_errors(self.state, required=True))

    def test_reader_requires_fresh_astra_context_and_substantive_findings(self):
        for update in ({"model": "gpt-5.5"}, {"findings": "PASS"}, {"findings": {}},
                       {"provenance": {"kind": "fresh", "prior_context": True, "manuscript_and_guideline_only": True}}):
            with self.subTest(update=update):
                ledger = self.fixture()
                self.patch_ref(ledger["rounds"][0]["reader_report"], lambda report: report.update(update))
                self.write_ledger(ledger)
                self.assertTrue(reader_round_errors(self.state, required=True))

    def test_duplicate_issues_and_missing_or_duplicate_responses(self):
        for mode in ("issues", "missing", "duplicate"):
            with self.subTest(mode=mode):
                ledger = self.fixture()
                item = ledger["rounds"][0]
                if mode == "issues":
                    self.patch_ref(item["reader_report"], lambda report: report["issues"].append(report["issues"][0]))
                elif mode == "missing":
                    self.patch_ref(item["disposition_report"], lambda report: report.update({"responses": []}))
                else:
                    self.patch_ref(item["disposition_report"], lambda report: report["responses"].append(report["responses"][0]))
                self.write_ledger(ledger)
                self.assertTrue(reader_round_errors(self.state, required=True))

    def test_final_substantive_failure_and_stale_manuscript_or_guideline(self):
        for mode in ("failure", "unresolved", "manuscript", "guideline"):
            with self.subTest(mode=mode):
                ledger = self.fixture()
                if mode in {"failure", "unresolved"}:
                    update = {"verdict": "FAIL"} if mode == "failure" else {"unresolved_substantive_issues": ["Still missing implication"]}
                    self.patch_ref(ledger["final_verification"], lambda report: report.update(update))
                elif mode == "manuscript":
                    self.output.write_text(self.output.read_text() + "Changed after verification")
                else:
                    self.guideline.write_text(self.guideline.read_text() + "New instruction")
                self.write_ledger(ledger)
                self.assertTrue(reader_round_errors(self.state, required=True))

    def test_before_inventory_internal_hash_and_legacy_second_reader_identity(self):
        ledger = self.fixture()
        self.patch_ref(ledger["rounds"][0]["before_inventory"],
                       lambda report: report["source_files"][0].update({"sha256": "0" * 64}))
        self.write_ledger(ledger)
        self.assertTrue(reader_round_errors(self.state, required=True))
        self.fixture()
        self.save("07-reader-audit.json", {"reader_id": "third-reader", "writer_ids": ["writer"]})
        self.assertTrue(reader_round_errors(self.state, required=True))
        self.save("07-reader-audit.json", {"reader_id": "reader-2", "writer_ids": ["writer"]})
        self.assertEqual(reader_round_errors(self.state, required=True), [])


if __name__ == "__main__":
    unittest.main()
