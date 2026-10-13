# round8_q1: answer

## 0. Verdict

**(PE-NH) is NOT proved here, and I found no counterexample.** So the problem's claim (zero topological entropy under GH) stays proved only in the cases already in the ledger: dim M <= 3, hyperbolic measures, and the mu(d)-bands. Below I record:
- §1: a check of the chain;
- §2: two new statements with complete proofs, both only for the volume-preserving sub-class;
- §3: the exact point where every route I tried stops.

By the task's own rules, §2 does not answer the question. It is reported as a partial result.

## 1. Check of the chain

- **Step 4 (variational principle, flow-ergodic reduction): correct.** One remark. Jacobs' integral formula is usually stated for the g_1-ergodic decomposition. The flow-ergodic decomposition is coarser, but each flow-ergodic component decomposes further into g_1-ergodic measures. Composing the two decompositions gives the g_1-ergodic decomposition of mbar, so the formula h_mbar(g_1) = ∫ h_{mu_omega}(g_1) holds for flow-ergodic components too.
- **Step 2 (entry 60): no flaw found.** It inherits the citation of the Katok / Lian-Young horseshoe theorem, which needs mu(Zero X) = 0; that is proved there.
- **Step 1 (PE-NH): open** (see §3).

## 2. New partial results (volume-preserving case only; complete proofs)

**Setting.** GH holds and X preserves a smooth positive probability density omega. By (O2) and Lemma F of R7-d:
- the flow is uniquely ergodic;
- X(C^∞) = C^∞_0 (the omega-mean-zero smooth functions);
- R := X^{-1} : C^∞_0 → C^∞_0 is continuous (tame).

### Proposition 2.1 (closed 1-forms can be straightened)

Let α be a smooth closed 1-form and c := ∫ α(X) dω. Then there is a smooth function u with β := α − du satisfying β(X) ≡ c.

Suppose c ≠ 0 and the de Rham class [α] is integral. Then:
- there is a smooth Θ : M → R/Z with XΘ ≡ c, and F := Θ^{-1}(0) is a closed hypersurface transverse to X;
- the flow is the suspension of φ := g_{1/c}|_F with constant roof 1/c;
- h_top(g_{1/c}) = h_top(φ);
- φ is "GH" in the discrete sense: if v ∈ D'(F) and v∘φ − v ∈ C^∞(F), then v ∈ C^∞(F).

*Proof.*
1. **Straightening.** f := α(X) is smooth, and f − c lies in C^∞_0. So f − c = Xu with u smooth, and β(X) = f − Xu = c.
2. **The map Θ.** β is closed and has integral periods (it is cohomologous to α). Fix a base point and let Θ(x) be the line integral of β from the base point, taken mod Z. Then Θ is a well-defined smooth map M → R/Z with dΘ = β, so XΘ = c.
3. **The section and the suspension.** Since dΘ(X) = c ≠ 0, 0 is a regular value, so F is a closed hypersurface transverse to X. We have Θ(g_t x) = Θ(x) + ct. Hence every orbit meets F, the first return time is exactly 1/c everywhere, and g_{1/c} maps F onto F.
4. **Entropy.** g_{1/c} preserves every level set Θ^{-1}(s), and on that level set it is conjugate to φ via g_{s/c}. Restricting to F gives h_top(g_{1/c}) ≥ h_top(φ). For the reverse inequality, Θ is a factor map onto (R/Z, id), and Bowen's fibre inequality (cited from memory: h(T) ≤ h(S) + sup_y h(T, π^{-1}y) for a factor map π from T to S) gives h_top(g_{1/c}) ≤ 0 + h_top(φ).
5. **GH for φ.** Let v ∈ D'(F) with v∘φ − v = h smooth. Choose ρ ∈ C^∞_c((0, 1/c)) with ∫ρ = 1. Define f on M by f(g_s x) = h(x)ρ(s) for x ∈ F and 0 ≤ s < 1/c. This is smooth, since it vanishes near s = 0 and s = 1/c. Define u on M by u(g_s x) = v(x) + h(x)∫_0^s ρ for 0 ≤ s < 1/c. This is a distribution: in the coordinates (x, s) ∈ F × [0, 1/c) it is v ⊗ 1 plus a smooth function. It glues across F because v(φx) = v(x) + h(x)·1. Then Xu = ∂_s u = f is smooth. By GH, u is smooth, so v = u|_F is smooth. ∎

**Scope.** For volume-preserving GH flows with an integral class [α] such that ∫ α(X) dω ≠ 0, the problem is equivalent to the same problem for a discrete-time "GH" diffeomorphism. It is not solved by this. It is recorded because it removes the flow direction (and with it the temporal-shift issues of Theorem G) in this sub-class.

### Proposition 2.2 (bounded primitives of all orders for balanced unstable-disc measures)

Same setting. Let σ_0 be a finite signed measure with σ_0(1) = 0 and
|σ_0(φ∘g_t)| ≤ C e^{θt} ||φ||_{C^1} for t ≤ 0
(for example a balanced measure on a Pesin local unstable disc, as in R7-g §3.5). Put F_φ(t) := σ_0(φ∘g_t). Then for every smooth φ with ω(φ) = 0 and every N ≥ 0, the N-fold primitive of F_φ from −∞ is F_{R^Nφ}. It is bounded on all of R by ||σ_0||_TV ||R^Nφ||_∞ ≤ C_N ||σ_0||_TV ||φ||_{C^{m_N}}.

Moreover, the "two-sided integral" ∫_{−∞}^T F_φ(t) dt = F_{Rφ}(T) is bounded in T, and it tends to 0 along every sequence T_n → ∞ along which (g_{T_n})_*σ_0 → 0 weak*.

*Proof.*
1. **The derivative identity.** For mean-zero φ we have φ = X(Rφ). Hence F_φ(t) = σ_0((XRφ)∘g_t) = (d/dt) F_{Rφ}(t).
2. **Primitive from −∞.** The backward bound applied to Rφ gives F_{Rφ}(t) → 0 as t → −∞. So F_{Rφ}(t) = ∫_{−∞}^t F_φ.
3. **Iteration and bounds.** Iterate, using that R maps C^∞_0 to itself. The tame bounds of Lemma B (R7-d) bound ||R^Nφ||_∞.
4. **Vanishing along good sequences.** Let Q be a weak* limit of the bounded functionals φ ↦ ∫_{−∞}^{T_n} F_φ (bounded in (C^{m_1})'). By step 1 applied to ψ = Xφ, these functionals send Xφ to F_φ(T_n) → 0. So Q is invariant with Q(1) = 0, hence Q = 0 by DUE (O2). ∎

This is the time-domain form of Proposition 3.1 of R7-b (spectral flatness at frequency 0). It shows that the pair or disc transform T_z of Theorem V is flat to infinite order at z = 0 along the real axis from the right, with tame constants. To apply Theorem J or Lemma H one still needs quasi-analytic control of C_N (or of ||R^Nφ||) for a C^1-dense set of φ, and GH does not supply it.

## 3. Where every route stops (precise)

1. **Grid / configuration route (Theorems G, J, J\*).** This needs two-sided exact cancellation, i.e. a finite weak su-graph of good orbits with more edges than vertices. For non-hyperbolic μ, closing su-paths costs c − 1 ≥ 1 conditions in the centre directions. Nothing in GH produces such closures.
   - In the volume sub-class with a section (Prop. 2.1), the temporal defect disappears, but the centre defect remains.
2. **Spectral / tame-inverse route (Theorem V, Prop. 2.2).** GH gives, through the closed graph theorem, existence of tame constants (C_k, m_k), but no growth control on ||R^N φ||. Positive entropy (countable Lebesgue spectrum off the Pinsker factor) is compatible with infinite-order flatness at 0 for every individual smooth φ.
3. **Continuation route (Lemma M, Theorem B).** For generic orbits of non-hyperbolic μ, Proposition O shows there is no quasi-compact transfer operator, so no meromorphic continuation of single-orbit Laplace transforms across Re z = 0 is available.
4. **Reweighting route.** Moving λ = μ(d) off 0 is impossible:
   - time changes hX send λ to λ/μ(1/h);
   - density changes ν → e^{a}ν leave λ unchanged;
   - a shift J_t → J_t + ct would need a smooth w with Xw = c, which (K1) forbids.

**Open (unchanged):** (PE0). Under GH, exclude an ergodic, non-hyperbolic μ with h_μ(g_1) > 0 and μ(d) = 0. Without the normal-form citation, the large-|λ| case with multidimensional unstable (stable) bundles is also open. This includes the volume-preserving case, reduced in R7-d to statement (*) and, in the sub-class of Prop. 2.1, to a discrete-time GH diffeomorphism.

=== END OF ANSWER round8_q1 ===
