# Round 1 Contract

## Mainline objective

Repair the seven localized gaps M-1..M-7 identified by the Round-0 review
in solution.tex, so that the verification of [GT, Definition 5.1(3)--(4)]
(checkerboard/subdivision and filtration isometry), the statements of
Proposition 4(a)/(c) and Lemma 3, and the section argument of Lemma 1 are
all at specialist line-by-line standard, and the computation
E_m(X)/W_2 = N, E_m'/E_m = U(-1) is quoted honestly as an external result
from [GT, Example 1.2] rather than presented as proved.

## Target ACs

- AC-1, AC-2

## Capability Anchor

N/A (the plan contains no `## Feature Map / Capability Map` section).

## Blocking side issues in scope

None: the review classified M-1..M-7 as mainline gaps, and no blocking side
issues exist.

## Queued side issues out of scope

- Q-1 (cosmetic grammar/typography): fixed opportunistically in the same
  editing pass, but it does not gate the round.

## Round success criteria

1. Prop 4(a) no longer conflates generic Picard rank with Picard rank at
   every parameter; the Type III boundary statement matches the assumed
   very-generality hypothesis.
2. Prop 4(c) states Gamma(X_0) = S^2 with cell structure (2 vertices,
   1 edge, 2 bigonal faces) plus an explicit 4-fold subdivision statement;
   Thm 4(b) relates Gamma(Y,gamma) to Gamma(X_0) by homeomorphism +
   subdivision, not by identification of complexes.
3. Thm 4(d) presents one explicit lattice E_m = N \oplus Z f model (rank
   19), both embeddings (v -> f on the degeneration side; fibre class -> f
   on the fibration side), Phi = identity, and a 4--6 line
   pairing/polarisation check (h = sigma + 2f on both sides).
4. The checkerboard clause is stated as a vertex bipartition of the
   equatorial 4-cycle (bipartite because 4 is even) with the light-leaf
   clause disposed of; no face-2-colouring assertion in the wrong slot.
5. Prop 4(d) quotes E_m/W_2 = N and E_m'/E_m = U(-1) from [GT, Example
   1.2] as a cited external result with hypotheses, parallel to Theorem C.
6. Lemma 3's statement contracts exactly sigma and the two II*-fibre
   components (Du Val E_8 + E_8 image), consistent with its proof;
   Lemma 1's section sentence is the clean three-line Riemann--Roch +
   Weyl-group argument; M-7 punctuation fixed.
7. pdflatex compiles twice cleanly, <= 16 pages; commit + round-1 summary.
