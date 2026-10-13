kind: attempt
Open question attempted: MS4 (ledger entry 17), the problem's claim in reduced form. This is a statement-only attempt with a fresh first move.

## Statement
**Missing statement (MS4, entry 17, wording unchanged).** Let g ≥ 2. Let V_0 ⊂ M_g be a smooth 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric. Let 𝒱 ⊂ M_g × Δ be a complex submanifold with V_t = ψ(φ^{-1}(t)), satisfying hypotheses (i) and (ii) of the problem, and read as follows:
- (R1) closure(𝒱) ⊂ M̄_g × Δ is analytic, with fibre closure(V_t) over t;
- (R2) there is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G.

Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product boundary stratum. Suppose that for every t the set ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1 and π_i(∂V_t) = {Y_t} for one fixed index i. Then the holomorphic map Δ → M_{g_i,n_i}, t ↦ Y_t, is constant.

## The one prior result you may use (statement only)
**(Holomorphy.)** Under (R1) and (R2), t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}.

## Task
1. First derive for yourself that the statement, together with the holomorphy result, gives the problem's conclusion. If the derivation does not go through, or if the readings (R1)/(R2) misrepresent the hypotheses, say so precisely; that is a result.
2. Then attack the statement: prove it, or construct a counterexample. Your first move must be one that none of the earlier attempts used.

Earlier attempts (all failed to settle it) used these first moves:
- local plumbing coordinates near ∂V_t, and hypothesis (ii) along Γ;
- monodromy and limiting mixed Hodge structures, including Torelli for the vertex-i component;
- Arakelov-type equalities and Higgs-field maximality;
- infinitesimal rigidity H^0(N) = 0 and Douady-space arguments;
- the Kobayashi metric inequality d_T ≤ k_{V_t};
- incidence or pinning with other boundary curves, plus Möller-type rigidity of Teichmüller curves;
- Imayoshi–Shiga rigidity over a fixed base, reducing to constancy of the complex structure of V_t;
- counterexample searches by level sets inside covering loci and by symmetric deformations.

What is already known not to work:
- No argument local to ∂V_t can work: any holomorphic arc Y_t is compatible with every local constraint of (i) and (ii).
- Topological data (monodromy, weight filtrations, intersection numbers) are blind to Y_t.

Examples of first moves NOT yet tried, as suggestions only:
- harmonic-map or energy methods (equivariant harmonic maps to Teichmüller space with the Weil–Petersson metric, Siu/Sampson-type Bochner formulas on V_t);
- the GL(2,R)-action and SL(2,R)-equivariant measure rigidity applied to limits as t → 0;
- algebraic or arithmetic arguments (fields of definition, Galois action on the countable set of totally geodesic subvarieties and their boundary data);
- a volume or characteristic-number identity tying closure(V_t) to the boundary data;
- a degeneration or bubbling argument for t → ∂Δ.

A proof for only some V_0 or some strata does not answer the question; report it labelled as partial if that is all you find.
