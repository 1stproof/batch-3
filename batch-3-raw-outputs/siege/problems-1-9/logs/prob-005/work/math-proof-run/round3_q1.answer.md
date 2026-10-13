# round3_q1: the exponent-3 class with -1 = 1 (partial result)

**Verdict.** I did not settle the question. I found no counterexample and no impossibility proof. Below are (1) the exact translation of the problem into conditions on triangles, and (2) a new proved obstruction: the "linear" derivations of (B6) still fail in the exponent-3 class, even though the extra coincidences x^3 = w^3 = 1 make the parity (mod 2) version solvable. The main question stays open.

## 1. Translation (proved, elementary)

Write G = F_3^k additively. Group element g stands for the multiplicative element, and the hyperfield zero is written ∞. Let Δ be the set of unordered triples {a,b,c} of elements of G, with repetition allowed, such that 0_H ∈ a⊞b⊞c.

**Statement.** By (B11c), the hyperfields of this class are exactly the families Δ that satisfy all of the following:
- Δ is invariant under translation by G;
- membership does not depend on the order of a, b, c;
- the 4-point condition holds.

Here a⊞b = {c ∈ G : {a,b,c} ∈ Δ}, with ∞ added when a = b. Put S_g := 1⊞g ∩ G = {h : {0,g,h} ∈ Δ} and D = S_0.

**Rules for the sets S_g.** Translation invariance and symmetry are equivalent to:

h ∈ S_g ⇔ g ∈ S_h ⇔ −g ∈ S_{h−g} ⇔ −h ∈ S_{g−h}.

These are the six images of {0,g,h} under the affine maps that permute the three points. They determine Δ completely.

**Counterexample condition, by (B10)/(B11).** Define
- Q = {0} ∪ ⋃_{d∈D} S_d,
- w with {x, 2x, w} ∈ Δ for some x,
- and require Q ∩ (w+Q) = ∅.

## 2. Linear derivations fail in the exponent-3 class (proved)

**Admissible moves.** Only the following moves are allowed:
- the relations 0 ∈ mx ⊞ mx² ⊞ mw, for monomials m = x^i w^j;
- the pairs 0 ∈ a⊞a;
- disjoint union of zero-sums (if 0 ∈ A and 0 ∈ B then 0 ∈ A⊞B);
- composition (B5), which cancels one shared term between two different components.

Cancelling a term inside a single component is not allowed (see B5).

**Claim.** In the generic situation, where the 9 monomials x^i w^j are distinct, no such derivation produces 0 ∈ 1⊞1⊞1⊞w⊞w⊞w. (Specific Δ might create extra coincidences among the monomials; that case is not covered.)

**Proof.**

*Step 1 (counting).* A component built from n triangles linked in a tree has n+2 remaining terms. A pair component has 2 terms. Attaching a pair to an existing term changes nothing, because 0∈A⊞a together with 0∈a⊞a gives back 0∈A⊞a. To get 6 terms, the possible shapes are:
- (i) a single tree of 4 triangles;
- (ii) a tree of 2 triangles plus one pair;
- (iii) two separate triangles.

*Step 2 (shapes (ii) and (iii)).* Each triangle has 3 distinct terms. Shape (ii) would need three equal leftover terms from two triangles; shape (iii) would need a triangle {1,1,w} or {1,w,w}. Both are impossible.

*Step 3 (shape (i), reduction to the group ring).* Reduce mod 2 in R = F_2[x,w]/(x³−1, w³−1) ≅ (F_2 × F_4)⊗(F_2 × F_4). Let f be the sum of the four chosen m's. Then f·(x+x²+w) = 1+w + 2(cancelled pairs) ≡ 1+w.

*Step 4 (solving at x = 1).* At x = 1 we have x+x² = 0. The equation becomes f(1,w)·w = 1+w, so f(1,w) = 1+w².

*Step 5 (solving at x = ω).* At x = ω we have x+x² = 1. The equation becomes f(ω,w)(1+w) = 1+w, so f(ω,w) ≡ 1 mod (1+w+w²).

*Step 6 (all solutions).* Write f = a + b w + c w². The conditions give a = 1, b = 0, c = 1+x+x², up to the kernel, which is h(x)(1+w+w²) with h ∈ {0, x+x², 1+x, 1+x²}. So the solutions are

f = 1 + (1+x+x²)w² + h(x)(1+w+w²).

The 4-term solutions include:
- {1, w², xw², x²w²};
- x + (1+x)w + x²w², i.e. {x, w, xw, x²w²}.

*Step 7 (checking multiplicities).* Expand the integer multiset of terms for either 4-term solution. It contains 1 and w exactly once each, and five other monomials exactly twice each. For example, the first solution gives x, x², xw², x²w², w² twice each. The target 1,1,1,w,w,w needs coefficient 3 on both 1 and w. Moreover, 3 tree edges can cancel only 3 of the 5 doubled pairs. So shape (i) fails as well. ∎

**Interpretation.** Unlike the generic case (B6), the mod-2 equation is solvable here. The obstruction comes from the integer multiplicities and the tree structure, not from parity. An affirmative proof would need witnesses from D = (1⊞1)\{0} or other auxiliary elements.

## 3. What is open

- **Construction step not done.** I did not carry out plan steps 2 and 3. I derived no further necessary conditions from the 4-point condition, and I built no explicit Δ on F_3^k with k ≥ 3.
- **Exponent-3 question.** Is there a Δ on G = F_3^k (k ≥ 3) or on F_3^(N) satisfying the rules of §1 and the 4-point condition, with Q ∩ (w+Q) = ∅ for some admissible w? This is OPEN.
- **Headline question.** OPEN.

=== END OF ANSWER round3_q1 ===
