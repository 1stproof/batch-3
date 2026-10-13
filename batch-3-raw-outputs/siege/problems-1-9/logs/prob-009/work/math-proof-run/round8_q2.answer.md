# round8_q2 — answer (MS8)

**Status line.** MS8 is NOT proved in full here, and I found no counterexample. What this file contains:
- (A) **Lemma U** (proved). Under (Rig), every 2-dimensional component W of every lifted family has one moving set M_W and one image curve K_W, shared by *all* components of *all* fibres W_t, t ∈ Δ, including t = 0. So every piece at every time has the form K_W × {point}. This repairs the earlier worker's Lemma 6, which is unjustified for non-product strata. It also removes, under (Rig), the non-product pathology of R7-5 §1.4.
- (B) **Theorem 1** (generic-time trichotomy; re-proved and checked). At every t outside a discrete set Z, no Y_t-copy merges or moves at a puncture.
- (C) **Theorem S** (new; conditional, partial). The twin problem reduces to a monodromy question: do curves of V_τ with *new* automorphisms accumulate on Proposition K's continuum as τ → 0? Under the hypotheses (NB) and (NB_∂) of §4 (both conditions on the family near K_0), MS8 holds whenever Proposition K ends in MERGE or in puncture-MOV. No (Lock) or "no twins" hypothesis is needed. Proved modulo Proposition K in the form (K\*) and the routine chart facts (Ch), (Tr) of R7-6.
- (D) Crossing endpoint (interior-MOV): still open. In that case Y(Δ) is contained in a fixed algebraic curve (Proposition 7). Corollary S′: under (NB) and (NB_∂), either Y is constant or Y(Δ) lies in one of finitely many fixed curves pr_y(K_W).
- Open: (NB), (NB_∂) and the crossing alternative (§7, Open questions A–C).

Readings (R1), (R2) and the notation of the task file are used throughout.

---

## 1. Conventions and cited facts

- Classes of pointed curves are compared in the coarse space 𝔐 := M_{g_i,n_i}/S_{n_i}. "≅ Y" means equal class.
- For a stable graph G, 𝓦_G ⊂ ∏_w M̄_w × Δ is the lifted family of R7-5 (P2). It is analytic by (R1) and proper over Δ. "W" always denotes a 2-dimensional irreducible component of some 𝓦_G.
- By R7-5 (P4), applied at every t (the argument is symmetric in t by (R2), and closure(V_t) is compact analytic by (R1)): every fibre W_t is non-empty and of pure dimension 1. Each 1-dimensional component D of W_t is the closure of a piece E at time t, so (Rig) applies to E. Write M(D) := M(E) and K(D) := K(E).
- Cited from memory (standard):
  - **Remmert's proper mapping theorem.**
  - **Cartan–Remmert.** For a holomorphic map Φ of complex spaces, {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
  - **Stein factorization** (Grauert–Remmert). A proper holomorphic map f: X → S factors as X → T → S, with X → T proper, surjective and with connected fibres, and T → S finite. If X is normal, so is T.
  - **Normal surfaces** have isolated singularities.

## 2. Lemma U (uniformity under (Rig)) — proved

**Lemma U.** Assume (R1), (R2) and (Rig). Let W be a 2-dimensional irreducible component of 𝓦_G. There are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, with the following property. For **every** t ∈ Δ and **every** 1-dimensional component D of W_t:
- M(D) = M_W and K(D) = K_W;
- every vertex u ∉ M_W is constant on D;
- D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*

**Step 1 (generic moving set).** Let n: W^ν → W be the normalization, a normal surface. Let W^ν →a T →b Δ be the Stein factorization of t∘n, which is proper. T is a normal, hence smooth, curve and b is finite.
- **Critical values are discrete.** Let C be an irreducible curve of critical points of a on W^ν_reg. Then d(a|_C) = 0, so a is constant on C. The singular points of W^ν are isolated. Hence the set of critical values of a (images of Sing W^ν, of isolated critical points, and of critical curves) is discrete in T.
- **Generic fibres are irreducible.** For τ ∈ T outside a discrete set, a^{-1}(τ) is a smooth, compact, connected curve, hence irreducible.
- **Fibres of W.** Since n is finite and surjective, for every t, W_t = ⋃_{τ ∈ b^{-1}(t)} n(a^{-1}(τ)). Every component of W_t is the image of a component of some a^{-1}(τ). For generic t the components of W_t are exactly the irreducible curves n(a^{-1}(τ)), τ ∈ b^{-1}(t).
- **The dichotomy for a vertex u.** Put Φ_u := (pr_u∘n, a): W^ν → M̄_u × T and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert.
  - If R_u = W^ν: let K be a component of a fibre a^{-1}(τ) and x ∈ K a point on no other component. The Φ_u-fibre through x lies in a^{-1}(τ) and is 1-dimensional at x, so it contains the germ of K at x. Hence pr_u is constant on K. So u is constant on every component of every fibre of a, and therefore on every component of every W_t.
  - If R_u ≠ W^ν: then dim R_u ≤ 1. Every fibre component on which pr_u is constant lies in R_u, and the components of R_u are locally finite. So this happens only for τ in a discrete subset of T.
- Put M_W := {u : R_u ≠ W^ν}. Then for t outside a discrete set Z_W ⊂ Δ, every component of W_t has moving set exactly M_W. For every t and every component of W_t, every u ∉ M_W is constant on it. M_W ≠ ∅, since components of W_t are curves.

**Step 2 (one image curve).** Let Σ := (pr_{M_W}, t)(W) ⊂ ∏_{u∈M_W} M̄_u × Δ. It is closed, analytic and irreducible (Remmert; the map is proper on W). It has dimension 2, since t is non-constant on it and its generic fibres are curves.
- For t ∉ Z_W and a component D of W_t, pr_{M_W}(D) is the closure of the image of the piece, i.e. K(D).
- By (Rig), K(D) belongs to the finite list {α^{-1}K : α ∈ Aut(G), (G, αM_W, K) ∈ 𝒦}, with factors relabelled by α. Call its members K_1, …, K_N.
- So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
- Σ is irreducible of dimension 2, so it lies in one K_j × Δ, and equals it since both are irreducible of dimension 2. Put K_W := K_j.
- For each u ∈ M_W, pr_u|_{K_W} is non-constant, because K_W = K(D) for a generic-time component D with u ∈ M(D).

**Step 3 (all times).** Let t be arbitrary and D a component of W_t.
- By Step 1 the vertices outside M_W are constant on D. So D ⊂ pr_{M_W}^{-1}(pr_{M_W}(D)) ∩ {coordinates outside M_W constant}.
- pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, so it is a point or all of K_W. If it were a point, every coordinate would be constant on the curve D, which is absurd.
- So pr_{M_W}(D) = K_W. Every u ∈ M_W is non-constant on D (end of Step 2), so M(D) = M_W and K(D) = K_W.
- D is an irreducible curve inside the irreducible curve K_W × {c_D}, so the two are equal. Here c_D ∈ ∏ M_u, because D is the closure of a subset of ∏_w M_w and the coordinates of c_D are constant on D. ∎

**Corollaries.**
- **U1 (L1′ with its converse; no non-product pathology).** For each W and vertex u, the following are equivalent:
  - u is constant on one component of one fibre;
  - u ∉ M_W;
  - u is constant on all components of all fibres.

  In particular the situation of R7-5 §1.4 (u constant on E_0 but non-constant on σE_0 inside the same W) cannot occur under (Rig). Consequently, for a component W' through a point p obtained from W by ρ ∈ Aut(G): M_{ρW} = ρM_W and K_{ρW} = ρK_W.
- **U2 (t-independent image curves; the earlier worker's Lemma 6, repaired).** The partial file's Lemma 6 asserts that "M is the same for all t by L1′". L1′ gives only one direction, and for non-product G the fibres of W can have components with different moving sets unless (Rig) is used as above. Lemma U is the correct statement.
- **U3 (puncture values).** For each W, the values pr_{M_W}(ν(p)) at punctures p of components of W_t lie in K_W ∩ ∂(∏ M̄_u). This is a finite set independent of t.
- **U4 (constant-vertex value curves).** For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t.

## 3. Generic times and the trichotomy (Theorem 1) — proved

From now on assume, for contradiction, that **Y is non-constant**. Y: Δ → 𝔐 is holomorphic by PR-A, so its graph is an irreducible curve.

**The finite set 𝔉 ⊂ 𝔐 (independent of t).**
- Let 𝒫_1 be the set of points of K ∩ ∂(∏_{u∈M} M̄_u), over all (G, M, K) ∈ 𝒦 and all Aut(G)-relabellings. It is finite: K is an irreducible compact curve not contained in the boundary.
- Let A_1 be the set of classes of the smooth components, with their special points, of all coordinates of points of 𝒫_1.
- Let 𝒫_2 be the set of points κ ∈ K such that the class of some coordinate pr_z(κ), z ∈ M, lies in A_1. It is finite, because pr_z|_K is non-constant for z ∈ M (Lemma U).
- Let 𝔉 be the set of classes of the smooth components of all coordinates of the points of 𝒫_1 ∪ 𝒫_2.

**The set Z.** Z is the set of t ∈ Δ such that one of the following holds:
- Y_t ∈ 𝔉;
- (Y_t, t) lies on the image in 𝔐 × Δ of some curve Γ_{W,u} (u ∉ M_W, M_u of type (g_i,n_i)) that is not the graph of Y.

Each W, and each such pair (W,u), contributes a discrete set: in the first case because Y is non-constant, in the second because two distinct irreducible curves meet discretely. The components W are locally finite over Δ. Hence **Z is discrete** in Δ.

Call a pair (W,u) with Γ_{W,u} ↦ graph(Y) a **Y-vertex**.

**Theorem 1.** Let t ∉ Z, Q ∈ B_t, q a lift of Q in Def(Q), and y a Y_t-copy of q (comp_y(q) ≅ Y_t). Let b̃ be a lifted branch through q of a branch b of B_t at Q. Let E be the piece of b at time t, with graph G_b and component W ⊃ E. Then exactly one of the following holds.
- **(STAY)** Every edge at y is pinched along b̃, y is a constant vertex of E, and (W, y) is a Y-vertex.
- **(IMOV)** Q is an interior point of E (so Q ∈ Δ_{G_b}), and y ∈ M_W. Moreover, for every z ∈ M_W and every other lifted branch b̃′ through q, z is neither merged along b̃′ nor non-constant at a puncture along b̃′.

In particular, a Y_t-copy is never merged along a branch (**MERGE excluded**), and never intact and non-constant at a puncture (**puncture-MOV excluded**).

*Proof.*
1. **Merge.** Suppose some edge at y is unpinched along b̃. By R7-1 Lemma 1(a) (= R7-4 Lemma 1), the point p of Ē over Q is a puncture, the vertex u ∋ y of G_b is non-constant, and comp_y(q) is a component, with the same special points, of f_u(p).
   - By Lemma U, u ∈ M_W and pr_{M_W}ν(p) ∈ 𝒫_1.
   - So Y_t ∈ A_1 ⊂ 𝔉, contradicting t ∉ Z.
2. **Puncture-move.** Suppose y is intact, {y} is non-constant, and Q ∉ Δ_{G_b}. Then p is a puncture and f_y(p) = comp_y(q) (R7-1 Lemma 1(b)). So Y_t ∈ A_1, again a contradiction.
3. **Constant.** Suppose y is intact and constant on E. Its value is comp_y(q) ≅ Y_t, so (Y_t, t) lies on the image of Γ_{W,y}. Since t ∉ Z, Γ_{W,y} maps onto graph(Y): this is STAY.
4. **Remaining case.** Here y is intact and non-constant, and Q ∈ Δ_{G_b}. So y ∈ M_W, and κ := pr_{M_W}(lift of Q) ∈ K_W.
   - Suppose some z ∈ M_W were merged, or moving at a puncture, along another branch b̃′ through q. Then, as in 1–2, comp_z(q) = pr_z(κ) has class in A_1. So κ ∈ 𝒫_2, and Y_t ≅ pr_y(κ) lies in 𝔉, a contradiction. ∎

**Remark.** Theorem 1 never compares two copies. At a generic t, *every* Y_t-copy obeys it, whatever the automorphisms of Q. Twins matter only when information is transported between t = 0 (where total geodesy is available) and generic t. That is the subject of §4.

## 4. Theorem S: the twin problem is a monodromy problem (conditional; partial)

### 4.1 Where the twin problem sits

Proposition K follows the subsurface Σ_i ⊂ S_g with a **marking** along an interior path γ ⊂ V_0, i.e. a lift γ̃ to T_g. R7-6 tried to carry this to time t by transporting along τ ↦ H_τ(γ(s)). As the planner noted, this needs the transported markings to be coherent in s, i.e. the square

 F(s,τ) := H_τ(γ(s)),  s ∈ [0,1], τ ∈ [0,t],

must lift to T_g × Δ. Two markings of the same surface differing by a mapping class g send Σ_i to different subsurfaces. In chart terms, the merged copy and the copy that stays ≅ Y_t differ by an automorphism α of the end point. This is exactly the twin swap of R7-2 §4.1 and R7-3 §4. So the twin problem is the monodromy of ∂F, and it can come only from **branch points of the covering 𝒱̃ → 𝒱** met by F. Below I show:
- (i) branch points over t = 0 are harmless, even if every curve of V_0 has automorphisms that disappear for t ≠ 0;
- (ii) the remaining ones matter only if they accumulate on K_0 × {0}.

That is hypothesis (NB). A similar issue inside boundary strata (Aut(G)-branching of the lifted boundary families) is controlled by Lemma U up to a coincidence condition, (NB_∂).

### 4.2 Definitions and the input from t = 0

- 𝒱̃ ⊂ T_g × Δ is the preimage of 𝒱 (Mod_g acts trivially on Δ). A point v ∈ 𝒱 is **regular** if it has a neighbourhood U such that every connected component of the preimage of U maps homeomorphically onto U. Over the open set 𝒱^reg of regular points, 𝒱̃ → 𝒱 is a covering map. The preimage of a small neighbourhood of any point of 𝒱 is a disjoint union of neighbourhoods of the (finitely many modulo Mod_g) fibre points, because Mod_g acts properly discontinuously.
- **Input (K\*+).** This is (K\*) of R7-6 §2.0 (Proposition K, PR-H §3, "proved modulo routine marking details"; not re-verified here), with the special set Sp ⊂ K_0 of R7-6, plus one robustness clause. For every ρ > 0 and every function θ : b \ {Q_0} → (0,∞) there are a marked path γ̃ (projecting to γ ⊂ V_0) and Q′ ∈ b \ {Q_0} satisfying (K\*)(a)–(c) with ρ, and in addition d(γ(1), Q′) < θ(Q′).
  - The clause reflects the two-step limit in Proposition K: first fix k, which fixes the end point Q′ = Q_k ≠ Q_0 at which γ_e has extremal length δ_k > 0; then let n → ∞, so the ray segments approach Q_k.
  - The path γ̃ is a Teichmüller ray segment, so it lies in one Teichmüller disc, hence in one irreducible component S of the preimage of V_0 in T_g.
- **(Ch), (Tr)** denote the chart lemma and the transport of vanishing data of R7-6 §2.1. They are used only at points of compact subsets of strata, at a fixed time t, with ρ chosen after t. This is the setting in which R7-6's proofs of them are routine.

**Hypotheses.**
- **(NB)** There are t_1 > 0 and an open neighbourhood 𝒪 of K_0 × {0} in closure(𝒱) such that every point of 𝒪 ∩ 𝒱 with 0 < |t| < t_1 is regular.
- **(NB_∂)** For every stable graph G, every 2-dimensional component W of 𝓦_G, every w ∉ M_W and every u ∈ M_W with M_w, M_u of type (g_i,n_i): the image of Γ_{W,w} in 𝔐 × Δ is not contained in pr_u(K_W) × Δ (classes in 𝔐). Equivalently, by irreducibility, the set D_∂(W,w,u) of τ at which some value of w on a component of W_τ has the class of a point of pr_u(K_W) is discrete. Let D_∂ be the union of these sets, which is discrete.

**Theorem S.** Assume the hypotheses of MS8 (with (R1), (R2), (Rig)), the input (K\*+) with end point of type MERGE or puncture-MOV, and (NB) and (NB_∂). Then Y_t = Y_0 for all t ∈ Δ.

No hypothesis on twins ((NT\*), (Lock)) is made.

### 4.3 Proof of Theorem S

Suppose Y is non-constant. Let Z be as in §3.

**Step 0 (choice of t).** Choose t ≠ 0 with the following properties.
- |t| < t_1, and |t| is small enough that, for the finitely many charts Def(z) used in Steps 3–5, H_τ(z) stays in the chart of z for τ ∈ [0,t].
- |t| is small enough that the finite exceptional set of R7-4 Theorem 3, steps 5–7, for the germs of closure(Ñ) at the end point (Step 5) is avoided.
- t ∉ Z.
- The segment [0,t] meets D_∂ only at 0 (possibly). Since D_∂ ∩ {|τ| ≤ t_1/2} is finite, only finitely many directions arg t are excluded.

Z is discrete, so such t exist. From now on t is fixed. All smallness requirements on ρ, θ below may depend on t.

**Step 1 (the path).** Take γ̃ ⊂ S from (K\*+) with ρ small.
- Let Bad ⊂ S be the proper analytic subset consisting of:
  - Sing(S);
  - the branch locus of S → V_0 (points with non-trivial stabilizer in Stab(S)/ker);
  - the sets S ∩ hS with hS ≠ S (all components of the preimage of the irreducible V_0 are translates of S).
- At each of its points, the Teichmüller disc containing γ̃ lies in a single local irreducible branch of S. In that branch the complement of Bad is connected and dense. So γ̃ can be perturbed, inside S and uniformly close to it in the Teichmüller metric, to a path avoiding Bad.
- Conditions (K\*)(a)–(c) are open conditions on the marked path, after replacing ρ by 2ρ. So they survive the perturbation. Keep the names γ̃, γ.
- Since γ avoids the image of Bad, a lift of γ to the preimage of V_0 is determined by its initial point.

**Step 2 (the square lifts).** For ρ small, γ ⊂ 𝒰′, where 𝒰′ is a neighbourhood of K_0 in closure(V_0) with H(𝒰′ × {|τ| ≤ |t|}) ⊂ 𝒪 (compactness, H continuous, H_0 = id).
- The half-open square F|_{[0,1]×(0,t]} lies in 𝒪 ∩ 𝒱 ∩ {0 < |τ| < t_1} ⊂ 𝒱^reg by (NB). It is simply connected, so it lifts to 𝒱̃.
- **Extension to τ = 0.** Fix s. The preimage of a small neighbourhood of (γ(s), 0) is a disjoint union of neighbourhoods of fibre points. The connected set F([s−δ, s+δ] × (0,δ]) lifts into one of them. Hence the lift extends continuously to τ = 0, and the extension is a continuous lift of γ into the preimage of V_0.
- Translate the whole lift by a deck element so that the extension starts at γ̃(0). By the uniqueness in Step 1, the extension equals γ̃.
- Over t = 0 the covering may branch along all of V_0 × {0}. This happens when every curve of V_0 carries automorphisms that disappear for t ≠ 0, as in the local model t = u^m of a deformation off a fixed locus. Such branching does no harm here: it lies on the boundary edge of the square only.
- **Consequence.** For every s, the *top-edge marking* of H_t(γ(s)) (continuation along s at time t) equals the *τ-transport* of the marking γ̃(s) along τ ↦ H_τ(γ(s)). In particular, R7-6's coherence gap does not arise.

**Step 3 (the class along arcs is a constant-vertex value).** Fix r > 0 smaller than half the minimal distance between points of Sp, and small for the charts at Sp.
- For s with d(γ(s), Sp) < 2r, take z_s ∈ Sp.
- Otherwise take z_s ∈ K_0 with d(γ(s), z_s) < ρ; then d(z_s, Sp) > r.
- Let c(s) ∈ 𝔐 be the class of the component of H_t(z_s) onto which Σ_i collapses, in the marking of Step 2. It is well defined for ρ small by (Tr), and up to o(1) as ρ → 0 independent of the choice of z_s, by (Ch).

*(a) Special points.* If z_s = J ∈ Sp, then c(s) is the class of a component of H_t(J): finitely many values.

*(b) Arc points.* Let K^r := K_0 \ (r-neighbourhood of Sp), a compact set of non-special points, each a smooth point of a piece. Cover K^r by finitely many charts Def(z_k) × Δ (z_k ∈ K^r, stratum G_k, piece D_k). The charts are so small that, in chart k, Σ_i corresponds for all points z of the chart to one chart label w_k, with comp_{w_k} ≅ Y_0 at the lift p^0_z of z selected by the marking at τ = 0 ((K\*)(b)). Consider the lifts of the points H_τ(z), z ∈ K^r ∩ chart k, τ ∈ [0,t]. They lie on the lifted boundary family of 𝒜_k := closure(𝒱) ∩ (Δ_{G_k} × Δ), whose 2-dimensional components W′ are as in Lemma U. Put:
- G′ := lifts lying on some W′ with w_k ∉ M_{W′};
- B′ := lifts lying on some W″ with w_k ∈ M_{W″}.

Both sets are compact. Every lift lies in G′ ∪ B′.

**Claim.**
- (i) G′ ∩ B′ ∩ {τ ∈ (0,t]} = ∅.
- (ii) At τ = 0, every point of B′ has comp_{w_k} ≇ Y_0. Hence B′ ∩ {τ = 0} stays at distance ≥ δ′ > 0 from the compact set of lifts with comp_{w_k} ≅ Y_0, which contains every p^0_z.

*Proof.*
- **The lifted fibre components through a point.** Let p be a lift of H_τ(z), z ∈ K^r. The fibre components through p are lifted branches of the germ of H_τ(D_k) at H_τ(z). This germ is unibranch: H_τ is a stratified homeomorphism and z is a smooth point of D_k, so the germ has a punctured neighbourhood homeomorphic to a punctured disc. Hence these fibre components are Stab(p)-translates of one another. So if W′, W″ both pass through p, there is σ ∈ Stab(p) with M_{W″} = σM_{W′}, by Lemma U applied to the fibre components through p.
- **(i).** Let p ∈ W′ ∩ W″ with w := w_k ∉ M_{W′}, w ∈ M_{W″} = σM_{W′}, over τ ∈ (0,t]. Then σ^{-1}w ∈ M_{W′} is moving on W′ while w is constant there. Since σ fixes p, comp_{σ^{-1}w}(p) ≅ comp_w(p). Here comp_w(p) is the value of w on the component of W′_τ through p, and comp_{σ^{-1}w}(p) lies in pr_{σ^{-1}w}(K_{W′}) (Lemma U). So τ ∈ D_∂(W′, w, σ^{-1}w), contradicting Step 0.
- **(ii).** Let p ∈ B′ at τ = 0 with comp_w(p) ≅ Y_0. Then w is a moving vertex of a lifted branch of D_k through p (the fibre component of W″ through p), and its value at z is ≅ Y_0. So z ∈ Sp (R7-6's Sp contains the points of D ∩ K_0 at which a non-constant vertex has class Y_0). This contradicts z ∈ K^r. The distance statement follows by compactness and continuity of comp_w on the stratum locus. ∎

**Consequence.** By (i), (ii) and compactness, there are τ_0 > 0 and δ_t > 0 such that:
- for τ ∈ [0, τ_0], B′ ∩ {τ ≤ τ_0} lies within δ′/4 of B′ ∩ {τ = 0} (upper semicontinuity for the compact set B′), and X̃_τ stays within δ′/4 of X̃_0 (uniform continuity of H and of the chart lift). So X̃_τ keeps distance ≥ δ′/4 − ε from B′;
- for τ ∈ [τ_0, t], G′ and B′ are at distance ≥ δ_t from each other (disjoint compact sets, by (i)).

The τ-transported marked surface X̃_τ (chart lift, continuous in τ) stays within ε = ε(ρ) of some lift of H_τ(z), by (Tr), and starts near p^0_z ∈ G′ \ B′. For ε < min(δ_t, δ′)/4, continuity forces X̃_τ to stay near G′ for all τ ∈ [0,t]. At τ = t, therefore, c(s) is, up to o(1), comp_{w_k} at a point of G′, i.e. the value of the constant vertex w_k on a component of some W′_t. These values form a finite set.

*(c) The finite set.* Let S_t be the union of:
- the classes of values of constant vertices on components of W_t, over all W;
- the classes of components of H_t(J), J ∈ Sp.

S_t is finite and contains Y_t. Let 2g_t > 0 be the minimal distance between distinct elements of S_t (in a fixed metric on the compactification of 𝔐). By (a), (b): for ρ small, every c(s) lies within g_t/4 of S_t.

**Step 4 (c is constant, equal to Y_t).**
- **Near-continuity.** By (Ch) applied at time t (finitely many charts covering H_t(K_0); Lebesgue number; ρ small), |c(s) − c(s′)| < g_t/4 whenever |s − s′| is small. Hence the element of S_t near c(s) is locally constant, so constant on [0,1].
- **Start.** P ∈ Sp, and for γ(0) near P we take z_0 = P. In Def(P), Σ_i ↔ the chart label i ((K\*)(a)).
  - Δ_Γ is of product type and dim M_{g_i,n_i} > 0, so every automorphism of a curve in Δ_Γ fixes the vertex i. (A graph automorphism moving i would act non-trivially on ∏_w M_w while ξ_Γ is injective.) Hence comp_i takes the same value at all lifts of P_t = H_t(P) ∈ ∂V_t.
  - That value is the vertex-i coordinate Y_t. So c(0) = Y_t.
- **Conclusion.** Hence c(1) = Y_t.

**Step 5 (the end point).** Work in Def(Q_0) × Δ. Let Ñ be the component of q^{-1}(H((b \ {Q_0}) × Δ)) containing b̃ \ {0}. Here b̃ is the lifted branch near which γ̃(1) lies, and along b̃ the chart label x of Σ_i is merged (MERGE) or intact and moving (MOV), by (K\*)(b),(c).
- **The right edge stays near Ñ.** Distinct components of q^{-1}(H((b∖Q_0)×Δ)) are disjoint. So the lifts of H_τ(Q′), τ ∈ [0,t], lying in Ñ and in the other components are at distance ≥ δ(Q′) > 0. Choose θ(Q′) ≪ δ(Q′) in (K\*+). Then the τ-transport of γ̃(1), i.e. the right edge of the lifted square, stays near Ñ_τ, with Σ_i ↔ x throughout.
- **The top edge ends at a lift of Q_t on that branch.** By Step 2 the top-edge marking at s = 1 is this one. As ρ → 0, Q′ → Q_0, so d(H_t(Q′), Q_t) becomes small compared with the separation of the (fixed) lifts of Q_t. So the end point lies near a lift q of Q_t, and the lifted branch of H_t(b) through q containing the lift of H_t(Q′) is a branch of closure(Ñ_t). Its pattern is the constant pattern S_b̃ of Ñ.
- **x is a Y_t-copy at q.** By Step 4, comp_x(q) ≅ c(1) = Y_t.
- **MERGE.** x is merged along a branch at q. Theorem 1 (merge excluded) gives Y_t ∈ 𝔉, so t ∈ Z, contradicting Step 0.
- **Puncture-MOV.** x is intact along the branch. By R7-4 Theorem 3, steps 5–7 (applied to the germs of closure(Ñ) at (0,0), with t outside their finite exceptional set by Step 0), comp_x is non-constant along it, and Q_t ∉ Δ_{G_b}. Theorem 1 (puncture-MOV excluded) gives a contradiction.

Hence Y is constant. ∎

### 4.4 Remarks on Theorem S

1. **What replaces (Lock) / (NT\*).** Neither is assumed. Twins at junction points are harmless as long as the square lifts, because the class c(s) is then read off in one coherent marking at time t. This is exactly R7-6's "why twins do no harm" remark, now with its gap closed by (NB).
2. **(NB) is a statement about new orbifold points only.** Branching along V_0 × {0} itself is allowed (Step 2). What (NB) forbids is a sequence of curves X_n ∈ V_{τ_n}, τ_n → 0, τ_n ≠ 0, with more automorphisms than the generic curve of the relevant sheet of 𝒱̃, converging to a point of K_0. By upper semicontinuity of |Aut| on M̄_g (cited from memory), the closure in M̄_g × Δ of the locus of such points is analytic (it is a union of components of an analytic set not contained in {t = 0}). Its t = 0 slice is a compact analytic set of dimension ≤ 1. So (NB) fails only if this slice meets K_0.
3. **(NB_∂) is a coincidence condition internal to single families W.** It fails only if, for some W, a constant vertex w and a moving vertex u of the same type satisfy: for every τ, the constant value of w lies on the fixed trace curve pr_u(K_W). For instance, in the quintic example (PR-I) the only family through ∂V_0 has M_W = {genus-4 vertex} and the constant vertex has genus 2. So the types differ and (NB_∂) holds there. I do not know how to exclude the coincidence in general.
4. **Interior-MOV end point.** Steps 0–4 work verbatim and give c(1) = Y_t. At the end, x is intact and non-constant along a branch through an interior point Q_t of E_{b,t}. That is an IMOV configuration of a Y_t-copy, which Theorem 1 allows. So Theorem S does not cover the crossing case (see §5).

## 5. The crossing (interior-MOV) case

**Proposition 7 (dichotomy for crossings; proved).** Assume the hypotheses of MS8 and that Y is non-constant. Let I be the set of t ∉ Z at which some Q ∈ B_t, with lift q and Y_t-copy y, lies in the IMOV case of Theorem 1. Then exactly one of the following holds:
- (a) I is discrete in Δ;
- (b) there are a 2-dimensional component W of some 𝓦_G and a vertex y ∈ M_W of type (g_i,n_i) such that **Y(Δ) ⊂ T_{W,y} := pr_y(K_W)**, a fixed irreducible algebraic curve in M̄_{g_i,n_i}/S_{n_i}.

*Proof.* For t ∈ I, with piece E ⊂ W_t and y ∈ M_W, Lemma U gives Y_t ≅ pr_y(pr_{M_W}(lift of Q)) ∈ pr_y(K_W). Here pr_y(K_W) is an irreducible curve (image of K_W under a morphism non-constant on it), independent of t by Lemma U. There are finitely many pairs (W,y) over any compact sub-disc. If I is not discrete, Y_t ∈ T_{W,y} for t in a set accumulating in Δ, for one pair. So Y^{-1}(T_{W,y}) is an analytic subset of Δ with an accumulation point, hence all of Δ. ∎

**Consequences.**
1. Under the hypotheses of Theorem S with an *interior-MOV* end point, Steps 0–5 apply at every admissible t in a small sector. They produce an IMOV at Q_t for all such t, so (b) holds with W ⊃ E_b, y = x and T = closure(π_x(E_{b,0})) ∋ Y_0.
   - Moreover, κ(t) := pr_{M_W}(lift of Q_t) ∈ K_W satisfies pr_x(κ(t)) = Y_t.
   - Every other coordinate z ∈ M_W of κ(t) is STAY along the branch by which the path reaches Q_t (IMOV clause of Theorem 1). So it equals a constant-vertex value of that family, a branch of an algebroid function Γ_{W′,z′}(t).
2. In case (a), at all t outside a discrete set no Y_t-copy is ever in the IMOV case. Together with Theorem 1, every Y_t-copy of every point of B_t then STAYs along every branch: this is case (II) of the earlier worker's file. In case (a) the interior-MOV end point of Theorem S is impossible: the end-point configuration of Step 5 is an IMOV at Q_t for all t in a sector. So, in case (a), Theorem S covers every end point type.

**Why (b) is not yet contradictory.** If the moving vertex x of E_{b,0} is a Teichmüller vertex (Lemma PA, PR-H §1, puts positive area only at vertices of maximal speed, so this is not guaranteed), then T is a Teichmüller curve. A non-constant holomorphic map Δ → T is not absurd, since T is uniformized by the disc. The local crossing model of R7-2 §4.2 (s_e = ρσ for the edges at x, s_f = ρ for the others, x-coordinate σ) is compatible with (R1), (R2), (i), (ii) and (Rig). So no local analytic argument at the crossing point excludes (b). Excluding it needs a global input at t = 0: either a version of Proposition K whose end point is never a crossing (R7-2 Open question 2), or a rigidity statement for the value Y_t = pr_x(κ(t)) along the fixed curve K_W. I have neither.

**Corollary S′ (summary of §4–§5; conditional).** Assume the hypotheses of MS8, the input (K\*+) (any end point type), (NB) and (NB_∂). Then either Y_t ≡ Y_0, or Y(Δ) is contained in one of the finitely many fixed curves T_{W,y} = pr_y(K_W) (y a moving vertex of type (g_i,n_i) of a family W).

*Proof.* If Y is non-constant and Proposition 7(a) holds, Theorem S together with Consequence 2 gives a contradiction. Otherwise Proposition 7(b) holds. ∎

## 6. On the chain and on the earlier files

1. **The derivation "MS8 + entry 69 ⇒ problem's claim" is sound.** MS8 has (Rig) as its hypothesis and the problem's conclusion as its conclusion; entry 69 is exactly "(Rig) holds". The consequence of (Rig) recorded in chain step 3 (puncture values of non-constant vertices lie in a t-independent finite set) is correct. It is Corollary U3 here, valid in all strata. I found no flaw in this part of the chain.
2. **Flaw in the earlier worker's Lemma 6 (partial file §3.1).** It claims that the moving set M of a lifted family is "the same for all t by L1′". L1′ gives only "constant at t = 0 ⇒ constant at all t" (for all components simultaneously). For non-product strata, the fibres of W can have components with different moving sets (R7-5 §1.4), so the claim is unjustified as stated. Lemma U proves the needed statement under (Rig), with a different argument (Stein factorization plus the finiteness in (Rig)). The partial file's Proposition 7 and Theorem 1 then hold as stated. I re-proved Theorem 1 in §3 using Lemma U.
3. **R7-6 (continuity principle).** The planner's warning is justified, and §4 makes it precise:
   - The coherence of the transported markings is exactly the liftability of the square F. It can fail only through branch points of 𝒱̃ → 𝒱 met by F.
   - Branch points over t = 0 are harmless (Step 2).
   - R7-6's hypothesis (P′) (Aut(G)-fixed constant vertices) can be replaced by Lemma U plus (NB_∂) (Step 3(b)).
   - The chart-size degeneration near junctions is handled by reading classes at the special points themselves (Step 3(a)), with ρ chosen after t. This is possible because t is fixed first and (NB) is uniform.
4. **(Lock), (NT\*) versus (NB).** These hypotheses are of different nature.
   - (Lock) and (NT\*) are conditions at the finitely many junction points of K_0.
   - (NB) is a condition on the *new* orbifold points of V_τ (τ ≠ 0) near K_0.
   - Neither family implies the other as far as I can see. Theorem S is therefore a new partial result, not a re-derivation of R7-1 Theorem T / R7-2 Theorem A. Like them, it is partial.

## 7. Final summary

**Proved (modulo the cited standard facts and the prior results explicitly used).**
- Lemma U and Corollaries U1–U4: under (Rig), every 2-dimensional component W of every lifted family has one moving set and one image curve for all components of all fibres at all times. In particular every piece at every time is K_W × {point}, and the non-product L1 pathology cannot occur.
- Theorem 1 (generic-time trichotomy): for t outside a discrete set Z, no Y_t-copy merges or moves at a puncture. Every Y_t-copy either STAYs (with value function ≡ Y) or is in an IMOV configuration.
- Proposition 7: either IMOV configurations occur only at a discrete set of times, or Y(Δ) lies in a fixed algebraic curve pr_y(K_W).

**Proved conditionally (new; partial).**
- Theorem S / Corollary S′. Their hypotheses are:
  - Proposition K in the form (K\*+), taken from PR-H / R7-6, "modulo routine marking details", not re-verified;
  - R7-6's chart facts (Ch), (Tr), routine, not re-proved in full;
  - (NB): no curves with new automorphisms in V_τ, τ → 0, accumulating on K_0;
  - (NB_∂): no identical coincidence between a constant-vertex value curve and a moving-vertex trace curve within one family.

  Under these, MS8 holds whenever Proposition K ends in MERGE or puncture-MOV, with no hypothesis on twins. For any end point type, either Y is constant or Y(Δ) ⊂ T_{W,y}.

**Not proved / open (named).**
- **MS8 itself.** No complete proof and no counterexample.
- **Open question A (new orbifold points).** Show (NB): for an admissible family, curves of V_τ (τ ≠ 0) whose automorphism group exceeds the generic one of 𝒱 do not accumulate, as τ → 0, on the continuum K_0 of Proposition K. Or show that Proposition K's continuum can be chosen to avoid the compact analytic set of dimension ≤ 1 formed by their limits at t = 0. Only accumulation on K_0 matters.
- **Open question B (coincidences).** Exclude (or handle) a family W in which the value of a constant vertex w lies, for every τ, on the trace curve pr_u(K_W) of a moving vertex u of the same type, i.e. show (NB_∂).
- **Open question C (crossings).** Exclude alternative (b) of Proposition 7: Y(Δ) ⊂ pr_y(K_W). Equivalently, sharpen Proposition K so that its end point is never an interior-MOV, or prove rigidity of the crossing value Y_t = pr_x(κ(t)) on the fixed curve K_W.
- Inherited inputs: Proposition K's marking details; entry 69 ((Rig) itself, via (O_G), (F2), L2′) is outside the scope of MS8.

=== END OF ANSWER round8_q2 ===

