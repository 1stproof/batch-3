# round6_q6 — answer (attempt at MS5)

## 0. Plan and current status (written first; updated at the end)

Plan.
1. Lemma 1: show that in MS5 the stratum G can never be Γ itself (nor any stratum along whose pieces the Y_0-vertex stays an unmerged constant factor). So MS5 implies that closure(V_0) has a 1-dimensional boundary piece outside Δ_Γ whose closure meets closure(∂V_0).
2. Example: the totally geodesic surface V_0 ⊂ M_6 of cyclic 5-fold covers y^5 = ∏_{j=1}^5 (x − a_j). All of its boundary curves coincide with ∂V_0 ⊂ Δ_Γ, Δ_Γ = M_{2,1} × M_{4,1}, and the first factor is constant. So MS5 fails for it. Caveat: this V_0 is not smooth, so it violates one hypothesis of MS5.
3. Show that in this example the problem's conclusion still holds, by another mechanism: a "twin" copy of Y_t sits inside a cusp of the rigid Teichmüller factor.
4. Say what this means for the chain (Theorem P with (T0) = MS5) and for the multi-scale approach of the task. Propose a corrected statement MS5* that covers both mechanisms, and prove that MS5* + (O) still gives the problem's conclusion.

Status: see Section 6 at the end.

## 1. Lemma 1: G = Γ never works in MS5

**Lemma 1.** Let Δ_G be a product-type stratum, E a 1-dimensional irreducible component of closure(V_0) ∩ Δ_G, and P_0 ∈ closure(E) \ E. Suppose some vertex u of G has π_u(E) = {Z}, a single point, where Z ∈ M_u is (after relabelling its marked points) isomorphic to Y_0. Then there is R ∈ 𝐂 := closure of ξ_G^{-1}(E) with ξ̄_G(R) = P_0 and R_u = Z ∈ M_u. So clause (a) of MS5 fails for (G, P_0, E, R, u).

In particular, MS5 can never hold with G = Γ: every 1-dimensional component of closure(V_0) ∩ Δ_Γ lies in ∂V_0, where π_i ≡ Y_0.

*Proof.*
1. ξ_G is a bijection ∏_w M_w → Δ_G, and π_u = pr_u ∘ ξ_G^{-1} on Δ_G. So every point of ξ_G^{-1}(E) has u-coordinate Z.
2. Take x_n ∈ E with x_n → P_0. The points ξ_G^{-1}(x_n) lie in the compact space ∏_w M̄_w. A subsequence converges to some R, and R ∈ 𝐂.
3. ξ̄_G is continuous, so ξ̄_G(R) = lim x_n = P_0.
4. The u-coordinate is constant equal to Z along the sequence, so R_u = Z. This is a smooth curve with a component (itself) isomorphic to Y_0, but R_u ∉ ∂M̄_u. ∎

**Corollary 1.** If MS5 holds, then closure(V_0) has a 1-dimensional boundary piece E ⊂ Δ_G with G ≠ Γ and closure(E) ∩ closure(∂V_0) ⊄ E. Along E, no vertex is constant with value isomorphic to Y_0.

So MS5 contains an existence statement, namely that boundary curves of closure(V_0) other than ∂V_0 exist and touch closure(∂V_0). Section 2 shows that this existence statement can fail for a totally geodesic surface.

## 2. Example: the surface of cyclic quintic covers in M_6 (MS5 fails; V_0 is not smooth)

### 2.1 Construction
- For distinct a = (a_1, …, a_5) on P^1, let X_a be the smooth projective model of y^5 = ∏_{j=1}^5 (x − a_j), with the obvious change if some a_j = ∞.
- X_a → P^1 is a Z/5-cover, totally ramified over a_1, …, a_5 with local monodromy 1 ∈ Z/5 at each, and unbranched elsewhere. The degree of the polynomial is 5 ≡ 0 mod 5, so ∞ is unbranched.
- Riemann–Hurwitz gives 2g − 2 = 5·(−2) + 5·4 = 10, so g = 6.
- This defines Φ : M_{0,5} → M_6, invariant under S_5 because all five monodromies are equal. Put V_0 := Φ(M_{0,5}).

### 2.2 V_0 is totally geodesic and 2-dimensional (standard; cited from memory)
- Let q be an integrable quadratic differential on (P^1; a_1, …, a_5), so it has at most simple poles at the a_j. Its pullback f^*q has order e(−1 + 2) − 2 = 3 ≥ 0 at each ramification point (e = 5). So f^*q is a holomorphic quadratic differential on X_a.
- The Teichmüller map of the base with initial differential q lifts to an affine map for f^*q, which is a Teichmüller map upstairs. Hence the lifting map T_{0,5} → T_6 is a holomorphic isometric embedding (classical).
- Every tangent direction of T_{0,5} at a point is the Teichmüller direction of a unique (up to positive scaling) q. The Teichmüller disc of T_6 in the image direction is the disc of f^*q, which is the image of the disc of q. So every Teichmüller disc tangent to V_0 lies in V_0.
- Φ is finite-to-one: X_a has finitely many automorphism subgroups, and the quotient by one of them recovers the unordered branch set. So dim V_0 = 2.

### 2.3 Boundary (admissible covers; Harris–Mumford, cited from memory)
- An abelian cover has a unique admissible cover over each stable 5-pointed tree. This gives a continuous extension Φ̄ : M̄_{0,5} → M̄_6, sending a stable tree to the stabilized admissible cover.
- Then closure(V_0) = Φ̄(M̄_{0,5}), since the image is compact and contains V_0 as a dense subset.
- Boundary points go to nodal curves (computed below), so Φ̄^{-1}(M_6) = M_{0,5}. Hence V_0 is closed in M_6.
- **Local monodromies.** On every component of an admissible cover, the local monodromies at the special points sum to 0 in Z/5. Here every local monodromy is nonzero, hence a generator. So each component cover is connected and totally ramified over every special point.

**Over D_{ab}° (base A ∪ B, with A ∋ a_a, a_b and B ∋ the other three points):**
- Over A the monodromies are (1, 1, 3). Riemann–Hurwitz gives 2g − 2 = −10 + 12, so g = 2, with one point over the node.
- Over B they are (1, 1, 1, 2), so 2g − 2 = −10 + 16 and g = 4, again with one point over the node.
- The stable curve is a genus-2 curve and a genus-4 curve glued at one point. Its dual graph Γ has vertices of genus 2 and 4 joined by one edge, and Δ_Γ = M_{2,1} × M_{4,1}. This is of product type: the gluing map is bijective onto Δ_Γ because the two vertices have different genera.
- The genus-2 component is the Z/5-cover of a 3-pointed sphere with monodromy (1, 1, 3), marked at the point over the third point. It is the same pointed curve Y_0 ∈ M_{2,1} for every (a, b) and every point of D_{ab}°, namely y^5 = x(x − 1) marked over x = ∞. So π_1 ≡ Y_0.
- The genus-4 component is the covering construction with data (1, 1, 1, 2) over the 4-pointed sphere B, marked over the node. Let C ⊂ M_{4,1} be its image as B runs over M_{0,4}. The map M_{0,4} → C is finite-to-one by the argument of 2.2, so dim C = 1.
- Hence Φ̄(D_{ab}°) = {Y_0} × C for all ten pairs (a, b).

**Over the 15 points D_{ab} ∩ D_{cd} (base chain A(a_a, a_b) — B(a_m) — C(a_c, a_d)):**
- The monodromies are (1, 1, 3) on A, (2, 1, 2) on B and (3, 1, 1) on C.
- The covers over A and C are both Y_0. The cover over B has genus 2 (2g − 2 = −10 + 12) and two points over the nodes; call this 2-pointed curve B_0.
- So all 15 points map to one stable curve P_0 = Y_0 — B_0 — Y_0, a chain of three genus-2 curves. Its dual graph is G' (path with 3 vertices).

**Conclusion.**
- closure(V_0) \ V_0 = ({Y_0} × C) ⊔ {P_0}.
- ∂V_0 = closure(V_0) ∩ Δ_Γ = {Y_0} × C is irreducible, because it is the image of the irreducible D_{12}°. It has dimension 1, and π_1(∂V_0) = {Y_0} with dim M_{2,1} = 4 > 0.
- closure(∂V_0) = ∂V_0 ⊔ {P_0}.

### 2.4 MS5 fails for this V_0
- The strata meeting closure(V_0) are M_6, Δ_Γ and Δ_{G'}.
  - closure(V_0) ∩ M_6 = V_0 is irreducible of dimension 2, so it has no 1-dimensional components.
  - closure(V_0) ∩ Δ_{G'} = {P_0}.
  - Hence the only 1-dimensional piece in any stratum is E = ∂V_0 ⊂ Δ_Γ.
- So the only candidate in MS5 is G = Γ, E = ∂V_0, P_0 the point above. Lemma 1 (u = genus-2 vertex) shows that clause (a) fails there. Concretely, the lift R = (Y_0, B_0 ∪ Y_0) ∈ {Y_0} × closure(C) has R_1 = Y_0 smooth.
- **All hypotheses of MS5 hold except smoothness:** g = 6 ≥ 2; V_0 is closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; dim ∂V_0 = 1; π_1(∂V_0) = {Y_0} with dim M_{2,1} > 0.

### 2.5 Caveat: this V_0 is not smooth (sketch)
- **Fermat point, orbifold sense.** The Fermat quintic F : x^5 + y^5 + z^5 = 0 has genus 6 and lies in V_0 in three ways. The quotients by z ↦ ζz, by y ↦ ζy and by x ↦ ζx are each P^1, totally branched over 5 points.
  - In a Teichmüller chart at a lift of F, the preimage of V_0 therefore contains the three fixed loci Fix(H_x), Fix(H_y), Fix(H_z) of these order-5 subgroups. Each is a smooth 2-dimensional germ.
  - They are distinct germs. If two coincided, the generic X_a would carry a second Z/5 acting nontrivially on X_a/H ≅ P^1 and preserving the branch set, and a generic 5-point configuration has no nontrivial symmetry.
  - So V_0 is not a smooth sub-orbifold at F.
- **The point c_4 = {0, ±1, ±i}, coarse sense.** Its stabilizer in PGL_2 is Z/4, generated by z ↦ iz. (0 is the only point lying on no harmonic 4-subset, so it is fixed. The symmetries of the square fixing 0 are the rotations.)
  - The induced action on T_{c_4} M_{0,5} has eigenvalues (i, −1). Compute T = (⊕_j T_{p_j} P^1)/sl_2 with characters {i, 1, i, −1, −i} − {i, 1, −i}.
  - So the coarse germ of M_{0,5}/S_5 there is C^2/(Z/4) with weights (1, 2). This is an A_1 singularity, since the group is not generated by reflections.
  - I expect the coarse germ of V_0 at Φ(c_4) to be this quotient. This needs the generic automorphism group of X_a to be exactly Z/5, which I have not checked.

So the example is a counterexample to **MS5 with the smoothness hypothesis removed**, not to MS5 as stated. Smoothness of V_0 is an interior condition, while everything in MS5 concerns the boundary. I see no way smoothness could create the missing boundary curves of Corollary 1. But I have not found a smooth example in which they are missing.

## 3. In the example the problem's conclusion still holds: the twin mechanism

**Proposition 3.** Let V_0 be the surface of Section 2. Let V_t be a family as in the problem, with readings (R1), (R2), and with ∂V_t := closure(V_t) ∩ Δ_Γ 1-dimensional and π_1(∂V_t) = {Y_t}. Assume condition (O) of PR-E for the piece E_0 = ∂V_0 and the genus-4 vertex. Then Y_t = Y_0 for all t ∈ Δ.

(Smoothness of V_0 plays no role in the argument.)

*Proof.*

**Step 0 (rigid factor).**
- π_2 : ∂V_0 = {Y_0} × C → C is a bijection, and C is the covering-construction curve from M_{0,4}.
- The lift T_{0,4} → T_{4,1} is a holomorphic isometric embedding. It is equivariant for the subgroup of Mod_{0,4} that preserves the monodromy data. So hypothesis (H_0) of PR-E holds: π_2(∂V_0) is a Teichmüller curve in the orbifold sense. Its normalization is the quotient of the disc by the stabilizer of the Teichmüller disc (standard).
- By Lemma R\* (PR-E, under (O)), K := closure(π_2(∂V_t)) = closure(C) ⊂ M̄_{4,1} for every t.
- K is an irreducible compact curve meeting M_{4,1}, so K_∂ := K ∩ ∂M̄_{4,1} is finite.
- Let F ⊂ M_{2,1} be the finite set of 1-pointed curves that occur as a smooth component of a point of K_∂, marked at one of its special points.

**Step 1 (the transported cusp).**
- Put P_t := H_t(P_0). Since H_t preserves strata, closure(V_t) ∩ Δ_{G'} = {P_t}, closure(V_t) \ V_t = ∂V_t ⊔ {P_t}, and P_t ∈ closure(∂V_t).
- So P_t is a chain A_t — B_t — C_t of genus-2 curves. A_t and C_t each carry one node point, and B_t carries two.

**Step 2 (local chart).**
- Let Def(P_t) be the versal deformation germ of P_t, a smooth germ of dimension 15 on which Aut(P_t) acts. The germ of M̄_6 at P_t is Def(P_t)/Aut(P_t).
- Let s_1, s_2 be the smoothing parameters of the nodes A–B and B–C. The locus {s_1 = 0 ≠ s_2} maps to Δ_Γ, with genus-2 vertex the deformation of A_t. The locus {s_2 = 0 ≠ s_1} also maps to Δ_Γ, with genus-2 vertex the deformation of C_t. The locus {s_1 = s_2 = 0} maps to Δ_{G'}.
- Let S̃ ⊂ Def(P_t) be the preimage of the germ of closure(V_t). It is analytic by (R1), since a fibre of an analytic set is analytic. It is of pure dimension 2, since V_t is a dense 2-dimensional manifold in closure(V_t) and the quotient map is finite.
- Moreover S̃ ∩ {s_1 s_2 = 0} is the preimage of ∂V_t ∪ {P_t}, and S̃ ∩ {s_1 = s_2 = 0} = {0}.

**Step 3 (A_t ≅ Y_t).**
- Since P_t ∈ closure(∂V_t), S̃ ∩ {s_1 s_2 = 0} has a branch β̃ through 0.
- β̃ \ {0} is connected and lies in the disjoint union of the relatively open sets {s_1 = 0 ≠ s_2} and {s_2 = 0 ≠ s_1}. Renaming A ↔ C if needed, β̃ \ {0} ⊂ {s_1 = 0 ≠ s_2}.
- Points of β̃ \ {0} lie over ∂V_t, so their genus-2 component (the A-side one) is Y_t. That component depends continuously on the point of the chart, and its value at 0 is A_t. Hence A_t ≅ Y_t as 1-pointed curves.

**Step 4 (the second branch; Lemma C1 of PR-C).**
- Let X_S be an irreducible component of S̃ containing β̃. The function s_2 is not identically 0 on X_S, because it is nonzero on β̃ \ {0}, and s_2(0) = 0.
- So {s_2 = 0} ∩ X_S is of pure dimension 1 through 0. It does not contain β̃, so it contains a branch b̃ ≠ β̃ with b̃ \ {0} ⊂ {s_2 = 0 ≠ s_1}, using S̃ ∩ {s_1 = s_2 = 0} = {0}.
- Points of b̃ \ {0} lie over closure(V_t) ∩ Δ_Γ = ∂V_t, so their genus-2 component, now the C-side one, is Y_t. Letting the point tend to 0 gives C_t ≅ Y_t.

**Step 5 (pinning).**
- Along β̃, π_2 takes values in π_2(∂V_t) ⊂ K: the genus-4 curve obtained by smoothing B ∪ C.
- Its limit at 0 is W_t := B_t ∪ C_t, glued at the B–C node and marked at the point of B_t over the A–B node. So W_t ∈ K ∩ ∂M̄_{4,1} = K_∂.
- C_t is a smooth component of W_t, marked at its special point, so C_t ∈ F. By Step 4, Y_t ∈ F for every t ∈ Δ.
- t ↦ Y_t is continuous (PR-A) and takes values in a finite set, so it is constant on the connected set Δ. ∎

**Remarks.**
1. Lemma 1 shows that the lift R = (Y_t, W_t) has an *unmerged* copy of Y_t at vertex 1, so Theorem P's (T0-a) fails. The pinning instead comes from a *second* copy (twin) C_t of Y_t, which sits inside the boundary point W_t of the *rigid* Teichmüller factor at the other vertex. Step 4 forces this twin to exist at every t: it is the local analytic Lemma C1 combined with the fact that no other boundary curves exist near P_t.
2. Proposition 3 needs neither t small nor hypothesis (ii) beyond (R2). It uses the totally geodesic structure of V_0 only through Step 0.

## 4. General consequences: a dichotomy, a pinning lemma, and a twin criterion

Throughout this section assume (R1), (R2) and the problem's hypotheses. Write P_t := H_t(P_0).

**Lemma D (merge or twin).** Fix t. Let P ∈ closure(∂V_t) \ ∂V_t lie in Δ_{G'}. Let S̃ be the preimage of the germ of closure(V_t) in the versal deformation germ Def(P), and let s_e (e ∈ E(G')) be the smoothing parameters. For a boundary branch c̃ of S̃ through 0, let S_c ⊂ E(G') be the set of edges with s_e ≡ 0 on c̃. Let β̃ be a branch lying over ∂V_t. Then:
1. The edges of G' not in S_β are contracted by the induced contraction c_β : G' → Γ. Its preimage c_β^{-1}(i) is a single vertex j with no loops and no contracted edges, and the component P_j is isomorphic to Y_t.
2. Let b̃ be another boundary branch with the merge property, i.e. some edge f of G' at j has f ∉ S_b. Then exactly one of the following holds.
   - **(D1) Merge.** b̃ lies over a 1-dimensional piece E of closure(V_t) ∩ Δ_{G_b} with G_b ≠ Γ. Then π_v(E) is non-constant, where v is the vertex of G_b containing j (Lemma C2 of PR-C).
   - **(D2) Twin.** b̃ lies over ∂V_t. Then c_b^{-1}(i) is a single loop-free vertex j' ≠ j, and P_{j'} ≅ Y_t. So P has a second component isomorphic to Y_t.

*Proof.*
1. Along β̃ \ {0}, the i-coordinate is the constant smooth curve Y_t. Its limit at 0 is the stable curve assembled from the components P_k, k ∈ c_β^{-1}(i), glued along the edges of G' contracted into i.
   - This limit is the smooth curve Y_t. So the assembled curve has no node, which means c_β^{-1}(i) is one vertex j with no contracted edges or loops, and P_j ≅ Y_t.
2. The coarse image of b̃ \ {0} lies in a single stratum, by connectedness. If that stratum is not Δ_Γ we are in (D1).
   - Otherwise b̃ lies over closure(V_t) ∩ Δ_Γ = ∂V_t. Part 1, applied to b̃, gives the single loop-free vertex j' = c_b^{-1}(i) with P_{j'} ≅ Y_t.
   - The edge f at j is contracted by c_b (f ∉ S_b). So the vertex c_b(j) contains a contracted edge, hence c_b(j) ≠ i, i.e. j ≠ j'. ∎

**Lemma (Pinning).** Let 𝒰 be a finite set of pairs (E_0, u). Here E_0 is a 1-dimensional component of closure(V_0) ∩ Δ_{G}, G product type, u is a vertex of G, π_u(E_0) is a Teichmüller curve in the orbifold sense, and condition (O) of PR-E holds for (E_0, u). Put E_t := H_t(E_0). Suppose:

**(Pin)** For every t in a disc around 0 there is (E_0, u) ∈ 𝒰 such that Y_t is isomorphic, after relabelling, to a smooth component of a point of closure(π_u(E_t)) ∩ ∂M̄_u.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. By Lemma R\* (PR-E), closure(π_u(E_t)) = closure(π_u(E_0)) =: K_u for all t. Each K_u ∩ ∂M̄_u is finite.
2. So Y_t lies in a fixed finite set for t in the disc. By continuity (PR-A) it is constant there.
3. By holomorphy (PR-A) and the identity theorem, Y_t = Y_0 on Δ. ∎

The step-3 argument of Theorem P shows that **(T0) ⇒ (Pin)**. Proposition 3 shows that **(Pin) holds in the example of Section 2**, where (T0) fails. The following criterion abstracts Proposition 3. Like (T0), it is a condition on V_0 alone.

**Theorem 4 (twin criterion).** Let P_0 ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G'}. Let 𝒞 be the set of edge sets S ⊂ E(G') such that contracting E(G') \ S gives a graph identified with Γ, by an identification compatible with ξ_Γ, in which the preimage of vertex i is a single loop-free vertex j(S). Assume:
- **(Tw1)** There is a neighbourhood U of P_0 with (closure(V_0) \ V_0) ∩ U ⊂ ∂V_0 ∪ {P_0}.
- **(Tw2)** For all S ≠ S' in 𝒞:
  - j(S) ≠ j(S');
  - the vertex w = w(S, S') of Γ that contains j(S') under the contraction by S has an edge of G' among the edges contracted into it;
  - for every component E_0 of ∂V_0 with P_0 ∈ closure(E_0), π_w(E_0) is a Teichmüller curve in the orbifold sense satisfying (O).

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Transport.** By (R2), H_t maps closure(V_0) ∩ U onto a neighbourhood of P_t in closure(V_t), preserving strata. So near P_t, closure(V_t) \ V_t ⊂ ∂V_t ∪ {P_t}, and in Def(P_t) we have S̃ ∩ {all s_e = 0, e ∈ E(G')} = {0}.
   - G' and its combinatorics are the same at P_t as at P_0, because the stratum is preserved. The set 𝒞 depends only on G' and Γ.
2. **The branch β̃.** Take a branch β̃ of the preimage of ∂V_t through 0. By Lemma D(1), S_β ∈ 𝒞, and P_t has the component Y_t at j := j(S_β).
   - S_β ≠ E(G'), since P_t ∉ Δ_Γ.
3. **The branch b̃.** Pick e ∉ S_β. Lemma C1 of PR-C, as in Step 4 of Proposition 3, gives a boundary branch b̃ ≠ β̃ through 0 with e ∈ S_b.
   - By Step 1, b̃ lies over ∂V_t. So S_b ∈ 𝒞 by Lemma D(1), S_b ≠ S_β, and P_t has the component Y_t at j' := j(S_b) ≠ j, by (Tw2).
4. **The good vertex.** Let E_t = H_t(E_0) be the component of ∂V_t containing the image of β̃, so P_0 ∈ closure(E_0). Let w = w(S_β, S_b).
   - Along β̃ the w-coordinate converges to the stable curve assembled from the components of P_t over w, which include P_{j'} ≅ Y_t.
   - That curve has a node, by (Tw2). So it lies in closure(π_w(E_t)) ∩ ∂M̄_w, and Y_t is one of its smooth components.
5. **Conclusion.** This is (Pin) with 𝒰 the finite set of pairs (E_0, w) allowed by (Tw2), and it holds for every t. The Pinning Lemma concludes. ∎

**Check against Section 2.**
- G' is the chain A — e_1 — B — e_2 — C, and 𝒞 = {{e_1}, {e_2}} with j({e_1}) = A and j({e_2}) = C.
- w({e_1}, {e_2}) is the genus-4 vertex, which contains the edge e_2. Symmetrically, w({e_2}, {e_1}) contains e_1.
- π_2(∂V_0) = C is a Teichmüller curve. (Tw1) holds because closure(V_0) \ V_0 = ∂V_0 ⊔ {P_0}.
- So Proposition 3 is the case (Tw) of Theorem 4, modulo (O).

**What this means for MS5 and the chain.**
- MS5 (= (T0)) is not the right missing statement. It is false without smoothness (Section 2), and the problem's conclusion survives there via (Tw).
- The correct target is **(Pin)**, or the V_0-only disjunction **"(T0) or (Tw) holds at some point P_0 of closure(∂V_0)"**. Both are still open in general.
- Lemma D explains why a disjunction is natural. At a cusp, Lemma C1 always produces a second boundary branch b̃. If b̃ has the merge property, it is either a genuinely new boundary curve (D1, the (T0) mechanism) or ∂V_t again with a twin (D2, the (Tw) mechanism).
- What neither mechanism covers:
  - a cusp where no branch b̃ merges vertex j and no twin arises: the non-merge case of PR-C, still open;
  - (D1)-branches whose merged vertex is not a Teichmüller curve: positive area not established, (PA) of PR-F;
  - (D2)-twins whose host vertex w is not a Teichmüller curve or carries no node.

## 5. Why the multi-scale approach of the task cannot prove MS5 as stated

The approach was:
1. pass to the closure of P𝓜 in the multi-scale space;
2. find a codimension-2 point over closure(∂V_0) where a second boundary divisor meets one over ∂V_0;
3. argue that along the second divisor the level of the Y_0-component merges with the top level, and get (b) from Lemma T′.

**Where it breaks.**
- Let p : closure(P𝓜) → closure(V_0) be the forgetful map. It is proper, so every boundary divisor of closure(P𝓜) maps onto an irreducible closed subset of closure(V_0) \ V_0.
- In the example of Section 2 that set is ∂V_0 ⊔ {P_0}. So every boundary divisor maps onto closure(∂V_0) or to the point P_0.
- Hence any "second divisor" at a codimension-2 point maps either to the point P_0, which gives no curve E at all, or again into ∂V_0.
- Even if the Y_0-level merges on the multi-scale side along that divisor, its image in M̄_g is a branch of type (D2) of Lemma D: the curve ∂V_0 again, approached through the other contraction, with the twin component C ≅ Y_0 now playing the role of the constant vertex.
- For the original branch β, the lift R = (Y_0, W) still has Y_0 unmerged at vertex i. So (a) fails for it, by Lemma 1.
- Thus the implication "merge at a codimension-2 multi-scale point ⇒ MS5" is false. Step 4's requirement that "every lift R and every twin of Y_0 is covered" cannot be met in general.
- These conclusions use only properness of p and the explicit boundary of Section 2. I did not need, and did not carry out, the level-graph computations for the quadratic stratum Q(3^5, 1^5) of this example.
- (The pullback differentials f^*q have zeros of order 3 at the five ramification points and five simple zeros, so this 𝓜 is a quadratic orbit closure; the double-cover step of the approach would be needed.)

**What the approach can still deliver.** By Lemma D, a merge branch at a cusp yields either (D1), the (T0) mechanism, or (D2), the (Tw) mechanism. A multi-scale proof of the disjunction "(T0) or (Tw)" would need three things:
1. a merge branch at some cusp (open; PR-C);
2. in case (D1), positive area on the merged vertex, so that Lemma T′ applies (open; (PA) of PR-F);
3. in case (D2), that the twin's host vertex w carries positive area at some point of ∂V_0 (then Lemma T′ gives the Teichmüller property) and contains a node at P_0.

I have not proved any of these in general.

## 6. Summary: proved, sketched, open

**Proved (modulo results cited from memory, flagged where used):**
- **Lemma 1.** MS5 can never hold with G = Γ, or along any piece on which a vertex is constant with value isomorphic to Y_0. So MS5 forces the existence of boundary curves of closure(V_0) outside Δ_Γ that touch closure(∂V_0).
- **Section 2.** For the totally geodesic surface V_0 ⊂ M_6 of cyclic quintic covers y^5 = ∏_{j=1}^5 (x − a_j):
  - closure(V_0) \ V_0 = ({Y_0} × C) ⊔ {P_0}, inside Δ_Γ = M_{2,1} × M_{4,1} and the point stratum of the chain Y_0 — B_0 — Y_0;
  - every hypothesis of MS5 except smoothness holds;
  - MS5 fails.
  - The boundary computation uses admissible covers (Harris–Mumford, cited); total geodesy is the classical covering-construction argument (cited).
- **Proposition 3.** In that example the problem's conclusion Y_t = Y_0 holds anyway, given (R1), (R2) and (O) for the genus-4 factor. The proof is a twin mechanism: Lemma C1 at P_t forces a second copy of Y_t inside a boundary point of the rigid Teichmüller factor.
- **Lemma D** (merge-or-twin dichotomy at a cusp), the **Pinning Lemma**, and **Theorem 4**: the twin criterion (Tw) implies the problem's conclusion, in the same way that Theorem P derives it from (T0).

**Sketched only:**
- Non-smoothness of the example's V_0 (§2.5): orbifold self-intersection at the Fermat quintic, and an A_1 coarse singularity at the {0, ±1, ±i} configuration. The latter assumes the generic automorphism group is exactly Z/5.
- Consequently, whether MS5 *with* the smoothness hypothesis is false is not settled.

**Verdict on MS5.** As stated it is not provable by any boundary argument that ignores smoothness, and I believe it is the wrong missing statement. The chain should replace (T0) by (Pin), or by the V_0-only disjunction "(T0) or (Tw) at some P_0 ∈ closure(∂V_0)".

**Open questions:**
1. Is there a *smooth* totally geodesic surface V_0 for which every 1-dimensional boundary piece meeting closure(∂V_0) lies in Δ_Γ? That would refute MS5 as stated.
2. Does every V_0 as in the problem satisfy (Pin)? Concretely, does it satisfy (T0) or (Tw) at some point of closure(∂V_0)? This needs:
   - (C-merge) of PR-C;
   - (PA) of PR-F;
   - a treatment of cusps where neither merging nor twinning occurs;
   - the case where closure(∂V_0) has no cusps, i.e. ∂V_0 is compact in Δ_Γ.
3. Condition (O) of PR-E, which is used in all pinning arguments here. It is a separate open input of the chain.
4. A rigorous check of the singularities of the example (generic automorphism group, coarse versus orbifold smoothness).

=== END OF ANSWER round6_q6 ===

