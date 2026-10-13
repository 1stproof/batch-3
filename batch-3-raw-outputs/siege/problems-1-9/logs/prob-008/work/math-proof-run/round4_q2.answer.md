# round4_q2: answer on statement (V)

**Outcome.** I did NOT prove (V) and I found no counterexample. A counterexample would also be a GH vector field that is not conjugate to a Diophantine linear flow on a torus, i.e. a counterexample to the Greenfield–Wallach conjecture; I cannot construct one.

This file contains:
- §1: a check of planner lemmas C, D, D1, D2, E and F. All are correct, with small precisions.
- §2: a new reduction (Proposition G, fully proved). Under GH, (V) is equivalent to *closed range of the transposed operator P_1 = X + d on C^∞*. It is also equivalent to the solvability in D' of Xu = f for every smooth f annihilated by the smooth invariant densities.
- §3: further small results:
  - a.e. divergence of the Jacobian integrals;
  - an L²/unitary-group necessary condition.
- §4: the exact point where the argument stops.

Conventions are those of the brief. ν is a smooth positive density and d = div_ν X. A distribution u is identified with φ ↦ ⟨u, φν⟩, and ⟨Xu, φν⟩ = −⟨u, (Xφ + dφ)ν⟩. Write P_s = X + s·d. Then P_1 is (minus) the transpose of X, I is the space of invariant distribution densities, and I/ν = ker(P_1 on D'). J_t(x) = ∫_0^t d(g_s x) ds, so ∫ φ∘g_t e^{J_t} dν = ∫ φ dν.

## 1. Check of planner lemmas C–F

**Lemma C — correct.**
- Since |d/dt log c| ≤ ‖d‖_∞, we get c(t) ≥ c(s)e^{−‖d‖|t−s|}. So integrability of c forces c(t) → 0 as |t| → ∞.
- T(Xφ + dφ) = ∫_R (d/dt)[c(t)φ(g_t x)] dt = 0.
- By Observation 0 and L1, T = Kν with K = T(M)/ν(M) > 0.
- But T is carried by the orbit. The orbit is a countable union of C¹ arcs, so it is ν-null when dim M ≥ 2. Contradiction.
- The zero and periodic cases are as stated.

**Corollary C1 — correct as stated**, granted the standard facts on hyperbolic periodic orbits:
- exponential convergence along strong stable and unstable leaves;
- existence of heteroclinic orbits between periodic orbits of a transitive hyperbolic set.

Backward asymptotics to γ_1 give J_t(x) ≈ (∫_{γ_1} d / P_1)·t → −∞ linearly as t → −∞ when ∫_{γ_1} d > 0. Forward asymptotics to γ_2 give J_t → −∞ linearly when ∫_{γ_2} d < 0. Hence e^{J_t} is integrable, contradicting Lemma C. The sign 0 is excluded by Observation P.

**Lemma D — correct.**
- With c_s(t) = e^{J_t(x) − s|t|} we have c_s' = (d(g_t x) − s·sign t)c_s a.e.
- c_s → 0 at ±∞, because P(s) < ∞ for every s and the log-Lipschitz argument of C applies.
- Hence |T_s(Xφ + dφ)| ≤ s‖φ‖_∞.
- Weak* limit points are probability measures T with T(Xφ + dφ) = 0. So T = ν̂ by Observation 0 and L1.

**Corollary D1 — correct.**
- For ergodic μ with μ(d) = 0, Birkhoff in both time directions gives J_t(x)/t → 0 as t → ±∞ for μ-a.e. x, and such x can be taken in supp μ.
- T_s is supported in the orbit closure of x, which lies in supp μ.
- The limit ν̂ has full support, so supp μ = M.

**Observation D2 — correct, signs as stated.**
- ∫ e^{J_t} dν = ν(M), so Jensen gives ∫ J_t dν̂ ≤ 0 for every real t.
- For t > 0, ∫ J_t dν̂ = ∫_0^t ((g_s)_*ν̂)(d) ds ≤ 0. Hence forward limits μ_+ satisfy μ_+(d) ≤ 0.
- For t < 0, ∫ J_t dν̂ = −∫_t^0 ((g_s)_*ν̂)(d) ds ≤ 0. Hence backward limits satisfy μ_−(d) ≥ 0.

**Lemma E — correct.**
- (i) does not even use GH: uniform convergence J_t/t → μ(d) together with ∫ e^{J_t} dν = ν(M) for all t forces μ(d) = 0.
- (ii) follows from D1, since the UE measure is ergodic.
- (iii) uses the Gottschalk–Hedlund theorem for minimal flows (cited from memory): a continuous cocycle J_t that is bounded along one orbit is a continuous coboundary, J_t = a∘g_t − a. Then ρ = e^{−a} is a continuous positive invariant density, so log ρ is bounded. Lemma B (N3) then makes a smooth.

**Lemma F — correct.**
- If ω = ρν is invariant, then P_1(ρw) = ρXw, so P_1 is conjugate to X.
- Conversely, assume P_1 is GH. Then every invariant probability is ρν with ρ smooth and ρ ≥ 0.
- {ρ > 0} is open, nonempty and invariant, hence conull by N1. So any two ergodic measures are equivalent, hence equal.
- An invariant probability on Z = {ρ = 0} would have to be ρν, which gives Z measure 0. So Z = ∅.

## 2. New reduction (proved)

**Proposition G.** Assume GH and let K_∞ = {w ∈ C^∞ : P_1 w = 0}, the smooth invariant densities divided by ν. The following are equivalent:
- (a) (V);
- (b) P_1(C^∞) is closed in C^∞;
- (c) every smooth f with ∫ f w dν = 0 for all w ∈ K_∞ is of the form f = Xu for some u ∈ D'.

*Proof.*

(a) ⇒ (b). Let ρν be a smooth positive invariant density, so Xρ = −dρ. Then P_1(ρw) = ρXw + w(Xρ + dρ) = ρXw. Hence P_1(C^∞) = ρ·X(C^∞). This is closed: X(C^∞) is closed (Text A, L2), and multiplication by ρ is a topological automorphism of C^∞.

(b) ⇒ (c).
1. K_∞ is closed. P_1 induces a continuous bijection from the Fréchet space C^∞/K_∞ onto the closed, hence Fréchet, subspace P_1(C^∞). By the open mapping theorem its inverse is continuous.
2. Let f be as in (c). Define ℓ(P_1 w) = −∫ f w dν. This is well defined because f ⊥ K_∞, and it is continuous on P_1(C^∞) by step 1.
3. By Hahn–Banach, ℓ extends to a continuous functional on C^∞, i.e. to a distribution u with ⟨u, (P_1 w)ν⟩ = −⟨f, wν⟩ for all w.
4. By the convention, ⟨Xu, wν⟩ = −⟨u, (P_1 w)ν⟩ = ⟨f, wν⟩. So Xu = f.

(c) ⇒ (a).
1. **K_∞ ≠ 0.** Otherwise (c) applies to f = 1, giving 1 = Xu with u ∈ D'. By GH, u is smooth. At a maximum point of u we have Xu = 0 ≠ 1. Contradiction.
2. **Each real ρ ∈ K_∞ \ {0} is one-signed.** P_1 is real, so real and imaginary parts of kernel elements lie in K_∞. Along orbits, d/dt ρ(g_t x) = −d(g_t x)ρ(g_t x), so ρ(g_t x) = ρ(x)e^{−J_t(x)}. Hence {ρ > 0}, {ρ < 0} and {ρ = 0} are invariant.
   - {ρ ≠ 0} is open, nonempty and invariant, so it has positive measure and is conull by N1.
   - Of the disjoint invariant open sets {ρ > 0} and {ρ < 0}, exactly one is conull. The other is null and open, hence empty.
   - So, after a change of sign, ρ ≥ 0, and U = {ρ > 0} is open and conull.
3. **K_∞ = Cρ.** Let ρ' be another real element. Then r = ρ'/ρ is continuous on U and r(g_t x) = r(x). Its level sets {r > c} are invariant Borel sets, hence null or conull (N1). So r is a.e. constant, ρ' = cρ a.e., and by continuity everywhere.
4. **I = Cρν.** Normalise ∫ρ dν = 1. For smooth f, the function f − ∫fρ dν is ⊥ K_∞. By (c) it equals Xu, and by GH u is smooth. So it lies in X(C^∞) and is annihilated by every T ∈ I. Hence T(f) = T(1)·∫ fρ dν, i.e. T = T(1)ρν.
5. **ρ > 0 everywhere.** Z = {ρ = 0} is closed and invariant. If Z ≠ ∅, Krylov–Bogolyubov gives an invariant probability μ_Z carried by Z. By step 4, μ_Z = cρν. But ρν(Z) = 0. Contradiction.

So ρν is a smooth positive invariant density. ∎

**Remark.** By the closed-range theorem for Fréchet spaces (Treves, Thm 37.2, cited from memory), (b) is also equivalent to X: D' → D' having (weak*-)closed range. So (V) reduces to the "dual" a priori estimate: for every k there are m and C with dist_{C^k}(w, K_∞) ≤ C‖P_1 w‖_{C^m}. GH gives this estimate for X, not for P_1. The Peetre argument of Text A/B cannot be run for P_1, because it needs regularity for P_1, i.e. Lemma F's hypothesis.

## 3. Further small results

**Proposition H (proved modulo the Hopf criterion, cited).** Assume GH and dim M ≥ 2. Then for ν-a.e. x,
∫_0^∞ e^{J_t(x)} dt = ∫_{−∞}^0 e^{J_t(x)} dt = ∞.

*Cited (from memory): Hopf's criterion.* For a nonsingular flow with Radon–Nikodym cocycle ω_t = d(ν∘g_t)/dν, the conservative part is {x : ∫_0^∞ ω_t(x) dt = ∞} mod ν. The same holds with negative times.

*Proof.* Here ν(g_t B) = ∫_B e^{J_t} dν, so ω_t = e^{J_t}. The flow is conservative by N2, and so is the flow of −X, which is GH by (O4). Apply the criterion to both. ∎

**Corollary H1.** Under GH, every ergodic μ with μ(d) < 0 has a ν-null forward basin, and every ergodic μ with μ(d) > 0 has a ν-null backward basin. (On the forward basin, J_t(x)/t → μ(d) < 0, so the forward integral is finite.) Hence an ergodic measure with μ(d) ≠ 0 can never be a "physical" (SRB-type) measure of a GH flow.

**Observation U (L² picture; elementary).**
- V_t φ = (φ∘g_t)e^{J_t/2} is a unitary group on L²(ν), with generator P_{1/2} = X + d/2 (half-densities).
- If (V) holds, then J_t = b∘g_t − b with b bounded. So ⟨V_t 1, 1⟩ = ∫ e^{J_t/2} dν is bounded below by a positive constant.
- By the von Neumann mean ergodic theorem, w = lim (1/T)∫_0^T V_t 1 dt in L². Its inner product with 1 is lim (1/T)∫_0^T ⟨V_t 1, 1⟩ dt > 0, so w ≠ 0. Also w ≥ 0 and V_t w = w.
- Conversely, any such w gives an a.c. invariant measure w²ν whose density is > 0 a.e. (N1).
- That density gives (V) as soon as log w ∈ L¹(ν) (Lemma B / N3). I could not prove log-integrability. I could not prove w ≠ 0 from GH either.

## 4. Where the argument stops (exact gap)

By Proposition G, (V) under GH is equivalent to closed range of P_1 = X + d on C^∞. Equivalently, it is equivalent to a tame estimate for the transposed operator.

GH is a statement about P_0 = X. Every attempt to pass from P_0 to P_1 failed, for the following reasons.
1. **Perturbation or continuity in s for P_s = X + s·d.** Openness of {s : P_s is GH} would need the zeroth-order term s·d·u to be absorbed into the estimate ‖u‖_{C^k} ≤ C‖Xu‖_{C^m}, which has m > k in general. The loss of derivatives prevents this. The same obstruction blocks applying GH-type regularity to ρ^ε ∈ ker P_ε, where ρν is an a.c. invariant measure.
2. **Conformal side.** Lemmas C and D give complete control of ν-conformal objects for every orbit. But invariant measures are the kernel of P_1, and every equation they satisfy has a non-smooth right-hand side, so GH does not apply.
3. **Unique ergodicity.** This remains open under GH. Lemma E reduces (V) under UE to boundedness of J_t along one orbit, and I did not prove that boundedness.

**Open questions (named):**
- (Q1) Does GH imply that P_1(C^∞) is closed (equivalently, (V))?
- (Q2) Does GH imply unique ergodicity?
- (Q3) Under GH and UE, is J_t bounded?
- (Q4) Under GH, does the unitary group V_t have a nonzero fixed vector with log-integrable modulus?

From memory and unverified: I believe Forni (Contemp. Math. 469, 2008) discusses GH vs cohomology-free vector fields. I could not reconstruct any argument from it, and nothing above relies on it.

**On the chain (steps 1–3 of the brief).** I checked step 2 given (V). Lemma A gives I = Rω, so X(C^∞) = mean-zero functions with the tame estimate, and (O2) gives UE, no zeros and no periodic orbits. I found no flaw in steps 2–3. Step 3 relies on Katok's horseshoe theorem for C^{1+α} flows, which is cited.

=== END OF ANSWER round4_q2 ===
