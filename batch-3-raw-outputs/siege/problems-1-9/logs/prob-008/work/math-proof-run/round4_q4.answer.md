# round4_q4: attempt to refute (V), or to prove it

## Outcome
- I did **not** refute (V).
- I did **not** prove (V).

What this file contains:
- (A) A check of planner Lemmas C, D, E, F. All four are correct; small precisions are noted.
- (B) New results, all proved:
  - an intrinsic reformulation of (V): every invariant distribution density kills div X;
  - a bounded-deviation lemma;
  - a generalised "no attractor" lemma: no proper closed invariant set has a basin of positive volume;
  - a structural description of what any counterexample must look like.
- (C) An analysis of the suggested candidate classes, giving the exact obstruction for each.
- (D) The chain (steps 1–3): I found no flaw in it.
- (E) A literature remark, from memory and unverified: refuting (V) would refute the Greenfield–Wallach conjecture.

Conventions are as in the brief: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, ν̂ = ν/ν(M), and I is the space of X-invariant distribution densities.

---

## A. Verification of the planner lemmas

**Observation 0. Correct.** For a finite measure T and u = T/ν:
⟨Xu, φν⟩ = −⟨u, L_X(φν)⟩ = −T(Xφ + dφ).
ν itself satisfies the condition, because ∫(Xφ + dφ)dν = ∫ L_X(φν) = 0. By L1, under GH the only such T are the constant multiples Kν.

**Lemma C. Correct.** I checked each step.
- Lipschitz bound: (log c)' = d(g_t x), so c(t) ≥ c(s)e^{−‖d‖|t−s|}.
- Integrability then forces c(t) → 0 as |t| → ∞.
- The boundary terms vanish, so T(Xφ + dφ) = 0.
- By L1, T = Kν.
- T is carried by the orbit. For a non-periodic, non-singular orbit this is a countable union of compact C¹ arcs, which is ν-null when dim M ≥ 2. Hence K·ν(M) = K·ν(M \ orbit) = T(M \ orbit) = 0, so K = 0, which contradicts T(M) > 0.
- Zeros and periodic orbits are handled correctly.

**Corollary C1. Correct.** If J_t(x) ≤ b − a|t|, the integral is finite, contradicting Lemma C.
- Heteroclinic part. Points on W^s(γ₂) converge to g_t y exponentially, with an asymptotic phase y. Since d is Lipschitz, J_t(x) − J_t(y) converges. Along γ_i, J_t grows linearly with slope (∫_{γ_i} d)/P_i. So an orbit from a volume-expanding γ₁ to a volume-contracting γ₂ has J_t(x) ≤ b − a|t|.
- In a transitive (basic) hyperbolic set, any two periodic orbits are joined by heteroclinic orbits in both directions (cited: standard, via the shadowing lemma or the spectral decomposition). So every periodic orbit in it has ∫_γ d of one strict sign; the sign 0 is excluded by Observation P.

**Lemma D. Correct.** Some details:
- "P(s) < ∞ for all s > 0 ⟺ limsup J_t(x)/|t| ≤ 0". The forward direction uses the same Lipschitz argument as Lemma C.
- c_s is Lipschitz and log-Lipschitz, so c_s → 0 at ±∞.
- Integration by parts gives ∫c_s(Xφ + dφ)(g_t x)dt = s∫sgn(t)c_s(t)φ(g_t x)dt. Hence |T_s(Xφ + dφ)| ≤ s‖φ‖_∞.
- Weak-* limits are probability measures annihilating Xφ + dφ, so by Observation 0 and L1 they equal ν̂.
- The lemma does not need P(s) → ∞.

**Corollary D1. Correct.** Take x with J_t(x)/t → μ(d) = 0 as t → ±∞ (Birkhoff in both time directions) and x ∈ supp μ. The closure of the orbit of x lies in supp μ, which is closed and invariant. That closure carries every T_s, so it also carries the limit ν̂, which has full support.

**Observation D2. Correct, with the signs as stated.**
- ∫e^{J_t}dν = ∫d(g_t^*ν) = ν(M), for every real t. By Jensen, ∫J_t dν̂ ≤ 0 for every t.
- Forward averages: μ₊(d) = lim (1/T)∫J_T dν̂ ≤ 0.
- Backward averages: ∫_{−T}^0 d∘g_s ds = −J_{−T}, so μ₋(d) = lim (1/T)∫(−J_{−T})dν̂ ≥ 0.

**Lemma E. Correct.**
- Part (i) does not use GH: it only uses unique ergodicity (UE) and D2-type mass conservation.
- In (iii), the cited Gottschalk–Hedlund theorem for flows (from memory) reads: if the flow is minimal, F is continuous, and sup_{t≥0}|∫_0^t F(g_s x₀)ds| < ∞ for one x₀, then F = −(Xa) in the integrated sense, i.e. ∫_0^t F∘g_s = a∘g_t − a with a continuous.
- With ρ = e^{−a} we get ρ∘g_t · e^{J_t} = ρ, the invariance of ρν. This density is bounded below, so R3-q1 §2(a) gives (V).
- The converse in (iii) holds trivially: J_t = log ρ − log ρ∘g_t is bounded. So under GH + UE, (V) ⟺ J_t is bounded along one forward orbit ⟺ J_t is bounded uniformly in (x, t).

**Lemma F. Correct.**
- (⇒) P(ρw) = ρXw + w(Xρ + dρ) = ρXw.
- (⇐) For invariant μ and w = μ/ν, ⟨Pw, φν⟩ = −μ(Xφ + dφ) + μ(dφ) = −μ(Xφ) = 0.
- The remaining steps (N1, mutual singularity of distinct ergodic measures, and the closed set Z = {ρ = 0}) are as written.
- More generally: (V) ⟺ every element of I is a smooth density.

---

## B. New results (proved)

### B1. Intrinsic form of (V)
For S ∈ I set Φ(S) = S(div_ν X).

**Claim:** Φ does not depend on ν, and (V) ⟺ Φ ≡ 0 on I.

*Proof.*
- Independence of ν: div_{e^aν}X = d + Xa, and S(Xa) = 0 because S is invariant.
- (⇐) Suppose Φ ≡ 0. Then d ∈ I^⊥ = X(C^∞) (Text A duality). So d = Xa' with a' smooth, and taking a = −a' in (O3) gives d + Xa = 0. Hence e^{a}ν is invariant.
- (⇒) Suppose ω = ρν is smooth, positive and invariant. Then d = −X log ρ ∈ X(C^∞), so S(d) = 0 for every S ∈ I. ∎

Comment. For an ergodic invariant measure μ, Φ(μ) = μ(d) is the sum of all Lyapunov exponents of μ. So (V) says: every invariant distribution has "total exponent zero". Any counterexample must contain some S ∈ I with S(div X) ≠ 0.

### B2. Bounded deviation (a strengthening of O1)
There are m and C such that for every x ∈ M and T ∈ ℝ:
- ∫_0^T δ_{g_t x} dt = R − S;
- R ∈ I ∩ (C^m)';
- ‖S‖_{(C^m)'} ≤ C.

*Proof.* By Text B Lemma 2 with k = 0:
|u(g_T x) − u(x)| ≤ 2‖u − mean‖_∞ ≤ 2C₀‖Xu‖_{C^m}.
So Xu ↦ u(g_T x) − u(x) is a well-defined functional on X(C^∞), of (C^m)'-norm at most 2C₀. Extend it by Hahn–Banach to S ∈ (C^m)'. Then R := ∫_0^T δ_{g_t x}dt + S vanishes on X(C^∞), because ∫_0^T (Xu)(g_t x)dt = u(g_T x) − u(x). By duality, R ∈ I. ∎

So orbit segments are uniformly close to invariant distributions. This does **not** force dim I = 1, and I found no way to make it do so (see D).

### B3. No proper closed invariant set has a basin of positive volume (generalises R3-q1(b))
Assume GH and dim M ≥ 2. Let K ≠ M be a closed invariant set. Then the basin W(K) = {x : dist(g_t x, K) → 0 as t → +∞} is ν-null. By (O4) applied to −X, the same holds for the backward basin.

*Proof.*
1. W(K) is invariant. If ν(W) > 0, then W is conull by N1.
2. ν(K) = 0. Otherwise K is conull, and a closed conull set is all of M, since ν has full support.
3. Hence A_ε = {x ∈ W : dist(x, K) ≥ ε} has positive measure for some ε > 0.
4. Each x ∈ A_ε visits A_ε only during a bounded set of times.
5. Step 4 contradicts conservativity (N2): by Halmos recurrence, a.e. x ∈ A_ε returns to A_ε at arbitrarily large times. ∎

This excludes many things at once:
- attracting invariant tori and graphs, including non-uniformly attracting ones, provided their basin has positive volume;
- SRB-type attractors;
- in particular, any invariant measure that is physical (a basin of positive volume) and different from ν̂.

### B4. Hopf criterion
Under GH, ∫_0^∞ e^{J_t(x)}dt = ∞ for ν-a.e. x, and likewise backwards.

*Proof.* This is Hopf's characterisation of the conservative part (cited from memory: for a nonsingular flow, the conservative part is, mod ν, the set where ∫_0^∞ (d(g_t^*ν)/dν)(x)dt = ∞), combined with N2. ∎

Consequence. Every ergodic μ with μ(d) ≠ 0 has a ν-null statistical basin. This is consistent with B3.

### B5. Shape of any counterexample
Suppose X is GH, dim M ≥ 2, and (V) fails. Then exactly one of the following holds.
- **(a)** X has at least two ergodic invariant probability measures. Then:
  - by Lemma A, dim I ≥ 2;
  - every ergodic μ with μ(d) = 0 has full support (D1);
  - every proper closed invariant set has null basins (B3);
  - D2 provides invariant μ₊ and μ₋ with μ₊(d) ≤ 0 ≤ μ₋(d).
- **(b)** X is uniquely ergodic with measure μ. Then:
  - μ(d) = 0 and the flow is minimal (Lemma E);
  - J_t is unbounded along every orbit (Lemma E(iii) and its converse);
  - μ is not absolutely continuous with log-integrable density (R3-q2 Lemma B), and if μ ≪ ν then μ ~ ν;
  - by B1 there is S ∈ I, necessarily **not** a measure (since μ(d) = 0), with S(div X) ≠ 0.
  So in case (b) the counterexample must be a minimal, uniquely ergodic, smooth flow with unbounded Jacobian cocycle that nevertheless solves every smooth cohomological equation in the closed subspace I^⊥ with tame estimates. Its non-measure invariant distributions must detect the divergence.

---

## C. The candidate classes, with exact obstructions

1. **Smooth conjugates and smooth time changes of volume-preserving flows: never counterexamples.**
   - If Y preserves a smooth positive ω, then hY (h > 0) preserves ω/h: L_{hY}(ω/h) = d(i_Y ω) = L_Y ω = 0.
   - If Φ is a diffeomorphism, Φ_*Y preserves Φ_*ω.
   - So every smooth conjugate of a smooth time change of a Diophantine linear flow has a smooth invariant volume.
   - More generally, any X that is smoothly orbit-equivalent to a volume-preserving flow, with a smooth positive time change, has one.

2. **Skew products over Diophantine rotations with dissipative fibres, X = ω·∂_θ + V(θ, z)∂_z on T^k × F.**
   - Suppose some ergodic μ has a negative fibre exponent with an invariant attracting graph whose basin has positive volume. Then B3 excludes GH.
   - Suppose the fibre dynamics is smoothly reducible to a rotation or translation cocycle. Then the system is a smooth conjugate of a volume-preserving flow, which is case 1.
   - What remains is the non-reducible, zero-exponent, non-attracting case: for example a cocycle that is only C⁰-conjugate to a rotation, with unbounded J_t. This is exactly B5(b).
   - Deciding GH there would require solving Xu = f with tame estimates when the only invariant measure is singular. I found no such example and no proof that none exists. The natural obstruction is that a non-smooth conjugacy typically produces small divisors with Liouville-type behaviour, hence non-smooth distributional solutions. I could not make this rigorous in general.

3. **Dissipative saddle periodic orbits and horseshoes.**
   - Corollary C1: inside any basic hyperbolic set, all periodic orbits have ∫_γ d of one strict sign.
   - Suppose the sign is negative. Then the horseshoe's equilibrium states have negative total exponent. I could not derive a contradiction with GH from this alone: the horseshoe has ν-null basin, which B3 permits.
   - Building a GH example containing such a set would require GH-type cohomological rigidity near a hyperbolic set. Livšic theory there gives infinitely many independent invariant measures (one per periodic orbit), and that is compatible with closed range. So I see no rigorous route either way. This is the most plausible place for a genuine counterexample, but GH of such a flow is far beyond what I can verify.

4. **Parabolic and homogeneous flows (for example horocycle flows).** They preserve Haar volume, so they cannot be counterexamples.

---

## D. Dead ends, and why they fail
- **(i) Finite-dimensionality of I.** One would need an estimate ‖S‖_{H^{−k}} ≤ C‖S‖_{H^{−k−1}} on I ∩ H^{−k}, followed by Rellich. That estimate is hypoellipticity of the transpose L_X, which is (V) in disguise (Lemma F). The approach is circular.
- **(ii) Bounded deviation (B2).** It shows that empirical measures lie within O(1) of I in (C^m)', but it says nothing about the dimension of I or about Φ.
- **(iii) Gauge and potential deformation.** (V) asks whether GH of X + 0 implies GH of X + d, where X + d is the representation of L_X on densities. GH is invariant under potentials in X(C^∞) (gauge), but nothing transports it to potentials outside X(C^∞) + ℝ. Writing X = A − d/2 with A skew-adjoint in L²(ν), the question is GH(A − d/2) ⇒ GH(A + d/2). Here X ↦ −X and time changes give only GH(−A + d/2) and nothing about A + d/2.
- **(iv) Lemma D compared with unweighted averages.** Under UE, Jacobian-weighted averages converge to ν̂ and unweighted averages converge to μ. These are compatible whenever J_t is unbounded and sublinear, as in type III nonsingular flows. No contradiction arises.

---

## E. Status of (V) in the literature (from memory, unverified)
- The Greenfield–Wallach conjecture says: a GH vector field on a compact connected manifold forces M to be a torus and X to be smoothly conjugate to a Diophantine linear flow. That conclusion implies (V).
- So a counterexample to (V) would refute the conjecture, which I recall is open in dimension ≥ 4. I recall that work of Forni (c. 2008) and Kocsard (c. 2009) settles dimension 3, and also gives unique ergodicity together with a smooth invariant volume in some generality. I cannot reconstruct those proofs. I do not rely on them, and I cannot confirm that (V) is stated there in full generality.
- This strongly suggests that refuting (V) in this round is not realistic. A proof, if one exists by elementary means, must break the circularity in D(i) and D(iii).

## F. The chain (steps 1–3)
I checked steps 2–3 as quoted.
- (V) ⇒ I = ℝω (Lemma A), so X(C^∞) = {ω-mean-zero} with the Text B estimate. This is hypothesis H.
- Variational principle with UE gives h_top = h_ω.
- Pesin's formula applies to g_1, which is C^∞ and preserves ω.
- Katok's theorem for flows (cited) applies when no transverse exponent vanishes.

I found no flaw. The chain therefore needs (V) and the Missing Lemma of R3-q4. Both remain open.

## Summary
**Proved:**
- Lemmas C, D, E, F (verified).
- B1: (V) ⟺ every invariant distribution density annihilates div X.
- B2: bounded deviation.
- B3: under GH no proper closed invariant set has a basin of positive volume (forward or backward).
- B4: Hopf divergence of ∫_0^{±∞} e^{J_t}dt for ν-a.e. point.
- B5: the dichotomy for counterexamples. In the uniquely ergodic case, (V) ⟺ J_t is bounded, and a counterexample needs a non-measure invariant distribution S with S(div X) ≠ 0.

**Open:**
- (V) itself.
- Unique ergodicity under GH.
- Whether a GH flow can contain a dissipative horseshoe.
- Whether a minimal uniquely ergodic GH flow can have an unbounded Jacobian cocycle.

=== END OF ANSWER round4_q4 ===
