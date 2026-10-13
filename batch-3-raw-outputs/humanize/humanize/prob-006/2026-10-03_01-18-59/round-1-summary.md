# Round 1 Summary

## What Was Implemented

The single small accuracy/consistency polish pass directed by the Round-0
review (queued side issues Q2-Q4). The mathematics was declared final by the
reviewer and was **not** restructured: I made only surgical edits to Section
1.3 ("Comments on the inputs") and the explicitly-optional Section 4
`($L$-space mechanism sketch)`. Sections 1-3 (statement, preliminary lemmas,
proof of the main theorem) are byte-for-byte unchanged.

Changes to `solution.tex`:

1. **(Q2) Attribution of the cabling theorem.** The theorem header was
   relabeled from "Ni--Wu, 2014: the cabling conjecture for $L$-space knots"
   to "The cabling conjecture for $L$-space knots; Ni--Wu, completed by
   Z.~Wu (2014)", and the inputs-comment now says the result is proved by
   Y.~Ni and Z.~Wu (Adv. Math. 267, 2014) via the genus-bound argument that
   reduces it to ruling out a closed nonseparating essential surface, and is
   completed by Z.~Wu (2014). Section 4 keeps the d-invariant mechanism
   attributed to Ni--Wu, as directed.

2. **(Q3) Rational-genus wording.** The clause "...equals the Thurston norm
   $x(\gamma)/2=g(K)-1/2$ when $K$ is a knot in $S^3$ with an incompressible
   Seifert surface" was changed to "...equals the Thurston norm
   $x(\gamma)/2=g(K)-1/2$ for every nontrivial knot $K\subset S^3$ (the
   minimal-genus Seifert surface of a nontrivial knot is incompressible)".
   (This line lives in the optional Section 4.2 paragraph; the reviewer's
   label "Definition 1.2" referred to this paragraph.)

3. **(Q4) Optional-sketch typography + garbled fragment.** The entire Section
   4.2 sketch (introductory paragraph, the genus-bound theorem, and the
   "How Heegaard Floer theory forces the bound" remark) is now wrapped in a
   `\begin{quote}\itshape ... \end{quote}` block with a bold banner "Optional
   explanatory sketch (not used in the proof; not a complete proof)", so the
   non-load-bearing status is typographically visible. The garbled "The two
   forces the equality" was repaired to "The two bounds force equality", and
   the doubled "The (rational) genus" was reworded to "The genus (rational
   Thurston norm)". The soft-hyphen artifact in "sketches" is gone.

(Q1, contract hygiene, required no `solution.tex` change; it is noted in the
goal tracker as superseded by the Round-0 plan-evolution entry.)

## Files Changed

- `solution.tex` (edited).
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` (updated Active Task
  status, queued-issue resolutions, Completed-and-Verified rows).
- `.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md` (created).

## Validation

- `pdflatex -interaction=nonstopmode solution.tex` run twice: no errors, no
  undefined references; the only `grep` hit in the log is the harmless
  `infwarerr` package-info string.
- `pdfinfo solution.pdf`: still **7 pages** (limit 16).
- Balanced `\begin{quote}`/`\end{quote}` (1 each); `\itshape` scoped inside
  the quote so body text after it is upright.
- `pdftotext` spot-check confirms all four fixes render correctly
  ("completed by Z. Wu (2014)", "for every nontrivial knot K ⊂ S^3",
  "Optional explanatory sketch (not used in the proof...)", "The two bounds
  force equality genus(F)=g").

## Remaining Items

None. The deliverable satisfies AC-1..AC-5: the proof is correct
(reviewer-verified line by line), self-contained relative to precisely stated
external theorems, and typographically clean. Awaiting reviewer verification
of this polish pass.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: No reusable technical lesson; this was a four-line editorial polish of
a mathematical proof, not a recurring tooling/build pattern.
