"""Lite review receipts bind artifacts without claiming mathematical verification."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from lite_review_rounds import validate_lite_review_rounds


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class LiteReviewRoundTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.work = Path(self.temp.name).resolve()
        self.route = "route-alpha"
        self.manifest = {
            "schema_version": 1,
            "route_id": self.route,
            "identity_provenance": "self_reported",
            "rounds": [],
        }
        self.previous_output = self.write("ledger-v0.md", "# Ledger\n\nS1 | draft\n")

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, content):
        path = self.work / name
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode("utf-8") if isinstance(content, str) else content
        path.write_bytes(data)
        return {"path": name, "sha256": digest(data)}

    def write_json(self, name, value):
        return self.write(name, json.dumps(value, indent=2, sort_keys=True) + "\n")

    def add_round(
        self,
        *,
        verdict="closed",
        objections=None,
        survived=None,
        resolutions=None,
        responses=None,
        output=None,
        actor="actor-a",
        reviewer=None,
        actor_context="actor-context",
        reviewer_context=None,
        input_reference=None,
    ):
        number = len(self.manifest["rounds"]) + 1
        reviewer = reviewer or f"reviewer-{number}"
        reviewer_context = reviewer_context or f"review-context-{number}"
        input_reference = input_reference or self.previous_output
        objections = objections or []
        survived = survived or []
        resolutions = resolutions or []
        blockers = [
            item["id"] for item in objections if item["severity"] in {"fatal", "gap"}
        ]
        review = {
            "schema_version": 1,
            "route_id": self.route,
            "round": number,
            "identity_provenance": "self_reported",
            "input_ledger_sha256": input_reference["sha256"],
            "reviewer_id": reviewer,
            "reviewer_context_id": reviewer_context,
            "verdict": verdict,
            "first_blocker": blockers[0] if blockers else None,
            "objections": objections,
            "survived": survived,
            "resolutions": resolutions,
        }
        review_reference = self.write_json(f"review-v{number}.json", review)
        if output is None and verdict in {"closed", "triage_required"}:
            output = (self.work / input_reference["path"]).read_bytes()
        output_reference = self.write(
            f"ledger-v{number}.md",
            output if output is not None else f"# Ledger\n\nround {number}\n",
        )
        if responses is None:
            responses = [
                {
                    "objection_id": item["id"],
                    "action": "revised",
                    "reason": "The actor revised the cited row and its dependent uses.",
                }
                for item in objections
            ]
        disposition = {
            "schema_version": 1,
            "route_id": self.route,
            "round": number,
            "identity_provenance": "self_reported",
            "actor_id": actor,
            "actor_context_id": actor_context,
            "input_ledger_sha256": input_reference["sha256"],
            "review_sha256": review_reference["sha256"],
            "output_ledger_sha256": output_reference["sha256"],
            "responses": responses,
        }
        disposition_reference = self.write_json(
            f"disposition-v{number}.json", disposition
        )
        self.manifest["rounds"].append(
            {
                "round": number,
                "actor_id": actor,
                "reviewer_id": reviewer,
                "actor_context_id": actor_context,
                "reviewer_context_id": reviewer_context,
                "input_ledger": input_reference,
                "review": review_reference,
                "disposition": disposition_reference,
                "output_ledger": output_reference,
            }
        )
        self.previous_output = output_reference
        return self.manifest["rounds"][-1]

    @staticmethod
    def gap(identifier="O1"):
        return {
            "id": identifier,
            "step": "S1",
            "severity": "gap",
            "scope": "step",
            "content": "The quantified boundary case is not justified.",
            "resolve": "Prove the boundary case under the frozen hypotheses.",
        }

    @staticmethod
    def conceded():
        return {
            "id": "C1",
            "step": "S2",
            "disposition": "conceded_by_exhaustion",
            "rationale": "No counterexample was found, but the inference remains uncertain.",
        }

    @staticmethod
    def nitpick():
        return {
            "id": "N1",
            "step": "S1",
            "severity": "nitpick",
            "scope": "step",
            "content": "The notation should name the quantified domain explicitly.",
            "resolve": "Name the domain in the displayed ledger claim.",
        }

    def test_valid_two_round_repair_lineage(self):
        self.add_round(verdict="objections", objections=[self.gap()])
        self.add_round(
            verdict="closed",
            resolutions=[{
                "id": "O1",
                "step": "S1",
                "rationale": "The later reviewer confirms the boundary repair.",
            }],
        )
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertEqual(result["rounds"], 2)
        self.assertEqual(result["final_verdict"], "closed")
        self.assertTrue(result["closure_claimed"])
        self.assertFalse(result["freshness_verified"])
        self.assertEqual(result["identity_provenance"], "self_reported")

    def test_false_closure_and_false_route_fatal_are_rejected(self):
        self.add_round(verdict="closed", objections=[self.gap()])
        with self.assertRaisesRegex(ValueError, "closed contradicts"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].clear()
        self.previous_output = self.write("second-start.md", "S1 | draft\n")
        self.add_round(
            verdict="route_fatal",
            objections=[self.gap()],
            responses=[{
                "objection_id": "O1",
                "action": "route_abandoned",
                "reason": "The actor accepts that the route cannot continue.",
            }],
        )
        with self.assertRaisesRegex(ValueError, "fatal representation"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_stale_ledger_bytes_are_rejected(self):
        first = self.add_round(verdict="closed")
        (self.work / first["input_ledger"]["path"]).write_text("changed after receipt\n")
        with self.assertRaisesRegex(ValueError, "missing or stale"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_every_objection_needs_exactly_one_disposition(self):
        self.add_round(verdict="objections", objections=[self.gap()], responses=[])
        with self.assertRaisesRegex(ValueError, "cover every objection"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_consecutive_rounds_must_use_preceding_output(self):
        self.add_round(verdict="objections", objections=[self.gap()])
        unrelated = self.write("unrelated-ledger.md", "S1 | unrelated branch\n")
        self.add_round(verdict="closed", input_reference=unrelated)
        with self.assertRaisesRegex(ValueError, "does not continue"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_paths_cannot_escape_or_follow_symlinks(self):
        round_record = self.add_round(verdict="closed")
        outside = self.work.parent / f"outside-{self.work.name}.md"
        outside.write_text("outside\n")
        try:
            for escaped in ("../outside-lite-ledger.md", str(outside)):
                with self.subTest(path=escaped):
                    round_record["input_ledger"] = {
                        "path": escaped,
                        "sha256": digest(outside.read_bytes()),
                    }
                    with self.assertRaisesRegex(ValueError, "stay below"):
                        validate_lite_review_rounds(self.work, self.manifest)
            link = self.work / "linked-ledger.md"
            link.symlink_to(outside)
            round_record["input_ledger"] = {
                "path": link.name,
                "sha256": digest(outside.read_bytes()),
            }
            with self.assertRaisesRegex(ValueError, "cannot safely read"):
                validate_lite_review_rounds(self.work, self.manifest)
        finally:
            outside.unlink(missing_ok=True)

    def test_resolved_and_conceded_by_exhaustion_are_not_equivalent(self):
        self.add_round(verdict="closed", survived=[self.conceded()])
        with self.assertRaisesRegex(ValueError, "conceded-by-exhaustion"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].clear()
        self.previous_output = self.write("triage-start.md", "S2 | uncertain\n")
        self.add_round(verdict="triage_required", survived=[self.conceded()])
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertTrue(result["triage_required"])
        self.assertFalse(result["closure_claimed"])

    def test_closed_allows_nitpicks_with_null_first_blocker_and_disposition(self):
        self.add_round(
            verdict="closed",
            objections=[self.nitpick()],
            output="S1 | revised notation with explicit domain\n",
        )
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertTrue(result["closure_claimed"])
        review = json.loads((self.work / "review-v1.json").read_text())
        self.assertIsNone(review["first_blocker"])

    def test_closed_nitpick_still_needs_an_actor_disposition(self):
        self.add_round(
            verdict="closed",
            objections=[self.nitpick()],
            responses=[],
        )
        with self.assertRaisesRegex(ValueError, "cover every objection"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_deferred_gap_needs_explicit_later_reviewer_resolution(self):
        self.add_round(
            verdict="objections",
            objections=[self.gap()],
            responses=[{
                "objection_id": "O1",
                "action": "deferred",
                "reason": "The repair needs another proof pass before it can be claimed.",
            }],
        )
        self.add_round(verdict="closed")
        with self.assertRaisesRegex(ValueError, "unresolved fatal/gap"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].pop()
        self.previous_output = self.manifest["rounds"][-1]["output_ledger"]
        self.add_round(
            verdict="closed",
            resolutions=[{
                "id": "O1",
                "step": "S1",
                "rationale": "The revised ledger now proves the boundary case explicitly.",
            }],
        )
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertEqual(result["outstanding_findings"], [])

    def test_conceded_finding_carries_until_stable_id_and_step_are_resolved(self):
        self.add_round(verdict="triage_required", survived=[self.conceded()])
        self.add_round(verdict="closed")
        with self.assertRaisesRegex(ValueError, "conceded-by-exhaustion"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].pop()
        self.previous_output = self.manifest["rounds"][-1]["output_ledger"]
        self.add_round(
            verdict="closed",
            resolutions=[{
                "id": "C1",
                "step": "different-step",
                "rationale": "This intentionally names the wrong step.",
            }],
        )
        with self.assertRaisesRegex(ValueError, "changes the step"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].pop()
        self.previous_output = self.manifest["rounds"][-1]["output_ledger"]
        self.add_round(
            verdict="closed",
            resolutions=[{
                "id": "C1",
                "step": "S2",
                "rationale": "The later reviewer now resolves the previously uncertain inference.",
            }],
        )
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertEqual(result["outstanding_findings"], [])

    def test_route_abandonment_is_terminal_for_one_manifest(self):
        fatal = {
            "id": "F1",
            "step": "representation",
            "severity": "fatal",
            "scope": "representation",
            "content": "The representation loses information required by the target.",
            "resolve": "Abandon this route and open a separately identified route.",
        }
        self.add_round(
            verdict="route_fatal",
            objections=[fatal],
            responses=[{
                "objection_id": "F1",
                "action": "route_abandoned",
                "reason": "This route is terminated while its evidence remains preserved.",
            }],
        )
        self.add_round(verdict="closed")
        with self.assertRaisesRegex(ValueError, "terminal for this route manifest"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_declared_identity_separation_does_not_claim_verified_freshness(self):
        self.add_round(verdict="closed", actor="same", reviewer="same")
        with self.assertRaisesRegex(ValueError, "identities must differ"):
            validate_lite_review_rounds(self.work, self.manifest)

        self.manifest["rounds"].clear()
        self.previous_output = self.write("identity-start.md", "S1 | draft\n")
        self.add_round(verdict="objections", objections=[self.gap()])
        self.add_round(
            verdict="closed",
            reviewer_context="review-context-1",
            resolutions=[{
                "id": "O1",
                "step": "S1",
                "rationale": "The later review explicitly accepts the repaired boundary case.",
            }],
        )
        result = validate_lite_review_rounds(self.work, self.manifest)
        self.assertFalse(result["declared_reviewer_contexts_unique"])
        self.assertFalse(result["freshness_verified"])

    def test_revised_disposition_must_change_ledger_bytes(self):
        unchanged = (self.work / self.previous_output["path"]).read_bytes()
        self.add_round(
            verdict="objections",
            objections=[self.gap()],
            output=unchanged,
        )
        with self.assertRaisesRegex(ValueError, "revised disposition must change"):
            validate_lite_review_rounds(self.work, self.manifest)

    def test_recursive_json_and_symlink_loop_become_clean_validation_errors(self):
        recursive = b'{"schema_version":' + b"[" * 2000 + b"0" + b"]" * 2000 + b"}"
        (self.work / "recursive.json").write_bytes(recursive)
        # JSON decoders differ in their nesting limit (including Python 3.14).
        # Deep input must be rejected cleanly, whether by parsing or schema validation.
        with self.assertRaises(ValueError):
            validate_lite_review_rounds(self.work, "recursive.json")
        with patch("lite_review_rounds.json.loads", side_effect=RecursionError("nested input")):
            with self.assertRaisesRegex(ValueError, "not valid UTF-8 JSON"):
                validate_lite_review_rounds(self.work, "recursive.json")

        loop = self.work / "loop"
        loop.symlink_to(loop)
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "src/lite_review_rounds.py"),
                str(loop),
                "manifest.json",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot resolve evidence_root safely", result.stderr)

    def test_cli_reports_advisory_summary(self):
        self.add_round(verdict="closed")
        self.write_json("manifest.json", self.manifest)
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "src/lite_review_rounds.py"),
                str(self.work),
                "manifest.json",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertTrue(summary["advisory"])
        self.assertFalse(summary["freshness_verified"])


if __name__ == "__main__":
    unittest.main()
