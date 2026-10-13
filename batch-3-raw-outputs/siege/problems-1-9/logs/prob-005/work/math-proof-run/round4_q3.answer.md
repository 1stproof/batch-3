# round4_q3 — answer

**Verdict: PARTIAL.** I did not settle (N). Below are the precise results I proved, the
reductions I obtained, and the dead ends I ran into (with the reasons). Everything labelled
"proved" was checked step by step from the hyperfield axioms. Nothing is cited from the
literature.

The derivation of (N) from the problem in the task file is correct; I re-checked it.

Notation: ε := −1 ∈ G. A finite multiset M over G is *null* if 0 ∈ ⊞M. "Fusion" means the
composition rule (B-1 §1): if A + t and B + εt are null, then A + B is null. This includes
t = 0, i.e. a union of null multisets is null.

---------------------------------------------------------------------------------------------

## Lemma 0 (proved): hyperfields from null-set families

Let G be an abelian group and ε ∈ G with ε² = 1. Let N be a family of finite multisets over G
with these properties:
(N1) N is G-invariant and contains every pair {a, εa};
(N2) no 1-element multiset lies in N, and the only 2-element multisets in N are pairs;
(N3) fusion: if A + t ∈ N and B + εt ∈ N with t ∈ G ∪ {0}, then A + B ∈ N (t = 0 means A ∈ N and B ∈ N);
(N4) splitting: if A + B ∈ N with A, B nonempty, there is t ∈ G ∪ {0} with A + t ∈ N and B + εt ∈ N;
(N5) for all a, b ∈ G there is c ∈ G ∪ {0} with {a, b, εc} ∈ N.

Define H = G ∪ {0} and c ∈ a⊞b :⇔ {a, b, εc} ∈ N, dropping zeros, with 0⊞a = {a}. Then H is
a hyperfield with −a = εa, and 0 ∈ ⊞M ⇔ M ∈ N for every finite multiset M over G.

Proof. Put S(M) := {c ∈ H : M + εc ∈ N}, dropping zeros. Then S({m}) = {m} by (N2), and
S({a,b}) = a⊞b.

Key claim: for nonempty M and a ∈ G, we have S(M + a) = ⋃_{s∈S(M)} s⊞a. That is,
M + a + εc ∈ N ⇔ ∃ s: M + εs ∈ N and {s, a, εc} ∈ N.
- (⇐) is fusion along εs/s.
- (⇒) splits M + a + εc as M | {a, εc} by (N4) and puts s := εt.

By induction, every left-nested sum of the elements of M equals S(M). S(M) is symmetric in M,
so ⊞ is associative. The remaining axioms:
- 0 ∈ a⊞b ⇔ b = εa, by (N2);
- sums are nonempty, by (N5);
- reversibility: c ∈ a⊞b ⇔ {a, b, εc} ∈ N ⇔ ε{a, b, εc} = {c, εb, εa} ∈ N ⇔ a ∈ c⊞εb;
- distributivity is G-invariance. ∎

---------------------------------------------------------------------------------------------

## Result 1 (proved): (N) holds when −1 = 1 and g² = 1 for all g ∈ G

Let 1 ∈ x⊞y with x, y ≠ 0. Put D := (1⊞1)\{0} and Q := 1⊞1⊞1. Since x³ = x and y³ = y,
T = x⊞y⊞xyQ.
- If 1 ∈ 1⊞1, then 0 ∈ Q, so T ⊇ x⊞y ∋ 1.
- If x = y, apply Proposition 1 of B-2.
- Otherwise, proceed as follows.
 1. Multiplying 0 ∈ 1⊞x⊞y by xy gives 0 ∈ xy⊞y⊞x (use x² = y² = 1).
 2. Fuse this with 0 ∈ 1⊞x⊞y along y = −y. This gives 0 ∈ (x⊞x)⊞(1⊞xy), so there is
    t ∈ (x⊞x) ∩ (1⊞xy). Here t ≠ 0, because xy ≠ 1. So t = xd with d ∈ D, and multiplying
    by x gives d ∈ x⊞y.
 3. Fuse 0 ∈ 1⊞x⊞y with 0 ∈ d⊞x⊞y along y. This gives some t' ∈ (x⊞x) ∩ (1⊞d). Here
    t' ≠ 0, because d ≠ 1 (as 1 ∉ 1⊞1). So t' = xd' with d' ∈ D.
 4. Q ⊇ 1⊞d ∋ xd', hence xyQ ∋ x²y·d' = yd', and T ⊇ x⊞y⊞yd'.
 5. d' ∈ 1⊞1 gives 1 ∈ 1⊞d', so y ∈ y⊞yd'. Hence T ⊇ x⊞y ∋ 1. ∎

Remark. This class contains no quotient hyperfield with 1 ∉ 1⊞1: in characteristic 2,
U ⊇ F^{×2} forces a² + b² = (a+b)² ∈ U. So the result is genuinely beyond (A3).

In the same class the "Frobenius" cycle identity 0 ∈ 1⊞x⊞y ⇒ 0 ∈ 1⊞x²⊞y² FAILS. Example:
G = V_4 = {1, a, b, c}, 1⊞1 = H\{1}, 1⊞g = G for g ≠ 1. This is a hyperfield; I checked the
4-point condition of (A5c) for every quadruple type. Take x = a, y = b: then 0 ∈ 1⊞a⊞b, but
0 ∉ 1⊞1⊞1. So identities whose field proof needs a cycle can genuinely fail in hyperfields.
The slack term 3xy in (N) is what saves Result 1.

---------------------------------------------------------------------------------------------

## Result 2 (proved): the "union-closure" family H_Δ

Let Δ be a G-invariant set of 3-element multisets ("triangles"). Let N' be the set of finite
multisets that contain, as a sub-multiset, a pair {a, εa} or a member of Δ. Assume:

(★) whenever T1, T2 ∈ Δ, t ∈ T1 and εt ∈ T2, the 4-multiset (T1 − t) + (T2 − εt) lies in N'.

Then N' satisfies (N1)–(N5), so H_Δ is a hyperfield (Lemma 0) with 0 ∈ ⊞M ⇔ M ∈ N'.
- Fusion: pass to minimal witnesses (pairs or Δ-triangles) inside A + t and B + εt. The only
  non-trivial case is two Δ-triangles, which is exactly (★).
- Splitting is automatic. A minimal witness has at most 3 elements. Either it lies on one
  side, or one side of it is a single element w, and then t = εw works.
- (N5) holds because {a, b, εa} contains a pair.

Corollary 2.1. A counterexample of this type is: Δ ∋ τ = {x, y, ε}, satisfying (★), such that
M := {x³, y³, xy, xy, xy, ε} contains no pair and no member of Δ. Note that ε ≠ 1 is needed,
since otherwise {xy, xy} is a pair.

Remark 2.2. If Δ is the triangle set of a hyperfield K with the property "every null 4-set
obtained by gluing two triangles contains a null sub-multiset of size ≤ 3", then (★) holds.
By induction over fusion trees, every K-null set then contains a K-null sub-multiset of size
≤ 3. So H_Δ satisfies (N) whenever K does. In particular:
- union-closures of phase, sign, tropical-type and other "convex" structures satisfy (N);
- so does any positive-dependence structure coming from commuting linear operators. Here the
  field identity, applied to commuting matrices with positive coefficients λ_i, gives a
  positive dependence for the target.

## Result 3 (proved): a single G-orbit Δ = G·τ never gives a counterexample

Use the symmetric form τ = {a, b, c}, M = {a³, b³, c³, m, m, m}, m = εabc. Gluing τ at u
with a translate placing v (≠ u) at εu gives, up to translation,
Y_{uv} = {v², vw, εuw, εu²}.

Assume M ∉ N', i.e. no x_i³ = εx_j³ and no x_i² = x_jx_k (otherwise M contains a pair).
- A pair in Y_{uv} then forces u² = v².
- A translate of τ inside Y_{uv} is impossible. I checked all 4 sub-triples and 6 bijections;
  each case forces an excluded relation.

Hence (★) forces a² = b² = c², and then {a³, b³, c³} = a²τ ⊆ M. ∎

## Result 4 (proved; a dead end): no H_Δ counterexample on Z_12 with τ = {0,1,5}

In additive exponents with ε = 6, M = {0, 3, 3, 0, 0, 0}. It has no pair, and its only
sub-triples are the shapes {s,s,s}, {s,s,s+3}, {s,s,s+9}. In Z_3 × Z_4 coordinates M lies in
one Z_3-coset, while τ = {(0,0),(1,1),(2,1)} is transversal.

Every single-coset triple contains a pair or is one of the forbidden shapes. So Δ consists of
transversal triangles and "2+1" triangles (d, π): a pair in coset A at positions z+π and a
single point at (A+d, z).

The forced contradiction:
- (D1) Gluing two (d, ·) triangles at their single points gives a 4-set inside one coset. It
  must contain a pair, so F_d := {π : (d,π) ∈ Δ} is an intersecting family.
- The six τ–τ gluings force (C1) (1,01) or (2,00) or (2,33), and (C2) (2,01) or (1,00) or
  (1,33).
- Gluing τ at its single point with (1,00) forces F_2 to meet both {01,11} and {22,23}. That
  violates (D1), so (1,00) ∉ Δ.
- (1,33) forces (2,00). The automorphism (i,x) ↦ (−i,x) fixes τ, ε and M, so the same
  argument gives (2,00) ∉ Δ, (2,33) ∉ Δ and (1,33) ∉ Δ.
- Hence (1,01) and (2,01) both lie in Δ.
- Gluing τ at (1,1) with (1,01) at its single point gives {(0,0),(0,0),(0,3),(2,1)}. Its
  only candidate triangles are (2,23) and (2,33). Either one contradicts (D1), since 01 ∈ F_2.
  ∎

## Result 5 (proved): a⊞(−a) = H for all a ≠ 0 ⇔ the null family is upward closed

(⇒) Let X = B + s be null, so −s ∈ ⊞B. Then
⊞(A + X) ⊇ ⊞A ⊞ (−s) ⊞ s = ⊞A ⊞ H = H ∋ 0.
(⇐) If the null family is upward closed, {a, −a, c} is null for every c, so a⊞(−a) = H.

So B-7's open "generic case" is exactly (N) for upward-closed hyperfields. The H_Δ of
Result 2 are exactly the upward-closed hyperfields whose minimal null sets all have size ≤ 3.

## Result 6 (proved): the free hyperfield F of (C4) exists and is a genuine hyperfield

Construction:
- Start from G_0 = ⟨ε⟩ × Z² (generators x, y) and the basic set {x, y, ε}.
- Repeatedly close under G-translates, pairs and fusion (including unions).
- For every unsatisfied splitting requirement (X, A|B) with |A|, |B| ≥ 2, adjoin a fresh free
  generator s together with A + s and B + εs. Requirements with a 1-element part are
  automatically satisfied, via t = εa.
- For every unsatisfied (N5) requirement (a, b), adjoin a fresh c together with {a, b, εc}.
- Process all requirements fairly and take the union.

The limit satisfies (N1), (N3), (N4) and (N5). For (N2): every basic set has ≥ 3 elements. The
family N_K = {multisets of size ≥ 3} ∪ {pairs} is G-invariant and fusion-closed (I checked the
small cases), and it contains all pairs and all basic sets, so N_F ⊆ N_K. Hence N_F has no
singletons and no non-pair 2-sets. By Lemma 0, F is a hyperfield with 1 ∈ x⊞y.

So **F is a counterexample to (N) iff M ∉ N_F.** This settles the coordinator's open point in
(C4) that the limit is a hyperfield.

Two caveats.
1. F is not universal. A fresh witness s cannot always be mapped into a given hyperfield H,
   because in H the only witness may be 0 (e.g. in a field). So "M ∈ N_F" would NOT by itself
   prove (N).
2. F is not conservative over G_0. I analysed derivations layer by layer (s-degree). Even
   though negative layers cannot occur, top-layer components produce new relations among old
   elements by "consistent substitution": if A_0 ⊔ B_0 and Z = {z_j} are null, then for every
   J ⊆ Z the multiset ⊎_{j∈J} εz_jA_0 ⊎ ⊎_{j∉J} z_jB_0 is null. This is valid in every
   hyperfield. So deciding M ∈ N_F is as hard as the original question, and I could not
   decide it.

## Result 7 (proved): a "Helly" reformulation

Put A := x²⊞y, B := y²⊞x, C := 1⊞(−xy).
1. If some s lies in A ∩ B ∩ C, then (N) holds:
   T ⊇ x(x²⊞y) ⊞ y(y²⊞x) ⊞ xy ⊇ s(x⊞y) ⊞ xy ⊇ s⊞xy ∋ 1.
2. All pairwise intersections A ∩ B, B ∩ C, C ∩ A are nonempty, by tree derivations. For
   example, A ∩ B comes from fusing x(x⊞y⊞ε) with −y(x⊞y⊞ε) along xy.
3. In characteristic 2 the natural witnesses are b ∈ C ∩ A and b' ∈ C ∩ B. Gluing {1,xy,b}
   with {1,xy,b'} gives b = b' or d ∈ b⊞b' for some d ∈ D.
4. If b = b', (N) follows. Otherwise one obtains 0 ∈ (target summands) ⊞ yd, a single
   leftover term "y·(1⊞1)". This is exactly the cycle obstruction of B-1, B-5 and B-6.

## Result 8 (proved): the exponent-3, characteristic-2 class (A4)

With w = xy and S := 1⊞w:
- the target is equivalent to 0 ∈ S⊞S⊞S;
- S ∩ x⁻¹S, S ∩ y⁻¹S and x⁻¹S ∩ y⁻¹S are all nonempty, from the 4-sets obtained by gluing
  R_1, R_{x²} and R_{y²} pairwise at 1;
- (N) follows if S ∩ x⁻¹S ∩ y⁻¹S ≠ ∅, since then 0 ∈ f(1⊞x⊞y) ⊆ S⊞S⊞S.

So in this class too, everything comes down to a three-fold Helly property.

---------------------------------------------------------------------------------------------

## What remains open

1. (N) itself, i.e. the problem: neither a proof nor a counterexample.
2. Whether M ∈ N_F for the free hyperfield F (Result 6). This is equivalent to "F is a
   counterexample".
3. Whether every H_Δ (upward-closed, minimal null sets of size ≤ 3) satisfies (N). Results 3
   and 4 suggest a strong local obstruction, but no general proof is known.
4. The triple intersections in Results 7 and 8. In particular (N) for the exponent-3,
   characteristic-2 class is still open.

=== END OF ANSWER round4_q3 ===
