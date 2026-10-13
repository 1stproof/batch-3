# round12_q2 — attempt on MS11♭

**Status line.** MS11♭ is **neither proved nor refuted** here. I prove one new structural lemma about the 3-fold component X: its lift-curves form a single G_X-orbit (Lemma A). This merges the planner's two failure modes into one and reduces (1L_X) to a group-theoretic condition. I also show that the planner's step-4 claim ("if g ∈ G_X fixes S × {0} pointwise, then g fixes L_0") is **false** in a local model that is consistent with every constraint used so far. The model is the natural "V_0 lies in a symmetric locus" situation, which covering constructions produce. Finally I re-check the logic of the chain at the points where MS11♭ is used. I found no flaw there, but I did not re-audit the entries it cites.

Readings: (R1), (R2) with H_0 = id, as in the brief. Notation: G := Aut(Q), q: Def(Q) → Def(Q)/G, B, ε, S, lift-curves, C(L), P(T), anchored sheets — all as in the brief. 𝒮 := q(S) is a coarse sheet (irreducible germ) of closure(V_0) at Q.

---

## 1. Lemma A (lift points in a 3-fold component form one G_X-orbit) — proved

**Setting.** X is an irreducible component of q^{-1}(closure 𝒱) ∩ (B × Δ_ε), with X ⊃ S × {0}. (By the choice of B and ε in MS11♭, such components are the germ components at (0,0).) Put G_X := Stab_G(X).

**Step 0 (coarse sheets of closure 𝒱; standard facts plus (R2)).**
- Let 𝒮_1, …, 𝒮_r be the irreducible components of the germ of closure(V_0) at Q.
- Standard fact (cited from memory): for a pure-dimensional germ (A, z) and a nowhere dense analytic Z ⊇ Sing A, and for a cofinal system of small neighbourhoods U, the connected components of (A ∖ Z) ∩ U correspond bijectively to the irreducible components of the germ. Their closures are the components. Inclusions between members of the system induce these bijections.
- V_0 is smooth, so V_0 ∩ 𝒮_k ∩ 𝒮_l = ∅ near Q for k ≠ l, and the components of V_0 ∩ W are the sets 𝒮_k ∩ V_0 ∩ W.
- 𝒱 is a manifold, so Sing(closure 𝒱) lies in the boundary. The sets H(W × D) (W a neighbourhood of Q in closure(V_0), D a disc about 0) form a neighbourhood basis of (Q,0), since H is a homeomorphism. Also 𝒱 ∩ H(W × D) = H((V_0 ∩ W) × D), whose components are the sets H((𝒮_k ∩ V_0 ∩ W) × D).
- Sandwiching this system between Milnor balls of closure(𝒱) gives the following. The irreducible components of the germ of closure(𝒱) at (Q,0) are exactly the sets 𝒳_k := H(𝒮_k × Δ_ε) (germs).
- 𝒳_k ∩ {t = 0} = 𝒮_k. Since q(X) is an irreducible component containing 𝒮 × {0}, we get q(X) = 𝒳 := H(𝒮 × Δ_ε).

**Step 1 (𝒳 is unibranch along the section).** For every small t, the germ (𝒳, (Q_t,t)) is irreducible, where Q_t = H_t(Q).
- *Proof.* Use the neighbourhoods H(W × D_t), with D_t a small disc around t. Then (𝒳 ∖ ∂) ∩ H(W × D_t) = H((𝒮 ∩ V_0 ∩ W) × D_t). This set is connected for a cofinal family of W, because 𝒮 is an irreducible germ (Step 0 applied to 𝒮). It lies in Reg(𝒳), because at points of 𝒱 only one component passes. By the standard fact, the germ is irreducible. ∎
- The same argument shows that 𝒳 is unibranch at (z, t) for every z ∈ 𝒮 ∩ V_0 near Q.

**Lemma A.** Let z ∈ 𝒳 be a point at which the germ of 𝒳 is irreducible, e.g. z = (Q_t, t) for small t, or z ∈ H((𝒮 ∩ V_0) × Δ_ε). Then the points of X over z form a single G_X-orbit.

*Proof.*
- Let p, p′ ∈ X with q(p) = q(p′) = z. Then p′ = gp for some g ∈ G.
- Let X_p be an irreducible component of the germ of X at p. Then q(X_p) is an irreducible 3-dimensional germ at z inside the irreducible 3-dimensional germ (𝒳, z), so q(X_p) = (𝒳, z).
- Near p′, q is the quotient by Stab(p′) (standard for finite group actions). The irreducible components at p′ of q^{-1}(𝒳, z) therefore form one Stab(p′)-orbit (standard: the preimage of an irreducible germ under a finite quotient).
- Both gX_p and any component X_{p′} of the germ of X at p′ are such components. Hence X_{p′} = k g X_p for some k ∈ Stab(p′).
- Then kg·X and X are irreducible components of the G-invariant set q^{-1}(closure 𝒱) ∩ (B × Δ_ε), and they share the 3-dimensional germ X_{p′}. Hence kgX = X, i.e. kg ∈ G_X, and kg·p = k p′ = p′. ∎

**Corollary A1 (lift-curves of X).**
- (a) X contains a lift-curve.
- (b) If L_0 ⊂ X is one, the lift-curves contained in X are exactly the hL_0 with h ∈ G_X.
- (c) Consequently (1L_X), "X contains exactly one lift-curve", holds iff G_X ⊆ H := Stab_G(L_0).
- (d) The planner's set A_X = {g : gL_0 ⊂ X} equals G_X·H.
- (e) The planner's second failure mode ("a second 3-fold component gX ≠ X meeting X along a lift-curve") is **subsumed** by the first: if gL_0 ⊂ X, then gL_0 = hL_0 with h ∈ G_X.

*Proof.*
- (a) (Q_t, t) ∈ 𝒳 = q(X), so X contains lifts of Q_t for every t. X ∩ 𝒥 is analytic and surjects onto Δ_ε, so it contains a curve not lying in {t = 0}.
- (b) Let L ⊂ X be a lift-curve. For each t ≠ 0, a point of L over t equals h_t·p_t with p_t ∈ L_0 and h_t ∈ G_X (Lemma A). Some h occurs for uncountably many t, so L ∩ hL_0 is infinite, and L = hL_0 since both are irreducible curve germs.
- (c), (d) follow from (b). (e) is (b) applied to L = gL_0. ∎

**Corollary A2 (MS11♭ in terms of G_X).** Suppose the x-persistent anchored sheet T of β̃ lies in X (as the brief notes, this can be arranged after an initial twist τ ∈ Stab_pt(β̃)), and let L_0 ⊂ T. Then:
- every D-sheet Σ of X of boundary type has P(Σ) = h·C(L_0) for some h ∈ G_X (Lemma 2.3 of round11_q1 / Lemma 2.2 of round11_q4, together with A1(b));
- MS11♭ holds for (Q, β̃, b̃, x) as soon as **C(L) is the same for all lift-curves L ⊂ X**, i.e. h·C(L_0) = C(L_0) for all h ∈ G_X. A sufficient condition is (1L_X).

**Corollary A3 (monodromy form of (1L_X)).**
- Fix t_* ≠ 0 small and let F be the set of lift points of Q_{t_*} lying in X. As a G_X-set, F ≅ G_X / A, where A := Stab_{G_X}(p) for p ∈ F.
- The monodromy μ of the finite covering {lift points in X} → Δ_ε^* around t = 0 commutes with G_X (G acts trivially on t). So μ is right multiplication by some n ∈ N_{G_X}(A)/A.
- The lift-curves in X correspond to the ⟨μ⟩-orbits on F.
- Hence (1L_X) holds iff ⟨n⟩ acts transitively on G_X/A. That requires A ⊲ G_X and G_X/A = ⟨n⟩ cyclic.
- In particular (1L_X) **fails whenever G_X/A is not cyclic** (for example G_X ⊇ (ℤ/2)² acting freely on F).

**Lemma A4 (X_0 and G_S).** Let K_S be the pointwise stabiliser of S, which equals the stabiliser of a generic point of S. Then:
- X_0 := X ∩ {t = 0} equals ⋃_{h ∈ G_X} hS as a set;
- G_S := Stab_G(S) ⊆ K_S·G_X.

*Proof.*
- Let z ∈ 𝒮 ∩ V_0 be generic and p ∈ S a lift of z. Then Stab(p) = K_S.
- First claim. Let g′S ⊂ X_0 be a translate. By Lemma A at (z,0), g′p = hp with h ∈ G_X. So h^{-1}g′ ∈ K_S, and g′S = hS. Conversely X_0 ⊇ S is G_X-invariant, so it contains every hS with h ∈ G_X.
- Second claim. Let g ∈ G_S. Then gX ⊇ S × {0} as well, so gX and X both contain the germ of S × {0} at (p,0).
  - Near (p,0), q^{-1}(𝒳) is the preimage of the manifold germ 𝒱 at (z,0). Its irreducible components at (p,0) form one Stab(p) = K_S-orbit.
  - A component of gX at (p,0) is therefore k times a component of X at (p,0), for some k ∈ K_S. So gX = kX, i.e. k^{-1}g ∈ G_X. ∎

## 2. The planner's step 4 is false in a consistent local model

**Claim (planner, step 4, 2-dimensional analogue of Lemma D3).** If g ∈ G_X fixes S × {0} pointwise, then gL_0 = L_0.

**Local model (counterexample to the claim).**
- Let k ≥ 2 and ζ = e^{2πi/k}.
- Let X be the smooth 3-fold germ with coordinates (a, w_1, w_2), with t = a^k on X. So X_0 = {a = 0} =: S, set-theoretically.
- Let G = ⟨g, h⟩ ≅ (ℤ/k)², acting by g(a, w_1, w_2) = (ζa, w_1, w_2) and h(a, w_1, w_2) = (ζa, ζw_1, w_2). Both preserve t.
- Let L_0 := {w_1 = a, w_2 = 0}, a curve on which t = a^k has degree k.

**Checks.**
- g fixes X_0 = {a = 0} pointwise, and g ∈ G_X = G.
- hL_0 = L_0, since h(a, a, 0) = (ζa, ζa, 0).
- gL_0 = {w_1 = ζ^{-1}a, w_2 = 0} ≠ L_0.
- The orbit of (a, a, 0) with a^k = t is {(ζ^{i+j}a, ζ^j a, 0)}, which has k² = |G| points. So the lift points over t form one G-orbit with trivial stabiliser, as (K1), (K4) require when Aut(Q_t) is trivial in this chart. The lift-curves are L_0, gL_0, …, g^{k−1}L_0, all in X, exactly as Lemma A predicts. Here G_X/A = G is not cyclic, so (1L_X) fails, consistently with A3.
- Coarse picture. Locally Def ≅ (a, w)-space and the coarse family near a generic point of S is X/⟨g⟩ with coordinate α = a^k = t. This is smooth with t a submersion. So the coarse family V_t = {α = t} is a smooth family of smooth surfaces. V_0 = {α = 0} lies in the locus of curves admitting the automorphism g, and V_t (t ≠ 0) leaves it.
- This is the typical behaviour when V_0 lies inside a symmetric locus: a covering construction, all of whose curves carry a deck group, deformed out of that locus.
- If g swaps two Y_0-labels x, gx of Q, it can happen that C(L_0) ∋ x and C(gL_0) = gC(L_0) ∌ x. Nothing local forbids this.

So "g fixes S pointwise" gives no control of lift-curves. Mode (F-a)/(F-b) of round11_q4 is exactly the situation "V_0 ⊂ Fix(g), V_t ⊄ Fix(g)", which is natural rather than exotic.

(Remark. The model contains no boundary data, i.e. no plumbing coordinates s_e. It only tests the group-theoretic claim. A version with boundary is obtained by adding coordinates on which N vanishes along curves in S; this changes nothing above.)

However, §3 shows that this symmetric-locus mechanism is **harmless for MS11♭**. The failure of step 4 does not produce a failure of MS11♭.

## 3. Proposition B: elements of K_S never cause a failure — proved (partial result)

**Proposition B.** Assume MS11♭'s setting. Suppose:
- (h1) some x-persistent anchored sheet T of β̃ lies in a 3-fold component X with X ⊇ S × {0};
- (h2) for some lift-curve L_0 ⊂ T, every h ∈ G_X lies in K_S·Stab_G(L_0).

Then MS11♭'s conclusion holds for (Q, β̃, b̃, x).

More precisely, (h2) can be weakened to:
- (h2′) there is a D-sheet Σ_b of b̃ in X whose lift-curve hL_0 (h ∈ G_X, Corollary A1) satisfies h ∈ Stab_pt(b̃)·Stab_G(L_0).

*Proof.*
1. By round11_q1 Lemma 3.1 (re-checked), D = X ∩ {N = 0} has a D-sheet Σ_b that is a transport sheet of b̃ and contains b̃ × {0}. The argument: b̃ × {0} ⊂ (S × {0}) ∩ {N = 0} ⊂ D; the D-sheet containing it is a 2-dimensional irreducible germ in q^{-1}(closure 𝓑) containing b̃ × {0}, so it is a transport sheet of b̃ by round11_q1 Lemma 2.2. So Σ_b is anchored.
2. By Lemma 2.1(c) of round11_q1, Σ_b contains a lift-curve, which lies in X. By Corollary A1(b) it is hL_0 with h ∈ G_X.
3. Write h = k h′ with k ∈ Stab_pt(b̃) and h′ ∈ Stab(L_0). Under (h2), k ∈ K_S ⊆ Stab_pt(b̃), since b̃ ⊂ S. Then hL_0 = kL_0.
4. k fixes b̃ pointwise, so kÑ_b̃ is the component of q^{-1}(N_b) containing k(b̃ ∖ 0) = b̃ ∖ 0. Hence kÑ_b̃ = Ñ_b̃.
   - Therefore k^{-1}Σ_b is an irreducible component of closure(Ñ_b̃) containing k^{-1}(b̃ × {0}) = b̃ × {0}, i.e. an anchored sheet of b̃.
   - It contains k^{-1}hL_0 = L_0.
5. By (P), Q is a puncture of the piece of b, so k^{-1}Σ_b is of boundary type. By round11_q1 Lemma 2.3 (P(Σ) = C(L) for every lift-curve L in a boundary-type sheet; this uses Y non-constant, which is part of MS11♭'s setting), P(k^{-1}Σ_b) = C(L_0).
6. x ∈ P(T) and L_0 ⊂ T, so x ∈ C(L_0) (evaluate on L_0). Hence x is Y-persistent on the anchored sheet k^{-1}Σ_b of b̃. ∎

**Consequence (what a failure of MS11♭ now requires).** Every 3-fold component containing S × {0} is of the form kX with k ∈ K_S: at a generic (p,0), p ∈ S, the components of q^{-1}(𝒳) form one K_S-orbit (proof of Lemma A4). If MS11♭ fails, then one of the following holds.
- **(R1) sheet-switching initial twist.** No x-persistent anchored sheet of β̃ lies in any 3-fold component containing S × {0}.
  - Let T ⊂ X_T. Then X_T ∩ {t = 0} ⊇ β̃ consists of chart sheets, and the one through β̃ that matters, S_T, is ≠ S.
  - So β̃ lies in two distinct chart sheets S ≠ S_T. (If S_T = S, then X_T ⊇ S × {0} and (h1) holds.)
  - Typical case: S_T = σS with σ ∈ Stab_pt(β̃) ∖ G_S. This is the "initial twist" of the brief, which must therefore also move the sheet S.
- **(R2) a local, non-global symmetry.** (h1) holds but (h2′) fails. Then some h ∈ G_X ∖ K_S·Stab(L_0) carries L_0 into a b̃-sheet. Such an h acts **non-trivially on X_0 = G_X·S** (Lemma A4):
  - either h ∈ G_S ∖ K_S acts on S as a non-trivial automorphism (e.g. the reflection of round11_q1 §5);
  - or hS ≠ S is another chart sheet in X_0.

  Moreover h ∉ Stab_pt(b̃)·Stab(L_0).

Compared with the planner's analysis, this removes all automorphisms of Q that are **global symmetries of the sheet** (elements of K_S: automorphisms of every curve of V_0 near Q on that sheet, for instance deck groups of covering constructions), whether or not V_t keeps them. In particular the §2 model, where G_X = K_S·H, is harmless. What remains is the case where the lost automorphism acts non-trivially on the t = 0 sheet (R2), or where β̃ lies in two chart sheets interchanged by a twist (R1).

This is a partial result in the sense of the task: it proves MS11♭ under the extra hypotheses (h1), (h2′). It does not answer the question.

**Remark (where (R1) might be removed: a suggestion, not proved).**
- MS11♭ as stated gives only *some* x-persistent anchored sheet T of β̃. In the chain, β̃_m comes with the chart sheet S_m of the canonical lift (Lemma S̃′).
- If the chain's induction claim were strengthened to "x_m is Y-persistent on an anchored sheet of β̃_m lying in a 3-fold component containing S_m × {0}", then (R1) would never arise, and Proposition B would reduce each non-product transition to (R2).
- This needs two things, neither of which I have proved:
  - (i) the base case (product-type Δ_Γ, where every sheet of every lift of ∂V_0 carries vertex i, so the base case is automatic);
  - (ii) the transfer along D^{m+1} preserving "lies in a 3-fold component containing the canonical sheet". This is a local question at generic points of the lifted piece: which 3-fold components through (p,0) contain a given transport sheet.
- The case of a product-type transition (Lemma PT / Cor. J′) would also have to output this stronger form.

## 4. Re-check of the chain at the points where MS11♭ enters

I checked the logic of steps 2(b)–(d) as stated in the brief. I did not re-audit the cited entries 84–87, 97–99, 112 (Prop. K_w and the R(D) repair, Lemma S̃′, Theorem X*_all).
- **(P) at genuine transitions.** If β̃′_m ≠ β̃_m, then J_m is in neither stratum(D^m) nor stratum(D^{m+1}). This is the contrapositive of entry 99, as used in 2(b). So J_m is a puncture of both pieces. Correct as stated.
- **(P) at the endpoint.**
  - For MERGE/pMOV, Q_0 ∉ stratum(E).
  - If Q_0 ∈ stratum(D^k), entry 99 gives b̃ = β̃. Then x is intact and constant along β̃ = b̃ and also MERGE/MOV along it, which is absurd.
  - An iMOV endpoint (Q_0 ∈ stratum(E)) likewise gives b̃ = β̃ by entry 99, and the same contradiction.
  - So in every surviving case Q_0 is a puncture of both pieces, as MS11♭ requires.
- **Use of the conclusion at the endpoint.** An anchored sheet contains b̃ × {0} by definition. So x Y-persistent on it gives x intact with F_x ≡ Y_0 along b̃, contradicting MERGE/MOV. Correct; no use of the false B1(a),(b).
- **Inductive use.** MS11♭'s output (an anchored sheet of the outgoing lift β̃′_m) is exactly the input format of the transfer step 2(c). This matches.
- **Logical status.** MS11♭ contains "Y non-constant". So, as the brief says, proving it amounts to proving the problem under (Rig). Proposition B is consistent with this: it uses Y non-constant only through round11_q1 Lemma 2.3.

No flaw found in the parts checked.

## 5. Summary

**Proved here** (modulo the cited run lemmas named in each proof — round11_q1 Lemmas 2.1(c), 2.2, 2.3, 3.1 — and standard local analytic geometry cited from memory):
1. **Lemma A**: for every point z of 𝒳 = q(X) at which 𝒳 is unibranch, the points of X over z form one G_X-orbit. In particular this holds at (Q_t, t) for all small t: 𝒳 = H(𝒮 × Δ) is unibranch there by a topological argument from (R2).
2. **Corollaries A1–A3**:
   - the lift-curves in X are exactly G_X·L_0;
   - (1L_X) ⇔ G_X ⊆ Stab_G(L_0) ⇔ the local monodromy of lift points is transitive on G_X/A, which forces G_X/A to be cyclic;
   - the planner's second failure mode reduces to the first.
3. **Lemma A4**: X_0 = G_X·S, and G_S ⊆ K_S·G_X.
4. **§2**: the planner's step-4 claim ("g ∈ G_X fixing S × {0} pointwise fixes L_0") is false in a consistent local model with V_0 inside a symmetric locus.
5. **Proposition B (partial)**: MS11♭ holds under (h1) together with (h2′), in particular when G_X ⊆ K_S·Stab(L_0). So automorphisms of Q that fix the t = 0 sheet pointwise, such as global symmetries like deck groups of covering constructions, never cause a failure, even when V_t loses them.

**Not proved:** MS11♭ itself, and hence the problem under (Rig). No counterexample is given.

**Open (precise):**
- **(R1)**: the x-persistent sheets of β̃ lie only in 3-fold components over chart sheets S_T ≠ S through β̃. This would be removed by the strengthened induction invariant of the Remark in §3, if the transfer step can be shown to preserve it.
- **(R2)**: an element h ∈ G_X ∖ K_S·Stab(L_0) that acts non-trivially on X_0 (as an automorphism of S, or by moving S to hS ≠ S) carries L_0 into a b̃-sheet. The known (β-fail) local model (round11_q1 §5, the reflection u ↦ −u) is of this type. Total geodesy (e.g. Lemma TG on Fix(h) ∩ S) is the natural tool, but I could not make it bite.
  - Heuristic I could not complete: in the reflection case the loop around the boundary curve in coarse V_0 has impure monodromy (it swaps the twin regions). Loops realised by cylinder shears or level rotation are pure. So such loops must wind an even number of times, which is an arithmetic (parity) condition on prong/plumbing orders rather than a contradiction.
- **(Rig)** (entry 82): untouched.

=== END OF ANSWER round12_q2 ===

