# Verification report on the draft proof (answer YES)

**Verdict.** I checked the draft step by step. I found no mathematical error. The main claim is **proved**: for every monoid P and every presheaf F on B_P^op, the morphism F → Rπ_*π^{-1}F is a quasi-isomorphism. This rests on the interpretive conventions listed in §B below, which are the natural readings of the problem. The remaining issues are minor: places where the exposition is terse or a standard step is sketched. They are listed in order of severity in §C.

## A. Step-by-step check

**§1 (foundations).**
- 1.1 (torsion-freeness) is correct.
- 1.2 (filtered colimits): each axiom is indeed witnessed at a finite stage. For saturation, an element x of the colimit group is a difference of elements from some stage, and nx = m holds at a later stage.
- 1.3 (the reflection): correct. M_0 generates G as a group, so T^gp = G/M_1^*, and the saturation argument is valid.
- 1.5: (b) and (c) are correct. (a) is the standard argument; injectivity is only sketched (see C3).
- 1.6: P[−x] is saturated because m(g + nx) = p + (m−1)nx. The universal property and Φ_{b_x} = face(x) are correct, and so is the identification B_P ≃ Pr(P).
- 1.7: correct.
  - Surjectivity is clear.
  - For injectivity, lift x to M_1; then some multiple nx = [a].
  - A bijective monoid homomorphism is an isomorphism, so M = colim T(S,R).
  - Compactness gives the retraction.
- 1.9 (iso / base change / composition): I verified all three. For base change, the pair (hc, p) factors g_i a_i. Uniqueness follows from the pushout property.
- 1.10: correct.

**§2 Theorem B.**
- Step 1 (kernel equality under a retraction under P) is correct.
- Step 2 is correct:
  - The group completion of (P⊕N^k)/R is (P^gp⊕Z^k)/L.
  - x dies iff −x ∈ M_1, iff −nx ∈ M_0 for some n.
  - K = {c ∈ Z^J : Ac ∈ −N^k} is the set of lattice points of the rational cone {Ac ≤ 0}. Gordan's lemma applies even though this cone need not be pointed.
  - ψ is additive, and the converse direction is correct.
  - S = Y ∩ P is a submonoid, so Φ_Q = ∪_{t∈S} face(t).
- Step 3 is correct:
  - F^gp ∩ P = F holds for any face F.
  - Strictness forces the rank of G_i inside the free finite-rank group Y^gp to increase strictly.
  - A maximal face therefore exists, and directedness finishes the argument.

**§3 Theorem D.**
- 3.1: the cone/valuation dictionary is correct. W total gives W ∩ (−W) = lin W, so W/lin W is the positive cone of a total order on U/lin W. Lemma Z (Zorn's lemma plus the lineality computation) and the existence of injective valuations are both correct.
- Lemma 1:
  - The retract reduction is valid because M is a retract of T *under Q*.
  - Maps T → H_{≥0} under Q are exactly solutions y ≥ 0 of (α_j − β_j)·y = c_j.
  - Fourier–Motzkin elimination over a totally ordered Q-vector space works with the c_j as parameters. The system is homogeneous, so the output consists of homogeneous rational forms u_m·c ≥ 0, independent of H.
  - (a) uses V_W = (H_W)_{≥0}, and v_W(x) ≥ 0 ⇔ x ∈ W. (b) uses V ⊂ (V^gp⊗Q)_{≥0}, which holds by torsion-freeness.
- Lemma 2: both inclusions are correct, and so is the version for tuples with repetitions, since maps out of Q_t are tuples of maps.
  - (⊂) uses a total W ⊃ K_σ with lin W = lin K_σ.
  - (⊃) uses an injective valuation of Q_σ (resp. Q_t) and torsion-freeness of V^gp.
- (G0)–(G3): correct for any subset τ ⊃ Φ_Q. In (G2) one uses f(p) ∈ Q_Q ⊂ K, so p ∈ f^{-1}(lin K) ⇔ −f(p) ∈ K.
- Lemma 3:
  - 𝒯 is closed in {0,1}^U, since each condition involves finitely many coordinates.
  - Each E_i is open because X_i is finite.
  - The E_i cover 𝒯 because v_W is a valuation and the family satisfies the factorization hypothesis.
  - Tychonoff's theorem then gives the finite subfamily J_0.
- Theorem T:
  - The coefficient system is well defined, and d² = 0 holds because (G0) makes every composite of coface maps consistent.
  - Cone lemma: I verified the identity dh + hd = id directly, including degree −1, where (hdc)() = c(j*).
  - Base case: every z ∈ X_{j*} lies in K, by the argument through lin W = lin K.
  - Row lemma: the nerve is a single vertex (which is a cone point) or a full edge (by (G2)). This needs K' ∈ 𝒢, and the complex is zero otherwise.
  - Inductive step: rows are exact by the row lemma applied to K' = K + cone X_σ. Columns with q ≥ 0 are exact by induction, because z becomes decided in K_ρ, decided elements stay decided, and the cover hypothesis is inherited by K_ρ ⊃ K.
  - The double-complex argument is sound. In each total degree only finitely many (p,q) with p,q ≥ −1 occur, and the subcomplex q ≥ 0 is closed under both differentials.
- 3.6: all five steps are correct.
  - Finite pieces via Theorem T and Lemma 2; nonemptiness via (G3) and (G1).
  - Universal coefficient surjection for complexes of free abelian groups, with A = H_n.
  - Directed union over finite J' ⊃ J_0.
  - An exact complex of free abelian groups is split exact, because subgroups of free abelian groups are free; hence Hom(−, A) is exact.

**§4 (sheaf theory).**
- 4.1:
  - The Kan-extension formula over ι/Q is correct for presheaves on B_P^op.
  - ι/Q is a nonempty directed preorder, so Lan is exact.
  - For f.p. Q, b(Q) is terminal in ι/Q (Theorem B), so the values and maps of Lan F on f.p. objects are those of F.
  - π_* is restriction to B_P (adjunction plus the sheafification adjunction).
- 4.2: I_{τ,A} is a functor, because the pattern 0 → A never occurs. The formula Hom(F, I_{τ,A}) = Hom(F(b_τ), A) is correct, so I_{τ,A} is injective for injective A. The embedding F ↪ ∏_τ I_{τ,E(F(τ))} is a monomorphism, using the component τ = Φ_b.
- 4.3: correct. Its part (iii) needs the witness subfamily (Lemma 1.10).
- 4.4: all Q_t lie in 𝔅, so G(Q_t) = I_{τ,A}(b(Q_t)) and the transition maps are id or 0. With Φ_t = Φ_{set(t)}, the complex is Hom(C̃(N_τ), A). Theorem D applies, with τ a principal face containing Φ_Q.
- Cor. 4.5: correct, since Lan commutes with products on f.p. objects.
- Lemma 4.6: correct.
  - The sieves generated by members of Cov are cofinal in the directed set J(Q), so G^+(Q) = G(Q).
  - The hypothesis transfers to G^+ because G → G^+ is an isomorphism at Q, Q_i and Q_ij.
  - Then apply the same step again to get G^{++}.
- Cor. 4.7: I checked the diagram chase; it uses Čech exactness of Lan I^0 in degrees −1 and 0, and of Lan I^1 in degree −1. Both the unit isomorphism and the Čech-acyclicity of π^{-1}I^k on Cov follow.
- 4.6 (Fact): correct.
  - K_•(W) splits over ψ into ordered-simplex chain complexes on T_ψ, so K_• resolves Z_R.
  - Sheafification is exact, and Hom_Sh(−, I) is exact for an injective sheaf I.
- Prop. 4.8: correct. (a) is the standard lifting argument via Ȟ^1 = 0 on a Cov-refinement. (b) is the short exact sequence of Čech complexes, valid because all U_t ∈ 𝔅, together with the Fact. (c) is an induction over all sheaves satisfying the hypothesis.
- 4.7: correct.
  - π^{-1}F → π^{-1}I^• is a Γ(U,−)-acyclic resolution for U ∈ 𝔅, and its sections are I^•(b(U)), which is exact in positive degrees.
  - (R^pπ_*G)(b) = H^p(b, G), and every b ∈ B_P lies in 𝔅.

## B. Interpretive conventions (stated in the draft; I find them reasonable)
1. The problem defines a cover only with base P. The draft takes the covering families of an object Q of A_P to be the birhizomic covers with base Q. The topology is then the one generated by this pretopology, which gives (★). This is consistent with the problem's assertion that the covers form a topology. Lemma 1.9 independently confirms the pretopology axioms.
2. "Finite presentation" is read as compactness in the under-category. Under the literal reading (finitely many generators and relations, then the int/sat/sharp reflection), Lemma 1.7 is immediate, and nothing else changes.
3. π^{-1}F = (Lan F)^#, where Lan is the presheaf left Kan extension. This is what the problem describes.

## C. Gaps and weaknesses, in order of severity (none affects the conclusion)
1. **(Interpretation, mild.)** Convention B1 is an assumption about the intended site. If the problem intends a different notion of covering sieve on objects Q ≠ P, the argument would need adapting. The draft states the convention explicitly, so this is not an error.
2. **(Quoted standard results.)** The proof quotes, rather than proves, the following: the topology generated by a pretopology (SGA4 II), the plus construction G^# = G^{++}, the equalizer description of Hom(R, G), enough injective sheaves, Gordan's lemma, Tychonoff's theorem, the universal coefficient surjection, and the double-complex lemma. All are standard, and I recall their statements as used.
3. **(Terse step.)** In Lemma 1.5(a), injectivity of colim_k Hom_P(Q', X_k) → Hom_P(Q', X) is only sketched ("uniquely up to going further"). The full argument is routine: first equalize the restrictions to Q at some stage, then use compactness of Q' under Q.
4. **(Terse step.)** In 1.2, the saturation witness needs x ∈ colim^gp to be written as a difference of elements at some stage, which is implicit in the text. In 4.6, cofinality of the Cov-sieves is used together with directedness of J(Q); this is implicit but correct.
5. **(Unused claims in §5.)** The characterization of birhizomy, the claim that "a separate referee check found this proof correct", and the dead-end remarks are not proved in the draft and are not used. They should not count as established.
6. **(Remark, not an error.)** The draft never uses infinitesimality. That is legitimate: the proof uses only two consequences of the definition, namely that the witness members are f.p. and that every valuation factors through some member.

## D. Conclusion
The main claim (YES) is proved by §§1–4 of the draft, under conventions B1–B3. I found no gap that invalidates any step. The open items are only the unproved, unused side claims of §5.

=== END OF ANSWER r3_verify ===
