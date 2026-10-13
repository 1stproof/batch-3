kind: attempt
Open question attempted: the run's open gap (F2) behind Lemma T′ (ledger entry 31, PROVED only "modulo the sketched fact (F2)"), which chain step 2 uses to give every boundary piece of closure(V_0) a Teichmüller vertex — a written check of Lemma T′ and a complete proof (or refutation) of (F2).

## Task
The run's chain toward the problem's claim uses, at its step 2, that every 1-dimensional boundary piece E of closure(V_0) (in every stratum Δ_G, on the lift ξ_G^{-1} for non-product G) has a Teichmüller vertex: a vertex v such that π_v∘ν, for a suitable orbifold structure on the normalization of E, lifts to an isometric equivariant embedding onto a Teichmüller disc. This comes from Lemma PA (positive area at a generic point; PR-H §1 below) and Lemma T′ (PR-F §2 below), which is proved only modulo a limit fact (F2) stated as a sketch in PR-F §0.
1. Check Lemma G/G′ and Lemma T′ of PR-F step by step, and say for each inference whether it is valid.
2. Prove (F2) in full — the affine transport of a positive-area component: for (X_n, q_n) ∈ V_0 converging to P with the vertex-v part of the rescaled differentials converging to an integrable η_v of positive area at scale 1, the v-component of every limit of g·(X_n,q_n) (g ∈ SL(2,R)) is the point g·(Y_v, η_v) of the Teichmüller disc, with the marking induced by the Teichmüller maps — or show precisely where it fails (e.g. area escaping into collars or to other vertices along g; non-uniformity in g; markings at orbifold points).
3. Check that the conclusion holds in the form chain step 2 needs: for EVERY piece (all strata, including non-product G on the lift, and pieces not meeting closure(∂V_0)), with an orbifold structure on the normalized piece for which the lift is an isometry onto a Teichmüller disc (state precisely which orbifold structure, and whether the map is orbifold-unramified).

Write all proofs in full; cite literature theorems (Masur's compactness criterion, Teichmüller's theorem, the multi-scale / Bainbridge–Chen–Gendron–Grushevsky–Möller compactification, Mumford compactness, etc.) by name with exact hypotheses, flagging those cited from memory. Begin with a plan/status line; end with proved / not proved / open.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G (including the open stratum M_g). Write H_t = H(·,t); one may assume H_0 = id. (This is our formalisation of "smoothly trivial" together with (i), (ii).)
- Notation: B_t := closure(V_t) \ V_t; a "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## Prior results (spliced verbatim from earlier answer files)

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



## Reminder
- V_0 is totally geodesic (every Teichmüller disc tangent to V_0 lies in V_0); V_t for t ≠ 0 plays no role in this task.
- Beware: limits of Teichmüller discs asserted to be Teichmüller discs without proof; "area leakage" into collars; markings at orbifold points.
