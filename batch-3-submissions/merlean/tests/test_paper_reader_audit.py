from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.reader_audit import reader_audit_errors, shrink_justification_errors
from paper_writing_codex.tex_inventory import inventory_tex
from paper_writing_codex.versioning import sha256_file
from paper_writing_codex.workflow import init_refine, mark_gate, GATES
from paper_writing_codex.cli import _compile_tex


PAPER = r"""\documentclass{article}
\begin{document}
\section{Setup}
A compact space is defined using finite subcovers of open covers.

\input{bridge}
\section{Conclusion}
The argument above establishes the stated conclusion with all hypotheses retained.
\end{document}
"""
BRIDGE = r"""\begin{proof}\label{proof:bridge}
The finite subcover supplies the uniform bound needed to complete this implication.
\end{proof}
"""


class ReaderEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.paper = self.root / "paper.tex"
        self.paper.write_text(PAPER)
        (self.root / "bridge.tex").write_text(BRIDGE)
        self.state = {"work_dir": str(self.root), "output": str(self.paper)}
        self.inventory = inventory_tex(self.paper)
        (self.root / "05-pre-shrink-inventory.json").write_text(json.dumps({"inventory": self.inventory}))
        for name, identity, provenance in (
                ("first-pass.md", "fresh-reader", {"kind": "fresh", "manuscript_only": True}),
                ("proof-review.md", "proof-reviewer", {"kind": "independent-proof"})):
            (self.root / name).write_text(json.dumps({
                "reviewer_id": identity, "source_tree_sha256": self.inventory["source_tree_sha256"],
                "verdict": "PASS", "unresolved_findings": [], "provenance": provenance,
                "findings": "The finite subcover explains the bound with every hypothesis retained."}))
        (self.root / "source.txt").write_text("Standard terminology reference: compact space, finite subcover definition.")
        self.proof = next(u for u in self.inventory["units"] if u["kind"] == "proof")
        self.definition = next(u for u in self.inventory["units"] if "A compact space" in u.get("normalized_text", ""))
        self.record = {
            "verdict": "PASS", "reader_id": "fresh-reader", "writer_ids": ["writer"],
            "proof_auditor_id": "proof-reviewer", "fresh_context": True,
            "manuscript_only_first_pass": True,
            "first_pass_report": {"path": "first-pass.md", "sha256": sha256_file(self.root / "first-pass.md")},
            "proof_audit_report": {"path": "proof-review.md", "sha256": sha256_file(self.root / "proof-review.md")},
            "source_tree_sha256": self.inventory["source_tree_sha256"],
            "pre_shrink_sha256": sha256_file(self.root / "05-pre-shrink-inventory.json"),
            "read_order": self.inventory["reading_order"],
            "findings": {k: "The actual manuscript was checked with concrete evidence for " + k
                         for k in ("sequential_read", "proof_bridges", "terminology")},
            "proofs": [{"unit_id": self.proof["id"], "bridges": [{
                "claim": "The finite subcover yields a uniform bound.",
                "justification": "The maximum of the finitely many local bounds supplies the bound.",
                "location_unit_id": self.proof["id"],
            }]}],
            "terminology": [{"concept": "compactness", "term": "compact space", "status": "standard",
                "defining_unit_id": self.definition["id"], "rejected_variants": ["cover capsule"],
                "evidence": {"path": "source.txt", "sha256": sha256_file(self.root / "source.txt"),
                             "locator": "Definition paragraph on compact spaces."}}],
        }

    def check(self, record=None):
        (self.root / "07-reader-audit.json").write_text(json.dumps(self.record if record is None else record))
        return reader_audit_errors(self.state, required=True)

    def test_complete_evidence_and_actual_include_order(self):
        self.assertEqual([], self.check())
        order = self.inventory["reading_order"]
        conclusion = next(u["id"] for u in self.inventory["units"] if u.get("title") == "Conclusion")
        self.assertLess(order.index(self.definition["id"]), order.index(self.proof["id"]))
        self.assertLess(order.index(self.proof["id"]), order.index(conclusion))
        bad = copy.deepcopy(self.record)
        bad["read_order"].reverse()
        self.assertTrue(any("document order" in e for e in self.check(bad)))

    def test_missing_report_only_blocks_late_gates(self):
        self.assertEqual([], reader_audit_errors(self.state))
        self.assertTrue(reader_audit_errors(self.state, required=True))
        self.state["gates"] = {"terminology": {"status": "pass"}}
        self.assertTrue(reader_audit_errors(self.state))

    def test_empty_report_fails_closed(self):
        self.assertTrue(self.check({}))

    def test_rehashed_fail_stale_or_wrong_identity_cannot_approve(self):
        for field, name in (("first_pass_report", "first-pass.md"), ("proof_audit_report", "proof-review.md")):
            path = self.root / name
            original = json.loads(path.read_text())
            for change in ({"verdict": "FAIL"}, {"unresolved_findings": ["missing compactness inference"]},
                           {"reviewer_id": "writer"}, {"source_tree_sha256": "0" * 64}):
                with self.subTest(field=field, change=change):
                    path.write_text(json.dumps({**original, **change}))
                    record = copy.deepcopy(self.record)
                    record[field]["sha256"] = sha256_file(path)
                    self.assertTrue(self.check(record))
            path.write_text(json.dumps(original))

    def test_failed_first_read_requires_linked_current_passing_reread(self):
        path = self.root / "first-pass.md"
        first = json.loads(path.read_text())
        first.update(verdict="FAIL", unresolved_findings=["bridge missing"], source_tree_sha256="0" * 64)
        path.write_text(json.dumps(first))
        self.record["first_pass_report"]["sha256"] = sha256_file(path)
        self.assertTrue(self.check())
        final = {**first, "verdict": "PASS", "unresolved_findings": [],
                 "source_tree_sha256": self.inventory["source_tree_sha256"],
                 "provenance": {"kind": "reread", "manuscript_only": True,
                                "prior_report_sha256": sha256_file(path)}}
        final_path = self.root / "reread.json"
        final_path.write_text(json.dumps(final))
        self.record["final_reader_report"] = {"path": "reread.json", "sha256": sha256_file(final_path)}
        self.assertEqual([], self.check())
        final["provenance"]["prior_report_sha256"] = "f" * 64
        final_path.write_text(json.dumps(final))
        self.record["final_reader_report"]["sha256"] = sha256_file(final_path)
        self.assertTrue(self.check())

    def test_stale_include_and_first_pass_are_rejected(self):
        self.assertEqual([], self.check())
        (self.root / "bridge.tex").write_text(BRIDGE.replace("finite subcover", "missing bridge"))
        self.assertTrue(any("snapshot is stale" in e for e in self.check()))
        (self.root / "first-pass.md").write_text("Replaced evidence after the review.")
        self.assertTrue(any("first-pass evidence" in e for e in self.check()))

    def test_writer_cannot_self_certify_fresh_or_proof_read(self):
        for field, value in (("reader_id", " WRITER "), ("proof_auditor_id", "writer"),
                             ("proof_auditor_id", "fresh-reader"), ("fresh_context", False),
                             ("manuscript_only_first_pass", False)):
            with self.subTest(field=field, value=value):
                self.assertTrue(self.check({**self.record, field: value}))

    def test_proof_census_and_bridge_locations_are_required(self):
        self.assertTrue(self.check({**self.record, "proofs": []}))
        record = copy.deepcopy(self.record)
        record["proofs"][0]["bridges"][0]["location_unit_id"] = "nonexistent"
        self.assertTrue(self.check(record))
        record["proofs"][0]["bridges"] = []
        self.assertTrue(self.check(record))
        record["proofs"][0]["no_bridges_reason"] = "This proof is a single reflexive equality with no omitted inference."
        self.assertEqual([], self.check(record))

    def test_deleted_load_bearing_bridge_cannot_hide_in_recovery_ledger(self):
        snapshot_path = self.root / "05-pre-shrink-inventory.json"
        snapshot_path.write_text(json.dumps({"inventory": self.inventory}))
        (self.root / "bridge.tex").write_text("The conclusion follows.\n")
        new = inventory_tex(self.paper)
        self.record.update(source_tree_sha256=new["source_tree_sha256"], read_order=new["reading_order"],
                           proofs=[], pre_shrink_sha256=sha256_file(snapshot_path))
        self.assertTrue(any("proof_preservation" in e for e in self.check()))
        entry = {"original_unit_id": self.proof["id"], "disposition": "omitted_nonessential",
                 "reason": "The reader is expected to reconstruct the missing compactness argument.",
                 "load_bearing": True}
        self.record["proof_preservation"] = [entry]
        self.assertTrue(any("load-bearing" in e for e in self.check()))
        entry.update(disposition="preserved", replacement_unit_id="ledger:archive")
        self.assertTrue(any("surviving proof" in e for e in self.check()))

    def test_terminology_source_coinage_and_synonym_checks(self):
        record = copy.deepcopy(self.record)
        record["terminology"][0]["evidence"]["sha256"] = "stale"
        self.assertTrue(any("source/search" in e for e in self.check(record)))
        record = copy.deepcopy(self.record)
        record["terminology"][0]["status"] = "local"
        self.assertTrue(any("rationale" in e for e in self.check(record)))
        record = copy.deepcopy(self.record)
        record["terminology"][0]["rejected_variants"] = ["uniform bound"]
        self.assertTrue(any("unresolved terminology" in e for e in self.check(record)))

    def test_explicit_disjoint_notation_scopes_are_allowed(self):
        record = copy.deepcopy(self.record)
        first = record["terminology"][0]
        first.update(notation="X", notation_scope="Setup paragraph")
        second = copy.deepcopy(first)
        second.update(concept="cover", term="finite subcovers", notation_scope="Proof-local reset")
        record["terminology"].append(second)
        self.assertEqual([], self.check(record))
        second.pop("notation_scope")
        self.assertTrue(any("notation" in e for e in self.check(record)))

    def test_nonnegative_size_requires_reason_not_forced_deletion(self):
        for delta in (0, 7):
            self.assertTrue(shrink_justification_errors({"main_text_characters_delta": delta}))
            self.assertEqual([], shrink_justification_errors({"main_text_characters_delta": delta,
                "semantic_justification": "Retain the compactness-to-uniform-bound bridge needed by the reader."}))
        self.assertEqual([], shrink_justification_errors({"main_text_characters_delta": -1}))
        for delta in (True, float("nan"), "-10", None):
            self.assertTrue(shrink_justification_errors({"main_text_characters_delta": delta}))

    def test_late_mark_gate_does_not_accept_bare_pass_string(self):
        source = self.root / "original.tex"
        source.write_text(PAPER)
        initialized = init_refine(source)
        state_path = Path(initialized["work_dir"]) / "00-run-state.json"
        state = json.loads(state_path.read_text())
        for gate in GATES[:GATES.index("terminology")]:
            state["gates"][gate]["status"] = "pass"
        state_path.write_text(json.dumps(state))
        (Path(initialized["work_dir"]) / "07-reader-audit.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "07-reader-audit"):
            mark_gate(state_path, "terminology", "pass", ["looks good"])

    def test_tectonic_fallback_is_untrusted_and_isolated(self):
        (self.root / "refs.bib").write_text("@book{key,title={Title}}")
        self.paper.with_suffix(".pdf").write_bytes(b"old pdf must not count")
        before = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}

        def run(command, **kwargs):
            build = Path(kwargs["cwd"])
            self.assertNotEqual(build, self.root)
            self.assertIn("--untrusted", command)
            self.assertEqual((build / "bridge.tex").read_text(), BRIDGE)
            self.assertTrue((build / "refs.bib").is_file())
            self.assertFalse((build / "paper.pdf").exists())
            self.assertTrue(str(build) in kwargs["env"]["TEXINPUTS"])
            (build / "paper.pdf").write_bytes(b"new isolated pdf")
            (build / "paper.log").write_text("clean build")
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch("paper_writing_codex.cli.shutil.which", side_effect=lambda tool: "/test/tectonic" if tool == "tectonic" else None), patch(
                "paper_writing_codex.cli.subprocess.run", side_effect=run):
            result = _compile_tex(self.paper, 10)
        self.assertTrue(result["pass"], result)
        self.assertEqual("tectonic", result["engine"])
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()})

    def test_tectonic_no_new_pdf_does_not_pass_using_old_pdf(self):
        self.paper.with_suffix(".pdf").write_bytes(b"old pdf")
        with patch("paper_writing_codex.cli.shutil.which", side_effect=lambda tool: "/test/tectonic" if tool == "tectonic" else None), patch(
                "paper_writing_codex.cli.subprocess.run", return_value=subprocess.CompletedProcess([], 0, "", "")):
            self.assertFalse(_compile_tex(self.paper, 10)["pass"])

    def test_pdflatex_runs_fresh_bibtex_then_two_tex_passes(self):
        calls = []
        def run(command, **kwargs):
            build = Path(kwargs["cwd"])
            calls.append(Path(command[0]).name)
            self.assertNotEqual(build, self.root)
            if calls[-1] == "bibtex":
                self.assertEqual(command[1], "paper")
                self.assertFalse((build / "paper.bbl").exists())
                (build / "paper.bbl").write_text("Fresh bibliography")
            else:
                self.assertIn("-no-shell-escape", command)
                (build / "paper.aux").write_text(r"\bibdata{refs}\bibstyle{plain}")
                (build / "paper.pdf").write_bytes(b"pdf")
                (build / "paper.log").write_text("clean")
            return subprocess.CompletedProcess(command, 0, "", "")
        self.paper.with_suffix(".bbl").write_text("Stale original bibliography")
        with patch("paper_writing_codex.cli.shutil.which", side_effect=lambda tool:
                   "/test/" + tool if tool in {"pdflatex", "bibtex"} else None), patch(
                   "paper_writing_codex.cli.subprocess.run", side_effect=run):
            result = _compile_tex(self.paper, 10)
        self.assertTrue(result["pass"], result)
        self.assertEqual(calls, ["pdflatex", "bibtex", "pdflatex", "pdflatex"])
        self.assertEqual(self.paper.with_suffix(".bbl").read_text(), "Stale original bibliography")

    def test_pdflatex_missing_or_failed_bibtex_cannot_pass(self):
        for available in (False, True):
            calls = []
            def run(command, **kwargs):
                calls.append(Path(command[0]).name)
                build = Path(kwargs["cwd"])
                (build / "paper.aux").write_text(r"\bibdata{refs}")
                (build / "paper.pdf").write_bytes(b"first pass pdf")
                return subprocess.CompletedProcess(command, 1 if calls[-1] == "bibtex" else 0,
                                                   "bibliography failed", "")
            with patch("paper_writing_codex.cli.shutil.which", side_effect=lambda tool:
                       "/test/" + tool if tool == "pdflatex" or (available and tool == "bibtex") else None), patch(
                       "paper_writing_codex.cli.subprocess.run", side_effect=run):
                if available:
                    self.assertFalse(_compile_tex(self.paper, 10)["pass"])
                    self.assertEqual(calls, ["pdflatex", "bibtex"])
                else:
                    with self.assertRaisesRegex(RuntimeError, "bibtex is unavailable"):
                        _compile_tex(self.paper, 10)


if __name__ == "__main__":
    unittest.main()
