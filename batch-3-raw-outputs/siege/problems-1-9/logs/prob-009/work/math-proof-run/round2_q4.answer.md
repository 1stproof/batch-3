# round2_q4: attempting to refute the claim

## Result
I found no rigorous counterexample and no proof. What follows is what can be stated precisely.

## 1. A reduction (proved, assuming Context items 1–2)
t ↦ Y_t is holomorphic (Context 1). So the claim fails exactly when there is a family with dY_t/dt ≠ 0 at some t. By Context 2–3, hypothesis (ii) puts no condition on Y_t: the closure of {Y_t} × C_t in deeper strata is {Y_t} × closure(C_t), and that holds for any Y_t. Hypothesis (i) only asks that ∂V_t = {Y_t} × C_t be a smoothly trivial family, and a holomorphically moving Y_t satisfies this. So **(i) and (ii) cannot rule out a moving Y_t by themselves.** Any proof must use one of the following:
- (a) the global geometry of the compact surface closure(V_t) in M̄_g, or
- (b) the totally geodesic structure of V_0, carried over to V_t by some rigidity.

The hypotheses on V_t for t ≠ 0 do not supply (b).

## 2. What a counterexample needs (precise)
1. A smooth totally geodesic surface V_0 with a boundary curve {Y_0} × C_0 in a product stratum, where the factor M_{g_i,n_i} has positive dimension.
2. A holomorphic deformation of closure(V_0) inside M̄_g (a deformation of the compact analytic surface, for example a section of the normal sheaf that integrates) whose normal component at that boundary curve has a nonzero projection to T_{Y_0} M_{g_i,n_i}.
3. The deformation must keep the stratification of the boundary combinatorially constant, so that (i) and (ii) hold.

Note on the covering-construction surfaces (images of M_{0,5} or M_{1,2}): for M_{0,5}, the boundary curves D_{ij} ≅ M̄_{0,4} split off a 3-pointed P^1. After lifting, the constant factor is a Belyi cover with 3 branch points. Such a cover has **no moduli** (it is a point of a 0-dimensional Hurwitz space). So Y_0 is rigid among covers. That does not stop a deformation of V_t that is no longer a covering locus from moving Y_t: by Context 4, nothing local prevents it. Whether a global deformation exists is decided by H^0 and H^1 of the normal sheaf of closure(V_0) in M̄_g (a stack/orbifold). I could not compute these.

A local model shows the mechanism a counterexample would use, in M_{0,6} rather than M_g. With marked points 0, 1, ∞, a, b, c, take surfaces of the form {c = λ_t a}. As a → 0, the points 0, a, c bubble off onto a component with 4 special points, and its cross-ratio is set by λ_t. So that factor varies with t. I did not verify that any member of this family is totally geodesic, or that it lifts to M_g. This is a heuristic, not a counterexample.

## 3. Proved special case
If every V_t is totally geodesic, the claim holds. Totally geodesic subvarieties form a countable set (cited from memory: Wright's correspondence between totally geodesic subvarieties and GL(2,R)-orbit closures, together with Eskin–Mirzakhani–Mohammadi). Then t ↦ V_t is a continuous map into a countable set, so it is constant, and Y_t ≡ Y_0. The same argument works under the weaker condition that Y_t lies in a countable set, for example Belyi-type curves defined over Q̄. Indeed, a holomorphic map into M_{g_i,n_i} whose values lie in a countable set is constant.

## 4. Open: the single missing lemma
**Lemma needed:** for a smooth totally geodesic surface V_0, every holomorphic, stratum-compatible deformation of closure(V_0) in M̄_g keeps fixed every constant boundary factor Y_0.

Equivalently: the normal-sheaf sections of closure(V_0) project to zero in T_{Y_0} M_{g_i,n_i} along the curve {Y_0} × C_0. I could not prove or refute this. I see no reason for it to follow from (i) and (ii); the claim as posed may need an extra hypothesis, for example that Y_t is defined over Q̄ or that the V_t are totally geodesic.

=== END OF ANSWER round2_q4 ===
