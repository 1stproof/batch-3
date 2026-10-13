# Round 0 Contract

## Mainline Objective

Produce a complete, rigorous, self-contained proof in `solution.tex` that every
irreducible 3-manifold obtained by Dehn surgery on an L-space knot is prime
(equivalently: such a surgery manifold always has at most two prime summands),
answering the problem in `problem.tex` affirmatively. The proof must give full
proofs of the two load-bearing lemmas (the Schubert/Scharlemann
closed-incompressible-surface theorem for reducible surgeries, and the
`HFK`-epsilon obstruction to closed non-fiber surfaces in L-space knot
complements) while precisely stating the external theorems invoked (Property R,
Property P results, adjunction inequality, cabling characterization of
reducible surgeries).

## Target ACs

- AC-1 (complete proof of every claimed implication)
- AC-3 (audit of logical direction, quantifiers, degeneracies)

## Capability Anchor

N/A (plan has no Feature Map / Capability Map)

## Blocking Side Issues In Scope

None known.

## Queued Side Issues Out Of Scope

None.

## Round Success Criteria

1. `solution.tex` compiles with `pdflatex` in the environment, is standalone,
   uses only standard packages, and fits within 16 typeset pages.
2. The document begins with `\documentclass`, ends with `\end{document}`, and
   contains no Markdown or workflow commentary.
3. Every lemma used in the main chain is either proved in the document or
   stated as an external theorem with precise hypotheses; the reductions
   `reducible surgery => closed incompressible surface in complement` and
   `L-space knot => no closed non-fiber incompressible surface in complement`
   are proved in full.
4. Edge cases handled: unknot (lens spaces); manifolds with S^1 x S^2 summands
   excluded by the b_1 = 0 argument for |p| >= 2 and by the cabling theorem for
   |p| = 1; the special case "reducible surgery on a genus-one L-space knot"
   subsumed by the general length argument; term-by-term verification of the
   floored sum and adjunction-inequality computations.

## IMMUTABLE SECTION Note

This contract's immutable scope decisions are fixed as of Round 0.
