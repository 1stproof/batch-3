# round10_q9: attempt on (Rig) / (Rig-w) via image-level rigidity

## Status / plan (written first)
Plan:
1. Make the "countability + continuity" part of the named approach (item 1) rigorous at image level, with no orbifold bookkeeping. Statement attempted: Lemma CD below. It turns out to apply to any vertex set M, so it covers joint images too.
2. Test the Hodge-theoretic half of item 1 (Möller's characterisation) at map level and at image level, and decide what it can and cannot give.
3. Item 2 (the other vertices): record what Lemma CD reduces (Rig) to, and why that reduction is not yet a proof.

Final status: **(Rig) and (Rig-w) are not proved.** The following are proved:
- a clean dichotomy (Lemma CD);
- a reformulation of (Rig-v) and of (Rig) as "countable-class membership for uncountably many t" (Cor. CD1, CD2);
- a proof that map-level Hodge theory cannot reach (Rig-v) (Prop. MH, which depends on a prior result, Prop X, that I have not re-checked).

What remains open is listed in §6.

Readings (R1) and (R2) are adopted throughout. G is a product-type stratum (the case relevant to Δ_Γ). E_0 is a piece, E_t := H_t(E_0), and W ⊂ ∏_w M̄_w × Δ is the irreducible 2-dimensional analytic set of Lemma R0. It is proper over Δ, and W_t = closure(E_t) (R7-5 L1, product case). These are prior results; I re-use them and do not re-prove them.

## 1. Lemma CD (countable dichotomy for image curves)

For a set M of vertices, write pr_M : ∏_w M̄_w → ∏_{u∈M} M̄_u, and K^M_t := pr_M(W_t). The special case M = {v} gives K^v_t. The case M = M(E) gives the joint image K(E_t).

**Lemma CD.** Let C ⊂ ∏_{u∈M} M̄_u be a closed analytic set, and put T_C := {t ∈ Δ : K^M_t ⊂ C}. Then exactly one of the following holds:
- (a) T_C = Δ;
- (b) T_C is a closed discrete subset of Δ.

In case (a), if C is an irreducible curve and K^M_t is a curve for some t, then K^M_t = C for all t.

*Proof.*
- Put Z_C := {(x,t) ∈ W : pr_M(x) ∈ C}. This is a closed analytic subset of W. Moreover t ∈ T_C ⟺ W_t ⊂ Z_C.
- **Case Z_C = W.** Then T_C = Δ.
- **Case Z_C ≠ W.** W is irreducible of dimension 2, so dim Z_C ≤ 1.
  - Let t ∈ T_C. The fibre W_t is a nonempty pure 1-dimensional analytic set (E_t is a curve), and it lies in Z_C. Each irreducible component of W_t is therefore a 1-dimensional irreducible analytic subset of the analytic set Z_C, which has dimension ≤ 1. So it is an irreducible component of Z_C, and it is contained in the fibre over t.
  - Z_C is closed in W, hence proper over Δ. For a compact set Q ⊂ Δ, the preimage of Q in Z_C is compact, so it meets only finitely many irreducible components of Z_C (irreducible components are locally finite).
  - Components that lie in fibres over different times are different. So only finitely many t ∈ T_C lie in Q. Hence T_C is closed and discrete.
- **The last sentence.** K^M_t is irreducible, being the image of the irreducible W_t: E_t = H_t(E_0) is irreducible by Lemma S″ of round8_q7, a prior result. Its dimension does not depend on t (L1′ of R7-5: a vertex is non-constant along E_t for one t iff for all t; prior result). So if K^M_t is a curve contained in the irreducible curve C, then K^M_t = C. ∎

**Corollary CD1 (countable classes).** Let 𝒞 be a countable set of irreducible curves in ∏_{u∈M} M̄_u. If K^M_t ∈ 𝒞 for uncountably many t ∈ Δ, then K^M_t = K^M_0 for all t.

*Proof.* We have {t : K^M_t ∈ 𝒞} ⊂ ∪_{C∈𝒞} T_C. A countable union of closed discrete subsets of Δ is countable. So some T_C is uncountable, hence not discrete. By Lemma CD, T_C = Δ and K^M_t = C for all t; in particular C = K^M_0. ∎

**Corollary CD2 (Teichmüller vertex; image level, no orbifold bookkeeping).** Let v be a Teichmüller vertex of E_0 (Theorem TV). Then the following are equivalent:
- (i) (Rig-v): K^v_t = K^v_0 for all t;
- (ii) K^v_t is a Teichmüller curve for uncountably many t;
- (iii) K^v_t is a Teichmüller curve for all t in some open subset of Δ.

*Proof.*
- (i) ⇒ (iii) holds because K^v_0 is a Teichmüller curve by Theorem TV.
- (iii) ⇒ (ii) is trivial.
- (ii) ⇒ (i) is Corollary CD1 with 𝒞 the set of closures of Teichmüller curves in M̄_v. This set is countable. *Cited from memory:* every Teichmüller curve is defined over a number field (McMullen, via rigidity; also Möller). An algebraic subvariety of the projective variety M̄_v defined over Q̄ is one of countably many. ∎

**Remark.**
- Corollary CD2 replaces the "continuity in t" step of item 1 of the named approach, and the analytic continuation step of Theorem L / Cor. G1. The type jump at t = 0 plays no role in it, because it compares closed image sets only. This is the second suggested way round the obstacle in item 1 ("compare … only through image curves").
- What remains of item 1 is exactly to show (ii): **the image curves K^v_t are Teichmüller curves for many t.** Nothing in the earlier rounds or in this one establishes that.
- The same argument applies to Y_t in the original problem: if Y_t lies in a countable set for uncountably many t, then Y ≡ Y_0. This is immediate from R-Hol in any case.

## 2. Item 1 at map level: Möller's characterisation cannot give (ii) through the maps f_t

**Proposition MH.** Fix a generic time t ∉ D (Lemma G). Consider f_t = π_v ∘ ν_t : O_t → M_v, with the minimal orbifold structure O_t and the lift F_t : H → T_v. Then the following are equivalent:
- (1) the weight-one VHS pulled back by f_t (on a finite cover of O_t without orbifold points) contains a rank-2 maximal-Higgs summand;
- (2) (H_0) holds at time t, i.e. F_t is an isometric embedding onto a Teichmüller disc.

Consequently, by Cor. G1, "map-level maximal Higgs at one generic t" already implies (Rig-v). Conversely, at a map-level type jump of the kind in Prop X of R7-7 (reported there as a jump at which the image stays constant), (1) fails at every generic t, even though (Rig-v) holds.

*Proof (uses Möller's theorem, cited from memory: Möller, "Variations of Hodge structures of a Teichmüller curve", JAMS 2006).*
- (2) ⇒ (1). Möller's theorem, applied to the Teichmüller curve, gives a maximal-Higgs rank-2 summand L. Under (2), f_t is an orbifold-unramified covering of the Teichmüller curve, and pulling back along it preserves maximality: the Higgs field θ : L^{1,0} → L^{0,1} ⊗ Ω^1(log) stays an isomorphism under unramified pull-back.
- (1) ⇒ (2). By Möller's theorem, maximal Higgs forces the period map of L to be a local isometry onto H. The ω-direction then generates a Teichmüller disc, and the lift F_t is the Teichmüller embedding composed with that isometry, hence unramified.
- **Prop X.** Suppose f_t factors as (Teichmüller curve map) ∘ h_t, with h_t a branched cover of orbifolds that is ramified at moving points. At a ramification point x of order e > 1, the Higgs field of h_t^*L, as a map L^{1,0} → L^{0,1} ⊗ Ω^1, vanishes to order e − 1. So h_t^*L is not maximal Higgs.
- Uniqueness of L: any rank-2 summand that is maximal Higgs would give, by Möller, a Teichmüller embedding lift, contradicting ramification. ∎

**Consequence.** The map-level form of item 1 ("show f_j(E_t) is Teichmüller via Möller for the pulled-back VHS") proves strictly more than is true in Prop X. So it cannot be the general route. Möller's characterisation has to be applied to the **normalised image curve** K̃^v_t with its own minimal orbifold structure.

## 3. Item 1 at image level: equivalent to excluding image-level jumps (sketch)

**Setup.**
- Let 𝓘 := (pr_v × id)(W) ⊂ M̄_v × Δ. It is irreducible, 2-dimensional and proper over Δ (Remmert).
- Let 𝓘^ν be its normalisation. For t outside a discrete set D_I, the fibre 𝓘^ν_t is the normalisation K̃^v_t of K^v_t. Reason: 𝓘^ν → 𝓘 is finite and bimeromorphic, and its non-isomorphism locus is a curve, which meets generic fibres in finitely many points.
- Lemma G's proof uses only an irreducible 2-dimensional analytic set that is proper over Δ, together with a fibrewise non-constant map to M̄_v. So it applies verbatim to 𝓘^ν. The minimal orbifolds O^I_t (t ∉ D_I) therefore all have one type and one monodromy ρ^I_*.
- By the argument of §2 (minimal orbifold of a Teichmüller curve normalisation = the Veech orbifold H/Γ′, since D is injective), K^v_t is a Teichmüller curve iff (H_0) holds for the image map at t.

**What follows.**
- By Cor. CD2, (Rig-v) ⟺ the image map is Teichmüller at one t ∉ D_I. That is, either all generic images are Teichmüller curves, or none is.
- Suppose L (the rank-2 summand on H/Γ′) is invariant under ρ^I_*, i.e. the cone generators produced at 0 by Cor. G3 preserve L. Then the Toledo invariant of ρ^I_*|_L is constant on Δ \ D_I. Milnor–Wood gives deg L_t^{1,0} ≤ −χ(O^I_t)/2 at generic t, while at t = 0 equality holds with −χ(O^I_0)/2.
- So, by the additivity of the Toledo invariant over S° and the bad discs (sketched, not checked in detail), Arakelov equality at generic t ⟺ χ(O^I_t) = χ(O^I_0) ⟺ **no image-level type jump at 0**.
- This is the image-level analogue of the §4 dead end of round7_q7. The Hodge route is equivalent to excluding image-level jumps; it gives no independent proof of that.

**The multiple-fibre phenomenon (why rigidity of K^v_0 alone cannot suffice).**
- Let m_0 be the multiplicity of the central fibre of 𝓘 along K^v_0.
- If m_0 > 1, then (Rig-v) fails by Lemma CD. Indeed, if K^v_t = K^v_0 for all t, then 𝓘 = K^v_0 × Δ, which has reduced central fibre.
- In general analytic geometry, rigid curves can be cycle-limits with multiplicity of moving curves. *Classical example, from memory:* a multiple fibre mF_0 of an elliptic surface. F_0 has torsion non-trivial normal bundle, so it is rigid, yet the nearby fibres are smooth curves converging to mF_0.
- So McMullen's rigidity of Teichmüller curves (a statement about maps from a fixed orbifold) does not by itself exclude m_0 > 1. Excluding it needs input specific to M̄_v or to V_t.
- After the base change t = s^{m_0} and normalisation, an m_0 > 1 scenario becomes a map-level family with reduced central fibre mapping with degree m_0 onto K^v_0. This family must have a map-level type jump: otherwise (O) holds, Lemma R* gives a constant image, and m_0 = 1, a contradiction. So the m_0 > 1 case is again a type-jump case.

## 4. Item 2 (other non-constant vertices): what Lemma CD gives

**Corollary CD3.** For a piece E_0 with non-constant vertex set M = M(E_0), (Rig) holds for E_0 iff the joint image K(E_t) belongs to some countable class of curves for uncountably many t.
- A natural countable class is: curves in ∏_{u∈M} M̄_u defined over Q̄.
- In particular, (Rig) for E_0 follows if K(E_t) is defined over Q̄ for uncountably many t.

*Proof.* "Only if" is trivial. "If" is Cor. CD1 with M = M(E_0). ∎

**Assessment.**
- At t = 0, I expect K(E_0) to be defined over Q̄ (boundary data of a totally geodesic surface). I have not proved this.
- For t ≠ 0 there is no reason for arithmeticity, because V_t is not totally geodesic.
- Examples Z and Z′ (round8_q9) satisfy every piece-level hypothesis and have K(E_t) defined over Q̄ only for countably many t. So, as before, the input must be global in V_t.
- Lemma Loc (round9_q9) shows that local input at boundary points of V_t is not enough either.
- None of the three candidate inputs listed in the task for item 2 produces such a countable-class membership:
  - multi-scale / affine-disc structure: it exists only at t = 0;
  - normal-bundle / plumbing ratios: empty in genus 0, per round8_q7;
  - Imayoshi–Shiga on the 2-dimensional family: the base complex structure varies, per round9_q9 §4.

## 5. A remark on the whole problem (same mechanism)

Lemma CD is a statement about cycle families, so it extends to closure(V_t) itself. By (R1), closure(𝒱) is an irreducible analytic set in M̄_g × Δ, proper over Δ. The same proof shows: if closure(V_t) belongs to a countable family of surfaces (e.g. surfaces defined over Q̄, or totally geodesic surfaces) for uncountably many t, then V_t is constant.

This strengthens Prop. TG of round9_q9: total geodesy is needed only for uncountably many t, not for all t, and the countable-metric-space argument is not needed. Combining it with countability of totally geodesic surfaces (cited from memory, as in round9_q9 §3) gives:

**Prop. TG′.** If V_t is totally geodesic for uncountably many t, then closure(V_t) = closure(V_0) for all t, hence Y_t = Y_0.

## 6. Final status

**Proved (given the cited prior results W, L1/L1′, Lemma S″ and the cited countability of Teichmüller curves):**
- Lemma CD and Corollaries CD1–CD3.
  - (Rig-v) ⟺ K^v_t is a Teichmüller curve for uncountably many t.
  - (Rig) for a piece ⟺ its joint image lies in a countable class (e.g. defined over Q̄) for uncountably many t.
  - Neither statement involves any orbifold bookkeeping or the type jump at t = 0.
- Prop. TG′ (strengthening of Prop. TG).
- Prop. MH:
  - map-level maximal Higgs at one generic t ⟺ (H_0) at that t;
  - so the map-level Hodge route (item 1 as stated) is too strong and fails in Prop X-type situations;
  - Möller must be applied to image normalisations.
  - This uses Möller's theorem from memory, and Prop X as reported in R7-7.

**Sketched only:**
- §3: at image level, the Hodge/Arakelov route is equivalent to excluding image-level type jumps (when L extends).
- §3: m_0 > 1 forces a map-level jump after base change.

**Not proved / open:**
- (Rig-v) in general, i.e. that K^v_t is a Teichmüller curve for many t. Equivalently: no image-level type jump at 0, and m_0 = 1.
- (Rig) and (Rig-w) for the other non-constant vertices; no global input found.
- Whether K(E_0) is defined over Q̄.
- Q1/Q2 of earlier rounds: realisability of moving deformations, and rigidity of totally geodesic surfaces under admissible deformations.

Overall: **not proved; open.**

=== END OF ANSWER round10_q9 ===
