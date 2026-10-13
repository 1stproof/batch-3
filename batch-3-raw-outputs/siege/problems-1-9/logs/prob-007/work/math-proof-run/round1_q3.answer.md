# round1_q3: candidate curve and lifting computation (partial)

Notation: a_0=c_1, a_{k+1}=f(a_k), indices mod 4; A={a_0,..,a_3}, B=A∪{v}. The critical values are a_1 and v.

## Proposal (curve γ)
γ is the boundary of a small regular neighbourhood of an arc α in S^2∖(A) joining the two critical values a_1 and v. So γ surrounds exactly {a_1, v}, and α is chosen as described in Lemma 2 below.

## Lemma 1 (preimage of γ). Proved.
Let D be the disk bounded by γ containing a_1 and v, and D' the complementary disk, which contains a_0, a_2, a_3. D contains both critical values. By Riemann–Hurwitz, f^{-1}(D) is connected with Euler characteristic 2·1−2=0, so it is an annulus containing c_1=a_0 and c_2. D' contains no critical value, so f^{-1}(D') is two disks E_1, E_2, each mapped homeomorphically onto D'. Hence f^{-1}(γ)=δ_1⊔δ_2 with δ_i=∂E_i, and each δ_i maps to γ with degree 1. The points of A that lie in f^{-1}(D') are a_3, a_1, a_2 (the preimages in the cycle of a_0, a_2, a_3). Each E_i contains exactly one preimage of each of a_0, a_2, a_3. a_0 lies in the annulus.

## Lemma 2 (lifting criterion). Proved, standard.
Let φ∈PMod(S^2,B). Suppose φ has a lift φ~ with f∘φ~=φ∘f, φ~ fixing A pointwise, and φ~ = i(φ) in PMod(S^2,A). Then φ preserves D_f: if f^*τ=i_*τ, then f^*(φτ)=φ~·f^*τ=i(φ)·i_*τ=i_*(φτ).
Because each δ_i maps to γ with degree 1, T_γ lifts to T_{δ_1}T_{δ_2}. This lift fixes every point (it is supported in annular neighbourhoods of δ_1, δ_2, which avoid A). Rel A, i(γ) surrounds only a_1, so i(T_γ) is trivial in PMod(S^2,A). So T_γ∈G exactly when T_{δ_1}T_{δ_2} is trivial rel A. That happens iff each δ_i is peripheral rel A. Since a_0 lies in the annulus, this means: one disk, say E_1, contains all of a_1, a_2, a_3, and E_2 contains no point of A (it holds only the other preimages a_1', a_2', a_3'). **Choice of α:** choose the arc α (its isotopy class rel B) so that this splitting holds. Such a choice exists: changing α by a twist about a curve around {a_1, v} plus one more point moves the preimages of single points between E_1 and E_2. Under this choice, T_γ (power k=1; k=2 in any case suffices if a sign ambiguity arises) preserves D_f.
I have only sketched the existence of such an α. It is not fully verified.

## Infinite orbit. Heuristic, not proved.
Theorem (recalled, not proved here): π_0(D_f)≅G/G_0, where G_0 is the image of the monodromy π_1(W)→PMod(S^2,B). So the orbit of a component is infinite iff no power T_γ^n (n≠0) lies in G_0. A parabolic element of G_0 must come from a puncture of W at which γ is pinched. Here pinching γ means the critical values a_1 and v collide while a_0, a_2, a_3 stay apart. That is f(c_2)=f(c_1), which for a quadratic map forces c_1=c_2, so it cannot happen for any genuine map. The argument is then that no such cusp of W exists, which would make the orbit infinite. This step is incomplete: degenerations to the boundary of rational-map space have not been ruled out. The punctures where v=a_j, j≠1, give the curves around {v,a_j} instead. Those have finite orbits and are excluded on purpose.

I recall (from memory, unverified) that this example appears in Hironaka–Koch, "A disconnected deformation space of rational maps". I think they use a twist about a curve that separates the two critical values from the rest, but I could not confirm the exact curve.

## Status
- Proved: Lemma 1, the lifting criterion, and that T_γ∈G given the splitting condition on α.
- Sketched: existence of an arc α that gives that splitting.
- Open: a rigorous proof that the orbit on π_0(D_f) is infinite.

=== END OF ANSWER round1_q3 ===
