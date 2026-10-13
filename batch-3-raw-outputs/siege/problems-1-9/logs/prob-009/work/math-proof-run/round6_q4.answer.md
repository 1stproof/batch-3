# round6_q4 — attempt to refute MS5

## Plan / status line
Candidate counterexample: the Picard family V_0 = {y^3 = (x-a_1)(x-a_2)(x-a_3)(x-a_4)(x-a_5)^2} ⊂ M_3.
This is a Z/3 covering construction over M_{0,5}, and every branch point is totally ramified.
Claim: MS5, exactly as stated (with "product type" required), FAILS for this V_0. The reason is that the only
product-type stratum meeting closure(V_0) in a curve is Γ itself, and for G = Γ, clause (a) fails at u = i.
All merges of vertex i happen in a stratum whose dual graph has three parallel edges, and that stratum is not of product type.
Caveat: whether V_0 is smooth (in the orbifold sense) at finitely many special curves (Section 5).

## 1. The surface V_0 and the hypotheses
Write k = (k_1,...,k_5) = (1,1,1,1,2). Then Σk = 6 ≡ 0 mod 3, so ∞ is not a branch point.
- **The map Φ.** Let Φ : M_{0,5} → M_3 send (P^1; a_1,…,a_5) to the curve X : y^3 = ∏(x-a_j)^{k_j}.
  - X → P^1 is cyclic of degree 3 and totally ramified over each a_j, since gcd(3,k_j) = 1.
  - Riemann–Hurwitz gives 2g-2 = 3(-2) + 5·2 = 4, so g = 3.
  - These are the Picard curves: put a_5 = ∞ to get y^3 = quartic.
- **Totally geodesic (standard; cited from memory).**
  - Let q be an integrable quadratic differential on (P^1; a_1..a_5). It has at most simple poles at the a_j.
  - f^*q is holomorphic on X: at a totally ramified point (e = 3) the order is 3·(-1) + 2·2 = 1 ≥ 0.
  - So Teichmüller maps lift to Teichmüller maps with the same K. By Teichmüller's uniqueness theorem the lifts are extremal.
  - Hence the lift T_{0,5} → T_3 is a holomorphic isometric embedding.
  - The infinitesimal extremal Beltrami differential in a direction tangent to V_0 is f^*(k|q|/q) = k|f^*q|/f^*q, which is of Teichmüller form. So the Teichmüller disc tangent to any direction of V_0 is the pulled-back disc, and it lies in V_0.
- **Closure.**
  - The Z/3 admissible cover over a stable 5-pointed tree is unique. Over each component the cover is determined by the local monodromies, because a hom π_1 → Z/3 factors through H_1. At an unbranched node, the equivariant gluings differ by deck transformations, and on a tree these can be absorbed.
  - Hence Φ extends to a continuous Φ̄ : M̄_{0,5} → M̄_3, which sends a stable curve to the stabilised source (Harris–Mumford / Abramovich–Corti–Vistoli; cited from memory).
  - closure(V_0) = Φ̄(M̄_{0,5}) and closure(V_0) \ V_0 = Φ̄(∂M̄_{0,5}).
- **Local rules for the boundary computations.**
  - Monodromy at a node, seen from the side carrying a set S of marked points: m = -Σ_{j∈S} k_j mod 3.
  - If m ≠ 0, there is one totally ramified source node.
  - If m = 0, there are three unramified source nodes, permuted by the deck group.
  - A Z/3 cover of a sphere branched at three points, all with nonzero monodromy, is the curve E_ω, where j(E_ω) = 0.
  - A cover branched at two points is P^1.
  - Preimages of the a_j are unmarked. Here they never need contracting, as the checks below show.

## 2. The boundary of closure(V_0), divisor by divisor
**(A) D_{jk} with j,k ≤ 4.** The bubble is A = {a_j, a_k, q}, and the node monodromy is 1 on the A side.
- Over A the cover is E_ω, with one node at a fixed point of the order-3 automorphism σ.
- The other side carries a_l, a_m (k = 1), a_5 (k = 2) and q (monodromy 2). The cover there has 4 total branch points, so it is a genus-2 curve Z with one node point.
- The source curve is E_ω ∪_1 Z, in the stratum Δ_Γ ≅ M_{1,1} × M_{2,1}.
- Γ has two vertices of different genus and one edge. It has no automorphisms, so the gluing map is bijective and Γ is of product type.
- π_1 is constantly Y_0 := (E_ω, p) ∈ M_{1,1}, and dim M_{1,1} = 1 > 0.
- π_2 is the covering construction M_{0,4} → M_{2,1}. It is isometric on Teichmüller spaces, hence non-constant.
- So ∂V_0 = closure(V_0) ∩ Δ_Γ = Φ̄(∪ D_{jk}°) is 1-dimensional and constant on factor 1. **The problem's setting holds**, with i the genus-1 vertex.

**(B) D_{j5}, j ≤ 4.** The node monodromy is -(1+2) ≡ 0, so the node is unbranched.
- Over {a_j, a_5, q} the cover is P^1, with 3 node points and no other special points. This is a rigid M_{0,3} vertex.
- Over the other side, branched at three points with k = 1, the cover is E_ω. It carries the 3 node points {x, σx, σ²x}, which form a σ-orbit that moves with q.
- The source curve is E_ω ∪_3 P^1, of genus 1 + 0 + 2 = 3. Its stratum is Δ_{G''}, where G'' has two vertices (g = 1 with 3 half-edges, g = 0 with 3 half-edges) and three parallel edges.
- The gluing map M_{1,3} × M_{0,3} → Δ_{G''} is generically 6-to-1, because relabelling the three edges simultaneously on both sides does not change the curve. **So G'' is not of product type.**

**(C) Corners.** The 15 points D ∩ D′ map to single points. Examples:
- Φ̄(D_{12} ∩ D_{34}) is the chain E_ω – E_ω – E_ω. The middle component has 2 special points, and all three nodes are branched.
- Φ̄(D_{12} ∩ D_{35}) is E_ω –_1 P_B ≡_3 P_C.
  - P_B is the cover branched at the q_1-node and at a_4. It has 4 special points: one node over q_1 and three over q_2.
  - P_C is the cover branched at a_3 and a_5, with three nodes.
  - All components are rigid.
- The other corners have one of these two types, up to the S_4 symmetry of a_1..a_4.

**Conclusion of Section 2.**
- The 1-dimensional irreducible components of closure(V_0) ∩ Δ_G, over all strata G, are exactly the images of the open divisors.
- They lie in Δ_Γ (type A) and in Δ_{G''} (type B).
- Δ_G = M_3 contributes only V_0, which is 2-dimensional.

## 3. Theorem: MS5 fails for this V_0
**Theorem.** No product-type stratum Δ_G and point P_0 satisfy the requirements of MS5.

*Proof.*
1. MS5 requires P_0 ∈ closure(E^{(a)}) \ E^{(a)} for some 1-dimensional component E^{(a)} of closure(V_0) ∩ Δ_G with G of product type. By Section 2, the only such G is Γ.
2. Take G = Γ, any admissible P_0, and any a with P_0 ∈ closure(E^{(a)}). Such an a exists by hypothesis.
3. E^{(a)} ⊂ ∂V_0 ⊂ {Y_0} × M_{2,1}. So 𝐂^{(a)} = closure(ξ_Γ^{-1}(E^{(a)})) ⊂ {Y_0} × M̄_{2,1}.
4. ξ_Γ is proper, so ξ_Γ(𝐂^{(a)}) = closure(E^{(a)}) ∋ P_0. Hence some R ∈ 𝐂^{(a)} has ξ̄_Γ(R) = P_0.
5. For u = i, the curve R_i = Y_0 is smooth and its only component is Y_0. So R_u ∉ ∂M̄_u, and clause (a) fails.
6. So every candidate (G, P_0) fails. ∎

The argument uses neither (O), nor the twin issue, nor positive area. It realises a variant of failure mode 1: merges do exist, but only in non-product strata. In those strata vertex i merges across an *unbranched* node, whose three preimages the deck group permutes, so the dual graph acquires the S_3 symmetry of parallel edges.

## 4. What does hold: MS5′ with finite-quotient strata allowed
Let **MS5′** be MS5 with "product type" weakened to: ξ_G : ∏ M_w → Δ_G finite, with all objects taken on lifts. The lifts 𝐂^{(a)} and R are already formulated this way in MS5, and π_u is used only on lifts.

**Claim.** MS5′ holds for the Picard V_0 with G = G'' and P_0 = Φ̄(D_{12} ∩ D_{35}).

*Proof.*
1. **P_0 is admissible.**
   - P_0 lies in closure(Φ̄(D_{12}°)) ⊂ closure(∂V_0).
   - P_0 lies in closure(E) \ E for E = Φ̄(D_{35}°) ⊂ Δ_{G''}.
   - By S_4 symmetry, all Φ̄(D_{l5}°) have the same image curve {E_ω ∪_3 P^1 with σ-orbit nodes}. So E is the only component of closure(V_0) ∩ Δ_{G''}, and it contains every branch of closure(V_0) ∩ Δ_{G''} through P_0.
2. **The lifts R over P_0.**
   - R_{w0} ∈ M_{0,3} has no genus-1 component.
   - R_{w1} is the limit in M̄_{1,3} of (E_ω; x, σx, σ²x) as a_1 → a_2, where q_2 effectively tends to a_4.
   - This limit is E_ω ∪_1 P_B, with the 3 marked points on P_B in some order. The fixed-point node of E_ω has 1 special point, so the E_ω component is ≅ Y_0. It is the only genus-1 component, so there is no twin.
   - R_{w1} ∈ ∂M̄_{1,3}, so **(a) holds**.
3. **(b) holds.**
   - π_{w1}(E) is the image of the marked covering construction M_{0,4} → M_{1,3}, sending (P^1; a,b,c,q) to (y^3 = cubic, with the three preimages of q marked).
   - The pullback T_{0,4} → T_{1,3} is a holomorphic isometric embedding. f^*q is holomorphic at the totally ramified points, and has simple poles only at the marked preimages of q, which is allowed.
   - It is equivariant for the lift of the liftable subgroup of Mod_{0,4}. This gives the Teichmüller-curve property.
   - I have not written out the orbifold bookkeeping in full: Ẽ is a finite quotient of M_{0,4} by the S_3 that permutes a_1, a_2, a_4.

So in this example the obstruction is precisely the product-type restriction. I have not verified whether Theorem P and Lemma R(*) of the chain survive when G is a non-product stratum.
- Their arguments are phrased via lifts R ∈ ∏ M̄_w, with K_u := pr_u(𝐂^{(a)}), which suggests they do.
- But Lemma R′s Step 1 (components of E_t, and ν_t) and Theorem P′s use of π_w on Δ_G would have to be redone on ξ_G^{-1}.
- **Recommendation:** replace "product type" in MS5 / (T0) by "the gluing map is finite", and re-check Theorem P with lifts.

## 5. Caveat: smoothness of V_0
- V_0 is the image of a component of Fix(σ) ⊂ T_3, where σ is the Picard automorphism. Fix(σ) is a smooth complex submanifold, by linearisation of a finite-order holomorphic map.
- V_0 is orbifold-smooth at a point X as long as all Picard automorphism subgroups of X coincide with ⟨σ⟩, that is, as long as ⟨σ⟩ is normal in Aut(X) up to the relevant conjugates.
- **Recollection (unverified):** the curve y^3 = x^4 + 1 has Aut of order 48, with signature (2,3,12) containing the C_12-signature (3,4,12). If so, ⟨σ⟩ is not normal there.
  - If it were normal, Aut/C_3, of order 16, would act on P^1 preserving the 5 branch points. But the orbits of the dihedral group of order 16 on P^1 have sizes 2, 8 and 16, so no orbit union has 5 points.
  - Then the Picard locus has several smooth branches through that point. These branches are distinct, because generic Picard curves have Aut = C_3.
- So, read literally, the Picard surface may fail the hypothesis "V_0 smooth" at finitely many points. If the problem's smoothness is strict, the example is not admissible and the refutation is conditional.
- Even so, the mechanism is purely a boundary phenomenon. Interior smoothness plays no role in Sections 2–4. So any proof of MS5 would have to use interior smoothness in an essential way to exclude it, which seems implausible. I do not have a verified strictly smooth example.

## 6. Summary
- **Proved, modulo the cited standard facts:** for the Picard surface, MS5 as stated (product-type G) is false. The problem's setting holds with Γ = (genus 1) – (genus 2) and Y_0 = E_ω.
- **Sketched:** MS5′ (non-product strata allowed) holds for this example.
- **Open:**
  - whether the Picard locus is orbifold-smooth; a strictly smooth counterexample;
  - whether Theorem P and Lemma R extend to non-product G;
  - MS5′ in general.

=== END OF ANSWER round6_q4 ===
