# round11_q8 answer

## 0. Plan and summary
Target: the [GOAL] (GH => h_top(g_1) = 0), or the missing statement (AP).

Outcome (details below):
- **Not settled.** I did not prove the [GOAL] or (AP). The case left open is (AP) with lambda = 0, which is the
  same as (PE0) of block R6-a: GH must exclude an ergodic, non-hyperbolic mu with h_mu(g_1) > 0 and mu(d) = 0. The
  whole volume-preserving case lies inside it.
- **Proved here (Theorem 1, Section 2):** under GH, every ergodic mu with h_mu(g_1) > 0 has mu(d) = 0. The proof is
  complete except for one cited theorem from the literature, (NF): non-stationary sub-resonance normal forms along
  Pesin unstable manifolds, quoted from memory and stated precisely in 2.1. The idea is to replace the pair
  delta_x - e^b delta_y of (AP) by a weighted sum of MANY Dirac masses on one local unstable leaf. The weights are
  chosen to kill every polynomial mode of the backward leaf dynamics: a non-autonomous version of the
  Cayley-Hamilton step in Lemma K. Block R6-a only sketched this extension, after its Prop. 6.2, and marked it
  conditional; here it is written out in full. Effect on the chain: (AP) is needed only for lambda = 0, and the
  branch "lambda <= -theta" of (AP) is no longer needed.
- **The suggested approach (volume growth, currents; Section 4) does not close the gap.** It produces currents with
  real nonzero L_X-eigenvalues, and GH does not exclude these. Every route I tried for bringing the exponent back to 0
  reduces to the open statement (E1), or to closed su-cycles (Section 3).
- **Section 3 explains exactly why lambda = 0 resists:**
  - a counting lemma: a finite combination of Dirac masses with two-sided cancellation needs closed su-cycles;
  - a computation, in the volume-preserving case, of what GH gives at the spectral point 0 for a pair: infinite-order
    flatness of the Laplace transform, which is consistent with S != 0;
  - an occupation-measure / pigeonhole attempt, and why it fails.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds,
P phi = X phi + d phi. A distribution density is a continuous linear functional on C^inf(M), and for such S we put
F_phi(t) = S(e^{J_t} (phi o g_t)). The cocycle identity is J_{t+r}(x) = J_r(x) + J_t(g_r x).

## 1. The GH input: Theorem J (block R6-a §2; I re-checked its proof)
**Theorem J.** Assume GH. Let S be a distribution density. Suppose there are eps > 0, k and C with
|S(e^{J_t} phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and all smooth phi. Then S = 0.

Check of the proof.
- The map t -> e^{J_t} phi o g_t is C^1 into C^inf(M), with derivative e^{J_t} (P phi) o g_t. So F_phi' = F_{P phi}.
- The moments m_j(phi) = int t^j F_phi dt are distribution densities, and integration by parts gives
  m_0(P phi) = 0 and m_j(P phi) = -j m_{j-1}(phi).
- (F1) If T(P phi) = 0 for all phi, then T = c nu. This is because u = T/nu has Xu = 0, so u is constant by L1.
- (F2) If T(P phi) = c' int phi dnu for all phi, then c' = 0. This is because Xu = -c' is smooth, so u is smooth by GH,
  and Xu vanishes at a maximum point of u.
- Induction with (F1) and (F2) gives m_j = 0 for all j.
- The Fourier transform of F_phi is holomorphic on |Im xi| < eps and has all derivatives 0 at 0. So F_phi = 0, and
  S(phi) = F_phi(0) = 0.

The proof is correct.

## 2. Theorem 1: under GH a positive-entropy ergodic measure has mu(d) = 0 (modulo the cited (NF))

### 2.1 Cited inputs (from memory; standard Pesin theory, plus one normal-form theorem)
Let f = g_1. Let mu be an ergodic flow-invariant probability; it is then f-invariant. If it is not f-ergodic, replace
it by a suitable f-ergodic component of positive entropy (Remark 2.3). Let 0 < chi_1 < ... < chi_l be the distinct positive Lyapunov exponents
of (f, mu), and E^u(x) the sum of their Oseledets spaces, of dimension u >= 1.

- **[Ru] Ruelle's inequality:** h_mu(f) <= sum of positive exponents. So h_mu(f) > 0 forces u >= 1.
- **[P] Pesin unstable manifolds:** for mu-a.e. x the global unstable manifold
  W^u(x) = {y : limsup_n (1/n) log d(f^{-n}x, f^{-n}y) < 0} is an injectively immersed C^inf copy of R^u, tangent to
  E^u(x), with f(W^u(x)) = W^u(fx).
- **[LY] Ledrappier-Strelcyn / Ledrappier-Young:** there is a measurable partition xi subordinate to W^u. That is,
  for a.e. x:
  - xi(x) ⊂ W^u(x);
  - xi(x) contains an open neighbourhood of x in W^u(x);
  - xi is increasing (f xi <= xi);
  - h_mu(f) = H_mu(xi | f xi).

  Write mu^xi_x for the conditional measures.
- **Lemma 6.0 (block R6-a; proof re-checked):** if h_mu(f) > 0, then mu^xi_x is non-atomic for a.e. x.
  - Put w(x) = mu^xi_x({x}). Then w(fx) = w(x) / mu^{f xi}_{fx}(xi(fx)) >= w(x).
  - Invariance and ergodicity then give w = w_0 a.e.
  - If w_0 > 0, then xi = f xi mod mu, so h_mu = 0.
  - So w = 0 a.e., and int mu^xi_x(atoms of mu^xi_x) dmu(x) = int w dmu = 0.
- **Support fact (elementary):** for a.e. x, x ∈ supp mu^xi_x.
  - Let E be the set of z with z not in supp mu^xi_z.
  - If z ∈ xi(x), then mu^xi_z = mu^xi_x. So E ∩ xi(x) = xi(x) \ supp mu^xi_x, which is mu^xi_x-null.
  - Hence mu(E) = int mu^xi_x(E) dmu(x) = 0.
- **(NF) Non-stationary sub-resonance normal forms on unstable manifolds.** I recall this from the Guysinsky-Katok
  and Kalinin-Sadovskaya theory of normal forms for contracting foliations and its measurable/non-uniform version
  (S. Melnick, "Non-stationary smooth geometric structures for contracting measurable cocycles", ETDS 2019; also used
  in work of Brown, Eskin, Filip and Rodriguez Hertz). This is the one input not checked here; I state exactly what
  I use.

  There is an integer D >= 1, depending only on chi_l / chi_1, such that for each K >= 1 and each delta > 0 the
  following holds for mu-a.e. x. There are:
  - an open neighbourhood U_x of x in W^u(x);
  - a C^K embedding H_x : U_x -> E^u(x) ≅ R^u with H_x(x) = 0;
  - constants C(x) and r(x) > 0;
  - for every n >= 0, a polynomial map P^{(n)}_x : R^u -> R^u of degree <= D;
  - C^K maps h_n : B(0, r(x) e^{-delta n}) -> M;

  such that:
  - (NF1) f^{-n}(y) = h_n(P^{(n)}_x(H_x(y))) for all y ∈ U_x and n >= 0;
  - (NF2) |P^{(n)}_x(v)| <= C(x) e^{-(chi_1 - delta) n} |v| for |v| <= r(x), and C(x) e^{-(chi_1 - delta)n} r(x) <= r(x) e^{-delta n};
  - (NF3) h_n(0) = f^{-n}x, and ||Psi o h_n||_{C^K(B(0, r(x)e^{-delta n}))} <= C(x) e^{delta n} ||Psi||_{C^K(M)} for every
    smooth Psi on M.

  In the usual formulation: h_n = H^{-1}_{f^{-n}x}, where the H_z are normal-form charts on W^u(z) with tempered
  C^K norms; P^{(n)}_x = H_{f^{-n}x} o f^{-n} o H_x^{-1} lies in the finite-dimensional group of sub-resonance
  polynomial maps, which is closed under composition and has degree <= D; and the contraction bound is the usual
  Lyapunov-norm estimate. If the cited theorem is only available with a slightly different normalisation, (NF1)-(NF3)
  are what the proof needs.

### 2.2 Theorem 1 and its proof
**Theorem 1.** Assume GH. Let mu be an ergodic flow-invariant Borel probability with h_mu(g_1) > 0. Then lambda := mu(d) = 0.

*Proof.*

**Step 0 (reduction to lambda < 0).** Suppose lambda > 0. Then -X is GH by (O4); its flow is g_{-t}, its
nu-divergence is -d, and mu is ergodic for it. Also h_mu(g_{-1}) = h_mu(g_1) > 0, and its lambda is -lambda < 0. So it
suffices to rule out lambda < 0.

From now on assume lambda < 0, and fix a small delta > 0. The size of delta is fixed in Step 5; in particular
lambda + delta < 0. Let chi := chi_1 > 0. By Birkhoff's theorem for the ergodic flow, the set
G = {z : J_t(z)/t -> lambda as t -> +inf and as t -> -inf} has mu(G) = 1. Let G_+ = {z : J_t(z)/t -> lambda as t -> +inf} ⊃ G.

**Step 1 (choice of x, of K, of the points).** Choose K ∈ N with K(chi - 2delta) >= |lambda| + 4 delta + 1, and put
N_1 := D(K-1) and N := K N_1. Let Q_N be the space of real polynomials on R^u of degree <= N, and put
m := dim Q_N + 1.

Choose x in the full-measure set where all of the following hold:
- x ∈ G;
- (NF) holds for this K and delta;
- mu^xi_x is non-atomic, with x ∈ supp mu^xi_x and mu^xi_x(G_+) = 1. The last condition holds a.e. because
  mu(G_+) = 1 = int mu^xi_x(G_+) dmu.

Shrink U_x to the open neighbourhood U := H_x^{-1}(B(0, r_0)) of x in W^u(x), with 0 < r_0 <= r(x). By [LY], xi(x)
lies in an embedded local unstable disc, on which the leaf topology and the topology of M agree. So
U ∩ xi(x) ⊃ xi(x) ∩ B_M(x, eps') for some eps' > 0. Then:
- mu^xi_x(U) >= mu^xi_x(B_M(x, eps')) > 0, since x ∈ supp mu^xi_x;
- U ∩ G_+ ∩ xi(x) has positive mu^xi_x-measure, hence is infinite, since mu^xi_x is non-atomic.

Pick m distinct points y_1, ..., y_m in U ∩ G_+, and put v_i := H_x(y_i) (distinct, as H_x is injective). The m
linear functionals q -> q(v_i) on Q_N are linearly dependent, since m > dim Q_N. So there is c = (c_i) != 0 with
sum_i c_i q(v_i) = 0 for all q ∈ Q_N.

**Step 2 (the weight correction beta).** Let a := J_{-1}, a smooth function on M. By the cocycle identity,
J_{-n}(y) = sum_{k=0}^{n-1} a(f^{-k} y). For y ∈ U and k >= 0, (NF1)-(NF3) give f^{-k}y = h_k(P^{(k)}_x(H_x y)), with
|P^{(k)}_x(H_x y)| <= C e^{-(chi-delta)k} r_0, and f^{-k}x = h_k(0). Hence

|a(f^{-k}y) - a(f^{-k}x)| <= ||a o h_k||_{C^1} |P^{(k)}(v)| <= C e^{-(chi - 2delta)k}.

Here and below C denotes constants depending on x, K, delta, the points and a, but not on n, t or phi. So
beta(y) := sum_{k>=0} [a(f^{-k}y) - a(f^{-k}x)] converges for y ∈ U, and

J_{-n}(y) - J_{-n}(x) = beta(y) - rho_n(y),  with  rho_n(y) := sum_{k>=n} [a(f^{-k}y) - a(f^{-k}x)].

Put the weights w_i := c_i e^{-beta(y_i)} and S := sum_i w_i delta_{y_i}. Since the y_i are distinct and some c_i != 0,
S != 0.

**Step 3 (polynomial structure of the backward transport).** Fix n >= 0, v ∈ B(0, r_0) and y = H_x^{-1}(v) ∈ U.
Write p_k := P^{(k)}_x(v), a polynomial in v of degree <= D, with |p_k| <= C e^{-(chi-delta)k}.

(a) *Taylor expansion of a single smooth function.* Let Psi be smooth on M and put psi_k := Psi o h_k, defined on
B(0, r(x)e^{-delta k}). By (NF3), ||psi_k||_{C^K} <= C e^{delta k} ||Psi||_{C^K}. Taylor's formula of order K at 0 gives

Psi(f^{-k}y) = psi_k(p_k) = T_k(p_k) + R_k,  with  |R_k| <= C e^{delta k} ||Psi||_{C^K} |p_k|^K <= C ||Psi||_{C^K} e^{-(K(chi-delta) - delta)k}.

Here T_k is the Taylor polynomial of degree <= K-1, with coefficients bounded by C e^{delta k}||Psi||_{C^K}. Since p_k
is a polynomial in v of degree <= D, the term T_k(p_k) is a polynomial in v of degree <= D(K-1) = N_1. Moreover
|T_k(p_k) - T_k(0)| <= C e^{delta k} ||Psi||_{C^K} |p_k| <= C ||Psi||_{C^K} e^{-(chi - 2delta)k}.

(b) *rho_n.* Apply (a) with Psi = a and subtract the value at v = 0, which is T_k(0) = a(f^{-k}x). Each term of
rho_n is then a polynomial in v of degree <= N_1, of size <= C e^{-(chi-2delta)k}, plus an error
<= C e^{-(K(chi-delta)-delta)k}. Summing over k >= n gives

rho_n(y) = Q_n(v) + E_n(v),  deg Q_n <= N_1,  |Q_n| <= C e^{-(chi-2delta)n},  |E_n| <= C e^{-(K(chi-delta)-delta)n}.

Hence e^{-rho_n} = e^{-Q_n} e^{-E_n} = e^{-Q_n}(1 + O(e^{-(K(chi-delta)-delta)n})). Also
e^{-Q_n} = sum_{j<K} (-Q_n)^j / j! + O(|Q_n|^K), where the sum is a polynomial in v of degree <= (K-1)N_1 and the
remainder is O(e^{-K(chi-2delta)n}). Since |Q_n| <= C, all these quantities are bounded. So

e^{-rho_n(y)} = A_n(v) + O(e^{-K(chi-2delta)n}),  with deg A_n <= (K-1)N_1 and |A_n| <= C.

(c) *The transported test function.* For phi smooth and r ∈ [0,1), put Phi^r := e^{J_{-r}} (phi o g_{-r}). Then
||Phi^r||_{C^K} <= C_K ||phi||_{C^K}, uniformly in r ∈ [0,1], since (r, z) -> (J_{-r}(z), g_{-r}z) is smooth on
[0,1] × M. By (a) with Psi = Phi^r and k = n,

Phi^r(f^{-n}y) = B_n(v) + O(||phi||_{C^K} e^{-(K(chi-delta)-delta)n}),  with deg B_n <= N_1 and |B_n| <= C e^{delta n} ||phi||_{C^K}.

(d) *Product.* Combining (b) and (c),

e^{-rho_n(y)} Phi^r(f^{-n}y) = A_n(v) B_n(v) + O(||phi||_{C^K} e^{-(K(chi-2delta) - delta)n}),

and A_n B_n ∈ Q_N, because (K-1)N_1 + N_1 = K N_1 = N.

**Step 4 (backward decay).** Let t <= 0 and write t = -n - r with n >= 0 an integer and r ∈ [0,1). By the cocycle
identity, J_t(y) = J_{-n}(y) + J_{-r}(f^{-n}y) and g_t y = g_{-r}(f^{-n} y). So
e^{J_t(y)} phi(g_t y) = e^{J_{-n}(y)} Phi^r(f^{-n}y). Then

F_phi(t) = sum_i w_i e^{J_{-n}(y_i)} Phi^r(f^{-n}y_i)
         = e^{J_{-n}(x)} sum_i c_i e^{-beta(y_i)} e^{beta(y_i) - rho_n(y_i)} Phi^r(f^{-n}y_i)
         = e^{J_{-n}(x)} sum_i c_i [ (A_n B_n)(v_i) + O(||phi||_{C^K} e^{-(K(chi-2delta)-delta)n}) ].

The polynomial part vanishes by the choice of c. Since x ∈ G and lambda < 0, J_{-n}(x) <= C + (|lambda| + delta) n.
Hence

|F_phi(t)| <= C ||phi||_{C^K} e^{(|lambda| + delta - K(chi - 2delta) + delta) n} <= C ||phi||_{C^K} e^{-n} <= C' ||phi||_{C^K} e^{-|t|}

by the choice of K.

**Step 5 (forward decay).** Each y_i ∈ G_+, so J_t(y_i) <= C + (lambda + delta) t for t >= 0. Hence
|F_phi(t)| <= sum |w_i| e^{J_t(y_i)} ||phi||_inf <= C e^{(lambda+delta)t} ||phi||_inf for t >= 0, with lambda + delta < 0.

**Step 6.** Steps 4 and 5 give |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^K} for all real t, with
eps = min(1, |lambda + delta|) > 0. By Theorem J, S = 0, contradicting Step 2. ∎

**Remark 2.3 (on the reduction to g_1-ergodic measures).** If the flow-ergodic mu is not g_1-ergodic, run the proof
with a suitable g_1-ergodic component mu_0 of positive entropy instead, chosen as below. Pesin theory, [LY],
Lemma 6.0 and (NF) are then applied to (g_1, mu_0).

The only flow-specific inputs are mu_0(G) = 1 and mu_0(G_+) = 1. These hold for the following reason. Since
mu(G) = 1, almost every component of the g_1-ergodic decomposition of mu gives G full measure; likewise for G_+.
Jacobs' formula h_mu(g_1) = ∫ h_{component} dP then gives a component mu_0 that has positive entropy and also satisfies
mu_0(G) = mu_0(G_+) = 1. Nothing else changes.

**Corollary 2.4 (effect on the chain).** Under GH, and granting (NF):
- (i) every ergodic mu with h_mu(g_1) > 0 has mu(d) = 0;
- (ii) in chain step 3, only the case lambda = 0 of (AP) is needed;
- (iii) together with Theorem 5.1 of block R6-a, such a mu is non-hyperbolic, with lambda = 0 and supp mu = M
  (Corollary D1).

Granting (NF), the [GOAL] therefore reduces to: GH excludes (PE0), an ergodic, non-hyperbolic mu with h_mu > 0 and
mu(d) = 0.

## 3. The case lambda = 0: what I tried and exactly where it stops

### 3.1 Why the Theorem J mechanism needs closed su-cycles when lambda = 0 (heuristic, not a lemma)
When lambda = 0, e^{J_t(z)} = e^{o(|t|)} at generic points in both time directions. So a Dirac combination
S = sum_z w_z delta_z needs cancellation in both directions:
- *forward:* inside classes of strong-stable-related points, with vanishing polynomial moments as in Section 2;
- *backward:* inside classes of strong-unstable-related points.

Consider the bipartite graph whose vertices are the s-classes and u-classes and whose edges are the points of Z.
Each class with nonzero total contribution needs at least N+1 points (N = dim Q_N - 1, which grows with K), so the
average degree must exceed N. A forest has fewer edges than vertices, so the graph must contain cycles. Each cycle is
a CLOSED su-cycle z_1 ~s z_2 ~u z_3 ~s ... ~u z_1 of points.

With center directions (forced by Theorem 5.1 of R6-a), or with only the flow direction (temporal distance), such
cycles generically do not close. Spreading the masses smoothly along center discs does not help. Consistency of the
weights around a cycle forces the cycle holonomy (a small map of a center-flow disc with no fixed point) to preserve
the spread measure, which is impossible for a compactly supported measure moved off itself.

Conversely, if exact su-grids exist (m×m points z_ij with z_ij ∈ W^s_loc(z_i1) and z_ij ∈ W^u_loc(z_1j), m > 2N,
base points (NF)-regular for g_1 and g_{-1}), then the argument of Section 2, applied row-wise backward and
column-wise forward, gives a nonzero S satisfying Theorem J. There are 2mN linear conditions on m^2 unknowns, and the
weight corrections beta are absorbed row- and column-wise as in Step 2. This covers any lambda. But grids exist only
in essentially jointly-integrable situations (e.g. Anosov suspension × rotation, which is not GH anyway because of its
periodic tori), so this is not a usable lemma.

### 3.2 Volume-preserving case: what GH gives at the spectral point 0 for a pair (proved; shows the obstruction)
**Proposition 3.2.** Assume GH and d = 0 (nu invariant). Let x != y with dist(g_t x, g_t y) <= C e^{-theta|t|} for
t <= 0. Put F_phi(t) = phi(g_t x) - phi(g_t y) and, for 0 < Re z < theta, E_z(phi) := int_R e^{-zt} F_phi(t) dt. Then:
(i) E_z is a distribution density of order 1, holomorphic in z, with E_z(X phi) = z E_z(phi);
(ii) E_z != 0 for some z in the strip;
(iii) for every smooth phi with int phi dnu = 0 and every N, E_z(phi) = z^N E_z(R^N phi), where R = X^{-1} on
     nu-mean-zero smooth functions (continuous, by (O2) and Text B). Hence
     |E_z(phi)| <= C_N(phi) |z|^N (1/Re z + 1/(theta - Re z)), while E_z(1) = 0.

*Proof.*
- (i): integrate d/dt[e^{-zt} F_phi(t)] over R. The boundary terms vanish: at -inf because Re z < theta and
  |F_phi| <= C e^{-theta|t|} ||phi||_{C^1}; at +inf because Re z > 0 and |F_phi| <= 2 ||phi||_inf.
- (ii): if E_z = 0 on a vertical line Re z = c, then the L^1 function e^{-ct} F_phi has zero Fourier transform. So
  F_phi = 0 and phi(x) = phi(y) for all phi, which is impossible.
- (iii): apply (i) to R phi, and iterate. The bound uses |int_{-inf}^0| <= C||R^N phi||_{C^1}/(theta - Re z) and
  |int_0^inf| <= 2||R^N phi||_inf/Re z. ∎

So, at the spectral point 0, GH is already satisfied to infinite order by every such pair. A contradiction needs
information at z != 0 near 0. For instance it would suffice that E_z extend holomorphically to a neighbourhood of 0:
then (iii) makes it flat at 0, hence identically 0, contradicting (ii). Equivalently, one needs control of the
forward part int_0^inf e^{-zt} F_phi dt across Re z = 0. For Diophantine linear flows this forward part has poles
i(k.alpha) accumulating at 0, so such an extension is false in the only known GH examples, even though there the
conclusion holds (no asymptotic pairs exist at all). The missing ingredient is therefore of the type (E1)/(OS):

**(OS) (open).** Under GH, there is no nonzero distribution density S such that F_phi(t) = S(e^{J_t} phi o g_t) is
O(e^{-theta|t|}) ||phi||_{C^k} as t -> -inf and O(e^{eta t}) ||phi||_{C^k} as t -> +inf for every eta > 0 (one-sided
decay).

(OS) holds for Diophantine linear flows: there F_phi is almost periodic, and an almost periodic function tending to 0
vanishes. (OS) implies (AP) at once, even without recurrence, since the pair gives such an S. Hence it implies the
[GOAL] via Section 2 and the chain. By the Laplace argument of 3.2, (OS) is equivalent to: GH excludes nonzero
holomorphic families z -> E_z, 0 < Re z < theta, of eigen-distributions E_z o (P - z) = 0 of the Laplace form above.
I could not prove it. Theorem J is exactly the two-sided version.

### 3.3 Occupation measures and entropy (volume-preserving case; dead end)
In the volume-preserving case, GH gives a tame inverse R = X^{-1}. Hence, for all a, b ∈ M, tau > 0 and smooth phi:

|int_0^tau phi(g_t a) dt - int_0^tau phi(g_t b) dt| <= C ||phi||_{C^m} (dist(a,b) + dist(g_tau a, g_tau b)).

So two orbit segments of equal length with eps-close endpoints have C^{-m}-close occupation measures, independently of
tau. I tried to contradict this with positive entropy by a pigeonhole argument. Among exp((h - eta) tau) separated
orbit segments, two have eps-close starts and ends once tau is large. But occupation measures, and even k-block
occupation measures for fixed k (test functions phi·(psi o g_1)···), are "abelian" statistics. Exponentially many
separated segments share them, so no contradiction follows. Letting k grow with tau forces eps ~ e^{-mLk}, which
destroys the pigeonhole count. Dead end.

## 4. The suggested approach (volume growth, currents): where it stops
- Kozlovski's formula (C^inf, cited from memory) is h_top(f) = lim_n (1/n) log int_M ||Lambda Df^n(x)|| dnu(x). With
  Yomdin's v(f) <= h_top(f) (C^inf) and Newhouse's h_top(f) <= v(f) (C^{1+alpha}), positive entropy gives a k-form
  omega with ||g_t^* omega||_{L^1} ~ e^{ht}.
  - The Laplace transform C_z = int_0^inf e^{-zt} g_t^* omega dt converges for Re z > h and satisfies
    L_X C_z = z C_z - omega.
  - The Patterson normalisation near the abscissa gives a nonzero current C with L_X C = hC, h > 0. Block R4-q10
    Lemma C gives the same thing via conformal measures on the Grassmann bundle.
- GH constrains only the eigenvalue 0. The available ways of moving h back to 0 are:
  - (a) Complementary degree. g_t^* on k-forms and on (n-k)-forms are dual under int alpha ∧ beta, so one gets a
    current C' with eigenvalue -h. But C ∧ C' is not defined for general currents. Where it is defined (product
    structure, as in Margulis' construction), it yields an invariant measure. In the volume case this is nu by (O2),
    which is no contradiction: nu may well be the measure of maximal entropy, and is, by unique ergodicity.
  - (b) Closedness. If C is closed, then C = (1/h) d i_X C is exact, which is consistent (R4-q10 noted the same). A
    GH-type statement for closed k-currents with k >= 2 is not available: Lemma B's reduction to functions uses
    k = 1.
  - (c) Contraction with smooth invariant objects. A smooth X-invariant 1-form eta would give w = eta(V) with
    Xw = (h - d) w, again an eigenvalue != 0.

  So the approach reduces to (E1) (no real nonzero eigenvalues of L_X on distributions/currents), which is open.

## 5. Status
**Proved (this answer):**
- Theorem 1 (Section 2): under GH, no ergodic measure of positive entropy has mu(d) != 0. The proof is complete
  modulo the cited normal-form theorem (NF) (stated precisely in 2.1) and standard Pesin / Ledrappier-Young theory.
  Theorem J and Lemma 6.0 were re-checked.
- Proposition 3.2: the infinite-order flatness at z = 0 of pair transforms in the volume-preserving case, showing
  that GH at the spectral point 0 alone cannot exclude asymptotic pairs.

**Consequence:** granting (NF), the [GOAL] is equivalent to (PE0), i.e. to (AP) with lambda = 0. This uses the chain,
Theorem 5.1 and Theorem J of R6-a.

**Open (named):**
- (AP) for lambda = 0, equivalently (PE0); in particular the volume-preserving case "cohomology-free (CF) flows have
  zero entropy";
- the sufficient statements (OS) (one-sided decay) and (E1) (no real nonzero eigenvalues);
- a self-contained proof of (NF) in the form (NF1)-(NF3) (I cite it from memory).

**Not proved:** the problem's claim in general. It is proved in dim M <= 3 (R6-a Theorem 5.2) and for hyperbolic
measures in all dimensions.

=== END OF ANSWER round11_q8 ===
