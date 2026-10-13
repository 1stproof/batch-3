"""Two bounded fresh-context manuscript/guideline reviews with revision evidence.

These checks bind declared provenance and decisions to artifacts. They do not
authenticate reviewer identities or establish that a model actually had fresh memory.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from .tex_inventory import inventory_tex, strip_comments
from .versioning import sha256_file

READER_POLICY = "two-fresh-astra-v2"
READER_AXES = ("exposition", "attribution")
READER_RUBRIC = """Read the supplied manuscript from beginning to end for a Batch3 mathematical
exam assessor. The manuscript is the sole scientific input; this rubric is instruction,
not scientific evidence. Assess two paper-writing axes separately: exposition (whether
the intended reader can reconstruct the argument, definitions,
notation, transitions and promised explanations), and attribution (whether credit,
citations and external dependencies are stated honestly and sufficiently within the
manuscript). Do not infer source verification from metadata or claim access to unseen
sources, Lean proofs, author maps or prior reports. Absence of external source-verification
evidence in this isolated read is not by itself a mathematical fault: distinguish an
unsupported manuscript claim from an inspection unavailable to this reader. Record located findings and limits
of what the manuscript establishes. Do not evaluate ordinary journal novelty,
publishability, journal readiness or stylistic preferences as acceptance criteria.
Each axis needs PASS or FAIL, substantive findings and unresolved_findings. Issues need
an axis, manuscript location, severity (substantive or style), and concrete finding.
Existing mathematical correctness and faithfulness audits remain separate; this read does
not certify correctness or require reproof. Flag a missing manuscript inference as a
reader obstacle without substituting a new correctness audit. Do not require Lean
artifacts, build provenance or verification marketing in the mathematical paper unless
the paper itself makes a verification claim or formalization is its subject.
An unsupported load-bearing attribution is substantive; decorative figures,
arbitrary length changes and optional orientation are not required repairs.
"""


def isolated_manuscript(text: str, *, source_dir: Path | None = None) -> str:
    """Conservative fail-closed native single-file route; not a TeX interpreter."""
    if not isinstance(text, str) or "\\begin{document}" not in text or "\\end{document}" not in text:
        raise ValueError("isolated reader input needs a complete TeX document")
    commands = (r"\\(?:input|include|subfile|includegraphics|bibliography|addbibresource|"
                r"openin|openout|read|write|immediate|catcode|csname|directlua|special|"
                r"InputIfFileExists|IfFileExists|verbatiminput|lstinputlisting|"
                r"usepackage\s*\{(?:shellesc|luacode)\})(?![A-Za-z@])")
    if "^^" in text or re.search(commands, strip_comments(text), re.IGNORECASE):
        raise ValueError("isolated reader input must contain all scientific content in one native TeX file; external or dynamic content is unsupported")
    standard_classes = {'article', 'amsart', 'amsbook', 'report', 'book', 'memoir', 'scrartcl', 'scrreprt', 'scrbook'}
    standard_packages = {'amsmath', 'amssymb', 'amsthm', 'amsfonts', 'mathtools', 'geometry', 'hyperref',
        'cleveref', 'graphicx', 'tikz', 'tikz-cd', 'xcolor', 'color', 'babel', 'fontenc', 'inputenc',
        'lmodern', 'newtxtext', 'newtxmath', 'microtype', 'enumitem', 'booktabs', 'array', 'longtable',
        'multicol', 'caption', 'subcaption', 'float', 'url', 'natbib', 'cite', 'fancyhdr', 'titlesec',
        'tcolorbox', 'bm', 'bbm', 'mathrsfs', 'stmaryrd', 'siunitx', 'etoolbox', 'xparse', 'latexsym',
        'thmtools', 'authblk', 'algorithm', 'algorithmic', 'algorithm2e', 'listings', 'verbatim', 'setspace'}
    for match in re.finditer(r'\\(documentclass|LoadClass|usepackage|RequirePackage)\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}', strip_comments(text)):
        command, names = match.groups()
        classes = command in {'documentclass', 'LoadClass'}
        allowed = standard_classes if classes else standard_packages
        for name in names.split(','):
            name = name.strip()
            if name not in allowed or (source_dir is not None and (source_dir / (name + ('.cls' if classes else '.sty'))).exists()):
                raise ValueError('isolated reader input contains a custom or locally shadowed TeX class/package')
    return text


def validate_reader_axes(report: dict, *, approving: bool = False) -> None:
    axes = report.get("axes")
    if not isinstance(axes, dict) or set(axes) != set(READER_AXES):
        raise ValueError("reader report needs separate exposition and attribution axes")
    for axis in READER_AXES:
        item = axes[axis]
        if (not isinstance(item, dict) or item.get("verdict") not in {"PASS", "FAIL"}
                or not _text(item.get("findings")) or not isinstance(item.get("unresolved_findings"), list)
                or any(not _text(finding) for finding in item["unresolved_findings"])):
            raise ValueError(f"reader {axis} axis needs a verdict, substantive findings and unresolved findings")
        if (item["verdict"] == "PASS" and item["unresolved_findings"]) or (approving and item["verdict"] != "PASS"):
            raise ValueError(f"reader {axis} axis has unresolved findings or lacks approval")


def _text(value: object) -> bool:
    return isinstance(value, str) and len(value.strip()) >= 20


def _identity(value: object) -> str:
    return value.strip().casefold() if isinstance(value, str) else ""


def _digest(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _reference(reference: object, work: Path, *, json_record: bool = True) -> tuple[Path, dict]:
    if not isinstance(reference, dict) or not isinstance(reference.get("path"), str) or not _digest(reference.get("sha256")):
        raise ValueError("review evidence needs a path and SHA-256")
    path = Path(reference["path"])
    if not path.is_absolute():
        path = work / path
    if not path.is_file() or sha256_file(path) != reference["sha256"]:
        raise ValueError(f"review evidence is missing or stale: {path.name}")
    record = json.loads(path.read_text(encoding="utf-8")) if json_record else {}
    if not isinstance(record, dict):
        raise ValueError(f"review evidence must be a JSON object: {path.name}")
    return path.resolve(), record


def _snapshot(record: dict, expected: str) -> None:
    files = record.get("source_files")
    if not isinstance(files, list) or not files or any(
            not isinstance(item, dict) or item.get("missing") or not isinstance(item.get("path"), str)
            or not _digest(item.get("sha256")) for item in files):
        raise ValueError("before_inventory needs the complete ordinary TeX source_files inventory")
    paths = [item["path"] for item in files]
    if len(paths) != len(set(paths)) or not any(
            item["path"] == record.get("source") and item["sha256"] == record.get("source_sha256") for item in files):
        raise ValueError("before_inventory needs a unique source-file census containing its hashed root")
    material = [{"path": item["path"], "sha256": item.get("sha256"), "kind": item.get("kind")} for item in files]
    computed = hashlib.sha256(json.dumps(material, sort_keys=True).encode("utf-8")).hexdigest()
    if computed != expected or record.get("source_tree_sha256") != expected:
        raise ValueError("before_inventory does not match its recorded source-tree hash")


def reader_round_errors(state: dict, *, required: bool = False) -> list[str]:
    work = Path(state["work_dir"])
    path = work / "08-reader-rounds.json"
    if not path.exists():
        return ["two fresh-reader revision cycles require 08-reader-rounds.json"] if required else []
    try:
        _reader_rounds(state, work, json.loads(path.read_text(encoding="utf-8")))
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        return [f"two-round reader review: {error}"]


def _reader_rounds(state: dict, work: Path, ledger: dict) -> None:
    schema = ledger.get("schema_version")
    if schema not in (1, 2):
        raise ValueError("unsupported reader-round schema")
    if state.get("reader_round_policy") == READER_POLICY and schema != 2:
        raise ValueError("new reader policy requires schema 2; historical reports cannot be relabeled")
    guideline_path, _ = _reference(ledger.get("guideline"), work, json_record=False)
    if schema == 2 and guideline_path.read_text(encoding="utf-8") != READER_RUBRIC:
        raise ValueError("isolated reader guideline must be the neutral instruction rubric")
    guideline_hash = ledger["guideline"]["sha256"]
    writers = ledger.get("writer_ids")
    if not isinstance(writers, list) or not writers or not all(_identity(w) for w in writers):
        raise ValueError("reader rounds need actual writer_ids")
    known_writers = {_identity(w) for w in writers}
    if state.get("raw_checkpoint"):
        _, manifest = _reference({"path": state["raw_checkpoint"]["manifest"],
                                  "sha256": state["raw_checkpoint"]["manifest_sha256"]}, work)
        known_writers.update(_identity(w) for w in manifest["evidence"]["writer_ids"])
    sidecar = work / "07-reader-audit.json"
    sidecar_reader = None
    if sidecar.exists():
        sidecar_record = json.loads(sidecar.read_text(encoding="utf-8"))
        sidecar_reader = _identity(sidecar_record.get("reader_id"))
        recorded_writers = sidecar_record.get("writer_ids")
        if not isinstance(recorded_writers, list) or not all(_identity(w) for w in recorded_writers):
            raise ValueError("reader sidecar writer identities are malformed")
        known_writers.update(_identity(w) for w in recorded_writers)
    rounds = ledger.get("rounds")
    if not isinstance(rounds, list) or len(rounds) != 2:
        raise ValueError("exactly two sequential fresh-reader rounds are required; no third stylistic round")
    if sidecar_reader is not None and sidecar_reader != _identity(rounds[1].get("reader_id")):
        raise ValueError("legacy reader-audit records must come from the second round's reader")
    identities: set[str] = set()
    reports: set[Path] = set()
    previous_after = None
    disposition_hashes = []
    for number, item in enumerate(rounds, 1):
        identity = _identity(item.get("reader_id"))
        if not identity or identity in identities or identity in known_writers:
            raise ValueError("each round needs a different reader, independent of all known writers")
        identities.add(identity)
        before, after = item.get("before_source_tree_sha256"), item.get("after_source_tree_sha256")
        if not _digest(before) or not _digest(after):
            raise ValueError("each round needs before and after source-tree SHA-256 values")
        if previous_after is not None and before != previous_after:
            raise ValueError("round two must read the manuscript resulting from round one's revision")
        _, snapshot = _reference(item.get("before_inventory"), work)
        _snapshot(snapshot, before)
        if schema == 2:
            _isolated_snapshot(item.get("manuscript_input"), work, snapshot)
        report_path, report = _reference(item.get("reader_report"), work)
        if report_path in reports:
            raise ValueError("fresh rounds need different reviewer artifacts")
        reports.add(report_path)
        provenance = ({"kind": "fresh", "prior_context": False, "manuscript_and_guideline_only": True}
                      if schema == 1 else {"kind": "fresh", "prior_context": False,
                          "sole_scientific_input": "manuscript", "rubric_is_instruction": True})
        if (_identity(report.get("reviewer_id")) != identity or report.get("model") != "gpt-6-astra"
                or report.get("provenance") != provenance
                or report.get("source_tree_sha256") != before or report.get("guideline_sha256") != guideline_hash
                or not _text(report.get("findings"))):
            raise ValueError(f"round {number} needs fresh-context Astra manuscript/guideline findings bound to its input")
        if schema == 2:
            if report.get("manuscript_sha256") != item["manuscript_input"]["sha256"]:
                raise ValueError("reader report must bind the exact sole manuscript input bytes")
            validate_reader_axes(report)
        issues = report.get("issues")
        if not isinstance(issues, list) or any(not isinstance(issue, dict) or not _identity(issue.get("id"))
                or issue.get("severity") not in {"substantive", "style"} or not _text(issue.get("finding")) for issue in issues):
            raise ValueError("reader issues need IDs, substantive/style severity, and concrete findings")
        if schema == 2 and any(issue.get("axis") not in READER_AXES or not _identity(issue.get("location")) for issue in issues):
            raise ValueError("reader issues need a separate axis and manuscript location")
        issue_ids = [issue["id"] for issue in issues]
        if len(issue_ids) != len(set(issue_ids)):
            raise ValueError("reader issue IDs must be unique within each round")
        _, disposition = _reference(item.get("disposition_report"), work)
        if (_identity(disposition.get("writer_id")) not in known_writers
                or disposition.get("before_source_tree_sha256") != before
                or disposition.get("after_source_tree_sha256") != after
                or disposition.get("reader_report_sha256") != item["reader_report"]["sha256"]
                or not _text(disposition.get("revision_summary"))):
            raise ValueError("writer disposition must bind the actual reader report and before/after revision")
        responses = disposition.get("responses")
        if not isinstance(responses, list) or any(not isinstance(response, dict)
                or response.get("action") not in {"revised", "justified-no-op"}
                or not _text(response.get("reason")) for response in responses):
            raise ValueError("every issue needs a substantive revision or justified-no-op response")
        response_ids = [response.get("issue_id") for response in responses]
        if len(response_ids) != len(set(response_ids)) or set(response_ids) != set(issue_ids):
            raise ValueError("writer responses must cover every reader issue exactly once")
        if before == after and (not _text(disposition.get("no_change_reason"))
                               or any(response["action"] == "revised" for response in responses)):
            raise ValueError("unchanged manuscripts require a justified no-op, not a claimed revision")
        disposition_hashes.append(item["disposition_report"]["sha256"])
        previous_after = after
    _, verification = _reference(ledger.get("final_verification"), work)
    current = inventory_tex(Path(state["output"]))["source_tree_sha256"]
    if schema == 2:
        final_snapshot = inventory_tex(Path(state["output"]))
        _isolated_snapshot(ledger.get("final_manuscript_input"), work, final_snapshot)
        if verification.get("manuscript_sha256") != ledger["final_manuscript_input"]["sha256"]:
            raise ValueError("final verification must bind its exact manuscript input bytes")
        validate_reader_axes(verification, approving=True)
    if (_identity(verification.get("reviewer_id")) != _identity(rounds[1]["reader_id"])
            or verification.get("model") != "gpt-6-astra"
            or verification.get("provenance") != {"kind": "post-revision-verification", "stylistic_round": False}
            or verification.get("source_tree_sha256") != previous_after or current != previous_after
            or verification.get("guideline_sha256") != guideline_hash
            or verification.get("disposition_report_sha256s") != disposition_hashes
            or verification.get("verdict") != "PASS" or verification.get("unresolved_substantive_issues") != []
            or not _text(verification.get("findings"))):
        raise ValueError("final revision verification must pass on the current manuscript, both dispositions, and guideline; substantive issues block release")


def _isolated_snapshot(reference: object, work: Path, snapshot: dict) -> None:
    path, _ = _reference(reference, work, json_record=False)
    isolated_manuscript(path.read_text(encoding="utf-8"), source_dir=Path(snapshot["source"]).parent)
    files = snapshot.get("source_files")
    if (not isinstance(files, list) or len(files) != 1 or files[0].get("kind") != "tex"
            or reference["sha256"] != snapshot.get("source_sha256")
            or files[0].get("path") != snapshot.get("source")):
        raise ValueError("reader input must faithfully preserve the entire single-file source snapshot")
