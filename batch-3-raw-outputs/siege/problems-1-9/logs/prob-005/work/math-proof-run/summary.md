# Round 6 summary (final: concluded)

## Problem / goal
The question: in every hyperfield, does 0 ∈ x⊞y⊞z imply 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz? The problem fixes this claim. Ledger [GOAL] #14 records it as REFUTED, with locator round4_q2.

## Headline: REFUTED and certified. The answer is NO.
Round4_q2 gives a complete counterexample, and two independent verify queries certified it with VERDICT: CORRECT.
- round5_q1: a step-by-step referee check.
- round5_q2: an adversarial recheck, which also confirms that the Krasner, Viro and Baker–Bowler definitions all accept the hyperfield.
These are recorded as [AUDIT] entries #22 and #23, both citing entry 14.

## The counterexample (round4_q2)
- Take a projective plane on an abelian group G, with lines the translates g+D of an infinite perfect difference set D ⊂ Z.
- Build H = G ∪ {0} with:
  - -1 = 1;
  - a⊞a = {0,a};
  - a⊞b = L(a,b) \ {a,b} for a ≠ b.
- Proposition 1: H satisfies all the hyperfield axioms. Associativity is proved by a four-case analysis: all three summands equal; exactly two equal; three distinct and collinear; three non-collinear.
- Lemma 2: suppose 1, x, y are distinct and collinear, and x^3, y^3, xy are distinct points on a line M that does not pass through 1. Then T := x^3⊞y^3⊞xy⊞xy⊞xy = M ∪ {0}, which does not contain 1.
- Lemma 3: a perfect difference set gives a plane satisfying (P1)–(P4).
- Lemma 4: a greedy construction gives a perfect difference set D with {0,1,4,103,105,112} ⊆ D and 100 ∉ D.
- The instance: x = t, y = t^4, z = 1. The hypothesis 0 ∈ x⊞y⊞z holds, but 0 ∉ the six-term sum.

Parallel complete counterexamples, all built on the same mechanism: round4_q1, round4_q4, round4_q6 and round4_q7.

## Standing results (for the "Other routes" section)
- #2 (round1_q1): the composition rule and the linear-derivation obstruction.
- #3 (round1_q3): the diagonal case.
- #4 (round1_q4): the reductions to (C).
- #7 (round2_q3): the exponent-3 reduction.
- #8 (round2_q4): the idempotent-class lemmas.
- #10 (round3_q4): the coincidence lemma and union-type hyperfields.
- #11 (round3_q2) and #12 (round3_q1): the translations, with their linear obstructions.
- #17 (round4_q2): plane-to-hyperfield construction and failure criterion.
- #18 (round4_q5): the hexagon lemma and the Helly criterion; skew fields and alternative division rings satisfy the claim.
- #19 (round4_q9): up-closure.
- #20 (round4_q3): the case g^2 = 1.

## Dead ends
- N (#13, equivalently #15): REFUTED by round4_q2.
- (C) (#5, equivalently #16): REFUTED by round4_q1 and round4_q2.

## Open (not needed for the verdict)
- #21: whether a FINITE counterexample exists.

## Target
None. The run concludes this round, with round6_DONE.md.
