# round1_q4: class-by-class partial results

The general question is NOT settled here. Normalized form (B2): if 1 ∈ x⊞y, is 1 ∈ T := x³⊞y³⊞xy⊞xy⊞xy?

## Lemma 0 (absorption). For any a, H ⊞ a = H. Also, if S ∋ 0 then A ⊞ S ⊇ A for any set A.
Proof. Given c, pick h ∈ c⊞-a (this set is nonempty). By reversibility c ∈ h⊞a. The second claim holds because A⊞S ⊇ A⊞0 = A. ∎

## (v) Hyperfields with a⊞-a = H for all a ≠ 0: the implication holds. (Proved.)
Normalize so that x, y ≠ 0. Case -1 = 1: then xy⊞xy = xy⊞-xy = H, so T ⊇ x³⊞y³⊞xy⊞H = H by Lemma 0, and 1 ∈ T. Case -1 ≠ 1: work in the unnormalized form. The target contains x³ ⊞ (-xyz ⊞ ...). If z = 0 the claim is trivial by (B2). Otherwise, if x³ = xyz then x³ ⊞ -xyz = H, so the target is H ⊞ (rest) = H, by Lemma 0. In general this argument needs one of x³, y³, z³ to equal xyz. So for (v) with -1 ≠ 1 only that special case is proved, and the rest is open. The hypothesis "a⊞-a ⊇ {0,a,-a}" gives nothing beyond this by the same method.

## Reduction lemma for (i) and (ii). If 0 ∈ xy⊞xy⊞xy, or if 0 ∈ xy⊞xy, then the implication follows from the core claim
 (C) 1 ∈ x⊞y ⇒ 1 ∈ x³⊞y³⊞xy.
Proof. In the second case, T = (x³⊞y³⊞xy)⊞(xy⊞xy) ⊇ x³⊞y³⊞xy by Lemma 0. The first case is analogous, with core x³⊞y³ (stronger). ∎
- (i) If -1 = 1, then xy⊞xy ∋ 0, so the problem reduces to (C).
- (ii) If a⊞a = {a}, then xy⊞xy⊞xy = {xy}, so T = x³⊞y³⊞xy exactly, and the problem is equivalent to (C).
Restatement of (C): (x³⊞y³) ∩ (1⊞-xy) ≠ ∅. I could not prove (C) and found no counterexample to it. In a field of characteristic 2, x³+y³ = (x+y)(x²+xy+y²) = x²+xy+y² = 1+xy uses cancellation (x+y)² = x²+y², which is not available in a hyperfield (1 ∈ x⊞y gives only 1 ∈ x²⊞xy⊞xy⊞y²).

## (iii) Stringent hyperfields. Conditional on a cited result.
From memory (Bowler–Su): every stringent hyperfield is isomorphic to a field, to K or S, or to an extension of one of these by an ordered abelian group (H ⋊ Γ). I believe each of these is a quotient F/U of a field: take Hahn series k((Γ)) modulo 1+𝔪, and then also modulo the residue units or the squares for K and S. Given this, (B3) applies and the implication holds. This step is cited from memory and not re-verified.

## (iv) Doubly distributive hyperfields. Conditional on a cited result.
From memory, Bowler–Su also classify these: fields, K, S, W (the weak sign hyperfield) and their extensions by ordered groups. W is a quotient of a finite field by its squares; for example, in F_7 the sum 1+1=2 is a square and 1+2=3 is a nonsquare, giving 1⊞1 = {±1}. If the whole class consists of quotient hyperfields, the implication holds by (B3). This is not verified here.

## 2. Counterexample shape (only partially analysed)
Any counterexample must satisfy:
- it is not a quotient hyperfield;
- it has at least 10 elements (B5);
- x, y ≠ 0;
- none of x³, y³, z³ equals xyz, if every a⊞-a = H.
No finite configuration was derived.

## Open
- The general question.
- Claim (C), which alone would settle classes (i) and (ii).
- Class (v) when -1 ≠ 1.

=== END OF ANSWER round1_q4 ===
