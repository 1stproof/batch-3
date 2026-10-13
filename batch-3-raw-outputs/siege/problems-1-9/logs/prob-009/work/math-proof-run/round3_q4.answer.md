# round3_q4: the Kobayashi-metric route. Result: no proof. The route stalls, and below I say exactly where.

## Interpretations adopted
As in context items 1, 5 and 6 of the task file. Y_t is holomorphic in t. All V_t share π_1 = G and the monodromy ρ: G → Mod(S_g). Lifts f_t: Ṽ_t → T_g are equivariant holomorphic embeddings.

## What is proved
**Lemma 1 (contraction).** Let k_X denote the Kobayashi distance. For all t and all x, y in Ṽ_t, d_T(f_t x, f_t y) ≤ k_{Ṽ_t}(x, y). Hence for every γ in G the translation lengths satisfy ℓ_{Ṽ_t}(γ) ≥ ℓ_T(ρ(γ)).
*Proof.* Holomorphic maps do not increase Kobayashi distance. By Royden's theorem (cited from memory), the Kobayashi distance of T_g is the Teichmüller distance d_T. Take the infimum over orbits. ∎

**Lemma 2 (t = 0).** Suppose V_0 is totally geodesic in the sense used here: through each point and each tangent direction, the Teichmüller disc lies in V_0. Then k_{Ṽ_0} = d_T restricted to Ṽ_0.
*Proof.* Let x, y be points of Ṽ_0. The Teichmüller geodesic from x to y lies in a Teichmüller disc D. The disc D is tangent to Ṽ_0 at x, so D ⊂ Ṽ_0. D is a holomorphic isometric disc, so k_{Ṽ_0}(x, y) ≤ k_D(x, y) = d_T(x, y). Lemma 1 gives the reverse inequality. ∎

Consequence: for γ with ρ(γ) pseudo-Anosov, ℓ_{Ṽ_t}(γ) ≥ ℓ_T(ρ(γ)) ≥ … with equality at t = 0 whenever the axis lies in Ṽ_0. So the Kobayashi length spectrum of V_t dominates that of V_0. (For a pseudo-Anosov arising from an affine automorphism inside the orbit closure, the axis is a Teichmüller geodesic in a disc contained in Ṽ_0.)

## Why the route stalls (precise)
(a) **Length spectra.** To turn "ℓ_{V_t} ≥ ℓ_{V_0}" into rigidity, we need a reverse inequality or an extremality principle for the intrinsic Kobayashi metric of 2-dimensional quasi-projective surfaces with fixed topology. Thurston's theorem ("ℓ_X ≥ ℓ_Y on all curves implies X = Y", cited from memory) relies on two facts:
- both metrics are complete hyperbolic of the same finite area (Gauss–Bonnet);
- the marked length spectrum is rigid.

Neither fact has a known analogue for the Kobayashi metric of a complex surface, which is a non-Hermitian Finsler metric. Restricting to curves does not help either:
- The Teichmüller curves inside V_0 do not persist in V_t for t ≠ 0. Nothing makes V_t contain any Teichmüller disc.
- The boundary curves ∂V_t = {Y_t} × C_t lie in Δ_Γ. There the Teichmüller metric degenerates (Minsky's product-region theorem, cited from memory). In the sup-metric on Teich(pieces) × horodiscs, moving Y_t only translates the curve in a factor where it is constant. So the length data of C_t do not detect Y_t at all; this is the metric version of context item 4.

(b) **Volume/extremality.** Kobayashi–Eisenman volumes, and integrals of the Teichmüller Finsler form, are not cohomological. Contraction bounds them by intrinsic quantities of V_t that vary with t. Characteristic numbers that are invariant (context 5) do not dominate these metric quantities with an equality case that characterizes totally geodesic embeddings. I know of no such Gauss–Bonnet/Toledo-type rigidity for Teichmüller space: Teichmüller space is not Hermitian symmetric, and its Kobayashi metric is not Kähler.

(c) **Boundary.** By (a), near Δ_Γ the metric is (up to bounded additive error) a product. Y_t sits in the factor Teich(S_i), and ∂V_t is constant in that factor. So every metric invariant built from the end of V_t near ∂V_t is insensitive to Y_t up to bounded error. Bounded error cannot pin a continuous parameter.

(d) **Conclusion.** The metric route proves only the one-sided inequality ℓ_{V_t} ≥ ℓ_{V_0}. There is no mechanism to force equality for t ≠ 0. Even equality would not obviously imply that V_t is totally geodesic.

## Missing lemma (single, explicit)
**Open:** If a holomorphic family V_t (t in Δ) is topologically trivial in the strong sense of context 5, with fixed monodromy ρ, and V_0 is totally geodesic, then V_t is totally geodesic (equivalently, by countability per Wright and Eskin–Mirzakhani–Mohammadi, V_t = V_0). Alternatively: V_0 is rigid as a subvariety, with the boundary behaviour fixed.

Granting this lemma, the claim follows by context 6. I have not proved it, and the Kobayashi metric does not appear sufficient to prove it. The claim as posed therefore remains open here.

=== END OF ANSWER round3_q4 ===
