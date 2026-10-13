# Answer to round6_q9: claim (Z0-lin)

**Status.** (Z0-lin) is NOT settled here. I prove two new reductions (Propositions 1 and 2) and one consequence (Corollary 3), and I record where each approach stops.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi, and Q_t phi = e^{J_t} (phi o g_t). GH means global hypoellipticity, and dim M >= 2.

## 0. Plan
1. Restate (Z0-lin) as the absence of positive eigen-measures of the transfer generator with a nonzero real eigenvalue (Proposition 1).
2. Use ergodicity of nu (Lemma 0 of R5-b / Lemma 4.1 of R5-e) to pin down the statistics of nu-typical orbits (Proposition 2).
3. Try to produce an orbit with expanding past and contracting future (approach 1 of the brief), so that Lemma C can be applied; record where this stops.

## 1. Proposition 1 (proved; GH is not needed for (a)-(c))

**(a)** {Q_t} is a one-parameter group of operators on C^infinity with generator P:
- Q_s Q_t = Q_{s+t}, because J_s(x) + J_t(g_s x) = J_{s+t}(x);
- d/dt Q_t phi = Q_t P phi = P Q_t phi.

**(b)** Let T be a positive Radon measure with T(1) = 1 and T(P phi) = lambda T(phi) for all smooth phi, with lambda real. Then:
- T(Q_t phi) = e^{lambda t} T(phi) for all t and all bounded Borel phi;
- K := supp T is closed and flow-invariant;
- there are invariant probabilities mu_1 and mu_2 carried by K with mu_1(d) >= lambda >= mu_2(d).

*Proof.*
1. Put F(t) = T(Q_t phi) for smooth phi. By (a), F'(t) = T(P Q_t phi) = lambda F(t), so F(t) = e^{lambda t} T(phi).
2. Both sides of this identity are finite positive-combination measures in phi (namely (g_t)_*(e^{J_t} T) and e^{lambda t} T). They agree on smooth functions, so they agree on bounded Borel functions.
3. Taking phi = 1_U for open U gives T(e^{J_t} 1_{g_t^{-1} U}) = e^{lambda t} T(U). Since e^{J_t} > 0, T(g_t^{-1} U) = 0 if and only if T(U) = 0. Hence K is invariant.
4. Taking phi = 1 gives int_K e^{J_t} dT = e^{lambda t}. So for each t > 0 there is x_t in K with J_t(x_t) >= lambda t.
5. Any weak* limit of the empirical measures (1/t) int_0^t delta_{g_s x_t} ds is an invariant probability mu_1 on K, and mu_1(d) = lim J_t(x_t)/t >= lambda.
6. For t < 0, step 4 gives y_t in K with J_t(y_t) >= lambda t, that is (1/|t|) int_t^0 d(g_s y_t) ds <= lambda. The backward empirical measures then give mu_2 with mu_2(d) <= lambda. ∎

**(c) Equivalence.** The following are equivalent:
- (Z0-lin) fails;
- there is a positive Radon measure T != 0 and a real lambda != 0 with T(P phi) = lambda T(phi) for all smooth phi. Equivalently, u = T/nu >= 0 satisfies Xu = -lambda u.

*Proof.* The forward direction is Proposition 2.2 of [R4-q7]. For the converse, if lambda > 0 then (b) gives mu_1(d) >= lambda > 0; if lambda < 0 then (b) gives mu_2(d) <= lambda < 0. ∎

**(d) Consequence.** (Z0-lin) is exactly the case "positive measures" of (E1). By Corollary 2 of R5-b, any such T is singular with respect to nu. This says no more about whether such a T exists.

## 2. Proposition 2 (statistics of nu-typical orbits; proved under GH)

For x in M let V^+(x) be the set of weak* limit points, as t -> +infinity, of the empirical measures e_t(x) = (1/t) int_0^t delta_{g_s x} ds. Define V^-(x) in the same way with backward time.

**Claim.** There are nonempty compact connected sets V^+ and V^- of invariant probabilities such that V^{+-}(x) = V^{+-} for nu-a.e. x. Moreover:
- V^+ contains measures m with m(d) >= 0 and measures m' with m'(d) <= 0. Hence V^+ contains an invariant m_0 with m_0(d) = 0.
- The same holds for V^-.

*Proof.*
1. **Invariance.** V^+(g_r x) = V^+(x), because the empirical measures of x and of g_r x differ in total variation by at most 2|r|/t.
2. **Connected and compact.** t -> e_t(x) is a continuous curve in the compact metric space of probability measures. The set of limit points at infinity of such a curve is nonempty, compact and connected. Every limit point is invariant.
3. **Almost-everywhere constancy.** Fix a countable family (phi_j) dense in C(M), and a compatible metric on Prob(M). For each finite tuple of indices and each rational vector q, the function
 x -> dist(q, {(m(phi_j))_j : m in V^+(x)})
 is Borel (take the limsup and liminf over rational t of the corresponding continuous expressions). It is bounded after truncation and flow-invariant. By Lemma 4.1 of R5-e (which uses only L1) it is a.e. constant. These countably many functions determine the compact set V^+(x), so V^+(x) = V^+ a.e.
4. **Some m in V^+ has m(d) >= 0.** Suppose instead that sup_{m in V^+} m(d) = -c < 0. Then for nu-a.e. x, J_t(x) <= -ct/2 for all large t. So int_0^infinity e^{J_t(x)} dt < infinity a.e. This contradicts B4 (the Hopf criterion: under GH that integral is infinite nu-a.e.).
5. **Some m' in V^+ has m'(d) <= 0.** Suppose instead that inf_{m in V^+} m(d) = c > 0. Then J_t(x) >= ct/2 eventually, for a.e. x. By Fatou, liminf_t int e^{J_t} dnu = infinity. This contradicts int e^{J_t} dnu = nu(M).
6. **Existence of m_0.** m -> m(d) is continuous on the connected set V^+, so it takes the value 0 there.
7. **Backward version.** Apply the same argument to -X, which is GH by (O4). ∎

**Corollary 3 (proved).** Under GH, suppose some ergodic mu has mu(d) != 0. Then:
- mu is not the only element of V^+, and not the only element of V^-;
- if every ergodic measure has mu(d) != 0, then the m_0 of Proposition 2 is not ergodic. Its ergodic decomposition charges both {mu(d) > 0} and {mu(d) < 0}.

*Proof.* If m_0 were ergodic, then m_0(d) = 0 would contradict the hypothesis of the second item. If m_0 had all ergodic components on one side, m_0(d) = 0 would force all of them to have mu(d) = 0. The first item follows from Proposition 2, since mu(d) != 0 but V^+ contains measures of both signs. ∎

So, if (Z0-lin) fails, typical orbits spend comparable stretches of time near volume-expanding and near volume-contracting invariant measures, with Cesaro balance 0 along some subsequence of times.

## 3. Where approach 1 stops

Lemma C kills any single orbit x with limsup_{t->+infinity} J_t(x)/t < 0 and limsup_{t->-infinity} J_t(x)/|t| < 0. For example, take an orbit with V^-(x) = {mu_+}, where mu_+(d) > 0, and V^+(x) = {mu_-}, where mu_-(d) < 0. Proposition 2 shows that nu-typical orbits are not of this kind: their limit sets contain measures of both signs in each time direction.

To find a special orbit going from mu_+ to mu_- one needs a connecting mechanism:
- shadowing or specification;
- or Pesin theory, giving stable and unstable manifolds of mu_- and mu_+ that intersect.

Without hyperbolicity no such mechanism is available. With hyperbolicity this is Proposition 4.0 and Theorem 4.1 of R5-d. Density of nu-typical orbits gives only topological recurrence, not exponential asymptotics. Lemma D needs only limsup <= 0, but its conclusion (a dense orbit) is consistent with Proposition 2. So the gap is the same as in the previous rounds: GH has to be used beyond L1 and positive measures. Lemma 5.1 of R5-d shows that smearing positive conformal weights never produces a contradiction.

I also attempted to rule out the eigen-measure T of Proposition 1(c) directly:
- **Dual estimate (O1).** It only says that T - nu^ lies in the range of L_X on distribution densities. That holds for every mean-zero density, so it carries no information.
- **Resolvents of Q_t applied to smooth densities.** These reduce to Lemma 5.1 of R5-d: the result is either smooth or infinite almost everywhere.

Neither gives a contradiction.

## 4. Summary

**Proved:**
- Proposition 1: (Z0-lin) holds if and only if there is no positive eigen-measure of P with a nonzero real eigenvalue. Every such eigenvalue lies in [min_K mu(d), max_K mu(d)] over measures on its support K, which is invariant.
- Proposition 2: nu-typical orbits have a.e.-constant connected empirical limit sets V^{+-}. Each contains invariant measures with mu(d) >= 0, with mu(d) <= 0, and with mu(d) = 0.
- Corollary 3.

**Open:**
- (Z0-lin) itself.
- Equivalently, (E1) for positive measures.
- Whether GH forces an orbit going from an expanding to a contracting ergodic measure in the absence of hyperbolicity.

=== END OF ANSWER round6_q9 ===
