# round12_q8 — answer

Plan. Part 1: derive the claim (zero topological entropy) from (PE0)+(R1)+(R2). Part 2: new first move = **quasi-invariant ("ν-conformal") measures with the volume Jacobian cocycle, built by thermodynamic formalism (eigenmeasures of transfer operators, Bowen–Ruelle–Sinai) on symbolic pieces of the flow**. I have not seen this used in "Tried so far": earlier work used Dirac combinations / normal forms / Jordan chains / spectral strips, never products of stable and unstable eigenmeasures solving a pressure equation. Status: Part 1 done. Part 2 gives new obstructions under GH, with proofs, and a fresh proof of the hyperbolic case. (PE0) itself is still open (§6).

Conventions. Distributions u ∈ D'(M) are identified with distributional densities σ = uν. For a distributional density σ, (L_Xσ)(φ) = −σ(Xφ). For a function u, L_X(uν) = (Xu + d·u)ν, where d = div_ν X.

## Part 1. (PE0) + (R1) + (R2) ⟹ zero topological entropy

By definition the topological entropy of the flow is h_top(g_1). (For every t ≠ 0, h_top(g_t) = |t| h_top(g_1), so the choice of time does not matter.) Suppose h_top(g_1) > 0. By (R1) there is a Borel probability μ that is g_1-invariant and ergodic with h_μ(g_1) > 0. By (R2), under GH, ∫ J_1 dμ = 0. So μ is g_1-invariant and ergodic, has h_μ(g_1) > 0 and ∫ J_1 dμ = 0, which is exactly what (PE0) says cannot exist. Contradiction, so h_top(g_1) = 0. ∎

The derivation is formally complete. Its only cost is that (R2) sits on Pesin theory, Ledrappier–Strelcyn and the normal forms, and I have not re-checked (R2) itself. (PE0) is not implausible on any ground I can name. It is not obviously as hard as the problem, but it does contain the volume-preserving case of the problem, which is the main case of the Katok/Greenfield–Wallach circle of questions.

## Part 2

### Lemma A (the conformal reformulation of ker X = constants)
Let σ be a distributional density with L_Xσ = d·σ. Then under GH, σ = cν for some constant c.

Proof. Put u = σ/ν ∈ D'. Then L_X(uν) = (Xu + du)ν, so (Xu)ν = L_Xσ − dσ = 0, i.e. Xu = 0. By (R4), u is constant. ∎

The relation L_Xσ = dσ means σ(Xφ) = −σ(dφ) for all smooth φ. Equivalently σ(φ∘g_t) = σ(φ·e^{J_{−t}}) for all t: σ has the same Jacobian cocycle as ν. **So GH forbids every finite measure σ ≠ cν whose flow Jacobian equals the ν-Jacobian.** The rest of Part 2 builds such measures from dynamics.

### Lemma B (periodic orbits and zeros)
Assume GH.
(i) If X(p) = 0, then d(p) = tr DX(p) ≠ 0.
(ii) If γ is a periodic orbit of period T through p, then ∫_0^T d(g_s p) ds ≠ 0. (This integral is log|det P| for the transverse Poincaré linearization P.)

Proof. (i) Take σ = δ_p. Then (L_Xσ)(φ) = −(Xφ)(p) = 0. If d(p) = 0, then L_Xσ = 0 = dσ, and Lemma A gives δ_p = cν, which is absurd.

(ii) Define σ(φ) = ∫_0^T φ(g_s p) e^{J_s(p)} ds, where J_s(p) = ∫_0^s d(g_τ p) dτ. Integrating by parts,
σ(Xφ) = ∫_0^T (d/ds)φ(g_s p) e^{J_s(p)} ds = φ(p)(e^{J_T(p)} − 1) − σ(dφ).
If J_T(p) = 0, then σ(Xφ) = −σ(dφ), i.e. L_Xσ = dσ. But σ is a nonzero positive measure on γ ≠ M, which contradicts Lemma A. (If dim M = 1 the problem is trivial.) ∎

Remark B' (sketch, not needed below). Replace δ_γ by distributions supported on γ of transverse order ≤ m. On these, the operator σ ↦ L_Xσ − dσ is a flat connection on a finite-rank bundle over γ, and its monodromy is block-triangular. One then gets: under GH, ∏_i λ_i^{1+α_i} ≠ 1 for every multi-index α ∈ ℕ^{n−1}, where λ_i are the eigenvalues of P. I have not written out the details of this generalisation.

### Lemma S (symbolic quasi-invariant measures with a prescribed Jacobian)
Let (Σ, T) be the two-sided SFT of an irreducible 0-1 matrix A, and let Φ: Σ → ℝ be Hölder. Put α = min_m ∫Φ dm and β = max_m ∫Φ dm, over T-invariant probabilities m. Suppose α < 0 < β, or α = β = 0. Then there is a Borel probability σ_0 on Σ with
(∗) T_*(e^Φ σ_0) = σ_0, i.e. σ_0(TB) = ∫_B e^Φ dσ_0 for all Borel B.

Proof.
(a) *Cohomology invariance.* Suppose Φ = Φ' + w∘T − w with w continuous, and τ satisfies (∗) for Φ'. Set σ_0 = e^w τ, normalized. Then T_*(e^Φ σ_0) = T_*(e^{w∘T} e^{Φ'} τ) = e^w T_*(e^{Φ'}τ) = e^w τ = σ_0.

(b) *Pressure equation.* We need a Hölder G with P(G) = P(G+Φ), where P is the pressure.
- If α = β = 0, then ∫Φ dm = 0 for every m, and the variational principle gives P(G+Φ) = P(G) for every G.
- If α < 0 < β, let p(τ) = P(τΦ). Then p is convex and C^1 with p'(τ) = ∫Φ dm_τ, where m_τ is the equilibrium state (Ruelle; cited from memory). Also p'(τ) → β as τ → +∞: indeed p' ≤ β, the variational principle gives τβ ≤ p(τ) ≤ h_top + τβ, and convexity gives p'(τ) ≥ (p(τ) − p(0))/τ → β. Likewise p'(τ) → α as τ → −∞. Hence f(s) = p(s+1) − p(s) = ∫_s^{s+1} p' is continuous, tends to β > 0 as s → +∞ and to α < 0 as s → −∞. Some s_0 has f(s_0) = 0; take G = s_0 Φ.

(c) *One-sided systems.* Let Σ⁺ be the space of one-sided sequences x = (x_0 x_1 …) with the shift S. Let Σ⁻ be the space of sequences y = (… y_{−2} y_{−1}) with the map S⁻ that deletes y_{−1}. Both are one-sided SFTs, the second for the transpose matrix.
- By Sinai's lemma (cited from memory), G is cohomologous, through a continuous transfer function, to ψ_1∘π⁺ with ψ_1 Hölder on Σ⁺. Likewise G+Φ is cohomologous to ψ_2∘π⁻ with ψ_2 Hölder on Σ⁻. Here π^± are the projections onto the future and past coordinates.
- By Ruelle's Perron–Frobenius theorem for irreducible A (cited from memory), there are probabilities ν⁺, ν⁻ with L_{ψ_1}^* ν⁺ = e^{P_1} ν⁺ and L_{ψ_2}^* ν⁻ = e^{P_2} ν⁻. Here P_1 = P(G) and P_2 = P(G+Φ), so P_1 = P_2.
- Applying L^* to f = 1_B e^{−ψ} gives: ν⁺(SB) = e^{P_1} ∫_B e^{−ψ_1} dν⁺ for Borel B inside a 1-cylinder. Similarly, for B⁻ ⊂ Σ⁻ and a symbol a with B⁻a admissible: ν⁻(B⁻a) = e^{−P_2} ∫_{B⁻} e^{ψ_2(ya)} dν⁻(y).

(d) *Product measure.* Identify Σ with the set of pairs (y, x) ∈ Σ⁻ × Σ⁺ with A_{y_{−1} x_0} = 1. Let σ_0 be ν⁻⊗ν⁺ restricted to Σ. It is nonzero because Ruelle eigenmeasures have full support. Then T(y, x) = (y x_0, Sx).
For a rectangle R = B⁻ × B⁺ with B⁺ ⊂ [a] and B⁻a admissible, T(R) = (B⁻a) × S(B⁺). By (c),
σ_0(TR) = ∫_R exp(ψ_2(y x_0) − ψ_1(x) + P_1 − P_2) dσ_0.
Such rectangles form a π-system generating the Borel σ-algebra, and both sides are finite measures in R, so σ_0(TB) = ∫_B e^Ψ dσ_0 for all Borel B, where Ψ = ψ_2∘π⁻∘T − ψ_1∘π⁺ + P_1 − P_2.
Since P_1 = P_2 and h∘T is cohomologous to h for continuous h, Ψ is cohomologous to (G+Φ) − G = Φ. By (a), (∗) holds for Φ after normalizing. ∎

### Proposition D (GH forbids "balanced" symbolic pieces)
Let (Σ, T) be an irreducible two-sided SFT with Hölder roof r > 0, let (Σ_r, φ_t) be the suspension flow, and let π: Σ_r → M be continuous with π∘φ_t = g_t∘π. Assume Φ(z) = ∫_0^{r(z)} d(π(z,s)) ds is Hölder; this holds e.g. for Bowen's Markov coding of a hyperbolic basic set, or a sub-SFT of it. Assume also that K = π(Σ_r) ≠ M.
Under GH, it cannot happen that inf_m ∫ d dm < 0 < sup_m ∫ d dm, nor that ∫ d dm = 0 for every m, where m ranges over the g-invariant probabilities that lift to Σ_r.

Proof. For a T-invariant m, the lifted flow-invariant measure m̄ satisfies ∫ d∘π dm̄ = ∫Φ dm / ∫ r dm, which has the same sign as ∫Φ dm. So the hypotheses of Lemma S hold for Φ; let σ_0 be the measure it gives. Put J_s(z) = ∫_0^s d(π(z,τ)) dτ and define
σ(φ) = ∫_Σ ∫_0^{r(z)} φ(π(z,s)) e^{J_s(z)} ds dσ_0(z).
This is a nonzero positive finite measure supported in K. For smooth φ, d/ds φ(π(z,s)) = (Xφ)(π(z,s)), and π(z, r(z)) = π(Tz, 0). Integrating by parts as in Lemma B,
σ(Xφ) = ∫ φ(π(Tz,0)) e^{Φ(z)} dσ_0 − ∫ φ(π(z,0)) dσ_0 − σ(dφ) = −σ(dφ).
The first two terms cancel by (∗) applied to z ↦ φ(π(z,0)). Hence L_Xσ = dσ. Lemma A gives σ = cν, which is impossible because supp σ ⊂ K ≠ M and σ ≠ 0. ∎

### Corollary E (consequences)
(E1) **Volume-preserving case, without (R2).** Suppose X is GH and preserves a smooth volume ν, so d = 0. Then X has no zeros and no periodic orbits (Lemma B), and no proper Hölder-coded symbolic piece as in Prop D, because all integrals of d vanish. In particular, every hyperbolic basic set of the flow is all of M or empty.

(E2) **Hyperbolic case of (PE0) (and of the problem), via a new route.** Suppose X is GH and μ is ergodic for the flow (or the flow-average of a g_1-ergodic measure), with h_μ > 0 and no zero Lyapunov exponent besides the flow direction. Katok's horseshoe theorem for C^{1+α} flows (cited from memory: Katok 1980 for diffeomorphisms, Lian–Young for flows) gives a nontrivial hyperbolic basic set Λ with h_top(Λ) > 0. Passing to a proper sub-horseshoe, which still has positive entropy, we may assume Λ ≠ M. Λ has a Bowen Markov coding, which is irreducible after choosing a component, Hölder, with Hölder roof.
- Without (R2): Prop D shows 0 ∉ (α, β) and (α, β) ≠ (0, 0) on Λ. In the volume case this is already a contradiction.
- With (R2): every equilibrium state m_τ of τΦ on the coding has positive entropy. Hence ∫Φ dm_τ = 0 by (R2), applied to the projected measures. So p'(τ) ≡ 0, and the limits computed in Lemma S(b) give α = β = 0, which contradicts Prop D.

So hyperbolic positive-entropy measures are impossible under GH. This reproves the known constraint (entry 60) by a different mechanism: conformal measures in place of normal forms.

## 6. Where the method stops; status of (PE0)

**What is proved here.**
- Part 1: complete.
- Lemmas A, B(i)(ii), S; Prop D; Corollary E1.
- E2: proved modulo the cited theorems of Katok/Lian–Young, Bowen (Markov sections), Ruelle (Perron–Frobenius and pressure), Sinai (one-sided reduction), and (R2) for the second bullet.
- Remark B' is only sketched.

**Why this does not settle (PE0).** Any hypothetical μ in (PE0) has a zero transverse exponent (entry 60, and E2 above). The construction of a ν-conformal measure in Lemma S/Prop D needs a symbolic model with Hölder Jacobian: a product of stable and unstable Ruelle eigenmeasures. With a centre direction there is no Markov coding and no horseshoe. Pesin-theoretic leafwise conditionals of μ have the right unstable Jacobian, but in the centre direction no transverse measure with the prescribed Jacobian e^{J_t} is available.

Heuristically, centre directions should make things worse for GH, not better. Remark B' gives resonance conditions ∏ λ_i^{1+α_i} ≠ 1. For periodic orbits whose centre multiplier λ_c is close to 1 with either sign of log|λ_c|, a large integer α_c lets Σ(1+α_i)χ_i cross 0. But I could not produce compact invariant sets with controlled centre behaviour from μ, so this remains a heuristic.

**Open questions (precise).**
- (Q1) The natural reformulation of (PE0) that this attempt points to: given g_1-ergodic μ with h_μ > 0 and ∫J_1 dμ = 0, construct a distributional density σ ≠ cν with L_Xσ = dσ. By Lemma A this suffices, and it uses only ker X|_{D'} = ℂ, not full GH.
- (Q2) Is the weaker hypothesis "every u ∈ D' with Xu = 0 is constant" already enough for h_top = 0? I have neither a proof nor a counterexample. Such a flow is ν-ergodic and has no wandering points, and Prop D applies to it.
- (Q3) Prove Remark B' in full, and find a centre-direction analogue of Lemma S. One candidate: measures on centre-unstable "fake leaves" with centre-direction derivatives, giving cocycles d + k·(centre log-derivative).
- (PE0) itself remains open.

=== END OF ANSWER round12_q8 ===
