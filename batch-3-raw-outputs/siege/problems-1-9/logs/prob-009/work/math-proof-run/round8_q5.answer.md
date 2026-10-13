# round8_q5: the twin step (TW) of MS8

**Status line.** Partial result. I prove (TW1) at a junction J, and (TW2) at Q_0, under a new hypothesis (U_J) (respectively (U_{Q_0})). This hypothesis is strictly weaker than (NT). It says: no curve of the deformed family near (J,0) has an automorphism that moves the tracked region x. The proof repairs the R7-6 continuity principle at J. Monodromy is handled by a finite covering. Non-uniformity near the junction is handled by comparing with the lifts of J(t) itself, for fixed t. I do not prove (TW) in general. The residual case is stated precisely in §6.

Plan:
1. State the chart-level readings.
2. Prove a covering lemma: under (U_J), squares lift modulo Γ_x.
3. Prove a separation lemma for τ-transport away from J.
4. Theorem A (TW1 under (U_J)).
5. Theorem B (TW2 under (U_{Q_0}) and an endpoint reading).
6. Residual analysis.

## 1. Set-up and readings

I adopt the task's readings (R1) and (R2), with H_0 = id, and the setting of MS8. I add the following conventions.

**(C1) Charts (standard; cited from memory).** Let J be a stable curve.
- Def(J) is its versal deformation germ. Aut(J) acts on it, and we may take the action to be linear in suitable coordinates (Cartan).
- Fix an Aut(J)-invariant open ball B ⊂ Def(J) around 0 and an Aut(J)-invariant Hermitian norm |·|. Then q : B → U := B/Aut(J) is a neighbourhood of J in M̄_g.
- On U use the quotient metric d̄(q(p), q(p')) = min_α |p − α p'|. It induces the topology of U. Every lift of a point realises the distance to the orbit of any other point.
- s_e (e ∈ E(G_J)) are the smoothing parameters. B° := B ∖ {∏ s_e = 0} lies over U ∩ M_g.
- For a vertex y, L_y := {s_e = 0 for all edges e at y}. It is closed, and F_y : L_y → M_{g_y,n_y}/S_{n_y} (coarse) is continuous (holomorphic into the coarse space).
- For α ∈ Aut(J): α L_y = L_{αy} and F_y(αp) = F_{α^{-1}y}(p) (K3 of R7-3).
- On product sets B × Δ_ε, the map q × id is again written q.

**(C2) The track at a junction (reading of Proposition K / (K\*) of R7-6 / the interpretation in R7-3 §1).** Let J = J^k be a junction between D := D^{k−1} and D' := D^k. Let β̃ ⊂ Def(J) and β̃' ⊂ Def(J) be lifts of the branches of D and D' at J, and let x be a chart vertex with:
- c_{k−1} = {x} along β̃, and c_k = {x} along β̃';
- c_{k−1} constant on D and c_k constant on D'.

Shrinking B, assume B_0 ∩ U is a finite union of branches through J (cone structure). Fix generic points z̃_1 ∈ β̃ ∖ 0 and z̃_2 ∈ β̃' ∖ 0, and put z_j = q(z̃_j). The track datum (TD_J) is: for every ρ > 0 there are a path γ : [a,b] → V_0 ∩ U and a continuous lift γ̃ : [a,b] → B° such that:
- (T1) |γ̃(a) − z̃_1| < ρ and |γ̃(b) − z̃_2| < ρ;
- (T2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_b = z_2;
- (T3) for every s with d̄(z_s, J) ≥ r_1 (r_1 > 0 arbitrary, fixed before ρ), there is a lift ẑ_s ∈ L_x of z_s with |γ̃(s) − ẑ_s| < ρ and F_x(ẑ_s) ≅ Y_0. One may take ẑ_a = z̃_1 and ẑ_b = z̃_2.

(T3) is the chart form of (K\*)(b): "Σ_i ↔ a single component of z_s of class Y_0". Here the region of γ̃(s) corresponding to Σ_i is the chart region x, which is constant along the continuous lift γ̃. Away from J the nearest lift of z_s is well defined up to the stabiliser, which is harmless; see Lemma 3. Proposition K yields (T1)–(T3) "modulo routine marking details" (PR-H). I have not re-proved Proposition K, and (TD_J) is the precise form in which I use it.

**(C3) The deformed family near J.**
- Put 𝒱_U := 𝒱 ∩ (U × Δ_ε) and ℬ° := B° × Δ_ε. Then q^{-1}(𝒱_U) ⊂ ℬ°.
- V_t is closed in M_g, so closure(𝒱) ∩ (M_g × Δ) = 𝒱.
- Let 𝒞° be the connected component of q^{-1}(𝒱_U) that contains γ̃ × {0}. Passing to a subsequence ρ_n → 0, it is the same for all the paths of (TD_J), because q^{-1}(𝒱_U) has finitely many components meeting a neighbourhood of 0. (I only use this for a single ρ at a time, so the subsequence is harmless.)
- Γ := {α ∈ Aut(J) : α𝒞° = 𝒞°}, and Γ_x := {α ∈ Γ : αx = x}.

**Fact 0.** q|_{𝒞°} : 𝒞° → 𝒜 := q(𝒞°) is the quotient map by Γ, and 𝒜 is a connected component of 𝒱_U.

*Proof.*
- q restricted to the saturated set q^{-1}(𝒱_U) is open and closed onto 𝒱_U. So q(𝒞°) is open, closed and connected, i.e. a component.
- If p, p' ∈ 𝒞° and q(p) = q(p'), then p' = αp for some α ∈ Aut(J). Then α𝒞° is a component of q^{-1}(𝒱_U) containing p', so α𝒞° = 𝒞°, i.e. α ∈ Γ. ∎

Let K ⊲ Γ be the kernel of the action of Γ on 𝒞°, i.e. the generic automorphisms of the family component. It is normal, so Γ_x^+ := K·Γ_x is a subgroup of Γ.

**Hypothesis (U_J).** After shrinking B and ε, every p ∈ 𝒞° satisfies Stab_Γ(p) ⊂ K·Γ_x.

(Generic twins, i.e. elements of K moving x, are thus allowed.)

In words: no curve of V_τ near J (|τ| < ε) in the family component 𝒜 has an automorphism, induced by an element of Aut(J), that maps the region x to a different region. Two remarks:
- (NT) at J (every σ ∈ Aut(J) fixes x) implies (U_J) trivially, since then Γ_x = Γ.
- (U_J) is a germ condition at (J, 0): it fails iff (0,0) ∈ closure(Fix(α) ∩ 𝒞°) for some α ∈ Γ ∖ KΓ_x.

## 2. The covering lemma: squares lift modulo Γ_x (proved)

**Lemma 1 (intermediate quotients).** Let a finite group G act on a Hausdorff, locally compact space X, and let H ≤ G. The natural map π : X/H → X/G is a local homeomorphism at the point Hp if and only if G_p ⊂ H. If this holds at every point, then π is a finite covering map over each connected component of X/G.

*Proof.*
- Since G is finite and X Hausdorff, p has a G_p-invariant open neighbourhood V with gV ∩ V = ∅ for g ∉ G_p.
- Then V/G_p → X/G and V/H_p → X/H are open embeddings, where H_p = G_p ∩ H. In these charts π is V/H_p → V/G_p, which is a homeomorphism iff H_p = G_p.
- π is closed with finite fibres, hence proper. A proper local homeomorphism between locally compact Hausdorff spaces is a covering over each component of the base (standard). ∎

**Lemma 2 (square lifting).** Assume (U_J). Let F : [a,b] × [0,1] → 𝒜 be continuous, and let F̂_0 : [a,b] → 𝒞° be a lift of F(·,0). Then:
- for every s, every lift μ_s : [0,1] → 𝒞° of F(s,·) with μ_s(0) = F̂_0(s), and
- every lift λ : [a,b] → 𝒞° of F(·,1) with λ(a) = μ_a(1),

satisfy λ(s) ∈ Γ_x · μ_s(1) for all s.

(Lifts of paths in 𝒞° exist for any initial point, by path lifting for finite group quotients: Bredon, *Introduction to compact transformation groups*, II.6.2, cited from memory.)

*Proof.*
- By Fact 0, 𝒜 = 𝒞°/Γ. By (U_J) and Lemma 1 (with H = K·Γ_x), π : 𝒞°/(KΓ_x) → 𝒜 is a covering.
- Let F̃ be the unique lift of F to 𝒞°/(KΓ_x) with F̃(a,0) = [F̂_0(a)] (homotopy lifting for coverings).
- Uniqueness of path lifts gives:
  - [F̂_0(s)] = F̃(s,0) for all s;
  - [μ_s(τ)] = F̃(s,τ) for all τ, since both are lifts of F(s,·) from [F̂_0(s)];
  - [λ(s)] = F̃(s,1), since both are lifts of F(·,1) from [μ_a(1)] = F̃(a,1).
- Hence λ(s) = kγ μ_s(1) with k ∈ K and γ ∈ Γ_x.
- Since K is normal and acts trivially on 𝒞°, kγ μ_s(1) = γ(γ^{-1}kγ)μ_s(1) = γ μ_s(1). So λ(s) ∈ Γ_x μ_s(1). ∎

We apply this with F(s,τ) := (H(γ(s), τt), τt) and F̂_0 := γ̃ × {0}.
- F takes values in 𝒱_U for |t| small: γ([a,b]) is a compact subset of U ∩ V_0, H is uniformly continuous, and H_0 = id.
- F takes values in 𝒜, because F([a,b]×[0,1]) is connected and contains γ × {0} ⊂ 𝒜.

## 3. τ-transport away from J (proved)

Fix 0 < r_1 small. Put B_0^{U} := B_0 ∩ U ∖ {J}. By the cone structure it is a finite union of punctured branches β_1, …, β_N.

Let 𝒵 be the set of connected components of q^{-1}(H(B_0^{U} × Δ_ε)). This set is finite:
- each H(β_j × Δ_ε) is connected;
- the components of its preimage are permuted transitively by Aut(J), as in Fact 0.

Each Z ∈ 𝒵 has a constant pinching pattern S(Z), because Z is connected and lies over a single stratum (R7-4 Lemma 2(a)).

**Lemma 3 (separation).** Fix t with |t| < ε/2. Let 𝔑 := q^{-1}(H((B_0^{U} ∖ {d̄(·,J) < r_1/2}) × [0,t])), where [0,t] := {τt : τ ∈ [0,1]}. Then:
- 𝔑 is compact;
- the sets 𝔑_Z := 𝔑 ∩ Z, Z ∈ 𝒵, are compact and pairwise disjoint;
- hence d'(r_1, t) := min_{Z ≠ Z'} dist(𝔑_Z, 𝔑_{Z'}) > 0.

*Proof.*
- The set (B_0 ∩ closure(U)) ∖ {d̄ < r_1/2} is compact; take U to be the image of a closed ball. Its image under the continuous H, intersected with times in [0,t], is compact, and q is proper. So 𝔑 is compact.
- 𝔑 ⊂ q^{-1}(H(B_0^U × Δ_ε)), in which each Z is closed. So 𝔑_Z is closed in 𝔑, hence compact.
- Distinct components are disjoint. ∎

**Corollary 3′ (τ-transport near the boundary).** Let s be such that d̄(z_s, J) ≥ r_1, and let ẑ_s ∈ Z_s ∈ 𝒵 be as in (T3). Let μ_s be a lift in 𝒞° of τ ↦ F(s,τ) from γ̃(s). Let ε_1 := ε_1(ρ) be such that d̄(X, z) < ρ implies d̄(H(X,τt), H(z,τt)) < ε_1 for all τ (uniform continuity of H; ε_1 → 0 as ρ → 0). If ρ < ε_1 < d'(r_1,t)/3, then:
- μ_s(1) lies within ε_1 of a point w ∈ Z_s that is a lift of H(z_s, t);
- w ∈ L_x;
- F_x(w) ∈ S_t, where S_t is the finite set defined in §4.

*Proof.*
- For each τ, the coarse distance between q(μ_s(τ)) = H(γ(s),τt) and H(z_s, τt) is < ε_1. So μ_s(τ) lies within ε_1 of some lift of H(z_s,τt), which lies in 𝔑 (for t small, H keeps z_s at distance ≥ r_1/2 from J(τt)).
- By Lemma 3, the Z for which dist(μ_s(τ), 𝔑_Z) < ε_1 is unique. It is locally constant in τ, hence constant.
- At τ = 0, μ_s(0) = γ̃(s) is within ρ < ε_1 of ẑ_s ∈ Z_s. So Z = Z_s for all τ, and at τ = 1 we get w ∈ Z_s, a lift of H(z_s,t), with |μ_s(1) − w| < ε_1.
- **w ∈ L_x.** The pattern S(Z_s) is constant, and ẑ_s ∈ L_x. So x is intact on Z_s, i.e. Z_s ⊂ L_x.
- **F_x(w) ∈ S_t.** Let D_s be the piece of the branch β_j ∋ z_s, and v the vertex of D_s that contains x along Z_s. Then v = {x}, since x is intact.
  - If v is constant on D_s, then F_x ≡ φ_v(t) on Z_s ∩ {time t}. This is Lemma 2 of R7-3 (transport of a lifted branch): Z_s is the set Ñ there.
  - Otherwise F_x(ẑ_s) ≅ Y_0 says that z_s ∈ Sp_J, the finite set defined in §4. Then F_x(w) is the class of a component of H(z_s,t). ∎

## 4. Theorem A: no twin jump at J under (U_J) (proved, given (TD_J))

**The finite set S_t.** Let Sp_J be the set of points z ∈ B_0^U such that some vertex v that is non-constant on the piece through z has a value ≅ Y_0 at z. Sp_J is finite: f_v extends to the compact normalisation Ē of each of the finitely many pieces meeting U, and f_v^{-1} of the finitely many relabellings of Y_0 is finite. Then S_t ⊂ M_{g_i,n_i}/S_{n_i} is the finite union of:
- the values φ_v(t) of all constant vertices v of type (g_i,n_i) of the finitely many pieces with a branch in B_0^U;
- the classes of all type-(g_i,n_i) components of H(z,t), for z ∈ Sp_J;
- the classes of all type-(g_i,n_i) components of J(t) := H(J,t).

Let 2ε'(t) > 0 be the minimum distance between distinct elements of S_t (put ε'(t) = 1 if |S_t| = 1). Note that S_t does not depend on r_1.

**Theorem A.** Assume the setting of MS8, the readings (R1), (R2), (C1)–(C3), the track datum (TD_J), and (U_J). Then φ_{c_{k−1}} ≡ φ_{c_k} on Δ.

Hence, if (TD_J) and (U_J) hold at every junction J^1, …, J^m of the chain, then φ_{c_k} ≡ Y for every k, i.e. (TW1) holds. This is by induction from c_0 = i, with φ_i = Y.

Theorem A uses neither (Rig) nor the non-constancy of Y.

*Proof.* By the identity theorem (φ_c is holomorphic: R7-3 Lemma 1), it suffices to prove φ_{c_{k−1}}(t) = φ_{c_k}(t) for all t ≠ 0 in a small disc Δ_{t_0}. Here t_0 is chosen so that, for |t| < t_0, F(s,τ) := (H(γ(s), τt), τt) stays in 𝒱_U for every path of (TD_J) (uniform continuity of H on the compact closure(V_0) ∩ closure(U)). Fix such a t ≠ 0.

**Choice of constants.**
- Let d_J(t) > 0 be the minimum distance in B between distinct lifts of J(t). (The lifts form one finite Aut(J)-orbit.)
- Let ω_H be a modulus of continuity of z ↦ H(z, τt) on closure(B_0 ∩ U), uniform in τ ∈ [0,1].
- Let ω_F be a modulus of continuity of F_x on the compact set L_x ∩ closure(B).
- Choose r_1 > 0 with:
  - r_1 < min(d̄(z_1,J), d̄(z_2,J));
  - r_2 := 2ω_H(r_1) < d_J(t)/4;
  - ω_F(3r_2) < ε'(t).
- Then choose ρ so small that ρ < ε_1(ρ) < min(ω_H(r_1), d'(r_1,t)/3) (Lemma 3, Corollary 3′).
- Take γ, γ̃, z_s, ẑ_s from (TD_J) for this ρ, and define F as above.

**Lifts.**
- For each s, let μ_s be a lift in 𝒞° of F(s,·) from γ̃(s).
- Let λ be a lift in 𝒞° of F(·,1) from μ_a(1).
- By Lemma 2, for every s there is κ_s ∈ Γ_x with λ(s) = κ_s μ_s(1). Take κ_a = id.

**The class function.** For each s choose u(s) ∈ L_x with |λ(s) − u(s)| < r_2 and F_x(u(s)) ∈ S_t, as follows.
- *Regime (ii): d̄(z_s, J) ≥ r_1.*
  - Corollary 3′ gives w_s ∈ L_x, a lift of H(z_s,t), with |μ_s(1) − w_s| < ε_1 and F_x(w_s) ∈ S_t.
  - Put u(s) := κ_s w_s. The norm is Aut(J)-invariant, so |λ(s) − u(s)| = |μ_s(1) − w_s| < ε_1 < r_2.
  - Since κ_s x = x, we have u(s) ∈ L_{κ_s x} = L_x and F_x(u(s)) = F_{κ_s^{-1}x}(w_s) = F_x(w_s) ∈ S_t.
  - **This is the only place where (U_J) is used.** Without it κ_s^{-1}x could be a twin region, which need not be intact at w_s or could carry a different value.
- *Regime (i): d̄(z_s, J) < r_1.*
  - d̄(q λ(s), J(t)) ≤ d̄(H(γ(s),t), H(z_s,t)) + d̄(H(z_s,t), H(J,t)) < ε_1 + ω_H(r_1) ≤ r_2.
  - So some lift ĵ(s) of J(t) has |λ(s) − ĵ(s)| < r_2 < d_J(t)/4, and it is unique.
  - Lifts of J(t) lie in {s_e = 0 for all e} ⊂ L_x. Put u(s) := ĵ(s); then F_x(u(s)) is the class of a component of J(t), so it lies in S_t.

Put c(s) := F_x(u(s)) ∈ S_t.

**Near-continuity.**
- λ is uniformly continuous, so there is δ > 0 with |λ(s) − λ(s')| < r_2 whenever |s − s'| < δ.
- For such s, s' we get |u(s) − u(s')| < 3r_2, with both points in L_x ∩ closure(B). Hence d(c(s), c(s')) ≤ ω_F(3r_2) < ε'(t).
- Since c takes values in S_t, whose distinct elements are ≥ 2ε'(t) apart, c(s) = c(s') whenever |s − s'| < δ. So c is constant on [a,b].

**Endpoints.**
- At s = a: z_a = z_1, so we are in regime (ii), and w_a lies in the component Z_a ∈ 𝒵 containing ẑ_a = z̃_1 ∈ β̃. This component is the set Ñ of R7-3 Lemma 2 for (D, c_{k−1}, x), on which F_x ≡ φ_{c_{k−1}}(t). With κ_a = id, c(a) = φ_{c_{k−1}}(t).
- Likewise c(b) = F_x(w_b) with w_b ∈ Z_b ∋ z̃_2 ∈ β̃'. So c(b) = φ_{c_k}(t).
- Hence φ_{c_{k−1}}(t) = φ_{c_k}(t). ∎

**Remarks on Theorem A.**
1. **Which gap of R7-6 this repairs.**
   - *(Monodromy.)* R7-6 transported markings along the 2-parameter square without controlling branch points. Under (U_J), the only branch points of 𝒞° → 𝒜 have stabilisers fixing x. These are invisible in the covering 𝒞°/Γ_x, which is exactly the object the labels live on.
   - *(Uniformity near J.)* R7-6 needed charts of the boundary points z_s to have size ≫ ε uniformly, which fails as z_s → J. Here, for z_s within r_1 of J, I compare with the lifts of J(t) themselves. They are separated by d_J(t) > 0 because t is fixed first, and all regions are intact at them. The two regimes are glued by the continuity of F_x on L_x.
   - The order of choices (t, then r_1, then ρ) is essential. This is possible because the identity theorem only needs the equality for each fixed small t, and (TD_J) provides tracks for every ρ.
2. **The twin jump of R7-3 §5 is exactly a monodromy phenomenon.** In the proof, every step except the line marked in regime (ii) holds without (U_J). So a twin jump at J (φ_{c_{k−1}} ≢ φ_{c_k}) forces: for a sequence ρ → 0 (with t fixed), some κ_s ∉ Γ_x. That means a nontrivial lift-monodromy of the square F in 𝒜, coming from points of 𝒞° whose stabiliser moves x. This is the precise content of the planner's sketch, step 5(b).
3. **Relation to (Lock).** If (Lock) holds at J (R7-1), then φ_{c_{k−1}} ≡ φ_{c_k} by R7-1 Step 2. So at each junction it suffices to have **(U_J) or (Lock_J)**.
   - In the quintic example (PR-I; not smooth, so only a test case), the twins A, C at P_0 = Y_0 — B_0 — Y_0 are exchanged by automorphisms of interior curves. These are the covers of the configurations (a_1, a_2, 1, 1/a_1, 1/a_2), whose involution x ↦ 1/x lifts because all local monodromies are equal.
   - So there (U) fails, while (Lock) holds. This is a sketch; I did not check which component 𝒞° the track uses.

## 5. Theorem B: the terminal point (TW2) under (U_{Q_0})

**Endpoint datum (TD_Q).** Let Q_0, the last STAY piece D := D^m and its lift β̃ with c_m = {x}, and the terminal branch b with a lift b̃ ⊂ Def(Q_0) be as in Proposition K. So either:
- (MERGE) some edge at x is unpinched along b̃; or
- (puncture-MOV) every edge at x is pinched along b̃, F_x is non-constant along b̃, and Q_0 ∉ Δ_{G_b}.

Fix generic z̃_1 ∈ β̃ ∖ 0 and a point z̃_b ∈ b̃ ∖ 0, with z_b = q(z̃_b). (TD_Q) asks that for every r_1 > 0 small and every ρ ≤ ρ_0(r_1) there are γ : [a,e] → V_0 ∩ U and a lift γ̃ such that:
- (TQ1) |γ̃(a) − z̃_1| < ρ and |γ̃(e) − z̃_b| < ρ;
- (TQ2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_e = z_b;
- (TQ3) with s_* := sup{s : d̄(z_s, Q_0) ≤ r_1}: (T3) holds for every s < s_* with d̄(z_s, Q_0) ≥ r_1.

The point z_b is FIXED, independent of ρ. This is the difference from (K\*)(c) of R7-6, where the merge witness Q′ satisfies d(Q′, Q_0) < ρ.
- **Where it comes from (sketch, not proved).** In the proof of Proposition K, fix k and let n → ∞. The ray endpoints converge to Q_k ∈ b ∖ {Q_0}, which is at a fixed distance from Q_0. Then take z_b := Q_k.
- The price is that along the track ∂Σ_i is only Ext-short (Ext ≤ δ_k), not pinched. So (T3) holds only approximately: there is a lift with |s_e| ≤ σ_k for the edges at x, where σ_k → 0 as k → ∞.
- In regime (ii) this suffices, after choosing k large depending on r_1. On the compact part {d̄(·, Q_0) ≥ r_1/2} of the finitely many lifted branches along which x is merged, some |s_e| with e at x is bounded below by m(r_1) > 0, since s_e is a holomorphic function on the branch vanishing only at the centre. So once σ_k + ρ < m(r_1)/2, the nearby boundary lift has x intact.
- I record this as the reading (TD_Q). Its derivation from Proposition K is a sketch.

Define Γ, Γ_x, 𝒞° and (U_{Q_0}) at Q_0 exactly as in (C3), with the track of (TD_Q).

**Theorem B.** Assume the setting of MS8, (R1), (R2), (C1)–(C3) at Q_0, (TD_Q) and (U_{Q_0}). Assume also φ_{c_m} ≡ Y (for instance from Theorem A at all junctions). Then for every t in a disc Δ_{t_0}, with t ≠ 0, there are:
- a lift Q̂ of Q(t) := H(Q_0, t) with F_x(Q̂) ≅ Y_t, and
- a lifted branch Z′ of b_t := H_t(b) through Q̂ (i.e. Q̂ ∈ closure(Z′)),

such that:
- (MERGE) some edge at x is unpinched along Z′; or
- (puncture-MOV) every edge at x is pinched along Z′, and F_x is non-constant along Z′ for t outside a countable set.

In particular (TW2) holds, and by R7-4 Lemma 1 (= R7-1 Lemma 1) the MS6 configuration exists at every such t.

*Proof.* Fix t as in Theorem A. Use the same constants, with J replaced by Q_0, plus two more:
- Let 𝒵_b be the finite set of connected components of q^{-1}(H_t(b ∩ U ∖ {Q_0})). The set H_t(b ∩ U ∖ Q_0) is connected, being the image of a punctured disc.
- For a lift Q̂ of Q(t), let η_1(t) > 0 be the minimum, over all lifts Q̂ and all Z′ ∈ 𝒵_b with Q̂ ∉ closure(Z′), of dist(Q̂, closure(Z′)). It is positive because there are finitely many compact closures.
- Shrink r_1 so that also 2r_2 < η_1(t). Shrink ρ so that ε_1 < d″/3, where d″ > 0 is the minimum distance between the compact sets closure(Z′) ∩ q^{-1}(H_t(b ∩ U ∩ {d̄(·,Q_0) ≥ r_1/2})), Z′ ∈ 𝒵_b. Also require that distinct branches of B_0 in the closed annulus {r_1/2 ≤ d̄(·,Q_0) ≤ r} are > 2ρ apart.

**Step 1 (class function up to s_*).** Run the proof of Theorem A on [a, s_*]. Regime (ii) uses (TQ3) and (U_{Q_0}); regime (i) uses the lifts of Q(t), separated by d_Q(t).
- This gives c constant on [a, s_*], with c(a) = φ_{c_m}(t) = Y_t.
- At s_* we have d̄(z_{s_*}, Q_0) ≤ r_1, i.e. regime (i). So the unique lift Q̂ of Q(t) with |λ(s_*) − Q̂| < r_2 satisfies F_x(Q̂) = c(s_*) = Y_t.

**Step 2 (after s_*, the track follows b).**
- For s ∈ (s_*, e] we have d̄(z_s, Q_0) > r_1. Consider z_s inside the annulus where the branches are separated. Since γ is continuous and d̄(γ(s), z_s) < ρ, the branch carrying z_s is locally constant. It equals b, because z_e = z_b ∈ b.
- (If z_s leaves the annulus outward, it is no longer near Q_0, and the same argument applies with U large enough to contain b up to z_b.)

**Step 3 (time t).**
- For s ∈ [s_*, e], λ(s) is within ε_1 of a lift of H(z_s, t) with z_s ∈ b and d̄(z_s, Q_0) ≥ r_1. That lift lies in some Z′ ∈ 𝒵_b.
- By the d″-separation, this Z′ =: Z′_* is the same for all s ∈ [s_*, e].
- At s = e: λ(e) = κ_e μ_e(1) with κ_e ∈ Γ_x (Lemma 2). As in Corollary 3′, μ_e(1) is within ε_1 of a point w_e of the component Z_b of q^{-1}(H((b∖Q_0) × Δ_ε)) that contains z̃_b. So λ(e) is within ε_1 of κ_e w_e ∈ κ_e Z_b.
- κ_e w_e lies in some component of 𝒵_b contained in (κ_e Z_b)_t. By d″-separation it is Z′_*. Hence Z′_* ⊂ κ_e Z_b.
- The pattern of κ_e Z_b is κ_e S(b̃), and κ_e x = x.
  - (MERGE) An edge at x is unpinched along b̃, so the edge κ_e(e_0) at x is unpinched along κ_e Z_b ⊃ Z′_*.
  - (MOV) All edges at x are pinched along κ_e Z_b. Also F_x(κ_e p) = F_x(p) for p ∈ Z_b. By R7-3 Lemma 1(b), F_x is non-constant on the time-t transport of the piece of b for t outside a countable set (the identity theorem on Ē gives non-constancy on each of its branches). Hence F_x is non-constant along Z′_* for such t.

**Step 4 (Q̂ lies on Z′_*).**
- λ(s_*) is within r_2 of Q̂ and within ε_1 of Z′_*. So dist(Q̂, Z′_*) < r_2 + ε_1 < 2r_2 < η_1(t).
- Therefore Q̂ ∈ closure(Z′_*). Put Z′ := Z′_*. ∎

**Corollary C (MS8 under (U), modulo the readings).** Assume:
- the setting of MS8 with (Rig);
- (TD_J) and [(U_J) or (Lock_J)] at every junction;
- (TD_Q) and (U_{Q_0}) at the terminal point;
- that the terminal branch is MERGE or puncture-MOV.

Then Y_t = Y_0 for all t.

*Proof.*
- Theorem A, or R7-1 Step 2 under (Lock), gives φ_{c_m} ≡ Y.
- Theorem B gives, for all t in a punctured disc outside a countable set, a non-constant vertex u of a piece E at time t and a puncture p with Y_t a component of f_u(p) (R7-4 Lemma 1). Here u = [x] in the MERGE case and u = {x} in the MOV case.
- By (Rig), puncture values of non-constant vertices lie in the finite set F, so Y_t is a component of an element of F for uncountably many t accumulating at 0.
- t ↦ Y_t is holomorphic (PR-A), so it is constant. ∎

## 6. The residual case: what a twin jump requires (partly proved, partly open)

**Proposition D (necessary conditions for a twin jump; proved, given (TD_J)).** Suppose φ_{c_{k−1}} ≢ φ_{c_k} at the junction J. Then:
- (a) (Lock_J) fails, and (U_J) fails. So there is α ∈ Γ ∖ KΓ_x (in particular αx ≠ x, and α is not a generic automorphism of the family) with (0,0) ∈ closure(Fix(α) ∩ 𝒞°): curves of V_τ near J, with |τ| arbitrarily small, have an automorphism (induced by α ∈ Aut(J)) that exchanges the tracked region x with a different region αx.
- (b) Let Φ be an irreducible component, through (0,0), of the analytic germ Fix(α) ∩ closure(𝒞°) ⊂ Def(J) × Δ that is not contained in {∏ s_e = 0}. One of the following holds:
  - **(A)** Φ ∩ {τ = 0} contains points of B° near 0, arbitrarily close to 0. That is: curves of V_0 itself, arbitrarily close to J, admit an automorphism (from Aut(J) acting on Def(J)) that moves x.
  - **(B)** Φ ∩ {τ = 0} ⊂ {∏ s_e = 0} and has dimension ≥ 1. That is: some lifted branch of B_0 at J (lying in closure(𝒞°)) is fixed pointwise by α. Then every boundary point of V_0 on that branch has an automorphism exchanging the components (or merged vertices) containing x and αx.
  - **(C)** dim Φ = 1 and Φ ∩ {τ = 0} = {(0,0)}. That is: there is a holomorphic arc τ ↦ C_τ ∈ V_τ (after a base change τ = σ^k) of smooth curves with automorphism α, converging to J as τ → 0. This is invisible at t = 0.

*Proof.*
- (a) is the contrapositive of Theorem A, together with R7-1 Step 2 for (Lock). For the germ reformulation of (U_J), see (C3).
- (b) closure(𝒞°) is a 3-dimensional analytic set. It is the closure of a connected component of the preimage of the 3-dimensional manifold 𝒱 (R1); closures of unions of components of q^{-1}(𝒱_U) are analytic, as in R7-4 Lemma 2(c). Fix(α) = Fix_{Def(J)}(α) × Δ is a smooth submanifold (linear action). So Fix(α) ∩ closure(𝒞°) is analytic, and Φ has dimension 1, 2 or 3.
  - **dim 3.** Then α fixes 𝒞° pointwise, i.e. α ∈ K ⊂ KΓ_x, contradicting the choice of α. So this case does not occur.
  - **dim Φ ≥ 2.** Φ ∩ {τ = 0} has dimension ≥ 1 at (0,0) (Krull, if τ ≢ 0 on Φ; trivially otherwise). It lies in closure(𝒞°) ∩ {τ=0} ⊂ q^{-1}(closure(V_0) ∩ U), by (R2): H commutes with closures and H_0 = id. Either it meets B° arbitrarily close to 0, giving (A), or it lies in the boundary, giving (B).
  - **dim 1.** If Φ ⊂ {τ = 0}, then Φ ∖ (0,0) consists of interior points of V_0's lift, giving (A). Otherwise τ|_Φ is finite at (0,0), and since Φ ⊄ {∏s_e = 0}, Φ ∖ (0,0) ⊂ B° × Δ near (0,0) (a proper analytic subset of an irreducible curve germ is the point). This is (C), with the normalisation of Φ giving the base change. ∎

**How this relates to the planner's dichotomy (step 5(b) of the sketch, and the "named approach").**
- The first alternative, "Fix(α) ∩ 𝓛 stays away from the region swept by the transported paths", is (U_J). Under it, Theorem A makes R7-6's argument rigorous at J.
- The second alternative, "the closure of the fixed locus meets the boundary at points J′_τ near J_τ at which α exchanges two components both ≅ Y_τ", is **not** forced by the analysis above. In case (C), Φ meets the boundary only at (0,0). In case (B), it meets it only at τ = 0.
- Even when Φ ∩ {∏s_e = 0} contains an arc Ψ with τ|_Ψ non-constant, the point ψ(τ) ∈ Ψ may be:
  - a lift ĵ(τ) of J(τ). Then F_x(ĵ(τ)) = F_{αx}(ĵ(τ)): the twins are locked at that particular lift, which is a pointwise form of (Lock).
  - a point of a lifted transported branch Z. Then only the components x, αx of that boundary point are exchanged.

  In neither case did I find a way to show that the monodromy κ of the square (a product of conjugates of such α's) fixes the class F_x on the transported D'-branch. Heuristically (this is not a construction), the R7-3 §5 local model, completed by an interior 3-fold, is compatible with (C). Take Def coordinates (a, b) for the two twin components with σ(a,b) = (b,a), and let 𝒞̄ be any irreducible 3-fold containing both transported branches and meeting Fix(σ) = {a = b} in a curve through (0,0) only.

So the chart-plus-interior-local analysis does not exclude (C) either. Any proof of (TW) must use total geodesy at t = 0, or global information, to exclude (A), (B) and (C) at a twin junction, or to show that they force (Lock).

**Remark (where total geodesy could enter, not carried out).** In case (A), the lift of V_0 and Fix(α) are both totally geodesic in T_g. Fix(α) is the image of the Teichmüller space of the quotient orbifold, a holomorphic isometric embedding. So their intersection near the lift of J is a totally geodesic subvariety of V_0 consisting of α-symmetric curves, whose closure contains J. One would want to show that such a sub-locus forces the twins x, αx to stay isomorphic at J(τ) under every deformation satisfying (i), (ii). That would be a (Lock) statement, and it is the natural next target. I have no proof.

## 7. Summary: proved / not proved / open

**Proved** (modulo the cited standard facts: versal deformations and linearisation of Aut(J), path lifting for finite quotients, covering-space theory, the analytic-set facts used in R7-3/R7-4; and the earlier lemmas R7-3 Lemmas 1–2, R7-1 Lemma 1/Step 2, PR-A, which I re-used but did not re-prove):
1. Lemma 1 (intermediate quotients) and Lemma 2 (square lifting modulo Γ_x under (U_J)).
2. Lemma 3 and Corollary 3′: τ-transport of the track is controlled uniformly away from J.
3. **Theorem A:** given the track datum (TD_J) and (U_J), there is no twin jump at J: φ_{c_{k−1}} ≡ φ_{c_k}. Hence (TW1) holds if every junction satisfies (U_J) or (Lock_J). This needs neither (Rig) nor non-constancy of Y. It repairs both gaps flagged in R7-6, monodromy and non-uniformity near junctions, under (U_J).
4. **Theorem B:** given the endpoint datum (TD_Q), (U_{Q_0}) and φ_{c_m} ≡ Y, (TW2) holds for MERGE and puncture-MOV terminals. **Corollary C:** with (Rig), Y_t = Y_0 under these hypotheses.
5. **Proposition D:** a twin jump at J forces the failure of (Lock_J) and (U_J), and one of the three configurations (A), (B), (C) of automorphisms exchanging the tracked region with a twin.

(U_J) is strictly weaker than (NT): it only forbids twin-exchanging automorphisms of nearby smooth curves of the deformed family, not automorphisms of J itself. So Theorems A and B are new partial results. By the task's rules they do **not** answer (TW) in general.

**Not proved / readings used:**
- (TD_J) and (TD_Q) are chart-level readings of Proposition K. (TD_J) is the content of (K\*) of R7-6 ("modulo routine marking details", not re-verified).
- (TD_Q) additionally needs a merge witness at a fixed point of b. This comes from Proposition K at fixed k, with approximate pinching. That derivation is only sketched in §5.
- The interior-MOV terminal is not treated (another query covers it).

**Open:**
- (O1) Can configurations (A), (B) or (C) of Proposition D occur at a twin junction of a smooth, closed, totally geodesic V_0 (or of its deformation), with (Lock_J) failing? A negative answer proves (TW1), and with (U_{Q_0}) also (TW2).
- (O2) In case (A), does the totally geodesic locus V_0 ∩ Fix(α) of α-symmetric curves accumulating at J force (Lock) for the twins x, αx under all admissible deformations?
- (O3) Case (C) (α-symmetric smooth curves of V_τ converging to J only as τ → 0) is invisible at t = 0. Is it excluded by (R2) and (i), (ii), or must it be handled by a global argument?
- (TW) in general remains open. In particular I have neither a proof nor a counterexample. A counterexample would need a twin junction realising (A), (B) or (C) with nontrivial square monodromy, on a smooth totally geodesic V_0.

=== END OF ANSWER round8_q5 ===

