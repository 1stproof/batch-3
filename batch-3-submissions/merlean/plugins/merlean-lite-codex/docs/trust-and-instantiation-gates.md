# Trust and intended-model gates

Lean's kernel checks the declaration that it is given. It does not decide whether the
declaration is the theorem that the research question asked for. In particular,
`#print axioms` does not list ordinary theorem parameters or proposition-valued fields of
structures. A theorem can therefore be axiom-clean while merely proving an implication
from the missing mathematics.

MerLean uses the following gates in every research runtime.

## Applying these gates in Lite

Faithfulness, explicit premises, intended objects and independent review apply in both
modes. They do not make every Lite ledger row a Lean task. For a natural-language Lite
argument, the exact definitions, use-site checks and dependency map may be established
in natural language and independently reviewed. Apply `workflows/lite-research.md` §L3
before requesting any Lean work: a selected local certificate needs faithful formal
interfaces and an audited transitive premise manifest, while accepted upstream facts
may enter as explicit hypotheses. Closing that manifest means accounting for their
mathematical evidence, not recursively formalizing all their proofs.

The completed Lean adapters and strict `/ref` source-boundary machinery described below
are mandatory for the corresponding formal certificate or Gold claim. They are not a
blanket prerequisite for Lite exploration, ordinary exact citations, or an accepted
natural-language step. Lite citations still require the exact source-to-ledger match and
use-site hypothesis audit. A selected certificate with an unresolved encoding or intended
instance must disclose that limitation and cannot be promoted by its clean axiom report.
Retain that evidence gap without turning it into an unbounded formalization project.
The original-problem completion gate remains mandatory for any complete-answer claim.

## Original-problem completion gate

Before either Lite or Heavy calls the original question `settled`, reports its full
formalization complete, or submits a complete solution, the **submitter** must obtain a
current independent source-to-interface review using `roles/original-problem-reviewer.md`.
This substantive original-target reviewer must be Astra (`gpt-6-astra`) on GPT/Codex or
Fable on Claude, with the real host-resolved model ID and hashed dispatch provenance.
It must differ from the submitter/orchestrator and every implementer; unavailable required
models block the gate rather than permit a silent fallback. The exact runtime pass token
is `PASS_FULL_SCOPE`. The role documents the existing `audit-research-grade` invocation
and the `original_problem` / `original_scope_audit` hash-bound evidence schema.
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

Freeze the original problem/request and complete answer criterion separately from the
working target and milestone contracts. This shared faithfulness gate applies to both GPT
and Claude Lite/Heavy runtimes, whether the authoritative input is natural language, Lean 4,
or a mixture:

- **Natural language:** retain the original words, locator/version and content hash; freeze
  an independent clause map for every quantifier, premise and requested conclusion.
- **Lean 4:** retain the supplied declaration and necessary definitions, imports and toolchain
  pins. Prove its exact type, or supply and audit a bridge that yields that original type.
  Matching an easier replacement declaration does not close the task.
- **Mixed input:** retain both sources and their relationship. A material mismatch in domains,
  assumptions or conclusions leaves faithfulness unresolved; do not choose the easier version
  and call it the original. Resolve the authoritative interpretation under the user's scope
  before allowing original-question completion.

Preserve their provenance and hashes. A partial
research goal, an author-written challenge, or a conditional theorem must not overwrite
that original reference, even when it earns its own valid research grade.

The reviewer reads the original statement, actual main theorem interface and necessary
mathematical definitions/structure fields. It compares domains, quantifiers, parameter
ranges, assumptions, all requested faces, and the logical direction of the answer. This
is a bounded interface audit, not a duplicate full-proof review or build. The submitter
supplies a clause-by-clause coverage map, but the independent reviewer must check it against
the source rather than approving its labels. Use an official Lean comparator where an
independently sourced official statement exists; record the precise reference and result.
Passing a comparator against a self-authored weakened statement cannot replace this gate.

`fail`, `unknown`, missing evidence, same-actor implementer/reviewer, or stale source or
candidate revision/hash blocks **original-question completion and complete-answer submission**.
Return failed or unresolved items to the submitter's repair queue with explicit gaps; retain
useful partial proofs, existing attribution and other workers' ownership. Re-run the gate
after relevant edits. Do not change the original target to manufacture a pass. A genuine
user-authorized change of question is a newly versioned scope decision, not retrospective
proof that the old question was solved.

For a natural-language original and a BRONZE/SILVER natural-language answer, the scope
manifest may use `candidate_kind=natural_language` with roots anchored to exact passages in
a hash-bound final answer. This does not satisfy Lean/mixed-input or GOLD obligations.
The reviewer role defines the schema. Campaign sealing requires the final artifact binding
for either candidate kind, plus a separate independent full-proof review of that same
artifact. Changing the final text invalidates those receipts. The ordinary scope checker
keeps legacy Lean manifests compatible unless final-answer binding is explicitly required.

A finite counterexample can settle a universal conjecture. A finite example, lower bound
or supporting lemma does not settle a general positive, asymptotic or classification problem
unless the original answer criterion requires exactly that result. The gate has no blanket
ban on `decide`, finite computation, imported credited proofs, or ordinary generic library
lemmas. Library work is judged against its actual authorized library target; translation-only
and editorial deliverables remain ungraded, and paper workflows preserve existing grades.

Lite may still honestly report BRONZE/SILVER partial research, and Heavy may grade an exact
conditional or supporting theorem under the existing rules. Neither may promote that grade
into original-question completion. This gate is necessary, not sufficient: it does not waive
kernel checks, proof audits, licensing/attribution or the destination's submission requirements.
The deterministic checker validates recorded evidence and version/identity bindings; it
cannot itself authenticate human/agent independence or decide mathematical equivalence.
The workflow requires the submitter to run it at completion/submission; this is not a Git
pre-push hook and does not intercept arbitrary remote writes.

## HYPOTHESIS FIREWALL

Every premise is classified transitively as one of:

- `ORIGINAL`: stated by the problem;
- `CONDITION`: introduced for the exact achieved conditional theorem, with status `declared`;
- `DERIVED`: proved from earlier rows/nodes;
- `CITED`: an exact external theorem with its use-site hypotheses discharged;
- `ASSUMED`: a residual premise not supplied by the problem and not yet proved;
- `REFUTED`: false or incompatible with the intended model.

`ASSUMED` premises must never remain proof-local or hidden. Either prove them, source-close
them at the strict boundary below, or freeze a new **conditional theorem face** in which each
one is a direct public antecedent. Every downstream result is then rendered “if these
conditions hold, then …”. A declared condition is not evidence that the condition holds for
the original intended object; it changes the scope of the exact theorem being graded.

`open-residual` and `declared condition` are disjoint states. An unexplained residual prevents
Gold. A declared condition may occur in conditional Gold only when it is frozen before proof,
enumerated in the kernel premise census, exposed as a direct binder rather than a hidden record
field, and propagated through every dependent public theorem.
An introduced condition must never be relabeled `ORIGINAL` or `closed`; its contract entry uses
`condition_premise_ids`, records why the scope was introduced, and remains visibly `declared` even
when the exact implication earns Gold.

Explicit typeclass binders such as `[AddCommGroup G]` are public structural context, not
logical premise rows.  They are nevertheless part of the trust census: schema-v2 contracts
must enumerate every such binder, in signature order, under `structural_binders`, and the
independent audit must explain the structural context.  Their proposition-valued law fields
are thereby universally quantified on the theorem face; custom structures or structures
that store a target-shaped fact still go through the interface and definition-independence
gates.

The contract also enumerates every remaining named non-instance parameter under
`data_binder_ids`. Heavy mode asks Lean itself to classify every binder type as `Prop` or
data, and requires the resulting ordered binder census to agree with the public-premise,
data, and structural lists. Proposition-valued instance binders are rejected; an unknown
custom structural class is not ambient context and must be expanded as a premise or audited
interface. Heavy mode also resolves the head structure of each binder type. Project-defined
structures are rejected unless an intended-model interface names the exact `lean_type` and
supplies its completed adapter; this prevents a target-shaped proposition from being smuggled
through a custom data record.

Mathlib's bundled `TopCat` spaces and `TopCat.Hom` continuous maps are trusted data
structures for this limited census purpose, like `LinearMap` and `AddMonoidHom`: they
package standard-library data and laws, not an intended model. A campaign-defined space,
fibration, or comparison package remains untrusted and requires an intended-model adapter.

The executable census stops after the binder prefix explicitly frozen before the result
colon. In particular, it must preserve a conclusion `¬ P` as the result proposition rather
than unfolding `Not` and misclassifying `P` as an anonymous public premise. This exception
is polarity-specific: a leading positive implication or `∀` after the result colon is a
hidden premise and fails Gold until moved into the named binder prefix. Heavy applies the
same runtime binder and result-shape census to every theorem-face root, not only the root
whose signature equals the frozen target.

## THEOREM-FACE CLOSURE

Every consumed mathematical premise must appear on the public theorem face, be an
`ORIGINAL` hypothesis, or be reached through a proved/cited dependency. Proof-only local
assumptions, proposition-valued structure fields, and definitions that encode the desired
conclusion are included in the transitive premise census. Definitions and constructors
must not make the target true by construction.

## CLASS-VS-CARRIER GATE

A claim that one distinguished class is zero is not interchangeable with a claim that its
whole carrier is subsingleton, that every class is zero, that the domain is empty, or that
the intended object is a zero/toy model. Any stronger replacement requires both a proved
implication or equivalence and proof that the stronger premise holds for the intended
object.

## INTENDED-MODEL GATE

A generic witness, one-point model, or zero construction establishes at most consistency
of an interface. Closure at the intended-model level requires an explicit adapter or
instance for the exact objects in the original question, with every residual field
discharged. For obstruction theory, record the stage, fibre connectivity, coefficient
system, primary/non-primary status, indeterminacy, and why the cited theorem applies at
that stage.

## STRICT /ref BOUNDARY

A classical result may remain at the proof boundary only as a direct theorem antecedent—never
as an unaudited Lean `axiom`. Its manifest entry must bind a hashed primary text under the
manifest-local `ref/` or `refs/`, an exact quote and locator, a notation map, and total
hypothesis/conclusion checklists marked exact. Two independent subagents must re-read the same
hashed source: one attacks source correspondence and one attacks use-site applicability. A
secondary quotation, approximate paraphrase, missing convention, or source absent from `ref/`
is `open-residual`, not a boundary result.

Even an exact source match reaches this boundary only as a last-resort cost decision. Heavy mode
must first record that the result is standard or well known, is not available in Mathlib after a
documented search, and resisted concrete proof/decomposition attempts. It may be deferred only
when formalizing the external theory would be disproportionate to the result's role in the
campaign. Novel, disputed, manuscript-specific, or merely inconvenient facts are never cited
boundaries. Cost never compensates for an inexact source or an undischarged source hypothesis.
Schema-v2 boundary entries therefore require a structured `formalization_cost` record.

When a family of cited operations and laws is naturally represented internally by a custom
structure, the question-level theorem must not take that structure witness as an ordinary data
binder and call the result conditional Gold. Expose the existence claim itself as a
proposition-valued antecedent, for example `hSource : Nonempty SourcePackage` or an equivalent
explicit `Exists`/conjunction, and select the witness only inside the proof. The boundary audit
checks this joint existence statement, flattens every component source id and hypothesis, and
checks compatibility of shared normalization, cup-product, and naturality data. It also requires
a manifest-local `source_closure` index that hash-binds every leaf packet and exact primary
excerpt, its locator and leaf checklist, and every compatibility edge. Its face registry must
equal exactly the manifest assumptions that reference the closure. Two independent joint-face
audits must each bind the complete component-boundary census and the complete edge set
(edge id, exact leaf endpoints, and shared datum); their reports may not be replayed across faces,
and their auditors must differ from the manifest author, Gold auditor, and source auditors.
Cross-campaign paths and composite summaries alone do not close the evidence graph. A cited source
package is not an intended-model interface and must not be registered as one merely to pass the
custom-structure census.

## Grade vocabulary

The only grades are `BRONZE`, `SILVER`, and `GOLD`.

- `BRONZE`: the natural-language ledger closes, subject to its disclosed trust base.
- `SILVER`: every triaged inference is Lean-checked. Parameterized certificates are
  reported as `SILVER (interface-certified)`.
- `GOLD`: the exact frozen public theorem—absolute or conditional—is proved or disproved
  end-to-end and passes the kernel, premise, source-boundary, faithfulness, and intended-model
  gates. Conditional Gold says only that the implication is Gold; it does not discharge its
  antecedents or settle the original unconditional question.

`CITED`, `CONDITIONAL`, and `OVER_INTERFACE` describe scope, never alternate grade tokens.
Any open residual, hidden condition, unmatched source boundary, or uninstantiated interface
not itself frozen as the exact conditional target prevents `GOLD`. Clean axioms are necessary,
not sufficient. Reports must separately record whether the original question is `settled`, a
`conditional_advance`, an `interface_lemma`, or `no_progress`, plus research value; a Gold
tautology is still no progress.

## Executable Gold evidence

`verification-manifest.json` schema version 2 binds a Gold claim to hashed evidence inside
the campaign directory: the frozen target contract and its source files, machine-produced
kernel/root evidence, every derived-premise Lean file, every intended-model adapter, the
definition-independence record, and an independent audit report. Premise, interface, and
theorem-face ids must agree exactly across the contract, kernel evidence, and manifest.
Missing arrays, arbitrary matching labels, plain booleans, and unresolvable declaration
names fail closed.

The heavy auditor generates its own Lean audit module; a manifest-supplied audit body is never
trusted. It rebuilds and imports the exact root module, checks the root at the frozen type using
a typed `example`, prints its axioms, and emits a Lean-environment binder census.
Metadata-only calls cannot award schema-v2 Gold. Source text, audit reports, and definition
independence use structured evidence; a declaration name in a comment, unrelated source file,
or content-free report fails.

Schema-v1 Gold is legacy/unaudited and is rejected by the active grader. Structured semantic
reports must bind the auditor id, target hash, question-status and research-value classifications,
and a nonempty finding for every required check. Boundary reports additionally bind the boundary
id, exact source hash, and public Lean binder. The runtime transcript's axiom set must equal—not
merely be a subset of—the axiom set recorded for the roots.

Plan-graph `add`, `update`, and JSON import may record BRONZE/SILVER metadata but cannot set
`verification_grade=GOLD` or `gold_audit`. Gold evidence is audit-controlled. Reconciliation
clears an existing Gold if its audited Lean source, manifest, or any transitively referenced
evidence digest is stale, or if the proof is no longer clean; compilation status never
manufactures a semantic grade. The target contract must bind the exact target plan node in
`plan_statement_id`. After a read-only Heavy `PASS`, persist the grade only with explicit offline
authority: `PLAN_OFFLINE=1 .../audit-research-grade <MANIFEST> --record-gold --plan-data
<PLAN_DATA_DIR> --statement-id <ID>`. The version-2 receipt freezes the complete manifest-local
evidence snapshot and resolved plan path so later reconciliation fails closed after
child-evidence tampering or receipt replay onto a different node or plan.

The public mode names are MerLean `-lite` (default, target SILVER) and `-heavy` (formerly
Lite off, target GOLD). Heavy may start directly on an existing proof/paper or Lean stub;
it creates the same target node and contracts without fabricating a prior Lite run.
Pure statement translation is an explicitly scoped Heavy procedure, not a graded proof.
The same engine and gates ship in both providers; a paper-writing run never awards Gold.
