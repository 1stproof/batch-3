"""Observable mode dispatch and generated-bundle preservation, without launching models."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.build_bundles import AGENTS, PROVIDERS, build_bundle, bundle_entries, verify_generated, write_archive, write_catalogs

ROOT = Path(__file__).resolve().parents[1]


class AgentModesTests(unittest.TestCase):
    def select(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts/merlean-agent"), *args],
                              capture_output=True, text=True, check=False)

    def test_default_lite_explicit_heavy_and_paper(self):
        for flags, agent, grade in [
            ((), "merlean-lite", "SILVER"), (("-lite",), "merlean-lite", "SILVER"),
            (("-heavy",), "merlean-heavy", "GOLD"),
            (("--task", "formalize"), "merlean-heavy", "GOLD"),
            (("--task", "prove"), "merlean-heavy", "GOLD"),
            (("--task", "translate-only"), "merlean-heavy", None),
            (("--paper-writing",), "paper-writing", None),
            (("--resume-mode", "heavy"), "merlean-heavy", "GOLD"),
        ]:
            with self.subTest(flags=flags):
                run = self.select(*flags)
                self.assertEqual(run.returncode, 0, run.stderr)
                data = json.loads(run.stdout)
                self.assertEqual((data["agent"], data["grade_target"]), (agent, grade))
                self.assertFalse(data["launches_model"])

    def test_campaign_is_explicit_and_preserves_problem_mode_and_model_roles(self):
        ordinary = json.loads(self.select().stdout)
        self.assertFalse(ordinary["campaign_enabled"])
        self.assertIsNone(ordinary["campaign_entrypoint"])
        for flags, grade in [((), "SILVER"), (("-heavy",), "GOLD")]:
            selected = json.loads(self.select("--campaign", *flags).stdout)
            self.assertTrue(selected["campaign_enabled"])
            self.assertEqual(selected["grade_target"], grade)
            self.assertFalse(selected["launches_model"])
            self.assertEqual(selected["model_defaults"]["execution_subagent"], "gpt-6.1-sol")
            self.assertEqual(selected["model_defaults"]["independent_reviewer"], "gpt-6-astra")
            self.assertTrue(Path(selected["campaign_entrypoint"]).is_file())
        self.assertNotIn("model_defaults", json.loads(self.select("--provider", "claude").stdout))

    def test_convergence_default_is_independent_of_mode_provider_and_exam(self):
        for provider in ('claude', 'codex'):
            for mode in ('--lite', '--heavy', '--paper-writing', '--referee'):
                selected = json.loads(self.select('--provider', provider, mode).stdout)
                self.assertTrue(selected['convergence']['enabled'])
                self.assertFalse(selected['convergence']['exam_required'])
                self.assertFalse(selected['convergence']['changes_research_acceptance'])
                self.assertFalse(selected['launches_model'])
                self.assertNotIn('exam', selected)

    def test_exam_selector_preserves_grades_and_does_not_claim_a_launch(self):
        standard = json.loads(self.select().stdout)
        self.assertEqual(standard['profile'], 'standard')
        self.assertNotIn('exam', standard)
        for flags, grade in [((), 'SILVER'), (('-heavy',), 'GOLD'),
                             (('--paper-writing',), None)]:
            selected = json.loads(self.select('--exam', *flags).stdout)
            self.assertEqual(selected['grade_target'], grade)
            self.assertFalse(selected['launches_model'])
            self.assertEqual(selected['exam']['clock_scope'], 'whole_exam_all_problems')
            self.assertEqual(selected['exam']['paper_transition_seconds'], 22.75 * 3600)
            self.assertEqual(selected['exam']['wall_clock_seconds'], 24 * 3600)
            self.assertEqual(selected['exam']['max_pages_per_solution'], 16)
            self.assertFalse(selected['exam']['changes_research_acceptance'])
        self.assertIsNone(json.loads(self.select('--exam', '--provider', 'claude').stdout)['exam']['runtime_entrypoint'])
        for flags in [('--exam', '--referee'), ('--exam', '--task', 'translate-only')]:
            self.assertNotEqual(self.select(*flags).returncode, 0)

    def test_referee_selects_internal_lite_without_awarding_a_grade(self):
        for flags in [("--referee",), ("--task", "referee"),
                      ("--resume-mode", "referee"),
                      ("--referee", "--task", "referee", "--resume-mode", "referee")]:
            with self.subTest(flags=flags):
                run = self.select(*flags)
                self.assertEqual(run.returncode, 0, run.stderr)
                data = json.loads(run.stdout)
                self.assertEqual(data["agent"], "referee")
                self.assertEqual(data["workflow"], "referee")
                self.assertIsNone(data["grade_target"])
                self.assertEqual(data["verification_agent"], "merlean-lite")
                self.assertEqual(data["verification_mode"], "lite")
                self.assertEqual(data["verification_grade_ceiling"], "SILVER")
                self.assertEqual(Path(data["verification_source_instructions"]),
                                 ROOT / "workflows/merlean-lite.md")
                self.assertFalse(data["launches_model"])

    def test_referee_rejects_conflicting_research_and_resume_modes(self):
        for flags in [("--referee", "-lite"), ("--referee", "-heavy"),
                      ("--referee", "--task", "prove"),
                      ("--referee", "--task", "research"),
                      ("--referee", "--task", "paper"),
                      ("--task", "referee", "--resume-mode", "heavy"),
                      ("--task", "referee", "--resume-mode", "lite"),
                      ("--task", "formalize", "--resume-mode", "referee")]:
            with self.subTest(flags=flags):
                self.assertNotEqual(self.select(*flags).returncode, 0)

    def test_referee_installed_verification_is_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            for provider in PROVIDERS:
                bundle = build_bundle(provider, "referee", Path(temp))
                run = subprocess.run([sys.executable, str(bundle / "scripts/merlean-agent"),
                                      "--referee"], check=True, capture_output=True, text=True)
                data = json.loads(run.stdout)
                self.assertEqual(data["provider"], provider)
                self.assertEqual(Path(data["entrypoint"]), bundle / "skills/referee/SKILL.md")
                self.assertEqual(Path(data["verification_source_instructions"]),
                                 bundle / "workflows/merlean-lite.md")
                self.assertTrue(Path(data["verification_source_instructions"]).is_file())
                self.assertFalse((bundle / "skills/merlean-lite/SKILL.md").exists())
                self.assertEqual((bundle / "scripts/report_language_audit.py").read_bytes(),
                                 (ROOT / "scripts/report_language_audit.py").read_bytes())

    def test_conflicting_mode_and_task_are_rejected(self):
        for flags in [("-lite", "-heavy"), ("-lite", "--task", "formalize"),
                      ("-lite", "--resume-mode", "heavy"), ("-heavy", "--task", "paper")]:
            self.assertNotEqual(self.select(*flags).returncode, 0)

    def test_eight_bundles_one_public_agent_and_identical_runtime(self):
        with tempfile.TemporaryDirectory() as temp:
            bundles = [build_bundle(p, a, Path(temp)) for p in PROVIDERS for a in AGENTS]
            self.assertEqual(len(bundles), 8)
            for bundle in bundles:
                self.assertEqual(len(list(bundle.glob("skills/*/SKILL.md"))), 1)
                for relative in ("src/research_grade.py", "src/plan_store/grade_policy.py",
                                 "src/plan_store/lean_sync.py", "workflows/common.md"):
                    self.assertEqual((bundle / relative).read_bytes(), (ROOT / relative).read_bytes())
                verify_generated(bundle)

    def test_rebuild_refuses_user_edits_and_unknown_files(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            bundle = build_bundle("codex", "merlean-lite", out)
            build_bundle("codex", "merlean-lite", out)  # unchanged regeneration is safe
            user_file = bundle / "personal-notes.md"
            user_file.write_text("preserve this")
            with self.assertRaises(ValueError):
                build_bundle("codex", "merlean-lite", out)
            self.assertEqual(user_file.read_text(), "preserve this")
            user_file.unlink()  # temporary test-owned artifact only
            source = bundle / "workflows/common.md"
            source.write_text("local edit")
            with self.assertRaises(ValueError):
                build_bundle("codex", "merlean-lite", out)
            self.assertEqual(source.read_text(), "local edit")

    def test_unknown_provider_agent_and_symlink_output_refused(self):
        with self.assertRaises(ValueError):
            bundle_entries("unknown", "merlean-lite")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            target = base / "preserve"
            target.mkdir()
            (base / "merlean-lite-codex").symlink_to(target, target_is_directory=True)
            with self.assertRaises(ValueError):
                build_bundle("codex", "merlean-lite", base)
            self.assertTrue(target.is_dir())

    def test_installed_provider_is_inferred_and_mismatch_not_mislabeled(self):
        with tempfile.TemporaryDirectory() as temp:
            bundle = build_bundle("claude", "merlean-lite", Path(temp))
            for flags, expected_provider, has_entry in [
                ((), "claude", True), (("--provider", "codex"), "codex", False),
            ]:
                run = subprocess.run([sys.executable, str(bundle / "scripts/merlean-agent"), *flags],
                                     check=True, capture_output=True, text=True)
                data = json.loads(run.stdout)
                self.assertEqual(data["provider"], expected_provider)
                self.assertEqual(data["entrypoint"] is not None, has_entry)

    def test_archive_never_overwrites_unrelated_files_or_links(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            package = build_bundle("codex", "merlean-lite", out / "packages")
            unrelated = out / "unrelated.txt"
            unrelated.write_text("USER CONTENT")
            archive = out / "output.zip"
            archive.symlink_to(unrelated)
            with self.assertRaises(ValueError):
                write_archive(package, archive)
            self.assertEqual(unrelated.read_text(), "USER CONTENT")
            archive.unlink()  # own temporary test link
            archive.write_text("USER ARCHIVE")
            with self.assertRaises(ValueError):
                write_archive(package, archive)
            self.assertEqual(archive.read_text(), "USER ARCHIVE")
            safe = out / "safe.zip"
            write_archive(package, safe)
            before = safe.read_bytes()
            write_archive(package, safe)
            self.assertEqual(safe.read_bytes(), before)

    def test_receipt_links_empty_user_directories_and_permissions_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            bundle = build_bundle("codex", "merlean-lite", out)
            receipt = bundle / ".merlean-generated.json"
            external = out / "external-receipt.json"
            receipt.rename(external)
            receipt.symlink_to(external)
            with self.assertRaises(ValueError):
                verify_generated(bundle)
            receipt.unlink()  # test-owned link only
            external.rename(receipt)
            empty = bundle / "new-project"
            empty.mkdir()
            with self.assertRaises(ValueError):
                build_bundle("codex", "merlean-lite", out)
            empty.rmdir()  # test-owned empty directory
            (bundle / "src").chmod(0o700)
            with self.assertRaises(ValueError):
                build_bundle("codex", "merlean-lite", out)
            self.assertEqual((bundle / "src").stat().st_mode & 0o777, 0o700)

    def test_optional_catalogs_resolve_eight_local_packages_without_overwriting(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packages = root / "plugins"
            for provider in PROVIDERS:
                for agent in AGENTS:
                    build_bundle(provider, agent, packages)
            outputs = write_catalogs(packages)
            for path, provider in zip(outputs, ("codex", "claude")):
                catalog = json.loads(path.read_text())
                self.assertEqual(len(catalog["plugins"]), 4)
                self.assertEqual({entry["name"] for entry in catalog["plugins"]},
                                 {f"{agent}-{provider}" for agent in AGENTS})
                for entry in catalog["plugins"]:
                    relative = entry["source"]["path"] if provider == "codex" else entry["source"]
                    manifest = json.loads((root / relative / f".{provider}-plugin/plugin.json").read_text())
                    self.assertEqual(manifest["name"], entry["name"])
            write_catalogs(packages)
            outputs[0].write_text("USER CATALOG")
            with self.assertRaises(ValueError):
                write_catalogs(packages)
            self.assertEqual(outputs[0].read_text(), "USER CATALOG")


if __name__ == "__main__":
    unittest.main()
