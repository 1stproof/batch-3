# round7_q6 — MS6 by a time-t analysis plus a "locked copies" transport

## Status / plan (written first)
Plan: (1) prove the fixed-t local lemmas of the suggested approach: a merge, or a move ending at a puncture, of ANY Y_t-copy gives MS6 at t (Lemma 1); N_t is closed (Lemma 2); if MS6 fails at t, then N_t is open except at "interior-MOV" points (Lemma 3). (2) Show why step 2(b) (a contradiction using only time-t data) cannot work, and locate the obstruction in step 2(a) passing to t -> 0: twins. (3) Main positive result, Theorem T: transport from t = 0 along the network K_0 of Proposition K, using only ISOMORPHISM CLASSES of components, which automorphisms preserve, and NOT the identities of branches. This proves MS6 for every t in a neighbourhood of 0, provided Proposition K ends in MERGE or puncture-MOV and a "locking" condition (Lock) holds at finitely many points of K_0. (Lock) holds automatically when those points have only one Y_0-component.

Conventions: (R1), (R2) as in the task; H_0 = id. B_t := closure(V_t) \ V_t. A *Y_t-copy* of a stable curve Q is an irreducible component of Q whose normalization, with its special points (preimages of nodes), is isomorphic to Y_t as an n_i-pointed curve after some reordering. For Q in M̄_g, Def(Q) is the versal deformation germ (smooth), and π: Def(Q) -> M̄_g is locally the quotient by Aut(Q). In Def(Q) the components of the central fibre are labelled by V(G_Q), and the nodes by E(G_Q), with smoothing parameters s_e. At a point r of Def(Q) with unpinched edge set U(r) := {e : s_e(r) ≠ 0}, the components of the curve C_r are labelled canonically by the vertices of the contraction G_Q/U(r), i.e. by subsets of V(G_Q).

Standard facts used, cited from memory:
- **(Def1)** For each S ⊂ E(G_Q) and each vertex V of G_Q/(E \ S), the V-component (with its special points) of C_r is a continuous function on {s_e = 0, e ∈ S}, with values in M̄_{g_V,n_V}/S_{n_V}, and holomorphic on each analytic subset there. Its value at a point where further edges inside V are pinched is the stable curve glued from the corresponding components. This comes from the partial normalization of the universal curve along the nodes in S.
- **(Def2)** Def(Q) is versal at every nearby point r, and Stab_{Aut(Q)}(r) ≅ Aut(C_r).

All other prior results (PR-x, L1, L2, Proposition K) are as quoted in the task file. Their status is restated where they are used.

## 1. Fixed-t local lemmas (proved)

Fix t. Let Q ∈ B_t, let x ∈ V(G_Q) be a vertex with Q_x a Y_t-copy, and let b be a 1-dimensional branch of B_t at Q. Let b̃ be a branch at a lift q of Q in Def(Q) of π^{-1}(b), with pinched set S_b := {e : s_e ≡ 0 on b̃} and U_b := E(G_Q) \ S_b. Let G_b := G_Q/U_b; this is the dual graph along b̃ \ {q}, which lies in one stratum. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing π(b̃ \ {q}), lifted to ∏_w M_w in the way the local labelling of b̃ induces. Let p ∈ Ē be the point over Q determined by b. Write [x] for the vertex of G_b containing x.

**Lemma 1 (merges and puncture-moves give MS6).**
- (a) Suppose some edge of G_Q at x lies in U_b ("merge"). Then f_{[x]} is non-constant on E, p is a puncture of E, and f_{[x]}(p) has the component Q_x with the same special points. So MS6 holds at t, witnessed by (E, [x], p).
- (b) Suppose all edges at x lie in S_b, Q ∉ Δ_{G_b} (i.e. U_b ≠ ∅), and f_{[x]} = f_x is non-constant on E. Then p is a puncture and f_x(p) = Q_x ≅ Y_t. So MS6 holds at t.

*Proof.*
- (a) By (Def1), as r → q along b̃ the [x]-component of C_r tends to the curve glued from the components Q_y, y ∈ [x], along the edges of U_b inside [x]. This set of edges contains an edge at x, so the limit is a nodal curve in ∂M̄_{[x]}. Off q the [x]-component lies in M_{[x]}. So f_{[x]} is non-constant (PR-C, Lemma C2), and ν(p) ∉ ∏_w M_w, so p is a puncture.
  - Q_x is a component of the limit curve f_{[x]}(p). Its special points there are the branches of nodes internal to [x] together with the marked points coming from edges leaving [x]. Together these are exactly the node branches of Q at Q_x. So the pointed curve is unchanged.
- (b) Here [x] = {x}, and by (Def1) f_x(p) = Q_x. Some edge of G_Q lies in U_b, so it is contracted into some vertex w of G_b, and f_w(p) is nodal. Hence ν(p) ∉ ∏ M_w, and p is a puncture. ∎

**Lemma 2 (closedness).** N_t := {Q ∈ B_t : Q has a Y_t-copy} is closed in B_t. More generally: if t_n → t, Q_n ∈ B_{t_n}, Q_n → Q, and Q_n has a Y_{t_n}-copy, then Q has a Y_t-copy.

*Proof.*
- Lift to Def(Q): r_n → q. Pass to a subsequence with U(r_n) = U constant, and with the copy of Q_n at a fixed vertex V of G_Q/U.
- By (Def1), the V-component of C_{r_n} converges to the curve glued from the Q_y, y ∈ V, along the edges of U inside V. Since Y_{t_n} → Y_t (PR-A) and Y_t is smooth, this limit is smooth.
- So V is a single vertex y, with no edge of U at y forming a node inside V, and Q_y ≅ Y_t. ∎

**Lemma 3 (dichotomy at a point of N_t).** Suppose MS6 fails at t. Let Q ∈ N_t, let x be any Y_t-copy of Q, and let b be any branch of B_t at Q (any lift b̃). Then exactly one of the following holds:
- (STAY) all edges at x are pinched along b̃, and f_x is constant (≡ Q_x) on the piece E of b; or
- (IMOV, interior move) all edges at x are pinched along b̃, U_b = ∅ (so Q ∈ E is an interior point of the piece, in the same stratum), and f_x is non-constant on E.

Consequently, if moreover no IMOV occurs at points of N_t, then N_t is open in B_t. By Lemma 2 it is then a union of connected components of B_t, and it contains the connected component C_t of B_t containing ∂V_t (on which vertex i is a copy).

*Proof.*
- Lemma 1(a) excludes a merge, and Lemma 1(b) excludes a non-constant f_x with U_b ≠ ∅. What remains is STAY or IMOV.
- Openness: near Q, B_t is the union of its finitely many branches b. If b is STAY for some copy x, the points of b near Q carry the constant component Q_x, so they lie in N_t. ∎

**Remarks on the approach of the task.**
1. IMOV cannot be excluded by Lemma 1: an interior point is not a puncture. L1 and L2 give only that Y_t lies on the t-independent curve closure(π_x(E_0)), with value Y_t = g(σ(t)) where g is one of finitely many maps (L2) and σ(t) := A_t^{-1}(Q̃_t) ∈ Ē_0. The point σ(t) is the transported "junction point" Q_t on E_t. Nothing ties it to a puncture or to a cone point of Ē_t, because A_t is the Thurston/Teichmüller identification and not H_t. So the IMOV case is **not pinned** by these tools. It remains open (see §4).
2. **Step 2(b) is dead in the stated generality (heuristic, not proved).** At a fixed t ≠ 0, V_t is an arbitrary algebraic surface: total geodesy is not available. The only time-t inputs are (R1) and the local analytic structure. A configuration in which a connected component C of the boundary carries a fixed isolated constant component Y is not locally contradictory. Near such a component, closure(V_t) looks like a smoothing of "Y glued to a moving family", with the normal direction contracting (negative normal degree, -ψ·C < 0, so Grauert contractibility is consistent). I did not construct a global algebraic example, so this is only a heuristic. But it shows that any contradiction must come from t = 0, as in option (a), and hence must face the twin problem. §2 explains exactly where that problem enters, and §3 bypasses it under (Lock).

## 2. Where option 2(a) breaks: twins (analysis)

Suppose MS6 fails, and Lemma 3 gives N_{t_n} ⊇ C_{t_n} = H_{t_n}(C_0) for generic t_n → 0. Pass to t = 0, and fix Q_0 ∈ C_0 together with the MERGE branch b of Proposition K, in which the tracked copy c of Q_0 merges along a lift b̃.
- For lifts q_n → q_0 of Q_{t_n}, every lift-branch b̃_n of b_{t_n} at q_n converges into a lift γ b̃ of b, for some γ ∈ Aut(Q_0). By the edge count of Step 3 below, its pinched set is S_{b̃_n} = γ S_b̃. So the label γc merges along b̃_n.
- The Y_{t_n}-copies of Q_{t_n} converge to Y_0-copies of Q_0 (Lemma 2), so the limiting labels lie in Λ(Q_0) := {ℓ ∈ V(G_{Q_0}) : Q_{0,ℓ} is a Y_0-copy}.
- But γc need not be among them. Q_0 may have several Y_0-copies, a merged one and an unmerged twin, and for t ≠ 0 these may stop being isomorphic. Then the merged one is not a Y_t-copy, and no contradiction arises.

This is exactly the twin phenomenon of PR-G/PR-I. Option (a) and the direct transport of §3 fail or succeed at the same place. I therefore isolate the needed property as a hypothesis.

**Definition (Lock).** Let R ∈ B_0 ∩ Δ_{G'}, let q_0 ∈ Def(R) be a lift, and let Λ(R) ⊂ V(G') be the set of labels of Y_0-copies of R. Note that Λ(R) is Aut(R)-invariant. R is *locked* if there is ε > 0 such that, for |t| < ε and every lift q of R_t := H_t(R) in a fixed small neighbourhood of q_0 in Def(R), the components C_{q,ℓ}, ℓ ∈ Λ(R), are pairwise isomorphic as pointed curves up to reordering.
- (Lock) holds trivially if |Λ(R)| = 1, i.e. R has a unique Y_0-copy.
- It holds at the point P_0 of the quintic example (PR-I, Proposition 3, Steps 3–4: A_t ≅ C_t ≅ Y_t for all t, and Λ(P_0) = {A, C} since B_0 has two special points).
- Note that R_t ∈ Δ_{G'} for all t by (R2), so its lifts lie in D' := {s_e = 0 for all e} ⊂ Def(R), where the labels make sense.

## 3. Theorem T: MS6 near t = 0 under (Lock) (proved modulo Proposition K and the cited standard facts)

### 3.1 Two auxiliary lemmas

**Lemma 4 (connected subsets of B_0).** B_0 is a compact analytic set of pure dimension 1. A compact connected K ⊂ B_0 is either a point or a finite union of closed arcs, each contained in the closure of one piece and meeting that piece in the arc minus finitely many points.

*Proof.*
- **Pure dimension 1.** closure(V_0) is pure 2-dimensional, and locally (in Def) B_0 is cut out by the single equation ∏ s_e = 0. So by Krull every component of B_0 has dimension ≥ 1, and dim B_0 ≤ 1.
- **Graph structure.** A compact 1-dimensional analytic set is triangulable as a finite graph. Its vertices include the singular points and the points where the stratum changes, and each open edge lies in a single piece.
- **K ∩ an edge.** Let e be a closed edge (an interval) and J a component of K ∩ e. If J missed both endpoints of e, apply the boundary-bumping theorem for the continuum K and an open interval U ⊃ J in e°. The component of K ∩ closure(U) containing J meets ∂U, so it is an interval strictly larger than J inside K ∩ e. This is a contradiction.
- So each component of K ∩ e contains an endpoint of e. Hence K ∩ e is a union of at most two closed intervals, or all of e.
- **Conclusion.** K is a finite union of points and closed arcs. Since K is connected, it is a single point or has no isolated points. ∎

**Lemma 5 (constant vertices at a junction).** Let E_0 be a piece of B_0 in a product-type stratum Δ_G, and x a vertex of G with π_x ≡ z_0 on E_0, where z_0 is a Y_0-copy-class. Put E_t := H_t(E_0). Then:
- (i) π_x is constant on E_t, with value z(t). The map t ↦ z(t) is continuous, and z(0) = z_0.
- (ii) Let R ∈ closure(E_0) ∩ Δ_{G'}, R_t := H_t(R), and q any lift of R_t. Then there is a label ℓ ∈ V(G') with C_{q,ℓ} ≅ z(t), as pointed curves up to reordering.
- (iii) If t_n → 0 and lifts q_n of R_{t_n} converge to the lift q_0 of R, then for large n every label ℓ_n as in (ii) lies in Λ(R).

*Proof.*
- **(i).** This is L1. **Check of L1 (I verified it).**
  - 𝓦 (the closure of the lift of H(E_0 × Δ); Lemma R0) is irreducible, 2-dimensional and proper over Δ, and pr_x(𝓦_0) = {z_0}.
  - Take an affine neighbourhood U of z_0 in the coarse space. By properness, pr_x(𝓦_t) ⊂ U for |t| small. Compact curves map to points of an affine variety, so the image Z := (pr_x, t)(𝓦) is finite over a small disc.
  - Z is analytic and irreducible by Remmert, so dim Z = 1. Hence Z is finite over all of Δ, and pr_x is constant on every compact irreducible curve in every fibre 𝓦_t.
  - For product type, closure(E_t) ⊂ 𝓦_t up to finitely many points (R0 with base point t; (R2) is symmetric in t), and E_t is irreducible (PR-D, Step 1). So π_x|_{E_t} ≡ z(t).
  - Continuity: z(t) = π_x(H(e, t)) for any fixed e ∈ E_0, and H is continuous.
- **(ii).**
  - R_t ∈ closure(E_t), by (R2) together with the fact that homeomorphisms commute with closures. Let β be a branch of closure(E_t) at R_t. The germ π^{-1}(β) is nonempty at every point of the fibre π^{-1}(R_t), since π^{-1}(β) is Aut(R)-invariant. Let β̃ be a branch of π^{-1}(β) at q.
  - Along β̃ \ {q}, the curve C_r has a component ≅ z(t). It sits at some vertex V(r) of G'/U, where U is the unpinched set of β̃.
  - The set {r ∈ β̃ : C_{r,V} ≅ z(t)} is analytic for each V (by (Def1)), and the union over the finitely many V is all of β̃. So one V works on all of β̃.
  - By (Def1), the limit at q of C_{r,V} is the curve glued from the C_{q,y}, y ∈ V, along the internal edges of U. It equals z(t), which is smooth. So V = {ℓ} is a single label, with no edge of U forming a node inside V, and C_{q,ℓ} ≅ z(t).
- **(iii).**
  - Suppose not. Pass to a subsequence with ℓ_n = ℓ ∉ Λ(R) fixed.
  - The q_n lie in D' (strata are preserved), on which ℓ ↦ C_{q,ℓ} is continuous by (Def1). So C_{q_0,ℓ} = lim C_{q_n,ℓ} ≅ lim z(t_n) = z_0, a Y_0-copy class. Hence ℓ ∈ Λ(R), a contradiction. ∎

(For pieces in non-product strata, replace E_t by an irreducible component of the lift of H((E_0 \ S_0) × Δ) to ∏_w M_w, as in R0, Step 3. The same proof applies. I have only checked this routinely.)

### 3.2 Statement and proof

**Input from t = 0 (Proposition K, PR-H §3, "proved modulo routine marking details" there; not re-verified here).** There are:
- a compact connected K_0 ⊂ B_0 with P ∈ K_0 ∩ ∂V_0, every point of which has a Y_0-copy;
- a point Q_0 ∈ K_0, and a branch b of B_0 at Q_0 with a lift b̃ at q_0 ∈ Def(Q_0), and a label c ∈ Λ(Q_0), such that along b̃ either (MERGE) some edge at c is unpinched, or (MOV) all edges at c are pinched and the c-component is non-constant along b̃.

Theorem T uses only these properties, and not the path-marking ("tracking") in Proposition K.

**Theorem T.** Assume (R1), (R2), the hypotheses of the problem, and the input above. Assume moreover:
- (T1) b is MERGE, or b is MOV with Q_0 ∉ Δ_{G_b} (Q_0 is a puncture of the piece of b; "puncture-MOV");
- (T2) the finitely many pieces met by the arcs of K_0 (Lemma 4) lie in product-type strata (removable, see the parenthetical remark after Lemma 5);
- (T3) (Lock) holds at P, at Q_0 and at the finitely many junction points R_1, …, R_{m-1} chosen in Step 0 below.

Then there is ε > 0 such that for every |t| < ε, MS6's witness exists at t. That is, there are a piece E at time t, a vertex u non-constant on E, and a puncture p of E such that f_u(p) has a Y_t-copy. In particular MS6 holds, with T ⊇ {|t| < ε}.

*Proof.*

**Step 0 (chain).**
- If K_0 = {P}, then Q_0 = P; put m := 0 and skip Steps 1–2.
- Otherwise, by Lemma 4, K_0 = A_1 ∪ … ∪ A_N is a finite union of closed arcs. Their intersection graph is connected, since K_0 is connected and the arcs are closed. So there is a chain of arcs A_1, …, A_m with P ∈ A_1, Q_0 ∈ A_m, and junction points R_k ∈ A_k ∩ A_{k+1}. Put R_0 := P and R_m := Q_0.
- Let A_k ⊂ closure(E^k), where E^k is a piece and A_k \ E^k is finite.
- Every point of A_k ∩ E^k has a Y_0-copy, and the copy is one of the finitely many vertex coordinates of the point. So for some vertex x_k, the analytic set {e ∈ E^k : π_{x_k}(e) is a Y_0-copy class} contains an open sub-arc, and hence equals E^k.
- Thus π_{x_k} ≡ z_k(0), a Y_0-copy class, on E^k_0. Let z_k(t) be as in Lemma 5(i).

**Step 1 (start).**
- P_t := H_t(P) ∈ ∂V_t, and the component of P_t at vertex i is Y_t. Apply Lemma 5(ii),(iii) to the component of ∂V_0 through P with the constant vertex i. For small |t| and every lift q of P_t near q_0, Y_t ≅ C_{q,ℓ_0} for some ℓ_0 ∈ Λ(P).
- Lemma 5(ii),(iii) for (E^1, x_1, R_0 = P) gives, for small |t| and lifts near q_0, a label ℓ ∈ Λ(P) with C_{q,ℓ} ≅ z_1(t). By (Lock) at P, z_1(t) ≅ C_{q,ℓ_0} ≅ Y_t.
- In detail: if this failed along t_n → 0, choose lifts q_n of P_{t_n} converging to q_0. This is possible since P_{t_n} → P, the fibres of π accumulate on π^{-1}(P) = Aut(P)·q_0, and we may translate by Aut(P). Lemma 5(iii) and (Lock) then give a contradiction.

**Step 2 (induction along the chain).** At R_k (1 ≤ k ≤ m−1), apply Lemma 5(ii),(iii) to (E^k, x_k) and to (E^{k+1}, x_{k+1}) at the same lift q of R_{k,t} near q_0(R_k). For small |t|, z_k(t) ≅ C_{q,ℓ} and z_{k+1}(t) ≅ C_{q,ℓ'} with ℓ, ℓ' ∈ Λ(R_k). By (Lock) at R_k, z_{k+1}(t) ≅ z_k(t). (Argue by contradiction along sequences, as in Step 1.) By induction, z_m(t) ≅ Y_t for |t| < ε.

**Step 3 (the end point; MERGE).**
- Let t_n → 0 and let q_n be lifts of Q_{t_n} := H_{t_n}(Q_0) converging to q_0. The branch b_{t_n} := H_{t_n}(b) is a branch of B_{t_n} at Q_{t_n}, lying in Δ_{G_b} by (R2). Let b̃_n be a branch of π^{-1}(b_{t_n}) at q_n, with pinched set S_n. Pass to a subsequence with S_n = S constant.
- **Limit branch.** Points of b̃_n map to H_{t_n}(b). Since H^{-1} is continuous and H_0 = id, every limit point of ∪_n b̃_n lies in π^{-1}(b).
  - Each b̃_n is connected, passes through q_n, and leaves the ball of radius r around q_0 (for r small and n large, because H_{t_n} → id uniformly near Q_0). So the limit set contains points at every small distance r from q_0.
  - These points lie in π^{-1}(b) ∩ {s_e = 0, e ∈ S}. So some branch γb̃ of π^{-1}(b) at q_0 (γ ∈ Aut(Q_0); the branches of the preimage of the irreducible germ b are permuted transitively by Stab(q_0) = Aut(Q_0)) meets this closed analytic set in infinitely many points accumulating at q_0. Hence γb̃ ⊂ {s_e = 0, e ∈ S}, i.e. S ⊂ γS_b̃.
- **Edge count.** Both b̃_n \ {q_n} and γb̃ \ {q_0} lie over Δ_{G_b}. Along such a branch the pinched edges are exactly the nodes of the generic curve, so |S| = |E(G_b)| = |γS_b̃|. Hence S = γS_b̃, and the unpinched set is U_n = γU_b̃.
- **The merged label is a Y_t-copy.**
  - In the MERGE case, U_b̃ contains an edge at c, so U_n contains an edge at γc. Moreover γc ∈ Λ(Q_0), since automorphisms preserve isomorphism classes of components.
  - By Step 2 and Lemma 5(ii),(iii) for (E^m, x_m) at R_m = Q_0, some label ℓ ∈ Λ(Q_0) has C_{q_n,ℓ} ≅ z_m(t_n) ≅ Y_{t_n}. (If m = 0, use the label i as in Step 1.)
  - By (Lock) at Q_0, C_{q_n,γc} ≅ Y_{t_n}.
- **Conclusion.** Lemma 1(a), applied at time t_n to Q = Q_{t_n}, x = γc and the branch b_{t_n} with lift b̃_n, gives MS6's witness at t_n.
- Since t_n → 0 was an arbitrary sequence (and the subsequence extraction is harmless), the witness exists for all small |t|.

**Step 3′ (the end point; puncture-MOV).**
- Proceed as in Step 3 up to S = γS_b̃. In the MOV case all edges at c lie in S_b̃, so all edges at γc lie in S: the label γc is intact along b̃_n. As before, (Lock) gives C_{q_n,γc} ≅ Y_{t_n}.
- Since Q_0 ∉ Δ_{G_b} and strata are preserved, Q_{t_n} ∉ Δ_{G_b}. So Lemma 1(b) applies at t_n, provided the γc-component is non-constant along b̃_n.
- Suppose instead it is constant along b̃_n for infinitely many n. Then it is ≡ C_{q_n,γc} ≅ Y_{t_n}.
  - On the closed set {s_e = 0 for e at γc}, which contains all b̃_n and γb̃, the γc-component is continuous (Def1).
  - Every limit point y of the b̃_n then has γc-component ≅ lim Y_{t_n} = Y_0. These limit points include infinitely many points of γb̃ accumulating at q_0, as in Step 3.
  - Hence the γc-component is constant (≅ Y_0) on γb̃, by the identity theorem on the normalized branch. Applying γ^{-1}, the c-component is constant on b̃, contradicting MOV.
- So for large n the γc-component moves along b̃_n, and Lemma 1(b) gives the witness at t_n. ∎

**Corollary T′ (the problem's claim under the same hypotheses).** Under the hypotheses of Theorem T, together with the chain's inputs (Teichmüller vertices for the pieces, (O) and (F2), as in step 5 of the chain), Y_t = Y_0 for all t ∈ Δ.

*Proof.* By the chain derivation 1–4 of the task, MS6 with T ⊇ {|t| < ε} gives Y_t ∈ F (a finite set) for |t| < ε. By continuity Y is constant near 0, and by PR-A and the identity theorem, Y_t = Y_0 on Δ.
- Directly: in the MERGE case the witness piece at t is H_t(E_b), where E_b is the piece of b. Its vertex [γc] is non-constant at t = 0 by C2, and L2 pins its puncture values. ∎

**Remark (a reduction of (Lock)).** Lock at R only needs to be proved for some sequence t_n → 0, not for all small t, provided the copies are given by holomorphic functions. Precisely: if a lift curve t ↦ q(t) of R_t can be chosen holomorphic on a small disc, which is the case when R is isolated in B_0 ∩ Δ_{G'}, because then t ↦ R_t is the analytic curve closure(𝒱) ∩ (Δ_{G'} × Δ) locally, then the set {t : C_{q(t),ℓ} ≅ C_{q(t),ℓ'}} is analytic. So it suffices that it has an accumulation point at 0.
- In particular, (Lock) at an isolated point R follows from the PR-I mechanism (Lemma C1 + Lemma D(D2)), whenever near R the only boundary branches are branches of ∂V_t: each such branch forces its own label in Λ(R) to be a Y_t-copy (Theorem 4 of PR-I, condition (Tw1)).
- I state this only as a sketch.

**Remark (what Theorem T removes).** Theorem T needs no tracking of "the" Y-component and no transport of branch identities. Only isomorphism classes are transported, and they are insensitive to automorphisms of R. The only places where twins can still hurt are the finitely many points of (T3), and the IMOV alternative is excluded by (T1).

## 4. Summary: proved / conditional / open

**Proved (modulo the cited standard deformation facts (Def1), (Def2), path lifting, and boundary bumping):**
- **Lemma 1.** At any t, a merge of any Y_t-copy along any boundary branch, or a non-constant move of an intact Y_t-copy along a branch ending at a deeper-stratum point, is a witness for MS6 at t. Twins are irrelevant here: any copy counts.
- **Lemma 2.** N_t is closed, also in families.
- **Lemma 3.** If MS6 fails at t, every copy along every branch is STAY or IMOV (interior move). Without IMOV, N_t is a union of connected components of B_t.
- **Lemma 4** (connected subsets of B_0 are finite unions of arcs) and **Lemma 5** (constant vertices at junctions).
- **L1** of the chain has been checked (in the proof of Lemma 5(i)).

**Conditional theorem.** **Theorem T**: MS6 holds for all t in a neighbourhood of 0, hence (Corollary T′, with the chain's other inputs) Y_t ≡ Y_0, provided:
- (T1) the output of Proposition K is MERGE or puncture-MOV;
- (T2) the pieces met by the arcs of K_0 lie in product-type strata (believed removable);
- (T3) (Lock) holds at the finitely many chain points P, R_1, …, R_{m−1}, Q_0, which is automatic at points with a unique Y_0-copy.

Theorem T depends on Proposition K (PR-H; "modulo routine marking details" there). It uses only the existence of K_0 ⊂ N_0 and of the terminal MERGE/MOV branch, not the tracking.

**Not achieved: MS6 in general.** The task's approach (contradiction at a generic t) reduces, by Lemmas 1–3, to exactly two residual issues. Both are open:
- **(Open-1) IMOV.** At t = 0 (Proposition K's MOV with Q_0 interior to the piece of b), or at a generic t (Lemma 3), a Y-copy may move through an interior point of a piece. L1 and L2 only place Y_t on a fixed curve closure(π_x(E_0)), at a point σ(t) of Ē_0 that is not pinned (Remark 1 of §1). Excluding IMOV, or continuing Proposition K's ray argument past an interior-MOV point to a MERGE or puncture-MOV, is open.
- **(Open-2) Twins / (Lock).** Passing from t to 0 (option 2(a)), or transporting from 0 to t (Theorem T), requires that the merged or moved Y_0-copy at Q_0 and the Y_0-copies at the junction points remain isomorphic to Y_t for t ≠ 0. This is (Lock). It holds when the copies are unique, and in the PR-I quintic configuration, but it is unproved in general. §2 shows precisely how an unlocked twin defeats both directions.
- **Option 2(b)** (a contradiction from time-t data alone) is argued, heuristically, to be impossible (Remark 2 of §1). I did not construct an explicit algebraic surface realizing a fully STAY boundary component, so this is a heuristic rather than a proof.

No counterexample to MS6 was found. A counterexample would need a configuration where the only Y_0-merges or Y_0-moves at t = 0 occur at unlocked twin copies or at interior points.

=== END OF ANSWER round7_q6 ===
