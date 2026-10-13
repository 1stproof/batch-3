# Reader-facing proof and exposition checks

Exam profiles retain this entire readability contract. No exam or novelty setting exempts proof structure, definition order, notation, explanations, reader reconstruction,
or repair of substantive readability findings.

Read this before the supporting-lemma plan and before release. It applies equally to
Claude and Codex, composition and refinement. The aim is a reconstructible argument,
not a shorter paper or a longer checklist.

## Recover the argument before editing it

For each retained result, assess and read its actual evidence: the Lean statement/proof where
available, the natural-language argument where not, and the cited source and use-site conditions.
Critical paths are auxiliary; Lite-only or partially formalized work needs mathematical judgment,
not exclusion from the paper or an invented completeness claim. Read dependencies
connecting hypotheses to conclusion. A build receipt or import list does not explain
the argument. In `04-proof-bridges.md` record the paper claim, exact Lean declaration or
natural-language/source location, actual proof and formalization status,
input objects and hypotheses, intermediate identity or inference, and the paper
location at which a reader can reconstruct it. Separate algebraic identities from
their identification with the intended bundle, class, map, orientation or coefficient theory.

A load-bearing bridge is an inference whose removal requires the reader to invent
a lemma, choose an unstated identification, or assume the target. Examples include
restriction-map calculations, spectral-sequence survivor/differential analysis,
injective descent, sign/normalization comparisons, and gluing over overlaps.
Being routine, short in Lean, or imported does not make such a bridge dispensable.
State it precisely and prove it in the body or a referenced appendix. A cited bridge
needs the exact source specialization and verification of its hypotheses at the use site.
A polynomial citation does not supply a geometric identification; vanishing of a
square does not establish vanishing of the class. A source package is not its application.

For every proof paragraph ask which established premise gives the next assertion.
“Compatibility gives”, “degree reasons”, “standard calculation”, and “details in the
appendix” need an equation, lemma, degree table, exact source specialization or
resolvable complete proof when they cross a bridge. An appendix repeating the
conclusion fails. Record uncertain steps as gaps, never replace them with plausible prose.

## Terminology before drafting

Build `07-terminology.md` before drafting and maintain it. For each concept record
the standard term, chosen notation, definition, first technical use and local scope.
Record aliases from Lean and the old paper which must not leak into prose. Prefer
ordinary mathematical descriptions to project nouns such as “certificate”, “adapter”,
“actual”, “literal” or “same-class mechanism”, unless the distinction is necessary
and explained once. These examples are not a blacklist of legitimate technical usage.
Different meanings of a symbol need clearly separated scopes and an explicit reset;
avoid overloading interacting objects. Do not name a one-use expression just to shorten it.
Claimed standard terminology needs field usage; genuinely new constructions may be
named with a definition and an explanation of their role.

## Dependency order and fresh-reader audit

Use `reader-facing-paper.md` as guidance for the writer and source-aware auditor, not as extra
context for the isolated final reader. Identify concrete reader obstacles
in bridges, source applications, figure relations and repetitive prose; do not demand workflow
diaries, decorative figures, or arbitrary cuts. Necessary mathematical limitations remain explicit.

In `02-reader-route.md` record each section's question, previously introduced
prerequisites, conclusion and link to the next section. Supply transitions when
objects, coefficients or proof mechanisms change. Define auxiliary spaces and maps
before technical use. Understandable introductory previews may precede full definitions.
Cross-reference standing setup without hiding public hypotheses under “claims only”.

Also check section purpose and level of detail: contribution summaries should state achievements,
background should explain a relevant idea, and passages about use should not restart construction
history without a reason. Locate abrupt shifts, redundant explanations, or confusing mixtures of
prior theory and new work. Explain the actual reading difficulty; do not demand shortening or
reorganization when the text already works, or remove qualifications needed for accuracy.

Apply the first-encounter check in `mathematical-writing.md` to what the intended reader can
understand at the introduction. For a judgment about local purpose or a definition's conceptual
role, locate the exact introductory passage and cite its explanation, or spell out the short
inference available there. If neither suffices, identify the missing objective or unexplained
consequential branch or term and the concrete obstacle it creates for that reader. Do not credit
a later proof or the reviewer's nontrivial reconstruction as an explanation supplied locally.
Routine or transparent material, including an immediately interpreted formula, needs no added
preamble; do not duplicate adequate explanations. Keep a preference for more orientation separate
from a required defect unless a concrete reader obstacle warrants repair.

Near the end, after a complete draft and before final preservation/release, run two sequential
feedback-and-revision cycles. In each cycle dispatch a new fresh-context Astra reader who
has not written or audited the manuscript. Use distinct readers for the two cycles. Give only
the final output `.tex` as the sole scientific document input, plus the fixed neutral
exposition/attribution rubric as instructions and a beginning-to-end reading task.
All needed manuscript content and bibliography must be in that TeX; unresolved external
includes or bibliography are not silently omitted. Do not supply project memory, proof maps, prior verdicts, author rationales
or intended repairs. Require locations of undefined objects, notation collisions,
missing inferences, abrupt transitions and unfulfilled promises of explanation.
Record actual identity, fresh-context provenance, guideline and manuscript hashes and located,
separate exposition and attribution findings for each round. The writer records each response, the actual repair,
or a substantive reason for a no-op; optional advice is not an instruction to change the mathematics.
Round two reads the version after round one's revisions, without seeing round one's feedback.
After the second revision obtain a hash-bound verification, which may be a reread by the second
reader. This verification checks the repairs and regressions, not a third routine polishing round.
Do not invent independence or PASS when fresh dispatch is unavailable. Two rounds complete the
scheduled editorial work, but any remaining substantive defect blocks release. Preserve all
first-pass reports, revision dispositions and final verification; see `two-round-review-runtime.md`
for `08-reader-rounds.json`. These two cycles supplement, not replace, the mathematical audit.

Separately, an evidence-aware mathematical auditor checks proof bridges and exact preservation,
using Lean where available and independently reviewing natural-language reasoning where not.
This reader evaluates reconstructible exposition and attribution visible in the paper, without
re-running the existing correctness/faithfulness workflow. Report an apparent mathematical
problem if encountered; never conceal it. Lean is an internal auxiliary by default: do not
demand verification prose or formal artifacts when the paper makes no such claim. Missing
external provenance for an explicit claim is unverified, not automatically false mathematics.
Do not add journal-novelty requirements,
examples, or stronger theorems just to obtain approval. Do not invent numeric Batch 3 scores.
Original-problem coverage and source/build verification belong to separate source-aware audits.
Reader approval is not mathematical certification; semantic approval is not evidence
of readable exposition. Both are needed. Machine sidecars may bind these actual reviews
to parsed units, but must not claim the reader received author-side maps or reviewed
parser identifiers they were never shown.

## Compression is optional; review is mandatory

Complete and audit the argument before deletion. Use the preservation recovery ledger.
For every omission record what readers use instead; “elementary”, “boring”, or “too long”
alone is insufficient. Never delete a load-bearing bridge. Moving it requires a forward
reference and a complete appendix proof, not another compressed restatement.
Size deltas are diagnostic, not targets. Unchanged or longer text is acceptable with
specific proof/exposition justification and independent review, within any supplied hard
page limit. Follow the page allocation and compiled-count checks in
`mathematical-writing.md`; a size justification cannot waive that limit. Do not move useful
arguments merely to force shrinkage. Statement locks, source checks, consumer accounting
and semantic audits remain mandatory. Writing does not upgrade research grades.

## Runtime evidence sidecar

For the two-cycle workflow, bind this sidecar's first-pass and final-reread records to the
second round reader. Retain round one's report separately in `08-reader-rounds.json`.
For historical schema-1 records only, the legacy field `manuscript_only` permits the writing guideline and bibliography, but excludes
project memory, author-side maps, prior feedback and intended repairs. It does not mean the
required guideline was withheld. New schema-2 records require the single-TeX contract in
`two-round-review-runtime.md`; never relabel a historical broader-context read as TeX-only.
The two-cycle release check runs at preservation/final, not
as a prerequisite for drafting or early terminology work.

After the real reviews, main writes `07-reader-audit.json` in the recorded work directory.
Do not create a passing template before review. `paperctl gate` requires this evidence at
`terminology`, `preservation`, and `final`; release audit checks it again. A preliminary
audit can run without it before those gates pass. Use this shape (angle-bracket values
are documentation placeholders, never acceptable evidence):

```json
{
  "verdict": "PASS",
  "reader_id": "<actual fresh reader>",
  "writer_ids": ["<every manuscript writer>"],
  "proof_auditor_id": "<separate independent semantic reviewer>",
  "fresh_context": true,
  "manuscript_only_first_pass": true,
  "first_pass_report": {"path": "08-fresh-reader.json", "sha256": "<file SHA-256>"},
  "proof_audit_report": {"path": "08-proof-audit.json", "sha256": "<file SHA-256>"},
  "source_tree_sha256": "<current inventory source_tree_sha256>",
  "read_order": ["<current inventory reading_order entries, in order>"],
  "pre_shrink_sha256": "<05-pre-shrink-inventory.json file SHA-256>",
  "findings": {
    "sequential_read": "<actual reader findings and disposition>",
    "proof_bridges": "<actual independent semantic findings>",
    "terminology": "<actual terminology and notation findings>"
  },
  "proofs": [{
    "unit_id": "<current proof unit>",
    "bridges": [{
      "claim": "<load-bearing inference>",
      "justification": "<how the manuscript establishes it>",
      "location_unit_id": "<live manuscript unit containing the explanation>"
    }]
  }],
  "proof_preservation": [],
  "terminology": [{
    "concept": "<concept>",
    "term": "<chosen term>",
    "defining_unit_id": "<live introduction containing that term>",
    "status": "standard",
    "evidence": {
      "path": "<local source or recorded search evidence>",
      "sha256": "<file SHA-256>",
      "locator": "<specific passage or search finding>"
    },
    "rejected_variants": ["<unwanted synonym, if any>"]
  }]
}
```

Paths in evidence records may be absolute or relative to the work directory. Obtain the
current inventory with `paperctl inventory OUTPUT.tex --json`. Main binds the actual
reader's recorded traversal to `reading_order` **after** the unprimed reading; it does
not send this inventory, proof map, or preservation ledger to that reader. The separate
proof auditor reviews those maps against the manuscript and available mathematical evidence,
using Lean when present and checking natural-language arguments where not. Their identity must
differ from the fresh reader and all declared writers. Preserve the actual first-pass
report even when it finds defects; repair and record a fresh final-version reread rather
than changing a failed finding into an invented pass.

The two reviewer references point to **typed JSON records**, not prose files whose hashes
could disguise a failed or outdated review. Each contains `reviewer_id`,
`source_tree_sha256`, `verdict` (`PASS` or `FAIL`), `unresolved_findings` (a list),
substantive `findings`, and `provenance`. The first reader's provenance is
`{"kind":"fresh","manuscript_only":true}`; the proof auditor's is
`{"kind":"independent-proof"}`. Identities must match the sidecar. Approval requires
`PASS`, an empty unresolved list, and the **current** manuscript tree hash.

The first reader may instead have found defects in an earlier version. Preserve that
record and add `final_reader_report: {"path":"08-reader-reread.json","sha256":"..."}`
to the sidecar. Its identity must be the same reader, its approving snapshot must be
current, and its provenance must be
`{"kind":"reread","manuscript_only":true,"prior_report_sha256":"<first-pass file hash>"}`.
Without this linked passing reread, a failed or stale first reading cannot approve.
Actual detailed Markdown reports may accompany these reviewer-authored JSON records;
never change reviewer verdicts or snapshot claims merely to satisfy the gate.

`proofs` covers every current parsed proof exactly once. An empty `bridges` list needs
a substantive `no_bridges_reason` backed by the independent proof review; “routine” or
an empty list is not evidence that no load-bearing bridge exists. `proof_preservation`
covers every removed or normalized-content-changed frozen proof exactly once, with:

- `original_unit_id`, `reason`, `disposition: "preserved"`, and a live proof
  `replacement_unit_id`; or
- `original_unit_id`, `reason`, `disposition: "cited"`, and `citation_key` present in
  the manuscript, with the separate source-registry and specialization checks still required; or
- `original_unit_id`, `reason`, `disposition: "omitted_nonessential"`, and
  `load_bearing: false`, justified by the actual independent review.

Terminology covers explicit definitions and every definition-ledger concept, plus prose
concepts the reviewers identify. `status: "local"` additionally needs `rationale`
explaining necessity and the recorded terminology search. `notation` is optional. Reuse
across concepts requires a different explicit nonempty `notation_scope` for every use;
an unscoped or repeated-scope collision fails. The semantic reviewer must verify that
those scopes really are separate and that the manuscript signals each reset. Rejected variants must be absent
from the normalized manuscript; do not list legitimate quoted or explicitly contrasted
terms as globally rejected variants. Evidence and substantive findings must describe
actual work, not merely satisfy minimum string lengths.

For unchanged or increased length, run
`paperctl shrink-stats --state WORK/00-run-state.json --semantic-justification "SPECIFIC REASON"`.
This records `semantic_justification` in the shrink report; it does not waive bridge,
statement, source, coverage, independent-review gates, or a supplied hard page limit.
All size measurements remain
honest even when the correct editorial decision is to retain or add explanatory text.

These checks validate hashes, declarations of identity, parsed locations, evidence
presence and census coverage. They cannot authenticate fresh memory, prove that a
reader saw only the supplied manuscript, discover every prose-only concept, or certify
mathematical truth. The TeX inventory is a conservative parser, not a full TeX expansion
engine. Genuine independent reading and evidence-aware mathematical review remain mandatory; a
machine pass or an unsupported bridge-free declaration cannot replace either.

## Located terminology and compression feedback

In the existing reader/referee rounds, explicitly locate undefined academic terms,
ambiguous or ad-hoc labels, and omitted key hypotheses, inferences or proof bridges.
A useful newly introduced construction is legitimate when its definition, role and
scope are explicit. The author should reconsider a challenged invented label: use
an actually equivalent standard term where supported, otherwise a precise descriptive
expression, or remove an unnecessary name. Do not defend a label merely because it
appeared in an earlier draft, invent evidence of standard usage, or change mathematics
to fit a fashionable term. This does not require a new search for every word.

Balance compression with explanation. Restore a needed step from the preserved raw
or pre-shrink manuscript when the detailed source supports it; keep a real gap explicit
when it does not. Remove redundancy and unrelated process history, not the important
argument. Useful additional detail is appropriate within the page limit. These checks
belong to existing rounds and existing author dispositions; they add no review round,
keyword ban, automatic acceptance or new scientific input for isolated readers.
