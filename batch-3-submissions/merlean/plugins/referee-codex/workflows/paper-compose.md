# Paper Writing

For exam writing, `workflows/paper/exam-mode.md` governs novelty and human literature waits.
All polishing, compression, readability, page-limit and release checks below remain required.

Internal workflow of the paper-writing agent, for composition, refinement, resume, audit,
and next-version operations. Run in the main context. Inherit `<PLUGIN_ROOT>` from the
public entry point; use `<PLUGIN_ROOT>/scripts/paperctl` for every deterministic operation.

Read the following only when applicable:

- Read [protocol.md](paper/protocol.md) for the complete eight-stage gates.
- Read [reader-proof-quality.md](paper/reader-proof-quality.md) before planning or drafting;
  its proof-bridge, terminology and fresh-reader checks apply to both providers.
- Read [mathematical-writing.md](paper/mathematical-writing.md) for evidence-aware planning
  and context-sensitive editorial rules, which supersede conflicting older style prescriptions.
- Apply [reader-facing-paper.md](paper/reader-facing-paper.md) in planning, drafting, revision
  and existing reviews, including the TikZ requirement for any new figure.
- Read [refinement.md](paper/refinement.md) whenever an existing `.tex` is supplied.
- Read [references.md](paper/references.md) for every writing run, including runs that
  initially have no citations; relevance search and content verification are mandatory.
- Read [merlean.md](paper/merlean.md) before extracting a dependency graph or critical path.
- Read [composition detail](paper-claude-protocol.md) for the retained campaign-specific
  presentation checks, subject to the unified protocol's state and preservation gates.

## Select a mode

- `compose`: write a new paper from a campaign/graph. Run `paperctl init-compose`.
- `refine`: polish or reorganize an existing paper. Run `paperctl init-refine`; never edit the
  input. An input without a terminal `-vN` is v0, so `paper.tex` produces `paper-v1.tex`.
- `resume`: run `paperctl resume --state ...` and continue at the first unpassed gate.
- `audit`: follow the internal [paper audit](paper-audit.md); do not edit, download, commit, or write build products into the
  project.
- `next-version`: run `paperctl next-version INPUT.tex`; make no files.

Never infer a version from sibling files. If the required output exists, stop and tell the user to
pass that version as the new input. Never overwrite or silently skip a version.

## Preflight

1. Locate the latest author-approved scope and all available arguments: Lite/natural-language
   proofs, partial or complete Lean, sources, and unresolved work. Record an evidence assessment;
   a critical path is auxiliary, not proof or a requirement that every paper be Heavy-complete.
   Prefer an existing usable graph; reconstruct dependencies from arguments when it is absent.
2. Snapshot `git status`. Preserve unrelated and pre-existing changes.
3. Initialize the run. In refine mode, verify the printed source/output paths before editing.
   If an editor intentionally replaces the output inode during an atomic save, immediately run
   `paperctl claim-output --state <work>/00-run-state.json`; investigate an unexplained replacement.
4. Treat `00-run-state.json` as the run checkpoint. At every gate, recheck the baseline hash.
5. In refine mode, select the baseline main theorem labels and run `paperctl lock-main`. Do not
   leave the main-result lock empty.

## Orchestration and auditor roles

Use the active runtime adapter for bounded independent dispatches. GPT leads and independent
reviewers default to `gpt-6-astra`; bounded execution subagents default to `gpt-6.1-sol`.
An explicit user model choice takes precedence. Preserve the Claude adapter's
Anthropic model roles. Respect the runtime concurrency cap (with four total slots, at most three
children). Give each writer exclusive files; the main agent alone edits run state, coverage ledgers,
the versioned TeX, and Git. Use read-only agents for:

- critical-path/certificate verification;
- relevant-literature search, source-content and preserved-credit checks (novelty only if requested);
- summary-strength and main-result-equivalence audits;
- final coverage, definitions, terminology, references, and LaTeX audit.

Do not leak an intended verdict to an auditor. Require evidence and `PASS`/`FAIL`. Two independent
auditor `PASS` records are required if a locked main theorem statement is reworded.

## Execute the gated workflow

Follow [protocol.md](paper/protocol.md) in order. The essential sequence is:

1. Assess each result's actual proof and formalization status, public premises and gaps.
   Use available critical paths to inspect dependencies, not to decide truth or silently limit scope.
2. Compile an empty standard mathematics-paper framework. For a supplied page limit, record its
   source, counting rule and proof-first allocation in `02-reader-route.md`, following
   [mathematical-writing.md](paper/mathematical-writing.md).
3. Fix a coherent set of results (often 2–4 clusters, not a quota), check literature, and decide
   one title/theme. Preserve all locked results in refine mode. In compose mode,
   populate `03-main-results.json` for each result with a stable `result_id` (and `graph_node_id`
   when available), `candidate_label`, the
   frozen statement `normalized_sha256`, full `hypothesis_surface`, `novelty_status` (`CLEAR`, `ADJACENT`, or audited `NOT_REQUESTED`/`NOT_ASSESSED` under
   the autonomous reference protocol), and `novelty_evidence`.
4. Before editorial optimization, reconstruct and preserve `paper-raw.tex` from the actual
   mathematical evidence, with explicit proof statuses and research gaps. It is not a renamed
   polished paper or a deletion ledger. Audit its fidelity, freeze its complete source tree,
   then initialize the editable version from it while preserving the approved-paper baseline.
   Follow the raw checkpoint contract in the shared protocol. Next optimize the reader-facing
   dependencies using the available arguments and Markdown. Where a graph exists, inspect the
   selected full ancestor union, not just longest paths. Collapse direct specializations, omit
   only reconstructible elementary steps, and summarize material outside that cone. Read
   actual proof bridges (Lean and/or natural language), not just the import graph. Record every
   replacement, omission, and old/new consumer in `04-lemmas.md`; if formal dependencies are
   explicitly changed, rebuild Lean and rewire the corresponding Markdown DAG before drafting.
5. Organize and complete the full draft, then run the separate compression gate:
   - run `paperctl freeze-shrink --state <work>/00-run-state.json` immediately after the draft
     gate and before deleting or relocating anything; use its compiled page count to flag
     limited remaining space and revise the allocation before polishing;
   - optionally remove genuinely unnecessary units from TeX only after recording their exact
     statement, source, consumers, and rationale in `05.5-deleted-steps.md`;
   - retain important statements and their reasoning; supporting proofs may move to an appendix
     when appropriate, with unique body/appendix references in both directions;
   - cite verified accessible literature where useful; retain supported self-contained arguments
     when a source cannot be obtained. Never remove a needed proof to satisfy citation style.
6. Supply definitions and conventions before technical use, with one authoritative definition,
   helpful brief reminders, explicit local scopes and understandable introductory previews.
   Keep central proof arguments visible; use appendices for supporting material when helpful.
7. Write title, abstract, and outlook last; then standardize field terminology and notation.
8. Run preservation, reference, isolated compile, and independent auditor gates; checkpoint locally.

Run `paperctl gate` only after storing evidence. A failed gate stays failed until repaired and
rerun. Never carry a known defect forward.

## Binding paper rules

- Treat Lean as an internal auxiliary tool by default. Deliver the mathematical argument,
  not a verification section, build claim, trust-model paragraph, or repository advertisement.
  Keep formalization status and theorem/build correspondence in internal evidence. Only when
  formalization itself is explicitly part of the paper's subject should it appear in the paper,
  with precise supported scope and references. Never use a verification claim instead of proof.
- State shared setup clearly and reference it. Keep every public antecedent explicit or
  unambiguously in scope; itemize genuinely multi-claim results when helpful.
- Give notions authoritative definitions before technical use. Permit brief reminders and
  clear previews; recheck first uses and downstream dependencies after moving text.
- Avoid low-value wrapper definitions. Define a new name for an expression only when it materially
  improves readability and is reused. If the name adds little convenience or is used only once,
  remove the definition and write the original expression directly.
- Do not organize paper prose or proofs with process-numbered headings such as `Step 1`, `Step 2`,
  or `Stage 3`. When a roadmap materially helps, use an unnumbered LaTeX `itemize` list whose
  items begin with short bold mathematical summary phrases; otherwise use cohesive prose.
- Expose every essential inference in main proofs; lengthy derivations may live in referenced
  appendices. “Coarse” never means that the reader must invent a missing lemma.
- Present a direct specialization by a brief explicit application, including every needed
  object and hypothesis substitution; do not re-prove it or promote it to an independent result. Never collapse a selected
  or locked main result.
- Omit only reconstructible elementary steps under the proof-bridge check. Omission does not authorize
  deletion of a Lean declaration that still has formal consumers.
- Judge material by its contribution to the selected mathematical scope, not mere graph membership.
  Natural-language proofs may have no Lean node. Preserve scope, credit, evidence, shared setup,
  key explanations and transitions; record genuinely unnecessary omissions in the recovery ledger.
- Treat formal dependencies as frozen during paper writing. An explicitly authorized Lean
  dependency change reopens the critical-path and lemma gates, requires a clean rebuild, and must
  be reflected in both `01-critical-path.md` and `04-lemmas.md` before TeX work resumes.
- Apply compact layout only after the proof plan, applicable Lean checks, compression, definitions, and
  terminology pass. Honor a supplied journal class; otherwise use a standard mathematics-journal
  class with approximately `0.85in` margins, never below `0.75in`. Do not compress with tiny type,
  condensed line spacing, negative spacing, scaling, cropping, or overlapping floats.
- Keep every abstract/introduction/section-lead restatement weaker than or equal to the exact
  theorem; carry scope riders and quantifiers.
- Distinguish absolute kernel verification, verification modulo named literature-supported axioms,
  and named hypothesis mode in internal evidence; preserve their mathematical hypotheses in prose.
- Preserve recorded credit splits in the same sentence as the associated claim.
- Never strengthen, weaken, demote, or silently drop a baseline main result during refinement.
- Never silently drop baseline content. Every changed unit receives exactly one coverage
  disposition and destination.

## Reference and novelty discipline

Every new writing run performs and records a targeted relevance search, reads the exact
content of plausible sources, and decides which important citations support the actual
paper. There is no citation quota and no requirement to prove novelty. Preserve known
attribution even for results re-proved in full. Freeze an input-credit census and independently
audit each retained or inapplicable source credit against the final use site; a self-contained
proof is not by itself a reason to delete attribution.

Human literature authorization/download requests are off by default. Follow the autonomous
fallback and `NOT_ASSESSED` evidence contract in [references.md](paper/references.md); unavailable
optional sources do not block a self-contained paper or require user intervention.

For new references, follow [references.md](paper/references.md) exactly: confirm identity on
arXiv, download and safely extract the complete TeX source into project `refs/`, inspect the source
for the claimed result, and save the arXiv “Export BibTeX citation” verbatim. Reuse a cached source
only when its registry and hashes pass. If the result is absent, reject that citation and verify a
similar arXiv paper. When no arXiv version exists, the reference protocol also permits an
authoritative public journal article or book with exact source and citation evidence.

Novelty assessment defaults off (`assess_novelty: false`): skip novelty searches, record
`NOT_REQUESTED`, preserve known credit and proceed regardless of whether results are new.
When explicitly enabled, a novelty search can document `CLEAR`, `ADJACENT`, or `COLLISION`; it cannot prove global novelty.
A collision reopens main-result selection in compose mode. In refine mode, preserve the locked main
result and correct the novelty/title language or stop for a genuine conflict.

## Completion

Before final audits, complete the two sequential fresh-context Astra read-feedback-revision
cycles in [reader-proof-quality.md](paper/reader-proof-quality.md), using only the output
`.tex` as scientific input and a neutral exposition/attribution rubric as instructions. Preserve both actual reports and revision dispositions, then
verify the second revision. Do not substitute one reader's repeated reading for two fresh readers.

Run the deterministic preservation audit and isolated compile first:

```text
<PLUGIN_ROOT>/scripts/paperctl audit --state <work>/00-run-state.json
<PLUGIN_ROOT>/scripts/paperctl compile <output-vN.tex>
```

Then dispatch two independent read-only audits: semantic preservation/summary strength, and
reference/coverage/notation/LaTeX. Mark the final gate only after both pass, then run `paperctl audit
--state <work>/00-run-state.json --require-all-gates` as the release check. In a Git worktree, make
path-scoped local checkpoint commits; push only with explicit authorization for the repository
and artifacts. Report the title, printed main results,
verified/total references, pages, open questions, output path, and unchanged baseline hash.
