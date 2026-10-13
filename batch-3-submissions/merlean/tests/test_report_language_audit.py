from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "report_language_audit.py"
SPEC = importlib.util.spec_from_file_location("report_language_audit", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

PDF_TOOLS = (
    shutil.which("pdflatex") is not None and shutil.which("pdftotext") is not None
)
TARGET_PDF_TOOLS = (
    PDF_TOOLS
    and shutil.which("latexpand") is not None
    and shutil.which("detex") is not None
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ReportLanguageAuditTests(unittest.TestCase):
    def audit(
        self,
        target_texts: list[str],
        report_rendered_text: str,
        report_source_text: str | None = None,
        max_collocations: int = -1,
        strict_vocabulary: bool = True,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            targets = []
            for index, target_text in enumerate(target_texts):
                target = root / f"target-{index}.txt"
                target.write_text(target_text)
                targets.append(target)
            report_rendered = root / "report.txt"
            report_source = root / "report.tex"
            report_rendered.write_text(report_rendered_text)
            report_source.write_text(
                report_rendered_text
                if report_source_text is None
                else report_source_text
            )
            return MODULE.audit(
                targets,
                report_rendered,
                report_source,
                max_collocations,
                strict_vocabulary=strict_vocabulary,
            )

    def test_missing_word_is_hard_failure(self) -> None:
        result = self.audit(
            ["The standard conditions are complete."],
            "The unusual conditions are complete.",
        )
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(
            [item["word"] for item in result["missing_words"]], ["unusual"]
        )

    def test_all_em_dash_forms_are_hard_failures(self) -> None:
        result = self.audit(
            ["The result is valid."],
            "The result is valid.",
            "The result---is valid. — \\textemdash \\emdash",
        )
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(len(result["em_dashes"]), 4)

    def test_macro_hidden_rendered_em_dash_is_a_hard_failure(self) -> None:
        result = self.audit(
            ["The result is valid."],
            "The result—is valid.",
            r"\newcommand{\hidden}{an em dash}The result\hidden is valid.",
        )
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(result["em_dashes"][0]["origin"], "rendered")

    def test_rendered_macro_word_cannot_hide(self) -> None:
        result = self.audit(
            ["The result is valid."],
            "The unusual result is valid.",
            r"\newcommand{\hidden}{unusual}\begin{document}The \hidden result is valid.",
        )
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(
            [item["word"] for item in result["missing_words"]], ["unusual"]
        )

    def test_visible_math_text_cannot_hide(self) -> None:
        result = self.audit(
            ["The result is valid."],
            "The unusual result is valid.",
            r"The $\text{unusual}$ result is valid.",
        )
        self.assertFalse(result["hard_checks_pass"])

    def test_possessive_inflection_is_preserved(self) -> None:
        result = self.audit(["The author result."], "The author's result.")
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(
            [item["word"] for item in result["missing_words"]], ["author's"]
        )

    def test_plural_possessive_inflection_is_preserved(self) -> None:
        result = self.audit(["The authors result."], "The authors' result.")
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(
            [item["word"] for item in result["missing_words"]], ["authors'"]
        )

    def test_closing_quote_is_not_a_possessive(self) -> None:
        result = self.audit(["The result is valid."], "The 'result' is valid.")
        self.assertTrue(result["hard_checks_pass"])

    def test_quoted_plural_is_not_a_possessive(self) -> None:
        result = self.audit(["The authors are valid."], "The ‘authors’ are valid.")
        self.assertTrue(result["hard_checks_pass"])

    def test_unicode_word_is_checked(self) -> None:
        result = self.audit(["The result is valid."], "The результат is valid.")
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual(
            [item["word"] for item in result["missing_words"]], ["результат"]
        )

    def test_unattested_collocation_is_reported_without_hard_failure(self) -> None:
        result = self.audit(
            ["The local map is valid. The finite conditions are complete."],
            "The local conditions are complete.",
        )
        self.assertTrue(result["hard_checks_pass"])
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertIn("local conditions", phrases)

    def test_visual_line_break_does_not_break_attested_collocation(self) -> None:
        result = self.audit(
            ["The local\nconditions are complete."],
            "The local conditions are complete.",
        )
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertNotIn("local conditions", phrases)

    def test_pdf_style_line_end_hyphen_is_joined(self) -> None:
        result = self.audit(
            ["The certification is complete."],
            "The certifi-\ncation is complete.",
        )
        self.assertTrue(result["hard_checks_pass"])

    def test_line_wrapped_lexical_compound_keeps_split_interpretation(self) -> None:
        result = self.audit(
            ["The finite-\ndimensional result."],
            "The finite-dimensional result.",
        )
        self.assertTrue(result["hard_checks_pass"])
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertNotIn("finite dimensional", phrases)

    def test_report_line_wrapped_lexical_compound_uses_split_interpretation(
        self,
    ) -> None:
        result = self.audit(
            ["The finite-dimensional result."],
            "The finite-\ndimensional result.",
        )
        self.assertTrue(result["hard_checks_pass"])
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertNotIn("finite dimensional", phrases)

    def test_decomposed_accent_is_normalized(self) -> None:
        result = self.audit(
            ["The Gröbner basis."], "The Gro\N{COMBINING DIAERESIS}bner basis."
        )
        self.assertTrue(result["hard_checks_pass"])

    def test_accent_is_not_discarded(self) -> None:
        result = self.audit(["The résumé."], "The resume.")
        self.assertFalse(result["hard_checks_pass"])
        self.assertEqual([item["word"] for item in result["missing_words"]], ["resume"])

    def test_collocations_do_not_cross_sentence_boundaries(self) -> None:
        result = self.audit(
            ["The action is valid. Previous work is complete."],
            "The action is valid. Previous work is complete.",
        )
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertNotIn("valid previous", phrases)

    def test_target_documents_do_not_form_cross_file_collocations(self) -> None:
        result = self.audit(["Earlier result", "method complete"], "result method")
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertIn("result method", phrases)

    def test_unattested_three_word_phrase_is_reported(self) -> None:
        result = self.audit(
            ["alpha beta. beta gamma."],
            "alpha beta gamma",
        )
        phrases = {item["phrase"] for item in result["unattested_content_phrases"]}
        self.assertIn("alpha beta gamma", phrases)

    def test_truncation_is_explicit(self) -> None:
        result = self.audit(
            ["alpha beta gamma delta epsilon"],
            "alpha gamma epsilon beta delta",
            max_collocations=1,
        )
        self.assertTrue(result["unattested_content_phrases_truncated"])
        self.assertTrue(result["manual_phrase_review_required"])
        self.assertGreater(result["unattested_content_phrases_total"], 1)
        self.assertEqual(len(result["unattested_content_phrases"]), 1)

    def run_cli(self, target: Path, report: Path, *extra: str, env=None):
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--target-rendered",
                str(target),
                "--report-rendered",
                str(report),
                "--report-source",
                str(report),
                "--json",
                *extra,
            ],
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )

    def test_cli_default_and_strict_vocabulary_and_dash_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target, report = root / "target.txt", root / "report.txt"
            target.write_text("The result is valid.")
            report.write_text("The unusual result is valid.")
            default = self.run_cli(target, report)
            self.assertEqual(default.returncode, 0, default.stderr)
            data = json.loads(default.stdout)
            self.assertEqual(data["missing_words"][0]["word"], "unusual")
            self.assertFalse(data["manual_phrase_review_required"])
            self.assertTrue(data["phrase_review_suggested"])
            strict = self.run_cli(target, report, "--strict-vocabulary")
            self.assertEqual(strict.returncode, 1, strict.stderr)
            self.assertTrue(json.loads(strict.stdout)["strict_vocabulary"])
            report.write_text("The result—is valid.")
            dashed = self.run_cli(target, report)
            self.assertEqual(dashed.returncode, 1, dashed.stderr)
            self.assertTrue(json.loads(dashed.stdout)["em_dashes"])

    @staticmethod
    def write_pdf(path):
        # A real, one-page text PDF requires no TeX installation to generate.
        stream = b"BT /F1 12 Tf 30 100 Td (The result is valid.) Tj ET"
        objects = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 150] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            b"<< /Length "
            + str(len(stream)).encode()
            + b" >>\nstream\n"
            + stream
            + b"\nendstream",
        ]
        pdf = bytearray(b"%PDF-1.4\n")
        offsets = [0]
        for number, body in enumerate(objects, 1):
            offsets.append(len(pdf))
            pdf.extend(f"{number} 0 obj\n".encode() + body + b"\nendobj\n")
        xref = len(pdf)
        pdf.extend(b"xref\n0 6\n0000000000 65535 f \n")
        for offset in offsets[1:]:
            pdf.extend(f"{offset:010d} 00000 n \n".encode())
        pdf.extend(
            f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
        )
        path.write_bytes(pdf)

    @unittest.skipUnless(shutil.which("pdftotext"), "requires pdftotext")
    def test_cli_target_pdf_needs_no_tex_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target, report = root / "target.pdf", root / "report.txt"
            self.write_pdf(target)
            report.write_text("The unusual result is valid.")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            (bin_dir / "pdftotext").symlink_to(shutil.which("pdftotext"))
            env = dict(os.environ, PATH=str(bin_dir))
            result = self.run_cli(target, report, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            self.assertGreater(data["target_vocabulary_size"], 0)
            self.assertTrue(data["target_extraction_notes"])
            strict = self.run_cli(target, report, "--strict-vocabulary", env=env)
            self.assertNotEqual(strict.returncode, 0)
            self.assertIn("target-source-root", strict.stderr)
            source = root / "target.tex"
            source.write_text("The result is valid.")
            enhanced = self.run_cli(
                target, report, "--target-source-root", str(source), env=env
            )
            self.assertEqual(enhanced.returncode, 0, enhanced.stderr)
            self.assertIn(
                "latexpand", json.loads(enhanced.stdout)["target_extraction_notes"][0]
            )
            strict_source = self.run_cli(
                target,
                report,
                "--strict-vocabulary",
                "--target-source-root",
                str(source),
                env=env,
            )
            self.assertNotEqual(strict_source.returncode, 0)

    @unittest.skipUnless(shutil.which("pdftotext"), "requires pdftotext")
    def test_default_report_pdf_requires_current_build_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target, source = root / "target.txt", root / "report.tex"
            pdf, manifest = root / "report.pdf", root / "build.json"
            target.write_text("The result is valid.")
            source.write_text("The result is valid.")
            self.write_pdf(pdf)
            with self.assertRaisesRegex(RuntimeError, "manifest is required"):
                MODULE.audit([target], pdf, source, -1)
            record = {
                "report_source_sha256": file_sha256(source),
                "report_rendered_sha256": file_sha256(pdf),
                "compile_exit_code": 0,
                "compile_command": ["test-pdf-generator"],
            }
            manifest.write_text(json.dumps(record))
            self.assertTrue(
                MODULE.audit([target], pdf, source, -1, manifest)["hard_checks_pass"]
            )
            for key, value in [
                ("report_source_sha256", "stale"),
                ("report_rendered_sha256", "stale"),
                ("compile_exit_code", 1),
            ]:
                manifest.write_text(json.dumps(dict(record, **{key: value})))
                with (
                    self.subTest(key=key),
                    self.assertRaisesRegex(RuntimeError, "mismatch"),
                ):
                    MODULE.audit([target], pdf, source, -1, manifest)

    @unittest.skipUnless(PDF_TOOLS, "requires pdflatex and pdftotext")
    def test_real_pdf_macro_word_and_build_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.txt"
            source = root / "report.tex"
            target.write_text("The result is valid.")
            source.write_text(
                "\\documentclass{article}\n"
                "\\newcommand{\\hidden}{unusual}\n"
                "\\pagestyle{empty}\n"
                "\\begin{document}The \\hidden{} result is valid.\\end{document}\n"
            )
            subprocess.run(
                ["pdflatex", "-interaction=batchmode", "-halt-on-error", source.name],
                cwd=root,
                check=True,
                capture_output=True,
            )
            rendered = root / "report.pdf"
            manifest = root / "report-build.json"
            manifest.write_text(
                json.dumps(
                    {
                        "report_source_sha256": file_sha256(source),
                        "report_rendered_sha256": file_sha256(rendered),
                        "compile_exit_code": 0,
                        "compile_command": [
                            "pdflatex",
                            "-interaction=batchmode",
                            "-halt-on-error",
                            source.name,
                        ],
                    }
                )
            )
            result = MODULE.audit(
                [target], rendered, source, -1, manifest, strict_vocabulary=True
            )
            self.assertFalse(result["hard_checks_pass"])
            self.assertEqual(
                [item["word"] for item in result["missing_words"]], ["unusual"]
            )
            self.assertTrue(result["report_build_manifest_validated"])

    @unittest.skipUnless(PDF_TOOLS, "requires pdflatex and pdftotext")
    def test_image_only_pdf_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "blank.tex"
            source.write_text(
                "\\documentclass{article}\n"
                "\\pagestyle{empty}\n"
                "\\begin{document}\\mbox{}\\end{document}\n"
            )
            subprocess.run(
                ["pdflatex", "-interaction=batchmode", "-halt-on-error", source.name],
                cwd=root,
                check=True,
                capture_output=True,
            )
            with self.assertRaisesRegex(RuntimeError, "produced no words"):
                MODULE.rendered_text(root / "blank.pdf")

    @unittest.skipUnless(TARGET_PDF_TOOLS, "requires TeX and PDF text tools")
    def test_target_discretionary_hyphen_does_not_admit_fragment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "target.tex"
            source.write_text(
                "\\documentclass{article}\n"
                "\\begin{document}The certifi\\-cation is complete.\\end{document}\n"
            )
            resolved = MODULE.resolve_target_pdf_text(
                "The certifi-\ncation is complete.", source
            )
            words = {token.word for token in MODULE.tokenize(resolved)}
            self.assertIn("certification", words)
            self.assertNotIn("cation", words)
            target = Path(directory) / "target.txt"
            report = Path(directory) / "report.txt"
            target.write_text(resolved)
            report.write_text("The cation is complete.")
            result = MODULE.audit([target], report, report, -1, strict_vocabulary=True)
            self.assertFalse(result["hard_checks_pass"])
            self.assertEqual(
                [item["word"] for item in result["missing_words"]], ["cation"]
            )

    @unittest.skipUnless(TARGET_PDF_TOOLS, "requires TeX and PDF text tools")
    def test_real_two_column_target_pdf_uses_reading_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "target.tex"
            source.write_text(
                "\\documentclass[twocolumn]{article}\n"
                "\\pagestyle{empty}\n"
                "\\begin{document}\n"
                "The infinite symmorphic result is valid.\\par\n"
                + "The algebraic construction is complete. " * 80
                + "\n\\end{document}\n"
            )
            subprocess.run(
                ["pdflatex", "-interaction=batchmode", "-halt-on-error", source.name],
                cwd=root,
                check=True,
                capture_output=True,
            )
            report = root / "report.txt"
            report.write_text("The infinite symmorphic result is valid.")
            result = MODULE.audit(
                [root / "target.pdf"],
                report,
                report,
                -1,
                target_source_roots=[source],
            )
            self.assertTrue(result["hard_checks_pass"])


if __name__ == "__main__":
    unittest.main()
