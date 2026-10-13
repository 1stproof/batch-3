kind: attempt
Open question attempted: the run's open input (Rig) (ledger entry 69) — that for every admissible family the non-constant part of every boundary piece is rigid (finitely many image curves, independent of t) — WITHOUT the orbifold-transport hypothesis (O_G); equivalently the open questions (Q1′)–(Q3′) of round7_q7 (Lemma R's image constancy at a type-jump time, the factorisation conjecture FAC, and finiteness of puncture values without (O)). Proving (Rig) unconditionally reduces the problem's claim to the single statement MS8.

## Task
Prove the following statement (Rig-all), or a counterexample to it, or reduce it strictly (e.g. prove it whenever closure(V_0) has no point at which a type jump of the orbifold structure of a piece occurs).

**(Rig-all).** Under the readings (R1), (R2) below and the problem's hypotheses (V_0 smooth, closed, 2-dimensional, totally geodesic; the family V_t as in the problem), for every stable graph G and every piece E_0 at time 0 (1-dimensional irreducible component of the lift ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ ∏_w M_w), the transported pieces at time t (the components over H_t(ξ_G(E_0))) have the same set M of non-constant vertices as E_0 and image curves K_t := closure of their image in ∏_{u∈M} M̄_u lying in a finite set of curves independent of t (up to Aut(G)). Consequently (since constant vertices take values in the interior M_w) the puncture values of non-constant vertices lie in a t-independent finite set.

What is known (all spliced below): the constancy part (L1/L1′); every piece at time 0 has a vertex of positive area (Lemma PA) and hence (Lemma T′, modulo the sketched fact (F2)) a Teichmüller vertex v in the orbifold sense; under (O) for v, Lemma R* gives f_v^t∘A_t = f_v^0 (PR-E); under (O_G) — (O) for the whole map to ∏M_w — every non-constant vertex is rigid (L2, round7_q9 §2, spliced); (O) holds between any two times outside a closed discrete set (Lemma G, round7_q7) and under pointwise conditions (Theorem L, earlier file: if at every point of the normalized piece every automorphism of the curve comes from the local group of the orbifold, and the limit curves at punctures have no extra automorphisms); but the map-level conclusion fails without (O) for families of maps (Prop. X, round7_q7), while the image stays constant there. So the target must be image-level. Suggested routes (from round7_q7 §4 and the FAC conjecture; you may use others): (a) rigidity of the image cycle pr_{M*}[𝓦_t] (reduced central fibre when the multiplicity is 1, plus Theorem-L-type analysis on the normalized image family); (b) the factorisation ν_t = Φ∘β_t through a fixed curve; (c) anchor transfer (Cor. G1) plus analytic continuation in t; (d) for non-Teichmüller vertices u, deduce rigidity of K_t from that of the Teichmüller vertex's image via the irreducible 2-dimensional lifted family and the finiteness of the map from the image family to the v-image family.

A proof only for pieces satisfying extra pointwise conditions (no type jump at t = 0, (★), (★∞), no orbifold points) is partial; say exactly what remains. Write any proof in full; cite literature theorems by name with exact hypotheses. Begin with a plan/status line; end with proved / not proved / open.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G (including the open stratum M_g). Write H_t = H(·,t); one may assume H_0 = id. (This is our formalisation of "smoothly trivial" together with (i), (ii).)
- Notation: B_t := closure(V_t) \ V_t; a "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## Prior results (spliced verbatim from earlier answer files)

### PR-D. Lemma R and Lemma R0 (from round5_q1, verbatim). NOTE: Lemma R here tacitly takes orbifold homotopy classes / level lifts for granted; PR-E gives the precise orbifold hypothesis (O) under which it is proved. Its Step 5 (Imayoshi–Shiga) and Step 6 are reused in the chain's Lemma L2.
## 0. Conventions
- H : closure(V_0) × Δ → closure(𝒱) is the stratified homeomorphism of (R2), and H_t = H(·, t).
- Replacing H by H ∘ (H_0^{-1} × id), we may assume H_0 = id.
- Orbifold issues are handled as usual. Pass to a level-N cover (N ≥ 3) of the relevant moduli spaces M_{h,m}. These covers are complex manifolds and fine moduli spaces. The mapping class group Mod_{h,m}[N] is torsion free.
- Homotopy classes of maps from a surface into M_{h,m} are taken in the orbifold sense, i.e. as conjugacy classes of homomorphisms π_1 → Mod_{h,m}. I take this standard reduction for granted, as PR-4 did.
- Let Δ_G be a boundary stratum of product type, i.e. the gluing map ξ_G : ∏_w M̄_w → closure(Δ_G) (product over the vertices w of G, with M_w = M_{g_w,n_w}) is injective on ∏_w M_w, and ξ_G^{-1}(Δ_G) = ∏_w M_w.
- On Δ_G we then have the projections π_w. The map ξ_G is finite and holomorphic (on level covers), and it is not injective over deeper strata in general.
- **Kobayashi normalization.** d_D is the Kobayashi distance of the unit disc D. By Royden's theorem, the Teichmüller metric d_T on T_{h,m} equals the Kobayashi metric. (Cited from memory: Royden 1971 for closed surfaces; the extension to finite type (h,m) is due to Earle–Kra / Gardiner.)
- A holomorphic map does not increase Kobayashi distances.

**Definition.** Let E be an irreducible 1-dimensional analytic curve in Δ_G with normalization ν : Ẽ → E, and let w be a vertex of G. Say **π_w(E) is a Teichmüller curve** if:
- f = π_w ∘ ν : Ẽ → M_w is non-constant, and
- some (equivalently, every) lift F : D → T_w of f to the universal covers is an isometry for the Kobayashi distances: d_T(F x, F y) = d_D(x, y).

This is the standard notion: F is a Teichmüller disc, generated by a quadratic differential, and f(Ẽ) is a (possibly non-primitive) Teichmüller curve.

## 1. Lemma R (rigidity of Teichmüller boundary curves under the family)

**Lemma R.** Assume (R1) and (R2). Let Δ_G be a product-type stratum, and let E_0 be an irreducible component of the 1-dimensional part of closure(V_0) ∩ Δ_G. Put E_t := H_t(E_0). Suppose π_w(E_0) is a Teichmüller curve. Let K_t ⊂ M̄_w be the closure of π_w(E_t). Then K_t = K_0 for all t ∈ Δ.

*Proof.*

**Step 1 (E_t is an irreducible component, of finite type).**
- closure(V_t) ∩ Δ_G is an analytic subset of Δ_G by (R1), and H_t maps closure(V_0) ∩ Δ_G homeomorphically onto it.
- Irreducible components of a 1-dimensional analytic set are topologically determined. A point lies on at least two branches iff the set is not a topological 2-manifold near it, because the punctured neighbourhood is then disconnected. The 1-dimensional irreducible components are the closures of the connected components of the set of manifold points of the 1-dimensional part.
- Hence E_t is an irreducible component of the 1-dimensional part of closure(V_t) ∩ Δ_G.
- closure(E_t) = H_t(closure(E_0)), and closure(E_t) \ E_t = H_t(closure(E_0) \ E_0) is finite. The latter holds because it is a proper analytic subset of the compact irreducible curve closure(E_0).
- So the normalization Ẽ_t is a compact Riemann surface minus finitely many points.

**Step 2 (marking).**
- Let S_t ⊂ E_t be the finite set of multi-branch points. By Step 1, H_t(S_0) = S_t.
- ν_t is biholomorphic over E_t \ S_t. Above a point p ∈ S_t, the points of Ẽ_t correspond bijectively to the connected components of U \ {p}, for U a small conic neighbourhood. H_t preserves this data.
- Hence H_t lifts to a homeomorphism h_t : Ẽ_0 → Ẽ_t, which equals ν_t^{-1} ∘ H_t ∘ ν_0 off ν_0^{-1}(S_0).
- Let f_t := π_w ∘ ν_t. On Ẽ_0^∘ := Ẽ_0 \ ν_0^{-1}(S_0), the map (s, τ) ↦ π_w(H(ν_0 s, τ t)), τ ∈ [0,1], is a homotopy from f_0 to f_t ∘ h_t. It is continuous because H is continuous and maps E_0 × Δ into Δ_G × Δ.
- π_1(Ẽ_0^∘) → π_1(Ẽ_0) is surjective, since we only remove points. So the monodromies satisfy ρ_t ∘ (h_t)_* = ρ_0 up to conjugation in Mod_w.

**Step 3 (length domination).**
- Ẽ_0 is hyperbolic. Otherwise its universal cover is ℂ or ℙ^1, and the lift F_0 into the bounded domain T_w (Bers embedding) would be constant, contradicting non-constancy.
- Ẽ_t is homeomorphic to Ẽ_0, so it is hyperbolic too. Give both surfaces their complete finite-area hyperbolic metrics. Punctures become cusps.
- For a deck transformation γ, let ℓ_t(γ) := lim_n d_D(x, γ^n x)/n. This is the translation length of γ, which is the length of the closed geodesic in Kobayashi normalization, and is 0 for parabolic γ.
- For φ ∈ Mod_w, put ||φ|| := lim_n d_T(y, φ^n y)/n. The limit exists by subadditivity (Fekete) and is independent of y, since |d(y, φ^n y) − d(y′, φ^n y′)| ≤ 2 d(y, y′). It is a conjugacy invariant.
- Let F_t be the ρ_t-equivariant lift of f_t. Then F_t(γ^n x) = ρ_t(γ)^n F_t(x), and F_t is 1-Lipschitz. Hence

  ||ρ_t(γ)|| = lim_n d_T(F_t x, F_t(γ^n x))/n ≤ ℓ_t(γ).
- At t = 0, F_0 is an isometry, so ||ρ_0(γ)|| = ℓ_0(γ).
- By Step 2, ρ_t((h_t)_* γ) is conjugate to ρ_0(γ). Hence for every γ ∈ π_1(Ẽ_0),

  ℓ_0(γ) = ||ρ_0(γ)|| = ||ρ_t(h_{t*} γ)|| ≤ ℓ_t(h_{t*} γ).

**Step 4 (Thurston).**
- **Cited theorem (from memory; Thurston, "Minimal stretch maps between hyperbolic surfaces", 1986 preprint; see also Papadopoulos–Théret's survey on Thurston's asymmetric metric).** Let X, Y be complete finite-area hyperbolic structures on a surface of finite type, marked by the same surface. If ℓ_Y(γ) ≥ ℓ_X(γ) for every simple closed curve γ, then X = Y in Teichmüller space. Equivalently, Thurston's asymmetric distance log sup_γ ℓ_Y(γ)/ℓ_X(γ) is positive for X ≠ Y. I believe Thurston allows cusps; this is flagged as a recollection.
- Apply it with X = Ẽ_0 and Y = Ẽ_t, marked by h_t. There is a biholomorphism k_t : Ẽ_0 → Ẽ_t homotopic to h_t, since a hyperbolic isometry of Riemann surfaces is conformal or anticonformal, and the orientation-preserving class forces conformal.

**Step 5 (Imayoshi–Shiga).**
- Put g_t := f_t ∘ k_t : Ẽ_0 → M_w. It is holomorphic, and by Step 2 its monodromy is conjugate to ρ_0.
- g_t is non-constant. Otherwise ρ_t would have finite image, so ||ρ_0(γ)|| = 0 for all γ, contradicting ℓ_0(γ) > 0 for hyperbolic γ.
- **Cited theorem (from memory; Imayoshi–Shiga 1988, the finiteness theorem behind Arakelov–Parshin rigidity, for families of Riemann surfaces of type (h,m) with 2h−2+m > 0 over a base of finite type).** A fixed (orbifold) homotopy class of maps from a finite-type Riemann surface into M_{h,m} contains only finitely many non-constant holomorphic maps. Use it after passing to a level cover and the corresponding finite étale cover of Ẽ_0, which is again of finite type.
- So g_t ∈ {φ_1, …, φ_r}, a finite set independent of t.
- *Alternative to this citation:* McMullen, "Rigidity of Teichmüller curves" (MRL 2009, from memory), which states that a holomorphic map homotopic to a Teichmüller curve coincides with it.

**Step 6 (closures, and constancy).**
- ξ_G^{-1}(closure(E_t)) is a compact analytic subset of ∏M̄_u. Its 1-dimensional part contains the closure 𝐂_t of the lift ξ_G^{-1}(E_t), which is a compact irreducible curve.
- By Remmert's proper mapping theorem, K_t = pr_w(𝐂_t) is a compact irreducible analytic curve in M̄_w. It is a curve, not a point, since f_t is non-constant.
- K_t contains f_t(Ẽ_t) = g_t(Ẽ_0) with finite complement. So K_t ∈ {K^{(1)}, …, K^{(r)}}, where K^{(j)} is the closure of φ_j(Ẽ_0).
- Fix j, and suppose t_n → t_* with K_{t_n} = K^{(j)}. For every x ∈ E_0 the point π_w(H(x, t_n)) lies in K^{(j)}, and it converges to π_w(H(x, t_*)), because H is continuous and Δ_G × Δ is open in closure(Δ_G) × Δ. So π_w(E_{t_*}) ⊂ K^{(j)}.
- That set is infinite, so the irreducible curves K_{t_*} and K^{(j)} share infinitely many points, and hence they are equal.
- So each set {t : K_t = K^{(j)}} is closed. Finitely many pairwise disjoint closed sets cover the connected set Δ, so only one of them is nonempty. ∎

**Remark (Lemma R0, used below).** In Step 6, the lifted family is analytic componentwise. Precisely:
- Let E_0^{(1)}, …, E_0^{(s)} be the 1-dimensional irreducible components of E_0 := closure(V_0) ∩ Δ_G.
- Put 𝓔^{(a)} := H(E_0^{(a)} × Δ) ⊂ Δ_G × Δ, and let 𝓦^{(a)} be the closure in ∏M̄_u × Δ of its lift (ξ_G × id)^{-1}(𝓔^{(a)}).
- Then 𝓦^{(a)} is an irreducible 2-dimensional analytic set, and its fibre over 0 is contained in 𝐂_0^{(a)} := closure of ξ_G^{-1}(E_0^{(a)}).

*Proof.*
1. **Analyticity of the whole family.** Let 𝓑 := (ξ_G × id)^{-1}(closure(𝒱) ∩ (closure(Δ_G) × Δ)). It is analytic by (R1), and Z := ∂(∏M̄_u) × Δ is analytic. The set 𝓑 \ Z is the lift of closure(𝒱) ∩ (Δ_G × Δ). Its closure 𝓦 is the union of the irreducible components of 𝓑 not contained in Z, so 𝓦 is analytic.
2. **The pieces N^{(a)}.** Let S_0 be the finite set of singular points of the 1-dimensional part of E_0. Let N^{(a)} be the lift of H((E_0^{(a)} \ S_0) × Δ). It is a connected topological 4-manifold, and it is open in 𝓦.
3. **Each N^{(a)} lies in one component.** Removing from N^{(a)} the analytic set Sing(𝓦) (of real dimension ≤ 2 there) does not disconnect it. So N^{(a)} ∩ Reg(𝓦) lies in a single irreducible component of 𝓦, and the closure of N^{(a)} is that component.
4. **The fibre over 0.** By (R2), H is a homeomorphism, so the closure of 𝓔^{(a)} in closure(𝒱) is H(closure(E_0^{(a)}) × Δ), with fibre closure(E_0^{(a)}) over 0. Hence the fibre 𝓦^{(a)}_0 lies in ξ_G^{-1}(closure(E_0^{(a)})). This is ξ_G^{-1}(E_0^{(a)}) together with a finite set.
5. **Conclusion.** 𝓦^{(a)} is irreducible of dimension 2, and t is non-constant on it, so 𝓦^{(a)}_0 is of pure dimension 1. Each of its irreducible curves meets ξ_G^{-1}(E_0^{(a)}) in infinitely many points, so it lies in 𝐂_0^{(a)}. ∎

**Remark.** Lemma R uses neither (ii) nor any hypothesis that V_t is totally geodesic. It replaces Proposition D of PR-3. That proposition needed (H2'), the Toledo invariant, and the citations (K) and (Ct).


### PR-E. Lemma R* with the orbifold hypothesis (O) made explicit (from round5_q4, verbatim)
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



### R7-7. Lemma G (generic (O)), Proposition X (map-level Lemma R* fails without (O)), corollaries, the FAC conjecture, and dead ends (from round7_q7, verbatim)
# round7_q7: (O) / Lemma R without (O)

## Status and plan (written first, updated at the end)
Plan:
(1) Prove a *generic* version of (O): the orbifold type and the monodromy are constant for t outside a closed discrete set D ⊂ Δ (Lemma G).
(2) Derive the consequences: anchor transfer (Cor. G1), and the reduction "Lemma R can fail only if 0 is a jump time" (Cor. G2).
(3) Test the map-level conclusion of Lemma R* (f_t ∘ A_t = f_0) against an explicit global family in mechanism (ram) (Prop. X).
(4) Check the chain lemmas L1 and L2.

Convention used throughout. The cone order e_t(x) of the minimal orbifold structure O_t^min at x ∈ Ẽ_t is the least e ≥ 1 such that Φ_t lifts to an orbifold chart U → U/G_X of M_v after the base change w = s^e at x. Equivalently, it is the order of the local monodromy modulo the elements fixing the local lift pointwise. In the cases at hand this agrees with the definition of PR-K. Note that PR-E's "branch stabiliser" wording would give the wrong answer at coarsely ramified points.

## 1. A global family in mechanism (ram): Lemma R*'s map-level conclusion is false without (O)

**Proposition X.** There is a holomorphic family of maps f_t : Ẽ_t → M_v (t in a disc) with the following properties.
- (a) The source family is the trivial family Ẽ_t = ℂ.
- (b) f_0 = ι ∘ β_0, where ι is the normalisation map of a Teichmüller curve and β_0 is an orbifold-unramified cover, so (H_0) of PR-E holds.
- (c) For t ≠ 0 the type of O_t^min differs from that of O_0: it has two additional cone points of order 2. So (O) fails.
- (d) For t ≠ 0 there is NO biholomorphism A_t : Ẽ_0 → Ẽ_t with f_t ∘ A_t = f_0. This holds whatever the homotopy class.
- (e) Nevertheless f_t(Ẽ_t) = f_0(Ẽ_0) for all t, so the image-level conclusion of Lemma R holds.

This is a family of maps only. I have NOT checked that it arises from the boundary pieces of an admissible family V_t. So it is not a counterexample to Lemma R, to the problem, or to the weak form of L2. It does show that the conclusion of Lemma R* (and therefore the proof of L2, which uses A_t) cannot be obtained without (O) by any argument that only uses the data (source family, f_t, Teichmüller anchor at t = 0).

*Input (cited from memory).* There is a Teichmüller curve ι : C_V = 𝔻/Γ_V → M_v whose Veech group (in PSL_2ℝ) contains an elliptic element of order 2. Example: Veech's double regular pentagon (genus 2, ω ∈ H(2)), whose Veech group is the triangle group Δ(2,5,∞). We may take M_v = M_{2,1} with the unique zero of ω marked. Every affine map fixes the zero, so the Veech group is unchanged. The disc stays isometric in T_{2,1}, since its image in T_2 is isometric and the forgetful map is 1-Lipschitz. The coarse curve C̄_V is ℙ^1 with:
- an orbifold point y of order 2,
- an orbifold point z_5 of order 5,
- one cusp ∞.

Choose the coarse coordinate u with y = 0, z_5 = 1, cusp = ∞. ι is generically injective on C_V: two distinct Teichmüller discs meet in at most one point, because the Teichmüller geodesic through two points is unique, and ι is algebraic.

*The family.* For |t| < 1/2 put β_t(w) := w² + t, β_t : ℂ → ℂ = C_V (coarse), and f_t := ι ∘ β_t. This is holomorphic in (w, t).

*Proof.*
- **(a)** This is immediate from the definition.
- **(b)** β_0(w) = w².
  - Over y: u = w². The orbifold coordinate z at y satisfies z² = u, so z = w is a single-valued local lift, and w = 0 is not a cone point. β_0 is an orbifold covering there.
  - Over z_5: w = ±1, where β_0 is locally biholomorphic, so these are cone points of order 5.
  - Over ∞: one puncture.
  - Hence β_0 : O_0 → C_V, with O_0 = ℂ carrying two cone points of order 5, is an orbifold covering of degree 2. Check: χ(O_0) = 1 − 2·(4/5) = −3/5 = 2·χ(C_V), where χ(C_V) = 2 − 1 − 1/2 − 4/5 = −3/10.
  - So the lift of f_0 to orbifold universal covers is (isomorphism 𝔻 → 𝔻) followed by the isometric Teichmüller disc. This is (H_0).
- **(c)** Let t ≠ 0.
  - Over y = 0: the two points w = ±√(−t) are simple preimages. A local lift needs z = √(β_t(w)), the square root of a function with a simple zero. Every lift of a point of π(L) near X_y is of the form F(±z), because the order-2 elliptic element acts on L by z ↦ −z, and elements fixing L pointwise do not change this. So no local lift exists without the base change, and both points are cone points of order 2.
  - Over u = t (a regular point of C_V): w = 0 is an ordinary critical point of f_t, with cone order 1.
  - Over z_5: two cone points of order 5, as before.
  - So O_t^min = ℂ with cone orders (5, 5, 2, 2), and χ = −8/5 ≠ −3/5. The types differ.
- **(d)** Suppose ι ∘ β_t ∘ A_t = ι ∘ β_0. Then:
  - ι is injective off a finite set, so β_t ∘ A_t = β_0 on a dense open set, hence everywhere.
  - Compare critical values. β_0 has the single finite critical value 0. β_t ∘ A_t has the single finite critical value t, because A_t is biholomorphic.
  - So t = 0. ∎
- **(e)** β_t : ℂ → ℂ is onto, so f_t(ℂ) = ι(C_V) for all t. ∎

**What Prop. X teaches.**
1. In mechanism (ram) the right statement is image-level: "closure(π_v(E_t)) is constant" (Lemma R), not "f_t ∘ A_t = f_0" (Lemma R*). Without (O), the map-level statement can fail even with a smooth, trivial source family.
2. In the example, every map factors through the fixed curve C_V: f_t = ι ∘ β_t, with β_t a family of finite maps. If *all* vertex maps of a piece factor in this way, i.e. ν_t = Φ ∘ β_t for a fixed Φ : C̃ → Δ_G, then the weak L2 conclusion holds: the puncture values lie in Φ(punctures of C̃), a finite set. This suggests the following.

**Conjecture FAC (open).** Under (H_0) for (E_0, v), there are a fixed curve C̃, a map Φ : C̃ → Δ_G that is generically injective and non-constant, and a family of finite maps β_t : Ẽ_t → C̃ such that ν_t = Φ ∘ β_t for all t.
- Under (O) this holds with β_t = A_t^{-1}. Indeed, Lemma R* together with Step 5 of PR-D Lemma R and continuity in t gives ν_t ∘ A_t = ν_0.
- FAC implies Lemma R and the weak L2 conclusion.
- *Caveat on the first bullet.* The continuity in t of A_t is asserted, not proved. A_t is unique in its homotopy class, because isometries of a finite-area hyperbolic orbifold homotopic to the identity are trivial, and continuity should follow from this. This bullet is a sketch.

## 2. Lemma G: (O) holds generically in t

**Setting.**
- 𝓦 is the irreducible 2-dimensional family of Lemma R0, proper over Δ, and n : 𝓦^ν → 𝓦 is its normalisation.
- Φ := pr_v ∘ n : 𝓦^ν → M̄_v.
- Z := ∂(∏_w M̄_w) × Δ, and 𝓟 := n^{-1}(Z) is the "puncture locus", an analytic set of dimension ≤ 1.
- 𝓦^∘ := 𝓦^ν \ 𝓟. For every t, 𝓦^∘_t contains the normalisation of the lift of E_t as an open dense subset, outside the fibres listed in Step 1 below.
- Assume Φ is non-constant on fibres (v is non-constant along E_0; by L1 this holds for all t).

**Lemma G.** There is a closed discrete set D ⊂ Δ such that, for all t, t' in Δ \ D:
- the orbifold curves (Ẽ_t, O_t^min) and (Ẽ_{t'}, O_{t'}^min) have the same type, via a homeomorphism isotopic to the transported marking Ĥ_{t'} ∘ Ĥ_t^{-1};
- under it the monodromies agree: ρ_{t'} = ρ_t ∘ θ.

In other words, (O) of PR-E holds between any two times of Δ \ D.

*Proof (careful sketch).*

**Step 1 (level cover).**
- Let M′ := M_v[N] → M_v (N ≥ 3) be the level cover. It is a manifold, Galois with group G_N, taken modulo K.
- Let 𝓦′ be the normalisation of 𝓦^∘ ×_{M_v} M′, and 𝓦′_1 a connected component with stabiliser G_1 ⊂ G_N. Then 𝓦′_1 → 𝓦^∘ is finite, and it is the quotient by G_1 (normal spaces, generically Galois).
- By the Grauert–Remmert extension theorem for finite branched coverings of normal spaces (cited from memory: a finite branched covering over X \ A, with A nowhere dense analytic and X normal, extends to a finite branched covering of X), 𝓦′_1 extends to a normal space 𝓦̂ finite over 𝓦^ν, with G_1 acting.
- R̂ := ∪_{g ≠ 1} (image of Fix(g)) is analytic in 𝓦^ν by Remmert. It is the closure of the branch locus R.
- All of 𝓦^ν, 𝓦̂, 𝓟 ∪ R̂ are proper over Δ, because 𝓦 is.

**Step 2 (discrete bad set).** Let D be the set of t over which at least one of the following happens:
- (i) a fibre of 𝓦^ν or of 𝓦̂ contains a singular point of the total space, or a critical point of t on its regular part;
- (ii) 𝓟 ∪ R̂ has a vertical component, or a singular point, or a point where its horizontal part is ramified over Δ, or a point where two horizontal components meet.

Each of these is a closed analytic subset of a space proper over Δ, not containing whole fibres, so its image in Δ is closed and discrete:
- Normal surfaces have isolated singularities.
- A curve of critical points of t on a regular surface lies in a fibre: its tangent lies in ker dt, so t is constant along it.
- An analytic curve proper over Δ is étale over Δ off a discrete set.

**Step 3 (fibrewise description).** For t ∉ D, the fibre Ẽ_t := 𝓦^ν_t is a smooth compact curve, and 𝓦̂_t → Ẽ_t is the quotient of the smooth curve 𝓦̂_t by G_1. (A bijective holomorphic map of normal curves is an isomorphism.)
- Since M′ → M_v is the orbifold quotient map of the manifold M′, the local lifts of Φ_t to orbifold charts exist exactly on the local branches of 𝓦̂_t.
- So the cone points of O_t^min in 𝓦^∘_t are the points of R̂_t ∖ 𝓟, and the cone order is the effective order of the G_1-stabiliser of a preimage point.
- By (ii), these points move along the étale horizontal part of R̂ and never meet 𝓟 over Δ \ D. Their orders are constant along each branch of R̂ over Δ \ D: the stabiliser is constant along the smooth curve Fix(g) away from the intersections excluded by (ii).

**Step 4 (Ehresmann and monodromy).**
- Over Δ \ D, the pair (𝓦^ν, 𝓟 ∪ R̂) is a proper submersion with an étale horizontal divisor. So it is a locally trivial family of marked curves (Ehresmann with boundary, i.e. relative isotopy).
- Over Δ \ D, 𝓦̂ is likewise locally trivial, and G_1-equivariantly so.
- Δ \ D is connected (D is discrete in a disc), so all fibres over Δ \ D have the same type.
- The monodromy ρ_t, read off from the G_1-cover together with the monodromy of the family of curves pulled back from M′, is continuous in t on Δ \ D, as a map into the discrete set Hom(Λ_*, Mod_v)/conj. Hence it is constant.
- The type-preserving homeomorphisms obtained by Ehresmann are isotopic to the transported markings, since both vary continuously along paths in Δ \ D. ∎

**Remark.** 0 ∈ D is possible. In PR-K's local models (cross), (fix) and (ram), and in Prop. X, the type jumps exactly at t = 0. Theorem L (PR-K) shows that under (★) and (★∞) the type at 0 is the generic type (O_0 ≅ O_* via the transport), and (O) holds between 0 and nearby t.

## 3. Consequences of Lemma G

**Corollary G1 (anchor transfer).** Suppose that for some t_1 ∈ Δ \ D the map f_{t_1} satisfies (H_0), i.e. it has an isometric equivariant lift onto a Teichmüller disc. Then closure(π_v(E_t)) = closure(π_v(E_{t_1})) for all t ∈ Δ, and in particular for t = 0.

*Proof.*
- By Lemma G, (O) holds between t_1 and every t ∈ Δ \ D.
- Lemma R* (PR-E), applied with base point t_1 in place of 0, gives π_v(E_t) = π_v(E_{t_1}) for t in a neighbourhood of t_1. PR-E's proof never uses that the base time is 0.
- Step 5 of Theorem L (analytic continuation inside the irreducible 𝓦) extends the inclusion π_v(E_t) ⊂ closure(π_v(E_{t_1})) to all t ∈ Δ.
- Equality of closures follows from irreducibility and non-constancy, as in PR-D Step 6. ∎

**Corollary G2 (where Lemma R can fail).** If 0 ∉ D, more precisely if O_0 has the generic type O_* via the transport and ρ_0 corresponds to ρ_*, then (O) holds and Lemma R holds for (E_0, v).

Hence a failure of Lemma R requires both of the following:
- (J1) 0 is a *type-jump time*: (Ẽ_0, O_0) is not of type O_* compatibly with the monodromy;
- (J2) f_t satisfies (H_0) at NO t ∈ Δ \ D, by G1. So all generic members are non-Teichmüller.

Conversely, J1 alone does not make Lemma R fail: Prop. X has J1 but Lemma R holds.

**Corollary G3 (monodromy bookkeeping at a jump; proved).** Let B ⊂ Ẽ_0 be the finite set of points c at which some cone point of O_t^min (t ∉ D) accumulates as t → 0 without being the transport of a cone point of O_0 of the same order, together with the bad punctures.

Let S° := Ẽ_0 minus small discs (and end-neighbourhoods) around B, with the cone points of O_0 that lie in S°. Let P := π_1^orb(S°), and let q_0 : P → Λ_0 and q_* : P → Λ_* be the maps induced by inclusion; q_* uses the transport. Then:
- (1) ρ_* ∘ q_* ≡ ρ_0 ∘ q_0 modulo the pointwise stabiliser A := Fix(𝔇_0) ⊂ Mod_v (mod K).
- (2) For each c ∈ B ∩ Ẽ_0, the cone generators a_1, …, a_k of O_t^min inside the small disc around c satisfy ρ_*(a_i) ∈ Stab(X̂_c), a finite group. Their ordered product is ρ_*(δ_c) = ρ_0(q_0 δ_c) mod A, where δ_c is the boundary loop.
- (3) Im ρ_* is generated by ρ_0(Λ_0)·A and the finitely many finite groups ⟨ρ_*(a_i)⟩.

*Proof.*
- (1) On S°, Theorem L's local analysis applies (Prop. L1 and Cor. L2 at points satisfying (★), Prop. L3 at good ends). So the lifts F_t converge to some lift of f_0 uniformly on compact sets of the universal cover of S°. Lifts of f_0 differ only by elements fixing 𝔇_0 pointwise, and Hom(P, Mod) is discrete.
- (2) For small t, f_t maps the disc around c into the orbifold chart at X_c, so its local monodromy lies in Stab(X̂_c). The product relation is the orbifold disc relation.
- (3) P → Λ_* together with the cone generators at B generates Λ_*. ∎

In (cross) and (ram), δ_c is hyperbolic in Λ_* but ρ_*(δ_c) = ρ_0(q_0δ_c) = 1, so ρ_* is *not faithful*. In (fix), ρ_*(a_i) ∈ A.

## 4. Dead end: inequality-based global arguments cannot settle J1

This section explains why the suggested global inputs do not close the gap. All of them are one-sided in the wrong direction.

- **Royden domination on the level cover.** On the level-N cover the induced cover E′_t of Ẽ_t has χ(E′_t) = |G_1|·χ^orb(O_t^min). In all three mechanisms the generic type has *larger* hyperbolic area than O_0: creation and splitting both decrease χ^orb. As t → 0 the family E′_t degenerates (nodes in (cross)/(ram), a non-reduced fibre in (fix)), and E′_0 is the normalisation of the central fibre. Royden gives ℓ_{E′_t}(γ) ≥ ℓ_{E′_0}(γ) for curves γ away from the vanishing cycles, which is consistent with degeneration: pinching increases lengths of the other curves relative to the filled-in surface. Thurston's theorem needs equal types, so there is no contradiction.
- **Area / Gauss–Bonnet / Toledo.** Abelian case, with Im ρ_* preserving W = span(Re ω, Im ω) (this excludes (cross)). The Harish-Chandra corner entry composed with the period map gives a holomorphic retraction p : T → 𝔻 with p ∘ F_0 = id that is equivariant for W-preserving mapping classes. (Recalled; Kra's theorem that Carathéodory = Kobayashi on abelian Teichmüller discs is the classical form.)
  - For t ∉ D, h_t := p ∘ F_t is σ_t-equivariant, and Γ_* := σ_t(Λ_*) lies between the lattices Γ_0 and Γ_V.
  - A Rouché count in each bad disc and the degree count against 𝔻/Γ_* give deg(h̄_t) = [Γ_* : Γ_0].
  - Schwarz–Pick then yields only Area(O_t) ≥ [Γ_*:Γ_0]·Area(𝔻/Γ_*) = Area(O_0), with equality iff h_t is an isometry. In (ram) the inequality is strict and consistent, as Prop. X confirms.
- **Arakelov-type equality** (Teichmüller curves are maximal Higgs). Again the inequality is 2 deg L_t ≤ −χ^orb(O_t) with deg L_t constant, and −χ^orb(O_t) ≥ −χ^orb(O_0) at a jump. This is consistent.

Conclusion of the dead end. Every comparison of "source size" against "image size" is a Schwarz–Pick inequality, and the jump makes the source bigger. So a proof must use finer structure, for instance FAC-type factorisation or rigidity of the *image cycle*, not length or area inequalities alone.

**A possible route (not carried out): rigidity of the image cycle.**
- The cycles Z_t := pr_{v*}[𝓦_t] form an analytic family of cycles in M̄_v, and Z_0 = d_0·[C̄_V].
- Lemma R ⇔ supp Z_t = C̄_V for all t.
- Write d_0 = d·m_0, with d the generic degree of 𝓦 → 𝓘 := (pr_v, t)(𝓦) and m_0 the multiplicity of 𝓘_0 along C̄_V.
- If m_0 = 1, the normalised image family 𝓘^ν has *reduced* central fibre: div(t) is Cartier on a normal, hence Cohen–Macaulay, surface, so it has no embedded points, and it is generically reduced.
- In Prop. X, and in the local model (ram), m_0 = 1 and d = d_0 = 2. The (ram) jump of the source then becomes a type-preserving deformation of the image curve C_V, where (★) holds at y for the birational map ι. This is why (ram) "should" be harmless at image level.
- What is missing to run PR-K's Prop. L1 on 𝓘^ν: unibranchness of the central fibre, which Lemma N got from (R2), and (R2) is not available for the image family; and the case m_0 > 1.

(The computations in the second and third bullets of §4 are sketches. They explain why a method fails, and are not used anywhere.)

## 5. Check of the chain lemmas

**L1 (constancy persists): correct.** Details:
- Choose an affine open U ∋ Z_0 of the projective coarse space M̄_u, e.g. the complement of a hyperplane section avoiding Z_0.
- Properness of 𝓦 → Δ gives pr_u(𝓦_t) ⊂ U for |t| < ε. Each compact connected curve in 𝓦_t maps to a point of U.
- The set where (pr_u, t) has rank ≤ 1 is analytic and contains a nonempty open set of the irreducible 𝓦, so it is all of 𝓦.
- So the image I := (pr_u, t)(𝓦) is an irreducible analytic curve (Remmert) that surjects onto Δ. Being irreducible, it has no vertical components, so its fibre over each t is finite.
- Hence pr_u is constant on every connected 1-dimensional component of every fibre 𝓦_t.

**L2: the proof is valid only under (O).**
- It uses the biholomorphism A_t of Lemma R*.
- Prop. X shows that without (O) such an A_t need not exist, even for a trivial source family and with the image constant. So L2's *proof* cannot be extended to the jump case.
- Its *conclusion* (finitely many puncture values) is not contradicted: in Prop. X all puncture values are constant.
- Under (O) the remaining steps of L2 are fine:
  - g_0 has infinite monodromy, otherwise a lift to the bounded domain T_u on a finite cover would extend over the punctures and be constant;
  - Imayoshi–Shiga finiteness applies to the fixed source Ẽ_0.

**Chain steps 1–4.**
- Steps 1 and 4 are correct as written, given L2.
- Step 3 currently needs (O) for every piece. By Lemma G and Cor. G1/G2, (O) can be replaced by "0 ∉ D or some generic member is Teichmüller". The genuinely open case is J1 ∧ J2.

## 6. Summary

**Proved.**
- **Prop. X.** An explicit global family f_t = ι ∘ β_t (double regular pentagon Teichmüller curve with its Veech group Δ(2,5,∞), cited from memory; β_t(w) = w² + t) with a smooth trivial source family and an orbifold-unramified Teichmüller anchor at t = 0.
  - For t ≠ 0 it has orbifold type change (O fails) and no A_t with f_t ∘ A_t = f_0.
  - Its image is constant.
  - So the map-level conclusion of Lemma R* is false without (O). The (ram) mechanism globalises, at least as a family of maps.
  - Not checked: realisability as boundary pieces of an admissible V_t.
- **Lemma G** (careful sketch, using the Grauert–Remmert extension theorem and Ehresmann). (O) holds between any two times outside a closed discrete set D ⊂ Δ.
- **Cor. G1** (anchor transfer), **Cor. G2** (Lemma R holds unless J1 ∧ J2), **Cor. G3** (monodromy bookkeeping at a jump: ρ_* agrees with ρ_0 mod A off the bad discs; it is non-faithful in (cross)/(ram); its extra generators lie in finite isotropy groups).
- **Check of L1** (correct), and of L2 (its proof needs (O), and this is unavoidable by Prop. X).

**Not proved / open.**
- (Q1′) Lemma R (image constancy) in case J1 ∧ J2, i.e. when 0 is a type-jump time and no generic member is Teichmüller. This covers (cross), (fix), (ram) and failures of (★∞) that actually produce a jump.
- (Q2′) Conjecture FAC (factorisation ν_t = Φ ∘ β_t through a fixed curve). It would give both Lemma R and the weak L2 conclusion, and it holds in Prop. X and under (O) (sketch).
- (Q3′) The weak L2 conclusion (finitely many puncture values for other vertices u) without (O).
- (Q4′) Whether Prop. X-type families (or the (cross)/(fix) models) are realised by admissible families V_t.
- §4 explains why length, area and Arakelov inequalities cannot settle Q1′: at a jump the generic source orbifold is larger, and all those inequalities are consistent with that. A possible route via rigidity of the image cycle (reduced central fibre when m_0 = 1) is outlined but not completed.


### R7-8. L2 under (O_G) for product strata, and the L2′ sketch for non-product strata (from round7_q9, verbatim, section 2)
## 2. L2

### 2.1 Corrected hypothesis

(O) of PR-E concerns Φ^v_t = π_v ∘ ν_t only. L2 uses, for another vertex u, that f^t_u ∘ A_t and f^0_u have the same orbifold monodromy. That requires:

**(O_u)** The orbifold structures (Λ_t, θ_t) of (O) can be chosen so that, in addition, f^t_u ∘ u_t lifts to a holomorphic f^{u}_t : D → T_u, equivariant for some ρ^u_t : Λ_t → Mod_u with ρ^u_t = ρ^u_0 ∘ θ_t up to conjugation in Mod_u.

Equivalently, assume **(O_G)**: (O) for the product map ν_t : Ê_t → ∏M_w, the Teichmüller space ∏T_w and the group ∏Mod_w. Then (O) for v and (O_u) for all u follow by projection.

*Why this cannot be skipped.* (R2) gives f^t_u ∘ Ĥ_t ≃ f^0_u only as maps into the coarse space M_u. Mod_u is generated by torsion in most cases, so the coarse space has very small fundamental group, and a coarse homotopy carries no information about ρ^u. That is exactly the phenomenon behind (O): cone points can appear or disappear along the family. The reduction (O-a)+(O-b) of PR-E applies verbatim to (O_G), with G_X replaced by the product of the stabilizers, but it has not been proved.

By Lemma O1 (PR-E), cone orders may be enlarged. So once (O-a) holds for v and for u separately, a common orbifold structure (lcm of orders) exists. The compatibility (O-b) for u is the real extra input.

### 2.2 Statement

**Lemma L2 (product G).** Let E_0 be a piece with a Teichmüller vertex v satisfying (H_0), and assume (O_G) for E_0. Let u be a vertex with f^0_u non-constant. Then there is a finite set F(E_0, u) ⊂ M̄_u such that, for every t, every puncture p of Ē_t (E_t = H_t(E_0)) satisfies f^t_u(p) ∈ F(E_0, u).

### 2.3 Proof

1. **A_t.** Lemma R* (PR-E), under (H_0) and (O) for v ⊂ (O_G), gives A_t ∈ PSL_2(ℝ) with A_t Λ_0 A_t^{-1} = Λ_t and A_t λ A_t^{-1} = θ_t^{-1}(λ). The induced map ā_t : D/Λ_0 = Ê_0 → D/Λ_t = Ê_t is an orbifold biholomorphism.
2. **Extension to the compactifications, punctures to punctures.**
   - Ê_t is the uniformized orbifold of the lattice Λ_t. Its ends are the cusps of Λ_t, and these are exactly the punctures of Ē_t. Indeed Ê_t = Ē_t \ {punctures}, a compact Riemann surface minus finitely many points, and finitely many points are removed from the compact Ē_t.
   - A_t is an isometry conjugating Λ_0 to Λ_t. It maps parabolic fixed points of Λ_0 to those of Λ_t, and horoball neighbourhoods to horoball neighbourhoods.
   - So ā_t maps a punctured-disc neighbourhood of each puncture of Ē_0 biholomorphically onto a punctured-disc neighbourhood of a puncture of Ē_t. By the Riemann removable singularity theorem it extends to a biholomorphism Ā_t : Ē_0 → Ē_t, sending punctures bijectively to punctures.
   - θ_t is induced by a homeomorphism homotopic to Ĥ_t^{-1}. Homotopic homeomorphisms induce the same bijection on punctures, since punctures correspond to conjugacy classes of maximal parabolic subgroups. So Ā_t induces the same bijection on punctures as Ĥ_t. This last point is not needed below.
3. **Homotopy.** Put g_t := f^{u}_t ∘ A_t : D → T_u. It is holomorphic, and for λ ∈ Λ_0,
   g_t(λx) = f^u_t(θ_t^{-1}(λ) A_t x) = ρ^u_t(θ_t^{-1}λ) g_t(x) = ρ^u_0(λ) g_t(x)
   after the conjugation allowed in (O_u). So g_t is ρ^u_0-equivariant, i.e. orbifold-homotopic to g_0 = f^u_0. It descends to ḡ_t = f^t_u ∘ Ā_t : Ē_0 → M̄_u, which is holomorphic, being a composite of holomorphic maps.
4. **Infinite monodromy, hence non-constancy.** Suppose ρ^u_0 had finite image.
   - By Selberg's lemma choose a torsion-free Λ′ ⊂ ker ρ^u_0 of finite index in Λ_0.
   - g_0 is Λ′-invariant, so it descends to a holomorphic map from R′ := D/Λ′, a compact Riemann surface R̄′ minus finitely many points, into T_u.
   - T_u is biholomorphic to a bounded domain in ℂ^N (Bers embedding; from memory). Bounded holomorphic functions extend over punctures, and holomorphic functions on the compact R̄′ are constant.
   - So g_0 is constant, a contradiction since f^0_u is non-constant and dim T_u > 0. (If dim M_u = 0, f_u is constant and there is nothing to prove.)
   - Hence ρ^u_0 has infinite image. A constant map has monodromy contained in a finite stabilizer, so every g_t is non-constant.
5. **Finiteness.**
   - Fix N ≥ 3. Let Λ″ := (ρ^u_0)^{-1}(Mod_u[N]) ∩ Λ′, a finite-index torsion-free normal subgroup of Λ_0 (intersect conjugates if needed). Then R := D/Λ″ is a hyperbolic Riemann surface of finite type.
   - Each g_t descends to a non-constant holomorphic map R → M_u[N] = T_u/Mod_u[N]. This is a complex manifold and a fine moduli space of curves of type (g_u, n_u), with 2g_u − 2 + n_u > 0.
   - The homotopy class of this map is ρ^u_0|_{Λ″} up to conjugation by Mod_u. Because of the conjugation in (O_u), this means up to conjugation by one of the finitely many coset representatives of Mod_u/Mod_u[N]. So there are only finitely many homotopy classes.
   - **Cited (from memory): Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces" (MSRI Publ. 11, 1988).** For a Riemann surface R of finite type and a type (h, m) with 2h − 2 + m > 0, a given homotopy class (monodromy) of maps R → T_{h,m}/Γ, Γ torsion-free of finite index, contains at most finitely many non-constant holomorphic maps. I believe they actually prove the rigidity statement "at most one", which is stronger. They also prove that there are finitely many non-trivial families overall, which is the Parshin–Arakelov finiteness.
   - The hypotheses hold: R has finite type, the target is a torsion-free quotient with ordered marked points allowed, and the maps are non-constant by step 4.
   - Hence the descended g_t, and so the g_t and ḡ_t, lie in a finite set {φ_1, …, φ_r} of maps Ē_0 → M̄_u, independent of t. Here ḡ_t is the unique continuous extension of g_t.
   - *Alternatives.* McMullen's rigidity of Teichmüller curves applies only to v, not to a general u, so it does not replace this step. Arakelov–Parshin rigidity (compact base, fixed degeneration set) gives the same conclusion after compactifying and passing to the family over R. I cite only Imayoshi–Shiga.
6. **Puncture values.** If p is a puncture of Ē_t, then q := Ā_t^{-1}(p) is a puncture of Ē_0, and f^t_u(p) = ḡ_t(q). So
   F(E_0, u) := {φ_j(q) : 1 ≤ j ≤ r, q a puncture of Ē_0},
   a finite set independent of t. ∎

### 2.4 Additional remarks

- The addendum "closure(π_u(E_t)) = closure(π_u(E_0))" (PR-D Step 6) also follows in the product case. Step 5 gives K_t ∈ {closure φ_j(Ē_0)}, and the closedness argument of PR-D Step 6 then applies. The chain does not need it.
- **PR-E's (O) does not imply (O_u).** Nothing forces the cone points needed by f_u to coincide with those needed by f_v, or to persist compatibly.

### 2.5 Is (O_G) "automatic when there are no orbifold issues"?

Yes, in this sense. Suppose that for all t, Φ_t = (π_w ∘ ν_t)_w maps Ê_t into the locus where every factor has trivial (effective) automorphism group. Then Φ_t lifts along the honest covering ∏T_w → ∏M_w, restricted to that locus, with Λ_t torsion-free. The monodromy is then defined from the continuous family H by the homotopy lifting property, so ρ_t = ρ_0 ∘ (Ĥ_t)_* holds automatically. (O-b) is immediate from covering theory, and (O-a) is vacuous.

### 2.6 L2′ for non-product G (sketch)

Let C^{(a)} be a 1-dimensional component of C, and C_t := H_t(C^{(a)}) with normalization Ĉ_t. Put Mod_G := the stabilizer of the stratum, an extension of Aut(G) by ∏Mod_w (more precisely: the group generated by ∏Mod_w and the relabelling/permutation lifts of Aut(G)), so that Δ_G = ∏T_w / Mod_G as coarse spaces.

**(O_G, downstairs).** For each t there are:
- an orbifold lattice Λ_t uniformizing Ĉ_t;
- ρ_t : Λ_t → Mod_G;
- an equivariant holomorphic f_t : D → ∏T_w lifting C_t ↪ Δ_G;
- θ_t : Λ_t → Λ_0 as in (O);

with ρ_t = ρ_0 ∘ θ_t up to conjugation in Mod_G.

Put Λ^♮_t := ρ_t^{-1}(∏Mod_w), a finite-index normal subgroup with Λ^♮_t = θ_t^{-1}(Λ^♮_0).
- D/Λ^♮_t → ∏M_w is holomorphic, and its image is dense in a piece at time t.
- Every piece over C_t is obtained this way after composing with an element of Aut(G).
- Cusps of Λ^♮_t map to points over closure(C_t) \ C_t, i.e. to punctures, and every puncture of a piece over C_t arises this way.

Let v be a Teichmüller vertex of some piece over C_0, given by step 2 of the chain. Then the v-coordinate of f_0, restricted to Λ^♮_0, is an isometric equivariant embedding. Run Lemma R* for the lattice Λ^♮_0, using the vertex σ_t(v) at time t, where σ_t is the permutation induced by the conjugating element. This gives A_t conjugating Λ^♮_0 onto Λ^♮_t compatibly with θ_t.

Steps 3–6 of §2.3 then apply verbatim to each vertex u and each of the finitely many Aut(G)-translates. The conclusion: the puncture values at vertex u of all pieces over C_t lie in a finite set F(C^{(a)}, u), independent of t.

I have not written this out in full. The only new ingredients beyond §2.3 are the normality of Λ^♮ and the bookkeeping of Aut(G). Status: **sketch.**


### R7-5. L1 and L1′ (from round7_q9, verbatim, section 1)
## 1. L1

Notation. G is a stable graph, and ξ̄ = ξ̄_G : ∏_w M̄_w → M̄_g is the gluing map. It is finite, and ξ̄ maps ∂(∏_w M̄_w) into strata deeper than Δ_G, since a boundary point of some M̄_w carries an extra node. Hence ξ̄^{-1}(Δ_G) = ∏_w M_w. On coarse spaces, ξ = ξ̄|_{∏M_w} : ∏M_w → Δ_G is the quotient by the finite group Aut(G) (standard; cited from memory). Aut(G) acts by permuting factors and relabelling marked points. In particular ξ is finite and open.

Put A := closure(𝒱) ∩ (Δ_G × Δ) and C := closure(V_0) ∩ Δ_G. By (R2), A = H(C × Δ).

### 1.1 Preliminaries

**(P1) closure(C) \ C is finite.** closure(V_0) is a compact analytic subset of M̄_g by (R1). The set C has dimension ≤ 1. Its 1-dimensional components are open dense subsets of irreducible compact curves, and each such curve meets the deeper strata (a closed analytic set not containing the curve) in finitely many points. The isolated points of C are closed. Since ξ̄ is finite, ξ̄^{-1}(closure(C)) = ξ^{-1}(C) ∪ (a finite set).

**(P2) The lifted family is analytic.** Put 𝓑 := (ξ̄ × id)^{-1}(closure(𝒱)) ∩ (ξ̄^{-1}(closure Δ_G) × Δ). It is analytic in ∏M̄_w × Δ by (R1). Put Z := ∂(∏M̄_w) × Δ, and let 𝓦_G be the closure of 𝓑 \ Z = (ξ×id)^{-1}(A).
- 𝓦_G is the union of the irreducible components of 𝓑 not contained in Z, so it is analytic.
- An irreducible component of 𝓑 minus a proper analytic subset stays irreducible. Hence the irreducible components of 𝓑 \ Z are the traces of these components.
- So the closure of any union of components of 𝓑 \ Z is analytic.
- 𝓦_G → Δ is **proper**, because 𝓦_G is closed in ∏M̄_w × Δ and ∏M̄_w is compact.

**(P3) Local purity.** Near a point of (C^{1} \ Sing) × {t}, where C^{1} is the 1-dimensional part, A is a topological 4-manifold. It is therefore pure 2-dimensional analytic there. Since ξ × id is finite and open, its preimage is also pure 2-dimensional there.

**(P4) Fibres of 2-dimensional components.** Let W be a 2-dimensional irreducible component of 𝓦_G.
- The coordinate t is non-constant on W, because every fibre of 𝓦_G → Δ has dimension ≤ 1: it lies in ξ̄^{-1}(H_t(closure C)), which is 1-dimensional plus a finite set.
- So every fibre W_t is either empty or of pure dimension 1. Fibres of a non-constant holomorphic function on an irreducible 2-dimensional space have pure dimension 1. By properness and the open mapping property, W_t is in fact nonempty for all t.
- By (P1), W_0 ⊂ ξ^{-1}(C) ∪ (finite set). Being pure 1-dimensional, **W_0 is a finite union of closures of pieces at time 0.**
- **Every piece E at time t is dense in a component of W_t for some such W.** Take a generic point x of E, i.e. not over Sing(C_t) and not on other pieces. By (P3), the germ of 𝓦_G at (x, t) is pure 2-dimensional, so E × {t} lies in the union of the fibres of the finitely many 2-dimensional components through nearby points. Since E is irreducible, E ⊂ W_t for one W. Then closure(E) is a component of the pure 1-dimensional set W_t.

### 1.2 L1 in the product case (proved)

Suppose G is of product type, so ξ is injective. By Lemma R0 (PR-D), the 2-dimensional components W are the 𝓦^{(a)}, and W_0 ⊂ 𝐂_0^{(a)} = closure(E_0^{(a)}). By (P4), W_0 is pure 1-dimensional, so **W_0 = closure(E_0)**. Likewise W_t = closure(E_t) with E_t = H_t(E_0): W_t contains the lift of E_t and lies in closure(E_t) ∪ (finite set).

**Lemma L1 (product case).** Suppose pr_u is constant on E_0, equal to Z_0 ∈ M_u. Then for every t, pr_u is constant on every 1-dimensional irreducible component of W_t; here W_t = closure(E_t).

This is the special case of L1′ below in which W_0 has a single component.

### 1.3 L1′ (all G, proved)

**Lemma L1′.** Let W be a 2-dimensional irreducible component of 𝓦_G, and u a vertex of G. Suppose pr_u is constant on each 1-dimensional component of W_0. Then for every t ∈ Δ, pr_u is constant on each 1-dimensional component of W_t.

*Contrapositive (the form used).* Let E be a piece at time t with E ⊂ W_t. If f_u is non-constant on E, then f_u is non-constant on some piece at time 0 contained in W_0.

*Proof.*
1. Let K_1, …, K_r be the components of W_0. The values z_j := pr_u(K_j) lie in M_u, not ∂M̄_u, because K_j is the closure of a subset of ∏M_w and pr_u is continuous.
2. **Affine neighbourhood.** M̄_u (coarse space) is projective (Knudsen–Mumford; from memory), and ∂M̄_u is closed. Choose a homogeneous polynomial vanishing on ∂M̄_u but at none of the z_j. Such a polynomial exists by prime avoidance applied to the homogeneous ideal of ∂M̄_u and the finitely many points z_j. Let U be the complement of its zero set in M̄_u. Then U is affine, U ⊂ M_u, and {z_j} ⊂ U.
3. **Small t.** pr_u(W_0) = {z_j} ⊂ U, and W → Δ is proper. So the set of t with pr_u(W_t) ⊄ U is the image of the closed set W ∩ pr_u^{-1}(M̄_u \ U) under a proper map. It is closed and misses 0, so pr_u(W_t) ⊂ U for |t| < ε.
4. **Compact curves in an affine set.** Each component K of W_t is a compact irreducible curve. Its normalization is a compact connected Riemann surface, and the coordinate functions of U are holomorphic on it, hence constant. So pr_u is constant on each component of W_t for |t| < ε.
5. **Fibre dimension.** Let Φ := (pr_u, t) : W → M̄_u × Δ, a holomorphic map of complex spaces. By the Cartan–Remmert theorem (upper semicontinuity of fibre dimension; from memory), R := {x ∈ W : dim_x Φ^{-1}(Φ(x)) ≥ 1} is an analytic subset of W. By step 4, R contains W ∩ {|t| < ε}, which is a nonempty open subset of the irreducible W. Hence R = W.
6. **All t.** Let K be a component of W_t and x a point of K on no other component of W_t. Near x, Φ^{-1}(Φ(x)) = (pr_u|_K)^{-1}(pr_u(x)), and this has dimension 1 at x. So the analytic subset (pr_u|_K)^{-1}(pr_u(x)) of the irreducible curve K contains a 1-dimensional germ, hence equals K. So pr_u is constant on K. ∎

*Remarks.*
- (a) This rank argument replaces "rank ≤ 1 on an open set, hence everywhere", which is awkward because M̄_u is singular.
- (b) The contrapositive follows from L1′ and (P4).

### 1.4 Why L1 as stated fails for non-product G

The lift of the irreducible family A^{(a)} can have an irreducible component W whose 0-fibre has several components σE_0, σ ∈ Stab(W) ⊂ Aut(G), while W_t is irreducible for t ≠ 0. Then pr_u ∘ σ = r ∘ pr_{σ^{-1}u}, with r a relabelling. So u can be constant on E_0 and non-constant on σE_0, and hence non-constant on W_t for t ≠ 0. Upstairs there is then also no homeomorphism Ē_0 → Ē_t. Nothing in (i), (ii), (R1), (R2) excludes this, since the topology of the finite cover W_t → C_t can change at t = 0.

Local model, ignoring global realizability: σ is the swap on ℂ², and W = {(x − y)^2 = t}. Then W_t (t ≠ 0) is a pair of lines swapped by σ, while W_0 is the diagonal. Combining this with a family in which the two branches over C_0 separate shows that the number of components of W_t can differ from that of W_0.

Indeed, W_0 is a single Stab(W)-orbit of components. Let K be a component of W_0. For generic x ∈ W_0, the point ξ(x) = ξ(k) for some k ∈ K, so x = σk with σ ∈ Stab(W). A component K′ therefore meets σK in infinitely many points, so K′ = σK. The orbit can have several elements.


## Reminder
- Never assume V_t totally geodesic for t ≠ 0. Total geodesy is available only at t = 0.
- Beware: homotopy in the coarse space M_u carries no orbifold-monodromy information; limits of Teichmüller discs asserted to be Teichmüller discs without proof.
