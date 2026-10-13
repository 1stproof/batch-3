# Answer to round4_q9 (MS4: is t -> Y_t constant?)

## Plan / status (written first)
Target: MS4. In what follows "the claim" means: t -> Y_t is constant.
Outcome. I did not find a complete proof or a counterexample. What follows is:
- (A) a rigorous rigidity criterion: the claim holds as soon as some fixed finite-type Riemann surface maps holomorphically into V_t, continuously in t, and reaches ∂V_t at a puncture;
- (B) as a corollary, the claim (in fact V_t = V_0) when the family V_t has constant complex structure;
- (C) an explanation of why a counterexample must have varying complex structure, and why the boundary hypotheses make this hard. This part is heuristic.
The general case remains open.

Conventions. f_t : V_t -> M_g is the inclusion. "Homotopic" means homotopic as maps into the coarse space M_g.
Readings: I use (R1) and (R2) of the query file only where stated. R1 gives that closure(V_t) is analytic in the projective variety M̄_g, so V_t is quasi-projective by Chow's theorem.

## Cited theorem (from memory)
**Rigidity theorem (Arakelov–Parshin; Imayoshi–Shiga 1988, "A finiteness theorem for holomorphic families of Riemann surfaces"; McMullen's Bull. AMS survey states it in this form).** Let S be a Riemann surface of finite type, i.e. a compact Riemann surface minus finitely many points. Then:
- a homotopy class of maps S -> M_g contains only finitely many non-constant holomorphic maps;
- in particular, a non-constant holomorphic map S -> M_g is rigid.

The original statement is for holomorphic families. It says that two locally non-trivial holomorphic families of genus-g curves over S that are topologically equivalent are holomorphically equivalent. To pass from families to maps into the coarse space one goes to a finite level cover M_g[m], m ≥ 3. I take this reduction as standard and do not re-prove it here. (Caveat: if one insists on orbifold homotopy classes, the continuous families below give orbifold-homotopic maps as long as the homotopy lifts. For the families below the homotopy is a continuous family of holomorphic maps, and I take that to suffice.)

**Lemma 0.** Let F_t : S -> M_g, t ∈ Δ, be holomorphic maps with (s,t) -> F_t(s) continuous, and suppose F_0 is non-constant. Then F_t = F_0 for all t.

*Proof.*
1. Suppose F_t were constant for some t. Since F_t is homotopic to F_0, the map F_0 would induce the trivial orbifold-monodromy class. Then F_0 would lift, on a finite cover S' of S (also of finite type), to a holomorphic map into Teichmüller space T_g.
2. T_g is a bounded domain (Bers embedding). Bounded holomorphic functions extend over punctures, so the lift extends to the compact surface S̄'. A holomorphic map from a compact Riemann surface into a bounded domain is constant (maximum principle applied to the coordinate functions). So F_0 would be constant, a contradiction.
3. Hence every F_t is non-constant and homotopic to F_0. By the rigidity theorem, the set Φ of non-constant holomorphic maps homotopic to F_0 is finite.
4. The map t -> F_t is continuous into C(S, M_g) with the compact-open topology, which is Hausdorff. So it is a continuous map from the connected set Δ into the finite, hence discrete, set Φ. It is therefore constant. ∎

## Theorem A (pinning by a rigid test curve)
Suppose there are:
- a compact Riemann surface S̄, a finite set P ⊂ S̄, S = S̄ \ P, and a point p ∈ P;
- continuous maps h : S̄ × Δ -> M̄_g with each h_t := h(·,t) holomorphic;

such that h_t(S) ⊂ V_t, h_0|_S is non-constant, and h_t(p) ∈ ∂V_t for all t. Then Y_t = Y_0 for all t.

*Proof.* Lemma 0 applied to F_t = h_t|_S (which maps into V_t ⊂ M_g) gives h_t|_S = h_0|_S. By continuity h_t(p) = h_0(p) for every t. This point lies in ∂V_t, so it lies in Δ_Γ, and π_i of it is Y_t. Hence Y_t = π_i(h_0(p)) = Y_0. ∎

## Theorem B (constant complex structure ⇒ V_t = V_0)
Suppose there are biholomorphisms Φ_t : V_0 -> V_t with (x,t) -> Φ_t(x) continuous and Φ_0 = id. This holds, for instance, if 𝒱 -> Δ is holomorphically locally trivial. Then V_t = V_0 for all t, and hence Y_t = Y_0.

*Proof.*
1. V_0 is quasi-projective (R1 and Chow's theorem). Fix x ∈ V_0.
2. A general complete-intersection curve through x in a projective closure gives an irreducible algebraic curve C ⊂ V_0 through x that is smooth at x (Bertini).
3. Let ν : S -> C be its normalization, with finitely many points removed so that S is of finite type and still contains a point s_x with ν(s_x) = x.
4. F_t := Φ_t ∘ ν : S -> M_g is a continuous family of holomorphic maps. F_0 = ν is non-constant.
5. Lemma 0 gives Φ_t(x) = F_t(s_x) = F_0(s_x) = x.
6. Since x was arbitrary, V_t = Φ_t(V_0) = V_0. So closure(V_t) = closure(V_0), ∂V_t = ∂V_0 and Y_t = Y_0. ∎

**Corollary B'.** Suppose the closures form a smooth proper family of log pairs (V̄_t, D_t) (simple normal crossing boundary) and H^1(V̄_0, T_{V̄_0}(-log D_0)) = 0. Then the claim holds. The same is true if all the pairs (V̄_t, D_t) are biholomorphic to one another.
- *Proof sketch.* Kodaira–Spencer–Kuranishi theory for log pairs, or the Fischer–Grauert theorem in the second case (both cited from memory), makes the family locally holomorphically trivial near t = 0. Then Theorem B applies near 0. The identity theorem for the holomorphic map t -> Y_t (P-a Lemma 1) extends constancy to the whole disc.
- *Status.* This is conditional on the extra hypotheses: that the family is log-smooth, and that the H^1 vanishes or the pairs are isomorphic. These are not part of the problem.

## What this says about the general case
1. **Any counterexample needs varying complex structure.**
   - By Theorem B, the abstract complex manifolds V_t must vary in moduli.
   - By Theorem A, the curves in V_t that pass into ∂V_t (in the sense of A) must have complex structures that change with t, or must fail to deform continuously.
   - So the claim is equivalent to a global rigidity statement about V̄_t near ∂V_t. Local data (plumbing coordinates, monodromy, weight filtrations, hypothesis (ii) along Γ) cannot decide it. This matches P-a Obs. 4 and P-b, which I re-checked and agree with.
2. **Heuristic evidence that (i), (ii) and smooth triviality are very restrictive.** (Sketch; not used anywhere.)
   - *Example 1.* In M_{0,7}, take V_0 = {there is an involution with p1<->p2, p3<->p4, p5<->p6 and p7 fixed}. It is totally geodesic, being a covering construction from M_{0,5}. It has a boundary curve in D_{127} ≅ M_{0,4} × M_{0,5} with a constant factor, the harmonic 4-pointed sphere (Y_0 is non-trivial here).
   - The natural deformation moves p7 off the fixed point within the 3-fold W where only the pairs are imposed. Every such deformation makes p7 collide with ±a or ±b over curves inside V_0. So V_t would meet new boundary strata, and smooth triviality fails.
   - Equivalently: a deformation of this kind would be a section of the log normal bundle ≈ ψ_7^∨|_{V̄_0}, and ψ_7 is nef and big, so no such section exists. I also checked that a deformation with p7 = t·h(X) would need h/a and h/b to be bounded regular functions on an affine variety, which is impossible.
   - *Example 2.* In M_{0,6}, viewed as a blow-up of the Segre cubic, the involution locus is a hyperplane section. It moves in a P^4 of hyperplane sections. However, (i) forces V_t to contain the same boundary curves of the codimension-2 strata (6 lines) and to pass through the same 4 nodes. This seems to leave only V_0. I did not complete this verification.
   - These examples suggest that the claim is "true because V_0 is rigid under (i) and (ii)". That is far from a proof.

## What is proved / not proved
- **Proved** (modulo the cited rigidity theorem and the standard reduction from families to the coarse space):
  - Lemma 0;
  - Theorem A (claim holds whenever there is a continuous family of holomorphic test curves of fixed complex structure reaching ∂V_t);
  - Theorem B (claim holds, indeed V_t = V_0, whenever the V_t are biholomorphic to V_0 compatibly with the family).
- **Conditional:** Corollary B' (log-smooth family together with H^1(T(-log D)) = 0, or isomorphic pairs).
- **Also known (P-a Lemma 3, re-checked):** the claim holds if every V_t is totally geodesic (countability of totally geodesic subvarieties, cited from memory).
- **Heuristic only:** the examples above.
- **Open:**
  - (Q1) Is every totally geodesic surface V_0 ⊂ M_g rigid among families satisfying (i), (ii) and smooth triviality, i.e. is V_t = V_0? A yes answer implies the claim.
  - (Q2) Without such rigidity, does some global mechanism pin Y_t? Candidates are a Hodge-theoretic coupling of the interior VHS to Gr^W_1 ⊃ H^1(Y_t), or the incidence mechanism of P-d.
  - (Q3) Is there a counterexample? It would need V_t with varying complex structure, by Theorem B.
  - The problem's claim in full generality is NOT established here.

=== END OF ANSWER round4_q9 ===
