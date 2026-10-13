from __future__ import annotations

import json
from pathlib import Path
import sys
import shutil
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.raw import freeze_raw, start_from_raw, raw_errors, raw_inventory, raw_preservation_errors, candidate_raw_inventory
from paper_writing_codex.versioning import sha256_file
from paper_writing_codex.workflow import init_refine, mark_gate, resume_point


def evidence_fixture(state_path: Path, source: Path, assets=None) -> Path:
    """Synthetic fidelity evidence for runtime tests; no mathematical certification."""
    work = state_path.parent.resolve()
    status = work / "test-proof-status.md"
    status.write_text("Synthetic test: the result is conjectural; no Lean proof is available.")
    hashes = raw_inventory(source, assets)
    audit = work / "test-raw-audit.json"
    audit.write_text(json.dumps({"reviewer_id": "independent-test-reviewer", "verdict": "PASS",
        "raw_source_sha256": hashes["source_sha256"],
        "raw_source_tree_sha256": hashes["source_tree_sha256"],
        "unresolved_fidelity_issues": [], "research_gaps": ["conjectural test result"],
        "findings": "The synthetic source faithfully retains its stated conjectural status."}))
    ref = {"path": str(status), "sha256": sha256_file(status)}
    evidence = work / "test-raw-evidence.json"
    evidence.write_text(json.dumps({"schema_version": 1, **hashes,
        "writer_ids": ["test-writer"], "selected_results": ["test-conjecture"], "critical_path_unavailable_reason": "No Lean graph in this Lite fixture",
        "source_records": [{**ref, "kind": "natural-language", "findings": "Conjectural status was retained."}],
        "evidence_assessment": ref, "reconstruction_map": ref,
        "independent_audit": {"path": str(audit), "sha256": sha256_file(audit)}}))
    return evidence


def seed_fixture(state_path: Path) -> None:
    state = json.loads(state_path.read_text())
    source = Path(state["output"]).resolve().with_name("paper-raw.tex")
    source.write_bytes(Path(state["output"]).read_bytes())
    state["gates"]["critical-path"]["status"] = "pass"
    state_path.write_text(json.dumps(state))
    freeze_raw(state_path, source, "pre-editorial", evidence_fixture(state_path, source))
    start_from_raw(state_path)


class RawCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        baseline = self.root / "paper-v2.tex"
        baseline.write_text("\\documentclass{article}\n\\begin{document}Approved v2.\\end{document}\n")
        self.state = init_refine(baseline)
        self.state_path = Path(self.state["work_dir"]) / "00-run-state.json"
        self.state["gates"]["critical-path"]["status"] = "pass"
        self.state_path.write_text(json.dumps(self.state))
        self.source = self.root / "paper-raw.tex"
        self.source.write_text("\\documentclass{article}\n\\begin{document}A conjecture, not a proved result.\\end{document}\n")

    def freeze(self, origin="pre-editorial"):
        return freeze_raw(self.state_path, self.source, origin, evidence_fixture(self.state_path, self.source))

    def read(self):
        return json.loads(self.state_path.read_text())

    def test_lite_without_lean_freezes_and_seeds_v3_preserving_v2(self):
        before = Path(self.state["source"]).read_bytes()
        self.freeze()
        start_from_raw(self.state_path)
        state = self.read()
        self.assertEqual(Path(state["output"]).name, "paper-v3.tex")
        self.assertEqual(Path(state["source"]).read_bytes(), before)
        self.assertEqual(Path(state["output"]).read_bytes(), self.source.read_bytes())
        self.assertEqual(raw_errors(state, required=True, lineage=True), [])
        with self.assertRaises(FileExistsError):
            start_from_raw(self.state_path)
        with self.assertRaises(FileExistsError):
            freeze_raw(self.state_path, self.source, "pre-editorial", self.state_path.parent / "test-raw-evidence.json")

    def test_includes_bibliography_assets_and_editable_support(self):
        (self.root / "parts").mkdir()
        (self.root / "parts" / "proof.tex").write_text("Proof detail.\\input{parts/detail}\n")
        (self.root / "parts" / "detail.tex").write_text("Essential conditional bridge.")
        (self.root / "refs.bib").write_text("@article{test,title={Test}}")
        (self.root / "fig.png").write_bytes(b"synthetic image bytes")
        self.source.write_text("\\documentclass{article}\n\\begin{document}\\input{parts/proof}"
                               "\\includegraphics{fig.png}\\bibliography{refs}\\end{document}\n")
        self.freeze()
        start_from_raw(self.state_path)
        output = Path(self.state["output"])
        self.assertIn("paper-v3-support/parts/proof.tex", output.read_text())
        self.assertNotIn(str(self.root), output.read_text())
        self.assertTrue((self.root / "paper-v3-support/fig.png").is_file())
        for entry in json.loads(Path(self.read()["raw_checkpoint"]["manifest"]).read_text())["files"]:
            if entry["kind"] == "manuscript":
                self.assertEqual(sha256_file(Path(entry["source"])), sha256_file(Path(entry["snapshot"])))
        (self.root / "paper-v3-support/parts/detail.tex").write_text("Editorial rewrite")
        self.assertEqual(raw_errors(self.read(), required=True, lineage=True), [])
        (self.root / "refs.bib").write_text("tampered bibliography")
        self.assertTrue(raw_errors(self.read()))

    def test_tampered_raw_snapshot_manifest_evidence_and_source_fail(self):
        self.freeze()
        state = self.read()
        manifest_path = Path(state["raw_checkpoint"]["manifest"])
        manifest = json.loads(manifest_path.read_text())
        for value in [manifest_path, *(Path(item["snapshot"]) for item in manifest["files"]), self.source]:
            with self.subTest(path=value):
                data = value.read_bytes()
                value.write_bytes(data + b"tampered")
                self.assertTrue(raw_errors(state))
                value.write_bytes(data)
        self.assertEqual(raw_errors(state), [])

    @unittest.skipUnless(shutil.which("pdflatex") or shutil.which("latexmk"), "TeX engine unavailable")
    def test_nested_root_relative_inputs_and_local_class_compile_after_seeding(self):
        from paper_writing_codex.cli import _compile_tex
        from paper_writing_codex.tex_inventory import inventory_tex
        (self.root / "parts").mkdir()
        (self.root / "parts" / "a.tex").write_text("A full proof follows.\\input{parts/b}\n")
        (self.root / "parts" / "b.tex").write_text("The needed implication holds under the stated condition.")
        (self.root / "localclass.cls").write_text("\\NeedsTeXFormat{LaTeX2e}\\ProvidesClass{localclass}\\LoadClass{article}\n")
        (self.root / "localstyle.sty").write_text("\\ProvidesPackage{localstyle}\\newcommand{\\testword}{Conditional}\n")
        self.source.write_text("\\documentclass{localclass}\\usepackage{localstyle}\n"
            "\\begin{document}\\testword{} result.\\input{parts/a}\\end{document}\n")
        self.freeze()
        start_from_raw(self.state_path)
        output = Path(self.state["output"])
        self.assertNotIn(str(self.root), output.read_text())
        self.assertFalse(any(item.get("missing") for item in inventory_tex(output)["source_files"]))
        report = _compile_tex(output, 60)
        self.assertTrue(report["pass"], report)

    def test_reconstruction_author_cannot_self_audit(self):
        evidence = evidence_fixture(self.state_path, self.source)
        record = json.loads(evidence.read_text())
        record["writer_ids"] = ["independent-test-reviewer"]
        evidence.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "raw audit"):
            freeze_raw(self.state_path, self.source, "pre-editorial", evidence)

    def test_audit_requires_substantive_actual_string_findings(self):
        evidence = evidence_fixture(self.state_path, self.source)
        original = json.loads(evidence.read_text())
        audit_path = Path(original["independent_audit"]["path"])
        report = json.loads(audit_path.read_text())
        for findings in (None, "", "PASS", {}, ["adequate looking content"]):
            with self.subTest(findings=findings):
                audit_path.write_text(json.dumps({**report, "findings": findings}))
                record = {**original, "independent_audit": {"path": str(audit_path), "sha256": sha256_file(audit_path)}}
                evidence.write_text(json.dumps(record))
                with self.assertRaisesRegex(ValueError, "raw audit"):
                    freeze_raw(self.state_path, self.source, "pre-editorial", evidence)

    def test_commented_missing_inputs_are_preserved_without_rewriting(self):
        comment = "% \\input{old-file} \\documentclass{missing-local}\n"
        self.source.write_text(comment + self.source.read_text())
        self.freeze()
        start_from_raw(self.state_path)
        self.assertTrue(Path(self.state["output"]).read_text().startswith(comment))

    def test_structured_substantive_audit_findings_remain_compatible(self):
        evidence = evidence_fixture(self.state_path, self.source)
        record = json.loads(evidence.read_text())
        path = Path(record["independent_audit"]["path"])
        audit = json.loads(path.read_text())
        audit["findings"] = [{"location": "Conjecture statement", "assessment": "The conjectural status is accurately preserved in the raw text."}]
        path.write_text(json.dumps(audit))
        record["independent_audit"]["sha256"] = sha256_file(path)
        evidence.write_text(json.dumps(record))
        freeze_raw(self.state_path, self.source, "pre-editorial", evidence)
        self.assertEqual(raw_errors(self.read()), [])

    def test_new_local_package_shadows_system_dependency_and_invalidates_raw(self):
        self.freeze()
        (self.root / "article.cls").write_text("Locally added class changes dependency resolution")
        self.assertTrue(raw_errors(self.read()))
        (self.root / "article.cls").unlink()
        snapshot = Path(json.loads(Path(self.read()["raw_checkpoint"]["manifest"]).read_text())["root"])
        (snapshot.parent / "article.cls").write_text("Snapshot shadow class")
        self.assertTrue(raw_errors(self.read()))

    def test_explicit_asset_remains_part_of_candidate_hash(self):
        asset = self.root / "supplement.dat"
        asset.write_bytes(b"Data used by a custom external figure command")
        evidence = evidence_fixture(self.state_path, self.source, [asset])
        freeze_raw(self.state_path, self.source, "pre-editorial", evidence, [asset])
        start_from_raw(self.state_path)
        state = self.read()
        before = candidate_raw_inventory(state)["source_tree_sha256"]
        audit = {"verdict": "PASS", "reviewer_id": "independent-final", "writer_ids": ["test-writer"],
            "unresolved_fidelity_issues": [], "raw_manifest_sha256": state["raw_checkpoint"]["manifest_sha256"],
            "baseline_sha256": state["source_sha256"], "candidate_source_tree_sha256": before,
            **{key: "Synthetic findings about the asset and source." for key in
               ("hypotheses", "proof_bridges", "research_status", "omissions_and_relocations")}}
        (self.state_path.parent / "08-raw-preservation-audit.json").write_text(json.dumps(audit))
        self.assertEqual(raw_preservation_errors(state, required=True), [])
        (self.root / "paper-v3-support/supplement.dat").write_bytes(b"Changed external data")
        self.assertNotEqual(before, candidate_raw_inventory(state)["source_tree_sha256"])
        self.assertTrue(any("stale" in e for e in raw_preservation_errors(state, required=True)))

    def test_symlink_hardlink_missing_dynamic_and_escape_rejected(self):
        for tex in (r"\input{missing}", r"\input{../outside}", r"\input{\dynamic}", r"\input bare"):
            self.source.write_text(tex)
            with self.assertRaises((ValueError, FileNotFoundError)):
                raw_inventory(self.source)
        self.source.unlink()
        self.source.symlink_to(self.state["source"])
        with self.assertRaises(ValueError):
            raw_inventory(self.source)

    def test_baseline_cannot_be_relabelled_raw(self):
        with self.assertRaisesRegex(ValueError, "distinct file"):
            freeze_raw(self.state_path, Path(self.state["source"]), "pre-editorial", self.state_path)

    def test_outer_pass_does_not_override_typed_audit_failure(self):
        evidence = evidence_fixture(self.state_path, self.source)
        record = json.loads(evidence.read_text())
        audit = Path(record["independent_audit"]["path"])
        audit.write_text(json.dumps({"verdict": "FAIL"}))
        record["independent_audit"].update({"sha256": sha256_file(audit), "verdict": "PASS", "auditor": "wrapper"})
        evidence.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "raw audit"):
            freeze_raw(self.state_path, self.source, "pre-editorial", evidence)

    def test_late_gate_and_legacy_release_need_explicit_migration(self):
        state = self.read()
        for gate in ("preflight", "critical-path", "framework", "main-results"):
            state["gates"][gate]["status"] = "pass"
        state.pop("raw_policy")
        self.state_path.write_text(json.dumps(state))
        self.assertTrue(resume_point(self.state_path)["raw_migration_required"])
        with self.assertRaisesRegex(ValueError, "uncertified"):
            mark_gate(self.state_path, "lemmas", "pass", ["bare assertion"])
        self.assertTrue(raw_errors(state, required=True, lineage=True))

    def test_retrospective_origin_cannot_claim_historical_lineage(self):
        state = self.read()
        state["gates"]["draft"]["status"] = "pass"
        self.state_path.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, "pre-editorial"):
            self.freeze()
        self.freeze("retrospective-reconstruction")
        with self.assertRaisesRegex(ValueError, "reopen"):
            start_from_raw(self.state_path)

    def test_candidate_edits_are_not_overwritten(self):
        self.freeze()
        output = Path(self.state["output"])
        output.write_text("User edits")
        with self.assertRaisesRegex(ValueError, "contents changed"):
            start_from_raw(self.state_path)
        self.assertEqual(output.read_text(), "User edits")

    def test_final_raw_fidelity_audit_is_bound_to_candidate_and_baseline(self):
        from paper_writing_codex.tex_inventory import inventory_tex
        self.freeze()
        start_from_raw(self.state_path)
        state = self.read()
        self.assertTrue(raw_preservation_errors(state, required=True))
        path = self.state_path.parent / "08-raw-preservation-audit.json"
        record = {"verdict": "PASS", "reviewer_id": "second-test-reader", "writer_ids": ["test-writer"], "unresolved_fidelity_issues": [],
            "raw_manifest_sha256": state["raw_checkpoint"]["manifest_sha256"],
            "baseline_sha256": state["source_sha256"],
            "candidate_source_tree_sha256": candidate_raw_inventory(state)["source_tree_sha256"],
            **{key: "Synthetic concrete comparison" for key in ("hypotheses", "proof_bridges", "research_status", "omissions_and_relocations")}}
        path.write_text(json.dumps(record))
        self.assertEqual(raw_preservation_errors(state, required=True), [])
        # A reporter cannot omit a known writer from its own declared writer list.
        for reviewer, sidecar in ((" TEST-WRITER ", None), ("editor-two", {"writer_ids": ["editor-two"]})):
            if sidecar:
                (self.state_path.parent / "07-reader-audit.json").write_text(json.dumps(sidecar))
            path.write_text(json.dumps({**record, "writer_ids": ["other-writer"], "reviewer_id": reviewer}))
            self.assertTrue(raw_preservation_errors(state, required=True))
        path.write_text(json.dumps(record))
        Path(state["output"]).write_text("Proof silently removed")
        self.assertTrue(raw_preservation_errors(state, required=True))


class ComposeResultScopeTests(unittest.TestCase):
    def test_nonempty_results_have_no_numeric_quota_or_mandatory_graph(self):
        from paper_writing_codex.cli import _compose_artifact_errors
        from paper_writing_codex.tex_inventory import inventory_tex
        from paper_writing_codex.workflow import init_compose
        for count, legacy in ((1, False), (5, False), (2, True)):
            with self.subTest(count=count, legacy=legacy), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                state = init_compose(root / "paper-v1.tex")
                policy_path = Path(state["work_dir"]) / "literature-policy.json"
                policy = json.loads(policy_path.read_text())
                policy["assess_novelty"] = True  # This fixture explicitly exercises assessed ADJACENT results.
                policy_path.write_text(json.dumps(policy))
                output = Path(state["output"])
                output.write_text("\\documentclass{article}\\newtheorem{theorem}{Theorem}\\begin{document}\n" +
                    "\n".join("\\begin{theorem}\\label{t:" + str(i) + "}Under the stated condition, the result follows.\\end{theorem}" for i in range(count)) +
                    "\\end{document}")
                results = [{("graph_node_id" if legacy else "result_id"): str(i), "candidate_label": u["label"],
                    "normalized_sha256": u["normalized_sha256"], "hypothesis_surface": "The stated condition",
                    "novelty_status": "ADJACENT", "novelty_evidence": "Synthetic scope record"}
                    for i, u in enumerate(u for u in inventory_tex(output)["units"] if u["kind"] == "statement")]
                records = Path(state["work_dir"]) / "03-main-results.json"
                records.write_text(json.dumps({"main_results": results}))
                issues = lambda: [e for e in _compose_artifact_errors(state) if "compose main" in e or "compose mode" in e]
                self.assertEqual(issues(), [])
                records.write_text(json.dumps({"main_results": []}))
                self.assertTrue(any("nonempty" in e for e in issues()))
                records.write_text(json.dumps({"main_results": [results[0], results[0]]}))
                self.assertTrue(any("duplicate" in e for e in issues()))


if __name__ == "__main__":
    unittest.main()
