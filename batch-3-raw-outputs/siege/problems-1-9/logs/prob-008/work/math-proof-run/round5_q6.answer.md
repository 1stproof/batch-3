# Answer to round5_q6: Claim (N)

## Summary of outcome

**(N) is PROVED, and GH is not needed for it.** For every smooth vector field X on a compact manifold with lambda* > 0, there is a real kappa != 0 and a nonzero generalized function u in D'(M) with Xu = kappa u. In the new case, u has order <= 1.

The proof splits into two cases.
- **Case A.** Some invariant probability mu has mu(d) != 0. This is the already-settled case ([R4-q7] Prop 2.2), re-checked below.
- **Case B.** Every invariant probability has mu(d) = 0. Here a new, explicit construction works. Take a pair of distinct points x != y that are exponentially asymptotic in backward time; such a pair is supplied by the Pesin–Ruelle unstable manifold of a measure with a positive exponent. Form a Laplace-transformed, Jacobian-weighted difference of their orbit measures. The result is an eigen-distribution. It is nonzero for all but a discrete set of kappa in an interval, by uniqueness of the Fourier transform.

The cancellation-of-orientation problem of the planner's sketch never arises. The object is not built from a stationary symmetric measure. It is built from a single pair of points, and its value at time 0 is the nonzero functional phi -> phi(x) - e^b phi(y).

Cited from memory, not proved here: the Pesin–Ruelle stable/unstable manifold theorem, used only in the weak form (R) below. Everything else is proved in full.

What remains open for the overall chain is (E1) only. (N) does not need GH. So in the chain, (E1) must carry the whole weight: (E1) would forbid exponentially asymptotic pairs (see the Remarks).

## Conventions

As in Text B and Lemmas C–F:
- nu is a smooth positive density, and d = div_nu X, so L_X(phi nu) = (X phi + d phi) nu.
- J_t(z) = int_0^t d(g_s z) ds for all real t. So d/dt J_t(z) = d(g_t z).
- A distribution density T (a continuous linear functional on C^inf(M)) gives the generalized function u = T/nu, defined by <u, phi nu> = T(phi).
- Then <Xu, phi nu> = -<u, L_X(phi nu)> = -T(X phi + d phi).
- Hence: **if T(X phi + d phi) = c T(phi) for all smooth phi, then Xu = -c u.** (*)

Fix a Riemannian distance on M. Every smooth phi is Lipschitz with constant ||dphi||_inf. The function d is Lipschitz with some constant Lip(d).

## Step 1. lambda* > 0 gives an invariant measure with a positive exponent

**Lemma 1.** Put a_n(x) = log||Dg_n(x)|| and assume lambda* = lim_n (1/n) max_x a_n(x) > 0. Then there is a flow-invariant Borel probability m such that chi(x) := lim_n (1/n) a_n(x) exists m-a.e. and int chi dm >= lambda*. In particular chi > 0 on a set of positive m-measure.

*Proof.*
1. a_n is continuous and subadditive: a_{n+k}(x) <= a_n(x) + a_k(g_n x).
2. Let x_n be a maximiser of a_n. Put mu_n = (1/n) sum_{k<n} delta_{g_k x_n}. Then (g_1)_* mu_n - mu_n = (delta_{g_n x_n} - delta_{x_n})/n -> 0. So every weak* limit mu is g_1-invariant. Fix such a limit along a subsequence.
3. Fix N. Let K = N max(0, max_x log||Dg_1(x)||), so that a_j <= K for 0 <= j <= N, since a_j <= j max log||Dg_1||.
4. For each 0 <= j < N, split [0, n) into [0, j), then blocks of length N, then a remainder of length < N. Subadditivity gives a_n(x) <= sum over blocks of a_N(g_{j+iN} x) + 2K.
5. The blocks for j = 0..N-1 together use each index k < n at most once, and the indices omitted lie within N of n. Summing over j:
   N a_n(x) <= sum_{k<n} a_N(g_k x) + 2NK + N^2 max|a_N|.
6. Take x = x_n and divide by Nn: max a_n / n <= (1/N) int a_N dmu_n + O_N(1/n).
7. Let n -> inf along the subsequence. Since a_N is continuous: lambda* <= (1/N) int a_N dmu. This holds for every N, with the same mu.
8. Put m = int_0^1 (g_s)_* mu ds. It is flow-invariant, because mu is g_1-invariant.
9. From Dg_N(g_s x) = Dg_s(g_N x) Dg_N(x) Dg_{-s}(g_s x) we get |a_N(g_s x) - a_N(x)| <= 2L, where L = max_{|r|<=1, z} log^+ max(||Dg_r(z)||, ||Dg_r(z)^{-1}||). Hence (1/N) int a_N dm >= lambda* - 2L/N.
10. By Kingman's subadditive ergodic theorem for g_1 and m: chi exists m-a.e., and int chi dm = lim_N (1/N) int a_N dm >= lambda*. ∎

## Step 2. A pair exponentially asymptotic in backward time (cited theorem)

**(R) Pesin–Ruelle stable manifold theorem, weak form (cited from memory).** Ruelle, "Ergodic theory of differentiable dynamical systems", Publ. IHES 50 (1979), Thm. 6.1. Also Pesin 1977, and Fathi–Herman–Yoccoz 1983.

Let f be a C^r diffeomorphism (r > 1) of a compact manifold, and m an f-invariant Borel probability. For m-a.e. x the following holds. If f has a negative Lyapunov exponent at x, then there is y != x with limsup_n (1/n) log d(f^n x, f^n y) < 0. Indeed, for lambda < 0 not an exponent at x and above the smallest exponent, the set {y : limsup (1/n) log d(f^n x, f^n y) <= lambda} contains an embedded C^1 disc through x of positive dimension. No hyperbolicity of the other exponents is required.

**Lemma 2.** If lambda* > 0, there are x != y in M and constants C0, theta > 0 with
d(g_{-t} x, g_{-t} y) <= C0 e^{-theta t} for all real t >= 0.

*Proof.*
1. Take m from Lemma 1, and apply (R) to f = g_{-1} = (g_1)^{-1}, which is C^inf. Here m is f-invariant.
2. By Oseledets, at m-a.e. x the exponents of g_{-1} are the negatives of those of g_1. On the positive-measure set where chi(x) > 0, f therefore has the negative exponent -chi(x).
3. So for some such x there is y != x and theta' > 0 with d(g_{-n} x, g_{-n} y) <= C e^{-theta' n} for all integers n >= 0.
4. For real t >= 0, write t = n + s with s in [0, 1). Then g_{-t} = g_{-s} o g_{-n}. With L' = max_{s in [0,1]} Lip(g_{-s}):
   d(g_{-t} x, g_{-t} y) <= L' C e^{theta'} e^{-theta' t}. ∎

## Step 3. Case B: uniform sublinearity of J

**Lemma 3.** Suppose every flow-invariant probability mu has mu(d) = 0. Then for every eps > 0 there is C_eps with |J_t(z)| <= eps|t| + C_eps for all z in M and all real t.

*Proof.*
1. Suppose not. Then there are eps > 0, |t_n| -> inf and z_n with |J_{t_n}(z_n)| >= eps|t_n|. Bounded |t| is trivial, since |J_t| <= ||d||_inf |t|.
2. If t_n -> +inf, put m_n = (1/t_n) int_0^{t_n} delta_{g_s z_n} ds, so that m_n(d) = J_{t_n}(z_n)/t_n.
3. If t_n -> -inf, put m_n = (1/|t_n|) int_{t_n}^0 delta_{g_s z_n} ds, so that m_n(d) = -J_{t_n}(z_n)/|t_n|.
4. In both cases ||(g_r)_* m_n - m_n|| <= 2|r|/|t_n|. So a weak* limit m is a flow-invariant probability, and since d is continuous, |m(d)| = lim |m_n(d)| >= eps. This is a contradiction. ∎

## Step 4. Case B: the eigen-distribution

**Theorem B.** Suppose lambda* > 0 and every invariant probability has mu(d) = 0. Let x != y, C0 and theta be as in Lemma 2. Then for every kappa in (0, theta), except at most a discrete subset of (0, theta), there is a nonzero distribution density T_kappa of order <= 1 with

T_kappa(X phi + d phi) = kappa T_kappa(phi) for all smooth phi.

Hence u_kappa = T_kappa/nu is a nonzero generalized function with X u_kappa = -kappa u_kappa, by (*). This is (N) with real eigenvalue -kappa != 0.

*Proof.*

(a) **Defining the constant b.** For t <= 0 we have J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds, and |d(g_s x) - d(g_s y)| <= Lip(d) C0 e^{-theta|s|}. So the limit b := lim_{t->-inf} (J_t(x) - J_t(y)) exists, and
|J_t(x) - J_t(y) - b| <= K e^{-theta|t|} for t <= 0, where K = Lip(d) C0/theta.

(b) **The orbit function.** For smooth phi define
c_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y), for t in R.
Then c_phi is C^1, and c_phi'(t) = c_{P phi}(t) with P phi := X phi + d phi. This is because d/dt[e^{J_t(z)} phi(g_t z)] = e^{J_t(z)} (X phi + d phi)(g_t z).

(c) **Bounds.** Fix kappa in (0, theta) and choose eps with 0 < eps < min(kappa, theta - kappa)/2.

For t <= 0, write e^{b + J_t(y)} = e^{J_t(x)} e^{-r_t} with |r_t| <= K e^{-theta|t|} <= K. Then
|c_phi(t)| <= e^{J_t(x)} [ ||dphi||_inf C0 e^{-theta|t|} + |1 - e^{-r_t}| ||phi||_inf ]
          <= C1 ||phi||_{C^1} C_eps e^{-(theta - eps)|t|},
where C1 = C0 + K e^K. This uses |1 - e^{-r}| <= |r| e^{|r|} and Lemma 3.

For t >= 0, Lemma 3 gives |c_phi(t)| <= (1 + e^b) C_eps e^{eps t} ||phi||_inf.

Hence e^{-kappa t} c_phi(t) is bounded by:
- C ||phi||_{C^1} e^{-(kappa - eps) t} for t >= 0;
- C ||phi||_{C^1} e^{-(theta - eps - kappa)|t|} for t <= 0.

Both are integrable, and both tend to 0 at their respective ends.

(d) **Definition and order.** Put T_kappa(phi) := int_R e^{-kappa t} c_phi(t) dt. By (c) the integral converges absolutely and |T_kappa(phi)| <= C' ||phi||_{C^1}. So T_kappa is a distribution density of order <= 1.

(e) **Eigen-relation.** Integrate by parts on [-R, R]:
int_{-R}^R e^{-kappa t} c_{P phi}(t) dt = [e^{-kappa t} c_phi(t)]_{-R}^R + kappa int_{-R}^R e^{-kappa t} c_phi(t) dt.
By (c), applied to phi and to P phi, the boundary terms tend to 0 and both integrals converge as R -> inf. Hence T_kappa(P phi) = kappa T_kappa(phi).

(f) **Nonvanishing.** Choose smooth phi0 with phi0(x) = 1 and phi0(y) = 0, which is possible since x != y. Then c_{phi0}(0) = 1.
1. Let F(z) = int_R e^{-z t} c_{phi0}(t) dt for complex z with 0 < Re z < theta. By the bounds of (c), the convergence is absolute and locally uniform, with eps chosen per compact sub-strip. So F is holomorphic on the strip, and F(kappa) = T_kappa(phi0) for real kappa.
2. Suppose the zeros of F in (0, theta) accumulated at a point of (0, theta). Then F would vanish identically on the strip.
3. Take kappa0 = theta/2. The function G(t) = e^{-kappa0 t} c_{phi0}(t) is continuous and in L^1(R). Its Fourier transform is omega -> F(kappa0 + i omega), which would be identically 0. Fourier uniqueness on L^1 gives G = 0 a.e., hence everywhere by continuity. This contradicts G(0) = 1.
4. So the set {kappa in (0, theta) : T_kappa(phi0) = 0} is discrete in (0, theta). Off this set, T_kappa != 0. ∎

## Step 5. Case A: some invariant mu has mu(d) != 0 (settled case, re-checked)

By ergodic decomposition, some ergodic mu has lambda := mu(d) != 0. The proof of [R4-q7] Prop 2.2 checks out:
1. Take x generic for mu in both time directions. Then J_t(x) = lambda t + o(|t|) as t -> +-inf.
2. So c_s(t) = e^{J_t(x) - lambda t - s|t|} is integrable for each s > 0, and tends to 0 at +-inf.
3. Integrate d/dt[c_s(t) phi(g_t x)] = c_s(t)[(X phi + d phi - lambda phi)(g_t x) - s sign(t) phi(g_t x)] over R. For the probabilities T_s = c_s(t) dt pushed along the orbit and normalised, this gives |T_s(X phi + d phi - lambda phi)| <= s ||phi||_inf.
4. A weak* limit T as s -> 0 is a probability, hence nonzero, and satisfies T(X phi + d phi) = lambda T(phi).
5. By (*), u = T/nu satisfies Xu = -lambda u, with lambda != 0.

## Conclusion

**Theorem.** Let X be any smooth vector field on a compact manifold M with lambda* > 0; GH is not needed. Then there are a real kappa != 0 and a nonzero u in D'(M) with Xu = kappa u.
- In Case B, u has order <= 1, and -kappa can be any point of an interval (0, theta) outside a discrete set.
- In Case A, u has order 0.

So (N) holds.

The 1-current form asked for in the task follows at once. C := dW (in the task's notation W = u) is a nonzero exact, hence closed, 1-current. Indeed u is nonconstant, since Xu = kappa u with kappa != 0 and u != 0. And C satisfies the eigen-relation with s0 = +-kappa, because L_X commutes with d.

The proof uses only:
- (R), the Pesin–Ruelle stable manifold theorem for g_{-1} (cited from memory);
- Oseledets' and Kingman's theorems (standard, cited);
- Lemmas 1 and 3 and Theorem B, proved above;
- Prop 2.2, re-checked above.

## Remarks: what this means for the chain, and what stays open

1. **Open: (E1).** The proof of (N) never uses GH. So with (N) settled, (Lambda) now rests entirely on (E1): under GH, there is no nonzero W in D' with XW = kappa W for real kappa != 0. (E1) is not addressed here; it remains open.
2. **Sharpened target.** Theorem B shows more than (N): every pair x != y that is exponentially asymptotic in backward time (or, by the same construction for -X, in forward time) yields such eigen-distributions, provided all invariant measures have mu(d) = 0. So a proof of (E1) would show that a GH flow has no exponentially asymptotic pairs. Then lambda* = 0 follows from Lemma 2, with no further appeal to Pesin theory beyond (R). This form, "GH excludes exponentially asymptotic pairs", may be a more concrete target than (E1) itself.
3. **Why these objects are not ruled out cheaply.** The distributions T_kappa have genuine order 1 in Case B. This is consistent with the observation in the task that for a measure W, X + kappa is invertible on C^0 when d = 0.
4. **Why the one-sided integral gives no direct contradiction.** S(phi) = int_{-inf}^0 c_phi(t) dt converges in Case B. It satisfies S(X phi + d phi) = phi(x) - e^b phi(y), so u = S/nu solves Xu = -(delta_x - e^b delta_y)/nu. Smearing over a family of pairs whose endpoint measures differ by a smooth density would give Xu smooth. But I see no way to make that family smooth, since Pesin manifolds vary only measurably, nor to show that the smeared u is non-smooth. So this does not yield a direct contradiction with GH. It is recorded only as a possible line of attack on (E1).

=== END OF ANSWER round5_q6 ===
