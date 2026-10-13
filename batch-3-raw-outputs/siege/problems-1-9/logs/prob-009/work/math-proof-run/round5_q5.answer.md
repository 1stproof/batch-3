# round5_q5 — attempt on (T0)

## Plan / status line (updated as I go)
Goal: (T0). I do not expect to settle (T0) in full. Plan:
1. Prove a qc-stability lemma (Lemma G): GL(2,R)-moves of generating differentials keep boundary limits in the same stratum.
2. Prove (Lemma T') that whenever a vertex v carries a *positive-area* limit of generating differentials at a point of a 1-dim boundary piece E, then pi_v maps (the irreducible component of) E, orbifold-unramified, onto a Teichmüller curve. This supplies exactly the isometry property demanded in (T0)(a),(b), and the unramifiedness that Lemma R tacitly needs.
3. Consequences: vertex i never carries positive area (Lemma V); cusp existence (c) whenever some vertex carries positive area (Prop. C).
4. Reduce (T0) to an explicit residual statement (T0*) and check the covering-construction model.

---

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

---

## 7. Summary

**Proved here (modulo the cited facts (Nbhd), (Ext), Royden, Masur's cylinder theorem, Veech/Teichmüller-curve basics, and the limit facts (F), (F2), of which (F2) is only sketched):**
- Lemma G / G′: GL(2,R)-moves of generating pairs keep boundary limits in the same stratum; limits along a sequence give a continuous map phi: H -> closure(V_0) ∩ Delta_G.
- Lemma T′: if a vertex v carries positive area at one point of a boundary piece, then pi_v maps that piece's irreducible component (orbifold-)unramified onto a Teichmüller curve, generated by the limiting quadratic differential. So its universal-cover lift is an isometry onto a Teichmüller disc, which is exactly the property used by Lemma R, and the piece is non-compact. This also repairs a tacit assumption of Lemma R: unramifiedness, which Lemma R needs and which (T0)(a) as worded asserts.
- Lemma V: the constant vertex i never carries positive area along ∂V_0.
- Prop. C: under (PA), (T0)(c) holds.
- Prop. 4.1: (T0\*) ⇒ (T0)(a),(c); (T0\*\*) ⇒ (T0)(b).
- Prop. 5.1: (T0) (in the form (a)+(c), at every cusp) for covering loci over M_{0,5} with all preimages of branch points marked, including the task's example in M_{0,3d+2}. This is **partial**: it covers only some V_0, and it does not cover covering loci in M_g without marked points (Section 5 caveat).

**Not proved / open:**
- (PA): some vertex carries positive area for some generating sequence at some point of ∂V_0.
- (T0\*) in general: a cusp with a merge branch whose merged vertex carries positive area. Section 6 sketches a Jenkins–Strebel-ray route with gaps (a)–(d).
- The unmarked covering-construction case (contracted bridges may pinch the vertex-i edges on both branches at a cusp).
- (T0) itself is neither proved nor refuted. I found no totally geodesic V_0 for which it fails.
- The full proof of (F2), and the infinite-area rigidity remark of Section 3.

=== END OF ANSWER round5_q5 ===
