# round13_q9: verification of Block R12-a (Theorem T, Lemma I, Corollary I', Corollary T2, Lemma T3)

Block R12-a is in the task file at lines 4263-4405. I checked every step against the quoted background: L1, Lemma 2 of Text B, (O2), and Theorem J of R6-a.

**Summary verdict.** Block R12-a proves Theorem T, Lemma I, Corollary I' and Corollary T2 as stated. Two inessential repairs are needed:
- the rearrangement argument at the end of Step 5 is imprecise, and is replaced below by a Fubini argument;
- the constant C_1 should be taken >= 1.

Lemma T3 holds with constant 2C (not C) and with the C^1-to-Lipschitz comparison constant of the metric. Remark 3 (Katok-free zero volume entropy in dimension 3) is correct modulo standard Pesin theory, listed in §3. The hypothesis dim M >= 2 is genuinely needed: the circle gives a counterexample.

## 1. Step-by-step check

### Lemma I: correct.
- eta_{r,eps} = H_eps(r - |x|) is (1/eps)-Lipschitz, takes values in [0,1], and has support in the closed r-ball, which is compact in B(R). It converges pointwise everywhere to 1[|x| < r].
- |G_k| <= min(1, d_k/eps), since eta takes values in [0,1] and has Lipschitz constant 1/eps. G_k vanishes outside (min I_k, max I_k + eps). g_k vanishes outside I_k and |g_k| <= 1. Hence int_0^R |G_k - g_k| <= min(1, d_k/eps)(d_k + eps) + d_k. If d_k <= eps the first term is <= 2d_k; if d_k > eps it is d_k + eps < 2d_k. So the total is <= 3 d_k, as claimed.
- For each k, G_k(r,eps) -> g_k(r) for r outside {alpha_k, beta_k}, with the bound 2 on [0,R]. Summable domination by 3d_k gives E(eps) -> 0.
- Choose eps_l with sum_l E(eps_l) < infinity. Then sum_l sum_k |G_k(r,eps_l) - g_k(r)| is integrable, hence finite a.e., so the inner sum tends to 0 a.e. Also sum_k |g_k(r)| < infinity a.e. At such r we get sum_k G_k(r,eps_l) -> sum_k g_k(r). The finitely many Dirac terms converge to e_j 1[|zeta_j| < r] for every r.
- The limit N(r) is an integer, since only finitely many of the g_k(r) in {-1,0,1} are nonzero.
- On the other side, int eta_{r,eps_l} w -> int_{B(r)} w by dominated convergence, since w is bounded on the closed r-ball.

### Corollary I': correct.
f(r) = tau int_{B(r)} w_0 is continuous with f(0) = 0. If tau != 0, f is strictly monotone (w_0 > 0 and m >= 1). So 0 < |f| < 1 on a nondegenerate interval, which contradicts "integer for a.e. r".

### Step 1: correct.
|phi(g_t a) - phi(g_t b)| <= Lip(phi) C_0 e^{-theta|t|}, so each leg integral converges absolutely. Also l(1) = 0.

### Step 2 (telescoping): correct.
- For a u-leg the boundary term at -infinity vanishes by uniform continuity of u.
- For an s-leg (a, b) = (x_{2i+2}, x_{2i+1}), the integral is u(x_{2i+1}) - u(x_{2i+2}), with the signs as stated.
- The sum telescopes to u(x_0) - u(x_{2L}) = u(x_0) - u(g_tau x_0) = -int_0^tau (Xu)(g_s x_0) ds, an oriented integral.

GH is not used in this step.

### Step 3 (identity (3.1)): correct.
- (O2) gives f = phi - omega(phi) = Xu with u smooth. This uses only GH, L1 and the duality consequence, and holds in every dimension.
- Since l(1) = 0 and seg(1) = tau, we get l(phi) = -seg(phi) + tau omega(phi).
- Extension to Lipschitz phi: chart-wise mollification of rho_alpha phi (partition of unity) gives smooth phi_j -> phi uniformly with sup_j Lip(phi_j) < infinity. Dominated convergence applies in each leg integral, with dominating function sup Lip(phi_j) C_0 e^{-theta|t|}.

### Step 4 (flow box): correct.
- K is a finite set together with a compact C^1 arc. It is Lebesgue-null, hence has empty interior when dim M >= 2, so p exists.
- X(p) != 0: a zero p would make delta_p an invariant probability different from omega, contradicting (O2).
- Shrinking the box so that U' misses K is possible, since K is closed.
- **"w_0 independent of s" is correct.** Psi_*(d/ds) = X gives L_{d/ds}(Psi^*omega) = Psi^*(L_X omega) = 0. So the density w(s,z) of Psi^*omega satisfies d_s w = 0 on the connected s-interval. (This invariance is not even essential: with a fixed chi one could use w(z) := int chi(s) w(s,z) ds, which is continuous and positive.)
- The constants c_2, C_1 are correct: take c_2 below the injectivity radius and so small that the c_2-neighbourhood of the compact set Psi([-delta,delta] x closed B(3R/2)) lies in a compact subset of the image of Psi. Minimising geodesics of length < c_2 then stay there, and C_1 = sup ||D Psi^{-1}|| there (l^1 norm on (s,z)).
- Repair (trivial): enlarge C_1 so that C_1 >= 1. The choice of T_1 in Step 5 needs C_0 e^{-theta(T_1 - delta)} < c_2, and that only follows from C_1 C_0 e^{-theta(T_1 - delta)} < c_2 when C_1 >= 1.
- The test function phi = (chi ⊗ eta) ∘ Psi^{-1} is Lipschitz on M: it is smooth-times-Lipschitz on the box and vanishes outside a compact subset of the box. Also seg(phi) = 0 and omega(phi) = int eta w_0. Correct.

### Step 5 (crossings).
- (i) and (ii): correct. Injectivity of Psi on (-3delta, 3delta) x B(3R) is what is used. z(t) is well defined, again by injectivity.
- (iii): correct. supp phi ⊂ Psi(supp chi x supp eta), so |s| < delta and z ∈ B(R).
  - t_c has the same sign as t: if H = (-inf, 0] and t_c >= 2delta, then t > delta, which is impossible; the other case is symmetric.
  - The window (t_c - delta, t_c + delta) lies inside H, because |t_c| >= 2delta.
  - On the window, g_t a = Psi(t - t_c, z(t_c)). If z(t_c) ∈ B(2R) \ B(R), injectivity shows that this point is outside Psi((-delta,delta) x B(R)), so phi = 0 = chi(t - t_c) eta(z(t_c)). So the formula phi(g_t a) = chi(t - t_c) eta(z(t_c)) holds for every crossing.
  - The windows are pairwise disjoint by (ii).
- **Matching: correct**, given C_1 >= 1.
  - Forward direction. y = g_{t_c} a = Psi(0, z) lies in the compact set, and d(y, g_{t_c} b) < c_2. So g_{t_c} b = Psi(s', z') with |s'| + |z' - z| < delta/2, and |z'| < 3R/2 + R/4 < 2R. Hence t_c - s' is a crossing time of b. It lies in H, since |t_c - s'| >= 2delta by (i) for b and it is within delta/2 of t_c.
  - Converse direction. For a crossing t' of b with |t'| >= T_1 + delta and z(t') ∈ B(5R/4), we get g_{t'} a = Psi(s'', z'') with z'' ∈ B(3R/2), so t_c := t' - s'' is an a-crossing with |t_c| >= T_1. Its partner is t' itself: g_{t_c} b = Psi(-s'', z(t')), so by injectivity s' = -s'' and z' = z(t').
  - The partner map is injective: the a-crossings are 2delta-separated and the partners move by < delta/2.
  - The bookkeeping is correct. Matched pairs come from a-crossings with |t_c| >= T_1 + 2delta and z ∈ B(3R/2); their partners have |t| >= T_1 + 3delta/2. Every b-crossing with |t'| >= T_1 + 3delta and z ∈ B(5R/4) is a partner. All unmatched crossings with |t| >= T_1 + 3delta have z outside B(R) and contribute 0. The unmatched crossings with |t| < T_1 + 3delta are finitely many, by (ii).
  - Summability: sum_k |alpha_k - beta_k| <= sum_k C_1 C_0 e^{-theta|t_k|} < infinity, since the t_k are 2delta-separated in a half-line.
  - **The data are independent of chi and eta.** They depend only on a, b, Psi, delta, R, T_1, and T_1 depends only on C_0, C_1, theta, delta, R, c_2.
- **Rearrangement: correct after the following repair.**
  - The issue: the individual integrals int_H phi(g_t a) dt are in general divergent. By (O2) the flow is minimal, so a crosses the box infinitely often with z ∈ B(R).
  - The given argument chooses T "in the gap between windows". Such gaps need not exist: the a-windows may tile H, and the b-windows can cover the remaining points. The bound on the straddling pair is also only sketched.
  - Repair (Fubini). By (iii) applied to a and to b, for every t ∈ H
    phi(g_t a) - phi(g_t b) = sum_j e_j chi(t - t_j) eta(zeta_j) + sum_k [chi(t - t_k) eta(alpha_k) - chi(t - t'_k) eta(beta_k)].
    Here t_j are the unmatched crossing times, t_k the matched a-crossings and t'_k = t_k - s'_k their partners. Each term is supported in a window inside H. The k-th bracket has L^1 norm at most
    ||chi'||_{L^1} |s'_k| ||eta||_inf + Lip(eta) |alpha_k - beta_k| <= (||chi'||_{L^1} ||eta||_inf + Lip(eta)) C_1 C_0 e^{-theta|t_k|},
    which is summable in k. So the series converges in L^1(H), and term-by-term integration gives
    int_H (phi(g_t a) - phi(g_t b)) dt = sum_j e_j eta(zeta_j) + sum_k (eta(alpha_k) - eta(beta_k)),
    because int chi = 1. This is exactly the claimed identity, with no truncation needed.
- Both time directions: each leg uses only one half-line H. A point x_i that appears in a u-leg and in an s-leg is treated separately in each leg, so infinitely many crossings in both time directions cause no extra difficulty.

### Step 6: correct.
- Summing over the 2L legs gives finite data (zeta_j, e_j ∈ {±1}) and a summable family of pairs.
- l(phi) = Lambda(eta) holds for every Lipschitz eta with compact support in B(R). By (3.1), (3.2) and seg(phi) = 0, Lambda(eta) = int eta (tau w_0) dz.
- Corollary I' with m = n - 1 >= 1 and w_0 continuous and positive on B(R) gives tau = 0.

### Step 7: correct.
- With nu = omega we have d = 0 and J = 0, so F_phi(t) = S(phi ∘ g_t).
- For t <= 0, grouping into u-legs gives |F_phi(t)| <= L Lip(phi) C_0 e^{-theta|t|}.
- For t >= 0, the identity sum_{i<2L} (-1)^i phi(g_t x_i) = -sum_i [phi(g_t x_{2i+1}) - phi(g_t x_{2i+2})] + phi(g_t x_0) - phi(g_t x_{2L}) holds, and the last two terms cancel because x_{2L} = x_0. This gives |F_phi(t)| <= L Lip(phi) C_0 e^{-theta t}.
- Since Lip(phi) <= c_M ||phi||_{C^1}, (*) of Theorem J holds with k = 1, eps = theta and C = c_M L C_0.
- Theorem J is stated for an arbitrary smooth positive density nu; its proof uses (F1) and (F2), which come from L1 and GH. So it applies with nu = omega, and S = 0.

### Corollary T2: correct.
- ~_u and ~_s are equivalence relations: for transitivity add the constants and take the smaller rate. Inserting trivial legs turns any finite ~_u/~_s path into a chain with common constants.
- Equivariance: for s <= 0 with s + t > 0 we have |s| <= |t|, so diam(M) <= diam(M) e^{theta|t|} e^{-theta|s|}. Correct.
- (i): a chain from x to g_t x closes up to the flow shift t, so T(a) gives t = 0 directly. The appeal to "no periodic orbits" is unnecessary but harmless.
- (ii): for t != t' in [0,1), g_t E ∩ g_{t'} E ⊂ g_t(A(x) ∩ A(g_{t'-t} x)) = ∅, by (i) and the fact that equivalence classes are equal or disjoint. Uncountably many disjoint sets of equal measure omega(E) in a probability space force omega(E) = 0. The statement is correctly restricted to measurable E ⊂ A(x); A(x) itself need not be measurable.
- (iii) is T(b).

### Lemma T3: correct after a constant repair.
- With f = phi - omega(phi) = Xu and omega(u) = 0, Step 2 (no closure needed) gives l(phi) = u(x_0) - u(x_{2L}). Also u(x_0) = u(g_tau x_0) - seg_tau(phi) + tau omega(phi). Hence l(phi) - tau omega(phi) + seg_tau(phi) = u(g_tau x_0) - u(x_{2L}).
- Lemma 2 (with nu = omega, k = 1) gives ||u||_{C^1} <= C ||f||_{C^m} <= 2C ||phi||_{C^m}.
- So the correct bound is 2C c_M ||phi||_{C^m} d(g_tau x_0, x_{2L}), not C ||phi||_{C^m} d(...). The proof in the block itself writes 2C; only the statement is off. Restate Lemma T3 with "some constant C' (= 2 c_M C)".

## 2. Hypotheses actually used, and Remark 3

### Hypotheses of Theorem T
- **M compact and connected, X smooth.** Connectedness enters through L1.
- **GH.** It is used in two places:
  - (3.1), via (O2): X(C^inf) is closed, and its annihilator is spanned by omega (L1, L2/Lemma 2, Hahn-Banach);
  - Theorem J in Step 7, via (F1) and (F2), i.e. L1 together with GH for constant right-hand sides.
- **A smooth invariant positive density omega.** It is used in (3.1), and for "no zeros" in Step 4 (via (O2)). Invariance of the box density w_0 under s is convenient but not essential, as noted in §1.
- **dim M >= 2.** It is used in Step 4 (K has empty interior) and in Lemma I (m = n - 1 >= 1). It is genuinely necessary. On M = S^1, X = d/dtheta is GH (Fourier series) and preserves dtheta. The trivial chain (L = 1, x_0 = x_1 = x_2) closes up to the flow shift tau = 2pi, so (a) fails.
- **Exponential convergence on the legs.**
  - For (a), it is only needed that int_H d(g_t a, g_t b) dt < infinity (so that l is defined on Lipschitz phi) and that the sum of the rate function over 2delta-separated times converges. Any rate rho(|t|) with rho decreasing and integrable suffices.
  - For (b), the two-sided exponential bound is needed, because Theorem J is used.
- **Not needed:** recurrence, Pesin theory, genericity, or any non-periodicity assumption. Non-periodicity is a consequence: a trivial chain at a periodic point would give tau = period != 0.

### Remark 3 (zero volume entropy in dimension 3 without Katok): correct, modulo standard Pesin theory
Setting: dim M = 3, GH, smooth invariant volume omega. The flow is then uniquely ergodic, so omega is ergodic, and X has no zeros.

Suppose h_omega(g_1) > 0.
1. **Exponents.** By Ruelle's inequality for g_1 and for g_{-1}, omega has a positive and a negative exponent. Together with the exponent 0 in the flow direction, the exponents are chi_+ > 0 > chi_- (in fact chi_- = -chi_+, since the volume is preserved). So omega is hyperbolic transverse to X.
2. **Pesin blocks.** Take a Pesin block Lambda of positive measure. On Lambda the local leaves W^u_loc and W^s_loc are one-dimensional C^1 curves of uniform size, depend continuously on the point, and are uniformly transverse to each other and to X. Points of W^u_loc(x) satisfy (u), and points of W^s_loc(x) satisfy (s), with constants uniform on Lambda. (Continuous time follows from the time-1 estimates and bounded Dg_t for |t| <= 1.)
3. **Absolute continuity.** The unstable and stable laminations are absolutely continuous (Pesin). Hence for omega-a.e. x_0 ∈ Lambda, W^u_loc(x_0) ∩ Lambda contains points x_1 != x_0 arbitrarily close to x_0. Likewise W^s_loc(x_1) ∩ Lambda contains points x_2 != x_1 arbitrarily close to x_1. The point is that x_1 and x_2 must lie in Lambda, so that their local leaves exist with uniform size; the block's sentence "in a Pesin block" should be read this way.
4. **Local product structure.** By uniform transversality on Lambda, for x_2 close enough to x_0 the curve W^u_loc(x_2) meets the 2-dimensional local weak-stable manifold W^{cs}_loc(x_0) = union over |s| small of W^s_loc(g_s x_0) at a point x_3 ∈ W^s_loc(g_tau x_0), with tau small.
5. **Contradiction.** x_0 ->u x_1 ->s x_2 ->u x_3 ->s g_tau x_0 is a chain (L = 2) closing up to the flow shift tau. Theorem T gives tau = 0 and delta_{x_0} - delta_{x_1} + delta_{x_2} - delta_{x_3} = 0. Since x_1 != x_0, we must have x_0 = x_3 and then x_1 = x_2, which is excluded.

Hence h_omega(g_1) = 0.

Pesin-theory facts cited (from memory, standard): Ruelle's inequality; the Oseledets theorem; the Pesin stable/unstable manifold theorem for nonuniformly hyperbolic flows; Pesin blocks with uniform leaf size, continuity and transversality; absolute continuity of the stable and unstable laminations; local product structure with the weak-stable leaf. (Pesin's entropy formula is not needed: Ruelle suffices.)

This gives zero *volume* entropy only. It does not give h_top = 0, which needs every ergodic measure, including non-volume and non-hyperbolic ones.

## 3. Verdict
- **Lemma I, Corollary I', Theorem T (a) and (b), and Corollary T2 (i)-(iii):** proved exactly as stated, under GH, dim M >= 2 and a smooth invariant positive density. Two repairs are needed:
  - (R1) C_1 >= 1 in Step 4;
  - (R2) the Fubini justification of the leg decomposition in Step 5, replacing the "gap between windows" truncation.
  Neither repair changes any statement.
- **Lemma T3:** proved with constant 2 c_M C in place of C, where C and m come from Lemma 2 and c_M bounds Lip by the C^1 norm.
- **Remark 3:** correct as a proof that h_omega(g_1) = 0 when dim M = 3 (volume case), modulo the Pesin facts listed above, and provided x_1, x_2 are chosen in the Pesin block.

## 4. Corrected full proof of Theorem T (for the final document)

**Setting.**
- M is compact, connected, of dimension n >= 2, with a Riemannian distance d.
- X is smooth and GH, and preserves a smooth positive probability density omega.
- c_M is a constant with Lip(phi) <= c_M ||phi||_{C^1}.

**Background used.**
- (O2): every smooth f with omega(f) = 0 is Xu with u smooth, and X has no zeros.
- Theorem J (R6-a), with nu = omega.

**Definition.** A *chain with constants (C_0, theta)* is a tuple (x_0, ..., x_{2L}) such that for 0 <= i < L:
- (u) d(g_t x_{2i}, g_t x_{2i+1}) <= C_0 e^{-theta|t|} for t <= 0;
- (s) d(g_t x_{2i+1}, g_t x_{2i+2}) <= C_0 e^{-theta t} for t >= 0.

It *closes up to the flow shift tau* if x_{2L} = g_tau x_0.

**Theorem T.** If a chain closes up to the flow shift tau, then
- (a) tau = 0;
- (b) sum_{i=0}^{2L-1} (-1)^i delta_{x_i} = 0.

**Lemma I and Corollary I'.** Exactly as in Block R12-a §2. The proof there is complete; see §1 above for the checked details.

### Proof of Theorem T

**Legs and the cycle functional.**
- The u-legs are (a, b; H) = (x_{2i}, x_{2i+1}; (-inf, 0]).
- The s-legs are (a, b; H) = (x_{2i+2}, x_{2i+1}; [0, inf)).
- In both cases d(g_t a, g_t b) <= C_0 e^{-theta|t|} on H.

For Lipschitz phi put
- l(phi) := sum over legs of int_H (phi(g_t a) - phi(g_t b)) dt. This is absolutely convergent and |l(phi)| <= 2L C_0 Lip(phi)/theta.
- seg(phi) := int_0^tau phi(g_s x_0) ds (oriented).

**Step A (telescoping, no GH).** For smooth u, l(Xu) = u(x_0) - u(x_{2L}).
- For a u-leg: int_{-inf}^0 d/dt[u(g_t a) - u(g_t b)] dt = u(a) - u(b), since u(g_t a) - u(g_t b) -> 0 as t -> -inf by uniform continuity.
- For an s-leg: the integral is u(b) - u(a) = u(x_{2i+1}) - u(x_{2i+2}).
- Summing telescopes. If x_{2L} = g_tau x_0, then l(Xu) = -seg(Xu).

**Step B (GH identity).** For Lipschitz phi: l(phi) = tau omega(phi) - seg(phi).
- For smooth phi, write phi - omega(phi) = Xu by (O2). Then use l(1) = 0, seg(1) = tau and Step A.
- For Lipschitz phi, take smooth phi_j -> phi uniformly with bounded Lipschitz constants. Pass to the limit, using dominated convergence in the leg integrals.

**Step C (flow box).**
- K := {x_i} ∪ g_{[0,tau]} x_0 is compact and null, hence has empty interior (n >= 2). Choose p ∉ K. Then X(p) != 0.
- Flow box: Psi(s, z) = g_s sigma(z) is a diffeomorphism of (-3delta, 3delta) x B(3R) (B(r) ⊂ R^{n-1}) onto an open set. Choose it with U' := Psi((-2delta, 2delta) x B(2R)) disjoint from K.
- Psi^*omega = w_0(z) ds dz with w_0 smooth and positive, because L_{d/ds} Psi^*omega = Psi^* L_X omega = 0.
- There are c_2 > 0 and C_1 >= 1 such that: if y ∈ Psi([-delta,delta] x closed B(3R/2)) and d(y, y') < c_2, then y' = Psi(s', z') and |s - s'| + |z - z'| <= C_1 d(y, y'), where y = Psi(s, z).
- Test functions: for chi ∈ C_c^inf((-delta, delta)) with int chi = 1 and eta Lipschitz with compact support in B(R), put phi := (chi ⊗ eta) ∘ Psi^{-1}, extended by 0. Then phi is Lipschitz with support in U' \ K. So seg(phi) = 0 and omega(phi) = int eta w_0 dz.

**Step D (one leg).** Fix a leg (a, b; H); a and b lie outside U'. A *crossing time* of a is a t with g_t a = Psi(0, z(t)) and z(t) ∈ B(2R).
- (i) |t| >= 2delta, since otherwise a = Psi(-t, z(t)) ∈ U'.
- (ii) Distinct crossing times differ by >= 2delta, by injectivity of Psi.
- (iii) For t ∈ H we have phi(g_t a) = sum over crossing times t_c ∈ H of chi(t - t_c) eta(z(t_c)). At most one term is nonzero, and the windows (t_c - delta, t_c + delta) lie in H and are pairwise disjoint. Indeed, if phi(g_t a) != 0 then g_t a = Psi(s, z) with |s| < delta and z ∈ B(R), so t_c = t - s is a crossing time; by (i), t_c lies in H. Conversely, on a window g_t a = Psi(t - t_c, z(t_c)), and injectivity gives phi = chi(t - t_c) eta(z(t_c)) (both sides vanish when z(t_c) ∉ B(R)).
- The same holds for b.

*Matching.* Choose T_1 > delta with C_1 C_0 e^{-theta(T_1 - delta)} < min(delta/2, R/4, c_2).
- For each crossing time t_k ∈ H of a with |t_k| >= T_1 + 2delta and alpha_k := z(t_k) ∈ B(3R/2), Step C gives g_{t_k} b = Psi(s'_k, beta_k) with |s'_k| + |beta_k - alpha_k| <= C_1 C_0 e^{-theta|t_k|} < delta/2.
- Then t'_k := t_k - s'_k is a crossing time of b in H with z(t'_k) = beta_k.
- The map k -> t'_k is injective.
- Every crossing t' of b in H with |t'| >= T_1 + 3delta and z(t') ∈ B(5R/4) is some t'_k (apply Step C at g_{t'} b, then injectivity of Psi).
- The remaining crossings are of two kinds:
  - those with |t| < T_1 + 3delta, which are finitely many by (ii); call them t_j, with zeta_j := z(t_j), e_j := +1 for a and -1 for b;
  - those with |t| >= T_1 + 3delta, which have z ∉ B(R) and contribute 0.

By (iii), for every t ∈ H:
 phi(g_t a) - phi(g_t b) = sum_j e_j chi(t - t_j) eta(zeta_j) + sum_k [chi(t - t_k) eta(alpha_k) - chi(t - t'_k) eta(beta_k)].
The k-th bracket has L^1(H)-norm at most (||chi'||_{L^1} ||eta||_inf + Lip(eta)) C_1 C_0 e^{-theta|t_k|}. This is summable because the t_k are 2delta-separated. So integrating term by term is legitimate:
 int_H (phi(g_t a) - phi(g_t b)) dt = sum_j e_j eta(zeta_j) + sum_k (eta(alpha_k) - eta(beta_k)), with sum_k |alpha_k - beta_k| < infinity.
The data (zeta_j, e_j, alpha_k, beta_k) do not depend on chi or eta.

**Step E (proof of (a)).** Summing Step D over the legs gives l(phi) = Lambda(eta), in the notation of Lemma I. By Steps B and C, Lambda(eta) = int eta (tau w_0) dz for all Lipschitz eta with compact support in B(R). Corollary I' (m = n - 1 >= 1) gives tau = 0.

**Step F (proof of (b)).** Now x_{2L} = x_0. Put S := sum_{i<2L} (-1)^i delta_{x_i} and F_phi(t) := S(phi ∘ g_t).
- For t <= 0, grouping into u-legs: |F_phi(t)| <= L c_M C_0 e^{-theta|t|} ||phi||_{C^1}.
- For t >= 0, F_phi(t) = -sum_i [phi(g_t x_{2i+1}) - phi(g_t x_{2i+2})], using x_{2L} = x_0. This gives the same bound with e^{-theta t}.

With nu = omega (so J = 0), (*) of Theorem J holds with k = 1 and eps = theta. Hence S = 0. ∎

## 5. Status
- **Proved:** everything in §3's verdict, with repairs (R1) and (R2) and the corrected constant in Lemma T3.
- **Cited:** Remark 3 relies on standard Pesin theory, cited from memory (§2).
- **Open, and not addressed by this block:**
  - the general problem (h_top = 0 for GH flows) beyond the volume case;
  - (Q-vol) of the block;
  - the non-volume case (PE0).

=== END OF ANSWER round13_q9 ===
