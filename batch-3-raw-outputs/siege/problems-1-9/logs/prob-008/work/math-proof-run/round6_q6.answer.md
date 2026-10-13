# round6_q6 — generic pairs + GH at the eigenvalue 0

## 0. Summary

Two things are fully proved here.
- **Lemma Z.** Under GH, a family of distribution densities T_z that depends holomorphically on z near 0 (or meromorphically, with the pole order bounded), and satisfies T_z(P phi) = z T_z(phi), is identically 0. This replaces the vague Step 3 of the brief ("show T_0 is not c nu") by a clean mechanism. At z = 0, L1 forces T_0 = c nu. GH then also forbids a Jordan block at 0, so c = 0. Inductively every z-derivative at 0 vanishes.
- **Theorem 1 (pair theorem).** Under GH there is no pair x != y that converges exponentially in backward time at rate theta, has forward Jacobian rate a < 0, and has backward Jacobian growth rate beta < theta. No dimension restriction is needed.

Consequence (Theorem 2, proved modulo the cited theorems of Pesin, Ledrappier–Young and Birkhoff). Assume GH, and let mu be ergodic with h_mu(g_1) > 0 and lambda = mu(d). Let chi^+ > 0 be the smallest positive Lyapunov exponent of mu and -chi^- < 0 the largest negative one. Then
  **lambda = 0, or lambda <= -chi^+, or lambda >= chi^-.**

Theorem 3 is a sketch that relies on cited linearisation along 1-D unstable leaves. If the unstable (respectively stable) Oseledets space of mu is one-dimensional, then lambda < 0 (respectively lambda > 0) is impossible. Combined with the earlier results [R5-d] Thm 4.1 / [R5-e] Prop 5.1 this would give (PE), and hence the goal, in dimension 3 (sketch level).

**Open.** The case lambda = 0 is open, and for lambda != 0 the band |lambda| >= theta is open in dimension >= 4. Section 5 explains why the forward-orbit construction cannot reach lambda = 0: the point z = 0 is always on the boundary of the domain of holomorphy. It also gives the precise extra input that would suffice: a meromorphic continuation across Re z = lambda.

So (PE) is NOT proved in general.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, and P phi = X phi + d phi. A distribution density is a continuous linear functional on C^inf(M), taken complex-valued. Fix a Riemannian distance; then |phi(p) - phi(q)| <= ||d phi||_inf dist(p,q).

## 1. Lemma A (GH at the eigenvalue 0, with no Jordan block)

**Lemma A.** Assume GH. Let S be a continuous linear functional on C^inf(M, C), and let alpha be in C, such that S(P phi) = alpha * int phi dnu for all smooth phi. Then alpha = 0 and S = c nu for a constant c.

*Proof.*
1. Let u be the distribution <u, phi nu> = S(phi). Then <Xu, phi nu> = -S(P phi) = <-alpha, phi nu>, so Xu = -alpha, which is a smooth (constant) function.
2. X is a real operator, so Re u and Im u separately satisfy X(.) = smooth. By GH both are smooth, so u is smooth.
3. Let mu be any flow-invariant Borel probability; one exists by Krylov–Bogolyubov. Then int Xu dmu = d/dt|_{t=0} int u o g_t dmu = 0, so alpha = 0.
4. Now Xu = 0, and L1 (applied to Re u and Im u) shows that u is a constant c. ∎

## 2. Lemma Z (holomorphic eigenfamilies through 0 vanish)

**Lemma Z.** Assume GH. Let Omega in C be a connected open set containing 0. Let (T_z), z in Omega, be continuous linear functionals on C^inf(M, C) such that:
- (i) z -> T_z(phi) is holomorphic on Omega for each phi;
- (ii) T_z(P phi) = z T_z(phi) for all z and phi.

Then T_z = 0 for all z in Omega.

The same conclusion holds if instead T_z is defined on Omega \ {0}, satisfies (i) and (ii) there, and z^m T_z(phi) extends holomorphically to 0 for one m independent of phi. (Apply the lemma to z^m T_z, which satisfies the same relation (ii).)

*Proof.*
1. **The derivatives are distributions.** Fix r > 0 with the closed disc of radius r inside Omega. For each phi, z -> T_z(phi) is bounded on the circle |z| = r. Banach–Steinhaus applies because C^inf is Fréchet, hence barrelled. So there is a continuous seminorm p with |T_z(phi)| <= p(phi) for |z| = r. By Cauchy's formula, T^{(k)}(phi) := (d/dz)^k T_z(phi)|_{z=0} satisfies |T^{(k)}(phi)| <= k! r^{-k} p(phi). So each T^{(k)} is a continuous linear functional.
2. **Differentiate (ii).** Differentiating (ii) k times at z = 0 (Leibniz) gives T^{(0)}(P phi) = 0, and T^{(k)}(P phi) = k T^{(k-1)}(phi) for k >= 1.
3. **Induction.** By Lemma A with alpha = 0, T^{(0)} = c_0 nu. Suppose T^{(k-1)} = c_{k-1} nu. Then T^{(k)}(P phi) = k c_{k-1} int phi dnu. Lemma A gives k c_{k-1} = 0 and T^{(k)} = c_k nu. Hence every c_j vanishes (each is killed at the next step), and every T^{(k)} = 0.
4. **Conclusion.** For each phi, all derivatives of z -> T_z(phi) vanish at 0. By the identity theorem, T_z(phi) = 0 on the connected set Omega. ∎

Remark. Lemma Z is exactly the statement "0 is not a resonance of the transposed operator, not even with a Jordan block". GH enters twice: through L1 (kernel) and through Lemma A (no generalized eigenvector at 0). Note that only the eigenvalue 0 is used; (E1) is not needed.

## 3. Theorem 1 (pair theorem)

**Theorem 1.** Assume GH (any dimension). There are no points x != y and constants C >= 1, theta > 0, a < 0, beta < theta such that:
- (1) dist(g_{-t} x, g_{-t} y) <= C e^{-theta t} for all real t >= 0;
- (2) J_t(x) <= a t + C and J_t(y) <= a t + C for all t >= 0;
- (3) J_t(x) <= beta |t| + C for all t <= 0.

*Proof.* Suppose such data exist.

(a) **The constant b.** For t <= 0,
J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds, and |d(g_s x) - d(g_s y)| <= Lip(d) C e^{-theta|s|}.
So b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists. Moreover r_t := J_t(x) - J_t(y) - b satisfies |r_t| <= K e^{-theta|t|}, where K = Lip(d) C / theta.

(b) **The orbit function.** Put c_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y). Since d/dt [e^{J_t(w)} phi(g_t w)] = e^{J_t(w)} (P phi)(g_t w), the function c_phi is C^1 with c_phi' = c_{P phi}.

(c) **Bounds.**
- For t >= 0, (2) gives |c_phi(t)| <= (1 + e^b) e^C e^{a t} ||phi||_inf.
- For t <= 0, use e^{b + J_t(y)} = e^{J_t(x)} e^{-r_t} to write
  c_phi(t) = e^{J_t(x)} [ phi(g_t x) - phi(g_t y) + (1 - e^{-r_t}) phi(g_t y) ].
  By (1), (3) and |1 - e^{-r}| <= |r| e^{|r|}, this gives |c_phi(t)| <= e^C (C + K e^K) ||phi||_{C^1} e^{-(theta - beta)|t|}.

(d) **Holomorphic family.** Let Sigma = {z : a < Re z < theta - beta}. This is a vertical strip, it is connected, and it contains 0. For z in Sigma put
T_z(phi) = int_R e^{-z t} c_phi(t) dt.
By (c), |e^{-zt} c_phi(t)| <= C' ||phi||_{C^1} e^{-(Re z - a) t} for t >= 0, and <= C' ||phi||_{C^1} e^{-(theta - beta - Re z)|t|} for t <= 0. These bounds are uniform for Re z in compact subintervals. Hence:
- the integral converges absolutely;
- T_z is holomorphic in z (differentiate under the integral sign, or use Morera);
- |T_z(phi)| <= C''(z) ||phi||_{C^1}, so T_z is a distribution density of order <= 1.

(e) **Eigen-relation.** Integrating by parts on [-R, R],
int_{-R}^R e^{-zt} c_{P phi} dt = [e^{-zt} c_phi]_{-R}^R + z int_{-R}^R e^{-zt} c_phi dt.
By (c) the boundary terms tend to 0 as R -> inf. Hence T_z(P phi) = z T_z(phi).

(f) **Contradiction.** By Lemma Z, T_z = 0 on Sigma. Pick a smooth phi_0 with phi_0(x) = 1 and phi_0(y) = 0; this is possible because x != y. Then G(t) := c_{phi_0}(t) (this is the case z = 0) is continuous and in L^1(R). Its Fourier transform is omega -> T_{i omega}(phi_0), and i omega lies in Sigma for every real omega. So the Fourier transform is identically 0. By Fourier uniqueness on L^1, G = 0, contradicting G(0) = 1. ∎

**Theorem 1' (time-reversed form).** Apply Theorem 1 to -X, which is GH by (O4). Its divergence is -d, its flow is g_{-t}, and its Jacobian cocycle is J'_t = -J_{-t}. Under GH there are no x != y and constants theta > 0, alpha > 0, beta < theta, C such that:
- dist(g_t x, g_t y) <= C e^{-theta t} for t >= 0;
- J_t(x) >= alpha |t| - C and J_t(y) >= alpha |t| - C for t <= 0;
- J_t(x) >= -beta t - C for t >= 0.

Remarks.
- (i) Theorem 1 does not use dim M >= 2, non-periodicity, or any invariant measure (except the one used in Lemma A).
- (ii) The same proof works for any finite family y_0, ..., y_k of points backward-asymptotic to x, with c_phi = sum_i a_i e^{b_i + J_t(y_i)} phi(g_t y_i), where b_i = lim (J_t(x) - J_t(y_i)) and a_0 != 0. What is needed is a backward bound |c_phi(t)| <= C ||phi||_{C^k} e^{-(theta' - beta)|t|} with theta' > beta, plus forward rates a < 0. This is used in Section 5.

## 4. Theorem 2 (consequence for ergodic measures)

**Cited from memory (standard).**
- **[Pes]** Pesin–Ruelle unstable manifold theorem for the C^inf diffeomorphism f = g_1 and an f-invariant probability mu. For mu-a.e. x, the unstable set W^u(x) consists of points y with lim sup_n (1/n) log dist(f^{-n} x, f^{-n} y) <= -chi^+(x) < 0, where chi^+(x) is the smallest positive exponent at x.
- **[LY]** Ledrappier–Strelcyn (1982) and Ledrappier–Young (Annals 1985, Part I). There is a measurable partition xi subordinate to W^u, meaning that xi(x) is contained in W^u(x) for a.e. x, with h_mu(f) = H_mu(xi | f xi). Consequently, if h_mu(f) > 0, the conditional measures mu^xi_x are not Dirac masses for a set of x of positive mu-measure. (If they were Dirac a.e., xi would be the point partition mod 0, and the conditional entropy would be 0.)
- **[Rue]** Ruelle's inequality; Birkhoff's theorem for flows.

**Theorem 2.** Assume GH. Let mu be a flow-ergodic invariant probability with h_mu(g_1) > 0, and put lambda = mu(d). The Lyapunov exponents of g_1 are flow-invariant functions, hence mu-a.e. constant. By [Rue] applied to g_{+-1} there are positive and negative exponents. Let chi^+ be the smallest positive exponent and chi^- the smallest modulus of a negative exponent. Then neither -chi^+ < lambda < 0 nor 0 < lambda < chi^- holds.

*Proof.* Suppose -chi^+ < lambda < 0.
1. **Constants.** Choose theta with -lambda < theta < chi^+. Choose eps > 0 with lambda + eps < 0 and -lambda + eps < theta.
2. **Generic points.** Let G be the set of points z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf. G is invariant and has full measure (Birkhoff, two directions).
3. **A generic pair.** By disintegration, mu^xi_x(G) = 1 for mu-a.e. x. Take x in G satisfying [Pes], with mu^xi_x not a Dirac mass and mu^xi_x(G) = 1. Then mu^xi_x(G \ {x}) > 0, so there is y in G ∩ xi(x) with y != x.
4. **Check (1).** By [Pes], dist(g_{-n} x, g_{-n} y) <= C e^{-theta n} for integers n >= 0. Real t is handled as in [R5-a] Lemma 2, step 4.
5. **Check (2).** Since x, y are in G, J_t(x), J_t(y) <= (lambda + eps) t + C for t >= 0. So (2) holds with a = lambda + eps < 0.
6. **Check (3).** For t <= 0, J_t(x) = lambda t + o(|t|) <= (-lambda + eps)|t| + C, so (3) holds with beta = -lambda + eps < theta.
7. Theorem 1 gives a contradiction.

The case 0 < lambda < chi^- is the same argument applied to -X. Here mu is invariant and ergodic for -X with the same entropy, the divergence is -d so lambda becomes -lambda, and the exponents change sign, so the smallest positive exponent of g_{-1} is chi^-. Use Theorem 1 (which assumes only GH, and -X is GH). ∎

Refinement (cited, less certain). In [LY] one can use the intermediate strong-unstable foliations W^i (exponents >= chi_i). Let i_0 be the first index with h_{i_0} > 0 in the Ledrappier–Young hierarchy. Then the conditionals on W^{i_0} are non-atomic, and theta can be taken just below chi_{i_0} instead of chi^+. This improves the excluded band to (-chi_{i_0}, 0).

## 5. Higher-order cancellation (sketch), and the case lambda = 0

### 5.1 One-dimensional unstable direction (sketch)

Suppose the unstable space of mu is one-dimensional, with exponent chi > 0, and lambda < 0.

**Cited.** For C^inf (C^{1+alpha} suffices for C^1) dynamics with 1-D unstable leaves, for mu-a.e. x there are C^inf charts H_w : W^u(w) -> R with H_w(w) = 0 and H_{g_t w} o g_t = Lambda_t(w) H_w, where Lambda_t(w) = |Dg_t restricted to E^u(w)|. These charts have tempered C^k bounds on fixed-size pieces: the C^k norm of H_{g_t w}^{-1} is <= C_eps e^{eps|t|}. (This is the standard nonstationary linearisation / affine structure: H_w(y) = int_w^y prod_{n>=1} ratio of the 1-D derivatives along the backward orbits.)

**Construction.**
1. Take k+1 distinct generic points y_0 = x, y_1, ..., y_k on W^u(x). They exist by the [LY] non-atomicity, since conditionals on a 1-D leaf that are non-atomic have uncountable support. Put sigma_i = H_x(y_i).
2. Take a = (a_0, ..., a_k) != 0 with sum_i a_i sigma_i^j = 0 for 0 <= j < k. This is a Vandermonde system, so a_0 != 0 can be arranged.
3. For t <= 0 write e^{b_i + J_t(y_i)} phi(g_t y_i) = e^{J_t(x)} h_t(sigma_i), where h_t(sigma) = e^{E_t(sigma)} phi(H_{g_t x}^{-1}(Lambda_t sigma)) and E_t(sigma) = -int_{-inf}^t [d(g_s y) - d(g_s x)] ds with y = H_x^{-1}(sigma).
4. In the linear coordinate, D_sigma^k [phi(H^{-1}_{g_t x}(Lambda_t sigma))] = O(e^{(eps - k chi)|t|}). Also D^k E_t = int_{-inf}^t O(e^{(eps - k chi)|s|}) ds = O(e^{(eps - k chi)|t|}).
5. By Taylor's formula with the moment conditions, |sum_i a_i h_t(sigma_i)| <= C ||phi||_{C^k} e^{-(k chi - eps')|t|}.

So Remark (ii) of Section 3 applies with theta' = k chi - eps', beta = -lambda + eps and a = lambda + eps. For k > -lambda/chi the strip contains 0, which contradicts GH. Step 1 needs k+1 distinct points, so it uses more than Theorem 2 did: there, a single point y != x was enough.
- What is needed is that the conditionals have no atoms at all, not merely that they are not Dirac.
- The standard dichotomy supplies this: for ergodic mu, the conditionals on an invariant measurable foliation are either a.e. Dirac or a.e. non-atomic. This is cited from memory.

Hence: **if mu has h_mu > 0 and a 1-D unstable space, then lambda >= 0; if it has a 1-D stable space, then lambda <= 0.** (Sketch: the tempered C^k bounds of the linearisation are cited, not proved.)

**Dimension 3 (sketch level).** For dim M = 3 and h_mu > 0, the exponents are chi_1 > 0 = chi_2 > chi_3 for mu-a.e. point, by [R5-d] Thm 4.1. So both the stable and the unstable spaces are 1-D, and 5.1 forces lambda = 0 for every ergodic mu of positive entropy. On the other hand, [R5-d] Thm 4.1 (modulo Katok / Lian–Young) produces a horseshoe Lambda carrying an ergodic measure of positive entropy (for example its measure of maximal entropy) with mu'(d) <= -a < 0. That is a contradiction. So in dimension 3, GH would imply h_top = 0, modulo the cited [KLY], [HYP], the linearisation along 1-D leaves, and [Pes], [LY]. This is consistent with Forni's theorem (recalled from memory) that GH vector fields in dimension 3 are smoothly conjugate to Diophantine linear flows on T^3.

### 5.2 Why lambda = 0 is out of reach of this construction

- **The strip touches 0.** For any construction based on forward orbit integrals of mu-generic points, holomorphy requires Re z > (forward Jacobian rate of the points used) = lambda. So the domain is contained in {Re z > lambda}, and Lemma Z needs 0 to be an interior point. At lambda = 0 one would need points of W^u(x) with forward rate < 0. For mu-generic points the forward rate is exactly 0. Other points of W^u(x) are not controlled by mu (no absolute continuity), and nothing in GH supplies them.
- **Higher-order backward cancellation does not help.** It moves only the right edge of the strip; the left edge is the forward rate.
- **Using -X does not help.** It replaces lambda by -lambda = 0.
- **What would suffice (proved, via the second form of Lemma Z).** Suppose the family T_z of Theorem 1, defined for lambda < Re z < lambda + theta with lambda = 0, admits a continuation (holomorphic, or meromorphic with bounded pole order at 0) to a connected neighbourhood of a segment that joins the strip to 0, still with values in distributions. Then GH is contradicted. Indeed, the relation T_z(P phi) = z T_z(phi) persists under analytic continuation for each phi. The family continues to consist of continuous functionals: Banach–Steinhaus gives local equicontinuity via Cauchy estimates, provided the continuation is locally bounded on each phi. Then Lemma Z applies. So the missing input at lambda = 0 is a *resonance-type continuation* of the single-orbit Laplace transforms int_0^inf e^{-zt} e^{J_t(x)} phi(g_t x) dt across Re z = 0. For individual orbits there is no reason for such a continuation to exist; Re z = 0 is generally a natural boundary.
- **Averaging over pairs does not help either.** Integrating T_z^{(x, y(x))} against conditionals of mu keeps the forward part as an average of e^{J_t}-weighted orbit integrals. By Jensen, int e^{J_t} dmu >= e^{lambda t}, so the left edge does not move below lambda.
- **The normalised limit is consistent with GH.** With s -> 0+ real, s T_s converges along subsequences to some S with S(P phi) = 0, hence S = c nu. In the volume-preserving uniquely ergodic case (nu = omega, d = 0, b = 0), S is the Abel mean of phi(g_t x) - phi(g_t y), and that tends to 0. So the normalised limit gives no contradiction.
- **The core case lies in the gap.** In the smooth-volume uniquely ergodic case, lambda = omega(d) = 0 is forced for the only invariant measure (O2). So the core case of the problem (the case predicted by the Greenfield–Wallach picture) sits exactly where this method stops.

## 6. What is proved, sketched and open

**Proved (given L1, Lemma 2 of Text B is not even needed):**
- Lemma A.
- Lemma Z, with its meromorphic variant.
- Theorems 1 and 1'.

**Proved modulo the cited Pesin, Ledrappier–Young, Ruelle and Birkhoff:** Theorem 2. Under GH every ergodic mu with h_mu > 0 has lambda in {0} ∪ (-inf, -chi^+] ∪ [chi^-, inf).

**Sketched (relying on cited tempered linearisation of 1-D unstable leaves):**
- 5.1: lambda < 0 is impossible when the unstable space is 1-D.
- (PE), hence h_top = 0, in dimension 3, combined with [R5-d] Thm 4.1.

**Open:**
- (O-a) lambda = 0, in every dimension >= 4, and in particular for flows with a smooth invariant volume.
- (O-b) lambda <= -chi^+ (or >= chi^-) when the unstable (stable) space has dimension >= 2 and the conditional measures do not live on a 1-D fast foliation.
  A route for (O-b): higher-order cancellation in polynomial nonstationary normal-form coordinates (Kalinin–Sadovskaya type), with the same Taylor argument as 5.1. I have not checked that such coordinates exist with tempered C^k bounds in general.
- (O-c) Continuation of the pair Laplace transforms T_z across Re z = lambda. By Lemma Z this would settle (O-a).

=== END OF ANSWER round6_q6 ===
