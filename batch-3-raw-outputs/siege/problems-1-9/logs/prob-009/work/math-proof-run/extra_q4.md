# Task: a finiteness theorem for holomorphic maps into level covers of moduli spaces of pointed curves

This is a self-contained question in Teichmüller theory / complex geometry. It arises as one cited input in a long conditional argument about the problem stated after this text, but you do NOT need to solve that problem. Your only job is the statement below.

## Setting

- (h, m) with h ≥ 1, m ≥ 1, 2h − 2 + m > 0, and (h, m) ≠ (1, 1). T_{h,m} is the Teichmüller space of genus-h surfaces with m labelled punctures; PMod_{h,m} is the pure mapping class group (fixing each puncture).
- N ≥ 3. Mod_{h,m}[N] is the kernel of PMod_{h,m} → Sp(2h, ℤ/N) (action on H_1 of the closed surface with ℤ/N coefficients). It is torsion-free (Serre's lemma for h ≥ 2; for h = 1 a finite-order class acting trivially on H_1(·, ℤ/N), N ≥ 3, is trivial), normal and of finite index. So M_{h,m}[N] := T_{h,m}/Mod_{h,m}[N] is a complex manifold, a K(Mod_{h,m}[N], 1), and a finite unramified cover of the orbifold M_{h,m}.
- R is a Riemann surface of finite type (compact Riemann surface minus finitely many points).

## Statement to prove (call it (IS_marked))

For every free homotopy class 𝔥 of continuous maps R → M_{h,m}[N], the set of non-constant holomorphic maps R → M_{h,m}[N] lying in 𝔥 is finite.

A WEAKER statement is also sufficient for the application, and you may prove it instead if it is easier; say clearly which one you prove:
(IS_count) every such set is countable; or
(IS_rig) any two non-constant holomorphic maps R → M_{h,m}[N] in the same free homotopy class are equal (rigidity). [(IS_rig) implies (IS_marked) and (IS_count).]

## What is already known / allowed

- You may cite, with precise statements, standard published theorems: e.g. the Imayoshi–Shiga finiteness/rigidity theorem for holomorphic families of compact Riemann surfaces of genus ≥ 2 over a finite-type base (closed fibres); the Parshin–Arakelov theorem; Manin–Grauert (function-field Mordell); de Franchis–Imayoshi (finitely many non-constant holomorphic maps between finite-type Riemann surfaces with hyperbolic target); Royden's theorem (Teichmüller = Kobayashi metric); Bers embedding; Kobayashi hyperbolicity facts. State exactly which form you cite and whether you are confident it covers the case used. If you believe the Imayoshi–Shiga paper itself (MSRI Publ. 11, 1988) is stated for families of type (g, n), say so and say how confident you are — but please ALSO give an argument reducing to closed-surface statements, since the scope of that citation is exactly what is in doubt.
- The genus-0 targets M_{0,n} and the target M_{1,1}[N] are already handled (by an elementary Riemann–Hurwitz argument and by de Franchis respectively); you need not treat them, but you may use them.

## Suggested routes (use any, or your own)

1. Forgetful maps. For h ≥ 2, compose with M_{h,m}[N] → M_h[N] (forget punctures; on these level covers the forgetful map exists as a holomorphic map of manifolds — check this). If the composite is non-constant, closed-surface finiteness/rigidity pins it to finitely many maps; then the marked points give holomorphic "multisections" of a fixed non-isotrivial family over R minus..., handled by Manin–Grauert / Parshin-type finiteness of sections. If the composite is constant, the fibre is (essentially) a configuration space of a fixed hyperbolic curve, and de Franchis-type finiteness applies coordinatewise, with an "omitted values" argument for constant coordinates (as in the genus-0 case: a non-constant holomorphic map from R to a compact curve minus points extends to the compactification and omits only finitely many values).
2. Branched covers. Use a characteristic cover branched over the punctures to get a holomorphic map M_{h,m}[N'] → M_{h'}[N] (h' ≥ 2) whose lift T_{h,m} → T_{h'} is a holomorphic isometric embedding and which is finite-to-one onto its image; apply closed-surface finiteness and pull back finiteness (if two maps upstairs have the same image downstairs, they differ by a deck-type ambiguity from a finite group).
3. For h = 1, m ≥ 2: map to M_{1,1}[N] (forget all but one point); handle the non-constant and constant cases as in route 1, using that the fibre over a fixed elliptic curve E is a configuration space of E minus a point.

Be careful with: whether forgetful maps descend to the chosen level covers; constant-versus-nonconstant coordinates (a family of maps with one constant coordinate varying continuously is exactly what must be excluded); the difference between "homotopic" and "equal monodromy".

## Output

Write a complete proof (or a proof of (IS_count) / (IS_rig) instead), with every cited theorem stated precisely. If you cannot complete it, say exactly which case remains and why. Do not overclaim.
