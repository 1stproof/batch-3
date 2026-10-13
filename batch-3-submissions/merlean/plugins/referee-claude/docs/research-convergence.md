# Evidence-based research convergence

Convergence is the default research allocation rule, independent of exam mode,
provider, deadline or research grade. Once a promising coherent proof skeleton
exists, develop that candidate's necessary gaps, original scope, verification and
write-up. Pause unrelated parallel route exploration. Convergence begins before
a complete natural-language proof or comprehensive review exists. It never
turns a promising outline into an accepted proof.

## Operational state and admission

`src/pilot_convergence.py` maintains three phases:

- `exploring`: no promising skeleton has yet been retained.
- `converging`: a main-proposed explicit skeleton or independently reviewed
  mathematical argument supplies an anchor. Candidate revisions and different
  labels do not reset this phase.
- `reconsidering`: current independent evidence identifies a fatal mathematical
  defect, counterexample, failed key bridge or original-scope failure. Alternative
  research is available again; the failed outline and findings remain retained.

A candidate may supply `convergence_outline` with substantive `skeleton` and
`why_promising` strings and an `open_gap_ids` string array. This is a scheduling
proposal. It carries no proof, review, worker, certificate or acceptance authority.
A changed outline after an evidenced failure can begin convergence again; simply
resubmitting the failed outline cannot erase the reopening decision.

The generic `work_admission(state, kind=..., consumer_ids=..., reason=...)`
returns the decision and its exact basis. Necessary gap closure, scope,
validation and write-up remain available. Parallel route work during convergence
must map to the retained current obstruction and explain its contribution.
`scout_admission(state, tasks)` applies that contract to existing scout task IDs.
The Codex pilot checks it before launching a route portfolio or a research execution
worker, saves the decision,
and still requires the existing independent scientific-obstruction authorization.
Fresh pilots optionally allow main-selected portfolios of two to four distinct Astra
scouts. General user authorization permits advisory scientific alternatives without
inventing an independently established gap; it does not bypass convergence admission.
Main may omit scouts when a single route suffices. Once a promising skeleton exists,
parallel work must serve its current necessary gaps. Changing portfolio width or task
wording cannot buy another assessment of the same scientific census.
Research execution tasks name `consumer_ids` and explain necessity in `context`;
selected certificate tasks retain their independent exact L3 authorization. An allowed
convergence decision alone never authorizes a worker or new review.
There is no lifetime round limit, diversity quota or prescribed strategy rotation.
Other mode schedulers can use the same provider-independent admission API; the
module does not launch models or claim control over an external host scheduler.

## Preserve useful answers before certificates finish

The state keeps two distinct pointers:

- `best_reviewed_mathematical_candidate`: a comprehensive independent review
  establishes mathematical readiness without remaining mathematical findings or
  research-gap rows. An `INCOMPLETE` verdict with missing certificates can still
  bank this NL argument. The raw verdict remains unchanged, and scope
  qualification is explicit: unreviewed, advisory adequate/inadequate/unknown,
  or final audited original scope.
- `best_reviewed_original_candidate`: the banked argument also has the existing
  two-reviewer, independently audited original-scope evidence.

The first pointer is useful while certification or final scope remains open.
Neither pointer is a grade or release decision. Prefer a stronger independently
supported scope qualification; preserve the incumbent among equally qualified
candidates. Do not rank proofs by length, number of self-reported gaps, timestamps
or claimed grade. Exploring a conditional or broader theorem retains the original
answer and all its unresolved obligations. New adverse independent evidence can
remove a candidate's eligibility, but never deletes its record.

## Four deficits and scope decisions

Every exact candidate has separate `original_scope`, `mathematical`,
`certification` and `delivery` deficits, each `unknown`, `open` or `closed`.
`closed` describes only that recorded domain under its exact evidence; it is
never research acceptance. In particular:

- A faithful-encoding failure cannot become a mathematical refutation.
- A compiled certificate cannot close a mathematical or original-scope gap.
- Advisory scope adequacy guides a stable interpretation but cannot close the
  final original-scope obligation.
- Complete review-material delivery does not imply a favorable review.
- Main-supplied `grade`, `complete_claim`, review or scope fields grant nothing.

The host calls `observation` only after the existing domain validators. Review
observations require current independent completed host receipts, exact candidate
and original bindings, and immutable evidence hashes. Final scope additionally
requires both distinct reviewers and the existing deterministic scope audit.
A focused independent counterexample can reopen exploration without a comprehensive
review. A verified same-reviewer timeout recovery retains its actual resume flags
and host-bound original timeout receipt for scheduling evidence; it never becomes a
fresh final scope reviewer or changes final acceptance requirements.
`update_convergence` rejects stale bindings, altered evidence, duplicate scope
sessions and scope passes contradicting their reports. Receipt or scheduling
metadata changes alone do not reopen an identical scientific scope decision.
Each changed scope observation links the preceding decision; all remain archived.

## Auxiliary work and cost retriage

Auxiliary records identify a work ID, exact deficit consumers and expected
contribution. Local certificate modules automatically map their selected claim to
its ledger consumers and retain the exact complete module evidence digest. If
new auxiliary attempts leave the core deficits unchanged without an explicit new
value, the state raises `auxiliary_crux_unchanged_reconsider_value`. This asks the
main to reconsider value; it does not manufacture a mathematical impossibility.
Useful negative research and failed approaches remain separate durable evidence,
without being mislabelled gap closure or renewing paid-review eligibility.

Stopped local modules produce `independent_cost_feasibility_retriage` entries with
the exact module hash and `obligation_waived: false`. Existing local module review
still requires every prior obligation and finding to be accounted for. Cost alone
cannot deselect a necessary certificate; accepted substantive replacement or
non-reliance evidence must justify any change. Natural-language research remains
available after a module returns to main.

## Persistence and compact context

The main owns `research-convergence.json`, an atomic index into
`convergence-archive/`. Individual candidate bodies, observations and research
records are immutable content-addressed artifacts. State manifests reference
those records; revising a deficit does not duplicate a large proof body.
Restoration verifies every referenced record and the reconstructed state hash.
The complete record archive must travel with a continuation.

`compact_context` sends the phase, qualified best-candidate pointers, four deficit
summaries, current triggers, certificate retriage and archive counts. It does not
recursively embed past proofs and review packages. Full exact evidence stays
available on disk. Existing candidate-catalog, archive-retrieval, finding-history,
review provenance, scope and grade mechanisms retain their authority.
