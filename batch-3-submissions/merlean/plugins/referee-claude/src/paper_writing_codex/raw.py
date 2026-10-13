"""Immutable, evidenced pre-editorial reconstruction and separate candidate lineage.

Hashes certify recorded bytes, not mathematical completeness. The latter remains an
independent audit obligation. No existing manuscript is automatically historical raw.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
from typing import Any

from .tex_inventory import inventory_tex, strip_comments
from .versioning import sha256_file


LATE_GATES = {"lemmas", "draft", "compression", "final-matter", "terminology", "preservation", "final"}
ORIGINS = ("pre-editorial", "retrospective-reconstruction")
DEPENDENCY = re.compile(
    r"\\(?P<command>input|include|subfile|bibliography|addbibresource|includegraphics)"
    r"\s*(?:\[[^\]]*\]\s*)?\{(?P<target>[^{}]+)\}"
)
PACKAGE = re.compile(r"\\(?P<command>usepackage|documentclass|RequirePackage|LoadClass)(?:\[[^\]]*\])?\{(?P<target>[^}]+)\}")


def _substantive(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _findings(value: Any) -> bool:
    return isinstance(value, str) and len(value.strip()) >= 20


def _audit_findings(value: Any) -> bool:
    # Retain already-frozen structured location/assessment reviews; do not coerce
    # arbitrary JSON containers to strings and mistake them for evidence.
    return _findings(value) or (isinstance(value, list) and bool(value) and all(
        isinstance(row, dict) and _substantive(row.get("location")) and _findings(row.get("assessment"))
        for row in value))


def _identity(value: str) -> str:
    return value.strip().casefold()


def _regular(path: Path) -> None:
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError(f"raw provenance path contains a symlink: {path}")
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"raw provenance needs a regular single-link file: {path}")


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_new(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)


def _encoded(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def _resolve(parent: Path, command: str, target: str) -> Path:
    if any(character in target for character in "\\#{}$"):
        raise ValueError(f"dynamic raw dependency must be made literal: {target}")
    path = Path(target)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"raw dependencies must stay relative inside the source tree: {target}")
    path = parent / path
    if not path.suffix:
        if command == "includegraphics":
            matches = [path.with_suffix(ext) for ext in (".pdf", ".png", ".jpg", ".jpeg", ".eps")
                       if path.with_suffix(ext).is_file()]
            if len(matches) != 1:
                raise ValueError(f"raw graphics dependency is missing or ambiguous: {target}")
            return matches[0]
        path = path.with_suffix(".bib" if command in {"bibliography", "addbibresource"} else ".tex")
    return path


def _tree(source: Path, assets: list[Path]) -> list[Path]:
    root = source.parent
    pending = [source, *assets]
    found: set[Path] = set()
    while pending:
        path = pending.pop().absolute()
        if not path.is_relative_to(root):
            raise ValueError(f"raw dependency escapes source directory: {path}")
        _regular(path)
        if path in found:
            continue
        found.add(path)
        if path.suffix.lower() not in {".tex", ".sty", ".cls"}:
            continue
        text = strip_comments(path.read_text(encoding="utf-8"))
        # Do not certify unsupported dependency mechanisms via a partial parser.
        if re.search(r"\\(?:import|subimport|inputfrom|includefrom|graphicspath|includeonly)\b", text):
            raise ValueError("raw source uses unsupported dependency routing; use literal local paths")
        for match in DEPENDENCY.finditer(text):
            pending.extend(_resolve(root, match["command"], target.strip())
                           for target in match["target"].split(","))
        if re.search(r"\\(?:input|include|subfile)\b(?!\s*\{)", text):
            raise ValueError("raw TeX inputs must use literal braced paths")
        # Local package/class files are dependencies too; installed TeX packages are not.
        for match in PACKAGE.finditer(text):
            for name in match["target"].split(","):
                local = root / (name.strip() + (".sty" if match["command"] in {"usepackage", "RequirePackage"} else ".cls"))
                if local.exists():
                    pending.append(local)
    return sorted(found)


def raw_inventory(source: Path, assets: list[Path] | None = None) -> dict:
    source = source.expanduser().absolute()
    files = _tree(source, [p.expanduser().absolute() for p in assets or []])
    entries = [{"path": str(p.relative_to(source.parent)), "sha256": sha256_file(p)} for p in files]
    return {"source_sha256": sha256_file(source), "source_tree_sha256": hashlib.sha256(_encoded(entries)).hexdigest(),
            "files": entries}


def _evidence(state: dict, source: Path, evidence_path: Path) -> tuple[dict, list[Path]]:
    _regular(evidence_path)
    record = _json(evidence_path)
    if record.get("schema_version") != 1 or record.get("source_sha256") != sha256_file(source):
        raise ValueError("raw evidence must bind the current raw source SHA-256")
    if not record.get("selected_results"):
        raise ValueError("raw evidence needs selected result identifiers")
    sources = record.get("source_records")
    if not isinstance(sources, list) or not sources:
        raise ValueError("raw evidence needs actual proof/source/status records and read findings")
    dependencies = [evidence_path]
    for item in sources:
        if item.get("kind") not in {"lean", "natural-language", "literature", "research-status"} or not _substantive(item.get("findings")):
            raise ValueError("raw source evidence needs its kind and read findings")
    graph = record.get("critical_path")
    if not graph and not _substantive(record.get("critical_path_unavailable_reason")):
        raise ValueError("raw evidence needs the available critical path or an explicit unavailable reason")
    audit = record.get("independent_audit", {})
    for item in [*sources, record.get("evidence_assessment", {}), record.get("reconstruction_map", {}), audit, *([graph] if graph else [])]:
        if not item.get("path") or not item.get("sha256"):
            raise ValueError("raw evidence dependency needs a path and SHA-256")
        path = Path(item["path"]).expanduser().absolute()
        _regular(path)
        if sha256_file(path) != item["sha256"]:
            raise ValueError(f"raw evidence dependency hash mismatch: {path}")
        dependencies.append(path)
    verdict = _json(Path(audit["path"]).expanduser().absolute())
    writers = record.get("writer_ids")
    if not isinstance(writers, list) or not writers or not all(_substantive(w) for w in writers):
        raise ValueError("raw evidence needs actual reconstruction writer_ids")
    if (not _substantive(verdict.get("reviewer_id")) or verdict.get("reviewer_id") in writers or verdict.get("verdict") != "PASS"
            or verdict.get("raw_source_sha256") != record["source_sha256"]
            or verdict.get("unresolved_fidelity_issues") != []
            or not isinstance(verdict.get("research_gaps"), list)
            or not _audit_findings(verdict.get("findings"))
            or _identity(verdict["reviewer_id"]) in {_identity(w) for w in writers}):
        raise ValueError("raw audit must identify its reviewer, bind the raw hash, and pass fidelity with research gaps explicit")
    return record, list(dict.fromkeys(dependencies))


def raw_errors(state: dict, *, required: bool = False, lineage: bool = False) -> list[str]:
    checkpoint = state.get("raw_checkpoint")
    if not checkpoint:
        return (["raw reconstruction is uncertified; run freeze-raw and start-from-raw (legacy runs require explicit migration)"]
                if required else [])
    try:
        manifest_path = Path(checkpoint["manifest"])
        _regular(manifest_path)
        if sha256_file(manifest_path) != checkpoint["manifest_sha256"]:
            raise ValueError("raw manifest hash changed")
        manifest = _json(manifest_path)
        if manifest.get("origin") not in ORIGINS or manifest.get("schema_version") != 1:
            raise ValueError("raw manifest has unsupported provenance")
        for item in manifest["files"]:
            for field in ("source", "snapshot"):
                path = Path(item[field])
                _regular(path)
                if sha256_file(path) != item["sha256"]:
                    raise ValueError(f"raw {field} file changed: {path}")
        manuscript = [item for item in manifest["files"] if item["kind"] == "manuscript"]
        source_files = [Path(item["source"]) for item in manuscript]
        if raw_inventory(Path(manifest["source"]), source_files)["source_tree_sha256"] != manifest["source_tree_sha256"]:
            raise ValueError("raw source dependency tree changed after freezing")
        frozen_files = {Path(item["snapshot"]) for item in manuscript}
        if set(_tree(Path(manifest["root"]), list(frozen_files))) != frozen_files:
            raise ValueError("raw snapshot dependency tree changed after freezing")
        evidence_source = next(item["source"] for item in manifest["files"] if item["kind"] == "evidence")
        _evidence(state, Path(manifest["source"]), Path(evidence_source))
        inventory_path = Path(manifest["inventory"])
        _regular(inventory_path)
        if sha256_file(inventory_path) != manifest["inventory_sha256"]:
            raise ValueError("raw inventory hash changed")
        if lineage:
            start = state.get("raw_lineage", {})
            if start.get("manifest_sha256") != checkpoint["manifest_sha256"] or start.get("output") != state["output"]:
                raise ValueError("candidate lacks start-from-raw lineage; explicit migration is required")
            seed = Path(start["seed_manifest"])
            _regular(seed)
            if sha256_file(seed) != start["seed_manifest_sha256"]:
                raise ValueError("raw candidate seed manifest changed")
            if Path(state["output"]).resolve() in {Path(item["source"]).resolve() for item in manifest["files"]}:
                raise ValueError("candidate aliases raw provenance")
        return []
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
        return [f"raw checkpoint: {error}"]


def candidate_raw_inventory(state: dict) -> dict:
    start = state.get("raw_lineage", {})
    seed_path = Path(start["seed_manifest"])
    _regular(seed_path)
    if sha256_file(seed_path) != start["seed_manifest_sha256"]:
        raise ValueError("raw candidate seed manifest changed")
    seed = _json(seed_path)
    # Older seeds recorded the complete file list but not explicit assets.
    assets = seed.get("assets", [item["path"] for item in seed["files"] if item["path"] != state["output"]])
    return raw_inventory(Path(state["output"]), [Path(p) for p in assets])


def raw_preservation_errors(state: dict, *, required: bool = False) -> list[str]:
    """Require a current independent fidelity review across raw and the approved baseline."""
    path = Path(state["work_dir"]) / "08-raw-preservation-audit.json"
    if not path.exists():
        return ["raw preservation needs 08-raw-preservation-audit.json"] if required else []
    try:
        _regular(path)
        record = _json(path)
        writers = record.get("writer_ids")
        if (not isinstance(writers, list) or not writers or not all(_substantive(w) for w in writers)
                or record.get("verdict") != "PASS" or not _substantive(record.get("reviewer_id")) or record.get("reviewer_id") in writers
                or record.get("unresolved_fidelity_issues") != []):
            raise ValueError("raw preservation requires identified independent PASS and no unresolved fidelity issues")
        manifest = _json(Path(state["raw_checkpoint"]["manifest"]))
        known_writers = list(manifest["evidence"]["writer_ids"])
        reader_path = Path(state["work_dir"]) / "07-reader-audit.json"
        if reader_path.exists():
            reader_writers = _json(reader_path).get("writer_ids")
            if not isinstance(reader_writers, list) or not all(_substantive(w) for w in reader_writers):
                raise ValueError("reader sidecar writer identities are malformed")
            known_writers.extend(reader_writers)
        if _identity(record["reviewer_id"]) in {_identity(w) for w in [*writers, *known_writers]}:
            raise ValueError("raw preservation reviewer must differ from raw and reader-sidecar writers")
        if record.get("raw_manifest_sha256") != state.get("raw_checkpoint", {}).get("manifest_sha256"):
            raise ValueError("raw preservation audit is not bound to the frozen raw manifest")
        if record.get("baseline_sha256") != state.get("source_sha256"):
            raise ValueError("raw preservation audit is not bound to the approved refinement baseline")
        if record.get("candidate_source_tree_sha256") != candidate_raw_inventory(state)["source_tree_sha256"]:
            raise ValueError("raw preservation audit is stale for the candidate source tree")
        for field in ("hypotheses", "proof_bridges", "research_status", "omissions_and_relocations"):
            if not _findings(record.get(field)):
                raise ValueError(f"raw preservation audit needs concrete {field} findings")
        return []
    except (OSError, ValueError, KeyError, TypeError) as error:
        return [f"raw preservation: {error}"]


def freeze_raw(state_path: Path, source: Path, origin: str, evidence: Path,
               assets: list[Path] | None = None) -> dict:
    from .workflow import verify_source, verify_output
    from .coverage import write_json
    state = _json(state_path)
    verify_source(state)
    verify_output(state, require_reservation=True)
    if origin not in ORIGINS:
        raise ValueError("raw origin must be explicitly pre-editorial or retrospective-reconstruction")
    source = source.expanduser().absolute()
    _regular(source)
    if source.suffix.lower() != ".tex":
        raise ValueError("raw source must be TeX")
    if source == Path(state["output"]) or source == Path(state.get("source") or state["output"]):
        raise ValueError("reconstruct raw in a distinct file; baseline/candidate is not historical raw")
    if state.get("raw_checkpoint"):
        raise FileExistsError("raw checkpoint already exists; it cannot be replaced")
    if state.get("gates", {}).get("critical-path", {}).get("status") != "pass":
        raise ValueError("freeze-raw requires the critical-path/evidence-assessment gate")
    if origin == "pre-editorial" and any(state.get("gates", {}).get(g, {}).get("status") == "pass" for g in LATE_GATES):
        raise ValueError("pre-editorial raw cannot be asserted after editorial gates; use retrospective-reconstruction")
    record, evidence_files = _evidence(state, source, evidence.expanduser().absolute())
    tree_hash = raw_inventory(source, assets)["source_tree_sha256"]
    audit = _json(Path(record["independent_audit"]["path"]).expanduser().absolute())
    if record.get("source_tree_sha256") != tree_hash or audit.get("raw_source_tree_sha256") != tree_hash:
        raise ValueError("raw evidence and independent audit must bind the complete source-tree hash from raw-inventory")
    files = _tree(source, [p.expanduser().absolute() for p in assets or []])
    snapshot = Path(state["work_dir"]).resolve() / "raw"
    if snapshot.exists() or snapshot.is_symlink():
        raise FileExistsError(snapshot)
    # Read and hash all inputs before creating the immutable directory.
    payloads = {p: p.read_bytes() for p in dict.fromkeys([*files, *evidence_files])}
    reserved = {"inventory.json", "manifest.json", "evidence"}
    if any(p != source and (p.relative_to(source.parent).parts[0] in reserved or p.relative_to(source.parent) == Path("paper-raw.tex")) for p in files):
        raise ValueError("raw dependency collides with reserved snapshot names")
    snapshot.mkdir()
    entries = []
    for path, data in payloads.items():
        destination = (snapshot / ("paper-raw.tex" if path == source else str(path.relative_to(source.parent)))
                       if path in files else snapshot / "evidence" / f"{len(entries):04d}-{path.name}")
        _write_new(destination, data)
        entries.append({"source": str(path), "snapshot": str(destination),
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "kind": "manuscript" if path in files else "evidence"})
    inventory_path = snapshot / "inventory.json"
    _write_new(inventory_path, _encoded(inventory_tex(snapshot / "paper-raw.tex")))
    manifest = {"schema_version": 1, "origin": origin, "source": str(source), "source_tree_sha256": tree_hash,
                "root": str(snapshot / "paper-raw.tex"), "files": entries,
                "evidence": record, "inventory": str(inventory_path),
                "inventory_sha256": sha256_file(inventory_path)}
    manifest_path = snapshot / "manifest.json"
    _write_new(manifest_path, _encoded(manifest))
    state["raw_checkpoint"] = {"manifest": str(manifest_path), "manifest_sha256": sha256_file(manifest_path)}
    state["raw_policy"] = "required-v1"
    errors = raw_errors(state)
    if errors:
        raise ValueError("; ".join(errors))
    write_json(state_path, state)
    return state["raw_checkpoint"]


def start_from_raw(state_path: Path) -> dict:
    """Seed a reserved version, copying its dependencies into an exclusive editable tree."""
    from .workflow import verify_source, verify_output
    from .coverage import write_json
    state = _json(state_path)
    if state.get("raw_lineage"):
        raise FileExistsError("candidate already started from raw")
    verify_source(state)
    verify_output(state, require_reservation=True, require_content=True)
    errors = raw_errors(state, required=True)
    if errors:
        raise ValueError("; ".join(errors))
    if state.get("raw_lineage"):
        raise FileExistsError("candidate already started from raw")
    if any(state.get("gates", {}).get(g, {}).get("status") == "pass" for g in LATE_GATES):
        raise ValueError("reopen lemmas and later gates before starting from raw")
    manifest = _json(Path(state["raw_checkpoint"]["manifest"]))
    output = Path(state["output"])
    support = output.with_name(output.stem + "-support")
    if support.exists() or support.is_symlink():
        raise FileExistsError(support)
    raw_root = Path(manifest["root"])
    mapping = {Path(item["snapshot"]): (output if Path(item["snapshot"]) == raw_root
               else support / Path(item["snapshot"]).relative_to(raw_root.parent))
               for item in manifest["files"] if item["kind"] == "manuscript"}
    payloads = {}
    for source, destination in mapping.items():
        data = source.read_bytes()
        if source.suffix.lower() in {".tex", ".sty", ".cls"}:
            def replace(match: re.Match) -> str:
                targets = [_resolve(raw_root.parent, match["command"], t.strip()) for t in match["target"].split(",")]
                names = [str(mapping[t].relative_to(output.parent)) for t in targets]
                return ",".join(names)
            def replace_package(match: re.Match) -> str:
                names = []
                for name in match["target"].split(","):
                    suffix = ".sty" if match["command"] in {"usepackage", "RequirePackage"} else ".cls"
                    local = raw_root.parent / (name.strip() + suffix)
                    names.append(str(mapping[local].relative_to(output.parent).with_suffix("")) if local in mapping else name)
                return ",".join(names)
            text = data.decode("utf-8")
            for pattern, replacement in ((DEPENDENCY, replace), (PACKAGE, replace_package)):
                for match in reversed(list(pattern.finditer(strip_comments(text)))):
                    text = text[:match.start("target")] + replacement(match) + text[match.end("target"):]
            data = text.encode("utf-8")
        payloads[destination] = data
    support.mkdir()
    for destination, data in payloads.items():
        if destination != output:
            _write_new(destination, data)
    seed_path = Path(state["work_dir"]).resolve() / "00-raw-candidate-seed.json"
    seed = {"schema_version": 1, "manifest_sha256": state["raw_checkpoint"]["manifest_sha256"],
            "output": str(output), "files": [{"path": str(p), "sha256": hashlib.sha256(d).hexdigest()}
                                              for p, d in payloads.items()]}
    discovered = set(_tree(raw_root, []))
    seed["assets"] = [str(destination) for source, destination in mapping.items() if source not in discovered]
    _write_new(seed_path, _encoded(seed))
    # The only replaced file is the explicitly reserved candidate, never its baseline.
    with output.open("r+b") as handle:
        info = os.fstat(handle.fileno())
        reservation = state["output_reservation"]
        if (info.st_dev, info.st_ino) != (reservation["dev"], reservation["ino"]):
            raise ValueError("candidate changed while starting from raw")
        handle.write(payloads[output])
        handle.truncate()
    state["raw_lineage"] = {"manifest_sha256": state["raw_checkpoint"]["manifest_sha256"],
                            "output": str(output), "seed_manifest": str(seed_path),
                            "seed_manifest_sha256": sha256_file(seed_path)}
    write_json(state_path, state)
    return state["raw_lineage"]
