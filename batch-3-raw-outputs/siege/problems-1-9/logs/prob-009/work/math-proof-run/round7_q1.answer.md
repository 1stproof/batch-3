# round7_q1 — attempt on MS6

**Status / plan (written first).** PARTIAL result. Plan:
(1) check the chain lemmas L1 and L2;
(2) prove a "continuity principle": follow the marked subsurface Σ_i along paths in the *interior* V_t, transported from t = 0 by H. Tracking through coarse boundary points (the twin problem) is replaced by tracking along interior paths;
(3) deduce MS6 for **every** t ∈ Δ in the MERGE case and the MOV-at-a-puncture case of Proposition K, under a hypothesis (P′) on the network pieces (automatic for product-type strata);
(4) isolate exactly what remains open: the "touching" MOV case, and network pieces whose stratum has a symmetry moving a Y_0-carrying vertex.

Readings (R1), (R2) are used throughout, as in the task. "Class" of an n_i-pointed curve means its image in M̄_{g_i,n_i}/S_{n_i}. MS6 allows any order of the special points, so classes are what we need. Fix a metric d on M̄_g and a metric on M̄_{g_i,n_i}/S_{n_i}.

---

## 1. Check of the chain lemmas L1, L2

### 1.1 L1 is correct for product-type strata (proof)

**Lemma L1(prod).** Let Δ_G be of product type, E_0 a piece at time 0 in Δ_G, w a vertex of G, and suppose pr_w is constant on E_0. Then pr_w is constant on E_t := H_t(E_0) for every t ∈ Δ. The same holds with the base time 0 replaced by any t_1. (Use the stratified homeomorphism H ∘ (H_{t_1}^{-1} × id), which satisfies (R2) with base fibre closure(V_{t_1}).) In particular, if pr_w is non-constant on E_{t_1} for one t_1, it is non-constant on E_t for all t.

*Proof.*
1. Let 𝓦 ⊂ ∏_u M̄_u × Δ be the closure of the lift of H(E_0 × Δ). It is analytic and proper over Δ (Lemma R0, Steps 1 and 4). Because ξ_G is bijective on ∏ M_u, its fibre 𝓦_0 lies in the closure of the unique lift of E_0. So pr_w(𝓦_0) is a single point: a constant extends continuously to the closure.
2. Let 𝓦′ be any irreducible component of 𝓦. It has dimension 2 and is not contained in a fibre of t. Put Φ = (pr_w, t) : 𝓦′ → M̄_w × Δ. This map is proper, so by Remmert I := Φ(𝓦′) is an irreducible analytic set.
3. Suppose dim I = 2. The function t restricted to the pure 2-dimensional set I has every nonempty fibre of dimension ≥ 1 (a fibre is the zero set of one function; active lemma / Krull). Its fibre over 0 is nonempty, since 𝓦′ → Δ is surjective (proper, open image). That fibre would be infinite and contained in pr_w(𝓦_0) × {0}, which is a single point. This is a contradiction.
4. So dim I = 1. Since I is irreducible and not contained in a fibre, every fibre I_t is finite. Hence pr_w takes finitely many values on 𝓦′_t, and so on 𝓦_t.
5. The lift of E_t lies in 𝓦_t and is connected. So pr_w is constant on it. ∎

(This is the planner's argument in a slightly cleaner form; no affine open set is needed.)

### 1.2 L1 is NOT proved for non-product strata (flaw in the chain)

For a stratum G with nontrivial Aut(G), the "lifted family" must be the closure 𝓦 of the full preimage ξ_G^{-1}(H(E_0 × Δ)). Its fibre 𝓦_0 contains the translates σẼ_0 (σ ∈ Aut(G)), and pr_w restricted to σẼ_0 equals pr_{σ^{-1}w} restricted to Ẽ_0. The latter can be non-constant. Then Step 3 of the proof fails.

**Local model showing that the step really can fail** (a model of analytic sets, not a full counterexample). Let σ ∈ Aut(G) swap two vertices w, w′ of type (g_i, n_i), with all other coordinates σ-symmetric. Suppose that along E_t the pair of coordinates (π_w, π_{w′}) is, in a local coordinate c on M_{g_i,n_i} and a coordinate x on E, the root set of

  (c − Y_0)(c − Y_0 − f(x)) = t·h(x).

- At t = 0 the roots are Y_0 (constant) and Y_0 + f(x) (non-constant).
- At t ≠ 0 the two roots form one 2-valued function, with square-root branch points near the zeros of f. There the curve has an automorphism swapping the two components, which is allowed because the stratum is not of product type.
- So the labelled lift Ẽ_t is connected, it degenerates to Ẽ_0 ∪ σẼ_0, and the vertex that is constant at t = 0 is non-constant for t ≠ 0.

I see nothing in (R1), (R2) or the local analysis that excludes this. **So L1, and with it step 4 of the chain's derivation, is established only for pieces in product-type strata,** or more generally for vertices w fixed by Aut(G) (Remark 1.3).

L2 inherits the same restriction. In the model above, Ẽ_t is a double cover of E_t ≅ E_0 whose branch points move with t, so Ē_t is not biholomorphic to Ē_0, and Lemma R\*/Imayoshi–Shiga cannot be applied vertex by vertex.

**Remark 1.3 (a harmless generalisation).** Suppose w is fixed by every element of Aut(G). Then for Z ∈ Δ_G the component of Z at w is well defined: pr_w(σR) = pr_w(R). So pr_w is constant on every translate σẼ_0 as soon as it is constant on Ẽ_0, and the proof of 1.1 goes through verbatim. Also, in a product-type stratum Aut(G) acts trivially on ∏ M_u: bijectivity of ξ_G gives R = σR for all R. Hence **no automorphism of a curve Z ∈ Δ_G (product type) can exchange two components lying at vertices with positive-dimensional moduli.** Components at such vertices are canonically labelled by vertices of G. The same holds for a vertex fixed by Aut(G).

### 1.3 L2

For a piece E_0 in a product-type stratum, with a Teichmüller vertex v satisfying (H_0) and (O), I re-checked L2 as written.
- g_t := f_u^t ∘ A_t is homotopic (orbifold sense) to g_0, because A_t ≃ Ĥ_t and f_u^t ∘ Ĥ_t ≃ f_u^0 via H.
- g_0 has infinite monodromy. If it had finite monodromy, then on a finite cover it would lift to the bounded domain T_u, extend over the punctures, and so be constant.
- So every g_t is non-constant. Imayoshi–Shiga finiteness (cited from memory, as in PR-D Step 5) then puts the g_t in a finite set. Their values at the punctures lie in a finite set, because A_t maps cusps to cusps.

I found no further flaw, beyond the non-product restriction of 1.2 and the open inputs (O), (F2) already listed by the chain.

### 1.4 Remark on the role of MS6

Modulo L1, L2 and (O), MS6 is *equivalent* to the problem's conclusion. "⇐": Proposition K gives a MERGE configuration at t = 0, and L2 keeps the merged copy equal to Y_0 = Y_t. So MS6 is not an easier statement. It carries the whole difficulty, which is the twin problem. Section 2 attacks that problem directly.

---

## 2. The continuity principle: tracking Σ_i through the interior

### 2.0 What is used from Proposition K (PR-H §3)

Notation: B_0 = closure(V_0) \ V_0. Σ_i ⊂ S_g is the subsurface of vertex i at a point P ∈ ∂V_0, and ∂Σ_i is its boundary multicurve. For a stable curve Z, a marked smooth surface X close to Z, and a multicurve m, write "m ⊂ N_X(Z)" if, in the marking of X, the curves of m are vanishing curves of Z. This is well defined for X in a versal-chart neighbourhood of Z, up to the local monodromy (twists about vanishing curves and Aut(Z)); that monodromy preserves N_X(Z) as a set. If moreover a subsurface Σ is a complementary region of N_X(Z) containing no other vanishing curve, write "Σ ↔ Z_x", where Z_x is the corresponding component of Z. The component is well defined up to Aut(Z), so its *class* is well defined.

Proposition K's proof (rays g_s X_n with path marking; continua K(δ_k, η_k) → K_0; endpoints Q_k → Q_0 on a branch b) provides the following. I did not re-verify Proposition K; its author lists it as "proved, modulo routine marking details".

**(K\*)** There are a compact connected set K_0 ⊂ B_0, a point P ∈ K_0 ∩ ∂V_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B_0 at Q_0, with the following property. For every ρ > 0 there are a path γ : [0,1] → V_0 with a continuous marking (a lift to T_g) and a point Q′ ∈ b \ {Q_0} with d(Q′, Q_0) < ρ, such that:
- (a) d(γ(0), P) < ρ, and in the marking of γ(0), Σ_i ↔ the vertex-i component of P;
- (b) for every s there is z ∈ K_0 with d(γ(s), z) < ρ, ∂Σ_i ⊂ N_{γ(s)}(z) and Σ_i ↔ a (smooth) component of z of class Y_0; for s = 1 one may take z = Q_0;
- (c) d(γ(1), Q′) < ρ, and either
  - **(MERGE)** some curve of ∂Σ_i is not in N_{γ(1)}(Q′), or
  - **(MOV)** ∂Σ_i ⊂ N_{γ(1)}(Q′) and Σ_i ↔ a component of Q′ of class ≠ Y_0.

(The paths are the ray segments for (δ_k, η_k) with k and then n large. In case (a) of Prop K, γ_e has extremal length δ_k > 0 at the endpoint, so it is not a vanishing curve of Q_k: this is (MERGE). Case (b) gives (MOV).) In the MOV case, Prop K's branch b lies in a piece E of some stratum G_b on which the Σ_i-vertex is non-constant. Call the MOV case **touching** if Q_0 ∈ Δ_{G_b}, i.e. Q_0 is an interior point of E, and **puncture-MOV** otherwise.

**Hypothesis (P′).** K_0 \ Sp is a finite union of open arcs (Sp is the finite set below), each inside a single piece D at time 0 (stratum G_D). Require: for every such D and every vertex w of G_D with π_w ≡ class Y_0 on D, w is fixed by Aut(G_D). This holds automatically if G_D is of product type (Remark 1.3).

**The special set Sp ⊂ K_0.** K_0 is a subcontinuum of the compact 1-dimensional analytic set B_0, which is topologically a finite graph. So K_0 is a finite subgraph after subdivision. Let Sp consist of:
- P and Q_0;
- the endpoints of the arcs;
- the singular points of B_0 lying in K_0;
- the isolated points of the sets B_0 ∩ Δ_G that lie in K_0;
- for each arc in a piece D: the points of K_0 ∩ closure(D) \ D, and the points of D ∩ K_0 at which some *non-constant* vertex u of D has a value of class Y_0. These are finitely many, because f_u : Ē → M̄_u is non-constant, so f_u^{-1}(finite set) is finite.

Sp is finite.

### 2.1 Two local facts

**(Ch) Chart lemma.** Let Z ∈ M̄_g and ε′ > 0. There is a neighbourhood U of Z with the following property. Let X ∈ U ∩ M_g be marked, and let Z′, Z″ ∈ U be such that, in the marking of X, ∂Σ_i ⊂ N_X(Z′) ∩ N_X(Z″), Σ_i ↔ Z′_{x′} and Σ_i ↔ Z″_{x″}. Then the classes of Z′_{x′} and Z″_{x″} are within ε′ of each other in M̄_{g_i,n_i}/S_{n_i}.

*Proof.* Work in a versal chart Def(Z) (smooth; M̄_g = Def(Z)/Aut(Z) locally) and lift X, Z′, Z″ into it. The vanishing curves of Z′ and Z″ are vanishing curves of Z, and collapse maps compose (X → Z′ → Z is isotopic to X → Z). So both Z′_{x′} and Z″_{x″} are deformations, inside Def(Z), of the stable curve Z_Σ obtained by gluing the components of Z that lie in Σ_i. The class of the Σ_i-part depends continuously on the point of the boundary stratum of Def(Z) where ∂Σ_i stays nodal (gluing is continuous). Shrinking U makes both classes ε′/2-close to the class of Z_Σ. ∎

**(Tr) Transport of vanishing data.** Fix t. By uniform continuity of H on the compact set closure(V_0) × {τt : τ ∈ [0,1]}, the following holds for each ε > 0: there is ρ > 0 such that d(X, z) < ρ (X ∈ V_0, z ∈ closure(V_0)) implies d(H_{τt}X, H_{τt}z) < ε for all τ.

Transport the marking of X along τ ↦ H_{τt}(X), a path in the interior. For ε small (charts around the compact set H({τt} × K_0)), the set N_{H_{τt}X}(H_{τt}z) is constant in τ. Indeed, H_{τt}z stays in one stratum by (R2), and near a stratum the vanishing multicurve of nearby marked surfaces is locally constant along continuous paths. Likewise "Σ_i ↔ a single component" persists in τ.

*Proof sketch of the last two claims (standard plumbing).* Near a point of Δ_G, surfaces close to the stratum have exactly the G-vanishing curves short, and these vary continuously along paths. ∎

### 2.2 Theorem A

**Theorem A.** Assume (R1), (R2), the problem's hypotheses, (K\*) and (P′). Then for **every** t ∈ Δ, the component of Q_t := H_t(Q_0) that corresponds to Σ_i (in the marking transported along H_t ∘ γ, for ρ small enough depending on t) has class Y_t.

*Proof.* Fix t.

**Step 1 (the finite set S_t).** Let S_t be the union of two sets:
- for every arc-piece D of K_0 and every vertex w of G_D with π_w ≡ class Y_0 on D_0: the value π_w(D_t). This is a single class, by L1 in the form of 1.1/Remark 1.3, which applies thanks to (P′). Put D_t := H_t(D_0).
- the classes of all components of H_t(z), for z ∈ Sp.

S_t is finite. It contains Y_t: the vertex i of the product-type stratum Δ_Γ is constant ≡ Y_0 on ∂V_0, and ∂V_0 ∩ K_0 contains P. If P is special, Y_t is a component class of H_t(P) = P_t ∈ ∂V_t; otherwise use the arc-piece ∂V_0 with w = i. Let 2ε′ be the minimal distance between distinct elements of S_t, or ε′ = 1 if S_t = {Y_t}.

**Step 2 (choice of ρ).** Cover the compact set K_t := H_t(K_0) by finitely many neighbourhoods U as in (Ch) for this ε′, and let λ be a Lebesgue number. Choose ε < λ/4, small enough also for (Tr), and then ρ by (Tr), with ρ < ε. Take γ, Q′ from (K\*) for this ρ.

**Step 3 (the class function).** For s ∈ [0,1], pick z_s ∈ K_0 as in (K\*)(b), with z_1 = Q_0. Put X_s := H_t(γ(s)), marked by transport, and Z_s := H_t(z_s). Then d(X_s, Z_s) < ε. By (Tr), ∂Σ_i ⊂ N_{X_s}(Z_s) and Σ_i ↔ a single smooth component of Z_s. Let c(s) be its class.

**Step 4 (c(s) ∈ S_t).**
- If z_s ∈ Sp, this holds by definition.
- Otherwise z_s lies on an arc in a piece D. Follow τ ↦ H_{τt}(z_s), which stays in Δ_{G_D}, together with τ ↦ H_{τt}(γ(s)).
  - By (Tr), Σ_i corresponds for every τ to a single component of H_{τt}(z_s).
  - Components at vertices that are Aut(G_D)-fixed are canonically labelled by vertices of G_D (Remark 1.3). At τ = 0 the component is of class Y_0, at a vertex w of D. Since z_s ∉ Sp, w is not a non-constant vertex with value Y_0 at z_s, so π_w ≡ Y_0 on D_0. By (P′), w is Aut(G_D)-fixed. So the label w is canonical at every τ.
  - The correspondence "Σ_i ↔ label w" is locally constant along the continuous path, by working in charts with canonical labels. So at τ = 1, Σ_i ↔ the w-component of Z_s, and c(s) = π_w(D_t) ∈ S_t.

**Step 5 (near-continuity).** Let s, s′ be close enough that d(X_s, X_{s′}) < ε. The marking of X_{s′} is the continuation of that of X_s along the short path. Then X_s, Z_s, Z_{s′} all lie in the ball of radius 3ε < λ around Z_s. That ball lies in one chart U of (Ch), and U also contains X_{s′}. Move the marking from X_{s′} to X_s inside U: the local monodromy preserves the correspondences. By (Ch), d(c(s), c(s′)) < ε′.

**Step 6 (conclusion).**
- c(0) = Y_t. Indeed, by (K\*)(a) and (Tr), Σ_i ↔ the vertex-i component of H_t(z_0) near P_t. This component is labelled canonically in the product-type Δ_Γ (Remark 1.3), or z_0 is special with the same conclusion, and vertex i is constant ≡ Y_t on ∂V_t. Strictly, z_0 can be any point near P. By Step 4 applied with D = ∂V_0 (or z_0 special), c(0) is the vertex-i value Y_t.
- The values c(s) lie in the finite set S_t, and values at nearby parameters differ by less than ε′, which is at most half the gap. Covering [0,1] by finitely many short intervals, c is constant.
- Hence c(1) = Y_t. And c(1) is the class of the component of Q_t = Z_1 corresponding to Σ_i. ∎

**Why twins do no harm here.** Suppose a point of K_t carries several components of class near Y_0 (twins at t = 0 that separate at t ≠ 0). The class c(s) is still determined by the *specific interior path* H_t ∘ γ, and it can change only continuously. A swap at a junction would have to be a jump between two distinct elements of the finite set S_t, which near-continuity forbids. (Loops in V_0 whose monodromy exchanges twins are transported by H to loops with the same monodromy. At time t that monodromy is realised by an automorphism of the transported boundary point, so the twins there stay isomorphic. This is consistent with the above.)

---

## 3. MS6 in the MERGE and puncture-MOV cases

**Theorem B.** Assume (R1), (R2), the problem's hypotheses, (K\*) and (P′).
- (i) If (K\*) holds in the MERGE case, MS6 holds with T = Δ.
- (ii) If it holds in the puncture-MOV case, and the Σ_i-vertex v of b's piece is Aut(G_b)-fixed (e.g. G_b of product type), MS6 holds with T = Δ.

*Proof.* Fix t and take ρ, γ, Q′ as in the proof of Theorem A. Put b_t := H_t(b), a branch of B_t at Q_t lying in the stratum G_b of b, by (R2). Put Q′_t := H_t(Q′) ∈ b_t. Let E be the piece at time t through b_t: a component of ξ_{G_b}^{-1}(closure(V_t) ∩ Δ_{G_b}) containing a lift of b_t \ {Q_t}, with Q_t ∉ Δ_{G_b} in both cases below. Let p be the puncture of E given by the end of b_t at Q_t.

By Theorem A, the component y of Q_t with Σ_i ↔ y (marking of X_1 = H_t γ(1)) has class Y_t. By (Tr) applied to Q′ and to Q_0 (both within ε of γ(1)), the time-0 relations of (K\*)(c) hold at time t for Q′_t and Q_t.

(i) **MERGE.** Some γ_e ⊂ ∂Σ_i is a vanishing curve of Q_t but not of Q′_t ∈ b_t. Hence Q_t ∉ Δ_{G_b}, so p is a genuine puncture.
- Let v be the vertex of G_b (in the lift E) whose region contains Σ_i ∪ γ_e.
- The limit f_v(p) is the curve obtained by gluing the components of Q_t that lie in the region of v. That set of components includes y and the node γ_e, so f_v(p) is nodal and has y, of class Y_t, as an irreducible component.
- By Lemma C2 (PR-C), applied at time t (its proof uses nothing about time 0), f_v is non-constant: a constant vertex has a smooth limit.
- This is exactly the configuration of MS6.

(ii) **Puncture-MOV.** Now ∂Σ_i stays nodal along b_t and Σ_i ↔ the v-component of Q′_t. Since Q_0 ∉ Δ_{G_b}, p is a puncture.
- The limit f_v(p) is the glue of the components of Q_t inside Σ_i. That is only y, because Σ_i ↔ the single component y of Q_t. So f_v(p) = y has class Y_t.
- f_v is non-constant at time 0: (MOV) says the Σ_i-component along b takes values of class ≠ Y_0 while its limit is Y_0.
- By L1 based at t (1.1/Remark 1.3; this is where Aut(G_b)-fixedness of v is used), f_v is non-constant on E for every t.
- So MS6 holds at t. ∎

**Corollary (problem's claim in these cases, modulo the chain).** In case (i), suppose b's piece E_0 lies in a product-type stratum, carries a Teichmüller vertex (Lemma PA + Lemma T′, i.e. (F2)), and satisfies (O). Then L2 puts f_v^t(p) in a finite set, so Y_t lies in a finite set for all t. Hence Y_t ≡ Y_0, by PR-A and the identity theorem. The same holds in case (ii).

---

## 4. What remains open

**(Open-1) The touching MOV case.** Here Q_0 ∈ Δ_{G_b}, i.e. Q_0 is an interior point of the piece E_0 ⊃ b, and the Σ_i-vertex v moves along E_0 with π_v(Q_0) = Y_0.
- Theorem A still gives π_v(Q_t) ≅ Y_t, with v non-constant on E_t (by L1).
- But Q_t is not a puncture, so MS6 is not obtained, and L2 gives no finiteness at interior points.
- K_0 reaches Q_0 through other branches, along which Σ_i is constant. Their pieces have Q_t as a puncture with smooth constant limit Y_t at the Σ_i-vertex. That is a constant vertex, so it does not count for MS6.
- To close this case one needs either a version of Proposition K whose MOV branch ends at a puncture, or an argument excluding touching for totally geodesic V_0. I have neither.

**(Open-2) Network pieces violating (P′).** These are arcs of K_0 in a stratum G_D with an automorphism moving a vertex that carries a constant Y_0-copy.
- There L1 can fail: see the local model in 1.2. The class of the Σ_i-component along D_t can then drift continuously, so S_t is not finite.
- Excluding the model of 1.2 for pieces of closure(V_t) is the missing input.
- If g_i ≥ 1, passing to a level-N cover does not help. The swapping automorphism of the curve at a branch point makes the level cover ramified there too, and the same degeneration occurs.

**(Open-3)** (K\*) itself rests on Proposition K (PR-H), which is "proved modulo routine marking details", on Lemma NH (needs Lemma PA) and on Lemma G/G′. In Section 2 I did not re-verify these; I only checked that (K\*) is what its proof produces. Theorem A, the Chart lemma and (Tr) are written at the level of standard plumbing / versal-chart facts, which I state but do not re-derive.

---

## 5. Summary

**Proved (modulo cited standard facts: versal deformation charts, plumbing, Remmert, active lemma):**
- L1 for vertices that are fixed by Aut(G), in particular all vertices of product-type strata (1.1, 1.3). In product-type strata, components at positive-dimensional vertices are canonically labelled; no automorphism exchanges them (1.3).
- Theorem A (continuity principle). Under (K\*) and (P′), for every t the Σ_i-component of Q_t, tracked along interior paths transported by H, is ≅ Y_t. This resolves the twin problem for the network.
- Theorem B. MS6 holds with T = Δ in the MERGE case of Proposition K. It also holds in the puncture-MOV case when the moving vertex is Aut-fixed. Each case assumes (K\*) and (P′).

**Flaw found in the chain:** L1 (and hence L2 and step 4 of the derivation) is unproved for pieces in non-product strata whose automorphisms move the vertex concerned. A local model (1.2) shows that the planner's proof genuinely breaks there. For product-type strata L1 is correct, and L2 is correct modulo (O) and the citations.

**Partial (not a proof of MS6 as stated):** MS6 is NOT proved in general. The remaining cases are exactly:
- (Open-1) the touching MOV endpoint of Proposition K;
- (Open-2) network arcs in strata with a symmetry moving a constant Y_0-carrying vertex, i.e. failure of (P′);
- (Open-3) the inherited dependence on Proposition K, Lemma NH and (F2).

No counterexample to MS6 was found.

=== END OF ANSWER round7_q1 ===
