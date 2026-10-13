# round7_q4 — attempt to refute MS6 (answer file)

**Status line (written first, updated at the end).** Plan: (1) test MS6 on the trivial family for the natural examples (Galois covering constructions over M_{0,5} and M_{1,2}); (2) prove a t = 0 criterion that implies MS6 on a neighbourhood of 0 without any Teichmüller or (O) hypothesis; (3) check the chain lemmas L1, L2; (4) isolate the residual loopholes (twins, MOV-interior).

**Final status:**
- No counterexample to MS6 was found.
- MS6 is proved for the trivial family over all Galois covering constructions on M_{0,5} and M_{1,2} (Theorem C).
- A t = 0 merge condition implies MS6 near t = 0 for every admissible family (Theorem A).
- The general case is open. The precise loopholes are listed in §3 and §5.

Readings (R1), (R2) of the task are adopted throughout.

## 1. The trivial family: no counterexample among Galois covering constructions

For the trivial family V_t ≡ V_0, MS6 reads:

**(MS6_0)** There are a piece E (any stratum G, lifted to ∏_w M_w), a vertex u with f_u non-constant on E, and a puncture p of E such that f_u(p) has an irreducible component which, with its special points, is isomorphic to Y_0 as an n_i-pointed curve (in some order).

I prove (MS6_0) for every Galois covering construction over M_{0,5} or M_{1,2}. This covers the cyclic examples of PR-I (quintic, Picard type). Smoothness of V_0 plays no role. So these examples cannot refute MS6 through the trivial family.

### 1.1 Cited facts (from memory)

**(Klein).** Let W → P^1 be a Galois cover with group K ≠ 1 and W ≅ P^1. Then either
- K is cyclic with exactly 2 branch points, both totally ramified; or
- K ∈ {D_k (k ≥ 2), A_4, S_4, A_5} with exactly 3 branch points, of ramification indices (2,2,k), (2,3,3), (2,3,4), (2,3,5).

Consequences:
- (S1) There are at most 3 branch points.
- (S2) A fibre consisting of a single point is totally ramified. This happens only in the cyclic case, which has exactly 2 branch points.
- (S3) In the non-cyclic case |K| ≥ 4, so unramified fibres have ≥ 4 points.

**(Adm) Admissible G-covers** (Harris–Mumford; Abramovich–Corti–Vistoli).
- Let H be a connected component of the Hurwitz space of connected G-covers C → P^1 with labelled branch points b_1, …, b_m, all with nontrivial local monodromy. Let H̄ be the normalization of its compactification by admissible G-covers. Then h : H̄ → M̄_{0,m} (or the relevant M̄_{h,m}) is finite and surjective, H̄ is normal, and h is open.
- Stabilizing the source gives a continuous Φ̄ : H̄ → M̄_g with Φ̄|_H = Φ. So closure(V_0) = Φ̄(H̄) for V_0 = Φ(H).
- A point of H̄ over a stable base curve B is an admissible G-cover C → B. Over each component B_v, the restriction is a G-cover of B_v branched at most over the special points of B_v. At a marked point b_j its local monodromy is conjugate to g_j ≠ 1. Over the nodes it is balanced.
- Along a connected boundary stratum of H̄ the combinatorial type of C → B is constant. As the base degenerates further, the part of the cover over a base component that does not degenerate stays constant. A family of admissible covers over a disc is a flat family of nodal curves; its stable limit is obtained by contracting the unstable rational components of the special fibre.

**Component covers.** Let C|_{B_v} = G ×_K W with W connected. Then W → B_v is a K-Galois cover. Its local monodromy at a point over b_j is an element of K conjugate in G to g_j ≠ 1. Hence **every component of C over B_v is ramified over every marked point of B_v.**

For a component W of C, its **nodal points** are its points over nodes of B. These are the special points of W in C, since the branch points b_j are not marked in M_g.

### 1.2 Lemma B (no tails; the only bridges are over 2-marked components)

**Lemma B.** Let C → B be an admissible G-cover over a stable curve B in M̄_{0,5} or M̄_{1,2}, and let W be a component of C over the base component B_v. Suppose B_v has m marked points and k node branches, and B is not smooth.
1. If W has genus ≥ 1, it has ≥ 1 nodal point, so it is stable as a pointed curve.
2. If W is rational and (m,k) ∈ {(3,1), (1,2), (0,3), (2,2)}, then W has ≥ 3 nodal points (it is stable).
3. If W is rational and (m,k) = (2,1), then W has ≥ 2 nodal points.

Hence C has no rational tails. Its only unstable components are bridges (rational with exactly 2 nodal points), which lie over (2,1)-components. The stable model st(C) is obtained by replacing each bridge by a node. This changes neither the curve nor the number of special points of any other component.

*Proof.*
- C is connected and B has a node, so every component has a nodal point. This gives 1.
- Let W be rational and let s_x be the number of points of W over a node branch x. Each s_x ≥ 1.
- (3,1): W is branched over the 3 marked points. By (S1) it is unramified over the node, and by (S3) the fibre there has |K| ≥ 4 points (K is non-cyclic, having 3 branch points).
- (1,2) with marked point e and nodes n, n′: if s_n + s_{n′} ≤ 2 then s_n = s_{n′} = 1. Both fibres are then totally ramified, and W is also branched over e. That is 3 branch points with total ramification, which contradicts (S2).
- (2,2) (the D_irr component of M̄_{1,2}, nodes n_±): the same argument works, using the two marked points.
- (0,3): there are three distinct node branches, each with s_x ≥ 1.
- (2,1): W is branched at both marked points. If s_n = 1, the node is totally ramified, giving 3 branch points with total ramification, which contradicts (S2). So s_n ≥ 2.
- Bridges cannot be adjacent to each other. A (2,1)-component meets only components over the neighbouring base component, which is of type (3,1), (1,2), (0,3) or (2,2), or of genus 1. So contracting all bridges just replaces each one by a node (possibly a self-node). ∎

**Lemma M (moving components move).** Let c be a 1-dimensional boundary stratum of H̄ (a component of h^{-1}(D)°, D a boundary divisor). Let B_v be the base component that varies along c: the 4-pointed sphere (3,1) for D_ab ⊂ M̄_{0,5}; the 1-pointed elliptic curve for D_0 ⊂ M̄_{1,2}; the (2,2)-sphere for D_irr. Then for every component W over B_v, the isomorphism class of (W, its nodal points) is non-constant along c.

*Proof.*
- By Lemma B, W is stable with its nodal point set S, so Aut(W,S) is finite.
- B_v ≅ W/K. The special points of B_v are the union of the branch values of W → W/K (these include all marked points, by 1.1) and the images of S (the nodes).
- So the class of (W,S) determines (B_v, unordered special points) up to finitely many choices.
- h maps c finitely onto D. So the modulus of B_v (its cross-ratio, or j) is a non-constant continuous function on the connected set c, and it takes infinitely many values. ∎

### 1.3 Theorem C (MS6_0 for covering constructions over M_{0,5})

**Theorem C.** Let V_0 = Φ(H), with H as in (Adm) over M_{0,5} (5 branch points, nontrivial monodromies, G any finite group). Let Δ_Γ be a product-type stratum such that ∂V_0 = closure(V_0) ∩ Δ_Γ has dimension 1 and π_i(∂V_0) = {Y_0}, with dim M_{g_i,n_i} > 0. Then (MS6_0) holds. Explicitly, there are a cusp P_0 ∈ closure(∂V_0) \ ∂V_0 and a piece E′ through P_0 such that the component Y ≅ Y_0 of P_0 coming from ∂V_0 is merged along E′ into a non-constant vertex.

*Proof.*

**Step 1 (where Y_0 lives).**
- closure(V_0) ∩ Δ_Γ is the union of the sets Φ̄(σ) ∩ Δ_Γ over the strata σ of H̄. Each Φ̄(σ) lies in a single stratum of M̄_g, by (Adm) and Lemma B.
- So a 1-dimensional component E_Γ of ∂V_0 contains Φ̄(c°) as a dense subset, for some boundary curve c of H̄ over some D_ab (base A(a,b,n) ∪ B_x(c,d,e,n)).
- Δ_Γ is of product type, so the vertex-i coordinate along Φ̄(c°) is a well-defined non-bridge component of C_x, with its special points. It is constant.
- By Lemma M it is not over B_x. So it is a stable component Y over A, with special points Y ∩ π^{-1}(n). Each of these is a node to a component over B_x, and such components are never bridges by Lemma B.
- So (Y, Y ∩ π^{-1}(n)) ≅ Y_0.

**Step 2 (the cusp).**
- h(c̄) = D_ab ≅ M̄_{0,4} contains the point D_ab ∩ D_cd (base A(a,b,n) — B′(e,n,n′) — C(c,d,n′)). Pick x_0 ∈ c̄ over it.
- By (Adm), C_{x_0} = C_A ∪ C_{B′} ∪ C_C, where C_A is the constant A-part along c. So Y is a component of C_{x_0}.
- P_0 := Φ̄(x_0) ∈ closure(∂V_0). Every point over n′ is a node of st(C_{x_0}) (Lemma B: components over C are never tails, and bridges become nodes). So P_0 has more nodes than the points of Δ_Γ, i.e. P_0 ∉ Δ_Γ.

**Step 3 (the merging piece).**
- h is finite and open at x_0, so h^{-1}(D_cd) contains a branch c′ through x_0. Along c′ \ {x_0}, C_y = C′_{A′_y} ∪ C′_C over A′_y(a,b,e,n′) ∪ C(c,d,n′), and A′_y → A ∪ B′.
- Φ̄(c′ \ {x_0}) lies in one stratum Δ_{G′} and is 1-dimensional (Lemma M). It therefore lies in a piece E′ ⊂ closure(V_0) ∩ Δ_{G′}.
- Lift a branch of Φ̄(c′) at P_0 to ξ_{G′}^{-1}(E′) (on a finite cover of the punctured disc if necessary). Its coordinates are single-valued, and its limit R satisfies ξ̄_{G′}(R) = P_0. This limit is ν(p) for a point p of the normalized closure of a component Ê′ of the lift.
- Let u be the vertex whose component W′_y (a component of C′_{A′_y}) contains Y in the limit. The special points of u are the points of W′_y over n′. These are nodes of st(C_y): a component over C is stable or a bridge, and a bridge becomes a node.
- So R_u = f_u(p) is the stable model of (Z, Z ∩ π^{-1}(n′)), where Z is the connected component of C_A ∪ C_{B′} containing Y.

**Step 4 (Y is a component of the nodal curve f_u(p)).**
- Inside Z, the neighbours of Y are components over B′. They are stable by Lemma B(2), (1,2)-case; this uses only nodal points, and all of them stay special in Z because the n′-points are marked.
- Contracting the bridges among the other A-components does not affect Y or its neighbours.
- So f_u(p) is a nodal curve having Y, with special set Y ∩ π^{-1}(n), as a component. Hence it has a component ≅ Y_0.
- f_u(p) ∈ ∂M̄_u, while f_u(Ê′) ⊂ M_u. So f_u is non-constant, and ν(p) ∉ Ê′, i.e. p is a puncture.

This is (MS6_0). ∎

**Remark.** In the merge, Y is merged along E′ at the cusp P_0 of ∂V_0. This is exactly the (C-merge) property of PR-C, so (C-merge) holds for all these examples. In the quintic example of PR-I, E′ is ∂V_0 itself, entered along its other branch at P_0 (D_12° and D_34° have the same image). Along the branch c, A ≅ Y_0 is the constant vertex and C is merged. Along c′ the roles are swapped. This is the twin mechanism of Proposition 3 of PR-I.

### 1.4 Theorem C for M_{1,2}

**Theorem C (M_{1,2}).** The same statement holds for V_0 = Φ(H), where H is a G-Hurwitz space of covers of genus-1 curves branched at 2 labelled points with nontrivial monodromy.

*Proof.* The boundary of M̄_{1,2} consists of:
- D_0, with base E(n) ∪ R(p_1,p_2,n);
- D_irr, with base P^1(p_1,p_2,n_+,n_−)/(n_+ ∼ n_−);
- the point D_0 ∩ D_irr, with base R(p_1,p_2,n) ∪ N(n,n_+,n_−)/(n_+ ∼ n_−);
- the "banana" point, which is not needed.

Lemma B covers all components:
- E-components have genus ≥ 1;
- R is of type (2,1);
- N is of type (0,3);
- the D_irr component is of type (2,2).

**Step 1 (where Y_0 lives).** Lemma M applies to E-components along D_0 and to the (2,2)-components along D_irr. So, as in Step 1 of Theorem C, ∂V_0 contains Φ̄(c°) for a curve c over D_0. Moreover Y is a stable R-component with special set Y ∩ π^{-1}(n), and its neighbours (E-components) are stable.

**Step 2 (the point x_0).** h(c̄) = D_0 ≅ M̄_{1,1}, so c̄ contains a point x_0 over D_0 ∩ D_irr. There C_{x_0} = C_R ∪ C_N, where C_R is constant along c and contains Y.

**Step 3 (the branch c′).** Take a branch c′ ⊂ h^{-1}(D_irr) at x_0. Let u be the vertex whose component W′ (over P^1_y) contains Y in the limit.
- The special points of W′ are its points over n_±. They are nodes to components over P^1_y, which are stable by Lemma B(2).
- f_u(p) is the stable model of the connected component Z of C_R ∪ C_N containing Y, marked at its points over n_±.

**Step 4 (conclusion).** N-components have ≥ 1 point over each of n, n_+ and n_−, so they are stable. Y is stable, and only R-bridges are contracted. So f_u(p) is nodal and contains (Y, Y ∩ π^{-1}(n)) ≅ Y_0, and u is non-constant. ∎

**Scope.**
- Covering constructions with non-Galois covers, and covering constructions over the primitive totally geodesic surfaces of M_{1,3} (flex and gothic loci; Eskin–McMullen–Mukamel–Wright, cited from memory), are **not** treated here.
- These are the only further natural candidates I know of.

## 2. Theorem A: a t = 0 merge condition implies MS6 near t = 0

This is Theorem P″ of PR-J with clause (b) (Teichmüller) dropped. Clause (b) is not needed for MS6, which only asks for a non-constant vertex. So **no Teichmüller hypothesis and no condition (O) enter**.

**Setting.** As in (T0_β) of PR-J:
- product-type strata Δ_G, Δ_{G′} with Δ_{G′} ⊂ closure(Δ_G);
- P_0 ∈ closure(∂V_0) ∩ Δ_{G′};
- a branch β of ∂V_0 at P_0 (if P_0 ∉ ∂V_0);
- a branch β″ at P_0 of a 1-dimensional component E of closure(V_0) ∩ Δ_G, with P_0 ∉ Δ_G;
- the limit lifts L_β ∈ ∏_{Γ} M̄_w and R_{β″} ∈ ∏_G M̄_w, which are unique by product type;
- the set I′ ⊂ V(G′) of vertices i′ such that κ_Γ(i′) = i for some pattern κ_Γ with glue_{κ_Γ}(P̂_0) = L_β.

**Condition (M_β).** For every i′ ∈ I′ and every pattern κ : G′ → G with glue_κ(P̂_0) = R_{β″}, κ contracts some edge of G′ at i′.

**Theorem A.** Assume (R1), (R2), the hypotheses of the problem and (M_β). Then there is ε > 0 such that MS6 holds at every t with |t| < ε, with the piece E_t := lift of H_t(E), some vertex u and the puncture given by the lifted branch H_t(β″). In particular MS6 holds with T = {|t| < ε}.

*Proof.*

**Step 1 (transport).**
- β_t := H_t(β) and β″_t := H_t(β″) are branches at P_t := H_t(P_0) ∈ Δ_{G′}, of ∂V_t and of E_t respectively. E_t is an irreducible component of closure(V_t) ∩ Δ_G (PR-D, Step 1).
- P̂_t := ξ_{G′}^{-1}(P_t) depends continuously on t, because ξ_{G′} is a homeomorphism (product type).
- Let L^t and R^t be the limit lifts along β_t and β″_t. R^t = ν(p_t) for a puncture p_t of the lifted E_t, since P_t ∉ Δ_G.

**Step 2 (limits).** Suppose MS6 fails, for this configuration, at times t_n → 0.
- By the germ argument of PR-J (Theorem P″, Step 2), every limit point of (L^{t_n}) is L_β, and every limit point of (R^{t_n}) is R_{β″}. I reuse that argument and have not re-derived it.
- There are finitely many patterns. So, after passing to a subsequence, L^{t_n} = glue_{κ_Γ}(P̂_{t_n}) and R^{t_n} = glue_κ(P̂_{t_n}) for fixed patterns κ_Γ and κ.
- Letting n → ∞ gives glue_{κ_Γ}(P̂_0) = L_β and glue_κ(P̂_0) = R_{β″}.

**Step 3 (the Y_t-component).**
- By Lemma D(1) of PR-I, κ_Γ^{-1}(i) = {i′} is a single vertex with no contracted edges or loops. So P̂_{t_n,i′} ≅ Y_{t_n}, and its special points (the half-edges at i′) correspond to those of vertex i of Γ.
- By Step 2, i′ ∈ I′.

**Step 4 (merge).**
- By (M_β), κ contracts an edge at i′. Put u := κ(i′).
- Then R^{t_n}_u = f_u(p_{t_n}) is a nodal curve, obtained by gluing the components P̂_{t_n,x} for x ∈ κ^{-1}(u). One of these components is P̂_{t_n,i′} ≅ Y_{t_n}, with the same special points: half-edges at i′ become nodes or marked points.
- f_u(p_{t_n}) ∈ ∂M̄_u, while f_u maps the lifted E_{t_n} into M_u. So f_u is non-constant.
- This is MS6 at t_n, a contradiction. ∎

**Corollary A′.** Under (M_β), and under the chain's other inputs (L1, L2, (O), (F2), Lemma PA; see the task's §"Derivation"), Y_t = Y_0 for all t.

**Application to Section 1.** Take the configuration of Theorem C:
- β = Φ̄(c) at P_0 = Φ̄(x_0);
- β″ = Φ̄(c′);
- G′, G the strata of P_0 and of Φ̄(c′°).

Suppose G′ and G are of product type. Then (M_β) holds under:

**(NT)** No component of C_{x_0} over C(c,d,n′), with its nodal points, is isomorphic to Y_0.

*Proof.* Let x ∈ I′, so P̂_{0,x} ≅ Y_0. Suppose a valid κ contracts no edge at x. Then R_{β″,κ(x)} = P̂_{0,x} is a smooth value of R_{β″}.

The smooth values of R_{β″} are exactly the C-components:
- every A′-type vertex has a nodal limit, because its limit contains a node over n (bridges become nodes);
- C-type vertices are constant.

This contradicts (NT). ∎

So, for covering constructions over M_{0,5} with G′, G of product type and (NT), MS6 holds on a neighbourhood of 0 for **every** admissible family. The same holds for M_{1,2}; there the analogue of (NT) is vacuous, because along D_irr there are no constant vertices.

When (NT) fails, we are in the twin situation of PR-I (quintic). There Proposition 3 of PR-I shows directly that the twin C_t ≅ Y_t, and C_t is merged along β_t into the genus-4 vertex. So MS6 holds at every t.

## 3. General V_0: what Proposition K gives, and the loopholes

**Proposition 3.1 (trivial family, general V_0).** Assume the conclusions of Proposition K (PR-H), which depends on Lemma PA, Lemma NH and Lemmas G/G′ of PR-F.
- If its output is MERGE, then (MS6_0) holds.
- If its output is MOV with Q_0 a puncture of the piece containing b (that is, Q_0 not in the stratum Δ_{G_b} of b \ {Q_0}), then (MS6_0) holds.

*Proof.*
- **MERGE.** Q_0 ∈ K_0, so the Σ_i-component of Q_0 is intact and isomorphic to Y_0. Its special points are the n_i pinched curves of ∂Σ_i, and ψ(Q_0) = Y_0 as a pointed curve.
  - Let E′ be the piece containing b, in the stratum G_b, and let v be the vertex containing Σ_i.
  - Some curve of ∂Σ_i is unpinched along b and pinched at Q_0. So Q_0 ∉ Δ_{G_b}, and Q_0 gives a puncture p of the lift of E′.
  - f_v(p) is the nodal curve obtained by gluing the components of Q_0 that lie in v. It contains the Σ_i-component.
  - By Lemma C2 (PR-C), v is non-constant.
- **MOV at a puncture.** Along b, ∂Σ_i stays pinched. Upper semicontinuity of the pinched set, together with the smooth limit Y_0, forces the Σ_i-side along b to be a single smooth vertex v. f_v is non-constant along b, and f_v(p) = Y_0 at the puncture p given by Q_0. ∎

**Loophole 1 (MOV-interior).** Suppose Q_0 ∈ Δ_{G_b}, so Q_0 is an interior point of the piece E′ ∋ b.
- Since K_0 is connected and contains P ≠ Q_0, some branch b′ of B at Q_0 carries the constant Y_0-component. It lies in a piece E″ of a stratum G″ that is either equal to G_b (two pieces crossing at Q_0) or less degenerate than G_b (Q_0 a puncture of E″).
- Neither case puts Y_0 into a puncture value of a non-constant vertex at Q_0.
- At time t, by L2/PR-D Step 6, the moving vertex satisfies closure(π_v(E′_t)) = closure(π_v(E′_0)) =: K_v, a fixed curve. So Y_t ∈ K_v for all t, but the point of K_v at which Y_t sits moves.
- So **no finite pinned set comes out of a single MOV-interior configuration.**
- What would pin: two MOV-interior configurations with distinct curves K_v ≠ K_{v′}, both containing the tracked Y_t for all t. Then Y_t ∈ K_v ∩ K_{v′}, which is finite.
- **Corrected statement (MS6′), offered as the weakest natural replacement.** Either MS6 holds, or there are two pairs (E′, v), (E‴, v′) with distinct curves K_v ≠ K_{v′} such that, for t in a set with an accumulation point, Y_t is isomorphic to a value of f_v^t and to a value of f_{v′}^t.
- MS6′ also suffices for the chain: each K is fixed by L2, and their intersection is finite. I cannot prove MS6′ either.

**Loophole 2 (twins / pattern ambiguity).** This is the content of condition (M_β): I′ may contain "accidental" vertices. At t ≠ 0 the tracked Y_t-component may then be the unmerged one of two twins. Section 2 handles this only under (NT) or via the explicit twin argument of PR-I.

**Loophole 3 (STAY networks; PR-H).** Proposition K's Q_0 may be far from closure(∂V_0). Transporting the conclusion to t ≠ 0 then requires tracking the Y-component through constant pieces of the network.

By L1, constant vertices stay constant, with values Z_t. Equality Z_t = Y_t follows from continuity of patterns **only when there is no twin ambiguity at the junction points**. This is the same issue as in Loophole 2, and it is not resolved in general.

**Search for a counterexample: outcome.**
- I found no smooth totally geodesic V_0 for which even (MS6_0) fails.
- All covering constructions over M_{0,5} and M_{1,2} with Galois monodromy satisfy (MS6_0) (Theorem C), and for them the merge happens at a cusp of ∂V_0 itself.
- A counterexample would need a V_0 whose Y_0-network reaches only MOV-interior or ambiguous (twin) configurations. No known totally geodesic surface is of that kind: the known ones are covering constructions and the M_{1,3} flex/gothic loci, and I did not compute boundaries of the latter.
- For this reason, **I did not verify smoothness of any candidate**: no candidate violating MS6 was found.

## 4. Checks of the chain lemmas L1, L2

**L1: correct.** Details I checked:
1. pr_u ≡ Z_0 on 𝓦_0. 𝓦_0 lies in the closure of the lift of E_0, and pr_u is continuous.
2. Small fibres land in U. M_u is quasi-projective, so the point Z_0 has an affine neighbourhood U. Properness of 𝓦 → Δ gives pr_u(𝓦_t) ⊂ U for small |t|.
3. Constancy on small fibres. Holomorphic functions on a compact connected analytic space are constant, so pr_u is constant on each connected component of 𝓦_t for small |t|.
4. Rank argument. The fibres of (pr_u, t) : 𝓦 → M̄_u × Δ have dimension ≥ 1 on the open set {|t| < ε}. 𝓦 is irreducible, and by upper semicontinuity of fibre dimension this holds everywhere.
5. Conclusion for all t. Every 1-dimensional component C of 𝓦_t contains a generic point lying on no other component. The ≥ 1-dimensional fibre through that point lies in 𝓦_t, so it contains C, and pr_u is constant on C.
6. Caveat. MS6 also allows non-product G. Then the lifts and 𝓦 must be built on ∏M_w for the non-product gluing map. Lemma R0 was written for product type; its proof uses only finiteness of ξ_G, so it extends.

**L2: correct modulo its stated inputs.** Those inputs are (H_0), (O), Lemma R*, Imayoshi–Shiga, and extension of holomorphic punctured-disc maps to M̄_u (cited from memory). Details I checked:
1. Infinite monodromy. With finite monodromy, the map lifts on a finite cover to the bounded Bers domain. Riemann extension then makes it bounded holomorphic on a compact surface, hence constant. So g_0 has infinite monodromy.
2. Non-constancy for all t. g_t has the same monodromy as g_0, because A_t is homotopic to the transported marking and f_u^t ∘ Ĥ_t ≃ f_u^0 (PR-D, Step 2). So each g_t is non-constant.
3. Finiteness of puncture values. A_t maps cusps to cusps, and the set of punctures of Ē_0 is fixed. So f_u^t(p) = φ̄_j(A_t^{-1}(p)) ranges over a finite set.
4. One point to note (not a flaw). MS6's "puncture" (ν(p) ∉ E) coincides with the cusps of the uniformized normalization. It is **not** the same as the cusps of the minimal orbifold, so (O) must be assumed for the pieces actually used.

**Chain step 4: correct.** It needs "every piece at time t is the transport of a piece at time 0". This holds by (R2) and PR-D, Step 1: irreducible components of 1-dimensional analytic sets are topologically determined.

## 5. Summary

**Proved here** (modulo the cited classical facts (Klein) and (Adm), marked as cited from memory):
- **Lemma B** (structure of admissible G-covers over M̄_{0,5} and M̄_{1,2}: no tails, bridges only over 2-marked components) and **Lemma M** (components over the moving base component move).
- **Theorem C** (M_{0,5} and M_{1,2}). For every Galois covering construction, (MS6_0) holds, with an explicit merge at a cusp of ∂V_0. So the trivial family over these examples does **not** refute MS6, smooth or not.
- **Theorem A.** The t = 0 merge condition (M_β) implies MS6 on a whole neighbourhood of t = 0, for every admissible family. It needs no Teichmüller or (O) hypothesis, but reuses the germ argument of PR-J (not re-derived).
- **Application of Theorem A** to covering constructions: under product type of G′, G and (NT), MS6 holds near 0 for every admissible family; for M_{1,2}, (NT) is vacuous. The quintic twin case is covered by Proposition 3 of PR-I.
- **Proposition 3.1.** MERGE, or MOV at a puncture, in Proposition K implies (MS6_0).
- **L1, L2 and chain step 4** checked; no flaw found. Caveats are noted in §4.

**Not achieved.**
- No counterexample to MS6 was found.
- MS6 is not proved in general.

**Open.**
1. MOV-interior (Loophole 1). Can a smooth totally geodesic V_0 have a Y_0-network whose only exits are MOV branches through Y_0 at interior points? MS6′ is proposed as a pinnable replacement, but it is unproved.
2. Twin ambiguity (Loophole 2). Condition (M_β) for general V_0, or a replacement such as (NT), is open.
3. Transport of Proposition K's output when Q_0 ∉ closure(∂V_0) (Loophole 3). This needs tracking through junctions without twin ambiguity.
4. Non-Galois covering constructions, and covering constructions over the M_{1,3} flex/gothic loci, were not examined.
5. Theorem A for non-product G, G′ was not written. It needs path-lifting through ∏M_w → Δ_{G′} (quotient by a finite group; Bredon, cited from memory).

=== END OF ANSWER round7_q4 ===

