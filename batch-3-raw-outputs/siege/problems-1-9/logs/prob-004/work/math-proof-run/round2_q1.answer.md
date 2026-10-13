# round2_q1 — answer (partial)

**Status.** I did not complete the proof of YES in general dimension. Below:
(A) the answer YES, proved (with cited inputs) for dim_R M ≤ 4;
(B) a non-relative reduction, proved, that avoids the relative line bundle lemma whenever the needed classes are differences of *disjoint* hypersurfaces;
(C) where the planner's global-configuration route stops, and the precise gap.

## A. dim_R M = 2 and 4 (proved modulo cited TMZ)

*dim 2.* D is a finite set of points, and every almost complex structure is integrable (NN). Take any tame J. Near p ∈ D, a local J-holomorphic coordinate z with z(p)=0 gives D = {z=0}, with r=1. Elsewhere r=0.

*dim 4.* Apply TMZ (cited from memory, as stated in Result 3) to get a regularization after a permitted deformation. Near each point q of a double point D_{ij}, the model is (N_{D_i} ⊕ N_{D_j})|_q = C^2 with the form ω_q + ½ Σ d(ρ_k α_k) and trivial connections. Set J = i ⊕ i there; it is integrable, and the coordinates z_i, z_j are holomorphic.

On each surface D_i:
- J_i := an extension of the standard structure near the points D_i ∩ D_j. It is integrable by (NN).
- Put a ∂̄-operator on N_{D_i} extending the trivial one near those points (∂̄-operators form an affine space; glue with a partition of unity). Over a Riemann surface every ∂̄-operator on a line bundle is integrable: locally ∂̄u = −α is solvable. So N_{D_i} gets a J_i-holomorphic cocycle that is trivial near the points.
- Take a Hermitian metric that is standard near the points. The Chern connection has (1,0) forms in holomorphic frames, and it is trivial near the points.

By Lemma C, replace the TMZ connection by this one; this is a permitted deformation, and the connection is unchanged near the points, so it stays compatible. By Lemmas A and B, J_∇ is tame near D_i, its fibre coordinate is holomorphic, and it equals J = i ⊕ i near the points. Extend J tamely to M, since the space of tame structures has contractible fibres. This gives the required coordinates everywhere.

## B. Non-relative reduction (proved)

**Lemma.** Let (B, ω_B) be closed and L → B a complex line bundle. Suppose:
- L ≅ O(E_1) ⊗ O(E_2)^{-1}, where E_1 and E_2 are *disjoint* closed symplectic hypersurfaces;
- each N_{E_k} admits a J_{E_k}-holomorphic cocycle for a tame J_{E_k}.

Then L admits a J_B-holomorphic cocycle for some ω_B-tame J_B.

*Proof.*
1. Proposition 3 applied to E_k ⊂ B gives a tame J near E_k with a holomorphic defining function f_k on a tube U_k. Extend J tamely to J_B on B.
2. Cover B by U_1, U_2 and V = B minus smaller closed tubes. Since E_1 ∩ E_2 = ∅, U_1 ∩ U_2 = ∅.
3. The cocycle g_{U_1V} = f_1 and g_{U_2V} = 1/f_2 (nonvanishing on the overlaps) is holomorphic and represents O(E_1) ⊗ O(E_2)^{-1}. ∎

This gives an induction on dimension with no relative statement, *provided* every needed class is such a disjoint difference. I could not establish that. Donaldson hypersurfaces in classes c + kPD[ω'] and kPD[ω'] always intersect when n ≥ 2, because their intersection has positive volume. So this is open.

## C. Planner's route: where it stops

- Steps 1–2: the configuration via Donaldson–Auroux transversal sections, then TMZ. I believe these are plausible, but I did not check the hypotheses (snag (iv)).
- Step 4 is the gap. On a needed stratum C_J we must glue several divisor-induced cocycles near the deeper strata C_{J∪{b}}. Pulled back from a deeper stratum, the cocycle of O(P)|_{C_J} need not agree with the divisor cocycle of P ∩ C_J when P ∈ J ∪ {b} \ J.
  - Where P = C_b itself, the structure is the recursive N_{C_b}. Near C_{J∪{b}} it must match both pullback data and the divisor data of the partners of b, which also meet C_J.
  - Matching these is again a relative extension of holomorphic structures over C_J ∖ (neighbourhood of the deeper strata). That is the same obstruction the route was designed to avoid, and I could not remove it.

In dimension 4 this is harmless only because of (A): holomorphic structures over Riemann surfaces extend relatively.

**Open:** the relative line bundle lemma, or the disjoint-difference representability, for real dim D_I ≥ 4. The general case (dim_R M ≥ 6) is therefore NOT proved here. The expected answer YES remains unconfirmed by this work.

=== END OF ANSWER round2_q1 ===
