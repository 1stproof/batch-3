# round9_q5 — the twin step (TW*): fixed loci of automorphisms

## Status / plan (written first; updated at the end)

**Final status: (TW\*) is NOT proved and NOT refuted.**

Proved (sections 1–3):
- **Case (C)** of R8-5 Prop. D is not an obstruction.
- Any α-fixed locus contained in {τ = 0} is not an obstruction.
- So a twin jump requires a family of α-symmetric curves in V_τ, τ ≠ 0, near J of complex dimension at least 2 (cases (D2), (D3)).
- In case (A2), total geodesy forces this family to restrict at τ = 0 to a Teichmüller curve of α-symmetric curves of V_0 with cusp J, or to an α-symmetric sheet of V_0.
- A boundary-trace trichotomy (Lemma 3) gives pointwise Lock at J(τ), or Lock on α-stable transported pieces. But it does not reach the persistent twin pair of the chain.

Open questions are listed in §5.

Plan:
1. Sharpen R8-5 Theorem A, and Theorem B, by a general-position argument. Branch points of 𝒞° → 𝒜 matter only if they form a **2-dimensional** set at times τ ≠ 0. This removes case (C) of R8-5 Prop. D. It also removes every bad locus lying in {τ = 0}: a whole α-fixed sheet of V_0, or an α-fixed curve of V_0 that does not deform.
2. Use total geodesy (Teichmüller uniqueness) to show the following. In the surviving case (A), the τ = 0 slice of the bad locus is the lift of a **Teichmüller curve of α-symmetric curves of V_0 with cusp J**.
3. Analyse the boundary trace Ψ of a surviving 2-dimensional bad component Φ. Ψ forces either α ∈ Aut(J(τ)) at a lift of J(τ), or a **locked pair of vertices on a whole transported piece**. Record what is missing to close (TW*).

Departure from the named approach: case (C) is not excluded by total geodesy. It is excluded by a dimension count (real codimension 4 in a 6-manifold), which makes it invisible to the 2-parameter squares of Theorem A. Total geodesy enters only in step 2.

---

## 0. Setting, readings and notation

Everything is as in the task. That is: MS8 with (Rig); readings (R1), (R2) with H_0 = id; the chain of Proposition K in the chart forms (TD_J), (TD_Q) of R8-5 §1, §5; and the chart conventions (C1)–(C3) of R8-5 §1. In particular, at a junction J:
- B ⊂ Def(J) is an Aut(J)-invariant ball and q : B → U the quotient. 𝒱_U = 𝒱 ∩ (U × Δ_ε).
- 𝒞° is the connected component of q^{-1}(𝒱_U) containing γ̃ × {0}, and 𝒜 = q(𝒞°) = 𝒞°/Γ (Fact 0 of R8-5).
- Γ = Stab_{Aut(J)}(𝒞°), K is the kernel of Γ acting on 𝒞°, and Γ_x = Stab_Γ(x).

As the task allows, I assume no junction crossings: each J_m is a puncture of every piece through it. So J is isolated in B_0 ∩ Δ_{G_J}.

Two further readings are made explicit, because they are used below.
- **(R3)** φ : 𝒱 → Δ is a holomorphic submersion. This is the natural reading of "smoothly trivial family of submanifolds" (Ehresmann). It is used only in Lemma 1, to perturb squares inside the time slices.
- **(T4)** The lifted track γ̃ of (TD_J) (resp. (TD_Q)) lies in a single *global sheet*. That is, near each of its points it lies on the image in Def(J) of one fixed component S of the preimage of V_0 in T_g. Prop. K's tracks are Teichmüller ray segments, so they lie in one Teichmüller disc and hence in one such S (this is the input of R8-2 §4.3 Step 1). "Totally geodesic" is read as in the literature: every component S of the preimage of V_0 in T_g is a complex submanifold that contains every real Teichmüller geodesic tangent to it.

**Bad sets.** For α ∈ Γ \ KΓ_x let Fix(α) := Fix_B(α) × Δ_ε. This is a smooth submanifold, since the action is linear in suitable coordinates. closure(𝒞°) is a 3-dimensional analytic set (R8-5 Prop. D proof). Shrink B and ε once and for all, so that:
- every irreducible component of every Fix(α) ∩ closure(𝒞°) passes through (0,0);
- every such component with τ ≢ 0 on it has the following property: if it has dimension 1, then τ restricted to it is a finite map.

Both are possible by the local finiteness of germs. As in R8-5, I assume the tracks of (TD_J) exist in the shrunken chart.

Call such a component Φ **relevant** if Φ ⊄ {∏ s_e = 0} and τ|_Φ ≢ 0.

**Hypothesis (U″_J).** For every α ∈ Γ \ KΓ_x, every relevant component of Fix(α) ∩ closure(𝒞°) has dimension 1.

Compare R8-5's (U_J): there are no α-fixed points in 𝒞° near (J,0) at all, i.e. no component of Fix(α) ∩ closure(𝒞°) meets 𝒞°. (U″_J) is much weaker:
- it allows α-fixed points at τ = 0 (any dimension);
- it allows 1-dimensional fixed loci at τ ≠ 0 (case (C) of Prop. D).

## 1. Squares only see 2-dimensional bad loci (proved)

Put
- 𝔅_all := {p ∈ 𝒞° : Stab_Γ(p) ⊄ KΓ_x} = ⋃_{α ∈ Γ∖KΓ_x} Fix(α) ∩ 𝒞°;
- 𝔅^+ := the union of Φ ∩ 𝒞° over the relevant 1-dimensional components Φ;
- A := q(𝔅^+) ⊂ 𝒜.

**Lemma 0.** Assume (U″_J). Then:
- (a) 𝔅_all ∩ {τ ≠ 0} ⊂ 𝔅^+;
- (b) A is a closed analytic subset of 𝒜 of dimension ≤ 1, contained in {τ ≠ 0}, and A ∩ 𝒜_τ is finite for every τ;
- (c) over 𝒜^good := 𝒜 ∩ {τ ≠ 0} ∖ A, the map π : 𝒞′ := 𝒞°/(KΓ_x) → 𝒜 is a covering map on each connected component.

*Proof.*
- (a) Let p ∈ 𝒞° with τ(p) ≠ 0 and α ∈ Stab_Γ(p) \ KΓ_x. Then p lies on some component Φ of Fix(α) ∩ closure(𝒞°). Φ ⊄ {∏ s_e = 0}, because p ∈ B°, and τ(p) ≠ 0. So Φ is relevant, hence 1-dimensional by (U″_J), and p ∈ 𝔅^+.
- (b) 𝔅^+ is closed in 𝒞° and analytic. q|_{𝒞°} is the finite quotient map by Γ (Fact 0). So A is closed (q is closed) and analytic of dimension ≤ 1 (Remmert, finite maps).
  - Each relevant 1-dimensional Φ meets {τ = 0} only in (0,0) ∉ 𝒞°, and τ|_Φ is finite. Hence A ⊂ {τ ≠ 0}, and its τ-fibres are finite.
- (c) By (a), every p ∈ q^{-1}(𝒜^good) has Stab_Γ(p) ⊂ KΓ_x. Apply Lemma 1 of R8-5 (intermediate quotients) with H = KΓ_x, over the open set 𝒜^good. ∎

**Lemma 1 (general position, time-preserving).** Assume (R3). Let Q := [a,b] × [0,1], fix t ≠ 0, and let F : Q → 𝒜 be smooth with φ(F(s,τ)) = τt and F(Q) ∩ A = ∅ near the bottom edge. Then for every η > 0 there are τ_1 > 0 and a smooth F′ : Q → 𝒜 such that:
- φ(F′(s,τ)) = τt;
- F′ = F on [a,b] × [0,τ_1];
- d̄(F′, F) < η uniformly;
- F′(Q) ∩ A = ∅.

*Proof.*
1. F^{-1}(A) is compact and misses the bottom edge (A ⊂ {τ ≠ 0}). So it lies in {τ ≥ 2τ_1} for some τ_1 > 0.
2. Let N be a relatively compact neighbourhood of F(Q) in 𝒜. By (R3), ker dφ is a smooth real rank-4 subbundle of T𝒜. Choose finitely many smooth vertical vector fields v_1, …, v_k on N spanning ker dφ at every point of closure(N).
3. Let χ : [0,1] → [0,1] be smooth, with χ = 0 on [0,τ_1] and χ = 1 on [2τ_1,1]. For p ∈ P := {p ∈ R^k : |p| < p_0} put
 G(s,τ,p) := time-1 flow of χ(τ) Σ_j p_j v_j, applied to F(s,τ).
   - For p_0 small this is defined and lies in N.
   - Vertical flows preserve φ, so φ∘G = τt. Also G_p = F on τ ≤ τ_1, and G_p → F uniformly as p → 0.
4. On {τ ≤ 2τ_1}: F misses the closed set A there, so G_p does too for p small (compactness).
5. On Q′ := [a,b] × [2τ_1,1], χ = 1, and ∂G/∂p spans ker dφ at G(s,τ,p) for p small (true at p = 0, and surjectivity is open). Let 𝒜_seg := φ^{-1}({σt : σ ∈ [0,1]}), a real 5-manifold with boundary. Then Ĝ := G|_{Q′×P} : Q′ × P → 𝒜_seg is a submersion: the p-directions give ker dφ, and ∂_τ G has dφ(∂_τ G) = t ≠ 0.
6. A_seg := A ∩ 𝒜_seg ∩ closure(N) is the preimage of a real segment under the finite holomorphic map φ|_A. So it is a compact semianalytic set of real dimension ≤ 1, a finite union of points and smooth arcs (stratification of semianalytic sets; standard, cited from memory).
   - Since Ĝ is a submersion, Ĝ^{-1}(arc) and Ĝ^{-1}(point) are submanifolds of codimension 4 and 5 in Q′ × P, i.e. of dimension ≤ (k+2) − 4 = k − 2.
   - Their projections to P are smooth images of manifolds of dimension < k, hence of measure zero.
7. So for almost every small p, G_p misses A. Take F′ := G_p with p so small that d̄(G_p, F) < η. ∎

**Lemma 2 (branching over τ = 0 is harmless).** Assume (U″_J), (R3) and (T4). Let F′ be as in Lemma 1, with F′(s,0) = γ(s), and with γ̃ a lift of γ as in (TD_J) satisfying (T4) and the genericity condition (G) below. Let λ be a lift in 𝒞° of the top edge F′(·,1) with λ(a) = μ_a(1), where μ_a is a lift of F′(a,·) from γ̃(a). Then for every s there are:
- a lift μ_s in 𝒞° of F′(s,·) with μ_s(0) = γ̃(s), and
- κ_s ∈ Γ_x,

with λ(s) = κ_s μ_s(1).

**(G)** γ̃ avoids the set Bad_0 ⊂ 𝒞°_0 := 𝒞° ∩ {τ = 0} of points p that satisfy one of:
- p is a singular point of q^{-1}(V_0 ∩ U);
- p lies on two different local sheets;
- Stab_Γ(p) is strictly larger than the pointwise stabiliser of its local sheet.

Bad_0 is an analytic subset of 𝒞°_0 of dimension ≤ 1. By (T4), γ̃ moves inside one global sheet S, a smooth complex surface, in which Bad_0 ∩ S is a proper analytic subset. So γ̃ can be perturbed inside S, by an arbitrarily small amount, to satisfy (G). This is the argument of R8-2 §4.3 Step 1, which also checks that (TD_J)'s conditions (T1)–(T3) survive, with ρ replaced by 2ρ, since they are open.

*Proof.*
1. **The covering of the τ = 0 slice.** Let R_0 := 𝒞°_0 \ Bad_0, which is Γ-invariant.
   - At p ∈ R_0, G_p := Stab_Γ(p) acts trivially on the unique smooth local sheet X through p. Take a G_p-invariant neighbourhood W of p with gW ∩ W = ∅ for g ∉ G_p.
   - Then W ∩ 𝒞°_0 = W ∩ X maps homeomorphically onto its image in 𝒜_0 := 𝒜 ∩ {τ = 0}, both from 𝒞°_0 and from 𝒞′_0 := 𝒞°_0/(KΓ_x).
   - So 𝒞′_0 → 𝒜_0 is a local homeomorphism at the classes of points of R_0. Since R_0 is saturated, it is a covering over q(R_0). In particular, lifts to 𝒞′_0 of paths in q(R_0) are unique given their initial point.
2. **Lifting the half-open square.** Q^+ := [a,b] × (0,1] is contractible, and F′(Q^+) ⊂ 𝒜^good (Lemma 1: φ∘F′ = τt ≠ 0 and F′ misses A). By Lemma 0(c) there is a lift L̂ : Q^+ → 𝒞′ with L̂(a,τ) = [μ_a(τ)].
3. **Extension to τ = 0.** Fix s.
   - π : 𝒞′ → 𝒜 is a finite quotient map of Hausdorff spaces. So a small neighbourhood N of γ(s) has preimage a disjoint union of neighbourhoods N_j of the finitely many fibre points.
   - The connected set F′([s−δ, s+δ] × (0,δ]) lies in N for δ small, so its lift lies in a single N_j.
   - Hence L̂ extends continuously to Q, and L̂(·,0) is a continuous lift of γ to 𝒞′_0.
4. **The extended bottom edge is [γ̃].** At s = a, L̂(a,0) = [γ̃(a)]. Both L̂(·,0) and s ↦ [γ̃(s)] are lifts of γ to 𝒞′_0, and γ(s) ∈ q(R_0) by (G). By uniqueness (step 1), L̂(s,0) = [γ̃(s)] for all s.
5. **The vertical lifts.**
   - Path lifting for finite group quotients (Bredon, II.6.2, cited from memory) gives a lift ν_s : [0,1] → 𝒞° of the path τ ↦ L̂(s,τ) in 𝒞′, through the quotient 𝒞° → 𝒞′. It starts at ν_s(0) = m γ̃(s) with m ∈ KΓ_x. Put μ_s := m^{-1} ν_s. This is a lift of F′(s,·) with μ_s(0) = γ̃(s).
   - L̂(·,1) and [λ] are both lifts of F′(·,1) to the covering over 𝒜^good, starting at [μ_a(1)]. So they coincide.
   - Hence λ(s) ∈ KΓ_x ν_s(1) = KΓ_x m μ_s(1) = KΓ_x μ_s(1). As K is normal and acts trivially on 𝒞°, λ(s) = κ_s μ_s(1) with κ_s ∈ Γ_x (as in R8-5 Lemma 2). ∎

Note the difference from R8-5 Lemma 2: there the vertical lift μ_s was arbitrary. Here it is *some* lift from γ̃(s). This suffices, because R8-5 Corollary 3′ holds for **every** lift of F(s,·) from γ̃(s): its proof only uses that the lift starts at γ̃(s), within ρ of ẑ_s.

**Theorem A″.** R8-5 Theorem A holds with (U_J) replaced by (U″_J), assuming (R3) and (T4). That is, under (TD_J), (T4), (R3) and (U″_J) at J we get φ_{c_{k−1}} ≡ φ_{c_k} on Δ.

*Proof.* Run the proof of R8-5 Theorem A with the following changes.
1. Fix t, r_1 and ρ as there, and take the track. Make γ smooth and generic, satisfying (G), by Lemma 2's remark. Then F(s,τ) := H(γ(s), τt) is smooth, because H is smooth on V_0 × Δ.
2. Replace F by the F′ of Lemma 1, with η < ε_1. F′ is still time-preserving, and its bottom edge is still γ.
3. Corollary 3′ of R8-5 applies to F′ with ε_1 replaced by 2ε_1: every point of the vertical path F′(s,·) is within ε_1 + η < 2ε_1 of H(z_s, τt). Accordingly, require ρ < 2ε_1 < d′(r_1,t)/3 in the choice of constants.
4. Take the lifts μ_s and κ_s ∈ Γ_x from Lemma 2 instead of R8-5 Lemma 2.
5. Everything after "**Lifts.**" in R8-5's proof is then unchanged:
   - regime (ii) uses κ_s ∈ Γ_x and Corollary 3′;
   - regime (i) uses d̄(qλ(s), J(t)) < η + ε_1 + ω_H(r_1) ≤ r_2, after adjusting the constant;
   - then near-continuity, and the endpoints s = a and s = b. ∎

**Theorem B″.** R8-5 Theorem B holds with (U_{Q_0}) replaced by (U″_{Q_0}), the same hypothesis written in the chart at Q_0, assuming (R3) and (T4).

*Proof.* Its proof uses only:
- the class-function argument of Theorem A on [a, s_*], to which the changes above apply verbatim;
- the identity λ(e) = κ_e μ_e(1) with κ_e ∈ Γ_x and μ_e a vertical lift from γ̃(e), which Lemma 2 provides;
- the separation constants d″ and η_1(t), which are unaffected by a perturbation of size η < ε_1. ∎

**Corollary 1 (R8-5 Prop. D sharpened).** Assume (R3) and (T4). If a twin jump occurs at a junction J (φ_{c_{k−1}} ≢ φ_{c_k}), then there are α ∈ Γ \ KΓ_x and a relevant component Φ of Fix(α) ∩ closure(𝒞°) with dim Φ ≥ 2. The same holds at the endpoint Q_0 if the conclusion of Theorem B fails. In particular:
- **case (C) of R8-5 Prop. D is not an obstruction;**
- nor is any α-fixed locus contained in {τ = 0}. This includes the α-symmetric curves of V_0 that do not deform, and whole α-symmetric sheets of V_0.

The surviving obstructions are:
- **(D3)** dim Φ = 3: α fixes pointwise a whole irreducible component of closure(𝒞°) (possible only if 𝒞° is reducible, since α ∉ K);
- **(D2)** dim Φ = 2 and τ|_Φ ≢ 0. Then Φ_0 := Φ ∩ {τ = 0} has pure dimension 1 (Krull), and either
  - **(A2)** Φ_0 meets B° arbitrarily close to 0, or
  - **(B)** Φ_0 ⊂ {∏ s_e = 0}.

  In both cases, for each small τ ≠ 0, Φ_τ is a complex curve of α-symmetric curves in (the lift of) V_τ near J.

*Proof.* Contrapositive of Theorems A″ and B″, together with the dimension count of R8-5 Prop. D(b). ∎

## 2. Total geodesy: the τ = 0 slice in case (A2) (proved, modulo cited Teichmüller facts)

**Cited facts (from memory, standard).**
- (Te1) *Teichmüller's theorem.* For X ∈ T_g and every unit tangent direction v at X there is exactly one real Teichmüller geodesic ray from X with initial direction v.
  - The map (r, v) ↦ (point at distance r on that ray) is a homeomorphism from T_X T_g ≅ R^{6g−6} onto T_g.
  - This uses the fact that q ↦ [q̄/|q|] is a homeomorphism from the unit sphere of Q(X) onto the unit sphere of T_X T_g, which holds by strict convexity of the L^1 norm on Q(X) and the infinitesimal Teichmüller theorem.
- (Te2) The Teichmüller disc of (X, q) is the union of the real geodesics from X in the directions e^{iθ}v_q. It is a closed, properly embedded holomorphic disc, the image of a holomorphic isometry H → T_g.
- (Te3) For a finite-order mapping class h with Fix(h) ≠ ∅, Fix(h) ⊂ T_g is a closed connected complex submanifold (Cartan linearisation; it is the Teichmüller space of the quotient orbifold).

**Lemma TG.** Let S be a component of the preimage of V_0 in T_g, which is totally geodesic in the sense of §0 (T4). Let h be as in (Te3). Then every irreducible component I of S ∩ Fix(h) is one of:
- a point;
- a single full Teichmüller disc D ⊂ S ∩ Fix(h);
- S itself.

*Proof.*
1. **Fix(h) is totally geodesic.** Let X ∈ Fix(h) and v ∈ T_X Fix(h), i.e. dh_X(v) = v. The isometry h maps the ray from X in direction v to the ray from hX = X in direction v. By uniqueness (Te1) these coincide, and h fixes the ray pointwise.
2. **The tangent intersection.** Let X be a smooth point of I lying on no other component of S ∩ Fix(h), and put L := T_X S ∩ T_X Fix(h), a complex subspace. For v ∈ L the ray in direction v lies in S (total geodesy of S) and in Fix(h) (step 1).
3. **Case L = T_X S.** The restriction of the homeomorphism of (Te1) to the real 4-dimensional subspace T_X S is injective and continuous, with image in S. By invariance of domain its image contains a neighbourhood of X in S, and that neighbourhood lies in Fix(h). So I contains a non-empty open subset of the connected complex manifold S, and I = S.
4. **Case dim_C L = 1 and dim I = 1.** By (Te2) the disc D tangent to L at X is a union of rays with directions in L, so D ⊂ S ∩ Fix(h). Since X lies on I only, D ⊂ I near X. Then:
   - D is irreducible and closed, and it shares an open piece with the irreducible 1-dimensional I, so D ⊂ I;
   - D is 1-dimensional and closed, so I = D.
5. **Remaining cases.**
   - If dim I = 2, then I = S, since I is closed analytic in the connected surface S.
   - If dim I = 1, step 3 cannot occur (it would give I = S), and T_X I ⊂ L. So step 4 applies.
   - Otherwise I is a point. ∎

**Corollary 2 (structure of case (A2)).** In case (A2) of Corollary 1, let p ∈ Φ_0 ∩ B° be a point near 0 that lies on no boundary component of Φ_0. Near p, the chart is a neighbourhood in T_g of a marked lift of the curve C_p, α corresponds to a mapping class h fixing that lift, and q^{-1}(V_0) corresponds to the union of the components S of the preimage of V_0. So by Lemma TG one of the following holds.
- **(A2-disc)** The interior part of Φ_0 lies on lifts of a **Teichmüller curve 𝒯 ⊂ V_0 all of whose curves carry the automorphism h**, and J ∈ closure(𝒯) is a cusp of 𝒯. Indeed:
  - the image in M_g of the disc D lies in V_0 ∩ M_g^{[h]}, where M_g^{[h]} is the closed algebraic locus of curves admitting an automorphism of type [h];
  - the component of V_0 ∩ M_g^{[h]} containing it is a closed algebraic curve whose lift contains D, i.e. a Teichmüller curve.
- **(A2-sheet)** Φ_0 lies inside a sheet of q^{-1}(V_0) that is fixed pointwise by α. Then every curve of V_0 on that sheet near J has the automorphism h, and Φ_τ is the part of it that stays α-symmetric for τ ≠ 0.

In both cases the automorphism exchanges the regions x and αx. Since F_x(0) = F_{α^{-1}x}(0) by (K3), every Aut(J)-translate of x is a Y_0-copy of J.

So total geodesy turns the vague "α-symmetric curves of V_0 near J" into a rigid object: a Teichmüller curve with cusp J, or a whole symmetric sheet. Neither, by itself, says anything about the deformed V_τ, which is not totally geodesic. That is why §3 turns to the boundary trace of Φ at τ ≠ 0.

## 3. The boundary trace of a surviving 2-dimensional bad locus (proved)

Let (α, Φ) be as in (D2). Put Ψ := Φ ∩ {∏ s_e = 0}. Φ is irreducible of dimension 2, not contained in the hypersurface {∏ s_e = 0}, and (0,0) ∈ Φ. So Ψ has pure dimension 1 at (0,0) (Krull).

Moreover Ψ ⊂ closure(𝒞°) ∩ {∏ s_e = 0} ⊂ q^{-1}(𝓑), where 𝓑 := closure(𝒱) ∩ (∂M̄_g × Δ) = H(B_0 × Δ) (R2). Near (J,0) the preimage q^{-1}(𝓑) is the disjoint union of:
- 𝒥 := q^{-1}(H({J} × Δ_ε)), the set of lifts of the points J(τ) := H_τ(J). Because J is isolated in B_0 ∩ Δ_{G_J} (no crossing), H({J} × Δ_ε) = 𝓑 ∩ (Δ_{G_J} × Δ_ε) near (J,0), and no deeper stratum meets a small neighbourhood of J. So this is an analytic curve, finite over Δ_ε, and 𝒥 is analytic.
- the components Z ∈ 𝒵 of q^{-1}(H(B_0^U × Δ_ε)) (R8-5 §3). Each Z has a constant pattern S(Z), and Z_0 = Z ∩ {τ = 0} is a lifted punctured boundary branch.

**Lemma 3 (trichotomy for the trace).** Let Ψ_1 be an irreducible component of the germ of Ψ at (0,0). Exactly one of the following holds.
- **(Ψ-0)** Ψ_1 ⊂ {τ = 0}. Then Ψ_1 is a lifted boundary branch of B_0 at J, fixed pointwise by α.
- **(Ψ-J)** Ψ_1 ⊂ 𝒥 and τ|_{Ψ_1} ≢ 0. Then for every small τ ≠ 0 some lift ĵ(τ) of J(τ) is fixed by α. So α ∈ Stab(ĵ(τ)) ≅ Aut(J(τ)) (K4), and F_x(ĵ(τ)) ≅ F_{αx}(ĵ(τ)): the twins x, αx of J(τ) are isomorphic at that lift ("pointwise Lock").
- **(Ψ-Z)** Ψ_1 \ {(0,0)} ⊂ Z for a single Z ∈ 𝒵, τ|_{Ψ_1} ≢ 0, and αZ = Z. Let D_Z be the piece of the branch underlying Z and G_Z its graph. Then α induces an automorphism ᾱ of G_Z, and:
  - (i) if ᾱ[x] ≠ [x] and both [x], [αx] are constant on D_Z, then φ_{[x]} ≡ φ_{[αx]} on Δ. This is **(Lock) of the pair on the whole transported piece D_{Z,τ}**;
  - (ii) if exactly one of them, say w, is constant and the other, u, is moving, then for every small τ the value φ_w(τ) is the u-coordinate of a point of the fixed curve K_W (Lemma U of R8-2). This is a coincidence of exactly the type excluded by (NB_∂) of R8-2;
  - (iii) if both are moving, the point of K_W over Ψ_1 ∩ {τ} has isomorphic [x]- and [αx]-coordinates for every τ.

*Proof.*
1. If τ ≡ 0 on Ψ_1, then Ψ_1 ⊂ closure(𝒞°) ∩ {τ = 0} ∩ {∏ s_e = 0}. This set lies over B_0 by (R2), since H_0 = id and H commutes with closures. A 1-dimensional germ there is a lifted branch of B_0, and it lies in Fix(α). This is (Ψ-0).
2. Otherwise τ|_{Ψ_1} is finite, and Ψ_1 ∩ {τ = 0} = {(0,0)} near (0,0). The germ Ψ_1 \ {(0,0)} is connected (an irreducible curve germ minus its centre is a punctured disc, after shrinking). Either Ψ_1 ⊂ 𝒥, or Ψ_1 ∩ 𝒥 is a proper analytic subset of the irreducible curve germ, hence ⊂ {(0,0)}.
   - In the first case, every point of Ψ_1 is an α-fixed lift of some J(τ), and τ(Ψ_1) is a neighbourhood of 0. Lifts of J(τ) lie in {s_e = 0 for all e} ⊂ L_x ∩ L_{αx}. By (K3) with σ = α^{-1} and α^{-1}ĵ = ĵ: F_x(ĵ) = F_x(α^{-1}ĵ) = F_{αx}(ĵ).
   - In the second case, Ψ_1 \ {(0,0)} lies in the disjoint union of the relatively open sets Z, so it lies in one of them. Take p ∈ Ψ_1 \ {(0,0)}. αZ is the component of q^{-1}(H(B_0^U × Δ)) containing αp = p, so αZ = Z.
3. **(Ψ-Z), the graph automorphism.** αZ = Z gives αS(Z) = S(Z). So α permutes the edges outside S(Z), and it descends to an automorphism ᾱ of G_Z = G_J/(E \ S(Z)) with ᾱ[y] = [αy].
4. **The comparison.** At p ∈ (Ψ_1)_τ, α is an automorphism of the fibre curve C_p. It maps the partial normalisation of C_p along the nodes in S(Z) to itself, and it carries the [x]-part isomorphically onto the [αx]-part. So, in the lifted transported piece over D_{Z,τ}, the [x]- and [αx]-coordinates of the point over p are isomorphic as pointed curves up to relabelling.
   - (i) Both coordinates are the constant values φ_{[x]}(τ), φ_{[αx]}(τ). They agree for all small τ ≠ 0, and both are holomorphic (R7-3 Lemma 1(a)), so they agree identically (identity theorem in the coarse space, R8-8 Lemma 1).
   - (ii) The moving coordinate at the point over p is a coordinate of a point of K_W, where W is the component of the lifted boundary family containing D_{Z,τ} (R8-2 Lemma U: D = K_W × {c_D}).
   - (iii) This is the same statement as (ii) with both coordinates on K_W. ∎

**Where the Ψ-components come from.**
- In case (A2) with Φ_0 ∩ {∏ s_e = 0} = {(0,0)} near 0, every component of Ψ is of type (Ψ-J) or (Ψ-Z), and there is at least one.
- In case (B), Ψ ⊇ Φ_0, and it can happen that Ψ = Φ_0. I call this **(B-pure)**: for τ ≠ 0, the α-symmetric curves Φ_τ ⊂ V_τ are disjoint from the boundary near J, and they converge, as τ → 0, to the α-fixed lifted boundary branch Φ_0. Lemma 3 gives no information at τ ≠ 0 in (B-pure).

## 4. Consequences for (TW*), and why (Lock) does not yet follow

**Corollary 3 (conditional (TW*), proved).** Assume the setting of (TW*), with no crossings, together with (R3) and (T4).
- If (U″_{J_m}) holds at every junction, then (TW*)(a) holds: [φ_{c_m}] ≡ [Y] for all m. This follows by induction from φ_{c_1} = Y and Theorem A″.
- If moreover (U″_{Q_0}) holds, then (TW*)(b) holds for all t in a punctured disc minus a countable set, by Theorem B″. So MS8 holds in this case (R8-5 Corollary C).
- At each junction, (U″_J) may be replaced by (Lock_J), using R7-1 Step 2 as in R8-5 Remark 3.

In words: **a counterexample to (TW*)(a) at J requires α ∈ Γ \ KΓ_x such that, for every small τ ≠ 0, V_τ contains near J a whole complex curve (case D2) or an open set (case D3) of curves on which α acts as an automorphism moving the tracked region x.** Isolated α-symmetric curves of V_τ (case (C)), or α-symmetry present only at τ = 0, do not suffice.

**What (D2) looks like, combining §§2–3.**
- (A2-disc): V_0 contains a Teichmüller curve 𝒯 of h-symmetric curves with cusp J. 𝒯 deforms to curves Φ_τ ⊂ V_τ ∩ M_g^{[h]}. The boundary trace gives either α ∈ Aut(J(τ)) at a lift (Ψ-J), or an α-stable transported branch Z on which the pair ([x],[αx]) is locked or (NB_∂)-coincident (Ψ-Z).
- (A2-sheet): the same, with 𝒯 replaced by a curve inside an α-symmetric sheet of V_0.
- (B): an α-fixed boundary branch at τ = 0, possibly with no boundary trace at τ ≠ 0 (B-pure).

**Why this does not give (Lock) of the persistent twin.** By R8-8 Prop. 3(b), a twin jump at J_m means the following. D^{m+1} carries two constant vertices, c_{m+1} = {x_m} and w = {a^{-1}x_m} along β̃^{m+1}, with [φ_w] ≡ [Y] ≢ [φ_{c_{m+1}}]. The jump is excluded exactly by (Lock) of this pair on D^{m+1}.

Lemma 3 (Ψ-Z)(i) produces (Lock) of a pair ([x],[αx]), but only on the pieces D_Z that the trace Ψ of a bad locus enters. To conclude, one would need:
- (L1) some bad component Φ, for an α whose conjugacy class contributes to the monodromy κ_b of the square, has a (Ψ-Z) trace in a translate g·Ñ^{m+1}_− of the D^{m+1}-family;
- (L2) with g^{-1}{x, αx} = {x_m, a^{-1}x_m}.

Neither (L1) nor (L2) follows from the construction. The monodromy κ_b is a product of local monodromies at the isolated points where the (perturbed) square crosses the real-codimension-2 set q(Φ). These crossings can lie in regime (i), near J(τt), where they are unrelated to any particular Z. This is the scale conflict of R8-8 §6, now localised: by Lemma 1 it concerns **only** 2-dimensional bad loci.

**Status of the three configurations of the task.**
- **Case (C):** *not an obstruction* (Theorem A″/B″, Corollary 1). Proved, given (R3), (T4) and the inputs (TD_J)/(TD_Q).
- **Case (A):** the part with Φ ⊂ {τ = 0} is *not an obstruction* (Lemma 2). The part with τ|_Φ ≢ 0 (A2) is reduced to a Teichmüller curve 𝒯 ⊂ V_0 of α-symmetric curves with cusp J (Lemma TG), or a symmetric sheet, deforming inside V_τ ∩ M_g^{[h]}. It is **not excluded**.
- **Case (B):** **not excluded**. Its sub-case (B-pure) is invisible to the boundary-trace argument.
- **Endpoint (TW*)(b):** the same statements hold at Q_0 (Theorem B″).

## 5. Summary: proved / not proved / open

**Proved here** (given the task's inputs (TD_J), (TD_Q), (R1), (R2), and the explicit readings (R3), (T4)):
1. Lemma 0, Lemma 1 (time-preserving general position), Lemma 2 (branching over τ = 0 is harmless).
2. Theorems A″ and B″. R8-5's Theorems A and B hold under the much weaker (U″): every relevant fixed-point component is 1-dimensional.
3. Corollary 1. Case (C) of Prop. D, and every α-fixed locus inside {τ = 0}, are not obstructions to (TW*). A twin jump needs a ≥ 2-dimensional family of α-symmetric curves of 𝒱 at τ ≠ 0 near (J,0).
4. Lemma TG (from Teichmüller uniqueness): the intersection of a totally geodesic sheet with Fix(h) is the sheet, a full Teichmüller disc, or points. Hence Corollary 2: in case (A2), V_0 contains a Teichmüller curve of h-symmetric curves with cusp J, or an h-symmetric sheet.
5. Lemma 3: trichotomy for the boundary trace of a surviving bad locus. In particular, (Lock) of the pair ([x],[αx]) holds on every α-stable transported piece that the trace enters with both vertices constant.
6. Corollary 3: (TW*) holds, hence MS8 holds in the no-crossing case, whenever (U″) or (Lock) holds at every junction and (U″) holds at the endpoint.

**Not proved:** (TW*) itself. I found neither a proof nor a counterexample. No configuration violating (TW*) was constructed: realising (D2) needs an actual smooth totally geodesic V_0 together with a deformation, which is out of reach here.

**Open questions (precise):**
- **(O1″)** Case (D2)/(A2): let V_0 contain a Teichmüller curve 𝒯 of h-symmetric curves with cusp J, where h exchanges two Y_0-copies x, αx of J, and let 𝒯 deform to h-symmetric curves Φ_τ ⊂ V_τ. Does this force (Lock) of the persistent twin pair (c_{m+1}, w) on D^{m+1}, or (IP) at J (|Aut J(τ)| = |Aut J|)? A positive answer would need (L1)–(L2) above.
- **(O2″)** Case (B-pure): can the α-symmetric curves Φ_τ ⊂ V_τ (τ ≠ 0) converge to an α-fixed boundary branch of V_0 without having boundary points near J(τ)? Neither (R1), (R2), (Rig) nor Lemma U seems to exclude this.
- **(O3″)** Case (D3): can a component of closure(𝒞°) be fixed pointwise by α ∉ K, which needs 𝒞° to be reducible over orbifold points of 𝒱?
- **(O4″)** The inputs (TD_J), (TD_Q) and (T4) are inherited from Proposition K "modulo routine marking details" and are not re-proved here. The reading (R3) is adopted.

=== END OF ANSWER round9_q5 ===

