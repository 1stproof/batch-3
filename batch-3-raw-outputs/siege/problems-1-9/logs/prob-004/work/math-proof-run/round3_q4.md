kind: attempt
Open question attempted: the cited input (R) of the assembly theorem (ledger entry 15) — derive the regularization properties (R1)-(R4) used, or weaken what the assembly needs.

# Context
A proof of the YES answer to the problem (stated after this query) uses an "assembly theorem", reproduced
verbatim below (between the ==== lines). It assumes (R): a regularization of an SC divisor C in the sense of
Tehrani-McLean-Zinger ("Normal crossings singularities for symplectic topology", Adv. Math. 2018), in the
specific form (R1)-(R4) stated in its Section 1, cited from memory. In particular it uses: compatible
tubular embeddings Psi_I of disc bundles of N_I = sum N_a|C_I, standard-form pullback of omega (R2), the
compatibility (R3) for I subset I' (Psi_{I'} = Psi_I composed with the induced map, metrics pulled back,
pi_{I'} = pi_{I'} o pi_I), and the domain conventions (R4) (U_I cap U_I' subset U_{I u I'}, empty if
C_{I u I'} empty; U_K cap C_c is the tube of C_{K u c} in C_c; z_c preserved by pi_K).

# Task
1. State, as precisely as you can, what TMZ prove: the definition of an omega-regularization for an SC
   divisor (and the overlap/compatibility conditions in it), and the theorem that after a deformation of
   omega through cohomologous symplectic forms keeping the divisor SC (supported near the divisor), a
   regularization exists. Note any differences from (R1)-(R4).
2. Derive (R1)-(R4) from that, or — for any part you cannot derive — show how the assembly theorem can be
   run with what is available (for instance: the assembly only uses (R2) at zero sections for tameness;
   could the tubular data be any system of compatible smooth tubular neighbourhoods, independent of omega,
   with omega-orthogonality only along strata? If so, prove that such a system exists after the TMZ
   deformation, or even directly, and check each use of (R) in the assembly).
3. Verdict: does the assembly theorem below hold with the input you have established? If you find any step
   of it that fails, say exactly which and repair it if possible.

==== assembly theorem (verbatim) ====
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

==== end ====
