# Refinement mode

## Version rule

Only a terminal `-vN` before `.tex` counts. `paper.tex` and `paper-v0.tex` both produce
`paper-v1.tex`; `paper-v7.tex` produces `paper-v8.tex`; `paper-v2-draft.tex` produces
`paper-v2-draft-v1.tex`. Reject leading-zero versions such as `-v01`. Derive N from the supplied
input, never siblings. Refuse a collision and never overwrite.

Initialize with:

```text
paperctl init-refine INPUT.tex
```

This creates an exact versioned copy before edits, records the input SHA-256, and builds a work
directory next to the paper under `paper-writing/<output-stem>/`.

The run records the output inode to detect path replacement. Ordinary in-place edits preserve it.
After a legitimate editor performs an atomic save, run `paperctl claim-output --state
WORK/00-run-state.json` before any gate, resume, snapshot, or audit command; investigate rather than
claim an unexpected replacement.

## Local author comments

Apply the shared mathematical-writing guidance to local revisions as well as whole-paper work.
Read the commented passage, its neighbors, and the later passages it introduces or supports.
Identify the reader's difficulty and the paragraph's purpose before choosing the smallest
adequate repair; do not reduce a conceptual comment to word substitution. Assess suggestions
critically, preserving claims, assumptions, credit, and essential reasoning. Generalize a local
lesson only where it applies in context and within the author's authorized editing scope.

After editing, reread the passage with its neighbors for dependency order, level of detail, and
duplication. Check affected first uses and incoming references; deleting an explanation must not
leave a missing label or a label attached to text that no longer supports the reference. Record
the repair or justified no-op in the existing revision records before resolving the comment.
Targeted fresh-reader feedback may help, but does not replace the full-manuscript review or
preservation gates below. Give fresh readers the text and reading task, not the author's
diagnosis or preferred fix. Preserve unrelated author edits and settled prose.

## Main-result preservation

The approved input remains the scope baseline even when the editorial output starts from
a separate raw reconstruction. Preserve `paper-raw.tex` before rewriting, following
`raw-checkpoint.md`. Never derive the revision number from the raw filename or claim a
retrospective reconstruction was the historical initial draft. Preserve and compare both
raw argument/status fidelity and approved-baseline scope. A partial Lean graph cannot
silently remove a natural-language result from either record.

After identifying every baseline main result, run one `--label` per result:

```text
paperctl lock-main --state WORK/00-run-state.json --label thm:first --label thm:second
```

Default to preserving each normalized statement and stable label exactly. If presentation requires
a mathematically equivalent rewording, record the changed statement and two independent
equivalence audits in `00-main-results-lock.json`. Any change to domain, quantifier, hypothesis,
scope rider, inequality direction, constant, or conclusion is a failure. Do not move a main result
out of the paper's main-results presentation.

## Coverage dispositions

Every baseline inventory unit starts as `auto`, which passes only while normalized content remains
unchanged. A changed unit must receive exactly one disposition in `05-coverage-ledger.json`:

- `retained`: reworded in place; give a target label, reason, evidence, and two independent
  semantic PASS records for any changed mathematical statement.
- `moved`: same content elsewhere; give a target label and reason; changed mathematical wording
  needs two independent semantic PASS records.
- `merged`: faithfully subsumed/factored; give the target and reason; changed mathematical wording
  needs two independent semantic PASS records.
- `cited`: replaced by verified literature; give citation key and reason.
- `ledger-only`: elementary/unnecessary; mirror the exact omitted normalized TeX plus its hash in
  `05.5-deleted-steps.md` and the JSON record, and preserve the verbatim raw TeX (including
  comments/formatting) plus its SHA-256.

  A synthetic `citation` inventory entry records only a citation key and has no raw TeX
  source span. If that key is absent from the candidate, its `LEDGER_ONLY` compression
  record may omit `archived_raw_text` and `archived_raw_sha256` (or set them to null), while
  retaining the exact normalized key, its hash, archive anchor, reason, source, consumer,
  and review evidence. Do not invent raw bytes for an index entry. This exception applies
  only to synthetic citation entries; removed or changed prose containing the citation
  still needs its own ordinary coverage disposition and exact recovery where required.
- `body-appendix`: important statement in body, proof moved with two-way labels/refs.

A baseline theorem that directly specializes a retained general theorem may be collapsed only as
`merged`, with the retained theorem as target, a compiling Lean instantiation witness where
formalized (otherwise an independently checked explicit mathematical application), two
independent semantic `PASS` records, complete old/new consumer mapping, and exact recovery text. A
locked main result is never eligible. Record presentation-edge rewiring in `04-lemmas.md`; formal
Lean edges remain frozen unless an authorized change reopens and reruns the earlier gates.

Run `paperctl freeze-shrink` after the full draft and before applying these dispositions. The
Markdown ledger is for readers and recovery; JSON is the deterministic mirror. Preserve old and
new consumers for omissions and merges. An unclassified change is a hard failure.

## Preservation audit

Apply `reader-facing-paper.md` to the editable version and existing reviews. Omitted process
history remains recoverable in sidecars; its mathematical consequences remain explicit in the
paper. Do not sanitize frozen raw or baseline files, or require internal labels in final prose.

Near completion, follow `reader-proof-quality.md`: two distinct fresh-context Astra readers
sequentially read the current full manuscript and writing guideline, with a revision after each.
Record both rounds and verify the final repairs before release; this does not replace the
independent mathematical preservation audit or excuse unresolved substantive findings.

Run `paperctl audit --state WORK/00-run-state.json`. It checks the baseline hash, aliases, complete
ledger, exact unchanged units, destination labels/citations, Markdown anchors, bidirectional appendix
links, main-result locks, unresolved refs, and reference registry. An independent semantic auditor must still
check mathematical equivalence and prose-topic coverage.
