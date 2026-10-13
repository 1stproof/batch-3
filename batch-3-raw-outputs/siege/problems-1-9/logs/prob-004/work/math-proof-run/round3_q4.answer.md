# round3_q4: what the assembly needs from (R), and how to supply it

## 1. What TMZ provide (cited from memory; treat as unverified)
Tehrani–McLean–Zinger, "Normal crossings singularities for symplectic topology" (Adv. Math. 2018). As I remember it:
- **Smooth regularization.** For a transverse collection {C_a} of closed submanifolds there is a system of tubular embeddings Ψ_I : N_I ⊃ dom → M with three properties: Ψ_I restricts to the identity on the zero section; dΨ_I induces the identity on normal bundles; Ψ_I^{-1}(C_a) = {z_a = 0} for a ∈ I. For I ⊂ I', the Ψ satisfy the overlap compatibility Ψ_{I'} = Ψ_I ∘ (induced map) on the overlap, where the induced map uses the canonical splitting N_{I'} = N_{I'−I}C_I|C_{I'} ⊕ N_I|C_{I'} and an identification N_I|C_I ≅ π^*(N_I|C_{I'}) near C_{I'}. This existence is a purely differential-topological statement, proved by induction on depth.
- **ω-regularization.** A smooth regularization together with Hermitian structures (ρ_{I;a}, ∇_{I;a}) such that Ψ_I^*ω = π^*ω|C_I + ½Σ d(ρ_a α_a), with the metrics and connections compatible under the identifications above.
- **Existence theorem (TMZ Theorem 2.13 or nearby).** Two spaces are weakly homotopy equivalent: the space of symplectic forms for which C is an SC divisor, and the space of pairs (ω, ω-regularization). Consequently, every such ω can be joined to a form ω' admitting an ω'-regularization by a path of forms keeping C SC. The deformation can be taken supported near C and cohomologous, because it is built from ω + dλ with λ supported near C.
- **Differences from (R1)–(R4).** The domain statements in (R4), "U_I ∩ U_I' ⊂ U_{I∪I'}" and "empty if C_{I∪I'} = ∅", are not stated in this form. They follow by shrinking the domains, using compactness and transversality. "z_c is preserved by π_K" is the overlap compatibility restricted to fibre coordinates. "U_K ∩ C_c is the tube of C_{K∪c} in C_c" follows from (R1) together with the compatibility.

## 2. Weakening: what the assembly actually uses
Going through the assembly theorem use by use:
- **ω enters only through Lemma B'.** That lemma needs two things along each stratum C_I: (i) the splitting TM = TC_I ⊕ ⊕_a dΨ(N_a) is ω-orthogonal; (ii) ω is positive on each dΨ(N_a) for its complex orientation. The Chern connections, the bundles O_M(c), Lemma F, Steps (a) and (b), and Lemma D use only the smooth data: the Ψ_I, Hermitian metrics ρ, the compatibility (R3), and the domains (R4). The metrics ρ can be arbitrary, provided they are compatible under the pullback identifications. Such compatible metrics can be built by induction from deep strata outward with cutoffs, exactly as in Lemma F.
- **So (R2) can be replaced by (R2'):** along each C_I, the fibre direction dΨ_I(N_a) equals the ω-orthogonal complement of TC_I inside TC_{I−a}.

**Lemma (R2' gives Lemma B's hypotheses).** Suppose the C_a intersect ω-orthogonally, meaning that at every point of C_I the subspaces (TC_{a})^{ω} for a ∈ I are pairwise ω-orthogonal. Then the subspaces V_a := (TC_I)^{ω} ∩ TC_{I−a} satisfy:
- TM|C_I = TC_I ⊕ ⊕_a V_a, and this splitting is ω-orthogonal;
- each V_a is symplectic, and ω on V_a is positive for the complex orientation of N_a.

*Proof.* Ω-orthogonal intersection means that V_a = (TC_a)^{ω}|C_I. These subspaces are pairwise ω-orthogonal by hypothesis, and they lie in (TC_I)^ω = ⊕_a (TC_a)^ω. Each V_a is symplectic because C_a is symplectic. The orientation of N_a = TM/TC_a is the one for which (TC_a)^ω is positive. ∎

*Realizing (R2').* The fibre direction N_a at the zero section is tangent to C_{I−a}, by (R1). A smooth regularization can be chosen with any prescribed complementary linearization along the strata, provided the choices are compatible. Here they are compatible, because V_a is defined intrinsically and is inherited along C_{I'} ⊂ C_I. This is a sketch, not a full proof.

*Getting ω-orthogonal intersections.* It suffices that ω admits an ω-regularization at all, because (R2) at the zero sections implies orthogonality. So the TMZ deformation theorem supplies this, too.

## 3. Verdict
I found no step of the assembly that fails, provided (R) is replaced by two inputs:
- a compatible smooth regularization satisfying (R1), (R3) and (R4), with (R4) obtained by shrinking;
- (R2') at the zero sections.

Both are available after the cited TMZ deformation: the full (R) gives them directly. The weakening makes the assembly independent of the connection and form parts of TMZ.

Remaining caveats:
- The TMZ existence/deformation theorem is cited from memory, and its exact numbering is unverified.
- Producing a compatible smooth regularization with prescribed linearization is sketched, not proved here.
- Step 1 (S1) is still open, as the assembly states.

=== END OF ANSWER round3_q4 ===
