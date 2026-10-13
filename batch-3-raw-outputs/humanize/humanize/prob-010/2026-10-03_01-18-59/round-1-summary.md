# Round 1 Summary

## What Was Implemented

Repaired all seven mainline gaps M-1..M-7 from the Round-0 review, plus
the queued cosmetic issue Q-1, in solution.tex (architecture unchanged;
all edits local, as the review prescribed):

1. M-1 (Def 5.1(3), dual-complex + checkerboard):
   - Prop 4(c) now states Gamma(X_0) ≃ S^2 with the minimal cell structure
     (2 monogonal 2-cells, 1 loop edge, 1 vertex; chi = 1-1+2 = 2) and an
     explicit 4-fold subdivision into the pillowcase cell structure.
   - Thm 4(b) now describes Gamma(Y,gamma) as the quadrangulated pillowcase
     (4 vertices, 4 edges, 2 quadrilateral faces; chi = 2), homeomorphic
     to (a subdivision of) Gamma(X_0) — no longer "matching Prop 4(c)" as
     an identification of complexes.
   - The checkerboard clause is now a vertex bipartition of the equatorial
     4-cycle (bipartite since 4 is even), with the light-leaf condition
     disposed of explicitly (two leaf branches, both carrying II*-fibres,
     same leaf type); the wrong "2-colouring of the faces" assertion is
     removed. In Prop 4(c) a former (E,V,F) = (2,1,2) triangulation claim
     (chi = 3, impossible) is replaced by the corrected (1,1,2) minimal
     structure found during the repair.
2. M-2 (Def 5.1(4), one lattice carrying both filtrations): Thm 4(d) now
   defines the explicit rank-19 model E := N \oplus Z f' with (f')^2 = 0,
   f'·f = 1, gives both embeddings (degeneration side: v -> f; fibration
   side: fibre class -> f), takes Phi = identity on N with v -> f, and
   verifies the four requirements item by item: W_2-lines match, Phi is
   the identity on E_m/W_2 = N on both sides, the pairing between
   E_m/W_2 = N and E_m'/E_m = U(-1) is the unimodular pairing of H = U on
   both sides (realised in the model by f·f' = 1), and both
   quasi-polarisations map to sigma + 2f.
3. M-3 (deg-side E_m/W_2 = N): Prop 4(d) no longer presents this as
   proved; it is now quoted as an external computation from [GT,
   Example 1.2] with hypotheses stated, parallel to the treatment of
   Theorem C, retaining the rank data (rk E_m = 18, rk E_m' = 20) actually
   used below.
4. M-4 (Prop 4(a)): statement and proof no longer conflate generic Picard
   rank with the rank at every parameter; the claim is "for very general t
   in the punctured disc, NS(X_t) = H", and the Type III boundary +
   Noether--Lefschetz avoidance is stated as the assumed hypothesis.
   "Imprimitive-cusp-free" and the pi_0 sentence removed.
5. M-5 (Lemma 3): statement now says h = sigma + 2f is big and nef and
   h·C = 0 for an effective (-2)-curve C iff C is the section sigma or a
   component of one of the two II*-fibres, with |mh| (m >= 2) contracting
   exactly these and Du Val E8 + E8 image. The garbled proof sentence is
   replaced by a coherent argument: contractions computed; converse split
   into horizontal (a >= 1: then C is a section, and effectivity +
   C·sigma force C = sigma) and vertical (a = 0: then C is a fibre
   component, hence one of the two E8 root systems) cases; nefness and
   bigness deduced; Saint-Donat applied.
6. M-6 (Lemma 1, section): replaced by the clean three-line argument —
   Riemann--Roch gives h^0(sigma) + h^0(-sigma) >= 1; E8-Weyl reflections
   (fixing f and h) arrange effectivity of sigma; an effective (-2)-class
   with sigma·f = 1 is irreducible of arithmetic genus 0, maps
   isomorphically to P^1, and is a section (citing Saint-Donat).
7. M-7: period inserted in Lemma 2's statement before "Conversely...".
8. Q-1 folded in: "rk N = rk H^2 - rk H - 1-bounds are standard"
   reworded to the standard bound rk N <= 20 - rk H with equality for a
   maximal cusp; "H^{perp-ish}" replaced by "N be DN-dual to L = H with
   mirror lattice \bar N = H"; italic "$nef$" occurrences eliminated;
   the Theorem C quote placeholder "L of rank 2N-type 20 - rk N" replaced
   by "rk N <= 18". A stray unused \newtheorem{definitionn} remains
   harmless (never referenced).

## Files Changed

- solution.tex (commit d0ad78a; +173/-109 lines)
- .humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md (created)
- .humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md (updated)

## Validation

- pdflatex solution.tex run 3 times: exit code 0, no LaTeX errors, no
  undefined references/citations, 11 typeset pages (<= 16).
- Structural checks: begin{lemma}/end{lemma} counts balance (3/3);
  theorem environments compile; document still begins with
  \documentclass[11pt]{article} and ends with \end{document}; only allowed
  packages.
- Committed as d0ad78a on branch humanize-rlcr with a specific-path stage.

## Remaining Items

None known; awaiting Round-1 review.

## BitLesson Delta

Action: add
Lesson ID(s): BL-20261003-dual-complex-cell-structure
Notes: During the M-1 repair I first wrote a (V,E,F) = (2,1,2) cell
structure for S^2, which has chi = 3 and is impossible; caught by
recomputing Euler characteristic. Lesson recorded: every claimed cell
structure of a topological surface in a proof must have its Euler
characteristic recomputed inline before being written down.
