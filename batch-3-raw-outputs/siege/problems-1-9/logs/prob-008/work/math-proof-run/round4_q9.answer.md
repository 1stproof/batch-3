# round4_q9: answer

**Note on the brief.** The "## Task" block of the query file contains a statement "(M)" about hyperbolic L-space knots. It has nothing to do with this problem and was evidently pasted in from another task. I worked on the task stated in line 2 and in the rest of the file:
- (V): GH implies a smooth positive invariant density;
- (V'): P = X + d is GH.

**Plan.** First prove regularity criteria strong enough that the planner's line (1) closes. Then reduce (V) to elementary dynamical statements, and record where the argument stops.

**Conventions.** These are the brief's conventions.
- ν is a smooth positive density and ν̂ = ν/ν(M).
- d = div_ν X.
- J_t(x) = ∫_0^t d(g_s x) ds, so that (g_t)^*ν = e^{J_t}ν, i.e. ∫ F∘g_t · e^{J_t} dν = ∫ F dν.
- ⟨Xu, φν⟩ = −⟨u, (Xφ + dφ)ν⟩.
- L1: the only distributions u with Xu = 0 are the constants.

## Status

(V) is **not** proved in general. The following are **proved** below:
- **Theorem 1.** An a.c. invariant probability whose density is ≥ δ > 0 a.e. on some nonempty open set forces (V). In particular, a nonzero continuous (signed) invariant density forces (V).
- **Corollary 2.** This completes the planner's line (1): (V) holds if and only if P(C^∞) is closed in C^∞.
- **Theorem 3.** (V) holds if and only if some point x has sup_{t≥0} |J_t(x)| < ∞, i.e. one forward orbit has bounded volume distortion. No unique ergodicity and no Gottschalk–Hedlund argument are needed.

What remains open is to show that GH forces any one of these equivalent conditions.

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

## Summary of the equivalences now proved (under GH)

The following are equivalent:
- (V);
- (V'), by Lemma F;
- dim I = 1, by Lemma A of R3-q2;
- P(C^∞) is closed (Corollary 2);
- there is a nonzero continuous signed invariant density (Corollary 1');
- some a.c. invariant probability has density ≥ δ > 0 on a nonempty open set (Theorem 1);
- some forward orbit has bounded J_t (Theorem 3);
- some a.c. invariant probability has log-integrable density (N3).

## Where the argument stops (open)

1. **The main gap.** I could not derive any of these conditions from GH alone. The argument of Theorem 1 breaks for an a.c. invariant ρν with ρ merely measurable. The measures λ_n of Step 5 must converge weak* to ν̂, but they may concentrate on a dense open set of small measure where ρ is tiny, and weak* convergence cannot see this. So it is **open** whether GH plus the existence of an a.c. invariant probability implies (V). It is also open whether GH implies existence of an a.c. invariant measure at all (Krieger type II_1 versus II_∞ or III of the nonsingular ergodic flow (M, ν)).
2. **Closed range of P (Corollary 2).** This is equivalent to the a priori estimate dist_{C^k}(φ, ker P) ≤ C ‖Pφ‖_{C^m}. By duality it is also equivalent to weak*-closedness of X(D'). That in turn would follow from a "negative-order GH" estimate ‖u − c(u)‖_{H^{−r'}} ≤ C ‖Xu‖_{H^{−r}}, which I could not get from GH: the closed-graph argument only controls smooth right-hand sides.
3. **By-product (sketched, not fully checked).** Dualising the estimate (*) of Text A shows the following, with Sobolev bookkeeping:
   - GH of X is equivalent to injectivity of X on D'/C^∞, and to surjectivity of P on D'/C^∞;
   - (V') is equivalent to surjectivity of X on D'/C^∞.
   
   So (V) amounts to an "injective implies surjective" statement for X modulo C^∞. Microlocal arguments cannot give this, since GH depends on arithmetic (Diophantine) data.
4. **Analytic family.** Consider P_z = X − z d, with transpose P_z' = −P_{−1−z}, so that X = P_0 and P = P_{−1}. Under (V), every P_z is conjugate to X. I found no way to propagate GH from z = 0 to z = −1. Theorem 1 does use the real-s family ρ^s ∈ ker(X + s d) inside the proof, but only in the direction "invariant density ⇒ (V)".
5. **Downstream.** Even with (V), the chain needs the "Missing Lemma" of R3-q4 in dimension ≥ 4. That is untouched here, so the zero-entropy problem itself remains open in this attempt beyond dim M ≤ 3 given (V).

=== END OF ANSWER round4_q9 ===
