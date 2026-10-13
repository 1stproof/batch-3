kind: attempt
Open question attempted: the missing statement (PE) (ledger entry 53), by a named approach not tried before: "generic Ledrappier-Young pairs" feeding the pair construction of [R5-a] Theorem B, with GH used through L1 at the eigenvalue 0.

## Task
Prove (PE) (stated below in the chain section): under GH, every ergodic invariant probability mu of the flow has h_mu(g_1) = 0 — or find exactly where the following approach fails and repair it.

Notation: nu smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi. Observation 0 + L1 (quoted below): a distribution density T with T(P phi) = 0 for all smooth phi is a constant multiple of nu. More generally T(P phi) = z T(phi) means u = T/nu satisfies Xu = -z u.

The approach. Suppose mu is ergodic with h_mu(g_1) > 0; put lambda = mu(d) (this number does not depend on nu).
Step 1. By Ruelle's inequality (for g_1 and g_{-1}) mu has a positive and a negative exponent. By Pesin theory, mu-a.e. x has a local unstable manifold W^u_loc(x) of positive dimension, and for y in it d(g_{-t}x, g_{-t}y) <= C e^{-theta t} for t >= 0, theta > 0 any number below the smallest positive exponent. By Ledrappier-Young, h_mu > 0 implies that the conditional measures of mu on unstable manifolds are non-atomic; hence for mu-a.e. x there are (uncountably many) y != x in W^u_loc(x) that are mu-generic for d in both time directions.
Step 2. For such a pair define, as in [R5-a] Step 4, b = lim_{t->-inf}(J_t(x) - J_t(y)), c_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b+J_t(y)} phi(g_t y), and T_z(phi) = int_R e^{-zt} c_phi(t) dt. Using J_t(x), J_t(y) = lambda t + o(|t|) (genericity) instead of the uniform sublinearity of [R5-a] Lemma 3, check that T_z is defined, of order <= 1 and holomorphic in z on the strip lambda < Re z < lambda + theta, and that T_z(P phi) = z T_z(phi). (Verify these bounds carefully; the forward bound for y uses only that y is forward-generic.)
Step 3 (the GH input). If -theta < lambda < 0, then z = 0 is in the strip and T_0 is P-harmonic, so T_0 = c nu by L1. Derive a contradiction by showing that for a suitable pair T_0 is not a constant multiple of nu (for instance: T_0 depends on y, while c(y) nu would have to vary in a one-dimensional space — exploit the freedom to move y along the non-atomic conditional measure, linear combinations of pairs, or the location of the orbits). If 0 < lambda < theta' use stable manifolds and -X (GH is preserved).
Step 4 (the hard cases). (i) |lambda| >= theta: can the strip be widened (e.g. use the fastest unstable direction, or pairs on strong unstable manifolds, or pairs whose partner is chosen by a different genericity), or can a different weight than e^{J_t} be used so that 0 becomes reachable? (ii) lambda = 0 (this includes every flow with a smooth invariant volume): here z = 0 is the boundary of both strips; when the flow has a smooth invariant volume and every mean-zero smooth function is Xu with u smooth, one computes T_z -> 0 as z -> 0 (exact cancellation via the transfer function u: T_0(phi) = -(u(x)-u(y)) + (u(x)-u(y))). Find a second-order or averaged object that survives at lambda = 0 — e.g. the derivative dT_z/dz at 0, the normalised limit T_z/||T_z||, families of pairs integrated against the conditional measures, or triples — and show it is a non-smooth solution of Xu = smooth, or a P-harmonic density different from c nu.
A proof of (PE) only for some measures (e.g. only 0 < |lambda| < theta) does not answer the question, though it should be reported with full proof if it is all you find. Deliverable: a complete proof of (PE), or the strongest proved partial result and the exact point where the approach stops (with a reason, if you find one, why it cannot work at lambda = 0).

=== THE CHAIN OF THIS ATTEMPT (for orientation) ===
The problem asks to show that a GH vector field has a flow of zero topological entropy ('[GOAL]' below means exactly that claim). The current missing statement is:

**Missing statement (PE).** Let M be a compact connected smooth manifold and X a smooth vector field on M with flow g_t such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Then every ergodic invariant Borel probability measure mu of the flow (g_t) has measure-theoretic entropy h_mu(g_1) = 0. (Equivalent forms, all usable: h_top(g_1) = 0; for C^inf flows, by Kozlovski's equality, lim_{t->inf} (1/t) log int_M ||Lambda Dg_t(x)|| dnu(x) = 0, where Lambda A is the full exterior power.)

**Chain.**
1. (Missing statement, PE) Under GH, every ergodic flow-invariant Borel probability mu has h_mu(g_1) = 0.
2. Classical (cited; round5_q2 Thm 4.1(a) writes out the reduction from g_1-invariant to flow-invariant measures): h_top(g_1) = sup h_mu(g_1) over g_1-invariant probabilities (variational principle); for g_1-invariant mu, mu-bar = int_0^1 (g_s)_* mu ds is flow-invariant and h_{mu-bar}(g_1) = h_mu(g_1) (g_s commutes with g_1; entropy is affine, Jacobs); by the ergodic decomposition of mu-bar for the flow and affinity again, h_mu(g_1) <= sup over ergodic flow-invariant mu' of h_{mu'}(g_1) = 0 by step 1. Hence h_top(g_1) = 0, which is the [GOAL].
Nothing else is needed.

Neither (V) 'GH implies a smooth invariant volume' nor (Lambda) 'GH implies lim (1/t) log max ||Dg_t|| = 0' is available as a fact (both open; (Lambda) is strictly stronger than the goal, see [R5-h]).
=== END OF CHAIN ===

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

=== RESULTS OF THE MOST RECENT ROUND (quoted verbatim from the workers' answers; each labelled with its source; 'the task'/'the brief'/'the planner' inside them refer to earlier task files, and 'Lemma C', 'Lemma D', 'Corollary D1', 'L1', 'P1', 'Observation P', 'B3', '(O1)-(O4)', '[R4-q7] Prop 2.1/2.2' refer to the background above) ===

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


[R5-b: GH. L^1 eigenfunctions and measurable time functions]
## Conventions
ν is a smooth positive density and d = div_ν X. J_t(x) = ∫_0^t d(g_s x) ds, so (g_t)^*ν = e^{J_t} ν. A generalized function W pairs with smooth densities ρ, and XW is defined by ⟨XW, ρ⟩ = −⟨W, L_X ρ⟩. For smooth W this agrees with the usual derivative. L1 (Text A) says: if Xu = 0 with u in D', then u is constant. GH is the hypothesis of the problem. n = dim M.

## Lemma 0 (ergodicity of ν; this is "N1", reproved here)
Assume GH. Let A be a Borel set with ν(g_t A Δ A) = 0 for every t. Then ν(A) = 0 or ν(M∖A) = 0.

*Proof.* Let φ be smooth. By change of variables, ∫_A (φ∘g_t) e^{J_t} dν = ∫_{g_t A} φ dν = ∫_A φ dν for all t. The integrand is C^1 in t, with t-derivative bounded uniformly in x for |t| ≤ 1, and at t = 0 that derivative equals Xφ + dφ. Differentiating under the integral at t = 0 gives ∫_A (Xφ + dφ) dν = 0. This says ⟨X1_A, φν⟩ = −⟨1_A, L_X(φν)⟩ = 0, so X1_A = 0 in D'. By L1, 1_A is a.e. constant. ∎

## Lemma 1 (integrated eigen-relation)
Let W be in D'(M) and κ in C with XW = κW. Then for every smooth density ρ and every real t,
⟨W, (g_{−t})^*ρ⟩ = e^{κt} ⟨W, ρ⟩.
If W is in L^1(M), this says W∘g_t = e^{κt} W ν-a.e., for each t.

*Proof.* Put F(t) = ⟨W, (g_{−t})^*ρ⟩. The map t ↦ (g_{−t})^*ρ is smooth into the space of smooth densities, with derivative −(g_{−t})^* L_X ρ = −L_X (g_{−t})^*ρ. (L_X commutes with pullback by its own flow.) Hence
F'(t) = −⟨W, L_X (g_{−t})^*ρ⟩ = ⟨XW, (g_{−t})^*ρ⟩ = κ F(t),
so F(t) = e^{κt} F(0).

Now let W be in L^1 and ρ = φν. Then (g_{−t})^*ρ = (φ∘g_{−t}) e^{J_{−t}} ν. Substituting x = g_{−t} y gives
∫ W(g_t x) φ(x) dν(x) = ∫ W(y) φ(g_{−t}y) e^{J_{−t}(y)} dν(y) = F(t) = e^{κt} ∫ W φ dν.
This holds for all smooth φ, so W∘g_t = e^{κt} W a.e. ∎

## Lemma T (no measurable time function)
Assume GH and n ≥ 2. There is no Borel function τ : M → R (finite ν-a.e.) such that, for each t, τ∘g_t = τ + t ν-a.e.

*Proof.* Suppose such a τ exists. Define π(x) = g_{−τ(x)} x. This is Borel, because x ↦ (τ(x), x) is Borel and (s, y) ↦ g_{−s} y is continuous.

For each t, and for a.e. x,
π(g_t x) = g_{−τ(x)−t} g_t x = π(x).

Let E be a Borel set in M and A = π^{−1}(E). Then g_t^{−1}A = A mod ν for every t, because each g_t is a diffeomorphism and therefore preserves ν-null sets. By Lemma 0, ν(A) is either 0 or ν(M). So m = π_*(ν/ν(M)) is a Borel probability on the compact metric space M that takes only the values 0 and 1.

Its support is a single point. If p ≠ q were both in the support, disjoint neighbourhoods of p and q would both have positive m-measure, hence both measure 1, which is impossible. So m = δ_p for some p. Then π(x) = p a.e., which means x = g_{τ(x)} p, i.e. a.e. x lies on the orbit O(p) = {g_s p : s in R}.

But O(p) is the union over k in Z of the images of [k, k+1] under the smooth map s ↦ g_s p. Each image has Hausdorff dimension ≤ 1 < n, so it is ν-null, and O(p) is ν-null. This contradicts ν(M) > 0. ∎

## Theorem 1 ((E1) for integrable W)
Assume GH. Let κ be real with κ ≠ 0, and let W be in L^1(M) (complex-valued) with XW = κW in D'(M). Then W = 0 a.e.

More generally, the same conclusion holds for any Borel function W that satisfies, for each t, W∘g_t = e^{κt} W a.e.

*Proof, n ≥ 2.* By Lemma 1 it suffices to treat the pointwise relation. Since κ is real, |W|∘g_t = e^{κt}|W| a.e. So A = {W ≠ 0} satisfies g_t^{−1}A = A mod ν for every t.

Suppose W is not a.e. 0. Then ν(A) > 0, so A is conull by Lemma 0. Then τ = κ^{−1} log|W| is finite a.e. and satisfies τ∘g_t = τ + t a.e. for each t. This contradicts Lemma T. ∎

*Proof, n = 1.* Then M = S^1. We first show that X has no zeros; let Z be its zero set.
- If Z = M, then X = 0 and every distribution solves Xu = 0, so GH fails.
- If M∖Z has a component I (an open invariant arc) with ν(M∖I) > 0, then 1_I is a non-constant invariant function. Indeed, g_t I = I, and Lemma 0's computation gives X1_I = 0. This contradicts L1.
- Otherwise M∖Z is a single arc of full measure, so Z = {p} is a single point. Then X does not change sign, so X'(p) = 0 in a chart. Hence div_ν X(p) = 0, which contradicts P1.

So X has no zeros. Then every orbit is the whole circle, with a common period P, and g_P = id. Hence W = W∘g_P = e^{κP} W a.e., which forces W = 0. ∎

**Remarks.**
1. Theorem 1 covers every W in H^s for s ≥ 0 and every W in L^p for p ≥ 1.
2. It also works for complex κ with Re κ ≠ 0: use Re κ in place of κ.
3. The proof uses only L1 and Lemma 0, which give ergodicity and hence conservativity of ν. It does not use the tame estimate.
4. Sanity check: GH is necessary. The north–south flow on S^2 has an L^1 eigenfunction W = e^{κτ}, where τ is a time function on the wandering region. It is integrable when κ is smaller than the contraction exponent at the sink. That flow is not GH.

## Corollary 2 (measure solutions are singular)
Assume GH. Let T be a complex Radon measure, let W = T/ν, and suppose XW = κW with κ real and nonzero. Then T is singular with respect to ν.

*Proof.* By Lemma 1, T_t = e^{κt} T for every t, where T_t(φ) := T((φ∘g_{−t}) e^{J_{−t}}). This identity first holds for smooth φ, and then for bounded Borel φ because both sides are measures.

The operation T ↦ T_t is a push-forward by a diffeomorphism followed by multiplication by a positive smooth function. So it maps measures absolutely continuous to ν to absolutely continuous ones, and singular measures to singular ones. By uniqueness of the Lebesgue decomposition T = T_ac + T_s, we get (T_ac)_t = e^{κt} T_ac for all t.

Write T_ac = Wν with W in L^1. The relation (T_ac)_t = e^{κt} T_ac is exactly ⟨W, (g_{−t})^*ρ⟩ = e^{κt}⟨W, ρ⟩. Differentiating at t = 0 gives XW = κW. By Theorem 1, W = 0, so T = T_s. ∎

This is consistent with known item (1): the tilted conformal measures are carried by supp μ, and by B4 they have ν-null basins.


[R5-c: GH. Measurable cocycles]
## (A) Measurable cocycles and eigenfunctions

### Lemma 0 (transport identity).
Let W be a distribution with XW = -kappa W (kappa in C). Then W o g_t = e^{-kappa t} W in D' for every t. Here (W o g_t)(rho) := W((g_t)_* rho).

*Proof.*
1. For a smooth density rho, the map t -> (g_t)_* rho is a smooth curve in the smooth densities, with derivative -L_X (g_t)_* rho.
2. Let f(t) = <W, (g_t)_* rho>. Then f'(t) = -<W, L_X (g_t)_* rho> = <XW, (g_t)_* rho> = -kappa f(t).
3. Hence f(t) = e^{-kappa t} f(0). ∎

When W is in L^1(nu), the conclusion says W(g_t x) = e^{-kappa t} W(x) for nu-a.e. x, for each fixed t.

The same computation applies to an L^infinity function u with u o g_t = u a.e. for each t. Then <u, L_X rho> = -d/dt|_0 int (u o g_t) rho = 0, so Xu = 0 in D'. This fact is used below and called (*).

### Theorem 1 (proved).
Assume GH and n >= 2. Let b be a continuous real function such that mu(b) != 0 for every invariant Borel probability mu. Write B_t(x) = int_0^t b(g_r x) dr.

Then there is no Borel function V: M -> R such that, for each t in R, V(g_t x) = V(x) - B_t(x) for nu-a.e. x.

*Proof.*

**Step 1 (constant sign).** The set of invariant probabilities is convex and weak* compact. The map mu -> mu(b) is affine and continuous, so it has constant sign. Replacing (V, b) by (-V, -b) if necessary, assume mu(b) > 0 for all mu.

**Step 2 (uniform growth).** There are T0 > 0 and c > 0 with B_T(x) >= cT for all x and all T >= T0.

Suppose not. Then there are T_k -> infinity and points x_k with B_{T_k}(x_k) <= T_k/k. Take a weak* limit point mu of the empirical measures (1/T_k) int_0^{T_k} delta_{g_r x_k} dr. It is invariant and mu(b) <= 0, a contradiction.

**Step 3 (positive cohomologous function).** Fix T >= T0. Put b' = B_T/T, which is continuous with b' >= c > 0. Put w = (1/T) int_0^T B_r dr, which is continuous. Since B_r(g_s x) = B_{r+s}(x) - B_s(x), the function s -> w(g_s x) is C^1 with derivative (b' - b)(g_s x). Hence w o g_t - w = B'_t - B_t, where B'_t = int_0^t b' o g_r.

Set V' = V - w. Then V' o g_t = V' - B'_t a.e., for each t.

**Step 4 (measurable section).** Fix x. The map s -> B'_s(x) is a strictly increasing homeomorphism of R onto R: it is >= cs for s >= 0 and <= cs for s <= 0. Let theta(x) be the unique s with B'_s(x) = V'(x). Then theta(x) = sup{s in Q : B'_s(x) < V'(x)}, so theta is Borel.

Put pi(x) = g_{theta(x)}(x), which is Borel.

Fix t, and take x with V'(g_t x) = V'(x) - B'_t(x); this holds for a.e. x. Using B'_s(g_t x) = B'_{s+t}(x) - B'_t(x), the number theta(g_t x) is the s solving B'_{s+t}(x) = V'(x). So theta(g_t x) = theta(x) - t, and therefore pi(g_t x) = pi(x).

Thus for each t, pi o g_t = pi nu-a.e.

**Step 5 (contradiction with L1).** Let psi be continuous on M and put u = psi o pi, which is in L^infinity. By Step 4, u o g_t = u a.e. for each t. By (*), Xu = 0, so by L1, u is a.e. equal to a constant c_psi.

Take a countable family {psi_j} that separates points. Then for a.e. x, pi(x) is the same point p. So a.e. x equals g_{-theta(x)}(p), which lies on the orbit of p.

That orbit is the image of R under a C^1 map, hence nu-null since n >= 2. This contradicts nu(M) > 0. ∎

### Corollary 2 (E1 for L^1 functions; proved).
Assume GH and n >= 2. If W is in L^1(nu), complex valued, with XW = -kappa W in D' and Re kappa != 0, then W = 0.

*Proof.*
1. By Lemma 0, W o g_t = e^{-kappa t} W a.e., for each t.
2. Let A = {W != 0}. Then 1_A o g_t = 1_A a.e., so X 1_A = 0 by (*). By L1, either nu(A) = 0 (and we are done) or A is conull.
3. In the second case, V = log|W| is a.e. finite and satisfies V o g_t = V - (Re kappa) t a.e.
4. Apply Theorem 1 with b ≡ Re kappa; then mu(b) = Re kappa != 0 for every mu. This gives a contradiction. ∎

**Remark 2'.**
- Same proof, using the variable-multiplier version of Lemma 0: there is no nonzero W in L^1 with L_X(W nu) = -s W nu (s real) whenever -s lies outside [min_mu mu(d), max_mu mu(d)]. Here b = s + d.
- That interval contains 0 by Prop 2.1 of the brief.
- Singular eigenmeasures are not excluded. These are the tilted conformal measures of [R4-q7] Prop 2.2, and they exist. Theorem 1 needs nu-measurable objects, because L1 is a statement about distributions.

### Corollary 3 (proved; M orientable, or pass to the orientation double cover).
Under GH, there is no nonzero closed (n-1)-current C of finite mass with C(L_X beta) = s C(beta) for all smooth (n-1)-forms beta, with s real and s != 0.

*Proof.*
1. Write C(beta) = int beta ∧ Ĉ, where Ĉ is a 1-form with measure coefficients.
2. Closedness: 0 = C(d eta) = ± int eta ∧ dĈ for all eta, so dĈ = 0.
3. The eigen-relation: int L_X beta ∧ Ĉ = -int beta ∧ L_X Ĉ. So L_X Ĉ = -s Ĉ.
4. de Rham–Hodge for currents (cited) gives Ĉ = h + dW, with h a smooth harmonic form and W in D'.
5. Cartan: L_X Ĉ = d(i_X Ĉ). Hence s h = -d(i_X Ĉ + sW) is exact and harmonic, so h = 0.
6. Then d(XW + sW) = 0, so XW + sW is a constant c. Replace W by W - c/s; now XW = -sW, and Ĉ = dW.
7. A distribution whose differential is a finite measure is a BV function (cited, standard). So W is in L^1. By Corollary 2, W = 0, hence C = 0. ∎

---


[R5-d: GH. Hyperbolic measures of positive entropy force uniformly dissipative horseshoes; dead ends of smearing constructions. Cited classical theorems are marked]
## 4. Dimension 3: reduction to one configuration (proved, modulo cited classical theorems)
Cited from memory (no GH involved):
 [Rue] Ruelle's inequality: for a C^1 diffeomorphism f of a compact manifold and ergodic mu,
   h_mu(f) <= sum of positive Lyapunov exponents of mu.
 [KLY] Katok's horseshoe theorem, flow version (Katok 1980 for diffeomorphisms; Lian-Young, J. AMS 2012, for C^2 flows):
   if mu is an ergodic invariant probability of a C^2 flow, mu is not supported on a zero of X, all exponents of mu
   other than the flow direction are nonzero, and h_mu > 0, then there is a compact invariant hyperbolic set Lambda
   on which the flow is topologically conjugate to a suspension of a transitive subshift of finite type of positive
   entropy (a "horseshoe"); Lambda is locally maximal and transitive, its periodic orbits are dense in it, and
   its cross-sections are Cantor sets, so Lambda != M.
 [HYP] For a hyperbolic basic set of a flow: stable manifold theorem (W^s(O) of a periodic orbit O in Lambda is the
   union of the strong stable leaves W^ss(y), y in O, and d(g_t x, g_t y) <= C e^{-ct} for x in W^ss(y)); any two
   periodic orbits O, O' of Lambda satisfy W^u(O) cap W^s(O') != empty (in the symbolic model take a point whose past
   code is that of O and whose future code is that of O'); periodic orbit measures are weak*-dense in the invariant
   probabilities on Lambda (Sigmund).

Proposition 4.0 (heteroclinic part of Corollary C1, now with full proof). Assume GH, dim M >= 2. Let O1, O2 be
hyperbolic periodic orbits (periods P1, P2) with I1 := int_0^{P1} d(g_s p1) ds > 0 and I2 := int_0^{P2} d(g_s p2) ds < 0.
Then W^u(O1) cap W^s(O2) is empty.
Proof. Let x be in the intersection; x is not a zero, and not periodic (its alpha- and omega-limit sets are the
disjoint orbits O1, O2). Choose y2 in O2 with x in W^ss(y2), so d(g_t x, g_t y2) <= C e^{-ct} for t >= 0; then
|J_t(x) - J_t(y2)| <= Lip(d) C / c for t >= 0, while J_t(y2) = (t/P2) I2 + O(1). So J_t(x) <= b - a t for t >= 0, some a > 0.
Symmetrically, x is in the strong unstable leaf of some y1 in O1, d(g_t x, g_t y1) <= C e^{ct} for t <= 0, and
J_t(y1) = (t/P1) I1 + O(1) for t <= 0 (note J_t = -int_t^0 d o g_s for t < 0), so J_t(x) <= b + a t = b - a|t| for t <= 0.
Hence int_R e^{J_t(x)} dt < infinity, contradicting Lemma C. QED

Theorem 4.1 (proved, modulo [Rue], [KLY], [HYP]). Assume GH, dim M = 3, and h_top(g_1) > 0. Then, after replacing X
by -X if necessary (GH is preserved, (O4)), there are a horseshoe Lambda != M as in [KLY] and a > 0, b such that
 (i) every periodic orbit O in Lambda has int_O d < 0;
 (ii) mu(d) <= -a for every invariant probability mu carried by Lambda; equivalently J_t(x) <= b - (a/2) t for all
     x in Lambda, t >= 0 (Lambda is uniformly volume-contracting);
 (iii) Lambda is not an attractor and its stable set W^s(Lambda) is nu-null;
 (iv) X has periodic orbits; the flow is neither minimal nor uniquely ergodic.
Proof. By the variational principle there is an ergodic mu with h_mu(g_1) > 0. mu gives no mass to the zero set Z
of X (Z is invariant and closed; if mu(Z) > 0 then mu(Z) = 1 and g_1 = id on supp mu, so h_mu = 0). For mu-a.e. x the
exponent in the flow direction is 0 (|Dg_t X(x)| = |X(g_t x)|, and by Poincare recurrence X(g_t x) returns near
X(x) != 0 along a sequence t -> infinity). By [Rue] for g_1 and for g_{-1}, mu has a positive and a negative exponent;
in dimension 3 the exponents are therefore lambda_1 > 0 = lambda_2 > lambda_3, so [KLY] applies and gives Lambda != M.
By [HYP], any two periodic orbits of Lambda are heteroclinically related in both orders, so by Proposition 4.0 and
Observation P (no periodic orbit with int_O d = 0) all int_O d (O in Lambda) have the same strict sign; changing
X to -X changes every int_O d to its negative, so we may assume (i). By Sigmund's density, mu(d) <= 0 for every
invariant mu on Lambda. The maximum of mu -> mu(d) on the compact convex set of invariant probabilities on Lambda is
attained at an extreme point mu0, which is ergodic. If mu0(d) = 0, Corollary D1 gives supp mu0 = M, impossible since
supp mu0 is contained in Lambda != M. So max = -a < 0, and the standard identity
limsup_{t -> inf} max_{x in Lambda} J_t(x)/t = max_{mu on Lambda} mu(d) (weak* limits of empirical measures, as in
Prop. 2.1 of [R4-q7]) gives (ii). (iii): B3 of [R4-q4] (the basin of a proper closed invariant set is nu-null), and
an attractor has a basin with nonempty interior. (iv): Lambda contains periodic orbits; dim M = 3 > 1. QED

Corollary 4.2 (proved, modulo the same citations). Under GH with dim M <= 3, if the flow has no periodic orbit —
in particular if it is uniquely ergodic (Lemma E: then it is minimal) — then h_top(g_1) = 0.
(dim 1: trivial; dim 2: Young's theorem; dim 3: Theorem 4.1(iv).)

Corollary 4.3 (any dimension; proved modulo citations). Assume GH. If mu is an ergodic invariant probability with
h_mu > 0 whose exponents are all nonzero except the flow direction, then the conclusions (i)-(iii) of Theorem 4.1
hold for a horseshoe Lambda (for X or -X). In particular, if GH holds and the flow is uniquely ergodic with
invariant measure mu, then h_top = h_mu and either h_top = 0 or mu is NON-hyperbolic with h_mu > 0, which needs
dim M >= 4 (one positive, one negative, the flow-direction zero, and one more zero exponent).
Proof. Same as Theorem 4.1, using [KLY] directly (hyperbolicity is now assumed). Under unique ergodicity a
horseshoe would carry many invariant measures, so a positive-entropy mu must be non-hyperbolic. QED

So in dimension 3 the problem reduces EXACTLY to excluding the following configuration under GH:
 (H3) a non-attracting horseshoe Lambda != M which is uniformly volume-contracting (J_t <= b - a t on Lambda), all of
 whose periodic orbits are volume-contracting, in a flow which is nu-ergodic and conservative, has dense nu-typical
 orbits, and all of whose ergodic measures with mu(d) = 0 have full support.

## 5. Dead ends of the "manufacture a non-smooth solution from unstable structure" approach (proved statements)
Lemma 5.1 (Jacobian cancellation). Let psi be bounded Borel with compact support, tau: M -> [0, infinity] Borel, and
T(phi) := int_M psi(x) int_0^{tau(x)} e^{J_t(x)} phi(g_t x) dt dnu(x) (whenever absolutely convergent). Then T = u nu with
 u(y) = int_0^infinity psi(g_{-t} y) 1[t < tau(g_{-t} y)] dt,
and, for smooth phi and tau < infinity a.e., T(X phi + d phi) = int psi(x) [e^{J_{tau(x)}(x)} phi(g_{tau(x)} x) - phi(x)] dnu(x).
Proof. Fubini, and the change of variables y = g_t x, dnu(y) = e^{J_t(x)} dnu(x) (J_t is the log nu-Jacobian of g_t);
the second formula integrates d/dt[e^{J_t(x)} phi(g_t x)] = e^{J_t(x)}(X phi + d phi)(g_t x) over [0, tau(x)]. QED
Meaning. Every construction "spread Patterson/conformal weights e^{J_t} over a smooth family of initial points"
(this includes integrating over Pesin unstable disks thickened to open sets, and Abel-regularised forward orbit
integrals with smooth initial densities) produces the function u above: the Jacobian weights cancel exactly.
(a) If tau = infinity identically and psi >= 0, psi != 0 is continuous, then u is not in L^1(nu): by conservativity
(N2, applied to -X) nu-a.e. point of {psi > 2c} returns to it at arbitrarily large negative times, each return
contributes at least c*delta to the integral (delta = dist({psi > 2c}, {psi < c}) / max|X|), so u = infinity a.e. there.
(b) If tau < infinity, the source term in Lemma 5.1 is psi nu minus the "exit distribution"
(g_tau)_*(e^{J_tau} psi nu), which is smooth only if x -> g_{tau(x)} x is smooth on supp psi; then u itself is
smooth wherever this holds. Singularities of u can only come from the set where tau is infinite or non-smooth,
and exactly there the source is singular.
So with smooth sources one never escapes the conservativity/Lemma C dichotomy: a contradiction with GH needs
cancellations (genuinely distributional objects), not positive measures. The only positive-measure objects with
smooth (namely zero) source are the nu-conformal measures, and these are completely controlled by Lemma C /
Corollary D1 — which is exactly what produced Theorem 4.1, and what stops at (H3).
(c) Using the formula in (iii) of the task: if Xu = f with u smooth and y in the strong unstable leaf of x, then
u(x) - u(y) = int_{-inf}^0 (f(g_t x) - f(g_t y)) dt; combined with the dual estimate (O1) this only yields
|int_{-inf}^0 (f(g_t x) - f(g_t y)) dt| <= C d(x,y) ||f||_{C^m} for f in X(C^inf), which is automatically true when
d(g_t x, g_t y) decays exponentially as t -> -inf. Similarly the derivative-loss route: the tame estimate
||u - c||_{C^k} <= C ||Xu||_{C^m} applied to u = int_0^T phi o g_s ds or u o g_t only compares quantities that both
grow like ||Dg_T||^{power}, with the larger power on the right, so it never contradicts exponential growth.
These are the checks behind the statement that I could not turn hyperbolic structure into a GH violation
beyond Theorem 4.1.


[R5-e: GH. Invariant Borel functions; proper hyperbolic basic sets; Anosov flows]
## 4. Two new elementary consequences of GH

**Lemma 4.1 (proved; uses only L1).** Let w be a bounded Borel function with w∘g_s = w ν-a.e. for each s ∈ R. Then w is ν-a.e. constant.

*Proof.*
1. **Change of variables.** Since (g_s)^*ν = e^{J_s}ν, for bounded Borel F we have ∫F dν = ∫ (F∘g_s) e^{J_s} dν. Apply this to F = wψ with ψ smooth and use invariance of w. This gives ∫ wψ dν = ∫ w·Q_sψ dν, where Q_sψ = e^{J_s}·(ψ∘g_s).
2. **Differentiate at s = 0.** (Q_sψ − ψ)/s → Xψ + dψ = Pψ uniformly. Hence ∫ w·Pψ dν = 0 for all smooth ψ.
3. **Conclude.** Step 2 says exactly ⟨Xw, ψν⟩ = 0, i.e. Xw = 0 in D'. By L1, w is a.e. constant. ∎

**Corollary 4.2 (proved).** Under GH, the pointwise top exponent χ(x) = limsup_{t→+∞} (1/t) log ||Dg_t(x)|| is ν-a.e. equal to a constant χ_ν ≤ λ*.

*Proof.* We check the three hypotheses of Lemma 4.1.
- *Bounded:* |log ||Dg_t||| ≤ t·||∇X||_∞ by Grönwall.
- *Borel:* t ↦ log ||Dg_t(x)|| is continuous, so the limsup can be taken over rational t.
- *Invariant:* Dg_t(g_s x) = Dg_s(g_t x)·Dg_{t+s}(x)·Dg_s(x)^{−1}, so log ||Dg_t(g_s x)|| differs from log ||Dg_{t+s}(x)|| by at most 2|s|·||∇X||_∞. Hence χ(g_s x) = χ(x).

The same argument applies to liminf_{t→+∞} J_t/t, limsup_{t→+∞} J_t/t, the backward versions, and every Oseledets-type pointwise quantity. ∎

Remark. If liminf_{t→+∞} J_t/t = c > 0 ν-a.e., then Fatou's lemma would give ∫ e^{J_t} dν → ∞. This contradicts ∫ e^{J_t} dν = ν(M). So that constant is ≤ 0.

**Lemma 4.3 (proved; a corollary of Lemma D).** Assume GH. Let x satisfy limsup_{t→+∞} J_t(x)/t ≤ 0 and limsup_{t→−∞} J_t(x)/|t| ≤ 0. Then the orbit of x is dense in M.

*Proof.* The hypothesis is exactly P(s) < ∞ for all s > 0 in Lemma D. By Lemma D, the probabilities T_s converge weak* to ν/ν(M), which has full support. Each T_s is supported in the orbit closure of x, and that closed set therefore also carries the limit. ∎

Consequently, a proper closed invariant set K contains no point whose forward Jacobian growth rate is ≤ 0 and whose backward Jacobian growth rate, in the sense above, is also ≤ 0.

## 5. Hyperbolic partial results (they rely on cited theorems)

**Proposition 5.1 (proved modulo cited thermodynamic formalism).** Assume GH and dim M ≥ 2. Let Λ ≠ M be a hyperbolic basic set of the flow (compact, invariant, locally maximal, transitive, hyperbolic, not a single orbit). Then one of the following holds:
- max{μ(d) : μ invariant on Λ} < 0, so J_t(x) ≤ b − ct on Λ for t ≥ 0, with c > 0 (uniformly volume-contracting); or
- min{μ(d) : μ invariant on Λ} > 0, so the same holds for −X (uniformly volume-expanding).

*Proof.* Let m_− = min μ(d) and m_+ = max μ(d) over invariant probabilities on Λ. Both are attained, and they are attained at ergodic measures, because the ergodic components of an extremal measure are extremal.
1. **Extreme value 0.** If m_+ = 0 or m_− = 0, there is an ergodic μ on Λ with μ(d) = 0. By Corollary D1, supp μ = M, which contradicts supp μ ⊂ Λ ≠ M.
2. **Strictly mixed signs.** Suppose m_− < 0 < m_+. Cited (Bowen–Ruelle thermodynamic formalism for hyperbolic basic sets of flows): for real q the Hölder potential q·d has a unique equilibrium state μ_q on Λ, which is ergodic. Moreover q ↦ μ_q(d) = P'(q) is continuous, with limits m_± as q → ±∞. By the intermediate value theorem some μ_q(d) = 0. This contradicts Corollary D1 as in step 1.
3. **Uniform rate.** The bound J_t ≤ b − ct on Λ follows from limsup_{t→∞} sup_{x∈Λ} J_t(x)/t = m_+, as in [R4-q7] Prop. 2.1 step 1, applied on Λ. ∎

**Proposition 5.2 (sketch; relies on cited Fredholm theory).** An Anosov flow is not GH.

*Sketch.*
1. **Cited (Butterley–Liverani; Faure–Sjöstrand).** There are anisotropic Sobolev spaces H with C^∞ ⊂ H ⊂ D' continuously, C^∞ dense in H, on which X − s is Fredholm of index 0 for Re s > −c(H). In particular X is Fredholm on H, so its range R is closed and has finite codimension.
2. **Range on smooth functions.** R ∩ C^∞ is the common kernel in C^∞ of finitely many continuous functionals. So it has finite codimension in C^∞.
3. **Periodic obstructions.** The periodic-orbit measures μ_γ are infinitely many linearly independent functionals on C^∞ (periodic orbits are dense and infinitely many). Hence ∩_γ ker μ_γ has infinite codimension. So there are f ∈ R ∩ C^∞ and a periodic orbit γ with μ_γ(f) ≠ 0.
4. **Contradiction with GH.** Write f = Xu with u ∈ H ⊂ D'. If u were smooth, integrating Xu along γ would give μ_γ(f) = 0. So u is not smooth, and X is not GH. ∎

**Corollary 5.3 (dimension 3; conditional on the cited Katok theorem).** Assume dim M = 3, GH and h_top > 0. Cited (Katok's horseshoe theorem for C^{1+α} flows on 3-manifolds; Lian–Young for flows in general dimension with hyperbolic measures): there is a hyperbolic basic set Λ with positive entropy. By Prop. 5.2, Λ ≠ M, since a basic set equal to M makes the flow Anosov. By Prop. 5.1, Λ is uniformly volume-contracting or uniformly volume-expanding. So in dimension 3, a GH flow with positive entropy must contain a strictly dissipative (or strictly anti-dissipative) horseshoe of saddle type.


[R5-f: GH. One-sided compactness (Lemma H) and the relative-entropy criterion for a smooth invariant volume]
## 1. Conventions and two technical lemmas

Conventions are those of the brief. nu is a smooth positive density and nu^ = nu/nu(M). d = div_nu X. J_t(x) = int_0^t d(g_r x) dr, which is smooth in (t,x). The cocycle rule is J_{t+r}(x) = J_r(x) + J_t(g_r x). A distribution u acts by phi -> <u, phi nu>, and <Xu, phi nu> = -<u, (X phi + d phi) nu>. L1 means ker(X on D') = constants.

Change of variables (used throughout): for bounded Borel psi,
 int psi(g_r x) dnu(x) = int psi(y) e^{J_{-r}(y)} dnu(y),
and int e^{J_t} dnu = nu(g_t M) = nu(M).

**Lemma T1 (orbitwise derivative = distributional derivative).** Let a be in L^1(nu), and let w be a bounded Borel function. Suppose there is a g-invariant Borel set Omega of full nu-measure such that, for every x in Omega, t -> a(g_t x) is finite and locally absolutely continuous with derivative w(g_t x) for a.e. t. Then Xa = w in D'.

*Proof.* For x in Omega, a(g_r x) - a(x) = int_0^r w(g_sigma x) dsigma. Multiply by a smooth phi and integrate against nu. By Fubini (w is bounded and (sigma,x) -> w(g_sigma x) is Borel),
 int (a o g_r - a) phi dnu = int_0^r [ int w (phi o g_{-sigma}) e^{J_{-sigma}} dnu ] dsigma.
The bracket is continuous in sigma (dominated convergence), so after dividing by r and letting r -> 0 the right side tends to int w phi dnu. The left side equals int a [ (phi o g_{-r}) e^{J_{-r}} - phi ] dnu. The bracket divided by r converges uniformly to -(X phi + d phi), and a is in L^1. So the left side divided by r tends to -int a (X phi + d phi) dnu = <Xa, phi nu>. ∎

*Chain rule.* Under the hypotheses of T1, a^- = max(-a, 0) satisfies them as well, with w replaced by -1_{a<0} w. Reason: for an absolutely continuous function alpha, alpha^- is absolutely continuous and (alpha^-)' = -1_{alpha<0} alpha' a.e., because alpha' = 0 a.e. on {alpha = 0}. So X(a^-) = -1_{a<0} w in D'.

**Lemma T2 (Cesaro averages of the Koopman flow).** For continuous f put D_T f = (1/T) int_0^T f o g_t dt. Every weak* limit point in L^infinity(nu) = L^1(nu)' of (D_{T_n} f) with T_n -> infinity is an a.e. constant c. The constant is c = lim int D_{T_n} f dnu^.

*Proof.* Let G be such a limit. Then ||(D_T f) o g_r - D_T f||_inf <= 2|r| ||f||_inf / T -> 0. The map h -> h o g_r is weak*-continuous on L^infinity, since it is the adjoint of psi -> (psi o g_{-r}) e^{J_{-r}} on L^1. Hence G o g_r = G a.e. for every r. Therefore int G [ (phi o g_{-r}) e^{J_{-r}} - phi ] dnu = 0. Dividing by r and letting r -> 0 gives -int G (X phi + d phi) dnu = 0, i.e. XG = 0 in D'. By L1, G is constant. ∎

## 2. Lemma H: a one-sided compactness principle

**Lemma H.** Assume GH. Let (a_n) be functions in L^1(nu) satisfying T1 with derivatives w_n. Assume:
 (H1) int a_n^+ dnu <= K for all n;
 (H2) ||w_n||_inf <= K for all n;
 (H3) w_n -> -d + c in D' for some constant c.
Put N_n = int a_n^- dnu. Then:
 (i) if liminf N_n < infinity, then (V) holds;
 (ii) if N_n -> infinity, then (a_n^-/N_n) nu -> nu/nu(M) weak* as measures. That is, int phi a_n^- dnu / N_n -> int phi dnu / nu(M) for every continuous phi.
 (iii) Consequently, if for some nonempty open O we have liminf_n int_O a_n^- dnu < infinity, then (V) holds.

*Proof.* (i) Pass to a subsequence with N_n <= K'. Then ||a_n||_1 <= K + K', so the measures a_n nu have bounded total variation. Extract a further subsequence converging weak* in C(M)' to a signed measure beta, and let b be the distribution <b, phi nu> = beta(phi). Then
 <Xb, phi nu> = -beta(X phi + d phi) = lim -int a_n (X phi + d phi) dnu = lim <X a_n, phi nu> = lim int w_n phi dnu = int (-d + c) phi dnu.
So Xb = -d + c is smooth, and by GH b is smooth. Then L_X(e^b nu) = e^b (Xb + d) nu = c e^b nu. Integrating over M, the left side has integral 0 (the integral of a Lie derivative of a density vanishes), so c = 0 and e^b nu is a smooth positive invariant density. That is (V). (This is (O3).)

(ii) Put u_n = a_n^-/N_n >= 0, so int u_n dnu = 1. By the chain rule and T1, X u_n = -1_{a_n<0} w_n / N_n, which has sup norm at most K/N_n -> 0. Let lambda be any weak* limit point of u_n nu. It is a positive measure with lambda(M) = 1, and
 lambda(X phi + d phi) = lim int u_n (X phi + d phi) dnu = -lim int (X u_n) phi dnu = 0.
By Observation 0 and L1, lambda = nu/nu(M). Every limit point is the same, so the whole sequence converges.

(iii) Pass to a subsequence along which int_O a_n^- dnu stays bounded. If N_n is bounded along a further subsequence, (i) gives (V). Otherwise N_n -> infinity along the subsequence. Take continuous psi with 0 <= psi <= 1, supp psi in O and psi not identically 0. Then int psi u_n dnu <= int_O a_n^- dnu / N_n -> 0. But by (ii) it tends to int psi dnu / nu(M) > 0. Contradiction. ∎

Lemma H is the mechanism of Theorem 1 of [R4-q9], freed from the need for an a priori invariant density. What the earlier proofs needed (log rho in L^1, or rho >= delta on an open set) is replaced by an L^1 bound on the negative part of an approximate solution of Xa = -d.

## 3. Two families, and the resulting criteria for (V)

### 3.1 Family 1: Cesaro-averaged log-Jacobians. Theorem K (relative entropy criterion)

Put Jbar_T = (1/T) int_0^T J_t dt. This is a smooth function. The facts needed are:
- X J_t = d o g_t - d. (Differentiate J_t(g_r x) = J_{t+r}(x) - J_r(x) at r = 0.) Hence X Jbar_T = -d + D_T d, with D_T as in T2, and ||X Jbar_T||_inf <= 2||d||_inf.
- J^+ <= e^J and int e^{J_t} dnu = nu(M). Hence int Jbar_T^+ dnu <= (1/T) int_0^T int J_t^+ dnu dt <= nu(M).
- Relative entropy. (g_t)_* nu has nu-density e^{J_{-t}}, so
 D((g_t)_* nu || nu) = int J_{-t} e^{J_{-t}} dnu = int J_{-t}(g_t x) dnu(x) = -int J_t dnu >= 0.
 In particular -int Jbar_T dnu = (1/T) int_0^T D((g_t)_* nu || nu) dt =: H_T. Also N_T := int Jbar_T^- dnu = H_T + int Jbar_T^+ dnu lies in [H_T, H_T + nu(M)].

**Theorem K (proved; assumes GH).** The following are equivalent:
 (a) (V);
 (b) sup_{t in R} D((g_t)_* nu || nu) < infinity;
 (c) liminf_{T -> infinity} H_T < infinity, i.e. the Cesaro mean of the relative entropy D((g_t)_* nu || nu), t >= 0, does not tend to infinity;
 (d) there are a nonempty open set O and T_n -> infinity with sup_n int_O Jbar_{T_n}^- dnu < infinity.
 A sufficient condition for (d) is sup_n (1/T_n) int_0^{T_n} int_O J_t^- dnu dt < infinity, because x -> x^- is convex.
Moreover, if (V) fails, then H_T -> infinity, and (Jbar_T^- / N_T) nu -> nu/nu(M) as T -> infinity. So the divergence of the relative entropy is spatially homogeneous: on every nonempty open set, Jbar_T -> -infinity in L^1-mean at the same rate as on all of M.

*Proof.*
- (a) => (b): with omega = e^b nu invariant and b smooth, J_t = b - b o g_t, so |J_t| <= 2||b||_inf.
- (b) => (c) and (c) => (d) with O = M: immediate, since N_T <= H_T + nu(M).
- (d) => (a): take the sequence a_n = Jbar_{T_n}, along a subsequence for which D_{T_n} d converges weak* in L^infinity. By T2 the limit is a constant c. Weak* convergence in L^infinity implies convergence in D'. So (H1) to (H3) hold with w_n = -d + D_{T_n} d. Lemma H(iii) gives (V).
- The "moreover" part: if (V) fails, then (c) fails, so H_T -> infinity and N_T -> infinity. Apply Lemma H(ii) along any sequence T_n -> infinity; this needs no convergence of D_T d, since only the sup bound (H2) is used there. ∎

Remarks.
- The same holds with t <= 0, i.e. with D((g_{-t})_* nu || nu). Apply the theorem to -X, which is GH by (O4).
- Theorem K is the "ergodic-average" form of the closed-range question. u_T = -Jbar_T is the Cesaro-regularised candidate solution of Xu = d - c. The theorem says that a one-sided L^1 bound on these candidates, even on a single open set, already forces (V).


[R5-g: GH. Correlation lemma]
## 2. Lemma 2: resolvent/correlation lemma (proved)

**Lemma 2.** Assume GH. Let f be in C^infinity(M). Suppose that for every smooth density sigma the improper integral
U(sigma) := lim_{R->infinity} int_0^R < f o g_t , sigma > dt
exists, where <h, sigma> = int h sigma. Then there is u in C^infinity with Xu = -f and U(sigma) = int u sigma. Consequently:
- mu(f) = 0 for every invariant probability mu;
- sup_{x,t} |int_0^t f(g_s x) ds| <= 2||u||_inf.

*Proof.*
1. **U is a distribution.** U_R(sigma) = int_0^R <f o g_t, sigma> dt satisfies |U_R(sigma)| <= R ||f||_inf ||sigma||_{L^1}, so each U_R is a continuous linear functional on the Fréchet space of smooth densities. By hypothesis U_R converges pointwise to U. By Banach–Steinhaus (a pointwise limit of continuous linear functionals on a Fréchet space is continuous), U is continuous, i.e. a distribution u.
2. **The correlation tends to 0.** Put a(t) = <f o g_t, sigma>. Since d/dt (f o g_t) = X(f o g_t),
a(R) - a(0) = int_0^R int X(f o g_t) sigma dt = - int_0^R <f o g_t, L_X sigma> dt = -U_R(L_X sigma).
The right side converges to -U(L_X sigma), because L_X sigma is a smooth density. So a(R) has a limit A. Since int_0^R a(t) dt converges, A = 0.
3. **Xu = -f.** Letting R -> infinity in step 2 gives U(L_X sigma) = a(0) = <f, sigma>. Hence <Xu, sigma> = -<u, L_X sigma> = -<f, sigma> for every sigma, i.e. Xu = -f.
4. **Consequences.** By GH, u is smooth. For an invariant probability mu, mu(Xu) = d/dt mu(u o g_t)|_{t=0} = 0, so mu(f) = 0. Finally, int_0^t f(g_s x) ds = u(x) - u(g_t x). ∎

**Corollary 3.** Assume GH and dim M >= 2. Suppose there is a Borel probability m such that, for every smooth phi and every smooth density sigma, the improper integral
int_0^infinity ( <phi o g_t, sigma> - m(phi) sigma(M) ) dt
converges. (For example, int |...| dt < infinity, as with exponential or integrable decay of correlations of pushed-forward smooth densities toward a limit measure m.) Then:
- the flow is uniquely ergodic with invariant measure m;
- m(d) = 0, and the flow is minimal;
- in particular it has no zeros and no periodic orbits.

The same conclusion holds with t -> -infinity, by applying it to -X.

*Proof.*
1. Apply Lemma 2 to f = phi - m(phi). The hypothesis holds because <f o g_t, sigma> = <phi o g_t, sigma> - m(phi) sigma(M). So mu(phi) = m(phi) for every invariant probability mu and every smooth phi, hence mu = m.
2. Invariant probabilities exist, so the flow is uniquely ergodic with invariant measure m.
3. Lemma E (established background) then gives m(d) = 0, supp m = M and minimality. A zero would give the invariant measure delta_p, and a periodic orbit (dim >= 2) its orbit measure; either would differ from the fully supported m. ∎

What this excludes: every GH flow with a periodic orbit or zero, together with integrable-rate convergence of smooth densities. For example, it excludes dissipative or conservative Anosov flows that are exponentially mixing for smooth densities; this uses the GH hypothesis only, with no volume needed. It is a partial result for a subclass and does NOT answer the problem. General positive-entropy flows need not have any decay of correlations.


[R5-h: GH. Why the earlier target (Lambda) = 'lim (1/t) log max ||Dg_t|| = 0' was abandoned: it is strictly stronger than zero entropy]
## 1. Proposition 1: what (Lambda) implies under GH (proved)

**Proposition 1.** Assume GH and dim M >= 2. Suppose (Lambda) holds for X. Then:
- (a) J_t(x)/t -> 0 uniformly in x as |t| -> infinity, and mu(d) = 0 for every invariant probability mu.
- (b) X has no zeros.
- (c) X has no periodic orbits.
- (d) Every ergodic invariant probability has support M, and the flow is minimal.

*Proof.* By (O4), -X is GH, so (Lambda) applies to -X as well. Write a(t) = max_y ||Dg_t(y)|| and b(t) = max_y ||Dg_{-t}(y)||. Both are e^{o(t)} as t -> +infinity.

(a) The nu-Jacobian e^{J_t(x)} equals |det Dg_t(x)| (determinant with respect to the Riemannian volume) times a ratio of smooth positive densities at x and g_t x. That ratio is bounded above and below by constants. For an invertible linear map A of n-dimensional Euclidean spaces,
||A^{-1}||^{-n} <= |det A| <= ||A||^n.
For t > 0, Dg_t(x)^{-1} = Dg_{-t}(g_t x), so ||Dg_t(x)^{-1}|| <= b(t). Hence |J_t(x)| <= n log max(a(t), b(t)) + C = o(t) uniformly in x. The case t < 0 follows by symmetry.

For an invariant probability mu, int J_t dmu = int_0^t mu(d o g_s) ds = t mu(d). So mu(d) = (1/t) int J_t dmu -> 0, and mu(d) = 0.

(b) If X(p) = 0, then delta_p is invariant, so by (a) d(p) = 0. This contradicts P1.

(c) If gamma is a periodic orbit of period T, the normalised orbit measure is invariant. By (a), int_0^T d(gamma(t)) dt = 0. This contradicts Observation P (dim >= 2).

(d) Let mu be ergodic. Take x in supp mu that is Birkhoff-generic for d in both time directions; mu-a.e. point qualifies. Then J_t(x)/t -> mu(d) = 0 as t -> +-infinity, so Lemma D applies.
- The measures T_s are carried by the closure of the orbit of x. That closure is contained in supp mu, a closed invariant set.
- Weak* limits of measures supported in a closed set stay supported in it. The limit nu/nu(M) has full support, so supp mu = M.
- Every orbit closure carries an ergodic invariant probability, whose support is M. So every orbit closure is M, and the flow is minimal. ∎

**Consequence for the chain.** To prove (Lambda) one must in particular prove, from GH alone, that GH vector fields have no zeros and are minimal. These are central unsolved points of the whole program (compare the remark after Lemma H: zeros are not excluded by any known argument).

Zero topological entropy implies none of (a)–(d). For example, north–south-type flows have zero entropy, zeros, and mu(d) != 0. So (Lambda) is strictly harder than the problem. A proof of the problem should not route through (Lambda) unless it also proves minimality.


=== END OF RESULTS OF THE MOST RECENT ROUND ===
