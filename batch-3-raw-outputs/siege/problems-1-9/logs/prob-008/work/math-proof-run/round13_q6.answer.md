# round13_q6 answer

## 0. Plan and statement attempted

Target: the statement (PE0) of the query file. The route has four steps: (a) check the data against Proposition MG; (b) put MG in extremality form; (c) prove non-extremality for a positive-entropy mu with a zero transverse exponent; (d) conclude.

Status, stated at the outset:
- (a) is done. The Pesin-block data satisfy MG once three routine choices are made (Section 1). MG also holds with w in L^1(m) (Lemma 1.1).
- (b) is done: a twisted Douglas lemma (Section 2).
- (c) is NOT achieved. Section 3 proves a measured, twisted "ladder" criterion for non-extremality. That criterion turns out to be no stronger than Theorem G / Corollary G3 (3x2 grids). Section 3 also explains why (c), for a non-hyperbolic mu, is the su-closing problem already isolated in R6-f, R7-a and R7-f, and why none of the tools listed in the route produces it.
- (d) therefore does not go through. **(PE0) remains open.** I could not build the counterexample the task asks for when the route fails (Section 4).

Conventions are those of the query file: nu, d = div_nu X, J_t, P phi = X phi + d phi, Gamma_t phi = e^{J_t} phi o g_t, and F_phi(t) = S(Gamma_t phi).

New results of this round, in brief:
- Lemma 1.1: MG with L^1 weights.
- Lemma 1.2: the Pesin–Egorov data meet MG.
- Lemma 2.1: twisted extremality.
- Proposition 3.2 (proved, modulo the standard Pesin facts listed in 1.2): under GH, for every Pesin–Egorov block of a (PE0)-type measure, fix any finite measure lambda; then the set of points reachable by su-walks through the block is lambda-null. This holds for all starting points of a local unstable plaque except countably many (the countable exceptional set depends on lambda). It is the non-volume analogue of Corollary T2(ii) of Block R12-a, and it is a necessary condition that any hypothetical (PE0)-measure must satisfy.

## 1. Step (a): the Pesin–Egorov data satisfy Proposition MG

### Lemma 1.1 (MG with integrable weights; proved)
Proposition MG (Block R8-f) remains true with "w in L^inf(m)" replaced by "w in L^1(m)".

*Proof.* Fix a xi^s-cell A and any a in A. The hypothesis int_A w(z) e^{beta^s(z,a)} dm_A(z) = 0 holds. Multiply it by the constant e^{J_t a} phi(g_t a) and subtract:
 int_A w e^{J_t} phi o g_t dm_A = int_A w(z) [ e^{J_t z} phi(g_t z) - e^{J_t a + beta^s(z,a)} phi(g_t a) ] dm_A(z).
The MG proof bounds the bracket, uniformly in z and a in A, by C_2 e^{-(theta-eta)t} ||phi||_{C^1}. This bound uses only (S), (R) at a, and |beta^s| <= K. Hence
 |int_A w e^{J_t} phi o g_t dm_A| <= C_2 e^{-(theta-eta)t} ||phi||_{C^1} int_A |w| dm_A.
Integrating over A against m^_s gives |F_phi(t)| <= C_2 ||w||_{L^1(m)} e^{-(theta-eta)t} ||phi||_{C^1} for t >= 0, where S = w m is a finite signed measure. The case t <= 0 is the same. Theorem J then gives S = 0, i.e. w = 0 m-a.e. ∎

The same proof also allows cell-dependent constants: C_A in (S) or (U), and C_a in (R) at the point a used for cell A. One only needs int |w| e^{C_a} (C_A + K_A e^{K_A}) dm < inf, where K_A = Lip(d) C_A/theta. I record this "tempered MG" but do not use it.

### Lemma 1.2 (the data; proved modulo standard Pesin theory, cited from memory)
Let mu be g_1-invariant and g_1-ergodic, with h_mu(g_1) > 0 and int J_1 dmu = 0. Let chi^+_min > 0 be the smallest positive exponent and chi^-_max < 0 the largest negative exponent (both exist by Ruelle's inequality for g_{+-1}). Fix 0 < theta < min(chi^+_min, |chi^-_max|) and 0 < eta < theta. Then there are a compact set K with mu(K) > 0, measurable partitions xi^s and xi^u of K, and m := mu|_K satisfying (S), (U) and (R) of MG with these theta and eta. Moreover:
 (i) every xi^s-cell is W^s_loc(z) ∩ K and every xi^u-cell is W^u_loc(z) ∩ K, for local Pesin plaques of a fixed size;
 (ii) each xi^s-cell meets each xi^u-cell in at most one point, so Pi := (pi_s, pi_u) is injective on K;
 (iii) for m-a.e. z the conditional measures m_{xi^u(z)} and m_{xi^s(z)} are non-atomic.

*Proof.*
1. *(R) by Egorov.* By Birkhoff for g_1 and g_{-1}, J_n(z)/n -> 0 as n -> +-inf for mu-a.e. z (as in R9-a, Step 2). Egorov gives a compact K_0 with mu(K_0) > 1 - eps on which the convergence is uniform. So there is N with |J_n(z)| <= eta|n| for |n| >= N and z in K_0. For |n| < N we have |J_n| <= N||d||_inf, and |J_t - J_{floor t}| <= ||d||_inf. Hence J_t(z) <= C + eta|t| for all real t and z in K_0. This is (R) with C := (N+1)||d||_inf.
2. *Pesin block.* Cited (Pesin theory for the C^inf diffeomorphism g_1 and ergodic mu, zero exponents allowed; e.g. Barreira–Pesin, from memory). There are compact Pesin blocks Lambda_l with mu(Lambda_l) -> 1. On each block, local stable and unstable manifolds W^s_r(z), W^u_r(z) of a uniform size r = r_l are embedded C^1 discs depending continuously on z in Lambda_l in the C^1 topology. For y, y' in W^s_r(z) and n >= 0, d(g_n y, g_n y') <= C_l e^{-theta n}. This holds because the block may be built with any contraction rate below |chi^-_max|, and theta < |chi^-_max|. Likewise, for y, y' in W^u_r(z) and n >= 0, d(g_{-n} y, g_{-n} y') <= C_l e^{-theta n}. Interpolating to real times with L' = max_{|s|<=1} Lip(g_s) gives (S) and (U) with a uniform constant.
3. *Localisation.* Pick a density point x0 of Lambda_l ∩ K_0 and a small ball B = B(x0, rho) with rho << r. Put K := Lambda_l ∩ K_0 ∩ closedball(x0, rho). It is compact, and mu(K) > 0 because x0 is a density point. For z in K, the plaques W^s_r(z) meet B in graphs over the E^s(x0)-disc, with uniformly small slope. Two such plaques through points of K either coincide in B or are disjoint there (cited, standard in Pesin theory: uniqueness of local stable manifolds at a fixed scale on a block). So z ~ z' iff z' is in W^s_r(z) is an equivalence relation on K. Its graph is closed, by continuity of the plaques. The quotient of a compact metric space by a closed equivalence relation is compact metrizable, so the partition xi^s is measurable (Rokhlin). The same holds for xi^u. This gives (i).
4. *(ii).* A C^1 graph over the E^s-disc and a C^1 graph over the E^u-disc, both of small slope, with E^s(x0) ∩ E^u(x0) = 0, meet in at most one point. The angle between E^s and E^u is bounded below on Lambda_l.
5. *(iii).* Cited (Ledrappier–Young I, from memory): the unstable conditional measures of mu are defined, up to normalisation, as Radon measures mu^u_z on W^u(z). Let U := union of the plaques W^u_r(z), z in K, partitioned into these plaques. This partition is measurable and subordinate to W^u, so its conditionals are the normalised restrictions of mu^u_z to the plaques. Restricting mu|_U to K restricts the conditionals: the conditional of m on the cell W^u_r(z) ∩ K is mu^u_z(· ∩ K ∩ W^u_r(z)) divided by its mass. The mass is positive for m-a.e. z. Indeed, the set Q of z whose plaque has zero conditional mass on K is saturated, so m(Q) = int mu^U_z(K ∩ Q) dmu = 0. The mu^u_z have no atoms by Lemma 6.0 (R6-a, re-proved in R9-a §2 for g_1-ergodic mu), transported to the Ledrappier–Young leaf measures. Hence the cell conditionals are non-atomic. The stable side is Lemma 6.0 for g_{-1}, using h_mu(g_{-1}) = h_mu(g_1) > 0. ∎

*Twists.* For z, z' in one xi^s-cell, beta^s(z,z') = lim_{t->+inf}(J_t z - J_t z') exists, and |beta^s| <= K := Lip(d) C/theta, exactly as in MG. So the twisted equations of MG are well defined. **Answer to (a): the data satisfy MG exactly. No extra hypothesis is needed beyond the three routine choices: Egorov set, Pesin block, and a small ball.** The Jacobian twists enter only through the bounded cocycles beta^s and beta^u.

## 2. Step (b): extremality form, with twists

Setting: (K, m, xi^s, xi^u) as in MG (or as in Lemma 1.2), with pi_s : K -> Omega_s := K/xi^s and pi_u : K -> Omega_u := K/xi^u. Define, without any measurable selection,
 rho_s(z) := int_{A} e^{beta^s(z,a)} dm_A(a)  (A = xi^s(z)),  rho_u(z) := int_{B} e^{beta^u(z,b)} dm_B(b)  (B = xi^u(z)).
By the cocycle rule, rho_s(z) = e^{beta^s(z,a0)} c_A for any a0 in A, with a constant c_A > 0. Also e^{-2K} <= rho_s, rho_u <= e^{2K}. Hence the MG hypothesis on w is equivalent to
 (H)  E_m[rho_s w | xi^s] = 0 and E_m[rho_u w | xi^u] = 0.

Let Gamma be the convex set of finite positive Borel measures gamma on K with
 (pi_s)_*(rho_s gamma) = (pi_s)_*(rho_s m) and (pi_u)_*(rho_u gamma) = (pi_u)_*(rho_u m).
These are the "twisted couplings": in the volume case rho = 1, and Gamma is the set of measures on K with the same s- and u-marginals as m. When Pi is injective, Gamma is the set of couplings of m^_s, m^_u carried by Pi(K), as in Block R12-e.

### Lemma 2.1 (twisted Douglas lemma; proved)
(1) There is a nonzero w in L^inf(m) satisfying (H) iff m is not an extreme point of Gamma.
(2) There is a nonzero w in L^1(m) satisfying (H) iff the linear space V := { rho_s (f o pi_s) + rho_u (g o pi_u) : f, g bounded Borel } is not weak*-dense in L^inf(m).
Consequently, under GH (MG plus Lemma 1.1), for every data set as in Lemma 1.2, m is an extreme point of Gamma and V is weak*-dense in L^inf(m).

*Proof.* (1) Suppose w != 0 is bounded and satisfies (H). Normalise so that ||w||_inf <= 1. Then gamma_± := (1 ± w) m are positive. They lie in Gamma because the constraints are linear and w m satisfies their homogeneous form: (pi_s)_*(rho_s w m) = 0 is the statement that E_m[rho_s w | xi^s] = 0, and likewise for u. So m = (gamma_+ + gamma_-)/2 with gamma_+ != gamma_-, and m is not extreme.
Conversely, suppose m = (gamma_1 + gamma_2)/2 with gamma_i in Gamma and gamma_1 != gamma_2. Then 0 <= gamma_i <= 2m, so gamma_1 = h m with 0 <= h <= 2. Put w := h - 1. It is bounded, and nonzero because gamma_1 != m. Subtracting the constraint for m from that for gamma_1 gives (pi_s)_*(rho_s w m) = 0 and (pi_u)_*(rho_u w m) = 0, which is (H).
(2) w in L^1(m) annihilates V for the L^1–L^inf pairing iff int w rho_s (f o pi_s) dm = 0 for all bounded f and the same for u. That is, iff (H) holds. By Hahn–Banach for the weak* topology, V has a nonzero annihilator in L^1 iff V is not weak*-dense.
The last sentence restates MG (in the L^1 form of Lemma 1.1) through (1) and (2). ∎

In the volume case Lemma 2.1(1) is Lemma 2.1 of R12-e. The twisted version shows that **the Jacobian cocycles change only the constraint set, not the logic**: extremality of m in Gamma is exactly what GH forces. I do not claim a twisted analogue of the cited Lindenstrauss criterion ("extreme implies singular to the product of the marginals"). Even granted, it would be useless in the non-hyperbolic case, for the reason given in R12-e: there the coupling is automatically singular. A usable twisted substitute for local product structure is Remark 3.1 below.

## 3. Step (c): what can be proved

### Remark 3.1 (twisted ladders reduce to Corollary G3)
In MG the measure m is arbitrary, so measured "ladders" can be built directly. Take a set E inside one xi^s-cell, carrying a non-atomic measure m_1, and a Borel injection h from E into a second s-cell, with y and h(y) uniformly backward-asymptotic. The u-cells are the pairs {y, h(y)}.
- The u-equations give w(h y) = -w(y) e^{-beta^u(hy, y)}.
- The two s-equations are then two bounded linear functionals of w|_E in L^inf(m_1). That space is infinite-dimensional, so a nonzero solution exists.
- **So Jacobian twists are never an obstruction once one s-cell carries at least 3 points joined by u-legs to a second s-cell.** But that configuration already contains the 3x2 grid of Corollary G3 (R7-a). The measured version therefore adds nothing beyond finite configurations: in every construction I could find, non-extremality comes from finitely many points forming cycles in the su-graph.

### Proposition 3.2 (su-reachable sets are null; proved modulo the Pesin facts of Lemma 1.2)
*Setting.*
- K is a compact set with plaques W^s_r(z), W^u_r(z), z in K, depending continuously on z.
- (S) and (U) hold uniformly at rate theta along plaques.
- (R) holds on K with eta < theta.
- Example: Lambda_l ∩ K_0 from Lemma 1.2, steps 1-2.

*Definitions.*
- For z in K and j >= 1, a K-walk of length j from z is a sequence (y_0 = z, y_1, ..., y_j) of points of K with y_{i+1} != y_i, where y_{i+1} lies in W^s_r(y_i) for i even and in W^u_r(y_i) for i odd.
- R_j(z) is the set of endpoints y_j of such walks.
- The set of K-walks is the intersection of a compact subset of M^{j+1} (closed by continuity of the plaques) with an open set. So it is sigma-compact, and R_j(z) is a sigma-compact (hence Borel) set.

*Statement.* Assume GH. Let x0 be in K, j >= 1, and lambda a finite Borel measure on M. Then the set of z in (W^u_r(x0) ∩ K) \ {x0} with lambda(R_j(z)) > 0 is countable.

*Proof.*
1. *Four walks with a common end.* Suppose the set is uncountable. Then for some delta > 0 there are infinitely many distinct such z_1, z_2, ... with lambda(R_j(z_i)) >= delta. Take N > 3 lambda(M)/delta. Then int sum_{i<=N} 1_{R_j(z_i)} dlambda >= N delta > 3 lambda(M), so some point y lies in four of the sets, say R_j(z_{i_1}), ..., R_j(z_{i_4}). Choose K-walks (z_{i_r}, y^r_1, ..., y^r_j = y). Prefix x0 to get four sequences
 omega^r = (x0, z_{i_r}, y^r_1, ..., y^r_j = y), r = 1..4.
 They are pairwise distinct, since their second entries differ. Consecutive entries are distinct, and all entries lie in K.
2. *Classes.* Let x ~_s^theta x' mean d(g_t x, g_t x') <= C e^{-theta t} for t >= 0, for some C. Define ~_u^theta with t <= 0. Both are equivalence relations: for transitivity, add the constants; the rate stays theta. Let Z be the finite set of all points occurring in the four sequences. Let Gamma' be the bipartite multigraph whose vertices are the ~_s^theta-classes and ~_u^theta-classes of points of Z, and whose edges are the points of Z, each joining its two classes. Gamma' has no loops.
3. *Walks in Gamma'.* Each leg of omega^r is a plaque leg at rate theta. So consecutive entries share their u-class (x0 and z, then y_1 and y_2, ...) and their s-class (z and y_1, ...), alternately. Hence omega^r is a walk in Gamma' with edges x0, z_{i_r}, y^r_1, ..., y. It runs from the vertex S(x0) to the class of y of the type not shared with y^r_{j-1}. That type depends only on the parity of j, so all four walks have the same end vertex and the same length j+2. The walks are non-backtracking (consecutive edges are distinct points) and pairwise distinct. Gamma', the union of their edges and end vertices, is connected, since every walk contains the edge x0.
4. *Cyclomatic number.* By Lemma W of R8-f (at most 3 non-backtracking walks of given length between two vertices when the cyclomatic number is <= 1), Gamma' has #edges >= #vertices + 1. That is, |Z| > p + q, where p and q are the numbers of s- and u-classes of points of Z.
5. *Theorem G.* Give each class a representative in K. Every class of a point of Z contains a point of K, because all points of Z are in K. Within a class, all pairs are theta-asymptotic on the relevant half-line with finitely many constants, so (S) and (U) of Theorem G (R7-a) hold with one constant C. (R) holds at the representatives because they lie in K. Since |Z| > p + q, the linear system (G) has a nonzero solution (item (a) of R7-a, valid for arbitrary Jacobian constants). Theorem G, which assumes GH, gives a contradiction. ∎

**Corollary 3.3 (proved, same citations).** Assume GH. Let mu be g_1-ergodic with h_mu(g_1) > 0 and int J_1 dmu = 0, and let K = Lambda_l ∩ K_0 be as in Lemma 1.2. Then for mu-a.e. x0 in K, for mu^u_{x0}-a.e. z in W^u_r(x0) ∩ K and every j >= 1: mu(R_j(z)) = 0, and indeed lambda(R_j(z)) = 0 for any fixed finite lambda (for instance lambda = nu). The analogous statement holds with u and s exchanged (apply it to -X, which is GH by (O4)).
*Proof.* Apply Proposition 3.2 for each j, with lambda = mu (resp. lambda = nu). The exceptional set of z is countable, hence null for the non-atomic conditional mu^u_{x0} (Lemma 1.2(iii)). ∎

*Meaning.* For a (PE0)-type measure under GH, the su-accessibility sets generated through a Pesin–Egorov block are null for mu and for Lebesgue, from almost every starting point. In the volume case this was known in a stronger form: Corollary T2(ii) of Block R12-a says that under GH every full su-class is omega-null. Proposition 3.2 is the version without a volume, with Jacobian twists absorbed by Theorem G's counting.
- It does not contradict positive entropy. In the non-GH model "Anosov flow x Diophantine translation" (Section 3 of Block R12-c), the su-classes are the slices N x {theta}, which are mu-null as well.
- In that model step (c) holds: take w(x, theta) = w_0(x) 1_I(theta), with w_0 a base function whose conditional means on base s- and u-plaques vanish. Such a w_0 exists by local product structure of the hyperbolic base measure, as in Corollary G3. The model is a reminder that (c) and "null su-classes" are compatible. What GH forbids, through Theorem G, is the cycle that makes w_0 possible, not the size of the classes.

### 3.4 Where (c) stops
By Lemma 2.1, (c) asks for a bounded w satisfying (H), i.e. for non-extremality of m in Gamma.
- In every mechanism I know, a nonzero w is produced by cycles of the su-graph. These are finitely many points, or measured ladders, which contain finite cycles (Remark 3.1); or open/Lipschitz families of walks with non-degenerate Jacobian (Theorem U, Example 2.3 of R12-e).
- For a non-hyperbolic mu (centre of dimension c - 1 >= 1 besides the flow), finite cycles need closing conditions in the centre direction. The families of walks through a Pesin block are parametrised by fractal sets and depend only Hölder-continuously on earlier legs. Neither invariance of domain/Hurewicz (topological dimension 0) nor the coarea formula (no Lipschitz bound, no a.e. Jacobian) applies. Even for Lipschitz walk maps with Jacobian 0 a.e., the C^1 Sard theorem fails in dimension D > n (Whitney's example), so no measure-theoretic shortcut is available. Proposition 3.2 converts the cycle problem into a measure-theoretic accessibility property: su-reachable sets of positive lambda-measure from uncountably many starting points. But positive entropy alone does not give that property: it fails in the non-GH product models, where su-classes are null slices. So it would have to be proved from GH, and I see no way to do so.
- So (c) for non-hyperbolic mu requires an input that produces exact (possibly long) su-cycles through a Pesin block. Nothing in the route's toolbox supplies it: non-atomic conditionals (Lemma 6.0), Ledrappier–Young conditionals, leafwise normal forms (R11-a), derivatives along leaves (Example 2.3), or the conditional-independence criterion (R12-e §3).

## 4. Step (d) and the counterexample question

- (d) is not reached, because (c) is not proved. With (a), (b) and Lemma 1.1, the route is: **(PE0) <= [for some Pesin–Egorov data of mu, m is not extreme in the twisted coupling set Gamma]**. That implication is proved here: Lemma 1.2 + Lemma 2.1 + MG.
- *Counterexample to the route.* The task asks, if the route cannot work, for a flow (GH or not) with a positive-entropy measure, a zero transverse exponent and (R), whose data are extreme for every choice of (K, m, xi^s, xi^u). I could not construct one.
  - The natural non-GH models (Anosov x Diophantine translation, skew products over hyperbolic bases, suspensions of A x R_alpha) all satisfy (c), via a function lifted from the hyperbolic factor (see "Meaning" after Corollary 3.3).
  - So they do not show that the route fails.
  - Any counterexample would need a positive-entropy measure whose su-graph through every Pesin block is free of cycles, even in the measured sense.
- So I cannot say that the route fails; I can only say exactly where it stops: step (c), in the form (C*) below.

## 5. Summary: proved / sketched / open

**Proved (given the cited standard facts: Pesin local manifolds on blocks, Ledrappier–Young leaf conditionals, Lemma 6.0, Theorem J, Theorem G, Lemma W):**
1. Lemma 1.1: Proposition MG holds for w in L^1(m), and also with tempered constants.
2. Lemma 1.2: the Pesin–Egorov data of a g_1-ergodic mu with h_mu > 0 and int J_1 dmu = 0 satisfy MG exactly. Cells are local plaques ∩ K, Pi is injective, and cell conditionals are non-atomic. This answers (a): no extra hypothesis is needed.
3. Lemma 2.1: twisted Douglas lemma. A nonzero bounded w exists iff m is not extreme in the twisted coupling set Gamma. A nonzero L^1 w exists iff V is not weak*-dense. Under GH, m is always extreme and V weak*-dense. This answers (b).
4. Remark 3.1: twisted measured ladders give w, but they contain 3x2 grids, so they reduce to Corollary G3. Twists are never the obstruction.
5. Proposition 3.2 and Corollary 3.3 (new; general case, no volume): under GH, su-reachable sets through a Pesin–Egorov block are lambda-null for any fixed finite lambda, from all but countably many points of any local unstable plaque. In particular they are mu-null and Lebesgue-null from mu-a.e. point. This is a necessary condition on any (PE0)-measure. It extends Corollary T2(ii) (volume case) to the general case.

**Not proved / open:**
- (C*) [the missing step (c), precise form] For a g_1-ergodic mu with h_mu(g_1) > 0, int J_1 dmu = 0, and a zero exponent transverse to X: there are data (K, m, xi^s, xi^u) as in Lemma 1.2, or any data satisfying MG's hypotheses, for which m is not an extreme point of the twisted coupling set Gamma. By Corollary 3.3 the needed cycles must live inside null su-reachable sets. Open; it implies (PE0) and hence the problem.
- Whether non-extremality of su-couplings of Pesin data can come from "infinitary" (measured, non-finite) cycles when no finite su-cycle exists. Open; I know no example either way.
- A counterexample to the route (§4). Open.
- **(PE0) itself remains open**, and so does the problem in dimension >= 4 along this chain. Proved earlier in the chain: dim M <= 3, and hyperbolic measures.

=== END OF ANSWER round13_q6 ===

