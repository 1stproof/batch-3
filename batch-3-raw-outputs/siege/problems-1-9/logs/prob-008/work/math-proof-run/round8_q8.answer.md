# Answer to round8_q8

Plan: (Part 1) check the derivation problem <= (PE-NH) + listed results, and how plausible (PE-NH) is. (Part 2) First move, named: **time-change invariance of GH and the cohomology class of the divergence** [d] in C^inf/X(C^inf). This splits the problem into (i) the case where X has a smooth invariant volume and (ii) the case [d] != 0. Then push (i) as far as possible.

## Part 1. The derivation goes through, and (PE-NH) is *equivalent* to the claim

**Derivation.** Suppose h_top(g_1) > 0. By the variational step there is an ergodic flow-invariant mu with h_mu(g_1) > 0.
- mu does not live on the zero set Z of X. Z is flow-invariant, so by ergodicity mu(Z) is 0 or 1. If mu(Z) = 1, then g_1 = id on supp mu and h_mu(g_1) = 0. So mu(Z) = 0.
- Hence X(x) != 0 for mu-a.e. x. Since |X(g_t x)| <= e^{C|t|}|X(x)| in both time directions, the flow direction has Lyapunov exponent 0 for g_1.
- The Oseledets exponents of g_1 are measurable g_1-invariant functions. They are also g_s-invariant, because Dg_s is uniformly bounded for s in [0,1]. So they are constant mu-a.e. by flow-ergodicity, and "multiplicity of the exponent 0" makes sense.
- By the listed result "positive entropy => non-hyperbolic" (proved modulo Ruelle and Katok/Lian-Young), mu has a zero exponent transverse to X. So the exponent 0 has multiplicity >= 2.
- Then mu satisfies (a) and (b) of (PE-NH), which (PE-NH) forbids. Contradiction, so h_top(g_1) = 0.

Note: the dim <= 3 result and the mu(d)-band result are not needed for this derivation. They only narrow the cases a proof of (PE-NH) has to treat.

**Plausibility.** The converse also holds trivially: if h_top(g_1) = 0, the variational principle gives h_mu(g_1) = 0 for every invariant mu, so (PE-NH) holds. So, given the listed results, (PE-NH) is exactly equivalent to the problem's claim. It is neither stronger nor weaker, and it is as plausible as the problem statement. The reduction gains only this: the remaining enemy is a non-hyperbolic positive-entropy measure. Product examples (horseshoe flow x irrational rotation) show that such measures really occur among smooth flows in general. So they cannot be ruled out by dynamics alone; GH must be used.

## Part 2. First move: time changes and the divergence class

**Lemma TC (GH is invariant under time change).** Let rho > 0 be smooth and Y = rho X. Then X is GH iff Y is GH. Also (L1), (K0) and (K1) transfer between X and Y.

*Proof.* Multiplication by a smooth function is a continuous operation on D'(M). For u in D'(M), Yu = rho·Xu. So Yu is smooth iff Xu = rho^{-1}Yu is smooth. Also Yu = 0 iff Xu = 0. Finally, Yu = 1 iff Xu = 1/rho; under GH that forces u to be smooth, and then a Y-invariant probability measure (one exists by Krylov-Bogolyubov) integrates Yu = 1 to 0, a contradiction. []

On the dynamical side (quoted from memory): positivity of topological entropy is preserved under smooth time changes. For flows without zeros this is due to Ohno; Sun-Young-Zhou treat C^1 flows in general. The measure-theoretic form is Abramov/Totoki: for ergodic mu with mu(Z) = 0, the measure mu~ = rho^{-1}mu / mu(rho^{-1}) is Y-invariant, and h_{mu~}(Y_1) = h_mu(g_1)/mu(rho^{-1}). Hence (PE-NH) and the problem may be proved for any time change of X.

**Divergence bookkeeping.**
- If nu' = e^v nu, then div_{nu'}X = d + Xv.
- div_nu(rho X) = rho d + X rho. Equivalently, div_nu(rho X)/rho = d + X(log rho).

So up to the positive factor rho, the class [d] in C^inf/X(C^inf) is an invariant of X under both changes of density and time changes.

**Lemma SV.** Under GH the following are equivalent:
- (a) X preserves some smooth positive density;
- (b) d is in X(C^inf);
- (c) T(d) = 0 for every X-invariant distribution density T.

*Proof.*
- (a) => (b): if e^v nu is invariant, then d + Xv = 0, so d = X(-v).
- (b) => (a): if d = Xw, then nu' = e^{-w}nu has divergence 0.
- (b) <=> (c): this is the listed tame-closed-range result. X(C^inf) is closed and equals the annihilator of the invariant distribution densities. []

**Lemma UE.** Assume GH (L1 suffices) and that X preserves a smooth positive density nu. Then every X-invariant distribution density is c·nu. In particular:
- g_t is uniquely ergodic, with unique invariant measure nu/nu(M), which has full support;
- if dim M >= 2, X has no zeros and no periodic orbits.

*Proof.* Every distribution density can be written T = t·nu with t in D'(M), and L_X(t nu) = (Xt)nu + t·L_X nu = (Xt)nu. So L_X T = 0 iff Xt = 0, and then t is constant by (L1). A zero p would carry the invariant measure delta_p. A periodic orbit would carry its orbit measure, which is supported on a curve. Neither is a multiple of nu when dim M >= 2. []

**Corollary (volume case).** Assume GH, a smooth invariant probability density nu, and nu(f) = 0 with f smooth. Then:
1. f = Xu for a unique smooth u with nu(u) = 0, and ||u||_{C^0} <= C||f||_{C^m}. (By Lemma UE the only invariant density is nu, so the tame-closed-range result applies.)
2. Uniform rate: ||(1/T)∫_0^T f∘g_s ds||_{C^0} <= 2C||f||_{C^m}/T for all T > 0, because ∫_0^T f∘g_s ds = u∘g_T - u.
3. Spectral form. Let sigma_f be the spectral measure of f for the unitary Koopman flow on L^2(nu). Then ∫ lambda^{-2} dsigma_f(lambda) = ||u||^2_{L^2} <= C^2||f||^2_{C^m}. Hence sigma_f((-eps,eps)) <= C^2 eps^2 ||f||^2_{C^m}. In particular, every smooth f has asymptotic variance 0 (no CLT fluctuations).
4. Dual Poincare inequality. If h is in L^2_0(nu) with Xh in L^2, then ||h||_{(C^m)^*} <= C||Xh||_{L^2}.
   *Proof:* for smooth phi with nu(phi) = 0, write phi = Xw as in 1. Then <h,phi> = -<Xh,w> <= ||Xh||_{L^2}·C||phi||_{C^m}. Constants are handled by nu(h) = 0. []

**Reduction obtained.** By Lemmas TC, SV and UE, (PE-NH) — equivalently the problem — splits into two cases.
- **Case (i), [d] = 0.** After a change of density, X preserves a smooth volume nu. Then X is uniquely ergodic, the unique measure is nu, and there are no zeros and no periodic orbits. If moreover h_nu(g_1) > 0, then Ruelle and Pesin give h_nu = sum of the positive exponents of nu. The listed non-hyperbolicity result (which in this case also follows directly from Katok's horseshoe, since a horseshoe would produce periodic orbits) forces a transverse zero exponent. So case (i) of (PE-NH) is equivalent to this:
  > **(V)** No smooth flow on a compact manifold of dimension >= 4 can be uniquely ergodic with a smooth volume nu, satisfy h_nu(g_1) > 0, and have every smooth nu-mean-zero function be Xu with u smooth and ||u||_{C^0} <= C||Xu||_{C^m}.

  (V) does not need the distributional part of GH beyond what is used above. Conversely, (V) together with (L1) gives back the case.
- **Case (ii), [d] != 0.** By Lemma SV, some invariant distribution density T has T(d) != 0. This T need not be a measure. If every invariant probability measure has mu(d) = 0, then J_t/t -> 0 uniformly (a standard semi-uniform ergodic argument). Volumes then change only subexponentially, but X has no smooth invariant volume.

## Pushing case (i): a spectral reformulation, and where it stalls

Throughout, case (i) holds: nu is a smooth invariant probability volume, X is uniquely ergodic, and h := h_nu(g_1) > 0 (assumed, for contradiction).

**Lemma CLT (sufficient condition for a contradiction in case (i)).** Suppose some smooth f has phi := ∫_0^1 f∘g_s ds - nu(f) with positive asymptotic variance under g_1:

  V(phi) := limsup_n (1/n)||sum_{k<n} phi∘g_k||^2_{L^2(nu)} > 0.

Then GH fails.

*Proof.* Under GH, Corollary item 1 gives f - nu(f) = Xu with u smooth. Then phi = u∘g_1 - u, so sum_{k<n} phi∘g_k = u∘g_n - u. Its L^2 norm is at most 2||u||_{L^2}, hence V(phi) = 0. []

So in case (i) the problem is reduced to the following purely ergodic-smooth statement:

> **(V')** If a smooth flow preserves a smooth volume nu with h_nu(g_1) > 0, then some smooth f has V(∫_0^1 f∘g_s ds) > 0. Weaker but sufficient: not every smooth mean-zero f is an L^2 coboundary of the flow.

Facts relevant to (V'), quoted from memory:
- Rokhlin-Sinai: for an ergodic automorphism of positive entropy, the orthocomplement of L^2(Pinsker algebra) carries countable Lebesgue spectrum.
- Gordin's martingale method: martingale differences with respect to an increasing generating sigma-algebra (here, by Ledrappier-Young, the one generated by a partition subordinate to Pesin unstable manifolds) have positive variance.

So L^2 functions with positive variance exist in abundance. **The gap is smoothness.** Martingale differences along the unstable partition are not smooth, and V is not continuous on L^2, so density of C^inf in L^2 gives nothing.

**Quantitative attempt (dead end, with reason).** Under GH, item 3 gives sigma_f((-eps,eps)) <= C^2 eps^2 ||f||^2_{C^m} for smooth f. Take h in L^2 with positive spectral density c at 0 (so sigma_h((-eps,eps)) >= c·eps), and approximate it by smooth f_r with ||h - f_r||_{L^2} <= a(r) and ||f_r||_{C^m} <= r^{-m}. This yields a contradiction only if

  inf_r ( a(r) + C·eps·r^{-m} ) = o(eps^{1/2}).

That is, h must lie in the real interpolation space (L^2, C^m)_{theta,inf} with theta > 1/2. Indicators of nice sets have a(r) ~ r^{1/2}, i.e. theta = 1/(2m+1) < 1/2, so this fails. So the method needs a function of "smoothness index > 1/2" with positive asymptotic variance. That is essentially (V') again.

**Why soft constructions cannot work.** Rokhlin-tower functions h with ||Xh|| <= ||h||/tau exist for every aperiodic volume-preserving flow. They satisfy the GH-consequence ||h||_{(C^m)^*} <= C||Xh|| without contradiction, and Diophantine linear flows on tori are GH. Hence any contradiction must use entropy (or exponents) together with smoothness, not aperiodicity or mixing alone. Mixing by itself is compatible with items 2-4, since smooth coboundaries of mixing flows exist in abundance.

## Status

**Proved here (modulo the listed results and the classical theorems named):**
- (P1) The problem follows from (PE-NH) plus the listed results. Conversely, the problem implies (PE-NH). So the two are equivalent given the listed results.
- (P2) Lemma TC: GH, (L1), (K0) and (K1) are invariant under smooth positive time changes. Positivity of entropy is also invariant (Ohno, Sun-Young-Zhou, Abramov, all cited from memory). So one may freely replace X by rho X.
- (P3) Lemma SV: under GH, a smooth invariant volume exists iff [d] = 0 in C^inf/X(C^inf), iff T(d) = 0 for all invariant distribution densities T.
- (P4) Lemma UE: under GH (indeed under (L1)) with a smooth invariant volume, the flow is uniquely ergodic, the volume is the only invariant distribution density, and there are no zeros or periodic orbits (dim >= 2). Consequences: smooth solvability of the cohomological equation with tame bounds, a uniform 1/T rate for ergodic averages, the spectral bound sigma_f((-eps,eps)) <= C eps^2 ||f||^2_{C^m}, and the dual Poincare inequality ||h||_{(C^m)^*} <= C||Xh||_{L^2}.
- (P5) Lemma CLT: in the volume case, a single smooth function whose time-one average has positive asymptotic variance under g_1 contradicts GH. Hence the volume case of (PE-NH) reduces to (V').

**Not proved / open:**
- (O1) **(V')**: does every smooth volume-preserving flow with positive metric entropy admit a smooth function that is not an L^2 (equivalently, not a smooth) coboundary, or that has positive asymptotic variance? Only the non-hyperbolic case is relevant here: in the hyperbolic case periodic orbits already give obstructions.
- (O2) **Case (ii)** ([d] != 0, no smooth invariant volume): nothing beyond the listed mu(d)-band result was obtained. The natural next questions are: must some invariant *probability measure* have mu(d) != 0? And if all have mu(d) = 0, can one use the uniform subexponential Jacobian bound together with Theorem J?
- (O3) Hence (PE-NH), and so the problem in dimension >= 4, remains open in this attempt. The first move does not solve Part 2. It yields only the reductions (P2)-(P5); it does not cover all measures or vector fields.

=== END OF ANSWER round8_q8 ===


