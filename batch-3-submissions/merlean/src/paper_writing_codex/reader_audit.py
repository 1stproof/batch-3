"""Evidence checks for reader-facing mathematics, not automated semantic approval."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

from .tex_inventory import inventory_tex
from .versioning import sha256_file


def substantive(value: object) -> bool:
    return isinstance(value, str) and len(value.strip()) >= 20


def shrink_justification_errors(report: dict) -> list[str]:
    delta = report.get("main_text_characters_delta")
    if isinstance(delta, bool) or not isinstance(delta, (int, float)) or not math.isfinite(delta):
        return ["shrink report needs a finite numeric main-text delta"]
    if delta >= 0 and not substantive(report.get("semantic_justification")):
        return ["nonnegative shrink delta needs explicit semantic_justification; never delete a proof bridge to meet a quota"]
    return []


def _load(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, dict) and value:
            return value
    except (OSError, ValueError):
        pass
    errors.append(f"reader audit requires a valid JSON object: {path.name}")
    return {}


def _review_record(ref: object, work: Path, identity: str, errors: list[str], label: str) -> dict:
    if not isinstance(ref, dict) or not isinstance(ref.get("path"), str):
        errors.append(f"{label} needs a typed reviewer JSON reference")
        return {}
    path = Path(ref["path"])
    if not path.is_absolute():
        path = work / path
    if not path.is_file() or ref.get("sha256") != sha256_file(path):
        errors.append(f"{label} is missing or stale")
        return {}
    record = _load(path, errors)
    if record.get("reviewer_id") != identity:
        errors.append(f"{label} reviewer identity disagrees with sidecar")
    if (record.get("verdict") not in {"PASS", "FAIL"}
            or not isinstance(record.get("unresolved_findings"), list)
            or not substantive(record.get("findings"))
            or not re.fullmatch(r"[0-9a-f]{64}", str(record.get("source_tree_sha256", "")))):
        errors.append(f"{label} needs verdict, unresolved_findings, substantive findings and manuscript SHA-256")
    return record


def _approving_record(record: dict, snapshot: str, errors: list[str], label: str) -> None:
    if record.get("verdict") != "PASS" or record.get("unresolved_findings") != []:
        errors.append(f"{label} is not an approving PASS with no unresolved findings")
    if record.get("source_tree_sha256") != snapshot:
        errors.append(f"{label} reviewed manuscript snapshot is stale")


def reader_audit_errors(state: dict, *, required: bool = False) -> list[str]:
    try:
        return _reader_audit_errors(state, required=required)
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        return ["reader audit contains malformed or unreadable evidence"]


def _reader_audit_errors(state: dict, *, required: bool = False) -> list[str]:
    """Fail closed at late gates; preliminary preservation audits stay available."""
    late = ("terminology", "preservation", "final")
    required = required or any(state.get("gates", {}).get(g, {}).get("status") == "pass" for g in late)
    work = Path(state["work_dir"])
    path = work / "07-reader-audit.json"
    if not required and not path.exists():
        return []
    errors: list[str] = []
    report = _load(path, errors)
    if not report:
        return errors
    candidate = inventory_tex(Path(state["output"]))
    units = {u["id"]: u for u in candidate["units"]}
    if report.get("verdict") != "PASS":
        errors.append("fresh-reader verdict must be PASS with resolved findings")
    reader = report.get("reader_id")
    writers = report.get("writer_ids")
    if (not isinstance(reader, str) or not reader.strip() or not isinstance(writers, list)
            or not writers or any(not isinstance(w, str) or not w.strip() for w in writers)
            or (isinstance(reader, str) and isinstance(writers, list)
                and reader.strip().casefold() in {w.strip().casefold() for w in writers if isinstance(w, str)})):
        errors.append("fresh-reader identity must be distinct from every declared writer")
    if report.get("fresh_context") is not True or report.get("manuscript_only_first_pass") is not True:
        errors.append("reader must attest fresh context and manuscript-only sequential first pass")
    proof_auditor = report.get("proof_auditor_id")
    if (not isinstance(proof_auditor, str) or not proof_auditor.strip()
            or proof_auditor.strip().casefold() == str(reader).strip().casefold()
            or (isinstance(writers, list) and proof_auditor.strip().casefold() in {
                w.strip().casefold() for w in writers if isinstance(w, str)})):
        errors.append("proof_auditor_id must differ from the fresh reader and all writers")
    first = _review_record(report.get("first_pass_report"), work, reader, errors, "fresh-reader first-pass evidence")
    if first.get("provenance") != {"kind": "fresh", "manuscript_only": True}:
        errors.append("first-pass reviewer record must attest fresh manuscript-only provenance")
    final = first
    if "final_reader_report" in report:
        final = _review_record(report["final_reader_report"], work, reader, errors, "final reader evidence")
        if final.get("provenance") != {
                "kind": "reread", "manuscript_only": True,
                "prior_report_sha256": report.get("first_pass_report", {}).get("sha256")}:
            errors.append("final reader reread must link the preserved first-pass report")
    _approving_record(final, candidate["source_tree_sha256"], errors, "final reader evidence")
    proof_review = _review_record(report.get("proof_audit_report"), work, proof_auditor, errors, "proof-audit evidence")
    if proof_review.get("provenance") != {"kind": "independent-proof"}:
        errors.append("proof-audit reviewer record needs independent-proof provenance")
    _approving_record(proof_review, candidate["source_tree_sha256"], errors, "proof-audit evidence")
    if report.get("source_tree_sha256") != candidate.get("source_tree_sha256"):
        errors.append("fresh-reader manuscript snapshot is stale")
    # The orchestrator binds the actual reading record to parser IDs after the
    # unprimed first pass; no proof ledger or inventory is supplied to the reader.
    if report.get("read_order") != candidate.get("reading_order"):
        errors.append("fresh-reader read_order must cover the exact expanded document order")
    findings = report.get("findings")
    if not isinstance(findings, dict) or any(not substantive(findings.get(k)) for k in (
            "sequential_read", "proof_bridges", "terminology")):
        errors.append("fresh-reader findings need substantive sequential_read, proof_bridges, terminology evidence")

    proofs = report.get("proofs")
    if not isinstance(proofs, list):
        proofs = []
    proof_ids = [p.get("unit_id") for p in proofs if isinstance(p, dict)]
    expected = {u["id"] for u in units.values() if u.get("kind") == "proof"}
    if set(proof_ids) != expected or len(proof_ids) != len(set(proof_ids)):
        errors.append("fresh-reader proof census must cover every current proof exactly once")
    for proof in proofs:
        if not isinstance(proof, dict):
            errors.append("invalid fresh-reader proof record")
            continue
        bridges = proof.get("bridges")
        if not isinstance(bridges, list):
            errors.append("proof record needs a bridges list")
            continue
        if not bridges and not substantive(proof.get("no_bridges_reason")):
            errors.append("proof needs load-bearing bridges or a substantive no_bridges_reason")
        for bridge in bridges:
            if (not isinstance(bridge, dict) or bridge.get("location_unit_id") not in units
                    or not substantive(bridge.get("claim")) or not substantive(bridge.get("justification"))):
                errors.append("proof bridge needs a live location, claim, and justification")

    # Hash-bound comparison to the complete draft; recovery text alone is not a proof.
    snapshot_path = work / "05-pre-shrink-inventory.json"
    if not snapshot_path.is_file():
        errors.append("fresh-reader preservation needs the frozen pre-shrink inventory")
    if snapshot_path.is_file():
        snapshot = _load(snapshot_path, errors).get("inventory", {})
        changed = {u["id"] for u in snapshot.get("units", []) if u.get("kind") == "proof"
                   and (u["id"] not in units or units[u["id"]].get("normalized_sha256") != u.get("normalized_sha256"))}
        preservation = report.get("proof_preservation", [])
        if not isinstance(preservation, list):
            preservation = []
        ids = [p.get("original_unit_id") for p in preservation if isinstance(p, dict)]
        if set(ids) != changed or len(ids) != len(set(ids)):
            errors.append("reader proof_preservation must cover every removed or rewritten frozen proof exactly once")
        if report.get("pre_shrink_sha256") != sha256_file(snapshot_path):
            errors.append("reader pre-shrink snapshot is missing or stale")
        for entry in preservation:
            if not isinstance(entry, dict) or not substantive(entry.get("reason")):
                errors.append("proof preservation needs a substantive reader reason")
                continue
            if entry.get("disposition") == "preserved":
                target = units.get(entry.get("replacement_unit_id"), {})
                if target.get("kind") != "proof":
                    errors.append("preserved proof bridge needs a surviving proof destination")
            elif entry.get("disposition") == "omitted_nonessential":
                if entry.get("load_bearing") is not False:
                    errors.append("a load-bearing proof cannot be omitted into a recovery ledger")
            elif entry.get("disposition") == "cited":
                if entry.get("citation_key") not in candidate.get("citations", []):
                    errors.append("cited proof bridge needs a citation in the current manuscript")
            else:
                errors.append("unknown reader proof-preservation disposition")

    terminology = report.get("terminology")
    if not isinstance(terminology, list) or not terminology:
        errors.append("terminology needs a nonempty concept/evidence census")
        terminology = []
    concepts: set[str] = set()
    terms: set[str] = set()
    notations: dict[str, list[str]] = {}
    text = "\n".join(u.get("normalized_text", "") for u in units.values())
    for entry in terminology:
        if not isinstance(entry, dict):
            errors.append("invalid terminology record")
            continue
        concept, term = entry.get("concept"), entry.get("term")
        if not isinstance(concept, str) or not concept.strip() or not isinstance(term, str) or not term.strip():
            errors.append("terminology record needs concept and term")
            continue
        if concept.casefold() in concepts or term.casefold() in terms:
            errors.append("terminology has duplicate concepts or conflicting chosen terms")
        concepts.add(concept.casefold())
        terms.add(term.casefold())
        notation = entry.get("notation")
        if notation:
            scope = entry.get("notation_scope", "")
            if not isinstance(scope, str):
                errors.append("notation_scope must identify an explicit manuscript scope")
                scope = ""
            previous = notations.get(notation, []) if isinstance(notation, str) else []
            if (not isinstance(notation, str) or (previous and
                    (not scope.strip() or "" in previous or scope.strip() in previous))):
                errors.append("terminology assigns one notation to multiple concepts")
            else:
                notations.setdefault(notation, []).append(scope.strip())
        location = units.get(entry.get("defining_unit_id"), {})
        if term not in location.get("normalized_text", ""):
            errors.append("chosen terminology must occur at its live defining_unit_id")
        if entry.get("status") not in {"standard", "local"}:
            errors.append("terminology status must be standard or local")
        if entry.get("status") == "local" and not substantive(entry.get("rationale")):
            errors.append("local terminology needs explicit necessity/search rationale")
        evidence = entry.get("evidence")
        if not isinstance(evidence, dict) or not substantive(evidence.get("locator")):
            errors.append("terminology needs source/search evidence with a locator")
        else:
            source = Path(evidence.get("path", ""))
            if not source.is_absolute():
                source = work / source
            if not source.is_file() or evidence.get("sha256") != sha256_file(source):
                errors.append("terminology source/search evidence is missing or stale")
        rejected = entry.get("rejected_variants")
        if not isinstance(rejected, list) or any(not isinstance(v, str) or not v.strip() for v in rejected):
            errors.append("terminology rejected_variants must be a list of nonempty strings")
        else:
            for variant in rejected:
                if re.search(r"(?<!\w)" + re.escape(variant) + r"(?!\w)", text, re.IGNORECASE):
                    errors.append(f"unresolved terminology variant: {variant}")
    defined = {e.get("defining_unit_id") for e in terminology if isinstance(e, dict)}
    if {u["id"] for u in units.values() if u.get("environment") == "definition"} - defined:
        errors.append("terminology census misses an explicit definition")
    definitions_path = work / "06-definition-ledger.json"
    if definitions_path.is_file():
        definitions = _load(definitions_path, errors).get("definitions", [])
        if any(str(d.get("concept", "")).casefold() not in concepts for d in definitions):
            errors.append("terminology census misses a definition-ledger concept")
    return errors
