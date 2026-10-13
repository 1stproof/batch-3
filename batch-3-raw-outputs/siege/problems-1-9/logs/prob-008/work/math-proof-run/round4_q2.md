kind: attempt
Open question attempted: the missing statement (V) of this attempt's chain (ledger entry 19): global hypoellipticity forces a smooth invariant volume. Prove it completely, or give an explicit counterexample.

## Task
Give a complete rigorous proof of the following statement, or else an explicit counterexample to it (a GH vector field with no smooth invariant positive density).

**Statement (V).** Let M be a compact connected smooth manifold and X a smooth vector field on M such that every distribution u in D'(M) with Xu in C^infinity(M) lies in C^infinity(M) (global hypoellipticity, GH). Then there is a smooth density omega on M, positive everywhere, with L_X omega = 0. Equivalently: for one (hence every) smooth positive density nu, div_nu X = Xa for some a in C^infinity(M).

IMPORTANT: a proof of (V) for only some of the cases it covers — a sub-class of vector fields (e.g. uniquely ergodic ones, ones without zeros, low dimension) or a sub-range of parameters — does NOT answer the question, though it should be reported clearly (with full proof) if it is all you found. Likewise an equivalent reformulation of (V) is not an answer; report it only as a by-product.

Everything below the task is material you may use: results proved in earlier rounds (quoted verbatim, with proofs), the chain explaining what (V) is for, planner lemmas (unverified), and a sketch. Standard theorems (closed graph, Hahn-Banach, Krylov-Bogolyubov, Birkhoff, Hopf decomposition, Pesin theory, Gottschalk-Hedlund, Katok's closing/horseshoe theorems, ...) may be cited by name with a precise statement. Do not answer by recalling a proof from the literature: reason it out. Deliverable: either a complete proof (every step justified), or a counterexample, or — if neither — the strongest rigorously proved partial result with the exact point where the argument stops.

=== WHAT (V) IS FOR: THE CHAIN OF THIS ATTEMPT ===
The problem asks to show that a globally hypoelliptic (GH) vector field has a flow of zero topological entropy. The attempt's main line is:
1. (V) — the statement you are asked to settle: GH => X preserves a smooth positive density omega.
2. Given (V): by the results of [R3-q2] below (Lemma A) and observation (O2) of the background, the flow is uniquely ergodic with invariant measure omega, X has no zeros and (dim M >= 2) no periodic orbits, and every omega-mean-zero smooth f equals Xu with u smooth, with the tame estimate of Text B ("hypothesis H").
3. Given H: by [R3-q4] below, h_top(g_1) = h_omega(g_1) = sum of the positive transverse Lyapunov exponents of omega (variational principle + unique ergodicity; Pesin's formula), and h_omega = 0 whenever omega has no zero transverse exponent (Katok's horseshoe theorem for C^{1+alpha} flows gives periodic orbits, excluded in step 2). This finishes the problem when dim M <= 3.
4. After (V), exactly one further statement remains open in this attempt: under GH plus a smooth invariant volume, omega cannot have a positive exponent together with a zero transverse exponent ([R3-q4], "Missing Lemma"). You are NOT asked to prove that; it is stated only so that you can see what (V) is for. If you find that steps 1-3 are themselves flawed (e.g. that (V) would not give H), say so explicitly: that is a valuable result.
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

=== RESULTS OF THE PREVIOUS ROUND (quoted verbatim from three workers' answers) ===
[R3-q1: nonsingular ergodic theory checks; N1-N4 are the following planner observations, here verified: (N1) invariant Borel sets are null or conull; (N2) conservativity; (N3) L^1 solutions of the cohomological equation with smooth right side are smooth; (N4) reformulations of (V)]
# round3_q1: does GH imply (V), a smooth invariant volume?

**Outcome.** I did NOT prove (V), and I did not refute it. Below I check (N1)–(N4); all four are correct, with small precisions noted. I then prove two small new statements that sharpen the reduction. Last, I state the exact remaining gap and record the dead ends.

Conventions are those of Text B: ν is a smooth positive density, d = div_ν X, and J_t = ∫_0^t d∘g_s ds. A density ρν is invariant iff L_X(ρν) = 0, i.e. Xρ + dρ = 0 in D', i.e. ρ∘g_t · e^{J_t} = ρ a.e.

## 1. Verification of (N1)–(N4)

**(N1) Correct.** For an invariant Borel set B and a test function φ:
⟨X1_B, φν⟩ = −∫_B L_X(φν) = −(d/dt)|_{0} ∫_B g_t^*(φν) = −(d/dt)|_0 ∫_{g_tB} φν = 0.
L1 then makes 1_B a.e. constant. For a measurable invariant F, apply this to the sets {F > c}.

**(N2) Correct.** The Hopf decomposition is invariant, so by (N1) the flow is either conservative or totally dissipative. In the totally dissipative case the flow is measurably a translation flow on R × Y. Ergodicity then forces Y to be a single atom, so ν would live on one orbit. That is impossible when dim M ≥ 2, since an orbit is a ν-null C^1 curve. (When dim M = 1 we have M = S^1. GH then excludes zeros by P1 and by the sink/source argument of §2(b), so X has no zeros and (V) is trivial on S^1.)

**(N3) Correct.** Assume u ∈ L^1 and u∘g_{−t} − u = −∫_{−t}^0 f∘g_s ds a.e. Then
⟨Xu, φν⟩ = −⟨u, L_X(φν)⟩ = −(d/dt)|_0 ∫ (u∘g_{−t}) φν = ∫ fφν.
Differentiation under the integral is allowed because the difference quotient (1/t)∫_{−t}^0 f∘g_s converges uniformly to f.
For an invariant ρν, put a = log ρ. Then a∘g_t − a = −J_t, so Xa = −d. If a ∈ L^1, GH makes a smooth, and ρ = e^a is a smooth positive invariant density.

**(N4) Correct.**
- Suppose d − c = Xa with a ∈ D'. Then a is smooth by GH, e^{−a}ν is invariant, and c = 0 (O3).
- The C^m-closure version: use the C^0 case (k = 0) of Lemma 2 on the normalised u_n.
- The duality version: X(C^∞) is closed and equals the annihilator of the space I of invariant distribution densities.

## 2. New (small) results

**(a) Proposition.** Under GH, suppose some absolutely continuous invariant probability ρν has ν-density ρ with ρ^{−ε} ∈ L^1(ν) for some ε > 0. Then (V) holds.

*Proof.*
1. ρ > 0 a.e. by (N1), since {ρ > 0} is invariant and has positive measure.
2. We have |log ρ| ≤ ε^{−1}(ρ^{ε} + ρ^{−ε}).
3. ρ^ε ∈ L^1 by Hölder, because ν is finite and ρ ∈ L^1. So log ρ ∈ L^1.
4. Conclude by (N3). ∎

In particular (V) follows as soon as there is an invariant a.c. probability whose density is bounded below by a positive constant.

**(b) Proposition.** Under GH with dim M ≥ 2, X has no zero or periodic orbit that is a Lyapunov-stable attractor or repeller with an open basin. (For example, it has no hyperbolic sink or source, and no attracting or repelling periodic orbit.)

*Proof.*
1. Let K be such an attractor. Its basin W is open and invariant, so by (N1) it has full volume.
2. Pick a small closed ball A ⊂ W \ K of positive volume, at positive distance from K.
3. Every x ∈ A satisfies g_t x → K, so x returns to A only for t in a bounded set.
4. This contradicts conservativity (N2): Halmos recurrence says a.e. point of A returns to A at arbitrarily large times.
5. For repellers, apply the same argument to −X, which is GH by (O4). ∎

This is strictly more than P1 and Observation P. Those results exclude only zeros with d(p) = 0 and periodic orbits whose return map has Jacobian 1. Saddle-type zeros and saddle periodic orbits are still not excluded.

## 3. The remaining gap, stated exactly

By (N3), (N4) and §2(a), (V) is equivalent to each of the following:
- (G1) some invariant measure ρν ≪ ν has log ρ ∈ L^1(ν);
- (G2) every invariant distribution density T satisfies T(d) = c·T(1).

What is missing is any mechanism that turns GH, which is a statement about the operator X on functions, into regularity information for the transposed operator X + d, which acts on densities. Every invariant object (μ, ρ, a Maharam-invariant function) satisfies an equation of the form Xv = −dv or Xv = −iλdv. The right-hand side is not smooth, so GH does not apply.

**Dead ends checked.**
1. *Truncations.* Replacing a by a_N, or by e^{iλa} or ρ^s, gives X(·) = (bounded measurable function), not a smooth one.
2. *Smoothing.* Friedrichs mollification controls the error of Xρ_ε + dρ_ε only in L^1, never in C^m. So Lemma 2 cannot be invoked.
3. *Time changes.* hX has invariant densities I/h and divergence hd + Xh. Making that divergence vanish is (V) itself, so time changes give nothing new.
4. *The dual estimate (O1).* Applied to μ1 − μ2 for two invariant measures, it is satisfied by S = 0, so it gives no contradiction. For the same reason, unique ergodicity is not obtained here.
5. *Averaging.* The functions u_T = (1/T)∫_0^T J_t dt satisfy Xu_T = A_T d − d. But ||A_T d||_{C^m} is not controlled.

**Literature note (from memory, unverified).** I recall that Forni ("On the Greenfield–Wallach and Katok conjectures", c. 2008) and Kocsard (dimension 3) relate GH to unique ergodicity with a smooth invariant volume. I cannot reconstruct their proofs and do not rely on them.

**Open:**
- (V) itself;
- unique ergodicity under GH;
- the absence of saddle-type zeros under GH.


[R3-q2: Lemma A, V <=> dim I = 1]
# round3_q2: attempt on (V) — I did not settle it

Plan: reduce (V) to a statement about the dimension of I, prove that reduction rigorously, and record exactly where the gap is.

Notation is as in the brief. I is the space of X-invariant distribution densities. By Text A, X(C^∞) = I^⊥, and X(C^∞) is closed.

## Lemma A (proved). (V) holds if and only if dim I = 1.
Proof.
(⇐) Krylov–Bogolyubov gives an invariant probability measure μ, and μ ∈ I. So I = Rμ. Let c = μ(d)/μ(1). Then d − c is annihilated by I. By Text A, d − c = Xa with a smooth. By (O3), e^{-a}ν is a smooth positive invariant density, and c = 0.
(⇒) Let ω be a smooth invariant density, normalised to ω(M) = 1. Take T ∈ I and write T = vω with v ∈ D'. Since div_ω X = 0, we get L_X T = (Xv)ω, so Xv = 0 in D'. By L1, v is constant. ∎

So (V) is equivalent to: **every X-invariant distribution density is a constant multiple of one invariant probability measure.** In particular, (V) implies unique ergodicity.

## Lemma B (proved). If μ ∈ I is a measure with μ = ρν for some ρ ∈ L¹(ν) with log ρ ∈ L¹(ν), then (V) holds.
This is planner observation (N3). I checked it: the invariance of ρν means L_X(ρν) = 0, i.e. Xρ + dρ = 0 in D'. Formally, a = log ρ satisfies Xa = −d. Rigorously, J_t is the log-Jacobian, and invariance gives ρ∘g_t · e^{J_t} = ρ a.e. Hence a∘g_t − a = −J_t = −∫_0^t d∘g_s ds a.e. Pairing with test densities and differentiating at t = 0 gives Xa = −d in D'. Then GH makes a smooth, and e^{a}ν is the smooth invariant volume. ∎
So (V) also follows from the existence of one absolutely continuous invariant measure whose density is log-integrable.

## Where the attempts stop
(a) Microlocal route. For T = vν ∈ I we have (X + d)v = 0. The operator P = X + d has real principal symbol iξ(X), and Hörmander's propagation theorem makes WF(v) invariant under the lifted flow in Σ. To transfer this to X one would need an order-0 pseudodifferential operator A with Xu ∈ C^∞ for u = Av. This needs [X, A]v − A(dv) ∈ C^∞, i.e. a symbol a with H_p a = d·a near WF(v), together with control at infinity. Solving H_p a = d·a along the lifted flow requires the Jacobian cocycle ∫ d along orbits to be bounded. That is exactly (V) again, so the argument is circular. I could not break the circularity.

(b) Finite-dimensionality of I would not suffice anyway. Lemma A needs dim I = 1, and I see no argument from the closed-range and a priori estimates (Text A/B) that bounds dim C^∞/X(C^∞).

(c) I could not exclude zeros of X beyond P1 (which gives d(p) ≠ 0), nor dissipative periodic orbits beyond R-b.

From memory, and not verified: the literature on the Greenfield–Wallach and Katok conjectures (Forni; Kocsard; Hurder; Chen–Chi) treats "GH ⟹ cohomological rigidity / smooth invariant volume" as nontrivial. As far as I recall it is settled only in low dimensions (dimension 3 via Forni and Kocsard, with some extra input). So (V) in general may well be open.

## Summary
- **Proved:** (V) ⇔ dim I = 1 ⇔ uniqueness of the invariant distribution density. Also proved: (V) follows from the existence of an absolutely continuous invariant measure with log-integrable density.
- **Open:** (V) itself, and the uniqueness of invariant distributions (or even of invariant measures) under GH.
- **Consequence for the problem:** the zero-entropy problem additionally needs lemma (M) of R-d, even assuming (V).


[R3-q4: the downstream part of the chain, given (V)]
# round3_q4: answer

**Status.** I did not prove the full core statement. What follows is:
- a proved reduction;
- a proved partial result: zero entropy when dim M ≤ 3, and more generally whenever ω has no zero transverse Lyapunov exponent;
- the exact missing lemma, stated precisely.

Results quoted from the literature are cited from memory.

## Setting
The hypotheses are H together with GH. By (O2), ω is the unique invariant probability measure. The flow has no zeros and no periodic orbits when dim M ≥ 2. I have checked (O2) myself: if μ is invariant, then v = μ/ω satisfies Xv = 0 in D', because div_ω X = 0. So v is constant by L1. A periodic orbit would carry an invariant probability measure different from ω.

## Step 1 (proved, using standard theorems). h_top(g_1) = h_ω(g_1).
This follows from the variational principle, h_top = sup over invariant probability measures μ of h_μ, because ω is the only invariant probability measure.

## Step 2 (standard). Exponents.
By Oseledets, ω-a.e. point has Lyapunov exponents of g_1. One of them is 0, in the flow direction. Call the others transverse and write them λ_1 ≥ … ≥ λ_{n-1}. Under H, ω is ergodic, so the exponents are constants. Since ω is a smooth invariant volume, the sum of all exponents equals ∫ div_ω X dω = 0. Pesin's formula (cited) gives h_ω = Σ λ_i^+. In particular, if h_ω > 0 then λ_1 > 0 and λ_{n-1} < 0.

## Step 3 (proved, citing Katok's theorem). If ω is hyperbolic, then h_ω = 0.
Here "hyperbolic" means that no transverse exponent is zero.

**Cited theorem.** Katok (1980) proved this for C^{1+α} diffeomorphisms. The flow version is in Katok's work and in Lian–Young (cited from memory). Let φ_t be a C^{1+α} flow without fixed points, and let μ be an ergodic hyperbolic invariant probability measure with h_μ > 0. Then φ_t has periodic orbits, in fact horseshoes, and h_μ is approximated by the entropies of the horseshoes.

**Proof of Step 3.** Suppose h_ω > 0. Since ω is hyperbolic, the theorem gives a periodic orbit. But Setting excludes periodic orbits. This is a contradiction, so h_ω = 0. ∎

## Corollary (proved). If dim M ≤ 3, then h_top = 0.
- **dim M = 1.** The flow is a rotation of the circle, or has zeros. Either way the entropy is 0.
- **dim M = 2.** Flows on surfaces have zero topological entropy. This follows from Ruelle's inequality: there is only one transverse exponent, and it equals 0 because the exponents sum to 0. So h_ω = 0, and Step 1 gives h_top = 0.
- **dim M = 3.** There are two transverse exponents λ_1 and λ_2, with λ_1 + λ_2 = 0. If h_ω > 0, then λ_1 = −λ_2 > 0, so ω is hyperbolic, and Step 3 gives a contradiction. Hence h_top = h_ω = 0.

## Reduction (proved). The core statement is equivalent to the following lemma.

**Missing Lemma (open).** Let g_t be a C^∞ flow on a compact manifold with the following properties:
- it preserves a smooth volume ω;
- it is uniquely ergodic and has no periodic orbits;
- it satisfies GH (and hence H, by the background results);
- ω has positive exponents.

Then ω has no zero transverse exponent.

**Why the lemma implies the core.** Assume the lemma and suppose h_ω > 0. Then ω has a positive exponent (Step 2), so by the lemma ω is hyperbolic, and Step 3 gives a contradiction. So h_ω = 0, and Step 1 gives h_top = 0.

**Equivalent form.** "The lemma" can be replaced by "h_ω > 0 is impossible for ω with a zero transverse exponent". The first open case is dim M = 4 with transverse exponents (λ, 0, −λ).

## Directions examined and not completed
None of these is claimed as proved.
- **(i) Martingale construction.** One could build a non-smooth L^1 solution U of XU = f from conditional expectations onto an increasing partition subordinate to W^u. The obstruction is that such a sum is the smooth solution u itself whenever f is a coboundary, and every mean-zero smooth f is a coboundary. So no non-smooth candidate arises unless f is non-smooth. Then N3 does not apply.
- **(ii) and (iii) Zero exponents.** I found no mechanism by which GH controls the centre directions E^0. The tame estimate loses derivatives (dead end 4 of R-c), so it cannot control subexponential growth or exponential growth along E^0 or E^u.

## Summary
- **Proved:** zero topological entropy under H+GH when dim M ≤ 3, and in any dimension whenever ω has no zero transverse exponent.
- **Open:** the Missing Lemma above, that is, the non-hyperbolic case.

=== END OF RESULTS OF THE PREVIOUS ROUND ===

=== PLANNER LEMMAS C-F (written by the planner of this attempt; believed correct but NOT yet checked by anyone — verify each step before you use it, and say so explicitly if one is wrong) ===
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
=== END OF PLANNER LEMMAS ===

=== PLANNER'S SKETCH OF WHY (V) SHOULD HOLD (a suggestion only; discard it if you see a better route) ===
- GH controls the operator X on functions; its distributional kernel corresponds (Observation 0 of the planner lemmas) to nu-conformal finite measures T (T(X phi + d phi) = 0), and GH + L1 say nu is the only one. (V) is the analogous uniqueness for the transposed operator X + d, whose kernel corresponds to invariant measures (Lemma F: (V) <=> X + d is GH). The task is to transfer uniqueness from the conformal side to the invariant side.
- Lemma C (no finite conformal measure on one orbit) and Lemma D (Jacobian-weighted orbit averages equidistribute to nu for every orbit with subexponential Jacobian) are the conformal-side information GH gives pointwise, for EVERY orbit — much more than Lebesgue-a.e. statements.
- Proposed route: (a) prove unique ergodicity: if mu_1 != mu_2 are ergodic, or one ergodic mu has mu(d) != 0, use Pesin stable/unstable manifolds of the ergodic measures (or Katok-type closing when available) together with Lebesgue ergodicity/conservativity (N1, N2) to produce orbits, or a measurable family of orbits, carrying a finite measure T with T(X phi + d phi) = 0 (a generalised Lemma C), or else a nu-non-trivial invariant set; Observation D2 provides invariant measures with mu(d) <= 0 and with mu(d) >= 0 to start from. (b) Under unique ergodicity, Lemma E reduces (V) to boundedness of J_t along one orbit; if J_t is unbounded on every orbit (while J_t = o(|t|) uniformly), try a Patterson-type construction along a well-chosen orbit, with weights e^{J_t - s|t|} modified by the excursions of J, to produce a finite measure T != c nu with T(X phi + d phi) = 0, contradicting L1; or prove directly that d - 0 lies in X(D') (then N4 gives (V)).
- Alternatively prove directly that the transposed operator X + d has closed range on C^infinity, or is GH, by duality with the closed range of X (Text A/B) — beware: round3_q2 found a naive microlocal commutator argument circular.
=== END OF SKETCH ===
