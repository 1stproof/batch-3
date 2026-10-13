# Answer to round1_q2 (partial)

## Proved: (L1) infinitesimal maps out of a valuative monoid

**Lemma 1.** Let M be valuative, N any (sharp) monoid, f : M -> N a homomorphism. Then f is infinitesimal iff f^{-1}(0) ∩ M = {0}. (Since M^gp = M ∪ (-M), this is the same as f^gp being injective.) In particular, a homomorphism of valuative monoids V -> W is infinitesimal iff it is injective.

*Proof.* (⇐) Suppose f(x) ∈ N with x ∈ M^gp, and suppose x ∉ M. Since M is totally ordered, -x ∈ M and -x ≠ 0. Then f(x) and f(-x) = -f(x) both lie in N. Because N is sharp, f(x) = 0, so f(-x) = 0 with -x a nonzero element of M. This contradicts the hypothesis. So x ∈ M. (The ≺ hypotheses are not even needed.)

(⇒) Let 0 ≠ h ∈ M with f(h) = 0. Put y = h and x = -h. Then (-1)y ≤ x ≤ 0·y, so x ≺ y. Also f(x) = 0 ∈ N, and f(y) = 0 ≺ 0 = f(x). The infinitesimal condition would then force -h ∈ M, which contradicts sharpness of M. ∎

**Example.** Take Z^2 with the lexicographic order, mapping to Z by the first coordinate, i.e. the quotient by the convex subgroup 0×Z. This map is **not** infinitesimal: use x = (0,-1), y = (0,1). Quotients by nonzero convex subgroups are never infinitesimal. Injective maps, for example Z -> Z^2 lex with n -> (0,n) or n -> (n,0), are infinitesimal. So, among valuative monoids, "infinitesimal" means "injective". It does not mean "quotient by a convex subgroup".

**Consequence for birhizomic maps (partial L2).** Suppose N = V is valuative and M is valuative. Then factorizations P -> M -> V with p injective are exactly the embeddings of valuation monoids into V. So, at least against valuative test objects, "birhizomic at g" is a unique-lifting property along *injective* maps into V. This looks like a valuative-criterion (properness/separatedness) condition rather than an étale one. This motivates the director's guess that covers are log modifications plus localizations at elements with g = 0. **I have not proved this.**

## Not settled
- (L2): the exact criterion for being birhizomic, when M is not valuative (Lemma 1 does not cover a non-valuative source).
- (L3): quasi-compactness and refinement by subdivisions.
- (L4): points of the topos and stalks of π^{-1}F.
- (L5): the degree-0 comparison.

The director's heuristics (a)–(c) are still unverified. Heuristic (b) is consistent with Lemma 1: a valuation v with v^{-1}(0) = 0 exists because the order on the torsion-free group P^gp extends to a total order. I recall this ordering-extension fact from memory and did not prove it here. Given that valuation, a family P -> P[-x_i]^sharp with all x_i ≠ 0 cannot factor v, so it is not a cover.

## Implication for the headline question
Still open. The single statement that would settle it is the following. For every P, the birhizomic cohomology of the terminal object with coefficients π^{-1}F equals the colimit, over subdivisions Σ of the dual cone, of R lim over Σ^op of the functor c ↦ F(r(c)). This should be paired with the contractibility of open stars, which would give F(P) in degree 0 and zero in higher degrees. If both hold, the answer is YES, at least for finitely generated P.

=== END OF ANSWER round1_q2 ===
