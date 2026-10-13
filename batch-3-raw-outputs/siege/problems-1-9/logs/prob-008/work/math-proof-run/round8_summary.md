# Running summary after round 8 planning (rounds 1-7 folded in)

## Problem and conventions
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No complete proof exists; the claim is now PROVED for dim M <= 3 (entry 61) and for all hyperbolic measures in every dimension (entry 60).

Conventions: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds = log nu-Jacobian of g_t; P = X + d acting on functions (L_X(phi nu) = (P phi) nu); I = space of X-invariant distribution densities; (V) = "X preserves a smooth positive density" (entry 19); H = smooth invariant volume + unique ergodicity + every mean-zero smooth f is Xu with u smooth. For an ergodic mu, lambda = mu(d) = sum of all Lyapunov exponents (independent of nu); chi^+_min smallest positive exponent, chi^-_max negative exponent closest to 0. Observation 0: for a density T, u = T/nu has <Xu, phi nu> = -T(P phi); by L1 the P-harmonic densities are multiples of nu.

Process notes: splice only from answer files in this run directory or the staged copies /tmp/prob008_r6/material_r5.txt, /tmp/prob008_r7/ (round-7 query material) and /tmp/prob008_r8/ (round-8 material). Grep query files for foreign text ("knot|L-space|lens").

## Standing results (never dropped; ledger numbers)
- S1 (#2, round1_q2): ker X on D' = constants (L1).
- S2 (#3, round1_q2): tame estimate ||u - mean||_{C^k} <= C||Xu||_{C^m}; X(C^inf) closed = annihilator of I.
- S3 (#4, round1_q2): no periodic orbit with Poincare Jacobian 1 (Observation P).
- S4 (#8 round2_q1, #33 round4_q5): at a zero p, d(p) != 0; jet non-resonance tr DX(p) + sum alpha_i lambda_i != 0.
- S5 (#5, round1_q3): under H, unstable-leaf formula for the transfer function. Not on the current line.
- S6 (#9, round2_q3): under H, bounded ergodic integrals, spectral estimate. Not on the current line.
- S7 (#11, round3_q1): invariant Borel sets null/conull; conservative (dim >= 2); L^1 solutions of the cohomological equation with smooth RHS are smooth; reformulations of (V).
- S8 (#12 round3_q1, #28 round4_q9): sufficient conditions for (V) (a.c. invariant probability with rho^{-eps} in L^1, etc.).
- S9 (#13, #32): no Lyapunov-stable attracting/repelling zero or periodic orbit; no proper closed invariant set has a basin of positive volume; Hopf: int_0^{+-inf} e^{J_t} dt = inf nu-a.e.
- S10 (#14, round3_q2): (V) <=> dim I = 1; (V) => H, unique ergodicity, no zeros, no periodic orbits.
- S11 (#15, round3_q4): under GH + (V): h_top = h_omega; goal under GH + (V) when omega hyperbolic or dim <= 3. Superseded in substance by S33-S35 but kept.
- S12 (#18, round3_q3): under H, long orbit segments are eps-dense. Not on the current line.
- S13 (#24-#26, round4_q1/q2): Lemma C (int_R e^{J_t(x)} dt = inf for every x, dim >= 2), Lemma D, Corollary D1 (ergodic mu with mu(d) = 0 has full support), Lemma E, Lemma F.
- S14-S17 (#27, #29, #30, #31): equivalent forms of (V).
- S18 (#34, round4_q7, no GH): tilted conformal probabilities T(P phi) = lambda T(phi) on supp mu.
- S19 (#35), S20 (#36, #37): smooth signed invariant densities; GH for closed 1-currents; conformal measures on SM.
- S21 (#40, round5_q6, no GH): lambda* > 0 gives a real eigen-distribution Xu = kappa u, kappa != 0 (pair construction, Theorem B there).
- S22 (#41, round5_q5): no L^1 eigenfunction XW = kappa W, Re kappa != 0; measure solutions are nu-singular.
- S23 (#42, round5_q8): no nu-measurable cocycle solutions with nonzero means.
- S24 (#43, round5_q1): (Lambda) is strictly stronger than the goal. Not on the current line.
- S25 (#44, #45, round5_q7, round5_q10): hyperbolic positive-entropy measures give uniformly dissipative horseshoes; proper basic sets are uniformly volume-contracting or -expanding; Anosov flows are not GH.
- S26 (#46, #47, round5_q9): Lemma H, Theorem K; no hyperbolic attracting/repelling zeros or periodic orbits.
- S27 (#48, #49, #50): invariant Borel functions const; correlation lemma; homogeneous classes; GH on S^1 excludes zeros.
New from round 6 (entries 56-68):
- S28 (#56; round6_q1 §1-2, also round6_q2 Thm G, round6_q3 Thm J, round6_q6 Lemma Z, round6_q10 Lemma M — five independent proofs, all agreeing): **Theorem J.** Under GH no nonzero distribution density S has |S(e^{J_t} phi∘g_t)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t. Proof: moments m_j(phi) = int t^j F_phi(t) dt are distributions with m_0(P phi) = 0, m_j(P phi) = -j m_{j-1}(phi); L1 gives m_0 = c_0 nu and "Xw = const => const = 0" (GH + max principle / invariant measure) kills c_0; induction kills all m_j; quasi-analyticity of the Fourier transform (holomorphic in a strip) gives F_phi = 0. Holomorphic/meromorphic-family form: any family T_z with T_z(P phi) = z T_z(phi) holomorphic (or meromorphic with bounded pole order) on a connected set containing 0 vanishes. This is the main new GH lever; it is a universal theorem.
- S29 (#57; round6_q1 §3-4, round6_q3 §2): Lemma K (Cayley-Hamilton on jets at a fixed point of g_P) and its corollaries: every connection between hyperbolic periodic orbits/zeros goes from int d < 0 to int d > 0; no hyperbolic periodic orbit or zero has a homoclinic point.
- S30 (#58; round6_q10 §4): Theorem B: no strong-unstable-to-strong-stable connection between periodic orbits at all (meromorphic continuation of orbit Laplace transforms by a transfer operator on contracting discs; cites Hennion + analytic Fredholm).
- S31 (#59): (DH) proved: no hyperbolic basic set of positive entropy.
- S32 (#60; round6_q1 Thm 5.1): under GH every positive-entropy ergodic mu is non-hyperbolic (cites Ruelle, Katok/Lian-Young).
- S33 (#61; round6_q1 Thm 5.2 and three others): **the problem's claim holds for dim M <= 3** (complete special case).
- S34 (#62; round6_q1 Prop 6.1 and four others): positive-entropy mu has mu(d) in {0} ∪ (-inf, -chi^+_min] ∪ [|chi^-_max|, inf) (cites Pesin, Ledrappier-Young). Also Lemma 6.0 (round6_q1, proved): h_mu > 0 => unstable conditionals non-atomic a.e.
- S35 (#63; round6_q4): GH passes to submersion factors; products reduce; constant-roof suspension is GH iff base diffeo is GH (so the flow problem contains the diffeomorphism problem).
- S36 (#64; round6_q5): periodic-orbit jet non-resonance |det A| mu^alpha != 1; no orbit from a uniformly volume-expanding to a uniformly volume-contracting compact invariant set.
- S37 (#65; round6_q8): positive Patterson eigen-measures: delta_m = 0 => omega(supp m) = M; (PE) <= (Q).
- S38 (#66; round6_q9): structure of empirical limit sets V^{+-}; (Z0-lin) <=> no positive eigen-measure with real nonzero eigenvalue.
- S39 (#67; round6_q7): under GH + (V): h_top > 0 iff omega has a positive exponent, then also a transverse zero exponent; smooth observables have spectral measures flat to infinite order at 0; tame C^1 transfer functions.
- Conditional (#68 OPEN; round6_q1 Prop 6.2, round6_q2 6(d), round6_q3 Prop 4.2, round6_q6 §5.1): with tempered non-stationary normal forms on Pesin unstable leaves (vanishing-moment combinations of k+1 points), every positive-entropy mu has mu(d) = 0; 1-dimensional unstable leaves need only affine parameters (sketch).

New from round 7 (entries 71-80; all universal under GH unless marked; none shortens the chain):
- S40 (#71; round7_q10 §2, also q2, q3, q7): Theorem J* — Theorem J with any two-sided quasi-analytic decay (moments M_j with sum M_j^{-1/j} = inf, e.g. e^{-|t|/log(e+|t|)}); sharp for the moment method (Paley-Wiener, round7_q7 Remark 1.3).
- S41 (#72; round7_q10 §3, round7_q6 Thm G with flow shifts over C[R], round7_q9 Lemma G, round7_q3 Prop Q): Theorem G — no finite weighted configuration cancelling in every exponentially-forward class and every backward class (Jacobian growth of representatives below the rate); more points than classes impossible; no closed su-cycle with zero Jacobian holonomy; with smooth volume no closed su-cycle, no doubly asymptotic pair. Temporal (flow-shift) defects and Jacobian holonomy are absorbed exactly (round7_q6); genuine center defects are not.
- S42 (#73; round7_q1 §2, round7_q6 Prop 4.1): Proposition N — lambda = mu(d) < 0 forces all entropy into exponents <= |lambda| (LY-II cited); |lambda| >= h/(n-2).
- S43 (#74; round7_q5 §1, round7_q1 §3): Theorem J and the whole hyperbolic chain use GH only via (K0) ker X = constants and (K1) no u with Xu = 1; hence a Theorem-J-only proof of PE-NH would prove zero entropy for all (K0)+(K1) flows (incl. "DUE volume flows", status unknown). Diagnostic: the closed-range/tame part of GH has never been used in the main line.
- S44 (#75; round7_q4 Prop 1.1, round7_q8): PE-NH is equivalent to the goal in dim >= 4 (given entry 60).
- S45 (#76; round7_q8 Lemmas A-F): tame estimate, closed range, dual tame solvability T = S∘X for T(1) = 0, bounded Birkhoff integrals on X(C^inf), Lebesgue class ergodic, a.c. invariant h nu with log h in L^1 is smooth, volume case = cohomology-free with tame bounds.
- S46 (#77; round7_q7): Lemma H (Carleman uniqueness for eigen-families on a half-disc), Theorem V (volume case: lambda* > 0 => quasi-analytic vectors of X^{-1} not C^1-dense), Proposition O (Hennion route has r_ess >= 1 with zero exponents).
- S47 (#78; round7_q4): integrable two-sided decay => open set of imaginary eigenvalues on D' (no GH); uniquely ergodic + rigid => h_top = 0; volume case: singular spectrum => h_top = 0; Liouville criterion (u_n with ||Xu_n||_{C^m} -> 0, ||u_n||_{C^0} = 1 => not GH); template (1) of skew products over Diophantine flows = constant-roof suspension; products never minimal counterexamples.
- S48 (#79; round7_q4 Lemma 3.1): W^u_loc(x) holds at most one forward volume-contracting point.
- S49 (#80; round7_q2 Lemma 3.1, no GH): mu(d) = 0 => int e^{J_t} diverges both ways a.e. (weights never give integrability at lambda = 0).

## Dead ends (refuted statements only)
- #17 (round3_q3): "under H, x -> int_0^T f(g_t x) dt is Lipschitz uniformly in T" is false.
- #51 (round5_q7): "a closed 1-current killing closed 1-forms equals dW for a generalized function W" is false for dim M >= 3.
(No statement was refuted in round 7.)

## Set aside, not refuted (open to re-attack)
- (Lambda) [#39]: strictly stronger than the goal. (E1) [#38] (no real eigenvalue of X on D'): with entry 40 it implies (Lambda), so also stronger than the goal; L^1 case proved. (Z0-lin) [#55]: open.
- The (V) line [#19] and volume core #16 (= "cohomology-free with tame estimates + uniquely ergodic smooth volume => zero entropy", a Katok-conjecture-type statement): open; round7_q4 (Q2-Q3: singular spectrum; algebra-coboundary variance), round7_q7 Theorem V (quasi-analytic vectors), round7_q8 (*) reduce it but do not close it.
- Conjecture (C) (GH-free existence of two-sided decaying S for non-hyperbolic positive-entropy mu): round7_q5 shows it implies DUE-0; not refuted.
- su-grids / configurations (Theorem G): the needed configurations (CH) (round7_q10 Prop 4.1; round7_q6 (O1); round7_q9) are absent for non-hyperbolic mu because closing an su-path costs c - 1 >= 1 center conditions; center smearing provably gives no decay (round7_q6 §3(b), q7 §4.3, q9 §3, q10 §4.2).
- Continuation across Re z = 0 via Pesin-block transfer operators: blocked by Proposition O (round7_q7); no continuation source known.
- Quasi-analytic decay (iii): now a theorem (S40) but still needs two-sided cancellation; no new case.
- Directional weights via closed currents: give nothing beyond Theorem J (round7_q2 Cor 2.2).
- Positive (zero-order) Patterson/conformal constructions; Grassmannian/Kozlovski volume growth; bump test under (V); single-orbit Laplace transforms; spectral route (M); return times; local saddle constructions: as recorded in earlier rounds.

## Diagnostics
- Theorem J converts GH into: "no nonzero distribution whose weighted transport decays exponentially in both time directions". Every round-6 success builds such an S from finitely many points: backward cancellation inside an unstable leaf (pairs, vanishing moments, Cayley-Hamilton at a periodic point) plus forward decay either from e^{J_t} (lambda < 0) or from cancellation at a periodic point (Lemma K both ways; Theorem B).
- The remaining case is a non-hyperbolic positive-entropy mu (dim >= 4), essentially with lambda = 0 (the lambda != 0 band beyond the exponent gap needs only normal forms, #68). At lambda = 0 e^{J_t} = e^{o(|t|)} both ways at generic points, so S needs simultaneous cancellation forward (stable side) and backward (unstable side): su-cycles/rectangles, which non-hyperbolic measures do not provide (dim W^s + dim W^u <= n - 2), and the holonomy of the Jacobian weights around a cycle is generically nonzero.
- Classical facts usable in any chain: Young (surface flows zero entropy), variational principle, Ruelle's inequality, Katok/Lian-Young horseshoes, Pesin and Ledrappier-Young theory, Newhouse upper semicontinuity of entropy for C^inf maps, Przytycki/Kozlovski.

- Added after round 7: the main line has used GH only through (K0)+(K1) (S43); the tame closed-range half of GH (S45) has entered no main-line argument. Every round-7 mechanism (grids, continuation, quasi-analytic decay, centre smearing) stops at the same point: at mu(d) = 0 a non-hyperbolic mu offers cancellation on one side only.
- One-sided cancellation is available for EVERY positive-entropy ergodic mu (planner computation, round 8; see the sketch below): a Pesin pair gives S with exponential decay on one side and growth at a strictly smaller rate on the other side, for X or for -X.

## The chain and the missing statement

(No complete written proof or refutation of the [GOAL] claim is in hand: all ten round-7 files stop at non-hyperbolic positive-entropy measures with mu(d) = 0 in dim >= 4; none refutes anything.)

**Chain.** (unchanged from round 7)
1. (Missing statement, PE-NH; ledger entry 70) Under GH no ergodic flow-invariant mu has h_mu(g_1) > 0 and a zero Lyapunov exponent of multiplicity >= 2.
2. (Entry 60, PROVED modulo Ruelle's inequality and the Katok/Lian-Young horseshoe theorem for flows; uses Theorem J (entry 56) through Lemma K / no-homoclinic (entry 57)) Under GH with dim M >= 2, every ergodic flow-invariant mu with h_mu(g_1) > 0 has a zero exponent transverse to X, i.e. exponent 0 of multiplicity >= 2. (For dim M = 1, M is a circle and g_1 is a circle homeomorphism: entropy 0.)
3. By 1 and 2, every ergodic flow-invariant mu has h_mu(g_1) = 0 (this is (PE), entry 53's claim).
4. Classical (variational principle, checked by round5_q2, round6_q1 §5, round6_q10 §6, round7_q3 §1, round7_q10 §1): h_top(g_1) = sup h_m(g_1) over g_1-invariant m; for such m, mbar = int_0^1 (g_s)_* m ds is flow-invariant with h_mbar(g_1) = h_m(g_1) (g_s conjugates g_1 to itself; entropy affine, Jacobs); by the flow-ergodic decomposition of mbar and Jacobs' formula, h_m(g_1) <= sup over flow-ergodic mu of h_mu(g_1) = 0 by 3. Hence h_top(g_1) = 0, the [GOAL]. (Entry 61 already gives the [GOAL] for dim M <= 3 independently.)
Alternative chain (round 8, for the record): (J1) [entry 81] applied to X and to -X, plus Pesin local stable/unstable manifolds, Ruelle's inequality and Lemma 6.0 (non-atomic conditionals), gives step 3 directly for every ergodic mu, bypassing step 2 and the Katok/Lian-Young citation. J1 is stronger than PE-NH, so it is posed as the hardest step of the sketch, not as the missing statement.

**Missing statement (PE-NH).** Let M be a compact connected smooth manifold and X a smooth vector field on M with flow g_t, such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Then there is no ergodic flow-invariant Borel probability measure mu on M such that (a) h_mu(g_1) > 0 and (b) the Lyapunov exponent 0 of the C^inf diffeomorphism g_1 with respect to mu has multiplicity at least 2 (i.e. mu is non-hyperbolic: besides the exponent 0 of the flow direction there is a further zero exponent). (By entries 61 and 62 below, a proof may assume dim M >= 4 and, if useful, mu(d) in {0} ∪ (-inf, -chi^+_min] ∪ [|chi^-_max|, inf), where d = div_nu X for a smooth positive density nu, chi^+_min is the smallest positive and chi^-_max the negative exponent of mu closest to 0; mu(d) is the sum of all exponents of mu.)
(Wording unchanged; ledger entry 70 stays in force. Entry 73 narrows the case mu(d) != 0 further.)

**Why it should hold (planner sketch, revised in round 8).**
(1) One-sided cancellation is free. Let mu be ergodic with h_mu(g_1) > 0, lambda = mu(d), chi^+_min > 0 > chi^-_max, 0 < delta small. If lambda = 0, take mu-generic x != y in one Pesin local unstable leaf (Lemma 6.0), S = delta_x - e^b delta_y: |S(e^{J_t} phi∘g_t)| <= C e^{-(theta-delta)|t|}||phi||_{C^1} for t <= 0 (theta < chi^+_min) and <= C e^{delta t}||phi||_{C^0} for t >= 0. If lambda > 0, take x != y in one local stable leaf: decay e^{-(lambda-delta)|t|} backward (weight), growth <= e^{max(0, lambda - theta' + delta) t} forward. If lambda < 0, the same for -X (GH by (O4)). In every case the decay rate eps exceeds the growth rate a >= 0 on the other side.
(2) Hence (J1) [entry 81] — "under GH no nonzero S decays like e^{-eps|t|} as t -> -inf and grows at most like e^{at}, a < eps, as t -> +inf" — implies PE outright. Theorem J is the case of decay on both sides (a < 0). In Laplace form J1 says: no polynomially bounded holomorphic eigenfamily T_z(P phi) = z T_z(phi) on the strip a < Re z < eps whose backward half B_z(phi) = int_{-inf}^0 e^{-zt} F_phi(t) dt (holomorphic on the half-plane Re z < eps, which contains 0) satisfies B_z(P phi) - z B_z(phi) = S(phi). At z = 0 the Taylor coefficients give B_0∘P = S, B_j∘P = B_{j-1}, with |B_j| <= eps^{-j-1}|S|-type bounds: S is infinitely P^T-divisible with geometrically bounded divisors. Candidate mechanism: combine this with the tame dual solvability of S45 (divisors of controlled order, unique mod nu by (K0), normalised by (K1)) and with the forward half F_z (holomorphic on Re z > a) to force a holomorphic continuation of T_z to a neighbourhood of 0, whereupon Theorem J (Lemma M form) kills it. I cannot close it: GH speaks about P at z = 0 only, and shifting the weight (J_t -> J_t + ct) would need a smooth w with Xw = c, which is exactly what (K1) forbids.
(3) Closed range must enter somewhere (S43). In the volume case Theorem V asks for C^1-dense quasi-analytic vectors of X^{-1}; the natural candidates rho(A)phi = int rho^(t) phi∘g_t dt with rho flat at 0 need rho^ of non-quasi-analytic decay and are then smooth only if ||Dg_t|| grows subexponentially — circular. So the tame inverse must be used on objects not built by transporting smooth functions (e.g. on the divisors B_j of (2), or on Hahn-Banach solutions S_{pq} of S∘X = delta_p - delta_q for pairs p, q).
(4) Fallback mechanism: an accessibility dichotomy for the zero-exponent centre (invariance principle of Ledrappier / Avila-Viana type): either su-paths of good points close modulo the flow often enough to give a Theorem-G configuration with more points than classes, or the conditionals along the centre are su-holonomy invariant, giving a measurable structure to be contradicted by GH (S45 ergodicity of Lebesgue class, S41).

**Tried so far** (on PE-NH, on its earlier wordings (PE) [#53] and (Lambda) [#39], and on the goal directly):
- round1_q1-q4: first reductions (L1, tame estimate, transfer formula, hyperbolic case under H). Yield: S1-S5.
- round2_q2 (spectral route), round2_q3, round3_q3 (bounded ergodic integrals, return times): obstructions only.
- round3_q4: GH + volume: hyperbolic case and dim <= 3 under (V) (S11).
- round4_q10: conformal measures on SM: reduction to (E1) + (E2).
- round5_q1, q2, q3, q10 (closing on Lambda): Lambda strictly stronger than the goal; dissipative horseshoes.
- round5_q4 (refute Lambda): no counterexample. round5_q5 (E1): L^1 case. round5_q6 (N): proved without GH. round5_q7 (Pesin/unstable constructions). round5_q8 (quantitative tame estimates): cocycles. round5_q9 ((V) via (Z0)).
- round6_q1, q2, q3, q10 (closing on PE): Theorem J; hyperbolic measures excluded; dim <= 3 solved; band; normal-form sketch. Stop at non-hyperbolic mu(d) = 0.
- round6_q4 (refute PE): reductions only. round6_q5 (DH): jet non-resonance. round6_q6 (generic pairs + L1): Lemma Z. round6_q7 (Kozlovski + measurable tools): obstructions. round6_q8 (Patterson): reduces to (Q). round6_q9 (Z0-lin): reformulations.
- round7_q1, q2, q3, q9, q10 (closing on PE-NH, identical): Theorem J* (quasi-analytic decay), Theorem G (configuration criterion), Prop N (wider band, LY-II), DUE observation, Atkinson divergence; all stop at the absence of two-sided cancellation for non-hyperbolic mu at mu(d) = 0.
- round7_q4 (refute PE-NH): equivalence with the goal; templates reduced (suspensions, products, rigid/Liouville constructions excluded); Lemmas 3.1-3.3; no counterexample.
- round7_q5 (Conjecture (C), GH-free): (C) implies DUE-0; Theorem J uses only (K0)+(K1); nothing on (C) itself.
- round7_q6 (su-grids with centre smearing): Theorem G with flow shifts; centre smearing provably gives no decay; obstruction = c - 1 centre closing conditions.
- round7_q7 (continuation via Pesin-block transfer operators + quasi-analytic decay): Lemma H, Theorem V; Proposition O kills the Hennion route.
- round7_q8 (statement-only; first move = closed graph/closed range + invariant indicators): Lemmas A-F; volume case reduced to a Katok-type statement; no proof.

## Where the next round should concentrate (round 8 wave)

Progress test: the last two rounds produced progress on the chain only in round 6 (Theorem J, a universal theorem that excluded hyperbolic measures and replaced PE by PE-NH). Round 7 produced no progress in the sense of rule (iv): its universal results (Theorem J*, Theorem G, Proposition N, Lemma H) sharpen tools and narrow the case mu(d) != 0 but do not shorten the chain; the hard part (non-hyperbolic, mu(d) = 0) is untouched. What differs in my sketch from round 7: round 7's sketch sought two-sided cancellation (grids, centre smearing, continuation, weaker decay), all Theorem-J-only; the new sketch (a) observes that one-sided cancellation with a rate gap is available for every positive-entropy measure and isolates the one-sided analytic statement (J1) that would finish from it, and (b) insists on using the tame closed-range half of GH, which no main-line attempt has used.
Wave (escalation rule; 10 queries, all attempt):
- q1, q2, q3, q4: identical closing task on PE-NH, carrying the round-7 material (background, Theorem J with proof, Lemma K, Theorem 5.1/5.2, Prop 6.1, Lemma 6.0, R5-a, Lemma M, Theorem B, R6-d/e/f) plus round-7 splices (Theorem J*, Theorem G, Prop 4.1 of round7_q10, (K0)/(K1) and Prop 3.1 of round7_q5, Prop N, Lemmas A-F of round7_q8, Lemma H/Theorem V/Prop O of round7_q7, round7_q6 §1 and §3, round7_q4 Lemma 3.2 and S3.5), and the revised sketch.
- q5: the hardest step of the sketch cut out: prove (J1) (entry 81), or show it fails for some flow satisfying GH; with Theorem J's proof, Lemma M, Lemma H, Theorem V, closed-range lemmas.
- q6: named approach "tame closed range / dual solvability" (never used in the main line): attack PE-NH using Lemma B(iii) of round7_q8 together with Theorem J, e.g. through infinitely divisible pair distributions and their divisors.
- q7: named approach "invariance principle / accessibility dichotomy for the centre" feeding Theorem G.
- q8: statement-only query (PE-NH has now been attacked in rounds 7 and, as PE, 6): derive the chain and attack by a first move none of the listed attempts used.
- q9: one more identical copy of the closing task.
- q10 (one of the at most two 'elsewhere' queries): the set-aside volume core [#16, #19 route]: "cohomology-free with tame bounds + uniquely ergodic smooth volume => zero entropy", by the algebra/variance mechanism (products u·(u∘g_s) of coboundaries, round7_q4 Q3) or singular spectrum (round7_q4 Lemma 3.3(c)).
Next round: if PE-NH, J1 (with the chain of the sketch), or the goal is proved, record PROVED [GOAL] citing the entries used and send two verify queries carrying the whole chain. If J1 is refuted by a GH example, record it and drop the alternative chain (PE-NH stands). If nothing moves in round 8, round 9 must change the decomposition (e.g. adopt J1 or a closed-range statement as the missing statement only if a worker shows it plausible), and by round 12-13 plan the final document around the standing results.
