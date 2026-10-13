# round3_q2: the Arakelov-equality transport route

**Status: not resolved.** This file does not prove the claim. It does three things: it states the infinitesimal "maximality" at t = 0 precisely, it explains why the natural global Arakelov equality is very likely false for V_0, and it names the single missing lemma that would finish the proof.

## Interpretations adopted
These are the same as context items 1, 5 and 6 of the task file:
- closure(𝒱) is analytic in M̄_g × Δ.
- Smooth triviality together with (i) and (ii) gives a stratified homeomorphism closure(V_0) × Δ ≅ closure(𝒱) over Δ.
- Consequently the monodromy ρ: π_1(V_t) → Sp(2g,Z) is independent of t, up to conjugation.

## (a) Infinitesimal structure at t = 0 (sketch; relies on Wright and Filip, cited from memory)
- Let M be the orbit closure over V_0, with dim_C M = 4, rank 2, rel 0.
- At a point (X, ω) we have T_{(X,ω)} M ≅ W_X = E_X ⊕ \bar E_X, with dim_C E_X = 2.
- The fibre of P(M) → V_0 is P(E_X). This gives T_X V_0 ≅ W_X/(E_X) ≅ \bar E_X, where the identification depends on [ω].
- In Higgs-field terms, θ: T_X V_0 ⊗ E_X → \bar E_X satisfies the following.
  - **(M)** For every nonzero ω ∈ E_X, the map μ ↦ θ(μ)ω is an isomorphism T_X V_0 → \bar E_X.
  - The Teichmüller direction \bar ω/ω is sent to \bar ω.

Property (M) is the "directional maximality" condition. It is pointwise and open, but not closed. It is not a numerical condition.

## (b) Dead end: the global Arakelov equality
Möller–Viehweg–Zuo (cited from memory) treat weight-one VHS over log surfaces. In their setting, Arakelov equality for the whole W forces the period map V_0 → A_2-type locally symmetric space to be totally geodesic for the Bergman/Siegel metrics. That would make the universal cover of V_0 a bounded symmetric domain with the Kobayashi = Teichmüller metric.

This contradicts the theorem, recalled from memory, that Teichmüller discs and totally geodesic Teichmüller submanifolds are not Kobayashi-isometric to symmetric domains (Antonakoudis). So the natural numerical equality very likely fails for V_0: the inequality is strict.

The extremality of V_0 is only directional, namely (M). The constancy of integer Chern numbers (context item 5) therefore transports nothing that characterizes total geodesicity.

## (c) Substitute considered and why it fails
One could restrict to the Teichmüller curves C ⊂ V_0, which are probably dense (from memory). Each such C has a rank-2 sub-VHS with Arakelov equality, and its Euler number is topological. However:
- Nothing forces C to deform to a curve in V_t.
- The hypotheses constrain only the boundary of V_t, not interior curves.

So this route is also blocked.

## Missing lemma (stated exactly)
**Lemma (open).** Let (closure(V_t), D_t) be a smoothly trivial family as in the problem. Suppose W persists as a flat sub-local system of R^1 over every V_t, and suppose V_0 satisfies (M). Then V_t satisfies (M) for all t. Equivalently, there exist a numerical or closed algebraic invariant of (V_t, W) that is constant in t and whose extremal value characterizes (M).

If this lemma holds, the claim follows:
1. Condition (M) at every point makes every Teichmüller disc tangent to V_t lie in V_t, i.e. V_t is totally geodesic.
2. Totally geodesic subvarieties are countable (Wright plus Eskin–Mirzakhani–Mohammadi, from memory), so the continuous family V_t is constant.
3. Hence Y_t = Y_0 (context items 1 and 6).

## What is proved
Only the reduction: (missing lemma) ⇒ claim, with step 1 above sketched and not proved in detail. The claim itself remains **open** here. Open questions:
1. Is the global Arakelov inequality for W over V_0 strict? This is expected (point (b)), but not proved.
2. Is there a closed numerical characterization of (M)?
3. Does V_0 admit any nontrivial deformation V_t at all? (Rigidity would settle the claim.)

=== END OF ANSWER round3_q2 ===
