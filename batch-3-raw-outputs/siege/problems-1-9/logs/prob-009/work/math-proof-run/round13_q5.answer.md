# round13_q5 — answer: (NRT) ⇒ MS8 (the Φ-chain)

**Status line.** PROVED (modulo the run's cited inputs listed in §0, which I use as stated and did not re-derive): under (R1), (R2), (Rig), a smooth closed totally geodesic V_0, Δ_Γ of product type with ∂V_t ≡ Y_t on factor i, and **(NRT)**, the assumption "t ↦ Y_t non-constant" leads to a contradiction. So (NRT) ⇒ MS8, and with (Rig) and entry 19 this gives the goal.

The route is shorter than the one the brief proposes:
- (NRT) is *equivalent* to the following statement at each point Q ∈ B_0 that has a boundary-type anchored sheet: the set C_Φ(L) of Φ-labels of a lift-curve L does not depend on L (Lemma 2).
- With that, MS11♭_Φ holds at **every** puncture point, product type or not, for any two lifted branches. It follows in a few lines from three facts: the lift-curves form one Aut(Q)-orbit, every sheet contains a lift-curve, and P_Φ = C_Φ (Prop. 3).
- The chain therefore does not need Mechanism D, the (β)-twists, (γ°), Lemma PT, Lemma J / Cor. J′, or Lemma 4.1. The residual cases (R-a), (R-b) of round12_q6 and (R1), (R2) of round12_q2 never arise. For completeness, §5 checks that each of them, and (γ°), is an instance of the (NRT) configuration.
- The only chain step that needs a new Φ-argument is the transfer along a piece (Lemma 5). There the tracked function may change from φ to another branch ψ ∈ Φ, and it can never become rigid.

No strengthening (NRT′) is needed.

---

## 0. Setting, notation, cited inputs

Readings and notation:
- Readings (R1), (R2) with H_0 = id; (Rig).
- Q ∈ B_0, chart Def(Q) with ball B, q, plumbing coordinates s_e, labels, F_y.
- Transport family Ñ_c̃, anchored sheet, lift-curve, Q_t := H_t(Q). All as in the task file.
- 𝔐 := M_{g_i,n_i}/S_{n_i}. [Z] denotes the class of an n_i-pointed curve Z in 𝔐.
- Y is assumed non-constant, for contradiction.

**Φ** (round12_q7 §1). Φ is the finite set of local branches φ at t = 0 of value curves Γ_{W,u} with:
- (g_u, n_u) = (g_i, n_i);
- φ(0) = Y_0;
- φ non-constant.

Here W ranges over the irreducible components of the lifted families 𝒲_G (all strata G; finitely many after shrinking Δ) and u over the constant vertices of W (u ∉ M_W). Γ_{W,u} := (pr_u, t)(W), mapped to 𝔐 × Δ, is an irreducible analytic curve, finite over Δ (R8-2 Lemma U). Y ∈ Φ: Y is holomorphic (entry 19), non-constant, and its graph is the value curve of vertex i of the lifted family of ∂V_t.

**P_Φ, C_Φ.**
- For an anchored sheet T: P_Φ(T) is the set of labels z that are Φ-persistent on T. That means there is φ ∈ Φ such that at every (p,t) ∈ T, z is intact and ([F_z(p)], t) lies on the branch φ.
- For a lift-curve L: C_Φ(L) is the set of labels z such that ([F_z(p)], t) lies on some branch φ ∈ Φ for all (p,t) ∈ L.

**Cited inputs, used as stated:**
- (I1) Lift-curves. Λ := {(p,t) : q(p) = Q_t}. Its components through (0,0) (the lift-curves) form **one Aut(Q)-orbit** (round11_q4 §2, notation; round12_q6 Lemma G1(a)). Λ ∩ {t = 0} = {(0,0)}. Every label is intact at every point of Λ, because Q_t ∈ Δ_{G_Q} (H preserves strata), so all s_e vanish there.
- (I2) Every anchored sheet (a 2-dimensional irreducible germ at (0,0)) contains a lift-curve (round11_q4 Lemma 2.1).
- (I3) Equivariance (K3): F_y(ap) ≅ F_{a^{-1}y}(p), and y is intact at ap iff a^{-1}y is intact at p, for a ∈ Aut(Q). Hence C_Φ(aL) = a·C_Φ(L), and aT is an anchored sheet of ac̃ if T is one of c̃ (round12_q1 Lemma F, whose proof does not use a c̃ = c̃ for these two statements).
- (I4) Lemma U / U3 of R8-2 under (Rig): let T be a boundary-type anchored sheet of a lifted branch c̃.
  - The map Π (partial normalisation) sends a dense open subset of T into one component W of the lifted family of the piece of c (round12_q7 Lemma 1.2, proof).
  - Every fibre component of W_t is K_W × {c_t}, with K_W a fixed irreducible compact curve and c_t[w] ∈ M_w holomorphic in t for w ∉ M_W.
  - F_W := K_W ∩ ∂(∏_{w∈M_W} M̄_w) is finite and independent of t.
- (I5) Lemma 1.1 of round12_q7 (R8-2 Theorem 1 for every φ ∈ Φ). Take t ∉ Z_Φ (a discrete set) and a φ(t)-copy y at a lift q of a point of B_t. Then along every lifted branch through q, y is STAY (intact, constant value φ(t), and (W, y) a φ-vertex) or IMOV. IMOV is impossible along a lifted branch of a piece having the point as a puncture.
- (I6) The chain's t = 0 skeleton, unchanged (entries 85, 98, 99; round11_q9 §§1, 2.3–2.5, 2.7, 2.8):
  - the walk chain with transitions J_m, lifts β̃_m, β̃′_m, labels x_m, and endpoint (Q_0, β̃, b̃, x) with x MERGE or MOV along b̃;
  - interior transitions are trivial (β̃′_m = β̃_m, same label);
  - (P) holds at every genuine transition and at the endpoint;
  - B1♭ (anchored sheets of any lifted branch exist, B1♭(a″)), and the transfer set-up of §2.7 (the sheet maps into a global component 𝒲̃ with 𝒲̃_0 ⊃ E, and the R(D)/marking identification x_m ↔ c ↔ x_{m+1}).

"Boundary-type" anchored sheet: an anchored sheet of a lifted branch c̃ whose piece has Q as a puncture.

---

## 1. Lemma 1 (values along a lift-curve: Φ or rigid) — proved

**Lemma 1.** Let Q ∈ B_0. Let L be a lift-curve contained in a boundary-type anchored sheet T, and let y be a label with F_y(0) ≅ Y_0. Then the germ of {([F_y(p)], t) : (p,t) ∈ L} is either a branch φ ∈ Φ or the constant germ {Y_0} × Δ. In the first case y ∈ C_Φ(L); in the second, y is a rigid Y_0-copy along L.

*Proof.*
1. *Labels along L.* By (I1), y is intact along L, and p ↦ F_y(p) is holomorphic on L. So λ_y : L → 𝔐 × Δ, (p,t) ↦ ([F_y(p)], t), is holomorphic. Since t|_L is finite, its image is an irreducible curve germ at ([F_y(0)], 0) = (Y_0, 0).
2. *Components of Q_t.* Let (p_*,t) ∈ L with t ≠ 0.
   - T is 2-dimensional and irreducible, and t ≢ 0 on T. So T_t has dimension ≥ 1 at p_*.
   - Λ_t is finite. So p_* is a limit of points p_n ∈ T_t lying over c_t ∖ Q_t, i.e. in the stratum of the piece of c.
   - By (I4), Π(p_n) = (κ_n, c_t) with κ_n ∈ K_W. Pass to a subsequence with κ_n → κ_∞ ∈ K_W, which is compact.
   - ξ̄ is continuous, so ξ̄(κ_∞, c_t) = Q_t. Q_t ∉ Δ_{G_c}, since Q is a puncture of the piece and H preserves strata. Hence κ_∞ lies in the boundary, i.e. κ_∞ ∈ F_W.
   - So every irreducible component of Q_t, with its special points, is of one of two kinds:
     - (a) a constant-vertex value c_t[w], w ∉ M_W, of class on Γ_{W,w}(t);
     - (b) a component of a coordinate of a point of F_W. Its class lies in the finite, t-independent set 𝔉_W.
3. *The dichotomy.* By step 2, the image of λ_y lies in the analytic curve 𝒢 := ⋃_{w∉M_W} Γ_{W,w} ∪ (𝔉_W × Δ) ⊂ 𝔐 × Δ.
   - An irreducible germ inside an analytic germ lies in one of its irreducible branches. That branch passes through (Y_0, 0).
   - So the branch is either a branch of some Γ_{W,w} at (Y_0, 0), or a constant germ {Y_0} × Δ (from 𝔉_W, or a constant branch of some Γ_{W,w}).
   - In the first case, if the branch is non-constant, it lies in Φ: w is a constant vertex of type (g_i, n_i), the type of F_y. Otherwise the branch is ≡ Y_0. ∎

## 2. Lemma 2 ((NRT) ⇔ C_Φ independent of the lift-curve) — proved

**Lemma 2.** Let Q ∈ B_0 have at least one boundary-type anchored sheet. Then (NRT) at Q is equivalent to: C_Φ(L) is Aut(Q)-invariant for one (equivalently, every) lift-curve L. In that case C_Φ(L′) = C_Φ(L) for all lift-curves L, L′ at Q.

*Proof.*
- Let T be a boundary-type anchored sheet. By (I2) it contains a lift-curve L_1.
- By (I1) every lift-curve is aL_1 for some a ∈ Aut(Q). It lies in aT, which is a boundary-type anchored sheet of ac̃ by (I3). So Lemma 1 applies to every lift-curve L at Q.

(⇒) Let x ∈ C_Φ(L) and a ∈ Aut(Q). If a^{-1}x = x, there is nothing to prove. Otherwise:
- F_{a^{-1}x}(0) ≅ F_x(a·0) = F_x(0) ≅ Y_0, by (I3), since a fixes the origin.
- By Lemma 1, a^{-1}x is either in C_Φ(L) or rigid (≡ Y_0) along L.
- The rigid case is exactly the configuration excluded by (NRT): Q ∈ B_0, a ∈ Aut(Q), a lift-curve L of Q_t, x ≠ a^{-1}x, x intact along L with value on a non-constant φ ∈ Φ, and a^{-1}x intact along L with value ≡ Y_0, for all small t.
- Hence a^{-1}x ∈ C_Φ(L). So C_Φ(L) is Aut(Q)-invariant.
- Then C_Φ(aL) = aC_Φ(L) = C_Φ(L) by (I3), and by (I1) this covers all lift-curves.

(⇐) Suppose an (NRT) configuration (a, L, x) exists. Then x ∈ C_Φ(L). But a^{-1}x ∉ C_Φ(L), since its value is the constant germ, which is not a branch in Φ. So C_Φ(L) is not invariant. ∎

## 3. Lemma 3 (P_Φ = C_Φ) and Proposition 4 (MS11♭_Φ everywhere) — proved

**Lemma 3 (Φ-version of round11_q4 Lemma 2.2).** Let T be a boundary-type anchored sheet at Q and L ⊂ T a lift-curve. Then P_Φ(T) = C_Φ(L). Moreover the function of y ∈ P_Φ(T) on T is its branch along L.

*Proof.*
- (⊂) Restrict to L ⊂ T.
- (⊃) Let y ∈ C_Φ(L) with branch φ. Let Γ ⊂ 𝔐 × Δ be the (closed analytic, after shrinking) union of the finitely many value curves. Put A_y := {(p,t) ∈ T : y intact at p and ([F_y(p)], t) ∈ Γ}. This is a closed analytic subset of T.
- For t ∉ Z_Φ (Z_Φ discrete), (p,t) ∈ L, y is a φ(t)-copy at the lift p of Q_t.
  - Every branch of T_t at p is a lifted branch of the transported piece c_t, and Q_t is a puncture of c_t.
  - By (I5), y is STAY along it: intact, with constant value φ(t).
  - So A_y contains the germ of T_t at (p,t), which is 1-dimensional (as in Lemma 1, step 2).
- This holds for uncountably many t. An analytic set of dimension ≤ 1 contains 1-dimensional t-slices for at most countably many t. Hence dim A_y = 2, and A_y = T by irreducibility.
- The map (p,t) ↦ ([F_y(p)], t) is holomorphic on the irreducible germ T and lands in Γ. So it lands in a single branch of Γ at (Y_0, 0) (the preimages of the branches are analytic and cover T).
- That branch contains the image of L, which is the branch φ. So it is φ, and y ∈ P_Φ(T) with function φ. ∎

**Proposition 4 (MS11♭_Φ, in a strong form).** Assume (NRT). Let Q ∈ B_0, let T and T′ be boundary-type anchored sheets at Q (of any lifted branches c̃, c̃′, equal or not, product type or not), and let x ∈ P_Φ(T). Then x ∈ P_Φ(T′). Moreover, if T′ is an anchored sheet of c̃′, then at t = 0 the label x is intact along c̃′ near 0 with F_x ≡ Y_0.

*Proof.*
- Choose lift-curves L ⊂ T and L′ ⊂ T′ (I2).
- By Lemma 3, x ∈ C_Φ(L). By Lemma 2, C_Φ(L′) = C_Φ(L) ∋ x. By Lemma 3 for T′, x ∈ P_Φ(T′).
- For the last claim, let ψ be the function of x on T′. Then c̃′ × {0} ⊂ T′ and x is intact on T′.
- ψ is a branch of a curve finite over Δ, so its germ meets {t = 0} only in (Y_0, 0). Hence [F_x] ≡ Y_0 on c̃′ near 0. ∎

In particular, MS11♭_Φ holds for every admissible datum. Note that (S) is not needed, and neither is β̃ ≠ b̃.

## 4. The Φ-chain — the derivation (NRT) + (R1), (R2), (Rig), Y non-constant ⇒ contradiction

**Induction claim (C_m).** x_m ∈ P_Φ(T) for some anchored sheet T of β̃_m, with some function φ_m ∈ Φ, which may vary with m.

1. **Base.** Δ_Γ is of product type. Vertex i is Y-persistent on every sheet of every lift of a branch of D^1 (round11_q9 §2.5). Since Y ∈ Φ, (C_1) holds with φ_1 = Y.
2. **Interior transitions and R(D)-points.** By (I6), β̃′_m = β̃_m and the label is unchanged. So the anchored sheets are the same, and the claim passes unchanged.
3. **Puncture transitions** (product or non-product, β̃′_m ≠ β̃_m or not). J_m is a puncture of D^m and of D^{m+1} (I6). So the anchored sheets of β̃_m and β̃′_m are of boundary type, and anchored sheets of β̃′_m exist (B1♭(a″)). Proposition 4 gives x_m ∈ P_Φ(T′) for every anchored sheet T′ of β̃′_m. (Lemma PT and Lemma J / Cor. J′ are not used. The question whether "pinned" contradicts a varying φ therefore does not arise.)
4. **Transfer along D^{m+1}** (Lemma 5 below): (C_m) on β̃′_m gives (C_{m+1}).
5. **Endpoint** (product or non-product). (P) holds at Q_0 (I6), so anchored sheets of b̃ are of boundary type. By (C_k) and Proposition 4, x is intact along b̃ near 0 with [F_x] ≡ Y_0.
   - The pattern is constant on b̃ ∖ 0, and F_x is holomorphic on L_x. So, by the identity theorem along the normalisation of b̃ (as in round11_q9 §2.8), x is intact along all of b̃ ∩ B with [F_x] ≡ [Y_0].
   - This contradicts MERGE (an edge at x is unpinched along b̃) and MOV ([F_x(z̃^∞)] ≠ [Y_0]).

Hence Y is constant, i.e. MS8 holds, and Y_t = Y_0 by entry 19. ∎

**Lemma 5 (Φ-transfer).** Let T be an anchored sheet of β̃′_m with x_m ∈ P_Φ(T), function φ. Then there is an anchored sheet T″ of β̃_{m+1} with x_{m+1} ∈ P_Φ(T″), with some function ψ ∈ Φ (possibly ψ ≠ φ).

*Proof.*
- Follow round11_q9 §2.7 verbatim:
  - Π_S of the relevant component of Ñ_{β̃′_m} lies in one global component 𝒲̃ of the lifted family of D^{m+1}, with 𝒲̃_0 ⊃ E.
  - x_m corresponds to a vertex c. c is constant on E with value Y_0 (x_m is intact with [F] ≡ Y_0 along β̃′_m, by the last clause of Prop. 4 applied to T itself). So c ∉ M_{𝒲̃} by U1.
  - At J_{m+1} there is a β̃_{m+1}-sheet T″ = closure(Ñ″^1) with Π(Ñ″^1) ⊂ 𝒲̃.
  - On T″ the label x_{m+1} ↔ c is intact (constant pattern; closedness), and ([F_{x_{m+1}}(p)], t) = ([c_t[c]], t) lies on Γ := Γ_{𝒲̃,c} (closedness again).
- The only change from the Y-version is the replacement of Lemma S(c) ("persistence holds on all of 𝒲̃"). It is replaced by the following observation.
  - Γ is irreducible, as the image of the irreducible 𝒲̃ under the proper map (pr_c, t).
  - The image of T contains the non-constant branch φ, so Γ ≠ {Y_0} × Δ.
  - If Γ had a constant branch {Y_0} × D at (Y_0, 0), then Γ ∩ ({Y_0} × Δ) would be a 1-dimensional analytic subset of the irreducible curve Γ, hence all of Γ. That is a contradiction.
  - So **every** branch of Γ at (Y_0, 0) is non-constant, i.e. lies in Φ (𝒲̃ is one of the W defining Φ).
- T″ is an irreducible germ, and its value map is holomorphic into Γ, with value (Y_0, 0) at the origin. At t = 0, x_{m+1} is intact at 0 with F ≅ Y_0, the constant value of c on E.
- So the image of T″ lies in a single branch ψ of Γ at (Y_0, 0), and ψ ∈ Φ. Hence x_{m+1} ∈ P_Φ(T″) with function ψ. ∎

**Product-type endpoint and genericity.** These are now covered by step 5 and by Lemma 3 (Z_Φ discrete). The "Y_t lies in a finite set on an open set" argument of the original product-type endpoint is not needed.

## 5. The items of the brief, and the residual cases

- **Lemma PT, Lemma J / Cor. J′.** Not used; step 3 covers product-type puncture transitions as well. (So the question whether "pinned" still gives a contradiction for a varying φ does not have to be decided.)
- **Transfer.** Lemma 5. The tracked function can change, but only to another branch of the same irreducible value curve, and it can never become rigid.
- **P(T) = C(L), Φ-version.** Lemma 3 (from (I5) = round12_q7 Lemma 1.1).
- **Mechanism D, (β)-twists, initial twist, (γ°).** Not used. Consistency checks:
  - (β)/initial twist with a rigid twin y = σ^{-1}x on T (round12_q7 (R-twin)): restricted to a lift-curve L ⊂ T (I2), this is an (NRT) configuration with a = σ. With a non-rigid twin, Prop. 2.1 of round12_q7 already passes it.
  - (γ°): round12_q8 Lemma 3 gives, along a lift-curve λ ⊂ T_1, F_x(λ(t)) on the tracked branch and F_{g^{-1}x}(λ(t)) ≡ Y_0, with g^{-1}x ≠ x (Lemma 1 there).
    - Its proof uses only that x is persistent on T_1 with its function (the value of x along λ is then that function, φ or Y) and that u = g^{-1}x ∈ M_W (a value in a finite set, hence ≡ Y_0). So it holds verbatim for a tracked φ ≠ Y.
    - So (γ°) is an (NRT) configuration (a = g, L = λ).
  - Endpoint rigidity (round12_q7 Lemma 4.1): L_b = aL_β with x rigid along L_b, i.e. a^{-1}x rigid along L_β while x ∈ C_Φ(L_β). This is an (NRT) configuration.
- **(R-a), (R-b)** (round12_q6 §4) and **(R1), (R2)** (round12_q2 §3). These are failure modes of particular routes to MS11♭ (through a 3-fold component X, an initial twist, or Stab(b̃)-transfer). The derivation of §4 does not go through any of them. More precisely, any failure of MS11♭_Φ at (Q, β̃, b̃, x), whatever its mechanism, gives an (NRT) configuration. Take lift-curves L_β ⊂ T_β, L_b ⊂ T_b, and a with L_b = aL_β (I1). If x ∉ C_Φ(L_b), then a^{-1}x ∉ C_Φ(L_β), so by Lemma 1 a^{-1}x is rigid along L_β, while x ∈ C_Φ(L_β).

## 6. Summary

**Proved** (modulo the cited inputs (I1)–(I6): R8-2 Lemma U/U3 and Theorem 1 under (Rig), round12_q7 Lemma 1.1, round11_q4 Lemma 2.1, round12_q6 Lemma G1(a), the walk chain with entries 85, 98, 99, B1♭ and the §2.7 transfer set-up and marking identification, entry 19):
- Lemma 1: along a lift-curve, every Y_0-copy has value either in Φ or ≡ Y_0.
- Lemma 2: (NRT) at Q ⇔ C_Φ(L) is Aut(Q)-invariant ⇔ C_Φ(L) is independent of L.
- Lemma 3: P_Φ(T) = C_Φ(L) for boundary-type anchored sheets.
- Proposition 4: under (NRT), Φ-persistence passes between any two boundary-type anchored sheets at Q; this gives MS11♭_Φ in full, without (S) and without the product/non-product distinction.
- Lemma 5: the Φ-transfer along a piece. The function may change within one irreducible value curve, all of whose branches at (Y_0, 0) are non-constant.
- §4: **(NRT) + (R1), (R2), (Rig) + Y non-constant ⇒ contradiction**, i.e. (NRT) ⇒ MS8, and with entry 82 ((Rig)) and entry 19 the problem's conclusion follows.

**Not proved / open:**
- (NRT) itself: exclude a rigid Y_0-copy and a Φ-copy of Y_0 exchanged by some a ∈ Aut(Q) along a lift-curve. By Lemma 2 this is now the single remaining twin statement. It is needed only at the finitely many puncture transitions and at the endpoint of the walk. By §5, every earlier residual obstruction is an instance of it.
- (Rig) (entry 82): untouched.
- The inherited inputs (I1)–(I6) were not re-derived here. In particular the marking identification x_m ↔ c ↔ x_{m+1} of §2.7 / R(D) was flagged earlier as "routine, inherited".

proved: the implication (NRT) ⇒ MS8 (Φ-chain), in the form above. not proved: (NRT). open: (NRT), (Rig).

=== END OF ANSWER round13_q5 ===
