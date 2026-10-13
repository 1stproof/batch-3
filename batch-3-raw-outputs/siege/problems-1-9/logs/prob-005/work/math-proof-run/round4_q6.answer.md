# Answer to round4_q6: the answer is NO (a complete counterexample)

**Plan / status.** I did not follow the free-hyperfield chase. A much more explicit counterexample exists, so I went straight to it. It is a "Krasner-type" hyperfield (-1 = 1, a⊞a = {0,a}) built from an **infinite cyclic projective plane**, which in turn comes from a perfect difference set in Z (M. Hall's greedy construction; that construction is reproved below). The coordinator's remark (C3) looked only at finite geometries, which are all Desarguesian. Infinite cyclic planes are not Desarguesian in general, and that is where the counterexample lives. Every step below is proved in full.

**Theorem.** There is a hyperfield H with elements x, y, z such that 0 ∈ x⊞y⊞z but 0 ∉ x³⊞y³⊞z³⊞(-xyz)⊞(-xyz)⊞(-xyz). Equivalently, (N) fails.

## 1. A perfect difference set

**Lemma 1.** Let D_0 = {0,1,3,20,24,29}. There is a set D ⊆ Z with D ⊇ D_0 such that every nonzero integer n can be written in exactly one way as n = d - d' with d, d' ∈ D.

*Proof.* Call a finite set S ⊂ Z *Sidon* if the differences d - d' (d ≠ d' in S) are pairwise distinct.

D_0 is Sidon. Its 15 positive differences are 1,3,2,20,19,17,24,23,21,4,29,28,26,9,5, and these are pairwise distinct.

Construct D_k inductively. Given a finite Sidon set D_k, let m_k be the least positive integer that is not a difference of D_k. Let M = max_{d∈D_k}|d|, choose an integer a > 2M + m_k, and set D_{k+1} = D_k ∪ {a, a+m_k}.

The positive differences of D_{k+1} that are not differences of D_k are:
- m_k;
- a - d for d ∈ D_k;
- a + m_k - d for d ∈ D_k.

They are pairwise distinct and distinct from the old differences:
- Every old difference is ≤ 2M.
- Each a - d and each a + m_k - d is ≥ a - M > M + m_k, so it exceeds m_k and also exceeds every old difference (old differences are ≤ 2M < a - M).
- m_k is not an old difference, by its choice.
- The values a - d are pairwise distinct, and so are the values a + m_k - d.
- If a - d = a + m_k - d', then d' - d = m_k. This is impossible: m_k > 0 is not a difference of D_k.

So D_{k+1} is Sidon, and m_k is now a difference. Every integer below m_k was already a difference of D_k, so m_{k+1} > m_k. Hence every positive integer is a difference of some D_k.

Let D = ∪_k D_k. Every positive integer n is a difference d - d' in D. Then -n = d' - d, so every nonzero integer is a difference.

Uniqueness: two representations of the same n would already lie in some finite D_k, which is Sidon. ∎

D is infinite. Note in particular **23 ∉ D**. Otherwise 3 = 23 - 20 and 3 = 3 - 0 would be two different representations of 3.

## 2. The cyclic plane

Points are the integers. Lines are the translates t + D (t ∈ Z).

**Lemma 2.**
- (L1) Two distinct points lie on exactly one line.
- (L2) Two distinct lines meet in exactly one point.
- (L3) Every line is infinite.
- (L4) Translation maps lines to lines.

*Proof.*

(L4) is clear, and (L3) holds because D is infinite.

Distinct t give distinct lines. Suppose t + D = t' + D with t ≠ t'. Then d + (t - t') ∈ D for every d ∈ D, so t - t' has more than one representation as a difference. That contradicts Lemma 1.

(L1) Let a ≠ b. A line t + D contains both a and b iff a - t, b - t ∈ D. Their difference is b - a, which equals d - d' for a unique pair (d, d'). So b - t = d and a - t = d', which forces t = a - d'. This t works, so the line exists and is unique.

(L2) Take two lines t + D and t' + D with t ≠ t'. A common point p satisfies p - t, p - t' ∈ D, and (p - t') - (p - t) = t - t'. Write t - t' uniquely as d - d'. Then p - t' = d, so p is unique, and p = t' + d does lie on both lines. ∎

## 3. The hyperfield

Let G = ⟨θ⟩ be infinite cyclic, with θ^n identified with the point n. Put H = G ∪ {0}, with 0 absorbing for multiplication. Write L(a,b) for the line through distinct a, b ∈ G. Define addition by:
- 0⊞a = a⊞0 = {a};
- a⊞a = {0, a} for a ∈ G;
- a⊞b = L(a,b) \ {a,b} for distinct a, b ∈ G.

So -a = a.

**Lemma 3.** H is a hyperfield.

*Proof.* We check the axioms in turn.

1. **Commutativity** is clear.

2. **Nonempty sums.** a⊞b is nonempty because lines are infinite (L3).

3. **Neutral element and negatives.** 0 is neutral. For a, b ∈ G we have 0 ∈ a⊞b iff a = b, because a⊞b ⊆ G when a ≠ b. So negatives are unique, and -a = a.

4. **Reversibility.** Since -b = b, we must show: c ∈ a⊞b ⇒ a ∈ c⊞b.
   - If a = 0, then c = b, and 0 ∈ b⊞b.
   - If b = 0, then c = a, and a ∈ a⊞0.
   - If c = 0, then a = b, and a ∈ 0⊞a.
   - If a, b, c ∈ G and a = b, then c = a, and a ∈ a⊞a.
   - If a, b, c ∈ G and a ≠ b, then c ∈ L(a,b) with c ≠ a, b. So L(c,b) = L(a,b), and a lies on this line with a ≠ c, b. Hence a ∈ c⊞b.

   With commutativity this gives: the relation Z3(a,b,c) :⇔ c ∈ a⊞b is invariant under all permutations of a, b, c. For a, b, c ∈ G, Z3(a,b,c) holds iff either a = b = c, or a, b, c are distinct and collinear.

5. **Distributivity.** Multiplication by θ^k is a translation, and translations map lines to lines (L4), so g·L(a,b) = L(ga,gb). Hence g(a⊞b) = ga⊞gb for g ∈ G. For w = 0, both sides equal {0}, since a⊞b ≠ ∅.

6. **Associativity.** We use the four-point criterion.

   *Reduction.* Since -1 = 1 and reversibility holds, e ∈ t⊞c ⇔ t ∈ e⊞c. Therefore
   - e ∈ (a⊞b)⊞c ⇔ R(a,b|c,e), where R(a,b|c,e) means (a⊞b)∩(c⊞e) ≠ ∅;
   - e ∈ a⊞(b⊞c) = (b⊞c)⊞a ⇔ R(b,c|a,e).

   So it suffices to show that R(a,b|c,e) depends only on the multiset {a,b,c,e}, and not on how it is split into two pairs.

   *If the multiset contains 0.* Suppose the pairing puts 0 with u, and the other pair is v, w. Then 0⊞u = {u}, so R ⇔ u ∈ v⊞w ⇔ Z3(u,v,w). Here {u,v,w} is the multiset with one 0 removed, so the result is independent of the pairing.

   *If a, b, c, e ∈ G.* There are five cases.
   - {a,a,a,a}: every pairing gives {0,a}∩{0,a}, which is nonempty, so all pairings are true.
   - {a,a,a,b} with b ≠ a: every pairing is {aa|ab}, giving {0,a}∩(L(a,b)\{a,b}) = ∅. So all pairings are false.
   - {a,a,b,b}: the pairing {aa|bb} gives a set containing 0. The pairing {ab|ab} gives a⊞b ≠ ∅. So all pairings are true.
   - {a,a,b,c} with a, b, c distinct:
     - The pairing {aa|bc} holds iff a ∈ L(b,c).
     - The pairing {ab|ac} is (L(a,b)\{a,b})∩(L(a,c)\{a,c}). If a, b, c are collinear, this is the line minus three points, which is nonempty. Otherwise two distinct lines meet only at a, which is excluded, so it is empty.
     - Both pairings therefore hold iff a, b, c are collinear.
   - a, b, c, e distinct:
     - If all four are collinear on a line L, every pairing gives L \ {a,b,c,e} ≠ ∅, so all are true.
     - Otherwise L(a,b) ≠ L(c,e). By (L2) they meet in a single point p, and R(a,b|c,e) ⇔ p ∉ {a,b,c,e}. Now p = a ⇔ a, c, e are collinear. Likewise p = b ⇔ b, c, e collinear; p = c ⇔ a, b, c collinear; p = e ⇔ a, b, e collinear.
     - So in this case R holds iff no three of the four points are collinear, which is symmetric in a, b, c, e.

   In all cases R depends only on the multiset, so ⊞ is associative. ∎

## 4. The counterexample

Take x = θ, y = θ³, z = 1. Then x³ = θ³, y³ = θ⁹, z³ = 1, and -xyz = xyz = θ⁴.

**Hypothesis.** 0 ∈ (x⊞y)⊞1 ⇔ 1 ∈ θ⊞θ³ ⇔ the points 0, 1, 3 are distinct and collinear. This holds because they all lie in D.

**Target.** The target sum is the six-term sum θ³⊞θ⁹⊞1⊞θ⁴⊞θ⁴⊞θ⁴. First, θ⁴⊞θ⁴⊞θ⁴ = {0,θ⁴}⊞θ⁴ = {θ⁴}∪{0,θ⁴} = {0,θ⁴}. Put A = θ³⊞θ⁹⊞1. Then the target sum is A⊞{0,θ⁴} = A ∪ (A⊞θ⁴). So 0 lies in it iff one of the following holds:

- **(i) 0 ∈ A.** This holds iff 1 ∈ θ³⊞θ⁹, i.e. iff the points 0, 3, 9 are collinear.
  - The line through 0 and 9: we have 9 = 29 - 20, so this line is -20 + D, and it contains 0, 4, 9.
  - 3 lies on -20 + D iff 23 ∈ D, which is false (end of §1).
  - So (i) fails.
- **(ii) θ⁴ ∈ A.** This holds iff (θ³⊞θ⁹)∩(1⊞θ⁴) ≠ ∅, by the reduction in §3, step 6.
  - Here 1⊞θ⁴ = (-20+D) \ {0,4} and θ³⊞θ⁹ = L(3,9) \ {3,9}.
  - These two lines are distinct, because 3 ∉ -20 + D. They share the point 9, so by (L2) they meet only at 9.
  - But 9 ∉ θ³⊞θ⁹. So the intersection is empty and (ii) fails.

Hence 0 ∉ x³⊞y³⊞z³⊞(-xyz)⊞(-xyz)⊞(-xyz), although 0 ∈ x⊞y⊞z. The answer to the question is **NO**.

In the normalized form (N): with x = θ, y = θ³ we have 1 ∈ x⊞y. But 1 ∉ T = x³⊞y³⊞xy⊞xy⊞xy, because 1 ∈ T ⇔ 0 ∈ T⊞1, which is exactly the set just shown not to contain 0.

## 5. Remarks (consistency checks; not needed for the proof)

- **The configuration.** Write 1, x³, y³, xy for the points 0, 3, 9, 4. Exactly one triple among them is collinear, namely {1, y³, xy}. For a hyperfield of this type, that is precisely the failure condition.
- **Consistency with (A3).** By (A3), quotient hyperfields satisfy the claim. So this H is not a quotient of a field, and correspondingly the plane is not Desarguesian.
- **Consistency with (C1).** Finite cyclic planes with lines of at least 4 points have |G| ≥ 13. This fits the search result (C1), which found no counterexample with |G| ≤ 9.
- **Consistency with B-3(i).** H also violates the core claim (C): 1 ∉ x³⊞y³⊞xy.
- **Literature.** Infinite cyclic projective planes are due to M. Hall Jr., "Cyclic projective planes" (Duke Math. J., 1947). The link between such planes and hyperfields with a⊞a = {0,a} is due to Connes–Consani. Both are cited from memory only. Every fact used here is proved above.
- **Open questions.** None for the posed question. The free-hyperfield construction suggested in the query was not needed and was not carried out.

=== END OF ANSWER round4_q6 ===
