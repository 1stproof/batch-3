kind: attempt
Open question attempted: ledger entry 82, the run's open input (Rig). The main line derives the goal from (Rig) together with the missing statement MS8. Specifically, attempt (Rig), or its weak form (Rig-w) below, for every admissible family, OR decide the realisability question Q1 of round8_q9.

## Task
In the setting below (readings (R1), (R2)), prove one of the following for every admissible family:

**(Rig).** There is a finite set 𝒦 of triples (G, M, K), with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in its boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G).

or at least

**(Rig-w).** The puncture values f_u(p), for u ∈ M(E) and p a puncture of a piece E at time t, range over a finite set independent of t.

**The definitions:**
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w.
- ν: Ē → ∏M̄_w is the normalization of its closure.
- A *puncture* is a point p ∈ Ē with ν(p) ∉ ∏M_w. Put f_u = pr_u∘ν.
- M(E) := {u : f_u non-constant}.
- K(E) := the closure of the image of E in ∏_{u∈M(E)} M̄_u.

Alternatively, refute: realise an Example-Z′-type deformation, with a non-constant vertex whose interior puncture value moves, by an actual admissible family V_t deforming a smooth closed totally geodesic V_0 (all of (i), (ii), i.e. (R1), (R2)). Then say whether the same mechanism lets a constant boundary factor move, which would contradict the problem's claim.

**What is known** (below, verbatim):
- Every piece at t = 0 has a Teichmüller vertex (Theorem TV, R8-10).
- L2 (round7_q9 §2): under the orbifold-transport hypothesis (O_G), (Rig) holds for product strata.
- Lemma G (round7_q7 §2): (O) holds off a discrete set of times.
- round8_q9: the birational case under (Σ-fixed), and the Examples Z, Z′. These show that NO argument from piece-level data alone can prove (Rig) or (Rig-w): Teichmüller anchor, trivial source family, fixed punctures and (O) for the Teichmüller vertex are all insufficient.
- A proof must therefore use global input:
  - the 2-dimensional open part of V_t near the piece and its compatibility (ii) with all strata; or
  - the structure of the piece at t = 0 coming from total geodesy, transported in a way that survives t ≠ 0.

**Approaches not yet tried** (you may use others; say which you use):
1. **Normal-bundle / plumbing constraints along a piece.** These use the 2-dimensional neighbourhood of the piece in closure(V_t). See round8_q7 §4 (below): ratio functions s_e^{m_f}/s_f^{m_e} restrict to meromorphic sections of fixed line bundles on the normalised piece, with divisors supported at punctures and junctions. The normal bundle of a boundary divisor restricted to a piece involves f_u^* of cotangent lines at the half-edges of moving vertices. Can these constraints, together with Lemma P0 (which vertices degenerate at a puncture is t-invariant) and the orders m_e (topological), pin the moving vertices' maps, or at least their puncture values? Test the result against Examples Z and Z′: does Example Z′ violate such a constraint once it is required to bound a 2-dimensional V_t?
2. **The t = 0 structure from total geodesy.** By Theorem F2* and Corollary Φ̂ (R8-10), every vertex coordinate of a piece at t = 0, for vertices carrying a nonzero limit differential at some scale, is an "affine disc" g ↦ Y_w^{c_g η̄_w/|η_w|}. So the piece is the projection of an SL(2,R)-orbit of a multi-scale differential. Use this, with incidence data at junctions (which H_t transports) and the image-cycle route of round7_q7 §4, to constrain the deformations.
3. **Imayoshi–Shiga finiteness on the 2-dimensional family**, after showing (Σ-fixed)-type conditions from global data.

A proof for only some pieces, strata or V_0 does not settle entry 82; report it, labelled partial, if that is all you find. Begin with a plan/status line and end with: proved / not proved / open.

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
