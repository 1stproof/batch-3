The document below is a draft proof. Check the argument step by step: for every inequality, interchange, cited result, and 'it follows that', ask whether it actually follows as written. List every error or gap in order of severity, and say explicitly whether the main claim is proved.

## The draft proof

# Answer: NO

**Theorem.** There is a hyperfield H with elements x, y, z such that 0 ∈ x⊞y⊞z but
0 ∉ x^3⊞y^3⊞z^3⊞(-xyz)⊞(-xyz)⊞(-xyz).

H is infinite. Its multiplicative group is infinite cyclic, ⟨t⟩ ≅ Z, and we can take x = t, y = t^4, z = 1.

Throughout, "hyperfield" means the standard notion (Krasner; Viro; Baker–Bowler). This is a set H with an element 0 and the following structure:
- a commutative, associative hyperoperation ⊞ with nonempty values, in which 0 is neutral;
- unique negatives, meaning that for each a there is exactly one b with 0 ∈ a⊞b;
- reversibility: c ∈ a⊞b ⇒ a ∈ c⊞(-b);
- a multiplication making H \ {0} an abelian group, with 0·h = 0 and w(a⊞b) = wa⊞wb.

Sums of sets are taken elementwise, A⊞B = ⋃_{a∈A, b∈B} a⊞b. By associativity, iterated sums do not depend on the bracketing.

## 1. Hyperfields from projective planes with a regular abelian group

Let G be an abelian group, written multiplicatively. Consider an incidence structure with point set G and a family of subsets called lines, satisfying:
- (P1) any two distinct points lie on exactly one line;
- (P2) any two distinct lines meet;
- (P3) every line has at least 5 points;
- (P4) for every w ∈ G, multiplication by w maps lines to lines.

By (P1), two distinct lines meet in exactly one point. Write L(a,b) for the line through the distinct points a and b.

Put H = G ∪ {0}. Let 0 be neutral (0⊞a = a⊞0 = {a}, and 0⊞0 = {0}). For nonzero a, b set
- a⊞a = {0, a};
- a⊞b = L(a,b) \ {a,b} for a ≠ b.

Multiplication is the group law on G, extended by 0·h = h·0 = 0.

**Proposition 1.** H is a hyperfield, and -a = a for every a.

*Proof.*

*Commutativity and nonempty values.* Commutativity is clear. For a ≠ b, the set a⊞b has at least 3 points by (P3), so every value is nonempty.

*Negatives.* Let a ≠ 0. For b ≠ a with b nonzero, a⊞b ⊆ G, so 0 ∉ a⊞b. Also 0⊞a = {a} does not contain 0, while 0 ∈ a⊞a. Hence a is the unique negative of a. The element 0 is its own unique negative.

*Reversibility.* We show c ∈ a⊞b ⇒ a ∈ c⊞b.
- If a = 0, then c = b and 0 ∈ b⊞b; this includes the case b = 0.
- If b = 0, then c = a and a ∈ a⊞0.
- If a = b ≠ 0, then c ∈ {0, a}. If c = 0, then a ∈ 0⊞a. If c = a, then a ∈ a⊞a.
- If a ≠ b, both nonzero, then c ∈ L(a,b) \ {a,b}. Since c ≠ b, L(c,b) = L(a,b), so c⊞b = L(a,b) \ {c,b}. This set contains a, because a ≠ c and a ≠ b.

*Distributivity.* For w ∈ G, multiplication by w is a bijection of G that maps lines to lines (P4). So w·L(a,b) = L(wa,wb), hence w(L(a,b)\{a,b}) = L(wa,wb)\{wa,wb}. Also w{0,a} = {0,wa} = wa⊞wa, and the cases involving 0 are trivial. The case w = 0 is trivial too.

*Associativity.* If one of a, b, c is 0, both (a⊞b)⊞c and a⊞(b⊞c) equal the sum of the other two, because 0 is neutral.

Now let a, b, c be nonzero and put S(a,b,c) := (a⊞b)⊞c. We show that S depends only on the multiset {a,b,c}. Then, using commutativity,
a⊞(b⊞c) = (b⊞c)⊞a = S(b,c,a) = S(a,b,c) = (a⊞b)⊞c.

1. **a = b = c.** S = (0⊞a) ∪ (a⊞a) = {0, a}.

2. **Multiset {a, a, c} with a ≠ c; let L = L(a,c).** There are two distinct orderings up to commutativity.
   - (a⊞a)⊞c = (0⊞c) ∪ (a⊞c) = {c} ∪ (L \ {a,c}) = L \ {a}.
   - (a⊞c)⊞a = ⋃_{p ∈ L\{a,c}} (p⊞a) = ⋃_{p ∈ L\{a,c}} (L \ {p,a}). The point a lies in none of these sets. Any point q ∈ L \ {a} is missing from L \ {p,a} only when p = q, and there are at least 3 choices of p. So the union is L \ {a}.

3. **a, b, c distinct and collinear on a line L.** Here a⊞b = L \ {a,b}, which contains c. Then
   S = (c⊞c) ∪ ⋃_{p ∈ L\{a,b,c}} (L \ {p,c}) = {0, c} ∪ (L \ {c}) = L ∪ {0}.
   This uses that L \ {a,b,c} has at least 2 points (P3). The result is symmetric in a, b, c.

4. **a, b, c not collinear.** We claim S = G \ (L(a,b) ∪ L(b,c) ∪ L(a,c)), which is symmetric in a, b, c. By definition,
   S = ⋃_{p ∈ L(a,b)\{a,b}} (L(p,c) \ {p,c}).
   Here p ≠ c, because c ∉ L(a,b). Also L(p,c) ≠ L(a,b), so L(p,c) ∩ L(a,b) = {p}.
   - 0 ∉ S, and c ∉ S.
   - **Points of L(a,b) are not in S**, including a and b. Such a point lies in L(p,c) only if it equals p, and p is excluded.
   - **Points q ∈ L(a,c) \ {a,c} are not in S.** If q ∈ L(p,c) \ {p,c}, then L(p,c) = L(q,c) = L(a,c). So p ∈ L(a,c) ∩ L(a,b) = {a}, since these lines are distinct; this contradicts p ≠ a.
   - **Points q ∈ L(b,c) \ {b,c} are not in S**, by the same argument with b in place of a.
   - **Every other point q of G is in S.** Here q lies on none of the three lines. The lines L(q,c) and L(a,b) are distinct because c ∉ L(a,b), so by (P2) they meet in a point p. Then p ≠ a, since otherwise q ∈ L(a,c). Likewise p ≠ b. Also p ≠ q, since q ∉ L(a,b), and p ≠ c. So q ∈ L(p,c) \ {p,c} with p ∈ L(a,b) \ {a,b}, hence q ∈ S.

These cases cover every multiset of three nonzero elements, so ⊞ is associative. ∎

## 2. The six-term sum in such an H

**Lemma 2.** Let H be as in §1, and let x, y ∈ G satisfy:
- the points 1, x, y are distinct and collinear;
- the points x^3, y^3, xy are distinct and lie on a line M with 1 ∉ M.

Then with z = 1 we have 0 ∈ x⊞y⊞z, but 0 ∉ x^3⊞y^3⊞z^3⊞(-xyz)⊞(-xyz)⊞(-xyz).

*Proof.*

*The hypothesis holds.* Since 1, x, y are distinct and collinear, 1 ∈ L(x,y) \ {x,y} = x⊞y. Hence (x⊞y)⊞1 ⊇ 1⊞1 ∋ 0.

*The target fails.* Every element is its own negative, so -xyz = xy; also z^3 = 1. The target sum is therefore T⊞1, where T := x^3⊞y^3⊞xy⊞xy⊞xy.
- First, xy⊞xy⊞xy = {0,xy}⊞xy = {xy} ∪ {0,xy} = {0, xy}.
- So T = (x^3⊞y^3)⊞{0,xy} = (x^3⊞y^3) ∪ ((x^3⊞y^3)⊞xy).
- The first part is M \ {x^3, y^3}. The second part is M ∪ {0}, by case 3 of the associativity proof (x^3, y^3, xy are distinct and collinear on M).
- Hence T = M ∪ {0}.

Finally, T⊞1 = ⋃_{u∈T} u⊞1. By uniqueness of negatives, 0 ∈ u⊞1 iff u = 1. Since 1 ∉ M and 1 ≠ 0, we get 1 ∉ T, so 0 ∉ T⊞1. ∎

## 3. A plane containing the required configuration

Now write G = Z additively. The integer n stands for the group element t^n, so the identity 1 corresponds to 0, and multiplication corresponds to addition.

A set D ⊂ Z is a **perfect difference set** if every nonzero integer has exactly one representation d - d' with d, d' ∈ D.

**Lemma 3.** If D ⊂ Z is an infinite perfect difference set, then the lines {g + D : g ∈ Z} on the point set Z satisfy (P1)–(P4).

*Proof.*
- (P1): distinct points p, q lie on g + D iff p - g = d1 and q - g = d2 for some d1, d2 ∈ D. Then p - q = d1 - d2. This representation exists and is unique, so g = p - d1 exists and is unique.
- (P2): for g ≠ h, let h - g = d1 - d2 be the representation. Then the lines g + D and h + D share the point g + d1 = h + d2.
- (P3): every line is infinite.
- (P4): translating g + D by w gives (g+w) + D, which is again a line. ∎

**Lemma 4.** There is an infinite perfect difference set D ⊂ Z with D ⊇ D_0 := {0, 1, 4, 103, 105, 112} and 100 ∉ D.

*Proof.* Call a finite set *Sidon* if every nonzero integer has at most one representation as a difference of two of its elements.

*D_0 is Sidon.* Its 15 positive differences are 1, 3, 4, 2, 7, 9, 99, 101, 102, 103, 104, 105, 108, 111, 112. These are pairwise distinct. (This was checked by computer and is also easy to check by hand.)

*Inductive step.* Let D_k be a finite Sidon set of nonnegative integers, and define:
- m: the least positive integer that is not a difference of D_k;
- R: max D_k;
- N: an integer with N > 3R + m.

Put D_{k+1} = D_k ∪ {N, N+m}. These are new elements, since N > R. The new positive differences are m = (N+m) - N, the numbers N - d, and the numbers N + m - d, for d ∈ D_k. We check that all differences of D_{k+1} are distinct:
- Old positive differences are at most R. Every N - d and every N + m - d is at least N - R > 2R + m. So these exceed both the old differences and m.
- The values N - d are pairwise distinct, and so are the values N + m - d.
- If N - d = N + m - d', then d' - d = m, which would make m a difference of D_k. This is impossible.
- m itself is not an old difference, by its choice.

So D_{k+1} is Sidon, and m is now a difference.

*Covering.* Every difference of D_k remains a difference of D_{k+1}, and m becomes one. So the least positive non-difference strictly increases at each step. Hence every positive integer is eventually a difference, and by symmetry so is every negative integer.

*The limit set.* Let D = ⋃_k D_k. D is infinite. Any two representations of the same nonzero integer already lie in a common D_k, so they coincide. By covering, every nonzero integer has at least one representation. So D is a perfect difference set.

*100 ∉ D.* 100 ∉ D_0, and every added element is at least N > 3·112 > 100. ∎

## 4. The counterexample

Let D be as in Lemma 4. By Lemma 3, the lines g + D on Z satisfy (P1)–(P4), so Proposition 1 gives a hyperfield H = ⟨t⟩ ∪ {0}. Take x = t, y = t^4, z = 1; in additive notation x ↔ 1, y ↔ 4 and 1_H ↔ 0. We check the hypotheses of Lemma 2.
- **The points 1_H, x, y** are 0, 1, 4. They are distinct and all lie on the line D.
- **The points x^3, y^3, xy** are 3, 12, 5. They are distinct and lie on the line M = -100 + D, because 103, 112, 105 ∈ D.
- **1_H is not on M.** The point 0 lies on M iff 100 ∈ D, which is false.

By Lemma 2, 0 ∈ x⊞y⊞z but 0 ∉ x^3⊞y^3⊞z^3⊞(-xyz)⊞(-xyz)⊞(-xyz). This proves the Theorem, so the answer to the question is **NO**. ∎

*Remark (no logical weight).* No quotient hyperfield F/K^× of a commutative field F can be a counterexample. If 0 ∈ x⊞y⊞z there, then there are representatives X, Y, Z ∈ F with X+Y+Z = 0. The identity X^3+Y^3+Z^3-3XYZ = (X+Y+Z)(X^2+Y^2+Z^2-XY-YZ-ZX) then puts 0 in the target sum, using the representative -XYZ three times. This is why the counterexample has to come from a non-Desarguesian plane.

## 5. Other routes recorded during the attempt

None of the following is needed for the Theorem. They were proved by individual workers in earlier rounds and were not re-audited for this document, so they are listed as reported.
- **Composition obstruction.** If 0 ∈ A⊞t and 0 ∈ B⊞(-t), then 0 ∈ A⊞B. However, no chain of such compositions applied to scaled copies of the hypothesis, 0 ∈ wx⊞wy⊞wz, reaches the target. This is a formal-monomial argument, and it has a variant for chains of 4-point exchanges when -1 = 1. It explains why no "linear" proof exists, and that is consistent with the counterexample.
- **Positive special cases.** The implication holds in the following cases:
  - when x = y in normalized form;
  - in hyperfields where a⊞-a = H for all a ≠ 0 (any multi-sum with two opposite nonzero summands is all of H);
  - when -1 = 1 and g^2 = 1 for all g;
  - in quotients of skew fields and alternative division rings, via a "hexagon lemma" (the target meets μ(1⊞-1) for each mixed monomial μ) and a Helly-type criterion.
- **Reductions.** When -1 = 1, the goal follows from the three-term statement (C): 1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy. In idempotent hyperfields (a⊞a = {a}), the goal is equivalent to (C). The hyperfield above also refutes (C): there T ⊇ x^3⊞y^3⊞xy, and T does not contain 1.
- **Up-closure.** Every hyperfield K has an up-closure in the class a⊞-a = H. Within that class the claim is equivalent to a weak zero-sum statement in all hyperfields.
- **Parallel counterexamples.** Several independent workers found the same mechanism with other seed difference sets, e.g. {0,1,7,100,103,108} and {0,1,3,20,24,29}. In every case the idea is an infinite non-Desarguesian plane on Z, built from a greedy perfect difference set that contains a prescribed configuration.

## Status

- **Settled.** The answer is NO, by the Theorem. §§1–4 are complete and self-contained. The argument was checked step by step by two independent referees, and every step was re-read for this document. The Sidon property of D_0, and of a few greedy extensions, was confirmed by computer.
- **Open.** It is not known whether a *finite* counterexample exists, and the question as posed does not require one. The construction here needs a plane with a regular abelian collineation group containing a non-Desarguesian configuration. For finite cyclic planes, whether any such plane is non-Desarguesian is a well-known open problem (recalled from memory). A small computer search, reported by one worker, found no counterexample with |G| ≤ 9.
