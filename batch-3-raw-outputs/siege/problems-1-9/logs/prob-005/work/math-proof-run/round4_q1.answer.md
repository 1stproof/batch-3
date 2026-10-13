# round4_q1 — answer

**Verdict: COUNTEREXAMPLE to (N).** So the answer to the Question is **NO**.

The counterexample is an infinite hyperfield extension of the Krasner hyperfield (-1 = 1, a⊞a = {0,a}). It is built from a non-Desarguesian cyclic projective plane over the infinite cyclic group, made by M. Hall's greedy "free extension" of planar difference sets. (Hall, *Cyclic projective planes*, Duke Math. J. 1947, cited from memory. Everything Hall-related is proved below from scratch, so the citation is not needed.) Concretely, x = t, y = t^10, z = 1 = -1.

## 1. Planar difference sets in Z (proved)

A finite set S ⊂ Z is **Sidon** if the map (s,s') ↦ s - s' is injective on pairs with s ≠ s'. Equivalently, all positive differences s - s' (s > s') are pairwise distinct: a coincidence between two negative differences becomes one between positive differences after swapping each pair. A set D ⊂ Z is a **planar difference set** if every nonzero integer n has exactly one representation n = d - d' with d, d' ∈ D.

**Lemma 1 (Hall's extension).** Let S_0 be a finite Sidon set with M_0 = max_{s∈S_0}|s|. Then there is a planar difference set D ⊇ S_0 with D \ S_0 ⊂ (3M_0, ∞).

*Proof.* Build finite Sidon sets S_0 ⊂ S_1 ⊂ … inductively. Given S_k, let M_k = max|s| over s ∈ S_k. Let n_k be the least positive integer that is not a difference of S_k (it exists because S_k is finite). Choose an integer c_k > 3M_k + n_k and put S_{k+1} = S_k ∪ {c_k, c_k + n_k}. Note c_k > M_k, so both elements are new.

The positive differences of S_{k+1} are of three kinds:
- the old ones, all ≤ 2M_k;
- n_k;
- c_k - s and c_k + n_k - s for s ∈ S_k.

Each number of the third kind is ≥ c_k - M_k > 2M_k + n_k, so it differs from every old difference and from n_k. Two numbers c_k - s, c_k - s' (or c_k + n_k - s, c_k + n_k - s') agree only if s = s'. And c_k - s = c_k + n_k - s' would give s' - s = n_k, a difference of S_k, which contradicts the choice of n_k. Finally, n_k is not an old difference. So S_{k+1} is Sidon.

Every positive integer ≤ n_k is a difference of S_{k+1}: those below n_k already were differences of S_k, and n_k = (c_k + n_k) - c_k. Hence n_{k+1} > n_k, so n_k → ∞.

Put D = ⋃ S_k. Every positive n is ≤ some n_k, so it is a difference of D. Any two representations of n lie in a common S_k, which is Sidon, so they coincide. Negative n follow by swapping. Every added element exceeds 3M_k ≥ 3M_0. ∎

**The specific set.** Take S_0 = {0, 1, 10, 1003, 1011, 1030}. Its 15 positive differences are

1, 9, 10 (from {0,1,10}); 8, 19, 27 (from {1003,1011,1030}); 1003, 1011, 1030, 1002, 1010, 1029, 993, 1001, 1020 (cross differences).

These are pairwise distinct, so S_0 is Sidon. Let D be given by Lemma 1. Then D ∩ (-∞, 3090] = S_0. In particular **1000 ∉ D**, and D is infinite, because a finite set has only finitely many differences.

## 2. The hyperfield H_D (all axioms verified)

Let G = {t^n : n ∈ Z} be the infinite cyclic group and H = G ∪ {0}, with the usual multiplication (0·a = 0). The **lines** are L_g = {t^{g+d} : d ∈ D} for g ∈ Z. Each line is infinite.

**Lemma 2 (projective plane).**
- (a) Two distinct points t^m, t^n lie on exactly one common line, called ℓ(t^m, t^n).
- (b) Two distinct lines meet in exactly one point.
- (c) Multiplication by t^k maps L_g to L_{g+k}, so it maps lines to lines.

*Proof.*
- (a) t^m, t^n ∈ L_g iff m - g = d and n - g = d' with d, d' ∈ D. Then m - n = d - d', which has a unique representation, and g = m - d. Conversely, that representation gives such a g.
- (b) t^m ∈ L_g ∩ L_h iff m - g = d and m - h = d' with d, d' ∈ D. Then h - g = d - d' ≠ 0, which has a unique representation, and m = g + d.
- (c) This is clear. ∎

**Definition of ⊞.** For a, b ∈ G:
- 0 ⊞ a = a ⊞ 0 = {a}, and 0 ⊞ 0 = {0};
- a ⊞ a = {0, a};
- a ⊞ b = ℓ(a,b) \ {a, b} for a ≠ b.

So a "point on a line" and "collinear" refer to Lemma 2.

**Axioms.**
1. **Commutativity.** This is clear from the definition.
2. **Nonempty sums.** All lines are infinite, so a ⊞ b ≠ ∅ for a ≠ b.
3. **Negatives.** For a, b ∈ G we have 0 ∈ a ⊞ b iff a = b. Also 0 ∈ 0 ⊞ b iff b = 0. So -a = a is the unique negative, and -1 = 1.
4. **Distributivity.** For w = t^k this follows from Lemma 2(c), since multiplication by w preserves ℓ, equality and 0. For w = 0 both sides are {0}.
5. **Reversibility.** Since -b = b, we must show c ∈ a ⊞ b ⇒ a ∈ c ⊞ b.
   - a = 0: then c = b, and 0 ∈ b ⊞ b.
   - b = 0: then c = a, and a ∈ a ⊞ 0.
   - a = b ≠ 0: then c ∈ {0, a}, and a ∈ 0 ⊞ a and a ∈ a ⊞ a.
   - a ≠ b, both nonzero: then c ∈ ℓ(a,b) \ {a,b}. So c ≠ b and ℓ(c,b) = ℓ(a,b) ∋ a with a ∉ {c,b}, hence a ∈ c ⊞ b.
6. **Associativity.**
   - **Symmetry of membership.** For a, b, c ∈ H put Ψ(a,b,c) :⇔ a ∈ b ⊞ c. By reversibility (with -1 = 1) and commutativity, Ψ is invariant under all permutations of its arguments.
   - **Step (i).** e ∈ t ⊞ c ⇔ t ∈ e ⊞ c, which is the symmetry of Ψ. Since (a⊞b)⊞c = ⋃_{s∈a⊞b} s⊞c, we get e ∈ (a⊞b)⊞c ⇔ R(a,b,c,e), where R(a,b,c,e) :⇔ (a⊞b) ∩ (c⊞e) ≠ ∅.
   - **Reduction.** Likewise e ∈ a⊞(b⊞c) = (b⊞c)⊞a ⇔ R(b,c,a,e). So associativity follows once R is invariant under all permutations of its four arguments. R is invariant under swapping inside each pair and under swapping the two pairs, so it suffices to show R(a,b,c,e) ⇔ R(a,c,b,e).
   - **Some argument is 0.**
     - R(0,b,c,e) = Ψ(b,c,e) and R(0,c,b,e) = Ψ(c,b,e).
     - R(a,b,c,0) = Ψ(c,a,b) and R(a,c,b,0) = Ψ(b,a,c).
     - R(a,0,c,e) = Ψ(a,c,e) and R(a,c,0,e) = Ψ(e,a,c). The case c = 0 is symmetric to this one.

     All of these agree by the symmetry of Ψ.
   - **All arguments nonzero.** Directly from the definition:
     - for a = b and c = e, R is true (0 lies in both sums);
     - for a = b and c ≠ e, R ⇔ a ∈ ℓ(c,e) \ {c,e};
     - for a ≠ b and c ≠ e, R is true if ℓ(a,b) = ℓ(c,e) (an infinite line minus at most 4 points is nonempty); otherwise the two lines meet in one point p, and R ⇔ p ∉ {a,b,c,e}.

     We sort by the multiplicity pattern of the multiset {a,b,c,e}:
     - **{a,a,a,a}.** R is always true.
     - **{a,a,a,c}, c ≠ a.** Every arrangement pairs {a,a} with {a,c}, and a ∉ ℓ(a,c) \ {a,c}. So R is always false.
     - **{a,a,c,c}, c ≠ a.** The pairing {a,a}|{c,c} is true. The pairing {a,c}|{a,c} uses the same line, so it is also true. So R is always true.
     - **{a,a,c,e}, with a, c, e distinct.** In the pairing {a,a}|{c,e}, R ⇔ a,c,e are collinear. In the pairing {a,c}|{a,e}, either the lines are equal (a,c,e collinear: true) or they meet exactly at a (false). So R ⇔ a,c,e are collinear in every arrangement.
     - **Four distinct points, pairing {a,b}|{c,e}.** Claim: R ⇔ (all four collinear) or (no three collinear).

       If ℓ(a,b) = ℓ(c,e), all four are collinear and R is true.

       Otherwise let p be the meeting point. Every triple of the four points contains a pair from one side and one point from the other side. If such a triple is collinear, that one point lies on both lines, so it equals p. Conversely, if p is one of the four points, say p = a, then a,c,e are collinear. Also b ∉ ℓ(c,e), because otherwise b = p = a. So in this case "R false" means exactly that some three are collinear but not all four.

     So in all patterns R depends only on the multiset {a,b,c,e}. Hence R is fully symmetric, and ⊞ is associative. ∎

So H_D is a hyperfield. (It is a Krasner extension in the sense of Connes–Consani, which I recall without relying on it.)

## 3. The counterexample

Take x = t, y = t^10, z = 1 = t^0. Then:
- xyz = t^11 and -xyz = t^11;
- x^3 = t^3, y^3 = t^30, z^3 = 1.

**Hypothesis.** 0 ∈ (x⊞y)⊞z ⇔ there is s ∈ x⊞y with 0 ∈ s⊞1 ⇔ 1 ∈ x⊞y. The line L_0 = {t^d : d ∈ D} contains t^0, t^1 and t^10, because 0, 1, 10 ∈ D. So ℓ(t, t^10) = L_0, and 1 ∈ x⊞y holds.

**Target.**
- Write S = t^3 ⊞ t^30 ⊞ t^11 ⊞ t^11 ⊞ t^11. The target set is S ⊞ 1, and it contains 0 ⇔ 1 ∈ S, because 0 ∈ s⊞1 iff s = 1.
- Next, t^11 ⊞ t^11 ⊞ t^11 = {0, t^11} ⊞ t^11 = {t^11} ∪ {0, t^11} = {0, t^11}. So by associativity S = A ∪ (A ⊞ t^11), where A = t^3 ⊞ t^30.
- Since 3 + 1000 = 1003, 11 + 1000 = 1011 and 30 + 1000 = 1030 all lie in D, the line L_{-1000} contains t^3, t^11 and t^30. So ℓ(t^3, t^30) = L_{-1000} =: L1, and t^11 ∈ L1.
- t^0 ∈ L1 ⇔ 1000 ∈ D, which is false (Section 1). So 1 ∉ L1.
- Hence 1 ∉ A ⊆ L1.
- Suppose 1 ∈ s ⊞ t^11 for some s ∈ A ⊆ L1. If s = t^11, then s ⊞ s = {0, t^11} ∌ 1. If s ≠ t^11, then s ⊞ t^11 ⊆ ℓ(s, t^11) = L1 ∌ 1. Either way this is a contradiction.
- So 1 ∉ S, and **0 ∉ x^3 ⊞ y^3 ⊞ z^3 ⊞ -xyz ⊞ -xyz ⊞ -xyz**, although 0 ∈ x⊞y⊞z.

**In the normalized form (N).** Here -z^{-1} = 1, so x and y are unchanged, and 1 ∈ x⊞y while 1 ∉ T = x^3⊞y^3⊞xy⊞xy⊞xy. This is exactly S above. The same computation also refutes the stronger core claim (C): 1 ∉ x^3⊞y^3⊞xy.

## 4. Remarks

- **Consistency with the background.**
  - The hyperfield is infinite, which is consistent with (C1): no counterexample was found among small ones.
  - It is not a quotient F/U, which is consistent with (A3).
  - It lies in the Krasner-extension class of (C3). That class was considered unpromising only because all *finite* cyclic planes known are Desarguesian. Infinite cyclic planes built by free extension need not be Desarguesian.
- **The incidence translation behind it.** In a Krasner extension coming from a projective plane, the claim fails exactly when 1, x, y are collinear, the points 1, x^3, y^3 are not collinear, and the meeting point of the lines ℓ(1, xy) and ℓ(x^3, y^3) is one of the four points. Here that happens because x^3, y^3 and xy are collinear. Free extension lets one impose this configuration while forbidding the collinearity of 1, x^3, y^3.
- **Status.** The derivation in the task file (that (N) is equivalent to the question) is correct, but it is not needed: the counterexample is checked directly in the original form. Nothing remains open for this question. The answer is NO, by a complete and fully verified counterexample.

=== END OF ANSWER round4_q1 ===
