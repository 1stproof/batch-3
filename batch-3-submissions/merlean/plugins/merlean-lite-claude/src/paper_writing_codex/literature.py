"""Evidence gates for papers whose novelty is deliberately disabled or unassessed.

Checks bind declared independent findings; they cannot authenticate a dispatch or
prove absence of priority claims. Those remain substantive reviewer obligations.
"""
from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path

from .reader_rounds import _identity, _reference, _text
from .tex_inventory import CITE_RE, inventory_tex, strip_comments
from .versioning import sha256_file


def attribution_input_sources(state: dict) -> list[dict]:
    """Read scientific inputs from frozen provenance, never from the final draft.

    The host must still ensure source_records include every supplied scientific
    input. Expanding literal TeX includes catches credits outside the root file.
    """
    work = Path(state["work_dir"])
    sources: dict[str, str] = {}

    def add(path: Path, expected: str) -> None:
        path = path.expanduser().resolve()
        if not path.is_file() or sha256_file(path) != expected:
            raise ValueError(f"scientific input is missing or changed: {path.name}")
        if str(path) in sources and sources[str(path)] != expected:
            raise ValueError("conflicting scientific input hashes")
        sources[str(path)] = expected
        if path.suffix.lower() == ".tex":
            for item in inventory_tex(path)["source_files"]:
                child = Path(item["path"]).resolve()
                if item.get("missing") or not item.get("sha256"):
                    raise ValueError("scientific input has an unresolved TeX/Bib include")
                sources[str(child)] = item["sha256"]

    if state.get("mode") == "refine":
        add(Path(state["source"]), state["source_sha256"])
    checkpoint = state.get("raw_checkpoint")
    if checkpoint:
        _, raw = _reference({"path": checkpoint["manifest"],
                             "sha256": checkpoint["manifest_sha256"]}, work)
        records = raw["evidence"]["source_records"]
        if not isinstance(records, list) or not records:
            raise ValueError("frozen raw evidence needs scientific source records")
        for item in records:
            path = Path(item["path"])
            add(path if path.is_absolute() else work / path, item["sha256"])
    elif state.get("mode") == "compose":
        raise ValueError("compose attribution census needs frozen scientific source records")
    return [{"path": path, "sha256": digest} for path, digest in sorted(sources.items())]


def _excerpt(record: dict, sources: dict[str, str], work: Path) -> str:
    path = Path(record["source_path"])
    path = (path if path.is_absolute() else work / path).resolve()
    if str(path) not in sources or sha256_file(path) != sources[str(path)]:
        raise ValueError("credit excerpt must belong to a bound source file")
    excerpt = record.get("excerpt")
    if not isinstance(excerpt, str) or not excerpt.strip():
        raise ValueError("credit evidence needs a nonempty exact excerpt")
    if hashlib.sha256(excerpt.encode("utf-8")).hexdigest() != record.get("excerpt_sha256"):
        raise ValueError("credit excerpt hash does not match")
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".tex":
        text = strip_comments(text)
    if excerpt not in text:
        raise ValueError("credit excerpt is absent from the uncommented source")
    if "line" in record:
        line = record["line"]
        if not isinstance(line, int) or isinstance(line, bool) or line < 1:
            raise ValueError("credit use-site needs a positive line number")
        if not text.splitlines(keepends=True)[line - 1:] or not "".join(text.splitlines(keepends=True)[line - 1:]).startswith(excerpt):
            raise ValueError("credit use-site excerpt does not start at its declared line")
    return excerpt


def _independent(record: dict, writers: set[str]) -> str:
    ids = record.get("writer_ids")
    if not isinstance(ids, list) or not ids or not all(_identity(w) for w in ids):
        raise ValueError("attribution evidence needs actual writer_ids")
    writers.update(_identity(w) for w in ids)
    reviewer = _identity(record.get("reviewer_id"))
    if not reviewer or reviewer in writers:
        raise ValueError("attribution reviewer must be independent of all recorded writers")
    if record.get("verdict") != "PASS" or not _text(record.get("findings")):
        raise ValueError("attribution evidence needs PASS and concrete findings")
    return reviewer


def attribution_errors(state: dict, inventory: dict | None = None, *, required: bool = False) -> list[str]:
    """Versioned input-credit census and separate final use-site audit.

    Hash checks bind declared credit decisions; semantic completeness and actual
    independent dispatch remain reviewer/host obligations. Citation metadata is
    separate from attribution and proof dependence.
    """
    if not required and state.get("attribution_policy") != "input-credit-v1":
        return []
    try:
        _attribution(state, inventory or inventory_tex(Path(state["output"])))
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError, IndexError) as error:
        return [f"input-credit attribution: {error}"]


def _attribution(state: dict, inventory: dict) -> None:
    work = Path(state["work_dir"])
    census_path, census = _reference(state.get("input_credit_census"), work)
    audit_path, audit = _reference(state.get("attribution_audit"), work)
    if census.get("schema_version") != 1 or audit.get("schema_version") != 1:
        raise ValueError("unsupported input-credit attribution schema")
    inputs = attribution_input_sources(state)
    if census.get("input_sources") != inputs:
        raise ValueError("credit census must cover the exact frozen scientific input sources")
    _, bound_census = _reference(audit.get("input_credit_census"), work)
    if bound_census != census or audit_path == census_path:
        raise ValueError("final attribution audit must separately bind the frozen input census")
    if audit.get("candidate_source_tree_sha256") != inventory.get("source_tree_sha256"):
        raise ValueError("final attribution audit is stale for the candidate manuscript")
    writers: set[str] = set()
    if state.get("raw_checkpoint"):
        checkpoint = state["raw_checkpoint"]
        _, raw = _reference({"path": checkpoint["manifest"], "sha256": checkpoint["manifest_sha256"]}, work)
        writers.update(_identity(w) for w in raw["evidence"]["writer_ids"])
    for filename in ("07-reader-audit.json", "08-reader-rounds.json"):
        path = work / filename
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            ids = record.get("writer_ids")
            if not isinstance(ids, list) or not all(_identity(w) for w in ids):
                raise ValueError("reader record has malformed writer identities")
            writers.update(_identity(w) for w in ids)
    # Collect both records' writers before testing either reviewer.
    for record in (census, audit):
        ids = record.get("writer_ids")
        if not isinstance(ids, list) or not ids or not all(_identity(w) for w in ids):
            raise ValueError("attribution evidence needs actual writer_ids")
        writers.update(_identity(w) for w in ids)
    census_reviewer = _independent(census, writers)
    if _independent(audit, writers) == census_reviewer:
        raise ValueError("final attribution audit must be independent of the input census reviewer")
    credits = census.get("credits")
    if not isinstance(credits, list) or any(not isinstance(c, dict) or not _identity(c.get("credit_id")) for c in credits):
        raise ValueError("input census needs a credit list with stable IDs")
    ids = [c["credit_id"] for c in credits]
    if len(ids) != len(set(ids)):
        raise ValueError("input credit IDs must be unique")
    input_map = {item["path"]: item["sha256"] for item in inputs}
    represented: set[tuple[str, str]] = set()
    for credit in credits:
        excerpt = _excerpt(credit, input_map, work)
        if not _text(credit.get("attribution")):
            raise ValueError("each input credit needs concrete established attribution")
        source = Path(credit["source_path"])
        source = (source if source.is_absolute() else work / source).resolve()
        for match in CITE_RE.finditer(excerpt):
            represented.update((str(source), key.strip()) for key in match.group(1).split(",") if key.strip())
    for source in inputs:
        path = Path(source["path"])
        if path.suffix.lower() == ".tex":
            for match in CITE_RE.finditer(strip_comments(path.read_text(encoding="utf-8"))):
                for key in match.group(1).split(","):
                    if key.strip() and (str(path), key.strip()) not in represented:
                        raise ValueError(f"input credit census omits citation: {key.strip()}")
    decisions = audit.get("decisions")
    if not isinstance(decisions, list) or any(not isinstance(d, dict) for d in decisions):
        raise ValueError("final audit needs per-credit decisions")
    decision_ids = [d.get("credit_id") for d in decisions]
    if len(decision_ids) != len(set(decision_ids)) or set(decision_ids) != set(ids):
        raise ValueError("final decisions must cover every input credit exactly once")
    final_map = {str(Path(item["path"]).resolve()): item["sha256"] for item in inventory["source_files"] if not item.get("missing")}
    for decision in decisions:
        if (decision.get("disposition") not in {"keep", "not-applicable"}
                or decision.get("proof_dependency") not in {"self-contained", "verified-external", "not-applicable"}
                or decision.get("metadata_status") not in {"verified", "unavailable", "not-applicable"}
                or not _text(decision.get("reason"))):
            raise ValueError("credit decisions need resolved attribution, separate proof/metadata status and reasons")
        if decision["disposition"] == "keep":
            sites = decision.get("use_sites")
            if not isinstance(sites, list) or not sites:
                raise ValueError("retained credit needs actual final manuscript use-sites")
            for site in sites:
                if not isinstance(site, dict) or "line" not in site:
                    raise ValueError("retained credit needs located final manuscript excerpts")
                _excerpt(site, final_map, work)
        elif decision.get("use_sites") != [] or not _text(decision.get("not_applicable_evidence")):
            raise ValueError("not-applicable credit needs substantive evidence that its attributed material is absent")
    if audit.get("unresolved_proof_dependencies") != [] or audit.get("unresolved_attribution_issues") != []:
        raise ValueError("unresolved proof dependencies or attribution issues block release")


def literature_search_errors(state: dict, inventory: dict | None = None, *, required: bool = False) -> list[str]:
    """Require recorded relevance discovery and precise primary-source reading.

    This does not request or certify novelty. Constrained retrieval may allow
    drafting to continue, but cannot be relabeled a completed relevance search.
    The host authenticates actual searches, cache origin and source reading.
    """
    if not required and state.get("literature_search_policy") != "search-read-v1":
        return []
    try:
        _literature_search(state, inventory or inventory_tex(Path(state["output"])))
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError, IndexError) as error:
        return [f"literature relevance search/read: {error}"]


def _literature_search(state: dict, inventory: dict) -> None:
    work = Path(state["work_dir"])
    _, record = _reference(state.get("literature_search"), work)
    transport = _search_audit(state, inventory, record, work)
    if (record.get("schema_version") != 1 or record.get("status") != "completed"
            or record.get("candidate_source_tree_sha256") != inventory.get("source_tree_sha256")
            or not _text(record.get("findings"))):
        raise ValueError("relevance search must be completed with concrete findings bound to the current manuscript")
    queries, candidates = record.get("queries"), record.get("candidates")
    if not isinstance(queries, list) or not queries or not isinstance(candidates, list):
        raise ValueError("relevance discovery needs actual search queries and candidate dispositions")
    discovered: set[str] = set()
    for query in queries:
        if (not isinstance(query, dict) or not _identity(query.get("query"))
                or not _text(query.get("purpose"))):
            raise ValueError("search queries need concrete relevance purposes")
        _, search = _reference(query.get("search_record"), work)
        ids = query.get("candidate_ids")
        if (not isinstance(ids, list) or any(not _identity(i) for i in ids)
                or len(ids) != len(set(ids)) or search.get("query") != query["query"]
                or search.get("candidate_ids") != ids or not _text(search.get("findings"))
                or search.get("execution") not in {"network-search", "cached-search"}):
            raise ValueError("search evidence must bind actual query, execution, findings and discovered candidates")
        if search["execution"] == "cached-search":
            _, original = _reference(search.get("cache_origin"), work)
            if (original.get("query") != query["query"] or original.get("candidate_ids") != ids
                    or original.get("execution") != "network-search" or not _text(original.get("findings"))):
                raise ValueError("cached search must bind an actual prior network-search record")
            search = original
        _search_call(search.get("host_call"), transport, query["query"])
        discovered.update(ids)
    if any(not isinstance(c, dict) or not _identity(c.get("candidate_id")) for c in candidates):
        raise ValueError("discovered candidates need stable IDs")
    ids = [c["candidate_id"] for c in candidates]
    if len(ids) != len(set(ids)) or set(ids) != discovered:
        raise ValueError("every discovered candidate needs exactly one relevance disposition")
    for candidate in candidates:
        disposition = candidate.get("disposition")
        if (not _text(candidate.get("identity")) or not _text(candidate.get("relevance"))
                or candidate.get("source_type") not in {"arxiv", "article", "book"}
                or not isinstance(candidate.get("cache_reused"), bool)
                or disposition not in {"selected", "rejected-content", "rejected-discovery", "unavailable"}):
            raise ValueError("candidate needs publication identity, retrieval/cache status and a precise relevance decision")
        _reference(candidate.get("retrieval_record"), work, json_record=False)
        if disposition in {"unavailable", "rejected-discovery"}:
            if candidate.get("read_status") != "not-read" or not _text(candidate.get("reason")):
                raise ValueError("unavailable/discovery-only candidates must explicitly remain not-read with a concrete reason")
            if disposition == "unavailable" and not _text(candidate.get("retrieval_constraint")):
                raise ValueError("unavailable source needs its actual retrieval failure or policy constraint")
            continue
        source_path, _ = _reference(candidate.get("primary_source"), work, json_record=False)
        _, reading = _reference(candidate.get("read_record"), work)
        if (candidate.get("read_status") != "read" or not _identity(reading.get("reader_id"))
                or reading.get("source_sha256") != candidate["primary_source"]["sha256"]
                or not _text(reading.get("findings")) or not _text(reading.get("exact_claim"))
                or not _identity(reading.get("locator"))):
            raise ValueError("content decisions need actual primary-source reading, precise claim and locator")
        excerpt = _excerpt(reading, {str(source_path): candidate["primary_source"]["sha256"]}, work)
        read_operation = _read_call(reading.get("host_call"), transport,
                                    candidate["primary_source"]["sha256"], source_path, excerpt)
        if candidate["source_type"] == "arxiv":
            _reference(candidate.get("archive"), work, json_record=False)
            tex_path, _ = _reference(candidate.get("source_tex"), work, json_record=False)
            if tex_path != source_path or tex_path.suffix.lower() != ".tex":
                raise ValueError("arXiv relevance reading must use the actual cached/downloaded source TeX")
            arxiv_id = candidate.get("arxiv_id")
            if not isinstance(arxiv_id, str) or re.fullmatch(r"(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})v[1-9]\d*", arxiv_id) is None:
                raise ValueError("arXiv source identity must pin an exact version")
            receipt_path, receipt = _public_receipt(candidate.get("public_source_receipt"), work)
            archive_path, _ = _reference(candidate.get("archive"), work, json_record=False)
            if (receipt["requested_url"] != f"https://arxiv.org/e-print/{arxiv_id}"
                    or archive_path != receipt_path.parent / "raw"
                    or candidate["archive"]["sha256"] != receipt.get("raw_sha256")
                    or not any(source_path == receipt_path.parent / m["member"]
                               and candidate["primary_source"]["sha256"] == m["sha256"] for m in receipt["members"])):
                raise ValueError("arXiv archive and read TeX must belong to the same versioned host retrieval receipt")
            public_read = read_operation["public_source"]
            if (public_read.get("source_id") != receipt["source_id"]
                    or public_read.get("receipt_sha256") != receipt["receipt_sha256"]
                    or source_path != receipt_path.parent / str(public_read.get("member", ""))):
                raise ValueError("actual arXiv read operation must bind this exact retrieval receipt and TeX member")
        if disposition == "selected":
            key = candidate.get("citation_key")
            if not _identity(key) or key not in inventory["citations"]:
                raise ValueError("selected publication needs its actual final manuscript citation use-site")
            export = candidate.get("bibtex_export")
            export_path, _ = _reference(export, work, json_record=False)
            if not export_path.read_text(encoding="utf-8").lstrip().startswith("@"):
                raise ValueError("selected publication needs a saved citation export")
            if candidate["source_type"] == "arxiv":
                arxiv_id = candidate.get("arxiv_id")
                base_id = re.sub(r"v[1-9]\d*$", "", arxiv_id)
                official_urls = {f"https://arxiv.org/bibtex/{arxiv_id}", f"https://arxiv.org/bibtex/{base_id}"}
                if export.get("source_url") not in official_urls:
                    raise ValueError("arXiv citation metadata must bind the official Export BibTeX URL")
                receipt_path, receipt = _public_receipt(export.get("public_source_receipt"), work)
                if (receipt["requested_url"] != export["source_url"]
                        or receipt.get("final_url") not in official_urls
                        or export_path != receipt_path.parent / "raw"
                        or export["sha256"] != receipt.get("raw_sha256")):
                    raise ValueError("official BibTeX export must be the exact host-retrieved bytes")
                bibtex = export_path.read_text(encoding="utf-8")
                entry_key = re.search(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibtex)
                eprint = re.search(r"\beprint\s*=\s*[\{\"]([^}\"]+)[}\"]", bibtex, re.IGNORECASE)
                if (not entry_key or entry_key.group(1) != key or not eprint
                        or eprint.group(1).strip() not in {base_id, arxiv_id}):
                    raise ValueError("official BibTeX must identify the selected key and the same arXiv publication")


def _public_receipt(reference: object, work: Path) -> tuple[Path, dict]:
    path, _ = _reference(reference, work)
    if path.name != "receipt.json" or not path.parent.parent.is_dir():
        raise ValueError("primary source needs a host public-source receipt")
    from pilot_public_sources import verify_public_source
    receipt = verify_public_source(path.parent.parent.resolve(), path.parent.name)
    if receipt.get("status") != "downloaded" or receipt.get("receipt_sha256") != reference["sha256"]:
        raise ValueError("primary source retrieval is unavailable or stale")
    return path, receipt


def _search_audit(state: dict, inventory: dict, search: dict, work: Path) -> list[dict]:
    _, audit = _reference(state.get("literature_search_audit"), work)
    _, audited_search = _reference(audit.get("literature_search"), work)
    writers = {_identity(w) for w in search.get("writer_ids", [])}
    checkpoint = state.get("raw_checkpoint")
    if checkpoint:
        _, raw = _reference({"path": checkpoint["manifest"], "sha256": checkpoint["manifest_sha256"]}, work)
        writers.update(_identity(w) for w in raw["evidence"]["writer_ids"])
    for filename in ("07-reader-audit.json", "08-reader-rounds.json"):
        path = work / filename
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            ids = record.get("writer_ids")
            if not isinstance(ids, list) or not all(_identity(w) for w in ids):
                raise ValueError("reader record has malformed writer identities")
            writers.update(_identity(w) for w in ids)
    _independent(audit, writers)
    if (audit.get("schema_version") != 1 or audited_search != search
            or audit.get("candidate_source_tree_sha256") != inventory.get("source_tree_sha256")
            or audit.get("unresolved_findings") != []):
        raise ValueError("independent search audit must bind the current search and manuscript with no unresolved findings")
    refs = audit.get("transport_evidence")
    if not isinstance(refs, list) or not refs:
        raise ValueError("independent search audit needs actual host transport evidence")
    paths = []
    for reference in refs:
        path, _ = _reference(reference, work, json_record=False)
        paths.append(path)
    if len(paths) != len(set(paths)):
        raise ValueError("search transport evidence paths must be unique")
    transport = []
    for path in paths:
        if path.name != "stage.meta.json":
            continue
        meta = json.loads(path.read_text(encoding="utf-8"))
        persisted = meta.get("persisted_rollout_audit", {})
        session = _identity(meta.get("session_id"))
        if (meta.get("status") != "completed" or meta.get("turn_completed") is not True
                or meta.get("model_verified") is not True or not session
                or persisted.get("status") != "verified" or meta.get("protocol_errors")):
            raise ValueError("search transport must be a completed verified actual model call")
        delivery = meta.get("document_audit", {})
        if (delivery.get("status") != "PASS" or delivery.get("complete_tool_outputs_delivered") is not True
                or delivery.get("errors") or delivery.get("delivery_errors")):
            raise ValueError("search/read transport must authenticate actual complete tool-result delivery")
        # The host writer identity is authoritative even when omitted from a report.
        if session == _identity(audit.get("reviewer_id")):
            raise ValueError("search auditor cannot review their own search/source-reading dispatch")
        rollout_paths = persisted.get("rollout_paths")
        operations_path = path.parent / "document-operations.jsonl"
        if (not isinstance(rollout_paths, list) or not rollout_paths
                or any(Path(p).resolve() not in paths for p in rollout_paths)
                or operations_path not in paths):
            raise ValueError("search evidence must hash raw rollout and document-operation receipts")
        operations = [json.loads(line) for line in operations_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        events = []
        for rollout_path in rollout_paths:
            for line in Path(rollout_path).read_text(encoding="utf-8").splitlines():
                item = json.loads(line)
                if item.get("type") == "response_item" and isinstance(item.get("payload"), dict):
                    events.append(item["payload"])
        transport.append({"session_id": meta["session_id"], "tool_events": persisted.get("tool_events", []),
                          "operations": operations, "events": events})
    if not transport:
        raise ValueError("search evidence lacks authenticated host stage metadata")
    return transport


def web_search_queries(payload: dict) -> list[str]:
    """Extract performed text searches from the two admitted web-call forms.

    Opening a URL, finding a string in a page, and mentioning a query in another
    argument never constitute executing that search query.
    """
    if (payload.get("type") == "function_call" and payload.get("namespace") == "web"
            and payload.get("name") == "run"):
        source = payload.get("arguments")
    elif (payload.get("type") == "custom_tool_call" and payload.get("name") == "exec"
          and payload.get("namespace") in {None, "functions"}):
        code = payload.get("input")
        if not isinstance(code, str):
            return []
        match = re.fullmatch(r"\s*text\(await tools\.web__run\((.*)\)\);?\s*", code, re.DOTALL)
        if not match:
            return []
        source = match.group(1)
    else:
        return []
    if not isinstance(source, str):
        return []
    try:
        request = json.loads(source, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (ValueError, RecursionError):
        return []
    operations = {"search_query", "open", "click", "find", "screenshot", "image_query"}
    if not isinstance(request, dict) or request.keys() - operations - {"response_length"}:
        return []
    searches = request.get("search_query")
    if not isinstance(searches, list):
        return []
    return [item["q"] for item in searches if isinstance(item, dict)
            and isinstance(item.get("q"), str) and item["q"].strip()]


def _search_call(call: object, transport: list[dict], query: str) -> None:
    if not isinstance(call, dict):
        raise ValueError("query must identify its actual host search call")
    for record in transport:
        if call.get("session_id") != record["session_id"]:
            continue
        event = next((e for e in record["tool_events"] if e.get("call_id") == call.get("call_id")
                      and (e.get("verified_native_web") == "native-web-run-v1"
                           or e.get("verified_web_bridge") == "literal-web-run-v1")), None)
        payload = next((e for e in record["events"] if e.get("call_id") == call.get("call_id")), None)
        if event and payload and query in web_search_queries(payload):
            return
    raise ValueError("query is not present in its authenticated actual web-search call")


def _read_call(call: object, transport: list[dict], source_hash: str, source_path: Path, excerpt: str) -> dict:
    if not isinstance(call, dict):
        raise ValueError("primary-source reading must identify its actual host read call")
    for record in transport:
        if call.get("session_id") != record["session_id"]:
            continue
        for operation in record["operations"]:
            public = operation.get("public_source") or {}
            if (operation.get("call_id") == call.get("call_id") and operation.get("session_id") == call["session_id"]
                    and operation.get("tool") == "read_public_source" and operation.get("is_error") is False
                    and public.get("status") == "read" and public.get("sha256") == source_hash
                    and any(e.get("call_id") == call["call_id"] for e in record["tool_events"])):
                text = source_path.read_text(encoding="utf-8")
                start, end = public.get("start"), public.get("end")
                if (type(start) is int and type(end) is int and 0 <= start <= end <= len(text)
                        and excerpt in text[start:end]):
                    return operation
                raise ValueError("primary-source claim excerpt is outside its actual delivered read window")
    raise ValueError("claimed primary-source reading lacks the actual successful host read receipt")


def novelty_errors(state: dict, result: dict, inventory: dict) -> list[str]:
    status = result.get("novelty_status")
    label = result.get("result_id") or result.get("graph_node_id")
    try:
        policy_path = Path(state["work_dir"]) / "literature-policy.json"
        if policy_path.exists():
            policy = json.loads(policy_path.read_text(encoding="utf-8"))
            if (policy.get("schema_version") != 1 or
                    not isinstance(policy.get("assess_novelty"), bool)):
                raise ValueError("literature policy needs a Boolean assess_novelty setting")
            if not policy["assess_novelty"] and status != "NOT_REQUESTED":
                raise ValueError("disabled novelty must be recorded as NOT_REQUESTED, never CLEAR/ADJACENT")
        if status in {"CLEAR", "ADJACENT"}:
            return []  # Preserve the existing enabled/legacy novelty evidence contract.
        if status not in {"NOT_REQUESTED", "NOT_ASSESSED"}:
            return [f"compose main result has unresolved novelty status: {label}"]
        _limited_novelty(state, result, inventory)
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        return [f"compose main result literature evidence ({label}): {error}"]


def _limited_novelty(state: dict, result: dict, inventory: dict) -> None:
    work = Path(state["work_dir"])
    policy = json.loads((work / "literature-policy.json").read_text(encoding="utf-8"))
    if (policy.get("schema_version") != 1 or
            not isinstance(policy.get("assess_novelty"), bool)):
        raise ValueError("literature policy needs a Boolean assess_novelty setting")
    if result["novelty_status"] == "NOT_REQUESTED" and policy["assess_novelty"]:
        raise ValueError("NOT_REQUESTED requires assess_novelty false")
    if result["novelty_status"] == "NOT_ASSESSED" and not policy["assess_novelty"]:
        raise ValueError("disabled novelty must be recorded as NOT_REQUESTED")
    if result.get("priority_claim") is not False or not _text(result.get("novelty_limitations")):
        raise ValueError("disabled/unassessed novelty needs priority_claim false and concrete limitations")
    _, audit = _reference(result.get("literature_audit"), work)
    _, audited_policy = _reference(audit.get("policy_record"), work)
    if audited_policy != policy:
        raise ValueError("independent audit does not bind the current literature policy")
    _reference(audit.get("retrieval_record"), work, json_record=False)
    writers = audit.get("writer_ids")
    if not isinstance(writers, list) or not writers or not all(_identity(w) for w in writers):
        raise ValueError("independent literature audit needs actual writer_ids")
    known_writers = {_identity(w) for w in writers}
    if state.get("raw_checkpoint"):
        checkpoint = state["raw_checkpoint"]
        _, raw = _reference({"path": checkpoint["manifest"], "sha256": checkpoint["manifest_sha256"]}, work)
        known_writers.update(_identity(w) for w in raw["evidence"]["writer_ids"])
    for filename in ("07-reader-audit.json", "08-reader-rounds.json"):
        path = work / filename
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            extra = record.get("writer_ids")
            if not isinstance(extra, list) or not all(_identity(w) for w in extra):
                raise ValueError("reader record has malformed writer identities")
            known_writers.update(_identity(w) for w in extra)
    reviewer = _identity(audit.get("reviewer_id"))
    if not reviewer or reviewer in known_writers:
        raise ValueError("literature reviewer must be independent of all recorded writers")
    if (audit.get("verdict") != "PASS" or
            audit.get("candidate_source_tree_sha256") != inventory.get("source_tree_sha256") or
            audit.get("novelty_status") != result["novelty_status"]):
        raise ValueError("literature audit must pass and bind the current manuscript and novelty status")
    ids = audit.get("result_ids")
    if not isinstance(ids, list) or (result.get("result_id") or result.get("graph_node_id")) not in ids:
        raise ValueError("literature audit does not cover this selected result")
    if (audit.get("priority_claims_absent") is not True or
            audit.get("unresolved_proof_dependencies") != [] or
            audit.get("unresolved_attribution_issues") != [] or
            not _text(audit.get("findings")) or not _text(audit.get("overlap_disposition"))):
        raise ValueError("literature audit needs concrete claims, proof-dependency, credit and overlap findings")
