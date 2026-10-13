# Answer to round10_q10: the missing statement (JC)

## Outcome
(JC) is **not proved** here, and I found no counterexample. Below are one small proved reduction lemma and an account of where the argument stops. I did not separately check the chain steps 1-3 (Theorem R', Theorem A). I have no new evidence for or against them.

## Notation
As in the brief: P = X + d acts on C^inf(M). A chain at c is written, in generalized-function form, as u = B/nu and v = A/nu with
Xu = -c u, Xv = -c v - u, u != 0.
I write kappa = Re c.

## Lemma 1 (proved). Continuity of the kernel at one point rules out every eigen-distribution there
Let c be a complex number with Re c != 0. Assume that every distribution u with (X + c)u = 0 is a continuous function. Then the only such u is u = 0. In particular c carries no eigen-density (B∘P = cB forces B = 0), and so a fortiori no Jordan chain of any order.

*Proof.*
1. Let u be continuous with (X + c)u = 0 in D'.
2. Fix a smooth density ρ and set F(t) = ∫ (u∘g_t) ρ = <u, (g_t)_*ρ>.
   - The map t -> (g_t)_*ρ is smooth into smooth densities, with derivative -L_X((g_t)_*ρ).
   - Hence F'(t) = -<u, L_X (g_t)_*ρ> = <Xu, (g_t)_*ρ> = -c F(t), using the definition <Xu, σ> = -<u, L_X σ>.
   - So F(t) = e^{-ct}F(0). Since this holds for every ρ, we get u∘g_t = e^{-ct}u as continuous functions, hence pointwise.
3. So |u(g_t x)| = e^{-κt}|u(x)|. If κ > 0, let t -> -inf; if κ < 0, let t -> +inf. In either case, u(x) != 0 would make the continuous function u unbounded on the compact manifold M. Hence u ≡ 0. ∎

*Consequence (reduction, proved).* (JC) and (NJ) would follow from the following statement:
(GH_c) For c with Re c != 0 (one c per strip suffices), the kernel of X + c on D' consists of continuous functions.

*Remark.* Lemma 1 explains why GH at c ≠ 0 must fail at some points. The tilted conformal measures of Proposition 2.2 (R4-q7) give nonzero measure solutions of Xu = -μ(d)u. So (GH_c) can only hold off a set containing {μ(d) : μ ergodic, μ(d) ≠ 0}. Whether that set can fill a whole strip is exactly the content of (JC).

## Where the argument stops
1. **No perturbation from 0.** The only quantitative form of GH is the tame estimate ||u||_{C^k} ≤ C||Xu||_{C^m}, with m > k in general.
   - On mean-zero functions, X^{-1} is continuous on C^inf, but it is not bounded on any fixed Banach space C^k.
   - So the Neumann series X + c = X(1 + cX^{-1}) does not converge for any c ≠ 0, however small.
   - Nash-Moser-type schemes need tame estimates for the perturbed operator, and those are what we are trying to prove.
   - This matches the brief's observation that GH acts only at the spectral point 0.
2. **Log trick.** For a smooth chain, w = v/u satisfies Xw = -1 on {u ≠ 0}. This would contradict (K1) if w were a global distribution. For measure-valued u, v the quotient is undefined.
   - Regularising (u_ε = u*ρ_ε) destroys the eigen-relation by commutator terms [X, ρ_ε*] of size O(1) in C^0. At order 1 they are of size O(ε^{-1}).
   - So the trick does not survive mollification without further structure.
3. **Spectral route under an invariant volume.** This route is not available, because (V) is itself open. Under (V), GH gives f = X^k u_k with u_k smooth for every mean-zero smooth f. So every smooth f has an L^2 spectral measure vanishing to infinite order at λ = 0, in the integrated sense ∫ dσ_f/λ^{2k} < inf.
   - Positive entropy gives countable Lebesgue spectrum on L^2 ⊖ L^2(Pinsker).
   - These two facts are not contradictory as they stand: vectors whose spectral density vanishes to infinite order at 0 are dense in a Lebesgue-spectrum space.
   - A contradiction would need a smooth f whose projection off the Pinsker algebra has spectral density not flat at 0, i.e. a nonzero Green-Kubo variance. I could not produce one without hyperbolic periodic data (Livšic), and periodic orbits need not exist.

## Status
- **Proved:** Lemma 1 and the reduction "(GH_c) at one c per strip ⇒ (NJ) on that strip ⇒ (JC)".
- **Open:** (JC); (NJ); (GH_c) for any c with Re c ≠ 0; (SO); (V). Through the chain, the problem's claim of zero topological entropy for GH flows is also still open.
- I know of no proof in the literature, citing from memory. The Greenfield-Wallach/Katok conjecture would imply the claim. As far as I recall it is proved only in low dimensions or under extra hypotheses (Forni; Kocsard; Rodriguez Hertz-Rodriguez Hertz on cohomology-free flows). I cannot reconstruct those hypotheses reliably.

=== END OF ANSWER round10_q10 ===
