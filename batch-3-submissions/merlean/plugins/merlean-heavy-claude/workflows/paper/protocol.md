# Gated paper protocol

For exam writing, `workflows/paper/exam-mode.md` governs novelty and human literature waits.
All polishing, compression, readability, page-limit and release checks below remain required.

Read [reader-proof-quality.md](reader-proof-quality.md) for the shared proof reconstruction,
terminology and independent fresh-reader contract supplementing these gates.
Read [mathematical-writing.md](mathematical-writing.md) for evidence assessment and the
editorial priorities governing both providers, including Lite-only and partial-Lean projects.
Apply [reader-facing-paper.md](reader-facing-paper.md) at the existing planning, drafting,
revision and audit stages; it changes presentation without weakening mathematical preservation.

## Artifacts and gates

### 0. Preflight and baseline lock

Create `00-run-state.json`. In refine mode also create `00-baseline-inventory.json`,
`00-baseline-source.sha256`, `00-main-results-lock.json`, and both JSON/Markdown coverage ledgers.
Inventory sections, statements including unlabeled ones, definitions/notation, displays, proofs,
figures/tables, citations, footnotes, includes, and substantive prose. Freeze each baseline main
result's exact environment, label, statement, hypotheses, quantifiers, constants, scope, and
conclusion. Gate: source hash frozen, output exclusive and absent before initialization, source and
output are not aliases.

The output inode is reserved. If a legitimate editor uses an atomic save, adopt the new regular,
single-link inode with `paperctl claim-output --state WORK/00-run-state.json` before continuing;
never claim an unexplained replacement.

### 1. Evidence assessment and auxiliary critical path

Deliver `01-evidence-assessment.md` before interpreting a graph: selected statements, public
assumptions, available evidence, proof status, formalization status/recorded grade, and gaps.
Inspect natural-language proofs when Lean is partial or absent. A Lite result is not rejected
for lacking Heavy certification, and a passing Lean build does not prove semantic completeness.
Never claim a stronger proof or verification status than inspected evidence supports.

Deliver `01-critical-path.md`: theorem-grade DAG, separate defense artifacts, all tied deepest paths
to selected terminals, one-line statements, recorded grades where available, and hypothesis surfaces. Record
the edge source: Mem0-g, dependency-browser JSON, certificate embeds/axioms, or ledger delivery.
For every selected result, also record its full ancestor closure and induced formal edges; longest
paths are navigation aids, not substitutes for the dependency cone. Module-import ancestors are
an overapproximation, not a declaration-exact proof census. When no useful graph exists, record
that limitation and derive the argument dependencies from the available evidence. Freeze available graph hashes and both
the dependency and reverse-consumer maps. Gate: verify grades and hypotheses against actual
certificate/audit files where applicable, and the actual mathematical arguments in every case.

### 2. Empty framework

Deliver compilable `02-framework.tex` appropriate to the argument and readership; no fixed
Verification/Outlook/appendix template is compulsory. In refine mode add a map
from every baseline section/topic to its planned destination. Gate: isolated clean compile and no
orphaned baseline topic.

### 3. Main results, novelty, theme

Choose a coherent set of results (2–4 clusters is a heuristic, not a quota). Novelty assessment
defaults off: record `NOT_REQUESTED`, skip novelty searching, and apply [references.md](references.md).
Targeted relevance search and primary-content reading remain mandatory regardless of novelty.
Preserve and audit known input credit, verify the important citations actually selected, and
record justified exclusions. No citation count is prescribed.
Correctness, not novelty, determines exam success. Only when assessment is enabled, reuse a dated novelty record, then
use available permitted retrieval to search arXiv from that date through today. If access or
evidence is insufficient, use the autonomous `NOT_ASSESSED` path in [references.md](references.md)
without a human authorization/download wait. Never infer search completion from failed access. Confirm closest hits and inspect source TeX, not search
snippets. Record `CLEAR`, scoped `ADJACENT` with a delta sentence, or `COLLISION`. Decide a
field-standard title and three-sentence theme. Deliver `03-main-results.md`. In compose mode also
lock each result in `03-main-results.json` with a stable mathematical `result_id` (and graph
node when available), body label, normalized statement
hash, complete hypothesis surface, `CLEAR`/`ADJACENT` or independently audited `NOT_REQUESTED`/`NOT_ASSESSED` novelty status, and evidence.
The latter requires no priority claim, recorded retrieval limits and no unresolved proof/credit
dependency; it does not certify novelty. Gate: no unresolved
collision and one-sentence through-line. In refine mode the main-result lock cannot be demoted.

### 3.5. Preserve the raw mathematical reconstruction

Before editorial selection, rearrangement or compression, save `paper-raw.tex`: the full
natural-language argument supported by the assessed evidence, with all selected statements,
used hypotheses, essential intermediate results, intended-object identifications, source
specializations and unresolved gaps. Use Lean where available, not as the sole authority.
Preserve a faithful account of Lite proofs or incomplete formalization without claiming Gold.
Missing mathematical arguments stay explicitly incomplete, not silently promoted to assumptions.

The raw draft is separate from the author's approved scope baseline and from the later
pre-compression freeze. An independent fidelity audit checks the actual reconstruction and
its mathematical qualifications and evidence status records. Final prose need not repeat internal
status labels or process history when the mathematics is preserved and the history remains in
sidecars. Its approval means honest representation, not that all research gaps are
closed. Freeze the root and all dependencies with `paperctl freeze-raw`, then use
`paperctl start-from-raw` to initialize the editable version. Keep original raw and frozen
copy unchanged. Follow [raw-checkpoint.md](raw-checkpoint.md) for the command/evidence contract.
If reconstructing after a historical run failed to save raw, label it retrospective with its
actual date and evidence. Never rename a polished paper and call it the original raw draft.

### 4. Proof-dependency presentation and supporting lemmas

Work in evidence files and Markdown during this planning stage, after raw preservation; do not
edit frozen raw or candidate TeX. Use the available proof dependencies in `01-critical-path.md`
and the evidence assessment (including natural-language results) and `04-lemmas.md`
as the reader-facing dependency plan and recovery ledger. Before editing TeX also prepare
`04-proof-bridges.md`, `02-reader-route.md`, and the initial terminology ledger. Include the
proof-first page allocation from `mathematical-writing.md` in that reader route when a limit
applies; record its source and counting rule without changing selected or locked scope.

Give every considered node one action: `KEEP`, `SPECIALIZATION_OF`, `INLINE`, `OMIT_ELEMENTARY`,
`OFF_PATH_SUMMARY`, or `OFF_PATH_LEDGER_ONLY`. Record its formal ID and source, normalized statement,
formal dependencies and consumers, presentation dependencies and paper consumers, replacements,
rationale, and recovery anchor. A direct specialization may be collapsed only when a placeholder-
free Lean witness, where formalized, or an independently checked explicit mathematical application
proves it by instantiation of the retained general result without another
theorem-grade ingredient. Selected and locked results are always `KEEP`.

Map every old live paper consumer of a collapsed or omitted unit to a surviving replacement, then
recompute the reverse presentation-consumer map. Formal edges remain frozen. If an explicitly
authorized Lean edit changes them, invalidate this and every later gate, rebuild Lean, regenerate
the formal graph, and record the old/new edges before continuing. Gate: the full cone is covered,
the presentation DAG is acyclic, every consumer resolves, every omission is recoverable, every
formalized specialization witnesses compile without placeholders/new axioms and unformalized
ones are explicitly reviewed without a grade claim, and no TeX changed in this
stage.

### 5. Organize and draft

Draft only the new/versioned TeX, plus appendix and bibliography files if split. Census explicit
and prose definitions, standing constraints, macro/declaration commands, and notation. Introduce
each before technical use in expanded reading order; allow clear previews and concise reminders.
Shared notions have an authoritative definition and explicit local scope. Explain or cite standard
steps accurately. Keep core arguments visible and place supporting work according to reader needs,
not length alone. Factor shared notions only when strength is unchanged. Maintain the
reference registry. Gate: definition census, coverage ledger, citations, summary-strength independent
audit, and isolated clean compilation all pass.

### 5.5. Compression and shrink gate

After the complete draft passes, run `paperctl freeze-shrink --state WORK/00-run-state.json`.
This compiles the draft and freezes the pre-shrink TeX inventory, bytes, and page count. Compare
that measured count with the applicable cap and planned reserve before polishing; revise the
allocation and flag a near-limit draft in `02-reader-route.md`. Then classify every mathematical unit:

- `CORE_INLINE`: original/significant mathematics kept in the body.
- `IMPORTANT_BODY_APPENDIX`: important routine statement stays in the body; proof moves.
- `CITED`: standard/published result stated as needed and cited, without reproof.
- `LEDGER_ONLY`: genuinely reconstructible and unnecessary for the reader; remove from TeX but
  preserve the verbatim raw TeX (including comments and formatting), normalized statement and both
  hashes, source, old/new consumers, and rationale in
  `05.5-deleted-steps.md`.
- `AUDITED_STYLE`: a frozen proof whose presentation is rewritten without changing its mathematics.
  Record the replacement proof label or unit id, source, consumer, rationale, and two independent
  semantic `PASS` audits. Never apply this class to a theorem-like statement.

Never classify a main result, scope condition, caveat, consumed definition, or required logical
interface as `LEDGER_ONLY`. For `IMPORTANT_BODY_APPENDIX`, preserve the body statement and stable
label; add a body reference to the appendix proof; give that proof a unique label and a back-reference
to the body statement. The shrink pass may move/delete proofs or whole classified routine units, but
every surviving theorem/lemma/proposition/corollary statement must remain byte-identical to the
frozen full draft. Gate: machine ledger complete, all live consumers replaced, both directions
resolve, and the Markdown archive is substantive rather than a vague note. Report net shrink but do
not delete merely to hit a target. Rerun the compression inventory if post-draft mathematical
material is added. Use `paperctl shrink-stats --state ...`; it compiles again and writes the
byte/unit/page and main-text delta to `05.5-shrink-report.json`. The delta is not a target.
If no safe shrink is possible, record specific proof/exposition reasons for retaining length
and independently review them. Unchanged or increased length does not fail this gate by itself;
proof loss or incomplete reader-facing derivations do. Retention or expansion must still fit any
supplied hard page limit; semantic justification never waives that separate delivery constraint.

When a direct specialization is removed, retain the general result as its target, archive the exact
specialized statement and the Lean witness where formalized or independently checked
natural-language application otherwise, and record complete old consumers, new consumers, and their
mapping. Every old live consumer must resolve to the retained result or another surviving unit.

### 6. Final matter

Write the abstract last (at most 200 words): through-line, main results at weaker-or-equal strength,
and necessary mathematical scope. Do not require a Lean verification clause; Lean is normally
an internal auxiliary tool. Confirm title. State outlook items as questions with what is
known and provenance. Gate: abstract and section summaries pass a theorem-by-theorem strength audit.

### 7. Terminology, notation, and layout

Deliver `07-terminology.md`: concepts, selected technical terms and notation, justified local names,
source aliases and scope. Review occurrences by meaning, not global substitution; resolve
one-symbol/two-object or two-symbol/one-object conflicts. Gate: grep and independent semantic audits find no
unresolved synonym or notation collision.

Only after the proof plan, applicable Lean checks, compression, definition census, and terminology checks pass,
freeze a pre-layout inventory and apply layout as a presentation-only pass. Preserve a supplied
journal class; otherwise use a standard mathematics-journal class with approximately `0.85in`
margins and never less than `0.75in`. The pass may change only the class and ordinary geometry,
font, header/footer, and float settings. It may not change mathematical units, declarations,
definitions, notation, labels, references, citations, or includes, and it may not use tiny type,
condensed line spacing, negative spacing, scaling, cropping, or forced overlap.

### 8. Release

Complete the two sequential fresh-context Astra single-TeX reading/revision
cycles in `reader-proof-quality.md`, and verify the second revision before release auditing.

Recheck the baseline hash. Complete every coverage disposition. Audit locked main results. Verify all
reference-source/BibTeX records. Compile clean in isolation and recount the final PDF after all
reader repairs and layout edits; report the measured count against any applicable cap and counting
rule. Obtain two independent auditor PASS verdicts.
Make path-scoped local checkpoints; push only explicitly authorized repository/artifacts. Report title, main results, reference count,
pages, open items, output path, and baseline hash.

After each earlier gate passes, make its path-scoped local checkpoint before opening the next gate
when the project is a Git worktree. At release, update the campaign dossier's repair-record appendix
with “paper vN drafted,” then make the final path-scoped checkpoint. Never stage unrelated changes.

## Failure discipline

Repair and rerun a failed gate before proceeding. When novelty assessment is enabled, a later collision reopens Stage 3; with it disabled,
record overlap and correct any misleading priority or credit without requiring originality. Record
user-authorized deviations in the relevant artifact. Never reinterpret a failed check as a pass.
