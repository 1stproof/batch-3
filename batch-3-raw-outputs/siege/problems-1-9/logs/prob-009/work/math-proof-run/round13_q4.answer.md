# round13_q4 — attempt on (NRT)

**Plan/status line.** (NRT) is **not proved and not refuted** here. What this file does:
1. §1: an explicit chart-level model of the *rigid-twin* (β)-reflection configuration (frozen twin, not just the (β)-twist of round11_q7 §6), and a check that it satisfies every chart-level constraint named in the brief. It shows *precisely where the planner's item 3 (side-swap) mechanism fails*: the sides of c_t are not glued by a label-preserving path; the swap is carried at t ≠ 0 by a curve of **interior** curves with the lost automorphism.
2. §2: **Lemma R (proved)**: in the reflection case of the (β)-origin, whenever the 3-fold component X is smooth at a generic point of c̃ × {0} and contains its own reflection, V_t contains, for every small t ≠ 0, a curve F_t of smooth curves admitting (a K_S-modification of) the lost automorphism a, with F_t → c as t → 0. This is forced, not an artefact of the model.
3. §3: **Lemma M (proved)**: the label monodromy statement behind item 3: the label permutation of a small loop around c_t in V_t is trivial on {x, y} for t ≠ 0, while at t = 0 it is the swap; the discrepancy is exactly accounted for by F_t. So item 3, as stated, is flawed (it would also "prove" the impossibility of the model in §1).
4. §4: the global object 𝒵 (the family of a-symmetric curves) and what total geodesy says about its central fibre (**Lemma Z, proved under (T4)**): the components of V_0 ∩ Z_a are Teichmüller curves or points. Reduction of the reflection case of (NRT) to a precisely stated open question (NRT-Z).
5. §5: what is not touched: the (γ°) origin, the endpoint origin, the sheet-moving case of (R-a)/(R-b), and singular X.

Readings: (R1), (R2) with H_0 = id, coarse reading (H_t need not preserve automorphism groups); (Rig); Y non-constant; and, only in Lemma Z, (T4) of round10_q1 §1 (every component of the preimage of V_0 in T_g is a totally geodesic complex submanifold). The family is assumed smoothly trivial in the sense of the footnote, in particular φ: 𝒱 → Δ is a submersion, so the coarse central fibre is reduced (this is the run's Lemma Red, entry 80).

---

## 1. A chart-level model of the rigid-twin reflection (proved as a local statement)

This sharpens round11_q7 §6. In that model the twin σy has value −t, so it is not frozen. Here the twin is frozen at Y_0, as (NRT) requires.

**Data.** P is a generic point of the piece c with Aut(P) = ⟨a⟩, a² = 1. a swaps two constant vertices x, y of type (g_i, n_i) with F_x(P) ≅ F_y(P) ≅ Y_0, and swaps their edges. Def(P) has coordinates including:
- m_x, m_y: one coordinate each on a fixed holomorphic curve germ through Y_0 in M_{g_i,n_i}, transported to the x- and y-slots, with value 0 at Y_0 (the other moduli of x, y are set to 0);
- s_e (e an edge at x) and s_{a e}; to keep notation light, all edges of the pattern of c are smoothed by the same function below;
- v: a coordinate of the moving vertex along c̃.

a acts by (m_x, m_y, s_e, s_{ae}, v) ↦ (m_y, m_x, s_{ae}, s_e, v).

**The 3-fold.** Let X be the image of (v, u, t) under
- m_x = (u + t)/2, m_y = (t − u)/2, v = v;
- s_e = u² − t² for every edge e of the pattern of c.

**Checks.**
1. *Embedding and equivariance.* (v, u, t) is recovered from (v, m_x − m_y, m_x + m_y), so this is an embedding. The image of (v, −u, t) is a·(image of (v, u, t)), so a preserves X and acts on it by u ↦ −u.
2. *Coarse family.* X/⟨a⟩ has coordinates (v, U = u², t), so it is smooth and t is a submersion on it. Coarse V_t ≅ {(v, U)} is smooth, with boundary {U = t²} ≅ (v-line) lying in the stratum of c. H_t(v, U) := (v, U + t²) is a stratum-preserving homeomorphism, smooth on the interior, with H_0 = id. The coarse central fibre is reduced. So the local versions of (R1), (R2), (i), (ii) and Lemma Red hold.
3. *t = 0.* S = X_0 = {(v, u)}, with c̃ = {u = 0}. a acts on S as the reflection u ↦ −u fixing c̃ pointwise, and x, y are intact constant Y_0-copies along c̃: the (β)-origin of (NRT).
4. *Anchored sheets and labels.* The boundary {N = 0} ∩ X is T ∪ aT, with T = {u = t} and aT = {u = −t}; both contain c̃ × {0}.
   - On T: F_x has coordinate m_x = t, so F_x = φ(t) with φ non-constant, φ(0) = Y_0. F_y has coordinate m_y = 0, so F_y ≡ Y_0: the **rigid twin**.
   - On aT: the roles are exchanged.
   - Both labels are constant along the piece (independent of v), as Lemma U requires of constant vertices.
5. *The symmetric curve.* Fix(a) ∩ X = F := {u = 0}. On F, s_e = −t² ≠ 0 for t ≠ 0. So F_t = {u = 0, t} is a curve of **smooth** curves in V_t admitting the automorphism a, at plumbing distance |s_e| = |t|² from the boundary curve c_t. On F_t the two subsurfaces have equal moduli m_x = m_y = t/2: "halfway" between φ(t) and Y_0.

So the rigid-twin (β)-configuration at a generic point of c̃ is consistent with every chart-level constraint. The only feature of V_t that distinguishes it from V_0 near P is item 5.

### 1.1 Label monodromy in the model (Lemma M, proved)
Fix v and t ≠ 0, and let γ_r be the loop U = t² + r e^{iθ}, θ ∈ [0, 2π], in coarse V_t around c_t. Lift it to X_t by u = √(t² + r e^{iθ}).
- If r < |t|², the lift is a closed loop around u = t (resp. u = −t), so the label permutation is trivial.
- If r > |t|², the lift runs from u_0 to −u_0, so the label permutation is a, which swaps x and y.
- At t = 0 every small loop around c (U = r e^{iθ}) has label permutation a.

So small loops around c_t do **not** swap the twins at t ≠ 0. The swap of t = 0 survives only on loops that also encircle the symmetric curve F_t (U = 0), a locus of orbifold points of V_t.

**Consequence for the planner's item 3.** Item 3 argues that the two sides of c̃ are glued continuously by H_t, so φ(t) and Y_0 would be values of the same constant vertex along a connected family. The model refutes this inference at the chart level. The two sides of c_t are joined inside V_t only through the region swept by loops of radius > |t|² around c_t, which crosses F_t, where Aut jumps. Under the coarse reading, H_t is not required to respect this jump. Any proof along the lines of item 3 must therefore show that the symmetric curve F_t cannot exist **globally**. §2 shows that F_t is forced in general, not only in the model.

---

## 2. Lemma R: the reflection forces a curve of symmetric smooth curves in V_t (proved under (H2))

**Setting.** This is the (β)-origin of (NRT), reflection case. Q, G := Aut(Q), B, q, 𝒳 := q^{-1}(closure 𝒱) ∩ (B × Δ_ε), and D := 𝒳 ∩ {N = 0}, as in the brief. c̃ is a lifted branch through 0 of a branch c of B_0, and S is a chart sheet (a component of q^{-1}(closure V_0) ∩ B) containing c̃. K_S is the pointwise stabiliser of S, and a ∈ G.
- **(H1)** a fixes c̃ pointwise, aS = S, and a|_S ≠ id (the "reflection" case of round12_q2 (R2) / round12_q6 (R-a)).
- **(H2)** X is a component of 𝒳 containing S × {0}. For p in a dense open subset of c̃ ∖ {0}: X is smooth at (p, 0), X ∩ {t = 0} = S near (p, 0) (no other G_X-translate of S contains c̃), and S and c̃ are smooth at p.

**Lemma R.** Under (H1), (H2) there are a′ ∈ a·K_S with a′ ∈ G_X = Stab_G(X), and an analytic set F ⊂ X (the union of the components of Fix(a′) ∩ X containing c̃ × {0}), such that:
1. a′|_S = a|_S. In particular a′ fixes c̃ pointwise and acts non-trivially on S.
2. Near (p, 0), for p as in (H2), F is a smooth surface, F ∩ {t = 0} = c̃ × {0}, and t|_F is non-constant. So F_t := F ∩ {t} is a non-empty curve for every small t, and F_t → c̃ as t → 0.
3. Dichotomy:
   - (R-i) either F ⊄ D, and then for p as in (H2) (outside a further discrete set) and small t ≠ 0, the points of F_t near (p, t) are **smooth curves in V_t admitting the automorphism induced by a′**;
   - (R-ii) or F ⊂ D, and then F is a 2-dimensional germ of D containing c̃ × {0} and pointwise fixed by a′. On F the labels z and a′z have isomorphic components at every point and every t.

*Proof.*
- **Step 0 (getting into G_X).** aX is a component of 𝒳 containing aS × {0} = S × {0}. Let z ∈ S be generic: interior, X smooth at (z, 0), Stab_G(z) = K_S. Near (z, 0), q^{-1}(𝒳) is the preimage of the irreducible germ (𝒳, (q(z), 0)) under the quotient by K_S, so its components through (z, 0) form one K_S-orbit (standard; this is the argument of round12_q2 Lemma A4). Hence aX = k_1X for some k_1 ∈ K_S, and a″ := k_1^{-1}a ∈ G_X with a″|_S = a|_S.
- **Step 1 (the order of t along S).** Put H := G_X ∩ K_S. It fixes S pointwise, so it acts on the normal line of S in X by a character χ, constant along S. Let m′ := |χ(H)|.
  - Near (z, 0), the coarse germ of 𝒱 is X/H. This is the quotient of a component by its stabiliser in Stab(z) = K_S.
  - Let y be a local equation of S in the smooth germ X. Then X/H is smooth with coordinate Y = y^{m′} transverse to S (Chevalley; the non-trivial elements of χ(H) are pseudo-reflections along S).
  - t|_X vanishes exactly on S near (z, 0), so t = unit · y^M, and hence t = unit · Y^{M/m′} on X/H.
  - The coarse central fibre is reduced, because φ is a submersion. So M = m′.
  - At (p, 0), X is smooth and X_0 = S, so t = u_0 · y^M there as well, with u_0 a unit and the same M (compare at nearby generic z).
- **Step 2 (normalising a″).** a″ preserves S and t, and fixes (p, 0). So y∘a″ = λ′y with λ′ a unit, λ := λ′(p, 0), and u_0 = (u_0∘a″)·λ′^M. Evaluating at the fixed point gives λ^M = 1. Since χ(H) = μ_M, pick k_2 ∈ H with χ(k_2) = λ and put a′ := k_2^{-1}a″. Then a′ ∈ G_X, a′|_S = a|_S, and a′ acts trivially on T_{(p,0)}X / T_pS. Also a′ ∈ a·K_S, which proves item 1.
- **Step 3 (linearisation).** By Cartan's theorem, a′ is linear in suitable coordinates on the smooth germ (X, (p, 0)). Its eigenvalues are:
  - 1 on T_pc̃, since a′ fixes c̃ pointwise;
  - ζ ≠ 1 on T_pS / T_pc̃. If dа′ were the identity on T_pS, then a′|_S would be the identity by Cartan's theorem on the smooth germ (S, p), contradicting item 1;
  - 1 on TX / TS, by Step 2.

  a′ has finite order, so it is semisimple. Its fixed set near (p, 0) is the smooth surface F with tangent space the 2-dimensional eigenspace E_1, and E_1 ∩ T_pS = T_pc̃. So F ⊄ S × {0}, and F ∩ S = Fix(a′|_S) = c̃ near p: a smooth curve contained in the fixed set, which is 1-dimensional because ζ ≠ 1. Hence F ∩ {t = 0} = c̃ × {0}. Since F ⊄ {t = 0}, t|_F is non-constant and vanishes on c̃ × {0}, so it takes every small value on F near (p, 0). This proves item 2.
- **Step 4 (dichotomy).** F ∩ D is analytic in F and contains c̃ × {0}.
  - If F ⊄ D, then c̃ × {0} is a component of the curve F ∩ D. Other components meet it in a discrete set of the punctured germ. For p off that set, F ∩ D = c̃ × {0} near (p, 0). So the points of F_t near (p, t), t ≠ 0, lie off {N = 0}, i.e. over V_t, and are fixed by a′. A point of the Kuranishi family fixed by g ∈ G is a curve admitting the automorphism induced by g (standard property of the Kuranishi family; (K1) in the run's notation). This is (R-i).
  - If F ⊂ D, then F is a 2-dimensional germ of D containing c̃ × {0} and pointwise fixed by a′. The label statement follows from equivariance (K3): F_{a′z}(a′w) ≅ F_z(w), and a′w = w on F. This is (R-ii). ∎

**Remarks.**
- In (NRT) with the (β)-origin, (R-ii) can only occur on an anchored sheet different from T and aT. On T itself the twins x, y = a^{-1}x have different values φ(t) ≠ Y_0 for small t ≠ 0, so T is not pointwise fixed by any element mapping y to x. Whether (R-ii) happens on some third anchored sheet is not decided here; in the §1 model it does not.
- The label action of a′ is k_2^{-1}k_1^{-1}a. It swaps x and y whenever K_S preserves x and y, for instance when K_S = 1, which is the typical situation of a "lost" automorphism.
- Lemma R needs no total geodesy. It is the general form of item 5 of §1.

---

## 3. The global object 𝒵 and what total geodesy says about its central fibre

### 3.1 Lemma Z (proved under (T4))
Let g ∈ Mod_g have finite order. Let Z_g ⊂ M_g be the locus of curves admitting an automorphism whose class in Mod_g is conjugate to g, and Z̄_g its closure in M̄_g. Z_g is a closed analytic (indeed algebraic) subset of M_g; its preimage in T_g is ⋃_h Fix(h), the union over the conjugates h of g (standard, cited from memory). Assume (T4). Then every 1-dimensional irreducible component of V_0 ∩ Z_g is the image of a Teichmüller disc, i.e. a Teichmüller curve, and V_0 ∩ Z_g has no 2-dimensional component unless V_0 ⊂ Z_g.

*Proof.*
- Fix(h) ⊂ T_g is a closed complex submanifold, namely the Teichmüller space of the quotient orbifold (cited, standard).
- It contains every Teichmüller disc tangent to it. Let X ∈ Fix(h) and v ∈ T_X Fix(h), v ≠ 0. The Teichmüller disc D_v through X tangent to v is unique: it is generated by the norming quadratic differential of v, which is unique (cited in PR-H §1.1, (Dual)). h is an isometry fixing X with dh(v) = v, so h(D_v) = D_v. Since h acts on D_v as a holomorphic self-map fixing X with derivative 1, and h has finite order, h|_{D_v} = id (Cartan). So D_v ⊂ Fix(h).
- Let C̃ be a 1-dimensional component of Ṽ ∩ Fix(h), where Ṽ is a component of the preimage of V_0, and let X be a smooth point of C̃ with tangent v. Then D_v ⊂ Fix(h). Also D_v ⊂ Ṽ by (T4), since D_v is the union of the real Teichmüller geodesics through X in the directions e^{iθ}v, all tangent to Ṽ.
- So D_v ⊂ Ṽ ∩ Fix(h). D_v is irreducible, 1-dimensional, closed, and contains the germ of C̃ at X. Hence C̃ = D_v. The image of C̃ in M_g is a closed algebraic curve (V_0 ∩ Z_g is algebraic), so it is a Teichmüller curve.
- If V_0 ∩ Z_g had a 2-dimensional component, it would be open in the irreducible V_0, hence V_0 ⊂ Z_g by the identity theorem. ∎

### 3.2 The family of symmetric curves
Assume (R-i) of Lemma R. Let g be the class of the automorphism induced by a′ on the smooth curves of F_t. Let 𝒵 be an irreducible component of the analytic set closure(𝒱) ∩ (Z̄_g × Δ) containing the germ q(F) at a point (q(p), 0), with p as in (H2).

**Proposition Z (proved, given Lemma R and Lemma Z).**
1. dim 𝒵 ≥ 2. If dim 𝒵 = 3, then 𝒵 = closure(𝒱) and V_0 ⊂ Z̄_g. Then every curve of V_0 has an automorphism of type g. Near a generic point z of S, that automorphism comes from Stab(z) = K_S, so some element of K_S is conjugate in Mod_g to the class of a′. Call this the **degenerate case**.
2. Otherwise dim 𝒵 = 2, 𝒵 is not contained in {t = 0}, and its central fibre 𝒵_0 is a pure 1-dimensional compact analytic subset of closure(V_0) ∩ Z̄_g. It contains the whole closure c̄ of the piece c.
3. For t ≠ 0 small, 𝒵_t ⊄ B_t. Near c_t, 𝒵_t contains q(F_t), a curve of smooth curves with an automorphism of type g, approaching c_t as t → 0.
4. Under (T4), every component of 𝒵_0 is either a boundary curve of closure(V_0) contained in Z̄_g (c̄ is one of them), or the closure of a Teichmüller curve contained in V_0 ∩ Z_g.

*Proof.*
- (1) closure(𝒱) is irreducible, because 𝒱 ≅ V_0 × Δ with V_0 connected and smooth. So a 3-dimensional component is all of it. The rest is the definition of Stab(z).
- (2) A 2-dimensional irreducible 𝒵 meeting {t = 0} in the curve c (locally), and not contained in it, has central fibre of pure dimension 1 (Krull). It is closed in the compact set closure(V_0) ∩ Z̄_g. It contains a non-empty open subset of the irreducible curve c̄, hence all of c̄.
- (3) This is Lemma R (R-i).
- (4) This is Lemma Z applied to V_0 ∩ Z_g: components of 𝒵_0 inside the boundary are boundary curves; the others are 1-dimensional components of V_0 ∩ Z_g, i.e. Teichmüller curves. ∎

**Remark (why this is the right global object).** In the §1 model, 𝒵 = q({u = 0}). The planner's item 3 implicitly assumes that 𝒵 does not exist. Lemma R shows that in the reflection case (with (H2)) 𝒵 always exists. So the reflection case of (NRT) is exactly the question of whether such a 𝒵 is compatible with total geodesy and smoothness of V_0, with (Rig) and with Y non-constant.

---

## 4. The residual open question (reflection case)

**(NRT-Z), open.** In the setting of (NRT), (β)-origin, reflection case with (H2), and outside the degenerate case: show that there is no irreducible 2-dimensional analytic 𝒵 ⊂ closure(𝒱) with the following properties:
- 𝒵_t ⊂ Z̄_g for all t;
- 𝒵_0 ⊃ c̄;
- near generic points of c, 𝒵_t (t ≠ 0) consists of smooth curves at plumbing distance → 0 from c_t, on which the two subsurfaces carried by x and y are exchanged by the automorphism;
- along the lift-curve L at the puncture Q, the boundary components x, y of Q_t have the distinct values φ(t), Y_0.

What I could not do:
- A degree argument (δ·𝒵_t = δ·𝒵_0, λ·𝒵_t = λ·𝒵_0) gives no contradiction. 𝒵_0 contains boundary curves, whose δ-degree has no sign.
- Following 𝒵_t to Q_t: Q_t lacks the automorphism, so 𝒵_t passes near Q_t without meeting it. I found no constraint on how it does so. The §1 model, extended to the puncture by adding a factor in which c̃ ends, gives no contradiction at chart level.
- Total geodesy enters only through Lemma Z, i.e. through the structure of 𝒵_0. That alone does not exclude 𝒵, since 𝒵_0 may consist of boundary curves only.

---

## 5. Not treated
- **Singular X**, i.e. (H2) failing: X singular along c̃ × {0}, X_0 ⊋ S near c̃, or S singular along c̃. Lemma R needs the linearisation on a smooth germ.
- **Sheet-moving twists:** aS ≠ S (round12_q2 (R1); round12_q6 (R-a), second bullet; (R-b) with τS ≠ S).
- **The (γ°) origin** (round12_q8) and **the endpoint origin** (round12_q7 Lemma 4.1). Here the frozen twin lives along a lift-curve without a (β)-twist at a generic point of a branch, and Lemma R has no input.
- The unchecked Φ-substitution of round12_q7 §3, and (Rig) (entry 82).

## Summary: proved / not proved / open

**Proved** (modulo cited standard facts: Cartan linearisation, Chevalley, Krull, uniqueness of Teichmüller discs, the Kuranishi family properties (K1), (K3); and round12_q2 Lemma A4's orbit argument):
- §1: an explicit chart-level model of the rigid-twin (β)-reflection configuration, consistent with all chart-level constraints. With it, Lemma M: at t ≠ 0, small loops around c_t have trivial label monodromy, while at t = 0 they swap the twins. Consequence: **the planner's item 3 (side-swap) argument is flawed as stated.** The sides of c_t are joined only across a curve F_t of orbifold points of V_t.
- §2, Lemma R: in the reflection case, under (H2), V_t contains for every small t ≠ 0 either a curve F_t of smooth curves admitting the lost automorphism (modified by K_S), converging to c (R-i), or an anchored sheet pointwise fixed by it (R-ii).
- §3, Lemma Z (under (T4)): the components of V_0 ∩ Z_g are Teichmüller curves. Proposition Z: the global 2-dimensional family 𝒵 of symmetric curves and the structure of its central fibre.

**Not proved:** (NRT) in any of its three origins. No counterexample is given.

**Open:** (NRT-Z) of §4; the cases listed in §5; and (R-ii) on a third anchored sheet.

**Verdict: not proved** (partial: a reduction of the reflection case of the (β)-origin to (NRT-Z), and a refutation of item 3's mechanism at chart level).

=== END OF ANSWER round13_q4 ===

