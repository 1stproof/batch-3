# round7_q7: (O) / Lemma R without (O)

## Status and plan (written first, updated at the end)
Plan:
(1) Prove a *generic* version of (O): the orbifold type and the monodromy are constant for t outside a closed discrete set D ⊂ Δ (Lemma G).
(2) Derive the consequences: anchor transfer (Cor. G1), and the reduction "Lemma R can fail only if 0 is a jump time" (Cor. G2).
(3) Test the map-level conclusion of Lemma R* (f_t ∘ A_t = f_0) against an explicit global family in mechanism (ram) (Prop. X).
(4) Check the chain lemmas L1 and L2.

Convention used throughout. The cone order e_t(x) of the minimal orbifold structure O_t^min at x ∈ Ẽ_t is the least e ≥ 1 such that Φ_t lifts to an orbifold chart U → U/G_X of M_v after the base change w = s^e at x. Equivalently, it is the order of the local monodromy modulo the elements fixing the local lift pointwise. In the cases at hand this agrees with the definition of PR-K. Note that PR-E's "branch stabiliser" wording would give the wrong answer at coarsely ramified points.

## 1. A global family in mechanism (ram): Lemma R*'s map-level conclusion is false without (O)

**Proposition X.** There is a holomorphic family of maps f_t : Ẽ_t → M_v (t in a disc) with the following properties.
- (a) The source family is the trivial family Ẽ_t = ℂ.
- (b) f_0 = ι ∘ β_0, where ι is the normalisation map of a Teichmüller curve and β_0 is an orbifold-unramified cover, so (H_0) of PR-E holds.
- (c) For t ≠ 0 the type of O_t^min differs from that of O_0: it has two additional cone points of order 2. So (O) fails.
- (d) For t ≠ 0 there is NO biholomorphism A_t : Ẽ_0 → Ẽ_t with f_t ∘ A_t = f_0. This holds whatever the homotopy class.
- (e) Nevertheless f_t(Ẽ_t) = f_0(Ẽ_0) for all t, so the image-level conclusion of Lemma R holds.

This is a family of maps only. I have NOT checked that it arises from the boundary pieces of an admissible family V_t. So it is not a counterexample to Lemma R, to the problem, or to the weak form of L2. It does show that the conclusion of Lemma R* (and therefore the proof of L2, which uses A_t) cannot be obtained without (O) by any argument that only uses the data (source family, f_t, Teichmüller anchor at t = 0).

*Input (cited from memory).* There is a Teichmüller curve ι : C_V = 𝔻/Γ_V → M_v whose Veech group (in PSL_2ℝ) contains an elliptic element of order 2. Example: Veech's double regular pentagon (genus 2, ω ∈ H(2)), whose Veech group is the triangle group Δ(2,5,∞). We may take M_v = M_{2,1} with the unique zero of ω marked. Every affine map fixes the zero, so the Veech group is unchanged. The disc stays isometric in T_{2,1}, since its image in T_2 is isometric and the forgetful map is 1-Lipschitz. The coarse curve C̄_V is ℙ^1 with:
- an orbifold point y of order 2,
- an orbifold point z_5 of order 5,
- one cusp ∞.

Choose the coarse coordinate u with y = 0, z_5 = 1, cusp = ∞. ι is generically injective on C_V: two distinct Teichmüller discs meet in at most one point, because the Teichmüller geodesic through two points is unique, and ι is algebraic.

*The family.* For |t| < 1/2 put β_t(w) := w² + t, β_t : ℂ → ℂ = C_V (coarse), and f_t := ι ∘ β_t. This is holomorphic in (w, t).

*Proof.*
- **(a)** This is immediate from the definition.
- **(b)** β_0(w) = w².
  - Over y: u = w². The orbifold coordinate z at y satisfies z² = u, so z = w is a single-valued local lift, and w = 0 is not a cone point. β_0 is an orbifold covering there.
  - Over z_5: w = ±1, where β_0 is locally biholomorphic, so these are cone points of order 5.
  - Over ∞: one puncture.
  - Hence β_0 : O_0 → C_V, with O_0 = ℂ carrying two cone points of order 5, is an orbifold covering of degree 2. Check: χ(O_0) = 1 − 2·(4/5) = −3/5 = 2·χ(C_V), where χ(C_V) = 2 − 1 − 1/2 − 4/5 = −3/10.
  - So the lift of f_0 to orbifold universal covers is (isomorphism 𝔻 → 𝔻) followed by the isometric Teichmüller disc. This is (H_0).
- **(c)** Let t ≠ 0.
  - Over y = 0: the two points w = ±√(−t) are simple preimages. A local lift needs z = √(β_t(w)), the square root of a function with a simple zero. Every lift of a point of π(L) near X_y is of the form F(±z), because the order-2 elliptic element acts on L by z ↦ −z, and elements fixing L pointwise do not change this. So no local lift exists without the base change, and both points are cone points of order 2.
  - Over u = t (a regular point of C_V): w = 0 is an ordinary critical point of f_t, with cone order 1.
  - Over z_5: two cone points of order 5, as before.
  - So O_t^min = ℂ with cone orders (5, 5, 2, 2), and χ = −8/5 ≠ −3/5. The types differ.
- **(d)** Suppose ι ∘ β_t ∘ A_t = ι ∘ β_0. Then:
  - ι is injective off a finite set, so β_t ∘ A_t = β_0 on a dense open set, hence everywhere.
  - Compare critical values. β_0 has the single finite critical value 0. β_t ∘ A_t has the single finite critical value t, because A_t is biholomorphic.
  - So t = 0. ∎
- **(e)** β_t : ℂ → ℂ is onto, so f_t(ℂ) = ι(C_V) for all t. ∎

**What Prop. X teaches.**
1. In mechanism (ram) the right statement is image-level: "closure(π_v(E_t)) is constant" (Lemma R), not "f_t ∘ A_t = f_0" (Lemma R*). Without (O), the map-level statement can fail even with a smooth, trivial source family.
2. In the example, every map factors through the fixed curve C_V: f_t = ι ∘ β_t, with β_t a family of finite maps. If *all* vertex maps of a piece factor in this way, i.e. ν_t = Φ ∘ β_t for a fixed Φ : C̃ → Δ_G, then the weak L2 conclusion holds: the puncture values lie in Φ(punctures of C̃), a finite set. This suggests the following.

**Conjecture FAC (open).** Under (H_0) for (E_0, v), there are a fixed curve C̃, a map Φ : C̃ → Δ_G that is generically injective and non-constant, and a family of finite maps β_t : Ẽ_t → C̃ such that ν_t = Φ ∘ β_t for all t.
- Under (O) this holds with β_t = A_t^{-1}. Indeed, Lemma R* together with Step 5 of PR-D Lemma R and continuity in t gives ν_t ∘ A_t = ν_0.
- FAC implies Lemma R and the weak L2 conclusion.
- *Caveat on the first bullet.* The continuity in t of A_t is asserted, not proved. A_t is unique in its homotopy class, because isometries of a finite-area hyperbolic orbifold homotopic to the identity are trivial, and continuity should follow from this. This bullet is a sketch.

## 2. Lemma G: (O) holds generically in t

**Setting.**
- 𝓦 is the irreducible 2-dimensional family of Lemma R0, proper over Δ, and n : 𝓦^ν → 𝓦 is its normalisation.
- Φ := pr_v ∘ n : 𝓦^ν → M̄_v.
- Z := ∂(∏_w M̄_w) × Δ, and 𝓟 := n^{-1}(Z) is the "puncture locus", an analytic set of dimension ≤ 1.
- 𝓦^∘ := 𝓦^ν \ 𝓟. For every t, 𝓦^∘_t contains the normalisation of the lift of E_t as an open dense subset, outside the fibres listed in Step 1 below.
- Assume Φ is non-constant on fibres (v is non-constant along E_0; by L1 this holds for all t).

**Lemma G.** There is a closed discrete set D ⊂ Δ such that, for all t, t' in Δ \ D:
- the orbifold curves (Ẽ_t, O_t^min) and (Ẽ_{t'}, O_{t'}^min) have the same type, via a homeomorphism isotopic to the transported marking Ĥ_{t'} ∘ Ĥ_t^{-1};
- under it the monodromies agree: ρ_{t'} = ρ_t ∘ θ.

In other words, (O) of PR-E holds between any two times of Δ \ D.

*Proof (careful sketch).*

**Step 1 (level cover).**
- Let M′ := M_v[N] → M_v (N ≥ 3) be the level cover. It is a manifold, Galois with group G_N, taken modulo K.
- Let 𝓦′ be the normalisation of 𝓦^∘ ×_{M_v} M′, and 𝓦′_1 a connected component with stabiliser G_1 ⊂ G_N. Then 𝓦′_1 → 𝓦^∘ is finite, and it is the quotient by G_1 (normal spaces, generically Galois).
- By the Grauert–Remmert extension theorem for finite branched coverings of normal spaces (cited from memory: a finite branched covering over X \ A, with A nowhere dense analytic and X normal, extends to a finite branched covering of X), 𝓦′_1 extends to a normal space 𝓦̂ finite over 𝓦^ν, with G_1 acting.
- R̂ := ∪_{g ≠ 1} (image of Fix(g)) is analytic in 𝓦^ν by Remmert. It is the closure of the branch locus R.
- All of 𝓦^ν, 𝓦̂, 𝓟 ∪ R̂ are proper over Δ, because 𝓦 is.

**Step 2 (discrete bad set).** Let D be the set of t over which at least one of the following happens:
- (i) a fibre of 𝓦^ν or of 𝓦̂ contains a singular point of the total space, or a critical point of t on its regular part;
- (ii) 𝓟 ∪ R̂ has a vertical component, or a singular point, or a point where its horizontal part is ramified over Δ, or a point where two horizontal components meet.

Each of these is a closed analytic subset of a space proper over Δ, not containing whole fibres, so its image in Δ is closed and discrete:
- Normal surfaces have isolated singularities.
- A curve of critical points of t on a regular surface lies in a fibre: its tangent lies in ker dt, so t is constant along it.
- An analytic curve proper over Δ is étale over Δ off a discrete set.

**Step 3 (fibrewise description).** For t ∉ D, the fibre Ẽ_t := 𝓦^ν_t is a smooth compact curve, and 𝓦̂_t → Ẽ_t is the quotient of the smooth curve 𝓦̂_t by G_1. (A bijective holomorphic map of normal curves is an isomorphism.)
- Since M′ → M_v is the orbifold quotient map of the manifold M′, the local lifts of Φ_t to orbifold charts exist exactly on the local branches of 𝓦̂_t.
- So the cone points of O_t^min in 𝓦^∘_t are the points of R̂_t ∖ 𝓟, and the cone order is the effective order of the G_1-stabiliser of a preimage point.
- By (ii), these points move along the étale horizontal part of R̂ and never meet 𝓟 over Δ \ D. Their orders are constant along each branch of R̂ over Δ \ D: the stabiliser is constant along the smooth curve Fix(g) away from the intersections excluded by (ii).

**Step 4 (Ehresmann and monodromy).**
- Over Δ \ D, the pair (𝓦^ν, 𝓟 ∪ R̂) is a proper submersion with an étale horizontal divisor. So it is a locally trivial family of marked curves (Ehresmann with boundary, i.e. relative isotopy).
- Over Δ \ D, 𝓦̂ is likewise locally trivial, and G_1-equivariantly so.
- Δ \ D is connected (D is discrete in a disc), so all fibres over Δ \ D have the same type.
- The monodromy ρ_t, read off from the G_1-cover together with the monodromy of the family of curves pulled back from M′, is continuous in t on Δ \ D, as a map into the discrete set Hom(Λ_*, Mod_v)/conj. Hence it is constant.
- The type-preserving homeomorphisms obtained by Ehresmann are isotopic to the transported markings, since both vary continuously along paths in Δ \ D. ∎

**Remark.** 0 ∈ D is possible. In PR-K's local models (cross), (fix) and (ram), and in Prop. X, the type jumps exactly at t = 0. Theorem L (PR-K) shows that under (★) and (★∞) the type at 0 is the generic type (O_0 ≅ O_* via the transport), and (O) holds between 0 and nearby t.

## 3. Consequences of Lemma G

**Corollary G1 (anchor transfer).** Suppose that for some t_1 ∈ Δ \ D the map f_{t_1} satisfies (H_0), i.e. it has an isometric equivariant lift onto a Teichmüller disc. Then closure(π_v(E_t)) = closure(π_v(E_{t_1})) for all t ∈ Δ, and in particular for t = 0.

*Proof.*
- By Lemma G, (O) holds between t_1 and every t ∈ Δ \ D.
- Lemma R* (PR-E), applied with base point t_1 in place of 0, gives π_v(E_t) = π_v(E_{t_1}) for t in a neighbourhood of t_1. PR-E's proof never uses that the base time is 0.
- Step 5 of Theorem L (analytic continuation inside the irreducible 𝓦) extends the inclusion π_v(E_t) ⊂ closure(π_v(E_{t_1})) to all t ∈ Δ.
- Equality of closures follows from irreducibility and non-constancy, as in PR-D Step 6. ∎

**Corollary G2 (where Lemma R can fail).** If 0 ∉ D, more precisely if O_0 has the generic type O_* via the transport and ρ_0 corresponds to ρ_*, then (O) holds and Lemma R holds for (E_0, v).

Hence a failure of Lemma R requires both of the following:
- (J1) 0 is a *type-jump time*: (Ẽ_0, O_0) is not of type O_* compatibly with the monodromy;
- (J2) f_t satisfies (H_0) at NO t ∈ Δ \ D, by G1. So all generic members are non-Teichmüller.

Conversely, J1 alone does not make Lemma R fail: Prop. X has J1 but Lemma R holds.

**Corollary G3 (monodromy bookkeeping at a jump; proved).** Let B ⊂ Ẽ_0 be the finite set of points c at which some cone point of O_t^min (t ∉ D) accumulates as t → 0 without being the transport of a cone point of O_0 of the same order, together with the bad punctures.

Let S° := Ẽ_0 minus small discs (and end-neighbourhoods) around B, with the cone points of O_0 that lie in S°. Let P := π_1^orb(S°), and let q_0 : P → Λ_0 and q_* : P → Λ_* be the maps induced by inclusion; q_* uses the transport. Then:
- (1) ρ_* ∘ q_* ≡ ρ_0 ∘ q_0 modulo the pointwise stabiliser A := Fix(𝔇_0) ⊂ Mod_v (mod K).
- (2) For each c ∈ B ∩ Ẽ_0, the cone generators a_1, …, a_k of O_t^min inside the small disc around c satisfy ρ_*(a_i) ∈ Stab(X̂_c), a finite group. Their ordered product is ρ_*(δ_c) = ρ_0(q_0 δ_c) mod A, where δ_c is the boundary loop.
- (3) Im ρ_* is generated by ρ_0(Λ_0)·A and the finitely many finite groups ⟨ρ_*(a_i)⟩.

*Proof.*
- (1) On S°, Theorem L's local analysis applies (Prop. L1 and Cor. L2 at points satisfying (★), Prop. L3 at good ends). So the lifts F_t converge to some lift of f_0 uniformly on compact sets of the universal cover of S°. Lifts of f_0 differ only by elements fixing 𝔇_0 pointwise, and Hom(P, Mod) is discrete.
- (2) For small t, f_t maps the disc around c into the orbifold chart at X_c, so its local monodromy lies in Stab(X̂_c). The product relation is the orbifold disc relation.
- (3) P → Λ_* together with the cone generators at B generates Λ_*. ∎

In (cross) and (ram), δ_c is hyperbolic in Λ_* but ρ_*(δ_c) = ρ_0(q_0δ_c) = 1, so ρ_* is *not faithful*. In (fix), ρ_*(a_i) ∈ A.

## 4. Dead end: inequality-based global arguments cannot settle J1

This section explains why the suggested global inputs do not close the gap. All of them are one-sided in the wrong direction.

- **Royden domination on the level cover.** On the level-N cover the induced cover E′_t of Ẽ_t has χ(E′_t) = |G_1|·χ^orb(O_t^min). In all three mechanisms the generic type has *larger* hyperbolic area than O_0: creation and splitting both decrease χ^orb. As t → 0 the family E′_t degenerates (nodes in (cross)/(ram), a non-reduced fibre in (fix)), and E′_0 is the normalisation of the central fibre. Royden gives ℓ_{E′_t}(γ) ≥ ℓ_{E′_0}(γ) for curves γ away from the vanishing cycles, which is consistent with degeneration: pinching increases lengths of the other curves relative to the filled-in surface. Thurston's theorem needs equal types, so there is no contradiction.
- **Area / Gauss–Bonnet / Toledo.** Abelian case, with Im ρ_* preserving W = span(Re ω, Im ω) (this excludes (cross)). The Harish-Chandra corner entry composed with the period map gives a holomorphic retraction p : T → 𝔻 with p ∘ F_0 = id that is equivariant for W-preserving mapping classes. (Recalled; Kra's theorem that Carathéodory = Kobayashi on abelian Teichmüller discs is the classical form.)
  - For t ∉ D, h_t := p ∘ F_t is σ_t-equivariant, and Γ_* := σ_t(Λ_*) lies between the lattices Γ_0 and Γ_V.
  - A Rouché count in each bad disc and the degree count against 𝔻/Γ_* give deg(h̄_t) = [Γ_* : Γ_0].
  - Schwarz–Pick then yields only Area(O_t) ≥ [Γ_*:Γ_0]·Area(𝔻/Γ_*) = Area(O_0), with equality iff h_t is an isometry. In (ram) the inequality is strict and consistent, as Prop. X confirms.
- **Arakelov-type equality** (Teichmüller curves are maximal Higgs). Again the inequality is 2 deg L_t ≤ −χ^orb(O_t) with deg L_t constant, and −χ^orb(O_t) ≥ −χ^orb(O_0) at a jump. This is consistent.

Conclusion of the dead end. Every comparison of "source size" against "image size" is a Schwarz–Pick inequality, and the jump makes the source bigger. So a proof must use finer structure, for instance FAC-type factorisation or rigidity of the *image cycle*, not length or area inequalities alone.

**A possible route (not carried out): rigidity of the image cycle.**
- The cycles Z_t := pr_{v*}[𝓦_t] form an analytic family of cycles in M̄_v, and Z_0 = d_0·[C̄_V].
- Lemma R ⇔ supp Z_t = C̄_V for all t.
- Write d_0 = d·m_0, with d the generic degree of 𝓦 → 𝓘 := (pr_v, t)(𝓦) and m_0 the multiplicity of 𝓘_0 along C̄_V.
- If m_0 = 1, the normalised image family 𝓘^ν has *reduced* central fibre: div(t) is Cartier on a normal, hence Cohen–Macaulay, surface, so it has no embedded points, and it is generically reduced.
- In Prop. X, and in the local model (ram), m_0 = 1 and d = d_0 = 2. The (ram) jump of the source then becomes a type-preserving deformation of the image curve C_V, where (★) holds at y for the birational map ι. This is why (ram) "should" be harmless at image level.
- What is missing to run PR-K's Prop. L1 on 𝓘^ν: unibranchness of the central fibre, which Lemma N got from (R2), and (R2) is not available for the image family; and the case m_0 > 1.

(The computations in the second and third bullets of §4 are sketches. They explain why a method fails, and are not used anywhere.)

## 5. Check of the chain lemmas

**L1 (constancy persists): correct.** Details:
- Choose an affine open U ∋ Z_0 of the projective coarse space M̄_u, e.g. the complement of a hyperplane section avoiding Z_0.
- Properness of 𝓦 → Δ gives pr_u(𝓦_t) ⊂ U for |t| < ε. Each compact connected curve in 𝓦_t maps to a point of U.
- The set where (pr_u, t) has rank ≤ 1 is analytic and contains a nonempty open set of the irreducible 𝓦, so it is all of 𝓦.
- So the image I := (pr_u, t)(𝓦) is an irreducible analytic curve (Remmert) that surjects onto Δ. Being irreducible, it has no vertical components, so its fibre over each t is finite.
- Hence pr_u is constant on every connected 1-dimensional component of every fibre 𝓦_t.

**L2: the proof is valid only under (O).**
- It uses the biholomorphism A_t of Lemma R*.
- Prop. X shows that without (O) such an A_t need not exist, even for a trivial source family and with the image constant. So L2's *proof* cannot be extended to the jump case.
- Its *conclusion* (finitely many puncture values) is not contradicted: in Prop. X all puncture values are constant.
- Under (O) the remaining steps of L2 are fine:
  - g_0 has infinite monodromy, otherwise a lift to the bounded domain T_u on a finite cover would extend over the punctures and be constant;
  - Imayoshi–Shiga finiteness applies to the fixed source Ẽ_0.

**Chain steps 1–4.**
- Steps 1 and 4 are correct as written, given L2.
- Step 3 currently needs (O) for every piece. By Lemma G and Cor. G1/G2, (O) can be replaced by "0 ∉ D or some generic member is Teichmüller". The genuinely open case is J1 ∧ J2.

## 6. Summary

**Proved.**
- **Prop. X.** An explicit global family f_t = ι ∘ β_t (double regular pentagon Teichmüller curve with its Veech group Δ(2,5,∞), cited from memory; β_t(w) = w² + t) with a smooth trivial source family and an orbifold-unramified Teichmüller anchor at t = 0.
  - For t ≠ 0 it has orbifold type change (O fails) and no A_t with f_t ∘ A_t = f_0.
  - Its image is constant.
  - So the map-level conclusion of Lemma R* is false without (O). The (ram) mechanism globalises, at least as a family of maps.
  - Not checked: realisability as boundary pieces of an admissible V_t.
- **Lemma G** (careful sketch, using the Grauert–Remmert extension theorem and Ehresmann). (O) holds between any two times outside a closed discrete set D ⊂ Δ.
- **Cor. G1** (anchor transfer), **Cor. G2** (Lemma R holds unless J1 ∧ J2), **Cor. G3** (monodromy bookkeeping at a jump: ρ_* agrees with ρ_0 mod A off the bad discs; it is non-faithful in (cross)/(ram); its extra generators lie in finite isotropy groups).
- **Check of L1** (correct), and of L2 (its proof needs (O), and this is unavoidable by Prop. X).

**Not proved / open.**
- (Q1′) Lemma R (image constancy) in case J1 ∧ J2, i.e. when 0 is a type-jump time and no generic member is Teichmüller. This covers (cross), (fix), (ram) and failures of (★∞) that actually produce a jump.
- (Q2′) Conjecture FAC (factorisation ν_t = Φ ∘ β_t through a fixed curve). It would give both Lemma R and the weak L2 conclusion, and it holds in Prop. X and under (O) (sketch).
- (Q3′) The weak L2 conclusion (finitely many puncture values for other vertices u) without (O).
- (Q4′) Whether Prop. X-type families (or the (cross)/(fix) models) are realised by admissible families V_t.
- §4 explains why length, area and Arakelov inequalities cannot settle Q1′: at a jump the generic source orbifold is larger, and all those inequalities are consistent with that. A possible route via rigidity of the image cycle (reduced central fibre when m_0 = 1) is outlined but not completed.

=== END OF ANSWER round7_q7 ===
