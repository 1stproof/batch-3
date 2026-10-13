"""Advisory research execution history; never assigns proof status or grades.

Callers must hold the plan lock for the lifetime of this object and its operations.
Evidence hashes establish byte identity, not truth or independent verification.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .offline_store import OfflinePlanGraph, _atomic_json, _is_meta
from .grade_policy import GOLD_INVALIDATING_FIELDS

OUTCOMES = frozenset({
    "progress", "interface_checkpoint", "evidence_checkpoint", "proof_failure",
    "counterexample_candidate", "interface_mismatch", "verification_failure",
    "integration_failure", "infrastructure_failure", "budget_exhausted",
})
SEMANTIC_FIELDS = sorted(GOLD_INVALIDATING_FIELDS - {
    "status", "proof_status", "question_status", "research_value",
})
_RECORD = {"expected_fingerprint", "outcome", "evidence", "note", "next_action"}
_PROPOSAL = {"expected_fingerprint", "checkpoint_id", "change", "reason", "consumer_impact"}
_HEX = re.compile(r"[0-9a-f]{64}\Z")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def _digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value


def _payload(value, allowed, required):
    if not isinstance(value, dict) or set(value) - allowed or required - set(value):
        raise ValueError("invalid payload fields")
    for key in set(value) - {"evidence"}:
        _text(value[key], key)
    if not _HEX.fullmatch(value["expected_fingerprint"]):
        raise ValueError("invalid expected_fingerprint")


class ResearchCheckpoints:
    """Append-only operational records in a sidecar, independent of graph grading."""

    def __init__(self, graph: OfflinePlanGraph, evidence_root: Path | None = None):
        self.graph = graph
        self.evidence_root = Path(evidence_root).resolve(strict=True) if evidence_root is not None else None
        if self.evidence_root is not None and not self.evidence_root.is_dir():
            raise ValueError("evidence_root must be a directory")
        self.path = graph.data_dir / ".merlean-research-checkpoints.json"
        self._store = {"version": 2, "evidence_root": None, "records": [], "proposals": []}
        if self.path.is_symlink():
            raise ValueError("checkpoint store cannot be a symlink")
        if self.path.exists():
            try:
                self._store = json.loads(self.path.read_text(), object_pairs_hook=_unique_object)
                self._validate_store()
            except (OSError, ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"malformed checkpoint store: {exc}") from exc

    def _validate_store(self):
        s = self._store
        if not isinstance(s, dict) or set(s) != {"version", "evidence_root", "records", "proposals"}:
            raise ValueError("invalid store shape")
        if type(s["version"]) is not int or s["version"] != 2:
            raise ValueError("unsupported store version")
        if not isinstance(s["evidence_root"], str) or not Path(s["evidence_root"]).is_absolute():
            raise ValueError("invalid bound evidence root")
        seen = set()
        prior = {}
        for kind, allowed, required in (
            ("records", _RECORD, {"expected_fingerprint", "outcome", "evidence"}),
            ("proposals", _PROPOSAL, _PROPOSAL),
        ):
            if not isinstance(s[kind], list):
                raise ValueError("history must be a list")
            for entry in s[kind]:
                if not isinstance(entry, dict) or set(entry) != ({"id", "sid", "created_at", "payload", "dependency_checkpoints", "target_snapshot"} if kind == "records" else {"id", "sid", "created_at", "payload"}):
                    raise ValueError("invalid history entry")
                for key in ("id", "sid", "created_at"):
                    _text(entry[key], key)
                if entry["id"] in seen:
                    raise ValueError("duplicate history id")
                seen.add(entry["id"])
                _payload(entry["payload"], allowed, required)
                if kind == "records":
                    if entry["payload"]["outcome"] not in OUTCOMES:
                        raise ValueError("invalid outcome")
                    self._evidence_shape(entry["payload"]["evidence"])
                    snapshot = entry["target_snapshot"]
                    if not isinstance(snapshot, dict) or set(snapshot) != {
                        "sid", "nodes", "missing", "cycles", "fingerprint", "valid"
                    }:
                        raise ValueError("invalid historical target snapshot")
                    binding = {k: snapshot[k] for k in ("sid", "nodes", "missing", "cycles")}
                    if (snapshot["sid"] != entry["sid"] or snapshot["valid"] is not True
                            or snapshot["missing"] != [] or snapshot["cycles"] != []
                            or not isinstance(snapshot["nodes"], dict)
                            or entry["sid"] not in snapshot["nodes"]
                            or _digest(binding) != snapshot["fingerprint"]
                            or snapshot["fingerprint"] != entry["payload"]["expected_fingerprint"]):
                        raise ValueError("historical target snapshot binding mismatch")
                    bindings = entry["dependency_checkpoints"]
                    if not isinstance(bindings, dict):
                        raise ValueError("invalid dependency checkpoint bindings")
                    for dep, event_id in bindings.items():
                        linked = prior.get(event_id) if isinstance(event_id, str) else None
                        if not linked or linked["sid"] != dep or linked["payload"]["outcome"] != "evidence_checkpoint":
                            raise ValueError("dependency binding must reference earlier evidence checkpoint")
                    prior[entry["id"]] = entry
        records = {e["id"]: e for e in s["records"]}
        for p in s["proposals"]:
            linked = records.get(p["payload"]["checkpoint_id"])
            if not linked or linked["sid"] != p["sid"] or linked["payload"]["expected_fingerprint"] != p["payload"]["expected_fingerprint"]:
                raise ValueError("invalid proposal checkpoint binding")

    def snapshot(self, sid: str) -> dict:
        """Bind declared plan semantics only, not implicit Lean imports or file bytes."""
        _text(sid, "sid")
        nodes, missing, cycles, visiting = {}, set(), [], []

        def visit(key):
            if key in visiting:
                cycles.append(visiting[visiting.index(key):] + [key])
                return
            if key in nodes or key in missing:
                return
            node = self.graph.get(key)
            if node is None:
                missing.add(key)
                return
            if _is_meta(node):
                missing.add(key)  # Notes cannot discharge formal dependencies.
                return
            deps = node.get("dependencies") or []
            if not isinstance(deps, list) or any(not isinstance(d, str) or not d for d in deps):
                raise ValueError(f"invalid dependencies for {key}")
            nodes[key] = {f: node.get(f) for f in SEMANTIC_FIELDS}
            nodes[key]["dependencies"] = sorted(set(deps))
            visiting.append(key)
            for dep in sorted(set(deps)):
                visit(dep)
            visiting.pop()

        visit(sid)
        binding = {"sid": sid, "nodes": nodes, "missing": sorted(missing), "cycles": cycles}
        return {**binding, "fingerprint": _digest(binding), "valid": not missing and not cycles}

    @staticmethod
    def _evidence_shape(evidence):
        if not isinstance(evidence, list) or not evidence:
            raise ValueError("nonempty evidence list required")
        for item in evidence:
            if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
                raise ValueError("invalid evidence reference")
            path = _text(item["path"], "evidence path")
            if Path(path).is_absolute() or ".." in Path(path).parts or not Path(path).parts:
                raise ValueError("evidence must use relative in-root paths")
            if not isinstance(item["sha256"], str) or not _HEX.fullmatch(item["sha256"]):
                raise ValueError("invalid evidence hash")

    def _require_root(self):
        if self.evidence_root is None:
            raise ValueError("evidence_root required for evidence-consuming operations")
        bound = self._store["evidence_root"]
        if bound is not None and bound != str(self.evidence_root):
            raise ValueError("evidence_root does not match bound store root")
        if not hasattr(os, "O_NOFOLLOW") or os.open not in os.supports_dir_fd:
            raise ValueError("secure nofollow descriptor-relative evidence access unavailable")

    def _evidence_digest(self, relative):
        # Traverse from /, including the bound root, without following symlinks.
        flags = os.O_RDONLY | os.O_NOFOLLOW
        fd = os.open("/", flags | os.O_DIRECTORY)
        try:
            parts = [*self.evidence_root.parts[1:], *Path(relative).parts]
            for index, part in enumerate(parts):
                next_fd = os.open(part, flags | (os.O_DIRECTORY if index < len(parts) - 1
                                                 else os.O_NONBLOCK), dir_fd=fd)
                os.close(fd)
                fd = next_fd
            if not stat.S_ISREG(os.fstat(fd).st_mode):
                raise ValueError("evidence is not a regular file")
            digest = hashlib.sha256()
            while chunk := os.read(fd, 1024 * 1024):
                digest.update(chunk)
            return digest.hexdigest()
        finally:
            os.close(fd)

    def _check_evidence(self, evidence):
        self._require_root()
        self._evidence_shape(evidence)
        errors = []
        for item in evidence:
            try:
                if self._evidence_digest(item["path"]) != item["sha256"]:
                    raise ValueError("evidence hash mismatch")
            except (OSError, ValueError) as exc:
                errors.append({"path": item["path"], "error": str(exc)})
        return errors

    def _current(self, sid, expected):
        snap = self.snapshot(sid)
        if not snap["valid"]:
            raise ValueError("target has missing dependencies or cycles")
        if expected != snap["fingerprint"]:
            raise ValueError("stale target fingerprint")
        return snap

    def _append(self, kind, sid, payload, bindings=None):
        entry = {"id": uuid.uuid4().hex, "sid": sid,
                 "created_at": datetime.now(timezone.utc).isoformat(),
                 "payload": json.loads(json.dumps(payload, allow_nan=False))}
        if kind == "records":
            entry["dependency_checkpoints"] = bindings or {}
            # Preserve readable historical claims/premises; artifact bytes remain external.
            entry["target_snapshot"] = json.loads(json.dumps(
                self._current(sid, payload["expected_fingerprint"]), allow_nan=False))
        updated = {**self._store, "evidence_root": str(self.evidence_root), kind: [*self._store[kind], entry]}
        _atomic_json(self.path, updated)
        self._store = updated
        return json.loads(json.dumps(entry))

    def record(self, sid: str, payload: dict) -> dict:
        _payload(payload, _RECORD, {"expected_fingerprint", "outcome", "evidence"})
        if payload["outcome"] not in OUTCOMES:
            raise ValueError("invalid checkpoint outcome")
        self._current(sid, payload["expected_fingerprint"])
        errors = self._check_evidence(payload["evidence"])
        if errors:
            raise ValueError(f"invalid checkpoint evidence: {errors}")
        latest = {e["sid"]: e for e in self.inspect() if e["kind"] == "checkpoint"
                  and e["current"] and e["payload"]["outcome"] == "evidence_checkpoint"}
        deps = self.graph.get(sid).get("dependencies") or []
        if payload["outcome"] == "evidence_checkpoint":
            if any(dep not in latest for dep in deps):
                raise ValueError("evidence checkpoint requires current dependency evidence checkpoints")
            lean_path = self.graph.get(sid).get("lean_path")
            if lean_path:
                self._evidence_shape([{"path": lean_path, "sha256": "0" * 64}])
                if str(Path(lean_path)) not in {str(Path(e["path"])) for e in payload["evidence"]}:
                    raise ValueError("evidence checkpoint must include declared lean_path")
                self._evidence_digest(lean_path)
        bindings = {dep: latest[dep]["id"] for dep in deps if dep in latest}
        return self._append("records", sid, payload, bindings)

    def inspect(self, sid=None) -> list:
        """History plus current applicability; never relabels evidence as a proof."""
        self._require_root()
        result = []
        current = {}
        for entry in self._store["records"]:
            snap = self.snapshot(entry["sid"])
            errors = self._check_evidence(entry["payload"]["evidence"])
            stale = not snap["valid"] or snap["fingerprint"] != entry["payload"]["expected_fingerprint"]
            deps = set((self.graph.get(entry["sid"]) or {}).get("dependencies") or [])
            bindings = entry["dependency_checkpoints"]
            binding_mismatch = (not set(bindings).issubset(deps) or
                                (entry["payload"]["outcome"] == "evidence_checkpoint" and set(bindings) != deps))
            dependency_stale = binding_mismatch or any(not current.get(event_id, False)
                                   for event_id in entry["dependency_checkpoints"].values())
            valid = not stale and not errors and not dependency_stale
            current[entry["id"]] = valid
            result.append({**entry, "kind": "checkpoint", "stale": stale,
                           "evidence_errors": errors, "applicable": valid, "current": valid,
                           "stale_reasons": (["target_changed_or_invalid"] if stale else []) +
                           (["evidence_invalid"] if errors else []) +
                           (["dependency_evidence_invalid"] if dependency_stale else [])})
        for entry in self._store["proposals"]:
            if sid is not None and entry["sid"] != sid:
                continue
            result.append({**entry, "kind": "revision_proposal", "applied": False,
                           "applicable": current.get(entry["payload"]["checkpoint_id"], False),
                           "current": current.get(entry["payload"]["checkpoint_id"], False),
                           "stale_reasons": ([] if current.get(entry["payload"]["checkpoint_id"], False)
                                             else ["linked_checkpoint_not_current"])})
        return json.loads(json.dumps([e for e in result if sid is None or e["sid"] == sid]))

    def propose_revision(self, sid: str, payload: dict) -> dict:
        _payload(payload, _PROPOSAL, _PROPOSAL)
        self._current(sid, payload["expected_fingerprint"])
        linked = next((e for e in self.inspect(sid) if e["id"] == payload["checkpoint_id"]
                       and e["kind"] == "checkpoint"), None)
        if linked is None or not linked["applicable"]:
            raise ValueError("proposal needs a current same-node evidence-bound checkpoint")
        return self._append("proposals", sid, payload)

    def ready(self, roots: list, mode="interface") -> dict:
        """Advisory only: interfaces or current recorded evidence, never grades."""
        if mode not in {"interface", "evidence"}:
            raise ValueError("mode must be interface or evidence")
        if not isinstance(roots, list) or not roots or any(not isinstance(r, str) or not r for r in roots):
            raise ValueError("nonempty roots list required")
        closures = {r: self.snapshot(r) for r in sorted(set(roots))}
        selected = sorted({sid for s in closures.values() for sid in s["nodes"]})
        latest = {}
        for event in self.inspect():
            if (event["kind"] == "checkpoint" and event["applicable"]
                    and event["payload"]["outcome"] == "evidence_checkpoint"):
                latest[event["sid"]] = event
        candidates, blocked = [], []
        for sid in selected:
            node = self.graph.get(sid)
            reasons = []
            snap = self.snapshot(sid)
            if not snap["valid"]:
                reasons.append("missing_dependencies_or_cycle")
            for key in sorted(set(snap["nodes"]) | set(snap["missing"])):
                dep = self.graph.get(key)
                if dep is None or _is_meta(dep):
                    reasons.append(f"missing_formal_dependency:{key}")
                elif dep.get("status") in {"failed", "completed_axiom"}:
                    reasons.append(f"{dep['status']}:{key}")
                elif key in (node.get("dependencies") or []):
                    if mode == "interface":
                        if not isinstance(dep.get("anchor"), str) or not dep["anchor"].strip():
                            reasons.append(f"missing_interface:{key}")
                    elif latest.get(key, {}).get("payload", {}).get("outcome") != "evidence_checkpoint":
                        reasons.append(f"missing_current_evidence_checkpoint:{key}")
            item = {"sid": sid, "consumer_roots": [r for r, s in closures.items() if sid in s["nodes"]],
                    "fingerprint": snap["fingerprint"], "blockers": sorted(set(reasons))}
            if reasons:
                blocked.append(item)
            elif node.get("status") != "completed":
                candidates.append(item)
        return {"advisory": True, "mode": mode, "ready": [x["sid"] for x in candidates],
                "blocked": {x["sid"]: x["blockers"] for x in blocked},
                "details": {x["sid"]: x for x in [*candidates, *blocked]},
                "root_errors": {r: {"missing": s["missing"], "cycles": s["cycles"]}
                                for r, s in closures.items() if not s["valid"]}}
