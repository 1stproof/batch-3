# Round 1 Summary

## Work Completed

Resolved all six blocking findings (B-1..B-6) of the Round 0 review
exactly at the places the directive indicated:

1. B-1 (f.g. scope breach, Branch B): Section 1 now takes "monoid" as
   in problem.tex and isolates an explicit "Scope hypothesis"
   paragraph: the theorem is proved for finitely generated P; the
   exact uses of f.g. (Prop 2.1(b), Lem 2.4, Cor 2.5, the face
   induction) are listed, Theorem 1.1 is restated for f.g. P, and
   Remark rem:nonfg + the scope paragraph describe precisely what
   obstructs the general case (P->P/K may fail f.p.; the face poset
   may be infinite).
2. B-2 (Lem 2.4 Step 2): deleted the false "same class" clause and
   rewrote the step: H_2/H_1 is archimedean (preimages of internal
   convex subgroups would refute maximality of the convex chain);
   generator classes outside H_1 are bounded below by c_0>0 through
   the archimedean embedding Lambda->R, so a decomposition of
   delta-n gamma has at most N_0=phi(delta-bar)/c_0 outside summands;
   a fixed partial sum s occurs for infinitely many n; then
   w:=delta-s lies in H_1 and 0<=n gamma<=w holds in the archimedean
   H_1 for infinitely many n -- contradiction. No "same class"
   argument remains anywhere in the file (grep-verified).
3. B-3 (finite presentation): new subsection ssec:fp with prop:fp
   (f.p. congruence characterization; f.p. of P->N, P->P/K,
   saturation/sharpening and pushouts), rem:nonfg (standing f.g.
   hypothesis and f.p. of all cover/refinement/test maps),
   one-sentence f.p. notes at lem:atomic (the necessity test maps),
   cor:probecover, and lem:sandwich; plus new lem:surj proving the
   w.l.o.g. that every cover admits a refinement with surjective piece
   maps (primitive-part reduction of folds), with the
   Z_U=P+Phi_U^gp consequence used by C1/C2. def:square now includes
   surjectivity in "standard".
4. B-4 (Cech nerve + citation): def:nerve (iterated pushouts over
   i(b), alternating complex), lem:nervemaps (structure maps iff the
   kernel face refines, for surjective pieces; kernel equality gives
   identity transitions), rem:verdier (Verdier hypercovering theorem,
   SGA 4 Exp. V, Theoreme 7.4.1, stated in words with hypotheses and
   used only via the displayed consequence). "Stacks Tag 03F9/01GY"
   removed from prop:vanish.
5. B-5 (Lem 4.3(b)): restated as (C1) and (C2) with exact hypotheses
   (Phi_U, Z_U) and full proofs via the pushout kernel criterion and
   the face property of K/J; iteration clause derives the consequence
   used downstream.
6. B-6: the iffalse/fi workflow block deleted (none remains);
   propagation cleanup of leftover "..." artifacts in lem:nerve,
   lem:mixed, and prop:vanish Steps 2-3 (both the two-fold
   subtraction with signs spelled out and the rank-one/base-case
   parentheticals made explicit).

## Files Changed
- solution.tex (sole deliverable), committed as 3522e48.
- goal-tracker.md: B-1..B-6 moved to resolved with resolution notes;
  plan-evolution row documenting the f.g.-scope decision.
- round-1-contract.md (written before implementation).

## Validation
- pdflatex twice after every item batch: final state 0 errors,
  0 undefined references, 14 pages (limit 16).
- Greps: no "\\iffalse", no "Stacks Tag", no "..." artifacts, no
  "same class", no wait/hmm/TODO strings.
- Q-2 check performed (only legitimate class-maximality usages
  remain, already verified correct by the review for ex:ff).

## Remaining Items
- Q-1 (global re-verification of nerve kernel claims over arbitrary
  parents) and Q-3 (typography pass) deferred to the Round 2 audit,
  as directed by the review.

## BitLesson Delta
Action: none
Lesson ID(s): NONE
Notes: no reusable workflow lesson; the round executed a
review-directed repair plan.
