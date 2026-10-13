# Running summary after round 6 planning (rounds 1-5 folded in)

## Problem and conventions
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No complete proof exists.

Conventions: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds = log nu-Jacobian of g_t; P = X + d acting on functions (L_X(phi nu) = (P phi) nu); I = space of X-invariant distribution densities; (V) = "X preserves a smooth positive density" (entry 19); H = smooth invariant volume omega + unique ergodicity + every omega-mean-zero smooth f is Xu with u smooth (tame estimates). lambda* = lim (1/t) log max_x ||Dg_t(x)||. Observation 0: for a measure/distribution density T, u = T/nu has <Xu, phi nu> = -T(P phi); so by L1 the only T with T(P phi) = 0 for all phi are c nu ("P-harmonic densities are multiples of nu") — the main GH lever found so far.

Process notes: round-4 queries q6-q9 carried a foreign paragraph by mistake (workers ignored it). Splice only from files in this run directory or the staged copy /tmp/prob008_r6/material_r5.txt (= background material of the round-5 queries: Texts A/B, O1-O4, P1, Observation P, Lemmas C-F, Prop 2.1/2.2, B3/B4, Lemma H jets, round4_q10 Lemmas A-C); grep query files for "knot|L-space|lens".

## Standing results (never dropped; ledger numbers)
- S1 (#2, round1_q2): ker X on D' = constants (L1).
- S2 (#3, round1_q2/round1_q1): tame estimate ||u - mean||_{C^k} <= C||Xu||_{C^m}; X(C^inf) closed = annihilator of I.
- S3 (#4, round1_q2; round2_q4): no periodic orbit with Poincare Jacobian 1.
- S4 (#8, round2_q1; #33 round4_q5): at a zero p, d(p) != 0; jet non-resonance tr DX(p) + sum alpha_i lambda_i != 0.
- S5 (#5, round1_q3): under H, unstable-leaf formula for the transfer function. Not on the current line.
- S6 (#9, round2_q3): under H, bounded ergodic integrals, spectral estimate. Not on the current line.
- S7 (#11, round3_q1): N1 invariant Borel sets null/conull; N2 conservative (dim >= 2); N3 L^1 solutions of cohomological equation with smooth RHS are smooth; N4 reformulations of (V).
- S8 (#12, round3_q1; #28 round4_q9): a.c. invariant probability with rho^{-eps} in L^1, or density >= delta on an open set, or a nonzero continuous signed invariant density, gives (V).
- S9 (#13, #32; round3_q1, round4_q4): no Lyapunov-stable attracting/repelling zero or periodic orbit; no proper closed invariant set has a basin of positive volume; Hopf: int_0^{+-inf} e^{J_t} dt = inf nu-a.e.
- S10 (#14, round3_q2): (V) <=> dim I = 1; (V) => H, unique ergodicity, no zeros, no periodic orbits.
- S11 (#15, round3_q4; also round5_q2 Thm 4.1, round5_q3 Prop V3): under GH + (V): h_top = h_omega, omega non-hyperbolic (Katok closing, cited); full solution of the special case GH + (V) + dim M <= 3. Not on the current line.
- S12 (#18, round3_q3): under H, orbit segments of length >= C eps^{-m-n} are eps-dense. Not on the current line.
- S13 (#24-#26, round4_q1/q2): Lemma C (int_R e^{J_t(x)} dt = inf for every x, dim >= 2), Lemma D (Patterson orbit averages with subexponential J converge to nu-hat; ergodic mu with mu(d) = 0 has full support, Cor D1), Lemma E (UE => mu(d) = 0, minimal), Lemma F ((V) <=> P is GH).
- S14 (#27, round4_q6): (V) <=> some x has sup_{t>=0}|J_t(x)| < inf; Principle G; Corollary 4.
- S15 (#29, round4_q7 etc.): (V) <=> P(C^inf) closed <=> X(D') weak*-closed <=> C^inf subset X(D') + R.
- S16 (#30, round4_q1): (V) <=> sup_{t,x}|J_t| < inf <=> bounded Cesaro means of F(t) = -int J_t d nu-hat.
- S17 (#31, round4_q4): (V) <=> S(d) = 0 for every S in I.
- S18 (#34, round4_q7 Prop 2.2; no GH): every ergodic mu with mu(d) = lambda carries a tilted conformal probability T with T(P phi) = lambda T(phi); ergodic mu_+, mu_- with mu_+(d) >= 0 >= mu_-(d) exist.
- S19 (#35, round4_q7): smooth signed invariant densities have constant sign, dimension <= 1.
- S20 (#36, #37, round4_q10): GH extends to closed 1-currents; under GH + volume, measurable invariant vector fields are divergence-free; conformal probability S on SM gives T_S of order 1 with T_S(phi o g_t) = e^{Pt} T_S(phi).
New this round (round-5 results; ledger numbers in the round-6 block, entries 40 onward):
- S21 (round5_q6, no GH): (N) if lambda* > 0 there is a nonzero u in D' with Xu = kappa u, kappa real != 0. Case A (some mu(d) != 0): tilted conformal measure (order 0). Case B (all mu(d) = 0): from a pair x != y exponentially asymptotic in backward time (Pesin-Ruelle, cited), T_kappa(phi) = int_R e^{-kappa t}[e^{J_t(x)} phi(g_t x) - e^{b+J_t(y)} phi(g_t y)] dt is a holomorphic family of order-1 densities with T(P phi) = kappa T(phi), nonzero off a discrete set of kappa in (0, theta). Also Lemma 1 (lambda* > 0 gives an invariant measure with positive exponent; Kingman), Lemma 3 (all mu(d) = 0 => |J_t| <= eps|t| + C_eps uniformly).
- S22 (round5_q5 Thm 1, Cor 2, Cor 4; round5_q8 Cor 2, 3): under GH, no nonzero W in L^1 with XW = kappa W, Re kappa != 0; measure solutions are nu-singular; no nonzero finite-mass closed (n-1)-current C with C(L_X beta) = s C(beta), s real != 0. Also round5_q5 Lemma 0 (nu ergodic) and Lemma T (no Borel time function tau o g_t = tau + t).
- S23 (round5_q8 Thm 1): under GH, no Borel V with V o g_t = V - B_t a.e. when b is continuous with mu(b) != 0 for every invariant mu.
- S24 (round5_q1 Prop 1, round5_q2 §2, round5_q4 Prop 2.1, round5_q8 (C)): under GH (dim >= 2), (Lambda) [for X and -X] implies mu(d) = 0 for all mu, no zeros, no periodic orbits, all exponents of all mu zero, minimality. So (Lambda) is strictly stronger than the goal.
- S25 (round5_q7 Prop 4.0, Thm 4.1, Cor 4.2, 4.3; cited Ruelle, Katok/Lian-Young, hyperbolic theory): under GH, no orbit is heteroclinic from a volume-expanding to a volume-contracting hyperbolic periodic orbit; every hyperbolic ergodic mu of positive entropy produces (for X or -X) a non-attracting horseshoe Lambda != M that is uniformly volume-contracting (mu(d) <= -a < 0 on Lambda) with nu-null stable set; in dim 3, positive entropy forces this configuration (H3) and periodic orbits; GH + dim <= 3 + no periodic orbit (e.g. UE) => h_top = 0. Same picture in round5_q3 Prop H, round5_q10 Prop 5.1 (proper hyperbolic basic sets are uniformly volume-contracting or -expanding; cited Bowen-Ruelle) and Cor 5.3.
- S26 (round5_q10 Prop 5.2 sketch, round5_q3 Prop H(i)): Anosov flows are not GH (anisotropic Fredholm theory or Bowen-Ruelle SRB + Livsic, cited).
- S27 (round5_q9): Lemma T1 (orbitwise derivative = distributional derivative), Lemma H (one-sided compactness: approximate solutions a_n of Xa = -d + c with bounded positive parts either give (V) or their negative parts equidistribute to nu-hat), Theorem K ((V) <=> sup_t D((g_t)_* nu || nu) < inf <=> Cesaro means of this relative entropy bounded <=> Cesaro log-Jacobians L^1-bounded below on an open set), Theorem R (same with Patterson normalisers R_s), Lemma 4.2 ((Z0) => (Z0-lin): mu(d) = 0 for all mu), Lemma 4.4 (no hyperbolic attracting/repelling zeros or periodic orbits), Lemma 4.3 (badness invariant under time change).
- S28 (round5_q10 Lemma 4.1, Cor 4.2, Lemma 4.3): under GH bounded invariant Borel functions are nu-a.e. constant; the pointwise top exponent is nu-a.e. constant; orbits with two-sided nonpositive Jacobian growth are dense.
- S29 (round5_q1 Lemma 2/Cor 3; round5_q2 Prop 5.1): under GH, a smooth f whose forward correlations against smooth densities are improperly integrable is -Xu with u smooth; hence integrable decay of nu-correlations towards a measure m forces unique ergodicity and minimality.
- S30 (round5_q4): GH passes to smooth factors (Lemma 3.1); invariant submanifold carrying an invariant density with coboundary normal divergence refutes GH (Lemma 3.2); nilmanifold flows have lambda* = 0; on Gamma\Sol and compact Gamma\PSL(2,R), GH => lambda* = 0; products and skew products reduce to lower dimension; on S^1 GH => no zeros (also round5_q2, round5_q5).

## Dead ends (refuted statements only)
- #17 (round3_q3): "under H, x -> int_0^T f(g_t x) dt is Lipschitz uniformly in T" is false.
- Round-5 planner sketch step (c) (round5_q7 §2, round5_q3, round5_q5, round5_q8 (B1), round5_q10 §2): "a closed 1-current killing closed 1-forms equals dW for a generalized function W" is false for dim M >= 3 (it is the boundary of an (n-2)-form-valued current). The hypersurface repair gives zero limits whenever the hypersurface bounds (round5_q8 (B2), round5_q10 Lemma 3.2).

## Set aside, not refuted (open to re-attack)
- (Lambda) [#39]: not refuted, but shown strictly stronger than the goal (S24); it contains "GH => no zeros / no periodic orbits / minimality", which no round could reach. With (N) proved (S21), (Lambda) follows from (E1) [#38]; (E1) is proved for L^1 eigenfunctions (S22) but its singular part contains "mu(d) = 0 for all mu" and "no zeros".
- The (V) line: (V) [#19] then #16 (non-hyperbolic core) then goal. 14 queries on (V) produced only equivalent reformulations (S13-S17, S27). Sharpest open forms: (Z0) (exclude a half-orbit with J bounded above and e^J of Cesaro density 0), (Z0-lin) (mu(d) = 0 for every invariant mu), and the open-set forms of Theorems K and R.
- #16 non-hyperbolic core under GH + volume: open; all routes (spectral, tame estimate, conformal measures on SM) stop.
- Naive tame-estimate vs derivative growth (loses derivatives; round5_q8 4, round5_q7 5(c)).
- Spectral route (M) (#10).
- One-point discrepancy / return times (round3_q3).
- Local constructions at saddles (round3_q3, round4_q3, round5_q2 §3, round5_q9 Lemma 4.4 remark): global stable manifolds obstruct.
- Smearing conformal weights over smooth families of initial points (round5_q7 Lemma 5.1): Jacobians cancel exactly; gives smooth u or infinite u.
- Krein-Rutman eigenmeasures on SM (round5_q1 §3, round5_q7 §3, round5_q10 6(d)): exist, sit exactly on the growth borderline kappa = lambda*, order 1; v -> -v symmetry may kill them.

## Diagnostics
- Closed range/tame estimates alone cannot give zero entropy (Anosov flows have closed range of X on ann(I)).
- GH acts through: (a) L1 (P-harmonic densities are multiples of nu; nu ergodic and conservative; no measurable time functions or nu-measurable cocycles with nonzero means), (b) the tame estimate (always loses derivatives against growth). Everything that singles out positive entropy (horseshoes, Pesin manifolds, eigenmeasures) lives on nu-null sets or is singular; the problem is to make GH see it.
- Classical facts usable in any chain: flows on manifolds of dim <= 2 have zero topological entropy (Young 1977); h_top(f) <= n log^+ Lip(f); variational principle; Ruelle's inequality; Przytycki's inequality h_top(f) <= limsup (1/n) log int ||Lambda Df^n|| dvol and Kozlovski's equality for C^inf maps (cited); Ledrappier-Young (h_mu > 0 => non-atomic conditionals on unstable manifolds).

## The chain and the missing statement

(No complete written proof or refutation of the [GOAL] claim is in hand: no round-5 file proves (Lambda), (E1) in full, or zero entropy.)

**Decision this round.** Round 5 showed (S24) that the old missing statement (Lambda) [#39] is strictly stronger than the goal: under GH it forces "no zeros, no periodic orbits, mu(d) = 0 for all mu, minimality", none of which the goal needs (a hyperbolic saddle zero or a dissipative periodic orbit carries no entropy). Its only reduction, (N) [proved, S21] + (E1) [#38], is stronger still. So the missing statement is replaced by the weakest statement that completes the chain: the measure-theoretic form (PE) of the goal. Entry 39 is retracted as the missing statement (the claim itself stays set aside, not refuted).

**Chain.**
1. (Missing statement, PE) Under GH, every ergodic flow-invariant Borel probability mu has h_mu(g_1) = 0.
2. Classical (cited; round5_q2 Thm 4.1(a) writes out the reduction from g_1-invariant to flow-invariant measures): h_top(g_1) = sup h_mu(g_1) over g_1-invariant probabilities (variational principle); for g_1-invariant mu, mu-bar = int_0^1 (g_s)_* mu ds is flow-invariant and h_{mu-bar}(g_1) = h_mu(g_1) (g_s commutes with g_1; entropy is affine, Jacobs); by the ergodic decomposition of mu-bar for the flow and affinity again, h_mu(g_1) <= sup over ergodic flow-invariant mu' of h_{mu'}(g_1) = 0 by step 1. Hence h_top(g_1) = 0, which is the [GOAL].
Nothing else is needed.

**Missing statement (PE).** Let M be a compact connected smooth manifold and X a smooth vector field on M with flow g_t such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity, GH). Then every ergodic invariant Borel probability measure mu of the flow (g_t) has measure-theoretic entropy h_mu(g_1) = 0. (Equivalent forms, all usable: h_top(g_1) = 0; for C^inf flows, by Kozlovski's equality, lim_{t->inf} (1/t) log int_M ||Lambda Dg_t(x)|| dnu(x) = 0, where Lambda A is the full exterior power.)

**Why it should hold (planner sketch, at most fifteen lines).** Let mu be ergodic with h_mu > 0 and lambda = mu(d) (independent of nu). By Ruelle's inequality for g_1 and g_{-1}, mu has positive and negative exponents.
(a) Hyperbolic mu: S25 already turns mu into a non-attracting horseshoe Lambda != M, uniformly volume-contracting for X or -X. Step (DH) to be proved: GH excludes this. Candidate mechanisms: (Z0-lin) (mu(d) = 0 for all mu) kills it at once; or a global orbit argument with Lemma C (an orbit forward-asymptotic to Lambda, where J_t <= b - at, and backward-asymptotic to a set where J_t <= b' - a'|t|); or an open-system resolvent (anisotropic spaces near Lambda, Dyatlov-Guillarmou type) producing a non-smooth u with Xu smooth.
(b) General mu (also non-hyperbolic), candidate mechanism "generic pairs": by Ledrappier-Young, h_mu > 0 makes the conditionals of mu on Pesin unstable manifolds non-atomic, so mu-a.e. x has y != x in W^u_loc(x), y mu-generic in both directions, with d(g_{-t}x, g_{-t}y) <= C e^{-theta t} (theta close to the smallest positive exponent). Then, exactly as in round5_q6 Theorem B but with J_t(x), J_t(y) = lambda t + o(|t|) in place of the uniform bound, T_z(phi) = int_R e^{-zt}[e^{J_t(x)} phi(g_t x) - e^{b+J_t(y)} phi(g_t y)] dt is a holomorphic family on the strip lambda < Re z < lambda + theta with T_z(P phi) = z T_z(phi). If -theta < lambda < 0, z = 0 lies in the strip: T_0 is P-harmonic, so T_0 = c nu by L1; one must then show T_0 is not a multiple of nu (e.g. vary y along the non-atomic conditional measure, or use supp/orbit-closure information) to contradict GH. The case 0 < lambda < theta' is symmetric (stable pairs, -X). Remaining: |lambda| >= theta, and lambda = 0, where under H the cancellation is exact (T_0 = 0, round-6 planner check via the transfer function u: T_0(phi) = -(u(x)-u(y)) + (u(x)-u(y))). So the lambda = 0 case needs a second-order object: e.g. the derivative dT_z/dz at z = 0, or T_0 built from triples/families of pairs, or the volume-growth (Kozlovski) form averaged over nu.
I do not see how to close (b) at lambda = 0; it is the heart of the problem (it contains the old core #16).

**Tried so far** (on (PE), on the goal directly, and on the earlier wordings (Lambda) and "zero entropy under H"):
- round1_q1-q4: first reductions; L1, tame estimate, unstable-leaf transfer formula; hyperbolic case under H (Katok). Yield: S1-S5, reduction to #7/#16.
- round2_q2 (spectral, Lebesgue spectrum vs smooth observables): Prop S, missing (M); round2_q3, round3_q3 (bounded ergodic integrals, return times): obstructions.
- round3_q4: under GH + volume, hyperbolic case and dim <= 3 (S11); core #16 open.
- round4_q10: conformal measures on SM under GH + volume: Lemmas A-C, reduction to (E1) + (E2).
- round5_q1, q2, q3, q10 (identical closing task on Lambda): chain step 2 checked; Lambda strictly stronger than the goal (S24); Prop H / Prop 5.1 (horseshoes uniformly dissipative), Anosov not GH; correlation lemma (S29); sketch step (c) refuted.
- round5_q4 (refute Lambda): no counterexample; homogeneous, product, skew-product classes cleared (S30).
- round5_q5 (E1): E1 for L^1 eigenfunctions, closed (n-1)-currents (S22); singular case open.
- round5_q6 (N): proved without GH (S21).
- round5_q7 (Pesin/unstable constructions): dim-3 reduction to (H3), Jacobian-cancellation lemma (S25; Lemma 5.1 dead end).
- round5_q8 (quantitative tame estimate with test functions): measurable cocycle theorem (S23); every test family loses derivatives.
- round5_q9 ((V) via (Z0)): Lemma H, Theorems K, R, Lemma 4.4 (S27); (Z0) open.

## Where the next round should concentrate (round 6 wave)

Progress test: rounds 4-5 did produce progress on the chain in the sense of rule (iv): round5_q6 proved (N) for every smooth flow (a universal PROVED result that shortened the then chain Lambda <= E1 + N to Lambda <= E1). Round 5 also showed the then missing statement to be strictly stronger than the goal; this round therefore re-decomposes, taking the weaker (PE) as the missing statement, with the sketch above (hyperbolic part via dissipative horseshoes, general part via generic Ledrappier-Young pairs and L1 at z = 0).
Wave (escalation rule; PE posed for the first time):
- q1, q2, q3, q10: identical closing task on (PE), with the background and the round-5 tools spliced in full.
- q4: try to REFUTE (PE) exactly as stated (a GH flow with positive entropy), or else prove the structure any counterexample must have and push it to a contradiction.
- q5: hardest step of sketch (a) cut out: (DH) GH excludes a positive-entropy hyperbolic basic set (equivalently, by S25, a uniformly volume-contracting non-attracting horseshoe), named approaches: global heteroclinic/Lemma C argument, open-system resolvent.
- q6: sketch (b) as a named approach: generic Ledrappier-Young pairs, holomorphic eigen-family T_z, L1 at z = 0; settle the lambda = 0 case or show where it fails.
- q7: named approach: Przytycki/Kozlovski volume-growth form (nu-averaged) combined with the nu-measurable GH tools (S22, S23, S28, Lemma H).
- q8: named approach: one-sided compactness (Lemma H of round5_q9) and Jacobian-weighted (Patterson) constructions on Pesin unstable manifolds, aiming at a P-harmonic density that is not a multiple of nu.
- q9 (elsewhere, set-aside line that would settle sketch step (a)): (Z0-lin) under GH every invariant probability has mu(d) = 0.
Next round: if (PE) or the goal is proved, record PROVED [GOAL] and send two verify queries with the whole chain. If (DH) or (Z0-lin) is proved, the hyperbolic half is done; the missing statement then narrows to non-hyperbolic positive-entropy measures only if the chain shows the hyperbolic ones settled (S25 + that proof). If (PE) is refuted, the problem's claim is false as posed: verify the counterexample (two verify queries) before concluding.
