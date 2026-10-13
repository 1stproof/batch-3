# round14_q9 — referee check of round13_q10 ("(R1) + (R2^orb) ⇒ Y_t = Y_0")

**Plan/status line.**
- I read the whole task file: round13_q10, and the spliced round12_q9, round13_q9, round11_q9, round11_q1, round11_q4, R8-3 and R8-2 excerpts.
- I check §§0–7 of round13_q10 in order. "✓" means I checked the inference and it is valid; "repair" means I supply a fix.
- Verdict, repairs and remaining dependencies are at the end (§V).

**Status at the end.**
- No fatal gap in the derivation of the conditional theorem.
- Six repairs or corrections are needed. Four are minor and do not touch the main line: (Rep-1) to (Rep-3) and (Rep-5).
- Two concern side claims:
  - (Rep-4): the closing remark of §6, "(Loc) near t_0 = 0 suffices", is **not proved** as written.
  - (Rep-6): the faithfulness claim of §7 has to be qualified. (R2^orb) is faithful to the *embedded / substack* orbifold reading, not to an *intrinsic* orbifold reading. The §7 example in fact satisfies the intrinsic reading.

---

## 1. §§0–1: the formalisation of (R2^orb) and the convention on Mod_G

**(R2^orb) as (a)–(d).**
- The formal statement is unambiguous: a continuous H̃^G on Ã_0 × Δ satisfying (a) lifting, (b) Mod_G-equivariance, (c) equality of Mod_G-stabilisers, (d) H̃_0 = id. ✓
- (R2^orb) contains (R2) verbatim, so Step 1 is trivial. ✓
- **Standing-reading caveat (not new; stated so the dependency list is complete).** (R2) is itself an interpretation of the problem's (i)+(ii). The problem gives, stratum by stratum, smoothly trivial families together with the compatibility (ii). (R2) assumes **one** homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ that trivialises all strata simultaneously, with H_0 = id. (R1) — closure(𝒱) analytic with fibres closure(V_t) — is likewise a reading. round13_q10 takes both as the run's standing readings. I do not re-examine them here, but they are dependencies of the final claim.

**Convention on Mod_G.**
- Mod_G is the group of pairs (σ, (φ_w)), with σ ∈ Aut(G) acting on half-edges. It contains ∏_w Mod_w (pure) with finite index, and T_G/Mod_G = Δ_G as a set and as a coarse space. ✓
- This agrees with round12_q9 §1: "finite extension by lifts of Aut(G), [T_G/Mod_G] = Δ_G as a sub-orbifold, isotropy Aut(z)".
- Allowing σ to swap the two half-edges of an edge is necessary. Automorphisms of Z can exchange the branches at a node, for example at a self-loop. Lemma 3.2 needs this to make the stabiliser map surjective. ✓

**Consequences listed in §1.** Items 1–3 are correct pointers to Lemma 3.2 + (c), round12_q9 Lemma 1.1, and Prop. T. ✓

## 2. §2: Theorem RO applies; which of (a)–(d) it uses

I re-traced the uses against the spliced round12_q9 and its verification round13_q9.

- **Lemma 1.1.**
  - Descent uses (b) for Mod_Π. ✓
  - Π_t lands in Â_t by (a). ✓
  - Injectivity uses (a), injectivity of H_t, and **one inclusion** of (c), namely Stab(H̃_t x) ⊂ Stab(x). ✓
  - Surjectivity uses (a), (b) and Mod_G-invariance of Ã_0. ✓
  - Continuity of Π_t holds because p × id is open on the saturated set Ã_0 × Δ. ✓
  - Continuity of Π_t^{-1} uses properness of ξ_G. ✓
  - "Pieces to pieces" is topological. ✓
  - The finite-type claim for Ê_t needs the repair (R1′) of round13_q9 (Chow). Round13_q10 inherits that repair through "Theorem RO with its repairs".
- **Prop. T** uses (a) through Lemma 1.1 and (b) for g ∈ Mod_Π, and Lemma CL gives holomorphy. ✓
- **Where (d) is used.** I can confirm one place where (d) is genuinely needed: in RO Step 6 (constancy), Π_0 = id is what identifies the constant value with K(E_0). In Prop. T, (d) only gives the consistency F_t|_{t=0} = F_0. Round13_q10's description is accurate.
- **Hence** Theorem RO applies under (R1), (R2^orb), TV/Φ̂ (+PA/TR) and Imayoshi–Shiga. It gives (Rig) in the labelled form, with K(E_t) = K(E_0) and M(E_t) = M(E_0). ✓
- **Strength of the output.** The (Rig) needed by Theorem N, Lemma U (R8-2) and the chain is the "finite set 𝒦 of triples up to Aut(G)-relabelling" form. RO's labelled form is stronger, so it suffices. ✓

**Verdict on §2:** correct. RO uses (a), (b), (c) (one inclusion) and (d), each exactly as stated.

## 3. §3: Lemma 3.1, Lemma 3.2, Proposition 3.3

### Lemma 3.1 (t ↦ Q_t holomorphic at a puncture point) — correct

**Step 1.**
- Near (Q,0), 𝓑 = H((c_1 ∪ ⋯ ∪ c_m) × Δ_ε), because H : B_0 × Δ → 𝓑 is a homeomorphism (by (R2), boundary maps onto boundary). ✓
- The decomposition 𝓑 = Γ_Q ⊔ ⊔_k N_{c_k} near (Q,0) holds by injectivity of H. ✓
- Each N_{c_k} is open in 𝓑 ∖ Γ_Q, because H is a homeomorphism and c_k ∖ Q is open in B_0 ∖ Q near Q. ✓

**Step 2.**
- dim 𝓑 ≤ 2, since 𝓑 is a proper analytic subset of the 3-dimensional closure(𝒱), in which 𝒱 is dense. ✓
- A 1-dimensional component W_i of the germ is not contained in the union of the others. At a point of W_i off the others, 𝓑 is locally a 1-dimensional analytic set, of topological dimension 2. Such a point cannot lie in an N_c, which is a 4-manifold. So W_i minus the other components lies in Γ_Q. By density and closedness, W_i ⊂ Γ_Q. ✓
- The 2-dimensional components cover N := ⊔N_c. Since Γ_Q ⊂ closure(N), they cover 𝓑. ✓

**Step 3.**
- For an irreducible germ, a small representative has connected Reg(W_j) (standard). ✓
- The removed set R := (Γ_Q ∪ ⋃_{i≠j} W_i) ∩ Reg(W_j) is closed in Reg(W_j) and has covering dimension ≤ 2: Γ_Q ≅ disc, and W_i ∩ W_j is analytic of dimension ≤ 1. ✓
- Hurewicz–Wallman (from memory): a closed subset of dimension ≤ n − 2 does not separate a connected n-manifold. ✓
- So Reg(W_j) ∖ R is connected and lies in one N_{c_k}. It is dense in W_j, because R has empty interior in the 4-manifold. Hence W_j ⊂ closure(N_{c_k}) = H(c_k × Δ_ε) (closure taken near (Q,0)). ✓

**Step 4.** Distinct c_k are disjoint off Q and H is injective, so each W_j lies in one H(c_k × Δ). Hence H(c_k × Δ_ε) is the union of the W_j it contains, and so it is analytic. ✓

**Step 5.**
- By (P), β ∩ Δ_G = {Q} near Q. H preserves strata, so Γ_Q = H(β × Δ_ε) ∩ (Δ_G × Δ_ε).
- Δ_G is open in closure(Δ_G): its complement there is a union of smaller strata, which is closed. So near Q we may replace Δ_G by closure(Δ_G), and Γ_Q is a closed analytic curve germ. ✓

**Step 6.** Γ_Q → Δ_ε is a homeomorphism, with inverse t ↦ (Q_t, t), which is continuous. So Γ_Q is locally irreducible everywhere and its normalisation is bijective. t∘ν is a bijective holomorphic map of smooth curves, hence biholomorphic. Therefore t ↦ Q_t is holomorphic. ✓

**Step 7.** ✓

**Scope.** Lemma 3.1 needs one branch with (P) at Q. Every point where the chain invokes MS11♭, and the endpoint, has (P) for both lifts (round11_q9 §1.2, entry 99). ✓

### Lemma 3.2 (Stab_{Mod_G}(x̂) ≅ Aut(Z)) — correct; two examples in the remark are wrong (Rep-1)

**The proof.**
- Uniqueness of α_w: two biholomorphisms in the same isotopy class differ by a biholomorphism of a stable pointed surface isotopic to the identity, which is the identity. ✓
- σ preserves the pairing of half-edges, so ⊔α_w descends to Z. ✓
- Injectivity: α(g) = id forces σ = id on vertices and on half-edges, hence α_w = id and φ_w = 1. ✓
- Surjectivity: lift α to the normalisation. ✓
- K_G ⊂ every stabiliser. ✓
- "(c) modulo K_G ⇔ (c)": both stabilisers contain K_G, so each is determined by its image in Mod_G/K_G. ✓

**(Rep-1), correction to the remark "cases named in the brief".** Two of the listed examples of elements of K_G are wrong. Neither is used anywhere.
- *"Hyperelliptic involution of a (2,0)-component."* A boundary stratum has at least one edge and a connected graph, so every vertex carries at least one half-edge. A (2,0)-vertex therefore does not occur.
- *"Elliptic involution of a (1,2)-component, extended by the identity."* With both special points labelled and fixed, the involution x ↦ −x about p_1 fixes p_2 only when p_2 is 2-torsion. So it is not a generic automorphism.
- *Correct examples:*
  - the elliptic involution of a (1,1)-vertex, extended by the identity;
  - for a (1,2)-vertex whose two special points are the half-edges of a self-loop, the pair (σ swapping the two half-edges, x ↦ p_1 + p_2 − x). That pair is an automorphism of every curve in the stratum.
- The statement "(c) controls all of Aut(Z)" is unaffected.

### Proposition 3.3 [orb] (one lift-curve) — correct

**Item 1.** x̂ ∈ Ã_0 over Q (Q ∈ A_0 trivially) and ŷ = H̃_t x̂ lies over Q_t by (a). Then (c) and Lemma 3.2 give Aut(Q_t) ≅ Aut(Q). ✓

**Item 2.**
- (Kur), from memory: for B small, [B/Aut(Q)] → M̄_g is an open embedding of stacks. That is, Stab_{Aut(Q)}(p) ≅ Aut(X_p) for every p ∈ B. ✓ (This is the standard Deligne–Mumford local structure. The isomorphism is with the full, possibly non-effective, Aut(Q), which is consistent with Lemma 3.2 counting K_G.)
- So |Stab_{Aut(Q)}(p)| = |Aut(Q_t)| = |Aut(Q)|. Hence Stab = Aut(Q), and the orbit q^{-1}(Q_t) ∩ B is a single point. ✓

**Item 3.**
- Continuity: the graph is closed, q is proper on a closed invariant ball, and q^{-1}(Q) ∩ B̄ = {0}. ✓
- Lemma CL applies to the finite group Aut(Q) acting on B. Its proof needs only a properly discontinuous action of a countable group and the Cartan quotient. t ↦ Q_t is holomorphic into q(B) ≅ B/Aut(Q) by Lemma 3.1 and (Kur). ✓
- 𝒥 = graph(p). ✓

## 4. §4: Lemma 4.1, Lemma 4.2, Proposition 4.3

### Shrinking convention — correct, and an even simpler route
- Ñ′_c̃ is connected, lies in q^{-1}(N_c) ∩ (B × Δ_ε), and meets Ñ_c̃. Hence Ñ′_c̃ ⊂ Ñ_c̃.
- An irreducible T′ lies in some component T of closure(Ñ_c̃), and T is anchored.
- The persistence locus is analytic and contains T′, so it equals T. ✓
- The opposite direction (big sheet ⇒ small sheet), which the chain also uses, is immediate here, since persistence equals C(L) and L is a germ. If x ∈ P(T) for an anchored T at scale (B, ε), then x ∈ C(L) by Lemma 4.1(b) and Lemma 4.2 (⊆). By Lemma 4.2, x ∈ P(T′) for every anchored T′ of a branch with (P), at any smaller scale. ✓
- Anchored sheets (T ⊃ c̃ × {0}) coincide with round11_q9's c̃-sheets (slice containing an open subset of c̃ ∖ 0). This is by closedness, given that c̃ ∩ B is irreducible (Milnor ball). ✓

### Lemma 4.1 — correct
- **(a)** c̃ × {0} ⊂ closure(Ñ_c̃), and an irreducible curve lies in one of the finitely many components. ✓
- **(b), setting up.**
  - t ≢ 0 on T, and Krull gives slices of pure dimension 1 at each point. ✓
  - The points (p_n, t_n) ∈ T ∖ 𝒥 exist. ✓
  - q(p_n) ∈ H_{t_n}(c ∖ Q), because T ⊂ Ñ_c̃ ∪ 𝒥 near (0,0) (R7-4 Lemma 2). ✓
  - z_n → Q by continuity of H^{-1}. ✓
  - The arc α_n ⊂ c ∩ U, and H_{t_n}(α_n) ⊂ q(B″). ✓
- **(b), arc argument.**
  - q|_B : B → B/Aut(Q) is proper, so Remmert gives q(C) a closed irreducible curve in q(B), contained in Z = B_{t_n} ∩ q(B). ✓
  - Z is a topological 2-manifold at the points of the open arc, because H_{t_n} is a homeomorphism and B_0 is a smooth disc there. Hence Z is locally irreducible there. ✓
  - O is non-empty (it contains q(p_n), the endpoint H_{t_n}(z_n)). It is open by definition. It is closed in the arc, because q(C) is closed and its germ at any of its points is pure 1-dimensional inside the irreducible germ Z_w. ✓
  - So the arc lies in q(C). Q_{t_n} lies in the closure of the arc and in q(B), so Q_{t_n} ∈ q(C). ✓
- **(b), conclusion.**
  - p′_n → 0 by properness and q^{-1}(Q) ∩ B̄ = {0}.
  - (0,0) is therefore not isolated in the analytic set T ∩ 𝒥, so the germ contains a curve. That curve is a component of the 1-dimensional germ 𝒥, which has no component in {t = 0} because 𝒥 ∩ {t = 0} = {(0,0)}. So T contains a lift-curve. ✓
- This gives a precise proof of round11_q1 Lemma 2.1(c), whose original wording ("every irreducible curve of Σ_t … ") was loose.

### Lemma 4.2 — correct (given Theorem N, R8-3 Lemma 1, entry 19)
- ⊆ ✓.
- ⊇:
  - T_t is pure 1-dimensional at p = p(t). ✓
  - γ ∖ p ⊂ Ñ_c̃ ∩ {t} ⊂ q^{-1}(H_t(c ∖ Q)). So q(γ) is the branch H_t(c) of B_t at Q_t; that branch is locally irreducible, being homeomorphic to a disc. ✓
  - By (Kur), the germ of Def(Q) at p is a versal deformation of Q_t compatible with labels, so Theorem N applies at (Q_t, p, γ). ✓
  - IMOV needs Q_t ∈ Δ_{G_c}. But Q_t ∈ Δ_{G_Q} ≠ Δ_{G_c}, because H preserves strata and (P) holds. So STAY holds. ✓
- The countability argument: an analytic set of dimension ≤ 1 contains curves in only countably many t-slices, while generic t form an uncountable set. Hence A_y = T by irreducibility. ✓

### Proposition 4.3 — correct
- Prop. 3.3 gives 𝒥 = L.
- Lemma 4.1(b) gives L ⊂ T_β and L ⊂ T_b.
- Lemma 4.2 (⊆) on T_β, which needs no (P), gives x ∈ C(L). Lemma 4.2 (⊇) on T_b, which needs (P) for b̃, gives x ∈ P(T_b). ✓
- The hypothesis and conclusion match MS11♭ (round11_q9 §5), since anchored sheets = c̃-sheets. The extra hypotheses of MS11♭ ((S), β̃ ≠ b̃) are not needed. ✓

## 5. §5: the chain

- **Step 1.** (Rig) comes from RO. Every result proved under (R1), (R2), (Rig) and "Y non-constant" applies, because (R2^orb) ⊃ (R2). ✓
- **Steps 2–3.**
  - At genuine transitions (β̃′_m ≠ β̃_m) and at the endpoint, both lifts satisfy (P) (round11_q9 §1.2, from S̃′ + X*_all). So these points are puncture points. ✓
  - Trivial transitions (β̃′ = β̃) need nothing. ✓
- **Step 4.** MS11♭ is invoked only at non-product genuine transitions. There Prop. 4.3's hypotheses hold:
  - J_m is a puncture point;
  - (P) holds for β̃′_m;
  - persistence holds on an anchored (= β̃_m-) sheet, by the induction hypothesis in round11_q9's strong form;
  - (Rig) holds and Y is non-constant.

  The other steps are round11_q9 §§2.5–2.7 (inherited). ✓
- **Step 5 (endpoint).**
  - *Product type:* inherited (Lemma PT, Lemma J, Theorem R). ✓
  - *Non-product type:* Prop. 4.3 gives an anchored T ⊃ b̃ × {0} with x persistent. At t = 0, x is intact on b̃ ∩ B and F_x ≅ Y_0 there.
  - **(Rep-2), a small precision.** The MOV witness z̃^∞ ∈ b̃ ∖ 0 of round11_q9 may lie outside the shrunken ball B used for Prop. 3.3. Then argue as in round11_q9 §2.8:
    - the pattern is constant on b̃ ∖ 0, so x is intact on all of b̃;
    - F_x is holomorphic on L_x ⊃ b̃;
    - the identity theorem along the connected normalisation of b̃ (in the original Milnor ball) propagates [F_x] ≡ [Y_0] to z̃^∞.

    This contradicts MOV ([F_x(z̃^∞)] ≠ [Y_0]). MERGE contradicts intactness. ✓
- **Step 6.**
  - The contradiction shows [Y] is constant.
  - **(Rep-3), a precision.** The problem asks for π_i(∂V_t) = {Y_0} in M_{g_i,n_i}, not only [Y_t] = [Y_0] in M_{g_i,n_i}/S_{n_i}.
    - By PR-A (entry 19, as quoted in R8-3 §0), t ↦ Y_t ∈ M_{g_i,n_i} is itself holomorphic.
    - If [Y_t] ≡ [Y_0], then Y_t lies in the finite set S_{n_i}·Y_0.
    - A continuous map from the connected Δ into a finite set is constant, so Y_t = Y_0. ✓

## 6. §6: Theorem LG and the reading (Loc)

**"Why (Loc) is the chart-level reading" — (Rep-5).**
- The inclusion Stab(h_s u) ⊂ φ(Stab u) is proved for elements b in the image of φ, i.e. b ∈ Stab(h_{t_0} x̂). To get equality of the **full** Mod_G-stabilisers, shrink W and I so that h((W ∩ Ã_0) × I) ⊂ W′. Here W′ is a slice neighbourhood of h_{t_0}(x̂) with gW′ ∩ W′ ≠ ∅ ⇒ g ∈ Stab(h_{t_0} x̂), and W is a slice neighbourhood of x̂ of the same kind.
- Then every b ∈ Mod_G fixing h_s(u) lies in Stab(h_{t_0} x̂), and every a ∈ Mod_G fixing u lies in Stab(x̂). So Stab_{Mod_G}(h_s u) = φ(Stab_{Mod_G}(u)), and (L2) holds.
- The sentence "φ is independent of s by continuity, since the set of isomorphisms is discrete" is not a deduction. The equivariance relation determines φ_s(a) only modulo the pointwise stabiliser of h_s(W ∩ Ã_0), which can be non-trivial on a 1-dimensional Ã_0. So "a single φ for all s ∈ I" has to be part of the reading of "continuous family of orbifold maps", not a consequence of it. This does not affect Theorem LG, which assumes (L1), (L2) directly.

**Lemma U.**
- E is closed (T_G is Hausdorff).
- E is open: use the slice neighbourhood U of y, the fact that fibres of ξ_G∘p are Mod_G-orbits, g_s ∈ Stab(y), and local constancy of Stab(γ_1(s)). ✓
- Only γ_1 needs locally constant stabiliser.

**Construction.**
- (Loc) at (x, τ_j) gives lifts h^j of H_s for s ∈ I_j, defined on neighbourhoods of the **same** x ∈ Ã_0 (the domain is at time 0). So the gluing is meaningful. ✓
- The normalisation h^1_0(x) = a x is correct, since H_0 = id. ✓
- The stabiliser is constant on each closed piece by (L2), and the values agree at the junctions. ✓
- Uniqueness follows from Lemma U. ✓

**(a)–(d) and uniqueness of H̃.** ✓ For (b), g∘γ_{x,t} lifts the same path, starts at gx, and has locally constant stabiliser, so it is γ_{gx,t} by Lemma U.

**Joint continuity.**
- j = 1: x and a_x x both tend to x_0, so a_x ∈ Stab(x_0) by proper discontinuity. ✓
- Induction: K_j = Stab(y_0) = K_{j+1}, and the two candidates lie in a common slice neighbourhood of y_0 over the same point. So they differ by k′ ∈ Stab(y_0), and Lemma U applies on [r_j, r_{j+1}]. ✓
- Final step: k ranges in a finite group fixing H̃_{t_1}(x_0). ✓
- **Theorem LG is correct.**

**(Rep-4): the closing remark "(Loc) only near t_0 = 0 suffices" is not proved.**
- (Loc) at (x̂, 0) gives a disc I(x̂) whose radius depends on x̂. Ã_0 is not compact modulo Mod_G: A_0 accumulates on smaller strata at the punctures of the pieces. So there may be no common r > 0 with (a)–(d) on Ã_0 × Δ_r.
- Theorem RO needs H̃ on all of Ã_0 for each t considered (Lemma 1.1's surjectivity and the piece transport), so a non-uniform radius does not suffice as written.
- The disc-size caveat in that remark is itself harmless: rescaling t ↦ rt yields an admissible family over Δ, and entry 19 propagates the identity Y_t ≡ Y_0. Uniformity of the radius is the real issue.
- The remark is correct if (Loc) is assumed at all (x̂, t_0) with |t_0| < r for a fixed r > 0. The main Theorem assumes (Loc) at all t_0 ∈ Δ and is unaffected.

## 7. §7: is (R2^orb) a faithful formalisation?

**(Rep-6): the claim must be qualified.**
- "Orbifold reading" admits two inequivalent precise forms.
- **(O-emb), the embedded / substack reading.** A_t is the reduced closed substack of the stack Δ_G = [T_G/Mod_G], so its isotropy at z is the full Aut(z). The trivialisation is an isomorphism of substacks over Δ, i.e. local lifts equivariant through **isomorphisms of the ambient local groups** Aut(z) → Aut(H_t z).
  - Under (O-emb), (L1)+(L2) hold, by the computation above with (Rep-5). Theorem LG then gives (a)–(d).
  - So **(R2^orb) is faithful to (O-emb).** ✓
- **(O-int), the intrinsic reading.** Each A_t (and V_t) is given its own effective orbifold structure, and H_t is an orbifold diffeomorphism A_0 → A_t of these intrinsic structures. Equivalently, an orbifold map into Δ_G whose local group homomorphisms need not be onto, or injective, on the ambient groups.
  - (O-int) is strictly weaker than (O-emb).
  - **The §7 example satisfies (O-int).** σ : u ↦ −u fixes the curve {u = 0} pointwise, so the intrinsic (effective) isotropy of that curve is trivial. The transported curve {u = ±t}/σ is a smooth curve with trivial intrinsic isotropy. Hence H_t is an intrinsic orbifold diffeomorphism (of trivial orbifolds), while (c) fails.
- So the correct statement is:
  - **(R2^orb) ⇔ (O-emb) ⊊ (O-int) ⊆ coarse (R2)**, at least locally. The first equivalence ⇐ is Theorem LG; ⇒ holds by definition.
  - The Theorem settles the problem under (O-emb) only.
- The problem's wording ("smooth subvariety of M_g", "complex submanifold 𝒱 ⊂ M_g × Δ", "smoothly trivial family") does not choose among these. As §7 itself says, the literal wording leans towards the coarse reading.

**The example itself.**
- The coarse chart is smooth (U = u²).
- H_t(U, v) = (U + t², v) is holomorphic, stratum-preserving and smooth, so it is (R2)-admissible at chart level.
- |Aut(H_t z)| < |Aut(z)| for t ≠ 0, so (c) fails.
- The non-existence of a lift with (a) and (c) follows directly by counting stabiliser orders. Lemma U is not even needed.
- It is a chart-level model only, as stated. Whether a global admissible family with such an isotropy drop exists is open. ✓

**"Compatibility (ii) is not needed beyond (R2)."** Correct as a statement about the proof. But (ii) is one of the problem's hypotheses that (R2) is meant to encode; see §1 above.

---

## §V. Verdict, repairs, remaining dependencies

### Verdict
**Round13_q10, together with the cited inputs, proves the conditional theorem exactly as stated:** under (R1) and (R2^orb) — equivalently, by Theorem LG, under (R1), (R2) and (Loc) at all (x̂, t_0) ∈ Ã_0 × Δ — Y_t = Y_0 for all t ∈ Δ.
- The new parts are Lemma 3.1, Lemma 3.2, Prop. 3.3, Lemmas 4.1–4.2, Prop. 4.3, the chain bookkeeping of §5, and Theorem LG. I checked every inference in them and found them valid, with the minor repairs below.
- The key mechanism is sound: (c) + Lemma 3.2 + (Kur) ⇒ the lift locus is a single Aut(Q)-fixed curve, so every anchored sheet contains it, and persistence transfers through it.
- The conclusion π_i(∂V_t) = {Y_0} follows with (Rep-3).
- Not established by round13_q10 as written:
  - the §6 closing remark (Rep-4);
  - the unqualified claim in §7 that (R2^orb) is "the" orbifold reading (Rep-6).

  Neither is needed for the theorem.

### Repairs (all supplied above)
- **(Rep-1)** Lemma 3.2 remark: the (2,0) and (1,2) examples of K_G are wrong. Correct examples are given. Not used anywhere.
- **(Rep-2)** Endpoint: if the MOV witness lies outside the shrunken ball, propagate along b̃ by the identity theorem (as in round11_q9 §2.8).
- **(Rep-3)** From [Y_t] constant to Y_t constant in M_{g_i,n_i}: holomorphy of Y_t (PR-A), finiteness of S_{n_i}-orbits, and connectedness of Δ.
- **(Rep-4)** The §6 remark "(Loc) near t_0 = 0 suffices" is unproved: radii of (Loc) are not uniform on the non-compact A_0. It is valid if (Loc) holds on a fixed disc Δ_r (then rescale).
- **(Rep-5)** "Why (Loc)": shrink to slice neighbourhoods to get equality of the full Mod_G-stabilisers. The constancy of φ in s is part of the reading, not a deduction.
- **(Rep-6)** §7: (R2^orb) is faithful to the embedded/substack orbifold reading (O-emb), not to the intrinsic one (O-int). The §7 example satisfies (O-int) but violates (R2^orb).

### Remaining unchecked dependencies (from round13_q10 §8.2, confirmed and completed)
1. **Standing readings:** (R1), and (R2) as one global stratum-preserving homeomorphism encoding (i)+(ii). Also the choice (O-emb) for (R2^orb).
2. **Theorem RO inputs:**
   - round8_q10 Theorem TV (items 1–4; by round13_q9 §3.1(d), item 2 reduces to properness of p_E) and Corollary Φ̂;
   - Lemma PA / Lemma TR (positive area at the vertex j), which round8_q10 itself cites from memory;
   - round13_q9 repairs (R1′), (R2′), (R3′);
   - Imayoshi–Shiga finiteness for punctured types (scope from memory; types (1,1) and (0,4) are covered by hyperbolic-curve rigidity instead).
3. **Chain (round11_q9):**
   - entries 85, 98, 112, 113 (walk chain, Gap A / R(D) repair, including the "routine" marking-continuity detail along travel intervals);
   - Lemma S̃′, Theorem X*_all (via Lemma P with (Res)/(Neg)/(RA)), Cor. IMOV_all (entries 97, 99);
   - Lemma B1♭;
   - Lemma PT, Lemmas T, S, J, Theorem R (entries 84, 86, 87);
   - the cited inputs listed in round11_q9 §4 (Lemma NH, (Fl), (Prop), Kerckhoff, Maskit, Wolpert/Abikoff, T̄_g/Def chart description, Milnor conic structure).
4. **Run lemmas used in §4:**
   - Theorem N and Lemma 1 of R8-3;
   - R7-4 Lemma 2 (closure(Ñ_c̃) ⊂ Ñ_c̃ ∪ 𝒥, pure dimension 2);
   - R8-2 Lemma U / Theorem 1 (through the chain);
   - entries 19 (PR-A) and 24.
5. **Classical results cited from memory:**
   - Deligne–Mumford local structure (Kur), in the stack form Stab_{Aut(Q)}(p) ≅ Aut(X_p);
   - proper discontinuity of Mod_G and slice neighbourhoods;
   - connectedness of Reg of an irreducible germ;
   - Hurewicz–Wallman non-separation;
   - invariance of domain;
   - normalisation of curves;
   - Remmert;
   - Krull;
   - Chow;
   - the classical inputs of RO (Royden, Earle–Kra, Bers, Thurston, Selberg, orbifold uniformisation, Bers embedding, Cartan).

### Open (named)
- The problem under the coarse reading (R2), and under the intrinsic orbifold reading (O-int). Both (Rig) and MS11♭ are open there, and the obstruction is isotropy drop at boundary points.
- Existence of a global admissible family (satisfying (i), (ii)) with isotropy drop at the boundary.
- The exact scope of Imayoshi–Shiga for punctured types.
- Whether (Loc) near t_0 = 0 alone (with non-uniform radii) implies (a)–(d) on some Δ_r × Ã_0.

=== END OF ANSWER round14_q9 ===
