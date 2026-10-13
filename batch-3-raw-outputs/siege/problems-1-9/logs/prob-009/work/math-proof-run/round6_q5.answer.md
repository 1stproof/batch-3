# round6_q5 — answer

## 0. Summary of results

- **Obs. 1 (proved).** In (H) and MS5 the stratum G can never be Γ. So a valid witness needs a 1-dimensional piece of closure(V_0) in a stratum Δ_G with G ≠ Γ, whose closure meets closure(∂V_0).
- **Prop. 2 (counterexample to (H) and MS5, except for one hypothesis).** Take the cyclic quintic family V_0 = {y^5 = ∏_{j=1}^5 (x − a_j)} ⊂ M_6.
  - It satisfies every hypothesis of MS5 except possibly smoothness of V_0. That hypothesis is not verified, and I believe it fails in the orbifold sense at the Fermat quintic.
  - For this V_0, (H) and MS5 are both false: every 1-dimensional boundary piece of closure(V_0) lies in Δ_Γ.
  - Consequences:
    - Any proof of (H) must use the smoothness of V_0 in an essential way, or (H) is false.
    - The clause "for every vertex u with a component isomorphic to Y_0" in (T0) and MS5 is exactly what breaks. The witness that does exist in this example is the twin configuration of PR-G.
- **Prop. 3 (proved, modulo standard cited facts).** Let Δ_G be any stratum, E a 1-dimensional piece of closure(V_0) ∩ Δ_G, and U ⊂ E a nonempty open set. Then at some point of U, lying on no other component, some sequence of generating pairs gives some vertex of G positive area.
  - With G = Γ this is hypothesis (PA) of PR-F, which was open there.
  - So Prop. C of PR-F holds unconditionally: some vertex j ≠ i of Γ has π_j(∂V_0-piece) an orbifold-unramified Teichmüller curve.
  - More generally, every 1-dimensional boundary piece of closure(V_0) has at least one Teichmüller-curve factor (Lemma T′).
- **Open.** The merge clause of (H) for general smooth V_0. Section 4 says where it breaks and proposes a corrected target, MS5′.

Readings used throughout:
- closure(V_0) is algebraic, so closure(V_0) \ V_0 is an analytic set of dimension ≤ 1. This is (R1) at t = 0.
- Everything is done on orbifold charts or level covers, as in PR-D and PR-F.

---

## 1. Observation 1: G = Γ never works

**Obs. 1.** Let Δ_G = Δ_Γ and P_0 ∈ closure(∂V_0). Some 1-dimensional component E^{(a)} of closure(V_0) ∩ Δ_Γ = ∂V_0 has P_0 in its closure. Some lift R of P_0 in 𝐂^{(a)} has R_i = Y_0, which is smooth. Hence (a) fails for u = i, and with this G both (H) and MS5 fail.

*Proof.*
1. P_0 ∈ closure(∂V_0), and closure(∂V_0) is the union of the closures of the finitely many 1-dimensional components of ∂V_0. So P_0 ∈ closure(E^{(a)}) for some a.
2. ξ_Γ^{-1}(E^{(a)}) ⊂ {Y_0} × ∏_{j≠i} M_j. Its closure 𝐂^{(a)} lies in {Y_0} × ∏_{j≠i} M̄_j.
3. A lift R ∈ 𝐂^{(a)} of P_0 exists by compactness: take a limit of lifts of points of E^{(a)} that tend to P_0.
4. R_i = Y_0 is smooth and contains Y_0. ∎

(When P_0 is not on any 1-dimensional piece of the chosen Δ_G, (H) as literally written is vacuously true. MS5 rules this out by requiring P_0 ∈ closure(E^{(a)}) \ E^{(a)} for some a, and this reading of (H) is used below.)

---

## 2. Proposition 2: the quintic family

**Setting.**
- For a = (a_1, …, a_5) ∈ M_{0,5}, let X_a be the smooth projective model of y^5 = ∏(x − a_j).
- This is a Z/5-cover of P^1, totally ramified over the five a_j and unramified over ∞, since 5 | deg. By Riemann–Hurwitz, 2g − 2 = 5·(−2) + 5·4 = 10, so g = 6.
- Let Φ : M_{0,5} → M_6 be the induced map and V_0 := Φ(M_{0,5}).
- All weights are equal, so Φ is S_5-invariant.

**Standard facts used (cited from memory).**
- (C1) V_0 is totally geodesic. The covering construction induces an isometric holomorphic embedding T_{0,5} → T_6: pull-backs of quadratic differentials give Teichmüller maps.
- (C2) Φ extends to Φ̄ : M̄_{0,5} → M̄_6, sending a stable 5-pointed curve to the stable model of its unique admissible Z/5-cover (Harris–Mumford). Hence closure(V_0) = Φ̄(M̄_{0,5}), and V_0 is closed in M_6, because Φ̄ maps ∂M̄_{0,5} into ∂M̄_6.
- (C3) For an admissible Z/5-cover, the local monodromy at a node, seen from either side, is the negative of the sum of the weights on that side.
- (C4) Φ̄ is finite on each D̄_{ab}: a Z/5-cover with its group action determines its branch data.

**Boundary computation.**
- *D_{12}°.* The base is A ∪ M, where:
  - A carries a_1, a_2, q, with weights (1, 1, 3);
  - M carries a_3, a_4, a_5, q, with weights (1, 1, 1, 2), the sum on M being 0 mod 5.
- *Cover over A.* All weights are prime to 5, so it is connected and totally ramified at 3 points, with 2g − 2 = −10 + 12 = 2. So g = 2, with a single point over q. Call this 1-pointed curve Y_0 ∈ M_{2,1}. It is the curve y^5 = x(x − 1), marked at the point over ∞, and it is independent of a.
- *Cover over M.* It is connected, with 2g − 2 = −10 + 16 = 6, so g = 4, and it has a single point over q. It varies with the cross-ratio, and is non-constant by (C4).
- Hence Φ̄(D_{12}°) ⊂ Δ_Γ, where Γ has a genus-2 vertex i and a genus-4 vertex, joined by one edge, and n_i = 1.
- Δ_Γ ≅ M_{2,1} × M_{4,1} is of product type: the two vertices have different genera.
- π_i ≡ Y_0 on Φ̄(D_{12}°), and dim M_{2,1} = 4 > 0.
- By S_5-symmetry, Φ̄(D_{ab}°) = Φ̄(D_{12}°) for all pairs {a, b}.

**The set closure(V_0) \ V_0.**
- It equals ∪ Φ̄(D̄_{ab}) = ∂V_0 ∪ Φ̄(corners), where ∂V_0 = Φ̄(D_{12}°) is 1-dimensional.
- The 15 corners D_{ab} ∩ D_{cd} form one S_5-orbit, so they all map to one point P_0.
- *Computing P_0* (corner D_{12} ∩ D_{34}). The base is a chain A – B – C:
  - A carries a_1, a_2, q, weights (1, 1, 3);
  - B carries q, a_5, q′, weights (2, 1, 2);
  - C carries a_3, a_4, q′, weights (1, 1, 3).
- All three covers are connected, totally ramified at 3 points, and of genus 2. So P_0 is a chain Ŷ – W – Ŷ′, where:
  - Ŷ ≅ Ŷ′ ≅ Y_0 as 1-pointed curves, since they have identical branch data;
  - W ∈ M_{2,2}.
- The genera add up: 2 + 2 + 2 = 6.

**Claim.** In this example there are no Δ_G and P_0 satisfying MS5, and none satisfying (H) in its non-vacuous reading.

*Proof.*
1. The 1-dimensional pieces of closure(V_0) ∩ Δ_G, over all strata G ≠ {M_6}, are contained in closure(V_0) \ V_0 = ∂V_0 ∪ {P_0}. So the only stratum carrying a 1-dimensional piece is Δ_Γ.
2. By Obs. 1, G = Γ fails (a).
3. Concretely, the only admissible point is P_0 = Ŷ – W – Ŷ′, and its lift along ∂V_0 is R = (Ŷ, W ∪ Ŷ′), with R_i = Ŷ ≅ Y_0 smooth. ∎

**Status of the hypotheses for this example.**
- Verified: closed in M_6, 2-dimensional, totally geodesic, dim ∂V_0 = 1, π_i(∂V_0) = {Y_0}, Δ_Γ of product type, dim M_{2,1} > 0.
- **Smoothness is not verified, and probably fails in the orbifold sense.**
  - The Fermat quintic x^5 + y^5 = 1 lies on V_0. It carries two distinct Z/5-subgroups of this branching type (x ↦ ζx and y ↦ ζy).
  - So in an orbifold chart at that point, the preimage of V_0 contains two distinct smooth surfaces Fix(H_x) and Fix(H_y).
  - Whether the coarse image is a smooth surface I have not settled. M_{0,5}/S_5 has quotient points, for instance at configurations with Z/4 symmetry.
- So Prop. 2 is a counterexample to (H) and MS5 only under a reading of "smooth" that this V_0 meets. Under the strict orbifold reading it is not a valid counterexample.
- Even so, every boundary hypothesis that (H) and MS5 refer to holds here. Any proof of (H) must therefore use interior smoothness of V_0, which seems unlikely to bear on boundary combinatorics. **My assessment: (H) and MS5, as stated, are false in spirit, and the chain needs a corrected target (Section 4).**

**What survives in this example (the twin mechanism of PR-G).**
- At P_0, closure(∂V_0) has two branches through the corner D_{12} ∩ D_{34}:
  - β, the image of D_{12}, with lift (Ŷ, W ∪ Ŷ′);
  - b, the image of D_{34}, with lift (Ŷ′, Ŷ ∪ W).
- On b, the β-specialization Ŷ of vertex i is merged into the genus-4 vertex. That vertex is the Teichmüller-curve factor: it carries positive area, by pull-back of base differentials as in PR-F Prop. 5.1.
- So a *component-tracking* version of (T0) holds at t = 0.
- The two lifts coincide as points of M̄_{2,1} × M̄_{4,1}: W has an involution swapping its two node points, lifting the involution of B that fixes a_5 and swaps q and q′ (they carry equal weights). So Aut(P_0) swaps Ŷ and Ŷ′, and PR-G's hypothesis (M2) fails.
- Transport to t ≠ 0 therefore cannot decide which end of the chain P_t is Y_t.
- Lemma R pins the genus-4 closure K_0 and hence the limit Z_t = Z_0 = [W ∪ Ŷ′]. So P_t = Y_t – W – Y_0. Nothing proved so far forces Y_t = Y_0.
- **This example is an open test case for the original problem itself.** Neither Theorem P nor any statement of type (H) or MS5 decides it.

---

## 3. Proposition 3: positive area at generic boundary points (proof of (PA))

**Cited standard facts (from memory).**
- (D1) **Duality.** For [μ] ∈ T_X T_g, the Teichmüller norm is ‖[μ]‖_T = sup_{q ∈ Q(X), ‖q‖_1 = 1} Re ∫_X qμ.
  - The supremum is attained at the unique unit-norm q_v whose Teichmüller disc is tangent to C·[μ] (Teichmüller's theorem; the extremal Beltrami is k·q̄_v/|q_v|).
  - The pairing depends only on the class [μ].
- (D2) **Wolpert's lemma.** For a K-quasiconformal map X → X′ and any simple closed curve β, ℓ_{X′}(β) ≤ K ℓ_X(β). Hence log ℓ(β) is 2-Lipschitz for d_T, since K = e^{2d}.
- (D3) **Augmented Teichmüller space.** If X_n → P with markings, and β is disjoint from the pinched multicurve and contained in the component Y_j, then ℓ_{X_n}(β) → ℓ_{Y_j}(β).
- (D4) **Plumbing.** Near P ∈ Δ_G, the orbifold chart of M̄_g is Def(P) = ∏_w Def(Y_w, nodes) × ∏_{e∈E(G)} {t_e}, with X(m, t) obtained by plumbing z w = t_e in fixed node coordinates. Fix compact sets K_w ⊂ Y_w equal to the complement of the discs {|z| < r_0} around the node branches.
  - Locally uniformly in (m, t), a tangent vector (ṁ, ṫ) is represented by a Beltrami differential μ = μ^{fac} + μ^{coll}, where:
    - μ^{fac} is supported in ∪ K_w, with ‖μ^{fac}‖_∞ ≤ C|ṁ|;
    - μ^{coll} is supported in the plumbing collars, with ‖μ^{coll}‖_∞ ≤ C Σ_e |ṫ_e/t_e| / log(1/|t_e|) for |t_e| small (and ≤ C|ṫ_e| when t_e is bounded away from 0).
  - The collar bound comes from realising t ↦ t e^ε by the map that is affine in log z on the collar {|t|/r_0 < |z| < r_0}, whose length is about log(1/|t|).

**Proposition 3.** Let E be a 1-dimensional irreducible piece of closure(V_0) ∩ Δ_G and U ⊂ E a nonempty open set. Then there are P″ ∈ U, lying on no other component of closure(V_0) \ V_0, and generating pairs (X_n, q_n) with ‖q_n‖_1 = 1 and X_n → P″, such that some vertex w of G carries positive area in the sense of (F): q_n converges, locally uniformly on Y_w minus its punctures, to an η_w ≢ 0.

*Proof.*
1. **Local model.**
   - closure(V_0) \ V_0 is an analytic set of dimension ≤ 1.
   - Other 1-dimensional pieces meet closure(E) in finitely many points.
   - Shrink U so that U avoids them, avoids singular points of E, and avoids the images of singular points of the normalization ν : Ṽ → closure(V_0) (taken in an orbifold chart). Singular points of a normal surface are isolated.
   - Then near a point P̂ over U, Ṽ is smooth with coordinates (z, w), and ν^{-1}(E) = {w = 0}, since near U the only boundary is E.
   - For each e ∈ E(G), t_e∘ν = w^{m_e} u_e(z, w) with m_e ≥ 1 and u_e a unit: t_e vanishes on E and nowhere else nearby.
   - The factor coordinates m(z, w) are holomorphic.
2. **A moving factor.**
   - ν({w = 0}) is an open piece of the curve E ⊂ ∏ M_w, so some coordinate m_j(z, 0) is non-constant.
   - Hyperbolic length functions of finitely many simple closed curves give local real-analytic coordinates on Teichmüller space. So there is a simple closed curve β ⊂ Y_j, not peripheral, with f(z) := log ℓ_{Y_j(z,0)}(β) non-constant on a small disc D_0 ∋ z_0.
   - Choose z_1, z_2 ∈ D_0 with |f(z_1) − f(z_2)| = 2δ > 0.
3. **Lower bound on the Teichmüller norm.**
   - Let w_n → 0, w_n ≠ 0. Set f_n(z) := log ℓ_{X(z,w_n)}(β), using the marking carried along D_0 × {w_n}.
   - By (D3), f_n → f pointwise, so |f_n(z_1) − f_n(z_2)| ≥ δ for n large.
   - By (D2), |f_n(z_1) − f_n(z_2)| ≤ 2 d_T(X(z_1,w_n), X(z_2,w_n)) ≤ 2|z_1 − z_2| · sup_{z∈[z_1,z_2]} ‖∂_z‖_T(z, w_n).
   - So there are z′_n ∈ [z_1, z_2] with ‖v_n‖_T ≥ c := δ/(4|z_1 − z_2|) > 0, where v_n := ν_*∂_z ∈ T_{X_n}V_0 and X_n := X(z′_n, w_n).
   - Pass to a subsequence with z′_n → z″, and put P″ := ν(z″, 0) ∈ U.
4. **The generating pair.**
   - Let q_n := q_{v_n} be as in (D1). Its Teichmüller disc is tangent to v_n ∈ T V_0, so by total geodesy (X_n, q_n) is a generating pair, and ‖q_n‖_1 = 1.
   - Represent v_n by μ_n as in (D4), with ṁ = ∂_z m and ṫ_e = ∂_z t_e = w^{m_e} ∂_z u_e.
   - Then |ṁ| ≤ C and |ṫ_e/t_e| = |∂_z log u_e| ≤ C, uniformly for z ∈ [z_1, z_2].
   - Hence ‖μ_n^{fac}‖_∞ ≤ C′, and ‖μ_n^{coll}‖_∞ ≤ C′ / min_e log(1/|t_e(z′_n, w_n)|) =: ε_n → 0.
5. **Area in the thick part.** By (D1),
   c ≤ ‖v_n‖_T = Re ∫ q_n μ_n ≤ C′ ∫_{∪K_w} |q_n| + ε_n.
   So ∫_{∪K_w} |q_n| ≥ (c − ε_n)/C′, which is bounded below. Pass to a subsequence and fix one vertex w with ∫_{K_w} |q_n| ≥ c/(2C′|V(G)|).
6. **Limit.**
   - Transport q_n to Y_w(m_n) via the plumbing trivialisation. The m_n converge, and the q_n are holomorphic with L^1-norm ≤ 1 on neighbourhoods of the exhausting compact sets of Y_w minus its punctures.
   - By the mean-value inequality they are locally uniformly bounded. A diagonal subsequence converges locally uniformly to a holomorphic η_w with ∫_{K_w} |η_w| ≥ c/(2C′|V(G)|) > 0 and ∫ |η_w| ≤ 1.
   - That is positive area at w with s_n = 1. ∎

**Corollaries.**
- (i) **(PA) of PR-F holds.** With G = Γ, Prop. 3 together with Lemma V gives positive area at some vertex j ≠ i. Then Prop. C of PR-F is unconditional: π_j(E) is an orbifold-unramified Teichmüller curve with closure(E) ≠ E, where E is the relevant component of ∂V_0.
- (ii) Every 1-dimensional piece E of closure(V_0) \ V_0 has a vertex w with π_w|_E an orbifold-unramified Teichmüller curve (Lemma T′, using a point P″ as in Prop. 3).
- (iii) In (H), the clause (area) at a merged vertex u is equivalent to π_u|_E being an isometric factor. (⇐ is only sketched; I do not use it.)
  - ⇒ is Lemma T′.
  - ⇐: Step 5 above, done with μ^{fac} split by vertex, suggests that the area of q_{v} concentrates on the vertices whose factor speed ‖dπ_w(v)‖ is maximal. Making this precise needs an infinitesimal product-region estimate (Minsky's product-region theorem is only coarse). I flag this as a sketch only.

---

## 4. Where the general case breaks, and the corrected target

1. **The merge clause of (H) is not proved.** Prop. 3 and Lemma T′ settle the analytic half: some factor of every boundary piece is a Teichmüller curve. They do not show that, at some point of closure(∂V_0), the component Y_0 lies inside a positive-area (maximal-speed) vertex of a piece in a stratum G ≠ Γ.
   - Prop. 2 shows that such a piece need not exist at all: all boundary pieces may lie in Δ_Γ.
   - In that case the Y_0-component merges only along *other branches of ∂V_0 itself*, as the twin end Ŷ′ in Prop. 2.
2. **The literal clause "every vertex u having a component isomorphic to Y_0" is too strong.** In Prop. 2, the branch β at P_0 always offers the lift R with R_i = Y_0 smooth. Any statement that quantifies over all lifts and all twins fails whenever P_0 lies on closure(∂V_0) through a branch of ∂V_0, and when G = Γ that is unavoidable (Obs. 1).
3. **Proposed corrected target (MS5′), for a future round.** There exist a point P_0 ∈ closure(∂V_0), a branch β of closure(∂V_0) at P_0, and a 1-dimensional piece E (G = Γ allowed) with a branch b at P_0, b ≠ β, such that:
   - the component of P_0 that is the β-limit of vertex i lies, in the b-lift, inside a vertex u with R_u nodal;
   - π_u|_E is a Teichmüller curve;
   - (M2) holds: Aut(P_0) fixes that component, or at least cannot exchange it with a non-merged twin.

   Theorem P's Step 3 goes through with MS5′ if (M2) holds. Prop. 2 shows that (M2) can fail, and in that example MS5′ without (M2) holds but does not suffice.
4. **Open questions.**
   - (Q1) Is the quintic family of Prop. 2 orbifold-smooth or coarse-smooth? If it satisfies the problem's smoothness hypothesis, it is a genuine counterexample to (H) and MS5.
   - (Q2) Is the original claim true for the quintic family, i.e. can a holomorphic family V_t satisfying (i) and (ii) have P_t = Y_t – W – Y_0 with Y_t ≠ Y_0? Neither Theorem P nor (H) decides this.
   - (Q3) For smooth V_0 in general, does some point of closure(∂V_0) admit a branch on which the β-specialization of vertex i is merged into a maximal-speed vertex, with (M2)?
   - (Q4) Is there a precise infinitesimal product-region estimate giving ⇐ in Corollary (iii)?

**What is proved here:** Obs. 1; Prop. 3 and Corollaries (i) and (ii), modulo the cited standard facts (D1)–(D4) and (C1)–(C4); the boundary computation in Prop. 2.
**Not proved:** the smoothness of the Prop. 2 example; Corollary (iii) ⇐; (H) in general.

=== END OF ANSWER round6_q5 ===
