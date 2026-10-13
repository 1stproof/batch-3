# Running summary after round 5 planning (rounds 1-4 folded in)

## Problem and conventions
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No complete proof exists.

Conventions: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds = log nu-Jacobian of g_t; I = space of X-invariant distribution densities; (V) = "X preserves a smooth positive density" (entry 19); H = smooth invariant volume omega + unique ergodicity + every omega-mean-zero smooth f is Xu with u smooth (tame estimates). P = X + d acting on functions (= L_X on densities, minus the transpose of X).

Process note: in round 4 the query files q6-q9 carried a foreign paragraph ("missing statement (M)" about L-space knots) spliced by mistake from an unrelated file; all workers recognised and ignored it. Splice only from files in this run directory, and grep the query files for foreign text before finishing.

## Standing results (never dropped; ledger numbers)
- S1 (#2, round1_q2): ker X on D' = constants (L1).
- S2 (#3, round1_q2 / round1_q1): tame estimate ||u - mean||_{C^k} <= C||Xu||_{C^m}; X(C^inf) closed = annihilator of I; X: C^inf_0 -> X(C^inf) isomorphism.
- S3 (#4, round1_q2; round2_q4): no periodic orbit with Poincare Jacobian 1.
- S4 (#8, round2_q1): at a zero p, d(p) != 0. Strengthened (#33, round4_q5 Lemma H): tr DX(p) + sum alpha_i lambda_i != 0 for every multi-index alpha (jet non-resonance). round4_q3 Lemma H: no zero C^inf-linearisable to an all-positive or all-negative linear field (local distributional proof).
- S5 (#5, round1_q3): under H, unstable-leaf formula for the transfer function. Not on the current line.
- S6 (#9, round2_q3): under H, bounded ergodic integrals, spectral estimate sigma_f([-e,e]) <= C e^2. Not on the current line.
- S7 (#11, round3_q1): N1 invariant Borel sets null or conull; N2 conservative (dim >= 2); N3 L^1 solutions of the cohomological equation with smooth RHS are smooth (log-integrable a.c. invariant density gives (V)); N4 reformulations of (V).
- S8 (#12, round3_q1): a.c. invariant probability with rho^{-eps} in L^1 gives (V). Strengthened by #28.
- S9 (#13, round3_q1): no Lyapunov-stable attracting/repelling zero or periodic orbit with open basin (dim >= 2). Strengthened by #32.
- S10 (#14, round3_q2): (V) <=> dim I = 1; (V) => H, unique ergodicity, no zeros, no periodic orbits.
- S11 (#15, round3_q4): under GH + (V): h_top = h_omega, = 0 when omega has no zero transverse exponent (Pesin, Katok cited); full solution of the special case GH + (V) + dim M <= 3. Not on the current line (the V line is set aside, see below).
- S12 (#18, round3_q3): under H, orbit segments of length >= C eps^{-m-n} are eps-dense. Not on the current line.
- S13 (#24-#26, planner Lemmas C-F verified by round4_q1-q9): Lemma C every x has int_R e^{J_t(x)} dt = inf (dim >= 2); Lemma D Jacobian-weighted (Patterson) orbit averages with subexponential J converge to nu-hat, so ergodic mu with mu(d) = 0 has full support; Lemma E under unique ergodicity mu(d) = 0 and minimality; Lemma F (V) <=> P = X + d is GH. Observation D2: forward Cesaro limits mu_+ of transported volume have mu_+(d) <= 0, backward mu_- >= 0.
- S14 (#27, round4_q6 Prop 1; also round4_q1 Prop 2.4, round4_q9 Thm 3): under GH, (V) <=> some x has sup_{t>=0}|J_t(x)| < inf; more generally sup_{t>=0} J_t(x) < inf plus positive upper Cesaro mean of e^{J_t(x)} gives (V). round4_q6 Principle G: Jacobian-weighted orbit segments with small endpoint weights equidistribute to nu-hat; Lemma 3 (no GH): some half-orbit of X or -X has J bounded above; Corollary 4: if (V) fails, along every such half-orbit e^{J} has Cesaro density 0.
- S15 (#28, round4_q9 Thm 1, Cor 1'): an a.c. invariant probability with density >= delta on a nonempty open set, or a nonzero continuous signed invariant density, gives (V).
- S16 (#29, round4_q7 Thm 3.2; round4_q2 Prop G; round4_q5 Prop C; round4_q9 Cor 2): (V) <=> P(C^inf) closed <=> X(D') weak*-closed <=> C^inf subset X(D') + R. Also round4_q5 Lemma A: X + d on D' has range = nu-mean-zero distributions (dual of S2).
- S17 (#30, round4_q1 Thm 2.3, Lemma 2.1/2.2): (V) <=> bounded Cesaro means of entropy production F(t) = KL(nu-hat || (g_{-t})_* nu-hat); (V) <=> sup_{t,x}|J_t| < inf; Cesaro averages of S_t f bounded in D' give f in R + X(C^inf).
- S18 (#31, round4_q4 B1): (V) <=> S(div_nu X) = 0 for every S in I (Phi(S) = S(d) independent of nu).
- S19 (#32, round4_q4 B3-B4; round4_q2 Prop H): no proper closed invariant set has a basin (forward or backward) of positive volume; Hopf: int_0^{+-inf} e^{J_t(x)} dt = inf for nu-a.e. x; ergodic mu with mu(d) != 0 has nu-null basin.
- S20 (#34, round4_q7 Prop 2.2, round4_q3 Lemma G; no GH): every ergodic mu with mu(d) = lambda carries a "tilted conformal" probability T with T(X phi + d phi) = lambda T(phi). round4_q7 Prop 2.1: there are ergodic mu_+, mu_- with mu_+(d) >= 0 >= mu_-(d).
- S21 (#35, round4_q7 Lemma 3.1; round4_q2 Prop G): smooth signed invariant densities have constant sign and span dimension <= 1.
- S22 (#36, round4_q10 Lemma B): GH extends to closed 1-currents (closed alpha with L_X alpha smooth is smooth).
- S23 (#37, round4_q10 Lemmas A, C; under GH + smooth invariant volume): measurable invariant L^1 vector fields are divergence-free; Schauder fixed point gives a probability S on the unit sphere bundle SM with int e^{A_t} Psi o g^_t dS = e^{Pt} int Psi dS (A_t = log|Dg_t v|), and T_S(phi) = int dphi(v) dS(v) satisfies L_X T_S = -P T_S; T_S = 0 when P = 0.

## Dead ends (refuted statements only)
- #17 (round3_q3): "under H, x -> int_0^T f(g_t x) dt is Lipschitz uniformly in T" is false as a tool (only Lip <= Lip(u)(1 + Lip g_T)); the "direction (i)" route built on it is dead.

## Set aside, not refuted (open to re-attack)
- The (V) line: (V) [#19] then #16 (non-hyperbolic core) then goal. Attacked in rounds 1-4 (13 queries on (V)); produced only equivalent reformulations (S13-S21). Every reformulation stops at the same point: GH controls the conformal/X side (solutions of X(.) = smooth, Jacobian-weighted averages), while (V) concerns the transposed operator P = X + d (unweighted averages, invariant measures). Open precise forms: exclude a half-orbit with J bounded above and e^J of Cesaro density 0 (round4_q6); P(C^inf) closed; unique ergodicity under GH. Literature recollection by several workers (unverified): Forni 2008 / Kocsard 2009 on Greenfield-Wallach and Katok conjectures; a counterexample to (V) would refute the Greenfield-Wallach conjecture.
- #16 non-hyperbolic core (under GH + volume, no positive exponent with a zero transverse exponent): round4_q10 reduced its natural route to (E1) "no real eigen-distributions" + (E2) "positive exponent gives a conformal S with T_S != 0" (symmetry v -> -v can kill T_S).
- Naive tame estimate vs derivative growth (loses derivatives).
- Spectral route (M) (#10, round2_q2): smooth observables vs Lebesgue spectrum.
- One-point discrepancy / return times (round3_q3): compatible with positive entropy.
- Local constructions at hyperbolic periodic orbits/saddles (round3_q3, round4_q3): singular along global stable manifolds; (Z) "no saddle zeros with d(p) != 0" is non-local.
- Nonsingular ergodic theory, microlocal propagation, martingale constructions, Patterson weights with running maxima, analytic family X + z d, pressure q(s), asymptotic cycles (rounds 3-4): each reaches only a reformulation.

## Diagnostics
- D1: closed range / tame estimates alone cannot give zero entropy (Anosov flows have closed range of X on the annihilator of I).
- Under H, GH <=> ker_{D'} X = constants.
- UE alone insufficient (minimal UE positive-entropy systems exist).
- The recurring obstruction: GH speaks only about X with smooth right-hand side; invariant measures, eigen-distributions (Xw = lambda w) and Lyapunov objects satisfy equations whose right-hand side is not smooth. Any proof must find a way to manufacture, from dynamics, a non-smooth u with Xu smooth.
- Classical facts usable in any chain: flows on manifolds of dimension <= 2 have zero topological entropy (Young 1977); h_top(f) <= n log^+ Lip(f) for a Lipschitz map of a compact n-manifold; variational principle; Ruelle's inequality.

## The chain and the missing statement

(No complete written proof or refutation of the [GOAL] claim is in hand: no round-4 file proves (V), #16, or the goal.)

**Chain.** (New decomposition this round; it bypasses both (V) [#19] and the non-hyperbolic core [#16]. Ledger: missing statement = entry 39, (E1) = entry 38.)
1. (Missing statement, Lambda) Under GH, lambda* := lim_{t->+inf} (1/t) log max_{x in M} ||Dg_t(x)|| = 0.
2. Classical (cited, no GH): for a Lipschitz self-map f of a compact n-dimensional Riemannian manifold, h_top(f) <= n max(0, log Lip f); and h_top(g_T) = T h_top(g_1) for T > 0. Hence h_top(g_1) = h_top(g_T)/T <= (n/T) log^+ max_x ||Dg_T(x)||, which tends to n max(0, lambda*) = 0 as T -> inf by step 1. The topological entropy of the flow is h_top(g_1), so it is 0. (dim M = 1 is trivial anyway.)
Nothing else is needed: a reader holding a proof of Lambda holds a complete proof of the goal.

**Missing statement (Lambda).** Let M be a compact connected smooth manifold, fix any Riemannian metric on M, and let X be a smooth vector field on M with flow g_t, such that every distribution u in D'(M) with Xu in C^inf(M) lies in C^inf(M) (global hypoellipticity). Then lim_{t->+inf} (1/t) log max_{x in M} ||Dg_t(x)|| = 0 (the limit exists by subadditivity and is >= 0); equivalently, no invariant Borel probability measure of the flow has a positive Lyapunov exponent; equivalently, for every eps > 0 there is C with ||Dg_t(x)|| <= C e^{eps t} for all x in M and t >= 0.

**Why it should hold (planner sketch).** Under the Greenfield-Wallach picture GH flows are Diophantine linear flows, whose derivatives are bounded; so Lambda is expected. Candidate mechanism (curve currents -> eigen-distribution):
(a) If lambda* > 0, some ergodic mu has a positive exponent; a C^{1+alpha} arc gamma inside a Pesin local unstable manifold has length L(t) = length(g_t gamma) >= c e^{(lambda - eps)t}. Let s0 > 0 be the critical exponent of Z(s) = int_0^inf e^{-st} L(t) dt (Patterson's slowly-varying weight makes Z diverge at s0 if needed).
(b) The normalised 1-currents C^s(beta) = Z(s)^{-1} int_0^inf e^{-st} (int_{g_t gamma} beta) dt have mass <= 1; by Stokes, |C^s(df)| <= 2||f||_inf /(s Z(s)) -> 0, and C^s(L_X beta) = s C^s(beta) - Z(s)^{-1} int_gamma beta. A weak* limit C as s -> s0 is a CLOSED 1-current with C(L_X beta) = s0 C(beta).
(c) For closed beta, L_X beta = d(i_X beta), so s0 C(beta) = C(d i_X beta) = 0: C kills closed forms, hence (de Rham for currents) C = dW for a generalized function W; the eigen-relation gives d(XW - kappa W) = 0 with kappa = +-s0, so after adding a constant XW = kappa W, and W is non-constant iff C != 0.
(d) (E1, entry 38) GH should exclude nonzero W in D' with XW = kappa W, kappa real != 0 (true for Diophantine linear flows by Fourier series). Caution found while composing round 5: order-0 solutions exist whenever some ergodic mu has mu(d) != 0 (tilted conformal measures, #34, give W = T/nu with XW = -mu(d) W), so (E1) contains 'every invariant probability has mu(div X) = 0', in particular 'no zeros'. In the d-free form (E1') T(X phi) = kappa T(phi) (the form of T_S), order-k T with |kappa| > k times the growth rate of Dg_t are killed by the resolvent; danger there is high order. Consequently (N) is automatic when some mu(d) != 0; its content is the case all mu(d) = 0.
Two hard points: (N) C may vanish by cancellation of orientations (choose gamma / weights so that it does not, e.g. orient along a measurable unstable orientation, or pass to a double cover / the unit tangent bundle); (E1) itself, which is a statement about X - kappa, i.e. a "transposed"-type statement again (GH of X versus kernel of X - kappa). An alternative to (a)-(c): the Krein-Rutman eigenmeasure S on SM for the positive operator Psi -> |Dg_t v| Psi(g^_t v) with eigenvalue e^{lambda* t} (spectral radius), giving T_S(phi) = int dphi dS with T_S(phi o g_t) = e^{lambda* t} T_S(phi) (round4_q10 Lemma C did this without the top eigenvalue, under a volume).

**Tried so far** (Lambda is newly posed; listed are the queries on earlier, narrower forms — zero exponents / zero entropy under GH plus a smooth volume — which count as tried approaches):
- round1_q3, round3_q4: under H, Pesin + Katok horseshoes: settles the hyperbolic case (#15); reduces the rest to #16.
- round2_q2: spectral route (Lebesgue spectrum vs smooth observables) -> Proposition S, missing lemma (M).
- round2_q3, round3_q3: tame estimate / bounded ergodic integrals / return times -> obstructions (F2 refuted, subshift counterexample to the return-time route).
- round4_q10: conformal measures on the unit tangent bundle under GH + volume -> Lemmas A-C (#36, #37) and the reduction to (E1) + (E2: some conformal S has T_S != 0).

## Where the next round should concentrate (round 5 wave)

Progress test: rounds 3 and 4 produced no progress on the chain in the strict sense — main line stalled — no universal progress (round 4 gave only equivalent reformulations of (V) and verified lemmas). What differs now: a different decomposition with a different missing statement — Lambda (subexponential derivative growth), which completes the goal by itself via the classical bound h_top <= n log^+ Lip, bypassing both (V) and #16 — with a new mechanism (closed eigen-currents from expanding curves, de Rham to an eigen-distribution, exclusion by GH).
Wave (escalation rule; Lambda is posed for the first time):
- q1, q2, q3 (and q10): identical closing task on Lambda.
- q4: refute Lambda exactly as stated (GH field with exponential derivative growth, or derive from Lambda something false).
- q5: the hardest step of the sketch cut out: (E1) GH excludes real eigen-distributions XW = kappa W, kappa != 0.
- q6: the other hard step cut out: (N) a positive exponent (lambda* > 0) yields a NONZERO distribution W with XW = kappa W for some real kappa != 0 (or directly a non-smooth u with Xu smooth).
- q7: named approach: Pesin theory / unstable conditional measures used to manufacture a non-smooth distributional solution of Xu = f with f smooth, directly from a positive exponent.
- q8: named approach: quantitative use of the tame estimate on test functions adapted to an exponentially expanding curve/disk (Yomdin-type volume growth), aiming at a contradiction with lambda* > 0.
- q9 (the one "elsewhere" query): the set-aside (V) line at its sharpest open form (round4_q6: exclude a half-orbit with J bounded above and e^J of Cesaro density 0), with round4_q6 and round4_q9 spliced.
Next round: if Lambda is proved, record PROVED [GOAL] citing it and the classical bound, and send two verify queries. If E1 or N is proved, record and feed it into the closing task. If Lambda is refuted (a GH field with positive exponent), the goal line must switch to a pure-entropy route (exponents may be positive yet entropy zero).
