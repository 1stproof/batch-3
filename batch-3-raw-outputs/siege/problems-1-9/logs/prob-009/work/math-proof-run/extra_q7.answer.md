# Referee report on Theorem 7.5, Corollary C.5, Lemmas F0/F1, Proposition Ψ

Plan: check the four proofs one step at a time (done in my reasoning; written up below section by section), give full repairs for every gap, then list citations that look misstated. Everything below was checked by hand; I had no code execution, and all literature facts are cited from memory.

## Summary table

| Result | Verdict | One-line reason |
|---|---|---|
| Theorem 7.5 (with Lemma 7.1, Lemma 2.5, Prop. 5.1) | correct with minor repairs | Path lifting, uniqueness, constant stabilisers, (P1), (P2)(i)–(v) and joint continuity all hold. There are two wording gaps: (1) in Step 1, translates must pass through points over c(r_{l-1}), not only over c(r_*); (2) in Step 3, the slices U_j come from a Lebesgue cover and need not be centred at γ_0(r_j). Both are fixed by the observation that a slice for one point of the K-fixed path is a slice for every point of it. Neither (Loc) nor anything beyond (AP) and (R2) is used. |
| Corollary C.5 | correct (conditional on Thm 7.5, Thm A, Lemma 2.3) | Z is closed (Kuranishi charts), and the uniformity in Step 2 follows correctly from compactness of B_0 and uniform continuity of H. The extension from a small disc rests entirely on Lemma 2.3, which is not under review. |
| Lemmas F0, F1 (with F1.1, F1.2) | correct with minor (presentational) repairs | Riemann–Hurwitz bounds are right. The pairs group L avoids Birman–Hilden; nothing uses injectivity of L → Mod(Y_0). Γ_1 is torsion-free, Υ is locally injective with finite fibres, and Step 6 is right. One ordering issue: §0 and Step 1 use that T → M is a covering, i.e. torsion-freeness of Mod_{h,m}[N], which is only proved in Step 2d. |
| Proposition Ψ with Lemma S | correct with one repair | The formulas are right: Case 1 (cosh s_a − cosh s_0), Case 2 (ξ_2 = α coth(x/2), the condition e^{σ_1} ≥ R, and the factorisation). The hexagon maps satisfy (H1)–(H3), and the gluing is consistent. The "marking identification" step is only sketched; a short rigorous replacement (a geodesic homotopy inside the hexagons) is given. The uses of (Prop) and (Th) in (c) are within scope. |

No fatal error was found in any of the four results.

---

## 1. Theorem 7.5 (with Lemma 7.1, Lemma 2.5, Proposition 5.1)

### Lemma 2.5 (Stab ≅ Aut)
- **Step 1 (the homomorphism).** Correct. g fixes x̂ iff, for each w, (C_w, f_w∘φ_w^{-1}, relabelled points) is equivalent to (C_{σ(w)}, f_{σ(w)}). That means there is a biholomorphism α_w : C_w → C_{σ(w)}, isotopic rel points to f_{σ(w)}∘φ_w∘f_w^{-1}, that sends the point labelled h to the point labelled σ(h).
  - Uniqueness of α_w: if α, α′ are two such maps, then α′^{-1}α is an automorphism of the stable pointed curve C_w isotopic to the identity rel marked points. Since 2g_w − 2 + n_w > 0 it is a hyperbolic isometry homotopic to the identity, hence the identity. So (Iso) is correctly stated and used.
  - Because σ respects the involution on half-edges, ⊔α_w identifies node preimages compatibly and descends to Z.
  - Composition: α(gg′) = α(g)α(g′), directly from the action formula.
- **Step 2 (injective).** Correct. Lifts of automorphisms to the normalisation are unique (functoriality). If the lift is the identity, then σ(w) = w, α_w = id and σ(h) = h, so φ_w ≃ f_w^{-1}∘f_w = id.
- **Step 3 (surjective).** Correct. σ preserves genera and the half-edge involution, because α maps nodes to nodes.
- **Remark on K_G.** The two listed examples are genuine elements of K_G. The list is not exhaustive: for example, a (0,4)-vertex whose four half-edges form two self-loops (a stratum of M̄_2) carries a Klein-four element acting trivially. The remark only says "correct examples" and is unused, so this is harmless.

### Proposition 5.1
Correct.
- x̂ exists by (St2).
- Q_t ∈ Δ_{G_Q} by (R2).
- (a) gives P(ŷ) = Q_t; then Lemma 2.5 together with (c) gives the conclusion.
- Only (a) and (c) for G = G_Q are used.

### Lemma 7.1
Correct.
- E is closed because T_G is Hausdorff.
- E is open: near s_1 both paths lie in the slice U of y; γ_2(s) = g_sγ_1(s) by (St2); g_s ∈ Stab(y) by the slice property; and Stab(γ_1(s)) = Stab(y) by local constancy, so g_s fixes γ_1(s).
- Only γ_1 needs a locally constant stabiliser. γ_2 is arbitrary, so uniqueness actually holds among **all** continuous lifts, which is stronger than what Step 1 of 7.5 states.

### Step 0, (P1)
Correct.
- p is the orbit map of a group action, so it is open.
- ξ_G : ∏M_w → Δ_G is finite. It is the restriction of ξ̄_G to ξ̄_G^{-1}(Δ_G) = ∏M_w: a tuple with a nodal coordinate glues to a curve with strictly more nodes, so it is not in Δ_G. Hence ξ_G is proper, and so closed.
- A closed continuous surjection is a quotient map. For O open, ξ_G^{-1}ξ_G(O) = ∪_{σ∈Aut(G)} σO is open, so ξ_G is open.
- Hence P = ξ_G∘p is open and continuous, and its fibres are the Mod_G-orbits by (St2).
- Surjectivity of Mod_G → Aut(G) in (St3) holds because Σ_w and Σ_{σ(w)} have the same type.

### Step 0, (P2)
- **(i)** Correct. If gU ∩ g′U ≠ ∅, then g^{-1}g′ ∈ A, and A-invariance of U gives g′U = gU. P(U) is open by (P1).
- **(ii)** Correct.
- **(iii)** Correct. U → P(U) is continuous, open (it is a restriction of P to an open set), surjective, and its fibres are A-orbits, so it is a homeomorphism U/A ≅ P(U). A finite-group quotient X → X/A is closed (the saturation ∪aF of a closed set is closed) and has finite fibres, so it is proper.
- **(iv)** Correct, since the groups are finite and Stab(u) ⊂ A.
- **(v)** Correct.
  - Injectivity: two points of U with the same image differ by an element of A, which fixes both.
  - A closed map restricted to a closed subset is closed, so P|Fix(A)∩U is a closed continuous injection, i.e. a homeomorphism onto its image.
  - Characterisation of the image: for z = P(u) with u ∈ U, Lemma 2.5 gives |Aut z| = |Stab u|; by (ii) and (iv), |Stab u| = |A| iff u ∈ Fix(A). This is independent of the choice of u in its A-orbit.

### Step 1 (path lifting at constant isotropy order)
- **Local sections.** Correct.
  - D_k := {z ∈ P(U) : |Aut z| = k} = P(Fix(A) ∩ U), and σ = (P|_{Fix(A)∩U})^{-1} is continuous on D_k.
  - c(r) ∈ P(U) for r near r_* (P(U) is open), and |Aut c(r)| = k by hypothesis, so c(J_{r_*}) ⊂ D_k.
- **Gap (wording, repairable).** The text says "through every point over c(r_*) passes one of these sections". The existence step needs a translate through the point already constructed over c(r_{l−1}), which is a different base point. Repair: for any r ∈ J_{r_*}, the points over c(r) form the orbit Mod_G·σ(c(r)) by (P1). So for any x′ ∈ P^{-1}(c(r)) there is g with x′ = gσ(c(r)), and gσ is a continuous section over D_k through x′. With this the existence step is correct, and the pieces agree at the junctions by construction.
- **Constant stabiliser.** Correct. Near r_1, γ(r) lies in a slice of γ(r_1). By Lemma 2.5, |Stab γ(r)| = |Aut c(r)| = k = |Stab γ(r_1)|, so (iv) gives equality. So the stabiliser is locally constant, hence constant on [0,1].
- **Uniqueness.** Correct by Lemma 7.1, and indeed it holds among all continuous lifts.

### Step 2 (definition of H̃ and (a)–(d))
Correct.
- P(x) ∈ A^G_0 ⊂ B_0, because G is a boundary stratum.
- (R2) gives c_{x,t}(r) = H_{rt}(P x) ∈ A^G_{rt} ⊂ Δ_G, and c_{x,t} is continuous.
- (AP) gives the constant order |Aut P(x)|.
- γ(1) ∈ P^{-1}(A^G_t) = Ã_t.
- (a), (c), (d) are immediate.
- (b): g∘γ_{x,t} is a continuous lift of c_{gx,t} = c_{x,t} starting at gx, so by uniqueness it is γ_{gx,t}.

### Step 3 (joint continuity)
- **Gap (repairable): choice of the U_j.** A Lebesgue-number argument on the cover {γ_0^{-1}(U(r))}_r gives a partition with γ_0([r_j, r_{j+1}]) ⊂ U(r′) for some r′, where U(r′) is a slice of γ_0(r′). It does **not** give a slice centred at γ_0(r_j), which is what the text asserts. Repair: every γ_0(r) has the same stabiliser K (Step 1). "Slice neighbourhood of y" in (St1) refers only to Stab(y): it means a Stab(y)-invariant open set with gU ∩ U ≠ ∅ ⇒ g ∈ Stab(y). So U(r′), if it contains γ_0(r_j), is a slice neighbourhood of γ_0(r_j), and also of γ_0(r_{j+1}). Take U_j := U(r′). Everything used later holds for this U_j: (P2)(i), (P2)(iii), and "the A-orbit of γ_0(r_{j+1}) is a single point" (A = K fixes it).
- **Uniform convergence.** Correct. H is uniformly continuous on the compact set closure(V_0) × {|s| ≤ (1+|t_1|)/2}, and c_{x,t}(r) = H(Px, rt).
  - The containment c_{x,t}([r_j, r_{j+1}]) ⊂ P(U_j) needs a small point. P(U_j) is open in Δ_G, i.e. P(U_j) = O ∩ Δ_G with O open in M̄_g. The compact set c_0([r_j, r_{j+1}]) is at positive distance from M̄_g ∖ O, and every c_{x,t} lies in Δ_G. This is implicit in the text and fine.
- **Induction.** Correct.
  - Connectedness of γ_n([r_j, r_{j+1}]) inside the disjoint union ⊔gU_j forces containment in U_j.
  - Properness of U_j → P(U_j): {c_n(r_{j+1})} ∪ {its limit} is a compact subset of P(U_j), so its preimage in U_j is compact.
  - Limit points lie over P(γ_0(r_{j+1})), i.e. in the K-orbit of γ_0(r_{j+1}), which is a single point.
- **Conclusion.** Sequential continuity suffices, since Ã_0 × Δ and T_G are metrisable.

### Does anything use (Loc), or more than (AP)?
No. The proof uses (R2) (stratum preservation, continuity, H_0 = id), (AP) only at points P(x) ∈ B_0, and (St1)–(St4) and Lemma 2.5. The equivalences in Step 4 are correct:
- (R2^orb) ⇒ (AP) by Prop. 5.1;
- (R2^orb) ⇒ (Loc) with h := H̃.

**Verdict: correct with the two minor repairs above.**

---

## 2. Corollary C.5

### Step 1 (Z is closed)
Correct.
- In a (Kur) chart, q(p) ∈ Z iff Stab_{Aut(J)}(p) ≠ 1 iff p ∈ ∪_{a≠1} Fix(a).
- Each Fix(a) is closed, and the union is finite.
- q : B → q(B) ≅ B/Aut(J) is a finite-group quotient map, hence closed.
- Closedness is local and the q(B) form an open cover, so Z is closed.

This remains correct when Aut(J) acts non-effectively on Def(J), as in genus 2, where the hyperelliptic involution acts trivially: then Fix(ι) = B, consistent with Z = M̄_2. The (Kur) statement "Stab_{Aut(J)}(p) ≅ Aut(X_p) for B small" is the standard one (openness of versality plus specialisation of automorphisms), and I consider it correctly cited.

An alternative is to say that |Aut| is upper semicontinuous by the same chart.

### Step 2 (uniformity)
Correct.
- B_0 = closure(V_0) ∩ ∂M̄_g is compact, and Z is closed and disjoint from it, so the distance δ between them is positive.
- H is uniformly continuous on the compact set B_0 × {|t| ≤ 1/2}, and H_0 = id. So there is r ≤ 1/2 with d(H_t z, z) < δ for all z ∈ B_0 and |t| < r.
- The uniformity in z comes exactly from compactness of B_0. This is the point where the general case fails, as Remark C.6 correctly explains: upper semicontinuity gives only |Aut H_t z| ≤ |Aut z|.

### Step 3
Correct, given the cited results.
- The rescaled family t ↦ V_{rt} satisfies (R1) and (R2) with H′_t = H_{rt}, and it satisfies (AP) on its whole parameter disc.
- Theorem 7.5 and Theorem A then give Y_{rt} = Y_0 for |t| < 1.
- Passing from |t| < r to all of Δ rests **entirely** on Lemma 2.3, which is not under review. Lemma 2.3 is not quoted in the excerpt, so I can only flag that C.5 depends on it.
- The dependence cannot be avoided by rebasing at t_1 ≠ 0, because V_{t_1} need not be totally geodesic.

### Remark C.6
Correct.
- An elliptic tail carries the involution fixing its attaching point, and this extends by the identity.
- In genus 2 the hypothesis of C.5 never holds, because every curve is hyperelliptic.

**Verdict: correct (conditional on Theorem 7.5, Theorem A and Lemma 2.3).**

---

## 3. Lemmas F0 and F1

### Lemma F0
- **(a) Big Picard.** Correct. f omits 0 and 1 on a punctured disc, so it has no essential singularity. Hence f̄ : R̄ → P¹ is holomorphic, and f̄^{-1}{0,1,∞} ⊂ P.
- **Riemann–Hurwitz.** I rechecked the computation. Σ_{f̄^{-1}{0,1,∞}}(e_p − 1) = 3d − #f̄^{-1}{0,1,∞} ≥ 3d − k. Then 2h − 2 = −2d + Σ_p(e_p − 1) ≥ d − k, so d ≤ 2h − 2 + k.
  - Consistency checks: for h = 0, k ≤ 2 there are no maps, which is right since C and C^* are not hyperbolic. For P¹ ∖ {0,1,∞} we get d ≤ 1, giving the 6 Möbius maps.
- **Divisors and constants.** Correct.
  - The divisor of f̄ is supported in P and has bounded degree, so there are finitely many possibilities.
  - f̄ = c f_0. At a point p ∈ P with f̄(p) = 1, f_0 has neither a zero nor a pole (the divisors agree), so c = 1/f_0(p).
- **(b).** Correct.
  - M_{0,n} is the stated open subset of C^{n−3}, so holomorphic maps are tuples of holomorphic coordinates.
  - A constant coordinate avoids x_l(R) ⊃ P¹ ∖ x̄_l(P).
  - Taking l to be the first non-constant index makes the choices finite.

**Verdict on F0: correct.**

### Lemma F1.1 (closed case)
- **Step 1.** Correct.
  - (TF) gives a free action, hence a free action on the Teichmüller curve, and the quotient is a proper holomorphic submersion.
  - The description of points as (X, α): two markings inducing the same α differ by an element of Mod_g[N′].
- **Step 2.** Correct.
  - If B → M_g were constant, F would take values in a finite fibre, and since B is connected F would be constant.
  - Constancy on an open set propagates by the identity theorem for maps into the manifold M_g[N′], applied after composing with the finite map. So F^*C is locally non-trivial in the sense of (IS_c).
- **Step 3.** Correct.
  - σ(b) ∈ Sp(2g, Z/N′) because Θ_b is a biholomorphism, so it preserves the intersection form. σ is continuous because everything is a section of a finite covering, hence constant.
  - Then F_2(b) = (X^{(2)}_b, α_2(b)) ≅ (X^{(1)}_b, Θ_b^{-1}α_2(b)) = (X^{(1)}_b, α_1(b)σ).
- **Step 4.** Correct.

### Step 2a
Correct.
- π is free of rank 2h + m − 1 ≥ 2.
- Each c_j ≠ 1; even for m = 1, c_1 is a product of h ≥ 1 commutators, non-trivial in a free group.
- A finitely generated group has finitely many subgroups of index ≤ d, so K is characteristic, of finite index, and contains no c_j.

### Step 2b
Correct.
- The subgroup is canonical because K is characteristic: any two identifications π ≅ π_1(X ∖ P_X) differ by an automorphism of π, including basepoint changes.
- Riemann–Hurwitz, rechecked: 2h′ − 2 = |G|(2h − 2) + Σ_j (|G|/n_j)(n_j − 1) = |G|(2h − 2 + Σ_j(1 − 1/n_j)) ≥ |G|/2 > 0. So h′ ≥ 2.

### Step 2c (pairs, Birman–Hilden)
Correct.
- Well-definedness of Φ also requires that equivalent marked curves have the same image. A conformal c : X → X′ with c∘φ ≃ φ′ lifts to a conformal Y_X → Y_{X′}. This is omitted but trivial.
- Kernel of L → PMod. A representative of the trivial class is isotopic rel P to the identity. The isotopy lifts, so its lifts are isotopic to deck transformations. Conversely, every deck class occurs. So the kernel is {(1, g)} ≅ G; G injects into Mod(Y_0) because h′ ≥ 2.
- **Nothing uses Birman–Hilden.** Birman–Hilden would be needed for injectivity of the second projection, i.e. that a lift isotopic to id forces ϑ = 1, and this is explicitly not used. Injectivity of Φ comes from (BC), the Bers-model inclusion of Beltrami coefficients, which also does not use Birman–Hilden.
- Equivariance: Φ(ϑp) = [Y_X, φ̃∘ϑ̃^{-1}] = ϑ̃Φ(p).
- (BC) sketch, checked:
  - Γ_Y = ker(Γ_0 → G) is torsion-free, because each elliptic generator maps to an element of exactly its order n_j.
  - T(Γ_0) ≅ T_{h,m} by Bers–Greenberg.
  - The inclusion is injective because the relation w^μ|_ℝ = w^ν|_ℝ is the same for Γ_0 and Γ_Y.
  - The inclusion is holomorphic via the linear inclusion B_2(Γ_0) ⊂ B_2(Γ_Y).
  - The one step not spelled out is that the Bers-model map agrees with the lift-defined Φ under the marking identifications. This is standard (it is MacLachlan–Harvey's construction), and I accept it as cited.

### Step 2d
Correct.
- Λ has finite index in L.
- Λ ∩ ker(first projection) = {(1, g) : g ∈ G ∩ Mod(Y_0)[N′]}. This is trivial because G consists of finite-order elements and Mod(Y_0)[N′] is torsion-free.
- So Λ ≅ Γ″, and [PMod : Γ″] ≤ [L : Λ].
- Γ_1 (the normal core of Γ″ ∩ Mod_{h,m}[N]) is normal, of finite index, and contained in Mod_{h,m}[N].
- **Torsion-freeness of Mod_{h,m}[N].**
  - Nielsen realisation for cyclic groups gives a conformal f of finite order on some (X, P_X). f fixes each marked point because the class is pure.
  - Serre's lemma for genus ≥ 2 gives f = id. In genus 1, f fixes a marked point, so f ∈ Aut(E, 0) ⊂ μ_6, and every non-trivial element acts on H_1(E; Z/N) by a matrix ≢ I for N ≥ 3. (−1 gives −I; the order-3, 4, 6 elements have trace ∈ {−1, 0, 1} ≢ 2 mod N, or are ≠ I mod N directly.) So f = id.
  - The stated genus-≥1 form of (TF) is correct.
- M_1 → M is a finite unramified covering. Υ is well defined and holomorphic.

**Ordering remark (presentational).** §0 lifts maps to the universal cover and Step 1 of §3 says "Mod_{h,m}[N] acts freely as deck group". Both need Mod_{h,m}[N] to act freely, i.e. the torsion-freeness argument of Step 2d (finite stabilisers plus torsion-free gives free). That argument does not depend on §0 or §3, so there is no circularity. It should simply be moved before §0.

### Lemma F1.2
- **(a)** Correct. Υ∘proj = proj∘Φ on U, and this is injective because Φ is injective and proj is injective on W.
- **(b)** Correct.
  - Equal images give Y_q ≅ Y_p via some c.
  - X_q = Y_q/G_q ≅ Y_p/(cG_qc^{-1}), and the marked points go to branch points.
  - Aut(Y_p) is finite (Hurwitz), there are finitely many subgroups and labellings, and the fibres of M_1 → M_{h,m} have at most [PMod : Γ_1] points.
  - Notational slip: "Σ_q" should read X_q.

### §3, Steps 1–6
- **Step 1.** Correct, given free action. ρ_f(γ) is locally constant by discreteness of orbits, hence constant, and it is a homomorphism.
- **Step 2.** Correct. Q is finite and Π is finitely generated, so there are finitely many kernels.
- **Step 3.** Correct. H has finite index, so R′ has finite type and is hyperbolic. f̃ descends because ρ_f(H) ⊂ Γ_1, and f is recovered from f′ via q∘f′ = f∘p_H.
- **Step 4.** Correct. Orbits of a properly discontinuous action are discrete, D is connected, and Φ is injective.
- **Step 5.** Correct: Lemma F1.1 with g = h′ ≥ 2 and N′ ≥ 3.
- **Step 6.** Correct.
  - The coincidence set is clopen by local injectivity of Υ.
  - Distinct lifts take distinct values at r_0, inside a finite fibre.
  - The bound is #{f} ≤ Σ_H Σ_{F′} #Υ^{-1}(F′(r_0)).

**Sanity check of the statement.** Take h = 1, m = 2, so M_{1,2}[N] is the universal elliptic curve minus the zero section over Y(N). Maps that are constant to a point E of Y(N) and non-constant in the fibre E ∖ {0} could a priori come in infinite families as E varies. They do not:
- Such a map extends to ψ : R̄ → E with ψ^{-1}(0) ⊂ P.
- Riemann–Hurwitz with a genus-1 target gives deg ψ ≤ 2h_R − 2 + k.
- I expect only finitely many (E, ψ) of bounded degree to exist. This is a heuristic remark, not proved here and not needed: the proof of F1 does not go through it.

So this is consistent with the lemma.

**Verdict on F1: correct, with the ordering fix.**

---

## 4. Proposition Ψ with Lemma S

### Conventions
- The identity ℓ_β(X|Σ′) = ℓ_β(X) holds. Σ′ is incompressible, X|Σ′ is convex with geodesic boundary, and the closed geodesic of a non-peripheral β ⊂ Σ′ cannot cross the γ_j.

### Proof of (a)
Correct.
- Continuity: ψ = Φ_{P′}(0,·) ∘ (projection to P′-coordinates).
- Naturality: correct.
- Twists about curves disjoint from int Σ′ can be supported in annuli outside int Σ′. Then h|_{Σ′} = id, so the seams, the P′-coordinates and the marking of X|Σ′ are unchanged.

### Lemma S, reduction to hexagons
- **Gluing.** Correct.
  - Using σ_0 f σ_a on H̄ agrees with f on the seams, since f maps seams into seams and σ fixes seams pointwise.
  - On interior cuffs the map is "the identity in the arclength coordinate with the seam feet as origin" from both adjacent pants, and both surfaces have the same (ℓ_α, τ_α). So the twist-gluings match.
  - Pants of the form (γ, α, α), Case 1 with x = y, are also consistent.
- **Locally 1-Lipschitz.** Correct. A geodesic segment meets each geodesic hexagon side in a point or a subarc, and hexagons are convex, so intrinsic and ambient distances agree.
- **Marking identification.** This is only sketched ("homotope a loop off the boundary sides … image loop freely homotopic"). It is believable, but the claim that arcs in a hexagon go to arcs "with endpoints on the same seams/half-cuffs" does not by itself define a homotopy. **Repair (rigorous):**
  - Let Ψ_0 : Φ(b,c) ∖ ∂ → Φ(0,c) be the reference homeomorphism defining the marking identification. It is built from hexagon homeomorphisms H_a ∖ (a-sides) → H_0 that map each seam onto the same seam and each interior half-cuff isometrically onto itself, fixing the seam feet, and it is extended by reflection.
  - Define F_s(z), s ∈ [0,1], as the point at parameter s on the geodesic segment from Ψ_0(z) to F(z) inside the hexagon H_0 containing both points (H_0 is convex).
    - On a seam, both endpoints lie on that seam, which is a geodesic arc or ray. So the segment stays in the seam, which is fixed by the reflection, and the definitions from H and H̄ agree.
    - On interior half-cuffs F = Ψ_0, so the homotopy is constant there and the twist-gluings match.
  - Hence F ≃ Ψ_0 on Σ′ minus an open collar of ∂Σ′. This is a deformation retract of Σ′, so F∘β ≃ Ψ_0∘β for every closed curve β.
- **Length inequality.** Correct. In the cusped surface a non-peripheral class has a geodesic, which minimises length.

### Case 1 (one boundary side)
I rechecked every formula.
- **(Hex).** The side opposite a satisfies cosh s = (cosh a + cosh x cosh y)/(sinh x sinh y). So cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0. ✓
- **Fermi picture.** The hexagon lies in the strip 0 ≤ τ ≤ s, because it lies on one side of the x-line and of the y-line, which are the fibres τ = 0 and τ = s.
- **Monotone projections.** Projection onto a line is injective along any geodesic that is not perpendicular to that line. Disjointness, which (Hex) adds, is not needed. The perpendicularity exclusions are right:
  - s_{ax} meets the x-fibre, so it is not itself a fibre.
  - If the a-line were a fibre, it, s_{ax}, x and s_{xy} would form a quadrilateral with four right angles, which is impossible.
  - The concatenated top path projects injectively by convexity (each fibre has a single top point), hence monotonically.
- **x-placement.** Correct. Both s_{ax}-lines are the perpendicular to x at its top endpoint, on the same side. Along H_0's ray the projection increases from 0 towards u_1′ without reaching it. So τ_C < u_1′. Likewise s_a − τ_D < u_2′.
- **Cut.** Correct. τ_C < u_1′ < u, and τ_D > s_a − u_2′ = u_1′ + 2d > u, so the fibre τ = u ends on the side a.
- **Map on P_1.** Correct.
  - The x-side and s_{ax}(H_a) ⊂ ray s_{ax}(H_0) lie in Q_1, so they are fixed.
  - Base points with u_1′ < τ ≤ u go to B′ ∈ Q_1. The nearest point in the half-plane lies in Q_1, so it is the nearest point of Q_1.
  - Points of c go to their feet on the ω′-line. By the symmetry under reflection in the s_{xy}-line, the foot lies on the upper half-line, which is all of ω′ ⊂ Q_1. Its height is p(h, d) by invariance under translation along s_{xy}.
- **Map on P_2.** Correct. The distance from W to c is s_a − u = u_2′ + d, which is again d beyond ω′. So both definitions send a point at height h on c to the point at height p(h, d) on ω′, and f is well defined and continuous.
- **1-Lipschitz.** Correct. A geodesic crosses c at most once, and distances in H_0 are intrinsic by convexity.
- **(H2), (H3).** Both hold.

### Case 2 (two boundary sides)
I rechecked every formula.
- **x-side.** d(iα, αe^{iφ}) = arccosh(1/sin φ). Also cosh(log cot(φ/2)) = 1/sin φ. So cot(φ/2) = e^x, sin φ = 1/cosh x and cos φ = tanh x. ✓
- **L_2.** The circle orthogonal to |z| = α at A_2 has its centre c on ℝ with (A_2 − c)·e^{iφ} = 0. So c = α/cos φ and r = √(c² − α²) = α tan φ. ✓
- **ξ_2.** The outer endpoint is ξ_2 = α(1 + sin φ)/cos φ = α(cosh x + 1)/sinh x = α coth(x/2) > α. ✓ The other endpoint lies inside |z| = α, on the wrong side of x.
- **M and H_0.** M = {Re z = α coth(x/2)}, and H_0 ⊂ {0 ≤ Re z ≤ α coth(x/2)}. ✓
- **Points on the a_1-line.** C_1 = iαe^{σ_1}, the a_1-line is |z| = αe^{σ_1}, and cos θ = tanh a_1. So Re D_1 ≥ α coth(x/2) ⇔ e^{σ_1} ≥ coth(x/2)/tanh a_1 = R. ✓
- **cosh σ_1.** The side between a_1 and x is opposite a_2, so cosh σ_1 = (cosh a_2 + cosh a_1 cosh x)/(sinh a_1 sinh x). Then R − cosh σ_1 = (cosh a_1 − cosh a_2)/(sinh a_1 sinh x). ✓
- **The case a_1 > a_2.**
  - The condition is equivalent to sinh σ_1 ≥ R − cosh σ_1 > 0, i.e. Nn² − Dd² ≥ (cosh a_1 − cosh a_2)².
  - Factorisation: (Nn − cosh a_1 + cosh a_2)(Nn + cosh a_1 − cosh a_2) = (cosh a_1(cosh x − 1) + 2cosh a_2) · cosh a_1(cosh x + 1). ✓
  - Dd² = sinh²a_1 (cosh²x − 1). ✓
  - After dividing by cosh x + 1, the final inequality holds strictly because cosh² > sinh².
- **Conclusion.** D_1 and D_2 lie beyond M, so by convexity the segment s_{12} does too. Its points project to their feet on M ⊂ ∂H_0 (M is the whole side). The σ_i ⊂ L_i are fixed, and x is fixed. So (H1)–(H3) hold.
- The sentence "no point of H_a projects into the interior of x" is true but not needed.

### Consequence in (b)
Correct.
- K is compact in M(Σ′°), and the systole is ≥ ε on K.
- Lemma S then gives sys(ψ(X)) < ε.
- ε depends on the type of Σ′°, η′ and the fixed metric d.
- Maskit's ℓ ≤ π Ext is correctly stated.

### Proof of (c)
Correct.
- The bound on the filling curves is independent of P′_k, because Lemma S is.
- (Prop) gives subsequential limits W′.
- ℓ_β(W′) ≤ ℓ_β(W) holds for **all** non-peripheral closed curves, not only simple ones. Both Lemma S and (GC1) are stated for all of them.
- (Th) is applied to the marking-change homeomorphism W → W′, which sends cusps to cusps. Its hypothesis is exactly this inequality over all closed geodesics of W, which are all non-peripheral. So W′ = W.
- The use of (Prop) is within scope: the β_j fill Σ′° in the stated sense.

### Proof of (d)
Correct.
- Diagonal choice τ_k w_k → w′, which needs k_j increasing. U is Tw-invariant, so τ w_k ∈ U ∩ T_g.
- Σ_y is a component of S cut along the node curves of w′: its boundary curves are nodes of w′ because p ∈ L_y, and no α_e lies inside it.
- (a) applies to τ_k, which is a product of twists about α_e disjoint from int Σ_y. Then (c) applies.

**Verdict: correct, with the marking-identification step replaced by the geodesic-homotopy argument above.**

---

## 5. Cited classical facts that look misstated or need a qualifier

These are all from memory; none is fatal.
1. **(Hex), monotonicity clause.** "Disjoint from L" is unnecessary. Injectivity holds along any geodesic not perpendicular to L. As stated the clause is true, just weaker than needed, and it is used only where it holds.
2. **Kerckhoff's formula.** The supremum is over **simple** closed curves (equivalently, measured foliations). The derived inequality Ext_Y(γ) ≤ e^{2d_T}Ext_X(γ) holds for all curve families anyway, by K-quasi-invariance of extremal length.
3. **Selberg's lemma.** It needs a field of characteristic 0, or should be stated for finitely generated subgroups of GL_n(ℂ). In positive characteristic only a virtually torsion-free variant holds.
4. **(Th).** The rigidity is correct for closed surfaces. I believe Thurston's paper covers complete finite-area surfaces with cusps, but I cannot confirm that from memory.
   - The intended consequence (length-spectrum domination ⇒ equality in Teichmüller space, i.e. positivity of Thurston's asymmetric metric) is standard for cusped finite-area surfaces.
   - Alternatively: domination gives a 1-Lipschitz map in the homotopy class (by Thurston's best-Lipschitz-constant theorem), and equal areas force it to be an isometry.
   - It would be safer to cite it in that form.
5. **(Kur).** "Stab_{Aut(J)}(p) ≅ Aut(X_p)" holds only after shrinking B, which the text does. With non-effective Aut(J)-actions, as in genus 2, it remains correct as stated. No issue.
6. **(IS_c).** It is correctly stated as a count of isomorphism classes over B (isomorphisms inducing the identity on B) of locally non-trivial families. The Parshin–Arakelov attribution for compact B is right.

No other cited fact used in the four proofs appears misstated: (dF), (TF), (BC), (FN), (Coll), (Mum), (Prop), (Ext), and the cited Bers–Greenberg and MacLachlan–Harvey results.

## What is settled and what is open
- **Proved here (as referee checks):** all four proofs are correct after the minor repairs written out above.
  - Theorem 7.5: two wording repairs.
  - C.5: no repair needed.
  - F1: moving the torsion-freeness argument before §0.
  - Lemma S: the geodesic-homotopy proof of the marking identification.
- **Conditional, not under review:** C.5 depends on Theorem A and Lemma 2.3, whose proofs were not checked. Theorem A also rests on the readings (R1), (R2) and (R2^orb).
- **Open:** the general case without (AP), i.e. whether isotropy can change along the family. As Remark C.6 says, the orientation (≤ vs ≥) and the non-uniformity of upper semicontinuity of |Aut| prevent the C.5 argument from extending.

=== END OF ANSWER extra_q7 ===

