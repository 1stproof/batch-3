kind: attempt
Open question attempted: the run's missing statement MS5 (ledger entry 40). This query attacks its hardest step: the existence, on closure(∂V_0), of a point where the Y_0-component merges into a vertex carrying positive area of limiting generating differentials. By Lemma T′ (PR-F), positive area at the merged vertex gives clause (b).

## Task
Prove the following claim (H), which together with Lemma T′ of PR-F gives the statement MS5 below. Or give a counterexample to (H).

**(H).** Setting and notation as in MS5 below; "generating pair" and "positive area" are as defined in PR-F §0. There are a product-type stratum Δ_G and a point P_0 ∈ closure(∂V_0) such that the following hold. For every 1-dimensional component E^{(a)} of closure(V_0) ∩ Δ_G through P_0, every lift R of P_0 in 𝐂^{(a)}, and every vertex u of G with a component of R_u isomorphic to Y_0:
- (a) R_u is nodal;
- (area) at some point of E^{(a)} that lies on no other component, some sequence of generating pairs gives vertex u positive area.

(Then Lemma T′ makes π_u(E^{(a)}) an orbifold-unramified Teichmüller curve, which is clause (b) of MS5.)

Suggested first move, which you may discard if you say why. Work with the 2-planes Q_V(X) ⊂ Q(X) of generating differentials (dim 2, one direction of V_0 per projective class). As X → P ∈ closure(V_0) ∩ Δ_Γ, they converge in the Grassmannian bundle of the vector bundle of stable quadratic differentials (sections of ω^{⊗2}) over M̄_g to a 2-plane L(P).
1. Prove that the quadratic residues at the Γ-nodes restricted to L(P) have rank exactly 1 at generic P ∈ ∂V_0. Heuristic: ∂V_0 has codimension 1 in closure(V_0).
2. Prove that the kernel element q_∂ is a limit of generating pairs whose area does not leak into the collars of the Γ-curves. Then some vertex j carries positive area; j ≠ i by Lemma V.
3. Using the Teichmüller curve π_j(∂V_0-piece) (Lemma T′) and its cusps, find P_0 and a branch along which the Γ-edges at i are unpinched and the merged vertex contains part of the positive-area region.
4. Handle every lift R and every twin of Y_0, for example by showing Aut(P_0) permutes the relevant configurations.

A proof of (H) for only some V_0 does not answer the question. Report it as partial if that is all you find, and say exactly where the general case breaks.

## The statement MS5 (the target that (H) serves)

**Missing statement (MS5, ledger entry 40).** Setting:
- Let g ≥ 2 and let V_0 ⊂ M_g be a smooth closed 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric (every Teichmüller disc tangent to V_0 at a point of V_0 lies in V_0).
- Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product-type boundary stratum of M̄_g. Assume ∂V_0 := closure(V_0) ∩ Δ_Γ has dimension 1 and π_i(∂V_0) = {Y_0} for an index i with dim M_{g_i,n_i} > 0.

Definitions:
- A stratum Δ_G is of product type if the gluing map ξ_G: ∏_{w∈V(G)} M_w → Δ_G is bijective. Here M_w = M_{g_w,n_w}, and ξ̄_G: ∏ M̄_w → M̄_g is its extension.
- Let E^{(1)}, …, E^{(s)} be the 1-dimensional irreducible components of closure(V_0) ∩ Δ_G, and let 𝐂^{(a)} be the closure of ξ_G^{-1}(E^{(a)}) in ∏_w M̄_w.
- For a vertex u, "π_u(E^{(a)}) is a Teichmüller curve in the orbifold sense" means: f = π_u∘ν: Ẽ^{(a)} → M_u (ν the normalization) is non-constant, and there are
  - an orbifold structure on Ẽ^{(a)} with orbifold uniformization D → Ẽ^{(a)} and group Λ,
  - a homomorphism ρ: Λ → Mod_u,
  - and a ρ-equivariant holomorphic lift F: D → T_u of f that is an isometry from the Poincaré (Kobayashi) distance onto its image for the Teichmüller distance.

**Statement.** There exist a product-type stratum Δ_G and a point P_0 ∈ closure(∂V_0) with P_0 ∈ closure(E^{(a)}) \ E^{(a)} for some a, such that the following holds. For every a with P_0 ∈ closure(E^{(a)}), every R ∈ 𝐂^{(a)} with ξ̄_G(R) = P_0, and every vertex u of G such that some irreducible component of the stable curve R_u, with its special points in some order, is isomorphic to Y_0:
- (a) R_u ∈ ∂M̄_u (the Y_0-component is merged with other components at u);
- (b) π_u(E^{(a)}) is a Teichmüller curve in the orbifold sense.

(P_0 may lie on ∂V_0 itself when G is a proper contraction of Γ; it need not be a cusp.)


## How the statement is used (the chain) — check it, and say so if it is flawed
Readings of the problem's hypotheses adopted throughout (state them in any proof):
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G. Write H_t = H(·,t).

Derivation of the problem's claim:
1. By PR-A, t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}. So it is enough to show that Y is constant for t near 0.
2. Suppose V_0 satisfies the statement below, with stratum Δ_G and point P_0. For every pair (a,u) that occurs in it, π_u(E^{(a)}) is a Teichmüller curve in the orbifold sense.
3. By Lemma R* (PR-E), closure(π_u(H_t(E^{(a)}))) = closure(π_u(E^{(a)})) for all small t. This needs the orbifold-transport condition (O) of PR-E for those pieces. (O) is a separate open input of the chain, attacked elsewhere. It is automatic when M_u has no orbifold points. You do NOT need to prove (O) here.
4. Theorem P (PR-D) then shows that Y_t lies in a finite set for |t| small. Its hypothesis (T0) is exactly the statement below, with "Teichmüller curve" in the orbifold sense. Y_t is continuous, so it is constant near 0, and by step 1 it is constant on Δ.

So the statement below is the remaining input about the totally geodesic surface V_0 itself. It concerns V_0 alone, at t = 0. No family appears in it.

## Prior results (spliced verbatim from earlier answer files)
They assume readings (R1) and (R2) (stated with the statement's chain below). Results marked as cited from memory are not verified; re-check anything you use. Labels inside them (PR-1, PR-3, P-a, P-b, P-d, Lemma B′, etc.) refer to still earlier files; what you need from them is spliced here: PR-1 = holomorphy (PR-A below); Lemma B′ of PR-3 = PR-B below; Lemma C1/C2 of PR-3 = PR-C below; P-b Lemma 1 says the closure of ∂V_t = {Y_t} × C_t in deeper strata is {Y_t} × closure(C_t), so every point of closure(∂V_t) keeps the smooth component Y_t at vertex i. PR-6 is a converse (log vector fields) now known never to apply.

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

### PR-D. Lemma R, Lemma R0 and Theorem P (from round5_q1, verbatim). NOTE: Lemma R here tacitly takes orbifold homotopy classes / level lifts for granted; see PR-E for the precise orbifold hypothesis (O) under which it is proved. Theorem P's hypothesis (T0) is exactly the missing statement MS5 (stated above in this file).
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

## 2. Theorem P (pinning under a hypothesis on V_0 alone)

**Hypothesis (T0).** There are:
- a product-type stratum Δ_G, with E_0 := closure(V_0) ∩ Δ_G and its 1-dimensional components E_0^{(a)};
- a point P_0 ∈ closure(∂V_0) ∩ (closure(E_0) \ E_0);

such that the following holds. Take any a with P_0 ∈ closure(E_0^{(a)}), any R ∈ 𝐂_0^{(a)} with ξ_G(R) = P_0, and any vertex u of G such that R_u has a smooth component isomorphic to Y_0 (as an n_i-pointed curve, after some relabelling of the special points). Then:
- (T0-a) R_u ∈ ∂M̄_u, i.e. the component Y_0 is "merged" with other components in the vertex u;
- (T0-b) π_u(E_0^{(a)}) is a Teichmüller curve.

**Theorem P.** Assume (R1), (R2), the hypotheses of MS4, and (T0). Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*

**Step 1 (transported point).**
- Put P_t := H_t(P_0). Since H_t is a stratum-preserving homeomorphism, P_t ∈ closure(∂V_t) ∩ closure(E_t^{(a)}) \ Δ_G whenever P_0 ∈ closure(E_0^{(a)}) (Lemma B′ of PR-3).
- **Y_t is a component of P_t.** Pick c_n ∈ C_t with ξ_Γ(Y_t, c_n) → P_t. Pass to a subsequence with c_n → c in ∏_{j≠i} M̄_j. By continuity of ξ_Γ, P_t = ξ_Γ(Y_t, c). The normalization of ξ_Γ(Y_t, c) contains Y_t, with its n_i special points, as a component.

**Step 2 (the finite set F).**
- Let 𝒰 be the set of pairs (a, u) with π_u(E_0^{(a)}) a Teichmüller curve. Let K_u^{(a)} be the closure of π_u(E_0^{(a)}) in M̄_u. It is a compact irreducible curve meeting M_u, so K_u^{(a)} ∩ ∂M̄_u is finite.
- Let F ⊂ M_{g_i,n_i} be the set of all n_i-pointed curves that are, after some relabelling, a smooth component of a point of K_u^{(a)} ∩ ∂M̄_u, for some (a, u) ∈ 𝒰.
- F is finite: there are finitely many points, finitely many components each, and finitely many relabellings.
- By Lemma R, K_u^{(a)} = closure(π_u(E_t^{(a)})) for every t and every (a, u) ∈ 𝒰.

**Step 3 (Y_t ∈ F for small |t|).**
- Suppose not. Then there are t_n → 0 with Y_{t_n} ∉ F.
- *Lifts R^n.* Pass to a subsequence and fix a with P_{t_n} ∈ closure(E_{t_n}^{(a)}) for all n (finitely many choices of a). By compactness of ∏M̄_u there is R^n ∈ 𝐂_{t_n}^{(a)} with ξ_G(R^n) = P_{t_n}: take a limit of lifts of points of E_{t_n}^{(a)} converging to P_{t_n}.
- *The vertex u.* The components of P_{t_n} are the components of the R^n_u, u ∈ V(G). By Step 1, Y_{t_n} is a component of some R^n_{u_n}. Pass to a subsequence so that u_n = u and the relabelling σ are fixed, and R^n → R.
- *R satisfies the hypotheses of (T0).* (R^n, t_n) ∈ 𝓦^{(a)}, so (R, 0) ∈ 𝓦^{(a)}. By Lemma R0, R ∈ 𝐂_0^{(a)}. Also ξ_G(R) = P_0, by continuity of ξ_G and of H.
- *Y_0 is a component of R_u.* Pass to a subsequence so that all R^n_u lie in one stratum of M̄_u, whose normalization is a product of moduli spaces. Choose lifts in that product, with the coordinate of the component Y_{t_n} equal to σ(Y_{t_n}). These lifts converge, after a further subsequence, to a lift of R_u whose corresponding coordinate is σ(Y_0) ∈ M_{g_i,n_i}, a smooth curve. So Y_0 is a component of R_u.
- *Applying (T0).* (T0-a) gives R_u ∈ ∂M̄_u, and (T0-b) gives (a, u) ∈ 𝒰.
- *R^n_u is a boundary point for large n.* If R^n_u ∈ M_u (smooth) for infinitely many n, then R^n_u = σ(Y_{t_n}) for those n, since a smooth curve has a single component. Its limit would be σ(Y_0) ∈ M_u, contradicting R_u ∈ ∂M̄_u. So R^n_u ∈ ∂M̄_u for large n.
- *Contradiction.* R^n_u ∈ closure(π_u(E_{t_n}^{(a)})) = K_u^{(a)} by Step 2. So R^n_u ∈ K_u^{(a)} ∩ ∂M̄_u, hence Y_{t_n} ∈ F. This contradicts the choice of t_n.

**Step 4 (conclusion).**
- t ↦ Y_t is continuous (PR-1) and takes values in the finite set F on the disc |t| < ε. So it is constant there.
- Y is holomorphic on Δ (PR-1), so by the identity theorem Y_t = Y_0 on all of Δ. ∎

**Remarks on Theorem P.**
- (T0) concerns V_0 only, and only its boundary, so it is a statement where total geodesy of V_0 is available.
- Hypothesis (ii) is never used, and neither is any total-geodesy property of V_t.
- Compared with PR-3 Theorem E, Theorem P:
  - drops (H2′) and the citations (K) and (Ct) (Lemma R uses Royden, Thurston and Imayoshi–Shiga instead);
  - handles the non-injectivity of the gluing map over deeper strata, which Theorem E glossed over;
  - does not need the combinatorics of the specialization at P_t to be "the same" as at P_0, because (T0) is imposed on all lifts R at t = 0 and the limit argument transfers it.
- The covering-construction model of round4_q3 (D) is reported there to satisfy the analogue of (T0): there E_0 (only x → 1) is a Teichmüller curve passing through the corner where the constant factor appears. I have **not** re-verified this, and in particular not (T0-a) and (T0-b) for every lift R.

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

### PR-F. Positive area forces Teichmüller curves; the constant vertex has no area; reduction of (T0) to a positive-area merge; marked covering model; a Jenkins–Strebel route with gaps (from round5_q5, verbatim; (F2) is only sketched there)
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
- (area) at some point P' of E_0 (not lying on another component of closure(V_0) ∩ Delta_{G''}) some sequence of generating pairs gives v positive area.

**Proposition 4.1.** (T0\*) implies (T0)(a), and also (T0)(c).

*Proof.*
- (c): P_0 is a cusp by construction.
- (a): Lemma T' applied at P' (stratum G'', vertex v) yields the irreducible component of closure(V_0) ∩ Delta_{G''} through P', which is the component E_0, with pi_v|_{E_0} orbifold-unramified onto the Teichmüller curve of (Y_v, eta_v); lifted to universal covers it is an isometry onto a Teichmüller disc. The remaining requirements of (a) (cusp, stratum incidences, merge) are in (T0\*). ∎

Similarly, **(T0\*\*)**: two pieces E_0, E'_0 as in (T0)(b), vertex i intact in both strata, vertex i carrying positive area at some point of each, and pi_i(E_0), pi_i(E'_0) without common component through Y_0. Then (T0)(b) holds: by Lemma T', pi_i(E_0) and pi_i(E'_0) are Teichmüller curves, and their closures contain Y_0 because P_0 ∈ closure(E_0) and vertex i of P_0 is Y_0 (P-b Lemma 1).

**What remains of (T0).** Lemma T' converts the analytic half of (T0) (the "isometric onto a Teichmüller disc" clauses) into a statement about *where area sits*. The genuinely open part is combinatorial-dynamical: existence of a cusp with a merge branch on which the merged vertex carries positive area for some generating sequence. Lemma V shows that vertex i itself is never a positive-area vertex along ∂V_0, so vertex i must be "lifted to positive area" when it merges, which is what happens in the covering model (Section 5).

---

## 5. The covering-construction model (partial; proved for the marked model)

**Setting (marked model).** Let H be a component of a Hurwitz space of covers f: X -> P^1 of fixed topological type, branched over (at most) five points p_1..p_5, with **all preimages of the p_k marked**; V_0 ⊂ M_{h,N} the image of H. (This includes the task's example: z -> z^d, base (0,∞,1,x,y), V_0 ⊂ M_{0,3d+2}.) V_0 is totally geodesic: pulling back q on (P^1; p_1..p_5) (simple poles at the p_k) gives integrable f^*q, and pullback is an isometric embedding of Teichmüller spaces (classical; cited). Its closure is the image of the Harris–Mumford space Hbar of admissible covers, which is finite over Mbar_{0,5} (cited from memory).

**Proposition 5.1.** In the marked model, (T0\*) holds at *every* cusp P_0 of ∂V_0; hence (T0)(a) and (c) hold.

*Proof.*
1. *No contraction.* Every source component over a base component with 3 special points has at least 3 special points (Riemann–Hurwitz: a degree-k cover of a 3-pointed P^1 by P^1 has 3k - (2k-2) = k+2 preimages, and higher-genus components are stable already), all of which are marked or nodes. So the source of an admissible cover is stable, and the map Hbar -> Mbar_{h,N} sends a cover to its source without contraction; each source node lies over exactly one base node.
2. *Gamma-edges lie over one base node.* Hbar -> Mbar_{0,5} is finite, so the image of ∂V_0 in Mbar_{0,5} is 1-dimensional, hence an open part of a boundary divisor D_S ≅ M_{0,4}. The nodes of Gamma are exactly the source nodes over the node S.
3. *Cusps.* closure(∂V_0) maps onto closure(D_S) = D_S ∪ {three points}, so cusps exist ((c)). Let P_0 be a cusp and h_0 a point of Hbar over P_0 in the closure of the preimage of ∂V_0. Its base point lies in D_S ∩ D_T for a second divisor D_T (it is not in the open part of D_S, since P_0 has extra nodes).
4. *Merge.* Mbar_{0,5} has simple normal crossings at D_S ∩ D_T, with local equations s_S, s_T. On Hbar (locally a finite quotient of a smooth germ with coordinates tau_S, tau_T, s_S = tau_S^a, s_T = tau_T^b; Harris–Mumford, cited), the smoothing parameter of a source node over S is a power of tau_S, of one over T a power of tau_T. Let b be the branch {tau_T = 0} through h_0 and E_0 its image, a 1-dimensional piece of closure(V_0) ∩ Delta_{G''} (finite map). On E_0, tau_S ≠ 0, so every node over S, in particular every Gamma-edge at vertex i (vertex i has at least one edge since Gamma is connected with >= 2 vertices), is smoothed. So (merge) holds.
5. *Area.* The merged vertex v maps to a component of the base curve on D_T. It is not the 3-pointed bubble: otherwise pi_v would be constant along E_0 (finitely many covers of a fixed 3-pointed curve), contradicting Lemma C2 of PR-3. So v maps to the 4-pointed component B_4. Choose base differentials q_n on (P^1; p_1..p_5) converging to the base point of a generic point of E_0 with a positive-area limit on B_4: if D_T = D_{ab} (p_a, p_b collide), take q_n with simple poles at the other three points and at p_a only, holomorphic at p_b (allowed: at most simple poles at marked points); the limit on B_4 has simple poles at its four special points, hence finite positive area. Then f^*q_n are generating pairs for V_0 and v carries positive area (the limit is f^* of the limit on B_4, area multiplied by the degree). So (area) holds. ∎

**Caveat (the problem's actual setting).** In the problem, V_0 ⊂ M_g has *no* marked points. For a covering locus in M_g, preimages of branch points are unmarked, and source components can become unstable (e.g. a rational component over the middle component of the base chain at D_S ∩ D_T, totally ramified over both nodes, has only two special points) and are contracted. A contracted bridge between a node over S and a node over T produces a stabilised edge with smoothing parameter tau_S^alpha tau_T^beta, pinched on *both* branches at P_0. If all edges at vertex i are of this type at every cusp, (merge) fails at every cusp for the branch over D_T. I have not found an example where this happens for all cusps, nor proved it cannot; so even for covering constructions in M_g, (T0) is not proved here. (The task's own example lives in M_{0,3d+2}, where Proposition 5.1 applies.)

---

## 6. A route to (T0\*) in general (sketch, not a proof)

Assume (PA) at a point P of ∂V_0, with positive-area vertex j ≠ i, limit eta_j; C = pi_j(E) a Teichmüller curve (Prop. C). Pick a cusp of C, i.e. a periodic direction of eta_j (Veech dichotomy for the lattice surface (Y_j,eta_j)), made horizontal. Then:
1. P_∞ := lim_{s->∞} phi(diag(e^{-s},e^s)) is a cusp of ∂V_0 (Lemma T' (3)), at which the cores of the horizontal cylinders of eta_j are pinched in addition to Gamma.
2. Second branch, heuristically: for fixed n, the Teichmüller ray from (X_n, q_n) in the same direction, if q_n is horizontally Jenkins–Strebel, converges in Mbar_g to the curve obtained by pinching exactly the horizontal cylinder cores of q_n (Masur's theorem on Jenkins–Strebel rays; cited from memory). The Gamma-curves at vertex i are short on X_n but, by Lemma V, sit in a region of zero relative area; if they are not horizontal cylinder cores of q_n, the limits Z_n lie in strata where those Gamma-edges are unpinched, and as n -> infinity they should accumulate on the cusp P_∞ along a merge branch. The merged vertex would then contain pieces of the top level, which suggests positive area.
3. Gaps: (a) existence, near P, of generating pairs q_n that are horizontally Jenkins–Strebel (true on a dense set of a GL(2,R)-orbit closure only if periodic directions of the whole surface, not just of eta_j, can be arranged; rank-2 orbit closures contain horizontally periodic surfaces (Smillie–Weiss), but density near a given boundary point is not clear); (b) interchanging the limits n -> infinity and s -> infinity; (c) excluding that the Gamma-curves at vertex i are themselves horizontal cylinder cores of q_n (they are short curves around a zero-area region, which in the multi-scale picture are vertical edges, poles of order >= 3 at the lower end, suggesting they are not cylinder cores, but horizontal edges at vertex i are not excluded); (d) proving (PA).

### PR-G. The automorphism (twin) issue and merges in cyclic covering constructions (from round5_q8, verbatim; 'Theorem M' there is a pinning theorem for a thrice-punctured merged curve, PR-3 Theorem E is an older version of Theorem P)
## 3. A gap in PR-3 Theorem E: hypothesis (M2) is needed
- PR-3's proof of Theorem E (step 5) takes for granted that "the component of P_t at vertex i lies in the merged vertex v" holds for every t because it holds at t = 0. That identification is made in an orbifold chart and is defined only up to Aut(P_t).
- When Aut(P_0) ⊋ Aut(P_t), the transported branch b_t may pass through a *different* lift kP̂ of P_t than β_t does.
- In that case, geometrically, E_t merges a former "twin" component x_{k(i)} of P_t, which at t = 0 was isomorphic to Y_0, instead of the Y_t-component.
- I see no local or topological argument excluding this. Theorem E should therefore carry a hypothesis such as (M2), for example "Aut(P_0) fixes the component Y_0".
- This scenario is also a possible counterexample mechanism, to be checked: a cusp whose symmetry is broken in the family.

## 4. Corollary N: covering constructions from M_{0,5}

**Setting.**
- Φ : M_{0,5} → M_g is a cyclic covering construction, sending (P^1, a_1, …, a_5) to the curve y^d = ∏ (x − a_j)^{k_j}.
- V_0 = Φ(M_{0,5}) is assumed smooth, as the problem requires.
- V_0 is totally geodesic: Teichmüller maps lift to covers, and the lifted map is extremal (standard; cited from memory).
- For abelian covers the admissible cover over a stable 5-pointed tree is unique, so Φ extends to Φ̄ : M̄_{0,5} → M̄_g, sending a stable curve to the stable model of the admissible cover (Harris–Mumford; cited from memory). Then closure(V_0) = Φ̄(M̄_{0,5}).

**Corollary N.** In this setting:
- Suppose that, for some boundary divisor D_{12}, say, with Φ̄(D_{12}°) ⊂ ∂V_0, the constant vertex i is a component Ŷ of the admissible cover lying over the 3-pointed bubble A ∋ a_1, a_2. Call this condition (B).
- Then there is a cusp P_0 = Φ̄(D_{12} ∩ D_{kl}), with {k,l} ⊂ {3,4,5}, at which (M1) and (M3) hold, with E_0 the component containing Φ̄(D_{kl}°).
- Hence, if (M2), (M4) and (M5) also hold at that cusp, Y_t is constant.

*Proof.*

**(a) The lifts.**
- Near the point D_{12} ∩ D_{kl} of M̄_{0,5}, take coordinates (λ_1, λ_2) with D_{12} = {λ_1 = 0} and D_{kl} = {λ_2 = 0}.
- The family of stable models over this polydisc is pulled back from the Kuranishi family by a classifying map κ, by versality.
- Then β̃ := κ{λ_1 = 0} and b̃ := κ{λ_2 = 0} are lifts through the common point κ(0) = P̃_0.

**(b) Monodromy at the cusp.** Over the chain A–B–C at the cusp:
- A carries a_1, a_2 and the node q; B carries a_m, with {m} = {3,4,5} \ {k,l}; C carries a_k, a_l.
- Let σ_3, σ_4, σ_5, σ_q be the monodromies of the main-side cover, the one over the sphere carrying a_3, a_4, a_5, q. Their product is 1.
- An edge of Γ at i corresponds to a node y of Ŷ over q, that is, to a cycle c of σ_q.
- Let W_B be the component over B at y. It is unstable if and only if it is a *bridge*: genus 0, with one preimage of each node. Then W_B, as a cover of B, has sheet set equal to c, and σ_r is a full cycle on c. Riemann–Hurwitz then gives 2·genus(W_B) = |c| − #cycles(σ_m|_c). So W_B is a bridge if and only if c is ⟨σ_q, σ_m⟩-invariant and σ_m|_c = id.
- If W_B is stable, then the node y is an edge of G' from i to W_B. It is smoothed along D_{kl}, where A ∪ B is smoothed. So (M1) holds with c_b ∋ i.

**(c) Some choice of m gives a merge.**
- Suppose, for contradiction, that W_B is a bridge for all three choices of m.
- Then c is invariant under σ_3, σ_4, σ_5, which act trivially on it. So σ_q|_c = (σ_3σ_4σ_5)^{-1}|_c = id, and |c| = 1.
- The main-side component at y is then a degree-1 rational tail with a single special point. It is contracted by stabilization, so y is not an edge of Γ. Contradiction.
- Vertex i has at least one Γ-edge. Otherwise Δ_Γ = M_{g_i,n_i} and ∂V_t would be a point, contradicting dim ∂V_t = 1. So some m gives the merge.

**(d) (M3).**
- Φ̄ maps D̄_{kl} ≅ P^1 onto closure(E_0), so the normalization of closure(E_0) has genus 0.
- Each puncture of Ẽ_0 has a preimage among the 3 special points of D̄_{kl}: D_{kl}° maps into Δ_G, and the map is surjective. Hence Ẽ_0 has at most 3 punctures.
- f_0 is non-constant (Step 5 above). By (M4) and the Liouville-type fact, Ẽ_0 has at least 3 punctures.
- Hence Ẽ_0 has exactly 3 punctures. ∎

**Remark.** Hypothesis (B) excludes the case where the constant factor is a component over the 4-pointed side that happens to be isotrivial. I have not analysed that case.
