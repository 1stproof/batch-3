# round5_q4 — Lemma R (length-spectrum rigidity) and its use for MS4

## Plan (written first)
1. Part 1: state Lemma R precisely, with the orbifold data made explicit as hypothesis (O). Then prove it with Royden, Bers' axis theorem and Thurston's stretch theorem. A new axis argument replaces Imayoshi–Shiga in step 4.
2. Discuss (O): what is automatic (cone points may disappear), and what is not (cone points may split or be created).
3. Part 2: a conditional pinning theorem (Theorem E*). Then say exactly which inputs are missing for a general V_0, and why the approach cannot be completed for every V_0 with the tools available.

(The final status is in Section 6.)

## 1. Conventions and cited results (all cited from memory)

**Metrics.**
- D is the unit disc with the Poincaré metric |dz|/(1−|z|²) (curvature −4). This is the Kobayashi metric of D.
- With this normalization, a Teichmüller disc z ↦ [X, z·q̄/|q|] is an isometric embedding of D into (T_{h,m}, d_T). The Teichmüller distance from 0 to r ∈ (0,1) is ½ log((1+r)/(1−r)), which is the Poincaré distance.
- For a hyperbolic element γ of a Fuchsian group, ℓ(γ) denotes its translation length in this metric.

**(Roy) Royden; Earle–Kra / Gardiner for punctures.** On T_{h,m} (3h−3+m > 0) the Kobayashi distance equals d_T. Hence every holomorphic map f : D → T_{h,m} satisfies d_T(f x, f y) ≤ d_D(x, y).

**(Bers) Bers' classification.** Let φ ∈ Mod_{h,m} leave a Teichmüller geodesic A invariant and translate along it by ℓ > 0. Then:
- φ is pseudo-Anosov;
- its translation length τ_T(φ) := inf_X d_T(X, φX) equals ℓ;
- the minimum set Min(φ) = {X : d_T(X, φX) = τ_T(φ)} is exactly A, the unique Teichmüller axis of φ. The axis is unique because its defining quadratic differential has the stable and unstable foliations of φ as its vertical and horizontal foliations.

**(Th) Thurston, "Minimal stretch maps between hyperbolic surfaces".** Let X, Y be marked complete finite-area hyperbolic structures on the same surface of finite type. If ℓ_Y(γ) ≥ ℓ_X(γ) for every closed curve γ, then X = Y in Teichmüller space. Equivalently, the asymmetric distance log sup_γ ℓ_Y(γ)/ℓ_X(γ) is ≥ 0, with equality only if X = Y.

**(Sel) Selberg's lemma.** A finitely generated subgroup of PSL_2(ℝ) has a torsion-free normal subgroup of finite index.

## 2. Part 1: Lemma R

### 2.1 Setting and the orbifold data
- E_0 is a 1-dimensional piece of closure(V_0) ∩ Δ_G. Put E_t := H(E_0 × {t}), where H is the homeomorphism of (R2).
- ν_t : Ê_t → E_t is the normalization. H_t lifts to a homeomorphism Ĥ_t : Ê_0 → Ê_t, because the branches of a curve at a point are the connected components of its punctured link, which is a topological notion.
- v is a vertex of G with factor M_{h,m}, and Φ_t := π_v ∘ ν_t : Ê_t → M_{h,m}.

**The orbifold issue.** T_{h,m} → M_{h,m} is not a covering map. It is branched over the locus B of curves with extra automorphisms. So "lifting Φ_t to universal covers" needs an orbifold structure on Ê_t. The hypothesis of Lemma R at t = 0 means the following.

**(H_0)** There are:
- a lattice Λ_0 ⊂ PSL_2(ℝ) = Aut(D), possibly with torsion, and an orbifold uniformization u_0 : D → D/Λ_0 ≅ Ê_0;
- a homomorphism ρ_0 : Λ_0 → Mod_{h,m};
- a holomorphic ρ_0-equivariant map f_0 : D → T_{h,m} lifting Φ_0 ∘ u_0, which is an isometric embedding onto a Teichmüller disc 𝔇_0.

**(O) Transport of the orbifold data.** For every t there are:
- a lattice Λ_t with orbifold uniformization u_t : D → Ê_t (for the complex structure of Ê_t);
- a holomorphic map f_t : D → T_{h,m} lifting Φ_t ∘ u_t, equivariant for some ρ_t : Λ_t → Mod_{h,m};
- an isomorphism θ_t : Λ_t → Λ_0, induced by an orientation-preserving homeomorphism Ê_t → Ê_0 that preserves cone points with their orders and cusps, and is homotopic to Ĥ_t^{-1};

such that ρ_t = ρ_0 ∘ θ_t (after conjugating f_t by an element of Mod_{h,m}).

Section 2.3 discusses when (O) holds. It is not automatic.

### 2.2 Statement and proof

**Lemma R\*.** Assume (H_0) and (O). Then f_t ∘ A_t = f_0 for some A_t ∈ PSL_2(ℝ) conjugating Λ_0 onto Λ_t compatibly with θ_t. In particular π_v(E_t) = π_v(E_0) for all t.

*Proof.*

**Step 1 (ρ_0 is faithful, and hyperbolic elements map to pseudo-Anosovs).**
- f_0 is an equivariant isometry onto 𝔇_0. So ρ_0(γ) preserves 𝔇_0 and acts on it as f_0 ∘ γ ∘ f_0^{-1}. In particular ρ_0 is injective.
- If γ ∈ Λ_0 is hyperbolic with axis α_γ ⊂ D, then ρ_0(γ) preserves the Teichmüller geodesic f_0(α_γ) and translates it by ℓ_0(γ) > 0.
- By (Bers), ρ_0(γ) is pseudo-Anosov, τ_T(ρ_0(γ)) = ℓ_0(γ), and Min(ρ_0(γ)) = f_0(α_γ).

**Step 2 (Schwarz–Pick inequality at time t).** Let γ ∈ Λ_t be hyperbolic, with axis α and x ∈ α. By (Roy) and equivariance,
  d_T(f_t x, ρ_t(γ) f_t x) = d_T(f_t x, f_t(γx)) ≤ d_D(x, γx) = ℓ_t(γ).
Hence τ_T(ρ_t(γ)) ≤ ℓ_t(γ).

**Step 3 (length domination).**
- θ_t is type-preserving, so γ is hyperbolic iff θ_t γ is.
- By (O), ρ_t(γ) = ρ_0(θ_t γ). By Step 1, τ_T(ρ_0(θ_tγ)) = ℓ_0(θ_tγ).
- Hence ℓ_t(γ) ≥ ℓ_0(θ_t γ) for every hyperbolic γ ∈ Λ_t.

**Step 4 (Thurston, with orbifolds handled through a manifold cover).**
- By (Sel), choose a torsion-free normal subgroup Λ'_0 ⊂ Λ_0 of finite index, and put Λ'_t := θ_t^{-1}(Λ'_0).
- D/Λ'_t and D/Λ'_0 are complete finite-area hyperbolic surfaces. θ_t is induced by a homeomorphism (lift the cone-preserving homeomorphism of (O) to the corresponding finite orbifold covers), so they are marked surfaces of the same type.
- Closed geodesics correspond to hyperbolic elements. By Step 3, ℓ_{D/Λ'_t} ≥ ℓ_{D/Λ'_0} on all closed curves.
- By (Th) the marked structures coincide: there is A_t ∈ PSL_2(ℝ) with θ_t^{-1}(λ) = A_t λ A_t^{-1} for all λ ∈ Λ'_0.
- **Extension to Λ_0.** The two faithful representations λ ↦ λ and λ ↦ A_t^{-1} θ_t^{-1}(λ) A_t of Λ_0 agree on the normal subgroup Λ'_0. Take g ∈ Λ_0 and put c = g^{-1}·A_t^{-1}θ_t^{-1}(g)A_t. For λ ∈ Λ'_0, applying the second representation to gλg^{-1} ∈ Λ'_0 shows that c commutes with λ. So c centralizes Λ'_0. Λ'_0 is a lattice, hence non-elementary, so its centralizer in PSL_2(ℝ) is trivial and c = 1.
- Therefore A_t conjugates Λ_0 onto Λ_t compatibly with θ_t, and A_t induces a biholomorphism of orbifolds Ê_0 → Ê_t homotopic to Ĥ_t.

**Step 5 (the maps coincide; this replaces Imayoshi–Shiga).**
- Put g_t := f_t ∘ A_t : D → T_{h,m}. It is holomorphic and ρ_0-equivariant: g_t(λx) = f_t(A_t λ A_t^{-1}·A_t x) = ρ_t(θ_t^{-1}λ) g_t(x) = ρ_0(λ) g_t(x).
- Let λ ∈ Λ_0 be hyperbolic and x ∈ α_λ. Then d_T(g_t x, ρ_0(λ) g_t x) ≤ d_D(x, λx) = ℓ_0(λ) = τ_T(ρ_0(λ)). So equality holds, g_t x ∈ Min(ρ_0(λ)), and by Step 1, g_t(α_λ) ⊂ f_0(α_λ).
- Let p = α_λ ∩ α_μ be a transverse intersection point of two distinct axes. Then g_t(p) ∈ f_0(α_λ) ∩ f_0(α_μ) = f_0(α_λ ∩ α_μ) = {f_0(p)}, using injectivity of f_0. So g_t(p) = f_0(p).
- For a lattice, the pairs of endpoints of axes of hyperbolic elements are dense in ∂D × ∂D. So transverse intersection points of axes are dense in D.
- By continuity, g_t = f_0.

**Step 6 (conclusion).** Φ_t ∘ u_t ∘ A_t = Φ_0 ∘ u_0, so π_v(E_t) = Φ_t(Ê_t) = Φ_0(Ê_0) = π_v(E_0). ∎

**Checks requested by the task.**
- *Elliptic elements and orbifold points.* They are handled by the orbifold uniformization in (H_0) and (O), and by passing to Λ'_0 in Step 4. Step 5 uses only hyperbolic elements, which exist in abundance.
- *Cusps.* Parabolic elements impose no constraint: (Th) concerns only closed geodesics. Their type is preserved by θ_t, which is part of (O).
- *E_0 → π_v(E_0) not injective.* This is harmless. Λ_0 is then a finite-index subgroup of the stabilizer of 𝔇_0, and nothing above uses injectivity of Φ_0. Only injectivity of f_0 is used, and that follows from f_0 being an isometry.
- *Abelian versus quadratic differentials.* None of this needs 𝔇_0 to be generated by an abelian differential. This is an improvement over Proposition D of PR-3, which needed (H2′). Lemma R\* also does not use the cited results (K) or (Ct).

### 2.3 On hypothesis (O): what is proved, what is not

**Minimal pullback orbifold.** For each t, call a point x ∈ Ê_t a cone point of order e_t(x) when the following holds. Near x, Φ_t maps into an orbifold chart ℂ^n/G_X of M_{h,m}. The preimage of the image germ in ℂ^n consists of branches; take the branch that is the normalization lift of the germ of Φ_t at x, and let e_t(x) be the order of the subgroup of G_X stabilizing it. (Modulo the generic automorphism group in the hyperelliptic-type cases h = 2, (h,m) = (1,1), and so on, where G_X is replaced by its effective quotient.) This is the smallest orbifold structure O_t^min on Ê_t over which Φ_t lifts locally.

**Lemma O1 (enlarging cone orders is free).** Suppose f : D → T_{h,m} is holomorphic and equivariant for the uniformization of some orbifold structure O on Ê_t. Let O′ have cone points containing those of O, with orders e′(x) divisible by e(x), and no other changes. Then there is a holomorphic f′ : D → T_{h,m}, equivariant for the uniformization of O′, lifting the same map Φ_t.

*Proof.* The orbifold fundamental group Λ′ of O′ surjects onto that of O, since the relations c^{e′} are implied by c^{e}. The identity of Ê_t lifts to a holomorphic map ψ : D → D that is equivariant for Λ′ → Λ. Near a cone point, locally ψ is z ↦ z^{e′/e} in orbifold charts. Put f′ = f ∘ ψ. ∎

**Consequence.** Condition (O) follows from (O-a) and (O-b) below.
- **(O-a)** For every t near 0, the cone points of O_t^min lie at the transported points Ĥ_t(c), c a cone point of O_0, possibly up to an isotopy within small discs. Their orders divide e_0(c), and no cone points arise near the cusps.
- **(O-b)** The local lifts f_t can be chosen to depend continuously on t, uniformly on compact subsets of D minus the cone-point orbits.

Indeed:
- By Lemma O1, (O-a) lets us use, at every t, the orbifold structure with cone orders exactly e_0 at the transported cone points. Its type is that of O_0.
- (O-b) makes t ↦ ρ_t ∘ θ_t^{-1} a continuous map into Hom(Λ_0, Mod_{h,m}). This set is discrete, since Λ_0 is finitely generated and Mod is discrete. So the map is constant, and ρ_t = ρ_0 ∘ θ_t.

**What can actually happen (local model, so that (O-a) is not vacuous).**
- **Disappearance (allowed by (O-a)).** Let 𝓤′ = ℂ² with ℤ/e acting by (w,s) ↦ (ζw, ζ^b s), (b,e) = 1. Map it equivariantly to ℂ^n ⊃ ℂ² by (w,s) ↦ (w,s,0,…), where G_X ⊃ ℤ/e acts on ℂ^n with these weights. Use the parameter t = s^e on 𝓤 = 𝓤′/(ℤ/e).
  - Every fibre U_t is a disc, so the family is topologically trivial.
  - At t = 0 the curve passes through the orbifold point, and U_0 has a cone point of order e.
  - At t ≠ 0 the image is a translate of the line missing Fix(ℤ/e), and there is no cone point.
  - This is exactly the situation Lemma O1 absorbs.
- **Creation is excluded near a point with e_0 = 1 (proof sketch).** A branch at time t that is invariant under g ≠ 1 converges, as t → 0, to a g-invariant branch at time 0 through the limit point. So the stabilizers at small t are, up to conjugacy, subgroups of the stabilizer at t = 0. This sketch ignores points escaping to cusps.
- **Splitting is NOT excluded by me.** One cone point of order e_0 at t = 0 might give several cone points near Ĥ_t(c) at t ≠ 0, with orders dividing e_0. Two cases:
  - If the normalized total space 𝓤′ of the local lifted family is smooth at the cone point, then g acts on the tangent space ℂ² with weights (1, b). All Fix(g^k) of dimension 1 lie in the single eigenline of weight b. So there is at most one cone point nearby, and (O-a) holds locally.
  - If 𝓤′ is singular there, I cannot exclude several fixed curves.
- **Cone points coming in from cusps.** These are also not excluded.

**Conclusion of 2.3.** **Lemma R\* is proved under (O)**, and (O) is reduced to the local statement (O-a)+(O-b). That statement is proved only in the smooth-total-space case, and only sketched there. Without (O) the argument breaks at Step 3. If the orbifold type of Ê_t differs from that of Ê_0, the lengths ℓ_t and ℓ_0 live on non-isomorphic groups, and (Th) has no cross-type version: the areas differ, so domination of lengths cannot force equality.

## 3. Part 2: pinning with Lemma R\*

### 3.1 The conditional theorem

**Theorem E\*.** Assume (R1) and (R2). Suppose there are:
- a cusp P_0 ∈ closure(∂V_0) \ ∂V_0, lying in a stratum Δ_{G′};
- a boundary branch b of closure(V_0) at P_0 with the merge property (PR-3, §C), with generic dual graph G_b and merged vertex v ⊃ {i} carrying the factor M_{h,m};
- the 1-dimensional piece E_0 of closure(V_0) ∩ Δ_{G_b} containing b \ {P_0};

such that π_v|_{E_0} satisfies (H_0) and the transported family E_t satisfies (O). Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*

**Step 1 (transport).**
- Put P_t := H(P_0, t), E_t := H(E_0 × {t}), b_t := H(b × {t}) and β_t := H(β × {t}), where β is a branch of closure(∂V_0) at P_0.
- By Lemma B′ of PR-3 (a formal consequence of (R2)), b_t is a boundary branch of closure(V_t) at P_t with b_t \ {P_t} ⊂ E_t ⊂ Δ_{G_b}, and β_t ⊂ closure(∂V_t).

**Step 2 (Y_t is a component of a limit point of F_t := π_v(E_t)).**
- Work in an orbifold chart W ≅ (∏_c Def(C_c) × ∏_{e∈E(G′)} ℂ_{s_e})/Aut(P_0) of M̄_g at P_0. Here the C_c are the components of P_0 and s_e are the node-smoothing parameters. For small t, P_t lies in W.
- Lift β_t and b_t to the chart, continuously in t. This is possible for small t: take the lifts of β, b at t = 0 and use continuity of H together with finiteness of the chart map.
- Along the lift of β_t \ {P_t}, exactly the edges of Γ are pinched (s_e = 0 iff e ∈ E(Γ)). By P-b Lemma 1, the component of P_t in the chart position of the vertex-i component is Y_t.
- Along the lift of b_t \ {P_t}, the pinched edges are the same set X_b ⊂ E(G′) for all small t. The vanishing pattern is locally constant on the connected set ∪_t b_t \ {P_t}, because H maps (b \ {P_0}) × Δ into Δ_{G_b} × Δ.
- So for x ∈ b_t near P_t, π_v(x) is a smoothing of the subcurve Q_t of P_t made of the components joined to the vertex-i component by edges outside X_b. These nodes are unpinched, the nodes of X_b inside Q_t's boundary become marked points, and the node parameters inside Q_t are nonzero but tend to 0.
- As x → P_t along b_t, π_v(x) → Q_t in M̄_{h,m}. So Q_t ∈ closure(F_t) ∩ ∂M̄_{h,m}: Q_t lies in the boundary because, by the merge property, at least one edge of G′ lies inside v.
- Y_t is a component of Q_t.

**Step 3 (pinning).**
- By Lemma R\*, F_t = F_0, so closure(F_t) = closure(F_0).
- closure(F_0) is a compact curve that is not contained in ∂M̄_{h,m}. So Σ := closure(F_0) ∩ ∂M̄_{h,m} is finite.
- By Step 2, for small t, Y_t is a component of one of the finitely many stable curves in Σ. These have finitely many components in total, so Y_t ranges over a finite subset of M_{g_i,n_i} (as a pointed curve with its markings). The marking order of the special points is fixed, because the labelling of the half-edges at vertex i is constant in t.
- t ↦ Y_t is continuous (PR-1), so it is constant near 0, and by the identity theorem (PR-1, Corollary) it is constant on Δ. ∎

**Variant (Lemma F of PR-3 with Proposition D replaced by Lemma R\*).** Suppose the merge property fails, but there are two non-merging boundary pieces E_0, E′_0 through cusps of ∂V_0 with the following properties:
- π_i(E_0) and π_i(E′_0) are curves satisfying (H_0), with (O) for their transports;
- they have no common component through Y_0.

Then Y_t is constant. The proof is PR-3's, with Lemma R\* in place of Proposition D.

### 3.2 A class of V_0 where the pinning configuration exists (sketch)

Take covering-construction surfaces. Let V_0 be the image of a finite map M_{0,5} → M_g given by a fixed covering type: degree-d covers of ℙ^1 branched over the 5 marked points, with all ramification indices over the 5 points even. Then pulled-back quadratic differentials with simple poles at the 5 points are holomorphic, and T_{0,5} → T_g is a holomorphic isometric embedding (classical, cited from memory). Assume this image is smooth, as the problem requires.

Its closure is the image of the admissible-covers compactification over M̄_{0,5}.
- **The constant factor.** A boundary curve ∂V_0 is the image of a divisor D_{jk} ≅ M_{0,4} × M_{0,3}. The constant factor Y_0 is a component of the admissible cover lying over the 3-pointed sphere A. It is a Belyi curve.
- **The cusps.** The cusps of closure(∂V_0) lie over the 0-dimensional strata: chains A – B – C of three spheres.
- **The merging branch.** The other boundary divisor through such a point smooths the node A–B. Every component Y_0 over A contains preimages of that node, so the merge property holds.
- **The merged projection.** The merged-vertex projection F_0 is the image of M_{0,4} under the covering construction for covers of the sphere A ∪ B branched over 4 points. Over the 3 original points the ramification is even, so the pulled-back differential is holomorphic there. Over the node, the preimages are marked points, where simple poles are allowed. Hence T_{0,4} → T_{h,m} is again an isometric embedding of a disc, and (H_0) holds.
- **Conclusion.** For this class, Theorem E\* gives MS4, **provided (O) holds**. I have not verified (O) there. The relevant orbifold points are the curves of F_t with extra automorphisms, typically deck transformations of the cover.

## 4. Why the approach cannot settle MS4 for every V_0 with present tools

The task asks for a pinning configuration for EVERY V_0, Γ, i. I could not produce one. Below are the precise obstructions, each a statement about V_0 alone (t = 0). Recall PR-6: no argument using only (i), (ii), (R1), (R2) near Δ_Γ can work, so total geodesy has to enter exactly here.

**(N1) Cusps may not exist.**
- Write ∂V_0 = {Y_0} × C_0. closure(∂V_0) has a cusp iff C_0 is not compact in ∏_{j≠i} M_{g_j,n_j}.
- Compact curves exist in M_{g,n} for 3g−3+n ≥ 3 (Satake–Baily–Borel, cited from memory). So compactness of C_0 is not excluded by dimension reasons.
- If some projection π_j(C_0) is a Teichmüller curve, then C_0 has a cusp. This uses Veech's theorem, cited from memory, that lattice Veech groups are never cocompact. But I see no reason why a projection of C_0 must be a Teichmüller curve (see N3).

**(N2) The merge property (C-merge) is not proved.** See PR-3 §C, whose model shows that local data cannot force it.

**(N3) Why (H_0) at the merged vertex is not automatic. The following heuristic suggests it may fail.**
- By Wright's correspondence (cited from memory), V_0 corresponds to a rank-2 GL_2(ℝ)-orbit closure 𝓜 of quadratic differentials of complex dimension 4. Its projectivization P𝓜 has dimension 3 and maps to V_0 with ℙ^1 fibres.
- The boundary of closure(P𝓜) over the 1-dimensional ∂V_0 is 2-dimensional with 1-dimensional fibres.
- Consider the limiting (multi-scale) differentials over ∂V_0. Either:
  - (α) their GL_2(ℝ)-orbits project onto open subsets of ∂V_0; or
  - (β) the orbits lie in the fibres, i.e. they map to points of ∂V_0.
- In case (α), the component Y_0 at vertex i must carry a limit differential whose orbit does not change the conformal structure of Y_0. For a finite-area nonzero differential on a stable Y_0 with dim M_{g_i,n_i} > 0 this is impossible, because the affine map is then a Teichmüller map with K > 1.
- So Y_0 sits at a lower level with the level-phase phenomenon, or case (β) holds. In case (β), ∂V_0 is **transverse** to the GL_2(ℝ)-directions, and nothing forces any projection of a boundary piece to be a Teichmüller curve.
- A proof would need a boundary theorem of roughly this form: at a cusp of ∂V_0 some boundary branch b has the merge property, and its merged component carries a nonzero WYSIWYG limit differential whose boundary orbit closure (Mirzakhani–Wright, cited from memory) has projective dimension 1, so that π_v(E_0) is a Teichmüller curve.
- I could not prove such a statement, and the heuristic above suggests it can fail. The pieces through the cusps of a type-(β) boundary curve need not be Teichmüller curves.

**(N4) The orbifold condition (O)** is an additional, genuinely t-dependent input (Section 2.3). Lemma R\* needs it even when (H_0) holds.

So the approach as specified must fail for any V_0 for which, at all cusps of closure(∂V_0) (or with no cusps at all), none of the boundary branches has a projection satisfying (H_0). I cannot exhibit such a V_0, and I cannot exclude one.

## 5. Remarks on the chain
- I accept the derivation in the task: MS4 is the problem's claim under (R1) and (R2), and it reduces to local constancy of Y by PR-1.
- Theorem E\* uses (R2) only through Lemma B′ and the chart argument of its Step 2.
- Lemma R\* uses (R2) only to obtain the homeomorphisms Ĥ_t and the homotopy class for θ_t.

## 6. Final status

**Proved** (modulo the classical results (Roy), (Bers), (Th) and (Sel), cited from memory):
- **Lemma R\* (Section 2.2).** Under (H_0) and the orbifold-transport hypothesis (O), π_v(E_t) = π_v(E_0) for all t; in fact the lifted maps agree after a Möbius reparametrization.
  - No abelian-differential hypothesis is needed, and (K), (Ct) and Imayoshi–Shiga are not used. Step 5 is a new axis-intersection argument.
  - Elliptic elements, cusps and non-injective E_0 → π_v(E_0) are handled.
- **Lemma O1.** Cone points that disappear or drop to an order dividing the original are harmless. So (O) follows from the local conditions (O-a) and (O-b).
- **Theorem E\* (Section 3.1).** Under (R1) and (R2), suppose there is a cusp of closure(∂V_0) with a merging boundary branch whose merged projection satisfies (H_0) and (O). Then Y_t ≡ Y_0, i.e. the problem's claim holds. The two-branch variant (Lemma F with Lemma R\*) also holds.

**Sketched only:**
- Non-creation of cone points (2.3).
- (O-a) when the local lifted total space is smooth (2.3).
- The covering-construction class over M_{0,5} (3.2), where the pinning configuration and (H_0) exist but (O) is unverified.

**Open (not proved here):**
1. **(O) in general:** can cone points of the pullback orbifold split, or enter from cusps, along the family E_t?
2. **(N1)** Must closure(∂V_0) have a cusp? Equivalently, can C_0 be compact?
3. **(N2)** Does (C-merge) always hold?
4. **(N3)** At some cusp, is there always a boundary branch whose projection to the merged (or the i-th) vertex is a Teichmüller curve? The heuristic in (N3) suggests that this may fail for boundary curves transverse to the GL_2(ℝ)-directions.

**Conclusion.** MS4, and hence the problem's claim, is **not** established for every V_0 by this approach. It is established only under the stated conditions: (C-merge), (H_0) at the merged vertex, and (O).

=== END OF ANSWER round5_q4 ===
