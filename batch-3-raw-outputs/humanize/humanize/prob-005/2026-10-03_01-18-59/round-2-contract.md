# Round 2 Contract (Drift Recovery)

## Root cause of recent drift/stagnation

Rounds 0-1 stalled on the same single point: the free case of the
theorem was never derived from the axioms. Round 0 attempted a descent
proof supported by enumeration (rejected: numerical evidence cannot be a
proof step). Round 1 downgraded to a conditional statement (Option B),
which the reviewer accepted only provisionally, because several concrete
Option-A routes remained untried and one falsity claim was over-stated.
The drift is therefore not scope drift but *proof search incompleteness*:
the mainline cannot advance without new mathematical results on the
Elevation Problem.

## Recovered mainline objective (exactly one)

Execute the reviewer's ordered plan M1.(1)-(4) against the Elevation
Problem (E): 1∈a⊞b ⟹ 0∈a^{⊞3}⊞b^{⊞3}⊞(−1)⊞(ab)^{⊞3}, attacking in
order: (1) the doubles-cube/1⊞1 saturation mechanism; (2) the
permutation-adjusted tower; (3) prove-or-refute the two conditional
sublemmas (H4-collapse; Delta condition); and (4) correct the
over-stated falsity claim of round 1. Each named item must end either
PROVED (from (H1)-(H4) alone, written into solution.tex) or REFUTED
(with a precise mathematical statement of the obstruction, written into
the summary). If any route closes (E) in general, the document is
restored to a full unconditional proof (Option A achieved). If all
routes are genuinely refuted, Option B stands with the refutations
recorded.

## Target ACs (the ones that prove mainline progress)

- AC-1 (a complete axiom-level proof, or refutations precise enough that
  no concrete untried route remains)
- AC-3 (no numerical evidence as a proof step; every refutation stated
  as a precise mathematical claim, not a failed-search narrative)

## Capability Anchor

N/A (plan.md contains no Feature Map / Capability Map section)

## Truly blocking issues (in scope)

- The Elevation Problem itself (this IS the mainline).
- The four untried routes M1.(1)-(4): each must be settled.

## Queued issues (out of scope this round)

- Q1: bitlesson-selector binary absent (informational).
- Q2: git history contains superseded drafts (no action).
- Q3: cosmetic: strings "enumeration"/"exchange" appear in two
  meta-statements of the PDF (not proof steps); the "conversely"
  sentence in prob:elevation is the same direction twice. To be fixed
  in the final cleanup pass, not during the mathematical work.

## Success criteria (what flips the verdict back to ADVANCED)

1. Every item M1.(1),(2),(3),(4) is either proved and incorporated into
   solution.tex, or refuted with a precise mathematical obstruction
   statement recorded in the round summary/document.
2. solution.tex either (a) proves the original theorem unconditionally
   from (H1)-(H4), or (b) retains the honest conditional verdict AND now
   contains the named sublemmas' precise proved/refuted status.
3. solution.tex continues to compile in two pdflatex passes with no
   errors, ≤ 16 pages, and contains no numerical-evidence or
   citation-based proof step.
4. Recovery contract, goal-tracker updates, commit, and round-2 summary
   all completed.
