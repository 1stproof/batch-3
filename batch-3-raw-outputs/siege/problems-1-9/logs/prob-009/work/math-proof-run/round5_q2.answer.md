# round5_q2 — answer (work in progress)

## Plan
Target: MS4 (t -> Y_t constant). Realistic sub-goals, in order:
1. Prove Lemma R (rigidity of a boundary curve whose vertex-projection is a Teichmüller curve, under a family with varying complex structure), carefully, using Royden, Thurston's asymmetric metric, Imayoshi–Shiga (all cited from memory).
2. Note that the pinning only needs a *fixed finite set* containing Q_t, so F_t = F_0 is not needed (only finiteness of the possible images).
3. State the resulting reduction theorem: MS4 holds whenever (T0) holds at t = 0; also a Lemma-F variant without the Hodge-theoretic input.
4. Analyse what remains of (T0); state clearly that MS4 in full is NOT settled here.

Status (written up front, revised at the end): MS4 is NOT proved in full here. What is proved is an abstract
rigidity lemma (Lemma R) that needs no Hodge theory and no countability of Teichmüller curves. It gives a
conditional theorem whose only conditions are a statement about V_0 alone, namely (T0), and an orbifold
bookkeeping condition (Lev).

---

## 1. Lemma R: rigidity of a Teichmüller-isometric curve whose complex structure varies

Notation.
- T = T_{h,m} is Teichmüller space, with Teichmüller distance d_T. By Royden's theorem (cited from memory; Royden
  1971 for closed surfaces, Earle–Kra / Gardiner for punctured ones), d_T equals the Kobayashi distance of T.
- D is the unit disc with Kobayashi distance d_D, i.e. the Poincaré distance normalised so that holomorphic maps
  D -> T are 1-Lipschitz for (d_D, d_T), and a Teichmüller disc is a holomorphic isometric embedding (D, d_D) -> (T, d_T).
- Γ' ≤ Mod_{h,m} is a torsion-free subgroup of finite index acting freely on T (e.g. a level-N subgroup, N ≥ 3,
  by Serre's lemma). So M' := T/Γ' is a complex manifold, and T -> M' is its universal covering.
- For φ ∈ Mod_{h,m} put τ_T(φ) := inf_{X ∈ T} d_T(X, φX). This is invariant under conjugation.
- Σ is a connected oriented surface of finite type with χ(Σ) < 0. A marked finite-type Riemann surface is a
  homeomorphism σ: Σ -> X onto a Riemann surface X (compact minus finitely many points, the punctures
  corresponding to the ends of Σ). X carries its complete finite-area hyperbolic metric. For a free homotopy class
  γ of closed curves in Σ, ℓ_X(γ) is the translation length on (D, d_D) of the corresponding deck transformation;
  this is 0 exactly for peripheral γ.

**Lemma R.** Let σ_t: Σ -> X_t (t in some index set containing 0) be marked finite-type Riemann surfaces, and let
F_t: X_t -> M' be holomorphic maps such that F_t ∘ σ_t is freely homotopic to F_0 ∘ σ_0 for every t. Assume that
some (equivalently, every) lift f̃_0: D -> T of F_0 to universal covers is a Teichmüller disc. Then for every t:
1. there is a biholomorphism β_t: X_0 -> X_t homotopic to σ_t ∘ σ_0^{-1};
2. G_t := F_t ∘ β_t: X_0 -> M' is a non-constant holomorphic map homotopic to F_0;
3. consequently G_t belongs to a finite set Φ of holomorphic maps X_0 -> M' that depends only on F_0, and the image
   curve F_t(X_t) = G_t(X_0) is one of the finitely many curves φ(X_0), φ ∈ Φ.

*Proof.*

Step 0 (monodromies). Identify π_1(X_t) with π_1(Σ) via σ_t. F_t induces ρ_t: π_1(Σ) -> Γ', defined up to
conjugation, with lift f̃_t: D -> T satisfying f̃_t(γx) = ρ_t(γ) f̃_t(x). Since F_t∘σ_t ≃ F_0∘σ_0 and T -> M' is a
covering with deck group Γ', ρ_t and ρ_0 are conjugate in Γ'. Hence τ_T(ρ_t(γ)) = τ_T(ρ_0(γ)) for all γ.

Step 1 (equality at t = 0). Let γ be non-peripheral, so γ acts on D as a hyperbolic isometry with axis A and
translation length ℓ := ℓ_{X_0}(γ) > 0. Put φ := ρ_0(γ).
- Upper bound: for x ∈ A, d_T(f̃_0 x, φ f̃_0 x) = d_T(f̃_0 x, f̃_0 γx) = d_D(x, γx) = ℓ.
- Lower bound: g := f̃_0(A) is a bi-infinite d_T-geodesic, since f̃_0 is an isometry. φ maps g to itself and
  translates it by ℓ. Fix x_0 ∈ A and any X ∈ T, and put c := d_T(X, f̃_0 x_0). For every n ≥ 1,
  n·d_T(X, φX) ≥ d_T(X, φ^n X) ≥ d_T(f̃_0 x_0, φ^n f̃_0 x_0) − 2c = nℓ − 2c,
  using the triangle inequality and the fact that φ is a d_T-isometry. Letting n -> ∞ gives d_T(X, φX) ≥ ℓ.
- Hence τ_T(ρ_0(γ)) = ℓ_{X_0}(γ).

Step 2 (inequality at time t). f̃_t is holomorphic, so it is 1-Lipschitz from (D, d_D) to (T, d_T) by Royden's
theorem and the distance-decreasing property of the Kobayashi distance. For every x ∈ D,
τ_T(ρ_t(γ)) ≤ d_T(f̃_t x, ρ_t(γ) f̃_t x) = d_T(f̃_t x, f̃_t γx) ≤ d_D(x, γx).
Taking the infimum over x gives τ_T(ρ_t(γ)) ≤ ℓ_{X_t}(γ). With Steps 0 and 1:
  ℓ_{X_t}(γ) ≥ ℓ_{X_0}(γ) for every non-peripheral γ, in particular for every essential non-peripheral simple closed curve.

Step 3 (Thurston). Cited from memory: W. Thurston, *Minimal stretch maps between hyperbolic surfaces* (preprint 1986),
Theorem 3.1 and its corollary. For two complete finite-area marked hyperbolic structures X ≠ Y on Σ,
sup_γ ℓ_Y(γ)/ℓ_X(γ) > 1, where the sup runs over essential non-peripheral simple closed curves. (This is the
positivity of Thurston's asymmetric metric; it equals the log of the best Lipschitz constant.)
- Apply this with X = X_t and Y = X_0. If X_t ≠ X_0 as marked surfaces, some γ has ℓ_{X_0}(γ) > ℓ_{X_t}(γ),
  contradicting Step 2.
- So X_t = X_0 in T(Σ), i.e. there is an isometry, hence a biholomorphism, β_t: X_0 -> X_t homotopic to σ_t∘σ_0^{-1}.

Step 4 (finiteness). G_t := F_t ∘ β_t is holomorphic and homotopic to F_t∘σ_t∘σ_0^{-1} ≃ F_0.
- G_t is non-constant: otherwise ρ_t would be trivial, so τ_T(ρ_t(γ)) = 0, whereas Steps 0 and 1 give
  τ_T(ρ_t(γ)) = ℓ_{X_0}(γ) > 0 for a non-peripheral γ, which exists since χ(Σ) < 0.
- Rigidity theorem (cited from memory, as in PR-4: Imayoshi–Shiga 1988, building on Arakelov–Parshin). For a
  Riemann surface S of finite type and a fine moduli space M' = T/Γ' as above, a homotopy class of maps S -> M'
  contains only finitely many non-constant holomorphic maps. (Holomorphic maps S -> M' are the same as holomorphic
  families of (h,m)-curves with Γ'-level structure over S, and non-constant means locally non-trivial.)
- Let Φ be that finite set for S = X_0 and the class of F_0. Then G_t ∈ Φ. ∎

**Remarks on Lemma R.**
- No continuity in t is used. The index set can be arbitrary.
- No Hodge theory is used, and neither is Möller's zero condition, McMullen's isometric-disc theorem (K), or the
  countability (Ct). This replaces Proposition D of PR-3.
- (Not needed below, and not proved here: whether G_t must itself be a Teichmüller disc. Equal translation lengths
  plus the 1-Lipschitz property suggest it, but I do not use it.)
- Lemma R uses the Teichmüller property of F_0 only through Step 1. So it holds verbatim for any F_0 whose
  monodromy is *length-saturating*, meaning τ_T(ρ_0(γ)) = ℓ_{X_0}(γ) for all simple closed γ.

---

## 2. Conditional theorem for MS4

Throughout, (R1) and (R2) hold, and H: closure(V_0) × Δ -> closure(𝒱) is the stratified homeomorphism of (R2),
with H_t := H(·, t).

### 2.1 Transport of boundary pieces (topological facts)

**Lemma T.** Let A_t be the union of the 1-dimensional irreducible components of closure(V_t) ∩ Δ_G. Then H_t maps
A_0 onto A_t, and it maps each irreducible component E_0 of A_0 onto an irreducible component E_t := H_t(E_0) of A_t.

*Proof.*
1. H_t maps closure(V_0) ∩ Δ_G homeomorphically onto closure(V_t) ∩ Δ_G, by (R2).
2. The 1-dimensional part is characterised topologically: it is the closure of the set of points having a
   neighbourhood homeomorphic to R^2. Hence it is preserved by H_t.
3. For a 1-dimensional analytic set A, call x ∈ A *multi-branched* if, for small neighbourhoods U of x, the set
   (U ∩ A) \ {x} has at least two connected components. Let B(A) be the set of multi-branched points. This is a
   discrete set, it is defined topologically, and H_t(B(A_0)) = B(A_t).
4. Each point of A \ B(A) is locally irreducible. So it lies on exactly one irreducible component, and that component
   is locally constant on A \ B(A).
5. Conversely, if C is an irreducible component, then C \ B(A) is connected. Indeed, it is the image of the
   connected normalisation of C minus a discrete set, and points of C lying on another component are in B(A).
6. So the irreducible components are exactly the closures in A of the connected components of A \ B(A), and this
   description is preserved by homeomorphisms. ∎

The same argument shows that H_t lifts to a homeomorphism h̃_t between the normalisations Ẽ_0 and Ẽ_t: points of
the normalisation are local branches, and those are preserved. Since closure(E_t) \ E_t is finite (it is a proper
analytic subset of a compact curve), Ẽ_t is a Riemann surface of finite type, homeomorphic to Ẽ_0.

### 2.2 The data (T0) and (Lev)

Fix a stratum Δ_{G'} ⊂ closure(Δ_Γ) and a point P_0 ∈ closure(∂V_0) ∩ Δ_{G'}. By P-b Lemma 1 (closure of
{Y_t} × C_t is {Y_t} × closure(C_t)), P_t := H_t(P_0) ∈ closure(∂V_t) ∩ Δ_{G'} (Lemma B′) has the smooth pointed
curve Y_t as its component at the vertex i of G'.

**(T0) (a condition on V_0 alone).** There exist such G', P_0, a stratum Δ_{G_b} with Δ_{G'} ⊂ closure(Δ_{G_b}),
an irreducible component E_0 of the 1-dimensional part of closure(V_0) ∩ Δ_{G_b} with P_0 ∈ closure(E_0), and a
local branch b of closure(E_0) at P_0, such that:
- (merge) writing G_b = G'/X′, where X′ ⊂ E(G') is the set of edges of G' that are smoothed along b, some edge of X′
  is incident to the vertex i. Let v be the vertex of G_b into which i is contracted, let W_v ⊂ V(G') be the set
  of vertices contracted to v, and let M_{h,m} be the factor of v.
- (Teich) the curve F_0 := π_v(E_0) ⊂ M_{h,m} is a Teichmüller curve, in the sense used in (Lev) below.

**(Lev) (orbifold bookkeeping).** For a torsion-free finite-index Γ' ≤ Mod_{h,m}, M' := T_{h,m}/Γ' and
p': M' -> M_{h,m} the natural finite map, and for all t in a neighbourhood N of 0, there are:
- a marked finite-type Riemann surface σ_t: Σ -> X_t, with Σ independent of t;
- a holomorphic map F̂_t: X_t -> M' with p'(F̂_t(X_t)) = F_t := π_v(E_t), and with F̂_t∘σ_t ≃ F̂_0∘σ_0;

and a lift of F̂_0 to universal covers is a Teichmüller disc. (This is the precise meaning of (Teich).)

(If Δ_{G_b} is a quotient stratum, π_v is only defined up to Aut(G_b). In that case replace E_t by the transported
irreducible component of its preimage in the product cover; nothing below changes.)

*Comment on (Lev).* The natural candidate is X_t := the normalisation of a component of Ẽ_t ×_{M_{h,m}} M', with the
marking induced by h̃_t. (Lev) asks that the topology of this branched cover of Ẽ_t be locally constant in t at
t = 0. That is a statement about how E_t meets the orbifold locus of M_{h,m}. I have not been able to derive it
from (R1)–(R2) in general, so I keep it as a hypothesis. It is the only purely technical hypothesis below.

### 2.3 The v-part of a point and its continuity

**Lemma Q.** Use the labelling of G' carried along by continuity (see the proof). For t in a neighbourhood of 0,
let Q_t ∈ M̄_{h,m} be the stable curve obtained from P_t by keeping the components at the vertices in W_v, with the
nodes corresponding to the edges in X′, and with the remaining half-edges as marked points. Then:
1. Q_t ∈ ∂M̄_{h,m}, and Y_t is one of its components;
2. Q_t ∈ closure(F_t) (closure in M̄_{h,m});
3. t ↦ Q_t is continuous along every path in Δ starting at 0.

*Proof.*
- (Local model, cited from memory as standard: plumbing coordinates, e.g. Arbarello–Cornalba–Griffiths,
  *Geometry of algebraic curves II*, Ch. XI.) Near P ∈ Δ_{G'}, M̄_g is the quotient by the finite group Aut(P)
  of a polydisc U_1 × D^{E(G')}. Here U_1 is a neighbourhood in the product of the factor moduli spaces of G', and
  s_e (e ∈ E(G')) are plumbing parameters. A point with exactly the s_e, e ∈ X′, nonzero lies in Δ_{G'/X′}. Its
  vertex-v part is the curve obtained by plumbing the W_v-components at the X′-nodes. As the point tends to P, this
  part tends in M̄_{h,m} to Q, because the same plumbing coordinates give the local chart of M̄_{h,m} at Q.
- In the chart, the points of Δ_{G_b} split into pieces according to the zero pattern of (s_e). Each piece is
  relatively open, since nonvanishing is an open condition and the number of zeros is |E(G_b)|.
- Hence on any connected subset of Δ_{G_b} ∩ chart the set X′ is constant. Apply this to the connected set
  ∪_{s ∈ [0,t]} H_s(b \ {P_0}) ∩ chart, which is homeomorphic to (punctured disc) × interval, for t on a short path.
  So the branch b_t := H_t(b) consists of points with the same smoothed-edge set X′, and (merge) persists. Paths
  lift through the finite quotient by Aut(P), so the labels of G' (and in particular the vertex i and the set W_v)
  can be carried continuously along a path; this is the labelling used in the statement.
- 1: X′ contains an edge at i, so Q_t has at least one node and lies in ∂M̄_{h,m}. Its component at i is the
  component of P_t at i, which is Y_t.
- 2: Points x ∈ b_t \ {P_t} tending to P_t lie in E_t, and π_v(x) ∈ F_t tends to Q_t, by the local model.
- 3: Q_t is obtained from P_t by a continuous operation in the chart, and P_t = H(P_0, t) is continuous. ∎

### 2.4 The theorem

**Theorem 1.** Assume (R1), (R2), (T0) and (Lev). Then Y_t = Y_0 for all t ∈ Δ, i.e. MS4 and the problem's claim hold.

*Proof.*
1. By Lemma R applied to (σ_t, F̂_t)_{t ∈ N}, each F̂_t(X_t) is one of finitely many curves φ(X_0) ⊂ M', with φ ∈ Φ.
   So F_t = p'(F̂_t(X_t)) is one of finitely many curves F^1, …, F^r ⊂ M_{h,m}.
2. Each closure(F^k) ⊂ M̄_{h,m} is a compact curve, so K := ∪_k closure(F^k) ∩ ∂M̄_{h,m} is a finite set.
3. By Lemma Q, Q_t ∈ K for t ∈ N. Along any path from 0 inside N, Q_t is continuous with values in a finite set,
   hence constant: Q_t = Q_0.
4. Y_t is a component of Q_t = Q_0 (Lemma Q.1), with its marked points labelled by half-edges. So Y_t lies in the
   finite set of pointed curves obtained from the components of Q_0 by all labellings.
5. Y_t is continuous (PR-1), so it is constant along each path. Hence Y_t = Y_0 on a neighbourhood of 0, and on all
   of Δ by the identity theorem (PR-1, Corollary). ∎

**Variant (Theorem 1′, the non-merging case, replacing PR-3 Lemma F).** Suppose instead that there are two pieces
E_0, E′_0 (at cusps P_0, P′_0 of closure(∂V_0)) with the vertex i intact, such that F_0 = π_i(E_0) and
F′_0 = π_i(E′_0) are curves satisfying (Lev) and (Teich) and whose closures have no common irreducible component.
Then Y_t is constant.

*Proof.*
- By Lemma R, F_t ranges over finitely many curves F^k, and F′_t over finitely many curves F′^l.
- As in Lemma Q, Y_t ∈ closure(F_t) ∩ closure(F′_t) (both limits at the vertex i are Y_t).
- For t near 0, F_t = F_0 and F′_t = F′_0. Indeed, the set of t ∈ N with F_t = F^k is closed: if t_n -> t and
  F_{t_n} = F^k, then for x ∈ E_0 the point π_i(H(x, t_n)) ∈ F^k tends to π_i(H(x,t)), so F_t ⊂ closure(F^k).
  Hence closure(F_t) = closure(F^k), as both are irreducible curves (F_t is a curve by Lemma R, and it is
  irreducible as the image of the irreducible E_t). Work with closures throughout. These finitely many closed sets
  (one for each distinct closure(F^k)) cover a connected neighbourhood and are pairwise disjoint, so
  closure(F_t) = closure(F_0) there. The same holds for F′_t.
- Hence Y_t lies in the finite set closure(F_0) ∩ closure(F′_0) ∩ M_{g_i,n_i}. It is continuous, hence constant. ∎

---

## 3. What remains: the condition (T0) on V_0

Theorem 1 shifts all the difficulty onto (T0), which concerns V_0 alone, together with the bookkeeping (Lev).
I could not prove (T0). Below I record what is needed and why it is not automatic.

**3.1 A meeting point is needed, and cusps need not exist.**
- The earlier sketch used cusps, i.e. points of closure(∂V_0) \ ∂V_0. But C_0 can be a complete curve in
  ∏_{j≠i} M_{g_j,n_j}, since M_{g_j,n_j} contains complete curves once g_j ≥ 3. Then ∂V_0 is compact and has no cusps.
- (T0) as stated in §2.2 allows G' = Γ, i.e. P_0 ∈ ∂V_0 itself, and Lemma Q covers this case unchanged.
- What is really needed is a second boundary branch b of closure(V_0) through a point of closure(∂V_0). Write
  D_0 := closure(V_0) \ V_0 for the boundary curve, which has pure dimension 1. The requirement is that the connected
  component of D_0 containing closure(∂V_0) is not just closure(∂V_0). I do not know a proof. A natural route:
  - Let D_0 be the support of an effective Cartier divisor on the normalisation of closure(V_0), namely the pullback
    of the boundary of M̄_g on a smooth level cover. Then D_0 is connected if that divisor is nef and big
    (numerical connectedness, cited from memory).
  - But the boundary divisor of M̄_g is not nef, so this route needs input specific to V_0.

**3.2 Merging is not automatic.** PR-3 §C gives a local model, s_γ = uv and s_e = v, in which every boundary branch
through the meeting point pinches all edges at i, so no branch merges at i. Nothing in (i), (ii), (R1) or (R2)
forbids this. If no branch merges, one is in the setting of Theorem 1′ or of a recursion (PR-3 §F).

**3.3 The Teichmüller property (Teich) of boundary pieces: heuristic only.**
- By Wright's correspondence (cited from memory: A. Wright, *Totally geodesic submanifolds of Teichmüller space*),
  V_0 is the image of a GL_2(R)-invariant subvariety 𝓜 of dimension 4, of rank 2 with no rel, in a stratum of
  abelian or quadratic differentials.
- By the boundary theory of Mirzakhani–Wright and Chen–Wright (also cited from memory), the limits of 𝓜 at
  1-dimensional boundary pieces E_0 should be invariant subvarieties of rank 1 in products of strata, on the
  components where the limit differential is nonzero.
- Projected to a single component, a rank-1 invariant subvariety should be a closed GL_2(R)-orbit, i.e. a
  Teichmüller curve.
- So (Teich) is expected for π_v(E_0) whenever the limit differential is nonzero on the components of v and π_v is
  not constant on E_0. Turning this into a proof requires the precise boundary theorems and a matching of the DM
  boundary piece E_0 with the WYSIWYG boundary. I have not done this, so (Teich) remains unproved.
- Moreover the constant component Y_0 is typically one on which the limit differential vanishes (it is "invisible"
  to 𝓜). In that case the merged vertex v must also contain components with nonzero limit differential, so that
  π_v(E_0) can be a Teichmüller curve. This is again not guaranteed.

**3.4 Why some global input like (T0) is unavoidable.** By PR-6 Theorem B, the problem's claim for a given V_0 is
equivalent to a global rigidity property of closure(V_0) ⊂ M̄_g. Lemma R is one such rigidity mechanism: rigidity of
Teichmüller-type boundary curves, even when their complex structure varies. It transfers to Y_t exactly through an
incidence like (T0).

---

## 4. Summary of status

**Proved here** (modulo the cited theorems of Royden, Thurston and Imayoshi–Shiga, the standard plumbing description
of M̄_g, and the earlier results PR-1, P-b Lemma 1 and Lemma B′):
- Lemma R: a holomorphic family of maps from varying finite-type Riemann surfaces into a fine moduli space M',
  all homotopic, one of which is a Teichmüller disc, has fixed domain up to biholomorphism and only finitely many
  possible images. No continuity in t, no Hodge theory, no Möller zero condition, no countability of Teichmüller
  curves.
- Lemma T (transport of irreducible boundary components and their normalisations under (R2)) and Lemma Q
  (continuity of the merged v-part Q_t, with Y_t a component of it).
- Theorem 1: (R1)+(R2)+(T0)+(Lev) imply MS4, hence the problem's claim. Theorem 1′ is the analogous non-merging
  version with two transverse Teichmüller-type projections through Y_0. These replace PR-3 Theorem E / Lemma F and
  remove their dependence on (H2′), (K) and (Ct).

**Not proved (open):**
- MS4 itself, for general V_0. This is a partial result in the sense of the task: it covers exactly those V_0 that
  satisfy (T0) (and (Lev)).
- (T0) for a general totally geodesic surface V_0, i.e. the existence of a boundary branch meeting closure(∂V_0) that
  merges vertex i into a vertex v whose projection is a Teichmüller curve (§3.1–3.3).
- (Lev): local constancy in t of the level-cover pullback of E_t -> M_{h,m}.
- No counterexample was found either. Constructing one would require a totally geodesic V_0 with a stratum-preserving
  deformation moving Y_0 (PR-6), and Theorem 1 shows that such a V_0 must violate (T0) or (Lev).

=== END OF ANSWER round5_q2 ===


