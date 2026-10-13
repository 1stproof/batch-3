# round6_q8 — attempt on MS5 / (T0)

## Plan (written first)
1. Weaken (T0) to a single-branch version (T0_1) and re-prove Theorem P under it. This is rigorous and short.
2. Construct a "merge branch" at a cusp of dV_0 from Wright's cylinder deformation theorem (cylinder-stretch limits). This gives (a) under an explicit hypothesis (H-cyl).
3. Analyse (b) on that branch. Isolate exactly what is missing.
4. Record the obstructions (accidental copies of Y_0, product type of the new stratum, interchange of limits). State the status and the open questions.

Status line (updated at the end): see Section 6.

Readings (R1), (R2) of the task file are used throughout, with H_0 = id. Notation as in the task file: for a 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, 𝐂_E is the closure of ξ_G^{-1}(E) in ∏_w M̄_w, and E_t := H_t(E).

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

## 2. A merge branch from cylinder stretches

### 2.1 Cited results (from memory) and two easy facts

**(W) Wright's cylinder deformation theorem** (A. Wright, "Cylinder deformations in orbit closures of translation surfaces", Geom. Topol. 19 (2015); from memory).
- Let (Z,ω) be a translation surface and N its GL_2(ℝ)-orbit closure.
- Let 𝒞 be an N-equivalence class of horizontal cylinders. Two parallel cylinders are N-equivalent if they stay parallel on a neighbourhood of (Z,ω) in N.
- Let a^𝒞_s act by diag(1, e^s) on the cylinders of 𝒞 and trivially on the rest of Z.
- Then a^𝒞_s(Z,ω) ∈ N for all s ∈ ℝ.

The same holds for a union of equivalence classes, because the deformations of different classes commute.

**Quadratic differentials.** Let (X,q) be a half-translation surface and (Z,ω) its holonomy double cover, with involution ι. Then ι maps N to N, and maps equivalence classes to equivalence classes.
- If 𝒞 is a union of classes, then 𝒞 ∪ ι𝒞 is an ι-invariant union of classes.
- Its stretch commutes with ι, so it descends to X.
- The double covers form a closed GL_2(ℝ)-invariant set, so the deformed surface is again a double cover of a point of the orbit closure of (X,q).

Call a family 𝒞 of horizontal cylinders of (X,q) *admissible* if its preimage in Z is a union of equivalence classes. For admissible 𝒞, write a^𝒞_s(X,q) for the descended stretch.

**Fact 2.1 (generating pairs are closed and invariant).** Let M_V := {(X,q) : X ∈ V_0, q ∈ Q_V(X)}. Then M_V is closed in the bundle of quadratic differentials over M_g, and it is GL_2(ℝ)-invariant.

*Proof.*
- Invariance: g·(X,q) generates the same Teichmüller disc as (X,q).
- Closedness: the Teichmüller disc map depends continuously on (X,q) ≠ 0. A limit of discs contained in V_0 lies in the closure of V_0 in M_g, which is V_0, because V_0 is closed in M_g. ∎

Hence the orbit closure of any generating pair lies in M_V. So by (W), for admissible 𝒞, the underlying surface X_s of a^𝒞_s(X,q) lies in V_0 for all s.

**Fact 2.2 (the stretch limit).** Let 𝒞 = {C_1, …, C_r} be disjoint maximal horizontal cylinders of (X,q), with cores γ_k pairwise non-homotopic, circumferences c_k and heights h_k. Let K̂(X,𝒞) be the stable curve obtained as follows:
- cut each C_k along its core;
- glue a half-infinite cylinder of circumference c_k to each of the two new boundary circles;
- fill in the punctures and identify the two punctures coming from C_k to a node.

Then X_s → K̂(X,𝒞) in M̄_g as s → +∞. The dual graph of K̂(X,𝒞) is the dual graph of the multicurve {γ_k}.

*Proof.*
- On a half-infinite cylinder {Im w > 0}/c_kℤ use the coordinate z = exp(2πi w/c_k), which identifies it with the punctured unit disc.
- X_s is obtained from K̂ by removing, at the two punctures of node k, the discs |z| < exp(−π e^s h_k/c_k) and |z′| < exp(−π e^s h_k/c_k), and gluing the remaining annuli by z z′ = ρ_k(s). Here |ρ_k(s)| = exp(−2π e^s h_k/c_k), and the argument of ρ_k(s) is fixed by the twist of C_k.
- This is the standard plumbing construction at the nodes of K̂ with fixed coordinates.
- Plumbing with fixed coordinates is continuous at ρ = 0 into M̄_g (it gives the standard local charts of M̄_g near K̂; Bers, Wolpert; cited from memory). Since ρ_k(s) → 0, X_s → K̂.
- The statement about the dual graph is topological. ∎

**Lemma 2.3 (stretch limits of nearby surfaces stay nearby).** Let X_n → P in M̄_g. Let 𝒞_n be families of disjoint maximal cylinders of generating pairs (X_n,q_n) whose cores are homotopic, in markings compatible with the convergence, to a fixed set of curves pinched at P. Suppose the minimal modulus of the cylinders in 𝒞_n tends to ∞. Then K̂(X_n,𝒞_n) → P.

*Proof (sketch; standard conformal surgery, not fully written).*
- Put W_n := X_n minus the cores of 𝒞_n. Then W_n embeds conformally both in X_n (with complement the cores) and in K̂_n := K̂(X_n,𝒞_n) minus its nodes (with complement punctured discs inside half-annuli of modulus m_{n,k}/2 → ∞).
- Use extremal length Ext.
  - Curves crossing a core have Ext → ∞ on both surfaces, by Minsky's inequality Ext(α)Ext(β) ≥ i(α,β)^2.
  - Cores have Ext → 0 on both.
  - For a curve β disjoint from the cores and not homotopic to one, Ext_{W_n}(β) ≥ max(Ext_{X_n}(β), Ext_{K̂_n}(β)) by monotonicity.
  - Conversely, removing the core of an annulus of modulus m (or a cusp neighbourhood of depth m) raises Ext of curves not crossing it by a factor 1 + o(1) as m → ∞. I cite this from memory as a standard estimate and have not proved it.
- Hence the Ext-spectra of X_n and K̂_n on the curves not crossing the cores agree up to factors → 1.
- By Kerckhoff's formula d_T = ½ log sup Ext_Y/Ext_X (Kerckhoff 1980; from memory), applied on the components of the stratum of augmented Teichmüller space, the two sequences have the same limits in M̄_g. ∎ (sketch)

The marked version is also used: if the marked X̃_n converge in augmented Teichmüller space T̄ to P̃, then so do the marked K̂_n. Moreover, the pieces of S \ (cores) converge as marked stable curves. The same sketch applies.

### 2.2 Hypothesis (H-cyl) and the merge branch

**Hypothesis (H-cyl).** There are:
- a point P_∞ ∈ closure(∂V_0) \ ∂V_0 lying in a product-type stratum Δ_{G'};
- a local branch β of ∂V_0 at P_∞;
- a marked lift P̃_∞ ∈ T̄ with pinched multicurve μ′ = μ_Γ ⊔ μ_X, where marked lifts of points of β converge to P̃_∞ and pinch exactly μ_Γ;
- generating pairs (X_n,q_n), X_n ∈ V_0, with marked X̃_n → P̃_∞;

such that, for every n, q_n has an admissible family 𝒞_n of horizontal cylinders whose cores are exactly the curves of μ_X, one cylinder for each curve, with minimal modulus → ∞.

Note that μ_X ≠ ∅, because P_∞ ∉ Δ_Γ.

**Proposition S.** Assume (H-cyl), and Lemma 2.3 in its marked form. Let G″ be the dual graph of μ_X; equivalently, G″ = G′ with the μ_Γ-edges contracted. Then:
1. K̂_n := K̂(X_n,𝒞_n) ∈ closure(V_0) ∩ Δ_{G″}, and K̂_n → P_∞.
2. There is a local branch β″ at P_∞ of a 1-dimensional irreducible component E″ of closure(V_0) ∩ Δ_{G″}, and β″ contains K̂_n for infinitely many n.
3. Let κ_Γ, κ be the patterns G′ → Γ and G′ → G″ defined by μ_Γ ⊂ μ′ and μ_X ⊂ μ′, in the marking of P̃_∞. Let i′ be the vertex of G′ with κ_Γ(i′) = i, and u := κ(i′). Then L_β = glue_{κ_Γ}(P̂_∞) and R_{β″} = glue_κ(P̂_∞), and R_{β″,u} ∈ ∂M̄_u.

In particular, if G″ is of product type and the only pair of patterns realising (L_β, R_{β″}) is (κ_Γ, κ), then S = {u} and condition (a) of (T0_β) holds for (G, G′, P_0, β, β″) = (G″, G′, P_∞, β, β″). There, "only pair" means the automorphisms of P̂_∞ compatible with the gluings create no other patterns.

*Proof.*
1. **K̂_n lies in closure(V_0) ∩ Δ_{G″}.** By (W) and Fact 2.1, the underlying surface of a^{𝒞_n}_s(X_n,q_n) lies in V_0 for all s. By Fact 2.2 it converges to K̂_n as s → ∞, so K̂_n ∈ closure(V_0). Its dual graph is that of the multicurve μ_X, which is G″. By Lemma 2.3, K̂_n → P_∞.
2. **The branch β″.**
   - closure(V_0) is an irreducible 2-dimensional algebraic subset of M̄_g, because V_0 is a closed subvariety of the quasi-projective variety M_g. Hence closure(V_0) ∩ ∂M̄_g has dimension ≤ 1.
   - Consider the analytic germ A of closure(V_0) ∩ closure(Δ_{G″}) at P_∞. Only finitely many of its irreducible germs contain points of Δ_{G″}, so one of them, A_1, contains K̂_n for infinitely many n.
   - A_1 ⊂ ∂M̄_g, so dim A_1 ≤ 1. Also A_1 ≠ {P_∞}, because P_∞ ∉ Δ_{G″}. Hence A_1 is an irreducible curve germ, i.e. a single local branch β″.
   - The points of β″ \ {P_∞} near P_∞ lie in Δ_{G″}: the deeper strata meet β″ in a closed analytic subset that does not contain K̂_n, so it is {P_∞} near P_∞.
   - β″ lies in a unique irreducible component E″ of the 1-dimensional set closure(V_0) ∩ Δ_{G″}.
3. **The lifts and the merge.**
   - The marked K̂_n converge to P̃_∞ in T̄, and their pieces (the components of S \ μ_X) converge as marked stable curves. Hence the G″-lifts of K̂_n converge to glue_κ(P̂_∞), so R_{β″} = glue_κ(P̂_∞).
   - In the same way, L_β = glue_{κ_Γ}(P̂_∞).
   - Γ has at least two vertices. If i were the only vertex, then Δ_Γ ≅ M_{g_i,n_i} (up to a finite quotient), and π_i constant on ∂V_0 would make ∂V_0 a point. Γ is connected, so i has an edge e to another vertex.
   - Vertex i stays intact along β. Indeed L_{β,i} = Y_0 is smooth, so κ_Γ^{-1}(i) = {i′}, and no μ_X-curve lies in the piece i′.
   - So the edge of G′ corresponding to e is a μ_Γ-edge at i′, and κ contracts it. Hence R_{β″,u} contains at least two pieces of P̂_∞ glued at a node, so R_{β″,u} ∈ ∂M̄_u. ∎

**Remark 2.4 (bridges).** In (H-cyl) one may allow μ′ = μ_Γ ∪ μ_X with μ_Γ ∩ μ_X ≠ ∅. That happens when a Γ-curve and an X-curve are homotopic, which is the "contracted bridge" of PR-F §5. The proof of Proposition S then gives (a) if and only if some μ_Γ-edge at i′ is not in μ_X. If every edge at i′ is in μ_Γ ∩ μ_X, then K̂_n pinches all curves around the island and there is no merge. For cyclic covers of M_{0,5}, Corollary N(c) of PR-G shows that, for each Γ-edge at i, at least one of the three possible second collisions D_{kl} makes that edge a non-bridge. So in that class (a) holds at the corresponding cusp for the branch over D_{kl}, with the lifted base cylinder as 𝒞. Base cylinders lift to cylinder families that are admissible, because the orbit closure of the lifted locus is the lift of the full genus-0 stratum, in which a cylinder's class consists of the cylinders homologous to it on the double cover. I did not re-verify that last point in detail.

**Comment.** This is the "second branch at a cusp with the merge property" (C-merge, PR-C), obtained without any local analytic analysis: the cylinder deformation theorem supplies it. What the cylinder stretch does geometrically is to make the X-curves infinitely long tubes while keeping the Y_0-island and its attaching Γ-curves unchanged. The island therefore stays attached, at a fixed small size, to the rest of its complementary component.

## 3. Condition (b) on the merge branch: what is and is not available

**3.1 What the stretch gives at u.** The u-component of K̂_n carries the limit differential η_{n,u}: q_n restricted to the part of the complement of 𝒞_n that lies in u, with half-infinite cylinders attached. So η_{n,u} has double poles with non-zero quadratic residue (c_k^2 up to normalisation) at the new nodes. It has infinite area, and Lemma T′ of PR-F (which needs a finite positive-area limit) does not apply to it.

**3.2 A disc in π_u(E″), but not an isometric one (proved, modulo (F2) for infinite area).**
- For g in the upper-triangular group B ⊂ SL_2(ℝ), g maps horizontal cylinders to horizontal cylinders. Its action commutes with the stretch up to shears inside the cylinders, which converge to twists at the nodes.
- So g·(X_n,q_n) satisfies the hypotheses of Fact 2.2 with the family g𝒞_n, and K̂(g·(X_n,q_n), g𝒞_n) ∈ closure(V_0) ∩ Δ_{G″}. Its u-component is g·(Y_u, η_{n,u}).
- B acts simply transitively on SO(2)\SL_2(ℝ) ≅ ℍ. The map k ↦ [k η̄/|η|] is holomorphic into T_u, by holomorphic dependence of solutions of the Beltrami equation on parameters (Ahlfors–Bers). Hence the u-components of the points of E″ near K̂_n contain the image of a non-constant holomorphic map 𝔡 : ℍ → M_u, the *affine disc* of η_{n,u}.
- If (Y_u, η_{n,u}) is not affinely rigid, then 𝔡 is non-constant. Rigidity is excluded because the island of Y_0 together with an attached positive-area region deforms. This is plausible but I have not proved it.
- However, 𝔡 is in general **not** an isometry for d_T. The dilatation of an affine map on a half-infinite cylinder can be removed near the puncture: a stretched half-infinite cylinder is again a punctured disc. So the extremal map in the class of g has smaller dilatation than ‖g‖ unless the finite-area part forces it.
- Example (covering model): for the branch over D_{34} of a cyclic cover of M_{0,5}, π_u(E″) *is* a Teichmüller curve. It is the pull-back of the Teichmüller disc of an integrable differential on the 4-pointed base component, with simple poles, not of the base differential with a double pole at the node. So (b) can hold even though the affine disc of η_{n,u} is not isometric. To prove (b) one needs another generating limit at u.

**3.3 Conditional statement (proved modulo (F), (F2) of PR-F).**

**Proposition 3.1.** In the situation of Proposition S, suppose that:
- (PA″) some point P′ of β″ \ {P_∞} has a sequence of generating pairs (Z_m, ζ_m) → P′, with Area(ζ_m) = 1, for which the vertex u carries positive area;
- P′ lies on no other component of closure(V_0) ∩ Δ_{G″}.

Then (b) holds for (E″,u), with an orbifold-unramified isometric lift.

*Proof.* Apply Lemma T′ of PR-F, parts 1 and 2, at P′ with stratum G″ and vertex v = u. The component it produces is the one through P′, which is E″. ∎

**3.4 Why (PA″) is plausible, and what blocks a proof.**
- *Heuristic (residue count).* As s → ∞, the curves P(Q_V(X_{n,s})) ⊂ P(Q(X_{n,s})) accumulate on a compact connected set L_n of projective stable quadratic differentials on K̂_n. Each P(Q_V(X)) is homeomorphic to P(T_X V_0) ≅ S², via q ↦ [q̄/|q|].
- Suppose L_n contains a curve, and the quadratic residues at the |μ_X| new nodes are proportional on L_n. A proportionality of this kind holds for differentials near a^{𝒞}_s q_n, because the cylinders of 𝒞_n are equivalent, so their circumferences have a locally constant ratio on the orbit closure. Then some ζ ∈ L_n has all these residues equal to 0.
- Such a ζ is integrable and non-zero. If it is non-zero on u, and the approximating ζ_m do not leak area into the collars of the X-curves, then (PA″) holds.
- In the covering model all of this is true: Q_V is a rank-2 vector bundle that extends over M̄_{0,5}, and the zero-residue line lives on the merged component.
- *Blocks.* In general:
  - (B1) Q_V(X) is a cone, not a linear space, so L_n might collapse to a point;
  - (B2) proportionality of residues is only known near the stretched differential, not on all of L_n;
  - (B3) the zero-residue limit could vanish on u (all its area on other components of K̂_n);
  - (B4) area leakage into the long collars must be controlled. This needs the residue of ζ_m to be o(1/modulus).
- This is the planner's "rank-1 residue count", now at the stretch branch rather than along ∂V_0. It is not proved.

## 4. On hypothesis (H-cyl)

(H-cyl) is an assumption about generating pairs near a cusp of ∂V_0. A natural route, extending PR-F §6, follows; every step marked (G) is a gap.
1. (PA) at a generic P ∈ ∂V_0 gives a positive-area vertex j ≠ i with a lattice surface (Y_j,η_j) (PR-F, Lemma T′ and Proposition C). (G0): (PA) itself is unproved.
2. Rotate so that the horizontal direction is periodic for (Y_j,η_j) (Veech dichotomy). By Lemma G′ of PR-F, the limit map φ along the diagonal flow tends to a cusp P_∞ ∈ closure(∂V_0) \ ∂V_0 at which the horizontal cylinder cores of η_j (the curves μ_X) are pinched in addition to Γ.
3. On (X_n,q_n) → P the horizontal cylinders D_k of the top level persist as cylinders D_{n,k} (cylinders persist under small deformation of the flat structure away from the islands). (G1): they are parallel on X_n only if they are equivalent for the orbit closure of (X_n,q_n). Being parallel on the boundary surface does not imply this.
4. Let 𝒞_n be the equivalence class (on the double cover) of the D_{n,k}. (G2): 𝒞_n might contain cylinders inside the islands, or might miss some D_{n,k}.
   - Island cylinders have circumference → 0 relative to the D_{n,k}. Equivalent cylinders have a locally constant ratio of circumferences, whose value is defined over the field of definition of the orbit closure. So (G2) would follow from a *finiteness of circumference ratios* for equivalent cylinders along sequences tending to the boundary. I expect this from the Mirzakhani–Wright description of boundary orbit closures, but I have not proved it.
5. Replace (X_n,q_n) by a^{𝒞_n}_{s_n}(X_n,q_n) with s_n large, so that the moduli tend to ∞, and pass to a diagonal subsequence. (G3): the result must converge to P_∞, not merely to some point of closure(V_0) pinching μ_Γ ∪ μ_X. This is the interchange of the limits n → ∞ and s → ∞. I expect it to follow from Lemma 2.3 together with the fact that, with the islands removed, the stretched top level is close to the stretched (Y_j,η_j). Not written.
6. (G4): the strata Δ_{G′} and Δ_{G″} must be of product type, and the pattern ambiguity in Proposition S must be absent or harmless. Theorem P″ is stated only for product-type strata. For strata with graph automorphisms one would have to redo Section 1 on the finite cover ∏M̄_w → closure(Δ_G). I have not done this.

## 5. Counterexample search (negative result only)

I looked for a V_0 at which every candidate fails.
- **Covering constructions from M_{0,5} (cyclic).** Here (H-cyl) holds with lifted base cylinders, and (a) holds at a suitable cusp by Remark 2.4 and Corollary N(c). (b) holds because the branch over D_{kl} is a pulled-back Teichmüller curve. So under the weaker (T0_β) there is no counterexample in this class, apart from the pattern/automorphism ambiguity (G4). I have not checked that ambiguity case by case.
- **Bridge mechanism.** A counterexample would need, at every cusp and for every second collision, all Γ-edges at i to be bridges (Remark 2.4). Corollary N(c) excludes this for cyclic covers.
- **Primitive totally geodesic surfaces** (McMullen–Mukamel–Wright, Eskin–McMullen–Mukamel–Wright; from memory, they live in M_{1,3}, M_{1,4} and related spaces with marked points). They are outside the problem's setting M_g, or I do not know their boundary well enough to test them.
- No counterexample was found. Note also that the original (T0), which quantifies over *all* components through P_0 and *all* vertices containing a copy of Y_0, can fail for reasons irrelevant to the problem: accidental copies, and ∂V_0 itself passing through P_0 inside Δ_G when G ≅ Γ. This is why Section 1 replaces it by (T0_β), which is all the chain uses.

## 6. Status

**Proved (rigorous, given (R1), (R2) and the cited prior results):**
- Theorem P′ and Theorem P″. The chain only needs (T0_β): one product-type stratum pair (G,G′), one cusp or boundary point P_0, one local branch β″ of one boundary curve E, the single limit lift R_{β″}, and only the vertices that can carry the genuine Y_0-component. The universality over all components and all copies of Y_0 in (T0) is unnecessary.
- Fact 2.1 and Fact 2.2 (given the standard plumbing charts of M̄_g), and Proposition S parts 1–3 given Lemma 2.3 and (H-cyl). This yields condition (a) of (T0_β) at a cusp, via Wright's cylinder deformation theorem (cited from memory).

**Sketched only:** Lemma 2.3 (conformal surgery on long cylinders); Remark 1.1; the admissibility claim in Remark 2.4; the affine-disc construction in 3.2.

**Not proved (open), so the task statement is NOT established:**
- (Q1) (H-cyl): gaps G0–G4 of Section 4.
- (Q2) Condition (b) on the merge branch E″, i.e. (PA″) of Proposition 3.1: blocks B1–B4.
- (Q3) Product type of Δ_{G″} and absence of pattern ambiguity (G4); otherwise Theorem P″ needs an orbifold version.
- (Q4) Condition (O) of PR-E, which remains an input of the chain and was not part of this task.

**Assessment of the chain.** The chain is sound as far as I can check, with three amendments:
- it can and should use (T0_β) instead of (T0);
- Theorem P/P″ needs product type for both Δ_G and the stratum Δ_{G′} of P_0, to track the genuine component;
- the original (T0) is strictly stronger than needed, and can fail for irrelevant reasons (accidental copies of Y_0, or a second component through P_0 without a merge).

=== END OF ANSWER round6_q8 ===
