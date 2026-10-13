# round2_q1: partial answer

## Proved: a criterion for birhizomic maps in one case

**Setting.** P is fine. f : P -> Q has f^gp an isomorphism, so Q is a fine saturated monoid with P ⊂ Q ⊂ P^gp. g : Q -> V, V is valuative, and v := g^gp : P^gp -> V^gp. Assume v(x) ≠ 0 for every x ∈ P \ {0}.

**Lemma A (necessary condition).** If f is birhizomic at g, then g(q) > 0 for every q ∈ Q \ {0}.

*Proof.* Let M = {x ∈ P^gp : v(x) > 0} ∪ {0}.
- M is a sharp, integral submonoid of P^gp. It is saturated: V^gp is a totally ordered torsion-free group, so v(nx) > 0 implies v(x) > 0.
- P ⊂ M, by the hypothesis on v.
- Let h : P -> M be the inclusion and p = v|_M : M -> V. Then ph = gf.
- p is infinitesimal. Suppose x ∈ P^gp, y ∈ M, p(x) ∈ V, x ≺ y and p(y) ≺ p(x). If v(x) > 0 then x ∈ M. Otherwise v(x) = 0, so p(y) ≺ 0, so p(y) = 0, so y = 0. Then x ≺ 0 forces x = 0 ∈ M.

So there is a u : Q -> M with uf = h. Because Q^gp = P^gp, u must be the inclusion (u^gp agrees with h^gp, which is the identity). Hence Q ⊂ M, i.e. v > 0 on Q \ {0}. ∎

This generalises R3: there v(e1 − e2) = 0 with e1 − e2 ∈ Q.

**Proposition B (rank one).** Suppose in addition that V is archimedean (rank one). Then f is birhizomic at g if and only if g^{-1}(0) = {0}.

*Proof.*
- (⇒) This is Lemma A.
- (⇐) Q is finitely generated, so Q is the saturation of P + ⟨a_1, …, a_k⟩ with a_i ∈ Q \ {0}, and g(a_i) > 0. Write each a_i = b_i − c_i with b_i, c_i ∈ P. Since V is archimedean and v(a_i) > 0, we have v(b_i + c_i) ≺ v(a_i). R4 then applies; I re-checked its proof and it is correct. Finite presentation holds because P and Q are fine. ∎

In words: for a rank-one valuation that is injective on P, the birhizomic neighbourhoods with f^gp an isomorphism are exactly the charts whose dual cone contains v in its interior. These are open-cone neighbourhoods, not the closed charts of a subdivision.

## Status of the remaining items (not done)

- **Higher rank.** Lemma A holds for every V. Sufficiency at higher rank needs the ≺ condition of R4, and I have not proved that it is necessary. So the R5 claim about the rank-two valuation of N^2 is still unverified. The test monoid M of Lemma A does not settle it.
- **Non-injective f^gp.** I have not classified birhizomic maps f with f^gp not injective (beyond the localizations P -> P[-x]^♯) or with nontrivial ker v on P.
- **Covers, quasi-compactness, the space X_P and stalk formulas.** Open; nothing beyond the background.
- **Headline question.** Undecided. The expected answer is YES, but it is not proved here.

=== END OF ANSWER round2_q1 ===
