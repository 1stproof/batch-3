# round7_q1: answer (partial result; (PE-NH) NOT settled)

## 0. Plan and status
Target: (PE-NH): under GH, no ergodic flow-invariant mu has h_mu(g_1) > 0 together with a transverse zero exponent.
Outcome: I could not prove (PE-NH), and I found no counterexample. What this file contains:
- §1: a check of the chain. Its logic is correct, modulo the cited theorems.
- §2: a new proposition, proved modulo the cited Ledrappier–Young intermediate-entropy theory. It strengthens Prop 6.1 (entry 62) for lambda = mu(d) != 0: a surviving measure with lambda != 0 must carry all its entropy in exponents of size at most |lambda|. In particular |lambda| >= h_mu/(n-2).
- §3: a proved structural observation. In the volume-preserving case, every ingredient that Theorem J uses is implied by "distributional unique ergodicity" (DUE), which is strictly weaker than GH. So any proof of (PE0) that only produces a Theorem-J distribution S (the planner's conjecture (C), routes (i)–(iii)) would also prove that DUE volume-preserving C^inf flows have zero entropy. I do not know whether that statement is true. This suggests that the closed-range / tame part of GH must enter.
- §4: where the argument stops, and the open questions.

## 1. The chain
Steps 2–4 are logically correct. I re-checked Theorem J (moments, Jordan chain via F1/F2, Fourier uniqueness on the strip), Lemma K, Corollary 4.2, Theorem 5.1 and the variational-principle reduction (step 4). They depend on two citations:
- the flow horseshoe theorem (Katok; Lian–Young) for hyperbolic ergodic measures of C^2 flows with mu(Zero X) = 0;
- Ruelle's inequality.
I found no flaw. The only missing link is step 1, (PE-NH).

## 2. Proposition N (intermediate unstable foliations): a sharper exclusion when lambda != 0

**Cited [LY-II]** (Ledrappier–Young, Ann. Math. 122 (1985), Part II, from memory).
Setting: f a C^2 diffeomorphism of a compact manifold, mu an f-ergodic probability, distinct positive exponents l_1 > l_2 > ... > l_u > 0 with multiplicities m_k. For each i there is:
- the i-th unstable lamination W^{(i)}, whose leaves are C^1 immersed and tangent to E_1 + ... + E_i, with W^{(i)}(x) = {y : limsup (1/m) log d(f^{-m}x, f^{-m}y) <= -l_i};
- a measurable partition xi_i, subordinate to W^{(i)} and increasing (xi_i refines f xi_i);
- the entropy h_i := H_mu(xi_i | f xi_i), which does not depend on the choice of xi_i.
These satisfy h_u = h_mu(f) and h_i - h_{i-1} = l_i gamma_i, where 0 <= gamma_i <= m_i (h_0 = 0). In addition, for every delta > 0 and a.e. x, each y in xi_i(x) satisfies d(f^{-m}x, f^{-m}y) <= C(x, delta) e^{-(l_i - delta)m} for m >= 0 (Pesin, local i-th unstable manifolds).

**Lemma 6.0' (proved).** If h_i > 0, then the conditional measures of mu on xi_i are non-atomic for a.e. x.
*Proof.* This is the proof of Lemma 6.0 word for word. That proof uses only that xi_i is increasing and that H(xi_i | f xi_i) > 0. ∎

**Proposition N.** Assume GH. Let mu be ergodic and flow-invariant, with h := h_mu(g_1) > 0 and lambda := mu(d). Let the positive exponents of g_1 be l_1 > ... > l_u with multiplicities m_k.
(a) If lambda < 0, then h = sum over {k : l_k <= |lambda|} of l_k gamma_k, which is at most sum over {k : l_k <= |lambda|} of l_k m_k.
(b) If lambda > 0, the same holds with the negative exponents: h = sum over {k : |r_k| <= lambda} of |r_k| gamma^s_k, where gamma^s_k are the stable-side Ledrappier–Young dimensions (Ledrappier–Young applied to g_{-1}).
(c) Consequently, if lambda != 0 then |lambda| >= h/(n-2), where n = dim M.

*Proof.*
(a) Suppose the conclusion fails. Since h = sum_k l_k gamma_k, some k with l_k > |lambda| has gamma_k > 0. Let i be the largest index with l_i > |lambda|. Then h_i = sum_{k<=i} l_k gamma_k > 0. Fix delta > 0 with lambda + delta < 0 and l_i - delta > |lambda| + 2 delta.
- *Choice of the pair.* Let G be the set of z with J_t(z)/t -> lambda as t -> +-inf; by Birkhoff, mu(G) = 1. By Lemma 6.0', for a.e. x we have x in G and the conditional mu^{xi_i}_x is non-atomic and carried by G. So there is y in G ∩ xi_i(x) with y != x. Then d(g_{-m}x, g_{-m}y) <= C e^{-(l_i - delta)m}. Interpolating over s in [0,1] with the Lipschitz constant of g_{-s}, this gives d(g_t x, g_t y) <= C' e^{-theta|t|} for t <= 0, with theta = l_i - delta.
- *The constant b.* As in R5-a Step 4(a), b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists, and |J_t(x) - J_t(y) - b| <= C e^{-theta|t|} for t <= 0. Put S := delta_x - e^b delta_y, which is nonzero.
- *Backward estimate (t <= 0).* |F_phi(t)| <= e^{J_t(x)} ( |phi(g_t x) - phi(g_t y)| + |1 - e^{b + J_t(y) - J_t(x)}| ||phi||_inf ) <= C e^{J_t(x)} e^{-theta|t|} ||phi||_{C^1}. Since x is in G and lambda < 0, J_t(x) <= C + (|lambda| + delta)|t| for t <= 0. Hence |F_phi(t)| <= C e^{-delta|t|} ||phi||_{C^1}.
- *Forward estimate (t >= 0).* Since x and y are in G, |F_phi(t)| <= C e^{(lambda + delta)t} ||phi||_inf.
So (*) of Theorem J holds and S = 0, a contradiction.
(b) Apply (a) to -X. It is GH by (O4), mu is ergodic for -X with the same entropy, its exponents are negated, and its lambda is -lambda.
(c) The flow direction carries the exponent 0, and Ruelle's inequality applied to g_{-1} gives at least one negative exponent. So the positive exponents have total multiplicity at most n - 2. In (a), the sum is then at most |lambda| (n-2). Case (b) is the same. ∎

*Remarks.*
- Proposition N contains Prop 6.1. If l_u = chi^+_min > |lambda|, the index set in (a) is empty, so h = 0.
- It also covers many configurations with higher-dimensional unstable bundles that Prop 6.2 handled only via unverified normal forms: for instance every lambda < 0 whose entropy is not concentrated in exponents of size at most |lambda|.
- It does not cover lambda = 0. The forward estimate needs lambda + delta < 0.

## 3. Structural observation: what Theorem J really uses (proved)

**Observation Q.** Let X preserve a smooth positive density omega. Take nu = omega, so d = 0 and J = 0. Then:
- (F1) is equivalent to DUE: every distribution density T with T(X phi) = 0 for all phi is c omega.
- (F2) holds automatically: put phi = 1 in T(X phi) = c' ∫ phi d omega to get c' = 0.
So Theorem J (and Lemma M) hold for every DUE volume-preserving flow. Its proof uses nothing else.

DUE is strictly weaker than GH plus volume. For example, a Liouville linear flow on T^n is DUE: Fourier coefficients satisfy (i k·alpha) T^_k = 0, so T^_k = 0 for k != 0. Such a flow is not GH.

Moreover, under DUE with volume:
- the flow is uniquely ergodic (an invariant probability is an invariant distribution density), so mu = omega and lambda = 0;
- any hyperbolic positive-entropy measure is impossible (Lemma K and Corollary 4.2 use only Theorem J, plus the periodic-orbit argument; a periodic orbit measure would be a second invariant measure anyway).

**Consequence.** Suppose a proof of (PE0) only constructs a nonzero S satisfying Theorem J's two-sided decay, using nothing else about X (conjecture (C), routes (i)–(iii)). Then the same proof would show that every DUE volume-preserving C^inf flow has zero entropy. I do not know whether that statement is true. If it fails, routes (i)–(iii) cannot work, and a proof of (PE0) must use the closed-range / tame estimate of GH (Text B, Lemma 2), not merely L1.

In the volume case, that estimate gives the following (classical, proved by O2 plus Lemma 2): for every k there are m and C such that every omega-mean-zero smooth f equals Xu with ||u||_{C^k} <= C||f||_{C^m}. Hence the uniform bounded-deviation estimate
|∫_0^T f(g_t x) dt - T omega(f)| <= 2C ||f||_{C^m} for all x and T.
So the volume-preserving core of (PE0) is exactly: "a cohomology-free (with tame estimates) volume-preserving C^inf flow has zero entropy".
- I recall, without being able to verify it, a paper by Flaminio–Paternain (DCDS-A, around 2011) stating that cohomology-free vector fields embed continuously in a linear flow on an abelian group. If that embedding is injective and equivariant, the flow is equicontinuous, and zero entropy follows in the volume case. I do not rely on this.
- Even granted, it says nothing about non-volume GH flows with lambda = 0.

## 4. Where the argument stops; open questions
What is proved under GH (combining earlier entries with §2): every ergodic mu with h_mu(g_1) > 0 is non-hyperbolic (Thm 5.1), and either
- lambda = 0, or
- lambda != 0 with all of its entropy carried by exponents of size at most |lambda| on the relevant side (Prop. N); in particular |lambda| >= h_mu/(n-2).

The problem is proved for dim M <= 3 (Thm 5.2).

**Open:**
(O-a) (PE0): exclude a non-hyperbolic ergodic mu with h > 0 and lambda = 0. This includes the volume-preserving / cohomology-free core.
(O-b) The residual case lambda != 0 with entropy concentrated in exponents of size at most |lambda|. Prop 6.2 handles it for a single simple exponent, as a sketch; in general it needs non-uniform normal forms (Kalinin–Sadovskaya type, not checked).
(O-c) Is "DUE plus volume implies zero entropy" true? If it is false, Theorem-J-only strategies for (O-a) are doomed (§3).

Approaches I checked that give no contradiction at lambda = 0 (cohomology-free volume case):
- *Pair Laplace transforms.* Their Taylor coefficients at z = 0 vanish, with bounds |T_z(f)| <= C_j |z|^j / Re z. Functions such as exp(-z^{-1/2}) show that this does not force T_z = 0.
- *Watson's lemma.* It would need loss of less than one derivative in R = X^{-1}, which is unavailable.
- *Spectral measures.* For smooth f they vanish to infinite order at 0. This is compatible with the Lebesgue spectrum of positive-entropy systems.
- *Center-direction cocycle identities for du.* They are consistent by Atkinson recurrence.

Conclusion: (PE-NH) remains open here, so the problem's claim is not established in dimension >= 4 by this work.

=== END OF ANSWER round7_q1 ===
