# round9_q10: rigidity of V_0 (open gap E)

**Plan and status.** I attack the route through the Kobayashi geometry of the deformed surfaces. This is a variant of suggested approach 1, combined with the Teichmüller-curve pinning of round5_q7.

What I establish:
- (K1) V_0 is Kobayashi-isometric in T_g: both the infinitesimal metric and the distance agree with the Teichmüller ones.
- (K2) A marked length-domination inequality for V_t.
- (K3) An equality-case lemma: if a single pseudo-Anosov keeps its length in V_t, and that length is attained, then a whole Teichmüller disc of V_0 persists in V_t. Combined with round5_q7 Lemma 1 / Prop. 2, this proves the claim.

I do **not** prove (D1), (D2) or (D3) in general. The route reduces to a Thurston-type length-spectrum rigidity for Kobayashi metrics, which I state as an open problem. I found no counterexample.

Readings (R1), (R2) are used as stated in the task. By (R2) together with round4_q8 B.2(a), H_t identifies π_1(V_t) with π_1(V_0), and the monodromies ρ_t, ρ_0 into Mod_g are conjugate. After composing with a fixed element of Mod_g we may take ρ_t = ρ_0 =: ρ.

Notation:
- T_g is Teichmüller space with the Teichmüller metric d_T.
- By Royden's theorem (cited from memory), d_T equals the Kobayashi distance of T_g, and the Teichmüller Finsler norm ‖·‖_T equals the Kobayashi–Royden metric.
- Ṽ_t ⊂ T_g is a fixed connected component of the preimage of V_t, chosen continuously in t via H_t. Write Γ_t ⊂ Mod_g for its stabilizer. Ṽ_t is a closed connected complex submanifold of T_g (V_t is smooth and closed in M_g; I work with the orbifold preimage).
- K_X denotes the Kobayashi–Royden metric and d_X the Kobayashi distance of a complex manifold X.

## 1. Lemma K1 (V_0 is Kobayashi-isometric)
(a) For every t, every x ∈ Ṽ_t and every v ∈ T_xṼ_t, K_{Ṽ_t}(v) ≥ ‖v‖_T. Hence d_{Ṽ_t} ≥ d_T on Ṽ_t × Ṽ_t.

(b) For t = 0 there is equality: K_{Ṽ_0}(v) = ‖v‖_T and d_{Ṽ_0} = d_T|_{Ṽ_0}.

*Proof.*
(a) Holomorphic maps decrease Kobayashi metrics. Apply this to the inclusion, and use Royden's theorem.

(b) Infinitesimal equality.
- Total geodesy means the following. For each v ∈ T_xṼ_0, v ≠ 0, the Teichmüller disc φ_v: 𝔻 → T_g has φ_v(0) = x and φ_v'(0) = v/‖v‖_T. It is a holomorphic isometry for the Poincaré metric (curvature −4 normalisation, the one matching Royden). Its image lies in Ṽ_0.
- So φ_v is a competitor in the definition of K_{Ṽ_0}, which gives K_{Ṽ_0}(v) ≤ ‖v‖_T. With (a), equality holds.

(b) Equality of distances.
- Fix x. Define E: T_xṼ_0 ≅ R^4 → T_g by E(v) = the point at Teichmüller distance ‖v‖_T along the geodesic ray from x in direction v. That ray is the real ray in φ_v(𝔻), so E maps into Ṽ_0.
- E is continuous. This follows from continuity of the Teichmüller geodesic flow (Teichmüller's theorem, cited).
- E is injective. Geodesics in T_g are unique, and d_T(x, E(v)) = ‖v‖_T.
- E is proper onto its image, since d_T(x, E(v)) = ‖v‖_T. So E(R^4) is closed in T_g, hence closed in Ṽ_0.
- By invariance of domain, E(R^4) is open in the real 4-manifold Ṽ_0.
- Ṽ_0 is connected, so E is onto. Hence any y ∈ Ṽ_0 is joined to x by the Teichmüller geodesic segment, which lies in Ṽ_0.
- By the infinitesimal equality and Royden's integrated form of the Kobayashi distance (d is the infimum of K-lengths of piecewise C^1 paths; cited), d_{Ṽ_0}(x,y) ≤ T-length of the segment = d_T(x,y). With (a), equality holds. ∎

## 2. Lemma K2 (marked length domination)
For g ∈ Mod_g and a subset X ⊂ T_g, set ℓ_X(g) := inf_{x ∈ X} d_X(x, gx) (the translation length; for X = T_g, d_X = d_T).

Let γ ∈ π_1(V_0) be such that ρ(γ) is pseudo-Anosov and its Teichmüller axis A_γ lies in Ṽ_0. This holds, for example, for hyperbolic elements of the Veech group of a Teichmüller curve contained in V_0. Then for all t:

  ℓ_{Ṽ_t}(ρ(γ)) ≥ τ(ρ(γ)) = ℓ_{Ṽ_0}(ρ(γ)),

where τ(ρ(γ)) = log λ(ρ(γ)) is the Teichmüller translation length, i.e. the log of the dilatation, half-log in some normalisations.

*Proof.*
- By K1(a), for any x ∈ Ṽ_t we have d_{Ṽ_t}(x, ρ(γ)x) ≥ d_T(x, ρ(γ)x) ≥ τ(ρ(γ)). Bers' theorem (cited) says τ is the minimum displacement, attained exactly on A_γ.
- For t = 0, take x ∈ A_γ ⊂ Ṽ_0. By K1(b), d_{Ṽ_0}(x, ρ(γ)x) = d_T(x, ρ(γ)x) = τ. Combined with the first point, ℓ_{Ṽ_0} = τ. ∎

So the deformation can only **increase** the Kobayashi lengths of these classes. This is the surface analogue of the first step of McMullen's proof of rigidity of Teichmüller curves (round5_q7 §2).

## 3. Lemma K3 (equality case: a Teichmüller disc persists)
Let γ, A_γ be as in K2, and let D = φ(𝔻) ⊂ Ṽ_0 be the Teichmüller disc containing A_γ. Suppose that for some t:
- ℓ_{Ṽ_t}(ρ(γ)) = τ(ρ(γ)), and
- the infimum is attained at some x ∈ Ṽ_t.

Then D ⊂ Ṽ_t.

*Proof.*
1. **x lies on the axis.** d_T(x, ρ(γ)x) ≤ d_{Ṽ_t}(x, ρ(γ)x) = τ, so x has minimal displacement. By Bers' theorem (cited), x ∈ A_γ.
2. **A minimizing path exists.** Ṽ_t is a closed complex submanifold of T_g, and d_{Ṽ_t} ≥ d_T with d_T complete. So d_{Ṽ_t} is a complete, locally compact length metric: by Royden it is the inner metric of K_{Ṽ_t} (cited). By Hopf–Rinow for length spaces, there is a rectifiable path c in Ṽ_t from x to ρ(γ)x of d_{Ṽ_t}-length τ.
3. **The path is the axis segment.** Since d_T ≤ d_{Ṽ_t}, the d_T-length of c is at most τ. It is also at least d_T(x, ρ(γ)x) = τ. So c is a d_T-geodesic. Teichmüller geodesics are unique (Teichmüller's theorem), so c is the segment of A_γ from x to ρ(γ)x.
4. **The whole axis lies in Ṽ_t.** Ṽ_t is ρ(γ)-invariant, because ρ_t = ρ and γ ∈ π_1(V_t) via H_t. So all translates of the segment lie in Ṽ_t, i.e. A_γ ⊂ Ṽ_t.
5. **The disc lies in Ṽ_t.** φ^{-1}(Ṽ_t) is an analytic subset of 𝔻: Ṽ_t is a closed submanifold, locally the zero set of holomorphic functions. It contains the real geodesic φ^{-1}(A_γ), which is a non-discrete set. So it is all of 𝔻. ∎

**Corollary K4 (conditional pinning).** Let T ⊂ V_0 be the Teichmüller curve with lift D (Teichmüller curves in V_0 come from Veech groups; every hyperbolic element of the Veech group gives an admissible γ). Suppose closure(T) meets the boundary piece ∂V_0 ⊂ Δ_Γ of the problem, and suppose the hypothesis of K3 holds for that γ and for all t in a set S accumulating in Δ. Then Y_t = Y_0 for all t.

*Proof.* For t ∈ S, K3 gives T ⊂ V_t. Then closure(T) ⊂ closure(V_t), so closure(V_t) ∩ ∂V_0 ≠ ∅. round5_q7 Lemma 1 finishes the argument (it uses only the holomorphy of t ↦ Y_t, round4_q8 §0). ∎

**Corollary K5 (conditional (D3)).** Suppose the hypothesis of K3 holds, for t near 0, for a family of discs whose projections are Zariski-dense in V_0. Then V_0 ⊂ V_t. Both are irreducible 2-dimensional and closed in M_g, so V_t = V_0, which gives (D3).

## 4. What remains: a length-spectrum rigidity problem
By K2 and K3, the route to (D2)/(D3) would follow from:

**Open problem (OQ-K).** For γ as in K2 (axis in Ṽ_0), and t near 0, is ℓ_{Ṽ_t}(ρ(γ)) ≤ τ(ρ(γ)), with the infimum attained? Equivalently, can a deformation V_t satisfying (i), (ii), (R1), (R2) strictly increase the Kobayashi length of every such class?

Why this is the precise point where the argument stops:
- **The model case.** For Teichmüller curves, McMullen closes the analogous gap with Thurston's theorem. A hyperbolic surface of the same finite-area type whose marked length spectrum dominates is isometric, because hyperbolic area is topological (Gauss–Bonnet).
- **The surface case.** Here K_{V_t} is only a Finsler metric. No Gauss–Bonnet-type invariant of the Kobayashi (or Kobayashi–Eisenman) volume is known to me that would make "domination implies equality" work. This is where the analogy breaks.
- **Attainment.** Even granting equality of lengths, attainment can fail, since V_t is non-compact. A minimizing sequence for the displacement could run into the cusps of V_t. Note that in K3 the axis A_γ projects to a closed geodesic of T, which lies in a compact part of V_0. But nothing transports compactness to V_t.
- **Semicontinuity.** I could not prove even upper semicontinuity of t ↦ ℓ_{Ṽ_t}(ρ(γ)) at t = 0. Holomorphic discs in V_0 do not push to discs in V_t, because the deformation is not holomorphically trivial (round5_q7 §3).

**Other suggested approaches (no progress; recorded).**
- **Approach 2 (Möller-type steps (α), (β), (γ)).** Nothing new. (γ) is still the core: I know no characterisation of totally geodesic surfaces by maximal Higgs fields.
- **Approach 3 (induction from the boundary).** Lemma R* fixes the Teichmüller vertex of each boundary curve. The constant factor Y_t is precisely the part that R* does not control. A maximum principle for sections of N vanishing on the boundary would need a negativity property of the (log) normal bundle N, and I could not establish one.
  - With the Weil–Petersson metric, N is a *quotient* bundle of T M_g|_{V_0}. Quotients gain curvature, and V_0 is not WP-totally-geodesic, so the second fundamental form term has the wrong sign.
  - So the standard Siu/Schumacher negativity argument does not apply.
- **Counterexample search.** None found. Any counterexample must vary the complex structure of V_t (round5_q7 §3). By K2 it must also strictly lengthen, in Kobayashi length, every closed Teichmüller geodesic of V_0 whose length is attained in V_t.

## Status
- **Proved** (modulo the cited theorems of Royden, Bers and Teichmüller uniqueness, Hopf–Rinow for length spaces, and round5_q7 Lemma 1):
  - K1: V_0 is Kobayashi-isometric in T_g, both infinitesimally and for distances.
  - K2: Kobayashi translation lengths of axis classes cannot decrease under the deformation.
  - K3: equality with attainment forces the corresponding Teichmüller disc to persist.
  - K4, K5: conditional pinning, and conditional (D3).
- **Not proved:** (D1), (D2), (D3) in general. The rigidity of V_0 remains **open**. It is reduced here to OQ-K, a Thurston-type marked length-spectrum rigidity for Kobayashi metrics of the surfaces V_t.

Final verdict: **not proved / open.**

=== END OF ANSWER round9_q10 ===
