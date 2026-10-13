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

=== END OF ANSWER round2_q3 ===
