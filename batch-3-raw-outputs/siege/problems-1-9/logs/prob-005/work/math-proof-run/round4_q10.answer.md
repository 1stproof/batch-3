# round4_q10 — answer

Class studied: hyperfields with -1 = 1 and g^3 = 1 for all g ∈ G. Neither (a) nor (b) is settled in
full. What is established is summarised in §6 at the end. In brief: the subclass |1⊞1| = 2 is
completely analysed. Its only member is a new order-4 hyperfield W, modulo one cited classification;
unconditionally in several sub-cases. So the claim holds there, and any counterexample in the class
needs |D| ≥ 2.

Notation: multiplicative, A := 1⊞w, Q := 1⊞1⊞1, D := (1⊞1)\{0}. "Relation" {a1,...,an} means 0 ∈ a1⊞...⊞an.
Since -1 = 1: 0 ∈ X⊞Y iff X ∩ Y ≠ ∅ (X, Y hypersums).

## 1. Basic lemmas (proved)

Throughout: -1 = 1, g^3 = 1 for all g ∈ G, x ∈ G, w ∈ x⊞x^2, w ≠ 0, y := x^2 w (so y ∈ 1⊞x, i.e. 0 ∈ 1⊞x⊞y), and the
triangles {g, gx, gx^2w} (g ∈ G) are relations.

**Lemma 1.1.** 1⊞1⊞1⊞w⊞w⊞w = A⊞A⊞A, and the claim (1 ∈ T) holds iff 0 ∈ A⊞A⊞A iff (A⊞A) ∩ A ≠ ∅.
Moreover A⊞A = {0} ∪ D ∪ wD ∪ (D⊞wD), so the claim holds iff A∩D ≠ ∅ or A∩wD ≠ ∅ or A∩(D⊞wD) ≠ ∅.
*Proof.* Regroup the six summands as (1⊞w)⊞(1⊞w)⊞(1⊞w) (associativity/commutativity); by (A4) the claim is
0 ∈ 1⊞1⊞1⊞w⊞w⊞w. 0 ∈ A⊞(A⊞A) iff A ∩ (A⊞A) ≠ ∅ (since -1 = 1). Finally A⊞A = (1⊞1)⊞(w⊞w) with
1⊞1 = {0}∪D, w⊞w = {0}∪wD. ∎

**Lemma 1.2 (sufficient criterion).** If A ∩ dA ≠ ∅ for some d ∈ D, the claim holds.
*Proof.* Take a, da ∈ A. Since d ∈ 1⊞1, da ∈ a⊞a, so 0 ∈ a⊞a⊞da ⊆ A⊞A⊞A. ∎

**Lemma 1.3.** Let K := {c ∈ G : A ∩ cA ≠ ∅} = A·A^{-1}. Then K ⊇ {x^i w^j : i ∈ {1,2}, j ∈ {0,1,2}}.
*Proof.* The triangles {1, x, x^2w} and {x, x^2, w} share x, so x ∈ (1⊞x^2w) ∩ (x^2⊞w), i.e.
0 ∈ 1⊞x^2w⊞x^2⊞w. Re-pairing (four-point form of associativity, A5(c)): (1⊞w) ∩ (x^2⊞x^2w) ≠ ∅, i.e.
A ∩ x^2A ≠ ∅; so x^2 ∈ K, and K = K^{-1} gives x ∈ K. The triangles {1,x,x^2w} and
x^2w·{1,x,x^2w} = {x^2w, w, xw^2} share x^2w; so 0 ∈ 1⊞x⊞w⊞xw^2, and re-pairing (1,w)|(x,xw^2) gives
A ∩ x(1⊞w^2) ≠ ∅; as 1⊞w^2 = w^2(w⊞1) = w^2A, xw^2 ∈ K. The triangles {1,x,x^2w} and xw·{1,x,x^2w} =
{xw, x^2w, w^2} share x^2w; so 0 ∈ 1⊞x⊞xw⊞w^2, and re-pairing (1,w^2)|(x,xw) gives w^2A ∩ xA ≠ ∅, so
x w^{-2} = xw ∈ K. Inverses give x^2, x^2w^2, x^2w. ∎

**Corollary 1.4.** If D contains some x^i w^j with i ≠ 0, the claim holds for (x, w). In a counterexample
D ∩ K = ∅; in particular D ∩ ⟨x,w⟩ ⊆ {w, w^2}.

**Lemma 1.5.** For distinct a, a' ∈ A: (a⊞a') ∩ D ≠ ∅ and (a⊞a') ∩ wD ≠ ∅. (And |A| ≥ 2 by 1.3.)
*Proof.* w ∈ (1⊞a) ∩ (1⊞a'), so by re-pairing (1⊞1) ∩ (a⊞a') ≠ ∅; the common element is not 0 since
a ≠ a' (0 ∈ a⊞a' iff a = a'), so it lies in D. Likewise 1 ∈ (w⊞a)∩(w⊞a') gives (w⊞w)∩(a⊞a') ≠ ∅. ∎

**Lemma 1.6.** If {p,q,r} is a relation (0 ∈ p⊞q⊞r) and d ∈ D, then (pd⊞q) ∩ (p⊞r) ≠ ∅.
*Proof.* p ∈ (p⊞pd) ∩ (q⊞r) (as 0 ∈ p⊞p⊞pd); re-pair. ∎

**Lemma 1.7 (two elements of one sum).** If s ≠ s' both lie in a⊞b (a, b ∈ G), then ad ∈ s⊞s' and
bd' ∈ s⊞s' for some d, d' ∈ D. (Proof as 1.5: b ∈ (a⊞s)∩(a⊞s') gives (a⊞a)∩(s⊞s') ≠ ∅, and the common
element is not 0.) If D = {d} this reads: ad, bd ∈ s⊞s'.

## 2. A new small example: the hyperfield W of order 4 (proved)

G = {1, d, d^2} (cyclic of order 3), H = G ∪ {0}, -1 = 1, and
 1⊞1 = {0, d}, 1⊞d = {1, d^2}, 1⊞d^2 = {d, d^2}, extended by a⊞b = a(1⊞b/a), 0 neutral.
Additively (G = Z3, d ↔ 1) the triangle system is {g, g, g+1} (g ∈ Z3) together with {0,1,2}; so
0⊞0 = {∞,1}, 0⊞1 = {0,2}, 0⊞2 = {1,2}, and translates.
*Verification.* Commutativity, reversibility (triangles are unordered), unique negatives (∞ ∈ a⊞b iff
a = b) and distributivity (translation invariance) are built in. Associativity, up to translation and
commutativity, needs (a⊞b)⊞c = (a⊞c)⊞b for the multisets {0,0,0}, {0,0,1}, {0,0,2}, {0,1,2}:
 (0⊞0)⊞1 = {1}∪(1⊞1) = {∞,1,2} = {0,2}⊞0 = (0⊞1)⊞0;
 (0⊞0)⊞2 = {2}∪(1⊞2) = {0,1,2} = {1,2}⊞0 = (0⊞2)⊞0;
 (0⊞1)⊞2 = {1,2}∪{∞,0} = H = (1⊞2)⊞0 = {∞,1}∪{0,2} = (0⊞2)⊞1 = {∞,2}∪{0,1}. ∎
Here 1 ∉ 1⊞1, D = {d}, and Q = 1⊞1⊞1 = {1, d^2} ≠ G. So, contrary to what all the coordinator's
enumerations (C2) showed, Q ⊇ G fails in this non-field. (W satisfies the claim: |G| = 3 < 2|Q|.)
W is not a quotient of a finite field: for F_q/U, D is stable under the Frobenius a ↦ a^2, which acts
on G = Z3 as inversion, whereas D = {d} is not. (I believe — from memory, not checked — that a
finite-index subgroup U of an infinite field always has solutions of u1+u2 = u3, which would force
1 ∈ 1⊞1; then W is a non-quotient hyperfield.)

## 3. The subclass |D| = 1 (proved structure; partial resolution)

Assume (besides -1 = 1, exponent 3) that 1⊞1 = {0, d}. Put X := 1⊞d (= Q, since Q = 1⊞(1⊞1) =
(1⊞0) ∪ (1⊞d) and 1 ∈ 1⊞d), Y := 1⊞d^2.

**Proposition 3.1.** X = {1} ∪ E ∪ M, where E ⊆ {d^2}, M is a union of cosets of ⟨d⟩ disjoint from
⟨d⟩, M = M^{-1}, and E ∪ M ≠ ∅.
*Proof.* (0) 1 ∈ X (d ∈ 1⊞1 ⇒ 1 ∈ d⊞1); d ∉ X (d ∈ 1⊞d ⇒ 1 ∈ d⊞d = {0,d^2}, false); 1 ∉ Y
(else d^2 ∈ 1⊞1); d^2 ∈ Y (⇔ 1 ∈ d^2⊞d^2 = {0, d^3} = {0,1}).
(1) For q ≠ q' in X, Lemma 1.7 (a = 1, b = d) gives d ∈ q⊞q' and d^2 ∈ q⊞q'. With q = 1: every
q' ∈ X\{1} satisfies d^2 ∈ 1⊞q', i.e. q' ∈ Y.
(2) For y ≠ y' in Y, Lemma 1.7 (a = 1, b = d^2) gives d ∈ y⊞y'. With y' = d^2: every y ∈ Y\{d^2}
satisfies y ∈ d⊞d^2 = dX, i.e. y/d ∈ X.
(3) Let q ∈ X \ ⟨d⟩. By (1) q ∈ Y, and q ≠ d^2, so q/d ∈ X by (2); q/d ∉ ⟨d⟩, so repeating,
q/d^2 ∈ X. Hence q⟨d⟩ ⊆ X. Also X ∩ ⟨d⟩ ⊆ {1, d^2} by (0). This gives the form of X.
(4) M = M^{-1}: for q ∈ M, q ≠ qd both lie in X, so by (1) d ∈ q⊞qd = qX, i.e. d/q ∈ X \ ⟨d⟩ ⊆ M,
so q^{-1} ∈ M.
(5) E ∪ M ≠ ∅: d ∈ (1⊞1) ∩ (d⊞d^2) (since d⊞d^2 = d(1⊞d) ∋ d), so by re-pairing (1⊞d)∩(1⊞d^2) ≠ ∅;
a common element p is ≠ 1 (1 ∉ Y), so p ∈ X\{1}. ∎

**Corollary 3.2.** With |D| = 1, the claim holds for (x, w) whenever w ∈ ⟨d⟩, or w ∈ M, or
M ∩ wM ≠ ∅. Conversely, for w ∉ ⟨d⟩ it fails iff w ∉ M and M ∩ wM = ∅ (i.e., in G/⟨d⟩,
w̄ ∉ M̄ and M̄ ∩ w̄M̄ = ∅).
*Proof.* Claim ⇔ Q ∩ wQ ≠ ∅ ⇔ X ∩ wX ≠ ∅ (A4). If w = d^2 and E ≠ ∅: w ∈ X ∩ wX. If w = d and
E ≠ ∅: 1 = d·d^2 ∈ X ∩ wX. If w ∈ ⟨d⟩ and E = ∅ then M ≠ ∅ and M = wM ⊆ X ∩ wX. If w ∉ ⟨d⟩:
each of 1 ∈ wX, w ∈ X, d^2 ∈ wX, wd^2 ∈ X is equivalent (M being ⟨d⟩-stable and symmetric) to
w ∈ M; the remaining possible common elements lie in M ∩ wM. ∎

So a counterexample with |D| = 1 needs w ∉ ⟨d⟩, and in the quotient Ḡ = G/⟨d⟩ the symmetric
set M̄ must avoid w̄ and its translate w̄M̄. If M = ∅ (then X = Q = {1, d^2}, as in W) the
claim fails as soon as some w ∈ x⊞x^2 lies outside ⟨d⟩. In that case the quotient H/⟨d⟩ has
1̄⊞1̄ = {0, 1̄} (the images of 1⊞1, 1⊞d, 1⊞d^2 are {0,1̄} ∪ M̄), so H/⟨d⟩ is a Krasner-type
hyperfield (a⊞a = {0,a}), i.e. (C3) a projective geometry on Ḡ with Ḡ acting regularly, and H
is a "W-bundle" over it. Theorem 3.4 below shows that M = ∅ always holds. §4 shows that
W-bundles do not exist: unconditionally over line-type quotients and over geometries with a
line of ≥ R(4,4,4) points, and in general modulo a cited classification.

**Theorem 3.4.** If |D| = 1 then M = ∅. Hence X = Q = {1, d^2}, and ⟨d⟩ ∪ {0} is a sub-hyperfield
isomorphic to W. (Indeed 1⊞1 = {0,d}, 1⊞d = {1,d^2}, 1⊞d^2 = Y = {d^2, d}.)
*Proof.* We use (F2): for c ≠ e in G, (1⊞c)∩(1⊞e) ≠ ∅ iff d ∈ c⊞e. This is re-pairing of
(1⊞1)∩(c⊞e) ≠ ∅, where the common element cannot be 0 since c ≠ e. Suppose n ∈ M.
Case E ≠ ∅. Then d^2 ∈ X = 1⊞d. Also d^2 ∈ 1⊞n, because n ∈ X\{1} ⊆ Y (step (1) of 3.1) gives
d^2 ∈ 1⊞n. So (1⊞d)∩(1⊞n) ≠ ∅, and by (F2) d ∈ d⊞n. Then n ∈ d⊞d = {0,d^2}, contradicting
n ∉ ⟨d⟩.
Case E = ∅, so X = {1} ∪ M. Let m ∈ M and q := d/m ∈ M (M = M^{-1} and M is ⟨d⟩-stable). For
q' ∈ X\{q}, step (1) of 3.1 gives d ∈ q⊞q'. Hence q' ∈ d⊞q, i.e. q'/q = q'm/d ∈ m⊞1. Reversibility
turns q'm/d ∈ 1⊞m into 1 ∈ m(q'/d ⊞ 1), i.e. m^{-1} ∈ 1⊞(q'/d). Writing k := q'/d, this holds for
every k ∈ M with k ≠ m^{-1}. Fix k ∈ M and let m run over M\{k^{-1}}: then 1⊞k ⊇ M\{k}. Since
|M| ≥ 3, (1⊞d) ∩ (1⊞k) ⊇ M\{k} ≠ ∅. By (F2), d ∈ d⊞k, so k ∈ d⊞d = {0,d^2}, a contradiction.
So M = ∅. Then E ≠ ∅ by 3.1(5), and Y = {d^2} ∪ dE = {d^2, d}. ∎

**Corollary 3.5.** If |D| = 1, the claim fails for (x,w) iff w ∉ ⟨d⟩ (by 3.2 with M = ∅). So H with
|D| = 1 is a counterexample iff some x⊞x^2 is not contained in ⟨d⟩. Every such H is "W or a
W-bundle": ⟨d⟩∪{0} ≅ W, and H/⟨d⟩ satisfies ā⊞ā = {0,ā} (see §4).

**Observation 3.3.** Thus any hyperfield H in the class with |D| = 1, G ≠ ⟨d⟩ and some x with
x⊞x^2 ⊄ ⟨d⟩ would be a counterexample to the problem (Corollary 3.2); by (C1) it would have
|G| ≥ 27. The coordinator's F_3^3 searches imposed symmetries (v ↦ −v; an order-13 multiplier
group) that such an H cannot have: inversion maps D = {d} to {d^2}, and an order-13 group cannot fix
⟨d⟩. So those searches did not cover this case. §4 closes it by proof instead.

## 4. W-bundles do not exist

Set-up. G = ⟨d⟩ × Ḡ (Ḡ ≅ F_3^m written additively; G splits since it is an F_3-vector space);
an element is (i, p) = d^i·p, i ∈ Z3 the "level", p ∈ Ḡ. Assume M = ∅. Then (proved above):
⟨d⟩∪{0} is a sub-hyperfield ≅ W. For c ∉ ⟨d⟩, the sum 1⊞c avoids ⟨d⟩ ∪ c⟨d⟩. (Indeed 1 ∈ 1⊞c iff
c ∈ 1⊞1; d ∈ 1⊞c iff c ∈ X; d^2 ∈ 1⊞c iff c ∈ Y = {d,d^2}; c ∈ 1⊞c iff 1 ∈ c⊞c = {0,cd};
cd ∈ 1⊞c iff c^{-1} ∈ X; cd^2 ∈ 1⊞c iff c^{-1} ∈ Y.) Hence H̄ := H/⟨d⟩ has ā⊞ā = {0,ā}
and ā⊞b̄ ⊆ Ḡ\{ā,b̄} for ā ≠ b̄, and no triangle of H has exactly two vertices in one fibre.
(A triangle {(i,p),(j,p),(k,q)} with q ≠ p would give the H̄-relation 0 ∈ p̄⊞p̄⊞q̄, i.e.
q̄ ∈ {0, p̄}.) Triangles inside one fibre are exactly the translates of W-triangles, because the
sums 1⊞1, 1⊞d, 1⊞d^2 lie inside ⟨d⟩ ∪ {0}.

**Step 4.1 (one orbit per triangle).** Take p ≠ q in Ḡ. For a, b in fibre p and c, e in fibre q,
the sets a⊞b and c⊞e lie in (fibre p) ∪ {0} and (fibre q) ∪ {0} respectively, so they meet only
if a = b and c = e. By re-pairing, (a⊞c) ∩ (b⊞e) = ∅ unless (a,c) = (b,e). Hence the nine sets
(i,p)⊞(j,q) are pairwise disjoint. Multiplication by d maps triangles to triangles. So, for distinct
p, q, r, the set R(p,q,r) of level triples (i,j,k) with {(i,p),(j,q),(k,r)} ∈ Δ is empty or a single
orbit {(θp+κ, θq+κ, θr+κ) : κ ∈ Z3}. Here θ = θ_{pqr} is a "potential" on the triangle, defined up to an
additive constant. By translation invariance, θ_{T+g}(X+g) = θ_T(X).
Write f(c,e) := θ_{0ce}(c) − θ_{0ce}(0) (the level jump from 0 to c in the triangle {0,c,e}). Then
(0,0)⊞(j,c) is nonempty iff j = f(c,s) for some s; so each f(c,·) must be onto Z3.

**Step 4.2 (the configuration {p,p,q,r}).** Take a = (0,0), b = (ρ,0), c = (u,c̄), e = (z,ē) with
0, c̄, ē distinct. Let L(0,ρ) := {k : {0,ρ,k} is a W-triangle}, so L(0,0) = {1}, L(0,1) = {0,2},
L(0,2) = {1,2}.
 R4(a,b,c,e) holds iff {0,c̄,ē} carries a triangle and u = A+ℓ, z = B+ℓ for some ℓ ∈ L(0,ρ), where
 A = f(c̄,ē), B = f(ē,c̄).
 R4(a,c,b,e) holds iff there is s̄ ∉ {0,c̄,ē} such that {0,c̄,s̄} and {0,ē,s̄} carry triangles and
 u = f(c̄,s̄), ρ = f(s̄,c̄) − f(s̄,ē), z − ρ = f(ē,s̄).
The four-point axiom requires these to coincide for all (ρ,u,z).

**Proposition 4.3 (no W-bundle over a line-type quotient).** No hyperfield H in the class has
1⊞1 = {0,d}, 1⊞d = {1,d^2}, G ≠ ⟨d⟩, and H̄ = H/⟨d⟩ "line-type", i.e. every three distinct points
of Ḡ carry a triangle of H̄.
*Proof.* Under line-type every triple carries exactly one orbit, and in 4.2 every s̄ ∉ {0,c̄,ē}
contributes a triple (ρ,u,z) of R4(a,c,b,e). That triple must lie in the set for R4(a,b,c,e), whose
members all satisfy u − A = z − B. Writing this out for all distinct nonzero c, s, e gives
 (★) f(c,s) + f(s,e) + f(e,c) = f(c,e) + f(e,s) + f(s,c).
Also the pair (ρ, ℓ) := (f(s,c) − f(s,e), f(c,s) − f(c,e)) must satisfy ℓ ∈ L(0,ρ). Equivalently,
{0, ρ, ℓ} is a W-triangle. The W-triangles are exactly the multisets in Z3 with sum 1, together
with {0,1,2}.
(i) Form of f. (★) says that A(c,s) := f(c,s) − f(s,c) has zero sum around every triangle of the
complete graph on Ḡ\{0}. Hence A(c,s) = π(s) − π(c) for some π: Ḡ\{0} → Z3. In the triangle
{0,c,s} this reads θ(c) − θ(s) = π(s) − π(c). Translating, in any triangle {X,Y,Z} we get
θ(X) − θ(Y) = π(Y−Z) − π(X−Z). Hence f(c,e) = θ(c) − θ(0) = π(−e) − π(c−e). The potentials must close
up around each triangle {0,c,e}. This gives ϱ(c) + ϱ(e−c) = ϱ(e) for ϱ(v) := π(v) − π(−v), so ϱ is
additive, hence F_3-linear. Changing the complement of ⟨d⟩ in G by a homomorphism λ: Ḡ → Z3
relabels levels (i,p) ↦ (i − λ(p), p). This changes f(c,e) to f(c,e) − λ(c) and π to π + λ, and
ϱ to ϱ + 2λ. Taking λ = ϱ makes π even: π(v) = π(−v). So π is a function on the set of
directions (1-dimensional subspaces) of Ḡ.
(ii) Contradiction. Take a 2-dimensional subspace V ≤ Ḡ, a direction [v] in V, and c ∈ V \ ⟨v⟩.
Put s = c+v, e = c+2v. These three points lie on an affine line missing 0, and their directions
are the three directions of V other than [v]. Since c−s, c−e, s−e ∈ {±v} and π is even,
 α := f(c,s) − f(c,e) = π(s) − π(e), β := f(s,e) − f(s,c) = π(e) − π(c), γ := f(e,c) − f(e,s) = π(c) − π(s).
Apply the W-triangle condition to the three ordered choices (c,e;s), (e,c;s) [i.e. {0,α,−β}],
{0,β,−γ}, {0,γ,−α}. Check the 3^3 cases with α+β+γ = 0: the admissible (α,β,γ) are
(0,2,1), (2,1,0), (1,0,2), (1,1,1), (2,2,2). So the values of π on the three directions are either
pairwise distinct, or of the form {λ, λ, λ+1} (the value occurring once is λ+1); they are never
all equal. Now the 4 directions of V carry 4 values in Z3, so some value repeats. If a value
occurs 3 times, those three are all equal: excluded. Pattern {λ,λ,μ,μ}: the triple {λ,λ,μ} forces
μ = λ+1, and {μ,μ,λ} forces λ = μ+1, a contradiction. Pattern {λ,λ,μ,ν} with μ ≠ ν: the triples
{λ,λ,μ} and {λ,λ,ν} force μ = ν = λ+1, a contradiction. Since G ≠ ⟨d⟩ we have dim Ḡ ≥ 1. If
dim Ḡ = 1, then H̄ has |Ḡ| = 3 with ā⊞ā = {0,ā}, and associativity fails: (1⊞1)⊞ω = {ω,ω^2} but
1⊞(1⊞ω) = 1⊞ω^2 = {ω}. So dim Ḡ ≥ 2 and V exists. ∎

**Corollary 4.4 (finite case; uses a cited classification).** There is no finite W-bundle, i.e. no finite
H in the class with 1⊞1 = {0,d}, 1⊞d = {1,d^2}, G ≠ ⟨d⟩.
*Argument.* H̄ satisfies -1 = 1 and ā⊞ā = {0,ā}, i.e. it is a hyperfield extension of the Krasner
hyperfield. By the Connes–Consani theorem (cited from memory: such extensions with |H̄| > 4
correspond to projective geometries in which every line has ≥ 4 points, with lines
{a,b} ∪ (a⊞b), the group acting regularly), Ḡ (|Ḡ| = 3^m, m ≥ 2) is the point set of a projective
geometry. A plane of order q has q^2+q+1 points, and if 3 divides this then q ≡ 1 (mod 3) and
q^2+q+1 ≡ 3 (mod 9), so it is never 3^m with m ≥ 2. Spaces of dimension ≥ 3 are PG(n,q) (Veblen–Young),
with (q^{n+1}−1)/(q−1) = 3^m. If q ≡ 1 (mod 3), lifting the exponent gives
v_3 = v_3(n+1) < n+1 ≤ the sum, which is impossible. If q ≡ 2 (mod 3), then n+1 must be even and
v_3 = v_3(q+1) + v_3((n+1)/2), so 3^m ≤ (q+1)(n+1)/2 < q^n for n ≥ 3. If 3 | q the sum is ≡ 1 (mod 3).
So the geometry is a single line, i.e. H̄ is line-type, and Proposition 4.3 applies.

**Corollary 4.5.** Every finite hyperfield in the class with |1⊞1| = 2 is isomorphic to W (G = ⟨d⟩).
In particular the claim holds for all finite hyperfields in the class with |D| = 1. (Proof:
Theorem 3.4 gives M = ∅, and Corollary 4.4 gives G = ⟨d⟩. This relies on the Connes–Consani
classification, cited from memory. Without it, the statement holds whenever H/⟨d⟩ is line-type.)

Remark. In the proof of 4.3, the W-triangle conditions on (α,β,γ) for one triple are satisfiable on
their own. The contradiction comes from the four directions of a plane. For non-line-type H̄, (★)
is only available for collinear points. This is handled next.

**Lines of H̄.** In H̄ (ā⊞ā = {0,ā}), put L(a,b) := {a,b} ∪ (a⊞b) for a ≠ b. If s ≠ e both lie in
a⊞b, then b ∈ (a⊞s)∩(a⊞e), so (a⊞a)∩(s⊞e) ≠ ∅, so a ∈ s⊞e and s ∈ a⊞e. From this one gets the
usual fact (also part of the Connes–Consani theorem, cited from memory) that the L(a,b) form a
linear space: any two points lie on exactly one line, and three distinct points form an
H̄-triangle iff they are collinear. Below I use this only in the form: for collinear distinct
p, c, e, the points s with {p,c,s} and {p,e,s} both H̄-triangles are exactly the points of the line
other than p, c, e.

**Proposition 4.6 (Ramsey bound on lines).** Suppose |D| = 1 and G ≠ ⟨d⟩ (a W-bundle). Then every
line of H̄ has fewer than R(4,4,4) points, where R(4,4,4) is the 3-colour Ramsey number for K4. In
particular H̄ has no infinite line.
*Proof.* Fix a line Λ of H̄. Each 3-subset T ⊆ Λ carries exactly one orbit (4.1), with potential
θ_T. For p ∈ Λ and distinct c, e ∈ Λ\{p}, put f_p(c,e) := θ_{pce}(c) − θ_{pce}(p). Step 4.2,
translated so that the fibre over p is the base fibre, applies verbatim with f_p in place of f.
Here s ranges over Λ\{p,c,e}. So for all distinct p, c, s, e ∈ Λ:
 (★_p) f_p(c,s)+f_p(s,e)+f_p(e,c) = f_p(c,e)+f_p(e,s)+f_p(s,c),
and the multisets {0, α, −β}, {0, β, −γ}, {0, γ, −α} are W-triangles, where α = f_p(c,s) − f_p(c,e),
β = f_p(s,e) − f_p(s,c), γ = f_p(e,c) − f_p(e,s).
(i) By (★_p), D_p(c,s) := θ_{pcs}(c) − θ_{pcs}(s) has zero cyclic sums on Λ\{p}. So D_p(c,s) =
Φ(p,s) − Φ(p,c) for some Φ(p,·): Λ\{p} → Z3, unique up to an additive constant depending on p.
Reading the triangle {p,c,e} from the base e gives f_p(c,e) = Φ(e,p) − Φ(e,c). The potentials close up
around each triangle {p,x,y}: (Φ(p,y) − Φ(p,x)) + (Φ(x,p) − Φ(x,y)) + (Φ(y,x) − Φ(y,p)) = 0. So
Ψ(x,y) := Φ(x,y) − Φ(y,x) is a cocycle on the complete graph on Λ, hence Ψ(x,y) = h(y) − h(x).
Write Φ = Σ + 2Ψ with Σ(x,y) := 2(Φ(x,y)+Φ(y,x)) symmetric. Then the Ψ-terms cancel in α, β, γ,
and with m1 := Σ(s,p)+Σ(c,e), m2 := Σ(e,p)+Σ(c,s), m3 := Σ(c,p)+Σ(s,e) (the three perfect
matchings of K4 on {p,c,s,e}) one gets
 α = m1 − m2, β = m2 − m3, γ = m3 − m1.
(The per-p constants shift Σ by φ(x)+φ(y), which shifts m1, m2, m3 equally.)
(ii) The W-triangle condition on (α,β,γ) is exactly as in the proof of 4.3: (α,β,γ) must be one of
(0,2,1), (2,1,0), (1,0,2), (1,1,1), (2,2,2). In particular m1 = m2 = m3 is forbidden.
(iii) Colour each edge {x,y} of the complete graph on Λ by Σ(x,y) ∈ Z3. If |Λ| ≥ R(4,4,4), then
by Ramsey's theorem (for infinite Λ, the infinite Ramsey theorem) there is a monochromatic K4
{p,c,s,e}, say of colour λ. Then m1 = m2 = m3 = 2λ, a contradiction. ∎

**Corollary 4.7 (the case |D| = 1, modulo a cited classification).** Every hyperfield in the class
with |1⊞1| = 2 is isomorphic to W. Hence the claim holds whenever |D| = 1.
*Argument.* By 3.4, H is W (if G = ⟨d⟩) or a W-bundle. In the latter case H̄ is a hyperfield
extension of the Krasner hyperfield with |Ḡ| = 3^m ≥ 9 or Ḡ infinite. By Connes–Consani (cited
from memory) its lines make Ḡ a projective geometry on which Ḡ acts regularly by collineations,
and in dimension ≥ 3 (and for Desarguesian planes) H̄ ≅ L/F^* for a field extension L ⊇ F.
- Dimension 1 (line-type): excluded by 4.3.
- Dimension 2: lines are finite by 4.6, so the plane is finite of order q, and |Ḡ| = q^2+q+1 ≠ 3^m.
- Dimension ≥ 3: H̄ ≅ L/F^*. Lines have |F|+1 points, so F is finite by 4.6. Then L^*/F^* of
exponent 3 gives a^{3(|F|−1)} = 1 for all a ∈ L^*, so L is finite, and the count of 4.4 excludes it.
Without the citation, what is proved is: no W-bundle has a line-type quotient (4.3), and no W-bundle
has a quotient geometry containing a line with ≥ R(4,4,4) points (4.6). With Cor. 4.4 this gives
the finite case, which still uses the classification for finite Krasner extensions.

## 5. A twisting construction (proved), and why it does not immediately help

**Proposition 5.1.** Let H be a hyperfield with abelian G. Let χ: G → Z/3 be a homomorphism and
v ∈ ker χ with v^3 = 1. Suppose T: H → H, T(0) = 0, T(a) = a·v^{χ(a)}, is an automorphism of
(H, ⊞): T(a⊞b) = T(a)⊞T(b). Define a∗b := ab·v^{χ(a)χ(b)}. Then H_∗ = (H, ⊞, ∗) is a hyperfield.
If G has exponent 3, so does (G, ∗).
*Proof.* (a∗b)∗c = abc·v^{χ(a)χ(b)+χ(a)χ(c)+χ(b)χ(c)}, using χ(v) = 0. This is symmetric, so ∗ is
associative and commutative. The identity is 1. The inverse of a is a^{-1}v^{χ(a)^2}. Since
T^j(s) = s·v^{jχ(s)}, we have c∗s = c·T^{χ(c)}(s). Hence c∗(a⊞b) = c·T^{χ(c)}(a⊞b) =
c·(T^{χ(c)}a ⊞ T^{χ(c)}b) = c∗a ⊞ c∗b. The additive axioms are unchanged. Also χ(−1) = 0 (as
2χ(−1) = 0), so (−1)∗a = −a. Finally a∗a∗a = a^3·v^{3χ(a)^2} = a^3. ∎

**Corollary 5.2.** Let H be in the class (−1 = 1, exponent 3), with T as in 5.1. Then T(Q) = Q
and w∗Q = w·T^{χ(w)}(Q) = wQ. So H_∗ is a counterexample iff there are x, y with 1 ∈ x⊞y and
Q ∩ (xy·v^{χ(x)χ(y)})Q = ∅. In words: twisting keeps Q and moves the relevant w = xy by v^{±1}.

If H = K/U and T is induced by an automorphism τ of K of order 3 with τ(U) = U, then H_∗ = N/U,
where N is the Dickson near-field with coupling map a ↦ τ^{χ(aU)} (standard construction; cited
from memory). So H_∗ is a "near-field quotient", which need not be a field quotient. Obstacle:
T must act on K^*/U as a ↦ a·v^{χ(a)}. By Hilbert 90 this forces U to contain an index-3 part of the
norm-one group of K/K^τ (modulo cubes), so U is large. In the example K = F_4(t), τ(t) = ωt, the
natural choice of U contains t^3 and t^3+1 (a full τ-orbit of primes), so 1 ∈ 1⊞1 and the claim
holds trivially. Conversely, for U = K^{*3} with K = F_4(t) no such τ exists: τ would have to fix
every place. I also expect Q to be very large in any quotient of an infinite char-2 field by a
subgroup containing the cubes, since Q ⊇ {[u(u+1)] : u ∈ K} by the identity
(u+λ)^3 + u^3 + λ^3 = λu(u+λ). Twisting cannot help when Q·Q^{-1} = G. So 5.1 is recorded as a
tool, not as a source of counterexamples.

## 6. Summary: proved / conditional / open

Proved (unconditionally):
- Reformulations and sufficient criteria (§1): the claim ⇔ 0 ∈ A⊞A⊞A with A = 1⊞w. It holds if
 A ∩ dA ≠ ∅ for some d ∈ D. Always A ∩ x^i w^j A ≠ ∅ for i ≠ 0, so the claim holds whenever D meets
 {x^i w^j : i ≠ 0}. Hence in a counterexample D ∩ ⟨x,w⟩ ⊆ {w, w^2}.
- A new hyperfield W of order 4 in the class (§2), with 1 ∉ 1⊞1 and Q = {1,d^2} ≠ G. It is not a
 quotient of a finite field.
- |D| = 1 structure (§3): if 1⊞1 = {0,d} then 1⊞d = {1,d^2}, ⟨d⟩∪{0} ≅ W, Q = {1,d^2}, and the claim
 fails for (x,w) iff w ∉ ⟨d⟩ (Thm 3.4, Cor 3.5).
- No W-bundle (|D| = 1, G ≠ ⟨d⟩) has a line-type quotient H/⟨d⟩ (Prop 4.3). No W-bundle has a
 quotient geometry with a line of ≥ R(4,4,4) points, in particular with an infinite line
 (Prop 4.6).
- Twisting construction (Prop 5.1): a way to build new hyperfields in the class from an additive
 automorphism a ↦ a v^{χ(a)}. It keeps Q and moves w by v^{±1}.

Conditional on the Connes–Consani classification of hyperfield extensions of the Krasner
hyperfield (cited from memory; see Cor 4.4, 4.7):
- every hyperfield in the class with |1⊞1| = 2 is isomorphic to W (the finite case needs only the
 finite part of the classification). Hence the claim holds for all hyperfields in the class with |D| = 1.
 So a counterexample in this class must have |D| ≥ 2.

Open:
- The class with |D| ≥ 2: neither a counterexample nor a proof. Natural next case: D = {d, d^2},
 or |D| = 2 in general. The method of §§3–4 (Lemma 1.7 + (F2): (1⊞c)∩(1⊞e) ≠ ∅ ⇔ D ∩ (c⊞e) ≠ ∅)
 is the tool to try.
- Whether the twisting of §5 can be applied to some sparse H with Q·Q^{-1} ≠ G.
- A self-contained proof (without the citation) that a W-bundle cannot sit over a projective
 geometry of dimension ≥ 2 with all lines shorter than R(4,4,4).

=== END OF ANSWER round4_q10 ===
