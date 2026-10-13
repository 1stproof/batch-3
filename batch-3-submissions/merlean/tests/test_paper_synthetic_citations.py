from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.coverage import (
    _synthetic_citation, _synthetic_citation_archive_errors, audit_refinement, lock_main_results,
)
from paper_writing_codex.tex_inventory import digest_text
from paper_writing_codex.workflow import init_refine


class SyntheticCitationArchiveTests(unittest.TestCase):
    def setUp(self):
        self.unit = {"id": "citation:old-key", "kind": "citation", "label": "old-key",
                     "normalized_text": "old-key", "normalized_sha256": digest_text("old-key")}
        self.entry = {"classification": "LEDGER_ONLY", "archive_anchor": "omitted-citation",
            "reason": "Unrelated historical context was removed after review.", "source": "approved baseline",
            "consumer": "separately archived historical prose", "evidence": "Independent scope review accepted omission.",
            "archived_text": "old-key", "archived_text_sha256": digest_text("old-key")}
        self.archive = "# omitted-citation\n\nold-key\n"

    def test_only_synthetic_citation_can_omit_raw_bytes(self):
        self.assertTrue(_synthetic_citation(self.unit))
        for kind in ("prose", "proof", "statement"):
            self.assertFalse(_synthetic_citation({**self.unit, "kind": kind}))
        self.assertFalse(_synthetic_citation({**self.unit, "raw_text": "\\cite{old-key}"}))
        self.assertEqual(_synthetic_citation_archive_errors(self.unit, self.entry, {"citations": []}, self.archive), [])
        self.assertEqual(_synthetic_citation_archive_errors(self.unit,
            {**self.entry, "archived_raw_text": None, "archived_raw_sha256": None}, {"citations": []}, self.archive), [])

    def test_raw_fabrication_live_key_wrong_hash_missing_evidence_and_archive_fail(self):
        for change in ({"archived_raw_text": "\\cite{old-key}"}, {"archived_raw_sha256": "0" * 64},
                       {"archived_text_sha256": "0" * 64}, {"archived_text": "different-key"},
                       {"evidence": None}, {"reason": None}, {"source": None}, {"consumer": None},
                       {"archive_anchor": "missing-anchor"}):
            with self.subTest(change=change):
                self.assertTrue(_synthetic_citation_archive_errors(self.unit, {**self.entry, **change},
                                                                 {"citations": []}, self.archive))
        self.assertTrue(_synthetic_citation_archive_errors(self.unit, self.entry, {"citations": ["old-key"]}, self.archive))
        self.assertTrue(_synthetic_citation_archive_errors(self.unit, self.entry, {"citations": []}, "# omitted-citation\n"))

    def test_normal_prose_coverage_remains_separate_and_verbatim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            source = root / "paper.tex"
            context = "This unrelated historical context cites an outside work \\cite{old-key}."
            text = ("\\documentclass{article}\n\\newtheorem{theorem}{Theorem}\n\\begin{document}\n"
                "\\begin{theorem}\\label{thm:main}For every integer $n$, $n=n$.\\end{theorem}\n"
                "\\begin{proof}The conclusion follows by reflexivity.\\end{proof}\n\n" + context + "\n\n\\end{document}\n")
            source.write_text(text)
            state = init_refine(source)
            work = Path(state["work_dir"])
            state_path = work / "00-run-state.json"
            lock_main_results(state_path, ["thm:main"])
            Path(state["output"]).write_text(text.replace(context, ""))
            baseline = json.loads((work / "00-baseline-inventory.json").read_text())
            citation = next(unit for unit in baseline["units"] if unit["kind"] == "citation")
            prose = next(unit for unit in baseline["units"] if unit["kind"] == "prose" and "old-key" in unit["normalized_text"])
            coverage_path = work / "05-coverage-ledger.json"
            coverage = json.loads(coverage_path.read_text())
            for entry in coverage["entries"]:
                if entry["unit_id"] == citation["id"]:
                    entry["disposition"] = "ledger-only"
            compression_path = work / "04-compression-ledger.json"
            compression = json.loads(compression_path.read_text())
            compression["entries"].append({"unit_id": citation["id"], **self.entry})
            coverage_path.write_text(json.dumps(coverage))
            compression_path.write_text(json.dumps(compression))
            (work / "05.5-deleted-steps.md").write_text(self.archive)
            report = audit_refinement(state_path)
            self.assertTrue(any(prose["id"] in error for error in report["errors"]))
            self.assertFalse(any(citation["id"] in error for error in report["errors"]))
            for entry in coverage["entries"]:
                if entry["unit_id"] == prose["id"]:
                    entry["disposition"] = "ledger-only"
            prose_entry = {**self.entry, "unit_id": prose["id"], "archive_anchor": "omitted-prose",
                "archived_text": prose["normalized_text"], "archived_text_sha256": prose["normalized_sha256"],
                "archived_raw_text": prose["raw_text"], "archived_raw_sha256": prose["raw_sha256"]}
            compression["entries"].append(prose_entry)
            coverage_path.write_text(json.dumps(coverage))
            compression_path.write_text(json.dumps(compression))
            (work / "05.5-deleted-steps.md").write_text(self.archive + "\n# omitted-prose\n\n" + prose["raw_text"])
            report = audit_refinement(state_path)
            self.assertTrue(report["pass"], report["errors"])
            # The exception must not leak to the prose's ordinary raw-byte archive.
            prose_entry.pop("archived_raw_text")
            prose_entry.pop("archived_raw_sha256")
            compression_path.write_text(json.dumps(compression))
            report = audit_refinement(state_path)
            self.assertTrue(any(prose["id"] in error and "raw" in error for error in report["errors"]))
            # Check the second code path: compression validation also handles the
            # synthetic index, while all unrelated late-stage requirements remain.
            current = json.loads(state_path.read_text())
            current["gates"]["compression"]["status"] = "pass"
            state_path.write_text(json.dumps(current))
            report = audit_refinement(state_path)
            self.assertFalse(any(citation["id"] in error for error in report["errors"]), report["errors"])


if __name__ == "__main__":
    unittest.main()
