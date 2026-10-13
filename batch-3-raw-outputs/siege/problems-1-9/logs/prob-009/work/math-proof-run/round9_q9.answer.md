# round9_q9: attempt on (Rig) / (Rig-w) / realisability question Q1

## Status / plan (written first)
Plan:
1. Check whether the "2-dimensional open part of V_t" (approach 1 of the task), used *locally*, can pin anything. Statement attempted: Lemma Loc below, a local realisation of a moving constant factor by germs of admissible families.
2. Check whether the t = 0 information (Corollary AR, approach 2) is strong enough to force the factor M_{g_i,n_i} to be 0-dimensional or Y_0 to be isolated. Statement attempted: Example AR-real.
3. Give the global reduction that is actually available: the claim holds if total geodesy propagates to all V_t.
4. Explain why the Hodge-theoretic and Imayoshi–Shiga routes do not reach the constant factor (dead end).

Final status: **(Rig) and (Rig-w) are not proved. Q1 is not decided.** See §6. Literature results are cited from memory and marked as such.

Readings (R1) and (R2) of the task are adopted throughout.

## 1. Lemma Loc: the conclusion is not local, even with the 2-dimensional open part included

**Setting.**
- Let P be a point of ∂V_0 := closure(V_0) ∩ Δ_Γ. Then every component of P is smooth, because P lies in the open stratum Δ_Γ.
- Write Def(P) = ∏_{w∈V(Γ)} D_w × ℂ^{E(Γ)}. Here D_w is a small Kuranishi ball, in the interior, of the pointed component (P_w, special points), and the s_e (e ∈ E(Γ)) are plumbing parameters.
- U = Def(P)/Aut(P) is an orbifold chart of M̄_g at P. After linearisation, Aut(P) acts on Def(P), permuting the factors D_w according to its action on V(Γ).
- Near P, the strata of M̄_g are the images of {s_e = 0 for e ∈ S} × ∏_w D_w, for S ⊂ E(Γ).

**Lemma Loc.** Assume dim M_{g_i,n_i} > 0, and that the stabiliser Stab(i) ⊂ Aut(P) of the vertex i acts trivially on D_i. This holds e.g. when (Y_0, special points) has no automorphisms, or only the generic ones of M_{g_i,n_i}. Then there is a holomorphic family Φ_t (|t| small) of stratum-preserving biholomorphisms of U with Φ_0 = id, such that V_t^{loc} := Φ_t(V_0 ∩ U) satisfies:
- the local versions of (i), (ii) and of smooth triviality;
- π_i(closure(V_t^{loc}) ∩ Δ_Γ) = {Y_0 + t a} for some fixed a ≠ 0 in a chart of M_{g_i,n_i}, so Y_t ≠ Y_0 for t ≠ 0.

*Proof.*
- Pick 0 ≠ a ∈ T D_i (a linear chart). For each coset σ·Stab(i) ⊂ Aut(P), put a_{σ(i)} := σ_*a ∈ T D_{σ(i)}. This is well defined because Stab(i) acts trivially on D_i.
- Define Φ_t on Def(P) as translation by t·a_{w} in each factor D_w with w ∈ Aut(P)·i, and the identity on all other factors and on ℂ^{E(Γ)}.
- By construction Φ_t commutes with Aut(P), so it descends to U.
- It preserves each stratum, because these are coordinate subspaces in the ℂ^{E(Γ)}-factor times the full product of the D_w.
- Hence H_t := Φ_t is a smooth trivialisation that maps strata to strata. So (i), (ii) hold locally.
- The trace on Δ_Γ is Φ_t(∂V_0 ∩ U), whose i-coordinate is Y_0 + t a. ∎

**Consequence.** No argument that uses only germs of V_t, together with their 2-dimensional open part, at individual boundary points can prove the problem, (Rig) or (Rig-w). This sharpens round8_q9: Examples Z and Z′ were piece-level only, whereas Lemma Loc includes the 2-dimensional open part.

So approach 1 of the task has to use features that are global along whole compact curves. The normal-bundle constraint of round8_q7 §4 (Prop. N) is of that kind: it uses the compactness of the normalised piece C. As recorded there, however, it is empty when g(C) = 0.

**Open (Q-semi-global).** Does Φ_t extend to a stratum-preserving family on a neighbourhood of the whole compact curve closure(∂V_0) in M̄_g? If it does, the problem's claim is not even semi-global: only the part of V_t far from Δ_Γ can enter. The obstruction is of cohomological type, roughly a class in H^1 of the normal sheaf of the stratum along the curve. I have not computed it.

## 2. Corollary AR does not make the constant factor rigid at t = 0 (Example AR-real)

Recall Corollary AR (R8-10 §6). If vertex i carries η ≢ 0 at some scale, then Y_0^{cη̄/|η|} = Y_0 in T(Σ_i) for all |c| < 1. One might hope this forces dim M_{g_i,n_i} = 0, or makes Y_0 an isolated point of the locus it defines. Both hopes fail.

**Example AR-real (proved).** Let Σ_i have genus 0, with special points z_1, …, z_{n−1} ∈ ℂ and ∞ (n ≥ 4). Let η = dz², which has a pole of order 4 at ∞ and is holomorphic and nonzero on ℂ.

Claim: Y^{cη̄/|η|} = Y in T(Σ_i) for all |c| < 1 if and only if the points z_1, …, z_{n−1} lie on one real line.

*Proof.*
- η̄/|η| = dz̄/dz. So the affine deformation is realised by the real-linear map L_c(z) = z + c z̄, whose Beltrami coefficient is c. It fixes ∞ and sends z_k to z_k + c z̄_k.
- Equality in moduli means L_c(configuration) = A(configuration) for a complex affine map A, because Möbius maps fixing ∞ are affine. With A_k := z_k − z_1, this means
  (A_k + c Ā_k)/(A_2 + c Ā_2) = A_k/A_2 for all k.
- Clearing denominators, this holds for a given c ≠ 0 iff Ā_k A_2 = Ā_2 A_k, i.e. iff A_k/A_2 ∈ ℝ. So the condition is collinearity, and when it holds it holds for every c.
- Passing from moduli to T(Σ_i): c ↦ [Y^{cη̄/|η|}] ∈ T(Σ_i) is continuous on the connected unit disc, takes values in the discrete fibre of T(Σ_i) → M_{0,n} over [Y], and equals Y at c = 0. So it is constant. This is the same argument as in the proof of AR. ∎

So for n ≥ 4 the locus allowed by AR (for this type of η) is the real-collinear locus. It has positive real dimension n − 3, so Y_0 is not isolated in it.

**Remark (what AR would give if it held at all t).** In this example the AR-locus is a totally real subset; for n = 4 it is λ ∈ ℝ. Suppose AR held for every t, with η of this type. Then t ↦ Y_t would be a holomorphic map, by R-Hol, into a totally real set, hence constant. But AR at time t needs V_t to be totally geodesic, which is exactly what is not assumed. This is the second route of §3.

## 3. The reduction that is available: propagation of total geodesy

**Proposition TG (conditional; uses cited results).** Suppose every V_t, t ∈ Δ, is totally geodesic. Then closure(V_t) = closure(V_0) for all t, and in particular π_i(∂V_t) = {Y_0}.

*Proof.*
- **Countability (cited from memory).** A totally geodesic complex submanifold V ⊂ M_g of dimension ≥ 2 is determined by the closed GL₂(ℝ)-invariant set M_V of quadratic differentials whose Teichmüller discs are tangent to V. Indeed V is the projection of M_V, and M_V is a union of orbit closures. The relevant sources are Eskin–McMullen–Mukamel–Wright for the setting, and Eskin–Mirzakhani–Mohammadi with Filip for orbit closures (via the canonical double cover for quadratic differentials). Orbit closures are affine invariant submanifolds, and there are only countably many of them (they are defined over ℚ̄). Hence the set 𝒯 of totally geodesic subvarieties of M_g of dimension ≥ 2 is countable. I cite this chain from memory; the correspondence between totally geodesic submanifolds and invariant sets of differentials in particular should be checked.
- **Continuity.** By (R2), H is a homeomorphism of the compact space closure(V_0) × Δ̄′ (Δ′ a smaller disc) onto its image. So t ↦ closure(V_t) is continuous for the Hausdorff metric d_H on compact subsets of M̄_g.
- **Conclusion.** A countable metric space is totally disconnected: for x ≠ y, only countably many radii r are of the form d(x,z), so some r < d(x,y) avoids them, and the ball B(x,r) is clopen. The continuous image of the connected Δ in the countable space (𝒯, d_H) is therefore a point. Hence closure(V_t) = closure(V_0), so ∂V_t = ∂V_0 and Y_t = Y_0. ∎

So the problem reduces to the following statement, which is presumably also what the source paper ultimately wants:

**(TG-prop)** Total geodesy of V_0 propagates along admissible deformations.

This is the 2-dimensional analogue of the rigidity of Teichmüller curves. For curves it is known; I recall it from memory, by McMullen's and by Möller's arguments. Möller's route runs as follows:
- the rank-2 sub-local system L ⊂ R¹f_*ℂ belonging to the Teichmüller curve is topological;
- by Deligne's semisimplicity it underlies a sub-VHS for every member of a deformation;
- its Arakelov equality deg L^{1,0} = −χ/2 is an equality between topological invariants;
- so it persists, and Möller's characterisation (maximal Higgs ⇒ Teichmüller curve) gives total geodesy of every member.

**Route M (sketch, not proved).** For a 2-dimensional V_0, the analogue would need two things:
- (a) a Hodge-theoretic characterisation of totally geodesic surfaces by conditions that are topological or closed under deformation, e.g. a sub-VHS on which the Higgs field / second fundamental form satisfies an equality of Chern numbers;
- (b) the persistence of these conditions under (R1)/(R2).

I do not know such a characterisation in dimension 2 and did not establish one. This is the global input that, in my view, the problem needs. It is consistent with Lemma Loc, which says the input cannot be local.

## 4. Dead end: Hodge rigidity and Imayoshi–Shiga do not see the constant factor

- **Local system along ∂V_t.** Near ∂V_t, take the punctured tubular neighbourhood U*_t of the boundary divisor in a log-resolution of closure(V_t). Write N for the logarithm of the unipotent part of the monodromy around ∂V_t; it is Σ_e m_e N_e with the m_e topological (round8_q7 §4(a)).
- **The Y_t-part of the limiting MHS.** Gr^W_1 of the limiting MHS is ker N / im N ≅ ⊕_w H¹(P̄_w). Its summand H¹(Ȳ_t) is a sub-quotient local system on ∂V_t with **finite** monodromy, because the factor i is constant along ∂V_t. The positions of the special points of Y_t sit in the W_0 / W_2 extension data, again with finite monodromy along ∂V_t.
- **Why rigidity fails here.** After a finite cover these are *constant* variations, and a constant VHS on a fixed lattice can vary freely: every point of the period domain is a constant VHS. Deligne's rigidity (uniqueness of the Hodge structure on an irreducible local system with infinite monodromy, up to shift; Deligne 1987, from memory) and Imayoshi–Shiga / Arakelov–Parshin finiteness (as used in L2 and Prop. F) apply only to *non-isotrivial* data with infinite monodromy. Those tools pin moving vertices and never the constant one.
- **Where the pinning would have to come from.** Pinning Y_t must use how this constant sub-quotient sits inside the global local system on V_t, whose monodromy ρ(π₁V_0) is fixed and large. That is a statement about the extension of the boundary data into the interior of V_t, which is global.
- **The 2-dimensional Imayoshi–Shiga.** Applied to the whole family V_t → M_g, Imayoshi–Shiga would need a fixed complex structure on the base. The complex structure J_t := H_t^*(structure of V_t) on the smooth manifold V_0 varies with t, so the theorem does not apply. (Approach 3 of the task fails at this point.)

## 5. On Q1 (realisability of Z′-type deformations)

- A realisation needs a non-trivial admissible deformation of V_0 itself.
- By §3, such a deformation cannot consist of totally geodesic surfaces.
- If totally geodesic surfaces are rigid as subvarieties (expected, by analogy with Teichmüller curves), then no admissible non-trivial V_t exists, and the problem is vacuously true. I could neither prove nor refute this rigidity.
- By Lemma Loc, local realisations exist at every boundary point. So Q1 is a genuinely global question, about the extension of local deformations to closed subvarieties of M_g. I have no construction of a non-trivial global deformation of any known totally geodesic surface, e.g. the flex or gothic loci of EMMW (cited from memory), and no proof that none exists. **Q1 remains open.**

## 6. Final status

**Proved:**
- **Lemma Loc** (§1). Under the mild automorphism hypothesis stated there, at every point of ∂V_0 there are local admissible deformations, including the 2-dimensional open part, along which the constant factor moves. Hence (Rig), (Rig-w) and the problem's claim are not consequences of local data at boundary points. This sharpens Examples Z/Z′ of round8_q9, which were piece-level only.
- **Example AR-real** (§2). Corollary AR does not force dim M_{g_i,n_i} = 0, and does not isolate Y_0. For genus 0 with η = dz², the AR-locus is the totally real collinear locus.
- **Countable-space step of Prop. TG** (§3): a continuous family in a countable metric space is constant.

**Conditional / cited from memory:**
- **Prop. TG.** If all V_t are totally geodesic, the claim holds. This relies on the countability of totally geodesic subvarieties of dimension ≥ 2, via EMMW and EMM/Filip.

**Sketched only:**
- Route M: propagation of total geodesy via a Hodge-theoretic characterisation, in the style of Möller.

**Dead ends (with reasons):**
- Hodge rigidity and Imayoshi–Shiga do not reach the constant factor, because its sub-quotient has finite monodromy (§4).
- 2-dimensional Imayoshi–Shiga fails because the base complex structure varies (§4).

**Not proved / open:**
- (Rig) and (Rig-w) for every admissible family: **not proved**.
- Q1, the realisability of Z′-type deformations by an admissible global V_t: **open**.
- (Q-semi-global): extension of the local deformations of Lemma Loc to a neighbourhood of closure(∂V_0).
- (TG-prop): propagation of total geodesy, equivalently, for the purposes of this problem, rigidity of V_0 under admissible deformations.
- A Hodge-theoretic characterisation of totally geodesic surfaces that is stable under deformation (Route M (a)).

Overall: **not proved; open.**

=== END OF ANSWER round9_q9 ===

