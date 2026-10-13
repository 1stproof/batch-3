from __future__ import annotations

import asyncio
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from proofstack.agents.pwc.workspace import (  # noqa: E402
    PWCStashAnswer,
    PWCWorkspaceInit,
    PWCWorkspaceSnapshot,
    pwc_workspace_path,
)
from proofstack.context import RunContext  # noqa: E402


class PWCComponentTests(unittest.TestCase):
    def test_workspace_init_creates_canonical_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            ctx = RunContext.create(run_id="test", root_workdir=temp_dir, flat=True)
            out = asyncio.run(
                PWCWorkspaceInit(ctx)(problem="Prove X.", problem_id="pwc test/1")
            )

            self.assertTrue((out.workspace / "answer.tex").exists())
            self.assertTrue((out.workspace / "research_notes.tex").exists())
            self.assertTrue((out.workspace / "references.bib").exists())
            self.assertTrue((out.workspace / "problem.txt").exists())
    def test_workspace_snapshot_accepts_missing_prior_notes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            ctx = RunContext.create(run_id="test", root_workdir=temp_dir, flat=True)
            workspace = asyncio.run(PWCWorkspaceInit(ctx)(problem="Prove X.", problem_id="p1")).workspace

            PWCWorkspaceSnapshot.Inputs(
                problem_id="p1",
                round=0,
                plan_md=None,
                review_md=None,
                workspace=workspace,
                status=None,
                diff_summary=None,
            )

    def test_stash_answer_embeds_bbl_when_available(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            ctx = RunContext.create(run_id="test", root_workdir=temp_dir, flat=True)
            compile_tex = ctx.root_workdir / "agents" / "compile" / "main.tex"
            compile_tex.parent.mkdir(parents=True)
            compile_tex.write_text("placeholder", encoding="utf-8")
            compile_tex.with_suffix(".bbl").write_text(
                "\\begin{thebibliography}{1}\\bibitem{x} X.\\end{thebibliography}",
                encoding="utf-8",
            )
            bib = ctx.root_workdir / "references.bib"
            bib.write_text("@article{x, title={X}}", encoding="utf-8")
            workspace = asyncio.run(PWCWorkspaceInit(ctx)(problem="P", problem_id="p1")).workspace
            (workspace / "references.bib").write_text(bib.read_text(encoding="utf-8"), encoding="utf-8")

            out = asyncio.run(
                PWCStashAnswer(ctx)(
                    problem_id="p1",
                    tex=(
                        "\\documentclass{article}\\begin{document}"
                        "\\cite{x}\\bibliographystyle{plain}\\bibliography{references}"
                        "\\end{document}"
                    ),
                    compile_tex_path=compile_tex,
                    workspace=workspace,
                )
            )

            final_tex = out.answer_tex.read_text(encoding="utf-8")
            self.assertIn("\\begin{thebibliography}", final_tex)
            self.assertNotIn("\\bibliography{references}", final_tex)
if __name__ == "__main__":
    unittest.main()
