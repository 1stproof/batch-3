# round4_q5 answer (work in progress)

## Plan
Goal: refute (N) by an explicit hyperfield, or find a structural reason why the constructions tried cannot work.
Routes I am examining:
1. "Generalized quotient" constructions: orbit hyperfields A/U, where M ≤ Aut(A) is transitive on A\{0}, U ⊴ M contains the point stabiliser, and M/U is abelian. These include twisted (near-field) multiplications, which is route (iii). I also look at quotients of skew fields.
2. The hexagon structure of the field identity, which gives a "one cycle short" lemma valid in every hyperfield.
3. The triple-intersection criterion.
4. The free / chase construction (route (i)) and what kind of invariant could block the target.

## Result 1 (proved): the hexagon lemma

Setting: H is any hyperfield (any sign of -1), and x, y, z ∈ H satisfy 0 ∈ x⊞y⊞z. Put
S := x³ ⊞ y³ ⊞ z³ ⊞ -xyz ⊞ -xyz ⊞ -xyz (the target set).

**Lemma 1.** For each μ ∈ {x²y, xy², y²z, yz², z²x, zx²}, S ∩ (μ ⊞ -μ) ≠ ∅. Equivalently, S contains an element of μ·(1⊞-1).

*Proof.* Multiply the hypothesis by six monomials (distributivity):
- R1 = x²·: 0 ∈ x³ ⊞ x²y ⊞ x²z
- R2 = (-xy)·: 0 ∈ -x²y ⊞ -xy² ⊞ -xyz
- R3 = y²·: 0 ∈ xy² ⊞ y³ ⊞ y²z
- R4 = (-yz)·: 0 ∈ -xyz ⊞ -y²z ⊞ -yz²
- R5 = z²·: 0 ∈ xz² ⊞ yz² ⊞ z³
- R6 = (-zx)·: 0 ∈ -x²z ⊞ -xyz ⊞ -xz²

Cyclically, consecutive relations contain a common monomial with opposite signs:
R1–R6 (x²z), R6–R5 (xz²), R5–R4 (yz²), R4–R3 (y²z), R3–R2 (xy²), R2–R1 (x²y).
This is the field identity x³+y³+z³-3xyz = (x+y+z)(x²+y²+z²-xy-yz-zx), read as a hexagon of relations. Once the six shared monomials cancel, the surviving terms are exactly x³, y³, z³, -xyz, -xyz, -xyz.

Composition rule (B-1): if 0 ∈ A⊞t and 0 ∈ B⊞-t, then 0 ∈ A⊞B.

Cut the hexagon at the edge R2–R1 and compose along the remaining five edges, in the order R1, R6, R5, R4, R3, R2:
- 0 ∈ x³⊞x²y⊞-xyz⊞-xz²
- then 0 ∈ x³⊞x²y⊞-xyz⊞yz²⊞z³
- then 0 ∈ x³⊞x²y⊞-xyz⊞z³⊞-xyz⊞-y²z
- then 0 ∈ x³⊞x²y⊞-xyz⊞z³⊞-xyz⊞xy²⊞y³
- finally 0 ∈ S ⊞ x²y ⊞ -x²y.

So some t ∈ S has 0 ∈ t⊞x²y⊞-x²y, i.e. -t ∈ x²y⊞-x²y. That set is closed under negation, so t ∈ μ⊞-μ. The other five μ are handled by cutting at the other five edges. ∎

**Corollaries.**
(a) A counterexample needs 0 ∉ S while S meets μ·E for all six μ, where E := (1⊞-1)\{0}.
(b) If 1⊞-1 = {0}, the claim holds. This is not new, since such an H is a field. Proof: if a⊞-a = {0} for all a and c, c' ∈ a⊞b, then a ∈ c⊞-b and -a ∈ -c'⊞b. Hence 0 ∈ a⊞-a ⊆ (c⊞-c')⊞(b⊞-b) = c⊞-c', so c = c'. Thus all sums are singletons, and H is a field.
(c) Interpretation. The target relation is exactly a closed cycle (hexagon) of six translates of the hypothesis. Hyperfield axioms let one compose along a tree, but a cycle leaves a "holonomy" element of μ(1⊞-1). The question is precisely whether this holonomy can be nontrivial. This sharpens the counting obstructions of B-1/B-6. In particular, it explains why the target has three copies of -xyz: those are the surviving terms of the hexagon.

## Result 2 (proved): triple-intersection criterion

Put A := x²⊞-yz, B := y²⊞-zx, C := z²⊞-xy.

**Lemma 2.**
(i) A∩B, B∩C and C∩A are all nonempty.
(ii) If A∩B∩C ≠ ∅, then 0 ∈ S.

*Proof.*
(ii) Let p ∈ A∩B∩C. Then xp ∈ x³⊞-xyz, yp ∈ y³⊞-xyz and zp ∈ z³⊞-xyz. Merging two summands into an element of their sum only shrinks a sum, so S ⊇ xp⊞yp⊞zp = p(x⊞y⊞z) ∋ 0.
(i) We have 0 ∈ x²⊞xy⊞xz (x times the hypothesis) and 0 ∈ -xy⊞-y²⊞-yz. Composing along xy gives 0 ∈ x²⊞xz⊞-y²⊞-yz = (x²⊞-yz)⊞-(y²⊞-zx). Since 0 ∈ P⊞-Q iff P∩Q ≠ ∅, this gives A∩B ≠ ∅. The other two pairs follow by symmetry. ∎

So a counterexample must violate a Helly-type property: the three sets meet pairwise but have no common point. In a quotient F/U one takes p = x'²-y'z' for lifts with x'+y'+z' = 0.

## Result 3 (proved): quotients of non-commutative or non-associative division rings satisfy the claim

This extends (A3) and rules out the most obvious "algebraic" non-quotient sources.

**Setting.** Let R be a ring with 1 in which every nonzero element has a two-sided inverse and both distributive laws hold. Multiplication need not be commutative or associative. Let R^× be its multiplicative loop, and let U ⊴ R^× be a normal subloop such that R^×/U is an abelian group; then the products [a][b] := [ab] are well defined. Define [a]⊞[b] := {[a'+b'] : a' ∈ [a], b' ∈ [b]}. This is the usual coset construction. Associativity of ⊞ comes from associativity of +, and distributivity from g(a+b) = ga+gb. (Whether R/U is a hyperfield in full generality is not needed here; I use only the two cases below.)

**Claim.** Suppose R is associative (a skew field), or R is alternative (e.g. the octonions), and R/U is a hyperfield as above. Then R/U satisfies the implication.

*Proof.* Take lifts x', y', z' with x'+y'+z' = 0.
- In the alternative case, Artin's theorem (cited from memory: in an alternative algebra any two elements generate an associative subalgebra) puts x', y', z' = -(x'+y') inside one associative subring. So we may compute associatively.
- Expand z'³ = -(x'+y')³ (in a skew field the expansion has 8 words). This gives
  x'³+y'³+z'³ = -(x'x'y' + x'y'x' + y'x'x' + x'y'y' + y'x'y' + y'y'x').
- Also x'y'z' = -(x'y'x' + x'y'y'), z'x'y' = -(x'x'y' + y'x'y') and y'z'x' = -(y'x'x' + y'y'x').
- Hence x'³+y'³+z'³ = x'y'z' + y'z'x' + z'x'y'.
- The three products lie in the class xyz, because R^×/U is abelian. So 0 = x'³+y'³+z'³-(x'y'z')-(y'z'x')-(z'x'y') is a representative sum of the target, and 0 ∈ S. ∎

The same computation works in any (non-associative) semifield with both distributive laws if cubes are bracketed as (aa)a. One uses (x'y')z', (z'x')y', (y'z')x', which expand to cover the six bracketed words (xx)y, (xy)x, (xy)y, (yx)x, (yx)y, (yy)x exactly once. The cube class does not depend on the bracketing, since R^×/U is a group.

## Result 4 (proved construction, unresolved claim): orbit hyperfields; near-field twists

**Construction.** Let A be an abelian group and M ≤ Aut(A) transitive on A\{0}. Let U ⊴ M contain the stabiliser M_e of some (hence every) e ≠ 0, with M/U abelian. Set H := {U-orbits on A}, with [a]⊞[b] := {[a'+b'] : a'∈[a], b'∈[b]}.
- G := M/U acts regularly on the nonzero orbits:
  - Transitivity comes from M.
  - Freeness: if m[ne] = [ne], then n⁻¹mn fixes [e], so n⁻¹mn·e = u·e for some u ∈ U. Then u⁻¹n⁻¹mn ∈ M_e ≤ U, so m ∈ U by normality.
- Identify mU ↔ [me] and define [me]·[m'e] := [mm'e].
- Then H is a hyperfield:
  - ⊞ is associative, since it is computed from + on A.
  - Negatives are unique, since 0 ∈ [a]⊞[b] iff [b] = [-a].
  - Reversibility holds: c' = a'+b' implies a' = c'-b'.
  - Distributivity holds because each m ∈ M is additive and permutes U-orbits.
  - Multiplication is commutative because M/U is abelian.

**Why the lifting proof fails.** Choose m_x, m_y, m_z ∈ M with m_x e = x', m_y e = y', m_z e = z', where x'+y'+z' = 0. Then (m_x+m_y+m_z)e = 0 in End(A), but m_x+m_y+m_z need not be 0. So nothing controls m_x³e + m_y³e + m_z³e. Quotients of fields are the case where M acts by scalar multiplication.

**Example (Dickson near-field twist).** Let F be a field, σ ∈ Aut(F) of order 2 with fixed field K, and χ: F^× → Z/2 a homomorphism with χ∘σ = χ and χ|_{K^×} = 0. Then:
- a∘b := a·σ^{χ(a)}(b) is a near-field multiplication on F, with multiplicative group M.
- M' = W := {σ(b)/b : χ(b) = 0}, an index-2 subgroup of ker N_{F/K}.
- U := W gives H = F/W as hyperaddition (a field quotient), but with twisted product [a]⋆[b] = [ab]·ε^{χ(a)χ(b)}, where ε := σ(c)/c for any c with χ(c) = 1, and ε ∉ W.
- In H, X^{⋆3} = [x³]ε^{χ(x)} and X⋆Y⋆Z = [xyz]ε^{e} with e = [at least two of χ(x), χ(y), χ(z) are 1].

Two observations:
- If χ(x) = χ(y) = χ(z), the whole target is multiplied by the same ε^{χ}, and the claim follows from the untwisted quotient F/W.
- Instances:
  - F = F_{p²} with χ the quadratic character gives |G| = 2(p-1). The orbits have size (p+1)/2, so the sums are dense.
  - F = Q(i) with χ(z) = v_{2+i}(z)+v_{2-i}(z) mod 2 is an infinite instance. There, when the archimedean polygon inequality for the target is an equality, the hypothesis triangle is degenerate. This forces x', y', z' to be proportional over Q_{>0}·W, hence to have equal χ, hence an untwisted target.
  - For mixed parities I expect, but have not proved, that the target holds by weak approximation: W is an open index-2 condition at the prime 5.

So this route (iii) gives genuine twisted non-field-multiplication hyperfields, but I found no instance where the claim fails.

## Result 5 (proved): a further sufficient condition

**Corollary of Lemma 2.** If one of A, B, C is a singleton, then 0 ∈ S. In the normalized form (z = -1) these sets are A = x²⊞y, B = y²⊞x and C = 1⊞-xy.

*Proof.* Say A = {p}. Lemma 2(i) gives A∩B ≠ ∅ and A∩C ≠ ∅, so p ∈ B and p ∈ C. Then A∩B∩C ∋ p, and Lemma 2(ii) applies. ∎

## Dead end: the free / chase construction (route (i))

The plan was to build a hyperfield freely from 1 ∈ x⊞y (with -1 = 1 imposed, and G free abelian on x, y and on fresh witnesses). Each chase step adds a fresh witness s for one instance of the 4-point condition (or of nonemptiness), together with its two triangles and all their G-translates.

I tried to prove that zero-sums among old elements are never created, by eliminating the newest witness. This fails, for the following reason.
- The translates s^k·g of s fill whole new cosets s^k G_old.
- Old relations translated by s, such as {s, sx, sy}, glue to the witness triangles {b,c,s}, {a,e,s} and their x- and y-translates.
- This produces genuinely new relations among old elements. Example: Z(b, c, ax, ex, by, cy), the analogue of s(1+x+y) = 0 with s "= b+c = a+e".

So witnesses act like ring elements multiplying relations. The free object's relation set is not the composition closure of the generating triangles. The linear-derivation obstructions of B-1/B-5/B-6 therefore do not by themselves show that the target fails in the free object.

Any invariant that blocks the target in the free object must itself be compatible with these witness steps. I only sketch why. Testing against a G-equivariant model of the triangle relation that admits witnesses amounts to testing against a hyperfield-like object (polygroup with regular abelian translations), which is the original problem again. So route (i) needs a genuinely new combinatorial invariant, and I did not find one.

## Summary of status

**Proved here:**
1. Hexagon lemma (Lemma 1). The target relation is exactly a closed cycle of six translates of the hypothesis. In every hyperfield, S meets μ(1⊞-1) for each μ ∈ {x²y, xy², y²z, yz², z²x, zx²}. So a counterexample needs non-trivial "holonomy" around this hexagon. Also: 1⊞-1 = {0} forces a field.
2. Triple-intersection criterion (Lemma 2): the sets x²⊞-yz, y²⊞-zx, z²⊞-xy meet pairwise, and if all three meet, the claim holds. Corollary: the claim holds if one of them is a singleton.
3. Quotients R^×/U of skew fields, of alternative division rings (octonions), and of semifields (cubes bracketed (aa)a) satisfy the claim.
4. Orbit hyperfields A/U with transitive M ≤ Aut(A) are hyperfields, and the field lifting proof does not transfer to them. Dickson near-field twists give explicit hyperfields with twisted multiplication [a]⋆[b] = [ab]ε^{χ(a)χ(b)}. In configurations where the three elements have equal twist parity, the claim holds there.

**Not proved / open:**
- The main question (N) remains open: I found neither a counterexample nor a proof.
- Specific open sub-questions:
  - (Q1) Does the Helly property A∩B∩C ≠ ∅ hold in every hyperfield? A yes would prove (N).
  - (Q2) Can the hexagon holonomy be nontrivial, i.e. is there a hyperfield with 0 ∉ S although S meets all six μ(1⊞-1)? This is just (N) restated.
  - (Q3) Does the claim hold in the twisted near-field hyperfields Q(i)/W (mixed parity), or in the finite twisted F_{p²}/μ_{(p+1)/2} for p ≥ 7? I expect yes, on density / weak-approximation grounds, but have not proved it.
  - (Q4) Is there a combinatorial invariant blocking the target in the free hyperfield on 1 ∈ x⊞y?
- Heuristic assessment (not a proof): every "algebraic" source tried (division-ring and semifield quotients, ordered extensions, orbit/near-field twists) either satisfies the claim or has dense sums. A counterexample, if one exists, should be a genuinely combinatorial (free-type) object in which x⊞y contains elements u ≠ 1 that block the needed "contraction" of x²y⊞xy² to xy.

=== END OF ANSWER round4_q5 ===

