# Round 3 Summary

## Mainline Objective

Fix the single P1 blocking accuracy finding from the Round-2 code review:
the closing Remark `rem:glcabling` falsely attributed a proof of the cabling
conjecture to Gordon--Luecke and asserted the main theorem's conclusion holds
for arbitrary knots.

## Blocking Issues Fixed

- **P1 — false historical/theorem claim in Remark `rem:glcabling`.** The
  remark stated that Gordon--Luecke proved "the cabling conjecture for knots
  in $S^3$" (that every knot in $S^3$ with a reducible surgery is cabled) and
  that, with Lemma~\ref{lem:cablesplit}, this implies the conclusion of
  Theorem~\ref{thm:main} for arbitrary knots. The cabling conjecture
  (Gonzalez-Acuna--Short) is open; Gordon--Luecke proved reducing-slope
  integrality (our Theorem~\ref{thm:gl}) and related two-summand results, not
  the full statement. As written the remark would trivialize the whole result
  by bypassing Ni--Wu's deep $L$-space-specific theorem.

  **Resolution:** the remark was deleted outright (the reviewer's first
  suggested remedy: "This should be deleted or corrected"). Its label
  `rem:glcabling` was never cross-referenced elsewhere in the document
  (verified by grep), so no dangling `\ref`. Neither `Theorem~\ref{thm:niwu}`
  nor the external-inputs remark `rem:honesty` depended on it. The proof
  correctly continues to use the *stronger* Ni--Wu $L$-space cabling theorem,
  so the logical content is unchanged by removing the incorrect side claim.
  I considered replacing it with a corrected attribution, but chose deletion:
  a hedged historical aside would add no mathematical value, risks reintroducing
  an imprecise claim, and the genuinely-correct facts (GL integrality = Theorem
  thm:gl; Ni--Wu cabling for L-space knots = Theorem thm:niwu) are already
  stated precisely where used.

## Issues Reclassified as Queued

None — the single finding was resolved this round.

## How the Issue Was Resolved

See above: deletion of lines containing the false remark; no other text
touched. The theorem header on line 138 ("The cabling conjecture for
$L$-space knots; Ni--Wu, completed by Z.~Wu (2014)") is a correctly-stated,
correctly-attributed theorem (the $L$-space case was proved) and is retained.

## Issues Not Resolved

None.

## Validation

- `pdflatex -interaction=nonstopmode solution.tex` run twice: no errors, no
  undefined references, no multiply-defined labels (only the harmless
  `infwarerr` package-info line).
- No dangling references: `grep -n "rem:glcabling"` returns nothing.
- Document still begins with `\documentclass[11pt]{article}` and ends with
  `\end{document}`; `\end{document}` immediately follows Remark `rem:honesty`.
- `pdfinfo solution.pdf`: still **7 pages** (limit 16).
- Full-document grep for "cabling conjecture" / "conjecture" / "arbitrary
  knot": only (a) the correct Theorem-1.4 header (`thm:niwu`) and (b) the
  true statement "Property P conjecture, proved for all nontrivial knots by
  Kronheimer--Mrowka" remain. No false claims remain.

## Goal Tracker Update

`goal-tracker.md` updated directly: the P1 finding logged as RESOLVED R3 in
"Queued Side Issues", and a new "Completed and Verified" row added for the
Round-3 deletion. No Codex reconciliation request needed.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: A one-off removal of an incorrect historical assertion; no recurring
technical/tooling pattern to record.
