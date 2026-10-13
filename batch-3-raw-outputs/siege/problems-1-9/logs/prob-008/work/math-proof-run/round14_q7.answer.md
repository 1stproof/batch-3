# round14_q7: answer

## 0. Plan and outcome

Target: the missing statement (SC) of the query file. It is GH-free: for every smooth flow and every g_1-ergodic mu with
h_mu(g_1) > 0 and int J_1 dmu = 0, it asks for a point x_0 and two summable su-chains from x_0 satisfying (L1)-(L4), with
weak-stable endings (E) and orbit-isolated vertices.

**Outcome (stated at the outset).**
- **(SC) is NOT proved in general.** I also found no counterexample.
- **Proved here, modulo standard Pesin theory cited from memory (Section 2):**
  - Theorem A: (SC) holds for every *hyperbolic* mu, i.e. one whose only zero Lyapunov exponent is the simple exponent of
    the flow direction. The two chains are finite, of the shortest possible form x_0 -u-> h -s-> g_tau x_0, so each is a
    "homoclinic point of the recurrent orbit of x_0".
  - Corollary A1: (SC) holds when dim M <= 3. In dimension 2 its hypothesis is never met; in dimension 3 every such mu is
    hyperbolic.
  - Theorem A': a stronger GH-free statement. The *conclusion* of (SC) holds for a flow as soon as it has some hyperbolic
    g_1-ergodic measure mu' of positive entropy with |int J_1 dmu'| below its smallest |exponent|. So any counterexample
    to (SC) must have no such measure at all.
- **Proved, elementary:** Proposition 4.1, an abstract criterion (HOM) that needs no Pesin theory. Two distinct
  non-trivial exponential homoclinic points of the orbit of a two-sided recurrent point with sub-theta Jacobian growth
  already give the conclusion of (SC).
- **These partial results do not answer the question.** By Theorem 5.1 of Block R6-a, GH already excludes
  positive-entropy hyperbolic measures. The open, relevant case is non-hyperbolic mu, where (SC) needs exact closing in
  the extra centre directions. Section 5 explains precisely why the method stops there. It also checks three model
  classes (sketches only) in which (SC) holds, which is why I could not produce a counterexample.
- **The chain.** I checked that the hypotheses of Theorem IC2, as quoted, are exactly the conclusion of (SC), and I found
  no flaw in steps 1-4. I did not re-verify entry 113 (step 2).

Conventions are those of the query file: nu is a smooth positive density, d = div_nu X, and J_t(x) = int_0^t d(g_s x) ds,
so that J_{t+r}(x) = J_r(x) + J_t(g_r x). L_tau := max_{|rho| <= tau} Lip(g_rho).

## 1. Elementary lemmas (fully proved, no Pesin theory)

**Definition.** For a, b in M write a ~s b if d(g_t a, g_t b) -> 0 as t -> +inf, and a ~u b if this holds as t -> -inf.
Both are equivalence relations. They are flow-equivariant: a ~s b implies g_r a ~s g_r b for every real r, because
d(g_t g_r a, g_t g_r b) = d(g_{t+r} a, g_{t+r} b). The same holds for ~u.

**Lemma 1.1 (typical points).** Let mu be g_1-invariant and g_1-ergodic with h_mu(g_1) > 0. Then:
(a) mu(Zero(X)) = 0;
(b) mu-a.e. point is not flow-periodic;
(c) for every Borel A with mu(A) > 0 and mu-a.e. z in A: for every delta > 0 there are infinitely many integers n >= 1,
and infinitely many integers n <= -1, with g_n z in A ∩ B(z, delta);
(d) for mu-a.e. z with X(z) != 0, lim_{n -> +-inf} (1/n) log|X(g_n z)| = 0. So X(z) spans an Oseledets direction with
exponent 0.

*Proof.*
(a) Zero(X) is closed and g_1-invariant, so mu(Zero(X)) is 0 or 1. If it is 1, then g_1 = id mu-a.e. and h_mu(g_1) = 0.
(b) Let Y be the set of non-zero periodic points. It is Borel and g_1-invariant, and the minimal period p(z) is a Borel
g_1-invariant function on Y. Suppose mu(Y) = 1. Then p = P a.e. by ergodicity. The map z -> O(z) = g_{[0,P]} z into the
space of compact subsets of M (Hausdorff metric) is continuous and g_1-invariant. A g_1-invariant Borel map into a
separable metric space is a.e. constant for an ergodic measure (preimages of a countable basis are invariant). So mu is
carried by a single periodic orbit O. On O, g_1 is topologically conjugate (via t -> g_{tP} z_0, t in R/Z) to the circle
rotation by 1/P, which has zero topological entropy. By the variational principle h_mu(g_1) = 0, a contradiction.
(c) This is Poincare recurrence for g_1 and for g_{-1}, applied to A ∩ B_j for each ball B_j of a countable basis and
discarding countably many null sets.
(d) By Oseledets the limits exist for the vector X(z) for a.e. z, and Dg_n X(z) = X(g_n z). Since |X| is bounded, the
limit as n -> +inf is <= 0. If it were < 0, then |X(g_n z)| -> 0. But apply (c) to A_q = {|X| > q} for every rational
q > 0. For a.e. z with X(z) != 0, taking a rational q < |X(z)| gives n_k -> inf with |X(g_{n_k} z)| > q > 0. The case n -> -inf is the same. ∎

**Lemma 1.2 (asymptotic rigidity).** Let z be neither a zero of X nor periodic, and forward recurrent: g_{t_k} z -> z for
some t_k -> +inf. If g_s z ~s z for some real s, then s = 0. The same holds with "backward recurrent" and ~u.

*Proof.* We have g_{t_k + s} z = g_s(g_{t_k} z) -> g_s z by continuity of g_s. Also d(g_{t_k+s} z, g_{t_k} z) -> 0 by the
hypothesis g_s z ~s z. Hence g_s z = lim g_{t_k} z = z. Since z is neither a zero nor periodic, s = 0. ∎

**Corollary 1.3.** If z is as in Lemma 1.2 in both time directions, then for real s, s': g_s z ~s g_{s'} z implies s = s',
and g_s z ~u g_{s'} z implies s = s'.
*Proof.* Apply g_{-s'} (equivariance), then Lemma 1.2. ∎

**Lemma 1.4 (Jacobian transfer).** If d(g_t a, g_t b) <= C e^{-theta t} d(a,b) for all t >= 0, then
|J_t(a) - J_t(b)| <= Lip(d) C d(a,b)/theta for all t >= 0. The same holds for t <= 0 under the backward hypothesis.
*Proof.* |J_t(a) - J_t(b)| <= int_0^t |d(g_s a) - d(g_s b)| ds <= Lip(d) C d(a,b) int_0^inf e^{-theta s} ds. ∎

**Lemma 1.5 (Egorov control).** Let mu be g_1-ergodic and lambda := int J_1 dmu. For every eta > |lambda| there are a
compact K_0 with mu(K_0) > 1/2 and a constant C_0 such that J_t(z) <= C_0 + eta|t| for all z in K_0 and all real t.
*Proof.* J_n = sum_{k=0}^{n-1} J_1∘g_k for n >= 1, and J_{-n} = -sum_{k=1}^{n} J_1∘g_{-k}. Birkhoff's theorem for g_1 and
for g_{-1} gives J_n(z)/n -> lambda as n -> +-inf, for mu-a.e. z. By Egorov there are a compact K_0 with
mu(K_0) > 1/2 and an N such that |J_n(z) - lambda n| <= (eta - |lambda|)|n| for |n| >= N and z in K_0; hence
J_n(z) <= eta|n| there. For |n| < N, |J_n| <= N||d||_inf. Finally |J_t - J_{floor(t)}| <= ||d||_inf, so
C_0 := (N+1)||d||_inf works. ∎

## 2. Pesin theory used (cited from memory; standard; the same facts as Block R13-c Lemma 1.2 and the availability remark of Theorem IC, plus local product structure)

Setting: mu is g_1-ergodic with h_mu(g_1) > 0. By Ruelle's inequality for g_1 and for g_{-1} it has a smallest positive
exponent chi^+_min > 0 and a largest negative exponent chi^-_max < 0. Fix 0 < theta < min(chi^+_min, |chi^-_max|).
Write E^s(z) and E^u(z) for the sums of the Oseledets spaces with negative and positive exponents.

**(P1) Pesin blocks [cited].** For every eps_0 > 0 there are a compact Lambda with mu(Lambda) > 1 - eps_0 and constants
r > 0 and C_Lambda >= 1 with the following properties. Every z in Lambda has local manifolds W^s_r(z) and W^u_r(z):
embedded C^1 discs through z, tangent at z to E^s(z) and E^u(z), depending continuously on z in Lambda in the C^1
topology. For y, y' in W^s_r(z) and n >= 0, d(g_n y, g_n y') <= C_Lambda e^{-theta n} d(y, y'). For y, y' in W^u_r(z)
and n >= 0, d(g_{-n} y, g_{-n} y') <= C_Lambda e^{-theta n} d(y, y'). The Oseledets splitting is continuous on Lambda,
with angles bounded below.
Interpolation: for real t = n + rho >= 0 with rho in [0, 1), d(g_t y, g_t y') <= L_1 d(g_n y, g_n y'). So on W^s_r(z),
d(g_t y, g_t y') <= C_1 e^{-theta t} d(y,y') for t >= 0, with C_1 := L_1 C_Lambda e^{theta}. The same holds backwards on
W^u_r(z).

**(P2) Local product structure, hyperbolic case [cited; e.g. the set-up of Katok's closing lemma for flows].** Assume
moreover that mu is *hyperbolic*: the zero exponent is simple. By Lemma 1.1(d) its Oseledets space is then R X(z), so
T_z M = E^u(z) ⊕ E^s(z) ⊕ R X(z) a.e. Take Lambda as in (P1) and, by Lemma 1.1(a), contained in {|X| >= c} for some
c > 0. Then there are eps in (0, 1/4] and delta > 0 such that for z, z' in Lambda with d(z, z') < delta,
 W^u_r(z) ∩ g_{[-eps, eps]}(W^s_r(z')) != ∅.
*Reason (standard).* Work in a chart at z. W^u_r(z) is the graph over an E^u(z)-disc of a C^1 map with small Lipschitz
constant. The map (sigma, w) -> g_sigma w on [-eps, eps] × W^s_r(z') is a C^1 embedding whose image is a graph over a
disc in R X(z) ⊕ E^s(z), again of small Lipschitz constant. All of this is uniform on Lambda, by continuity of the
plaques, of E^s and of X, and because the angles are bounded below. Two such graphs over complementary subspaces, with
radii large compared with d(z, z'), meet in exactly one point (contraction mapping). Only existence is used below.

## 3. Theorem A: (SC) for hyperbolic measures

**Theorem A.** Let M be compact and connected with dim M = n >= 2, and X a smooth vector field. Let mu be g_1-invariant
and g_1-ergodic, with h_mu(g_1) > 0, int J_1 dmu = 0, and mu hyperbolic in the sense of (P2). Then the conclusion of (SC)
holds. In fact, for any theta in (0, min(chi^+_min, |chi^-_max|)) and any eta in (0, theta), there are x_0 and two
finite chains
 (a_i) = (x_0, h_a, p_a, p_a, p_a, ...),  (b_i) = (x_0, h_b, p_b, p_b, ...),  p_k = g_{tau_k} x_0 (k = a, b),
with tau_a != tau_b, such that (L1)-(L4) and (E) hold, with h_a and h_b as the orbit-isolated vertices.

*Proof.*
**Step 0 (choice of sets).** Fix theta as stated and eta in (0, theta). (SC) only asks for some eta in [0, theta), so
eta > 0 is no loss.
- Lemma 1.5 with lambda = 0 gives K_0 and C_0.
- (P1) and (P2) give Lambda (with mu(Lambda) > 1/2, contained in {|X| >= c}), r, C_1, eps and delta.
- Let G be the full-measure set of points that are not zeros, not periodic, and recurrent forwards and backwards along
  integer times (Lemma 1.1(a)-(c)).
- Put K := Lambda ∩ K_0 ∩ G. Then mu(K) > 0.

**Step 1 (base point and two returns).** By Lemma 1.1(c) applied to A = K, choose x_0 in K and integers 1 <= n_a < n_b
with y_k := g_{n_k} x_0 in K and d(x_0, y_k) < delta (k = a, b).

**Step 2 (the homoclinic points).** By (P2) with z = x_0 and z' = y_k, choose
 h_k in W^u_r(x_0) ∩ g_{[-eps,eps]}(W^s_r(y_k)), and write h_k = g_{sigma_k} w_k with w_k in W^s_r(y_k), |sigma_k| <= eps.
Put tau_k := n_k + sigma_k and p_k := g_{tau_k} x_0 = g_{sigma_k} y_k. Since n_b - n_a >= 1 > 2 eps >= |sigma_a - sigma_b|,
we get tau_a != tau_b. Also tau_k >= 1 - eps > 0.

**Step 3 ((L1)-(L3), (E)).** Consider the chain (a_i); chain (b_i) is the same.
- (L1), i = 0: h_a and x_0 both lie in W^u_r(x_0), so d(g_t x_0, g_t h_a) <= C_1 e^{-theta|t|} d(x_0, h_a) for t <= 0.
  For i >= 1 the u-legs (p_a, p_a) have length 0.
- (L2), i = 0: the leg is (h_a, p_a) = (g_sigma w, g_sigma y), with sigma = sigma_a, w = w_a, y = y_a, and w, y in W^s_r(y).
  - If t >= 0 and t + sigma >= 0: d(g_t h_a, g_t p_a) = d(g_{t+sigma} w, g_{t+sigma} y) <= C_1 e^{-theta(t+sigma)} d(w,y)
    <= C_1 e^{theta eps} L_eps e^{-theta t} d(h_a, p_a), using d(w,y) = d(g_{-sigma} h_a, g_{-sigma} p_a) <= L_eps d(h_a, p_a).
  - If 0 <= t < -sigma <= eps: d(g_t h_a, g_t p_a) <= L_eps d(h_a, p_a) <= L_eps e^{theta eps} e^{-theta t} d(h_a, p_a).
  - For i >= 1 the s-legs have length 0.
- (L3) is trivial (finitely many non-zero legs), and the limit point is p_a.
- (E): d(g_t p_a, g_{t + tau_a} x_0) = 0 for all t.
So (L1)-(L3) and (E) hold with C := C_1 e^{theta eps} L_eps (>= 1 after enlarging).

**Step 4 ((L4)).** All constants below depend only on the finitely many chosen points.
- x_0 in K_0, so J_t(x_0) <= C_0 + eta|t| for all t. This covers a_0 (t <= 0) and the extra condition on x_0 (t >= 0).
- a_{2i} = p_a for i >= 1, t <= 0: J_t(p_a) = J_{t+tau_a}(x_0) - J_{tau_a}(x_0) <= C_0 + eta|t| + eta tau_a + |J_{tau_a}(x_0)|.
- a_{2i+1} = p_a for i >= 1, t >= 0: the same bound.
- a_1 = h_a, t >= 0: J_t(h_a) = J_{t+sigma}(w) - J_sigma(w), and |J_sigma(w)| <= eps ||d||_inf.
  - If t + sigma >= 0, Lemma 1.4 on W^s_r(y_a) gives J_{t+sigma}(w) <= J_{t+sigma}(y_a) + Lip(d) C_1 diam(M)/theta.
  - If t + sigma < 0, then |t + sigma| <= eps and |J_{t+sigma}(w) - J_{t+sigma}(y_a)| <= 2 eps ||d||_inf.
  - Finally J_{t+sigma}(y_a) = J_{t+sigma+n_a}(x_0) - J_{n_a}(x_0) <= C_0 + eta(t + eps + n_a) + |J_{n_a}(x_0)|.
So (L4) holds with eta and a common C' (the maximum of the finitely many constants, over both chains).

**Step 5 (orbit-isolated vertices).** We use Corollary 1.3 for x_0 (x_0 is in G). Note that h_k ~u x_0 (Step 3, (L1)) and
h_k ~s p_k = g_{tau_k} x_0 (Step 3, (L2)).
(i) *h_k != x_0.* Otherwise x_0 ~s g_{tau_k} x_0, so tau_k = 0 by Corollary 1.3, contradicting tau_k > 0.
(ii) *O(h_k) ∩ O(x_0) = ∅.* If h_k = g_s x_0, then g_s x_0 ~u x_0, so s = 0 and h_k = x_0, contradicting (i). Hence the
orbit of h_k contains none of x_0, p_a, p_b. In particular it contains neither limit point, and h_k is not in
{x_0, p_a, p_b}.
(iii) *h_b is not on O(h_a).* If h_b = g_s h_a, then x_0 ~u h_b = g_s h_a ~u g_s x_0, so s = 0 and h_a = h_b. Then
g_{tau_a} x_0 ~s h_a = h_b ~s g_{tau_b} x_0, so tau_a = tau_b, contradicting Step 2. The relation is symmetric, so h_a is
not on O(h_b) either.
(iv) *h_k is neither a zero nor periodic.* Otherwise O(h_k) is compact. Choose integers m_j -> +inf with g_{-m_j} x_0 -> x_0
(x_0 is in G). Since h_k ~u x_0, d(g_{-m_j} h_k, g_{-m_j} x_0) -> 0, so g_{-m_j} h_k -> x_0, and x_0 lies in the closure
of O(h_k), which is O(h_k). This contradicts (ii).
(v) *Counting.* The combined vertex list is x_0, h_a, p_a (repeated), x_0, h_b, p_b (repeated). By (ii) and (iii), h_a
occurs exactly once, and its orbit contains no other vertex and neither p_a nor p_b. The same holds for h_b.
So h_a and h_b are orbit-isolated vertices, different from x_0. ∎

**Remark 3.1 (what Theorem A shows under GH).** Combined with Theorem IC2 (Block R13-a), Theorem A re-proves the
following without Katok's horseshoe theorem: *under GH, no hyperbolic g_1-ergodic mu with h_mu > 0 has int J_1 dmu = 0.*
Theorem A' extends this to |int J_1 dmu| < min(chi^+_min, |chi^-_max|). Only Pesin local product structure and
recurrence are used. This is weaker than Theorem 5.1 of Block R6-a, which needs no condition on mu(d). It adds nothing to
the problem, because the relevant measures (entry 113 plus Theorem 5.1) are non-hyperbolic with mu(d) = 0.

**Corollary A1 ((SC) in dimension <= 3).** If dim M <= 3, (SC) holds.
*Proof.* Let mu be as in (SC). By Lemma 1.1(d) the flow direction carries the exponent 0. Ruelle's inequality for g_1 and
for g_{-1} (h_mu(g_{-1}) = h_mu(g_1) > 0) gives a positive and a negative exponent. If n = 2 there is only one further
exponent, which cannot be both positive and negative, so no such mu exists and (SC) is vacuous. If n = 3 the exponents
are chi^+ > 0 = 0 > chi^-, each simple, so mu is hyperbolic and Theorem A applies. ∎

**Theorem A' (a GH-free strengthening; the measure need not be the given one).** Let X be a smooth vector field on M
(n >= 2). Suppose the flow has a g_1-ergodic mu' with h_{mu'}(g_1) > 0, hyperbolic in the sense of (P2), with
lambda' := int J_1 dmu' satisfying |lambda'| < min(chi^+_min(mu'), |chi^-_max(mu')|). Then the conclusion of (SC) holds:
there are x_0 and two chains with (L1)-(L4), (E) and orbit-isolated vertices.
*Proof.* Repeat the proof of Theorem A for mu', choosing theta and eta with |lambda'| < eta < theta <
min(chi^+_min, |chi^-_max|). Lemma 1.5 applies with this eta, and nothing else changes. ∎

*Consequence.* A counterexample to (SC) must be a flow with no hyperbolic positive-entropy ergodic measure whose |mu'(d)|
is below its smallest |exponent|. For volume-preserving flows (d = 0 for the invariant density) this means no hyperbolic
positive-entropy measure at all. In particular, by Smale-Birkhoff, it means no transverse homoclinic point of any
hyperbolic periodic orbit.

## 4. The abstract criterion behind Theorem A (fully proved, no Pesin theory)

**Proposition 4.1 (criterion (HOM)).** Let theta > 0 and eta in [0, theta). Let x_0 be neither a zero nor periodic, be
recurrent forwards and backwards, and satisfy J_t(x_0) <= C_0 + eta|t| for all real t. Suppose there are two distinct
points h_a != h_b, both different from x_0, and reals tau_a, tau_b, with, for k = a, b:
 d(g_t x_0, g_t h_k) <= C e^{-theta|t|} (t <= 0)  and  d(g_t h_k, g_{t+tau_k} x_0) <= C e^{-theta t} (t >= 0).
Then the conclusion of (SC) holds, with the chains (x_0, h_k, g_{tau_k} x_0, g_{tau_k} x_0, ...).
(tau_a = tau_b is allowed.)

*Proof.* Put p_k := g_{tau_k} x_0.
- As in Step 5(ii) of Theorem A: if h_k = g_s x_0 then g_s x_0 ~u x_0, so s = 0 by Lemma 1.2, a contradiction. So
  O(h_k) ∩ O(x_0) = ∅, and in particular h_k != p_k and d(h_k, p_k) > 0.
- Hence (L1) and (L2) hold with the length factor, after replacing C by C / min_k min(d(x_0, h_k), d(h_k, p_k)).
- (E) is trivial, and (L3) is too.
- (L4): at x_0 by hypothesis; at p_k by the cocycle identity, as in Step 4; at h_k (t >= 0) by Lemma 1.4 in the form
  |J_t(h_k) - J_t(p_k)| <= Lip(d) C/theta.
- Orbit isolation: (ii) above. If h_b = g_s h_a then x_0 ~u h_b ~u g_s x_0, so s = 0 and h_a = h_b, which is excluded.
  Non-periodicity is (iv) of Theorem A. The counting is as in (v). ∎

So (SC) follows from the existence of a two-sided recurrent point, with sub-theta Jacobian growth, whose orbit has two
distinct non-trivial *exponential homoclinic points*: points h in W^u_theta(x_0) ∩ W^s_theta(O(x_0)). Theorem A is the
statement that hyperbolic mu gives (HOM) through local product structure and recurrence.

## 5. The non-hyperbolic case: where the argument stops, and why I found no counterexample

### 5.1 The obstruction (precise)
Let mu be as in (SC) with c >= 1 zero exponents transverse to X. This is the case that matters: under GH, Theorem 5.1 of
R6-a forces it. Put u = dim E^u and s = dim E^s, so n = u + s + 1 + c.
- A homoclinic point as in (HOM) lies in W^u(x_0), of dimension u, and in the weak-stable set of the orbit,
  ∪_tau W^s(g_tau x_0), which is locally of dimension s + 1.
- Their dimensions add up to n - c < n. So for a recurrent x_0 the local intersection W^u_r(x_0) ∩ g_{[-eps,eps]} W^s_r(y)
  (y = g_n x_0 close to x_0) is generically empty. Step 2 of Theorem A has no analogue.
- Chains with more legs move the endpoint in the u- and s-directions freely, but in the c centre directions only through
  su-holonomy defects.
- So any proof of (SC) for non-hyperbolic mu must produce *exact* closing in the centre, either by finite chains or in the
  limit of summable infinite chains (Proposition CP of Block R13-a).
- On a Pesin block the admissible vertices form a fractal set. Leaves depend only Hölder-continuously on their base
  points, and the closing point is non-generic. So neither the intermediate value theorem nor a first-order bracket
  expansion is available.
- I could not overcome this. It is exactly the gap (ii) of Proposition CP ("centre steering at all scales, or exact
  closing").

### 5.2 Three model classes in which (SC) holds (sketches, not full proofs)
These cover the uniform versions of both branches of the planner's dichotomy, jointly integrable (M1, M2) and
non-integrable (M3). That is why I could not build a counterexample.
- **(M1)** The suspension (roof 1) of A × R_alpha on T^2 × T^1, with A a hyperbolic automorphism and alpha irrational.
  - It preserves volume, so d = 0 and (L4) is automatic. Lebesgue measure has positive entropy and an extra zero exponent.
  - Take x_0 = (z_0, phi_0, s_0) generic. The lifts of W^u_A(z_0) and of W^s_A(z_0) + k (k in Z^2) are lines of
    irrational slope meeting once each. This gives infinitely many distinct homoclinic points z of z_0 under A.
  - h = (z, phi_0, s_0) satisfies h ~u x_0 and h ~s x_0 exponentially, with tau = 0.
  - Proposition 4.1 applies. (This is also the sanity example of Block R13-b.)
- **(M2)** Suspensions of skew products (z, phi) -> (A_phi z, phi + alpha) on T^2 × T^1, with A_phi C^1-close to a
  hyperbolic automorphism.
  - The phi-coordinate is preserved along exponentially asymptotic pairs.
  - In the fibre over phi_0, the non-autonomous composition of the maps A_{phi_0 + k alpha} has stable and unstable
    laminations given by invariant cone fields. Their lifts are graphs over the e_s- and e_u-lines and meet once for
    each lattice translate.
  - This gives infinitely many exponential homoclinic points of x_0 in the same fibre, so (HOM) holds. (Sketch; the
    non-autonomous stable manifold theorem is used without proof.)
- **(M3)** (Contact Anosov flow on N^3) × (linear flow on T^2 with direction alpha, alpha_1/alpha_2 irrational).
  - Legs preserve the T^2-coordinate, and (E) then forces tau alpha in Z^2, so tau = 0.
  - So one needs base su-chains returning exactly into W^{ss}(z_0) with zero total temporal displacement.
  - A small su-quadrilateral with side parameters (a, b) has temporal displacement T(a, b), continuous, vanishing on the
    axes, and of sign sgn(ab) for small a, b != 0 (non-integrability of the contact flow).
  - Run a first small quadrilateral, then a second one based at its endpoint with the opposite sign. The intermediate
    value theorem in the second side parameter gives total displacement 0 exactly, a finite chain ending in
    W^{ss}(z_0), and an isolated vertex (generic choices avoid orbit coincidences). Sketch only.

### 5.3 What a counterexample would have to look like
By Theorem A' and 5.2, a counterexample flow would have the following properties:
- (i) no hyperbolic positive-entropy ergodic measure with |mu'(d)| below its smallest |exponent|;
- (ii) a non-hyperbolic positive-entropy mu with mu(d) = 0, whose su-structure admits no exact centre closing, finite or
  in the limit, from ANY base point of M. Note that (SC) lets x_0 be any point of M, not only a mu-typical one.
- (iii) This must hold even though su-paths can be concatenated arbitrarily, and loops of opposite orientation have
  centre defects of opposite sign (Block R13-a, the remark after Proposition CP).
I know of no construction with these properties. Herman-type positive-entropy minimal diffeomorphisms are skew products of
type (M2) and satisfy (HOM).

## 6. Check of the chain (steps 1-4 of the query file)
- Step 4 (Theorem IC2, Block R13-a, as quoted in the query file). Its hypotheses are, verbatim, the conclusion of (SC):
  - two summable chains from a common x_0 with the same constants (C, theta);
  - (L4) with the same eta < theta, including J_t(x_0) <= C' + eta t for t >= 0, which IC2 uses in step 1 to bound E_k;
  - weak-stable endings with arbitrary tau_1, tau_2;
  - orbit-isolated vertices.
  I read its proof (the two cases psi_1 = 0 and psi_1, psi_2 != 0, the group-ring cancellation, and the non-vanishing at
  the orbit-isolated vertex) and found no gap. GH enters only through Theorem J.
- Step 1 (variational principle and Jacobs) is standard. I did not re-verify step 2 (entry 113).
- So, granted entry 113, (SC) implies the problem's claim. Theorem A / Corollary A1 prove (SC) only in cases (hyperbolic
  mu; dim <= 3) that the earlier rounds had already settled for the problem (Theorems 5.1 and 5.2 of R6-a). **The chain
  therefore remains incomplete exactly at the non-hyperbolic case of (SC).**

## 7. Status

**Proved (complete proofs above, modulo the cited Pesin facts (P1), (P2), Ruelle's inequality and the variational
principle):**
1. Lemmas 1.1-1.5 (elementary, including the asymptotic-rigidity Lemma 1.2: a non-periodic recurrent orbit has no
   non-trivial self-asymptotic translates).
2. Proposition 4.1: criterion (HOM) for the conclusion of (SC), with no Pesin theory.
3. Theorem A: (SC) for hyperbolic mu, with two-leg chains x_0 -u-> h -s-> g_tau x_0.
4. Corollary A1: (SC) for dim M <= 3.
5. Theorem A': the conclusion of (SC) for any flow carrying a hyperbolic positive-entropy measure mu' with
   |mu'(d)| < min |exponent|.
6. Remark 3.1: with Theorem IC2, a horseshoe-free proof that under GH a hyperbolic positive-entropy measure cannot have
   |mu(d)| < min |exponent| (weaker than the known Theorem 5.1; no new consequence for the problem).

**Sketched only:** the model classes (M1)-(M3), in which (SC) holds.

**Not proved / open:**
- (SC) for non-hyperbolic mu (necessarily dim M >= 4), hence the problem's claim by this chain.
- Open question Q1 (finite version): for a g_1-ergodic, non-hyperbolic mu with h_mu > 0 and mu(d) = 0 (already in the
  volume-preserving case), is there a two-sided recurrent point whose orbit has two distinct exponential homoclinic points
  (criterion (HOM))?
- Open question Q2 (infinite version): failing Q1, the centre-steering property (ii) of Proposition CP on Pesin blocks, or
  a proof that its failure forces exact closing.
- No counterexample to (SC) was found. Section 5.3 lists what one would require.

=== END OF ANSWER round14_q7 ===
