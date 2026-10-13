kind: attempt
Open question attempted: the headline claim itself (ledger [GOAL]: GH implies zero topological entropy), by TOPOLOGICAL-DYNAMICS routes that do not first need a smooth invariant volume — in particular proving that GH forces rigidity/equicontinuity-type behaviour, or directly building a GH-violating distribution from positive entropy.

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

Routes to try (choose; settle at least one decisively — a proof, or a precise reason it cannot work):
(R1) Uniform rigidity. If there are t_n -> infinity with g_{t_n} -> id uniformly on M, then every invariant measure is rigid, hence has no absolutely continuous spectral component, hence zero entropy (rigid transformations have zero entropy), and by the variational principle h_top = 0 (Glasner–Maon). Try to show GH implies uniform rigidity (or the weaker: for every ergodic invariant measure mu the Koopman group on L^2(mu) is rigid along some sequence). Diophantine linear flows on tori, the conjectured only GH examples, are rigid.
(R2) Asymptotic pairs. Positive topological entropy implies (Blanchard–Host–Ruette, for homeomorphisms; apply to g_1) the existence of asymptotic pairs x != y with d(g_t x, g_t y) -> 0; with Pesin theory for an ergodic measure of positive entropy (Ruelle inequality gives a positive exponent; Ledrappier–Young gives non-atomic unstable conditional measures) one gets y in W^u(x), not on the orbit of x, with exponential backward convergence, many of them in every neighbourhood of x. The distribution w = integral_{-inf}^0 (delta_{g_t x} - delta_{g_t y}) dt then satisfies L_X-type equation with right side +-(delta_x - delta_y). Try to integrate such pairs against smooth weights over smooth families (along unstable discs, along the flow, and — where possible — over a smooth transversal family) so that the right side becomes a smooth function while w stays non-smooth; that contradicts GH directly. Determine exactly what regularity of the family is needed and whether positive entropy supplies it (e.g. via a C^1 family of unstable discs on a Pesin block, or via the absolutely continuous unstable conditionals of a smooth measure).
(R3) Volume growth. For C^infinity maps, h_top equals the exponential growth rate of volumes of images of smooth discs (Yomdin, Newhouse). Look for a GH-violating distribution or an estimate violation built from a disc whose volume grows exponentially (e.g. pushforwards of smooth measures on the disc, or currents), using the tame estimate of Text B and the dual estimate (O1).

Dead ends already found (do not repeat): (i) the invariant pseudometric D(x,y) = sup{|u(x)-u(y)| : ||Xu||_{C^0} <= 1} is flow-invariant but infinite off orbits (even for Diophantine torus flows there is no measure S with transposed X S = delta_x - delta_y); with C^r norms of Xu instead, D is comparable to d but no longer invariant. (ii) The tame estimate alone holds also for transitive Anosov flows (Livsic theory, recalled), which have positive entropy; so the estimate on the range is not enough, and any proof must use GH or the fact that the range is ALL mean-zero functions (when a smooth invariant volume exists) — e.g. at periodic orbits or near-closed loops. (iii) Comparing ||u o g_t|| with ||f o g_t|| in the tame estimate gives nothing because of loss of derivatives.

Deliverable: a complete rigorous proof of the problem's claim if you can; otherwise the strongest rigorously proved statement (for instance: GH implies uniform rigidity under an extra hypothesis; or positive entropy plus GH yields a contradiction whenever some explicit regularity condition holds), with the remaining gap stated precisely. Cite only standard theorems, with the version used.
