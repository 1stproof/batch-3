# round1_q1 — answer (partial: reductions proved, the inductive core sketched)

Conventions: the ones in the task file. D = D_1 u ... u D_N, transverse, all strata symplectic, positive orientations. The goal near p in D_I with |I| = r is: z_1..z_r J-holomorphic, D_i = {z_i = 0}.

## 1. Necessity of a holomorphic normal structure (proved)
Suppose J is as required. Let z, z' be two such local defining functions of D_i, on overlapping charts. Then h = z'/z is smooth and nonvanishing off D_i. Since both vanish transversally on D_i, h extends smoothly and nonvanishingly across D_i (Hadamard division in the normal directions). Off D_i, dh = (dz' - h dz)/z is C-linear, so by continuity dh is C-linear everywhere. Hence h|_{D_i} is J|_{D_i}-holomorphic. The normal bundle N_{D_i} therefore carries a cocycle of nonvanishing J|_{D_i}-holomorphic functions. Note that J|_{D_i} preserves TD_i, because D_i = {z_i = 0} with dz_i C-linear.
So the following is unavoidable:

**Line Bundle Lemma (LBL).** For closed symplectic (B, ω_B) and a complex line bundle L → B, there are an ω_B-tame J_B and a J_B-holomorphic C*-valued cocycle representing L.

## 2. Linear algebra at crossings (proved, modulo one cited standard fact)
Let p ∈ E_1 ∩ E_2, where E_1, E_2 are transverse symplectic hypersurfaces with symplectic, positively oriented intersection. Put H = T_p(E_1∩E_2)^ω, which is 4-dimensional and symplectic. Put ℓ_1 = T_pE_2 ∩ H and ℓ_2 = T_pE_1 ∩ H. Each ℓ_j is the ω-complement of T(E_1∩E_2) inside a symplectic space, so it is symplectic. We have H = ℓ_1 ⊕ ℓ_2, and positivity means this sum orientation is the symplectic one.

Standard fact (cited from memory, e.g. McDuff–Salamon / Gompf): two transverse symplectic planes in a symplectic 4-space are J-complex for some ω-tame linear J iff they intersect positively.

Let G = (g_1, g_2) be local defining functions with dG|_H mapping ℓ_j to the j-th axis and pulling i back to that tame J. Set J = (any ω-compatible structure on ker dG) ⊕ (dG|_H)^{-1} i dG on H' = (ker dG)^ω. This J makes g_1, g_2 holomorphic. It is tame at p, because the two summands are ω-orthogonal and each is tame. Being tame is an open condition, so J is tame near p. The case of r = 1, or of more components, is the same.

## 3. Reduction of r = 1 (one smooth divisor) to LBL (proved given LBL)
This is O2 of the task file. Take J_D from LBL for L = N_D, and put J = J_D × i in each holomorphic trivialization of N_D. This is well defined, because the transition (x, w) ↦ (x, g(x) w) has C-linear differential when g is J_D-holomorphic. The fibre coordinates w are J-holomorphic.
Transport J to M with the symplectic neighbourhood theorem. This requires the symplectic form on N_D to be chosen tame for J. Use ω_D + d(ρ α) with a Hermitian metric and a connection α, and choose the connection so that the horizontal and vertical splitting is J-invariant near the zero section. This holds after shrinking, since at the zero section ω = ω_D ⊕ fibre form and J = J_D ⊕ i is block-tame.
Finally extend J to all of M. Tame structures are sections of a bundle with contractible fibres, so the extension exists; leave J unchanged on a smaller neighbourhood of D.

## 4. Attack on LBL (sketch; GAP)
Approximate ω_B by a rational form ω'. Tameness is C^0-open, so a J tame for ω' close to ω_B is tame for ω_B. Let P be a prequantum bundle for ω'. Donaldson/Auroux asymptotically holomorphic transverse sections (cited from memory) of L⊗P^k and P^k, taken for k large, give symplectic hypersurfaces E_1 and E_2. They meet transversally with symplectic, positive intersection, and they are approximately J_0-complex for a compatible J_0.
Then L = O(E_1 - E_2). A J_B-holomorphic cocycle comes from J_B-holomorphic local defining functions of E_1 ∪ E_2, which are coherent along each E_j. Section 2 gives such J_B locally. To make them coherent one needs the problem itself for the 2-component divisor E_1 ∪ E_2 in dimension dim B. By Section 3 this reduces to LBL for N_{E_j} → E_j, compatibly on E_1 ∩ E_2. This is the same problem in dimension 2 lower, and the base case (real surfaces, where every J is integrable) is trivial.

**Gap (not completed):** the induction must carry several extra pieces of data that I have not written out:
- (a) a statement for multi-component divisors whose holomorphic normal structures on N_{D_i}|_{D_I} are compatible over all strata;
- (b) a symplectic neighbourhood / regularization model in which the J built from those structures is tame. Here one would use Tehrani–McLean–Zinger, cited from memory: after a deformation of the allowed type, D admits an ω-regularization, meaning compatible tubular models in which ω is the standard Hermitian-connection form on ⊕_{i∈I} N_i near D_I. This deformation is why the question allows changing ω;
- (c) in the step inside B, no non-small deformation of ω_B is allowed. Small ones are harmless because tameness is open. So one must check that Donaldson pairs can be made to admit an ω_B-regularization after a C^1-small isotopy, using their near-J_0-holomorphicity.

## Status
- Proved: the necessity statement (Section 1); local existence of tame J with holomorphic defining functions at positive crossings (Section 2, citing one standard linear fact); the r = 1 case conditional on LBL (Section 3).
- Sketched, not proved: LBL, and the general SC case, via the dimension induction of Section 4.
- Expected answer: YES, but this is not established here.
- Open: points (a), (b), (c) above.

=== END OF ANSWER round1_q1 ===
