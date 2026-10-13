# round7_q4 — answer (work in progress)

## Plan / statement attempted
Target: (PE-NH). Under GH there is no ergodic flow-invariant mu with h_mu(g_1) > 0 and a transverse zero exponent.
Plan:
(1) Find out what a refutation would mean logically. Result (S1): (PE-NH) is equivalent to the [GOAL] in dim >= 4, so a refutation is a disproof of the problem.
(2) Go through the three templates. For each, either reduce it to the core case or give a precise obstruction (S2).
(3) Prove whatever new structural restrictions I can (S3), and isolate exactly where the argument stops (S4).

## S1. What a refutation of (PE-NH) would mean (proved)

**Proposition 1.1.** Let dim M >= 4. Modulo the results cited in the chain (Theorem 5.1 of R6-a, which uses Ruelle's inequality and the Katok / Lian-Young horseshoe theorem, and the variational principle step 4), the following are equivalent for GH vector fields:
(a) (PE-NH);
(b) h_top(g_1) = 0 for every GH vector field (the [GOAL]).

*Proof.* (b) => (a): by the variational principle, h_mu(g_1) <= h_top(g_1) = 0 for every invariant mu, so no mu as in (PE-NH) exists. (a) => (b): this is the chain (steps 1-4). ∎

**Consequence.** A counterexample to (PE-NH) would be a GH flow of positive topological entropy, i.e. a counterexample to the problem itself. Conversely, a counterexample to the problem in dimension >= 4 has, by the variational principle, an ergodic mu with h_mu > 0, and by Theorem 5.1 this mu is non-hyperbolic. So refuting (PE-NH) is exactly the same task as disproving the problem.

The Greenfield-Wallach conjecture (cited from memory; open in general) says that every GH vector field is, after a time change, smoothly conjugate to a Diophantine linear flow on a torus. It predicts that no counterexample exists. I did not find one. What follows are obstructions for the suggested templates, together with new structural restrictions.

## S2. The templates

### 2.1 Template (1) is a special case of template (2) (proved)
Let X = alpha . d_theta + Y(theta, y) on T^d x F, where alpha is Diophantine; then alpha_1 != 0 after renumbering. The theta_1-coordinate of g_t(theta, y) is theta_1 + alpha_1 t. So Sigma = {theta_1 = 0} is a global cross-section, and every orbit returns to it after exactly the time r = 1/alpha_1. Let F = g_r restricted to Sigma, and let N_F be the mapping torus Sigma x [0, r] / (p, r) ~ (F p, 0). The map Phi(p, s) = g_s(p) is a diffeomorphism from N_F onto M, and it carries d/ds to X. By the round-6 facts (constant-roof suspension; GH is invariant under constant time change), X is GH iff F is GH, i.e. iff every distribution v on Sigma = T^{d-1} x F with v o F - v smooth is smooth. Abramov's formula gives h_top(g_1) = h_top(F)/r. Hence template (1) is the special case of template (2) in which the diffeomorphism F is a skew product over a translation of T^{d-1}.

### 2.2 Products cannot be minimal counterexamples (proved)
Let M = M_1 x M_2 and X = X_1 + X_2, where X_i is tangent to M_i.
- If X is GH, so is X_1. Indeed, if u_1 is in D'(M_1) and X_1 u_1 is smooth, then u = u_1 (x) 1 satisfies Xu = (X_1 u_1) (x) 1, which is smooth. So u is smooth, and hence u_1 is smooth (pair u with phi (x) psi, where int psi = 1).
- Topological entropy is additive for products: h_top(g_1) = h_top(g^1_1) + h_top(g^2_1).
So a product counterexample has a factor that is itself a counterexample, of dimension >= 4 by Theorem 5.2. In particular, template (1) with Y independent of theta (a Diophantine linear flow times a fibre flow) gives a counterexample only if the fibre flow already is one.

### 2.3 Template (3): rigidity and Liouville obstructions (proved; standard inputs cited)
**Lemma 2.3 (Liouville criterion).** Suppose there are smooth u_n with int u_n dnu = 0 and ||u_n||_{C^0} = 1, and with ||X u_n||_{C^m} -> 0 for every m. Then X is not GH.
*Proof.* By Lemma 2 of Text B with k = 0, there are m and C such that 1 = ||u_n||_{C^0} <= C ||X u_n||_{C^m} -> 0, a contradiction. ∎

This is the mechanism that defeats Anosov-Katok / fast-approximation limits X = lim (h_n)_* X_n built from Liouvillean linear flows X_n. Take u_n = e_{k_n} o h_n^{-1}, where e_{k_n} is a character with |<k_n, alpha_n>| tiny. Then ||X u_n||_{C^m} <= ||(X - (h_n)_* X_n) u_n||_{C^m} + |<k_n, alpha_n>| ||u_n||_{C^m}. In the usual constructions both terms tend to 0, because the convergence is chosen faster than any power of ||h_n||_{C^{m+1}}. (I did not check this for a specific published construction; it is a sketch.)

**Lemma 2.4 (rigidity kills entropy; no GH needed).** Suppose the flow is uniquely ergodic with invariant measure omega, and rigid for omega: there are t_n -> infinity with phi o g_{t_n} -> phi in L^2(omega) for every phi. Then h_top(g_1) = 0.
*Proof.* Let U = Koopman operator of g_1 on L^2(omega) and U_s that of g_s. Write t_n = m_n + s_n with m_n integer, s_n in [0,1), and pass to a subsequence with s_n -> s. Then U^{m_n} phi = U_{-s_n}(U_{t_n} phi) and ||U_{-s_n}(U_{t_n}phi - phi)|| = ||U_{t_n}phi - phi|| -> 0, while U_{-s_n} phi -> U_{-s} phi by strong continuity; so U^{m_n} -> V := U_{-s} strongly. Let Pi be the Pinsker sigma-algebra of g_1; since g_s commutes with g_1, it preserves Pi, so V preserves H := L^2 ⊖ L^2(Pi). By the Rokhlin-Sinai theorem (cited) U has countable Lebesgue spectrum on H; so for f in H the spectral measure of f is absolutely continuous and <U^{m} f, f> -> 0 as m -> infinity (Riemann-Lebesgue). Hence <V f, f> = 0 for every f in H, so by polarisation V = 0 on H; V is unitary, so H = 0, Pi is everything, and h_omega(g_1) = 0. Unique ergodicity and the variational principle give h_top = h_omega = 0. ∎

Hence every fast-approximation construction that yields rigid systems (the standard AbC outcome) cannot produce positive entropy at all, and template (3) must use non-rigid systems. Herman's minimal positive-entropy diffeomorphisms (cited from memory: skew products (theta, x) -> (theta + alpha, A(theta) x) on T x SL(2,R)/Gamma, with a positive fibre exponent) preserve a smooth volume. Under GH this forces (by (O2)) unique ergodicity, and forces every volume-mean-zero smooth function to be a smooth coboundary with tame bounds. This is exactly the volume-preserving core case (inside (PE0)). I found no obstruction specific to Herman's examples beyond those listed in S3.

## S3. New structural restrictions (proved unless marked)

Conventions as in the brief: nu a smooth positive density, d = div_nu X, J_t the log-Jacobian cocycle, P phi = X phi + d phi, F_phi(t) = S(e^{J_t} phi o g_t) for a distribution density S.

### 3.1 Unstable sets contain at most one forward volume-contracting point
**Lemma 3.1.** Assume GH. Let x be in M, and let theta > eta > 0 and C be constants with J_t(x) <= C + (theta - eta)|t| for t <= 0. There are no two distinct points y_1, y_2 with
 (i) d(g_t y_i, g_t x) <= C e^{-theta|t|} for t <= 0 (i = 1, 2), and
 (ii) J_t(y_i) <= C - eps t for t >= 0 (i = 1, 2), for some eps > 0.
(One of the y_i may equal x.)
*Proof.* Since d is Lipschitz, |d(g_s y_1) - d(g_s y_2)| <= 2C Lip(d) e^{-theta|s|} for s <= 0. So b := lim_{t -> -inf}(J_t(y_1) - J_t(y_2)) exists, and |J_t(y_1) - J_t(y_2) - b| <= K e^{-theta|t|} for t <= 0. Likewise J_t(y_1) - J_t(x) converges as t -> -inf, so J_t(y_1) <= C' + (theta - eta)|t| for t <= 0. Put S = delta_{y_1} - e^b delta_{y_2}. It is nonzero because y_1 != y_2.
- For t <= 0: F_phi(t) = e^{J_t(y_1)}[phi(g_t y_1) - e^{r_t} phi(g_t y_2)], with r_t = b + J_t(y_2) - J_t(y_1) and |r_t| <= K e^{-theta|t|}. So |F_phi(t)| <= e^{J_t(y_1)} (2C ||phi||_{C^1} + K e^K ||phi||_inf) e^{-theta|t|} <= C'' e^{-eta|t|} ||phi||_{C^1}.
- For t >= 0: |F_phi(t)| <= (1 + e^b) C e^{-eps t} ||phi||_inf.
So S satisfies (*) of Theorem J, which gives S = 0, a contradiction. ∎

This contains Prop 6.1 (take y_1 = x and y_2 generic in W^u_loc(x)). It also gives, in the case lambda = mu(d) = 0 left open in (PE0), the following. For mu-a.e. x (Pesin-regular, with W^u_loc(x) contracted backward at rate theta), the local unstable manifold W^u_loc(x) contains at most one point y with limsup_{t -> +inf} J_t(y)/t < 0. In particular, for every ergodic m with m(d) < 0, W^u_loc(x) contains at most one m-generic point. Symmetrically (apply to -X), W^s_loc(x) contains at most one point with limsup_{t -> -inf} J_t(y)/|t| > 0.

### 3.2 Integrable two-sided decay gives a continuum of imaginary eigen-distributions
**Lemma 3.2 (no GH needed).** Let S be a distribution density. Suppose that for every smooth phi, F_phi is in L^1(R), with int |F_phi| dt <= C ||phi||_{C^k}. For real xi put T_xi(phi) = int e^{-i xi t} F_phi(t) dt. Then:
- each T_xi is a distribution density of order <= k with T_xi(P phi) = i xi T_xi(phi);
- u_xi = T_xi/nu satisfies X u_xi = -i xi u_xi;
- if S != 0, then T_xi != 0 for all xi in a nonempty open set of R.
*Proof.* The order bound is clear. F_phi is C^1 with F_phi' = F_{P phi} (Theorem J, step 1), and F_{P phi} is in L^1. So F_phi has limits at plus and minus infinity, and these limits are 0 because F_phi is in L^1. Integrating by parts, int e^{-i xi t} F_phi' dt = i xi int e^{-i xi t} F_phi dt. This is the eigen-relation, and it translates into X u_xi = -i xi u_xi by Observation 0. If S(phi) != 0 for some phi, then F_phi(0) = S(phi) != 0, so the continuous L^1 function F_phi is not identically 0. By Fourier uniqueness its Fourier transform xi -> T_xi(phi) is a continuous function that is not identically 0, hence nonzero on an open set. ∎

**Consequence.** Theorem J can be extended from exponential to merely integrable two-sided decay, provided one proves:
(E1-i) under GH, the set of xi in R for which X u = i xi u has a nonzero solution u in H^{-s} is countable (for each s).
For smooth solutions, (E1-i) holds. If u is smooth and nonzero, then |u|^2 is smooth and X|u|^2 = 0, so |u| is a nonzero constant by L1. Eigenfunctions with distinct eigenvalues are orthogonal in L^2(m) for any invariant probability m, and L^2(m) is separable. For distributional solutions I could not prove (E1-i). It is a new sharp open sub-question. In the Diophantine linear case it holds by Fourier series.

### 3.3 The volume-preserving case: spectral restrictions
Assume GH and a smooth invariant volume omega (take nu = omega, so d = 0 and J = 0). By (O2) the flow is uniquely ergodic, and every omega-mean-zero smooth f equals Xu with u smooth and ||u||_{C^k} <= C ||f||_{C^m}.

**Lemma 3.3.**
(a) For every smooth f with int f domega = 0 and every k, the L^2(omega)-spectral measure sigma_f of the flow satisfies sigma_f([-e, e]) <= C_k(f) e^{2k}. Moreover sup_{T,x} |int_0^T f(g_t x) dt| < infinity, and the asymptotic variance of f is 0.
(b) There is no nonzero smooth psi such that |int psi . (phi o g_t) domega| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and all smooth phi. In particular the flow is not exponentially mixing (in both time directions) for smooth observables. Moreover, if (E1-i) holds, the same is true with e^{-eps|t|} replaced by any integrable function of t.
(c) If every smooth f had a singular spectral measure sigma_f, then h_top(g_1) = 0.
*Proof.* (a) Iterate the cohomological equation: f = X u_1 and u_1 - mean = X u_2, and so on. This gives f = X^k u_k with u_k smooth. On L^2(omega), X is the generator of the unitary group U_t phi = phi o g_t, and smooth functions lie in its domain. So sigma_{Xu} = s^2 sigma_u, and sigma_f = s^{2k} sigma_{u_k} gives the bound with C_k = ||u_k||^2_{L^2}. The bound on the ergodic integrals is |u_1(g_T x) - u_1(x)| <= 2||u_1||_inf. Bounded ergodic integrals give zero asymptotic variance.
(b) Apply Theorem J to S = psi omega. Here F_phi(t) = int psi . (phi o g_t) domega, because J = 0. The second claim follows from Lemma 3.2.
(c) By Rokhlin-Sinai (cited), g_1 has absolutely continuous (Lebesgue) spectrum on L^2 ⊖ L^2(Pi), where Pi is the Pinsker algebra. Fix a smooth f. Its projection to L^2 ⊖ L^2(Pi) has a spectral measure that is absolutely continuous with respect to sigma_f (for g_1). Since sigma_f is singular, that spectral measure is 0, so f is Pi-measurable. (Singularity for the flow implies singularity for g_1: the g_1-spectral measure is the pushforward of the flow spectral measure under s -> s mod 2 pi, and a.c. measures pull back to a.c. ones on each period interval.) Smooth functions generate the Borel sigma-algebra mod omega, so Pi is everything and h_omega = 0. Unique ergodicity then gives h_top = 0. ∎

So in the volume case, (PE-NH) would follow from: "GH implies purely singular spectrum." Part (a) gives singular behaviour only at the single frequency 0 (vanishing to infinite order). I could not move this to other frequencies, since GH controls only X and not X - i xi. This is the same gap as (E1-i).

### 3.4 Remark on Prop 6.2 in higher unstable dimension
R6-d worried that "generic points y_i might lie on an algebraic subvariety of the leaf, which would degenerate the moment system". This worry is unfounded. The system has N homogeneous linear equations in N+1 unknowns, so it always has a nonzero solution. The resulting S = sum a_j e^{-beta_x(y_j)} delta_{y_j} is nonzero because the y_j are distinct. So in any unstable dimension, Prop 6.2 needs only one input: C^K-tempered non-stationary normal-form coordinates on W^u in which g_{-1} acts by maps of the sub-resonance group (cited from memory: Kalinin-Sadovskaya type normal forms; not checked). The moment conditions are then imposed against all polynomials of weighted degree <= s, with weights equal to the unstable exponents. The sub-resonance group preserves the weighted-degree filtration, so the vanishing moments persist along the backward orbit. The Taylor remainder beyond weighted degree s decays like e^{-s n}, and one chooses s > |lambda| + 1. This removes the 1-dimensionality restriction of Prop 6.2 modulo that citation. It does not touch lambda = 0.

### 3.5 First-order backward cancellation needs no normal forms when lambda = 0 (proved, standard Pesin input)
Let mu be ergodic with lambda = mu(d) = 0. Let x be mu-generic and Pesin-regular, and let W be a C^inf local unstable disc through x with d(g_t y, g_t x) <= C e^{-theta|t|} for t <= 0, uniformly in y in W. Let m be any finite measure on W (leaf Lebesgue, or the conditional mu^u_x), and psi bounded measurable with int psi e^{-beta_x} dm = 0, where beta_x(y) = -lim_{t -> -inf}(J_t(y) - J_t(x)). Then S = psi m satisfies |S(e^{J_t} phi o g_t)| <= C e^{-(theta - delta)|t|} ||phi||_{C^1} for t <= 0.
*Proof.* e^{J_t(y)} = e^{J_t(x)} e^{-beta_x(y)}(1 + O(e^{-theta|t|})) and phi(g_t y) = phi(g_t x) + O(||phi||_{C^1} e^{-theta|t|}), uniformly on W. The leading term e^{J_t(x)} phi(g_t x) int psi e^{-beta_x} dm vanishes, and e^{J_t(x)} = e^{o(|t|)}. ∎
So in the case (PE0) the backward half of Theorem J is free for any first-order-balanced measure on an unstable disc. Everything hinges on the forward half (S4).

## S4. Where the attempt stops, and why

**Status.** (PE-NH) is neither proved nor refuted. By Prop 1.1, refuting it is the same as disproving the problem. The templates give no counterexample: template (1) reduces to (2) (S2.1); products are never minimal counterexamples (S2.2); rigid or Liouvillean fast-approximation constructions are excluded (Lemmas 2.3, 2.4); Herman-type volume-preserving skew products fall into the volume core case, which is not excluded.

**The precise obstruction in (PE0) (lambda = 0).** Theorem J needs a nonzero S with exponential decay of S(e^{J_t} phi o g_t) in both time directions. When lambda = 0 the weight e^{J_t} is e^{o(|t|)} at generic points, so cancellation is needed on both sides.
- Backward cancellation must come from objects determined by the past: point masses or measures on one unstable leaf (S3.5).
- Forward cancellation must come from objects determined by the future: point masses on one stable leaf, or derivatives in E^s directions. I also tried S(phi) = int psi(y)[d phi_y(e_s(y)) + c(y) phi(y)] dmu^u_x(y) with e_s(y) in E^s(y) and c(y) = -int_0^inf (dd)(Dg_r e_s(y)) dr. The correction c makes the forward part decay at rate theta^s - delta. But backward, Dg_t e_s(y) grows like e^{|chi^-||t|}. Cancelling it along W would need E^s(g_t y) and E^s(g_t x) to converge exponentially fast as t -> -inf. They do not: E^s is future-determined, and along an unstable leaf it varies only Hölder-continuously.
- Coupling the two sides needs local product structure (W^s(y) meeting W^u(x')). When there is a transverse zero exponent, dim W^s + dim W^u <= n - 2, and this structure is absent.
So the single-orbit and leaf-measure constructions of Theorem J cannot reach (PE0). Smearing over unstable discs gives forward decay only at the (unknown, generally non-exponential) rate of equidistribution of unstable discs.

**Open questions isolated here (each would settle part of (PE-NH)):**
(Q1) (E1-i) Under GH, is the set of xi in R for which X u = i xi u has a nonzero solution u in H^{-s} countable? A positive answer extends Theorem J to integrable two-sided decay (Lemma 3.2).
(Q2) Volume core: does GH plus a smooth invariant volume force purely singular spectrum for smooth functions? A positive answer gives h_top = 0 in that case (Lemma 3.3(c)). Lemma 3.3(a) proves the singularity only at the single frequency 0.
(Q3) An ergodic-theoretic version of (Q2), which I believe is the real content of the volume core case. Let (M, omega, g_t) be uniquely ergodic. Let A = C^inf(M), a dense flow-invariant algebra of bounded functions, and suppose every element of A with mean 0 is X u for some u in A. Does it follow that h_omega = 0? For Gaussian or Bernoulli-like systems the answer is yes: products u . (u o g_s) acquire positive asymptotic variance (for a Bernoulli shift with u = x_0 - 1/2, the function u . (u o T) - E[u . (u o T)] has Birkhoff sums of variance ~ N/16, so it is not an L^2 coboundary). For general K-systems I could not control the fourth-order cumulants.
(Q4) (PE0) itself: under GH, exclude an ergodic, non-hyperbolic mu with h_mu > 0 and mu(d) = 0.

**Summary of what is proved here.** Prop 1.1 (equivalence of (PE-NH) with the problem); S2.1 (template (1) is a constant-roof suspension); S2.2 (GH passes to product factors; entropy is additive); Lemma 2.3 (Liouville criterion); Lemma 2.4 (uniquely ergodic plus rigid implies zero entropy, via Rokhlin-Sinai); Lemma 3.1 (unstable sets contain at most one forward volume-contracting point, under GH); Lemma 3.2 (integrable two-sided decay gives an open set of imaginary eigenvalues); Lemma 3.3 (volume case: infinite-order vanishing of spectral measures at 0, zero variance, no two-sided exponential mixing, and "singular spectrum implies zero entropy"); S3.4 (the moment system always has a nonzero solution, so Prop 6.2 extends to all unstable dimensions modulo cited normal forms); S3.5 (free backward cancellation when lambda = 0). Cited from memory: Rokhlin-Sinai (Lebesgue spectrum off the Pinsker algebra), Abramov's formula, Kalinin-Sadovskaya normal forms (S3.4 only), Pesin theory.

=== END OF ANSWER round7_q4 ===

