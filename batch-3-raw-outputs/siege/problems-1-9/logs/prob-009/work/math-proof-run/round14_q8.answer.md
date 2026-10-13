# round14_q8 — check of round13_q5 ((NRT_P) ⇒ MS8)

**Plan/status.** I checked round13_q5 step by step against the spliced inputs: Lemma 1, Lemma 2, Lemma 3, Prop. 4, §4 (base, interior transitions, puncture transitions, Lemma 5, endpoint) and §5.

**Verdict in one line.** CORRECT after five minor repairs (R-i)–(R-v) below. None of the repairs changes a statement; they only make explicit points that were implicit. round13_q5 proves:
- (NRT_P) + (R1), (R2) (with H_0 = id) + (Rig) + "Y non-constant" ⇒ contradiction;
- hence (NRT_P) ⇒ MS8;

modulo the cited inputs (I1)–(I6), entry 19, and the inherited marking identification (round11_q9 §2.4, "routine", not re-derived by anyone). (NRT) is used only at puncture points, so it may be read as (NRT_P).

Readings throughout: (R1), (R2) with H_0 = id, (Rig), and the definitions of the task file. [Z] is the class in 𝔐 = M_{g_i,n_i}/S_{n_i}.

---

## 0. The cited inputs: located and checked against their use

- **(I1)** Located: round11_q4 §2 (notation) and round12_q6 Lemma G1(a).
  - G1(a) says exactly what is used: Λ = ⋃_{g∈A} gL_0 near (0,0), i.e. the lift-curves form one Aut(Q)-orbit, and Λ ∩ {t=0} = {(0,0)} because q^{-1}(Q) = {0}.
  - Its proof is valid. Λ is the preimage of the irreducible germ {(Q_t,t)} under the finite quotient q × id, and t|_{L_0} is finite.
  - "Every label is intact on Λ" is also valid. Q_t ∈ Δ_{G_Q} because H preserves strata, and the points of Def(Q) over Δ_{G_Q} are exactly {s_e = 0 for all e}.
- **(I2)** Located: round11_q4 Lemma 2.1 (stated for sheets as germs at (0,0), which covers anchored sheets).
  - Proof re-checked. Σ_c is irreducible: its dense part H((c∖Q)×Δ) is a connected 4-manifold and the rest has real codimension 2. Then (q×id)(T) = Σ_c by Remmert, so T ∩ Λ surjects onto a t-neighbourhood of 0 and contains a lift-curve.
  - One point is implicit there: the points of T ∩ Λ tend to (0,0) as t → 0. This holds after shrinking ε relative to B, because q^{-1}(Q) = {0}. Valid.
- **(I3)** Located: round12_q1 Lemma F. Lemma F is stated under a c̃ = c̃, but the two facts round13_q5 needs do not use that hypothesis.
  - **C(aL) = aC(L).** Lemma F(4) uses only (K3) and the Aut(Q)-invariance of Λ. Its Φ-version C_Φ(aL) = aC_Φ(L) is the same computation.
  - **aT is an anchored sheet of ac̃.** In the proof of F(1), aÑ_c̃ is the connected component of the a-invariant set q^{-1}(H((c∖Q)×Δ_ε)) ∩ (B×Δ_ε) that contains a(c̃∖0), so aÑ_c̃ = Ñ_{ac̃}. Then a maps closure(Ñ_c̃) to closure(Ñ_{ac̃}) component by component, and aT ⊃ ac̃ × {0}.
  - Moreover ac̃ is a lift of the same coarse branch c. So aT is again of boundary type. Valid.
- **(I4)** Located: R8-2 Lemma U, U1, U3, U4, and the proof of round12_q7 Lemma 1.2.
  - They say what is used: each fibre component of W_t is K_W × {c_D} with c_D ∈ ∏_{w∉M_W} M_w; F_W = K_W ∩ ∂ is finite and t-independent; Γ_{W,u} is an irreducible curve, finite over Δ.
  - See (R-i) for a strengthening of "dense open subset of T ↦ W".
- **(I5)** Located: round12_q7 Lemma 1.1. It is stated exactly as used. Its proof is R8-2 Theorem 1 with Y replaced by φ. See (R-ii) for multivalued branches.
- **(I6)** Located: round11_q9.
  - Walk chain: §1.1, S̃′.
  - Interior transitions and R(D)-points are trivial: §1.2.
  - Genuine transitions satisfy (P), as the contrapositive of IMOV_all(a), §1.2. So J_m is a puncture of **both** D^m and D^{m+1}.
  - (P) at the endpoint (Q_0 a puncture of D^k and of E_b): §1.2.
  - B1♭(a″): §2.3. The §2.7 transfer set-up: 𝒲̃ with 𝒲̃_0 ⊃ E, and Π(Ñ″^1) ⊂ 𝒲̃.
  - The marking identification x_m ↔ c ↔ x_{m+1}: §2.4. It is accepted there as "routine, inherited" and I did not re-derive it.
  - Side remark (an identification of definitions): a c̃-sheet (its t=0 slice contains an open subset of c̃∖0) is the same as an anchored sheet. The sheet is closed and c̃ ∩ B is irreducible, so the sheet contains c̃ × {0}. The converse is clear. So B1♭(a″) supplies anchored sheets.

---

## 1. Lemma 1 — CORRECT (with repair (R-i))

**Step 1.** L is an irreducible curve germ and y is intact on L (I1). F_y is holomorphic on the locus L_y where y is intact, so λ_y is holomorphic. t|_L is finite, so the image is an irreducible 1-dimensional germ at (Y_0,0). Valid.

**Step 2.** Brief's points: limits κ_n → κ_∞ ∈ F_W; continuity of ξ̄; use of Q_t ∉ Δ_{G_c}. All are valid, once the following is made explicit.

- **(R-i) Π is defined and continuous on all of T, and (Π,t)(T) ⊂ W.** Let S be the generic pattern of T (the pattern of c̃). By closedness, T ⊂ {s_e = 0 for all e ∈ S}, which is the domain of the continuous map Π = Π_S into ∏M̄_w. Since W is closed and (I4) gives a dense open subset of T mapping into W, we get (Π,t)(T) ⊂ W.
- So there is no need to know whether the p_n lie in "the" dense open set. In fact Π(p_*) = lim Π(p_n) directly.
- **Choice of fibre component.** W_t may have several components K_W × {c_D}. Pass to a subsequence lying in one of them. "c_t" in the text should be read as this c_D.
- **Why κ_∞ is in the boundary.** ξ̄_G : ∏M̄_w → M̄_g is the continuous gluing morphism, and ξ̄∘Π = q on the closure. So ξ̄(κ_∞, c_D) = q(p_*) = Q_t.
  - Q ∉ Δ_{G_c} by boundary type, and H_t preserves strata. So Q_t ∉ Δ_{G_c} = ξ(∏M_w).
  - c_D has interior coordinates, so κ_∞ ∈ ∂. Hence κ_∞ ∈ F_W. Correct.
- **The components of Q_t.** Every component of the glued curve ξ̄(κ_∞,c_D), with its special points, is either some c_D[w] (w ∉ M_W) or a component of a coordinate of κ_∞. Gluing turns marked points into nodes and leaves the set of special points of a component unchanged, as in R8-3 Lemma 1 (⊇). F_y(p_*) is a component of q(p_*) = Q_t. So the dichotomy (a)/(b) holds.

**Step 3.**
- 𝒢 is closed analytic: it is a finite union of the curves Γ_{W,w} (images under proper maps, contained in M_w × Δ, mapped to 𝔐) and of finitely many lines {f} × Δ.
- Only vertices w of type (g_i,n_i) matter, because the type of F_y is constant along L.
- The image germ minus the origin lies in 𝒢, and 𝒢 is closed. So the image germ lies in one irreducible branch of 𝒢 through (Y_0,0).
- A non-constant such branch belongs to Φ, since Φ ranges over all components of all 𝒲_G. Otherwise the image germ is {Y_0} × Δ.
- The image germ is irreducible and 1-dimensional, so "contained in φ" means "equal to φ". Valid.

---

## 2. Lemma 2 — CORRECT

- A boundary-type anchored sheet exists at every puncture point (B1♭(a″)). By (I2) it contains a lift-curve L_1. By (I1) and (I3), every lift-curve aL_1 lies in the boundary-type sheet aT. So Lemma 1 applies to every lift-curve.
- **(⇒).** The step F_{a^{-1}x}(0) ≅ F_x(a·0) = F_x(0) ≅ Y_0 is valid: (I3) with p = 0, and F_x(0) ≅ Y_0 because φ(0) = Y_0.
  - By Lemma 1, a^{-1}x is either in C_Φ(L) or rigid along L. The rigid case is literally the configuration excluded by (NRT_P), with Q a puncture point.
  - The case a^{-1}x = x is trivial. A label cannot be both on a non-constant branch and ≡ Y_0.
  - Invariance under Aut(Q) then gives C_Φ(aL) = aC_Φ(L) = C_Φ(L).
- **(⇐).** Valid.
- "Puncture point" (some branch c with c∖Q in a stratum other than Δ_{G_Q}) is equivalent to "Q ∉ Δ_{G_c}", i.e. to boundary type. Valid.

---

## 3. Lemma 3 — CORRECT (with repairs (R-ii), (R-iii))

**(⊂).** Restrict to L ⊂ T.

**(⊃), analyticity.** A_y is a closed analytic subset of T: L_y is closed analytic, F_y is holomorphic on it, and Γ is a finite union of closed analytic curves.

**(⊃), the generic slice.**
- q(T) ⊂ closure H((c∖Q)×Δ), which equals H(c×Δ) near Q. So T_t ⊂ q^{-1}(c_t), where c_t = H_t(c) is one irreducible branch at Q_t (a disc).
- T_t is 1-dimensional at p, since t ≢ 0 on the irreducible 2-dimensional T. So every branch of T_t at p is a lifted branch of c_t.
- Q_t ∉ Δ_{G_c} ⊃ c_t ∖ Q_t, so Q_t is a puncture of the piece. IMOV requires Q ∈ Δ_{G_b}, so IMOV is excluded and (I5) gives STAY.
- So y is intact with constant value [F_y(p)], and ([F_y(p)],t) ∈ φ ⊂ Γ. Hence A_y contains the germ of T_t at p.

**(R-ii) Multivalued branches.** A branch φ ∈ Φ may be a Puiseux branch of degree > 1, so "φ(t)" is multivalued.
- Read "φ(t)-copy" as "class equal to a point of φ over t".
- Read Z_φ as the set of t such that some point of φ over t lies in 𝔉, or lies on a value curve that does not contain the germ φ, or lies on another φ′ ∈ Φ. Each irreducible value curve either contains φ or meets it only at the origin after shrinking, so Z_φ is still discrete.
- With this reading the proof of R8-2 Theorem 1 goes through unchanged: steps 1, 2, 4 use the value ∉ 𝔉, and step 3 uses that Γ_{W,y} ∋ (value, t) forces Γ_{W,y} ⊃ φ. So (I5) holds as used.

**The countability argument.** If dim A_y ≤ 1, a 1-dimensional slice A_y ∩ {t = t_0} means that some 1-dimensional component of A_y lies in {t = t_0}. There are countably many components, each in at most one level. Valid.

**(R-iii) Germ conventions.** To conclude A_y = T from dim A_y = 2, use a representative of the irreducible germ T on a small neighbourhood U on which T ∩ U is irreducible; such U exist for an irreducible germ (local parametrisation). The uncountably many slices occur inside every such U, because L reaches every small t. So A_y ∩ U = T ∩ U.

**Single branch.** The preimages of the finitely many branches of Γ at (Y_0,0) are analytic germs covering the irreducible germ T, so one of them is T. That branch contains the image of L, which is the 1-dimensional germ φ, so it equals φ. Valid.

---

## 4. Proposition 4 — CORRECT

- The first part is Lemma 3, then Lemma 2 at Q (which has the boundary-type sheet T), then Lemma 3 again.
- **Last clause.** ψ is a branch of a curve finite over Δ, so a representative meets {t=0} only in (Y_0,0). [F_x] is continuous on c̃′ and lies on ψ, so [F_x] ≡ Y_0 on c̃′ near 0.
- Moreover x is intact on all of c̃′ ∩ B, because c̃′ × {0} ⊂ T′. This clause uses only x ∈ P_Φ(T′), **not** (NRT). That matters for Lemma 5, where it is applied with T′ = T.

---

## 5. §4, the induction — CORRECT (with repairs (R-iv), (R-v))

- **Base.**
  - Vertex i is constant on the pieces of ∂V_t in Δ_Γ, so i ∉ M_W.
  - Γ_{W,i} is the graph of the holomorphic, non-constant Y (entry 19), so Y ∈ Φ.
  - Y-persistence is Φ-persistence with φ = Y (round11_q9 §2.5 gives it on every sheet). Anchored sheets of β̃_1 exist (B1♭(a″)). Valid.
- **Interior and R(D) transitions.** (I6) gives β̃′_m = β̃_m with the same label. So a sheet of one is a sheet of the other. Valid.
- **(R-iv) Puncture transitions.** Step 3 says "J_m is a puncture of D^m and of D^{m+1}" for every transition, "β̃′_m ≠ β̃_m or not". That is not justified for a non-genuine transition lying in the stratum of D^m or of D^{m+1}. Repair: split the transitions.
  - (a) J_m lies in the stratum of D^m or of D^{m+1}. Then β̃′_m = β̃_m (entry 99), and step 2 applies.
  - (b) Otherwise J_m is a puncture of both. Then Prop. 4 applies at the puncture point J_m, whether or not β̃′_m = β̃_m.
  
  The two cases are exhaustive, so nothing is lost.
- **Lemma 5.** Brief's points: the identification x_{m+1} ↔ c, the value of x_m on β̃′_m, and "every branch of Γ is non-constant".
  - **Value of x_m on β̃′_m.** By the last clause of Prop. 4 with T′ = T (no NRT needed), x_m is intact with [F] ≡ Y_0 along β̃′_m. Intactness makes c = {x_m} a single vertex of G_S, whose coordinate is F_{x_m}. It is constant on the open arc Π(β̃′_m) ⊂ E, hence constant on the component E of 𝒲̃_0, and c ∉ M_𝒲̃ by U1. Valid.
  - **(R-v) What the step "Γ ⊃ φ" uses.** It uses the identification x_m ↔ c **at J_m**, as well as at J_{m+1}: on Ñ′^1, F_{x_m} is the c-coordinate of Π_S, which lies in Γ_{𝒲̃,c}. Both identifications are the inherited marking identification of round11_q9 §2.4/§2.7. Given that, x_m ∈ P_Φ(T) with function φ, and closedness gives φ ⊂ Γ := Γ_{𝒲̃,c}.
  - **Irreducibility of Γ.** 𝒲̃ is irreducible and (pr_c,t) is proper on it (𝒲 is proper over Δ), so Γ is irreducible. This must be read over the disc on which 𝒲̃ is irreducible; it is a global, not a germ, statement. The argument uses only that.
  - **No constant branch.** Suppose Γ had a constant branch at (Y_0,0). Then Γ ∩ ({Y_0}×Δ) would be a 1-dimensional analytic subset of the irreducible 1-dimensional Γ, hence all of Γ. That contradicts Γ ⊃ φ with φ non-constant.
  - **So every branch of Γ at (Y_0,0) lies in Φ.** The vertex c has type (g_i,n_i), and 𝒲̃ is a 2-dimensional component of some 𝒲_G. Valid.
  - **T″.** On Ñ″^1, x_{m+1} ↔ c is intact: c is a single vertex, the pattern is constant on Ñ″, and intactness is closed. Its value lies on Γ, and by continuity on all of T″.
  - The value at the origin is Y_0, as the limit along β̃_{m+1} ⊂ Π^{-1}(E) of c ≡ Y_0.
  - If the global T″ has a reducible germ at (0,0), take the germ component containing β̃_{m+1} × {0}; it is an anchored germ sheet.
  - The value map on that irreducible germ lands in a single branch ψ ∈ Φ. Valid.
- **Endpoint.**
  - (P) at Q_0 (I6) makes the anchored sheets of β̃ and of b̃ of boundary type. Q_0 is a puncture point.
  - Prop. 4 gives x intact on b̃ ∩ B and [F_x] ≡ Y_0 near 0. MERGE is contradicted at once.
  - **MOV.** b̃ ∩ B is irreducible in a Milnor ball, so its normalisation is a connected disc. [F_x] is a holomorphic map from it into the analytic space 𝔐 that is constant on an open set. By the identity theorem it is constant, so [F_x(z̃^∞)] = [Y_0], which contradicts MOV. Valid.
  - The case k = 1 (no transitions) is the same argument.
- **Only puncture points are used.** (NRT) enters only through Lemma 2, which is invoked only inside Prop. 4. Prop. 4 is used only at puncture transitions (case (b)) and at Q_0, which is a puncture point by (P). So "(NRT) at Q" may be read as (NRT_P). Confirmed.

---

## 6. §5 — consistent; not load-bearing

The reductions of (β)/initial twists, (γ°) and Lemma 4.1 to (NRT_P) configurations are consistent with Lemma 1 and (I1). They are not used in §4, so they need no check for the chain.

---

## 7. Verdict / repairs / remaining dependencies

**Verdict.** round13_q5 proves exactly the following: under (R1), (R2) with H_0 = id and (Rig), with V_0 smooth, closed and totally geodesic and Δ_Γ of product type, **(NRT_P) + "t ↦ Y_t non-constant" ⇒ contradiction**. Hence (NRT_P) ⇒ MS8, and with entry 19, Y_t = Y_0.

**Repairs** (all minor, all made above):
- **(R-i)** (Π,t)(T) ⊂ W on all of T, by continuity and closedness. Pass to a subsequence inside one fibre component K_W × {c_D}.
- **(R-ii)** Reading of φ(t) and Z_φ for multivalued Puiseux branches. (I5) holds in this reading.
- **(R-iii)** Germ-representative conventions in Lemma 3, and in Lemma 5 for T″.
- **(R-iv)** Step 3 is restricted to transitions where J_m is a puncture of both pieces; the others fall under step 2.
- **(R-v)** Lemma 5 uses the marking identification x_m ↔ c at J_m as well as at J_{m+1}, and the irreducibility of 𝒲̃ over the disc in use.

**Remaining dependencies.**
- Cited inputs, used as stated and not re-derived here:
  - (I1) round12_q6 G1(a);
  - (I2) round11_q4 L2.1;
  - (I3) round12_q1 Lemma F, proof;
  - (I4) R8-2 Lemma U/U1/U3/U4 and round12_q7 L1.2;
  - (I5) round12_q7 L1.1 / R8-2 Theorem 1;
  - (I6) round11_q9 §§1.2, 2.3–2.5, 2.7, 2.8, i.e. the walk chain with entries 85, 98, 99 and S̃′;
  - entry 19.
  
  I re-checked the proofs of (I1), (I2), (I3) and the Lemma U statements as spliced.
- The marking identification of round11_q9 §2.4: inherited as "routine" and never re-derived. It is used twice in Lemma 5.
- **Open:** (NRT_P) itself (entry 141).
- **Open:** (Rig) (entry 82). It is needed for the problem's conclusion in addition to MS8.
- The problem's hypotheses are used only through the readings (R1), (R2).

=== END OF ANSWER round14_q8 ===
