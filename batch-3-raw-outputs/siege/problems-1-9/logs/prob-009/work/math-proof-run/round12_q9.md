kind: attempt
Open question attempted: ledger entry 82, the run's open input (Rig) — the second open statement of the main chain (the goal follows from (Rig) together with the missing statement MS11♭, entry 124). This query is one of the wave's two queries outside the missing statement.

## Task
In the setting below (readings (R1), (R2)), prove (Rig) for every admissible family:

**(Rig).** There is a finite set 𝒦 of triples (G, M, K) such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G). Here a piece at time t is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w, M(E) ⊂ V(G) is its set of non-constant vertices, and K(E) is the closure of its image in ∏_{u∈M(E)} M̄_u (an irreducible closed curve not contained in the boundary).

What is known (spliced below): Lemma CD (round10_q9: (Rig) for a piece ⇔ countable-class membership of its joint image for uncountably many t); Theorem TV and (F2) (round8_q10: every piece of closure(V_0) has a Teichmüller vertex); Lemma Red, Lemma P0, Theorem B, Examples Z, Z′ (round8_q9: piece data alone cannot give (Rig)); Lemma Loc (round9_q9: local data cannot); L2 under (O_G) (round7_q9); Lemma G (round7_q7); Lemma R* (round5_q4: under (H_0) and orbifold transport (O) the Teichmüller vertex is pinned); Theorem L (round6_q7: conditions under which (O) holds); Lemma TR (round11_q6 §4: under (OT) the Teichmüller-vertex map of a product-type piece is t-independent); Prop. MP, Prop. DP, Lemma HQ (round11_q10).

Order of work:
1. Prove (Rig) in general, by global input from the 2-dimensional V_t (Prop. DP shows the ambient geometry of one factor cannot suffice; Examples Z, Z′ that piece data cannot). Ideas not yet tried: the boundary-trace constraint (c2) of round11_q10 §2 (the question (Q-DP)); transport of local intersection multiplicities of pieces with boundary divisors under H_t; the interplay of several pieces meeting at a common deeper point (the image curves of adjacent pieces share puncture values, so a finite set at one piece propagates).
2. If (Rig) in general is out of reach, prove it under the **orbifold reading (R2^orb)**: H restricted to each stratum is an orbifold isomorphism, i.e. it preserves isotropy groups compatibly with the local charts Def(z)/Aut(z), for every z ∈ closure(V_0). Decide whether (R2^orb) implies the orbifold-transport hypotheses (O), (O_G), (OT), (H_0) used by Lemma R*, Theorem L, L2 and Lemma TR — note that an automorphism of one component C_v fixing all its special points extends by the identity to an automorphism of the whole stable curve, so cone points of the vertex maps are visible in Aut(z) — and then assemble (Rig) (product-type and non-product strata; L2′ for non-product strata is only sketched in round7_q9 §2.6). Under (R2^orb) the run has also shown that the missing statement MS11♭ holds at every point (a single lift-curve; round11_q4 Lemmas 2.1–2.2), so a proof of (Rig) under (R2^orb) would complete a proof of the problem's claim under that reading. Make every use of (R2^orb) explicit.
3. In either case state precisely the weakest form of (Rig) your argument gives, and which inputs are cited from memory.

A proof for only some pieces, strata or V_0, or only for the Teichmüller vertex, does not settle entry 82 in general; report it, labelled partial, if that is all you find. Begin with a plan/status line and end with: proved / not proved / open.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## Prior results (verbatim from earlier answer files; re-check what you use)
Labels:
- PR-D = Lemma R/R0 (the lifted family 𝓦 of a piece: an irreducible 2-dimensional analytic set, proper over Δ).
- PR-E = Lemma R*: under (H_0) for a Teichmüller vertex and the orbifold transport (O), the vertex map is rigid up to biholomorphisms A_t.
- PR-F = Lemmas G, T′ (now superseded by Theorem TV).
- R7-k, R8-k = round-7 and round-8 files.
- Lemma PA (cited in R8-10): at generic points of a piece, norming differentials have positive-area limits on the max-speed vertices.

### R8-10. (F2) in general form, Corollary Φ̂, Theorem TV, Corollary AR (from round8_q10, verbatim, §§2, 5, 6)
## 2. (F2) proved, in a general form

**Definition FA (vertex v carries η_v at scale s_n).** Let (X_n,f_n) → P̃ in T̄ with P̃ in the γ_G-stratum (possible after a subsequence, by (GC3), whenever X_n → P ∈ Δ_G), Y_v := P̃_v, and let σ_v be a holonomy of Y_v (type-preserving). Let q_n ∈ Q(X_n) ∖ 0 and s_n ∈ C^*. We say *v carries η_v at scale s_n* if there are holonomies ρ_n of (X_n,f_n) with ρ_n|_{Γ_v} → σ_v pointwise and q̃_n/s_n → η̃_v locally uniformly on H, where η̃_v ≢ 0 is the σ_v-lift of a holomorphic quadratic differential η_v on the punctured surface Y_v. *Positive area* means: ‖q_n‖_1 = 1, s_n = 1, and η_v is integrable. (Lemma TR in §3 shows that the plumbing-chart convergence produced by PR-H Lemma PA gives exactly this, with η_v integrable.)

By Lemma B, replacing s_n by |s_n| replaces η_v by e^{iθ}η_v when arg s_n → θ (pass to a subsequence); so we may and do assume s_n > 0.

**Theorem F2\*.** Assume Def. FA with s_n > 0. Let g ∈ SL(2,R), let F_n: X_n → X'_n be the map which is affine of derivative g for q_n (X'_n = underlying surface of g·(X_n,q_n); F_n is the Teichmüller map of q_n, of dilatation K(g)), and f'_n := F_n∘f_n. Then:
(i) every subsequence of (X'_n, f'_n) has a further subsequence converging in T̄, and every such limit P̃' lies in the γ_G-stratum;
(ii) for every such limit, P̃'_v = g·(Y_v, η_v) as a point of T(Σ_v), the marking of g·(Y_v,η_v) being that of Y_v transported by the identity map Y_v → g·(Y_v,η_v) (the affine map of derivative g for η_v);
(iii) consequently, if X'_n → P' in M̄_g along a subsequence, then P' ∈ Δ_G and the v-entry of the labelled lift λ(P̃') ∈ Δ̂_G is [g·(Y_v,η_v)] ∈ M_{g_v,n_v}, the point of (the image of) the Teichmüller disc of (Y_v,η_v) labelled by g. For product-type G this is π_v(P') = [g·(Y_v,η_v)].
Neither integrability of η_v nor any control of the area of q_n in the collars or on other vertices is needed; the statement is for each fixed g, with no uniformity in g required.

*Proof.*
*Step 1 (lifts).* Let ρ_n be as in Def. FA. F_n lifts to a K(g)-qc homeomorphism F̃_n: H → H and there are holonomies ρ'_n of (X'_n, f'_n) with F̃_n∘ρ_n(γ) = ρ'_n(γ)∘F̃_n for all γ ∈ π_1(S) (lift F_n to universal covers; it conjugates deck groups compatibly with the markings f_n, F_n f_n). By Lemma B, μ_{F_n} = c_g q̄_n/|q_n|, and Beltrami coefficients lift, so a.e. on H
  μ_{F̃_n} = c_g \overline{q̃_n}/|q̃_n| = c_g \overline{(q̃_n/s_n)}/|q̃_n/s_n|  (s_n > 0).
*Step 2 (each vertex).* Fix w ∈ V(G). By (GC1) there are B^w_n with B^w_nρ_n|_{Γ_w}(B^w_n)^{-1} → σ_w (for w = v take B^v_n = 1 by Def. FA). σ_w(Γ_w) is non-elementary (P̃_w is a stable component: hyperbolic of finite area). The maps F̃_n(B^w_n)^{-1} conjugate B^w_nρ_n(B^w_n)^{-1} to ρ'_n on Γ_w. By Lemma Lim, after a subsequence, suitable Möbius conjugates of ρ'_n|_{Γ_w} converge to a discrete faithful type-preserving R'_w with H/R'_w(Γ_w) K(g)-qc equivalent (in the marking class) to P̃_w; in particular of finite area. Do this for the finitely many w successively.
*Step 3 (convergence).* ℓ_{X_n}(γ_e) → 0 for the γ_G-curves (GC1); by Maskit's comparison (PR-F (Ext)) Ext_{X_n}(γ_e) → 0, so Ext_{X'_n}(γ_e) ≤ K(g) Ext_{X_n}(γ_e) → 0 and ℓ_{X'_n}(γ_e) → 0. By (GC2), (X'_n,f'_n) converges (along the subsequence of Step 2) in T̄ to the point P̃' of the γ_G-stratum with P̃'_w = H/R'_w. If a subsequence of (X'_n,f'_n) converges to some P̃'', run Steps 2–3 along it: a further subsequence converges to a point of the γ_G-stratum, which equals P̃'' since T̄ is Hausdorff. This proves (i).
*Step 4 (identification of the v-component).* Take w = v, B^v_n = 1. In Lemma Lim the maps M_nF̃_n (M_n Möbius) converge uniformly to F̃, and μ_{M_nF̃_n} = μ_{F̃_n}. Since q̃_n/s_n → η̃_v locally uniformly and η̃_v ≢ 0 is holomorphic, its zero set Z is discrete, and at every point of H ∖ Z, \overline{(q̃_n/s_n)}/|q̃_n/s_n| → \overline{η̃_v}/|η̃_v|. Thus μ_{M_nF̃_n} → c_g \overline{η̃_v}/|η̃_v| a.e., with ‖μ_{M_nF̃_n}‖_∞ = |c_g| < 1. Lemma Conv on every disc D ⋐ H gives μ_{F̃} = c_g \overline{η̃_v}/|η̃_v| a.e. on H. F̃ descends to a qc homeomorphism Φ: Y_v = H/σ_v → H/R'_v = P̃'_v in the marking class, with μ_Φ = c_g η̄_v/|η_v| — by Lemma B, the Beltrami coefficient of the identity map ι_g: Y_v → g·(Y_v,η_v). By (QC3), Φ∘ι_g^{-1}: g·(Y_v,η_v) → P̃'_v is conformal; it is in the marking class; it maps punctures to punctures with the same labels (peripheral subgroups correspond, Φ being equivariant for the type-preserving R'_v). This is (ii). Since this identifies P̃'_v independently of the subsequence, and the marked limit of any further subsequence agrees, (iii) follows: P' is the image of some such P̃' in M̄_g, P' ∈ Δ_G, and λ(P̃')_v = [P̃'_v] = [g·(Y_v,η_v)]. ∎

**Where the feared failure modes went.** (a) *Area escaping into collars or to other vertices along g*: irrelevant — the Beltrami coefficient of the Teichmüller map is the *pointwise* expression c_g q̄_n/|q_n|; convergence of q_n on the v-part (up to positive scaling) determines it there, whatever happens elsewhere. (b) *Non-uniformity in g*: each g is treated separately; the joint (in g) statement needed for Lemma T′ is Corollary Φ̂ below, which uses only K(g g'^{-1}) and not F2\*. (c) *Markings at orbifold points*: everything takes place in T̄ and T(Σ_v); passing to M_{g_v,n_v} is done at the very end by a continuous map, so automorphisms of Y_v play no role. (d) *Extremality of the limit map*: not used; only its Beltrami coefficient. Hence F2\* also covers non-integrable η_v (lower-scale limits): the v-component of the limit is the affine deformation Y_v^{c_g η̄_v/|η_v|}.

**Corollary G′\* (the first sentence of PR-F Lemma G′, proved).** If d_T(X_n, X'_n) → 0 and X_n → P in M̄_g, then X'_n → P.
*Proof.* It suffices that every subsequence has a further subsequence converging to P. Choose markings with (X_n,f_n) → P̃ (GC3), Teichmüller maps F_n: X_n → X'_n of dilatation K_n → 1, and f'_n := F_n f_n. Steps 1–3 above (with K := sup K_n) apply verbatim with F_n in place of the affine map: a further subsequence of (X'_n, f'_n) converges to P̃' in the γ_G-stratum with P̃'_w ≅ H/R'_w, R'_w = F̃σ_wF̃^{-1}. Now ‖μ_{F̃_n}‖_∞ → 0, so Lemma Conv (with μ = 0) shows F̃ is conformal, i.e. Möbius; hence P̃'_w = P̃_w for all w (marked), P̃' = P̃ and X'_n → P. ∎
(By the compactness of M̄_g this gives the uniform continuity of (M_g, d_T) → M̄_g by the usual contradiction argument; so Lemma G′ is fully proved.)

**Corollary Φ̂ (the marked lift of the limiting disc).** Let X_n → P ∈ Δ_G, (X_n,f_n) → P̃ as in Def. FA, q_n ∈ Q(X_n) with ‖q_n‖_1 = 1 (no positive-area assumption yet). For g ∈ SL(2,R) let X^g_n, F^g_n be as in F2\*, f^g_n := F^g_n f_n. Then there is a subsequence and continuous maps φ̂_w: H = SO(2)\SL(2,R) → T(Σ_w), each 1-Lipschitz from the Poincaré metric d_H (curvature −4, d_H(SO(2)a, SO(2)b) = ½ log K(b a^{-1})) to the Teichmüller metric, such that for **every** g, (X^g_n, f^g_n) converges in T̄ to the γ_G-stratum point P̃^g with P̃^g_w = φ̂_w(g). Put φ̂ := ([φ̂_w])_w: H → Δ̂_G and φ := ξ_G∘φ̂. Then φ(g) = lim_n X^g_n in M̄_g; if (X_n,q_n) are generating pairs for V_0, φ(H) ⊂ closure(V_0) ∩ Δ_G and φ̂(H) ⊂ Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G). If moreover v carries positive area η_v, then [φ̂_v(g)] = [g·(Y_v,η_v)], i.e. π_v∘φ̂ = u, where u: H → M_{g_v,n_v} is the projection of the Teichmüller disc D of (Y_v,η_v) and φ̂_v = D (as maps to T(Σ_v)).

*Proof.* (K(h) := dilatation of the affine map of derivative h; it is invariant under h ↦ k_1hk_2, k_i ∈ SO(2), so d_H is well defined; it is the hyperbolic metric of curvature −4.) Let {g_k} be a countable dense subset of SL(2,R). By F2\*(i) and a diagonal argument, pass to a subsequence along which (X^{g_k}_n, f^{g_k}_n) → P̃^{g_k} for every k. Fix k, l and w. The map F^{g_l}_n∘(F^{g_k}_n)^{-1}: X^{g_k}_n → X^{g_l}_n is affine of derivative g_lg_k^{-1} for g_k·q_n, hence K_{kl} := K(g_lg_k^{-1})-qc, and it carries the marking f^{g_k}_n to f^{g_l}_n. Lift it, with holonomies of X^{g_k}_n normalized (GC1) so that their restrictions to Γ_w converge to a holonomy σ^k_w of P̃^{g_k}_w. Lemma Lim gives a K_{kl}-qc map in the marking class from P̃^{g_k}_w onto H/R', where R' = lim of Möbius conjugates of ρ^{g_l}_n|_{Γ_w}. By (GC1) other conjugates of ρ^{g_l}_n|_{Γ_w} converge to a holonomy σ^l_w of P̃^{g_l}_w, so Lemma Conj gives R' conjugate to σ^l_w (marked). Hence d_T(P̃^{g_k}_w, P̃^{g_l}_w) ≤ ½ log K_{kl} = d_H(g_k, g_l). So g_k ↦ P̃^{g_k}_w is 1-Lipschitz on a dense set and extends (T(Σ_w) is complete) to a 1-Lipschitz φ̂_w on H. For arbitrary g, by F2\*(i) every subsequence of (X^g_n, f^g_n) has a further subsequence converging to some P̃'' in the γ_G-stratum, and the same comparison with g_k gives d_T(P̃''_w, φ̂_w(g_k)) ≤ d_H(g, g_k) for all k, so P̃''_w = φ̂_w(g) for all w. A point of the γ_G-stratum is determined by its components, so P̃'' is independent of the subsequence and (X^g_n, f^g_n) converges. The rest: T̄ → M̄_g is continuous; X^g_n ∈ V_0 by total geodesy; and φ̂_v(g) = g·(Y_v,η_v) = D(g) by F2\*(ii). ∎

So Lemma G′'s map φ exists for every G (product or not), it lifts canonically and continuously to φ̂: H → Â ⊂ Δ̂_G, and (F2) holds in the form used in Lemma T′ Step 1: π_v∘φ̂ = u. (Steps 1–3 of the proof of F2\* use only (GC1), not Def. FA; this is what the first part of the proof of Corollary Φ̂ uses.)
## 5. The form needed by chain step 2 (task item 3)

**Theorem TV (every boundary piece has a Teichmüller vertex).** Let G be the dual graph of a boundary stratum (any G with at least one edge, product type or not), Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ Δ̂_G = ∏_w M_{g_w,n_w}, and E any 1-dimensional irreducible component of Â (no assumption that E meets closure(∂V_0)), with normalization ν: E^ν → E. Then there are a vertex j of G and an integrable quadratic differential η_j ≠ 0 on a curve Y_j ∈ π_j(E) such that, with D: H → T(Σ_j) the Teichmüller disc of (Y_j,η_j) and Γ′ ⊂ Aut(H) the (projectivized) Veech group:
1. C := closure of π_j(E) is a Teichmüller curve, C^ν = H/Γ′, and Γ′ is a lattice;
2. p := π_j∘ν: E^ν → C^ν is **proper** and E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p;
3. **orbifold structure**: give E^ν the orbifold structure of H/Λ_E, i.e. a point e over an orbifold point of C^ν of order m, at which p has local degree k, gets order m/k (k always divides m). Then p is an orbifold covering (orbifold-unramified), and the lift of π_j∘ν to orbifold universal covers is D, an isometric holomorphic embedding onto the Teichmüller disc, equivariant for Λ_E → Mod(Σ_j);
4. E is not compact, and every end of E^ν maps to a cusp of C (so along every end of E the j-component degenerates).
For product-type G (the case of the problem's Δ_Γ), Â = closure(V_0) ∩ Δ_G and ξ_G = id.

*Proof.* Pick P̂ ∈ E outside the finite set Sing Â ∪ (E ∩ other components) and outside the discrete exceptional set of PR-H Lemma PA, and let P = ξ_G(P̂). Lemma PA (PR-H, quoted; its proof is local in the plumbing chart at P, an orbifold chart of M̄_g whose fibres carry a labelling of components by V(G), hence it applies at P̂ ∈ Δ̂_G; and it uses only a ≠ 0 at P̂, true off a discrete set) gives generating pairs (X_n,q_n), ‖q_n‖ = 1, X_n → P along the branch of closure(V_0) through P̂, and a vertex j with q_j ≢ 0 (it maximizes the Teichmüller norm of the j-component of the tangent vector a of E at P̂). Lemma TR turns this into "j carries positive area" (Def. FA, η_j := q_j integrable, ∫|η_j| ≤ 1). Corollary Φ̂ gives φ̂: H → Â with φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂) and π_j∘φ̂ = u. Steps 2′, 3′, 4′, 5 of §4 then give 1–4; Step 2′ produces the component through φ̂(i) = P̂, which is E by the choice of P̂. ∎

**Caveats on item 3 (stated precisely).**
- The orbifold structure in (3) is the one *induced by Λ_E*; I have **not** shown that it coincides with the orbifold structure E inherits as a curve in the orbifold Δ̂_G (or M̄_g). They agree away from the finitely many points over orbifold points of C. If one prefers to avoid orbifolds, pass to a level-m cover: replace Γ′ by the torsion-free Γ′_m := π_1(C'^ν) and E^ν by a component of the fibre product E^ν ×_{C^ν} C'^ν normalized; then p becomes a genuine unramified finite covering of Riemann surfaces and the lift to universal covers is again D.
- Lemma PA is quoted, not re-proved, and in the non-product case its applicability on Δ̂_G rests on the labelled plumbing chart (Pl), which I have only described.
- The map φ̂ depends on the chosen subsequence; Theorem TV does not.

## 6. A by-product: the infinite-area remark of PR-F §3 (proved, given a non-zero scaled limit)

**Corollary AR.** In the problem's setting at t = 0 (Γ of product type, π_i(∂V_0) = {Y_0}, ∂V_0 := closure(V_0) ∩ Δ_Γ), let (X_n,q_n) be generating pairs with X_n → P ∈ ∂V_0, and suppose vertex i carries some η_i ≢ 0 at some scale s_n with arg s_n → θ (Def. FA; such a scale and limit is what the multi-scale compactness (F) of PR-F §0 provides — cited, not re-proved). Then every affine deformation of (Y_0, e^{iθ}η_i) is trivial in T(Σ_i): Y_0^{c\,\overline{η}/|η|} = Y_0 (marked) for all |c| < 1, where η := e^{iθ}η_i. Infinitesimally, ∫_{Y_0} φ η̄/|η| = 0 for every φ ∈ Q(Y_0).

*Proof.* By F2\*(iii) (which does not need integrability), for every g ∈ SL(2,R) and every limit P'_g of g·X_n, P'_g ∈ closure(V_0) ∩ Δ_Γ = ∂V_0 (X'_n ∈ V_0; F2\*(i) puts P'_g in Δ_Γ), so [Y_0^{c_g η̄/|η|}] = π_i(P'_g) = Y_0 in M_{g_i,n_i}. The map c ↦ [Y_0^{c η̄/|η|}] ∈ T(Σ_i) is continuous on the unit disc (the Teichmüller class depends continuously on the Beltrami coefficient in L^∞), and {c_g : g ∈ SL(2,R)} is the whole unit disc (c_g = β/α; e.g. g = diag(λ, 1/λ) composed with rotations). Its values lie in the discrete set Mod(Σ_i)·Y_0 ⊂ T(Σ_i) and it equals Y_0 at c = 0; the disc is connected, so it is constantly Y_0. Differentiating at c = 0 in every complex direction gives that the Beltrami differential c η̄/|η| is infinitesimally trivial for every c ∈ C, i.e. Re ∫ c φ η̄/|η| = 0 for all c, φ, i.e. ∫ φ η̄/|η| = 0 (Teichmüller's lemma: μ represents 0 iff ∫ μφ = 0 for all φ ∈ Q). ∎

(This is a necessary condition only; I do not derive a contradiction from it here.)

### round8_q9 (verbatim, §§1–7): Lemma Red, Lemma Deg, Cor. B, Lemma P0, Lemma P, Prop. F, Theorem B, Examples Z and Z′
## Status / plan (written first; final status in §7)
Plan:
1. Prove that the central fibre of the lifted family is reduced (Lemma Red). This uses only (R1)/(R2) and the product case.
2. Use Lemma Red to show that the degree of pr_v is constant in homology (Lemma Deg). In the *birational case*, i.e. when pr_v : E_0 → K_0 is generically injective, deduce that image-rigidity for the Teichmüller vertex v makes the whole normalized source family trivial (Cor. B).
3. Show that, under (Rig-v), punctures lying over v-cusps cannot move (Lemma P).
4. Prove rigidity of the other vertices in the birational case under a fixed-orbifold condition (Prop. F).
5. Give an explicit family of maps (Example Z). It satisfies every piece-level property that is available: constant Teichmüller vertex, trivial source family, fixed punctures, no type jump, (O) for v. Yet the joint image K_t ⊂ M̄_v × M̄_u varies with t. So (Rig-all) in its joint-image form cannot be proved from piece data alone. This is not a counterexample to the problem, since I have not checked that the family can be realized by an admissible V_t.

Statement now attempted: steps 1–4. The product case is assumed throughout: ξ_G is injective on ∏M_w.

## 1. Setting
Readings (R1), (R2) are as in the task. H_0 = id.

G is a product-type stable graph, and E_0 is a piece, i.e. a 1-dimensional irreducible component of closure(V_0) ∩ Δ_G, identified with its lift in ∏_w M_w. Put E_t := H_t(E_0).

W := 𝓦^{(a)} ⊂ ∏_w M̄_w × Δ is the irreducible 2-dimensional analytic set of Lemma R0. By R7-5 §1.2 (L1, product case), W_t = closure(E_t) as sets for every t, and W → Δ is proper.

For a vertex w, put K^w_t := pr_w(W_t) = closure of pr_w(E_t). It is a point or an irreducible curve (Remmert).

v is a Teichmüller vertex of E_0, i.e. (H_0) of PR-E holds. Let ι : K̃ → K_0 := K^v_0 be the normalization of the closed Teichmüller curve.

**(Rig-v)** denotes the image-level Lemma R for v: K^v_t = K_0 for all t. It is proved under (O) for v (PR-D, PR-E). By Cor. G2 of R7-7 it also holds unless 0 is a type-jump time with no Teichmüller generic member; that case is open.

## 2. Lemma Red (the central fibre is reduced)

**Lemma Red.** Regard t as a holomorphic function on W. Its divisor over 0 is the reduced cycle [closure(E_0)], with multiplicity 1. Consequently the fibre cycles [W_t] are all homologous to [closure(E_0)] in H_2(∏_w M̄_w; ℤ).

*Proof.*

**Setup.** W_0 = closure(E_0) as a set, and it is irreducible. So the divisor of t over 0 is m·[closure(E_0)] for some integer m ≥ 1. We must show m = 1.

- Choose x ∈ E_0 such that closure(E_0) is a smooth curve germ at x. Choose x also generic in the following sense: it is not a multi-branch point of the 1-dimensional part of closure(V_0) ∩ Δ_G, and not a puncture.
- Embed a neighbourhood of x in the coarse analytic space ∏M̄_w into some ℂ^N. Some linear coordinate s restricts to a local coordinate on the smooth germ (closure(E_0), x). Put s(x) = 0.
- Near x, Ψ := (s, t) : W → ℂ² has Ψ^{-1}(0,0) = {x}. So Ψ is finite at x.

**Step 1 (m = local degree μ of Ψ).** Let μ be the local degree of Ψ at x: the number of preimages near x of a generic point near (0,0). By the projection formula for the finite map Ψ, Ψ_*(div t near x) = Ψ_*(m·[closure E_0]) = m·deg(s|_{closure E_0})·[t = 0] = m·[t = 0]. Also Ψ_*Ψ^*[t = 0] = μ·[t = 0]. Hence m = μ.

**Step 2 (counting via H).**
- Fix r > 0 small. Let B := {y ∈ closure(E_0) : |s(y)| ≤ r} be a closed disc around x.
- Since H is a homeomorphism of closure(V_0) × Δ onto closure(𝒱), H_t → id and H_t^{-1} → id uniformly near x as t → 0. In the product case lifting through ξ_G is a homeomorphism near x, so we may work upstairs.
- Hence there are a neighbourhood N of x and ε > 0 with the following properties for every |t| < ε:
  - (a) H_t(B) ⊂ N.
  - (b) |s(H_t(y))| > r/2 for all y ∈ ∂B.
  - (c) every y ∈ W_t ∩ N with |s(y)| < r/2 lies in H_t(B).
  - For (c): if y ∈ W_t is close to x, then H_t^{-1}(y) is close to x, so it lies in B.
- Fix c with |c| < r/2, and t with 0 < |t| < ε. By (a) and (c), the solutions of s = c on W_t ∩ N are exactly the solutions on the topological disc H_t(B).
- H_t(B) is a disc, so it contains no multi-branch point of the curve W_t. Hence it is a topological 2-manifold that is oriented by the complex structure at its smooth points.
- **Holomorphic count.** For generic (c, t), s|_{H_t(B)} has μ simple solutions, each of local degree +1.
- **Topological count.** The map s ∘ H_t : B → ℂ has topological degree over c equal to ±μ. The sign is that of the homeomorphism H_t : B → H_t(B) with respect to the complex orientations.
- **Homotopy.** τ ↦ s ∘ H_{τt}, τ ∈ [0,1], is a homotopy from s|_B to s ∘ H_t. By (b) it never takes the value c on ∂B. So the degree over c is that of s|_B, which is 1, because s|_B is a homeomorphism onto the disc |s| ≤ r.
- Hence ±μ = 1, so μ = 1 and m = 1.

**Homology.** The fibre cycles [W_t] = div(t − t_0) of the proper map t : W → Δ are homologous in W, since Δ is connected. This is the standard fact that fibre cycles of a proper flat family over a connected base are homologous. So [W_t] is homologous to [W_0] = [closure E_0] in ∏M̄_w. ∎

*Remark.* Only (R2), continuity and the product case are used. The proof is a topological degree argument. It is the "degree" counterpart of the unibranchness of the central fibre (Lemma N in the chain).

## 3. Lemma Deg and the birational transfer

**Lemma Deg.** Let w be a vertex with K^w_0 a curve. Let d_t be the degree of pr_w : closure(E_t) → K^w_t when K^w_t is a curve, and put d_t := 0 when it is a point. Then d_t·[K^w_t] = d_0·[K^w_0] in H_2(M̄_w; ℚ). In particular, if K^w_t = K^w_0, then d_t = d_0.

*Proof.*
- Take pr_{w*} of the homology relation in Lemma Red: pr_{w*}[closure E_t] = d_t·[K^w_t] as cycles.
- M̄_w is projective (Knudsen–Mumford; from memory). So an ample class pairs positively with the curve K^w_0, and [K^w_0] ≠ 0 in H_2(M̄_w; ℚ).
- If K^w_t = K^w_0, we may cancel [K^w_0] and get d_t = d_0. ∎

(Note: by L1, K^w_t is a point for one t iff it is a point for all t. So the case d_t = 0 does not actually occur here.)

**Corollary B (birational case).** Assume (Rig-v), and that pr_v : E_0 → K_0 is generically injective (d_0 = 1). Let n : 𝓦^ν → W be the normalization. Then:
- (a) (lift of pr_v ∘ n, t) : 𝓦^ν → K̃ × Δ is a biholomorphism over Δ;
- (b) under this identification the v-coordinate is ι for every t: pr_v ∘ n(x, t) = ι(x);
- (c) there are holomorphic maps φ^u : K̃ × Δ → M̄_u, one for each vertex u, with ν_t = (φ^u_t)_u, where φ^v_t = ι.

In particular, (O) holds for v trivially, with A_t = id. For this piece, (Rig-all) is equivalent to φ^u_t = φ^u_0 for all non-constant u. The joint image is the image of K̃ under x ↦ (ι(x), φ^u_t(x)), and ι is generically injective, so equality of joint images forces equality of maps.

*Proof.*
- **Degree.** By Lemma Deg and (Rig-v), d_t = 1 for all t.
- **The map exists.** pr_v ∘ n maps 𝓦^ν into K_0, by (Rig-v). 𝓦^ν is normal and no component of it maps into Sing(K_0) × Δ. By the universal property of normalization, (pr_v ∘ n, t) factors through the normalization K̃ × Δ of K_0 × Δ.
- **The map is finite.** It is proper, since 𝓦^ν → Δ is proper. Its fibres are finite, since each W_t maps finitely onto K_0.
- **The map is bimeromorphic.** For generic t, its degree is d_t = 1.
- **Conclusion.** A finite bimeromorphic holomorphic map onto a normal space is biholomorphic. This is the analytic Zariski main theorem; cited from memory. This gives (a). (b) and (c) follow by composing with pr_u ∘ n. ∎

## 4. Lemma P (whether a puncture degenerates at v is constant in t)

**Lemma P0 (general product case).** Let Π be an irreducible component of the puncture locus 𝓟 := n^{-1}(∂(∏M̄_w) × Δ) ⊂ 𝓦^ν, and let w be a vertex. Then either pr_w ∘ n(Π) ⊂ ∂M̄_w, or pr_w ∘ n(Π) ∩ ∂M̄_w = ∅.

*Proof.*

**Π is horizontal and surjects onto Δ.**
- 𝓟 contains no whole fibre, since E_t ⊂ ∏M_w. So 𝓟 is a curve that is proper and finite over Δ.
- Hence each component Π surjects onto Δ, by Remmert's proper mapping theorem and irreducibility.

**The transported point is the same along Π.**
- For y ∈ ∏M̄_w, the stable curve ξ̄_G(y) has |E(G)| + Σ_w δ(y_w) nodes, where δ(y_w) is the number of nodes of the curve y_w.
- Let F_t := closure(E_t) \ E_t ⊂ M̄_g be the finite set of puncture points. By (R2), F_t = H_t(F_0), and H_t preserves strata.
- So the continuous map t ↦ ξ̄_G(n(π(t))), along a local continuous branch π(t) of Π, takes values in H_t(F_0).
- For fixed t the points H_t(f), f ∈ F_0, are distinct, and each depends continuously on t. A continuous selection from finitely many distinct continuous functions is locally one of them. So ξ̄_G(n(π(t))) = H_t(f) for one fixed f ∈ F_0.
- Hence the total number of nodes N(t) := |E(G)| + Σ_w δ(pr_w n π(t)) is independent of t along Π.

**Semicontinuity forces the dichotomy.**
- The sets {δ ≥ k} ⊂ M̄_w are closed. So if π(t) → π(t_1), then δ(pr_w n π(t_1)) ≥ δ(pr_w n π(t)) for each vertex w and all t near t_1.
- N(t) is constant along Π, so all these inequalities are equalities.
- In particular, if pr_w n π(t_1) ∈ ∂M̄_w, i.e. δ ≥ 1, then pr_w n π(t) ∈ ∂M̄_w for all t near t_1. So the set where pr_w n ∈ ∂M̄_w is open in Π.
- That set is also closed and analytic, and Π is irreducible, hence connected. So it is empty or all of Π. ∎

**Lemma P (birational case).** Under the hypotheses of Cor. B, put Cusp := ι^{-1}(∂M̄_v), a finite subset of K̃. Every component of 𝓟 ⊂ K̃ × Δ is either:
- {c} × Δ for some c ∈ Cusp, or
- disjoint from Cusp × Δ.

In particular:
- the punctures of E_t at which v degenerates are the fixed points c ∈ Cusp ∩ 𝓟_0, and their v-values ι(c) are independent of t;
- if every puncture of E_0 is a v-degenerate puncture, then 𝓟 = 𝓟_0 × Δ. That is, the punctures of E_t, as points of the fixed curve K̃, do not move.

*Proof.* By Cor. B, pr_v ∘ n(x, t) = ι(x). By Lemma P0 a component Π either lies in Cusp × Δ, or misses it. In the first case Π is a component of {c} × Δ, which is irreducible, so Π = {c} × Δ. ∎

*Remark.* For the problem itself, Lemma P0 says that "which vertices degenerate at a given puncture" is a deformation invariant. This uses only (R2) and node counting.

## 5. Prop. F (rigidity of the other vertices in the birational case, fixed orbifold data)

Fix a non-constant vertex u. By L1′ applied with arbitrary base time (its proof is symmetric in t), φ^u_t is non-constant for every t. Let M′ := M_u[N] → M_u (N ≥ 3) be the level cover. M′ is a complex manifold and a fine moduli space. Let 𝓢 be the normalization of (K̃ × Δ \ 𝓟) ×_{M_u} M′. It is a finite map onto K̃ × Δ \ 𝓟, and it is branched along an analytic set R̂ of pure dimension 1, by Zariski–Nagata purity: 𝓢 is normal and the base is smooth.

**(Σ-fixed for u).** There is a finite set Σ_u ⊂ K̃ with R̂ ∪ 𝓟 ⊂ Σ_u × Δ.

**Prop. F.** Assume (Rig-v), d_0 = 1 (Cor. B), and (Σ-fixed) for u. Then φ^u_t = φ^u_0 for all t.

*Proof.*

**The cover is a product.**
- Over B° := (K̃ \ Σ_u) × Δ, the map 𝓢 → B° is finite and unbranched onto a manifold, with normal source. So it is a finite covering map.
- B° deformation retracts onto (K̃ \ Σ_u) × {0}. Coverings are classified by π_1 and are homotopy invariant. So each connected component of 𝓢|_{B°} is isomorphic over B° to S° × Δ, where S° → K̃ \ Σ_u is a connected finite covering.
- In particular S° is a Riemann surface of finite type, and is fixed.

**The lifted maps.**
- The fibre product gives a holomorphic lift φ̂ : S° × Δ → M′ of φ^u.
- φ̂_t is non-constant for each t, because φ^u_t is.
- t ↦ φ̂_t is a continuous family of maps from the fixed surface S°, so all φ̂_t are homotopic.

**Finiteness.** *Cited from memory: Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces", MSRI Publ. 11, 1988.* For a finite-type Riemann surface S° and a torsion-free finite-index Γ ⊂ Mod_{h,m} with 2h − 2 + m > 0, a homotopy class of maps S° → T_{h,m}/Γ contains only finitely many non-constant holomorphic maps. So φ̂_t ∈ {ψ_1, …, ψ_r} for every t.

**Constancy.**
- Each set {t : φ̂_t = ψ_j} is closed, by pointwise continuity in t.
- These finitely many disjoint closed sets cover the connected Δ, so only one is nonempty, and φ̂_t = φ̂_0.
- Projecting to M_u gives φ^u_t = φ^u_0 on K̃ \ Σ_u. By continuity this holds on all of K̃. ∎

**Theorem B (what is now proved for (Rig-all)).** Let E_0 be a product-type piece with Teichmüller vertex v. Assume:
- (Rig-v) for v; this holds e.g. under (O) for v, or under Cor. G2's condition;
- pr_v|_{E_0} is generically injective;
- (Σ-fixed) holds for every non-constant vertex u.

Then ν_t = ν_0 ∘ (identification of Cor. B) for all t. Hence the joint image K_t ⊂ ∏_{u∈M} M̄_u is independent of t, and so are all puncture values. So (Rig-all) holds for E_0.

**Sufficient conditions for (Σ-fixed) for u.** Suppose:
- (1) every puncture of E_0 is v-degenerate; then 𝓟 = 𝓟_0 × Δ by Lemma P;
- (2) for every t, φ^u_t(K̃ \ 𝓟_t) avoids the locus of M_u where the automorphism group is larger than the generic one.

Then R̂ = ∅ and (Σ-fixed) holds with Σ_u := 𝓟_0.

Condition (1) is what one expects for boundary pieces of a totally geodesic V_0. Heuristically, all cylinders pinch only at the cusps of the SL_2ℝ-orbit. This is a sketch, not proved here.

## 6. Example Z: the joint-image form of (Rig-all) does not follow from piece data

**Data** (the Teichmüller curve is cited from memory, as in Prop. X of R7-7).
- **Vertex v.** M_v = M_{2,1}. ι : ℂ → M_{2,1} is the closed Teichmüller curve of the double regular pentagon (Veech group Δ(2,5,∞)), in the coarse coordinate z on C_V ≅ ℂ:
  - an orbifold point of order 2 at z = 0;
  - an orbifold point of order 5 at z = 1;
  - a cusp at z = ∞, so ι(∞) ∈ ∂M̄_{2,1}.

  ι is generically injective.
- **Vertex u.** M_u = M_{1,1}. Its coarse space is the j-line ℂ, with orbifold points j = 0 (order 3) and j = 1728 (order 2), and ∂M̄_{1,1} = {∞}.
- **The stratum.** G is the genus-3 graph with a genus-2 vertex v and a genus-1 vertex u joined by one edge. It has no automorphisms, and Δ_G ≅ M_{2,1} × M_{1,1} is of product type.
- **The family.** For |t| < ε put J_t(z) := z³ + z + t z² and

  E_t := {(ι(z), J_t(z)) : z ∈ ℂ} ⊂ M_{2,1} × M_{1,1},

  normalized by K̃ = ℙ¹ through z ↦ (ι(z), J_t(z)).

**Properties (proved).**
- (a) **Trivial source, one fixed puncture.** The source family is the trivial family ℙ¹ × Δ. The map depends holomorphically on (z, t). Its only puncture is z = ∞, with constant value (ι(∞), ∞). So the family is smoothly trivial and its puncture is v-degenerate. Condition (1) of §5 holds, and the conclusion of Lemma P holds.
- (b) **The v-coordinate is ι for all t.** So (H_0) holds for v, (O) holds for v with A_t = id, (Rig-v) holds, and d_0 = 1.
- (c) **No type jump of the joint minimal orbifold for small t.** J_t(z) = z(z² + tz + 1).
  - Its zeros are z = 0 (fixed) and the two roots of z² + tz + 1 (near ±i, moving). For small t they are simple, since J_0′(0) = 1 and J_0′(±i) = −2.
  - The three roots of J_t = 1728 are simple and move. The discriminant of z³ + z − c is −4 − 27c² ≠ 0 at c = 1728.
  - None of these points meets z = 1 or another of them for small t, because J_0(1) = 2 ∉ {0, 1728}.
  - So the joint orbifold is ℙ¹ with a cusp at ∞ and cone points of orders 6 (at z = 0, lcm(2,3)), 3, 3, 2, 2, 2 and 5. Its type is constant, but the cone points of orders 3 and 2 move. Hence (Σ-fixed) fails for u.
  - (O_G) holds in the sense of a type-preserving transport with constant monodromy (by continuity). But (H_0) fails for the *joint* orbifold: the lift of ι from the joint orbifold's universal cover is a branched map, not an isometry. So L2 (R7-8) does not apply. This is consistent with L2.
- (d) **The joint image varies.** Suppose closure(E_t) = closure(E_{t′}).
  - For generic z, ι^{-1}(ι(z)) = {z}. So (ι(z), J_t(z)) ∈ E_{t′} forces J_t(z) = J_{t′}(z).
  - Then t z² = t′ z² for generic z, so t = t′.
  - Hence the joint image curves K_t ⊂ M̄_v × M̄_u are pairwise distinct. The conclusion of (Rig-all) fails for this family of pieces.
- (e) **The single-vertex images and the puncture values are constant.** K^u_t = M̄_{1,1}, because J_t is onto. The only puncture value is (ι(∞), ∞).

**What Example Z shows, and what it does not.**
- It is a family of *maps* (pieces) only. I have NOT checked:
  - that E_0 is a boundary piece of a totally geodesic surface V_0 (its u-coordinate z³ + z is arbitrary);
  - that the deformation extends to a family V_t satisfying (i) and (ii).

  So it is not a counterexample to (Rig-all) or to the problem.
- It does show that **no argument using only the piece family** can prove the joint-image form of (Rig-all). That covers source triviality, the Teichmüller anchor, (O) for v, puncture behaviour and orbifold type constancy. Theorem B's hypothesis (Σ-fixed) cannot simply be dropped.
- The mechanism is general. Let E_0 be any product-type piece with a non-constant vertex u of type (1,1) and pr_v birational. Then J_t := φ^u_0 + t·g, with g a rational function on K̃ whose poles lie among those of φ^u_0 with smaller order, deforms the piece with fixed punctures and varying joint image. Any proof must therefore use the global existence of V_t (conditions (i), (ii) on all strata, including the 2-dimensional open part), or the totally geodesic structure at t = 0 combined with such global input.
- One might hope to retreat to the **weak form (Rig-w)**: the puncture values of the non-constant vertices lie in a t-independent finite set. The task states that this consequence is what the reduction to MS8 uses. Example Z satisfies (Rig-w), but Example Z′ shows that (Rig-w) also fails at the piece level.

**Example Z′ ((Rig-w) also fails for families of pieces).**
- Let ι : K̃ → M̄_{2,1} be any closed Teichmüller curve whose normalization K̃ has at least two cusps c_1 ≠ c_2, i.e. points of ι^{-1}(∂M̄_{2,1}). Arithmetic Teichmüller curves of L-shaped square-tiled surfaces in H(2) are standard examples; cited from memory.
- By Riemann–Roch choose a non-constant meromorphic function J_0 on K̃ whose only pole is at c_1. Put J_t := J_0 + t, and let E_t be the image of z ↦ (ι(z), J_t(z)) in M_{2,1} × M_{1,1} (same stratum G as in Example Z).
- **Fixed data.** The source family is trivial, and the v-coordinate is constant in t. The punctures are the cusps of K̃, and are fixed. Every puncture is v-degenerate, so Lemma P's hypothesis holds. (Rig-v) holds and d_0 = 1.
- **Moving puncture value.** At the puncture c_2 the vertex u is *not* degenerate, and its value J_0(c_2) + t ∈ M_{1,1} moves with t.
- **Translation to M̄_g.** The deeper boundary point H_t(P_0) ∈ Δ_{G′} has a genus-1 component whose j-invariant varies with t. This is exactly the phenomenon the problem asks to exclude, now for a non-constant vertex. Again, realizability by an admissible V_t is unchecked.

**Consequence for the chain.** Neither (Rig-all) nor (Rig-w) can be derived from properties of the individual piece families: (R2) on the piece, the Teichmüller anchor, (O) for v, puncture rigidity, Lemma P0. A proof must use the global family V_t, e.g.:
- the 2-dimensional open part and its compatibility (ii) with all strata;
- or the totally geodesic structure at t = 0 in a way that propagates to t ≠ 0. That is, at t = 0, φ^u_0 must be shown to be constrained by V_0, and the constraint must be shown to persist.

The same is true of the problem itself: with u constant, Y_t := j_0 + t is a piece-level "counterexample" in the same sense. So (Rig) is not an easier intermediate statement than the problem at the level of piece data.

## 7. Final status

**Proved** (product-type strata, readings (R1)/(R2); literature cited from memory as indicated):
- **Lemma Red.** The central fibre of the lifted 2-dimensional family W is reduced: div(t)|_0 = [closure E_0]. So all fibre cycles are homologous to [closure E_0]. The proof is a topological degree argument from (R2).
- **Lemma Deg.** d_t·[K^w_t] = d_0·[K^w_0]. Under image constancy the degree d_t of pr_w is constant.
- **Cor. B.** If (Rig-v) holds and pr_v|_{E_0} is birational, then the normalized family is K̃ × Δ, the v-map is ι for all t, and (O) for v holds with A_t = id. This uses the analytic Zariski main theorem, cited.
- **Lemma P0.** For every component of the puncture locus and every vertex w, w is degenerate along the whole component or nowhere on it. The proof is node counting plus stratum preservation by H.
- **Lemma P.** In the birational case, v-degenerate punctures are fixed points of K̃ with fixed v-values. If all punctures at t = 0 are v-degenerate, no puncture moves.
- **Prop. F / Theorem B.** In the birational case, (Rig-v) together with (Σ-fixed) for every non-constant u gives ν_t ≡ ν_0, hence (Rig-all) for the piece. This uses Imayoshi–Shiga finiteness, cited. Sufficient conditions are: all punctures v-degenerate, and the u-maps avoiding the extra-automorphism locus of M_u.
- **Examples Z and Z′.** Explicit holomorphic families of pieces with:
  - a constant Teichmüller vertex, trivial source family and fixed punctures;
  - in Z, no orbifold type jump and (O) for v;
  - nevertheless, a varying joint image (Z) and a varying interior puncture value (Z′).

  So (Rig-all), and even its weak form (Rig-w), cannot be proved from piece-level data. These are not counterexamples to (Rig-all) or to the problem, because realizability by an admissible V_t is unchecked.

**Not proved.** (Rig-all) in general. In particular:
- the non-birational case (d_0 > 1, as in Prop. X);
- (Rig-v) at a type-jump time (J1 ∧ J2 of R7-7);
- non-constant vertices hitting orbifold points of M_u at moving points;
- punctures that are not v-degenerate.

**Sketched only.** That for a totally geodesic V_0 all punctures of a piece are v-degenerate (§5, condition (1)).

**Open questions.**
- (Q1) Can Examples Z/Z′, or the problem's own analogue Y_t = j_0 + t, be realized as boundary pieces of an admissible family V_t deforming a totally geodesic V_0? If yes, (Rig-all) and (Rig-w) are false, and the problem's claim would be in doubt. If no, the obstruction is global (conditions (i), (ii) and the 2-dimensional open part), and identifying it is the real content of the problem.
- (Q2) Is a 2-dimensional totally geodesic V_0 ⊂ M_g rigid as a subvariety, i.e. has no non-trivial deformations V_t satisfying (i), (ii)? This would make the problem vacuous-true.
- (Q3) The non-birational case of Theorem B, i.e. FAC of R7-7 given (Rig-v).
- (Q4) (Rig-v) at type-jump times (Q1′ of R7-7).

### round7_q9 §2 (verbatim): L2 under (O_G), and the L2′ sketch
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


### round7_q7 §§2–4 (verbatim): Lemma G ((O) holds generically in t), consequences, the inequality dead end and the image-cycle route
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


### round8_q7 §§2–4 (verbatim): Lemma S (pieces are products under (Rig)), Lemma J, normal-bundle / plumbing-ratio constraint (Proposition N)
## Step 2. First move: (Rig) forces pieces to be products K° × {c(t)}

Conventions. Work at a fixed time t. By Chow's theorem, closure(V_t) is algebraic (closed analytic in the projective M̄_g, via (R1)), so all the sets below are algebraic.

**Lemma S (structure of pieces under (Rig)).** Let E be a piece at time t in a stratum G, with M = M(E). Write c_u (u ∉ M) for the constant values of f_u. Then E = (K(E) ∩ ∏_{u∈M} M_u) × {(c_u)_{u∉M}} exactly. Moreover Ē is the normalisation of K(E), and the maps f_u (u ∈ M) are the coordinate projections composed with K̃ → K. Hence, by (Rig), the curve Ē and the maps f_u (u ∈ M(E)) come from a t-independent finite list. Only the constant values c_u move.

*Proof.* E is an irreducible component of ξ_G^{-1}(closure(V_t) ∩ Δ_G), which is closed in ∏_w M_w. So E is a closed irreducible 1-dimensional algebraic subset. Because f_u is constant for u ∉ M, we have E = E^M × {c}, where E^M is closed irreducible 1-dimensional in ∏_{u∈M} M_u. The closure K = K(E) is an irreducible curve. Since K is not contained in the boundary, K° := K ∩ ∏_M M_u is a nonempty Zariski-open subset of K, hence irreducible of dimension 1. Then E^M ⊂ K° is a closed 1-dimensional subset of the irreducible curve K°, so E^M = K°. The closure of E in ∏ M̄_w is K × {c}, so its normalisation is K̃. ∎

**Corollary S′ (puncture values and fibres are rigid).** Fix a triple (G, M, K) ∈ 𝒦. Then:
- (a) The set Φ_K of all points of K ∖ K° is finite. Hence so is the set of their coordinates and of the components of these stable curves. Thus the puncture values f_u(p), u ∈ M, of any piece of type K, and all their components, lie in a finite set Φ that is independent of t.
- (b) For u ∈ M and any point z ∈ M̄_u, the set {k ∈ K : pr_u(k) = z} is finite, because pr_u|_K is non-constant on an irreducible curve.

**Lemma S″ (pieces are carried to pieces; K(E_t) is t-independent).** Each stratum restriction of H_t is a homeomorphism of 1-dimensional analytic sets, so it maps irreducible components to irreducible components. The reason is that the irreducible components of a curve X are the closures of the connected components of the set of points where X is a topological 2-manifold: unibranch points are exactly the points with disc neighbourhoods, and multi-branch points form a finite set. Write E_t for the piece corresponding to E_0, with a lift chosen locally continuously in t.

Then t ↦ K(E_t) is locally constant, hence constant on Δ, up to Aut(G). Suppose t_n → t* and K(E_{t_n}) = K′ for all n. H is continuous, so each point of E_{t*} is a limit of points of E_{t_n}. Since K′ is closed, K(E_{t*})° ⊂ K′, and therefore K(E_{t*}) = K′, both being irreducible curves. As 𝒦 is finite, this gives local constancy.

*Caveat (this is where "twins" live).* The constant values c_u(t) are holomorphic as points of Δ_G / Stab. A *lift* to labelled vertices can be branched at isolated values of t, for example {c_u, c_{u′}} = {±√t}, when an automorphism of G exchanges two constant vertices whose values coincide at that t. For the vertex i of the product-type stratum Γ there is no ambiguity, and Y_t is holomorphic (R-Hol).

## Step 3. Junction lemma: where Y_t can and cannot escape pinning

Fix t. Let Q ∈ B_t lie in a stratum G′. Since ∂M̄_g is (orbifold-locally) a Cartier divisor and closure(V_t) is an irreducible surface not contained in it, Krull's principal ideal theorem shows that B_t is pure of dimension 1. So every point of B_t lies on the closure of some 1-dimensional piece.

**Lemma J.** Let E be a piece at time t with Q = ν(p) for a puncture p of E (Q ∈ Δ_{G′}, and G′ contracts to G). Suppose a vertex x of G′ is a constant vertex of E with value Z_t, and let E′ be another piece with Q in its closure. Then one of the following holds.

- (J1) *Merge.* Q is a puncture of E′, and x lies inside a vertex u′ of E′ that is degenerate at that puncture. Then u′ ∈ M(E′), and Z_t is a component of the puncture value f_{u′}(p′). Hence Z_t ∈ Φ.
- (J2) *Puncture move.* Q is a puncture of E′, x is a vertex of E′, and x ∈ M(E′). Then Z_t = f_x(p′) ∈ Φ.
- (J3) *Constant.* x is a constant vertex of E′, and Z_t is unconstrained by this junction.
- (J4) *Pinned crossing.* Q is an interior point q of E′, x ∈ M(E′), and some vertex w ∈ M(E′) of G′ lies in a group G′_u with u ∈ M(E). Then q lies in a finite t-independent subset of K(E′), so Z_t = f_x(q) is in a finite t-independent set.
- (J5) *Sliding crossing.* Q is an interior point q(t) of E′, x ∈ M(E′), and every vertex of M(E′) belongs to a group G′_u with u a **constant** vertex of E. Equivalently, every vertex of G′ that is a component of a fixed puncture value of E is constant along E′.

*Proof.*
- **(J1).** If u′ were constant on E′, then f_{u′}(p′) = c_{u′} ∈ M_{u′} would be non-degenerate, contradicting that x lies in a degenerate vertex. So u′ ∈ M(E′), and Corollary S′(a) applies.
- **(J2).** This is Corollary S′(a) again.
- **(J4).** The value f_w(q) is a component of some fixed puncture value f_u(p), so it lies in Φ. Corollary S′(b) then puts q in a finite set, and Z_t = f_x(q) follows.
- **Exhaustiveness.** If Q is a puncture of E′ we are in (J1), (J2) or (J3). If Q is an interior point of E′, then G′ is E′'s stratum, so x is a vertex of E′: either constant, which is (J3), or moving, which is (J4) or (J5).

The finite sets in (J1), (J2) and (J4) are unions over the finite list 𝒦, so they do not depend on t. ∎

**Consequence (pinning criterion).** Let 𝒯 be the set of times t at which there is an *intact chain* from a generic point of ∂V_t to a junction of type J1, J2 or J4 for the copy. An intact chain is a finite chain of closures of pieces along which a chosen component stays a constant vertex, continuing continuously across junctions, so its value is locally constant: on each piece it is a constant vertex, and at a junction an intact component varies continuously. If 𝒯 accumulates in Δ, then Y_t lies in a finite fixed set for t ∈ 𝒯, and R-Hol gives Y ≡ Y_0.

This refines R-time-t. It shows that **the only escape is that, for all t in a nonempty open set U ⊂ Δ, every intact chain from ∂V_t ends only in (J3) or (J5) junctions.** By Lemma S, the escape has a specific shape. All moving vertex data are fixed. At a (J5) junction, E slides along E′: the moving parameter is the attachment point q(t) on the fixed curve K̃(E′). The constant values of E then equal f_w(q(t)) for w ∈ M(E′), and Y_t = f_x(q(t)) runs along the fixed curve pr_x K(E′).

*Remark on t = 0 information.* Suppose Proposition K's endpoint at t = 0 is a MERGE (J1 at t = 0) at a point Q_0. Then Lemma S applied at Q_t := H_t(Q_0) shows that Q_t has, for **all** t, a component with constant value Y_0: it is a component of the fixed puncture value f_{u′}(p′). The MS8 problem is thus exactly the problem of connecting the vertex i at P_t ∈ ∂V_t to this Y_0-component by an intact chain at time t. The obstruction is the branching of lifts at t = 0 (twins), as in R-Known-partial. Lemma S shows the twin ambiguity is the *only* non-rigid datum. Everything else on the network is rigid.

*Why twins are genuinely topological (and not removable by choosing t generic).* Take a stable curve Q_0 and its Kuranishi chart Def(Q_0), on which Aut(Q_0) acts. In the chart, components are labelled consistently until they merge. A path lifts through a finite-group quotient, but a 2-parameter family (chain × [0, t]) need not. Example: z ↦ z² from C to C/±1 admits no continuous lift of the identity map of a disc around 0. So the copy tracked along the t = 0 chain can be continued to time t only if the square chain × [0, t] does not wind around the twin locus. Lemma S does not touch this point.

## Step 4. Normal-bundle / plumbing-ratio constraint on sliding crossings (sketched)

Let E′ be a piece at time t (stratum G′) and let C := K̃(E′) be its normalisation. By Lemma S, C is fixed. Let S̃ → closure(V_t) be the normalisation, a normal surface. Abusing notation, write E′ also for the curve in S̃ over E′.

For an edge e of G′, let s_e be a local defining equation of the boundary branch D_e (in an orbifold chart). Its pull-back to S̃ vanishes along E′ to an order m_e ≥ 1.

**(a) The m_e are independent of t.** A small loop in V_t around E′ has monodromy in Mod_g of the form ∏_e T_e^{m_e}, a product of Dehn twists about the pinched curves. H_s (s ∈ [0, t]) gives a homotopy of such loops inside M_g, so the monodromy is a homotopy invariant, and the m_e are constant. The same argument shows that the vanishing orders of the s_e along the other boundary branches through a junction point are constant in t.

**(b) Ratio function.** For two edges e, f put F_{e,f} := s_e^{m_f} / s_f^{m_e}. This is a meromorphic function on a neighbourhood of E′ in S̃ whose divisor contains E′ with multiplicity 0. Let ρ_{e,f} := F_{e,f}|_{E′}. Changing the coordinates s_e multiplies ρ_{e,f} by a non-vanishing function, so ρ_{e,f} is canonically a meromorphic section of L_{e,f} := N_{D_e}^{⊗m_f} ⊗ N_{D_f}^{⊗(−m_e)} restricted to C.
- At an interior point q of E′ through which no other branch of B_t passes: S̃ is normal there, and div F_{e,f} has no component through q. So F_{e,f} is a unit near q (normal surface: a meromorphic function with zero divisor is a unit), and ord_q ρ_{e,f} = 0.
- Therefore div ρ_{e,f} is supported on two kinds of points: the punctures of C, which are fixed, and the junction points q_j(t) of E′ with other branches of B_t. Its coefficients there are integers fixed by the topology, as in (a).

**(c) The line bundle is fixed.** Cited from memory (standard deformation theory of nodal curves, e.g. Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, ch. XI/XIII): on the normalisation of the branch D_e, the normal bundle is ξ^*N_{D_e} ≅ L_h^∨ ⊠ L_{h′}^∨. Here h, h′ are the two half-edges of e, and L_h is the cotangent line at the marked point h of the vertex carrying it. Pull back to C:
- If the vertex carrying h is constant along E′, this factor is a trivial bundle on C.
- If that vertex is moving, the factor is f_u^* L_h^∨, which is t-independent by Lemma S.

Hence the class of L_{e,f} in Pic(C) is independent of t.

**Proposition N (Abel constraint; sketch, subject to (a)–(c) and the orbifold bookkeeping at orbifold points of E′).** For every pair of edges e, f,

  Σ_j a_j^{(e,f)} · q_j(t) ~ D^{(e,f)}  in Pic(C),

where the integers a_j^{(e,f)} and the divisor D^{(e,f)}, supported on the fixed punctures, do not depend on t.

**Corollary N1 (partial pinning of sliding crossings).** Consider a (J5) junction for the Y_t-copy at q_1(t) ∈ C, and suppose:
- genus(C) ≥ 1;
- for some pair (e, f), the only junction point of E′ with nonzero coefficient that is not already pinned (by J1, J2 or J4 data) is q_1(t).

Then a_1 q_1(t) is constant in Jac(C). Multiplication by a_1 composed with the Abel–Jacobi map C → Jac(C) is finite-to-one when genus ≥ 1, so q_1(t) lies in a finite set, Y_t = f_x(q_1(t)) lies in a finite set, and R-Hol gives Y ≡ Y_0.

In the crossing coordinates (x, y), with E′ = {x = 0} and E = {y = 0}, we have s_A = x^a and s_G = x^b y^c (c ≥ 1). So the pair (e ∈ G-edges, f ∈ A-internal edges) has ord_{q_1} ρ = c·a ≠ 0. The nonzero-coefficient hypothesis on q_1 is therefore automatic for that pair. What is not automatic is that no *other* unpinned junction appears in the same relation.

**Dead end (precise).** When C has genus 0, Pic^0(C) = 0 and Proposition N carries no information: every degree-0 divisor is principal. Teichmüller-curve pieces (the pieces carrying area, by R-PA and R-T′) are frequently of genus 0, for example triangle-group Teichmüller curves. Several sliding points in the same relation also escape Corollary N1. So the normal-bundle move does not close MS8.

### round9_q9 (verbatim answer to last round's query on (Rig); bookkeeping line removed)
# round9_q9: attempt on (Rig) / (Rig-w) / realisability question Q1

## Status / plan (written first)
Plan:
1. Check whether the "2-dimensional open part of V_t" (approach 1 of the task), used *locally*, can pin anything. Statement attempted: Lemma Loc below, a local realisation of a moving constant factor by germs of admissible families.
2. Check whether the t = 0 information (Corollary AR, approach 2) is strong enough to force the factor M_{g_i,n_i} to be 0-dimensional or Y_0 to be isolated. Statement attempted: Example AR-real.
3. Give the global reduction that is actually available: the claim holds if total geodesy propagates to all V_t.
4. Explain why the Hodge-theoretic and Imayoshi–Shiga routes do not reach the constant factor (dead end).

Final status: **(Rig) and (Rig-w) are not proved. Q1 is not decided.** See §6. Literature results are cited from memory and marked as such.

Readings (R1) and (R2) of the task are adopted throughout.

## 1. Lemma Loc: the conclusion is not local, even with the 2-dimensional open part included

**Setting.**
- Let P be a point of ∂V_0 := closure(V_0) ∩ Δ_Γ. Then every component of P is smooth, because P lies in the open stratum Δ_Γ.
- Write Def(P) = ∏_{w∈V(Γ)} D_w × ℂ^{E(Γ)}. Here D_w is a small Kuranishi ball, in the interior, of the pointed component (P_w, special points), and the s_e (e ∈ E(Γ)) are plumbing parameters.
- U = Def(P)/Aut(P) is an orbifold chart of M̄_g at P. After linearisation, Aut(P) acts on Def(P), permuting the factors D_w according to its action on V(Γ).
- Near P, the strata of M̄_g are the images of {s_e = 0 for e ∈ S} × ∏_w D_w, for S ⊂ E(Γ).

**Lemma Loc.** Assume dim M_{g_i,n_i} > 0, and that the stabiliser Stab(i) ⊂ Aut(P) of the vertex i acts trivially on D_i. This holds e.g. when (Y_0, special points) has no automorphisms, or only the generic ones of M_{g_i,n_i}. Then there is a holomorphic family Φ_t (|t| small) of stratum-preserving biholomorphisms of U with Φ_0 = id, such that V_t^{loc} := Φ_t(V_0 ∩ U) satisfies:
- the local versions of (i), (ii) and of smooth triviality;
- π_i(closure(V_t^{loc}) ∩ Δ_Γ) = {Y_0 + t a} for some fixed a ≠ 0 in a chart of M_{g_i,n_i}, so Y_t ≠ Y_0 for t ≠ 0.

*Proof.*
- Pick 0 ≠ a ∈ T D_i (a linear chart). For each coset σ·Stab(i) ⊂ Aut(P), put a_{σ(i)} := σ_*a ∈ T D_{σ(i)}. This is well defined because Stab(i) acts trivially on D_i.
- Define Φ_t on Def(P) as translation by t·a_{w} in each factor D_w with w ∈ Aut(P)·i, and the identity on all other factors and on ℂ^{E(Γ)}.
- By construction Φ_t commutes with Aut(P), so it descends to U.
- It preserves each stratum, because these are coordinate subspaces in the ℂ^{E(Γ)}-factor times the full product of the D_w.
- Hence H_t := Φ_t is a smooth trivialisation that maps strata to strata. So (i), (ii) hold locally.
- The trace on Δ_Γ is Φ_t(∂V_0 ∩ U), whose i-coordinate is Y_0 + t a. ∎

**Consequence.** No argument that uses only germs of V_t, together with their 2-dimensional open part, at individual boundary points can prove the problem, (Rig) or (Rig-w). This sharpens round8_q9: Examples Z and Z′ were piece-level only, whereas Lemma Loc includes the 2-dimensional open part.

So approach 1 of the task has to use features that are global along whole compact curves. The normal-bundle constraint of round8_q7 §4 (Prop. N) is of that kind: it uses the compactness of the normalised piece C. As recorded there, however, it is empty when g(C) = 0.

**Open (Q-semi-global).** Does Φ_t extend to a stratum-preserving family on a neighbourhood of the whole compact curve closure(∂V_0) in M̄_g? If it does, the problem's claim is not even semi-global: only the part of V_t far from Δ_Γ can enter. The obstruction is of cohomological type, roughly a class in H^1 of the normal sheaf of the stratum along the curve. I have not computed it.

## 2. Corollary AR does not make the constant factor rigid at t = 0 (Example AR-real)

Recall Corollary AR (R8-10 §6). If vertex i carries η ≢ 0 at some scale, then Y_0^{cη̄/|η|} = Y_0 in T(Σ_i) for all |c| < 1. One might hope this forces dim M_{g_i,n_i} = 0, or makes Y_0 an isolated point of the locus it defines. Both hopes fail.

**Example AR-real (proved).** Let Σ_i have genus 0, with special points z_1, …, z_{n−1} ∈ ℂ and ∞ (n ≥ 4). Let η = dz², which has a pole of order 4 at ∞ and is holomorphic and nonzero on ℂ.

Claim: Y^{cη̄/|η|} = Y in T(Σ_i) for all |c| < 1 if and only if the points z_1, …, z_{n−1} lie on one real line.

*Proof.*
- η̄/|η| = dz̄/dz. So the affine deformation is realised by the real-linear map L_c(z) = z + c z̄, whose Beltrami coefficient is c. It fixes ∞ and sends z_k to z_k + c z̄_k.
- Equality in moduli means L_c(configuration) = A(configuration) for a complex affine map A, because Möbius maps fixing ∞ are affine. With A_k := z_k − z_1, this means
  (A_k + c Ā_k)/(A_2 + c Ā_2) = A_k/A_2 for all k.
- Clearing denominators, this holds for a given c ≠ 0 iff Ā_k A_2 = Ā_2 A_k, i.e. iff A_k/A_2 ∈ ℝ. So the condition is collinearity, and when it holds it holds for every c.
- Passing from moduli to T(Σ_i): c ↦ [Y^{cη̄/|η|}] ∈ T(Σ_i) is continuous on the connected unit disc, takes values in the discrete fibre of T(Σ_i) → M_{0,n} over [Y], and equals Y at c = 0. So it is constant. This is the same argument as in the proof of AR. ∎

So for n ≥ 4 the locus allowed by AR (for this type of η) is the real-collinear locus. It has positive real dimension n − 3, so Y_0 is not isolated in it.

**Remark (what AR would give if it held at all t).** In this example the AR-locus is a totally real subset; for n = 4 it is λ ∈ ℝ. Suppose AR held for every t, with η of this type. Then t ↦ Y_t would be a holomorphic map, by R-Hol, into a totally real set, hence constant. But AR at time t needs V_t to be totally geodesic, which is exactly what is not assumed. This is the second route of §3.

## 3. The reduction that is available: propagation of total geodesy

**Proposition TG (conditional; uses cited results).** Suppose every V_t, t ∈ Δ, is totally geodesic. Then closure(V_t) = closure(V_0) for all t, and in particular π_i(∂V_t) = {Y_0}.

*Proof.*
- **Countability (cited from memory).** A totally geodesic complex submanifold V ⊂ M_g of dimension ≥ 2 is determined by the closed GL₂(ℝ)-invariant set M_V of quadratic differentials whose Teichmüller discs are tangent to V. Indeed V is the projection of M_V, and M_V is a union of orbit closures. The relevant sources are Eskin–McMullen–Mukamel–Wright for the setting, and Eskin–Mirzakhani–Mohammadi with Filip for orbit closures (via the canonical double cover for quadratic differentials). Orbit closures are affine invariant submanifolds, and there are only countably many of them (they are defined over ℚ̄). Hence the set 𝒯 of totally geodesic subvarieties of M_g of dimension ≥ 2 is countable. I cite this chain from memory; the correspondence between totally geodesic submanifolds and invariant sets of differentials in particular should be checked.
- **Continuity.** By (R2), H is a homeomorphism of the compact space closure(V_0) × Δ̄′ (Δ′ a smaller disc) onto its image. So t ↦ closure(V_t) is continuous for the Hausdorff metric d_H on compact subsets of M̄_g.
- **Conclusion.** A countable metric space is totally disconnected: for x ≠ y, only countably many radii r are of the form d(x,z), so some r < d(x,y) avoids them, and the ball B(x,r) is clopen. The continuous image of the connected Δ in the countable space (𝒯, d_H) is therefore a point. Hence closure(V_t) = closure(V_0), so ∂V_t = ∂V_0 and Y_t = Y_0. ∎

So the problem reduces to the following statement, which is presumably also what the source paper ultimately wants:

**(TG-prop)** Total geodesy of V_0 propagates along admissible deformations.

This is the 2-dimensional analogue of the rigidity of Teichmüller curves. For curves it is known; I recall it from memory, by McMullen's and by Möller's arguments. Möller's route runs as follows:
- the rank-2 sub-local system L ⊂ R¹f_*ℂ belonging to the Teichmüller curve is topological;
- by Deligne's semisimplicity it underlies a sub-VHS for every member of a deformation;
- its Arakelov equality deg L^{1,0} = −χ/2 is an equality between topological invariants;
- so it persists, and Möller's characterisation (maximal Higgs ⇒ Teichmüller curve) gives total geodesy of every member.

**Route M (sketch, not proved).** For a 2-dimensional V_0, the analogue would need two things:
- (a) a Hodge-theoretic characterisation of totally geodesic surfaces by conditions that are topological or closed under deformation, e.g. a sub-VHS on which the Higgs field / second fundamental form satisfies an equality of Chern numbers;
- (b) the persistence of these conditions under (R1)/(R2).

I do not know such a characterisation in dimension 2 and did not establish one. This is the global input that, in my view, the problem needs. It is consistent with Lemma Loc, which says the input cannot be local.

## 4. Dead end: Hodge rigidity and Imayoshi–Shiga do not see the constant factor

- **Local system along ∂V_t.** Near ∂V_t, take the punctured tubular neighbourhood U*_t of the boundary divisor in a log-resolution of closure(V_t). Write N for the logarithm of the unipotent part of the monodromy around ∂V_t; it is Σ_e m_e N_e with the m_e topological (round8_q7 §4(a)).
- **The Y_t-part of the limiting MHS.** Gr^W_1 of the limiting MHS is ker N / im N ≅ ⊕_w H¹(P̄_w). Its summand H¹(Ȳ_t) is a sub-quotient local system on ∂V_t with **finite** monodromy, because the factor i is constant along ∂V_t. The positions of the special points of Y_t sit in the W_0 / W_2 extension data, again with finite monodromy along ∂V_t.
- **Why rigidity fails here.** After a finite cover these are *constant* variations, and a constant VHS on a fixed lattice can vary freely: every point of the period domain is a constant VHS. Deligne's rigidity (uniqueness of the Hodge structure on an irreducible local system with infinite monodromy, up to shift; Deligne 1987, from memory) and Imayoshi–Shiga / Arakelov–Parshin finiteness (as used in L2 and Prop. F) apply only to *non-isotrivial* data with infinite monodromy. Those tools pin moving vertices and never the constant one.
- **Where the pinning would have to come from.** Pinning Y_t must use how this constant sub-quotient sits inside the global local system on V_t, whose monodromy ρ(π₁V_0) is fixed and large. That is a statement about the extension of the boundary data into the interior of V_t, which is global.
- **The 2-dimensional Imayoshi–Shiga.** Applied to the whole family V_t → M_g, Imayoshi–Shiga would need a fixed complex structure on the base. The complex structure J_t := H_t^*(structure of V_t) on the smooth manifold V_0 varies with t, so the theorem does not apply. (Approach 3 of the task fails at this point.)

## 5. On Q1 (realisability of Z′-type deformations)

- A realisation needs a non-trivial admissible deformation of V_0 itself.
- By §3, such a deformation cannot consist of totally geodesic surfaces.
- If totally geodesic surfaces are rigid as subvarieties (expected, by analogy with Teichmüller curves), then no admissible non-trivial V_t exists, and the problem is vacuously true. I could neither prove nor refute this rigidity.
- By Lemma Loc, local realisations exist at every boundary point. So Q1 is a genuinely global question, about the extension of local deformations to closed subvarieties of M_g. I have no construction of a non-trivial global deformation of any known totally geodesic surface, e.g. the flex or gothic loci of EMMW (cited from memory), and no proof that none exists. **Q1 remains open.**

## 6. Final status

**Proved:**
- **Lemma Loc** (§1). Under the mild automorphism hypothesis stated there, at every point of ∂V_0 there are local admissible deformations, including the 2-dimensional open part, along which the constant factor moves. Hence (Rig), (Rig-w) and the problem's claim are not consequences of local data at boundary points. This sharpens Examples Z/Z′ of round8_q9, which were piece-level only.
- **Example AR-real** (§2). Corollary AR does not force dim M_{g_i,n_i} = 0, and does not isolate Y_0. For genus 0 with η = dz², the AR-locus is the totally real collinear locus.
- **Countable-space step of Prop. TG** (§3): a continuous family in a countable metric space is constant.

**Conditional / cited from memory:**
- **Prop. TG.** If all V_t are totally geodesic, the claim holds. This relies on the countability of totally geodesic subvarieties of dimension ≥ 2, via EMMW and EMM/Filip.

**Sketched only:**
- Route M: propagation of total geodesy via a Hodge-theoretic characterisation, in the style of Möller.

**Dead ends (with reasons):**
- Hodge rigidity and Imayoshi–Shiga do not reach the constant factor, because its sub-quotient has finite monodromy (§4).
- 2-dimensional Imayoshi–Shiga fails because the base complex structure varies (§4).

**Not proved / open:**
- (Rig) and (Rig-w) for every admissible family: **not proved**.
- Q1, the realisability of Z′-type deformations by an admissible global V_t: **open**.
- (Q-semi-global): extension of the local deformations of Lemma Loc to a neighbourhood of closure(∂V_0).
- (TG-prop): propagation of total geodesy, equivalently, for the purposes of this problem, rigidity of V_0 under admissible deformations.
- A Hodge-theoretic characterisation of totally geodesic surfaces that is stable under deformation (Route M (a)).

Overall: **not proved; open.**



### round10_q9 (verbatim answer to last round's query on (Rig); bookkeeping line removed)
# round10_q9: attempt on (Rig) / (Rig-w) via image-level rigidity

## Status / plan (written first)
Plan:
1. Make the "countability + continuity" part of the named approach (item 1) rigorous at image level, with no orbifold bookkeeping. Statement attempted: Lemma CD below. It turns out to apply to any vertex set M, so it covers joint images too.
2. Test the Hodge-theoretic half of item 1 (Möller's characterisation) at map level and at image level, and decide what it can and cannot give.
3. Item 2 (the other vertices): record what Lemma CD reduces (Rig) to, and why that reduction is not yet a proof.

Final status: **(Rig) and (Rig-w) are not proved.** The following are proved:
- a clean dichotomy (Lemma CD);
- a reformulation of (Rig-v) and of (Rig) as "countable-class membership for uncountably many t" (Cor. CD1, CD2);
- a proof that map-level Hodge theory cannot reach (Rig-v) (Prop. MH, which depends on a prior result, Prop X, that I have not re-checked).

What remains open is listed in §6.

Readings (R1) and (R2) are adopted throughout. G is a product-type stratum (the case relevant to Δ_Γ). E_0 is a piece, E_t := H_t(E_0), and W ⊂ ∏_w M̄_w × Δ is the irreducible 2-dimensional analytic set of Lemma R0. It is proper over Δ, and W_t = closure(E_t) (R7-5 L1, product case). These are prior results; I re-use them and do not re-prove them.

## 1. Lemma CD (countable dichotomy for image curves)

For a set M of vertices, write pr_M : ∏_w M̄_w → ∏_{u∈M} M̄_u, and K^M_t := pr_M(W_t). The special case M = {v} gives K^v_t. The case M = M(E) gives the joint image K(E_t).

**Lemma CD.** Let C ⊂ ∏_{u∈M} M̄_u be a closed analytic set, and put T_C := {t ∈ Δ : K^M_t ⊂ C}. Then exactly one of the following holds:
- (a) T_C = Δ;
- (b) T_C is a closed discrete subset of Δ.

In case (a), if C is an irreducible curve and K^M_t is a curve for some t, then K^M_t = C for all t.

*Proof.*
- Put Z_C := {(x,t) ∈ W : pr_M(x) ∈ C}. This is a closed analytic subset of W. Moreover t ∈ T_C ⟺ W_t ⊂ Z_C.
- **Case Z_C = W.** Then T_C = Δ.
- **Case Z_C ≠ W.** W is irreducible of dimension 2, so dim Z_C ≤ 1.
  - Let t ∈ T_C. The fibre W_t is a nonempty pure 1-dimensional analytic set (E_t is a curve), and it lies in Z_C. Each irreducible component of W_t is therefore a 1-dimensional irreducible analytic subset of the analytic set Z_C, which has dimension ≤ 1. So it is an irreducible component of Z_C, and it is contained in the fibre over t.
  - Z_C is closed in W, hence proper over Δ. For a compact set Q ⊂ Δ, the preimage of Q in Z_C is compact, so it meets only finitely many irreducible components of Z_C (irreducible components are locally finite).
  - Components that lie in fibres over different times are different. So only finitely many t ∈ T_C lie in Q. Hence T_C is closed and discrete.
- **The last sentence.** K^M_t is irreducible, being the image of the irreducible W_t: E_t = H_t(E_0) is irreducible by Lemma S″ of round8_q7, a prior result. Its dimension does not depend on t (L1′ of R7-5: a vertex is non-constant along E_t for one t iff for all t; prior result). So if K^M_t is a curve contained in the irreducible curve C, then K^M_t = C. ∎

**Corollary CD1 (countable classes).** Let 𝒞 be a countable set of irreducible curves in ∏_{u∈M} M̄_u. If K^M_t ∈ 𝒞 for uncountably many t ∈ Δ, then K^M_t = K^M_0 for all t.

*Proof.* We have {t : K^M_t ∈ 𝒞} ⊂ ∪_{C∈𝒞} T_C. A countable union of closed discrete subsets of Δ is countable. So some T_C is uncountable, hence not discrete. By Lemma CD, T_C = Δ and K^M_t = C for all t; in particular C = K^M_0. ∎

**Corollary CD2 (Teichmüller vertex; image level, no orbifold bookkeeping).** Let v be a Teichmüller vertex of E_0 (Theorem TV). Then the following are equivalent:
- (i) (Rig-v): K^v_t = K^v_0 for all t;
- (ii) K^v_t is a Teichmüller curve for uncountably many t;
- (iii) K^v_t is a Teichmüller curve for all t in some open subset of Δ.

*Proof.*
- (i) ⇒ (iii) holds because K^v_0 is a Teichmüller curve by Theorem TV.
- (iii) ⇒ (ii) is trivial.
- (ii) ⇒ (i) is Corollary CD1 with 𝒞 the set of closures of Teichmüller curves in M̄_v. This set is countable. *Cited from memory:* every Teichmüller curve is defined over a number field (McMullen, via rigidity; also Möller). An algebraic subvariety of the projective variety M̄_v defined over Q̄ is one of countably many. ∎

**Remark.**
- Corollary CD2 replaces the "continuity in t" step of item 1 of the named approach, and the analytic continuation step of Theorem L / Cor. G1. The type jump at t = 0 plays no role in it, because it compares closed image sets only. This is the second suggested way round the obstacle in item 1 ("compare … only through image curves").
- What remains of item 1 is exactly to show (ii): **the image curves K^v_t are Teichmüller curves for many t.** Nothing in the earlier rounds or in this one establishes that.
- The same argument applies to Y_t in the original problem: if Y_t lies in a countable set for uncountably many t, then Y ≡ Y_0. This is immediate from R-Hol in any case.

## 2. Item 1 at map level: Möller's characterisation cannot give (ii) through the maps f_t

**Proposition MH.** Fix a generic time t ∉ D (Lemma G). Consider f_t = π_v ∘ ν_t : O_t → M_v, with the minimal orbifold structure O_t and the lift F_t : H → T_v. Then the following are equivalent:
- (1) the weight-one VHS pulled back by f_t (on a finite cover of O_t without orbifold points) contains a rank-2 maximal-Higgs summand;
- (2) (H_0) holds at time t, i.e. F_t is an isometric embedding onto a Teichmüller disc.

Consequently, by Cor. G1, "map-level maximal Higgs at one generic t" already implies (Rig-v). Conversely, at a map-level type jump of the kind in Prop X of R7-7 (reported there as a jump at which the image stays constant), (1) fails at every generic t, even though (Rig-v) holds.

*Proof (uses Möller's theorem, cited from memory: Möller, "Variations of Hodge structures of a Teichmüller curve", JAMS 2006).*
- (2) ⇒ (1). Möller's theorem, applied to the Teichmüller curve, gives a maximal-Higgs rank-2 summand L. Under (2), f_t is an orbifold-unramified covering of the Teichmüller curve, and pulling back along it preserves maximality: the Higgs field θ : L^{1,0} → L^{0,1} ⊗ Ω^1(log) stays an isomorphism under unramified pull-back.
- (1) ⇒ (2). By Möller's theorem, maximal Higgs forces the period map of L to be a local isometry onto H. The ω-direction then generates a Teichmüller disc, and the lift F_t is the Teichmüller embedding composed with that isometry, hence unramified.
- **Prop X.** Suppose f_t factors as (Teichmüller curve map) ∘ h_t, with h_t a branched cover of orbifolds that is ramified at moving points. At a ramification point x of order e > 1, the Higgs field of h_t^*L, as a map L^{1,0} → L^{0,1} ⊗ Ω^1, vanishes to order e − 1. So h_t^*L is not maximal Higgs.
- Uniqueness of L: any rank-2 summand that is maximal Higgs would give, by Möller, a Teichmüller embedding lift, contradicting ramification. ∎

**Consequence.** The map-level form of item 1 ("show f_j(E_t) is Teichmüller via Möller for the pulled-back VHS") proves strictly more than is true in Prop X. So it cannot be the general route. Möller's characterisation has to be applied to the **normalised image curve** K̃^v_t with its own minimal orbifold structure.

## 3. Item 1 at image level: equivalent to excluding image-level jumps (sketch)

**Setup.**
- Let 𝓘 := (pr_v × id)(W) ⊂ M̄_v × Δ. It is irreducible, 2-dimensional and proper over Δ (Remmert).
- Let 𝓘^ν be its normalisation. For t outside a discrete set D_I, the fibre 𝓘^ν_t is the normalisation K̃^v_t of K^v_t. Reason: 𝓘^ν → 𝓘 is finite and bimeromorphic, and its non-isomorphism locus is a curve, which meets generic fibres in finitely many points.
- Lemma G's proof uses only an irreducible 2-dimensional analytic set that is proper over Δ, together with a fibrewise non-constant map to M̄_v. So it applies verbatim to 𝓘^ν. The minimal orbifolds O^I_t (t ∉ D_I) therefore all have one type and one monodromy ρ^I_*.
- By the argument of §2 (minimal orbifold of a Teichmüller curve normalisation = the Veech orbifold H/Γ′, since D is injective), K^v_t is a Teichmüller curve iff (H_0) holds for the image map at t.

**What follows.**
- By Cor. CD2, (Rig-v) ⟺ the image map is Teichmüller at one t ∉ D_I. That is, either all generic images are Teichmüller curves, or none is.
- Suppose L (the rank-2 summand on H/Γ′) is invariant under ρ^I_*, i.e. the cone generators produced at 0 by Cor. G3 preserve L. Then the Toledo invariant of ρ^I_*|_L is constant on Δ \ D_I. Milnor–Wood gives deg L_t^{1,0} ≤ −χ(O^I_t)/2 at generic t, while at t = 0 equality holds with −χ(O^I_0)/2.
- So, by the additivity of the Toledo invariant over S° and the bad discs (sketched, not checked in detail), Arakelov equality at generic t ⟺ χ(O^I_t) = χ(O^I_0) ⟺ **no image-level type jump at 0**.
- This is the image-level analogue of the §4 dead end of round7_q7. The Hodge route is equivalent to excluding image-level jumps; it gives no independent proof of that.

**The multiple-fibre phenomenon (why rigidity of K^v_0 alone cannot suffice).**
- Let m_0 be the multiplicity of the central fibre of 𝓘 along K^v_0.
- If m_0 > 1, then (Rig-v) fails by Lemma CD. Indeed, if K^v_t = K^v_0 for all t, then 𝓘 = K^v_0 × Δ, which has reduced central fibre.
- In general analytic geometry, rigid curves can be cycle-limits with multiplicity of moving curves. *Classical example, from memory:* a multiple fibre mF_0 of an elliptic surface. F_0 has torsion non-trivial normal bundle, so it is rigid, yet the nearby fibres are smooth curves converging to mF_0.
- So McMullen's rigidity of Teichmüller curves (a statement about maps from a fixed orbifold) does not by itself exclude m_0 > 1. Excluding it needs input specific to M̄_v or to V_t.
- After the base change t = s^{m_0} and normalisation, an m_0 > 1 scenario becomes a map-level family with reduced central fibre mapping with degree m_0 onto K^v_0. This family must have a map-level type jump: otherwise (O) holds, Lemma R* gives a constant image, and m_0 = 1, a contradiction. So the m_0 > 1 case is again a type-jump case.

## 4. Item 2 (other non-constant vertices): what Lemma CD gives

**Corollary CD3.** For a piece E_0 with non-constant vertex set M = M(E_0), (Rig) holds for E_0 iff the joint image K(E_t) belongs to some countable class of curves for uncountably many t.
- A natural countable class is: curves in ∏_{u∈M} M̄_u defined over Q̄.
- In particular, (Rig) for E_0 follows if K(E_t) is defined over Q̄ for uncountably many t.

*Proof.* "Only if" is trivial. "If" is Cor. CD1 with M = M(E_0). ∎

**Assessment.**
- At t = 0, I expect K(E_0) to be defined over Q̄ (boundary data of a totally geodesic surface). I have not proved this.
- For t ≠ 0 there is no reason for arithmeticity, because V_t is not totally geodesic.
- Examples Z and Z′ (round8_q9) satisfy every piece-level hypothesis and have K(E_t) defined over Q̄ only for countably many t. So, as before, the input must be global in V_t.
- Lemma Loc (round9_q9) shows that local input at boundary points of V_t is not enough either.
- None of the three candidate inputs listed in the task for item 2 produces such a countable-class membership:
  - multi-scale / affine-disc structure: it exists only at t = 0;
  - normal-bundle / plumbing ratios: empty in genus 0, per round8_q7;
  - Imayoshi–Shiga on the 2-dimensional family: the base complex structure varies, per round9_q9 §4.

## 5. A remark on the whole problem (same mechanism)

Lemma CD is a statement about cycle families, so it extends to closure(V_t) itself. By (R1), closure(𝒱) is an irreducible analytic set in M̄_g × Δ, proper over Δ. The same proof shows: if closure(V_t) belongs to a countable family of surfaces (e.g. surfaces defined over Q̄, or totally geodesic surfaces) for uncountably many t, then V_t is constant.

This strengthens Prop. TG of round9_q9: total geodesy is needed only for uncountably many t, not for all t, and the countable-metric-space argument is not needed. Combining it with countability of totally geodesic surfaces (cited from memory, as in round9_q9 §3) gives:

**Prop. TG′.** If V_t is totally geodesic for uncountably many t, then closure(V_t) = closure(V_0) for all t, hence Y_t = Y_0.

## 6. Final status

**Proved (given the cited prior results W, L1/L1′, Lemma S″ and the cited countability of Teichmüller curves):**
- Lemma CD and Corollaries CD1–CD3.
  - (Rig-v) ⟺ K^v_t is a Teichmüller curve for uncountably many t.
  - (Rig) for a piece ⟺ its joint image lies in a countable class (e.g. defined over Q̄) for uncountably many t.
  - Neither statement involves any orbifold bookkeeping or the type jump at t = 0.
- Prop. TG′ (strengthening of Prop. TG).
- Prop. MH:
  - map-level maximal Higgs at one generic t ⟺ (H_0) at that t;
  - so the map-level Hodge route (item 1 as stated) is too strong and fails in Prop X-type situations;
  - Möller must be applied to image normalisations.
  - This uses Möller's theorem from memory, and Prop X as reported in R7-7.

**Sketched only:**
- §3: at image level, the Hodge/Arakelov route is equivalent to excluding image-level type jumps (when L extends).
- §3: m_0 > 1 forces a map-level jump after base change.

**Not proved / open:**
- (Rig-v) in general, i.e. that K^v_t is a Teichmüller curve for many t. Equivalently: no image-level type jump at 0, and m_0 = 1.
- (Rig) and (Rig-w) for the other non-constant vertices; no global input found.
- Whether K(E_0) is defined over Q̄.
- Q1/Q2 of earlier rounds: realisability of moving deformations, and rigidity of totally geodesic surfaces under admissible deformations.

Overall: **not proved; open.**


### round11_q10 (verbatim answer to last round's query on (Rig); bookkeeping line removed)
# round11_q10: attempt on (Rig) / (Rig-v): maximum-principle route

## Status / plan (written first)
Plan:
1. Point 1 of the task. Replace the orbifold-sensitive inputs (type jumps, m_0) by a purely image-level global input: a plurisubharmonic (psh) function near the Teichmüller curve. Statement attempted: Prop. MP. If K^v_0 is "psh-isolated", then (Rig-v) holds. No orbifold bookkeeping, no m_0, no type jump.
2. Test whether psh-isolation, or its algebraic shadow (negative self-intersection), can hold in general. Statement attempted: Prop. DP. For vertices of type (0,5), every closed Teichmüller curve moves in a linear pencil of curves in M̄_{0,5}. So psh-isolation fails there, and (Rig-v) cannot come from the ambient geometry of M̄_v alone.
3. The same principle applied to closure(V_0) itself (Prop. MP′), and what it would need.

Readings (R1), (R2) of the task are adopted throughout. G is product type. E_0 is a piece, E_t := H_t(E_0), and W is the 2-dimensional family of Lemma R0 (prior result, not re-proved), proper over Δ with W_t = closure(E_t). K^v_t := pr_v(W_t).

Final status: see §5. **(Rig), (Rig-w) and (Rig-v) are not proved in general.**

## 1. Prop. MP: a maximum-principle criterion for (Rig-v) and (Rig) (proved)

Conventions.
- M̄_v is the coarse projective variety, a normal complex space.
- A function φ : Ω → [−∞, ∞) on an open subset Ω of a normal complex space is *psh* if it is upper semicontinuous and every point has a neighbourhood with a local embedding into some ℂ^N on which φ is the restriction of a psh function.
- The pull-back of a psh function by a holomorphic map from a connected Riemann surface is subharmonic or ≡ −∞.

**Proposition MP.** Let M ⊂ V(G) be a set of vertices and K_0 := K^M_0 = pr_M(W_0) ⊂ ∏_{u∈M} M̄_u. Assume K_0 is a curve. Write M_M := ∏_{u∈M} M_u and ∂_M := ∏_{u∈M} M̄_u \ M_M. Suppose there are:
- an open neighbourhood U of K_0 in ∏_{u∈M} M̄_u, and
- a psh function φ on U ∩ M_M that is bounded above,

such that

(★) for every irreducible compact curve C ⊂ U with C ⊄ ∂_M and C ≠ K_0, the function φ is not constant on C ∩ M_M.

Then K^M_t = K_0 for all t ∈ Δ. In particular:
- M = {v} with v a Teichmüller vertex gives (Rig-v);
- M = M(E_0) gives (Rig) for this piece;
- (Rig) for this piece in turn gives (Rig-w) for this piece, by round8_q7 Cor. S′(a).

*Proof.*
- **Step 1 (K^M_t ⊂ U for small t).** Suppose not. Then there are t_n → 0 and x_n ∈ W_{t_n} with pr_M(x_n) ∉ U. W is proper over Δ, so after passing to a subsequence x_n → x ∈ W. Since W is closed, x ∈ W_0. Then pr_M(x) ∈ K_0 ⊂ U, and U is open, so pr_M(x_n) ∈ U for large n. This is a contradiction. Hence there is ε > 0 with K^M_t ⊂ U for |t| < ε.
- **Step 2 (K^M_t is an irreducible compact curve not inside ∂_M).**
  - W_t = closure(E_t) is irreducible, because E_t = H_t(E_0) is irreducible (round8_q7 Lemma S″, prior result).
  - So K^M_t is irreducible and compact (Remmert).
  - It is a curve, because "pr_M non-constant on E_t" does not depend on t (L1′, prior result).
  - It meets M_M, because E_t ⊂ ∏_w M_w.
- **Step 3 (maximum principle).** Fix |t| < ε and let n : C̃ → K^M_t be the normalisation. C̃ is a compact connected Riemann surface.
  - F := n^{-1}(∂_M) is a proper analytic subset of C̃, hence a finite set.
  - ψ := φ∘n is subharmonic (or ≡ −∞) on C̃ \ F and bounded above.
  - A subharmonic function that is bounded above extends subharmonically across a finite set (removable singularities). So ψ extends to a subharmonic function on the compact connected C̃, or is ≡ −∞.
  - By the maximum principle ψ is constant. Hence φ is constant on K^M_t ∩ M_M.
  - By (★), K^M_t = K_0 for |t| < ε.
- **Step 4 (all t).** Lemma CD (round10_q9) with C := K_0: the set T_C contains the disc |t| < ε, so it is not discrete. Hence T_C = Δ and K^M_t = K_0 for all t. ∎

**Remarks.**
1. Prop. MP compares closed image sets only, so it does not see:
   - orbifold type jumps at t = 0;
   - the multiplicity m_0;
   - the degree d_0;
   - the twin/labelling ambiguities.

   It needs one global input: a psh "potential" around K_0 that separates K_0 from all other compact curves nearby. This is the "global input" of task item 1, in a form that does not need the deformation to be totally geodesic.
2. It is enough to verify (★) for the curves that actually occur, C = K^M_t with t small. The proof uses (★) only for them.
3. (★) forces a strong rigidity: K_0 is not the limit of any family of compact curves C_s ≠ K_0 (s → 0) contained in U. Steps 1–3 apply verbatim to such a family. So (★) can only hold if K_0 is *infinitesimally isolated among compact curves*, whatever their boundary behaviour. §2 shows this fails in general.

## 2. Prop. DP: psh-isolation and negativity fail for vertices of type (0,5) (proved, modulo classical facts cited from memory)

**Classical facts used (cited from memory).**
- (F1) M̄_{0,5} is the del Pezzo surface S_5 of degree 5, i.e. the blow-up of ℙ² at 4 general points. It is smooth and projective, with −K_S ample, K_S² = 5 and χ(O_S) = 1.
- (F2) ∂M̄_{0,5} is the union of the ten (−1)-curves D_{ij} of S_5.
- (F3) M_{0,5} contains closed Teichmüller curves. Example: take a Veech-type Teichmüller curve of genus-2 forms ω ∈ ΩM_2(2) and divide by the hyperelliptic involution J. Then ω² descends to a quadratic differential on ℙ¹ with simple poles at the 5 Weierstrass points other than the zero, and a simple zero at the image of the zero. Its Teichmüller disc in T_{0,5} has a lattice stabiliser, so it projects to a closed Teichmüller curve, and a component of its preimage in the labelled M_{0,5} is again one.

**Proposition DP.** Let C ⊂ M̄_{0,5} = S_5 be the closure of any irreducible curve meeting M_{0,5}, e.g. a closed Teichmüller curve. Then:
- (a) C² ≥ 0;
- (b) dim |C| ≥ 1. In particular C is a member of a pencil of curves, all compact and linearly equivalent to C, filling S_5.

Consequently, if v is a vertex of type (0,5) and K^v_0 is a Teichmüller curve:
- no psh function as in Prop. MP exists for M = {v};
- no negativity argument (K_t·K_0 ≥ 0 versus K_0² < 0) can give (Rig-v).

*Proof.*
- **(a).** Adjunction gives C² + K_S·C = 2p_a(C) − 2 ≥ −2. Since −K_S is ample, K_S·C ≤ −1, so C² ≥ −1. If C² = −1, then p_a = 0 and K_S·C = −1, so C is a (−1)-curve. By (F2) C would then be a boundary curve, contradicting C ∩ M_{0,5} ≠ ∅. Hence C² ≥ 0.
- **(b).**
  - Riemann–Roch on S_5 gives h^0(O(C)) − h^1(O(C)) + h^2(O(C)) = 1 + (C² − K_S·C)/2.
  - h^2(O(C)) = h^0(O(K_S − C)) = 0, because (K_S − C)·(−K_S) < 0 and −K_S is ample.
  - Hence h^0(O(C)) ≥ 1 + (C² − K_S·C)/2 ≥ 1 + (0 + 1)/2. As h^0 is an integer, h^0(O(C)) ≥ 2, i.e. dim |C| ≥ 1.
- **Consequence for Prop. MP.**
  - Let {C_s} be a pencil in |C| through C = C_0. Its members are compact curves, and C_s → C_0 as s → 0 (in the Hausdorff sense, after choosing a line in |C| through C).
  - For small s ≠ 0, C_s ⊂ U. This is Step 1 of Prop. MP, applied to the incidence variety of the pencil, which is proper over the parameter line.
  - Moreover C_s has an irreducible component C′_s ≠ C_0. Otherwise C_s = k·C_0 + 0 with k = 1 by linear equivalence (pair with an ample class), so C_s = C_0 as divisors, which is false for s ≠ 0.
  - C′_s is compact, irreducible, not inside ∂ (otherwise it would be a line D_{ij}; but a fixed line cannot be a component of C_s for all small s, since then it would be a component of the limit C_0 — and only finitely many members of a pencil without fixed component contain a given curve; if D_{ij} is a fixed component of the pencil, remove the fixed part first, which does not affect C_0 = C irreducible ⊄ ∂).
  - Steps 1–3 of the proof of Prop. MP then make φ constant on C′_s ∩ M_{0,5}, contradicting (★). So no such φ exists.
- **Consequence for the intersection argument.** The would-be argument runs: Lemma Deg gives [K_t] = (d_0/d_t)[K_0] in H_2(M̄_v; ℚ), and K_t ≠ K_0 forces K_t·K_0 ≥ 0, which contradicts K_0² < 0. Since K_0² ≥ 0 by (a), this argument cannot start. ∎

(Fixed components: a pencil |C| ⊃ {C_s} may have a fixed part F. Since C_0 = C is irreducible and C_0 = F + (moving part at s = 0), and the moving part is non-zero, F = 0. So the pencil has no fixed component, and a given curve is a component of only finitely many members.)

**What Prop. DP shows.**
- (Rig-v) is not a consequence of the position of the Teichmüller curve K^v_0 in M̄_v. Nearby compact curves, even homologous ones, exist.
- So any proof must use the constraints the problem puts on K^v_t, which are:
  - (c1) K^v_t is the v-image of a piece of a surface V_t in M_g. This is global and is what Lemma Loc said cannot be used locally.
  - (c2) the boundary trace K^v_t ∩ ∂M̄_v is the v-image of H_t-transported punctures, with stratum-preserving behaviour (Lemma P0). This is a strong constraint on the members of |K_0|: a generic member of the pencil meets the ten lines D_{ij} transversally at points that move, while K_0 itself, a Teichmüller curve, meets ∂ at its cusps. The cusps are typically the 0-dimensional strata, where a cylinder decomposition with 2 cylinders pinches two curves.
- This is consistent with Examples Z, Z′ (round8_q9) and Lemma Loc (round9_q9). Prop. DP adds that even the *ambient* geometry of a single factor is not enough. Whatever pins K^v_t must be the boundary constraint (c2), combined with (c1).

**The intersection version that would use (c2) (open).** Let 𝔽 ⊂ |C| be the family of members C′ whose intersection with ∂M̄_{0,5}, as a 0-cycle on each D_{ij} with the stratum data, has the "same combinatorial type" as C ∩ ∂ (same strata, same local contact orders), with the points allowed to move.
- (Q-DP) Is a closed Teichmüller curve isolated in 𝔽?
- This is a concrete, finite-dimensional question about plane curves (via S_5 → ℙ²) that I have not answered.
- Under (Rig-v) one needs exactly isolation of K_0 among the K^v_t. By Lemma P0 and node counting, those lie in 𝔽 provided the contact orders are also transported. That transport is not proved: H_t is only a homeomorphism, but local intersection multiplicities of a curve with a divisor are topological invariants (linking numbers) once the curve and divisor are fixed analytic sets, so I expect this step to go through.

## 3. Prop. MP′: the same principle for the whole surface (proved; hypothesis open)

**Proposition MP′.** Suppose closure(V_0) has an open neighbourhood U in M̄_g and a psh function φ on U ∩ M_g that is bounded above, such that φ is non-constant on S ∩ M_g for every irreducible compact analytic surface S ⊂ U with S ⊄ ∂M̄_g and S ≠ closure(V_0). Then closure(V_t) = closure(V_0) for all t. In particular ∂V_t = ∂V_0 and Y_t = Y_0, which is the problem's claim.

*Proof.*
- **Small t.** closure(𝒱) is closed analytic in M̄_g × Δ by (R1), hence proper over Δ (M̄_g is compact). The argument of Step 1 of Prop. MP gives closure(V_t) ⊂ U for |t| < ε.
- **Each fibre.** closure(V_t) is irreducible, since V_t ≅ V_0 is connected and smooth, and it is a surface not contained in ∂M̄_g. Let n : S̃ → closure(V_t) be its normalisation, a compact connected normal surface.
  - ψ := φ∘n is psh on S̃ \ n^{-1}(∂M̄_g) and bounded above.
  - A psh function bounded above extends psh across a nowhere dense analytic subset of a normal space (Grauert–Remmert; cited from memory).
  - By the maximum principle on the compact connected normal space S̃, ψ is constant (or ≡ −∞).
  - By hypothesis, closure(V_t) = closure(V_0) for |t| < ε.
- **All t.** Apply Lemma CD in its surface version (round10_q9 §5, same proof with W replaced by closure(𝒱)): the set of t with closure(V_t) ⊂ closure(V_0) contains a disc, hence is Δ. Equality follows from irreducibility and equal dimension. ∎

**Assessment.**
- The hypothesis of MP′ forces closure(V_0) to be isolated among *all* compact surfaces in a neighbourhood. This is stronger than (Q2) of the earlier rounds (rigidity under *admissible* deformations).
- I know of no candidate φ. Krushkal's theorem (cited from memory: log tanh d_T(x_0, ·) is psh on T_g, being the pluricomplex Green function) gives psh functions on T_g that are not Mod_g-invariant. A minimum over Mod_g-translates, or over a disc, is not psh in general, and Kiselman's minimum principle needs convexity data I do not have.
- By the analogue of Prop. DP, such a φ cannot exist whenever closure(V_0) moves in a positive-dimensional family of compact surfaces in M̄_g. I did not decide whether known totally geodesic surfaces do. A candidate test case is the bielliptic locus in M_2, a covering-construction image and therefore totally geodesic, which is a divisor in M̄_2 (dim 3). It is psh-isolated only if it is not a moving divisor.

## 4. Task item 3: the weakest consequence, in a holomorphic form (Lemma HQ, proved)

**Lemma HQ (isolated boundary points move holomorphically).** Let G′ be a stratum and Q_0 an isolated point of A := closure(V_0) ∩ Δ_{G′}. Put Q_t := H_t(Q_0). Then t ↦ Q_t is a holomorphic map Δ → Δ_{G′} (into the coarse space; into ∏_w M_w when G′ is of product type). Consequently exactly one of the following holds:
- Q_t ≡ Q_0;
- for every point Q′, the set {t : Q_t = Q′} is closed and discrete.

So Q_t ≡ Q_0 as soon as Q_t lies in a countable set for uncountably many t.

*Proof.*
- **Σ is open in an analytic set.** 𝒜 := closure(𝒱) ∩ (Δ_{G′} × Δ) is a locally closed analytic set, by (R1). By (R2), H restricts to a homeomorphism A × Δ → 𝒜 over Δ. {Q_0} × Δ is open in A × Δ, because Q_0 is isolated in A. So Σ := H({Q_0} × Δ) is open in 𝒜, hence is itself a locally closed analytic set.
- **pr_Δ|_Σ is biholomorphic on the normalisation.**
  - Σ is homeomorphic to Δ via pr_Δ, so it is a pure 1-dimensional analytic set that is a topological 2-manifold.
  - Hence Σ is unibranch at every point, and its normalisation Σ̃ → Σ is a bijection.
  - pr_Δ : Σ̃ → Δ is a bijective holomorphic map of Riemann surfaces, hence biholomorphic.
  - Therefore t ↦ Q_t, the composite Δ → Σ̃ → Σ → Δ_{G′}, is holomorphic.
- **The dichotomy.** The identity theorem applied to the holomorphic map t ↦ Q_t. In the product case use the coordinates of ∏ M_w; in general, pull back local holomorphic functions on the coarse space. ∎

**Statement of the weakest consequence (Rig-0).** For every stratum G′ and every point Q_0 isolated in closure(V_0) ∩ Δ_{G′}, Q_t = Q_0 for all t.

Relation to the chain:
- The punctures of a piece E′ that are not interior points of another piece of their stratum are exactly the isolated points of their stratum's part of B_t.
- At such a puncture, (J1) and (J2) of round8_q7 Lemma J pin the Y_t-copy if (Rig-0) holds there. Indeed, the components of the constant stable curve Q_0 form a finite set, and the Y_t-copy component varies continuously in t (in the labelled chart of Q_0), so it is constant.
- So (Rig-0) can replace (Rig) / (Rig-w) in (J1) and (J2). It does not cover (J4), which concerns interior points of a 1-dimensional piece.
- By Lemma HQ, (Rig-0) at Q_0 is equivalent to "Q_t lies in a countable set for uncountably many t", for instance the set of stable curves defined over Q̄.

Status: Lemma HQ is proved. (Rig-0) itself is **not proved**. I have no global input that makes Q_t arithmetic or otherwise countable for t ≠ 0.

## 5. Final status

**Proved** (readings (R1), (R2); prior results W/Lemma R0, L1′, Lemma S″ and Lemma CD re-used, not re-proved; classical facts cited from memory as marked):
- **Prop. MP.** If the image curve K^M_0 has a neighbourhood carrying a bounded-above psh function that is non-constant on every other compact curve, then K^M_t = K^M_0 for all t. This gives (Rig-v) for M = {v}, and (Rig) and hence (Rig-w) for M = M(E_0). It needs no orbifold bookkeeping and does not see m_0 or type jumps.
- **Prop. MP′.** The same for closure(V_0) in M̄_g. Its hypothesis would prove the problem's claim outright.
- **Prop. DP.** For a vertex of type (0,5), every curve in M̄_{0,5} through the interior has C² ≥ 0 and moves in a pencil. So psh-isolation (Prop. MP) and negativity arguments cannot prove (Rig-v) there. Any proof must use the boundary constraint (c2) together with the global constraint (c1). This uses (F1)–(F3) from memory.
- **Lemma HQ.** Points of closure(V_0) isolated in their stratum move holomorphically under H_t. So (Rig-0), the weakest consequence covering junction types (J1) and (J2), is equivalent to countable-class membership for uncountably many t.

**Partial / conditional:**
- (Rig-v), (Rig) and the problem itself follow under the psh-isolation hypotheses of MP / MP′. Those hypotheses are **not verified** for any piece or any V_0, and by Prop. DP they fail for type-(0,5) Teichmüller vertices.

**Not proved / open:**
- (Rig), (Rig-w) and (Rig-v) for every admissible family: **not proved**. In particular, excluding m_0 > 1 and image-level type jumps (task point 1) is not achieved. Prop. MP would bypass them but its hypothesis is unavailable.
- Task point 2 (pinning the other non-constant vertices): no progress beyond Prop. MP with M = M(E_0).
- (Rig-0): open.
- (Q-DP): is a closed Teichmüller curve in M̄_{0,5} isolated among curves of its linear system with the same combinatorial boundary contact type? Also open: the transport of contact orders by H_t.
- Is closure(V_0) psh-isolated, or at least non-moving, among compact surfaces in M̄_g? This is a strengthening of Q2. The bielliptic locus in M̄_2 is a test case.
- Q1/Q2 of the earlier rounds remain open.

Overall: **not proved; open.**


### round11_q6 §4 (verbatim): Lemma TR
## 4. Second move: Thurston length-spectrum dominance for the Teichmüller vertex of a piece

**Setting.**
- E_0 is a 1-dimensional piece in a product-type stratum Δ_G, and E_t is its transport. A homeomorphism of curves maps irreducible components to irreducible components (they are the closures of the components of the complement of the non-manifold points). So H_t maps closure(E_0) ∩ Δ_G onto closure(E_t) ∩ Δ_G, and it induces homeomorphisms between the normalisations (it maps local branches to local branches), with punctures going to punctures.
- K_t is the normalisation of E_t, a punctured compact Riemann surface.
- By Theorem TV (entry 70) there is a vertex j such that f_0 := π_j ∘ ν_0 : K_0 → M_j is a proper orbifold covering of a Teichmüller curve C = H/Γ_C ⊂ M_j, and the ends of K_0 map to cusps.
- f_t := π_j ∘ ν_t : K_t → M_j.

**Hypothesis (OT).** The orbifold structure that f_t induces on K_t (cone points and their orders, read off from local lifts to T_j) is carried by H_t to that of K_0. Then the orbifold fundamental groups are all identified with one group G := π_1^orb(K_0). G is a lattice, because K_0^orb = H/G is a finite-area orbifold cover of C.

**Lemma TR.** Under (R1), (R2) and (OT), for every t the following hold.
- K_t is isometric to K_0, by an isometry homotopic to the map induced by H_t.
- f_t composed with this isometry equals f_0.

In particular closure(π_j(E_t)) = closure(π_j(E_0)) = C̄. The Teichmüller-vertex factor of every piece is t-independent.

*Proof.*
1. *Lifts.* Lift f_t to f̃_t : H → T_j, equivariant for ρ_t : G → Mod_j, and choose the lifts continuously in t. Mod_j is discrete and G is finitely generated, so ρ_t = ρ is independent of t. Let G_t ⊂ PSL_2(R) be the Fuchsian group of K_t^orb, marked by G.
2. *Contraction.* By Royden's theorem (also for T_{g,n}; cited from memory) the Teichmüller metric is the Kobayashi metric. The Poincaré metric, normalised to curvature -4, is the Kobayashi metric of H. Holomorphic maps contract Kobayashi distance, so d_T(f̃_t z, f̃_t w) ≤ d_H(z, w).
3. *t = 0.* The map f̃_0 is an isometric holomorphic embedding onto the Teichmüller disc D_0 of a Veech surface (X, q). ρ(G) preserves D_0 and acts on it as G acts on H. For hyperbolic γ ∈ G, ρ(γ) is affine with hyperbolic derivative, hence pseudo-Anosov, with Teichmüller translation length τ(ρ(γ)) = ℓ_0(γ).
4. *Bers (cited from memory).* For a pseudo-Anosov φ, d_T(x, φx) ≥ τ(φ), with equality exactly on the unique φ-invariant geodesic A_φ. Equality means the extremal map x → φx is a Teichmüller self-map of x in the class φ with dilatation λ_φ. Such a map is affine for some q on x, so x lies on the invariant geodesic, and that geodesic is unique. Here A_{ρ(γ)} ⊂ D_0.
5. *Length dominance.* For z on the axis of γ in H (acting through G_t):
   τ(ρ(γ)) ≤ d_T(f̃_t z, ρ(γ) f̃_t z) = d_T(f̃_t z, f̃_t(γz)) ≤ ℓ_t(γ).
   So ℓ_t(γ) ≥ ℓ_0(γ) for every hyperbolic γ.
6. *Thurston (cited from memory, "Minimal stretch maps between hyperbolic surfaces").* For complete finite-area marked hyperbolic structures X, Y on the same surface, sup_γ ℓ_Y(γ)/ℓ_X(γ) ≥ 1, with equality iff X = Y.
   - Pass to a torsion-free normal subgroup G' of finite index in G (Selberg). Both structures restrict to marked structures of the same type on H/G'. By step 5, sup ℓ_0/ℓ_t ≤ 1, so the two G'-representations are conjugate by some A.
   - For g ∈ G, the element ρ_0(g)^{-1} A ρ_t(g) A^{-1} centralises the lattice ρ_0(G'), so it is trivial.
   - Hence G_t = A G_0 A^{-1} as marked groups. Identify them, so ℓ_t = ℓ_0.
7. *Image lies in D_0.* Steps 4 and 5 are now equalities. Hence f̃_t(z) ∈ A_{ρ(γ)} ⊂ D_0 for every z on the axis of every hyperbolic γ. The axes of hyperbolic elements of a lattice are dense in H, and D_0 is closed. So f̃_t(H) ⊂ D_0.
8. *Conclusion.* D_0 is a closed complex submanifold and f̃_0 : H → D_0 is biholomorphic. So g_t := f̃_0^{-1} ∘ f̃_t is a holomorphic, G-equivariant self-map of H.
   - If g_t were not an automorphism, Schwarz–Pick would make it strictly contracting. Then for z on an axis, d(g_t z, γ g_t z) < ℓ_0(γ) = τ, which contradicts step 4.
   - So g_t is an automorphism commuting with the lattice G, and therefore g_t = id. Thus f̃_t = f̃_0. ∎

**Status of TR:** proved under (OT). Without (OT), cone points of K_t^orb could appear or disappear at t ≠ 0. I have not ruled this out, and the run has no statement covering it.

**Why TR cannot reach Y (dead end for MS11).**
- TR pins only the vertex j whose map is a Teichmüller-isometry. The constant vertex Y never enters it: π_i is constant on ∂V_t, so there is no length spectrum to compare.
- At a puncture-MOV endpoint of MS11, the moving Y_0-copy cannot be a Teichmüller vertex of the leaving piece. By TV, Teichmüller-vertex ends go to cusps of M̄_{g_i,n_i}, but F_x(Q_0) ≅ Y_0 is interior. So the moving copy is a non-Teichmüller moving vertex. Entry 81 (Examples Z, Z′) shows that fixing the Teichmüller vertex does not pin such vertices or their puncture values.
- What TR does add is that every cusp of every piece has a t-independent j-component. This supplies the "fixed Teichmüller vertex" hypothesis that entry 81 assumes, rather than taking it as given.


### round5_q4 (verbatim): Lemma R*
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


### round6_q7 (verbatim): Theorem L
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
- Never assume V_t totally geodesic for t ≠ 0. The coarse reading (R2) is the run's default; any use of (R2^orb) must be flagged and kept separate from the general argument.
- A proof for a sub-class or under an extra hypothesis does not settle entry 82; report it as partial.
- Begin with a plan/status line. End with: proved / not proved / open.
