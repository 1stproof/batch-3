# round11_q3 answer

Status: MS11 is NOT proved and no counterexample is given. I found and repaired a flaw in the chain: Lemma B1(a)/(b) is wrong as stated, so the chain's endpoint step needs "proper" sheets (§2). I verified Mechanism D, steps 1–3, with one correction (§1). Using Theorem N, I proved that the lift-curve edges and the interior/IMOV edges never change the persistent label (§3). What is left is two explicit edge types, both coming from automorphisms that fix a curve pointwise (§3.6). There is a partial result, Corollary 3.5. Lists are in §4.

Plan followed: (1) check Mechanism D (connectedness of D = X ∩ {N=0}); (2) handle the edges with Theorem N (R8-3, PROVED under (Rig), generic t), which keeps the exact label; (3) find exactly which edges can still change the label; (4) check the chain.

## 1. Mechanism D, steps 1–3: verified (with one correction; step 4's edge list is revised in §3)

Setting of MS11. Let S be the component of (S). Let X be a 3-dimensional irreducible component of the germ of q^{-1}(closure 𝒱) at (0,0) ⊂ Def(Q) × Δ_ε with S × {0} ⊂ X (exists: the germ is pure 3-dimensional, since 𝒱 is a 3-manifold dense in closure(𝒱) and q is finite; the irreducible 2-dim set S × {0} lies in the union of the finitely many components, hence in one). N := ∏_e s_e, D := X ∩ {N = 0}.

(D1) D has pure dimension 2 (Krull: N ≢ 0 on X since X contains points over 𝒱, and N(0,0) = 0). No component of D lies in {t = 0}, because X ∩ {t=0} ∩ {N=0} ⊂ q^{-1}(B_0) is at most 1-dimensional.

(D2) Every component T of D is a transport sheet of a lifted branch c̃ with c̃ × {0} ⊂ T. Proof: T ∩ {t = 0} is a curve germ through (0,0) (dimension drops by exactly one), contained in q^{-1}(B_0), hence a union of lifted branches c̃ × {0}. Near (Q,0), closure(𝒱) ∖ 𝒱 = H(B_0 × Δ_ε) is the disjoint union of the lift-curve set {Q_t} and of the sets N_c = H((c ∖ Q) × Δ_ε) over the branches c of B_0 at Q; these are pairwise disjoint and each is relatively open and closed in the complement of the Q_t-curve. T minus the (at most 1-dimensional) preimage of the Q_t-curve is connected (T is irreducible), lies in q^{-1}(⋃ N_c), and contains c̃ ∖ 0 × {0} in its closure... more precisely it contains points of c̃ ∖ 0 × {0}; hence it lies in the connected component Ñ_c̃ of q^{-1}(N_c). So T ⊂ closure(Ñ_c̃); both are 2-dimensional and T irreducible, so T is an irreducible component, i.e. a transport sheet of c̃. ∎

(D3) Since β̃, b̃ ⊂ S, D contains a sheet T_β ⊃ β̃ × {0} and a sheet T_b ⊃ b̃ × {0}.

(D4) Grothendieck's connectedness theorem (cited from memory, SGA 2 XIII 2.1 / Hartshorne "Complete intersections and connectedness" Prop. 2.1 + 3.1 form): if A is a complete local noetherian domain of dimension d and f ∈ m, then Spec(A/f) ∖ {m} is connected when d ≥ 3. The analytic local ring of the irreducible germ X is a domain whose completion is a domain (analytic local rings are excellent and an irreducible analytic germ is analytically irreducible). Hence D ∖ {(0,0)} is connected; equivalently the graph whose vertices are the components of D, two being adjacent when they share a curve germ through (0,0), is connected. (Connectedness in dimension 1 of D: components can be chained so that consecutive ones meet in dimension ≥ 1.)

**Correction 1.** The sheet on which x is assumed persistent in MS11 need not lie in X: (S) only places β̃, b̃ in S, and q^{-1}(closure 𝒱) may have several 3-dimensional components through S × {0} (e.g. X and gX with g fixing S pointwise; local model: Def ∋ (a,b), g: b ↦ −b, quotient coordinate c = b², 𝒱-sheet {c = t²} lifts to b = ±t). Lemma 3.4 below handles this, at the price of relabelling x by an element of Stab_pt(β̃). (The connectedness in (D4) is for small conic representatives: if two sheets meet away from the origin, the curve selection lemma gives a common curve germ through (0,0).)

## 2. A flaw in Lemma B1(a)/(b) (round10_q3), and its effect on the chain and on MS11

Lemma B1(a) asserts that every irreducible component Ñ^1 of Ñ_b̃ meets {t = 0} in a non-empty open subset of b̃ ∖ 0; its proof says "Ñ ∩ {t = 0} = b̃ ∖ 0". That equality is not justified: Ñ_b̃ is the connected component of q^{-1}(N) containing b̃ ∖ 0, and it may also contain σb̃ ∖ 0 for σ ∈ Aut(Q) with σb̃ ≠ b̃, the connection being made at t ≠ 0 through points with extra automorphisms.

**Chart-local model (consistent with the chart data).** Coordinates (z, w, …) on Def(Q), where z is a smoothing parameter s_e of an edge unpinched along b (b̃ ∖ 0 ⊂ {z ≠ 0}), σ ∈ Aut(Q) acts by w ↦ −w (fixing z), b̃ = {w = z} and σb̃ = {w = −z} (two distinct lifts of the same coarse branch b; other coordinates frozen). Downstairs coordinates (z, u = w², t). Let the transported coarse branch be N = {u = (z + t)²}, the graph of a function of (z,t), hence a topologically trivial family of punctured discs as required by (R2). Then
 q^{-1}(N) = T_1 ∪ σT_1, T_1 = {w = z + t}, σT_1 = {w = −z − t},
and T_1 ∩ σT_1 = {w = 0, z = −t}, which lies in the region z ≠ 0 for t ≠ 0. So q^{-1}(N) is connected, Ñ_b̃ = T_1 ∪ σT_1, and its component σT_1 meets {t = 0} only in σb̃. (At time t the boundary curve H_t(b) passes through the point z = −t with the extra automorphism σ; nothing in the chart data forbids this.)

Consequences.
- B1(a) is false as stated in this model, and B1(b) (transitivity of Stab_pt(b̃) on components) fails too: σT_1 is not a Stab_pt(b̃)-translate of T_1. B1(c) and B1(d) are unaffected (B1(d) at product type: every α fixes the label, Lemma PT).
- **Chain step (d) and MS11's parenthetical conclusion.** If the sheet T delivered by MS11 is of the type σT_1 (meets t = 0 only in σb̃), persistence of x on T gives, at t = 0, that x is intact with F_x ≡ Y_0 along σb̃, i.e. that σ^{-1}x is intact with F ≡ Y_0 along b̃. This does not contradict MERGE/MOV of x along b̃ unless σ fixes x. So the step "MS11 ⇒ contradiction at the endpoint" is not valid with the current definition of transport sheet.
- **Repair (proposed, checked against the chain's other steps that I read).** Call a transport sheet T of c̃ *proper* if c̃ × {0} ⊂ T. Read MS11's hypothesis and conclusion with proper sheets. Then the endpoint step is valid: x persistent on a proper sheet T of b̃ gives at t = 0 that x is intact with F_x ≡ Y_0 on b̃ ∖ 0 (closed conditions, b̃ × {0} ⊂ T), contradicting MERGE and MOV. The transfer step of the chain (round10_q3 §2.2 item 3) produces a global component containing a germ at (p̃, 0), p̃ ∈ β̃_{m+1} generic, whose t = 0 slice lies on β̃_{m+1}; that component contains β̃_{m+1} × {0}, so it is proper. The base step is unaffected (product type). I have not re-checked Lemma J / Cor. J′ for properness of the sheet they produce; this is a point to verify.

## 3. New results on the sheet graph of D

Standing assumptions for §3: the MS11 setting, (Rig), Y non-constant, so Theorem N (R8-3 §3, PROVED there under (Rig)) is available at every generic t (t outside a countable set Z). Notation: P(r) := {e ∈ E(G_Q) : s_e(r) = 0}; P(T) := the pattern at generic points of a sheet T (constant on T minus the preimage of the lift-curve, by R7-4 Lemma 2(a)); Π(T) := the set of labels persistent on T. By (K3), Π(hT) = hΠ(T) for h ∈ Aut(Q).

### Lemma 3.1 (every sheet of D is puncture-type). Proved, using Theorem X*_all.
For every sheet T of D, P(T) ≠ E(G_Q).

*Proof.* q(X) is an irreducible 3-dimensional germ of closure(𝒱) at (Q,0) (Remmert), so a local irreducible component 𝒮 of closure(𝒱). By the topological description of local components (R8-1 Lemma S, applied to closure(𝒱) with the homeomorphism H of pairs from (R2)), 𝒮 = H(Σ × Δ_ε) for a local sheet Σ of closure(V_0) at Q, so 𝒮 ∩ {t = 0} = Σ (H_0 = id). Then S × {0} ⊂ X_0 ⊂ q^{-1}(Σ), so q(S) = Σ, and q^{-1}(Σ) = ⋃_{g∈Aut(Q)} gS (components of the preimage of an irreducible germ are permuted transitively). By (D2), T ∩ {t = 0} ⊃ c̃ × {0} with c̃ a boundary branch of some gS, and P(T) = P(c̃). If P(c̃) = E(G_Q), then c̃ is a lifted branch of a piece containing Q in its stratum, and Theorem X*_all (round10_q1 §2: a sheet containing such a branch has no other boundary curve through 0) applied to gS contradicts gβ̃ ≠ gb̃ ⊂ gS (two distinct boundary curves). ∎

### Proposition 3.2 (edges along curves not in {t = 0}). Proved.
Let T_1 ≠ T_2 be sheets of D sharing an irreducible curve germ C through (0,0), C ⊄ {t = 0}, and let x ∈ Π(T_1). Then x ∈ Π(T_2), unless the following configuration (γ°) occurs: T_2 = gT_1 for some g ∈ Aut(Q) fixing C pointwise, P(T_1) = P(T_2) = gP(T_1), and for all t in a co-countable subset of a punctured disc, at the points r ∈ C_t the label x is intact, F_x(r) ≅ Y_t, and x is non-constant along T_{2,t} (IMOV in Theorem N), the point q(r) lying in the stratum of the coarse piece of T_1. In case (γ°), gx ∈ Π(T_2).

*Proof.* 𝔛 := {(p,t) ∈ D : p ∈ L_x, [F_x(p)] = [Y_t]} is closed analytic, and T_1 ⊂ 𝔛. For small t ≠ 0, C_t is finite and non-empty. Let t be generic and r ∈ C_t, R := q(r) ∈ B_t. Then x is intact at r and F_x(r) ≅ Y_t. The chart Def(Q) near r is a universal deformation of R, so Theorem N applies at R with the lift r, the copy x and any branch of T_{2,t} at r (a lifted branch of B_t at R): x is intact along it and either STAY (F_x ≡ Y_t on it) or IMOV (P(T_2) = P(r), F_x non-constant on it); here the pattern of the branch minus r is P(T_2).
- If STAY occurs for uncountably many t, then T_2 ∩ 𝔛 contains curve germs in uncountably many t-fibres; an analytic set of dimension ≤ 1 cannot (countably many components, each in one fibre or finite over t), so T_2 ∩ 𝔛 is 2-dimensional and T_2 ⊂ 𝔛: x ∈ Π(T_2).
- Otherwise IMOV holds for t in a co-countable set. Two sub-cases at such (r,t):
  - (B1) the germs of T_{1,t} and T_{2,t} at r map to different coarse germs at R. Then R ∈ D_{2,t} (stratum part, since P(r) = P(T_2)) is either in closure(D_{1,t}) with D_1 ≠ D_2, or a point where closure(D_{2,t}) has ≥ 2 local branches. Both sets are H_t(F) for a finite F ⊂ D_2 (H_t is a stratum- and piece-preserving homeomorphism, PR-B, and the number of local branches of a curve is topological). If B1 holds for t_n → 0 with r_n ∈ C_{t_n}, pass to R_{t_n} = H_{t_n}(f) with fixed f ∈ F; then H_{t_n}(f) → f and q(r_n) → Q, so Q = f ∈ D_2, i.e. T_2 is interior-type, contradicting Lemma 3.1.
  - (B2) otherwise, for t in a co-countable subset of a smaller punctured disc, both germs map to the same coarse germ, so (transitivity of Stab(r) on the components of the preimage of an irreducible germ) T_{2,t}-germ = g_t·T_{1,t}-germ with g_t ∈ Stab(r). Some g occurs for uncountably many t; then T_2 ∩ gT_1 is 2-dimensional, so T_2 = gT_1, and Fix(g) ∩ C is infinite, so C ⊂ Fix(g). P(T_1) ⊂ P(r) = P(T_2) = gP(T_1) forces equality. gx ∈ gΠ(T_1) = Π(T_2) by (K3). This is (γ°). ∎

*Remark (strengthening inside (γ°)).* Since g fixes r, every label g^k x is a Y_t-copy at r (F_{g^kx}(r) ≅ F_x(g^{-k}r) = F_x(r)), so Theorem N applies to each of them along both T_{1,t} and T_{2,t}; in particular if g changed the pattern (gP(T_1) ≠ P(T_1)) then IMOV would be impossible at r for every label and x ∈ Π(T_2) would follow — which is why (γ°) requires gP(T_1) = P(T_1). (Consequence: the "same coarse branch, twin MERGE" variant of the §2 model is impossible inside D. Suppose b̃ = σβ̃ with σ an involution, x ∈ Π(T_1) for a proper sheet T_1 of β̃, x merged along b̃ at t = 0 (MERGE endpoint), and T_1, σT_1 meet along a curve C ⊂ Fix(σ) not in {t = 0}. Then σx is merged along β̃ = σb̃, i.e. some edge at σx is not in P(T_1) = P(β̃). At r ∈ C_t (generic t), σx is an intact Y_t-copy (σ fixes r), and it is merged along the branch of T_{1,t} at r — contradicting Theorem N. So in this variant the twin edge must be a (β)-edge, C = c̃ × {0}.)

### Lemma 3.3 (edges along t = 0 curves). Proved.
If T_1 ≠ T_2 share C = c̃ × {0}, then T_2 = σT_1 with σ ∈ Stab_pt(c̃), and σΠ(T_1) = Π(T_2).

*Proof.* For generic p ∈ c̃ ∖ 0, Stab(p) = Stab_pt(c̃), q near (p,0) is the quotient by Stab(p), and the germ of N_c at (q(p),0) is irreducible (it is a topological 4-manifold). So the germs of q^{-1}(N_c) at (p,0) are hG_0, h ∈ Stab(p). T_1 ⊃ h_1G_0, T_2 ⊃ h_2G_0, hence T_2 = h_2h_1^{-1}T_1 (identity principle for irreducible germs sharing an open set). ∎

### Lemma 3.4 (Correction 1 made precise). Proved.
The proper sheets of β̃ (§2) are exactly the hT*, h ∈ Stab_pt(β̃), for any one of them T* (same proof as 3.3). Hence if x is persistent on some proper sheet of β̃, then hx ∈ Π(T_β) for the proper sheet T_β ⊂ D of (D3) and some h ∈ Stab_pt(β̃).

### Corollary 3.5 (partial result toward MS11, proper reading).
In the setting of MS11 with proper sheets, suppose every element of Aut(Q) that fixes pointwise a curve germ through (0,0) contained in q^{-1}(closure 𝒱 ∖ 𝒱) — more precisely: the elements h of Lemma 3.4, σ of Lemma 3.3 and g of (γ°) arising in D — fixes the label x. Then x is persistent on a proper sheet of b̃, i.e. the conclusion of MS11 holds.

*Proof.* Start at T_β with x ∈ Π(T_β) (Lemma 3.4 and h x = x). Walk along a path of the connected sheet graph (D4) to T_b. At each edge the persistent label is preserved (Prop. 3.2) or replaced by its image under an element that fixes the shared curve pointwise (Lemma 3.3, case (γ°)), which by hypothesis fixes x. So x ∈ Π(T_b), and T_b ⊃ b̃ × {0}. ∎

### 3.6 What remains: the (β)-twin edge (why I could not close it)
After 3.1–3.4 the only label-changing edges are (β)-edges T_1 — σT_1 along c̃ × {0}, σ ∈ Stab_pt(c̃), and (γ°)-edges. At a (β)-edge: since c̃ × {0} ⊂ T_1 ∩ σT_1, P(T_1) = P(c̃) = σP(T_1), so y := σ^{-1}x is intact along T_1 as well (x ∈ Π(T_2) ⟺ y ∈ Π(T_1)). Via Π_{P} the sheet T_1 maps into a component W_1 of the lifted family of the piece of c (round8_q2 Lemma U). At t = 0, F_y = F_x∘σ ≡ Y_0 on c̃, so y ∉ M_{W_1} and y is a constant vertex of every fibre of W_1, with a holomorphic value φ(t), φ(0) = Y_0. The failure configuration is exactly φ ≢ Y, i.e. y ∉ Π(T_1): the two twin components of the curves over c (Y_0 and Y_0 at t = 0, swapped by σ which fixes c̃ pointwise) deform to (Y_t, φ(t)). Theorem N is silent here (φ(t) is not a Y_t-copy), Krull/connectedness is already used up, and Theorem X*_all does not apply (puncture-type sheets). Total geodesy would have to enter through Fix(σ) ∩ S (planner's Lemma TG); I did not obtain a usable statement. So this is the precise remaining obstruction for MS11 inside one 3-fold component X: **(β)-twin edges, and (γ°)-edges** (the latter: an interior self-crossing of a lifted piece at a g-fixed point, with g^{-1}x moving along T_1).

Remark on Corollary 3.5: it is PARTIAL (an extra hypothesis of the type excluded by the task), but it is strictly weaker than (NT): only automorphisms of Q fixing pointwise a curve of the lifted boundary family 𝓑 near 0 matter, and Lemma 3.1 / Prop. 3.2 remove the lift-curve edges (α) and the IMOV/interior obstruction entirely.

## 4. Summary

**Proved here** (under the run's readings (R1), (R2); §3 also uses (Rig) and "Y non-constant" through Theorem N; cited facts: Grothendieck connectedness, Remmert, curve selection, Kuranishi universality at nearby points, all from memory):
1. Mechanism D, steps 1–3 (§1, D1–D4). D = X ∩ {∏s_e = 0} has pure dimension 2. Its components are transport sheets that contain their t = 0 branch. Its sheet graph is connected. Correction: the hypothesis sheet of MS11 need not lie in X (handled by Lemma 3.4).
2. Lemma B1(a)/(b) of round10_q3 is false as stated: a transport family can contain sheets that meet {t = 0} only in a different lift σb̃ (explicit chart model in §2). As a result, chain step (d) ("MS11 ⇒ contradiction at the endpoint") is invalid with the current definition of sheet. Repair: read MS11's hypothesis and conclusion with *proper* sheets (sheets containing c̃ × {0}). With that reading, step (d) is valid, and so is the transfer step of round10_q3 §2.2(3).
3. Lemma 3.1: every sheet of D is puncture-type (uses Theorem X*_all).
4. Proposition 3.2: along a shared curve not contained in {t = 0}, persistence of the *same* label passes, except in configuration (γ°). In particular lift-curve edges (α) never change the label, and IMOV/interior edges cannot occur. This replaces the planner's step 4(α) and corrects 4(γ).
5. Lemma 3.3: a (β)-edge is T_1 — σT_1 with σ ∈ Stab_pt(c̃). Lemma 3.4: proper sheets of β̃ form one Stab_pt(β̃)-orbit.
6. Corollary 3.5 (PARTIAL): MS11 (proper reading) holds whenever the automorphisms of Q that fix pointwise a curve of the lifted boundary family (the h, σ, g above) fix x.
7. The "same coarse branch, twin MERGE" variant with a dominating fixed curve is impossible (remark after Prop. 3.2).

**Not proved:**
- MS11 itself, in either reading.
- That Lemma J / Cor. J′ (round9_q7), used at product-type junctions of the chain, produce *proper* sheets. I did not re-check this. It is needed for the repaired chain.
- Theorem N and Theorem X*_all were used as PROVED by earlier rounds; I did not re-prove them.

**Open (precise):**
- (O1) (β)-twin edges. Let c̃ be a boundary branch of a translate gS with σ ∈ Stab_pt(c̃), and let T_1, σT_1 ⊂ D be sheets with x ∈ Π(T_1). Show that σ^{-1}x ∈ Π(T_1), i.e. that the constant twin value φ(t) of §3.6 equals Y_t, or that the composite of such relabellings along some path to T_b lies in Stab(x)·Stab_set(b̃). Total geodesy has to enter here, presumably through Fix(σ) ∩ S.
- (O2) (γ°)-edges: a self-crossing of a lifted piece, at points interior to its stratum, through g-fixed points C_t → 0, with g^{-1}x moving along T_1.
- (O3) The global input (Rig) (entry 82), unchanged.

No counterexample to MS11 or to the problem is claimed. The chart-local models (§2; §3.6) only show that chart-local reasoning cannot close (O1).

=== END OF ANSWER round11_q3 ===
