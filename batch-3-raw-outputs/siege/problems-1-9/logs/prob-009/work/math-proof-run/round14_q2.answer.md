# round14_q2 — attempt on (NRT_P)

**Plan/status line.** NOT PROVED, and no global counterexample. I work under the readings (R1) and (R2) with H_0 = id (coarse), together with (Rig), as in the task file. The orbifold reading (R2^orb) is not used. This file contains:

- §1. A check of the derivation (NRT_P) ⇒ MS8 ⇒ claim. I found no flaw. One remark: the chain uses (NRT_P) only through a strictly weaker consequence.
- §2. Proposition A (proved): an exact description of (NRT_P) failures in terms of the (Rig) data of a single lifted family W.
- §3. A correction to the planner's sketch, item 2. A case-(A) failure does **not** need a split lifted family W ≠ σW over the same t = 0 lifted piece. That is needed only when σÊ = Ê.
- §4. A chart-level model of an (NRT_P) failure **at the puncture point Q itself** (proved as a local statement). In it:
  - coarse 𝒱 is smooth;
  - (R1), (R2), (i), (ii) hold in the chart;
  - (Rig) holds for both pieces through Q, and their moving parts are t-independent;
  - Theorem N / Lemma 1.1 hold at Q_t;
  - Fix(a) ∩ X = c̃′ × {0}. So **no curve of V_t, t ≠ 0, near Q has the lost automorphism**: there is no detaching mirror and no family 𝒵/𝒟 of symmetric curves.
  - The chain's actual requirement (MS11♭_Φ, "some sheet") holds in the model even though (NRT_P) fails there.
- §5. Consequences for strategy, and the list of what is proved and what is open.

Throughout, "chart-level" means a model of germs at (Q,0). By the task's rules such a model is not a counterexample. It only shows what local arguments, and the global objects tried in round 13, cannot do.

---

## 1. The derivation (NRT_P) ⇒ MS8 ⇒ claim: check

I re-read round13_q5 §§1–4 (Lemmas 1, 2, 3, Prop. 4, Lemma 5, §4). I checked each step against the cited inputs as stated in the brief. I did not re-derive (I1)–(I6) or (Rig).

- **Lemma 1, step 2.** Q_t = ξ̄(κ_∞, c_t) with κ_∞ ∈ F_W, so the components of Q_t with their special points are of two kinds:
  - components of the smooth constant coordinates c_t[w], w ∉ M_W;
  - components of coordinates of κ_∞.

  F_W is finite and independent of t, so the classes of the second kind lie in a finite set 𝔉_W. Correct.
- **Lemma 1, step 3.** An irreducible germ inside the curve germ 𝒢 lies in one branch of 𝒢. A constant branch of an irreducible Γ_{W,w} forces Γ_{W,w} = {Y_0} × Δ. Correct.
- **Lemma 2.** Correct. The hypothesis "Q has a boundary-type anchored sheet" holds at every puncture point, by B1♭(a″).
- **Lemma 3, Prop. 4, Lemma 5.** Correct as written, given (I4)–(I6). In Lemma 5, the irreducibility argument (every branch of Γ at (Y_0,0) is non-constant once one branch is) is right.
- **Endpoint.** Correct.

**Remark 1.1 (the derivation uses more than it needs).** The chain uses Prop. 4 in only two places:
- at the transitions J_m, for the pair (β̃_m, β̃′_m);
- at the endpoint, for the pair (β̃, b̃).

In both places the lifts lie in a common component S of q^{-1}(closure V_0) ∩ B (Lemma S̃′). Transfer (Lemma 5) and the endpoint need x ∈ P_Φ(T′) for **some** anchored sheet T′ of the leaving lift. So the chain needs only:

> **(MS11♭_Φ)** at the walk data (Q, β̃, b̃, x) with β̃, b̃ ⊂ S: if x ∈ P_Φ(T) for some anchored sheet T of β̃, then x ∈ P_Φ(T′) for some anchored sheet T′ of b̃.

(NRT_P) implies it (Prop. 4), but it is strictly stronger as a local statement: §4 gives a chart model in which (NRT_P) fails and (MS11♭_Φ) holds. This is not a flaw in the derivation. It shows that a counterexample to (NRT_P) need not obstruct the chain, and that (MS11♭_Φ) is the sharper target.

---

## 2. Proposition A: what an (NRT_P) failure is, in terms of one lifted family (proved)

Setting of (NRT_P). G := Aut(Q), Q a puncture point. T is a boundary-type anchored sheet at Q, of a lifted branch c̃ with pattern P. W is the component of the lifted family of the piece of c that contains Π(T) (by (I4)). For a label z, let w_z denote the vertex of G_c = G_P that contains z.

**Proposition A.** (NRT_P) fails at Q if and only if there are T and W as above, an element a ∈ G, and a label x with the following properties.
1. w_x = {x} is a constant vertex of W, i.e. x ∉ M_W. Its value curve Γ_{W,x} is non-constant, and F_x(0) ≅ Y_0.
2. y := a^{-1}x satisfies one of:
   - **(A)** w_y = {y} is a constant vertex of W with Γ_{W,y} = {Y_0} × Δ;
   - **(B)** w_y ∈ M_W, i.e. y lies in a moving vertex of W.

So (NRT_P) at Q says exactly this: no automorphism of Q carries a "rigid-type" Y_0-label of W (type (A) or (B)) to a "moving-type" constant Y_0-vertex of W.

*Proof.*

(⇒) Let (a, L, x) be a failure.
- **Reduction to L ⊂ T.** By (I2), T contains a lift-curve L_1. By (I1), L = gL_1 for some g ∈ G.
  - Put x′ := g^{-1}x and a′ := g^{-1}ag.
  - By (K3), F_{x′}(p) ≅ F_x(gp), and F_{a′^{-1}x′}(p) = F_{g^{-1}a^{-1}x}(p) ≅ F_{a^{-1}x}(gp), for p ∈ L_1.
  - So (a′, L_1, x′) is again a failure, and we may assume L ⊂ T.
- **The vertex of x.** The pattern of T at its generic points is P, and Π extends continuously to T with values in ∏ M̄_w.
  - At (p,t) ∈ L with t ≠ 0, the limit point is (κ_∞, c_t) with pr_{M_W}(κ_∞) ∈ F_W (round13_q5 Lemma 1, step 2).
  - If w_x ∈ M_W, then F_x(p) is a component of a coordinate of κ_∞. Its class then lies in the finite set 𝔉_W. It is continuous on the connected set L ∖ {(0,0)}, hence constant. This contradicts x ∈ C_Φ(L).
  - So w_x ∉ M_W. Its coordinate c_t[w_x] ∈ M_{w_x} is a smooth curve, so w_x consists of the single label x, and F_x(p) = c_t[w_x].
  - Hence the germ of values of x along L lies in Γ_{W,x}, and it is non-constant. F_x(0) ≅ Y_0 because φ(0) = Y_0.
- **The vertex of y = a^{-1}x.**
  - If w_y ∈ M_W, this is (B).
  - Otherwise, as above, w_y = {y} and F_y(L(t)) = c_t[y]. Then Γ_{W,y} contains the constant germ {Y_0} × (germ of Δ). An irreducible curve with a constant branch is that constant line (round13_q5 Lemma 5, last step), so Γ_{W,y} = {Y_0} × Δ. This is (A).

(⇐) Take a lift-curve L ⊂ T (I2).
- **x along L.** Along L, x has value c_t[x] on a branch of Γ_{W,x} through ([F_x(0)], 0) = (Y_0, 0). Γ_{W,x} is irreducible and not constant. So none of its branches is constant (same argument as above), and that branch lies in Φ. Hence x ∈ C_Φ(L).
- **y along L, case (A).** The value of y is c_t[y] ≡ Y_0.
- **y along L, case (B).** The value of y lies in 𝔉_W. It is continuous on L ∖ 0, hence constant. It equals F_y(0) ≅ F_x(a·0) = F_x(0) ≅ Y_0 by (K3).
- In both cases y is rigid along L, and (a, L, x) is an (NRT_P) configuration. ∎

**Remark.** Conditions 1 and 2 involve only the following:
- the t = 0 curve Q and its automorphisms;
- the (Rig) data (M_W, K_W) of one family;
- *which* constant Y_0-vertices of W have a moving value curve.

So (NRT_P) asserts that this last "moving / rigid" marking is Aut(Q)-invariant on the Y_0-components of Q. This is Lemma 2 of round13_q5, read inside one W.

---

## 3. Correction to the planner's sketch, item 2 (proved)

Item 2 of the sketch claims: in case (A) a failure needs the coarse piece family to have two distinct lifted components W ≠ σW **through the same t = 0 lifted piece**. This is true only under an extra condition, namely σÊ = Ê.

**Setting.** Take a failure of type (A) with L ⊂ T, as in Prop. A. Assume aP = P, so that a induces an automorphism σ of G_c = G_P with σ(w_y) = w_x. (If aP ≠ P there is no canonical σ at all; with the identification G_{aP} ≅ G_P induced by a, one gets Π(aT) ⊂ W itself, and no second family appears.)
- Let Ê be the component of ξ_{G_c}^{-1}(c) containing Π(c̃ ∖ 0). By Lemma U, Ê = K_W × {c_0}.
- Then Π(ac̃) ⊂ σÊ and Π(aT) ⊂ σW.

**Lemma 3.1.**
- (a) W ≠ σW.
- (b) If σÊ = Ê, then W and σW are two distinct components containing Ê × {0}. This is the "split" situation of item 2.
- (c) If σÊ ≠ Ê, nothing splits. W is the family of Ê, and σW is the family of the different lifted piece σÊ of the same coarse piece c.
- (d) σÊ = Ê holds if and only if σK_W = K_W (factors relabelled) and σc_0 = c_0. The existence of a ∈ Aut(Q) gives only that σ fixes the single point (κ_0, c_0), where κ_0 ∈ F_W is the cusp under Q. In particular κ_0 ∈ K_W ∩ σK_W, and two irreducible curves through κ_0 need not coincide.

*Proof.*
- (a) Γ_{σW,w_x} = Γ_{W,σ^{-1}w_x} = Γ_{W,w_y} = {Y_0} × Δ, while Γ_{W,w_x} is non-constant.
- (b), (c) W ⊃ Ê × {0} and σW ⊃ σÊ × {0}.
- (d) This is Lemma U together with the definition of σ. ∎

Case (c) actually occurs in the chart model of §4, where K_W = {(s, sζ)} and σK_W = {(s, −sζ)}. So item 2's reduction of case (A) to "split lifted families" is incomplete. In case (c), the failure is simply this: the piece c has two constant Y_0-vertices, one moving (Γ ∋ φ) and one rigid, and at one cusp κ_0 of the moving part the curve acquires an automorphism exchanging them. Nothing at t = 0, and nothing in the (Rig) data, distinguishes this from a harmless situation.

---

## 4. A chart-level model of an (NRT_P) failure at a puncture point (proved as a local statement)

Earlier models (round13_q3 §1, round13_q4 §1, round13_q6 §3) live at generic points of a piece, in the reflection case aS = S, and they force a detaching mirror (Lemma R / Lemma FC). The model here differs in three ways:
- it sits at the puncture point Q itself, and contains the lift-curves;
- aS ≠ S;
- no curve of V_t (t ≠ 0) near Q has the lost automorphism.

### 4.1 Data (hypotheses on the stable curve Q, chart level)

**The curve Q.** Aut(Q) = {1, a}, with a an involution, and Q has the following parts.
- Two components u, v ≅ Y_0, of type (g_i, n_i), d := dim M_{g_i,n_i} ≥ 1. For notational simplicity n_i = 1, so each is attached by one node, e_u and e_v respectively. a swaps u and v, and swaps e_u and e_v.
- The remaining part R′ of Q has two further nodes n and e. a maps each of them to itself, and acts trivially on their smoothing parameters.
- The components of R′ incident to n have a local moduli space with coordinate z ∈ C^k. On it a acts linearly by ι_* ≠ id, and ζ ≠ 0 is a vector with ι_*ζ = −ζ.
- All other moduli of Q are held fixed and are suppressed.
- E(G_Q) = {n, e, e_u, e_v}.

**Coordinates on Def(Q)** (a-equivariant):
- m_u, m_v ∈ C^d: moduli of u and v centred at Y_0, with a*(m_u, m_v) = (m_v, m_u);
- s_u, s_v: smoothing parameters of e_u, e_v, swapped by a;
- s_n, s_e: smoothing parameters of n, e, invariant under a;
- z, with a acting by ι_*.

Fix α ∈ C^d ∖ 0 such that t ↦ [Y_0 + tα] ∈ 𝔐 is non-constant.

**The 3-fold.** Let X ⊂ Def(Q) × Δ be the image of (s, w, t) under

  s_n = s, z = sζ, s_e = w, s_u = s_v = sw, m_u = tα, m_v = 0.

Its translate aX is given by z = −sζ, m_u = 0, m_v = tα, with all other formulas the same. Put S := X ∩ {t = 0}. Coarse objects are defined by
- closure(𝒱) := q(X);
- closure(V_t) := q(X_t);
- V_t := q(X_t ∖ {N = 0}), with N = s_n s_e s_u s_v = s w (sw)².

### 4.2 Checks

1. **X is a smooth embedded 3-fold, and t|_X is a submersion.** s = s_n, w = s_e and t (from m_u, since α ≠ 0) are recovered from the image point.

2. **X ∩ aX = c̃′ × {0}, where c̃′ := {s = 0} ⊂ S, and this curve is fixed pointwise by a.**
   - Suppose the point with parameters (s,w,t) on X equals the point with parameters (s′,w′,t′) on aX. Then:
     - s = s′ (compare s_n) and sζ = −s′ζ (compare z), so s = 0;
     - tα = 0 (compare m_u) and t′α = 0 (compare m_v), so t = t′ = 0.
   - The points (0, w, 0) have z = 0, s_u = s_v = 0 and m_u = m_v = 0, so a fixes them.
   - Hence Fix(a) ∩ X = c̃′ × {0}. **For t ≠ 0, no point of X_t is a-fixed.**

3. **q|_X is injective.** If p and ap both lie in X, then p ∈ X ∩ a^{-1}X = X ∩ aX, so ap = p.

4. **q|_X is an immersion, so coarse closure(𝒱) = q(X) is a smooth 3-dimensional germ, biholomorphic to X.**
   - Off c̃′ × {0}, points have trivial stabiliser, so q is a local biholomorphism there.
   - At (0, w, 0), use the a-invariant functions s_n, s_e and the d coordinates of m_u + m_v (and the quadratic invariants of the anti-invariant coordinates, whose differentials vanish there).
   - Their differentials send ∂_s, ∂_w, ∂_t to linearly independent vectors: ∂_s has s_n-component 1; ∂_w has s_e-component 1 and s_n-component 0; ∂_t has (m_u + m_v)-component α and zero s_n- and s_e-components.
   - So q|_X is an injective immersion, and the image of the germ is a complex submanifold.
   - In particular the coarse central fibre is reduced, since t is a coordinate on it. So Lemma Red holds.

5. **(R1), (R2), (i), (ii) in the chart.**
   - The strata of q(X) are read off (s, w) alone:
     - {w = 0, s ≠ 0}: pattern {e, e_u, e_v}; this is the piece c_t;
     - {s = 0, w ≠ 0}: pattern {n, e_u, e_v}; this is the piece c′_t;
     - {s = w = 0}: the point Q_t;
     - {sw ≠ 0}: the interior.
   - So H(q(s,w,0), t) := q(s,w,t) is a stratum-preserving biholomorphism with H_0 = id. Each stratum intersection is a trivial family, and (ii) holds trivially.
   - V_0 near Q is q(S) ≅ S, which is smooth.
   - Fix(a) ∩ S = c̃′ is a boundary curve, which is compatible with Lemma TG.

6. **(Rig) and Lemma U near Q.**
   - **Piece c.** Its moving vertex is the block of R′ containing n. Its moving part K_c = {(s_n, z) = (s, sζ)} does not depend on t. Its constant vertices are:
     - u, with value [Y_0 + tα] (non-constant);
     - v, with value Y_0 (rigid);
     - the rest, fixed.
   - **Piece c′.** Its moving vertex is the block containing e, with moving part K_{c′} = {s_e = w}, independent of t. Its constant vertices are u (value Y_0 + tα), v (value Y_0), and the R′-components on either side of n (fixed).
   - So (Rig) holds in the chart with 𝒦 = {(G_c, M_c, K_c), (G_{c′}, M_{c′}, K_{c′})}. The value curves are Γ_{W,u} = {([Y_0 + tα], t)} ∈ Φ and Γ_{W,v} = {Y_0} × Δ.

7. **Lift-curves, Q_t, isotropy drop.**
   - Q_t = H_t(Q) = q(0,0,t), and Λ = L ∪ aL with L := {(0,0,t)} ⊂ X. This is one Aut(Q)-orbit, as (I1) requires.
   - Q_t has m_u = tα ≠ 0 = m_v, so Aut(Q_t) = 1 for t ≠ 0.

8. **Anchored sheets.**
   - c̃ := {w = 0} ⊂ S. The transport family of c̃ is X ∩ {w = 0, s ≠ 0}; its aX-counterpart is disjoint from it for s ≠ 0, by item 2. So c̃ has the single anchored sheet T := X ∩ {w = 0}, and ac̃ ⊂ aS has aT.
   - c̃′ ⊂ S ∩ aS. Its transport family is (X ∪ aX) ∩ {s = 0, w ≠ 0}, which is connected because the two parts meet along t = 0. Its closure has the two components T′ := X ∩ {s = 0} and aT′, and both contain c̃′ × {0}.
   - L ⊂ T ∩ T′ and aL ⊂ aT ∩ aT′.

9. **The (NRT_P) configuration.** Let x be the label of u, so y := a^{-1}x is the label of v. Along L:
   - x is intact with class [Y_0 + tα], a branch in Φ;
   - y is intact with class ≡ Y_0.

   So C_Φ(L) ∋ x but not y = a^{-1}x, and **(NRT_P) fails at Q in the chart**. This is case (A) of Prop. A, in the non-split form (c) of Lemma 3.1, since σK_c = {(s, −sζ)} ≠ K_c.

10. **Theorem N / Lemma 1.1 hold at Q_t (t ≠ 0).**
    - The branches of B_t through the lift L(t) are the germs of {w = 0} and {s = 0} in X_t. aX_t does not pass through L(t), by item 2.
    - Along both branches, the φ(t)-copy x is intact with constant value: it is STAY. Nothing merges.
    - So the generic-time trichotomy imposes no obstruction. In particular Lemma 1.1's prohibition of IMOV at a puncture is respected.

11. **(MS11♭_Φ) holds in the model.** S contains the two lifted branches c̃ and c̃′ through 0, so a walk can pass from one to the other inside S.
    - x ∈ P_Φ(T) (Lemma 3, since L ⊂ T), and x ∈ P_Φ(T′) (since L ⊂ T′).
    - So Φ-persistence of x passes from c̃ to c̃′ and back. The chain is not obstructed, even though (NRT_P) fails.
    - The reason is that S × {0} lies in the single 3-fold component X, which contains exactly one lift-curve: this is round11_q4's (1L) condition.

### 4.3 What the model shows (and what it does not)

- It is a germ at (Q, 0). It does not check:
  - total geodesy of V_0;
  - closedness of V_0 in M_g;
  - whether the whole of closure(V_0) has such a Q.

  So it is **not** a counterexample. A globalisation to an admissible family with Y non-constant would be a counterexample to the problem itself.
- It shows that **no argument local at Q can prove (NRT_P)**, even one that uses all of the following together:
  - the lift-curves, (I1)–(I5) and (Rig) in the chart;
  - Theorem N at generic t;
  - smoothness of coarse 𝒱 and of V_0;
  - Lemma TG at t = 0.
- More specifically, the global objects proposed so far are **absent** in this mechanism:
  - The mirror family 𝒵 / 𝒟 of round13_q4 Prop. Z and round13_q6 Prop. G is absent: by item 2, no point of X_t (t ≠ 0) is a-fixed. Lemma R does not apply, because a moves S (aS ≠ S). So the "detaching mirror" route can at best cover the reflection sub-case, never all of (NRT_P).
  - The split lifted family of sketch item 2 is absent (Lemma 3.1(c)).

---

## 5. Consequences for strategy; proved / not proved / open

### 5.1 Strategic consequences
1. **Any proof of (NRT_P) must be global and must use t ≠ 0 data.**
   - Lemma NG (round13_q7) excludes t = 0-only arguments.
   - §4 excludes arguments local at Q, including every argument that works only with the germ of the family at (Q, 0) together with (Rig) and Theorem N.
   - §4 also excludes the symmetric-curve route as a general method. In the sheet-moving case (aS ≠ S), V_t need contain no curve with the lost automorphism.
2. **Prop. A identifies what must be shown.**
   - Let κ_0 ∈ F_W be a cusp of the moving part of some piece W at which the curve has an automorphism a.
   - Then a must not exchange a constant Y_0-vertex of W whose value curve moves with a Y_0-label of W whose value is rigid. The rigid label is either a rigid constant vertex (A) or a cusp component (B).
   - Equivalently: for a constant vertex, being a "moving" or a "rigid" Y_0-vertex must be determined by data that a preserves.
   - Nothing in the inputs listed in the task file, as far as I can see, ties the time evolution of a constant vertex to Aut(Q).
3. **The chain does not need (NRT_P).** It needs only (MS11♭_Φ) at the walk data (Remark 1.1). In the §4 model, (NRT_P) fails while (MS11♭_Φ) holds, because S × {0} lies in a single 3-fold component containing one lift-curve.
   - So the open target should be restated as (MS11♭_Φ) at walk data.
   - By round11_q4 Cor. 2.5 and round12_q6, a failure of (MS11♭_Φ) needs one of the following:
     - several lift-curves in a 3-fold component through S × {0}, (F-a)/(F-b);
     - an initial twist τ ∉ Stab(b̃)Stab(x).
   - The (NRT_P)-type configuration of §4 alone is not enough.
   - I have not proved that (MS11♭_Φ) is easier. I only show that it is strictly weaker as a chart-level statement.

### 5.2 Summary

**Proved:**
- §1: the derivation (NRT_P) ⇒ MS8 ⇒ claim was re-checked step by step, modulo (I1)–(I6) and (Rig). I found **no flaw**. Remark 1.1: only the weaker (MS11♭_Φ) at walk data is used.
- §2, Proposition A: exact characterisation of (NRT_P) failures at Q by the data of one lifted family W:
  - a ∈ Aut(Q) maps a rigid-type Y_0-label y (type (A): a constant vertex with Γ_{W,y} = {Y_0} × Δ; type (B): inside a moving vertex) to a constant vertex x with non-constant Γ_{W,x};
  - the converse also holds.
- §3, Lemma 3.1: the planner's item 2 is corrected. A split family W ≠ σW over one lifted piece is forced only when σÊ = Ê. When σÊ ≠ Ê the failure needs no splitting.
- §4: an explicit chart-level model at the puncture point. It satisfies:
  - smooth coarse 𝒱 and smooth V_0;
  - (R1), (R2), (i), (ii) and Lemma Red in the chart;
  - (Rig) with t-independent moving parts;
  - Theorem N at Q_t;
  - Lemma TG at t = 0.

  In it, (NRT_P) fails (case (A), non-split), no curve of V_t (t ≠ 0) has the lost automorphism, and (MS11♭_Φ) holds.

**Not proved:**
- (NRT_P) itself, in any of its cases (A) or (B), split or non-split.
- No global counterexample is given. The §4 model is a germ; total geodesy and global closedness of V_0 are not addressed.

**Open (named):**
- (NRT_P) (entry 141). By Prop. A it is equivalent to: Aut(Q) preserves the moving/rigid marking of the Y_0-labels of W at every cusp κ_0 of every piece family W.
- (MS11♭_Φ) at the walk data. This is the weaker statement the chain actually uses, and it is the recommended replacement target.
- Whether the §4 configuration can occur in the closure of a smooth totally geodesic V_0. Any such occurrence with Y non-constant would be a counterexample to the problem.
- (Rig) (entry 82), untouched.

**Verdict: not proved** (open). Partial results: Prop. A, Lemma 3.1, and the §4 model with its consequences.

=== END OF ANSWER round14_q2 ===


