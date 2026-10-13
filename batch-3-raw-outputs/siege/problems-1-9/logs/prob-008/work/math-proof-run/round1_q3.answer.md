# round1_q3: partial answer. The zero-entropy claim is NOT fully proved here.

## 0. Reductions (standard; the literature is cited from memory)
By H1 the volume ω is the only invariant measure. The variational principle then gives h_top(g_1) = h_ω(g_1). Pesin's formula (ω is a smooth measure) gives h_ω = ∫ Σ λ_i^+ dω. So we only need to show that ω has no positive Lyapunov exponent.

**Hyperbolic case.** Suppose every exponent of ω other than the flow direction is nonzero. If h_ω > 0, the closing lemma / horseshoe theorem for flows yields periodic orbits. This is Katok's theorem (1980) for diffeomorphisms; the version for C^{1+α} flows without fixed points, with a hyperbolic ergodic measure of positive entropy, is due to Lian–Young and others (cited from memory). Periodic orbits contradict H1, so h_ω = 0 in this case. Even more simply, a periodic orbit carries an invariant probability measure different from ω, which contradicts unique ergodicity.

## 1. Lemma A (rigorous, given H2 and Pesin theory)
**Setting.** Take a Pesin-regular x and y in the global unstable manifold W^u(x), so that d(g_{-T}x, g_{-T}y) → 0 as T → ∞. Let f be smooth with ∫f dω = 0, and let u be the smooth solution of Xu = f given by H2.

**Claim.**
Φ_f(y) := ∫_{-∞}^0 (f(g_t x) - f(g_t y)) dt = u(x) - u(y).

Consequently |Φ_f(y)| ≤ C ||f||_{C^k} d_M(x,y), where d_M is the distance in M, not the distance along the leaf.

**Proof.** By the fundamental theorem of calculus along orbits,
∫_{-T}^0 f(g_t z) dt = u(z) - u(g_{-T} z).
Subtract this identity for z = y from the one for z = x. Let T → ∞ and use the continuity of u together with d(g_{-T}x, g_{-T}y) → 0. The bound then follows from the C^1 estimate in H2. ∎

**What this means.** Lemma A turns the planner's distribution w rigorously into H2: the identity gives <w,f> = u(x) - u(y) for every mean-zero f. Its content is the following. The function Φ_f is defined intrinsically, by the leaf dynamics, and is continuous in the leaf topology. Lemma A says that Φ_f is even Lipschitz for the ambient metric, uniformly in ||f||_{C^k}.

## 2. Missing lemma (open)
The proof would be complete with the following statement, which I do not prove.

**(L)** Suppose ω has a positive exponent. Then there exist:
- a regular x,
- points y_n ∈ W^u(x) with d_M(x, y_n) → 0,
- mean-zero smooth f_n,

such that |Φ_{f_n}(y_n)| / (||f_n||_{C^k} d_M(x, y_n)) → ∞.

**How (L) would be used.** By Lemma A, (L) contradicts H2.

**Expected proof strategy.**
1. Minimality (H1) and recurrence should give points y_n that lie on the unstable leaf of x, are leaf-far from x, but are ambient-close to x.
2. Take f_n to be a bump of width ε_n, so that ||f_n||_{C^k} ~ ε_n^{-k}.
3. Place the bump on a stretch of the backward orbit of y_n that is separated from the orbit of x. This should give |Φ_{f_n}(y_n)| ≳ ε_n, provided the two backward orbits do not compensate each other.
4. Choose ε_n with d(x, y_n) ≪ ε_n^{k+1}.

**Where it breaks.** The gap is the lower bound in step 3. The two orbits may revisit the bump region and cancel each other, and when there are extra zero exponents no Pesin-theoretic tool controls this.

I also checked the other natural uses of H2 and H3:
- linearised versions (letting y → x along the unstable direction v),
- forward ergodic integrals,
- uniformly bounded ergodic integrals |∫_0^T f∘g_t| ≤ C ||f||_{C^k}.

Each of them only gives bounds that are consistent with exponential growth. For example, for the linearised object w_v, H3 gives ||w_v|| ≤ C, and w_v is in fact bounded. So none of these alone yields a contradiction.

## Status
- **Proved:** the reductions in §0, the hyperbolic case (modulo the cited closing lemma), and Lemma A.
- **Open:** lemma (L), i.e. the case where ω has a positive exponent together with extra zero transverse exponents. So h_top = 0 is not established in general.

=== END OF ANSWER round1_q3 ===
