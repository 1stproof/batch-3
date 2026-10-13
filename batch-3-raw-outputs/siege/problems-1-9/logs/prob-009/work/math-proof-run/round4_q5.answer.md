# round4_q5 — answer

Plan: (1) derive problem conclusion from MS4; (2) new first move: rigidity of homotopic holomorphic maps from a FIXED base (Imayoshi–Shiga), giving a rigorous reduction of MS4 to a statement about the complex structure of V_t only ("base rigidity"); (3) conditional sub-class; (4) a dead end (naive counterexample by level sets) and why it dies.

## 1. MS4 implies the problem's conclusion

MS4 says t -> Y_t is constant on the (connected) disc Δ, hence Y_t = Y_0, i.e. π_i(∂V_t) = {Y_0} for all t. That is exactly the conclusion. Two remarks on readings:
- The problem says "for some i"; a priori i could depend on t. There are finitely many indices, and for each i the set of t with π_i(∂V_t) a point is closed (under R1/R2, by continuity of ∂V_t in t), so by Baire some index works on an open set; MS4 as formulated (one fixed i) therefore loses nothing on an open subset of t, but to cover all t one must either assume a fixed i (as MS4 does) or argue separately. Taking i fixed is the natural reading of the problem ("that factor").
- (R1) (closure analytic, fibres are closures) and (R2) (stratified trivialization) are reasonable readings of "holomorphic family of subvarieties" + (i) + "smoothly trivial". By Chow/Remmert–Stein, closure(V_t) is algebraic in the projective coarse space M̄_g, so V_t is an irreducible quasi-projective surface, closed in M_g. I use only this below.

## 2. New first move: Imayoshi–Shiga rigidity with a fixed base

### Cited result (from memory)
**Lemma A (Imayoshi–Shiga 1988, rigidity half of their finiteness theorem; also follows from Daskalopoulos–Wentworth harmonic-map uniqueness).** Let R be a Riemann surface of finite type, R~ its universal cover, ρ: π_1(R) -> Mod_g a homomorphism. If F_0, F_1: R~ -> T_g are holomorphic, ρ-equivariant, and F_0 is non-constant, then F_0 = F_1.
(Equivalently: a non-isotrivial holomorphic family of genus-g curves over R is determined up to isomorphism by its monodromy.) Remark: if R = C or C*, every holomorphic R~ -> T_g is constant (T_g is a bounded domain), so non-constant F_0 forces R hyperbolic; nothing extra is needed.

### Setting (to avoid orbifold problems)
Fix m >= 3, let M_g[m] be the level-m moduli space (smooth, quasi-projective, T_g -> M_g[m] an unramified Galois covering since Mod_g[m] is torsion-free and acts freely), and q: M_g[m] -> M_g the finite quotient map. Let V_0' be an irreducible component of q^{-1}(V_0). (Working in M_g directly fails: V_0 may lie in the branch locus of T_g -> M_g — e.g. covering-construction surfaces consist of curves with automorphisms — and a holomorphic map into the coarse space need not lift.)

### Proposition B (proved, modulo Lemma A)
Suppose there is a continuous map Φ: V_0' × Δ -> M_g[m] such that
 (a) for each t, Φ(·,t) is holomorphic on V_0' (on its smooth locus; continuity elsewhere suffices),
 (b) Φ(·,0) is the inclusion V_0' ⊂ M_g[m],
 (c) q(Φ(V_0' × {t})) ⊂ V_t for all t.
Then V_t = V_0 for all t; in particular ∂V_t = ∂V_0 and Y_t = Y_0.
(No use is made of total geodesicity, nor of (i),(ii).)

**Proof.** Fix t ∈ Δ and x ∈ V_0'. Since V_0' is an irreducible quasi-projective surface (finite over the quasi-projective V_0), there is an irreducible algebraic curve through x in V_0' (e.g. a hyperplane section through x). Let ν: R -> V_0' be its normalization composed with inclusion; R is a compact Riemann surface minus finitely many points, so of finite type, and ν(R) ∋ x.
Let H = Φ∘(ν × id): R × Δ -> M_g[m]; it is continuous. R~ × Δ is simply connected and locally path connected and T_g -> M_g[m] is a covering, so H∘(cover × id) lifts to a continuous H~: R~ × Δ -> T_g. For γ ∈ π_1(R) and each s, z -> H~(γz, s) and H~(z,s) are lifts of the same map, so H~(γz,s) = ρ_s(γ) H~(z,s) for a unique ρ_s(γ) ∈ Mod_g[m] (deck group). Since s -> ρ_s(γ) is locally constant (deck group discrete, H~ continuous, action properly discontinuous and free) and Δ is connected, ρ_s = ρ is independent of s. Put F_s = H~(·, s): each F_s is holomorphic (local inverse of a holomorphic covering composed with the holomorphic Φ(·,s)∘ν) and ρ-equivariant. F_0 is non-constant because its projection is ν, which maps R onto a curve. By Lemma A, F_t = F_0, hence Φ(ν(r), t) = ν(r) for all r ∈ R; in particular Φ(x,t) = x.
As x was arbitrary, Φ(·,t) is the inclusion, so by (c) V_0 = q(V_0') ⊂ V_t. Both are irreducible closed 2-dimensional analytic subsets of M_g (V_t is the image of a connected 2-dimensional manifold, closed by the reading of §1), so V_0 = V_t. ∎

### Consequence: precise reduction
**MS4 (indeed the stronger V_t ≡ V_0) follows from the "base-rigidity" statement**
> (BR) For some m >= 3 and some component V_0' of q^{-1}(V_0), there is a continuous family Φ as in Prop. B, i.e. the surfaces V_t' (components of q^{-1}(V_t) continuing V_0') receive holomorphic maps from the fixed complex surface V_0', continuous in t, starting at the identity.
For instance (BR) holds if the component 𝒱' of (q × id)^{-1}(𝒱) through V_0' is, over Δ, holomorphically (even just fibrewise-holomorphically and continuously) trivial, V_0' × Δ ≅ 𝒱'.

So the entire content of MS4 is about whether the *complex structure* of the abstract surfaces V_t can move. Equivalently, by Prop. B: **in any counterexample to MS4 (indeed in any non-constant family V_t), the complex structure of V_t' must vary in t, in the sense that no continuous family of holomorphic maps V_0' -> V_t' starting at the identity exists.** In particular the map data (monodromy, homotopy class), which entry 8 shows are constant, can never be the obstruction; total geodesicity of V_0 can only enter through the complex-analytic rigidity of the base V_0.

Strictly simpler statement left open (no map to M_g involved beyond the fixed monodromy):
> (BR') Let V_0 ⊂ M_g be a totally geodesic surface. Any family of complex surfaces V_t' as above (images of the fixed-monodromy family, with the stratified topological triviality R2) is holomorphically trivial over Δ.

## 3. Conditional sub-class (sketch, NOT proved)
If the normalization of closure(V_0') admits a log-smooth compactification (X̄, D) with H^1(X̄, T_X̄(-log D)) = 0, and the closures closure(V_t') form a locally trivial deformation of the pair (X̄, D) (this is what (i),(ii),(R2) suggest but do not literally give: one needs a flat analytic family of compactifications resolving the boundary simultaneously), then by Kodaira–Spencer the deformation of pairs is trivial over a neighbourhood of 0, giving (BR) near t = 0, hence V_t = V_0 near 0 and, by the identity principle applied to the analytic set {t : V_t = V_0} (closed by R1, open by the same argument at every t0 for which the vanishing holds for V_{t0} = V_0), for all t.
Unproved steps: (1) existence of a simultaneous log resolution in the family; (2) the vanishing H^1(T(-log D)) = 0 for any actual totally geodesic surface. For covering-construction surfaces V_0 (finite orbifold covers of M_{0,5}, M_{1,2}) one expects (2) from log-rigidity of M̄_{0,5} (I recall from memory that M̄_{0,n} with its boundary is log-rigid, but did not verify it for the finite covers). This is reported as a conditional, sub-class statement only.

## 4. Dead end: naive counterexamples by level sets
Attempt: take W = image of a covering construction T_{0,6} -> T_g, let V_0 be the (totally geodesic) locus of 6-point configurations symmetric under an involution σ pairing (1,2),(3,4),(5,6). On the cover of M_{0,6} on which the fixed points of σ_{12,34} are ordered, in the coordinate z with σ(z) = -z, p_1 = 1, p_3 = b, p_5 = c, p_6 = d, one has V_0 = {d = -c} and the level sets V_λ = {d = -λ c}.
Why it dies: for λ ≠ ±1, V_λ = {(b,c) : c ∉ {0,∞,±1,±b,±1/λ,±b/λ}} while V_0 = {(b,c): c ∉ {0,∞,±1,±b}}: the fibres acquire four extra punctures (p_6 colliding with p_1,...,p_4), i.e. closure(V_λ) meets boundary strata that closure(V_0) does not meet in that way. This violates (i)/(R2). (Using the symmetric function λ + 1/λ on M_{0,6} itself instead gives a double cover of V_0, not a deformation.) This is the general mechanism: deformations obtained by moving a divisor inside a larger subvariety change the boundary combinatorics, which the hypotheses forbid. It does not rule out counterexamples, but any counterexample must, by §2, be a family in which the complex structure of the base varies while all topological/boundary data stay fixed.

## Summary of status
- Proved: MS4 => problem conclusion (with fixed i). Prop. B: any family of holomorphic maps from the fixed base V_0' (level cover) into M_g[m], continuous in t, starting at the inclusion, is constant; hence MS4 (in the strong form V_t = V_0) follows from base rigidity (BR). Proof is rigorous modulo the cited Imayoshi–Shiga rigidity (Lemma A, from memory).
- Sketched/conditional: (BR) for V_0 with log-rigid compactification, assuming a locally trivial family of log compactifications.
- Open: (BR') — whether the complex structure of V_t can vary under the hypotheses; hence MS4 itself remains open. Neither proved nor disproved; no counterexample found.

=== END OF ANSWER round4_q5 ===
