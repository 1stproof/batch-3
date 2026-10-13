# Referee report on Part II (Theorem A), extra_q8

Scope: §§2–7, §9 and the citations of §10 (including Lemmas F0 and F1). The Part I inputs I.2, I.3 (CL, J0), I.5 and I.6 are taken as given, as instructed. Citations are judged from memory; I had no access to the literature.

## (1) Verdict

**Theorem A is proved after minor repairs**, given I.2, I.3, I.5, I.6, the cited classical facts, and the readings (R1) + (R2^orb). Equivalent forms of the hypotheses are (R1) + (R2) + (AP), or (R1) + (R2) + (Loc).

- I found no fatal error.
- All the repairs below are local and are given in full:
  - an open-versus-closed disc slip in Setting 6.0;
  - a tacit closedness assumption in §1.2, which turns out to be harmless;
  - a dangling cross-reference in Remark 7.6, for which I give a self-contained replacement.
- The one citation whose scope I would ask the authors to state more carefully is Thurston's theorem (Th) for **cusped** finite-area surfaces (§4 notes below). I believe it holds in that generality, but this is from memory.

**A condition, not a gap.** The result is conditional on the orbifold reading. In the coarse form this is the hypothesis (AP): H_t preserves |Aut| of every boundary point. (AP) is not stated in the problem, and the document says so. **The problem under the coarse reading (R2) alone remains open** — it is neither proved nor refuted here.

## (2) Table

| Result | Verdict | Reason |
|---|---|---|
| §1.2 (dim B_t ≤ 1) | correct, with a remark | Needs V_t locally closed (true: 𝒱 is a submanifold). The identity closure(V_t)∖V_t = closure(V_t) ∩ ∂M̄_g needs V_t closed in M_g. Only A_t ⊂ closure(V_t) ∩ ∂M̄_g is used, so this is harmless. |
| Lemma 1.1 | correct | Node count equals |S(p)|, and S(p) ⊆ S(p_0) nearby. |
| Lemma 2.1 | correct | Chow, finiteness of components, K(E) = pr_M(Ē). |
| Lemma 2.2 | correct | Immediate. |
| Lemma 2.3 | correct | Proper image is the closed graph; locally irreducible, so normalisation is a homeomorphism. |
| Lemma 2.4 | correct | Topological characterisation via (CG). |
| Lemma 2.5 | correct | Standard. The remark on K_G is correct and unused. |
| Lemma 3.1 | correct | Descent, injectivity (via "⊂" of (c)), surjectivity, openness of p on a saturated set, properness of ξ_G for Θ^{-1}, extension of Ĥ_t over finitely many points: all check. |
| Lemma 4.1 | correct | Lifting criterion with (Ĥ_t)_*N_0 = N_t; conjugation preserves element types. |
| Prop. 4.2 | correct | The identity p∘F_t = ν_t∘u_t checks; CL applies; (b) gives equivariance. |
| Lemma 4.3 | correct (citation caveat on (Th)) | τ(g) = ℓ(μ) with Min(g) the axis; 1-Lipschitz bound; Thurston; centraliser; density of axis crossings. |
| Thm 4.4(a) | correct | t-independent homomorphism r; constancy ⟺ r_w = 1. Lemma 4.3 is not even needed for (a) (note §4.6). |
| Thm 4.4(b) | correct | Finite candidate set (F0/F1), then a closed-partition argument on the connected Δ. |
| Cor. 4.5 | correct | Lemma 2.2 applied to E_t, with (a) and (b). |
| Prop. 5.1 | correct | Lemma 2.5 + (a), (c). |
| Prop. 5.2 | correct | Orbit-counting via (Kur) and Prop. 5.1. |
| Setting 6.0 | minor slip, repaired | β must be an **open** disc for the openness claim in 6.1(1). |
| Lemma 6.1 | correct after the repair | (1) local connectedness via (R1); (3) clopen argument via Θ; (4) uniqueness of p(t); (5) (PN2). |
| Prop. 6.2 | correct | (PN3) on the whole of L_S ∩ B, plus continuity of comp_x at p(t) ∈ L_S ⊂ L_x. |
| Prop. 6.3 | correct | Both MERGE and MOV give u ∈ M(E). F′(E) includes the smooth coordinates. |
| Remark 6.4 | correct | (b) gives Π_t∘σ = σ∘Π_t. |
| Lemma 7.1 | correct | Slice argument. |
| Thm 7.2 | correct | Construction, uniqueness, (a)–(d), joint continuity (finite K fixes the limit). |
| Remark 7.3 | acceptable | It is a statement about a reading, not a proof. |
| Thm 7.5 | correct | (P2)(i)–(v) check; path lifting at constant |Aut|; joint continuity by properness of U → P(U). |
| Remark 7.6 | dangling reference, repaired | "Corollary C.5" is not in Part II. A self-contained proof is given in §7 notes. |
| §9 assembly | correct | Same fixed point p_m(t) on both sides of each transition. The endpoint lands in the finite set F′(E_b). Then Lemma 2.3. |
| Lemma F0 | correct | Big Picard, Riemann–Hurwitz degree bound, divisor + constant count. |
| Lemma F1 | correct (given (IS_c), (BC), (TF)) | Characteristic cover, pair group L, local injectivity and finite fibres of Υ, rigidity of lifts. |

## (3) Detailed notes and repairs

### §1.2 and §2

**Dimension of B_t.**
- The argument that every component Z of closure(V_t) has dimension 2 needs V_t to be open in closure(V_t) near its own points. This holds because V_t is a locally closed (embedded) submanifold: 𝒱 is a submanifold of M_g × Δ, and the family is smoothly trivial, so V_t is a 2-dimensional submanifold.
  - Then Z meets V_t in a non-empty open subset of V_t, near which closure(V_t) = V_t is 2-dimensional. Irreducibility gives dim Z = 2.
- The text writes B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g. The equality requires closure(V_t) ∩ M_g = V_t, i.e. V_t closed in M_g. That is the natural reading ("subvariety"), but it is not proved.
- **Repair / remark.** Everything actually used is A^G_t ⊂ closure(V_t) ∩ ∂M̄_g for boundary strata G. This is a proper analytic subset of every component (each component meets V_t ⊂ M_g), so dim ≤ 1 regardless. Define B_t := closure(V_t) ∩ ∂M̄_g; nothing else changes.

**Lemma 2.1.** Correct.
- (R1) gives closure(V_t) closed analytic in M̄_g.
- K(E) = pr_M(Ē) because pr_M(Ē) is compact, contains pr_M(E), and lies in closure(pr_M E).

**Lemma 2.3.** Correct.
- Continuity: Y_t = π_i(H_t z_0).
- (ξ̄_Γ)^{-1}(Δ_Γ) = ∏ M_{g_j,n_j}, since a boundary coordinate adds nodes. Hence φ(𝒜̂′ ∖ 𝒵̂) is the graph of Y.
- φ is proper because ∏M̄ is compact. The graph is closed by continuity of Y.
- Σ ≅ Δ topologically, so Σ is pure 1-dimensional and locally irreducible. Its normalisation is a homeomorphism, and a bijective holomorphic map of Riemann surfaces is biholomorphic.
- The identity theorem finishes the proof.

**Lemma 2.4.** Correct. Point 3 uses that ν^{-1} of the multi-branch points, and of E ∩ (other components), is discrete in Ê.

**Lemma 2.5.** Correct.

### §3, Lemma 3.1 (task item 1)

1. **Descent.**
   - Π_t(px) := p(H̃_t x) is well defined by (b) for Mod_Π.
   - ξ_G Π_t = H_t ξ_G by (a).
   - Π_t takes values in Â_t because H_t(A^G_0) = A^G_t (R2).
2. **Injectivity of H̃_t.**
   - H̃_t x = H̃_t y ⇒ ξ_G p x = ξ_G p y (H_t injective) ⇒ y = gx (St2).
   - Then g ∈ Stab(H̃_t x) ⊆ Stab(x). This is exactly the inclusion Stab(H̃_t x) ⊆ Stab(x) of (c), which the text calls "⊂". Correct.
3. **Surjectivity onto Ã_t.** Correct; it uses Mod_G-invariance of Ã_0 and (b) for all g ∈ Mod_G.
4. **Bijectivity of Π_t.** Correct.
5. **Joint continuity.**
   - Correct: the restriction of an open orbit map to a saturated subset is open onto its image, because p(U ∩ Ã_0) = p(U) ∩ Â_0.
   - Hence p × id is a quotient map on Ã_0 × Δ.
6. **Continuity of Θ^{-1}.** Correct.
   - ξ_G(z_n) = H_{t_n}^{-1}(ξ_G w_n) converges in A_0 ⊂ Δ_G, by continuity of H^{-1} on closure(𝒱).
   - ξ_G : ∏M_w → Δ_G is proper, so (z_n) lies in a compact set.
   - Â_0 = ξ_G^{-1}(A_0) is closed, and A_0 is closed in Δ_G.
   - Limit points are unique by injectivity of Π_t.
   - Restricting Θ to the slice t gives that Π_t is a homeomorphism.
7. **(4)** Correct.
8. **(5)** Correct: Lemma 2.4 applies to Â_0 and Â_t (dimension ≤ 1 by the corrected §1.2).
9. **(6), the homeomorphism Ĥ_t.** Correct.
   - Off a finite set, ν and ν_t are homeomorphisms.
   - At an exceptional point ẑ, the images of shrinking punctured discs are connected and accumulate only on the finite fibre ν_t^{-1}(Π_t ν ẑ), by properness of ν_t. Hence they eventually lie near a single point of that fibre, and the choice is consistent for nested discs.
   - The extension of Ĥ_t^{-1} is constructed the same way. The two compositions are the identity on a dense set, hence everywhere.
   - A homeomorphism of finite-type surfaces maps ends to ends.

No gap.

### §4, Theorem RO (task item 2)

**Lemma 4.1.** Correct.
- Ĥ_t preserves genus, the number of punctures and the cone data, so χ^orb is unchanged and (Unif) applies. The bad orbifolds have χ^orb > 0 and are excluded.
- **Lifting criterion.** We need (Ĥ_t ∘ u_0)_* π_1(H^♮_0) = (Ĥ_t)_*(N_0) ⊆ N_t. This holds because Ĥ_t maps a peripheral loop around c to a loop freely homotopic to the peripheral loop around Ĥ_t(c) or its inverse, and N_0, N_t are normal. So base points do not matter.
- The lift is a homeomorphism (lift the inverse; compositions are deck transformations, and one normalises). It extends over the cone preimages.
- θ_t preserves element types: elliptic ⟺ finite order; parabolic ⟺ stabilises a horoball component over a cusp neighbourhood.

**Prop. 4.2.** Correct.
- F_0(H) ⊂ Ã_0.
- From ν_t Ĥ_t = Π_t ν and u_0 h̃_t^{-1} = Ĥ_t^{-1} u_t:
  p F_t = Π_t ν Ĥ_t^{-1} u_t = ν_t u_t.
- CL applies with Γ = Mod_Π. Non-effectiveness of the action is irrelevant, and ∏M_w carries Cartan's quotient structure.
- Equivariance: h̃_t^{-1} λ = θ_t(λ) h̃_t^{-1}, then (b).

**Lemma 4.3.** Correct.
- **Step 1.**
  - Projecting F_0 λ = g F_0 to the j-coordinate gives g_j f_0 = f_0 μ. So g_j preserves the Teichmüller disc and acts on it as a hyperbolic isometry; it is pseudo-Anosov by (VT).
  - **Min(g) = axis can be proved directly** from uniqueness of the invariant geodesic and τ(g^n) = nτ(g):
    - If d(X, gX) = τ, then d(X, g^n X) ≤ nτ = τ(g^n) ≤ d(X, g^n X).
    - So the orbit lies on a geodesic, because Teichmüller space is uniquely geodesic.
    - That geodesic is g-invariant, hence it is the axis.
  - The normalisation (curvature −4 versus the Teichmüller metric) makes the disc isometric, so τ(g) = ℓ(μ).
- **Step 2.** Correct. It uses Royden: a holomorphic map is 1-Lipschitz from Kobayashi to Kobayashi = Teichmüller. The direction of the inequality is right.
- **Step 3.**
  - φ : H/Λ′ → H/Λ′_t is induced by h̃_t. For γ = θ_t^{-1}(λ′) = h̃_t λ′ h̃_t^{-1}, Step 2 gives ℓ_t(γ) ≥ ℓ(λ′). So ψ = φ^{-1} does not increase the length of any closed geodesic.
  - Thurston: see the citation caveat in (4).
  - Lifting the homotopy: start from the lift h̃_t^{-1} of ψ. The end lift Ã is an isometry with Ã γ Ã^{-1} = θ_t(γ) on Λ′_t, so A_t := Ã^{-1}. This only fixes the notational direction.
  - The conjugation is constant along the lifted homotopy because it varies continuously in a discrete set.
- **Extension to Λ.** Correct.
  - c centralises the lattice Λ′.
  - Proof of (Cent): c conjugates each hyperbolic h to itself, so it fixes the attracting fixed point of h. These points are dense in ∂H, so c = id. This covers orientation-reversing c as well.
- **Step 4.** Correct. Equality in the 1-Lipschitz bound forces k_t(x) ∈ Min(g) = f_0(α_μ). Injectivity of f_0 at crossings, plus (Dens), gives k_t = f_0.
- **Orientation.** A map that is both holomorphic and anti-holomorphic is constant. So A_t ∈ PSL_2(ℝ) and A_t Λ A_t^{-1} = Λ_t.

**Theorem 4.4(a).** Correct.
- **Step 1 (the homomorphism r).**
  - (N(S) ∩ Mod[N]S)/S is a subgroup of finite index.
  - Λ″ := the normal core of (Selberg subgroup ∩ Λ^N).
  - For μ ∈ Λ″, R(μ) = gS with g = ms (m ∈ Mod[N], s ∈ S). So m = g s^{-1} ∈ R(μ).
  - Uniqueness: S ∩ Mod[N] = 1, since Mod[N] is torsion-free by (TF). For genus-0 vertices this is the pure spherical group; a finite-order pure class is a Möbius map fixing ≥ 3 points, hence trivial.
  - r is a homomorphism because R(μν) = R(μ)R(ν).
- **Step 2.** g_t(μx) = r(μ) g_t(x), independently of t. Correct.
- **Step 4.**
  - Both directions are correct. The finite stabiliser in the torsion-free Mod_w[N] is trivial.
  - Bounded holomorphic functions on a finite-type R extend to R̄.
  - ρ_w has finite fibres and H is connected, so "pr_w constant on E_t ⟺ ḡ^w_t constant".
  - ā_t∘u_0 maps onto Ê_t.

**Answer to "constant vertices stay constant with the same value".**
- What is established: c ∉ M(E) ⇒ c ∉ M(E_t) for every t, i.e. constant vertices stay constant.
- The value φ_c(E_t) is **not** claimed to be independent of t, and it need not be. §9 only uses the time-t identity [comp_x(p(t))] = [φ_c(E_t)] (Prop. 6.2) at each fixed t.
- So the Route sentence "carries constant vertex values along pieces" should be read as: at each time t, the constant value on E_t is the value seen at the fixed lift p(t). In that sense it is established.

**Theorem 4.4(b).** Correct.
- Step 5: the image of pr_M on E_t is determined by the tuple (ḡ^u_t), which lies in the finite set ∏Φ_u. The source R = H/Λ″ is fixed, thanks to A_t.
- Step 6:
  - T_K is closed, using joint continuity of Π and closedness of K in ∏M̄_u.
  - K(E_{t*}) ⊂ K forces equality, since both are irreducible curves.
  - The T_K are finitely many, disjoint and closed, and they cover the connected Δ; and 0 ∈ T_{K(E)}.

**Cor. 4.5.** Correct.

### §5, Props. 5.1 and 5.2 (task item 3)

**Prop. 5.1.** Correct.

**Prop. 5.2.** Correct.
- **Single point.** q^{-1}(J_t) ∩ B = Aut(J)·p, and |Stab_{Aut(J)}(p)| = |Aut(X_p)| = |Aut(J_t)| = |Aut(J)|. So the orbit is a single, Aut(J)-fixed point.
  - Only |Aut(J_t)| ≥ |Aut(J)| is needed, i.e. the inclusion "⊃" of (c), as the text says.
- **Continuity** follows from compactness of closure(B′) ⊂ B and uniqueness.
- **Deepest locus** follows from the node count.
- The (Kur) statement Stab_{Aut(J)}(p) ≅ Aut(X_p) for all p ∈ B (B small) is the standard fact that [B/Aut(J)] → M̄_g is an open immersion of stacks. It is correctly stated.

**Use in Lemma 6.1(4) and Prop. 6.2.** Correct. Every sequence (p_n, t) ∈ Ñ with q(p_n) → J_t converges to p(t), because closure(B′) is compact and the limit is unique.

### §6

**Setting 6.0(i): open versus closed disc (minor slip).**
- β is taken to be a *closed* disc. But Lemma 6.1(1) (openness of N in ℬ_G) and 6.1(3) (openness of ξ_G^{-1}(β ∖ J) in Â_0) need β ∖ J to be **open** in A^G_0.
- **Repair.**
  - Choose a closed disc β_c satisfying (i)–(iv), and let β be its interior, an open disc neighbourhood of J in the branch.
  - β ∖ J is then a connected punctured open disc. It is open in A^G_0 because, near any y ∈ β ∖ J, B_0 coincides with β (by (iv)) and A^G_0 ⊂ B_0.
  - Take β̃ to be the closure in B of the component of q^{-1}(β ∖ J) ∩ B meeting the given lift germ. Its intersection with B, minus 0, is connected for B small.
  - Nowhere is compactness of β used; Lemma 6.1(4) only needs y_n ∈ β ∖ J with y_n → J.

**Lemma 6.1.**
- (1) Correct.
  - q^{-1}(N) is open in the analytic set (q × id)^{-1}(ℬ_G) ∩ (B × Δ_ε), which uses (R1). So it is locally connected and its components are open.
  - The union of the Aut(J)-translates of Ñ is clopen.
  - q is an open and closed surjection of q^{-1}(N) onto N: surjective because N ⊂ q(B′) × Δ_ε. The image is clopen in the connected set N.
- (2) Correct.
- (3) Correct.
  - Uses (ii) to put ξ_G^{-1}(β ∖ J) in the regular 1-dimensional locus.
  - Uses Θ restricted to the open set ξ_G^{-1}(β ∖ J) × Δ_ε.
  - Π_0 = id gives the base point of the connectedness argument.
- (4) Correct.
- (5) Correct. S = E(G_J) would give G_β ≅ G_J, i.e. J ∈ Δ_{G_β}, contradicting (P). An edge outside S is contracted into some vertex, which becomes nodal by (PN2).

**Prop. 6.2.** Correct.
- (PN3) holds on all of L_S ∩ B, not only on β̃. So the labelling identity holds on Ñ_t, which has pattern S.
- p(t) ∈ L_S ⊂ L_x because x is intact.

**Prop. 6.3.** Correct.
- In the MOV case, κ̂(t)_u may itself be smooth. F′(E) still contains its class, because Definition 2.1′ takes *all* coordinates u ∈ M of points κ ∈ K(E) ∩ ∂. Here pr_M κ̂(t) ∈ K(E) ∩ ∂ because some coordinate is nodal (6.1(5)) and is indexed by M (Cor. 4.5).
- Under (PN2), comp_x(p(t)), with the half-edges at x as unordered special points, is exactly a component of κ̂(t)_u with its special points: half-edges in S become markings; edges outside S inside [x] become node preimages.

**Remark 6.4.** Correct.

### §7 (task item 5)

**Lemma 7.1 and Theorem 7.2.** Correct.
- In the joint-continuity claim, every k_j lies in the finite group K = Stab(y_0) = Stab(γ_0(r)).
- The limit H̃_{t_1}(x_0) is fixed by K, so k_k h^k_t(x) → y_1 for every choice of k_k.

**Theorem 7.5.** Correct.
- (P2)(iii): U → P(U) is an open continuous bijection after dividing by A, hence a homeomorphism; and it is proper.
- (P2)(v): the restriction to the closed, A-saturated set Fix(A) ∩ U is a closed injection.
- **Step 1.**
  - Existence: the already-constructed point over c(r_{l−1}) lies in some gU (by (P2)(i)) and has stabiliser of order k. So it is in Fix(gAg^{-1}) ∩ gU and lies on the translated section. The text says this tersely, but it is right.
  - Constancy of stabilisers via (P2)(iv); uniqueness via Lemma 7.1.
- **Step 3.** Uniform convergence of c_{x,t} on [0,1]; disjointness of the translates gU_j confines γ_n([r_j, r_{j+1}]) to U_j; properness plus K-fixedness of γ_0(r_{j+1}) identifies the limit. Correct.

**Remark 7.6: the dangling reference.** "Corollary C.5 below" is not in Part II and could not be checked. **Self-contained replacement.** Suppose no point of B_0 has a non-trivial automorphism. Then (AP) holds for |t| < r, for some r > 0:
- |Aut| is upper semicontinuous on M̄_g: near J, Aut(X_p) ≅ Stab_{Aut(J)}(p) ⊂ Aut(J), by (Kur).
- So {z : Aut(z) = 1} is an open set U ⊃ B_0.
- B_0 is compact, being closed in the projective M̄_g. H is continuous with H(B_0 × {0}) = B_0 × {0}, so H(B_0 × Δ_r) ⊂ U × Δ_r for some r > 0.
- Then |Aut(H_t z)| = 1 = |Aut(z)| for |t| < r.
- The rescaling argument of Remark 7.6 and Lemma 2.3 then give the claim on all of Δ.
- (This is vacuous in genus 2, where every curve has the hyperelliptic involution.)

### §9 (task item 4)

**Set-up.**
- One pair of balls B′ ⋐ B is fixed at each of the points J_1, …, J_{k−1}, Q_0. These balls are shared by all lifts at that point, so at J_m both applications of Prop. 6.2 refer to the same p_m(t).
- Finitely many Setting-6.0 conditions give one common ε.
- Shrinking preserves "labelled by". By (ii), the piece of Setting 6.0 is the piece E^m of I.5.

**Base step.** Π_t on Γ equals ξ_Γ^{-1} H_t ξ_Γ, and E^1_t ⊂ ∂V_t, so φ_1(t) = Y_t.

**Transition m → m+1.**
- Both applications of Prop. 6.2 are at the same point p_m(t), with the same vertex x_m. The two isomorphisms ι, ι′ differ, but classes in 𝔐 forget the labelling.
- The types agree, since ι({x_m}) = c_m and ι′({x_m}) = c_{m+1}.
- So [φ_{m+1}(t)] = [φ_m(t)].

**Endpoint.**
- [Y_t] = [comp_x(p_0(t))] ∈ F′(E_b).
- F′(E_b) is finite and independent of t. The map M_{g_i,n_i} → 𝔐 has finite fibres.
- Y is continuous and Δ_ε is connected, so Y_t = Y_0 on Δ_ε. Lemma 2.3 extends this to Δ.

All hypotheses of the lemmas are met.

### Task item 6: coarse versus orbifold reading

I found no silent substitution of one reading for the other.
- Every use of Π_t, H̃_t or p(t) goes through Lemma 3.1 or Prop. 5.2, which are labelled [orb].
- Lemma 2.3 and Lemma 6.1(1),(2) are genuinely coarse.
- Remark 3.2 (product strata under (R2)) is not used.

### Note 4.6 (simplification, not an error)

Theorem 4.4(a) does not need Lemma 4.3 or Thurston's theorem.
- Use instead the subgroup Λ″_t := θ_t^{-1}(Λ″) ⊂ Λ_t and the map F_t itself. It satisfies F_t(λy) = r(θ_t λ) F_t(y), so it descends to R_t := H/Λ″_t → M[N].
- The criterion "ḡ^w constant ⟺ r_w = 1" is proved exactly as in Step 4.
- Lemma 4.3 is only needed for (b), to fix the source surface R. So the transitions in §9 survive even if (Th) were in doubt; only the endpoint step uses it.

## (4) Citations

- **(Th).** Stated for complete finite-area surfaces with cusps.
  - Thurston's "Minimal stretch maps" proves the identification Lipschitz constant = sup of length ratios, and the rigidity at constant 1 via an area argument. I believe the paper works with complete finite-area surfaces, but this is from memory and should be checked.
  - If only the closed case were available, (b) would need another argument. (a) does not need it (note 4.6).
- **(Bers).** Correctly stated. "Min(g) = axis" also follows from uniqueness of the axis (proof in the §4 notes).
- **(VT), (Roy), (Sel), (Cent), (Dens), (Unif), (KP1), (BE), (Chow), (Irr), (Cl), (CG).** Correct as stated and used within scope.
- **(Kur), (K2), (PN), (St).** Correct as used.
  - (Kur) requires B small enough that Stab ≅ Aut holds at every p ∈ B (an open immersion of [B/Aut(J)]); this is how it is stated.
  - (PN) relies on normalisation along persistent node sections; standard.
- **(TF).** Correct. Nielsen realisation for finite cyclic groups is Nielsen's theorem; Kerckhoff is needed only for general finite groups. Serre's lemma for g ≥ 1 with a fixed point is fine.
- **(IS_c).** Imayoshi–Shiga 1988: finiteness of non-isotrivial holomorphic families of closed genus ≥ 2 curves over a finite-type base. Correctly stated.
- **(dF).** Imayoshi's generalised de Franchis theorem (1983). Correctly stated; not needed given F1.
- **(BC).** MacLachlan–Harvey and Bers–Greenberg give that Φ : T(Γ_0) → T(Γ_Y) is a holomorphic embedding. Correctly stated.
- **(HW), (Krull).** Statements correct; not used in Part II.

**Lemma F0.** Checked.
- The big Picard theorem excludes essential singularities.
- The Riemann–Hurwitz bound d ≤ 2h − 2 + k is correct.
- Divisors are supported in P with bounded degree.
- The constant is fixed by a point of P where f̄ = 1.

**Lemma F1.** Checked.
- K is characteristic, of finite index, and avoids the c_j. Then h′ ≥ 2 by Riemann–Hurwitz.
- Φ is well defined.
- The pair group L avoids Birman–Hilden.
- Λ ∩ ker = 1 by torsion-freeness.
- Γ_1 is torsion-free.
- Υ is locally injective and has finite fibres.
- Two lifts agreeing at one point agree everywhere.

## Open questions (as stated by the document; I agree)

- The claim under the coarse reading (R2) alone, and under (O-int), is open.
- It is open whether a global admissible family can change isotropy at the boundary; under (R2) this is exactly a failure of (AP).
- It is open whether (Loc) at t_0 = 0 alone suffices.
- From this review: the cusped-surface scope of (Th), which is used only for Theorem 4.4(b).

=== END OF ANSWER extra_q8 ===
