# Answer to round4_q7: NO, the statement (N) is false (task part (b))

**Result (proved below).** There is a hyperfield H with -1 = 1, and elements x, y, z with 0 ∈ x⊞y⊞z, such that
0 ∉ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz.
So the answer to the Question is **No**. In the normalized form (N), this hyperfield has x, y ∈ G with 1 ∈ x⊞y and 1 ∉ x^3⊞y^3⊞xy⊞xy⊞xy.

The counterexample does not use a term model of the zero-sum calculus. It is an extension of the Krasner hyperfield built from a projective plane. The plane is a *free* (non-Desarguesian) projective plane whose point set is a free abelian group of countable rank, with that group acting regularly by translations. In such a plane the configuration "1, x, y collinear; 1, x^3, xy collinear; y^3 not on that line" can be imposed. Desarguesian planes, which are quotients, forbid it. The coordinator's remark (C3) judged this class unpromising, but that remark only considered Desarguesian geometries.

Notation: the multiplicative group G is written additively as A. The group identity "1" is the element 0 of A. The zero of the hyperfield is written ∞.

## 1. Projective planes with a regular abelian group give hyperfields

**Lemma 1.** Let A be an abelian group (written additively), and let 𝓛 be a family of subsets of A ("lines") such that:
- (P1) any two distinct points lie on exactly one line;
- (P2) any two distinct lines meet in exactly one point;
- (P3) every line has at least 4 points;
- (P4) 𝓛 is invariant under all translations p ↦ p + w.

Put H = A ∪ {∞}. Multiplication is the group law of A, with ∞·h = ∞. Every element is its own negative. Addition is defined as follows:
- ∞ ⊞ a = a ⊞ ∞ = {a};
- a ⊞ a = {∞, a} for a ∈ A;
- for distinct a, b ∈ A, a ⊞ b = ℓ(a,b) \ {a,b}, where ℓ(a,b) is the line through a and b.

Then H is a hyperfield in the sense of the task. Here -1 = 1, i.e. -a = a.

*Proof.* All sums are nonempty, since lines have at least 3 points. Commutativity is clear. Multiplication by w ∈ A is the translation by w. That map sends lines to lines (P4), fixes ∞, and sends {∞, a} to {∞, a+w}, so w(a⊞b) = wa⊞wb.

*The ternary relation.* Define T(p,q,r) :⇔ r ∈ p⊞q, for p, q, r ∈ H. Directly from the definition, T(p,q,r) holds iff one of the following holds:
- two of p, q, r are ∞ and the third is ∞;
- exactly one of them is ∞ and the other two are equal;
- none is ∞, and either p = q = r, or p, q, r are three distinct collinear points.

Check of the case "none is ∞": if p = q then p⊞q = {∞, p}, so r = p; if p ≠ q, then r ∈ ℓ(p,q) \ {p,q}. Each condition in the list is symmetric in p, q, r, so T is totally symmetric. This gives:
- 0_H-uniqueness: ∞ ∈ a⊞b ⇔ T(a,b,∞) ⇔ a = b. So the negative of a is unique and equals a.
- Reversibility: c ∈ a⊞b ⇔ T(a,b,c) ⇔ T(c,b,a) ⇔ a ∈ c⊞b = c⊞(-b).

*Associativity.* Put R(a,b,c,e) :⇔ (a⊞b) ∩ (c⊞e) ≠ ∅, i.e. ∃t: T(a,b,t) ∧ T(c,e,t).

We have e ∈ (a⊞b)⊞c ⇔ ∃t ∈ a⊞b with e ∈ t⊞c ⇔ ∃t ∈ a⊞b with t ∈ e⊞c (symmetry of T) ⇔ R(a,b,c,e). Likewise e ∈ a⊞(b⊞c) = (b⊞c)⊞a ⇔ R(b,c,a,e). By definition R is invariant under a↔b, under c↔e, and under swapping the two pairs. So associativity follows once R depends only on the multiset {a,b,c,e}. This means checking that the three pairings {ab|ce}, {ac|be}, {ae|bc} agree.

- *Some entry is ∞*, say e = ∞. Then R(a,b,c,∞) ⇔ ∃t: T(a,b,t) ∧ t = c ⇔ T(a,b,c). The pairing {a∞|bc} gives ∃t: t = a ∧ T(b,c,t) ⇔ T(a,b,c) as well. Since T is symmetric, every pairing is equivalent to T of the other three entries. This also covers the cases with several ∞'s.

- *All entries in A, pairwise distinct.* Then t = ∞ is impossible, and so is t ∈ {a,b}. So R(a,b,c,e) ⇔ (ℓ(a,b) \ {a,b}) ∩ (ℓ(c,e) \ {c,e}) ≠ ∅.
  - If all four points are collinear on m, every pairing gives m \ {a,b,c,e} ≠ ∅. This is true for every pairing, since |m| ≥ 5 in our application; in general the condition "|m| ≥ 5" is the same for all pairings.
  - If exactly three are collinear, say a, b, c on m and e ∉ m, then in every pairing one pair spans m and the other pair is {p, e} with p ∈ m. The line ℓ(p,e) meets m only in p, and p is excluded. So every pairing is false.
  - If no three are collinear, ℓ(a,b) ≠ ℓ(c,e) meet in a point q (P2), and q ∉ {a,b,c,e}: for example q = a would make a, c, e collinear. So every pairing is true.

- *Multiset {a,a,c,e}* with a, c, e ∈ A pairwise distinct.
  - {aa|ce}: {∞,a} ∩ (c⊞e) ≠ ∅ ⇔ a ∈ c⊞e ⇔ a, c, e collinear.
  - {ac|ae}: if a, c, e lie on a line m, the intersection is m \ {a,c,e}, which is nonempty by (P3). Otherwise ℓ(a,c) ∩ ℓ(a,e) = {a}, and a is excluded.
  - So both pairings say "a, c, e collinear".

- *Multiset {a,a,c,c}*, a ≠ c. Both pairings are true: {∞,a} ∩ {∞,c} ∋ ∞, and a⊞c ≠ ∅.

- *Multiset {a,a,a,e}* (only one pairing) and *{a,a,a,a}* (only one pairing): nothing to check.

So R is symmetric, ⊞ is associative, and H is a hyperfield. ∎

(For the record: from memory, this is the classical construction of a hypergroup from a projective geometry with at least 4 points per line, due to Prenowitz and Lyndon and used by Connes–Consani for extensions of the Krasner hyperfield. The proof above is self-contained and does not rely on that citation.)

## 2. Failure of the claim in such a plane

**Lemma 2.** In the setting of Lemma 1, suppose x, y ∈ A satisfy the following (additive notation, so 1 = 0, x^3 = 3x, xy = x+y, y^3 = 3y):
- (i) 0, x, y are distinct and collinear;
- (ii) 0, 3x, x+y are distinct and lie on a line L;
- (iii) 3y ∉ L.

Then, with z = 1 (the element 0 of A), we have 0_H ∈ x⊞y⊞z, but 0_H ∉ x^3⊞y^3⊞z^3⊞(-xyz)⊞(-xyz)⊞(-xyz).

*Proof.* The hypothesis: x⊞y = ℓ(x,y) \ {x,y} contains the point 0 by (i). Hence ∞ ∈ x⊞y⊞0.

The target: since -1 = 1 and z = 1, the target sum is S = T ⊞ 1, where T = x^3⊞y^3⊞xy⊞xy⊞xy. For a set U, ∞ ∈ U ⊞ 1 ⇔ 1 ∈ U, so it suffices to show 1 ∉ T.

We have xy⊞xy = {∞, xy}, and then xy⊞xy⊞xy = (∞⊞xy) ∪ (xy⊞xy) = {∞, xy}. Hence T = (x^3⊞y^3) ∪ ((x^3⊞y^3)⊞xy).

Let M = ℓ(3x, 3y); note 3x ≠ 3y because 3y ∉ L ∋ 3x. Since 3y ∉ L, M ≠ L, and the two lines meet exactly in 3x.
- 1 ∈ x^3⊞y^3 = M \ {3x,3y} would put the point 0 on M. But 0 ∈ L and 0 ≠ 3x, so 0 ∉ M.
- 1 ∈ (x^3⊞y^3)⊞xy ⇔ ∃t ∈ x^3⊞y^3 with 1 ∈ t⊞xy ⇔ ∃t ∈ (x^3⊞y^3) ∩ (1⊞xy), by reversibility. Here x^3⊞y^3 = M \ {3x,3y}. Also 1⊞xy = L \ {0, x+y}, since L is the line through 0 and x+y. Now M ∩ L = {3x}, and 3x is excluded from M \ {3x,3y}. So the intersection is empty.

Hence 1 ∉ T, and the target fails. ∎

Remark (consistency check): in Desarguesian planes coming from quotients F_{q^3}/F_q^*, write x' + y' = 1. Then y'^3 = 1 - x'^3 - 3x'y' lies in the span of 1, x'^3, x'y'. So (ii) forces y^3 ∈ L, and (iii) cannot hold. This agrees with (A3).

## 3. A free planar difference set realizing (i)–(iii)

Translation-invariant planes on A with a single line orbit are given by a set D ⊂ A with:
- **(Sidon)** d1 - d2 = d3 - d4 with d1 ≠ d2 and d3 ≠ d4 forces (d1,d2) = (d3,d4);
- **(Cover)** D - D = A.

**Lemma 3.** If D is infinite and satisfies (Sidon) and (Cover), then 𝓛 = {D + h : h ∈ A} satisfies (P1)–(P4).

*Proof.*
- (P4) is clear.
- Distinct h give distinct lines: if D + h = D + h' with h ≠ h', then w = h' - h ≠ 0 and D + w = D. Then (d + w) - d = w for every d ∈ D, giving two different pairs with the same difference, contrary to (Sidon).
- (P1): for points p ≠ q, the line D + h contains both iff (q - h, p - h) is a pair in D with difference q - p. By (Cover) and (Sidon) there is exactly one such pair, and it determines h.
- (P2): lines D + h ≠ D + h' meet in p iff p - h, p - h' ∈ D. These two elements differ by h' - h ≠ 0, and there is exactly one pair (d, d') in D with d - d' = h' - h. So there is exactly one common point p = d + h.
- (P3): D is infinite. ∎

**Construction.**
- Let A_0 = Z^3 with free generators X, Y, u.
- Let D_0 = {0, X, Y, u, u+3X, u+X+Y}.

D_0 is Sidon. The differences inside {0,X,Y} are ±X, ±Y, ±(X-Y). The differences inside {u, u+3X, u+X+Y} are ±3X, ±(X+Y), ±(2X-Y). The cross differences are ±(u + s - f) with s ∈ {0, 3X, X+Y} and f ∈ {0, X, Y}. The nine values of s - f are 0, -X, -Y, 3X, 2X, 3X-Y, X+Y, Y, X, which are pairwise distinct. The cross differences have u-coefficient ±1, the others have u-coefficient 0. So all 30 ordered differences are distinct.

*Extension step.* Suppose D_n ⊂ A_n is a finite Sidon set, and a ∈ A_n \ ({0} ∪ (D_n - D_n)). Put A_{n+1} = A_n ⊕ Z t_n (t_n a new free generator) and D_{n+1} = D_n ∪ {t_n, t_n + a}. Then D_{n+1} is Sidon and a ∈ D_{n+1} - D_{n+1}. The new differences are ±a, ±(t_n - d) and ±(t_n + a - d) for d ∈ D_n.
- ±a are not old differences, because D_n - D_n is symmetric and a is not in it. Also a ≠ -a, since the group is torsion-free.
- The differences containing t_n differ from all others by their t_n-coefficient.
- Among themselves, a coincidence t_n - d = t_n + a - d' gives a = d' - d. This is either 0 or an element of D_n - D_n, which is excluded.
- Coincidences t_n - d = t_n - d' and t_n + a - d = t_n + a - d' force d = d'.

*Dovetailing.* When A_i is created, fix an enumeration (a_{i,k})_k of it; A_i is countable. Fix a bijection N → N×N, n ↦ (i(n), k(n)), with i(n) ≤ n (e.g. the inverse of the Cantor pairing).
- At stage n, look at a = a_{i(n),k(n)} ∈ A_{i(n)} ⊆ A_n.
- If a ≠ 0 and a ∉ D_n - D_n, apply the extension step.
- Otherwise put A_{n+1} = A_n and D_{n+1} = D_n.

Let A = ∪ A_n, which is free abelian of countable rank, hence abelian and torsion-free, and let D = ∪ D_n.
- D is Sidon, because any two pairs lie in a common D_n.
- D satisfies (Cover): every nonzero a ∈ A equals some a_{i,k}, and this element is treated at the stage n with (i(n),k(n)) = (i,k).
- D is infinite, since D - D = A is infinite.

By Lemmas 3 and 1, the lines D + h make H = A ∪ {∞} a hyperfield.

**Verification of (i)–(iii).** Take x = X and y = Y.
- (i) 0, X, Y ∈ D are distinct and lie on the line D.
- (ii) The line L = D - u contains u - u = 0, (u+3X) - u = 3X and (u+X+Y) - u = X+Y. These three points are distinct.
- (iii) 3Y ∈ L ⇔ 3Y + u ∈ D. The element 3Y + u lies in A_0. It is not in D_0, and every element of D \ D_0 has a nonzero coefficient on some t_n, so it is not in A_0. Hence 3Y ∉ L.

Key point: free extension steps only add *new* points to D. Incidences among the old points of A_0 are never changed.

By Lemma 2, in this hyperfield we have 0 ∈ x⊞y⊞z for x = X, y = Y, z = 1, but 0 ∉ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz.

## 4. Summary

**Proved.** The answer to the Question is **No**. The counterexample is a hyperfield H = A ∪ {0}, where:
- A is free abelian of countable rank;
- -1 = 1 and 1⊞1 = {0,1}, so H is an extension of the Krasner hyperfield;
- H comes from a free projective plane whose lines are the translates of an infinite planar Sidon set D ⊂ A.

With x = X, y = Y, z = 1, the hypothesis 0 ∈ x⊞y⊞z holds and the conclusion fails.

**Consistency with the earlier evidence.**
- H is infinite, so it is consistent with the search result (C1).
- Its plane is non-Desarguesian, so H is not one of the quotients in (A3).
- It also fails the stronger core claim (C) of B-3, as Lemma 2 shows.
- Therefore no derivation of the kind asked for in task part (a) exists.

**Not addressed.** Whether a *finite* counterexample exists remains open. A finite one of this type would need a finite non-Desarguesian plane with an abelian Singer group, which is conjecturally impossible. The case -1 ≠ 1 is also not needed and not addressed: one counterexample settles the question.

=== END OF ANSWER round4_q7 ===
