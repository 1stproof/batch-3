# round2_q4 — answer (partial)

## Candidate curve
Use the normalization of background item (2) with a real parameter t in (1/2, (3-sqrt5)/2)... actually any fixed base point t_0 in W. Let gamma be a simple closed curve that bounds a disk Delta with Delta ∩ B = {a_1 = ∞, v}, i.e. it separates the two critical values {a_1, v} from {a_0, a_2, a_3}, and that is **not** in the G_0-orbit of the cusp curve gamma_0 at t = 1/2. Take k = 1 if gamma has the 3/0 split of item (6) (e.g. gamma = h(gamma_0) with h in G \ G_0), and note that for a 2/1-split curve no power lies in G, so only 3/0 curves can be candidates. Alternatively a curve around {v, a_j}, j in {0,2,3}, with k = 2 (item (5)).

## What is proved here
1. (Item (5), checked) For any gamma around {v, a_j}, j ∈ {0,2,3}: f^{-1}(Delta) is a single disk branched at c_2 containing only a_{j-1} from A, so T_gamma^2 lifts to the twist about a curve peripheral rel A, and i(T_gamma) = 1. Hence T_gamma^2 ∈ G and preserves D_f.
2. (Item (6), checked) For gamma around {a_1, v} with 3/0 split, T_gamma lifts to T_{δ1}T_{δ2} with δ_1 bounding a disk containing a_1,a_2,a_3 (and δ_2 bounding a disk with no point of A, hence trivial rel A), so the lift is trivial rel A... together with i(T_gamma)=1 this gives T_gamma ∈ G, so T_gamma preserves D_f.
3. Orbit is infinite iff no T_gamma^{kn} (n≠0) lies in K = G_0 ∩ F (item (7)).

## What is NOT proved (open)
I could not establish, for any explicit gamma, that T_gamma^{kn} ∉ K for all n ≠ 0. The abelian obstruction fails (item (3)); the quotient Q = F/<<ℓ_0²,ℓ_2²,ℓ_3²>> kills T_gamma^2 for the {v,a_j} curves, and for 3/0 curves around {a_1,v} the image in Q is a parabolic conjugate of ℓ_1, which may lie in the image of K, so Q does not decide it either. From memory (not verified) Hironaka–Koch (J. Mod. Dyn. 2017) prove the infinite orbit for a twist of this kind; I cannot reproduce their argument. The headline claim remains OPEN in this file.

=== END OF ANSWER round2_q4 ===
