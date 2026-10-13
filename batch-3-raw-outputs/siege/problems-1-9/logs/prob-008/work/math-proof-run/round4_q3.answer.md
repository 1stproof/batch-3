# round4_q3: statement (V) (GH => smooth invariant positive density)

**Plan.** (1) Check the planner lemmas C–F one by one. (2) Prove new partial results. (3) Locate exactly where (V) gets stuck, and say what (V) secretly contains.

**Outcome in brief.** I did NOT prove (V), and I did NOT find a counterexample. A counterexample would be a GH vector field with no invariant volume. That would also disprove the Greenfield–Wallach conjecture (recalled from memory: GH vector fields are smoothly conjugate to Diophantine linear flows on tori, which preserve volume). So a counterexample is not realistic.

What this file establishes:
- (§1) Planner lemmas C, D, D1, D2, E and F are all correct. I checked every step and note small precisions. The heteroclinic part of C1 is only a sketch.
- (§2) A new Lemma G, which generalises Lemma D to ergodic measures with μ(d) ≠ 0. A new Lemma H, which gives a purely local proof that GH excludes hyperbolic sinks and sources.
- (§3) The obstruction, stated precisely. (V) implies "GH ⇒ X has no zeros", and in particular "no hyperbolic saddle zero p with d(p) ≠ 0". I show this saddle case is not a local question: the natural singular solution lives on the global stable manifold of p. So (V) contains a statement that none of the tools at hand can reach.

Conventions are those of the brief: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, and ⟨Xu, φν⟩ = −⟨u, (Xφ + dφ)ν⟩. The operator group P_tφ(x) = e^{J_t(x)} φ(g_t x) satisfies P_{s+t} = P_s P_t (by the cocycle identity) and has generator X + d.

## 1. Verification of the planner lemmas

**Observation 0: correct.** Take u = T/ν. Then ⟨Xu, φν⟩ = −T(Xφ + dφ). Under GH, L1 says that Xu = 0 forces T = Kν.

**Lemma C: correct.**
- At a zero, the integrand is e^{t d(x)}, which is not integrable on R.
- On a periodic orbit of period P, c(t+P) = e^{J_P(x)} c(t). This follows from J_{t+P}(x) = J_P(x) + J_t(g_P x) = J_P(x) + J_t(x). So ∫_R c dt = ∞ whatever the sign of J_P(x).
- On a non-periodic orbit: |J_t − J_s| ≤ ‖d‖_∞ |t−s|, so integrability of c forces c(t) → 0 as |t| → ∞. The function c is C^1, so ∫_R d/dt[c(t)φ(g_t x)] dt = 0, which gives T(Xφ + dφ) = 0. Then T = Kν with K = T(M)/ν(M) > 0. But T is carried by the orbit, and ν(orbit) = 0 because the orbit is a countable union of C^1 arcs and dim M ≥ 2. Contradiction.

**Corollary C1: correct in its first sentence**, which is immediate from Lemma C. The heteroclinic consequences are only sketched: they use exponential convergence along strong stable and strong unstable leaves. I did not re-check them and I do not use them.

**Lemma D: correct.**
- P(s) < ∞ for all s > 0 if and only if limsup J_t/|t| ≤ 0. One direction is clear. For the other, if J_{t_n} ≥ a|t_n| along a sequence, the Lipschitz bound puts mass ≳ e^{(a−s)|t_n|} near t_n.
- c_s is Lipschitz and tends to 0 at ±∞. So 0 = ∫ d/dt[c_s φ(g_t x)] dt = ∫ c_s[(Xφ + dφ) − s·sign(t)φ](g_t x) dt. This gives |T_s(Xφ + dφ)| ≤ s‖φ‖_∞.
- Every weak* limit point is a probability measure T with T((X+d)φ) = 0, so T = ν/ν(M) by Observation 0. The limit is unique, so the whole family converges.

**Corollary D1: correct.** For μ-a.e. x, Birkhoff's theorem in both time directions gives J_t(x)/t → μ(d) = 0. Choose such an x in supp μ. Each T_s is carried by the orbit closure of x, which lies in supp μ (closed and invariant). Hence ν/ν(M) is carried by supp μ, so supp μ = M.

**Observation D2: correct, with the stated signs.**
- ∫ e^{J_t} dν = ν(g_t M) = ν(M), because e^{J_t} is the ν-Jacobian. Jensen then gives ν̂(J_t) ≤ 0 for every real t.
- Forward averages: (1/T)∫_0^T ν̂(d∘g_t) dt = ν̂(J_T)/T ≤ 0, so μ_+(d) ≤ 0.
- Backward averages: (1/T)∫_{−T}^0 ν̂(d∘g_t) dt = −ν̂(J_{−T})/T ≥ 0, so μ_−(d) ≥ 0.

**Lemma E: correct.**
- (i) Under unique ergodicity, J_t/t → μ(d) uniformly as t → ±∞. If μ(d) ≠ 0, then ∫ e^{J_t} dν → 0 as t → +∞ (if μ(d) < 0) or as t → −∞ (if μ(d) > 0). This contradicts ∫ e^{J_t} dν = ν(M).
- (ii) D1 gives supp μ = M. Every orbit closure carries an invariant probability, which must be μ, so every orbit closure is M.
- (iii) I use the Gottschalk–Hedlund theorem for minimal flows, cited from memory: if g_t is minimal on a compact metric space, f is continuous, and sup_{t≥0} |∫_0^t f(g_s x_0) ds| < ∞ for some x_0, then ∫_0^t f(g_s x) ds = a(g_t x) − a(x) for a continuous a. Applied to f = d it gives J_t = a∘g_t − a.
  - Shortest finish: a is continuous, hence in L^1. The (N3) computation gives Xa = d in D', so a is smooth by GH. Then e^{−a}ν is invariant, because L_X(e^{−a}ν) = e^{−a}(−Xa + d)ν = 0.
  - Conversely, a smooth invariant ρν gives J_t = log ρ − log ρ∘g_t, which is bounded.

**Lemma F: correct.**
- (⇒) Xρ = −dρ gives P(ρw) = ρXw. So P = ρ X ρ^{−1}, and multiplication by ρ^{±1} preserves both C^∞ and D'.
- (⇐) Every invariant probability μ has the form ρν with ρ ≥ 0 smooth, by GH of P.
  - For ergodic μ, the set {ρ > 0} is open, invariant and nonempty, so it is conull by (N1), which uses GH of X. Two distinct ergodic measures would then both be equivalent to ν, yet they are mutually singular. So the flow is uniquely ergodic.
  - The set Z = {ρ = 0} is invariant, since ρ(g_t x) = ρ(x)e^{−J_t(x)}, and closed. If Z were nonempty it would carry μ, but μ(Z) = 0. So ρ > 0.

## 2. New partial results

### Lemma G (proved). Let X satisfy GH, and let μ be an ergodic invariant probability measure with μ(d) = λ. Then there is a probability measure T carried by supp μ such that T((X + d − λ)φ) = 0 for all smooth φ. Equivalently, T(P_tφ) = e^{λt} T(φ) for all t; equivalently, u = T/ν satisfies Xu = −λu. If λ = 0, then T = ν/ν(M).

*Proof.*
1. Take x ∈ supp μ with J_t(x)/t → λ as t → ±∞. This holds for μ-a.e. x, by Birkhoff applied to d in both time directions.
2. For s > 0 put c_s(t) = e^{J_t(x) − λt − s|t|}. Since J_t(x) − λt = o(|t|), the function c_s is integrable and tends to 0 at ±∞. Normalise: T_s(φ) = ∫ c_s φ(g_t x) dt / ∫ c_s.
3. Integrate d/dt[c_s φ(g_t x)] = c_s[(X + d − λ)φ − s·sign(t)φ](g_t x). This gives |T_s((X + d − λ)φ)| ≤ s‖φ‖_∞.
4. Take any weak* limit T as s → 0. It works, and it is carried by the orbit closure of x, which lies in supp μ.
5. Equivalence of the forms: the generator of the group P_t is X + d, and P_t commutes with it. So d/dt T(P_tφ) = T((X+d)P_tφ) = λ T(P_tφ). Also ⟨Xu, φν⟩ = −T((X+d)φ) = −λT(φ).
6. If λ = 0, Observation 0 and L1 give T = ν/ν(M). ∎

**Remark (why G does not close the gap).** Without GH, λ ≠ 0 eigen-measures are harmless. At a zero p, T = δ_p satisfies T((X+d)φ) = d(p)φ(p), so it is a λ = d(p) eigen-measure. GH excludes it only when d(p) = 0 (this is P1). So Lemma G produces real eigen-measures, but GH as such gives no contradiction for them. GH concerns only smooth right-hand sides, and the eigen-equation Xu = −λu has a non-smooth right-hand side. This is the same obstruction as dead ends 1–2 of round 3.

### Lemma H (proved; a local version of round 3's §2(b) for linearisable zeros). Let X be GH with dim M ≥ 2. Then X has no zero p near which X is C^∞-conjugate to a linear field Σ λ_i x_i ∂_i with all λ_i > 0, or with all λ_i < 0. By Sternberg's theorem (cited) this covers every non-resonant hyperbolic source or sink.

*Proof.* Take all λ_i > 0; for all λ_i < 0 replace X by −X, using (O4).
1. Work in linear coordinates on the ball B = {Q < r^2}, where Q(x) = Σ_i x_i^2 and Λ = diag(λ_i) with all λ_i > 0. Along the linear flow e^{tΛ}, the function t ↦ Q(e^{tΛ}y) is strictly increasing for y ≠ 0, because d/dt Q = 2Σ λ_i x_i^2 > 0. Each nonzero orbit tends to p as t → −∞ and leaves every compact subset of R^n as t → +∞.
   - Hence the sphere S = {Q = r^2/4} is smooth and transversal to X.
   - Each orbit in B∖{p} meets S exactly once, at a time −τ(x). The function τ is smooth on B∖{p} by the implicit function theorem, using transversality.
   - Put π(x) = e^{−τ(x)Λ}x ∈ S. The map π is smooth on B∖{p} and constant along orbits, so X(h∘π) = 0 on B∖{p} for every smooth h on S.
2. Let h be a smooth non-constant function on S, and put u_0 = h∘π on B∖{p}. Then u_0 is bounded, so it defines a distribution on B, and it has no continuous extension to p, because every orbit tends to p as t → −∞. Also Xu_0 = 0 in D'(B): the point p has capacity zero for a first-order operator acting on L^∞ functions. Concretely, for test φ,
   ∫ u_0 L_X(φν) = lim_{ε→0} ∫_{Q>ε^2} u_0 L_X(φν). Here the integral over {Q < ε^2} → 0, since the integrand is bounded.
   On {Q > ε^2} we have u_0 L_X(φν) = L_X(u_0 φν) − (Xu_0)φν = L_X(u_0φν) = d(ι_X(u_0φν)), by Cartan's formula for a top-degree density (use an orientation on the ball). By Stokes, this equals −∫_{Q=ε^2} u_0 φ ι_Xν. That term is O(‖u_0‖_∞‖φ‖_∞ · ε · ε^{n−1}) → 0, since |X| = O(ε) there.
   So ⟨Xu_0, φν⟩ = 0 for all test φ supported in B.
3. Let χ ∈ C_c^∞(B) with χ = 1 near p. Then u = χu_0 ∈ L^∞(M) and Xu = (Xχ)u_0. This is smooth, because Xχ is supported where u_0 is smooth, away from p. But u is not continuous at p. This contradicts GH. ∎

(Round 3's §2(b) already excluded Lyapunov-stable attractors and repellers by a measure-theoretic argument. Lemma H is a local, distributional argument of a different nature. It is listed because it shows exactly where the saddle case fails; see §3.)

## 3. Where (V) is stuck, stated exactly

**(V) implies "no zeros".** By Lemma A, (V) gives dim I = 1. A zero p gives δ_p ∈ I, while the smooth invariant volume ω is also in I and is not a multiple of δ_p. So proving (V) requires in particular proving:

> **(Z)** a GH vector field (dim M ≥ 2) has no hyperbolic saddle zero p with d(p) ≠ 0.

Round 3 and this round exclude only d(p) = 0 (P1), and sinks and sources ((b) and Lemma H).

**Why (Z) is not local.** Take a linear saddle in R^2, X = a x∂_x − b y∂_y with a, b > 0, so d(0) = a − b.
- The only local candidates for Xu = 0 that are singular at 0 are carried by the invariant axes. For example u = δ(x) ⊗ |y|^{−a/b}: a computation gives Xu = −δ(x)(a v + b y v') with v = |y|^{−a/b}, and this vanishes. The function v is locally integrable iff a < b, i.e. iff d(p) < 0. For d(p) > 0, use the unstable axis and −X.
- So a singular local solution exists exactly when the sign of d(p) allows it. But any cut-off χu has X(χu) = (Xχ)u, which is singular on W^s(p) ∩ supp(Xχ).
- Hence the solution must be continued along the whole global stable manifold W^s(p), with the conformal density e^{J_t} along each branch orbit. That density is integrable at the p-end exactly when d(p) < 0. At the far end, integrability requires J_t(x) → −∞ fast as t → −∞ along the branch orbit x, which is the hypothesis of Lemma C.
- Whether that happens depends on the global recurrence of the branch, which is uncontrolled. When it does happen, Lemma C gives the contradiction. When it does not, I have no argument.

So (Z), and with it (V), comes down to the same global problem as in the sketch: building from non-integrable conformal weights a finite measure T ≠ cν with T((X+d)φ) = 0.

**Why the functional-analytic route fails.**
- From Text A/B, X: C^∞_0 → X(C^∞) is an isomorphism, and its transpose X + d: D' → D' has range equal to the ν-mean-zero distributions and kernel I/ν.
- Both are consistent with any dim I ≥ 1: there is no index or homotopy argument, since nothing is Fredholm.
- The estimates can only bound solutions from above, while (V) needs to rule out extra invariant distributions. The microlocal route is circular (round3_q2).

**Remark on the chain.**
- Even with (V), the main line still needs the Missing Lemma of [R3-q4] when dim M ≥ 4. Since (V) ⇒ (Z), (V) is at least as hard as excluding saddle zeros, which is open here.
- The chain's steps 2 and 3, given (V), look correct to me: Lemma A, (O2), the variational principle, Ruelle–Pesin, and Katok's horseshoe theorem for C^{1+α} flows, all cited from memory.

## Summary
- **Proved:**
  - verification of planner lemmas C (apart from the sketched part of C1), D, D1, D2, E and F;
  - Lemma G (eigen-conformal measures for ergodic μ with μ(d) = λ);
  - Lemma H (no linearisable sources or sinks, by a local distributional argument);
  - (V) ⇒ (Z), and (Z) is non-local.
- **Reduction, from Lemmas E and F:** (V) ⇔ [unique ergodicity + J_t bounded along one orbit] ⇔ GH of X + d.
- **Open:**
  - (V) itself;
  - unique ergodicity under GH;
  - (Z), the absence of saddle zeros with d(p) ≠ 0;
  - the absence of dissipative saddle periodic orbits;
  - the Missing Lemma of [R3-q4] (not attempted).

=== END OF ANSWER round4_q3 ===
