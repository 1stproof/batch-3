"""Validated infrastructure-only continuation notices; no research authority."""
import hashlib
import json
from pathlib import Path

CHANGES = {
    'explicit_handoff_resolution_and_user_routes': 'An explicitly supplied supervisor continuation resolution may resolve one exact saved operational handoff for the same original main in one fixed successor. The old request, receipt, scientific state and exhaustion history remain preserved. Later handoffs still stop; no review renewal or acceptance is granted. When enabled and explicitly user-requested, the existing pair of main-owned scientific_alternative tasks may explore concrete questions on valid current rows without claiming independent gaps. They remain bounded, deduplicated advisory work requiring original-main synthesis. Certificate strategies and all scientific review, independence, delivery, grade, model, deadline and retry gates remain unchanged.',
    'explicit_operational_handoff': 'The same original main may explicitly request an evidence-bound operational handoff when the current submitted candidate matches an authenticated exhausted review and no new scientific work is proposed. The exact typed response preserves all artifacts and ends partial for supervisor attention; no review, retry, acceptance or automatic resume authority is granted. Existing ordinary no-action checkpoints still continue research. Persisted handoff or a completed unadjudicated handoff response blocks automatic continuation and paper dispatch.',
    'local_compile_pending_contract_disclosure': 'Prospective local compile-pending returns explicitly place implementation_complete and next_step inside local_module_result, with source and approved rows at the response root. Shape diagnostics preserve the unchanged return and strict execution predicate. No historical return, retry limit, approval, or acceptance gate changes.',
    'draft_checkpoint_contract_disclosure': 'The main and its existing bounded structural correction now receive the exact three-field save-only draft response contract and literal shape diagnostics. Draft saves still do not submit scientific work or grant review, execution, or acceptance; historical rejected responses remain rejected.',
    'review_timeout_exhaustion_persistence': 'Exact exhausted review pairs remain operationally exhausted across continuations. Metadata-only changes cannot renew admission; changed original-main scientific content requires a fresh independent review under unchanged limits and acceptance gates. No historical prose becomes a verdict.',
    'legacy_terminal_process_reconciliation': 'A distinct legacy terminal receipt path can reconcile an unrelated recycled numeric PID when the historical stage has no recorded fingerprint. It requires immutable exact terminal command/session receipts, an independently hash-bound intervening complete absence census and seal, and repeated later unrelated current identity and ownership checks. It never fabricates historical fingerprints, signals processes, infers scientific completion, reopens terminal work, or alters budgets or acceptance gates. The existing complete-fingerprint path remains unchanged.',
    'typed_local_module_registry_restore': 'Continuation restoration now reads the local verification registry as its original JSON array of module records. It validates exact terminal-checkpoint and per-module artifact equality, structural lineage, bindings and consumed accounting, retaining historical records verbatim. Other control files remain object-only. This parsing repair neither resets counters nor changes terminal outcomes, independent approvals, scientific obligations or acceptance gates.',
    'selective_lean_coherent_execution': 'Prospective Lite certificate selection records exact remaining uncertainty, actual intended objects, noncircular accepted premises, bounded encoding feasibility/cost and added verification value. Zero new checks is valid when independently justified; existing selected obligations remain until substantive reassessment. An explicit compile_pending worker return requests host compilation and bounded implementation repair inside the same independently approved unchanged local module. A diagnostic need not claim prior uncertainty reduction. The host retains exact task, candidate, claim, premise, scope, approval and original cumulative budgets, and all source/diagnostic history. Changed boundaries, material adverse evidence, unavailable execution or exhausted limits return to main for existing reassessment; stopped historical returns are never relabelled or reopened by migration. Compilation does not grant scientific acceptance, deselection, Silver, full-proof or paired fresh original-scope passes.',
    'required_evidence_verification_convergence': 'Reviewers now receive a deterministic finite sequence of exact mandatory evidence pages before optional catalog navigation. Page size is transport framing, not a cap; every required character and historical record remains. Only authenticated complete model-visible delivery counts, and the existing same-reviewer recovery can retain verified complete chunks under the same scope and session. A fresh reviewer starts without that credit. Incomplete delivery remains a separate deficit: supported negative findings remain, but missing required evidence cannot grant global readiness, finding resolution, certificate deselection or execution approval. Existing completed-assessment dispatch identities and no-execution deduplication remain unchanged. Original scope, mathematical obligations, selected certificates, fresh final reviews, retry limits and acceptance gates remain unchanged.',
    'candidate_focused_convergence': 'The maintained research runtime now tracks a main-authored promising coherent high-level proof skeleton and the best preserved candidate as a convergence focus in every mode. During that focus, new advisory routes and research-worker tasks must address its necessary gaps; unrelated alternatives and optional generalizations are deferred. Concrete contrary evidence can reopen targeted exploration. Entry into convergence is a scheduling state, not proof completeness, original-scope acceptance or a grade. Existing findings, prior failures, independent reviews, selected-certificate obligations and final acceptance gates remain. This continuation has no exam profile, competition clock or automatic deadline.',
    'local_module_lineage_census': 'Independent local-verification reviews now receive the exact closed census of current registered module IDs and explicit JSON-null lineage examples. Historical probe paths and worker/stage labels remain evidence, not module ID aliases. A first registered lineage is bookkeeping, not a new mathematical claim or authorization to repeat historical work. Unknown and stale IDs still fail validation; existing independent selection, bounded protocol correction, task admission, resource limits and proof/grade gates remain unchanged. Prior rejected reviews remain non-authoritative and are not repaired retrospectively.',
    'exact_shared_main_feedback': 'Main feedback may now share byte-identical complete objects once using readable names, original source paths and explicit host-owned bindings. The exact original task remains in a separately hash-bound immutable artifact; the host verifies exact inverse reconstruction before dispatch. Every distinct field, finding version, status, source and historical record remains in the required delivery representation. Main must read all unique contents and bindings in the current stage; references, hashes, prior memory and partial reads cannot satisfy delivery. Sharing changes neither source authority nor proof acceptance, and does not select, summarize or make history optional.',
    'lossless_main_task_document_delivery': 'Document-enabled original-main turns now receive their complete exact task, response contract and feedback through immutable hash-bound read_artifact inputs. Every original byte remains in a full original root artifact. Exact bounded chunks partition the complete delivery representation, whose inverse reconstructs that original when exact sharing is used; chunk size is transport framing, not an evidence cap or summary. All required chunks or the exact complete root must actually be delivered in the current stage before any returned candidate, checkpoint, archive request, controller acknowledgement or publication is applied. Hashes and indexes alone grant no delivery. Existing main proof draft reads and saves remain available. The existing same-session timeout recovery retains its original retry bound and requires complete current-stage delivery, never inherited partial reads. This changes neither the original session, science, findings, convergence policy, review eligibility, acceptance gates nor accounting uncertainty; all historical failures remain preserved.',
    'rejected_review_authority_feedback': 'Preserved invalid proof-review receipts are bound to exact historical raw responses and explicitly delivered as rejected, non-authoritative evidence to the same original main. Transport completion never implies protocol acceptance; missing rejection receipts do not establish acceptance. Current-row research gaps retain their unchanged blocking predicates, now with row-specific errors. Main alone may reconcile its candidate and dependencies while preserving historical conjectures and findings; fresh independent scientific review remains mandatory. No raw verdict is repaired, finding resolved, gate weakened or execution authorized by this infrastructure change.',
    'main_owned_research_allocation': 'Research continuation now offers an advisory strategy menu rather than selecting a strategy by round number. Main may continue, refine or change its route based on the actual obstruction, preserved useful work and the next discriminating derivation. Scout synthesis compares obligations removed and introduced through existing research records; it does not force adoption or dispatch. Established background may be reused with precise statements and checked applicability; difficult theorem proofs do not alone require reconstruction. Research-result and uncertain-variant CITED source, trust and use-site requirements remain unchanged. No candidate binding, review/scout admission, deduplication, finding, retry or acceptance gate changes.',
    'readable_working_log': 'A readable working-log.md is reconstructed from existing durable problem records at status checkpoints, with source hashes and explicit historical provenance. It is a derived view separate from the current standalone proof.md and grants no scientific or execution authority. It preserves raw history and authored notes, dispatches no models, and exposes projection failures without changing research outcomes.',

    'explicit_reviewer_metadata_contract': 'Independent review guidance now spells out the unchanged reassessment reason requirement for deselecting either a previously selected row or a currently triaged candidate row, with mechanically applicable row IDs. Finding dispositions explicitly require nonempty string rationale and evidence fields, and host feedback identifies failing fields per finding. An evidence array fails the existing nonempty-string requirement even when no current consumers are named; a raw PASS does not override blocked accountability. These interface diagnostics do not judge evidence truth, supply reasons, coerce arrays, change candidate flags, remove findings, grant extra retries or relax any acceptance predicate. Already-reviewed unchanged assessments remain deduplicated; this notice does not reopen them or authorize a repeat. Earlier rejected or effectively blocked reports remain preserved with their original authority status.',
    'same_session_document_delivery_recovery': 'The existing one-time timeout recovery for an independent document reviewer now preserves verified full evidence delivery within that same logical review. The host revalidates the prior timed-out stage, capability, immutable artifacts, prompt and durable receipt evidence, then requires the same actual reviewer session and model, unchanged review scope, exact recovery prompt lineage and a successful current delivery audit. Only previously proven full artifact coverage may carry. Fresh reviewers, changed evidence, unsupported failures or tampered receipts cannot inherit it. No timeout bound, retry allowance, substantive review gate or grade requirement is changed; prior rejected reports remain rejected historical evidence.',
    'direct_scoped_document_tools': 'Document-enabled stages now use a recorded stage-local capability profile for the exact configured model so the confined MCP tools are advertised directly. Only tool exposure is downscoped: direct dispatch, no search, no internal agent delegation, no patch tool and no experimental tools. All other model metadata remains exact, the shared model cache is unchanged, and the same model/account/session and scientific gates remain. Call the advertised document tools directly; do not discover or invoke them through exec, shell or code-mode wrappers. Historical invalid tool attempts remain rejected and preserved, never retroactively accepted.',
    'canonical_proof_document': 'The original main maintains a standalone proof.md through atomic host revision publication. Draft saves preserve incomplete work without granting review or acceptance; explicit final submission binds exact immutable proof and full structured candidate. Interrupted drafts and all prior history remain preserved. A new draft does not invalidate old evidence on its original snapshot, but that evidence cannot approve the new draft.',
    'scoped_proof_document_tools': 'A confined local document channel permits original-main reads and draft saves during reasoning, with compare-and-swap revision binding. It cannot edit controller state, source, other problems or arbitrary files, and dispatches no reviewer or worker. Actual provider failure and missing usage remain explicit.',
    'plain_immutable_review_inputs': 'Independent reviewers receive the full current submitted proof as readable Markdown with complete current obligations, structured sidecars and exact immutable evidence access. Required and relied-on evidence must actually be delivered before a pass; unresolved needed evidence blocks. Historical files remain intact and indexed; no favorable selection, last-N pruning or automatic historical authority is introduced. Paper handoff pins the same independently accepted immutable source.',
    'remove_artificial_prompt_limits': 'The pilot-specific one-million-byte prompt and seven-hundred-thousand-byte resume guards are removed. No evidence is truncated and no replacement local cap is introduced. Actual provider, transport, timeout and quota failures retain their existing handling and exact accounting uncertainty.',

    'explicit_selected_triage_rows': 'Review guidance now states the unchanged exact relationship between triaged_rows and selected:true decisions, including the valid empty array when none are selected. Mismatch diagnostics retain expected selected IDs and the received field. Every ledger row still requires a substantive decision, and removing prior selection still requires independent reassessment. Raw rejected reports, the single fresh protocol correction bound and all scientific gates remain unchanged; no coercion or retrospective authority is introduced.',

    'positive_reference_cost_selection': 'One additional exact text-sharing candidate prices the already supported positive-reference representation and explores dense short word spans. All eleven earlier candidates, frequency orderings, v1-v4 representations and decoders remain available; the smallest complete UTF-8 packet wins. Literal integers, booleans, floats, negative zero, JSON field order, Unicode, whitespace and every historical diagnostic remain exact. No evidence, instruction, trust gate or prompt limit is removed or changed; tested current sizing is not a guarantee for future growth.',

    'exact_archive_evidence_retrieval': 'The original main may request one complete whitelisted historical item from its own immutable continuation checkpoint using the exact indexed pointer and hashes. The host checks snapshot bytes, original question and session, returns exact full content with historical provenance, and records separate operational receipts. No arbitrary path, network retrieval, rewritten history, current verdict reuse, task approval or review eligibility is granted. Missing, changed, private or out-of-scope items are refused; complete delivery still obeys the unchanged one-million-byte prompt guard. One retrieval round is followed by the ordinary typed main contract and its existing bounded structural correction. Existing no-action exploration checkpoints remain available only when the stored candidate is unchanged and no new finding or execution request is hidden.',
    'preserved_named_accounting_phase': 'Continuation may retain an existing parent pN-phaseN accounting phase exactly, in addition to existing phaseN behavior. This does not introduce or rename a problem-scoped phase, change source questions, reset usage, or grant scientific authority.',

    'explicit_checkpoint_finding_protocol': 'Main and the existing same-session correction now receive the exact unchanged scientific finding keys and enums, with indexed literal schema diagnostics. Complete invalid corrections are preserved on exhaustion. Administrative host-gate history remains intact and cannot be relabeled as science; no alias conversion, authority relaxation or additional retry is introduced.',
    'positive_reference_review_packing': 'A lossless v4 review representation uses nonnegative integer references with explicit colliding integer escapes; frequency-ordered dictionaries retain dependency order. All previous codecs/candidates remain available and the smallest complete UTF-8 packet wins. Fields, types, order, raw failed diagnostics, Unicode and whitespace remain exact; the one-million-byte predispatch guard and all mathematical gates are unchanged.',
    'lite_local_verification_modules': 'Lite selected local checks now use bounded host-owned claim lineages shared by Sol and inline Lean. Scope, encoding or no-value exits return full evidence to the original main without resolving mathematical obligations. Existing independent review supplies exact retriage and justified replacement or deselection; accepted explicit hypotheses need no foundational formalization. All final gates and Heavy behavior remain unchanged.',
    'adverse_obstruction_feedback_routing': 'Advisory route eligibility may retain an independently identified adverse obstruction when the exact reviewed scientific artifact is authenticated and unchanged, even after supplemental unreviewed checkpoint findings or new task proposals. Those new findings are preserved and supplied; they grant no execution, resolution or acceptance authority. Changed proof, ledger, assumptions or other substantive fields still require current independent review. Supplemental-only finding churn cannot renew an identical paid advisory portfolio, including authenticated legacy portfolios; complete prompt and acceptance bindings retain all findings. An ineligible route proposal returns its exact rejection to the same main for substantive strategy development without scout dispatch or terminating the unfinished research goal.',
    'compact_lossless_review_tags': 'Additional exact short-span candidates now price text and shared-value substitutions using their eventual v3 wire representation, instead of legacy v1 reference overhead. All older candidates and v1-v3 decoders remain available; the complete smallest packet wins. Version3 additionally flattens container syntax and explicitly escapes negative integer literals; versions1/2 remain decodable. Exact literal span selection may minimize estimated shared storage, with complete encoded size deciding the winner. Additional short literal word spans now compete with every prior packing variant; only a smaller complete encoding is selected. Review packing now chooses the smallest complete representation among existing lossless packets and explicit compact-reference/text tags with literal clause and repeated word-span sharing. Every field, dictionary value, order, Unicode and whitespace character is reconstructible from the supplied packet; no evidence or invalid-response diagnostic is omitted. The unchanged one-million-byte predispatch guard and all acceptance gates still apply. This infrastructure repair grants no mathematical progress or retrospective acceptance.',
    'persistent_unfinished_research': 'An unfinished original problem remains active across honest no-action checkpoints, deduplicated reviews and failed route portfolios. The same Astra main performs substantive strategy development with durable candidate/findings/route bindings, while unchanged paid reviews and scout portfolios remain suppressed. Strategy metadata is not scientific progress or acceptance authority. A completed peer is carried forward only after independent controller validation of its exact prior acceptance evidence, without new research dispatch. User stop, drain, quota and infrastructure safeguards remain effective.',
    'parallel_scientific_routes': 'When explicitly enabled, main can propose two distinct bounded Astra advisory route tasks for current independently evidenced scientific or selected-certificate obstructions. No administrative failure triggers scouts. Main alone selects and synthesizes; scouts become implementers excluded from independent final reviews.',
    'progress_aware_assessment_admission': 'Cumulative assessment attempts remain historical accounting, not a lifetime research cap. An exact unfinished infrastructure-interrupted assessment may resume after reconciliation; an identical completed assessment cannot repeat without substantive new evidence. Attempts increment only after concrete stage admission, before spawn. No historical attempt is refunded and no proof, scope, or grade gate is waived.',
    'interrupted_assessment_resume': 'An identical typed reassessment request may resume an exact host-recorded interrupted final assessment after validated stopped reconciliation, while the exact unfinished stage remains eligible under the progress-aware policy. Historical attempt counts are retained and do not impose a lifetime limit. Completed or rejected assessments and changed candidate/evidence cannot use this exception. The host resumes the pending assessment directly; fresh comprehensive and final independent gates remain mandatory, with no new execution authority.',
    'typed_checkpoint_contract': 'Main can select a host-recorded full artifact through the typed checkpoint contract; it may explicitly request independent reassessment or choose an honest no-action checkpoint.',
    'scope_schema_precheck': 'Prospective final natural-language scope responses require exactly verdict, answer_kind, coverage, extra_assumptions, gaps, findings at the root. findings requires exactly source_fidelity, clause_completeness, definitions, premises, answer_direction, each a nonempty substantive string, with no additional keys such as verification_language. coverage entries require exactly clause_id, root, result, explanation; result is covered or gap and explanation is nonempty. verdict is PASS_FULL_SCOPE, fail or unknown; answer_kind is proof or counterexample; coverage, extra_assumptions and gaps are arrays. Deterministic structural and complete semantic checks run before Silver. No earlier malformed response is accepted by this schema description.',
    'scope_pair_protocol_recovery': 'Only eligible structural scope errors permit one replacement blind pair on identical original inputs and schema-only correction. Substantive rejection never authorizes such a retry.',
    'lossless_prompt_packing': 'The host supplies exact reversible evidence packing. The unchanged one-million-byte guard still rejects oversized future prompts; prior sizing does not certify unseen future outputs.',
    'explicit_migration_notice': 'The resumed main now receives this host-validated prospective infrastructure receipt in its continuation feedback.',
}
POLICY_FIELDS = ('main_response_contract_version', 'original_scope_review_count', 'internet_browse', 'models')
AUTHORITY = 'infrastructure_only_no_mathematical_or_acceptance_authority'
AVAILABILITY = 'main_may_request_fresh_independent_review'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def policy_binding(config):
    return {key: config.get(key) for key in POLICY_FIELDS} | {
        key: config[key] for key in ('nl_only', 'proof_document_version', 'lite_local_verification_version', 'parallel_route_scouts', 'assessment_protocol_epoch', 'campaign_phase') if key in config}


def confined(base, relative):
    if not isinstance(relative, str) or Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('notice evidence path must be confined relative path')
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError('notice evidence path escapes or is missing')
    return path


def validate_notice(notice, base, config, parent):
    required = {'schema_version', 'kind', 'parent_source_root', 'parent_manifest_sha256',
                'target_code_hashes', 'target_policy_hashes', 'target_runtime_policy',
                'changes', 'evidence', 'authority', 'availability'}
    if not isinstance(notice, dict) or set(notice) != required:
        raise ValueError('infrastructure notice requires exactly the typed schema fields')
    if (type(notice['schema_version']) is not int or notice['schema_version'] != 1
            or notice['kind'] != 'infrastructure_migration_notice'
            or notice['authority'] != AUTHORITY or notice['availability'] != AVAILABILITY):
        raise ValueError('invalid infrastructure notice kind or authority')
    if (notice['parent_source_root'] != parent.get('source_root')
            or notice['parent_manifest_sha256'] != parent.get('manifest_sha256')
            or notice['parent_source_root'] != config.get('continuation_parent')):
        raise ValueError('infrastructure notice parent binding mismatch')
    if (not config.get('code_hashes') or not config.get('policy_hashes')
            or notice['target_code_hashes'] != config['code_hashes']
            or notice['target_policy_hashes'] != config['policy_hashes']
            or notice['target_runtime_policy'] != policy_binding(config)):
        raise ValueError('infrastructure notice frozen target binding mismatch')
    if not isinstance(parent.get('files'), dict) or digest(json.dumps(parent['files'], sort_keys=True, separators=(',', ':')).encode()) != parent.get('manifest_sha256'):
        raise ValueError('infrastructure notice parent manifest is not canonical')
    changes = notice['changes']
    if (not isinstance(changes, list) or not changes or any(not isinstance(c, str) or c not in CHANGES for c in changes)
            or len(changes) != len(set(changes))):
        raise ValueError('infrastructure notice contains unsupported changes')
    evidence = notice['evidence']
    if not isinstance(evidence, list) or not evidence:
        raise ValueError('infrastructure notice needs audited evidence')
    kinds, paths = set(), set()
    for ref in evidence:
        if (not isinstance(ref, dict) or set(ref) != {'kind', 'path', 'sha256'}
                or ref['kind'] not in ('current_infrastructure_audit', 'historical_preflight')):
            raise ValueError('unsupported infrastructure evidence reference')
        name = ref['path']
        if (not isinstance(name, str) or str(Path(name)) != name or name == 'notice.json'
                or name.startswith('notice.json/') or name in paths
                or any(name.startswith(old + '/') or old.startswith(name + '/') for old in paths)):
            raise ValueError('notice evidence path is duplicate, noncanonical or collides with receipt')
        paths.add(name)
        path = confined(Path(base), ref['path'])
        if digest(path.read_bytes()) != ref['sha256']:
            raise ValueError('infrastructure evidence hash mismatch')
        report = json.loads(path.read_text())
        if not isinstance(report, dict) or report.get('status') != 'PASS':
            raise ValueError('infrastructure evidence must be a passing host audit/preflight report')
        if ref['kind'] == 'current_infrastructure_audit' and (
                report.get('target_code_hashes') != config['code_hashes']
                or report.get('target_policy_hashes') != config['policy_hashes']):
            raise ValueError('current infrastructure audit does not bind exact target source and policies')
        if ref['kind'] == 'historical_preflight' and report.get('model_dispatched') is not False:
            raise ValueError('historical sizing evidence must record no model dispatch')
        kinds.add(ref['kind'])
    if 'current_infrastructure_audit' not in kinds:
        raise ValueError('current independent infrastructure audit required')
    return notice


def load_notice(root, config):
    ref = config.get('infrastructure_notice')
    if ref is None:
        return None
    if not isinstance(ref, dict) or set(ref) != {'path', 'sha256'} or ref['path'] != 'infrastructure-notice/notice.json':
        raise ValueError('invalid frozen infrastructure notice reference')
    path = confined(Path(root), ref['path'])
    if digest(path.read_bytes()) != ref['sha256']:
        raise ValueError('frozen infrastructure notice changed')
    parent = json.loads((Path(root) / 'continuation-parent.json').read_text())
    return validate_notice(json.loads(path.read_text()), path.parent, config, parent)


def feedback_notice(root, config):
    notice = load_notice(root, config)
    if notice is None:
        return None
    return {'receipt': notice, 'host_verified_receipt': config['infrastructure_notice'],
            'prospective_changes': {key: CHANGES[key] for key in notice['changes']},
            'authority_boundary': 'This is host-verified infrastructure status, not mathematical evidence or acceptance. '
                'All earlier schema/controller rejections and substantive findings remain valid historical evidence. '
                'A prior raw positive verdict alone never establishes controller acceptance. No report is retroactively repaired or promoted. '
                'Historical preflight receipts describe only their tested predecessor inputs. They do not prove current or future prompt sizes. '
                'Fresh review can be requested prospectively through the typed contract; the main independently decides whether it is useful. '
                'This notice neither schedules tasks nor supplies new execution approval, proof PASS, scope PASS or a grade.'}
