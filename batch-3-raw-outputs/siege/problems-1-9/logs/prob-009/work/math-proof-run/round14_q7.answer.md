# round14_q7: attempt on (Rig) under the coarse reading (R2)

## Plan/status line (written first)
Plan: steps 2 and 3 of the suggested route, reformulated as *dichotomies in t*. Statement attempted:

**(JD)** Assume (Rig-v) for a product-type piece E_0. Then exactly one of the following holds:
- (V_t) of Proposition V holds for all t outside a closed discrete subset of Δ, and then K(E_t) ≡ K(E_0);
- (V_t) fails for all t outside a closed discrete subset of Δ. In this case t = 0 is an isolated "jump time".

Approach:
- §1: a dichotomy for condition (ii), via the branch divisor of the family of source maps over C° × Δ.
- §2: a dichotomy for condition (iii) with fixed source, via the branch divisor of a level-N fibre product.

Final status: **(JD) proved** (product type, under (Rig-v), coarse reading). **(Rig) itself: not proved; open.** What remains is exactly to exclude that the totally geodesic member is an isolated jump time.

Readings (R1) and (R2) are adopted (coarse; no (R2^orb)). G is of product type, E_0 is a piece, E_t := H_t(E_0), and M := M(E_0) = M(E_t) (L1′). The following are prior results, used as quoted in the brief and not re-proved: W (Lemma R0), 𝓦^ν, the puncture locus 𝓟, Lemma Deg, Lemma RH(a), Proposition V, Lemma CL, J0.

The following are cited from memory:
- **(Pur)** Purity of the branch locus (Zariski–Nagata), in the form needed: if f : X → Y is finite and surjective, X is a normal complex space and Y is a complex manifold, then the set B(f) of points of Y over which f is not a local covering is analytic and either empty or of pure codimension 1.
- **(Card)** For such f of degree d over a connected manifold Y, every fibre has at most d points, with equality exactly over Y ∖ B(f).
- **(Ext)** Uniqueness and existence of normal finite completions (Grauert–Remmert). Let Y be a manifold, A ⊂ Y a nowhere dense analytic set, and X°→ Y∖A a finite covering. Then there is, up to unique isomorphism over Y, exactly one normal complex space X finite over Y extending X°.

## 0. Setting under (Rig-v)
Assume (Rig-v): K^j_t = C̄ for all t. Here j is the Teichmüller vertex and C̄ the Teichmüller curve, with C^ν = H/Γ′.

Let n : 𝓦^ν → W be the normalisation. Then (pr_j ∘ n, t) factors through C̄^ν × Δ, by the universal property of normalisation, as in Cor. B of round8_q9. Call the factored map p̄ : 𝓦^ν → C̄^ν × Δ.

**Properties of p̄.**
- It is proper, since 𝓦^ν is proper over Δ.
- It has finite fibres, since each W_t maps finitely onto C̄.
- It is surjective.
- Its degree is d_0 (Lemma Deg).

Let C° := C^ν, the open orbifold curve. By Lemma RH(a), applied at every t, 𝓝 := p̄^{-1}(C° × Δ) = 𝓦^ν ∖ 𝓟. Write p̂ := p̄|_𝓝 : 𝓝 → C° × Δ. This map is finite and surjective of degree d_0, and 𝓝 is normal.

Let Orb ⊂ C° be the finite set of orbifold points.

**Lemma 0 (generic fibres).** Let D_1 be the set of t such that the fibre 𝓦^ν_t contains a singular point of 𝓦^ν or a critical point of t|_{Reg 𝓦^ν}. Then D_1 is closed and discrete. For t ∉ D_1, the fibre 𝓝_t is a smooth curve equal to Ê_t, and p̂|_{𝓝_t} = p_t.

*Proof.*
- **D_1 is closed and discrete.** Sing 𝓦^ν is discrete, because 𝓦^ν is a normal surface. The critical set of t on Reg 𝓦^ν is analytic. Its closure is analytic by Remmert–Stein, since it is added along a 0-dimensional set. Its 1-dimensional components lie in fibres, because t is constant along a curve of critical points. All these sets are closed analytic subsets of a space proper over Δ, and none of them contains a horizontal curve. So their images in Δ are closed and discrete.
- **The fibre for t ∉ D_1.** Here 𝓦^ν_t is a smooth compact curve. It maps finitely onto W_t = closure(E_t).
- **Degree count.** The fibre has d_0 points over a generic y ∈ C°, since p̂ has degree d_0 and the generic fibre count is constant. The curve Ê_t also has d_0 points over y, by Lemma Deg. So 𝓦^ν_t → W_t is generically injective.
- **Conclusion.** 𝓦^ν_t is therefore the normalisation of W_t. Removing 𝓟_t gives 𝓝_t = Ê_t. ∎

**Lemma 0′ (no vertical branching).** B := B(p̂) ⊂ C° × Δ contains no component of the form C° × {t*}. Every irreducible component Z of B is a horizontal curve, and its closure Z̄ ⊂ C̄^ν × Δ surjects properly onto Δ.

*Proof.*
- **No vertical component.** Fix any t*. For generic y ∈ C°, the curve W_{t*} has d_0 points over y: by Lemma Deg its normalisation maps with degree d_0. The fibre 𝓦^ν_{t*} surjects onto W_{t*}. So #p̂^{-1}(y, t*) ≥ d_0, and hence (y, t*) ∉ B by (Card). So B ⊅ C° × {t*}.
- **B is a curve.** By (Pur), B is pure 1-dimensional or empty. Each component is then not contained in a fibre.
- **Properness of Z̄.** Z̄ is closed in C̄^ν × Δ, and C̄^ν is compact, so Z̄ → Δ is proper.
- **Surjectivity of Z̄.** Z̄ is irreducible and not contained in a fibre. So the image of Z̄ is an irreducible closed analytic subset of Δ that is not a point, i.e. it is all of Δ. ∎

## 1. Proposition A (dichotomy for condition (ii))

**Proposition A.** Assume (Rig-v) for E_0. Then exactly one of the following holds.
- **(A1) Source rigidity.** Every component of B has the form {y} × Δ with y ∈ Orb. In this case:
  - there is an isomorphism 𝓝 ≅ Ê_0 × Δ over C° × Δ, with p̂ corresponding to p_0 × id;
  - every fibre 𝓝_t is Ê_t;
  - so (Ê_t, p_t) ≅ (Ê_0, p_0) for every t. In particular (ii) holds for every t, with Λ_t = Λ_0.
- **(A2)** Some component Z of B is not of the form {y} × Δ with y ∈ Orb. In this case (ii) fails for every t outside a closed discrete set D_A ⊂ Δ.

*Proof of (A2).*
- **Case Z = {y} × Δ with y ∉ Orb.** For t ∉ D_1, Lemma 0 identifies the fibre with Ê_t. Since (y, t) ∈ B, (Card) gives #p_t^{-1}(y) < d_0 = deg p_t. So p_t ramifies over the non-orbifold point y, and (ii) fails. Put D_A := D_1.
- **Otherwise.** Z̄ is not contained in any line {y} × Δ.
  - Hence Z̄ ∩ ((Orb ∪ cusps) × Δ) is a 0-dimensional analytic subset of Z̄. It is finite over compact subsets of Δ, by properness (Lemma 0′). Let T_Z be its image, which is closed and discrete.
  - Since Z̄ surjects onto Δ, for every t ∉ T_Z there is a point (y, t) ∈ Z with y ∈ C° ∖ Orb.
  - As in the first case, (ii) fails at every t ∉ T_Z ∪ D_1 =: D_A. ∎

*Proof of (A1).*
- **Covering over the complement of Orb.** Over (C° ∖ Orb) × Δ, the map p̂ is a finite covering of degree d_0. Its base is homotopy equivalent to C° ∖ Orb. Coverings are classified up to isomorphism by π_1 and are homotopy invariant, so this covering is isomorphic over the base to (Ê_0 ∖ p_0^{-1}(Orb)) × Δ.
  - Use for this its restriction to t = 0. That restriction is a covering of C° ∖ Orb whose normal completion is p_0 : Ê_0 → C°, because the fibre over 0 near points over C° ∖ Orb is smooth and equals Ê_0 there (unbranched cover of a manifold).
- **Extension over Orb.** Both 𝓝 and Ê_0 × Δ are normal and finite over C° × Δ, and they agree over the complement of Orb × Δ. By (Ext) they are isomorphic over C° × Δ.
- **Fibres.** Every fibre 𝓝_t ≅ Ê_0 is therefore smooth. It maps finitely onto E_t, with degree δ satisfying δ·d_0 = d_0 (Lemma Deg). So δ = 1, and 𝓝_t = Ê_t.
- **(ii) at every t.** p_t corresponds to p_0, so (ii) at t is (ii) at 0, which holds by TV item 3. ∎

**Remark A.** The proof never uses the profile of p_t over the orbifold points. In (A1) the profile is automatically constant. So the "redistribution with e ∤ m" mechanism of Lemma RH cannot occur without ramification also leaving the fibres over Orb.

## 2. Proposition B (dichotomy for condition (iii) when the source is rigid)

Assume (A1). Put S := Ê_0, and identify 𝓝 = S × Δ by Proposition A. Let G : S × Δ → M_M := ∏_{u∈M} M_u be the joint map pr_M ∘ n, and g_t := G(·, t). By (A1), the pulled-back orbifold O_t is O_0 = H/Λ_0 for every t. So (iii) at t says: g_t ∘ q_0 : H → M_M lifts holomorphically to T_M.

**Fixing the level structure and the auxiliary surface.**
- Fix N ≥ 3, and let Mod[N] ⊂ Mod_M be as in (R2′) of round13_q9. It is torsion-free and normal of finite index.
- Then M[N] := T_M/Mod[N] is a connected complex manifold.
- ρ : M[N] → M_M is the quotient by the finite group A := Mod_M/Mod[N].
- Fix a torsion-free normal subgroup Λ″ ⊂ Λ_0 of finite index (Selberg). Put R := H/Λ″, and let π : R → S be the induced orbifold covering. R is a Riemann surface of finite type, with compactification R̄.

**Lemma B1 (local criterion).** (iii) holds at t if and only if g_t ∘ π is locally liftable through ρ at every point of R.

*Proof.*
- (⇒) Compose a lift F : H → T_M with T_M → M[N]. The map H → R is a local biholomorphism, so this gives local lifts on R.
- (⇐) Let F_t be the normalised fibre product of R with M[N] over M_M. Local liftability everywhere means that F_t → R is unbranched, so F_t is a disjoint union of finite coverings of R.
  - Take a component R′ = H/Λ‴ with Λ‴ ⊂ Λ″. It carries a holomorphic map R′ → M[N] over g_t ∘ π.
  - T_M → M[N] is a covering map, since Mod[N] acts freely and properly. H is simply connected, so the map lifts to F : H → T_M with p_M ∘ F = g_t ∘ q_0. ∎

**The compactified family.**
- Φ := G ∘ (π × id) : R × Δ → M_M.
- **Extension of G.** By (A1) and (Ext) over neighbourhoods of the cusps, 𝓦^ν ≅ S̄ × Δ. So G extends to S̄ × Δ → ∏M̄_u, and Φ extends to Φ̄ : R̄ × Δ → ∏M̄_u.
- **Compactified level space.** Let M̄[N] be the normalisation of ∏M̄_u in M[N]. It is finite over ∏M̄_u and restricts to M[N] over M_M, because M[N] is normal and finite over M_M. (Cited from memory: existence of this normalisation.)
- Let 𝓢̄ be the normalisation of the components of (R̄ × Δ) ×_{∏M̄} M̄[N] that dominate R̄ × Δ. It is finite over R̄ × Δ, hence proper over Δ.
- Let B̄ := B(𝓢̄ → R̄ × Δ), and B_S := B̄ ∩ (R × Δ). The latter is the branch locus of the normalised fibre product 𝓢 over R × Δ, because normalisation is local.
- **Non-injectivity locus.** Let 𝓝𝓘 ⊂ 𝓢̄ be the set of points whose image in the fibre product is also the image of another point. It is the projection of the non-diagonal components of 𝓢̄ ×_F 𝓢̄. So it is analytic of dimension ≤ 1, because normalisation is bimeromorphic.

**The exceptional set D_3.** D_3 ⊂ Δ is the set of times t over which at least one of the following happens:
- B̄ has a vertical component, or a singular point;
- a horizontal component of B̄ is ramified over Δ;
- a horizontal component of B̄ different from a line {p} × Δ meets {p} × Δ, for p a puncture of R̄;
- 𝓝𝓘 has a vertical component.

Each of these is a closed analytic subset of a space proper over Δ, and none contains a horizontal curve. So D_3 is closed and discrete.

**Lemma B2 (fibre criterion).** Let t ∉ D_3. Then (iii) holds at t if and only if B_S ∩ (R × {t}) = ∅. The implication "⇐" holds for every t.

*Proof.*

**(⇐), for every t.** Let x ∈ R. A neighbourhood U × Δ′ of (x, t) misses B_S, so over it 𝓢 is a finite unbranched covering of a simply connected base, hence trivial.
- A sheet is the graph of a holomorphic map to M[N] that lifts Φ.
- Restricting to time t gives a local lift of g_t ∘ π at x.
- Conclude by Lemma B1.

**(⇒) for t ∉ D_3: the local model.** Let (x, t) ∈ B_S. Then (x, t) lies on a horizontal component Z of B̄ that is smooth and transverse to the fibres there. So there are coordinates (a, s) near (x, t) with Z = {a = 0}, s = time, and a restricted to the fibre a coordinate at x.
- On a small polydisc P, π_1(P ∖ Z) = ℤ. So 𝓢 over P is, by (Ext), a disjoint union of sheets (α, s) ↦ (α^k, s).
- Since (x, t) ∈ B_S, some sheet Σ has k > 1. Let μ : Σ → M[N] be its map, so that ρ ∘ μ = Φ ∘ (α^k, s).

**(⇒): a lift gives a contradiction.** Suppose g_t ∘ π had a local lift L at x.
- On the punctured slice {(α, t) : α ≠ 0}, the maps μ(·, t) and L(·^k) are holomorphic lifts through ρ of the same map. So they differ pointwise by elements of the finite group A.
- By the Baire and identity-theorem argument of Lemma CS, μ(α, t) = c·L(α^k) for a single c ∈ A.
- Hence μ(ζα, t) = μ(α, t) for ζ^k = 1. So the distinct points (α, t) and (ζα, t) of Σ have the same image in the fibre product.
- So the punctured slice curve lies in 𝓝𝓘. The irreducible component of 𝓝𝓘 containing it has t constant on an open subset, hence everywhere. That component is vertical, so t ∈ D_3, a contradiction. ∎

**Proposition B.** Assume (Rig-v) and (A1). Then exactly one of the following holds.
- **(B1)** Every horizontal component of B̄ is a line {p} × Δ through a puncture p of R̄. Then (iii) holds for all t ∉ D_3.
- **(B2)** Some horizontal component Z ≠ {p} × Δ exists. Then (iii) fails for all t outside a closed discrete set D_B.

*Proof.*
- **(B1).** For t ∉ D_3 there is no vertical component at t, so B_S ∩ (R × {t}) = ∅. Lemma B2 gives (iii).
- **(B2).** Z is proper over Δ and surjective, as in Lemma 0′. Its intersection with the finitely many lines {p} × Δ has discrete image in Δ. So for t outside a closed discrete set, Z meets R × {t}. Lemma B2 then gives that (iii) fails for t ∉ D_3 ∪ (this set) =: D_B. ∎

## 3. Theorem JD (jump dichotomy) and what it reduces (Rig) to

**Theorem JD.** Let E_0 be a product-type piece satisfying (Rig-v). Exactly one of the following holds.
- **(G) Generic case.** (A1) and (B1) hold. Then (V_t) holds for all t outside a closed discrete set, and hence K(E_t) = K(E_0) for all t by Proposition V(b). In this case:
  - the normalised source and its map to C^ν are constant;
  - all puncture values of the vertices in M are constant (Cor. S′ of round8_q7).
- **(J) Jump at 0.** (A2) holds, or (A1) and (B2) hold. Then (V_t) fails for all t outside a closed discrete set, while (V_0) holds (TV, J0). So 0 is an isolated point of {t : (V_t)}.
  - In case (A2), a horizontal branch curve Z of p̂ leaves Orb × Δ for t ≠ 0. At t = 0 the possibilities are as follows:
    - If 0 ∉ D_1, then Z meets the fibre t = 0 only over Orb ∪ cusps, because TV item 3 places all ramification of p_0 = p̂|_{𝓝_0} over Orb.
    - If 0 ∈ D_1, Z may also pass through a point over which the fibre 𝓝_0 is singular, even though p_0 on its normalisation Ê_0 is unramified there. This is the fixed-image (ram) mechanism, now *forced to happen for all small t ≠ 0*, not just some.
  - In case (B2), a horizontal branch curve Z of the level-N fibre product has one of two behaviours at t = 0. Either Z meets R × {0} at a point where the fibre over 0 is special (0 ∈ D_3; mechanisms (cross)/(fix)), or Z meets the fibre over 0 only at punctures, i.e. a joint cone point "emerges from a puncture".

*Proof.* Propositions A, B and V. In (G), the set of good times is co-discrete in Δ, hence uncountable, so Proposition V(b) applies. In (J), the failure statements are Propositions A(A2) and B(B2). ∎

**Consequence (precise form of the remaining gap).** Under (Rig-v), (Rig) for the family of E_0 fails only if E_0 is in case (J).
- (R1) and (R2) are symmetric under changing the base time: H(H_{t_1}^{-1}(·), ·) is again an admissible trivialisation. The only asymmetry is total geodesy of V_0, which is what gives (V_0).
- So the open question is exactly whether **the totally geodesic member can be an isolated jump time**. Equivalently: is (V_t) an "open condition at a totally geodesic member"?
- No argument based on (R1), (R2) alone can answer it. Round6_q7's local models realise (J) for families of maps. Lemma Loc and Examples Z/Z′ show that piece-level and germ-level data do not decide it.

**Corollary JD′.** Proposition V's hypothesis "(ii) and (iii) for uncountably many t" is equivalent to "(ii) and (iii) for all t outside a closed discrete set". It is also equivalent to "for t in some set with an accumulation point in Δ".

## 4. Items of the suggested route not settled
- **Step 1, (Rig-v) under (R2) at an image-level type jump.** Not touched; still open. Theorem JD assumes it.
- **Step 2, fixed-image (ram).** Reduced to excluding (A2), i.e. a horizontal branch curve leaving Orb × Δ at the totally geodesic member and then staying off it for all small t ≠ 0. Not excluded.
- **Step 3, joint cone points.** Reduced to excluding (B2), in the presence of (A1). Not excluded.
- **Step 4, non-product strata.** Not treated. Propositions A and B use the product structure only through Lemma Deg, W and L1′. The twin ambiguity of lifting pieces is untouched.

## 5. Final status
**Proved here.** These hold in product-type strata, under (R1), (R2) (coarse reading) and (Rig-v). Prior results are used as quoted. (Pur), (Card), (Ext), Selberg, Remmert–Stein and the level-N normalisation are cited from memory.
- Lemma 0 / 0′: fibres are generic outside a discrete set, and p̂ has no vertical branching.
- Proposition A, the dichotomy for (ii):
  - either the source family is constant, i.e. 𝓝 ≅ Ê_0 × Δ with p_t = p_0 and Λ_t = Λ_0;
  - or (ii) fails off a closed discrete set.
- Lemmas B1, B2 and Proposition B, the dichotomy for (iii) when the source is rigid.
- Theorem JD: (Rig) holds for the family of E_0 unless t = 0 is an isolated jump time of (V_t), i.e. (V_0) holds while (V_t) fails off a closed discrete set. Corollary JD′ follows.

**Not proved.** (Rig) under the coarse reading. Equivalently, given (Rig-v), the exclusion of case (J) at the totally geodesic member.

**Open (named).**
1. **(Jump-TG).** Can a totally geodesic V_0 be an isolated jump time, in case (A2) or (B2), for some boundary piece of an admissible family? The hypotheses (R1), (R2) are symmetric in the base time, so only total geodesy can exclude this.
2. (Rig-v) at image-level type jumps.
3. Non-product strata (twins).
4. The realisability questions Q1/Q2 from earlier rounds.

Entry 82 under the coarse reading: **not proved / open** (partial: Theorem JD).

=== END OF ANSWER round14_q7 ===
