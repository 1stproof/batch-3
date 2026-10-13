# round9_q6 answer: statement (EF-0)

## 0. Status (summary)
- **(EF-0) is not proved here, and no counterexample is given.** I know of no GH field other than those smoothly conjugate to Diophantine linear flows, and for those (EF-0) holds by Fourier series (R8-b §4.1).
- Proved below, with complete proofs and using GH only through (F1) and (F2), i.e. through (K0) and (K1):
  - **Proposition 1.** The planner's mechanism (A), "subtract the ν-aligned singular part and use a Lemma-M variant with a ν-valued defect", works exactly when z -> T_z restricted to the hyperplane ker ν̂ has a holomorphic (or meromorphic) continuation, with order bounds, to a neighbourhood of 0. So (A) adds nothing beyond Lemma M except that the continuation is needed only modulo Cν. The open point is exactly continuation, or quantitative control, of G_z on ker ν̂ near 0.
  - **Proposition 2.** This generalises Theorem J*. Suppose the weighted transports S∘Γ_t converge as t -> +∞ and as t -> -∞, at a quasi-analytic rate and uniformly in C^k, to limits that need not be 0. Then S is a multiple of ν. In particular (EF-0) holds for every S whose forward transport converges at a quasi-analytic rate.
  - **Proposition 3** (Section 3). In the volume case, the eigen-family (or equivalently the forward Abel transform) of every (EF-0)-type S is flat at z = 0 in every proper sector, with explicit tame constants. This was already essentially known; it is recorded here together with the exact reason flatness is not enough.
- **Where it stops.** For the pair distributions that the chain actually produces, the forward transport S∘Γ_t (t >= 0) does not converge: the two forward orbits separate. GH, through (K0), (K1) or tame closed range, gives no quantitative information on G_z near z = 0 beyond infinite-order flatness without rates. Section 4 explains why every known consequence of GH is consistent, at the level of the analytic objects involved, with a nonzero S.

Notation is as in the task: P φ = Xφ + dφ, Γ_t φ = e^{J_t}(φ∘g_t), F_φ(t) = S(Γ_t φ), F_φ' = F_{Pφ}, ν(Pφ) = 0, ν̂ = ν/ν(M). Also ν(d) = 0, since ∫ d dν = ∫ L_X ν = 0. For an (EF-0)-type S of order k:
- T_z = B_z + G_z on 0 < Re z < ε;
- B_z(φ) = ∫_{-∞}^0 e^{-zt} F_φ dt is holomorphic on Re z < ε, with B_z∘(P - z) = S;
- G_z(φ) = ∫_0^∞ e^{-zt} F_φ dt is holomorphic on Re z > 0, with G_z∘(P - z) = -S and |G_z(φ)| <= C_δ ||φ||_{C^k}/(Re z - δ) for Re z > δ;
- T_z∘P = z T_z.

(F1): if T∘P = 0, then T ∈ Rν. (F2): if T∘P = c ν̂, then c = 0.

## 1. Proposition 1 (mechanism (A) = continuation modulo Cν)

**Proposition 1.** Assume GH. Let T_z (0 < Re z < ε) be the eigen-family of an (EF-0)-type S, or more generally any family satisfying (i)–(iii) of (EF) on the strip Σ(0, ε). Suppose there are:
- an open disc D centred at 0 with D_+ := D ∩ {Re z > 0} ⊂ Σ(0, ε);
- a family W_z, z ∈ D, of distribution densities such that z -> W_z(φ) is holomorphic on D for every smooth φ, and |W_z(φ)| <= C ||φ||_{C^K} for z in compact subsets of D;
- the property W_z(φ) = T_z(φ) for every φ ∈ ker ν̂ and every z ∈ D_+.

Then T_z = 0 on the whole strip; for an (EF-0)-type S this gives S = 0 (Theorem 2.1(A) of R8-b). The same conclusion holds if W_z is only meromorphic at 0, with the bounds on a circle around 0.

*Proof.*
1. Put W̃_z(φ) := W_z(φ - ν̂(φ)). This family is holomorphic on D, of order K, and W̃_z(1) = 0. On D_+ we have T_z(φ) = W̃_z(φ) + ν̂(φ) T_z(1), because φ - ν̂(φ) ∈ ker ν̂.
2. Take φ = 1. Since P1 = d and ν̂(d) = 0, z T_z(1) = T_z(d) = W̃_z(d) on D_+. So c(z) := z T_z(1) extends holomorphically to D as W̃_z(d).
3. For any φ, Pφ ∈ ker ν̂. Hence, on D_+,
   W̃_z(Pφ) = T_z(Pφ) = z T_z(φ) = z W̃_z(φ) + ν̂(φ) W̃_z(d).
   Both sides are holomorphic on D, so the identity holds on D by the identity theorem.
4. Expand W̃_z = Σ_n A_n z^n near 0. By Cauchy's formula on a circle, each A_n is a distribution density of order K. The identity of step 3 gives, coefficient by coefficient,
   A_n∘P = A_{n-1} + A_n(d) ν̂,  with A_{-1} = 0,  and A_n(1) = 0 for all n.
5. Induction on n. Suppose A_{n-1} = 0 (true for n = 0). Then A_n∘P = A_n(d) ν̂. By (F2), A_n(d) = 0. By (F1), A_n = a ν, and A_n(1) = 0 forces a = 0. So every A_n vanishes, and W̃ ≡ 0 near 0, hence on D.
6. Then, on D_+, T_z(φ) = ν̂(φ) T_z(1). So z T_z(φ) = T_z(Pφ) = ν̂(Pφ) T_z(1) = 0, and T_z = 0 on D_+. By the identity theorem T_z(φ) ≡ 0 on the strip for every φ.
7. Meromorphic case. Use Laurent coefficients A_n (n ∈ Z). The pole order is finite by the Baire argument of Lemma M. The least nonzero A_{n0} satisfies A_{n0}∘P = A_{n0}(d) ν̂, and step 5 shows A_{n0} = 0, a contradiction. ∎

**Consequences.**
- (a) Since B_z is holomorphic across 0, the hypothesis of Proposition 1 is equivalent to: the forward transform G_z, restricted to ker ν̂, has such a continuation. The one-sided Patterson lemma (R8-c, Lemma 2.2) says that the divergent part of G_s as s -> 0+ is aligned with ν̂. Proposition 1 shows that removing that part is the only thing the ν-aligned "defect" mechanism can do. Everything rests on the sub-leading behaviour of G_z on ker ν̂.
- (b) The Lemma-M variant asked for in the planner's step (2) is proved; it is steps 4–5. Its general form: a family A_z holomorphic near 0 with A_z∘P = z A_z + c(z) ν̂ must equal -(c(z)/z) ν̂. Here c is automatically holomorphic, being A_z(d) up to the normalisation A_z(1). So step (2) is settled, and the planner's step (3) (control of H_z near 0) is exactly the continuation hypothesis above. It is not proved.

## 2. Proposition 2 (two-sided convergence at a quasi-analytic rate)

Let w : [0, ∞) -> [0, ∞) be admissible as in Theorem J* (R7-a): M_j := ∫_R |t|^j e^{-w(|t|)} dt < ∞ for all j, and Σ_j M_j^{-1/j} = ∞. An example is w(t) = t/log(e + t).

**Proposition 2.** Assume GH. Let S be a distribution density of order k. Suppose that for every smooth φ the limits ℓ_±(φ) := lim_{t -> ±∞} F_φ(t) exist, with
 |F_φ(t) - ℓ_±(φ)| <= C e^{-w(|t|)} ||φ||_{C^k}  for ±t >= 0.
Then S = cν for a constant c, and ℓ_+ = ℓ_- = cν.
In particular, if F_φ(t) -> 0 as t -> -∞ (as in (EF-0)) and F_φ converges as t -> +∞ at an admissible rate, then S = 0.

*Proof.*
1. *The limits are multiples of ν.* For fixed t_0 we have |F_φ(t_0)| <= ||S|| ||Γ_{t_0}φ||_{C^k} <= C_{t_0} ||φ||_{C^k}. Hence ℓ_± ∈ (C^k)'.
   - From F_{Γ_s φ}(t) = F_φ(t + s), letting t -> ±∞ gives ℓ_±(Γ_s φ) = ℓ_±(φ). Here we use ||Γ_s φ||_{C^k} < ∞ for fixed s.
   - Differentiate at s = 0: (Γ_s φ - φ)/s -> Pφ in C^k. This gives ℓ_±∘P = 0, so ℓ_± = c_± ν by (F1).
2. *Subtract the limits.* Put F̃_φ(t) := F_φ(t) - c_+ ν(φ) H(t) - c_- ν(φ) H(-t), where H is the Heaviside function. Then |F̃_φ(t)| <= C' e^{-w(|t|)} ||φ||_{C^k}, and m̃_j(φ) := ∫ t^j F̃_φ dt are distribution densities of order k. Also F̃_{Pφ} = F_{Pφ}, because ν(Pφ) = 0.
3. *Moment relations.* Choose R_n -> ∞ with R_n^j (|F̃(R_n)| + |F̃(-R_n)|) -> 0. This is possible as in J*, step 3.
   - j = 0: ∫_{-R}^{R} F_{Pφ} = F_φ(R) - F_φ(-R) -> (c_+ - c_-) ν(φ).
   - j >= 1: ∫_{-R}^{R} t^j F_φ' = [t^j F_φ]_{-R}^{R} - j ∫_{-R}^{R} t^{j-1} F_φ dt.
   - First consequence: m̃_0∘P = (c_+ - c_-) ν. By (F2), c_+ = c_- =: c. By (F1), m̃_0 = a_0 ν.
   - Now F_φ = F̃_φ + c ν(φ) on all of R. The constant contributes c ν(φ)(R^j - (-R)^j) to the boundary term and -c ν(φ)(R^j - (-R)^j) to the integral term, so these cancel. Hence m̃_j∘P = -j m̃_{j-1} for j >= 1.
4. *Induction as in Theorem J.* If m̃_{j-1} = a_{j-1} ν, then m̃_j∘P = -j a_{j-1} ν. By (F2), a_{j-1} = 0, and by (F1), m̃_j = a_j ν. So all m̃_j = 0.
5. *Quasi-analyticity, as in J* step 5 (Denjoy–Carleman, cited).* The Fourier transform of F̃_φ has all derivatives at 0 equal to zero and lies in a quasi-analytic class, so it vanishes. Hence F̃_φ = 0 a.e. Since c_+ = c_- = c, F̃_φ(t) = F_φ(t) - c ν(φ) for t ≠ 0. So F_φ(t) = c ν(φ) for a.e. t, and by continuity for every t. At t = 0 this gives S(φ) = c ν(φ). ∎

*Remarks.*
- Proposition 2 contains Theorems J and J* (case c_± = 0) and Corollary E of R8-f.
- For an absolutely continuous S = wν, F_φ(t) = ∫ (w∘g_{-t}) φ dν. The hypothesis then says that the ν-transfer operator mixes w at a quasi-analytic rate in both directions, and the conclusion says w is constant.
- It does **not** apply to the pair distributions of Theorem R. Their forward transport e^{J_t(x)} φ(g_t x) - e^{b + J_t(y)} φ(g_t y) does not converge, since x and y separate forward. To use Proposition 2 one would need to smear S along a family of pairs, with a positive-measure set of base points, in such a way that the forward transport converges at a quasi-analytic rate. No rate of equidistribution is available for general positive-entropy measures; this is the "coarse tail" of R8-e §4.

## 3. Proposition 3 (volume case: sectorial flatness, recorded) and why flatness is not enough

Assume GH and that ω = ν is invariant (d = 0, P = X). Let R be the tame inverse of X on C^∞_0 (Text B, Corollary 3). For an (EF-0)-type S:
- T_z(1) = 0, because F_1(t) = S(1) is constant and decays as t -> -∞.
- T_z(φ) = z^N T_z(R^N φ_0) for every N.
- |T_z(ψ)| <= C ||ψ||_{C^k} (1/(ε - Re z) + C_δ/(Re z - δ)).
- Hence, in every sector |arg z| <= π/2 - η and for |z| small:
  |T_z(φ)| <= C_{η,N} |z|^{N-1} ||R^N φ_0||_{C^k} <= C'_{η,N} |z|^{N-1} ||φ||_{C^{m_N}}.
- So T_z is flat at 0 in every proper sector, with tame but uncontrolled constants. Equivalently, the forward Abel transform has the complete asymptotic expansion G_z ~ -Σ_j B_j z^j in each sector (B_j are the Taylor coefficients of B at 0).

This is Theorem V of R7-e and Lemma Q of R8-a in sectorial form; I record it only to make the failure point precise. Sectorial flatness of a function holomorphic on a half-disc and O(1/Re z) there does not force vanishing: e^{-1/√z}/(1+z) is a counterexample (Lemma 4.1 of R8-e). Lemma H needs quasi-analytic growth of the constants C'_{η,N}, and GH (closed graph theorem) gives no growth control.

## 4. Where the argument stops, and why (precise)

1. **The analytic objects are consistent with GH at every order at z = 0.** For an (EF-0)-type S:
   - the backward Jordan chain B_j∘P = B_{j-1}, B_0∘P = S has geometric bounds;
   - the forward transform has a ν-aligned divergent leading term (Patterson), killed modulo Cν by Proposition 1;
   - in the volume case it is flat to all orders in sectors (Section 3).
   (K0) and (K1) act only at the single point z = 0, and they act exactly through these Taylor/Laurent data. Proposition 1 shows that, given continuation, the data at 0 are all that is needed. Without continuation, flatness without rates carries no information (the e^{-1/√z} example).
2. **What a proof must supply.** One of the following:
   - (a) a continuation of G_z on ker ν̂ across 0 (Proposition 1);
   - (b) quasi-analytic convergence of a suitably smeared forward transport (Proposition 2);
   - (c) quasi-analytic sectorial bounds (Lemma H; in the volume case, quasi-analytic growth of ||R^N φ_0|| for a C^1-dense set of φ, by Theorem V);
   - (d) an entirely new use of GH at z ≠ 0.
   For (a)–(c) the needed input is quantitative information on the forward (coarse-scale) behaviour of transported distributions. That is a mixing-rate statement which neither positive entropy nor the qualitative GH hypothesis supplies.
3. **The full GH hypothesis at z = 0 does not obviously help either.** Full GH says that A∘P ∈ C^∞ ν implies A ∈ C^∞ ν; (K0) and (K1) are its special cases. In the relations of (EF-0) the right-hand sides are S, ν̂, or T_z itself, never smooth densities other than multiples of ν̂. So the extra content of full GH beyond (K0), (K1) enters only through the closed range of the unweighted X. By Proposition A of R8-d that gives no weighted information outside the volume case, and inside the volume case it gives exactly Section 3.
4. **Planner's mechanisms (B) and (C).**
   - (B): with V_z(ψ) := T_z(φψ) we get V_z∘X = z V_z - T_z((Pφ)·). Taking φ = e^a only replaces ν by e^a ν (d by d + Xa), so it is the same problem. A φ with Pφ = 0 exists only under (V) (Proposition A of R8-d). Approximate solutions of Pφ ≈ 0 in C^k exist only if μ(d) takes a single value c over all invariant μ, since the closure of R + X(C^∞) in C^k is cut out by the C^k-continuous invariant distributions, which include all invariant measures. So (B) reduces to the volume case, i.e. to Section 3.
   - (C) was not advanced.
5. **Chain check.** I re-checked the derivation "(EF-0) excludes every ergodic μ with h_μ > 0 and μ(d) = 0" (pair on a Pesin unstable leaf, Theorem R with λ = 0). It is correct modulo the cited Pesin, Ledrappier–Young and Ruelle inputs. So (EF-0) contains the volume-preserving case "GH + smooth invariant volume ⇒ h_ω = 0". That case is the core case #16 and is close to Katok's cohomological-stability conjecture. As far as I recall it is not known in dimension >= 4. I cite this from memory: the dimension-3 results are those of Kocsard and Forni.

## 5. Open questions (explicit)
- **(EF-0) itself.** Open.
- **(Q1)** Under GH, does G_z restricted to ker ν̂ continue (even meromorphically, or only as a hyperfunction with quasi-analytic sectorial bounds) across z = 0, for the pair distributions of Theorem R with μ(d) = 0? By Proposition 1 this suffices.
- **(Q2)** Volume case: does GH force, for a C^1-dense set of φ, quasi-analytic growth of ||R^N φ_0||_{C^0} or ||R^N φ_0||_{C^1}? By Theorem V and Lemma H this suffices.
- **(Q3)** Can one smear pairs along a positive-measure family so that the forward weighted transport converges to cν at a quasi-analytic rate? By Proposition 2 this suffices.

=== END OF ANSWER round9_q6 ===
