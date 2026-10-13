# Read-only paper audit checklist

Apply `reader-facing-paper.md` in these existing checks: retain every mathematical qualification,
verify useful bridges and claim-specific source locators, review any new TikZ figure
for faithful labels and relations, and assess length by reader benefit. Internal history belongs
in faithful sidecars, not final exposition; no figure or arbitrary shortening quota is required.

1. Hash baseline, candidate, state, ledgers, registry, bibliography, and included TeX. Snapshot Git.
2. Run deterministic audit and isolated compile. Treat any project mutation as failure.
3. Compare each locked main result's domain, quantifiers, hypotheses, scope riders, constants,
   inequality directions, and conclusions. Check its main-text prominence and all summaries.
4. Sample every automatic coverage class and inspect every moved/merged/cited/ledger-only item.
   Confirm surviving consumers and complete Markdown recovery records.
5. For body/appendix items, retain the statement in the body and verify both references resolve.
6. Recompute the full selected-result ancestor closure and compare frozen formal dependencies and
   reverse consumers with the current graph and Lean sources. Audit every proof-plan action,
   specialization witness, recovery anchor, and consumer rewire; reject a presentation edge changed
   in only one Markdown artifact or an unrecorded formal-edge change.
7. Census explicit and prose definitions, standing constraints, macro/declaration commands, and
   notation across the expanded root document. Confirm one authoritative occurrence per concept or
   symbol, with sufficient setup or explicit references before technical use. Allow clear previews,
   brief reminders, and explicit local scopes; place shared setup where its consumers can find it.
8. Check every citation against registry hashes and the downloaded TeX passage or verified public
   article/book source. Confirm arXiv BibTeX is the saved export, other publications have a saved
   citation snapshot, and every citation key resolves. For NOT_REQUESTED/NOT_ASSESSED novelty, verify the
   current manuscript-bound independent audit and retrieval record, absent priority claims,
   preserved known credit, and no hidden unresolved proof dependency. Zero references alone
   is not a failure; unknown novelty must never be reported as verified.
9. Audit title, abstract, introduction, and section leads for claims stronger than precise results.
10. Check established terminology and consistent names for each technical concept, preserving
    distinct meanings, necessary source aliases, and ordinary prose variation; check notation collisions.
11. Reject process-numbered paper organization such as `Step 1` or `Stage 2`; a necessary roadmap
    should use unnumbered `itemize` entries beginning with short mathematical summary phrases.
12. Compare the pre-layout and final inventories. Reject body or semantic changes, margins below
    `0.75in`, tiny or condensed type, negative spacing, scaling/cropping tricks, overlap, or layout
    performed before the proof-plan and Lean checks passed.
13. Apply `reader-proof-quality.md`: reconstruct each essential proof bridge from the paper,
    check it against Lean or its exact source, and reject an appendix that only repeats its
    promised conclusion. Verify an actual fresh-context sequential reader reviewed this
    manuscript version without author-side maps or prior verdicts. Resolve their findings.
    Neither an import graph nor a size decrease proves reader completeness.
14. Rehash and resnapshot Git. Return `PASS` only with no residuals; otherwise `FAIL` with exact
    locations and repairs. Never edit.
