# Round 1 summary (no results yet; round 1 is the first wave)

## Problem / goal
Decide: in every hyperfield, does 0 ∈ x⊞y⊞z imply 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz? Ledger [GOAL] line: the universal claim, OPEN; settle by proof or refute by explicit counterexample.

## Coordinator's own observations (plan step, not from result files; elementary, but re-check before use in proof.md)
- Normalization: z = 0 is trivial (y = -x, target x^3⊞-x^3 ∋ 0). For z ≠ 0 scale by -1/z: equivalent to "1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy⊞xy⊞xy" (x, y nonzero WLOG).
- Quotient hyperfields F/U of fields satisfy the implication (lift to representatives with x'+y'+z' = 0, use the field identity). So Krasner, sign, tropical, phase, triangle etc. all satisfy it; a counterexample must be non-quotient.
- Expansion (w ∈ wx⊞wy) only enlarges sums; the field identity needs cancellation of 12 of 18 terms of (x+y+z)(x^2+y^2+z^2-xy-yz-zx), which is not available in hyperfields. A proof must use reversibility/element-level witnesses; a counterexample must be a hyperfield where this is genuinely lacking.
- Easy checks done by hand: Krasner-extension "Massouros" type (x⊞y = {x,y}, x⊞x = H\{x}, char 2) satisfies it; "x⊞y = {x,y}" type rules satisfy it.
- Exhaustive computer search (coordinator, Python backtracking over S_g = 1⊞g, checking all axioms): no counterexample among all hyperfields with |G| ≤ 8 (all abelian groups of order ≤ 8; e.g. 3806 labelled hyperfields for G = Z2^3), nor |G| = 9 (Z9 and Z3×Z3). So a counterexample has ≥ 11 elements.

## Established from result files
Nothing yet.

## Open gaps
- The whole question. Neither a proof route nor a counterexample candidate is known.

## Round 1 wave (where to concentrate)
Exploration with four independent lenses, all attempts at the goal:
- q1: direct proof attempt via element-level membership chains/reversibility (fallback counterexample).
- q2: explicit counterexample constructions (non-quotient: custom S_g on larger/infinite groups, Massouros/Nakassis, Krasner extensions / incidence geometries, ordered-group extensions).
- q3: "free/minimal hyperfield closure" lens: closure of the single relation 1 ∈ x⊞y under the axioms; either a model avoiding the conclusion or a derivation.
- q4: class-by-class (char-2-like, a⊞a={a}, stringent, doubly distributive, large a⊞-a) plus forced-constraints analysis of a minimal counterexample.
Next round: fold results; if a counterexample or proof appears, send two verify queries on it verbatim; otherwise sharpen the most promising lens.
