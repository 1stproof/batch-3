# round5_q7: the Kobayashi / length-spectrum rigidity approach to MS4

## Plan
Attempted: MS4 by transporting McMullen's rigidity argument from Teichmüller curves to surfaces. The outcome is that the approach, as suggested, **fails or is circular** at a precisely identifiable step. Along the way I prove:
- (§1) a one-point pinning criterion;
- (§2) a Teichmüller-curve criterion, together with the fact that "persistence of a Teichmüller curve T in V_t" is *equivalent* to "T ⊂ V_t";
- (§3) that holomorphically trivial deformations are trivial. This shows that the hypothesis of PR-6 Theorem B can never hold, so the counterexample mechanism of PR-6 is void;
- (§4) the domination inequality, with a proof, and the reasons why no "domination ⇒ equality" step is available.

MS4 itself is **not proved** here.

Standing conventions: (R1) and (R2) as in the task. Orbifold issues are handled as in PR-4, by passing to a finite level cover M_g[m], m ≥ 3, and I suppress them. Results cited from memory are marked **[mem]**.

---

## §1. One-point pinning (proved)

**Lemma 1.** Suppose there is a set S ⊂ Δ with an accumulation point in Δ such that, for each t ∈ S, closure(V_t) ∩ closure(∂V_0) ∩ Δ_Γ ≠ ∅. Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. Fix t ∈ S and a point p in the intersection.
2. Since p ∈ closure(V_t) ∩ Δ_Γ = ∂V_t, we have π_i(p) = Y_t.
3. Since p ∈ closure(∂V_0) ∩ Δ_Γ, and the latter set equals ∂V_0 because ∂V_0 is closed in Δ_Γ, we have π_i(p) = Y_0.
4. So Y_t = Y_0 on S. The map t ↦ Y_t is holomorphic (PR-1), so the identity theorem gives Y ≡ Y_0. ∎

So MS4 is equivalent to the statement that ∂V_t meets ∂V_0 for t in a set accumulating in Δ. Conversely, if Y_t ≠ Y_0 then ∂V_t ∩ ∂V_0 = ∅.

---

## §2. Teichmüller curves: persistence is equivalent to containment

**Cited theorem (McMullen, rigidity of Teichmüller curves) [mem].** Let f : B → M_g be a Teichmüller curve, with B a hyperbolic Riemann surface of finite type. Let f' : B' → M_g be a holomorphic map from a Riemann surface of finite type, and let h : B → B' be a homeomorphism (preserving punctures) such that f' ∘ h is homotopic to f. Then f'(B') = f(B). In fact h is homotopic to a biholomorphism B → B' that intertwines the maps up to finite ambiguity.

The proof is the one recalled in the task:
- Royden's theorem plus Schwarz–Pick give ℓ_{B'}(h_*γ) ≥ τ_T(ρ(γ)) = ℓ_B(γ) for all γ.
- Thurston's theorem (a surface of the same finite-area type cannot have its length spectrum dominate unless isometric) gives B' ≅ B.
- Imayoshi–Shiga then gives f' = f ∘ h^{-1} up to finitely many choices. Continuity in a parameter removes this ambiguity.

**Proposition 2.** Let T = f(B) ⊂ V_0 be a Teichmüller curve with closure(T) ∩ ∂V_0 ≠ ∅. Fix t. The following are equivalent:
- (a) there is a holomorphic map f_t : B_t → V_t from a finite-type Riemann surface, and a homeomorphism h : B → B_t, such that ι_t ∘ f_t ∘ h is homotopic to ι_0 ∘ f, where ι_s : V_s ⊂ M_g;
- (b) T ⊂ V_t.

If (a) or (b) holds for all t in a set accumulating in Δ, then Y_t ≡ Y_0.

*Proof.*
1. (b) ⇒ (a): take f_t = f.
2. (a) ⇒ (b): by the cited theorem, f_t(B_t) = T, so T ⊂ V_t.
3. Under (b), closure(T) ⊂ closure(V_t). Pick p ∈ closure(T) ∩ ∂V_0. Then p ∈ closure(V_t) ∩ ∂V_0, and Lemma 1 applies. ∎

In particular, a family f_t ⊂ V_t obtained by continuously deforming f along the trivialization of (R2) would give (a), because the homotopy then exists automatically.

**Consequence for the suggested strategy (first bullet of the task).** "Show that T forces a holomorphic curve T_t ⊂ V_t homotopic to T" is *literally equivalent* to "T ⊂ V_t". So it carries the full difficulty: it is the claim that V_t contains a fixed curve of V_0. At first order this is the following.

- Let σ ∈ H^0(V_0, N_{V_0/M_g}) be the first-order deformation (the Kodaira–Spencer normal section) defined by 𝒱.
- Suppose a curve deformation T_t ⊂ V_t exists. Then T_t = T by the above, so T ⊂ V_t for all small t, and the first-order normal motion of V_0 vanishes along T, i.e. σ|_T = 0.
- So persistence of the Teichmüller curves of a dense family forces σ ≡ 0. That is first-order rigidity of V_0, which is exactly what is unknown.

Deformation theory cannot produce T_t either.
- The obstruction to lifting T into the fibres of 𝒱 lies in H^1 of the (log) normal bundle N_{T/V_0}.
- That group is in general nonzero. T is rigid in V_0, so h^0(N) = 0, and Riemann–Roch gives h^1(N) = −χ(N) = −deg N + g(T̄) − 1.
- By analogy with totally geodesic curves in locally symmetric surfaces (e.g. the diagonal in C × C has self-intersection 2 − 2g), I expect this to be positive. I have not proved deg N < 0 here.
- Even where h^1 = 0 one gets T_t ⊂ V_t only for those t, and then T_t = T, i.e. the conclusion T ⊂ V_t again.

**Status.** Proposition 2 is proved, modulo the cited McMullen theorem. It turns the first suggested route into the equivalent problem "V_t ⊃ T". I could not solve that.

---

## §3. Holomorphically trivial deformations are trivial; PR-6's mechanism is void

**Proposition 3.** Suppose there are biholomorphisms Φ_t : V_0 → V_t with (x,t) ↦ Φ_t(x) continuous and Φ_0 = id. Then V_t = V_0 for all t, so Y_t ≡ Y_0.

This is PR-4 Theorem B. I re-checked its proof:
- through every x ∈ V_0 there passes an algebraic curve, with normalization ν : S → V_0 and ν(s_x) = x;
- Lemma 0 (Imayoshi–Shiga finiteness, cited, plus connectedness of Δ) applied to Φ_t ∘ ν gives Φ_t(x) = x.

The only external input is the Imayoshi–Shiga / Arakelov–Parshin finiteness [mem].

**Corollary 3′ (correction to PR-6).** No holomorphic vector field ξ satisfying (a) and (b) of PR-6 Theorem B, with v(Y_0) ≠ 0, exists. More generally, every logarithmic holomorphic vector field ξ defined near closure(V_0) is tangent to V_0 along V_0.

*Proof.*
1. Let Φ_s be the flow of ξ. For |s| small, Φ_s restricts to biholomorphisms V_0 → Φ_s(V_0), continuous in s with Φ_0 = id. These are subvarieties of M_g: Φ preserves M_g and the strata, and Chow's theorem applies, as in PR-6 step 2.
2. Proposition 3 gives Φ_s(V_0) = V_0 for all small s, so ξ is tangent to V_0 along V_0.
3. Under (b), PR-6 shows that π_i(Φ_s(∂V_0)) = {φ_s(Y_0)}. Since Φ_s(V_0) = V_0, it is also {Y_0}. Hence φ_s(Y_0) = Y_0 for small s, and v(Y_0) = 0. ∎

So the "open question" at the end of PR-6 is settled in the negative: PR-6's construction never yields a counterexample. **Any counterexample to MS4 must be a family in which the abstract complex structure of V_t, or of the pair (closure V_t, boundary), genuinely varies.** That is, the family 𝒱 → Δ is not holomorphically locally trivial near any t. Equivalently, the problem is a statement about the Kodaira–Spencer class of 𝒱, not about ambient motions.

---

## §4. The domination step: what holds and why it does not close

Setting:
- p_t : Ṽ_t → V_t is the universal cover, with deck group π := π_1(V_t), identified with π_1(V_0) via (R2);
- F_t : Ṽ_t → T_g is a holomorphic ρ-equivariant lift of V_t → M_g. Here ρ : π → Mod_g is the same for all t up to conjugacy, because the classifying maps are homotopic by (R2);
- k_t is the Kobayashi pseudo-distance of Ṽ_t, and λ_t(γ) := inf_x k_t(x, γx).

**Lemma 4 (domination; proved, using Royden's theorem [mem]: Kobayashi = Teichmüller distance on T_g).**
- (i) For all γ ∈ π and all t, λ_t(γ) ≥ τ_T(ρ(γ)) := inf_y d_T(y, ρ(γ)y).
- (ii) Let D ⊂ Ṽ_0 be a holomorphic disc such that F_0|_D is a Teichmüller disc (an isometry for k_D and d_T). Suppose γ preserves D and ρ(γ) is pseudo-Anosov with axis in F_0(D). Then λ_0(γ) = τ_T(ρ(γ)).

*Proof.*
- (i) Holomorphic maps do not increase Kobayashi distance, so d_T(F_t x, ρ(γ)F_t x) = d_T(F_t x, F_t γx) ≤ k_t(x, γx). Take the infimum over x.
- (ii) Take x ∈ D with F_0(x) on the axis. Then k_0(x, γx) ≤ k_D(x, γx) = d_T(F_0 x, F_0 γx) = τ_T(ρ(γ)). Combine with (i). ∎

**Why "domination ⇒ equality ⇒ rigidity" fails for surfaces, as far as I can see.**

1. *No Thurston theorem.* For curves, equality is forced by Thurston's theorem. Its engine is that two finite-area hyperbolic surfaces of the same type have the same area (Gauss–Bonnet), so a 1-Lipschitz-on-lengths comparison cannot be strict. For V_t one would need:
   - an intrinsic "size" of Ṽ_t/π, for instance the Kobayashi–Eisenman volume, that is a topological invariant, or at least is bounded above by its value at t = 0;
   - and a rigidity statement for equality.

   Neither is available. The Kobayashi–Eisenman volume is not known to be topological for quasi-projective surfaces. It is for compact ball quotients (Miyaoka–Yau equality), but those are rigid for other reasons (Calabi–Vesentini), and V_0 is not known to be such. Moreover, Lemma 4 only controls the thin set of γ that stabilize Teichmüller discs, not the whole spectrum.

2. *Equality would still not give discs.* Suppose one had λ_t(γ) = τ_T(ρ(γ)) for every disc-stabilizing γ. To conclude T ⊂ V_t (§2) one needs a holomorphic disc in Ṽ_t realizing the translation length. Kobayashi extremal discs in a general complex surface need not exist or be unique, so this does not follow either. Conversely, by §2 the existence of such a disc is equivalent to the conclusion T ⊂ V_t.

3. *Energy / calibration.* An "area of F_t" calibration argument would need a Kähler form on T_g whose restriction to totally geodesic surfaces calibrates them, with equality only for totally geodesic surfaces. The Teichmüller metric is Finsler, not Kähler. On Teichmüller discs it is the hyperbolic metric, but it gives no 2-form that is closed and positive with the required comparison on 2-planes that are not complex lines of a Teichmüller disc. I know of no such calibration [mem; I am not aware of one in the literature].

4. *Use of the cusps (R2).* By §1 everything reduces to producing one common boundary point of ∂V_t and ∂V_0. The Kobayashi data near a cusp of V_t are local holomorphic invariants of the germ of closure(V_t) near ∂V_t. These are topologically controlled by (R2) only up to homeomorphism, so they give no such point.

**Summary of the obstruction.** The approach needs one of the following:
- a substitute for Thurston's minimal-stretch theorem for the Kobayashi geometry of quasi-projective surfaces, with a topological volume;
- or a proof that the Teichmüller curves of V_0 (or one of them with a cusp on ∂V_0) lie in V_t.

By §2 the second is not a consequence of deformation theory: it is equivalent to the conclusion restricted to T. By §3, the remaining possible counterexamples are exactly the families with varying complex structure, which no ambient-flow argument can see.

---

## §5. Final status

**Proved** (under (R1) and (R2), using only the cited Royden, Imayoshi–Shiga and McMullen theorems [mem]):
- Lemma 1: MS4 holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t in a set accumulating in Δ.
- Proposition 2: for a Teichmüller curve T ⊂ V_0 with closure(T) ∩ ∂V_0 ≠ ∅, a homotopic holomorphic curve in V_t exists iff T ⊂ V_t. If this holds for t accumulating in Δ, then MS4 holds.
- Proposition 3 and Corollary 3′: holomorphically locally trivial families are trivial. In particular PR-6's vector-field construction never gives a counterexample, which corrects/settles PR-6's open question. Every log vector field near closure(V_0) is tangent to V_0.
- Lemma 4: the Kobayashi translation-length domination λ_t ≥ τ_T∘ρ, with equality at t = 0 on disc-stabilizing pseudo-Anosovs.

**Not proved:** MS4 itself. The suggested transport of McMullen's argument breaks at the "domination ⇒ equality" step (§4.1–4.3). Its curve-based variant is equivalent to the conclusion (§2).

**Open questions, named explicitly:**
- (Q1) Does every closed Teichmüller curve T ⊂ V_0 with a cusp on ∂V_0 lie in V_t for small t? Equivalently, for each such T, does V_t contain a holomorphic curve homotopic to T? A positive answer for a single such T proves MS4, via Proposition 2.
- (Q2) Is there a topological upper bound for the Kobayashi–Eisenman volume of V_t, attained at t = 0, together with an equality-rigidity statement? This would be a Thurston-type theorem for surfaces.
- (Q3) Is the first-order normal deformation σ ∈ H^0(N_{V_0/M_g}) of a totally geodesic surface necessarily zero, i.e. is the Douady space at closure(V_0) a reduced point, as in PR-5? By §3, a nonzero σ must have nonzero Kodaira–Spencer image δ(σ) ∈ H^1(T_{V_0}) at some order. Whether that can happen is the heart of MS4.
- (Q4) Are closed Teichmüller curves dense in every totally geodesic surface? (True when the associated orbit closure is defined over ℚ, since square-tiled surfaces are then dense [mem]; unknown to me in general.) And does some such curve have a cusp exactly on ∂V_0?

=== END OF ANSWER round5_q7 ===
