kind: attempt
Open question attempted: the missing statement (PE-NH) of this attempt's chain (ledger entry 70), attacked by a named approach not yet tried: an invariance-principle / accessibility dichotomy for the zero-exponent centre, feeding the configuration criterion Theorem G.

## Task
Prove the missing statement (PE-NH) below (or directly the problem's claim), or a counterexample, by the following named approach (you may depart from it if you say why). Theorem G (blocks R7-a, R7-f; ledger entry 72) proves under GH: no finite configuration of distinct points with Jacobian growth below the rate, grouped into exponentially forward-asymptotic classes and exponentially backward-asymptotic classes (flow shifts allowed), carries a nonzero class-wise cancelling weight vector; in particular there is none with more points than classes. For a positive-entropy ergodic mu with mu(d) = 0 (lambda = 0, the hard case), any finite configuration of mu-generic points in which the weak-stable / weak-unstable incidence graph has a component with two independent cycles contradicts GH (Proposition 4.1 of R7-a, Proposition 2.1 of R7-f). Round 7 found that for non-hyperbolic mu such configurations are not supplied by Pesin theory, because closing an su-path costs c - 1 >= 1 real conditions in the genuine centre (block R7-f §3), and that smearing along the centre gives no decay.
Named approach — a dichotomy for the zero-exponent centre: use the invariance principle (Ledrappier 1986 for cocycles with zero exponents; Avila-Viana 2010; Avila-Santamaria-Viana 2013; or Tahzibi-Yang for diffeomorphisms with partially hyperbolic structure; cite precisely the statement you use, and check its hypotheses — they are usually stated for partially hyperbolic or skew-product settings and you will need a non-uniform version, or a reduction to one) applied to the non-hyperbolic positive-entropy mu, together with Ledrappier-Young theory and non-atomic stable and unstable conditionals (Lemma 6.0 of R6-a). Branch 1 ("twisting"): su-paths of mu-generic points close modulo the flow, often enough to produce a Theorem-G configuration (for instance two independent closed weak su-cycles in one component, or N > p + q points). Branch 2 ("rigid"): the disintegration of mu along the centre is invariant under stable and unstable holonomies (or the centre is jointly integrable with E^s + E^u on a positive-measure set), and this rigid structure is contradicted by GH — e.g. it produces an invariant distribution not proportional to an admissible one (contradicting L1/(K0)), a non-smooth solution of Xu = f smooth, a configuration for Theorem G, or a distribution with two-sided decay for Theorem J / J* (block R7-a). Make either branch, or the dichotomy itself, rigorous; if the dichotomy cannot be established, identify the exact missing property and whether GH could supply it.

A proof covering only some of the measures or vector fields (e.g. only partially hyperbolic ones, only skew products, only the volume-preserving case) does NOT answer the question, though it should be reported (with full proof) if it is all you found. Standard theorems may be cited by name (say exactly which statement). Write your plan and partial results into your answer as you go.

**Missing statement (PE-NH).** Let M be a compact connected smooth manifold and X a smooth vector field on M with flow g_t, such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Then there is no ergodic flow-invariant Borel probability measure mu on M such that (a) h_mu(g_1) > 0 and (b) the Lyapunov exponent 0 of the C^inf diffeomorphism g_1 with respect to mu has multiplicity at least 2 (i.e. mu is non-hyperbolic: besides the exponent 0 of the flow direction there is a further zero exponent). (By entries 61 and 62 below, a proof may assume dim M >= 4 and, if useful, mu(d) in {0} ∪ (-inf, -chi^+_min] ∪ [|chi^-_max|, inf), where d = div_nu X for a smooth positive density nu, chi^+_min is the smallest positive and chi^-_max the negative exponent of mu closest to 0; mu(d) is the sum of all exponents of mu.)

=== THE CHAIN OF THIS ATTEMPT ===
**Chain.**
1. (Missing statement, PE-NH; ledger entry 70) Under GH no ergodic flow-invariant mu has h_mu(g_1) > 0 and a zero Lyapunov exponent of multiplicity >= 2.
2. (Entry 60, PROVED modulo Ruelle's inequality and the Katok/Lian-Young horseshoe theorem for flows; uses Theorem J (entry 56) through Lemma K / no-homoclinic (entry 57)) Under GH with dim M >= 2, every ergodic flow-invariant mu with h_mu(g_1) > 0 has a zero exponent transverse to X, i.e. exponent 0 of multiplicity >= 2. (For dim M = 1, M is a circle and g_1 is a circle homeomorphism: entropy 0.)
3. By 1 and 2, every ergodic flow-invariant mu has h_mu(g_1) = 0 (this is (PE), entry 53's claim).
4. Classical (variational principle, checked by round5_q2, round6_q1 §5, round6_q10 §6, round7_q3 §1, round7_q10 §1): h_top(g_1) = sup h_m(g_1) over g_1-invariant m; for such m, mbar = int_0^1 (g_s)_* m ds is flow-invariant with h_mbar(g_1) = h_m(g_1) (g_s conjugates g_1 to itself; entropy affine, Jacobs); by the flow-ergodic decomposition of mbar and Jacobs' formula, h_m(g_1) <= sup over flow-ergodic mu of h_mu(g_1) = 0 by 3. Hence h_top(g_1) = 0, the [GOAL]. (Entry 61 already gives the [GOAL] for dim M <= 3 independently.)
Alternative chain (round 8, for the record): (J1) [entry 81] applied to X and to -X, plus Pesin local stable/unstable manifolds, Ruelle's inequality and Lemma 6.0 (non-atomic conditionals), gives step 3 directly for every ergodic mu, bypassing step 2 and the Katok/Lian-Young citation. J1 is stronger than PE-NH, so it is posed as the hardest step of the sketch, not as the missing statement.
=== END OF CHAIN ===

=== THE PLANNER'S SKETCH (context; free to discard) ===
**Why it should hold (planner sketch, revised in round 8).**
(1) One-sided cancellation is free. Let mu be ergodic with h_mu(g_1) > 0, lambda = mu(d), chi^+_min > 0 > chi^-_max, 0 < delta small. If lambda = 0, take mu-generic x != y in one Pesin local unstable leaf (Lemma 6.0), S = delta_x - e^b delta_y: |S(e^{J_t} phi∘g_t)| <= C e^{-(theta-delta)|t|}||phi||_{C^1} for t <= 0 (theta < chi^+_min) and <= C e^{delta t}||phi||_{C^0} for t >= 0. If lambda > 0, take x != y in one local stable leaf: decay e^{-(lambda-delta)|t|} backward (weight), growth <= e^{max(0, lambda - theta' + delta) t} forward. If lambda < 0, the same for -X (GH by (O4)). In every case the decay rate eps exceeds the growth rate a >= 0 on the other side.
(2) Hence (J1) [entry 81] — "under GH no nonzero S decays like e^{-eps|t|} as t -> -inf and grows at most like e^{at}, a < eps, as t -> +inf" — implies PE outright. Theorem J is the case of decay on both sides (a < 0). In Laplace form J1 says: no polynomially bounded holomorphic eigenfamily T_z(P phi) = z T_z(phi) on the strip a < Re z < eps whose backward half B_z(phi) = int_{-inf}^0 e^{-zt} F_phi(t) dt (holomorphic on the half-plane Re z < eps, which contains 0) satisfies B_z(P phi) - z B_z(phi) = S(phi). At z = 0 the Taylor coefficients give B_0∘P = S, B_j∘P = B_{j-1}, with |B_j| <= eps^{-j-1}|S|-type bounds: S is infinitely P^T-divisible with geometrically bounded divisors. Candidate mechanism: combine this with the tame dual solvability of block R7-d (Lemma B(iii)) (divisors of controlled order, unique mod nu by (K0), normalised by (K1)) and with the forward half F_z (holomorphic on Re z > a) to force a holomorphic continuation of T_z to a neighbourhood of 0, whereupon Theorem J (Lemma M form) kills it. I cannot close it: GH speaks about P at z = 0 only, and shifting the weight (J_t -> J_t + ct) would need a smooth w with Xw = c, which is exactly what (K1) forbids.
(3) Closed range must enter somewhere (block R7-b). In the volume case Theorem V asks for C^1-dense quasi-analytic vectors of X^{-1}; the natural candidates rho(A)phi = int rho^(t) phi∘g_t dt with rho flat at 0 need rho^ of non-quasi-analytic decay and are then smooth only if ||Dg_t|| grows subexponentially — circular. So the tame inverse must be used on objects not built by transporting smooth functions (e.g. on the divisors B_j of (2), or on Hahn-Banach solutions S_{pq} of S∘X = delta_p - delta_q for pairs p, q).
(4) Fallback mechanism: an accessibility dichotomy for the zero-exponent centre (invariance principle of Ledrappier / Avila-Viana type): either su-paths of good points close modulo the flow often enough to give a Theorem-G configuration with more points than classes, or the conditionals along the centre are su-holonomy invariant, giving a measurable structure to be contradicted by GH (ergodicity of the Lebesgue class, Lemma D of block R7-d; Theorem G of blocks R7-a, R7-f).
=== END OF SKETCH ===

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

=== LEMMAS C-F (written by the planner of this attempt and checked line by line by seven independent workers: all correct; only the heteroclinic part of Corollary C1 is a sketch. Entry S8 cited in Lemma E(iii) is: under GH, an a.c. invariant probability whose density rho has rho^{-eps} in L^1 for some eps > 0 gives a smooth invariant volume) ===
Conventions: nu is a smooth positive density on M, d = div_nu X (so L_X nu = d nu and L_X(phi nu) = (X phi + d phi) nu), J_t(x) = int_0^t d(g_s x) ds for all real t (so J_t(x) = log of the nu-Jacobian of g_t at x, d/dt J_t(x) = d(g_t x), and J_{t+r}(x) = J_r(x) + J_t(g_r x)). A distribution u is identified with the functional phi -> <u, phi nu> on smooth phi, and <Xu, phi nu> = -<u, (X phi + d phi) nu>. "L1" is the result that every distribution u with Xu = 0 is constant (Text A).

Observation 0 (dictionary). A finite (signed) Borel measure T on M defines the distribution u = T/nu by <u, phi nu> = T(phi). Then <Xu, phi nu> = -T(X phi + d phi). So Xu = 0 iff T(X phi + d phi) = 0 for all phi, i.e. iff L_X T = d T in the sense of densities ("T is nu-conformal"). Invariant measures mu (L_X mu = 0) instead give v = mu/nu with Xv = -d v. By L1: under GH the only finite measures T with T(X phi + d phi) = 0 for all phi are the constant multiples of nu.

Lemma C. Assume GH and dim M >= 2. Then for every x in M, int_{-inf}^{inf} e^{J_t(x)} dt = infinity.
Proof. If x is a zero of X, J_t(x) = t d(x) and the integral diverges. If x is periodic of period P, then J_{t+P}(x) = J_t(x) + J_P(x), so the integrand is not integrable on R. Otherwise t -> g_t x is injective. Suppose c(t) := e^{J_t(x)} is integrable on R. Since c' = d(g_t x) c, we have c(t) >= c(s) e^{-||d||_inf |t-s|}; if c(t_n) >= eps along t_n -> +inf (or -inf), c >= eps e^{-||d||} on infinitely many disjoint unit intervals, contradicting integrability; so c(t) -> 0 as |t| -> inf. Define the positive finite measure T(phi) = int_R c(t) phi(g_t x) dt. For smooth phi, d/dt [c(t) phi(g_t x)] = c(t)[(X phi)(g_t x) + d(g_t x) phi(g_t x)], so T(X phi + d phi) = lim_{R->inf} [c phi(g_. x)]_{-R}^{R} = 0. By Observation 0 and L1, T = K nu for a constant K. But T is carried by the orbit of x, a countable union of compact C^1 arcs, which is nu-null since dim M >= 2, while T(M) = int c > 0. Contradiction. QED
Corollary C1. Under GH (dim M >= 2) there is no orbit x with J_t(x) <= b - a|t| for all t (some a > 0). In particular there is no orbit backward-asymptotic (along its strong unstable manifold) to a hyperbolic periodic orbit or zero with int_gamma d > 0 and forward-asymptotic (along its strong stable manifold) to one with int_gamma d < 0 (exponential convergence makes J_t(x) - J_t(y) converge, y the asymptotic phase). Hence in any horseshoe (transitive hyperbolic set, all periodic orbits heteroclinically related) all periodic orbits have int_gamma d of the same strict sign (sign 0 is excluded by entry #4: Jacobian-1 periodic orbits do not exist).

Lemma D (Patterson-type equidistribution). Assume GH. Let x satisfy P(s) := int_R e^{J_t(x) - s|t|} dt < infinity for every s > 0 (this holds iff limsup_{|t|->inf} J_t(x)/|t| <= 0). Let T_s(phi) = P(s)^{-1} int_R e^{J_t(x) - s|t|} phi(g_t x) dt (a probability measure). Then T_s -> nu/nu(M) weak* as s -> 0+.
Proof. With c_s(t) = e^{J_t(x) - s|t|} (Lipschitz, c_s' = (d(g_t x) - s sign t) c_s a.e., c_s -> 0 at +-inf as in Lemma C), integrating d/dt[c_s phi(g_t x)] over R gives int c_s (X phi + d phi)(g_t x) dt = int s sign(t) c_s(t) phi(g_t x) dt, so |T_s(X phi + d phi)| <= s ||phi||_inf. Any weak* limit point T (a probability measure) satisfies T(X phi + d phi) = 0 for all phi, so by Observation 0 and L1, T = nu/nu(M). Compactness gives convergence of the whole family. QED
Corollary D1. Under GH, every ergodic invariant probability mu with mu(d) = 0 has supp mu = M. (Take x mu-generic in both time directions with x in supp mu: J_t(x)/t -> 0 as t -> +-inf, so Lemma D applies; T_s is supported in the closure of the orbit of x, contained in supp mu, and the limit nu/nu(M) has full support.)
Remark. Lemma D says GH already gives "unique ergodicity for Jacobian-weighted orbit averages" (the nu-conformal structure). (V) is the same uniqueness for unweighted averages, i.e. for the transposed operator; under (V) the two coincide (J_t is then a bounded coboundary).
Observation D2 (Jensen). For t real, int_M e^{J_t} d nu = nu(M), so int J_t d nu <= 0 for t > 0 and for t < 0. Hence weak* limits of (1/T) int_0^T (g_t)_* nu-hat dt are invariant probabilities mu_+ with mu_+(d) <= 0, and those of (1/T) int_{-T}^0 (...) dt give mu_- with mu_-(d) >= 0 (nu-hat = nu/nu(M); check the signs when you use this).

Lemma E (unique ergodicity case). Assume GH, dim M >= 2, and that the flow is uniquely ergodic with invariant probability mu. Then (i) mu(d) = 0; (ii) supp mu = M and the flow is minimal; (iii) X preserves a smooth positive density iff sup_{t>=0} |J_t(x0)| < infinity for some x0.
Proof. (i) By UE, J_t(x)/t -> mu(d) uniformly in x as t -> +inf. If mu(d) < 0 then int e^{J_t} d nu -> 0, contradicting int e^{J_t} d nu = nu(M); if mu(d) > 0 use t -> -inf similarly. (ii) Corollary D1 gives supp mu = M; every orbit closure carries an invariant probability, which must be mu, so every orbit closure is M. (iii) If omega = rho nu is a smooth invariant positive density, J_t = log rho - log rho o g_t is bounded. Conversely, if J_t(x0) is bounded for t >= 0, the Gottschalk-Hedlund theorem (minimal flow, continuous d; cited) gives a continuous a with J_t(x) = a(g_t x) - a(x) for all x, t; then rho = e^{-a} satisfies rho o g_t e^{J_t} = rho, so rho nu is an invariant measure with continuous positive density, and entry S8 (a.c. invariant probability with density bounded below gives a smooth invariant volume) finishes. QED

Lemma F (adjoint reformulation). (V) holds iff the operator P = X + d acting on functions is GH (every distribution w with Pw smooth is smooth).
Proof. If omega = rho nu is smooth invariant positive, then X rho = -d rho and P(rho w) = rho X w, so P is conjugate to X by multiplication by rho, hence GH. Conversely, assume P GH. For any invariant probability mu, w = mu/nu satisfies Pw = 0 (L_X(w nu) = (Xw + dw) nu), so mu = rho nu with rho smooth, rho >= 0. If mu is ergodic, {rho > 0} is open, invariant, nonempty, hence conull (N1); two distinct ergodic measures are mutually singular, so the flow is uniquely ergodic, mu = rho nu. Z = {rho = 0} is closed and invariant; if nonempty it carries an invariant probability, which must be mu, but mu(Z) = 0; so rho > 0 everywhere. QED (N1 uses GH of X.)
=== END OF LEMMAS C-F ===

=== FURTHER RESULTS OF THE PREVIOUS ROUND (quoted verbatim from the workers' answers; GH-consequences without volume unless stated) ===
[R4-q7, section 2: no GH needed]
## 2. Two elementary facts about the exponent of d

**Proposition 2.1 (proved).** There are ergodic invariant probabilities μ_+ and μ_− with μ_+(d) ≥ 0 ≥ μ_−(d). This needs no GH.

*Proof.*
1. Standard fact: limsup_{t→+∞} sup_x J_t(x)/t = max_μ μ(d) over invariant probabilities.
   - Take x_t and t → ∞ achieving the sup. The empirical measures (1/t)∫_0^t δ_{g_s x_t} ds have invariant weak* limits μ, and μ(d) equals the limit of J_t(x_t)/t.
   - The maximum is attained at an ergodic measure, since μ ↦ μ(d) is affine and continuous.
2. If max_μ μ(d) < 0, then J_t ≤ −ct on all of M for large t, so ∫ e^{J_t} dν → 0. But this integral equals ν(M) for every t, a contradiction.
3. The case t → −∞ is the same and gives μ_−. ∎

**Proposition 2.2 (tilted conformal measures; proved, assuming only that X is a smooth vector field).** Let μ be ergodic with λ = μ(d). Then there is a Borel probability T with supp T ⊂ supp μ and
T(Xφ + dφ) = λ·T(φ) for all smooth φ.
Equivalently, u = T/ν is a nonnegative measure-distribution with Xu = −λu.

*Proof.*
1. Take x μ-generic in both time directions. Then J_t(x) − λt = o(|t|) as t → ±∞. For t < 0 this holds because J_t = −∫_t^0 d∘g_s ≈ λt.
2. So c_s(t) = e^{J_t(x) − λt − s|t|} is integrable for every s > 0 and tends to 0 at ±∞, as in Lemma C.
3. Integrating d/dt[c_s φ(g_t x)] = c_s·(Xφ + dφ − λφ − s·sign t·φ) shows that the normalised measures T_s satisfy |T_s(Xφ + dφ − λφ)| ≤ s‖φ‖_∞.
4. Take a weak* limit as s → 0. The support claim holds because supp T_s lies in the orbit closure of x, which lies in supp μ. ∎

When λ = 0 this is Lemma D, and GH then forces T = ν̂. When λ ≠ 0, GH does not visibly exclude a positive eigen-distribution Xu = −λu. This is one of the places where I am stuck (see §4).

[R4-q4, B3-B4: GH, dim M >= 2]
### B3. No proper closed invariant set has a basin of positive volume (generalises R3-q1(b))
Assume GH and dim M ≥ 2. Let K ≠ M be a closed invariant set. Then the basin W(K) = {x : dist(g_t x, K) → 0 as t → +∞} is ν-null. By (O4) applied to −X, the same holds for the backward basin.

*Proof.*
1. W(K) is invariant. If ν(W) > 0, then W is conull by N1.
2. ν(K) = 0. Otherwise K is conull, and a closed conull set is all of M, since ν has full support.
3. Hence A_ε = {x ∈ W : dist(x, K) ≥ ε} has positive measure for some ε > 0.
4. Each x ∈ A_ε visits A_ε only during a bounded set of times.
5. Step 4 contradicts conservativity (N2): by Halmos recurrence, a.e. x ∈ A_ε returns to A_ε at arbitrarily large times. ∎

This excludes many things at once:
- attracting invariant tori and graphs, including non-uniformly attracting ones, provided their basin has positive volume;
- SRB-type attractors;
- in particular, any invariant measure that is physical (a basin of positive volume) and different from ν̂.

### B4. Hopf criterion
Under GH, ∫_0^∞ e^{J_t(x)}dt = ∞ for ν-a.e. x, and likewise backwards.

*Proof.* This is Hopf's characterisation of the conservative part (cited from memory: for a nonsingular flow, the conservative part is, mod ν, the set where ∫_0^∞ (d(g_t^*ν)/dν)(x)dt = ∞), combined with N2. ∎

Consequence. Every ergodic μ with μ(d) ≠ 0 has a ν-null statistical basin. This is consistent with B3.

[R4-q5, Lemma H; 'E8' there means: at a zero p, d(p) != 0 (result P1 above)]
**Lemma H (jet non-resonance at zeros; extends E8).** Under GH, if X(p) = 0 and lambda_1..lambda_n are the eigenvalues
(with multiplicity) of A = DX(p), then tr A + sum alpha_i lambda_i != 0 for every multi-index alpha in N^n.
*Proof.* In coordinates at p let V_k = span{ phi -> (partial^alpha phi)(p) : |alpha| <= k }, viewed as generalized
functions via phi nu <-> phi; finite-dimensional. For u in V_k, (Xu)(phi) = -u(X phi + d phi). Since X(p)=0,
partial^alpha (X_i partial_i phi)(p) involves only derivatives of phi of order <= |alpha|, with top-order part
sum_{i,j} alpha_j (partial_j X_i)(p) partial^{alpha - e_j + e_i} phi(p); and d(p) = tr A. So V_k is X-invariant and on
V_k/V_{k-1} X acts as -(tr A + (derivation induced by A on degree-k symmetric tensors)), with eigenvalues
-(tr A + alpha.lambda), |alpha| = k. A zero eigenvalue would give 0 != u in V_k with Xu = 0, u not smooth,
contradicting GH. QED
(This forbids resonant zeros but does not forbid zeros; global stable/unstable manifolds of saddles obstruct the
local cut-off constructions that work for sinks/sources, cf. E13.)


[R4-q10: under GH plus a smooth invariant volume omega. Planner's note: the proof of Lemma B uses only GH and de Rham theory for currents, not the volume; Lemmas A and C use the volume (C(ii) also uses unique ergodicity, which follows from the volume by (O2)). 'Statement (C)' there is: under GH + smooth invariant volume, h_omega(g_1) = 0.]

Standing setting: (C)'s hypotheses. X is GH and preserves a smooth positive probability density omega.
We use L1 from the background in the form "an invariant distribution density is c·omega". Proof: T = u·omega
with L_X T = (Xu) omega because div_omega X = 0, so Xu = 0 and u is constant by L1.
Fix a Riemannian metric on M.

## Lemma A (proved). Measurable invariant vector fields are divergence-free.
Let V be a measurable vector field with |V| in L^1(omega) and Dg_t V(x) = V(g_t x) for omega-a.e. x, for each t.
Then ∫ dφ(V) omega = 0 for every smooth φ. That is, div_omega V = 0 in the sense of distributions.

*Proof.* T(φ) := ∫ dφ(V) dω is a distribution of order 1, since |T(φ)| ≤ ||dφ||_∞ ||V||_{L^1}.
We have d(φ∘g_t)_x(V(x)) = dφ_{g_t x}(Dg_t V(x)) = (dφ(V))(g_t x).
So T(φ∘g_t) = ∫ (dφ(V))∘g_t dω = T(φ), by invariance of ω.
As t → 0, (φ∘g_t − φ)/t → Xφ in C^1, so T(Xφ) = 0. Thus T is an invariant distribution density, T = cω,
and T(1) = 0 forces c = 0. ∎

## Lemma B (proved). GH extends to closed 1-currents.
Let α be a closed 1-current (a 1-form with distribution coefficients, dα = 0) such that L_X α is smooth. Then α is smooth.

*Proof.* By de Rham–Hodge theory for currents, α = h + du with h a smooth harmonic 1-form and u in D'.
(A closed current is cohomologous to its smooth harmonic representative, by de Rham's theorem for currents.)
Cartan's formula gives L_X α = d i_X α, and the same for h. So L_X α − L_X h = d(Xu), and this is a smooth exact form.
A distribution w with dw smooth is smooth up to a constant. (Locally dw = β smooth and closed; write β = dw_0 with
w_0 smooth; then d(w − w_0) = 0, so w − w_0 is locally constant.) Hence Xu is smooth. By GH, u is smooth, and so is α. ∎

## Lemma C (proved). Conformal measures on the unit tangent bundle and eigen-distributions.
Let SM be the unit sphere bundle. Define ĝ_t(v) = Dg_t v / |Dg_t v|, A_t(v) = log|Dg_t v|, and
a(v) = d/dt|_{t=0} A_t(v) = ⟨∇_v X, v⟩, which is smooth on SM. The cocycle identity is A_{s+t}(v) = A_t(v) + A_s(ĝ_t v).

(i) There are a Borel probability measure S on SM and a real P with
 ∫ e^{A_t} (Ψ∘ĝ_t) dS = e^{Pt} ∫ Ψ dS for all continuous Ψ and all t ≥ 0.
(ii) P = ∫ a dS, and P lies in [λ_min, λ_max], the range of the Lyapunov exponents of ω (the flow exponent 0 included).
(iii) The distribution T_S(φ) := ∫ dφ(v) dS(v) satisfies T_S(φ∘g_t) = e^{Pt} T_S(φ) and T_S(Xφ) = P·T_S(φ),
 i.e. L_X T_S = −P T_S. Also T_S(1) = 0.
(iv) If P = 0, then T_S = 0, i.e. the 1-current C_S(β) = ∫ β(v) dS(v) is closed.

*Proof.* (i) Let K = Prob(SM) with the weak* topology. K is compact and convex.
Define Φ_t(m)(Ψ) = ∫ e^{A_t} Ψ∘ĝ_t dm / ∫ e^{A_t} dm. This is continuous on K, because e^{A_t} > 0 and both
e^{A_t} and Ψ∘ĝ_t are continuous. The cocycle identity gives Φ_s∘Φ_t = Φ_{s+t}.
By Schauder–Tychonoff, F_k = Fix(Φ_{2^{-k}}) is nonempty and compact. Since Φ_{2^{-k}} = Φ_{2^{-k-1}}∘Φ_{2^{-k-1}},
we have F_{k+1} ⊂ F_k. So ∩F_k is nonempty, and any S in it is fixed by Φ_t for every dyadic t ≥ 0.
The map t ↦ Φ_t(S)(Ψ) is continuous, so S is fixed by every t ≥ 0.
Put c_t = ∫ e^{A_t} dS. Then c_{s+t} = c_t · Φ_t(S)(e^{A_s}) = c_t c_s. Since c is continuous and positive,
c_t = e^{Pt}, and differentiating at t = 0 gives P = ∫ a dS.
(ii) For every t, P = (1/t) log ∫ e^{A_t} dS lies between min_v A_t(v)/t and max_v A_t(v)/t.
Let v_t be a maximiser. Any weak* limit point of the empirical measures (1/t)∫_0^t δ_{ĝ_s v_t} ds is ĝ-invariant;
call it m. Then ∫ a dm = lim (1/t) A_t(v_t). Decompose m into ergodic components. Each component projects to an
invariant measure on M, which is ω by unique ergodicity (O2). By Birkhoff and Oseledets, its integral of a is a
Lyapunov exponent of ω. So lim sup max_v A_t/t ≤ λ_max. The lower bound is symmetric.
(iii) For unit v we have e^{A_t(v)} dφ(ĝ_t v) = dφ(Dg_t v) = d(φ∘g_t)(v). Apply (i) with Ψ(v) = dφ(v).
Then differentiate at t = 0, using (φ∘g_t − φ)/t → Xφ in C^1.
(iv) If P = 0, T_S is an invariant distribution density with T_S(1) = 0, so T_S = 0 as in Lemma A. ∎

## Where this stops (the precise gaps)
Two further statements would be needed to obtain h_ω = 0 by this route, and I could prove neither.
(E1) GH excludes real eigen-distributions: if L_X T = κT with κ real and nonzero, then T = 0.
Diophantine linear flows satisfy E1, by Fourier series.
What I checked: the tame estimate only gives T(Rφ) = T(φ)/κ on mean-zero φ, where R = X^{-1}.
Iterating this produces no contradiction, because R^j loses derivatives as j grows and time rescaling
X → cX (which preserves GH) changes κ arbitrarily.
Flow-direction growth gives |T(φ∘g_{−t})| = e^{−κt}|T(φ)|, which is also consistent.
(E2) Positive exponents force some conformal measure S (on SM, or on a Grassmann/k-vector bundle, by the same
construction with Jacobian cocycles) with T_S ≠ 0.
What fails: S may be symmetric under v ↦ −v, and then T_S = 0 automatically.
If both E1 and E2 held, Lemma C(iii) would contradict GH. Even then this would only show that some S has T_S ≠ 0,
not h_ω = 0 directly, so the route is at best a reduction attempt and is incomplete.
Other checks:
- Suppose C_S happens to be closed while P ≠ 0. Then (g_t)_*C_S = e^{−Pt}C_S, but g_t is isotopic to the
  identity and so acts trivially on homology. Hence the homology class of C_S is 0, i.e. C_S is exact.
  No contradiction arises.
- For (n−1)-currents paired with the invariant form i_Xω, the same construction gives an invariant positive measure,
  hence ω. No information.

=== END OF FURTHER RESULTS ===

=== RESULTS OF ROUND 6 AND ONE OF ROUND 5 (quoted verbatim from the workers' answers; each labelled with its source; 'the brief'/'the planner'/'the background' inside them refer to earlier task files and to the background above; '[R5-a]' is the block labelled R5-a below; '[R5-d] Theorem 4.1' is not quoted — the facts used from it are: an ergodic mu with h_mu(g_1) > 0 is not carried by Zero(X), its flow-direction exponent is 0, and by Ruelle's inequality for g_1 and g_{-1} it has a positive and a negative exponent; '(O4)' is in the background: GH is preserved under time changes, X -> -X and conjugation) ===

[R6-a: round6_q1, complete answer. Theorem J, Lemma K, no homoclinic points, (PE) for hyperbolic measures, dim <= 3, the band Prop 6.1, Lemma 6.0, Prop 6.2 sketch, and where it stops]
# round6_q1: answer (final; partial result — (PE) proved for hyperbolic measures and for dim M <= 3, open case (PE0) isolated)

## Plan / statement being attempted
Target: (PE) under GH. New tool found: **Theorem J** ("no two-sided exponentially decaying transported distribution"), proved by a Jordan-chain argument at the eigenvalue 0 (L1 + GH applied to Xw = const) together with Fourier uniqueness. It replaces the missing step "T_0 is not a multiple of nu" in the planner's sketch. Consequences pursued:
(a) a periodic-orbit version (Lemma K) using Cayley-Hamilton on jets (no normal forms needed), giving: GH => no hyperbolic periodic orbit has a homoclinic orbit;
(b) hence (PE) for every hyperbolic ergodic measure (via the Katok / Lian-Young horseshoe theorem), and h_top = 0 when dim M <= 3;
(c) a pair version for non-hyperbolic measures with 0 < |mu(d)| < (smallest exponent on the relevant side).

Conventions: as in the brief. nu smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (log nu-Jacobian of g_t), P phi = X phi + d phi, so that d/dt [e^{J_t} (phi o g_t)] = e^{J_t} (P phi) o g_t. A *distribution density* is a continuous linear functional S on C^inf(M); S/nu is the generalized function u with <u, phi nu> = S(phi), and <Xu, phi nu> = -S(P phi) (Observation 0).

## 1. Two elementary facts used repeatedly (GH assumed)

**(F1)** If T is a distribution density with T(P phi) = 0 for all smooth phi, then T = c nu for a constant c.
*Proof.* u = T/nu satisfies <Xu, phi nu> = -T(P phi) = 0, so Xu = 0 and u is constant by L1. ∎

**(F2)** If T is a distribution density and c' a constant with T(P phi) = c' int phi dnu for all phi, then c' = 0 (and then T = c nu by F1).
*Proof.* u = T/nu satisfies <Xu, phi nu> = -c' int phi dnu, i.e. Xu = -c' (a constant, smooth function). By GH u is smooth and Xu = -c' holds pointwise. At a point q where u attains its maximum, s -> u(g_s q) has a maximum at s = 0, so (Xu)(q) = 0. Hence c' = 0. ∎

## 2. Theorem J (no two-sided exponentially decaying transported distribution)

**Theorem J.** Assume GH. Let S be a distribution density on M. For smooth phi put
 F_phi(t) := S( e^{J_t} (phi o g_t) ),  t in R.
(Equivalently F_phi(t) = <u_0 o g_{-t}, phi nu> with u_0 = S/nu: it is the pairing of the transported generalized function with phi nu.) Suppose there are eps > 0, k and C with
 |F_phi(t)| <= C e^{-eps |t|} ||phi||_{C^k}  for all t in R and all smooth phi.  (*)
Then S = 0.

*Proof.*
1. *Regularity in t.* The map t -> e^{J_t}(phi o g_t) is C^1 (indeed C^inf) from R into C^inf(M): the function (t,x) -> e^{J_t(x)} phi(g_t x) is jointly C^inf, so difference quotients in t converge in every C^m on compact t-sets (Taylor's formula with integral remainder). Its derivative is e^{J_t}(P phi) o g_t. Since S is continuous and linear, F_phi is C^1 and
 F_phi'(t) = F_{P phi}(t).
2. *Moments.* For j = 0,1,2,... define m_j(phi) := int_R t^j F_phi(t) dt. By (*), |m_j(phi)| <= C ||phi||_{C^k} int |t|^j e^{-eps|t|} dt, so each m_j is a distribution density (of order <= k).
3. *Jordan relations.* By (*) applied to P phi, F_{P phi} = F_phi' is also O(e^{-eps|t|}), and t^j F_phi(t) -> 0 as |t| -> inf. Integrating by parts on [-R, R] and letting R -> inf:
 m_0(P phi) = int F_phi' dt = 0,  and for j >= 1:  m_j(P phi) = int t^j F_phi'(t) dt = -j m_{j-1}(phi).
4. *Induction: m_j = 0 for every j.* By (F1), m_0 = c_0 nu. Then m_1(P phi) = -m_0(phi) = -c_0 int phi dnu, so c_0 = 0 by (F2); thus m_0 = 0. Suppose m_{j-1} = 0. Then m_j(P phi) = 0, so m_j = c_j nu by (F1), and m_{j+1}(P phi) = -(j+1) c_j int phi dnu, so c_j = 0 by (F2). Hence m_j = 0 for all j.
5. *Fourier uniqueness.* Fix phi. F_phi is continuous and |F_phi(t)| <= C' e^{-eps|t|}, so G(xi) := int e^{-i xi t} F_phi(t) dt extends holomorphically to the strip |Im xi| < eps, and G^{(j)}(0) = (-i)^j m_j(phi) = 0 for all j. So G = 0 on the strip, in particular on R. By uniqueness of the Fourier transform on L^1 and continuity, F_phi = 0 identically. In particular S(phi) = F_phi(0) = 0. As phi is arbitrary, S = 0. ∎

*Remarks.* (i) Only L1 and GH for constant right-hand sides are used (via F1, F2). (ii) The proof shows more: if F_phi is merely rapidly decreasing (with continuous dependence on phi), then all moments int t^j F_phi dt vanish. Exponential decay is used only in step 5 (quasi-analyticity of the Fourier transform). (iii) Sanity check: Lemma C of the background is the special case S = delta_x when int e^{J_t(x)} dt < inf with exponential decay at both ends; the north-south flow on S^2 (not GH) gives such an S = delta_y for y on a source-to-sink orbit.
(iv) This is exactly what closes the gap in the planner's sketch (b): the pair distribution T_z is the Laplace transform z -> int e^{-zt} F_phi(t) dt of a pair S = delta_x - e^b delta_y; when 0 lies in the open strip of convergence, (*) holds and S = 0, impossible for x != y. One does not need to show "T_0 is not a multiple of nu": the Jordan chain at z = 0 kills all Taylor coefficients.

## 3. Lemma K (orbits backward-asymptotic to a periodic point) — proved, elementary

**Lemma K.** Assume GH. Let p in M and P > 0 with g_P(p) = p (p may be a zero of X or a periodic point; no hyperbolicity assumed). Put I := J_P(p). There is no point y != p such that
 (a) d(g_{-mP} y, p) <= C kappa^m for all integers m >= 0, for some C and some kappa in (0,1); and
 (b) J_t(y) <= C - eps t for all t >= 0, for some eps > 0.

*Proof.* Suppose y is such a point.
1. *A weighted Koopman operator.* For Psi in C^inf(M) put (L Psi)(v) := e^{J_{-P}(v)} Psi(g_{-P} v). By the cocycle identity J_{-(m+1)P}(v) = J_{-P}(v) + J_{-mP}(g_{-P}v), induction gives (L^m Psi)(v) = e^{J_{-mP}(v)} Psi(g_{-mP} v). L is continuous on each C^K(M).
2. *Jets and Cayley-Hamilton.* Fix K >= 1 (chosen in step 6). Let I_K be the space of smooth functions all of whose derivatives of order < K vanish at p. Since g_{-P}(p) = p, L(I_K) ⊂ I_K. So L induces a linear map L_K on the finite-dimensional space C^inf(M)/I_K (the (K-1)-jets at p), of dimension N = binom(n+K-1, n). Let Q(zeta) = sum_{j=0}^N q_j zeta^j be the characteristic polynomial of L_K (monic: q_N = 1). By Cayley-Hamilton Q(L_K) = 0, i.e. Q(L) Psi in I_K for every smooth Psi. Since Q(L) is a finite combination of the L^j, ||Q(L)Psi||_{C^K} <= C_1 ||Psi||_{C^K}. Taylor's formula in a coordinate ball B around p gives |G(v)| <= C_2 ||G||_{C^K} d(v,p)^K for G in I_K and v in B.
3. *The distribution.* Let y_j := g_{-jP} y (j = 0..N) and w_j := q_j e^{J_{-jP}(y)}, and S := sum_j w_j delta_{y_j}. The y_j are pairwise distinct: if g_{-aP}y = g_{-bP}y with a < b, then y is fixed by g_{-(b-a)P}, so g_{-l(b-a)P} y = y for all l, and (a) forces y = p, excluded. Since w_N = e^{J_{-NP}(y)} != 0, S != 0.
4. *Backward decay.* Let t <= 0 and write t = -mP - r with m >= 0 an integer and r in [0, P). Put Phi_r(v) := e^{J_{-r}(v)} phi(g_{-r} v); then ||Phi_r||_{C^K} <= C_3 ||phi||_{C^K} uniformly in r in [0,P]. Using J_t(g_{-jP}y) = J_{t-jP}(y) - J_{-jP}(y) and J_{-(m+j)P - r}(y) = J_{-(m+j)P}(y) + J_{-r}(g_{-(m+j)P} y):
 w_j e^{J_t(y_j)} phi(g_t y_j) = q_j e^{J_{-(m+j)P}(y)} Phi_r(g_{-(m+j)P} y) = q_j (L^{m+j} Phi_r)(y).
Summing over j: F_phi(t) = S(e^{J_t} phi o g_t) = (L^m G_r)(y) = e^{J_{-mP}(y)} G_r(g_{-mP} y), where G_r := Q(L) Phi_r lies in I_K.
5. *Estimating the two factors.* By (a), for m >= m_0 the point g_{-mP}y lies in B and |G_r(g_{-mP}y)| <= C_2 C_1 C_3 ||phi||_{C^K} C^K kappa^{mK}. Also J_{-mP}(y) = -sum_{i=1}^m J_P(g_{-iP} y), and |J_P(g_{-iP}y) - I| <= Lip(J_P) C kappa^i, so J_{-mP}(y) <= -mI + C_4. Hence for t <= -m_0 P:
 |F_phi(t)| <= C_5 ||phi||_{C^K} exp( m (-I - K log(1/kappa)) ).
6. *Choice of K.* Choose K with K log(1/kappa) > max(0, -I) + 1. Then |F_phi(t)| <= C_6 e^{-|t|/P} ||phi||_{C^K} for t <= 0 (the finitely many m < m_0 are absorbed into C_6).
7. *Forward decay.* For t >= 0: J_t(y_j) = J_{t - jP}(y) - J_{-jP}(y). For t >= jP, (b) gives J_{t-jP}(y) <= C - eps(t - jP); for 0 <= t < jP it is bounded by ||d||_inf N P. So |F_phi(t)| <= sum_j |w_j| e^{J_t(y_j)} ||phi||_inf <= C_7 e^{-eps t} ||phi||_inf.
8. By 6 and 7, S satisfies (*) of Theorem J (with k = K and rate min(eps, 1/P)). So S = 0, contradicting step 3. ∎

**Lemma K' (time-reversed form).** Assume GH. There is no p with g_P p = p (P > 0) and y != p such that d(g_{mP} y, p) <= C kappa^m (m >= 0) and J_t(y) <= C - eps|t| for all t <= 0.
*Proof.* Apply Lemma K to -X, which is GH by (O4). Its flow is g_{-t}, its nu-divergence is -d, and its log-Jacobian at time t is J_{-t}. Condition (b) for -X reads J_{-t}(y) <= C - eps t for t >= 0. ∎

*Remark.* Lemma K needs no normal forms: Cayley-Hamilton on the finite-dimensional jet space at the fixed point p of g_{-P} annihilates, in one stroke, all the "slowly decaying modes" e^{-mI} mu^alpha (products of eigenvalues of Dg_{-P}(p)) of the backward sequence. This is where periodicity of p is essential (Section 7).

## 4. Consequences for connecting orbits (proved; uses only the classical stable manifold theorem for hyperbolic periodic orbits / zeros)

Cited [SM] (stable manifold theorem, classical). Let gamma be a hyperbolic periodic orbit of period P (resp. a hyperbolic zero p; then read gamma = {p}, P = 1). Then W^s(gamma) := {y : dist(g_t y, gamma) -> 0 as t -> +inf} is the union over q in gamma of W^{ss}(q), and there is c > 0 such that for y in W^{ss}(q), d(g_t y, g_t q) <= C_y e^{-ct} for t >= 0 ("asymptotic phase"). Likewise W^u(gamma) = union of W^{uu}(q), with d(g_{-t} y, g_{-t} q) <= C_y e^{-ct} for t >= 0.

Notation: for gamma as above put I(gamma) := J_P(q) = int_0^P d(g_s q) ds (independent of q in gamma; for a zero, I = d(p)). Note J_{mP}(q) = m I(gamma) for q in gamma, hence J_t(q) = (t/P) I(gamma) + O(1) for all real t, uniformly.

**Corollary 4.1 (connections).** Assume GH. Let gamma_1, gamma_2 be hyperbolic periodic orbits or hyperbolic zeros (possibly gamma_1 = gamma_2), and let y in W^u(gamma_1) ∩ W^s(gamma_2), y not in gamma_1 ∪ gamma_2. Then I(gamma_2) >= 0 and I(gamma_1) <= 0 (that is, I(gamma_2) < 0 is impossible, and I(gamma_1) > 0 is impossible).
*Proof.* Choose q_1 in gamma_1 and q_2 in gamma_2 with y in W^{uu}(q_1) ∩ W^{ss}(q_2) ([SM]). Since d is Lipschitz, |J_t(y) - J_t(q_2)| <= Lip(d) C_y / c for t >= 0 and |J_t(y) - J_t(q_1)| <= Lip(d) C_y / c for t <= 0. Let P_1 be the period of gamma_1.
- If I(gamma_2) < 0: J_t(y) <= C + (t/P_2) I(gamma_2) for t >= 0, which is (b) of Lemma K with eps = |I(gamma_2)|/P_2; and d(g_{-mP_1} y, q_1) = d(g_{-mP_1} y, g_{-mP_1} q_1) <= C_y e^{-c m P_1}, which is (a) with p = q_1, P = P_1, kappa = e^{-cP_1}; and y != q_1. Lemma K gives a contradiction.
- If I(gamma_1) > 0: for t <= 0, J_t(y) <= C + (t/P_1) I(gamma_1) = C - (I(gamma_1)/P_1)|t|; and d(g_{mP_2} y, q_2) <= C_y e^{-c m P_2}. Lemma K' (with p = q_2) gives a contradiction. ∎

So under GH every connection between hyperbolic periodic orbits/zeros goes from a volume-contracting one (I < 0) to a volume-expanding one (I > 0). (This strengthens Prop. 4.0 of [R5-d], which excluded only I(gamma_1) > 0 > I(gamma_2).)

**Corollary 4.2 (no homoclinic orbits).** Assume GH and dim M >= 2. No hyperbolic periodic orbit and no hyperbolic zero has a homoclinic point (a point of W^u(gamma) ∩ W^s(gamma) outside gamma), transverse or not.
*Proof.* With gamma_1 = gamma_2 = gamma, Corollary 4.1 gives I(gamma) >= 0 and I(gamma) <= 0, so I(gamma) = 0; and I(gamma) = 0 is excluded by Observation P (periodic orbits, dim >= 2) or by P1 (zeros: d(p) != 0). ∎

## 5. (PE) for hyperbolic measures; zero topological entropy in dimension <= 3 (proved modulo cited classical theorems)

Cited (from memory, standard):
- [Ru] Ruelle's inequality: for a C^1 diffeomorphism f of a compact manifold and an f-invariant ergodic mu, h_mu(f) <= sum of the positive Lyapunov exponents of mu (with multiplicity).
- [KLY] Katok's horseshoe theorem, flow version (Katok, Publ. IHES 51 (1980), including flows on 3-manifolds; Lian-Young for C^2 flows in any finite dimension): if mu is an ergodic invariant probability of a C^2 flow with h_mu(g_1) > 0, mu(Zero(X)) = 0, and all Lyapunov exponents of mu other than the (zero) exponent in the flow direction are nonzero, then the flow has a horseshoe: a compact invariant hyperbolic set Lambda on which the flow is conjugate to a suspension of a transitive subshift of finite type of positive entropy. In particular Lambda contains a hyperbolic periodic orbit gamma and a point x not in gamma whose alpha- and omega-limit sets are gamma (in the symbolic model: a sequence that agrees with the periodic sequence of gamma in the far past and far future but not everywhere; it exists because the SFT is transitive and not a single periodic orbit). By [SM], x is a homoclinic point of gamma.
- Variational principle and the reduction to ergodic flow-invariant measures (step 2 of the chain; I checked it and see no flaw: mu-bar = int_0^1 (g_s)_* mu ds is flow-invariant because (g_1)_* mu = mu; h_{(g_s)_* mu}(g_1) = h_mu(g_1) because g_s conjugates g_1 to itself; entropy is affine and satisfies the integral formula over decompositions into g_1-invariant measures (Jacobs), applied to the flow-ergodic decomposition of mu-bar).

**Theorem 5.1.** Assume GH and dim M >= 2. Let mu be an ergodic flow-invariant probability with h_mu(g_1) > 0. Then mu is not hyperbolic: besides the flow direction, mu has a zero Lyapunov exponent.
*Proof.* As in Theorem 4.1 of [R5-d]: mu(Zero(X)) = 0 (otherwise mu is carried by the closed invariant set Zero(X) on which g_1 = id, so h_mu = 0); the exponent in the flow direction is 0 for mu-a.e. x; by [Ru] for g_1 and for g_{-1}, mu has a positive and a negative exponent. If all other exponents were nonzero, [KLY] would give a hyperbolic periodic orbit with a homoclinic point, contradicting Corollary 4.2. ∎

**Theorem 5.2 (the problem, for dim M <= 3).** Assume GH and dim M <= 3. Then h_top(g_1) = 0.
*Proof.* By step 2 of the chain it suffices that h_mu(g_1) = 0 for every ergodic flow-invariant mu. Suppose h_mu(g_1) > 0. As above, mu(Zero(X)) = 0, the flow direction carries the exponent 0, and [Ru] (for g_1 and g_{-1}) gives a positive and a negative exponent. If dim M <= 2 there is at most one further exponent, which cannot be both positive and negative: contradiction. If dim M = 3 the exponents are chi^+ > 0 = 0 > chi^-, so mu is hyperbolic, contradicting Theorem 5.1 (dim M = 3 >= 2). ∎

Remark. In dimension 3 this does not use Theorem 4.1(ii) of [R5-d] (uniform sign of volume contraction on the horseshoe): a single hyperbolic periodic orbit with a single homoclinic point is already excluded by Lemma K / K', whatever the sign of I(gamma).

## 6. Non-hyperbolic measures: the pair version (proved modulo cited Pesin / Ledrappier-Young facts)

Cited:
- [P] Pesin theory for f = g_1 (C^inf diffeo) and an ergodic mu: for mu-a.e. x there is a local unstable manifold W^u_loc(x) (an embedded C^1 disc tangent to the sum of the Oseledets spaces of positive exponents) such that for every delta > 0 and y in W^u_loc(x): d(f^{-m}x, f^{-m}y) <= C(x,delta) e^{-(chi^+_min - delta) m} for m >= 0, where chi^+_min is the smallest positive exponent of mu.
- [LY] (Ledrappier-Strelcyn, Ledrappier-Young) There is a measurable partition xi subordinate to W^u (xi(x) ⊂ W^u_loc(x), xi(x) contains a neighbourhood of x in W^u(x)) with h_mu(f) = H_mu(xi | f xi). If the conditional measures mu^xi_x were Dirac masses delta_x for a.e. x, xi would be the point partition mod mu and h_mu(f) = 0. Hence h_mu(f) > 0 implies mu^xi_x(xi(x) \ {x}) > 0 for a.e. x.

Let lambda := mu(d); by Birkhoff J_t(x)/t -> lambda as t -> +inf and as t -> -inf for mu-a.e. x. (lambda is the sum of all Lyapunov exponents of mu; it does not depend on nu.) Let chi^-_max denote the negative exponent of mu closest to 0.

**Proposition 6.1.** Assume GH. Let mu be ergodic with h_mu(g_1) > 0. Then lambda = mu(d) satisfies neither -chi^+_min < lambda < 0 nor 0 < lambda < |chi^-_max|.
*Proof.* Case -chi^+_min < lambda < 0. Fix delta > 0 with lambda + 3 delta < 0 and chi^+_min - 2delta > |lambda| + 2delta. Let G be the set of points z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf; mu(G) = 1. By [P] and [LY], for mu-a.e. x (so we may take x in G) the conditional mu^xi_x gives positive mass to xi(x) \ {x} and full mass to G, so there is y in G ∩ W^u_loc(x), y != x. Put theta := chi^+_min - delta. Interpolating between integer times as in [R5-a] Lemma 2: d(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0. Then b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists and |J_t(x) - J_t(y) - b| <= C e^{-theta|t|} for t <= 0 ([R5-a] Step 4(a)). Let S := delta_x - e^b delta_y (nonzero, as x != y), so F_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y).
- t >= 0: since x, y in G, J_t(x), J_t(y) <= C + (lambda + delta) t, so |F_phi(t)| <= C e^{(lambda+delta)t} ||phi||_inf.
- t <= 0: as in [R5-a] Step 4(c), |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|} ||phi||_{C^1}, and J_t(x) <= C + (|lambda| + delta)|t| for t <= 0 (x in G, lambda < 0). So |F_phi(t)| <= C e^{-(theta - |lambda| - delta)|t|} ||phi||_{C^1}, and theta - |lambda| - delta > 0 by the choice of delta.
So (*) of Theorem J holds and S = 0: contradiction.
Case 0 < lambda < |chi^-_max|: apply the first case to -X (GH by (O4)); mu is ergodic for the reversed flow with the same entropy, its exponents are the negatives of those of mu, so its smallest positive exponent is |chi^-_max|, and its lambda is -lambda. ∎

So for a GH flow, an ergodic measure of positive entropy must be non-hyperbolic (Theorem 5.1) and must have lambda = 0, or lambda <= -chi^+_min, or lambda >= |chi^-_max| (Proposition 6.1).

**Lemma 6.0 (non-atomic unstable conditionals; proved from the Ledrappier-Strelcyn formula).** In the setting of [LY] with h_mu(f) > 0, the conditional measures mu^xi_x are non-atomic for mu-a.e. x.
*Proof.* xi is increasing: (f xi)(fx) = f(xi(x)) ⊃ xi(fx), so xi refines f xi. Put w(x) := mu^xi_x({x}). By invariance mu^{f xi}_{fx} = f_* mu^xi_x, so mu^{f xi}_{fx}({fx}) = w(x); and mu^xi_{fx} is mu^{f xi}_{fx} restricted to xi(fx) and normalised. Hence w(fx) = w(x) / mu^{f xi}_{fx}(xi(fx)) >= w(x). Since w is bounded and mu is invariant, int (w o f - w) dmu = 0 with a nonnegative integrand, so w o f = w a.e., and w = w_0 a.e. by ergodicity. If w_0 > 0, equality forces mu^{f xi}_{fx}(xi(fx)) = 1 a.e., i.e. xi = f xi mod mu, so h_mu(f) = H_mu(xi | f xi) = 0, a contradiction. So w = 0 a.e. Finally the mu-measure of the set of points z which are atoms of their own conditional is int w dmu = 0, while it also equals int mu^xi_x(atoms of mu^xi_x) dmu(x); so a.e. conditional has no atoms. ∎

**Proposition 6.2 (one-dimensional unstable direction; proof sketched, modulo standard Pesin-theory estimates).** Assume GH. Let mu be ergodic with h_mu(g_1) > 0 and lambda = mu(d) < 0, and suppose mu has exactly one positive exponent chi, of multiplicity one. This is impossible. Symmetrically (apply to -X), lambda > 0 is impossible when mu has exactly one negative exponent, simple.
*Sketch.*
1. *Affine parameters (standard for 1-dimensional unstable leaves).* For a.e. x the global unstable leaf W^u(x) is a C^inf curve, and there is a C^inf parameter H_x : W^u(x) -> R, H_x(x) = 0, with H_{g_{-m}x}(g_{-m} y) = A_m(x) H_x(y) for m >= 0, where |A_m(x)| <= C(x) e^{-(chi - delta)m}. (Construction: with a(z) := log |Dg_{-1}(z) e(z)|, e(z) the unit tangent to the leaf, take H_x(y) = int_x^y exp( sum_{m >= 0} [a(g_{-m} z) - a(g_{-m} x)] ) dz along the leaf; the series converges in C^K along the leaf by the 1-dimensional distortion estimates, and the change of variables w = g_{-1} z shows the linearisation identity, as checked in the derivation: H_{g_{-1}x}(g_{-1}y) = e^{a(x)} H_x(y).) The charts H_{g_{-m}x}^{-1} have C^K norms on intervals of radius rho(g_{-m}x) bounded by C(x) e^{delta m}, with rho(g_{-m}x) >= rho(x) e^{-delta m} (tempered Pesin bounds).
2. *Removing the Jacobian weight.* For w in W^u(z) put beta_z(w) := -int_{-inf}^0 (d(g_s w) - d(g_s z)) ds. Then J_{-m}(y) - J_{-m}(x) = beta_x(y) - beta_{g_{-m}x}(g_{-m}y) (direct computation from the definition), and beta_{g_{-m}x} has tempered C^K norms along the leaf.
3. *The distribution.* By Lemma 6.0 there are K+1 distinct points y_0..y_K in xi(x) whose forward Birkhoff averages of d converge to lambda. Let s_j = H_x(y_j) (distinct), choose a nonzero vector (a_j) with sum_j a_j s_j^i = 0 for i = 0..K-1 (K equations, K+1 unknowns), put w_j := a_j e^{-beta_x(y_j)}, S := sum_j w_j delta_{y_j} != 0.
4. *Backward estimate.* For t = -m - r (m >= 0 integer, r in [0,1)), exactly as in Lemma K step 4 and by step 2:
 S(e^{J_t} phi o g_t) = e^{J_{-m}(x)} sum_j a_j theta_{m,r}(A_m(x) s_j),
 where theta_{m,r}(sigma) := e^{-beta_{g_{-m}x}(w)} Phi_r(w) at w = H^{-1}_{g_{-m}x}(sigma), Phi_r(w) = e^{J_{-r}(w)} phi(g_{-r} w). By the vanishing moments, Taylor's formula of order K at sigma = 0 gives |sum_j a_j theta_{m,r}(A_m s_j)| <= C |A_m|^K ||theta_{m,r}||_{C^K} <= C(x) e^{-(K(chi - delta) - delta) m} ||phi||_{C^K}. Also e^{J_{-m}(x)} <= C e^{(|lambda| + delta) m}. Choosing K with K chi > |lambda| + 1 and delta small, S(e^{J_t} phi o g_t) decays exponentially as t -> -inf, with a C^K bound.
5. *Forward estimate.* Each y_j has J_t(y_j) <= C + (lambda + delta) t for t >= 0, so |S(e^{J_t} phi o g_t)| <= C e^{(lambda+delta)t} ||phi||_inf.
6. Theorem J gives S = 0, a contradiction. ∎
The only non-elementary inputs are the tempered C^K bounds in steps 1-2 (standard Pesin theory for C^inf flows, 1-dimensional leaves). For higher-dimensional unstable manifolds the same argument goes through verbatim if one has C^K-tempered non-stationary normal form coordinates along W^u in which g_{-1} is a polynomial map of uniformly bounded degree r (non-uniform sub-resonance normal forms, Guysinsky-Katok / Kalinin-Sadovskaya type; cited from memory, hypotheses not checked): one then imposes vanishing moments against all polynomials of degree < rK. **If that citation is granted, every ergodic mu with h_mu > 0 under GH has mu(d) = 0.** I mark this extension as conditional.

**Corollary 6.3 (dimension 4, modulo the same Pesin estimates).** If dim M = 4 and GH holds, every ergodic mu with h_mu(g_1) > 0 has exponents chi^+ > 0 = 0 = 0 > chi^- = -chi^+ (all simple), i.e. it is non-hyperbolic with lambda = mu(d) = 0; consequently (Corollary D1 of the background) supp mu = M.
*Proof.* Theorem 5.1 gives a second zero exponent; the remaining two are chi^+ > 0 > chi^- by [Ru], each simple; Proposition 6.2 and its symmetric form exclude lambda < 0 and lambda > 0. ∎

## 7. What remains open, and where the argument stops

**Unconditionally open case of (PE).** Under GH, exclude an ergodic mu with h_mu(g_1) > 0 such that
 (i) mu has a zero Lyapunov exponent transverse to X (non-hyperbolic; forced by Theorem 5.1), and
 (ii) either lambda = mu(d) = 0, or lambda <= -chi^+_min with no 1-dimensional simple unstable direction (resp. lambda >= |chi^-_max| with no 1-dimensional simple stable direction), the latter only modulo the cited normal forms of Prop. 6.2.
With the normal-form citation granted, the single remaining case is:
**(PE0)** GH excludes an ergodic, non-hyperbolic mu with h_mu > 0 and mu(d) = 0. (Such a mu has supp mu = M by Corollary D1; the volume-preserving case, where every invariant measure has mu(d) = 0, is inside (PE0); this is the old core #16.) **(PE0) is open; I could not prove it.** So the problem's claim is proved here only for dim M <= 3 (Theorem 5.2), and in every dimension for hyperbolic measures (Theorem 5.1); in dim 4 it is reduced (modulo standard Pesin estimates) to (PE0).

**Why the method stops at lambda = 0.** Theorem J needs a nonzero S with |S(e^{J_t} phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k} in BOTH time directions.
- If lambda != 0, one direction is free (e.g. lambda < 0: forward decay of e^{J_t} at generic points), and the other is obtained by cancellation inside one unstable leaf (pairs, or vanishing moments in an affine/normal-form parameter, or Cayley-Hamilton on jets at a periodic point).
- If lambda = 0, e^{J_t} = e^{o(|t|)} in both directions at generic points, so S needs cancellation forward (clusters of forward-asymptotic points, inside stable leaves) and backward (clusters inside unstable leaves) at the same time. For a combination of point masses this requires closed su-cycles of points x_{11} ~s x_{12} ~u x_{22} ~s x_{21} ~u x_{11} with consistent weights; the weights are consistent only if the Jacobian holonomy around the cycle vanishes: b^s_1 + b^u_2 = b^u_1 + b^s_2, where b^s, b^u are the limits of J_t(.) - J_t(.) along the stable/unstable sides. Generic su-paths do not even close up (temporal distance), and when they close the cycle condition is an extra codimension-one condition. Spreading S along unstable discs gives forward decay only at the speed of equidistribution of unstable discs, which is not exponential in general (no mixing rates are available for general positive-entropy measures).
- Remark (ii) after Theorem J shows that rapid (super-polynomial) two-sided decay already forces all moments int t^j F_phi dt to vanish; but for sub-exponential decay this does not force F_phi = 0 (no quasi-analyticity), so even a weaker decay statement would not suffice without a further idea.
- The planner's observation applies: under the strong hypothesis H (smooth invariant volume, unique ergodicity, all mean-zero smooth functions are smooth coboundaries) the pair transform T_z, 0 < Re z < theta, has the formal Taylor expansion 0 at z = 0 (all Jordan coefficients vanish, consistently with Theorem J's step 4), but T_z is not known to extend holomorphically across Re z = 0, so no contradiction follows.

**Status of the chain.** Step 2 is correct (checked in Section 5). Step 1 (PE) is proved for: all hyperbolic ergodic measures (any dimension; cited [KLY]); all ergodic measures when dim M <= 3; all ergodic measures with -chi^+_min < mu(d) < 0 or 0 < mu(d) < |chi^-_max| (Prop. 6.1, cited [P], [LY]); all ergodic measures with mu(d) < 0 and a single simple positive exponent, or mu(d) > 0 and a single simple negative exponent (Prop. 6.2, sketched modulo standard Pesin estimates). It remains open in the case (PE0) (and, without the normal-form citation, in the non-1-dimensional large-|lambda| case).

## Summary of what is proved (new in this round)
1. **Theorem J (fully proved, GH + L1 only):** no nonzero distribution density S has S(e^{J_t} phi o g_t) = O(e^{-eps|t|}) ||phi||_{C^k} for t -> +inf and t -> -inf. Proof: the moments m_j(phi) = int t^j F_phi(t) dt form a Jordan chain m_j(P phi) = -j m_{j-1}(phi); L1 and "Xw = const => const = 0" kill it; Fourier uniqueness finishes.
2. **Lemma K / K' (fully proved):** no point y != p, p a periodic point or a zero, with g_{-mP} y -> p exponentially and forward exponential volume contraction along y (resp. the time-reversed version). Proof: Cayley-Hamilton on the jet space at p for the weighted Koopman operator L Psi = e^{J_{-P}} Psi o g_{-P} produces a finite combination of Dirac masses on the backward orbit of y satisfying Theorem J.
3. **Corollary 4.1/4.2 (proved, modulo the classical stable manifold theorem):** under GH, every connection between hyperbolic periodic orbits/zeros goes from I < 0 to I > 0; in particular no hyperbolic periodic orbit or hyperbolic zero has a homoclinic point.
4. **Theorem 5.1 / 5.2 (proved modulo Ruelle's inequality and the Katok / Lian-Young horseshoe theorem):** under GH every positive-entropy ergodic measure is non-hyperbolic; **h_top(g_1) = 0 whenever dim M <= 3.**
5. **Prop. 6.1 (proved modulo Pesin theory and Ledrappier-Strelcyn), Lemma 6.0 (proved), Prop. 6.2 and Cor. 6.3 (sketched):** restrictions on mu(d) for non-hyperbolic positive-entropy measures; in dimension 4 only mu(d) = 0 survives.
**Open:** (PE0), hence the problem in dimension >= 4.


[R5-a: no GH needed. A positive top exponent gives a real eigen-distribution of X (claim (N)); the pair construction of Step 4 is the template for the 'generic pairs' idea below]
## Conventions

As in Text B and Lemmas C–F:
- nu is a smooth positive density, and d = div_nu X, so L_X(phi nu) = (X phi + d phi) nu.
- J_t(z) = int_0^t d(g_s z) ds for all real t. So d/dt J_t(z) = d(g_t z).
- A distribution density T (a continuous linear functional on C^inf(M)) gives the generalized function u = T/nu, defined by <u, phi nu> = T(phi).
- Then <Xu, phi nu> = -<u, L_X(phi nu)> = -T(X phi + d phi).
- Hence: **if T(X phi + d phi) = c T(phi) for all smooth phi, then Xu = -c u.** (*)

Fix a Riemannian distance on M. Every smooth phi is Lipschitz with constant ||dphi||_inf. The function d is Lipschitz with some constant Lip(d).

## Step 1. lambda* > 0 gives an invariant measure with a positive exponent

**Lemma 1.** Put a_n(x) = log||Dg_n(x)|| and assume lambda* = lim_n (1/n) max_x a_n(x) > 0. Then there is a flow-invariant Borel probability m such that chi(x) := lim_n (1/n) a_n(x) exists m-a.e. and int chi dm >= lambda*. In particular chi > 0 on a set of positive m-measure.

*Proof.*
1. a_n is continuous and subadditive: a_{n+k}(x) <= a_n(x) + a_k(g_n x).
2. Let x_n be a maximiser of a_n. Put mu_n = (1/n) sum_{k<n} delta_{g_k x_n}. Then (g_1)_* mu_n - mu_n = (delta_{g_n x_n} - delta_{x_n})/n -> 0. So every weak* limit mu is g_1-invariant. Fix such a limit along a subsequence.
3. Fix N. Let K = N max(0, max_x log||Dg_1(x)||), so that a_j <= K for 0 <= j <= N, since a_j <= j max log||Dg_1||.
4. For each 0 <= j < N, split [0, n) into [0, j), then blocks of length N, then a remainder of length < N. Subadditivity gives a_n(x) <= sum over blocks of a_N(g_{j+iN} x) + 2K.
5. The blocks for j = 0..N-1 together use each index k < n at most once, and the indices omitted lie within N of n. Summing over j:
   N a_n(x) <= sum_{k<n} a_N(g_k x) + 2NK + N^2 max|a_N|.
6. Take x = x_n and divide by Nn: max a_n / n <= (1/N) int a_N dmu_n + O_N(1/n).
7. Let n -> inf along the subsequence. Since a_N is continuous: lambda* <= (1/N) int a_N dmu. This holds for every N, with the same mu.
8. Put m = int_0^1 (g_s)_* mu ds. It is flow-invariant, because mu is g_1-invariant.
9. From Dg_N(g_s x) = Dg_s(g_N x) Dg_N(x) Dg_{-s}(g_s x) we get |a_N(g_s x) - a_N(x)| <= 2L, where L = max_{|r|<=1, z} log^+ max(||Dg_r(z)||, ||Dg_r(z)^{-1}||). Hence (1/N) int a_N dm >= lambda* - 2L/N.
10. By Kingman's subadditive ergodic theorem for g_1 and m: chi exists m-a.e., and int chi dm = lim_N (1/N) int a_N dm >= lambda*. ∎

## Step 2. A pair exponentially asymptotic in backward time (cited theorem)

**(R) Pesin–Ruelle stable manifold theorem, weak form (cited from memory).** Ruelle, "Ergodic theory of differentiable dynamical systems", Publ. IHES 50 (1979), Thm. 6.1. Also Pesin 1977, and Fathi–Herman–Yoccoz 1983.

Let f be a C^r diffeomorphism (r > 1) of a compact manifold, and m an f-invariant Borel probability. For m-a.e. x the following holds. If f has a negative Lyapunov exponent at x, then there is y != x with limsup_n (1/n) log d(f^n x, f^n y) < 0. Indeed, for lambda < 0 not an exponent at x and above the smallest exponent, the set {y : limsup (1/n) log d(f^n x, f^n y) <= lambda} contains an embedded C^1 disc through x of positive dimension. No hyperbolicity of the other exponents is required.

**Lemma 2.** If lambda* > 0, there are x != y in M and constants C0, theta > 0 with
d(g_{-t} x, g_{-t} y) <= C0 e^{-theta t} for all real t >= 0.

*Proof.*
1. Take m from Lemma 1, and apply (R) to f = g_{-1} = (g_1)^{-1}, which is C^inf. Here m is f-invariant.
2. By Oseledets, at m-a.e. x the exponents of g_{-1} are the negatives of those of g_1. On the positive-measure set where chi(x) > 0, f therefore has the negative exponent -chi(x).
3. So for some such x there is y != x and theta' > 0 with d(g_{-n} x, g_{-n} y) <= C e^{-theta' n} for all integers n >= 0.
4. For real t >= 0, write t = n + s with s in [0, 1). Then g_{-t} = g_{-s} o g_{-n}. With L' = max_{s in [0,1]} Lip(g_{-s}):
   d(g_{-t} x, g_{-t} y) <= L' C e^{theta'} e^{-theta' t}. ∎

## Step 3. Case B: uniform sublinearity of J

**Lemma 3.** Suppose every flow-invariant probability mu has mu(d) = 0. Then for every eps > 0 there is C_eps with |J_t(z)| <= eps|t| + C_eps for all z in M and all real t.

*Proof.*
1. Suppose not. Then there are eps > 0, |t_n| -> inf and z_n with |J_{t_n}(z_n)| >= eps|t_n|. Bounded |t| is trivial, since |J_t| <= ||d||_inf |t|.
2. If t_n -> +inf, put m_n = (1/t_n) int_0^{t_n} delta_{g_s z_n} ds, so that m_n(d) = J_{t_n}(z_n)/t_n.
3. If t_n -> -inf, put m_n = (1/|t_n|) int_{t_n}^0 delta_{g_s z_n} ds, so that m_n(d) = -J_{t_n}(z_n)/|t_n|.
4. In both cases ||(g_r)_* m_n - m_n|| <= 2|r|/|t_n|. So a weak* limit m is a flow-invariant probability, and since d is continuous, |m(d)| = lim |m_n(d)| >= eps. This is a contradiction. ∎

## Step 4. Case B: the eigen-distribution

**Theorem B.** Suppose lambda* > 0 and every invariant probability has mu(d) = 0. Let x != y, C0 and theta be as in Lemma 2. Then for every kappa in (0, theta), except at most a discrete subset of (0, theta), there is a nonzero distribution density T_kappa of order <= 1 with

T_kappa(X phi + d phi) = kappa T_kappa(phi) for all smooth phi.

Hence u_kappa = T_kappa/nu is a nonzero generalized function with X u_kappa = -kappa u_kappa, by (*). This is (N) with real eigenvalue -kappa != 0.

*Proof.*

(a) **Defining the constant b.** For t <= 0 we have J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds, and |d(g_s x) - d(g_s y)| <= Lip(d) C0 e^{-theta|s|}. So the limit b := lim_{t->-inf} (J_t(x) - J_t(y)) exists, and
|J_t(x) - J_t(y) - b| <= K e^{-theta|t|} for t <= 0, where K = Lip(d) C0/theta.

(b) **The orbit function.** For smooth phi define
c_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y), for t in R.
Then c_phi is C^1, and c_phi'(t) = c_{P phi}(t) with P phi := X phi + d phi. This is because d/dt[e^{J_t(z)} phi(g_t z)] = e^{J_t(z)} (X phi + d phi)(g_t z).

(c) **Bounds.** Fix kappa in (0, theta) and choose eps with 0 < eps < min(kappa, theta - kappa)/2.

For t <= 0, write e^{b + J_t(y)} = e^{J_t(x)} e^{-r_t} with |r_t| <= K e^{-theta|t|} <= K. Then
|c_phi(t)| <= e^{J_t(x)} [ ||dphi||_inf C0 e^{-theta|t|} + |1 - e^{-r_t}| ||phi||_inf ]
          <= C1 ||phi||_{C^1} C_eps e^{-(theta - eps)|t|},
where C1 = C0 + K e^K. This uses |1 - e^{-r}| <= |r| e^{|r|} and Lemma 3.

For t >= 0, Lemma 3 gives |c_phi(t)| <= (1 + e^b) C_eps e^{eps t} ||phi||_inf.

Hence e^{-kappa t} c_phi(t) is bounded by:
- C ||phi||_{C^1} e^{-(kappa - eps) t} for t >= 0;
- C ||phi||_{C^1} e^{-(theta - eps - kappa)|t|} for t <= 0.

Both are integrable, and both tend to 0 at their respective ends.

(d) **Definition and order.** Put T_kappa(phi) := int_R e^{-kappa t} c_phi(t) dt. By (c) the integral converges absolutely and |T_kappa(phi)| <= C' ||phi||_{C^1}. So T_kappa is a distribution density of order <= 1.

(e) **Eigen-relation.** Integrate by parts on [-R, R]:
int_{-R}^R e^{-kappa t} c_{P phi}(t) dt = [e^{-kappa t} c_phi(t)]_{-R}^R + kappa int_{-R}^R e^{-kappa t} c_phi(t) dt.
By (c), applied to phi and to P phi, the boundary terms tend to 0 and both integrals converge as R -> inf. Hence T_kappa(P phi) = kappa T_kappa(phi).

(f) **Nonvanishing.** Choose smooth phi0 with phi0(x) = 1 and phi0(y) = 0, which is possible since x != y. Then c_{phi0}(0) = 1.
1. Let F(z) = int_R e^{-z t} c_{phi0}(t) dt for complex z with 0 < Re z < theta. By the bounds of (c), the convergence is absolute and locally uniform, with eps chosen per compact sub-strip. So F is holomorphic on the strip, and F(kappa) = T_kappa(phi0) for real kappa.
2. Suppose the zeros of F in (0, theta) accumulated at a point of (0, theta). Then F would vanish identically on the strip.
3. Take kappa0 = theta/2. The function G(t) = e^{-kappa0 t} c_{phi0}(t) is continuous and in L^1(R). Its Fourier transform is omega -> F(kappa0 + i omega), which would be identically 0. Fourier uniqueness on L^1 gives G = 0 a.e., hence everywhere by continuity. This contradicts G(0) = 1.
4. So the set {kappa in (0, theta) : T_kappa(phi0) = 0} is discrete in (0, theta). Off this set, T_kappa != 0. ∎

## Step 5. Case A: some invariant mu has mu(d) != 0 (settled case, re-checked)

By ergodic decomposition, some ergodic mu has lambda := mu(d) != 0. The proof of [R4-q7] Prop 2.2 checks out:
1. Take x generic for mu in both time directions. Then J_t(x) = lambda t + o(|t|) as t -> +-inf.
2. So c_s(t) = e^{J_t(x) - lambda t - s|t|} is integrable for each s > 0, and tends to 0 at +-inf.
3. Integrate d/dt[c_s(t) phi(g_t x)] = c_s(t)[(X phi + d phi - lambda phi)(g_t x) - s sign(t) phi(g_t x)] over R. For the probabilities T_s = c_s(t) dt pushed along the orbit and normalised, this gives |T_s(X phi + d phi - lambda phi)| <= s ||phi||_inf.
4. A weak* limit T as s -> 0 is a probability, hence nonzero, and satisfies T(X phi + d phi) = lambda T(phi).
5. By (*), u = T/nu satisfies Xu = -lambda u, with lambda != 0.

## Conclusion

**Theorem.** Let X be any smooth vector field on a compact manifold M with lambda* > 0; GH is not needed. Then there are a real kappa != 0 and a nonzero u in D'(M) with Xu = kappa u.
- In Case B, u has order <= 1, and -kappa can be any point of an interval (0, theta) outside a discrete set.
- In Case A, u has order 0.

So (N) holds.

The 1-current form asked for in the task follows at once. C := dW (in the task's notation W = u) is a nonzero exact, hence closed, 1-current. Indeed u is nonconstant, since Xu = kappa u with kappa != 0 and u != 0. And C satisfies the eigen-relation with s0 = +-kappa, because L_X commutes with d.

The proof uses only:
- (R), the Pesin–Ruelle stable manifold theorem for g_{-1} (cited from memory);
- Oseledets' and Kingman's theorems (standard, cited);
- Lemmas 1 and 3 and Theorem B, proved above;
- Prop 2.2, re-checked above.

## Remarks: what this means for the chain, and what stays open

1. **Open: (E1).** The proof of (N) never uses GH. So with (N) settled, (Lambda) now rests entirely on (E1): under GH, there is no nonzero W in D' with XW = kappa W for real kappa != 0. (E1) is not addressed here; it remains open.
2. **Sharpened target.** Theorem B shows more than (N): every pair x != y that is exponentially asymptotic in backward time (or, by the same construction for -X, in forward time) yields such eigen-distributions, provided all invariant measures have mu(d) = 0. So a proof of (E1) would show that a GH flow has no exponentially asymptotic pairs. Then lambda* = 0 follows from Lemma 2, with no further appeal to Pesin theory beyond (R). This form, "GH excludes exponentially asymptotic pairs", may be a more concrete target than (E1) itself.
3. **Why these objects are not ruled out cheaply.** The distributions T_kappa have genuine order 1 in Case B. This is consistent with the observation in the task that for a measure W, X + kappa is invertible on C^0 when d = 0.
4. **Why the one-sided integral gives no direct contradiction.** S(phi) = int_{-inf}^0 c_phi(t) dt converges in Case B. It satisfies S(X phi + d phi) = phi(x) - e^b phi(y), so u = S/nu solves Xu = -(delta_x - e^b delta_y)/nu. Smearing over a family of pairs whose endpoint measures differ by a smooth density would give Xu smooth. But I see no way to make that family smooth, since Pesin manifolds vary only measurably, nor to show that the smeared u is non-smooth. So this does not yield a direct contradiction with GH. It is recorded only as a possible line of attack on (E1).



[R6-b: round6_q10 Section 2. Lemma M: the meromorphic form of Theorem J]
## 2. Lemma M (proved): no meromorphic eigen-family through z = 0

**Lemma M.** Assume GH. Let r > 0. For 0 < |z| < r let T_z be a distribution density with
 (a) for each smooth phi, z -> T_z(phi) is holomorphic on 0 < |z| < r and meromorphic at 0;
 (b) there are K and C with |T_z(phi)| <= C ||phi||_{C^K} for |z| = r/2;
 (c) T_z(P phi) = z T_z(phi) for all smooth phi and 0 < |z| < r.
Then T_z = 0 for all 0 < |z| < r.

*Proof.* For n in Z put A_n(phi) = (1/2 pi i) oint_{|z| = r/2} T_z(phi) z^{-n-1} dz. By (b), each A_n is a
distribution (|A_n(phi)| <= C (r/2)^{-n} ||phi||_{C^K}). By (a), T_z(phi) = sum_n A_n(phi) z^n is the Laurent
expansion on 0 < |z| < r. Multiply (c) by z^{-n-1} and integrate over the circle. This gives
 A_n(P phi) = A_{n-1}(phi) for all n in Z and all phi.   (2.1)
*Finite order.* E_m = {phi : A_n(phi) = 0 for all n < -m} is a closed subspace of C^inf(M) (an intersection of
kernels of continuous functionals). By (a), the union of the E_m is C^inf(M). By Baire, some E_m has interior, so
E_m = C^inf(M). Hence A_n = 0 for n < -m.
Suppose some A_n is nonzero, and let n0 be the least such index. By (2.1), A_{n0}(P phi) = A_{n0-1}(phi) = 0 for all
phi. So u = A_{n0}/nu satisfies Xu = 0. By L1, u is a constant c, i.e. A_{n0} = c nu. By (2.1) again,
A_{n0+1}(P phi) = c nu(phi) = c int phi dnu. So w = A_{n0+1}/nu satisfies <Xw, phi nu> = -c int phi dnu, i.e.
Xw = -c, a smooth (constant) function. By GH, w is smooth. Let mu be any flow-invariant Borel probability (one
exists, M being compact). Then int Xw dmu = d/dt|_{t=0} int w o g_t dmu = 0, so c = 0 and A_{n0} = 0. This
contradicts the choice of n0. Hence all A_n = 0 and T_z = 0. ∎

Remarks.
1. Only L1 and GH applied to a constant right-hand side are used. The argument uses neither dimension, nor volume,
nor Pesin theory.
2. Without GH the lemma fails. For the north–south flow, the weighted orbit integral over a source-to-sink orbit is
an entire eigen-family of this kind, and its value at z = 0 is a non-constant solution of Xu = 0.
3. If the family is holomorphic on a connected open set Omega containing 0 (respectively meromorphic on Omega with
the bounds (b) near 0), then T_z(phi) = 0 near 0. By the identity theorem it vanishes on all of Omega, for each phi.


[R6-c: round6_q10 Section 4. Theorem B: meromorphic continuation from exact periodicity (in that file (1.1) is d/dt [e^{J_t(w)} phi(g_t w)] = e^{J_t(w)} (P phi)(g_t w), with P phi = X phi + d phi)]
## 4. Theorem B (proved modulo two cited functional-analytic facts): GH excludes heteroclinic connections between periodic orbits

**Definition.** Let O be a periodic orbit of period P > 0 and x in O. A *contracting backward disc* at x is a
C^inf embedded closed disc Dbar containing x such that g_{-P}(Dbar) ⊂ Dbar, with a flat Riemannian metric on Dbar
(a chart metric) in which Dbar is a convex ball and ||D(g_{-P}|_Dbar)|| <= rho1 < 1 pointwise. A *contracting
forward disc* at x' in O' (period P') is defined the same way with g_{P'} in place of g_{-P}.

**Existence (cited, standard).** Suppose the linearised return map Dg_P(x) has an eigenvalue of modulus > 1. Then
the strong unstable manifold W^{uu}(x) of the fixed point x of g_P (for the part of the spectrum outside the unit
circle) is a C^inf injectively immersed submanifold. (Strong unstable manifold theorem, e.g. Hirsch–Pugh–Shub; strong
manifolds are as smooth as the map.) g_{-P} restricted to it is a contraction at x with spectral radius rho < 1.
Choosing a norm on T_x W^{uu} in which ||Dg_{-P}(x)|| < rho1 < 1, a small ball in a chart is a contracting backward
disc. Every y in W^{uu}(x) has g_{-nP} y in Dbar for all large n. For a hyperbolic periodic orbit O, W^u(O) is the
union of the W^{uu}(x), x in O. The same holds with s/forward in place of u/backward.

**Theorem B.** Assume GH. There are no periodic orbits O, O' (possibly O = O'), points x in O and x' in O',
contracting backward and forward discs Dbar at x and Dbar' at x', and a point y not in O ∪ O', such that
g_{-nP} y is in Dbar and g_{n P'} y is in Dbar' for some n >= 0 (equivalently for all large n).
In particular, GH excludes every orbit that is homoclinic or heteroclinic, along strong unstable and strong stable
manifolds, between periodic orbits whose linearised return maps have an eigenvalue outside, respectively inside,
the unit circle. No sign condition on int_O d is needed, so this contains Proposition 4.0.

**Cited facts.**
(H) Hennion's theorem (Proc. AMS 1993), quoted from memory. Let (B, ||.||) be a Banach space and |.| a norm on B
such that bounded subsets of (B, ||.||) are relatively compact for |.|. Let L be bounded on (B, ||.||) and on
(B, |.|) (more precisely, L: (B, ||.||) -> (B, |.|) compact), with
 ||L^n f|| <= R_n ||f|| + C_n |f| for all n,
and set r = liminf R_n^{1/n}. Then the essential spectral radius of L on B is at most r.
(F) Riesz–Schauder / analytic Fredholm theory. If r_ess(L) <= r, then the spectrum of L in {|s| > r} consists of
isolated eigenvalues of finite algebraic multiplicity, and the resolvent s -> (s - L)^{-1} is meromorphic on
{|s| > r} with finite-rank principal parts. Hence q -> (I - qL)^{-1} = q^{-1}(q^{-1} - L)^{-1} is meromorphic on
{|q| < 1/r}, and holomorphic near q = 0, where it is given by the Neumann series.

*Proof of Theorem B.*

**Step 1 (transfer operator on the backward disc).** Put G = g_{-P}|_Dbar and j = J_{-P}|_Dbar (smooth). Fix K >= 1
and let B_K = C^K(Dbar), with ||f||_K = max_{i <= K} sup |D^i f|, derivatives taken in the flat metric. Define
 (L f)(w) = e^{j(w)} f(G w).
By the cocycle rule, (L^n f)(w) = e^{J_{-nP}(w)} f(g_{-nP} w). Indeed J_{-(m+1)P}(w) = J_{-mP}(w) + J_{-P}(g_{-mP} w).
- *Lasota–Yorke bound.* D^K(L^n f) = e^{J_{-nP}} (D^K f)(G^n)[DG^n, ..., DG^n] + (terms containing only D^i f with
 i < K, with coefficients bounded for fixed n). Here ||DG^n|| <= rho1^n by the chain rule, and
 e^{J_{-nP}} <= E^n with E = max_Dbar e^j. So ||L^n f||_K <= E^n rho1^{nK} ||f||_K + C_n ||f||_{K-1}.
- *Compactness.* C^K(Dbar) embeds compactly in C^{K-1}(Dbar) (Arzelà–Ascoli), and L is bounded on both.
- By (H), r_ess(L on B_K) <= r_K := E rho1^K. By (F), q -> (I - qL)^{-1} is meromorphic on {|q| < 1/r_K} as a family
 of bounded operators on B_K.

**Step 2 (backward orbit integrals continue meromorphically to C).** For smooth phi, z in C and w in Dbar put
 Phi_z(w) = int_{-P}^0 e^{-zt} e^{J_t(w)} phi(g_t w) dt.
This is in C^inf(Dbar). It is entire in z as a B_K-valued map, with ||Phi_z||_K <= C(z) ||phi||_{C^K} and C(z) locally
bounded. Splitting (-inf, 0] into the intervals [-(n+1)P, -nP] and using the cocycle rule:
 int_{-inf}^0 e^{-zt} e^{J_t(w)} phi(g_t w) dt = sum_{n >= 0} e^{znP} (L^n Phi_z)(w),   (4.1)
which converges absolutely when Re z < -(log E)/P. (Then ||L^n||_{C^0} <= E^n, and the left side converges
absolutely too.) Fix n0 with y0 := g_{-n0 P} y in Dbar. Define, for Re z < -(log E)/P,
 B_z(phi) := int_{-inf}^0 e^{-zt} e^{J_t(y)} phi(g_t y) dt
  = int_{-n0P}^0 e^{-zt} e^{J_t(y)} phi(g_t y) dt + e^{z n0 P + J_{-n0P}(y)} [(I - e^{zP} L)^{-1} Phi_z](y0).
The second equality uses the shift t = s - n0 P and (4.1) at w = y0.
The right side is meromorphic in z on the half-plane H_K = {Re z < (-log r_K)/P} by Step 1. (Here z -> e^{zP} is
entire, Phi_z is entire, and evaluation at y0 is continuous on B_K.) Since r_K -> 0 as K -> inf and the
continuations for different K agree on a common left half-plane (the Neumann region), B_z(phi) extends to a
meromorphic function on C.
For K fixed and z in a compact set avoiding the poles of the K-resolvent (a set independent of phi),
|B_z(phi)| <= C ||phi||_{C^K}.
*Eigen-identity.* For Re z very negative, integrate (1.1) for w = y by parts over [-R, 0] and let R -> inf. The
boundary term at -R tends to 0 in the Neumann region. This gives
 B_z(P phi) = phi(y) + z B_z(phi);
by uniqueness of meromorphic continuation the identity holds on all of C (both sides are meromorphic in z, since
P phi is smooth).

**Step 3 (forward part).** In the same way, with G' = g_{P'}|_{Dbar'}, j' = J_{P'}, L' f = e^{j'} f o G' and
Phi'_z(w) = int_0^{P'} e^{-zt} e^{J_t(w)} phi(g_t w) dt, the forward integral
 F_z(phi) = int_0^inf e^{-zt} e^{J_t(y)} phi(g_t y) dt
(absolutely convergent for Re z large) extends meromorphically to C, with the analogous bounds and
 F_z(P phi) = -phi(y) + z F_z(phi).

**Step 4 (the eigen-family).** R_z := F_z + B_z is meromorphic on C (weakly), and R_z(P phi) = z R_z(phi). Fix K
large. On the closed unit disc the K-level families have finitely many poles, so there is r in (0, 1) with no pole
in 0 < |z| <= r. Then (a)–(c) of Lemma M hold (with the order bound C||phi||_{C^K} on |z| = r/2). Lemma M gives
R_z(phi) = 0 for 0 < |z| < r and every smooth phi.

**Step 5 (R is not zero).** delta := dist(y, O ∪ O')/3 > 0. Since g_t y -> O as t -> -inf and g_t y -> O' as
t -> +inf (in distance), there is T0 with dist(g_t y, O ∪ O') < delta for |t| >= T0. Shrink Dbar, Dbar' (still
contracting discs) so that g_t w is within delta of O for w in Dbar, t in [-P, 0], and similarly for Dbar'. Take n0,
n0' with n0 P, n0' P' >= T0. Let phi0 >= 0 be smooth, supported in the ball B(y, delta), with phi0(y) = 1. Then
Phi_z = 0 and Phi'_z = 0 for phi0, and phi0(g_t y) = 0 for |t| >= T0. Hence
 R_z(phi0) = int_{-n0P}^{n0'P'} e^{-zt} e^{J_t(y)} phi0(g_t y) dt,
which is entire in z and strictly positive at every real z: the integrand is >= 0 and positive near t = 0. This
contradicts Step 4. ∎

**Remarks.**
1. *Sanity check.* For the north–south flow on S^2 (not GH) the analogous family along a source-to-sink orbit is
entire, and its value at 0 is a non-constant solution of Xu = 0. Lemma M is exactly where GH enters.
2. Theorem B uses no information on the signs of int_O d or int_{O'} d, no volume, and no dimension restriction.
3. The meromorphic continuation in Step 2 is the only place where periodicity is used. It supplies the exact
self-similarity that a generic Pesin point lacks.


[R6-d: round6_q10 Section 7. What remains open]
## 7. What remains open (precisely)

By Corollaries A, 5.1 and 5.3, (PE) — and hence the problem — is reduced to the following statement. It is NOT
proved here.

**(PE-rest).** Under GH, there is no ergodic flow-invariant mu with h_mu(g_1) > 0 such that mu is non-hyperbolic
(it has a zero exponent besides the flow direction; this forces dim M >= 4) and lambda := mu(d) (the sum of the
exponents) satisfies lambda = 0, or lambda <= -chi^+, or lambda >= |chi^-|.

Notes on the two remaining sub-cases.

(R1) |lambda| >= theta (say lambda <= -chi^+ < 0). This is a sketch only, and I expect it is provable. Theorem A
needs backward cancellation at a rate > |lambda|. With k+1 points y_0 = x, y_1, ..., y_k on one unstable leaf, all
forward-generic (available by the non-atomic conditionals), and weights w_i, the combination
sum_i w_i e^{J_t(y_i)} phi(g_t y_i) decays backward like e^{-k theta |t|} times e^{J_t(x)}, provided:
- the leaf maps g_{-t} are written in normal-form coordinates along the leaf, in which they are polynomial maps of
 bounded degree; these are nonstationary normal forms for non-uniform contractions (Kalinin–Sadovskaya, cited from
 memory, not checked);
- the weights solve a moment (Vandermonde-type) system in those coordinates.
In 1-dimensional leaves an affine structure suffices and the weights are divided-difference weights. Then
Theorem A, with kappa < k theta, applies verbatim and Lemma M finishes. Two points are not checked: tempered bounds
on the normal-form charts, and the possibility that the generic points y_i lie on an algebraic subvariety of the
leaf, which would degenerate the moment system.

(R2) lambda = 0, non-hyperbolic, positive entropy. Here supp mu = M (Corollary D1). The obstruction is genuine:
- for generic pairs the eigen-family T_z lives only on the strip 0 < Re z < theta;
- its forward part diverges as z -> 0+ (Patterson behaviour: normalised, it converges to nu-hat, by the one-sided
 version of Lemma D);
- so Lemma M cannot be applied at 0.
Theorem B circumvents this only when exact self-similarity (periodic orbits) gives meromorphic continuation across
Re z = 0. Non-hyperbolic positive-entropy measures need not have periodic orbits nearby: there are C^inf minimal
flows with positive entropy. A forward cancellation by a "quadrilateral" of four points (pairwise backward and
forward asymptotic) would also give a family holomorphic across 0. But it needs the Jacobian-cycle constant and the
temporal-distance constant of the quadrilateral to vanish simultaneously, and I could not produce such
configurations.
This sub-case contains the old core #16 and the volume-preserving case (C) of R4-q10.


[R6-e: round6_q6 Section 5.2 (Lemma Z there = Theorem J / Lemma M in holomorphic-family form; Theorem 1 there = the pair theorem, i.e. Prop 6.1 of R6-a in deterministic form)]
### 5.2 Why lambda = 0 is out of reach of this construction

- **The strip touches 0.** For any construction based on forward orbit integrals of mu-generic points, holomorphy requires Re z > (forward Jacobian rate of the points used) = lambda. So the domain is contained in {Re z > lambda}, and Lemma Z needs 0 to be an interior point. At lambda = 0 one would need points of W^u(x) with forward rate < 0. For mu-generic points the forward rate is exactly 0. Other points of W^u(x) are not controlled by mu (no absolute continuity), and nothing in GH supplies them.
- **Higher-order backward cancellation does not help.** It moves only the right edge of the strip; the left edge is the forward rate.
- **Using -X does not help.** It replaces lambda by -lambda = 0.
- **What would suffice (proved, via the second form of Lemma Z).** Suppose the family T_z of Theorem 1, defined for lambda < Re z < lambda + theta with lambda = 0, admits a continuation (holomorphic, or meromorphic with bounded pole order at 0) to a connected neighbourhood of a segment that joins the strip to 0, still with values in distributions. Then GH is contradicted. Indeed, the relation T_z(P phi) = z T_z(phi) persists under analytic continuation for each phi. The family continues to consist of continuous functionals: Banach–Steinhaus gives local equicontinuity via Cauchy estimates, provided the continuation is locally bounded on each phi. Then Lemma Z applies. So the missing input at lambda = 0 is a *resonance-type continuation* of the single-orbit Laplace transforms int_0^inf e^{-zt} e^{J_t(x)} phi(g_t x) dt across Re z = 0. For individual orbits there is no reason for such a continuation to exist; Re z = 0 is generally a natural boundary.
- **Averaging over pairs does not help either.** Integrating T_z^{(x, y(x))} against conditionals of mu keeps the forward part as an average of e^{J_t}-weighted orbit integrals. By Jensen, int e^{J_t} dmu >= e^{lambda t}, so the left edge does not move below lambda.
- **The normalised limit is consistent with GH.** With s -> 0+ real, s T_s converges along subsequences to some S with S(P phi) = 0, hence S = c nu. In the volume-preserving uniquely ergodic case (nu = omega, d = 0, b = 0), S is the Abel mean of phi(g_t x) - phi(g_t y), and that tends to 0. So the normalised limit gives no contradiction.
- **The core case lies in the gap.** In the smooth-volume uniquely ergodic case, lambda = omega(d) = 0 is forced for the only invariant measure (O2). So the core case of the problem (the case predicted by the Greenfield–Wallach picture) sits exactly where this method stops.


[R6-f: round6_q3 end of Section 4: the lambda = 0 case and the grid (bipartite) remark]
**What remains open: lambda = 0 with mu non-hyperbolic (needs dim M >= 4).**
By Theorem 3.1 and Props. 4.1-4.2 the only case left (unconditionally: non-hyperbolic mu with lambda = 0, or with
lambda outside the ranges of Prop. 4.1) is a non-hyperbolic positive-entropy ergodic mu. For lambda = 0 the
mechanism of Theorem J needs cancellation in BOTH time directions, because e^{J_{+-t}} = e^{o(t)} decays in
neither. Point masses on one unstable leaf give only backward cancellation (strip 0 < Re z < theta, with 0 on the
boundary: this is exactly the old obstruction), and on one stable leaf only forward cancellation.
Linear-algebra reformulation of what would suffice: finitely many generic points z_k, each lying in one
"stable class" (points pairwise exponentially asymptotic forward) and one "unstable class"; first-order
cancellation imposes one linear equation per class on the coefficients; so a nonzero solution exists as soon
as the bipartite graph (classes = vertices, points = edges) has more edges than vertices, e.g. a 3 x 2
"rectangle" x_1, x_2, x_3 on one unstable leaf and their stable-holonomy images x'_1, x'_2, x'_3 on another
unstable leaf. (A single su-cycle (4 points) is not enough: its solvability is a holonomy condition on d which
fails in general.) Such rectangles exist under local product structure, i.e. for hyperbolic measures (already
excluded by Theorem 3.1); for non-hyperbolic mu, W^s(z) and W^u(z') generically do not meet
(dim W^s + dim W^u <= n - 2), and I could not produce such configurations. I also checked that the
pressure function P(q) = sup_m (h_m + q m(d)) does not force a positive-entropy ergodic measure with
lambda != 0 (P may be flat near q = 0), so the lambda = 0 case cannot be reduced away by that route.


=== END OF QUOTED RESULTS ===

=== RESULTS OF ROUND 7 (quoted verbatim from the workers' answers; each labelled with its source; 'the brief' inside them refers to the round-7 task, whose material is the blocks above; 'Text A/Text B', 'Lemma 2', '(O2)', 'L1' refer to the background above; 'R6-a' etc. to the blocks above) ===

[R7-a: round7_q10 Sections 2-4. Theorem J* (quasi-analytic decay), Theorem G (configurations), Proposition 4.1 (reduction to configurations (CH)) and where it stops]
## 2. Theorem J* (quasi-analytic version of Theorem J) — proved

Notation as in the brief: P phi = X phi + d phi, and F_phi(t) = S(e^{J_t} (phi o g_t)).

**Theorem J\*.** Assume GH. Let w : [0, inf) -> [0, inf) be measurable with
M_j := int_R |t|^j e^{-w(|t|)} dt < inf for every j >= 0, and with sum_{j>=1} M_j^{-1/j} = inf.
Let S be a distribution density for which there are k and C with
 |F_phi(t)| <= C e^{-w(|t|)} ||phi||_{C^k}  for all real t and all smooth phi.  (**)
Then S = 0.

*Proof.*
1. As in Theorem J step 1, F_phi is C^1 and F_phi' = F_{P phi}. By (**) applied to P phi,
   |F_phi'(t)| <= C e^{-w(|t|)} ||P phi||_{C^k}.
2. *Moments.* m_j(phi) := int t^j F_phi(t) dt satisfies |m_j(phi)| <= C M_j ||phi||_{C^k}. So m_j is a
   distribution density of order <= k.
3. *Jordan relations.* Fix j >= 0 and phi, and put h(R) := R^j (|F_phi(R)| + |F_phi(-R)|).
   - By (**) and M_j < inf, int_1^inf h(R) dR < inf, hence liminf_{R -> inf} h(R) = 0. Choose R_n -> inf with
     h(R_n) -> 0.
   - Integrate by parts on [-R_n, R_n]: int_{-R_n}^{R_n} t^j F_phi'(t) dt = [t^j F_phi]_{-R_n}^{R_n} - j int t^{j-1} F_phi dt.
   - Let n -> inf. Both integrals converge absolutely by (**) and step 1, and the boundary term tends to 0.
   This gives m_0(P phi) = 0 and m_j(P phi) = -j m_{j-1}(phi) for j >= 1.
4. *Induction.* Exactly as in Theorem J step 4 (using F1 and F2), m_j = 0 for all j.
5. *Quasi-analyticity.* Fix phi and put G(xi) := int e^{-i xi t} F_phi(t) dt for real xi.
   - G is C^inf, with G^{(j)}(xi) = int (-it)^j e^{-i xi t} F_phi dt, so |G^{(j)}(xi)| <= C_phi M_j and
     G^{(j)}(0) = (-i)^j m_j(phi) = 0.
   - The sequence (M_j) is log-convex. By Cauchy-Schwarz, M_j = int |t|^{(j-1)/2} |t|^{(j+1)/2} e^{-w} dt <=
     (M_{j-1} M_{j+1})^{1/2}.
   - Put Mt_j := M_j / M_0. Then Mt_0 = 1, (Mt_j) is still log-convex, and Mt_j^{-1/j} = M_0^{1/j} M_j^{-1/j}.
     Since M_0^{1/j} lies between min(1, M_0) and max(1, M_0), sum Mt_j^{-1/j} = inf.
   - Denjoy-Carleman theorem (cited from memory; Rudin, *Real and Complex Analysis*, Thm 19.11). For a log-convex
     sequence with Mt_0 = 1, the class C{Mt_j} = {f in C^inf(R) : ||f^{(j)}||_inf <= beta_f B_f^j Mt_j} is
     quasi-analytic iff sum Mt_j^{-1/j} = inf. Here G lies in the class with beta = C_phi M_0 and B = 1.
   - So G, all of whose derivatives vanish at 0, is identically 0.
   - F_phi is continuous and in L^1 with Fourier transform 0, so F_phi = 0. Then S(phi) = F_phi(0) = 0. ∎

**Example.** w(t) = t / log(e + t) is admissible. Laplace's method gives max_t (j log t - w(t)) = j log(j log j) + O(j),
the maximum being near t ~ j log j. Hence M_j^{1/j} = O(j log j) and sum M_j^{-1/j} >= c sum 1/(j log j) = inf.
(This is a routine estimate, given here in outline only.) By contrast, w(t) = t^{1-delta} with delta > 0 is NOT
admissible: then M_j^{1/j} ~ j^{1/(1-delta)}, and the sum converges.

**What J\* buys.** An S with two-sided decay e^{-|t|/log|t|} already contradicts GH. So in Theorem G below, and in
Prop. 6.1 / Lemma K, it is enough that the cancellation rate beats the Jacobian growth at the representatives by a
margin of order |t|/log|t|. For example, J_t(x) <= C + theta|t| - |t|/log(e+|t|) suffices against the cancellation
rate e^{-theta|t|}. This does not help in the core case: there the difficulty is the existence of two-sided
cancellation at all, not the size of the margin.

## 3. Theorem G (finite configurations with stable and unstable cancellation) — proved

**Setting.**
- Z = {z_1, ..., z_N} is a set of N >= 1 *distinct* points of M.
- Z is partitioned in two ways: into "stable classes" A_1, ..., A_p and into "unstable classes" B_1, ..., B_q.
  Every point lies in exactly one A and exactly one B.
- In each class a representative is fixed: a(A) in A and b(B) in B.
- Fix constants C >= 1 and theta > eta >= 0. Assume:
  - (S) for each A and each z in A: dist(g_t z, g_t a(A)) <= C e^{-theta t} for all t >= 0;
  - (U) for each B and each z in B: dist(g_t z, g_t b(B)) <= C e^{-theta |t|} for all t <= 0;
  - (R) for each A: J_t(a(A)) <= C + eta t for t >= 0; for each B: J_t(b(B)) <= C + eta |t| for t <= 0.

**Jacobian constants.** For z in A put beta^s_z := lim_{t -> +inf} (J_t(z) - J_t(a(A))). It exists because
J_t(z) - J_t(a) = int_0^t (d(g_s z) - d(g_s a)) ds and the integrand is at most Lip(d) C e^{-theta s}. Moreover
|J_t(z) - J_t(a) - beta^s_z| <= K e^{-theta t} for t >= 0, with K = Lip(d) C/theta. Similarly, for z in B,
beta^u_z := lim_{t -> -inf} (J_t(z) - J_t(b(B))), and |J_t(z) - J_t(b) - beta^u_z| <= K e^{-theta|t|} for t <= 0.

**Theorem G.** Assume GH. In the setting above there is no nonzero vector (w_z)_{z in Z} with
 sum_{z in A} w_z e^{beta^s_z} = 0 for every stable class A, and sum_{z in B} w_z e^{beta^u_z} = 0 for every unstable class B.  (G)

*Proof.* Suppose (w_z) is nonzero and satisfies (G). Put S := sum_z w_z delta_z. Then S != 0, since the points are
distinct, and F_phi(t) = sum_z w_z e^{J_t(z)} phi(g_t z).

*t >= 0.* Fix a class A with representative a. For z in A write
- e^{J_t(z)} = e^{J_t(a)} e^{beta^s_z} e^{r_z(t)}, with |r_z(t)| <= K e^{-theta t} <= K;
- phi(g_t z) = phi(g_t a) + e_z(t), with |e_z(t)| <= ||phi||_{C^1} C e^{-theta t}.

Expanding the product and using |e^{r} - 1| <= |r| e^{|r|}:
 sum_{z in A} w_z e^{J_t(z)} phi(g_t z) = e^{J_t(a)} [ phi(g_t a) sum_{z in A} w_z e^{beta^s_z} + E_A(t) ],
 with |E_A(t)| <= C' e^{-theta t} ||phi||_{C^1}.
The first term vanishes by (G). By (R), |sum_{z in A} ...| <= C'' e^{-(theta - eta) t} ||phi||_{C^1}. Summing over
the finitely many A gives |F_phi(t)| <= C''' e^{-(theta - eta)t} ||phi||_{C^1} for t >= 0.

*t <= 0.* The same computation with the unstable classes, (U), (R) and the second half of (G) gives
|F_phi(t)| <= C''' e^{-(theta-eta)|t|} ||phi||_{C^1}.

So (*) of Theorem J holds with k = 1 and eps = theta - eta > 0. Hence S = 0, a contradiction. ∎

(By Theorem J\*, (R) can be weakened to J_t(rep) <= C + theta|t| - w(|t|) with w admissible.)

**Linear algebra of (G).** (G) is a homogeneous linear system with N unknowns and p + q equations. Each point z
occurs in exactly one equation of each family, with nonzero coefficient. So the system is the incidence system
of a bipartite multigraph Gamma: vertices are the classes, and edges are the points (an edge joins the stable
class and the unstable class of z), with nonzero weights e^{beta}. Hence:
- (a) If N > p + q, a nonzero solution exists, whatever the beta's are.
- (b) A connected component of Gamma that is a tree carries only the zero solution.
- (c) Suppose the component is a single even cycle z_1, ..., z_{2n} (n >= 1, indices mod 2n), where z_{2i-1}, z_{2i}
  share an unstable class and z_{2i}, z_{2i+1} share a stable class. Put
  beta^u(x, y) := lim_{t -> -inf} (J_t(x) - J_t(y)) and beta^s(x, y) := lim_{t -> +inf} (J_t(x) - J_t(y)).
  - The equations are w_{2i} = -w_{2i-1} e^{beta^u(z_{2i-1}, z_{2i})} and w_{2i+1} = -w_{2i} e^{beta^s(z_{2i}, z_{2i+1})}.
  - Going once around the cycle, a nonzero solution exists iff the **Jacobian holonomy** vanishes:
    H := sum_{i=1}^{n} [ beta^u(z_{2i-1}, z_{2i}) + beta^s(z_{2i}, z_{2i+1}) ] = 0.
  - The sign factors contribute (-1)^{2n} = 1.
  - Check: beta^u(x, y) = beta^u_x - beta^u_y for x, y in one unstable class, and similarly for stable classes;
    these are the constants entering (G).

**Corollary G1 (closed su-cycles with zero holonomy).** Assume GH. There are no n >= 1 and distinct points
z_1, ..., z_{2n} (indices mod 2n) such that all of the following hold:
- z_{2i} is exponentially backward-asymptotic to z_{2i-1}, i.e. (U) holds for the pair;
- z_{2i+1} is exponentially forward-asymptotic to z_{2i}, i.e. (S) holds;
- H = 0;
- the growth condition (R) holds at one point of each pair, with eta < theta.

*Proof.* Take the classes {z_{2i-1}, z_{2i}} (unstable) and {z_{2i}, z_{2i+1}} (stable), apply (c) and then
Theorem G. For n = 1 the "cycle" is a pair x != y that is exponentially asymptotic in both time directions. Then
H = beta^u(x, y) + beta^s(y, x) = 0 means lim_{-inf} (J_t x - J_t y) = lim_{+inf} (J_t x - J_t y). ∎

**Corollary G2 (smooth invariant volume).** Assume GH and that X preserves a smooth positive density omega.
- There is no closed su-cycle as in G1 at all, for any n >= 1.
- In particular, no two distinct points are exponentially asymptotic in both time directions.
- Also, no nondegenerate "su-quadrilateral" exists: x, y in W^{uu}(x), z in W^{ss}(x), and a fourth point in
  W^{ss}(y) ∩ W^{uu}(z), with the four points distinct and all asymptotics exponential.

*Proof.* Take nu = omega. Then d = 0 and J = 0, so every beta vanishes, H = 0, and (R) holds with eta = 0.
Corollary G1 applies. ∎

**Corollary G3 (more points than classes).** Assume GH. There is no configuration as in the setting with N > p + q.
This holds for arbitrary Jacobian constants, hence with no holonomy condition. Example: a 3 x 2 "rectangle": three
distinct points x_1, x_2, x_3 on one unstable class, and three distinct points x'_i forward-asymptotic to x_i,
forming a second unstable class (classes {x_i, x'_i} stable). Here N = 6 > 2 + 3 = 5.

*Proof.* By (a), a nonzero solution of (G) exists; Theorem G applies. ∎

**Relation to earlier results.** The single pair (one unstable class of 2 points, two singleton stable classes) is
the case of Prop 6.1, where the forward decay instead comes from lambda < 0 (a singleton stable class with
J_t(a) <= -c t needs no cancellation; Theorem G is stated with eta >= 0, but the same proof allows a singleton
class whose representative has J_t <= C - c|t| on its side). Lemma K is the analogous statement with
Cayley-Hamilton cancellation along a single orbit.

Precise form of the variant, used in Section 4. In Theorem G, any class (stable or unstable) whose representative
satisfies J_t(rep) <= C - c|t| on the relevant time half-line (c > 0) may be **exempted** from its equation in
(G). The proof of Theorem G bounds that class's contribution by e^{J_t(rep)} sum |w_z| ... <= C' e^{-c|t|} ||phi||_inf
without any cancellation. Then eps = min(c, theta - eta).

*Sanity check (consistency, not needed).* Let M = T^1 Sigma × T^2, where Sigma is a closed hyperbolic surface, and
let X = (geodesic generator) + (Diophantine constant field on T^2). This X preserves volume and has positive
entropy. It is not GH, by (O2): the measure mu_gamma ⊗ Leb_{T^2} for a closed geodesic gamma is a second
invariant measure.
- The relation (u(1) l(-1))^3 = ±I in SL(2, R) between the upper and lower unipotents gives closed
  strong-stable/strong-unstable hexagons in T^1 Sigma.
- These hexagons lift to M with the T^2 coordinate unchanged.
So Corollary G2 independently confirms that this X is not GH, as it must be.

## 4. Reduction of (PE-NH) to a configuration statement, and where it stops

**Proposition 4.1 (conditional reduction; proved given its hypothesis).** Assume GH. Let mu be ergodic,
flow-invariant, with h_mu(g_1) > 0 and mu(d) = 0. Assume the following.

**(CH)** There is a finite configuration as in Section 3 whose class representatives are mu-generic in both time
directions, i.e. J_t(rep)/t -> 0 as t -> ±inf. Each stable (resp. unstable) class is contained in the Pesin local
strong stable (resp. unstable) manifold of its representative. The configuration is either
- a closed su-cycle of distinct points with zero Jacobian holonomy H = 0 (automatic if X preserves a smooth volume),
  or
- a configuration with more points than classes.

Then we have a contradiction. So, under GH, (CH) fails for every such mu.

*Proof.* Steps:
1. *Rates.* Let chi^+_min, chi^-_max be as in the brief. Fix 0 < theta < min(chi^+_min, |chi^-_max|) and
   eta := theta/2.
2. *Asymptotics.* By Pesin theory [P] (for g_1 and for g_{-1}), points of the local strong stable manifold of a
   regular point a satisfy dist(g_m z, g_m a) <= C(a) e^{-theta m} for integers m >= 0. Interpolating to real
   t >= 0 with L' = max_{s in [0,1]} Lip(g_s) gives (S) with constant L' C(a) e^{theta}. Likewise (U).
3. *Growth.* For a mu-generic representative, J_t(rep) <= C(rep) + eta|t| for all t in both directions, since
   J_t/t -> 0. This gives (R).
4. *Conclusion.* All constants are finite, because the configuration is finite. Linear algebra (c), respectively
   (a), gives a nonzero solution of (G), and Theorem G gives the contradiction. ∎

Prop. 4.1 only uses that the representatives satisfy (R). It also applies to non-generic points whose Jacobian
grows sub-linearly.

**Hence (PE-NH) at mu(d) = 0 would follow from (CH).** Together with Prop. 6.1 and the (conditional) Prop. 6.2 of
round 6, this would complete the problem, apart from the large-|lambda| case (R1) discussed below.

### Where the argument stops (precise)

1. **(CH) is not available for non-hyperbolic mu.** The center bundle E^c has dimension c >= 2 (the flow
   direction plus at least one zero exponent). So dim W^{ss} + dim W^{uu} = n - c <= n - 2.
   - Closing an su-path into a cycle imposes c independent conditions (closure in the center directions,
     including the temporal direction).
   - Pesin leaves exist only through mu-typical points and vary only measurably (continuously on Pesin blocks,
     which are compact sets with empty interior in general). So no implicit-function argument can produce exact
     closures.
   - For hyperbolic measures, local product structure gives exact rectangles. Corollary G3 then gives another
     proof of Theorem 5.1 that avoids horseshoes. But hyperbolic measures are already excluded.
   - Whether positive entropy plus GH forces some "accessibility" that closes su-cycles is exactly the missing
     point. Nothing in GH that I can see produces it. The only global consequences of GH used so far are L1, F1,
     F2 (on distributions) and their corollaries: Lemma D (uniqueness of the nu-conformal measure), Corollary D1
     (supp mu = M if mu(d) = 0), and B3/B4 (conservativity).
2. **Approximate cycles do not suffice.** Suppose a cycle closes up to a center/temporal defect delta. Then S
   misses cancellation by a term of size delta · e^{J_t} ||phi||_{C^1}. That term does not decay when lambda = 0,
   whatever delta > 0 is, so Theorems J and J\* cannot be applied. Spreading the point masses along a center
   transversal (planner's mechanism (i)) replaces the defect by a derivative in the center direction. Center
   derivatives are not contracted in either time direction (zero exponents), so the C^k norm does not absorb
   them. This is the precise reason mechanism (i) stops.
3. **Mechanism (iii) (sub-exponential decay) is now rigorous (Theorem J\*), but does not help.** Two-sided
   cancellation is still needed, and the only source of cancellation is exponential asymptoticity along strong
   leaves; it is first-order, and exponential when it exists.
4. **Mechanism (ii) (continuation across Re z = 0).** I have nothing to add to round 6.
   - Lemma M needs a meromorphic continuation of single-orbit Laplace transforms.
   - For generic orbits of a non-hyperbolic measure there is no exact self-similarity, which is the ingredient
     Theorem B used.
   - Theorem J\* shows that "quasi-analytic" two-sided decay suffices, but this is still a decay statement for one
     fixed distribution, which is the same difficulty.
5. **Case (R1) (lambda <= -chi^+_min, or the symmetric case).** Theorem G does not help here.
   - The stable side can be exempted (J_t <= C - c t forward).
   - The unstable side needs cancellation at a rate > |lambda| >= chi^+_min. First-order cancellation (Theorem G)
     gives only the rate chi^+_min - delta.
   - Higher-order cancellation requires the non-stationary normal forms along W^u, as in round 6 Prop. 6.2. That
     citation remains unchecked in dimension of W^u >= 2.


[R7-b: round7_q5 Sections 1 and 3. Theorem J uses only (K0) and (K1); a closed-range spectral fact]
## 1. Theorem J and the whole chain use only (K0) and (K1)

Define two conditions on a smooth vector field X (u ranges over distributions, i.e. generalized functions; Xu is the distributional derivative). Neither depends on any choice of density.
- **(K0)** If u is in D'(M) and Xu = 0, then u is constant.
- **(K1)** There is no u in D'(M) with Xu = 1.

GH implies both:
- (K0) is L1 of Text A.
- (K1): GH makes u smooth, and at a maximum point of u we get (Xu) = 0, not 1. This is the argument of (F2).

**Lemma 1.1 (checked).** Theorem J holds with GH replaced by (K0) ∧ (K1).
*Proof.* I re-read the proof of Theorem J (R6-a §2). GH enters only through (F1) and (F2).
- (F1): T(Pφ) = 0 for all φ implies T = cν. Its proof is "u = T/ν has Xu = 0, so u is constant": this is exactly (K0).
- (F2): T(Pφ) = c'∫φ dν implies c' = 0. Its proof is "u = T/ν has Xu = -c'": if c' ≠ 0 then u/(-c') solves Xw = 1, contradicting (K1).
Steps 1–3 and 5 (regularity in t, moments, integration by parts, Fourier uniqueness) use no hypothesis on X. ∎

**Lemma 1.2 (checked).** The following hold under (K0) ∧ (K1) for dim M ≥ 2, with the same proofs:
- P1: at a zero p, d(p) ≠ 0;
- Observation P: no periodic orbit with ∫_γ d = 0;
- Lemma K / K';
- Corollaries 4.1 and 4.2: no homoclinic point of a hyperbolic periodic orbit or zero;
- Theorem 5.1: every positive-entropy ergodic measure is non-hyperbolic. This one is modulo the cited Ruelle inequality and the Katok / Lian–Young horseshoe theorem.

For Lemma K' (applied to -X) note that (K0) and (K1) are invariant under X → -X: Xu = 1 becomes (-X)(-u) = 1.

*Proof.* Where each result uses GH:
- P1 and Observation P use only "Xu = 0 implies u constant", which is (K0). The distribution u there is μ_γ/ν' or δ_p/ν. It is not constant because it is supported on a ν-null set and is nonzero.
- Lemma K uses only Theorem J, which holds by Lemma 1.1.
- Corollaries 4.1 and 4.2 use Lemma K / K', P1, Observation P and the classical stable manifold theorem.
- Theorem 5.1 uses Corollary 4.2 together with the cited [Ru] and [KLY].
None of these uses closed range or the tame estimate. ∎

**Proposition 1.3 (proved, modulo the citations of Lemma 1.2 and the variational principle).** Assume (C) holds for every C^inf flow. Then every C^inf vector field X on a compact connected manifold that satisfies (K0) and (K1) generates a flow of zero topological entropy.

*Proof.*
1. If dim M = 1, every flow on a compact 1-manifold has zero entropy.
2. Let dim M ≥ 2. By the variational principle and the reduction to flow-ergodic measures (step 2 of the chain, checked in R6-a §5), it suffices to show h_μ(g_1) = 0 for every ergodic flow-invariant μ.
3. Suppose h_μ(g_1) > 0. By Lemma 1.2 (Theorem 5.1), μ is non-hyperbolic. Then the 0 exponent of g_1 has multiplicity ≥ 2: the flow direction contributes one (R5-d, as quoted in the brief) and there is at least one further zero exponent.
4. (C) gives a nonzero S with two-sided exponential decay.
5. Lemma 1.1 (Theorem J under (K0) ∧ (K1)) gives S = 0. This is a contradiction. ∎

**Corollary 1.4.** (C) implies (DUE-0).
*Proof.* Let ω be a smooth invariant volume and take ν = ω, so d = 0 and P = X.
- (K0) is DUE. If Xu = 0, then T = uω satisfies L_X T = (Xu)ω = 0, so T is invariant and hence T = cω, i.e. u = c. Conversely, DUE says exactly that every invariant distribution density is cω.
- (K1) is automatic. If Xu = 1, pairing with ω gives ⟨Xu, ω⟩ = -⟨u, L_X ω⟩ = 0. But ⟨1, ω⟩ = ω(M) > 0.
Proposition 1.3 then applies. ∎

**Remarks.**
- DUE means only that the transposed operator has dense range. GH means kernel = constants plus closed range.
- I know no proof of (DUE-0) and no reference for it, from memory. The DUE diffeomorphisms I recall (Avila–Fayad–Kocsard, built by approximation by conjugation) have zero entropy, but I know of no theorem saying DUE forces zero entropy.
- So proving (C) would in particular settle (DUE-0). That statement is stronger than the problem, and the problem's extra hypothesis (closed range) is not used.
- Conversely, refuting (C) requires a flow that has a non-hyperbolic positive-entropy ergodic measure but no S. Note that this does not need such a flow to satisfy (K0) or (K1). Still, by Proposition 1.3, the most natural source of counterexamples (flows where some (K0) ∧ (K1) mechanism forbids S) would be positive-entropy (K0) ∧ (K1) flows, and I cannot construct one.
## 3. A GH-only spectral fact that DUE does not give (proved)

This records a consequence of the closed-range part of GH, which Section 1 shows must eventually be used.

**Proposition 3.1.** Assume GH and that X preserves a smooth probability ω. Let A be the self-adjoint generator of the unitary Koopman group U_t f = f∘g_t on L^2(ω), so that U_t = e^{itA} and X = iA on smooth functions. For f in L^2 let σ_f be its spectral measure. Then for every j there are m_j and C_j such that for every smooth f with ∫f dω = 0:
 σ_f({0}) = 0, and ∫ ξ^{-2j} dσ_f(ξ) ≤ C_j ||f||^2_{C^{m_j}}.

*Proof.*
1. By (O2), the invariant distribution densities are cω. Closed range (Corollary 3) and its duality consequence give f = Xu_1 with u_1 smooth, and we may take ∫u_1 dω = 0.
2. Lemma 2 (Text B) gives ||u_1||_{C^k} ≤ C||f||_{C^m}. Iterating gives smooth mean-zero u_j with X^j u_j = f and ||u_j||_{L^2} ≤ C_j ||f||_{C^{m_j}}.
3. Unique ergodicity (O2) gives ker A = constants. Since f ⊥ 1, σ_f({0}) = 0.
4. f = (iA)^j u_j gives dσ_f = ξ^{2j} dσ_{u_j}. Hence ∫ξ^{-2j} dσ_f = σ_{u_j}(R \ {0}) ≤ ||u_j||^2. ∎

So the spectral measures of smooth functions vanish to infinite order at 0, tamely in f. Theorem J is the analytic form of this statement for one fixed S: it kills all Taylor coefficients at 0 of the cross-spectral density, and then uses analyticity.

Positive entropy gives countable Lebesgue spectrum on the orthocomplement of the Pinsker factor. That alone gives no contradiction: smooth functions approximating a Lebesgue-spectrum vector in L^2 can have spectral measures vanishing to infinite order at 0, with constants that blow up.

A contradiction would need **tame** control on how smooth functions see the Lebesgue part near frequency 0. That is the same missing ingredient as the decay rate required by (C).


[R7-c: round7_q1 Section 2. Proposition N (Ledrappier-Young intermediate laminations); 'Lemma 6.0' is in R6-a]
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


[R7-d: round7_q8 Part 2. Closed graph, closed range and duality (Lemmas A-F) and what they give]
### Lemma A (tame a priori estimate). Under GH, for every k >= 1 there exist m and C such that ||u||_{C^k} <= C ||Xu||_{C^m} for every smooth u with int u dnu = 0.

*Proof.*
1. Let E = { u in L^2(nu) : Xu in C^inf (in D') }. Give E the seminorms ||u||_{L^2} and ||Xu||_{C^j}, j >= 0.
2. E is Fréchet. If (u_n) is Cauchy, then u_n -> u in L^2 and Xu_n -> f in C^inf. Since Xu_n -> Xu in D', we get Xu = f.
3. By GH, E is contained in C^inf. The inclusion E -> C^inf has closed graph, because both spaces inject continuously into D'. By the closed graph theorem it is continuous. So for each k there are m, C with ||u||_{C^k} <= C(||u||_{L^2} + ||Xu||_{C^m}).
4. To remove the L^2 term, argue by contradiction. Suppose there are mean-zero smooth u_n with ||u_n||_{C^k} > n ||Xu_n||_{C^m}. Rescale so that ||u_n||_{L^2} = 1. Then ||u_n||_{C^k} <= C(1 + ||u_n||_{C^k}/n), so ||u_n||_{C^k} <= 2C once n >= 2C.
5. Hence ||Xu_n||_{C^m} -> 0. Because k >= 1, Arzelà–Ascoli gives a subsequence u_n -> u in C^0. This u has mean 0, ||u||_{L^2} = 1 and Xu = 0 in D'.
6. By (L1), u is constant, so u = 0. This contradicts ||u||_{L^2} = 1. ∎

### Lemma B (closed range and duality). Under GH:
1. R is closed in C^inf, and R = { f : T(f) = 0 for all T in I }.
2. For f in R, the unique mean-zero solution u = X^{-1} f satisfies ||u||_{C^k} <= C_k ||f||_{C^{m(k)}}.
3. For every T in (C^k)' with T(1) = 0, there is S in (C^{m(k)})' with S(X phi) = T(phi) for all phi, and ||S|| <= C_k ||T||.

*Proof.*
- (i) Take Xu_n -> f in C^inf with u_n of mean zero. Lemma A for every k shows (u_n) is Cauchy in C^inf. Its limit u satisfies Xu = f. The description of R then follows from Hahn–Banach, since R is closed.
- (ii) This is Lemma A.
- (iii) Put S(X phi) := T(phi - nu(phi)) = T(phi). This is well defined because ker X = constants and T(1) = 0. Moreover |S(X phi)| <= ||T|| ||phi - nu(phi)||_{C^k} <= C ||T|| ||X phi||_{C^m}. Extend S to C^m by Hahn–Banach. ∎

In particular, for any two points p, q there is a current S_{pq} of order <= m(0) with uniformly bounded norm such that S_{pq}(X phi) = phi(p) - phi(q).

### Lemma C (bounded Birkhoff integrals). For f in R: sup_{p, t} |int_0^t f(g_s p) ds| <= 2 C_0 ||f||_{C^{m(0)}}.

*Proof.* With u = X^{-1} f, the integral equals u(g_t p) - u(p). ∎

### Lemma D (the Lebesgue class is ergodic). Under GH, every Borel set B with nu(g_t B Δ B) = 0 for all t is nu-null or nu-conull.

*Proof.*
- For a smooth density omega, int_B L_X omega = d/dt|_0 int_B g_t^* omega = d/dt|_0 int_{g_t B} omega = 0. Differentiating under the integral is allowed because g_t^* omega is C^1 in t, uniformly on M.
- So X 1_B = 0 in D'. By (L1), 1_B is a.e. constant. ∎

**Corollaries of Lemma D.**
1. Every nonempty open invariant set is conull. Every proper closed invariant set is nu-null.
2. nu-a.e. orbit is dense. Apply (1) to the saturations of a countable base.
3. If dim M >= 2, the flow is conservative for nu. Sketch, quoting the Hopf decomposition from memory: the dissipative part is invariant, so it is null or conull. If it were conull, ergodicity would force nu to sit on a single orbit, and an orbit is Lebesgue-null when n >= 2.
4. (Cesàro statement.) For w in L^inf, every weak-* limit point of A_T w = (1/T) int_0^T w∘g_s ds is invariant and hence constant.
   - Invariance holds because ||(A_T w)∘g_r - A_T w||_inf <= 2|r| ||w||_inf / T.
   - Hence, for every mean-zero rho in L^1(nu), the Cesàro averages of the transfer operator applied to rho tend to 0 weakly in L^1. By the Yosida–Kakutani mean ergodic theorem (cited from memory) they tend to 0 in norm.
   - So all absolutely continuous probability measures have the same Cesàro push-forward asymptotics.

### Lemma E (absolutely continuous invariant measures). If mu = h nu is flow-invariant with h > 0 a.e. and log h in L^1, then h is smooth. So mu is a smooth invariant volume.

*Proof.*
- Invariance gives log h∘g_t - log h = -J_t a.e. for each t.
- Pair with a test density, divide by t and let t -> 0. Since J_t / t -> d uniformly, this gives X(log h) = -d in D'.
- By GH, log h is smooth. ∎

### Lemma F (the volume-preserving case). Suppose d is in R, i.e. d = -X psi with psi smooth. Equivalently, by Lemma B, T(d) = 0 for every T in I. Then nu' = e^{psi} nu is invariant, and:
1. I = R nu', so the flow is **uniquely ergodic** and **minimal**.
2. R = { f : nu'(f) = 0 }. So **every** mean-zero smooth f is a smooth coboundary with the tame bounds of Lemma B. This is Katok's "cohomological C^inf-stability".
3. There are m, C such that for all p, t and smooth f: |int_0^t f(g_s p) ds - t nu'(f)| <= C ||f||_{C^m}.
4. Consequently, every orbit segment of length >= C' eps^{-(m+n)} meets every eps-ball, where n = dim M.

*Proof.*
1. div_{nu'} X = d + X psi = 0. Write T in I as T(phi) = u(phi nu') with u a generalized function. Then T(X phi) = u(L_X(phi nu')) = -(Xu)(phi nu'). So T is in I iff Xu = 0, which by (L1) means u is constant.
   - Unique ergodicity follows.
   - Minimality: every orbit closure supports an invariant measure, which must be nu'. Since nu' has full support, every orbit closure is M.
2. This is Lemma B(i) combined with (1).
3. Apply Lemma C to f - nu'(f).
4. Apply (3) to a bump f of height 1 and radius eps. Then nu'(f) is of order eps^n and ||f||_{C^m} is of order eps^{-m}. ∎

### What this first move gives for (PE-NH), and where it stops

- **Volume-preserving case.** If d is a coboundary (for instance when X preserves a smooth volume), Lemma F reduces (PE-NH) to the following statement.
  - (*) A C^inf flow cannot have positive entropy if it is minimal and uniquely ergodic with a smooth measure nu', and every mean-zero smooth function is a smooth coboundary with the tame bounds of Lemmas B and C.
  - The non-hyperbolic case of (*) is exactly what remains, since in the hyperbolic case Katok's periodic orbits contradict unique ergodicity.
  - I could not prove (*). Spectral arguments are insufficient. Positive entropy gives countable Lebesgue spectrum on the Pinsker complement. The coboundary property only forces spectral measures of smooth functions to vanish to infinite order at 0 (f = X^k u_k for all k). That is compatible with Lebesgue spectrum, because such vectors are dense in the Pinsker complement.
- **Leaf-cycle variant.** Let x_0, ..., x_{2k} be a closed stable/unstable cycle that closes up to a flow segment. Then the regularized alternating sum of full-orbit "measures" lies in I. In the volume case this sum must therefore be c nu', and testing on 1 gives c = 0.
  - Test it on an eps-bump at a generic vertex x_1. The passage of x_1 through the bump at time 0 contributes about eps. Partner orbits contribute only through returns within time O(log(1/eps)), which do not occur for generic vertices. So the sum is nonzero, a contradiction.
  - Hence: **in the volume case, under GH, no closed s/u-cycle (closing up to a flow segment) passes through generic points of mu.** The step "generic vertices do not return to the bump within time O(log 1/eps)" is only sketched.
  - For hyperbolic mu such cycles exist by local product structure. For non-hyperbolic mu, center directions block local product structure, so existence of cycles is precisely the open point.
  - This is close in spirit to the excluded "Dirac masses on leaves" move. I report it only as a by-product.
- **General (non-volume) case.** Lemmas A–E still hold. But I may contain elements that are not measures, and nothing here controls them or the class [d] in C^inf / R. Note that d is in R exactly when T(d) = 0 for all T in I (Lemma B). So "every T in I kills d" would reduce the general case to the volume case. I could not prove it. By the mu(d)-band result, mu(d) = 0 is one allowed value for a positive-entropy measure, so even the measures in I are not controlled.


[R7-e: round7_q7 Sections 2-4. Lemma H (Carleman uniqueness on a half-disc), Theorem V (volume case and quasi-analytic vectors of X^{-1}), Proposition O (no Hennion continuation with zero exponents). 'R5-a Lemma 2' there = Step 2 of block R5-a; '(H)', '(F)' = Hennion's theorem and Riesz-Schauder theory as cited in R6-c]
## 2. Lemma H (proved): uniqueness for eigen-families known only on a strip, under Carleman-flatness at 0

Lemma M needs a continuation of T_z to a punctured neighbourhood of 0. The following purely complex-analytic lemma replaces the continuation by quantitative flatness on the half-disc.

**Lemma H.** Let r > 0, U := {z : Re z > 0, |z| < r}, and let f be holomorphic on U. Suppose there are C and numbers K_N in [0, inf) (N = 0, 1, 2, ...) with
 |f(z)| <= C K_N |z|^N / Re z for all z in U and all N,
and put Lambda(y) := inf_N K_N y^{-N} for y >= 1. If int_1^inf log Lambda(y) dy/y^2 = -infinity, then f = 0 on U.

*Proof.* Fix a with 1/(2a) < r and let H := {z : Re(1/z) > 2a}. This is the open disc with centre 1/(4a) and radius 1/(4a). Every z in closure(H) \ {0} has Re z > 0 and |z| <= 1/(2a) < r, so closure(H) \ {0} ⊂ U. Put g(w) := f(1/w), which is holomorphic on a neighbourhood of the closed half-plane {Re w >= 2a}. Since Re z = Re w/|w|^2 and |z| = 1/|w|,
 |g(w)| <= C K_N |w|^{2-N} / Re w.
- With N = 2: |g| <= C K_2/(2a) on {Re w >= 2a}, so g is bounded there.
- On the line w = 2a + iy with |y| >= 1: |w| >= |y|, so |w|^{-N} <= |y|^{-N}, and |g(2a+iy)| <= (C/2a) |w|^2 Lambda(|y|).
Hence log|g(2a+iy)| <= c + 2 log(|y| + 2a) + log Lambda(|y|), and int log|g(2a+iy)| dy/(1+y^2) = -infinity (the positive part is bounded, because g is bounded).
[cited: Hardy-space fact, e.g. Garnett, Bounded Analytic Functions, Ch. II] If g is bounded and holomorphic on an open half-plane, continuous on its closure, and not identically 0, then the integral of log|g| over the boundary line against dy/(1+y^2) is > -infinity.
So g = 0. Hence f = 0 on H, and so on U by the identity theorem. ∎

Remark. [cited: Mandelbrojt / Ostrowski] For log-convex K_N the condition int log Lambda(y) dy/y^2 = -inf is equivalent to sum K_N^{-1/N} = inf, i.e. to the Carleman condition. If K_N <= A B^N, then Lambda(y) = 0 for y > B and the condition holds trivially.
Lemma H is sharp for the same reason as Remark 1.3. f(z) = e^{-1/sqrt z} (principal branch) is holomorphic and nonzero on U and satisfies |f(z)| <= e^{-|z|^{-1/2}/sqrt 2} <= C_N |z|^N on U. Here C_N ~ (2N)! 2^N is a Gevrey-2, non-quasi-analytic sequence. So flatness at the boundary point 0 alone never suffices; a quasi-analytic rate is needed.

## 3. Theorem V (proved): the volume-preserving case reduced to quasi-analytic vectors of X^{-1}

Setting: GH, and X preserves a smooth positive density omega. Take nu = omega, so d = 0, J_t = 0 and P = X. Write omega-hat = omega/omega(M). By (O2), the invariant distribution densities are the multiples of omega. By the duality consequence of Text A, X(C^inf) = {f : omega-hat(f) = 0} =: C^inf_0. By Corollary 3 of Text B, X: C^inf_0 -> C^inf_0 is a topological isomorphism. Let R := (X|_{C^inf_0})^{-1}. For smooth phi put phi_0 := phi - omega-hat(phi),
 K_N(phi) := ||R^N phi_0||_{C^1},  Lambda_phi(y) := inf_N K_N(phi) y^{-N},
and let Q be the set of smooth (complex-valued) phi with int_1^inf log Lambda_phi(y) dy/y^2 = -infinity ("quasi-analytic vectors of R").

**Theorem V.** In this setting, suppose lambda* > 0 (lambda* := lim (1/n) max_x log||Dg_n(x)||; by Ruelle's inequality and the variational principle, h_top(g_1) > 0 implies lambda* > 0). Then Q is not dense in C^inf(M) for the C^1 norm.
Equivalently: if Q is C^1-dense, then lambda* = 0 and h_top(g_1) = 0.

*Proof.*
1. By R5-a Lemma 2 (which uses only lambda* > 0 and the cited Pesin-Ruelle theorem), there are x != y and C0, theta > 0 with d(g_{-t}x, g_{-t}y) <= C0 e^{-theta t} for t >= 0. Let S := delta_x - delta_y and F_phi(t) := phi(g_t x) - phi(g_t y). Then
 |F_phi(t)| <= C0 e^{-theta|t|} ||phi||_{C^1} for t <= 0,  |F_phi(t)| <= 2||phi||_inf for t >= 0.
(In the volume case no hypothesis on J is needed, because J = 0.)
2. For z in the strip Sigma := {0 < Re z < theta} put T_z(phi) := int_R e^{-zt} F_phi(t) dt. This is holomorphic in z, and |T_z(psi)| <= (2/Re z + C0/(theta - Re z)) ||psi||_{C^1}. Since F_{X psi} = F_psi', and the boundary terms vanish at both ends (Re z > 0 handles +inf; the backward bound with Re z < theta handles -inf), integration by parts gives T_z(X psi) = z T_z(psi). Also F_1 = 0, so T_z(1) = 0.
3. Hence, for any smooth phi and any N: T_z(phi) = T_z(phi_0) = T_z(X^N R^N phi_0) = z^N T_z(R^N phi_0). On U := {Re z > 0, |z| < theta/2} this gives
 |T_z(phi)| <= (2 + C0) K_N(phi) |z|^N / Re z.
4. If phi is in Q, Lemma H gives T_z(phi) = 0 on U, hence on Sigma by the identity theorem.
5. Each T_z (z in Sigma) is continuous for the C^1 norm. So if Q were C^1-dense, T_z = 0 for every z in Sigma. But take phi_* smooth with phi_*(x) = 1 and phi_*(y) = 0. Then G(t) := e^{-theta t/2} F_{phi_*}(t) is continuous and in L^1 with G(0) = 1, and its Fourier transform is omega' -> T_{theta/2 + i omega'}(phi_*). So that transform is not identically 0 (R5-a step (f)), a contradiction. ∎

**Corollary V.1 (sanity check).** In the setting of Theorem V with lambda* > 0, the constants together with the smooth eigenfunctions of X (X phi = i eta phi, eta real and nonzero) do not span a C^1-dense subspace.
(Proof: a finite combination phi of eigenfunctions with |eta_i| >= delta has mean zero, R phi_i = phi_i/(i eta_i), and K_N(phi) <= A delta^{-N}. So Lambda_phi = 0 for large y, and phi is in Q.) This is consistent with the classical fact that discrete spectrum forces zero entropy; it is not new.

**Where Theorem V stops (precise).** The models show what is missing.
- Diophantine linear flows on T^n: the trigonometric polynomials lie in Q (geometric K_N), so Q is dense.
- For real-analytic phi on T^n with |phi-hat_k| <= e^{-a|k|} and |k.alpha| >= c|k|^{-tau}: ||R^N phi||_{C^1} grows like (N!)^tau, with tau >= n-1. This is non-quasi-analytic for n >= 3, so analyticity of phi is not the right notion.
Thus a GH volume-preserving flow with lambda* > 0 would have to be one in which no C^1-dense set of smooth functions has iterated inverses R^N of quasi-analytic growth. GH, through the closed graph theorem, gives the existence of the tame bounds ||R psi||_{C^k} <= C_k ||psi||_{C^{m_k}} and nothing about the growth of C_k, m_k, or of ||R^N phi||. I could not produce quasi-analytic vectors from GH alone. L^2 spectral theory (X is skew-adjoint on L^2(omega)) gives L^2-analytic vectors (spectral subspaces E(|eta| > delta)), but T_z is not L^2-continuous: it has order 1, because of the point masses.
Remark on removing the point masses. One can make S absolutely continuous, S = sigma omega with sigma in L^1, by smearing the pair along unstable leaves over a Pesin block, using the absolute continuity of the unstable foliation for omega. If sigma is in L^2, then for Re z > 0 the forward part equals <(z - X)^{-1} phi, sigma>, and the backward part is the continuation of -<(z - X)^{-1} phi, sigma> from Re z < 0. Then T_z is the jump of the L^2 resolvent across iR, i.e. 2 pi times the density of the cross spectral measure of (phi, sigma), continued into the strip. GH (step 3) makes this density flat at 0 to all orders. Positive entropy (countable Lebesgue spectrum off the Pinsker factor) does not contradict flatness for individual phi, and I could not get a contradiction for a dense set of phi. So the gap is the same: smooth phi whose spectral data near 0 is controlled quantitatively.
**Non-volume case.** Step 3 needs a tame inverse of P = X + d on its range. Without a smooth invariant volume, P is injective on C^inf, and its range is dense in ker(nu-hat), since the annihilator of the range of P is span(nu) by (F1). I could not show that this range is closed. By the closed range theorem for Fréchet spaces [cited], this is equivalent to weak*-closedness of the range of the transpose of P, i.e. of L_X on distribution densities. Even granting it, the iteration breaks: P^{-1} maps ker(nu-hat) into C^inf but not into ker(nu-hat).

## 4. Approach (2): continuation via Pesin-block transfer operators, and why it stops

### 4.1 The continuation is needed only for the forward part
Let mu be ergodic with h_mu > 0 and mu(d) = 0. Let x be mu-generic and y != x a mu-generic point of xi(x) ⊂ W^u_loc(x) (Lemma 6.0). Let b, theta be as in Prop 6.1, S = delta_x - e^b delta_y, and T_z = B_z + F_z with
 B_z(phi) = int_{-inf}^0 e^{-zt} F_phi(t) dt,  F_z(phi) = int_0^inf e^{-zt} F_phi(t) dt.
- For t <= 0: |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|} ||phi||_{C^1} and J_t(x) = o(|t|). So B_z is holomorphic on the half-plane Re z < theta, which contains Re z = 0 and everything to its left.
- So the transfer operator on unstable discs proposed in the brief serves the backward part, and the backward part needs no continuation. Theorem B used that operator only because its points were not generic.
- The obstruction is entirely in F_z. This is the difference of the two single-orbit forward transforms int_0^inf e^{-zt} e^{J_t(w)} phi(g_t w) dt, for w = x and for w = y (weight e^b). The forward orbits of x and y separate, since y is on the unstable leaf of x.
- In Theorem B, F_z continued because the forward orbit of y entered a contracting forward disc at a periodic point and stayed there. Then one autonomous operator L' f = e^{j'} f o g_{P'} on C^K(disc) represents the whole forward tail, and the resolvent (I - e^{-zP'} L')^{-1} continues it.

### 4.2 What a Pesin-block version would need, and what fails
For a mu-generic w, the forward returns to a Pesin block K occur at times n_1 < n_2 < ..., with return maps g_{n_{i+1} - n_i} between different local stable discs W^s_loc(g_{n_i} w). The forward transform becomes sum_i e^{-z n_i} (L_i ... L_1 Phi_i)(w), a non-autonomous product with no resolvent identity, so Hennion + Riesz-Schauder (facts (H), (F) of R6-c) do not apply.
To get one autonomous operator, it must act on functions on the whole family of discs {W^s_loc(v) : v in K}, as the induced (first-return) weighted Koopman operator. That space contains functions that are constant along the discs, and on them the operator is the Koopman operator of the induced base dynamics, including the centre (zero-exponent) directions, which are neither contracted nor expanded. The following shows that this kills quasi-compactness.

**Proposition O (proved).** Let L be a bounded operator on a Banach space B with infinitely many distinct eigenvalues of modulus >= 1. Then r_ess(L) >= 1, so (H)+(F) cannot give a meromorphic resolvent on any disc {|s| > r} with r < 1.
*Proof.* If r_ess(L) = r < 1, then by (F) the spectrum in {|s| > r} consists of isolated eigenvalues. The infinitely many eigenvalues in the compact set sigma(L) ∩ {|s| >= 1} would accumulate at a point s* with |s*| >= 1 > r, and s* lies in sigma(L) since the spectrum is closed. Then s* is not isolated, a contradiction. ∎

*Application (model with a zero exponent).* Let N carry a flow h_t with an ergodic positive-entropy measure m (e.g. an Anosov flow). On N × T^q take g_t(n, theta) = (h_t n, theta + t alpha) with alpha Diophantine and mu = m × Haar. Then mu has q additional zero exponents, and its local stable and unstable discs are W^{s/u}_h(n) × {theta}.
- Let L f = e^{j} f o g_P be the fixed-time weighted Koopman operator on any Banach space B of functions on a family of such discs (or on N × T^q) that contains the functions e_k(n, theta) = e^{i k.theta}, with product volume so that j = 0.
- Then L e_k = e^{i P k.alpha} e_k. For all but countably many P these eigenvalues are pairwise distinct for infinitely many k, so r_ess(L) >= 1 by Proposition O.
- Directly: ||L^n e_k||_{C^K} ~ |k|^K while |e_k|_{C^{K-1}} ~ |k|^{K-1}. So no Lasota-Yorke inequality ||L^n f||_K <= R_n ||f||_K + C_n |f|_{K-1} with R_n < 1 can hold on all e_k.
The continuation step of Theorem B is GH-free. So any GH-free continuation theorem for non-hyperbolic positive-entropy mu would have to work in such product models, and there the Hennion mechanism provably has no spectral gap.
This does not prove that the pair transform has a natural boundary at Re z = 0 in the model. Heuristically it does: for phi = sum_k a_k(n) e^{ik.theta}, F_z(phi) = sum_k e^{ik.theta} A_k(z - i k.alpha), where A_k is the forward pair transform of the base flow. A singularity of A_k at 0 (expected, of size zeta^{-1/2}, from CLT behaviour of a(h_t n) - a(h_t n')) is then copied to the dense set {i k.alpha}. That is a heuristic, not a proof.

### 4.3 Mechanisms (i) and (iii) of the sketch
- (iii) is settled in §1. Quasi-analytic two-sided decay suffices and non-quasi-analytic decay does not (for the moment method). Two-sided decay is still required, so (iii) does not remove the need for forward cancellation.
- (i), smearing along the centre: for S = int rho(c) delta_{x(c)} dc along a centre curve, F_phi(t) for t >= 0 is int rho(c) e^{J_t(x(c))} phi(g_t x(c)) dc. With a zero exponent, the curve g_t(x(c)) has length e^{o(t)}, so averaging over c gives no exponential gain. In the product model, the integral of e^{i k.(theta(c) + t alpha)} rho(c) dc does not decay in t at all. So centre-smearing cannot replace the missing su-intersections. In the model, dim W^{ws} + dim W^{uu} = n - q < n, so forward and backward clusters cannot be matched by holonomy.


[R7-f: round7_q6 Sections 1 and 3. Theorem G with flow shifts (linear algebra over the group ring C[R]); why centre smearing and su-closing fail]
## 1. The grid criterion with flow shifts (Theorem G) — proved (uses only Theorem J)

Notation as in the brief: nu, d = div_nu X, J_t(z) = int_0^t d(g_s z) ds, and
 F^z_phi(t) := e^{J_t(z)} phi(g_t z)  (z in M, t in R, phi smooth).
Cocycle identity: e^{J_s(z)} F^{g_s z}_phi(t) = F^z_phi(t+s). Fix a Riemannian distance; d is Lipschitz.

**Definition.** Let theta > 0, tau in R. z' is *forward theta-asymptotic to z with shift tau* if d(g_t z', g_{t+tau} z) <= C e^{-theta t} for all t >= 0 (some C). *Backward* : d(g_t z', g_{t+tau} z) <= C e^{-theta|t|} for all t <= 0. (Shift 0 = the usual strong stable / unstable relation; a shift means z' lies on the strong stable (unstable) leaf of a point of the orbit of z, i.e. on the "weak" leaf.)

**Grid data.** Points z_1, ..., z_N such that
 (G1) the orbits of the z_k are pairwise distinct, and no z_k is a zero of X or periodic;
 (G2) a partition of {1..N} into *forward classes* C_1..C_p; each class C has a representative index r = r(C) in C, and for k in C a shift tau_k with z_k forward theta-asymptotic to z_r with shift tau_k (tau_r = 0);
 (G3) a partition into *backward classes* D_1..D_q, representatives r'(D), shifts sigma_k, backward theta-asymptotic;
 (G4) J_t(z_k) <= C + eta|t| for all real t and all k, for some eta < theta.

**Theorem G.** Assume GH. Grid data with N > p + q do not exist.

*Lemma G.1 (Jacobian constants).* In (G2), beta_k := lim_{t -> +inf} [J_t(z_k) - J_{t+tau_k}(z_r)] exists and |J_t(z_k) - J_{t+tau_k}(z_r) - beta_k| <= C_1 e^{-theta t} for t >= 0. Consequently
 F^{z_k}_phi(t) = e^{beta_k} F^{z_r}_phi(t + tau_k) + E_k(t),  |E_k(t)| <= C_2 e^{J_{t+tau_k}(z_r)} e^{-theta t} ||phi||_{C^1}  (t >= 0).
*Proof.* J_t(z_k) - J_{t+tau}(z_r) = J_t(z_k) - J_t(g_tau z_r) - J_tau(z_r); its t-derivative is d(g_t z_k) - d(g_t g_tau z_r), bounded by Lip(d) C e^{-theta t}, which is integrable; this gives the limit and the rate. For E_k: write e^{J_t(z_k)} = e^{J_{t+tau_k}(z_r)} e^{beta_k + r(t)}, |r(t)| <= C_1 e^{-theta t}; then |E_k| <= e^{J_{t+tau_k}(z_r)} e^{beta_k}[ |e^{r} - 1| ||phi||_inf + ||d phi||_inf d(g_t z_k, g_{t+tau_k} z_r) ]. ∎
The same holds backward with constants beta'_k := lim_{t -> -inf}[J_t(z_k) - J_{t+sigma_k}(z_{r'})].

*The ring.* Let R = C[R] be the group algebra of the additive group (R,+): finite formal sums psi = sum_j c_j [s_j], equivalently finitely supported complex measures sum c_j delta_{s_j} on R with convolution as product ([a][b] = [a+b]). R is an integral domain (group algebra of a torsion-free abelian group, hence of an ordered group, over a field: the product of the leading terms w.r.t. the order is the leading term of the product, so it is nonzero). For psi in R and a function F on R put (psi ⋆ F)(t) := int F(t+s) dpsi(s) = sum_j c_j F(t + s_j). Then ([a]psi) ⋆ F (t) = int F(t+s+a) dpsi(s), and (psi psi') ⋆ F = psi ⋆ (psi' ⋆ F).

*Proof of Theorem G.* Unknowns psi_1..psi_N in R. Equations: for every forward class C, Lambda_C := sum_{k in C} e^{beta_k} [tau_k] psi_k = 0; for every backward class D, M_D := sum_{k in D} e^{beta'_k} [sigma_k] psi_k = 0. These are p + q homogeneous R-linear equations in N > p + q unknowns. Over the fraction field of the domain R such a system has a nonzero solution; multiplying by a common denominator gives a nonzero solution (psi_k) in R^N. Write psi_k = sum_j c_{kj} [s_{kj}] and define the finite complex combination of Dirac masses
 S := sum_k sum_j c_{kj} e^{J_{s_{kj}}(z_k)} delta_{g_{s_{kj}} z_k}.
(i) S != 0: by (G1) the map (k, s) -> g_s z_k is injective, so the points carrying S are pairwise distinct; some c_{kj} != 0.
(ii) By the cocycle identity, S(e^{J_t} phi o g_t) = sum_k (psi_k ⋆ F^{z_k}_phi)(t).
(iii) Forward bound. Let T_0 = max |s_{kj}| + max|tau_k| + max|sigma_k|. For t >= T_0 and a forward class C with representative r, Lemma G.1 gives
 sum_{k in C} (psi_k ⋆ F^{z_k})(t) = sum_{k in C} e^{beta_k} sum_j c_{kj} F^{z_r}(t + s_{kj} + tau_k) + E_C(t) = (Lambda_C ⋆ F^{z_r})(t) + E_C(t) = E_C(t),
 with |E_C(t)| <= C_3 max_{k,j} e^{J_{t+s_{kj}+tau_k}(z_r)} e^{-theta(t + s_{kj})} ||phi||_{C^1} <= C_4 e^{-(theta - eta)t} ||phi||_{C^1} by (G4). Summing over classes: |S(e^{J_t} phi o g_t)| <= C_5 e^{-(theta-eta)t} ||phi||_{C^1} for t >= T_0, and trivially <= C_6 ||phi||_inf for 0 <= t <= T_0.
(iv) Backward bound: identical, with the backward classes and Lemma G.1 for t -> -inf.
(v) For real phi, Re S and Im S (real combinations of Dirac masses) satisfy the same bounds, so (*) of Theorem J holds for both with k = 1, eps = theta - eta. Theorem J gives Re S = Im S = 0, contradicting (i). ∎

**Remarks.** (1) The Jacobian holonomy around su-cycles is absorbed by the constants e^{beta_k}, e^{beta'_k} in the equations (item (c) of the brief: it is never an obstruction). (2) **Temporal closing defects are absorbed exactly** by allowing several flow-translates of each point: in Fourier terms the equations read sum_k e^{beta_k - i xi tau_k} psihat_k(xi) = 0, one exponential-polynomial equation per class, and the solution psi_k are finite combinations of Dirac masses in time. So only *weak* (flow-shifted) asymptotic classes matter, and an su-cycle need only close up to a flow shift. (3) Classes whose representative satisfies J_t(z_r) <= C - eps t (t >= 0) need no equation (their contribution already decays); this recovers Prop. 6.1 of R6-a (single backward class {x, y}, forward classes singletons, lambda < 0). (4) The count N > p + q is the "more edges than vertices" condition of R6-f for the bipartite graph (vertices = classes, edges = points); a connected component with E > V must contain two independent cycles. A single su-cycle (E = V) is not enough in general.
(5) Classes may be merged freely: the relation "forward theta-asymptotic with some shift" is transitive (d(g_t a, g_{t+tau+tau'} c) <= d(g_t a, g_{t+tau} b) + d(g_{t+tau} b, g_{t+tau+tau'} c) <= C e^{-theta t} + C e^{-theta(t+tau)}), and merging only lowers p + q. So the right object is the **weak su-graph** Gamma: vertices = weak forward classes and weak backward classes, edges = orbits (an orbit lies in a single weak forward and a single weak backward class), an edge joining the two classes of its orbit. Theorem G says: *under GH, every finite subgraph of Gamma spanned by orbits satisfying (G1), (G4) (with a common rate theta > eta) has at most as many edges as vertices, i.e. each connected component contains at most one cycle (Gamma restricted to good orbits is a pseudoforest).*
**Corollary G.2.** Under GH, no ergodic flow-invariant mu with mu(d) = 0 admits mu-generic points (two-sided Birkhoff generic for d, so (G4) holds with any eta > 0) forming grid data with N > p + q, for any theta > 0.

## 3. Items (a), (b), (c) of the brief: what works, what does not, and why

Write the exponents of mu as u positive, c zero (c >= 2: flow plus at least one more), s negative; n = u + c + s. Let E^c_0 denote the "genuine" center (Oseledets space of exponent 0 modulo RX), of dimension c - 1 >= 1.

**(c) Jacobian holonomy: no obstruction (proved).** Theorem G: the constants e^{beta}, e^{beta'} enter as coefficients of a linear system; only the count N > p + q matters.

**Temporal (flow-direction) defect: no obstruction (proved).** Theorem G, Remark (2): the flow commutes with itself, so g_s W^s(z) = W^s(g_s z) and e^{J_s(z)} F^{g_s z}(t) = F^z(t+s); classes are flow-equivariant and time-smearing by finitely supported measures turns the class conditions into exponential-polynomial equations over the domain C[R]. So an su-cycle needs to close only modulo the flow. (Same proof: if mu-good orbits are permuted by a further vector field Y with [X, Y] = 0 tangent to E^c_0, smearing along Y works too, with C[R^2]; this covers product-like situations, but is no help in general.)

**(a) Intersections W^{s0} ∩ W^{u0}: the genuine center defect (obstruction; analysis, partly heuristic).** W^{s0}(z) has dimension s + 1, W^{u0}(z') dimension u + 1, and both contain the flow lines; modulo the flow they are of dimensions s and u in an (n-1)-dimensional quotient, and s + u = n - c = (n - 1) - (c - 1). So the existence of a bracket point is c - 1 >= 1 real conditions in excess of transversality.
- *Locally* (sketch): in a Lyapunov chart at z_1, if the stable and unstable plaques through nearby good points are smooth graphs and the Frobenius bracket form omega: E^u x E^s -> E^c_0 (the E^c_0-component of [V, W] for V tangent to the unstable and W tangent to the stable plaques) is nonzero at z_1, then the E^c_0-defect of the would-be quadrilateral with corners z_2 = exp(v) in W^u_loc(z_1), z_4 = exp(w) in W^s_loc(z_1) is Delta(v, w) = omega(v, w) + o(|v||w|). For u = s = 1, c = 2 (the first open dimension, n = 4) and omega(z_1) != 0 this is nonzero for all small v, w != 0: **no small su-quadrilateral closes, even modulo the flow.** Only when E^s ⊕ E^u ⊕ RX is "jointly integrable" along the support (omega = 0 and the brackets exist) does Proposition 2.1 apply.
- *Non-atomicity of both conditionals does not help:* it gives positive-dimensional (typically fractal, possibly of small Hausdorff dimension) families of corners, but the closing condition is c - 1 real equations on these families; no measure- or dimension-theoretic principle forces a nontrivial solution on a given fractal set (Marstrand-type statements hold for almost every member of a parametrized family, not for one dynamically given map).
- *Global (long) cycles:* leaves are immersed and recurrent, so long su-paths might close; each further u- or s-leg adds parameters while the closing condition stays (c - 1)-dimensional, so heuristically long closed weak su-cycles should exist when the conditional dimensions are not too small — but I can prove nothing of the kind. Already deciding whether two good leaves W^{s0}(z), W^{u0}(z') meet anywhere is a global question about the measure's leaves on which GH gives no information.

**(b) Smearing along the center (dead end, with reason).** Replace a point mass by a smooth density along a disc tangent to E^c_0, so that a closing defect delta in E^c_0 becomes, to first order, delta times a derivative along a center vector field Y. Then the defect contributes delta · S_1( Y(e^{J_t} phi o g_t) ), and Y(phi o g_t) = dphi(Dg_t Y) o g_t with |Dg_t Y| = e^{o(|t|)} (exponent 0), with no cancellation available (Dg_t Y is not tangent to any class structure). So the defect term is of size delta e^{o(|t|)} ||phi||_{C^1}: it does not decay at all, let alone exponentially, and making delta small (or summing infinitely many cycles with defects delta_j -> 0) does not produce decay in t. Exponential decay in Theorem J requires exact class membership; this is exactly where the flow direction differs from E^c_0 (equivariance). Weakening Theorem J to quasi-analytic decay (planner's (iii)) does not help here either, since the defect term does not decay.

**Which measures the approach cannot handle (precise form of the obstruction).** By Theorem G the grid method (finite combinations of Dirac masses, including time-smearing) produces a contradiction for mu exactly when the weak su-graph Gamma restricted to good orbits (two-sided rate-0 Jacobian growth, e.g. mu-generic orbits and their brackets) contains a finite subgraph with more edges than vertices. If for mu this graph is a pseudoforest (every component has at most one cycle), no finite grid exists and the method gives nothing; in particular this happens if no two good orbits off one weak stable class are joined both ways, i.e. if W^{s0}(z) ∩ W^{u0}(z') contains no good orbit for good z, z' in distinct classes. The heuristics above say this is the expected situation for "accessible-type" non-hyperbolic measures (omega != 0) whose conditional measures have small dimension; I could not prove for any specific flow that its graph is a pseudoforest, so this is stated as the obstruction, not as a theorem.


[R7-g: round7_q4 Lemma 3.2 and S3.5. Integrable two-sided decay gives imaginary eigen-distributions; free backward cancellation at lambda = 0]
### 3.2 Integrable two-sided decay gives a continuum of imaginary eigen-distributions
**Lemma 3.2 (no GH needed).** Let S be a distribution density. Suppose that for every smooth phi, F_phi is in L^1(R), with int |F_phi| dt <= C ||phi||_{C^k}. For real xi put T_xi(phi) = int e^{-i xi t} F_phi(t) dt. Then:
- each T_xi is a distribution density of order <= k with T_xi(P phi) = i xi T_xi(phi);
- u_xi = T_xi/nu satisfies X u_xi = -i xi u_xi;
- if S != 0, then T_xi != 0 for all xi in a nonempty open set of R.
*Proof.* The order bound is clear. F_phi is C^1 with F_phi' = F_{P phi} (Theorem J, step 1), and F_{P phi} is in L^1. So F_phi has limits at plus and minus infinity, and these limits are 0 because F_phi is in L^1. Integrating by parts, int e^{-i xi t} F_phi' dt = i xi int e^{-i xi t} F_phi dt. This is the eigen-relation, and it translates into X u_xi = -i xi u_xi by Observation 0. If S(phi) != 0 for some phi, then F_phi(0) = S(phi) != 0, so the continuous L^1 function F_phi is not identically 0. By Fourier uniqueness its Fourier transform xi -> T_xi(phi) is a continuous function that is not identically 0, hence nonzero on an open set. ∎

**Consequence.** Theorem J can be extended from exponential to merely integrable two-sided decay, provided one proves:
(E1-i) under GH, the set of xi in R for which X u = i xi u has a nonzero solution u in H^{-s} is countable (for each s).
For smooth solutions, (E1-i) holds. If u is smooth and nonzero, then |u|^2 is smooth and X|u|^2 = 0, so |u| is a nonzero constant by L1. Eigenfunctions with distinct eigenvalues are orthogonal in L^2(m) for any invariant probability m, and L^2(m) is separable. For distributional solutions I could not prove (E1-i). It is a new sharp open sub-question. In the Diophantine linear case it holds by Fourier series.

### 3.5 First-order backward cancellation needs no normal forms when lambda = 0 (proved, standard Pesin input)
Let mu be ergodic with lambda = mu(d) = 0. Let x be mu-generic and Pesin-regular, and let W be a C^inf local unstable disc through x with d(g_t y, g_t x) <= C e^{-theta|t|} for t <= 0, uniformly in y in W. Let m be any finite measure on W (leaf Lebesgue, or the conditional mu^u_x), and psi bounded measurable with int psi e^{-beta_x} dm = 0, where beta_x(y) = -lim_{t -> -inf}(J_t(y) - J_t(x)). Then S = psi m satisfies |S(e^{J_t} phi o g_t)| <= C e^{-(theta - delta)|t|} ||phi||_{C^1} for t <= 0.
*Proof.* e^{J_t(y)} = e^{J_t(x)} e^{-beta_x(y)}(1 + O(e^{-theta|t|})) and phi(g_t y) = phi(g_t x) + O(||phi||_{C^1} e^{-theta|t|}), uniformly on W. The leading term e^{J_t(x)} phi(g_t x) int psi e^{-beta_x} dm vanishes, and e^{J_t(x)} = e^{o(|t|)}. ∎
So in the case (PE0) the backward half of Theorem J is free for any first-order-balanced measure on an unstable disc. Everything hinges on the forward half (S4).


=== END OF ROUND-7 RESULTS ===
