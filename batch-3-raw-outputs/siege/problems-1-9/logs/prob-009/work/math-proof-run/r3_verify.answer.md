# Referee report r3_verify

Scope: I read the whole draft (Status; §1; Section U; Part I §§0–8 including Proposition Ψ; the Bridge, L.1–L.3; Part II §§1–11 including Theorem 7.5, Appendix A, Lemmas F0/F1; Part III; Sections C, R, G). I checked every step for whether it follows *as written*. I re-derived the explicit formulas the document relies on:
- the collar Beltrami coefficient (Lemma PA);
- Lemma B's α and β;
- both hexagon cases of Lemma S, including the factorisation in Case 2;
- the Riemann–Hurwitz degree bound of Lemma F0;
- the deformation-space computation for elliptic tails in Remark C.9(d).

Classical facts are judged as the document states them; where I comment on whether a cited fact is true, that is from memory.

---

## (i) Errors and gaps, in order of severity

### Fatal
**None found.** No step that a main result needs is false, and every gap I found has a repair available from material already in the document.

### Serious but repairable

**S1. Part I §I.5.7, "Σ_i is a single label x with no internal edge", and the conclusions drawn from it.** The affected conclusions are "x is intact along β̃ and F_x ≡ Y_0 on β̃" at entry, the same statement at exit ("Persistence and exit"), and F_x(0) = Y_0, which §I.5.8 uses.

- *What is wrong.* The step argues by contradiction. It assumes Σ_i contains an internal chart edge f, and it needs the Σ_i-component of the fibres to be ≡ Y_0 along β̃ ∖ 0. For this it says: "Near z̃_{s_1} it equals the value of the constant vertex c_I, namely Y_0 (Lemma TI(4))."
- *Why it does not follow.* Lemma TI(4) only gives approximate statements: Λ(s_1) lies within o(1) of a point of K̂_D^k, and the c_I-coordinate of that point is Y_0. It does not show the following:
  - that the labelled image of the *chart point* z̃_{s_1} (partial normalisation at the pattern S(β̃), labelled through the U_J marking) lies exactly on the lifted piece Ê;
  - that this holds on an open subset of β̃.

  Without that, the identity principle has nothing to propagate: being within o(1) of Y_0 at one point does not give constancy.
- *Repair (inside the document, non-circular).* Bridge Lemma L.1, Steps 2–3, proves exactly the missing statement: ι∘Π_S maps (λ̃ ∩ B̃) ∖ 0 into Ê^m, for ι := θ_m∘κ with κ : G_S → G_{A_m}. Its proof uses only:
  - the first half of §5.7 ("A = node curves", which does not use the single-label claim);
  - Lemma TI(3);
  - Proposition Ψ(a), (c).

  So L.1 Steps 2–3 should be moved before the single-label step of §5.7, stated with the vertex w of G_S that contains the chart labels of Σ_i (not with {y}), and n_1 should be enlarged to n_2. With that order the contradiction goes through: the Σ_i-coordinate is constant Y_0 on Ê^m, so the length of α_f is constant along β̃ ∖ 0, while s_f → 0 at 0. The same repair covers the exit lift.
- *Severity.* The written justification is insufficient at a point the whole walk chain (Proposition K_w(2), (4), hence I.5) depends on. The fix is a reordering, but as written §5.7 does not prove its claim.

### Minor

**M1. Bridge Lemma L.2, Step 4.**
- The case analysis covers only dim X_l = 2 and dim X_l ≤ 1. It never says why dim X_l ≤ 2.
- Repair: closure(𝒱) is irreducible of dimension 3, and X lies over its intersection with closure(Δ_G) × Δ ⊂ ∂M̄_g × Δ, a proper analytic subset. So dim X ≤ 2 (q × id is finite).

**M2. Appendix A, Lemma A.1(1).**
- The step "Since b × Δ_ε is closed and H is a homeomorphism onto the closed set closure(𝒱), closure(N) ∩ Ω = H(b × Δ_ε) ∩ Ω" conflicts with Setting 6.0(i). There the branch disc is deliberately taken *open*, and A.0 imports that setting.
- Repair: use the closed disc b_c of 6.0(i), and shrink Ω inside M̄_g × Δ_{ε/2} so that it misses the compact set H(∂b_c × closed Δ_{ε/2}), which does not contain (J, 0).
- Part III §0.7 uses a closed disc and is not affected.

**M3. Status §0, item 3 (labelling).**
- The heading reads "Unconditional corollaries of Theorem B", but every result listed assumes (Rig). The body of the item says so, but the heading is wrong.
- The "three cases" do not match Corollary C.1 (a)–(c):
  - the third listed case ("the isotropy groups of the transported puncture points do not drop") is Corollary C.2;
  - C.1(c) (Aut(Q) = 1 at puncture points) is not mentioned.
- Repair: retitle the item "Corollaries of Theorem B under (Rig)" and list C.1(a), (b), (c) and C.2.

**M4. Lemma PA, Step 2 (and Lemma S̃′, Step 1): reading at orbifold points.**
- "v_n is a tangent vector of V_0" and "total geodesy puts that disc in V_0" need X̃_n to be a regular point of the relevant sheet of q^{-1}(V_0). V_0 may lie inside the locus of curves with automorphisms.
- This is achievable (choose τ_n generic) and is declared as a reading in §I.8, item 5. Lemma PA itself should say "choose τ_n generic"; §4.3, Step 2 already does.

**M5. Appendix A, Lemma A.6, Step 1.**
- The claim "for t outside a discrete set the components of W_t are exactly the curves n(a^{-1}(τ))" also needs distinct generic fibres of a to have distinct images in W.
- This holds off the finitely many fibre curves contained in the non-normal locus of W. The gap is harmless, since only the set-theoretic statement is used.

**M6. Remark U.8, global example.**
- The assertion that moving the p_k by diffeomorphisms of P¹ that are translations near the p_k "gives a stratum-preserving trivialisation satisfying (R1), (R2), (i), (ii)" of the blow-ups is asserted, not proved.
- It is a remark about M_{0,7}, not a result about M_g, and the document does not lean on it. It should be labelled a sketch.

**M7. Theorem U.6, step 1 (wording).**
- "V_t is irreducible: it is homeomorphic to V_0" is correct only together with V_t being a connected complex manifold (§II.1.2), so that connectedness implies irreducibility. One clause.

### Scope checks requested (all passed, apart from S1)

- **Fixed versus varying pants decompositions.** Lemma TI(3), §5.8, L.1 Step 2 and Proposition Ψ(d) all invoke Ψ(c) in its uniform form. Ψ(c) is proved uniformly: Lemma S is independent of P′, and the limit is identified by (Th). Correct.
- **Product-type versus non-product strata.**
  - Remark 3.2 (Π_t := H_t only for product type) is correctly confined.
  - Lemma 3.1 is used for non-product strata only under (R2^orb).
  - Lemma PT is used only for product-type strata (C.1(b), Remark 6.1).
  - Part III Lemmas 2.7 and 6.1 use product type only for Γ.
- **Coarse versus orbifold.**
  - Lemma 6.1(1), (2) are genuinely coarse.
  - Lemma 6.1(3)–(5), Propositions 5.1, 5.2 and Theorem 4.4 are correctly labelled [orb].
  - Appendix A and Part III use only (R1), (R2), (Rig) and the BB inputs.
- **t = 0 versus t ≠ 0.**
  - Part I is about t = 0 only.
  - Proposition 3.1 of Part III needs only 0 < |t| < ε, through Lemma 2.8. Correct.
  - Theorem 7.5 needs (AP) only on a disc, by the rescaling plus Lemma 2.3. Correct.

### Honesty of the readings

- **(R1)** (closure(𝒱) analytic) is an *additional* hypothesis. As far as I can see it is not implied by the problem's data: Remmert–Stein does not apply, because ∂M̄_g × Δ has dimension 3g − 3 ≥ 3 = dim 𝒱. The document states it as a reading, which is acceptable.
- **(R2)** encodes "smoothly trivial" together with (i) and (ii) as one global stratum-preserving homeomorphism. This is stronger than the literal hypotheses, which give stratum-wise trivialisations plus the closure compatibility (ii), not joint continuity across strata. The document says so explicitly in §1 and in Part II §1.3.
- **(R2^orb)** is much stronger again. Under (R2), Theorem 7.5 shows it is equivalent to (AP). The document never claims that (R2^orb) is the intended reading, and it states that the claim under (R2) alone is open.
- Every result names the reading it uses. Transparency is adequate.

---

## (ii) Verdict per main result

- **Theorem 7.5** ((R2) + (AP) ⇔ (R2^orb) ⇔ (Loc)): **proved.**
  - I checked (P1) and (P2)(i)–(v).
  - Path lifting at constant isotropy order: the local sections come from Fix(A) ∩ U, and their translates pass through any base point.
  - Uniqueness follows from Lemma 7.1.
  - Joint continuity: a slice neighbourhood of γ_0(r) is a slice neighbourhood of every γ_0(r′) it contains, because all these points have the same stabiliser K.
  - No gap.
- **Theorem A** ((R1) + (R2^orb)): **proved, modulo the Part I inputs and the cited facts**, with the following details.
  - Part II §§2–6, 9 and Lemmas F0/F1 are correct as written.
  - The cited facts are (Th) for cusped finite-area surfaces, (IS_c), (BC), (VT), (Bers), (Unif), (Kur)/(PN) and (St).
  - The input I.5 depends on Part I §5.7, which has gap S1. S1 is repairable, so Theorem A stands once S1 is repaired.
- **Corollary C.5:** **proved**, given Theorem 7.5 and Theorem A. The closedness of Z = {Aut ≠ 1} and the uniform-continuity step are correct.
- **Theorems C.7 and C.8:** **proved.**
  - Lemma C.7.0 is correct: the restriction of a closed quotient map to a saturated set is closed.
  - The contradiction argument is correct: the path c_n stays in one q(M_O), and the end point is translated into L_S^∘.
- **Remark C.9(d)** (elliptic tails): **correct, given the cited equivariant-Kuranishi fact.** I recomputed the action: ι acts by +1 on H¹(T, T_T(−p)) ≅ H¹(O_T) ⊗ H⁰(T_T) and by −1 on s_{e_T}.
- **Proposition C.10:** **proved.**
- **Theorem B** ((R1), (R2), (Rig), (NRT_P)): **proved under its hypotheses, modulo BB1**, whose labelled form BB1-M comes from L.1 and Part I §5.7 (repair S1).
  - I checked Lemmas 2.1–2.8, Proposition 3.1, Lemmas 1–3, Proposition 4, Lemma 5, the induction and the endpoint. No error found.
  - The "moreover" clauses are correct: the equivalence with the claim is formal, and the isotropy-drop argument is valid.
- **Corollaries C.1, C.2, C.3:** **correct** (under (Rig) where stated). There is a labelling mismatch in the Status (M3).
- **Section U:** **correct, modulo citations.**
  - U.1, U.2, U.3 (genus 2: I checked all graphs with Σ(2g_w − 2 + n_w) = 2) and U.4 are proved.
  - U.5 depends on Wright's finiteness theorem (JDG 2020), which as I remember it is stated correctly.
  - U.6 depends on Imayoshi–Shiga rigidity, Serre's lemma and K(π,1) theory.
  - U.7 is correct.
  - U.8 is an illustrative sketch (M6).
- **Part I other results** (TV, J0, X*_all, Proposition Ψ, IMOV_all): **correct as written.** The walk chain (Proposition K_w) is correct except for S1.
- **Bridge:** L.1 and L.3 are correct. L.2 is correct after the one-line repair M1.

---

## (iii) Explicit conclusions

- **The problem's main claim, as posed, is NOT proved by this document.** The document itself says so (Status §0, Section G). Under the coarse reading (R1) + (R2) it proves the claim only when (AP) holds on some disc around t = 0: in particular when (K_z) holds at every boundary point (Theorem C.7), or when no boundary point has a non-trivial automorphism (C.5). Otherwise the claim is reduced to the open statements (Rig) and (NRT_P).
- **Conditional theorems, under their stated hypotheses:**
  - **Theorem 7.5, C.5, C.7, C.8 and C.10 are proved.** C.5 and C.7 inherit Theorem A's dependence on Part I.
  - **Theorem A is proved under (R1) + (R2^orb)** (equivalently (R1) + (R2) + (AP)), modulo the cited classical facts, *provided* the Part I §5.7 gap S1 is repaired by moving Bridge L.1 Steps 2–3 ahead of it. That repair is available and non-circular.
  - **Theorem B is proved under (R1) + (R2) + (Rig) + (NRT_P)**, with the same proviso on S1 (through BB1-M).
  - **Section U results are proved**, modulo the cited theorems.

=== END OF ANSWER r3_verify ===
