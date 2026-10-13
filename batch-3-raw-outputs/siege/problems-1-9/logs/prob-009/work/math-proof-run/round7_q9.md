kind: attempt
Open question attempted: ledger entry 53 — the chain lemmas L1 (constancy persists) and L2 (rigidity of every non-constant vertex) on which the run's derivation of the problem's claim from its missing statement MS6 rests.

## Task
Prove L1 and L2 (stated below with proof sketches) completely and rigorously, or find the flaw and give the strongest correct replacement. Check in particular:
- L1: that the lifted family 𝓦 (Lemma R0, PR-D) is proper over Δ with fibre over 0 contained in the closure of the lift of E_0 (including for non-product strata, where ξ_G is finite but not injective, so "the lift" may have several components permuted by a finite group); the existence of an affine (Stein) neighbourhood of a point in the coarse space M_u; the rank argument extending constancy from |t| < ε to all t (irreducibility of 𝓦; fibre components that do not dominate; points of 𝓦_t over deeper strata).
- L2: the orbifold bookkeeping; whether Lemma R*'s biholomorphism A_t extends to the compactifications sending punctures to punctures; that g_t = f_u^t ∘ A_t is homotopic to g_0 in the orbifold sense (via (R2) and A_t ≃ transported marking); the claim that a non-constant holomorphic map from a finite-type orbifold curve to M_u has infinite monodromy; the exact hypotheses of the Imayoshi–Shiga finiteness theorem (or Arakelov–Parshin / McMullen alternatives) for maps into M_{h,m} with marked points, and whether they hold here; and the conclusion that puncture values f_u^t(p) lie in a finite set independent of t.
- Whether the chain's derivation (below) of the problem's claim from MS6, L1, L2, (O) and Lemma T′ is correct; if any step fails, say precisely which and why.

Do not try to prove MS6 or (O) here.

## Readings
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G. H_t = H(·,t).

## The statement (MS6)

**Setting.** g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric (every Teichmüller disc tangent to V_0 at a point of V_0 lies in V_0). V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (R1) and (R2). Δ_Γ ≅ ∏_j M_{g_j,n_j} is a boundary stratum of product type (the gluing map is bijective onto Δ_Γ); ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1 and π_i(∂V_t) = {Y_t} for all t, for a fixed index i with dim M_{g_i,n_i} > 0. (V_t is NOT assumed totally geodesic for t ≠ 0.)

**Definitions.**
- For a stable graph G with vertices w (genus g_w, n_w special points), ξ̄_G: ∏_w M̄_w → M̄_g is the gluing map (finite), ξ_G its restriction to ∏_w M_w, with image Δ_G. G need NOT be of product type here.
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w, for some G.
- Let Ē be the normalization of the closure of E in ∏_w M̄_w (a compact Riemann surface, possibly after normalizing), ν: Ē → ∏_w M̄_w the map. A *puncture* of E is a point p ∈ Ē with ν(p) ∉ E (finitely many).
- For a vertex u of G, f_u := pr_u ∘ ν : Ē → M̄_u = M̄_{g_u,n_u}.

**Statement (MS6).** There is a set T ⊂ Δ having an accumulation point in Δ such that for every t ∈ T there exist a piece E at time t (for some stable graph G), a vertex u of G with f_u non-constant, and a puncture p of E, such that the stable curve f_u(p) ∈ M̄_u has an irreducible component which, with its special points (preimages of nodes and marked points, in some order), is isomorphic to Y_t as an n_i-pointed curve.

Typical ways it can hold (for orientation only): at a point Q ∈ closure(V_t) \ V_t, a boundary branch of closure(V_t) along which some node at a component Q_x ≅ Y_t of Q is smoothed (a "merge"; then the vertex u containing x has a nodal limit containing Q_x, and u is non-constant by Lemma C2 of PR-C) — this includes merges along ∂V_t itself where Q_x is a *twin* copy of Y_t (as in the quintic example of PR-I); or a branch along which the vertex carrying a Y_t-copy moves non-constantly, with limit Y_t at a puncture of that piece. ANY component isomorphic to Y_t counts: no tracking of "the" Y-component from t = 0 is required.

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

### PR-A. Holomorphy of Y_t (from round4_q3, verbatim)
## (A) Lemma 1 (holomorphy of Y_t), proved from (R1) and (R2)

**Lemma 1.** t -> Y_t is a holomorphic map Delta -> M_{g_i,n_i}.

*Proof.*
1. **Continuity.** Fix p in dV_0. By (R2), Phi(p,t) lies in dV_t for every t, so Y_t = pi_i(Phi(p,t)). This is continuous in t because Phi is continuous.
2. **The analytic set A.** Let A = closure(calV) cap (Delta_Gamma x Delta). By (R1), A is a closed analytic subset of the complex manifold Delta_Gamma x Delta. By (R2), A is homeomorphic to dV_0 x Delta. The set dV_0 is a 1-dimensional analytic set, so every nonempty open subset of A has real topological dimension 4. Hence A has pure complex dimension 2.
3. **The projection to Delta.** Each fibre A_t = dV_t has dimension 1. So no irreducible component of A lies in a fibre of phi : A -> Delta.
4. **The bad set.** Let B be the union of Sing(A) and the critical set of phi restricted to Reg(A). Then B is a closed analytic subset of dimension at most 1.
   - It is a proper subset in each component. Otherwise phi would be locally constant on an open subset of Reg(A), and that would force a component into a fibre.
   - The 1-dimensional irreducible components of B form a locally finite family. Those contained in fibres of phi lie over a discrete set D in Delta.
   - For t not in D, the fibre A_t (dimension 1) is not contained in B. Indeed, the intersection of A_t with B is a union of fibre-contained components of B, which do not occur over such t, and of finitely many points locally.
5. **Local sections.** For t_0 not in D, pick a in A_{t_0} \ B. Near a, A is a manifold and phi is a submersion. So there is a holomorphic local section s of phi with s(t_0) = a, and Y_t = pi_i(s(t)) is holomorphic near t_0.
6. **Conclusion.** Y is continuous on Delta and holomorphic on Delta \ D with D discrete. By the removable singularity theorem (in local coordinates of M_{g_i,n_i}, which is an orbifold, so work in a local manifold chart / finite cover near Y_{t_0}), Y is holomorphic on Delta. ∎

**Corollary.** MS4 is equivalent to "Y_t = Y_0 for all t in some neighbourhood of 0", by the identity theorem.

---



### PR-C. Local structure at a cusp; merge property (from round4_q7, verbatim)
## C. Local structure at a cusp of ∂V_t (partial (H1))

Fix t and a point P ∈ closure(∂V_t) \ ∂V_t. Then P lies in some Δ_{G'}, where G' degenerates Γ: it has edge set E(Γ) ∪ X with X ≠ ∅, and vertex i is intact. Let S be the germ of closure(V_t) at P. It is pure 2-dimensional, because V_t is dense in it.

**Lemma C1.** S has a 1-dimensional boundary branch b through P, other than the branches of closure(∂V_t), such that some edge e ∈ X is pinched along b.

*Proof.*
1. closure(∂V_t) \ ∂V_t is a proper analytic subset of a 1-dimensional analytic set, hence discrete.
2. So a branch β of closure(∂V_t) at P satisfies β \ {P} ⊂ Δ_Γ. Let X_S be an irreducible component of S containing β.
3. Take e ∈ X. On β \ {P} exactly the edges of Γ are pinched, so s_e ≠ 0 there. Hence s_e|_{X_S} is a non-unit that is not identically zero on the irreducible 2-dimensional germ X_S.
4. Its zero set is therefore of pure dimension 1 (Krull's principal ideal theorem / Weierstrass preparation; standard).
5. That zero set meets β only at P. So it contains a branch b ≠ β, and b lies in the boundary with s_e ≡ 0 on b. ∎

**Definition (merge property).** Let b be a boundary branch at P, and let G_b be the dual graph of a generic point of b. Equivalently, G_b is G' with the edges unpinched along b contracted. Let v be the vertex of G_b containing vertex i of G'. Say b has the *merge property* if v is strictly bigger than {i}, that is, some edge of G' incident to i is unpinched along b.

**Lemma C2 (merging forces variation).** Suppose b has the merge property. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing b. Then π_v(E) is not a point. Moreover, the limit Q of π_v along b at P is a boundary point of M̄_{h,m}, where M_{h,m} is the factor of vertex v. The dual graph of Q is the subgraph of G' contracted into v, and its component at vertex i is Y_t.

*Proof.*
1. As a point of b tends to P, the edges of G' inside v get pinched. So π_v tends to the stable curve Q described in the statement. Q lies in ∂M̄_{h,m}, because v contains at least one such edge.
2. Its component at vertex i is the component of P at vertex i, which is Y_t.
3. If π_v were constant on E, equal to some Z ∈ M_{h,m}, then its limit along b would be Z ∈ M_{h,m}, not a boundary point. Contradiction. ∎

**What C1 does not give.** C1 produces a branch b on which an extra edge e is pinched. It does not control the edges at vertex i. The merge property fails exactly when every edge of G' incident to i is pinched along b. Lemma C1 cannot exclude this. Example: in local coordinates (u,v) on a smooth germ, s_γ = uv and s_e = v, with β = {u=0} and b = {v=0} ⊂ Δ_{G'}. Nothing in (i), (ii), (R1) or (R2) rules out a surface whose boundary branches all look like this at every cusp of ∂V_0; compare Observation 4 of P-a. Define:

**(C-merge)** There is a cusp P_0 of ∂V_0 and a boundary branch b of closure(V_0) at P_0 with the merge property.

(C-merge) is the precise residue of (H1). It is not proved in general.


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


## Reminder
- Begin with a plan/status line; end with proved / not proved / open, and a corrected statement of L1/L2 if needed.
