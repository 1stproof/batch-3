"""Current evidence observations for optional campaign milestones.

Silver is a recorded independent review, never a machine-certified grade. A
manifest may supply ``silver_review: {path, sha256}``. That JSON report binds
``final_answer``, ``ledger``, ``assumption_census`` and ``target_contract`` hashed
files; names its reviewer and the manifest's complete implementers census; and
pins ``reviewer_provenance`` (reviewer, role=lite_grade_review, task_id, provider,
actual model, final_answer_sha256, ledger_sha256; Codex also model_family=astra). Its
``checks`` maps comprehensive_composition, theorem_face_closure,
intended_model, no_open_findings, and triage_complete to {pass: true, rationale}.
The JSON ledger has nonempty ``rows`` with unique ids, closed=true, and an
explicit boolean ``triaged``. Every triaged row has status=lean-certified and
hashed certificate, axiom_report, and premise_manifest files. The review lists
exactly those ids in ``triaged_rows``. These receipts record substantive review
and L3 coverage; they do not authenticate identities or replay Lean certificates.
All relative references resolve beside their containing JSON file.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from research_grade import audit_manifest, verify_kernel_runtime
from paper_writing_codex.cli import audit_paper


SILVER_CHECKS = {
    "comprehensive_composition", "theorem_face_closure", "intended_model",
    "no_open_findings", "triage_complete",
}


def _load(path):
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("evidence JSON must be an object")
    return value


def _ref(ref, base):
    if not isinstance(ref, dict) or not isinstance(ref.get("path"), str) or not ref["path"]:
        raise ValueError("evidence requires a path and SHA-256")
    path = (Path(base) / ref["path"]).resolve()
    if not path.is_relative_to(Path(base).resolve()):
        raise ValueError("evidence path escapes its containing evidence directory")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if ref.get("sha256") != digest:
        raise ValueError(f"stale evidence: {path.name}")
    return {"path": str(path), "sha256": digest}


def _identity(value):
    return " ".join(value.casefold().split()) if isinstance(value, str) else ""


def _observation(status, *details, **extra):
    return {"status": status, "details": list(details), **extra}


def _silver(data, base, answer):
    report_ref = _ref(data["silver_review"], base)
    report = _load(report_ref["path"])
    review_base = Path(report_ref["path"]).parent
    if _ref(report.get("final_answer"), review_base) != answer:
        raise ValueError("Silver review does not bind the current final answer")
    author = _identity(data.get("manifest_author"))
    reviewer = _identity(report.get("reviewer"))
    people = data.get("implementers")
    if (not isinstance(people, list) or not people or any(not _identity(p) for p in people)
            or report.get("implementers") != people or not author or not reviewer
            or reviewer in {_identity(p) for p in people} | {author}):
        raise ValueError("Silver review requires an independent reviewer and complete implementers census")
    provenance_ref = _ref(report.get("reviewer_provenance"), review_base)
    provenance = _load(provenance_ref["path"])
    if (_identity(provenance.get("reviewer")) != reviewer
            or provenance.get("role") != "lite_grade_review" or not provenance.get("task_id")):
        raise ValueError("Silver review dispatch provenance is missing or inconsistent")
    provider = data.get("provider")
    if provenance.get("provider") != provider or provider not in {"codex", "claude"}:
        raise ValueError("Silver review requires matching provider provenance")
    if provider == "codex" and (provenance.get("model") != "gpt-6-astra" or provenance.get("model_family") != "astra"):
        raise ValueError("Silver substantive review requires an Astra reviewer")
    if provider == "claude" and (not isinstance(provenance.get("model"), str)
                                or not provenance["model"].strip()):
        raise ValueError("Silver substantive review requires the actual configured Claude model")
    if (provenance.get("final_answer_sha256") != answer["sha256"]
            or provenance.get("ledger_sha256") != _ref(data.get("ledger"), base)["sha256"]):
        raise ValueError("Silver dispatch provenance does not bind the current final answer and ledger")
    if report.get("verdict") != "SILVER" or report.get("review_mode") != "comprehensive":
        raise ValueError("Silver requires a comprehensive SILVER review")
    checks = report.get("checks", {})
    for name in SILVER_CHECKS:
        check = checks.get(name, {})
        if (not isinstance(check, dict) or check.get("pass") is not True
                or not isinstance(check.get("rationale"), str) or not check["rationale"].strip()):
            raise ValueError(f"Silver substantive review missing: {name}")
    refs = [report_ref, provenance_ref]
    for name in ("ledger", "assumption_census", "target_contract"):
        pin = _ref(report.get(name), review_base)
        if pin != _ref(data.get(name), base):
            raise ValueError(f"Silver review has a different {name}")
        refs.append(pin)
    ledger_ref = _ref(report["ledger"], review_base)
    ledger = _load(ledger_ref["path"])
    rows = ledger.get("rows")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Silver requires a nonempty step ledger")
    seen, triaged = set(), []
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"] or row["id"] in seen:
            raise ValueError("Silver ledger requires unique row ids")
        seen.add(row["id"])
        if row.get("closed") is not True or type(row.get("triaged")) is not bool:
            raise ValueError("Silver ledger contains an open or untriaged row")
        if row["triaged"]:
            triaged.append(row["id"])
            if row.get("status") != "lean-certified":
                raise ValueError("Silver requires every L3-triaged row to be lean-certified")
            for name in ("certificate", "axiom_report", "premise_manifest"):
                refs.append(_ref(row.get(name), Path(ledger_ref["path"]).parent))
    selected = report.get("triaged_rows")
    if (not isinstance(selected, list)
            or any(not isinstance(row, str) or not row.strip() for row in selected)
            or len(selected) != len(set(selected))):
        raise ValueError("Silver triaged_rows must be an array of unique nonempty string row IDs")
    if sorted(selected) != sorted(triaged):
        raise ValueError("Silver review triage census differs from the current ledger")
    return _observation("review_recorded", "Current independent comprehensive review and L3 evidence recorded.",
                        evidence=refs, evidence_basis="Hashed review receipts only; reviewer identities are self-reported and mathematical correctness and Lean certificates are not independently replayed.")


def assess_evidence(manifest_path, *, mode, paper_state=None, max_pages=None):
    """Reassess current transitive evidence without launching model calls.

    Gold invokes live Lean in Heavy only. Paper invokes the full current audit,
    including isolated compilation. Its actual output must be the manifest's
    final answer; a state ``final_answer`` reference is an additional assertion.
    Missing/unavailable/stale evidence fails closed and is returned in details.
    """
    result = {"answer": None, "silver": _observation("pending"),
              "gold": _observation("not_applicable" if mode != "heavy" else "pending"),
              "paper": _observation("pending")}
    try:
        path = Path(manifest_path).resolve()
        data = _load(path)
        answer = _ref(data.get("final_answer"), path.parent)
        result["answer"] = answer
    except (OSError, ValueError, TypeError, RecursionError) as error:
        for kind in ("silver", "paper") + (("gold",) if mode == "heavy" else ()):
            result[kind] = _observation("failed", str(error))
        return result
    if "silver_review" in data:
        try:
            result["silver"] = _silver(data, path.parent, answer)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as error:
            result["silver"] = _observation("failed", str(error))
    if mode == "heavy" and data.get("grade") == "GOLD":
        try:
            runtime_errors = verify_kernel_runtime(data, path.parent)
            errors = runtime_errors + audit_manifest(data, path.parent, kernel_runtime_verified=not runtime_errors)
            result["gold"] = _observation("failed" if errors else "verified", *errors)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, RuntimeError, RecursionError, subprocess.SubprocessError) as error:
            result["gold"] = _observation("failed", str(error))
    if paper_state is not None:
        try:
            state_path = Path(paper_state).resolve()
            state = _load(state_path)
            if not state_path.is_relative_to(path.parent):
                raise ValueError("paper state escapes the problem evidence directory")
            if state.get("work_dir") and not Path(state["work_dir"]).resolve().is_relative_to(path.parent):
                raise ValueError("paper work directory escapes the problem evidence directory")
            output = Path(state["output"]).resolve()
            if not output.is_relative_to(path.parent):
                raise ValueError("paper output escapes the problem evidence directory")
            bound = {"path": str(output), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}
            if bound != answer:
                raise ValueError("audited paper output must be the current final answer path and hash")
            if "final_answer" in state and _ref(state["final_answer"], state_path.parent) != answer:
                raise ValueError("paper final_answer reference differs from its audited output")
            report = audit_paper(state_path, require_all_gates=True)
            errors = list(report.get("errors", []))
            if not report.get("pass") or report.get("compile", {}).get("pass") is not True:
                errors.append("full paper audit and current compilation must pass")
            if max_pages is not None:
                pages = report.get("compile", {}).get("pdf_pages")
                if type(max_pages) is not int or max_pages < 1:
                    errors.append("max_pages must be a positive integer")
                elif type(pages) is not int or not 0 < pages <= max_pages:
                    errors.append("current compiled paper exceeds page limit or page count is unavailable")
            if _ref(data["final_answer"], path.parent) != answer:
                errors.append("final answer changed during paper audit")
            result["paper"] = _observation("failed" if errors else "complete", *errors, audit=report)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, RuntimeError, RecursionError, subprocess.SubprocessError) as error:
            result["paper"] = _observation("failed", str(error))
    return result
