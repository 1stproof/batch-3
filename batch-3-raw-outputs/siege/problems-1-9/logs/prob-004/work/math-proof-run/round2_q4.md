kind: attempt
Open question attempted: the assembly lemma (Steps 2-4 of the route below), an open load-bearing gap: given an omega-regularized auxiliary SC configuration with integral partner relations, construct the omega-tame J with the required holomorphic coordinates, with all compatibilities checked (the earlier sketch left compatibility of connection changes across strata unchecked).

## Background: conventions and results already obtained by earlier work (verify anything you rely on)

Conventions. "Symplectic simple normal crossings (SC) divisor" is taken in the Tehrani-McLean-Zinger (TMZ)
sense: D = D_1 u ... u D_N, each D_i a closed embedded symplectic submanifold of real codimension 2, the D_i
meeting transversally, every stratum D_I = (intersection of the D_i, i in I) symplectic, with symplectic
orientation equal to its intersection orientation (positivity; without it the answer is trivially no). The
desired coordinates near p: r = number of components through p, z_1..z_r J-holomorphic with dz_1..dz_r
C-linearly independent, D_i = {z_i = 0} near p, other coordinates merely smooth. At the top level one may
deform omega as the problem allows (D itself must be kept). In auxiliary sub-problems on a closed symplectic
manifold B where only the existence of a tame J (and of some hypersurfaces in given homology classes) is
needed, a cohomologous deformation can be undone by Moser's theorem (phi^* omega_1 = omega_0, phi isotopic
to the identity), pulling everything back by phi.

### Result 1 (necessity; proved in earlier work, quoted verbatim)
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


### Result 2 (smooth case reduces to a line bundle lemma; proved, quoted verbatim)
**Proposition 3 (reduction, r = 1, complete given the input).** Suppose D is smooth, and suppose N_D admits a J_D-holomorphic cocycle g_ab for some ω_D-tame J_D. Then the answer is yes for D.

*Proof.*
1. On N_D, define J = J_D ⊕ i in each local trivialisation. The transition map (x, v) ↦ (x, g_ab(x) v) is J-holomorphic because dg_ab is C-linear with respect to J_D, so J is well defined, and the fibre coordinate v is J-holomorphic.
2. Along the zero section, J is ω_0-tame for the standard model form ω_0, which is ω_D plus a fibre area form after choosing a connection. Tameness is an open condition, so J is ω_0-tame on a neighbourhood of the zero section.
3. Weinstein's symplectic neighbourhood theorem identifies a neighbourhood of D in (M, ω) with (N_D, ω_0) near the zero section. No change of ω is needed here.
4. The ω-tame almost complex structures form a bundle with contractible fibres, so J extends from a smaller neighbourhood to an ω-tame J on all of M. Away from D, take r = 0. ∎


### Result 3 (regularization, connection-type almost complex structures; quoted verbatim from earlier work — TMZ is cited from memory there, state it precisely if you use it)
## 0. Cited results (from memory)

**(TMZ)** Tehrani–McLean–Zinger, "Normal crossings singularities for symplectic topology". Let D = ∪D_i be an SC divisor in (M, ω). Then ω can be deformed through cohomologous symplectic forms, keeping D an SC divisor, to a form (still called ω) that admits an ω-regularization. This means the following. For every I there are:
- Hermitian structures (ρ_{I;i}, ∇_{I;i}) on the line bundles N_{D_i}|_{D_I}, for i ∈ I;
- a tubular embedding Ψ_I from a neighbourhood of the zero section of N_I = ⊕_{i∈I} N_{D_i}|_{D_I} into M.

These satisfy:
1. Ψ_I^*ω = ω_{(ρ,∇)} := π^*ω|_{D_I} + ½ Σ_{i∈I} d(ρ_i α_i), where α_i is the connection 1-form of ∇_i.
2. Ψ_I^{-1}(D_i) is the bundle {z_i = 0} for i ∈ I.
3. Compatibility for I ⊂ I'. Over D_{I'} we have N_{I'} = N_{I'−I}D_I|_{D_{I'}} ⊕ N_I|_{D_{I'}}. The maps Ψ_{I'} and Ψ_I agree after composition with the induced tubular map of D_{I'} inside D_I. Under this identification the Hermitian structures on N_{D_i}|_{D_I} near D_{I'} are the pullbacks, by the model projection, of the ones on N_{D_i}|_{D_{I'}}.

**(NN)** On a 2-dimensional manifold every almost complex structure is integrable.

**(Moser)** On a closed manifold, if ω_t is a path of cohomologous symplectic forms, there is a diffeomorphism φ isotopic to the identity with φ^*ω_1 = ω_0.

## 2. Key local fact: the connection almost complex structure

**Lemma A.** Let B carry an almost complex structure J_B. Let E = ⊕ L_i → B carry connections ∇_i. Define J_∇ on the total space as follows: on the horizontal subspace it is the lift of J_B; on the fibres it is i.

Let s_i be a local frame with ∇ s_i = θ_i s_i, and let z_i be the matching fibre coordinates. Then:
- z_i is J_∇-holomorphic if and only if θ_i is of type (1,0) for J_B;
- the projection π is (J_∇, J_B)-holomorphic;
- if f is J_B-holomorphic, then π^*f is J_∇-holomorphic.

*Proof.* Horizontal vectors are the kernel of dz_i + θ_i z_i. Hence dz_i(h(v)) = −θ_i(v) z_i.

z_i is J_∇-holomorphic iff dz_i∘J_∇ = i·dz_i. On vertical vectors this holds automatically. On a horizontal lift h(v) it reads −θ_i(J_B v) z_i = −i θ_i(v) z_i for all v and all z_i, that is, θ_i∘J_B = iθ_i. This is exactly the (1,0) condition.

The statements about π hold by construction. ∎

**Lemma B (tameness).** Let ω_{(ρ,∇)} be as in TMZ and J_B be ω|_B-tame. Then J_∇ is ω_{(ρ,∇)}-tame on a neighbourhood of the zero section.

*Proof.* Along the zero section, ω_{(ρ,∇)} is the direct sum of ω_B and the standard fibre forms, and J_∇ = J_B ⊕ i. Tameness is an open condition, and B is compact. ∎

**Lemma C (changing ∇ costs only a permitted deformation).** Let ∇' = ∇ + iβ, with β a real 1-form on B that vanishes near K. Then ω_t = ω + ½ d(χ ρ t β), t ∈ [0,1], is a path of cohomologous symplectic forms. Here χ = χ(ρ) is a cutoff equal to 1 for ρ < ε² and 0 for ρ > 4ε², and ε is small.

*Proof.* The forms are cohomologous because the change is exact. For symplecticity, write d(χρβ) = (χ'ρ + χ) dρ∧β + χρ dβ. The coefficient χ'ρ + χ is O(1), and |dρ| = O(ε) on the support, so the change is O(ε) in C⁰ against the fixed nondegenerate ω. For small ε the forms stay symplectic.

D stays SC: the strata are unchanged, the zero sections stay symplectic, and the normal-form structure is unchanged near D, where χ = 1. ∎

Where χ = 1, ω_1 is the regularized form for ∇'. So any regularization may be changed to one whose connections have (1,0) forms in holomorphic frames, at the price of a permitted deformation. Doing this stratum by stratum requires the new ∇' to satisfy the compatibility condition 3. This holds by the construction order below, because each ∇' equals the already-pulled-back connection near deeper strata.

Additional observation (not yet checked): if {g_ab} is a cocycle of J_B-holomorphic nonvanishing
functions for L on an ALMOST complex (B,J_B) and h is a Hermitian metric (h_a = |s_a|^2 in the frames),
then theta_a := partial log h_a (the (1,0)-part of d log h_a) is of type (1,0), and theta_a - theta_b =
d log g_ab because g_ab is holomorphic (partial of conj(g) vanishes); so the "Chern connection" exists and
its forms are (1,0) in the holomorphic frames; and it commutes with pullback along a
(J_nabla, J_B)-holomorphic projection.

Earlier sketch of the relative difficulty: the obvious induction (deepest stratum first, extend a tame J and
holomorphic cocycles of N_{D_i}|D_I from a neighbourhood of deeper strata to all of D_I) needs a RELATIVE
line bundle lemma; trying to supply it by writing L = O(E_1 - E_2) with Donaldson hypersurfaces fails to
match the prescribed structure near the deeper strata (the mismatch is a holomorphic structure on a
topologically trivial bundle over the deeper stratum, not necessarily holomorphically trivial).

## Proposed route: a global auxiliary configuration (planner's outline — NOT proved; check every step)

Idea: never extend holomorphic structures relatively. Fix, before constructing J, all hypersurfaces whose
divisor line bundles will provide every holomorphic structure that is needed, so that every holomorphic
cocycle on every stratum is INDUCED by local defining functions of global hypersurfaces of M, and the only
thing ever extended is a tame almost complex structure (contractible fibres, no obstruction).

Step 1 (configuration). Let dim_R M = 2n. Construct a finite collection C = {C_a} of closed symplectic
hypersurfaces of M containing D_1,...,D_N, forming an SC divisor (all strata symplectic and positive), with
a level function: the D_i have level 0; every component C_a of level l <= n-2 has two partner components
P_a^+, P_a^- of level l+1, distinct from everything else, with PD[C_a] = PD[P_a^+] - PD[P_a^-] in H^2(M;Z),
so O(C_a) = O(P_a^+) (x) O(P_a^-)^{-1} as smooth complex line bundles on M. Intended construction:
Donaldson-Auroux asymptotically holomorphic transverse sections of O(C_a) (x) P^k and of P^k (P a
prequantum bundle for a rational symplectic form omega' close to omega, k large), chosen level by level
transverse to all strata of the configuration built so far, approximately J_0-holomorphic for an
omega-compatible J_0 for which D (and then each new component) is (approximately) J_0-complex, which should
give symplecticity and positivity of all new strata for omega.

Step 2 (regularize). Apply TMZ to the SC divisor C: deform omega through cohomologous forms keeping C, hence
D, SC, to a form admitting an omega-regularization of C. This is a permitted deformation for the problem.

Step 3 (which strata need what). Call an index set J ancestrally closed if C_J is nonempty and every
component of level >= 1 in J has its parent (the component it is a partner of) in J. On C_J the needed
data: an omega-tame J_J and, for each a in J, a J_J-holomorphic cocycle on N_{C_a}|C_J, namely the
divisor-induced one: O(C_a)|C_J = O(P_a^+)|C_J (x) O(P_a^-)^{-1}|C_J, where O(P)|C_J is the divisor bundle
of the hypersurface P cap C_J of C_J if P is not in J (cocycle = ratios of holomorphic local defining
functions of P cap C_J), and is N_P|C_J (recursively) if P is in J. Recursion terminates: a component of
level n-1 lying in an ancestrally closed J forces |J| >= n, so C_J is a finite set of points, where nothing
is needed. On C_J the hypersurfaces C_b cap C_J for b not in J with J u {b} ancestrally closed must have
J_J-holomorphic local defining functions; in particular the D_k cap C_J.

Step 4 (assembly, deepest first). Process ancestrally closed J by decreasing |J|. Near each deeper needed
stratum C_{J u {b}} inside C_J, define J_J as the connection-type structure J_nabla (Lemma A) built from the
data on C_{J u {b}} in the regularization model; check these agree on overlaps (both are pulled back from
the common deeper stratum, using the TMZ compatibility); extend tamely to all of C_J. Then the divisor
defining functions are J_J-holomorphic, so the divisor-induced cocycles are J_J-holomorphic automatically;
they agree near deeper strata with pullbacks of the deeper cocycles. Use Lemma C (permitted deformation) to
replace the regularization connections by Chern-type connections of the divisor-induced structures, so that
fibre coordinates are holomorphic (Lemma A). The top stratum J = empty set (M itself) needs no line bundle,
only the J near D; then the fibre coordinates of the models give the required z_i.

Snags to check: (i) the smooth isomorphisms N_{C_a}|C_J = divisor bundle must be compatible across strata
(choose one global isomorphism O(C_a) = O(P_a^+)(x)O(P_a^-)^{-1} on M and make it "pulled back" near each
stratum by a homotopy along the tubular retractions); (ii) Lemma C changes near different strata must stay
consistent with the TMZ compatibility condition; (iii) tameness of the J_nabla's for the model forms after
the connection changes; (iv) the exact Donaldson-Auroux statements (transversality to a finite family of
approximately holomorphic submanifolds, positivity of intersections, integrality of classes).

## Task
Assume Step 1 (the configuration C exists, as stated) and the TMZ regularization of C (state precisely the
version you use, including the compatibility conditions between models of nested strata). Prove rigorously
that there is an omega'-tame J, for omega' obtained from omega by a permitted deformation, with the
required local coordinates for D. Concretely: (1) formalize the needed strata and bundles (or a cleaner
bookkeeping); (2) construct J_J on each needed stratum deepest first, proving the connection-type
structures from different deeper strata agree on overlaps; (3) prove the divisor-induced cocycles are
J_J-holomorphic, including across the hypersurfaces (removable singularities as in Result 1) and at
crossings; (4) handle the bundle isomorphisms N_{C_a}|C_J = divisor bundle coherently; (5) show that the
regularization connections can be replaced by Chern-type connections of the divisor-induced structures
through a permitted deformation, compatibly across all strata at once (or show this is unnecessary, e.g. by
building the regularization after J, or by a direct alternative to Lemma A); (6) tameness and extension;
(7) the coordinates at every point. Where the outline is wrong, fix it. If something cannot be completed,
mark it precisely and prove the rest.
