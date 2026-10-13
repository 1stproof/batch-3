# Answer to round11_q2: attempt on (AP)

## Plan (stage 1)
1. Read the brief, especially Theorem J, Lemma K and Theorem G, and check the chain (Theorem R' Steps 1-4 with G ∩ Rec, and the reduction X -> -X).
2. Try for a pair-only argument in the case lambda = 0. Use recurrence (c) to build a two-sided decaying density from shifted copies of the pair density, and then apply Theorem J or Lemma D.
3. Write down any partial result (with proof) as soon as I have it.

## Progress log

### Stage 1: check of the chain (done)
I checked Steps 1-4 of the chain, with G replaced by G ∩ Rec, and the reduction X -> -X. I found no flaw.
- Rec is Borel: Rec = ∩_m ∩_N [∪_{t>=N} {z : dist(g_t z, z) < 1/m}] ∩ (the same with t <= -N). Each union over real t is open.
- nu'(Rec) = 1. Poincare recurrence for the homeomorphism g_1 on the separable metric space M gives: for nu'-a.e. z, g_n z returns to every neighbourhood of z for infinitely many n >= 1. Hence z ∈ ω(z). The same argument for g_{-1} gives z ∈ α(z).
- If nu'(A) = 1 then nu'^xi_x(A) = 1 for a.e. x. Together with the non-atomic conditionals (Lemma 6.0), this gives y ≠ x with y ∈ xi(x) ∩ G ∩ Rec. Pesin's local unstable manifold estimate at integer times, interpolated to real times, gives (a).
- In the reduction X -> -X, the log-Jacobian is J^{-X}_t = J_{-t}. Its Birkhoff limit is -lambda, and the entropy of nu' for g_{-1} equals its entropy for g_1. GH passes to -X by (O4).
So the chain is sound: (AP) for all lambda <= 0 implies the goal.

### Stage 2: two new facts in the volume-preserving case (proved)
Setting (V0): X is GH and preserves a smooth positive probability density ω. Take nu = ω, so d = 0 and J = 0. By (O2), every ω-mean-zero smooth ψ equals Xφ for a unique ω-mean-zero smooth φ =: Rψ. R is continuous on C^∞_0 (Text B, Cor. 3). In this setting (AP) reads: there is no bi-recurrent pair x ≠ y with dist(g_t x, g_t y) <= C e^{-θ|t|} for t <= 0.

**Lemma S (a single-observable form of Theorem J; proved).** Assume (V0). Let h be a smooth function with ∫h dω = 0, and put C(t) = ∫ (h∘g_t) h dω. If |C(t)| <= K e^{-ε|t|} for all real t, for some K and some ε > 0, then h = 0.
*Proof.*
1. C is even: C(-t) = ∫ (h∘g_{-t}) h dω = ∫ h (h∘g_t) dω by invariance of ω.
2. U_t f = f∘g_t is a strongly continuous unitary group on L^2(ω). By Bochner, C(t) = ∫ e^{iωt} dσ_h(ω), where σ_h is the spectral measure of h, a finite positive measure. Since C ∈ L^1, σ_h = ρ(ω) dω with ρ(ω) = (2π)^{-1} ∫ C(t) e^{-iωt} dt. Because C decays exponentially, ρ extends holomorphically to |Im ω| < ε. So ρ is real-analytic and ρ >= 0.
3. Put φ_0 = h and φ_k = R φ_{k-1}. All of these are smooth with mean zero, and h = X^k φ_k. The generator of U_t is X = iA with A self-adjoint, and smooth functions lie in its domain. The spectral measure of Aφ is ω^2 dσ_φ. Hence ρ(ω) dω = ω^{2k} dσ_{φ_k}, so ∫_{R∖{0}} ρ(ω) ω^{-2k} dω <= ||φ_k||^2_{L^2} < ∞ for every k.
4. Suppose ρ is not identically 0. Since ρ is analytic and >= 0, ρ(ω) >= c|ω|^m near 0 for some c > 0 and some m. Then the integral in step 3 diverges once 2k >= m + 1. Hence ρ = 0, so ||h||^2 = C(0) = σ_h(R) = 0. ∎
Remarks. (i) Theorem J needs decay of S(φ∘g_t) for every φ, uniformly in a C^k norm. Lemma S needs decay of a single autocorrelation, because positivity (Bochner) replaces the Jordan-chain and Fourier steps. (ii) Exponential decay is used only to make ρ quasi-analytic. Steps 3-4 already show that ρ vanishes to infinite order at 0 whenever ρ is C^∞; any decay of C that puts ρ in a quasi-analytic class (Denjoy–Carleman) is enough. (iii) Consequence: in a volume-preserving GH flow, no nonzero smooth observable has exponentially decaying autocorrelations. This would settle (PE0) in the volume case for any positive-entropy flow known to have one smooth observable with exponential (or quasi-analytic) decay of autocorrelation. Positive entropy alone gives no rate, so Lemma S does not close the gap.

**Lemma P (iterated primitives along an asymptotic pair; proved).** Assume (V0). Let x ≠ y satisfy dist(g_t x, g_t y) <= C_0 e^{-θ|t|} for t <= 0, and put S = δ_x - δ_y. Then for every ω-mean-zero smooth ψ and every n >= 1,
 |(R^n ψ)(x) - (R^n ψ)(y)| <= C_0 θ^{-n} ||dψ||_∞.
More precisely, M_n(ψ) := (1/n!) ∫_{-∞}^0 (-t)^n S(ψ∘g_t) dt = S(R^{n+1}ψ) for n >= 0.
*Proof.* Put F_φ(t) = S(φ∘g_t) = φ(g_t x) - φ(g_t y). Then |F_φ(t)| <= C_0 e^{-θ|t|} ||dφ||_∞ for t <= 0, and F_{Xφ} = F_φ'. For Re z < θ put V(z)(φ) = ∫_{-∞}^0 e^{-zt} F_φ(t) dt. This is holomorphic in z, and by Taylor expansion of e^{-zt} it equals Σ_n z^n M_n(φ) for |z| < θ. Integration by parts gives V(z)(Xφ) = F_φ(0) + z V(z)(φ). The boundary term at -∞ vanishes because Re z < θ. Take φ = Rψ and compare coefficients of z^n: M_0(ψ) = S(Rψ) and M_n(ψ) = M_{n-1}(Rψ). Hence M_n(ψ) = S(R^{n+1}ψ). The bound follows from |M_n(ψ)| <= (1/n!) ∫_0^∞ s^n C_0 e^{-θ s} ||dψ||_∞ ds = C_0 θ^{-n-1} ||dψ||_∞. ∎
Remark. R loses derivatives globally, but along an exponentially asymptotic pair the differences of the iterates R^nψ are controlled by the C^1 norm of ψ alone, with only geometric growth θ^{-n}. This is a necessary condition that GH imposes on any (AP)-pair. It needs neither recurrence nor genericity. I could not turn it into a contradiction; see Stage 3.

### Stage 3: a conditional closing criterion in case (V0), and where it stops
Notation as in Lemma P. For 0 < Re z < θ let T_z(φ) = ∫_R e^{-zt} F_φ(t) dt. This is the pair eigen-family of Theorem R': T_z(Xφ) = z T_z(φ), T_z(1) = 0, and |T_z(φ)| <= C_0 ||dφ||_∞/(θ - Re z) + 2||φ||_∞/Re z.

**Proposition E (proved).** Assume (V0). Let E_exp be the set of ω-mean-zero smooth ψ for which there is A = A_ψ with ||R^n ψ||_∞ <= A^n for all n. If E_exp + R·1 is dense in C^1(M), then no pair x ≠ y satisfies dist(g_t x, g_t y) <= C_0 e^{-θ|t|} for all t <= 0. In particular (AP) holds, and with the chain, every volume-preserving GH flow with this property has zero topological entropy.
*Proof.*
1. Fix ψ ∈ E_exp. Applying T_z(Xφ) = zT_z(φ) n times gives T_z(ψ) = z^n T_z(R^nψ). Split T_z = V(z) + T^+_z into the integrals over t <= 0 and t >= 0.
2. By Lemma P, V(z)(R^nψ) = Σ_m z^m S(R^{n+m+1}ψ), so |V(z)(R^nψ)| <= C_0 ||dψ||_∞ θ^{-n-1}/(1 - |z|/θ) for |z| < θ. Also |T^+_z(R^nψ)| <= 2A^n/Re z.
3. For real w with 0 < w < min(θ, 1/A): |T_w(ψ)| <= C(w/θ)^n + 2w^{n-1}A^n → 0 as n → ∞. So T_w(ψ) = 0 on an interval. Since z ↦ T_z(ψ) is holomorphic on the strip, T_z(ψ) = 0 on the whole strip.
4. T_z(1) = 0, and each T_z is continuous on C^1 (by the bound above). By density, T_z = 0 for every z in the strip.
5. Fix σ ∈ (0, θ). The function t ↦ e^{-σt} F_φ(t) is continuous and in L^1(R), and its Fourier transform η ↦ T_{σ+iη}(φ) vanishes identically. So F_φ ≡ 0, and in particular φ(x) - φ(y) = F_φ(0) = 0 for every smooth φ. Then x = y, a contradiction. ∎
Remarks.
(i) For Diophantine linear flows E_exp contains the trigonometric polynomials, so the hypothesis holds; but those flows have no asymptotic pairs anyway. I do not know whether GH implies density of E_exp. GH only gives tame bounds ||R^nψ||_{C^k} <= C_n ||ψ||_{C^{m_n}}, and for Diophantine flows applied to analytic data these grow like (n!)^τ with τ >= dim M - 1. That is again the non-quasi-analytic regime.
(ii) The same computation, without density, shows T_w(ψ) = -lim_{t→-∞} e^{w|t|} (u_w(g_t x) - u_w(g_t y)), where u_w = -∫_0^∞ e^{-ws} ψ∘g_s ds is the bounded continuous solution of (X - w)u_w = ψ along orbits. So (EF) for this pair, i.e. T ≡ 0, is equivalent to: for some (equivalently every) w ∈ (0, θ), the forward resolvent solutions u_w of a C^1-dense set of ψ have differences along the pair decaying faster than e^{-w|t|}. GH gives smooth, hence pair-Lipschitz, solutions only at w = 0. This is the barrier of round 10 ("GH acts only at the spectral point 0") in its simplest form. It is a reformulation, not progress.
(iii) Averaged pairs. With Pesin theory one can average the pair over a Pesin block, via a measurable ω-preserving map Φ moving points inside their unstable partition elements. This replaces δ_x - δ_y by hω with h = κ - κ∘Φ^{-1} ∈ L^2, and the forward bound by 2||φ||_{L^2}||h||_{L^2}/Re z. Then Proposition E holds with ||R^nψ||_{L^2} <= A^n in place of the sup norm. That hypothesis says that a C^1-dense set of smooth ψ have spectral measure vanishing near frequency 0. This is a spectral-gap condition, again not implied by GH as far as I can see. The details of the averaging (measurability of Φ, integrability of the Pesin constants) are only sketched here, so (iii) is a sketch.
(iv) Lemma S and the averaged pairs do not combine. The averaged-pair function h does have exponentially decaying autocorrelation, at least formally: C_hh(t) decays as t → -∞, and C_hh is even. But h is not smooth, so GH says nothing about its spectral measure at 0. Smooth functions, on the other hand, have no decay rates. This is the λ = 0 obstruction (forward cancellation) seen from the spectral side.

### Stage 4: remarks on the case lambda <= -θ for a bare pair
For λ < 0 the forward direction is free, and one needs backward cancellation of order k > |λ|/θ - 1. Every distribution built from finitely many Dirac masses on the two orbits O(x) ∪ O(y) has transport function Σ_i [time shift by t_i of a combination of F_x and F_y]. In the limit t → -∞, the terms with different shifts sit at the points g_{t+t_i}x, which are generically far apart. So only first-order cancellation (x against y at equal shifts) is available, and the backward rate cannot be improved beyond θ - |λ| in general. Recurrence only produces time shifts, which act as multipliers e^{-z t_i} on T_z and do not widen the strip. So a proof of (AP) for λ <= -θ must use points off the two orbits, e.g. the local unstable leaf (Prop. 6.2 of R6-a). This is a heuristic no-go for pair-only arguments, not a theorem. It suggests that (AP), as stated with a bare pair, may be strictly harder than what the chain needs. The chain itself supplies whole unstable leaves, and for those the case λ < 0 reduces, as in R6-a §6, to non-stationary normal forms (cited there, not checked).

## Final status
**Proved here:**
1. The chain (Theorem R' Steps 1-4 with G ∩ Rec, plus the reduction X -> -X) is correct (Stage 1).
2. Lemma S: under GH with a smooth invariant volume, no nonzero mean-zero smooth function has exponentially (or quasi-analytically) decaying autocorrelation.
3. Lemma P: under GH with a smooth invariant volume, along any backward-exponentially-asymptotic pair, |R^nψ(x) - R^nψ(y)| <= C_0 θ^{-n} ||dψ||_∞.
4. Proposition E: under GH with a smooth invariant volume, (AP) and hence zero entropy hold if the exponential-type vectors of R (in sup norm) are C^1-dense.

**Sketched only:** the L^2 / averaged-pair version of Proposition E (Remark (iii)), and the no-go remark for bare pairs with λ <= -θ (Stage 4).

**Not proved: (AP) itself, in both the case λ = 0 and the case λ <= -θ, and hence the problem's claim in dimension >= 4.** Explicitly open:
- (O-1) Volume case: does GH imply that exponential-type vectors of R are C^1-dense (sup norm), or that smooth functions with a spectral gap at 0 are C^1-dense? Either would settle the volume-preserving case through Proposition E and the chain.
- (O-2) General λ = 0: forward cancellation for a backward-asymptotic pair, i.e. (AC) of round9_q9 / (EF).
- (O-3) λ <= -θ for a bare pair, which by Stage 4 probably requires leaf structure.

No counterexample was found. The only known GH fields, the Diophantine linear flows, have no asymptotic pairs.

=== END OF ANSWER round11_q2 ===
