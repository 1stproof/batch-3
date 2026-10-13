# round1_q1: partial answer (the main claim is not proved)

Notation: a_0=c_1, a_{i+1}=f(a_i), a_4=a_0. The critical values are a_1 and v. G is the group of φ in PMod(S^2,B) that have a lift φ~ with φ~ = i(φ) in PMod(S^2,A). Elements of G preserve D_f. This follows from the task's framework: f^*(φτ)=φ~ f^*(τ) and i_*(φτ)=i(φ) i_*(τ).

## Lemma 1 (proved). Curves around v and a_j, j in {0,2,3}, give twist-squares in G.
Setup: γ bounds a disk D with D∩B={v,a_j}.
- D contains exactly one critical value, v. So f^{-1}(D) is a single disk D~, mapping 2:1 and branched at c_2. Its boundary δ=f^{-1}(γ) maps to γ with degree 2.
- B∩D~ consists of the preimages of a_j and v. These are a_{j-1} (in A), another point a'_{j-1} (not in A), and the preimages of v (not in A).
- Since j≠1, a_{j-1}≠a_0... except in the case j=1, which is excluded. In every allowed case D~ contains exactly one point of A, so δ is peripheral in (S^2,A).
- T_γ^2 lifts to T_δ, because the degree-2 cover unwinds a double twist into a single twist. T_δ is trivial in PMod(S^2,A).
- i(T_γ)=1 as well, since γ encloses only one point of A.
- Therefore T_γ^2 ∈ G, and T_γ^2 preserves D_f.

## Lemma 2 (proved). Curves around the two critical values are not in G.
Setup: γ bounds a disk D with D∩B={a_1,v}.
- f^{-1}(D) is an annulus containing c_1=a_0 and c_2. It is bounded by curves δ_1 and δ_2, each mapping with degree 1.
- The two complementary disks split {a_1,a_2,a_3}. Each power T_γ^k lifts to T_{δ_1}^k T_{δ_2}^k, while i(T_γ)=1.
- If the split is 2/1, one δ_i is essential rel A. Then no nonzero power of T_γ lies in G.
- So this kind of curve is a candidate only when the split is 3/0, and in that case the twist acts trivially rel A.

## Proposed answer (claimed, not proved)
Take γ to be the boundary of a regular neighbourhood of an arc α from v to a_j, with j ∈ {0,2,3}. Choose α so that γ is **not** the curve that pinches at the puncture of W (the image of D_f in M_{0,5}) where f(c_2) collides with a_j. Concretely, α is obtained from the "pinching" arc α_0 by sliding its endpoint once around a second cycle point.

By Lemma 1, the power T_γ^2 preserves D_f.

The expected reason for an infinite orbit is the abelianization obstruction:
- The class of T_γ in H_1(M_{0,5}) = Z^5 equals the class of the twist about any curve surrounding {v,a_j}.
- So the obstruction has to come from a non-abelian quotient, or from the cusp argument. A parabolic element of G_0 acting on the disk D_0 must be conjugate within G_0 to a cusp monodromy of W. W has one cusp per collision type (v=a_j for each j, plus the degenerations of the cycle).
- If T_γ^{2n} were in G_0, then γ would be G_0-conjugate to a pinching curve α_0-type. Excluding this requires the explicit combinatorics of W.

I recall, without having checked it, that this is the mechanism in Hironaka–Koch, "A disconnected deformation space of rational maps". There, a twist of this kind has an infinite orbit on π_0(D_f).

## Open
- The proof that ⟨T_γ^2⟩ has an infinite orbit on π_0(D_f) is not given.
- Neither are the explicit computation of W (its genus, cusps and cusp monodromies) and the exclusion of γ from the G_0-conjugates of the cusp curves.

=== END OF ANSWER round1_q1 ===
