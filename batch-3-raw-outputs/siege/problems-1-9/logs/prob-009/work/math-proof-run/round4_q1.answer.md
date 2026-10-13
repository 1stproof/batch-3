# Answer to round4_q1 (MS4: is t -> Y_t constant?)

## Plan (written first)
I could not find a full proof or an explicit counterexample. What this file proves:
- (A) Y_t is constant whenever closure(V_0) has no nontrivial deformation as a compact subspace. A sufficient condition is H^0(K, N_K) = 0 for K = closure(V_0).
- (B) A conditional converse: every suitable logarithmic holomorphic vector field near closure(V_0) produces a family that satisfies all of the problem's hypotheses but has Y_t non-constant.

Together, (A) and (B) show that the claim is a rigidity statement for totally geodesic surfaces. It is the 2-dimensional analogue of Möller's rigidity of Teichmüller curves. No argument that uses only (i), (ii) and the geometry near Δ_Γ can prove it.

## Verdict
**The statement is not proved and not refuted here.** It stays open in this run. Only special cases are proved: Theorem A, and Lemma 3 of P-a (all V_t totally geodesic). Theorem B shows exactly what a counterexample would need.

---

## 0. Re-check of Lemma 1 of P-a (holomorphy of Y_t)
The proof in P-a appeals to Remmert's proper mapping theorem. That step is not justified as written:
- the restriction of π_i × id to Z := closure(𝒱) ∩ (Δ_Γ × Δ) need not be proper;
- the reason is that points of closure(Z) \ Z in deeper strata, where only the *other* factors degenerate, are missing from Z.

Here is a corrected proof.

**Lemma 0.** Under (R1) and (R2), t ↦ Y_t is holomorphic.

*Proof.*
1. **Z is 2-dimensional at each of its points.** Z is a locally closed analytic subset of M̄_g × Δ, by (R1). By (R2), Z is locally homeomorphic to ∂V_0 × Δ, which has real dimension 4. So every point of Z has local complex dimension 2.
2. **Cut Z down to a curve.** Fix t_0 and a point p ∈ ∂V_{t_0}. Take local coordinates (y, z) on Δ_Γ near p, with y the coordinates on M_{g_i,n_i}. Then Z ⊂ {y = Y_t}, and the fibre Z_{t_0} = {Y_{t_0}} × C_{t_0} is a curve in z.
   - Choose a holomorphic function h(z) with h(p) = 0 such that (p, t_0) is an isolated point of Z_{t_0} ∩ {h = 0}.
   - Then Z'' := Z ∩ {h = 0} has dimension ≥ 1 at (p, t_0), by Krull.
   - Its fibre over t_0 is isolated at that point. Hence near (p, t_0), Z'' is a curve whose projection to Δ is finite and non-constant.
3. **Parametrize.** Take an irreducible branch of Z'' and a Puiseux parametrization τ ↦ (y(τ), z(τ), t = τ^m). Then y(τ) = Y_{τ^m}, so y(ζτ) = y(τ) for every m-th root of unity ζ. Therefore y(τ) = Ŷ(τ^m) with Ŷ holomorphic.
4. **Conclude.** The branch covers a neighbourhood of t_0, so Y_t = Ŷ(t) is holomorphic near t_0. ∎

**Consequence.** By the identity theorem, the claim holds as soon as Y_t is constant on some nonempty open set of t.

---

## 1. Theorem A (rigidity of K implies the claim) — proved, modulo standard deformation theory cited from memory

**Setting.** To avoid orbifold issues, pass to a finite Galois cover M̄^{(ℓ)} → M̄_g by a smooth projective variety (level structures; Looijenga, Boggi–Pikaart, cited from memory). Write:
- K for an irreducible component of the preimage of closure(V_0);
- N_K = Hom(I_K/I_K^2, O_K) for its normal sheaf.

The family closure(𝒱) lifts to a family K_t, for small t, after choosing the component that continues K. (Lifting a connected family of irreducible compact subspaces along a finite étale-in-orbifold-sense cover is routine; I have not written out the details.)

**Theorem A.** Suppose the germ at [K] of the Douady space 𝒟 of compact analytic subspaces of M̄^{(ℓ)} is a reduced point. This holds in particular if H^0(K, N_K) = 0. Then K_t = K for all small t, and so Y_t = Y_0 for all t.

*Proof.*
1. **The family is flat.** The total space closure(𝒱) is reduced and irreducible of dimension 3, and it dominates the smooth curve Δ. A reduced, irreducible space that dominates a smooth curve is flat over it, since there is no torsion.
2. **Constancy near 0.** So t ↦ [K_t] is a holomorphic map from a neighbourhood of 0 to 𝒟. The Zariski tangent space of 𝒟 at [K] is H^0(K, N_K) (Douady; Grothendieck for the Hilbert scheme; cited from memory). If this space is 0, the germ is a reduced point. In either case the map is constant near 0, so closure(V_t) = closure(V_0) for small t.
3. **Conclude.** For small t this gives ∂V_t = ∂V_0, hence Y_t = Y_0. By Lemma 0 and the identity theorem, Y_t = Y_0 for all t. ∎

**Contrapositive.** Suppose Y_t is not constant. Then t ↦ [K_t] is a non-constant germ of a curve in 𝒟 through [K]. Its leading term is a nonzero vector in the tangent cone, which lies inside H^0(K, N_K). It is in fact logarithmic: it is tangent to the strata, because of (i). So any counterexample needs a nonzero (logarithmic) normal vector field on closure(V_0).

**Limitation.** I do not know how to prove H^0(K, N_K^{log}) = 0, or the weaker statement that the germ of 𝒟 is a point, for a general totally geodesic surface. Three routes and why they stall:
- **Möller's route for Teichmüller curves.** That proof combines a maximal Higgs field, the topological invariance of the Arakelov/Toledo degree, and Möller's Hodge-theoretic characterization of Teichmüller curves. For surfaces I know no Hodge-theoretic characterization of total geodesicity that is topologically invariant. The defining condition "θ_v(ω) ∈ C·ω̄ for some v" involves complex conjugation pointwise, so it is not a holomorphic condition. **Open.**
- **Restricting to a dense family of Teichmüller curves C ⊂ V_0, where such a family exists.** Rigidity of each C only kills the part of ξ|_C that lifts to N_{C/M_g}. The obstruction to lifting lies in H^1(C, N_{C/K}), which need not vanish. **Dead end as it stands.**
- **Pinning through deeper incidences (P-d).** This needs an extra boundary branch E through a deeper point of closure(∂V_0). Such a branch need not exist, because the boundary of closure(V_0) near that point may be a single curve. Even when it exists, one needs rigidity of the relevant factor of E_t for t ≠ 0. That requires Möller's characterization theorem, whose hypothesis on the zeros of the generating differential is not known to be topologically invariant. **Not completed.**

---

## 2. Theorem B (a conditional counterexample) — proved, given its hypothesis

**Theorem B.** Let U be an open neighbourhood of K_0 := closure(V_0) in M̄_g, working in an orbifold chart or on a smooth level cover as in §1. Let ξ be a holomorphic vector field on U with two properties:
- (a) ξ is tangent to every boundary stratum Δ_G, that is, logarithmic;
- (b) near closure(∂V_0) ∩ U, ξ restricted to the product Δ_Γ ≅ ∏_j M_{g_j,n_j} has product form ξ = (v(y), w(y, z)). Here v is a holomorphic vector field on the i-th factor, with v(Y_0) ≠ 0.

Let Φ_s be the flow of ξ. Then for ε > 0 small, the sets V_t := Φ_{εt}(V_0), t ∈ Δ, satisfy all of the problem's hypotheses, together with (R1) and (R2). Moreover Y_t = φ_{εt}(Y_0), where φ is the flow of v. In particular Y_t is non-constant.

*Proof.*
1. **The flow exists on the whole disc.** K_0 is compact, so Φ_s is defined on a neighbourhood of K_0 for |s| < 2ε, by the ODE existence theorem. Each Φ_s is a biholomorphism onto its image. By (a), Φ_s maps each stratum into itself, because a logarithmic vector field is tangent to every stratum closure.
2. **Each V_t is an algebraic subvariety of M_g.**
   - Since Φ is a homeomorphism, closure(V_t) = Φ_{εt}(K_0). This is a compact set, locally analytic at each of its points, so it is a closed analytic subset of M̄_g.
   - By Chow's theorem (GAGA, cited from memory) it is algebraic.
   - Since Φ preserves M_g, V_t = closure(V_t) ∩ M_g. So V_t is a smooth closed subvariety of M_g, being biholomorphic to V_0.
3. **The family is a smooth trivial family of submanifolds.** The total space 𝒱 = {(Φ_{εt}(x), t) : x ∈ V_0, t ∈ Δ} is a complex submanifold of M_g × Δ. The map (x, t) ↦ (Φ_{εt}(x), t) trivializes it. This proves (R2) and the footnote condition.
4. **Hypothesis (i).** closure(V_t) ∩ Δ_G = Φ_{εt}(K_0 ∩ Δ_G), which is trivialized by the same map.
5. **Hypothesis (ii).** Φ_{εt} is a homeomorphism that preserves every stratum. Therefore it commutes with taking closures and intersections. Let U' be any open set for which the incidence in (ii) holds at t = 0. Then the same incidence holds at time t with U' replaced by Φ_{εt}(U').

   (ii) is stated for the *same* U at all times, so it needs one more remark. By (b), Φ preserves the product structure near Δ_Γ. Taking U' to be a small product-type neighbourhood, Φ moves it only slightly for small ε. Since (ii) is local, one can cover U by such sets.

   **Possible gap.** This last reduction is only sketched. If (ii) is read literally for an arbitrary fixed U, I have not checked that every U can be handled this way.
6. **The boundary and the constant factor.**
   - ∂V_t = Φ_{εt}({Y_0} × C_0) = {φ_{εt}(Y_0)} × (curve), by (b). So it is constant on the i-th factor with Y_t = φ_{εt}(Y_0).
   - Y_t is non-constant because v(Y_0) ≠ 0.
   - dim ∂V_t = 1.
   - V_0 is totally geodesic by assumption. Nothing is asserted about V_t for t ≠ 0, and the problem asks for nothing. ∎

**Consequence.**
- The problem's claim for a given V_0 fails if and only if V_0 can be moved in a way that moves Y_0 (Theorem A in the contrapositive, with Theorem B).
- Theorem B produces such motions from logarithmic vector fields near closure(V_0) of the stated product form.
- So the claim is equivalent to a *global rigidity* property of the compact surface closure(V_0) ⊂ M̄_g. Hypotheses (i) and (ii) are automatically satisfied by any stratum-preserving ambient flow. This confirms and sharpens Observation 4 of P-a and Lemma 1 of P-b: no argument based only on (i), (ii), the monodromy or the local geometry near Δ_Γ can work.

**Open question.** I do not know whether any totally geodesic surface V_0 admits a vector field as in Theorem B. More generally, I do not know whether any admits a nonzero log normal section with nonzero Y-component at ∂V_0. So Theorem B does not give an actual counterexample.

Constraints I found while looking for one:
- **Genus 2.** Every product stratum carrying a 1-dimensional ∂V that is constant on a positive-dimensional factor is a quotient stratum, which the problem excludes. So genus 2 gives nothing.
- **Covering constructions over M_{0,5} or M_{0,6}.** I tried the loci of 6 points with an involution, inside covering loci over M_{0,6}. In every case I checked, the constant factor Y_0 is a cover of a 3-pointed sphere, and it stays such in any family that remains inside the covering locus. A deformation that breaks the symmetry runs into the fact that the normal bundle of the symmetric locus has monodromy −1. Then a symmetric level-set deformation becomes a branched double cover, which is not smoothly trivial. **Not a counterexample.**

---

## 3. Other special cases that are proved
1. **All V_t totally geodesic (Lemma 3 of P-a).** Totally geodesic subvarieties form a countable set (Eskin–Mirzakhani–Mohammadi and Wright, cited from memory). By Lemma 0, t ↦ Y_t is continuous, and a continuous map from the connected disc into a countable set is constant.
2. **More generally: Y_t confined to a countable set.** If for every t, Y_t lies in a fixed countable set S ⊂ M_{g_i,n_i}, then Y_t is constant, by the same argument. An example of such S is the set of curves admitting a cover of P^1 branched over 3 points (Belyi-type). The hypotheses of the problem do not force Y_t into any such set.
3. **Rigid closure.** If closure(V_0) is rigid in the sense of Theorem A, the claim holds.

## 4. Summary
- **Proved:**
  - Lemma 0 (holomorphy, with a corrected proof);
  - Theorem A (rigidity of closure(V_0) implies the claim);
  - Theorem B (conditional counterexample from stratum-preserving flows; step 5 sketched as noted);
  - the countability special cases in §3.
- **Not proved (open):**
  - the claim for a general totally geodesic surface V_0;
  - equivalently, that no deformation of closure(V_0) moves the constant factor Y_0;
  - a sufficient condition would be H^0(closure V_0, N^{log}) = 0, or the vanishing of its Y-component on ∂V_0;
  - whether a vector field as in Theorem B exists for any totally geodesic V_0.
- **About the reduction itself:** the reduction of the problem to MS4 under (R1) and (R2) is legitimate. Theorem B shows that, under these readings, the problem is a genuine global rigidity question. It would be false for a non-rigid V_0 of the stated kind, if one exists.

=== END OF ANSWER round4_q1 ===
