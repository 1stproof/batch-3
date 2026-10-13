# extra_q6 — isotropy change under admissible deformations

Plan: (1) a local criterion (K) at points of B_0 that gives (AP) on a small disc (this generalises Cor. C.5); (2) structure results for pieces and for isolated points: no curve rise, curve drop is all-or-nothing, point drop at isolated points is all-or-nothing; (3) local models showing curve drop is compatible with the plumbing structure, so (AP) cannot be proved locally; (4) open questions.

## Summary

**Proved, using only (R1), (R2), the classical chart facts (Kur) and Theorem A′ / Remark 7.6 as black boxes:**

- **Theorem 1 (local criterion ⇒ (AP) ⇒ claim).** Suppose every z ∈ B_0 satisfies condition (K_z) below: near z, |Aut| is constant on every local stratum branch through z that carries points of B_0. Then (AP) holds on a disc |t| < r, and so Y_t = Y_0 for all t. This contains Cor. C.5. It also covers boundary points whose only automorphisms are "inert" on the relevant strata, for example generic elliptic tails, which is the case Remark C.6 says C.5 misses (see Example 1.4; this example is checked in charts only modulo a standard equivariance fact).
- **Theorem 1′ (localisation).** Let F ⊂ B_0 be the set of points where (K_z) fails. For every open N ⊃ F there is r > 0 such that (AP) holds on (B_0 ∖ N) × Δ_r. So every failure of (AP) close to t = 0 happens next to F.
- **Proposition 2 (pieces).** Let E be a piece of B_0 in a stratum Δ_G, with generic automorphism order k_E. Then for some r > 0:
  - (a) no curve rise: H_t(E°) ⊄ Z_{k_E+1} for 0 < |t| < r;
  - (b) the generic automorphism order of H_t(E°) is a constant k′_E ≤ k_E for 0 < |t| < r;
  - (c) curve drop along E (k′_E < k_E) happens iff the lifted transported surface in a chart at a generic point of E is non-reduced over Δ (it has degree ≥ 2 over c̃ × Δ). It never happens for automorphisms that act trivially on the stratum germ (the K_G-type ones).
- **Proposition 3 (isolated points).** If z is isolated in B_0 ∩ Δ_{G_z}, then t ↦ H_t(z) is holomorphic near 0, and |Aut H_t(z)| is constant for 0 < |t| < r. So a point drop at such a z happens either for all small t ≠ 0 or for none. Also, if Aut(z) acts trivially on the germ of Δ_{G_z} at z, then |Aut H_t z| = |Aut z| for small t, so there is no drop at z.

**Sketched (evidence, not proofs):** local chart models, compatible with the plumbing description of a totally geodesic surface near a boundary piece, in which a whole boundary piece leaves the isotropy locus (curve drop). One model has a genus-2 component attached at a Weierstrass point; another has a constant elliptic tail with j = 1728. So (AP) cannot be proved by local arguments, which confirms Excerpt 3. The second model shows that (AP) failure is closely tied to the problem itself: if the constant factor Y_0 has non-generic automorphisms, then "Y_t ≠ Y_0" is itself a curve drop along ∂V_0.

**Not settled:** (AP) in general; whether a *global* admissible family with curve drop or point drop exists; whether H can be re-chosen to satisfy (AP) when no genuine drop occurs. Section 5 lists these.

---

## 0. Standard facts used

Notation is as in the task file. For J ∈ M̄_g let A = Aut(J), and let q : B → q(B) ≅ B/A be the Kuranishi chart, with plumbing coordinates s_e (e ∈ E(G_J)). For S ⊆ E(G_J) put
- L_S := {s_e = 0 for e ∈ S};
- L_S^∘ := {p : S(p) = S} = L_S ∩ {s_e ≠ 0 for e ∉ S}.

From (Kur):
- X_p has exactly |S(p)| nodes, and its dual graph is G_J/(E ∖ S(p)).
- Aut(X_p) ≅ Stab_A(p).
- q^{-1}(q(p)) = A·p, and q^{-1}(J) = {0}.
- q is a finite-group quotient map, so it is open, closed and proper.

**0.1 Lemma (isotropy loci).** For k ≥ 1, the set Z_k := {w ∈ M̄_g : |Aut w| ≥ k} is a closed analytic subset of M̄_g. Hence |Aut| is upper semicontinuous.

*Proof.* In a chart, Z_k ∩ q(B) = q(⋃_{C ≤ A, |C| ≥ k} Fix(C)). Each Fix(C) is a closed analytic subset of B, and q is finite, so the image is closed analytic (Remmert). ∎

**0.2 Lemma (local stratum decomposition).** Let B″ ⊂ B be an A-invariant ball and G′ a stratum. Then P_{G′} := q^{-1}(Δ_{G′}) ∩ B″ is the disjoint union of the sets L_S^∘ ∩ B″ over the S with G_J/(E ∖ S) ≅ G′, and each of these is relatively closed in P_{G′}. For an A-orbit O of such patterns put M_O := ⋃_{S∈O} L_S^∘ ∩ B″. Then the sets q(M_O) partition Δ_{G′} ∩ q(B″) into finitely many relatively open-and-closed subsets.

*Proof.*
- The decomposition is (Kur).
- Relative closedness: let p_k ∈ L_S^∘ with p_k → p ∈ P_{G′}. Then S(p) ⊇ S, and |S(p)| = |E(G′)| = |S|, so S(p) = S.
- Since aL_S^∘ = L_{aS}^∘, each M_O is A-saturated and relatively closed in P_{G′}.
- P_{G′} is q-saturated and q is closed, so q|_{P_{G′}} : P_{G′} → Δ_{G′} ∩ q(B″) is closed.
- So the q(M_O) are relatively closed. They are pairwise disjoint, because the M_O are saturated and disjoint. There are finitely many of them and they cover. Hence each is also relatively open. ∎

**0.3 Uniform continuity.** H is continuous on the compact set closure(V_0) × {|t| ≤ 1/2}, and H_0 = id. Fix a metric d on M̄_g. Then

  ε(τ) := sup{ d(H_s(z), z) : z ∈ closure V_0, |s| ≤ τ } → 0 as τ → 0.

---

## 1. Theorem 1: a local criterion that gives (AP)

**Definition (K_z).** Let z ∈ B_0, with chart q : B → q(B) at z and A = Aut(z). Say **(K_z)** holds if there is an A-invariant ball B′ ⊂ B centred at 0 such that, for every pattern S ⊆ E(G_z) with q(L_S^∘ ∩ B′) ∩ B_0 ≠ ∅, the function w ↦ |Aut w| is constant on q(L_S^∘ ∩ B′).

*Equivalent form (used to check examples).* L_S^∘ ∩ B′ is connected, being the complement of hypersurfaces in a ball inside a linear subspace. By upper semicontinuity together with (P2)(ii),(iv) of Thm 7.5 (Stab(p′) ⊆ Stab(p) for p′ near p, with equality when the orders agree), constancy of |Stab| on L_S^∘ ∩ B′ is the same as constancy of Stab_A on it. That in turn is the same as: **for every g ∈ A, either g fixes L_S ∩ B′ pointwise or g has no fixed point in L_S^∘ ∩ B′.**

For S = E(G_z) (always relevant, because q(0) = z ∈ B_0), this says that **A acts trivially on the stratum germ D = L_{E(G_z)} at 0**.

**Theorem 1.** Assume (R1), (R2), and that (K_z) holds for every z ∈ B_0. Then there is r > 0 with |Aut H_t(z)| = |Aut z| for all z ∈ B_0 and |t| < r. Consequently (Theorem A′ with Remark 7.6), Y_t = Y_0 for all t ∈ Δ.

**Theorem 1′.** Assume (R1), (R2). Let F := {z ∈ B_0 : (K_z) fails}. For every open N ⊇ F there is r > 0 with |Aut H_t z| = |Aut z| for z ∈ B_0 ∖ N and |t| < r.

*Proof (of both; Theorem 1 is the case F = ∅, N = ∅).*
1. **Setup.** Suppose the conclusion fails. Then there are t_n → 0 and z_n ∈ B_0 ∖ N with |Aut H_{t_n} z_n| ≠ |Aut z_n|. B_0 ∖ N is compact, so after passing to a subsequence z_n → z_* ∈ B_0 ∖ N. In particular (K_{z_*}) holds; take B, B′, A for z_* as in the definition. There are finitely many strata, so after passing to a subsequence every z_n lies in a single stratum Δ_{G′}.
2. **The path stays in one chart.** Choose an A-invariant ball B″ ⊂ B′ centred at 0. q(B″) is an open neighbourhood of z_*. Consider the path c_n(ρ) := H_{ρ t_n}(z_n), ρ ∈ [0,1]. By 0.3, d(c_n(ρ), z_n) ≤ ε(|t_n|) → 0, and z_n → z_*. So for large n the whole of c_n lies in q(B″). By (R2), c_n also lies in Δ_{G′}.
3. **The path stays in one branch.** c_n is connected, so by Lemma 0.2 it lies in a single q(M_O), namely the one containing z_n = c_n(0). Write z_n = q(p_n) with p_n ∈ L_{S_n}^∘ ∩ B″. Then H_{t_n} z_n = q(p′_n) for some p′_n ∈ M_O; after replacing p′_n by an A-translate, p′_n ∈ L_{S_n}^∘ ∩ B″ as well. Pass to a subsequence with S_n = S constant.
4. **Contradiction.** q(L_S^∘ ∩ B′) contains z_n ∈ B_0, so (K_{z_*}) applies to S. Therefore |Aut z_n| = |Stab_A p_n| = |Stab_A p′_n| = |Aut H_{t_n} z_n|, which contradicts the choice of (z_n, t_n). ∎

**Remarks 1.1.**
- (a) Cor. C.5 is the special case where every Aut(z) is trivial.
- (b) Theorem 1′ shows that the only obstruction to (AP) near t = 0 is located at the closed-up set F. F consists of the points z ∈ B_0 at which some automorphism g ∈ Aut(z) fixes a point of a relevant open pattern locus L_S^∘ but not all of L_S. In particular, F contains every z at which Aut(z) acts non-trivially on the germ of its own stratum.
- (c) In the configuration of Cor. C.3(d), where Q has two components of class [Y_0] exchanged by a, the automorphism a swaps the moduli coordinates of these two components in D. Since dim M_{g_i,n_i} ≥ 1, a acts non-trivially on D, so Q ∈ F. This is consistent with Theorem 1′.

**Corollary 1.2 (pointwise version, for Cor. C.2).** Let z ∈ B_0, and suppose Aut(z) acts trivially on the stratum germ D at z (the S = E(G_z) part of (K_z)). Then |Aut H_t z| = |Aut z| for all small |t|.

*Proof.* H_t z ∈ Δ_{G_z} and H_t z → z. Near z, Δ_{G_z} ∩ q(B) = q(D ∩ B), where every point has stabiliser ⊇ A, hence equal to A. ∎

Hence, under (Rig): **if every puncture point Q of B_0 has Aut(Q) acting trivially on the germ of Δ_{G_Q} at Q, then Y_t ≡ Y_0** (Cor. 1.2 together with Cor. C.2). By Remark 1.1(c), this is equivalent to what C.1/C.3(d) already give, so it is a reformulation rather than a new case.

**Example 1.4 (elliptic tails; relies on a standard fact, stated here).** *Standard fact used:* the Kuranishi family of J can be chosen Aut(J)-equivariantly, with plumbing coordinates built from Aut(J)-equivariant local coordinates at the nodes.

Let z ∈ B_0 be such that Aut(z) is generated by elliptic involutions ι_T of elliptic tails T with j(T) ∉ {0, 1728}, and contains nothing else. Then:
- ι_T acts trivially on D and on every s_e with e ≠ e_T;
- ι_T acts on s_{e_T} by −1, because it acts by −1 on the tangent line of T at the node and trivially on the other branch.

For a product g = ∏_{T∈𝒯} ι_T:
- if S ⊇ {e_T : T ∈ 𝒯}, then g fixes L_S pointwise;
- otherwise g has no fixed point in L_S^∘, since there some s_{e_T} ≠ 0 is sent to −s_{e_T}.

So (K_z) holds. Hence, by Theorem 1: **if every z ∈ B_0 has only such elliptic-tail involutions as automorphisms, then the claim holds.** This is exactly the case singled out as missed by C.5 in Remark C.6.

---

## 2. Proposition 2: pieces (no curve rise; drop is all-or-nothing)

**Setting.** Let E be a piece: a 1-dimensional irreducible component of the closure of B_0 ∩ Δ_G. Let E° be E ∩ Δ_G with the following finitely many points removed: points lying on other components of B_0 ∩ Δ_G, singular points of B_0 ∩ Δ_G, and points not in Δ_G.
- E° is connected: it is an irreducible compact curve minus finitely many points.
- E° is open in B_0 ∩ Δ_G.
- Put 𝒟_G := closure(𝒱) ∩ (Δ_G × Δ), a locally closed analytic set, and X_E := H(E° × Δ).
- By (R2), X_E is open in 𝒟_G. So X_E is an analytic set, locally closed in Δ_G × Δ, and homeomorphic to E° × Δ, a connected topological 4-manifold.
- Hence X_E is pure 2-dimensional and locally irreducible. This is the standard fact that an analytic set which is a topological manifold at a point is locally irreducible there: two distinct top-dimensional local components would disconnect the complement of a real-codimension-≥2 subset. Being connected and locally irreducible, X_E is irreducible.
- Put k_E := min_{E°} |Aut|. By 0.1, every point of E° has |Aut| ≥ k_E, and |Aut| = k_E off a discrete subset of E°.

**Proposition 2.** There is r > 0 such that:
- (a) **No curve rise:** for 0 < |t| < r, H_t(E°) ⊄ Z_{k_E+1}.
- (b) **All-or-nothing:** for each k ≤ k_E, either H_t(E°) ⊂ Z_k for all |t| < r, or H_t(E°) ⊄ Z_k for all 0 < |t| < r. Consequently the generic order k′_E of H_t(E°) is independent of t for 0 < |t| < r, and k′_E ≤ k_E.
- (c) **No drop:** k′_E = k_E iff X_E ∩ {|t| < r} ⊂ Z_{k_E} × Δ.

*Proof.*
- **(a)** Suppose t_m → 0, t_m ≠ 0, with H_{t_m}(E°) ⊂ Z_{k_E+1}. For z ∈ E°, H_{t_m}(z) → z and Z_{k_E+1} is closed, so z ∈ Z_{k_E+1}. That makes E° ⊂ Z_{k_E+1}, contradicting the definition of k_E.
- **(b)** 𝒜_k := X_E ∩ (Z_k × Δ) is an analytic subset of X_E.
  - If 𝒜_k = X_E, the first alternative holds.
  - Otherwise dim 𝒜_k ≤ 1. Then for t ≠ 0 with H_t(E°) ⊂ Z_k, the curve H_t(E°) × {t} is a 1-dimensional irreducible component of 𝒜_k. (It is irreducible because it is homeomorphic to E°, hence locally irreducible and connected.)
  - If this happened for t_m → 0, t_m ≠ 0, then for any z ∈ E° every neighbourhood of (z, 0) would meet the infinitely many distinct components H_{t_m}(E°) × {t_m}, since H_{t_m}(z) → z. This contradicts local finiteness of the components of 𝒜_k. So for small r the second alternative holds.
  - Finitely many k, together with (a), give the rest of (b).
- **(c)** is (b) with k = k_E. ∎

**2.1 Multiplicity criterion for a drop.** Take a generic J ∈ E°. Then A := Aut(J) has |A| = k_E and fixes the lift c̃ := q^{-1}(E° ∩ q(B)) pointwise (by (P2)(iv), as the stabiliser order is constant on c̃). Let 𝒮 := (q × id)^{-1}(X_E) near (0,0), an A-invariant 2-dimensional analytic set in D × Δ whose fibre over t = 0 is c̃ (as a set).

Choose an A-invariant holomorphic retraction P : D → c̃ near 0. For example, factor through the projection onto Fix(A) in coordinates in which A acts linearly (Cartan), then retract Fix(A) → c̃.

*Claim.* (P, t) : 𝒮 → c̃ × Δ is finite. Its degree m is a multiple of the generic A-orbit size d = |A|/|generic Stab on 𝒮|. There is no drop along E iff d = 1. In particular, **a drop forces m ≥ 2**: the lifted transported boundary family is non-reduced (multiply covers c̃) at t = 0, even though its coarse image X_E is a topological product.

*Proof.*
- The fibre of (P, t) over (v, 0) is {v}, so the map is finite near (0,0) (isolated fibre).
- The map is A-invariant, so generic fibres are unions of free-ish A-orbits of size d. Hence d divides m.
- No drop iff the generic stabiliser on 𝒮 is all of A, i.e. d = 1 (P2(iv)). ∎

**2.2 Graph lemma (when the lifted transport is a C¹-small deformation).** Let A act linearly on D = Fix(A) ⊕ N with N^A = 0, and let c̃ ⊂ Fix(A) be a smooth curve through 0. Suppose c̃_t is an A-invariant curve that, near 0, is the graph over the tangent line of c̃ of a map that is C⁰-close to that of c̃. Then c̃_t ⊂ Fix(A).

*Proof.*
- Write the points of c̃_t as (x(v), n(v)), one for each v. Here v is a coordinate on the tangent line T_0c̃ ⊂ Fix(A), so a ∈ A fixes v.
- a·(x(v), n(v)) = (x(v), a n(v)) lies on c̃_t and has the same v-coordinate. Since there is one point per v, a n(v) = n(v) for every a ∈ A.
- So n(v) ∈ N^A = 0. ∎

Hence a drop requires that the transported boundary curve, lifted to the chart, is *not* a single graph-like sheet near c̃. Its lift must split into ≥ 2 sheets that are permuted by A and coalesce on c̃ at t = 0.

**2.3 Automorphisms acting trivially on the stratum never drop.** If g ∈ A acts trivially on D (for example K_G-elements such as elliptic involutions, or hyperelliptic involutions of (1,2)-self-loop vertices), then g fixes 𝒮 ⊂ D × Δ pointwise. So only automorphisms acting non-trivially on the stratum germ can drop. (Immediate.)

---

## 3. Proposition 3: isolated points

**Proposition 3.** Let z ∈ B_0 be isolated in B_0 ∩ Δ_{G_z}. Then:
- there is r > 0 such that t ↦ H_t(z) is a holomorphic map Δ_r → Δ_{G_z};
- |Aut H_t(z)| is constant on 0 < |t| < r, and is ≤ |Aut z|.

*Proof.*
1. {z} is open in B_0 ∩ Δ_{G_z}. So Γ_z := H({z} × Δ) is open in 𝒟_{G_z}, hence a 1-dimensional analytic set (locally closed). The projection t : Γ_z → Δ is a homeomorphism.
2. Γ_z is a topological disc, hence locally irreducible. So its normalisation ν : Γ̃ → Γ_z is a homeomorphism, and t∘ν : Γ̃ → Δ is a bijective holomorphic map of Riemann surfaces, hence biholomorphic. Then t ↦ H_t(z) = pr∘ν∘(t∘ν)^{-1}(t) is holomorphic.
3. For each k, {t : H_t(z) ∈ Z_k} is an analytic subset of Δ (Lemma 0.1). So it is either all of Δ or discrete. Shrinking r, the values of |Aut H_t z| are constant on the punctured disc.
4. Upper semicontinuity at t = 0 gives ≤ |Aut z|. ∎

So, at isolated points, (AP) failure is either a genuine drop for all small t ≠ 0, or absent near 0. In Cor. C.2, "there are t_n → 0 without a drop" is then equivalent to "no drop on a punctured disc".

---

## 4. Sketches and evidence (NOT proofs)

**4.1 A curve-drop model compatible with plumbing (sketch).**
- *The boundary piece.* Let a piece E of B_0 consist of curves J_v = X_v ∪_P R, where:
  - X_v (genus 2) runs over a Teichmüller curve in M_{2,1}, the marked point being a Weierstrass point;
  - R is constant.
  Weierstrass points are periodic points, so this is consistent with Part I's description of pieces. The hyperelliptic involution σ of X_v, extended by the identity on R, lies in Aut(J_v) for every v. It acts on Def(J) by u ↦ −u (u being the displacement of the attaching point from the Weierstrass point, a stratum coordinate) and s ↦ −s on the plumbing coordinate. So σ is *not* of K_G type, and E ⊂ F.
- *The lift of V_0.* The plumbing description of a totally geodesic surface near a boundary piece gives u = u_0(v) + h(v, s) along V_0, with h holomorphic in the plumbing parameters and u_0 ≡ 0. So the lift is Σ = {u = h(v,s)}, a graph over (v, s), with σΣ = {u = −h(v,−s)}.
- *A local deformation.* Deform h to h_t with h_t(v, 0) ≢ 0. The coarse surface V_t is locally the image of Σ_t ∪ σΣ_t. Its boundary lifts to the two sheets u = ±h_t(v,0) (when h is odd in s, Σ is σ-invariant and the sheets are the two halves of {u² = h_t(v,0)²}), and these leave Fix(σ). This is precisely the non-reduced situation of 2.1. Locally all of (i), (ii), smoothness and stratum-preservation hold.
- *Conclusion of the sketch.* Neither total geodesy at t = 0 nor the hypotheses on the family exclude curve drop **locally**. Whether such a local deformation extends to a global admissible family V_t is exactly the open global question.

**4.2 Link with the problem (sketch, but elementary).**
- Let α be an automorphism of the pointed curve Y_0 (fixing each marked point) that acts non-trivially on T_{Y_0} M_{g_i,n_i}, i.e. Y_0 lies in the orbifold locus of the factor.
- Extending α by the identity gives an automorphism of every point of ∂V_0, and it acts non-trivially on the stratum germ. So ∂V_0 ⊂ F.
- If Y_t ≠ Y_0 for small t ≠ 0 (and, generically, Y_t ∉ Z_{|Aut Y_0|}), then ∂V_t loses α. That is a curve drop along the pieces of ∂V_0.
- Conversely, if Y_0 has generic isotropy in M_{g_i,n_i}, no drop along ∂V_0 can come from the i-th factor.
- So the problem itself is one source of isotropy change. Proving (AP) in general would in effect include the conclusion of the problem in the orbifold-special case. This suggests (AP) is *not* a strictly easier intermediate statement, and that a direct proof (part 2 of the task) has to handle drop configurations head-on.

**4.3 Re-choosing H (sketch, no proof).** Suppose that for every piece E the alternative "no drop" of Prop. 2(b) holds, and that every isolated point of excess isotropy is a limit of exactly one holomorphic excess-isotropy multisection of the same order. Then the isotropy stratification {Z_k ∩ B_t ∩ Δ_G} is topologically equisingular in t, and one expects a stratum- and isotropy-preserving trivialisation of B_t. What I have *not* done is extend such a trivialisation to closure(V_t) while keeping smoothness on V_0 × Δ, which (R2) requires. So the "rise" artefacts (z ≠ excess point mapped onto an excess point) are presumably removable, but this is unproved.

---

## 5. Open questions (explicit)

1. **(Global curve drop.)** Does there exist an admissible family (R1), (R2) with V_0 totally geodesic and a piece E of B_0 with k′_E < k_E? By 2.1–2.3, such a drop requires a non-K_G automorphism generic on E and a non-reduced lifted transport.
2. **(Global point drop.)** The same question for a puncture point Q ∈ F, in particular the configuration of Cor. C.3(d).
3. **(Re-choice.)** If neither 1 nor 2 occurs, can H be replaced by H′ satisfying (R2) and (AP)? (Sketch 4.3.)
4. **(Direct route.)** Prove Y_t ≡ Y_0 in the presence of drop. By Theorem 1′, it suffices to control the finitely many pieces and points of F. By 4.2, these include ∂V_0 itself whenever Y_0 is an orbifold point of M_{g_i,n_i}.

What is proved here: Lemmas 0.1, 0.2; Theorems 1 and 1′; Corollary 1.2; Proposition 2 with 2.1–2.3; Proposition 3. Example 1.4 is proved modulo the stated standard equivariance fact. Section 4 consists of sketches and heuristics only.

=== END OF ANSWER extra_q6 ===
