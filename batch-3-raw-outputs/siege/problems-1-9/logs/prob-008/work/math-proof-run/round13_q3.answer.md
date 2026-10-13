# round13_q3: answer

## Status (read first)
I could **not** prove (PE0), and I found **no counterexample**. (PE0) therefore stays **open**, and so does the problem's claim along this chain. Below are:
- §1, a check of the chain;
- §2, a fully proved quantitative tool for the volume case. It is new relative to the background quoted in the brief, though it may well be known in the literature on cohomology-free flows;
- §3, consequences of §2 and an exact account of where they stop;
- §4, a list of open questions.

None of §2–§3 proves (PE0), not even in the volume case.

## 1. Check of the chain
- **Step 1 is correct.** It is the variational principle for the homeomorphism g_1, plus ergodic decomposition. Entropy is affine, and Jacobs' formula expresses h_mu as the integral of the entropies of the ergodic components, so some component has positive entropy. Also h_top(g_t) = |t| h_top(g_1).
- **Step 3 is correct as logic.**
- **Step 2 (entry 113)** is cited from earlier rounds. I did not re-check it.

So if Step 2 holds, (PE0) implies the problem's claim. I found no gap in the logic of the chain.

## 2. A two-point bounded-deviation estimate (volume case; proved)
**Setting.** Assume X is GH and preserves a smooth positive probability density omega. Fix a Riemannian distance dist on M.

**Lemma 2.0.** X(C^inf) = {f in C^inf : omega(f) = 0}. For every k there are m and C such that the solution u with omega(u) = 0 of Xu = f satisfies ||u||_{C^k} <= C ||f||_{C^m}.

*Proof.* By Text B, Corollary 3 (with nu = omega), X(C^inf) is closed. By the duality consequence in Text A, a closed subspace equals the annihilator of its annihilator. The annihilator consists of the invariant distribution densities T, those with T(Xu) = 0 for all u. By (O2), each such T equals u·omega with Xu = 0, so T = c·omega by L1. Hence X(C^inf) = ker(omega). The estimate is Text B, Lemma 2. ∎

**Proposition 2.1.** There are m and C such that, for every smooth phi, all x, x' in M and all real T:
(a) |∫_0^T phi(g_t x) dt − T·omega(phi)| <= C ||phi||_{C^m};
(b) |∫_0^T [phi(g_t x) − phi(g_t x')] dt| <= C ||phi||_{C^m} · (dist(x, x') + dist(g_T x, g_T x'));
(c) (linearised form) for every v in T_x M, |∫_0^T dphi(Dg_t v) dt| <= C ||phi||_{C^m} · (|v| + |Dg_T v|).

*Proof.* Put f = phi − omega(phi), so that ||f||_{C^m} <= 2||phi||_{C^m}. Let u be the mean-zero solution of Xu = f from Lemma 2.0, taken with k = 1. Since d/dt u(g_t x) = f(g_t x),
∫_0^T f(g_t x) dt = u(g_T x) − u(x).
- (a): the right side has absolute value at most 2||u||_inf.
- (b): subtract the same identity at x'. The mean terms cancel. Use |u(a) − u(b)| <= ||du||_inf dist(a, b), which holds because M is connected.
- (c): differentiate the identity in x along v. This gives ∫_0^T df(Dg_t v) dt = du(Dg_T v) − du(v), and df = dphi. ∎

**Remark 2.2.** (a) is a uniform bounded-deviation property for every smooth observable, with a tame constant. (b) and (c) are its two-point and infinitesimal versions. The point of (b) and (c) is that the bound depends only on the endpoints, not on T.

## 3. Consequences, and where they stop (volume case)
**Corollary 3.1 (bi-asymptotic pairs; proved).** Suppose there are T_k → +inf with dist(g_{±T_k} x, g_{±T_k} y) → 0. Then for every smooth phi,
lim_k ∫_{−T_k}^{T_k} [phi(g_t x) − phi(g_t y)] dt = 0.

*Proof.* Apply Proposition 2.1(b) to the points g_{−T_k} x and g_{−T_k} y, with time 2T_k. ∎

This is the volume-case analogue of the "cycle functional" vanishing used in earlier rounds (Theorem J, Lemma K). Turning it into a contradiction needs a bump function phi near one leg that the other leg does not cancel. That requires an exact bi-asymptotic pair (a homoclinic pair) with control at a fixed scale. For a non-hyperbolic measure (a zero exponent transverse to the flow, which entry 60 forces), a dimension count gives no such pairs in general. The strong unstable leaf of x and the weak stable leaf of z have dimensions u and s + 1, and u + s + 1 = n − c < n when there are c >= 1 zero exponents besides the flow. So this is exactly the obstruction recorded in round 12. I could not get past it.

**Corollary 3.2 (infinite spectral flatness; proved).** Let E be the spectral measure of the unitary flow phi ↦ phi∘g_t on L^2(omega). For every N there are m_N and C_N such that, for every smooth phi and every delta > 0,
||E[−delta, delta](phi − omega(phi))||_{L^2} <= C_N delta^N ||phi||_{C^{m_N}}.

*Proof.* Iterating Lemma 2.0 N times gives phi − omega(phi) = X^N u_N, with u_N smooth, of mean zero, and ||u_N||_inf <= C_N ||phi||_{C^{m_N}}. Since X is the skew-adjoint generator, E[−delta, delta] X^N u_N = X^N E[−delta, delta] u_N, whose norm is at most delta^N ||u_N||. ∎

This does **not** contradict positive entropy. A K-flow has Lebesgue spectrum, and a Lebesgue spectral density may vanish to infinite order at 0 for every vector in a dense set. This is consistent with round 12's finding that Mechanism B is dead (#126).

**Remark 3.3 (sufficient condition; a reformulation, not an answer).** In the volume case the flow is uniquely ergodic by (O2), so h_top(g_1) = h_omega(g_1) by the variational principle. Positive h_omega forces a Lebesgue spectral component on the orthocomplement of the Pinsker algebra. This is the Kolmogorov–Sinai/Rokhlin theorem, extended to flows by Gurevich; I cite it from memory. Hence each of the following would suffice, in the volume case only:
- the flow is L^2(omega)-rigid (g_{t_k} → id strongly for some t_k → inf);
- the flow has no absolutely continuous spectral component.

I could prove neither from GH.

**What I tried and why it fails.**
- (i) Combining 2.1(c), applied to the coordinate functions of an embedding M ⊂ R^N and localised by a partition of unity, with Oseledets vectors. The integrals ∫_0^T dphi(Dg_t v) dt may cancel, because the vectors Dg_t v rotate in each chart. No positivity is available.
- (ii) Real eigen-distributions (statement (E1) of R4-q10). The identity T(R^j phi) = (−1/kappa)^j T(phi), with R = X^{-1}, can only lead to a contradiction if R is bounded on a fixed C^s. But R loses derivatives, and rescaling time (X → cX) changes kappa freely.
- (iii) The general (non-volume) case. Proposition 2.1 depends on the invariant distribution densities being one-dimensional. Without a volume, the weighted analogue would need the operator P = X + d (phi ↦ Xphi + dphi) to have closed range on C^inf. By the closed-range theorem this is equivalent to X(D') being weak*-closed. GH does not visibly imply this, and I could not decide it. If P(C^inf) were closed, then P(C^inf) = {phi : ∫ phi dnu = 0}, using L1 for the kernel of the transpose. One would then get the conformally weighted analogue of 2.1(a): |∫_0^T e^{J_t(x)} phi(g_t x) dt − (nu-mean term)| bounded. I did not derive (PE0) from this either.

## 4. Open questions (explicit)
1. **(PE0) itself.** It is open after this attempt, including the volume-preserving case in dim M >= 4.
2. **Volume case.** Does uniform bounded deviation for all smooth observables with tame constants (Proposition 2.1(a)) force zero metric entropy for a smooth flow? A positive answer would settle the volume case.
3. Under GH, is the range of P = X + d on C^inf closed? Equivalently, is X(D') weak*-closed?
4. Under GH, does a smooth invariant volume (V) exist? I recall, without being certain, that Forni (Contemp. Math. 2008) stated GH ⇒ cohomology-free, which includes (V). I could not reconstruct a proof, and I do not use it.
5. (E1): does GH exclude distributions T ≠ 0 with L_X T = kappa T, kappa real and nonzero?

=== END OF ANSWER round13_q3 ===
