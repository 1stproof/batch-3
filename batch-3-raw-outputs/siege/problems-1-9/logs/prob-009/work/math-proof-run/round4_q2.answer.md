# Answer to round4_q2 (MS4: is t -> Y_t constant?)

## Plan
I tried for a full proof of MS4, i.e. that t -> Y_t is constant. I did not find one, and I did not find a counterexample either. Below I record:
- re-checked reductions, including one new observation about hypothesis (ii);
- three conditional theorems with complete proofs, each under an explicit extra hypothesis;
- the precise remaining gap.

**Status: MS4 is NOT proved here. It remains open in this run.**

---

## 0. Reading and reduction (re-checked)

- P-a Lemma 1 (holomorphy of t -> Y_t) is correct under (R1), with the properness argument as given there. The problem's conclusion is literally "t -> Y_t is constant". By the identity theorem this is equivalent to local constancy near some t_0, and also to the set {Y_t} being countable, because a continuous map from a connected set with countable image into a Hausdorff manifold is constant.

- **New observation 0.1: (ii) is vacuous or tautological for every pair (Δ_G, Δ_Γ) with Δ_Γ ⊂ closure(Δ_G).**
  - Let G be a proper contraction of Γ that is not the trivial one-vertex graph. Then Δ_G ⊂ ∂M_g. Since closure(V_0) ∩ ∂M_g has dimension at most 1, closure(V_0) ∩ Δ_G has dimension at most 1.
  - The closure of a quasi-projective curve adds only finitely many points. So closure(closure(V_0) ∩ Δ_G) ∩ Δ_Γ is finite.
  - Every open U meeting ∂V_0 in a curve piece therefore violates the premise of (ii), so (ii) says nothing about such U.
  - For G the one-vertex graph (Δ_G = M_g), the conclusion of (ii) is the tautology closure(V_t) ∩ Δ_Γ = closure(V_t ∩ M_g) ∩ Δ_Γ.
  - Together with P-b, hypothesis (ii) carries information only at isolated points of deeper strata.

- **Observation 0.2: incidences are transported by (R2), even where (ii) is silent.**
  - Let E_0 be a component of closure(V_0) ∩ Δ_G and let Q_0 ∈ closure(E_0) ∩ closure(V_0) ∩ Δ_{G'}.
  - Let H : closure(V_0) × Δ -> closure(𝒱) be the homeomorphism of (R2). It maps strata to strata and, being a homeomorphism, commutes with taking closures.
  - Hence Q_t := H(Q_0, t) lies in closure(E_t) ∩ Δ_{G'}, where E_t := H(E_0 × {t}) is a union of components of closure(V_t) ∩ Δ_G.
  - Q_t depends continuously on t. Apply this with Q_0 ∈ ∂V_0 or Q_0 ∈ closure(∂V_0).
  - The Y-coordinate of H(Q_0, t) is Y_t whenever Q_0 ∈ closure(∂V_0) lies in a stratum where the Y-vertex is intact (P-b).

---

## 1. Conditional theorem A (pinning by a rigid incident boundary curve)

**Theorem A.** Assume (R1) and (R2). Suppose there are:
- a point Q_0 ∈ closure(∂V_0) lying in a stratum Δ_{G'} in which the vertex carrying Y_0 is intact;
- a 1-dimensional component E_0 of closure(V_0) ∩ Δ_G with Q_0 ∈ closure(E_0);
such that the transported curves E_t (Observation 0.2) satisfy closure(E_t) = closure(E_0) for all t. Then Y_t = Y_0 for all t.

*Proof.*
1. By Observation 0.2, Q_t ∈ closure(E_t) ∩ Δ_{G'} = closure(E_0) ∩ Δ_{G'}.
2. If Δ_{G'} = Δ_G, then Q_t ∈ E_0 ∩ closure(∂V_0) for all t; otherwise Q_t ∈ closure(E_0) \ E_0. In the second case the set is finite, because E_0 is a quasi-projective curve.
3. In the first case, E_0 ∩ closure(∂V_t) is a proper analytic subset of the irreducible curve E_0 (if E_0 ⊄ closure(∂V_t)), hence finite. If instead E_0 ⊂ closure(∂V_t), then E_0 ⊂ ∂V_t, since 1-dimensional pieces in distinct strata are disjoint and so G = Γ. Then E_0 carries the Y-coordinate Y_t for every t, and the hypothesis forces Y_t to be the Y-coordinate of E_0, which is fixed.
4. In the remaining cases t -> Q_t is a continuous map into a finite set, so Q_t = Q_0.
5. The Y-coordinate of Q_t is Y_t, so Y_t = Y_0. ∎

**Status.** Proved. It reduces MS4 to two things, neither of which I proved:
- (a) existence of such an incident boundary curve E_0;
- (b) rigidity of E_t, e.g. via maximal-Higgs or Milnor–Wood topological invariance plus Möller's characterization of Teichmüller curves plus countability.

The Y-vertex must also be "visible" in E_0, which is automatic by step 5 of the proof.

---

## 2. Conditional theorem B (all V_t totally geodesic)

**Theorem B.** If every V_t is totally geodesic, then Y_t is constant.

*Proof.*
- Cited from memory: there are only countably many totally geodesic subvarieties of M_g. This is due to Eskin–Mirzakhani–Mohammadi, who showed that GL(2,R)-orbit closures are affine invariant manifolds and that there are countably many of them. It is combined with the fact that a totally geodesic subvariety V is the projection of the GL(2,R)-invariant locus of quadratic differentials generating Teichmüller discs in V, which is a finite union of orbit closures.
- So t -> closure(V_t) takes countably many values, and so does t -> Y_t (each V_t determines ∂V_t and hence Y_t).
- A holomorphic map with countable image is constant (Section 0). ∎

**Status.** Proved, modulo the cited countability. It does not apply to the problem, which explicitly does not assume that V_t is totally geodesic.

---

## 3. Conditional theorem C (abstract triviality implies rigidity, via Imayoshi–Shiga)

**Theorem C.** Assume:
- there are biholomorphisms φ_t : V_0 -> V_t, continuous in t, with φ_0 = id;
- the maps f_t := ψ ∘ φ_t : V_0 -> M_g are homotopic to the inclusion f_0, after passing to a finite-index torsion-free level cover so that M_g^{(m)} is a manifold and the maps lift. This holds automatically for a continuous family.

Then V_t = V_0 for all t, and in particular Y_t = Y_0.

*Proof.*
1. Cited from memory, Imayoshi–Shiga (1988), following Arakelov–Parshin: let R be a Riemann surface of finite type. A non-isotrivial holomorphic family of compact genus-g curves over R is determined up to isomorphism by its monodromy. Equivalently, two homotopic non-constant holomorphic maps R -> M_g^{(m)} coincide.
2. Let R ⊂ V_0 be any irreducible algebraic curve, normalized. Then f_0|_R is non-constant, since f_0 is an embedding.
3. f_t|_R is homotopic to f_0|_R and is non-constant, since φ_t is biholomorphic onto V_t ⊂ M_g. Hence f_t|_R = f_0|_R.
4. Algebraic curves cover V_0, so f_t = f_0 and V_t = V_0. ∎

**Status.** Proved, modulo the cited theorem and the extra hypothesis that the V_t are abstractly biholomorphic to V_0. That hypothesis is not given by the problem: a smoothly trivial family of complex surfaces can vary its complex structure. So MS4 reduces to the following (open) statement.

**(Rigidity of the log pair).** A deformation of V_0 inside M_g as in the problem is abstractly isotrivial. For example, H^1(closure(V_0)^~, T(-log D)) = 0 on a log resolution, or every such deformation of the log pair is trivial.

I did not prove this. It is plausible for covering constructions, which are finite covers of M_{0,5} or of the flex-locus type, but unproved even there.

---

## 4. Why I could not close the gap

- **Local data cannot see Y_t.**
  - Observation 0.1 and P-a/P-b/P-c show that (i), (ii), the monodromy, the local monodromy, the weight filtrations and the self-intersections are all blind to Y_t.
  - The only data coupling Y_t to anything else are incidences at isolated points of deeper strata (Observation 0.2).
  - Pinning through those incidences needs another boundary curve whose closure is rigid (Theorem A).
  - The natural rigidity mechanism for that curve is the following chain: its non-constant factor carries a rank-2 sub-local system whose Milnor–Wood (Toledo) invariant is topological; the invariant is maximal at t=0; by Möller's characterization (cited from memory), a curve in M_{g',n'} carrying a maximal-Higgs rank-2 sub-VHS is a Teichmüller curve; Teichmüller curves are countable.
  - That chain requires showing, for t ≠ 0, that the rank-2 sub-local system still underlies a sub-VHS of the transported family. Deligne's semisimplicity and rigidity of the VHS on irreducible summands make this plausible, but I have not verified it.
  - I also could not show that a suitable incident curve exists. If closure(∂V_0) = ∂V_0 is compact (no cusps on C_0), there are no deeper incidence points at all. The extra input then needed is the fact (expected, not proved here) that the non-constant factors of boundary curves of totally geodesic surfaces are Teichmüller curves, which are never compact.
- **Hodge-theoretic route.**
  - H^1(Y_t) appears as a constant Hodge-structure summand of Gr^W_1 of the limiting mixed Hodge structure along ∂V_t.
  - For V_0, a limiting argument with Teichmüller discs shows that every limit of the generating quadratic differentials vanishes identically on the Y-component (the Y-coordinate is constant on ∂V_0, so limiting discs act trivially there).
  - This is a property of V_0 only. I found no deformation-invariant (topological) consequence of it that pins Y_t.

## 5. Summary

- **Proved:**
  - holomorphy and the reduction (re-checked);
  - Observation 0.1: (ii) is vacuous or tautological along Δ_Γ for all coarser strata;
  - Observation 0.2: (R2) transports incidences;
  - Theorem A (pinning via a rigid incident curve);
  - Theorem B (all V_t totally geodesic);
  - Theorem C (abstractly trivial deformations are trivial, via Imayoshi–Shiga).
- **Open:**
  - MS4 itself;
  - specifically, either (1) rigidity of the log pair (closure(V_0), boundary) under the problem's deformations, or (2) for every such V_0 and Γ, the existence of an incident boundary curve whose non-constant factor is rigid (persistence of a maximal-Higgs rank-2 sub-VHS under the deformation), plus non-compactness of C_0.
- **No counterexample found.** Any counterexample would require a non-trivial deformation of a totally geodesic surface inside M_g. None is known to me, and one is expected not to exist.

=== END OF ANSWER round4_q2 ===
