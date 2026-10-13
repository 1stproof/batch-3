# Answer to round5_q3: statement (Lambda)

## Summary of the outcome
I have **not** proved (Lambda), and I have **not** proved zero entropy in general. I have no counterexample either. What this file contains:

- §1: a check of step 2 of the chain (it is correct), plus two corrections to the planner's sketch. The main correction: sketch step (c) is wrong for dim M ≥ 3.
- §2: Proposition H (proved, modulo cited classical hyperbolic theory). Under GH a vector field is never Anosov. Every hyperbolic basic set Λ is uniformly volume-expanding or uniformly volume-contracting: there is c > 0 with μ(d) ≥ c for all invariant μ on Λ, or μ(d) ≤ −c for all of them.
- §3: Proposition V3 (proved, modulo Katok's closing lemma). Under GH together with (V), the measure ω is not hyperbolic. In dimension 3 this gives (Lambda), and hence zero entropy.
- §4: the exact point where the argument stops.

Notation: ν is a smooth positive density, d = div_ν X, and J_t(x) = ∫_0^t d(g_s x) ds. L1, P, C, C1, D, D1, Prop 2.1, B3 and O2 are as in the task file.

## 1. Checks of the chain and of the sketch

**Step 2 is correct.** For a Lipschitz map f of a compact n-dimensional Riemannian manifold, h_top(f) ≤ n·max(0, log Lip f). This is classical (Kushnirenko/Ito; cited from memory). Also h_top(g_T) = T·h_top(g_1) for T > 0 (Abramov-type, for topological entropy). With Lip(g_T) = max‖Dg_T‖ this gives h_top(g_1) ≤ (n/T) log^+ max‖Dg_T‖ → n·max(0, λ*). So (Lambda) implies the problem. (Lambda) is strictly stronger than zero entropy, because zero entropy alone allows λ* > 0. It is the natural target nonetheless, since under the expected Greenfield–Wallach picture λ* = 0.

**Correction 1: sketch step (c) is wrong for n ≥ 3.** The limit object C in step (b) acts on 1-forms, so it is a current of *dimension 1*, i.e. of degree n−1.

- If C(β) = 0 for every closed 1-form β, then C is closed (C(dψ) = 0), and its homology class vanishes by de Rham duality.
- Hence C = ∂R for a current R of dimension 2 (degree n−2).
- R is a generalized *function* only when n = 2.
- For n ≥ 3 the route therefore yields at best a dimension-2 eigen-current with L_X R − κR closed. It does not yield an eigen-distribution W with XW = κW.
- Getting from R to a function W would require solving (L_X − κ)Q' = Q inside closed currents. That needs surjectivity of X − κ on D', which is not available.

**Correction 2: the normalisation must use the mass norm.** In every negative Sobolev norm the 1-form currents g_t^*β, with β closed, grow at most linearly in t:

- g_t^*β = β + d(∫_0^t (i_Xβ)∘g_r dr), and the function inside the d is bounded by t‖i_Xβ‖_∞.
- Likewise R_sψ = ∫_0^∞ e^{−st} ψ∘g_t dt is bounded by ‖ψ‖_∞/s.

So the distributional critical exponent is always 0. A critical exponent s0 > 0 appears only for the *mass* (order-0) normalisation. The limit current is then of order 0, and it can vanish by cancellation (the problem labelled (N) in the sketch).

**Correction 3: the Krein–Rutman alternative.** The object T_S(φ) = ∫ dφ(v) dS(v) satisfies T_S(Xφ) = λ*·T_S(φ). This is the *transposed* eigen-equation for a density-type distribution. GH controls X acting on function-type distributions, and passing from one to the other (u = T/ν) introduces the term d·u. Without (V) this route therefore lands again on the hard point (E1).

## 2. Proposition H (proved; uses cited classical hyperbolic theory)

**Proposition H.** Assume GH and dim M ≥ 2.
(i) X is not an Anosov vector field.
(ii) Let Λ be a hyperbolic basic set of the flow, i.e. compact, invariant, locally maximal, transitive and hyperbolic, and not a single orbit. Then there is c > 0 such that either μ(d) ≥ c for every invariant probability μ supported on Λ, or μ(d) ≤ −c for all of them.

Classical facts cited from memory:
- (K1) Periodic orbits in a basic set are hyperbolic, and any two of them γ1, γ2 are heteroclinically related: W^u(γ1) ∩ W^s(γ2) ≠ ∅. This follows from transitivity and local product structure.
- (K2) Sigmund: on a basic set of a flow, the measures carried by periodic orbits are weak*-dense among the invariant probabilities.
- (K3) For a hyperbolic periodic orbit γ, each x ∈ W^s(γ) has an asymptotic phase y ∈ γ with dist(g_t x, g_t y) ≤ C e^{−βt} for t ≥ 0, and symmetrically for W^u. Here β > 0.
- (K4) Spectral decomposition for Anosov flows. If the non-wandering set Ω ≠ M, there is an attracting basic set whose basin is open; it is nonempty, so it has positive volume.
- (K5) Bowen–Ruelle: a C^2 transitive Anosov flow has an SRB measure μ^+, and μ^+(d) ≤ 0. If μ^+(d) = 0, then μ^+ is absolutely continuous, and by Livšic regularity the flow preserves a smooth positive volume.

**Step 1 (the heteroclinic part of C1, now proved).** Let γ1, γ2 be hyperbolic periodic orbits with periods P1, P2 and a1 = (1/P1)∫_{γ1} d > 0 > a2 = (1/P2)∫_{γ2} d. Then no x lies in W^u(γ1) ∩ W^s(γ2).

*Proof.* Take the asymptotic phase y2 ∈ γ2 from (K3). Then
|J_t(x) − J_t(y2)| ≤ Lip(d)·C/β for t ≥ 0.
Also J_t(y2) = a2·t + O(1). So J_t(x) ≤ b + a2·t for t ≥ 0.

Symmetrically, for t ≤ 0 we have J_t(x) = −∫_t^0 d(g_s x) ds ≤ b − a1|t|.

Hence ∫_R e^{J_t(x)} dt < ∞. The orbit of x is not periodic and not a zero, since it is asymptotic to two different orbits, or to γ1 in both directions with incompatible rates. This contradicts Lemma C. ∎

**Step 2 (proof of (ii)).**
- By P, every periodic orbit γ ⊂ Λ has ∫_γ d ≠ 0.
- By Step 1 and (K1), all of these integrals have the same sign. Say they are all > 0; otherwise replace X by −X, which keeps GH by (O4) and changes d to −d.
- By (K2), every invariant μ on Λ has μ(d) ≥ 0.
- Let a = min μ(d) over invariant μ on Λ. The minimisers form a closed face of the simplex, so a is attained at an ergodic μ0.
- If a = 0, Corollary D1 gives supp μ0 = M, hence Λ = M and the flow is Anosov. This is excluded by (i), proved in Step 3 independently of (ii).
- So c := a > 0. ∎

**Step 3 (proof of (i)).** Suppose X is Anosov.
- If Ω ≠ M, the attractor from (K4) is a proper closed invariant set whose basin has positive volume. This contradicts B3. So Ω = M.
- The basic sets of Ω are open and closed in Ω = M, and M is connected, so the flow is transitive.
- Steps 1–2 apply to Λ = M. Up to replacing X by −X, every periodic orbit has ∫_γ d > 0, and every invariant μ has μ(d) ≥ 0.
- By (K5), μ^+(d) ≤ 0, so μ^+(d) = 0, and X preserves a smooth positive volume.
- By (O2) the flow then has no periodic orbits. An Anosov flow has periodic orbits, which is a contradiction. ∎

*Remark.* Proposition H says that in a GH flow every horseshoe is uniformly dissipative, with one sign of volume change throughout. All earlier GH consequences (Lemmas C and D, B3, B4) are consistent with uniformly dissipative horseshoes. I could not exclude them, and this is exactly where a positive-entropy GH flow in dimension 3 would have to live. By Katok/Lima–Sarig, such a flow has horseshoes approximating any hyperbolic positive-entropy measure.

## 3. Proposition V3: zero entropy under (V) in dimension 3 (proved, citing Katok)

**Proposition V3.** Assume GH, dim M ≥ 2, and (V): X preserves a smooth positive density ω. Then ω is not a hyperbolic measure, meaning ω has some zero Lyapunov exponent transverse to X. If dim M = 3, then λ* = 0, so (Lambda) holds and h_top = 0.

*Proof.*
- By (O2) the flow is uniquely ergodic with measure ω, and it has no zeros and no periodic orbits.
- Cited (Katok's closing lemma for C^{1+α} flows): if an ergodic measure, not carried by a single orbit, has all exponents nonzero except the flow direction, then periodic orbits accumulate on its support. So ω cannot be hyperbolic.
- In dimension 3 the exponents of ω are 0 (flow direction; |Dg_t X| = |X∘g_t| is bounded above and below), λ1 and λ3. They satisfy λ1 + λ3 = ω(div_ω X) = 0.
- Non-hyperbolicity forces λ1 = λ3 = 0.
- λ* equals the maximum of the top exponent over ergodic invariant measures (standard semi-uniform subadditive theorem). By unique ergodicity this maximum is that of ω, so λ* = 0. Step 2 of the chain then gives h_top = 0. ∎

For any n, (V) together with GH therefore reduces (Lambda) to excluding non-hyperbolic ω with a positive exponent. In dimension 3 the problem is thus fully reduced to (V), which remains unproved.

## 4. Where the argument stops (open)

1. **(E1), measure form.** Does GH imply μ(d) = 0 for every ergodic invariant μ? Equivalently, by Prop 2.2, are there no nonnegative measure-distributions u ≠ 0 with Xu = κu for real κ ≠ 0? Proposition H shows that a counterexample would need uniformly dissipative horseshoes or non-hyperbolic measures. The tools tried here fail on this question:
   - multiplying u by a smooth w would need Xw = κw, which has no nonzero smooth solution;
   - the relation u = X(−u/κ) gives a non-smooth v with Xv = u, but u is not smooth, so it does not contradict GH;
   - mollification destroys the high-order bound needed in the estimate of L2.
2. **(N), non-vanishing of the limit currents.** This is open even when (E1) is granted. For n ≥ 3, sketch step (c) must also be replaced, since it yields a dimension-2 current (§1).
3. **(Lambda) in general, and zero entropy in general.** Both remain open here, as does dimension 3 without (V). Under (V), dimension 3 is settled by §3.

=== END OF ANSWER round5_q3 ===
