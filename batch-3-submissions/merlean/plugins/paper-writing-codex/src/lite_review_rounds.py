"""Validate provenance and consistency receipts for MerLean Lite review rounds.

This module does not launch agents, authenticate identities, establish fresh model
context, assess mathematical correctness, mutate a plan, or award a research grade.
It binds self-reported review/disposition records to immutable artifact bytes and
checks the declared round-to-round lineage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from typing import Any


SCHEMA_VERSION = 1
IDENTITY_PROVENANCE = "self_reported"
VERDICTS = {"closed", "triage_required", "objections", "route_fatal"}
SEVERITIES = {"fatal", "gap", "nitpick"}
SCOPES = {"step", "representation"}
SURVIVAL_DISPOSITIONS = {"resolved", "conceded_by_exhaustion"}
RESPONSE_ACTIONS = {"revised", "rebutted", "deferred", "route_abandoned"}
_HEX = re.compile(r"[0-9a-f]{64}\Z")
_MAX_ARTIFACT_BYTES = 64 * 1024 * 1024


def sha256_file(path: str | os.PathLike[str]) -> str:
    """Return the SHA-256 digest of one ordinary file."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        while chunk := source.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _json(data: bytes, label: str) -> dict[str, Any]:
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=_object)
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as error:
        raise ValueError(f"{label} is not valid UTF-8 JSON: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a JSON object")
    return value


def _fields(
    value: object,
    required: set[str],
    optional: set[str] = frozenset(),
    *,
    label: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    missing = required - set(value)
    extra = set(value) - required - optional
    if missing or extra:
        detail = []
        if missing:
            detail.append("missing " + ", ".join(sorted(missing)))
        if extra:
            detail.append("unknown " + ", ".join(sorted(extra)))
        raise ValueError(f"{label} has invalid fields: {'; '.join(detail)}")
    return value


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value.strip()


def _identity(value: object, label: str) -> str:
    return " ".join(_text(value, label).casefold().split())


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or _HEX.fullmatch(value) is None:
        raise ValueError(f"{label} must be a lowercase SHA-256 digest")
    return value


def _relative_path(value: object, label: str) -> Path:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a relative path")
    path = Path(value)
    if (
        not value
        or path.is_absolute()
        or not path.parts
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise ValueError(f"{label} must stay below the evidence root")
    return path


def _read_below(root: Path, relative: Path, label: str) -> bytes:
    """Read a regular file descriptor-relatively without following symlinks."""
    if not hasattr(os, "O_NOFOLLOW") or os.open not in os.supports_dir_fd:
        raise ValueError("secure descriptor-relative artifact access is unavailable")
    flags = os.O_RDONLY | os.O_NOFOLLOW
    descriptor = os.open(root, flags | os.O_DIRECTORY)
    try:
        for index, part in enumerate(relative.parts):
            last = index == len(relative.parts) - 1
            next_flags = flags | (0 if last else os.O_DIRECTORY)
            if last and hasattr(os, "O_NONBLOCK"):
                next_flags |= os.O_NONBLOCK
            following = os.open(part, next_flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = following
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"{label} is not a regular file")
        if metadata.st_size > _MAX_ARTIFACT_BYTES:
            raise ValueError(f"{label} exceeds the artifact size limit")
        chunks: list[bytes] = []
        total = 0
        while chunk := os.read(descriptor, 1024 * 1024):
            total += len(chunk)
            if total > _MAX_ARTIFACT_BYTES:
                raise ValueError(f"{label} exceeds the artifact size limit")
            chunks.append(chunk)
        return b"".join(chunks)
    except OSError as error:
        raise ValueError(f"cannot safely read {label}: {error}") from error
    finally:
        os.close(descriptor)


def _artifact(root: Path, reference: object, label: str) -> tuple[Path, str, bytes]:
    reference = _fields(reference, {"path", "sha256"}, label=label)
    relative = _relative_path(reference["path"], f"{label}.path")
    expected = _digest(reference["sha256"], f"{label}.sha256")
    data = _read_below(root, relative, label)
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise ValueError(f"{label} is missing or stale: {relative}")
    return relative, expected, data


def _context_id(record: dict[str, Any], field: str, label: str) -> str | None:
    value = record.get(field)
    return _identity(value, f"{label}.{field}") if value is not None else None


def _review(
    record: dict[str, Any],
    *,
    route_id: str,
    round_number: int,
    input_hash: str,
    reviewer_id: str,
    reviewer_context_id: str | None,
) -> tuple[
    str,
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    required = {
        "schema_version", "route_id", "round", "identity_provenance",
        "input_ledger_sha256", "reviewer_id", "verdict", "first_blocker",
        "objections", "survived", "resolutions",
    }
    record = _fields(
        record,
        required,
        {"reviewer_context_id"},
        label=f"round {round_number} review",
    )
    if type(record["schema_version"]) is not int or record["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"round {round_number} review has unsupported schema")
    if _text(record["route_id"], "review.route_id") != route_id:
        raise ValueError(f"round {round_number} review route does not match manifest")
    if type(record["round"]) is not int or record["round"] != round_number:
        raise ValueError(f"round {round_number} review number does not match manifest")
    if record["identity_provenance"] != IDENTITY_PROVENANCE:
        raise ValueError("review identities must be labelled self_reported")
    if _digest(record["input_ledger_sha256"], "review.input_ledger_sha256") != input_hash:
        raise ValueError(f"round {round_number} review is bound to a stale input ledger")
    if _identity(record["reviewer_id"], "review.reviewer_id") != reviewer_id:
        raise ValueError(f"round {round_number} reviewer identity does not match manifest")
    if _context_id(record, "reviewer_context_id", "review") != reviewer_context_id:
        raise ValueError(f"round {round_number} reviewer context does not match manifest")

    verdict = record["verdict"]
    if verdict not in VERDICTS:
        raise ValueError(f"round {round_number} review has invalid verdict")
    objections = record["objections"]
    if not isinstance(objections, list):
        raise ValueError("review.objections must be a list")
    checked: list[dict[str, Any]] = []
    identifiers: set[str] = set()
    for index, objection in enumerate(objections):
        objection = _fields(
            objection,
            {"id", "step", "severity", "scope", "content", "resolve"},
            label=f"review.objections[{index}]",
        )
        identifier = _text(objection["id"], f"objection {index}.id")
        if identifier in identifiers:
            raise ValueError("objection IDs must be unique within a round")
        identifiers.add(identifier)
        _text(objection["step"], f"objection {identifier}.step")
        if objection["severity"] not in SEVERITIES:
            raise ValueError(f"objection {identifier} has invalid severity")
        if objection["scope"] not in SCOPES:
            raise ValueError(f"objection {identifier} has invalid scope")
        _text(objection["content"], f"objection {identifier}.content")
        _text(objection["resolve"], f"objection {identifier}.resolve")
        checked.append(objection)

    blockers = [one["id"] for one in checked if one["severity"] in {"fatal", "gap"}]
    first_blocker = record["first_blocker"]
    if blockers:
        if first_blocker != blockers[0]:
            raise ValueError("first_blocker must name the first fatal/gap objection")
    elif first_blocker is not None:
        raise ValueError("first_blocker must be null when no fatal/gap objection exists")

    survived = record["survived"]
    if not isinstance(survived, list):
        raise ValueError("review.survived must be a list")
    survived_ids: set[str] = set()
    checked_survivors: list[dict[str, Any]] = []
    for index, item in enumerate(survived):
        item = _fields(
            item,
            {"id", "step", "disposition", "rationale"},
            label=f"review.survived[{index}]",
        )
        identifier = _text(item["id"], f"survived {index}.id")
        step = _text(item["step"], f"survived {index}.step")
        if identifier in identifiers or identifier in survived_ids:
            raise ValueError("review finding IDs must be unique within a round")
        survived_ids.add(identifier)
        if item["disposition"] not in SURVIVAL_DISPOSITIONS:
            raise ValueError(f"survived {step} has invalid disposition")
        _text(item["rationale"], f"survived {step}.rationale")
        checked_survivors.append(item)

    resolutions = record["resolutions"]
    if not isinstance(resolutions, list):
        raise ValueError("review.resolutions must be a list")
    checked_resolutions: list[dict[str, Any]] = []
    resolution_ids: set[str] = set()
    for index, item in enumerate(resolutions):
        item = _fields(
            item,
            {"id", "step", "rationale"},
            label=f"review.resolutions[{index}]",
        )
        identifier = _text(item["id"], f"resolution {index}.id")
        _text(item["step"], f"resolution {identifier}.step")
        _text(item["rationale"], f"resolution {identifier}.rationale")
        if (
            identifier in identifiers
            or identifier in survived_ids
            or identifier in resolution_ids
        ):
            raise ValueError("review finding and resolution IDs must be unique within a round")
        resolution_ids.add(identifier)
        checked_resolutions.append(item)

    representation_fatal = any(
        one["severity"] == "fatal" and one["scope"] == "representation"
        for one in checked
    )
    if verdict == "route_fatal" and not representation_fatal:
        raise ValueError("route_fatal needs a fatal representation objection")
    return verdict, checked, checked_survivors, checked_resolutions


def _disposition(
    record: dict[str, Any],
    *,
    route_id: str,
    round_number: int,
    actor_id: str,
    actor_context_id: str | None,
    input_hash: str,
    review_hash: str,
    output_hash: str,
    verdict: str,
    objections: list[dict[str, Any]],
) -> None:
    required = {
        "schema_version", "route_id", "round", "identity_provenance", "actor_id",
        "input_ledger_sha256", "review_sha256", "output_ledger_sha256", "responses",
    }
    record = _fields(
        record,
        required,
        {"actor_context_id"},
        label=f"round {round_number} disposition",
    )
    if type(record["schema_version"]) is not int or record["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"round {round_number} disposition has unsupported schema")
    if _text(record["route_id"], "disposition.route_id") != route_id:
        raise ValueError(f"round {round_number} disposition route does not match manifest")
    if type(record["round"]) is not int or record["round"] != round_number:
        raise ValueError(f"round {round_number} disposition number does not match manifest")
    if record["identity_provenance"] != IDENTITY_PROVENANCE:
        raise ValueError("actor identities must be labelled self_reported")
    if _identity(record["actor_id"], "disposition.actor_id") != actor_id:
        raise ValueError(f"round {round_number} actor identity does not match manifest")
    if _context_id(record, "actor_context_id", "disposition") != actor_context_id:
        raise ValueError(f"round {round_number} actor context does not match manifest")
    for key, expected in (
        ("input_ledger_sha256", input_hash),
        ("review_sha256", review_hash),
        ("output_ledger_sha256", output_hash),
    ):
        if _digest(record[key], f"disposition.{key}") != expected:
            raise ValueError(f"round {round_number} disposition has stale {key}")

    responses = record["responses"]
    if not isinstance(responses, list):
        raise ValueError("disposition.responses must be a list")
    by_id = {one["id"]: one for one in objections}
    seen: set[str] = set()
    abandoned = False
    for index, response in enumerate(responses):
        response = _fields(
            response,
            {"objection_id", "action", "reason"},
            label=f"disposition.responses[{index}]",
        )
        identifier = _text(response["objection_id"], f"response {index}.objection_id")
        if identifier in seen:
            raise ValueError("each objection may be disposed only once")
        seen.add(identifier)
        if identifier not in by_id:
            raise ValueError(f"response names unknown objection: {identifier}")
        if response["action"] not in RESPONSE_ACTIONS:
            raise ValueError(f"response {identifier} has invalid action")
        if response["action"] == "route_abandoned":
            abandoned = True
            objection = by_id[identifier]
            if (
                verdict != "route_fatal"
                or objection["severity"] != "fatal"
                or objection["scope"] != "representation"
            ):
                raise ValueError(
                    "route_abandoned must answer a fatal representation objection"
                )
        _text(response["reason"], f"response {identifier}.reason")
    if seen != set(by_id):
        raise ValueError("disposition responses must cover every objection exactly once")
    if verdict == "route_fatal" and not abandoned:
        raise ValueError("route_fatal needs an explicit route_abandoned disposition")
    if input_hash == output_hash and any(
        response["action"] == "revised" for response in responses
    ):
        raise ValueError("a revised disposition must change the ledger bytes")


def validate_lite_review_rounds(
    evidence_root: str | os.PathLike[str],
    manifest: dict[str, Any] | str | os.PathLike[str],
) -> dict[str, Any]:
    """Validate one Lite route's review receipts and return a provenance summary.

    ``manifest`` may be an already-parsed object or a relative path below
    ``evidence_root``. Validation raises ``ValueError`` on malformed, stale, escaping,
    contradictory, incomplete, or discontinuous records.
    """
    try:
        root = Path(evidence_root).resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise ValueError(f"cannot resolve evidence_root safely: {error}") from error
    if not root.is_dir():
        raise ValueError("evidence_root must be a directory")
    if isinstance(manifest, dict):
        held = manifest
    else:
        relative = _relative_path(str(manifest), "manifest")
        held = _json(_read_below(root, relative, "manifest"), "manifest")
    held = _fields(
        held,
        {"schema_version", "route_id", "identity_provenance", "rounds"},
        label="manifest",
    )
    if type(held["schema_version"]) is not int or held["schema_version"] != SCHEMA_VERSION:
        raise ValueError("unsupported Lite review-round schema")
    route_id = _text(held["route_id"], "manifest.route_id")
    if held["identity_provenance"] != IDENTITY_PROVENANCE:
        raise ValueError("manifest identities must be labelled self_reported")
    rounds = held["rounds"]
    if not isinstance(rounds, list) or not rounds:
        raise ValueError("manifest.rounds must be a nonempty list")

    previous_output: str | None = None
    declared_reviewer_contexts: list[str] = []
    pending: dict[str, dict[str, str]] = {}
    last_verdict = ""
    final_hash = ""
    for expected_round, item in enumerate(rounds, 1):
        item = _fields(
            item,
            {
                "round", "actor_id", "reviewer_id", "input_ledger", "review",
                "disposition", "output_ledger",
            },
            {"actor_context_id", "reviewer_context_id"},
            label=f"manifest.rounds[{expected_round - 1}]",
        )
        if type(item["round"]) is not int or item["round"] != expected_round:
            raise ValueError("review rounds must be consecutive and start at one")
        actor_id = _identity(item["actor_id"], f"round {expected_round}.actor_id")
        reviewer_id = _identity(item["reviewer_id"], f"round {expected_round}.reviewer_id")
        if actor_id == reviewer_id:
            raise ValueError("actor and reviewer identities must differ")
        actor_context = _context_id(item, "actor_context_id", f"round {expected_round}")
        reviewer_context = _context_id(item, "reviewer_context_id", f"round {expected_round}")
        if actor_context is not None and reviewer_context == actor_context:
            raise ValueError("actor and reviewer context IDs must differ")
        if reviewer_context is not None:
            declared_reviewer_contexts.append(reviewer_context)

        _, input_hash, _ = _artifact(root, item["input_ledger"], f"round {expected_round} input ledger")
        _, output_hash, _ = _artifact(root, item["output_ledger"], f"round {expected_round} output ledger")
        if previous_output is not None and input_hash != previous_output:
            raise ValueError("round input does not continue from the preceding output ledger")
        _, review_hash, review_data = _artifact(root, item["review"], f"round {expected_round} review")
        review = _json(review_data, f"round {expected_round} review")
        verdict, objections, survivors, resolutions = _review(
            review,
            route_id=route_id,
            round_number=expected_round,
            input_hash=input_hash,
            reviewer_id=reviewer_id,
            reviewer_context_id=reviewer_context,
        )
        for resolution in resolutions:
            identifier = resolution["id"]
            finding = pending.get(identifier)
            if finding is None:
                raise ValueError(
                    f"round {expected_round} resolves unknown prior finding {identifier}"
                )
            if resolution["step"].strip() != finding["step"]:
                raise ValueError(
                    f"round {expected_round} resolution changes the step for {identifier}"
                )
            del pending[identifier]

        current_findings = [
            {
                "id": objection["id"],
                "step": objection["step"].strip(),
                "kind": "blocker",
                "severity": objection["severity"],
            }
            for objection in objections
            if objection["severity"] in {"fatal", "gap"}
        ]
        current_findings.extend(
            {
                "id": survivor["id"],
                "step": survivor["step"].strip(),
                "kind": "conceded_by_exhaustion",
                "severity": "",
            }
            for survivor in survivors
            if survivor["disposition"] == "conceded_by_exhaustion"
        )
        for finding in current_findings:
            existing = pending.get(finding["id"])
            if existing is not None and (
                existing["step"] != finding["step"]
                or existing["kind"] != finding["kind"]
            ):
                raise ValueError(
                    f"round {expected_round} reuses finding ID {finding['id']} inconsistently"
                )
            pending[finding["id"]] = finding

        pending_blockers = [
            finding for finding in pending.values() if finding["kind"] == "blocker"
        ]
        pending_conceded = [
            finding
            for finding in pending.values()
            if finding["kind"] == "conceded_by_exhaustion"
        ]
        representation_fatal = any(
            objection["severity"] == "fatal"
            and objection["scope"] == "representation"
            for objection in objections
        )
        if verdict == "closed" and (pending_blockers or pending_conceded):
            raise ValueError(
                "closed contradicts unresolved fatal/gap or conceded-by-exhaustion findings"
            )
        if verdict == "triage_required" and (
            pending_blockers or not pending_conceded
        ):
            raise ValueError(
                "triage_required needs no unresolved fatal/gap and a conceded-by-exhaustion finding"
            )
        if verdict == "objections" and (
            not pending_blockers or representation_fatal
        ):
            raise ValueError(
                "objections needs unresolved fatal/gap findings but no representation-fatal claim"
            )
        _, _, disposition_data = _artifact(
            root, item["disposition"], f"round {expected_round} disposition"
        )
        disposition = _json(disposition_data, f"round {expected_round} disposition")
        _disposition(
            disposition,
            route_id=route_id,
            round_number=expected_round,
            actor_id=actor_id,
            actor_context_id=actor_context,
            input_hash=input_hash,
            review_hash=review_hash,
            output_hash=output_hash,
            verdict=verdict,
            objections=objections,
        )
        previous_output = output_hash
        final_hash = output_hash
        last_verdict = verdict
        if verdict == "route_fatal" and expected_round != len(rounds):
            raise ValueError(
                "route_fatal with route_abandoned is terminal for this route manifest"
            )

    return {
        "schema_version": SCHEMA_VERSION,
        "route_id": route_id,
        "rounds": len(rounds),
        "final_ledger_sha256": final_hash,
        "final_verdict": last_verdict,
        "triage_required": any(
            finding["kind"] == "conceded_by_exhaustion"
            for finding in pending.values()
        ),
        "closure_claimed": last_verdict == "closed",
        "route_terminal": last_verdict == "route_fatal",
        "outstanding_findings": [pending[key] for key in sorted(pending)],
        "identity_provenance": IDENTITY_PROVENANCE,
        "declared_reviewer_contexts_unique": len(declared_reviewer_contexts)
        == len(set(declared_reviewer_contexts)),
        "freshness_verified": False,
        "advisory": True,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate MerLean Lite review receipts without dispatching or grading."
    )
    parser.add_argument("evidence_root")
    parser.add_argument("manifest", help="relative manifest path below evidence_root")
    args = parser.parse_args(argv)
    try:
        result = validate_lite_review_rounds(args.evidence_root, args.manifest)
    except (OSError, ValueError, TypeError, KeyError, RuntimeError, RecursionError) as error:
        print(f"lite review receipts: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
