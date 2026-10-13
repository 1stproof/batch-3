"""Credit survives self-contained proofs and unavailable citation metadata."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.literature import attribution_errors, attribution_input_sources, literature_search_errors, web_search_queries
from paper_writing_codex.tex_inventory import inventory_tex


class AttributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.source = self.work / "supplied.tex"
        self.source.write_text("A previous theorem of Smith \\cite{smith} supplies this identity.\n")
        self.output = self.work / "final.tex"
        self.output.write_text("This identity is due to Smith; a self-contained proof follows.\n")
        self.state = {"mode": "compose", "work_dir": str(self.work), "output": str(self.output),
                      "attribution_policy": "input-credit-v1"}
        self.write("raw.json", {"evidence": {"writer_ids": ["writer"], "source_records": [
            {**self.ref(self.source), "kind": "natural-language"}]}})
        self.state["raw_checkpoint"] = {"manifest": str(self.work / "raw.json"),
                                        "manifest_sha256": self.ref(self.work / "raw.json")["sha256"]}
        self.census = {"schema_version": 1, "verdict": "PASS", "reviewer_id": "input-reader",
                       "writer_ids": ["writer"], "findings": "All supplied mathematical sources and prose credit were read.",
                       "input_sources": attribution_input_sources(self.state), "credits": [{
                           "credit_id": "smith-identity", **self.excerpt(self.source),
                           "attribution": "The supplied mathematical input explicitly credits Smith's identity."}]}
        self.audit = {"schema_version": 1, "verdict": "PASS", "reviewer_id": "final-reader",
                      "writer_ids": ["writer"], "findings": "Smith's established credit remains at the actual identity use-site.",
                      "candidate_source_tree_sha256": inventory_tex(self.output)["source_tree_sha256"],
                      "unresolved_proof_dependencies": [], "unresolved_attribution_issues": [],
                      "decisions": [{"credit_id": "smith-identity", "disposition": "keep",
                          "proof_dependency": "self-contained", "metadata_status": "unavailable",
                          "reason": "Official citation metadata is unavailable but known scientific credit is retained.",
                          "use_sites": [{**self.excerpt(self.output), "line": 1}]}]}
        self.save()

    def write(self, name, value):
        (self.work / name).write_text(json.dumps(value))

    def ref(self, path):
        return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    def excerpt(self, path):
        text = path.read_text().rstrip("\n")
        return {"source_path": str(path), "excerpt": text,
                "excerpt_sha256": hashlib.sha256(text.encode()).hexdigest()}

    def save(self):
        self.write("credit-census.json", self.census)
        self.state["input_credit_census"] = self.ref(self.work / "credit-census.json")
        self.audit["input_credit_census"] = self.state["input_credit_census"]
        self.write("attribution-audit.json", self.audit)
        self.state["attribution_audit"] = self.ref(self.work / "attribution-audit.json")

    def test_zero_formal_references_can_preserve_actual_named_credit_without_export(self):
        self.assertEqual(inventory_tex(self.output)["citations"], [])
        self.assertEqual(attribution_errors(self.state), [])

    def test_empty_credit_census_cannot_pass_when_scientific_input_cites_prior_work(self):
        self.census["credits"] = []
        self.audit["decisions"] = []
        self.save()
        self.assertIn("omits citation", " ".join(attribution_errors(self.state)))

    def test_missing_unresolved_duplicate_or_unlocated_decisions_fail(self):
        original = copy.deepcopy(self.audit)
        for change in ([], [dict(original["decisions"][0], disposition="unresolved")],
                       original["decisions"] * 2,
                       [dict(original["decisions"][0], use_sites=[])],
                       [dict(original["decisions"][0], use_sites=[dict(self.excerpt(self.output), line=2)])]):
            self.audit = {**copy.deepcopy(original), "decisions": change}
            self.save()
            self.assertTrue(attribution_errors(self.state))

    def test_input_omission_stale_source_and_stale_final_fail(self):
        self.census["input_sources"] = []
        self.save()
        self.assertTrue(attribution_errors(self.state))
        self.census["input_sources"] = attribution_input_sources(self.state)
        self.save()
        self.source.write_text("Source credit was silently erased.\n")
        self.assertTrue(attribution_errors(self.state))
        self.source.write_text("A previous theorem of Smith \\cite{smith} supplies this identity.\n")
        self.output.write_text("This identity is entirely our original work.\n")
        self.assertTrue(attribution_errors(self.state))

    def test_reviewers_must_be_separate_and_independent_of_all_writers(self):
        for identity in ("input-reader", " WRITER "):
            self.audit["reviewer_id"] = identity
            self.save()
            self.assertTrue(attribution_errors(self.state))

    def test_not_applicable_needs_explanation_and_has_no_fictional_use_site(self):
        d = self.audit["decisions"][0]
        d.update(disposition="not-applicable", use_sites=[])
        self.save()
        self.assertTrue(attribution_errors(self.state))
        d["not_applicable_evidence"] = "The identity and all of its consumers were removed from the final manuscript."
        self.save()
        self.assertEqual(attribution_errors(self.state), [])

    def test_new_contract_does_not_reinterpret_legacy_receipts(self):
        self.state.pop("attribution_policy")
        self.state.pop("input_credit_census")
        self.assertEqual(attribution_errors(self.state), [])
        self.assertTrue(attribution_errors(self.state, required=True))


class RelevanceSearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.output = self.work / "paper.tex"
        self.output.write_text("A complete self-contained argument.\n")
        self.state = {"work_dir": str(self.work), "output": str(self.output),
                      "literature_search_policy": "search-read-v1"}
        self.query = {"query": "Smith identity mathematical proof", "candidate_ids": ["smith"],
                      "execution": "network-search", "findings": "The search found Smith's potentially relevant identity article.",
                      "host_call": {"session_id": "search-writer", "call_id": "query-1"}}
        self.search = {"schema_version": 1, "status": "completed",
                       "writer_ids": ["search-writer"],
                       "candidate_source_tree_sha256": inventory_tex(self.output)["source_tree_sha256"],
                       "findings": "Relevance search performed; the identified candidate belongs to an unrelated domain.",
                       "queries": [{"query": self.query["query"], "purpose": "Find earlier work on the identity used in the present proof.",
                                    "candidate_ids": ["smith"]}],
                       "candidates": [{"candidate_id": "smith", "identity": "Smith, Identities in an unrelated mathematical domain",
                           "source_type": "article", "disposition": "rejected-discovery", "read_status": "not-read",
                           "cache_reused": False, "relevance": "The discovery record identifies an unrelated application domain.",
                           "reason": "The title and discovery metadata concern a different mathematical object."}]}
        self.save()

    def ref(self, name, value):
        path = self.work / name
        path.write_text(json.dumps(value))
        return {"path": name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    def save(self):
        self.search["queries"][0]["search_record"] = self.ref("query.json", self.query)
        self.search["candidates"][0]["retrieval_record"] = self.ref("retrieval.json", {"findings": "Candidate metadata inspected through the actual search result."})
        self.state["literature_search"] = self.ref("search.json", self.search)
        events = [{"call_id": "query-1", "verified_native_web": "native-web-run-v1"}]
        payload = {"type": "function_call", "namespace": "web", "name": "run", "call_id": "query-1",
                   "arguments": json.dumps({"search_query": [{"q": self.query["query"]}]})}
        rollout = self.work / "rollout.jsonl"
        rollout.write_text(json.dumps({"type": "response_item", "payload": payload}) + "\n")
        operations = []
        candidate = self.search["candidates"][0]
        if "primary_source" in candidate:
            events.append({"call_id": "read-1"})
            source_path = Path(candidate["primary_source"]["path"])
            if not source_path.is_absolute():
                source_path = self.work / source_path
            public = {"status": "read", "sha256": candidate["primary_source"]["sha256"],
                      "start": 0, "end": len(source_path.read_text())}
            if "public_source_receipt" in candidate:
                receipt_path = Path(candidate["public_source_receipt"]["path"])
                source_path = Path(candidate["primary_source"]["path"])
                member = str(source_path.relative_to(receipt_path.parent)) if source_path.is_relative_to(receipt_path.parent) else source_path.name
                public.update(source_id=receipt_path.parent.name, receipt_sha256=candidate["public_source_receipt"]["sha256"], member=member)
            operations.append({"tool": "read_public_source", "call_id": "read-1", "session_id": "search-writer",
                               "is_error": False, "public_source": public})
        ops = self.work / "document-operations.jsonl"
        ops.write_text("".join(json.dumps(o) + "\n" for o in operations))
        meta = self.ref("stage.meta.json", {"status": "completed", "turn_completed": True,
            "model_verified": True, "session_id": "search-writer", "protocol_errors": [],
            "document_audit": {"status": "PASS", "complete_tool_outputs_delivered": True, "errors": [], "delivery_errors": []},
            "persisted_rollout_audit": {"status": "verified", "tool_events": events, "rollout_paths": [str(rollout)]}})
        self.audit = {"schema_version": 1, "reviewer_id": "search-auditor", "writer_ids": ["search-writer"],
            "candidate_source_tree_sha256": self.search["candidate_source_tree_sha256"],
            "literature_search": self.state["literature_search"], "verdict": "PASS", "unresolved_findings": [],
            "findings": "The actual host query and read receipts support the relevance and source decisions.",
            "transport_evidence": [meta, {"path": str(rollout), "sha256": hashlib.sha256(rollout.read_bytes()).hexdigest()},
                                   {"path": str(ops), "sha256": hashlib.sha256(ops.read_bytes()).hexdigest()}]}
        self.state["literature_search_audit"] = self.ref("search-audit.json", self.audit)

    def test_discovery_rejection_is_not_falsely_claimed_as_read(self):
        self.assertEqual(literature_search_errors(self.state), [])
        self.search["candidates"][0]["read_status"] = "read"
        self.save()
        self.assertTrue(literature_search_errors(self.state))

    def test_zero_references_without_actual_relevance_search_cannot_pass(self):
        self.search["queries"] = []
        self.state["literature_search"] = self.ref("search.json", self.search)
        self.assertTrue(literature_search_errors(self.state))

    def test_constrained_or_fictional_cached_search_cannot_pass(self):
        self.search["status"] = "constrained"
        self.save()
        self.assertTrue(literature_search_errors(self.state))
        self.search["status"] = "completed"
        self.query["execution"] = "cached-search"
        self.save()
        self.assertTrue(literature_search_errors(self.state))
        original = dict(self.query, execution="network-search")
        self.query["cache_origin"] = self.ref("old-search.json", original)
        self.save()
        self.assertEqual(literature_search_errors(self.state), [])

    def test_content_rejection_requires_actual_hashed_source_and_precise_reading(self):
        candidate = self.search["candidates"][0]
        candidate.update(disposition="rejected-content", read_status="read")
        self.save()
        self.assertTrue(literature_search_errors(self.state))
        source = self.work / "article.tex"
        source.write_text("Theorem 2 concerns objects absent from the present paper.\n")
        source_ref = {"path": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
        excerpt = source.read_text().rstrip("\n")
        candidate["primary_source"] = source_ref
        candidate["read_record"] = self.ref("reading.json", {
            "reader_id": "reader", "source_sha256": source_ref["sha256"], "locator": "Theorem 2",
            "exact_claim": "Theorem 2 establishes an identity for different objects under different assumptions.",
            "findings": "Read the precise theorem and its surrounding hypotheses; not used in this paper.",
            "source_path": source.name, "excerpt": excerpt,
            "host_call": {"session_id": "search-writer", "call_id": "read-1"},
            "excerpt_sha256": hashlib.sha256(excerpt.encode()).hexdigest()})
        self.save()
        self.assertEqual(literature_search_errors(self.state), [])
        source.write_text("Different unread source.\n")
        self.assertTrue(literature_search_errors(self.state))

    def test_search_audit_is_independent_and_binds_actual_host_transport(self):
        original = copy.deepcopy(self.audit)
        for key, value in (("reviewer_id", "SEARCH-WRITER"), ("transport_evidence", []),
                           ("unresolved_findings", ["No actual source read"]),
                           ("candidate_source_tree_sha256", "0" * 64)):
            self.audit = {**copy.deepcopy(original), key: value}
            self.state["literature_search_audit"] = self.ref("search-audit.json", self.audit)
            self.assertTrue(literature_search_errors(self.state))

    def test_self_declared_query_with_no_matching_host_call_fails(self):
        self.query["host_call"]["call_id"] = "invented-call"
        self.save()
        self.assertTrue(literature_search_errors(self.state))

    def test_host_query_binding_requires_performed_search_not_open_or_find(self):
        query = self.query["query"]
        forms = [("native", {"search_query": [{"q": query}], "response_length": "short"}, True),
                 ("bridge", {"search_query": [{"q": query}, {"q": "other query"}]}, True),
                 ("native", {"open": [{"ref_id": query}]}, False),
                 ("native", {"find": [{"ref_id": "source", "pattern": query}]}, False),
                 ("bridge", {"find": [{"ref_id": "source", "pattern": query}]}, False),
                 ("native", {"search_query": [{"q": "different query"}], "open": [{"ref_id": query}]}, False)]
        rollout = self.work / "rollout.jsonl"
        meta_path = self.work / "stage.meta.json"
        for kind, request, accepted in forms:
            with self.subTest(kind=kind, request=request):
                payload = {"call_id": "query-1"}
                meta = json.loads(meta_path.read_text())
                if kind == "native":
                    payload.update(type="function_call", namespace="web", name="run", arguments=json.dumps(request))
                    event = {"call_id": "query-1", "verified_native_web": "native-web-run-v1"}
                else:
                    payload.update(type="custom_tool_call", namespace="functions", name="exec",
                                   input="text(await tools.web__run(" + json.dumps(request) + "));" )
                    event = {"call_id": "query-1", "verified_web_bridge": "literal-web-run-v1"}
                meta["persisted_rollout_audit"]["tool_events"] = [event]
                meta_path.write_text(json.dumps(meta))
                rollout.write_text(json.dumps({"type": "response_item", "payload": payload}) + "\n")
                for ref in self.audit["transport_evidence"]:
                    path = Path(ref["path"])
                    path = path if path.is_absolute() else self.work / path
                    ref["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                self.state["literature_search_audit"] = self.ref("search-audit.json", self.audit)
                self.assertEqual(bool(literature_search_errors(self.state)), not accepted)

    def test_search_parser_rejects_unsupported_bridge_code_and_argument_shapes(self):
        native = {"type": "function_call", "namespace": "web", "name": "run"}
        for request in ({"search_query": {"q": "query"}}, {"search_query": [{"q": 4}]},
                        {"image_query": [{"q": "query"}]}, {"search_query": [{"q": "query"}], "extra": True}):
            self.assertEqual(web_search_queries(dict(native, arguments=json.dumps(request))), [])
        self.assertEqual(web_search_queries({"type": "custom_tool_call", "namespace": "functions", "name": "exec",
            "input": 'text(await tools.web__run({"search_query":[{"q":"query"}]})); text("extra");'}), [])

    def test_actual_read_window_must_contain_the_claim_excerpt(self):
        candidate = self.search["candidates"][0]
        candidate.update(disposition="rejected-content", read_status="read")
        source = self.work / "article.txt"
        source.write_text("An unrelated opening sentence.\nThe exact theorem used for this relevance decision.\n")
        source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        excerpt = "The exact theorem used for this relevance decision."
        candidate["primary_source"] = {"path": str(source), "sha256": source_hash}
        candidate["read_record"] = self.ref("reading.json", {"reader_id": "search-writer", "source_sha256": source_hash,
            "locator": "The second paragraph", "exact_claim": "The source establishes the precise theorem considered for relevance.",
            "findings": "The precise source statement was read and its domain differs from this paper.",
            "source_path": str(source), "excerpt": excerpt, "excerpt_sha256": hashlib.sha256(excerpt.encode()).hexdigest(),
            "host_call": {"session_id": "search-writer", "call_id": "read-1"}})
        self.save()
        self.assertEqual(literature_search_errors(self.state), [])
        ops_path = self.work / "document-operations.jsonl"
        original = json.loads(ops_path.read_text())
        for start, end in ((0, 29), (0, 45), (-1, len(source.read_text())),
                           (0, len(source.read_text()) + 1), (False, len(source.read_text())), (None, None)):
            operation = copy.deepcopy(original)
            operation["public_source"].update(start=start, end=end)
            ops_path.write_text(json.dumps(operation) + "\n")
            for ref in self.audit["transport_evidence"]:
                if Path(ref["path"]) == ops_path:
                    ref["sha256"] = hashlib.sha256(ops_path.read_bytes()).hexdigest()
            self.state["literature_search_audit"] = self.ref("search-audit.json", self.audit)
            self.assertTrue(literature_search_errors(self.state), (start, end))
        operation = copy.deepcopy(original)
        operation["public_source"].update(start=source.read_text().index(excerpt), end=len(source.read_text()))
        ops_path.write_text(json.dumps(operation) + "\n")
        for ref in self.audit["transport_evidence"]:
            if Path(ref["path"]) == ops_path:
                ref["sha256"] = hashlib.sha256(ops_path.read_bytes()).hexdigest()
        self.state["literature_search_audit"] = self.ref("search-audit.json", self.audit)
        self.assertEqual(literature_search_errors(self.state), [])

    def test_arxiv_selection_requires_versioned_host_archive_and_official_export_bytes(self):
        candidate = self.search["candidates"][0]
        candidate.update(source_type="arxiv", disposition="selected", read_status="read",
                         citation_key="smith", arxiv_id="2401.12345v2")
        self.output.write_text("Smith's identity is used here \\cite{smith}.\n")
        self.search["candidate_source_tree_sha256"] = inventory_tex(self.output)["source_tree_sha256"]

        def public(url, raw, member=None):
            source_id = hashlib.sha256(url.encode()).hexdigest()
            folder = self.work / "public-sources" / source_id
            folder.mkdir(parents=True)
            (folder / "raw").write_bytes(raw)
            members = []
            if member:
                (folder / member).write_text("Theorem 2 proves the identity under the displayed assumptions.\n")
                members = [{"member": member, "sha256": hashlib.sha256((folder / member).read_bytes()).hexdigest()}]
            else:
                members = [{"member": "raw", "sha256": hashlib.sha256(raw).hexdigest()}]
            receipt = {"source_id": source_id, "requested_url": url, "final_url": url, "status": "downloaded",
                       "raw_sha256": hashlib.sha256(raw).hexdigest(), "members": members, "content_files": []}
            (folder / "receipt.json").write_text(json.dumps(receipt))
            return folder, {"path": str(folder / "receipt.json"),
                            "sha256": hashlib.sha256((folder / "receipt.json").read_bytes()).hexdigest()}

        folder, receipt = public("https://arxiv.org/e-print/2401.12345v2", b"host-recorded archive bytes", "source.tex")
        source = folder / "source.tex"
        source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        candidate.update(primary_source={"path": str(source), "sha256": source_hash},
                         source_tex={"path": str(source), "sha256": source_hash}, public_source_receipt=receipt,
                         archive={"path": str(folder / "raw"), "sha256": hashlib.sha256((folder / "raw").read_bytes()).hexdigest()})
        excerpt = source.read_text().rstrip("\n")
        candidate["read_record"] = self.ref("reading.json", {"reader_id": "search-writer", "source_sha256": source_hash,
            "locator": "Theorem 2", "exact_claim": "Theorem 2 proves the identity under explicitly stated assumptions.",
            "findings": "Read the precise theorem and hypotheses and checked this manuscript's use.",
            "source_path": str(source), "excerpt": excerpt, "excerpt_sha256": hashlib.sha256(excerpt.encode()).hexdigest(),
            "host_call": {"session_id": "search-writer", "call_id": "read-1"}})
        export_folder, export_receipt = public("https://arxiv.org/bibtex/2401.12345", b"@article{smith,title={Identity},eprint={2401.12345}}\n")
        candidate["bibtex_export"] = {"path": str(export_folder / "raw"),
            "sha256": hashlib.sha256((export_folder / "raw").read_bytes()).hexdigest(),
            "source_url": "https://arxiv.org/bibtex/2401.12345", "public_source_receipt": export_receipt}
        self.save()
        self.assertEqual(literature_search_errors(self.state), [])
        original = copy.deepcopy(candidate)
        for field, value in (("arxiv_id", "2401.12345"), ("public_source_receipt", export_receipt),
                             ("source_tex", candidate["archive"]),
                             ("bibtex_export", dict(candidate["bibtex_export"], public_source_receipt=receipt))):
            self.search["candidates"][0] = {**copy.deepcopy(original), field: value}
            self.save()
            self.assertTrue(literature_search_errors(self.state))


if __name__ == "__main__":
    unittest.main()
