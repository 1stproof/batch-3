# round13_q6: attempt on (Refl), the reflection case of MS11♭

**Status line.** NOT PROVED. What this file gives:
- (1) an exact equivariance lemma (Lemma E), which disposes of every h that stabilises the relevant sheet;
- (2) a local normal form at generic points of the mirror curve c̃, under an explicit smoothness hypothesis (Sm), with a dichotomy (Prop. D). Case I is harmless. Case II is the only surviving local mechanism. A numerical criterion forces case I whenever k ∤ M;
- (3) the exact point where the planner's "two sides of c̃" mechanism (sketch item 3) breaks down: in case II the mirror of h *detaches from the boundary* for t ≠ 0. There is an explicit chart-level model of this, consistent with every local constraint, including Lemma TG at t = 0;
- (4) the global necessary condition that a failure forces;
- (5) a list of open items.

Readings (R1), (R2) and the notation of the task file are used throughout. G := Aut(Q) acts on Def(Q) × Δ_ε by g·(p,t) = (gp, t). No result is cited from the literature except standard facts named where they are used (Cartan linearisation, Weierstrass preparation), which I cite from memory.

---

## 1. Lemma E (equivariance of persistence sets)

**Lemma E.** Let g ∈ G and let c̃ be a lifted branch at Q.
1. g maps Ñ_c̃ onto Ñ_{g c̃}, and maps anchored sheets of c̃ bijectively onto anchored sheets of g c̃.
2. For every anchored sheet T, P(gT) = g·P(T).
3. If g fixes T pointwise, then F_{gx}(p) ≅ F_x(p) (as pointed curves, for some ordering) at every (p,t) ∈ T at which x is intact.
4. Items 2 and 3 also hold for any irreducible 2-dimensional germ T (for example a local branch of an anchored sheet at a point (p_0,0) ≠ (0,0)), with P(T) defined in the same way.

*Proof.*
- (1) The set q^{-1}(H((c∖Q)×Δ_ε)) ∩ (B×Δ_ε) is G-invariant, because q∘g = q and B is G-invariant. So g permutes its connected components and sends the one containing c̃∖{0} to the one containing g c̃∖{0}. Being a biholomorphism, g preserves closures, irreducible components, and the property "contains c̃×{0}" (sending it to "contains gc̃×{0}").
- (2) g acts on the universal family over Def(Q), covering its action on the base. For p ∈ Def(Q) it gives an isomorphism C_p → C_{gp} that sends the component with label x to the component with label g·x. Here G acts on the labels V(G_Q) through its action on the dual graph of Q, and s_{g e}(gp) = 0 iff s_e(p) = 0, so intactness is transported.
  - Let x ∈ P(T) and (p,t) ∈ gT. Then (g^{-1}p, t) ∈ T, so x is intact at g^{-1}p and F_x(g^{-1}p) ≅ Y_t.
  - Hence gx is intact at p and F_{gx}(p) ≅ F_x(g^{-1}p) ≅ Y_t, with the special points transported (the definition allows some ordering).
  - So gx ∈ P(gT). The reverse inclusion follows by applying this to g^{-1}.
- (3) This is the same computation with gp = p.
- (4) Only the G-action and the universal family were used. ∎

**Corollary E1 (sheet-stabilising reflections are harmless).** In (Refl)(a), let L be an x-good lift-curve lying in an anchored sheet T, with x ∈ P(T) (P(T) = C(L) on boundary-type sheets, as recorded in the task file). If h(T) = T, then hL ⊂ T and x ∈ P(T). So h carries L to a lift-curve inside a sheet on which x **is** persistent, and in addition hx ∈ P(T).
- In the (NRT-config) of the planner's sketch, the sheet carries x with F_x ≅ φ(t) non-constant and y = h^{-1}x with F_y ≡ Y_0. If h fixes that sheet T, or merely stabilises it, Lemma E(2) gives h^{-1}x ∈ P(T): F_y ≅ Y_t on T, so Y_t ≅ Y_0 up to reordering for all t. That puts Y_t in a finite set, so Y would be constant (entry 19), which contradicts the hypothesis "Y non-constant".
- **Hence any failure of (Refl)(a) needs h ∉ Stab(T) for every anchored sheet T carrying x along the relevant lift-curves.** The same holds for the local branches of T at generic points of c̃ (Lemma E(4)).

---

## 2. Local normal form along the mirror c̃ and the dichotomy

**Setting of this section.**
- h ∈ G with h(S) = S, h|_S ≠ id, and h fixing the boundary curve c̃ ⊂ S pointwise (case (a)).
- E_c ⊂ E(G_Q) is the set of edges with s_e ≡ 0 on c̃, and N_c := ∏_{e∈E_c} s_e.
- p_0 is a generic point of c̃∖{0}: it lies on no other lifted branch, at p_0 the curve c̃ is smooth and the germ (S,p_0) is smooth, and Stab_G(p_0) = Stab_pt(c̃).
- X is a 3-dimensional irreducible component of q^{-1}(closure 𝒱) ∩ (B×Δ_ε) with X ⊃ S×{0} and h(X) = X. (h(X) = X is automatic if S×{0} lies in only one 3-fold component.)
- k ≥ 2 is the order of h|_S.
- M := ord_{c̃}(N_c|_S) = Σ_{e∈E_c} ord_{c̃}(s_e|_S) ≥ 1.

**Hypothesis (Sm) (extra; not known in general).** At (p_0,0), X is smooth and t|_X is a submersion, with X ∩ {t=0} = S near p_0 (reduced).

**Lemma LN (normal form).** Under (Sm) there are holomorphic coordinates (z,σ,t) on X near (p_0,0) such that:
- t is the time coordinate;
- S = {t=0} and c̃×{0} = {σ = t = 0};
- h(z,σ,t) = (z, ζσ, t), with ζ a primitive k-th root of unity.

Moreover N_c|_X = U·W, where U is a unit and W is a Weierstrass polynomial of degree M in σ with W(σ; z, 0) = σ^M. Finally:

  **W(σ) = σ^r · W_1(σ^k; z, t),** where 0 ≤ r < k, r ≡ M (mod k), and W_1 is a Weierstrass polynomial in τ = σ^k.

*Proof.*
- **Linearising h.** By Cartan's linearisation theorem (cited from memory: a finite group fixing a point of a complex manifold is linearisable there), h is linear in suitable coordinates at (p_0,0). The function t is h-invariant and dt ≠ 0 on T X, so the line T X / T S ≅ C (via dt) is a trivial representation. T S splits h-invariantly as T c̃ ⊕ ν, with h trivial on T c̃. On ν it acts by a primitive k-th root ζ: it is non-trivial because h|_S ≠ id and finite-order maps are determined by their derivative at a fixed point, and k is the order of h|_S.
- So Fix(dh) is 2-dimensional, and Fix(h) ∩ X = D is a smooth surface tangent to T c̃ ⊕ (an invariant complement of T S). Take linear coordinates (z, σ, w) with D = {σ = 0}.
- **Making t a coordinate.** h-invariance of t gives t = f(z, σ^k, w). Since dt|_{T D} ≠ 0 and t vanishes on c̃×{0} ⊂ D, we may replace w by t.
- **The function N_c.** Each g ∈ G permutes the divisors {s_e = 0}, so s_e∘h = (unit)·s_{π(e)}, where π is a permutation of E_c (h fixes c̃ pointwise, so it preserves its pattern). Hence N_c∘h = v·N_c with v a unit.
- **Weierstrass form.** At t = 0, N_c|_S = (unit)·σ^M. Weierstrass preparation in σ gives N_c|_X = U·W.
- **The shape of W.** ζ^{-M}W(ζσ) is again a Weierstrass polynomial in σ, and it differs from W by a unit. By uniqueness in the preparation theorem it equals W. Write W = Σ_j a_j(z,t) σ^j. Then a_j(ζ^j − ζ^M) = 0, so a_j = 0 unless j ≡ M (mod k). Hence W = σ^r W_1(σ^k). ∎

**Lemma B0 (boundary branches near (p_0,0)).** Let U be a small neighbourhood of (p_0,0). Every irreducible component B of X ∩ {N_c = 0} ∩ U has the following properties:
- it is a local branch at (p_0,0) of an anchored sheet of c̃;
- all s_e, e ∈ E_c, vanish on B;
- B ∩ {t=0} = c̃ near p_0.

*Proof.*
- By (R2), closure(𝒱) ∩ (∂M̄_g × Δ) ∩ q(U) = H((c ∩ U')×Δ) for a small neighbourhood U' of Q' := q(p_0). Here we use that p_0 is generic, so c is the only boundary branch of closure V_0 at Q'. H preserves strata, so q(B) lies in the stratum of c, and every s_e, e ∈ E_c, vanishes on B.
- The set B ∩ {t=0} is ≥ 1-dimensional (a hypersurface section of a surface through (p_0,0)) and lies in S ∩ ∂ = c̃ near p_0.
- B ∖ {t=0} is connected (an irreducible germ minus a proper analytic subset) and lies in q^{-1}(H((c∖Q)×Δ_ε)). Its closure meets c̃∖{0} ⊂ Ñ_c̃. So B ⊂ closure(Ñ_c̃), and B lies in some irreducible component T of it containing c̃×{0}. ∎

**Proposition D (dichotomy under (Sm)).** Let D = Fix(h) ∩ X = {σ = 0}. Then D is a smooth surface, transverse to {t = 0}, with D ∩ {t=0} = c̃ near p_0. Exactly one of the following holds.
- **Case I (σ | W, i.e. r ≥ 1 or W_1(0;z,t) ≡ 0).** D ⊂ X ∩ {N_c = 0}. So D is a local branch at (p_0,0) of an anchored sheet T_D of c̃, and h fixes D pointwise. By Lemma E(3,4), P(D) is h-invariant, and on D one has F_{hx} ≅ F_x at every point where x is intact.
- **Case II (σ ∤ W; this forces k | M).** For t ≠ 0 small, D_t := D ∩ {t} is a curve in the interior part q^{-1}(V_t) that converges to c̃ as t → 0. So V_t contains a curve q(D_t) of smooth curves admitting the automorphism h, accumulating on c as t → 0. The boundary branches near (p_0,0) are the branches of {W_1(σ^k) = 0}, and h permutes them.

In particular: **if k ∤ M, then case I holds.**

*Proof.* The statement about D is part of Lemma LN. If σ | W then D ⊂ {N_c = 0}, and Lemma B0 applies. If σ ∤ W then r = 0, so k | M. Moreover W_1(0; z, t) ≢ 0, while W_1(0; z, 0) = 0 (because W(σ;z,0) = σ^M). So N_c ≠ 0 on D at generic points with t ≠ 0, i.e. D_t is interior there. ∎

**Corollary D1 (what survives locally).** Assume (Sm) at a generic p_0. Let T be an anchored sheet with x ∈ P(T) and let B_x be any local branch of T at (p_0,0). The planner's configuration fails at T only if both of the following hold:
- B_x ≠ D (otherwise Lemma E(3) gives F_{hx} ≅ F_x ≅ Y_t on D);
- h(B_x) ≠ B_x (otherwise Lemma E(4)).

So, besides the condition h ∉ Stab(T) of Cor. E1, a failure needs the x-carrying local branches at generic points of the mirror to be non-fixed branches of {W_1(σ^k) = 0} that h moves.
- In Puiseux terms: B_x lies over a branch R of {W_1(τ) = 0} ⊂ (z,τ,t)-space, and the cyclic k-fold cover σ ↦ σ^k = τ restricted over R splits. For example, when R = {τ = t^a u} with u a unit, the cover splits only if gcd(a,k) > 1.
- In case I the fixed branch D is itself a boundary sheet, and on it hx is persistent iff x is.

---

## 3. Where the planner's mechanism (sketch item 3) fails

The planner's mechanism has two ingredients:
1. a loop around c in the coarse sheet Σ_0 = q(S) lifts in S to a path from p to hp, so h swaps the two sides of c̃;
2. H_t is a homeomorphism, so at time t the meridian of c_t should again swap the sides, which would force φ(t) ≅ Y_0.

Step 2 fails exactly in case II.

**The rigorous half (proved, under (Sm)).**
- Lift the meridian of c_t to Def(Q). Let it be a small loop at time t around c_t near Q'_t, radius r → 0, and let p* be the limit point of the lifts on a boundary branch.
- For r small, q^{-1}(small ball around q(p*)) is a disjoint union of small balls around the points of G·p*. So the lifted path stays in one of them, and its monodromy g satisfies g·p* = p*. That is, g ∈ Aut(curve at p*).
- If g moved x to y, then F_x(p*) ≅ F_y(p*), and φ(t) ≅ Y_0 up to reordering. So **step 2 would be correct if the monodromy of the small meridian of c_t were still h (modulo K_S)**.

**Why it is not.**
- The big loop (radius r_0 fixed, t → 0) does have monodromy in hK_S, by continuity of the endpoint and the fact that generic points of S have stabiliser K_S.
- But the big loop and the small meridian of c_t are homotopic in Σ_t ∖ c_t only through the interior branch locus of q, and in case II that locus contains q(D_t). Crossing it multiplies the monodromy by h^{±1}.
- So at time t the h-swap belongs to the mirror q(D_t), not to c_t. On each lift of c_t the labels x, y are no longer exchanged by anything.

**Chart-level model of case II (consistent with all local constraints, not globalised).**
- Coordinates. X = C³_{(z,σ,t)} ⊂ Def(Q)×Δ (locally near (p_0,0)), S = {t=0}, h(z,σ,t) = (z,−σ,t), so k = 2.
- Edges. E_c = {e, e'} with e at x and e' = h(e) at y, and s_e|_X = s_{e'}|_X = σ² − t² (up to units). Then M = 4, k | M, and r = 0: case II.
- At t = 0. N_c|_S = σ⁴, Fix(h) ∩ S = c̃ = {σ = 0}, and h acts on S as a reflection fixing c̃. This is allowed by Lemma TG ("a union of points and boundary curves").
- At t ≠ 0. The stratum of c is cut out on X by s_e = s_{e'} = 0, i.e. by {σ = t} ∪ {σ = −t}. These are two anchored sheets T_± = {σ = ±t}, both containing c̃×{0}, exchanged by h. Both e and e' are pinched on each, so H preserves the stratum, as (R2) requires.
- Labels. Put F_x = φ(t), F_y ≡ Y_0 on T_+. By Lemma E(2), F_y = φ(t), F_x ≡ Y_0 on T_−. This is consistent.
- The mirror. D = {σ = 0} has s_e = s_{e'} = −t² ≠ 0: it is interior.
- The coarse picture. With w = σ², Σ_t is (z,w)-space with boundary c_t = {w = t²} and an interior curve {w = 0} of h-symmetric smooth curves. So Σ_0 → Σ_t is the homeomorphism w ↦ w + t², which is compatible with (R2) locally. V_t is smooth (the quotient by a reflection is smooth).
- Conclusion of the model. x is persistent on T_+ but not on T_− = hT_+. This is exactly the (R-a) failure.

This model is chart-local, so by the task's rules it is not a counterexample. It shows that **no argument using only the germ of the family at points of c̃ can prove (Refl)(a)**, even with total geodesy at t = 0, since Lemma TG constrains only Fix(h) ∩ S. This agrees with round11_q7 §6 and round11_q1 §5, and pins the obstruction to the detaching mirror.

---

## 4. Global necessary condition for a failure (proved, under (Sm) at one generic point of c̃)

**Proposition G.** Suppose (Refl)(a) fails through h and mirror curve c̃, and (Sm) holds at some generic p_0 ∈ c̃. Then either:
- (i) the failure is through a moved branch of {W_1(σ^k)=0} in case I (Cor. D1); or
- (ii) case II holds.

In case II, for all small t ≠ 0, V_t contains smooth curves admitting an automorphism of the topological type of h, arbitrarily close to c_t. Their limit set as t → 0 contains c.
- So the closed analytic set 𝒜 := closure(𝒱) ∩ (M̄_g^{[h]} × Δ) has a 2-dimensional irreducible component 𝒟 with 𝒟_t ⊄ ∂M̄_g for t ≠ 0 and 𝒟_0 ⊃ c. Here M̄_g^{[h]} is the closed locus of stable curves with an automorphism of the type of h.
- The fundamental classes of the curves H_t^{-1}(𝒟_t) ⊂ closure(V_0) are constant in H_2(closure V_0) and equal [𝒟_0], a cycle that contains the boundary curve c with positive multiplicity.

*Proof.* Case II is Prop. D. 𝒜 is closed analytic because M̄_g^{[h]} is closed analytic: it is the image of a proper map from a moduli space of stable curves with a Z/k-action, which I cite from memory as standard. q(D) ⊂ 𝒜 is 2-dimensional, and its closure gives 𝒟. Constancy of homology classes in a flat analytic family of 1-cycles over a disc, transported by the homeomorphism H, is standard. ∎

**Remarks on using Prop. G (unproved routes).**
- At t = 0, the interior part of 𝒟_0 consists of h-symmetric curves of V_0. By total geodesy (the fixed set of h on the lifted Teichmüller disc structure), it is a union of Teichmüller curves and points. But 𝒟_0 may lie entirely in B_0, so this gives no contradiction.
- A contradiction would follow from a **negativity statement**: if the boundary curves of closure(V_0) through q(c) (or the relevant component of B_0) had negative definite intersection matrix, then an effective cycle supported on B_0 could not be homologous to the effective cycle H_t^{-1}(𝒟_t) meeting the interior.
  - Sketch: Z := 𝒟_0 = Σ a_j C_j. Then Z² = Σ a_j Z·C_j = Σ a_j W·C_j ≥ 0 when W shares no component with B_0, which contradicts Z² < 0.
  - Caveats: W may contain boundary components; the closure may be singular, so intersection numbers need Mumford's rational intersection theory on normal surfaces; and negativity is false in general (λ is positive on boundary curves whose moving part has positive genus). So this route is open and probably needs extra structure.
- Constancy of λ·𝒟_t and δ·𝒟_t gives numerical constraints only.

---

## 5. What is proved, what is not, open questions

**Proved.**
- Lemma E and Cor. E1: persistence sets are G-equivariant. Reflections, or any lost automorphisms, that stabilise the x-carrying anchored sheet (or one of its local branches) never cause a failure. In particular the planner's (NRT-config) is contradictory whenever h stabilises the sheet that carries x.
- Lemma LN, Lemma B0, Prop. D, Cor. D1, under (Sm) at a generic point of c̃:
  - the normal form, with N_c|_X = U·σ^r W_1(σ^k);
  - the dichotomy case I / case II;
  - **k ∤ M ⇒ case I**;
  - in case I the mirror is a pointwise-h-fixed boundary sheet on which hx is persistent iff x is;
  - a failure needs moved branches.
- Section 3: the precise failure point of the planner's sketch item 3 (the detaching mirror), with a chart-level model of case II consistent with (R2), the stratum condition and Lemma TG.
- Prop. G: the global necessary condition (a 2-dimensional family of h-symmetric curves of V_t degenerating onto c).

**Not proved.**
- (Refl)(a) in general.
- (Refl)(b) (h(S) ≠ S): only Lemma E applies, giving no failure when h stabilises the x-carrying sheet.
- The initial-twist clause τ ∉ Stab(b̃)Stab(x): not treated beyond Lemma E.
- MS11♭, hence MS8 and the problem's claim: not proved here.

**Open questions.**
1. Exclude case II globally. Show that a totally geodesic smooth V_0 admits no deformation satisfying (R1), (R2) in which the mirror of a reflection h of a sheet S, fixing a boundary curve, detaches into V_t. Prop. G's family 𝒟 with 𝒟_0 ⊂ B_0 is the object to rule out (negativity, or a Teichmüller-disc argument at t = 0 applied to H_t^{-1}(𝒟_t)).
2. Exclude, or realise globally, the moved-branch configuration of Cor. D1 in case I.
3. Remove hypothesis (Sm), e.g. by working on the normalisation of X. Its singular locus may contain the curve over c̃, so this is not automatic.
4. Settle whether k | M can actually occur for (S, h, c̃) arising from a totally geodesic smooth V_0. This is a t = 0 question about vanishing orders of plumbing coordinates along a mirror curve, and the plumbing description of Teichmüller discs near c (Lemma PA style) might decide it. If k ∤ M always held, case II would be excluded, and only the moved-branch configuration of case I would remain to exclude (Cor. D1).

Outcome: **not proved** (partial results above; the obstruction is sharpened to the detaching-mirror configuration of Prop. D, case II, plus moved branches).

=== END OF ANSWER round13_q6 ===
