kind: write-up (consolidation into a complete, self-contained proof)

## Task
A research document on the problem stated below needs, as its "Part I", a complete and self-contained proof of a block of results about the geometry at t = 0 of the totally geodesic surface V_0 and its boundary in the Deligne–Mumford compactification. These results were found and refereed in earlier analyses; that material is spliced verbatim below, together with the referees' repairs. It is scattered, uses shifting notation, and in places refers to further texts not available to you.

Your job: write ONE coherent Markdown text "Part I" that states and proves the results listed below completely, in consistent notation, with every referee repair incorporated, so that a referee who sees ONLY your text (plus the problem statement) can check every step. Rules:
- Do not refer to the spliced analyses by name (no "round9_q4", "PR-H", "entry 85", "R7-4" etc.); the reader cannot see them. Write each argument out.
- Cite classical theorems explicitly by name/author and give the precise statement you use (e.g. Royden's theorem, Masur–Wolpert plumbing coordinates, Abikoff/Fenchel–Nielsen description of augmented Teichmüller space, Veech, Lehto–Virtanen, Remmert, Krull, Milnor conic structure, Mumford pull-back, Grauert's contractibility criterion, ...).
- Where a step cannot be completed from the material and your own reasoning, mark it "GAP:" with a precise description. A clearly marked gap is far better than a papered-over one. In particular the "routine marking identification along travel intervals" of the walk chain has never been written out: write it out, or mark it as a GAP.
- Say, for each result, exactly which hypotheses it uses (smoothness/closedness of V_0, total geodesy, the readings (R1)/(R2) below; most of these are statements about V_0 alone).
- If you find an error in the spliced material that you cannot repair, say so plainly at the top.

Results to be written up (make the statements precise yourself, following the spliced material):
- (I.1) Lemma PA: at a generic point of any 1-dimensional boundary piece of closure(V_0) (any stratum), the norming quadratic differentials of tangent vectors of V_0 at nearby smooth points have full-area limits supported on the vertices of maximal Teichmüller speed; in particular some vertex has positive area and a constant vertex has none.
- (I.2) Lemmas B, Conv, Conj, Lim; Theorem F2*; Corollary Φ̂; Lemma TR (round8 §3 version: plumbing convergence ⇒ "Def. FA"); the repaired Lemma T′ steps 2′–4′; and Theorem TV: every 1-dimensional boundary piece E of closure(V_0) in every stratum has a vertex j such that π_j∘ν is a proper orbifold covering of a Teichmüller curve C (C^ν = H/Γ′, E^ν = H/Λ_E), lifting to the Teichmüller disc, every end of E mapping to a cusp, E non-compact.
- (I.3) Lemmas CS, CL and Lemma J0 (at t = 0 the joint vertex map of every piece lifts holomorphically to T_G over H/Λ_E, isometric Teichmüller coordinate, coset-valued monodromy), with the repair R3′ for non-product strata.
- (I.4) Theorem X*_all (any stratum): for a piece E, Q_0 ∈ E and a lift β̃ of a branch of E, every irreducible component of the germ at 0 ∈ Def(Q_0) of q^{-1}(closure V_0) containing β̃ meets {∏ s_e = 0} near 0 only in β̃ — via Lemma P and the maximum-principle route (Steps 1–4, 5′).
- (I.5) Proposition K_w (the walk chain), with the repairs (R-a)–(R-d), the enlargement of Σ by the finite sets R(D) ("Gap A" repair), and Lemma S̃′ (entering and leaving lifts at each transition, and the terminal lift at the endpoint, lie in one irreducible component of q^{-1}(closure V_0) ∩ B). The final statement should be: starting from a generic point of ∂V_0 there are pieces D^1 ⊂ ∂V_0, ..., D^k, transition points J_m with entering/leaving lifts β̃_m, β̃′_m and chart labels x_m (the tracked Y_0-component), and an endpoint Q_0 with entering lift β̃, label x and terminal lift b̃ along which x MERGEs or MOVes at t = 0, with all the properties needed downstream (labels constant along travel intervals; x_m a constant vertex ≅ Y_0 of D^m; common irreducible component at each transition).
- (I.6) Corollary IMOV_all: a transition point lying in the stratum of either adjacent piece has equal entering and leaving lifts (same label), so the endpoint and every genuine transition are punctures of both adjacent pieces (property (P)); no interior-MOV endpoints.
Also include Lemma PT (in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type) since it is used with these.

Output format: a single Markdown document headed "Part I", with numbered conventions/definitions, statements and proofs, then "Cited classical facts" (each with a precise statement) and "GAPs" (possibly empty). Completeness matters more than brevity; up to about 25,000 words is fine. Begin with a one-paragraph status line saying what you achieved.

## Spliced material (verbatim; bookkeeping lines removed)
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






### Referee check of the above (round14 referee report, verbatim)
# round14_q10 — referee check of Lemma PA, (F2)/F2*, Lemma T′, Corollary Φ̂, Theorem TV, Lemma TR

**Plan / status.** I am checking, one inference at a time: (1) Lemma PA (round6_q9 §1); (2) round8_q10, namely Lemmas B, Conv, Conj and Lim, Theorem F2*, Corollaries G′* and Φ̂, Lemma TR (round8 §3), Steps 2′, 3′ and 4′ of Lemma T′, and Theorem TV items 1–4; (3) "Lemma TR".

**Naming clash.** Two different results are both called "Lemma TR":
- **TR₈** (round8_q10 §3): plumbing convergence ⇒ Def. FA, with an integrable limit. This is the one used for "positive area at j".
- **TR₁₁** (round11_q6 §4): Thurston length-spectrum rigidity of the Teichmüller vertex under (OT). It is *not* used for positive area.

The task attributes the positive-area use to round11 §4; that is a mislabel. I check both, TR₈ in §2.3 and TR₁₁ in §4.

**Status: complete.** Every item is correct or correct after minor repairs. All repairs are stated below. No substantive gap was found. The remaining dependencies are the facts cited from memory, listed in §5.

Readings used throughout:
- V_0 is a closed (in M_g), smooth, 2-dimensional subvariety.
- "Totally geodesic" means: every Teichmüller geodesic tangent to V_0 stays in V_0. Since V_0 is complex, every Teichmüller disc tangent to V_0 lies in V_0.
- (R1) is as in the task file. closure(V_0) is then a closed analytic subset of the projective coarse space M̄_g, hence algebraic (Chow).

---

## 1. Lemma PA (round6_q9 §1)

### 1.1 Cited facts
- **(Pl) Plumbing chart (Masur, Wolpert, Bers).** Standard and correctly stated, with one precision needed in Step 2: the Kuranishi family of each component should be taken *smooth*. Take Beltrami differentials μ_k that are smooth with compact support in K_w. Then the qc maps h_z: Y_w → Y_w(z) are smooth diffeomorphisms depending smoothly on z, and they converge in C^∞ to the identity on compacts as z → 0 (elliptic regularity of the Beltrami equation with smooth coefficients depending smoothly on parameters).
- **(Dual) Teichmüller duality.** Standard: ‖v‖_T = sup Re∫μφ, the sup is attained at a unique norming φ, and the extremal Beltrami of v is ‖v‖ φ̄/|φ|. So the Teichmüller disc tangent to v is the disc generated by the norming differential. This also holds on punctured surfaces, with Q = integrable differentials.
- **(Bun) Quadratic differentials at a stable curve.** Standard:
  - h^0(ω_X^{⊗2}) = 3g−3 on all stable curves, so π_*ω^{⊗2} is locally free.
  - The fibre at P consists of differentials with at most double poles at the nodes and matching quadratic residues. Check: with zw = t we have z^{−2}dz² = w^{−2}dw², so the matching is consistent.
  - The functionals a_e(φ) = (2πi)^{-1}∮_{|z|=r_0} zφ/dz pick out the z^{−2}-coefficient. They are holomorphic in the parameters, because for |t| < r_0 the circle lies in the fixed part of the plumbing region.
  - The dimension count is Σ_w(3g_w−3+n_w) + |E| = 3g−3.

### 1.2 Collar Beltrami (§1.2) — verified
Write L = log|t_0| and λ = log|z|/L.
- **Boundary values.** F_t(z) = z e^{cλ} equals z at |z| = 1 and equals z·t/t_0 at |z| = |t_0|.
- **w-coordinate.** In w' = t/F(z) one gets w' = (t_0/z)(t/t_0)e^{−cλ} = w (t/t_0)^{1−λ}, which is the identity at |w| = 1. So F_t glues to the identity off the collar, and it maps X(z,t_0) to X(z,t) in the marking class.
- **Beltrami coefficient.** ∂_zλ = ∂_{z̄}λ = 1/(2L) times 1/z and 1/z̄ respectively. Hence
  ∂_zF = e^{cλ}(1 + c/(2L)), ∂_{z̄}F = e^{cλ} c z/(2L z̄),
  μ = (z/z̄)(c/2L)/(1 + c/2L), as claimed.
- **Derivative.** Differentiating at c = 0 with c ≈ δ = (t−t_0)/t_0 gives the vector b∂/∂t_e with b = δ t_0, represented by a Beltrami of sup-norm |b|/(2|t_0| log(1/|t_0|)).

So (C) holds. Moreover — and this is what Step 2 really uses — this *explicit representative* has that sup-norm, which is stronger than a bound on the Teichmüller norm.

### 1.3 Step by step
- **Step 1 (local model).** Valid after a precision. One must take a branch N of the lifted germ of closure(V_0) whose image *contains* the germ of the component E of ∂V_0 through P. Such a branch exists because E ⊂ closure(V_0).
  - The factorization t_e = u_e τ^{m_e} then needs only that t_e vanishes on ν^{-1}(E) = {τ = 0} and that u_e is not divisible by τ. The zero set of u_e|_{τ=0} is discrete, as stated. Other components of {∏t_e = 0} ∩ N are harmless: they only make u_e vanish at isolated points of {τ = 0}, which are excluded.
  - Genericity excludes a discrete subset of E: singular points of N and of ν^{-1}(E); points where ν^{-1}(E) → E is not an immersion; zeros of u_e|_{τ=0}; points where a = ∂_s z = 0.
  - a_i = 0: on the lifted chart, z_i(s,0) is a continuous map into the finite fibre over Y_0, hence constant. Valid.
- **Step 2.** Valid.
  - The chart Def(P) away from {∏t_e = 0} is a local chart of T_g, so v_n is a Teichmüller tangent vector, non-zero because V_0 is smooth.
  - The bound |∂_s t_e| ≤ C|t_e| holds because u_e is a unit.
  - The collar part ν_n has ‖ν_n‖_∞ ≤ C/(2 log(1/|t_e|)) → 0 by §1.2.
  - The z-part: by the smooth version of (Pl), the vector ∂/∂z_k at z_n is represented by h_{z_n,*}(μ̂_k(z_n)), with μ̂_k depending continuously on z in C^0. Since ∂_s z(s_0,τ_n) → a, we get μ_w^{(n)} → μ_w representing a_w, with μ_i^{(n)} → 0.
- **Step 3 (upper bound).** Valid.
  - Normal families: |φ| is subharmonic in local coordinates, so the mean-value inequality plus ‖φ_n‖_1 ≤ 1 gives local bounds on the fixed thick parts.
  - An integrable holomorphic quadratic differential on a punctured disc has at most a simple pole. So φ_w ∈ Q(Y_w), and Fatou gives Σ‖φ_w‖ ≤ 1.
  - Convergence of ∫_{h_n(K_w)} μ_w^{(n)} φ_n: by the change of variables h_n, this is ∫_{K_w} (h_n^*μ_w^{(n)})(h_n^*φ_n). Here h_n → id in C^1 and the integrands converge uniformly. This is the precise reading of "transplanted" that the smooth (Pl) supplies; round8's remark on K_v asked for exactly such a reading. **Repair: reading supplied.**
  - Then (Dual) on each Y_w gives Re∫μ_wφ_w ≤ ‖a_w‖ ‖φ_w‖. Applied to near-norming φ_n, this gives limsup ‖v_n‖ ≤ A.
- **Step 4 (lower bound).** Valid.
  - Since φ ⊕ 0 has a_e = 0, it lies in the subbundle ker(a_e), which is a holomorphic subbundle near P because the a_e are independent there. Its section φ_n converges to φ ⊕ 0 on the thick parts (continuity of the family).
  - Collar mass. For the terms with k ≥ −1, Cauchy on |z| = r_0 gives |c_k| ≤ M r_0^{−k}. For the terms with k ≤ −3, rewrite them as c_k t^{k+2} w^{−k−4} dw² with exponent ≥ −1 and use Cauchy on |w| = r_0. The k = −2 term vanishes.
  - So on {|t|/ρ < |z| < ρ} the mass is at most the mass of the first group on |z| < ρ plus that of the second group on |w| < ρ. This is ≤ Cρ, since ∫_{|z|<ρ}|z|^{−1} = 2πρ and the geometric tails are bounded by 2.
  - The tail of φ near the punctures of Y_j is small because φ has at most simple poles. Hence ‖φ_n‖_1 → 1. After normalizing, Re∫μ_nφ_n → Re∫μ_jφ = A.
- **Step 5.** Valid.
  - The norming q_n of v_n generates the disc tangent to v_n (Dual), which lies in V_0 (total geodesy). So (X_n,q_n) is a generating pair.
  - The chain of inequalities is forced to be equalities. Hence: Σ‖q_w‖ = 1; q_w ≠ 0 ⇒ ‖a_w‖ = A (if ‖a_w‖ < A and q_w ≠ 0 the second inequality would be strict); some q_j ≠ 0; and j ≠ i because a_i = 0 < A.

**Verdict on Lemma PA: correct after (minor) repair.** The repairs are: the choice of a branch containing E; the genericity list; and smooth Kuranishi data, so that the "transplanted" pairing on K_w is meaningful and converges.

For Theorem TV only item 3 of PA is needed, for an arbitrary 1-dimensional component E of Â (no constant vertex). The proof uses only the local model and a ≠ 0. On non-product strata the plumbing chart Def(P) carries the labelling of components by V(G), so the argument is unchanged.

---

## 2. round8_q10

### 2.1 Elementary lemmas
- **Lemma B: correct.**
  - Solving αζ+βζ̄ = (α+β)x + i(α−β)y against the matrix gives α+β = g11 + i g21 and α−β = g22 − i g12. This yields the stated α, β, and |α|²−|β|² = g11g22 − g12g21.
  - The μ computation is correct, since q̄/|q| = \overline{ζ_z}/ζ_z · dz̄/dz.
  - The rescaling identity is correct.
  - Convention check: K(diag(e^s,e^{−s})) = e^{2s}, and ½ log K = s is distance in the curvature −4 metric. This is consistent with d_T = ½ log K.
- **Lemma Conv: correct.**
  - h_n = f_n∘w_n^{-1} is conformal on w_n(D) because μ_{f_n} = μ_{w_n} on D.
  - Uniform convergence on L follows from |f_n(w_n^{-1}x) − f(w^{-1}x)| ≤ sup_{L'}|f_n − f| + ω_f(|w_n^{-1}x − w^{-1}x|). Here only uniform continuity of f on L′ is needed, not equicontinuity of the f_n.
  - The cited facts (QC1) and (QC2) are standard and correctly stated (Lehto–Virtanen; Ahlfors).
- **Lemma Conj: correct.**
  - Two facts cited about a discrete subgroup of PSL(2,R): two hyperbolic elements cannot share exactly one fixed point, and if they share both they commute. Both are standard.
  - tr² is continuous, so σ(γ_i) is hyperbolic.
  - B_n matches converging attracting and repelling fixed points; three distinct points determine a Möbius map continuously.
- **Lemma Lim: correct.**
  - The normalization M_n exists because the boundary extension of F̃_n preserves the cyclic order on R̂.
  - Uniform limits of Möbius maps that converge to a homeomorphism are Möbius.
  - Discreteness follows from proper discontinuity, which is preserved under conjugation by a homeomorphism. Type preservation follows from counting and locating fixed points.
  - The hypotheses "non-elementary, finite area" are not used. That is harmless.

### 2.2 Theorem F2*, Corollary G′*, Corollary Φ̂

**(GC1–3).** These are standard (Abikoff; Fenchel–Nielsen description of augmented Teichmüller space): a sequence converges to a point of the γ-stratum iff the γ-lengths tend to 0 and the FN coordinates of the non-pinched curves converge. The restricted-holonomy formulation is correctly stated. In GC2 the FN coordinates inside Σ_w are continuous functions on the representation variety near the type-preserving R_w, including at boundary length 0 (trace formulas).

**Theorem F2*: correct.**
- Step 1: Beltrami coefficients lift.
- Step 2: Lemma Lim applies to B^w_nρ_n(B^w_n)^{-1} with the maps F̃_n(B^w_n)^{-1}. The limit H/R′_w is a qc image of a finite-area surface with all peripherals parabolic. So it has no funnels and has finite area, as GC2 requires.
- Step 3: ℓ_{X'_n}(γ_e) → 0, using Maskit's comparison (cited, standard) and the K-quasi-invariance of extremal length. The uniqueness-of-limit argument is valid (T̄ is Hausdorff).
- Step 4: a.e. convergence of the phase off the discrete zero set of η̃_v; Lemma Conv on discs; equal Beltrami coefficients give a conformal Φ∘ι_g^{-1}; it preserves the marking and the labels of the punctures.
- Integrability is indeed not used.

**Corollary G′*: correct.** With μ → 0, Lemma Conv makes F̃ Möbius, so the components are equal as marked surfaces. A point of the γ-stratum is determined by its components.

**Corollary Φ̂: correct.**
- Comparison maps F^{g_l}_n∘(F^{g_k}_n)^{-1} are affine of derivative g_lg_k^{-1} for g_k·q_n.
- Lemma Lim produces a K_{kl}-qc map in the marking class. Lemma Conj identifies the target with P̃^{g_l}_w: its hypothesis is met with ρ_n the GC1-normalized holonomies of X^{g_l}_n, which converge to σ^l_w.
- Hence d_T(P̃^{g_k}_w, P̃^{g_l}_w) ≤ d_H(g_k,g_l). The metric is well defined on SO(2)\SL(2,R) because K is bi-SO(2)-invariant.
- The extension uses completeness of T(Σ_w). Convergence for every g along the single subsequence follows by the same comparison.
- X^g_n ∈ V_0 because V_0 is closed and totally geodesic, so the whole disc of a generating pair lies in V_0. Hence φ̂(H) ⊂ Â.
- φ̂_v = D under Def. FA follows from F2*(ii).
- The basepoint: φ̂(SO(2)) = λ(lim of (X_n,f_n)). With plumbing markings this is P̂.

### 2.3 Lemma TR₈ (round8 §3): correct
- **(a) Normal families.** The lifted (1+ε_n)-qc embeddings omit the lower half-plane, so they form a normal family. The limit is non-constant, because otherwise the translation length of ρ_n(γ) would tend to 0, contradicting GC1. It is conformal by Lemma Conv. ρ_n(γ) moves x_0 a bounded amount, so (ρ_n(γ)) is precompact.
- **(b) The limit is Möbius.** Strict Schwarz–Pick for a proper simply connected subdomain Ω ⊊ H, combined with ℓ(R(γ)) = ℓ_{Y_v}(γ) from GC1 and continuity of trace, is a correct contradiction. So ι̃ is Möbius.
- **(c) Convergence on Ũ.** Holomorphic convergence gives ι̃_n' → 1. Inverting the composition is valid.
- **(d) Convergence on H.** The multiplicity bound N(L′) is correct because ι_n is injective on Y^{r_n}. Then the mean value inequality, Montel, and the identity theorem give convergence on all of H.
- **(e) Integrability.** Correct.

The only input from PA is the convergence on an open set U ⊂ Y_v∖K_v, where ι_n is holomorphic. This is exactly what Lemma PA's conclusion provides.

### 2.4 Lemma T′ Steps 2′, 3′, 4′ and Theorem TV

**Step 2′: correct after one minor repair.**
- Z is discrete because u is non-constant and π_v(Sing Â) is finite. u is non-constant because D is an isometric embedding and T → M has discrete fibres.
- Punctured discs map into a single punctured branch. If φ̂(z_0) were an isolated point of Â, φ̂ would be locally constant, contradicting non-constancy of u.
- The constant-component argument is correct.
- **Repair.** The target M_{g_v,n_v} (coarse space) may be singular, so "local coordinates with p(ζ) = ζ^k" must be read as follows. Choose a holomorphic function f near p(e_0) on the normal analytic space M_{g_v,n_v} (e.g. an invariant coordinate in an orbifold chart) with f∘p non-constant on the branch. Choose ζ with f∘p = ζ^k. Then (ζ∘φ^ν)^k = f∘u is holomorphic, so ζ∘φ^ν is a continuous k-th root of a holomorphic function, hence holomorphic (Riemann). The rest is unchanged.

**Step 3′: correct after a cosmetic repair.**
- The level-m cover, the lift Λ through T → M[m], and C̃ ≅ H (T bounded, Liouville) are all valid.
- Λ∘ũ = D after adjusting Λ by a deck transformation. D is isometric for Kobayashi = Teichmüller (Royden; cited, standard, valid for all T_{g,n}). Λ and ũ are contractions, so ũ preserves d_H and is in Aut(H).
- **Repair.** Γ′ should be defined through the lift u^ν: H → C^ν, as {γ : u^ν∘γ = u^ν}, rather than through u. Defining it through u could identify points on different branches of C at its singular points. With this definition the bijectivity argument via Stab(C′)/Mod_v[m] is correct, and C^ν ≅ C′^ν/Stab(C′) holds because a finite birational map between normal curves is an isomorphism.
- Γ′ ⊃ π_1(C′^ν) with finite index, and π_1(C′^ν) is a lattice (C′^ν is an algebraic curve), so Γ′ is a lattice.

**Step 4′: correct.** I re-checked each point:
1. **Coverings over C°.** p: E° → C° is a finite unramified covering: it is the restriction of p̄ to a full preimage, and E° ⊂ E^ν because the images of the punctures were removed. u^ν: H° → C° is the regular Γ′-covering, since Γ′ acts freely off the orbifold points.
2. **φ^ν is a covering.** φ^ν is a local homeomorphism (locally φ^ν = p^{-1}∘u^ν). Its image is open and closed in the connected E°, by the sheet argument. A continuous surjection φ with p∘φ and p both coverings is itself a covering (locally path-connected spaces).
3. **Λ_E.** Intermediate covers of a regular covering are quotients by subgroups, so φ^ν|_{H°} is the quotient by Λ_E, of index deg p.
4. **h is a biholomorphism.** The map h: H/Λ_E → p̄^{-1}(C^ν) is holomorphic (invariant holomorphic maps descend). It is proper, because H/Λ_E → C^ν is finite. It is injective over the dense C°. The target is connected (Ē^ν minus finitely many points). A proper holomorphic map that is injective on a dense open set has degree 1, hence is a biholomorphism.
5. **Properness of p.** Hence p̄^{-1}(C^ν) = φ^ν(H) ⊂ E^ν ⊂ p̄^{-1}(C^ν), so E^ν = p̄^{-1}(C^ν) and p: E^ν → C^ν is proper.

**On round13_q9's remark.** Properness of p_E is **not assumed** in Step 4′. It is **derived**, from Φ̂ (through Step 2′, φ^ν: H → E^ν with p∘φ^ν = u^ν) together with the fact that u^ν is the orbifold universal covering of C^ν = H/Γ′ (Step 3′). So item 2 and the properness in item 4 are both proved.

**Theorem TV item by item.**
- **Item 1: correct after the Step 3′ repair.**
  - Here C is the closure of π_j(E) *in M_{g_j,n_j}*, an irreducible algebraic curve: π_j(E) is constructible, E being algebraic by Chow.
- **Item 2: correct** (Step 4′).
- **Item 3: correct.**
  - At a point of H over c, Stab_{Γ′} ≅ Z/m, and Stab_{Λ_E} is a subgroup Z/m′. The local degree is k = m/m′, so k | m and the cone order is m′ = m/k. Hence p is an orbifold covering for the Λ_E-structure.
  - The lift to universal covers is D, since π_j∘ν∘φ^ν = proj∘D.
  - As round8 itself notes, nothing is claimed about the orbifold structure E inherits from Δ̂_G.
- **Item 4: correct, with one cited fact.**
  - "Ends map to cusps" follows from properness of p: E^ν → C^ν. Also C^ν → M_{g_j,n_j} is proper because C is closed in M_{g_j,n_j}. So along each end of E^ν the j-component leaves every compact subset of M_{g_j,n_j}, i.e. degenerates.
  - "E is not compact" needs Γ′ to be non-cocompact. **Cited fact (from memory, Veech 1989; standard):** the Veech group of a lattice surface contains parabolic elements, so Teichmüller curves are never compact. For example, a cylinder direction exists (Masur) and is parabolic by the Veech dichotomy. Then Λ_E, of finite index in Γ′, is non-cocompact as well, and E^ν = H/Λ_E is non-compact.
  - This citation is not made explicit in round8. **Repair: the citation is supplied.**
- **Proof of TV (choice of P̂).** Valid. Choose P̂ ∈ E generic and off the other components and Sing Â. Then Step 2′ lands in E, and φ̂(i) = P̂.

---

## 3. Lemma T′ Steps 1, 3, 5 and Lemmas G, G′
Step 1 is subsumed by Φ̂ (checked above). Step 3 is subsumed by Step 3′ (checked above). Step 5 (Gauss–Bonnet for a flat disc bounded by a cylinder core) is correct:
- turning curvature 2π is needed;
- each zero contributes ≤ −π;
- a simple pole contributes π.

So at least two poles would be needed, i.e. the curve is not peripheral (it is not around a single puncture). It is not needed for TV.

Lemmas G and G′ are subsumed by F2*(i) and Corollary G′*, both correct.

---

## 4. Lemma TR₁₁ (round11_q6 §4) — correct under (OT), with one implicit hypothesis

1. **Lifts.** f_t is an orbifold map for the (OT) structure, so it lifts. ρ_t is constant because it varies continuously in t (lifts chosen continuously via H_t) and Mod_j is discrete with G finitely generated. **Implicit hypothesis:** the continuity of f_t∘H_t in (x,t), which follows from continuity of H and of π_j∘ν. State it.
2. **Contraction.** Royden/Kobayashi contraction (cited; standard for T_{g,n}). Valid.
3. **t = 0.** Hyperbolic elements of the Veech group act by pseudo-Anosov affine maps (Veech; cited, standard). The translation length is ℓ_0(γ) in the curvature −4 normalization. The convention must be the same as in step 5, and it is.
4. **Bers' theorem** (cited; standard, also for punctured surfaces). For pseudo-Anosov φ, inf_x d_T(x,φx) = ½ log λ(φ). It is attained exactly on the axis, and the axis is unique. Valid.
5. **Length dominance.** ℓ_t ≥ ℓ_0 on hyperbolic elements. Valid.
6. **Thurston's theorem** (cited; "Minimal stretch maps", 1986; it holds for complete finite-area structures). It requires the identification G_0 ≅ G_t to be type-preserving. This holds because it is induced by the homeomorphism H_t of orbifolds, which sends punctures to punctures and cone points to cone points of equal order under (OT). Passage to a torsion-free normal subgroup G′ of finite index (Selberg) and the centraliser argument (a lattice has trivial centraliser in PSL(2,R)) are valid.
7. **Image in D_0.** Equality forces f̃_t(z) onto the axes. The axes are dense (lattice), and D_0 is closed (isometric image of a complete space). Valid.
8. **Conclusion.** D_0 is a closed complex submanifold, so g_t is holomorphic. If g_t were not an automorphism, strict Schwarz–Pick would contradict Bers. An automorphism commuting with a lattice is the identity. Valid.

**Verdict:** correct under (OT) and continuity of the family. Its own stated limitation stands: without (OT), cone points of K_t could change.

TR₁₁ plays **no role** in positive area at j. That role is played by Lemma PA + TR₈.

---

## 5. Verdicts / repairs / remaining dependencies

**Verdicts.**

| Result | Verdict |
|---|---|
| Lemma PA | **correct after minor repair** (see repairs 1–2 below) |
| Lemmas B, Conv, Conj, Lim | **correct** |
| (F2) = Theorem F2* | **correct** |
| Lemma T′ Steps 1, 3, 5 | **correct** (1 and 3 via Φ̂ and Step 3′) |
| Lemma T′ Step 2′ | **correct after repair** (local coordinate on the singular coarse target) |
| Lemma T′ Step 3′ | **correct after cosmetic repair** (Γ′ defined via u^ν) |
| Lemma T′ Step 4′ | **correct** |
| Corollary G′* | **correct** |
| Corollary Φ̂ | **correct** |
| Lemma TR₈ (round8 §3) | **correct** |
| Lemma TR₁₁ (round11 §4) | **correct under (OT)**, with the continuity of the family made explicit; it is not the result used for positive area |
| Theorem TV item 1 | **correct after the Step 3′ repair** (C is the closure in M_{g_j,n_j}) |
| Theorem TV item 2 | **correct**: properness of p_E is derived in Step 4′, not assumed, so round13_q9's reduction is discharged |
| Theorem TV item 3 | **correct**, for the Λ_E-induced orbifold structure (as round8 states) |
| Theorem TV item 4 | **correct**, given the cited non-cocompactness of Veech lattices for "E not compact"; "ends map to cusps" follows from properness |

**Repairs made here.**
1. In PA Step 1: choose a branch containing E, and give the explicit discrete exceptional set.
2. In PA Steps 2–3 (and the round8 §3 remark): use smooth Kuranishi data, so that transplanted Beltrami and quadratic differentials converge in C^0 on K_w. This gives the precise reading of "locally uniform convergence of ι_n^*q_n".
3. In Step 2′: use a holomorphic function f on the possibly singular coarse space instead of a coordinate.
4. In Step 3′: define Γ′ using the lift u^ν: H → C^ν.
5. In item 4: cite explicitly that Teichmüller curves are never compact.
6. In TR₁₁: state the continuity-in-t hypothesis explicitly.

**Remaining dependencies (all cited from memory; all standard and, as far as I can judge, correctly stated):**
- (Pl) with smooth Kuranishi data; (Dual); (Bun);
- (GC1–3) (Abikoff / FN description of T̄);
- (QC1–3) (Lehto–Virtanen, Ahlfors);
- Maskit's extremal-length comparison;
- Royden's theorem (Kobayashi = Teichmüller);
- the Bers embedding (T bounded);
- Chow's theorem;
- Masur's cylinder theorem and Veech's non-cocompactness of lattice Veech groups;
- for TR₁₁ only: Bers' pseudo-Anosov axis theorem, Thurston's stretch-map theorem, Selberg's lemma.

**Open (unchanged by this check):**
- The comparison of the Λ_E-orbifold structure with the inherited one.
- Hypothesis (OT) in TR₁₁.
- The downstream steps of the run's chain (STAY branches, MS11), which were outside this task.

This check establishes the Theorem TV / Corollary Φ̂ / Lemma PA layer that Lemma J0 and Theorem RO rely on. It does not by itself prove the problem's claim Y_t = Y_0.


### Lemmas CS, CL, J0 (verbatim §§1–3 of a later analysis)
## round12_q9 (verbatim): Lemmas CS, CL, J0, Prop. T, Lemma R*′, Theorem RO
# round12_q9 — attempt on (Rig) (ledger entry 82)

**Plan/status line (written first).** Brief read in full.
1. Item 1 ((Rig) under the coarse reading (R2)): I found no global argument. I record a new reduction (§7).
2. Item 2 ((Rig) under the orbifold reading): I formalise (R2^orb) as an equivariant lift of H on every stratum (§1). Then:
   - (H_0) holds for the **joint** vertex map of every piece at t = 0, over the Veech-type orbifold structure Λ_E. This is Lemma J0, derived from Theorem TV and Corollary Φ̂ of round8_q10. It is what makes Example Z irrelevant at t = 0.
   - (R2^orb) transports this joint lift (§4).
   - Lemma R* with set-valued monodromy, plus Imayoshi–Shiga, then gives (Rig) for all pieces in all strata, product or not (§5–§6).
3. The weakest form proved, the cited inputs, and the open questions are listed in §8.

---

## 1. Readings and conventions

(R1) and (R2) are as in the task: H is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, H_0 = id, mapping strata to strata.

**Stratum notation.** For a stable graph G with at least one edge:
- T_G := ∏_{w∈V(G)} T_w, where T_w is the Teichmüller space of type (g_w, n_w) with labelled special points.
- Mod_Π := ∏_w Mod_w, where Mod_w is the pure mapping class group.
- p : T_G → ∏_w M_w = T_G/Mod_Π is the quotient (coarse spaces).
- Mod_G ⊃ Mod_Π is the finite extension, by lifts of Aut(G), for which [T_G/Mod_G] is the stratum Δ_G as a sub-orbifold of M̄_g. Its isotropy groups are the Aut(z), modulo generic automorphisms.
- ξ_G : ∏M_w → Δ_G is the finite quotient map.
- A_t := closure(V_t) ∩ Δ_G, Â_t := ξ_G^{-1}(A_t) ⊂ ∏_w M_w, and Ã_t := p^{-1}(Â_t) ⊂ T_G.

All groups act properly discontinuously by biholomorphisms, and they are countable.

**Reading (R2^orb) (formal version used here).** For every stratum G there is a continuous map H̃ = H̃^G : Ã_0 × Δ → T_G, written H̃_t := H̃(·, t), such that for all t:
- (a) H̃_t lifts H_t: ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
- (b) H̃_t is Mod_G-equivariant: H̃_t(g x) = g H̃_t(x) for all g ∈ Mod_G;
- (c) H̃_t preserves isotropy: Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x);
- (d) H̃_0 = id.

*Why this is the content of "H restricted to each stratum is an orbifold isomorphism, compatible with the charts Def(z)/Aut(z)".*
- Near ẑ ∈ T_G over z, the chart Def(z) → Def(z)/Aut(z) is a Stab(ẑ)-invariant neighbourhood of ẑ in T_G, modulo Stab(ẑ) ≅ Aut(z).
- A family of orbifold maps of the global quotient [Ã_0/Mod_G] into [T_G/Mod_G] that starts at the identity is represented by an equivariant lift, with equivariance through an automorphism of Mod_G. Since t ↦ that automorphism is continuous into a discrete set and is the identity at t = 0, it is the identity.
- (c) is "preserves isotropy groups".
- I do **not** prove that a purely local formulation (local equivariant lifts at each z, with no coherent choice) implies the global one. That is a gap in the *interpretation*, not in the proofs below: every later use of (R2^orb) is a use of (a)–(d).

**Uses of (R2^orb)** are marked [orb] below. Everything not marked uses only (R1) and (R2).

**Lemma 1.1 [orb] (descended transport).** H̃_t descends to a map Π_t : Â_0 → Â_t (so p∘H̃_t = Π_t∘p) with the following properties:
- Π_t is a homeomorphism;
- ξ_G∘Π_t = H_t∘ξ_G;
- (x, t) ↦ Π_t(x) is continuous;
- Π_t maps each piece (1-dimensional irreducible component) of Â_0 onto a piece of Â_t, and every piece at time t arises this way.

*Proof.*
- **Descends.** By (b) for g ∈ Mod_Π, H̃_t descends. By (a) the descended map lands in Â_t, because ξ_G p H̃_t(x) = H_t(ξ_G p x) ∈ A_t.
- **Injective on Ã_0.** If H̃_t x = H̃_t y, then by (a) and injectivity of H_t we get ξ_G p x = ξ_G p y, so y = g x for some g ∈ Mod_G. Then g H̃_t x = H̃_t x. By (c), g ∈ Stab(H̃_t x) = Stab(x), so y = x.
- **Surjective onto Ã_t.** Let y ∈ Ã_t. Then ξ_G p y = H_t(ξ_G p x) = ξ_G p H̃_t x for some x ∈ Ã_0, so y = g H̃_t x = H̃_t(g x).
- **Π_t is bijective.** Injectivity: if Π_t(p x) = Π_t(p y), then H̃_t x = g H̃_t y = H̃_t(g y) with g ∈ Mod_Π, so x = g y. Surjectivity is immediate from the surjectivity of H̃_t.
- **Continuity.** H̃ is continuous and p is open, so Π_t is continuous, jointly in (x, t).
- **Continuity of Π_t^{-1}.** Let y_n → y and x_n := Π_t^{-1} y_n. Then ξ_G(x_n) = H_t^{-1} ξ_G(y_n) converges. Since ξ_G is finite, hence proper, the x_n lie in a compact set. Every limit point x satisfies Π_t x = y, so x_n → Π_t^{-1}y.
- **Pieces.** A homeomorphism of 1-dimensional analytic sets maps isolated points to isolated points, and irreducible components of the 1-dimensional part to irreducible components. The latter are the closures of the connected components of the set of points with a disc neighbourhood (round8_q7 Lemma S″, argument re-checked). ∎

For a piece E_0 of Â_0, put E_t := Π_t(E_0). Its normalisation is ν_t : Ê_t → E_t. Π_t lifts to a homeomorphism Ĥ_t : Ê_0 → Ê_t with ν_t∘Ĥ_t = Π_t∘ν_0, because local branches are the components of punctured links (round5_q4 §2.1).

**Ê_t has finite type with puncture ends.** The closure of ξ_G(E_t) in M̄_g is a component of the compact analytic set closure(V_t) ∩ closure(Δ_G). So its normalisation is a compact Riemann surface minus finitely many points. Ê_t maps finitely onto that normalisation, and a finite unbranched cover of a punctured disc is a disjoint union of punctured discs. Hence Ê_t is a compact Riemann surface minus finitely many points, and Ĥ_t maps punctures to punctures.

## 2. Two lifting lemmas (proved; no hypothesis beyond the setting)

Throughout §2, Γ is a countable group acting properly discontinuously by biholomorphisms on a complex manifold T. X := T/Γ carries Cartan's quotient analytic structure, and p : T → X is the quotient map. Q is a connected Riemann surface.

**Lemma CS (two holomorphic lifts differ by one group element).** Let F, F′ : Q → T be holomorphic with p∘F = p∘F′. Then F′ = g∘F for some g ∈ Γ. The set of such g is a coset g·S_F, where S_F := {s ∈ Γ : s∘F ≡ F} is a finite group.

*Proof.*
- Q = ∪_{g∈Γ} Z_g, where Z_g := {y : F′(y) = gF(y)}.
- Each Z_g is a closed analytic subset of Q, and Γ is countable. By Baire, some Z_g has interior.
- By the identity theorem F′ ≡ gF.
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. Finally S_F ⊂ Stab(F(y)), which is finite. ∎

**Lemma CL (continuous lifts of holomorphic maps are holomorphic).** Let h : Q → X be holomorphic and L : Q → T continuous with p∘L = h. Then L is holomorphic.

*Proof.* The statement is local. Fix y_0 and put x̂ := L(y_0), A := Stab_Γ(x̂) (finite).

**Chart.** By Cartan there is an A-invariant neighbourhood B of x̂ such that:
- B is A-equivariantly a ball with linear A-action;
- gB ∩ B ≠ ∅ implies g ∈ A;
- B/A → X is an open embedding.

Let σ = (σ_1, …, σ_m) be generators of the A-invariant polynomials. They induce an embedding σ̄ of B/A into ℂ^m. Since h is holomorphic, σ̄∘h is holomorphic near y_0.

**Fibre product.** Take a disc Q_0 ∋ y_0 whose closure satisfies L(closure Q_0) ⊂ B. Put Z := {(y,b) ∈ Q_0 × B : σ(b) = σ̄(h(y))}.
- Z is analytic, and its fibre over y is the finite orbit A·L(y).
- Z → Q_0 is proper, since fibres lie in the compact set A·L(closure Q_0).
- So Z is finite over Q_0. Let Σ ⊂ Q_0 be the image of Sing Z, of the 0-dimensional part of Z, and of the critical points of the projection on Reg Z. Σ is discrete: a curve of critical points would lie in a fibre, and fibres are finite.
- Over Q_0 ∖ Σ, Z → Q_0 is a finite covering map whose local sheets are graphs of holomorphic maps.

**Conclusion.** The graph of L|_{Q_0∖Σ} is a continuous section of this covering. Over every evenly covered disc a continuous section lies in a single sheet, so L is holomorphic on Q_0 ∖ Σ. L is continuous and bounded in the coordinates of the ball B, so by Riemann's extension theorem it is holomorphic on Q_0. ∎

*Remark.* Lemma CL is why no orbifold bookkeeping (cone orders, minimal orbifolds) is needed below. If a continuous lift exists, it is automatically holomorphic, and cone points that would obstruct it cannot be present.

## 3. Lemma J0: the joint vertex map of every piece at t = 0 lifts over the Veech orbifold (no use of (R2^orb))

**Prior results used** (round8_q10, quoted in the brief; not re-proved here):
- **Theorem TV.** Let E be a piece of Â_0 (any G). There are:
  - a vertex j;
  - a closed Teichmüller curve C ⊂ M_j, with normalisation κ : C^ν = H/Γ′ → M̄_j (Γ′ a lattice);
  - a subgroup Λ_E ⊂ Γ′ of finite index, with E^ν ≅ H/Λ_E such that p_E := (π_j∘ν lifted to normalisations) : E^ν → C^ν is the map H/Λ_E → H/Γ′ induced by the inclusion.

  The Teichmüller disc D : H → T_j satisfies D∘γ = (affine class of γ)∘D for γ ∈ Γ′, and κ∘q_{Γ′} = u := (projection of D to M_j).
- **Corollary Φ̂, together with the proof of TV.** For a point P̂ ∈ E chosen off Sing Â and off the other components of Â, there is a continuous map Φ = (φ̂_w)_w : H → T_G with:
  - each φ̂_w 1-Lipschitz;
  - φ̂ := p∘Φ mapping H into Â;
  - φ̂(i) = P̂;
  - φ̂_j = D, so π_j∘φ̂ = u.

**Lemma J0.** Let E be a piece at t = 0, with the notation of TV. Put Λ := Λ_E and let q : H → H/Λ = E^ν be the quotient map. There are γ_0 ∈ Γ′ and a **holomorphic** map F : H → T_G such that:
- (i) p∘F = ν∘q, i.e. F lifts the whole vertex map of E;
- (ii) pr_j∘F = D∘γ_0^{-1}, an isometric holomorphic embedding of H onto the Teichmüller disc 𝔇 := D(H);
- (iii) for every λ ∈ Λ the set R(λ) := {g ∈ Mod_Π : F∘λ = g∘F} is a coset of the finite group S := {s ∈ Mod_Π : s∘F ≡ F}. Moreover R(λμ) = R(λ)R(μ), and every element of R(λ) normalises S.

*Proof.*

**Step 1 (φ̂(H) ⊂ E).** Let Z be the union of the following sets:
- the points of E lying on other components of Â;
- the isolated points of Â;
- the components E′ ≠ E of Â on which π_j is constant.

Z is closed, and it is a locally finite union of points and curves. For a compact disc K ⊂ H, φ̂(K) is compact. It meets only finitely many points and components making up Z, and π_j takes finitely many values on φ̂(K) ∩ Z. Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite set) ∩ K, which is finite because u is non-constant holomorphic. So φ̂^{-1}(Z) is discrete, and H° := H ∖ φ̂^{-1}(Z) is connected.

Now Â ∖ Z is the disjoint union of E ∖ Z and the sets E′ ∖ Z (E′ ≠ E, π_j non-constant on E′). Each of these is relatively closed, and the family is locally finite, so E ∖ Z is clopen in Â ∖ Z. Its preimage is clopen in H° and contains i, because P̂ ∉ Z. Hence it is all of H°, and since E is closed, φ̂(H) ⊂ E.

**Step 2 (φ̂ is holomorphic).** Let Σ_E ⊂ E be the discrete set consisting of:
- Sing E;
- the points where π_j|_E : E → C is not a local biholomorphism onto a smooth point of C.

π_j|_E is a non-constant finite map of curves, so Σ_E is discrete. As in Step 1, φ̂^{-1}(Σ_E) is discrete. Off it, φ̂ = (π_j|_E)^{-1}_{loc}∘u is holomorphic. Since φ̂ is continuous, Riemann's extension theorem (in a local embedding of ∏M_w) makes it holomorphic on H.

**Step 3 (lift to E^ν, and p_E∘φ^ν = q_{Γ′}).** φ̂ lifts to a holomorphic φ^ν : H → E^ν, by the universal property of normalisation. Then κ∘p_E∘φ^ν = π_j∘φ̂ = u = κ∘q_{Γ′}. Since κ is generically injective, p_E∘φ^ν = q_{Γ′}.

**Step 4 (φ^ν = q∘γ_0).** Let Br ⊂ C^ν be the finite set of orbifold points of H/Γ′.
- Over C^ν ∖ Br, both H → H/Γ′ and the finite map p_E : H/Λ → H/Γ′ are unbranched coverings.
- Put H^♮ := q_{Γ′}^{-1}(C^ν ∖ Br), a connected set (H minus a discrete set), and fix x_0 ∈ H^♮.
- The fibre p_E^{-1}(q_{Γ′} x_0) is {q(γ x_0) : γ ∈ Γ′}. So φ^ν(x_0) = q(γ_0 x_0) for some γ_0 ∈ Γ′.
- φ^ν and q∘γ_0 are both lifts of q_{Γ′}|_{H^♮} through a covering map, and they agree at x_0. So they agree on H^♮, hence on H.

**Step 5 (F).** Put F := Φ∘γ_0^{-1}.
- F is continuous, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- ν∘q is holomorphic, so F is holomorphic by Lemma CL (with Γ = Mod_Π). This gives (i).
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is an isometry of H.
- (iii): for λ ∈ Λ, F∘λ and F are holomorphic lifts of the same map ν∘q∘λ = ν∘q, so Lemma CS applies.
- Product rule: if a ∈ R(λ) and b ∈ R(μ), then F(λμx) = aF(μx) = abF(x).
- Normality: if g ∈ R(λ) and s ∈ S, then g^{-1}sgF = g^{-1}s(F∘λ) = g^{-1}(F∘λ) = F, so g^{-1}sg ∈ S. ∎

**Consequences.**
- **(H_0) for the joint map.** At t = 0 the whole vertex map of every piece, not only its Teichmüller coordinate, has an equivariant holomorphic lift over the single orbifold structure Λ_E for which the j-coordinate is an isometry. This is hypothesis (H_0) of Lemma R*, together with (O_u) at t = 0 in L2 (round7_q9).
- In particular the joint minimal orbifold structure of ν_0 is dominated by Λ_E: every cone point of the joint map is a cone point of Λ_E, with order dividing.
- **Example Z (round8_q9) cannot occur at t = 0.** There the u-coordinate z³ + z needs cone points (orders 3 and 2 at roots of J_0 = 0, 1728, and order 6 at z = 0) that Λ_E does not have. So Lemma J0 excludes it as a boundary piece of a totally geodesic V_0. This answers the t = 0 half of question Q1 of round9_q9 for Example Z: E_0 is not realisable. For Example Z′, Lemma J0 excludes E_0 unless J_0∘q lifts holomorphically to T_{1,1} = H. I have not decided which J_0 satisfy this. So the remaining objection to Z/Z′-type deformations concerns t ≠ 0: Lemma J0 says nothing about E_t for t ≠ 0.


### Referee check of Lemmas CS, CL, J0 (verbatim §§1–3)
## round13_q9 (verbatim): independent verification of round12_q9
# round13_q9 — verification of round12_q9 (Lemma CS, CL, J0, 1.1, Prop. T, Lemma R*′, Theorem RO, Prop. C)

**Plan/status line (written first).** I read the whole brief, including round12_q9 verbatim. I check each lemma inference by inference, in the order CS, CL, J0, 1.1 (with O_t, h̃_t, θ_t), Prop. T, R*′, RO, Prop. C. Then I give the verdicts.

**Status at the end.**
- No fatal gap found.
- Three minor repairs are needed, all supplied below:
  - (R1′) finite type of Ê_t: the argument given is incomplete, and is repaired by algebraicity;
  - (R2′) the definition of the torsion-free level subgroups Mod_w[N] in genus 0 and type (1,1);
  - (R3′) the labelled lift φ̂(i) = P̂ in non-product strata: repaired by Aut(G)-relabelling.
- Proposition C's non-product clause is only a sketch.
- Every external input is cited from memory, by me as in round12_q9: Bers, Thurston, Royden, Selberg, Imayoshi–Shiga, orbifold uniformisation, Cartan.
- Theorem RO also depends on prior results that I did not re-check because they are not spliced: TV items 1–3 (the proofs of round8_q10 §4, Steps 2′–5) and Lemma PA. It also depends on the reading (R2^orb) in its global form (a)–(d).

Notation is that of round12_q9. "✓" means I checked the inference and it is valid.

---

## 1. Lemma CS — correct

- Q = ∪_{g∈Γ} Z_g with Z_g = {F′ = gF}. Each Z_g is the coincidence set of two holomorphic maps into a manifold, so it is closed analytic. Γ is countable and Q is a Baire space, so some Z_g has interior. Q is connected, so the identity theorem gives F′ ≡ gF. ✓
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. So the solution set is the coset gS_F. ✓
- S_F ⊂ Stab_Γ(F(y)), which is finite because the action is properly discontinuous. ✓

## 2. Lemma CL — correct

- **Chart.** Stab_Γ(x̂) = A is finite. Cartan's linearisation gives an A-invariant ball B with linear A-action. By proper discontinuity, B can be shrunk so that gB ∩ B ≠ ∅ ⇒ g ∈ A. By the definition of Cartan's quotient structure, B/A → X is an open embedding. ✓
- **Holomorphy of σ̄∘h.** The A-invariant polynomials σ_k are A-invariant holomorphic functions on B. By definition of the quotient structure sheaf, they are holomorphic functions on B/A. So σ̄∘h is holomorphic on Q_0, since h(Q_0) = p(L(Q_0)) ⊂ B/A. ✓ (The embedding property of σ̄ is not needed. Only two facts are used: σ separates A-orbits, which holds for finite groups, and σ_k descends.)
- **Z.** Z is analytic, and its fibre over y is {b ∈ B : σ(b) = σ(L(y))} = A·L(y), because σ separates orbits. ✓
- **Properness.** For compact K ⊂ Q_0, Z ∩ (K × B) is a closed subset of K × A·L(K), which is compact. ✓
- **Σ is discrete.** Sing Z and the 0-dimensional part are closed and discrete. On Reg Z the critical points of the projection are discrete, since a 1-dimensional component of critical points would be a curve on which the projection is constant, i.e. a curve inside a finite fibre. Images of closed discrete sets under a proper finite map are closed and discrete. ✓
- **Covering.** Over Q_0∖Σ, Z is a 1-manifold mapping by a proper local biholomorphism, hence a finite covering whose sheets are graphs of holomorphic maps. ✓
- **Conclusion.** y ↦ (y, L(y)) is a continuous section. Over a connected evenly covered disc it stays in one sheet, so L is holomorphic off Σ. L is bounded in the ball coordinates and continuous, so Riemann's extension theorem makes it holomorphic on Q_0. ✓

## 3. Lemma J0 — correct, given TV items 1–3 and Corollary Φ̂ as stated (one minor repair in non-product strata)

### 3.1 What TV and Φ̂ actually state, against what J0 quotes

**(a) Is there a continuous Φ : H → T_G with 1-Lipschitz coordinates?**
- Yes. Corollary Φ̂ gives, along a subsequence, maps φ̂_w : H → T(Σ_w), each 1-Lipschitz from d_H (curvature −4) to d_T.
- Put Φ := (φ̂_w)_w. It is continuous, and p∘Φ = ([φ̂_w])_w = φ̂.
- Φ̂ also states φ̂(H) ⊂ Â, using that X^g_n ∈ V_0 by total geodesy. ✓

**(b) pr_j∘Φ = D?**
- Φ̂ states: "if moreover v carries positive area η_v, then … φ̂_v = D (as maps to T(Σ_v))".
- The proof of TV supplies positive area at the vertex j, via Lemma PA (cited from memory in round8_q10) and Lemma TR. TV's D is the Teichmüller disc of (Y_j, η_j) with Y_j = P̃_j, which is the same D.
- So pr_j∘Φ = D holds, **conditional on Lemma PA**. ✓

**(c) φ̂(i) = P̂ with P̂ generic?**
- This is **not** in the statement of Φ̂. It is asserted in the proof of TV: "φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂)".
- What Φ̂ itself gives is φ̂(i) = λ(P̃), the labelled lift of the limit of (X_n, f_n), since g = 1 gives X^1_n = X_n.
- **Product type** (ξ_G = id): λ(P̃) = P = P̂ automatically. ✓
- **Non-product type:** λ(P̃) is one of the finitely many points of ξ_G^{-1}(P). It equals P̂ only through the labelled plumbing chart (Pl), which round8_q10 says it has "only described".
- **Repair (R3′).** In general λ(P̃) = σP̂ for some σ in the finite group Mod_G/Mod_Π acting on ∏M_w. That group acts because Mod_Π ⊲ Mod_G.
  - σP̂ is again generic: it lies off Sing Â and off the other components, since σ permutes the components of the σ-invariant set Â.
  - So Steps 1–5 below run verbatim for the piece σE.
  - Then a lift σ̃ ∈ Mod_G of σ^{-1} gives σ̃∘F, which satisfies (i)–(iii) for E. It uses the vertex σ^{-1}(j), the same Λ (E^ν ≅ (σE)^ν via σ), S replaced by σ̃Sσ̃^{-1}, and R(λ) by σ̃R(λ)σ̃^{-1}. This uses that σ̃ normalises Mod_Π.
  - So J0 holds for every piece, with the Teichmüller vertex and disc transported by σ. Nothing downstream uses the specific j.

**(d) E^ν = H/Λ_E with Λ_E ⊂ Γ′?**
- TV item 2 states it: "E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p". Item 3 states that the lift of π_j∘ν to the universal cover is D.
- This is what J0 quotes: p_E∘q = q_{Γ′} and κ∘q_{Γ′} = u.
- The proof of item 2 (round8_q10 §4, Steps 2′–5) is **not spliced**, so I could not check it. It is a dependency.
- **Remark (partial independent check).** Given Φ̂ alone, Steps 2–3 below produce a holomorphic φ^ν : H → E^ν with p_E∘φ^ν = q_{Γ′}. Suppose one also knows that p_E : E^ν → C^ν is proper (TV items 2 and 4: ends go to cusps). Then:
  - At a point x ∈ H that is not an elliptic fixed point, q_{Γ′} has local degree 1. So p_E has local degree 1 at φ^ν(x), and p_E is unbranched over C^ν∖Br.
  - A proper unbranched finite map is a covering. So φ^ν restricted to H^♮ is a covering of p_E^{-1}(C^ν∖Br), with deck group a finite-index Λ_E ⊂ Γ′.
  - Hence E^ν ≅ H/Λ_E, after filling in the cone points.
  - So TV item 2 reduces to **properness of p_E** (TV item 4). That is the only part of TV's §4 that J0 really needs beyond Φ̂ and Lemma PA.

### 3.2 Steps of J0

**Step 1 (φ̂(H) ⊂ E).** ✓, including non-product strata. The argument is purely topological in ∏M_w.
- Â is closed in ∏M_w and of dimension ≤ 1: it lies in the boundary, and closure(V_0) is an irreducible surface not contained in it.
- Z is a locally finite union of points and curves.
- For a compact disc K ⊂ H, φ̂(K) meets only finitely many of the following: points of E ∩ E′ (closed discrete), isolated points, and components on which π_j is constant. So π_j takes finitely many values on φ̂(K) ∩ Z.
- Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite) ∩ K, which is finite because u = κ∘q_{Γ′} is non-constant. Here π_j∘φ̂ = u needs (b).
- **Clopen argument.** Â∖Z = (E∖Z) ⊔ ⋃_{E′}(E′∖Z), where the union runs over E′ ≠ E with π_j non-constant on E′. E∖Z misses every E′, because points of E on other components lie in Z. Both parts are relatively closed, the second by local finiteness.
- i ∈ φ̂^{-1}(E∖Z), because P̂ is non-isolated, off the other components, and therefore off Z.
- H° is connected, so φ̂(H°) ⊂ E. E is closed and H° is dense, so φ̂(H) ⊂ E.
- **Non-product strata:** the only issue is (c) above, which is repaired by (R3′).

**Step 2 (φ̂ holomorphic).** ✓
- Σ_E is discrete in E. It consists of Sing E, the critical points of π_j on Reg E, and the preimage of the discrete set Sing C. A non-constant map from an irreducible curve has discrete fibres. Finiteness of π_j|_E is not needed.
- φ̂^{-1}(Σ_E) is discrete. Σ_E is closed and discrete in the closed set E, so it meets φ̂(K) in a finite set; then argue as in Step 1.
- At x with φ̂(x) = e ∉ Σ_E: by continuity φ̂ maps a neighbourhood of x into a neighbourhood U_e on which π_j is a biholomorphism onto a neighbourhood of a smooth point of C. There φ̂ = (π_j|_{U_e})^{-1}∘u, which is holomorphic.
- Riemann extension in a local embedding of ∏M_w then gives holomorphy everywhere.

**Step 3.** ✓
- The lift φ^ν exists by the universal property of normalisation: H is smooth and φ̂^{-1}(Sing E) is discrete.
- κ∘p_E∘φ^ν = u = κ∘q_{Γ′}. Since κ is injective off a finite set N and q_{Γ′} is non-constant, the two maps agree off the discrete set q_{Γ′}^{-1}(κ^{-1}κ(N)), hence everywhere.

**Step 4.** ✓
- Over C^ν∖Br, H/Λ → H/Γ′ is the covering H^♮/Λ → H^♮/Γ′, since both groups act freely on H^♮. The fibre over [x_0] is {Λγx_0 : γ ∈ Γ′}.
- φ^ν and q∘γ_0 are lifts of q_{Γ′}|_{H^♮} that agree at x_0. H^♮ is connected, so they agree on H^♮, and by density on H.

**Step 5.** ✓
- F := Φ∘γ_0^{-1}, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- Lemma CL applies with T = T_G and Γ = Mod_Π. The action is properly discontinuous, the group is countable, and T_G/Mod_Π = ∏M_w as analytic spaces. So F is holomorphic.
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is a biholomorphic isometry of H.
- (iii) R(λ) is a coset of S: by Lemma CS, since p∘F∘λ = ν∘q∘λ = ν∘q.
- (iii) Normality: if g ∈ R(λ) and s ∈ S, then s g F = s(F∘λ) = (sF)∘λ = F∘λ = gF, so g^{-1}sg ∈ S.
- (iii) Product rule: by normality gS·hS = ghS, and ghS ⊂ R(λμ) is a coset of S, hence equal to R(λμ). ✓

**Consequences.**
- "Example Z cannot occur at t = 0" is correct. At a simple zero z_* of J_0 that is not a cone point of Λ_E, a holomorphic lift L to T_{1,1} = H would satisfy J_0 = (unit)·(L − L_*)^3 near z_*, contradicting the simple zero.
- At z = 0, which is a cone point of order 2, J_0∘q ~ w² is not a cube.
- This is a remark only and is not used downstream.

**Verdict on J0: correct, with the repair (R3′) in non-product strata.** It is conditional on TV items 1–3 (equivalently on properness of p_E, by the Remark in 3.1(d)), on Corollary Φ̂, and on Lemma PA/TR for positive area at j.


### Theorem X* and Proposition K_w (verbatim)
# round9_q4 — answer

**Status.**
- Part 1, the claim (CR*): **proved for every normal singularity**, given Steps 1–4 of Theorem X (R8-1), which I re-checked. Q-factoriality is not needed, and neither is the monomial criterion. The new ingredient replaces Step 5 (Hurwitz applied to a Q-Cartier equation) by a homological intersection argument on a resolution of Ŝ, using Mumford's negative definiteness.
- Part 2, the same-sheet lemma: **the literal reading (TD_J) does not follow from Proposition K as written.** The chain read off the Hausdorff limit K_0 can record a transition at a point J that the approximating rays never pass near. I give a repaired version of Proposition K, the "walk chain", built from a single approximating ray. Every transition of the walk chain is realised by a sub-path that stays inside a small Milnor ball around the transition point. For the walk chain the same-sheet lemma is **proved**.
- Combination: in the walk chain, no junction or endpoint is a crossing, except in the case where the incoming and outgoing branches are the same coarse branch of the same piece. That residual case is the twin case (type (T) of R8-6), which is outside this task.

Plan, written first:
- §1: prove (CR*) in a strengthened form (Theorem X*).
- §2: same-sheet lemma: what fails, and the repair.
- §3: the combination.
- §4: summary of what is proved and what is open.

---

## 1. Part 1: (CR*) for arbitrary normal sheets

### 1.1 Statement
Setting and notation are exactly as in Theorem X (R8-1 §3.1):
- V_0 ⊂ M_g is a closed totally geodesic surface. Smoothness is not needed for this part.
- E is a piece of B_0 in a product-type stratum Δ_G.
- Q_0 ∈ E, so Q_0 lies in Δ_G.
- β is a local branch of E at Q_0, and β̃ is a lift of β to Def(Q_0).
- S is an irreducible component of the germ at 0 of the preimage of closure(V_0) in Def(Q_0), with S ⊃ β̃.
- ν: Ŝ → S is the normalisation, and ŝ_0 = ν^{-1}(0).
- B̂ = ν^{-1}(S ∩ {∏ s_e = 0}).
- Ê_1, …, Ê_r are the components of the germ (B̂, ŝ_0) that map onto β̃, and C_1, …, C_m are the others.

**Theorem X\*.** m = 0. That is, every irreducible component at ŝ_0 of the boundary curve of Ŝ maps onto the single lifted branch β̃.

In particular (CR*) holds. Any sheet S of closure(V_0) at Q_0 that contains a branch of E contains no other boundary curve through Q_0. This excludes boundary curves of other pieces, and also other branches of E itself, including other lifts αβ̃ ≠ β̃ of β.

### 1.2 What is used from Theorem X (re-checked)
Steps 1–4 of R8-1 §3.2 produce the following, and I re-checked each item:
- a connected open set Ω ⊂ 𝔻;
- holomorphic maps D̂_n: Ω → Ŝ with D̂_n(Ω) ∩ B̂ = ∅;
- a holomorphic L̂: Ω → Ŝ with D̂_n → L̂ locally uniformly;
- a point w* ∈ Ω with L̂(w*) = ŝ_0, and L̂(Ω) ⊂ Ê_1.

Here is the check, item by item.
- **L̂(Ω) ⊂ Ê_1.** L̂(Ω) ⊂ B̂, since L takes values in the boundary. The sets L̂^{-1}(Ê_l) and L̂^{-1}(C_i) are analytic and cover Ω, and L̂^{-1}(Ê_1) contains a neighbourhood of 0. By the identity principle it is all of Ω.
- **L̂ is non-constant.** Its image under ν is a lift of L, and L is non-constant by (Fl).
- **L̂^{-1}(ŝ_0) is discrete.** It is analytic and does not contain 0.
- **Surjectivity of L onto E^ν (Step 3).** This uses:
  - the closedness of Teichmüller discs and the local finiteness of their translates, (Prop);
  - finiteness of the set Λ of lifts;
  - properness of L̄.
  I re-checked each of these.
- **Lifting to Def(Q_0) and to Ŝ (Steps 2 and 5).**
  - The Teichmüller disc lifts to T_g. A component of the preimage of the chart interior maps holomorphically to Def(Q_0)°. This is cited, as in R8-1.
  - The lifted disc lies in S, by an analytic-covering argument plus the choice of X̃_n off S ∩ S_i.
  - It lifts to Ŝ by the universal property of normalisation, since X̃_n is off the non-normal locus.
- **Ŝ is smooth off ŝ_0 near ŝ_0.** A normal surface has isolated singular points, and ŝ_0 ∈ B̂. Hence D̂_n maps into the smooth part of Ŝ.

Only Step 5 of R8-1 (the Hurwitz step with a Q-Cartier equation G) is replaced.

### 1.3 Cited standard facts (from memory)
- **(Res)** Let (Ŝ, ŝ_0) be a normal surface germ. There is a resolution π: S′ → W, where W = Ŝ ∩ (closed Milnor ball) is a small closed neighbourhood of ŝ_0, such that:
  - π is an isomorphism over W ∖ {ŝ_0};
  - Exc := π^{-1}(ŝ_0) is a compact connected curve with irreducible components F_1, …, F_p, p ≥ 1. Connectedness follows from Zariski's main theorem. If ŝ_0 is a smooth point, take π to be the blow-up of ŝ_0, so that p = 1 and F_1² = −1.
  - U′ := π^{-1}(int W) deformation retracts onto Exc. Hence H_2(U′; ℤ) is free with basis [F_1], …, [F_p].
- **(Neg)** (Du Val, Mumford, Grauert.) The intersection matrix N = (F_j · F_k) is negative definite.
- **(Int)** Let A ⊂ U′ be a closed analytic curve. The intersection number with A, z ↦ z · A, is a well-defined homomorphism on H_2(U′; ℤ) (Poincaré–Lefschetz duality: A defines a Borel–Moore class). Suppose a 2-cycle z consists of pieces that are disjoint from A, together with holomorphic discs meeting A in isolated interior points. Then z · A is the sum of the local intersection multiplicities at those points, and each multiplicity is > 0.
- **(Pos)** This is elementary, and I prove it here. Let N be a negative definite symmetric real matrix whose off-diagonal entries are ≥ 0 and whose graph ({j,k} is an edge iff N_{jk} > 0) is connected. Let λ ≥ 0 with λ ≠ 0. Then x := −N^{-1}λ has all entries strictly positive.
  *Proof.*
  - Write x = x⁺ − x⁻, where x⁺ and x⁻ are non-negative with disjoint supports.
  - Then (x⁻)ᵀ N x = (x⁻)ᵀ N x⁺ − (x⁻)ᵀ N x⁻.
  - The first term is ≥ 0, because the supports are disjoint and the off-diagonal entries are ≥ 0. The second term, −(x⁻)ᵀ N x⁻, is ≥ 0, with equality only if x⁻ = 0. So (x⁻)ᵀ N x ≥ 0.
  - But (x⁻)ᵀ N x = −λ · x⁻ ≤ 0. Hence x⁻ = 0, i.e. x ≥ 0.
  - Suppose x_j = 0 for some j. Then Σ_{k≠j} N_{jk} x_k = (Nx)_j = −λ_j ≤ 0. Every term on the left is ≥ 0, so x_k = 0 for every neighbour k of j.
  - By connectedness x = 0. Then λ = −Nx = 0, a contradiction. ∎
  For the matrix N of (Neg), the off-diagonal entries F_j · F_k (j ≠ k) are ≥ 0, and the graph is connected because Exc is connected.

### 1.4 Proof of Theorem X*
Suppose m ≥ 1, and fix C := C_1.

**Choices.**
- Choose W as in (Res) so small that, inside W, C ∩ Ê_1 = {ŝ_0}. Distinct irreducible curve germs meet only at the base point.
- Choose ε > 0 so small that the closed disc Ω̄_ε := {|w − w*| ≤ ε} lies in Ω, L̂(Ω̄_ε) ⊂ int W, and L̂^{-1}(ŝ_0) ∩ Ω̄_ε = {w*}.
- For n large, D̂_n(Ω̄_ε) ⊂ int W, by uniform convergence on Ω̄_ε.

**Lifts.**
- D′_n := π^{-1} ∘ D̂_n is holomorphic, since π is an isomorphism over W ∖ {ŝ_0} ⊃ W ∖ B̂.
- Its image avoids π^{-1}(B̂). That set contains Exc, the strict transform C′ of C, and the strict transform Ê′_1.
- L̂|_{Ω_ε} takes values in the curve Ê_1, and is not contained in its singular locus. So it factors through the normalisation of Ê_1, and that normalisation maps holomorphically onto Ê′_1 ⊂ S′. This defines a holomorphic L′: Ω_ε → Ê′_1 ⊂ S′ with π ∘ L′ = L̂.
- L′(w) ∈ Exc only for w = w*.
- C′ ∩ Ê′_1 ⊂ Exc, because C ∩ Ê_1 = {ŝ_0} in W. Hence L′(Ω̄_ε) ∩ C′ = ∅.

**Boundary circles.**
- K := L̂(∂Ω_ε) is a compact subset of Ê_1 ∖ {ŝ_0}. Over a neighbourhood of K, π^{-1} is a biholomorphism. Hence D′_n → L′ uniformly on ∂Ω_ε.
- K′ := L′(∂Ω_ε) is compact and disjoint from Exc ∪ C′. Fix a Riemannian metric and a tubular neighbourhood N_K of K′ in U′ that is disjoint from Exc ∪ C′.
- For n large, the short-geodesic homotopy between D′_n|_{∂Ω_ε} and L′|_{∂Ω_ε} sweeps a singular annulus A_n ⊂ N_K with ∂A_n = L′(∂Ω_ε) − D′_n(∂Ω_ε).

**The cycle.** Put
 Z_n := D′_n(Ω̄_ε) − L′(Ω̄_ε) + A_n.
This is a singular 2-cycle in U′. By (Res), [Z_n] = Σ_j k_j [F_j] with k_j ∈ ℤ.

**Intersection with F_k.**
- The piece D′_n(Ω̄_ε) is disjoint from F_k, and so is A_n.
- L′(Ω̄_ε) meets Exc only at L′(w*), in isolated points. Put λ_k := (local intersection number of the disc L′ with F_k) ≥ 0. Then Σ_k λ_k > 0, because L′(w*) ∈ Exc and L′ ⊄ Exc.
- By (Int), Σ_j k_j (F_j · F_k) = Z_n · F_k = −λ_k for all k. That is, N k = −λ.
- N is invertible by (Neg). So k = −N^{-1}λ, and by (Pos) all k_j > 0.

**Intersection with C′.** C′ is a closed analytic curve in U′.
- Each piece of Z_n is disjoint from C′: D′_n avoids π^{-1}(B̂), L′ avoids C′, and A_n ⊂ N_K. Hence Z_n · C′ = 0.
- On the other hand, Z_n · C′ = Σ_j k_j (F_j · C′).
  - Each F_j · C′ ≥ 0, because F_j ≠ C′ are distinct curves.
  - Some F_j · C′ > 0. C passes through ŝ_0, so points of C ∖ {ŝ_0} accumulate at ŝ_0. Their preimages accumulate on the compact set Exc, and C′ is closed, so C′ ∩ Exc ≠ ∅.
  - With all k_j > 0, this gives Z_n · C′ > 0.

This contradiction proves m = 0. ∎

**Remarks.**
1. In the language of Mumford's ℚ-valued intersection theory, the proof says the following.
   - The local intersection C · L̂ at ŝ_0 is strictly positive, as always for two distinct curves through a normal surface point.
   - Mumford intersection numbers are continuous under the convergence D̂_n → L̂.
   - Mumford's pull-back π^*C = C′ + Σ a_j F_j is numerically trivial on Exc. So the homology class of the bubble Σ k_j F_j that may appear in the limit of the D′_n contributes nothing.

   The Q-Cartier equation G of Theorem X is only needed to make this continuity hold for an honest function. Q-factoriality is therefore irrelevant.
2. Only the following were used: the discs D̂_n avoid the whole boundary B̂, and their limit L̂ is a disc inside one boundary curve Ê_1 passing through ŝ_0. The second fact is the place where total geodesy enters (Lemma PA, (Fl), (Prop): the limit disc sweeps all of E).
3. Strengthening. Two different branches of the same piece E at Q_0 (or two different lifts β̃, αβ̃ of one branch) never lie in a common sheet S of the chart. Indeed, apply Theorem X* with β; the curve over the other branch would be a C_i.
4. As in R8-1 Remark 2, product type of the stratum of E is used: the global coordinate f_j on E appears in Step 3. Non-product strata are not checked.
5. From chart sheets to coarse sheets. Suppose a sheet 𝒮 of closure(V_0) at Q_0 in M̄_g contains a branch b of E and another boundary branch β′. Take a chart component S over 𝒮. The preimage of 𝒮 is ⋃_α αS, so S contains some lift of b and some lift of β′. Theorem X* then gives a contradiction, unless β′ = b as coarse branches.

---

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

## 3. Combination with Theorem X*
Assume the pieces of the chain are of product type (PT_chain), as MS8 already assumes. Use the walk chain.

**(a) No junction lies in the stratum of an adjacent piece, except along a single coarse branch.**
- Suppose J_m ∈ stratum(D^{m+1}), i.e. J_m is a point of the piece D^{m+1}.
- The common sheet at J_m contains a branch of D^{m+1} and the incoming branch β^m.
- By Theorem X* and Remark 5, β^m and the outgoing branch are the same coarse branch of the same piece, so D^m = D^{m+1}.
- The same holds with the roles of m and m+1 exchanged.

**(b) The junction crossing of R8-8 Prop. 3(c).**
- Case (c) asserts J_m ∈ stratum(D^{m+1}), with c_{m+1} = {x_m} constant on D^{m+1} along β^{m+1}_−. Strata are transported by H_t, so this is a statement at t = 0.
- By (a), D^m = D^{m+1} and the two branches coincide coarsely. Then the lifts satisfy β̃^{m+1}_− = aβ̃^m_+ for some a ∈ Aut(J_m).
- This is the same-branch twin configuration (type (T) of R8-6), not a crossing.
- So genuine junction crossings (a different piece, or a different coarse branch) do not occur.

**(c) Endpoint.**
- Suppose the endpoint is iMOV, i.e. Q ∈ stratum(E_b).
- The common sheet at Q contains b and β. By Theorem X*, β and b are the same coarse branch, so E_b = D.
- But x is constant along β̃ (STAY) and non-constant along b̃. So b̃ = aβ̃ with ax ≠ x: again the twin type (T).
- Hence the endpoint is MERGE, puncture-MOV, or a same-branch twin.

**Conclusion of the derivation.** Under MS8's hypotheses plus (PT_chain), the walk chain has no interior-MOV endpoint and no junction crossing, apart from configurations of same-branch twin type. The planner's derivation is therefore correct for the walk chain, after this caveat about twins is added. It was not correct for the K_0-chain without the repair of §2.3.

---

## 4. Summary
**Proved:**
- **Theorem X\*** ((CR*) in strengthened form) for every normal sheet. It assumes Steps 1–4 of R8-1 Theorem X (re-checked) and a product-type stratum for E. Its corollary: two distinct coarse boundary branches through an interior point of a piece never share a sheet.
- **Lemma S′** and **Proposition K_w**: the walk chain, whose transitions are local, and which therefore satisfies the same-sheet lemma. This is modulo the cited inputs of PR-H.
- The combination of §3: crossings (Cr1) and (Cr2) are eliminated for the walk chain.

**Found false or unsupported:**
- The reading (TD_J) for the chain read off the Hausdorff limit K_0. The track need not stay near J during the transition (§2.2). The repair is to replace that chain by the walk chain.

**Open / not covered:**
- (i) The same-branch twin configurations (type (T)) at junctions and at the endpoint. These were excluded from this task.
- (ii) Non-product strata (Theorem X Step 3 uses the global coordinate f_j).
- (iii) The cited inputs: (Fl), the T_g ↔ Def chart description, Proposition K's Lemmas PA and NH, and (Res), (Neg), (Int), all cited from memory.
- (iv) Entry 82 (Rig), as before.


### Referee check and repairs of Proposition K_w, Lemma S̃′ (verbatim)
**Plan/status.** This is a chain check of Proposition K_w and Lemma S′ (round9_q4 §2). I check every step against points 1–7 of the brief.

**Verdict in brief: REPAIRED.** Proposition K_w holds in the form the chain uses, but only after four repairs:
- (R-a) the choice of η and ρ_* needs three extra small conditions;
- (R-b) Step 3: the chart lift must be the *canonical* lift through augmented Teichmüller space, not an arbitrary Bredon lift. With an arbitrary lift, the label x can change at orbifold points;
- (R-c) Step 5, upstairs: an arbitrary lifted path need *not* lie in a single irreducible component of q^{-1}(closure V_0). The canonical lift does lie in one, because it lies on the image of a Teichmüller disc. This also needs r small enough that distinct lifted branches meet only at the chart centre;
- (R-d) the chain's combinatorics are not uniform in n. The number of excursions can grow with n. A single chain with all the properties is obtained by keeping only "recurrent" transition types.

The inputs are taken as given, as in the text: Lemma PA, Lemma NH, Kerckhoff, Maskit, the plumbing/Kuranishi charts and the collar lemma. Below, "cited" means cited from memory.

---

## 0. Conventions made explicit

- **Pieces.** B_0 = closure(V_0) ∖ V_0 is the intersection of the irreducible 2-dimensional analytic set closure(V_0) with ∂M̄_g. Locally, ∂M̄_g is the zero set of the Aut-invariant function N = ∏_{g∈Aut(J)} g^*(∏_e s_e), which descends to the coarse chart. Hence B_0 has pure dimension 1. A *piece* is a 1-dimensional irreducible component of B_0 ∩ Δ_G, for some stratum Δ_G.
  - closure(D) ∖ D consists of punctures of D, which lie in Σ.
  - So K_D ⊂ D, the K_D are compact, and they are pairwise disjoint: common points of two closures are junctions.
- **Vertices of a piece.** For the strata Δ_G of the pieces (which may be quotient strata), "vertex of D" means an orbit of vertices under the monodromy of D. "Constant vertex" and "value class" are monodromy-invariant, so nothing below changes.
- **The metric d.** Σ is finite. I take a metric d on M̄_g which, near each J ∈ Σ, is the quotient of an Aut(J)-invariant Euclidean metric on Def(J). Then small metric balls B(J,ρ) are images of round Aut-invariant balls B̃(J,ρ) ⊂ Def(J). For small ρ these are Milnor balls for the germs (X,J) downstairs and (q^{-1}X, 0) upstairs. (Milnor's conic structure theorem, cited.)

## 1. Step 0 (point 1): correct

Let s_n ≤ T_n. Since (X_n, q_n) is a generating pair and V_0 is totally geodesic, γ_n(s_n) ∈ V_0, so every limit point lies in closure(V_0).
- If s_n stays bounded: Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n}(Γ-curves) → 0, since X_n → P ∈ Δ_Γ.
- If s_n → ∞: Lemma NH(1) gives Ext(c_n) ≤ e^{-2s_n}/m → 0.
- In both cases some curve has Ext → 0. By Maskit's comparison its hyperbolic length → 0, so the limit lies in ∂M̄_g.

Hence every limit point lies in closure(V_0) ∩ ∂M̄_g = B_0. Here V_0 is closed in M_g (an algebraic subvariety), so closure(V_0) ∩ M_g = V_0.

Uniformity follows by contradiction. If ρ_n ↛ 0, choose s_n ≤ T_n with dist(γ_n(s_n), B_0) ≥ ε along a subsequence. A further subsequence converges, by compactness of M̄_g, to a point of B_0, which is a contradiction. **Verified.**

## 2. Step 1 (point 2, first half): correct

- **T_n is finite.** This is Lemma NH(2), an input. So [0,T_n] is compact and γ_n|[0,T_n] is uniformly continuous into (M̄_g, d).
- **Finitely many excursions.** γ_n(0) = X_n is near P, and P ∉ B(J,3r). So every excursion is entered from the sphere d(·,J) = 2r and must reach d < r. Each excursion therefore contains a sub-interval crossing the shell r ≤ d ≤ 2r. By uniform continuity such a crossing takes time ≥ τ_n > 0. The balls B(J,3r) are disjoint, so excursions at different J are disjoint, and there are at most T_n/τ_n + 1 excursions.
- **Times outside the excursions are travel times.** Suppose γ_n(s) ∈ B(J,r). Then the maximal interval of times in B(J,2r) containing s contains a time in B(J,r), so it is an excursion. Hence a time outside all excursions lies outside ⋃_J B(J,r).
- **The piece at a travel time is unique.** Let s be a travel time and z ∈ B_0 with d(z, γ_n(s)) ≤ ρ_n < r/2. Then d(z,J) > r/2 for all J, so z ∈ K_D for some D, since closure(D) ∖ ⋃B(J,r/2) = K_D. Two such points are within 2ρ_n < 4ρ_* of each other, so they lie in the same K_D. By continuity the same holds on whole travel intervals, so D is locally constant there.
- **First piece.** P ∉ Σ, so the first travel is along the piece D^1 ∋ P, and D^1 ⊂ ∂V_0.

**Verified.** The claim that the walk ends inside an excursion is Step 2.

## 3. Step 2 (points 2 and 3): correct after repair (R-a)

**Repair (R-a).** Add three conditions, all depending only on r:
- **(a′)** Shrink ρ_* if necessary so that the closed ρ_*-neighbourhood N_D of each K_D lies in the open set O_{G_D} of points whose dual graph is a contraction of G_D. This is possible because K_D is compact and K_D ⊂ Δ_{G_D} ⊂ O_{G_D}.
  - Choose ρ_* also below the Lebesgue number of a finite cover of K_D by plumbing charts.
  - Then for z ∈ K_D and X ∈ M_g with d(X,z) ≤ ρ_*, X lies in a chart at z. The node curves of z are well defined on X, up to Aut(z).
  - The non-node curves have hyperbolic length ≥ ℓ_0(r) > 0, by continuity of the hyperbolic metric in plumbing families (Wolpert/Masur, cited) and compactness of N_D.
  - Hence Ext_X ≥ ℓ_0²/(2π(2g−2)) for non-node curves, and (a) holds with δ below this bound. As stated, (a) silently needs this shrinking: points within the original ρ_* of K_D can lie near deeper strata.
- **(b0)** 2η < d(Y_0, ∂M̄_{g_i,n_i}).
- **(b1)** 2η < min{ d(σY_0, Y_0) : σ ∈ S_{n_i}, σY_0 ≠ Y_0 }. This is the labelled versus unlabelled issue: the stopping rule uses labelled distance, while "≅ Y_0" is unlabelled.

**Check of the step.** Let s ≤ T_n be a travel time on D, and z_s ∈ K_D with d(z_s, γ_n(s)) ≤ ρ_n.
- Since s ≤ T_n, every curve of ∂Σ_i has Ext ≤ δ at γ_n(s). By (a)/(a′) they are node curves of z_s.
- Hence ψ(z_s) ∈ M̄_{g_i,n_i} is defined.
- **Uniform continuity of ψ.** ψ depends on (X, isotopy class of Σ_i). It is continuous near pinched points, and the dependence on the auxiliary pants decomposition disappears in the limit ℓ(∂Σ_i) → 0. There are finitely many Mod-classes of pairs (z, subsurface bounded by node curves of z), and the z range over the compact set ⋃K_D. So ψ is uniformly continuous there, and d(ψ(γ_n(s)), ψ(z_s)) = o(1) uniformly in s.
- So d(ψ(z_s), Y_0) ≤ η + o(1) < 2η. By (b0), ψ(z_s) is smooth: Σ_i contains no node curve of z_s, and the Σ_i-side is a single vertex c of D.
- By (b), c is a constant vertex of D whose value class is [Y_0]. By (b1), and continuity of the labelled value along the travel, its labelled value is Y_0.
- Then Ext_{γ_n(s)}(∂Σ_i) = o(1), because these are node curves of z_s and d → 0 uniformly on the compact set N_D. Also d(ψ(γ_n(s)), Y_0) = o(1).
- So for n large, neither stopping condition holds at a travel time. T_n lies in an excursion, at some Q ∈ Σ.

**Verified with (R-a).**

## 4. Step 3 (point 4): gap for an arbitrary lift; repaired by the canonical lift (R-b)

**The gap.** Lifting through Def(J) → Def(J)/Aut(J) (Bredon, cited: paths lift through quotients by compact groups) is not unique. At a time s where γ_n(s) = q(ỹ) with Stab(ỹ) ≠ 1, a lift may continue as h·(lift), h ∈ Stab(ỹ). Then:
- h acts on the fibre curve as an automorphism and permutes the vanishing cycles, e ↦ h(e);
- after the switch, the T_g-marked curves ∂Σ_i correspond to the edges at h(x), not at x.

So with an arbitrary Bredon lift the chart label x is **not** well defined. The text's sentence "the T_g-marking along γ_n is compatible with the chart" is true only for a specific lift, which it does not specify.

**Repair (R-b).** The facts below are cited from memory (Abikoff, Bers; Hubbard–Koch's analytic construction of M̄_g; Wolpert).
- Let J̃ be a point of augmented Teichmüller space T̄_g over J.
- Stab(J̃) ⊂ Mod_g sits in an exact sequence 1 → Tw → Stab(J̃) → Aut(J) → 1, where Tw ≅ Z^{E(J)} is generated by the Dehn twists about the node curves α_e.
- There is a Stab(J̃)-invariant neighbourhood U of J̃, precisely invariant (gU ∩ U = ∅ for g ∉ Stab(J̃)), with:
  - U/Tw ≅ Def(J) (the plumbing/Kuranishi chart);
  - U/Stab(J̃) ≅ Def(J)/Aut(J), a neighbourhood of J in M̄_g;
  - U° := U ∩ T_g → Def(J)° a covering. Tw is torsion-free and acts properly, hence freely.

Construction of the canonical lift:
- The ray γ_n is given in T_g from the start, as the Teichmüller geodesic of the marked (X̃_n, q_n). This is the path marking.
- During an excursion at J the T_g-path is connected and lies in the preimage of B(J,2r) ⊂ B(J,3r) ⊂ image of U. That preimage is the disjoint union of the translates gU, so the path lies in a single translate. Replace J̃ by gJ̃ (relabel the marking).
- Define γ̃_n := image of the T_g-path under U → U/Tw = Def(J). This is a continuous lift into Def(J)°, determined up to one global element of Aut(J). No choice is made at orbifold points.

Consequences:
- Each node curve α_e of J̃ is a fixed marked curve on S_g. It is pinched exactly where s_e = 0, and it is Tw-invariant.
- The components of S_g ∖ ⋃_e α_e are marked subsurfaces Σ_y, one for each vertex y of J.

**Entry.** Let s be the entry time, a travel time on D. Let z_s be as in Step 2, and z̃_s the lift of z_s close to γ̃_n(s); it lies on a lifted branch β̃ of D at J. The node curves of z_s, in the marking of U, are the α_e with s_e(z̃_s) = 0. The Σ_i-side is the constant vertex c ≅ Y_0, and it corresponds to a connected subgraph S_c of J.
- **S_c is a single vertex x with no internal edge.** Suppose S_c had an edge f. Then s_f ≠ 0 along β̃ ∖ {0}, but s_f → 0 at 0. So the hyperbolic length of α_f inside the c-component would tend to 0 (continuity of hyperbolic metrics on plumbing families, cited). That component is constant, equal to Y_0, and α_f is essential and non-peripheral in it, so its length is the constant ℓ_{Y_0}(α_f) > 0. Contradiction.
- Hence c = {x}, all edges of J at x are pinched along β̃, and **Σ_i = Σ_x as marked subsurfaces**, with ∂Σ_i = {α_e : e at x}.

**Persistence.** Σ_i (path marking) and Σ_x (marking of U) are both fixed marked subsurfaces, and the path stays in U. So the identity Σ_i = Σ_x holds throughout the excursion.

**Exit.** Step 2 on D′ gives c′ = {x′} along the lifted branch β̃′ through z̃_{s′}, with Σ_i = Σ_{x′}. Then Σ_x = Σ_{x′}, so x′ = x.
- Remark: equality of the boundary-curve sets alone would not suffice. If J has two vertices joined by all its edges, x and x′ have the same edge set. The subsurface identity is what fixes the label.

**Verified with (R-b).** Orbifold points cause no trouble for the canonical lift, because it is never produced by lifting through T_g → M_g. It is the given T_g-path, pushed down by an honest covering.

## 5. Step 4 (point 5): correct, given (R-b)

- Fix (r, δ, η). Endpoint types (Q, D, Aut-orbit of (β̃, x)) form a finite set. Pass to a subsequence of n on which the type is constant, and normalise lifts by the global Aut(J) element.
- Let z̃_n be a lift of a boundary point within ρ_n of γ_n(T_n), chosen near γ̃_n(T_n). A subsequence converges to z̃^∞ ∈ q^{-1}(B_0) ∩ closure(B̃(Q,2r)).
- **F_x(0) = Y_0.** On L_x := {s_e = 0 for all e at x} the x-component F_x is holomorphic, and β̃ ⊂ L_x with F_x ≡ Y_0 on β̃ ∖ {0}.
- **z̃^∞ ≠ 0.** Suppose z̃^∞ = 0. Then γ̃_n(T_n) → 0, so Ext(α_e) → 0 for every e at x, and ψ(γ_n(T_n)) → ψ(J̃) = F_x(0) = Y_0. Both use Σ_i = Σ_x from (R-b). For large n both stopping conditions then fail at T_n, a contradiction.
- So z̃^∞ ∈ b̃ ∖ {0} for a lifted branch b̃ at Q. In the chosen ball, B_0 ∩ B(Q,3r) is the union of the branches. Pass to a further subsequence on which one stopping condition holds for all n.
  - **Ext(α_e) = δ for some e at x.** If s_e(z̃^∞) = 0, then Ext_{γ_n(T_n)}(α_e) → 0 (Maskit), contradicting = δ. So s_e(z̃^∞) ≠ 0. Since b̃ ∖ {0} lies in one stratum, e is unpinched on all of b̃ ∖ {0}: **MERGE**.
  - **d(ψ, Y_0) = η.** If some edge at x is unpinched along b̃, we are in MERGE. Otherwise b̃ ⊂ L_x, and continuity of ψ with Σ_i = Σ_x gives d(F_x(z̃^∞), Y_0) = η > 0, while F_x(0) = Y_0. Here F_x(z̃^∞) is a smooth curve because all edges at x are pinched. So F_x is non-constant on b̃: **MOV**.
- In particular b̃ ≠ β̃, as it must be.

**Verified.**

## 6. Lemma S′ and Step 5 (point 6)

### 6.1 The coarse Lemma S′ is correct
- **γ_n avoids Z.** V_0 is smooth, so V_0 ⊂ Reg X and V_0 ∩ W = (X ∖ Z) ∩ W.
- **Local sheets.** Each irreducible germ X_k has connected regular part in a Milnor ball. Its normalisation over the ball is connected, and removing a proper analytic subset keeps it connected. Distinct X_k meet inside Sing X ⊂ Z. So the components of V_0 ∩ W are the X_k ∩ W ∖ Z.
- **One sheet along a subsequence.** Each γ_n is connected, so it lies in one X_k ∩ W ∖ Z. There are finitely many, so pass to a subsequence with k fixed.
- **Limit points.** X_k ∩ W is closed in W, so z^1 ∈ X_k; note z^1 ∈ W, since it is at distance 2r from Q.
- **Near z^1.** N|_{X_k} is not identically zero on any local component of X_k at z^1, since X_k is the closure of X_k ∖ Z ⊂ M_g. So X_k ∩ ∂M̄_g is empty or of pure dimension 1 at z^1 (active lemma), and it contains z^1.
- Near z^1, B_0 = β, a smooth curve (W ∩ Σ = {Q}). So X_k ⊃ a neighbourhood of z^1 in β. β ∩ W is irreducible, so X_k ⊃ β ∩ W. The same holds for β′.

**Verified** (coarse statement: β and β′ lie in a common sheet X_k of (X, J)).

### 6.2 Upstairs: an arbitrary lift can change component
Here is a local model of reflection type. Let q(u,v_1,v_2) = (u², v_1, v_2) be the quotient by the reflection u ↦ −u. The smooth coarse surface V = {w = v_2²} (w = u²) has preimage {u = v_2} ∪ {u = −v_2}: two smooth sheets exchanged by the reflection, crossing along {u = v_2 = 0} inside the fixed hyperplane.

If V_0 passes through such a point of the reflection locus inside Def(J)°, then q^{-1}(V_0) is locally reducible there. A Bredon lift may arrive along one sheet and leave along the other. So for an **arbitrary** lift, γ̃_n need **not** lie in a single irreducible component of q^{-1}(closure V_0) ∩ B̃. The coarse conclusion of 6.1 then gives only the weaker statement:

> **(W)** some component of q^{-1}(X_k) contains β̃, and the same component contains g·β̃′ for some g ∈ Aut(J).

Proof of (W): the components of q^{-1}(X_k) are permuted transitively by Aut(J). Two distinct orbits of components would both map onto X_k, and a generic fibre is a single Aut-orbit, which forces them to share a component.

### 6.3 Repair (R-c): the canonical lift stays in one component
**Lemma S̃′.** Choose r so small that, in addition:
- B̃(J,3r) is a Milnor ball for (X̃ := q^{-1}X, 0). The irreducible components X̃_1, …, X̃_p of X̃ ∩ B̃ are then representatives of the germ components (cited, conic structure).
- Distinct lifted branches of q^{-1}(B_0) meet only at 0 in B̃, and each lifted branch minus 0 is smooth. There are finitely many pairs of distinct irreducible curve germs at 0, and each pair meets only at 0 in a small enough ball; Puiseux parametrisations give smoothness.

Let the γ̃_n be canonical lifts (R-b) of transition paths whose endpoints converge to z̃^1 ∈ β̃ ∖ {0} and z̃^2 ∈ β̃′ ∖ {0}. Then some X̃_l contains both β̃ and β̃′.

*Proof.*
1. **The path lies on a holomorphic curve in q^{-1}(V_0).** Let F: H → T_g be the Teichmüller disc of (X̃_n, q_n). Since V_0 is totally geodesic and (X_n,q_n) is generating, F(H) lies over V_0. Let R be the connected component of F^{-1}(gU) containing the parameters of the excursion; R is a connected Riemann surface. Put f := (U° → Def(J)°) ∘ F|_R. Then f is holomorphic, f(R) ⊂ q^{-1}(V_0) ∩ B̃, and γ̃_n ⊂ f(R).
2. **f(R) lies in one component.** Each f^{-1}(X̃_l) is an analytic subset of R, and their finite union is R. So one of them has interior, and by the identity theorem it is all of R. Hence γ̃_n ⊂ X̃_{l(n)}, even if f(R) passes through crossing points such as those in 6.2: a smooth connected curve germ cannot change sheets.
3. **Conclusion.** Pass to a subsequence with l(n) = l. X̃_l is closed in B̃, so z̃^1, z̃^2 ∈ X̃_l. X̃_l is irreducible of dimension 2, so X̃_l ∩ {∏ s_e = 0} is nowhere dense in it and has pure dimension 1 at z̃^1. Near z̃^1, q^{-1}(B_0) = β̃, a smooth curve, by the choice of r. So X̃_l contains an open piece of β̃, hence all of β̃. The same argument gives β̃′. ∎

**Step 5 then holds upstairs for every transition, and at the endpoint.** At the endpoint, z̃^2 = z̃^∞ ∈ b̃ ∖ {0}.

## 7. Point 7: dependence on (r, δ, η, n), and existence of one chain

**Order of choices.**
- First r: all conditions of §2.3, the Milnor conditions up- and downstairs, and the branch-separation condition of 6.3.
- Then δ, η, depending on r: (a), (a′), (b), (b0), (b1).
- Then n_0 such that, for n ≥ n_0, ρ_n < min(ρ_*, r/2) and the o(1) terms of Step 2 are below δ and η.

**The gap.** The text implicitly treats the chain as fixed while n → ∞, both in Step 4 and in Step 5 ("over the subsequence these points converge"). But T_n → ∞, and the number of excursions in [0,T_n] can be unbounded in n: the walk may loop around B_0. So the chains for different n need not agree, and "the same transition along a subsequence" is not automatic.

**Repair (R-d).**
- A *transition type* is an Aut(J)-orbit of (J, β̃, β̃′, x); an *endpoint type* is an orbit of (Q, D, β̃, x). Both sets are finite.
- Call a type recurrent if it occurs in the walks of infinitely many n. Let N ≥ n_0 exceed the last n at which any non-recurrent type occurs.
- Fix any n ≥ N and take its walk chain. Every transition of this chain has a recurrent type τ.
  - Along the infinite set of n′ where τ occurs, the corresponding excursions are canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃(J,2r). Their entry and exit boundary points lie at distance ≈ 2r from 0.
  - A subsequence converges to points of β̃ ∖ {0} and β̃′ ∖ {0}. This is the sequence of paths the chain form requires, and Lemma S̃′ applies to it.
- The terminal type τ_end of the chosen n is also recurrent. Step 4, run along the n′ of type τ_end, supplies b̃, the MERGE/MOV dichotomy and the convergent terminal paths.

So a single finite chain with all required properties exists. The only caveat: the witnessing sequences of paths at different transitions come from different subsequences of walks, not from one common sequence.
- If the downstream argument needs one common sequence n′ for all transitions at once, this is **not** established: the chain combinatorics need not stabilise.
- As far as I can see, the per-transition form listed in the brief needs only per-transition sequences, and that is what is proved.

## 8. Final verdict

**Proved, with repairs (R-a)–(R-d), modulo the cited inputs** (Lemma PA, Lemma NH, Kerckhoff, Maskit, the T̄_g/Def chart description, collar and continuity of hyperbolic metrics in plumbing families, local analytic geometry). There is a chain:
- pieces D^1 ∋ P (D^1 ⊂ ∂V_0), D^2, …, D^k; transition points J_1, …, J_{k−1}; an endpoint Q_0;
- at each J_m: lifts β̃_m, β̃′_m and a single chart vertex x_m, which is the constant vertex ≅ Y_0 (labelled, = Y_0) of D^m along β̃_m and of D^{m+1} along β̃′_m;
- witnessing sequences of canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃, with endpoints converging to points of β̃_m ∖ {0} and β̃′_m ∖ {0};
- β̃_m and β̃′_m lie in a common irreducible component of q^{-1}(closure V_0) at 0 (upstairs, by Lemma S̃′), and hence in a common sheet downstairs;
- at Q_0, the entering lift β̃ with vertex x and the terminal lifted branch b̃ are joined in the same way, and along b̃ the vertex x is MERGED or MOVING.

**What the original text gets wrong or leaves implicit.**
- (R-a): three extra smallness conditions.
- (R-b): the chart label x is ill-defined for arbitrary Bredon lifts through orbifold points. The canonical lift through augmented Teichmüller space fixes this.
- (R-c): the upstairs same-component claim is false for arbitrary lifts (reflection model). For them only the weaker (W) holds. It is true for the canonical lift, because that lift lies on a Teichmüller disc.
- (R-d): chain combinatorics depend on n. Fixed by recurrent types; the witnessing sequences are per transition.

**Open / not established.**
- A single subsequence n′ witnessing all transitions of one chain simultaneously.
- Anything about the cited inputs themselves (in particular Lemma NH and the T̄_g/Def(J) chart description, which I used in the form stated in §4).

Overall result: **repaired**.


### Theorem X*_all, Lemma 1SS, Corollary IMOV_all (verbatim)
# round10_q1 — attempt on MS10

## Status / plan
- **Outcome: PARTIAL.** I neither prove MS10 in full nor give a counterexample.
- **What is new and proved here** (modulo cited standard facts and the run's inputs, listed in §6):
  1. **Theorem X\*\_all.** Theorem X\* of round9_q4 holds for pieces in **every** stratum, not only product-type ones (§2). Steps 1–4 of R8-1 Theorem X are redone on a lifted piece Ê ⊂ ∏_w M_w. This was listed as open in round9_q3 (Remark 4, "Not proved") and round9_q4 (open item (ii)). I also correct a small slip in the homological step of X\*. The slip does not affect its conclusion.
  2. **Lemma 1SS (one chart sheet per excursion).** Assume the reading (T4) of round9_q5 (every component of the preimage of V_0 in T_g is a totally geodesic complex submanifold). Then every excursion of the walk chain (Prop. K_w) lifts into a **single irreducible component S** of the preimage of closure(V_0) in the chart, and S contains both the entering lift and the leaving lift (§3). Before this, round9_q3 (Cor. SS′(b)) and round9_q4 (Lemma S′) only placed *some* lift of the entering branch in a common sheet with the leaving lift.
  3. **Corollary IMOV\_all (§4).** Combine 1 and 2. In the walk chain, at every junction and at the endpoint, **in every stratum**: if Q lies in the stratum of the entering or of the leaving piece, then the entering and leaving lifted branches coincide as sets. Consequences:
     - the endpoint is never interior-MOV;
     - there are no junction crossings;
     - the "turning twin" (T) never occurs.
     So the MS10 instances that the chain uses are **proved whenever Q is an interior point of the piece of β̃ or of the piece of b̃**. For walk-chain data the IMOV part of chain step (d) is settled for non-product strata.
  4. **Residual (precisely located).** MS10 for walk-chain data is open only when Q is a **puncture of both** adjacent pieces. Equivalently, these are the persistent twin (b) at a junction and the endpoint twin (e) with MERGE or puncture-MOV, at a point Q of a non-product stratum.
- **Chain check (§5).** I found no logical flaw in the derivation "MS10 + (Rig) + proved entries ⇒ claim". But **MS10 as worded is stronger than what the chain uses.** It allows arbitrary joining paths in q^{-1}(V_0) ∩ B. The walk chain supplies Teichmüller-ray paths, which satisfy one-sheet property 2. I recommend replacing MS10 by MS10′ (§5), which carries that property. MS10′'s open part is exactly item 4.
- I also re-derived the "global tracking along Prop.-K segments + finite-set continuity" argument independently. It coincides with R8-5 Theorem A, so it is not claimed as new; see §6.

---

## 1. Conventions

- Readings (R1), (R2) with H_0 = id, as in the task file. The orbifold reading (R2^orb) is **not** used.
- **(T4)** (round9_q5 §0). Every component S_T of the preimage of V_0 in Teichmüller space T_g is a complex submanifold that contains every real Teichmüller geodesic tangent to it.
  - This is the literature's meaning of "totally geodesic subvariety": the image of a totally geodesic complex submanifold of T_g.
  - Smoothness of V_0 in the coarse space alone would not give it, so I state it as a reading.
  - It is used only in §3.
- **Charts.** For a stable curve Q:
  - Def(Q) is the Kuranishi germ, with smoothing parameters s_e, e ∈ E(G_Q).
  - q : B → B/Aut(Q) is the chart on a small Aut(Q)-invariant ball B.
  - The stratum locus is L := {s_e = 0 ∀e}.
  - Fix an identification G_Q ≅ G of the dual graph. Partial normalisation gives the holomorphic map Π : L → ∏_{w∈V(G)} M_w, with ξ_G ∘ Π = q on L. Here ξ_G : ∏_w M_w → Δ_G is the gluing map. It is finite, and on coarse spaces it is the quotient by Aut(G).
- **Pieces and lifted pieces.**
  - A *piece* is a 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, for some stratum Δ_G (product type **not** assumed).
  - A *lifted piece* is an irreducible component Ê of the 1-dimensional analytic set ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ ∏_w M_w with ξ_G(Ê) dense in E.
  - Ē̂ denotes the closure of Ê in ∏_w M̄_w. It is a compact irreducible curve, being a component of the compact analytic set ξ̄_G^{-1}(closure(V_0) ∩ closure(Δ_G)). Here ξ̄_G is finite, hence proper.
  - Ê^ν denotes the normalisation of Ê, a connected Riemann surface.
- **Sheet.** A *sheet* at Q is an irreducible component of the germ at 0 of q^{-1}(closure V_0). For B small these are the global irreducible components of q^{-1}(closure V_0) ∩ B.

## 2. Theorem X\*\_all: Theorem X\* in every stratum

**Setting** (as in R8-1 §3.1 and round9_q4 §1.1, but with **no product hypothesis**):
- V_0 ⊂ M_g is closed, 2-dimensional and totally geodesic.
- E is a piece in a stratum Δ_G, and Q_0 ∈ E. So Q_0 is an interior point of E in its own stratum.
- β is a local branch of E at Q_0, and β̃ ⊂ L ⊂ Def(Q_0) is a lift of β through 0.
- S is a sheet at Q_0 containing β̃.
- ν : Ŝ → S is the normalisation, ŝ_0 := ν^{-1}(0), and B̂ := ν^{-1}(S ∩ {∏ s_e = 0}).
- Ê_1, …, Ê_r are the components of the germ (B̂, ŝ_0) that map onto β̃. C_1, …, C_m are the others. **The others include any component mapping onto a different lift aβ̃ ≠ β̃ of the same coarse branch.**

**Theorem X\*\_all.** m = 0. Every component of the boundary curve of Ŝ at ŝ_0 maps onto β̃. Equivalently, S ∩ {∏ s_e = 0} = β̃ near 0.

The proof of round9_q4 has two parts:
- Steps 1–4 of R8-1 Theorem X, which produce discs D̂_n → L̂;
- the homological step, which is local in Ŝ and uses no product hypothesis.

Product type was used only in Step 3 (R8-1 Remark 2), through a global coordinate f_j on E ⊂ ∏ M_w. I redo Steps 1–4 with E replaced by a lifted piece.

### 2.1 Steps 1–4 for an arbitrary stratum

**Step 1 (base point, approximants).**
- Ê := the lifted piece containing the germ Π(β̃). Π(β̃) is a curve germ at ẑ_0 := Π(0) inside ξ_G^{-1}(E), so it lies in a lifted piece.
- e_0 ∈ Ê^ν is the point over ẑ_0 on the branch Π(β̃).
- B ⊂ Ê^ν is a small closed disc around e_0. Its image in Ê is a neighbourhood of ẑ_0 on the branch Π(β̃). It maps under ξ_G into a small neighbourhood U of Q_0, and B ∖ {e_0} maps into β ∖ {Q_0}.
- Pick P_1 ∈ β ∖ {Q_0}, with lift P̃_1 ∈ β̃ and Π(P̃_1) in the image of B ∖ {e_0}. Take P_1 generic in the sense of R8-1 Step 1, and also require that Π(P̃_1) lie on no other component of ξ_G^{-1}(closure V_0 ∩ Δ_G). The excluded set is discrete in β.
- **Lemma PA holds at P_1.** Its proof (PR-H §1) uses only:
  - the local plumbing chart at P_1 (Def(P_1) with coordinates (z, s_e));
  - a normalised local branch N of closure(V_0) along E at P_1;
  - a ≠ 0, where a is the s-derivative of z.

  None of these needs product type. In particular a possible generic automorphism group of the piece is harmless, since one works in Def(P_1).

  So there are X_n ∈ V_0 ∩ N with X_n → P_1, and generating pairs (X_n, q_n), with transplanted limits (q_w)_w satisfying Σ‖q_w‖ = 1. There is a vertex j with q_j ≠ 0 and ‖a_j‖ = A > 0, so the j-coordinate moves along E at P_1. The approximants can be chosen in the sheet S, as in R8-1 Step 1.

**Step 2 (the limit disc and its lift).**
- Let D_n : 𝔻 → V_0 be the Teichmüller disc of (X_n, q_n). It lies in V_0 by total geodesy.
- Let D̃_n ⊂ T_g be its lift through a lift of X_n. This gives a marking along all of D_n.
- R8-1 Step 2 is local and stratum-independent. Each D_n(w) stays within Teichmüller distance ρ = d_𝔻(0,w) of X_n, so by Wolpert and Abikoff every limit point lies in a compact part K_ρ of Δ_G. A subsequence converges locally uniformly to L : 𝔻 → B_0 ∩ Δ_G with L(0) = P_1.
- **The lift L̂.** For w ∈ 𝔻, the node curves of L(w) are, under the disc's marking, exactly those of P_1 (same estimate). So the components of L(w) are labelled by the vertex subsurfaces of P_1.
  - Label those subsurfaces by V(G) through the chart Def(Q_0) at the lift X̃_n near P̃_1. This is the identification fixed in Π.
  - This defines L̂(w) ∈ ∏_w M_w with ξ_G ∘ L̂ = L and L̂(0) = Π(P̃_1).
  - Locally near w, L̂ equals Π_Z ∘ (limit of the chart lifts of D_n into Def(Z)), with Z a limit point and Π_Z the partial normalisation of Def(Z) under the marking-induced labels. Chart lifts are images of the T_g-lift (T_g ↔ Def chart description, cited as in R8-1). So L̂ is well defined and holomorphic.
- **L̂(𝔻) ⊂ Ê.**
  - L̂^{-1}(Ê) is an analytic subset of 𝔻, since Ê is closed analytic in ∏_w M_w.
  - Near w = 0, L̂ takes values in ξ_G^{-1}(E) near Π(P̃_1), and that point lies only on Ê. So L̂^{-1}(Ê) contains a neighbourhood of 0.
  - By the identity theorem, L̂^{-1}(Ê) = 𝔻.
  - L̂ is not contained in Sing(Ê), so it lifts to Ê^ν. I keep the name L̂.
- **Non-constancy.** By (Fl), the j-component of L(w), labelled through the marking, is A_w·(Y_j(P_1), q_j). So pr_j ∘ L̂ = τ, the Teichmüller disc of (Y_j(P_1), q_j) in M_j := M_{g_j,n_j}. It is non-constant.

**Step 3 (L̂ : 𝔻 → Ê^ν is surjective).**
- C_j := pr_j(Ē̂) is a compact irreducible curve in M̄_j: it is the image of an irreducible compact curve (Remmert), and it is not a point because τ is non-constant.
- Put C_j° := C_j ∩ M_j. It is irreducible, and τ(𝔻) ⊂ pr_j(Ê) ∩ M_j ⊂ C_j°.
- Let τ̃ : 𝔻 → T_j lift τ, and put Δ̃ := τ̃(𝔻).
  - By (Prop), Δ̃ is a closed 1-dimensional submanifold, and its Mod-translates form a locally finite family.
  - So Δ̃ is an irreducible component of the preimage of C_j° in T_j.
  - Its image in M_j is closed and analytic, hence equal to C_j° by irreducibility.
  - With Γ := Stab(Δ̃), the map 𝔻/Γ → C_j° is proper.
- Let Λ be the set of holomorphic λ : 𝔻 → Ê^ν with pr_j ∘ λ = τ.
  - The map pr_j : Ê^ν → Ĉ_j (normalisation of C_j°) is the restriction of the finite map of compact Riemann surfaces (Ē̂)^ν → Ĉ_j to an open subset. So its fibres have at most deg elements.
  - A lift is determined by its value at one point over an unbranched value. Hence |Λ| ≤ deg, and L̂ ∈ Λ.
- Γ acts on Λ by precomposition. So Γ_L := Stab_Γ(L̂) has finite index, and L̂ descends to L̄ : 𝔻/Γ_L → Ê^ν.
- **L̄ is proper.** For compact K ⊂ Ê^ν, L̄^{-1}(K) is closed in (pr_j ∘ L̄)^{-1}(pr_j K). The latter is compact, because pr_j ∘ L̄ : 𝔻/Γ_L → Ĉ_j is proper (finite index in a proper map).
  - This needs **no** properness of pr_j on Ê, so it is unaffected by punctures of Ê at which only other coordinates degenerate. This is the same argument as R8-1.
- A proper non-constant holomorphic map to the connected Ê^ν is surjective.

**Step 4 (a path to Q_0).** Verbatim as R8-1 Step 4, with Ê^ν and e_0 from Step 1.
- Let W be the component of L̄^{-1}(int B) containing [0]. L̄|_W : W → int B is proper and non-constant, hence onto. Pick [w*] ∈ W with L̄([w*]) = e_0.
- Lift a path from [0] to [w*] in W to a path π ⊂ 𝔻 from 0 to w*. This is path lifting for properly discontinuous actions (Bredon, cited).
- Choose Ω ⊃ π connected and relatively compact, with L̂(Ω̄) ⊂ image of B.
- Then L(w*) = ξ_G(ẑ_0) = Q_0, and L(Ω) lies in β (coarse) ∪ {Q_0}.
- **Chart lift.** For n large, D_n(Ω̄) ⊂ U ∩ V_0. Lift D_n|_Ω to D̃_n : Ω → Def(Q_0) with D̃_n(0) = X̃_n. It lies in S (R8-1 Step 5; under (T4) also automatic, see §3). A subsequence converges to L̃, a lift of L|_Ω.
  - L̃(Ω) ⊂ ⋃_a aβ̃, and L̃^{-1}(0) = L^{-1}(Q_0) ∩ Ω is discrete, since q^{-1}(Q_0) = {0}.
  - The sets aβ̃ ∖ {0} are pairwise disjoint near 0, because distinct irreducible curve germs at 0 meet only at 0 in a small ball. Ω minus a discrete set is connected and its image contains P̃_1 ∈ β̃. Hence L̃(Ω) ⊂ β̃.
  - L̃(w*) = 0.

This gives exactly the data used by round9_q4 §1.2, with no product hypothesis:
- D̂_n : Ω → Ŝ ∖ B̂;
- D̂_n → L̂_S (the lift of L̃ to Ŝ);
- L̂_S(w*) = ŝ_0 and L̂_S(Ω) ⊂ Ê_1.

### 2.2 The homological step, with a small correction

I re-checked round9_q4 §1.4. One sentence is not justified as written, but the argument survives.
- **The sentence.** "C′ ∩ Ê′_1 ⊂ Exc, hence L′(Ω̄_ε) ∩ C′ = ∅." The strict transforms C′ and Ê′_1 may meet at a point of Exc, unless the resolution separates them. In that case the disc L′ passes through C′ at L′(w*).
- **Why the argument survives.**
  - The cycle is Z_n := D′_n(Ω̄_ε) − L′(Ω̄_ε) + A_n. Its pieces D′_n and A_n are disjoint from C′, and the disc L′ meets C′ at most at the isolated interior point w*, with local multiplicity μ ≥ 0.
  - By (Int), Z_n · C′ = −μ ≤ 0.
  - On the other hand, [Z_n] = Σ_j k_j[F_j] with all k_j > 0 (by (Neg) and (Pos), unchanged). Also F_j · C′ ≥ 0 for all j and > 0 for some j. So Z_n · C′ > 0.
  - This is still a contradiction. Alternatively, blow up further so that C′ and Ê′_1 are disjoint.

Hence **m = 0 in every stratum.** ∎

**Corollary X′\_all.** Theorem X′ (round9_q3) and all corollaries of X\* (round9_q4 §3: no junction crossing in a different coarse branch, no interior-MOV end except a same-branch twin) hold for non-product strata. In particular, R8-1 Remark 2, round9_q3 Remark 4 and round9_q4 open item (ii) are settled. The cited inputs remain those listed in §6.

---

## 3. Lemma 1SS: a walk excursion lies in one chart sheet (assuming (T4))

**Set-up.** This is the walk chain of Prop. K_w (round9_q4 §2.3), with r fixed. Let J be a transition point (a junction, or the endpoint Q_0).
- Take the chart ball B ⊂ Def(J) small, with q(B) ⊃ B(J, 3r). Here r is taken small enough for the following to hold.
  - The global irreducible components S_1, …, S_k of q^{-1}(closure V_0) ∩ B are the sheets at J.
  - q^{-1}(B_0) ∩ B is the union of the finitely many lifted branches at 0, and any two distinct ones meet only at 0.
- Let I = [s_1, s_2] be the excursion interval of the ray γ_n(s) = g_s X_n.
- γ_n is the projection of the T_g-ray γ̂_n.
- The canonical chart lift is γ̃_n := p_c ∘ γ̂_n on I. Here 𝔘_c is the component of the preimage in T_g of q(B) ∩ M_g that contains γ̂_n(I), and p_c : 𝔘_c → B° := B ∖ {∏ s_e = 0} is the holomorphic local biholomorphism with q ∘ p_c = (T_g → M_g). This is the T_g ↔ Def chart description, cited exactly as in R8-1 Step 2 and in the walk chain, Step 3.

**Lemma 1SS.** Assume (T4). Then:
- for each n, γ̃_n(I) lies in a single sheet S = S_{k(n)};
- after passing to a subsequence (already done in K_w to fix the combinatorial data), S is independent of n;
- S contains the entering lift β̃, and S contains the leaving lift β̃′ at a junction, or the terminal lift b̃ at the endpoint.

*Proof.*
1. **The ray lies in one T_g-sheet.**
   - X_n is a generic point of V_0, not an orbifold point, so exactly one component S_T of the preimage of V_0 passes through the lift X̂_n.
   - The vector v_n of Lemma PA is tangent to V_0, so its lift is tangent to S_T. q_n is its norming differential, possibly rotated by e^{−2iθ_n} as in Lemma NH. The Teichmüller geodesic of q_n is therefore tangent to the complex line spanned by v_n, which lies in T S_T.
   - By (T4), the whole ray γ̂_n lies in S_T.
2. **One global component in the chart.** Let W be the connected component of S_T ∩ 𝔘_c containing γ̂_n(I). It is a connected complex surface, and p_c|_W is a holomorphic immersion into A := q^{-1}(V_0) ∩ B°.
   - The components of A are A_l := S_l ∩ B°. Each is irreducible: an irreducible analytic set minus a proper analytic subset stays irreducible.
   - For w ∈ W and a small connected neighbourhood P of w in W, the analytic sets P ∩ p_c^{-1}(A_l) cover P. One of them has interior, hence equals P (identity theorem).
   - Let K(w) be the set of l with p_c(P) ⊂ A_l for some neighbourhood P of w. If l ∈ K(w) and w′ ∈ P, then P′ ∩ p_c^{-1}(A_l) has interior in P′, so l ∈ K(w′). So K is locally constant, hence constant on the connected W.
   - Thus p_c(W) ⊂ A_l for one l, and γ̃_n(I) ⊂ S_l.
3. **Entering lift.**
   - At the entry time s_1, γ̃_n(s_1) lies within ρ_n → 0 of a point z̃_n ∈ β̃ with d̄(q z̃_n, J) ∈ [r, 2r]. Pass to a limit z̃^1 ∈ β̃ ∖ {0}. Since S is closed in B, z̃^1 ∈ S.
   - Near z̃^1, q^{-1}(B_0) coincides with β̃, by the choice of B.
   - ∏ s_e vanishes at z̃^1. It vanishes identically on no local component of S at z̃^1, because dim(S ∩ {∏ s_e = 0}) ≤ 1. So S ∩ {∏ s_e = 0} is pure 1-dimensional at z̃^1 (Krull).
   - Hence S contains the germ of β̃ at z̃^1. Then S ⊃ β̃: the normalisation of the irreducible germ β̃ is a disc, and S ∩ β̃ is an analytic subset of it with interior.
4. **Leaving lift.**
   - At a junction, the exit point gives z̃^2 ∈ β̃′ ∖ {0} in the same way, so S ⊃ β̃′.
   - At the endpoint, z̃^∞ ∈ b̃ ∖ {0} is the limit of the nearest boundary lifts of γ̃_n(T_n) (K_w Step 4), so z̃^∞ ∈ S. Near z̃^∞ the only lifted branch is b̃, and the same argument gives S ⊃ b̃. ∎

**Remark.**
- Lemma 1SS replaces the coarse Lemma S′ / SS′ of round9_q3 and round9_q4. Those lemmas allowed the track's chart lift to change sheet at interior orbifold points of q^{-1}(V_0). That is where the same-branch twin (T) came from.
- (T4) excludes such sheet changes for the *canonical* lift of a Teichmüller ray. At an orbifold point the ray continues in the same T_g-sheet S_T, by uniqueness of geodesics.

---

## 4. Corollary IMOV\_all: no interior transitions, no interior-MOV endpoint, in any stratum

**Corollary IMOV\_all.** Assume (T4), the walk chain K_w, and Theorem X\*\_all. Let J be a transition point with entering lift β̃ (piece D) and leaving lift β̃′ (piece D′; at the endpoint, b̃ and E_b).
- (a) If J lies in the stratum of D or in the stratum of D′, then β̃′ = β̃ as sets. Then D′ = D, and x is intact and constant ≡ Y_0 along β̃′ = β̃.
- (b) Consequently, at the endpoint Q_0 is a **puncture of both D and E_b**. In particular the endpoint is MERGE or puncture-MOV, never interior-MOV, whatever the type of the stratum of Q_0.
- (c) Every junction at which the walk changes piece or lift is a puncture of both adjacent pieces. Junction crossings (R8-8 Prop. 3(c), Lemma J (J3)) and the turning twin (T) do not occur.

*Proof.*
- (a) Suppose J lies in the stratum of D, so J is an interior point of D.
  - By Lemma 1SS, S ⊃ β̃ ∪ β̃′.
  - Theorem X\*\_all, applied to (E, β, S) := (D, the coarse branch of β̃, S), gives S ∩ {∏ s_e = 0} = β̃ near 0.
  - β̃′ is an irreducible curve germ at 0 inside that set, so β̃′ = β̃.
  - The case of the stratum of D′ is symmetric.
  - Equal sets have equal patterns, so the pieces coincide. x is constant ≡ Y_0 along β̃ (STAY on the entering piece), hence along β̃′.
- (b) Suppose Q_0 lay in the stratum of D or of E_b. By (a), b̃ = β̃, so x would be intact and constant along b̃. This contradicts MERGE and MOV (K_w Step 4).
- (c) This follows from (a). ∎

**Consequence for MS10.**
- The instances of MS10 that the chain uses are walk-chain data: β̃, b̃, x as produced by K_w at a non-product point Q.
- If Q is an interior point of the piece of β̃ or of b̃, then β̃ = b̃ as sets. The transport families coincide, Ñ_b̃ = Ñ_β̃, so Y-persistence along β̃ **is** Y-persistence along b̃, and MS10's conclusion holds.
- At the endpoint this case does not even arise, by (b).
- The non-constancy hypothesis on Y is not needed for this part.
- **What remains of MS10 (walk-chain form):** Q a puncture of both adjacent pieces. These are exactly the persistent-twin junction (R8-8 Prop. 3(b), round9_q3 §5(b)) and the endpoint twin with MERGE or puncture-MOV (R8-8 Prop. 3, endpoint; round9_q3 §5(e)), at points of non-product strata.

---

## 5. Check of the chain

I re-read chain steps 1, 2(a)–(d) against the spliced proofs.

1. **Step 1** (Goal ⇐ MS8 + (Rig) + PR-A) is correct as stated.
   - MS10 has the hypothesis "Y non-constant". So if (Rig) holds and the problem's claim is true, MS10 is vacuously true.
   - Conversely, any configuration violating MS10 under (Rig) would contradict the claim. MS10 is therefore not easier than the problem in the hard case. A "counterexample to MS10" would be a counterexample to the problem, given (Rig).
2. **Steps 2(a)–(c)** use only the entries cited. I found no gap in their logic, but they inherit two cited inputs:
   - the K_w inputs (Lemma PA, Lemma NH, (Fl), Kerckhoff, Maskit, the T_g ↔ Def chart description, the collar lemma);
   - for Theorem X′ / X\*: (Res), (Neg), (Int), (RA).
3. **Step 2(d) and the wording of MS10.**
   - MS10 allows the joining paths γ_n to be *arbitrary* paths in q^{-1}(V_0) ∩ B. Such paths may change sheet at interior orbifold points.
   - The chain applies MS10 only to walk-chain data. There the paths are canonical lifts of Teichmüller ray segments, and by Lemma 1SS (under (T4)) they stay in one sheet.
   - This is not an error, since a stronger statement is asked than is needed. But it hides that the IMOV and turning-twin part of step (d) is settled by §4.
   - I propose the following replacement, which suffices for the chain verbatim.

> **MS10′.** As MS10, with "joined inside the chart" replaced by "β̃ and b̃ are the entering and leaving (or terminal) lifts of an excursion of the walk chain K_w at Q (so they lie in one sheet S by Lemma 1SS), and Q is a puncture of the pieces of both β̃ and b̃".

   By §4, MS10 for walk-chain data at points Q that are interior to one of the two pieces is **proved**, under (T4) and the inputs of §6. So MS10′ is all that remains of MS10 for the chain.
4. **Readings.**
   - The chain implicitly uses the reading (Sm) or (T4) for "smooth totally geodesic V_0" (round9_q3, round9_q5).
   - I use (T4) explicitly.
   - Without (T4), Lemma 1SS is unavailable, and the same-branch twin (T) of round9_q3 Cor. IM(c) returns for non-product strata (now with Theorem X\*\_all available).
5. **Remaining dependence.** As the task file says, the chain still needs entry 82 ((Rig)) in addition to MS10/MS10′.

---

## 6. What I re-derived and found not to be new; inputs used

- **Global tracking (not new).** My first approach transported the Prop.-K Teichmüller segments to time t:
  - (s,τ) ↦ H_τ(g_s X_n);
  - with a class function that lies, at fixed t, in a finite set S_t;
  - and is hence constant along the segment.

  This is exactly R8-5 Theorem A (with round9_q5's general-position refinement). It reduces the twin problem to the lift monodromy of the transport square. The monodromy is non-trivial only if 2-dimensional families of α-symmetric curves of V_τ (α ∈ Aut(J) moving x) accumulate at J (cases (A2), (B), (D3) of round9_q5). I have nothing new to add on these cases.
- **Frozen merging copy (not new).** By the generic-time Theorem N applied to the value function of the merging label instead of Y, an endpoint twin forces a component frozen at Y_0 at the relevant lift for all t. This is round9_q8 Lemma 1′.
- **Inputs used in §§2–4, cited from memory or taken from the run as stated:**
  - Lemma PA (PR-H §1), whose proof is local;
  - (Fl) (sketched in R8-1, cited);
  - (Prop) (Teichmüller discs are closed, with locally finite translates);
  - Wolpert's lemma and Abikoff's continuity;
  - the T_g ↔ Def(Q) chart description;
  - path lifting for properly discontinuous actions (Bredon);
  - (Res), (Neg), (Int), (Pos) of round9_q4;
  - Krull's theorem and Remmert's proper mapping theorem;
  - Proposition K_w (round9_q4, proved there modulo PR-H's inputs);
  - the reading (T4).

---

## 7. Summary

**Proved here** (given the inputs of §6):
1. **Theorem X\*\_all** (§2). For a piece E in **any** stratum and Q_0 ∈ E, every sheet of closure(V_0) at Q_0 containing a lift β̃ of a branch of E meets the boundary near Q_0 only in β̃. This settles the non-product extension of Theorems X, X′ and X\* left open in R8-1 Remark 2, round9_q3 Remark 4 and round9_q4 open item (ii).
2. A correction to round9_q4 §1.4. L′ may meet C′ on the exceptional set. The sign argument still gives the contradiction.
3. **Lemma 1SS** (§3, under (T4)). Each excursion of the walk chain lifts into one sheet, which contains the entering and leaving (or terminal) lifts.
4. **Corollary IMOV\_all** (§4).
   - In every stratum, the walk chain has no interior-MOV endpoint, no junction crossing and no turning twin (T).
   - Every genuine transition happens at a point that is a puncture of both adjacent pieces.
   - Hence MS10 holds, for the data the chain feeds it, whenever Q is an interior point of the piece of β̃ or of b̃.

**Not proved:**
- MS10 in full.
- MS10′, i.e. the twin case at points Q of non-product strata that are punctures of both pieces: the persistent twin (b) at junctions and the endpoint twin (e). No counterexample was found either.

**Open (precise):**
1. **MS10′** (§5). Equivalently, exclude for smooth totally geodesic V_0 the following situation:
   - a 2-dimensional family of α-symmetric curves of V_τ, τ ≠ 0, with α ∈ Aut(J) moving x;
   - accumulating at a point J that is a puncture of both pieces of a walk transition;
   - in one of the forms (A2) (Teichmüller curve of symmetric curves of V_0 with cusp J, or a symmetric sheet), (B) (an α-fixed boundary branch, including (B-pure)), or (D3) of round9_q5.

   Alternatively, prove (Lock) of the twin pair in these cases.
2. **Entry 82 (Rig)** for every admissible family. This is still needed by the chain after MS10′.
3. The reading (T4). It is needed for Lemma 1SS. Without it, the turning twin (T) at non-product points is open again; Theorem X\*\_all reduces it to a same-coarse-branch twin.
4. The inputs inherited from Proposition K and PR-H, listed in §6.



### Theorem X′ / Lemma P, Lemma SS, Lemma PT (verbatim §§1–3)
# round9_q3 answer (final; PARTIAL)

## Status / plan
- MS8 is NOT proved in full here, and no counterexample is given. This file is a PARTIAL answer.
- New results in this file (full summary in §7):
  1. **Theorem X′**: Theorem X of R8-1 holds with no Q-Cartier / Q-factoriality hypothesis. So the crossing case (Cr2) of R8-1 §4.3 disappears for product-type pieces.
  2. **Lemma SS** (same sheet): if V_0 is locally irreducible at its points, every transition of Prop K's track (junction or end point) takes place inside one sheet of closure(V_0). So (Cr1) never occurs at a track transition.
  3. **Lemma PT** (product strata carry no twins): in a product-type stratum, an automorphism of a curve fixes every vertex of positive-dimensional type.
  4. **Corollary IM**: combining 1–3, an interior-MOV end point of Prop K is impossible when the stratum of the end point is of product type. In general (non-product stratum, assuming Theorem X′ extends to it) an interior-MOV end point must be a "same-branch twin" (type (T) of R8-6).
- What remains open: twins at junctions and end points lying in NON-product strata, and the non-product extension of Theorem X / X′ (stated as a remark, not proved).

Conventions: readings (R1), (R2) with H_0 = id, and the notation of the task file. "Product type" for a stratum Δ_G means: the gluing map ξ_G : ∏_w M_w → Δ_G is injective (on coarse spaces). Reading of "smooth" used in Lemma SS: **(Sm)** every point of V_0 is a locally irreducible point of V_0 (this holds if V_0 is a complex submanifold of the coarse space, and also if V_0 is an embedded suborbifold).

---

## 1. Theorem X′: Theorem X without any Q-Cartier hypothesis

### 1.1 Cited standard facts (from memory)
- **(Res)** Resolution of a normal surface germ (Ŝ, ŝ_0): for a small Stein neighbourhood W of ŝ_0 there is a proper holomorphic map π : W̃ → W, W̃ a complex manifold of dimension 2, π biholomorphic over W ∖ {ŝ_0}, with exceptional set E := π^{-1}(ŝ_0) a compact, **connected** curve (Zariski's main theorem, Ŝ normal) with irreducible components E_1, …, E_r. (If ŝ_0 is a smooth point one may take π = blow-up, r = 1.)
- **(Neg)** (Du Val, Mumford, Grauert) The intersection matrix M = (E_k · E_j) is negative definite. Its off-diagonal entries are ≥ 0, and its dual graph is connected because E is connected.
- **(Str)** For an irreducible curve germ A ⊂ Ŝ at ŝ_0, its strict transform Ã := closure of π^{-1}(A ∖ ŝ_0) is an irreducible curve germ meeting E in exactly one point (the normalization of A is a disc, the lift to W̃ of the punctured disc extends continuously by properness). The number Ã · E_j (local intersection number of a curve with a compact curve not containing it) is ≥ 0, and > 0 for some j.
- **(RA)** (Grauert; relative ampleness, from memory) Let L be a holomorphic line bundle on W̃ with deg(L|_{E_k}) > 0 for every k. Then, after shrinking W around ŝ_0, some power L^N is generated by its global holomorphic sections on W̃. (L|_E is ample on the projective curve E because its degree on each component is positive; ampleness on the only positive-dimensional fibre gives π-ampleness near E; then Cartan's Theorem A for the coherent sheaf π_*L^N on the Stein space W.)

### 1.2 An elementary lemma
**Lemma M.** Let M be a real symmetric negative definite r×r matrix with M_{kj} ≥ 0 for k ≠ j and connected graph {k ~ j iff M_{kj} > 0}. If Mc = −b with b ∈ R^r, b ≥ 0, b ≠ 0, then c_k > 0 for all k.

*Proof.* Write c = c⁺ − c⁻ with c⁺, c⁻ ≥ 0 of disjoint supports. Then (c⁻)ᵀMc = (c⁻)ᵀMc⁺ − (c⁻)ᵀMc⁻. The first term is ≥ 0 (disjoint supports, off-diagonal entries ≥ 0), and −(c⁻)ᵀMc⁻ > 0 if c⁻ ≠ 0. But (c⁻)ᵀMc = −(c⁻)ᵀb ≤ 0. Hence c⁻ = 0 and c ≥ 0; c ≠ 0 since b ≠ 0. If c_k = 0 for some k, then −b_k = (Mc)_k = Σ_{j≠k} M_{kj}c_j ≥ 0 forces b_k = 0 and c_j = 0 for all neighbours j of k; by connectedness c = 0, a contradiction. ∎

### 1.3 Lemma P (a pole function for a curve that need not be Q-Cartier)
**Lemma P.** Let (Ŝ, ŝ_0) be a normal 2-dimensional germ, W a small Stein representative, C ⊂ W a curve through ŝ_0 (a finite union of irreducible germs at ŝ_0), and A_1, …, A_l irreducible curve germs at ŝ_0 not contained in C. Then, after shrinking W, there is a holomorphic function g on W ∖ C such that for every l′ and every sequence z_n ∈ A_{l′} ∖ {ŝ_0} with z_n → ŝ_0, |g(z_n)| → ∞.

*Proof.*
1. Take π : W̃ → W as in (Res). Let C̃ be the strict transform of C (union of the strict transforms of its branches), and p_{l′} the point where Ã_{l′} meets E (Str).
2. **Mumford pull-back.** Let b_j := C̃ · E_j ≥ 0; b ≠ 0 because C passes through ŝ_0 (Str). Solve Mc* = −b (M invertible by (Neg)). By Lemma M, c*_k > 0 for all k. So π*C := C̃ + Σ_k c*_k E_k is a Q-divisor with π*C · E_j = 0 for all j.
3. **An anti-ample exceptional cycle.** Solve Mz = −(1, …, 1). By Lemma M, z_k > 0 for all k. Choose an integer d ≥ 1 with dz integral and put Z := Σ_k d z_k E_k, so Z · E_j = −d < 0 for all j.
4. **The divisor D.** Choose an integer m ≥ 1 such that m c*_k ∈ Z and m c*_k − d z_k ≥ 1 for all k. Put D := m π*C − Z = m C̃ + Σ_k (m c*_k − d z_k) E_k. It is an effective integral divisor with support exactly C̃ ∪ E, and D · E_j = −Z · E_j = d > 0 for all j.
5. **Sections.** Let L := O_{W̃}(D) and s its canonical section (div s = D). By (RA), after shrinking W, there is N with L^N globally generated; pick a global section σ of L^N with σ(p_{l′}) ≠ 0 for all l′ (a generic linear combination of generators).
6. Put g̃ := σ / s^N. It is holomorphic on W̃ ∖ supp(D) = W̃ ∖ (C̃ ∪ E). Since π maps W̃ ∖ (C̃ ∪ E) biholomorphically onto W ∖ C, g := g̃ ∘ π^{-1} is holomorphic on W ∖ C.
7. **Blow-up along A_{l′}.** Let z_n ∈ A_{l′} ∖ {ŝ_0}, z_n → ŝ_0. Then z̃_n := π^{-1}(z_n) ∈ Ã_{l′} ∖ E converges to p_{l′} ∈ E (Str). In a local trivialization of L^N near p_{l′}, σ(z̃_n) → σ(p_{l′}) ≠ 0, while s^N(z̃_n) → s^N(p_{l′}) = 0, because p_{l′} ∈ E ⊂ supp(D) (every E_k has coefficient ≥ 1 in D). Hence |g(z_n)| = |g̃(z̃_n)| → ∞. ∎

*Remark.* If C is Q-Cartier, one can take g = 1/G with G as in Theorem X. Lemma P is the replacement when it is not: g is allowed zeros (along curves not in C); only its poles are confined to C. That is all a maximum-principle argument needs.

### 1.4 Statement
Setting of Theorem X (R8-1 §3.1): V_0 ⊂ M_g closed, 2-dimensional, totally geodesic; Δ_G a product-type stratum; E a piece of B_0 in Δ_G; Q_0 ∈ E (an interior point of E); 𝓛_0 ⊂ Def(Q_0) the preimage of closure(V_0) near 0; β a local branch of E at Q_0 with a lift β̃ through 0; S an irreducible component of the germ (𝓛_0, 0) containing β̃; ν : Ŝ → S its normalization, ν^{-1}(0) = {ŝ_0}; B̂ := ν^{-1}(S ∩ {∏_e s_e = 0}).

Call an irreducible component of the germ (B̂, ŝ_0) **of type β** if its image under q∘ν (q : Def(Q_0) → M̄_g the chart map) is contained in β, and **foreign** otherwise.

**Theorem X′.** B̂ has no foreign component at ŝ_0. Equivalently: every boundary curve of the sheet S through 0 lies over the coarse branch β of E.

(Compared with Theorem X(b): no Q-factoriality, no Q-Cartier hypothesis, no monomial condition. In R8-1's notation, every C_i is a curve mapping onto a lift aβ̃, a ∈ Aut(Q_0); if aβ̃ = β̃ for all such curves, m = 0.)

### 1.5 Proof
Assume a foreign component C exists. Let A_1, …, A_l be the components of type β (there is at least one: ν^{-1}(β̃) is a curve through ŝ_0).

**Steps 1–4 of Theorem X are used unchanged.** They give (R8-1 §3.2; I re-read them and use exactly their conclusions): a connected relatively compact open set Ω ⊂ 𝔻 containing 0 and a point w*; holomorphic maps D̂_n : Ω → Ŝ ∖ B̂ (lifts of Teichmüller discs D_n ⊂ V_0, which lie in S because their base points do, and avoid B̂ because D_n ⊂ V_0 ⊂ M_g); and a locally uniform limit L̂ : Ω → Ŝ of D̂_n (Montel in an embedding Û ⊂ C^M) with:
- ν∘L̂ is a lift of L|_Ω, where L : 𝔻 → E^ν is the non-constant limit disc (via (Fl), the Teichmüller vertex j moves);
- L̂(w*) = ŝ_0;
- L(Ω) ⊂ the image of a small disc B ⊂ E^ν around the point e_0 over (Q_0, β), with B ∖ {e_0} mapping into β ∖ {Q_0}.

The only place where Theorem X used the function G is Step 5. I replace it.

**Step 5′.**
1. *L̂ near w* lies in the type-β curves.* For w ∈ Ω, q∘ν∘L̂(w) = L(w) ∈ β. So L̂(Ω) ⊂ ν^{-1}(q^{-1}(β)) ∩ Ŝ ⊂ B̂, and near ŝ_0 this set is the union of the type-β components A_1 ∪ … ∪ A_l (a foreign component maps into β only at ŝ_0, being an irreducible germ not contained in q^{-1}β ∩ …; more precisely, its intersection with ν^{-1}q^{-1}(β) is a proper analytic subset of an irreducible curve germ, hence {ŝ_0} near ŝ_0). L̂ is non-constant (ν∘L̂ lifts the non-constant L), so L̂^{-1}(ŝ_0) is discrete in Ω.
2. *Choice of the small disc.* Shrink W (the Stein representative of (Ŝ, ŝ_0)) so that W ∩ C ∩ (A_1 ∪ … ∪ A_l) = {ŝ_0}, and apply Lemma P to (W, C, A_1, …, A_l): g is holomorphic on W ∖ C and |g| → ∞ along each A_{l′} at ŝ_0. Pick a closed disc Δ* ⊂ Ω centred at w* with L̂(Δ*) ⊂ W and L̂^{-1}(ŝ_0) ∩ Δ* = {w*}. Then L̂(Δ* ∖ {w*}) ⊂ (A_1 ∪ … ∪ A_l) ∖ {ŝ_0} ⊂ W ∖ C, and K := L̂(∂Δ*) is a compact subset of W ∖ C.
3. *Uniform bound on the boundary circle.* D̂_n → L̂ uniformly on Δ*. Fix a compact neighbourhood K′ ⊂ W ∖ C of K. For n large, D̂_n(∂Δ*) ⊂ K′ and D̂_n(Δ*) ⊂ W. g is continuous on K′, so max_{∂Δ*} |g∘D̂_n| → max_{∂Δ*} |g∘L̂| =: e^{μ} < ∞.
4. *Maximum principle.* D̂_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, so g∘D̂_n is holomorphic on Δ*. By the maximum principle, |g∘D̂_n(w)| ≤ max_{∂Δ*}|g∘D̂_n| for all w ∈ Δ*.
5. *Passage to the limit.* For w ∈ Δ* ∖ {w*}, L̂(w) ∈ W ∖ C, where g is continuous, so |g(L̂(w))| = lim_n |g(D̂_n(w))| ≤ e^{μ}.
6. *Contradiction.* Take w_k → w*, w_k ≠ w*. Then L̂(w_k) ∈ (A_1 ∪ … ∪ A_l) ∖ {ŝ_0} and L̂(w_k) → ŝ_0; passing to a subsequence they lie on one A_{l′}. By Lemma P, |g(L̂(w_k))| → ∞, contradicting step 5. ∎

**Remarks.**
1. Total geodesy enters exactly as in Theorem X: through Lemma PA, (Fl), (Prop), which produce discs in the interior of the sheet converging to a parametrisation of the whole branch through Q_0. The new point is only that a holomorphic function with poles confined to C (Lemma P) exists for every curve C on a normal surface germ, whereas a holomorphic function with zeros confined to C exists only if C is Q-Cartier. Hurwitz is replaced by the maximum principle.
2. Sanity check (local crossing model of R7-2 §4.2 at t = 0, S smooth): C = {z = 0} is Cartier, g = 1/z, and the argument is the Hurwitz argument of Theorem X.
3. **Consequence for R8-1 §4.3.** Case (Cr2) ("non-Q-Cartier crossings") does not exist: for every product-type piece E and every Q_0 ∈ E, every sheet of closure(V_0) at Q_0 that contains a branch β of E has no boundary curve through Q_0 other than curves over β. In particular two different pieces never meet at an interior point of a product-type piece inside a common sheet, whatever the singularity of the sheet.
4. **Non-product strata (not proved).** R8-1 Remark 2 says Theorem X uses product type only to have the global coordinate f_j on E; one would work on the lifted piece in ∏_w M_w. The replacement Step 5′ is local in Ŝ and does not care about the stratum type. So Theorem X′ holds for non-product G as soon as Steps 1–4 of Theorem X do. I have not checked those steps for non-product G.

---

## 2. Lemma SS: interior paths stay in one sheet

**Lemma SS.** Assume (Sm). Let U be an open subset of M̄_g, and let X_1, X_2, … be the (global) irreducible components of the analytic set closure(V_0) ∩ U in U. Then V_0 ∩ U is the disjoint union of the sets V_0 ∩ X_k, each of which is open and closed in V_0 ∩ U. Hence every path γ : [a,b] → V_0 ∩ U lies in a single X_k.

*Proof.*
1. Since V_0 is closed in M_g, closure(V_0) ∩ M_g = V_0. So near a point z ∈ V_0 ∩ U the analytic set closure(V_0) coincides with V_0.
2. Each X_k is pure 2-dimensional (closure(V_0) is the closure of the 2-dimensional V_0).
3. Suppose z ∈ V_0 ∩ X_k ∩ X_l with k ≠ l. The germs (X_k, z), (X_l, z) are 2-dimensional and contained in (V_0, z), which is irreducible by (Sm) and 2-dimensional. So (X_k, z) = (V_0, z) = (X_l, z). Then X_k ∩ X_l contains a non-empty open subset of the irreducible analytic set X_k, hence X_k ⊂ X_l (identity theorem for irreducible analytic sets), and so X_k = X_l, a contradiction.
4. Each V_0 ∩ X_k is closed in V_0 ∩ U. The family {X_k} is locally finite in U, so the union of all V_0 ∩ X_l, l ≠ k, is closed too. Its complement in V_0 ∩ U is V_0 ∩ X_k (by 3), which is therefore open.
5. A path is connected, so it lies in one of these open and closed pieces. ∎

**Corollary SS′ (two branches of one transition lie in one sheet at Q_0).** Let Q_0 ∈ B_0 and let b_1, b_2 be branches of B_0 at Q_0. Fix generic points z_1 ∈ b_1, z_2 ∈ b_2 near Q_0, and a small neighbourhood U of Q_0 containing them. Suppose that for every ρ > 0 there is a path γ_ρ : [a,b] → V_0 ∩ U with d(γ_ρ(a), z_1) < ρ and d(γ_ρ(b), z_2) < ρ. (This is supplied by the track data (TD_J) at a junction and (TD_Q) at the end point of Prop K, R8-5 §1 (C2) and §5; they are readings of Proposition K, which is itself "proved modulo routine marking details".) Then:
- (a) there is a global irreducible component X of closure(V_0) ∩ U containing b_1 ∩ U and b_2 ∩ U;
- (b) for any lifts b̃_2 ⊂ Def(Q_0) of b_2 through 0 there is a lift b̃_1 of b_1 through 0 such that b̃_1 and b̃_2 lie in a common irreducible component of the germ at 0 of the preimage of closure(V_0).

*Proof.*
- (a) Only finitely many X_k meet a compact neighbourhood of {z_1, z_2}. By Lemma SS each γ_ρ lies in one X_{k(ρ)}; pass to a sequence ρ_n → 0 with k(ρ_n) = k fixed. Since X_k is closed in U, z_1, z_2 ∈ X_k. X_k ∩ B_0 is an analytic subset of B_0; near z_1 it is pure 1-dimensional (locally, in an orbifold chart, it is the zero set in the 2-dimensional preimage of X_k of the single function ∏ s_e, which is not identically zero on any component; Krull), and B_0 near the generic point z_1 is the smooth curve b_1. So X_k contains the germ of b_1 at z_1, hence the irreducible branch b_1 ∩ U (identity theorem on the normalization of b_1). Same for b_2.
- (b) Shrink U so that U = q(B), B ⊂ Def(Q_0) a small Aut(Q_0)-invariant ball, and so that the global irreducible components of q^{-1}(closure V_0) ∩ B are the germ components at 0 (for a small enough ball an irreducible germ has an irreducible representative; standard, from memory). q^{-1}(X) is a union of such components, and Aut(Q_0) permutes the components of q^{-1}(X) transitively, because X is irreducible and q is the quotient by the finite group Aut(Q_0) (standard). Each lift of a branch contained in X is an irreducible curve contained in q^{-1}(X), hence in one component. Let b̃_2 ⊂ S_2 and pick any lift b̃_1^0 ⊂ S_1 of b_1. Write S_2 = cS_1 with c ∈ Aut(Q_0). Then b̃_1 := c b̃_1^0 ⊂ S_2 is a lift of b_1. ∎

**Remark.** (b) gives a sheet containing *some* lift of b_1 together with the given lift of b_2, not necessarily the lift along which the track arrived. For the coarse statements below this is enough.

---

## 3. Lemma PT: product-type strata carry no twins of positive dimension

**Lemma PT.** Let Δ_G be of product type, Q ∈ Δ_G, and α ∈ Aut(Q). Let x be a vertex of G with dim M_{g_x,n_x} > 0. Then α maps the component Q_x to itself. More generally, the partial-normalization map Π : {s_e = 0 ∀e} ⊂ Def(Q) → ∏_w M_w (comp_y ↦ y-th factor, for a fixed identification G_Q ≅ G) satisfies ξ_G∘Π = q and is independent of the identification; so comp_x = pr_x∘Π on the stratum locus of Def(Q), and comp_x(αp) ≅ comp_x(p) for all α ∈ Aut(Q).

*Proof.*
1. α induces σ ∈ Aut(G), which acts on ∏_w M_w by permuting the factors and relabelling marked points, and ξ_G∘σ = ξ_G on all of ∏_w M_w (gluing does not see the order of the factors).
2. ξ_G is injective (product type), so σ acts as the identity on ∏_w M_w.
3. If σ(x) = x′ ≠ x, then for every z ∈ ∏_w M_w the coordinate z_{x′} would be a fixed relabelling of z_x. Since dim M_x > 0, choose z with z_x arbitrary and z_{x′} different from every relabelling of z_x (possible: the coordinates are independent and M_{x′} ≅ M_x up to relabelling is positive-dimensional). Contradiction. So σ(x) = x.
4. Two identifications G_Q ≅ G differ by some σ ∈ Aut(G); by step 2, Π does not change. By (K3), comp_x(αp) ≅ comp_{α^{-1}x}(p) = comp_x(p). ∎

**Consequences.**
- At a junction J or end point Q_0 of Prop K's chain whose stratum is of product type, (NT) holds for the tracked chart vertex (it has type (g_i,n_i) and dim M_{g_i,n_i} > 0). So no twin jump can occur there (R7-3 Theorem A, R8-8 Theorem 1 with (NT_m)).
- R8-6 type (T) ("same-branch twin") cannot occur at a point of a product-type stratum.
- Hence **every twin problem of the chain lives at points of non-product strata.** (This was used for Δ_Γ in R8-2 Step 4; here it is recorded for all strata.)

---


### Gap A (verbatim §2.1 of an audit)
## 2. Audit of the chain (MS10 ⇒ MS8 ⇒ goal)

Notation. For a stable graph G, Δ_G ≅ (∏_w M_w)/Aut(G) (standard, cited from memory; Aut(G) acts by permuting factors and relabelling marked points), with quotient map ξ = ξ_G. For a piece D ⊂ Δ_G at t = 0, ξ^{-1}(D) = E_1 ∪ … ∪ E_r, irreducible curves permuted transitively by Aut(G). κ(D) is the component of ℬ_G containing H(D × Δ) (round9_q7 Lemma T). A *lifted family component* of D is an irreducible component 𝒲̃ of (ξ × id)^{-1}(κ(D)) ⊂ ∏_w M_w × Δ. Persistence of a label is a property of a lifted family component *together with the labelling of ∏_w M_w* (round9_q7 Lemma S(c)). It is not a property of the coarse κ(D). For product-type G, ξ is injective, so the two notions coincide. For non-product G they do not, and the two gaps below come from this.

### 2.1 Gap A: sheet switching in the middle of a travel interval

**The step concerned.** Chain step (b): "persistence passes along D^{m+1} to β̃_{m+1}, because persistence is a property of the whole component κ(D^{m+1}) (Lemma S(c)) and the chart vertex is c_{m+1} on both ends (K_w Step 3)."

**What is missing.** Along a travel interval of the walk chain (round9_q4 §2.3), the track stays near K_D, and its marking gives a continuous lift to ∏_w M̄_w near ξ^{-1}(D). The tracked subsurface Σ_i corresponds to one fixed factor c of ∏_w M_w along the whole interval, by continuity. But the lift can pass from one lifted curve E_k to another one, σE_k (σ ∈ Aut(G)), at a point z ∈ E_k ∩ σE_k. Then:
- before z, the track's label is c on E_k;
- after z, the label is still the factor c, but now on σE_k. In terms of E_k, the factor c of σE_k is the factor σ^{-1}c of E_k.

So the label the track follows after z is the twin σ^{-1}c, not c. The special set Σ of the walk chain consists of junctions, singular points of B_0, punctures, and points where a non-constant vertex has value [Y_0]. It does **not** contain such crossing points in general.

**Local model showing that such a point need not be in Σ (proved, local).** Take G non-product with σ ∈ Aut(G) exchanging two vertices c, c′ = σc of type (g_i, n_i), and exchanging two further vertices m, m′ of the same type. Assume near the point z the other factors are σ-fixed. Use local coordinates a on M_m and b on M_{m′} centred at z, with σ(a, b) = (b, a). Let
- E_k := {z_c = z_{c′} = Y_0, (a, b) = (s, 2s), other coordinates fixed}, so on E_k both c and c′ are constant with value Y_0, and m, m′ move;
- σE_k = {z_c = z_{c′} = Y_0, (a, b) = (2s, s), …}.

They meet at z (s = 0), which is fixed by σ. In the quotient coordinates (u, v) = (a + b, ab), E_k maps to u = 3s, v = 2s² = 2u²/9, a smooth curve. So, if Stab(z) = ⟨σ⟩, D = ξ(E_k) is **smooth** at ξ(z). ξ(z) is not a junction, not a puncture, not singular on B_0, and the non-constant vertices m, m′ have value z_m = z_{m′} there, which need not be ≅ Y_0. So ξ(z) ∉ Σ.

At the family level, let 𝒲̃ ⊃ E_k × {0} be the lifted family component on which c is persistent. Then σ𝒲̃ ⊃ σE_k × {0}, and on σ𝒲̃ the factor c carries the value function of c′ on 𝒲̃. If c′ is a "persistent twin" with [φ_{c′}] ≢ [Y] (round9_q3 §5(b)), the track's label is no longer persistent after z. Nothing in the chain's step (b) detects this.

**Repair (proved, given the walk-chain inputs).** For each piece D let R(D) be the set of P ∈ D such that, near ξ^{-1}(P), the set ξ^{-1}(D) is not a disjoint union of smooth arcs each mapped homeomorphically onto a neighbourhood of P in D.
- R(D) is finite. It consists of images of singular points of the compact curve ξ̄^{-1}(closure D) ⊂ ∏ M̄_w, and of ramification points of the finite maps from the normalisations of its components to the normalisation of closure(D). Both sets are finite.
- Replace Σ by Σ ∪ ⋃_D R(D) in round9_q4 §2.3, before choosing r. Everything there goes through unchanged: Σ is still finite.
- Then, over a neighbourhood of K_D, ξ^{-1}(D) is a disjoint union of compact arcs at positive mutual distance. By continuity, the track's lift stays near one arc of one lifted curve E for the whole travel interval, and its label is a fixed factor c. (This is a "routine marking detail" of the same kind as K_w Step 3. I use it in the same way.)
- The new transition points P ∈ R(D) are interior points of D. The track arrives along a lift β̃ and leaves along a lift b̃ of a branch of D at P, possibly of the same coarse branch, joined inside the chart (K_w Steps 3 and 5 apply verbatim). If the two lifts lie on different lifted curves, ξ is not injective, so Δ_G is non-product. Then this is exactly an MS10 configuration. MS10 explicitly allows "lifts of the same coarse branch", so it already covers these points. If both lifts lie on the same E_k at a ramification point, the label is unchanged and nothing is needed.

So Gap A is a gap in the walk-chain bookkeeping. It does not change the missing statement, but **the list of points where MS10 is invoked must include R(D) for every non-product piece D of the chain.**


### Chain check (verbatim; §§1, 2.4 and 3 concern Part I)
# round11_q9: check of chain steps 2(b)–2(d) (entries 99, 100), MS11 ⇒ MS8

**Plan/status.** I checked every item of the brief against the spliced proofs:
- round10_q1 §2 and §4;
- round10_q10 §6.3;
- round10_q3 §2;
- round9_q7 Lemmas S, J and Cor. J′;
- round9_q3 Lemma PT, Lemma P, Theorem X′.

**Verdict: correct after named repairs.** With MS11 worded as it is, the chain has a gap at two places: step 2(c), the transfer along a travel interval, and step 2(d), the MOV case of the endpoint. Both come from Lemma B1(a), which is false as stated. The repair is to replace "transport sheet of c̃" by "c̃-sheet" (defined in §2) in MS11 and in the induction claim; the repaired statement is called MS11♭ below. With that change every step 2(b)–(d) goes through. Everything else checks, modulo the inherited cited inputs and one inherited "routine marking detail" (§4).

Readings throughout: (R1), (R2) with H_0 = id, (Rig), and the notation of the task file. [Z] is the class in 𝔐 = M_{g_i,n_i}/S_{n_i}.

---

## 1. Item 1: Lemma S̃′ ⇒ Theorem X*_all ⇒ Cor. IMOV_all (entry 99). Correct.

### 1.1 Lemma S̃′ supplies exactly the hypothesis of Theorem X*_all
Theorem X*_all needs three things:
- a point Q_0 lying in the stratum of a piece E;
- a lift β̃ ⊂ L (the stratum locus) of a branch β of E;
- a sheet S, i.e. an irreducible component of the germ at 0 of q^{-1}(closure V_0), with S ⊃ β̃.

Its conclusion is S ∩ {∏ s_e = 0} = β̃ near 0.

Lemma S̃′ gives a component X̃_l of q^{-1}(closure V_0) ∩ B̃ with X̃_l ⊃ β̃ ∪ β̃′. Because B̃(J,3r) is taken to be a Milnor ball, X̃_l represents a germ component, i.e. a sheet.

I re-checked the proof of S̃′.
- **Step 1.** The ray g_s(X_n,q_n) lies on the Teichmüller disc F of the generating pair. The rotation by e^{-2iθ_n} from Lemma NH does not change the disc. F lies over V_0 by total geodesy, in the form already used in Lemma PA Step 5. (T4) is **not** needed, so S̃′ really replaces Lemma 1SS.
- **Minor repair in Step 1.** R should be the component of F^{-1}(gU ∩ (preimage of B̃(J,3r))) that contains the excursion arc, not the component of F^{-1}(gU). Otherwise f(R) need not lie in B̃, which is where the X̃_l live. The excursion arc lies in B(J,2r), so this changes nothing else.
- **Step 2.** The sets f^{-1}(X̃_l) are analytic subsets of the connected Riemann surface R and cover it, so one of them is R. Correct.
- **Step 3.** z̃^1 lies in X̃_l because X̃_l is closed in B̃. X̃_l ∩ {∏ s_e = 0} is pure 1-dimensional at z̃^1: no local component of X̃_l at z̃^1 can lie in the 1-dimensional set q^{-1}(B_0). Near z̃^1, q^{-1}(B_0) = β̃, because distinct lifted branches meet only at 0. So X̃_l contains a neighbourhood of z̃^1 in β̃, hence all of β̃, since β̃ ∩ B̃ is irreducible in a Milnor ball. Correct.

### 1.2 Cor. IMOV_all(a) at every transition in the stratum of an adjacent piece
- **J in the stratum of D (entering piece).** Apply X*_all to (D, coarse branch of β̃, S = X̃_l). Then β̃′ ⊂ S ∩ {∏ s_e = 0} = β̃ near 0. Both are irreducible representatives in B̃, so β̃′ = β̃.
- **J in the stratum of D′ (leaving piece).** Symmetric: apply X*_all to D′.
- **The label.** The label does not change, independently of S̃′. By (R-b), Σ_x = Σ_i = Σ_{x′}, so x′ = x.
- **Consequences.** The coarse branches coincide, so the transport families Ñ_β̃ and Ñ_β̃′ coincide, and so do their sheets. Persistence passes unchanged.
- **R(D)-points.** These are interior points of D. Entering and leaving lifts are lifts of branches of D; in the Gap A model they lie over E_k and σE_k. The same argument gives β̃′ = β̃. So the walk never switches lifted curve at an R(D)-point, and these transitions are trivial. Correct.
- **Endpoint.** S̃′ also holds with z̃^2 = z̃^∞ ∈ b̃ ∖ 0. If Q_0 were in the stratum of D^k or of E_b, then b̃ = β̃, so x would be intact and ≡ Y_0 along b̃, contradicting MERGE/MOV. So Q_0 satisfies (P). A genuine transition (β̃′ ≠ β̃) also satisfies (P), by contraposition of (a).
- **Small addition.** A puncture transition with β̃′_m = β̃_m needs nothing. MS11 requires β̃ ≠ b̃, so it is invoked only at transitions with β̃′_m ≠ β̃_m. The chain should say this explicitly.

### 1.3 Theorem X*_all where it departs from round9_q4
- **(i) The lift L̂ to ∏_w M_w.**
  - By Wolpert and Abikoff, the node curves of every limit L(w), under the disc's marking, are exactly those of P_1.
  - The vertex subsurfaces are invariant under the twist group Tw, so the labelling does not depend on twisting.
  - The labels are fixed once, by the chart Def(Q_0) at X̃_n near P̃_1. This is consistent in n, because all the lifts X̃_n converge to P̃_1 in one chart.
  - Locally, L̂ = Π_Z ∘ (limit of the chart lifts), so it is holomorphic.
  - The step L̂(𝔻) ⊂ Ê uses that Π(P̃_1) lies on Ê only.
  - Step 3 is correct as written: properness of L̄ is obtained through pr_j ∘ L̄, with no properness of pr_j on Ê needed, and Γ acts on the finite set Λ.
  - Step 4's new point is that the chart limit L̃ lands in the **specific** lift β̃, not only in ⋃_a aβ̃. It is proved correctly: the sets aβ̃ ∖ 0 are pairwise disjoint and closed in B ∖ 0, Ω minus a discrete set is connected, and L̃(0) = P̃_1.
  - Verified, modulo the cited T̄_g ↔ Def chart description.
- **(ii) The homological step.** The corrected sign argument is plausible. If L′ meets C′ only at the isolated point w*, then Z_n · C′ = −μ ≤ 0, while Σ k_j F_j · C′ > 0. But the text of round9_q4 §1.4, with (Int) and (Pos), is not spliced into my brief, so I cannot check it line by line.
- **It is not needed.** The maximum-principle route of round9_q3 (Step 5′ with Lemma P) proves X*_all directly from Steps 1–4. I checked this as follows.
  - Call a component of B̂ at ŝ_0 *of type β̃* if it maps onto β̃. These are the Ê_l. Let C be the union of all the other components; this includes components over aβ̃ ≠ β̃.
  - By Step 4, L̂_S(Ω) ⊂ ν^{-1}(β̃). The germ of ν^{-1}(β̃) at ŝ_0 is ⋃_l Ê_l, because ν is finite and β̃ is irreducible. A component over aβ̃ meets ν^{-1}(β̃) only in ν^{-1}(aβ̃ ∩ β̃) = {ŝ_0}.
  - Lemma P applies to (W, C, Ê_1, …, Ê_r). I re-checked its proof: Lemma M; the Mumford pull-back; the anti-ample cycle Z; D = mπ*C − Z effective with support C̃ ∪ E and D·E_j > 0; (RA); g = σ/s^N. It is correct given (Res), (Neg), (RA).
  - Steps 5′.2–5′.6 then go through verbatim: D̂_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, the maximum principle bounds |g ∘ D̂_n|, and |g| → ∞ along Ê_l at ŝ_0 gives the contradiction.
  - **So X*_all holds in every stratum, with or without the homological correction.**

---

## 2. Item 2: Lemma B1 is false as stated in (a) and (b), and the repair

### 2.1 Where the proof of B1(a) fails
The proof of B1(a) says: "So Ñ^1 meets {t = 0}, **where Ñ ∩ {t = 0} = b̃ ∖ 0**." Nothing justifies the bold claim.
- Ñ = Ñ_b̃ is the connected component of q^{-1}(N) containing b̃ ∖ 0.
- Its t = 0 slice lies in q^{-1}(b ∖ Q) = ⋃_a (ab̃ ∖ 0).
- Ñ can contain a second lift ab̃ ≠ b̃, joined to b̃ ∖ 0 through points with t ≠ 0.
- Then Ñ_{ab̃} = Ñ_b̃, and Ñ can have an irreducible component whose t = 0 slice lies in ab̃ and misses b̃ ∖ 0.
- The proof of (b) uses (a) ("every global component of Ñ contains such a germ"), so (b) fails too.

### 2.2 Local model 1 (chart-level, consistent with (R2); it refutes B1(a), (b) and the MOV endpoint step under MS11's weak notion)
**Coordinates and branches.**
- Def(Q) has coordinates (s_1, s_2, p, p′, u, …). The labels x and x′ = ax have the same type, with moduli coordinates p and p′; Y_0 ↔ 0, and Y_t ↔ t (to first order).
- a ∈ Aut(Q) acts by p ↔ p′ and u ↦ −u, and fixes s_1, s_2.
- Put b̃ := {s_1 = 0, p = s_2², p′ = 0, u = s_2} and ab̃ = {s_1 = 0, p′ = s_2², p = 0, u = −s_2}.
- These are distinct lifts with the same pattern {e_1}. Q is a puncture: s_2 ≢ 0.
- Along b̃, x is intact and **moving** (MOV), and x′ is constant ≅ Y_0.

**Transport.**
- A := {s_1 = 0, p = t + s_2(s_2+t), p′ = t, u = s_2 + t, s_2 ≠ 0}, and aA := {s_1 = 0, p′ = t + s_2(s_2+t), p = t, u = −(s_2+t), s_2 ≠ 0}.
- A ∩ {t = 0} = b̃ ∖ 0 and aA ∩ {t = 0} = ab̃ ∖ 0.
- For t ≠ 0, A and aA meet at the a-fixed point P_t = (s_2 = −t, p = p′ = t, u = 0), which has s_2 ≠ 0.

**Coarse smoothness.**
- q is injective on A_t, because A_t ∩ aA_t = {P_t} and P_t is a-fixed.
- s_2 is an a-invariant coordinate that restricts to a coordinate on A_t. So N_t := q(A_t) is a smooth coarse curve, a graph over s_2.
- H_t(q(b̃(s_2))) := q(A_t(s_2)) is a smooth trivialisation of N = ⋃_t N_t. The lift of Q_t is s_2 = 0, i.e. p = p′ = t, u = ±t. So |Aut(Q_t)| < |Aut(Q)|, which matches the known necessary conditions.

**Conclusions in the model.**
- Ñ_b̃ = A ∪ aA. It is connected (through P_t) and has two irreducible components, one of which has slice ab̃ ∖ 0. The pointwise stabiliser of b̃ does not contain a. So **(a) and (b) of B1 fail.**
- x is Y-persistent on aA: F_x = p = t ↔ Y_t, and x is intact. So **x is Y-persistent on a transport sheet of b̃ in MS11's sense, while x MOVES along b̃.**
- The model is chart-level only. It satisfies every chart-checkable constraint I know of, the same way the Gap B model of round10_q3 does. The point is that the step "B1(a) ⇒ the endpoint contradiction" is not a valid inference.

### 2.3 The repaired lemma (B1♭), proved
**Definition.** Let c̃ be a lifted branch. A *c̃-sheet* is an irreducible component of closure(Ñ_c̃) in B × Δ_ε whose t = 0 slice contains a non-empty open subset of c̃ ∖ 0.

**Lemma B1♭.** Let Ñ = Ñ_b̃.
- (a′) Every irreducible component Ñ^1 of Ñ maps onto N. Its t = 0 slice is a non-empty union of open subsets of finitely many lifts ab̃ ∖ 0, each with ab̃ ⊂ closure(Ñ) and with aS_b̃ = S_b̃.
- (a″) b̃-sheets exist. For generic p̃ ∈ b̃ ∖ 0 near 0, every germ component of q^{-1}(N) at (p̃, 0) lies in a b̃-sheet, and every b̃-sheet contains such a germ.
- (b′) The pointwise stabiliser Stab(b̃) permutes the b̃-sheets transitively.
- (c), (d) as in round10_q3. In (d), at product-type points every a ∈ Aut(Q) fixes x (Lemma PT). So persistence of x on an ab̃-sheet T is equivalent to persistence of a^{-1}x = x on the b̃-sheet a^{-1}T, and the weak and strong notions agree there.

*Proof.*
- **(a′).** Ñ^1 maps onto N by Remmert: N is a connected topological 4-manifold, hence an irreducible analytic set, and q is finite on Ñ^1. So t is non-constant on Ñ^1, and by Krull its slice is pure 1-dimensional. The slice lies in ⋃_a ab̃ ∖ 0, and these sets are pairwise disjoint and closed in B ∖ 0. The pattern is constant on the connected set Ñ (R7-4 Lemma 2(a)), which gives aS_b̃ = S_b̃.
- **(a″).** Near (q(p̃), 0) the set N is the whole of ℬ. Near p̃, q^{-1}(b) = b̃. So every germ component of q^{-1}(N) at (p̃, 0) has its t = 0 slice in b̃, lies in Ñ (q^{-1}(N) is locally connected at (p̃,0) ∈ Ñ), and lies in one global component, which is then a b̃-sheet. Conversely, a b̃-sheet contains a generic point (p̃, 0) of its slice in b̃ ∖ 0, and with it a germ component there.
- **(b′).** This is the original proof of (b), restricted to b̃-sheets, which is where it is valid. For generic p̃, Stab(p̃) equals the pointwise stabiliser of b̃ and permutes the germ components at (p̃, 0) transitively. Each element of it maps Ñ to itself. ∎

### 2.4 Gap A repair (R(D) added to Σ): correct
- R(D) is finite. It consists of the singular points of ξ̄^{-1}(closure D), which include the crossings E_k ∩ σE_k, together with the images of ramification points of the normalisation maps.
- With R(D) ⊂ Σ chosen before r, ξ^{-1}(K_D) is a disjoint union of compact pieces at positive mutual distance, each mapped by a covering onto K_D. So the marking lift stays on one lifted curve E with a fixed factor c.
- The new transitions are trivial by §1.2.
- The step "marking lift continuous along travel, label = c" is a routine marking detail of the K_w kind. I accept it as inherited; I did not re-derive it.

### 2.5 Base step: correct, and gives the strong notion
- Δ_Γ is of product type, so Aut(Γ) acts trivially on ∏ M_w (Lemma PT, steps 1–2) and Π_S is canonical.
- At every (p,t) ∈ Ñ_{β̃_1}, q(p) ∈ H_t(β_1 ∖ J_1) ⊂ ∂V_t (R2), and the pattern is constant. So x_1 = {i} is intact and F_{x_1}(p) = pr_i Π_S(p) = Y_t.
- Closedness passes this to closure(Ñ). So x_1 is persistent on **every** sheet, in particular on β̃_1-sheets. (B1(d) is not even needed.)

### 2.6 Product-type puncture junction (Lemma J / Cor. J′): correct; weak input suffices, strong output
**Input.**
- Let T be any sheet of Ñ_{β̃_m} on which x is persistent; it may be an aβ̃-sheet.
- T ⊂ q^{-1}(closure H((β∖J)×Δ_ε)), and by Lemma T(c) this lies in q^{-1}(ℬ^{(k(β))}) near (0,0). Also (0,0) ∈ T, since lifts of J_t accumulate there.
- So any germ component of T at (0,0) is a germ component 𝒲̃^a of q^{-1}(ℬ^{(k(β))}) with persistent vertex x.
- Lemma J never uses β̃ ⊂ 𝒲̃^a. Its step 1 uses only that Aut(Q) permutes the preimage germ components transitively, and step 2 uses only persistence on 𝒲̃^a.

**Conclusion.**
- By Lemma PT, x̂ = x.
- x = x_m is intact and constant ≅ Y_0 along b̃ = β̃′_m: this is the track's c′ = {x_m}. So (J1) and (J3) are excluded (Cor. J′), and (J2) holds: x is persistent on a germ component 𝒲̃″ ⊃ b̃ at (0,0).

**Strong output.**
- Take p̃ ∈ b̃ ∖ 0 generic and close enough to 0 that a representative of 𝒲̃″ is defined near (p̃, 0).
- Near (q(p̃), 0), ℬ = N, so the germ of 𝒲̃″ at (p̃,0) is a union of germ components of q^{-1}(N) at (p̃,0). By B1♭(a″) these lie in b̃-sheets.
- The persistence set is analytic: intactness is the pattern, and {[F_x] = [Y_t]} is analytic because [Y] is holomorphic. Persistence holds on an open subset of the irreducible component, hence on all of it (identity principle), and on its closure by continuity.
- So x is persistent on a **β̃′_m-sheet**.

I also checked Lemma J step 5 (Lemma S(b), continuity of F_x on L_x at q_t) and step 7. Both use (Rig) through Lemma S(a), and (Rig) is part of MS8's setting.

### 2.7 Transfer along a travel interval: correct for c̃-sheets, unsupported for MS11's notion
**Proof with the strong notion.**
- Let Ñ′^1 be a component whose closure is a β̃′_m-sheet with x_m ↔ c persistent.
- Π_S(Ñ′^1) is irreducible and 2-dimensional, inside (ξ×id)^{-1}(κ(D)), so it lies in one global component 𝒲̃.
- By B1♭(a′), and **because the sheet is a β̃′_m-sheet**, 𝒲̃_0 contains an open arc of Π_S(β̃′_m), which lies on the track's E. Hence 𝒲̃_0 ⊃ E.
- At J_{m+1}, take p̃ ∈ β̃_{m+1} ∖ 0 generic, with z = Π(p̃) ∈ E under the track's identification. Near p̃, Π is a finite open map from the stratum locus of Def(C_p̃), and q^{-1}(ℬ_G) ∩ L = (Π×id)^{-1}((ξ×id)^{-1}ℬ_G). Near (q(p̃),0), ℬ_G = κ(D), a 4-manifold.
- So the germ components of q^{-1}(N″) at (p̃,0) map onto the germ components at (z,0), and (z,0) ∈ 𝒲̃. Some germ component maps into 𝒲̃. By B1♭(a″) it lies in a β̃_{m+1}-sheet Ñ″^1, and by the identity principle Π(Ñ″^1) ⊂ 𝒲̃.
- c is constant (c ∉ M), so Lemma S(c) applies: persistence of c holds on all of 𝒲̃. Hence x_{m+1} ↔ c is persistent on Ñ″^1, intact by the constant pattern, and persistent on its closure.
- The output is again a **β̃_{m+1}-sheet**.

**Why the weak notion fails.** If the persistent sheet T at J_m is only an aβ̃′_m-sheet with ax_m ≠ x_m, then 𝒲̃ ⊃ Π(T) has its slice on āE, not on E. Equivalently, the persistent label on β̃′_m-sheets is a^{-1}x_m, by (K3), and the transfer carries the factor of the twin a^{-1}x_m. At J_{m+1} the track label is x_{m+1} ↔ c, so MS11's hypothesis there is not supplied.

So step 2(c) is **not** established from MS11 as worded. It is established from MS11♭.

### 2.8 Endpoint 2(d)
- **Product type: correct** with the weak input. Lemma PT makes Q_0 aligned, and Lemma J (J1) applies.
  - MERGE: [x] ≠ {x}.
  - Puncture-MOV: {x} ∈ M(κ(E_b)), using U_b ≠ ∅, (P) and step 7.
  - In both cases Y_t ∈ F on an open set, and (P) with PR-A gives that Y is constant: a contradiction.
- **Non-product, MERGE: correct even with MS11 as worded.** Let T be any sheet of Ñ_b̃ on which x is persistent. Then x is intact on T. The pattern is constant (= S_b̃) on the connected set Ñ_b̃, and T ∩ Ñ_b̃ ≠ ∅. So every edge at x lies in S_b̃, which contradicts MERGE.
- **Non-product, MOV: gap with MS11 as worded.** Local model 1 (§2.2) satisfies "x persistent on a transport sheet of b̃" through the ab̃-sheet aA, while x moves along b̃.
  - The chain's sentence "by Lemma B1(a), T ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0" is false for such T. One only gets F_{a^{-1}x} ≡ Y_0 along b̃, which is the endpoint twin and no contradiction.
  - With MS11♭ the step is correct. T is a b̃-sheet, so its slice contains an open subset of b̃ ∖ 0 on which x is intact and F_x ≅ Y_0. The pattern is constant on b̃ ∖ 0, and F_x is holomorphic on L_x ⊃ b̃. The identity theorem in 𝔐 along the normalisation of b̃ gives [F_x] ≡ [Y_0] along b̃.
  - This contradicts MOV. Here MOV means d(F_x(z̃^∞), Y_0) = η with 0 < 2η < min d(σY_0, Y_0) by (b1), so [F_x(z̃^∞)] ≠ [Y_0].

---

## 3. Item 3: interaction with the repairs (R-a)–(R-d): nothing needs a common sequence
- Each use of S̃′ in 2(a)/(b) concerns one transition.
  - Its witnessing sequence comes from the n′ of that transition's recurrent type τ.
  - The data are normalised by a global a ∈ Aut(J). Since a permutes components, a^{-1}X̃_l contains walk n's own pair (β̃, β̃′).
- Theorem X*_all is a pure t = 0 statement and involves no walks.
- The induction 2(c) uses:
  - the per-transition sheet data;
  - the labels along travel intervals of the **single fixed walk n ≥ N**: canonical lifts for that n, Σ_i = Σ_{x_m}, and the marking lift on E;
  - global analytic objects (𝒲̃, κ(D)).
  None of these refers to other walks.
- The endpoint uses the n′ of type τ_end only to obtain b̃ and the MERGE/MOV dichotomy.
- Shrinking ε finitely many times is harmless. A c̃-sheet for the old ε contains the germ at a generic (p̃,0), hence a c̃-sheet for the new ε, and persistence passes by the identity principle.

So no common subsequence is needed. This confirms round10_q10's remark.

---

## 4. Item 4: other points in 2(a)–(d)
- **Puncture transitions with β̃′_m = β̃_m** are trivial and must be excluded from the MS11 invocations, since MS11 requires distinct branches. This is a wording point only.
- **Inherited, not re-derived:**
  - the marking-continuity detail along travel intervals (round10_q3 §2.1, "routine");
  - the cited inputs: Lemma PA, Lemma NH, (Fl), (Prop), Kerckhoff, Maskit, the T̄_g/Def chart description, Wolpert/Abikoff, (Res)/(Neg)/(RA), Krull, Remmert, Milnor conic structure.
- **(T4)** is not needed by the chain: S̃′ replaces Lemma 1SS.
- **The step "Goal ⇐ MS8 + (Rig) + entry 19"** is unaffected.

---

## 5. Corrected missing statement and corrected chain
**MS11♭ (replaces MS11; same setting and data, including "Y non-constant", (P) and (S)).**
- *Hypothesis:* x is Y-persistent on some **β̃-sheet**, i.e. a component of closure(Ñ_β̃) whose t = 0 slice contains a non-empty open subset of β̃ ∖ 0.
- *Conclusion:* x is Y-persistent on some **b̃-sheet**.

**Chain with MS11♭.** Induction claim: x_m is Y-persistent on some β̃_m-sheet.
- Base: §2.5.
- Interior transitions and R(D)-points: §1.2.
- Product-type puncture junctions: §2.6, which outputs a β̃′_m-sheet.
- Non-product puncture junctions with β̃′_m ≠ β̃_m: MS11♭ (§5).
- Transfer: §2.7.
- Endpoint: §2.8.

So **MS11♭ + entries 19, 24, 84–87, 97–100 (with B1 replaced by B1♭) ⇒ MS8**, and MS8 + (Rig) ⇒ the goal.

**Relation between MS11 and MS11♭.** Neither formally implies the other: MS11♭ has a stronger hypothesis and a stronger conclusion. MS11 alone does not suffice, by §§2.7–2.8 and model 1. MS11♭ is still vacuous whenever the problem's claim holds. Its failure configurations are the same twin configurations as before: an a ∈ Aut(Q) moving x, together with a stabiliser jump of the transported branch at t ≠ 0, as in model 1.

---

## 6. Summary
**Proved / checked:**
- Lemma S̃′ (with the minor repair to R) gives exactly the sheet hypothesis of Theorem X*_all, without (T4).
- Theorem X*_all holds in every stratum. Its new lifting step is checked. The homological correction is plausible but not checkable from the brief, and it is superseded by the Lemma P / maximum-principle route, which I verified for type-β̃ components.
- Cor. IMOV_all(a)–(c) is correct, including at R(D)-points and at the endpoint. So (P) holds wherever MS11 is invoked.
- The Gap A repair, the base step, the product-type junction step (Lemma J / Cor. J′, with weak input and strong output), the product-type endpoint and the non-product MERGE endpoint are correct.
- No common witnessing sequence is needed.

**Found false:**
- Lemma B1(a) and (b) of round10_q3, as stated. Explicit chart-level model in §2.2.
- Corrected version: B1♭ (§2.3), proved.

**Gap at named steps (with MS11 as worded):**
- 2(c), the transfer along a travel interval;
- 2(d), the non-product MOV endpoint.

Both are closed by replacing "transport sheet" by "c̃-sheet", i.e. MS11 by MS11♭.

**Verdict:** the chain proves MS8 from MS11♭ (with entries 19, 24, 84–87, 97–100, B1 replaced by B1♭), modulo the inherited cited inputs and marking details. It does **not** prove MS8 from MS11 exactly as stated.

**Open:**
- MS11♭ itself;
- entry 82 (Rig);
- the inherited inputs listed in §4.

**Status: proved (the corrected derivation MS11♭ ⇒ MS8); not proved (MS11 ⇒ MS8 as worded); open (MS11♭, (Rig)).**

