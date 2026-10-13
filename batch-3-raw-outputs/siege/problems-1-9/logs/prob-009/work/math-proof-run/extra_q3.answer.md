# Part III — A self-contained proof of Theorem B (the Φ-chain)

**Status.** This part proves Theorem B (stated in §0.10). Inputs taken as given: the black boxes BB1–BB6 in the precise forms stated in §1, and the classical facts listed at the end. Every other step is proved here. That includes Lemmas 1–3, Proposition 4, Lemma 5, the Φ-version of the generic-time dichotomy (Proposition 3.1), the lift-curve facts (I1)–(I3), the induction along the walk chain, and the endpoint. Exactly one point is not established: the marking identification x_m ↔ c ↔ x_{m+1} along travel intervals. It is used in one precise form (BB1-M, §1). That form is my reading of BB1's phrase "the chart labels correspond to c at both ends". Insofar as BB1 says less than BB1-M, the difference is recorded as **GAP-M**. (Rig) and (NRT_P) are hypotheses of Theorem B, and neither is proved here. (Rig) enters only through BB3. The problem itself remains open in this document: it reduces exactly to (Rig) together with (NRT_P).

*Structure:*
- §0: conventions and statement;
- §1: black boxes in the form used;
- §2: preliminary lemmas ((I1)–(I3); sheets map into one component W);
- §3: the Φ-dichotomy;
- §4: Lemmas 1–3 and Proposition 4;
- §5: Lemma 5;
- §6: proof of Theorem B and the isotropy drop;
- then the cited facts and the GAPs.

---

## 0. Conventions, definitions, statement

**0.1 Setting and readings.** g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric. 𝒱 ⊂ M_g × Δ is the family of the problem, V_t its fibres. The hypotheses (i), (ii) and "smoothly trivial" are read as follows.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set. Its fibre over t is closure(V_t) (closures in M̄_g).
- **(R2)** There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ, i.e. H(z,t) = (H_t(z), t). It is smooth on V_0 × Δ, and H_0 = id. For every stratum Δ_G (including the open stratum M_g), H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ).

  This is the *coarse* reading: H_t need not preserve automorphism groups of points.

Δ_Γ is a boundary stratum of *product type*: the gluing map ξ_Γ : ∏_{w∈V(Γ)} M_w → Δ_Γ is bijective on coarse spaces. Here M_w = M_{g_w,n_w}, with the half-edges at w as the marked points. So Δ_Γ ≅ ∏_j M_{g_j,n_j}, and π_i = pr_i ∘ ξ_Γ^{-1}. We put ∂V_t := closure(V_t) ∩ Δ_Γ and assume dim ∂V_t = 1 and π_i(∂V_t) = {Y_t} for all t, with dim M_{g_i,n_i} > 0.

**0.2 Notation.**
- B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g.
- By (R2), H_t(B_0) = B_t, and H_t maps closure(V_0) ∩ Δ_G onto closure(V_t) ∩ Δ_G for every stratum.
- 𝔐 := M_{g_i,n_i}/S_{n_i}, a normal complex space. For an n_i-pointed curve Z of genus g_i, [Z] ∈ 𝔐 is its class with the marked points unordered.
- A *component of type (g_i,n_i)* of a nodal curve is an irreducible component whose normalisation has genus g_i and carries n_i special points (preimages of nodes and marked points).
- Y : Δ → M_{g_i,n_i} denotes t ↦ Y_t. Since M_{g_i,n_i} → 𝔐 has finite fibres and Δ is connected, Y is constant iff [Y] is constant.
- *Germs.* "Germ" always means a germ of a complex-analytic set. Inclusions and equalities of germs are inclusions and equalities of germs.

**0.3 Charts (classical; see facts K1–K5 at the end).** For Q ∈ M̄_g, Def(Q) is the base of the Kuranishi family of the stable curve C_Q. B ⊂ Def(Q) is a small Aut(Q)-invariant ball centred at the point 0 representing C_Q. The map q : B → M̄_g is the quotient by Aut(Q) onto an open neighbourhood q(B) of Q.
- For every edge e of the dual graph G_Q there is a plumbing coordinate s_e on B. For p ∈ B, the nodes of the fibre C_p correspond bijectively to the edges e with s_e(p) = 0.
- The *labels* are the vertices of G_Q.
- A label y is *intact at p* if s_e(p) = 0 for every edge e at y. Then C_p has a distinguished irreducible component deforming the component y of C_Q; with its special points, this is F_y(p).
- Put L_y := {p : y intact at p}. Then p ↦ F_y(p) is holomorphic on L_y (fact PN below), with values in M_{g_y,n_y} for a chosen ordering of the half-edges at y.
- The *pattern* at p is S(p) := {e : s_e(p) = 0}.
- An element a ∈ Aut(Q) acts on B, on the labels and on the edges.

**0.4 Pieces, lifted families, (Rig).**
- A *lifted piece at time t* in a stratum Δ_G is a 1-dimensional irreducible component E of the analytic set ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w. Its image ξ_G(E) is a *piece* (at time t).
- M(E) is the set of vertices w for which pr_w is non-constant on E. K(E) is the closure of pr_{M(E)}(E) in ∏_{u∈M(E)} M̄_u.
- **(Rig)** There is a finite set 𝒦 of triples (G, M, K) with the following properties:
  - M ⊂ V(G);
  - K ⊂ ∏_{u∈M} M̄_u is an irreducible closed curve not contained in the boundary;
  - for every t and every lifted piece E at time t in Δ_G, the triple (G, M(E), K(E)) lies in 𝒦 up to the action of Aut(G).
- The *lifted family* 𝒲_G is the closure in ∏_w M̄_w × Δ_* of (ξ_G × id)^{-1}(closure(𝒱) ∩ (Δ_G × Δ_*)). Here Δ_* ⊂ Δ is the disc fixed in 0.6.
- For a 2-dimensional irreducible component W of 𝒲_G, write W_t for its fibre over t, and M_W, K_W, F_W for the data of BB3 (§1).

**0.5 Remark (dimensions).** dim B_0 ≤ 1. Indeed, B_0 is an analytic subset of the 2-dimensional analytic set closure(V_0). Every point of B_0 is a limit of points of V_0, so B_0 contains no 2-dimensional component of closure(V_0).

By (R2), closure(𝒱) ∩ (∂M̄_g × Δ) = H(B_0 × Δ). This set has topological dimension ≤ 4, so as an analytic set it has dimension ≤ 2. Since ξ_G is finite, 𝒲_G^∘ := 𝒲_G ∩ (∏M_w × Δ_*) = (ξ_G × id)^{-1}(closure 𝒱 ∩ (Δ_G × Δ_*)) has dimension ≤ 2. (𝒲_G^∘ is closed in ∏M_w × Δ_*, being the preimage of a set closed in Δ_G × Δ_*.)

Let C be an irreducible component of 𝒲_G. Pick x ∈ C on no other component, and a neighbourhood U of x with 𝒲_G ∩ U = C ∩ U. Since x lies in the closure of 𝒲_G^∘, C ∩ U meets 𝒲_G^∘. So C ∩ (∏M_w × Δ_*) is a non-empty open subset of C. It is contained in 𝒲_G^∘, hence dim C ≤ 2.

**0.6 The disc Δ_*, the finite set 𝔉, the value curves, and Φ.**
- Fix a closed disc Δ̄_* ⊂ Δ centred at 0, with interior Δ_*. All lifted families are taken over Δ_*.
- 𝒲_G is proper over Δ_* (BB3). Each 2-dimensional component W surjects onto Δ_* (BB3: every fibre W_t is non-empty). Components are locally finite, and all of them meet the compact set 𝒲_G ∩ {t = 0}. Hence there are only finitely many components, and there are finitely many stable graphs G of genus g. So **the set 𝒲 of all 2-dimensional components W of all 𝒲_G is finite.**
- For W ∈ 𝒲, let 𝔉_W ⊂ 𝔐 be the set of classes of components of type (g_i,n_i), with their special points, of the coordinates κ[w] (w ∈ M_W) of points κ ∈ F_W. A coordinate that is a smooth curve counts as its own unique component. 𝔉_W is finite because F_W is finite (BB3). Put 𝔉 := ⋃_{W∈𝒲} 𝔉_W, a finite set.
- For W ∈ 𝒲 and a vertex u ∉ M_W of type (g_i,n_i), let Γ̄_{W,u} ⊂ 𝔐 × Δ_* be the image of Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ_* under M_u × Δ_* → 𝔐 × Δ_*.
  - Γ_{W,u} is an irreducible closed curve, finite over Δ_* (BB3; it is closed by Remmert, since (pr_u,t) is proper on W).
  - M_u → 𝔐 is finite, so Γ̄_{W,u} is again an irreducible closed analytic curve, finite over Δ_*.
  - Put Γ̄_all := ⋃_{W,u} Γ̄_{W,u}, a finite union of closed curves.
- **Definition (Φ).** Φ is the set of irreducible germs φ at (Y_0, 0) ∈ 𝔐 × Δ_* that are local branches at (Y_0,0) of some Γ̄_{W,u} (W ∈ 𝒲, u ∉ M_W of type (g_i,n_i)) and are *non-constant*, i.e. φ ≠ germ of {Y_0} × Δ_*. Φ is finite.
- A branch φ may be a Puiseux branch of degree > 1 over Δ_*. So "the value of φ over t" is the finite set φ_t := φ̂ ∩ (𝔐 × {t}), where φ̂ is a fixed small closed representative. All statements involving φ_t are statements about this set (repair (R-ii)).

**0.7 Transport families, anchored sheets, lift-curves.** Let Q ∈ B_0, with chart q : B → q(B), and let c be a local branch of B_0 at Q, i.e. an irreducible component of the germ of B_0 at Q.
- Since B_0 is a curve, after shrinking B we may represent c by a closed subset of q(B) that is homeomorphic to a closed disc with centre Q. After a further shrinking, c ∖ Q lies in a single stratum Δ_{G_c}. Reason: each stratum meets c ∖ Q in a locally closed analytic subset, and c ∖ Q is a connected punctured disc, so only the stratum containing the generic points of c meets c ∖ Q near Q. Possibly G_c = G_Q; then c ⊂ Δ_{G_Q} near Q.
- Choose ε > 0 with H(c × Δ̄_ε) ⊂ q(B) × Δ_ε. Put N_c := H((c° ∖ Q) × Δ_ε), where c° is the interior of the disc c. N_c is homeomorphic to a punctured disc times a disc, hence connected.
- A *lifted branch* (lift) c̃ of c is an irreducible component at 0 of the germ q^{-1}(c). Its pattern S(c̃) := {e : s_e ≡ 0 on c̃}. After shrinking B, s_e ≠ 0 on c̃ ∖ 0 for e ∉ S(c̃), so S(p) = S(c̃) on c̃ ∖ 0.
- The **transport family** Ñ_c̃ is the connected component, containing (c̃ ∖ 0) × {0}, of (q × id)^{-1}(N_c) ⊂ B × Δ_ε.
- An **anchored sheet** of c̃ is an irreducible component T of the germ at (0,0) of closure(Ñ_c̃) (closure in B × Δ_ε) with c̃ × {0} ⊂ T. Anchored sheets exist: the irreducible germ c̃ × {0} lies in the germ of closure(Ñ_c̃), hence in one of its components.
- c̃ (and any anchored sheet of c̃) is **of boundary type** if Q ∉ Δ_{G_c}. Q is a **puncture point** if it has a branch c of boundary type, i.e. a branch with c ∖ Q in a stratum other than Δ_{G_Q}. Being of boundary type depends only on the coarse branch c, not on the lift.
- Put Q_t := H_t(Q), 𝒬 := {(Q_t, t) : t ∈ Δ_ε}, and the *lift locus* Λ := (q × id)^{-1}(𝒬) ⊂ B × Δ_ε.
- A **lift-curve** is an irreducible component of the germ of Λ at (0,0). (§2 shows that, at a puncture point, Λ is analytic near (0,0) and that its germ is a finite union of curve germs.)

**0.8 Persistence.** Let T be an irreducible 2-dimensional germ at (0,0) in B × Δ_ε, L an irreducible curve germ at (0,0), and z a label. For a germ X on which z is intact, write v_z : X → 𝔐 × Δ_ε, (p,t) ↦ ([F_z(p)], t).
- z is **Y-persistent** on T if z is intact on T (T ⊂ L_z × Δ_ε) and [F_z(p)] = [Y_t] for all (p,t) in a representative of T.
- z is **Φ-persistent on T with function φ** (φ ∈ Φ) if z is intact on T and the image germ v_z(T) is contained in φ. Then P_Φ(T) := the set of labels Φ-persistent on T with some φ ∈ Φ. The function is unique: if v_z(T) ⊂ φ ∩ φ′, then since t|_T is non-constant (Lemma 2.1(c)), v_z(T) is a 1-dimensional germ in both irreducible 1-dimensional germs, so φ = v_z(T) = φ′.
- For a lift-curve L (on which every label is intact, Lemma 2.3(c)): C_Φ(L) := the set of labels z for which the image germ v_z(L) is a branch in Φ.
- z is a **rigid Y_0-copy along L** if v_z(L) is the germ of {Y_0} × Δ_ε.
- **Y ∈ Φ** means: the germ of the graph of [Y] at (Y_0,0) belongs to Φ (proved in Lemma 2.7, assuming Y non-constant).

**0.9 Statement (NRT_P).** *Setting:* that of 0.1, together with (R1), (R2), (Rig), and "t ↦ Y_t is non-constant". *Claim:* there do not exist a puncture point Q ∈ B_0, an automorphism a ∈ Aut(Q), a lift-curve L at Q and a label x of G_Q such that
- x ∈ C_Φ(L), and
- a^{-1}x is a rigid Y_0-copy along L.

In words: along L, for all small t ≠ 0, the component x is intact with class on a branch φ ∈ Φ, while the component a^{-1}x is intact with class ≡ Y_0. (Necessarily a^{-1}x ≠ x: a label cannot be both.)

**0.10 Theorem B.** *Assume the setting of 0.1 with (R1), (R2), Δ_Γ of product type, dim M_{g_i,n_i} > 0, (Rig) and (NRT_P). Then Y_t = Y_0 for all t ∈ Δ.* Moreover:
- (NRT_P) is implied by the problem's conclusion, and a counterexample to (NRT_P) is a counterexample to the problem;
- any configuration violating (NRT_P) forces an isotropy drop |Aut(Q_t)| < |Aut(Q)| for small t ≠ 0.

---

## 1. The black boxes, in the form used

**BB1 (walk chain; t = 0 geometry of V_0).** Assume Y non-constant (this is the situation in which BB1 is invoked). There are the following data:
- pieces D^1, …, D^k at t = 0 (k ≥ 1), with D^1 ⊂ ∂V_0 (so G(D^1) = Γ);
- points J_1, …, J_{k−1} ∈ B_0 with J_m ∈ closure(D^m) ∩ closure(D^{m+1});
- an endpoint Q_0 ∈ closure(D^k) ∩ B_0.

For uniform notation put J_k := Q_0.

*At each J_m (1 ≤ m ≤ k), in the chart Def(J_m):*
- an *entering lift* β̃_m of a branch β_m of closure(D^m) at J_m;
- a label x_m of G_{J_m}, the *common chart label*.

*At each J_m with m ≤ k − 1, in addition:*
- a *leaving lift* β̃′_m of a branch β′_m of closure(D^{m+1}) at J_m.

*At J_k = Q_0, in addition:*
- a *terminal lift* b̃ of a branch b of B_0 at Q_0, belonging to a piece E_b;
- (MERGE or MOV) at t = 0: either some edge at x_k is not in S(b̃) (MERGE), or x_k is intact along b̃ and [F_{x_k}] is not identically [Y_0] on b̃ ∩ B (MOV).
- Here b̃ ∩ B is irreducible: B is a Milnor ball for b̃, so the normalisation of b̃ ∩ B is a disc.

*(IMOV_all) and (P):*
- If J_m (m ≤ k−1) lies in Δ_{G(D^m)} or in Δ_{G(D^{m+1})}, then β̃′_m = β̃_m (same label x_m).
- If J_m lies in neither stratum, it is a puncture of both adjacent pieces. In particular J_m is a puncture point, and β̃_m, β̃′_m are of boundary type.
- (P) at the endpoint: Q_0 ∉ Δ_{G(D^k)} and Q_0 ∉ Δ_{G(E_b)}. So β̃_k and b̃ are of boundary type, and Q_0 is a puncture point.

*(BB1-M) marking identification, in the precise form used.* For each m = 1, …, k (the travel interval along D^m that ends at J_m), there are:
- a lifted piece E^m ⊂ ∏_{w∈V(G(D^m))} M_w over D^m;
- a vertex c_m of G(D^m) that is constant on E^m with value of class [Y_0];
- for m ≥ 2, a graph isomorphism ι′_{m−1} : G_{S(β̃′_{m−1})} → G(D^m) such that ι′_{m−1}∘Π_{S(β̃′_{m−1})} maps β̃′_{m−1} ∖ 0 into E^m;
- a graph isomorphism ι_m : G_{S(β̃_m)} → G(D^m) such that ι_m∘Π_{S(β̃_m)} maps β̃_m ∖ 0 into E^m.

These satisfy:
- x_m is intact along β̃_m, and ι_m({x_m}) = c_m;
- for m ≥ 2: whenever x_{m−1} is intact along β̃′_{m−1}, ι′_{m−1}({x_{m−1}}) = c_m;
- for m = 1: c_1 = i (the tracked vertex on ∂V_0 is the vertex i of Γ).

Here G_S is G_{J} with the edges outside S contracted, and Π_S is the partial normalisation map of fact PN. "{x}" denotes the vertex of G_S consisting of x alone, which is a vertex exactly when x is intact along the lift.

*Comment.* BB1 says: "along each travel interval the tracked label is a constant vertex c of the piece with value ≅ Y_0, and the chart labels correspond to c at both ends (marking identification x_m ↔ c ↔ x_{m+1})". BB1-M is my precise reading of that sentence. The content I read into it is this: **the same** lifted piece E^m serves at both ends of the travel interval, and the correspondences are taken with respect to identifications under which both end-lifts land in E^m. See GAP-M at the end.

**BB2 (holomorphy).** Under (R1), (R2), t ↦ Y_t ∈ M_{g_i,n_i} is holomorphic.

**BB3 (Lemma U, under (Rig)), form used.**
- 𝒲_G is a closed analytic subset of ∏_w M̄_w × Δ_*, proper over Δ_*.
- For each 2-dimensional irreducible component W of 𝒲_G there are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, such that for every t and every 1-dimensional irreducible component D of W_t:
  - D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u;
  - each u ∈ M_W is non-constant on D, and each u ∉ M_W is constant on D. (U1)
- Every fibre W_t is non-empty and is a finite union of such curves D.
- F_W := K_W ∩ ∂(∏_{u∈M_W} M̄_u) is finite and does not depend on t.
- For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ_* is an irreducible curve, finite over Δ_*. Its fibre over t is the set of values c_D[u] for the components D of W_t.

Consequence: t is non-constant on W, since otherwise a fibre would be 2-dimensional. So every W_t is of pure dimension 1 (Krull), and every point of W_t lies on some component K_W × {c_D}.

**BB4 (Theorem 1, generic-time trichotomy for Y).** Not used as a black box. Its Φ-analogue, in the only case needed here (punctures), is proved in full in §3, by running its argument with Y replaced by φ ∈ Φ.

**BB5.** Not used.

**BB6 (transport families), form used.** For every Q ∈ B_0 and every lift c̃ as in 0.7, closure(Ñ_c̃) is, near (0,0), a closed analytic subset of B × Δ_ε of pure dimension 2. The remaining items of BB6 (Lemma B1♭, the base step, the product-type junction and endpoint) are not used; the base step is reproved in Lemma 6.1.

---

## 2. Preliminary lemmas: transport families, lift-curves, equivariance

Throughout §§2–5, Q ∈ B_0 has chart q : B → q(B), c is a branch of B_0 at Q, c̃ is a lift of c, S := S(c̃), Ñ := Ñ_c̃, and ε is as in 0.7. The data B and ε may be shrunk finitely many times; all statements are about germs at (0,0), or hold for small enough representatives. Z_S := {p ∈ B : s_e(p) = 0 for all e ∈ S}, and Z_S^∘ := {p : S(p) = S}.

**Lemma 2.1 (transport families).**
- (a) For every (p,t) ∈ Ñ: S(p) = S, and q(p) ∈ H_t(c° ∖ Q) ⊂ closure(V_t) ∩ Δ_{G_c}.
- (b) (q × id)(Ñ) = N_c.
- (c) Near (0,0): closure(Ñ) ⊂ Ñ ∪ Λ; closure(Ñ) ⊂ Z_S × Δ_ε; and closure(Ñ) ∩ {t = 0} ⊂ q^{-1}(c) × {0}, which has dimension ≤ 1.
- (d) Near (0,0), for every t_0 ≠ 0, closure(Ñ) ∩ {t = t_0} has dimension ≤ 1.

  Consequently, if T̂ is a small representative of a 2-dimensional germ in closure(Ñ) at (0,0), then t − t_0 vanishes identically on no local irreducible component of T̂ at any of its points. Hence every slice T̂_{t_0} := T̂ ∩ {t = t_0} has pure dimension 1 wherever it is non-empty.

*Proof.*
- (a) q(p) ∈ H_t(c° ∖ Q) by definition of N_c. Since c° ∖ Q ⊂ closure(V_0) ∩ Δ_{G_c}, (R2) gives H_t(c° ∖ Q) ⊂ closure(V_t) ∩ Δ_{G_c}. So C_p has exactly |E(G_c)| nodes, i.e. |S(p)| = |E(G_c)| (fact K2). If s_e(p) ≠ 0, then s_e ≠ 0 near p. So S(p′) ⊂ S(p) for p′ near p, and on Ñ equality of cardinalities gives S(p′) = S(p). Thus S(·) is locally constant on the connected set Ñ. At points of (c̃ ∖ 0) × {0} it equals S (0.7).
- (b) (q × id) : B × Δ_ε → q(B) × Δ_ε is the orbit map of the finite group Aut(Q). Paths in the orbit space lift to paths starting at any preimage of the initial point (fact T1).
  - Let n ∈ N_c, and pick (p_0, 0) ∈ (c̃ ∖ 0) × {0} ⊂ Ñ. N_c is path connected, so there is a path in N_c from q(p_0) to n. Its lift starting at (p_0, 0) stays in (q × id)^{-1}(N_c) and is connected, so it lies in Ñ. Hence n ∈ (q × id)(Ñ).
  - The reverse inclusion holds by definition.
- (c) Let (p,t) ∈ closure(Ñ) be close to (0,0).
  - Then (q(p), t) lies in the closure of N_c, which is contained in H(c × Δ_ε) because c is closed and H is a homeomorphism onto the closed set closure(𝒱). So (q(p), t) = H(z, t) with z ∈ c, and z is close to Q because H is a homeomorphism with H_0 = id.
  - If z ≠ Q, then (q(p), t) ∈ N_c, so (p,t) lies in (q × id)^{-1}(N_c) and in the closure of its connected component Ñ. Connected components are closed in the space, so (p,t) ∈ Ñ.
  - If z = Q, then q(p) = Q_t, i.e. (p,t) ∈ Λ.
  - The inclusion closure(Ñ) ⊂ Z_S × Δ_ε follows from (a), since Z_S is closed.
  - At t = 0, (q(p), 0) = H(z, 0) = (z, 0) with z ∈ c, so p ∈ q^{-1}(c). The set q^{-1}(c) is a curve, because q is finite.
- (d) By (c) and (a), closure(Ñ) ∩ {t = t_0} ⊂ q^{-1}(H_{t_0}(c)) ∪ Λ_{t_0}.
  - H_{t_0}(c) is contained in the curve B_{t_0}, so q^{-1}(H_{t_0}(c)) has dimension ≤ 1.
  - Λ_{t_0} ⊂ q^{-1}(Q_{t_0}) is finite.

  For the consequence: a local component on which t ≡ t_0 would be a 2-dimensional subset of a slice of dimension ≤ 1, which is impossible. Krull's principal ideal theorem then gives pure dimension 1 for the slices. ∎

**Lemma 2.2 (Σ_c, 𝒬 and Λ are analytic at a puncture point).** Assume c is of boundary type (Q ∉ Δ_{G_c}).
- (a) Near (Q,0), Σ := (q × id)(closure(Ñ)) is a closed analytic set, equal to H(c × Δ_ε). Its germ at (Q,0) is irreducible of pure dimension 2.
- (b) Near (Q,0), 𝒬 = Σ ∩ (Δ_{G_Q} × Δ_ε) is a closed analytic curve. Λ = (q × id)^{-1}(𝒬) is closed analytic near (0,0), with Λ ∩ {t = 0} = {(0,0)} and Λ_t finite for every t.

*Proof.*
- (a) Analyticity and the equality.
  - q × id is proper (finite group quotient). closure(Ñ) is closed analytic near (0,0) (BB6). By Remmert's proper mapping theorem (fact A1), Σ is closed analytic near (Q,0).
  - By Lemma 2.1(b), Σ ⊃ N_c, and Σ is closed, so Σ ⊃ closure(N_c). Conversely Σ ⊂ closure((q × id)(Ñ)) = closure(N_c) by continuity.
  - Near (Q,0), closure(N_c) = H(c° × Δ_ε), because c° ∖ Q is dense in c° and H is a homeomorphism.
- (a) Irreducibility. Near (Q,0), Σ is homeomorphic to c° × Δ_ε, a topological 4-manifold. So every irreducible component of the germ has dimension 2: a component of dimension ≤ 1 would contain points, off the other components, where Σ has topological dimension ≤ 2.
  - Suppose the germ were Σ_1 ∪ Σ_2 with Σ_1 ⊄ Σ_2 and Σ_2 ⊄ Σ_1. Then dim(Σ_1 ∩ Σ_2) ≤ 1.
  - Take a neighbourhood U of (Q,0) in which Σ ∩ U is homeomorphic to a 4-ball and representatives of Σ_1, Σ_2 are defined.
  - The set (Σ ∩ U) ∖ (Σ_1 ∩ Σ_2) is connected, since a closed set of topological dimension ≤ 2 does not separate a connected 4-manifold (fact T2).
  - But it is the disjoint union of the relatively open sets Σ_1 ∖ Σ_2 and Σ_2 ∖ Σ_1, both non-empty for all small U. This is a contradiction.
- (b) By fact K2, q^{-1}(Δ_{G_Q}) ∩ B = {s_e = 0 for all e}, a closed Aut(Q)-invariant analytic set. So Δ_{G_Q} ∩ q(B) is closed analytic in q(B) (fact A1).
  - By (R2), Σ ∩ (Δ_{G_Q} × Δ_ε) = H((c ∩ Δ_{G_Q}) × Δ_ε) near (Q,0).
  - Here c ∩ Δ_{G_Q} = {Q}, because c ∖ Q ⊂ Δ_{G_c} and distinct strata are disjoint. So this set equals 𝒬, which is therefore analytic near (Q,0), and so is its preimage Λ.
  - Finally, q^{-1}(Q) = Aut(Q)·0 = {0} (fact K1), and q^{-1}(Q_t) is finite. ∎

*Remark.* 𝒬 is homeomorphic to a disc via t, so it is locally irreducible. Its normalisation maps biholomorphically onto Δ_ε, and t ↦ Q_t is therefore holomorphic. This is not needed below.

**Lemma 2.3 ((I1): lift-curves).** Let Q be a puncture point.
- (a) Every irreducible component L of the germ of Λ at (0,0) is a curve germ on which t is non-constant. In particular t(L) contains a neighbourhood of 0, and L ∩ {t = 0} = {(0,0)}. There is at least one lift-curve.
- (b) If L_0 is a lift-curve, the lift-curves are exactly the germs aL_0, a ∈ Aut(Q). So they form one Aut(Q)-orbit.
- (c) Every label is intact at every point of Λ (near (0,0)).

*Proof.*
- (a) Λ ∩ {t = 0} = {(0,0)} (Lemma 2.2(b)), so t is a finite map on Λ near (0,0) and dim Λ ≤ 1.
  - As t → 0, Q_t → Q. Since q is proper with q^{-1}(Q) = {0}, the non-empty sets q^{-1}(Q_t) converge to 0. So (0,0) is not isolated in Λ, the germ has positive dimension, and all its components are curves: a 0-dimensional component {(0,0)} would make (0,0) isolated.
  - On a component L, t ≢ 0, since L ⊄ {(0,0)}. By the open mapping property for a non-constant function on an irreducible curve germ (fact A3), t(L) is a neighbourhood of 0.
- (b) Each aL_0 is a component, because a is an automorphism of B × Δ_ε preserving t and Λ.
  - Let L be any component, and take small representatives. For (p,t) ∈ L with t ≠ 0 small, (a) gives (p′,t) ∈ L_0 with p′ near 0. Since q(p) = Q_t = q(p′), fact K1 gives p = ap′ for some a ∈ Aut(Q).
  - Hence L ⊂ ⋃_a aL_0 as germs. L is irreducible, so L ⊂ aL_0 for one a. Both are irreducible curve germs, so L = aL_0.
- (c) q(p) = Q_t ∈ Δ_{G_Q}, since H preserves strata. So all s_e(p) = 0 (fact K2). ∎

**Lemma 2.4 ((I3): equivariance).** Let a ∈ Aut(Q).
- (a) For p ∈ B and a label y: y is intact at ap iff a^{-1}y is intact at p, and then F_y(ap) ≅ F_{a^{-1}y}(p) as pointed curves (unordered special points).
- (b) a(Ñ_c̃) = Ñ_{ac̃}. If T is an anchored sheet of c̃, then aT is an anchored sheet of ac̃. ac̃ is a lift of the same branch c, so aT is of boundary type iff T is.
- (c) If L is a lift-curve, so is aL, and C_Φ(aL) = a·C_Φ(L). If z is Φ-persistent on T with function φ, then az is Φ-persistent on aT with function φ.

*Proof.*
- (a) This is fact K3.
- (b) (q × id)^{-1}(N_c) is a-invariant, because q∘a = q. So a permutes its connected components, and the image of Ñ_c̃ is the component containing a((c̃ ∖ 0) × {0}) = (ac̃ ∖ 0) × {0}, i.e. Ñ_{ac̃}.
  - a is a biholomorphism of B × Δ_ε fixing (0,0). So it maps closure(Ñ_c̃) onto closure(Ñ_{ac̃}), and the germ components at (0,0) of the one onto those of the other.
  - If T ⊃ c̃ × {0}, then aT ⊃ ac̃ × {0}.
  - ac̃ is a component of the germ q^{-1}(c), because q∘a = q.
- (c) Λ is a-invariant, so aL is a lift-curve. By (a), v_y(ap,t) = v_{a^{-1}y}(p,t). So v_y(aL) = v_{a^{-1}y}(L) as germs, which gives y ∈ C_Φ(aL) ⟺ a^{-1}y ∈ C_Φ(L). The statement for T is the same computation, together with: az intact at ap ⟺ z intact at p. ∎

**Lemma 2.5 ((I2): every anchored sheet of boundary type contains a lift-curve).** Let Q be a puncture point, c of boundary type, and T an anchored sheet of c̃. Then T contains a lift-curve.

*Proof.*
- Let B′ ⊂ B be any smaller Aut(Q)-invariant ball and 0 < ε′ ≤ ε. Let T̂ be a representative of T that is closed analytic in B′ × Δ_{ε′}, of pure dimension 2 (BB6).
- By Remmert (fact A1), (q × id)(T̂) is closed analytic in q(B′) × Δ_{ε′}.
- Its germ at (Q,0) is the image of the germ T, since (0,0) is the only preimage of (Q,0). So it is 2-dimensional, because q × id is finite.
- It is contained in the germ of Σ, which is irreducible and 2-dimensional (Lemma 2.2(a)). Hence it equals the germ of Σ, which contains 𝒬.
- So for all small t there is (p,t) ∈ T̂ with q(p) = Q_t, i.e. T̂ ∩ Λ has points with t ≠ 0 in every B′ × Δ_{ε′}.
- Therefore the analytic germ T ∩ Λ is not contained in {(0,0)}. It has a 1-dimensional irreducible component. That component is an irreducible curve germ inside the germ Λ, so it lies in a component of Λ and equals it by dimension. ∎

**Lemma 2.6 (a sheet maps into one component W) — repair (R-i).** Let T be an anchored sheet of c̃ (any type). Fix a graph isomorphism ι : G_S → G_c, and put Π := ι_*∘Π_S : Z_S → ∏_{w∈V(G_c)} M̄_w.
- (a) There is W ∈ 𝒲, a component of 𝒲_{G_c}, such that (Π, t)(T̂) ⊂ W for a small representative T̂ of T.
- (b) Π(c̃ ∖ 0) lies in a single lifted piece E at time 0, and closure(E) is an irreducible component of W_0.
- (c) For (p,t) ∈ T̂ and u ∉ M_W: Π(p)[u] ∈ M_u and (Π(p)[u], t) ∈ Γ_{W,u}.

*Proof.*
- (a) Set-up. By Lemma 2.1(c), T̂ ⊂ Z_S × Δ_ε, so (Π, t) is defined and continuous on T̂.
  - Ñ is dense in closure(Ñ). The points of T̂ lying on no other germ component of closure(Ñ) form a dense open subset of T̂. Hence T̂ ∩ Ñ is dense in T̂.
  - For (p,t) ∈ Ñ we have p ∈ Z_S^∘ (Lemma 2.1(a)). So Π(p) ∈ ∏M_w and ξ_{G_c}(Π(p)) = q(p) ∈ closure(V_t) ∩ Δ_{G_c} (fact PN(ii)), i.e. (Π(p), t) ∈ 𝒲_{G_c}.
  - By closedness, (Π, t)(T̂) ⊂ 𝒲_{G_c}.
- (a) Choice of W. Only finitely many components of 𝒲_{G_c} pass through (Π(0), 0). Their preimages are analytic subgerms covering the irreducible germ T, so T maps into one of them, W.
  - On T̂ ∩ Ñ, (Π, t) has finite fibres: Π_S has finite fibres on Z_S^∘ (fact PN(v)). So the image of the 2-dimensional germ T is 2-dimensional (fact A4), and dim W ≥ 2.
  - By 0.5, dim W ≤ 2. So W ∈ 𝒲.
- (b) For p ∈ c̃ ∖ 0, S(p) = S and q(p) ∈ c ∖ Q ⊂ closure(V_0) ∩ Δ_{G_c}. So Π(c̃ ∖ 0) ⊂ ξ_{G_c}^{-1}(closure(V_0) ∩ Δ_{G_c}).
  - The irreducible components of that analytic set are countably many. c̃ ∖ 0 is a connected punctured disc (on its normalisation), and Π is non-constant on it.
  - So the preimage of some component is not discrete. It is then all of c̃ ∖ 0, by the identity theorem on the normalisation (Baire). That component is 1-dimensional, i.e. a lifted piece E.
  - E × {0} meets the analytic set W_0 ∩ (∏M_w) in a set with non-empty interior in E. E is irreducible, so E ⊂ W_0, and closure(E) ⊂ W_0.
  - W_0 has pure dimension 1 (BB3, consequence), so the irreducible curve closure(E) is a component of W_0.
- (c) (Π(p), t) ∈ W_t lies on a component K_W × {c_D} (BB3). Hence Π(p)[u] = c_D[u] ∈ M_u, and (c_D[u], t) ∈ Γ_{W,u}. ∎

**Lemma 2.7 (Y ∈ Φ).** Assume Y is non-constant. Let E be a lifted piece in Δ_Γ at time 0, i.e. over a piece of ∂V_0, and let W ∈ 𝒲 be a component of 𝒲_Γ such that closure(E) is a component of W_0. Then:
- i ∉ M_W;
- Γ_{W,i} = graph(Y|_{Δ_*});
- the germ of graph([Y]) at (Y_0,0) is a non-constant irreducible germ belonging to Φ.

Such a W exists: apply Lemma 2.6(a),(b) to an anchored sheet of the lift β̃_1 at J_1 (BB1), with E := E^1.

*Proof.*
- For z ∈ E, ξ_Γ(z) ∈ ∂V_0, so z[i] = π_i(ξ_Γ(z)) = Y_0. Here we use product type: π_i∘ξ_Γ = pr_i. So i is constant on the fibre component closure(E), and i ∉ M_W by (U1).
- Let D = K_W × {c_D} be a component of W_t. K_W is not contained in the boundary, so D contains points z ∈ ∏M_w. They lie in 𝒲_Γ ∩ (∏M_w × Δ_*) = 𝒲_Γ^∘, so ξ_Γ(z) ∈ closure(V_t) ∩ Δ_Γ = ∂V_t, and c_D[i] = z[i] = Y_t.
- Hence Γ_{W,i} ⊂ graph(Y). Y is holomorphic (BB2), so graph(Y) is an irreducible closed curve. Γ_{W,i} is a closed curve surjecting onto Δ_*, so Γ_{W,i} = graph(Y).
- Its image in 𝔐 × Δ_* is graph([Y]). This is the graph of a holomorphic map, so its germ at (Y_0,0) is irreducible, and it is non-constant because [Y] is non-constant (0.2).
- i has type (g_i,n_i). So the germ lies in Φ. ∎

**Lemma 2.8 (Φ avoids 𝔉 off t = 0).** After shrinking ε, for every φ ∈ Φ:
- φ_t ∩ 𝔉 = ∅ for 0 < |t| < ε;
- φ̂ ∩ {t = 0} = {(Y_0,0)}.

*Proof.*
- For f ∈ 𝔉, the germ φ ∩ ({f} × Δ_*) is a proper analytic subgerm of the irreducible 1-dimensional germ φ. If f = Y_0 this is because φ is non-constant; if f ≠ Y_0, the line {f} × Δ_* does not pass through (Y_0,0). So it is ⊂ {(Y_0,0)}.
- φ ⊄ {t = 0}, because φ lies in a curve that is finite over Δ_*.
- Φ and 𝔉 are finite. ∎

---

## 3. The Φ-dichotomy at punctures (Φ-version of BB4)

BB4 (Theorem 1) is stated for Y and a generic time t ∉ Z. We need it for every φ ∈ Φ, but only at points that are punctures of the piece. In that case its trichotomy STAY / IMOV / excluded collapses: IMOV requires the point to lie in the stratum of the piece. We run its argument with Y replaced by φ. The only property of the time t that it uses is "the value avoids the finite set 𝔉". For a Puiseux branch φ this is read as φ_t ∩ 𝔉 = ∅ (repair (R-ii)), and by Lemma 2.8 it holds for **all** 0 < |t| < ε. So no discrete exceptional set Z_Φ is needed at all.

**Proposition 3.1 (Φ-dichotomy at a puncture).** Let Q be a puncture point, c of boundary type, c̃ a lift, T an anchored sheet of c̃, and T̂ a small representative. Let ι, Π, W be as in Lemma 2.6. Suppose:
- 0 < |t| < ε and (p,t) ∈ T̂ ∩ Λ (so q(p) = Q_t);
- y is a label with [F_y(p)] ∈ φ_t for some φ ∈ Φ (y is intact at p by Lemma 2.3(c));
- b is an irreducible component of the germ at p of the slice T̂_t.

Then y is intact at every point of b, and p′ ↦ F_y(p′) is constant on b.

(In the language of BB4: y is STAY along b, MERGE and puncture-MOV being excluded.)

*Proof.*
- **Set-up.** By Lemma 2.1(d), b is an irreducible curve germ at p. Λ_t is finite, and T̂ ∖ Λ ⊂ Ñ by Lemma 2.1(c). So b ∖ {p} ⊂ Ñ ⊂ Z_S^∘ × Δ_ε.
  - By Lemma 2.6(a), Π(b) ⊂ W_t. Π has finite fibres on Z_S^∘, so Π(b) is an irreducible 1-dimensional germ at Π(p). It therefore lies in one component D = K_W × {c_D} of W_t (BB3).
  - Write Π(p′) = (κ(p′), c_D) for p′ ∈ b, with κ(p′) ∈ K_W.
- **Π(p) is a puncture value.** ξ̄_{G_c}(Π(p)) = q(p) = Q_t (fact PN(ii)). Q ∉ Δ_{G_c} and H_t preserves strata, so Q_t ∉ Δ_{G_c} = ξ_{G_c}(∏M_w). Hence Π(p) ∉ ∏M_w. Since c_D ∈ ∏_{u∉M_W} M_u, the point κ := κ(p) has a coordinate in the boundary, i.e. κ ∈ F_W.
- Let u be the vertex of G_S that contains y, transported to G_c by ι.
- **Step 1 (MERGE excluded).** Suppose some edge e at y is not in S. Then e is contracted in G_S, so e joins two vertices of u (possibly y to itself).
  - By fact PN(iii), Π(p)[u] is the curve glued from the components of C_p labelled by the vertices of u, along the edges outside S joining them. It contains the node e, so Π(p)[u] ∈ ∂M̄_u.
  - If u ∉ M_W, then Π(p)[u] = c_D[u] ∈ M_u, a contradiction. So u ∈ M_W and Π(p)[u] = κ[u].
  - By PN(iii), F_y(p) with all its special points is an irreducible component, with its special points, of κ[u]. All edges are pinched at p ∈ Λ, so the special points of F_y(p) are exactly the half-edges at y, and these are exactly its special points in κ[u]: half-edges outside S become nodes of κ[u], half-edges in S become marked points.
  - Hence [F_y(p)] ∈ 𝔉_W ⊂ 𝔉. But [F_y(p)] ∈ φ_t, and φ_t ∩ 𝔉 = ∅ (Lemma 2.8). Contradiction.
  - So every edge at y lies in S. Then y is intact on Z_S ⊃ b, u = {y} is a vertex of G_S, and F_y = Π(·)[{y}] on Z_S (PN(iii)).
- **Step 2 (puncture-MOV excluded).** Suppose {y} ∈ M_W. Then F_y(p) = κ[{y}] is a coordinate of κ ∈ F_W, and it is a smooth curve because F_y(p) ∈ M_y. So [F_y(p)] ∈ 𝔉_W ⊂ 𝔉, which again contradicts Lemma 2.8.
  - Hence {y} ∉ M_W, and F_y(p′) = Π(p′)[{y}] = c_D[{y}] for every p′ ∈ b. ∎

*Remark.* No genericity of t beyond 0 < |t| < ε was used, and no comparison of different copies of Y_0 was made. The proof uses only BB3 (through F_W, 𝔉 and the product form K_W × {c_D}) and fact PN.

---

## 4. Values along lift-curves; persistence equals lift-curve values; Proposition 4

**Lemma 1 (values along a lift-curve: Φ or rigid).** Let Q be a puncture point, T a boundary-type anchored sheet at Q, L ⊂ T a lift-curve, and y a label with [F_y(0)] = Y_0. Then the image germ v_y(L) is either a branch φ ∈ Φ (so y ∈ C_Φ(L)) or the germ of {Y_0} × Δ (y is a rigid Y_0-copy along L).

*Proof.*
- **Step 1.** y is intact on L (Lemma 2.3(c)), so v_y is holomorphic on L. The t-component of v_y is finite on L (Lemma 2.3(a)), so v_y|_L is a finite map. Hence v_y(L) is an irreducible 1-dimensional germ at v_y(0,0) = (Y_0, 0) (fact A4).
- **Step 2 (the components of Q_t).** Let ι, Π, W be as in Lemma 2.6 for T, and T̂ a small representative. Let (p_*, t) ∈ L with 0 < |t| < ε.
  - By Lemma 2.1(d), T̂_t has pure dimension 1 at p_*. Λ_t is finite. So there are points p_n ∈ T̂_t ∖ Λ ⊂ Ñ with p_n → p_*.
  - By Lemma 2.6(a), Π(p_n) ∈ W_t. W_t has finitely many components; pass to a subsequence lying in one of them, K_W × {c_D}. Then Π(p_n) = (κ_n, c_D) with κ_n ∈ K_W.
  - Π is continuous on Z_S, so Π(p_*) = lim Π(p_n) = (κ_∞, c_D) with κ_∞ ∈ K_W (K_W is compact).
  - As in the proof of Proposition 3.1, ξ̄(Π(p_*)) = Q_t ∉ Δ_{G_c}, so κ_∞ ∈ F_W.
  - Q_t = q(p_*) is the curve obtained by gluing the coordinates of (κ_∞, c_D) (fact PN(ii)). Gluing identifies marked points pairwise and does not change the set of special points on any irreducible component.
  - So every irreducible component of Q_t, with its special points, is of one of two kinds:
    - **(a)** a whole coordinate c_D[w] with w ∉ M_W; then (c_D[w], t) ∈ Γ_{W,w};
    - **(b)** a component of a coordinate κ_∞[w] with w ∈ M_W; if it has type (g_i,n_i), its class lies in 𝔉_W.
  - F_y(p_*) is the component of Q_t labelled y, of type (g_i,n_i).
  - Hence v_y(p_*, t) ∈ 𝒢 := ⋃ {Γ̄_{W,w} : w ∉ M_W of type (g_i,n_i)} ∪ (𝔉_W × Δ_*). This is a closed analytic curve in 𝔐 × Δ_*.
- **Step 3 (the dichotomy).** By Step 2 and closedness, v_y(L) ⊂ 𝒢 as germs at (Y_0,0).
  - An irreducible 1-dimensional germ inside a 1-dimensional analytic germ equals one of its irreducible components. So v_y(L) is either a branch at (Y_0,0) of some Γ̄_{W,w} (w ∉ M_W of type (g_i,n_i)), or the germ of {f} × Δ for some f ∈ 𝔉_W. In the second case f = Y_0, since the germ passes through (Y_0,0).
  - In the first case: if the branch is non-constant, it belongs to Φ by definition (W ∈ 𝒲). Otherwise it is the germ of {Y_0} × Δ. ∎

**Lemma 2 ((NRT_P) at Q ⇔ C_Φ is Aut(Q)-invariant).** Let Q be a puncture point. Then Lemma 1 applies to every lift-curve L at Q. Moreover the following are equivalent:
- (i) there is no (a, L, x) at Q as excluded in (NRT_P);
- (ii) C_Φ(L) is Aut(Q)-invariant for some lift-curve L;
- (iii) C_Φ(L) is Aut(Q)-invariant for every lift-curve L, and C_Φ(L) = C_Φ(L′) for all lift-curves L, L′ at Q.

*Proof.*
- **Lemma 1 applies everywhere.** Q has a boundary-type branch c. Let c̃ be a lift and T an anchored sheet of c̃ (both exist, 0.7). By Lemma 2.5, T contains a lift-curve L_1. By Lemma 2.3(b), every lift-curve has the form aL_1. Then aL_1 ⊂ aT, which is a boundary-type anchored sheet of ac̃ (Lemma 2.4(b)).
- **(i) ⇒ (iii).** Let L be a lift-curve, x ∈ C_Φ(L) with branch φ, and a ∈ Aut(Q).
  - v_x(0,0) = (Y_0,0), so [F_x(0)] = Y_0.
  - By Lemma 2.4(a) with p = 0 (a fixes 0), F_{a^{-1}x}(0) ≅ F_x(0), so [F_{a^{-1}x}(0)] = Y_0.
  - By Lemma 1, a^{-1}x is in C_Φ(L) or is a rigid Y_0-copy along L. The second alternative is exactly the configuration excluded by (i). Hence a^{-1}x ∈ C_Φ(L).
  - As a ranges over the group Aut(Q), this shows that C_Φ(L) is Aut(Q)-invariant.
  - Then for every a, C_Φ(aL) = a·C_Φ(L) = C_Φ(L) (Lemma 2.4(c)). By Lemma 2.3(b) this covers all lift-curves.
- **(iii) ⇒ (ii).** Trivial.
- **(ii) ⇒ (i).** Suppose (a, L′, x) is an excluded configuration, and let L be the lift-curve in (ii). By Lemma 2.3(b), L′ = hL for some h ∈ Aut(Q), and C_Φ(L′) = h·C_Φ(L), which is Aut(Q)-invariant.
  - x ∈ C_Φ(L′), so a^{-1}x ∈ C_Φ(L′), i.e. v_{a^{-1}x}(L′) ∈ Φ.
  - But v_{a^{-1}x}(L′) is the germ of {Y_0} × Δ, which is not in Φ. Contradiction. ∎

**Lemma 3 (P_Φ(T) = C_Φ(L)).** Let Q be a puncture point, T a boundary-type anchored sheet at Q, and L ⊂ T a lift-curve. Then P_Φ(T) = C_Φ(L). Moreover, the function on T of a label y ∈ P_Φ(T) is the branch v_y(L).

*Proof.*
- **(⊂).** Let y ∈ P_Φ(T) with function φ. y is intact on L ⊂ T, and v_y(L) ⊂ v_y(T) ⊂ φ. By Lemma 1, Step 1, v_y(L) is a 1-dimensional irreducible germ, so v_y(L) = φ ∈ Φ and y ∈ C_Φ(L).
- **(⊃), the analytic set A_y.** Let y ∈ C_Φ(L), with φ := v_y(L) ∈ Φ. Let T̂ be a small representative of T, closed analytic in a neighbourhood U of (0,0), with L̂ ⊂ T̂. Put

  A_y := {(p,t) ∈ T̂ : y intact at p and ([F_y(p)], t) ∈ Γ̄_all}.

  A_y is a closed analytic subset of T̂: L_y is closed analytic, F_y is holomorphic on it, and Γ̄_all is closed analytic.
- **The slices.** For 0 < |t| < ε and (p,t) ∈ L̂, we have [F_y(p)] ∈ φ_t.
  - By Proposition 3.1, along every irreducible component b of the germ of T̂_t at p, y is intact and F_y is constant, equal to F_y(p). Its class lies in φ_t ⊂ Γ̄_all.
  - So A_y contains the germ of T̂_t at (p,t), which is 1-dimensional (Lemma 2.1(d)).
- **Countability argument.** By Lemma 2.3(a), such points (p,t) exist for every t in a punctured disc, i.e. for uncountably many t, inside every neighbourhood of (0,0).
  - If the germ A_y had dimension ≤ 1, some representative in a neighbourhood U′ ⊂ U would have dimension ≤ 1. Its 1-dimensional irreducible components are countably many (local finiteness). Each one either lies in a single level {t = t_0} or meets every level in a discrete set.
  - A 1-dimensional germ of A_y ∩ {t = t_0} must lie in a component contained in {t = t_0}. So only countably many levels could carry such germs. This is a contradiction.
  - Hence the germ A_y is 2-dimensional. T is an irreducible 2-dimensional germ, so A_y = T as germs (repair (R-iii): all statements are germ statements, and the uncountably many slices occur in every neighbourhood).
- **Single branch.** Thus y is intact on T, and v_y(T) ⊂ Γ̄_all. Γ̄_all has finitely many irreducible branches at (Y_0,0). Their preimages under v_y are analytic subgerms covering the irreducible germ T, so v_y(T) lies in one branch φ′.
  - Then φ = v_y(L) ⊂ φ′. Both are irreducible 1-dimensional germs, so φ′ = φ ∈ Φ.
  - Hence y ∈ P_Φ(T), with function φ. ∎

**Proposition 4 (transfer between boundary-type sheets at one puncture point).** Assume (NRT_P). Let Q be a puncture point, T, T′ boundary-type anchored sheets at Q (of lifts c̃, c̃′, equal or not, of the same or different branches), and x ∈ P_Φ(T). Then:
- x ∈ P_Φ(T′);
- if T′ is an anchored sheet of c̃′, then x is intact along c̃′ and [F_x] ≡ Y_0 on c̃′ near 0.

The second item holds for any anchored sheet T′ of c̃′ with x ∈ P_Φ(T′); it does not use (NRT_P).

*Proof.*
- By Lemma 2.5, choose lift-curves L ⊂ T and L′ ⊂ T′.
- By Lemma 3, x ∈ C_Φ(L). By (NRT_P) and Lemma 2 (i) ⇒ (iii), C_Φ(L′) = C_Φ(L) ∋ x. By Lemma 3 for T′, x ∈ P_Φ(T′).
- **Last clause.** Let ψ be the function of x on T′. Since c̃′ × {0} ⊂ T′, x is intact along c̃′, and v_x(p,0) ∈ ψ̂ ∩ {t = 0} = {(Y_0,0)} for p ∈ c̃′ near 0 (Lemma 2.8). ∎

---

## 5. Lemma 5 (Φ-transfer along a travel interval)

**Lemma 5.** Let 1 ≤ m ≤ k − 1. Let T be an anchored sheet of the leaving lift β̃′_m (in Def(J_m)) with x_m ∈ P_Φ(T), with function φ. Then there is an anchored sheet T″ of the entering lift β̃_{m+1} (in Def(J_{m+1})) with x_{m+1} ∈ P_Φ(T″), with some function ψ ∈ Φ, possibly ψ ≠ φ. Neither (NRT_P) nor boundary type is used.

*Proof.* Write G := G(D^{m+1}), E := E^{m+1}, c := c_{m+1} (BB1-M).

**Step 1 (the component 𝒲̃).**
- In Def(J_m), the branch β′_m of closure(D^{m+1}) has β′_m ∖ J_m ⊂ D^{m+1} ⊂ Δ_G, so G_{β′_m} = G.
- Put S′ := S(β̃′_m) and Π′ := (ι′_m)_*∘Π_{S′}.
- By Lemma 2.6(a), applied with ι := ι′_m, there is 𝒲̃ ∈ 𝒲, a component of 𝒲_G, with (Π′, t)(T̂) ⊂ 𝒲̃.
- By BB1-M, Π′(β̃′_m ∖ 0) ⊂ E. So by Lemma 2.6(b), closure(E) is a component of 𝒲̃_0.
- c is constant on E, so **c ∉ M_𝒲̃** by (U1).

**Step 2 (x_m is the vertex c on T).**
- x_m is intact on T ⊃ β̃′_m × {0}, hence along β̃′_m. By BB1-M, ι′_m({x_m}) = c.
- By fact PN(iii), F_{x_m}(p) = Π′(p)[c] for p ∈ Z_{S′}. By Lemma 2.6(c), (Π′(p)[c], t) ∈ Γ_{𝒲̃,c} for (p,t) ∈ T̂.
- Since [F_{x_m}(0)] = Y_0, the vertex c has type (g_i,n_i).
- Put Γ̄ := Γ̄_{𝒲̃,c}, a closed irreducible curve in 𝔐 × Δ_*, finite over Δ_*. We get v_{x_m}(T̂) ⊂ Γ̄.

**Step 3 (Γ̄ ⊃ φ).**
- t is non-constant on the irreducible germ T (Lemma 2.1(c)), so t(T̂) contains a neighbourhood of 0 (fact A3).
- Hence v_{x_m}(T̂), which lies in φ̂ ∩ Γ̄, meets 𝔐 × {t} for every small t.
- So the germ φ ∩ Γ̄ is an analytic subgerm of the irreducible curve germ φ that is not ⊂ {(Y_0,0)}. Hence it equals φ, i.e. φ ⊂ Γ̄.

**Step 4 (every branch of Γ̄ at (Y_0,0) lies in Φ).**
- Suppose some branch of Γ̄ at (Y_0,0) were the germ of {Y_0} × Δ. Then Γ̄ ∩ ({Y_0} × Δ_*) would be an analytic subset of the irreducible curve Γ̄ of dimension 1, hence all of Γ̄ (fact A2), and Γ̄ ⊂ {Y_0} × Δ_*.
- This contradicts φ ⊂ Γ̄ with φ non-constant.
- So every branch of Γ̄ at (Y_0,0) is non-constant. Since 𝒲̃ ∈ 𝒲 and c ∉ M_𝒲̃ is of type (g_i,n_i), every such branch belongs to Φ.

(This replaces the Y-version's "persistence holds on all of 𝒲̃": the function may change from φ to another branch of the same irreducible Γ̄, but it can never become constant.)

**Step 5 (a sheet T″ of β̃_{m+1} mapping into 𝒲̃).** Work in Def(J_{m+1}).
- Put β̃ := β̃_{m+1}, of the branch β := β_{m+1} of closure(D^{m+1}). Put S″ := S(β̃) and Π″ := (ι_{m+1})_*∘Π_{S″}. By BB1-M, Π″(β̃ ∖ 0) ⊂ E.
- Choose p̃ ∈ β̃ ∖ 0 so close to 0 that the following hold:
  - (α) closure(Ñ_β̃) is analytic of pure dimension 2 near (p̃,0) (BB6);
  - (β) q(p̃) is a smooth point of the curve B_0, near which B_0 coincides with D^{m+1}, hence with β. All but finitely many points of β ∖ J_{m+1} near J_{m+1} qualify: B_0 has finitely many singular points, and β ∖ J_{m+1} ⊂ D^{m+1}.
- Put z := Π″(p̃) ∈ E. Then (z,0) ∈ 𝒲̃, by Step 1.
- **(i)** Δ_G ⊂ ∂M̄_g, so closure(V_0) ∩ Δ_G = B_0 ∩ Δ_G. By (β), this coincides with β near q(p̃). By (R2), near (q(p̃), 0),
  closure(𝒱) ∩ (Δ_G × Δ) = H((closure(V_0) ∩ Δ_G) × Δ) = H(β × Δ),
  and this is the transport base N_β near that point.
- **(ii)** Let (p,t) be near (p̃,0).
  - If (q(p),t) ∈ closure(𝒱) ∩ (Δ_G × Δ), then |S(p)| = |E(G)| = |S″| and S(p) ⊂ S(p̃) = S″. So S(p) = S″ and p ∈ Z_{S″}^∘.
  - Conversely, points of Z_{S″} near p̃ lie in Z_{S″}^∘, because s_e(p̃) ≠ 0 for e ∉ S″.
  - Since ξ_G∘Π″ = q on Z_{S″}^∘ (fact PN(ii)), near (p̃,0) we get
    (q × id)^{-1}(N_β) = {(p,t) ∈ Z_{S″} × Δ_ε : (Π″(p), t) ∈ 𝒲_G}.
- **(iii)** By fact PN(iv), Π″ × id is a finite open map from a neighbourhood of (p̃,0) in the manifold Z_{S″} × Δ_ε onto a neighbourhood of (z,0) in ∏M_w × Δ_*. These manifolds have the same dimension.
  - Hence the germ at (p̃,0) of (Π″ × id)^{-1}(𝒲̃) has dimension 2. It is ≤ 2 by finiteness and ≥ 2 by openness (fact A4).
  - Let Z be a 2-dimensional irreducible component of this germ.
- **(iv)** By (ii), Z ⊂ (q × id)^{-1}(N_β). Take a connected representative of Z containing (p̃,0) (fact A5). Since (p̃,0) ∈ Ñ_β̃, which is a connected component of (q × id)^{-1}(N_β), this representative lies in Ñ_β̃.
- **(v)** The germ of closure(Ñ_β̃) at (p̃,0) is the union of the germs of its global irreducible components through (p̃,0). Let 𝒯 be one containing Z. It has pure dimension 2 and lies in Z_{S″} × Δ_ε (Lemma 2.1(c)).
  - 𝒯 ∩ (Π″, t)^{-1}(𝒲̃) is an analytic subset of the irreducible 𝒯 containing the 2-dimensional germ Z. So it is 𝒯 (fact A2), i.e. (Π″, t)(𝒯) ⊂ 𝒲̃.
- **(vi)** By Lemma 2.1(c),(d) and Krull, Z ∩ {t = 0} has pure dimension 1 at (p̃,0). It lies in q^{-1}(β) × {0}, and near p̃ this equals β̃ × {0}, since distinct lifts of β meet only at 0.
  - So 𝒯 ∩ (β̃ × {0}) contains a non-empty open subset of the irreducible curve β̃ ∩ B (B a Milnor ball, fact A5). Hence it contains all of β̃ ∩ B, and (0,0) ∈ 𝒯.
- **(vii)** 𝒯 has pure dimension 2, and so does closure(Ñ_β̃). So each irreducible component of the germ of 𝒯 at (0,0) is a component of the germ of closure(Ñ_β̃) at (0,0).
  - The irreducible germ β̃ × {0} lies in one of them, T″. So T″ is an anchored sheet of β̃_{m+1}, and (Π″, t)(T″) ⊂ 𝒲̃.

**Step 6 (x_{m+1} on T″).**
- By BB1-M, x_{m+1} is intact along β̃ and ι_{m+1}({x_{m+1}}) = c. So x_{m+1} is intact on Z_{S″} ⊃ T″, and F_{x_{m+1}} = Π″(·)[c] there (fact PN(iii)).
- For (p,t) ∈ T̂″, (Π″(p), t) ∈ 𝒲̃_t lies on a component K_𝒲̃ × {c_D}. Since c ∉ M_𝒲̃, Π″(p)[c] = c_D[c] with (c_D[c], t) ∈ Γ_{𝒲̃,c}. So v_{x_{m+1}}(T̂″) ⊂ Γ̄.
- At the origin: for p ∈ β̃ ∖ 0, Π″(p) ∈ E, on which c is constant of class Y_0. By continuity, [F_{x_{m+1}}(0)] = Y_0.
- So v_{x_{m+1}}(T″) is a germ at (Y_0,0) inside Γ̄. Since T″ is irreducible, it lies in a single branch ψ of Γ̄ at (Y_0,0): the preimages of the branches are analytic subgerms covering T″.
- By Step 4, ψ ∈ Φ. Hence x_{m+1} ∈ P_Φ(T″) with function ψ. ∎

---

## 6. Proof of Theorem B

**Lemma 6.1 (base).** Assume Y is non-constant. For every anchored sheet T of β̃_1 (in Def(J_1)):
- x_1 is Y-persistent on T;
- consequently x_1 ∈ P_Φ(T), with function the germ of graph([Y]), which belongs to Φ by Lemma 2.7.

*Proof.*
- Put S := S(β̃_1) and Π := (ι_1)_*∘Π_S. By BB1-M (with m = 1, c_1 = i), x_1 is intact along β̃_1 and ι_1({x_1}) = i. So x_1 is intact on Z_S, and F_{x_1} = Π(·)[i] there (fact PN(iii)).
- Let (p,t) ∈ Ñ_{β̃_1}. By Lemma 2.1(a), p ∈ Z_S^∘ and q(p) ∈ H_t(β_1 ∖ J_1) ⊂ closure(V_t) ∩ Δ_Γ = ∂V_t, since β_1 ∖ J_1 ⊂ D^1 ⊂ Δ_Γ.
- By fact PN(ii), ξ_Γ(Π(p)) = q(p). By product type, Π(p)[i] = π_i(q(p)) = Y_t. So [F_{x_1}(p)] = [Y_t].
- Ñ_{β̃_1} is dense in a representative of T (proof of Lemma 2.6(a)), and both sides are continuous on Z_S × Δ_ε. Hence [F_{x_1}] = [Y_t] on all of T̂, and v_{x_1}(T) ⊂ graph([Y]). ∎

**The induction.** Suppose, for contradiction, that Y is non-constant. Then BB1 applies. For m = 1, …, k consider:

**(C_m)** There is an anchored sheet T_m of β̃_m (in Def(J_m)) with x_m ∈ P_Φ(T_m).

- **(C_1)** holds by Lemma 6.1, because anchored sheets of β̃_1 exist (0.7).
- **(C_m) ⇒ (C_{m+1})** for 1 ≤ m ≤ k − 1. First we produce an anchored sheet T′_m of the leaving lift β̃′_m with x_m ∈ P_Φ(T′_m). The two cases are exhaustive (repair (R-iv)).
  - **Case (a): J_m ∈ Δ_{G(D^m)} ∪ Δ_{G(D^{m+1})}.** By BB1 (IMOV_all), β̃′_m = β̃_m with the same label. Take T′_m := T_m.
  - **Case (b): otherwise.** By BB1 (P), J_m is a puncture point, and β̃_m, β̃′_m are of boundary type. Let T′_m be any anchored sheet of β̃′_m (0.7). Proposition 4, applied at Q = J_m to T = T_m and T′ = T′_m, gives x_m ∈ P_Φ(T′_m). This is the only place, besides the endpoint, where (NRT_P) is used.

  Lemma 5 applied to T′_m then gives (C_{m+1}).
- **Endpoint.** By (C_k), x := x_k ∈ P_Φ(T_k) for an anchored sheet T_k of β̃_k at Q_0. By BB1 (P), Q_0 is a puncture point and β̃_k, b̃ are of boundary type.
  - Let T_b be an anchored sheet of b̃. By Proposition 4, x ∈ P_Φ(T_b), and x is intact along b̃ with [F_x] ≡ Y_0 on b̃ near 0.
  - **MERGE is impossible.** For an edge e at x, s_e vanishes on b̃ near 0, hence on the irreducible germ b̃. So e ∈ S(b̃).
  - **MOV is impossible.**
    - x is intact along b̃, so F_x is holomorphic on the irreducible curve b̃ ∩ B.
    - Let n : D → b̃ ∩ B be the normalisation, where D is a disc (connected).
    - [F_x]∘n : D → 𝔐 is holomorphic and equals Y_0 on a non-empty open set. The preimage of the point Y_0 is an analytic subset of D with interior, so it is all of D (fact A2).
    - Hence [F_x] ≡ [Y_0] on b̃ ∩ B, contradicting MOV.
  - Since BB1 asserts MERGE or MOV at the endpoint, we have a contradiction. (The case k = 1 is included: then J_1 = Q_0 and the induction is empty.)

Hence Y is constant, so Y_t = Y_0 for all t ∈ Δ. ∎ (main statement of Theorem B)

**Where the hypotheses enter.**
- (R1), (R2): everywhere.
- (Rig): only through BB3, used in Lemmas 2.6, 2.7, Proposition 3.1, Lemma 1 and Lemma 5.
- Product type: Lemmas 2.7 and 6.1.
- (NRT_P): only through Lemma 2, i.e. Proposition 4, at the puncture transitions of case (b) and at Q_0. All of these are puncture points, so (NRT_P), which is stated only at puncture points, suffices.
- dim M_{g_i,n_i} > 0 is used only to make the non-constancy assumption meaningful. If dim M_{g_i,n_i} = 0, Y is trivially constant.

**6.2 The "moreover" clauses.**
- **(NRT_P) is implied by the problem's conclusion.** The setting of (NRT_P) (0.9) includes "t ↦ Y_t is non-constant". If the problem's conclusion holds for a family, i.e. Y_t = Y_0 for all t, that family does not satisfy the setting, and (NRT_P) holds vacuously for it.
- **A counterexample to (NRT_P) is a counterexample to the problem.** Such a counterexample is a family satisfying the setting of (NRT_P) and admitting a configuration (Q, a, L, x). In particular it satisfies the problem's hypotheses (in the readings (R1), (R2)) and has Y non-constant, so the problem's conclusion fails for it. Theorem B and this remark together say that, under (Rig), the problem and (NRT_P) are equivalent.
- **Isotropy drop.** Let (Q, a, L, x) be a configuration violating (NRT_P).
  - Then aL ≠ L. Otherwise C_Φ(L) = C_Φ(aL) = a·C_Φ(L) (Lemma 2.4(c)), so C_Φ(L) = a^{-1}·C_Φ(L) ∋ a^{-1}x. But a^{-1}x is a rigid Y_0-copy along L, so v_{a^{-1}x}(L) ∉ Φ. Contradiction.
  - L and aL are distinct irreducible curve germs, so after shrinking they meet only at (0,0). For small t ≠ 0 and (p,t) ∈ L, we get (ap,t) ∈ aL ∖ L, hence ap ≠ p.
  - So a ∉ Stab_{Aut(Q)}(p). By fact K4, Stab_{Aut(Q)}(p) ≅ Aut(C_p) = Aut(Q_t).
  - Hence |Aut(Q_t)| = |Stab(p)| < |Aut(Q)|, and Q_t has |Aut(Q)|/|Aut(Q_t)| ≥ 2 preimages in B.
  - So a failure of (NRT_P) requires the automorphism a of the puncture curve Q to be lost along the transported points Q_t (t ≠ 0). This is possible under the coarse reading (R2), which does not require H_t to preserve automorphism groups.

---

## Cited classical facts

All are cited from memory; standard references are indicated.

- **K1 (Kuranishi chart).** For a stable curve C_Q and a small enough Aut(Q)-invariant ball B ⊂ Def(Q), q : B → M̄_g is the quotient by Aut(Q) onto an open neighbourhood of Q. Its fibres are Aut(Q)-orbits, and q^{-1}(Q) = {0}. (Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, Ch. XI.)
- **K2 (plumbing coordinates).** For each edge e of G_Q there is a coordinate s_e on B such that the nodes of C_p correspond to the edges with s_e(p) = 0, and the dual graph of C_p is G_{S(p)}. In particular q^{-1}(Δ_{G_Q}) ∩ B = {s_e = 0 for all e}.
- **K3 (equivariance).** For a ∈ Aut(Q) and p ∈ B there is an isomorphism C_p → C_{ap} that maps the node of e to the node of ae, and, when y is intact at p, the component labelled y to the component labelled ay. Hence s_e(p) = 0 ⟺ s_{ae}(ap) = 0 and F_{ay}(ap) ≅ F_y(p). Lemma 2.4(a) is this with y replaced by a^{-1}y.
- **K4 (isotropy).** For B small and p ∈ B, Stab_{Aut(Q)}(p) ≅ Aut(C_p).
- **PN (partial normalisation along node sections).** For S ⊂ E(G_Q) there is a holomorphic map Π_S : Z_S → ∏_{w∈V(G_S)} M̄_w (G_S := G_Q with the edges outside S contracted) such that:
  - (i) it is obtained by normalising the nodes in S of the fibres;
  - (ii) ξ̄_{G_S}∘Π_S = q on Z_S, and Π_S(Z_S^∘) ⊂ ∏M_w;
  - (iii) for p ∈ Z_S, the u-coordinate Π_S(p)[u] is the partial normalisation of C_p at the S-nodes, restricted to the part labelled by u, with the S-half-edges as marked points. If S(p) = E(G_Q), it is glued from the components labelled by the vertices of u along the non-S edges joining them. If every edge at y lies in S, then {y} is a vertex of G_S and Π_S(p)[{y}] = F_y(p) on Z_S. This is the definition of F_y, and it shows that F_y is holomorphic on L_y = Z_{S_y};
  - (iv) near p̃ ∈ Z_S^∘, Z_S is smooth, and Π_S|_{Z_S} is finite and open onto a neighbourhood of Π_S(p̃) in ∏M_w (equisingular deformations of C_{p̃} are the deformations of its pointed normalisation);
  - (v) Π_S has finite fibres on Z_S^∘, by (ii) and the finiteness of q.
- **A1 (Remmert proper mapping theorem).** The image of a closed analytic set under a proper holomorphic map is analytic; finite maps preserve dimension.
- **A2 (irreducibility, identity).**
  - An analytic subset (or subgerm) of an irreducible analytic set (or germ) X that has dimension dim X, or contains a non-empty open subset of X, equals X.
  - An irreducible germ contained in a finite union of analytic germs lies in one of them.
  - Global irreducible components are locally finite, and the germ of an analytic set at a point is the union of the germs of the global components through it.
- **A3 (open mapping).** A holomorphic function that is non-constant on an irreducible germ maps it onto a neighbourhood germ of its value.
- **A4 (images and dimension).** Under a finite map, the image of an irreducible germ is an irreducible germ of the same dimension. A holomorphic map with discrete fibres on a pure k-dimensional set has k-dimensional image (Remmert rank theorem). A finite open map between equidimensional manifolds pulls back a k-dimensional analytic germ to a k-dimensional germ.
- **A5 (local topology).**
  - An analytic germ has arbitrarily small connected representatives (conic structure theorem).
  - An irreducible curve germ has, in a small Milnor ball, an irreducible representative whose normalisation is a disc; distinct irreducible curve germs at a point meet only at the point in a small ball.
- **A6 (Krull).** If f is holomorphic on a pure k-dimensional analytic set and does not vanish identically on any local component at x, then {f = 0} has pure dimension k − 1 at x.
- **T1 (path lifting).** For a finite group acting on a Hausdorff space, every path in the orbit space lifts to a path starting at any prescribed preimage of its initial point (Bredon, *Introduction to Compact Transformation Groups*, II.6.2).
- **T2 (non-separation).** A closed subset of covering dimension ≤ n − 2 does not separate a connected n-manifold (Hurewicz–Wallman, *Dimension Theory*).

---

## GAPs

- **GAP-M (marking identification, precise form).** Lemma 5 (Steps 1, 2 and 6) and Lemma 6.1 use BB1 in the precise form BB1-M (§1). The requirements are:
  - (1) **one** lifted piece E^{m+1} over D^{m+1} serves at both ends of the travel interval;
  - (2) graph identifications ι′_m and ι_{m+1} under which Π′(β̃′_m ∖ 0) and Π″(β̃_{m+1} ∖ 0) both land in this E^{m+1};
  - (3) under these identifications, {x_m} ↦ c_{m+1} and {x_{m+1}} ↦ c_{m+1}, with x_{m+1} intact along β̃_{m+1} (and x_1 ↦ i at the start).

  BB1 only states "the chart labels correspond to c at both ends (x_m ↔ c ↔ x_{m+1})". BB1-M is my reading of that sentence, and it has never been written out with proof in the material. If BB1 is meant more weakly, the proof of Lemma 5 needs the missing part. The weaker reading has the correspondence only up to Aut(G(D^{m+1})), i.e. the two ends land on lifted pieces E and σE with labels c and σc, σ ∈ Aut(G(D^{m+1})). Then σE need not lie in 𝒲̃_0, and Step 5 can produce a sheet mapping into 𝒲̃ only for the label σ^{-1}-related to x_{m+1}.

  For product-type D^{m+1}, Aut(G) acts trivially on ∏M_w (Lemma PT, BB1), so E = σE and requirement (1) is automatic. Requirement (3) still needs the identification of the label.

- No other gaps. In particular:
  - (I1)–(I3) are Lemmas 2.3, 2.4 and 2.5;
  - the Φ-dichotomy is Proposition 3.1, which needs no exceptional set Z_Φ;
  - the existence of anchored sheets is the trivial germ argument of 0.7, so B1♭ is not needed;
  - the base is Lemma 6.1, and the endpoint is §6.

**Open (outside Theorem B):** (NRT_P) itself, and (Rig). By §6.2, under (Rig), (NRT_P) is equivalent to the problem's conclusion. A counterexample to it would need an automorphism of a puncture curve that exchanges a Φ-copy of Y_0 with a rigid Y_0-copy and is lost along Q_t.

=== END OF ANSWER extra_q3 ===

