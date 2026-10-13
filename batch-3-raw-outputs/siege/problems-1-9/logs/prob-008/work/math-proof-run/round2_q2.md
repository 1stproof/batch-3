kind: attempt
Open question attempted: the dynamical core (ledger OPEN item): a C^infinity flow with a smooth invariant volume omega, uniquely ergodic, and cohomology-free with tame estimates (every omega-mean-zero smooth f equals Xu with u smooth, ||u||_{C^r} <= C ||f||_{C^k}) has zero entropy, INCLUDING when omega has zero Lyapunov exponents transverse to the flow. The problem statement below also gives you full GH (every distribution u with Xu smooth is smooth), which you may use freely.

Your task: prove that, under GH plus the hypotheses
  H. X preserves a smooth volume omega (mass 1), the flow is uniquely ergodic (omega the only invariant probability measure), and every omega-mean-zero smooth f is Xu with u smooth with tame estimates,
the volume omega has no positive Lyapunov exponent (equivalently, by the variational principle, unique ergodicity and Pesin's formula, h_top = 0). Give a complete proof, or prove a precise strictly easier reduction and state the missing lemma exactly.

Background you may use (proved earlier) follows.

=== ESTABLISHED BACKGROUND (proved in earlier work; you may use it, quoted verbatim) ===

[Text A, from one earlier result]
Notation: GH means: if u ∈ D'(M), f ∈ C^∞ and Xu = f, then u ∈ C^∞. Fix a smooth positive density ω₀ (no invariance assumed). Sobolev spaces H^s are taken with respect to it, and c(u) = ∫u ω₀ / ∫ω₀.

## L1 (proved). ker(X on D') = constants.
Proof. Suppose Xu = 0 with u ∈ D'. By GH, u is smooth. Suppose u is not constant. Choose c with min u < c < max u. Then U₊ = {u>c} and U₋ = {u<c} are nonempty open sets. Take smooth nondecreasing functions H_ε on R with H_ε(t) = 0 for t ≤ -ε and H_ε(t) = 1 for t ≥ 0, and set v_ε = H_ε(u-c). This is smooth and Xv_ε = H_ε'(u-c)·Xu = 0. As ε→0, v_ε → v = 1_{U₊} pointwise and boundedly, hence in L¹, hence in D'. Since X is continuous on D', Xv = 0. By GH, v agrees a.e. with a continuous function w. Then w ∈ {0,1} a.e., hence everywhere by continuity. Since M is connected, w is constant. But w = 1 a.e. on U₊ and w = 0 on U₋, and both sets have positive measure. Contradiction. ∎

## L2 (proved). For every r there are k and C with ||u-c(u)||_{H^r} ≤ C||Xu||_{H^k} for all u ∈ C^∞. Hence X(C^∞) is closed in C^∞.
Proof. Fix s. Let F_s = {u ∈ H^{-s} : Xu ∈ C^∞} with the seminorms ||u||_{H^{-s}} + ||Xu||_{H^j}, j ∈ N. F_s is Fréchet: a Cauchy sequence converges in H^{-s} to u, and Xu_n converges in C^∞ to some g; since X: H^{-s} → H^{-s-1} is continuous, g = Xu.

By GH, F_s ⊂ C^∞. The inclusion has closed graph, because both spaces embed continuously in H^{-s}. By the closed graph theorem for Fréchet spaces (a linear map between Fréchet spaces with closed graph is continuous), the inclusion is continuous. So for each r there are j and C with
(*) ||u||_{H^r} ≤ C(||u||_{H^{-s}} + ||Xu||_{H^j}).

Now fix r > -s, take j large enough that (*) holds both for r and for r+1, and suppose the claimed estimate fails with k = j. Then there are smooth u_n with c(u_n) = 0, ||u_n||_{H^r} = 1 and ||Xu_n||_{H^j} → 0. By (*) at level r+1 (note ||u_n||_{H^{-s}} ≤ ||u_n||_{H^r} = 1), the u_n are bounded in H^{r+1}. By Rellich (H^{r+1} → H^r is compact on a compact manifold), a subsequence converges in H^r to some u with ||u||_{H^r} = 1 and c(u) = 0. Moreover Xu = lim Xu_n = 0 in H^{r-1}. By L1, u is constant, and then c(u) = 0 forces u = 0. Contradiction.

Closed range: suppose Xu_n → f in C^∞. Apply the estimate to u_n - c(u_n): this sequence is Cauchy in every H^r, so it converges in C^∞ to some u, and Xu = f. ∎

Duality consequence: X(C^∞) is exactly the annihilator of the X-invariant distribution densities. Indeed, by Hahn–Banach, a closed subspace of C^∞ equals the annihilator of its annihilator in D'-densities, and that annihilator is {T : L_X T = 0}.

[Text B, from another earlier result; C^k form of the estimate]
**Convention.** Fix a smooth positive density ν on M. A distribution is a continuous linear functional on smooth densities. Using ν, identify distributions u with functionals φ ↦ ⟨u, φν⟩ on C^∞(M). Then L_X u is defined by ⟨L_X u, ρ⟩ = −⟨u, L_X ρ⟩. Write d = div_ν X, so that L_X(φν) = (Xφ + dφ)ν. For smooth u, L_X u = Xu. The facts below do not depend on this choice of identification.
## Lemma 2 (a priori estimate; Peetre-type argument). For every k there are m and C such that ‖u‖_{C^k} ≤ C‖Xu‖_{C^m} for all u ∈ C^∞ with ∫u dν = 0.
*Proof.* Fix s > n/2 + 1. Let Y = {u ∈ H^{-s} : Xu ∈ C^∞}. Give Y the Fréchet topology defined by the seminorms ‖u‖_{-s} and ‖Xu‖_{C^j}, j ≥ 0. Y is complete, because X: H^{-s} → H^{-s-1} is continuous. By hypothesis Y ⊂ C^∞. The inclusion Y → C^∞ has closed graph, since both topologies are finer than D'. By the closed graph theorem for Fréchet spaces, the inclusion is continuous. So
(∗) ‖u‖_{C^k} ≤ C(‖u‖_{-s} + ‖Xu‖_{C^m}) for some m and C.

Suppose the estimate of the lemma fails. Then there are u_n with zero mean, ‖u_n‖_{C^k} = 1 and Xu_n → 0 in C^m. A bounded set in C^k is precompact in H^{-s} (Rellich), so a subsequence is Cauchy in H^{-s}. By (∗) that subsequence is Cauchy in C^k, so u_n → u in C^k. In the limit Xu = 0 in D', so u is constant by Lemma 1. Also u has mean 0, so u = 0. This contradicts ‖u‖_{C^k} = 1. ∎

## Corollary 3. X(C^∞) is closed in C^∞, and X: C^∞_0 → X(C^∞) is a topological isomorphism. Here C^∞_0 denotes the smooth functions with ν-mean zero.
*Proof.* Suppose Xu_n → f with u_n ∈ C^∞_0. By Lemma 2, (u_n) is Cauchy in every C^k, so u_n → u and Xu = f. ∎

[Further observations, elementary; check them as you use them]
(O1) Dual estimate. From the C^k estimate (Text B, Lemma 2): for every k there are m, C such that for every distribution T in (C^k)' with T(1) = 0 there is a distribution density S in (C^m)' with S(Xu) = T(u) for all smooth u (i.e. S solves the transposed equation -L_X S = T up to sign convention), and ||S||_{(C^m)'} <= C ||T||_{(C^k)'}. (Hahn–Banach applied to Xu -> T(u) on the closed subspace X(C^infinity).) In particular for points x, y one gets S_{x,y} with S(Xu) = u(x) - u(y) and ||S_{x,y}|| <= C d(x,y).
(O2) If X preserves a smooth positive density omega, then for any invariant probability measure mu the distribution v = mu/omega satisfies Xv = 0 (because L_X(v omega) = (Xv) omega when div_omega X = 0), so by Lemma L1 v is constant: mu = omega. Hence a smooth invariant volume gives at once: unique ergodicity, minimality, no zeros of X, no periodic orbits (dim M >= 2), and (by the duality consequence in Text A) every omega-mean-zero smooth f equals Xu with u smooth, with the tame estimate of Text B.
(O3) With nu any smooth positive density and d = div_nu X: if d = c + Xa with c constant and a smooth, then e^{-a} nu is invariant (and c = 0 automatically, integrating L_X(e^{-a}nu) = c e^{-a} nu over M). Conversely a smooth invariant density rho nu gives d = -X log rho. So "smooth invariant volume" is equivalent to d lying in R + X(C^infinity), equivalently (closed range) to T(d) = c T(1) for every X-invariant distribution density T, for one constant c.
(O4) GH is preserved under time changes hX (h > 0 smooth), under X -> -X, and under conjugation X -> X + Xa = e^{-a} X e^{a} (as operators on distributions).
=== END OF BACKGROUND ===

=== AN EARLIER PARTIAL RESULT (quoted verbatim; H1 = unique ergodicity with smooth volume, H2 = cohomology-free with tame estimate) ===
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
=== END OF EARLIER PARTIAL RESULT ===

Two diagnostic facts the planner found (check them; they constrain any proof):
(D1) The tame estimate alone cannot suffice. For a transitive Anosov flow (e.g. a geodesic flow of a negatively curved surface) X(C^infinity) is closed (Livsic theory with tame estimates, de la Llave–Marco–Moriyon; recalled), so an estimate ||u - mean||_{C^1} <= C||Xu||_{C^m} holds there too, and so does the identity of Lemma A for f in the range — yet the entropy is positive. What fails for Anosov flows is that the range is not all mean-zero functions: bump functions f placed along the configuration have nonzero integrals over nearby periodic orbits produced by the closing lemma. So a proof must use that EVERY mean-zero smooth f (in particular arbitrary bumps) is in the range — in effect, a "distributional closing lemma": near-loops formed by y in W^u(x) with d(x,y) tiny must produce something that, in the UE setting, contradicts the estimate, whereas in the hyperbolic setting they produce periodic orbits.
(D2) Loss of derivatives in the bump strategy of step 3 of the earlier result. With d(x,y) = delta and Lipschitz constant L of the flow, the backward orbits of x and y stay within e^{L|t|} delta of each other for |t| <= log(eps/delta)/L, while by unstable contraction at rate lambda they are within eps again for |t| >= log(r_0/eps)/lambda (r_0 = leaf distance). An eps-separated window exists only if delta >= eps^{1 + L/lambda} roughly, but the contradiction needs delta << eps^{m+1}; so the naive single-pair bump argument works only when m < L/lambda. A successful argument must beat this — e.g. by choosing the pair (x,y) cleverly (Pesin blocks, Ledrappier–Young conditional measures on unstable leaves are absolutely continuous since omega is smooth, recurrence to sets of positive measure, many returns), by averaging over families of pairs to obtain distributions whose X-image is smooth (then GH applies directly: a non-smooth distribution W with XW smooth contradicts GH), by summing many near-loops coherently (so that the left side grows while the right side stays bounded by C||f|| times the sum of the gaps), or by using test functions f adapted to the dynamics rather than plain bumps.

Further ideas you may use or discard: (a) any u in L^2(omega) with Xu smooth is a distribution, hence smooth by GH — so constructing, from unstable-leaf data, an L^2 or measure-valued solution of Xu = f that is visibly non-smooth (e.g. discontinuous across a measurable partition subordinate to W^u) contradicts GH; (b) the solution S_{x,y} of observation (O1) is unique modulo multiples of omega, so for y in W^u(x) it equals the explicit distribution w = integral_{-inf}^0 (delta_{g_t x} - delta_{g_t y}) dt up to a multiple of omega, giving ||w + c omega||_{(C^m)'} <= C d(x,y).
Write every step; cite only standard theorems (Pesin theory, Ledrappier–Young, Ruelle inequality, variational principle) and state exactly which version you use.
