# round6_q7: Lemma R without (O)

## Status and plan
**Lemma R without (O) is NOT settled in general here.** This file establishes the following.

1. **Lemma N (proved).** Under (R2), the normalised total space 𝓝 of 𝓔 = H(E_0 × Δ) has reduced fibre over t = 0. At every point, the germ of that fibre is unibranch, and its normalisation is the corresponding germ of Ẽ_0.
2. **Theorem L (proved; the globalisation in §3.3, Steps 1–3, is written at the level of a careful sketch).** (O) holds, and hence Lemma R holds via Lemma R* of PR-E, under a pointwise condition (★) at the interior points of Ẽ_0 and (★∞) at its punctures. Roughly, (★) says that every automorphism of the curve f_0(c) comes, modulo the generic automorphism group K, from the local group of O_0 at c. There is no hypothesis that 𝓝 is smooth: smoothness is *derived*.
   - In particular (O) holds automatically near every c with f_0(c) not an orbifold point. This proves the creation-excluded claim of PR-E §2.3, whose sketch there was flawed (see §4).
3. **Obstructions (proved).** If (★) fails, three explicit local models show that the germ of the Teichmüller disc at t = 0, together with a smooth, topologically trivial family of source curves, is compatible with a change of orbifold type. Any proof of (O), or of Lemma R, in the remaining cases must therefore be global.
   - This corrects the planner's claim that a pseudo-reflection of the isotropy group acting on T is needed. It is enough that the isotropy acts as a reflection on the lifted 2-dimensional family, which needs no reflection on T.
4. **Open.** Lemma R when (★) or (★∞) fails, i.e. in the three mechanisms of §4.

Conventions are those of PR-D/PR-E. Readings (R1) and (R2) are assumed throughout. K denotes the kernel of the action of Mod_{h,m} on T_{h,m} (the generic automorphisms; trivial except in the usual small cases). All isotropy groups below are taken modulo K, i.e. effectively.

## 1. Setting and notation

- E_0 ⊂ Δ_G, the vertex v with factor M := M_{h,m}, and T := T_{h,m}.
- (Ẽ_0, O_0), Λ_0, ρ_0 and F_0 : D → T are as in Lemma R:
  - F_0 is ρ_0-equivariant and is an isometry onto the Teichmüller disc 𝔇_0;
  - f_0 := π_v ∘ ν_0.
- 𝓔 := H(E_0 × Δ) ⊂ Δ_G × Δ. Near every point of E_0 × {0} this is a 2-dimensional analytic set:
  - it is locally a union of irreducible components of closure(𝒱) ∩ (Δ_G × Δ), by (R1) and Lemma R0's argument;
  - near points of E_0 this union is exactly 𝓔, because H is a homeomorphism onto closure(𝒱) mapping strata to strata.
- 𝓝 → 𝓔 is the normalisation, t : 𝓝 → Δ is the projection, and Φ := π_v ∘ (𝓝 → 𝓔) : 𝓝 → M is holomorphic.
- For c ∈ Ẽ_0:
  - c̃ ∈ D is a lift of c, and X̂ := F_0(c̃) ∈ 𝔇_0;
  - Stab(X̂) ⊂ Mod is the (finite) isotropy group of X̂, taken modulo K;
  - e_0(c) := |Stab_{Λ_0}(c̃)|. Since ρ_0 is injective (PR-E Step 1), this equals |ρ_0(Stab_{Λ_0}(c̃))|.
- **Orbifold chart.** U is a small Stab(X̂)-invariant ball around X̂ in T, and π : U → U/Stab(X̂) is an orbifold chart of M at X = f_0(c).
- L := the germ of 𝔇_0 at X̂, a smooth disc.

**Condition (★) at c.** The injection ρ_0 : Stab_{Λ_0}(c̃) → Stab(X̂) (modulo K) is surjective.

Equivalently, every automorphism of the curve X = f_0(c) is, modulo K, an affine automorphism of the generating differential lying in ρ_0(Λ_0). Consequences:
- Stab(X̂) ⊂ Stab(𝔇_0)·K.
- Stab(X̂)/K acts **faithfully** on L. Proof: if ρ_0(λ)k fixes L pointwise, then λ acts trivially on D, because F_0 is equivariant and injective. So λ = 1.
- (★) holds trivially at every c with f_0(c) not an orbifold point of M.

**Condition (★∞) at a puncture p of Ẽ_0.** Let Z ∈ ∂M̄ be the limit of f_0 at p. This limit exists: the closure of π_v(E_0) is analytic (PR-D Step 6), so f_0 extends holomorphically to the compactification. The condition is that Aut(Z) acts on the versal deformation space of Z through K, i.e. Aut(Z)/K = 1. Then M̄ is a manifold near Z, modulo K.

## 2. Lemma N (the zero fibre of 𝓝)

**Lemma N.** Assume (R2), and let n_0 ∈ 𝓝 with t(n_0) = 0. Then:
- (a) the divisor div(t) of 𝓝 is reduced near n_0;
- (b) the germ at n_0 of the reduced zero fibre (𝓝_0)_red is unibranch;
- (c) the normalisation of (𝓝_0, n_0) is the germ of Ẽ_0 at a unique point c. Conversely, every c ∈ Ẽ_0 arises from exactly one n_0.

*Proof.*

**Step 1 (generic points).** Let q ∈ E_0 be a manifold point of E_0 at which E_0 has a single branch. Choose:
- a small disc W ∋ q in E_0, with H(W × Δ') a neighbourhood of (q,0) in 𝓔.

H(W × Δ') is homeomorphic to W × Δ', a topological 4-manifold. So 𝓔 is locally irreducible at (q,0): the regular part of an analytic germ that is a topological manifold is connected near the point, because the singular set has real codimension ≥ 2. Hence the normalisation 𝓝 → 𝓔 is a homeomorphism near (q,0).

**Step 2 (reducedness, (a)).** Let Z_1 be a component of (𝓝_0)_red through n_0, and z ∈ Z_1 a generic point, at which 𝓝 and Z_1 are smooth. Then:
- In coordinates (σ, x) at z with Z_1 = {σ = 0}, we have t = (unit)·σ^μ.
- Hence, for small polydiscs N ∋ z and 0 < |t| < ε, the fibre N_t is a disjoint union of μ discs D_1, …, D_μ. Each of them passes through any prescribed smaller polydisc N'' ∋ z once t is small.

By Step 1, applied at q = image of z, the following holds. Choose a disc W' ∋ q and Δ'' with H(W' × Δ'') ⊂ N (identifying 𝓝 with 𝓔 near z). Then choose N'' with H^{-1}(N'') ⊂ W' × Δ''. This is possible because H is a homeomorphism.

Now H_t(W') is connected and contained in N_t = ⊔ D_j. It contains N''_t, which meets every D_j. Therefore μ = 1. So div(t) has multiplicity 1 along every component, and (a) follows.

The same argument shows that (𝓝_0)_red → E_0 is generically injective. If two points of 𝓝 lay over a generic point q, then 𝓔 would not be locally irreducible at (q,0).

**Step 3 (unibranch, (b)).** Since 𝓝 is normal, the germ (𝓝, n_0) is irreducible, so 𝓝 \ {t = 0} is connected near n_0.

The Milnor fibre F_t := 𝓝_t ∩ B (B a Milnor ball) is connected. Indeed, its components are permuted transitively by the monodromy. If there were d ≥ 2 of them, then "which component" would define a d-valued function. Normality of 𝓝 would make this function single-valued holomorphic on a d-fold cyclic cover, giving g with t = (unit)·g^d. That contradicts (a). (This is the standard argument; I cite the conclusion — a function with reduced divisor on a normal surface germ has connected Milnor fibre — from memory.)

Now suppose (𝓝_0)_red had k ≥ 2 branches at n_0. By Step 2 they map to k distinct branches W_1, …, W_k of E_0 at q := image of n_0. Let W be the union of all branches of E_0 at q. Then:
- W \ {q} = ⊔ (W_i \ {q}) is a disjoint union of open sets, so H_t(W) \ {H_t(q)} = ⊔ H_t(W_i \ {q}) is a disjoint union of open sets of 𝓔_t.
- For t small, H_t(W) contains F_t ∩ N'' (as in Step 2), and F_t ∩ N'' minus one point is connected.
- Each H_t(W_i \ {q}) with i ≤ k meets F_t ∩ N''. Indeed, points of W_i near q are sent near n_0 by H_t, by continuity of H at (q,0), and into the local piece of 𝓔 normalised by the germ at n_0. This is because H(W_i^∘ × Δ) is a connected subset of the locally irreducible part of 𝓔.

So a connected set meets k ≥ 2 disjoint open sets covering it. This is a contradiction, so k = 1 and (b) holds.

**Step 4 ((c)).** (c) follows from (b) and generic injectivity: the normalisation of (𝓝_0)_red is the normalisation of E_0, namely Ẽ_0. ∎

*Remark.* This is the precise form of the Milnor-fibre / topological-triviality input that Route 1 asked for. Note that it does **not** say that 𝓝 is smooth or that the zero fibre of 𝓝 is smooth. Smoothness is obtained in §3, and only under (★).

## 3. Theorem L: (★) and (★∞) imply (O)

### 3.1 Local proposition at an interior point

**Proposition L1.** Let c ∈ Ẽ_0 satisfy (★), let n_0 ∈ 𝓝 be the point from Lemma N(c), and put G := Stab(X̂)/K, of order e_0(c). Then there are:
- a smooth 2-dimensional germ (𝓟, p_0) with coordinates (s, t), on which G acts by g·(s,t) = (χ(g)s, t) with χ : G → ℂ^* injective;
- a G-equivariant holomorphic map Ψ : 𝓟 → U;

such that 𝓝 ≅ 𝓟/G near n_0, compatibly with t, and π∘Ψ = Φ under this identification. Consequently:
- 𝓝 is smooth at n_0 and t is a submersion there, with coordinates (s^{e_0}, t);
- for every small t, the minimal orbifold structure O_t^min has, in the neighbourhood {|s| < r} of n_0 in 𝓝_t, exactly one cone point, of order e_0(c), at s = 0;
- the local lifts Ψ|_{𝓟_t} of Φ|_{𝓝_t} depend holomorphically on t.

*Proof.*

**Step 1 (the fibre product).** Put 𝓠 := 𝓝 ×_{U/G} U near (n_0, X̂). The only point over n_0 is (n_0, X̂), since π^{-1}(X) = {X̂}. Let 𝓟^ν be the normalisation of 𝓠.

The generic isotropy of the lifted surface Ψ(𝓟^ν) is trivial: if g ≠ 1 fixed it pointwise, then g would fix its zero fibre, which is L (Step 2), pointwise, contradicting faithfulness under (★). So 𝓠 → 𝓝 is generically a G-torsor, of degree |G| = e_0, and G permutes the components of 𝓟^ν transitively.

**Step 2 (the zero fibre of 𝓟^ν).** Choose a coordinate z on L in which G acts by z ↦ χ(g)z. Then π(L) ≅ L/G has coarse coordinate z^{e_0}. Let w be a coordinate of Ẽ_0 at c, which by Lemma N(c) is the normalisation parameter of (𝓝_0, n_0).

By (★), F_0 near c̃ is the orbifold chart of O_0 at c followed by a biholomorphism onto L, and the stabiliser of c̃ is all of G. So f_0 is a coarse local isomorphism B_0 → L/G, and we may take z^{e_0} = w on the lift. Under (★), π^{-1}(f_0(B_0)) = ∪_g gL = L. Hence the zero fibre of 𝓠, pulled back to the normalisation of 𝓝_0, is {(w, z) : z^{e_0} = w}: **one** smooth branch b, mapping with degree e_0 to the normalisation of 𝓝_0.

**Step 3 (multiplicity).** Let p : 𝓟^ν → 𝓝 be the projection, and write p^* div(t) = Σ m_i Z'_i. By the projection formula, p_*(p^* div t) = e_0 · div(t), and div(t) = 1·(𝓝_0) near n_0 by Lemma N(a). Each Z'_i lies over the single branch b, so deg(Z'_i → 𝓝_0) ≥ e_0. Hence Σ m_i deg(Z'_i → 𝓝_0) = e_0 forces:
- there is exactly one Z'_1 =: Z', with m_1 = 1 and deg = e_0;
- in particular 𝓟^ν is irreducible near the point p_0 over (n_0, X̂), and G_k = G.

**Step 4 (smoothness).** Z' is unibranch, since its normalisation is the single branch b ≅ L. The function z∘Ψ restricted to Z' has order 1 at p_0 on that normalisation. A unibranch curve germ carrying a function of order 1 has multiplicity 1, so Z' is smooth at p_0.

𝓟^ν is a normal surface, so it is Cohen–Macaulay. Hence 𝒪/(t) has no embedded points. It is generically reduced along Z', because m = 1, so 𝒪_{𝓟^ν}/(t) = 𝒪_{Z'}, a regular 1-dimensional ring. Therefore 𝒪_{𝓟^ν, p_0} is regular of dimension 2 and t is part of a coordinate system. Put 𝓟 := 𝓟^ν.

**Step 5 (linear coordinates).** t is G-invariant. At p_0, T_{p_0}Z' = ker dt, and G acts on it by χ, since Z' ≅ L equivariantly. Take any function s_0 with ds_0|_{TZ'} ≠ 0, and put
  s := |G|^{-1} Σ_g χ(g)^{-1} (s_0∘g).
Then s∘g = χ(g)s, and ds|_{TZ'} = ds_0|_{TZ'} ≠ 0. So (s, t) are coordinates and g(s,t) = (χ(g)s, t). χ is injective because G acts faithfully on L.

**Step 6 (consequences).** 𝓝 is normal and 𝓟 → 𝓝 is generically Galois with group G. Hence 𝓝 = 𝓟/G, which is smooth with coordinates (s^{e_0}, t).

For fixed t, 𝓟_t = {t = const} is a disc on which G acts by rotations about s = 0 alone. Every nonidentity element has the single fixed point s = 0. Two fibres 𝓟_t lying over the same 𝓝_t cannot be distinct branches, since 𝓟_t is connected. So:
- the branch stabiliser of the lift Ψ|_{𝓟_t} of Φ|_{𝓝_t} is G at the image of s = 0, and is trivial elsewhere;
- this is exactly the definition of the cone orders of O_t^min (PR-E §2.3).

Ψ is holomorphic in (s, t), which gives the last claim. ∎

**Corollary L2 (creation is excluded at points that are not orbifold points).** If f_0(c) is not an orbifold point of M, then near n_0 the surface 𝓝 is smooth, t is a submersion, and O_t^min has no cone point near n_0 for small t. (This is the case G = 1 of L1.)

### 3.2 Punctures

**Proposition L3.** Let p be a puncture of Ẽ_0 satisfying (★∞). Then there are a neighbourhood 𝒱_p of the end p of Ẽ_0, and ε > 0, such that for |t| < ε the part of Ẽ_t corresponding to 𝒱_p, under the transport of (R2) and Ĥ_t, contains no cone point of O_t^min.

*Proof.*
- By (★∞) there is a neighbourhood Ω of Z in M̄ such that Ω ∩ M contains no orbifold points (modulo K).
- The compactified maps f̄_t are restrictions of a single holomorphic, hence continuous, map on the normalisation of the analytic family 𝓦^{(a)} of Lemma R0 (PR-D), composed with pr_v. This is the place where (R1) enters.
- So there are a neighbourhood of the point over (p, 0) in that normalisation, mapped into Ω, and ε > 0 such that its fibres over |t| < ε contain the transported end.
- Points mapped into Ω ∩ M are not orbifold points, so they are not cone points. ∎

### 3.3 Theorem L

**Theorem L.** Assume (R1) and (R2), and the hypotheses of Lemma R. Assume (★) at every c ∈ Ẽ_0 and (★∞) at every puncture of Ẽ_0. Then (O) of PR-E holds for |t| small. Consequently, by Lemma R* of PR-E together with the analytic-continuation argument below, closure(π_v(E_t)) = closure(π_v(E_0)) for all t ∈ Δ.

*Proof.*

**Step 1 ((O-a) and (O-b)).**
- Cover a compact core 𝒦 ⊂ Ẽ_0, the complement of small end neighbourhoods 𝒱_p as in L3, by finitely many neighbourhoods given by L1 and L2.
- By L1 and L2, 𝓝 is smooth with t a submersion along 𝒦 × {0}. So by Ehresmann the fibres over |t| < ε form a smooth trivial family over 𝒦.
- By L1, the cone points of O_t^min in this family are exactly one point near each cone point c of O_0, of the same order e_0(c). By L3, there are none near the ends.
- The local lifts vary continuously (L1), which gives (O-b).

**Step 2 (the end neighbourhoods).** These are punctured discs for all small t: by (R2) they are transported by H, and they do not touch the core.

**Step 3 (θ_t and ρ_t).** Combining the Ehresmann trivialisation with these discs gives a homeomorphism Ẽ_0 → Ẽ_t that:
- preserves cone points with their orders, and cusps;
- is isotopic to Ĥ_t, since both depend continuously on t and agree with the identity at t = 0.

This yields θ_t. Then t ↦ ρ_t∘θ_t^{-1} is continuous into the discrete set Hom(Λ_0, Mod) (PR-E §2.3), hence constant. This is (O).

**Step 4 (Lemma R*).** Lemma R* (PR-E) gives π_v(E_t) = π_v(E_0) for |t| < ε.

**Step 5 (all t).** Let 𝒲 be the irreducible 2-dimensional analytic family of Lemma R0, and C̄_0 := closure(π_v(E_0)) ⊂ M̄. The set 𝒲 ∩ (pr_v^{-1}(C̄_0)) is analytic in 𝒲 and contains all fibres over |t| < ε. Hence it equals 𝒲. (Otherwise it would have dimension ≤ 1, and its fibre-contained components lie over a discrete set of t.) So π_v(E_t) ⊂ C̄_0 for all t. Then equality of closures follows from irreducibility and non-constancy, as in PR-D Step 6. ∎

*Scope of Theorem L.*
- It covers every E_0 whose Teichmüller curve meets the orbifold locus of M only at points X with Aut(X)/K = ρ_0(local group). This holds, for example, when E_0 → C_0 is birational, Λ_0 is the full Veech group modulo K, and every automorphism of every curve on the Teichmüller disc preserves the disc.
- It also covers the case where C_0 avoids the orbifold locus altogether (except through K) and its cusps are curves without extra automorphisms.
- It does **not** cover Teichmüller curves lying inside an orbifold locus, e.g. hyperelliptic Teichmüller curves in M_3, for which (★) fails at every point.

## 4. When (★) fails: three local models (proved), so any further proof must be global

(★) can fail at c in exactly three ways. Write G := Stab(X̂)/K and H_c := ρ_0(Stab_{Λ_0}(c̃)) ⊂ G ∩ Stab(𝔇_0). Then (★) fails iff one of the following holds:
- **(cross)** G ⊄ Stab(𝔇_0);
- **(fix)** some g ∈ G \ {1} fixes 𝔇_0 pointwise;
- **(ram)** G ⊂ Stab(𝔇_0) acts faithfully on L, but H_c ⊊ G. Equivalently, Ẽ_0 → C_0 has coarse local degree r = |G|/e_0(c) > 1 at c.

For each of them there is an explicit germ with the following properties:
- a family 𝓝 ≅ ℂ² with t a coordinate, so the source family is smooth and trivial, and Lemma N holds;
- a holomorphic Φ : 𝓝 → U/G;
- at t = 0, Φ_0 lifts isometrically onto the germ L of the Teichmüller disc, with the orbifold structure prescribed by O_0;
- O_t^min for t ≠ 0 has a **different type** near c.

Write X̂ = 0 in a linear chart of U where G acts linearly (Cartan). Let δ(z) parametrise L.

**(cross).** Take g ∈ G of order 2 with gL ≠ L and T_0(gL) ≠ T_0L. Such g exists whenever g^*q ∉ ℂ^* q for the generating q, by genericity of the tangent directions.
- Ψ(z,w) := δ(z) + gδ(w) is an immersion at 0, and g(Ψ(z,w)) = Ψ(w,z).
- Let 𝓝 be the quotient by the swap, with coordinates (σ, t) = (z+w, zw), and Φ := π∘Ψ. This descends to 𝓝.
- t = 0: the fibre {zw = 0}/swap ≅ L, with lift z ↦ δ(z) and no cone point at c.
- t ≠ 0: the lifted fibre {zw = t} is connected and g-invariant, with fixed points z = w = ±√t. So there are **two cone points of order 2** (creation).
- The (ℤ/2)² splitting model of the task is the analogous construction with e_0(c) = 2.

**(fix).** Take a ∈ G of order 2 with L ⊂ Fix(a), and a normal eigen-direction x_2 with eigenvalue −1, so a = diag(1, −1, …) and L = {x_2 = 0}.
- Put Φ(s,t) := π(s, √(ts), 0, …). The coarse coordinates are (x_1, x_2², …), so this is the holomorphic map (s, ts, 0, …).
- t = 0: the lift s ↦ (s, 0) ∈ L. Here a acts trivially on L, so there is no cone point.
- t ≠ 0: the lift x_2 = √(ts) branches at s = 0, giving **one cone point of order 2** (creation).
- This occurs, for example, along every hyperelliptic Teichmüller curve in M_3 (with ι a reflection on T_3). However, there are no marked points there, so it is only an analogue of the boundary-factor situation.

**(ram).** Take g ∈ G ∩ Stab(L) of order 2 acting on L by −1, with a g-fixed direction x_2 transverse to L, so g = diag(−1, 1, …) and L = x_1-axis. This needs dim Fix(g) ≥ 1.
- Put Φ(w,t) := (w² − t, t, 0, …) in coarse coordinates (x_1², x_2, …).
- t = 0: the lift w ↦ (w, 0) ∈ L is isometric, and c is regular in O_0 with e_0 = 1. Here f_0 is coarsely 2:1 onto L/G, so this is an orbifold-unramified point over an order-2 orbifold point of C_0.
- t ≠ 0: the lift x_1 = √(w² − t) branches at w = ±√t, giving **two cone points of order 2**, while f_t acquires an ordinary ramification point at w = 0. The images C_t are the g-invariant discs {x_2 = t} through the orbifold points (0, t).

**Consequences.**
1. In each model, the data at t = 0 are only the germ of 𝔇_0 at X̂ and the local orbifold structure. Lemma N and the conclusion "𝓝 smooth, t submersive" also hold. So (O-a) cannot be derived from local information at c, and Route 1 alone cannot prove (O) without (★).
2. **Correction to the planner.** In (cross) and (ram), g need not be a pseudo-reflection on T. It acts as a reflection on the 2-dimensional lifted family (the swap, respectively the folding), which is automatic. So "pseudo-reflection in the isotropy group of M" is not a necessary condition for splitting or creation.
3. **Correction to PR-E §2.3.** The sketch "a g-invariant branch at time t converges to a g-invariant branch at time 0" is false in (cross): the g-invariant branch {zw = t} converges to the union of two branches. Corollary L2 replaces that sketch by a proof in the case where f_0(c) is not an orbifold point. In that case all three mechanisms are absent.
4. In all three models the orbifold Euler characteristic of O_t differs from that of O_0 by −1 or −1/2. So the length comparison ℓ_{O_t} ≥ ℓ_{O_0} of PR-E Step 3 cannot conclude via Thurston. Larger orbifolds have larger lengths, and the inequality is then consistent.

## 5. A global tool for the (fix) mechanism (proved)

**Lemma D (negative normal degree pins the family).** Let 𝒟 be an effective ℚ-Cartier divisor on the coarse space of M̄_v, with support B ⊇ C̄_0 := closure(π_v(E_0)) and deg(f̄_0^* 𝒟) < 0, where f̄_0 is the compactified map from the compactification of Ẽ_0. Then π_v(E_t) ⊂ B for all t ∈ Δ.

*Proof.*
- The compactified maps f̄_t are the fibres of the proper analytic family 𝒲^{(a)} → Δ of Lemma R0, composed with pr_v. The fibre cycles of a proper family over a disc are homologous, so deg f̄_t^*𝒟 = ⟨[pr_{v*} 𝒲_t], c_1(𝒟)⟩ is independent of t.
- If π_v(E_t) ⊄ B, then f̄_t^*𝒟 is an effective ℚ-divisor on a curve, so its degree is ≥ 0. That is a contradiction.
- So π_v(E_t) ⊂ B for every t. ∎

*Use.* In mechanism (fix), with B the closure of the image of Fix(a), negative normal degree confines the whole family to B. One can then hope to rerun §3 inside the smaller orbifold B, which is uniformised by T(X/a) ⊂ T. There a no longer obstructs, because it acts trivially there. I have not carried this out.

*Heuristic illustration (cited from memory, not used).* For M_3 (no marked points), use:
- [H̄yp] = 9λ − δ_0 − 3δ_1;
- slope 28/3 for Teichmüller curves in the hyperelliptic components, from Chen–Möller / Eskin–Kontsevich–Zorich;
- δ_1·C = 0, since cylinder cores are non-separating.

These give [H̄yp]·C = −λ·C/3 < 0, so Lemma D would apply. The boundary factors M_{3,m} with m ≥ 1 are a different situation.

## 6. Summary: proved, conditional, open

**Proved.**
- Lemma N.
- Proposition L1 (local transport under (★)) and Corollary L2 (no creation at points that are not orbifold points).
- Proposition L3 (no cone points near a cusp under (★∞)).
- Theorem L: (★) everywhere and (★∞) at all punctures ⇒ (O) ⇒ the conclusion of Lemma R for all t. The globalisation steps are written as a careful sketch. The cited inputs are the Milnor-fibre connectivity (from memory) plus those of PR-E (Royden, Bers, Thurston, Selberg).
- The three local models of §4, showing that without (★) local analysis cannot give (O).
- Lemma D.

**Not proved / open.**
- (Q1) Lemma R when (★) fails at some c: mechanisms (cross), (fix) and (ram). It is unknown whether any of the local models globalises to a deformation f_t of an orbifold-unramified cover of a Teichmüller curve with non-constant image. A counterexample to Lemma R would require exactly such a global deformation in which the orbifold type changes. Lemma R* rules out all deformations that preserve the type.
- (Q2) Lemma R when (★∞) fails, i.e. some cusp of the Teichmüller curve goes to a stable curve with extra automorphisms. Here cone points can enter from the cusp. The local model is: puncture section {s^e = t} and fixed curve {s = 0} in 𝓟. I have not analysed this.
- (Q3) In mechanism (fix), the sign of the normal degree of the fixed locus along C_0. Lemma D handles only the negative case.

So the chain of the run (MS5 + Lemma R ⇒ the problem's claim) is now complete **only** for Teichmüller pieces satisfying (★) and (★∞), together with the previously known case where M_u has no orbifold points (which is the special case of Theorem L with all groups trivial).

=== END OF ANSWER round6_q7 ===

