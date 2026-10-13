# round3_q1: referee report on the YES proof chain

Plan: check each step of Part 1 and Part 2 in order, then give a verdict. Everything cited below is cited from memory.

## 0. A preliminary remark on conventions (it matters for the answer)

The chain uses the TMZ convention, in which positivity is part of "SC divisor". **This is necessary.** Without
positivity the answer is NO. Here is the reason.
- In a J-holomorphic local model {z_1 z_2 = 0}, the components are J-complex. A transverse intersection point of
  two J-complex hypersurfaces is positive for the complex orientation, and that orientation equals the
  ω-orientation because J is tame.
- Positivity is not implied by "transverse with symplectic strata". Example in (C^2, ω_std): take D_1 = {z_2 = 0}
  and D_2 = {z_2 = ε z̄_1} with 0 < ε < 1.
  - ω restricted to D_2 is (1 − ε²) dx_1∧dy_1 > 0, so D_2 is symplectic.
  - The two planes are transverse.
  - Basis: (1,0,0,0), (0,1,0,0), (1,0,ε,0), (0,1,0,−ε). Its determinant is −ε² < 0, so the intersection sign is
    negative.
- The sign of an intersection point is unchanged along any path of forms keeping D transverse. So no permitted
  deformation repairs it.

From here on the TMZ convention (positivity included) is assumed, as the chain does.

## 1. Cited results

**(TMZ).** From memory: Tehrani–McLean–Zinger, Adv. Math. 2018. The projection from the space of pairs
(ω, ω-regularization of D) to Symp^+(X,D) is a weak homotopy equivalence. In particular every ω ∈ Symp^+(X,D)
can be joined, inside Symp^+(X,D), to a form that admits a regularization.
- Their regularizations are systems (ρ_{I;i}, ∇^{(I;i)}, Ψ_I). They satisfy the standard-form condition
  Ψ_I^*ω = ω_{(ρ,∇)} and compatibility Ψ_{I'} = Ψ_I ∘ (overlap map) for I ⊂ I'. This is (R1)–(R3) as stated.
- (R4) is the "after shrinking" consequence of that compatibility: intersections of tubes lie in the tube of the
  union, and π_K preserves z_c.
- I derived "π_K preserves z_c" myself from the compatibility on U_{K∪c}. In N_{K∪c}-coordinates, π_K is
  (z_K, z_c, x) ↦ (0, z_c, x).
- **Not certain from memory: that the path can be taken cohomologous.** It is very plausible, by the following
  standard argument, which I only sketch.
  - Near C_I the orthogonalized model form and ω have the same restriction to TC_I.
  - Their difference is therefore a closed 2-form on the tube whose pullback to C_I vanishes. It is exact,
    = dμ, with μ = 0 along C_I.
  - The interpolation ω + d(χ μ_t) is exact and compactly supported near D.
  - I believe McLean ("growth rate of symplectic homology") and TMZ deform exactly this way, by forms
    ω + dμ supported near D. I cannot certify the precise published statement.

**(AH).** Every ingredient is published:
- Donaldson 1996 (J. Diff. Geom.);
- Auroux 1997 (GAFA): sections of E ⊗ L^k, η-transversality of vector-valued sections, families;
- transversality of restrictions to fixed J-complex submanifolds, as used in Donaldson's pencils (1999) and in
  Auroux's later works;
- the non-integral case, handled by approximating [ω] by rational classes, or as here by an O(1) curvature
  error.

I know of no single reference that states the combined form (finitely many exactly J-complex Σ_j, all
sub-tuples, a fixed twist E, an O(1) unrescaled curvature error). The combination is routine:
- localized reference sections centred on Σ restrict to localized sections on Σ;
- the error is O(k^{-1}) after rescaling;
- conditions are imposed one after another, with perturbations smaller than half the previous constant.

So (AH) is "standard, but not published in this form".

## 2. Part 1, step by step

- **Lemma 0: correct.**
  - Step 2: a compatible J preserving W also preserves W^ω, hence N_i = T C_{I−i} ∩ W^ω.
  - Step 3: product of contractible spaces.
  - Step 4: two points need checking.
    - The S^{I'} bundle is defined and smooth over all of C_{I'}. For this, ω-orthogonality of the splitting is
      needed at every point of C_{I'}, including points of C_{I'} inside tubes of deeper strata. It holds in the
      TMZ standard form: on C_{I'} we have ρ_a = 0 and dρ_a = 0 for a ∈ I', so the mixed terms dρ_a ∧ π^*A
      vanish there.
    - The data already defined at points of C_{I'} lying in deeper strata lie in the smaller sets S^{I} ⊂ S^{I'}.
  - Extension of a section with contractible fibres from a closed set: fine.
- **Lemma 1, integrality (step 2): correct.**
  - The image of H²(M;Z) is a full lattice.
  - η_k = O(1/k), and P_k carries a connection with curvature −2πik(ω_l + η_k).
  - c_1(P_k) = c_k is integral, torsion included.
  - Step 3: PD[Z(s^+)] − PD[Z(s^-)] = c_1(L_a) + c_k − c_k = PD[C_a] in H²(M;Z). This is right: the zero set of
    a transverse section of a complex line bundle, oriented compatibly, is Poincaré dual to c_1 integrally. The
    complex and symplectic orientations agree by step 5.
- **Step 4: correct.** Transversality of every sub-tuple on every Σ is exactly transversality of the enlarged
  configuration.
- **Step 5: correct.**
  - (AH') holds: the kernel of ∂s + ∂̄s, with |∂̄s| ≤ Ck^{-1/2} and ∂s surjective with bound η, lies within
    O(k^{-1/2}/η) of the complex subspace ker ∂s.
  - Old strata are exactly J_l-complex, and η is uniform. So every new stratum, and every intersection
    orientation, is within o(1) of complex. Hence the strata are ω_l-symplectic and positive.
  - Only ω_l is used as the symplectic form.
- **Steps 6–7: correct.** Each level is regularized afresh. Sub-configurations of SC divisors are SC, so D stays
  SC along the concatenated path. The relation PD[C_a] = PD[C_{a^+}] − PD[C_{a^-}] is topological, so it
  survives the TMZ paths.
- Minor point: components may be disconnected. Nothing in the chain uses connectedness, and TMZ allow it, to my
  knowledge.

## 3. Part 2, step by step

- **Bookkeeping: correct.** If I is needed, b ∈ B_I and c ∈ B_I with C_K ≠ ∅, where K = I∪{b,c}, then
  c ∈ B_{I∪b} and K is needed. Also I∪a^± is needed whenever it is nonempty and a ∈ I, since p(a^±) = a.
  - Level n−1: a needed I containing a level-(n−1) element contains its whole ancestor chain. So |I| = n and C_I
    is finite, and (C1)–(C3) are vacuous there.
  - Every structure used at stage I comes from stage I∪b (b ∈ B_I) or I∪{b,c}. Both are deeper and already built.
- **Lemma A: correct.** On the horizontal subspace, dz = −θz. So dz∘J_∇ = i dz holds iff θ∘J_B = iθ, that is,
  iff θ is (1,0).
- **Lemma Ch: correct.**
  - θ_α − θ_β = d log g + ∂ log ḡ, and ∂ log ḡ = conj((d log g)^{0,1}) = 0.
  - θ + θ̄ = d log h.
  - The pullback statement holds because a pseudo-holomorphic π preserves types.
  - No integrability of J_B is used.
- **Lemma D: correct.** I checked the horizontal lifts. The vertical vector u lifts to (u, 0).
- **Lemma B': correct.** Positivity of ω on N_a for the complex orientation means exactly ω(n, in) > 0. Combined
  with orthogonality this gives tameness along B, and tameness is open.
- **Lemma F: correct, with a thin-tube proviso.**
  - The inference u = 1 near deeper C_{K'} needs π_K(x) ∈ U_{K'} for x ∈ U_K ∩ U_{K'}. This follows from (R3)/(R4)
    for thin tubes.
  - log u exists on the disc fibres by path lifting from u = 1.
  - The modification is supported where f ≠ 0, which avoids all deeper tubes. It keeps Φ unchanged on C_K and
    on every C_{K'}.
  - The global Φ^0 exists because c_1 agree integrally.
- **Step (a): correct, with a fixable bookkeeping gap.**
  - Overlap agreement holds. On the tube of C_{I∪b} near C_K:
    - J_{I∪b} = J_∇ over (C_K, J_K) for N_c, by (C1) at I∪b;
    - ℋ_{I∪b;b} = π^*ℋ_{K;b}, by (C2) at I∪b;
    - the metrics are pulled back, by (R3);
    - Lemma Ch makes the Chern connection a pullback, and Lemma D gives J_∇ for N_b ⊕ N_c, which is symmetric
      in b and c.
  - The gap: the tubes must be chosen so that U_{I∪b} ∩ U_{I∪c} projects into the region of C_{I∪b} where
    J_{I∪b} already has its K-model form. The fix: shrink the radius functions of shallower tubes after the deeper
    J's are fixed.
    - As the radii go to 0, U_{I∪b} ∩ U_{I∪c} shrinks to C_K, by compactness.
    - TMZ regularizations restrict to smaller radii and stay compatible.
    - The J_∇ model is defined on the whole disc bundle, so shrinking never breaks (C1).
  - Extension: tame structures form a bundle with contractible fibres. Fine.
- **Step (b), O_I(c): correct.**
  - All transition functions are explicit: z^{(α)} and π^*g. Both are J_I-holomorphic by Lemmas A and Ch.
  - Products and inverses of J-holomorphic functions are J-holomorphic, so the tensor products O(a^+) ⊗ O(a^-)^*
    have holomorphic atlases.
  - Small omission: if C_{I∪a^s} = ∅, O_I(a^s) is trivialized by the single frame s_{a^s}. This is trivially
    holomorphic.
- **(C2), all cases: correct.**
  - Case c = b: the frames of the divisor bundle of the zero section are e_α = π^*σ_α, where τ = z^{(α)} π^*σ_α.
  - Case c ∉ I∪b: here c ∈ B_{I∪b} and b ∈ B_{I∪c}.
    - (C2) at stage I∪c gives ℋ_{I∪c;c} = π^*ℋ_{K;c}, so the frames can be taken pulled back.
    - z_c is preserved by π. So e_α = π^*e'_α, and s_c corresponds to π^*s_c under the "bundle with section"
      identification.
    - Both atlases generate the same maximal atlas.
  - Case c ∈ I: this is (C2) for a higher-level element of I, already established.
  - The identifications used are the restrictions of O_M(c)|U_{I∪b} ≅ π^*O_M(c)|C_{I∪b}. These are exactly the
    ones Lemma F uses, so Φ_a|C_I = π^*(Φ_a|C_{I∪b}) is the right compatibility, and (C2) follows for a.
- **Conclusion on M: correct.**
  - Induction along K ⊂ A_0, using (C1), (C2) and Lemma D, shows that J = J_∇ on N_K over D_K with the Chern
    connections of the ℋ_{K;k}.
  - By Lemma A, the z_k taken in local holomorphic frames are J-holomorphic, C-linear on the fibres, and
    D_k = {z_k = 0}.
  - The other components avoid a small neighbourhood of p.
  - (z_k, π_K^*(coordinates on D_K)) is a chart.
- **The relative-extension (Pic^0) worry: genuinely avoided.**
  - No holomorphic structure is ever produced by solving a ∂̄-equation or by extending one from near deeper strata.
  - Every ℋ_{I;a} is defined globally on C_I by an explicit formula, (C3): Φ_a^* applied to tensor products of
    divisor bundles, whose atlases consist of J_I-holomorphic functions built from deeper data.
  - Agreement near deeper strata, (C2), is *verified*, not *imposed*. The only freedom used is the choice of J_I
    away from the tubes, which carries no constraint.
  - The one global topological input is the integral identity c_1(O(a)) = c_1(O(a^+)) − c_1(O(a^-)), torsion
    included. It is paid for in Part 1 through the common P_k.

## 4. Verdict

**(V2).** The chain proves YES, modulo two cited results; the remaining gaps are fixable (listed below).
- The combined (AH) is standard but, to my knowledge, not published in exactly this form. I can sketch its proof
  (§1) but not fully write it.
- The precise TMZ statement is cited from memory, in two respects:
  - that the deformation path can be taken cohomologous: plausible, and I sketched the standard exact-deformation
    argument (§1), but I have not verified it as a published statement;
  - the domain conventions (R3)/(R4), which follow from TMZ's compatibility axioms after shrinking.

Fixable gaps found:
1. The tube-radius ordering in Step (a): shrink the shallower tubes after the deeper J's are fixed.
2. The empty-stratum case of O_I(c).

The answer YES depends on positivity being part of the definition. Without positivity the answer is NO, by the
example in §0.

Open:
- a full written proof of the combined (AH);
- confirming the cohomologous-path clause of TMZ.

=== END OF ANSWER round3_q1 ===
