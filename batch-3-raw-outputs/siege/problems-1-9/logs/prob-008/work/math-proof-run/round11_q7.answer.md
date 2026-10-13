# round11_q7 answer

## 0. Status (read first)

- **(AP) is NOT proved here, and no counterexample is given.** Hence the goal (zero topological entropy for GH flows in every dimension) is not reached on this route.
- I worked the suggested approach: closed range and tame inverse of X, applied at the level of one pair with the UNWEIGHTED transport. It yields three rigorous results that are new relative to the brief, plus a precise account of where it stops.
  1. **Proposition 1 (tower of primitives; sector flatness).** Assume GH together with a smooth invariant volume (V). Let x != y be a pair satisfying only (a) of (AP). For every smooth phi, the eigen-family T_z(phi) = int e^{-zt}(phi(g_t x) - phi(g_t y)) dt (0 < Re z < theta) satisfies
     |T_z(phi)| <= |z|^j ( 2||X^{-j}phi_0||_inf / Re z + C theta^{-j} ||phi||_{C^1} / (theta - Re z) ) for every j.
     So T_z(phi) is flat at z = 0 inside every sector |Im z| <= K Re z.
  2. **Proposition 2 (quantitative obstruction).** Under (V), an (AP)-pair forces liminf_j ||X^{-j}(phi - omega(phi))||_inf^{1/j} = infinity for EVERY smooth phi with phi(g_t x) != phi(g_t y) for some t. Consequently (Corollary 2.1), (AP) holds in the volume case as soon as the smooth functions whose iterated X-primitives grow at most geometrically separate points. A Gevrey-type strengthening (growth A^j (j!)^s with s < 1 already suffices) is only sketched.
  3. **Lemma V (spectral).** Under GH + (V), no nonzero smooth mean-zero h has an autocorrelation <h o g_t, h> that decays exponentially, or even at a quasi-analytic rate, as t -> +inf (one side suffices). This is stronger than Theorem J for densities S = h omega: it needs decay only for the single test function h and only in one time direction.
- **Where it stops (Section 4).** Under (V), everything that the facts (i)-(vi) and (c) say about a single pair is captured by the scalar functions F_phi(t) = phi(g_t x) - phi(g_t y). These are bounded, exponentially small as t -> -inf, and all their iterated primitives from -inf are bounded. I give reasons (not a proof) to believe that such scalar data are consistent. A contradiction needs either "band-limited" smooth functions (Prop. 2) or exponential mixing of some smooth observable (Lemma V). Neither is available from GH plus positive entropy. The non-volume case adds the further obstruction that R is not X^{-1}-stable.

Conventions as in the brief: nu is a smooth positive density, d = div_nu X, J_t is the log-Jacobian, R = X(C^inf), I is the set of invariant distribution densities, and S_0 = delta_x - delta_y. "(V)" means that X preserves a smooth positive density omega. Under GH this gives (fact (iv), (O2)) a minimal, uniquely ergodic flow such that every omega-mean-zero smooth f equals Xu with u smooth and omega-mean-zero. Write X^{-1}f for this u. Under (V) we take nu = omega, so d = 0 and J = 0. Then every point is Birkhoff-regular with lambda = 0, every point is bi-recurrent (by minimality), and **(AP) in the volume case says exactly: there is no pair x != y with dist(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0.**

## 1. Proposition 1 (tower of primitives; flatness in sectors)

**Proposition 1.** Assume GH and (V). Let x != y satisfy (a): dist(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0. For smooth phi put F_phi(t) = phi(g_t x) - phi(g_t y), phi_0 = phi - omega(phi), U_0 = phi_0 and U_j = X^{-j} phi_0 (all smooth and mean-zero). Then:
 (1) G_j(t) := int_{-inf}^t ((t-s)^{j-1}/(j-1)!) F_phi(s) ds (the j-fold primitive of F_phi vanishing at -inf) equals U_j(g_t x) - U_j(g_t y) for every real t and every j >= 1. In particular |G_j(t)| <= 2||U_j||_inf on R, and |G_j(t)| <= C theta^{-j} ||dphi||_inf e^{-theta|t|} for t <= 0.
 (2) For 0 < Re z < theta, T_z(phi) := int_R e^{-zt} F_phi(t) dt converges absolutely, is holomorphic in z, satisfies T_z(X phi) = z T_z(phi), and for every j >= 0:
   T_z(phi) = z^j int_R e^{-zt} G_j(t) dt,
   |T_z(phi)| <= |z|^j ( 2||U_j||_inf / Re z + C theta^{-j} ||dphi||_inf / (theta - Re z) ).
 (3) In each sector Sigma_K = {z : |Im z| <= K Re z, 0 < |z| < theta/2}, T_z(phi) = O_{j,K,phi}(|z|^{j-1}) for every j.

*Proof.*
(1) For t <= 0: |F_phi(t)| <= ||dphi||_inf dist(g_t x, g_t y) <= C||dphi||_inf e^{-theta|t|}. So the primitives exist, and
 |G_j(t)| <= C||dphi|| int_0^inf (r^{j-1}/(j-1)!) e^{-theta(|t|+r)} dr = C||dphi|| theta^{-j} e^{-theta|t|} for t <= 0.
Put H_j(t) := U_j(g_t x) - U_j(g_t y). Then H_j'(t) = (XU_j)(g_t x) - (XU_j)(g_t y) = H_{j-1}(t), and H_0 = F_phi, because the constant omega(phi) cancels. Also H_j(t) -> 0 as t -> -inf, since U_j is Lipschitz and the pair is asymptotic. Induction: G_j and H_j have the same derivative G_{j-1} = H_{j-1}, and both tend to 0 at -inf, so G_j = H_j.
(2) Absolute convergence: |F_phi| <= 2||phi||_inf for t >= 0, and the bound above holds for t <= 0. Holomorphy follows by dominated convergence on compact sub-strips.
The eigen-relation: F_{X phi} = F_phi', and integration by parts has vanishing boundary terms, because F_phi is bounded at +inf and O(e^{-theta|t|}) at -inf while |e^{-zt}| = e^{Re z |t|} there with Re z < theta.
The tower: integrate by parts j times, using G_i' = G_{i-1}. The boundary terms [e^{-zt} G_i(t)] vanish at +inf, since G_i is bounded by (1) and Re z > 0. They vanish at -inf, since |G_i(t)| <= C' e^{-theta|t|} and Re z < theta. The bound splits the integral at t = 0.
(3) On Sigma_K, 1/Re z <= sqrt(1+K^2)/|z| and theta - Re z >= theta/2. ∎

*Remarks.* (i) Only (a) and (V) are used, not (c). Recurrence is automatic under (V) anyway (minimality). (ii) Under (V), Proposition 1 contains everything that facts (i), (iii), (v), (vi) of the brief give for the pair. (iii) Without (V), (2)-(3) remain true for phi in R_inf := {f : X^{-j} f exists in C^inf for all j}, with U_j := X^{-j} f. (Boundedness of G_j then comes from fact (iii), since U_{j-1} = X U_j lies in R.) But R_inf need not separate points, so nothing is gained for the non-volume case.

## 2. Proposition 2 (quantitative obstruction in the volume case)

**Proposition 2.** Assume GH and (V), and let x != y satisfy (a). Let phi be smooth with F_phi not identically 0, i.e. phi(g_t x) != phi(g_t y) for some t. Then
 liminf_{j -> inf} ||X^{-j}(phi - omega(phi))||_inf^{1/j} = +infinity.

*Proof.* Suppose that ||U_j||_inf <= A^j for infinitely many j. Fix K = 1 and z in Sigma_1 with |z| < r := min(1/A, theta)/2. Proposition 1(2) along those j gives
 |T_z(phi)| <= (|z|A)^j 2 sqrt2/|z| + (|z|/theta)^j 2C||dphi||/theta -> 0.
So T_z(phi) = 0 on the nonempty open set Sigma_1 ∩ {|z| < r}. By the identity theorem it vanishes on the whole (connected) strip 0 < Re z < theta, in particular on the line Re z = theta/2. The function t -> e^{-theta t/2} F_phi(t) is continuous and in L^1(R), and its Fourier transform, xi -> T_{theta/2 + i xi}(phi), is identically 0. By Fourier uniqueness, F_phi = 0: a contradiction. ∎

**Corollary 2.1 (conditional form of (AP), volume case).** Under GH + (V), let B be the set of smooth phi with liminf_j ||X^{-j}(phi - omega(phi))||_inf^{1/j} < inf. If B separates points of M, then there is no pair x != y with backward exponential asymptoticity (a), so (AP) holds.
*Proof.* Pick phi in B with phi(x) != phi(y). Then F_phi(0) != 0, which contradicts Proposition 2. ∎
Examples: on a Diophantine torus the trigonometric polynomials lie in B. A smooth eigenfunction e (Xe = i xi e, xi != 0) lies in B. (For such e the conclusion is elementary anyway: |e(g_t x) - e(g_t y)| = |e(x) - e(y)| is constant in t.) Corollary 2.1 is a quantitative generalisation of "continuous eigenfunctions separate points ⇒ no asymptotic pairs".

**Remark 2.2 (Gevrey strengthening; sketch only, not checked in detail).** Suppose only ||U_j||_inf <= C A^j (j!)^s along all j, with some s < 1. Optimising j in Proposition 1(2) gives |T_z(phi)| <= C_eps exp(-c|z|^{-1/s}) in the sector |arg z| < pi/2 - eps. In w = 1/z this is a function on a sector of opening pi - 2eps that decays like exp(-c|w|^{1/s}). Choose eps with pi/(pi - 2eps) < 1/s. The Phragmen-Lindelof theorem (cited from memory: a bounded holomorphic function on a sector of opening alpha that is O(exp(-c|w|^beta)) there with beta > pi/alpha vanishes identically) then gives T_z(phi) = 0, and the proof of Proposition 2 finishes. For s >= 1 the method gives nothing, because e^{-1/z} is flat in every sector of the half-plane. On Diophantine tori, real-analytic phi typically give s = tau (the Diophantine exponent) >= 1, so B (not its Gevrey enlargement) is the relevant class there.

## 3. Lemma V (spectral form of Theorem J in the volume case)

**Lemma V.** Assume GH and (V). Let h be smooth, real, with omega(h) = 0, and let c(t) = int h(g_t p) h(p) d omega(p). Suppose |c(t)| <= C e^{-w(t)} for t >= 0, where w >= 0 is measurable and M_j := int_0^inf t^j e^{-w(t)} dt < inf for all j, with sum_j M_j^{-1/j} = inf. (For example w(t) = eps t, or w(t) = t/log(e+t).) Then h = 0.

*Proof.*
1. U_t f = f o g_t is a strongly continuous unitary group on L^2(omega), since omega is invariant. Let A be its skew-adjoint generator (Stone). On smooth f, A f = Xf. Let sigma_h be the spectral measure of h: c(t) = <U_t h, h> = int e^{it xi} d sigma_h(xi). Since h is real and omega invariant, c(-t) = <h, U_t h> = c(t) (real). So the bound holds for all real t.
2. By GH + (V), h = X a_1 with a_1 smooth and mean-zero, and inductively h = X^n a_n = A^n a_n. In the spectral representation A is multiplication by i xi, so d sigma_h = xi^{2n} d sigma_{a_n}. Hence int xi^{-2n} d sigma_h = ||a_n||^2 < inf for every n, and sigma_h({0}) = 0.
3. Since c is in L^1(R), sigma_h is absolutely continuous with continuous density p(xi) = (2 pi)^{-1} int e^{-it xi} c(t) dt >= 0. Then p is C^inf with |p^{(j)}| <= (2 pi)^{-1} 2C M_j.
4. All derivatives of p vanish at 0. Otherwise let k be the first index with p^{(k)}(0) != 0. Then p(xi) >= c_0 |xi|^k near 0 with c_0 > 0 (p >= 0 forces k even and p^{(k)}(0) > 0), and int xi^{-2n} p dxi = inf for 2n >= k+1. This contradicts step 2.
5. The sequence (M_j) is log-convex, and sum M_j^{-1/j} = inf. The Denjoy-Carleman theorem (cited from memory, e.g. Rudin, Real and Complex Analysis, Thm 19.11, after normalising M_0 as in Theorem J* of the brief) says the class is quasi-analytic. So p = 0. Hence sigma_h = 0 and ||h||^2 = c(0) = 0. ∎

*Comments.*
- Compared with Theorem J applied to S = h omega, Lemma V needs decay only of the single correlation <h o g_t, h>, and only for t -> +inf. It uses GH only through cohomology-freeness, i.e. through all the iterated primitives X^{-n} h.
- **Consequence:** a GH flow with a smooth invariant volume is not exponentially (or quasi-analytically) mixing for any nonzero smooth observable.
- **Why it does not settle (AP).** One would need a smooth h with fast-decaying autocorrelation. Averaging Dirac pairs (x, y(x)) over a smooth measure produces densities that are not smooth: Pesin manifolds depend only measurably on the point. If h is only in a Sobolev space H^K, step 2 gives finitely many vanishing moments only, which is no contradiction for an analytic p. Positive entropy does not provide exponential mixing in general.

## 4. Where the closed-range approach stops (dead ends, with reasons)

4.1. **What the closed range gives at the pair level is exhausted by Proposition 1.** Under (V), the dual solutions of S o X = S_0 (fact (ii)) are, modulo I = R omega, the distributions Q_j(phi) = int_{-inf}^0 (|t|^{j-1}/(j-1)!) S_0(phi o g_t) dt, and Q_j(phi o g_s) = G_j(s). The bounded Birkhoff integrals (fact (iii)) say exactly that each G_j is bounded on R. Recurrence (c) adds nothing under (V), because it holds for every point. The weighted and unweighted transports coincide (J = 0). So the information on the pair available from (i)-(vi) and (c) is: for every smooth phi, F_phi is bounded, F_phi = O(e^{-theta|t|}) as t -> -inf (with a C^1 bound), F_{X phi} = F_phi', F_{phi o g_s} = F_phi(. + s), and all primitives G_j are bounded with bounds 2||X^{-j} phi_0||_inf.

4.2. **The scalar data appear consistent.** Proposition 1(3) says that z -> T_z(phi) is flat at 0 in sectors. Flatness in sectors of a half-plane does not force vanishing: e^{-1/z} is flat in every sector |arg z| <= pi/2 - eps. A contradiction needs quantitative control of the constants, i.e. of ||X^{-j} phi_0||_inf (Prop. 2, Remark 2.2). I tried to manufacture such control by smoothing along the flow: phi = int rho(t) psi o g_t dt with rho-hat supported in a <= |xi| <= b. This gives ||X^{-j} phi_0||_inf <= ||rho_j||_{L^1} ||psi||_inf <= C j^2 a^{-j}, which is geometric. But two things fail:
  - phi is then only continuous: rho is not exponentially decaying, while ||psi o g_t||_{C^k} grows exponentially.
  - More decisively, F_phi = rho-check * F_psi decays as t -> -inf only like the tail of rho. Since F_phi is entire of exponential type and bounded on R, Cartwright's theorem (cited: such a function with int log|F|/(1+t^2) = -inf vanishes) would give a contradiction only for decay with int w(t)/t^2 dt = inf. Functions rho with compactly supported Fourier transform cannot decay that fast (same log-integral condition).
  So band-limiting in the flow direction and exponential backward decay are incompatible (an uncertainty principle), and this route is closed. I did not construct an explicit bounded F with all the properties in 4.1 (a "scalar counterexample"), so the consistency claim is a heuristic, not a theorem.

4.3. **Non-volume case.** Here R has codimension dim I, which may exceed 1. Facts (iii) and (vi) apply only to f in R, and the tower of Proposition 1 needs f in R_inf. Nothing forces R_inf to separate x from y. The suggestion "show that an (AP)-pair forces T(d) = c T(1) for all T in I" (which would give (V)) did not lead anywhere: I found no mechanism linking the pair, which lives on one orbit closure, to the values T(d) of arbitrary invariant distributions.

## 5. Summary: proved / sketched / open

**Proved (rigorous, given the brief's established facts (iv), (O2) and standard spectral theory):**
- Proposition 1: the tower identity G_j = U_j(g_t x) - U_j(g_t y), the factorisation T_z = z^j (Laplace transform of G_j), and flatness in sectors (under GH + (V), for any backward exponentially asymptotic pair).
- Proposition 2 and Corollary 2.1: under GH + (V), (AP) holds whenever the smooth functions with geometrically bounded iterated X-primitives separate points. More precisely, any asymptotic pair forces super-geometric growth of ||X^{-j} phi_0||_inf for every phi separating the two orbits.
- Lemma V: under GH + (V), no nonzero smooth mean-zero observable has an exponentially (or quasi-analytically) decaying autocorrelation in one time direction.

**Sketched only:** Remark 2.2 (Gevrey s < 1 version); the consistency heuristic of 4.2.

**Open (explicitly):**
- (AP) itself, both in the volume case (= no backward exponentially asymptotic pair for a GH flow with smooth invariant volume) and in general.
- Two natural sub-questions isolated here, either of which would settle the volume case of (AP):
  - (Q1) Under GH + (V), do the smooth functions with liminf ||X^{-j} phi_0||^{1/j} < inf (or with Gevrey-s, s < 1, growth) separate points?
  - (Q2) Under GH + (V) and an (AP)-pair (or positive entropy), is there a nonzero smooth mean-zero h with exponentially decaying autocorrelation?
- The zero-entropy goal in dimension >= 4 remains open on this chain.

=== END OF ANSWER round11_q7 ===
