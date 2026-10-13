# Round 1, q3: assembly for r >= 2, assuming a relative line bundle lemma

Conventions are those of the task file. "Pseudo-holomorphic" means J-holomorphic. "Proved" below means proved modulo the cited results and the hypothesis (RLB). Gaps are marked **GAP**.

## 0. Cited results (from memory)

**(TMZ)** Tehrani–McLean–Zinger, "Normal crossings singularities for symplectic topology". Let D = ∪D_i be an SC divisor in (M, ω). Then ω can be deformed through cohomologous symplectic forms, keeping D an SC divisor, to a form (still called ω) that admits an ω-regularization. This means the following. For every I there are:
- Hermitian structures (ρ_{I;i}, ∇_{I;i}) on the line bundles N_{D_i}|_{D_I}, for i ∈ I;
- a tubular embedding Ψ_I from a neighbourhood of the zero section of N_I = ⊕_{i∈I} N_{D_i}|_{D_I} into M.

These satisfy:
1. Ψ_I^*ω = ω_{(ρ,∇)} := π^*ω|_{D_I} + ½ Σ_{i∈I} d(ρ_i α_i), where α_i is the connection 1-form of ∇_i.
2. Ψ_I^{-1}(D_i) is the bundle {z_i = 0} for i ∈ I.
3. Compatibility for I ⊂ I'. Over D_{I'} we have N_{I'} = N_{I'−I}D_I|_{D_{I'}} ⊕ N_I|_{D_{I'}}. The maps Ψ_{I'} and Ψ_I agree after composition with the induced tubular map of D_{I'} inside D_I. Under this identification the Hermitian structures on N_{D_i}|_{D_I} near D_{I'} are the pullbacks, by the model projection, of the ones on N_{D_i}|_{D_{I'}}.

**(NN)** On a 2-dimensional manifold every almost complex structure is integrable.

**(Moser)** On a closed manifold, if ω_t is a path of cohomologous symplectic forms, there is a diffeomorphism φ isotopic to the identity with φ^*ω_1 = ω_0.

## 1. The hypothesis

**(RLB) Relative line bundle lemma.** Let:
- (B, ω_B) be a compact symplectic manifold, possibly with boundary;
- K ⊂ B be a closed subset with a neighbourhood U;
- J_U be an ω_B-tame almost complex structure on U;
- L → B be a complex line bundle with Hermitian metric h, carrying over U a cocycle of nonvanishing J_U-holomorphic functions;
- the Chern connection of (cocycle, h) agree with a given unitary connection ∇ on U.

Then there exist:
- an ω_B-tame J_B on B with J_B = J_U near K;
- a J_B-holomorphic cocycle for L extending the given one near K;
- a unitary connection ∇' equal to ∇ near K whose local connection forms (in the holomorphic frames) are of type (1,0).

## 2. Key local fact: the connection almost complex structure

**Lemma A.** Let B carry an almost complex structure J_B. Let E = ⊕ L_i → B carry connections ∇_i. Define J_∇ on the total space as follows: on the horizontal subspace it is the lift of J_B; on the fibres it is i.

Let s_i be a local frame with ∇ s_i = θ_i s_i, and let z_i be the matching fibre coordinates. Then:
- z_i is J_∇-holomorphic if and only if θ_i is of type (1,0) for J_B;
- the projection π is (J_∇, J_B)-holomorphic;
- if f is J_B-holomorphic, then π^*f is J_∇-holomorphic.

*Proof.* Horizontal vectors are the kernel of dz_i + θ_i z_i. Hence dz_i(h(v)) = −θ_i(v) z_i.

z_i is J_∇-holomorphic iff dz_i∘J_∇ = i·dz_i. On vertical vectors this holds automatically. On a horizontal lift h(v) it reads −θ_i(J_B v) z_i = −i θ_i(v) z_i for all v and all z_i, that is, θ_i∘J_B = iθ_i. This is exactly the (1,0) condition.

The statements about π hold by construction. ∎

**Lemma B (tameness).** Let ω_{(ρ,∇)} be as in TMZ and J_B be ω|_B-tame. Then J_∇ is ω_{(ρ,∇)}-tame on a neighbourhood of the zero section.

*Proof.* Along the zero section, ω_{(ρ,∇)} is the direct sum of ω_B and the standard fibre forms, and J_∇ = J_B ⊕ i. Tameness is an open condition, and B is compact. ∎

**Lemma C (changing ∇ costs only a permitted deformation).** Let ∇' = ∇ + iβ, with β a real 1-form on B that vanishes near K. Then ω_t = ω + ½ d(χ ρ t β), t ∈ [0,1], is a path of cohomologous symplectic forms. Here χ = χ(ρ) is a cutoff equal to 1 for ρ < ε² and 0 for ρ > 4ε², and ε is small.

*Proof.* The forms are cohomologous because the change is exact. For symplecticity, write d(χρβ) = (χ'ρ + χ) dρ∧β + χρ dβ. The coefficient χ'ρ + χ is O(1), and |dρ| = O(ε) on the support, so the change is O(ε) in C⁰ against the fixed nondegenerate ω. For small ε the forms stay symplectic.

D stays SC: the strata are unchanged, the zero sections stay symplectic, and the normal-form structure is unchanged near D, where χ = 1. ∎

Where χ = 1, ω_1 is the regularized form for ∇'. So any regularization may be changed to one whose connections have (1,0) forms in holomorphic frames, at the price of a permitted deformation. Doing this stratum by stratum requires the new ∇' to satisfy the compatibility condition 3. This holds by the construction order below, because each ∇' equals the already-pulled-back connection near deeper strata.

## 3. Assembly (proved, assuming TMZ and RLB)

Order the strata D_I by decreasing |I|, i.e. deepest first. By induction on the strata we construct, for each I:
- (a) an ω|_{D_I}-tame J_I on D_I;
- (b) for each i ∈ I, a J_I-holomorphic cocycle on N_{D_i}|_{D_I}, with the regularization connection ∇_{I;i} having (1,0) forms in these frames (after Lemma C);
- (c) for every I' ⊋ I: near D_{I'}, inside the model of D_I, J_I equals the connection structure J_∇ built from data (a), (b) on D_{I'}, and the cocycles of (b) are π-pullbacks of those on D_{I'}.

**Step for I.** Let K = ∪_{I'⊋I} D_{I'}. This is the union of the deeper strata contained in D_I, a closed subset.

Near each D_{I'}, the model of D_I is the bundle N_{I'−I}D_I → D_{I'}. The inductive data on D_{I'} define J_∇ there.

- Different I' are consistent on overlaps: an overlap near D_{I'} ∩ D_{I''} is a neighbourhood of D_{I'∪I''}, and both structures are J_∇ pulled back from that deeper stratum. This uses compatibility condition 3 and statement (c) for I' and I''.
- Lemma B gives tameness after shrinking.

Choose U a neighbourhood of K. RLB applied to B = D_I, the bundle L = N_{D_i}|_{D_I} and the pulled-back cocycles then gives (a) and (b), first for one i. **GAP 1:** RLB must be applied to all i ∈ I with a single J_I. RLB as stated produces a new J_B for each bundle, so we must strengthen it to finitely many line bundles simultaneously. Call this RLB_m.

**Base case.** The deepest strata either have K = ∅, or are points or surfaces. For surfaces, NN makes every J integrable, so RLB is the classical fact that holomorphic line bundles of every degree exist and holomorphic structures extend relatively. This is standard. **GAP 2:** the relative version is not written out here.

**Final J on M.** Take the model of D_∅ = M near each stratum. On Ψ_I(N_I) define J = J_∇ from the data on D_I. By (c) and condition 3 these definitions agree on overlaps.

In the coordinates Ψ_I, the fibre coordinates z_i, i ∈ I, are J-holomorphic by Lemma A. They cut out D_i by condition 2, and their differentials are C-independent, being independent fibre coordinates.

J is tame near D by Lemma B. Extend it to an ω-tame J on M: ω-tame structures form a bundle with contractible fibres, so an extension from a closed neighbourhood exists.

This answers the question YES, under TMZ and RLB_m.

## 4. Is the hypothesis needed?

**Necessity (proved modulo removable singularities).** Suppose J and coordinates as in the question exist. Then for each i, J|_{D_i} is ω-tame on D_i, and N_{D_i} has a J|_{D_i}-holomorphic cocycle. The argument is O1 of the task:
- z'/z is J-holomorphic off D_i and bounded near D_i, hence extends J-holomorphically across D_i (removable singularity in codimension 2 for J-holomorphic functions). **Cited from memory, not proved here.**
- Its restriction to D_i is the transition function of N_{D_i} = (dz)|_{D_i}^{-1}.

So the plain line bundle lemma, for the line bundles N_{D_i} on the specific manifolds D_i, is necessary. The relative form is what the inductive construction uses; I did not prove that the relative form is necessary.

## 5. Does RLB follow from the plain lemma? Reduction by induction on dimension (sketch)

Let L → (B^{2m}, ω_B) be a complex line bundle.

1. **Representing c_1(L).** Using Donaldson/Auroux asymptotically holomorphic sections (cited from memory), pick symplectic hypersurfaces E_1, E_2 ⊂ B that are transverse with positive intersection, so that E_1 ∪ E_2 is SC, with L ≅ O(E_1) ⊗ O(E_2)^{-1}.
   - Construction: take sections of L ⊗ P^k and of P^k, where P is prequantum for a rational ω' close to ω_B.
   - Hypersurfaces that are nearly J'-complex are also ω_B-symplectic.
2. **Holomorphic cocycle from the divisor problem.** If J_B makes E_1 ∪ E_2 have J_B-holomorphic local defining functions w, then ratios of these give a J_B-holomorphic cocycle for O(E_1 − E_2) ≅ L. So RLB in dimension 2m follows from the question itself for the SC divisor E_1 ∪ E_2 ⊂ B. By §3, that follows from RLB in dimension 2m − 2.
3. **The deformation of ω_B is harmless.** TMZ may deform ω_B to ω'_B. Moser gives φ, isotopic to id, with φ^*ω'_B = ω_B. Then φ^*J is ω_B-tame, φ^{-1}(E_1 ∪ E_2) is still SC, and φ^*L ≅ L.

So the plain (non-relative) lemma holds in every dimension by induction from dimension 2, modulo the cited results. **This argument is only sketched.**

**GAP 3:** in the relative setting, Moser's φ and the choice of E_1, E_2 must respect K. The hypersurfaces must agree near K with the given data, and φ must equal id near K. I have not proved this.

So: the plain lemma follows (sketch), but RLB_m does not, as far as shown here.

## Summary

- **Proved, modulo TMZ and RLB_m:** YES. This relies on the connection-J construction (Lemmas A–C) and the deepest-first assembly (§3).
- **Proved, modulo removable singularities:** the plain line bundle lemma on each D_i is necessary.
- **Sketched:** the plain lemma in all dimensions, by induction on dimension.
- **Open:**
  - GAP 1: the simultaneous version of RLB for several line bundles;
  - GAP 2: the relative version in the surface base case;
  - GAP 3: the relative version of the Donaldson/Moser step.

=== END OF ANSWER round1_q3 ===
