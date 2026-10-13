# round5_q3 answer: attempt on MS4 (constancy of t -> Y_t)

## 0. Plan and status (written first)
Plan:
1. Prove the planner's Lemma R carefully: a transported boundary piece whose vertex-v projection is a Teichmuller curve keeps the same projection for all t. Proof via Royden, Bers' axis of pseudo-Anosovs, Thurston's stretch theorem, and finiteness (Imayoshi-Shiga / McMullen).
2. Deduce a conditional theorem: (T0) at t = 0 implies MS4.
3. Check (T0) for one class of V_0, covering constructions over M_{0,5}. This is partial.
4. State precisely what remains open.

Status: **MS4 is NOT settled in general.** I give no counterexample and no full proof. What follows is a conditional theorem with a complete proof given its stated hypotheses, plus a sketch that the main hypothesis (T0) holds in one class of examples.

I use readings (R1) and (R2) as in the task, and PR-1 (Y is holomorphic, so local constancy near 0 suffices). H denotes the stratified homeomorphism of (R2), and H_t := H(·, t).

## 1. Topological preliminaries (proved)

**Lemma 1.1 (transport of irreducible components and normalizations).** Let E_0 be an irreducible component of the pure 1-dimensional analytic set closure(V_0) ∩ Δ_G, and put E_t := H_t(E_0). Then:
- E_t is an irreducible component of closure(V_t) ∩ Δ_G;
- H_t lifts to a homeomorphism Ĥ_t : Ê_0 → Ê_t of the normalizations;
- ν_t ∘ Ĥ_t = H_t ∘ ν_0, where ν_t : Ê_t → E_t is the normalization map;
- Ê_t is a compact Riemann surface minus finitely many points, of the same topological type as Ê_0.

*Proof.*
1. By (R2), H_t maps closure(V_0) ∩ Δ_G homeomorphically onto A_t := closure(V_t) ∩ Δ_G. By (R1), A_t is an analytic subset of Δ_G. It has pure dimension 1, since topological dimension is a homeomorphism invariant.
2. For a pure 1-dimensional analytic set A, let N(A) be the discrete set of points with at least two local branches. A point has ≥ 2 branches iff it is not a topological-manifold point. Indeed, at a unibranch point A is locally homeomorphic to a disc (Puiseux). At a point with k ≥ 2 branches, A is locally a wedge of k discs, which is not a manifold. So N(A) is topologically defined.
3. The irreducible components of A are the closures of the connected components of A \ N(A). Two different components meet only in points with ≥ 2 branches, so they are separated in A \ N(A), and each A_j \ N(A) is connected. Hence H_t maps irreducible components to irreducible components.
4. The local branches of A at p correspond to the connected components of U \ {p} for a small conic neighbourhood U of p. This is topological. The normalization is obtained by separating branches: as a set it is ⊔_p {branches at p}, with the evident topology. So H_t induces a homeomorphism Ĥ_t with ν_t ∘ Ĥ_t = H_t ∘ ν_0.
5. Ê_t is the normalization of the compact curve closure(E_t) (compact by (R1)), minus the finite preimage of closure(E_t) \ E_t. This is a finite set, being a proper analytic subset of a compact curve. ∎

**Lemma 1.2 (Ĥ_t preserves orientation).** With the complex orientations, Ĥ_t is orientation-preserving.

*Proof.*
1. Let 𝓐 = closure(𝒱) ∩ (Δ_G × Δ). As in PR-1, outside a discrete set D of values of t, every fibre contains a point a at which 𝓐 is smooth and φ is a submersion.
2. Near such a point a = (p, t_1) choose holomorphic coordinates (z, t). The local degree of the continuous map z ∘ Ĥ_t on a small disc around Ĥ_{t_1}^{-1}(p) is ±1. It is locally constant in t, by homotopy invariance of degree for maps of a disc whose boundary circle avoids a point.
3. So the orientation character of Ĥ_t is locally constant on the connected set Δ \ D. It is +1 at t = 0, where Ĥ_0 = id. For t ∈ D, use a nearby t′ ∉ D and the same argument at a regular point of the fibre over t′, comparing with Ĥ_{t′}. ∎

(Lemma 1.2 is only needed to make the isometry of Step 4 of Lemma R holomorphic rather than antiholomorphic.)

**Lemma 1.3 (homotopy).** Let Δ_G be a product stratum and v a vertex of G with factor M_{h,m}. Put f_t := π_v ∘ ν_t : Ê_t → M_{h,m}. Then f_t ∘ Ĥ_t = π_v ∘ H_t ∘ ν_0, which is jointly continuous in (x̂, t). So f_t ∘ Ĥ_t is homotopic to f_0 through the maps s ↦ π_v ∘ H_{st} ∘ ν_0. ∎

## 2. Lemma R (rigidity of Teichmüller-curve projections), proved under a lifting hypothesis

**Notation.**
- T = T_{h,m} is Teichmüller space with the Teichmüller metric d_T. By Royden's theorem (cited from memory; valid for T_{h,m} with 3h−3+m > 0) this is the Kobayashi distance.
- Γ ⊂ Mod_{h,m} is a torsion-free normal subgroup of finite index (a level subgroup), and M′ = T/Γ. This is a complex manifold, and T → M′ is a holomorphic universal covering. The map M′ → M_{h,m} is finite.

**Hypotheses on E_0 and v.**
- (TC) There is a finite unbranched covering S_0 → Ê_0 and a holomorphic lift f′_0 : S_0 → M′ of f_0. Its lift F̃_0 : S̃_0 = ℍ → T is an isometric embedding for the Kobayashi distances, i.e. a Teichmüller disc. In other words, π_v(E_0) is a Teichmüller curve and f_0 parametrizes it by an orbifold-unramified map.
- Let S_t → Ê_t be the covering corresponding to S_0 under Ĥ_t, and Ĥ′_t : S_0 → S_t the induced homeomorphism.
- (Lift_t) The homotopy of Lemma 1.3, pulled back to S_0, lifts to a continuous homotopy into M′ starting at f′_0. Its end is then f′_t ∘ Ĥ′_t for a lift f′_t : S_t → M′ of f_t ∘ (S_t → Ê_t), and f′_t is automatically holomorphic.

**Remark on (Lift_t).** This is automatic when the factor is M_{0,m} with ordered points, because Mod_{0,m} (pure) is torsion-free and one may take Γ = Mod_{0,m}. It is also automatic when the homotopy avoids the branch locus of M′ → M_{h,m}, by the covering homotopy property. I could NOT prove it in general: transported curves may meet the orbifold locus of M_{h,m} differently from E_0. This is a genuine gap in the general case.

On holomorphy of f′_t: a continuous lift through a finite holomorphic map of normal spaces of a holomorphic map is holomorphic off a nowhere-dense analytic set, hence holomorphic by Riemann extension. If f_t(Ê_t) lies inside the branch locus, one repeats the argument inside the corresponding sub-orbifold. I state this as standard and do not prove it.

**Lemma R.** Assume (TC) and (Lift_t) for all t in a disc Δ_ε. Then π_v(E_t) = π_v(E_0) for all |t| < ε.

*Proof.*

*Step 1 (equivariance).* Let ρ_0 : π_1(S_0) → Γ be the monodromy of f′_0, so that F̃_0 is ρ_0-equivariant. Since f′_t ∘ Ĥ′_t ≃ f′_0 as maps into the K(Γ,1)-manifold M′, the monodromy of f′_t satisfies ρ_t ∘ (Ĥ′_t)_* = ρ_0 up to conjugation in Γ.

*Step 2 (equality at t = 0).* Let γ ∈ π_1(S_0) be represented by a non-peripheral closed geodesic of length ℓ = ℓ_{S_0}(γ). Lengths are taken in the Kobayashi metric of S_0, a fixed multiple of the hyperbolic metric; the same normalization is used throughout.
- F̃_0 is an isometric embedding, so it maps the axis of γ in ℍ to a d_T-geodesic A. The element φ = ρ_0(γ) preserves A and translates along it by ℓ.
- Let τ(φ) = inf_X d_T(X, φX). Then τ(φ) ≤ ℓ, using points of A.
- Conversely, for every X we have n·d_T(X, φX) ≥ d_T(X, φ^n X) by the triangle inequality. Moreover d_T(X, φ^n X) ≥ d_T(X_A, φ^n X_A) − 2 d_T(X, X_A) = nℓ − 2 d_T(X, X_A), where X_A ∈ A. Dividing by n and letting n → ∞ gives d_T(X, φX) ≥ ℓ.
- Hence τ(ρ_0(γ)) = ℓ_{S_0}(γ). This step needs no theory of pseudo-Anosov maps.

*Step 3 (inequality at t).*
- F̃_t : S̃_t → T is holomorphic and ρ_t-equivariant, so it does not increase Kobayashi distance (Royden).
- Hence τ(ρ_t(δ)) ≤ inf_x d_T(F̃_t x, F̃_t δx) ≤ inf_x k_{S̃_t}(x, δx) = ℓ_{S_t}(δ) for every δ ∈ π_1(S_t).
- Put δ = (Ĥ′_t)_* γ. By Step 1 and conjugation invariance of τ, ℓ_{S_t}((Ĥ′_t)_* γ) ≥ τ(ρ_0(γ)) = ℓ_{S_0}(γ) for every simple closed non-peripheral γ.

*Step 4 (Thurston).*
- **Thurston's theorem** (cited from memory: W. Thurston, *Minimal stretch maps between hyperbolic surfaces*, 1986 preprint; stated there for complete finite-area hyperbolic surfaces): if X, Y are complete finite-area hyperbolic structures on the same surface, then sup_γ ℓ_Y(γ)/ℓ_X(γ) ≥ 1, the sup taken over simple closed curves. Equality holds iff some isometry X → Y is homotopic to the identity.
- Apply it with X = (S_t, marking Ĥ′_t) and Y = S_0. Step 3 gives sup_γ ℓ_{S_0}(γ)/ℓ_{S_t}(γ) ≤ 1. S_0 and S_t are of the same finite type by Lemma 1.1, hence of the same area. So there is an isometry ψ_t : S_0 → S_t homotopic to Ĥ′_t.
- By Lemma 1.2, ψ_t is orientation-preserving, hence a biholomorphism.

*Step 5 (Arakelov–Parshin / Imayoshi–Shiga rigidity).*
- The map g_t := f′_t ∘ ψ_t : S_0 → M′ is holomorphic and homotopic to f′_0.
- f′_0 is non-constant, since ρ_0 has elements of infinite order (Step 2 with ℓ > 0).
- **Rigidity theorem** (cited from memory: Imayoshi–Shiga 1988, in the form "a non-constant holomorphic map from a finite-type Riemann surface to M′ is the only holomorphic map in its homotopy class"; this is the rigidity half of the Arakelov–Parshin theorem; see also McMullen's *Rigidity of Teichmüller curves*, which proves exactly Lemma R's conclusion for Teichmüller curves, also from memory). It gives g_t = f′_0.
- Therefore f′_t(S_t) = f′_0(S_0). Projecting to M_{h,m}: π_v(E_t) = f_t(Ê_t) = f_0(Ê_0) = π_v(E_0). ∎

**Note.** If one prefers to avoid the uniqueness form of Step 5, the finiteness form suffices. The set of non-constant holomorphic maps in the homotopy class is finite, and closure(π_v(E_t)) varies continuously in the Hausdorff topology. Hence it is constant.

## 3. Conditional theorem: (T0) at t = 0 implies MS4 (proved, given Lemma R's hypotheses)

**Hypothesis (T0).** There are:
- a point P_0 ∈ closure(∂V_0) \ ∂V_0, lying in a stratum Δ_{G′}. Here G′ degenerates Γ, and vertex i of Γ survives intact as a vertex of G′, by P-b Lemma 1;
- a product (non-quotient) stratum Δ_{G_b} and an irreducible component E_0 of closure(V_0) ∩ Δ_{G_b}, such that some local branch b of E_0 at P_0 has the **merge property**. In the local orbifold chart of M̄_g at P_0, with smoothing parameters s_e (e ∈ E(G′)), let X_b be the set of edges with s_e ≡ 0 on b. Some edge of G′ incident to vertex i is not in X_b. Let c_b : G′ → G_b be the contraction of the edges not in X_b, and v := c_b(i);
- (TC) holds for (E_0, v), and (Lift_t) holds for small t.

**Theorem 3.1.** Under (R1), (R2) and (T0), Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Transport.** Put P_t := H_t(P_0) and E_t := H_t(E_0). By (R2), P_t ∈ Δ_{G′} ∩ closure(∂V_t) ∩ closure(E_t). By P-b Lemma 1, the vertex-i component of P_t is Y_t, with its n_i special points.
2. **The merge type is constant in t.**
   - Fix x ∈ b \ {P_0} close to P_0. The path t ↦ H_t(x) stays in Δ_{G_b} and, for t small, in the chart neighbourhood U of P_0.
   - Lift it to the chart Ũ; paths lift through quotients by finite groups.
   - The preimage of Δ_{G_b} in Ũ is the disjoint union of the sets Z_X = {s_e = 0 exactly for e ∈ X}, over the edge sets X of type G_b. Each Z_X is relatively closed in this union, because closure(Z_X) ∩ Z_{X′} = ∅ for X ≠ X′: points of closure(Z_X) ∩ Z_{X′} would have all edges of X ∪ X′ vanishing, which is more than in type G_b. So the lifted path stays in Z_{X_b}.
   - Hence the transported branch b_t := H_t(b) of E_t at P_t has the same pinched set X_b and the same contraction c_b, for small t.
3. **The limit Q_t.**
   - Along (a lift of) b_t, as x → P_t, the vertex-v component of x converges in M̄_{h,m}. The limit is the stable curve Q_t := P_t[c_b^{-1}(v)]: the components of P_t at the vertices of c_b^{-1}(v), glued along the edges of G′ inside c_b^{-1}(v), with the remaining half-edges as marked points. This is continuity of the gluing/clutching description of the local universal deformation, standard.
   - Since c_b^{-1}(v) contains a G′-edge at i (merge property), Q_t is nodal, i.e. Q_t ∈ ∂M̄_{h,m}.
   - Its component at vertex i, with its special points, is Y_t.
   - Moreover Q_t ∈ closure(π_v(E_t)).
4. **Finiteness.**
   - By Lemma R, closure(π_v(E_t)) = closure(π_v(E_0)) =: F̄_0 for small t. This is a compact irreducible curve not contained in ∂M̄_{h,m}, so K := F̄_0 ∩ ∂M̄_{h,m} is finite.
   - The set 𝒞 of points of M_{g_i,n_i} obtained as a component of some Q ∈ K, with some labelling of its special points, is finite.
5. **Conclusion.** For small t we have Y_t ∈ 𝒞, a finite set, and Y_t is continuous (PR-1). So Y_t = Y_0 for small t, and for all t by PR-1 and the identity theorem. ∎

**Remark (where totally geodesic V_0 enters).** Only in (T0), i.e. in (TC) at t = 0. Nothing is assumed about V_t for t ≠ 0. This is consistent with PR-6: (T0) forbids the log vector fields of PR-6 Theorem B. Theorem 3.1 shows that, under (T0), the flow of such a field cannot move Y_0.

**Theorem 3.2 (second pinning mechanism; PR-3 Lemma F with Lemma R replacing Proposition D).** Suppose there are two irreducible boundary pieces E_0 ⊂ Δ_G and E′_0 ⊂ Δ_{G″}, both product strata. Each passes through a cusp of closure(∂V_0) (points P_0 and P′_0) via a branch along which vertex i stays a vertex, with no merge. Suppose also:
- (TC) and (Lift_t) hold for (E_0, i) and (E′_0, i);
- closure(π_i(E_0)) and closure(π_i(E′_0)) have no common irreducible component.

Then Y_t = Y_0 for all t.

*Proof.* By Lemma R, closure(π_i(E_t)) = closure(π_i(E_0)) and closure(π_i(E′_t)) = closure(π_i(E′_0)) for small t. As in Step 3 of Theorem 3.1, but with no merge, the limit of π_i along the transported branch at P_t is the vertex-i component of P_t, which is Y_t; the same holds at P′_t. Hence Y_t lies in closure(π_i(E_0)) ∩ closure(π_i(E′_0)) ∩ M_{g_i,n_i}. This set is finite, since the two curves have no common component. Y_t is continuous, so it is constant near 0, and constant on Δ by PR-1. ∎

## 4. (T0) for covering constructions over M_{0,5}: SKETCH ONLY (partial, not claimed as proved)

**Setting.**
- Let π : X → P^1 be a degree-d cover branched over 5 ordered points, with monodromy σ_1, …, σ_5 ∈ S_d (transitive, product 1).
- Isometry condition: no σ_k has a fixed point, i.e. every preimage of every branch point is ramified. Under this condition, pulling back quadratic differentials with simple poles at the x_k gives holomorphic quadratic differentials on X. Teichmüller maps lift to Teichmüller maps (Teichmüller's uniqueness theorem). So the induced map T_{0,5} → T_g is a holomorphic isometric embedding, and V_0 = image of the Hurwitz component is totally geodesic.
- Boundary of V_0: the image of the Harris–Mumford admissible-cover compactification, after stabilization.

**Constant factor.** Over the divisor D_{ab} (x_a, x_b collide), the target is T_1(x_c, x_d, x_e, n) ∪ T_2(x_a, x_b, n). Components over T_2 are covers of a 3-pointed P^1, hence constant. A stable such component Z is a typical constant factor Y_0. Its special points are all nodes over n.

**Merge.**
- Take P_0 over D_{ab} ∩ D_{cd}, with target chain T_2(x_a, x_b, n_1) – T_m(n_1, x_e, n_2) – T_3(x_c, x_d, n_2). Take b the branch along D_{cd}.
- Along b, the node n_1 is smoothed. Every special point of Z lies over n_1, so every G′-edge at i is smoothed along b, which gives the merge property.
- The merged component W ⊃ Z lies over T′_1(x_a, x_b, x_e, n_2). It is the orbit of ⟨σ_a, σ_b, σ_e⟩ containing that of Z.

**(TC) for W.**
- W → T′_1 is a cover of a 4-pointed sphere in which every preimage of x_a, x_b, x_e is ramified.
- Unramified preimages of n_2 remain marked (nodes). A tail over T_3 attached at such a point and contracted by stabilization would have degree 1, which contradicts ramification over x_c.
- So pulled-back quadratic differentials are integrable holomorphic on (W, marks), and the covering-construction map from the Hurwitz curve Hur′ (finite étale over M_{0,4}) to T_{h,m} is isometric on universal covers. This is the same Teichmüller-uniqueness argument as above.

**Gaps in this sketch.**
- (g1) One must show that Hur′ → Ê_0 is an unbranched covering (or reformulate Lemma R for Hur′ directly). Royden would give this if f_0 lifts, but that is circular with (Lift).
- (g2) (Lift_t) for t ≠ 0 when h > 0.
- (g3) The bookkeeping of stabilization (contracted rational bridges and tails) in identifying the vertices i and v of the stable graphs.
- (g4) The other kind of constant factor: components over T_1 branched over only 3 of the 4 points. These need a separate merge argument, at the corner where the unbranched point collides.

So even for this class the result is a sketch, not a proof. If (g1)–(g4) are filled, Theorem 3.1 proves MS4 for covering constructions over M_{0,5} satisfying the isometry condition, but only for the constant factors Z over T_2.

## 5. What remains open (explicit)

1. **(T0) in general.** For an arbitrary totally geodesic surface V_0 (e.g. primitive ones such as the flex and gothic loci of McMullen–Mukamel–Wright, or the quadrilateral loci of Eskin–McMullen–Mukamel–Wright, all cited from memory), I cannot show that some cusp of closure(∂V_0) carries a merged boundary branch whose merged projection is a Teichmüller curve. Nor can I show the alternative of Theorem 3.2. Possible failure modes:
   - every boundary branch at every cusp pinches all edges at i (PR-3 §C example);
   - the relevant projection is generated by a quadratic, non-orientable differential. This is harmless for Lemma R, which never uses orientability. Or it is not Teichmüller at all, i.e. some boundary piece is not a Kobayashi geodesic for the sup-product metric. The heuristic that limits of Teichmüller discs are complex geodesics of the product rests only on Minsky's product-region theorem, which has an additive error, so it does not give exact isometry in the limit;
   - closure(∂V_0) has no cusps at all.
2. **(Lift_t)** for factors of positive genus. Orbifold points of M_{h,m} may be met differently by E_t than by E_0.
3. **MS4 itself.** It remains open whether it is true for all V_0. By PR-6 it is equivalent to the absence of suitable log deformations of closure(V_0). I found no counterexample: every concrete construction I examined either keeps Y_0 among rigid (Belyi-type) curves or fails smooth triviality, as in PR-6.

## 6. Critique of the chain
The chain (PR-1 plus the identity theorem) is correct under (R1) and (R2). (R2), which provides a stratified homeomorphism of closures, is a strengthening of the problem's (i)+(ii). The footnote and (i) give smooth triviality stratum by stratum, and (ii) gives compatibility of closures. A global homeomorphism of closures that respects all strata is a natural reading but not literally stated. Lemma 1.1, Lemma 1.2 and Step 2 of Theorem 3.1 use it essentially. Under the weaker literal reading, Lemma B′ of PR-3 must be replaced by the (ii)-based argument of PR-2. That argument additionally needs the isolatedness condition (a) there.

## 7. Summary of status
- **Proved, under (R1) and (R2):** Lemmas 1.1 and 1.3, and Lemma 1.2 (whose argument at the exceptional values t ∈ D is only briefly sketched).
- **Proved, given (TC) and (Lift_t) and the cited theorems of Royden, Thurston and Imayoshi–Shiga (all from memory):** Lemma R. Its Step 2 (translation length equals hyperbolic length at t = 0) is proved elementarily.
- **Proved, given (T0):** Theorems 3.1 and 3.2. These reduce MS4 to a statement about V_0 alone, plus (Lift).
- **Sketch only:** (T0) for covering constructions over M_{0,5}, with gaps (g1)–(g4).
- **Open:** (T0) for general V_0; (Lift_t) in positive genus; MS4 itself. No counterexample was found.

=== END OF ANSWER round5_q3 ===
