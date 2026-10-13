# round8_q1 — answer

**Status / plan line.** I do not prove MS8 in full, and I have no counterexample. The file contains:
- (§2) A short check of what (Rig) gives at generic times. One lemma is new: an interior move (IMOV) at generic t is a *pure crossing*, and the crossing point and its coordinates are holomorphic in t.
- (§3) **Theorem X**, a new t = 0 result, proved modulo cited standard facts. It is an intersection-theoretic consequence of total geodesy. Let Q_0 be an interior point of a piece E of B_0, and let S be a local sheet (irreducible component of the germ) of closure(V_0) at Q_0 that contains a branch β of E. Then no other boundary curve of the normalization Ŝ through Q_0 is Q-Cartier. In particular, if Ŝ is smooth, or has a rational singularity, at the point over Q_0, then the boundary of S near Q_0 lies over β.
- (§4) Consequence: crossings, in particular the IMOV endpoints of the chain, are excluded whenever the two pieces lie in a common Q-factorial sheet. What remains of the crossing case is "two-sheet" and "non-Q-Cartier" crossings.
- (§5) Twins: no new resolution, only a precise statement of what is missing.
- (§6) Proved / not proved / open.

Readings (R1), (R2) and the notation of the task (B_t, pieces, M(E), K(E), punctures, Y_t-copies, Def(Q), s_e, comp_x) are used throughout.

## 1. Cited standard facts (from memory; not re-proved here)

- **(Wol) Wolpert's lemma.** If d_T(X, X') ≤ d, then e^{-2d} ℓ_X(γ) ≤ ℓ_{X'}(γ) ≤ e^{2d} ℓ_X(γ) for every closed curve γ. Here ℓ is hyperbolic length.
- **(Ab) Abikoff.** Hyperbolic length functions are continuous on augmented Teichmüller space. On a noded surface, the length of a curve disjoint from the nodes is computed on its component, and the length of a node curve is 0. Finitely many length functions give local coordinates, or at least a proper injective map, on each stratum. Hence, if X_n → Z in M̄_g, the curves with ℓ → 0 are exactly the node curves of Z, and the components of Z are determined by the limits of the lengths of curves disjoint from the nodes.
- **(Prop) Teichmüller discs.** For (X, q) with q ∈ Q(X) ∖ 0, the Teichmüller disc τ̃: 𝔻 → T_g is a holomorphic isometric (Kobayashi = Teichmüller, Royden) proper embedding. Its image is a closed complex submanifold of T_g. The family of its Mod_g-translates is locally finite.
- **(Fl) Flat convergence on positive-area components.** Let X_n → P in M̄_g and q_n ∈ Q(X_n) with ‖q_n‖ = 1. Suppose the transplanted differentials ι_n^* q_n converge locally uniformly on each component Y_w of P to q_w, and Σ_w ‖q_w‖ = 1 (no area is lost in the collars). Let A ∈ SL_2(R) and let Z be any limit point of A·(X_n, q_n). If q_j ≠ 0, then Z has, at the node-pattern position of j, the component A·(Y_j, q_j). *Sketch:* the affine maps converge on compact subsets of Y_j ∖ {punctures}, and a conformal embedding between finite-type hyperbolic surfaces of the same signature that is a homotopy equivalence is onto up to punctures. I cite this as standard and have not written a full proof.
- **(PA) Lemma PA** (prior result PR-H §1, proved there modulo (Pl), (Dual), (Bun)). Let P_1 be a generic point of a piece E (product-type stratum) and fix a local branch N of closure(V_0) along E at P_1. Then there are X_n ∈ V_0 ∩ N, X_n → P_1, and generating pairs (X_n, q_n) whose transplants converge to (q_w)_w with Σ‖q_w‖ = 1 and q_j ≠ 0 for some vertex j ∈ M(E). Since V_0 is totally geodesic, the Teichmüller discs D_n of (X_n, q_n) lie in V_0.
  - The proof in PR-H uses approximants X_n = ν(s_0, τ_n) inside a chosen local branch N, so the branch can be prescribed.
  - The vertex j is a max-speed vertex. It moves along E because a_j ≠ 0.
- **Hurwitz.** If holomorphic functions h_n without zeros on a connected open Ω converge locally uniformly to h, then h ≡ 0 or h has no zeros on Ω.
- **Normal surface germs.** Let Ŝ be a normal 2-dimensional germ. A meromorphic function whose divisor is ≥ 0 is holomorphic, and the zero set of a holomorphic function is the support of its divisor. A Weil divisor C is *Q-Cartier* if mC = div(G) for some m ≥ 1 and some holomorphic G. Rational surface singularities, in particular smooth points and quotient singularities, are Q-factorial (Lipman). Normalization has the universal property for maps from normal spaces whose image is not contained in the non-normal locus.

## 2. What (Rig) gives at generic times

Throughout this section assume **Y is non-constant**, to reach a contradiction.

### 2.1 Generic times (re-check of chain step 3)
- K ∩ ∂(∏_{u∈M} M̄_u) is finite for each (G, M, K) ∈ 𝒦, because K is an irreducible compact curve not contained in the boundary.
- At a puncture p of a piece E, ν(p) ∉ ∏_w M_w. Constant vertices of E take values in M_w, since they are constant on E ⊂ ∏M_w. So some u ∈ M(E) has f_u(p) ∈ ∂M̄_u, and pr_{M(E)} ν(p) ∈ K(E) ∩ ∂.
- Hence the puncture values f_u(p), u ∈ M(E), lie in the finite t-independent set F. Let C_F be the finite set of pointed curves (in all orderings of special points) that occur as components of elements of F.
- For (G, M, K) ∈ 𝒦, u ≠ y ∈ M with pr_y|_K and pr_u|_K non-constant, put Fin(K, u, y) := pr_y(K ∩ pr_u^{-1}(C_F)). This is finite: pr_u|_K is non-constant on the irreducible curve K, so K ∩ pr_u^{-1}(finite set) is finite.
- Let Z ⊂ Δ be the set of t at which Y_t (up to relabelling) lies in C_F or in some Fin(K, u, y). It is countable, and in fact discrete, because Y is holomorphic and non-constant (PR-A). Call t ∉ Z *generic*. (The chain's step 1 is correct as stated.)

### 2.2 Lemma A (no merge, no puncture-move at generic t)
For generic t there is no Q ∈ B_t, lift q, Y_t-copy y at q, and lifted branch c̃ through q such that y is merged along c̃, or y is intact and comp_y is non-constant along c̃ with Q a puncture of the piece of c̃.

*Proof.* This is R7-4 Lemma 1, which I re-checked. In either case there are a piece E, a vertex u ∈ M(E) and a puncture p with comp_y(q) a component of f_u(p) ∈ F. So Y_t ∈ C_F, and t ∈ Z. ∎

### 2.3 Lemma B (new: interior moves at generic t are pure crossings)
Let t be generic. Let Q ∈ B_t with lift q. Let E be a piece at time t with Q ∈ E, i.e. Q is an interior point of E in its own stratum Δ_{G_Q}, with lifted branch Ẽ through q. Let x ∈ M(E) with comp_x(q) ≅ Y_t (an IMOV). Then:
1. for every u ∈ M(E) and every lifted boundary branch c̃ through q, the label u is intact along c̃;
2. if moreover Q is a puncture of the piece E_c of c̃, then comp_u is constant along c̃;
3. let Q = H_t(Q_0), where Q_0 ∈ E_0 := H_t^{-1}(E) is a point at which closure(E_0) meets the closure of another piece D_0 ≠ E_0 (a junction; there are finitely many). Then t ↦ comp_u(q(t)), u ∈ M(E), are holomorphic along a holomorphic choice of lifts, wherever such a choice exists. Concretely, the coordinates of the point Q̂_t ∈ E_t ⊂ ∏M_w over Q_t are holomorphic in t. If the IMOV occurs at this junction for a set of t with an accumulation point in Δ, then the x-coordinate of Q̂_t equals Y_t for all t.

*Proof.*
- Write k := pr_{M(E)}(Q̂) ∈ K(E), so k_x ≅ Y_t.
- (1), (2): Suppose u is merged along c̃, or intact and non-constant with Q a puncture of E_c. By Lemma A's argument, comp_u(q) = k_u ∈ C_F.
  - If u = x, then Y_t ∈ C_F, which is impossible.
  - If u ≠ x, then k ∈ K ∩ pr_u^{-1}(C_F), so Y_t ≅ k_x ∈ Fin(K(E), u, x). This is impossible for generic t.
  - Hence u is intact along c̃, and in the puncture case comp_u is constant along c̃.
- (3): The junction set J_0 := {Q_0 ∈ E_0 : Q_0 ∈ closure(D_0) for some piece D_0 ≠ E_0} is finite. H_t is a stratum-preserving homeomorphism of closures (Lemma B′ of PR-B), so H_t(J_0) is the corresponding junction set at time t.
  - The set {(Q, t) : Q ∈ E_t ∩ closure(D_t)} is the intersection of two analytic families (Lemma R0 of PR-D, and (R1)). It is an analytic set, finite over Δ.
  - t ↦ H_t(Q_0) is a continuous section of it, hence holomorphic. This is the argument of R7-3 Lemma 1(a): a continuous function whose graph lies in a 1-dimensional analytic set finite over Δ is holomorphic off a discrete set, and then everywhere by Riemann extension.
  - The final claim follows from the identity theorem in the coarse space M_x/S_{n_x}, applied to two holomorphic functions of t that agree on a set with an accumulation point. ∎

**What Lemma B leaves.** At generic t, an IMOV at Q is a *pure crossing*:
- every non-constant label of E stays intact along every branch through q, and is constant along every branch for which Q is a puncture;
- the remaining branches through q are pieces of the same stratum Δ_{G_Q} crossing E at Q.

Time-t arguments cannot exclude pure crossings: R7-2 §4.2 gives a local model compatible with (R1), (R2), (i), (ii). So total geodesy at t = 0 is needed. §3 supplies it for crossings inside a single Q-factorial sheet.

## 3. Theorem X: total geodesy forbids Q-Cartier boundary curves through interior points of a piece, inside one sheet

### 3.1 Statement
Let V_0 ⊂ M_g be a closed 2-dimensional totally geodesic subvariety. Smoothness is not needed here. Let Δ_G be a product-type stratum, E a piece of B_0 in Δ_G, and Q_0 ∈ E. Note that Q_0 lies in Δ_G itself, so it is an interior point of E, not a puncture.
- Let 𝓛_0 ⊂ Def(Q_0) be the preimage of closure(V_0) near 0. Let β be a local branch of E at Q_0, with a lift β̃ through 0.
- Let S be an irreducible component of the germ (𝓛_0, 0) containing β̃. Let ν: Ŝ → S be the normalization. Since S is an irreducible germ, ν^{-1}(0) is a single point ŝ_0.
- Let B̂ := ν^{-1}(S ∩ {∏_e s_e = 0}), a curve germ at ŝ_0. Let Ê_1, …, Ê_r be its irreducible components at ŝ_0 that map onto β̃, and C_1, …, C_m the others.

**Theorem X.** There is no holomorphic function G on a neighbourhood of ŝ_0 in Ŝ whose divisor is effective, nonzero, and supported on C_1 ∪ … ∪ C_m. Equivalently, no nonzero effective Q-Cartier divisor is supported on the C_i. In particular:
- (a) no C_i is Q-Cartier at ŝ_0;
- (b) if Ŝ is Q-factorial at ŝ_0 (e.g. smooth, a quotient singularity, or a rational singularity), then m = 0: every boundary curve of S through Q_0 lies over the branch β;
- (c) **(monomial form, valid for any singularity)** there are no integers (n_e)_{e∈E(G)} with Σ_e n_e ord_{Ê_l}(s_e) = 0 for all l, Σ_e n_e ord_{C_i}(s_e) ≥ 0 for all i, and > 0 for some i. Indeed G = ∏ s_e^{n_e} would be such a function.

### 3.2 Proof
Suppose G exists, with div G = Σ c_i C_i, all c_i ≥ 0 and some c_i > 0, defined on a neighbourhood Û of ŝ_0. Then:
- G(ŝ_0) = 0;
- the zero set of G is ∪_{c_i>0} C_i ⊂ B̂, so G has no zeros on Û ∖ B̂;
- G|_{Ê_l} ≢ 0 for every l, since Ê_l is not in the support of the divisor.

Choose a neighbourhood U of Q_0 in M̄_g such that ν^{-1}(preimage of U, intersected with S) ⊂ Û. Shrink U so that the preimage of closure(V_0) ∩ U in Def(Q_0) is a finite union of irreducible components S = S_1, S_2, …, S_k of the germ.

**Step 1 (base point and approximants).**
- Let E^ν be the normalization of E (an open Riemann surface; E ⊂ ∏_w M_w by product type). Let e_0 ∈ E^ν be the point over Q_0 corresponding to β. Choose a closed disc B ⊂ E^ν around e_0 mapping into U, with B ∖ {e_0} mapping into β ∖ {Q_0}.
- Pick P_1 ∈ B ∖ {e_0} generic:
  - Lemma PA applies at P_1;
  - P_1 lies on no other piece;
  - P̃_1 (its lift in β̃) lies on no boundary curve of S other than β̃;
  - ν^{-1}(P̃_1) consists of points on the Ê_l only, where the Ê_l are pairwise disjoint.
- Pick p̂_1 ∈ ν^{-1}(P̃_1), say on Ê_1. The image under ν of a small neighbourhood of p̂_1 is a local branch N of closure(V_0) along E at P_1.
- Apply (PA) with this N: X_n ∈ V_0, lifts X̃_n ∈ S near p̂_1's image, X_n → P_1, and generating pairs (X_n, q_n) whose limit (q_w) has q_j ≠ 0.
- In PR-H the approximants are ν(s_0, τ_n) with s_0 generic and τ_n → 0. So they can be chosen off the at most 1-dimensional analytic set made of the non-normal locus of S and the intersections S ∩ S_i, i ≥ 2.

**Step 2 (the limit disc L).** Let D_n: 𝔻 → M_g be the Teichmüller disc of (X_n, q_n), with D_n(0) = X_n. Since V_0 is totally geodesic, D_n(𝔻) ⊂ V_0. I claim: after passing to a subsequence, D_n → L locally uniformly on 𝔻, where L: 𝔻 → E is holomorphic, non-constant, and L(0) = P_1.

- *Limits stay in Δ_G, in a compact part.* Fix w and put ρ = d_𝔻(0, w). Then d_T(D_n(w), X_n) ≤ ρ.
  - By (Wol), the node curves of P_1 have ℓ_{D_n(w)} ≤ e^{2ρ} ℓ_{X_n} → 0, and every other curve has length bounded below by e^{-2ρ} times its (positive) limit at P_1.
  - By (Ab), every limit point Z of D_n(w) lies in Δ_G, and the length functions of its components are within a factor e^{2ρ} of those of P_1. So Z lies in a compact set K_ρ ⊂ Δ_G ≅ ∏M_w.
  - Also Z ∈ closure(V_0) ∖ M_g ⊂ B_0.
- *Local uniform convergence.* Orbifold charts Def(Z), Z ∈ K_ρ, can be taken of uniform size, since K_ρ is compact in the open stratum. If |w' − w| < r with r small (depending only on ρ), the same length estimate shows that D_n(w') lies in the chart of any limit point Z of D_n(w), for all large n of the subsequence.
  - Each D_n restricted to a small disc around w lifts holomorphically into Def(Z). Indeed, D_n is the image of a Teichmüller disc in T_g, and the component of the preimage in T_g of the chart's interior maps holomorphically onto Def(Z)° (standard description of the Deligne–Mumford boundary charts: Bers, Earle–Marden, Hubbard–Koch; cited).
  - The lifts are bounded, so Montel applies. A diagonal argument over a countable cover of 𝔻 gives the locally uniform limit L, holomorphic in charts, with values in B_0 ∩ Δ_G and L(0) = P_1.
- *Non-constant.* By (Fl) and q_j ≠ 0, the j-component of L(w) is A_w·(Y_j(P_1), q_j). Here w ↦ A_w·(Y_j, q_j) =: τ(w) is the Teichmüller disc of (Y_j(P_1), q_j) in M_j := M_{g_j,n_j}. It is non-constant.
- *Image in E.* B_0 ∩ Δ_G is a 1-dimensional analytic set, and L^{-1} of each of its finitely many irreducible components meeting L(closed disc of radius R) is analytic. These preimages cover the disc, so one of them is everything. P_1 lies only on E. Hence L(𝔻) ⊂ E. Since 𝔻 is normal and L(𝔻) ⊄ Sing(E), L lifts to E^ν; I keep the name L.

**Step 3 (L: 𝔻 → E^ν is surjective).**
- Let τ̃: 𝔻 → T(Y_j) be the Teichmüller disc lifting τ. By (Prop) its image Δ̃ is a closed 1-dimensional submanifold, and its Mod-translates form a locally finite family.
- τ(𝔻) ⊂ f_j(E) ⊂ C_j° := f_j(Ē) ∩ M_j, which is an irreducible closed analytic curve in M_j (j ∈ M(E), since τ is non-constant).
- So Δ̃ is an irreducible component of the preimage 𝒞 of C_j° in T(Y_j). By local finiteness, the image of Δ̃ in M_j is closed and analytic, hence equal to C_j°.
- With Γ := Stab_{Mod}(Δ̃), the map 𝔻/Γ → C_j° (via τ̃) is proper.
- τ factors through the normalization Ĉ_j of C_j°, and f_j: E^ν → Ĉ_j is a finite map of normal curves.
- The set Λ of holomorphic λ: 𝔻 → E^ν with f_j∘λ = τ is finite, with at most deg f_j elements: a lift is determined by its value at one point over an unbranched value.
- Γ acts on Λ by precomposition, since τ∘γ = τ. So Γ_L := Stab_Γ(L) has finite index, and L descends to L̄: 𝔻/Γ_L → E^ν.
- f_j∘L̄ is proper (finite index in a proper map), so L̄ is proper: L̄^{-1}(K) is a closed subset of (f_j L̄)^{-1}(f_j K).
- A proper non-constant holomorphic map to the connected Riemann surface E^ν is surjective. In particular e_0 ∈ L(𝔻).

**Step 4 (a path to the crossing point).**
- Let W be the connected component of L̄^{-1}(int B) containing [0]. Then L̄|_W: W → int B is proper and non-constant, hence surjective. Pick [w*] ∈ W with L̄([w*]) = e_0.
- Join [0] to [w*] by a path in W and lift it to a path π from 0 to w* in 𝔻. Path lifting holds for quotients by properly discontinuous actions (Bredon II.6; cited).
- Let Ω be a connected relatively compact open neighbourhood of π with L(Ω̄) ⊂ ν-image of B ⊂ U. Then L(π) ⊂ B, and w* ∈ Ω with L(w*) = e_0, i.e. L(w*) = Q_0 approached along β.

**Step 5 (Hurwitz).**
- For large n, D_n(Ω̄) ⊂ U ∩ V_0 by uniform convergence. Lift D_n|_Ω to D̃_n: Ω → Def(Q_0) as in Step 2, with D̃_n(0) = X̃_n.
- D̃_n(Ω) lies in the interior part of 𝓛_0 = S_1 ∪ … ∪ S_k. The sets D̃_n^{-1}(S_i) are analytic subsets of the connected Ω covering it, so one of them is Ω. Since X̃_n lies only in S, D̃_n(Ω) ⊂ S.
- D̃_n(Ω) ⊄ non-normal locus (it contains X̃_n), so D̃_n lifts to D̂_n: Ω → Ŝ, with D̂_n(Ω) ⊂ Û ∖ B̂.
- Hence **G∘D̂_n has no zeros on Ω**.
- Embed Û in some C^M. By Montel, a subsequence D̂_n → L̂ locally uniformly on Ω, where ν∘L̂ is a lift of L. Then:
  - L̂(w*) ∈ ν^{-1}(0) = {ŝ_0}, so **G∘L̂(w*) = 0**;
  - near 0, L̂ takes values in ν^{-1}(β̃-lift of L), which near the generic point P̃_1 is the disjoint union of the Ê_l. By connectedness L̂ maps a neighbourhood of 0 non-constantly into one Ê_l, where G ≢ 0. So **G∘L̂ ≢ 0**.
- By Hurwitz, G∘L̂ has no zeros on Ω, which contradicts G∘L̂(w*) = 0. ∎

**Remarks.**
1. *Intuition.* The Teichmüller discs D_n are holomorphic curves in the interior of the sheet S that converge to the whole branch β of E, through Q_0. Any Q-Cartier curve C through Q_0 meets β with positive local intersection number, so it would meet D_n. But C lies in the boundary and D_n does not. Total geodesy enters only through the existence of these discs: Lemma PA for positive area, then (Fl) and (Prop) to make L sweep all of E.
2. *Non-product strata.* The proof uses product type only to have the global coordinate f_j on E. For non-product G one would work on the lifted piece in ∏M_w. I have not checked this.
3. *Sanity check.* In the local crossing model of R7-2 §4.2 (the t = 0 version), S = {s_1 = z s_2} ⊂ C³ is smooth, E is the z-axis, and D = {z = s_1 = 0}. Theorem X(b) excludes it: G = z|_S has zero set exactly D. At interior points of boundary divisors of M̄_{0,5}, and in the quintic example, no second boundary curve passes through an interior point of a piece, so nothing is contradicted there.

## 4. Consequences for the crossing (IMOV) obstacle of MS8

### 4.1 Lemma S (sheets are topological and are transported by H_t)
For Q ∈ B_t, the irreducible components ("sheets") of the germ of closure(V_t) at Q are in canonical bijection with the elements of lim← π_0(V_t ∩ W), taken over neighbourhoods W of Q and keeping only components whose closure contains Q. A boundary branch b at Q lies in the sheet corresponding to a component if b ∖ {Q} lies in the closure of that component, for all W.

Consequently H_t maps sheets at Q_0 bijectively onto sheets at H_t(Q_0), compatibly with the boundary branches they contain.

*Proof.*
- For an analytic germ (X, Q), the irreducible components correspond to lim← π_0(Reg(X) ∩ W). This is the standard local description: a germ is irreducible iff its regular part is locally connected at Q.
- Here X = closure(V_t), and Reg(X) ∩ W ∖ V_t lies in the 1-dimensional boundary. That set has real codimension 2 in the manifold Reg(X), so removing it does not change π_0.
- The description is purely topological in the pair (closure(V_t), V_t). By (R2), H_t is a homeomorphism of pairs (closure(V_0), V_0) → (closure(V_t), V_t) that preserves strata and pieces (PR-B). ∎

### 4.2 Corollary X′ (crossings inside a Q-factorial sheet do not occur, at any time)
Let E_0 be a piece of B_0 in a product-type stratum, Q_0 ∈ E_0, and D_0 ≠ E_0 a piece with Q_0 ∈ closure(D_0). Suppose some sheet S of closure(V_0) at Q_0 contains a branch of E_0 and a branch of D_0. Suppose also that the normalization Ŝ is Q-factorial at the point over Q_0, or more generally that the monomial criterion of Theorem X(c) applies. Then we get a contradiction. So such (Q_0, E_0, D_0, S) do not exist.

Transported by Lemma S: let t ∈ Δ be arbitrary. If E_t := H_t(E_0) and D_t meet at Q_t = H_t(Q_0) inside a common sheet, then E_0 and D_0 meet at Q_0 inside a common sheet. The Q-factoriality condition is imposed at t = 0.

*Proof.* The lifted branch of D_0 in S gives a boundary curve C of Ŝ through ŝ_0 that does not lie over the branch β of E_0. If Ŝ is Q-factorial, some multiple mC is Cartier, and G := a local equation of mC contradicts Theorem X. ∎

### 4.3 What this does to the IMOV endpoint of the chain
Combine with Lemma B. Suppose Y is non-constant and t is generic. Then an IMOV at Q_t, with the Y_t-network entering E_t from a piece D_t on which x is constant, is a pure crossing at the junction Q_t = H_t(Q_0). By Corollary X′ it is impossible if E_0 and D_0 share a Q-factorial sheet at Q_0. **The crossing obstacle therefore reduces to:**
- **(Cr1) two-sheet crossings:** E_0 and D_0 meet at Q_0 but lie in different sheets of closure(V_0) at Q_0. Every sheet containing E_0's branch has boundary lying over E_0 at Q_0 (Theorem X(b), when Q-factorial). The network passes from E to D through a point where two different local sheets of closure(V_t) touch.
- **(Cr2) non-Q-Cartier crossings:** the common sheet has a non-Q-factorial (hence non-rational) normal singularity over Q_0, and the monomial criterion fails. That is, the normalized order vectors (ord_C(s_e)/ord_{Ê}(s_e))_e of the other boundary curves C positively span, modulo constants, a linear subspace.

Neither is excluded here.
- For (Cr1), local Krull/Hurwitz arguments cannot help: the two sheets are separate analytic germs, and the discs in the E-sheet never see the D-sheet.
- For (Cr2), the discs D_n may pass "around" C through the exceptional curves of a resolution.

**Note on Proposition K's endpoint.** If Prop K's MOV branch is "touching" (Q_0 an interior point of E_b), and Q_0 is also on the closure of the STAY piece through which K_0 arrives, in the same Q-factorial sheet as E_b, then Theorem X excludes this configuration at t = 0 already. So for those V_0, Prop K's endpoint is MERGE, puncture-MOV, or a two-sheet / non-Q-Cartier touching. This partially answers R7-2 Open question 2.

## 5. Twins: what is still missing (no new resolution)

Under (Rig) the time-t picture at generic t is canonical. With Y non-constant and t generic:
- a component of a boundary point is a Y_t-copy iff its class is exactly Y_t;
- by Lemma A no Y_t-copy merges or moves at a puncture;
- by Lemma B every IMOV is a pure crossing, and by Corollary X′ a two-sheet or non-Q-Cartier one.

The obstruction is entirely at t = 0. One needs a statement of the following form, about V_0 alone.

**(MS7*) Needed t = 0 statement.** Let V_0 be a smooth closed totally geodesic surface. There is no assignment Q ↦ L(Q) ⊂ {Y_0-copy labels of Q} on the connected component B_0^∂ of B_0 containing ∂V_0 with all of the following properties:
- L(Q) ≠ ∅ and L(Q) is Aut(Q)-invariant;
- vertex i ∈ L on ∂V_0;
- for every branch b at Q, some lift a·b̃ keeps every label of L(Q) intact, and constant if Q is a puncture of b's piece, and continues it into L at nearby points;
- the only exceptions are two-sheet / non-Q-Cartier pure crossings.

Lemma A, Lemma B and the closedness/spreading lemmas (R7-1 Lemma 2, R7-4 Lemma 4) show that if Y is non-constant, then the limits as t → 0 of the Y_t-copies form such an assignment. So **(MS7*) ⇒ MS8.** This is the content of R7-3 §5 (MS7), updated by Lemma B and Theorem X; I re-checked the implication.

Prop K proves the twin-free special case (Theorem A of R7-2 / R7-3). What fails in general is the one thing Prop K's marked track cannot see: at a junction J with σ ∈ Aut(J), σx ≠ x, the track may continue on x while L(J) continues on σx (R7-3 §4–5).

The planner's mechanism 5(b) remains a sketch. It runs as follows:
- A twin jump of an *interior-transported* track at time t requires the square (s, τ) ↦ H_τ(γ(s)) to meet points of 𝒱 where the orbifold covering of 𝒱 is branched in complex codimension 1 ("reflection points"), with a reflection α that exchanges Σ_i and a twin.
- Limits of such points are boundary points W ∈ B_τ with α ∈ Aut(W) exchanging two copies. So the two copies have equal classes at time τ.
- If this happens for a set of τ with an accumulation point, and the two copies are carried by constant vertices with holomorphic classes, then the classes agree identically. That is (Lock), and Theorem T of R7-1 then applies.

What I could not close:
- (i) the copies at W may be carried by *non-constant* vertices, which gives no identity;
- (ii) the times τ at which reflection points occur depend on the square, and need not accumulate;
- (iii) the continuity principle of R7-6 needs its chart-size uniformity near junctions repaired as well.

So this route is **not** a proof.

## 6. Summary: proved / not proved / open

**Proved here (modulo the cited standard facts of §1, and Lemma PA as a prior result):**
1. §2.1: the finite set F and the generic-time set Z under (Rig). The chain's steps 1 and 3 consequence are correct.
2. Lemma B (new): under (Rig), at generic t, every IMOV is a pure crossing at a junction point, whose coordinates are holomorphic in t.
3. **Theorem X (new, t = 0, total geodesy):** at an interior point Q_0 of a piece E, no sheet of closure(V_0) containing a branch β of E carries a nonzero effective Q-Cartier divisor supported on boundary curves not lying over β. In particular such curves are absent when the sheet's normalization is Q-factorial (e.g. smooth, quotient or rational singularity), and the monomial criterion (c) excludes them at any singularity.
4. Lemma S and Corollary X′: crossings inside a common Q-factorial sheet never occur, at any time t. The crossing obstacle of MS8 is reduced to two-sheet crossings (Cr1) and non-Q-Cartier crossings (Cr2). The same applies to Prop K's "touching MOV" endpoints.

**Not proved:**
- **MS8 itself.** I have neither a proof nor a counterexample.
- The non-product-stratum version of Theorem X (Remark 2).
- Fact (Fl) is cited, not proved.

**Open (precisely):**
- (O1) **Twins:** (MS7*) of §5, i.e. whether an Aut-closed system of constant Y_0-copies without merges can exist on B_0^∂ for a smooth closed totally geodesic V_0. Equivalently: whether a twin jump (R7-3 Theorem B) can occur.
- (O2) **Crossings (Cr1):** whether the Y-network can pass, at a junction point, between two *different* sheets of closure(V_0), entering a piece on which the copy moves.
- (O3) **Crossings (Cr2):** non-Q-factorial common sheets where the monomial criterion fails.
- (O4) Entry 69 (the input (Rig) itself): untouched, as instructed.

**On the chain's derivation of the problem from MS8.** I found no flaw in it:
- (Rig) gives the finite set F exactly as stated, because constant coordinates of a piece lie in the open strata M_w.
- Holomorphy of Y (PR-A) and the identity theorem give the countable/discrete generic set.

=== END OF ANSWER round8_q1 ===

