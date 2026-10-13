# round9_q1 — attempt on MS8

**Status: MS8 is NOT proved in full. This is a PARTIAL result. It contains no counterexample.**

What is new here, and proved (given the cited prior results, whose steps I re-checked as I used them):
- **Theorem 1 (copy-free dichotomy).** If t ↦ Y_t is non-constant, then one of two things happens:
  - (I) a crossing (IMOV) event lies on the persistent network at every generic time near 0;
  - (II) a "sealed" configuration exists, made of conditions that can be checked at t = 0 only: (II-a) and (Seal_Q).
- **Corollary 2 (release criterion).** MS8 holds, unless case (I) occurs, whenever some point of the connected component of B_0 through ∂V_0 has no component isomorphic to Y_0.
- **Corollary 3 (seal criterion).** MS8 holds, unless case (I) occurs, whenever (Seal_Q) fails at some point Q of that component. R8-3 Corollary T and R8-4 Theorem 2V are special cases of Corollary 3.
- So the twin obstruction becomes a statement about V_0 alone: "(Seal) holds everywhere on B_0^∂". That statement does not refer to the deformation.

Still open:
- the crossing case (I);
- the sealed case (II), i.e. excluding (Seal_Q) at every point of B_0^∂.

§5 records a dead end. The natural strengthening of Proposition K ("total release") is false in the quintic test case.

---

## 0. Setting, notation, and the prior results used

The setting is MS8 exactly as in the task, in readings (R1) and (R2):
- H is the stratified homeomorphism, with H_0 = id.
- V_0 is smooth, closed, 2-dimensional and totally geodesic.
- Δ_Γ is of product type, ∂V_t has dimension 1, and π_i(∂V_t) = {Y_t}.
- (Rig) holds.

Notation:
- B_t := closure(V_t) \ V_t. By (R2), H_t : B_0 → B_t is a homeomorphism preserving strata.
- B_0^∂ is the connected component of B_0 that contains ∂V_0. Put B_t^∂ := H_t(B_0^∂); this is the connected component of B_t containing ∂V_t.
- N_t := {Q ∈ B_t : Q has a Y_t-copy}.
- For Q ∈ B_0, the chart is Def(Q), with Aut(Q) acting and quotient map π.
  - Labels are the vertices of G_Q.
  - F_z is the z-component on L_z = {s_e = 0 for all e at z}.
  - A lifted branch c̃ has a constant pattern S_c̃.
  - A label z is *intact* along c̃ if every edge at z lies in S_c̃.

Prior results used. I re-checked each step that I use.
- **(TN) = R8-3 Theorem N, and R8-3 Lemma 2.**
  - Lemma 2 says each coarse piece D satisfies exactly one of (N) and (F):
    - (N): for every t, every point of H_t(closure D) has a Y_t-copy;
    - (F): for t outside a countable set Z_D, only finitely many points of H_t(closure D) have a Y_t-copy.
  - Put 𝒩 := {D : (N) holds} and C_t := ⋃_{D∈𝒩} H_t(closure D) = H_t(C_0). Then closure(∂V_t) ⊂ C_t.
  - Assume Y is non-constant. Then there is a countable set Z ⊂ Δ such that, for t ∉ Z ("generic"), the following holds. Let Q ∈ B_t, let q be a lift of Q, let y be a label with F_y(q) ≅ Y_t, and let c̃ be any lifted branch of B_t through q. Then y is intact along c̃, and exactly one of the following holds:
    - **STAY**: F_y ≡ Y_t along c̃, and the coarse piece of c̃ lies in 𝒩;
    - **IMOV**: Q lies in the stratum of the piece of c̃, and F_y is non-constant along c̃.
  - *Re-check.*
    - A merge, or a non-constant intact y at a puncture, would make [Y_t] a component class of a puncture value of a non-constant vertex. By (Rig) that class lies in a fixed finite set F′, which is excluded for generic t.
    - If y is intact and constant along c̃, infinitely many points of the piece D′ have a Y_t-copy. For t ∉ Z_{D′}, Lemma 2 then forces D′ ∈ 𝒩.
- **(Fam) = R7-4 Lemma 2 / R7-3 Lemma 2 (transport families).** Let b be a branch of B_0 at Q with lift b̃.
  - Let Ñ be the component of π^{-1}(H((b∖Q) × Δ_ε)) containing b̃ ∖ 0.
  - Every lifted branch of H_t(b) through a lift q of Q_t (t small) lies in (aÑ)_t for some a ∈ Aut(Q).
  - The pattern, and the partition of labels into vertices, are constant on aÑ, and the t = 0 slice of aÑ is a b̃ ∖ 0.
- **(LU) = Lemma U of R8-2 and its corollary U1.** A vertex is constant on one component of one fibre of a 2-dimensional family W iff it is constant on all of them.
  - The time-t and time-0 pieces of a family aÑ lie in one such W. Π_S(Ñ) is a connected topological 4-manifold, so its regular part lies in a single irreducible component, as in R8-3 Lemma 2, step 3.
  - Hence a label {z} is constant along (aÑ)_t iff it is constant along a b̃.
- **(Sh) = R8-1 Lemma S.** Sheets (irreducible components of the germ of closure(V_t) at a point) are transported by H_t, compatibly with the boundary branches they contain.
- **Krull (cited, standard).** Let X be an irreducible 2-dimensional germ and h a holomorphic function with h ≢ 0 on X and h(x) = 0. Then X ∩ {h = 0} has pure dimension 1 at x.
- **Closedness = R7-1 Lemma 2** (equivalently, the analytic set 𝓝 of R8-3 Lemma 1). If t_n → t, Q_n ∈ B_{t_n} has a Y_{t_n}-copy and Q_n → Q, then Q has a Y_t-copy.

---

## 1. Lemma 1 (sheet Krull at one lift) — proved

**Lemma 1.** Fix t. Let Q ∈ B_0, let q ∈ Def(Q) be a lift of Q_t := H_t(Q) (t small enough that Q_t lies in the chart), and let Σ_t be a sheet of closure(V_t) at Q_t. Then:
- (a) the preimage of the germ Σ_t at q is a non-empty union of irreducible 2-dimensional germs X^1, …, X^r, and **each X^k maps onto Σ_t**;
- (b) for every boundary branch b of Σ_t at Q_t, each X^k contains a lifted branch of b through q;
- (c) for every edge f ∈ E(G_Q), each X^k contains a lifted branch through q whose pattern contains f;
- (d) every 1-dimensional germ of X^k ∩ {∏ s_e = 0} at q is a lifted branch through q of a boundary branch of Σ_t.

*Proof.*
1. **(a).** Near q, π is the quotient by Stab(q), a finite map, and π(q) = Q_t ∈ Σ_t. So the preimage germ is non-empty and of pure dimension 2.
   - The image of an irreducible component X^k is an irreducible analytic germ of dimension 2 (Remmert), contained in the irreducible 2-dimensional germ Σ_t. So it equals Σ_t.
2. **(b).** b ⊂ Σ_t = π(X^k). So π^{-1}(b) ∩ X^k is a 1-dimensional germ at q that maps onto b. Its components are lifted branches of b through q.
3. **(d).** Near q, π^{-1}(B_t) is the union of the lifted branches through q of the branches of B_t at Q_t. A 1-dimensional germ of X^k inside it is one of these lifted branches, and its image lies in Σ_t ∩ B_t. So it lifts a boundary branch of Σ_t.
4. **(c).** By (a), X^k maps onto Σ_t, whose generic points lie in V_t ⊂ M_g. So s_f ≢ 0 on X^k, while s_f(q) = 0 because q lies over the stratum of Q.
   - By Krull, X^k ∩ {s_f = 0} is pure 1-dimensional at q, and it lies in {∏ s_e = 0}.
   - By (d) it consists of lifted branches through q, and s_f ≡ 0 on each of them. ∎

---

## 2. Theorem 1 (copy-free dichotomy) — proved

Assume Y is non-constant, and let Z be the countable set of (TN). Let I be the set of t ∈ Δ ∖ Z at which some point Q ∈ C_t, some lift q, some Y_t-copy y at q and some lifted branch through q are in the IMOV case.

**Theorem 1.** One of the following holds.
- **(I) Crossings near 0.** There is r > 0 such that every t ∈ Δ_r ∖ (Z ∪ {0}) lies in I. In particular, IMOV events on the persistent network C_t occur at uncountably many times accumulating at 0. R8-6 Propositions 1 and 2 then apply: these events are pure crossings (P), shared crossings (S) or same-branch twins (T), with the persistence conclusions (Pers 1)–(Pers 3) stated there.
- **(II) Sealed configuration.** All of the following hold.
  - **(II-a)** Every point of B_0^∂ has a Y_0-copy, and every coarse piece contained in B_0^∂ belongs to 𝒩. So it carries a constant vertex whose value function is ≡ Y.
  - **(II-b) (Seal_Q) holds at every Q ∈ B_0^∂.** (Seal_Q) means that there are a non-empty set Π of labels of G_Q and, for every sheet Σ of closure(V_0) at Q, a set 𝒫_Σ of lifted branches at 0 ∈ Def(Q), with the following properties:
    1. 𝒫_Σ contains at least one lift of every boundary branch of Σ at Q, and every member of 𝒫_Σ lifts a boundary branch of Σ;
    2. ⋃_{c̃∈𝒫_Σ} S_c̃ = E(G_Q) (every edge is pinched along some member);
    3. every z ∈ Π satisfies F_z(0) ≅ Y_0. Moreover, along every member c̃ of 𝒫 := ⋃_Σ 𝒫_Σ, the label z is intact and {z} is a constant vertex of the piece of c̃;
    4. if Q ∈ closure(∂V_0), then for every member c̃ ∈ 𝒫 that lifts a branch of ∂V_0, the label carrying vertex i along c̃ belongs to Π.

*Proof.*
**Step 0 (the dichotomy).** If (I) fails, there are t_n ∈ Δ ∖ (Z ∪ I ∪ {0}) with t_n → 0. Fix such t = t_n.
- *Claim:* C_t ⊇ B_t^∂, and at every lift q of every point of B_t^∂, every Y_t-copy is in the STAY case along every lifted branch through q.
- This is R8-3 Corollary N1. I re-check it:
  - at Q ∈ C_t, every branch is STAY by (TN), because t ∉ I, so it lies in C_t;
  - hence C_t is open in B_t; it is also closed, being a finite union of compact sets;
  - it contains ∂V_t, so it contains the connected component B_t^∂;
  - the second part is (TN) again.

**Step 1 (II-a).**
- C_t = H_t(C_0) ⊇ H_t(B_0^∂), so C_0 ⊇ B_0^∂.
- A coarse piece D ⊂ B_0^∂ is irreducible and lies in the finite union of the closures of 𝒩-pieces. So D ⊂ closure(D′) for one D′ ∈ 𝒩. This forces D = D′: the closure of a piece of a different stratum meets the stratum of D in a finite set.
- Every point of C_{t_n} has a Y_{t_n}-copy. Let Q ∈ B_0^∂. Then H_{t_n}(Q) → Q has Y_{t_n}-copies, and Closedness gives a Y_0-copy at Q.

**Step 2 (II-b).** Fix Q ∈ B_0^∂. For n large, Q_n := H_{t_n}(Q) lies in the chart Def(Q). Pick a lift q_n of Q_n.
- Let Π_n be the set of labels z with F_z(q_n) ≅ Y_{t_n}. It is non-empty, since Q_n ∈ B_{t_n}^∂ ⊂ C_{t_n}.
- For each sheet Σ of closure(V_0) at Q, let Σ_n be its transport at Q_n (by (Sh)). Choose an irreducible component X_n of the preimage of Σ_n at q_n (Lemma 1(a)).
- By Lemma 1(b), (c), (d), the lifted branches of B_{t_n} through q_n that lie in X_n include at least one lift of every boundary branch of Σ_n. Their patterns cover E(G_Q).
- By (Fam), each such lifted branch lies in a family aÑ_b, where b is the corresponding branch of Σ at Q (sheets and branches are transported together by (Sh) and PR-B). Record the t = 0 slices a b̃. The patterns are the same.
- There are finitely many labels, families and sheets. So, after passing to a subsequence, Π_n = Π and the sets of recorded families are independent of n. Let 𝒫_Σ be the set of their t = 0 slices.

Now check the four conditions.
- **Condition 1** holds by Lemma 1(b), (d).
- **Condition 2** holds by Lemma 1(c).
- **Condition 3.**
  - For z ∈ Π, F_z(q_n) ≅ Y_{t_n} → Y_0. Since q_n → 0 and F_z is continuous on the closed set L_z (all lifts lie over the stratum of Q), F_z(0) ≅ Y_0.
  - By Step 0 every z ∈ Π is STAY along every recorded lifted branch through q_n. So z is intact there, and {z} is constant on the time-t_n piece.
  - The pattern is constant on the family (Fam), and constancy transfers to t = 0 by (LU). So z is intact along the t = 0 slice, and {z} is constant on its piece.
- **Condition 4.**
  - Suppose c̃ ∈ 𝒫 is the slice of a family aÑ_b with b a branch of ∂V_0. Then the time-t_n lifted branch through q_n lifts a branch of ∂V_{t_n}.
  - Along it, vertex i is a single label j with F_j ≡ Y_{t_n} (PR-I Lemma D(1)). By continuity at q_n, F_j(q_n) ≅ Y_{t_n}, so j ∈ Π.
  - The label carrying vertex i is constant along the family, so it is j at t = 0 as well. ∎

**Remarks.**
1. No automorphism, marking or track enters Theorem 1. Twins are handled automatically: Π is the set of all Y_t-copies at one lift, and Krull is applied at that same lift (this is the idea of R8-3 Corollary T, carried out in every sheet).
2. Theorem 1 does not use total geodesy. Total geodesy is needed only to rule out (I) and (II) for the given V_0.

---

## 3. Corollaries — proved

**Corollary 2 (release criterion; t = 0 only).** Suppose some point of B_0^∂ has no component isomorphic to Y_0 (with its special points, in some order). Then either Y_t = Y_0 for all t, or (I) holds.

*Proof.* (II-a) fails, so if Y is non-constant, Theorem 1 gives (I). ∎

Equivalently, the hypothesis says that some coarse piece of B_0^∂ has no constant vertex of class [Y_0], or that some isolated stratum point of B_0^∂ has no Y_0-copy. It is a condition on V_0 alone. Under it, **twins play no role at all**: the only remaining obstruction is a crossing.

**Corollary 3 (seal criterion; t = 0 only).** Suppose that for some Q ∈ B_0^∂ no data (Π, (𝒫_Σ)_Σ) satisfy (Seal_Q). Then either Y_t = Y_0 for all t, or (I) holds. ∎

**Corollary 3 recovers the earlier twin criteria.**
- **R8-3 Corollary T.** Hypotheses: (Tw1) all branches at J ∈ closure(∂V_0) ∖ ∂V_0 lie in ∂V_0; (Mg) for S ≠ S′ in 𝒞, some edge at j(S) is not in S′.
  - Suppose (Seal_J) held. Every member of 𝒫 has pattern in 𝒞 (Lemma D(1)), and each pattern is ≠ E(G′).
  - By Condition 2 for a sheet Σ, 𝒫_Σ contains two members with patterns S ≠ S′.
  - By Condition 4, j(S) ∈ Π. By Condition 3, j(S) is intact for S′. This contradicts (Mg).
  - In particular, Corollary 3 covers the quintic test case of PR-I.
- **R8-4 Theorem 2V.** Hypotheses (Tw1), (C1), (C2).
  - Suppose (Seal_{P_0}) held, and take S ∈ 𝒫 (pattern). Then j(S) ∈ Π.
  - By Condition 3, any z ∈ Π is intact and constant along the member with pattern S. By (C1), the only constant vertex there is i. So Π = {j(S)}.
  - By (C2) choose e ∉ S lying in no S′ ∈ 𝒞_{j(S)}. By Condition 2, e ∈ S″ for a member with pattern S″ ∈ 𝒞, and j(S″) ∈ Π = {j(S)}. So S″ ∈ 𝒞_{j(S)} and contains e, a contradiction.

So Theorem 1 contains both earlier twin criteria, with neither (Tw1) nor (C1)/(C2) imposed globally. They become one point-wise t = 0 test.

---

## 4. What remains (precise)

MS8 follows from the following two statements, both open.
- **(X) No persistent crossing.** Case (I) is impossible. By R8-6 Proposition 2, this reduces to excluding the t = 0 configurations (Pers 1)–(Pers 3) and the persistent same-branch twin coincidence of R8-6 §3.3. Theorem X of R8-1 excludes those that lie inside one Q-factorial sheet. Open: two-sheet crossings, and crossings in non-Q-factorial sheets.
- **(MS9) Unsealability.** For every smooth closed totally geodesic V_0 satisfying the problem's hypotheses, at least one of the following holds:
  - some point of B_0^∂ has no Y_0-copy;
  - some coarse piece of B_0^∂ has no constant vertex of class [Y_0];
  - (Seal_Q) fails at some Q ∈ B_0^∂.

  Note that (II-a) also requires the constant vertices to be persistent (value function ≡ Y). That requirement cannot be tested at t = 0, so MS9 is a sufficient condition and is stronger than needed.

**How Proposition K relates to (MS9) (analysis; not a proof).**
- In case (II), the chain of Proposition K lies in B_0^∂, because K_0 ⊂ B_0 is connected and contains P.
- At its MERGE or pMOV endpoint Q_0, let Σ be the ray's sheet. Condition 1 provides a member σβ̃^E ∈ 𝒫_Σ along which all of Π stays. Since x merges or moves along β̃^E, σ^{-1}Π ∌ x.
- So the copy that Proposition K tracks is never in the pulled-back persistent set at the endpoint: a "frozen twin". This is consistent with R8-4 Corollary G1 and R8-8 Proposition 3, but it is not a contradiction.
- A contradiction would follow if the ray's lifted sheet at t = 0 contained only members of a single 𝒫_Σ ("unsplit sheet"). This is (SC) of R8-8 in sheet form. It fails exactly in the "star splitting" picture of R8-8 §6.

---

## 5. Dead end: "total release" (Proposition K for all copies at once) is false

Natural idea: stop Proposition K's rays at the first time at which **no** subsurface is Y_0-like, instead of following one marked copy.
- If that stopping time T_n were finite, the endpoint Q_0 would have a branch along which no point has a Y_0-copy. Corollary 2's mechanism, or its proof at Q_0, would then finish without twins.
- **This conclusion is false in general.** In the quintic test case (PR-I; totally geodesic but not smooth), closure(V_0) ∖ V_0 = ∂V_0 ⊔ {P_0}. Every point of ∂V_0 has the Y_0-copy at vertex i, and P_0 has the twins A ≅ C ≅ Y_0. So B_0^∂ ⊂ N_0: no point of B_0 releases every copy.
  - There MS8 holds through Condition 2 of (Seal) (Krull at one lift), not through total release.
- **Where the proof attempt breaks.** For a fixed ray, the all-copies stopping time can be infinite. A lower-level component (Y, η) whose own differential is Strebel (all horizontal leaves closed and peripheral) is fixed, up to scale, by g_s. Also, new Y_0-like subsurfaces can be split off at junctions while older ones are released.

So no t = 0 argument based only on "some point releases every copy" can work. Case (II) needs Krull at one lift (Condition 2), combined with total geodesy, and that combination is MS9.

---

## 6. Summary

**Proved:**
- Lemma 1: at one lift q, every lifted sheet germ covers its coarse sheet, contains lifts of all of that sheet's boundary branches, and its boundary patterns cover all edges.
- Theorem 1: if Y is non-constant, then (I) crossings occur near 0, or (II) holds, i.e. (II-a) together with (Seal_Q) at every point of B_0^∂.
- Corollary 2 (release criterion) and Corollary 3 (seal criterion), both checkable at t = 0.
- R8-3 Corollary T and R8-4 Theorem 2V are special cases of Corollary 3.
- "Total release" is false in general (quintic test case).

**Not proved / open:**
- (X): exclusion of persistent crossings (pure, shared, same-branch twin) for smooth totally geodesic V_0.
- (MS9): unsealability of B_0^∂ for smooth totally geodesic V_0.
- MS8 itself, in full generality.
- The inherited inputs are not re-proved: (Rig) (entry 82), Proposition K with its "routine marking details" (used only in §4's analysis, not in Theorem 1), and Lemma PA / Theorem TV.

**Chain check.** I found no flaw in the derivation of the problem's claim from MS8 together with entry 82 (chain steps 1–4). Theorem 1 and Corollaries 2–3 use only (R1), (R2), (Rig) and the cited prior lemmas.

=== END OF ANSWER round9_q1 ===
