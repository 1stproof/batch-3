# Campaign composition details (retained Claude protocol)

For exam writing, `workflows/paper/exam-mode.md` governs novelty and human literature waits.
All polishing, compression, readability, page-limit and release checks below remain required.

This internal supplement preserves the detailed presentation checks of the original Claude
composition workflow. The shared [paper protocol](paper/protocol.md) is authoritative for stage
ordering, state files, versioned outputs, locks, compression artifacts, isolated compilation,
and release gates in both runtimes. Apply the additional checks below without weakening those
gates. For existing papers, [refinement](paper/refinement.md) governs preservation: a collision
never authorizes demoting a locked result. Inherit `<PLUGIN_ROOT>` and the active model/concurrency
adapter from the public paper-writing entry point. Bare `paper/` artifact paths below mean the
work directory recorded by `paperctl`, not a second output tree.

Read [mathematical-writing.md](paper/mathematical-writing.md) first. Evidence may be natural
language, partial Lean, complete formalization, or a mixture; the critical path is auxiliary.
The shared evidence assessment and immutable raw checkpoint precede editorial optimization.
This supplement supplies examples, not a mandatory article template or a proof-certification shortcut.
Apply [reader-facing-paper.md](paper/reader-facing-paper.md) throughout these stages. Keep internal
research history in evidence records and mathematical scope and limitations explicit in the final
paper; any new figure uses TikZ under the existing provider dispatch policy.

Run in the MAIN context as the orchestrator. Subordinate dispatches (scouts, verifiers,
reference hunters, drafting passes) follow the active runtime adapter: Claude workers retain
`model: "opus"`; GPT leads and independent reviewers default to `gpt-6-astra`, while
bounded execution subagents default to `gpt-6.1-sol`, subject to explicit user model choices.
Every step produces a named artifact in the paper's working directory and is committed
(path-scoped, in Git worktrees; pushing requires explicit user authorization) before the next step begins. Steps are GATED: a step's exit
checklist must pass before the next step opens.

## Inputs (fixed at invocation)

- `CAMPAIGN_DIR` — the campaign home (the ledger, dossier/novelty/citation records
  where present, cert/). Resolve the campaign supplied by the user or the active project;
  never silently substitute the demonstration campaign.
- `PLAN_GRAPH` — the dependency graph. Default: the campaign's Mem0-g plan store
  (`<campaign>_data/`; query via the internal `workflows/plan-graph.md` routine and
  `<PLUGIN_ROOT>/scripts/merlean`). Where the
  campaign's dependency structure instead lives in cert-file embeds + ledger blocks (the
  lite campaigns), derive the graph from: each cert file's embedded-region manifest
  (A embeds B ⟹ A depends on B) + each theorem's `#print axioms` cone + the ledger's
  per-delivery "consumes/discharges" records. Record which source was used.
- `PAPER_DIR` — output and work directory resolved by `paperctl init-compose` or
  `init-refine`; preserve exclusive versioned output creation and all source locks.

## Standing rules (binding, from the campaign's memory — violations are defects)

- **Lean is auxiliary by default.** No Lean identifiers, code, workflow filenames, or
  mandatory verification section in a mathematical paper. Keep verification records in
  internal evidence. Discuss them only when formalization is explicitly the paper's subject.
- **Precise statement style.** State shared setup clearly and retain every public hypothesis
  explicitly or by an unambiguous reference. Concise reminders are allowed. Every asserted
  claim needs proof or verified citation; unresolved claims stay explicitly unresolved, and
  locked results cannot simply be removed. Itemize multi-claim statements when useful.
- **Definitions in reader order.** Use one authoritative definition before technical use,
  local auxiliary definitions, and helpful reminders or understandable previews. Recheck
  first occurrences and dependencies after every move.
- **Avoid low-value wrapper definitions.** Define a new name for an expression only when it
  materially improves readability and is reused. If the name adds little convenience or is
  used only once, remove the definition and write the original expression directly.
- **Complete reader-facing proofs.** Main proofs expose every load-bearing inference;
  long workhorse derivations may move to a referenced appendix, never disappear behind
  “one can check”. Apply `paper/reader-proof-quality.md` in both provider runtimes.
- **Direct mathematical explanation.** Explain the objects, questions, assumptions and
  reasons in clear language appropriate to the reader. Equations and terminology serve
  that explanation; neither method-name lists nor newly invented nouns replace it.
- **Summary-layer discipline.** Every restatement of a result (abstract, intro, section
  leads) must be weaker-or-equal to the precise statement. Shorter ⟹ weaker, never
  stronger. Scope riders and quantifiers travel with every restatement.
- **Grade honesty.** Internal evidence uses the dossier's three-tier language
  (kernel-checked absolutely / kernel-checked modulo named literature-verified axioms /
  named hypothesis). Never conflate the accounting counts; cite the census with its
  method. The travelling residuals appear wherever a formalized status is claimed.
- **Credit splits verbatim.** Where the ledger records a credit split (a result half-due
  to a cited work, published identities, classical cores), the paper carries it in the
  same sentence as the claim.

---

## STEP 1 — the critical path

Assess available evidence first. Read a usable dependency graph when present (see PLAN_GRAPH),
or derive the dependency account from natural-language arguments and record graph limitations.
Deliver `paper/01-critical-path.md`:
- The full DAG restricted to theorem-grade nodes (drop gates, models, counterweights —
  list them separately as internal evidence).
- THE CRITICAL PATH(S): the longest/deepest chains ending at the campaign's strongest
  results, with each node's one-line statement and its grade
  (absolute / cited / hypothesis-mode).
- For each terminal node: its full hypothesis surface (the named structures it consumes).

GATE 1: each selected result's hypotheses and actual proof status checked against the
arguments. Verify recorded formal grades against certificates when available; absent Lean
or certificates are disclosed, not fabricated and not grounds for dropping supported results.

## STEP 2 — the empty section framework

Deliver `paper/02-framework.tex`: an empty section skeleton appropriate to the argument.
The following is one possible organization, not a required template:

  1. Introduction (context, the question, main results informally, related work, outline)
  2. Preliminaries / Setup (definitions and notation — populated later, just-in-time rule)
  3–k. One section per main-result cluster (named after the mathematics, not the campaign)
  k+1. Outlook / open problems, if useful
  Appendix A… (technical lemmas, lengthy proofs)
  References

No content yet. GATE 2: the framework compiles under latexmk with empty sections.

## STEP 3 — main-result selection + novelty double-check + title/theme

3a. From the assessed mathematical evidence, select coherent MAIN RESULTS (often 2–4
    clusters, not a quota), forming a through-line (each must
    answer the selected mathematical question). Require a novelty delta only when
    novelty assessment was explicitly enabled.
3b. Novelty assessment defaults off: record NOT_REQUESTED and follow `paper/references.md`;
    perform its mandatory relevance search and primary-content reading without a citation quota;
    do not perform a novelty sweep or require a new result for exam completion. Only when
    assessment is enabled, NOVELTY DOUBLE-CHECK, per result: reuse NOVELTY-OF-RECORD.md where it already covers
    the result, then run a FRESH arXiv sweep for anything published since the record's
    date (dispatch an independent verifier; the record's method: verdicts CLEAR/ADJACENT/
    COLLISION with evidence; summarizer output is never evidence — read the TeX).
    A COLLISION demotes the result and reopens 3a.
3c. Decide TITLE + MAIN THEME. Title = a name, not a summary; field-standard nouns.
Deliver `paper/03-main-results.md` (the selected results with their precise statements,
per-result novelty verdicts with evidence pointers, the title, a 3-sentence theme).

GATE 3: every selected result CLEAR, properly scoped ADJACENT with a delta sentence,
or independently audited NOT_REQUESTED/NOT_ASSESSED under the autonomous reference protocol. The latter
records retrieval limits, omits priority claims, and preserves proof dependencies and credit.
Do not wait for human literature authorization or downloads; state the through-line in one sentence.

## STEP 4 — the supporting-lemma selection

First preserve and audit the full raw reconstruction under shared Stage 3.5. It records the
available evidence and gaps, not only formalized results. Initialize the editable version
from that immutable raw before applying the following editorial selection.

With the main results fixed, walk their dependency cones and select the IMPORTANT lemmas
(the nodes a reader needs to follow the proofs — not every node; the harness proved far
more than the paper should print). For each: write the paper-facing STATEMENT (arXiv
statement style; the definition-dependencies it needs, listed).
Deliver `paper/04-lemmas.md`: the lemma list in dependency order, each with (statement,
where its proof will live: inline / appendix / citation, and — for citation — the source
candidate).

GATE 4: the union of definition-dependencies across main results + lemmas = the exact
definition list for Step 5.i (no definition without a consumer; no consumer without a
definition).

## STEP 5 — organize and draft

Draft the versioned paper under these binding rules. The final isolated-reader route needs
one native TeX file with inline supporting sections and bibliography; separately saved
BibTeX exports remain author-side evidence.

  (i) DEFINITIONS IN READING ORDER. Census explicit and prose introductions; ensure
      technical consumers have sufficient prior setup. Permit brief reminders and
      understandable previews. Do not delete definition clauses merely because no current
      consumer uses them: they may determine the mathematical object's scope.
  (ii) STANDARD STEPS. Briefly explain or precisely cite textbook/literature arguments
      according to reader needs; verify actual use-site hypotheses. Every citation follows
      the REFERENCE STANDARD (below). Keep auxiliary Lean formalization records internal.
  (iii) PROOF PLACEMENT. Keep central arguments visible. Supporting derivations may move
      to an appendix when useful, with statement/proof references both ways. Length alone
      does not justify moving the paper's main mathematical contribution.
  (iv) FACTORING (optional but attempted): where two definitions/constructions are
      instances of one, factor into a single definition with parameters; where two proofs
      share an argument, consider a shared lemma. Goal: reduce genuine duplication. Any factor
      that changes a statement's strength is forbidden (summary-layer rule).
  (v) THE REFERENCE STANDARD (for every paper not already treated this way in
      CAMPAIGN_DIR/refs or the registry). For the i-th new reference:
        1. Browse the internet; find the arXiv version — confirm by title, abstract,
           authors.
        2. If confirmed: download the TeX source from https://arxiv.org/e-print/[id],
           decompress into PROJECT/refs/ (create refs/ if none; naming: id with
           underscores).
        3. Read the .tex; verify it contains what we need. Select by importance and relevance,
           not merely because it was downloaded; record the decision.
           If the content is absent: find and verify a similar paper instead.
        4. If no arXiv version exists: use the exact publication type when the source is
           authoritative and public: `article` for a journal article and `book` for a
           book. Save the public PDF in the campaign references, read and verify it,
           and apply the autonomous fallback in `paper/references.md` if unavailable.
           Omit unverified optional citations; do not request human downloads or hide dependencies. Never classify an article as a
           book merely to satisfy a registry schema.
        5. After commitment: take the BibTeX from the arXiv abs page's
           "Export BibTeX citation" — verbatim, no hand-written entries for arXiv works.
      References already in refs/ with registry/ledger verification records are DONE —
      reuse their entries; do not re-download.

Deliver: the full draft. GATE 5: (a) the definition census passes; (b) every \cite
resolves to a refs/-verified source or a registry record; (c) latexmk compiles clean;
(d) a summary-layer audit pass (an independent skeptic reads intro+section-leads against the
precise statements; strikes propagate).

## STEP 5½ — SHRINK

A dedicated compression pass after the full draft passes: run `paperctl freeze-shrink` before
any deletion or relocation. If resuming a historical run with final matter already drafted,
reopen the required gates and rebuild the frozen inventory before the pass, then recheck Gate 6.

- **Reconstructible and unnecessary steps: optionally remove from the .tex** — preserve every
  deleted step verbatim in `paper/05.5-deleted-steps.md` (with its original location, the
  reason for deletion, and what the reader is now trusted to supply). Deletion may never
  change what a statement claims (summary-layer rule); if removing a step would force a
  statement to silently strengthen or a proof to gap, the step is not "unnecessary".
- **Important steps: KEEP.** A supporting proof may move to an appendix when appropriate, with
  the two-way `\label`/`\ref` system: the calling site references the appendix proof, and
  the appendix proof references every calling site. No orphaned appendix material:
  everything in the appendix is referenced from the body at least once.
- The classification of every touched step (deleted / moved / left) is recorded in
  `paper/05.5-shrink.md` with one-line reasons.

GATE 5½: (a) isolated compilation clean after the pass; (b) the two-way `\ref` audit passes
(every appendix item referenced from the body; every body reference resolves); (c) a page-count delta
is reported (unchanged or longer text needs specific proof/exposition justification, not
forced deletion); (d) a statement-integrity
check — every theorem/lemma/corollary statement byte-identical before and after the pass
(diff the statement environments; proofs may change, statements may not).

## STEP 6 — abstract, title (final), outlook

Write the abstract LAST (from the actual content): ≤ 200 words, the through-line, the
main results at weaker-or-equal strength, and necessary mathematical scope; no mandatory
verification-model clause.
Confirm or revise the Step-3 title against the finished content. Write §Outlook from the
campaign's recorded open problems (the dossier's remaining-surface list; each open item
stated as a question, with what is known).
GATE 6: the abstract survives the summary-layer audit against every statement it
compresses.

## STEP 7 — terminology and notation standardization

A dedicated full pass (dispatch an editor under the active runtime adapter, then independently verify):
- Build the TERMINOLOGY TABLE by mathematical concept, checking relevant primary usage
  and conventions. New names require a real repeated role or necessary distinction.
- Inspect each technical occurrence by meaning, including source synonyms and explicit
  local notation scopes. Do not mechanically replace ordinary words or conflate distinct
  objects because they have similar spellings. Resolve genuine ambiguous collisions.
- Remove unnecessary coinages and redundant explanation, not legitimate technical vocabulary.
Deliver `paper/07-terminology.md` (the table) + the standardized .tex.
GATE 7: a grep-based synonym audit over the final .tex against the table returns zero
unresolved synonyms; the notation index has no collisions.

## STEP 8 — two fresh-reader revision cycles, then release

Apply the shared `paper/reader-proof-quality.md` and `paper/two-round-review-runtime.md`:
two distinct fresh-context Astra readers each read only the entire current output TeX, with
the neutral exposition/attribution rubric as instructions, followed by a recorded revision.
Round two starts after the first revision and sees
no earlier feedback. Verify the second revision, then stop routine polishing. Unresolved
substantive issues still block release. If Astra dispatch is unavailable, report that limitation;
never relabel the writer or an already-primed auditor as a fresh reader.

Final checks: latexmk clean; all gates' artifacts present; the repair-record appendix of
the dossier updated with "paper vN drafted"; commit. Report to the user: the title, the
main results as printed, the reference count (verified/total), the length, and the open
items list. STOP — the user reviews before any further iteration.

## Failure discipline

Any gate failure: fix and re-run the gate before proceeding — never carry a known defect
forward. When novelty assessment is enabled, a novelty COLLISION reopens Step 3. In exam mode,
record known overlap and correct credit/priority framing without requiring originality. Any conflict
between this protocol and the user's live instructions: the user wins; record the
deviation in the step artifact.
