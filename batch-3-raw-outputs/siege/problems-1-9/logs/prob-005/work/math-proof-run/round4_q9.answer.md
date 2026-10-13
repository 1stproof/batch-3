# round4_q9 answer: class C (-1 != 1, a⊞-a = H for a != 0)

## Summary of what is proved here

The class C sub-case is NOT easier than the general problem. Every hyperfield K has an "up-closure" K^↑ in class C: same multiplicative group, and a⊞'b = (a⊞b) ∪ {a,b} for b ≠ -a, a⊞'-a = H. From this:

**Theorem E (proved).** The following are equivalent:
1. (N) holds in every hyperfield of class C.
2. (W) For every hyperfield K and all x, y in K^× with 1 ∈ x⊞y, some NONEMPTY sub-multiset of M := {x^3, y^3, xy, xy, xy, -1} has 0 in its K-sum.

Moreover:
- A class-C counterexample exists iff some hyperfield K (necessarily with -1 ≠ 1) has x, y with 1 ∈ x⊞y such that no nonempty sub-multiset of M is a zero-sum in K. Such a K is itself a counterexample to the original problem, and K^↑ is then a class-C counterexample.
- (N) for K implies (N) for K^↑.

(W) is implied by the original claim, and in a generic field no proper sub-multiset of M is a zero-sum. So settling class C either way is essentially as hard as the whole problem:
- A proof for class C proves (W) for all hyperfields.
- A counterexample in class C is the same thing as a "strong" counterexample anywhere.

This also answers hint 3 (enlarging a⊞-a): see Section 5.

I could not decide (W) (see Section 7).

---

## 1. Zero-sum families (proved)

**Notation.**
- Let H = G ∪ {0} be a hyperfield. For a finite multiset X over G, Σ(X) denotes the iterated hypersum. It is well defined by associativity and commutativity, and Σ(∅) = {0}.
- Z_H = {X : 0 ∈ Σ(X)} is the zero-sum family.
- Summands equal to 0 are simply dropped. "A ⊔ {t}" with t = 0 means A.

**Lemma 1.1 (properties of Z_H).** For every hyperfield H:
- (a) ∅ ∈ Z, and {g} ∉ Z for g ∈ G. Also {a,b} ∈ Z iff b = -a.
- (b) gX ∈ Z ⇔ X ∈ Z for g ∈ G.
- (c) For multisets A, B: A ⊔ B ∈ Z ⇔ there is t ∈ H with A ⊔ {t} ∈ Z and B ⊔ {-t} ∈ Z.
- (d) Σ(X) = {c ∈ H : X ⊔ {-c} ∈ Z}.

*Proof.*
- (a) and (b) follow from neutrality of 0, uniqueness of negatives, and distributivity.
- (d) Σ(X ⊔ {-c}) = ∪_{u ∈ Σ(X)} u ⊞ (-c), and 0 ∈ u ⊞ (-c) iff u = c.
- (c) Write Σ(A ⊔ B) = Σ(A) ⊞ Σ(B), a union over a ∈ Σ(A), b ∈ Σ(B) of a ⊞ b.
  - If 0 ∈ a ⊞ b, then b = -a. Put t = -a. Then 0 ∈ a ⊞ t ⊆ Σ(A ⊔ {t}), and 0 ∈ b ⊞ a ⊆ Σ(B ⊔ {-t}).
  - Conversely, 0 ∈ Σ(A) ⊞ t forces -t ∈ Σ(A), and 0 ∈ Σ(B) ⊞ (-t) forces t ∈ Σ(B). Hence 0 ∈ (-t) ⊞ t ⊆ Σ(A ⊔ B).
  - The case t = 0 is included. ∎

**Lemma 1.2 (converse).** Let G be an abelian group with an element -1 satisfying (-1)^2 = 1, and let H = G ∪ {0}. Let Z be a family of finite multisets over G satisfying (a), (b), (c) and
- (e) for all a, b ∈ G there is c ∈ H with {a, b, -c} ∈ Z.

Define:
- Σ(X) := {c : X ⊔ {-c} ∈ Z};
- a ⊞ b := Σ({a,b}) for a, b ∈ G;
- a ⊞ 0 = 0 ⊞ a = {a}.

Then H is a hyperfield, its iterated sums are Σ, and its zero-sum family is Z.

*Proof.*
1. **Single summands.** Σ({a}) = {a} for a ∈ G: c = 0 would need {a} ∈ Z, and for c ≠ 0, {a, -c} ∈ Z iff c = a.
2. **Recursion.** For nonempty X and w ∈ G:
   - c ∈ Σ(X ⊔ {w}) ⇔ X ⊔ {w, -c} ∈ Z.
   - By (c) applied to the split X | {w, -c}, this holds iff there is t with X ⊔ {t} ∈ Z and {w, -c, -t} ∈ Z.
   - Put u = -t. For u ≠ 0 the conditions read u ∈ Σ(X) and c ∈ Σ{u, w} = u ⊞ w. For u = 0 they read 0 ∈ Σ(X) and {w, -c} ∈ Z, i.e. c = w ∈ 0 ⊞ w.
   - So Σ(X ⊔ {w}) = ∪_{u ∈ Σ(X)} u ⊞ w.
3. **Associativity and commutativity.** By induction, every left-bracketed sum ((a_1 ⊞ a_2) ⊞ …) ⊞ a_n equals Σ{a_1, …, a_n}, which is symmetric in its arguments. Hence (a ⊞ b) ⊞ c = Σ{a,b,c} = (b ⊞ c) ⊞ a = a ⊞ (b ⊞ c). Instances involving 0 are trivial.
4. **Remaining axioms.**
   - Nonempty sums: by (e).
   - Unique negatives: 0 ∈ a ⊞ b iff {a,b} ∈ Z iff b = -a, by (a).
   - Reversibility: c ∈ a ⊞ b ⇔ {a, b, -c} ∈ Z ⇔ {-a, -b, c} ∈ Z (by (b) with g = -1) ⇔ a ∈ c ⊞ (-b). The cases with a zero are immediate.
   - Distributivity: by (b).
5. **Zero-sum family.** 0 ∈ Σ(X) ⇔ X ∈ Z. ∎

So hyperfields on G ∪ {0} are the same thing as families Z satisfying (a), (b), (c), (e).

## 2. Class C = up-closed zero-sum families (proved)

**Lemma 2.1.** H is in class C (a ⊞ -a = H for all a ≠ 0) iff Z_H is up-closed on nonempty multisets: X ∈ Z, X nonempty, X ⊆ X' ⇒ X' ∈ Z.

*Proof.*
- (⇐) {a, -a} ∈ Z, so {a, -a, -c} ∈ Z for every c, i.e. c ∈ a ⊞ -a.
- (⇒) It suffices to show X ⊔ {w} ∈ Z.
  - Pick x ∈ X. Since 0 ∈ Σ(X) and {x} ∉ Z, the rest X∖x is nonempty, and -x ∈ Σ(X∖x).
  - Then Σ(X ⊔ {w}) ⊇ (-x ⊞ x) ⊞ w = H ⊞ w.
  - H ⊞ w = H: given h, pick h' ∈ h ⊞ (-w). By reversibility h ∈ h' ⊞ w.
  - So 0 ∈ Σ(X ⊔ {w}). ∎

**Consequences in class C.**
- 0 ∈ Σ(X) ⇔ Σ(X) = H.
- Σ is monotone: Σ(X) ⊆ Σ(X ⊔ {w}).
- a, b ∈ a ⊞ b for all a, b.

## 3. The up-closure K^↑ (proved)

Let K = G ∪ {0} be any hyperfield. Define

Z^↑ := {∅} ∪ {X : X ⊇ Y for some nonempty Y ∈ Z_K}.

**Theorem 3.1.** Z^↑ satisfies (a), (b), (c), (e). Hence (Lemma 1.2) it defines a hyperfield K^↑ on the same set with the same multiplication. K^↑ lies in class C. Its sums are:
- Σ^↑(X) = H if some nonempty sub-multiset of X lies in Z_K;
- otherwise Σ^↑(X) = ∪_{∅ ≠ Y ⊆ X} Σ_K(Y).

In particular:
- a ⊞' b = (a ⊞ b) ∪ {a, b} for b ≠ -a;
- a ⊞' -a = H.

Also K^↑ = K iff K is in class C.

*Proof.*
- **(a)** The nonempty sub-multisets of {g} are only {g} ∉ Z_K. Those of {a, b} are {a}, {b}, {a, b}, so {a, b} ∈ Z^↑ iff {a, b} ∈ Z_K iff b = -a.
- **(b)** Clear.
- **(e)** {a, b, -a} ⊇ {a, -a} ∈ Z_K.
- **(c) ⇐.** Suppose A ⊔ {t} ∈ Z^↑ and B ⊔ {-t} ∈ Z^↑.
  - If t = 0: then A, B ∈ Z^↑, and A ⊔ B contains A, or equals B when A = ∅. Either way A ⊔ B ∈ Z^↑.
  - If t ≠ 0: choose nonempty Y_1 ⊆ A ⊔ {t} and Y_2 ⊆ B ⊔ {-t} in Z_K.
    - If Y_1 does not use the added copy of t, then Y_1 ⊆ A ⊆ A ⊔ B. The same holds for Y_2.
    - Otherwise Y_1 = Y_1' ⊔ {t} and Y_2 = Y_2' ⊔ {-t} with Y_1' ⊆ A and Y_2' ⊆ B. By (c) for Z_K, Y_1' ⊔ Y_2' ∈ Z_K. It is nonempty, since Y_1' = ∅ would give {t} ∈ Z_K. So A ⊔ B ∈ Z^↑.
- **(c) ⇒.** If A or B is empty, take t = 0. Otherwise let Y ⊆ A ⊔ B be nonempty in Z_K, and write Y = Y_A ⊔ Y_B.
  - If both parts are nonempty, (c) for K gives t with Y_A ⊔ {t} ∈ Z_K and Y_B ⊔ {-t} ∈ Z_K. These are nonempty sub-multisets of A ⊔ {t} and B ⊔ {-t}. If t = 0, use Y_A ⊆ A and Y_B ⊆ B themselves.
  - If Y_B = ∅, then Y ⊆ A. Take t = b ∈ B: A ⊔ {b} ⊇ Y, and B ⊔ {-b} ⊇ {b, -b} ∈ Z_K.
  - The case Y_A = ∅ is symmetric.
- **Class C.** Z^↑ is up-closed by definition, so Lemma 2.1 applies.
- **Formula for Σ^↑.** Σ^↑(X) = {c : X ⊔ {-c} ⊇ some nonempty Y ∈ Z_K}. The witness Y either avoids -c (then Y ⊆ X and everything is in Σ^↑) or equals Y' ⊔ {-c} with c ∈ Σ_K(Y'), where Y' ≠ ∅ because {-c} ∉ Z_K.
- **K^↑ = K iff K in class C.** By Lemma 2.1, Z_K is up-closed iff K is in class C. ∎

**Examples.**
- The up-closure of the phase hyperfield S^1 ∪ {0} is the hyperfield whose sums are: H if 0 ∈ conv(X), and the closed arc hull of X otherwise. I checked that it satisfies (N), by positivity.
- The up-closure of any field or quotient F/U satisfies (N), by Corollary 4.2 below.

## 4. The equivalence (proved)

**Lemma 4.1.** Let x, y ∈ G. Then:
- 1 ∈ x ⊞' y iff 1 ∈ x ⊞ y, or 1 ∈ {x, y}, or y = -x.
- In K^↑: 1 ∈ T' := x^3 ⊞' y^3 ⊞' xy ⊞' xy ⊞' xy iff M = {x^3, y^3, xy, xy, xy, -1} ∈ Z^↑, iff some nonempty sub-multiset of M is a zero-sum in K.

*Proof.* The first statement is Theorem 3.1. For the second, use Lemma 1.1(d) and the definition of Z^↑. ∎

**Corollary 4.2.** If K satisfies (N), so does K^↑.

*Proof.* Suppose 1 ∈ x ⊞' y.
- If 1 ∈ x ⊞ y, then M ∈ Z_K by (N) for K, so M ∈ Z^↑.
- If x = 1, then {x^3, -1} = {1, -1} ⊆ M. The case y = 1 is the same.
- If y = -x, then {x^3, y^3} is an opposite pair in M. ∎

**Theorem E.** (N) holds in all hyperfields of class C ⇔ (W) holds in all hyperfields.

*Proof.*
- (⇐) Let H be in class C with 1 ∈ x ⊞ y. By (W) some nonempty Y ⊆ M is in Z_H. By up-closure (Lemma 2.1), M ∈ Z_H, i.e. 1 ∈ T.
- (⇒) Let K be any hyperfield with 1 ∈ x ⊞ y. Then 1 ∈ x ⊞' y in K^↑, which is in class C. So 1 ∈ T' in K^↑, which by Lemma 4.1 is exactly (W) for K and x, y. ∎

**Corollary 4.3 (shape of a class-C counterexample).** A class-C counterexample exists iff there is a hyperfield K and x, y with 1 ∈ x ⊞ y such that no nonempty sub-multiset of M is a zero-sum in K. Call this a **strong counterexample**. In particular K needs all of the following:
- -1 ≠ 1 (else {xy, xy} ∈ Z);
- 0 ∉ 1 ⊞ 1 ⊞ 1 (else {xy, xy, xy} ∈ Z);
- x^3 ≠ 1, y^3 ≠ 1, x^3 ≠ -y^3, xy ≠ 1, y ≠ -x^2, x ≠ -y^2 (the 2-element sub-multisets);
- 1 ∉ Σ_K(Y') for every nonempty Y' ⊆ {x^3, y^3, xy, xy, xy};
- 0 ∉ Σ_K(Y') for every such Y'.

A strong counterexample K is in particular a counterexample to the original problem, and so is K^↑.

This explains the coincidence list of B-7 and why the generic case is the whole difficulty: the class-C condition only collapses relations that already contain a zero sub-sum.

## 5. Hint 3: enlarging a⊞-a to all of H (proved)

**Proposition 5.1.** Let K be a hyperfield. Define the naive enlargement: a ⊞~ b = a ⊞ b for b ≠ -a, and a ⊞~ -a = H for a ≠ 0. Then:

the naive enlargement is a hyperfield ⇔ a ∈ a ⊞ b for all a, b ∈ G with b ≠ -a.

In that case it equals K^↑.

*Proof.*
- (⇒) A hyperfield with a ⊞ -a = H is in class C, and there a ∈ a ⊞ b (end of Section 2).
- (⇐) The condition gives (a ⊞ b) ∪ {a, b} = a ⊞ b for b ≠ -a, so the binary sums of the naive enlargement coincide with those of K^↑ (Theorem 3.1). A hyperaddition is determined by its binary sums, so the naive enlargement is K^↑, which is a hyperfield. ∎

**Example.** For a field K, 1 ∉ 1 + b = {1 + b} when b ∉ {0, -1}. So the naive enlargement is not associative, which matches the direct computation: (a ⊞ -a) ⊞ c = H but a ⊞ (-a ⊞ c) = {c}.

**Can enlargement destroy (N)?** The correct enlargement K^↑ never destroys (N) (Corollary 4.2). It can only create (N) where K fails it non-strongly. Conversely K^↑ fails (N) exactly when K is a strong counterexample.

## 6. Further observations

### 6.1 Half-space description of a subclass (proved)

Let 𝓗 be a family of subsets h ⊆ G ("halves") with these properties:
- h ⊔ (-h) = G;
- 𝓗 is closed under translation by G;
- (H0) any a, b with b ≠ -a lie in a common half;
- (S) if the finite sets A, B have A ∪ B in no half, then cl(A) ∩ -cl(B) ≠ ∅, where cl(A) is the intersection of all halves containing A, and cl(A) = G if there is none.

Then Z = {X : supp X lies in no half} satisfies (a), (b), (c), (e). So it gives a class-C hyperfield with:
- Σ(X) = cl(X) if X lies in a half;
- Σ(X) = H otherwise.

*Proof.*
- (c ⇐) If A ∪ B lies in a half h, then A ⊆ h forces t ∉ h, and B ⊆ h forces -t ∉ h. This is impossible because h ⊔ (-h) = G.
- (c ⇒) This is exactly (S) together with the opposite-pair trick: if A ∈ Z, take t = b ∈ B.
- (a) follows from (H0) and h ∩ (-h) = ∅.

In this language, (N) fails iff some half contains {x^3, y^3, xy, -1} while no half contains {x, y, -1}.

**Remarks on examples (proofs only sketched).**
- If every half is a homomorphic sign map σ: G → {±1} with σ(-1) = -1, then (N) holds. Suppose 1 ∉ cl{x^3, y^3, xy}, so some half has σ(x) = σ(y) = σ(xy) = + and σ(1) = -. Then since σ(x) = σ(y) = +, also σ(1) = + (because 1 ∈ cl{x, y}), a contradiction.
- I also looked at halves given by open semicircles of a cyclic order on which an abelian G acts. For an orbit of a single circle homeomorphism (G = {±1} × Z) I found only rotation-type or "μ_{2q}-phase ⋊ ordered group" structures, and these satisfy (N). I did not prove this classification in general.

### 6.2 Why (W) is not easier

In a field with x + y = 1 and x, y generic, the only zero-sum sub-multiset of M is M itself. The linear-derivation obstructions of B-1, B-5 and B-6 apply to proper sub-multisets as well: they are statements about derivations of short relations from the triangles {mx, my, -m}, and the term counts only get worse for fewer terms. I checked this only informally.

## 7. Status

**Proved.**
- Lemmas 1.1 and 1.2 (zero-sum calculus).
- Lemma 2.1 (class C = up-closed zero-sum families).
- Theorem 3.1 (the up-closure K^↑ is a class-C hyperfield).
- Theorem E and Corollaries 4.2 and 4.3 (class C ⇔ (W); shape of a counterexample).
- Proposition 5.1 (exactly when naive enlargement works).
- The half-space construction of 6.1.

**Not proved / open.**
- (W) itself. Equivalently: does a strong counterexample exist? Equivalently: does (N) hold throughout class C?
- Neither (a) nor (b) of the task is achieved. What is established is that (a) is equivalent to finding a strong counterexample in an arbitrary hyperfield, and (b) is equivalent to proving the weak form (W) for all hyperfields.
- Any proof for class C must therefore work for arbitrary hyperfields, up to the weakening "some sub-multiset of M is a zero-sum". So the class-C restriction gives no essential leverage.

**Open questions, named explicitly.**
- (Q1) Is there a hyperfield K and x, y with 1 ∈ x ⊞ y such that no nonempty sub-multiset of {x^3, y^3, xy, xy, xy, -1} is a zero-sum?
- (Q2) Does every counterexample to (N) (if one exists) yield a strong one, so that (N) for class C would be equivalent to (N) in general?

=== END OF ANSWER round4_q9 ===
