# Referee workflow

Read [referee-standing-rules.md](referee-standing-rules.md) first. It controls comment
selection, mathematical criticism, and review proportionality throughout this
workflow. Internal evidence collection does not impose a quota of report items.

## Scope and project

Resolve the exact submission/version, `PROJECT_DIR`, `REPORT`, and, for TeX,
`REPORT_RENDERED`. Prefer the existing layout. For a new review, use the
manuscript ID under the user's requested review directory; keep reference
sources, audit evidence, and the report with that project. Do not relocate an
existing manuscript or formalization merely to match a template.

Keep `PROJECT_DIR` outside the maintained MerLean source and installed/generated
packages. Resolve `<PLUGIN_ROOT>` from the entrypoint, independently of the
working directory. Read supporting files and run helper scripts from that root;
write manuscripts, ledgers, Lean certificates, references, and reports only into
the review project or its explicitly selected external Lean workspace. A review
repository should point to this workflow, not maintain another copy of it.

Distinguish a new review, a reassessment of an existing report, and an explicit
full-formalization request. Preserve user limits. The main agent owns the
report and final judgments; independent reviewers return evidence and advice.

## 1. Establish the evidence

Read the submission, including the relevant equations, figures, tables,
appendices, and supplements. Confirm the matching arXiv version if one is
used. Record source hashes and material version differences. Reuse verified
local source copies; retrieve primary material only where needed. Extract
archives safely without path traversal.

For an existing report, preserve its pre-edit version once and inspect the
related audit/verification notes. Revalidate old concerns against the paper.
A concise decision record is sufficient: concern, manuscript location,
current evidence, retain/withdraw/narrow, reason, and report location if kept.
A resolved, low-value, routine, stylistic, or unsupported concern may be omitted
without carrying its full substance into another report item. Historical
notes do not establish that a criticism is true.

## 2. Assess mathematics and existing Lean

### Default MerLean Lite verification

This manuscript-review adaptation controls task scope and report selection;
Lite's substantive evidence, source/premise fidelity, targeted Lean triage, and
honest-limit requirements remain mandatory. Reading a manuscript without editing
it does not exempt a substantive referee review from this verification pass.

For a new substantive review or a mathematical reassessment, execute
`<PLUGIN_ROOT>/workflows/merlean-lite.md` and its required
`<PLUGIN_ROOT>/workflows/lite-research.md` procedure in the current host, using
the same provider adapter and shared contract. This is an actual workflow
handoff: reading these files or printing the selector JSON alone is not a
verification run. No separately installed Lite plugin is needed; these internal
files and the shared runtime are included in the Referee package.

Bind its documented inputs explicitly: `QUESTION` is whether the specified
manuscript claims follow under their actual hypotheses and whether the proposed
mathematical objections are justified; `SOURCE` is the frozen submission plus
relevant existing proofs; `QUESTION_NAME` identifies this verification scope.
Use `PROJECT_DIR/audit` as the working directory, so the derived
`<QuestionName>_lite/` evidence directory stays in the project. If `LIB_DIR` is
needed, select a dedicated Lean workspace under that audit directory, or an
existing project workspace whose derived sibling evidence directory remains
inside `PROJECT_DIR`. Never let a supplied external `LIB_DIR` redirect new
review evidence outside the project: use a project-local verification workspace
instead, while reading the supplied proofs in place. Preserve the original
toolchain/dependency versions and relevant mathematical definitions when
constructing that workspace. If setup is unavailable, retain the no-setup path
and record the targeted checks left unperformed. Do not invent a CLI
`--project` argument for the mode selector.

Preserve Lite's frozen dossier/target and goal contracts, claim/step ledger,
assumption census, independent adversarial review, feasible computational
checks, L3 weakest-link Lean triage, premise manifests for certificates, final
composition review, failure log, and resume evidence. Existing relevant Lean
source must be inspected even if no new certificate is needed. Record the
triage decision; zero new Lean targets is a possible justified result, not an
automatic default. Execute the selected targeted Lean checks where possible.
Missing infrastructure or faithful encodings remain explicit verification
limits, never successful checks.

Apply Lite within this fixed review scope. The submitted proof is a candidate
route to inspect. Additional routes are bounded independent ways to test the
same claim or objection; they do not require inventing new representations or
an alternative proof once current evidence is sufficient. The shared convergence
rule stops redundant discovery after required validation. A counterexample
needs independent checking under the actual hypotheses; generalizing it beyond
what establishes the issue is optional. Repair attempts may diagnose the minimum
adequate correction, but must not silently change the paper's theorem, solve a
new conjecture, or turn a stronger desired result into an author obligation.

Lite's SILVER ceiling applies only to the precisely scoped mathematical result
and requires all of Lite's evidence gates. Do not award a grade to the referee
report or equate a grade with acceptance/rejection or verification of the whole
paper. Preserve BRONZE/unresolved status when warranted, including the existing
no-setup path. No automatic Heavy escalation, Gold recorder, or full-paper
formalization follows from requesting a review. For editorial-only edits,
reuse current evidence; for changed mathematics, resume and revalidate the
affected scope using source hashes rather than restarting unchanged checks.

Internal evidence requirements are not demands on the authors. Missing Lite
artifacts, a citation tier restriction, or a formalization gap alone do not
justify a revision request. Numerical support and independent agreement do not
guarantee correctness or replace a proof; apply the standing rules when deciding
which issues survive into the report.

### Inspect the mathematical correspondence

Map each proposed mathematical criticism to the paper and any relevant Lean
statement. Inspect hypotheses, definitions, representation choices, imported
results, and the proof/use-site, not just the theorem name or build status.
Read inherited assumptions before claiming that the paper lacks a premise.
Check that a counterexample satisfies the actual hypotheses.

Record what the formalization establishes, what it assumes from verified
literature, and what it does not cover. Do not infer a manuscript defect from
an unproved formal adapter, a conditional interface, a missing library lemma,
or an unavailable build environment. Conversely, a successful build cannot
validate an incorrectly translated or weakened statement.

If a build is run, record the exact project/toolchain, command, result, and
scope. Review existing relevant proof code even when no build is needed.
Never describe historical logs or source inspection as a fresh compilation.

### When full formalization is explicitly requested

Use `<PLUGIN_ROOT>/workflows/merlean-heavy.md`, the current provider adapter,
and the required shared contracts. The supplied-paper branch is
`<PLUGIN_ROOT>/workflows/formalize.md`. These are internal workflows in the
same package; do not assume a removed slash command still exists. Record the
user-authorized Heavy scope separately from the default Lite review.

Pass the frozen target source and the requested mathematics scope, along with
its actual `PAPER`, `DATA_DIR`, `LIB_DIR`, `LEAN_LIB`, and strict axiom policy
where supported by that version. Inspect the invoked workflow's contract;
do not invent API fields or imitate a missing formalizer. Preflight the Lean
and Mathlib project and use the workflow's source-faithfulness, intended-object,
build, and axiom checks. Preserve its single-writer plan discipline.

Keep the formalization within the authorized target scope. Reuse Mathlib
results and apply Heavy's existing cost-of-formalization decision before
admitting any literature boundary, with precise primary-source statements,
matched hypotheses, independent source/use-site audits, and visible dependencies.
A cited result is not automatically exempt from Heavy's proof obligations.
Never assume an unproved target claim, declare a convenient project axiom,
or silently weaken the theorem. An uncovered target obligation remains
uncovered. Missing dependencies or incomplete proofs must be reported as
limits; do not mark requested full verification complete. Continue independent
review work that remains possible, without labelling its report fully verified.

## 3. Check computations and comparisons

Reconstruct feasible inputs from the source and independently check exact
arithmetic, commutators, ranks, small instances, and decisive comparison rows.
Preserve a small reproducible script or certificate when useful. Distinguish
independent recomputation from reproducing the authors' original run, and
both from merely inspecting a printed output.

An inability to reproduce a run is not evidence of a wrong result. Request
additional method details or data only when needed to substantiate a principal
claim, accepting the smallest adequate form. A claimed exact distance can
justify asking how its lower bound was established; it does not justify a
routine demand for every raw SAT log and certificate.

Compare against the criterion the authors actually state. Do not demand
matched geometry, a different proof method, a broader search, or a full noise
model unless their claim depends on it. Distinguish conditional hardware
interpretations from unsupported unconditional performance claims.

## 4. Check relevant literature

For a retained attribution, novelty objection, or benchmark, read the relevant
primary-source passage and record its version/location. Use local TeX or an
adequate primary PDF; do not require a TeX download when the necessary evidence
is already available. Missing source access limits the claim you can make.

Assess overlap with prior work concretely. An unsuccessful search is not
proof of novelty, a missing table entry does not prove a construction impossible,
and different polynomial representatives do not alone prove codes inequivalent.
Do not prescribe a preferred narrative when the authors' stated contribution
is defensible. Search further when the conclusion actually depends on it.

## 5. Select and write comments

Apply the standing rules after evidence review. Keep only the essential,
substantiated issues and a few useful clear typos/small factual corrections.
Do not promote every verified detail to a minor comment. Omit the minor
section when it adds no value. For retained issues give the problem, a precise
locator or concrete example, and the minimum repair.

Use the journal's rating fields if supplied; do not impose a particular
journal's rubric on every manuscript. Keep editor-only comments separate
when requested. Review artifacts do not authorize messaging authors/editors,
saving into a journal account, or submitting a report; use only actions already
authorized by the user.

## 6. Language and rendering

Prefer established target terminology, natural concise English, and no em
dashes. Differences from target vocabulary or phrases are suggestions, not
scientific errors. A terminology scanner never substitutes for reading the
report or requires deleting a valid objection.

Optional checker for a current TeX report:

```text
python3 <PLUGIN_ROOT>/scripts/report_language_audit.py \
  --target-rendered TARGET_PDF \
  --report-rendered REPORT_PDF --report-source REPORT_TEX \
  --report-build-manifest PROJECT_DIR/audit/REPORT_BUILD.json \
  --json-out PROJECT_DIR/audit/report-language.json
```

For PDF reports the build record must match `report_source_sha256`,
`report_rendered_sha256`, a successful `compile_exit_code`, and the actual
`compile_command`. This guards against scanning a stale PDF. For plain text,
use the same file for rendered/source; no build manifest is needed. Target
TeX may optionally improve extraction with `--target-source-root`. Exact
vocabulary restriction requires the user's explicit request and the
`--strict-vocabulary` flag; consult `--help` for its extraction requirements.
No automatic language result constitutes scientific approval.

Compile changed TeX and inspect every final PDF page for layout and glyph
problems. Rerun the checker only when used and affected; a typography change
does not require a new full Lean build or all scientific audits.

## 7. Independent review and delivery

For substantive review, obtain independent Astra perspectives on mathematical
validity and whether the objections are justified and proportionate. Add or
combine computation/literature review as needed. Provide the current report,
exact target source, relevant Lean files and primary references, and review
scope. Respect the host's concurrency; audits need not all run at once.

Ask for retained/withdrawn/narrowed recommendations with evidence. Do not
prime reviewers toward rejection or a desired recommendation. Main resolves
disagreements and records reasons. Reviewers do not mutate the report.
After substantive edits rerun affected review; preserve valid unaffected
findings. After minor wording/layout edits check the changed material and
record that scope instead of claiming a fresh scientific review of everything.

Deliver the final report and a concise verification/reassessment summary,
with current source/output hashes and material limitations. Report commands
actually run; distinguish prior from current results. Do not repeat expensive
checks already valid for unchanged code. Do not claim either unanimous audit
or compilation guarantees scientific correctness.
