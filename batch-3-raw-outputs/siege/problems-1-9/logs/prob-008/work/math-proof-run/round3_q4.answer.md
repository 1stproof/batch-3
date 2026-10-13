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

=== END OF ANSWER round3_q4 ===
