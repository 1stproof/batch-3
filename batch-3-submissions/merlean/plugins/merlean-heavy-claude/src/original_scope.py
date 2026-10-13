"""Original-question completion gate, independent of the selected theorem's grade.

This validates pinned evidence and review structure, not mathematical truth or reviewer
identity authentication. Both Lite and Heavy must use it before claiming the original
question complete. A correct finite counterexample is an admissible answer.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

_HASH = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
FULL_FIELDS = {"original_problem_completed", "submission_eligible"}


def claims_original_completion(data: Mapping[str, Any]) -> bool:
    return (data.get("question_status") == "settled"
            or data.get("claim_scope") in {"full_original", "original_problem"}
            or any(data.get(key) is True for key in FULL_FIELDS))


def _text(value: Any) -> bool:
    return isinstance(value, str) and len(value.strip()) >= 12


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _identity(value: Any) -> str:
    return " ".join(value.casefold().split()) if isinstance(value, str) else ""


def _read(ref: Any, base: Path | None, label: str, errors: list[str], *, json_file=False):
    if (not isinstance(ref, dict) or not isinstance(ref.get("path"), str)
            or not isinstance(ref.get("sha256"), str) or not _HASH.fullmatch(ref["sha256"])
            or base is None):
        errors.append(f"ORIGINAL_SCOPE_EVIDENCE: {label} needs a path and sha256")
        return None, None
    try:
        root = base.resolve()
        path = (root / ref["path"]).resolve()
        path.relative_to(root)
        payload = path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != ref["sha256"]:
            raise ValueError("stale hash")
        value = json.loads(payload) if json_file else payload.decode()
        if json_file and not isinstance(value, dict):
            raise ValueError("expected JSON object")
        return value, path
    except (OSError, ValueError, UnicodeError) as exc:
        errors.append(f"ORIGINAL_SCOPE_EVIDENCE: {label}: {exc}")
        return None, None


def _declaration_signature(payload: str, name: str) -> str | None:
    """Find an actual theorem header, excluding nested comments and string literals.

    Complex headers containing an internal := require a separate bridge interface;
    unsupported syntax fails closed instead of trusting text inside documentation.
    """
    from research_grade import _strip_lean_comments
    clean = _strip_lean_comments(payload)
    masked = list(clean)
    quoted = escaped = False
    for i, char in enumerate(clean):
        if quoted:
            if char != "\n":
                masked[i] = " "
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
            masked[i] = " "
    masked_text = "".join(masked)
    pattern = r"(?m)^\s*(?:(?:theorem|lemma)\s+([\w'.]+)|(?P<example>example)(?=\s|:))(?=\s|[:({\[])([\s\S]*?)\s*:="
    for found in re.finditer(pattern, masked_text):
        declaration = found.group(1) or "example"
        stack = []
        for command in re.finditer(r"(?m)^\s*(namespace\s+([\w'.]+)|section(?:\s+[\w'.]+)?|end(?:\s+[\w'.]+)?)\s*$", masked_text[:found.start()]):
            token = command.group(1)
            if token.startswith("namespace "):
                stack.append(command.group(2))
            elif token.startswith("section"):
                stack.append(None)
            elif stack:
                stack.pop()
        full = ".".join([part for part in stack if part] + [declaration])
        if declaration.startswith("_root_."):
            full = declaration[len("_root_."):]
        if name == full:
            return clean[found.start():found.end()-2].strip()
    return None



def _audit_original_scope(data: Mapping[str, Any], base: Path | None, *, required=False, require_final_answer=False) -> list[str]:
    """Check immutable original source, complete clause census and independent review."""
    if not required and not require_final_answer and not claims_original_completion(data):
        return []
    errors: list[str] = []
    original, opath = _read(data.get("original_problem"), base, "original_problem", errors, json_file=True)
    report, rpath = _read(data.get("original_scope_audit"), base, "original_scope_audit", errors, json_file=True)
    target, _ = _read(data.get("target_contract"), base, "target_contract", errors, json_file=True)
    if original is None or report is None or target is None:
        return errors
    author = _identity(data.get("manifest_author"))
    reviewer = _identity(report.get("reviewer"))
    implementers = data.get("implementers")
    if (not isinstance(implementers, list) or not implementers
            or any(not _identity(person) for person in implementers)):
        errors.append("ORIGINAL_SCOPE_INDEPENDENCE: complete implementers census required")
        implementers = []
    identities = {_identity(person) for person in implementers}
    if (report.get("implementers") != implementers or len(identities) != len(implementers)):
        errors.append("ORIGINAL_SCOPE_INDEPENDENCE: review must bind the complete unique implementers census")
    if not author or not reviewer or reviewer in identities | {author}:
        errors.append("ORIGINAL_SCOPE_INDEPENDENCE: reviewer must differ from submitter and every implementer")
    if _identity(report.get("implementer")) not in identities:
        errors.append("ORIGINAL_SCOPE_INDEPENDENCE: report implementer absent from manifest census")
    provenance, _ = _read(report.get("reviewer_provenance"), rpath.parent, "reviewer dispatch provenance", errors, json_file=True)
    provider = data.get("provider")
    if (provider not in {"codex", "claude"} or provenance is None
            or provenance.get("provider") != provider
            or _identity(provenance.get("reviewer")) != reviewer
            or not _nonempty(provenance.get("task_id"))
            or provenance.get("role") != "original_scope_review"):
        errors.append("ORIGINAL_SCOPE_REVIEWER_MODEL: matching provider/task dispatch provenance required")
    elif provider == "codex" and (provenance.get("model_family") != "astra" or provenance.get("model") != "gpt-6-astra"):
        errors.append("ORIGINAL_SCOPE_REVIEWER_MODEL: Codex original-target review requires gpt-6-astra")
    elif provider == "claude" and (provenance.get("model_family") != "fable" or not _nonempty(provenance.get("model"))
                                  or any(x in provenance["model"].lower() for x in ("opus", "sonnet", "haiku"))):
        errors.append("ORIGINAL_SCOPE_REVIEWER_MODEL: Claude original-target review requires host-resolved Fable")
    if report.get("verdict") != "PASS_FULL_SCOPE":
        errors.append("ORIGINAL_SCOPE_NOT_PASSED: failed, missing or uncertain verdict")
    for name in ("original_problem", "target_contract"):
        if report.get(name + "_sha256") != data[name]["sha256"]:
            errors.append(f"ORIGINAL_SCOPE_STALE: {name} binding differs")
    if data.get("proof_commit") is not None and (
            not isinstance(data["proof_commit"], str) or not _COMMIT.fullmatch(data["proof_commit"])
            or report.get("proof_commit") != data["proof_commit"]):
        errors.append("ORIGINAL_SCOPE_STALE: supplied proof commit does not match review")
    if report.get("extra_assumptions") != [] or report.get("gaps") != []:
        errors.append("ORIGINAL_SCOPE_INCOMPLETE: extra premises or unresolved gaps block original completion")
    if report.get("answer_kind") not in {"proof", "counterexample"}:
        errors.append("ORIGINAL_SCOPE_INVALID: answer_kind must be proof or counterexample")

    input_kind = original.get("input_kind")
    if input_kind not in {"natural_language", "lean", "mixed"}:
        errors.append("ORIGINAL_SCOPE_SOURCE: input_kind must be natural_language, lean or mixed")
    if original.get("unresolved_conflicts") != []:
        errors.append("ORIGINAL_SCOPE_CONFLICT: conflicting original sources must be resolved")
    source = original.get("source")
    source_text, source_path = _read(source, opath.parent, "original source", errors)
    origin = original.get("origin")
    kind = original.get("source_kind")
    if (kind not in {"user_request", "official_catalog", "original_publication", "official_lean"}
            or not isinstance(origin, str)
            or not (origin.startswith("https://") or (kind == "user_request" and origin.startswith("user-request:")))):
        errors.append("ORIGINAL_SCOPE_SOURCE: independent original provenance required; a local Challenge is not a source")
    if (not _nonempty(original.get("statement")) or source_text is None
            or original["statement"] not in source_text):
        errors.append("ORIGINAL_SCOPE_SOURCE: complete original statement must be present in frozen source")
    mixed_text = None
    if input_kind == "mixed":
        natural = original.get("natural_language")
        if not isinstance(natural, dict):
            errors.append("ORIGINAL_SCOPE_MIXED: independently frozen natural-language input required")
        else:
            mixed_text, _ = _read(natural.get("source"), opath.parent, "mixed natural-language source", errors)
            if (not _nonempty(natural.get("statement")) or mixed_text is None
                    or natural["statement"] not in mixed_text):
                errors.append("ORIGINAL_SCOPE_MIXED: original natural-language statement is not source-bound")
    clause_sources = (source_text or "") + "\n" + (mixed_text or "")
    clauses = original.get("required_clauses")
    clause_ids: set[str] = set()
    if not isinstance(clauses, list) or not clauses:
        errors.append("ORIGINAL_SCOPE_CENSUS: nonempty original required_clauses required")
    else:
        for clause in clauses:
            if (not isinstance(clause, dict) or not isinstance(clause.get("id"), str)
                    or not clause["id"].strip() or clause["id"] in clause_ids
                    or not _nonempty(clause.get("text")) or not _nonempty(clause.get("source_excerpt"))
                    or clause["source_excerpt"] not in clause_sources):
                errors.append("ORIGINAL_SCOPE_CENSUS: invalid, duplicate or source-unbound original clause")
            else:
                clause_ids.add(clause["id"])

    candidate_kind = data.get("candidate_kind", "lean")
    if candidate_kind not in {"lean", "natural_language"}:
        errors.append("ORIGINAL_SCOPE_CANDIDATE: candidate_kind must be lean or natural_language")
    if report.get("candidate_kind", "lean") != candidate_kind:
        errors.append("ORIGINAL_SCOPE_CANDIDATE: report candidate_kind differs")
    natural_candidate = candidate_kind == "natural_language"
    if natural_candidate and (input_kind != "natural_language" or data.get("grade") not in {"BRONZE", "SILVER"}):
        errors.append("ORIGINAL_SCOPE_CANDIDATE: natural-language answers require a natural-language original and BRONZE/SILVER; no formal certification")
    final_answer = None
    if natural_candidate or require_final_answer or "final_answer" in data or "final_answer_sha256" in report:
        final_answer, _ = _read(data.get("final_answer"), base, "final answer", errors)
        if not _nonempty(final_answer):
            errors.append("ORIGINAL_SCOPE_FINAL_ANSWER: nonempty frozen final answer required")
        ref = data.get("final_answer")
        if (not isinstance(ref, dict) or report.get("final_answer_sha256") != ref.get("sha256")
                or not _HASH.fullmatch(str(report.get("final_answer_sha256", "")))):
            errors.append("ORIGINAL_SCOPE_FINAL_ANSWER: review must bind the exact final answer hash")

    roots = report.get("roots")
    root_names: set[str] = set()
    matched_target = False
    if not isinstance(roots, list) or not roots:
        errors.append("ORIGINAL_SCOPE_INTERFACE: exact main theorem roots required")
    elif natural_candidate:
        for root in roots:
            if not isinstance(root, dict):
                errors.append("ORIGINAL_SCOPE_INTERFACE: malformed natural-language root")
                continue
            name, statement = root.get("name"), root.get("statement")
            if not _nonempty(name) or name in root_names or not _text(statement):
                errors.append("ORIGINAL_SCOPE_INTERFACE: invalid/duplicate natural-language root")
                continue
            root_names.add(name)
            passage = root.get("answer_passage")
            if not isinstance(passage, dict):
                errors.append("ORIGINAL_SCOPE_PASSAGE: exact final-answer passage required")
                continue
            start, end, text = passage.get("start"), passage.get("end"), passage.get("text")
            if (type(start) is not int or type(end) is not int or final_answer is None
                    or not (0 <= start < end <= len(final_answer))
                    or text != statement or final_answer[start:end] != text):
                errors.append("ORIGINAL_SCOPE_PASSAGE: root statement must equal the exact final-answer character slice")
            matched_target |= statement == target.get("target_statement")
    else:
        # Reuse the maintained Lean lexer; never trust declarations hidden in comments.
        from research_grade import _strip_lean_comments
        for root in roots:
            if not isinstance(root, dict):
                errors.append("ORIGINAL_SCOPE_INTERFACE: malformed root")
                continue
            name, signature = root.get("name"), root.get("signature")
            payload, file = _read(root.get("lean_file"), rpath.parent, "root Lean file", errors)
            valid = isinstance(name, str) and bool(re.fullmatch(r"[\w'.]+", name)) and _text(signature)
            if (not valid or name in root_names or payload is None
                    or source_path == file):
                errors.append("ORIGINAL_SCOPE_INTERFACE: invalid/duplicate root or selected theorem used as original source")
                continue
            root_names.add(name)
            clean = _strip_lean_comments(payload)
            compact = lambda s: s.strip()
            # The interface must start at a real declaration and end at its proof separator.
            declaration = _declaration_signature(payload, name)
            if (declaration is None or compact(declaration) != compact(signature)
                    or root.get("signature_sha256") != hashlib.sha256(signature.encode()).hexdigest()):
                errors.append("ORIGINAL_SCOPE_INTERFACE: main signature is not the pinned source declaration")
            matched_target |= signature == target.get("target_signature")
            definitions = root.get("definitions")
            if not isinstance(definitions, list):
                errors.append("ORIGINAL_SCOPE_DEFINITIONS: explicit necessary-definition census required (possibly empty)")
            else:
                for definition in definitions:
                    if not isinstance(definition, dict):
                        errors.append("ORIGINAL_SCOPE_DEFINITIONS: malformed definition")
                        continue
                    text, _ = _read(definition.get("source"), rpath.parent, "definition source", errors)
                    if (not isinstance(definition.get("name"), str) or not _text(definition.get("statement"))
                            or text is None or definition["statement"] not in _strip_lean_comments(text)):
                        errors.append("ORIGINAL_SCOPE_DEFINITIONS: source-bound definition text required")
    if isinstance(roots, list):
        snapshot = hashlib.sha256(json.dumps(roots, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if report.get("proof_snapshot_sha256") != snapshot:
            errors.append("ORIGINAL_SCOPE_STALE: main interfaces/definition snapshot differs")
    if input_kind in {"lean", "mixed"}:
        _check_lean_original(original, report, target, opath.parent, rpath.parent, root_names, errors)
    if not matched_target:
        errors.append("ORIGINAL_SCOPE_TARGET: review roots do not include the exact selected target interface")
    findings = report.get("findings")
    required_findings = {"source_fidelity", "clause_completeness", "definitions", "premises", "answer_direction"}
    if input_kind == "mixed":
        required_findings.add("mixed_consistency")
    if (not isinstance(findings, dict) or set(findings) != required_findings
            or any(not _text(findings.get(key)) for key in required_findings)):
        errors.append("ORIGINAL_SCOPE_FINDINGS: substantive source/interface comparison findings required")
    covered: set[str] = set()
    coverage = report.get("coverage")
    if not isinstance(coverage, list):
        errors.append("ORIGINAL_SCOPE_COVERAGE: coverage list required")
    else:
        for item in coverage:
            if (not isinstance(item, dict) or not isinstance(item.get("clause_id"), str)
                    or item["clause_id"] in covered or item["clause_id"] not in clause_ids
                    or item.get("root") not in root_names or item.get("result") != "covered"
                    or not _text(item.get("explanation"))):
                errors.append("ORIGINAL_SCOPE_COVERAGE: missing, duplicate or unproved original clause")
            else:
                covered.add(item["clause_id"])
    if data.get("grade") == "GOLD" and isinstance(roots, list):
        kernel, kpath = _read(data.get("kernel_evidence"), base, "Gold kernel roots", errors, json_file=True)
        faces = data.get("theorem_faces", [])
        face_roots = {f.get("lean_decl") for f in faces if isinstance(f, dict) and f.get("covered") is True}
        kernel_roots = kernel.get("root_declarations", []) if isinstance(kernel, dict) else []
        for root in roots:
            if not isinstance(root, dict):
                continue
            matches = [k for k in kernel_roots if isinstance(k, dict) and k.get("name") == root.get("name")]
            if (len(matches) != 1 or root.get("name") not in face_roots
                    or matches[0].get("signature") != root.get("signature")
                    or matches[0].get("signature_hash") != root.get("signature_sha256")
                    or matches[0].get("lean_file", {}).get("sha256") != root.get("lean_file", {}).get("sha256")):
                errors.append("ORIGINAL_SCOPE_KERNEL_BINDING: every coverage/bridge root must belong to the live-audited Gold roots and theorem faces")
                continue
            _, kernel_path = _read(matches[0].get("lean_file"), base, "Gold root source", errors)
            _, reviewed_path = _read(root.get("lean_file"), rpath.parent, "reviewed root source", errors)
            if kernel_path != reviewed_path:
                errors.append("ORIGINAL_SCOPE_KERNEL_BINDING: reviewed and kernel root paths differ")
    if covered != clause_ids:
        errors.append("ORIGINAL_SCOPE_COVERAGE: every original clause must be covered exactly once")
    return errors


def _audit_scope_panel(data, base, *, required=False, require_final_answer=False):
    if not required and not require_final_answer and not claims_original_completion(data):
        return []
    refs = data.get('original_scope_audits')
    if not isinstance(refs, list) or len(refs) < 2:
        return ['ORIGINAL_SCOPE_PANEL: at least two independently dispatched original_scope_audits required; legacy single review is insufficient']
    errors = []
    count = data.get('original_scope_review_count', len(refs))
    if type(count) is not int or count != len(refs) or count < 2:
        errors.append('ORIGINAL_SCOPE_PANEL: review count must match all supplied reviews and be at least two')
    if 'original_scope_audit' in data and data['original_scope_audit'] != refs[0]:
        errors.append('ORIGINAL_SCOPE_PANEL: optional primary alias must equal the first panel reference')
    reviewers, tasks, sessions = set(), set(), set()
    forbidden = {_identity(data.get('manifest_author'))} | {_identity(x) for x in data.get('implementers', [])}
    forbidden_tasks = set(forbidden)
    for field in ('final_proof_review', 'silver_review'):
        if field not in data:
            continue
        other, path = _read(data[field], base, field, errors, json_file=True)
        if other is not None:
            forbidden.add(_identity(other.get('reviewer')))
            forbidden_tasks.add(_identity(other.get('reviewer')))
            receipt, _ = _read(other.get('reviewer_provenance'), path.parent, field + ' dispatch', errors, json_file=True)
            if receipt is not None:
                forbidden_tasks.update(_identity(receipt.get(key)) for key in ('task_id', 'session_id'))
    binding = None
    prompt_hash = None
    for number, ref in enumerate(refs):
        individual = dict(data, original_scope_audit=ref)
        try:
            errors.extend(f'review[{number}]: ' + error for error in _audit_original_scope(
                individual, base, required=True, require_final_answer=require_final_answer))
        except (TypeError, ValueError, KeyError, AttributeError) as exc:
            errors.append(f'ORIGINAL_SCOPE_SCHEMA: review[{number}] malformed evidence: {exc}')
        report, path = _read(ref, base, f'original_scope_audits[{number}]', errors, json_file=True)
        if report is None:
            continue
        receipt, _ = _read(report.get('reviewer_provenance'), path.parent,
                           f'review[{number}] dispatch', errors, json_file=True)
        if receipt is None:
            continue
        reviewer, task = _identity(report.get('reviewer')), _identity(receipt.get('task_id'))
        session = _identity(receipt.get('session_id', receipt.get('task_id')))
        if (not reviewer or reviewer in reviewers or reviewer in forbidden or not task or not session
                or task in tasks or session in sessions or task in forbidden_tasks or session in forbidden_tasks
                or task in sessions or session in tasks
                or reviewer in tasks | sessions | forbidden_tasks
                or task in reviewers | forbidden or session in reviewers | forbidden):
            errors.append('ORIGINAL_SCOPE_PANEL_INDEPENDENCE: distinct independent reviewer identities and dispatch tasks/sessions required')
        reviewers.add(reviewer); tasks.add(task); sessions.add(session)
        input_hash = report.get('review_input_sha256')
        actual_prompt = receipt.get('prompt_sha256')
        if (not isinstance(input_hash, str) or not _HASH.fullmatch(input_hash)
                or receipt.get('review_input_sha256') != input_hash
                or not isinstance(actual_prompt, str) or not _HASH.fullmatch(actual_prompt)):
            errors.append('ORIGINAL_SCOPE_PANEL_STALE: report and dispatch must bind the immutable review input and actual prompt hashes')
        if prompt_hash is None:
            prompt_hash = actual_prompt
        elif prompt_hash != actual_prompt:
            errors.append('ORIGINAL_SCOPE_PANEL_STALE: independently dispatched reviews must receive identical actual prompts')
        current = {key: report.get(key) for key in ('original_problem_sha256', 'target_contract_sha256',
            'final_answer_sha256', 'proof_snapshot_sha256', 'roots', 'proof_commit', 'review_input_sha256')}
        if binding is None:
            binding = current
        elif current != binding:
            errors.append('ORIGINAL_SCOPE_PANEL_STALE: every review must bind the identical original, target, answer and complete root snapshot')
    return errors


def audit_original_scope(data: Mapping[str, Any], base: Path | None, *, required=False, require_final_answer=False) -> list[str]:
    try:
        return _audit_scope_panel(data, base, required=required, require_final_answer=require_final_answer)
    except (TypeError, ValueError, KeyError, AttributeError) as exc:
        return [f"ORIGINAL_SCOPE_SCHEMA: malformed evidence: {exc}"]


def _check_lean_original(original, report, target, original_base, report_base, root_names, errors):
    lean = original.get("lean_target")
    if not isinstance(lean, dict):
        errors.append("ORIGINAL_SCOPE_LEAN: original Lean target metadata required")
        return
    payload, _ = _read(lean.get("source"), original_base, "original Lean declaration", errors)
    signature = lean.get("signature")
    from research_grade import _strip_lean_comments
    if (not _text(signature) or payload is None or not isinstance(lean.get("declaration"), str)
            or _declaration_signature(payload, lean["declaration"]) != signature):
        errors.append("ORIGINAL_SCOPE_LEAN: exact original declaration must bind its frozen source")
        return
    # Input environments may be supplied as a pinned manifest or a literal version record.
    if not _nonempty(lean.get("toolchain")) or not isinstance(lean.get("imports"), list):
        errors.append("ORIGINAL_SCOPE_LEAN: frozen toolchain and import/version census required")
    elif any(not isinstance(x, dict) or not x.get("module") or not x.get("revision") for x in lean["imports"]):
        errors.append("ORIGINAL_SCOPE_LEAN: each imported module needs its pinned revision")
    definitions = lean.get("definitions")
    if not isinstance(definitions, list):
        errors.append("ORIGINAL_SCOPE_LEAN: original necessary definitions census required")
    else:
        for definition in definitions:
            if not isinstance(definition, dict):
                errors.append("ORIGINAL_SCOPE_LEAN: invalid definition")
                continue
            text, _ = _read(definition.get("source"), original_base, "original definition", errors)
            if not _text(definition.get("statement")) or text is None or definition["statement"] not in _strip_lean_comments(text):
                errors.append("ORIGINAL_SCOPE_LEAN: original definition is not bound to source")
    comparison = report.get("lean_comparison")
    original_hash = hashlib.sha256(signature.encode()).hexdigest()
    selected_hash = hashlib.sha256(str(target.get("target_signature", "")).encode()).hexdigest()
    if (not isinstance(comparison, dict) or comparison.get("original_signature_sha256") != original_hash
            or comparison.get("target_signature_sha256") != selected_hash):
        errors.append("ORIGINAL_SCOPE_LEAN: comparison must bind both original and selected interfaces")
        return
    def statement_type(value):
        return re.sub(r"^(?:(?:theorem|lemma)\s+[\w'.]+|example)", "", value).strip()
    if comparison.get("mode") == "exact_type":
        if statement_type(signature) != statement_type(target.get("target_signature", "")):
            errors.append("ORIGINAL_SCOPE_LEAN: claimed exact type is not the original Lean type")
    elif comparison.get("mode") == "checked_bridge":
        bridge = comparison.get("bridge_root")
        if not isinstance(bridge, str) or bridge not in root_names:
            errors.append("ORIGINAL_SCOPE_LEAN: bridge must be an inspected main root")
        evidence, _ = _read(comparison.get("verification"), report_base, "bridge verification", errors, json_file=True)
        if (evidence is None or evidence.get("status") != "passed"
                or evidence.get("original_signature_sha256") != original_hash
                or evidence.get("target_signature_sha256") != selected_hash
                or evidence.get("bridge_root") != bridge or not _text(evidence.get("command"))
                or evidence.get("bridge_source_sha256") != next((r.get("lean_file", {}).get("sha256")
                    for r in report.get("roots", []) if r.get("name") == bridge), None)):
            errors.append("ORIGINAL_SCOPE_LEAN: missing or stale checked bridge evidence")
        elif _read(evidence.get("transcript"), report_base, "bridge transcript", errors)[0] is None:
            errors.append("ORIGINAL_SCOPE_LEAN: bridge transcript is unavailable")
    else:
        errors.append("ORIGINAL_SCOPE_LEAN: exact_type or checked_bridge comparison required")


def node_scope_errors(node: Mapping[str, Any]) -> list[str]:
    """Plan claims use a hash-bound audited manifest; a selected anchor is insufficient."""
    if not claims_original_completion(node):
        return []
    ref = node.get("original_scope_manifest")
    if not isinstance(ref, dict) or not isinstance(ref.get("path"), str) or not Path(ref["path"]).is_absolute():
        return ["ORIGINAL_SCOPE_PLAN: an absolute hash-bound original_scope_manifest is required"]
    manifest, path = _read(ref, Path(ref["path"]).parent, "plan scope manifest", errors := [], json_file=True)
    if manifest is None:
        return errors
    errors.extend(audit_original_scope(manifest, path.parent, required=True))
    target, _ = _read(manifest.get("target_contract"), path.parent, "plan target", errors, json_file=True)
    target_key = "target_statement" if manifest.get("candidate_kind") == "natural_language" else "target_signature"
    if target is not None and (target.get(target_key) != node.get("anchor")
                              or target.get("plan_statement_id") != node.get("statement_id", node.get("id"))):
        errors.append("ORIGINAL_SCOPE_PLAN: reviewed target is not this plan node and exact anchor")
    return errors


def require_node_scope(node: Mapping[str, Any]) -> None:
    errors = node_scope_errors(node)
    if errors:
        raise ValueError("; ".join(errors))


def scope_checked_view(node: dict | None) -> dict | None:
    """Fail closed on stale persisted claims, without silently rewriting user history."""
    if node is None:
        return None
    if node.get("original_scope_status") == "blocked" and not claims_original_completion(node):
        return dict(node)
    errors = node_scope_errors(node)
    if not errors:
        # The plan store historically exposes live nodes. Preserve that API for
        # valid/local results so receipt reconciliation observes actual mutations.
        # Only blocked claims need a masked copy; never mutate their stored history.
        node["original_scope_status"] = "passed" if claims_original_completion(node) else "not_certified"
        return node
    result = dict(node)
    result["original_scope_status"] = "blocked"
    if errors:
        result["question_status"] = "scope_review_required"
        if result.get("claim_scope") in {"full_original", "original_problem"}:
            result["historical_claim_scope"] = result["claim_scope"]
            result["claim_scope"] = "scope_review_required"
        result["original_problem_completed"] = False
        result["submission_eligible"] = False
        result["original_scope_errors"] = errors
    return result
