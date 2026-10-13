kind: attempt
Open question attempted: the one other open link of this attempt's chain, ledger entry 16 (the non-hyperbolic core): under global hypoellipticity plus a smooth invariant volume, the volume cannot have a positive Lyapunov exponent together with a zero transverse exponent. Together with the missing statement (V) (attacked separately) it would complete the proof of the problem.

## Task
Prove the following statement (C), or find a counterexample.

**Statement (C).** Let M be a compact connected smooth manifold, X a smooth vector field on M that is globally hypoelliptic (every distribution u with Xu smooth is smooth) and preserves a smooth positive probability density omega. Then h_omega(g_1) = 0, where g_t is the flow of X. (By [R3-q4] below this is already proved when omega has no zero transverse Lyapunov exponent, so the case left is: omega has a positive exponent and a zero transverse exponent. Under these hypotheses the flow is uniquely ergodic, minimal, has no periodic orbits, every omega-mean-zero smooth f equals Xu with u smooth and ||u||_{C^k} <= C||f||_{C^m}, and — equivalently to GH here — the only distributions u with Xu = 0 are the constants.)

Why it suffices: given (V) (a GH field preserves a smooth volume; attacked separately), (C) and the variational principle with unique ergodicity give h_top = h_omega = 0, which is the problem.

Approaches NOT yet tried (pick, combine, or replace with your own; earlier dead ends are listed in the quoted results): (1) Non-smooth invariant distributions from measurable invariant geometric structures: an L^1 measurable vector field V with Dg_t V = V o g_t gives the invariant distribution phi -> int dphi(V) d omega, which must vanish (GH: invariant distributions of the form u omega are constant multiples of omega); more generally measurable invariant line fields or flags with a cocycle, the Oseledets centre bundle E^0, Pesin unstable foliation and its conditional measures — find one that yields a non-constant u in D' with Xu = 0, or a smooth f with no smooth solution of Xu = f. (2) Periodic-orbit or invariant-set producing results for non-uniformly hyperbolic systems with zero centre exponents (e.g. closing lemmas along the hyperbolic part, Ledrappier-Young entropy along the unstable foliation, entropy in the centre-unstable direction), turned into a non-constant invariant measure or distribution — anything other than omega contradicts unique ergodicity. (3) Exponential growth of ||Dg_t|| on a set of positive volume against the tame estimate, but using GH for NON-SMOOTH data (distributions built from unstable conditional measures, currents of integration over unstable discs pushed forward and renormalised) rather than smooth test functions, to avoid the derivative-loss obstruction. (4) A reduction showing that zero transverse exponents plus positive entropy force a measurable (or continuous) invariant fibration over a lower-dimensional factor, and a proof that GH passes to such factors.

A proof of (C) only for a sub-class (e.g. a dimension, or ergodic-theoretic extra assumptions) does not settle it, though it should be reported, with full proof, if it is all you found. Do not answer by recalling a proof from the literature: reason it out. Deliverable: a complete proof, a counterexample, or the strongest rigorously proved partial result with the exact point where the argument stops.

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

=== FURTHER RESULTS PROVED IN THE PREVIOUS ROUND (quoted verbatim from the workers' answers; each labelled with its source) ===

[R-a: at zeros]
Convention (Text B): ν is a smooth positive density, d = div_ν X, and a distribution u corresponds to the density uν. Then L_X(uν) = (Xu + d u)ν, so Xu = (L_X(uν))/ν − d u.

## P1 (proved). If X(p) = 0, then d(p) ≠ 0.
*Proof.* Let u be the distribution with uν = δ_p, i.e. ⟨u, φν⟩ = φ(p). For a test function φ, ⟨L_X δ_p, φ⟩ = −⟨δ_p, Xφ⟩ = −(Xφ)(p) = 0, because X(p) = 0. So L_X(uν) = 0, and therefore Xu = −d u = −d(p) u. (The product d·δ_p equals d(p)δ_p.) If d(p) = 0, then Xu = 0 with u not smooth. This contradicts GH (equivalently L1). ∎

The conclusion of P1 does not depend on the choice of ν. If ν' = e^{a}ν, then div_{ν'} X = d + Xa, and Xa(p) = 0 at a zero p.

[R-b: periodic orbits]
### Observation P (proved). How a periodic orbit interacts with GH.
Let γ be a closed orbit of period T, and let ν be a smooth positive density with d = div_ν X. The invariant measure μ_γ = ∫_0^T δ_{γ(t)} dt is a distribution density with L_X μ_γ = 0. As a distribution *function* u = μ_γ/ν it satisfies Xu = −d·u. This is a distribution supported on γ, so it is never smooth when dim M ≥ 2. Replacing ν by e^{a}ν (or using the time change hX, which by (O4) keeps GH) changes d into d + Xa (resp. h d + Xh). Restricted to γ, the equation d + Xa = 0 is solvable iff ∫_0^T d(γ(t)) dt = 0. That integral is the log of the Jacobian of the Poincaré return map, so this holds only when the Poincaré map preserves volume.
**Conclusion (proved):** if GH holds and dim M ≥ 2, X has no periodic orbit along which the linearised return map has Jacobian determinant 1. (Proof: if ∫_γ d = 0, pick a with d + Xa = 0 on γ. Then for ν' = e^{a}ν, div_{ν'}X vanishes on γ, so u = μ_γ/ν' satisfies Xu = −d' u = 0 (d' vanishes on supp u, and d'u as a product of a smooth function with a measure is 0). Hence u is constant by L1, which is a contradiction.)
This does not exclude dissipative periodic orbits. Horseshoes, and so positive entropy, can occur where all periodic orbits are dissipative. So P does not reach the goal.

=== FURTHER RESULTS UNDER HYPOTHESIS H (quoted verbatim from earlier workers' answers) ===
[R-c: consequences of hypothesis H = smooth invariant volume omega + unique ergodicity + every omega-mean-zero smooth f is Xu with u smooth (tame estimates)]
Standing assumptions are those of (S). In particular, ω is a smooth invariant probability volume. Every ω-mean-zero smooth f equals Xu with u smooth. Text B, Lemma 2 then gives, for each k, constants m = m(k) and C_k with ||u||_{C^k} ≤ C_k ||f||_{C^m} when u is normalised to ω-mean zero.

## P1 (proved). Uniformly bounded ergodic integrals.
For every smooth f, every x and every T:
|∫_0^T f(g_t x) dt − T ω(f)| ≤ 2C_0 ||f − ω(f)||_{C^m} ≤ 4C_0 ||f||_{C^m}.
*Proof.* Write f − ω(f) = Xu. Then d/dt u(g_t x) = (f − ω(f))(g_t x). Integrate and use |u| ≤ C_0 ||f − ω(f)||_{C^m}. ∎

## P2 (proved). The unstable-leaf formula with an ambient Lipschitz bound.
Let x, y satisfy d(g_{−t}x, g_{−t}y) → 0 as t → ∞, with the integral below converging. This holds, for example, for y on the Pesin unstable manifold of an ω-regular x, where the convergence is exponential. Then for every smooth f:
(i) u(x) − u(y) = ∫_{−∞}^0 (f(g_t x) − f(g_t y)) dt;
(ii) |∫_{−∞}^0 (f(g_t x) − f(g_t y)) dt| ≤ 2C_1 ||f||_{C^{m(1)}} d(x,y).

*Proof.* The constant ω(f) cancels in the difference, so we may take f of mean zero, with Xu = f. Then
u(x) − u(y) − [u(g_{−T}x) − u(g_{−T}y)] = ∫_{−T}^0 (f(g_t x) − f(g_t y)) dt.
The bracket tends to 0 because u is uniformly continuous. For (ii), use ||du||_{C^0} ≤ C_1 ||f − ω(f)||_{C^{m(1)}} and a geodesic between x and y. ∎

The analogous statements hold for stable manifolds, with the integral taken over [0, ∞).

## P3 (proved). The derivative cocycle identity.
For smooth f with f − ω(f) = Xu, every tangent vector v and every t:
du(Dg_t v) = du(v) + ∫_0^t df(Dg_s v) ds.
Consequently |∫_0^t df(Dg_s v) ds| ≤ 2C_1 ||f||_{C^{m(1)}} (|v| + |Dg_t v|).

*Proof.* We have L_X du = d(Xu) = df. Differentiate α(Dg_s v) in s, with α = du. ∎

## P4 (proved). Spectral decay at zero frequency.
Iterate the cohomological equation. For smooth mean-zero f there are smooth u_j with X^j u_j = f. Hence the spectral measure satisfies σ_f = λ^{2j} σ_{u_j}, so σ_f([−ε, ε]) ≤ ||u_j||_{L^2}^2 ε^{2j}.

## Dead ends (checked)
1. **P4 with Pinsker / Lebesgue spectrum.** This does not give a contradiction. In a countable Lebesgue spectrum component, the vectors whose spectral measure vanishes near 0 are dense, so the linear spectral data alone is consistent with positive entropy.

2. **P2 with Pesin theory, at first order.** For y on W^u(x), the integral in P2(i) is at most about ∫ |Dg_t (y − x)| dt ≈ d(x,y)/λ. This is already O(d(x,y)), so the Lipschitz bound P2(ii) produces no contradiction. To get one, a single f with bounded C^m norm would need df aligned with the displacement along the whole backward orbit. A recurrent orbit returns to the same region with different displacement directions, so such an f does not exist.

3. **P3.** The bound grows with |Dg_t v| itself, so it cannot rule out exponential growth of Dg_t. The identity is a tautology for exact forms. A contradiction would need solvability of L_X α = β for some non-exact 1-forms β, which (S) does not provide.

4. **Derivative growth against the tame estimate.** As the planner noted, this fails because derivatives are lost: ||f ∘ g_s||_{C^m} ~ e^{mLs}.

[R-d: spectral form, under the same hypothesis H]
## 1. Spectral estimate (proved)

Setting: omega is a smooth invariant probability volume. Then X is skew-symmetric on C^∞ ⊂ L²(omega), and its closure is skew-adjoint because the flow is unitary on L²(omega) (Stone's theorem). Write X = iA with A self-adjoint, and let P_ε = 1_{[-ε,ε]}(A) be the spectral projection.

**Proposition S.** There are m and C such that for every smooth f with ∫f omega = 0 and every ε > 0,
 ||P_ε f||_{L²} ≤ C ε ||f||_{C^m}.
Equivalently, the spectral measure σ_f satisfies σ_f([-ε,ε]) ≤ C² ε² ||f||²_{C^m}, and ∫ s^{-2} dσ_f(s) ≤ C²||f||²_{C^m}.

*Proof.*
1. By H (or by O2 together with Text B, Lemma 2 with ν = omega and k = 0), f = Xu, where u is smooth with mean zero and ||u||_{C^0} ≤ C||f||_{C^m}. Hence ||u||_{L²} ≤ C||f||_{C^m}.
2. Then P_ε f = i P_ε A u = i (A P_ε) u. Since ||A P_ε|| ≤ ε, we get ||P_ε f|| ≤ ε||u||.
3. For the second form: σ_f = s² σ_u, so ∫ s^{-2} dσ_f = ||u||². ∎

**Consequences.**
- The spectral measure of every smooth mean-zero f vanishes to second order at 0, uniformly in the C^m norm.
- In particular, the Green–Kubo variance of every smooth mean-zero f is 0. Equivalently, the ergodic integrals ∫_0^T f∘g_t are uniformly bounded (by 2C||f||_{C^m}), so no smooth observable satisfies a CLT with nondegenerate variance.

## 2. Missing lemma (open)

**(M)** Let g_t be a C^∞ flow that preserves a smooth volume omega, with h_omega(g_1) > 0. Then for every m there are smooth mean-zero f_n and ε_n → 0 such that
 ||P_{ε_n} f_n|| / (ε_n ||f_n||_{C^m}) → ∞.

(M) together with Proposition S contradicts H. Then Pesin's formula and the variational principle (the reduction in the earlier partial result) give h_top = 0.

**Why (M) is plausible.** By Rokhlin–Sinai, positive entropy gives countable Lebesgue spectrum on the orthocomplement of L²(Pinsker) (cited from memory). So there is F ∈ L² with σ_F equal to Lebesgue measure near 0, and hence ||P_ε F||² ≈ 2ε, which is much larger than ε².

**Why (M) is not proved.** Smooth f_n → F in L² need not inherit this: ||P_ε f_n|| can be as small as about ε·||f_n||_{C^m}, because the C^m norms blow up. One would need to approximate F by smooth functions whose C^m norm grows slower than ε^{-1/2} at the scale where ||P_ε(F − f_n)|| is small. This is a quantitative "smooth observables see the Lebesgue spectrum" statement, and it is exactly where the hard dynamics enters.

**The tame estimate alone cannot settle it (consistent with D1).** For Anosov flows, generic smooth f has positive Green–Kubo variance, so (M) holds there trivially. But that proof uses the hyperbolic structure (CLT for smooth observables), which is not available here. A plausible route is a CLT, or merely positive variance for a single smooth observable, for nonuniformly hyperbolic smooth-volume flows with positive entropy. Such a result is known in special cases (e.g. Young towers) but not, to my knowledge, in general.
=== END ===

[R3-q4: the reduction to the non-hyperbolic case, quoted verbatim]
# round3_q4: answer

**Status.** I did not prove the full core statement. What follows is:
- a proved reduction;
- a proved partial result: zero entropy when dim M ≤ 3, and more generally whenever ω has no zero transverse Lyapunov exponent;
- the exact missing lemma, stated precisely.

Results quoted from the literature are cited from memory.

## Setting
The hypotheses are H together with GH. By (O2), ω is the unique invariant probability measure. The flow has no zeros and no periodic orbits when dim M ≥ 2. I have checked (O2) myself: if μ is invariant, then v = μ/ω satisfies Xv = 0 in D', because div_ω X = 0. So v is constant by L1. A periodic orbit would carry an invariant probability measure different from ω.

## Step 1 (proved, using standard theorems). h_top(g_1) = h_ω(g_1).
This follows from the variational principle, h_top = sup over invariant probability measures μ of h_μ, because ω is the only invariant probability measure.

## Step 2 (standard). Exponents.
By Oseledets, ω-a.e. point has Lyapunov exponents of g_1. One of them is 0, in the flow direction. Call the others transverse and write them λ_1 ≥ … ≥ λ_{n-1}. Under H, ω is ergodic, so the exponents are constants. Since ω is a smooth invariant volume, the sum of all exponents equals ∫ div_ω X dω = 0. Pesin's formula (cited) gives h_ω = Σ λ_i^+. In particular, if h_ω > 0 then λ_1 > 0 and λ_{n-1} < 0.

## Step 3 (proved, citing Katok's theorem). If ω is hyperbolic, then h_ω = 0.
Here "hyperbolic" means that no transverse exponent is zero.

**Cited theorem.** Katok (1980) proved this for C^{1+α} diffeomorphisms. The flow version is in Katok's work and in Lian–Young (cited from memory). Let φ_t be a C^{1+α} flow without fixed points, and let μ be an ergodic hyperbolic invariant probability measure with h_μ > 0. Then φ_t has periodic orbits, in fact horseshoes, and h_μ is approximated by the entropies of the horseshoes.

**Proof of Step 3.** Suppose h_ω > 0. Since ω is hyperbolic, the theorem gives a periodic orbit. But Setting excludes periodic orbits. This is a contradiction, so h_ω = 0. ∎

## Corollary (proved). If dim M ≤ 3, then h_top = 0.
- **dim M = 1.** The flow is a rotation of the circle, or has zeros. Either way the entropy is 0.
- **dim M = 2.** Flows on surfaces have zero topological entropy. This follows from Ruelle's inequality: there is only one transverse exponent, and it equals 0 because the exponents sum to 0. So h_ω = 0, and Step 1 gives h_top = 0.
- **dim M = 3.** There are two transverse exponents λ_1 and λ_2, with λ_1 + λ_2 = 0. If h_ω > 0, then λ_1 = −λ_2 > 0, so ω is hyperbolic, and Step 3 gives a contradiction. Hence h_top = h_ω = 0.

## Reduction (proved). The core statement is equivalent to the following lemma.

**Missing Lemma (open).** Let g_t be a C^∞ flow on a compact manifold with the following properties:
- it preserves a smooth volume ω;
- it is uniquely ergodic and has no periodic orbits;
- it satisfies GH (and hence H, by the background results);
- ω has positive exponents.

Then ω has no zero transverse exponent.

**Why the lemma implies the core.** Assume the lemma and suppose h_ω > 0. Then ω has a positive exponent (Step 2), so by the lemma ω is hyperbolic, and Step 3 gives a contradiction. So h_ω = 0, and Step 1 gives h_top = 0.

**Equivalent form.** "The lemma" can be replaced by "h_ω > 0 is impossible for ω with a zero transverse exponent". The first open case is dim M = 4 with transverse exponents (λ, 0, −λ).

## Directions examined and not completed
None of these is claimed as proved.
- **(i) Martingale construction.** One could build a non-smooth L^1 solution U of XU = f from conditional expectations onto an increasing partition subordinate to W^u. The obstruction is that such a sum is the smooth solution u itself whenever f is a coboundary, and every mean-zero smooth f is a coboundary. So no non-smooth candidate arises unless f is non-smooth. Then N3 does not apply.
- **(ii) and (iii) Zero exponents.** I found no mechanism by which GH controls the centre directions E^0. The tame estimate loses derivatives (dead end 4 of R-c), so it cannot control subexponential growth or exponential growth along E^0 or E^u.

## Summary
- **Proved:** zero topological entropy under H+GH when dim M ≤ 3, and in any dimension whenever ω has no zero transverse exponent.
- **Open:** the Missing Lemma above, that is, the non-hyperbolic case.


[R3-q3: further results and dead ends under H, quoted verbatim]
# round3_q3: answer (partial; the core is NOT settled)

Plan: check the facts F1–F3 listed in the query, try directions (i) and (ii), and record what is proved and what fails.

## 1. Correction: (F2) is false as stated
(F2) claims that x -> I_T f(x) := ∫_0^T f(g_t x) dt is Lipschitz with a constant that does not depend on T. But I_T f = u∘g_T − u, so
Lip(I_T f) ≤ Lip(u)·Lip(g_T) + Lip(u),
and Lip(g_T) is exactly the quantity that grows exponentially when entropy is positive (Ruelle's inequality). The identity gives no bound uniform in T. The correct uniform statement is only the C^0 bound P1/F1:
|I_T f − Tω(f)| ≤ 2C_0‖f‖_{C^m}.
Direction (i), as proposed, depends on F2, so it collapses. Writing out the same difference along two orbits gives
u_i(g_t x) − u_i(g_t y) = [u_i(x) − u_i(y)] + ∫_0^t (f_i(g_s x) − f_i(g_s y)) ds.
This is a tautology, and its integral term is bounded only by 2 sup|u_i|. That bound is O(1), not O(d(x,y)). So it gives no control of separation at scales below the diameter.

## 2. Verified: (F1) gives polynomial uniform return times. Dead end for entropy
**Lemma R (proved).** There are m and C such that, for every z and every ε < 1, every orbit segment of length T ≥ C ε^{-m-n} meets B(z,ε). Here n = dim M.

*Proof.* Take a bump function f with 0 ≤ f ≤ 1, support in B(z,ε), f = 1 on B(z,ε/2), and ‖f‖_{C^m} ≤ C ε^{-m}. Then ω(f) ≥ c ε^n. By P1, ∫_0^T f(g_t x) dt ≥ T c ε^n − 4C_0 C ε^{-m}, and this is > 0 once T ≥ C' ε^{-m-n}. ∎

**Why this is a dead end (checked).** Polynomial return times do not imply zero entropy. In a minimal uniquely ergodic subshift with entropy h > 0, a cylinder of length k has measure about e^{-hk}. The metric ball of radius ε = 2^{-k} is such a cylinder, and its return time is about e^{hk} = ε^{-h/log 2}. That is polynomial in 1/ε. Uniform discrepancy at the level of one-point statistics (visit frequencies of balls) is therefore compatible with positive entropy. Entropy is a statement about the *order* of visits, i.e. about joint statistics of (g_t x, g_{t+s} x). Those statistics involve the functions a·(b∘g_s), whose C^m norms grow like e^{mLs}. This is the same loss of derivatives as dead end 4 of R-c. So direction (ii) only goes through if one can control visit patterns at scale ε over time T using a fixed number of smooth observables. Pigeonholing over ~e^{hT} separated segments needs about e^{hT} distinct test functions, and the O(ε^{-m}) error then accumulates. I could not close this gap.

## 3. Attempted route via periodic orbits and invariant non-smooth functions (GH only)
Suppose γ is a hyperbolic periodic orbit with Poincaré map P (positive entropy plus a hyperbolic measure gives such orbits by Katok's horseshoe theorem, cited from memory, for C^{1+α} flows). Take a 1-dimensional unstable eigenvalue λ_u > 1 and stable eigenvalue 0 < λ_s < 1. Then w = y_u^{2k} |y_s|^b, with b = 2k log λ_u / |log λ_s|, is invariant under the linear P. It is continuous, and it is not smooth if b is not an even integer. This would produce a non-smooth distribution solution of Xu = 0 locally. **Obstruction (checked):** w is singular along the whole local unstable manifold {y_s = 0}. Cutting off with χ gives Xu = (Xχ)w, which is singular where supp Xχ meets W^u(γ). Every function of w that is nonzero near γ is also nonzero along the axes, which leave the box. So no global distribution with smooth Xu results. Distributions supported on γ (transverse derivatives of δ) satisfy Xu = 0 only under the resonance Π|λ_i|^{α_i+1} = 1, which is not available in general. The no-volume case already appears in R-b (∫_γ d = 0).

## 4. Status
- Proved here: Lemma R. Also the correction that F2 is false, together with the reason (Lip(g_T) enters).
- Not proved: the core claim. It remains open in this run that H (+GH) implies h_ω = 0, i.e. that ω has no positive Lyapunov exponent.
- Precise missing lemma (equivalent to (M) of R-d, restated): *if g_t preserves a smooth volume ω with h_ω > 0, then for every m, sup over smooth mean-zero f of ‖P_ε f‖_{L²} / (ε‖f‖_{C^m}) = ∞ as ε → 0.* Equivalently: some C^∞ observable has ergodic integrals ∫_0^T f∘g_t that are not uniformly bounded (for instance, it has positive Green–Kubo variance). Proving this needs a CLT-type, or merely unbounded-deviation, result for smooth observables of general nonuniformly hyperbolic volume-preserving flows. I do not know such a result in that generality.
- Dead ends added: (a) direction (i), because it relies on the false F2; (b) direction (ii) through one-point discrepancy, by the subshift example; (c) local invariant functions at hyperbolic periodic orbits, because cut-offs fail along W^u.

