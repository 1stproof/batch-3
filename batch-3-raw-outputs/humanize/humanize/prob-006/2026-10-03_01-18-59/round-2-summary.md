# Round 2 Summary

## Mainline Objective

Resolve the two P3 expository findings from the Round-1 code review of
`solution.tex`, without altering the (final, twice-reviewer-verified) proof
chain and without adding content.

## Blocking Issues Fixed

Both findings were treated as must-fix for clean acceptance:

- **P3-a (Case 2, $0$-surgery, primality inference).** The original sentence
  "It is not $S^3$ (indeed $b_1=1$...), hence it is prime" leaned on $b_1=1$,
  which excludes $S^3$ but *not* $S^1\times S^2$ (both have $b_1=1$), and so
  did not by itself settle primality. Fixed by rewriting the passage to state
  the correct logical chain: $S^3_0(K)$ is irreducible (sphere theorem); an
  irreducible closed orientable manifold is prime unless it is
  $S^1\times S^2$; the latter is excluded because it contains a nonseparating
  essential sphere $\{\mathrm{pt}\}\times S^2$, contradicting irreducibility
  (with an explicit note that $b_1(S^3_0(K))=1=b_1(S^1\times S^2)$, so this
  case is not excluded by homology alone); and it is not $S^3$ since
  $b_1\ne 0$. This matches the reviewer's suggested wording in substance.

- **P3-b (closing Remark 5.4, unsourced generalization).** The sentence
  claiming the Ni--Wu cabling theorem "generalizes to knots in arbitrary
  $L$-space homology spheres, where [Gordon--Luecke integrality] is
  unavailable" was unsubstantiated in that generality. Fixed by replacing it
  with a hedged parenthetical: analogues of the $L$-space-knot cabling
  statement have been studied for knots in more general $L$-space homology
  spheres, where the integrality conclusion of Theorem~\ref{thm:gl} is
  unavailable, and that we use none of that here. No unsupported claim
  remains.

## Issues Reclassified as Queued

None — both findings were resolved in this round. There were no other review
findings.

## How Each Issue Was Resolved

See "Blocking Issues Fixed" above. The two edits are surgical and confined to
the Case-2 paragraph (proof of Theorem 1.1) and the final explanatory Remark
5.4. No load-bearing citation, theorem statement, or other case was touched.

## Issues Not Resolved

None.

## Validation

- `pdflatex -interaction=nonstopmode solution.tex` run twice: no errors, no
  undefined references (only the harmless `infwarerr` package-info line in the
  log).
- `pdfinfo solution.pdf`: still **7 pages** (limit 16).
- `pdftotext` confirms both fixes render correctly: "nonseparating essential
  sphere {pt}×S^2 ... this case is not excluded by homology alone" and
  "Analogues of that L-space-knot cabling statement have been studied for
  knots in more general L-space homology spheres ... we use none of that
  here."
- File still begins with `\documentclass` and ends with `\end{document}`; the
  `quote`/`itshape` block from Round 1 remains balanced and scoped.

## Goal Tracker Update

`goal-tracker.md` updated directly: both findings logged as RESOLVED R2 in
"Queued Side Issues", and a new "Completed and Verified" row added for the
Round-2 fixes. No Codex reconciliation request needed.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: Expository/clarity fixes in a mathematical proof; no recurring
tooling/build pattern worth recording.
