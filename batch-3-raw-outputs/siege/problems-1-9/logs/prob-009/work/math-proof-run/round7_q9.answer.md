# round7_q9: checking the chain lemmas L1, L2 and the derivation from MS6

## 0. Verdict (summary)

- **L1 holds for product-type strata G**, with the proof sketched in the task once two details are filled in (§1). These are the boundary points in the 0-fibre, and the rank argument, which is redone with the Cartan–Remmert semicontinuity of fibre dimension.
- **L1 as stated is not justified for non-product strata G, and can fail as phrased.** The irreducible lifted family W can have a 0-fibre consisting of several Aut(G)-translates σE_0 of a piece. A vertex u can be constant on E_0 and non-constant on σE_0, and then it is non-constant on W_t. The correct statement is L1′ (§1.3): if u is non-constant on a piece at time t lying in W_t, then u is non-constant on *some* piece at time 0 lying in W_0. L1′ is proved for all G.
- **L2 has a genuine gap even for product strata.** Hypothesis (O) is about the vertex v only, so it gives θ_t and the compatibility ρ^v_t = ρ^v_0∘θ_t only for v. The claim "g_t is orbifold-homotopic to g_0" for another vertex u needs the same transport for u. Call this **(O_u)**, or assume **(O_G)**, which is (O) for the full map to ∏_w M_w with group ∏_w Mod_w. The continuous family coming from (R2) does not give it: a homotopy in the coarse space M_u carries no orbifold-monodromy information. With (O_G) added, L2 is proved (§2), product case.
- **Non-product case of L2.** The "transport E_0 → E_t" upstairs need not exist, because of the splitting in §1.3. A downstairs replacement L2′ is given in §2.6 as a sketch. It works on the normalization of the image curve in Δ_G, with an (O_G)-type hypothesis for maps into ∏T_w with group Mod_G.
- **The chain** (MS6 + L1 + L2 + (O) + Lemma T′ ⟹ claim) is correct for product strata once (O) is strengthened to (O_G), or (O) is assumed for every vertex u that is non-constant on the piece. For non-product G, L1 must be replaced by L1′ and L2 by L2′. Steps 1 and 3 are fine. Step 4 must be rephrased: "E_t is the transport of some piece E_0" is false in general for non-product G. §3 checks each step.

## 1. L1

Notation. G is a stable graph, and ξ̄ = ξ̄_G : ∏_w M̄_w → M̄_g is the gluing map. It is finite, and ξ̄ maps ∂(∏_w M̄_w) into strata deeper than Δ_G, since a boundary point of some M̄_w carries an extra node. Hence ξ̄^{-1}(Δ_G) = ∏_w M_w. On coarse spaces, ξ = ξ̄|_{∏M_w} : ∏M_w → Δ_G is the quotient by the finite group Aut(G) (standard; cited from memory). Aut(G) acts by permuting factors and relabelling marked points. In particular ξ is finite and open.

Put A := closure(𝒱) ∩ (Δ_G × Δ) and C := closure(V_0) ∩ Δ_G. By (R2), A = H(C × Δ).

### 1.1 Preliminaries

**(P1) closure(C) \ C is finite.** closure(V_0) is a compact analytic subset of M̄_g by (R1). The set C has dimension ≤ 1. Its 1-dimensional components are open dense subsets of irreducible compact curves, and each such curve meets the deeper strata (a closed analytic set not containing the curve) in finitely many points. The isolated points of C are closed. Since ξ̄ is finite, ξ̄^{-1}(closure(C)) = ξ^{-1}(C) ∪ (a finite set).

**(P2) The lifted family is analytic.** Put 𝓑 := (ξ̄ × id)^{-1}(closure(𝒱)) ∩ (ξ̄^{-1}(closure Δ_G) × Δ). It is analytic in ∏M̄_w × Δ by (R1). Put Z := ∂(∏M̄_w) × Δ, and let 𝓦_G be the closure of 𝓑 \ Z = (ξ×id)^{-1}(A).
- 𝓦_G is the union of the irreducible components of 𝓑 not contained in Z, so it is analytic.
- An irreducible component of 𝓑 minus a proper analytic subset stays irreducible. Hence the irreducible components of 𝓑 \ Z are the traces of these components.
- So the closure of any union of components of 𝓑 \ Z is analytic.
- 𝓦_G → Δ is **proper**, because 𝓦_G is closed in ∏M̄_w × Δ and ∏M̄_w is compact.

**(P3) Local purity.** Near a point of (C^{1} \ Sing) × {t}, where C^{1} is the 1-dimensional part, A is a topological 4-manifold. It is therefore pure 2-dimensional analytic there. Since ξ × id is finite and open, its preimage is also pure 2-dimensional there.

**(P4) Fibres of 2-dimensional components.** Let W be a 2-dimensional irreducible component of 𝓦_G.
- The coordinate t is non-constant on W, because every fibre of 𝓦_G → Δ has dimension ≤ 1: it lies in ξ̄^{-1}(H_t(closure C)), which is 1-dimensional plus a finite set.
- So every fibre W_t is either empty or of pure dimension 1. Fibres of a non-constant holomorphic function on an irreducible 2-dimensional space have pure dimension 1. By properness and the open mapping property, W_t is in fact nonempty for all t.
- By (P1), W_0 ⊂ ξ^{-1}(C) ∪ (finite set). Being pure 1-dimensional, **W_0 is a finite union of closures of pieces at time 0.**
- **Every piece E at time t is dense in a component of W_t for some such W.** Take a generic point x of E, i.e. not over Sing(C_t) and not on other pieces. By (P3), the germ of 𝓦_G at (x, t) is pure 2-dimensional, so E × {t} lies in the union of the fibres of the finitely many 2-dimensional components through nearby points. Since E is irreducible, E ⊂ W_t for one W. Then closure(E) is a component of the pure 1-dimensional set W_t.

### 1.2 L1 in the product case (proved)

Suppose G is of product type, so ξ is injective. By Lemma R0 (PR-D), the 2-dimensional components W are the 𝓦^{(a)}, and W_0 ⊂ 𝐂_0^{(a)} = closure(E_0^{(a)}). By (P4), W_0 is pure 1-dimensional, so **W_0 = closure(E_0)**. Likewise W_t = closure(E_t) with E_t = H_t(E_0): W_t contains the lift of E_t and lies in closure(E_t) ∪ (finite set).

**Lemma L1 (product case).** Suppose pr_u is constant on E_0, equal to Z_0 ∈ M_u. Then for every t, pr_u is constant on every 1-dimensional irreducible component of W_t; here W_t = closure(E_t).

This is the special case of L1′ below in which W_0 has a single component.

### 1.3 L1′ (all G, proved)

**Lemma L1′.** Let W be a 2-dimensional irreducible component of 𝓦_G, and u a vertex of G. Suppose pr_u is constant on each 1-dimensional component of W_0. Then for every t ∈ Δ, pr_u is constant on each 1-dimensional component of W_t.

*Contrapositive (the form used).* Let E be a piece at time t with E ⊂ W_t. If f_u is non-constant on E, then f_u is non-constant on some piece at time 0 contained in W_0.

*Proof.*
1. Let K_1, …, K_r be the components of W_0. The values z_j := pr_u(K_j) lie in M_u, not ∂M̄_u, because K_j is the closure of a subset of ∏M_w and pr_u is continuous.
2. **Affine neighbourhood.** M̄_u (coarse space) is projective (Knudsen–Mumford; from memory), and ∂M̄_u is closed. Choose a homogeneous polynomial vanishing on ∂M̄_u but at none of the z_j. Such a polynomial exists by prime avoidance applied to the homogeneous ideal of ∂M̄_u and the finitely many points z_j. Let U be the complement of its zero set in M̄_u. Then U is affine, U ⊂ M_u, and {z_j} ⊂ U.
3. **Small t.** pr_u(W_0) = {z_j} ⊂ U, and W → Δ is proper. So the set of t with pr_u(W_t) ⊄ U is the image of the closed set W ∩ pr_u^{-1}(M̄_u \ U) under a proper map. It is closed and misses 0, so pr_u(W_t) ⊂ U for |t| < ε.
4. **Compact curves in an affine set.** Each component K of W_t is a compact irreducible curve. Its normalization is a compact connected Riemann surface, and the coordinate functions of U are holomorphic on it, hence constant. So pr_u is constant on each component of W_t for |t| < ε.
5. **Fibre dimension.** Let Φ := (pr_u, t) : W → M̄_u × Δ, a holomorphic map of complex spaces. By the Cartan–Remmert theorem (upper semicontinuity of fibre dimension; from memory), R := {x ∈ W : dim_x Φ^{-1}(Φ(x)) ≥ 1} is an analytic subset of W. By step 4, R contains W ∩ {|t| < ε}, which is a nonempty open subset of the irreducible W. Hence R = W.
6. **All t.** Let K be a component of W_t and x a point of K on no other component of W_t. Near x, Φ^{-1}(Φ(x)) = (pr_u|_K)^{-1}(pr_u(x)), and this has dimension 1 at x. So the analytic subset (pr_u|_K)^{-1}(pr_u(x)) of the irreducible curve K contains a 1-dimensional germ, hence equals K. So pr_u is constant on K. ∎

*Remarks.*
- (a) This rank argument replaces "rank ≤ 1 on an open set, hence everywhere", which is awkward because M̄_u is singular.
- (b) The contrapositive follows from L1′ and (P4).

### 1.4 Why L1 as stated fails for non-product G

The lift of the irreducible family A^{(a)} can have an irreducible component W whose 0-fibre has several components σE_0, σ ∈ Stab(W) ⊂ Aut(G), while W_t is irreducible for t ≠ 0. Then pr_u ∘ σ = r ∘ pr_{σ^{-1}u}, with r a relabelling. So u can be constant on E_0 and non-constant on σE_0, and hence non-constant on W_t for t ≠ 0. Upstairs there is then also no homeomorphism Ē_0 → Ē_t. Nothing in (i), (ii), (R1), (R2) excludes this, since the topology of the finite cover W_t → C_t can change at t = 0.

Local model, ignoring global realizability: σ is the swap on ℂ², and W = {(x − y)^2 = t}. Then W_t (t ≠ 0) is a pair of lines swapped by σ, while W_0 is the diagonal. Combining this with a family in which the two branches over C_0 separate shows that the number of components of W_t can differ from that of W_0.

Indeed, W_0 is a single Stab(W)-orbit of components. Let K be a component of W_0. For generic x ∈ W_0, the point ξ(x) = ξ(k) for some k ∈ K, so x = σk with σ ∈ Stab(W). A component K′ therefore meets σK in infinitely many points, so K′ = σK. The orbit can have several elements.

## 2. L2

### 2.1 Corrected hypothesis

(O) of PR-E concerns Φ^v_t = π_v ∘ ν_t only. L2 uses, for another vertex u, that f^t_u ∘ A_t and f^0_u have the same orbifold monodromy. That requires:

**(O_u)** The orbifold structures (Λ_t, θ_t) of (O) can be chosen so that, in addition, f^t_u ∘ u_t lifts to a holomorphic f^{u}_t : D → T_u, equivariant for some ρ^u_t : Λ_t → Mod_u with ρ^u_t = ρ^u_0 ∘ θ_t up to conjugation in Mod_u.

Equivalently, assume **(O_G)**: (O) for the product map ν_t : Ê_t → ∏M_w, the Teichmüller space ∏T_w and the group ∏Mod_w. Then (O) for v and (O_u) for all u follow by projection.

*Why this cannot be skipped.* (R2) gives f^t_u ∘ Ĥ_t ≃ f^0_u only as maps into the coarse space M_u. Mod_u is generated by torsion in most cases, so the coarse space has very small fundamental group, and a coarse homotopy carries no information about ρ^u. That is exactly the phenomenon behind (O): cone points can appear or disappear along the family. The reduction (O-a)+(O-b) of PR-E applies verbatim to (O_G), with G_X replaced by the product of the stabilizers, but it has not been proved.

By Lemma O1 (PR-E), cone orders may be enlarged. So once (O-a) holds for v and for u separately, a common orbifold structure (lcm of orders) exists. The compatibility (O-b) for u is the real extra input.

### 2.2 Statement

**Lemma L2 (product G).** Let E_0 be a piece with a Teichmüller vertex v satisfying (H_0), and assume (O_G) for E_0. Let u be a vertex with f^0_u non-constant. Then there is a finite set F(E_0, u) ⊂ M̄_u such that, for every t, every puncture p of Ē_t (E_t = H_t(E_0)) satisfies f^t_u(p) ∈ F(E_0, u).

### 2.3 Proof

1. **A_t.** Lemma R* (PR-E), under (H_0) and (O) for v ⊂ (O_G), gives A_t ∈ PSL_2(ℝ) with A_t Λ_0 A_t^{-1} = Λ_t and A_t λ A_t^{-1} = θ_t^{-1}(λ). The induced map ā_t : D/Λ_0 = Ê_0 → D/Λ_t = Ê_t is an orbifold biholomorphism.
2. **Extension to the compactifications, punctures to punctures.**
   - Ê_t is the uniformized orbifold of the lattice Λ_t. Its ends are the cusps of Λ_t, and these are exactly the punctures of Ē_t. Indeed Ê_t = Ē_t \ {punctures}, a compact Riemann surface minus finitely many points, and finitely many points are removed from the compact Ē_t.
   - A_t is an isometry conjugating Λ_0 to Λ_t. It maps parabolic fixed points of Λ_0 to those of Λ_t, and horoball neighbourhoods to horoball neighbourhoods.
   - So ā_t maps a punctured-disc neighbourhood of each puncture of Ē_0 biholomorphically onto a punctured-disc neighbourhood of a puncture of Ē_t. By the Riemann removable singularity theorem it extends to a biholomorphism Ā_t : Ē_0 → Ē_t, sending punctures bijectively to punctures.
   - θ_t is induced by a homeomorphism homotopic to Ĥ_t^{-1}. Homotopic homeomorphisms induce the same bijection on punctures, since punctures correspond to conjugacy classes of maximal parabolic subgroups. So Ā_t induces the same bijection on punctures as Ĥ_t. This last point is not needed below.
3. **Homotopy.** Put g_t := f^{u}_t ∘ A_t : D → T_u. It is holomorphic, and for λ ∈ Λ_0,
   g_t(λx) = f^u_t(θ_t^{-1}(λ) A_t x) = ρ^u_t(θ_t^{-1}λ) g_t(x) = ρ^u_0(λ) g_t(x)
   after the conjugation allowed in (O_u). So g_t is ρ^u_0-equivariant, i.e. orbifold-homotopic to g_0 = f^u_0. It descends to ḡ_t = f^t_u ∘ Ā_t : Ē_0 → M̄_u, which is holomorphic, being a composite of holomorphic maps.
4. **Infinite monodromy, hence non-constancy.** Suppose ρ^u_0 had finite image.
   - By Selberg's lemma choose a torsion-free Λ′ ⊂ ker ρ^u_0 of finite index in Λ_0.
   - g_0 is Λ′-invariant, so it descends to a holomorphic map from R′ := D/Λ′, a compact Riemann surface R̄′ minus finitely many points, into T_u.
   - T_u is biholomorphic to a bounded domain in ℂ^N (Bers embedding; from memory). Bounded holomorphic functions extend over punctures, and holomorphic functions on the compact R̄′ are constant.
   - So g_0 is constant, a contradiction since f^0_u is non-constant and dim T_u > 0. (If dim M_u = 0, f_u is constant and there is nothing to prove.)
   - Hence ρ^u_0 has infinite image. A constant map has monodromy contained in a finite stabilizer, so every g_t is non-constant.
5. **Finiteness.**
   - Fix N ≥ 3. Let Λ″ := (ρ^u_0)^{-1}(Mod_u[N]) ∩ Λ′, a finite-index torsion-free normal subgroup of Λ_0 (intersect conjugates if needed). Then R := D/Λ″ is a hyperbolic Riemann surface of finite type.
   - Each g_t descends to a non-constant holomorphic map R → M_u[N] = T_u/Mod_u[N]. This is a complex manifold and a fine moduli space of curves of type (g_u, n_u), with 2g_u − 2 + n_u > 0.
   - The homotopy class of this map is ρ^u_0|_{Λ″} up to conjugation by Mod_u. Because of the conjugation in (O_u), this means up to conjugation by one of the finitely many coset representatives of Mod_u/Mod_u[N]. So there are only finitely many homotopy classes.
   - **Cited (from memory): Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces" (MSRI Publ. 11, 1988).** For a Riemann surface R of finite type and a type (h, m) with 2h − 2 + m > 0, a given homotopy class (monodromy) of maps R → T_{h,m}/Γ, Γ torsion-free of finite index, contains at most finitely many non-constant holomorphic maps. I believe they actually prove the rigidity statement "at most one", which is stronger. They also prove that there are finitely many non-trivial families overall, which is the Parshin–Arakelov finiteness.
   - The hypotheses hold: R has finite type, the target is a torsion-free quotient with ordered marked points allowed, and the maps are non-constant by step 4.
   - Hence the descended g_t, and so the g_t and ḡ_t, lie in a finite set {φ_1, …, φ_r} of maps Ē_0 → M̄_u, independent of t. Here ḡ_t is the unique continuous extension of g_t.
   - *Alternatives.* McMullen's rigidity of Teichmüller curves applies only to v, not to a general u, so it does not replace this step. Arakelov–Parshin rigidity (compact base, fixed degeneration set) gives the same conclusion after compactifying and passing to the family over R. I cite only Imayoshi–Shiga.
6. **Puncture values.** If p is a puncture of Ē_t, then q := Ā_t^{-1}(p) is a puncture of Ē_0, and f^t_u(p) = ḡ_t(q). So
   F(E_0, u) := {φ_j(q) : 1 ≤ j ≤ r, q a puncture of Ē_0},
   a finite set independent of t. ∎

### 2.4 Additional remarks

- The addendum "closure(π_u(E_t)) = closure(π_u(E_0))" (PR-D Step 6) also follows in the product case. Step 5 gives K_t ∈ {closure φ_j(Ē_0)}, and the closedness argument of PR-D Step 6 then applies. The chain does not need it.
- **PR-E's (O) does not imply (O_u).** Nothing forces the cone points needed by f_u to coincide with those needed by f_v, or to persist compatibly.

### 2.5 Is (O_G) "automatic when there are no orbifold issues"?

Yes, in this sense. Suppose that for all t, Φ_t = (π_w ∘ ν_t)_w maps Ê_t into the locus where every factor has trivial (effective) automorphism group. Then Φ_t lifts along the honest covering ∏T_w → ∏M_w, restricted to that locus, with Λ_t torsion-free. The monodromy is then defined from the continuous family H by the homotopy lifting property, so ρ_t = ρ_0 ∘ (Ĥ_t)_* holds automatically. (O-b) is immediate from covering theory, and (O-a) is vacuous.

### 2.6 L2′ for non-product G (sketch)

Let C^{(a)} be a 1-dimensional component of C, and C_t := H_t(C^{(a)}) with normalization Ĉ_t. Put Mod_G := the stabilizer of the stratum, an extension of Aut(G) by ∏Mod_w (more precisely: the group generated by ∏Mod_w and the relabelling/permutation lifts of Aut(G)), so that Δ_G = ∏T_w / Mod_G as coarse spaces.

**(O_G, downstairs).** For each t there are:
- an orbifold lattice Λ_t uniformizing Ĉ_t;
- ρ_t : Λ_t → Mod_G;
- an equivariant holomorphic f_t : D → ∏T_w lifting C_t ↪ Δ_G;
- θ_t : Λ_t → Λ_0 as in (O);

with ρ_t = ρ_0 ∘ θ_t up to conjugation in Mod_G.

Put Λ^♮_t := ρ_t^{-1}(∏Mod_w), a finite-index normal subgroup with Λ^♮_t = θ_t^{-1}(Λ^♮_0).
- D/Λ^♮_t → ∏M_w is holomorphic, and its image is dense in a piece at time t.
- Every piece over C_t is obtained this way after composing with an element of Aut(G).
- Cusps of Λ^♮_t map to points over closure(C_t) \ C_t, i.e. to punctures, and every puncture of a piece over C_t arises this way.

Let v be a Teichmüller vertex of some piece over C_0, given by step 2 of the chain. Then the v-coordinate of f_0, restricted to Λ^♮_0, is an isometric equivariant embedding. Run Lemma R* for the lattice Λ^♮_0, using the vertex σ_t(v) at time t, where σ_t is the permutation induced by the conjugating element. This gives A_t conjugating Λ^♮_0 onto Λ^♮_t compatibly with θ_t.

Steps 3–6 of §2.3 then apply verbatim to each vertex u and each of the finitely many Aut(G)-translates. The conclusion: the puncture values at vertex u of all pieces over C_t lie in a finite set F(C^{(a)}, u), independent of t.

I have not written this out in full. The only new ingredients beyond §2.3 are the normality of Λ^♮ and the bookkeeping of Aut(G). Status: **sketch.**

## 3. The derivation of the claim from MS6

1. **Step 1 (correct).**
   - Y : Δ → M_{g_i,n_i} is holomorphic (PR-A).
   - Suppose Y_t ∈ F for t ∈ T, with F finite and T accumulating at t_* ∈ Δ. Choose distinct t_n ∈ T with t_n → t_*. By pigeonhole, infinitely many t_n satisfy Y(t_n) = y for a single y ∈ F.
   - Y^{-1}(y) is an analytic subset of the connected 1-dimensional Δ with a non-isolated point, so it is all of Δ. Hence Y_t = y = Y_0.
2. **Step 2.** This depends on Lemma PA, Lemma T′ and (F2), which I did not check (not provided). For non-product G, "apply on the lift" must mean what §2.6 requires: a Teichmüller vertex, in the sense of (H_0), of the finite cover D/Λ^♮_0, i.e. of a piece over C_0.
3. **Step 3 (correct, given finiteness of the inputs).**
   - There are finitely many strata G. For each G, finitely many pieces at time 0 (by (P1); a compact analytic set has finitely many components) and finitely many vertices.
   - Each F(E_0, u) is finite. Each stable curve has finitely many irreducible components.
   - The n_i-pointed smooth curves isomorphic, after one of the n_i! relabellings, to a smooth irreducible component (or its normalization) with its special points form a finite subset of M_{g_i,n_i}.
   - So F is finite and independent of t. **But** L2 must be applied under (O_G), or (O_u) for every non-constant vertex u, not merely (O) for the Teichmüller vertex.
4. **Step 4.**
   - *Product G:* correct. By (P4) and §1.2, a piece E at time t equals H_t(E_0) for a unique piece E_0, with W_t = closure(E_t). By L1, u is non-constant on E_0. By L2, f^t_u(p) ∈ F(E_0, u).
   - *Non-product G:* the sentence "E_t is the transport of some piece E_0" is **false in general** (§1.4). Replace it as follows. E lies over C_t = H_t(C^{(a)}). The puncture values of E at u lie in F(C^{(a)}, u) by L2′ (§2.6). L1′ is then not even needed: L2′ covers all vertices u that are non-constant on some piece over C_0. Moreover, by L1′, a vertex non-constant on E is non-constant on some piece over C_0. Since F(C^{(a)}, u) is only claimed to be finite, the argument only needs u non-constant somewhere over C_0, which L1′ gives.
   - Alternatively, restrict MS6 to product-type strata G, or to pieces with W_0 irreducible. Then the original L1/L2 suffice.
5. **Conclusion.** With MS6, (O_G) (or (O_u) for all relevant u), Lemma PA, Lemma T′ and (F2), the problem's claim follows for product-type strata G in MS6. For non-product G in MS6 it follows modulo the sketch L2′.

## 4. Proved / not proved / open

**Proved here** (modulo the cited standard facts: Knudsen–Mumford projectivity, Cartan–Remmert, Bers embedding, Selberg, Imayoshi–Shiga, and the coarse-space description of Δ_G; all cited from memory):
- (P1)–(P4).
- L1 for product G.
- L1′ for all G.
- L2 for product G under (H_0) and (O_G). This includes: extension of A_t to the compactifications with punctures going to punctures, infinite monodromy of non-constant maps, the reduction to Imayoshi–Shiga, and finiteness of the puncture values.
- Steps 1 and 3 of the chain, and step 4 for product G.

**Flaws found in the chain as written:**
1. L1 is wrong as phrased for non-product G. Corrected to L1′.
2. L2 needs (O_u)/(O_G), not just (O) for the Teichmüller vertex v.
3. Step 4's "E_t is the transport of some E_0" fails for non-product G. Replace it with L2′, or restrict MS6 to product strata.

**Sketched only:** L2′ (§2.6) for non-product G.

**Open (not attempted, as instructed):**
- MS6.
- (O) and its strengthening (O_G), including the splitting and cusp issues of PR-E §2.3.
- (F2) of PR-F, and Lemmas PA and T′, which I did not check.

=== END OF ANSWER round7_q9 ===
