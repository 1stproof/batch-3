# round1_q4: necessity (O1) and the search for a counterexample

Conventions are as in the query file. J is ω-tame and smooth. A local J-holomorphic defining function of D_i is a smooth z with dz∘J = i·dz, D_i = {z=0} locally, and dz surjective onto C along D_i.

## 1. O1, proved

**Lemma 1.** Let z and z' be J-holomorphic defining functions of D_i on a connected neighbourhood U. Then h := z'/z extends to a smooth, nowhere-vanishing J-holomorphic function on U. On D_i ∩ U we have dz' = h·dz.

*Proof.*
1. *h is smooth off D_i and bounded near it.* Because z is a submersion near D_i, we can take local coordinates (x_1, x_2, y) with z = x_1 + i x_2. The function z' vanishes on {x_1 = x_2 = 0}, so by Hadamard's lemma z' = a·z + b·z̄ with a, b smooth. Hence h = a + b·(z̄/z), which is bounded and smooth off D_i.
2. *b = 0 on D_i.* Apply ∂̄_J to z' = a z + b z̄ and restrict to D_i, where z = z̄ = 0. This gives 0 = b·∂̄_J z̄ = b·dz̄. Since z is J-holomorphic, dz̄ is J-antilinear and nonzero along D_i, so b = 0 there. Hence h → a along D_i, so h extends continuously and lies in L^∞.
3. *Removable singularity.* The set D_i has real codimension 2, hence zero capacity, so a bounded function cannot carry ∂̄_J h as a distribution supported on D_i. Concretely, test against the cut-offs φ_ε, which equal 1 outside an ε-tube and satisfy ‖∇φ_ε‖_{L^1} → 0. This gives ∂̄_J h = 0 in the sense of distributions on U.
4. *Smoothness.* The operator ∂̄_J on functions is overdetermined elliptic: its symbol is injective, and the second-order operator (∂̄_J)*∂̄_J has the symbol of the Laplacian. Elliptic regularity therefore makes h smooth.
5. *Conclusion.* On D_i, z' = h z gives dz' = h·dz. Since dz' ≠ 0 there, h does not vanish on D_i. Off D_i, h = z'/z does not vanish either. ∎

**Corollary 2 (holomorphic cocycle).** Suppose J has the required coordinates. Then:
- D_i is J-complex (it is a level set of a J-holomorphic submersion), so J_i := J|_{D_i} is an ω|_{D_i}-tame almost complex structure.
- dz identifies N_{D_i} with the trivial bundle, so the restrictions g_ab := h_ab|_{D_i} form a cocycle for N_{D_i}. Each g_ab satisfies dg∘J_i = i·dg, i.e. it is J_i-holomorphic.
- Consequently N_{D_i} → D_i admits a J_i-holomorphic cocycle for an ω_{D_i}-tame J_i.

**Further necessary conditions.**
- **(N1) Nijenhuis condition.** If f is J-holomorphic, then df(N_J(X,Y)) = 0 for all X, Y. This follows by expanding N_J and using df∘J = i·df together with d²f = 0. Hence:
  - dz_k(N_J) = 0 for all k ≤ r;
  - on D_i, dg_ab(N_{J_i}) = 0;
  - on any open set where some g_ab is a submersion, the image of N_{J_i} lies in ker dg_ab.
  For dim_R D_i ≥ 4 and generic J_i, N_{J_i} spans TD_i, which forces g_ab to be locally constant there. So for generic J_i, N_{D_i} would carry a locally constant cocycle, i.e. be flat, and c_1(N_{D_i}) ⊗ R would vanish. A non-flat normal bundle therefore requires a non-generic J_i whose Nijenhuis tensor degenerates on an open set.
- **(N2) Compatibility at crossings.** Take a point of D_{ij} with i ≠ j. Then z_j|_{D_i} is a J_i-holomorphic defining function of D_{ij} inside D_i. Restricting further to D_I, the cocycles of N_{D_i}|_{D_I} must be J|_{D_I}-holomorphic, and the identification N_{D_I} = ⊕_{i∈I} N_{D_i}|_{D_I} becomes a splitting of holomorphic cocycles. This applies Lemma 1 inside D_i.

Neither (N1) nor (N2) is an obstruction by itself: J_i may be chosen to be integrable on large open sets.

## 2. Status of the line bundle lemma and of a counterexample

**Proposition 3 (reduction, r = 1, complete given the input).** Suppose D is smooth, and suppose N_D admits a J_D-holomorphic cocycle g_ab for some ω_D-tame J_D. Then the answer is yes for D.

*Proof.*
1. On N_D, define J = J_D ⊕ i in each local trivialisation. The transition map (x, v) ↦ (x, g_ab(x) v) is J-holomorphic because dg_ab is C-linear with respect to J_D, so J is well defined, and the fibre coordinate v is J-holomorphic.
2. Along the zero section, J is ω_0-tame for the standard model form ω_0, which is ω_D plus a fibre area form after choosing a connection. Tameness is an open condition, so J is ω_0-tame on a neighbourhood of the zero section.
3. Weinstein's symplectic neighbourhood theorem identifies a neighbourhood of D in (M, ω) with (N_D, ω_0) near the zero section. No change of ω is needed here.
4. The ω-tame almost complex structures form a bundle with contractible fibres, so J extends from a smaller neighbourhood to an ω-tame J on all of M. Away from D, take r = 0. ∎

**Gap.** The line bundle lemma itself is NOT proved here, not even for dim_R D = 4. Here is the intended route O3 and where it stops.
- Write L = O(E_1 − E_2), with E_1 and E_2 symplectic hypersurfaces of D obtained from Donaldson–Auroux asymptotically holomorphic sections. This is cited from memory: such hypersurfaces exist in classes k[ω'] + c_1(L) for k ≫ 0, with ω' a rational approximation of ω_D.
- The cocycle is then f^1_a f^2_b / (f^1_b f^2_a), built from local defining functions of E_1 and E_2. It requires a tame J_D in which E_1 ∪ E_2 has J_D-holomorphic local defining functions. That is the original problem for an SC divisor one dimension lower, but now WITHOUT the permitted deformation of ω_D.
- For dim_R D = 4, the E_i are surfaces. They can be taken to meet transversally and positively (Auroux's construction gives this, again from memory). The missing step is to make them ω_D-orthogonal at their intersection points by an isotopy. A local isotopy perturbation is standard in dimension 4 (Gompf-type), but I have not written it out. With orthogonality, and recursively for points inside surfaces, which is trivial, the induction would close for dim_R D = 4. This step, and the corresponding statement in all dimensions, remains open in this answer.

**Counterexample search.** I found no counterexample.
- The necessary conditions (N1) and (N2) only constrain J_D on the open sets where the cocycle is nonconstant. One can arrange those sets to be tubular neighbourhoods of the E_k, where J_D can be integrable.
- A closed symplectic 4-manifold D with no complex structure is therefore NOT an obstruction: J_D need only be integrable near the curves E_k.
- Classes c_1(N_D) outside the span of symplectic surfaces do not exist, because Donaldson's theorem lets every integral class be written as a difference of symplectic classes.

## Summary
- **Proved:** O1 (Lemma 1), the holomorphic-cocycle necessary condition (Corollary 2), the Nijenhuis restriction (N1), the crossing compatibility (N2), and the reduction of the smooth case (r = 1) to the line bundle lemma (Proposition 3).
- **Open:**
  - the line bundle lemma, even for dim_R D = 4: the orthogonalisation of E_1 ∪ E_2 is the missing step;
  - the inductive case r ≥ 2;
  - hence the full question.
- **Expectation, not proved:** the answer is YES. No obstruction was found.

=== END OF ANSWER round1_q4 ===
