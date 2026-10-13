kind: attempt
Open question attempted: statement (V) (ledger entry 19: GH implies a smooth invariant positive density), on a set-aside line of this attempt, in its sharpest open form from the previous round: exclude a 'null-recurrent' half-orbit of the volume cocycle.

## Task
Notation: M compact connected, X smooth and globally hypoelliptic (GH: every distribution u with Xu smooth is smooth), nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (the log nu-Jacobian of g_t at x), dim M >= 2.
**Claim (Z0).** Under GH there is no point z in M with sup_{t>=0} J_t(z) < inf and (1/T) int_0^T e^{J_t(z)} dt -> 0 as T -> inf.
By [R4-q6] Proposition 1, Lemma 3 and Corollary 4 below (proved), (Z0) — applied to X and to -X, which is also GH — is EQUIVALENT to (V): X preserves a smooth positive density. Prove (Z0) (hence (V)), or construct a counterexample (a GH field with such a point; this would also refute the Greenfield-Wallach conjecture, so be critical). A proof for only part of the cases (e.g. uniquely ergodic X, or X without zeros) does NOT answer the question, though it should be reported with full proof if it is all you found.
What the earlier attempts found: every route stops at the same point — GH controls the nu-conformal side (Jacobian-weighted orbit averages converge to nu-hat: Lemma D, Principle G), while invariant measures live on the transposed side; Proposition 1 bridges the two exactly when e^{J} has positive Cesaro density along a half-orbit where J is bounded above. In the remaining case J drifts to -inf in density along such half-orbits without being integrable (local-time-like behaviour). New first moves to try (free to discard): (i) use Lemma C/Principle G for SEGMENTS cut at the times where J_t(z) returns to its running maximum (ladder times), comparing the weighted mass with the number of ladder epochs; (ii) combine with Theorem 1 of [R4-q9] (an a.c. invariant density bounded below on an open set suffices) by producing an a.c. invariant measure from the ladder structure; (iii) a Hopf-ratio / Maharam-extension argument on M x R with the skew flow (x, r) -> (g_t x, r + J_t(x)), where GH gives the conformal uniqueness of [R4-q6] Principle G; (iv) exploit that the same point z must also be handled for the time-changed fields hX (GH is invariant under time change, and the cocycle changes by a coboundary plus a change of clock).
Context: (V) is not by itself the goal of the run (the problem asks for zero topological entropy of the flow); with (V), earlier work proves zero entropy when dim M <= 3 and reduces the general case to one further lemma. The run's main line currently pursues a different statement; this query keeps the (V) line alive.

Deliverable: a complete proof or refutation of (Z0); otherwise the strongest rigorously proved partial result and the exact point where the argument stops. Do not answer by recalling a proof from the literature: reason it out. Everything below the task is material you may use.

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

=== RESULTS OF THE PREVIOUS ROUND (quoted verbatim from the workers' answers). Terms used there: (N1) invariant Borel sets are nu-null or conull under GH; (N2) the flow is conservative under GH (dim >= 2); (N3)/'Lemma B': an a.c. invariant probability rho nu with log rho in L^1(nu) gives (V) (a = log rho satisfies Xa = -d in D', so a is smooth by GH); (O4) GH is preserved by X -> -X and time changes. ===
[R4-q6: Principle G, Proposition 1, Lemma 3, Corollary 4, and where it stops]
**A remark on plan (a) of the brief (a "generalised Lemma C" for families of orbits).** It is vacuous as formulated. Lemma C gives ∫_R e^{J_t(y)} dt = ∞ for **every** y. So any superposition ∫ T_y dτ(y) of orbitwise conformal measures, over any transverse measure τ ≠ 0, has infinite mass. Its hypothesis ("volume Jacobian tending to 0 in both time directions on a set of orbits carrying a finite transverse measure") is never met by any single orbit, so it contains nothing beyond Lemma C. The only usable non-orbitwise mechanism is the limit principle G below. All of its limits equal ν̂, so it cannot detect a second invariant measure unless it is compared with unweighted averages, which is what Proposition 1 does.

## Step 1. New results (proved)

**Principle G (proved; assumes GH).** Let A_n be finite positive Borel measures with A_n(1) > 0 such that ε_n := sup_{‖φ‖_∞ ≤ 1} |A_n(Xφ + dφ)| / A_n(1) → 0. Then A_n/A_n(1) → ν̂ weak*.

*Proof.* The normalised measures are probabilities, so it suffices to identify every weak* limit point T. Xφ + dφ is continuous, so T(Xφ + dφ) = lim A_n(Xφ + dφ)/A_n(1) = 0. Thus T is a conformal probability, and Observation 0 with L1 gives T = ν̂. ∎

For an orbit segment A = ∫_{−R₁}^{R₂} e^{J_t(x)} δ_{g_t x} dt we have the identity A(Xφ + dφ) = e^{J_{R₂}(x)} φ(g_{R₂}x) − e^{J_{−R₁}(x)} φ(g_{−R₁}x). This holds because d/dt [e^{J_t} φ(g_t x)] = e^{J_t}(Xφ + dφ)(g_t x). So **Jacobian-weighted orbit segments whose endpoint weights are small compared with their total mass equidistribute to ν̂.** Lemmas C and D are special cases.

**Proposition 1 (proved; assumes GH).** Suppose some x ∈ M satisfies
 B := sup_{t ≥ 0} J_t(x) < ∞ and a := limsup_{T→∞} (1/T) ∫_0^T e^{J_t(x)} dt > 0.
Then (V) holds. Consequently, under GH:
 **(V) ⇔ there is a point x with sup_{t≥0} |J_t(x)| < ∞.**
In that case every x has sup_{t∈R} |J_t(x)| < ∞. The same holds with t ≤ 0 in place of t ≥ 0, by applying the result to −X, which is GH by (O4); for −X one has J^{−X}_t = J_{−t}.

*Proof.*
1. Choose T_n → ∞ with (1/T_n) ∫_0^{T_n} e^{J_t(x)} dt → a. Passing to a subsequence, we may assume C_n := (1/T_n) ∫_0^{T_n} δ_{g_t x} dt converges weak* to a probability μ'. Since |C_n(φ∘g_r) − C_n(φ)| ≤ 2|r| ‖φ‖_∞ / T_n, μ' is invariant.
2. Put A_n := ∫_0^{T_n} e^{J_t(x)} δ_{g_t x} dt. Then A_n(1) = T_n(a + o(1)) → ∞. By the identity above, |A_n(Xφ + dφ)| ≤ (e^B + 1)‖φ‖_∞. So ε_n → 0, and Principle G gives A_n/A_n(1) → ν̂.
3. Let φ ≥ 0 be continuous. Since e^{J_t(x)} ≤ e^B for t ≥ 0, we have A_n(φ) ≤ e^B T_n C_n(φ). Dividing by A_n(1) and letting n → ∞ gives ν̂(φ) ≤ (e^B/a) μ'(φ). By regularity, μ'(E) ≥ c ν̂(E) for all Borel E, where c = a e^{−B} > 0.
4. Write the Lebesgue decomposition μ' = μ'_ac + μ'_s, with μ'_s concentrated on a ν-null Borel set N. For every Borel E, μ'_ac(E) ≥ μ'(E∖N) ≥ c ν̂(E∖N) = c ν̂(E). So μ'_ac = ρ' ν̂ with ρ' ≥ c a.e.; in particular μ'_ac ≠ 0.
5. Each g_t is a diffeomorphism, so it maps ν-null sets to ν-null sets. Hence (g_t)_* μ'_ac is absolutely continuous and (g_t)_* μ'_s is singular. By uniqueness of the Lebesgue decomposition of (g_t)_* μ' = μ', the measure μ'_ac is invariant.
6. Normalising, ρ = ρ'/μ'_ac(M) is the ν̂-density of an invariant probability, with ρ ≥ c' > 0. Then |log ρ| ≤ |log c'| + ρ, so log ρ ∈ L^1.
7. By Lemma B / (N3), whose proof I re-checked: ρ∘g_t · e^{J_t} = ρ a.e. gives a∘g_t − a = −J_t for a = log ρ. Differentiating the pairing at t = 0 gives Xa = −d in D'. GH makes a smooth, and e^{a}ν is a smooth positive invariant density.
8. For the "consequently": if sup_{t≥0} |J_t(x)| ≤ B, then a ≥ e^{−B} > 0, so the first part applies. Conversely, if ω = e^{a}ν is invariant with a smooth, then J_t = a − a∘g_t, which is bounded by 2‖a‖_∞ everywhere. ∎

**Relation to Lemma E(iii).** Proposition 1 removes the unique-ergodicity hypothesis and the use of Gottschalk–Hedlund. It also explains the mechanism: the conformal limit ν̂ is squeezed below a multiple of an invariant limit μ'.

**Corollary 2 (proved; assumes GH).** If (V) fails, then for every x ∈ M:
- ∫_R e^{J_t(x)} dt = ∞ (Lemma C, dim M ≥ 2);
- either sup_{t≥0} J_t(x) = +∞, or (1/T) ∫_0^T e^{J_t(x)} dt → 0;
- the same dichotomy holds for t ≤ 0;
- in particular, sup_{t≥0} |J_t(x)| = ∞.

*Proof.* The first item is Lemma C. The remaining items are the contrapositive of Proposition 1, applied to X and to −X. ∎

**Lemma 3 (running maxima; proved, no GH needed).** There is a point z and a sign σ ∈ {+1, −1} such that J_{σt}(z) ≤ B for all t ≥ 0, for some finite B. In words: for X or for −X, some forward half-orbit has Jacobian bounded above.

*Proof.*
1. If some x has sup_{t≥0} J_t(x) < ∞, take z = x and σ = +1.
2. Otherwise fix any x. For k ∈ N let t_k be the first time with J_{t_k}(x) = k. Such a time exists by continuity, since J_0 = 0 and sup J = ∞. Then t_k → ∞ and J_{t_k}(x) = max_{[0,t_k]} J_·(x).
3. Put y_k = g_{t_k} x. For s ∈ [−t_k, 0] the cocycle identity gives J_s(y_k) = J_{t_k+s}(x) − J_{t_k}(x) ≤ 0.
4. Let z be a limit point of (y_k). For each fixed s ≤ 0, J_s is continuous in the point, so J_s(z) ≤ 0. Take σ = −1 and B = 0. ∎

**Corollary 4 (proved; assumes GH, dim M ≥ 2).** Suppose (V) fails. Let z, σ be as in Lemma 3, and replace X by σX, which is GH by (O4). Then:
- J_t(z) ≤ B for all t ≥ 0;
- (1/T) ∫_0^T e^{J_t(z)} dt → 0.
Every forward Cesàro limit μ' of the orbit of z then satisfies μ'(d) = lim J_{T_n}(z)/T_n ≤ 0.

*Proof.* The first item is Lemma 3. The second item is Proposition 1 (contrapositive). For the last claim, (1/T_n) J_{T_n}(z) = C_n(d) → μ'(d), and J_{T_n}(z) ≤ B. ∎

(Remark: I could not prove that ∫_0^∞ e^{J_t(z)} dt = ∞. If it were finite, the one-sided measure A = ∫_0^∞ e^{J_t} δ_{g_t z} dt would satisfy A(Xφ + dφ) = −φ(z), i.e. u = A/ν would solve Xu = δ_z/ν (since ⟨Xu, φν⟩ = −A(Xφ + dφ) = φ(z)). The right-hand side is not smooth, so GH gives no contradiction.)

So, if (V) fails, half-orbits with Jacobian bounded above always exist, but along every one of them e^{J_t} has zero Cesàro density, i.e. J_t → −∞ in density. Proposition 1 shows that excluding this "null" behaviour along one half-orbit is all that is needed for (V).

## Step 2. Where the argument stops; dead ends

1. **Patterson weights adapted to running maxima (plan (b)).** Lemma 3 is exactly this construction. It produces half-orbits with J ≤ 0. Principle G then makes the weighted measures converge to ν̂, while the unweighted ones converge to some invariant μ'. The comparison ν̂ ≤ C μ' needs the weighted mass to be a positive fraction of the time. In the remaining case, where J drifts to −∞ in density but is not integrable (local-time-like behaviour, as for a null-recurrent random walk), the weighted mass is o(T). Then the comparison gives only ν̂ ≤ ∞·μ', which is no information.
   - Cutting off the weights does not help. With weights ψ(J_t), the conformal defect is ∫(ψ − ψ')(J_t) d(g_t x) φ dt. For any cutoff it is of the same order as the mass, because exponential weights concentrate their mass at the top of the range.
2. **Plan (a)** is vacuous, as explained at the end of Step 0.
3. **Plan (c).** Transferring uniqueness of conformal measures to uniqueness of invariant ones requires comparing e^{J_t}-weighted and unweighted orbit averages. Proposition 1 does this exactly in the case where it is possible.
4. **An a.c. invariant probability alone does not obviously suffice.** If μ = ρν is invariant with ρ > 0 a.e., Proposition 1 needs ρ bounded below along one half-orbit; Lemma B needs log ρ ∈ L^1. I could not exclude ρ ∈ L^1 with log ρ ∉ L^1. Along μ-generic orbits the weighted limit is automatically (1/ρ)μ normalised, which equals ν̂, so Lemma D gives no information there.

**Open (precisely).** Under GH and dim M ≥ 2, exclude the following: a point z with sup_{t≥0} J_t(z) < ∞ and (1/T)∫_0^T e^{J_t(z)} dt → 0. Equivalently, by Proposition 1 and Lemma 3: show that some half-orbit, for X or −X, has J bounded above and e^{J} of positive upper Cesàro density. This statement is equivalent to (V).

[R4-q9: Theorem 1, Corollary 1', Corollary 2, Theorem 3]
## Preliminary facts (checked)

**(a) Invariant densities.** If ρ ∈ L^1(ν) and ρν is g_t-invariant, then for every t, ρ∘g_{−t} · e^{J_{−t}} = ρ ν-a.e.

*Proof.* Substitute in ∫ φ∘g_t · ρ dν = ∫ φρ dν, using the change of variables (g_{−t})^*ν = e^{J_{−t}}ν. ∎

**(b) Positivity a.e.** By N1 (whose proof works verbatim for sets B with ν(g_tB Δ B) = 0 for all t), such a ρ ≥ 0 with ρ ≢ 0 satisfies ρ > 0 ν-a.e.

**(c) Planner lemmas.** I checked Lemma C, Lemma D and Lemma F of the planner. They are correct as written. In Lemma F, P(ρw) = ρXw + w(Xρ + dρ) = ρXw.

## Theorem 1

**Statement.** Assume GH. Let ρν be an invariant probability with ρ ∈ L^1(ν). Suppose there are δ > 0 and a nonempty open set O with ρ ≥ δ ν-a.e. on O. Then X preserves a smooth positive density, i.e. (V) holds.

**Proof.**

*Step 1: the functions h_s.* For 0 < s ≤ 1, put F_s = ρ^s and h_s = (1 − ρ^s)/s. Then F_s ∈ L^1, because ρ^s ≤ 1 + ρ.

*Step 2: X F_s = −s d F_s in D'.* By (a), F_s∘g_{−t} = F_s · e^{−sJ_{−t}} a.e. Hence, for every smooth φ,
∫ F_s e^{−sJ_{−t}} φ dν = ∫ (F_s∘g_{−t}) φ dν = ∫ F_s (φ∘g_t) e^{J_t} dν.
Differentiate at t = 0. This is legitimate by dominated convergence: F_s ∈ L^1, and the other factors are smooth in (t, x) with t-derivatives bounded uniformly in x for |t| ≤ 1. Using d/dt J_{±t}|_{t=0} = ±d, we get
s ∫ F_s dφ dν = ∫ F_s (Xφ + dφ) dν.
So ⟨X F_s, φν⟩ = −s ∫ d F_s φ dν, i.e. X F_s = −s d F_s. Since X1 = 0, it follows that X h_s = d ρ^s, and
‖X h_s‖_{L^1} ≤ ‖d‖_∞ (ν(M) + ‖ρ‖_1) =: K for all s ∈ (0, 1].

*Step 3: monotonicity and bounds.* The function s ↦ (x^s − 1)/s is nondecreasing on (0, ∞) for each x > 0. With a = log x, its derivative is [e^{sa}(sa − 1) + 1]/s², and e^y(y − 1) + 1 ≥ 0. Hence:
- h_s increases, as s ↓ 0, to −log ρ (a.e., since ρ > 0 a.e.).
- On {ρ ≥ 1}: 0 ≥ h_s ≥ −(ρ − 1). So h_s^− ≤ ρ uniformly in s.
- On {δ ≤ ρ < 1}: 0 < h_s ≤ log(1/δ).
Thus h_s^+ ≤ max(0, log(1/δ)) a.e. on O.

*Step 4: the case where N_s := ∫ h_s^+ dν stays bounded as s ↓ 0.* By monotone convergence (h_s^+ ↑ (−log ρ)^+), we get (log ρ)^− ∈ L^1. Also (log ρ)^+ ≤ ρ ∈ L^1. So log ρ ∈ L^1(ν). By N3 (equivalently Lemma B of R3-q2), the function a = log ρ satisfies Xa = −d in D'. GH makes a smooth, and then e^{a}ν = ρν is a smooth positive invariant density.

*Step 5: the case N_{s_n} → ∞ along some s_n ↓ 0 leads to a contradiction.* Put u_n = h_{s_n}/N_{s_n}.
1. ‖h^−_{s_n}‖_1 ≤ ‖ρ‖_1, so h^−_{s_n}/N_{s_n} → 0 in L^1.
2. The measures λ_n = (h^+_{s_n}/N_{s_n}) ν are positive with mass 1. Pass to a subsequence with λ_n → λ weak*; λ is a positive measure of mass 1. Then u_n → λ/ν in D'.
3. ‖X u_n‖_{L^1} ≤ K/N_{s_n} → 0, so X(λ/ν) = 0 in D', because X is continuous on D'.
4. By L1, λ/ν is constant, so λ = ν̂.
5. Choose a continuous ψ with 0 ≤ ψ ≤ 1, supp ψ ⊂ O and ψ ≢ 0. Then ν̂(ψ) > 0.
6. By Step 3, λ_n(ψ) ≤ ν(M) · max(0, log(1/δ)) / N_{s_n} → 0. This contradicts λ_n(ψ) → ν̂(ψ) > 0. ∎

**Remark.** Theorem 1 strengthens R3-q1 §2(a) and the planner's S8. Neither ρ bounded below everywhere nor ρ^{−ε} ∈ L^1 is needed; a positive lower bound on one open set suffices.

**Corollary 1'.** Assume GH. If there is a continuous ρ ≢ 0 such that ρν is a (signed) invariant measure, then (V) holds.

*Proof.* Invariance gives ρ∘g_t · e^{J_t} = ρ a.e., hence everywhere by continuity. So the open sets {ρ > 0} and {ρ < 0} are invariant. By N1 each is null or conull; they cannot both be conull, and ρ ≢ 0 is continuous, so they cannot both be null. Replacing ρ by −ρ if necessary, ρ ≥ 0 a.e., hence everywhere. Normalise ρν to a probability and take O = {ρ > δ}, which is nonempty for small δ > 0. Theorem 1 applies. ∎

## Corollary 2: line (1) of the brief completed

**Statement.** Assume GH. Then (V) holds if and only if P(C^∞) is closed in C^∞, where P = X + d acts on C^∞. Moreover:
- since the annihilator of P(C^∞) is {u ∈ D' : Xu = 0} = R·1 (by L1), closedness of P(C^∞) is equivalent to P(C^∞) = {f ∈ C^∞ : ∫ f dν = 0};
- by Lemma F, (V') is equivalent to each of these conditions as well.

**Proof.**

(⇒) If ρν is a smooth positive invariant density, then Xρ = −dρ and P(ρw) = ρXw. So P(C^∞) = ρ · X(C^∞), which is closed by Text A/B.

(⇐)
1. *Closed range theorem* (Fréchet spaces, cited): for a continuous linear map T between Fréchet spaces, T has closed range if and only if the transpose T' has weak*-closed range, and then range T' = (ker T)^⊥.
2. *The transpose of P.* Identify distribution densities with distributions via ν. For u ∈ D', ⟨uν, Pφ⟩ = ⟨u, (Xφ + dφ)ν⟩ = −⟨Xu, φν⟩, so P' = −X on D'.
3. *ker P ∩ C^∞ is nonzero.* If it were {0}, then X(D') = D', so Xu = 1 for some u ∈ D'. GH makes u smooth, but Xu = 0 at a maximum point of u. This is a contradiction.
4. *Conclusion.* Take a smooth ρ ≢ 0 with Pρ = 0. Then L_X(ρν) = (Pρ)ν = 0, so ρν is a signed smooth invariant density. Corollary 1' gives (V). ∎

So the planner's line (1) is now correct and complete: the only missing input is that P has closed range on C^∞.

## Theorem 3: bounded volume distortion along one orbit

**Statement.** Assume GH. Then (V) holds if and only if there exist x ∈ M and B < ∞ with |J_t(x)| ≤ B for all t ≥ 0. Changing ν changes J by a bounded coboundary, so the condition is independent of ν.

**Proof.**

(⇒) If ρν is smooth, positive and invariant, then J_t = log ρ − log ρ∘g_t, which is bounded for all x and t.

(⇐)
1. *Weighted averages.* For s > 0 put c_s(t) = e^{J_t(x) − st} for t ≥ 0, P(s) = ∫_0^∞ c_s dt, and T_s(φ) = P(s)^{−1} ∫_0^∞ c_s(t) φ(g_t x) dt. Since e^{−B}/s ≤ P(s) ≤ e^{B}/s, P(s) → ∞ as s ↓ 0.
2. *Near-conformality.* Integrate d/dt [c_s(t) φ(g_t x)] = c_s · [(Xφ + dφ)(g_t x) − s φ(g_t x)] over [0, ∞); this is legitimate because c_s decays exponentially. It gives
T_s(Xφ + dφ) = (−φ(x) + s ∫_0^∞ c_s φ(g_t x) dt) / P(s),
which is bounded in absolute value by ‖φ‖_∞ (1/P(s) + s) → 0.
3. *Limit of T_s.* Every weak* limit T of the T_s is a probability with T(Xφ + dφ) = 0 for all φ. By Observation 0 and L1, T = ν̂. So T_s → ν̂.
4. *Unweighted averages.* Let A_s(φ) = s ∫_0^∞ e^{−st} φ(g_t x) dt. Every weak* limit μ of A_s is invariant, because A_s(Xφ) = s(−φ(x) + s ∫_0^∞ e^{−st} φ(g_t x) dt) → 0.
5. *Comparison.* For φ ≥ 0, e^{−2B} A_s(φ) ≤ T_s(φ) ≤ e^{2B} A_s(φ).
6. *Conclusion.* Along a common subsequence, e^{−2B} μ ≤ ν̂ ≤ e^{2B} μ as Borel measures (by regularity). So μ = ρν with ρ bounded between two positive constants. Theorem 1 with O = M (or directly N3, since log ρ is bounded) gives (V). ∎
=== END OF RESULTS ===
