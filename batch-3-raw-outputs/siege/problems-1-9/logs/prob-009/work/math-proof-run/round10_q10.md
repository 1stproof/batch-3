kind: attempt
Open question attempted: chain check of ledger entry 85 (Proposition K_w, the walk chain, round9_q4 §2). The run's chain to its goal rests on this result, and no separate query has yet checked it. Checking it is the one chain check this round allows.

## Task
Check, step by step, the proof of Proposition K_w and of Lemma S′ in round9_q4 §2, which is spliced verbatim below together with the Proposition K material it builds on (PR-H, verbatim). For every inference, say whether it is correct, and repair it if you can. End with an explicit verdict: does the proof establish Proposition K_w exactly as stated, and in the form the chain uses it?

**The form the chain uses.** Fix r > 0 small. There are:
- pieces D^1 ⊂ ∂V_0, D^2, …, D^k;
- transition points J_1, …, J_{k−1} and an endpoint Q_0.

At each J_m there are:
- an entering lift β̃_m (of the branch of D^m at J_m) and a leaving lift β̃′_m (of the branch of D^{m+1}) in the Kuranishi chart Def(J_m);
- a single chart vertex x_m that is the constant vertex c_m ≅ Y_0 of D^m along β̃_m and the constant vertex c_{m+1} ≅ Y_0 of D^{m+1} along β̃′_m;
- continuous lifted paths γ̃_n in q^{-1}(V_0) ∩ B (B a fixed Aut(J_m)-invariant chart ball), whose endpoints converge to points of β̃_m ∖ {0} and of β̃′_m ∖ {0}.

At Q_0 there are:
- an entering lift β̃ with chart vertex x and a terminal lifted branch b̃ joined in the same way;
- along b̃, at t = 0, either x is MERGED (some edge at x is unpinched along b̃), or x is MOVING (all edges at x are pinched and F_x is non-constant along b̃).

**Points to scrutinise in particular.**
1. Step 0: the rays stay close to B_0 up to time T_n, uniformly.
2. Step 1: finiteness of the excursions, and the claim that the walk ENDS inside an excursion rather than during travel (Step 2).
3. Step 2: the curves of ∂Σ_i are node curves of the nearby boundary point, and the Σ_i-side is a single constant vertex of the travelled piece with value ≅ Y_0. This uses the choice of δ, η in (a), (b).
4. Step 3: the T_g-marking along the ray is compatible with the chart. The identification of ∂Σ_i with the vanishing cycles of the edges at a single chart vertex x persists through the whole excursion, so that x is the same label on entry and on exit. Check this carefully when the excursion passes near orbifold points (curves with automorphisms): does the continuous lift of the path through Def(J)/Aut(J) stay well defined, and does the label x stay well defined?
5. Step 4: the limit point z̃^∞ ≠ 0, and the MERGE/MOV dichotomy at the endpoint.
6. Lemma S′ and Step 5: the incoming and outgoing branches lie in a common sheet. Is the lifted path γ̃_n in Def(J)° contained in a single irreducible component of q^{-1}(closure V_0)? This matters because the preimage of a smooth coarse surface can be locally reducible at points with reflection-type stabilisers. If it is not, say what weaker statement holds.
7. The dependence of the chain on (r, δ, η, n), and whether a single chain with all these properties exists.

If you find a gap, give the repaired statement and proof, or a counterexample to the step. Begin with a short plan/status line. End with: verified / repaired / gap remains.

## Readings
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.


### PR-H. Lemma PA (positive area at generic boundary points), Lemma NH and Proposition K (the Y_0-network reaches a MERGE or MOV branch) (from round6_q9, verbatim, sections 1–3)
## 1. Gap (d): Lemma PA (proved, modulo cited standard facts)

### 1.1 Cited standard facts (from memory)
- **(Pl) Plumbing chart.** Near P ∈ Δ_Γ there is a holomorphic orbifold chart of M̄_g with coordinates (z, t) = (z, (t_e)_{e∈E(Γ)}), built as follows. z ranges over a neighbourhood of P in ∏_w T_w (or a Kuranishi chart of the product); the component Y_w(z) is obtained from the fixed Y_w = Y_w(0) by a quasiconformal deformation whose Beltrami differential is supported in a fixed compact set K_w ⊂ Y_w, disjoint from fixed coordinate discs {|z_e| < 1} around the punctures. The surface X(z,t) is obtained by plumbing z_e w_e = t_e in these discs. (Masur 1976; Bers; Wolpert. Cited from memory.) Consequently:
  - the tangent vector ∂/∂z_k at (z,t) is represented on X(z,t) by the transplanted Beltrami differential of the deformation of the components, supported in ι(K_w) and with sup norm bounded uniformly in t;
  - the vector ∂/∂t_e at (z,t) is represented by a Beltrami differential supported in the collar of e (computed in 1.2).
- **(Dual) Teichmüller norm.** For a tangent vector v at X represented by a Beltrami μ, ‖v‖_T = sup{Re ∫ μφ : φ ∈ Q(X), ‖φ‖_1 = 1}, where Q(X) is the space of integrable holomorphic quadratic differentials (at most simple poles at punctures). The supremum is attained at a unique φ = q_v (the norming differential), and the Teichmüller disc through X tangent to v is the disc generated by q_v. (Teichmüller, Hamilton–Krushkal, Royden; classical.)
- **(Bun) Quadratic differentials at a stable curve.** For the plumbing family, π_*(ω^{⊗2}) is a vector bundle of rank 3g−3 whose fibre at P is H^0(P, ω_P^{⊗2}): differentials on the components with at most double poles at the node branches, with equal leading (double-pole) coefficients a_e on the two branches of each node. The functionals a_e (leading coefficient in the plumbing coordinate z_e, i.e. a_e(φ) = (2πi)^{-1}∮_{|z_e|=r_0} z_e φ/dz_e) are holomorphic on the bundle and linearly independent at P; their common kernel at P is ⊕_w Q(Y_w). (Standard; dimension count Σ_w(3g_w−3+n_w) = 3g−3−|E(Γ)|.)

### 1.2 The collar Beltrami
In the collar of e at X(z,t_0), use the coordinate z = z_e on {|t_0| < |z| < 1} (with w_e = t_0/z). For t near t_0 define F_t(z) = z·exp(c·λ(z)), λ(z) = log|z| / log|t_0|, c = log(t/t_0), and F_t = id off the collar. Then F_t is the identity at |z| = 1, and in the w-coordinate it is w ↦ w (t/t_0)^{1−λ}, the identity at |w| = 1. So F_t: X(z,t_0) → X(z,t) is quasiconformal. Its Beltrami coefficient is
 μ_t = (z/z̄) · (c/(2 log|t_0|)) / (1 + c/(2 log|t_0|)).
Differentiating at t = t_0 (c ≈ δ := (t − t_0)/t_0): the vector δ·t_0 ∂/∂t_e is represented by the Beltrami (δ/(2 log|t_0|))·(z/z̄) on the collar, with sup norm |δ|/(2 log(1/|t_0|)). Hence

 **(C)** ‖b ∂/∂t_e‖_T ≤ |b| / (2 |t_e| log(1/|t_e|)).

### 1.3 The statement
**Lemma PA.** Let P be a generic point of ∂V_0 (outside a discrete subset of ∂V_0). There are X_n ∈ V_0, X_n → P, and generating pairs (X_n, q_n), ‖q_n‖_1 = 1, such that, after passing to a subsequence, the transplanted differentials ι_n^*q_n converge locally uniformly on each component Y_w of P to q_w ∈ Q(Y_w) with:
1. Σ_w ‖q_w‖_1 = 1 (no area is lost in the collars);
2. q_w ≠ 0 only for vertices w at which ∂V_0 moves (in a sense made precise below); in particular q_i = 0;
3. there is a vertex j ≠ i with q_j ≠ 0, i.e. j carries positive area in the sense of PR-F (F) with s_n = 1.
In particular hypothesis (PA) of PR-F holds, at every generic point of ∂V_0.

*Proof.*
**Step 1 (local model).** Let ν: N → closure(V_0) be the normalization of a local irreducible component (branch) of the germ of closure(V_0) along ∂V_0 near P, lifted to the manifold chart of (Pl). Normal surfaces have isolated singular points, and the preimage of ∂V_0 is a curve; so for generic P, N is smooth at the point over P, with coordinates (s, τ) in which the preimage of ∂V_0 is {τ = 0}. The plumbing coordinates pull back to holomorphic functions t_e(s,τ) vanishing on {τ = 0}; write t_e = u_e(s,τ) τ^{m_e} with m_e ≥ 1 and u_e not divisible by τ. The zero set of u_e meets {τ = 0} in a discrete set, which we avoid (genericity). Also z(s,0) parametrizes ∂V_0, and for generic P, a := ∂_s z(s_0,0) ≠ 0 (the parametrization of the curve ∂V_0 is an immersion off a discrete set). Since π_i is constant on ∂V_0, the i-component of a is 0: a = (a_w)_w with a_i = 0.

**Step 2 (the vectors v_n).** Take τ_n → 0 and X_n := ν(s_0, τ_n) ∈ V_0 (points with τ ≠ 0 are in V_0 since t_e ≠ 0 there). Let v_n := dν(∂_s) at (s_0,τ_n), a tangent vector to V_0. In plumbing coordinates v_n = (∂_s z(s_0,τ_n), (∂_s t_e(s_0,τ_n))_e), with ∂_s z(s_0,τ_n) → a and ∂_s t_e = (∂_s u_e) τ^{m_e}, so |∂_s t_e| ≤ C|t_e| because u_e is a unit near (s_0,0). By (Pl) and (C), v_n is represented by a Beltrami differential μ_n = Σ_w ι_n^* μ_w^{(n)} + ν_n, where μ_w^{(n)} is supported in K_w, depends continuously on the vector and converges to a Beltrami μ_w on Y_w representing a_w (take μ_i^{(n)} → 0, since a_i = 0), and ‖ν_n‖_∞ ≤ C' / log(1/max_e|t_e(X_n)|) → 0.

**Step 3 (upper bound).** Put A := max_w ‖a_w‖_{T(Y_w)} > 0 (a ≠ 0). Let φ_n ∈ Q(X_n), ‖φ_n‖_1 = 1. By normal families (an L^1-bounded family of holomorphic quadratic differentials is locally uniformly bounded), after a subsequence ι_n^*φ_n → φ_w locally uniformly on each Y_w. By Fatou on the disjoint images ι_n(K) of exhausting compacts, Σ_w ‖φ_w‖_{L^1(Y_w)} ≤ 1; in particular φ_w is integrable, hence φ_w ∈ Q(Y_w). Then
 Re ∫ μ_n φ_n → Σ_w Re ∫_{Y_w} μ_w φ_w ≤ Σ_w ‖a_w‖ ‖φ_w‖ ≤ A Σ_w ‖φ_w‖ ≤ A,
using |∫ ν_nφ_n| ≤ ‖ν_n‖_∞ → 0 and (Dual) on Y_w. Hence limsup ‖v_n‖_T ≤ A.

**Step 4 (lower bound).** Let j attain the maximum, and φ ∈ Q(Y_j) with ‖φ‖ = 1 and Re ∫ μ_j φ = A. The element φ ⊕ 0 lies in the fibre at P of the subbundle ker(a_e : e ∈ E(Γ)) of (Bun); extend it to a holomorphic section of that subbundle and let φ_n be its value at X_n. Then ι_n^*φ_n → φ on Y_j and → 0 on the other components, locally uniformly. **Collar mass.** In the collar {|t|/r_0 < |z| < r_0} of an edge e write φ_n = Σ_k c_k z^k dz². By construction c_{−2} = a_e(φ_n) = 0. The coefficients c_k, k ≥ −1, are bounded by C r_0^{−k} (Cauchy estimates on |z| = r_0, where φ_n is uniformly bounded). The terms with k ≤ −3 are, in the coordinate w = t/z, the terms c_k t^{k+2} w^{−k−4} dw² with −k−4 ≥ −1, bounded likewise by Cauchy on |w| = r_0. Since ∫_{|z|<ρ}|z|^k dA ≤ 2πρ^{k+2}/(k+2) ≤ 2πρ for k ≥ −1, ρ ≤ 1, the mass of φ_n in {|t|/ρ < |z| < ρ} is ≤ Cρ for ρ ≤ r_0/2, uniformly in n. With convergence on the thick parts this gives ‖φ_n‖_1 → ‖φ‖ = 1. Then Re ∫ μ_n φ_n → Re ∫ μ_j φ = A. So liminf ‖v_n‖_T ≥ A, and ‖v_n‖_T → A.

**Step 5 (the norming differentials).** Let q_n be the norming differential of v_n (‖q_n‖ = 1). By (Dual) the Teichmüller disc tangent to v_n is generated by q_n; since v_n is tangent to V_0 and V_0 is totally geodesic, (X_n,q_n) is a generating pair. Pass to a subsequence with ι_n^*q_n → q_w on each Y_w. As in Step 3,
 A = lim Re ∫ μ_n q_n = Σ_w Re ∫ μ_w q_w ≤ Σ_w ‖a_w‖‖q_w‖ ≤ A Σ_w ‖q_w‖ ≤ A.
All inequalities are equalities. Hence Σ_w ‖q_w‖ = 1 (item 1); q_w = 0 unless ‖a_w‖ = A (item 2; in particular q_i = 0 since a_i = 0 and A > 0); and some q_j ≠ 0, j ≠ i (item 3); moreover q_w norms a_w whenever q_w ≠ 0. ∎

**Remarks.**
- This closes gap (d) of PR-F §6 completely, at every generic point of ∂V_0, with positive area located at a vertex j where the tangent vector of ∂V_0 has maximal Teichmüller norm.
- By Proposition C of PR-F, π_j(E) is then a Teichmüller curve (E the component of ∂V_0 through P), π_j|_E is orbifold-unramified onto it, and closure(∂V_0) ≠ ∂V_0 has cusps. (PR-F's Lemma T' depends on (F2), which PR-F only sketched; I have not re-proved (F2).)
- Corollary (full area): the area of the limit sits entirely on the moving vertices at maximal speed; in particular for the generic P the limit differential (q_w)_w on P is a genuine area-1 integrable differential on the stable curve P, with q_i = 0.
- The same proof applies verbatim to **any** 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, for any product-type stratum Δ_G and any generic point of E (only the local model of Step 1 was used, plus a ≠ 0). Used in §4.

## 2. Gap (c), first half: choice of direction (proved)

Setting: P, (X_n,q_n), (q_w)_w and j as in Lemma PA. For e ∈ Γ_i (edges at i) let γ_e be the core curve of the e-collar of X_n. Transport curves along Teichmüller maps X_n → g_s X_n, where g_s = diag(e^{-s}, e^{s}) contracts horizontal and expands vertical q-lengths ("path marking").

**Lemma NH.** After passing to a subsequence and replacing q_n by e^{-2iθ_n} q_n with θ_n → 0 (which keeps all conclusions of Lemma PA, the rotation being absorbed in the limit), we may assume:
1. there is an essential, non-peripheral curve c of Y_j (hence of S_g, not homotopic to any Γ-curve) and m > 0 such that each q_n has a horizontal cylinder in the class c_n of c of modulus ≥ m; hence Ext_{g_sX_n}(c_n) ≤ e^{-2s}/m for all s ≥ 0;
2. there is e_0 ∈ Γ_i such that the q_n-geodesic representative of γ_{e_0} is not horizontal; hence Ext_{g_sX_n}(γ_{e_0}) → ∞ as s → ∞, for each n.

*Proof.*
- (Cited from memory: Masur.) Cylinder directions of a finite-area quadratic differential are dense in RP^1. A cylinder core of (Y_j,q_j) is non-peripheral: a flat cylinder boundary bounding a disc with at most one simple pole contradicts Gauss–Bonnet (PR-F, Step 5 of Lemma T').
- For each e ∈ Γ_i, the q_n-geodesic representative of γ_e is a chain of saddle connections or a cylinder core. If all its segments are parallel, call their direction θ_n(e) ∈ RP^1; otherwise θ_n(e) is undefined. Pass to a subsequence along which, for e = e_0 fixed, either θ_n(e_0) is always undefined or θ_n(e_0) → θ_∞(e_0).
- Choose a cylinder direction of q_j different from θ_∞(e_0) and rotate so that it is horizontal. Let A be the open horizontal cylinder, A' ⋐ A a compact sub-annulus of modulus m' > 0. On ι_n(A') the differentials q_n converge to q_j in C^1; √q_n is defined on ι_n(A') for large n (the sign holonomy is discrete), so the developing map of ι_n(A') is equivariant under a translation v_n → v ∈ R \ {0}. Its image contains a straight strip in direction v_n of width close to that of A', so q_n has a cylinder in the class of c of modulus ≥ m := m'/2, in direction arg v_n → 0. Put θ_n := arg v_n and rotate. Then this cylinder is exactly horizontal. Under g_s its modulus is multiplied by e^{2s}, giving item 1.
- Since arg v_n → 0 ≠ θ_∞(e_0), for large n γ_{e_0} is not horizontal for the rotated q_n. So some saddle connection of its geodesic has nonzero vertical component, and its vertical measure v := i(γ_{e_0}, F_hor(q_n)) is > 0. (The q-geodesic realizes the intersection numbers with both measured foliations; standard, cited.) Then ℓ_{g_sq_n}(γ_{e_0}) ≥ e^{s}v, and Ext ≥ ℓ²/Area = ℓ² ≥ e^{2s}v² → ∞. ∎

**Remark.** This bypasses gaps (a) and (b) of PR-F §6. Item 1 needs only one exactly horizontal cylinder, obtained by a rotation tending to 0, and not a Jenkins–Strebel q_n. No interchange of the limits is needed below, because I work with connected limit sets instead of the Jenkins–Strebel limits Z_n.

## 3. Proposition K: Y_0 merges or moves somewhere on its own boundary network (proved, modulo routine marking details)

Notation:
- B := closure(V_0) \ V_0. This is a compact 1-dimensional analytic set; work on a level cover if needed.
- Σ_i ⊂ S_g is the subsurface of vertex i, and ∂Σ_i = {γ_e : e ∈ Γ_i}. Both are path-marked.
- ψ(X) ∈ M̄_{g_i,n_i} is the "Σ_i-part" of X. Fix a pants decomposition of Σ_i. ψ(X) is the surface with the Fenchel–Nielsen coordinates of X inside Σ_i and boundary lengths set to 0. It is continuous on augmented Teichmüller space near points where ∂Σ_i is pinched, and there it equals the stable curve on the Σ_i-side.
- d is a metric on M̄_{g_i,n_i}.

**Cited facts (from memory).**
- Kerckhoff: Ext_Y(γ) ≤ e^{2 d_T(X,Y)} Ext_X(γ).
- Maskit's comparison (Ext) of PR-F.
- Lemma G / G′ of PR-F: limits of g_{s_n}X_n with s_n → s* < ∞ lie in ∂V_0. Each such limit equals φ(g_{s*}), up to a subsequence of the φ's.

For δ, η > 0 let T_n = T_n(δ,η) be the first s ≥ 0 at which max_{e∈Γ_i} Ext_{g_sX_n}(γ_e) = δ or d(ψ(g_sX_n), Y_0) = η.

**Step 1 (T_n is finite and tends to ∞).** By Lemma NH(2), Ext(γ_{e_0}) → ∞ along the ray, so T_n < ∞. For s in a compact set, g_sX_n converges to points of ∂V_0, uniformly in s (Lemma G′). At those points ∂Σ_i is pinched and ψ = Y_0, because vertex i of every point of ∂V_0 is Y_0. Hence T_n → ∞.

**Step 2 (the continuum).** Let K = K(δ,η) be a Hausdorff limit (subsequence) of the compact connected sets {g_sX_n : 0 ≤ s ≤ T_n}. Then K is compact and connected, and it contains P. Every point of K is a limit of g_{s_n}X_n with s_n ≤ T_n:
- if s_n stays bounded, the limit lies in ∂V_0 ⊂ B;
- if s_n → ∞, the curve c is pinched by Lemma NH(1), so the limit lies in B.

So K ⊂ B. On K, every ∂Σ_i curve has Ext ≤ δ (in the limit sense along the approximating sequences) and d(ψ, Y_0) ≤ η. Let Q = Q(δ,η) ∈ K be a limit of the endpoints g_{T_n}X_n. Then Q ∈ B, and either
- (a) some γ_e, e ∈ Γ_i, has Ext = δ > 0 at Q, so it is unpinched at Q; or
- (b) d(ψ(Q), Y_0) = η.

**Step 3 (δ_k, η_k → 0).** Pass to a subsequence with K(δ_k,η_k) → K_0 and Q_k := Q(δ_k,η_k) → Q_0. Then K_0 ⊂ B is compact and connected, and contains P and Q_0. At every point of K_0 the curves ∂Σ_i are pinched (Ext ≤ δ_k → 0 along approximating sequences) and the Σ_i-side is the single smooth component Y_0. So vertex "i" is intact, ≅ Y_0, at every point of K_0, consistently with the path marking.

**Proposition K.** There are a compact connected set K_0 ⊂ B containing ∂V_0's point P, along which the Σ_i-component is intact and equal to Y_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B at Q_0 such that one of the following holds:
- **(MERGE)** along b \ {Q_0} some curve of ∂Σ_i is unpinched, i.e. the Y_0-component of Q_0 is merged with other components along b (the merge property of PR-C, at Q_0);
- **(MOV)** along b all of ∂Σ_i stays pinched, but the Σ_i-component is non-constant along b, with limit Y_0 at Q_0.

*Proof.*
- In case (a) for infinitely many k, Q_k ≠ Q_0, because γ_e is pinched at Q_0 and unpinched at Q_k. Put Q̃_k → Q̃_0 in augmented Teichmüller space by choosing lifts and applying mapping classes, so that the path markings converge; this is possible since M̄_g is the quotient of augmented Teichmüller space.
- Near Q_0, B is a finite union of branches, each of which minus Q_0 lies in one stratum. Infinitely many Q_k lie on one branch b, and γ_e is unpinched on b \ {Q_0}: (MERGE).
- In case (b) for infinitely many k: if some ∂Σ_i curve is unpinched at infinitely many Q_k, argue as before to get (MERGE).
- Otherwise ∂Σ_i is pinched at the Q_k, so the Σ_i-side of Q_k is a union of components with ψ(Q_k) at distance η_k > 0 from Y_0 = ψ(Q_0). Again Q_k ≠ Q_0, and the Q_k lie on one branch b, along which ψ is non-constant: (MOV). ∎

**What Proposition K does not give.**
- Q_0 need not lie in closure(∂V_0). K_0 can leave closure(∂V_0) through "STAY" branches: branches of B at points of closure(∂V_0) along which the Y_0-vertex stays intact and constant, but which are not contained in closure(∂V_0).
- The ρ-variant settles nothing. Add the stopping condition "g_sX_n leaves the ρ-neighbourhood of closure(∂V_0)", with η ≪ ρ. That variant shows: **at some point Q ∈ closure(∂V_0) there is a branch of B, not contained in closure(∂V_0), of type MERGE, MOV or STAY.** This is only Lemma C1 of PR-C with the extra edge located; it does not exclude STAY.
- Heuristic for why STAY should really occur, from the multi-scale picture, not proved. Suppose the zero-area part of the limit at P has two levels below the top: a vertex w at level −1 and the vertex i at level −2, attached below w. Along the ray, lower levels are "released" (become commensurate with the contracted top-level skeleton) top-down. w merges with the top-level skeleton first, along a branch b_w at the cusp Q of ∂V_0, and the Y_0-vertex is still intact and constant along b_w. The merge of Y_0 then happens at a cusp of b_w, which is in general not in closure(∂V_0).





### round9_q4 §2 (verbatim): the same-sheet lemma, the failure of (TD_J), and the walk chain (Proposition K_w)
## 2. Part 2: the same-sheet lemma

### 2.1 Sheets and Milnor balls (Lemma S, made precise)
This lemma is cited and standard (local structure of analytic germs).

Let X = closure(V_0) ⊂ M̄_g and Q ∈ B_0. Assume V_0 is smooth, so Sing X ⊂ B_0. Put Z := Sing X ∪ B_0. For W in a fundamental system of small (Milnor) neighbourhoods of Q:
- the connected components of V_0 ∩ W = (X ∖ Z) ∩ W are exactly the sets X_k ∩ W ∖ Z, where X_k runs over the irreducible components of the germ (X, Q);
- each such set is connected, and its closure in W is X_k ∩ W.

Fix such a W. Choose it also so small that B_0 ∩ W is the union of the branches of B_0 at Q, each branch minus Q lying in one stratum. Then:

**Lemma S′.** Let γ: [a,b] → V_0 ∩ W be a path. Suppose there are a sequence of such paths γ_n and points z^1 ∈ β ∖ {Q} and z^2 ∈ β′ ∖ {Q}, where β, β′ are branches of B_0 at Q, such that γ_n(a) → z^1 and γ_n(b) → z^2. Then some sheet X_k contains both β and β′.

*Proof.*
- Pass to a subsequence along which all the γ_n lie in the same component X_k ∩ W ∖ Z. There are finitely many components.
- X_k ∩ W is closed in W, so z^1 ∈ X_k.
- Near z^1, B_0 coincides with β, since z^1 is not Q and W contains no other special point.
- X_k ∩ ∂M̄_g is locally the zero set of ∏ s_e on the 2-dimensional germ X_k. So it is either empty near z^1 or of pure dimension 1 through z^1. It contains z^1, so it is the germ of β at z^1.
- So X_k contains an open piece of the irreducible germ β, hence all of β. The same argument applies to β′. ∎

### 2.2 What fails in the reading (TD_J)
Proposition K (PR-H §3) produces the continuum K_0 as a Hausdorff limit of K(δ_k, η_k). Each K(δ, η) is in turn a Hausdorff limit of the ray segments {g_s X_n : 0 ≤ s ≤ T_n}. The chain D^1, J_1, …, Q_0 is then read off from K_0.

Hausdorff convergence says nothing about the order in which a ray visits the parts of K_0. Here is a failure mode, which nothing in the proof excludes.
- Suppose the rays come near β at J, then leave every small ball around J along β, run around a loop of B_0, and re-enter the ball along β′.
- Then K_0 ⊃ (β ∪ β′) near J, and J ∈ K_0. A chain read off K_0 may record the transition D → D′ "at J".
- But no ray sub-path stays near J while passing from β to β′.

So the clause in (TD_J) that γ maps into V_0 ∩ U, with U a small neighbourhood of J, is not justified by Proposition K as written. In this situation the same-sheet conclusion at J has no support: β and β′ may lie in different sheets at J (the case Cr1). This is exactly what the "routine marking details" hide.

### 2.3 Repair: the walk chain (Proposition K_w)
**Data.**
- P (generic on ∂V_0), (X_n, q_n), the ray γ_n(s) := g_s X_n and T_n = T_n(δ, η) are as in PR-H §2–3.
- **Special set Σ.** Σ is the finite set of points of B_0 consisting of:
  - junctions (points in the closures of two distinct pieces);
  - singular points of B_0;
  - punctures of pieces;
  - points of a piece D at which some vertex non-constant on D has a value of class [Y_0].

  The last kind is finite: a non-constant vertex takes a given value at finitely many points, and there are finitely many pieces and vertices.
- Fix r > 0 so small that:
  - the balls B(J, 3r), J ∈ Σ, are pairwise disjoint;
  - each B(J, 3r) is a Milnor neighbourhood as in §2.1;
  - each B(J, 3r) lies in an orbifold chart Def(J)/Aut(J);
  - P ∉ B(J, 3r) for all J.

  Put K_D := closure(D) ∖ ⋃_J B(J, r/2). This is compact, and the K_D are pairwise disjoint. Let 4ρ_* be the least distance between distinct K_D.
- Choose δ, η small, depending on r, so that (a) and (b) hold.
  - (a) **Short curves are node curves.** If a stable curve z ∈ B_0 lies outside ⋃ B(J, r/2), and X is within distance ρ_* of z, then every curve with Ext_X ≤ δ is a node curve of z under the nearby marking. This holds by compactness of the stratum parts involved (collar lemma, cited).
  - (b) **η separates Y_0.** For every piece D and every vertex u non-constant on D, the class of u on K_D is at distance > 2η from [Y_0]. For every constant vertex of every piece whose value is not ≅ Y_0, the value is at distance > 2η from [Y_0].

**Step 0 (closeness to B_0).** ρ_n := sup_{s ≤ T_n} dist(γ_n(s), B_0) → 0.
- Let s_n ≤ T_n.
- If s_n is bounded, Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n} → 0.
- If s_n → ∞, Lemma NH(1) gives Ext(c_n) ≤ e^{−2s_n}/m → 0.
- In either case every limit point of γ_n(s_n) lies in closure(V_0) ∩ ∂M̄_g = B_0, by Maskit's comparison.

**Step 1 (travel and excursions).** Take n large, with ρ_n < min(ρ_*, r/2).
- A time s is a *travel time* if γ_n(s) lies outside ⋃ B(J, r). Then the B_0-points within ρ_n of γ_n(s) lie in a unique K_D. The piece D is locally constant on maximal intervals of travel times.
- An *excursion* at J is a maximal interval of times in B(J, 2r) that contains a time in B(J, r). Its interior endpoints are travel times on the sphere of radius 2r.
- By uniform continuity there are finitely many excursions. Every excursion crosses the shell r ≤ d ≤ 2r.
- The complement of the excursions consists of travel times, so [0, T_n] is a finite alternation: travel along D^1, excursion at J_1, travel along D^2, …. The first travel is along the piece D^1 ⊃ P of ∂V_0.

**Step 2 (STAY along travel intervals).** Let s be a travel time on D, and z_s ∈ K_D a point at distance < ρ_n from γ_n(s).
- Since Ext(∂Σ_i) ≤ δ, (a) shows that the curves of ∂Σ_i are node curves of z_s.
- ψ is continuous on augmented Teichmüller space, so the Σ_i-side of z_s is within η + o(1) of Y_0. In particular it is a single smooth component, a vertex c of D.
- By (b), c is a constant vertex of D with value ≅ Y_0.
- Consequently, at travel times Ext(∂Σ_i) = o(1) < δ and d(ψ, Y_0) = o(1) < η. So **T_n is not a travel time**, and the walk ends inside an excursion, at some Q ∈ Σ.

**Step 3 (chart consistency inside an excursion at J).**
- During the excursion, γ_n lies in the chart Def(J)/Aut(J) and lifts continuously to γ̃_n in Def(J)°. Path lifting through a finite quotient is cited (Bredon).
- The T_g-marking along γ_n is compatible with the chart. The component of the preimage of the chart in T_g covers Def(J)°, with deck group generated by the Dehn twists about the vanishing cycles and the stabiliser. So the vanishing cycle of each chart edge e is a well-defined marked curve throughout the excursion.
- At the entry time, ∂Σ_i is the set of node curves around the constant vertex c of D. A constant vertex stays intact at J, since its value lies in M_w. So c = {x} for a single chart vertex x along the entry lift β̃ (a branch of D at J), and ∂Σ_i = {vanishing cycles of the edges at x}.
- This identification persists along the whole excursion.
- At the exit time (if the excursion is not the last), Step 2 applies on the exit piece D′ along a lift β̃′. The same x satisfies c′ = {x} along β̃′.

So the walk gives a chain in the sense of (K′): constant vertices c_m ≅ Y_0, and a common chart vertex x_m at each J_m.

**Step 4 (the endpoint).** Let Q be the point of the last excursion, entered from D along β̃ with chart vertex x.
- Take a subsequence n → ∞, with (r, δ, η) fixed. The finite combinatorial data are then constant: Q, D, β̃, x.
- The nearest boundary lifts z̃_n of γ̃_n(T_n) converge to some z̃^∞ ∈ (preimage of B_0) ∩ closure(B(Q, 2r)).
- **z̃^∞ ≠ 0.**
  - F_x(0) ≅ Y_0, by continuity of F_x on L_x along β̃.
  - If z̃^∞ = 0, then near 0 every s_e with e at x tends to 0, so Ext(∂Σ_i) → 0. Also ψ → F_x(0) ≅ Y_0.
  - Both stopping conditions would then fail at T_n.
- So z̃^∞ lies on a lifted branch b̃ ∖ {0} at Q. At T_n one of the two stopping conditions holds.
  - **Ext(γ_e) = δ for some e at x.** Then s_e(z̃^∞) ≠ 0, so e is unpinched along b̃: **MERGE**.
  - **d(ψ, Y_0) = η.** Then all edges at x are pinched along b̃, and d(F_x(z̃^∞), Y_0) = η > 0 while F_x(0) ≅ Y_0: **MOV** (interior or puncture).

**Step 5 (same sheet at every transition).**
- Each junction transition of the walk chain is a sub-path of γ_n inside B(J_m, 2r) ⊂ W. It starts within ρ_n of a point of β^m ∩ shell and ends within ρ_n of a point of β^{m+1} ∩ shell.
- Over the subsequence these points converge to points of the branches other than J_m.
- Lemma S′ applies: the incoming branch and the outgoing branch lie in a common sheet at J_m.
- At the endpoint, the last excursion goes from near β to near z^∞ ≠ Q on b. So β and b lie in a common sheet at Q.

The walk chain depends on (r, δ, η, n), but it is a single finite chain with all the properties (K′) requires. **Proposition K_w (proved, modulo the inputs of PR-H: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T_g ↔ Def chart description, and the collar lemma, all cited):** there is a chain as in (K′), with endpoint MERGE or MOV, in which every transition, including the endpoint, has its incoming and outgoing branches in a common sheet.

---

