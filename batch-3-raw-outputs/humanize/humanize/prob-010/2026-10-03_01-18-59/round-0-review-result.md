# Round 0 Review Result (Reviewer: Kimi-k3, max effort)

## Scope of review

Read in full: `plan.md`, `problem.tex`, the round-0 prompt, the round-0
contract, the goal tracker, and all 736 lines of `solution.tex`. Verified
`pdflatex solution.tex` compiles twice with exit code 0, no LaTeX errors,
no undefined references, 10 typeset pages (AC-5 satisfied: begins with
`\documentclass[11pt]{article}`, ends with `\end{document}`, only allowed
packages, no Markdown/commentary). Commit 4bc6512 exists; `.gitignore`
commit 84c0d90 present.

## Part 2: Goal Alignment Summary

ACs: 5/5 addressed structurally (AC-1/AC-4 governed by mathematical
gaps below) | Forgotten items: 0 | Unjustified deferrals: 0

The immutable section (Ultimate Goal, ACs) matches the plan. Both active
tasks are marked done; the completion row is honestly marked "pending
verification". The tracker needs one post-review adjustment (added Queued
Side Issue Q-1 below); I have made that edit myself per Part 5.

## Part 3: Capability Alignment Summary

Capability anchor: N/A (plan has no Feature Map / Capability Map) |
Dependency gaps: 0 | Scope drift: no

## Part 4: Findings

### Mainline Gaps

The proof has the correct overall architecture (Dolgachev--Nikulin
duality, explicit fibration y^2 = x^3 + c t^4 x + t^5 beta(t),
II* + II* + 4 I_1 fibre analysis, centroid loop, dual complex S^2,
filtration matching, quote of [GT, Theorem C]), and the Weierstrass
computation in Lemma 2 (Tate orders at 0 and infinity,
Delta = t^{10}(4 c^3 t^2 + 27 beta^2), four residual simple roots) is
correct and well done. However, against AC-1/AC-2 ("a specialist can
verify the argument line by line"; "no substantive lemma left
unproved"), the following genuine gaps remain. None require
restructuring; all are localised repairs.

**M-1 (Definition 5.1(3) checkerboard and dual-complex matching).**
Prop 4 (deg-side, item (c)) asserts Gamma(X_0) is "a triangulation of
S^2 with 2 vertices, one edge, and 2 triangular faces", while Thm 4(b)
asserts Gamma(Y,gamma) is "a triangulation of S^2 with 4 edges and 2
faces meeting along the equatorial 4-gon" (2 vertices, 4 edges, 2
faces: chi = 0, and "triangular faces" is inconsistent with the 4-gon
equator on the other side). These two asserted complexes cannot be
identified as complexes: the degeneration side has one edge (the smooth
double curve C), the fibration side has four edges (the four double
curves of the Type III model associated to gamma). Definition 5.1(3)
only requires a homeomorphism plus a compatible checkerboard structure,
so the result survives, but the solution must state this honestly:
  * Declare Gamma(X_0) = S^2 with cell structure (2 vertices, 1 edge,
    2 bigonal faces) and explain that subdividing the single edge into
    4 edges yields the pillowcase cell structure of Gamma(Y,gamma),
    matching the notation of [GT, 4.11--4.14].
  * Remove the phrase "matching Proposition 4(c)" at the end of
    Thm 4(b) or replace it by the subdivision statement.
  * The checkerboard paragraph after Thm C ("the pillowcase
    triangulation is the 2-colouring of the two faces") must be
    corrected: the checkerboard data in [GT, 5.1(3)] is a compatible
    2-colouring (bipartition) of the vertices of the triangulation
    together with the light-leaf condition. Here the dual graph of the
    equatorial subdivision is a 4-cycle, which is bipartite precisely
    because 4 is even, so the vertex 2-colouring exists; state this,
    and dispose of the light-leaf clause (identify the two large
    faces / E_8's, or state that the condition is vacuous in this
    rk N = 18 case). Currently the 2-colouring is asserted for faces,
    which is the wrong slot in the definition.

**M-2 (Definition 5.1(4): present one lattice carrying both
filtrations).** GT Definition 5.1(4) asks for filtrations on both sides,
living on isometric lattices, with an isometry Phi respecting both
W_2-lines and both quotient pairings. The solution shows the two sides
have abstractly isomorphic quotients (E_m/W_2 = N, E_m'/E_m = U(-1))
and says "Phi is the identity in our identification". This is not yet a
verification: the pairing between E_m/W_2 and E_m'/E_m and the
polarisation embeddings on both sides must be shown to correspond
under Phi. Repair: in Thm 4(d), define E_m := N plus Z f (rank 19)
with the intersection form making f isotropic and pairing with N via
the H-summand; give the two embeddings (degeneration side: v maps to
f; fibration side: fibre class maps to f); exhibit Phi explicitly (it
may be the identity); and state that both quasi-polarisations map to
sigma + 2f. Four to six lines of form-matrix computation suffice.

**M-3 (Deg-side E_m(X)/W_2 = N is not proved).** Prop 4(d) reduces the
central computation E_m(X)/W_2 = H + E_8 + E_8 to "a direct
computation ... shows it is isomorphic to N" and then defaults to
"These are exactly the computations carried out in [GT, Example 1.2
and Section 4.1] ... so we record the result". Quoting a computation
from GT is acceptable (GT is the framework of the problem), but then it
must be quoted as a cited external result with hypotheses, as is done
elsewhere for Theorems B/C, not presented as proved. Repair: replace
the sentence by "By [GT, Example 1.2], for the very general H-polarised
Tyurin degeneration E_m/W_2 = H + E_8^{+2} and E_m'/E_m = U(-1)",
exactly parallel to the treatment of Theorem C (two lines, honest).

**M-4 (Prop 4(a) mischaracterises the very-generality hypothesis).**
"the very generality hypothesis says precisely that ... avoids them,
giving NS(X_t) = H for all t in Delta" conflates the generic Picard
rank with the Picard rank at every parameter, and
"Imprimitive-cusp-free Type III boundary stratum" is not standard
terminology. Repair: replace by "for very general t in the punctured
disc; the image of 0 lies in the Type III boundary stratum of the
Alexeev--Brunyate--Engel compactification and avoids all
Noether--Lefschetz loci, as assumed".

**M-5 (Lemma 3 statement garbled).** The statement "vanishes exactly
on the two E_8-root systems" contradicts its own proof, which correctly
notes h . sigma = 0 as well. Repair the statement to: h . C = 0 for an
effective (-2)-curve C if and only if C is the section sigma or a
component of the two II* fibres, and |m h| contracts exactly these; the
image has two Du Val E_8 singularities; and the contracted
configuration is the one of [GT, Example 4.20] with k = 2, which the
proof already cites. Also fix "relative to the $nef$ class" (roman
type) and the garbled sentence "h.sigma = 0 precisely means sigma spans
the -2-direction of H and is semiample-contracted together with the
fibre roots".

**M-6 (Proof of Lemma 1, the section).** "up to replacing sigma by
sigma + k f and more precisely by a (-2)-curve in its numerical class
after applying reflections in roots" is garbled. Replace with the clean
three-line argument: Riemann--Roch gives
h^0(sigma) + h^0(-sigma) >= 1; the chamber choice forces effectivity of
sigma up to the E_8-Weyl group, which fixes f and h; an effective
(-2)-class with sigma . f = 1 and no root decomposition is irreducible
of arithmetic genus 0, hence a section (standard, cf. Saint-Donat).

**M-7 (Statement of Lemma 2 punctuation).** The display listing the
four I_1-roots runs straight into "conversely all generic such
(c, beta)" without a period; one-character fix.

### Blocking Side Issues

None beyond M-1--M-7 (they are mainline completeness gaps, not side
issues).

### Queued Side Issues

Q-1 (cosmetic): Prop 4(b)'s sentence "the maximality rk N = rk H^2
- rk H - 1-bounds are standard" is ungrammatical; the Remark after
Thm C writes "H^{perp-ish}" informally; Lemma 3's proof has "$nef$"
in italic limbo. Fix opportunistically in the same editing pass; do
not schedule a separate round.

## Round-0 contract cross-check

The contract's success criteria mention "explicit period-map
computation of W(Y)" (done: Remark 1 plus Shioda--Tate), "the
I_{18} + I_1 + I_1 cusp" (the actual fibre configuration is
II* + II* + 4 I_1; the contract's phrase was a placeholder and the
implementation correctly supersedes it -- recorded here as an
intentional, correct plan refinement, not a gap), and "checkerboard
condition checked over an explicit 18-element integral basis"
(partially done; see M-1 and M-2). The contract items not fully met
are exactly M-1 and the filtration display of M-2.

## Directive implementation plan for Round 1 (all edits in solution.tex)

1. Prop 4(a) and (c): rewrite as in M-4 and M-1 -- correct the
   generality sentence; in (c) state the cell structure (2 vertices,
   1 edge, 2 bigonal faces) and add one sentence on the 4-fold
   subdivision matching the pillowcase.
2. Thm 4(b): add the subdivision/homeomorphism sentence; delete
   "matching Proposition 4(c)".
3. Thm 4(d): insert the explicit E_m := N plus Z f model, the two
   embeddings, Phi = identity, and the pairing/polarisation check
   (M-2); 4--6 lines.
4. Checkerboard paragraphs (after Thm C and the final remark):
   replace "2-colouring of the faces" by the vertex bipartition of the
   equatorial 4-cycle, note that 4 is even hence bipartite hence the
   checkerboard exists, and dispose of the light-leaf clause (M-1).
5. Prop 4(d): re-quote E_m/W_2 = N and E_m'/E_m = U(-1) as a cited
   external result from [GT, Example 1.2], mirroring the Theorem C
   treatment (M-3).
6. Lemma 3 statement and Lemma 1's section sentence: apply the M-5
   and M-6 repairs (about five lines total).
7. Punctuation/grammar fixes from M-7 and Q-1 in the same pass.
8. Re-run pdflatex twice; confirm at most 16 pages (expected +0 to
   +1 page); commit.

All repairs are local; no change to the proof architecture. After these
edits the document satisfies AC-1/AC-2 at the specialist line-by-line
level, taking [GT]'s Theorems B/C and definition framework as cited
external input, which the problem statement itself presupposes.

## Verdict

The mainline advanced substantially (full architecture assembled; the
hard computations -- Weierstrass/Tate/discriminant, Dolgachev--Nikulin
duality, fibre count -- done correctly), but the verification of
Definition 5.1(3)--(4) and the statements of Prop 4(a), Prop 4(c) and
Lemma 3 are not yet at the bar set by AC-1/AC-2. Not complete.

Mainline Progress Verdict: ADVANCED
