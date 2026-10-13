# Running summary after round 7 planning (rounds 1-6 folded in)

## Problem and conventions
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No complete proof exists; the claim is now PROVED for dim M <= 3 (entry 61) and for all hyperbolic measures in every dimension (entry 60).

Conventions: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds = log nu-Jacobian of g_t; P = X + d acting on functions (L_X(phi nu) = (P phi) nu); I = space of X-invariant distribution densities; (V) = "X preserves a smooth positive density" (entry 19); H = smooth invariant volume + unique ergodicity + every mean-zero smooth f is Xu with u smooth. For an ergodic mu, lambda = mu(d) = sum of all Lyapunov exponents (independent of nu); chi^+_min smallest positive exponent, chi^-_max negative exponent closest to 0. Observation 0: for a density T, u = T/nu has <Xu, phi nu> = -T(P phi); by L1 the P-harmonic densities are multiples of nu.

Process notes: splice only from answer files in this run directory or the staged copies /tmp/prob008_r6/material_r5.txt (background L1, L2, (O1)-(O4), P1, Observation P, Lemmas C-F incl. Corollary D1, B3, B4, Lemma H, round4_q10 Lemmas A-C) and /tmp/prob008_r7/ (round-7 query material). Grep query files for foreign text ("knot|L-space|lens").

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

## Dead ends (refuted statements only)
- #17 (round3_q3): "under H, x -> int_0^T f(g_t x) dt is Lipschitz uniformly in T" is false.
- #51 (round5_q7): "a closed 1-current killing closed 1-forms equals dW for a generalized function W" is false for dim M >= 3.

## Set aside, not refuted (open to re-attack)
- (Lambda) [#39, retracted as missing statement]: strictly stronger than the goal.
- (E1) [#38]: proved for L^1; singular part open. (Z0-lin) [#55]: open; round6_q9 reformulated it (S38) and showed nu-typical orbits do not supply the needed expanding-to-contracting orbit.
- The (V) line [#19] and the volume-preserving non-hyperbolic core #16: open; now a sub-case of (PE-NH) (lambda = 0 automatically under (V)).
- Positive (zero-order) Patterson/conformal constructions: exhausted (round6_q8 Lemma 1, Cor 4-5; round6_q5 §3.3): they reduce to (Q).
- Grassmannian/Kozlovski volume growth (round6_q7 §4.1): GH does not act on fibre cocycles.
- Bi-asymptotic pair bump test under (V) (round6_q7 §4.3): Cantor-gap example shows passages can cancel; needs a generic-position input.
- Single-orbit Laplace transforms at lambda = 0: Re z = 0 is the boundary of holomorphy for generic Pesin points (round6_q6 §5.2, round6_q10 §7 R2); continuation across it would suffice (Lemma Z/M) but is unavailable without periodic self-similarity.
- Older: spectral route (M) #10, return times, local saddle constructions, smearing conformal weights, Krein-Rutman eigenmeasures on SM.

## Diagnostics
- Theorem J converts GH into: "no nonzero distribution whose weighted transport decays exponentially in both time directions". Every round-6 success builds such an S from finitely many points: backward cancellation inside an unstable leaf (pairs, vanishing moments, Cayley-Hamilton at a periodic point) plus forward decay either from e^{J_t} (lambda < 0) or from cancellation at a periodic point (Lemma K both ways; Theorem B).
- The remaining case is a non-hyperbolic positive-entropy mu (dim >= 4), essentially with lambda = 0 (the lambda != 0 band beyond the exponent gap needs only normal forms, #68). At lambda = 0 e^{J_t} = e^{o(|t|)} both ways at generic points, so S needs simultaneous cancellation forward (stable side) and backward (unstable side): su-cycles/rectangles, which non-hyperbolic measures do not provide (dim W^s + dim W^u <= n - 2), and the holonomy of the Jacobian weights around a cycle is generically nonzero.
- Classical facts usable in any chain: Young (surface flows zero entropy), variational principle, Ruelle's inequality, Katok/Lian-Young horseshoes, Pesin and Ledrappier-Young theory, Newhouse upper semicontinuity of entropy for C^inf maps, Przytycki/Kozlovski.

## The chain and the missing statement

(No complete written proof or refutation of the [GOAL] claim is in hand: every round-6 file stops at non-hyperbolic positive-entropy measures in dim >= 4. The old missing statement (PE) [#53] is retracted as missing statement (entry 69), being replaced by the narrower-but-equivalent-in-the-chain (PE-NH), since entry 60 now settles all hyperbolic measures.)

**Chain.**
1. (Missing statement, PE-NH; ledger entry 70) Under GH no ergodic flow-invariant mu has h_mu(g_1) > 0 and a zero Lyapunov exponent of multiplicity >= 2.
2. (Entry 60, PROVED modulo Ruelle's inequality and the Katok/Lian-Young horseshoe theorem for flows; uses Theorem J (entry 56) through Lemma K / no-homoclinic (entry 57)) Under GH with dim M >= 2, every ergodic flow-invariant mu with h_mu(g_1) > 0 has a zero exponent transverse to X, i.e. exponent 0 of multiplicity >= 2. (For dim M = 1, M is a circle and g_1 is a circle homeomorphism: entropy 0.)
3. By 1 and 2, every ergodic flow-invariant mu has h_mu(g_1) = 0 (this is (PE), entry 53's claim).
4. Classical (variational principle, checked by round5_q2, round6_q1 §5, round6_q10 §6): h_top(g_1) = sup h_m(g_1) over g_1-invariant m; for such m, mbar = int_0^1 (g_s)_* m ds is flow-invariant with h_mbar(g_1) = h_m(g_1) (g_s conjugates g_1 to itself; entropy affine, Jacobs); by the flow-ergodic decomposition of mbar and Jacobs' formula, h_m(g_1) <= sup over flow-ergodic mu of h_mu(g_1) = 0 by 3. Hence h_top(g_1) = 0, the [GOAL]. (Entry 61 already gives the [GOAL] for dim M <= 3 independently.)

**Missing statement (PE-NH).** Let M be a compact connected smooth manifold and X a smooth vector field on M with flow g_t, such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Then there is no ergodic flow-invariant Borel probability measure mu on M such that (a) h_mu(g_1) > 0 and (b) the Lyapunov exponent 0 of the C^inf diffeomorphism g_1 with respect to mu has multiplicity at least 2 (i.e. mu is non-hyperbolic: besides the exponent 0 of the flow direction there is a further zero exponent). (By entries 61 and 62 below, a proof may assume dim M >= 4 and, if useful, mu(d) in {0} ∪ (-inf, -chi^+_min] ∪ [|chi^-_max|, inf), where d = div_nu X for a smooth positive density nu, chi^+_min is the smallest positive and chi^-_max the negative exponent of mu closest to 0; mu(d) is the sum of all exponents of mu.)

**Why it should hold (planner sketch, at most fifteen lines).** By Theorem J (entry 56) it suffices to build, from a non-hyperbolic positive-entropy ergodic mu, ONE nonzero distribution density S (finite order) with |S(e^{J_t} phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k} in both time directions. Conjecture (C), GH-free: every C^inf flow with such a mu admits such an S. Evidence: every hyperbolic configuration admits one (pairs on unstable leaves when -chi^+_min < mu(d) < 0; Cayley-Hamilton combinations along the orbit of a homoclinic point of a periodic orbit, which cancel in BOTH directions at once; exponentially mixing volume flows, where S = (smooth mean-zero function) times volume works); for flows of zero entropy such as Diophantine linear flows no S exists (transport is an isometry of H^{-k}).
Candidate mechanisms for (C) at mu(d) = 0:
(i) su-grids: by Ledrappier-Young (applied to g_1 and g_{-1}) both unstable and stable conditionals are non-atomic; a finite combination of points with one linear cancellation condition per unstable class and per stable class has a nonzero solution once the bipartite incidence graph has more edges than vertices (round6_q3 §4); the needed rectangles fail for non-hyperbolic mu because W^s and W^u do not meet, so replace points by smooth densities along the missing center/flow directions (distributions spread over a center transversal), turning the temporal/center closing defect into a derivative that the C^k norm absorbs.
(ii) continuation: the pair Laplace transform T_z (holomorphic on 0 < Re z < theta) is an eigenfamily; any continuation across Re z = 0 that is meromorphic with bounded pole order kills it (Lemma Z/M). Theorem B obtained continuation from exact periodicity via a transfer operator on a contracting disc; for mu use returns of a generic orbit to a Pesin block (approximate self-similarity) and a transfer operator on unstable discs of the block, whose essential spectral radius is small on C^K.
(iii) weaker decay: Theorem J's last step only needs quasi-analyticity; decay e^{-w(|t|)} with int^inf w(t) t^{-2} dt = inf (Denjoy-Carleman), uniform in C^k, already forces S = 0, which may be reachable with subexponential (CLT-size) Jacobian fluctuations when mu(d) = 0 if forward cancellation of a stable cluster is available.
I cannot close any of (i)-(iii); (i) seems the most concrete.

**Tried so far** (on (PE-NH), on its earlier wordings (PE) [#53] and (Lambda) [#39], and on the goal directly):
- round1_q1-q4: first reductions (L1, tame estimate, transfer formula, hyperbolic case under H). Yield: S1-S5.
- round2_q2 (spectral route), round2_q3, round3_q3 (bounded ergodic integrals, return times): obstructions only.
- round3_q4: GH + volume: hyperbolic case and dim <= 3 under (V) (S11); core #16 open.
- round4_q10: conformal measures on SM: reduction to (E1) + (E2).
- round5_q1, q2, q3, q10 (identical closing task on Lambda): Lambda strictly stronger than the goal; dissipative horseshoes; correlation lemma.
- round5_q4 (refute Lambda): no counterexample; homogeneous/product classes cleared.
- round5_q5 (E1): L^1 case. round5_q6 (N): proved without GH. round5_q7 (Pesin/unstable constructions): dim-3 reduction to (H3). round5_q8 (quantitative tame estimates): measurable cocycles. round5_q9 ((V) via (Z0)): Lemma H, Thm K.
- round6_q1, q2, q3, q10 (identical closing task on PE): Theorem J (Jordan chain at z = 0) found independently by all four; hyperbolic measures excluded via Lemma K / Sternberg / Theorem B; dim <= 3 solved; band Prop 6.1; normal-form sketch for mu(d) != 0. Stop at non-hyperbolic mu(d) = 0 (no two-sided cancellation).
- round6_q4 (refute PE): no counterexample; factor/product/suspension reductions; surviving templates: skew products over Diophantine flows with chaotic fibres (non-hyperbolic), dissipative horseshoes (now excluded).
- round6_q5 (DH): periodic jet non-resonance; set version of Prop 4.0; DH itself then closed by round6_q1/q10.
- round6_q6 (generic pairs + L1 at z = 0): Lemma Z, pair theorem; lambda = 0 out of reach (strip boundary).
- round6_q7 (Kozlovski volume growth + nu-measurable tools): (V)-case equivalences; Grassmann cocycles invisible to GH; Cantor-gap obstruction for the bump test.
- round6_q8 (Patterson on unstable discs + Lemma H): positive constructions reduce to (Q); exhausted.
- round6_q9 (Z0-lin): reformulations only.

## Where the next round should concentrate (round 7 wave)

Progress test: rounds 5-6 produced progress on the chain in the sense of rule (iv). Round 6 proved Theorem J (entry 56), a universal theorem valid for every GH flow, which is the missing lever of every earlier sketch and, through Lemma K / Theorem B (entries 57-58) and entry 60, removes all hyperbolic positive-entropy measures and solves dim M <= 3 (entry 61). Honest caveat: the missing statement itself only narrowed (PE -> PE-NH); its hard part (non-hyperbolic, essentially mu(d) = 0) is untouched, and the round-6 workers all stopped exactly there.
Wave (escalation rule; PE-NH posed for the first time, earlier wordings PE (R6) and Lambda (R5) attacked in two rounds):
- q1, q2, q3, q9, q10: identical closing task on (PE-NH), carrying the background, Theorem J with proof, Lemma K and corollaries, Theorem 5.1/5.2, Prop 6.1, Lemma 6.0, Prop 6.2 sketch (round6_q1 whole), R5-a pair construction, Lemma M + Theorem B (round6_q10 §2, §4, §7), round6_q6 §5.2 and round6_q3 §4 (why lambda = 0 stops; grid remark).
- q4: try to REFUTE (PE-NH) exactly as stated (a GH flow with a non-hyperbolic positive-entropy measure; templates: skew products over Diophantine flows with chaotic fibres, suspensions of a GH diffeomorphism), or derive from it something false.
- q5: hardest step of the sketch cut out, GH-free: conjecture (C) (a nonzero distribution with two-sided exponentially decaying weighted transport exists for every C^inf flow with a non-hyperbolic positive-entropy ergodic measure) — prove or refute.
- q6: named approach (i): su-grids with smoothing along center/flow directions, feeding Theorem J.
- q7: named approach (ii)+(iii): strengthen Theorem J (quasi-analytic decay; one-sided decay plus continuation) and obtain continuation across Re z = 0 from Pesin-block returns (approximate self-similarity, transfer operators on unstable discs), generalizing Theorem B.
- q8: statement-only query: given PE-NH and the cited entries' statements only, derive that it completes the goal and attack it by a first move none of the listed attempts used.
Next round: if (PE-NH) or the goal is proved, record PROVED [GOAL] (citing entries 60, 56, 57 and the new locator) and send two verify queries carrying the whole chain (entry 60's proof = round6_q1 §1-5; chain step 4 as above). If (C) is proved (q5), the chain is complete via Theorem J: same. If PE-NH is refuted by a verified GH flow with positive entropy, the problem's claim is false (two verify queries before concluding).
