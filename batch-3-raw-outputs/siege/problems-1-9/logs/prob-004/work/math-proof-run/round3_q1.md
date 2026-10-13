kind: attempt
Open question attempted: independent audit of the claimed proof of the headline goal (ledger entry 16: the answer is YES).

# Task: referee a claimed proof, step by step

Below is a complete written proof chain claiming the answer to the problem (stated after this query) is YES,
under the conventions stated at the top of the chain. It cites two external results from memory: the
Tehrani-McLean-Zinger (TMZ) regularization theorem for SC divisors, and Donaldson-Auroux asymptotically
holomorphic transversality in the combined form (AH) stated in Part 1.

Your job: check EVERY inference of the chain, in order. For each lemma/step write "correct", "correct with
a fixable gap (and the fix)", or "wrong (and why)". In particular check, for Part 2 (assembly):
- that the "needed" index sets are closed under exactly the operations the induction uses (I u b for b in
  B_I; I u {b,c}; I u a^{+-} for a in I), and that every structure used at stage I has been built at a
  deeper stage;
- that the prescriptions of J_I near different deeper strata agree on overlaps (Lemmas Ch and D), and that
  J_I is omega|C_I-tame (Lemma B'), including the shrinking of tubes;
- that the divisor-induced bundles O_I(c) really have J_I-holomorphic transition functions, and that the
  verification of (C2) covers every case (c = b, c not in I u b, c in I), with the identifications
  compatible with those used in Lemma F;
- Lemma F (making the global isomorphism Phi_a pulled back near every stratum);
- the final reading-off of coordinates on M, including that z_k are C-independent and D_k = {z_k = 0};
- whether some earlier worry is really avoided: that on a stratum the holomorphic structures coming from
  several deeper strata must be glued relatively (a relative line-bundle-extension problem with a
  Pic^0-type obstruction). Decide whether the construction genuinely never has to extend a holomorphic
  structure relatively.
For Part 1 check Lemma 0, the integrality bookkeeping, and the symplecticity/positivity argument for the
new strata, and say whether the cited (AH) and (TMZ) statements are correct as stated (to your knowledge of
the literature: Donaldson 1996, Auroux 1997 GAFA and later, Tehrani-McLean-Zinger 2018 Adv. Math.).

End with an explicit verdict, one of:
 (V1) the chain proves the YES answer exactly as stated (modulo the cited results, which are correctly
      stated published theorems);
 (V2) the chain proves it modulo the cited results, but some cited statement is not (to your knowledge)
      published in that form — say exactly which part and whether you can supply a proof;
 (V3) there is a genuine gap — locate it precisely and, if you can, repair it.
Be concrete; do not re-derive the whole subject, but do not wave anything through.

## Conventions used by the chain
"Symplectic simple normal crossings (SC) divisor" is taken in the Tehrani-McLean-Zinger sense: finitely many
closed codimension-2 symplectic submanifolds D_i meeting transversally, every stratum D_I = cap_{i in I} D_i
symplectic, and the symplectic orientation of each stratum equal to its intersection orientation
(positivity). The "permitted deformation" of omega is a path of cohomologous symplectic forms along which D
stays SC. The required local coordinates: near a point lying on exactly the components D_k, k in K, with
r = |K|, there are smooth complex coordinates z_1..z_n with z_1..z_r J-holomorphic and D = {z_1...z_r = 0}
nearby; z_{r+1..n} only smooth.

The proof chain consists of two parts, written by two different authors: PART 1 (configuration lemma =
Step 1, hypothesis (S1) of Part 2) and PART 2 (assembly theorem: (S1) + TMZ regularization (R) => YES).
Both are reproduced verbatim below. Lemma A (used in Part 2) is proved in Part 2.

======== PART 1 (configuration lemma) ========
# round2_q3: the configuration lemma (Step 1)

Plan: build the configuration one level at a time. Before each level, re-regularize with TMZ; this is a permitted
deformation. Use one family of Donaldson–Auroux sections for each level. Integrality comes from the line bundle
P_k, whose class is an integral class rounded from k[omega]. The new strata are shown to be symplectic for the
actual current form omega: J is omega-compatible, and omega' is never used as the symplectic form.

## Cited results (from memory; stated as I use them)

**(TMZ)** Tehrani–McLean–Zinger. Let C be an SC divisor in (M, omega), with positivity. Then there is a path
omega_t, all cohomologous to omega, along which C stays an SC divisor (all strata symplectic and positive), such
that omega_1 admits a regularization of C. In particular, along each stratum the components meet
omega_1-orthogonally: in the model, T M|_{C_I} = T C_I + sum_i N_i is an omega_1-orthogonal splitting, and
T C_i = T C_I + sum_{j != i} N_j. I recall that the path keeps the class fixed and is supported near C. I am
quoting this from memory, so it is a hedge.

**(AH)** Donaldson's and Auroux's asymptotically holomorphic theory. I state it in the form needed here; it is
recalled, not proved.
- Setting: (M, omega) is closed, J is omega-compatible, and g = omega(., J .). Let E be a fixed Hermitian vector
  bundle. Let P_k be Hermitian line bundles with connections whose curvature F_k satisfies
  |F_k + 2 pi i k omega|_{C^r, g} = O(1), unrescaled. Let Sigma_1, ..., Sigma_m be closed submanifolds that are
  exactly J-complex.
- Conclusion: for k >> 0 there are sections s_k of E (x) P_k and an eta > 0 independent of k with the following
  properties. The sections are asymptotically holomorphic (rescaled metric kg: |s|, |nabla s| = O(1) and
  |dbar s|, |nabla dbar s| = O(k^{-1/2})). Their restrictions to every Sigma_j, and every sub-tuple of
  components, are eta-transverse to 0.
- The O(1) curvature error is O(k^{-1}) in the rescaled metric, so Donaldson's and Auroux's local estimates do
  not see it. That is the standard way of handling non-integral [omega], and twisting by a fixed E is part of
  Auroux's GAFA 1997 setting.
- Restricting to an exactly J-complex Sigma gives an asymptotically holomorphic sequence on (Sigma, J|, omega|).
  The localized reference sections centred at points of Sigma restrict to localized sections, so Auroux's
  globalization runs on Sigma.
- The finitely many conditions are achieved one after another. Each perturbation is smaller than half the
  transversality constant already obtained, and eta-transversality is open under C^1 perturbations of size
  < eta/2.
- I do not know a single reference stating exactly this combination. Every ingredient is standard, but this is
  the least verified input.

**Consequence (AH').** On the zero set Z of an eta-transverse asymptotically holomorphic section, restricted to
any J-complex Sigma, the tangent space T(Z ∩ Sigma) lies within angle O(k^{-1/2}/eta) of a J-complex subspace.
The reason is that the kernel of nabla s = del s + dbar s with |dbar s| << |del s| is close to ker del s, and
ker del s is complex.

## Lemma 0 (compatible J preserving a regularized SC divisor)

**Statement.** If the components of C meet omega-orthogonally (as after TMZ), then there is an omega-compatible
J for which every C_i is J-complex.

**Proof.**
1. At p in the open stratum of C_I, let S_p be the set of compatible J on T_pM that preserve every T_pC_i,
   i in I.
2. Any such J preserves W = T_pC_I. Because J is compatible, it also preserves W^omega, and hence it preserves
   N_i = T_pC_{I-i} ∩ W^omega.
3. Conversely, a compatible J on each block of the omega-orthogonal splitting W + sum N_i preserves all the
   T_pC_i. So S_p is the product of the spaces of compatible structures on the blocks, which is contractible
   and nonempty.
4. Proceed from the deepest strata upwards. If I' ⊂ I, then S_p^{I} ⊂ S_p^{I'}. The bundle of the S^{I'} over
   C_{I'} is locally trivial with contractible fibres, so the section already defined on C_I ∩ C_{I'} extends
   over C_{I'}. Finally extend to all of M (contractible fibres). ∎

## Lemma 1 (configuration lemma)

**Statement.** Let D be an SC divisor in closed (M^{2n}, omega). After a permitted deformation of omega (a
cohomologous path keeping D SC), there is a finite SC divisor C ⊇ D with the following properties:
- C is transverse, every stratum is symplectic, and every stratum is positively oriented.
- C has levels 0, ..., n-1, and D is level 0.
- Every component C_a of level l <= n-2 has two new partners P_a^+ and P_a^- of level l+1.
- PD[C_a] = PD[P_a^+] - PD[P_a^-] holds in H^2(M; Z), including torsion.

Finally, TMZ applied to C keeps D SC along the path, because C stays SC and D is a union of its components.

**Proof.** By induction on the level. Suppose C_{<=l} has been built and is SC for the current form omega_l.

1. *Regularize.* Apply TMZ to C_{<=l}. This is a permitted deformation, and D stays SC. Lemma 0 then gives an
   omega_l-compatible J_l for which all strata of C_{<=l} are exactly J_l-complex.

2. *Integrality.* The image Lambda of H^2(M; Z) in H^2(M; R) is a full lattice. Choose c_k in H^2(M; Z) whose
   real image lies within a fixed distance of k[omega_l]. Let eta_k be the harmonic representative of
   (c_k - k[omega_l])/k, so |eta_k|_{C^r} = O(1/k). Let P_k be a line bundle with c_1(P_k) = c_k, with a
   connection whose curvature is -2 pi i k(omega_l + eta_k). That curvature satisfies the hypothesis of (AH).

3. *The sections.* For each a of level l, let L_a be the line bundle with c_1(L_a) = PD[C_a] (which is integral).
   Apply (AH) with E = sum over a of (L_a + C), the bundle P_k, and the family Sigma given by all strata of
   C_{<=l} together with M itself. The result is sections s_a^+ of L_a (x) P_k and s_a^- of P_k.
   - Every sub-tuple, restricted to every Sigma, is eta-transverse.
   - Set P_a^± = Z(s_a^±).
   - Since the same P_k is used for both partners, PD[P_a^+] - PD[P_a^-] = c_1(L_a) + c_k - c_k = PD[C_a] in
     H^2(M; Z).

4. *Transversality.* Transversality of every sub-tuple on every Sigma is exactly transversality of the enlarged
   configuration C_{<=l+1}. The new hypersurfaces are distinct from each other and from the old ones, because
   they meet transversally.

5. *Symplectic and positive strata (for omega_l itself).*
   - By (AH'), each new stratum Z_S ∩ Sigma has tangent spaces within angle O(k^{-1/2}) of J_l-complex
     subspaces.
   - J_l is compatible with omega_l. So omega_l(v, J_l v) >= (1 - O(k^{-1/2}))|v|^2 on these subspaces, and
     they are symplectic for k large.
   - Every stratum is the transverse intersection of approximately complex subspaces. Its intersection
     orientation is therefore the complex orientation, which equals the symplectic orientation. This holds at
     the J_l-complex limit, and orientations are locally constant under a nondegenerate deformation.
   - omega' = omega_l + eta_k only shapes the curvature of P_k; it is never used as the symplectic form.

6. *Uniformity across levels.* Not needed. Each level gets its own TMZ step, its own J_l and its own k_l, and the
   old strata are exactly J_l-complex. This avoids the error that would build up if one J_0 had to serve every
   level.

7. *Termination.* Stop at level n-1, which needs no partners. Concatenating the TMZ paths gives a permitted
   deformation, along which every C_{<=l}, and hence D, stays SC. The last TMZ application regularizes all of C.
   ∎

## Status
- **Proved, modulo cited results:** Lemma 1 and Lemma 0. They depend on (TMZ), quoted from memory, including the
  claim that the path keeps the class fixed, and on the combined statement (AH).
- **Main open point:** a precise literature reference for (AH), or a full proof of it. It combines three things:
  transversality to finitely many J-complex submanifolds, twisting by a fixed bundle, and an O(1) curvature
  error coming from the non-integral class. Each ingredient is standard, but I could not cite them together.
- **Not addressed:** snags (i)–(iii) of the overall route, which concern Steps 2–4.


======== PART 2 (assembly theorem) ========
# round2_q4: the assembly lemma (Steps 2–4), proved assuming Step 1 and the TMZ regularization

## Summary
**Theorem.** Assume (S1), the configuration of Step 1, and (R), a TMZ ω-regularization of the SC divisor C. Both are stated precisely below; (R) is cited from memory. Then there is an ω-tame J on M with the required coordinates at every point. Here ω is the form after the TMZ deformation, which is a permitted deformation because C is SC along it, and hence so is D ⊂ C.

The proof makes two changes to the planner's outline.
- **Lemma C is not needed.** The connection used to build the connection-type almost complex structure J_∇ does not have to be the TMZ connection. Tameness depends only on zero-section data, and that data is the same for every connection (§3, Lemma B'). So we use Chern connections throughout, and we never deform ω after TMZ. Snags (ii) and (iii), and task item (5), disappear.
- **The bundle isomorphisms are built globally on M first (snag (i), item (4)).** Extending an isomorphism N_a|C_I → L stratum by stratum has an obstruction in H²(C_I, deeper strata; Z), which need not vanish. We avoid it by fixing one global smooth isomorphism Φ_a on M. We then make Φ_a "pulled back" near every stratum by modifications on the tubes U_K. The fibres of the tubes are contractible, so no obstruction arises there (Lemma F).

What remains open is Step 1 itself, which is assumed here, and the exact form of the cited TMZ statement (R).

## 1. Hypotheses

**(S1)** C = {C_a}_{a∈A} is an SC divisor in (M^{2n}, ω): transverse, every stratum C_I symplectic and positively oriented. D_i = C_i for i ∈ A_0 ⊂ A. There is a level function ℓ: A → {0,…,n−1} with ℓ^{-1}(0) = A_0. Each a with ℓ(a) ≤ n−2 has two partners a^+ ≠ a^- of level ℓ(a)+1. Every component of level ≥ 1 is a partner of exactly one parent p(b). Finally PD[C_a] = PD[C_{a^+}] − PD[C_{a^-}] in H²(M; Z).

**(R)** (TMZ, cited from memory). For every I with C_I ≠ ∅ there are:
- Hermitian metrics ρ_{I;a} on N_a|C_I for a ∈ I, where N_a := N_{C_a};
- an embedding Ψ_I of a disc-bundle neighbourhood of the zero section of N_I = ⊕_{a∈I} N_a|C_I onto an open set U_I ⊃ C_I, with Ψ_I = id on the zero section and dΨ_I inducing the identity on normal bundles.

These satisfy (R1)–(R4).
- **(R1)** Ψ_I^{-1}(C_a) = {z_a = 0} for a ∈ I.
- **(R2)** Ψ_I^*ω = π^*ω|_{C_I} + ½ Σ_a d(ρ_a α_a) for some unitary connections. In particular, along C_I the splitting TM = TC_I ⊕ ⊕_a N_a is ω-orthogonal, and each N_a is a symplectic plane on which ω is positive for the complex orientation.
- **(R3)** For I ⊂ I', near C_{I'} we have N_I|C_I ≅ π^*(N_I|C_{I'}) with metrics pulled back. Under N_{I'} = N_{I'−I}C_I|C_{I'} ⊕ N_I|C_{I'}, Ψ_{I'} equals Ψ_I composed with the induced map, and the projections satisfy π_{I'} = π_{I'}∘π_I on U_I ∩ U_{I'}.
- **(R4) Domains.** The tubes are as thin as needed. U_I ∩ U_{I'} ⊂ U_{I∪I'}, and this set is empty if C_{I∪I'} = ∅. U_K ∩ C_c is the tube of C_{K∪c} in C_c. The fibre coordinate z_c (c ∉ K) is preserved by π_K on U_K ∩ U_c.

Restricting (R) to a stratum C_I gives a regularization of the induced SC divisor {C_b ∩ C_I} in (C_I, ω|C_I). In particular the tube of C_{I∪b} inside C_I is the total space of N_b|C_{I∪b}, by (R3).

## 2. Local lemmas

**Lemma A** (from earlier work; proof rechecked). Let J_∇ be the structure on the total space of E = ⊕L_i → (B, J_B) that equals the horizontal lift of J_B on the horizontal subspace and i on the fibres. Let s_i be frames with ∇s_i = θ_i s_i, and let z_i be the fibre coordinates. Then:
- z_i is J_∇-holomorphic if and only if every θ_i is of type (1,0);
- the projection π is (J_∇, J_B)-holomorphic.

*Proof.* The horizontal subspace is ker(dz_i + θ_i z_i), since a section z s is parallel iff (dz + zθ)s = 0. ∎

**Lemma Ch (Chern connection on an almost complex base).** Let (B, J_B) be almost complex, and let L have a holomorphic structure: an atlas of frames s_α whose transition functions g, with s_α = g s_β, are J_B-holomorphic. Let h be a Hermitian metric with h_α = |s_α|². Then θ_α := ∂ log h_α defines a unitary connection whose connection forms are of type (1,0) in holomorphic frames.

If π: (B', J') → (B, J_B) is pseudo-holomorphic, the Chern connection of (π^*L, π^*h) is π^*∇^{Ch}.

*Proof.*
- *Well defined.* Here ∂ means the (1,0)-part of d. We have log h_α = log h_β + log g + log ḡ. Since g is holomorphic, d log g is of type (1,0); since ḡ is antiholomorphic, ∂ log ḡ = 0. Hence θ_α = θ_β + d log g. This is exactly the transformation rule for ∇s_α = θ_α s_α.
- *Unitary.* θ_α + θ̄_α = ∂ log h_α + ∂̄ log h_α = d log h_α, because log h_α is real.
- *Pullback.* π^* commutes with d and preserves types when dπ∘J' = J_B∘dπ. Hence ∂ π^* log h = π^* ∂ log h. ∎

**Lemma D (iterated connection structures).** Let E_1, E_2 → (B, J_B) carry connections ∇_1, ∇_2. Write J_1 = J_{∇_1} on the total space of E_1. The total space of E_1 ⊕ E_2 equals that of π_1^*E_2 → E_1. Then the structure built from (E_1, J_1) and π_1^*∇_2 equals J_{∇_1⊕∇_2}.

*Proof.* Let w ∈ T_{e_1}E_1, written w = h_1(v) + u with u vertical. The π_1^*∇_2-horizontal lift of h_1(v) is the (∇_1⊕∇_2)-horizontal lift of v. The lift of u is u itself, because its E_2-component is constant. Then
J_1 w = h_1(J_B v) + iu,
whose lift is the (∇_1⊕∇_2)-lift of J_B v plus iu. In both structures the E_2-fibres carry i. So the two structures agree. ∎

**Lemma B'** (tameness, for any connection). Let B ⊂ (X, ω) be a symplectic submanifold, and let Ψ be a tubular map with ω-orthogonal, ω-positive splitting along B as in (R2). Then for every connection ∇ and every ω|_B-tame J_B, Ψ_*J_∇ is ω-tame on a neighbourhood of B.

*Proof.* Along B, J_∇ = J_B ⊕ i ⊕ … ⊕ i, independently of ∇. For v = b + Σ n_a, orthogonality gives
ω(v, Jv) = ω(b, J_B b) + Σ ω(n_a, i n_a) > 0 for v ≠ 0.
Tameness is an open condition and B is compact. ∎

## 3. Bookkeeping

Call I ⊂ A **needed** if C_I ≠ ∅ and p(b) ∈ I for every b ∈ I with ℓ(b) ≥ 1. The empty set is needed, with C_∅ = M. Every subset of A_0 with nonempty stratum is needed.

Basic facts:
- If I is needed, b ∉ I, C_{I∪b} ≠ ∅, and either ℓ(b) = 0 or p(b) ∈ I, then I∪b is needed. Set B_I := {such b}.
- If I is needed and contains a component of level n−1, then I contains its whole ancestor chain, so |I| ≥ n. Transversality gives |I| = n, and C_I is a finite set.
- If I and I' are needed and C_{I∪I'} ≠ ∅, then I∪I' is needed.

**Global bundles (smooth).** For c ∈ A, let O_M(c) be π_c^*N_c on U_c, glued to the trivial bundle on M − C_c via the tautological section. Its canonical section s_c vanishes transversally exactly on C_c, and c_1 = PD[C_c].

Using (R3)/(R4) there are canonical isomorphisms O_M(c)|U_K ≅ π_K^*(O_M(c)|C_K):
- for c ∈ K, via N_c|C_c ≅ π^*(N_c|C_K);
- for c ∉ K, as bundles with section, via z_c ↦ z_c.

These isomorphisms are compatible for K ⊂ K'. Restricted to C_I:
- if c ∈ I, O_M(c)|C_I = N_c|C_I;
- if c ∉ I, O_M(c)|C_I is the divisor bundle of C_{I∪c} ⊂ C_I with section s_c.

Since c_1 agree integrally, choose a smooth isomorphism Φ_a^0: O_M(a) → O_M(a^+) ⊗ O_M(a^-)^* for each a with ℓ(a) ≤ n−2.

**Lemma F.** Φ_a can be chosen *pulled back*: Φ_a|U_K = π_K^*(Φ_a|C_K) for every K, after shrinking the tubes.

*Proof.* Order strata by decreasing codimension. Suppose Φ is pulled back near all strata deeper than C_K. Set u := Φ / π_K^*(Φ|C_K): U_K → C^*.
- u = 1 on C_K.
- Near any deeper C_{K'} ⊂ C_K, both maps are pulled back from C_{K'}, using π_{K'}∘π_K = π_{K'}. So u = 1 there.
- Fibres of U_K are discs, so f := log u is well defined by continuation from the zero section. It satisfies f = 0 on C_K and near deeper strata.

Replace Φ by e^{−χ f}Φ, where χ is a cutoff in the fibre radius, equal to 1 on a thinner tube and 0 near ∂U_K. This leaves Φ unchanged near deeper strata. Tubes of other strata of the same codimension meet U_K only near deeper strata (R4), where f = 0. ∎

## 4. The induction

We construct, for needed I by decreasing |I|:
- **(a)** an ω|C_I-tame almost complex structure J_I on C_I;
- **(b)** holomorphic structures ℋ_{I;a} on N_a|C_I for a ∈ I.

On 0-dimensional strata both are vacuous: every frame of a line counts as holomorphic.

The induction maintains three properties.
- **(C1)** For b ∈ B_I, near C_{I∪b} in C_I: J_I = J_∇, built from J_{I∪b} and the Chern connection of (ℋ_{I∪b;b}, ρ).
- **(C2)** For a ∈ I and b ∈ B_I: near C_{I∪b}, ℋ_{I;a} = π^*ℋ_{I∪b;a}.
- **(C3)** For a ∈ I with ℓ(a) ≤ n−2, ℋ_{I;a} = (Φ_a|C_I)^*(holomorphic structure of L_{I;a}), where L_{I;a} := O_I(a^+) ⊗ O_I(a^-)^* is defined below.

**Step (a): J_I.** By (C1), J_I is prescribed near each C_{I∪b}, b ∈ B_I.
- *Overlaps.* The tubes of C_{I∪b} and C_{I∪c} meet only near C_K, K = I∪{b,c}, which is needed. There, by (C1)/(C2) for I∪b, J_{I∪b} is J_∇ over C_K for N_c, and ℋ_{I∪b;b} = π^*ℋ_{K;b}. Lemma Ch says the Chern connection of the pulled-back structure is the pullback of the Chern connection. Lemma D then gives J_∇ over C_K for N_b ⊕ N_c with Chern connections. This is symmetric in b and c, so the prescriptions agree.
- *Tameness and extension.* By Lemma B' (inside C_I) the prescribed structure is tame near the deeper strata. Tame structures form a bundle with contractible fibres, so after shrinking the tubes, J_I extends to an ω|C_I-tame structure on all of C_I.

**Step (b): O_I(c).** For c ∉ I with I∪c needed, let O_I(c) be the divisor bundle of C_{I∪c} in C_I, with the following atlas:
- the frame s_c on C_I − C_{I∪c};
- on the tube, frames e_α with s_c = z^{(α)} e_α, where z^{(α)} is the fibre coordinate for a holomorphic frame of ℋ_{I∪c;c}.

By (C1) and Lemmas A and Ch, each z^{(α)} is J_I-holomorphic, and each ratio z^{(α)}/z^{(β)} = π^*g is J_I-holomorphic. So all transition functions are J_I-holomorphic. As a smooth bundle with section this is O_M(c)|C_I. No removable-singularity argument is needed, since the transitions are explicit.

For c ∈ I, set O_I(c) := (N_c|C_I, ℋ_{I;c}).

**Step (b): ℋ_{I;a}.** Define ℋ_{I;a} by (C3), proceeding in decreasing order of level within I. This uses ℋ_{I;a^s} only when a^s ∈ I, which has a higher level, and otherwise I∪a^s, which is needed and deeper. The recursion terminates because the levels are bounded and the level n−1 cases are finite sets.

**Verification of (C2).** Near C_{I∪b}, O_I(c) ≅ π^*O_{I∪b}(c) holomorphically, for each case:
- **c = b:** the divisor bundle of the zero section of a line bundle E is π^*E, with the tautological section, and the frames match.
- **c ∉ I∪b:** near C_{I∪b} the hypersurface C_{I∪c} is π^{-1}(C_{I∪b∪c}) by (R3)/(R4), and both bundles are defined by the same functions z_c.
- **c ∈ I:** this is (C2) for c, by induction on level.

Lemma F makes Φ_a|C_I equal to π^*(Φ_a|C_{I∪b}) under these same identifications. So (C2) holds for a.

## 5. Conclusion on M (I = ∅)

On M, B_∅ = A_0. Set J := J_∅, built by Step (a). Near D_K for K ⊂ A_0, applying Lemma D repeatedly shows that J is J_∇ on N_K over D_K, built from J_K and the Chern connections of the ℋ_{K;k}. By Lemmas A and Ch, the fibre coordinates z_k (k ∈ K) taken in holomorphic frames are J-holomorphic. They are C-linearly independent on vertical vectors, and D_k = {z_k = 0} by (R1).

Let p ∈ D_K lie on no other D_j. Take r = |K|, and complete z_k (k ∈ K) by π_K^* of arbitrary smooth complex coordinates on D_K; this is a chart because Ψ_K is a diffeomorphism. Away from D take r = 0.

J is ω-tame by Lemma B' near D and by the extension step elsewhere. ∎

## 6. Status
- **Proved, given (S1) and (R):** everything above.
- **Cited from memory:** (R), the TMZ regularization theorem, including the domain and compatibility conventions (R3)/(R4) as I have stated them. The only symplectic input used is the zero-section orthogonality and positivity in (R2).
- **Open, not addressed here:** Step 1, the existence of the configuration C with integral partner relations, all strata symplectic and positive, and a unique parent for each component.


======== END OF THE CHAIN ========
