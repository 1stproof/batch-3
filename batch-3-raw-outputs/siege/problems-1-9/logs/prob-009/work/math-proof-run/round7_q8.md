kind: attempt
Open question attempted: the run's missing statement MS6 (ledger entry 52): at time t, for t in a set accumulating in Δ, some component isomorphic to Y_t lies inside a puncture value of a non-constant vertex of some boundary piece of closure(V_t).

## Task
Give a complete proof of exactly the statement MS6 below, or an explicit counterexample to it (a concrete V_0 and family V_t satisfying every hypothesis, including smoothness and total geodesy of V_0 and readings (R1), (R2), for which no t outside a discrete set admits the required configuration — each check written out).

A proof of the statement for only some of the cases it covers does NOT answer the question: this includes proofs for a sub-class of surfaces V_0 (for example covering constructions), for some strata Γ or factors i only, under extra hypotheses on the boundary configuration (such as "no other boundary near a cusp", or absence of automorphisms/twins), or only at t = 0. If that is all you find, report it, clearly labelled as partial, and say exactly which case remains.

Write any proof in full. Cite literature theorems by name with their exact hypotheses and check those hypotheses where you use them. The prior results below may be used; if you rely on one, re-check the steps you use. If you find that the chain's derivation of the problem's claim from MS6 (section "How the statement is used") is flawed — in particular the lemmas L1, L2 — say so explicitly and precisely.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G (including the open stratum M_g). Write H_t = H(·,t); one may assume H_0 = id. (This is our formalisation of "smoothly trivial" together with (i), (ii).)

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

## Prior results (spliced verbatim from earlier answer files)
All assume readings (R1) and (R2) (stated above). Results marked as cited from memory are not verified; re-check anything you use. Labels inside them refer to each other as follows: PR-1 = holomorphy (PR-A); Lemma B′ of PR-3 = PR-B; Lemma C1/C2 of PR-3 = PR-C; PR-D = Lemma R/R0 (round5_q1); PR-E = Lemma R* (round5_q4); PR-F = Lemma G, T′, V (round5_q5); PR-G = an earlier file on the twin issue in cyclic covers (not reproduced; its point is that automorphisms of a boundary point can swap a merged copy of Y_0 with an unmerged twin). 'P-b Lemma 1' says the closure of ∂V_t = {Y_t} × C_t in deeper strata is {Y_t} × closure(C_t), so every point of closure(∂V_t) has a smooth component ≅ Y_t at vertex i. Earlier files call the old missing statement 'MS5' or '(T0)': it asked, at t = 0, for a point of closure(∂V_0) where EVERY copy of Y_0 in EVERY lift is merged into a Teichmüller vertex; it is now known to fail for a (singular) totally geodesic surface (PR-I) and is no longer the target.

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



### PR-B. Incidence transport (from round4_q7, verbatim)
## B. Under (R2), incidences are transported automatically

**Lemma B′.** Let H : closure(V_0) × Δ → closure(𝒱) be the stratified homeomorphism of (R2). Let E_0 be a 1-dimensional piece of closure(V_0) ∩ Δ_{G''}, and let P_0 ∈ closure(E_0) ∩ closure(∂V_0) ∩ Δ_{G'}. Put E_t := H(E_0 × {t}) and P_t := H(P_0, t). Then:
- E_t ⊂ Δ_{G''};
- P_t ∈ closure(E_t) ∩ closure(∂V_t) ∩ Δ_{G'};
- t ↦ P_t is continuous.

*Proof.*
1. H is a homeomorphism over Δ that maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G.
2. A homeomorphism commutes with closures. Hence H(closure(E_0) × {t}) = closure(E_t), and H(closure(∂V_0) × {t}) = closure(∂V_t).
3. Continuity of P_t follows from continuity of H. ∎

So neither hypothesis (ii) nor the "isolated point" condition in (H1) is needed under (R2). Under a weaker reading one would fall back on (ii) as in P-d. By P-b, the component of P_t at the vertex i of G' is Y_t: the vertex i stays intact because π_i is constant along ∂V_t.

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


### PR-F. Lemma G, Lemma T′ (positive area forces a Teichmüller curve), Lemma V (from round5_q5, verbatim, sections 0–3; its fact (F2) is only sketched there)
## 0. Conventions and cited facts

- Work on a fine level cover where needed (M_g[m], m >= 3, and the corresponding covers of the boundary factors) so that "point of moduli space" can be replaced by "point of Teichmüller space modulo a torsion-free group"; orbifold points of curves below are handled by this. I do not re-verify this standard reduction.
- **Totally geodesic.** V_0 is totally geodesic means: for every X in V_0 and every complex tangent line L in T_X V_0, the Teichmüller disc through X tangent to L is contained in V_0. Write Q_V(X) for the set of nonzero q in Q(X) whose Teichmüller disc lies in V_0. It is nonempty, invariant under multiplication by C*, and for g in SL(2,R) the underlying surface of g.(X,q) lies in V_0 and g.q lies in Q_V of it. Call (X,q) with q in Q_V(X) a *generating pair*.
- **Teichmüller discs.** For q a nonzero integrable holomorphic quadratic differential on a finite-type surface (simple poles allowed at punctures), the map SO(2)\SL(2,R) = H -> T, g -> [g.(X,q)] is a holomorphic isometric embedding (Teichmüller metric restricted = hyperbolic metric of curvature -4); in particular it is non-constant and injective. (Classical: Teichmüller, Royden, Kra.)
- **(Ext)** Maskit: for a simple closed curve gamma on a hyperbolic surface, l(gamma)/pi <= Ext(gamma) <= (l(gamma)/2) e^{l(gamma)/2}. Under a K-qc map, Ext changes by a factor in [1/K, K].
- **(Nbhd)** (augmented Teichmüller space; Abikoff, Bers; cited from memory). If X_n -> P in Mbar_g and P has dual graph G with multicurve gamma_G (in a marking coming from the convergence), then l_{X_n}(gamma_e) -> 0 for the curves of gamma_G, and there is eps > 0 with l_{X_n}(beta) >= eps for all other essential simple closed curves beta and n large. Conversely, if Y_n -> P' and a multicurve has lengths -> 0 while every other simple closed curve has length bounded below, then the dual graph of P' is the dual graph of that multicurve.
- **(F) Limits of differentials on components** (standard compactness of stable/multi-scale differentials; BCGGM for abelian, and the quadratic version / canonical double cover; cited from memory, I state only what I use). Let X_n -> P in Delta_G, q_n in Q(X_n) nonzero, and v a vertex of G with component Y_v (punctured at the node-branches). After passing to a subsequence there are s_n in C^* and a nonzero meromorphic quadratic differential eta_v on Y_v, holomorphic off the punctures, together with exhausting compact sets K of Y_v and conformal embeddings iota_{n,K}: K -> X_n (in the plumbing description of a neighbourhood of P), such that iota_{n,K}^* q_n / s_n -> eta_v uniformly on K. One can take |s_n| non-increasing in "level"; I only use: **v carries positive area** (for this sequence) if one can take s_n = 1 after normalising Area(q_n) = 1; then eta_v is integrable (finite area <= 1), has at most simple poles at punctures, and Y_v is not of type (0,3) (a finite-area quadratic differential on a thrice-punctured sphere would have total degree >= -3 > -4).
- **(F2) Affine transport of a positive-area component** (sketch-level; it follows from (F) by taking limits of the Teichmüller maps; I flag it as not fully written out). In the situation of (F) with v of positive area and s_n = 1 (after a rotation absorbed into eta_v), let g in SL(2,R) and let P_g be any limit point of the underlying surfaces of g.(X_n,q_n). Then the v-component of P_g, as a pointed curve with the marking induced from the Teichmüller maps X_n -> gX_n, is the underlying pointed surface of g.(Y_v, eta_v); i.e. it is the point of the Teichmüller disc of (Y_v,eta_v) labelled by g.
  *Sketch.* The Teichmüller map f_n : X_n -> gX_n is affine of derivative g in q_n-charts. On iota_n(K) the q_n-charts are C^0-close to the eta_v-charts, so f_n o iota_n is (1+o(1))-close to the affine map of derivative g from (K,eta_v) into (gX_n, g q_n). Passing to the limit (bounded-dilatation maps between converging surfaces), the v-component of P_g contains, compatibly for all K, conformal copies of g.(K,eta_v), hence equals g.(Y_v,eta_v) off the punctures, and the punctures correspond. ∎ (sketch)

## 1. Lemma G (GL(2,R)-moves preserve the stratum of boundary limits) — proved

**Lemma G.** Let (X_n,q_n) be generating pairs with X_n -> P in closure(V_0) ∩ Delta_G. Let g in SL(2,R) and X'_n := underlying surface of g.(X_n,q_n). Then X'_n is in V_0, and every limit point P' of (X'_n) in Mbar_g lies in closure(V_0) ∩ Delta_G (same stratum G).

*Proof.*
1. X'_n is in V_0 by total geodesy, so P' is in closure(V_0).
2. The Teichmüller map X_n -> X'_n is K-qc with K = K(g) independent of n.
3. By (Nbhd) for X_n -> P: Ext_{X_n}(gamma_e) -> 0 for the G-curves (by (Ext)), and Ext_{X_n}(beta) >= eps/pi for all other curves beta.
4. By (Ext) under K-qc maps: Ext_{X'_n}(gamma_e) <= K Ext_{X_n}(gamma_e) -> 0, so l_{X'_n}(gamma_e) -> 0; and Ext_{X'_n}(beta) >= eps/(pi K), so l_{X'_n}(beta) is bounded below by a positive constant (since (l/2)e^{l/2} >= Ext forces l bounded below).
5. By the converse part of (Nbhd), every limit P' has dual graph G. ∎

**Lemma G' (equicontinuity).** If d_T(X_n, X'_n) -> 0 and X_n -> P in Mbar_g, then X'_n -> P. Consequently, for a fixed sequence of generating pairs, the maps phi_n: H -> Mbar_g, phi_n(SO(2)g) = underlying(g.(X_n,q_n)), are equicontinuous on compact subsets of H (they are 1-Lipschitz from the hyperbolic metric to d_T), and a subsequence converges locally uniformly to a continuous map phi: H -> closure(V_0) ∩ Delta_G.

*Proof.* (1+o(1))-qc maps X_n -> X'_n: by (Nbhd)/(Ext) as in Lemma G the limits have the same pinched multicurve, and (1+o(1))-qc maps between the converging thick parts converge to conformal isomorphisms between the corresponding components of the limits (standard normal-families argument for qc maps with dilatation -> 1), compatibly with the nodes; so the limits coincide. Equicontinuity into the compact metrisable space Mbar_g follows, Arzelà–Ascoli gives the subsequence (diagonal over an exhaustion of H), and Lemma G puts the values in closure(V_0) ∩ Delta_G. Well-definedness on SO(2)\SL(2,R): rotating q does not change the underlying surface. ∎
(The first sentence is the uniform continuity of (M_g,d_T) -> Mbar_g; I give only the sketch above.)

---

## 2. Lemma T' (positive area forces a Teichmüller curve, unramified) — proved modulo (F), (F2)

**Lemma T'.** Let Delta_G ≅ prod_w M_{g_w,n_w} be a stratum, v a vertex of G, and let (X_n,q_n) be generating pairs with X_n -> P in closure(V_0) ∩ Delta_G such that v carries positive area, with limit eta_v on Y_v = pi_v(P). Then:
1. There is a 1-dimensional irreducible component E of closure(V_0) ∩ Delta_G through P (closure taken in Delta_G) such that C := pi_v(E) is (the image in M_{g_v,n_v} of) the Teichmüller curve generated by (Y_v, eta_v); in particular the SL(2,R)-orbit of (Y_v,eta_v) projects to a closed curve, and its stabiliser is a lattice.
2. pi_v|_E : E -> C is unramified in the orbifold sense (after passing to a level cover, unramified), over C ∩ M_{g_v,n_v}. Hence, lifted to universal covers, pi_v|_E is an isometry from the Poincaré disc onto the Teichmüller disc of (Y_v,eta_v).
3. E is not compact; more precisely pi_v(E) = C is non-compact in M_{g_v,n_v}, so closure(E) ≠ E.

*Proof.*
Step 1 (the lift phi). Take phi: H -> closure(V_0) ∩ Delta_G from Lemma G' (after a subsequence), phi(i) = P. By (F2), pi_v(phi(g)) = [g.(Y_v,eta_v)] in M_{g_v,n_v}, i.e. pi_v o phi = u, where u: H -> M_{g_v,n_v} is the projection of the Teichmüller disc D of (Y_v,eta_v). u is non-constant (Teichmüller discs are embedded in T and T -> M is a quotient by a properly discontinuous action).

Step 2 (phi lands in one irreducible curve). closure(V_0) \ V_0 is a closed analytic set of dimension <= 1 (V_0 is a 2-dimensional algebraic subvariety; reading (R1)). So A := closure(V_0) ∩ Delta_G is a closed analytic subset of Delta_G of dimension <= 1, with locally finitely many irreducible components. phi is continuous and pi_v o phi = u is holomorphic and non-constant. At points z with phi(z) a smooth point of A where pi_v|_A has nonzero derivative, phi = (local inverse of pi_v|_A) o u is holomorphic; the remaining z form a closed set whose image under u lies in the discrete set of critical values... (more cleanly: lift to the normalisation A^nu; phi is a continuous lift of the holomorphic u through the finite holomorphic map pi_v: A^nu -> M, and a continuous lift of a holomorphic map through a finite holomorphic map of curves is holomorphic, since it is holomorphic off a discrete set and continuous.) So phi: H -> A^nu is holomorphic and non-constant; its image lies in a single irreducible component E (H is irreducible: the preimages of the components are analytic subsets covering H). E has dimension 1 since phi is non-constant.

Step 3 (C is a Teichmüller curve). C := pi_v(E) is an irreducible algebraic curve (image of an irreducible quasi-projective curve with non-constant map; constructible, 1-dimensional; take its closure in M_{g_v,n_v}). u(H) ⊂ C. Let C^nu be the normalisation and C~ its universal cover. Since u is a non-constant holomorphic map H -> C, it lifts to u~: H -> C~ (H simply connected, lifting through normalisation as in Step 2), and C~ = H: otherwise C~ = C or P^1 and the classifying map C~ -> M lifts (simply connected, level cover) to a holomorphic map into the bounded domain T, hence is constant, contradicting non-constancy of u. Let Lambda: C~ -> T be the lift of C -> M with Lambda o u~ = D (the Teichmüller disc map, after choosing the lift compatibly). Kobayashi distances do not increase under holomorphic maps and k_T = d_T (Royden), so for x,y in H:
  d_T(D x, D y) = d_T(Lambda u~ x, Lambda u~ y) <= k_H(u~ x, u~ y) <= k_H(x,y) = d_T(D x, D y),
the last equality because D is an isometric embedding. Hence u~ is a holomorphic self-map of H preserving the Poincaré distance, i.e. an automorphism, and Lambda = D o u~^{-1} is a Teichmüller disc. So C is covered by the Teichmüller disc of (Y_v,eta_v): u: H -> C is the orbifold universal covering, C is a Teichmüller curve, and the Veech group of eta_v is a lattice (its quotient covers C, which has finite hyperbolic area as a quasi-projective curve).

Step 4 (unramified). Let p := pi_v|: E^nu -> C^nu (finite, surjective onto its image) and recall p o phi = u with u the orbifold universal covering. Remove from C the finitely many orbifold points and branch values of p, getting C°, and let E° := p^{-1}(C°). Then p: E° -> C° is a finite covering, u: u^{-1}(C°) -> C° is a covering, and phi restricted to u^{-1}(C°) is a lift; its image is open and closed in E°, hence equal to E° (E° is connected, E being irreducible). Now let c_0 be a non-orbifold point of C and e_0 in p^{-1}(c_0) with local degree k. Take a small disc B around c_0; u^{-1}(B) is a disjoint union of discs B_alpha mapped biholomorphically by u. Each phi(B_alpha) is a continuous section of p over B, so it is a sheet of p over B meeting p^{-1}(c_0) at a point of local degree 1. The punctured neighbourhood of e_0 lies in E° ⊂ phi(H), so it is covered by such sheets; but a punctured neighbourhood of a point of local degree k is a connected k-fold cover of B \ {c_0} and contains no sheet over B \ {c_0} unless k = 1. Hence k = 1: p is unramified away from orbifold points. At orbifold points the same argument on a level cover (where C is replaced by a manifold quotient H/Lambda', Lambda' torsion-free) gives orbifold-unramifiedness. Therefore the lift of pi_v|_E to universal covers is a biholomorphism onto H composed with the isometry D: an isometry onto the Teichmüller disc.

Step 5 (non-compact). Teichmüller curves are never compact: (Y_v,eta_v) has a cylinder (Masur's theorem on closed trajectories of finite-area quadratic differentials, cited from memory); its core is non-peripheral (Gauss–Bonnet: a disc bounded by a cylinder boundary would have to contain total curvature 2 pi, impossible with at most one cone point of angle pi plus non-positive curvature points), and contracting it by the diagonal flow in u(H) ⊂ C sends its extremal length to 0, so C leaves every compact subset of M_{g_v,n_v}. Since u = p o phi with phi(H) ⊂ E, pi_v(E) ⊇ u(H) = C is non-compact, so E is not compact, i.e. closure(E) ≠ E. ∎

**Remark (relation to Lemma R).** Lemma R (Royden + Thurston + Imayoshi–Shiga) needs l_{E_0}(gamma) = tau_T(rho(gamma)) for all gamma, which holds iff pi_v|_{E_0} lifts to an isometry of universal covers, i.e. iff pi_v|_{E_0} is (orbifold-)unramified onto a Teichmüller curve. If pi_v|_{E_0} were a branched cover of a Teichmüller curve, l_{E_0} would be strictly larger than tau_T(rho) for some gamma and the Thurston step would fail. Lemma T' shows unramifiedness comes for free whenever v carries positive area at one point of E_0. I checked the remaining steps of Lemma R and found them sound modulo the cited theorems (Thurston's minimal-stretch theorem in the finite-area case with cusps, and rigidity of homotopic non-constant holomorphic maps over a fixed base); I did not re-prove them.

---

## 3. Consequences at t = 0

**Lemma V (the constant vertex carries no area).** In the setting of (T0) (pi_i(∂V_0) = {Y_0}, dim M_{g_i,n_i} > 0), for every P in ∂V_0 and every sequence of generating pairs (X_n,q_n) -> P, vertex i does not carry positive area.

*Proof.* Otherwise Lemma T' (with G = Gamma, v = i) gives a component E of closure(V_0) ∩ Delta_Gamma = ∂V_0 with pi_i(E) a curve, contradicting pi_i(∂V_0) = {Y_0}. ∎

**Remark (infinite-area version, sketch only).** If vertex i carries a non-integrable limit eta_i at a lower scale s_n -> 0, the same limiting argument (with g replaced by its conjugate r_theta^{-1} g r_theta, theta = lim arg s_n) suggests that every affine deformation of (Y_0,eta_i) is conformally trivial, rel the punctures, in the Teichmüller space T_{g_i,n_i}. Infinitesimally: the Beltrami differential conj(eta_i)/|eta_i| annihilates Q(Y_0), i.e. ∫_{Y_0} phi conj(eta_i)/|eta_i| = 0 for all integrable phi in Q(Y_0). (E.g. eta_i = dz^2 on (P^1; ∞,0,1,lambda) is affinely rigid iff lambda is real; a meromorphic differential with all relative periods on one real line is affinely rigid.) I have not written a complete proof (it needs (F2) for non-integrable limits, where the affine map is no longer extremal) and I do not use it below.

**Proposition C (cusps).** Suppose that at some P in ∂V_0 some sequence of generating pairs gives some vertex j of Gamma positive area. Then j ≠ i, the component E of ∂V_0 through P given by Lemma T' satisfies closure(E) ≠ E, and pi_j(E) is a Teichmüller curve onto which pi_j|_E is orbifold-unramified. In particular (T0)(c) holds.

*Proof.* j ≠ i by Lemma V; the rest is Lemma T' (1)–(3) with G = Gamma. ∎

**Hypothesis (PA) and when it can fail.** Normalise Area(q_n) = 1. If no vertex carries positive area, then all the area of q_n concentrates, in the limit, in the collars of the curves of Gamma; these collars then contain flat cylinders of modulus -> infinity carrying area -> 1 (the edges are "horizontal"). I could not exclude that this happens at every point of ∂V_0 for every choice of generating pairs, so (c) is proved only under:
- **(PA)** some point of ∂V_0 admits generating pairs for which some vertex carries positive area.
Note that (PA) is about the choice of q_n in the one-complex-parameter family Q_V(X_n)/C^* (a P^1 of directions); it is not a condition on a single sequence. I expect (PA) always to hold (choose q_n dual to a tangent vector of V_0 along the boundary direction, which deforms the thick part), but I have no proof.

---

## 4. Reduction of (T0) to a positive-area merge statement

**(T0\*)** There is a cusp P_0 of ∂V_0 (P_0 in closure(∂V_0) \ ∂V_0, in a stratum Delta_{G'}) and a 1-dimensional piece E_0 of closure(V_0) ∩ Delta_{G''}, with Delta_{G'} ⊂ closure(Delta_{G''}) and P_0 in closure(E_0), such that
- (merge) some edge of G' at vertex i is unpinched in G'' (equivalently, vertex i of G' lies in a strictly larger vertex v of G''), and

### PR-H. Lemma PA (positive area at generic boundary points), Lemma NH and Proposition K (the Y_0-network reaches a MERGE or MOV branch) (from round6_q9, verbatim, sections 1–3)
## 1. Gap (d): Lemma PA (proved, modulo cited standard facts)

### 1.1 Cited standard facts (from memory)
- **(Pl) Plumbing chart.** Near P ∈ Δ_Γ there is a holomorphic orbifold chart of M̄_g with coordinates (z, t) = (z, (t_e)_{e∈E(Γ)}), built as follows. z ranges over a neighbourhood of P in ∏_w T_w (or a Kuranishi chart of the product); the component Y_w(z) is obtained from the fixed Y_w = Y_w(0) by a quasiconformal deformation whose Beltrami differential is supported in a fixed compact set K_w ⊂ Y_w, disjoint from fixed coordinate discs {|z_e| < 1} around the punctures. The surface X(z,t) is obtained by plumbing z_e w_e = t_e in these discs. (Masur 1976; Bers; Wolpert. Cited from memory.) Consequently:
  - the tangent vector ∂/∂z_k at (z,t) is represented on X(z,t) by the transplanted Beltrami differential of the deformation of the components, supported in ι(K_w) and with sup norm bounded uniformly in t;
  - the vector ∂/∂t_e at (z,t) is represented by a Beltrami differential supported in the collar of e (computed in 1.2).
- **(Dual) Teichmüller norm.** For a tangent vector v at X represented by a Beltrami μ, ‖v‖_T = sup{Re ∫ μφ : φ ∈ Q(X), ‖φ‖_1 = 1}, where Q(X) is the space of integrable holomorphic quadratic differentials (at most simple poles at punctures). The supremum is attained at a unique φ = q_v (the norming differential), and the Teichmüller disc through X tangent to v is the disc generated by q_v. (Teichmüller, Hamilton–Krushkal, Royden; classical.)
- **(Bun) Quadratic differentials at a stable curve.** For the plumbing family, π_*(ω^{⊗2}) is a vector bundle of rank 3g−3 whose fibre at P is H^0(P, ω_P^{⊗2}): differentials on the components with at most double poles at the node branches, with equal leading (double-pole) coefficients a_e on the two branches of each node. The functionals a_e (leading coefficient in the plumbing coordinate z_e, i.e. a_e(φ) = (2πi)^{-1}∮_{|z_e|=r_0} z_e φ/dz_e) are holomorphic on the bundle and linearly independent at P; their common kernel at P is ⊕_w Q(Y_w). (Standard; dimension count Σ_w(3g_w−3+n_w) = 3g−3−|E(Γ)|.)

### 1.2 The collar Beltrami
In the collar of e at X(z,t_0), use the coordinate z = z_e on {|t_0| < |z| < 1} (with w_e = t_0/z). For t near t_0 define F_t(z) = z·exp(c·λ(z)), λ(z) = log|z| / log|t_0|, c = log(t/t_0), and F_t = id off the collar. Then F_t is the identity at |z| = 1, and in the w-coordinate it is w ↦ w (t/t_0)^{1−λ}, the identity at |w| = 1. So F_t: X(z,t_0) → X(z,t) is quasiconformal. Its Beltrami coefficient is
 μ_t = (z/z̄) · (c/(2 log|t_0|)) / (1 + c/(2 log|t_0|)).
Differentiating at t = t_0 (c ≈ δ := (t − t_0)/t_0): the vector δ·t_0 ∂/∂t_e is represented by the Beltrami (δ/(2 log|t_0|))·(z/z̄) on the collar, with sup norm |δ|/(2 log(1/|t_0|)). Hence

 **(C)** ‖b ∂/∂t_e‖_T ≤ |b| / (2 |t_e| log(1/|t_e|)).

### 1.3 The statement
**Lemma PA.** Let P be a generic point of ∂V_0 (outside a discrete subset of ∂V_0). There are X_n ∈ V_0, X_n → P, and generating pairs (X_n, q_n), ‖q_n‖_1 = 1, such that, after passing to a subsequence, the transplanted differentials ι_n^*q_n converge locally uniformly on each component Y_w of P to q_w ∈ Q(Y_w) with:
1. Σ_w ‖q_w‖_1 = 1 (no area is lost in the collars);
2. q_w ≠ 0 only for vertices w at which ∂V_0 moves (in a sense made precise below); in particular q_i = 0;
3. there is a vertex j ≠ i with q_j ≠ 0, i.e. j carries positive area in the sense of PR-F (F) with s_n = 1.
In particular hypothesis (PA) of PR-F holds, at every generic point of ∂V_0.

*Proof.*
**Step 1 (local model).** Let ν: N → closure(V_0) be the normalization of a local irreducible component (branch) of the germ of closure(V_0) along ∂V_0 near P, lifted to the manifold chart of (Pl). Normal surfaces have isolated singular points, and the preimage of ∂V_0 is a curve; so for generic P, N is smooth at the point over P, with coordinates (s, τ) in which the preimage of ∂V_0 is {τ = 0}. The plumbing coordinates pull back to holomorphic functions t_e(s,τ) vanishing on {τ = 0}; write t_e = u_e(s,τ) τ^{m_e} with m_e ≥ 1 and u_e not divisible by τ. The zero set of u_e meets {τ = 0} in a discrete set, which we avoid (genericity). Also z(s,0) parametrizes ∂V_0, and for generic P, a := ∂_s z(s_0,0) ≠ 0 (the parametrization of the curve ∂V_0 is an immersion off a discrete set). Since π_i is constant on ∂V_0, the i-component of a is 0: a = (a_w)_w with a_i = 0.

**Step 2 (the vectors v_n).** Take τ_n → 0 and X_n := ν(s_0, τ_n) ∈ V_0 (points with τ ≠ 0 are in V_0 since t_e ≠ 0 there). Let v_n := dν(∂_s) at (s_0,τ_n), a tangent vector to V_0. In plumbing coordinates v_n = (∂_s z(s_0,τ_n), (∂_s t_e(s_0,τ_n))_e), with ∂_s z(s_0,τ_n) → a and ∂_s t_e = (∂_s u_e) τ^{m_e}, so |∂_s t_e| ≤ C|t_e| because u_e is a unit near (s_0,0). By (Pl) and (C), v_n is represented by a Beltrami differential μ_n = Σ_w ι_n^* μ_w^{(n)} + ν_n, where μ_w^{(n)} is supported in K_w, depends continuously on the vector and converges to a Beltrami μ_w on Y_w representing a_w (take μ_i^{(n)} → 0, since a_i = 0), and ‖ν_n‖_∞ ≤ C' / log(1/max_e|t_e(X_n)|) → 0.

**Step 3 (upper bound).** Put A := max_w ‖a_w‖_{T(Y_w)} > 0 (a ≠ 0). Let φ_n ∈ Q(X_n), ‖φ_n‖_1 = 1. By normal families (an L^1-bounded family of holomorphic quadratic differentials is locally uniformly bounded), after a subsequence ι_n^*φ_n → φ_w locally uniformly on each Y_w. By Fatou on the disjoint images ι_n(K) of exhausting compacts, Σ_w ‖φ_w‖_{L^1(Y_w)} ≤ 1; in particular φ_w is integrable, hence φ_w ∈ Q(Y_w). Then
 Re ∫ μ_n φ_n → Σ_w Re ∫_{Y_w} μ_w φ_w ≤ Σ_w ‖a_w‖ ‖φ_w‖ ≤ A Σ_w ‖φ_w‖ ≤ A,
using |∫ ν_nφ_n| ≤ ‖ν_n‖_∞ → 0 and (Dual) on Y_w. Hence limsup ‖v_n‖_T ≤ A.

**Step 4 (lower bound).** Let j attain the maximum, and φ ∈ Q(Y_j) with ‖φ‖ = 1 and Re ∫ μ_j φ = A. The element φ ⊕ 0 lies in the fibre at P of the subbundle ker(a_e : e ∈ E(Γ)) of (Bun); extend it to a holomorphic section of that subbundle and let φ_n be its value at X_n. Then ι_n^*φ_n → φ on Y_j and → 0 on the other components, locally uniformly. **Collar mass.** In the collar {|t|/r_0 < |z| < r_0} of an edge e write φ_n = Σ_k c_k z^k dz². By construction c_{−2} = a_e(φ_n) = 0. The coefficients c_k, k ≥ −1, are bounded by C r_0^{−k} (Cauchy estimates on |z| = r_0, where φ_n is uniformly bounded). The terms with k ≤ −3 are, in the coordinate w = t/z, the terms c_k t^{k+2} w^{−k−4} dw² with −k−4 ≥ −1, bounded likewise by Cauchy on |w| = r_0. Since ∫_{|z|<ρ}|z|^k dA ≤ 2πρ^{k+2}/(k+2) ≤ 2πρ for k ≥ −1, ρ ≤ 1, the mass of φ_n in {|t|/ρ < |z| < ρ} is ≤ Cρ for ρ ≤ r_0/2, uniformly in n. With convergence on the thick parts this gives ‖φ_n‖_1 → ‖φ‖ = 1. Then Re ∫ μ_n φ_n → Re ∫ μ_j φ = A. So liminf ‖v_n‖_T ≥ A, and ‖v_n‖_T → A.

**Step 5 (the norming differentials).** Let q_n be the norming differential of v_n (‖q_n‖ = 1). By (Dual) the Teichmüller disc tangent to v_n is generated by q_n; since v_n is tangent to V_0 and V_0 is totally geodesic, (X_n,q_n) is a generating pair. Pass to a subsequence with ι_n^*q_n → q_w on each Y_w. As in Step 3,
 A = lim Re ∫ μ_n q_n = Σ_w Re ∫ μ_w q_w ≤ Σ_w ‖a_w‖‖q_w‖ ≤ A Σ_w ‖q_w‖ ≤ A.
All inequalities are equalities. Hence Σ_w ‖q_w‖ = 1 (item 1); q_w = 0 unless ‖a_w‖ = A (item 2; in particular q_i = 0 since a_i = 0 and A > 0); and some q_j ≠ 0, j ≠ i (item 3); moreover q_w norms a_w whenever q_w ≠ 0. ∎

**Remarks.**
- This closes gap (d) of PR-F §6 completely, at every generic point of ∂V_0, with positive area located at a vertex j where the tangent vector of ∂V_0 has maximal Teichmüller norm.
- By Proposition C of PR-F, π_j(E) is then a Teichmüller curve (E the component of ∂V_0 through P), π_j|_E is orbifold-unramified onto it, and closure(∂V_0) ≠ ∂V_0 has cusps. (PR-F's Lemma T' depends on (F2), which PR-F only sketched; I have not re-proved (F2).)
- Corollary (full area): the area of the limit sits entirely on the moving vertices at maximal speed; in particular for the generic P the limit differential (q_w)_w on P is a genuine area-1 integrable differential on the stable curve P, with q_i = 0.
- The same proof applies verbatim to **any** 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, for any product-type stratum Δ_G and any generic point of E (only the local model of Step 1 was used, plus a ≠ 0). Used in §4.

## 2. Gap (c), first half: choice of direction (proved)

Setting: P, (X_n,q_n), (q_w)_w and j as in Lemma PA. For e ∈ Γ_i (edges at i) let γ_e be the core curve of the e-collar of X_n. Transport curves along Teichmüller maps X_n → g_s X_n, where g_s = diag(e^{-s}, e^{s}) contracts horizontal and expands vertical q-lengths ("path marking").

**Lemma NH.** After passing to a subsequence and replacing q_n by e^{-2iθ_n} q_n with θ_n → 0 (which keeps all conclusions of Lemma PA, the rotation being absorbed in the limit), we may assume:
1. there is an essential, non-peripheral curve c of Y_j (hence of S_g, not homotopic to any Γ-curve) and m > 0 such that each q_n has a horizontal cylinder in the class c_n of c of modulus ≥ m; hence Ext_{g_sX_n}(c_n) ≤ e^{-2s}/m for all s ≥ 0;
2. there is e_0 ∈ Γ_i such that the q_n-geodesic representative of γ_{e_0} is not horizontal; hence Ext_{g_sX_n}(γ_{e_0}) → ∞ as s → ∞, for each n.

*Proof.*
- (Cited from memory: Masur.) Cylinder directions of a finite-area quadratic differential are dense in RP^1. A cylinder core of (Y_j,q_j) is non-peripheral: a flat cylinder boundary bounding a disc with at most one simple pole contradicts Gauss–Bonnet (PR-F, Step 5 of Lemma T').
- For each e ∈ Γ_i, the q_n-geodesic representative of γ_e is a chain of saddle connections or a cylinder core. If all its segments are parallel, call their direction θ_n(e) ∈ RP^1; otherwise θ_n(e) is undefined. Pass to a subsequence along which, for e = e_0 fixed, either θ_n(e_0) is always undefined or θ_n(e_0) → θ_∞(e_0).
- Choose a cylinder direction of q_j different from θ_∞(e_0) and rotate so that it is horizontal. Let A be the open horizontal cylinder, A' ⋐ A a compact sub-annulus of modulus m' > 0. On ι_n(A') the differentials q_n converge to q_j in C^1; √q_n is defined on ι_n(A') for large n (the sign holonomy is discrete), so the developing map of ι_n(A') is equivariant under a translation v_n → v ∈ R \ {0}. Its image contains a straight strip in direction v_n of width close to that of A', so q_n has a cylinder in the class of c of modulus ≥ m := m'/2, in direction arg v_n → 0. Put θ_n := arg v_n and rotate. Then this cylinder is exactly horizontal. Under g_s its modulus is multiplied by e^{2s}, giving item 1.
- Since arg v_n → 0 ≠ θ_∞(e_0), for large n γ_{e_0} is not horizontal for the rotated q_n. So some saddle connection of its geodesic has nonzero vertical component, and its vertical measure v := i(γ_{e_0}, F_hor(q_n)) is > 0. (The q-geodesic realizes the intersection numbers with both measured foliations; standard, cited.) Then ℓ_{g_sq_n}(γ_{e_0}) ≥ e^{s}v, and Ext ≥ ℓ²/Area = ℓ² ≥ e^{2s}v² → ∞. ∎

**Remark.** This bypasses gaps (a) and (b) of PR-F §6. Item 1 needs only one exactly horizontal cylinder, obtained by a rotation tending to 0, and not a Jenkins–Strebel q_n. No interchange of the limits is needed below, because I work with connected limit sets instead of the Jenkins–Strebel limits Z_n.

## 3. Proposition K: Y_0 merges or moves somewhere on its own boundary network (proved, modulo routine marking details)

Notation:
- B := closure(V_0) \ V_0. This is a compact 1-dimensional analytic set; work on a level cover if needed.
- Σ_i ⊂ S_g is the subsurface of vertex i, and ∂Σ_i = {γ_e : e ∈ Γ_i}. Both are path-marked.
- ψ(X) ∈ M̄_{g_i,n_i} is the "Σ_i-part" of X. Fix a pants decomposition of Σ_i. ψ(X) is the surface with the Fenchel–Nielsen coordinates of X inside Σ_i and boundary lengths set to 0. It is continuous on augmented Teichmüller space near points where ∂Σ_i is pinched, and there it equals the stable curve on the Σ_i-side.
- d is a metric on M̄_{g_i,n_i}.

**Cited facts (from memory).**
- Kerckhoff: Ext_Y(γ) ≤ e^{2 d_T(X,Y)} Ext_X(γ).
- Maskit's comparison (Ext) of PR-F.
- Lemma G / G′ of PR-F: limits of g_{s_n}X_n with s_n → s* < ∞ lie in ∂V_0. Each such limit equals φ(g_{s*}), up to a subsequence of the φ's.

For δ, η > 0 let T_n = T_n(δ,η) be the first s ≥ 0 at which max_{e∈Γ_i} Ext_{g_sX_n}(γ_e) = δ or d(ψ(g_sX_n), Y_0) = η.

**Step 1 (T_n is finite and tends to ∞).** By Lemma NH(2), Ext(γ_{e_0}) → ∞ along the ray, so T_n < ∞. For s in a compact set, g_sX_n converges to points of ∂V_0, uniformly in s (Lemma G′). At those points ∂Σ_i is pinched and ψ = Y_0, because vertex i of every point of ∂V_0 is Y_0. Hence T_n → ∞.

**Step 2 (the continuum).** Let K = K(δ,η) be a Hausdorff limit (subsequence) of the compact connected sets {g_sX_n : 0 ≤ s ≤ T_n}. Then K is compact and connected, and it contains P. Every point of K is a limit of g_{s_n}X_n with s_n ≤ T_n:
- if s_n stays bounded, the limit lies in ∂V_0 ⊂ B;
- if s_n → ∞, the curve c is pinched by Lemma NH(1), so the limit lies in B.

So K ⊂ B. On K, every ∂Σ_i curve has Ext ≤ δ (in the limit sense along the approximating sequences) and d(ψ, Y_0) ≤ η. Let Q = Q(δ,η) ∈ K be a limit of the endpoints g_{T_n}X_n. Then Q ∈ B, and either
- (a) some γ_e, e ∈ Γ_i, has Ext = δ > 0 at Q, so it is unpinched at Q; or
- (b) d(ψ(Q), Y_0) = η.

**Step 3 (δ_k, η_k → 0).** Pass to a subsequence with K(δ_k,η_k) → K_0 and Q_k := Q(δ_k,η_k) → Q_0. Then K_0 ⊂ B is compact and connected, and contains P and Q_0. At every point of K_0 the curves ∂Σ_i are pinched (Ext ≤ δ_k → 0 along approximating sequences) and the Σ_i-side is the single smooth component Y_0. So vertex "i" is intact, ≅ Y_0, at every point of K_0, consistently with the path marking.

**Proposition K.** There are a compact connected set K_0 ⊂ B containing ∂V_0's point P, along which the Σ_i-component is intact and equal to Y_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B at Q_0 such that one of the following holds:
- **(MERGE)** along b \ {Q_0} some curve of ∂Σ_i is unpinched, i.e. the Y_0-component of Q_0 is merged with other components along b (the merge property of PR-C, at Q_0);
- **(MOV)** along b all of ∂Σ_i stays pinched, but the Σ_i-component is non-constant along b, with limit Y_0 at Q_0.

*Proof.*
- In case (a) for infinitely many k, Q_k ≠ Q_0, because γ_e is pinched at Q_0 and unpinched at Q_k. Put Q̃_k → Q̃_0 in augmented Teichmüller space by choosing lifts and applying mapping classes, so that the path markings converge; this is possible since M̄_g is the quotient of augmented Teichmüller space.
- Near Q_0, B is a finite union of branches, each of which minus Q_0 lies in one stratum. Infinitely many Q_k lie on one branch b, and γ_e is unpinched on b \ {Q_0}: (MERGE).
- In case (b) for infinitely many k: if some ∂Σ_i curve is unpinched at infinitely many Q_k, argue as before to get (MERGE).
- Otherwise ∂Σ_i is pinched at the Q_k, so the Σ_i-side of Q_k is a union of components with ψ(Q_k) at distance η_k > 0 from Y_0 = ψ(Q_0). Again Q_k ≠ Q_0, and the Q_k lie on one branch b, along which ψ is non-constant: (MOV). ∎

**What Proposition K does not give.**
- Q_0 need not lie in closure(∂V_0). K_0 can leave closure(∂V_0) through "STAY" branches: branches of B at points of closure(∂V_0) along which the Y_0-vertex stays intact and constant, but which are not contained in closure(∂V_0).
- The ρ-variant settles nothing. Add the stopping condition "g_sX_n leaves the ρ-neighbourhood of closure(∂V_0)", with η ≪ ρ. That variant shows: **at some point Q ∈ closure(∂V_0) there is a branch of B, not contained in closure(∂V_0), of type MERGE, MOV or STAY.** This is only Lemma C1 of PR-C with the extra edge located; it does not exclude STAY.
- Heuristic for why STAY should really occur, from the multi-scale picture, not proved. Suppose the zero-area part of the limit at P has two levels below the top: a vertex w at level −1 and the vertex i at level −2, attached below w. Along the ray, lower levels are "released" (become commensurate with the contracted top-level skeleton) top-down. w merges with the top-level skeleton first, along a branch b_w at the cusp Q of ∂V_0, and the Y_0-vertex is still intact and constant along b_w. The merge of Y_0 then happens at a cusp of b_w, which is in general not in closure(∂V_0).


### PR-I. The quintic-cover example, the Krull/twin mechanism, Lemma D (merge or twin), the Pinning Lemma and Theorem 4 (from round6_q6, verbatim, sections 2–4). The example surface is NOT smooth (it has a coarse A_1 point at y^5 = x^5 − x and two fixed-locus sheets crossing at the Fermat quintic; proved in round6_q3), so it is a test case, not an admissible V_0.
## 2. Example: the surface of cyclic quintic covers in M_6 (MS5 fails; V_0 is not smooth)

### 2.1 Construction
- For distinct a = (a_1, …, a_5) on P^1, let X_a be the smooth projective model of y^5 = ∏_{j=1}^5 (x − a_j), with the obvious change if some a_j = ∞.
- X_a → P^1 is a Z/5-cover, totally ramified over a_1, …, a_5 with local monodromy 1 ∈ Z/5 at each, and unbranched elsewhere. The degree of the polynomial is 5 ≡ 0 mod 5, so ∞ is unbranched.
- Riemann–Hurwitz gives 2g − 2 = 5·(−2) + 5·4 = 10, so g = 6.
- This defines Φ : M_{0,5} → M_6, invariant under S_5 because all five monodromies are equal. Put V_0 := Φ(M_{0,5}).

### 2.2 V_0 is totally geodesic and 2-dimensional (standard; cited from memory)
- Let q be an integrable quadratic differential on (P^1; a_1, …, a_5), so it has at most simple poles at the a_j. Its pullback f^*q has order e(−1 + 2) − 2 = 3 ≥ 0 at each ramification point (e = 5). So f^*q is a holomorphic quadratic differential on X_a.
- The Teichmüller map of the base with initial differential q lifts to an affine map for f^*q, which is a Teichmüller map upstairs. Hence the lifting map T_{0,5} → T_6 is a holomorphic isometric embedding (classical).
- Every tangent direction of T_{0,5} at a point is the Teichmüller direction of a unique (up to positive scaling) q. The Teichmüller disc of T_6 in the image direction is the disc of f^*q, which is the image of the disc of q. So every Teichmüller disc tangent to V_0 lies in V_0.
- Φ is finite-to-one: X_a has finitely many automorphism subgroups, and the quotient by one of them recovers the unordered branch set. So dim V_0 = 2.

### 2.3 Boundary (admissible covers; Harris–Mumford, cited from memory)
- An abelian cover has a unique admissible cover over each stable 5-pointed tree. This gives a continuous extension Φ̄ : M̄_{0,5} → M̄_6, sending a stable tree to the stabilized admissible cover.
- Then closure(V_0) = Φ̄(M̄_{0,5}), since the image is compact and contains V_0 as a dense subset.
- Boundary points go to nodal curves (computed below), so Φ̄^{-1}(M_6) = M_{0,5}. Hence V_0 is closed in M_6.
- **Local monodromies.** On every component of an admissible cover, the local monodromies at the special points sum to 0 in Z/5. Here every local monodromy is nonzero, hence a generator. So each component cover is connected and totally ramified over every special point.

**Over D_{ab}° (base A ∪ B, with A ∋ a_a, a_b and B ∋ the other three points):**
- Over A the monodromies are (1, 1, 3). Riemann–Hurwitz gives 2g − 2 = −10 + 12, so g = 2, with one point over the node.
- Over B they are (1, 1, 1, 2), so 2g − 2 = −10 + 16 and g = 4, again with one point over the node.
- The stable curve is a genus-2 curve and a genus-4 curve glued at one point. Its dual graph Γ has vertices of genus 2 and 4 joined by one edge, and Δ_Γ = M_{2,1} × M_{4,1}. This is of product type: the gluing map is bijective onto Δ_Γ because the two vertices have different genera.
- The genus-2 component is the Z/5-cover of a 3-pointed sphere with monodromy (1, 1, 3), marked at the point over the third point. It is the same pointed curve Y_0 ∈ M_{2,1} for every (a, b) and every point of D_{ab}°, namely y^5 = x(x − 1) marked over x = ∞. So π_1 ≡ Y_0.
- The genus-4 component is the covering construction with data (1, 1, 1, 2) over the 4-pointed sphere B, marked over the node. Let C ⊂ M_{4,1} be its image as B runs over M_{0,4}. The map M_{0,4} → C is finite-to-one by the argument of 2.2, so dim C = 1.
- Hence Φ̄(D_{ab}°) = {Y_0} × C for all ten pairs (a, b).

**Over the 15 points D_{ab} ∩ D_{cd} (base chain A(a_a, a_b) — B(a_m) — C(a_c, a_d)):**
- The monodromies are (1, 1, 3) on A, (2, 1, 2) on B and (3, 1, 1) on C.
- The covers over A and C are both Y_0. The cover over B has genus 2 (2g − 2 = −10 + 12) and two points over the nodes; call this 2-pointed curve B_0.
- So all 15 points map to one stable curve P_0 = Y_0 — B_0 — Y_0, a chain of three genus-2 curves. Its dual graph is G' (path with 3 vertices).

**Conclusion.**
- closure(V_0) \ V_0 = ({Y_0} × C) ⊔ {P_0}.
- ∂V_0 = closure(V_0) ∩ Δ_Γ = {Y_0} × C is irreducible, because it is the image of the irreducible D_{12}°. It has dimension 1, and π_1(∂V_0) = {Y_0} with dim M_{2,1} = 4 > 0.
- closure(∂V_0) = ∂V_0 ⊔ {P_0}.

### 2.4 MS5 fails for this V_0
- The strata meeting closure(V_0) are M_6, Δ_Γ and Δ_{G'}.
  - closure(V_0) ∩ M_6 = V_0 is irreducible of dimension 2, so it has no 1-dimensional components.
  - closure(V_0) ∩ Δ_{G'} = {P_0}.
  - Hence the only 1-dimensional piece in any stratum is E = ∂V_0 ⊂ Δ_Γ.
- So the only candidate in MS5 is G = Γ, E = ∂V_0, P_0 the point above. Lemma 1 (u = genus-2 vertex) shows that clause (a) fails there. Concretely, the lift R = (Y_0, B_0 ∪ Y_0) ∈ {Y_0} × closure(C) has R_1 = Y_0 smooth.
- **All hypotheses of MS5 hold except smoothness:** g = 6 ≥ 2; V_0 is closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; dim ∂V_0 = 1; π_1(∂V_0) = {Y_0} with dim M_{2,1} > 0.

### 2.5 Caveat: this V_0 is not smooth (sketch)
- **Fermat point, orbifold sense.** The Fermat quintic F : x^5 + y^5 + z^5 = 0 has genus 6 and lies in V_0 in three ways. The quotients by z ↦ ζz, by y ↦ ζy and by x ↦ ζx are each P^1, totally branched over 5 points.
  - In a Teichmüller chart at a lift of F, the preimage of V_0 therefore contains the three fixed loci Fix(H_x), Fix(H_y), Fix(H_z) of these order-5 subgroups. Each is a smooth 2-dimensional germ.
  - They are distinct germs. If two coincided, the generic X_a would carry a second Z/5 acting nontrivially on X_a/H ≅ P^1 and preserving the branch set, and a generic 5-point configuration has no nontrivial symmetry.
  - So V_0 is not a smooth sub-orbifold at F.
- **The point c_4 = {0, ±1, ±i}, coarse sense.** Its stabilizer in PGL_2 is Z/4, generated by z ↦ iz. (0 is the only point lying on no harmonic 4-subset, so it is fixed. The symmetries of the square fixing 0 are the rotations.)
  - The induced action on T_{c_4} M_{0,5} has eigenvalues (i, −1). Compute T = (⊕_j T_{p_j} P^1)/sl_2 with characters {i, 1, i, −1, −i} − {i, 1, −i}.
  - So the coarse germ of M_{0,5}/S_5 there is C^2/(Z/4) with weights (1, 2). This is an A_1 singularity, since the group is not generated by reflections.
  - I expect the coarse germ of V_0 at Φ(c_4) to be this quotient. This needs the generic automorphism group of X_a to be exactly Z/5, which I have not checked.

So the example is a counterexample to **MS5 with the smoothness hypothesis removed**, not to MS5 as stated. Smoothness of V_0 is an interior condition, while everything in MS5 concerns the boundary. I see no way smoothness could create the missing boundary curves of Corollary 1. But I have not found a smooth example in which they are missing.

## 3. In the example the problem's conclusion still holds: the twin mechanism

**Proposition 3.** Let V_0 be the surface of Section 2. Let V_t be a family as in the problem, with readings (R1), (R2), and with ∂V_t := closure(V_t) ∩ Δ_Γ 1-dimensional and π_1(∂V_t) = {Y_t}. Assume condition (O) of PR-E for the piece E_0 = ∂V_0 and the genus-4 vertex. Then Y_t = Y_0 for all t ∈ Δ.

(Smoothness of V_0 plays no role in the argument.)

*Proof.*

**Step 0 (rigid factor).**
- π_2 : ∂V_0 = {Y_0} × C → C is a bijection, and C is the covering-construction curve from M_{0,4}.
- The lift T_{0,4} → T_{4,1} is a holomorphic isometric embedding. It is equivariant for the subgroup of Mod_{0,4} that preserves the monodromy data. So hypothesis (H_0) of PR-E holds: π_2(∂V_0) is a Teichmüller curve in the orbifold sense. Its normalization is the quotient of the disc by the stabilizer of the Teichmüller disc (standard).
- By Lemma R\* (PR-E, under (O)), K := closure(π_2(∂V_t)) = closure(C) ⊂ M̄_{4,1} for every t.
- K is an irreducible compact curve meeting M_{4,1}, so K_∂ := K ∩ ∂M̄_{4,1} is finite.
- Let F ⊂ M_{2,1} be the finite set of 1-pointed curves that occur as a smooth component of a point of K_∂, marked at one of its special points.

**Step 1 (the transported cusp).**
- Put P_t := H_t(P_0). Since H_t preserves strata, closure(V_t) ∩ Δ_{G'} = {P_t}, closure(V_t) \ V_t = ∂V_t ⊔ {P_t}, and P_t ∈ closure(∂V_t).
- So P_t is a chain A_t — B_t — C_t of genus-2 curves. A_t and C_t each carry one node point, and B_t carries two.

**Step 2 (local chart).**
- Let Def(P_t) be the versal deformation germ of P_t, a smooth germ of dimension 15 on which Aut(P_t) acts. The germ of M̄_6 at P_t is Def(P_t)/Aut(P_t).
- Let s_1, s_2 be the smoothing parameters of the nodes A–B and B–C. The locus {s_1 = 0 ≠ s_2} maps to Δ_Γ, with genus-2 vertex the deformation of A_t. The locus {s_2 = 0 ≠ s_1} also maps to Δ_Γ, with genus-2 vertex the deformation of C_t. The locus {s_1 = s_2 = 0} maps to Δ_{G'}.
- Let S̃ ⊂ Def(P_t) be the preimage of the germ of closure(V_t). It is analytic by (R1), since a fibre of an analytic set is analytic. It is of pure dimension 2, since V_t is a dense 2-dimensional manifold in closure(V_t) and the quotient map is finite.
- Moreover S̃ ∩ {s_1 s_2 = 0} is the preimage of ∂V_t ∪ {P_t}, and S̃ ∩ {s_1 = s_2 = 0} = {0}.

**Step 3 (A_t ≅ Y_t).**
- Since P_t ∈ closure(∂V_t), S̃ ∩ {s_1 s_2 = 0} has a branch β̃ through 0.
- β̃ \ {0} is connected and lies in the disjoint union of the relatively open sets {s_1 = 0 ≠ s_2} and {s_2 = 0 ≠ s_1}. Renaming A ↔ C if needed, β̃ \ {0} ⊂ {s_1 = 0 ≠ s_2}.
- Points of β̃ \ {0} lie over ∂V_t, so their genus-2 component (the A-side one) is Y_t. That component depends continuously on the point of the chart, and its value at 0 is A_t. Hence A_t ≅ Y_t as 1-pointed curves.

**Step 4 (the second branch; Lemma C1 of PR-C).**
- Let X_S be an irreducible component of S̃ containing β̃. The function s_2 is not identically 0 on X_S, because it is nonzero on β̃ \ {0}, and s_2(0) = 0.
- So {s_2 = 0} ∩ X_S is of pure dimension 1 through 0. It does not contain β̃, so it contains a branch b̃ ≠ β̃ with b̃ \ {0} ⊂ {s_2 = 0 ≠ s_1}, using S̃ ∩ {s_1 = s_2 = 0} = {0}.
- Points of b̃ \ {0} lie over closure(V_t) ∩ Δ_Γ = ∂V_t, so their genus-2 component, now the C-side one, is Y_t. Letting the point tend to 0 gives C_t ≅ Y_t.

**Step 5 (pinning).**
- Along β̃, π_2 takes values in π_2(∂V_t) ⊂ K: the genus-4 curve obtained by smoothing B ∪ C.
- Its limit at 0 is W_t := B_t ∪ C_t, glued at the B–C node and marked at the point of B_t over the A–B node. So W_t ∈ K ∩ ∂M̄_{4,1} = K_∂.
- C_t is a smooth component of W_t, marked at its special point, so C_t ∈ F. By Step 4, Y_t ∈ F for every t ∈ Δ.
- t ↦ Y_t is continuous (PR-A) and takes values in a finite set, so it is constant on the connected set Δ. ∎

**Remarks.**
1. Lemma 1 shows that the lift R = (Y_t, W_t) has an *unmerged* copy of Y_t at vertex 1, so Theorem P's (T0-a) fails. The pinning instead comes from a *second* copy (twin) C_t of Y_t, which sits inside the boundary point W_t of the *rigid* Teichmüller factor at the other vertex. Step 4 forces this twin to exist at every t: it is the local analytic Lemma C1 combined with the fact that no other boundary curves exist near P_t.
2. Proposition 3 needs neither t small nor hypothesis (ii) beyond (R2). It uses the totally geodesic structure of V_0 only through Step 0.

## 4. General consequences: a dichotomy, a pinning lemma, and a twin criterion

Throughout this section assume (R1), (R2) and the problem's hypotheses. Write P_t := H_t(P_0).

**Lemma D (merge or twin).** Fix t. Let P ∈ closure(∂V_t) \ ∂V_t lie in Δ_{G'}. Let S̃ be the preimage of the germ of closure(V_t) in the versal deformation germ Def(P), and let s_e (e ∈ E(G')) be the smoothing parameters. For a boundary branch c̃ of S̃ through 0, let S_c ⊂ E(G') be the set of edges with s_e ≡ 0 on c̃. Let β̃ be a branch lying over ∂V_t. Then:
1. The edges of G' not in S_β are contracted by the induced contraction c_β : G' → Γ. Its preimage c_β^{-1}(i) is a single vertex j with no loops and no contracted edges, and the component P_j is isomorphic to Y_t.
2. Let b̃ be another boundary branch with the merge property, i.e. some edge f of G' at j has f ∉ S_b. Then exactly one of the following holds.
   - **(D1) Merge.** b̃ lies over a 1-dimensional piece E of closure(V_t) ∩ Δ_{G_b} with G_b ≠ Γ. Then π_v(E) is non-constant, where v is the vertex of G_b containing j (Lemma C2 of PR-C).
   - **(D2) Twin.** b̃ lies over ∂V_t. Then c_b^{-1}(i) is a single loop-free vertex j' ≠ j, and P_{j'} ≅ Y_t. So P has a second component isomorphic to Y_t.

*Proof.*
1. Along β̃ \ {0}, the i-coordinate is the constant smooth curve Y_t. Its limit at 0 is the stable curve assembled from the components P_k, k ∈ c_β^{-1}(i), glued along the edges of G' contracted into i.
   - This limit is the smooth curve Y_t. So the assembled curve has no node, which means c_β^{-1}(i) is one vertex j with no contracted edges or loops, and P_j ≅ Y_t.
2. The coarse image of b̃ \ {0} lies in a single stratum, by connectedness. If that stratum is not Δ_Γ we are in (D1).
   - Otherwise b̃ lies over closure(V_t) ∩ Δ_Γ = ∂V_t. Part 1, applied to b̃, gives the single loop-free vertex j' = c_b^{-1}(i) with P_{j'} ≅ Y_t.
   - The edge f at j is contracted by c_b (f ∉ S_b). So the vertex c_b(j) contains a contracted edge, hence c_b(j) ≠ i, i.e. j ≠ j'. ∎

**Lemma (Pinning).** Let 𝒰 be a finite set of pairs (E_0, u). Here E_0 is a 1-dimensional component of closure(V_0) ∩ Δ_{G}, G product type, u is a vertex of G, π_u(E_0) is a Teichmüller curve in the orbifold sense, and condition (O) of PR-E holds for (E_0, u). Put E_t := H_t(E_0). Suppose:

**(Pin)** For every t in a disc around 0 there is (E_0, u) ∈ 𝒰 such that Y_t is isomorphic, after relabelling, to a smooth component of a point of closure(π_u(E_t)) ∩ ∂M̄_u.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. By Lemma R\* (PR-E), closure(π_u(E_t)) = closure(π_u(E_0)) =: K_u for all t. Each K_u ∩ ∂M̄_u is finite.
2. So Y_t lies in a fixed finite set for t in the disc. By continuity (PR-A) it is constant there.
3. By holomorphy (PR-A) and the identity theorem, Y_t = Y_0 on Δ. ∎

The step-3 argument of Theorem P shows that **(T0) ⇒ (Pin)**. Proposition 3 shows that **(Pin) holds in the example of Section 2**, where (T0) fails. The following criterion abstracts Proposition 3. Like (T0), it is a condition on V_0 alone.

**Theorem 4 (twin criterion).** Let P_0 ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G'}. Let 𝒞 be the set of edge sets S ⊂ E(G') such that contracting E(G') \ S gives a graph identified with Γ, by an identification compatible with ξ_Γ, in which the preimage of vertex i is a single loop-free vertex j(S). Assume:
- **(Tw1)** There is a neighbourhood U of P_0 with (closure(V_0) \ V_0) ∩ U ⊂ ∂V_0 ∪ {P_0}.
- **(Tw2)** For all S ≠ S' in 𝒞:
  - j(S) ≠ j(S');
  - the vertex w = w(S, S') of Γ that contains j(S') under the contraction by S has an edge of G' among the edges contracted into it;
  - for every component E_0 of ∂V_0 with P_0 ∈ closure(E_0), π_w(E_0) is a Teichmüller curve in the orbifold sense satisfying (O).

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Transport.** By (R2), H_t maps closure(V_0) ∩ U onto a neighbourhood of P_t in closure(V_t), preserving strata. So near P_t, closure(V_t) \ V_t ⊂ ∂V_t ∪ {P_t}, and in Def(P_t) we have S̃ ∩ {all s_e = 0, e ∈ E(G')} = {0}.
   - G' and its combinatorics are the same at P_t as at P_0, because the stratum is preserved. The set 𝒞 depends only on G' and Γ.
2. **The branch β̃.** Take a branch β̃ of the preimage of ∂V_t through 0. By Lemma D(1), S_β ∈ 𝒞, and P_t has the component Y_t at j := j(S_β).
   - S_β ≠ E(G'), since P_t ∉ Δ_Γ.
3. **The branch b̃.** Pick e ∉ S_β. Lemma C1 of PR-C, as in Step 4 of Proposition 3, gives a boundary branch b̃ ≠ β̃ through 0 with e ∈ S_b.
   - By Step 1, b̃ lies over ∂V_t. So S_b ∈ 𝒞 by Lemma D(1), S_b ≠ S_β, and P_t has the component Y_t at j' := j(S_b) ≠ j, by (Tw2).
4. **The good vertex.** Let E_t = H_t(E_0) be the component of ∂V_t containing the image of β̃, so P_0 ∈ closure(E_0). Let w = w(S_β, S_b).
   - Along β̃ the w-coordinate converges to the stable curve assembled from the components of P_t over w, which include P_{j'} ≅ Y_t.
   - That curve has a node, by (Tw2). So it lies in closure(π_w(E_t)) ∩ ∂M̄_w, and Y_t is one of its smooth components.
5. **Conclusion.** This is (Pin) with 𝒰 the finite set of pairs (E_0, w) allowed by (Tw2), and it holds for every t. The Pinning Lemma concludes. ∎

**Check against Section 2.**
- G' is the chain A — e_1 — B — e_2 — C, and 𝒞 = {{e_1}, {e_2}} with j({e_1}) = A and j({e_2}) = C.
- w({e_1}, {e_2}) is the genus-4 vertex, which contains the edge e_2. Symmetrically, w({e_2}, {e_1}) contains e_1.
- π_2(∂V_0) = C is a Teichmüller curve. (Tw1) holds because closure(V_0) \ V_0 = ∂V_0 ⊔ {P_0}.
- So Proposition 3 is the case (Tw) of Theorem 4, modulo (O).

**What this means for MS5 and the chain.**
- MS5 (= (T0)) is not the right missing statement. It is false without smoothness (Section 2), and the problem's conclusion survives there via (Tw).
- The correct target is **(Pin)**, or the V_0-only disjunction **"(T0) or (Tw) holds at some point P_0 of closure(∂V_0)"**. Both are still open in general.
- Lemma D explains why a disjunction is natural. At a cusp, Lemma C1 always produces a second boundary branch b̃. If b̃ has the merge property, it is either a genuinely new boundary curve (D1, the (T0) mechanism) or ∂V_t again with a twin (D2, the (Tw) mechanism).
- What neither mechanism covers:
  - a cusp where no branch b̃ merges vertex j and no twin arises: the non-merge case of PR-C, still open;
  - (D1)-branches whose merged vertex is not a Teichmüller curve: positive area not established, (PA) of PR-F;
  - (D2)-twins whose host vertex w is not a Teichmüller curve or carries no node.


### PR-J. Theorems P′ and P″: pinning from a single branch, and the germ argument for transported branches (from round6_q8, verbatim, section 1)
## 1. The chain needs (T0) for one branch only (rigorous)

**Hypothesis (T0_1).** There are:
- a product-type stratum Δ_G;
- a point P_0 ∈ closure(∂V_0);
- ONE 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G with P_0 ∈ closure(E) \ E;

such that the following holds for every R ∈ 𝐂_E with ξ̄_G(R) = P_0 and every vertex u of G for which R_u has an irreducible component isomorphic to Y_0 (with its special points, in some order):
- (a) R_u ∈ ∂M̄_u;
- (b) π_u(E) is a Teichmüller curve in the orbifold sense.

(T0) as stated in the task implies (T0_1): take E = E^{(a)} for one a with P_0 ∈ closure(E^{(a)}) \ E^{(a)}. The difference is that (T0_1) puts no condition on the other components E^{(b)} through P_0. This matters in Section 4: it removes the obstruction that ∂V_0 itself, or another boundary curve, might pass through P_0 in the same stratum without a merge.

**Theorem P′.** Assume (R1), (R2), the hypotheses of the problem, (T0_1), and condition (O) of PR-E for the pairs (E,u) occurring in (b). Then Y_t = Y_0 for all t ∈ Δ.

*Proof.* I follow Theorem P (PR-D) and change only the choice of the component.

1. **Transport.** H_t is a homeomorphism closure(V_0) → closure(V_t). Both sets are closed in M̄_g, so H_t commutes with closures taken in M̄_g. Put P_t := H_t(P_0) and E_t := H_t(E). Then P_t ∈ closure(∂V_t) ∩ closure(E_t), for EVERY t. As in Step 1 of Theorem P, Y_t is (the normalization of) a component of P_t.
2. **Finite set.** Let U_E be the set of vertices u such that π_u(E) is a Teichmüller curve in the orbifold sense, and K_u := closure of π_u(E) in M̄_u. Let F be the set of n_i-pointed curves which, after some relabelling, are smooth components of points of K_u ∩ ∂M̄_u, for u ∈ U_E. F is finite, as in Theorem P. By Lemma R* (PR-E, using (O)), closure(π_u(E_t)) = K_u for all small t and all u ∈ U_E.
3. **Y_t ∈ F for small |t|.** Suppose t_n → 0 with Y_{t_n} ∉ F.
   - Since P_{t_n} ∈ closure(E_{t_n}), there are points of E_{t_n} converging to P_{t_n}. Their lifts lie in the compact space ∏M̄_w, so a subsequence of the lifts converges to some R^n ∈ 𝐂_{E_{t_n}} with ξ̄_G(R^n) = P_{t_n}.
   - Every component of P_{t_n} is a component of some R^n_w. Pass to a subsequence so that Y_{t_n} is a component of R^n_u for a fixed u, with a fixed relabelling σ, and R^n → R.
   - By Lemma R0 (applied to the single component E), R ∈ 𝐂_E, and ξ̄_G(R) = P_0 by continuity.
   - Y_0 is a component of R_u. The argument is the one in Theorem P, Step 3.
   - (T0_1) gives R_u ∈ ∂M̄_u and u ∈ U_E. Hence R^n_u ∈ ∂M̄_u for large n (Theorem P, Step 3), and R^n_u ∈ K_u. So Y_{t_n} ∈ F, a contradiction.
4. **Conclusion.** Y is continuous and takes values in the finite set F near 0, so it is constant there. By PR-A, Y is holomorphic, so Y is constant on Δ. ∎

The only change from Theorem P: the component a is fixed once and for all. The point P_{t_n} lies in the closure of the transported component E_{t_n} for every n by Step 1, so no choice among components through P_{t_n} is needed.

**Remark 1.1 (accidental copies; sketch only).** In Step 3 the vertex u is the one whose curve contains the component of P_{t_n} that *is* Y_{t_n}. So (a) and (b) are only needed for vertices u such that R_u contains a component that is a limit of the Y_{t_n}-components. Every such limit is the vertex-i coordinate of a point of the closure of ξ_Γ^{-1}(∂V_0) over P_0. The reason: (Y_{t_n}, c_n) ∈ closure(ξ_Γ^{-1}(∂V_{t_n})), and the family version of Lemma R0 for Δ_Γ applies.
- Call such components of P_0 *genuine*, and saturate this set under Aut(P_0).
- Then (T0_1) may be weakened further, to "every u such that R_u contains a genuine Y_0-component".
- This excludes *accidental* copies: components of P_0 that are isomorphic to Y_0 but arise, for example, from the degeneration of a varying factor at a cusp.
- Making "the component of R^n_u that is Y_{t_n} converges to a component of R_u" precise needs the finite cover of ∏M̄_w parametrizing (curve, chosen component). I have only sketched this, so I do not use it below.

### 1.2 A sharper version: one local branch and one vertex

**Setting.**
- Let Δ_{G'} be a product-type stratum. Then ξ_{G'} : ∏_{w∈V(G')} M_w → Δ_{G'} is a homeomorphism: it is continuous, bijective and proper, because by definition ξ_{G'}^{-1}(Δ_{G'}) = ∏ M_w and ξ̄_{G'} is finite.
- For P ∈ Δ_{G'} write P̂ := ξ_{G'}^{-1}(P).
- Let Δ_G be a stratum with Δ_{G'} ⊂ closure(Δ_G). A *pattern* is a contraction κ : G' → G, that is, a choice of a subset of edges of G' whose contraction gives G, together with an identification of the result with G.
- glue_κ(P̂) ∈ ∏_{w∈V(G)} M̄_w denotes the point whose w-coordinate is obtained by gluing the pieces P̂_x, x ∈ κ^{-1}(w), along the contracted edges.
- Every R ∈ ∏ M̄_w with ξ̄_G(R) = P and R_w ∈ M̄_w of the right topological type is glue_κ(P̂) for at least one, and at most finitely many, patterns κ. (Up to the finitely many identifications, this is the definition of the gluing maps.)

**Hypothesis (T0_β).** There are:
- product-type strata Δ_G and Δ_{G'} with Δ_{G'} ⊂ closure(Δ_G);
- a point P_0 ∈ closure(∂V_0) ∩ Δ_{G'};
- if P_0 ∉ ∂V_0, a local branch β of ∂V_0 at P_0 (if P_0 ∈ ∂V_0, then G' = Γ and β is not needed);
- a local branch β″ at P_0 of a 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, with P_0 ∉ Δ_G.

Let L_β be the limit at P_0 of the lift ξ_Γ^{-1}(β), and R_{β″} the limit at P_0 of the lift ξ_G^{-1}(β″). Both limits are unique, because the lift of a local branch is a holomorphic punctured disc (on the normalization) in a compact algebraic variety, and therefore extends. Let
- I′ := {i′ ∈ V(G') : κ_Γ(i′) = i for some pattern κ_Γ with glue_{κ_Γ}(P̂_0) = L_β};
- S := {κ(i′) : i′ ∈ I′, κ a pattern with glue_κ(P̂_0) = R_{β″}}.

Require, for every u ∈ S:
- (a) R_{β″,u} ∈ ∂M̄_u, equivalently some edge of G' at i′ is contracted by κ;
- (b) π_u(E) is a Teichmüller curve in the orbifold sense.

S consists of vertices u such that R_{β″,u} has a component isomorphic to Y_0. So (T0_β) is implied by (T0) (take a to be the index of E and R = R_{β″}). It is much weaker: one local branch, one lift, and only the vertices that can carry the *genuine* Y_0-component.

**Theorem P″.** Assume (R1), (R2), the hypotheses of the problem, (T0_β), and (O) for the pairs (E,u), u ∈ S. Then Y_t = Y_0 for all t.

*Proof.* The proof is that of Theorem P′, with the following additions.

1. **Transported branches.** By (R2), H restricted to (closure(V_0) ∩ U) × Δ, for a small neighbourhood U of P_0, is a stratum-preserving homeomorphism. So β_t := H_t(β) and β″_t := H_t(β″) are local branches at P_t := H_t(P_0) of ∂V_t and of E_t. Moreover P_t ∈ Δ_{G'} for all t, and P̂_t → P̂_0 because ξ_{G'} is a homeomorphism.

2. **The limit lifts are the branch lifts (germ argument).** Let 𝓦 be the analytic set of Lemma R0 for E, and 𝒵 := {(R′,t) : ξ̄_G(R′) = P_t}. Locally near (R,0), 𝒵 is a 1-dimensional set, finite over Δ.
   - By (R2), the lift N_{β″} of H((β″ \ {P_0}) × Δ) is open and closed in 𝓦 \ 𝒵 near (R,0).
   - An irreducible 2-dimensional germ stays connected after removing a proper analytic subset. So the closure of N_{β″} is a union of irreducible germs W of 𝓦 at (R,0).
   - For each such W, the fibre W_0 is of pure dimension 1, by Krull, since t is non-constant on W.
   - W_0 minus the finite set 𝒵_0 lies in N_{β″} ∩ {t = 0}, which is the lift of β″. So every point of the fibre over 0 of closure(N_{β″}) that lies over P_0 is R_{β″}.
   - The same argument in Δ_Γ shows that limits of the lifts L_t := lim_{β_t} ξ_Γ^{-1} are L_β.

3. **Identification of the vertex.** Let t_n → 0 with Y_{t_n} ∉ F, where F is now built from the pairs (E,u), u ∈ S.
   - Put R^n := R_{β″_{t_n}} and L^n := L_{β_{t_n}}.
   - By finiteness, pass to a subsequence along which the patterns are fixed: L^n = glue_{κ_Γ}(P̂_{t_n}) and R^n = glue_κ(P̂_{t_n}).
   - Then Y_{t_n} = P̂_{t_n, i′} with κ_Γ(i′) = i, and Y_{t_n} is a component of R^n_u for u := κ(i′).
   - In the limit, by continuity of glue_κ and Step 2: L_β = glue_{κ_Γ}(P̂_0) and R_{β″} = glue_κ(P̂_0). Hence i′ ∈ I′ and u ∈ S.
   - The rest is Step 3 of Theorem P′: (a) and (b) at u give R^n_u ∈ K_u ∩ ∂M̄_u for large n, so Y_{t_n} ∈ F, a contradiction. ∎

**Remark 1.2.** P_t ∈ Δ_{G'} together with the product type of Δ_{G'} is what lets us *track* the genuine Y-component. Accidental components of P_0 isomorphic to Y_0 play no role. Twins play a role only through the finite ambiguity of patterns, which is caused by automorphisms of P̂_0 compatible with the gluings.


## A suggested mechanism (the planner's sketch; you are free to discard it)
1. At t = 0, Proposition K (PR-H §3) gives, starting from ∂V_0, a compact connected set K_0 of boundary points (the "Y_0-network": the path-marked subsurface Σ_i stays pinched off and its component is ≅ Y_0) ending at a point Q_0 with a MERGE or MOV branch b. A MERGE gives a nodal puncture value containing a component ≅ Y_0 (Lemma C2), i.e. MS6 at t = 0; MOV at a puncture of b's piece also gives it; MOV at an interior point of b's piece needs extra care (there Q_0 is also a cusp of the previous network piece).
2. Transport to time t. The network is (up to finitely many points) a finite union of "STAY" pieces D on which the Σ_i-vertex is constant; by L1 it stays constant along D_t, with a holomorphic value z_D(t). At a junction point J, the multiset of components of H_t(J) can be read off from each branch through H_t(J): constants (holomorphic in t, by L1) and components of puncture values of non-constant vertices (t-independent, by L2). Matching these multisets as holomorphic functions of t (finitely many bijections; identity theorem) forces z_D ≡ z_{D′}, or z_D ≡ a fixed value (then Y is constant and you are done).
3. Twins (automorphisms of J or Q_0 swapping copies of Y_0 that separate for t ≠ 0) break the naive matching; Krull applied at each time t (every node of a boundary point is kept along some boundary branch; Lemma D of PR-I) plus a count of the components ≅ Y_t (for generic t, distinct holomorphic functions are distinct values) should keep at least one Y_t-copy on the network, which is all MS6 needs.
4. At Q_t = H_t(Q_0) the transported branch b_t lies in the same stratum; its merged (or moving) vertex is non-constant; the count at Q_t should place a Y_t-copy inside its puncture value.
An alternative purely at time t: at a cusp P_t of ∂V_t every component other than the Y_t-component is either a constant of ∂V_t (holomorphic in t) or a component of a fixed puncture value (L2); show from Krull and the connectedness of closure(V_t) \ V_t near the network that "every Y_t-copy stays isolated and constant everywhere" is impossible, using the t = 0 Proposition K.

## Reminder
- The target is MS6 exactly as stated, for every admissible V_0 and family. Partial results must be labelled partial.
- Never assume V_t totally geodesic for t ≠ 0. Total geodesy is available only at t = 0; information reaches t ≠ 0 only through (R1), (R2), L1, L2, Krull-type local arguments at time t, and analytic continuation in t.
- Beware: twins (several components ≅ Y_0 at a boundary point, exchanged by automorphisms that may disappear for t ≠ 0); limits of Teichmüller discs asserted to be Teichmüller discs without proof; "area leakage" into collars; claims that a merge must exist derived from purely local analysis (impossible: PR-C).
- Begin your answer with a plan/status line, and end with a clear list: proved / not proved / open.
