# round1_q4 answer

Notation: a_0=c_1, a_1=f(c_1), a_2, a_3 is the critical 4-cycle, A={a_0,...,a_3}, B=A∪{v}. The critical values are a_1 and v.

## The curve
Let γ be a simple closed curve in S^2∖B that bounds a disk Δ with Δ∩B={a_1,v}, so γ surrounds both critical values. In addition we need the outer disk Δ'=S^2∖Δ, which contains a_0,a_2,a_3, to have preimage under f consisting of two disks E_1,E_2, where E_1 contains a_1,a_2,a_3 and E_2 contains no point of A. The precise conditions are given in the Lemma.

## Lemma (T_γ preserves D_f). Proved.
Since Δ' contains no critical value, f^{-1}(Δ') is two disks E_1,E_2, each mapped homeomorphically onto Δ'. Then f^{-1}(Δ) is an annulus containing c_1,c_2, and f^{-1}(γ)=δ_1∪δ_2 with δ_i=∂E_i, each mapping with degree 1.

- The preimages of a_0,a_2,a_3 are {a_3,a_3'}, {a_1,a_1'}, {a_2,a_2'}. One of each pair lies in E_1 and the other in E_2.
- The point a_0=c_1 lies in the annulus.
- So the A-points outside the annulus are a_1,a_2,a_3. Choosing the arc that Δ thickens means choosing γ so that all three lie in the same disk E_1. This is always possible: pass from one choice to another by pushing v around loops, which permutes which sheet each preimage lies in.

With this choice, δ_2 bounds a disk with no point of A, and δ_1 bounds a disk whose complement contains only a_0. So both are peripheral in (S^2,A). The lift of T_γ is T_{δ_1}T_{δ_2}, which is trivial in PMod(S^2,A). Also i(T_γ) is trivial, because i(γ) encloses only a_1. Hence f^*(T_γ τ)=f^*(τ) and i_*(T_γ τ)=i_*(τ), so T_γ maps D_f to D_f. Here the power is k=1.

The 3/0 split is not automatic. With a 2/1 split, δ_1 is essential and T_γ^n is never in G for n≠0. So the arc choice is part of the answer.

## Infinite orbit: not proved here
The claim is that no nonzero power of T_γ stabilises a component D_0 of D_f, i.e. T_γ^n ∉ G_0 for n≠0. Then the T_γ-orbit of D_0 in π_0(D_f) is infinite. From memory, this is the theorem of Hironaka–Koch ("A disconnected deformation space of rational maps"). They use exactly a twist about a curve surrounding the two critical values, and show D_f has infinitely many components. I have not reproduced their argument.

The route I would take: compare the image of H_1(W) in H_1(M_{0,5}) with the class e_{a_1 v}. The cusps of W are where v collides with a_j, j=0,2,3, and their monodromies are powers of twists around {v,a_j}. One would need to show the class e_{a_1 v} is not in the span of the cusp classes and the other contributions from H_1(W). Steps not done: proving W is connected, and computing the full image of H_1(W).

Status:
- Proved: T_γ ∈ G for the explicit curve with the 3/0 lift condition.
- Cited, not proved: the infinite orbit.
- Open: a self-contained proof that T_γ^n ∉ G_0 for all n≠0.

=== END OF ANSWER round1_q4 ===
