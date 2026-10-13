kind: attempt
Open question attempted: are Theorem TV, Corollary Φ̂ and (F2) of round8_q10 (ledger entry 70) and Lemma PA of round6_q9 (entry 45) correct? round13_q9 verified Lemma J0 and Theorem RO but listed these as unchecked dependencies: J0 needs Corollary Φ̂, positive area at the Teichmüller vertex (Lemma PA / Lemma TR) and properness of p_E (TV item 4); Theorem RO and hence the conditional theorem "(R1) + (R2^orb) ⇒ Y_t = Y_0" (entries 128, 149) rest on them. (Final-round allowance: verification of standing results the final document presents.)

## Task
Check, step by step and as an independent referee, the following spliced results:
1. Lemma PA (round6_q9 §1): at a generic point of a 1-dimensional boundary piece of closure(V_0), norming differentials of tangent vectors of V_0 have full-area limits supported on the vertices of maximal Teichmüller speed, so some vertex has positive area and a constant vertex has none. Check the collar Beltrami estimate and the cited facts.
2. round8_q10: (F2) in general form (Theorem F2*), the repaired Lemma T′, Corollary Φ̂ (1-Lipschitz limit maps φ̂_w : H → T(Σ_w), with φ̂_v = D at a positive-area vertex v), and Theorem TV items 1–4 (a Teichmüller vertex j with π_j∘ν a proper orbifold covering of a Teichmüller curve, E^ν ≅ H/Λ_E with Λ_E ⊂ Γ′ of finite index, universal-cover lift = Teichmüller disc, every end maps to a cusp). Note round13_q9's remark that, given Φ̂, TV item 2 reduces to properness of p_E (item 4) — check whether item 4 is proved.
3. Lemma TR (round11_q6 §4), as used for positive area at j.
For each inference say whether it is valid; flag every fact cited from memory and say whether it is standard and correctly stated; repair what you can (say so). End with explicit verdicts for Lemma PA, (F2)/T′, Corollary Φ̂, and each item of Theorem TV: correct / correct after repair / gap (state the gap precisely).

Begin with a plan/status line. End with: verdicts / repairs / remaining dependencies.

## Readings of the problem's hypotheses (as adopted by the run)
## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.


**Definitions** (as in earlier rounds).

**Definitions** (as before, plus anchored sheets).
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w; M(E), K(E) as before.
- *Chart at Q*: Def(Q) with plumbing coordinates s_e, N := ∏_e s_e, q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g. *Labels* = vertices of G_Q; x intact at p if s_e(p) = 0 for every edge e at x; then F_x(p) is that component with its special points.
- *Transport family* Ñ_c̃ of a lifted branch c̃ of a branch c of B_0 at Q: the connected component containing c̃ ∖ {0} of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε).
- *Anchored sheet* of c̃: an irreducible component T of closure(Ñ_c̃) (in B × Δ_ε, germ at (0,0)) with c̃ × {0} ⊂ T.
- *x is Y-persistent on T*: at every (p,t) ∈ T, x is intact at p and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).
- *Lift-curve*: an irreducible component of {(p,t) : q(p) = Q_t}, Q_t := H_t(Q).
- *Product-type stratum*: ξ_G injective on coarse spaces.
- Older spliced files use "transport sheet" for any irreducible component of closure(Ñ_c̃) and sometimes "Y-persistent along b̃" for the whole family; both older notions are superseded: the chain and MS11♭ use anchored sheets. *Boundary-type* sheet: its generic pattern is not all of E(G_Q), i.e. Q is not in the stratum of its branch. P(T) := the set of labels Y-persistent on T; C(L) := the set of labels y with F_y ≅ Y_t along a lift-curve L.


## round8_q10 (verbatim answer)
# round8_q10 — Lemma G/G′/T′ check and a proof of (F2)

**Plan / status line.** (a) Recast "vertex v carries the limit η_v" in Fuchsian language (Def. FA) and prove (F2) in a general form (any scale, any phase) from the explicit Beltrami coefficient of a Teichmüller/affine map and the a.e.-convergence theorem for Beltrami coefficients. (b) Prove that the plumbing-chart convergence used in PR-H Lemma PA implies Def. FA (Lemma TR). (c) Check Lemmas G, G′, T′ step by step; repair Step 2 and Step 4 of T′ (properness, orbifold structure). (d) Treat non-product strata through a marked lift φ̂ and state exactly the form chain step 2 needs.

Status: complete. (F2) is proved (Theorem F2\*, §2), modulo cited standard facts listed in §0. Lemmas G and G′ are valid; Lemma T′ had two gaps (Steps 2 and 4), repaired in §4. The form needed by chain step 2 is Theorem TV (§5). Open points are listed in §7.

## 0. Setting, notation, cited facts

S is a closed oriented surface of genus g ≥ 2. A *marked* surface is (X, f), f: S → X a homeomorphism; T̄ is augmented Teichmüller space, M̄_g = T̄/Mod(S). For a multicurve γ = γ_G on S with dual graph G, let Σ_w (w ∈ V(G)) be the closures of the components of S∖γ (open collars of γ removed), and Γ_w := π_1(Σ_w) ⊂ π_1(S) (base points and paths fixed once and for all; Γ_w is well defined up to conjugation, and only up-to-conjugation statements are made). Peripheral elements of Γ_w are those freely homotopic into ∂Σ_w. For a marked hyperbolic surface (X,f), a *holonomy* is a discrete faithful ρ: π_1(S) → PSL(2,R) with H/ρ(π_1 S) = X, compatible with f; it is unique up to conjugation in PSL(2,R). q̃ denotes the lift to H of a quadratic differential q on X through the covering H → X determined by ρ.

**Readings (as in the task).** (R1), (R2) of the task file; V_0 is a closed, connected, smooth 2-dimensional subvariety of M_g, so closure(V_0) is an irreducible projective surface (Chow) and closure(V_0) ∖ V_0 has dimension ≤ 1.

**Δ̂_G.** For any graph G, Δ̂_G := ∏_{w∈V(G)} M_{g_w,n_w} (the n_w marked points labelled by half-edges/legs), with its finite surjection ξ_G: Δ̂_G → Δ_G (quotient by Aut(G)); ξ_G is an isomorphism in the product case of the problem. A point P̃ of the γ_G-stratum of T̄ (marked stable curve with pinched multicurve exactly γ_G) has marked components P̃_w ∈ T(Σ_w) := T_{g_w,n_w}, and a *labelled* image λ(P̃) := ([P̃_w])_w ∈ Δ̂_G with ξ_G(λ(P̃)) = image of P̃ in M̄_g. (The labelling of components of S∖γ_G by V(G) is fixed once.)

**Cited facts (all from memory; stated in the form used).**
- **(GC) Augmented Teichmüller space via restricted holonomies** (Abikoff, Bers; Fenchel–Nielsen coordinates). Let (X_n, f_n) be marked hyperbolic surfaces with holonomies ρ_n, γ = γ_G a multicurve.
  (GC1) If (X_n,f_n) → P̃ in T̄ and P̃ lies in the γ-stratum, then ℓ_{X_n}(γ_e) → 0 for each e, and for each w there are B^w_n ∈ PSL(2,R) with B^w_n ρ_n|_{Γ_w} (B^w_n)^{-1} → σ_w pointwise on Γ_w, where σ_w is a type-preserving (peripheral ↦ parabolic) discrete faithful holonomy of the marked punctured surface P̃_w; and ℓ_{X_n}(c) → ℓ_{P̃_w}(c) for every non-peripheral closed curve c in Σ_w.
  (GC2) Conversely, if ℓ_{X_n}(γ_e) → 0 for all e and for each w some conjugates of ρ_n|_{Γ_w} converge pointwise to a discrete faithful type-preserving R_w: Γ_w → PSL(2,R) with H/R_w(Γ_w) of finite area, then (X_n,f_n) converges in T̄ to the point P̃ of the γ-stratum with P̃_w = H/R_w(Γ_w) (marked through Σ_w). (In FN coordinates adapted to a pants decomposition containing γ: the γ-lengths tend to 0, the γ-twists are irrelevant at the γ-stratum, and all other FN coordinates are continuous functions of the conjugacy classes of the restricted holonomies.)
  (GC3) If X_n → P in M̄_g, then after passing to a subsequence there are markings f_n with (X_n,f_n) convergent in T̄ to a lift P̃ of P.
- **(QC1) Normal families** (Lehto–Virtanen, Ch. II §5). K-qc self-homeomorphisms of Ĉ fixing 0, 1, ∞ form a sequentially compact family for uniform convergence in the spherical metric, and limits are K-qc homeomorphisms. K-qc embeddings of a domain D ⊂ C omitting two fixed values form a normal family; a locally uniform limit is constant or a K-qc embedding.
- **(QC2) A.e.-convergence theorem** (Lehto–Virtanen Ch. V, Thm. 5.3; Ahlfors, *Lectures on qc mappings*, Ch. V). If μ_n, μ ∈ L^∞(C), ‖μ_n‖_∞ ≤ k < 1, and μ_n → μ almost everywhere, then the normalized solutions w^{μ_n} (fixing 0,1,∞) converge to w^μ uniformly on Ĉ in the spherical metric.
- **(QC3)** A qc map with Beltrami coefficient 0 a.e. is conformal (Weyl's lemma); chain rule for Beltrami coefficients: if f, h are qc and μ_f = μ_h a.e., then f∘h^{-1} is conformal.
- **(Pl), (Bun), (Dual)** as in PR-H §1.1; Teichmüller discs, Royden's theorem k_T = d_T, the Bers embedding (T is a bounded domain), Masur's theorem on cylinders — as in PR-F §0.

## 1. Four elementary lemmas (proved)

**Lemma B (Beltrami coefficient of an affine map).** Let q ≢ 0 be a meromorphic quadratic differential on a Riemann surface X and g = (g_{11} g_{12}; g_{21} g_{22}) ∈ GL^+(2,R). Write the real-linear map g of R² = C as ζ ↦ αζ + β ζ̄ with α = ((g_{11}+g_{22}) + i(g_{21}−g_{12}))/2, β = ((g_{11}−g_{22}) + i(g_{21}+g_{12}))/2; then |α|² − |β|² = det g > 0. The surface underlying g·(X,q) is X^{μ} with
  μ = c_g · q̄/|q|,  c_g := β/α, |c_g| < 1,
(defined off the zeros and poles of q), and the identity X → X^μ is the map that is affine of derivative g in natural coordinates. For s ∈ C^*: q̄/|q| = (s̄/|s|) · \overline{(q/s)}/|q/s|.

*Proof.* Near a point where q ≠ 0, ∞, take a natural coordinate ζ, q = dζ². The structure g·(X,q) is the one whose charts are ζ' = gζ = αζ + βζ̄. In a local coordinate z of X: ∂_z ζ' = α ζ_z (ζ is holomorphic in z) and ∂_{z̄}ζ' = β \overline{ζ_z}. So μ = (β/α) \overline{ζ_z}/ζ_z · dz̄/dz. Since q = ζ_z² dz², q̄/|q| = \overline{ζ_z}²/|ζ_z|² · dz̄/dz = \overline{ζ_z}/ζ_z · dz̄/dz. Hence μ = (β/α) q̄/|q|. The rescaling identity is immediate from q̄/|q| = \overline{s(q/s)}/|s||q/s|. ∎

(For g ∈ SL(2,R), the identity X → X^{μ} is the Teichmüller map of dilatation K(g) = (|α|+|β|)/(|α|−|β|) = e^{2 d_H(i, g^{-1} i)} — standard; only K(g) < ∞ and its continuity in g are used.)

**Lemma Conv (Beltrami coefficients pass to a.e. limits).** Let D ⊂ C be a domain, f_n: D → C K-qc embeddings converging locally uniformly to a non-constant f, and suppose μ_{f_n} → μ a.e. on D. Then f is a qc embedding and μ_f = μ a.e.

*Proof.* f is a K-qc embedding by (QC1). Extend μ_n := μ_{f_n} and μ by 0 to C; ‖μ_n‖ ≤ k := (K−1)/(K+1). Let w_n := w^{μ_n}, w := w^μ. By (QC2) w_n → w uniformly on Ĉ; the inverses w_n^{-1} are normalized K-qc maps, hence (QC1) relatively compact, and every limit of a subsequence is w^{-1}; so w_n^{-1} → w^{-1} uniformly. Let L ⊂ w(D) be compact. Then w^{-1}(L) is a compact subset of D; pick a compact neighbourhood L' ⊂ D of it; for n large w_n^{-1}(L) ⊂ L', i.e. L ⊂ w_n(L'). On w_n(D), h_n := f_n ∘ w_n^{-1} is conformal (QC3). On L, h_n → f∘w^{-1} uniformly (f_n → f uniformly on L', equicontinuity of the f_n on L', and w_n^{-1} → w^{-1}). A locally uniform limit of holomorphic functions is holomorphic, so h := f∘w^{-1} is holomorphic and injective on w(D), i.e. conformal. Thus f = h∘w on D and μ_f = μ_w = μ a.e. ∎

**Lemma Conj (rigidity of normalizations).** Let Γ be a group, ρ_n, R: Γ → PSL(2,R) with ρ_n → R pointwise, R discrete and faithful with R(Γ) non-elementary (no finite orbit in H ∪ R̂). Let B_n ∈ PSL(2,R) with B_n ρ_n B_n^{-1} → σ pointwise, σ discrete faithful. Then (B_n) has a subsequence converging to some B ∈ PSL(2,R), and σ = B R B^{-1}.

*Proof.* A non-elementary torsion-free-or-not Fuchsian group contains two hyperbolic elements R(γ_1), R(γ_2) without common fixed point (standard); then γ_1, γ_2 do not commute, so σ(γ_1), σ(γ_2) (faithful) do not commute. tr σ(γ_i) = lim tr ρ_n(γ_i) = tr R(γ_i), so σ(γ_i) is hyperbolic. In a discrete group two hyperbolic elements with exactly one common fixed point do not exist, and two with both fixed points in common commute; hence the four fixed points of σ(γ_1), σ(γ_2) are pairwise distinct, and likewise for R. The fixed points of ρ_n(γ_i) converge to those of R(γ_i) (hyperbolic elements; fixed points depend continuously), and B_n maps the attracting/repelling fixed points of ρ_n(γ_i) to those of B_nρ_n(γ_i)B_n^{-1}, which converge to those of σ(γ_i). So B_n maps three points x^j_n → x^j (distinct) to three points y^j_n → y^j (distinct). A Möbius map depends continuously on the images of three distinct points, hence B_n converges to the Möbius map B with B(x^j) = y^j, and σ(γ) = lim B_nρ_n(γ)B_n^{-1} = B R(γ) B^{-1}. ∎

**Lemma Lim (limits of qc conjugacies).** Let Γ be a group, ρ_n: Γ → PSL(2,R) with ρ_n → R pointwise, R discrete faithful, R(Γ) non-elementary, type-preserving with H/R(Γ) of finite area. Let F̃_n: H → H be K-qc homeomorphisms (extended to R̂) and ρ'_n: Γ → PSL(2,R) with F̃_n ∘ ρ_n(γ) = ρ'_n(γ) ∘ F̃_n. Let M_n ∈ PSL(2,R) be such that M_nF̃_n fixes 0, 1, ∞. Then after a subsequence M_nF̃_n → F̃ uniformly on H̄ (spherical metric), F̃ a K-qc homeomorphism of H, and M_n ρ'_n M_n^{-1} → R' := F̃ R F̃^{-1} pointwise; R' is discrete, faithful, type-preserving, and F̃ descends to a K-qc homeomorphism H/R(Γ) → H/R'(Γ) in the marking class (inducing γ ↦ γ on π_1).

*Proof.* Extend M_nF̃_n by reflection to K-qc maps of Ĉ fixing 0,1,∞; (QC1) gives the convergent subsequence and the K-qc limit F̃, preserving H. Uniform convergence of homeomorphisms of the compact Ĉ to a homeomorphism implies uniform convergence of the inverses. Hence for γ ∈ Γ, M_nρ'_n(γ)M_n^{-1} = (M_nF̃_n)ρ_n(γ)(M_nF̃_n)^{-1} → F̃ R(γ) F̃^{-1} uniformly on Ĉ. Möbius maps converging uniformly on three points to a homeomorphism converge in PSL(2,R), and the limit is Möbius; so R'(γ) := F̃R(γ)F̃^{-1} ∈ PSL(2,R), R' is a homomorphism, faithful, and R'(Γ) acts properly discontinuously and freely-where-R-does on H (conjugate by a homeomorphism), so it is discrete. A parabolic R(γ) has one fixed point on R̂ and none in H, hence so does R'(γ): type-preserving. F̃ is R–R' equivariant, so it descends. ∎

## 2. (F2) proved, in a general form

**Definition FA (vertex v carries η_v at scale s_n).** Let (X_n,f_n) → P̃ in T̄ with P̃ in the γ_G-stratum (possible after a subsequence, by (GC3), whenever X_n → P ∈ Δ_G), Y_v := P̃_v, and let σ_v be a holonomy of Y_v (type-preserving). Let q_n ∈ Q(X_n) ∖ 0 and s_n ∈ C^*. We say *v carries η_v at scale s_n* if there are holonomies ρ_n of (X_n,f_n) with ρ_n|_{Γ_v} → σ_v pointwise and q̃_n/s_n → η̃_v locally uniformly on H, where η̃_v ≢ 0 is the σ_v-lift of a holomorphic quadratic differential η_v on the punctured surface Y_v. *Positive area* means: ‖q_n‖_1 = 1, s_n = 1, and η_v is integrable. (Lemma TR in §3 shows that the plumbing-chart convergence produced by PR-H Lemma PA gives exactly this, with η_v integrable.)

By Lemma B, replacing s_n by |s_n| replaces η_v by e^{iθ}η_v when arg s_n → θ (pass to a subsequence); so we may and do assume s_n > 0.

**Theorem F2\*.** Assume Def. FA with s_n > 0. Let g ∈ SL(2,R), let F_n: X_n → X'_n be the map which is affine of derivative g for q_n (X'_n = underlying surface of g·(X_n,q_n); F_n is the Teichmüller map of q_n, of dilatation K(g)), and f'_n := F_n∘f_n. Then:
(i) every subsequence of (X'_n, f'_n) has a further subsequence converging in T̄, and every such limit P̃' lies in the γ_G-stratum;
(ii) for every such limit, P̃'_v = g·(Y_v, η_v) as a point of T(Σ_v), the marking of g·(Y_v,η_v) being that of Y_v transported by the identity map Y_v → g·(Y_v,η_v) (the affine map of derivative g for η_v);
(iii) consequently, if X'_n → P' in M̄_g along a subsequence, then P' ∈ Δ_G and the v-entry of the labelled lift λ(P̃') ∈ Δ̂_G is [g·(Y_v,η_v)] ∈ M_{g_v,n_v}, the point of (the image of) the Teichmüller disc of (Y_v,η_v) labelled by g. For product-type G this is π_v(P') = [g·(Y_v,η_v)].
Neither integrability of η_v nor any control of the area of q_n in the collars or on other vertices is needed; the statement is for each fixed g, with no uniformity in g required.

*Proof.*
*Step 1 (lifts).* Let ρ_n be as in Def. FA. F_n lifts to a K(g)-qc homeomorphism F̃_n: H → H and there are holonomies ρ'_n of (X'_n, f'_n) with F̃_n∘ρ_n(γ) = ρ'_n(γ)∘F̃_n for all γ ∈ π_1(S) (lift F_n to universal covers; it conjugates deck groups compatibly with the markings f_n, F_n f_n). By Lemma B, μ_{F_n} = c_g q̄_n/|q_n|, and Beltrami coefficients lift, so a.e. on H
  μ_{F̃_n} = c_g \overline{q̃_n}/|q̃_n| = c_g \overline{(q̃_n/s_n)}/|q̃_n/s_n|  (s_n > 0).
*Step 2 (each vertex).* Fix w ∈ V(G). By (GC1) there are B^w_n with B^w_nρ_n|_{Γ_w}(B^w_n)^{-1} → σ_w (for w = v take B^v_n = 1 by Def. FA). σ_w(Γ_w) is non-elementary (P̃_w is a stable component: hyperbolic of finite area). The maps F̃_n(B^w_n)^{-1} conjugate B^w_nρ_n(B^w_n)^{-1} to ρ'_n on Γ_w. By Lemma Lim, after a subsequence, suitable Möbius conjugates of ρ'_n|_{Γ_w} converge to a discrete faithful type-preserving R'_w with H/R'_w(Γ_w) K(g)-qc equivalent (in the marking class) to P̃_w; in particular of finite area. Do this for the finitely many w successively.
*Step 3 (convergence).* ℓ_{X_n}(γ_e) → 0 for the γ_G-curves (GC1); by Maskit's comparison (PR-F (Ext)) Ext_{X_n}(γ_e) → 0, so Ext_{X'_n}(γ_e) ≤ K(g) Ext_{X_n}(γ_e) → 0 and ℓ_{X'_n}(γ_e) → 0. By (GC2), (X'_n,f'_n) converges (along the subsequence of Step 2) in T̄ to the point P̃' of the γ_G-stratum with P̃'_w = H/R'_w. If a subsequence of (X'_n,f'_n) converges to some P̃'', run Steps 2–3 along it: a further subsequence converges to a point of the γ_G-stratum, which equals P̃'' since T̄ is Hausdorff. This proves (i).
*Step 4 (identification of the v-component).* Take w = v, B^v_n = 1. In Lemma Lim the maps M_nF̃_n (M_n Möbius) converge uniformly to F̃, and μ_{M_nF̃_n} = μ_{F̃_n}. Since q̃_n/s_n → η̃_v locally uniformly and η̃_v ≢ 0 is holomorphic, its zero set Z is discrete, and at every point of H ∖ Z, \overline{(q̃_n/s_n)}/|q̃_n/s_n| → \overline{η̃_v}/|η̃_v|. Thus μ_{M_nF̃_n} → c_g \overline{η̃_v}/|η̃_v| a.e., with ‖μ_{M_nF̃_n}‖_∞ = |c_g| < 1. Lemma Conv on every disc D ⋐ H gives μ_{F̃} = c_g \overline{η̃_v}/|η̃_v| a.e. on H. F̃ descends to a qc homeomorphism Φ: Y_v = H/σ_v → H/R'_v = P̃'_v in the marking class, with μ_Φ = c_g η̄_v/|η_v| — by Lemma B, the Beltrami coefficient of the identity map ι_g: Y_v → g·(Y_v,η_v). By (QC3), Φ∘ι_g^{-1}: g·(Y_v,η_v) → P̃'_v is conformal; it is in the marking class; it maps punctures to punctures with the same labels (peripheral subgroups correspond, Φ being equivariant for the type-preserving R'_v). This is (ii). Since this identifies P̃'_v independently of the subsequence, and the marked limit of any further subsequence agrees, (iii) follows: P' is the image of some such P̃' in M̄_g, P' ∈ Δ_G, and λ(P̃')_v = [P̃'_v] = [g·(Y_v,η_v)]. ∎

**Where the feared failure modes went.** (a) *Area escaping into collars or to other vertices along g*: irrelevant — the Beltrami coefficient of the Teichmüller map is the *pointwise* expression c_g q̄_n/|q_n|; convergence of q_n on the v-part (up to positive scaling) determines it there, whatever happens elsewhere. (b) *Non-uniformity in g*: each g is treated separately; the joint (in g) statement needed for Lemma T′ is Corollary Φ̂ below, which uses only K(g g'^{-1}) and not F2\*. (c) *Markings at orbifold points*: everything takes place in T̄ and T(Σ_v); passing to M_{g_v,n_v} is done at the very end by a continuous map, so automorphisms of Y_v play no role. (d) *Extremality of the limit map*: not used; only its Beltrami coefficient. Hence F2\* also covers non-integrable η_v (lower-scale limits): the v-component of the limit is the affine deformation Y_v^{c_g η̄_v/|η_v|}.

**Corollary G′\* (the first sentence of PR-F Lemma G′, proved).** If d_T(X_n, X'_n) → 0 and X_n → P in M̄_g, then X'_n → P.
*Proof.* It suffices that every subsequence has a further subsequence converging to P. Choose markings with (X_n,f_n) → P̃ (GC3), Teichmüller maps F_n: X_n → X'_n of dilatation K_n → 1, and f'_n := F_n f_n. Steps 1–3 above (with K := sup K_n) apply verbatim with F_n in place of the affine map: a further subsequence of (X'_n, f'_n) converges to P̃' in the γ_G-stratum with P̃'_w ≅ H/R'_w, R'_w = F̃σ_wF̃^{-1}. Now ‖μ_{F̃_n}‖_∞ → 0, so Lemma Conv (with μ = 0) shows F̃ is conformal, i.e. Möbius; hence P̃'_w = P̃_w for all w (marked), P̃' = P̃ and X'_n → P. ∎
(By the compactness of M̄_g this gives the uniform continuity of (M_g, d_T) → M̄_g by the usual contradiction argument; so Lemma G′ is fully proved.)

**Corollary Φ̂ (the marked lift of the limiting disc).** Let X_n → P ∈ Δ_G, (X_n,f_n) → P̃ as in Def. FA, q_n ∈ Q(X_n) with ‖q_n‖_1 = 1 (no positive-area assumption yet). For g ∈ SL(2,R) let X^g_n, F^g_n be as in F2\*, f^g_n := F^g_n f_n. Then there is a subsequence and continuous maps φ̂_w: H = SO(2)\SL(2,R) → T(Σ_w), each 1-Lipschitz from the Poincaré metric d_H (curvature −4, d_H(SO(2)a, SO(2)b) = ½ log K(b a^{-1})) to the Teichmüller metric, such that for **every** g, (X^g_n, f^g_n) converges in T̄ to the γ_G-stratum point P̃^g with P̃^g_w = φ̂_w(g). Put φ̂ := ([φ̂_w])_w: H → Δ̂_G and φ := ξ_G∘φ̂. Then φ(g) = lim_n X^g_n in M̄_g; if (X_n,q_n) are generating pairs for V_0, φ(H) ⊂ closure(V_0) ∩ Δ_G and φ̂(H) ⊂ Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G). If moreover v carries positive area η_v, then [φ̂_v(g)] = [g·(Y_v,η_v)], i.e. π_v∘φ̂ = u, where u: H → M_{g_v,n_v} is the projection of the Teichmüller disc D of (Y_v,η_v) and φ̂_v = D (as maps to T(Σ_v)).

*Proof.* (K(h) := dilatation of the affine map of derivative h; it is invariant under h ↦ k_1hk_2, k_i ∈ SO(2), so d_H is well defined; it is the hyperbolic metric of curvature −4.) Let {g_k} be a countable dense subset of SL(2,R). By F2\*(i) and a diagonal argument, pass to a subsequence along which (X^{g_k}_n, f^{g_k}_n) → P̃^{g_k} for every k. Fix k, l and w. The map F^{g_l}_n∘(F^{g_k}_n)^{-1}: X^{g_k}_n → X^{g_l}_n is affine of derivative g_lg_k^{-1} for g_k·q_n, hence K_{kl} := K(g_lg_k^{-1})-qc, and it carries the marking f^{g_k}_n to f^{g_l}_n. Lift it, with holonomies of X^{g_k}_n normalized (GC1) so that their restrictions to Γ_w converge to a holonomy σ^k_w of P̃^{g_k}_w. Lemma Lim gives a K_{kl}-qc map in the marking class from P̃^{g_k}_w onto H/R', where R' = lim of Möbius conjugates of ρ^{g_l}_n|_{Γ_w}. By (GC1) other conjugates of ρ^{g_l}_n|_{Γ_w} converge to a holonomy σ^l_w of P̃^{g_l}_w, so Lemma Conj gives R' conjugate to σ^l_w (marked). Hence d_T(P̃^{g_k}_w, P̃^{g_l}_w) ≤ ½ log K_{kl} = d_H(g_k, g_l). So g_k ↦ P̃^{g_k}_w is 1-Lipschitz on a dense set and extends (T(Σ_w) is complete) to a 1-Lipschitz φ̂_w on H. For arbitrary g, by F2\*(i) every subsequence of (X^g_n, f^g_n) has a further subsequence converging to some P̃'' in the γ_G-stratum, and the same comparison with g_k gives d_T(P̃''_w, φ̂_w(g_k)) ≤ d_H(g, g_k) for all k, so P̃''_w = φ̂_w(g) for all w. A point of the γ_G-stratum is determined by its components, so P̃'' is independent of the subsequence and (X^g_n, f^g_n) converges. The rest: T̄ → M̄_g is continuous; X^g_n ∈ V_0 by total geodesy; and φ̂_v(g) = g·(Y_v,η_v) = D(g) by F2\*(ii). ∎

So Lemma G′'s map φ exists for every G (product or not), it lifts canonically and continuously to φ̂: H → Â ⊂ Δ̂_G, and (F2) holds in the form used in Lemma T′ Step 1: π_v∘φ̂ = u. (Steps 1–3 of the proof of F2\* use only (GC1), not Def. FA; this is what the first part of the proof of Corollary Φ̂ uses.)

## 3. Lemma TR: the plumbing convergence of PR-H gives Def. FA (proved, modulo (Pl), (GC))

**Setting (from (Pl)).** X_n = X(z_n, t_n) with (z_n,t_n) → (0,0) in a plumbing chart at P, markings f_n induced by the (marked) plumbing family, so (X_n, f_n) → P̃ in T̄. For the vertex v: h_n: Y_v → Y_v(z_n) is quasiconformal, conformal off the fixed compact K_v, with ‖μ_{h_n}‖_∞ =: ε'_n → 0; Y^r_v := Y_v minus the coordinate discs {|z_e| ≤ r} at the punctures; for r ≥ r_n → 0, ι_n := h_n|_{Y^{r}_v}: Y^r_v → X_n is an embedding in the marking class (homotopic to the inclusion Σ_v ⊂ S). Let U ⊂ Y_v ∖ K_v be a non-empty connected open set on which ι_n is holomorphic.

**Lemma TR.** Assume ‖q_n‖_1 = 1 and ι_n^*q_n → q_v ≢ 0 locally uniformly on U (this is what PR-H Lemma PA provides for v = j, restricted to U; q_v ∈ Q(Y_v)). Then, after a subsequence, v carries q_v at scale 1 in the sense of Def. FA, and ∫_{Y_v}|q_v| ≤ 1. In particular PR-H Lemma PA yields "positive area at j" in the sense of Def. FA, so Theorem F2\* applies to it.

*Proof.*
(a) *Lifts and normalization.* Let σ be a holonomy of Y_v and Ỹ^r ⊂ H the preimage of Y^r_v (H minus a σ-invariant family of disjoint horodiscs; connected and simply connected). Let ρ_n be holonomies of (X_n, f_n). Since ι_n is in the marking class, it lifts to an embedding ι̃_n: Ỹ^{r_n} → H with ι̃_n∘σ(γ) = ρ_n(γ)∘ι̃_n (γ ∈ Γ_v). Fix x_0 ∈ Ỹ^{r_1}, and conjugate ρ_n so that ι̃_n(x_0) = x_0. The ι̃_n are (1+ε_n)-qc embeddings (ε_n → 0) of the domains int Ỹ^{1/k} (k fixed, n large) into H, omitting the lower half plane; by (QC1) and a diagonal argument a subsequence converges locally uniformly on H = ∪_k int Ỹ^{1/k} to a map ι̃ which on each int Ỹ^{1/k} is constant or a qc embedding.
Not constant: pick γ ∈ Γ_v with σ(γ) hyperbolic. If ι̃ ≡ x_0, then d(x_0, ρ_n(γ)x_0) = d(x_0, ι̃_n(σ(γ)x_0)) → 0, so the translation length of ρ_n(γ), which is ℓ_{X_n}(γ), tends to 0; but ℓ_{X_n}(γ) → ℓ_{Y_v}(γ) > 0 by (GC1). So ι̃ is a qc embedding, and conformal by Lemma Conv (Beltrami coefficients → 0 uniformly).
For γ ∈ Γ_v, ρ_n(γ)x_0 = ι̃_n(σ(γ)x_0) stays bounded, so {ρ_n(γ)} is relatively compact in PSL(2,R); after a diagonal subsequence (Γ_v countable) ρ_n|_{Γ_v} → R pointwise, and ι̃∘σ(γ) = R(γ)∘ι̃.
(b) *ι̃ is Möbius.* Let Ω := ι̃(H) ⊂ H and suppose Ω ≠ H. Then the hyperbolic metric of Ω is strictly larger than that of H at every point of Ω (strict Schwarz–Pick for the non-surjective inclusion), and ι̃: H → Ω is an isometry of hyperbolic metrics. Take γ with σ(γ) hyperbolic, x on its axis, and the segment c = [x, σ(γ)x] (H-length ℓ(σ(γ))). Then
  ℓ(R(γ)) ≤ d_H(ι̃x, R(γ)ι̃x) = d_H(ι̃x, ι̃σ(γ)x) ≤ length_H(ι̃c) < length_Ω(ι̃c) = ℓ(σ(γ)).
But ℓ(R(γ)) = lim ℓ(ρ_n(γ)) = lim ℓ_{X_n}(γ) = ℓ_{Y_v}(γ) = ℓ(σ(γ)) by (GC1) (translation length is a continuous function of the trace). Contradiction; so Ω = H and ι̃ ∈ PSL(2,R). Replacing ρ_n by ι̃^{-1}ρ_nι̃ and ι̃_n by ι̃^{-1}ι̃_n, we get ι̃_n → id locally uniformly on H and ρ_n|_{Γ_v} → σ.
(c) *Convergence on the preimage of U.* Let Ũ ⊂ H be the preimage of U ∩ Y^r_v (r small). There ι̃_n is holomorphic, so ι̃_n → id implies ι̃_n' → 1 locally uniformly. The lift of ι_n^*q_n is (q̃_n∘ι̃_n)(ι̃_n')², which → q̃_v locally uniformly on Ũ by hypothesis. Since ι̃_n^{-1} → id locally uniformly as well, q̃_n → q̃_v uniformly on compact subsets of Ũ.
(d) *Local boundedness and convergence on H.* Let L ⊂ H be a closed disc and L' a larger closed concentric disc. For n large, L' ⊂ Ỹ^{r_n} and ι̃_n(L') ⊃ L (a homeomorphism uniformly close to the identity on L' covers L, by a degree argument). The covering projection H → X_n restricted to ι̃_n(L') equals ι_n∘π_σ∘ι̃_n^{-1}, which is at most N(L')-to-one with N(L') := #{γ ∈ Γ_v : σ(γ)L' ∩ L' ≠ ∅} < ∞ (σ discrete, ι_n injective). Hence ∫_L |q̃_n| ≤ N(L')‖q_n‖_1 = N(L'). By the mean value inequality for holomorphic functions, {q̃_n} is uniformly bounded on smaller discs, i.e. locally bounded on H. By Montel every subsequence has a locally uniformly convergent subsequence; by (c) its limit equals q̃_v on the non-empty open set Ũ, hence on H (identity theorem). So q̃_n → q̃_v locally uniformly on H: Def. FA holds with η_v = q_v, s_n = 1.
(e) *Integrability.* For disjoint compact sets L'_1, …, L'_m ⊂ H each mapping injectively to Y_v with pairwise disjoint images, the sets ι̃_n(L'_k) map injectively and disjointly to X_n, so Σ_k ∫_{ι̃_n(L'_k)} |q̃_n| ≤ 1; letting n → ∞ (uniform convergence of q̃_n and of ι̃_n → id near the L'_k) gives Σ_k ∫_{L'_k}|q̃_v| ≤ 1, hence ∫_{Y_v}|q_v| ≤ 1. ∎

*Remark.* On K_v the maps ι_n are not holomorphic and "ι_n^*q_n" is not a quadratic differential; PR-H's phrase "converge locally uniformly on each component" therefore needs a reading on K_v (e.g. as differentials on the varying components Y_v(z_n)). Whatever reading is used there, its restriction to U ⊂ Y_v ∖ K_v is all that Lemma TR needs, and Lemma TR shows it implies the Fuchsian reading of Def. FA. I did not re-check PR-H Lemma PA itself (it is outside this task).

## 4. Step-by-step check of Lemma G, Lemma G′, Lemma T′ (task item 1)

### Lemma G
- Step 1 (X'_n ∈ V_0): **valid** — q_n ∈ Q_V(X_n) means the whole Teichmüller disc of (X_n,q_n) lies in V_0.
- Step 2 (K(g) independent of n): **valid** (Lemma B).
- Step 3: **valid**, using (Nbhd) in a marking with (X_n, f_n) → P̃ (GC3) and Maskit's lower bound Ext ≥ ℓ/π.
- Step 4: **valid** (Ext is K-quasi-invariant; Maskit's upper bound Ext ≤ (ℓ/2)e^{ℓ/2} turns a lower Ext-bound into a lower ℓ-bound).
- Step 5: **valid**, with this justification of the converse of (Nbhd): pick by (GC3) markings h_n with (X'_n,h_n) → P̃'; for small δ the curves of length < δ on X'_n are, for n large, exactly the γ_G-curves in the marking f'_n (Step 4) and exactly the pinched curves of P̃' in the marking h_n ((GC1) plus a positive lower bound on the lengths of the other curves of P̃'), so the dual graphs agree. Lemma G is also contained in Theorem F2\*(i), whose proof is independent.

### Lemma G′
- First sentence (uniform continuity of (M_g,d_T) → M̄_g): was only sketched; **now proved** (Corollary G′\*).
- Equicontinuity, Arzelà–Ascoli, well-definedness on SO(2)\SL(2,R): **valid**. (d_T(gX, g'X) = d_H(g,g') because Teichmüller discs are isometric.)
- Superseded by Corollary Φ̂, which in addition gives convergence for every g along one subsequence and the continuous marked lift φ̂ needed for non-product strata.

### Lemma T′
Hypothesis to be read as: v carries positive area in the sense of Def. FA (supplied by Lemma PA through Lemma TR).

- **Step 1**: valid **once (F2) is available — now Theorem F2\***; precisely, Corollary Φ̂ gives a continuous φ̂: H → Â ⊂ Δ̂_G with φ̂(i) = λ(P̃) and π_v∘φ̂ = u. For product-type G, φ = φ̂.
- **Step 2**: the conclusion is correct, but the argument as written ("a continuous lift … is holomorphic, since it is holomorphic off a discrete set and continuous") skips how φ lifts to the normalization at the singular points of A, and the case of components on which π_v is constant. **Repaired Step 2′** below.
- **Step 3**: **valid**, with the routine level-cover details spelled out in Step 3′ below; I add the identification C^ν = H/Γ′ (needed in Step 4′).
- **Step 4**: **gap**: it treats p = π_v∘ν: E^ν → C^ν as a finite map, so that p: E° → C° is a finite covering after removing finitely many points. But E is closed only in Δ_G (or Δ̂_G), not in M̄_g, and nothing a priori prevents an end of E (where some *other* component degenerates) from mapping to an interior point of C; then p is not proper and E° → C° need not be a covering. The orbifold-point case ("the same argument on a level cover") was also only asserted. **Repaired Step 4′** below; it shows a posteriori that p is proper and identifies the orbifold structure exactly.
- **Step 5**: **valid** (Masur's theorem that finite-area quadratic differentials have cylinders, cited; the Gauss–Bonnet argument: a flat disc bounded by a cylinder core needs interior curvature 2π, while zeros contribute ≤ −π each and the only possible puncture, a simple pole, contributes π).

**Step 2′ (φ̂ lifts holomorphically into one component).** Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G) is a closed algebraic subset of the quasi-projective Δ̂_G of dimension ≤ 1 (reading (R1) and §0); so it has finitely many irreducible components and finitely many singular points, and its normalization Â^ν → Â is a homeomorphism off the finite set Sing Â. Let p := π_v∘ν: Â^ν → M_{g_v,n_v}, holomorphic. Since u is non-constant, the set Z := u^{-1}(π_v(Sing Â)) is discrete in H, and φ̂(H ∖ Z) ⊂ Â ∖ Sing Â, where φ̂ lifts uniquely and continuously to φ^ν. For z_0 ∈ Z, a small punctured disc around z_0 is connected and is mapped by φ̂ into a small punctured neighbourhood of the point φ̂(z_0), which is a disjoint union of punctured branches; so it lies in one branch, and φ^ν extends continuously over z_0 by the corresponding point of Â^ν. Now p∘φ^ν = u. The union of the connected components of Â^ν on which p is constant is open and closed, so its preimage under φ^ν is open and closed in H; it is not all of H since u is non-constant; so it is empty. At z_0 ∈ H, with e_0 = φ^ν(z_0), choose local coordinates with p(ζ) = ζ^k (k ≥ 1) near e_0. Then (φ^ν)^k = u locally: a continuous k-th root of the holomorphic function u, holomorphic off the discrete zero set of u (where it is locally a branch of u^{1/k}), hence holomorphic by Riemann's removable singularity theorem. So φ^ν: H → Â^ν is holomorphic, non-constant, and (H connected) lies in a single connected component E^ν of Â^ν, the normalization of an irreducible component E of Â of dimension 1, with φ̂(i) ∈ E.

**Step 3′ (C is a Teichmüller curve; C^ν = H/Γ′).** C := closure of π_v(E) (an irreducible curve; π_v algebraic). Fix a level m ≥ 3, M[m] := T(Σ_v)/Mod_v[m] (a manifold; T(Σ_v) → M[m] a covering), and let C' be the component of the preimage of C containing u'(H), u' := (T → M[m])∘D. As in PR-F Step 3, u' lifts to the universal cover C̃ of C'^ν, C̃ ≅ H (Bers embedding: T is bounded, so C̃ is neither C nor P^1), and the lift Λ: C̃ → T with Λ∘ũ = D (both lifts of u' agree at a point after a deck transformation, hence everywhere) gives, by Royden (k_T = d_T) and Schwarz–Pick, that ũ ∈ Aut(H). Hence u': H → C'^ν is the universal covering. Let Γ′ := {γ ∈ Aut(H) : u∘γ = u}. Then the induced map H/Γ′ → C^ν is bijective: if u(x) = u(y), the images of x, y in C'^ν differ by an element of the finite group Stab(C')/Mod_v[m] acting on C'^ν with quotient C^ν; lifting that element through the universal covering u' gives γ ∈ Γ′ with u'(γx) = u'(y), and then y ∈ π_1(C'^ν)·γx ⊂ Γ′x. So C^ν = H/Γ′ as orbifolds, Γ′ is a lattice (C^ν is a curve of finite type), and Γ′ is the image in Aut(H) of the Veech group of (Y_v,η_v) (the elements γ with D∘γ = ψ_γ∘D for a mapping class ψ_γ).

**Step 4′ (E^ν = H/Λ_E; p is a proper orbifold covering).** Let Ē^ν, C̄^ν be the smooth compactifications and p̄: Ē^ν → C̄^ν the extension of p (a finite map of compact curves). Let C° ⊂ C^ν be C^ν minus: the orbifold points of H/Γ′, the branch values of p̄, and the (finitely many) points p̄(Ē^ν ∖ E^ν) ∩ C^ν. Put E° := p̄^{-1}(C°) ⊂ E^ν and H° := u^{-1}(C°) (H minus a discrete set; connected). Then p: E° → C° and u: H° → C° are coverings (the first is finite and unramified over C°), and φ^ν(H°) ⊂ E°.
- φ^ν(H°) = E°: the image is open (φ^ν is a lift of a covering through a covering, hence a local homeomorphism) and closed in E° (if φ^ν(z_k) → e ∈ E°, take an evenly covered disc B ∋ p(e) for both coverings; the z_k lie in sheets B_{α_k} of u over B, each φ^ν(B_{α_k}) is one of the finitely many disjoint sheets of p over B and contains φ^ν(z_k), so eventually it is the sheet through e); E° is connected.
- Hence φ^ν: H° → E° is a covering, and since u = p∘φ^ν with u Galois over C° with group Γ′, φ^ν|_{H°} is the quotient by the subgroup Λ_E := {γ ∈ Γ′ : φ^ν∘γ = φ^ν on H°} (= on H, by continuity). Λ_E has index deg p in Γ′.
- φ^ν descends to a holomorphic map h: H/Λ_E → Ē^ν; h is proper over C^ν, injective over C°, and of degree 1 relative to the two maps to C^ν, which both have degree [Γ′:Λ_E]. So h is a biholomorphism onto p̄^{-1}(C^ν). Since h(H/Λ_E) = φ^ν(H) ⊂ E^ν, we get p̄^{-1}(C^ν) ⊂ E^ν: **no end of E^ν lies over C^ν, i.e. p: E^ν → C^ν is proper**, and E^ν = H/Λ_E.
- With the orbifold structure of H/Λ_E on E^ν, p is the orbifold covering H/Λ_E → H/Γ′: at a point e over an orbifold point c of order m, the local degree k of p at e divides m and e gets orbifold order m/k. With this structure φ^ν is the orbifold universal covering, and the lift of π_v∘ν: E^ν → M_{g_v,n_v} to orbifold universal covers is D: H → T(Σ_v), an isometric holomorphic embedding onto the Teichmüller disc of (Y_v,η_v), equivariant for Λ_E ⊂ Γ′ → Mod(Σ_v).

This proves Lemma T′(1)–(3) in the strengthened form recorded in §5, for every G, the non-product case being handled on Δ̂_G.

## 5. The form needed by chain step 2 (task item 3)

**Theorem TV (every boundary piece has a Teichmüller vertex).** Let G be the dual graph of a boundary stratum (any G with at least one edge, product type or not), Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ Δ̂_G = ∏_w M_{g_w,n_w}, and E any 1-dimensional irreducible component of Â (no assumption that E meets closure(∂V_0)), with normalization ν: E^ν → E. Then there are a vertex j of G and an integrable quadratic differential η_j ≠ 0 on a curve Y_j ∈ π_j(E) such that, with D: H → T(Σ_j) the Teichmüller disc of (Y_j,η_j) and Γ′ ⊂ Aut(H) the (projectivized) Veech group:
1. C := closure of π_j(E) is a Teichmüller curve, C^ν = H/Γ′, and Γ′ is a lattice;
2. p := π_j∘ν: E^ν → C^ν is **proper** and E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p;
3. **orbifold structure**: give E^ν the orbifold structure of H/Λ_E, i.e. a point e over an orbifold point of C^ν of order m, at which p has local degree k, gets order m/k (k always divides m). Then p is an orbifold covering (orbifold-unramified), and the lift of π_j∘ν to orbifold universal covers is D, an isometric holomorphic embedding onto the Teichmüller disc, equivariant for Λ_E → Mod(Σ_j);
4. E is not compact, and every end of E^ν maps to a cusp of C (so along every end of E the j-component degenerates).
For product-type G (the case of the problem's Δ_Γ), Â = closure(V_0) ∩ Δ_G and ξ_G = id.

*Proof.* Pick P̂ ∈ E outside the finite set Sing Â ∪ (E ∩ other components) and outside the discrete exceptional set of PR-H Lemma PA, and let P = ξ_G(P̂). Lemma PA (PR-H, quoted; its proof is local in the plumbing chart at P, an orbifold chart of M̄_g whose fibres carry a labelling of components by V(G), hence it applies at P̂ ∈ Δ̂_G; and it uses only a ≠ 0 at P̂, true off a discrete set) gives generating pairs (X_n,q_n), ‖q_n‖ = 1, X_n → P along the branch of closure(V_0) through P̂, and a vertex j with q_j ≢ 0 (it maximizes the Teichmüller norm of the j-component of the tangent vector a of E at P̂). Lemma TR turns this into "j carries positive area" (Def. FA, η_j := q_j integrable, ∫|η_j| ≤ 1). Corollary Φ̂ gives φ̂: H → Â with φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂) and π_j∘φ̂ = u. Steps 2′, 3′, 4′, 5 of §4 then give 1–4; Step 2′ produces the component through φ̂(i) = P̂, which is E by the choice of P̂. ∎

**Caveats on item 3 (stated precisely).**
- The orbifold structure in (3) is the one *induced by Λ_E*; I have **not** shown that it coincides with the orbifold structure E inherits as a curve in the orbifold Δ̂_G (or M̄_g). They agree away from the finitely many points over orbifold points of C. If one prefers to avoid orbifolds, pass to a level-m cover: replace Γ′ by the torsion-free Γ′_m := π_1(C'^ν) and E^ν by a component of the fibre product E^ν ×_{C^ν} C'^ν normalized; then p becomes a genuine unramified finite covering of Riemann surfaces and the lift to universal covers is again D.
- Lemma PA is quoted, not re-proved, and in the non-product case its applicability on Δ̂_G rests on the labelled plumbing chart (Pl), which I have only described.
- The map φ̂ depends on the chosen subsequence; Theorem TV does not.

## 6. A by-product: the infinite-area remark of PR-F §3 (proved, given a non-zero scaled limit)

**Corollary AR.** In the problem's setting at t = 0 (Γ of product type, π_i(∂V_0) = {Y_0}, ∂V_0 := closure(V_0) ∩ Δ_Γ), let (X_n,q_n) be generating pairs with X_n → P ∈ ∂V_0, and suppose vertex i carries some η_i ≢ 0 at some scale s_n with arg s_n → θ (Def. FA; such a scale and limit is what the multi-scale compactness (F) of PR-F §0 provides — cited, not re-proved). Then every affine deformation of (Y_0, e^{iθ}η_i) is trivial in T(Σ_i): Y_0^{c\,\overline{η}/|η|} = Y_0 (marked) for all |c| < 1, where η := e^{iθ}η_i. Infinitesimally, ∫_{Y_0} φ η̄/|η| = 0 for every φ ∈ Q(Y_0).

*Proof.* By F2\*(iii) (which does not need integrability), for every g ∈ SL(2,R) and every limit P'_g of g·X_n, P'_g ∈ closure(V_0) ∩ Δ_Γ = ∂V_0 (X'_n ∈ V_0; F2\*(i) puts P'_g in Δ_Γ), so [Y_0^{c_g η̄/|η|}] = π_i(P'_g) = Y_0 in M_{g_i,n_i}. The map c ↦ [Y_0^{c η̄/|η|}] ∈ T(Σ_i) is continuous on the unit disc (the Teichmüller class depends continuously on the Beltrami coefficient in L^∞), and {c_g : g ∈ SL(2,R)} is the whole unit disc (c_g = β/α; e.g. g = diag(λ, 1/λ) composed with rotations). Its values lie in the discrete set Mod(Σ_i)·Y_0 ⊂ T(Σ_i) and it equals Y_0 at c = 0; the disc is connected, so it is constantly Y_0. Differentiating at c = 0 in every complex direction gives that the Beltrami differential c η̄/|η| is infinitesimally trivial for every c ∈ C, i.e. Re ∫ c φ η̄/|η| = 0 for all c, φ, i.e. ∫ φ η̄/|η| = 0 (Teichmüller's lemma: μ represents 0 iff ∫ μφ = 0 for all φ ∈ Q). ∎

(This is a necessary condition only; I do not derive a contradiction from it here.)

## 7. Summary: proved / not proved / open

**Proved here (modulo the cited facts (GC1)–(GC3), (Pl), (QC1)–(QC3), Royden, Bers embedding, Masur's cylinder theorem):**
- Lemma B, Lemma Conv, Lemma Conj, Lemma Lim (§1).
- **(F2) in full**, in the general form Theorem F2\* (any scale, any phase, no integrability, no area control, fixed g): the v-component of every limit of g·(X_n,q_n), marked through the Teichmüller maps, is g·(Y_v,η_v). Key point: the Beltrami coefficient of the Teichmüller map is the pointwise expression c_g q̄_n/|q_n|, and a.e. convergence of Beltrami coefficients passes to limits (QC2).
- Corollary G′\* (the sketched first sentence of Lemma G′) and Corollary Φ̂ (continuous marked lift φ̂: H → Â ⊂ Δ̂_G with π_v∘φ̂ = u, valid for non-product strata).
- Lemma TR: the plumbing convergence of PR-H Lemma PA implies the Fuchsian definition Def. FA, with integrable limit.
- Check of Lemma G (valid), Lemma G′ (valid, first sentence now proved), Lemma T′ (Steps 1, 3, 5 valid; Steps 2 and 4 had gaps — Step 2 a missing lifting argument, Step 4 an unjustified properness/finite-covering claim and an unproved orbifold case — both repaired as Steps 2′, 4′).
- Theorem TV (§5): every 1-dimensional component of every boundary piece (all strata, non-product ones on Δ̂_G, whether or not it meets closure(∂V_0)) has a Teichmüller vertex j, with π_j∘ν proper, E^ν = H/Λ_E, Λ_E ⊂ Veech group of finite index, orbifold-unramified for the H/Λ_E orbifold structure, lift = Teichmüller disc isometry.
- Corollary AR (affine rigidity of the constant vertex, given a non-zero scaled limit there).

**Quoted, not re-proved:** PR-H Lemma PA (and its use on Δ̂_G for non-product strata via the labelled plumbing chart); the standard facts listed in §0.

**Open / not established:**
- Whether the H/Λ_E orbifold structure on E^ν coincides with the orbifold structure E inherits from Δ̂_G at the finitely many points over orbifold points of C (only matters if a later step uses the inherited structure).
- Corollary AR is only a necessary condition; deriving the problem's claim from it (or from Theorem TV) is not attempted here — the remaining steps of the run's chain (Lemma R, Proposition K, the STAY issue described in PR-H §3) are outside this task and remain as they were.



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





### round11_q6 §4 (verbatim): Lemma TR
## 4. Second move: Thurston length-spectrum dominance for the Teichmüller vertex of a piece

**Setting.**
- E_0 is a 1-dimensional piece in a product-type stratum Δ_G, and E_t is its transport. A homeomorphism of curves maps irreducible components to irreducible components (they are the closures of the components of the complement of the non-manifold points). So H_t maps closure(E_0) ∩ Δ_G onto closure(E_t) ∩ Δ_G, and it induces homeomorphisms between the normalisations (it maps local branches to local branches), with punctures going to punctures.
- K_t is the normalisation of E_t, a punctured compact Riemann surface.
- By Theorem TV (entry 70) there is a vertex j such that f_0 := π_j ∘ ν_0 : K_0 → M_j is a proper orbifold covering of a Teichmüller curve C = H/Γ_C ⊂ M_j, and the ends of K_0 map to cusps.
- f_t := π_j ∘ ν_t : K_t → M_j.

**Hypothesis (OT).** The orbifold structure that f_t induces on K_t (cone points and their orders, read off from local lifts to T_j) is carried by H_t to that of K_0. Then the orbifold fundamental groups are all identified with one group G := π_1^orb(K_0). G is a lattice, because K_0^orb = H/G is a finite-area orbifold cover of C.

**Lemma TR.** Under (R1), (R2) and (OT), for every t the following hold.
- K_t is isometric to K_0, by an isometry homotopic to the map induced by H_t.
- f_t composed with this isometry equals f_0.

In particular closure(π_j(E_t)) = closure(π_j(E_0)) = C̄. The Teichmüller-vertex factor of every piece is t-independent.

*Proof.*
1. *Lifts.* Lift f_t to f̃_t : H → T_j, equivariant for ρ_t : G → Mod_j, and choose the lifts continuously in t. Mod_j is discrete and G is finitely generated, so ρ_t = ρ is independent of t. Let G_t ⊂ PSL_2(R) be the Fuchsian group of K_t^orb, marked by G.
2. *Contraction.* By Royden's theorem (also for T_{g,n}; cited from memory) the Teichmüller metric is the Kobayashi metric. The Poincaré metric, normalised to curvature -4, is the Kobayashi metric of H. Holomorphic maps contract Kobayashi distance, so d_T(f̃_t z, f̃_t w) ≤ d_H(z, w).
3. *t = 0.* The map f̃_0 is an isometric holomorphic embedding onto the Teichmüller disc D_0 of a Veech surface (X, q). ρ(G) preserves D_0 and acts on it as G acts on H. For hyperbolic γ ∈ G, ρ(γ) is affine with hyperbolic derivative, hence pseudo-Anosov, with Teichmüller translation length τ(ρ(γ)) = ℓ_0(γ).
4. *Bers (cited from memory).* For a pseudo-Anosov φ, d_T(x, φx) ≥ τ(φ), with equality exactly on the unique φ-invariant geodesic A_φ. Equality means the extremal map x → φx is a Teichmüller self-map of x in the class φ with dilatation λ_φ. Such a map is affine for some q on x, so x lies on the invariant geodesic, and that geodesic is unique. Here A_{ρ(γ)} ⊂ D_0.
5. *Length dominance.* For z on the axis of γ in H (acting through G_t):
   τ(ρ(γ)) ≤ d_T(f̃_t z, ρ(γ) f̃_t z) = d_T(f̃_t z, f̃_t(γz)) ≤ ℓ_t(γ).
   So ℓ_t(γ) ≥ ℓ_0(γ) for every hyperbolic γ.
6. *Thurston (cited from memory, "Minimal stretch maps between hyperbolic surfaces").* For complete finite-area marked hyperbolic structures X, Y on the same surface, sup_γ ℓ_Y(γ)/ℓ_X(γ) ≥ 1, with equality iff X = Y.
   - Pass to a torsion-free normal subgroup G' of finite index in G (Selberg). Both structures restrict to marked structures of the same type on H/G'. By step 5, sup ℓ_0/ℓ_t ≤ 1, so the two G'-representations are conjugate by some A.
   - For g ∈ G, the element ρ_0(g)^{-1} A ρ_t(g) A^{-1} centralises the lattice ρ_0(G'), so it is trivial.
   - Hence G_t = A G_0 A^{-1} as marked groups. Identify them, so ℓ_t = ℓ_0.
7. *Image lies in D_0.* Steps 4 and 5 are now equalities. Hence f̃_t(z) ∈ A_{ρ(γ)} ⊂ D_0 for every z on the axis of every hyperbolic γ. The axes of hyperbolic elements of a lattice are dense in H, and D_0 is closed. So f̃_t(H) ⊂ D_0.
8. *Conclusion.* D_0 is a closed complex submanifold and f̃_0 : H → D_0 is biholomorphic. So g_t := f̃_0^{-1} ∘ f̃_t is a holomorphic, G-equivariant self-map of H.
   - If g_t were not an automorphism, Schwarz–Pick would make it strictly contracting. Then for z on an axis, d(g_t z, γ g_t z) < ℓ_0(γ) = τ, which contradicts step 4.
   - So g_t is an automorphism commuting with the lattice G, and therefore g_t = id. Thus f̃_t = f̃_0. ∎

**Status of TR:** proved under (OT). Without (OT), cone points of K_t^orb could appear or disappear at t ≠ 0. I have not ruled this out, and the run has no statement covering it.

**Why TR cannot reach Y (dead end for MS11).**
- TR pins only the vertex j whose map is a Teichmüller-isometry. The constant vertex Y never enters it: π_i is constant on ∂V_t, so there is no length spectrum to compare.
- At a puncture-MOV endpoint of MS11, the moving Y_0-copy cannot be a Teichmüller vertex of the leaving piece. By TV, Teichmüller-vertex ends go to cusps of M̄_{g_i,n_i}, but F_x(Q_0) ≅ Y_0 is interior. So the moving copy is a non-Teichmüller moving vertex. Entry 81 (Examples Z, Z′) shows that fixing the Teichmüller vertex does not pin such vertices or their puncture values.
- What TR does add is that every cusp of every piece has a t-independent j-component. This supplies the "fixed Teichmüller vertex" hypothesis that entry 81 assumes, rather than taking it as given.



## Reminder
Give explicit verdicts (correct / correct after repair / gap) for Lemma PA, (F2) and Lemma T′, Corollary Φ̂, and each item of Theorem TV, with repairs and remaining dependencies.
