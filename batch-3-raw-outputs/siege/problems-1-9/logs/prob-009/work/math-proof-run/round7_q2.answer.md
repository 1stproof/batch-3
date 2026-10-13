Status / plan: PARTIAL. MS6 is not proved in full, and no counterexample is given. This file contains:
(1) a time-t criterion for MS6 (Lemma 1), which is proved;
(2) a transport lemma for branch patterns (Lemma 2), which is proved;
(3) a "total-merge" transport theorem (Theorem 3): MS6 follows from a condition on V_0 alone at one boundary point. Proved;
(4) a "spreading" lemma at time t (Lemma 4): if MS6 fails at t, copies of Y_t spread through the boundary component of ∂V_t, except across "MOV-blocked" incidences. Proved;
(5) MS6 under a no-twin hypothesis along the Prop K chain (Theorem 5). Proved modulo Prop K and L1. This result is PARTIAL;
(6) a structural remark (Proposition 6): under the chain's own hypotheses, MS6 is equivalent to the problem's conclusion together with MS6 at t = 0. So MS6 is not a strictly easier statement. The configuration any proof must exclude is described exactly;
(7) checks of L1, L2 and the chain. There is a genuine gap in L2 (orbifold homotopy for the vertex u) and a gap in L1 for non-product strata;
(8) a list of open questions.

Readings (R1), (R2) are adopted throughout, exactly as stated in the task.

## 0. Notation used throughout

- B_t := closure(V_t) \ V_t. This is a compact analytic set of dimension ≤ 1. By (R2), H_t(B_0) = B_t, and H_t preserves strata.
- For a point Q ∈ B_0, put Q_t := H_t(Q).
- Def(Q) is the versal deformation germ of the stable curve Q, with smoothing parameters s_e, e ∈ E(G_Q). The group 𝔅 := Aut(Q) acts on Def(Q). The germ of M̄_g at Q is q : Def(Q) → Def(Q)/𝔅.
- On the locus {s_e = 0 for all e ∈ E(G_Q)} ≅ ∏_{x ∈ V(G_Q)} Def(Q_x), each point p has components comp_x(p), labelled by the vertices x of G_Q. Each comp_x(p) is a smooth curve carrying its special points, and it depends holomorphically on p.
- An element a ∈ 𝔅 acts on labels, and comp_x(a p) ≅ comp_{a^{-1}x}(p) as pointed curves.
- The fibre q^{-1}(Q) is {0}. Since q is proper, every lift of Q_t tends to 0 as t → 0.
- **Pattern.** For a point p of Def(Q) put S(p) := {e : s_e(p) = 0}. For S ⊂ E(G_Q):
  - an edge not in S is *unpinched*;
  - a vertex x is *intact* for S if every edge at x lies in S, and *merged* otherwise;
  - M(S) denotes the set of merged vertices.
- A *Y_t-copy* of a point P is a component of P that is isomorphic to Y_t as an n_i-pointed curve, in some order of its special points.
- C_0(Q) := {x ∈ V(G_Q) : comp_x(0) is a Y_0-copy}. This set is 𝔅-invariant.
- A *boundary branch* at Q is a local branch b at Q of B_0 with Q ∉ the stratum of b. Equivalently, Q is a puncture of the piece E_b that contains b.
  - A lift b̃ ⊂ Def(Q) has constant pattern S_b̃. The other lifts are the translates a b̃, with patterns a S_b̃.
  - M^+(b̃) := M(S_b̃) ∪ {x intact for S_b̃ : comp_x is non-constant along b̃}.

## 1. Lemma 1 (time-t criterion for MS6)

**Lemma 1.** Fix t. Suppose there are:
- a point P ∈ B_t,
- a lift P̃ ∈ Def(P),
- a Y_t-copy y of P̃,
- a lift c̃ through P̃ of a boundary branch c at P,

such that y ∈ M(S_c̃), or y is intact for S_c̃ and comp_y is non-constant along c̃. Then the MS6 configuration exists at time t.

*Proof.*
1. Let E be the piece at time t that contains c̃. Concretely, E is the irreducible component, in ∏_w M_w of the stratum Δ_{G_c}, of the lift of closure(V_t) ∩ Δ_{G_c} that contains the image of c̃. Here the stratum locus S_c̃ of Def(P) is mapped to ∏_w M_w by taking partial normalizations. This is compatible with ξ_{G_c}, after identifying G_P / (E(G_P) \ S_c̃) with G_c.
2. P is not in Δ_{G_c}. So the endpoint of c̃ corresponds to a puncture p of Ē.
3. Let u be the vertex of G_c that contains y. Then f_u(p) is the curve obtained by gluing the components comp_x(P̃), x ∈ u, along the unpinched edges between them.
   - comp_y(P̃) is an irreducible component of f_u(p).
   - Its special points in f_u(p) are its special points in P. A half-edge at y is either part of an unpinched edge inside u, which becomes a node of f_u(p), or a half-edge of a pinched edge, which becomes a marked point of M̄_u.
   - So it is a Y_t-copy.
4. **Case y merged.** f_u(p) has a node, so f_u(p) ∈ ∂M̄_u. On E the values of f_u lie in M_u. So f_u is not constant. This is Lemma C2 of PR-C.
5. **Case y intact.** u = {y}, and f_u = comp_y along c̃ is non-constant by hypothesis. In both cases (E, u, p) is an MS6 configuration at time t. ∎

**Remark.** The converse does not hold in the relevant sense. A configuration "Y_t-copy y at an interior point P ∈ E, with the vertex of E carrying y non-constant" (called **MOV-interior** below) is NOT an MS6 configuration. At an interior point there is no puncture, and the moving value lies on a curve, not in a finite set.

## 2. Lemma 2 (transport of branch patterns)

**Lemma 2.** Let Q ∈ B_0 and let b be a boundary branch at Q. Put N := H((b \ {Q}) × Δ) near (Q,0). Then:
- (a) the components of q^{-1}(N) ⊂ Def(Q) × Δ are permuted transitively by 𝔅, and the pattern is constant on each of them. So the components are the a Ñ, with patterns a S, where Ñ ⊃ b̃ has pattern S = S_b̃;
- (b) for every t and every lift Q̃_t of Q_t, some a Ñ has Q̃_t in the closure of its t-slice. For that a, the lift of the branch H_t(b) through Q̃_t has pattern a S;
- (c) the closure of N near (Q,0) is a union of irreducible 2-dimensional germs of an analytic set. The same holds for q^{-1}(N).

*Proof.*
(a) **Patterns are constant on components.**
- The sets {S(p) = S'} for distinct S' with isomorphic contracted graphs are pairwise disjoint.
- Each is relatively open in the union of all strata of that graph type, because a nearby point has fewer zero coordinates unless it is in the same stratum.
- So S(·) is locally constant on q^{-1}(N) ⊂ q^{-1}(Δ_{G_b} × Δ), and hence constant on each component.

**Transitivity.**
- q restricted to q^{-1}(N) is open and closed (finite quotient), and q^{-1}(N) is locally connected (semi-analytic). So each component maps onto N, which is connected: it is homeomorphic to a punctured disc times a disc.
- If Z_1, Z_2 were components with 𝔅Z_1 ∩ 𝔅Z_2 = ∅, take a point n ∈ N. Its fibre is a single 𝔅-orbit, and it would have to lie in both 𝔅Z_1 and 𝔅Z_2, a contradiction.

(b) Q_t ∈ closure(H_t(b)). Hence the closure of q^{-1}(H_t(b)) contains a point of q^{-1}(Q_t) = 𝔅 Q̃_t. By 𝔅-invariance it contains Q̃_t. Near Q̃_t the set q^{-1}(H_t(b)) is contained in ⋃_a (a Ñ)_t. Apply (a).

(c) **The set 𝒜.** Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ). It is analytic by (R1). Let 𝒵 be the part of 𝒜 over strata deeper than Δ_{G_b}; it is analytic.

**N is open and closed in 𝒜 \ 𝒵.**
- Near (Q,0), 𝒜 \ 𝒵 = H((closure(V_0) ∩ Δ_{G_b} ∩ U) × Δ) by (R2).
- For U small, closure(V_0) ∩ Δ_{G_b} ∩ U is a disjoint union of punctured branches at Q, since Q ∉ Δ_{G_b}.
- So N is open and closed in 𝒜 \ 𝒵.

**Conclusion.**
- Let X be an irreducible component of 𝒜 not contained in 𝒵. The set X minus (𝒵, Sing 𝒜, and the other components) is connected and dense in X.
- Hence the closure of a union of connected components of 𝒜 \ 𝒵 is a union of such X.
- Preimages under the finite map q of analytic sets are analytic. ∎

## 3. Theorem 3 (total-merge transport)

**Theorem 3.** Let Q ∈ B_0. Assume:
- (Y) there is a sequence t_n → 0, t_n ≠ 0, such that Q_{t_n} has a Y_{t_n}-copy;
- (TM) for every y ∈ C_0(Q) there is a boundary branch b at Q, with a lift b̃, such that 𝔅·y ⊂ M^+(b̃).

Then for all but finitely many n, the MS6 configuration exists at time t_n. In particular MS6 holds, with T = {t_n : n ≥ n_0} minus a finite set. T accumulates at 0 ∈ Δ.

Hypothesis (Y) holds whenever Q ∈ closure(∂V_0), as shown in the proof.

*Proof.*
1. **Hypothesis (Y) for Q ∈ closure(∂V_0).**
   - Q_t ∈ closure(∂V_t), because H_t commutes with closures and preserves Δ_Γ.
   - Take a branch of ∂V_t at Q_t, and lift it to Def(Q) through a lift Q̃_t. Along it, the vertex-i curve is the constant Y_t ∈ M_{g_i,n_i}.
   - In the chart, the vertex-i curve converges to the curve glued from the components over the contracted vertex. That curve is Y_t, which is smooth, so it is a single component (Lemma D(1) of PR-I; re-checked).
2. **Choice of a limit copy.** Fix lifts Q̃_{t_n} and Y_{t_n}-copies y_n.
   - Pass to a subsequence along which y_n = y is constant and the ordering of special points is fixed.
   - Q̃_{t_n} → 0, and comp_y is continuous. M_{g_i,n_i} is Hausdorff and Y_{t_n} → Y_0 (PR-A). So comp_y(0) ≅ Y_0, i.e. y ∈ C_0(Q).
   - Arguing by contradiction on subsequences, it suffices to show that MS6 holds at t_n for all large n in this subsequence.
3. **Applying (TM).** Take b, b̃ as in (TM) for this y.
   - By Lemma 2(b), at time t_n there is a lift of H_{t_n}(b) through Q̃_{t_n} with pattern a_n S_b̃, lying in a_n Ñ.
   - Pass to a subsequence with a_n = a. Then a^{-1} y ∈ 𝔅y ⊂ M^+(b̃).
4. **Case a^{-1}y ∈ M(S_b̃).** Then y ∈ M(a S_b̃): y is merged along the lift through Q̃_{t_n}. Lemma 1 gives MS6 at t_n. (Q_{t_n} ∉ Δ_{G_b}, because H_t preserves strata.)
5. **Case a^{-1}y intact, with comp_{a^{-1}y} non-constant along b̃.** Then y is intact for a S_b̃, and comp_y is non-constant along a b̃.
   - Let W̃ be any irreducible germ of closure(a Ñ) at (0,0) (Lemma 2(c)). φ := comp_y is holomorphic on W̃, because y is intact for the constant pattern a S_b̃.
   - t is non-constant on W̃, so W̃_0 has pure dimension 1 (Krull). Its components are lifts a′b̃ with a′S_b̃ = a S_b̃, and along each of them φ = comp_{a′^{-1}y} along b̃.
   - a′^{-1}y ∈ 𝔅y is intact for S_b̃, so it is not in M(S_b̃). Hence comp_{a′^{-1}y} is non-constant along b̃. So φ is non-constant on every component of W̃_0.
6. **Generic rank of Φ = (φ, t) on W̃ is 2.**
   - Otherwise every fibre of Φ has dimension ≥ 1 at every point (semicontinuity of fibre dimension).
   - The fibre of Φ through a point of W̃_0 \ {0} lies in W̃_0 ∩ {φ = const}, which is 0-dimensional there. Contradiction.
7. **Only finitely many bad times.**
   - The set Σ := {p ∈ W̃ : dim_p Φ^{-1}Φ(p) ≥ 1} is analytic (Cartan–Remmert, cited from memory). It is a proper subset, so dim Σ ≤ 1.
   - So only finitely many 1-dimensional components of Σ lie in t-fibres, and φ is non-constant on W̃_t for t outside a finite set.
   - There are finitely many germs W̃. So for large n, φ is non-constant along the lift through Q̃_{t_n}, and Lemma 1 (intact case) gives MS6 at t_n. ∎

**Corollary 3′.** If 𝔅 = Aut(Q) fixes every element of C_0(Q), then (TM) reads: every Y_0-copy of Q is merged, or is intact and moving, along some boundary branch at Q. Hence MS6 holds if some Q ∈ closure(∂V_0) with this property exists.

**How Theorem 3 relates to Prop K and to PR-I.**
- Prop K (PR-H) produces a MERGE or MOV branch at a point Q_0 for the *path-marked* copy x_0 only. In general:
  - (G1) Q_0 ∉ closure(∂V_0), so (Y) is not automatic;
  - (G2) other Y_0-copies at Q_0, or 𝔅-translates of x_0, need not be merged (TM fails);
  - (G3) the MOV branch may have Q_0 in its own stratum (MOV-interior), which is excluded from M^+.
- In the quintic example of PR-I (not smooth), at P_0 = A—B—C one has C_0 = {A, C}, branch β (S = {e_1}) with M = {B, C}, and branch β′ (S = {e_2}) with M = {A, B}.
  - If Aut(P_0) does not swap A and C, (TM) holds and Theorem 3 applies.
  - If it does swap them, (TM) fails, and one needs PR-I's Krull-at-time-t argument (Lemma D) instead.
- So Theorem 3 does not supersede PR-I's Theorem 4. It is a different sufficient condition.

## 4. Lemma 4 (spreading of Y_t-copies at a time t where MS6 fails)

Call a coarse piece D (an irreducible 1-dimensional component of closure(V_t) ∩ Δ_G) **MOV-blocked at P** if P ∈ D and no vertex of a lift of D that is constant along D takes a value at P isomorphic to Y_t.

**Lemma 4.** Fix t, and suppose there is NO MS6 configuration at time t. Let P ∈ B_t have a Y_t-copy, and let D be a coarse piece with P ∈ closure(D). Assume that either
- (a) P ∉ D, or
- (b) P ∈ D and D is not MOV-blocked at P.

Then some lift-piece E of D has a vertex u with f_u ≡ const ≅ Y_t, and every point of closure(D) has a Y_t-copy.

*Proof.*
1. **Case (a).** Lift a branch of D at P to Def(P) through a lift P̃ carrying a Y_t-copy y. This is possible by the argument of Lemma 2(b) at fixed t.
   - Since MS6 fails at t, Lemma 1 says that y is intact for the branch pattern, and that comp_y is constant along the branch.
   - So the vertex u = {y} of the lift-piece E containing the branch has f_u constant on a branch, hence on E by the identity theorem on Ē. Its value is comp_y(P̃) ≅ Y_t.
2. **Case (b).** The vertex given by the hypothesis is constant along D with value ≅ Y_t.
3. **Every point of closure(D) has a Y_t-copy.**
   - ξ_G(E) = D, since ξ_G(E) ⊂ D, both are irreducible, and ξ_G(E) contains a branch of D.
   - Every R ∈ closure(D) is ξ̄_G(ν(r)) for some r ∈ Ē, and the u-coordinate of ν(r) is the smooth curve Y_t ∈ M_u.
   - So R has a component ≅ Y_t, carrying the same special points as in the proof of Lemma 1. ∎

**Corollary 4′.** Let B_t^∂ be the connected component of B_t containing ∂V_t. Note B_t^∂ = H_t(B_0^∂). Suppose MS6 fails at t and no coarse piece in B_t^∂ is MOV-blocked at a point of B_t^∂. Then:
- every point of B_t^∂ has a Y_t-copy;
- every coarse piece in B_t^∂ has a lift with a vertex that is constant and ≅ Y_t.

*Proof.*
1. B_t^∂ is a finite union of closures of coarse pieces. A compact analytic set of dimension ≤ 1 has 1-dimensional irreducible components, each the closure of the piece of its generic stratum, together with isolated points. The component containing the 1-dimensional set ∂V_t is a union of the former, and their incidence graph (two pieces adjacent if their closures meet) is connected.
2. Start from the pieces of ∂V_t, whose vertex i is ≡ Y_t, and apply Lemma 4 along the incidence graph. ∎

**What Lemma 4 shows.** If MS6 fails, the Y_t-copies are never "lost" at a puncture. They can be lost only at MOV-blocked incidences, i.e. MOV-interior configurations. They can also be carried by a component different from the one at t = 0 (twins). Lemma 4 is purely a time-t statement and uses neither total geodesy nor L2.

## 5. Theorem 5 (MS6 when no automorphism moves the tracked copy along the Prop K chain) — PARTIAL

**Chain data (CH)**, as produced by Prop K (PR-H §3) together with the argument below:
- STAY pieces D^0 ⊂ ∂V_0, D^1, …, D^m (coarse pieces at time 0);
- junction points J^k ∈ closure(D^{k−1}) ∩ closure(D^k), for k = 1, …, m;
- a terminal point Q_0 ∈ closure(D^m);
- for each k, a vertex w_k of D^k, constant on D^k with value Y_0 (w_0 = i);
- labels x_k ∈ V(G_{J^k}) and x_Q ∈ V(G_{Q_0}), such that:
  - in Def(J^k) there are lifts of a branch of D^{k−1} and of a branch of D^k through 0, along both of which x_k is intact and comp_{x_k} is the w_{k−1}-coordinate (resp. the w_k-coordinate);
  - the same holds at Q_0 for D^m, w_m and x_Q;
- a boundary branch b at Q_0 with a lift b̃ such that x_Q ∈ M^+(b̃). This is MERGE, or MOV with Q_0 ∉ the stratum of b.

**Why Prop K gives (CH), apart from the terminal condition.**
- K_0 is a compact connected subset of B_0 on which the path-marked Σ_i is pinched off and ≅ Y_0.
- If K_0 contains a smooth point x of a piece D other than a junction, then K_0 contains a non-degenerate continuum in D through x (K_0 is connected and not a point). So the path-marked Σ_i-vertex of D, a holomorphic coordinate, is ≡ Y_0 on D.
- B_0 has finitely many singular and junction points, so K_0 lies in the union of finitely many such STAY-piece closures and finitely many points, and connectedness gives the chain.
- The labels x_k come from the consistency of the path marking that Prop K asserts.
- The terminal condition x_Q ∈ M^+(b̃) holds when Prop K ends in MERGE, or in MOV with Q_0 a puncture of b's piece. It FAILS for MOV-interior.

**(NT) No twin moved by automorphisms:** Aut(J^k) fixes x_k for every k, and Aut(Q_0) fixes x_Q. This holds, for example, if x_k (resp. x_Q) is the only Y_0-copy of J^k (resp. Q_0).

**Theorem 5.** Assume (R1), (R2), L1 for the pieces D^k (proved in product-type strata, see §7), (CH) and (NT). Then MS6 holds: for all t in a punctured disc around 0, outside a finite set, there is an MS6 configuration at time t.

*Proof.*
1. **Constancy at time t.** By L1, the vertex w_k is constant on D^k_t := H_t(D^k), with some value z_k(t).
2. **Matching at a junction J = J^k.** Fix a continuous lift J̃_t of J_t. Continuous lifts exist by path lifting for finite group quotients (Bredon, *Introduction to compact transformation groups*, II.6, cited from memory).
   - By Lemma 2(b), applied to the branch of D^k (and to that of D^{k−1}), the lift of the transported branch through J̃_t has pattern a S^+ for some a ∈ Aut(J^k). Its constant vertex is the image a·(label of w_k).
   - By (NT), a fixes x_k, so x_k is intact along that lift. Its coordinate is the w_k-coordinate, which is constant ≡ z_k(t). The limit at J̃_t is comp_{x_k}(J̃_t).
   - So z_k(t) ≅ comp_{x_k}(J̃_t). In the same way, from the D^{k−1} side, z_{k−1}(t) ≅ comp_{x_k}(J̃_t).
   - Hence z_{k−1}(t) ≅ z_k(t) for all t near 0. Here "near 0" depends only on the fixed chart Def(J^k).
3. **Chaining.** Y_t = z_0(t) ≅ z_1(t) ≅ … ≅ z_m(t). By the same argument at Q_0, z_m(t) ≅ comp_{x_Q}(Q̃_t). So comp_{x_Q}(Q̃_t) is a Y_t-copy for all small t.
4. **Terminal step.** By (NT), every a ∈ Aut(Q_0) satisfies a^{-1}x_Q = x_Q ∈ M^+(b̃). Steps 3–7 of the proof of Theorem 3, with y := x_Q, now apply for every small t, not just along a subsequence:
   - in the merged case, Lemma 1 applies directly;
   - in the intact-moving case, there are finitely many germs W̃, and the bad times form a finite set. ∎

**Status.**
- Theorem 5 is rigorous given (CH), (NT) and L1.
- (CH) depends on Prop K (stated in PR-H as "proved modulo routine marking details", not re-checked here) and on its terminal branch NOT being MOV-interior.
- Hence Theorem 5 is a PARTIAL answer. It covers the case "no automorphism of a junction or terminal point moves the tracked Y_0-copy, and the terminal branch is MERGE or MOV-at-a-puncture".

## 6. Proposition 6: MS6 is not easier than the problem

**Proposition 6.** Assume the chain's inputs:
- L2 for every pair (E_0, u) with u non-constant;
- hence (O) for all those pairs;
- continuity in t of transported puncture values, which follows from the germ argument of PR-J Step 2.

Then MS6 ⇔ [Y_t = Y_0 for all t, and an MS6 configuration exists at t = 0].

*Proof.*
- (⇒) The chain (§7) gives Y_t = Y_0 for all t.
  - Take one MS6 configuration (E_t, u, p) at some t ∈ T. By L1, u is non-constant on the corresponding piece E_0.
  - By L2, the transported puncture value f_u^s(p_s) is constant in s. So f_u^0(p_0) = f_u^t(p) contains a Y_t-copy, and Y_t = Y_0.
  - So (E_0, u, p_0) is an MS6 configuration at t = 0.
- (⇐) Let (E_0, u, p) be an MS6 configuration at t = 0.
  - By L2, g_t is non-constant, and f_u^t(p_t) ranges over a finite set. It is continuous in t, so it is constant, equal to f_u^0(p_0).
  - That curve contains a Y_0-copy, which is a Y_t-copy since Y_t = Y_0. ∎

**Consequence.** Any proof of MS6 must exclude the following configuration (Ob), which is exactly what a counterexample to the problem would look like near the Prop K terminal point:
- at Q_t, the copy merged along the rigid branch b_t has value ≡ Y_0, because it lies in a rigid puncture value (L2);
- the Y_t-copy carried by the network (Lemma 4) is a *different* component;
- the two coincide in value only at t = 0.

By Theorem 5, (Ob) requires at least one of:
- (G2′) an automorphism of some junction J^k or of Q_0 that moves the tracked copy;
- (G3) a MOV-interior terminal;
- a failure of L1 / Prop K.

Local analysis cannot exclude (G2′). Lemma C1 of PR-C and its time-t version only produce *some* branch pinching a given edge. They do not produce a branch merging a given copy, as PR-C's example s_γ = uv, s_e = v shows.

## 7. Checks of the chain lemmas L1, L2 and of the derivation

**L1.**
- *Product-type strata: correct.* The chain of reasoning, written out:
  1. 𝓦 → Δ is proper, and pr_u(𝓦_0) = {Z_0}. Upper semicontinuity of the fibres of a proper map gives pr_u(𝓦_t) ⊂ U (affine) for |t| < ε.
  2. A compact connected analytic curve maps constantly to an affine variety, so on each component of 𝓦_t, |t| < ε, pr_u is constant. The constants may differ between components.
  3. Hence Ψ = (pr_u, t) maps 𝓦 ∩ {|t| < ε} onto a set with finite t-fibres. Ψ(𝓦) is irreducible (Remmert, Ψ proper) and has a 1-dimensional open part, so dim Ψ(𝓦) = 1. Its t-fibres are finite for all t, since t is non-constant on it.
  4. This gives L1.
- *Supplement (used in Proposition 6 and Theorem 3).* If pr_u is non-constant on some component of 𝓦_0, then dim Ψ(𝓦) = 2, so Ψ(𝓦)_t is pure 1-dimensional for every t (Krull), and pr_u is non-constant on some component of 𝓦_t for every t.
- *Non-product strata: GAP.*
  - Pieces in MS6 are components of the lift in ∏_w M_w, and ξ_G may ramify along loci that the transported family crosses differently at different t.
  - Then the closure of one lift-component of H(E_0 × Δ) can have, over t = 0, several lift-components of E_0 that differ by graph automorphisms. pr_u may be constant on one of them and not on another, and the proof of L1 needs constancy on all of 𝓦_0.
  - Fix: either state L1 for "constant on every lift-component in 𝓦_0", or add an (O)-type hypothesis for ξ_G. In product-type strata ξ_G is bijective and the issue does not arise.

**L2. Genuine GAP (orbifold homotopy for u).**
- The step "g_t := f_u^t ∘ A_t is (orbifold-)homotopic to g_0" is not justified by (O) for (E_0, v). (O) transports the orbifold structure and monodromy adapted to v, and A_t is an orbifold isomorphism for v's structure.
- Homotopy of maps into the *coarse* space M_u carries no information: coarse M_u is simply connected, because Mod is generated by torsion elements (cited from memory).
- Imayoshi–Shiga needs equality of monodromies π_1^{orb} → Mod_u, i.e. an (O)-type hypothesis (O_u) for (E_0, u): the cone points and monodromy of f_u transport along the family as well. The cone points of f_u and of f_v can differ.
- So step 3 of the derivation must assume (O) for every pair (E_0, u) with u non-constant, not only for the Teichmüller vertex.
- *Correct as written:*
  - non-constancy of g_t: finite monodromy gives a bounded lift on a finite cover, which extends over the punctures (Riemann) and is constant;
  - extension of g_t to the punctures: it is the restriction of ν_t;
  - finiteness of the puncture values.
- *Citation precision.* Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces" (1988), from memory: for a Riemann surface of finite type R and type (g,n), a non-constant holomorphic map R → M_{g,n}[N] (level N ≥ 3) is determined by its homotopy class, and there are only finitely many such classes realised. Only "finitely many holomorphic maps in a homotopy class" is used here.

**Derivation steps 1–4.**
- Step 1 is correct. Pigeonhole on a sequence t_n → t* ∈ Δ, then the identity theorem in an orbifold chart at y.
- Step 4: the transport of pieces and punctures is correct by (R2), with the non-product caveat of L1 above.
- With (O_u) added, the derivation MS6 ⇒ problem is correct as stated, modulo (F2) of PR-F and the cited theorems.

## 8. Summary: proved / not proved / open

**Proved (under (R1), (R2)):**
- Lemma 1 (time-t criterion: merge, or move at a puncture, gives MS6 at t).
- Lemma 2 (transport of branch patterns).
- Theorem 3 and Corollary 3′: MS6 follows from (TM) at one point Q ∈ closure(∂V_0), or from (TM) plus (Y) at any Q ∈ B_0.
- Lemma 4 and Corollary 4′ (spreading of Y_t-copies at a time where MS6 fails, except across MOV-blocked incidences).
- Theorem 5, given L1 (product type), the chain data (CH) from Prop K, and (NT): MS6 holds with T a punctured disc minus a finite set. This is PARTIAL in the task's sense: it assumes absence of automorphism-moved twins at junctions and at the terminal point, and a non-MOV-interior terminal.
- Proposition 6 (MS6 ⇔ problem's conclusion plus MS6 at t = 0, under the chain inputs).
- L1 is verified in product-type strata.
- Gaps found:
  - in L2: orbifold homotopy for vertex u; (O_u) must be added;
  - in L1 for non-product strata.

**Not proved:**
- MS6 in general. No counterexample is found either.

**Open questions:**
1. (G2′) Twins moved by automorphisms. Can an automorphism of a junction J^k or of Q_0 move the path-marked Y_0-copy, such that at t ≠ 0 the network copy (≅ Y_t) and the merged copy (≡ Y_0, rigid) separate? This is configuration (Ob). No local argument excludes it.
2. (G3) MOV-interior terminal. Can Prop K's network end only at points Q_0 lying *inside* a piece E_b along which the tracked copy moves, with no MERGE or MOV-at-puncture anywhere on B_0^∂? In that case even MS6 at t = 0 fails, and the chain (MS6 + L2) cannot pin Y_t, since Y_t would only be constrained to the rigid curve closure(π_w(E_b)).
3. Whether Prop K can be re-run from an arbitrary STAY piece with a twin constant vertex, which would iterate past twins. Lemma PA applies to any piece, but I have not re-checked Lemma NH and Prop K in that generality.
4. (O), (O_u) and (F2), as before.

=== END OF ANSWER round7_q2 ===

