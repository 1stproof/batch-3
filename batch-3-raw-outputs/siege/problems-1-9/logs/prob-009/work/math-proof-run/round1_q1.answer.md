# round1_q1 — attempt (partial; no complete proof)

## Interpretation
- t -> Y_t is a map Δ -> M_{g_i,n_i}. It is continuous by (i): the family ∂V_t is smoothly trivial. It is holomorphic because ∂V_t is the fibre over t of the complex-analytic set closure(𝒱) ∩ (Δ_Γ × Δ), and π_i is constant on each fibre.
- Hypothesis (ii) only compares closures of boundary pieces in deeper strata Δ_{G'}, within open sets U.

## What is proved
**Lemma 1 (the deeper boundary does not pin Y_t).** Write ∂V_t = {Y_t} × C_t, where C_t is a curve in the other factors. Every point of the closure of ∂V_t in a deeper stratum Δ_{G'} comes from degenerating C_t, or from bubbling inside the remaining factors. So that point still has the component Y_t at the i-th vertex, or a stable curve obtained by degenerating Y_t if the limit also lands in the closure of M_{g_i,n_i}. If we apply (ii) only to the pair (Δ_Γ, Δ_{G'}), it says that these deeper points of V_t arise as limits of ∂V_t. That holds tautologically for every t, whatever Y_t is. So (ii) applied to Γ and its degenerations gives no constraint on Y_t.

*Proof.* The statement is local in a product chart of closure(M_{g_i,n_i}) × (the other factors). The closure of a product set is the product of the closures. ∎

**Consequence.** Any proof must bring in boundary pieces of V_0 in strata Δ_G that **contain** Δ_Γ in their closure (less degenerate strata). It must use the total geodesicity of V_0 to show that Y_0 is cut out by conditions there that are rigid under deformation. Hypotheses (i) and (ii) then transport those conditions to V_t.

## Proposed route (not completed)
1. By Wright (cited from memory: totally geodesic subvarieties of M_g of dimension ≥ 2 are projections of GL(2,R)-orbit closures of quadratic differentials whose rank equals the dimension), V_0 = p(M), where M has rank 2.
2. By Mirzakhani–Wright / Chen–Wright (from memory: the boundary of an orbit closure in the WYSIWYG partial compactification is a finite union of orbit closures of lower rank), the limit differential on the Y_0 component must vanish. Otherwise the boundary orbit closure would move Y_0 in Teichmüller directions, contradicting the fact that ∂V_0 is constant in the i-th factor.
3. Missing step: show that "the multi-scale limit of M has a zero top-level part on the Y_0 component" forces Y_0 to be an isolated solution of algebraic conditions. These conditions would be lower-level residue/GRC conditions in the BCGGM sense, together with linear equations of M on lower levels. They would also have to be expressible purely through the incidence of closures of boundary strata of V_0, so that (i) and (ii) carry them over to V_t.

## Missing lemma (precise statement)
**Lemma X (open).** Suppose V_0 is totally geodesic of dimension 2, and the curve ∂V_0 ⊂ Δ_Γ is constant (= Y_0) in the factor M_{g_i,n_i}. Then there are a stratum Δ_G, with Δ_Γ in the closure of Δ_G, and an open set U meeting Δ_Γ, such that
- the closure of closure(V_0) ∩ Δ_G, intersected with Δ_Γ ∩ U, equals closure(V_0) ∩ Δ_Γ ∩ U; and
- for any curve D ⊂ Δ_G which is a smooth deformation of closure(V_0) ∩ Δ_G, the boundary of D in Δ_Γ can only be constant in factor i if that constant is Y_0.

If Lemma X holds, the claim follows: apply (i) and (ii) to the pair (Δ_G, Δ_Γ) and to D = closure(V_t) ∩ Δ_G.

I could not prove Lemma X. I also could not rule out a counterexample: hypotheses (i) and (ii) are purely topological and incidence-theoretic, and V_t is not assumed totally geodesic for t ≠ 0. So the claim as posed may need an extra hypothesis, for example that V_t is totally geodesic for all t. If we assume that extra hypothesis, then by rigidity of orbit closures (they are defined over Q-bar, by Eskin–Filip–Wright, cited from memory) the family V_t is locally constant. In that case Y_t = Y_0 immediately.

## Status
- Proved: Lemma 1 (a reduction); and the claim under the extra hypothesis that every V_t is totally geodesic, assuming the cited Eskin–Filip–Wright result.
- Open: Lemma X, and therefore the claim as posed.

=== END OF ANSWER round1_q1 ===
