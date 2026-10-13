# round4_q6: answer

**Outcome in one line.** (V) is NOT proved and NOT refuted.
- Lemmas C, D, D1, D2, E and F are all correct.
- Proved here: under GH, (V) holds iff a single half-orbit has bounded log-Jacobian J_t (Proposition 1). This needs no unique ergodicity.
- Proved here: if (V) fails, every half-orbit whose J is bounded above has e^{J_t} → 0 in Cesàro density, and such half-orbits exist (Lemma 3, Corollary 4).
- The gap is to exclude this "null-recurrent" Jacobian behaviour.

**Note on the brief.** The "## Task" header of the query file states a different problem: a knot-surgery statement (M) about S^3_{2g-1}(K). Everything else in the file (the approach, the deliverable, the chain, the background, Lemmas C-F) is about statement (V): *GH implies that X preserves a smooth positive density*. I treat (V) as the task and do not address the knot statement (M). The pasted "planner's sketch" for (M) is ignored.

Plan:
- (0) Verify Lemmas C, D, D1, D2, E and F.
- (1) Prove a new criterion for (V) that needs no unique ergodicity: a single forward orbit along which J_t is bounded is enough.
- (2) Record what the conformal/Patterson route can and cannot give, and say where it stops.

Conventions are the planner's. ν is a smooth positive density and d = div_ν X. J_t(x) = ∫_0^t d(g_s x) ds for all real t; it is the log of the ν-Jacobian of g_t, so ∫_M e^{J_t} dν = ν(M). We write ν̂ = ν/ν(M). A finite measure T is called **conformal** if T(Xφ + dφ) = 0 for every smooth φ.

## Step 0. Verdict on the planner's lemmas

**Observation 0: correct.** For u = T/ν we have ⟨Xu, φν⟩ = −⟨u, (Xφ + dφ)ν⟩ = −T(Xφ + dφ). So Xu = 0 holds iff T is conformal. Under GH, L1 then says that the conformal finite measures are exactly the multiples cν.

**Lemma C: correct** (dim M ≥ 2). I checked each step.
- At a zero p, J_t = t·d(p), so the integral diverges.
- On a periodic orbit, e^{J_{t+nP}} = e^{J_t} e^{nJ_P}. This is not integrable over R, whatever the sign of J_P.
- In the non-periodic case, c(t) = e^{J_t} satisfies c(t) ≥ c(s) e^{−‖d‖_∞ |t−s|}. Integrability therefore forces c(t) → 0 as |t| → ∞, so the boundary terms vanish and T is conformal.
- T is carried by the orbit. The orbit is a countable union of the compact C^1 arcs g_{[n,n+1]}x, so it is ν-null when dim M ≥ 2. Hence T = Kν is impossible, since T(orbit) = T(M) > 0 = Kν(orbit).

**Corollary C1: correct.**
- The bound J_t ≤ b − a|t| makes ∫ e^{J_t} dt finite, which Lemma C excludes.
- The heteroclinic statement holds as written. Asymptotic phase along the strong stable (resp. strong unstable) manifold makes J_t(x) − J_t(y) converge exponentially fast. So J_t(x) decreases linearly in both time directions when ∫_{γ₋} d > 0 and ∫_{γ₊} d < 0.
- In a basic (transitive hyperbolic) set, W^{cu}(γ₁) ∩ W^{cs}(γ₂) ≠ ∅ for any two periodic orbits. A point of this intersection lies on a strong unstable leaf of γ₁ and on a strong stable leaf of γ₂. Sign 0 is excluded by Observation P.

**Lemma D: correct.**
- P(s) < ∞ for every s > 0 holds iff limsup_{|t|→∞} J_t/|t| ≤ 0. More precisely, finiteness for all s > 0 follows from that limsup condition, and the converse holds up to the borderline case, which is irrelevant here.
- c_s is Lipschitz and integrable with log-derivative bounded by ‖d‖ + s. So c_s → 0 at ±∞, by the same argument as in Lemma C.
- Integrating (c_s φ(g_t x))' over R gives |T_s(Xφ + dφ)| ≤ s‖φ‖_∞.
- Every weak* limit point of T_s is a conformal probability, hence equals ν̂. Compactness of the space of probability measures gives convergence of the whole family.

**Corollary D1: correct.** For μ ergodic, Birkhoff's theorem applied in both time directions shows that μ-a.e. x satisfies J_t(x)/t → μ(d) = 0 as t → ±∞. Such points can be chosen in supp μ. The closure of the orbit of x is contained in supp μ and carries every T_s, so it carries the limit ν̂, which has full support.

**Observation D2: correct, with the signs as stated.**
- Jensen's inequality gives ∫ J_t dν̂ ≤ log ∫ e^{J_t} dν̂ = 0 for every real t.
- (1/T)∫_0^T ((g_t)_*ν̂)(d) dt = (1/T)∫ J_T dν̂ ≤ 0. So forward limits μ₊ satisfy μ₊(d) ≤ 0.
- (1/T)∫_{−T}^0 ((g_t)_*ν̂)(d) dt = −(1/T)∫ J_{−T} dν̂ ≥ 0. So backward limits μ₋ satisfy μ₋(d) ≥ 0.
- By convexity there is always an invariant probability μ₀ with μ₀(d) = 0. It need not be ergodic.

**Lemma E: correct.**
- (i) Unique ergodicity makes J_t/t converge to μ(d) uniformly. If μ(d) ≠ 0, then ∫ e^{J_t} dν → 0 as t → +∞ (when μ(d) < 0) or as t → −∞ (when μ(d) > 0). This contradicts ∫ e^{J_t} dν = ν(M).
- (ii) follows from D1. Every orbit closure carries an invariant probability, which must be μ.
- (iii) uses the flow version of Gottschalk–Hedlund (cited from memory): for a minimal flow, a continuous f and some x₀ with sup_{t≥0} |∫_0^t f(g_s x₀) ds| < ∞, there is a continuous a with ∫_0^t f(g_s x) ds = a(g_t x) − a(x) for all x and t. The rest of the argument is correct, and it ends with R3-q1 §2(a).
- Proposition 1 below proves (iii) **without** unique ergodicity and without Gottschalk–Hedlund.

**Lemma F: correct.**
- (⇒) If Xρ = −dρ, then P(ρw) = ρXw. So Pv ∈ C^∞ gives X(v/ρ) ∈ C^∞, hence v/ρ is smooth, hence v is smooth.
- (⇐) Let μ be invariant and w = μ/ν. Then Pw = 0 by the convention L_X(wν) = (Xw + dw)ν, so w = ρ is smooth.
- If μ is ergodic, {ρ > 0} is open, invariant and nonempty, hence conull by (N1). Two distinct ergodic measures would then both be equivalent to ν, but distinct ergodic measures are mutually singular. Hence the flow is uniquely ergodic.
- The set {ρ = 0} is closed and invariant and has μ-measure 0. If it were nonempty it would carry an invariant probability, which must be μ. So it is empty.

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

**Remark on the chain (checked, not new).** Even with (V), the chain of this attempt does not close the original problem. Step 4 of the chain (the "Missing Lemma" of R3-q4, which excludes positive entropy together with a zero transverse exponent) remains open. The only cases that are complete given (V) are dim M ≤ 3 and the hyperbolic case. Steps 2 and 3 of the chain are correct as stated, given (V): I checked (O2), Lemma A and Step 1 of R3-q4.

**Literature (from memory, unverified, not used).** I recall that G. Forni (Contemp. Math. 469, 2008, on the Greenfield–Wallach and Katok conjectures) and A. Kocsard (dimension 3) relate GH to cohomology-free flows with a smooth invariant volume. I cannot reconstruct their arguments, so nothing above depends on them.

## Summary
- **Verified:** Observation 0, Lemma C, Corollary C1, Lemma D, Corollary D1, Observation D2, Lemma E and Lemma F are all correct as stated.
- **Proved (new):**
  - Principle G: Jacobian-weighted orbit segments with small endpoint weights equidistribute to ν̂.
  - Proposition 1: under GH, (V) ⇔ some half-orbit has bounded J. More generally, J bounded above together with a positive upper Cesàro mean of e^{J} gives (V).
  - Lemma 3: half-orbits with J bounded above always exist, for X or −X.
  - Corollary 4: if (V) fails, e^{J} has zero Cesàro density along all such half-orbits.
- **Open:** (V) itself, in the equivalent form stated under "Open (precisely)"; unique ergodicity under GH; and, downstream, the Missing Lemma of R3-q4.

=== END OF ANSWER round4_q6 ===

