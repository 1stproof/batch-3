Read `<PLUGIN_ROOT>/workflows/common.md` and the **Original-problem completion gate**
in `docs/trust-and-instantiation-gates.md` first. This is an internal independent
interface reviewer, not an additional public agent or a proof-implementation worker.
For this gate, GPT/Codex requires **`gpt-6-astra`** and Claude requires **Fable**.
Resolve Fable to the actual model ID exposed by the Claude host; this repository does not
invent a universal Fable ID. These are requirements, not default suggestions. Sol or Opus
implementation workers cannot substitute. If the required reviewer model is unavailable,
leave original-scope completion blocked and report the limitation; do not silently downgrade.

## Task and independence

The submitter owns this gate: it supplies the exact current candidate, arranges this
independent review, resolves findings, and checks the result again before claiming full
completion or submitting a complete answer. The reviewer must be a different actor from
all implementers of the reviewed result, with an honestly recorded fresh review context.
Do not accept a requested verdict, an implementer's self-assessment, or a renamed actor
label as evidence of independence. If the host cannot provide independence, return
`unknown`; a provisional self-check may guide work but cannot clear the gate.

The final original-question conformity gate defaults to **two independent reviewers**.
Commission two fresh review contexts on the same immutable original source, current final
answer, theorem interfaces, definitions and evidence. Neither reviewer sees the other's
report or conclusion before returning its own. They must be distinct from each other,
the submitter, every implementer, and the proof and grade reviewers. Both reports must
individually return `PASS_FULL_SCOPE` with complete current bindings and no gaps or extra
premises. A missing, repeated, stale, failing or uncertain report blocks completion; do not
choose the favorable opinion or turn disagreement into a majority/aggregate pass. Preserve
both reports and route all findings to the responsible main. A relevant candidate change
requires a new independent pair for that version. Single-review advisory or preacceptance
scope checks are advice only and cannot satisfy this final gate.

## Inputs

- The frozen original request/problem text, its provenance, exact locator and content hash;
  the original source version must be separate from the selected research milestone.
- The complete original answer criterion and an explicit list of its clauses/faces.
- Source kind: natural language, Lean 4, or mixed. For Lean input, freeze the original
  declaration with its necessary definitions/imports/toolchain; check exact type coverage
  or an explicit proved bridge. For NL input, read the original words and independently
  derive the clause map. For mixed input, identify unresolved conflicts rather than select
  the easier source. All versions stay visible.
- The current main theorem statement(s), source revision and file hashes, and only the
  definitions and structure fields needed to understand their mathematical meaning.
- The identities of the submitter and implementers; previous findings with stable ids.
- If applicable, an independently sourced official Lean statement and the actual comparator
  result bound to its version. A locally authored `Challenge.lean` is a candidate
  specification; comparing a proof to that file alone cannot establish original scope.

## Review procedure

1. Read the original source first and state what would count as a complete answer. Resolve
   the intended domain, quantifier order, parameter ranges, boundary cases, all requested
   conjuncts/directions, exactness versus bounds, and existence versus classification.
2. Read the actual main theorem interface. Unfold necessary definitions, bundled fields
   and notation until its ordinary mathematical content is clear. Check for added premises,
   a restricted model/domain, a smaller parameter range, or a definition that assumes the
   answer. Do not infer coverage from a theorem name, build log, grade or PR description.
3. Map every original clause to the exact theorem clause or explicit logical implication.
   Record a concrete gap when the interface is weaker. A finite counterexample can completely
   refute a universal question; a single instance cannot prove a general positive claim.
   Kernel `decide` is valid evidence for an appropriate finite claim, not a scope defect.
4. Stop at the interface boundary: do not re-read full proof bodies or launch compilation
   for this review. Existing proof/kernel audits remain separate obligations. If a necessary
   definition or source is unavailable or the original wording is ambiguous, return `unknown`
   and identify exactly what is needed. Do not manufacture a defect to avoid uncertainty.
5. Bind the report to the original-source hash, exact current theorem/definition evidence,
   reviewed source revision, actor identities and every clause comparison. Return `PASS_FULL_SCOPE`
   only for complete original coverage; `fail` for an identified mismatch; `unknown` when
   the comparison cannot be completed. A narrowed milestone may be correct while this gate
   fails. Preserve its research value and attribution without calling the original solved.

## Return

Use the current gate's structured evidence schema and include human-readable findings:
original answer criterion; theorem interface summary; necessary definitions inspected;
one finding per original clause; exact gap or justification; reviewer/implementer provenance;
source and candidate version bindings; verdict; and what would resolve each remaining issue.
A `PASS_FULL_SCOPE` means interface coverage only, not proof correctness, novelty, eligibility or an
award. It becomes stale after a relevant source, theorem, definition or revision change.


## Executable evidence handoff

The runtime pass token is exactly `PASS_FULL_SCOPE`; explanatory fail/unknown reports must
not use that token. Run the existing shared CLI, not a new command:

```sh
<PLUGIN_ROOT>/scripts/audit-research-grade <DATA_DIR>/verification-manifest.json
```

To request this gate, the manifest must assert a full-completion trigger:
`question_status: "settled"`, `claim_scope: "full_original"` or `"original_problem"`,
`original_problem_completed: true`, or `submission_eligible: true`. Require the CLI output
**`Original-question scope: passed`**. A partial manifest can pass its grade audit while
printing original scope **NOT CERTIFIED**; bare `PASS` cannot clear this gate.

The manifest includes `provider` (`codex` or `claude`), `manifest_author`, the complete unique
`implementers` list, and hash-bound `{ "path": "...", "sha256": "..." }` references named
`original_problem` and `target_contract`, plus `original_scope_audits`, an array of at least
two hash-bound scope report references. Each report has its own reviewer and provenance.
`original_scope_review_count` defaults to 2; the final gate cannot be reduced below two.
A legacy `original_scope_audit` primary reference may be retained for compatibility, but
it cannot replace the required independent pair. Each reviewer differs from
the manifest author and every implementer. The review repeats the exact `implementers`
array; `implementer` identifies one member. The report's `reviewer_provenance` is a hash-bound
JSON reference containing `provider`, `reviewer`, `task_id`, `role: "original_scope_review"`,
`model_family` (`astra` or `fable`) and the actual dispatched `model` ID. Use real dispatch
provenance; those fields do not authenticate the host or make a self-review independent.

The `original_problem` JSON uses `input_kind` (`natural_language`, `lean`, `mixed`),
`source_kind` (`user_request`, `official_catalog`, `original_publication`, `official_lean`),
`origin` (an HTTPS source or `user-request:<id>`), `source` (a hashed text reference), the
verbatim `statement`, `required_clauses: [{id, text, source_excerpt}]` and
`unresolved_conflicts: []`. Lean/mixed adds `lean_target` with `declaration`, exact
`signature`, hashed `source`, `definitions: [{name, statement, source}]`, `toolchain` and
`imports: [{module, revision}]`. Mixed additionally preserves `natural_language` with its
own hashed `source` and verbatim `statement`.

The scope report binds `original_problem_sha256`, `target_contract_sha256`, and
`proof_snapshot_sha256` (SHA-256 of `json.dumps(roots, sort_keys=True, separators=(",", ":"))`
encoded as UTF-8). Its `roots` have `name`, exact `signature`, `signature_sha256`, hashed
`lean_file` and necessary `definitions`. It records `coverage: [{clause_id, root,
result: "covered", explanation}]`, `extra_assumptions: []`, `gaps: []`, `answer_kind`
(`proof` or `counterexample`) and substantive `findings` for `source_fidelity`,
`clause_completeness`, `definitions`, `premises`, `answer_direction`; mixed also requires
`mixed_consistency`. Lean/mixed uses `lean_comparison` with `mode` (`exact_type` or
`checked_bridge`) and both signature hashes; bridge mode also supplies its named reviewed
`bridge_root` and hashed verification evidence. If `proof_commit` is supplied, its full SHA
must agree between manifest and report; local content-hash review does not require a commit.

Original-scope references resolve inside the directory of the containing evidence file.
Existing Gold kernel-root `lean_file` references remain manifest-relative, not relative to
the kernel JSON file. The checker fails
closed for unsupported declaration headers; preserve the original source and provide an
explicit reviewed wrapper/bridge when appropriate, never rewrite the source as an easier
statement. Plan-level original-completion metadata uses an absolute hash-bound
`original_scope_manifest` pointing to this manifest. `src/original_scope.py` and its tests
are the maintained schema; this role does not generate semantic approval automatically.


## Natural-language candidates and final answer binding

The original input kind and candidate output kind are separate. A pure Lite prose
answer uses manifest and report `candidate_kind: "natural_language"`. It requires
`grade: "BRONZE"` or `"SILVER"` and an original `input_kind: "natural_language"`;
it cannot certify GOLD, formalization, or replace a Lean/mixed original's exact-type
obligations. Omitted candidate kind retains the existing Lean-root schema.

For a natural-language candidate, the manifest includes a hash-bound `final_answer`
text-file reference, resolved relative to the manifest. The report includes matching
`final_answer_sha256`. Its `roots` use:

```json
{"name": "answer", "statement": "The exact answer passage.",
 "answer_passage": {"start": 0, "end": 25, "text": "The exact answer passage."}}
```

Offsets are zero-based Python Unicode character offsets, with an exclusive end.
`statement` and `text` must equal that exact slice of the frozen final answer.
At least one root statement must exactly match `target_contract.target_statement`.
Existing `coverage` maps each original clause to one of these named roots;
`proof_snapshot_sha256` still hashes the complete roots array. All existing original
source, target-contract, substantive findings, implementer census and independently
recorded reviewer dispatch requirements apply unchanged. The reviewer must assess
whether each cited passage actually answers its original clause; a matching slice or
valid hash alone cannot establish mathematical equivalence or proof correctness.

Lean candidates may also supply `final_answer` and matching report
`final_answer_sha256`. Delivery controllers must call
`audit_original_scope(..., required=True, require_final_answer=True)` to require
current final-answer binding in either branch. This option does not dispatch a reviewer
or verify host independence. The independent review must read the complete final
answer, and substantive edits require review of the new version. Original-scope
approval remains separate from proof verification and publication authorization.

Each report also includes `review_input_sha256`, the SHA-256 of the identical scope-review
instruction and evidence packet before shared host policy framing. Its dispatch provenance
repeats this hash and supplies the actual fully composed `prompt_sha256`. Both hashes are
required; the actual prompt hashes must agree across the pair. Distinct reviewer/task/session
identities must come from actual fresh dispatches, not copied or renamed reports.

### Raw response for the natural-language pilot

When the host supplies and attaches the artifact bindings and dispatch provenance, return
exactly six root fields: `verdict`, `answer_kind`, `coverage`, `extra_assumptions`, `gaps`,
and `findings`. Use `PASS_FULL_SCOPE`, `fail`, or `unknown`; `answer_kind` is `proof` or
`counterexample`. Each coverage entry has exactly `clause_id`, `root`, `result` (`covered`
or `gap`), and a nonempty `explanation`. The `findings` object has exactly five nonempty
substantive strings: `source_fidelity`, `clause_completeness`, `definitions`, `premises`,
and `answer_direction`. Put verification-language concerns into the appropriate existing
finding and gaps; do not add a `verification_language` key. Do not invent host receipt,
identity or hash fields. The host appends its actual bindings without changing your judgment.

The host checks this structural contract before any Silver call. A malformed pair may be
replaced once by two fresh blind reviewers receiving the same original evidence and the same
schema-only correction. Every prior raw report remains preserved without acceptance authority.
An expressed substantive failure, uncertainty, extra premise, gap, or failed scope comparison
blocks this retry and returns to the main. Never select favorable reports across attempts.
A structurally correct pair must still pass the complete independent scope gate before Silver.
