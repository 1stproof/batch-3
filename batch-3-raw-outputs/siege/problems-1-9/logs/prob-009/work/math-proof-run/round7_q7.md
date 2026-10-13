kind: attempt
Open question attempted: the orbifold-transport input (O) of the run's chain (ledger entry 41) — Lemma R without (O) — in the cases not covered by Theorem L (ledger entry 46).

## Task
The chain of this run (below) needs, for a 1-dimensional boundary piece E_0 of closure(V_0) whose projection to a vertex v is a Teichmüller curve in the orbifold sense, the conclusion of Lemma R* (PR-E): an orbifold biholomorphism A_t: Ẽ_0 → Ẽ_t homotopic to the transported marking with f_t ∘ A_t = f_0 — or at least the weaker conclusion actually used downstream (lemma L2 below): for every vertex u non-constant on E_0, the limit values of π_u at the punctures of Ẽ_t lie in a finite set independent of t. Lemma R* is proved under (O). Theorem L (round6_q7, spliced below) proves (O) under pointwise conditions (★) and (★∞), and exhibits local models (cross), (fix), (ram) showing that local analysis cannot give (O) otherwise.

Prove the conclusion of Lemma R* (or the weaker L2 conclusion) WITHOUT (O), for every piece and Teichmüller vertex as above — or give an explicit global counterexample (a family f_t of maps from deforming finite-type orbifold curves to M_v, with f_0 an orbifold-unramified cover of a Teichmüller curve, arising as boundary pieces of an admissible family V_t), each check written out. A proof only when (★) holds, or only for some of the mechanisms (cross)/(fix)/(ram)/(★∞), is partial; report it labelled as such and say what remains.

Suggested global inputs (free to discard): the total family is a holomorphic family over Δ of maps from a topologically trivial family of punctured curves (Lemma N of Theorem L's file); Royden domination ℓ_t ≥ (translation lengths of the fixed monodromy) holds for every manifold cover on which the monodromy lifts — choose a finite-index torsion-free subgroup Γ′ ⊂ Mod_v and pass to the corresponding finite cover of the family (a level-structure cover), where no orbifold issue arises, and compare Thurston's theorem on that cover (is the induced finite cover of Ẽ_t of constant topological type in t? — its topological type is determined by the monodromy, which is constant); area/Euler characteristic bookkeeping; McMullen's rigidity of Teichmüller curves; Lemma D (negative normal degree) of Theorem L's file.

## Readings
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G. H_t = H(·,t).

## How the statement is used (the chain) — check it, and say so explicitly if any step is flawed

Two chain lemmas (the planner's derivations; not yet checked in writing — if you find a flaw, say so):

**L1 (constancy persists).** Let E_0 be a piece at time 0 in a stratum G, and let 𝓦 ⊂ ∏_w M̄_w × Δ be its lifted family as in Lemma R0 of PR-D (the closure of the lift of H(ξ_G(E_0) × Δ); an irreducible 2-dimensional analytic set, proper over Δ, fibre over 0 inside the closure of the lift of E_0). If pr_u is constant (= Z_0 ∈ M_u) on E_0, then for every t, pr_u is constant on every 1-dimensional irreducible component of the fibre 𝓦_t (in particular on the transported piece E_t).
*Proof sketch.* Take an affine open U ∋ Z_0 in the quasi-projective coarse space M_u. Since 𝓦 → Δ is proper and pr_u(𝓦_0) = {Z_0}, pr_u(𝓦_t) ⊂ U for |t| < ε. A holomorphic map from a compact connected analytic curve to an affine variety is constant. So the map (pr_u, t): 𝓦 → M̄_u × Δ has rank ≤ 1 on a nonempty open set of the irreducible 𝓦, hence everywhere; as t is non-constant on fibre components, pr_u is constant on each fibre component, for all t. Contrapositive: a vertex non-constant along E_t for some t is non-constant along E_0.

**L2 (rigidity of every non-constant vertex).** Let E_0 be a piece with a Teichmüller vertex v in the orbifold sense of PR-E (H_0), and assume (O) of PR-E for (E_0, v). By Lemma R* (PR-E), there is an orbifold biholomorphism A_t: Ē_0 → Ē_t (punctures to punctures), homotopic to the transported marking, with f_v^t ∘ A_t = f_v^0. Let u be any vertex with f_u^0 non-constant. Then g_t := f_u^t ∘ A_t is holomorphic and (orbifold-)homotopic to g_0 on the punctured surface. g_0 has infinite monodromy (a finite-monodromy holomorphic map lifts, on a finite cover, to the bounded domain T_u, extends over the punctures, and is constant), so every g_t is non-constant; by Imayoshi–Shiga finiteness (as in PR-D Lemma R, Step 5) the g_t lie in a finite set of maps independent of t. Hence the puncture values f_u^t(p) lie in a finite set F(E_0,u) ⊂ M̄_u independent of t (and closure(π_u(E_t)) = closure(π_u(E_0)) by PR-D Step 6).

**Derivation of the problem's claim from MS6.**
1. By PR-A, t ↦ Y_t is holomorphic. If Y_t ∈ F for all t in a set T with an accumulation point in Δ, F finite, then some Y^{-1}(y) (y ∈ F) is a non-discrete analytic subset of Δ, so Y ≡ y, i.e. Y_t = Y_0 for all t.
2. Every piece E_0 at time 0 has a Teichmüller vertex: Lemma PA (PR-H §1) gives positive area at some vertex at a generic point, and Lemma T′ (PR-F, modulo its fact (F2)) turns positive area into a Teichmüller vertex in the orbifold sense. (For non-product strata, apply both on the lift.)
3. Assume (O) for these vertices (a separate open input, attacked elsewhere; automatic when there are no orbifold issues, and proved under pointwise conditions in another file). Then L2 applies to every piece. Let F be the finite set of n_i-pointed smooth curves isomorphic (after relabelling) to an irreducible component, with its special points, of some point of some F(E_0,u), over the finitely many pieces E_0 and vertices u non-constant on E_0.
4. MS6 gives, for t ∈ T, a piece E = E_t at time t, a vertex u with f_u non-constant on E_t and a puncture p with a component of f_u(p) ≅ Y_t. By (R2) and Lemma R0, E_t is the transport of some piece E_0; by L1, u is non-constant on E_0; by L2, f_u(p) ∈ F(E_0,u). So Y_t ∈ F for t ∈ T, and step 1 concludes.
5. Still needed outside MS6: (O) for the pieces used, (F2) of PR-F, and written checks of L1, L2. You do NOT need to prove these.

So MS6 is exactly the remaining geometric input: at time t, some copy of Y_t must sit inside a puncture value of a non-constant vertex of some boundary piece.

## Prior results (spliced verbatim)

### PR-D. Lemma R and Lemma R0 (from round5_q1, verbatim; Lemma R tacitly assumes the orbifold transport; PR-E makes it precise)
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


### PR-K. Theorem L: (O) under (★) and (★∞); Lemma N; the local models (cross), (fix), (ram); Lemma D (from round6_q7, verbatim)
# round6_q7: Lemma R without (O)

## Status and plan
**Lemma R without (O) is NOT settled in general here.** This file establishes the following.

1. **Lemma N (proved).** Under (R2), the normalised total space 𝓝 of 𝓔 = H(E_0 × Δ) has reduced fibre over t = 0. At every point, the germ of that fibre is unibranch, and its normalisation is the corresponding germ of Ẽ_0.
2. **Theorem L (proved; the globalisation in §3.3, Steps 1–3, is written at the level of a careful sketch).** (O) holds, and hence Lemma R holds via Lemma R* of PR-E, under a pointwise condition (★) at the interior points of Ẽ_0 and (★∞) at its punctures. Roughly, (★) says that every automorphism of the curve f_0(c) comes, modulo the generic automorphism group K, from the local group of O_0 at c. There is no hypothesis that 𝓝 is smooth: smoothness is *derived*.
   - In particular (O) holds automatically near every c with f_0(c) not an orbifold point. This proves the creation-excluded claim of PR-E §2.3, whose sketch there was flawed (see §4).
3. **Obstructions (proved).** If (★) fails, three explicit local models show that the germ of the Teichmüller disc at t = 0, together with a smooth, topologically trivial family of source curves, is compatible with a change of orbifold type. Any proof of (O), or of Lemma R, in the remaining cases must therefore be global.
   - This corrects the planner's claim that a pseudo-reflection of the isotropy group acting on T is needed. It is enough that the isotropy acts as a reflection on the lifted 2-dimensional family, which needs no reflection on T.
4. **Open.** Lemma R when (★) or (★∞) fails, i.e. in the three mechanisms of §4.

Conventions are those of PR-D/PR-E. Readings (R1) and (R2) are assumed throughout. K denotes the kernel of the action of Mod_{h,m} on T_{h,m} (the generic automorphisms; trivial except in the usual small cases). All isotropy groups below are taken modulo K, i.e. effectively.

## 1. Setting and notation

- E_0 ⊂ Δ_G, the vertex v with factor M := M_{h,m}, and T := T_{h,m}.
- (Ẽ_0, O_0), Λ_0, ρ_0 and F_0 : D → T are as in Lemma R:
  - F_0 is ρ_0-equivariant and is an isometry onto the Teichmüller disc 𝔇_0;
  - f_0 := π_v ∘ ν_0.
- 𝓔 := H(E_0 × Δ) ⊂ Δ_G × Δ. Near every point of E_0 × {0} this is a 2-dimensional analytic set:
  - it is locally a union of irreducible components of closure(𝒱) ∩ (Δ_G × Δ), by (R1) and Lemma R0's argument;
  - near points of E_0 this union is exactly 𝓔, because H is a homeomorphism onto closure(𝒱) mapping strata to strata.
- 𝓝 → 𝓔 is the normalisation, t : 𝓝 → Δ is the projection, and Φ := π_v ∘ (𝓝 → 𝓔) : 𝓝 → M is holomorphic.
- For c ∈ Ẽ_0:
  - c̃ ∈ D is a lift of c, and X̂ := F_0(c̃) ∈ 𝔇_0;
  - Stab(X̂) ⊂ Mod is the (finite) isotropy group of X̂, taken modulo K;
  - e_0(c) := |Stab_{Λ_0}(c̃)|. Since ρ_0 is injective (PR-E Step 1), this equals |ρ_0(Stab_{Λ_0}(c̃))|.
- **Orbifold chart.** U is a small Stab(X̂)-invariant ball around X̂ in T, and π : U → U/Stab(X̂) is an orbifold chart of M at X = f_0(c).
- L := the germ of 𝔇_0 at X̂, a smooth disc.

**Condition (★) at c.** The injection ρ_0 : Stab_{Λ_0}(c̃) → Stab(X̂) (modulo K) is surjective.

Equivalently, every automorphism of the curve X = f_0(c) is, modulo K, an affine automorphism of the generating differential lying in ρ_0(Λ_0). Consequences:
- Stab(X̂) ⊂ Stab(𝔇_0)·K.
- Stab(X̂)/K acts **faithfully** on L. Proof: if ρ_0(λ)k fixes L pointwise, then λ acts trivially on D, because F_0 is equivariant and injective. So λ = 1.
- (★) holds trivially at every c with f_0(c) not an orbifold point of M.

**Condition (★∞) at a puncture p of Ẽ_0.** Let Z ∈ ∂M̄ be the limit of f_0 at p. This limit exists: the closure of π_v(E_0) is analytic (PR-D Step 6), so f_0 extends holomorphically to the compactification. The condition is that Aut(Z) acts on the versal deformation space of Z through K, i.e. Aut(Z)/K = 1. Then M̄ is a manifold near Z, modulo K.

## 2. Lemma N (the zero fibre of 𝓝)

**Lemma N.** Assume (R2), and let n_0 ∈ 𝓝 with t(n_0) = 0. Then:
- (a) the divisor div(t) of 𝓝 is reduced near n_0;
- (b) the germ at n_0 of the reduced zero fibre (𝓝_0)_red is unibranch;
- (c) the normalisation of (𝓝_0, n_0) is the germ of Ẽ_0 at a unique point c. Conversely, every c ∈ Ẽ_0 arises from exactly one n_0.

*Proof.*

**Step 1 (generic points).** Let q ∈ E_0 be a manifold point of E_0 at which E_0 has a single branch. Choose:
- a small disc W ∋ q in E_0, with H(W × Δ') a neighbourhood of (q,0) in 𝓔.

H(W × Δ') is homeomorphic to W × Δ', a topological 4-manifold. So 𝓔 is locally irreducible at (q,0): the regular part of an analytic germ that is a topological manifold is connected near the point, because the singular set has real codimension ≥ 2. Hence the normalisation 𝓝 → 𝓔 is a homeomorphism near (q,0).

**Step 2 (reducedness, (a)).** Let Z_1 be a component of (𝓝_0)_red through n_0, and z ∈ Z_1 a generic point, at which 𝓝 and Z_1 are smooth. Then:
- In coordinates (σ, x) at z with Z_1 = {σ = 0}, we have t = (unit)·σ^μ.
- Hence, for small polydiscs N ∋ z and 0 < |t| < ε, the fibre N_t is a disjoint union of μ discs D_1, …, D_μ. Each of them passes through any prescribed smaller polydisc N'' ∋ z once t is small.

By Step 1, applied at q = image of z, the following holds. Choose a disc W' ∋ q and Δ'' with H(W' × Δ'') ⊂ N (identifying 𝓝 with 𝓔 near z). Then choose N'' with H^{-1}(N'') ⊂ W' × Δ''. This is possible because H is a homeomorphism.

Now H_t(W') is connected and contained in N_t = ⊔ D_j. It contains N''_t, which meets every D_j. Therefore μ = 1. So div(t) has multiplicity 1 along every component, and (a) follows.

The same argument shows that (𝓝_0)_red → E_0 is generically injective. If two points of 𝓝 lay over a generic point q, then 𝓔 would not be locally irreducible at (q,0).

**Step 3 (unibranch, (b)).** Since 𝓝 is normal, the germ (𝓝, n_0) is irreducible, so 𝓝 \ {t = 0} is connected near n_0.

The Milnor fibre F_t := 𝓝_t ∩ B (B a Milnor ball) is connected. Indeed, its components are permuted transitively by the monodromy. If there were d ≥ 2 of them, then "which component" would define a d-valued function. Normality of 𝓝 would make this function single-valued holomorphic on a d-fold cyclic cover, giving g with t = (unit)·g^d. That contradicts (a). (This is the standard argument; I cite the conclusion — a function with reduced divisor on a normal surface germ has connected Milnor fibre — from memory.)

Now suppose (𝓝_0)_red had k ≥ 2 branches at n_0. By Step 2 they map to k distinct branches W_1, …, W_k of E_0 at q := image of n_0. Let W be the union of all branches of E_0 at q. Then:
- W \ {q} = ⊔ (W_i \ {q}) is a disjoint union of open sets, so H_t(W) \ {H_t(q)} = ⊔ H_t(W_i \ {q}) is a disjoint union of open sets of 𝓔_t.
- For t small, H_t(W) contains F_t ∩ N'' (as in Step 2), and F_t ∩ N'' minus one point is connected.
- Each H_t(W_i \ {q}) with i ≤ k meets F_t ∩ N''. Indeed, points of W_i near q are sent near n_0 by H_t, by continuity of H at (q,0), and into the local piece of 𝓔 normalised by the germ at n_0. This is because H(W_i^∘ × Δ) is a connected subset of the locally irreducible part of 𝓔.

So a connected set meets k ≥ 2 disjoint open sets covering it. This is a contradiction, so k = 1 and (b) holds.

**Step 4 ((c)).** (c) follows from (b) and generic injectivity: the normalisation of (𝓝_0)_red is the normalisation of E_0, namely Ẽ_0. ∎

*Remark.* This is the precise form of the Milnor-fibre / topological-triviality input that Route 1 asked for. Note that it does **not** say that 𝓝 is smooth or that the zero fibre of 𝓝 is smooth. Smoothness is obtained in §3, and only under (★).

## 3. Theorem L: (★) and (★∞) imply (O)

### 3.1 Local proposition at an interior point

**Proposition L1.** Let c ∈ Ẽ_0 satisfy (★), let n_0 ∈ 𝓝 be the point from Lemma N(c), and put G := Stab(X̂)/K, of order e_0(c). Then there are:
- a smooth 2-dimensional germ (𝓟, p_0) with coordinates (s, t), on which G acts by g·(s,t) = (χ(g)s, t) with χ : G → ℂ^* injective;
- a G-equivariant holomorphic map Ψ : 𝓟 → U;

such that 𝓝 ≅ 𝓟/G near n_0, compatibly with t, and π∘Ψ = Φ under this identification. Consequently:
- 𝓝 is smooth at n_0 and t is a submersion there, with coordinates (s^{e_0}, t);
- for every small t, the minimal orbifold structure O_t^min has, in the neighbourhood {|s| < r} of n_0 in 𝓝_t, exactly one cone point, of order e_0(c), at s = 0;
- the local lifts Ψ|_{𝓟_t} of Φ|_{𝓝_t} depend holomorphically on t.

*Proof.*

**Step 1 (the fibre product).** Put 𝓠 := 𝓝 ×_{U/G} U near (n_0, X̂). The only point over n_0 is (n_0, X̂), since π^{-1}(X) = {X̂}. Let 𝓟^ν be the normalisation of 𝓠.

The generic isotropy of the lifted surface Ψ(𝓟^ν) is trivial: if g ≠ 1 fixed it pointwise, then g would fix its zero fibre, which is L (Step 2), pointwise, contradicting faithfulness under (★). So 𝓠 → 𝓝 is generically a G-torsor, of degree |G| = e_0, and G permutes the components of 𝓟^ν transitively.

**Step 2 (the zero fibre of 𝓟^ν).** Choose a coordinate z on L in which G acts by z ↦ χ(g)z. Then π(L) ≅ L/G has coarse coordinate z^{e_0}. Let w be a coordinate of Ẽ_0 at c, which by Lemma N(c) is the normalisation parameter of (𝓝_0, n_0).

By (★), F_0 near c̃ is the orbifold chart of O_0 at c followed by a biholomorphism onto L, and the stabiliser of c̃ is all of G. So f_0 is a coarse local isomorphism B_0 → L/G, and we may take z^{e_0} = w on the lift. Under (★), π^{-1}(f_0(B_0)) = ∪_g gL = L. Hence the zero fibre of 𝓠, pulled back to the normalisation of 𝓝_0, is {(w, z) : z^{e_0} = w}: **one** smooth branch b, mapping with degree e_0 to the normalisation of 𝓝_0.

**Step 3 (multiplicity).** Let p : 𝓟^ν → 𝓝 be the projection, and write p^* div(t) = Σ m_i Z'_i. By the projection formula, p_*(p^* div t) = e_0 · div(t), and div(t) = 1·(𝓝_0) near n_0 by Lemma N(a). Each Z'_i lies over the single branch b, so deg(Z'_i → 𝓝_0) ≥ e_0. Hence Σ m_i deg(Z'_i → 𝓝_0) = e_0 forces:
- there is exactly one Z'_1 =: Z', with m_1 = 1 and deg = e_0;
- in particular 𝓟^ν is irreducible near the point p_0 over (n_0, X̂), and G_k = G.

**Step 4 (smoothness).** Z' is unibranch, since its normalisation is the single branch b ≅ L. The function z∘Ψ restricted to Z' has order 1 at p_0 on that normalisation. A unibranch curve germ carrying a function of order 1 has multiplicity 1, so Z' is smooth at p_0.

𝓟^ν is a normal surface, so it is Cohen–Macaulay. Hence 𝒪/(t) has no embedded points. It is generically reduced along Z', because m = 1, so 𝒪_{𝓟^ν}/(t) = 𝒪_{Z'}, a regular 1-dimensional ring. Therefore 𝒪_{𝓟^ν, p_0} is regular of dimension 2 and t is part of a coordinate system. Put 𝓟 := 𝓟^ν.

**Step 5 (linear coordinates).** t is G-invariant. At p_0, T_{p_0}Z' = ker dt, and G acts on it by χ, since Z' ≅ L equivariantly. Take any function s_0 with ds_0|_{TZ'} ≠ 0, and put
  s := |G|^{-1} Σ_g χ(g)^{-1} (s_0∘g).
Then s∘g = χ(g)s, and ds|_{TZ'} = ds_0|_{TZ'} ≠ 0. So (s, t) are coordinates and g(s,t) = (χ(g)s, t). χ is injective because G acts faithfully on L.

**Step 6 (consequences).** 𝓝 is normal and 𝓟 → 𝓝 is generically Galois with group G. Hence 𝓝 = 𝓟/G, which is smooth with coordinates (s^{e_0}, t).

For fixed t, 𝓟_t = {t = const} is a disc on which G acts by rotations about s = 0 alone. Every nonidentity element has the single fixed point s = 0. Two fibres 𝓟_t lying over the same 𝓝_t cannot be distinct branches, since 𝓟_t is connected. So:
- the branch stabiliser of the lift Ψ|_{𝓟_t} of Φ|_{𝓝_t} is G at the image of s = 0, and is trivial elsewhere;
- this is exactly the definition of the cone orders of O_t^min (PR-E §2.3).

Ψ is holomorphic in (s, t), which gives the last claim. ∎

**Corollary L2 (creation is excluded at points that are not orbifold points).** If f_0(c) is not an orbifold point of M, then near n_0 the surface 𝓝 is smooth, t is a submersion, and O_t^min has no cone point near n_0 for small t. (This is the case G = 1 of L1.)

### 3.2 Punctures

**Proposition L3.** Let p be a puncture of Ẽ_0 satisfying (★∞). Then there are a neighbourhood 𝒱_p of the end p of Ẽ_0, and ε > 0, such that for |t| < ε the part of Ẽ_t corresponding to 𝒱_p, under the transport of (R2) and Ĥ_t, contains no cone point of O_t^min.

*Proof.*
- By (★∞) there is a neighbourhood Ω of Z in M̄ such that Ω ∩ M contains no orbifold points (modulo K).
- The compactified maps f̄_t are restrictions of a single holomorphic, hence continuous, map on the normalisation of the analytic family 𝓦^{(a)} of Lemma R0 (PR-D), composed with pr_v. This is the place where (R1) enters.
- So there are a neighbourhood of the point over (p, 0) in that normalisation, mapped into Ω, and ε > 0 such that its fibres over |t| < ε contain the transported end.
- Points mapped into Ω ∩ M are not orbifold points, so they are not cone points. ∎

### 3.3 Theorem L

**Theorem L.** Assume (R1) and (R2), and the hypotheses of Lemma R. Assume (★) at every c ∈ Ẽ_0 and (★∞) at every puncture of Ẽ_0. Then (O) of PR-E holds for |t| small. Consequently, by Lemma R* of PR-E together with the analytic-continuation argument below, closure(π_v(E_t)) = closure(π_v(E_0)) for all t ∈ Δ.

*Proof.*

**Step 1 ((O-a) and (O-b)).**
- Cover a compact core 𝒦 ⊂ Ẽ_0, the complement of small end neighbourhoods 𝒱_p as in L3, by finitely many neighbourhoods given by L1 and L2.
- By L1 and L2, 𝓝 is smooth with t a submersion along 𝒦 × {0}. So by Ehresmann the fibres over |t| < ε form a smooth trivial family over 𝒦.
- By L1, the cone points of O_t^min in this family are exactly one point near each cone point c of O_0, of the same order e_0(c). By L3, there are none near the ends.
- The local lifts vary continuously (L1), which gives (O-b).

**Step 2 (the end neighbourhoods).** These are punctured discs for all small t: by (R2) they are transported by H, and they do not touch the core.

**Step 3 (θ_t and ρ_t).** Combining the Ehresmann trivialisation with these discs gives a homeomorphism Ẽ_0 → Ẽ_t that:
- preserves cone points with their orders, and cusps;
- is isotopic to Ĥ_t, since both depend continuously on t and agree with the identity at t = 0.

This yields θ_t. Then t ↦ ρ_t∘θ_t^{-1} is continuous into the discrete set Hom(Λ_0, Mod) (PR-E §2.3), hence constant. This is (O).

**Step 4 (Lemma R*).** Lemma R* (PR-E) gives π_v(E_t) = π_v(E_0) for |t| < ε.

**Step 5 (all t).** Let 𝒲 be the irreducible 2-dimensional analytic family of Lemma R0, and C̄_0 := closure(π_v(E_0)) ⊂ M̄. The set 𝒲 ∩ (pr_v^{-1}(C̄_0)) is analytic in 𝒲 and contains all fibres over |t| < ε. Hence it equals 𝒲. (Otherwise it would have dimension ≤ 1, and its fibre-contained components lie over a discrete set of t.) So π_v(E_t) ⊂ C̄_0 for all t. Then equality of closures follows from irreducibility and non-constancy, as in PR-D Step 6. ∎

*Scope of Theorem L.*
- It covers every E_0 whose Teichmüller curve meets the orbifold locus of M only at points X with Aut(X)/K = ρ_0(local group). This holds, for example, when E_0 → C_0 is birational, Λ_0 is the full Veech group modulo K, and every automorphism of every curve on the Teichmüller disc preserves the disc.
- It also covers the case where C_0 avoids the orbifold locus altogether (except through K) and its cusps are curves without extra automorphisms.
- It does **not** cover Teichmüller curves lying inside an orbifold locus, e.g. hyperelliptic Teichmüller curves in M_3, for which (★) fails at every point.

## 4. When (★) fails: three local models (proved), so any further proof must be global

(★) can fail at c in exactly three ways. Write G := Stab(X̂)/K and H_c := ρ_0(Stab_{Λ_0}(c̃)) ⊂ G ∩ Stab(𝔇_0). Then (★) fails iff one of the following holds:
- **(cross)** G ⊄ Stab(𝔇_0);
- **(fix)** some g ∈ G \ {1} fixes 𝔇_0 pointwise;
- **(ram)** G ⊂ Stab(𝔇_0) acts faithfully on L, but H_c ⊊ G. Equivalently, Ẽ_0 → C_0 has coarse local degree r = |G|/e_0(c) > 1 at c.

For each of them there is an explicit germ with the following properties:
- a family 𝓝 ≅ ℂ² with t a coordinate, so the source family is smooth and trivial, and Lemma N holds;
- a holomorphic Φ : 𝓝 → U/G;
- at t = 0, Φ_0 lifts isometrically onto the germ L of the Teichmüller disc, with the orbifold structure prescribed by O_0;
- O_t^min for t ≠ 0 has a **different type** near c.

Write X̂ = 0 in a linear chart of U where G acts linearly (Cartan). Let δ(z) parametrise L.

**(cross).** Take g ∈ G of order 2 with gL ≠ L and T_0(gL) ≠ T_0L. Such g exists whenever g^*q ∉ ℂ^* q for the generating q, by genericity of the tangent directions.
- Ψ(z,w) := δ(z) + gδ(w) is an immersion at 0, and g(Ψ(z,w)) = Ψ(w,z).
- Let 𝓝 be the quotient by the swap, with coordinates (σ, t) = (z+w, zw), and Φ := π∘Ψ. This descends to 𝓝.
- t = 0: the fibre {zw = 0}/swap ≅ L, with lift z ↦ δ(z) and no cone point at c.
- t ≠ 0: the lifted fibre {zw = t} is connected and g-invariant, with fixed points z = w = ±√t. So there are **two cone points of order 2** (creation).
- The (ℤ/2)² splitting model of the task is the analogous construction with e_0(c) = 2.

**(fix).** Take a ∈ G of order 2 with L ⊂ Fix(a), and a normal eigen-direction x_2 with eigenvalue −1, so a = diag(1, −1, …) and L = {x_2 = 0}.
- Put Φ(s,t) := π(s, √(ts), 0, …). The coarse coordinates are (x_1, x_2², …), so this is the holomorphic map (s, ts, 0, …).
- t = 0: the lift s ↦ (s, 0) ∈ L. Here a acts trivially on L, so there is no cone point.
- t ≠ 0: the lift x_2 = √(ts) branches at s = 0, giving **one cone point of order 2** (creation).
- This occurs, for example, along every hyperelliptic Teichmüller curve in M_3 (with ι a reflection on T_3). However, there are no marked points there, so it is only an analogue of the boundary-factor situation.

**(ram).** Take g ∈ G ∩ Stab(L) of order 2 acting on L by −1, with a g-fixed direction x_2 transverse to L, so g = diag(−1, 1, …) and L = x_1-axis. This needs dim Fix(g) ≥ 1.
- Put Φ(w,t) := (w² − t, t, 0, …) in coarse coordinates (x_1², x_2, …).
- t = 0: the lift w ↦ (w, 0) ∈ L is isometric, and c is regular in O_0 with e_0 = 1. Here f_0 is coarsely 2:1 onto L/G, so this is an orbifold-unramified point over an order-2 orbifold point of C_0.
- t ≠ 0: the lift x_1 = √(w² − t) branches at w = ±√t, giving **two cone points of order 2**, while f_t acquires an ordinary ramification point at w = 0. The images C_t are the g-invariant discs {x_2 = t} through the orbifold points (0, t).

**Consequences.**
1. In each model, the data at t = 0 are only the germ of 𝔇_0 at X̂ and the local orbifold structure. Lemma N and the conclusion "𝓝 smooth, t submersive" also hold. So (O-a) cannot be derived from local information at c, and Route 1 alone cannot prove (O) without (★).
2. **Correction to the planner.** In (cross) and (ram), g need not be a pseudo-reflection on T. It acts as a reflection on the 2-dimensional lifted family (the swap, respectively the folding), which is automatic. So "pseudo-reflection in the isotropy group of M" is not a necessary condition for splitting or creation.
3. **Correction to PR-E §2.3.** The sketch "a g-invariant branch at time t converges to a g-invariant branch at time 0" is false in (cross): the g-invariant branch {zw = t} converges to the union of two branches. Corollary L2 replaces that sketch by a proof in the case where f_0(c) is not an orbifold point. In that case all three mechanisms are absent.
4. In all three models the orbifold Euler characteristic of O_t differs from that of O_0 by −1 or −1/2. So the length comparison ℓ_{O_t} ≥ ℓ_{O_0} of PR-E Step 3 cannot conclude via Thurston. Larger orbifolds have larger lengths, and the inequality is then consistent.

## 5. A global tool for the (fix) mechanism (proved)

**Lemma D (negative normal degree pins the family).** Let 𝒟 be an effective ℚ-Cartier divisor on the coarse space of M̄_v, with support B ⊇ C̄_0 := closure(π_v(E_0)) and deg(f̄_0^* 𝒟) < 0, where f̄_0 is the compactified map from the compactification of Ẽ_0. Then π_v(E_t) ⊂ B for all t ∈ Δ.

*Proof.*
- The compactified maps f̄_t are the fibres of the proper analytic family 𝒲^{(a)} → Δ of Lemma R0, composed with pr_v. The fibre cycles of a proper family over a disc are homologous, so deg f̄_t^*𝒟 = ⟨[pr_{v*} 𝒲_t], c_1(𝒟)⟩ is independent of t.
- If π_v(E_t) ⊄ B, then f̄_t^*𝒟 is an effective ℚ-divisor on a curve, so its degree is ≥ 0. That is a contradiction.
- So π_v(E_t) ⊂ B for every t. ∎

*Use.* In mechanism (fix), with B the closure of the image of Fix(a), negative normal degree confines the whole family to B. One can then hope to rerun §3 inside the smaller orbifold B, which is uniformised by T(X/a) ⊂ T. There a no longer obstructs, because it acts trivially there. I have not carried this out.

*Heuristic illustration (cited from memory, not used).* For M_3 (no marked points), use:
- [H̄yp] = 9λ − δ_0 − 3δ_1;
- slope 28/3 for Teichmüller curves in the hyperelliptic components, from Chen–Möller / Eskin–Kontsevich–Zorich;
- δ_1·C = 0, since cylinder cores are non-separating.

These give [H̄yp]·C = −λ·C/3 < 0, so Lemma D would apply. The boundary factors M_{3,m} with m ≥ 1 are a different situation.

## 6. Summary: proved, conditional, open

**Proved.**
- Lemma N.
- Proposition L1 (local transport under (★)) and Corollary L2 (no creation at points that are not orbifold points).
- Proposition L3 (no cone points near a cusp under (★∞)).
- Theorem L: (★) everywhere and (★∞) at all punctures ⇒ (O) ⇒ the conclusion of Lemma R for all t. The globalisation steps are written as a careful sketch. The cited inputs are the Milnor-fibre connectivity (from memory) plus those of PR-E (Royden, Bers, Thurston, Selberg).
- The three local models of §4, showing that without (★) local analysis cannot give (O).
- Lemma D.

**Not proved / open.**
- (Q1) Lemma R when (★) fails at some c: mechanisms (cross), (fix) and (ram). It is unknown whether any of the local models globalises to a deformation f_t of an orbifold-unramified cover of a Teichmüller curve with non-constant image. A counterexample to Lemma R would require exactly such a global deformation in which the orbifold type changes. Lemma R* rules out all deformations that preserve the type.
- (Q2) Lemma R when (★∞) fails, i.e. some cusp of the Teichmüller curve goes to a stable curve with extra automorphisms. Here cone points can enter from the cusp. The local model is: puncture section {s^e = t} and fixed curve {s = 0} in 𝓟. I have not analysed this.
- (Q3) In mechanism (fix), the sign of the normal degree of the fixed locus along C_0. Lemma D handles only the negative case.

So the chain of the run (MS5 + Lemma R ⇒ the problem's claim) is now complete **only** for Teichmüller pieces satisfying (★) and (★∞), together with the previously known case where M_u has no orbifold points (which is the special case of Theorem L with all groups trivial).



## Reminder
- Begin with a plan/status line; end with proved / not proved / open.
- If you prove only the weaker L2 conclusion (finiteness of puncture values), say so; that suffices for the chain.
