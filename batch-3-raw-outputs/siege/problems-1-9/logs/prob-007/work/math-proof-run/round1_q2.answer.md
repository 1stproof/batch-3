# round1_q2 — explicit model of W and the abelian obstruction

## (a) Normal form and parametrization (proved by direct computation)
Notation: a_0=c_1, a_1=f(a_0), a_2, a_3, with f(a_3)=a_0. Normalize so that a_0=0, a_1=∞, a_2=1, a_3=t.
- 0 is critical and f(0)=∞, so f(z)=(αz²+βz+γ)/z². From f(∞)=1 we get α=1, so f(z)=1+β/z+γ/z².
- f(1)=t gives t=1+β+γ. f(t)=0 gives t²+βt+γ=0.
- Solving: β=(t²+t−1)/(1−t) and γ=t(1−2t)/(1−t).

So Per_4(0) with a marked cycle is rational, with parameter t.
- Other critical point: c_2=−2γ/β = −2t(1−2t)/(t²+t−1).
- Other critical value: v = 1−β²/(4γ). Write D=4t(1−2t)(1−t). Then:
  - v = −(t²−3t+1)²/D,
  - v−1 = −(t²+t−1)²/D,
  - v−t = −(3t²−3t+1)²/D.
  These follow from the identities (t²+t−1)²−D=(t²−3t+1)² and D(1−t)−(t²+t−1)²=−(3t²−3t+1)². I checked both by expansion.

## (b) Punctures of W
Fixing (a_0,a_1,a_2)=(0,∞,1) uses up the Möbius freedom, so t determines the marked conjugacy class. This gives the map W → M_{0,5}, t ↦ (0,∞,1,t,v(t)). W is the t-line minus 10 points:
- t = 0, 1, ∞, 1/2: degenerations. Either cycle points collide or the degree drops.
- The 2 roots of t²+t−1: here v=1=a_2, with contact order 2.
- The 2 roots of t²−3t+1: here v=0=a_0, with contact order 2.
- The 2 roots of 3t²−3t+1: here v=t=a_3, with contact order 2.

v never equals ∞=a_1 except at degenerate points.

## (c) Abelianization (proved)
In H_1(M_{0,5}) ≅ Z^5, use the coordinates given by the winding numbers of the functions t, t−1, v, v−1, v−t. These correspond to the classes e_{a3a0}, e_{a3a2}, e_{va0}, e_{va2}, e_{va3}. The class of a loop around a puncture p is the vector of orders of these five functions at p:
- t=0: (1,0,−1,−1,−1)
- t=1: (0,1,−1,−1,−1)
- t=1/2: (0,0,−1,−1,−1)
- t=∞: (−1,−1,−1,−1,−1)
- each root of t²−3t+1: (0,0,2,0,0)
- each root of t²+t−1: (0,0,0,2,0)
- each root of 3t²−3t+1: (0,0,0,0,2)

These vectors span a sublattice of rank 5. So the image of H_1(W) in H_1(M_{0,5}) has full rank (finite index; its index divides 2^3). **Conclusion: the abelian obstruction is insufficient.** For every curve γ, some power of the class of T_γ lies in the image of H_1(W). A finer, non-abelian invariant is needed.

## (d) Candidate curve and status
**Candidate (not proved):** γ is the curve surrounding the two critical values a_1=f(c_1) and v, and separating them from {a_0,a_2,a_3}.

Lifting structure (proved):
- f^{-1}(disk bounded by γ) is an annulus containing c_1=a_0 and c_2. This is a degree-2 cover of a disk branched over two points.
- The complement of that annulus is two disks. Each maps homeomorphically onto the outside of γ.
- So f^{-1}(γ)=δ_1⊔δ_2, each component mapping with degree 1, and T_γ lifts to T_{δ_1}T_{δ_2}.

For T_γ^k to lie in G, we need the lift to equal i(T_γ^k)=T_{i(γ)}^k in PMod(S²,A), where i(γ) surrounds {a_1}∪... rel A. Note that i(γ) is peripheral rel A. So this requires each δ_j to be peripheral rel A, or to be isotopic to each other with cancelling twists. I have not verified which case occurs for this map. This is the remaining step that is needed.

I recall that the problem appears in Hironaka–Koch, "A disconnected deformation space of rational maps". I am citing this from memory and have not checked which curve they use.

**Open:**
1. Verify that a power of T_γ lies in G.
2. Prove that no power of it lies in G_0 = image of π_1(W) (a free group of rank 9). One possible route is a non-abelian quotient, e.g. the action on curves/arcs or a finite-index congruence quotient. Another is the parabolic argument: a twist power in G_0 must be conjugate to a puncture loop of W, and the puncture loops have monodromy twists about curves around {v,a_j} for j=0,2,3, or about curves from degenerations of the cycle.

I have **not** proved an infinite orbit for any explicit γ.

=== END OF ANSWER round1_q2 ===
