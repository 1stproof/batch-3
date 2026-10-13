# Round 1 Contract

## Mainline Objective

Apply the single small accuracy/consistency polish pass to `solution.tex`
required by the Round-0 review (queued side issues 2-4): correct the
attribution of the $L$-space cabling theorem, fix one wording clause in the
$L$-space definition, and make the optional Section-4 sketch typographically
distinct while repairing its cosmetic glitches --- without restructuring the
(final, reviewer-verified) proof or changing its mathematical content.

## Target ACs

- AC-2 (precise statement/attribution of external theorems)
- AC-5 (clean, consistent standalone LaTeX document)

## Capability Anchor

N/A (plan has no Feature Map / Capability Map).

## Blocking Side Issues In Scope

None (Round-0 review found no blocking side issues).

## Queued Side Issues In Scope For This Round

The mainline objective is precisely to clear these queued items:
- Q2: relabel Theorem "Ni--Wu, 2014" attribution of the $L$-space cabling
  theorem as proved by Ni--Wu and completed by Z. Wu (2014); keep Section 4's
  d-invariant attribution to Ni--Wu.
- Q3: in the $L$-space definition, replace the clause "...with an
  incompressible Seifert surface" by "for every nontrivial knot $K$ in $S^3$".
- Q4: set the optional Section-4.2 sketch in slanted/italic type; fix the
  garbled fragment in Remark 4.4 ("the two forces the equality"); add the
  missing word "Theorem" before the Section-4.2 cross-reference; delete the
  doubled word "rational".

## Queued Side Issues Out Of Scope

- Q1 (contract hygiene annotation): optional, no `solution.tex` change; handled
  by noting Round-0 contract supersession in the summary.

## Round Success Criteria

1. The four surgical edits above are applied to `solution.tex`; the proof's
   logical chain, theorem count, and case analysis are unchanged.
2. `pdflatex` (run twice) compiles with no errors and no undefined references;
   the PDF remains <= 16 pages.
3. No new content claims are introduced; Section 4 remains clearly marked as an
   optional, non-load-bearing sketch.
4. Changes committed; round-1 summary written; goal tracker updated.

## Immutability Note

The immutable section of the goal tracker (Ultimate Goal, ACs) is unchanged
from Round 0.
