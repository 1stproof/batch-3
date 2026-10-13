kind: attempt
Open question attempted: the missing statement (JC) of this attempt's chain (ledger entry 101), by a named approach not yet tried: MICROLOCAL / SEMICLASSICAL analysis of Jordan chains at points c of the strip with |Im c| large.

## Task
Prove the statement (JC) below (or the stronger (NJ): no c with Re c != 0 carries an order-1 Jordan chain), or give a counterexample, by the following approach — you may depart from it if you say why.
Approach. By Theorem A (block R9-b §7, ledger entry 92) it suffices to find, in each strip a < Re c < b with 0 not in [a, b], ONE point c carrying no order-1 Jordan chain, and c may be chosen anywhere in the strip — in particular c = sigma + i y with y -> +infinity. In generalized-function form a chain is u, v in D'(M) of order <= 1, u != 0, with (X + c) u = 0 and (X + c) v = -u. Ideas to develop:
 (1) Wavefront sets: WF(u), WF(v) lie in the characteristic set {xi(X) = 0} of T*M \ 0 and are invariant under the symplectic lift of the flow (propagation of singularities for the first-order operator X + c). Use GH (global hypoellipticity of X, equivalently of X + q for q in X(C^inf)) to constrain what invariant closed conic subsets of {xi(X) = 0} can carry wavefront sets of solutions of (X + c)u = 0 when Re c != 0 — e.g. radial source/sink estimates (Dyatlov-Zworski style) in which the threshold condition involves Re c and the expansion rates of the lifted flow on the fibres; GH might force every invariant conic set to be of "neutral" type, where such estimates give regularity, and then u smooth would contradict the maximum principle (a smooth u with Xu = -c u, Re c != 0, vanishes: X|u|^2 = -2 Re c |u|^2 at a maximum).
 (2) Semiclassical limit: for chains at c_y = sigma + i y, rescale h = 1/y; semiclassical defect measures of normalised u_y live on {xi(X) = -1} and are transported by the lifted flow with damping 2 sigma - (divergence terms); try to show that GH forbids such measures for a sequence y -> infinity, which by Theorem A (applied at c = c_y for one y) would settle the strip.
 (3) Any other way to make GH act at a point c with Re c != 0, e.g. showing that a chain at c with large |Im c| would yield, by a construction you specify, a nonsmooth distribution w with Xw smooth.
Known background (blocks R8-b Remark 3.3, R9-g (D7)): hypoellipticity of P - z for small real z != 0 would essentially contain the conclusion, so the approach must not assume it; smooth eigenfunctions at Re c != 0 are excluded by the maximum principle; isolated eigen-densities at Re c != 0 exist in general (tilted conformal measures at c = mu(d)), so the argument must use the chain (length 2) or the freedom in c.
A proof for only part of the cases (only order 0, only volume-preserving fields, only some strips) does NOT answer the question, though it should be reported with full proof if it is all that was found. Deliverable: a complete proof of (JC) or (NJ) (or directly of zero topological entropy), or a counterexample; otherwise the strongest rigorously proved partial result and the exact point where the argument stops. Standard theorems may be cited by name; say exactly which statement you use. Write your plan and partial results into your answer as you go.

**Missing statement (JC).** Let M be a compact connected smooth manifold and X a smooth vector field on M such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Fix a smooth positive density nu on M, put d = div_nu X and P phi = X phi + d phi for phi in C^inf(M) (so that L_X(phi nu) = (P phi) nu). Say that a complex number c *carries an order-1 Jordan chain* if there are continuous linear functionals A, B : C^1(M) -> C (complex distribution densities of order <= 1) with B != 0 such that
  B(P phi) = c B(phi)   and   A(P phi) = c A(phi) + B(phi)   for all phi in C^inf(M).
Then for every pair of real numbers a < b there is a complex number c with a < Re c < b that carries no order-1 Jordan chain.
(Remarks. The statement does not depend on nu: replacing nu by e^w nu conjugates P by multiplication by e^w and maps chains to chains. In terms of generalized functions u = B/nu, v = A/nu the chain reads Xu = -c u, Xv = -c v - u, u != 0. If a < 0 < b the point c = 0 works: B o P = 0 forces B = const nu by (K0) "ker X on D' = constants", and then A o P = const nu forces const = 0 by (K1) "no distribution w has Xw = 1". So the content is the strips not containing 0. It would suffice to prove the cleaner, formally stronger statement (NJ): no c with Re c != 0 carries an order-1 Jordan chain. Isolated eigen-densities at Re c != 0 are NOT excluded and do occur, e.g. tilted conformal measures at c = mu(d); the statement concerns chains of length 2.)

=== WHAT (JC) IS FOR: THE CHAIN OF THIS ATTEMPT ===
The problem asks to show that a globally hypoelliptic (GH) vector field has a flow of zero topological entropy ("[GOAL]" below means exactly that claim). Dictionary for ledger entries cited, all quoted with proofs in the material below: entry 91 = the repaired Theorem R (Theorem R') together with the variational step and the derivation check (block R9-a, from round9_q10); entry 82 = Theorem R in its original form (block R8-a); entry 92 = Theorem A (block R9-b, section 7, from round9_q3); entry 94 = Lemma 1.1 / Corollary 1.2 (block R9-c); entry 95 = Proposition T (block R9-d); entry 56 = Theorem J (block R6-a, §2; holomorphic/meromorphic form = Lemma M, block R6-b); Lemma 6.0 = block R6-a §6 (re-checked in R9-a §2); (K0), (K1), (F1), (F2), L1, Lemma C = background and blocks R6-a, R7-b; entry 90 = the statement (EF) (defined in the header of the round-9 block).

**Chain.**
1. (Variational step; ledger entry 91 = round9_q10 §3, classical.) If h_top(g_1) > 0 then there is a g_1-invariant, g_1-ergodic Borel probability nu' with h_nu'(g_1) > 0 (variational principle for the homeomorphism g_1, then Jacobs' formula over the g_1-ergodic decomposition).
2. (Ledger entry 82 = Theorem R, in the repaired form Theorem R' of entry 91 = round9_q10 §1; GH not used; cites Ruelle's inequality, Pesin local unstable manifolds, the Ledrappier-Strelcyn/Young subordinate partition, Lemma 6.0.) For such nu', with lambda = nu'(J_1), chi = smallest positive exponent, 0 < theta < chi and 0 < delta < theta/4, there is a family (T_z) on the strip Omega = {lambda + delta < Re z < lambda + theta - delta} of continuous linear functionals on C^1(M) with (i) z -> T_z(phi) holomorphic, (ii) sup of |T_z(phi)| over closed substrips and ||phi||_{C^1} <= 1 finite, (iii) T_z(P phi) = z T_z(phi); and T_z != 0 off a discrete set.
3. (Ledger entry 92 = Theorem A of round9_q3 §7, with k = 1; GH not used.) If some single point c of Omega carries no order-1 Jordan chain, every family with (i)-(iii) on Omega vanishes identically.
4. (Missing statement (JC), applied with a = lambda + delta, b = lambda + theta - delta.) Under GH such a point c exists. So the family of step 2 vanishes, contradicting its non-vanishing; hence no g_1-ergodic measure has positive entropy and by step 1 h_top(g_1) = 0: the [GOAL]. (dim M = 1 is trivial; steps 1-3 need neither entry 60 nor Katok/Lian-Young; strips containing 0 are covered by c = 0 inside (JC) itself.)
Note: (JC) is formally stronger than (EF) (entry 90: (JC) => (EF) by Theorem A), but nearly equivalent: a failure of (EF) on a strip puts an order-1 chain at EVERY point of it (round9_q3 Cor 7.2). Steps 1-2 were separately checked by round9_q10 (and re-read by round9_q2, q3, q7); step 3 has not had a separate check.

If you think the chain is flawed (for instance that Theorem R', Theorem A or step 1 does not hold as stated, or that (JC) does not deliver the hypothesis Theorem A needs), say so explicitly. A direct proof of zero topological entropy by any route fully answers the task.
History in one paragraph: earlier chains went through (V) "GH implies a smooth invariant volume" (open), (Lambda) (abandoned as strictly stronger than the goal), and (PE-NH) "no non-hyperbolic ergodic measure of positive entropy" (attacked by twenty-one workers without success; set aside, not refuted). Round 6 found Theorem J (no nonzero distribution whose weighted transport decays exponentially in both time directions; equivalently no holomorphic eigen-family through z = 0), which excluded all hyperbolic positive-entropy measures and solved dim M <= 3. Round 8 found Theorem R (every positive-entropy ergodic measure yields a holomorphic order-1 eigen-family of P^T on a vertical strip), and round 9 attacked the resulting statement (EF) "no such family under GH" with eight workers: no proof, no counterexample, but Theorem A (one point of the strip free of Jordan chains suffices), the order-0 dissipativity lemma, the tensor trick, and proofs that several mechanisms (Leibniz coupling, positivity of moduli, horizontal multipliers, forward divisibility by P) carry no information. Every known use of GH acts at the single spectral point 0, through (K0) "Xu = 0 => u constant" and (K1) "no u with Xu = 1"; the tame closed-range half of GH acts on the weighted operator only when a smooth invariant volume exists. A proof of (JC) must therefore make GH act at some point c with Re c != 0 — e.g. by showing that a Jordan chain there would produce, by some construction, an object to which (K0)/(K1)/GH at 0 applies.
=== END OF CHAIN ===

=== A SUGGESTION (the planner's own sketch for (JC); you are free to discard it) ===
(File names in the chain and in this suggestion map to the blocks of the material: round9_q10 = R9-a, round9_q3 = R9-b, round9_q1 = R9-c, round9_q5 = R9-d, round9_q8 = R9-e, round9_q6 = R9-f, round9_q2 = R9-g, round9_q7 = R9-h; round8_q3 = R8-a, round8_q5 = R8-b, round6_q1 = R6-a; Lemma K = R6-a §3; Lemma C = background Lemmas C-F.)

**Why it should hold (planner sketch, new in round 10).**
(0) Evidence: for Diophantine linear flows (the only known GH fields) there are no eigen-densities at all off iR; volume-preserving fields have no order-0 chains anywhere (round9_q3 Cor 7.4); under GH an order-0 chain at Re c = kappa lives on orbits with int_R e^{J_t - kappa t} dt < inf (entry 94), a nu-null set.
(1) Mechanism: order reduction plus a tilted Lemma C. (a) Order 0. By entry 94, (JC) for order-0 chains (indeed (NJ) at order 0) follows from the statement (SO) "under GH, for every x in M and every real kappa != 0, int_R e^{J_t(x) - kappa t} dt = infinity" — the tilted form of Lemma C (kappa = 0, proved: the orbit measure would be P-harmonic, hence a multiple of nu by (F1), impossible for an orbit). Dynamically (SO) says: no orbit has backward divergence rate strictly above its forward rate (uniformly); this is consistent with Lemma K's corollary that connections between hyperbolic periodic orbits go from int d < 0 to int d > 0. Note (SO) <= (J2): delta_x (x) delta_x decays two-sided under Gamma_t (x) Gamma_{-t} for such x. (b) Order 1. Lift to the 1-jet bundle E = R + T*M, on which Gamma_t acts as a linear cocycle over g_t; an order-1 chain is an order-0 chain of the lifted transfer operator restricted to 1-jets. The step to make rigorous is an EQUIVARIANT measure representation of A and B on E (Hahn-Banach extensions are not canonical — round9_q2 (D5)); then Lemma 1.1 of round9_q1 puts |B-hat| on lifted orbits with int e^{J_t - kappa t} |covector transported| dt < inf, and one needs the jet analogue of (SO), where GH must enter through the Theorem-J machinery at 0 rather than directly. (c) Free choice of c: Theorem A allows c anywhere in the strip, e.g. |Im c| -> infinity (semiclassical limit of chains: defect measures on {xi(X) = -1} transported by the symplectic lift with real damping Re c), or Re c where the growth criterion of Prop 7.3 is closest to applying.
I cannot close (a) or (b); (SO) is the cleanest new GH question in the sketch.

**Tried so far** (on (JC) and its earlier, equivalent or stronger wordings (EF) [#90], (J1) [#81], (E1) [#38], (E1-int); the 21 queries on the retired (PE-NH) are listed under 'Set aside'):
- round4_q10: (E1) from conformal measures on the unit sphere bundle; reduction only.
- round5_q5: (E1) for L^1 eigenfunctions proved; measure solutions nu-singular.
- round5_q6: (no GH) lambda* > 0 gives real eigen-distributions — any proof must use GH.
- round6_q1, q2, q3, q6, q10: Theorem J / Lemma M — families through z = 0 excluded (the c = 0 case of (JC)).
- round7_q7: volume case Lemma H / Theorem V (needs quasi-analytic vectors of X^{-1}); Prop O.
- round8_q5: (J1) <=> strip families (Thm 2.1); empty-interior criteria (Props 3.1-3.2); obstruction Remark 3.3.
- round8_q2, q3, q4, q6: dual tame bounds non-quasi-analytic; Lemma Q; Patterson asymptotics at 0; weighted/unweighted dichotomy.
- round9_q1, q2, q3, q5 (closing task on (EF)): q1 order-0 chains -> total dissipativity (#94), product form (N2); q2 positivity vacuous, Leibniz information-free (#98), band lemma; q3 Theorem A (#92, the basis of (JC)), (J1-0) equivalence, Lemma 3, growth criterion Prop 7.3; q5 tensor trick (#95), (J2)/(SS_Y).
- round9_q4 (refute (EF)): no counterexample; every template is Diophantine-type or not GH.
- round9_q6 (strips touching 0): continuation modulo C nu (Prop 1), quasi-analytic two-sided convergence (#97), sectorial flatness insufficient.
- round9_q7 (Leibniz approach (B)): dead in all forms (#98).
- round9_q8 (obstruction "GH only at 0"): Prop A, Theorem B (#96); no model counterexample.
=== END OF SUGGESTION ===

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

=== RESULTS OF ROUND 8 (quoted verbatim from the workers' answers; each labelled with its source; 'the brief' inside them refers to the round-8 task, whose material is the blocks above; 'R6-a', 'R7-d' etc. refer to the blocks above; '(J1)' there is: under GH no nonzero distribution density S with |S(e^{J_t} phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k} for t <= 0 and <= C e^{a t} ||phi||_{C^k} for t >= 0, 0 <= a < eps; 'Text A/Text B', '(O2)', '(O3)', '(O4)', '(F1)', '(F2)', 'L1' refer to the background above) ===

[R8-a: round8_q3 Sections 1-2. Theorem R (every positive-entropy ergodic measure gives a holomorphic eigen-family on a strip; no GH) and Lemma Q (volume case)]
## 1. Theorem R (reduction of the problem to "no interval of real eigenvalues")

**Definition.** Sigma := { kappa in R : there is a nonzero distribution density T of order <= 1 (T in (C^1)', complex-valued allowed) with T(P phi) = kappa T(phi) for all smooth phi }.

Equivalently, kappa is in Sigma iff some nonzero u in D' of order <= 1 has Xu = -kappa u (Observation 0).

Remarks:
- 0 is always in Sigma (T = nu).
- Every ergodic mu contributes mu(d) to Sigma (Prop. 2.2 of R4-q7).
- For a Diophantine linear flow on T^n (nu = Lebesgue, so P = X) we have Sigma = {0}. Indeed, testing on e_k gives (i k.alpha - kappa) T(e_k) = 0.

**Theorem R.** Let X be any smooth vector field on a compact manifold; GH is not used. Let mu be an ergodic flow-invariant probability with h_mu(g_1) > 0. Then Sigma contains a nonempty open interval.

**Corollary R1.** Suppose (E1-int) holds: under GH, Sigma has empty interior. Then every GH vector field has a flow of zero topological entropy.
*Proof.* Theorem R gives h_mu(g_1) = 0 for every ergodic flow-invariant mu. Then apply step 4 of the chain (variational principle plus flow-ergodic decomposition). ∎

*Proof of Theorem R.*
1. *Exponents.* h_mu(g_{-1}) = h_mu(g_1) > 0. Ruelle's inequality for g_1 and for g_{-1} gives that mu has a positive exponent and a negative exponent. Let chi := chi^+_min > 0 be the smallest positive exponent and lambda := mu(d). Fix theta with 0 < theta < chi and delta with 0 < delta < theta/4.
2. *A generic pair on one unstable leaf.* Let G be the set of z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf. By Birkhoff, mu(G) = 1. We use [P], [LY] and Lemma 6.0 of R6-a for the C^inf diffeomorphism g_1. These say that, for mu-a.e. x, the unstable conditional mu^xi_x is non-atomic and carried by G. So we may pick x in G and y in G ∩ xi(x) with y != x.
   By [P], d(g_{-m}x, g_{-m}y) <= C e^{-(chi - delta')m} for integers m >= 0. Interpolating with the Lipschitz constants of g_{-s}, s in [0,1], gives d(g_t x, g_t y) <= C_0 e^{-theta|t|} for all t <= 0 (choose delta' with chi - delta' > theta).
3. *Constants.* For t <= 0, J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds, and the integrand is O(e^{-theta|s|}). So b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists and |J_t(x) - J_t(y) - b| <= K e^{-theta|t|}. Since x, y are in G, there is C_1 with
   J_t(x), J_t(y) <= C_1 + (lambda + delta) t for t >= 0, and J_t(x) <= C_1 + (-lambda + delta)|t| for t <= 0.
4. *Bounds.* Put S := delta_x - e^b delta_y, so that F_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y).
   - For t >= 0: |F_phi(t)| <= (1 + e^b) e^{C_1} e^{(lambda+delta)t} ||phi||_inf.
   - For t <= 0: |F_phi(t)| <= e^{J_t(x)} ( |phi(g_t x) - phi(g_t y)| + |1 - e^{b + J_t(y) - J_t(x)}| ||phi||_inf ) <= C_2 e^{-(theta + lambda - delta)|t|} ||phi||_{C^1}.
   This uses |1 - e^{-r}| <= |r| e^{|r|} and |r| <= K e^{-theta|t|}.
5. *Laplace family.* Let Omega := { z : lambda + delta < Re z < lambda + theta - delta }, which is nonempty since theta > 2 delta. For z in Omega put T_z(phi) := int_R e^{-zt} F_phi(t) dt.
   - The integral converges absolutely and locally uniformly in z: the exponents are -(Re z - lambda - delta)t for t >= 0 and (Re z - theta - lambda + delta)|t| for t <= 0, and both are negative.
   - So T_z is a distribution density of order <= 1, with |T_z(phi)| <= C(z) ||phi||_{C^1} and C(z) locally bounded. For each phi, z -> T_z(phi) is holomorphic on Omega.
6. *Eigen-relation.* t -> e^{J_t} phi o g_t is C^1 into C^inf with derivative e^{J_t} (P phi) o g_t (Theorem J, step 1). So F_phi' = F_{P phi}. Integrate by parts on [-R, R]:
   int e^{-zt} F_{P phi} dt = [e^{-zt} F_phi]_{-R}^{R} + z int e^{-zt} F_phi dt.
   By the bounds of step 4 for phi and for P phi, the boundary terms tend to 0 and the integrals converge. So T_z(P phi) = z T_z(phi).
7. *Non-vanishing.* Choose smooth phi_0 with phi_0(x) = 1 and phi_0(y) = 0. Then F_{phi_0}(0) = 1. Fix a real kappa_0 in Omega. Then G(t) := e^{-kappa_0 t} F_{phi_0}(t) is continuous, lies in L^1, and has G(0) = 1. Its Fourier transform is omega -> T_{kappa_0 + i omega}(phi_0). By Fourier uniqueness this transform is not identically 0, so the holomorphic function z -> T_z(phi_0) is not identically 0 on Omega. Hence its zero set D on the real segment I := Omega ∩ R is discrete and closed in I.
8. For kappa in I \ D, T_kappa is a nonzero distribution density of order <= 1 with T_kappa(P phi) = kappa T_kappa(phi), i.e. kappa is in Sigma. Finally, I \ D is a nonempty open set. ∎

**Remarks on Theorem R.**
1. Compared with Theorem J and Lemma M, the GH-part is now a single global spectral statement. The geometry of mu (zero exponents, the value of mu(d), dimension) has disappeared. The only dynamical input is one exponentially backward-asymptotic pair of forward-generic points, which positive entropy provides.
2. (E1-int) is weaker than (E1) of R4-q10. (E1) excludes every real nonzero eigenvalue; (E1-int) excludes only intervals. (E1) is in fact false in general unless GH also forces mu(d) = 0 for all mu, because mu(d) is in Sigma. (E1-int) is compatible with countably many real eigenvalues, so it does not conflict with possible zeros (d(p) is in Sigma) or with measures having mu(d) != 0.
3. With the same proof one can restrict Sigma to eigen-distributions whose Laplace-in-kappa family is holomorphic. So it suffices to exclude *holomorphic* families kappa -> T_kappa of nonzero order-1 eigen-distributions on a real interval. This is the precise form of the planner's (J1). Lemma M excludes such families exactly when the interval reaches 0 from both sides (or meromorphically).
4. Sanity check (north-south flow on S^2, not GH; heuristic, not used). For a single source-to-sink orbit, the weighted Laplace transform int e^{-zt} e^{J_t(y)} phi(g_t y) dt converges on the strip d(S) < Re z < d(N) (sink S with d(S) < 0, source N with d(N) > 0). By the same argument as steps 5-8, Sigma then contains an interval minus a discrete set. So intervals in Sigma do occur for non-GH fields, consistent with Theorem R not using GH.

## 2. Lemma Q (volume case: what the closed-range half of GH gives for eigen-distributions)
Assume GH and that X preserves a smooth positive density omega. Take nu = omega, so d = 0 and P = X.

**Lemma Q.** For every k there are m = m(k) and C_k such that every distribution density T in (C^k)' with T o X = kappa T, where kappa != 0 is complex, satisfies T(1) = 0 and
||T||_{(C^m)'} <= 2 C_k |kappa| ||T||_{(C^k)'}.
Iterating along k_0 = k, k_{j+1} = m(k_j) gives ||T||_{(C^{k_N})'} <= (prod_{j<N} 2C_{k_j}) |kappa|^N ||T||_{(C^k)'}.

*Proof.*
1. kappa T(1) = T(X1) = 0, so T(1) = 0.
2. By Lemma B(iii) of R7-d (tame dual solvability) there is S in (C^m)' with S o X = T and ||S|| <= C_k ||T||.
3. Then (S - T/kappa) o X = 0, so S - T/kappa is an invariant distribution density. By (O2) it equals c omega.
4. Evaluating at 1 gives S(1) = c omega(M), so |c| omega(M) <= ||S||_{(C^m)'}. Also ||omega||_{(C^m)'} <= omega(M).
5. Hence ||T/kappa||_{(C^m)'} <= ||S|| + |c| omega(M) <= 2||S||. ∎

**Why it stops.** Apply Lemma Q to the family T_z of Theorem R with lambda = 0, whose (C^1)'-norm is O(1/Re z) near the left edge. It gives |T_z(phi)| <= A_N(phi) |z|^N / Re z with A_N(phi) = (prod_{j<N} 2C_{k_j}) C ||phi||_{C^{k_N}}. This is Theorem V/Lemma H of R7-e in dual form: a contradiction needs the Carleman condition sum A_N^{-1/N} = inf for a C^1-dense set of phi.
- GH (closed graph theorem) gives no control on the growth of C_k or of the losses m(k) - k.
- Even with a fixed loss sigma and constants C_k <= B^k, the product is about B^{sigma N^2/2}, which is super-geometric. So no choice of phi (not even Laplace eigenfunctions, which have ||phi||_{C^j} of geometric growth) satisfies Carleman.

So the closed-range half of GH, used through tame constants alone, cannot give (E1-int) unless one has a uniform-loss, geometric-constant tame estimate. I could not derive such an estimate from GH; for Diophantine flows it holds (Fourier multiplier |k.alpha|^{-1} <= C|k|^tau, uniform in s).


[R8-b: round8_q5 Sections 1-5. Eigen-families on strips; equivalence with (J1); spectral sufficient conditions; the obstruction of Remark 3.3; models]
## 1. Definitions

**Eigen-family (EF) on a strip.** Let a < b. An EF on Sigma(a,b) = {a < Re z < b} is a family of distribution densities
T_z, z in Sigma(a,b), such that
 (E1) z -> T_z(phi) is holomorphic on Sigma(a,b) for every smooth phi;
 (E2) T_z(P phi) = z T_z(phi) for all phi, z;
 (E3) for every closed substrip a < a1 <= Re z <= b1 < b there are k, N, C with |T_z(phi)| <= C (1+|z|)^N ||phi||_{C^k}.
It is *nonzero* if T_z != 0 for some z.

Lemma 1.1 (no GH). If T_z is a distribution density with T_z∘P = z T_z, then T_z(Gamma_t phi) = e^{zt} T_z(phi)
for all real t.
Proof. h(t) := T_z(Gamma_t phi) is C^1 with h'(t) = T_z(Gamma_t P phi) = T_z(P Gamma_t phi) = z h(t). ∎

In terms of generalized functions (Observation 0), t_z := T_z/nu satisfies X t_z = -z t_z: an EF is a holomorphic
family of eigen-distributions of X with eigenvalues -z filling a strip.

## 2. Theorem 2.1 (equivalence; proved; no GH needed)

Let X be any smooth vector field on a compact manifold.
(A) Let S be a distribution density, k, C, and real a < eps with |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} (t <= 0),
 |F_phi(t)| <= C e^{a t} ||phi||_{C^k} (t >= 0) [the hypothesis of (J1), here without requiring a >= 0].
 Then T_z(phi) := int_R e^{-zt} F_phi(t) dt is an EF on Sigma(a, eps), and if this EF is zero then S = 0.
(B) Conversely, if T is a nonzero EF on Sigma(a,b) and a < a' < b' < b, there is a nonzero distribution density S
 (complex; its real or imaginary part is a nonzero real one) satisfying the hypothesis of (A) with (a, eps) = (a', b').
Consequently:
 **(J1) holds for X  <=>  X has no nonzero EF on any strip Sigma(a,b) with 0 <= a < b.**
(=>: an EF on Sigma(a,b), a >= 0, gives by (B) a nonzero S with 0 <= a < a' < b' = eps, contradicting (J1).
 <=: given S as in (J1), (A) gives an EF on Sigma(a,eps), a >= 0, which must be zero, so S = 0.)

*Proof of (A).*
1. Holomorphy and bounds. For t <= 0, |e^{-zt}F_phi(t)| <= C e^{-(eps - Re z)|t|}||phi||_k; for t >= 0,
 <= C e^{-(Re z - a)t}||phi||_k. So the integral converges absolutely, locally uniformly on Sigma(a,eps), T_z(phi) is
 holomorphic and |T_z(phi)| <= C(1/(eps - Re z) + 1/(Re z - a))||phi||_k: (E1), (E3) (with N = 0) hold.
2. Eigen-relation. F_phi is C^1 with F_phi' = F_{P phi}. On [-R,R]: int e^{-zt}F_{P phi} dt = [e^{-zt}F_phi]_{-R}^{R}
 + z int e^{-zt}F_phi dt. The bounds of step 1 (applied to phi and P phi) make the boundary terms -> 0 and the integrals
 converge; so T_z(P phi) = z T_z(phi): (E2).
3. Split T_z = B_z + G_z, B_z(phi) := int_{-inf}^0 e^{-zt}F_phi dt (holomorphic on Re z < eps, |B_z(phi)| <=
 C||phi||_k/(eps - Re z)), G_z(phi) := int_0^inf e^{-zt}F_phi dt (holomorphic on Re z > a, |G_z(phi)| <=
 C||phi||_k/(Re z - a)). Suppose T = 0. Fix phi. Then E(z) := B_z(phi) on Re z < eps and E(z) := -G_z(phi) on
 Re z > a agree on the strip, so E is entire. With m = (a+eps)/2: |E| <= C||phi||_k/(eps - m) on Re z <= m and
 |E| <= C||phi||_k/(m - a) on Re z >= m. By Liouville E is constant; and E(x) = B_x(phi) -> 0 as x -> -inf along the
 reals (dominated convergence on t <= 0: for real x <= m, |e^{-xt}F_phi(t)| = e^{x|t|}|F_phi(t)| <=
 e^{m|t|}C e^{-eps|t|}||phi||_k, integrable, and e^{x|t|} -> 0 for t < 0 as x -> -inf). So E = 0.
4. In particular y -> B_{iy}(phi) = int_{-inf}^0 e^{-iyt} F_phi(t) dt vanishes identically: the L^1 function
 F_phi·1_{(-inf,0]} has zero Fourier transform, hence is 0 a.e.; F_phi is continuous, so S(phi) = F_phi(0) = 0. ∎

*Proof of (B).* Choose c in (a', b'). For real omega let rho_omega(z) := exp((z-c)^2 + omega(z-c)) (entire; on
z = sigma + iy, |rho_omega(z)| = exp((sigma-c)^2 - y^2 + omega(sigma-c)): Gaussian decay in y, uniformly on vertical
strips). Define
 S_omega(phi) := (1/2 pi i) int_{Re z = c} rho_omega(z) T_z(phi) dz.
By (E3) on the closed strip a' <= Re z <= b' (constants k, N, C), S_omega is a distribution density of order k.
1. Transport. By Lemma 1.1, F_phi(t) := S_omega(Gamma_t phi) = (1/2 pi i) int_{Re z = c} rho_omega(z) e^{zt} T_z(phi) dz.
2. Contour shift. The integrand is holomorphic on the closed strip [a', b'] and, by (E3) and the Gaussian factor, it
 is O(e^{-y^2/2}) on horizontal segments uniformly in sigma in [a',b'] (for fixed t). By Cauchy's theorem the line
 Re z = c can be moved to Re z = b' (use for t <= 0) or to Re z = a' (use for t >= 0). Hence
 |F_phi(t)| <= e^{b' t} K ||phi||_k for t <= 0 and |F_phi(t)| <= e^{a' t} K ||phi||_k for t >= 0, with
 K = (1/2pi) sup_{sigma in{a',b'}} int |rho_omega(sigma+iy)| C(1+|sigma+iy|)^N dy < inf.
 This is the hypothesis of (A) with eps = b', a = a'.
3. Nonvanishing. Since T != 0, pick z0, phi with T_{z0}(phi) != 0. If T_z(phi) vanished on the whole line Re z = c it
 would vanish on Sigma(a,b) (identity theorem), so h(y) := T_{c+iy}(phi) is a continuous, polynomially bounded function,
 not identically 0. Now S_omega(phi) = (1/2pi) int e^{-y^2} e^{i omega y} h(y) dy, the Fourier transform (at -omega) of
 the nonzero continuous L^1 function e^{-y^2}h; it is not identically 0 in omega. So S_omega != 0 for some omega.
4. Real form. For real phi set (Re S)(phi) := Re S(phi), extended complex-linearly; Re S and Im S satisfy the same
 bounds, and one of them is nonzero. ∎

**Corollary 2.2 (complete picture of "strip statements"; under GH).**
- Strips containing 0 (a < 0 < b): no nonzero EF. (Lemma M of R6-b on a small disc around 0, plus the identity
 theorem; equivalently Theorem J via Theorem 2.1(B) with a' < 0 < b'.)
- Strips with 0 <= a: no nonzero EF  <=> (J1) for X.
- Strips with b <= 0: no nonzero EF <=> (J1) for -X. (For -X: P_{-X} = -P, Gamma^{-X}_t = Gamma_{-t}; so T_z is an EF
 of X on Sigma(a,b) iff T_{-z} is an EF of -X on Sigma(-b,-a).)
So **(J1) for X and for -X together is equivalent to: a GH vector field has no nonzero holomorphic eigen-family
T_z∘P = zT_z (with (E3)) on any open vertical strip.** Equivalently, in terms of generalized functions: no
holomorphic, locally polynomially bounded family of eigen-distributions X t_z = -z t_z over a strip.

Remark 2.3 (what (J1) is NOT). A single eigen-distribution with real part kappa > 0 gives F_phi(t) = e^{zt}S(phi),
rate kappa on both sides, outside (J1) (as the brief notes). Theorem 2.1 shows that (J1) is precisely the statement
that eigenvalues off the imaginary axis cannot occur *holomorphically on an open set*; isolated eigenvalues are
irrelevant.

Remark 2.4 (the families that the problem actually produces). In the case lambda = mu(d) = 0 of the pair construction
(x != y, mu-generic, on one Pesin local unstable leaf), (A) gives a nonzero EF on Sigma(0, theta) (union over delta of
the strips (delta, theta - delta)) with |T_z(phi)| <= C_delta ||phi||_{C^1} for delta <= Re z <= theta - delta; it is
nonzero by R5-a step (f). So for the problem's purposes the needed statement is: **under GH no nonzero EF on
Sigma(0, theta)** (with blow-up of the bounds at Re z -> 0+ allowed). For lambda > 0 (stable pairs), the strip is
(max(0, lambda + delta - theta'), lambda - delta), which in the surviving range lambda >= |chi^-_max| (Prop 6.1)
does not touch 0; so for that case the full (J1), with a > 0, is needed.

## 3. Sufficient spectral conditions for (J1) (proved reductions)

For k >= 0 let Sigma_k := {z in C : there is a nonzero distribution density B of order <= k with B∘P = zB}
(the order-k point spectrum of the transpose of P; equivalently -Sigma_k is the set of eigenvalues of X on
generalized functions of order k). Sigma_k does not depend on nu: if nu' = e^{c}nu then P' phi = e^{-c}P(e^{c}phi),
and B -> B(e^{-c}·) is an order-preserving bijection between eigen-densities for P and P'.

**Proposition 3.1.** If for every k the set Sigma_k ∩ {Re z > 0} has empty interior, then (J1) holds.
Proof. Let S be as in (J1) (0 <= a < eps) and T the EF of Theorem 2.1(A); on Sigma(a,eps) ⊂ {Re z > 0} it has fixed
order k. If S != 0, T is nonzero, so T_{z}(phi) ≢ 0 for some phi; its zeros are discrete, so T_z != 0 and z in Sigma_k
for all z off a discrete set of the strip: Sigma_k contains an open set. ∎

**Proposition 3.2 (Jordan-chain form).** Say that z admits an order-k Jordan chain if there are distribution densities
A, B of order <= k, B != 0, with B∘P = zB and A∘P = zA + B. If for every k the set of z with Re z > 0 admitting an
order-k Jordan chain has empty interior, then (J1) holds. In fact a nonzero EF of order k on a strip produces an
order-k Jordan chain at every point of the strip off a discrete set.
Proof. Let T be a nonzero EF of order k on a closed substrip. T'_z(phi) := d/dz T_z(phi) = (1/2 pi i) oint T_w(phi)
(w-z)^{-2} dw over a small circle, so T'_z is a distribution density of order k. Differentiating (E2) in z:
T'_z(P phi) = zT'_z(phi) + T_z(phi). At every z with T_z != 0, (A,B) = (T'_z, T_z) is a Jordan chain. ∎

Remark 3.3 (why this is the natural generalisation of (K1), and where GH stops). At z = 0, GH excludes Jordan chains:
B∘P = 0 gives B = c nu (F1), and A∘P = c nu forces c = 0 (F2 = (K1)). The proof of (F2) is "u = A/nu satisfies
Xu = -c smooth, so u is smooth by GH, and Xu = 0 at a maximum of u". At z != 0 the analogous equations are
X b = -z b, X alpha = -z alpha - b (b = B/nu, alpha = A/nu): the right-hand sides are not smooth, so GH gives nothing.
If b and alpha were smooth, then: Re z != 0 => b = 0 (at a maximum of |b|^2, 0 = X|b|^2 = -2 Re z |b|^2);
Re z = 0 => |b| is a nonzero constant (X|b|^2 = 0, L1) and w := alpha/b is smooth with Xw = -1, contradicting (K1).
So smooth eigen-families and smooth Jordan chains are excluded for every z; the whole difficulty is that GH
(a statement about X = P - 0 only) does not make P - z hypoelliptic for z != 0. Note that P - z hypoelliptic for small
real z > 0 would by itself be a very strong statement: the continuous solution u_0 = int_{-inf}^0 e^{zs} f∘g_s ds of
(X + z)u = f (in the generalized-function form) would have to be smooth for every smooth f, which essentially says
that derivatives of f∘g_s grow subexponentially, i.e. it already contains the zero-entropy conclusion. So I see no
way to obtain hypoellipticity of P - z from GH that is not circular.

Remark 3.4 (one-sided divisibility, recorded; no GH). Under the hypothesis of (J1), with B_z, G_z as in the proof of
Theorem 2.1(A): Taylor expansion of B at 0 (radius eps) gives B_j(phi) := int_{-inf}^0 ((-t)^j/j!) F_phi dt (order k,
||B_j|| <= C eps^{-j-1}) with B_0∘P = S, B_j∘P = B_{j-1}; expansion of G at any z0 > a (radius z0 - a) gives G_j of
order k, ||G_j|| <= C (z0-a)^{-j-1}, with G_0∘(P - z0) = -S, G_j∘(P - z0) = G_{j-1}. So S is geometrically divisible
by P and by P - z0, with two "inverses" that may differ by an element of ker(·∘(P - z)); by Theorem 2.1 they agree
(on the strip) iff S = 0. This is the precise content of the brief's point (ii): divisibility alone carries no
contradiction unless ker(·∘(P - z)) is controlled for z in the strip.

## 4. Checks

**4.1 Models (proved).** Let Y be a Diophantine linear field on T^n (|k.alpha| >= c|k|^{-tau} for k != 0), nu = Lebesgue,
so d = 0, P = Y. If B∘Y = zB then with e_k = e^{2 pi i k.x}: (2 pi i k.alpha) B(e_k) = z B(e_k), so B(e_k) = 0 unless
z = 2 pi i k.alpha; since B is determined by its values on trigonometric polynomials, Sigma_k ⊂ 2 pi i{k.alpha}, a
countable subset of iR. By Proposition 3.1 (J1) holds for Y and for -Y; by invariance of Sigma_k under smooth
conjugacy (and under the change of nu) the same holds for every vector field smoothly conjugate to a Diophantine linear
field. (This is the only class of GH fields I know, so it is consistent with (J1).)
For a flow with an ergodic mu of positive entropy and mu(d) = 0 (not GH), R5-a Theorem B shows that (0, theta) minus a
discrete set lies in Sigma_1: an EF on Sigma(0, theta) exists. So (J1) is exactly the statement that GH removes this
continuum of non-imaginary eigenvalues.

**4.2 The "why it matters" derivation (checked; correct).**
- lambda = 0: x != y in G on one local unstable leaf (Lemma 6.0, conditionals non-atomic and carried by G).
 t <= 0: |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|}||phi||_{C^1} (R5-a step 4(c)), and J_t(x) <= C_delta + delta|t|,
 giving rate theta - delta; t >= 0: e^{J_t(x)}, e^{b + J_t(y)} <= C e^{delta t}. So a = delta < eps = theta - delta for
 small delta. Correct; constants depend on x, y, which is allowed.
- lambda > 0: x != y in G on one local stable leaf (Lemma 6.0 for g_{-1}); b' exists since d(g_t x, g_t y) <= C e^{-theta' t},
 t >= 0. t <= 0: no cancellation needed, e^{J_t(x)}, e^{b'+J_t(y)} <= C e^{-(lambda - delta)|t|}. t >= 0: cancellation
 gives C e^{J_t(x)} e^{-theta' t}||phi||_{C^1} <= C e^{(lambda + delta - theta')t}||phi||_{C^1}. Then
 a := max(0, lambda + delta - theta') < lambda - delta = eps as soon as 2 delta < theta' and delta < lambda. Correct.
- lambda < 0: -X is GH (O4), mu is (-X)-ergodic with the same entropy, divergence -d, mean -lambda > 0. Correct.
- S != 0 since x != y. And (J1) => h_mu = 0 for all ergodic mu, then the variational step. Correct, modulo the cited
 Pesin theory, Ruelle inequality and Ledrappier-Strelcyn/Lemma 6.0 as in R6-a.
So the chain "(J1) => problem" is sound. By Theorem 2.1 it can be restated: **the problem follows from: under GH,
X has no nonzero EF on any strip Sigma(a,b) with 0 <= a < b, nor (for -X) on any strip with a < b <= 0** — i.e. GH
forbids holomorphic families of non-imaginary eigen-distributions. (For the lambda = 0 case alone, strips Sigma(0,theta)
suffice, Remark 2.4.)

## 5. Can (J1) fail?
A counterexample needs a GH field X with a nonzero EF on a strip in {Re z > 0} (Theorem 2.1). By 4.1 such an X is not
smoothly conjugate to a Diophantine linear flow, so it would in particular be a counterexample to the
Greenfield-Wallach / Katok conjecture (cited from memory: the conjecture that every GH vector field is smoothly
conjugate to a Diophantine linear flow on a torus, up to the known time-change normalisations; proved, as I recall, only
in low dimensions, by Forni and Kocsard in dimension 3, under assumptions I cannot reconstruct reliably). Conversely, if
that conjecture were known in all dimensions, (J1) would follow from 4.1 (and the problem would follow trivially anyway).
So neither a proof via the conjecture nor a counterexample is within reach here.


[R8-c: round8_q4 Sections 2-3. One-sided divergence and one-sided Patterson lemma; asymptotics of the strip transforms at z = 0; analysis of (J1)]
## 2. New small results (proved)

**Lemma 2.1 (no GH needed).** Let mu be ergodic and flow-invariant. Put A^+(x) := int_0^inf e^{J_t(x)} dt, which lies in (0, inf].
(i) Either A^+ < inf mu-a.e., or A^+ = inf mu-a.e.
(ii) If A^+ < inf a.e., then mu(1/A^+) = -mu(d). In particular mu(d) < 0.
Hence, if mu(d) >= 0, then int_0^inf e^{J_t(x)} dt = inf for mu-a.e. x. Symmetrically, if mu(d) <= 0, then int_{-inf}^0 e^{J_t(x)} dt = inf for mu-a.e. x. So in case (PE0) both one-sided integrals diverge at mu-a.e. point.

*Proof.*
1. *Cocycle identity.* Since J_t(g_s x) = J_{t+s}(x) - J_s(x), we have
 A^+(g_s x) = e^{-J_s(x)} int_s^inf e^{J_t(x)} dt.
 So {A^+ < inf} is invariant, and (i) follows from ergodicity.
2. *A lower bound.* A^+ >= int_0^1 e^{J_t} dt >= e^{-||d||_inf}. So 0 < 1/A^+ <= e^{||d||_inf}, and 1/A^+ is bounded and measurable.
3. *The derivative of a = log A^+ along orbits.* Assume A^+ < inf a.e. On {A^+ < inf}, step 1 gives
 a(g_s x) = -J_s(x) + log( A^+(x) - int_0^s e^{J_t(x)} dt ).
 This is C^1 in s, and differentiating gives
 d/ds a(g_s x) = -d(g_s x) - e^{J_s(x)} / (e^{J_s(x)} A^+(g_s x)) = -(d + 1/A^+)(g_s x).
4. *Integrated form.* Hence a(g_s x) - a(x) = -int_0^s (d + 1/A^+)(g_r x) dr.
5. *Birkhoff.* Divide by s. By Birkhoff's theorem the right side tends to -(mu(d) + mu(1/A^+)) for a.e. x.
6. *Recurrence.* Choose K with mu{|a| <= K} > 0. By Poincaré recurrence for g_1, a.e. x in {|a| <= K} has g_n x in {|a| <= K} for infinitely many integers n. Along those times the left side, divided by s, tends to 0.
7. Hence mu(d) + mu(1/A^+) = 0. Since 1/A^+ > 0, this gives mu(d) < 0.
8. *Time reversal.* For the backward statement apply the result to -X. Its log-Jacobian is J_{-t}, its divergence is -d, and mu(-d) >= 0 when mu(d) <= 0. ∎

**Lemma 2.2 (one-sided Patterson lemma; GH).** Let x satisfy J_t(x) = o(t) as t -> +inf and int_0^inf e^{J_t(x)} dt = inf. For s > 0 put
 N(s) := int_0^inf e^{J_t(x) - st} dt,
 T_s^+(phi) := N(s)^{-1} int_0^inf e^{J_t(x) - st} phi(g_t x) dt.
Then T_s^+ -> nu-hat weak* as s -> 0+. The same holds backward.

*Proof.*
1. *Finiteness and divergence.* N(s) < inf because J_t = o(t). By monotone convergence, N(s) -> inf as s -> 0+.
2. *An identity.* d/dt [e^{J_t(x) - st} phi(g_t x)] = e^{J_t(x) - st} (P phi - s phi)(g_t x). Integrate over [0, R] and let R -> inf; the boundary term at R tends to 0 because J_t = o(t). This gives
 T_s^+(P phi) = s T_s^+(phi) - phi(x)/N(s).
3. *The limit.* Every weak* limit point T of T_s^+ as s -> 0+ is a probability measure with T(P phi) = 0 for all phi.
4. By (F1) (that is, GH through L1), T = nu-hat. Compactness then gives convergence of the whole family. ∎

**Corollary 2.3 (what the strip transforms of (PE0) look like at z = 0).**
Setting: mu is ergodic with mu(d) = 0 and h_mu > 0. Points x and y are mu-generic and backward exponentially asymptotic at rate theta (as in Prop. 6.1). Put S = delta_x - e^b delta_y, so that T_z = B_z + Phi_z on 0 < Re z < theta.

Facts:
- B_z is holomorphic on Re z < theta, hence across z = 0.
- For real s -> 0+, we have Phi_s = N_x(s)(nu-hat + o(1)) - e^b N_y(s)(nu-hat + o(1)) weak*, and N_x(s), N_y(s) -> inf.

*Proof.* Apply Lemmas 2.1 and 2.2 to x and to y; the hypothesis J_t = o(t) holds by genericity. ∎

Consequences:
- For every phi with nu(phi) = 0, |T_s(phi)| = o(N_x(s) + N_y(s)).
- T_s(phi) / (N_x(s) + N_y(s)) converges to a multiple of nu(phi) along subsequences.

These are exactly the asymptotics that F1 and F2 permit. So no contradiction can come from the leading term at z = 0. This makes rigorous the "Patterson behaviour" remark of R6-d (R2): the singularity of T_z at 0 is of divergent-normalisation type, and it is aligned with nu.

## 3. On the planner's statement (J1)

(J1) says: under GH there is no nonzero S with
- |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for t <= 0, and
- |F_phi(t)| <= C e^{a t} ||phi||_{C^k} for t >= 0,
for some 0 <= a < eps.

*Finite-dimensional model.* Replace the transport by e^{tA} on C^N and S by a covector.
- Backward decay at rate eps forces S into the sum of generalised eigenspaces with Re(eigenvalue) >= eps.
- Forward growth <= e^{at} forces S into those with Re <= a.
- So S = 0 automatically, with no use of (K0) or (K1).

In infinite dimensions the analogue fails as soon as there is continuous spectrum. The shift on L^2(R) has functionals with one-sided (indeed two-sided) decay. So (J1) is precisely a statement that, near the imaginary axis, the transport has no "continuous spectrum" seen by finite-order distributions.

*What (K0) and (K1) can and cannot see.* (K0) and (K1) constrain the transposed operator only at the single spectral point z = 0. They enter Theorem J through the moments int t^j F_phi(t) dt, and these moments are not defined under one-sided decay. The backward moments m_j^- = int_{-inf}^0 t^j F_phi dt do exist. They satisfy
- m_0^-(P phi) = S(phi), and
- m_j^-(P phi) = -j m_{j-1}^-(phi) for j >= 1.
This is a Jordan chain that starts at S instead of 0, so F1 and F2 never apply. Hence any proof of (J1) must use GH away from z = 0, or the closed-range half of GH, and I found no way to do either. This agrees with R7-b.


[R8-d: round8_q2 Sections 1-2. (V) iff P has closed range; (V) iff dim I = 1; the weighted/unweighted dichotomy. 'Text B' = Corollary 3 of the background]
## 1. Proposition A: (V) iff P has closed range

**Proposition A.** Assume GH. The following are equivalent.
(i) X preserves a smooth positive density (V).
(ii) P(C^inf(M)) is closed in C^inf(M).
When they hold, P(C^inf) = ker nu-hat.

*Proof.*

**(i) => (ii).** Let rho nu be a smooth positive invariant density, so L_X(rho nu) = 0. For smooth phi,
 L_X(rho phi nu) = (X phi) rho nu + phi L_X(rho nu) = rho (X phi) nu.
So P(rho phi) = rho X phi, i.e. P = M_rho X M_rho^{-1}, where M_rho (multiplication by rho) is a topological automorphism of C^inf. Hence P(C^inf) = rho X(C^inf). This is closed, because X(C^inf) is closed (Corollary 3 of Text B).

**(ii) => (i).** Four steps.

*Step 1: P(C^inf) is dense in ker nu-hat, hence equal to it.*
- P(C^inf) lies in ker nu-hat, because int (P phi) dnu = int_M L_X(phi nu) = int_M d(i_X phi nu) = 0.
- Let T be a continuous functional on C^inf vanishing on P(C^inf). Then T(P phi) = 0 for all phi, so T = c nu by (F1). Such a T vanishes on ker nu-hat.
- By Hahn-Banach, P(C^inf) is therefore dense in ker nu-hat. Under (ii) it is closed, so P(C^inf) = ker nu-hat.

*Step 2: ker P != 0.*
- Suppose P is injective. Then P : C^inf -> ker nu-hat is a continuous linear bijection between Fréchet spaces (ker nu-hat is a closed subspace). By the open mapping theorem, P^{-1} is continuous.
- Put S_0(psi) := -nu(P^{-1} psi) on ker nu-hat. This functional is continuous. Extend it to S in (C^inf)' by Hahn-Banach (locally convex form).
- Then S(P phi) = -int phi dnu for all phi. So u := S/nu satisfies <Xu, phi nu> = -S(P phi) = int phi dnu, i.e. Xu = 1.
- This contradicts (K1). (By GH u is smooth, and at a maximum point of u we have Xu = 0.)

*Step 3: a non-negative smooth invariant density.*
- P has real coefficients, so ker P contains a real rho != 0. Then Pρ = 0, i.e. X rho = -d rho.
- Along orbits, d/dt rho(g_t x) = -d(g_t x) rho(g_t x), so rho(g_t x) = rho(x) e^{-J_t(x)}. Hence U_+ = {rho > 0} and U_- = {rho < 0} are open and invariant.
- A nonempty open invariant set is nu-conull (Lemma D of R7-d). Proof: for an invariant Borel set B, X 1_B = 0 in D', so 1_B is a.e. constant by L1.
- U_+ and U_- are disjoint, so they cannot both be nonempty. Replacing rho by -rho, we may assume rho >= 0 and U_+ != ∅.
- Then U_+ is conull, hence dense, and Z := {rho = 0} is a closed invariant nu-null set.

*Step 4: Z is empty.*
- For eps > 0 put v_eps := log(rho + eps), which is smooth. Then
 X v_eps = f_eps := -d rho/(rho + eps).
 We have |f_eps| <= ||d||_inf, and f_eps -> -d · 1_{U_+} = -d nu-a.e. So f_eps -> -d in L^1(nu), hence in D'.
- Take smooth phi with int phi dnu = 0. By Step 1, phi = P psi with psi smooth. Then
 <v_eps, phi nu> = <v_eps, (P psi) nu> = -<X v_eps, psi nu> = -int f_eps psi dnu -> int d psi dnu.
- Put w_n := v_{1/n} - c_n, where c_n := nu-hat(v_{1/n}). For every smooth phi,
 <w_n, phi nu> = <v_{1/n}, (phi - nu-hat(phi)) nu>,
 which converges by the previous item.
- C^inf(M) is Fréchet, hence barrelled. By the Banach-Steinhaus theorem, the pointwise limit w is a distribution and w_n -> w weak*. Hence Xw = lim X w_n = lim f_{1/n} = -d, which is smooth. By GH, w is smooth.
- Take smooth chi >= 0 supported in U_+ with int chi dnu = 1. On U_+, v_{1/n} -> log rho in C^inf_loc. So int v_{1/n} chi dnu converges, and therefore c_n = int v_{1/n} chi dnu - <w_n, chi nu> converges to some c.
- Hence w = log rho - c on U_+, so log rho >= min_M w + c on U_+.
- If Z contained a point z, density of U_+ and continuity of rho would give points of U_+ where rho is arbitrarily small, i.e. log rho -> -inf. This is a contradiction. So Z = ∅.

So rho > 0 everywhere and rho nu is a smooth positive invariant density: (V) holds. The final claim of the proposition is Step 1. ∎

*Remarks.*
1. Proposition A only rewrites (V). It does not prove it. Its use is diagnostic: R7-e (end of §3) and the planner's sketch (2) both asked for a tame inverse of P on its range. Proposition A shows that this tame inverse exists exactly in the volume case, where P is conjugate to X and nothing new is gained.
2. In particular the iteration T_z(phi) = z^N T_z(P^{-N} phi) (Theorem V of R7-e) cannot be run in the non-volume case without first proving (V).
3. Cited only: the open mapping theorem, Hahn-Banach and Banach-Steinhaus for Fréchet spaces. GH enters through L1, (F1), (K1), and in Step 4 through GH itself applied to Xw = -d.

## 2. Proposition B and the dichotomy

**Proposition B.** Assume GH. Then (V) holds iff dim I = 1.

*Proof.*
- (V) => dim I = 1. Take nu = omega invariant. Then T in I iff u = T/omega satisfies Xu = 0 (by (O2)), iff u is constant (L1).
- dim I = 1 => (V). I contains every invariant probability, so I = R mu for the unique invariant probability mu. By the duality consequence of Text A, X(C^inf) = {f : mu(f) = 0}. Hence d - mu(d) = Xa with a smooth, and (O3) gives (V). ∎

**Corollary C (dichotomy for Jordan-chain arguments).** Assume GH and not (V).

*Weighted operator P (the operator of Theorems J, J*, G, Lemma M).*
- Uniqueness holds: T∘P = 0 implies T = c nu (F1), and the Jordan chain at 0 terminates (F2).
- But P(C^inf) is not closed (Proposition A).
- So no estimate |T(phi)| <= C ||P^{-1} phi||_{C^k}-type can be iterated, and the tame "divisibility" of Theorem V is unavailable.

*Unweighted operator X (functions transported without Jacobian weight).*
- The tame inverse exists (Lemma B of R7-d).
- But dim I >= 2 (Proposition B), so the unweighted Jordan chain does not terminate. Its moments are m_j(phi) = int t^j S(phi o g_t) dt.
  - From m_0∘X = 0 and m_1∘X = -m_0 one gets only m_0 in I and m_0(1) = 0.
  - That forces m_0 = 0 iff I ∩ {T : T(1) = 0} = 0, i.e. iff dim I <= 1, i.e. (V).
- So the unweighted analogue of Theorem J (no S != 0 with |S(phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k}) holds under GH iff (V) holds, as far as this proof goes.

*Consequence.* Any proof of (PE-NH) along the round-6/7 lines (moments at z = 0 + continuation or quantitative flatness near 0) must either
- (a) first prove (V), and then handle the volume case, where everything reduces to quantitative growth of ||R^N phi|| (Theorem V); or
- (b) use a mechanism that does not rest on a single operator having both uniqueness and a tame inverse.

Two checks:
- The unweighted moment claim is verified directly. Integration by parts as in Theorem J gives m_j(X phi) = -j m_{j-1}(phi).
- The weighted claim is Proposition A.


[R8-e: round8_q6 Sections 2-4. Where each half of GH lives; volume case divisors B_j = S o R^{j+1}; the coarse-tail obstruction]
## 2. Weighted versus unweighted transport: where each half of GH lives

Two transports are attached to a distribution density S:
- weighted: F_phi(t) = S(e^{J_t} phi o g_t), with d/dt F_phi(t) = F_{P phi}(t);
- unweighted: G_phi(t) = S(phi o g_t), with d/dt G_phi(t) = G_{X phi}(t).

The Jordan-chain proof of Theorem J (moments m_j, m_j o P = -j m_{j-1}) works for a transport exactly when the transpose of the governing operator has
(a) a one-dimensional kernel spanned by an element that does not lie in its own range.

| | operator | kernel of transpose | range |
|---|---|---|---|
| weighted | P | R·nu by (K0) | contains nu? No, by (K1) |
| unweighted | X | I (invariant densities) | closed, = {T : T(1) = 0} (GH, Lemma B) |

**Observation 2.1 (proved).** Assume GH.
(a) For the weighted transport, (a) holds by (K0) and (K1). This is Theorem J.
(b) For the unweighted transport, (a) holds iff dim I = 1. Under GH, dim I = 1 implies (V).

*Proof of (b).*
- Run Theorem J's steps 2–4 with X in place of P. Then m_0 o X = 0, so m_0 lies in I. Also m_0 = -m_1 o X lies in the range of the transpose of X, which is {T : T(1) = 0} (Lemma B(iii) of R7-d, together with the fact that ker X on C^inf is the constants).
- If I = R·mu with mu(1) = 1, then m_0 = c mu with c = m_0(1) = 0. Inducting as in Theorem J gives all m_j = 0, and Fourier uniqueness gives S = 0. If dim I >= 2, the chain argument does not close.
- If dim I = 1, then I = R·mu, where mu is the unique invariant probability. The condition of (O3), "T(d) = c T(1) for all T in I", holds with c = mu(d). So d lies in R + X(C^inf), and (O3) gives (V). ∎

**What this means for leads (a) and (b) in general.**
- Lemma B(iii) (tame Hahn–Banach division: T = S o X) is division in the *unweighted* picture.
- The divisors B_j of lead (a) satisfy B_j o P = B_{j-1}. This is division in the *weighted* picture, i.e. by P^T, which is -X on distribution functions.
- Outside (V) these are different operators. By Proposition C1, the weighted division has closed range only under (V).
- So the tame bounds of Lemma B(iii) give no information on the B_j unless (V) holds. The same applies to the Hahn–Banach pair functionals S_{pq} of lead (b): they live in the unweighted picture, where the uniqueness needed for a Jordan chain holds only if dim I = 1, which again gives (V).
- **Conclusion: the closed-range half of GH can enter a Theorem-J-type argument only in the volume case.** §3 treats that case.

---

## 3. Volume case: divisors = iterated tame inverses; leafwise geometric bounds

Setting: GH, and X preserves a smooth positive density omega. Take nu = omega, so d = 0, J = 0 and P = X. By (O2) the flow is uniquely ergodic, and I = R·omega. By Text B Corollary 3, X: C^inf_0 -> C^inf_0 is a topological isomorphism, where C^inf_0 is the space of omega-mean-zero functions. Let R be its inverse and phi_0 := phi - omega-hat(phi). R commutes with composition by g_t: if Xv = f, then X(v o g_t) = f o g_t, and v o g_t is again mean zero.

Let x != y satisfy d(g_t x, g_t y) <= C0 e^{-theta|t|} for t <= 0. Such pairs exist whenever lambda* > 0 (R5-a, Lemma 2), for example on a Pesin unstable leaf. Put S = delta_x - delta_y and G_phi(t) := phi(g_t x) - phi(g_t y). Then |G_phi(t)| <= C0 e^{-theta|t|} ||phi||_{C^1} for t <= 0.

**Definition.** B_j(phi) := int_{-inf}^0 ((-t)^j / j!) G_phi(t) dt for j >= 0. Then |B_j(phi)| <= C0 theta^{-j-1} ||phi||_{C^1}.

**Proposition 3.1 (proved).**
(a) B_0(X phi) = S(phi), B_j(X phi) = B_{j-1}(phi) for j >= 1, and B_j(1) = 0.
(b) B_j(phi) = S(R^{j+1} phi_0) for all smooth phi and all j >= 0.
(c) Hence, for every N >= 1, every smooth phi and every t <= 0:
 |(R^N phi_0)(g_t x) - (R^N phi_0)(g_t y)| <= C0 theta^{-N} e^{-theta|t|} ||phi||_{C^1}.
(d) Every Hahn–Banach solution S' of S'(X phi) = phi(x) - phi(y) with S'(1) = 0 equals B_0. In particular such S' are unique, and S' = S o R.

*Proof.*
(a) G_{X phi} = G_phi'. Integrate by parts on [-L, 0] and let L -> inf. The boundary term at -L vanishes by the exponential decay. At 0 it equals G_phi(0) = S(phi) for j = 0, and 0 for j >= 1. Also G_1 = 0.
(b) Put D_j(phi) := S(R^{j+1} phi_0), a continuous functional with D_j(1) = 0. For psi smooth, R^{j+1}(X psi) = R^j psi_0, so D_0(X psi) = S(psi_0) = S(psi) (S(1) = 0) and D_j(X psi) = D_{j-1}(psi). Let E_j := B_j - D_j. Then E_0 o X = 0, so E_0 is an invariant distribution density, hence E_0 = c omega. Since E_0(1) = 0, c = 0. Inductively, E_j o X = E_{j-1} = 0 gives E_j = 0 in the same way.
(c) R^N phi_0 o g_t = R^N((phi o g_t)_0). So the left side equals |B_{N-1}(phi o g_t)| by (b). Now
 B_{N-1}(phi o g_t) = int_{-inf}^0 ((-s)^{N-1} / (N-1)!) G_phi(s + t) ds.
 For t <= 0 the integrand is bounded by C0 ||phi||_{C^1} (|s|^{N-1} / (N-1)!) e^{-theta(|s| + |t|)}, and the integral of that is C0 theta^{-N} e^{-theta|t|} ||phi||_{C^1}.
(d) S' - B_0 vanishes on X(C^inf) = C^inf_0 and on 1, so S' - B_0 = 0. ∎

**Corollary 3.2 (stable side).** The same holds for x, y exponentially forward-asymptotic, with R replaced by -R. Apply Proposition 3.1 to -X, which is GH by (O4) and preserves omega; its tame inverse is -R. So on Pesin blocks of an ergodic measure with positive entropy, the iterated inverses R^N phi_0 have geometrically bounded oscillation (C theta^{-N} ||phi||_{C^1}) along local strong unstable and local strong stable leaves. The constants depend only on the Pesin block. By contrast, ||R^N phi_0||_{C^0} is controlled only tamely (C_N ||phi||_{C^{m_N}}), and along the flow direction R^N phi_0(g_s x) - R^N phi_0(x) = int_0^s R^{N-1} phi_0(g_r x) dr, which carries no geometric bound.

**What this gives, and why it is not enough (precise).**
1. Theorem V (R7-e) asks for quasi-analytic growth of K_N(phi) = ||R^N phi_0||_{C^1}. Proposition 3.1 gives geometric growth of the strong-leaf oscillations of R^N phi_0. That is the right size, but in the wrong directions: the eigen-family T_z(phi) = z^N T_z(R^N phi_0) needs S(R^N phi_0 o g_t) for t >= 0, where x and y separate.
2. For t >= 0, Proposition 3.1(b) gives
 |S(R^N phi_0 o g_t)| = |B_{N-1}(phi o g_t)| <= C0 ||phi||_{C^1} sum_{k=0}^{N} t^k theta^{-(N-k)} / k! + 2||phi||_inf t^N/N!,
 which is <= C ||phi||_{C^1} theta^{-N} e^{theta t}. Combined with the trivial bound 2||R^N phi_0||_inf =: 2K'_N, this gives
 |T_z(phi)| <= C |z|^N K'_N^{1 - sigma/theta} theta^{-N sigma/theta} / sigma,  sigma = Re z in (0, theta),
 for N with K'_N >= theta^{-N}. This is an improvement over Theorem V's bound |z|^N K'_N / sigma. But as sigma -> 0 it degenerates to the same bound, so Lemma H still needs quasi-analytic K'_N. Lead (a)'s hoped-for contradiction "geometric growth of the B_j + eigen-relation + tame bounds" does not materialise: the geometric bounds on the B_j are exactly the Taylor coefficients at 0 of the backward transform B_z, which is already holomorphic on Re z < theta. The forward transform remains uncontrolled.

---

## 4. Why the volume-case approach stops: the coarse tail (partly heuristic)

**Lemma 4.1 (proved, complex analysis).** Put F(z) = e^{-z^{-1/2}}/(1+z) (principal branch) on Re z > 0.
- F is in the Hardy space H^2 of the right half-plane. Indeed, for Re z >= 0, z != 0, one has Re(z^{-1/2}) >= |z|^{-1/2} cos(pi/4) > 0, so |F(z)| <= 1/|1+z|.
- For every N, z^{-N} F(z) is also in H^2. Indeed, |z^{-N} e^{-z^{-1/2}}| <= |z|^{-N} e^{-|z|^{-1/2}/sqrt 2} is bounded near 0.
- By Paley–Wiener, F and z^{-N}F are Laplace transforms of L^2 functions k_0 and k_N supported in [0, inf), with d^N k_N / dt^N = k_0 in the distributional sense. Their Fourier transforms are F(i xi) and (i xi)^{-N} F(i xi) up to normalisation.

**Heuristic model (sketch, not proved for a general positive-entropy omega).** Assume an exhaustive filtration by unstable partitions for the flow (Pesin / Ledrappier–Young). Then the Pinsker complement H carries a translation (Lax–Phillips) representation: H ≅ L^2(R; K), with U_t = translation and the subspaces "measurable w.r.t. g_T xi, orthogonal to Pinsker" corresponding to functions supported in [T, inf). In that model:
- smooth phi have exponentially decaying *left* (fine) tails: ||1_{s<T} k_phi|| <= C e^{theta T} ||phi||_{C^1}. This is the smoothness of phi at small unstable scales, the L^2 shadow of Proposition 3.1(c).
- GH gives that k_phi is infinitely divisible by d/ds in L^2, tamely (Proposition 3.1 of R7-b).
- Nothing constrains the *right* (coarse) tail: there is no rate for E(phi | g_T xi) -> E(phi | Pinsker) as T -> inf.

Lemma 4.1 shows that nonzero k satisfying the first two properties exist; it can even have support in [0, inf). So any contradiction must use coarse-scale information. In the hyperbolic case the coarse unstable scale is linked to the fine stable scale by local product structure (this is where Theorem G and Lemma K succeed). With a zero centre exponent there is no such link (R7-a §4, R7-f §3). That is the same obstruction as in the weighted picture, seen spectrally.

---


[R8-f: round8_q9 Sections 1-3. Proposition MG (measured Theorem G), Theorem U (no uniform partial hyperbolicity), Corollary E. 'Theorem G of R7-a' = Theorem G in block R7-a above]
## 1. A measure-valued form of Theorem G (proved; GH + Theorem J only)

**Proposition MG.** Assume GH. Let K ⊂ M be a Borel set and m a finite positive Borel measure on K. Let ξ^s and ξ^u be partitions of K that are measurable for m, with disintegrations m = ∫ m_A dm̂^s(A) = ∫ m_B dm̂^u(B), where the m_A, m_B are probabilities on the elements. Let C, θ > η >= 0 be constants such that:
 (S) if z, z' lie in one ξ^s-element, then d(g_t z, g_t z') <= C e^{-θ t} for t >= 0;
 (U) if z, z' lie in one ξ^u-element, then d(g_t z, g_t z') <= C e^{-θ|t|} for t <= 0;
 (R) J_t(z) <= C + η|t| for all z in K and all real t.
For z, z' in one ξ^s-element put β^s(z,z') := lim_{t->+inf}(J_t z - J_t z'). The limit exists: the derivative of J_t z - J_t z' in t is bounded by Lip(d) C e^{-θ t}. Moreover |J_t z - J_t z' - β^s(z,z')| <= K e^{-θ t} for t >= 0, with K = Lip(d) C/θ. Define β^u for t -> -inf in the same way. Both satisfy the cocycle rule β(z,z'') = β(z,z') + β(z',z'').
Let w be in L^inf(m) such that, for m̂^s-a.e. A and some (hence, by the cocycle rule, every) a in A,
 ∫_A w(z) e^{β^s(z,a)} dm_A(z) = 0,
and, for m̂^u-a.e. B and b in B,
 ∫_B w(z) e^{β^u(z,b)} dm_B(z) = 0.
Then w = 0 m-a.e.

*Proof.* Let S := w m, a finite signed measure and so a distribution density of order 0.
- *t >= 0.* For fixed A and any a in A, the hypothesis gives ∫_A w(z) e^{J_t(a) + β^s(z,a)} φ(g_t a) dm_A(z) = 0. Averaging over a in A with respect to m_A, we get
 ∫_A w e^{J_t} φ o g_t dm_A = ∫_A ∫_A w(z) [ e^{J_t z} φ(g_t z) - e^{J_t a + β^s(z,a)} φ(g_t a) ] dm_A(z) dm_A(a).
- The bracket equals e^{J_t a} [ e^{J_t z - J_t a} φ(g_t z) - e^{β^s(z,a)} φ(g_t a) ]. We have |J_t z - J_t a - β^s| <= K e^{-θt}, |β^s| <= K, and |φ(g_t z) - φ(g_t a)| <= ||φ||_{C^1} C e^{-θt}. So the bracket is at most e^{J_t a} C_1 e^{-θ t} ||φ||_{C^1}, where C_1 depends only on C, K. By (R), this is at most C_2 e^{-(θ-η)t} ||φ||_{C^1}.
- Integrating over A gives |F_φ(t)| = |∫ w e^{J_t} φ o g_t dm| <= C_2 ||w||_inf m(K) e^{-(θ-η)t} ||φ||_{C^1} for t >= 0.
- *t <= 0.* The same argument with ξ^u, (U), β^u and (R) gives the same bound with |t|.
Theorem J (k = 1, eps = θ - η), applied to Re S and Im S, gives S = 0. A finite signed measure that vanishes on C^inf vanishes, so w = 0 m-a.e. ∎

*Remarks.*
- The case where m is counting measure on a finite set is Theorem G of R7-a: the conditions on w are the equations (G).
- In the volume-preserving case (ν = ω invariant), d = 0, so all β vanish and (R) holds with η = 0. The conditions then say: E_m[w | ξ^s] = 0 and E_m[w | ξ^u] = 0. **So under GH plus volume, L^2(m, σ(ξ^s)) + L^2(m, σ(ξ^u)) is dense in L^2(m) for every such (K, m, ξ^s, ξ^u).**
- For a hyperbolic μ, local product structure on a Pesin block makes m ≈ (marginal) ⊗ (marginal), and a product w = f(s-index) g(u-index) with mean-zero factors works. This gives another proof of Theorem 5.1 of R6-a that does not use horseshoes. For non-hyperbolic μ, see §4.

## 2. GH excludes uniform partial hyperbolicity (proved, modulo cited classical theorems)

**Definition.** X is *partially hyperbolic* if there are a continuous Dg_t-invariant splitting TM = E^s ⊕ E^c ⊕ E^u with X in E^c, dim E^s >= 1 and dim E^u >= 1, and constants C >= 1, θ > 0, θ' > 0, such that for t >= 0:
- ||Dg_t|E^s|| <= C e^{-θt} and ||Dg_{-t}|E^u|| <= C e^{-θt};
- ||Dg_t|E^s(x)|| · ||Dg_{-t}|E^c(g_t x)|| <= C e^{-θ' t}, and symmetrically for E^u with t replaced by -t (domination).
Anosov flows are included (E^c = RX).

**Cited [HPS]** (Hirsch–Pugh–Shub, strong stable manifold theorem, from memory). For such a flow there are continuous foliations W^{ss}, W^{uu} with C^1 leaves tangent to E^s, E^u. "Continuous" means the following: around every x0 there are a chart φ: V -> R^n with E^u(x0) = R^u × 0, a neighbourhood V0 of x0 and ρ > 0, such that for a in V0 the plaque of W^{uu}(a) through a is, in the chart, the graph of a C^1 map h_a over the ball B^u(π(a), ρ), with (a, v) -> h_a(v) continuous. The same holds for W^{ss} with E^s(x0). Leaves are tangent to E^s, so a C^1 path in a leaf is contracted: d(g_t y, g_t z) <= d_{W^{ss}}(g_t y, g_t z) <= C e^{-θt} d_{W^{ss}}(y,z) for y in W^{ss}(z) and t >= 0. Likewise for W^{uu} with t <= 0.

**Cited [Hu]** (Hurewicz's theorem on closed maps, from memory). If f: X -> Y is a closed continuous map of separable metric spaces, then dim X <= dim f(X) + sup_y dim f^{-1}(y) (covering dimension). Also used: dim of a closed ball in R^D is D, and every subset of an n-manifold has dim <= n.

**Lemma W (graphs).** Let G be a finite connected multigraph without loops, and let E - V + 1 <= 1 be its cyclomatic number. Then for vertices s, t and a length L there are at most 3 non-backtracking walks of length L from s to t. (Non-backtracking: consecutive edges are distinct.)
*Proof.*
1. *Trees.* In a tree a non-backtracking walk is a path. Suppose a vertex repeats, v_i = v_j with j - i minimal. Then j - i = 1 is a loop, which is impossible. j - i = 2 needs two distinct edges between v_i and v_{i+1}, which is impossible in a tree (equal edges would be backtracking). j - i >= 3 gives a cycle. Paths between two vertices of a tree are unique, so there is at most 1 walk.
2. *Unicyclic graphs.* If E - V + 1 = 1, let C be the unique cycle; it may have length 2, i.e. a pair of parallel edges. G minus the edges of C is a forest, and each of its components T_c contains exactly one vertex c of C.
   - A non-backtracking walk that uses no edge of C lies in one T_c, so by step 1 it is the unique path from s to t.
   - Otherwise, consider any maximal sub-walk between two cycle edges. It lies in a single T_c, and it starts and ends at c, because c is the only vertex of T_c incident to cycle edges. A non-backtracking walk in a tree from c to c has length 0 (step 1). So all cycle edges used are consecutive.
   - Every cycle vertex has exactly two cycle edges. So the cycle part of the walk is determined by its first edge, which is one of the 2 cycle edges at the entry vertex c1, together with its length.
   - The part before the cycle is the tree path from s to c1, where c1 is the root of the component of s. The part after it is the tree path from c2 to t, where c2 is the root of the component of t. So the length of the cycle part is L - d(s,c1) - d(c2,t), which is determined.
   - Hence there are at most 2 walks of this kind, and at most 3 walks in all. ∎

**Theorem U.** Assume GH. Then X is not partially hyperbolic with |m(d)| < θ for every flow-invariant probability m. In particular, **a GH vector field preserving a smooth positive density is not partially hyperbolic** (take ν = ω, so that d = 0).

*Proof.* Suppose X is partially hyperbolic and max_m |m(d)| < η < θ. (The maximum is attained, since m -> m(d) is continuous and affine on a compact set.) Let u = dim E^u, s = dim E^s, n = dim M.

*Step 1 (uniform growth bound).* By the standard fact (R4-q7 Prop 2.1, step 1), limsup_{t->+inf} sup_x J_t(x)/t = max_m m(d) < η. The same fact for the reversed flow gives limsup_{t->+inf} sup_x J_{-t}(x)/t = max_m(-m(d)) < η. Hence J_t(x) <= C_0 + η|t| for all x and all real t. So (R) of Proposition MG holds for every point.

*Step 2 (the walk map).* Fix x0 and the chart, V0 and ρ of [HPS] (for both foliations). Define Φ^u_a(v) := φ^{-1}(π(a) + v, h_a(π(a)+v)) for |v| < ρ, and Φ^s_a(w) in the same way. These are continuous in (a, v), injective in v, and Φ_a(0) = a. Fix k with k(u+s) >= n+1. For a parameter vector P = (v_1, w_1, ..., v_k, w_k) put
 a_0 = x0, a_{2i-1} = Φ^u_{a_{2i-2}}(v_i), a_{2i} = Φ^s_{a_{2i-1}}(w_i).
By continuity there is a neighbourhood N0 of 0 in R^D, D = k(u+s), on which all a_j lie in V0. Let B be a closed ball contained in {P in N0 : all v_i ≠ 0, all w_i ≠ 0}, which is open and nonempty. Put F(P) := a_{2k}. F is continuous on the compact set B, hence closed. The point sequence (a_0, ..., a_{2k}) determines P, because v_i = π(a_{2i-1}) - π(a_{2i-2}) and similarly for w_i.

*Step 3 (four walks with a common end).* If every fibre of F|B had at most 3 points, [Hu] would give D = dim B <= dim F(B) <= n, a contradiction. So there are a point z and four distinct parameter vectors P^1, ..., P^4 in B with F(P^r) = z.

*Step 4 (the class graph).* Let Γ be the bipartite multigraph whose vertices are the global leaves of W^{ss} and of W^{uu}. Its edges are the points of M: the point y joins W^{ss}(y) and W^{uu}(y).
- For a parameter vector P, the edges a_0, a_1, ..., a_{2k} form a walk of length 2k+1 from the vertex W^{ss}(x0) to the vertex W^{uu}(z). Indeed a_{2i-1} and a_{2i-2} share their uu-leaf, and a_{2i} and a_{2i-1} share their ss-leaf.
- This walk is non-backtracking, because a_{j+1} ≠ a_j (the v_i, w_i are nonzero and the Φ are injective).
- The four walks are distinct (Step 2). Let U be the finite subgraph formed by their edges and vertices. It is connected, since all walks start at x0, and it has no loops.
- By Lemma W, U has cyclomatic number >= 2, i.e. #edges >= #vertices + 1.

*Step 5 (contradiction).* Let Z be the edge set of U (finitely many distinct points). The stable classes are the ss-vertices of U, and the unstable classes are its uu-vertices. Every point of Z lies in exactly one class of each kind. Then:
- (S) and (U) of Proposition MG hold with m the counting measure on Z: points in a class lie on one global strong leaf at finite leaf distance, and [HPS] gives d(g_t y, g_t y') <= C d_leaf(y,y') e^{-θ|t|} on the relevant half-line.
- (R) holds by Step 1.
- The equations of Proposition MG (= the equations (G)) form a homogeneous linear system with #Z unknowns and #vertices < #Z equations, so it has a nonzero solution w.
Proposition MG gives w = 0, a contradiction. ∎

*Remark (the volume case needs only invariance of domain).* If ν = ω is invariant, then all β = 0. A single cycle in Γ then already gives a solution (alternating signs ±1 around the even cycle; this is item (c) of R7-a). It is enough that F|B is not injective, which follows from invariance of domain because D > n. Two distinct walks with the same ends contain a cycle made of their edges (by step 1 of Lemma W, applied to a forest).

*Remark (scope).* By Yomdin's theorem (C^inf: h_top >= the exponential growth rate of volumes of discs; cited from memory), partially hyperbolic flows have h_top >= the growth rate of uu-discs > 0. So Theorem U excludes a class of positive-entropy flows outright, in every dimension, without Pesin theory or horseshoes. It is a statement about a sub-class of vector fields, so by the task's rules it does NOT answer (PE-NH).

## 3. Two further corollaries (proved)

**Corollary E (no two-sided exponential decay of a density).** Assume GH. There is no nonzero w in L^1(ν) with |∫ (w o g_{-t}) φ dν| <= C e^{-ε|t|} ||φ||_{C^k} for all real t and all smooth φ.
*Proof.* Let S = wν. Since ∫ ψ o g_t e^{J_t} dν = ∫ ψ dν (change of variables), F_φ(t) = ∫ w e^{J_t} φ o g_t dν = ∫ (w o g_{-t}) φ dν. Apply Theorem J. ∎
In the volume case (ν = ω, J = 0) this says: under GH no nonzero (mean-zero) w in L^1 has correlations ∫ w · φ o g_t dω decaying exponentially, uniformly in C^k norms. So GH + volume rules out exponential mixing of any nonzero mean-zero density. By Theorem J*, it also rules out mixing at any quasi-analytic rate.

**Corollary U' (dimension 4 and up, partially hyperbolic positive-entropy measures).** This is contained in Theorem U. A GH flow with a smooth invariant volume has no continuous invariant splitting of the above kind on M. Note: under GH any invariant compact set with nonempty interior is M (Lemma D of R7-d), so "partially hyperbolic on an invariant set with interior" is the same thing.


=== END OF ROUND-8 RESULTS ===

=== RESULTS OF ROUND 9 (quoted verbatim from the workers' answers; each labelled with its source; '[R8-a]', '[R8-b]', '[R6-a]', 'R7-e', 'Text B', '(F1)', '(F2)', '(K0)', '(K1)', 'L1', 'Lemma C', 'B4' etc. refer to the blocks above; 'the brief' inside them refers to the round-9 task, whose missing statement (EF) was: under GH every family T_z of order-<=1 distribution densities on an open vertical strip, holomorphic in z, bounded in (C^1)' on closed substrips, with T_z(P phi) = z T_z(phi), vanishes identically) ===

### Block R9-a (from round9_q10: check and repair of Theorem R; Theorem R' for g_1-ergodic measures; Lemma 6.0; variational step; derivation)
## 1. Theorem R

### 1.0 The gap and the corrected statement

**Where the gap is.** In step 2 of Theorem R, the facts "for mu-a.e. x the conditional mu^xi_x is non-atomic" (Lemma 6.0) and "h_mu(g_1) = H_mu(xi | g_1 xi)" ([LY]) are used for f = g_1 and the flow-ergodic mu.
- In the proof of Lemma 6.0 one gets w o f = w a.e. The conclusion "w is a.e. constant" then requires f-ergodicity.
- Without it, the argument only shows that {w > 0} is an f-invariant set on which the integrand of H(xi | f xi) vanishes. If h_mu(f) > 0, this gives mu{w = 0} > 0, not w = 0 a.e.
- A flow-ergodic mu fails to be g_1-ergodic exactly when the flow has an L^2(mu)-eigenfunction with eigenvalue in 2 pi i Z \ {0}. This can certainly happen, for instance for suspensions with constant roof 1/k.

So, as written, step 2 is not justified for every flow-ergodic mu.

**Corrected statement (Theorem R').** Let X be any smooth vector field on a compact manifold M (GH not used). Let nu be a Borel probability that is g_1-invariant and g_1-ergodic, with h_nu(g_1) > 0. Put lambda := nu(J_1) = int int_0^1 d(g_s z) ds dnu(z). Let chi > 0 be the smallest positive Lyapunov exponent of (g_1, nu), and fix 0 < theta < chi and 0 < delta < theta/4. Put Omega := {lambda + delta < Re z < lambda + theta - delta}. Then there is a family T_z (z in Omega) of continuous linear functionals on C^1(M) satisfying (i), (ii), (iii) of (EF), with T_z != 0 for all z in Omega outside a discrete subset of Omega.

**Relation to the original statement.** Let mu be flow-ergodic with h_mu(g_1) > 0, and let mu = int nu dtau(nu) be its g_1-ergodic decomposition.
- By Jacobs' formula, h_mu(g_1) = int h_nu(g_1) dtau. So tau{nu : h_nu(g_1) > 0} > 0.
- Let G_mu be the set of z with J_t(z)/t -> mu(d) as t -> +inf and as t -> -inf. By the continuous-time Birkhoff theorem for the flow-ergodic mu (applied to the flow and to the reversed flow), mu(G_mu) = 1. Hence nu(G_mu) = 1 for tau-a.e. nu.
- For such nu, nu-a.e. point has J_n/n -> nu(J_1) (Birkhoff for g_1). So nu(J_1) = mu(d).
- The Lyapunov spectrum of g_1 is flow-invariant, because Dg_s is uniformly bounded for |s| <= 1. So it is mu-a.e. constant, and nu has the same chi.

So Theorem R' applied to such a nu gives the family of Theorem R for mu, with the same lambda = mu(d), the same chi and the same strip. **Theorem R as stated is therefore true, but its proof must go through nu.**

### 1.1 Proof of Theorem R' (written out in full, with each check)

**Step 1 (exponents).** h_nu(g_{-1}) = h_nu(g_1) > 0.
- [Ru] Ruelle's inequality (cited from memory): for a C^1 diffeomorphism f of a compact manifold and an f-invariant ergodic nu, h_nu(f) <= sum of the positive Lyapunov exponents of (f, nu), with multiplicity. Here g_{+-1} is C^inf, and nu is ergodic for both.
- Applied to g_1, it gives a positive exponent, so chi := chi^+_min > 0 exists. (Applied to g_{-1}, it gives a negative exponent; that is not needed below.)
- Exponents are nu-a.e. constant by ergodicity.

**Step 2 (generic points).** Let G := {z : J_t(z)/t -> lambda as t -> +inf and as t -> -inf}.
- *Birkhoff.* J_n(z) = sum_{k=0}^{n-1} J_1(g_k z). So J_n/n -> nu(J_1) = lambda nu-a.e. (Birkhoff for g_1).
- *Backward.* J_{-n}(z) = -sum_{k=1}^{n} J_1(g_{-k} z), and nu is g_{-1}-ergodic. So J_{-n}/(-n) -> lambda nu-a.e.
- *Real times.* |J_t - J_{floor(t)}| <= ||d||_inf. So the integer limits give the real ones.
- Hence nu(G) = 1. G is Borel: it is defined by integer-time limits of continuous functions.

**Step 3 (choice of the pair; checks the citations [P], [LY] and Lemma 6.0).** Cited from memory, for the C^inf diffeomorphism f = g_1 and the f-ergodic nu:
- [P] (Pesin; Ruelle 1979; Fathi–Herman–Yoccoz; no hyperbolicity assumption on the other exponents). For nu-a.e. x there is a local unstable manifold W^u_loc(x), an embedded C^1 disc tangent to the sum of the Oseledets spaces of the positive exponents. For every delta' > 0 and every y in W^u_loc(x): d(f^{-m}x, f^{-m}y) <= C(x, delta') e^{-(chi - delta')m} for m >= 0.
  - The same holds, with a constant depending also on y, for y in the global unstable manifold W^u(x) = union_n f^n W^u_loc(f^{-n}x). Indeed, if f^{-n}y lies in W^u_loc(f^{-n}x), apply [P] at f^{-n}x for m >= n, and absorb the finitely many m < n into the constant.
- [LS/LY] (Ledrappier–Strelcyn 1982; Ledrappier–Young 1985, Part I). There is a measurable partition xi subordinate to W^u, with xi(x) contained in W^u(x) (indeed in a local unstable manifold) for a.e. x. It is increasing: xi refines f xi, i.e. xi(fx) ⊂ f(xi(x)). And h_nu(f) = H_nu(xi | f xi) = -int log nu^{f xi}_z(xi(z)) dnu(z).
  - These are stated for ergodic measures and C^2 (indeed C^{1+alpha}) diffeomorphisms, zero exponents allowed. Both hypotheses hold here because nu is g_1-ergodic, and that is the point of the repair.
  - Since h_nu(f) <= sum chi^+ < inf by [Ru], H(xi | f xi) is finite.
- Lemma 6.0 (re-proved in §2) gives: nu^xi_x({x}) = 0 for nu-a.e. x.
- *The conditional is carried by G.* nu(G) = 1 and nu = int nu^xi_x dnu(x). So int nu^xi_x(G) dnu(x) = 1, hence nu^xi_x(G) = 1 for a.e. x. (G is Borel, so this is legitimate.)
- *The pair.* Intersect the full-measure sets: the set where [P] holds, x in G, nu^xi_x({x}) = 0, nu^xi_x(G) = 1, and nu^xi_x(xi(x)) = 1. Take x in this intersection. Then nu^xi_x(G ∩ xi(x) \ {x}) = 1, so there is y in G ∩ xi(x) with y != x. **Answer to the brief's question:** the conditional is carried by G because G has full measure and conditionals of a full-measure set are a.e. full. No dynamical property of G is needed beyond its Borel measurability.
- *Rate.* Choose delta' with chi - delta' > theta. By [P] (global form): d(g_{-m}x, g_{-m}y) <= C e^{-(chi - delta')m} for integers m >= 0, where C depends on x and y.

**Step 4 (interpolation to real times).** Let t <= 0 and write t = -m - s with m >= 0 an integer and s in [0,1). Then g_t = g_{-s} o g_{-m}. Put L' := max_{s in [0,1]} Lip(g_{-s}); it is finite because (s, z) -> g_{-s}(z) is C^1 on [0,1] x M with M compact. Then

d(g_t x, g_t y) <= L' C e^{-(chi - delta')m} <= L' C e^{chi} e^{-(chi - delta')|t|} <= C_0 e^{-theta|t|}.

Checked.

**Step 5 (the constant b).** For t <= 0, J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds. The integrand is bounded by Lip(d) C_0 e^{-theta|s|}, which is integrable on (-inf, 0]. So
- b := lim_{t -> -inf} (J_t(x) - J_t(y)) = -int_{-inf}^0 (d(g_s x) - d(g_s y)) ds exists, and
- J_t(x) - J_t(y) - b = int_{-inf}^t (d(g_s x) - d(g_s y)) ds, so |J_t(x) - J_t(y) - b| <= K e^{-theta|t|} with K := Lip(d) C_0/theta.

Checked.

**Step 6 (one-sided growth bounds).** Since x and y lie in G, there is C_1 (depending on x and y) with:
- J_t(x) <= C_1 + (lambda + delta)t and J_t(y) <= C_1 + (lambda + delta)t for t >= 0;
- J_t(x) <= C_1 + (-lambda + delta)|t| for t <= 0, because J_t(x) = lambda t + o(|t|) = -lambda|t| + o(|t|) as t -> -inf.

Checked.

**Step 7 (the two bounds of step 4 of R8-a).** Put S := delta_x - e^b delta_y and F_phi(t) := e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y). This makes sense for every continuous phi, and is continuous in t.
- *t >= 0.* |F_phi(t)| <= (1 + e^b) e^{C_1} e^{(lambda + delta)t} ||phi||_inf.
- *t <= 0.* Write r_t := J_t(x) - J_t(y) - b, so that e^{b + J_t(y)} = e^{J_t(x)} e^{-r_t} and |r_t| <= K e^{-theta|t|} <= K. Then
  F_phi(t) = e^{J_t(x)} [ (phi(g_t x) - phi(g_t y)) + (1 - e^{-r_t}) phi(g_t y) ].
  Using |phi(p) - phi(q)| <= ||dphi||_inf d(p,q), Step 4, and |1 - e^{-r}| <= |r| e^{|r|}:
  |F_phi(t)| <= e^{C_1} e^{(-lambda + delta)|t|} (C_0 + K e^K) e^{-theta|t|} ||phi||_{C^1} = C_2 e^{-(theta + lambda - delta)|t|} ||phi||_{C^1}.
- *Constants.* C_2 = e^{C_1}(C_0 + K e^K) and C_3 := (1 + e^b) e^{C_1} depend on x, y and the flow, never on phi. That is all that is required, since the pair is fixed once and for all.

Checked.

**Step 8 (convergence, holomorphy, bound (ii)).** Let a := lambda + delta and b_0 := lambda + theta - delta. Then a < b_0 because theta > 2 delta (indeed delta < theta/4). For z with sigma = Re z in (a, b_0):
- for t >= 0: |e^{-zt} F_phi(t)| <= C_3 e^{-(sigma - a)t} ||phi||_inf;
- for t <= 0: |e^{-zt} F_phi(t)| = e^{sigma|t|} |F_phi(t)| <= C_2 e^{-(b_0 - sigma)|t|} ||phi||_{C^1}.

So T_z(phi) := int_R e^{-zt} F_phi(t) dt converges absolutely for every phi in C^1(M), and is linear in phi. On a closed substrip a < a_1 <= Re z <= b_1 < b_0:

|T_z(phi)| <= ( C_3/(a_1 - a) + C_2/(b_0 - b_1) ) ||phi||_{C^1},

uniformly in Im z. This gives (ii) and continuity of T_z on C^1(M).
- *Holomorphy (i).* For fixed t the integrand is entire in z, and it is jointly continuous in (t, z). On every compact subset of Omega it is dominated by the z-independent integrable function C_3 e^{-(a_1 - a)t} 1_{t >= 0} + C_2 e^{-(b_0 - b_1)|t|} 1_{t <= 0} (times the norm of phi). So z -> T_z(phi) is holomorphic, by Morera plus Fubini, or by differentiation under the integral sign. This holds for every phi in C^1, in particular for smooth phi.

Checked.

**Step 9 (the eigen-relation (iii)).** For smooth phi, F_phi is C^1 with F_phi' = F_{P phi}. This is elementary here and needs no C^inf-valued argument. For a single point w:

d/dt [e^{J_t(w)} phi(g_t w)] = d(g_t w) e^{J_t(w)} phi(g_t w) + e^{J_t(w)} (X phi)(g_t w) = e^{J_t(w)} (P phi)(g_t w),

using d/dt J_t(w) = d(g_t w) and d/dt phi(g_t w) = (X phi)(g_t w). Apply this to w = x and to w = y (with the constant factor e^b).

On [-R, R]:

int_{-R}^{R} e^{-zt} F_{P phi}(t) dt = [e^{-zt} F_phi(t)]_{-R}^{R} + z int_{-R}^{R} e^{-zt} F_phi(t) dt.

- *Boundary terms.* By Step 8 applied to phi, |e^{-zR} F_phi(R)| <= C_3 e^{-(sigma - a)R} ||phi||_inf -> 0 and |e^{zR} F_phi(-R)| <= C_2 e^{-(b_0 - sigma)R} ||phi||_{C^1} -> 0.
- *Integrals.* Both integrals converge absolutely as R -> inf, by Step 8 applied to phi and to P phi (P phi is smooth, so in C^1).

Hence T_z(P phi) = z T_z(phi) for every smooth phi and every z in Omega. This is (iii). Checked.

**Step 10 (non-vanishing).** Since x != y, there is a smooth phi_0 with phi_0(x) = 1 and phi_0(y) = 0. Then F_{phi_0}(0) = 1.
- Fix a real kappa_0 in (a, b_0). By Step 8, G(t) := e^{-kappa_0 t} F_{phi_0}(t) is continuous and in L^1(R), with G(0) = 1.
- Its Fourier transform is Ghat(omega) = int e^{-i omega t} G(t) dt = T_{kappa_0 + i omega}(phi_0).
- If z -> T_z(phi_0) vanished identically on Omega, then Ghat = 0. By uniqueness of the Fourier transform on L^1, G = 0 a.e., hence everywhere by continuity. This contradicts G(0) = 1.
- So the holomorphic function z -> T_z(phi_0) on the connected open strip Omega is not identically zero. By the identity theorem its zero set Z is discrete and closed in Omega.
- For z in Omega \ Z we have T_z(phi_0) != 0, so T_z != 0.

Checked. ∎

**Conclusion on (1).** With the repair of §1.0, Theorem R holds as stated: there is no GH, and the family satisfies (i), (ii) and (iii) of (EF) on Omega, with T_z != 0 off a discrete set.

---

## 2. Lemma 6.0 (re-checked, with two clarifications)

**Setting.** f a C^2 diffeomorphism, nu an **f-ergodic** invariant probability, and xi as in [LS/LY]: increasing, with H(xi | f xi) = h_nu(f) in (0, inf).

**Claim.** nu^xi_x({x}) = 0 for a.e. x, and a.e. conditional nu^xi_x is non-atomic.

**Proof (the R6-a proof, with the missing justifications supplied).**
1. *Transport of conditionals.* (f xi)(fx) = f(xi(x)). By invariance of nu and uniqueness of disintegration, nu^{f xi}_{fx} = f_* nu^xi_x for a.e. x. Hence nu^{f xi}_{fx}({fx}) = nu^xi_x({x}) =: w(x).
   - w is measurable: w(z) = lim_n nu^xi_z(Q_n(z)) for a refining sequence of finite partitions Q_n generating the Borel sigma-algebra.
2. *Restriction formula (clarification 1).* Since xi refines f xi:
   nu^xi_z = nu^{f xi}_z(· ∩ xi(z)) / nu^{f xi}_z(xi(z)) for a.e. z.
   This needs nu^{f xi}_z(xi(z)) > 0 a.e., which holds because -int log nu^{f xi}_z(xi(z)) dnu = H(xi | f xi) < inf.
   - Given that, nu^{f xi}_z-almost every point lies in one of the countably many xi-cells of positive conditional mass inside (f xi)(z).
   - The right side is then a xi-measurable system of probabilities whose average over each f xi-cell, hence over M, reproduces nu. Uniqueness of disintegration gives the formula.
   R6-a used this without comment; it is correct.
3. *Monotonicity.* With z = fx and {fx} ⊂ xi(fx):
   w(fx) = nu^{f xi}_{fx}({fx}) / nu^{f xi}_{fx}(xi(fx)) = w(x) / nu^{f xi}_{fx}(xi(fx)) >= w(x).
4. *Invariance.* 0 <= w <= 1 and nu is invariant, so int (w o f - w) dnu = 0. The integrand is nonnegative, so w o f = w a.e.
5. *Constancy.* By **f-ergodicity**, w = w_0 a.e. (This is the step that needs g_1-ergodicity; see §1.0.)
6. *If w_0 > 0.* Step 3 with equality gives nu^{f xi}_{fx}(xi(fx)) = 1 for a.e. x, hence nu^{f xi}_z(xi(z)) = 1 for a.e. z (f preserves nu). Then H(xi | f xi) = 0, contradicting h_nu(f) > 0. So w_0 = 0.
7. *Non-atomicity (clarification 2).* Let A := {z : nu^xi_z({z}) > 0} = {w > 0}. Then nu(A) = 0 by step 6. (R6-a wrote "nu(A) = int w dnu"; that is a slip, since nu(A) = nu{w > 0}, but the conclusion is the same.)
   - Conditionals are constant on cells. So A ∩ xi(x) is exactly the set of atoms of nu^xi_x.
   - Hence 0 = nu(A) = int nu^xi_x(A) dnu(x) = int nu^xi_x(atoms of nu^xi_x) dnu(x).
   - So a.e. conditional is non-atomic. ∎

Only "nu^xi_x({x}) = 0 a.e." is actually used in Theorem R (§1.1 Step 3). Lemma 6.0 is correct for f-ergodic nu.

---

## 3. The variational step (step 1 of the chain)

**Statement needed (repaired form).** If h_top(g_1) > 0, then there is a g_1-invariant, g_1-ergodic Borel probability nu with h_nu(g_1) > 0.

**Proof (cited classical theorems).**
- *Variational principle* (Goodwyn–Dinaburg–Goodman; g_1 is a homeomorphism of a compact metric space): h_top(g_1) = sup h_m(g_1) over g_1-invariant m. So some m has h_m(g_1) > 0.
- *Jacobs' formula*: if m = int nu dtau(nu) is the g_1-ergodic decomposition, then h_m(g_1) = int h_nu(g_1) dtau. Hence some ergodic component nu has h_nu(g_1) > 0.
- This is all Theorem R' needs. The topological entropy of the flow is by definition h_top(g_1), and h_top(g_t) = |t| h_top(g_1).

**The chain's original version.** It passes through m-bar = int_0^1 (g_s)_* m ds and the flow-ergodic decomposition. It is also correct:
- (g_r)_* m-bar = m-bar, because s -> (g_s)_* m is 1-periodic when (g_1)_* m = m.
- h_{(g_s)_* m}(g_1) = h_m(g_1), because g_s conjugates (g_1, m) to (g_1, (g_s)_* m).
- The barycentre formula holds for these integral decompositions into g_1-invariant measures (combine Jacobs' formula with the decomposition of the ergodic decompositions).

But it then needs the reduction of §1.0 (flow-ergodic to g_1-ergodic) before Lemma 6.0 can be applied. Going directly to a g_1-ergodic nu is shorter.

---

## 4. The derivation (EF) + Theorem R' + variational step => h_top(g_1) = 0

1. Suppose h_top(g_1) > 0. By §3 there is a g_1-ergodic nu with h_nu(g_1) > 0.
2. By Theorem R' (with the same smooth density nu_0 used to define d and P in (EF)), there is a family T_z on Omega = {a < Re z < b_0} with a < b_0, satisfying (i), (ii), (iii), and T_z != 0 for some z in Omega.
3. *Hypothesis-by-hypothesis comparison with (EF).*
   - T_z is a continuous linear functional on C^1(M) (Step 8).
   - (i): holomorphy for smooth phi. Delivered for all C^1 phi.
   - (ii): sup over closed substrips and ||phi||_{C^1} <= 1. Delivered, uniformly in Im z.
   - (iii): T_z(P phi) = z T_z(phi) for smooth phi. Delivered.
   - Same nu_0, d and P on both sides.
   **No hypothesis of (EF) is stronger than what Theorem R' gives.** (EF) is even stated with a uniform bound, which is exactly what Step 8 gives; no polynomial growth in |Im z| is needed.
4. Under GH, (EF) gives T_z = 0 for all z in Omega. This is a contradiction, so h_top(g_1) = 0.

**Dimension and zeros.**
- Neither Theorem R' nor the derivation uses dim M >= 2.
- If dim M = 1, Theorem R' is vacuous: by [Ru] for g_1 and g_{-1} a positive-entropy measure would need a positive and a negative exponent among n = 1 exponents. In any case flows on compact 1-manifolds have zero entropy.
- mu(Zero X) = 0 is not used anywhere. If nu(Zero X) > 0, then nu(Zero X) = 1 by ergodicity (Zero X is invariant), and since g_1 = id there, h_nu = 0. So such nu never enter, but the proof does not need this.
- GH enters only through (EF).

**Remark on (EF) (no attempt).** The strip Omega may or may not contain 0. When it does, (EF) on Omega is already Lemma M / Theorem J, so the open content of (EF) is the case of strips avoiding 0, as the brief says.

---


### Block R9-b (from round9_q3: band lemma, Proposition 2 (J1-0), Lemma 3, obstruction, and Theorem A: single-point Jordan-chain criterion)
---

## 1. Lemma 1: the spectral band (no GH)

**Transport norms.** For k ≥ 0 let G_k(t) := ‖Γ_t‖_{C^k → C^k} (the operator norm of Γ_t on the
Banach space C^k(M)); it is finite, submultiplicative in t (G_k(t+s) ≤ G_k(t)G_k(s)) and locally
bounded, so the limits
  γ_k^+ := lim_{t → +∞} (1/t) log G_k(t),   γ_k^- := lim_{t → +∞} (1/t) log G_k(−t)
exist in [−∞, ∞) by Fekete's subadditivity lemma, and are finite because G_k(t) ≥ G_0(t) ≥
e^{min_x J_t(x)} > 0.

**Lemma 1.** Let X be any smooth vector field on a compact manifold (GH is **not** used). If
z ∈ Σ_k then
  −γ_k^- ≤ Re z ≤ γ_k^+ .

*Proof.* Let T ≠ 0 of order ≤ k with T ∘ P = zT, and fix φ with T(φ) ≠ 0. Put h(t) := T(Γ_t φ).
Since t ↦ Γ_t φ is C^1 into C^∞ with derivative Γ_t(Pφ) = P(Γ_tφ) (joint smoothness of
(t,x) ↦ e^{J_t(x)}φ(g_t x); this is step 1 of Theorem J), h is C^1 and h'(t) = T(P Γ_t φ) =
z T(Γ_t φ) = z h(t). Hence h(t) = e^{zt} T(φ) and
  e^{Re z · t} |T(φ)| = |T(Γ_t φ)| ≤ ‖T‖_{(C^k)'} G_k(t) ‖φ‖_{C^k}
for every real t. Taking t → +∞ gives Re z ≤ γ_k^+, and t → −∞ gives Re z ≥ −γ_k^-. ∎

**Lemma 1.1 (identification of the band for k = 0, and an upper bound for general k).**
Let D^+ := max_m m(d) and D^- := min_m m(d), the maxima/minima over flow-invariant probabilities
(attained, since m ↦ m(d) is affine and weak*-continuous on a compact convex set). Let
  Λ_k := limsup_{|t| → ∞} (1/|t|) log max_x max_{1 ≤ j ≤ k} ‖D^j g_t(x)‖  (k ≥ 1), Λ_0 := 0.
Then
  (i) γ_0^+ = D^+ and γ_0^- = −D^-; consequently Σ_0 ⊂ { D^- ≤ Re z ≤ D^+ }.
  (ii) γ_k^+ ≤ D^+ + (k² + k) Λ_k and γ_k^- ≤ −D^- + (k² + k) Λ_k.
  (iii) In particular, if X preserves a smooth positive density ω (take ν = ω, d = 0) then
        Σ_0 ⊂ i R: **every eigen-distribution of order 0 has purely imaginary eigenvalue**, and more
        generally Σ_k ⊂ {|Re z| ≤ (k²+k) Λ_k}.

*Proof.* (i) G_0(t) = ‖e^{J_t}‖_∞ = exp(max_x J_t(x)), and the standard fact
limsup_{t→+∞}(1/t) max_x J_t(x) = max_m m(d) ([R4-q7] Prop. 2.1, step 1: the empirical measures of
near-maximizing orbit segments have invariant weak* limits, and conversely Birkhoff gives ≥) yields
γ_0^+ = D^+. Applying this to −X (whose divergence is −d and whose time-t log-Jacobian is J_{−t})
gives γ_0^- = max_m m(−d) = −D^-.

(ii) Write A_t := max(1, max_{1 ≤ j ≤ k} max_x ‖D^j g_t(x)‖), so A_t ≤ C_ε e^{(Λ_k + ε)|t|}. By the
chain rule, for |α| ≤ k, ∂^α(φ∘g_t) is a finite sum of terms (∂^β φ)∘g_t times products of at most
|β| ≤ k derivatives of g_t of orders summing to |α|; hence ‖φ∘g_t‖_{C^k} ≤ C_k ‖φ‖_{C^k} A_t^k.
Next, J_t = ∫_0^t d∘g_s ds, so ‖J_t‖_{C^k} ≤ |t| ‖d‖_{C^k} C_k max_{|s| ≤ |t|} A_s^k, and by the
Faà di Bruno/Leibniz formula ‖e^{J_t}‖_{C^k} ≤ e^{max J_t} C_k (1 + ‖J_t‖_{C^k})^k. Multiplying the
two estimates and using max_x J_t(x) ≤ C_ε + (D^+ + ε)t (t ≥ 0) gives
G_k(t) ≤ C_{k,ε} e^{(D^+ + ε)t} (1 + |t| e^{k(Λ_k+ε)|t|})^k A_t^k ≤ C'_{k,ε} e^{(D^+ + (k²+k)(Λ_k+ε) + ε)t},
whence the bound on γ_k^+. The backward bound is the same statement for −X.

(iii) Immediate from (i), (ii) with d = 0 (so D^± = 0). ∎

**Corollary 1.2 (what Lemma 1 does and does not give for (EF)).**
(a) (EF) holds for every strip Ω with a > γ_1^+ or b < −γ_1^-: there is simply no z ∈ Σ_1 there, so
T_z = 0 for every z (the hypothesis of (EF) that T_z has order ≤ 1 is used here).
(b) The families produced by Theorem R always live inside the band: their strip is
(λ + δ, λ + θ − δ) with λ = μ(d) ≤ D^+ and θ < χ^+_min ≤ Λ_1, so b < D^+ + Λ_1 ≤ γ_1^+ (by
Lemma 1.1(ii) with k = 1, the band is at least [−γ_1^-, D^+ + 2Λ_1]). **So Lemma 1 never applies to
the families coming from positive entropy.** It is a consistency check, plus the following
quantitative statement: any nonzero order-1 EF on a strip with right edge b forces
Λ_1 ≥ (b − D^+)/2, i.e. forces exponential growth of ‖Dg_t‖ when b > D^+. This is the exact
converse of the implication "positive entropy ⇒ Λ_1 > 0 ⇒ eigen-families exist" of Theorem R, and
it shows that any proof of (EF) must in particular contain a proof that GH forbids exponential
derivative growth (with the band interpretation: must push the whole band onto the imaginary axis).

*Proof of (a),(b).* (a) is Lemma 1 with k = 1. For (b): λ = μ(d) ≤ D^+, and θ < χ^+_min, while
χ^+_min ≤ max exponent ≤ Λ_1. ∎

---

## 2. Proposition 2: the sharpened target for strips touching the imaginary axis

For the core case of the chain (λ = μ(d) = 0, the case (PE0)) the strip produced by Theorem R is
(δ, θ − δ) for every small δ > 0, with the *same* family T_z (a Laplace transform of a fixed S);
so the family is holomorphic on Σ(0, θ) = {0 < Re z < θ} with order-1 bounds on closed substrips.
Hence the relevant case of (EF) is a = 0. Proposition 2 replaces it by a statement about a single
distribution, with a forward hypothesis weaker than the one in (J1).

**Statement (J1-0).** Assume GH. There is no nonzero distribution density S for which there exist
k, ε > 0 and C with
  (b−) |S(Γ_t φ)| ≤ C e^{−ε|t|} ‖φ‖_{C^k} for all t ≤ 0 and all φ ∈ C^∞(M);
  (f0) for every η > 0 there is C_η with |S(Γ_t φ)| ≤ C_η e^{η t} ‖φ‖_{C^k} for all t ≥ 0 and all φ.
("backward exponential decay, forward sub-exponential growth".)

**Proposition 2.** For a fixed smooth X on a compact M the following are equivalent.
 (i) For every b > 0 there is no nonzero family (T_z) on Σ(0,b) satisfying (i),(ii),(iii) of (EF)
     (holomorphy, local uniform order-1 bounds, eigen-relation).
 (ii) The statement (J1-0) holds, with "order ≤ k" allowed to be any finite order k.
Moreover (ii) ⟹ (i) already holds with k = 1 in (J1-0), and in (i) the order-1 requirement may be
replaced by order ≤ k throughout.

*Proof.* **(ii) ⟹ (i).** Let (T_z) satisfy (EF)(i)–(iii) on Σ(0,b) and suppose T_{z_0}(φ_0) ≠ 0 for
some z_0, φ_0. Fix a real c ∈ (0, b) with T_{c+iy}(φ_0) ≢ 0 in y (possible: if T_z(φ_0) vanished on
one vertical line it would vanish identically on Σ(0,b) by the identity theorem, contradicting
T_{z_0}(φ_0) ≠ 0; so every line works). For ω ∈ R put ρ_ω(z) := exp((z−c)² + ω(z−c)) and
  S_ω(φ) := (1/2πi) ∫_{Re z = c} ρ_ω(z) T_z(φ) dz.
On the line z = c + iy, |ρ_ω(c+iy)| = e^{−y²} and |T_{c+iy}(φ)| ≤ C_c ‖φ‖_{C^1} by (EF)(ii); so the
integral converges absolutely and S_ω is a distribution density of order ≤ 1 with
‖S_ω‖_{(C^1)'} < ∞. Exactly as in Theorem 2.1(B) of [R8-b] (which I re-checked line by line):
 • transport: by the computation in Lemma 1 above, T_z(Γ_t φ) = e^{zt} T_z(φ), so
   S_ω(Γ_t φ) = (1/2πi)∫_{Re z = c} ρ_ω(z) e^{zt} T_z(φ) dz;
 • contour shift: for 0 < a' < c < b' < b the integrand is holomorphic on a' ≤ Re z ≤ b' and, by
   (EF)(ii) on that closed substrip together with the Gaussian factor
   |ρ_ω(σ+iy)| = e^{(σ−c)² − y² + ω(σ−c)}, it is O(e^{−y²/2}) uniformly for σ ∈ [a',b'] (t fixed).
   Cauchy's theorem lets us move the line to Re z = b' (use for t ≤ 0) or to Re z = a' (use for
   t ≥ 0), giving
   |S_ω(Γ_t φ)| ≤ K_{b'} e^{b' t} ‖φ‖_{C^1} (t ≤ 0),  |S_ω(Γ_t φ)| ≤ K_{a'} e^{a' t} ‖φ‖_{C^1} (t ≥ 0),
   with K_σ := (1/2π) ∫ |ρ_ω(σ+iy)| C_{[a',b']} dy < ∞. The first bound with a fixed b' ∈ (0,b) is
   (b−) with ε = b'; the second, as a' ranges over (0, c), is exactly (f0) (the constants K_{a'}
   are allowed to blow up as a' ↓ 0).
 • nonvanishing: h(y) := T_{c+iy}(φ_0) is continuous, bounded and ≢ 0, and
   S_ω(φ_0) = (1/2π) ∫ e^{−y²} e^{iωy} h(y) dy is the Fourier transform at −ω of the nonzero
   continuous L^1 function e^{−y²}h; by Fourier uniqueness it is ≠ 0 for some ω.
Taking the real or imaginary part of such an S_ω (both satisfy the same bounds, and one of them is
nonzero) contradicts (J1-0) with k = 1.

**(i) ⟹ (ii).** Let S ≠ 0 satisfy (b−) and (f0) with order k and backward rate ε. For each
η ∈ (0, ε) put T_z(φ) := ∫_R e^{−zt} S(Γ_t φ) dt on Σ(η, ε). By (b−),(f0) the integral converges
absolutely and locally uniformly there (the exponents are −(Re z − η)t for t ≥ 0 and
−(ε − Re z)|t| for t ≤ 0), so z ↦ T_z(φ) is holomorphic with
|T_z(φ)| ≤ (C_η/(Re z − η) + C/(ε − Re z)) ‖φ‖_{C^k}. Since F_φ(t) := S(Γ_tφ) is C^1 with
F_φ' = F_{Pφ} and the same bounds hold for Pφ, integration by parts over [−R,R] (boundary terms
→ 0) gives T_z(Pφ) = z T_z(φ). The definition of T_z does not depend on η, so (T_z) is a family on
Σ(0, ε) satisfying (EF)(i)–(iii) with order k. By (i) it vanishes identically; but then, as in step 3
of Theorem 2.1(A) of [R8-b],
  E(z) := ∫_{−∞}^0 e^{−zt}F_φ dt (Re z < ε) and E(z) := −∫_0^∞ e^{−zt}F_φ dt (Re z > 0)
agree on the strip, hence define an entire function which is bounded (by the two one-sided bounds,
split at Re z = ε/2) and tends to 0 along the negative real axis (dominated convergence on t ≤ 0);
so E ≡ 0 by Liouville. Then y ↦ ∫_{−∞}^0 e^{−iyt}F_φ(t)dt ≡ 0, so the L^1 function F_φ·1_{(−∞,0]}
vanishes a.e.; F_φ is continuous, so S(φ) = F_φ(0) = 0 for every φ, i.e. S = 0, a contradiction. ∎

**Remark 2.1.** (J1-0) is weaker than the planner's (J1) (whose forward hypothesis is
|F_φ(t)| ≤ Ce^{at}, a > 0 fixed), because its hypothesis on S is stronger. By Proposition 2 and
Theorem R it is nevertheless enough for the core case: **(J1-0) ⟹ no ergodic measure with
μ(d) = 0 has positive entropy** (take the pair family of Theorem R with λ = 0: its strip is
Σ(0,θ)). For ergodic measures with μ(d) ≠ 0 the strip of Theorem R is
(λ+δ, λ+θ−δ) and does not touch 0, so those cases need the full (EF) (equivalently (J1) for X and
for −X, by Theorem 2.1 of [R8-b]); several of them are already excluded by Prop. 6.1 of [R6-a] and
Proposition N of [R7-c].

---

## 3. Lemma 3: geometric divisibility by P^T is harmless (no GH)

This closes a line that looks promising at first sight: the Taylor coefficients of the backward
Laplace transform give a *geometrically bounded* sequence of "divisors" of S by the transpose of P,
and one might hope to iterate them against the tame estimates. Lemma 3 says exactly what that
iteration yields, and it is not a contradiction.

**Lemma 3.** Let S be a distribution density, k ≥ 0, θ > 0, C with
|S(Γ_t φ)| ≤ C e^{−θ|t|} ‖φ‖_{C^k} for all t ≤ 0 and all smooth φ. Put
  B_j(φ) := ∫_{−∞}^0 ((−t)^j / j!) S(Γ_t φ) dt  (j ≥ 0).
Then:
 (a) B_j is a distribution density of order ≤ k with ‖B_j‖_{(C^k)'} ≤ C θ^{−j−1};
 (b) B_0 ∘ P = S and B_j ∘ P = B_{j−1} (j ≥ 1); hence S = B_{n−1} ∘ P^n for every n ≥ 1 and
     |S(φ)| ≤ C θ^{−n} ‖P^n φ‖_{C^k} for all n ≥ 1 and all smooth φ.
 (c) Consequently S(φ) = 0 for every smooth φ with liminf_n ‖P^n φ‖_{C^k}^{1/n} < θ.
 (d) The same with P − w in place of P, for every complex w with Re w < θ: with
     B_j^w(φ) := ∫_{−∞}^0 e^{−wt}((−t)^j/j!) S(Γ_tφ) dt one gets ‖B_j^w‖ ≤ C (θ − Re w)^{−j−1},
     B_0^w ∘ (P−w) = S, B_j^w ∘ (P−w) = B^w_{j−1}, hence
     |S(φ)| ≤ C (θ − Re w)^{−n} ‖(P−w)^n φ‖_{C^k}.
No hypothesis on X beyond smoothness is used; in particular GH is not used.

*Proof.* (a) |B_j(φ)| ≤ C‖φ‖_{C^k} ∫_0^∞ (t^j/j!) e^{−θt} dt = C θ^{−j−1} ‖φ‖_{C^k}.
(b) F_φ(t) := S(Γ_tφ) is C^1 with F_φ' = F_{Pφ} (as in Lemma 1). For j = 0,
B_0(Pφ) = ∫_{−∞}^0 F_φ'(t)dt = F_φ(0) − lim_{t→−∞}F_φ(t) = S(φ), the limit being 0 by the decay
hypothesis. For j ≥ 1, integrating by parts on [−R, 0],
∫_{−R}^0 ((−t)^j/j!) F_φ'(t)dt = [((−t)^j/j!)F_φ]_{−R}^0 + ∫_{−R}^0 ((−t)^{j−1}/(j−1)!)F_φ dt;
the boundary term at t = 0 vanishes because j ≥ 1, the one at −R tends to 0 by the decay. So
B_j ∘ P = B_{j−1}. Iterating, S = B_0 ∘ P = B_1 ∘ P² = … = B_{n−1} ∘ P^n, and the estimate follows
from (a).
(c) If liminf ‖P^nφ‖^{1/n} = r < θ, pick n_i → ∞ with ‖P^{n_i}φ‖_{C^k} ≤ (r')^{n_i} for some
r < r' < θ; then |S(φ)| ≤ C θ^{−n_i}(r')^{n_i} → 0.
(d) Identical computation; the decay of e^{−wt}F_φ(t) as t → −∞ is e^{(Re w − θ)|t|}. ∎

**Why this is a dead end (and why Theorem V of [R7-e] had to use the inverse of P).**
P is a first-order differential operator, so ‖P^nφ‖_{C^k} typically grows factorially in n; the set
Q_θ := {φ : liminf ‖P^nφ‖_{C^k}^{1/n} < θ} is a "low-frequency" set, never C^1-dense. Example: on
T^1 with X = ∂_x, ν = Lebesgue (d = 0, P = X), for φ = e^{imx} one has ‖P^nφ‖_{C^k} ≍ |m|^{n+k},
so liminf ‖P^nφ‖^{1/n} = |m|, and Q_θ is contained in the span of the modes with |m| < θ, plus
limits — a finite-dimensional-type set, certainly not dense. Thus Lemma 3(c) is consistent with
S ≠ 0 and gives no contradiction. To contradict S ≠ 0 one needs the opposite divisibility, i.e.
estimates of the form |S(φ)| ≤ C r^{−n} ‖R^n φ‖ with R a (tame) *inverse* of P, since then the
smoothing of R can beat r^{−n}. By Proposition A of [R8-d] a tame inverse of P exists only in the
volume case (V), and in that case Theorem V of [R7-e] shows precisely what is still missing
(quasi-analytic growth of ‖R^Nφ‖_{C^1} on a C^1-dense set). Lemma 3 shows that nothing is gained by
re-running the argument in the "forward" direction, for any choice of the base point w in the strip.

---

## 4. The obstruction in the abstract (EF) setting

Earlier rounds located the obstruction using the concrete S = δ_x − e^b δ_y (chain starting at S,
[R8-c] §3). The following shows it is intrinsic to (EF): the Abel/Patterson means of an *abstract*
family produce a Jordan chain whose inhomogeneous term is a distribution of the same (generally
non-smooth) nature as S, so (F1)+(F2) cannot be bootstrapped.

**Proposition 4.1 (proved).** Let (T_z) be a family on Σ(0,b) as in (EF) (holomorphy, order-1
bounds on closed substrips, T_z ∘ P = z T_z), let S be one of the distributions S_ω produced from it
in the proof of Proposition 2 (so S ≠ 0 for a suitable ω, S has order ≤ 1, S satisfies (b−) with
rate ε = b' and (f0)), and for s > 0 put
  W_s(φ) := s ∫_0^∞ e^{−st} S(Γ_t φ) dt.
Then:
 (a) W_s is a distribution density of order ≤ 1, well defined for every s > 0 by (f0), and
     W_s ∘ P = s W_s − s S.
 (b) If ‖W_{s_n}‖_{(C^1)'} is bounded for some sequence s_n ↓ 0, then every weak* limit W of
     (W_{s_n}) satisfies W ∘ P = 0, hence (under GH, by (F1)) W = c ν for a constant c.
 (c) If in addition ‖(W_{s_n} − cν)/s_n‖_{(C^1)'} is bounded, then every weak* limit V of that
     sequence satisfies V ∘ P = c ν − S, i.e. the generalized function v = V/ν solves
     X v = (S − cν)/ν.
 (d) Under GH, (c) forces (S − cν)/ν to be smooth. Hence: **if the family (EF) is nonzero and the
     two normalizations in (b),(c) are bounded, then S agrees with cν plus a smooth density.**
     Conversely, for the families of Theorem R, S is (a Gaussian average of Laplace transforms of)
     a difference of two Dirac masses and is *not* of that form, so the boundedness assumptions in
     (b) or (c) must fail — which is exactly the Patterson blow-up of [R8-c], Cor. 2.3.

*Proof.* (a) Convergence: by (f0) with η = s/2, |S(Γ_tφ)| ≤ C_{s/2} e^{st/2}‖φ‖_{C^1}, so the
integral converges absolutely; the order bound is immediate. For the relation, use F_φ' = F_{Pφ}
and integrate by parts on [0,R]:
s∫_0^R e^{−st}F_{Pφ} dt = s[e^{−st}F_φ]_0^R + s² ∫_0^R e^{−st}F_φ dt; the boundary term at R tends
to 0 (again by (f0) with η = s/2), and at 0 it equals −sF_φ(0) = −sS(φ). This gives
W_s(Pφ) = −sS(φ) + sW_s(φ).
(b) Along a subsequence with bounded (C^1)'-norms, Banach–Alaoglu (or Banach–Steinhaus plus the
separability of C^1(M)) gives a weak* limit W in (C^1)'; passing to the limit in (a),
W(Pφ) = 0·W(φ) − 0·S(φ) = 0. By (F1) (which is GH through L1), W = cν.
(c) ν ∘ P = 0 because ∫ Pφ dν = ∫ L_X(φν) = 0. So, with V_s := (W_s − cν)/s,
V_s ∘ P = (1/s) W_s ∘ P = W_s − S = cν − S + s V_s. Taking weak* limits along a subsequence where
‖V_{s_n}‖ is bounded, and using s_n V_{s_n} → 0 in (C^1)' (norms bounded, s_n → 0), gives
V ∘ P = cν − S.
(d) X v = (S − cν)/ν with the convention ⟨Xv, φν⟩ = −V(Pφ); if the right-hand side is smooth, GH
makes v smooth, which is a statement about S, not a contradiction — hence the assertion as stated.
For the concrete families: S = S_ω is a Gaussian-weighted contour average of
T_z = Laplace transform of t ↦ δ_x(Γ_t·) − e^bδ_y(Γ_t ·); by the computation in Theorem 2.1(B) it is
a (complex) measure-plus-order-1 object concentrated on the single orbit closure of {x,y} and in
particular it is not of the form cν + (smooth density) unless it vanishes (such an S has, e.g.,
non-zero restriction to a ν-null set in the examples). ∎

**What Proposition 4.1 says.** The only mechanism by which GH has ever been made to act — the
Jordan chain at z = 0 coming from the moments of the transport, i.e. (F1)+(F2) — closes only when
the chain is homogeneous. In the two-sided situation (Theorem J) it is homogeneous because all the
moments ∫ t^j F_φ dt exist. In the one-sided situation of (EF) with a ≥ 0 the chain is inhomogeneous
with inhomogeneity S itself, and GH can be applied to it only if S is smooth modulo ν. This is the
same wall as in [R8-c] §3 and [R8-e] §2, now established without any reference to the geometric
origin of S. Making S smooth would require smearing the pair of Theorem R into an absolutely
continuous family with smooth density, which needs (at least) absolute continuity and smoothness of
the Pesin unstable lamination — unavailable.

---

## 5. Open questions (explicit)

1. **(EF)** itself, in the generality of the brief: a nonzero holomorphic family of order-≤1
   eigen-densities of P^T, locally bounded on closed substrips, over an open vertical strip
   Ω ⊂ {Re z ≠ 0}. Open. Equivalently (Theorem 2.1 of [R8-b]) the statement (J1) for X and for −X.
2. **(J1-0)** (Section 2): the special case of (EF) for strips with a = 0, equivalently
   "no nonzero finite-order S with backward exponential decay and forward sub-exponential growth of
   the weighted transport". Open; by Proposition 2 and Theorem R it suffices for the core case
   μ(d) = 0 (which contains the volume-preserving case and the old core (PE0)).
3. **(V)**: does GH imply the existence of a smooth invariant volume? Open (equivalent by
   Proposition A of [R8-d] to closedness of P(C^∞), and by Proposition B to dim I = 1). A positive
   answer would make the weighted and unweighted pictures coincide and would let the tame
   (closed-range) half of GH act on the Jordan chain; by Theorem V of [R7-e] one would then still
   need quasi-analytic growth of ‖R^Nφ‖_{C^1} on a C^1-dense set of φ.
4. **Quantitative tameness**: does GH give a tame estimate with uniform derivative loss and
   geometric constants (‖R φ‖_{C^k} ≤ C B^k ‖φ‖_{C^{k+σ}} with σ fixed)? By Lemma Q of [R8-a] and
   Theorem V this is exactly what is missing in the volume case. Open; GH is obtained from the
   closed graph theorem, which gives no growth information.
5. **Smearing**: is there a nonzero *absolutely continuous* S with smooth density whose weighted
   transport decays backwards exponentially and grows forwards sub-exponentially, in the presence of
   a positive-entropy measure? By Proposition 4.1(d) such an S would let GH act directly. Open (and
   presumably false in general, because the Pesin lamination is only measurable).

---

## 7. Theorem A: (EF) reduces to a **single-point** Jordan-chain exclusion

This is the main new result of this file. It strictly improves Propositions 3.1 and 3.2 of [R8-b]
("the set of z admitting an order-k Jordan chain has empty interior") to "**one** point of the strip
admits no order-k Jordan chain", and it exhibits Theorem J as the special case c = 0 of a general
principle: *the moment/Jordan argument of Theorem J can be run at any point c of the strip, after
renormalizing the transport by e^{−ct}; GH enters only through the exclusion of a Jordan chain of
length 2 at that single point c.*

**Definition.** For c ∈ C and k ≥ 0, say that *c admits an order-k Jordan chain (of length 2)* if
there are distribution densities A, B of order ≤ k with B ≠ 0,
  B ∘ (P − c) = 0 and A ∘ (P − c) = B,
i.e. (with b = B/ν, α = A/ν) X b = −c b, b ≠ 0, X α = −c α − b.

**Theorem A.** Let X be a smooth vector field on a compact manifold M (GH is used only through the
hypothesis below), let a < b be real, Ω = Σ(a,b) = {a < Re z < b}, and let (T_z)_{z ∈ Ω} be
distribution densities such that
 (i) z ↦ T_z(φ) is holomorphic on Ω for every φ ∈ C^∞(M);
 (ii) for every closed substrip a < a_1 ≤ Re z ≤ b_1 < b, sup{ |T_z(φ)| : a_1 ≤ Re z ≤ b_1,
      ‖φ‖_{C^k} ≤ 1 } < ∞ (some fixed k; k = 1 in (EF));
 (iii) T_z ∘ P = z T_z on Ω.
Suppose that **some single point c ∈ Ω** does not admit an order-k Jordan chain. Then T_z = 0 for
every z ∈ Ω.

*Proof.* Suppose T ≠ 0. Fix c ∈ Ω as in the hypothesis and put σ := Re c ∈ (a,b); choose ρ > 0 with
[σ − ρ, σ + ρ] ⊂ (a,b), and set a' := σ − ρ, b' := σ + ρ.

**Step 1 (a renormalized two-sided decaying transport).** Exactly as in the proof of Proposition 2
(the Gaussian contour construction, Theorem 2.1(B) of [R8-b]), with the contour Re z = σ, there is
ω ∈ R such that S := S_ω,
  S(φ) := (1/2πi) ∫_{Re z = σ} exp((z−σ)² + ω(z−σ)) T_z(φ) dz,
is a nonzero distribution density of order ≤ k, and (shifting the contour to Re z = b' for t ≤ 0 and
to Re z = a' for t ≥ 0, which is legitimate by (i),(ii) and the Gaussian decay of the weight)
  |F_φ(t)| ≤ K e^{b' t} ‖φ‖_{C^k} (t ≤ 0),   |F_φ(t)| ≤ K e^{a' t} ‖φ‖_{C^k} (t ≥ 0),
where F_φ(t) := S(Γ_t φ). (Non-vanishing: pick φ_0, z_0 with T_{z_0}(φ_0) ≠ 0; then
h(y) := T_{σ+iy}(φ_0) is continuous, bounded and ≢ 0 by the identity theorem, and
S_ω(φ_0) = (1/2π)∫ e^{−y²} e^{iωy} h(y) dy is the Fourier transform at −ω of a nonzero continuous
L^1 function, hence ≠ 0 for some ω.)

Put H_φ(t) := e^{−ct} F_φ(t). Then
  |H_φ(t)| ≤ K e^{−ρ|t|} ‖φ‖_{C^k} for all t ∈ R and all smooth φ,   (7.1)
because |e^{−ct}| = e^{−σt}. Moreover t ↦ Γ_tφ is C^1 into C^∞ with (d/dt)Γ_tφ = Γ_t(Pφ), so F_φ is
C^1 with F_φ' = F_{Pφ}, and therefore
  H_φ'(t) = e^{−ct}(F_{Pφ}(t) − c F_φ(t)) = H_{(P − c)φ}(t).   (7.2)

**Step 2 (moments and the Jordan relations).** For j ≥ 0 put m_j(φ) := ∫_R t^j H_φ(t) dt. By (7.1)
the integral converges absolutely and |m_j(φ)| ≤ K ‖φ‖_{C^k} ∫ |t|^j e^{−ρ|t|} dt, so each m_j is a
distribution density of order ≤ k. By (7.2), applied also to (P−c)φ (which satisfies (7.1) with
‖(P−c)φ‖_{C^k} in place of ‖φ‖_{C^k}), t^j H_φ(t) → 0 as |t| → ∞ and all integrals below converge
absolutely; integrating by parts on [−R,R] and letting R → ∞,
  m_0((P−c)φ) = ∫_R H_φ'(t) dt = 0,   m_j((P−c)φ) = −j m_{j−1}(φ)  (j ≥ 1).   (7.3)

**Step 3 (induction, using the hypothesis at c).** From (7.3) with j = 0,1:
m_0 ∘ (P−c) = 0 and (−m_1) ∘ (P−c) = m_0. If m_0 ≠ 0, then (A,B) = (−m_1, m_0) is an order-k Jordan
chain at c, contrary to the hypothesis. So m_0 = 0. Assume m_{j−1} = 0 for some j ≥ 1. Then by (7.3)
m_j ∘ (P−c) = 0 and (−m_{j+1}/(j+1)) ∘ (P−c) = m_j, so the same argument gives m_j = 0. By induction
m_j = 0 for every j ≥ 0.

**Step 4 (quasi-analyticity).** Fix φ. By (7.1), G(ξ) := ∫_R e^{−iξt} H_φ(t) dt converges and is
holomorphic on the strip |Im ξ| < ρ, with G^{(j)}(0) = (−i)^j m_j(φ) = 0 for all j. Hence G ≡ 0 on
the strip, in particular on R; H_φ ∈ L^1 ∩ C^0 with vanishing Fourier transform, so H_φ ≡ 0, and
S(φ) = H_φ(0) = 0. As φ was arbitrary, S = 0, contradicting Step 1. Therefore T ≡ 0. ∎

**Remarks.**
1. **c = 0 is Theorem J.** If 0 ∈ Ω one may take c = 0; under GH, 0 admits no Jordan chain: B∘P = 0
   gives B = cν by (F1) = (K0), and then A ∘ P = cν forces c = 0 by (F2) = (K1), i.e. B = 0. So
   Theorem A contains Lemma M / Theorem J (for strips through 0) and shows that the two facts
   (K0),(K1) are used *only at the single spectral point 0*.
2. **Strict improvement of [R8-b], Props. 3.1–3.2.** Those propositions require that the set of z
   admitting an order-k eigen-density (resp. an order-k Jordan chain) have empty interior in the
   half-plane. Theorem A requires only that *one* point of the given strip be free of Jordan chains.
   In particular Σ_k may be the whole strip minus one point and (EF) still holds there.
3. **c need not be real**, and need not be a zero of z ↦ T_z(φ_0).
4. The hypothesis can be weakened further to: "there is no *infinite geometric* chain at c", i.e. no
   sequence (A_j)_{j ≥ 0} of order-≤k densities with A_0 ≠ 0, A_0∘(P−c) = 0, A_j∘(P−c) = A_{j−1}
   and ‖A_j‖_{(C^k)'} ≤ C r^{−j} for some r > 0. Indeed Step 3 only needs the chain (m_j) to be
   killed, and ‖m_j‖ ≤ K j! ρ^{−j−1} … — more precisely, conversely, a nonzero family on the disc
   |z − c| < r *is the same thing* as such an infinite geometric chain: given (A_j), the series
   T_z := Σ_j (z−c)^j A_j converges for |z−c| < r and satisfies T_z ∘ (P − c) = (z−c)T_z, i.e.
   T_z ∘ P = z T_z; and conversely A_j := T^{(j)}_c/j! satisfies the chain relations with Cauchy
   bounds. So:
   **(EF) on Ω ⟺ no point c ∈ Ω carries a nonzero infinite geometric order-k Jordan chain**, and by
   Theorem A it is enough to kill the *first two* terms of the chain at one point.

**Corollary 7.1 (the problem reduced to a pointwise statement).** Assume GH, and suppose
  (JC) for every c ∈ C with Re c ≠ 0 lying in one of the strips produced by Theorem R, there are no
      distribution densities A, B of order ≤ 1 with B ≠ 0, X(B/ν) = −c(B/ν), X(A/ν) = −c(A/ν) − B/ν
      — it suffices to have *one* such c in each of those strips.
Then every ergodic flow-invariant probability has zero entropy and h_top(g_1) = 0.

*Proof.* If some ergodic μ has h_μ(g_1) > 0, Theorem R gives a nonzero family (T_z) of order ≤ 1 on
Ω = Σ(λ+δ, λ+θ−δ) satisfying (i)–(iii) of Theorem A with k = 1. If 0 ∈ Ω, Remark 1 above (i.e.
Theorem J) gives T ≡ 0; otherwise Ω ⊂ {Re z ≠ 0} and (JC) supplies a point c ∈ Ω with no order-1
Jordan chain, so Theorem A gives T ≡ 0. Either way we contradict the non-vanishing in Theorem R.
Hence h_μ(g_1) = 0 for every ergodic flow-invariant μ, and the variational step (step 1 of the
chain) gives h_top(g_1) = 0. ∎

**Corollary 7.2 (contrapositive; a strengthening of the known consequences of positive entropy).**
If X is any smooth field with an ergodic measure of positive entropy, then for the strip Ω of
Theorem R, **every** c ∈ Ω admits an order-1 Jordan chain (not merely every c off a discrete set is
in Σ_1). Indeed, apply Theorem A: if some c ∈ Ω had no chain, the family would vanish identically,
contradicting its non-vanishing.

**What is still missing after Theorem A (precisely).** One must exclude, for at least one point c of
a given strip with Re c ≠ 0, the pair of equations
  X b = −c b (b ≠ 0, order ≤ 1), X α = −c α − b (order ≤ 1).
GH does this at c = 0 by (K0) and (K1). At c ≠ 0 the obstruction identified in Remark 3.3 of [R8-b]
persists: the right-hand sides are not smooth, so GH cannot be applied directly, and the smooth
version of the statement (which *is* provable: at a maximum of |b|², X|b|² = −2 Re c |b|² forces
b = 0 when Re c ≠ 0) is unavailable for distributions. Two things that Theorem A newly makes
available, and that I could not exploit:
 (a) one is free to choose c anywhere in the strip, in particular at points where extra information
     might hold (e.g. c with Re c = max_m m(d), or c not of the form μ(d) for any ergodic μ, or c
     off the countable set of "tilted conformal" eigenvalues);
 (b) by Corollary 7.2 a counterexample must have Jordan chains at *every* point of a two-dimensional
     open set, with holomorphic dependence — an uncountable, analytically parametrized family of
     non-smooth eigen-distributions of order 1, all with wavefront sets inside the characteristic set
     {ξ : ξ(X) = 0} and invariant under the lifted flow (standard propagation of singularities for
     the first-order operator X + c, whose principal symbol does not depend on c). I record the
     wavefront remark as an observation only: it is the same for all c, so by itself it does not
     separate c = 0 from c ≠ 0.

### 7.1 A case where the Jordan chain *can* be excluded (proved; no GH)

Theorem A is not vacuous: here is a growth criterion that kills chains outright, and a genuine
consequence of it. Recall G_k(t) = ‖Γ_t‖_{C^k → C^k} and γ_k^± from Section 1.

**Proposition 7.3.** Let c ∈ C. If
  liminf_{t → +∞} G_k(t) e^{−(Re c)t} / t = 0  or  liminf_{t → +∞} G_k(−t) e^{(Re c)t} / t = 0,
then c admits no order-k Jordan chain. (In particular this holds whenever Re c ≥ γ_k^+ and
G_k(t) = o(t e^{γ_k^+ t}), or symmetrically on the backward side.)

*Proof.* Let (A,B) be a chain at c: B ≠ 0, B ∘ (P−c) = 0, A ∘ (P−c) = B. Fix φ with B(φ) ≠ 0. As in
Lemma 1, h_B(t) := B(Γ_tφ) satisfies h_B' = c h_B, so h_B(t) = e^{ct}B(φ); and
h_A(t) := A(Γ_tφ) satisfies h_A'(t) = A(P Γ_t φ) = c h_A(t) + B(Γ_t φ) = c h_A(t) + e^{ct}B(φ),
whence h_A(t) = e^{ct}(A(φ) + t B(φ)). Therefore
  |A(φ) + t B(φ)| e^{(Re c)t} = |A(Γ_tφ)| ≤ ‖A‖_{(C^k)'} G_k(t) ‖φ‖_{C^k},
so |t| |B(φ)| ≤ |A(φ)| + ‖A‖ ‖φ‖_{C^k} G_k(t) e^{−(Re c)t} for all real t. Dividing by |t| and using
either hypothesis along a sequence gives B(φ) = 0, a contradiction. ∎

**Corollary 7.4 (proved).** Suppose X preserves a smooth positive density ω and take ν = ω (so
d = 0, J ≡ 0, Γ_t φ = φ ∘ g_t, G_0(t) ≡ 1). Then no c ∈ C admits an order-0 Jordan chain, and
consequently (Theorem A) **there is no nonzero family (T_z) of complex measures on any open vertical
strip with T_z ∘ P = z T_z, holomorphic and locally bounded in total variation**. No GH is needed.
Combined with Lemma 1.1(iii) (Σ_0 ⊂ iR in the volume case) this completely settles the order-0 case
of (EF) for volume-preserving fields.

*Proof.* G_0(t) ≡ 1 = o(t), so Proposition 7.3 applies at every c with Re c ≥ 0 (forward hypothesis)
— and at every c (the forward hypothesis alone already covers all c, since e^{−(Re c)t}/t → 0 for
Re c > 0, while for Re c ≤ 0 one uses the backward hypothesis G_0(−t)e^{(Re c)t}/t = e^{(Re c)t}/t
→ 0). Then apply Theorem A with k = 0 on any strip. ∎

**Scope (honest).** Corollary 7.4 does not help with the problem, because the families produced by
Theorem R have genuine order 1 (the pair construction loses one derivative: the bound involves
‖φ‖_{C^1}), and for k = 1 the band is wide: γ_1^+ ≥ Λ_1 > 0 as soon as the flow has exponential
derivative growth, while the strips of Theorem R sit strictly inside the band (Corollary 1.2(b)).
Proposition 7.3 therefore never applies to them. It is recorded to show that the single-point
criterion of Theorem A is usable, and to isolate the exact quantity — the growth of
‖Γ_t‖_{C^1 → C^1} relative to e^{(Re c)t} — that would have to be controlled.

**Updated list of open questions.** Replace item 1 of Section 5 by the sharper
  1'. **(JC)**: under GH, exhibit in each strip of Theorem R one point c with Re c ≠ 0 carrying no
      order-1 Jordan chain of P^T (equivalently, by Remark 4 above, no infinite geometric chain).
      This is now the only missing input of the whole chain. By Theorem A it is a *pointwise*
      statement about the transposed operator at a single spectral point, and it is the exact
      analogue at c ≠ 0 of (K0) ∧ (K1) at c = 0.
Items 2–5 of Section 5 remain as stated; item 2 ((J1-0)) remains the natural target for the core
case μ(d) = 0, where one may also take c in the strip as close to 0 as one likes — note that
Theorem A allows c → 0, but the hypothesis "no Jordan chain at c" is *not* known to be stable as
c → 0, which is precisely the discontinuity that the Patterson blow-up of [R8-c] Cor. 2.3 embodies.

### Block R9-c (from round9_q1 §1: order-0 Jordan chains force total dissipativity)
## 1. Order-0 Jordan chains force total dissipativity (PROVED; no GH used)

**Lemma 1.1.** Let z = kappa + i y in C, and let B != 0 and A be complex Borel measures on M with
 B(P phi) = z B(phi),  A(P phi) = z A(phi) + B(phi)  for all smooth phi.
Let beta := |B| (total variation). Then for beta-a.e. x,
 I_kappa(x) := int_R e^{J_t(x) - kappa t} dt < infinity.
In particular beta gives no mass to zeros of X or to periodic orbits.

*Proof.*
(a) Transport identities. For smooth phi, h(t) := A(Q_t phi) is C^1 (t -> Q_t phi is C^1 into C^0) with
h'(t) = A(P Q_t phi) = z h(t) + B(Q_t phi), and likewise B(Q_t phi) = e^{zt} B(phi). Hence
A(Q_t phi) = e^{zt}(A(phi) + t B(phi)). Both sides are C^0-continuous in phi (Q_t is bounded on C^0), so the
identities hold for continuous phi, i.e. L_t B = e^{zt} B and L_t A = e^{zt}(A + tB) as measures, and then for
bounded Borel phi.
(b) Elementary properties of L_t: it is positive, |L_t m| = L_t |m| (g_t is a Borel bijection and e^{J_t} > 0), it
preserves absolute continuity and mutual singularity, and if m = k n with k in L^1(n) then
L_t m = (k o g_{-t}) L_t n (direct change of variables).
(c) Polar part. By (b), L_t beta = |L_t B| = e^{kappa t} beta. Write B = h beta, |h| = 1. Then
L_t B = (h o g_{-t}) e^{kappa t} beta = e^{zt} h beta, so h o g_{-t} = e^{iyt} h beta-a.e., for each t.
(d) Lebesgue decomposition of A. Write A = k beta + A_s with A_s singular to beta. By (b),
L_t A = (k o g_{-t}) e^{kappa t} beta + L_t A_s, and L_t A_s is singular to L_t beta = e^{kappa t} beta. Comparing with
e^{zt}(A + tB) = e^{zt}(k + t h) beta + e^{zt} A_s and using uniqueness of the Lebesgue decomposition:
k o g_{-t} = e^{iyt}(k + t h) beta-a.e. Put q := k/h. By (c), q o g_{-t} = q + t beta-a.e., for each real t.
Let r := Re q (a real Borel function, defined beta-a.e.; fix a Borel version). Then for each t:
 r(g_{-t} x) = r(x) + t for beta-a.e. x.   (1.1)
(e) Integrability. Let E := {r in [0,1)} and, for n in Z, E_n := {r in [n, n+1)}. For each t, by (1.1),
g_t E = {x : r(g_{-t}x) in [0,1)} coincides beta-a.e. with {r in [-t, 1-t)}. Using L_t beta = e^{kappa t} beta
with the bounded Borel function 1_E o g_{-t}:
 int e^{J_t} 1_E dbeta = int e^{J_t} (1_E o g_{-t}) o g_t dbeta = e^{kappa t} int 1_E o g_{-t} dbeta = e^{kappa t} beta(g_t E).
By Tonelli,
 int_E I_kappa dbeta = int_R e^{-kappa t} int e^{J_t} 1_E dbeta dt = int_R beta(r in [-t, 1-t)) dt
  = int ( int_R 1{-r(x) <= t < 1 - r(x)} dt ) dbeta(x) = beta(M) < infinity.
(Joint measurability of (t,x) -> e^{J_t(x)} 1_E(x) is clear.) Hence I_kappa < infinity beta-a.e. on E. The same
computation with E_n (replace [0,1) by [n,n+1)) gives I_kappa < infinity beta-a.e. on each E_n, and the E_n cover
a beta-conull set. Finally, at a zero p, J_t(p) = t d(p) and I_kappa(p) = infinity; on a periodic orbit of
period T, J_{t+T} = J_t + J_T(x) and again I_kappa = infinity. ∎

**Corollary 1.2 (GH, dim M >= 2).** (i) There is no order-0 Jordan chain (A, B as in Lemma 1.1) at any z in iR.
(ii) For real kappa != 0, the set N_kappa := {x : I_kappa(x) < infinity} is nu-null, so in an order-0 Jordan chain
at z with Re z != 0, |B| is singular to nu and carried by N_{Re z}.
(iii) If X preserves a smooth positive density (statement (V)), there is no order-0 Jordan chain at any z, hence
no nonzero order-0 eigen-family on any strip.
*Proof.* (i) kappa = 0: Lemma C of the background (GH) says I_0(x) = int e^{J_t(x)} dt = infinity for every x.
(ii) For kappa > 0, I_kappa(x) >= int_{-inf}^0 e^{J_t(x)} dt, which is infinite nu-a.e. by B4 (backward); for
kappa < 0 use the forward half of B4. (iii) Take nu invariant, so d = 0, J = 0 and I_kappa = infinity everywhere.
For the eigen-family statement: if T_z is a nonzero EF of order 0 (bounded in total variation on closed substrips),
then T'_z(phi) = (2 pi i)^{-1} oint T_w(phi)(w-z)^{-2} dw is again a measure, and differentiating T_z o P = z T_z
gives T'_z o P = z T'_z + T_z; at any z with T_z != 0 this is an order-0 Jordan chain. ∎

**Corollary 1.3 (structure; PROVED modulo standard measurable cross-section bookkeeping).** In Lemma 1.1, B is a
superposition of single-orbit Laplace transforms: there are a Borel set Sigma meeting beta-a.e. orbit once, a
finite measure eta on Sigma and a bounded Borel c on Sigma with
 B(phi) = int_Sigma c(sigma) int_R e^{J_s(sigma) - z s} phi(g_s sigma) ds deta(sigma).
(Sketch: Sigma = {r = 0} via x -> g_{r(x)} x; beta is quasi-invariant (L_t beta = e^{kappa t} beta), so its
orbit-disintegration is equivalent to Lebesgue in the time parameter; the identity L_t beta = e^{kappa t} beta forces
the time density on the orbit of sigma to be const(sigma) e^{J_s(sigma) - kappa s}; the phase is h(g_s sigma) =
e^{-iys} h(sigma) by (c).)

*Scope.* This settles order-0 Jordan chains on the imaginary axis and reduces order-0 eigen-families to single
orbits with int e^{J_t - kappa t} dt < infinity, kappa != 0. It does NOT touch the families of Theorem R: those are
genuinely of order 1 (for no z are both single-orbit transforms of x and y convergent: forward convergence needs
Re z > lambda, backward needs Re z < lambda). Single-orbit families with kappa != 0 are themselves not excluded by
anything I know under GH (they are excluded under (V) by (iii)). So this is a sub-class result only.

**Remark 1.4 (order-0 eigen-measures on iR; PROVED).** Under GH, if B is a complex measure with B o P = iy B (y real),
then |B| = c nu and B = c h nu with h in L^inf(nu), |h| = 1, h o g_{-t} = e^{iyt} h nu-a.e. (Proof: by (c) above,
L_t|B| = |B|, i.e. |B|(Q_t phi) = |B|(phi); differentiating at t = 0 gives |B| o P = 0, so |B| = c nu by (F1).)
So order-0 point spectrum on iR = L^inf point spectrum of the (ergodic, Lemma D of R7-d) nu-class flow, and by
Corollary 1.2(i) it is semisimple at the order-0 level. I could not show such h are smooth.


### Block R9-d (from round9_q5: Lemma S, Proposition T (tensor-square trick), reduction to (J2)/(SS_Y), model check, positivity reformulation)
## 1. Lemma S: Theorem J under semisimplicity at 0 (proved)

Let N be a compact manifold, Z a smooth vector field on N, ν_N a smooth positive density, d_Z = div_{ν_N} Z, J^Z_t(p) = ∫_0^t d_Z(G_s p) ds (G_t the flow of Z), P_Z Φ = ZΦ + d_Z Φ, and Γ^Z_t Φ = e^{J^Z_t} Φ∘G_t.

**Definition (SS_Z).** P_Z^T is *semisimple at 0 (in finite order)* if the following holds. Whenever A, B are distribution densities of finite order on N with A∘P_Z = 0 and B∘P_Z = A, then A = 0.

**Lemma S.** Assume (SS_Z). Let S be a distribution density on N, and suppose there are ε > 0, k and C with |S(Γ^Z_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^k} for all real t and all smooth Φ. Then S = 0.

*Proof.* This is the proof of Theorem J (R6-a §2) with step 4 replaced.
1. Steps 1–3 use no hypothesis on the field. Put F_Φ(t) = S(Γ^Z_t Φ). It is C^1 with F_Φ' = F_{P_Z Φ}. The moments m_j(Φ) = ∫ t^j F_Φ dt are densities of order ≤ k. They satisfy m_0∘P_Z = 0 and m_j∘P_Z = −j m_{j−1} for j ≥ 1.
2. Induction. Suppose m_0 = … = m_{j−1} = 0; for j = 0 this is vacuous. Then m_j∘P_Z = 0 (for j ≥ 1 because m_{j−1} = 0; for j = 0 by step 1). Put B := −m_{j+1}/(j+1). Then B∘P_Z = m_j. By (SS_Z), m_j = 0. So all moments vanish.
3. Step 5 of Theorem J (Fourier transform holomorphic on |Im ξ| < ε, all Taylor coefficients at 0 equal to 0) gives F_Φ ≡ 0. Hence S(Φ) = F_Φ(0) = 0. ∎

*Remarks.*
- (K0) ∧ (K1) for Z imply (SS_Z). Indeed A∘P_Z = 0 gives A = cν_N by (K0). Then B∘P_Z = cν_N means u = B/ν_N satisfies Zu = −c, so c = 0 by (K1).
- The converse fails. For a Diophantine linear field on a torus, the field Y of Section 2 satisfies (SS_Y) (Section 3) but has an infinite-dimensional kernel, so (K0) fails for it.

## 2. Proposition T: the tensor-square trick (proved; no GH)

Let N = M×M, ν_N = ν⊗ν, and Y(x_1,x_2) = (X(x_1), −X(x_2)). Then:
- the flow is G_t = g_t × g_{−t};
- d_Y(x_1,x_2) = d(x_1) − d(x_2);
- J^Y_t(x_1,x_2) = J_t(x_1) + J_{−t}(x_2). (Check: ∫_0^t d(g_{−s}x_2) ds = −J_{−t}(x_2).)

Hence P_Y = P⊗1 − 1⊗P and Γ^Y_t = Γ_t ⊗ Γ_{−t}.

**Proposition T.** Let μ be an ergodic flow-invariant probability with h_μ(g_1) > 0, and λ = μ(d). Then there is a nonzero real distribution density S_2 on N, a combination of four Dirac masses, with
 |S_2(Γ^Y_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^1} for all t ∈ R and Φ ∈ C^∞(N),
for some ε > 0. No sign or size condition on λ is needed.

*Proof.*
1. **Inputs.** Theorem R, steps 1–3 (R8-a; Pesin, Ledrappier–Young and Lemma 6.0, cited as there) give the following, with 0 < θ < χ^+_min and 0 < δ < θ/4:
   - points x ≠ y with d(g_t x, g_t y) ≤ C_0 e^{−θ|t|} for t ≤ 0;
   - a constant b with |J_t(x) − J_t(y) − b| ≤ K e^{−θ|t|} for t ≤ 0;
   - since x and y are two-sided Birkhoff-generic for d, the bounds J_t(p) ≤ C_1 + (λ+δ)t and J_{−t}(p) ≤ C_1 + (−λ+δ)t for t ≥ 0 and p ∈ {x, y}.
2. **Definition.** Put w_x = 1 and w_y = −e^b, and S_2 := Σ_{p,q∈{x,y}} w_p w_q δ_{(p,q)} = S⊗S with S = δ_x − e^bδ_y. The four points are distinct and the weights are nonzero, so S_2 ≠ 0.
3. **Expansion.** F_2(t) := S_2(Γ^Y_t Φ) = Σ_{p,q} w_p w_q e^{J_t(p)+J_{−t}(q)} Φ(g_t p, g_{−t} q).
4. **Case t ≥ 0.** Fix p and sum over q:
   Σ_q w_q e^{J_{−t}(q)} Φ(g_t p, g_{−t} q) = e^{J_{−t}(x)} [Φ(g_tp, g_{−t}x) − Φ(g_tp, g_{−t}y) + (1 − e^{−r})Φ(g_tp, g_{−t}y)],
   where r = J_{−t}(x) − J_{−t}(y) − b and |r| ≤ K e^{−θt}.
   - The bracket is at most (C_0 + K e^K) e^{−θt} ||Φ||_{C^1}. This uses the Lipschitz bound of Φ in the second variable.
   - Multiplying by e^{J_t(p)} ≤ e^{C_1} e^{(λ+δ)t} and e^{J_{−t}(x)} ≤ e^{C_1} e^{(−λ+δ)t} gives |F_2(t)| ≤ C e^{−(θ−2δ)t} ||Φ||_{C^1}.
5. **Case t ≤ 0.** Write s = −t ≥ 0, fix q and sum over p. The same computation in the first variable, using backward asymptoticity, gives a factor e^{J_{−s}(x)} e^{−θs} ||Φ||_{C^1}, multiplied by e^{J_s(q)}. The bounds e^{J_{−s}(x)} ≤ C e^{(−λ+δ)s} and e^{J_s(q)} ≤ C e^{(λ+δ)s} give |F_2(t)| ≤ C e^{−(θ−2δ)|t|} ||Φ||_{C^1}.
6. Take ε = θ − 2δ > 0. ∎

The point is that the forward Jacobian growth of one factor is cancelled by the backward Jacobian growth of the other, because J_t(p) + J_{−t}(q) = o(|t|). So λ drops out, and the strip-position problem of (EF) disappears.

**Proposition T' (general S).** Let S be a distribution density on M with |S(Γ_t φ)| ≤ C e^{ρ(t)} ||φ||_{C^k}, where ρ(t) + ρ(−t) ≤ −ε|t|. This covers, for example, ρ(t) = a't for t ≥ 0 and ρ(t) = −b'|t| for t ≤ 0 with a' < b' (the hypothesis of (J1), any position of the interval (a', b')). Then |(S⊗S)(Γ^Y_t Φ)| ≤ C' e^{−ε|t|} ||Φ||_{C^{2k}}, and S⊗S ≠ 0 if S ≠ 0.

*Proof.*
1. Write (S⊗S)(Γ_t⊗Γ_{−t} Φ) = S(Γ_t f_t), where f_t(x_1) := S(Γ_{−t} Φ(x_1, ·)).
2. Derivatives in x_1 commute with S and with Γ_{−t} acting in x_2. So ||f_t||_{C^k} ≤ C e^{ρ(−t)} ||Φ||_{C^{2k}}. This step is the reason for the C^{2k} norm: x_1-derivatives fall on Φ, not on g_t.
3. Then |S(Γ_t f_t)| ≤ C e^{ρ(t)} ||f_t||_{C^k}, and the bound follows from ρ(t) + ρ(−t) ≤ −ε|t|. ∎

## 3. The reduction to (J2) / (SS_Y), and the model check

**(J2)** Under GH of X, no nonzero distribution density S_2 on M×M satisfies |S_2(Γ^Y_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^k} for all t.

**(SS_Y)** Under GH of X, P_Y^T is semisimple at 0 in finite order.

**Corollary 3.1 (proved).**
(a) (SS_Y) ⇒ (J2). This is Lemma S.
(b) (J2) ⇒ every GH flow has zero topological entropy. Use step 1 of the chain and Proposition T.
(c) (J2) ⇒ (EF), for strips in any position.
 - A nonzero EF on Σ(a,b) gives, by Theorem 2.1(B) of R8-b, a nonzero S with rates a' < b'. The uniform bounds (ii) of (EF) imply (E3).
 - Proposition T' then gives a nonzero two-sided decaying S⊗S, which contradicts (J2).
So (J2) implies (EF) and is formally stronger. Its advantage is that it is a statement at the single spectral point 0, which is where Jordan-chain arguments work.

**Model check (proved).** Let X = Σ α_i ∂_i on T^n with α Diophantine, ν = Lebesgue (so d = 0), and e_k = e^{2πi k·x}. Then P_Y(e_k⊗e_l) = 2πi (k−l)·α e_k⊗e_l. Let A, B be as in (SS_Y).
- A∘P_Y = 0 gives A(e_k⊗e_l) = 0 unless (k−l)·α = 0, i.e. unless k = l.
- B∘P_Y = A gives A(e_k⊗e_k) = B(P_Y(e_k⊗e_k)) = 0.
So A vanishes on trigonometric polynomials, hence A = 0. (SS_Y) is invariant under smooth conjugacy and under ν → e^cν, because P_Y is conjugated by multiplication by e^{c(x_1)+c(x_2)}. So (SS_Y), and hence (J2), holds for every field smoothly conjugate to a Diophantine linear flow. These are the only known GH fields. By contrast, the kernel of P_Y^T is infinite-dimensional here (the e_k⊗e_k-dual functionals), so (K0) fails for Y and Theorem J cannot be used as it stands.

## 4. Where it stops (precise)

1. **Y is not GH, even in the model**, so GH of X cannot be applied on M×M directly. What GH of X gives on M×M I could identify:
   - Partial pairing. Let A^ψ(φ) := A(φ⊗ψ). Then A∘P_Y = 0 gives A^ψ∘P = A^{Pψ}, and B∘P_Y = A gives B^ψ∘P = B^{Pψ} + A^ψ.
   - In the volume case (ν = ω, P = X) take ψ = 1. Then A^1∘X = 0, so A^1 = cω by (K0). Next B^1∘X = cω, so c = 0 by (K1). So A(·⊗1) = A(1⊗·) = 0: only the "zero mode" is killed.
   - Without a volume no function ψ has Pψ = 0, and not even this step is available.
   - The remaining modes would need the joint spectrum of (X_1, X_2) near the diagonal to be "discrete". That is the same missing spectral input as in (EF): absence of continuous spectrum of P^T off the point 0.
2. **The tensor objects are exactly Jordan chains of the M-families.** If T_z is the Laplace family of S on the line Re z = c, Parseval gives
   m_0 = (1/2πi) ∫_{Re z=c} T_z⊗T_z dz and m_1 = −(1/2πi) ∫ T'_z⊗T_z dz.
   Check: (T'_z⊗T_z)∘P_Y = T_z⊗T_z, because T'_z∘P = zT'_z + T_z.
   So (SS_Y) for these particular tensors means: superposed Jordan chains (T'_z, T_z) of P^T along a vertical line cannot exist. By Prop 3.2 of R8-b, this is the same object that (EF) must exclude. The tensor trick removes the dependence on the strip's position and the sign of λ (no more λ = 0 versus λ ≠ 0 cases), but not the spectral core.
3. **Variants checked (dead ends).**
   - (X, X) with S^u⊗S^s, an unstable pair times a stable pair: two-sided decay only when |λ| is small. In the λ = 0 case it works, but X⊕X is not GH either, and its kernel contains T_z⊗T_{−z}.
   - (X, −cX), or X⊕cX with c ≠ 1: for a nonzero EF on a strip, (K0) fails for every c close to 1, because z = cw has solutions with both z and w in the strip. So "K0 for some c" is again equivalent to the spectral statement.
   - S⊗T_{z0}, with T_{z0} an eigen-distribution and Re z_0 in the strip: this decays two-sided. But its moment chain is (Taylor coefficients of T_z at z_0)⊗T_{z_0}, so (SS_Y) for it is exactly "no Jordan chain of P^T at z_0". That is Remark 3.3 of R8-b, where GH gives nothing.

## 5. A positivity reformulation (proved; recorded for future use)
Let S be real as in Proposition T', with rates a' < b', and let c ∈ (a', b'). Put ι_c(φ)(t) := e^{−ct} F_φ(t). Then:
- ι_c(φ) ∈ L^1 ∩ L^∞ ⊂ L^2(R), with ||ι_c φ||_{L^2} ≤ C ||φ||_{C^k};
- ι_c(Pφ) = (d/dt + c) ι_c(φ);
- ι_c(Γ_s φ) = e^{cs} τ_s ι_c(φ), where τ_s is translation by s.

The closure of ι_c(C^∞) is translation-invariant. By Wiener's theorem (cited: closed translation-invariant subspaces of L^2(R) are {f : f̂ = 0 a.e. off E}), it equals L^2_E. Its Fourier transforms are ξ ↦ T_{c+iξ}(φ), which are real-analytic and not all identically 0. So E has full measure, and ι_c has dense range in L^2(R).

Thus a nonzero EF is equivalent to a C^k-continuous map C^∞(M) → L^2(R) with dense range that intertwines P − c with d/dt, i.e. Lebesgue spectrum of P^T on the line Re z = c. The positive forms Q_c(φ, ψ) = ∫ e^{−2ct} F_φ \overline{F_ψ} dt satisfy Q_c∘(P⊗1 + 1⊗P̄) = 2c Q_c. GH would have to forbid this. I could not connect it to GH: no smooth density is Q_c-continuous, since point-mass orbits do not see bumps placed away from them for long times.


### Block R9-e (from round9_q8: Proposition A (nu-aligned defect lemma), Theorem B (strips touching 0), dead ends)
## 1. Proposition A (nu-aligned defect lemma) — proved, using only (K0) and (K1)

**Proposition A.** Assume (K0) and (K1); GH suffices. Let D be an open disc around 0. Let (A_z), z in D, be distribution densities such that:
- z -> A_z(phi) is holomorphic on D for every smooth phi;
- there are k and C with |A_z(phi)| <= C ||phi||_{C^k} for all z in D (locally uniform suffices);
- A_z(P phi) = z A_z(phi) + c(z) nu-hat(phi) for all phi and all z in D, for some function c.

Then c is holomorphic on D, and there is a holomorphic alpha on D with A_z = alpha(z) nu-hat and c(z) = -z alpha(z).

Conversely, every such pair is a solution, since nu-hat∘P = 0. So the defect equation does **not** force A = 0. The planner's sketch (A) asked whether "a family with nu-valued defect must vanish". The answer is no: it must be **nu-aligned**.

*Proof.*
1. *c is holomorphic.* Fix phi_1 smooth with nu-hat(phi_1) = 1. Then c(z) = A_z(P phi_1) - z A_z(phi_1), which is holomorphic.
2. *Taylor coefficients.* Write A_z = sum_n A_n z^n, with A_n(phi) = (1/2 pi i) ∮ A_w(phi) w^{-n-1} dw over a small circle in D. Each A_n is a distribution density of order <= k (Cauchy estimates). Write c(z) = sum_n c_n z^n.
3. *Comparing coefficients.* Comparing coefficients in the defect equation gives
   - A_0∘P = c_0 nu-hat, and
   - A_n∘P = A_{n-1} + c_n nu-hat for n >= 1.
4. *Induction.*
   - n = 0: by (F2), c_0 = 0. Then (F1) gives A_0 = a_0 nu-hat.
   - Step: if A_{n-1} = a_{n-1} nu-hat, then A_n∘P = (a_{n-1} + c_n) nu-hat. By (F2), a_{n-1} + c_n = 0, and by (F1), A_n = a_n nu-hat.
5. *Conclusion.* a_n = A_n(phi_1), so alpha(z) := sum a_n z^n converges on D. We get A_z = alpha(z) nu-hat, and c_n = -a_{n-1}, i.e. c(z) = -z alpha(z). ∎

**Meromorphic variant (same proof).** Suppose A_z is holomorphic on D \ {0} and meromorphic at 0 with finite pole order. Then the Laurent coefficients satisfy A_n∘P = A_{n-1} + c_n nu-hat. The same recursion, started at the least index with A_n != 0, gives the same conclusion. Below that index, the relation gives c_n = 0.

---

## 2. Theorem B (strips touching 0: only the mean-zero part needs to continue) — proved, using only (K0) and (K1)

**Theorem B.** Assume (K0) and (K1); GH suffices.
- Let W be a connected open set with 0 on its boundary, e.g. W = Sigma(0,b) = {0 < Re z < b}.
- Let (T_z), z in W, be an EF on W: T_z(phi) is holomorphic in z for each phi, T_z is locally uniformly of finite order, and T_z∘P = z T_z.
- Suppose there are a disc D around 0 and distribution densities H_z (z in D) such that:
  - z -> H_z(phi) is holomorphic on D;
  - |H_z(phi)| <= C ||phi||_{C^k} on D;
  - D ∩ W is connected and nonempty;
  - H_z(phi) = T_z(phi) for every z in D ∩ W and every phi with nu-hat(phi) = 0.

Then T_z = 0 for all z in W.

**Nothing at all is assumed about z -> T_z(phi_1) near 0** for phi_1 with nu-hat(phi_1) = 1. In particular:
- the divergence of the forward transform along nu-hat as Re z -> 0+ (the Patterson behaviour of R8-c, Lemma 2.2 / Corollary 2.3) is harmless;
- so is an essential singularity, or a natural boundary, in that one direction.

Lemma M of R6-b is the special case in which T_z itself continues.

*Proof.*
1. *Projected family.* Fix phi_1 with nu-hat(phi_1) = 1. For z in D put H'_z(phi) := H_z(phi - nu-hat(phi) phi_1). This is holomorphic and of order <= k (phi_1 is fixed and smooth), and H'_z(phi_1) = 0 for all z.
2. *Defect equation on D ∩ W.* Let z be in D ∩ W.
   - Since nu-hat∘P = 0, H'_z(P phi) = H_z(P phi) = T_z(P phi) = z T_z(phi).
   - Also z H'_z(phi) = z T_z(phi) - z nu-hat(phi) T_z(phi_1).
   - Hence H'_z(P phi) - z H'_z(phi) = c(z) nu-hat(phi), with c(z) := z T_z(phi_1).
3. *Extension to D.* Define c~(z) := H'_z(P phi_1) for z in D; it is holomorphic on D. On D ∩ W, step 2 with phi = phi_1 gives c~(z) = c(z), since H'_z(phi_1) = 0. For each fixed phi, both sides of
   H'_z(P phi) - z H'_z(phi) = c~(z) nu-hat(phi)
   are holomorphic on the connected disc D and agree on the nonempty open set D ∩ W. By the identity theorem they agree on D.
4. *Proposition A.* It gives H'_z = alpha(z) nu-hat on D and c~ = -z alpha. Evaluating at phi_1 gives alpha = 0. Hence H' = 0 on D and c~ = 0.
5. *T vanishes near 0.* On D ∩ W we get z T_z(phi_1) = c(z) = c~(z) = 0. Since 0 is not in W, T_z(phi_1) = 0. Then T_z(phi) = H'_z(phi) + nu-hat(phi) T_z(phi_1) = 0 for every phi.
6. *T vanishes on W.* For each phi, z -> T_z(phi) vanishes on the open set D ∩ W. By the identity theorem (W connected) it vanishes on W. ∎

**Remark B1 (what this says about (PE0), the case lambda = mu(d) = 0 of Theorem R).** There T_z = B_z + G_z on Sigma(0, theta).
- B_z, the backward part, is holomorphic on Re z < theta, so across 0.
- G_z(phi) = int_0^inf e^{-zt} F_phi(t) dt, with F_phi(t) = e^{J_t(x)} phi(g_t x) - e^b e^{J_t(y)} phi(g_t y).

By Theorem B, the whole case (PE0) of the chain follows from the following statement.

**(A-res).** For every nu-mean-zero smooth phi, the forward pair transform G_z(phi) continues holomorphically from {0 < Re z < theta} to a neighbourhood of 0, with C^k bounds that are uniform in phi.

R8-c's Corollary 2.3 shows that the divergent leading term of G_s as s -> 0+ is aligned with nu-hat. So (A-res) says exactly that **after the nu-hat direction is removed, nothing singular is left at 0**. I could not prove (A-res).

The meromorphic variant of Proposition A lets (A-res) be weakened to meromorphic continuation with bounded pole order. By Lemma H of R7-e, it can presumably also be replaced by quasi-analytic flatness on a half-disc. I have not written out that version, so I do not claim it.

---

## 3. Dead ends, with reasons

**Remark C (the planner's mechanism (B) adds no information by itself).** Leibniz gives P(phi psi) = phi X psi + psi P phi. So the identity
  V_z(X psi) = z V_z(psi) - T_z((P phi) psi),  with V_z := T_z(phi ·),
is literally the eigen-relation T_z∘P = z T_z tested on the product phi psi. Taking phi = 1 recovers the eigen-relation. So the family of identities indexed by (phi, psi) is equivalent to the eigen-relation alone.

Taking phi = e^a with a smooth gives the eigen-relation for P_a = X + (d + Xa). That is just the change nu -> e^{a} nu, which is already absorbed in the statement of (EF). The best one can do this way is inf_a ||d + Xa||_inf = max_mu |mu(d)|. (This is the Hahn–Banach distance from d to the closure of the coboundaries in C^0, cited as standard.) So the weight can never be made smaller than the largest |mu(d)|.

Combining (B) with the tame inverse R of X (Lemma B of R7-d) gives
  T_z(phi f) = z T_z(phi R f) - T_z((P phi) R f)  for f in X(C^inf).
Inserting the tame bound ||Rf||_{C^1} <= C ||f||_{C^m} gives an estimate *weaker* than the trivial |T_z(phi f)| <= ||T_z|| ||phi f||_{C^1}. So no contradiction can come from size estimates alone. A contradiction would need a kernel (Jordan-chain) argument for the unweighted operator. By R8-d Corollary C, that needs dim I = 1, i.e. (V).

Moreover, without (V), X(C^inf) is the annihilator of I, which has codimension dim I >= 2. Then R is not even defined on all nu-mean-zero functions. **(B) can therefore act only through (V), as the round-8 dichotomy predicted.**

**Remark D (countability of Sigma_1 ∩ {Re z != 0} cannot come from soft arguments).**
- Eigenvectors for distinct eigenvalues are linearly independent. But (C^1)' has uncountable algebraic dimension and is not separable, so cardinality gives nothing.
- Operators with an open set of eigenvalues of the transpose exist in every infinite-dimensional setting; the backward shift is an example.
- GH is a statement about X = P - 0 only.

So countability off iR would itself need a mechanism transferring GH to P - z. Remark 3.3 of R8-b explains why such a transfer seems to contain the [GOAL]. I found none.

**Remark E (model computation: (A-res) fails for single orbits, even for GH fields).** Let Y be a Diophantine linear field on T^n, with nu = Lebesgue (so d = 0), and phi a mean-zero trigonometric polynomial. Then
  int_0^inf e^{-zt} phi(x + t alpha) dt = sum_{k != 0} phi-hat_k e^{2 pi i k.x} / (z - 2 pi i k.alpha).
This has poles at 2 pi i k.alpha. For general smooth mean-zero phi these poles accumulate at 0 along iR, so iR is generically a natural boundary.

Hence the single-orbit transforms of mean-zero functions do **not** continue across 0, even for the model GH fields. Any proof of (A-res) must use the cancellation inside the pair S = delta_x - e^b delta_y, which has no analogue in the model (Diophantine flows have no asymptotic pairs). This is consistent with R6-e's remark that Re z = 0 is generally a natural boundary, now isolated to the mean-zero part.

---


### Block R9-f (from round9_q6 §1-2: continuation modulo C nu; two-sided convergence at a quasi-analytic rate)
## 1. Proposition 1 (mechanism (A) = continuation modulo Cν)

**Proposition 1.** Assume GH. Let T_z (0 < Re z < ε) be the eigen-family of an (EF-0)-type S, or more generally any family satisfying (i)–(iii) of (EF) on the strip Σ(0, ε). Suppose there are:
- an open disc D centred at 0 with D_+ := D ∩ {Re z > 0} ⊂ Σ(0, ε);
- a family W_z, z ∈ D, of distribution densities such that z -> W_z(φ) is holomorphic on D for every smooth φ, and |W_z(φ)| <= C ||φ||_{C^K} for z in compact subsets of D;
- the property W_z(φ) = T_z(φ) for every φ ∈ ker ν̂ and every z ∈ D_+.

Then T_z = 0 on the whole strip; for an (EF-0)-type S this gives S = 0 (Theorem 2.1(A) of R8-b). The same conclusion holds if W_z is only meromorphic at 0, with the bounds on a circle around 0.

*Proof.*
1. Put W̃_z(φ) := W_z(φ - ν̂(φ)). This family is holomorphic on D, of order K, and W̃_z(1) = 0. On D_+ we have T_z(φ) = W̃_z(φ) + ν̂(φ) T_z(1), because φ - ν̂(φ) ∈ ker ν̂.
2. Take φ = 1. Since P1 = d and ν̂(d) = 0, z T_z(1) = T_z(d) = W̃_z(d) on D_+. So c(z) := z T_z(1) extends holomorphically to D as W̃_z(d).
3. For any φ, Pφ ∈ ker ν̂. Hence, on D_+,
   W̃_z(Pφ) = T_z(Pφ) = z T_z(φ) = z W̃_z(φ) + ν̂(φ) W̃_z(d).
   Both sides are holomorphic on D, so the identity holds on D by the identity theorem.
4. Expand W̃_z = Σ_n A_n z^n near 0. By Cauchy's formula on a circle, each A_n is a distribution density of order K. The identity of step 3 gives, coefficient by coefficient,
   A_n∘P = A_{n-1} + A_n(d) ν̂,  with A_{-1} = 0,  and A_n(1) = 0 for all n.
5. Induction on n. Suppose A_{n-1} = 0 (true for n = 0). Then A_n∘P = A_n(d) ν̂. By (F2), A_n(d) = 0. By (F1), A_n = a ν, and A_n(1) = 0 forces a = 0. So every A_n vanishes, and W̃ ≡ 0 near 0, hence on D.
6. Then, on D_+, T_z(φ) = ν̂(φ) T_z(1). So z T_z(φ) = T_z(Pφ) = ν̂(Pφ) T_z(1) = 0, and T_z = 0 on D_+. By the identity theorem T_z(φ) ≡ 0 on the strip for every φ.
7. Meromorphic case. Use Laurent coefficients A_n (n ∈ Z). The pole order is finite by the Baire argument of Lemma M. The least nonzero A_{n0} satisfies A_{n0}∘P = A_{n0}(d) ν̂, and step 5 shows A_{n0} = 0, a contradiction. ∎

**Consequences.**
- (a) Since B_z is holomorphic across 0, the hypothesis of Proposition 1 is equivalent to: the forward transform G_z, restricted to ker ν̂, has such a continuation. The one-sided Patterson lemma (R8-c, Lemma 2.2) says that the divergent part of G_s as s -> 0+ is aligned with ν̂. Proposition 1 shows that removing that part is the only thing the ν-aligned "defect" mechanism can do. Everything rests on the sub-leading behaviour of G_z on ker ν̂.
- (b) The Lemma-M variant asked for in the planner's step (2) is proved; it is steps 4–5. Its general form: a family A_z holomorphic near 0 with A_z∘P = z A_z + c(z) ν̂ must equal -(c(z)/z) ν̂. Here c is automatically holomorphic, being A_z(d) up to the normalisation A_z(1). So step (2) is settled, and the planner's step (3) (control of H_z near 0) is exactly the continuation hypothesis above. It is not proved.

## 2. Proposition 2 (two-sided convergence at a quasi-analytic rate)

Let w : [0, ∞) -> [0, ∞) be admissible as in Theorem J* (R7-a): M_j := ∫_R |t|^j e^{-w(|t|)} dt < ∞ for all j, and Σ_j M_j^{-1/j} = ∞. An example is w(t) = t/log(e + t).

**Proposition 2.** Assume GH. Let S be a distribution density of order k. Suppose that for every smooth φ the limits ℓ_±(φ) := lim_{t -> ±∞} F_φ(t) exist, with
 |F_φ(t) - ℓ_±(φ)| <= C e^{-w(|t|)} ||φ||_{C^k}  for ±t >= 0.
Then S = cν for a constant c, and ℓ_+ = ℓ_- = cν.
In particular, if F_φ(t) -> 0 as t -> -∞ (as in (EF-0)) and F_φ converges as t -> +∞ at an admissible rate, then S = 0.

*Proof.*
1. *The limits are multiples of ν.* For fixed t_0 we have |F_φ(t_0)| <= ||S|| ||Γ_{t_0}φ||_{C^k} <= C_{t_0} ||φ||_{C^k}. Hence ℓ_± ∈ (C^k)'.
   - From F_{Γ_s φ}(t) = F_φ(t + s), letting t -> ±∞ gives ℓ_±(Γ_s φ) = ℓ_±(φ). Here we use ||Γ_s φ||_{C^k} < ∞ for fixed s.
   - Differentiate at s = 0: (Γ_s φ - φ)/s -> Pφ in C^k. This gives ℓ_±∘P = 0, so ℓ_± = c_± ν by (F1).
2. *Subtract the limits.* Put F̃_φ(t) := F_φ(t) - c_+ ν(φ) H(t) - c_- ν(φ) H(-t), where H is the Heaviside function. Then |F̃_φ(t)| <= C' e^{-w(|t|)} ||φ||_{C^k}, and m̃_j(φ) := ∫ t^j F̃_φ dt are distribution densities of order k. Also F̃_{Pφ} = F_{Pφ}, because ν(Pφ) = 0.
3. *Moment relations.* Choose R_n -> ∞ with R_n^j (|F̃(R_n)| + |F̃(-R_n)|) -> 0. This is possible as in J*, step 3.
   - j = 0: ∫_{-R}^{R} F_{Pφ} = F_φ(R) - F_φ(-R) -> (c_+ - c_-) ν(φ).
   - j >= 1: ∫_{-R}^{R} t^j F_φ' = [t^j F_φ]_{-R}^{R} - j ∫_{-R}^{R} t^{j-1} F_φ dt.
   - First consequence: m̃_0∘P = (c_+ - c_-) ν. By (F2), c_+ = c_- =: c. By (F1), m̃_0 = a_0 ν.
   - Now F_φ = F̃_φ + c ν(φ) on all of R. The constant contributes c ν(φ)(R^j - (-R)^j) to the boundary term and -c ν(φ)(R^j - (-R)^j) to the integral term, so these cancel. Hence m̃_j∘P = -j m̃_{j-1} for j >= 1.
4. *Induction as in Theorem J.* If m̃_{j-1} = a_{j-1} ν, then m̃_j∘P = -j a_{j-1} ν. By (F2), a_{j-1} = 0, and by (F1), m̃_j = a_j ν. So all m̃_j = 0.
5. *Quasi-analyticity, as in J* step 5 (Denjoy–Carleman, cited).* The Fourier transform of F̃_φ has all derivatives at 0 equal to zero and lies in a quasi-analytic class, so it vanishes. Hence F̃_φ = 0 a.e. Since c_+ = c_- = c, F̃_φ(t) = F_φ(t) - c ν(φ) for t ≠ 0. So F_φ(t) = c ν(φ) for a.e. t, and by continuity for every t. At t = 0 this gives S(φ) = c ν(φ). ∎

*Remarks.*
- Proposition 2 contains Theorems J and J* (case c_± = 0) and Corollary E of R8-f.
- For an absolutely continuous S = wν, F_φ(t) = ∫ (w∘g_{-t}) φ dν. The hypothesis then says that the ν-transfer operator mixes w at a quasi-analytic rate in both directions, and the conclusion says w is constant.
- It does **not** apply to the pair distributions of Theorem R. Their forward transport e^{J_t(x)} φ(g_t x) - e^{b + J_t(y)} φ(g_t y) does not converge, since x and y separate forward. To use Proposition 2 one would need to smear S along a family of pairs, with a positive-measure set of base points, in such a way that the forward transport converges at a quasi-analytic rate. No rate of equidistribution is available for general positive-entropy measures; this is the "coarse tail" of R8-e §4.


### Block R9-g (from round9_q2 §2-5: modulus lemma, conformal eigenvalues, Leibniz mechanism carries no information, band lemma, routes found dead)
## 2. The modulus of an order-0 eigen-family: positivity is vacuous

**Lemma 1 (modulus lemma; proved, no GH).** Let T be a nonzero complex Borel measure on M with T o P = z T for
some z in C. Put m := |T| (total variation measure) and c := Re z. Then

  (i) (g_t)_*(e^{J_t} m) = e^{c t} m for all t, equivalently m(P phi) = c m(phi) for all smooth phi
      ("m is a c-conformal probability after normalisation");
  (ii) c = m(d)/m(M);
  (iii) writing T = h m with |h| = 1 m-a.e. (polar decomposition), one has h o g_t = e^{-i (Im z) t} h  m-a.e.,
        for every t: the conformal measure m carries a measurable unimodular eigenfunction of the flow with
        eigenvalue -i Im z.

*Proof.* (i) For a positive continuous weight w one has |w T| = w |T| (write dT = h d|T| with |h| = 1), and for a
Borel bijection G with Borel inverse one has |G_*rho| = G_*|rho| (pushforward along a bijection matches partitions
of a set with partitions of its preimage). Apply this with w = e^{J_t} and G = g_t to (1.2):
|e^{zt} T| = e^{ct} m on the one hand, and |(g_t)_*(e^{J_t}T)| = (g_t)_*(e^{J_t} m) on the other. This is the
displayed identity; pairing with phi gives m(Gamma_t phi) = e^{ct} m(phi), and differentiating at t = 0 (dominated
convergence, Fact 1.1) gives m(P phi) = c m(phi).
(ii) Put phi = 1 in m(P phi) = c m(phi) and use P 1 = d.
(iii) Fix t. The measure (g_t)_*(e^{J_t} T) = e^{zt} h m has, with respect to (g_t)_*(e^{J_t} m) = e^{ct} m, the
density (h o g_t^{-1}); comparing the two expressions of the same measure gives h o g_{-t} = e^{i(Im z) t} h
m-a.e., which is the claim with t replaced by -t. ∎

So the modulus of an order-0 eigen-density is a tilted conformal measure in the sense of Prop. 2.2 of R4-q7, whose
eigenvalue is Re z and which "knows" Im z only through a measurable unimodular eigenfunction.

**Proposition 2 (conformal eigenvalues always fill at least the set of ergodic averages of d; proved, no GH).**
Let C := { c in R : there is a Borel probability m on M with m(P phi) = c m(phi) for all smooth phi }. Then
 (a) C is a nonempty compact subset of R;
 (b) C contains mu(d) for every ergodic flow-invariant probability mu;
 (c) C contains a number >= 0 and a number <= 0; under GH, 0 in C and the 0-conformal probability is unique,
     namely nu-hat = nu/nu(M).

*Proof.* (b) is Prop. 2.2 of R4-q7, re-proved here for completeness: take x generic for mu in both time directions,
so J_t(x) - mu(d) t = o(|t|) as t -> ±inf; then c_s(t) := e^{J_t(x) - mu(d) t - s|t|} is integrable for each s > 0
and tends to 0 at ±inf; integrating d/dt [c_s(t) phi(g_t x)] = c_s(t)[(P phi - mu(d) phi)(g_t x) - s sgn(t)
phi(g_t x)] over R gives |T_s(P phi - mu(d) phi)| <= s ||phi||_inf for the normalised probabilities T_s carried by
the orbit; any weak* limit as s -> 0+ is a probability m with m(P phi) = mu(d) m(phi).
(a) Nonemptiness follows from (b) (invariant measures exist). Compactness: if m_n is c_n-conformal, c_n -> c and
m_n -> m weak*, then m is a probability and m(P phi) = c m(phi); boundedness of C follows from (ii) of Lemma 1
(|c| = |m(d)| <= ||d||_inf).
(c) By Prop. 2.1 of R4-q7 there are ergodic mu_± with mu_+(d) >= 0 >= mu_-(d); apply (b). Under GH, nu-hat is
0-conformal (int P phi dnu = int L_X(phi nu) = 0) and uniqueness is (F1). ∎

**Corollary 3 (the positivity route to (EF) is vacuous; proved).** Let (T_z) be a family as in (EF) which in
addition consists of *measures* (order 0). Then the only information extractable from the moduli |T_z| is that the
numbers Re z, z in Omega, all lie in C. Since C contains, with no hypothesis at all, every value mu(d) of an
ergodic measure, and since the problem's own chain produces strips at Re z near lambda = mu(d) (Theorem R), GH does
not contradict this. In particular no argument which uses only the positive measures |T_z| (conformality,
uniqueness of conformal measures at eigenvalue 0, Lemma C/Lemma D of the background) can prove (EF).

*Proof.* Immediate from Lemma 1 and Proposition 2: the map z -> |T_z| forgets Im z, and the resulting constraint
"Re z in C for all z in Omega" is satisfiable: e.g. take X with an ergodic mu, lambda = mu(d), and recall from
Prop. 2 that lambda in C; the conformal measures produced by Prop. 2 exist for GH fields as well (nothing in the
proof of Prop. 2 uses or contradicts GH). ∎

**Remark 4 (what Lemma 1(iii) would need).** One could hope to contradict (EF) for order-0 families as follows: if
the c-conformal probability were *unique* for each c (as it is for c = 0 under GH, by (F1)), then all the measures
|T_{c+iy}|, y in R, would be one fixed probability m_c, and by Lemma 1(iii) m_c would carry measurable unimodular
eigenfunctions for every eigenvalue in an interval of iR, hence (taking products and quotients of the h's) for
every real eigenvalue. For a *measure-preserving* ergodic flow this is impossible (eigenvalues form a countable
group, by orthogonality in the separable space L^2). For a nonsingular (here: conformal, hence not invariant)
ergodic action it is **not** impossible: the translation flow on R with any probability measure equivalent to
Lebesgue has h_y(x) = e^{i y x} as eigenfunction for every y. I could neither prove uniqueness of c-conformal
measures for c != 0 under GH (Lemma C and Lemma D of the background use (F1), i.e. c = 0, in an essential way:
the tilted equation m(P phi) = c m(phi) is not the kernel of any operator to which GH applies), nor rule out the
dissipative single-orbit behaviour, which is exactly the behaviour of the measures that Theorem R produces. So
Remark 4 is a *possible* route for order-0 families only, and it needs a new uniqueness theorem at c != 0; note
that Lemma C of the background (int_R e^{J_t(x)} dt = inf under GH) does **not** tilt: its proof uses (F1).

---

## 3. The Leibniz/module mechanism (B) carries no information

Throughout this section: GH holds **and** X preserves a smooth positive probability density omega (the "volume
case"). Take nu = omega, so d = 0, J = 0, P = X, Gamma_t phi = phi o g_t. By (O2) the invariant distribution
densities are the multiples of omega, X(C^inf) = C_0^inf := {f : omega(f) = 0} (duality consequence of Text A),
and by Corollary 3 of Text B, X : C_0^inf -> C_0^inf is a topological isomorphism of Fréchet spaces; let
R := (X|_{C_0^inf})^{-1} and phi_0 := phi - omega(phi) (omega normalised to mass 1). Note R(C_0^inf) = C_0^inf.

Outside the volume case none of this is available: by Proposition A of R8-d, P(C^inf) is closed **iff** X preserves
a smooth positive density, so P has no continuous inverse on its range unless we are in the volume case. This is
why mechanism (B), which needs to divide by X or by P, is confined to the volume case from the start.

**Proposition 5 (Leibniz identity; proved).** Let T be any linear functional on C^inf with T o X = z T. Then for
every smooth phi and every smooth psi with omega(psi) = 0,

  T(phi psi) = z T(phi R psi) - T((X phi) R psi).        (3.1)

*Proof.* X(phi · R psi) = (X phi)(R psi) + phi X(R psi) = (X phi)(R psi) + phi psi. Apply T and use
T(X(·)) = z T(·). ∎

**Proposition 6 (the iterated expansion; proved).** With the hypotheses of Prop. 5, for every N >= 1,

  T(phi psi) = z^N T(phi R^N psi) - sum_{j=1}^{N} z^{j-1} T( (X phi) R^{j} psi ).      (3.2)

*Proof.* Put A_k := T(phi R^k psi), B_k := T((X phi) R^k psi) (all R^k psi are smooth and omega-mean-zero). By
(3.1) applied to R^k psi in place of psi: A_k = z A_{k+1} - B_{k+1}. Iterate from k = 0. ∎

For phi = 1 this is the relation T(psi) = z^N T(R^N psi) used in Theorem V of R7-e and in Lemma Q of R8-a. The
planner's suggestion (B) was to use nonconstant phi to transport tame estimates. The next theorem shows that this
cannot help, for a reason that is not quantitative but logical: (3.1), (3.2) and every other consequence of the
Leibniz rule are formal consequences of the single relation of Theorem V.

**Theorem 5' (the content of the eigen-equation; proved).** Assume the volume case above and let z != 0. The
restriction map T -> tau := T|_{C_0^inf} is a bijection

  { T : C^inf -> C linear, T o X = z T }  -->  { tau : C_0^inf -> C linear, tau = z (tau o R) },

and its inverse is tau -> T, T(phi) := tau(phi_0). Under this bijection T(1) = 0 automatically, and T is
continuous for the C^k norm if and only if tau is.

*Proof.* (a) If T o X = z T then T(1) = z^{-1} T(X 1) = 0, hence T(phi) = T(phi_0) for all phi, so T is determined
by tau. For psi in C_0^inf we have psi = X(R psi), so tau(psi) = T(X R psi) = z T(R psi) = z tau(R psi) (using
R psi in C_0^inf). Thus tau satisfies the fixed-point relation.
(b) Conversely let tau satisfy tau = z (tau o R) on C_0^inf, and put T(phi) := tau(phi_0). Then for smooth phi,
X phi is in C_0^inf and (X phi)_0 = X phi, so T(X phi) = tau(X phi); also phi_0 = R(X phi_0) = R(X phi), so
z T(phi) = z tau(phi_0) = z tau(R(X phi)) = tau(X phi) by the hypothesis. Hence T o X = z T.
(c) The two constructions are mutually inverse, and continuity in the C^k norm is preserved in both directions
because phi -> phi_0 is C^k-bounded. ∎

**Corollary (mechanism (B) cannot work).** Let z != 0. Every identity satisfied by all order-<=1 functionals T with
T o X = z T — in particular (3.1), (3.2) for all phi and psi, and any identity derived from the Leibniz rule, from
the module structure of C^inf over itself, or from the dual division of GH (O1) — is a formal consequence of the
single relation `tau = z(tau o R)` on C_0^inf. Hence no such identity can exclude the existence of a nonzero T:
the set of solutions it cuts out is exactly the set of solutions of the fixed-point relation. In particular, to
prove (EF) along the lines of (B) one must prove that the fixed-point relation has no nonzero order-1 solution for
z in the strip, i.e. precisely the statement that Theorem V of R7-e reduces to a Carleman condition on
||R^N phi||_{C^1}. Quantitatively: the "new" terms in (3.2) are the T((X phi)R^j psi), whose only available bounds
are C ||X phi||_{C^1} ||R^j psi||_{C^1} with the *non-decaying* coefficients |z|^{j-1}; so the estimate obtained
from (3.2) is never better than the one obtained from the case phi = 1 (which has no such terms), and it is worse
unless X phi = 0, i.e. (by L1) unless phi is constant.

*Proof.* The first two sentences are Theorem 5' (the solution set is unchanged). The quantitative last sentence is
read off (3.2): taking absolute values gives
|T(phi psi)| <= C|z|^N ||phi R^N psi||_{C^1} + C sum_{j=1}^N |z|^{j-1} ||X phi||_{C^1} ||R^j psi||_{C^1}, and the
sum contains ||R^j psi||_{C^1} for every j <= N with coefficient |z|^{j-1} > 0. ∎

**Remark 7 (why no functional analysis alone can give (EF)).** By Theorem 5', in the volume case (EF) says exactly:
*the transpose of R has no holomorphic family of order-<=1 eigenfunctionals with eigenvalues 1/z filling an open
set.* This is **not** a formal property of operators: for the unilateral forward shift S on l^2, the adjoint S^*
has every point of the open unit disc as an eigenvalue, with eigenvectors depending holomorphically and locally
boundedly on the eigenvalue. The tame properties that GH gives R (continuity, ||R psi||_{C^k} <= C_k
||psi||_{C^{m_k}}, injectivity, surjectivity onto C_0^inf) are all shared by a shift-like operator. Therefore any
proof of (EF) must use the *dynamical* fact that R inverts the generator of a one-parameter group of composition
operators, not only the operator-theoretic consequences of GH. This makes rigorous the heuristic of R8-c Section 3
("in infinite dimensions the finite-dimensional argument fails as soon as there is continuous spectrum; the shift
on L^2(R) has functionals with one-sided decay").

---

## 4. A band lemma (elementary, locates the possible strips)

**Lemma 8 (proved, no GH).** Fix k >= 0 and let T != 0 be a distribution density of order <= k with T o P = z T.
Put Lambda_k^+ := limsup_{t -> +inf} (1/t) log ||Gamma_t||_{C^k -> C^k} and
Lambda_k^- := limsup_{t -> +inf} (1/t) log ||Gamma_{-t}||_{C^k -> C^k}. Then

  -Lambda_k^- <= Re z <= Lambda_k^+ .

*Proof.* Pick phi with T(phi) != 0. By (1.1), e^{Re z t} |T(phi)| = |T(Gamma_t phi)| <= ||T||_{(C^k)'}
||Gamma_t||_{C^k->C^k} ||phi||_{C^k}. Take logarithms, divide by t and let t -> +inf; then do the same with
t -> -inf. ∎

Consequences. (i) ||Gamma_t||_{C^0->C^0} = sup_x e^{J_t(x)}, whose exponential rate is max_mu mu(d) forward and
max_mu(-mu(d)) backward (Prop. 2.1 step 1 of R4-q7). So all order-0 eigenvalues satisfy
min_mu mu(d) <= Re z <= max_mu mu(d), the extrema being over invariant probabilities; and by Proposition 2 every
value mu(d), mu ergodic, is attained by an order-0 eigen-density. So Lemma 8 is essentially sharp at k = 0 and
gives no contradiction. (ii) For k = 1 the rate involves in addition sup_x ||Dg_t(x)||, whose rate is the
quantity lambda* of R5-a; so a nonzero order-1 eigen-distribution with Re z > max_mu mu(d) forces lambda* > 0.
This is a (very weak) converse to Theorem R, and it shows that (EF) for strips far from 0 is "allowed" by the
coarse growth bounds exactly in the positive-entropy regime; no contradiction.

---

## 5. Routes checked and found dead (with the reason)

(D1) **Positivity / moduli.** Dead by Corollary 3: the modulus of an order-0 eigen-density is a conformal measure,
and conformal measures with eigenvalue c exist for every c = mu(d); GH constrains only c = 0.

(D2) **Leibniz / module structure (the planner's bet (B)).** Dead by Theorem 5' and its corollary: in the volume
case the Leibniz identities carry no information beyond the fixed-point relation tau = z(tau o R); outside the
volume case the required division by P is unavailable (Prop. A of R8-d).

(D3) **Moving the strip.** Dead for the reasons already recorded in the brief ((C)) and re-checked here:
 - changing nu to e^a nu conjugates P by e^{a} and changes neither Sigma_k nor the strip (brief's remark);
 - a constant time change X -> cX rescales z by c, so it cannot move a strip contained in {Re z > 0} to one
   containing 0;
 - a real shift z -> z - kappa would require a smooth a with X a = kappa != 0, forbidden by (K1);
 - multiplication by a smooth eigenfunction (X psi = i gamma psi, |psi| = 1) shifts z by i gamma only, i.e. moves
   the strip vertically, never horizontally; and a smooth psi with X psi = kappa psi, kappa real != 0, cannot exist
   (at a maximum of |psi|^2 one gets 2 kappa |psi|^2 = X|psi|^2 = 0).
 - a general time change hX (h > 0 smooth) does not act on eigen-distributions at all: X u = -z u gives
   (hX) u = -z h u, which is not an eigen-equation.

(D4) **Tensor square / Hilbert-space positivity.** If T is an order-<=1 eigen-density with T o P = z T, the kernel
U := T (x) conj(T) on M x M satisfies (X (+) X) U = 2 Re z · U and is a positive-definite kernel
(U(sum_i phi_i (x) conj(phi_i)) = sum_i |T(phi_i)|^2 >= 0). This is a genuine positivity statement surviving in
order 1 (unlike (D1)). It is nevertheless useless here, for two proved reasons: (i) X (+) X on M x M is never GH,
because f(x,y) = F(the difference of first integrals) can be invariant — concretely, for a Diophantine linear flow
on T^n the product field on T^{2n} has the nonconstant invariant functions e^{2 pi i k.(x-y)}, so GH fails for the
product even when it holds for X; (ii) a positive-definite kernel distribution of order 1 need not be a measure
(T = derivative of a Dirac mass gives U(phi (x) conj(phi)) = |phi'(x)|^2 >= 0), so Lemma 1 cannot be applied to U.

(D5) **Principal symbol on the sphere bundle.** An order-<=1 functional can be represented (Riesz) as
T(phi) = mu_0(phi) + <m, dphi> with mu_0 a complex measure and m a complex TM-valued measure; (1.1) transforms the
pair by a *triangular* cocycle whose top block is m -> (g_t)_*(e^{J_t} Dg_t m) and whose off-diagonal term
(coming from d(e^{J_t}) = e^{J_t} dJ_t) lands in the order-0 part. Taking total variations of the top block would
produce a conformal measure S on the unit sphere bundle SM for the cocycle J_t + A_t, A_t(v) = log|Dg_t v|, with
eigenvalue Re z (hence Re z = int (d + a) dS by the computation of Lemma 1(ii), a(v) = <grad_v X, v>), exactly as in
Lemma C of R4-q10. I could not make this rigorous, because the decomposition (mu_0, m) is not canonical: m is
determined only modulo TM-valued measures whose divergence is a measure, and the off-diagonal term of the cocycle
is of exactly that size. Even if it were rigorous, the conclusion is a *bound* on Re z (by max_{SM}(d + a)), not a
contradiction; so this route is at best a refinement of Lemma 8.

(D6) **Strips touching 0 (suggestion (A)).** I have nothing to add beyond R8-c Corollary 2.3: the splitting
T_z = B_z + G_z has B_z holomorphic across 0, and the singular part of G_s as s -> 0+ is
(N_x(s) - e^b N_y(s)) nu-hat + o(N) with N(s) -> inf, i.e. exactly the behaviour that (F1)/(F2) permit. What is
missing is the second-order asymptotics of G_s - (that leading term) as s -> 0+, i.e. a Patterson expansion with
remainder. I looked for one and found that it requires a rate in Lemma 2.2 of R8-c (the one-sided Patterson lemma),
and that lemma's proof (weak* compactness + (F1)) is rate-free by nature; a rate would amount to an equidistribution
rate for weighted orbit averages, which is a mixing-type statement of the kind GH is not known to give.
(Indeed Corollary E of R8-f shows GH *forbids* exponential mixing rates for L^1 densities, so quantitative
equidistribution of this type cannot be expected in the form needed.)

(D7) **Making GH act at z != 0 by hypoellipticity of P - z.** Dead for the reason given in Remark 3.3 of R8-b and
re-checked: hypoellipticity of P - z for small real z > 0 already implies that
u_0 = int_{-inf}^0 e^{z s} (f o g_s) ds is smooth for every smooth f, which forces subexponential growth of the
derivatives of f o g_s and so is at least as strong as the conclusion we want. So this is circular, not a route.

---


### Block R9-h (from round9_q7 B3: multipliers cannot move the eigenvalue horizontally)
## B3. Multipliers cannot move the eigenvalue horizontally

This is the structural reason why (b) and (d) fail. A multiplier changes the eigen-parameter only through an eigenfunction relation for X, and that relation forces the multiplier to vanish wherever the eigen-density lives.

**Lemma B3.0 (support).** Let T != 0 be a distribution density with T o P = zT, and let K := supp T. Then K is a nonempty closed flow-invariant set.

*Proof.*
- Suppose psi is smooth with supp psi ∩ K = ∅. Then L_t psi = e^{J_t} psi o g_t is supported in g_{-t}(supp psi).
- So T(L_t psi) = e^{zt} T(psi) = 0, i.e. T vanishes on all smooth functions supported in g_{-t}(M \ K), for every t.
- Hence g_{-t}(M \ K) ⊂ M \ K for all t, so K is invariant. ∎

**Lemma B3.1 (division).** Let T be a distribution density of order <= 1, f in C^1(M) and K = supp T. Suppose T(f psi) = 0 for all smooth psi. Then f = 0 on K.

*Proof.*
- Suppose f(x0) != 0 for some x0 in K. Choose a neighbourhood U of x0 on which f != 0. There 1/f is C^1.
- For smooth psi supported in U, psi/f is C^1 with compact support in U, and T(psi) = T(f · (psi/f)) = 0. The last equality holds by continuity of T on C^1 and density of smooth functions in C^1.
- So x0 is not in supp T, a contradiction. ∎

**Lemma B3.2 (no bounded multiplier with real growth).** Let K be a closed invariant set, phi continuous and C^1 along orbits, and c in C with Re c != 0. Suppose X phi = c phi on K. Then phi = 0 on K.

*Proof.* For x in K, s -> phi(g_s x) solves y' = c y. So |phi(g_s x)| = e^{(Re c) s} |phi(x)|. The left side is bounded by ||phi||_inf for all s in R. Letting s -> +inf or s -> -inf, according to the sign of Re c, gives phi(x) = 0. ∎

**Proposition B3.** Let T_z != 0 be an order-<=1 eigen-density, T_z o P = z T_z, with support K. Let phi be in C^2 and c in C, and put V := T_z(phi ·).
(a) V o P = (z - c) V holds iff T_z((X phi - c phi) psi) = 0 for all psi. In that case X phi = c phi on K.
(b) V o X = (z - c) V holds iff T_z((P phi - c phi) psi) = 0 for all psi. In that case P phi = c phi on K.
(c) In case (a) with Re c != 0: phi = 0 on K. In particular, if K = M then phi = 0 and V = 0.
(d) In case (b) with Re c != 0:
 (d1) if K = M, phi has no zeros;
 (d2) for general K: every x in K with phi(x) != 0 has an orbit closure carrying flow-invariant probabilities mu_+ and mu_- with mu_+(d) >= Re c >= mu_-(d).
 In particular, (d1) is impossible.

*Proof.*
(a), (b) The equivalences are Proposition B1 with the eigenvalue moved: V(P psi) = z V(psi) - T_z((X phi) psi), and V(X psi) = z V(psi) - T_z((P phi) psi). The conclusion on K follows from Lemma B3.1 with f = X phi - c phi (resp. P phi - c phi), which is C^1.
(c) This is Lemma B3.2 applied on the invariant set K (Lemma B3.0).
(d) On K we have X phi = (c - d) phi, so for x in K, |phi(g_s x)| = |phi(x)| exp((Re c) s - J_s(x)).
- (d2) Suppose phi(x) != 0. Boundedness of phi gives (Re c) s - J_s(x) <= C' for all real s.
  - For s -> +inf, J_s(x)/s >= Re c - C'/s. So every weak* limit mu_+ of (1/s) int_0^s delta_{g_r x} dr (an invariant probability on the orbit closure, which lies in K) has mu_+(d) >= Re c.
  - For s -> -inf, the backward empirical measures (1/|s|) int_s^0 delta_{g_r x} dr have d-average -J_s(x)/|s| <= Re c + C'/|s|. So their limits mu_- satisfy mu_-(d) <= Re c.
- (d1) If K = M and phi has no zeros, log|phi| is smooth with X log|phi| = Re c - d. So d lies in R + X(C^inf), and (O3) forces the constant to vanish: Re c = 0, a contradiction. ∎

*Remark (what is rigorous in B3).* Everything stated in B3 is proved. For the weighted form (a) the conclusion is complete: phi vanishes on K. For the brief's unweighted form (b) the conclusion is weaker:
- with full support and no zeros, a shift is impossible (d1);
- in general, the multiplier can be nonzero only at points whose orbit closures carry invariant measures with mu(d) on both sides of Re c (d2).
This weaker form is natural: tilted conformal measures (Prop. 2.2 of R4-q7) show that eigen-objects with real eigenvalue mu(d) do exist, so soft arguments cannot exclude such multipliers on small invariant sets. Whether a C^2 phi with P phi = c phi on supp T_z (Re c = Re z) can exist for the families of Theorem R is not settled here. If one did exist, the unweighted coupling would turn T_z into an X-transpose eigen-family near 0. Excluding a family of that kind would still require dim I = 1 (Observation 2.1 of R8-e), i.e. (V).

**What B3 means for the approach.**
- *Idea (d) (build a family holomorphic through 0 from V_{z,phi}).* This requires V_{z,phi} o P = (z - c)V with Re(z - c) = 0, i.e. Re c = Re z != 0 throughout the strip. By B3(a) the multiplier vanishes on supp T_z. So the only C^2 multipliers that move a strip horizontally are those that kill the family on its support. For the families of Theorem R in the case lambda = 0, the support is contained in supp mu, which is M under GH (Corollary D1). If supp T_z = M, the multiplier is 0.
- *Idea (b) (vary phi to show T_z vanishes on products).* By B1, T_z(phi psi) for all phi, psi is just T_z on C^inf. There is no smaller set of products to exploit unless phi satisfies an eigen-relation, and B3 excludes that horizontally.
- *Idea (c) (Jordan chains).* Differentiating (2) in z gives V'_{z,phi}(X psi) = z V'(psi) + V(psi) - T'_z((P phi) psi). These are again the Leibniz identities for the Taylor coefficients of T, so B1 applies to each coefficient. Pairing with R gives exactly the iteration T_z(phi) = z^N T_z(R^N phi_0) of Theorem V / Lemma Q, and only in the volume case (Proposition A of R8-d).
- *Imaginary shifts.* When Re c = 0 a nonvanishing smooth multiplier with X phi = c phi may exist (a circle-valued eigenfunction, e.g. a torus factor). It moves the family vertically, which is harmless and useless.


=== END OF ROUND-9 RESULTS ===
