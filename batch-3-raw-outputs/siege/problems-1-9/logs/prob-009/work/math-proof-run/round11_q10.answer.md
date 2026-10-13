# round11_q10: attempt on (Rig) / (Rig-v): maximum-principle route

## Status / plan (written first)
Plan:
1. Point 1 of the task. Replace the orbifold-sensitive inputs (type jumps, m_0) by a purely image-level global input: a plurisubharmonic (psh) function near the Teichmüller curve. Statement attempted: Prop. MP. If K^v_0 is "psh-isolated", then (Rig-v) holds. No orbifold bookkeeping, no m_0, no type jump.
2. Test whether psh-isolation, or its algebraic shadow (negative self-intersection), can hold in general. Statement attempted: Prop. DP. For vertices of type (0,5), every closed Teichmüller curve moves in a linear pencil of curves in M̄_{0,5}. So psh-isolation fails there, and (Rig-v) cannot come from the ambient geometry of M̄_v alone.
3. The same principle applied to closure(V_0) itself (Prop. MP′), and what it would need.

Readings (R1), (R2) of the task are adopted throughout. G is product type. E_0 is a piece, E_t := H_t(E_0), and W is the 2-dimensional family of Lemma R0 (prior result, not re-proved), proper over Δ with W_t = closure(E_t). K^v_t := pr_v(W_t).

Final status: see §5. **(Rig), (Rig-w) and (Rig-v) are not proved in general.**

## 1. Prop. MP: a maximum-principle criterion for (Rig-v) and (Rig) (proved)

Conventions.
- M̄_v is the coarse projective variety, a normal complex space.
- A function φ : Ω → [−∞, ∞) on an open subset Ω of a normal complex space is *psh* if it is upper semicontinuous and every point has a neighbourhood with a local embedding into some ℂ^N on which φ is the restriction of a psh function.
- The pull-back of a psh function by a holomorphic map from a connected Riemann surface is subharmonic or ≡ −∞.

**Proposition MP.** Let M ⊂ V(G) be a set of vertices and K_0 := K^M_0 = pr_M(W_0) ⊂ ∏_{u∈M} M̄_u. Assume K_0 is a curve. Write M_M := ∏_{u∈M} M_u and ∂_M := ∏_{u∈M} M̄_u \ M_M. Suppose there are:
- an open neighbourhood U of K_0 in ∏_{u∈M} M̄_u, and
- a psh function φ on U ∩ M_M that is bounded above,

such that

(★) for every irreducible compact curve C ⊂ U with C ⊄ ∂_M and C ≠ K_0, the function φ is not constant on C ∩ M_M.

Then K^M_t = K_0 for all t ∈ Δ. In particular:
- M = {v} with v a Teichmüller vertex gives (Rig-v);
- M = M(E_0) gives (Rig) for this piece;
- (Rig) for this piece in turn gives (Rig-w) for this piece, by round8_q7 Cor. S′(a).

*Proof.*
- **Step 1 (K^M_t ⊂ U for small t).** Suppose not. Then there are t_n → 0 and x_n ∈ W_{t_n} with pr_M(x_n) ∉ U. W is proper over Δ, so after passing to a subsequence x_n → x ∈ W. Since W is closed, x ∈ W_0. Then pr_M(x) ∈ K_0 ⊂ U, and U is open, so pr_M(x_n) ∈ U for large n. This is a contradiction. Hence there is ε > 0 with K^M_t ⊂ U for |t| < ε.
- **Step 2 (K^M_t is an irreducible compact curve not inside ∂_M).**
  - W_t = closure(E_t) is irreducible, because E_t = H_t(E_0) is irreducible (round8_q7 Lemma S″, prior result).
  - So K^M_t is irreducible and compact (Remmert).
  - It is a curve, because "pr_M non-constant on E_t" does not depend on t (L1′, prior result).
  - It meets M_M, because E_t ⊂ ∏_w M_w.
- **Step 3 (maximum principle).** Fix |t| < ε and let n : C̃ → K^M_t be the normalisation. C̃ is a compact connected Riemann surface.
  - F := n^{-1}(∂_M) is a proper analytic subset of C̃, hence a finite set.
  - ψ := φ∘n is subharmonic (or ≡ −∞) on C̃ \ F and bounded above.
  - A subharmonic function that is bounded above extends subharmonically across a finite set (removable singularities). So ψ extends to a subharmonic function on the compact connected C̃, or is ≡ −∞.
  - By the maximum principle ψ is constant. Hence φ is constant on K^M_t ∩ M_M.
  - By (★), K^M_t = K_0 for |t| < ε.
- **Step 4 (all t).** Lemma CD (round10_q9) with C := K_0: the set T_C contains the disc |t| < ε, so it is not discrete. Hence T_C = Δ and K^M_t = K_0 for all t. ∎

**Remarks.**
1. Prop. MP compares closed image sets only, so it does not see:
   - orbifold type jumps at t = 0;
   - the multiplicity m_0;
   - the degree d_0;
   - the twin/labelling ambiguities.

   It needs one global input: a psh "potential" around K_0 that separates K_0 from all other compact curves nearby. This is the "global input" of task item 1, in a form that does not need the deformation to be totally geodesic.
2. It is enough to verify (★) for the curves that actually occur, C = K^M_t with t small. The proof uses (★) only for them.
3. (★) forces a strong rigidity: K_0 is not the limit of any family of compact curves C_s ≠ K_0 (s → 0) contained in U. Steps 1–3 apply verbatim to such a family. So (★) can only hold if K_0 is *infinitesimally isolated among compact curves*, whatever their boundary behaviour. §2 shows this fails in general.

## 2. Prop. DP: psh-isolation and negativity fail for vertices of type (0,5) (proved, modulo classical facts cited from memory)

**Classical facts used (cited from memory).**
- (F1) M̄_{0,5} is the del Pezzo surface S_5 of degree 5, i.e. the blow-up of ℙ² at 4 general points. It is smooth and projective, with −K_S ample, K_S² = 5 and χ(O_S) = 1.
- (F2) ∂M̄_{0,5} is the union of the ten (−1)-curves D_{ij} of S_5.
- (F3) M_{0,5} contains closed Teichmüller curves. Example: take a Veech-type Teichmüller curve of genus-2 forms ω ∈ ΩM_2(2) and divide by the hyperelliptic involution J. Then ω² descends to a quadratic differential on ℙ¹ with simple poles at the 5 Weierstrass points other than the zero, and a simple zero at the image of the zero. Its Teichmüller disc in T_{0,5} has a lattice stabiliser, so it projects to a closed Teichmüller curve, and a component of its preimage in the labelled M_{0,5} is again one.

**Proposition DP.** Let C ⊂ M̄_{0,5} = S_5 be the closure of any irreducible curve meeting M_{0,5}, e.g. a closed Teichmüller curve. Then:
- (a) C² ≥ 0;
- (b) dim |C| ≥ 1. In particular C is a member of a pencil of curves, all compact and linearly equivalent to C, filling S_5.

Consequently, if v is a vertex of type (0,5) and K^v_0 is a Teichmüller curve:
- no psh function as in Prop. MP exists for M = {v};
- no negativity argument (K_t·K_0 ≥ 0 versus K_0² < 0) can give (Rig-v).

*Proof.*
- **(a).** Adjunction gives C² + K_S·C = 2p_a(C) − 2 ≥ −2. Since −K_S is ample, K_S·C ≤ −1, so C² ≥ −1. If C² = −1, then p_a = 0 and K_S·C = −1, so C is a (−1)-curve. By (F2) C would then be a boundary curve, contradicting C ∩ M_{0,5} ≠ ∅. Hence C² ≥ 0.
- **(b).**
  - Riemann–Roch on S_5 gives h^0(O(C)) − h^1(O(C)) + h^2(O(C)) = 1 + (C² − K_S·C)/2.
  - h^2(O(C)) = h^0(O(K_S − C)) = 0, because (K_S − C)·(−K_S) < 0 and −K_S is ample.
  - Hence h^0(O(C)) ≥ 1 + (C² − K_S·C)/2 ≥ 1 + (0 + 1)/2. As h^0 is an integer, h^0(O(C)) ≥ 2, i.e. dim |C| ≥ 1.
- **Consequence for Prop. MP.**
  - Let {C_s} be a pencil in |C| through C = C_0. Its members are compact curves, and C_s → C_0 as s → 0 (in the Hausdorff sense, after choosing a line in |C| through C).
  - For small s ≠ 0, C_s ⊂ U. This is Step 1 of Prop. MP, applied to the incidence variety of the pencil, which is proper over the parameter line.
  - Moreover C_s has an irreducible component C′_s ≠ C_0. Otherwise C_s = k·C_0 + 0 with k = 1 by linear equivalence (pair with an ample class), so C_s = C_0 as divisors, which is false for s ≠ 0.
  - C′_s is compact, irreducible, not inside ∂ (otherwise it would be a line D_{ij}; but a fixed line cannot be a component of C_s for all small s, since then it would be a component of the limit C_0 — and only finitely many members of a pencil without fixed component contain a given curve; if D_{ij} is a fixed component of the pencil, remove the fixed part first, which does not affect C_0 = C irreducible ⊄ ∂).
  - Steps 1–3 of the proof of Prop. MP then make φ constant on C′_s ∩ M_{0,5}, contradicting (★). So no such φ exists.
- **Consequence for the intersection argument.** The would-be argument runs: Lemma Deg gives [K_t] = (d_0/d_t)[K_0] in H_2(M̄_v; ℚ), and K_t ≠ K_0 forces K_t·K_0 ≥ 0, which contradicts K_0² < 0. Since K_0² ≥ 0 by (a), this argument cannot start. ∎

(Fixed components: a pencil |C| ⊃ {C_s} may have a fixed part F. Since C_0 = C is irreducible and C_0 = F + (moving part at s = 0), and the moving part is non-zero, F = 0. So the pencil has no fixed component, and a given curve is a component of only finitely many members.)

**What Prop. DP shows.**
- (Rig-v) is not a consequence of the position of the Teichmüller curve K^v_0 in M̄_v. Nearby compact curves, even homologous ones, exist.
- So any proof must use the constraints the problem puts on K^v_t, which are:
  - (c1) K^v_t is the v-image of a piece of a surface V_t in M_g. This is global and is what Lemma Loc said cannot be used locally.
  - (c2) the boundary trace K^v_t ∩ ∂M̄_v is the v-image of H_t-transported punctures, with stratum-preserving behaviour (Lemma P0). This is a strong constraint on the members of |K_0|: a generic member of the pencil meets the ten lines D_{ij} transversally at points that move, while K_0 itself, a Teichmüller curve, meets ∂ at its cusps. The cusps are typically the 0-dimensional strata, where a cylinder decomposition with 2 cylinders pinches two curves.
- This is consistent with Examples Z, Z′ (round8_q9) and Lemma Loc (round9_q9). Prop. DP adds that even the *ambient* geometry of a single factor is not enough. Whatever pins K^v_t must be the boundary constraint (c2), combined with (c1).

**The intersection version that would use (c2) (open).** Let 𝔽 ⊂ |C| be the family of members C′ whose intersection with ∂M̄_{0,5}, as a 0-cycle on each D_{ij} with the stratum data, has the "same combinatorial type" as C ∩ ∂ (same strata, same local contact orders), with the points allowed to move.
- (Q-DP) Is a closed Teichmüller curve isolated in 𝔽?
- This is a concrete, finite-dimensional question about plane curves (via S_5 → ℙ²) that I have not answered.
- Under (Rig-v) one needs exactly isolation of K_0 among the K^v_t. By Lemma P0 and node counting, those lie in 𝔽 provided the contact orders are also transported. That transport is not proved: H_t is only a homeomorphism, but local intersection multiplicities of a curve with a divisor are topological invariants (linking numbers) once the curve and divisor are fixed analytic sets, so I expect this step to go through.

## 3. Prop. MP′: the same principle for the whole surface (proved; hypothesis open)

**Proposition MP′.** Suppose closure(V_0) has an open neighbourhood U in M̄_g and a psh function φ on U ∩ M_g that is bounded above, such that φ is non-constant on S ∩ M_g for every irreducible compact analytic surface S ⊂ U with S ⊄ ∂M̄_g and S ≠ closure(V_0). Then closure(V_t) = closure(V_0) for all t. In particular ∂V_t = ∂V_0 and Y_t = Y_0, which is the problem's claim.

*Proof.*
- **Small t.** closure(𝒱) is closed analytic in M̄_g × Δ by (R1), hence proper over Δ (M̄_g is compact). The argument of Step 1 of Prop. MP gives closure(V_t) ⊂ U for |t| < ε.
- **Each fibre.** closure(V_t) is irreducible, since V_t ≅ V_0 is connected and smooth, and it is a surface not contained in ∂M̄_g. Let n : S̃ → closure(V_t) be its normalisation, a compact connected normal surface.
  - ψ := φ∘n is psh on S̃ \ n^{-1}(∂M̄_g) and bounded above.
  - A psh function bounded above extends psh across a nowhere dense analytic subset of a normal space (Grauert–Remmert; cited from memory).
  - By the maximum principle on the compact connected normal space S̃, ψ is constant (or ≡ −∞).
  - By hypothesis, closure(V_t) = closure(V_0) for |t| < ε.
- **All t.** Apply Lemma CD in its surface version (round10_q9 §5, same proof with W replaced by closure(𝒱)): the set of t with closure(V_t) ⊂ closure(V_0) contains a disc, hence is Δ. Equality follows from irreducibility and equal dimension. ∎

**Assessment.**
- The hypothesis of MP′ forces closure(V_0) to be isolated among *all* compact surfaces in a neighbourhood. This is stronger than (Q2) of the earlier rounds (rigidity under *admissible* deformations).
- I know of no candidate φ. Krushkal's theorem (cited from memory: log tanh d_T(x_0, ·) is psh on T_g, being the pluricomplex Green function) gives psh functions on T_g that are not Mod_g-invariant. A minimum over Mod_g-translates, or over a disc, is not psh in general, and Kiselman's minimum principle needs convexity data I do not have.
- By the analogue of Prop. DP, such a φ cannot exist whenever closure(V_0) moves in a positive-dimensional family of compact surfaces in M̄_g. I did not decide whether known totally geodesic surfaces do. A candidate test case is the bielliptic locus in M_2, a covering-construction image and therefore totally geodesic, which is a divisor in M̄_2 (dim 3). It is psh-isolated only if it is not a moving divisor.

## 4. Task item 3: the weakest consequence, in a holomorphic form (Lemma HQ, proved)

**Lemma HQ (isolated boundary points move holomorphically).** Let G′ be a stratum and Q_0 an isolated point of A := closure(V_0) ∩ Δ_{G′}. Put Q_t := H_t(Q_0). Then t ↦ Q_t is a holomorphic map Δ → Δ_{G′} (into the coarse space; into ∏_w M_w when G′ is of product type). Consequently exactly one of the following holds:
- Q_t ≡ Q_0;
- for every point Q′, the set {t : Q_t = Q′} is closed and discrete.

So Q_t ≡ Q_0 as soon as Q_t lies in a countable set for uncountably many t.

*Proof.*
- **Σ is open in an analytic set.** 𝒜 := closure(𝒱) ∩ (Δ_{G′} × Δ) is a locally closed analytic set, by (R1). By (R2), H restricts to a homeomorphism A × Δ → 𝒜 over Δ. {Q_0} × Δ is open in A × Δ, because Q_0 is isolated in A. So Σ := H({Q_0} × Δ) is open in 𝒜, hence is itself a locally closed analytic set.
- **pr_Δ|_Σ is biholomorphic on the normalisation.**
  - Σ is homeomorphic to Δ via pr_Δ, so it is a pure 1-dimensional analytic set that is a topological 2-manifold.
  - Hence Σ is unibranch at every point, and its normalisation Σ̃ → Σ is a bijection.
  - pr_Δ : Σ̃ → Δ is a bijective holomorphic map of Riemann surfaces, hence biholomorphic.
  - Therefore t ↦ Q_t, the composite Δ → Σ̃ → Σ → Δ_{G′}, is holomorphic.
- **The dichotomy.** The identity theorem applied to the holomorphic map t ↦ Q_t. In the product case use the coordinates of ∏ M_w; in general, pull back local holomorphic functions on the coarse space. ∎

**Statement of the weakest consequence (Rig-0).** For every stratum G′ and every point Q_0 isolated in closure(V_0) ∩ Δ_{G′}, Q_t = Q_0 for all t.

Relation to the chain:
- The punctures of a piece E′ that are not interior points of another piece of their stratum are exactly the isolated points of their stratum's part of B_t.
- At such a puncture, (J1) and (J2) of round8_q7 Lemma J pin the Y_t-copy if (Rig-0) holds there. Indeed, the components of the constant stable curve Q_0 form a finite set, and the Y_t-copy component varies continuously in t (in the labelled chart of Q_0), so it is constant.
- So (Rig-0) can replace (Rig) / (Rig-w) in (J1) and (J2). It does not cover (J4), which concerns interior points of a 1-dimensional piece.
- By Lemma HQ, (Rig-0) at Q_0 is equivalent to "Q_t lies in a countable set for uncountably many t", for instance the set of stable curves defined over Q̄.

Status: Lemma HQ is proved. (Rig-0) itself is **not proved**. I have no global input that makes Q_t arithmetic or otherwise countable for t ≠ 0.

## 5. Final status

**Proved** (readings (R1), (R2); prior results W/Lemma R0, L1′, Lemma S″ and Lemma CD re-used, not re-proved; classical facts cited from memory as marked):
- **Prop. MP.** If the image curve K^M_0 has a neighbourhood carrying a bounded-above psh function that is non-constant on every other compact curve, then K^M_t = K^M_0 for all t. This gives (Rig-v) for M = {v}, and (Rig) and hence (Rig-w) for M = M(E_0). It needs no orbifold bookkeeping and does not see m_0 or type jumps.
- **Prop. MP′.** The same for closure(V_0) in M̄_g. Its hypothesis would prove the problem's claim outright.
- **Prop. DP.** For a vertex of type (0,5), every curve in M̄_{0,5} through the interior has C² ≥ 0 and moves in a pencil. So psh-isolation (Prop. MP) and negativity arguments cannot prove (Rig-v) there. Any proof must use the boundary constraint (c2) together with the global constraint (c1). This uses (F1)–(F3) from memory.
- **Lemma HQ.** Points of closure(V_0) isolated in their stratum move holomorphically under H_t. So (Rig-0), the weakest consequence covering junction types (J1) and (J2), is equivalent to countable-class membership for uncountably many t.

**Partial / conditional:**
- (Rig-v), (Rig) and the problem itself follow under the psh-isolation hypotheses of MP / MP′. Those hypotheses are **not verified** for any piece or any V_0, and by Prop. DP they fail for type-(0,5) Teichmüller vertices.

**Not proved / open:**
- (Rig), (Rig-w) and (Rig-v) for every admissible family: **not proved**. In particular, excluding m_0 > 1 and image-level type jumps (task point 1) is not achieved. Prop. MP would bypass them but its hypothesis is unavailable.
- Task point 2 (pinning the other non-constant vertices): no progress beyond Prop. MP with M = M(E_0).
- (Rig-0): open.
- (Q-DP): is a closed Teichmüller curve in M̄_{0,5} isolated among curves of its linear system with the same combinatorial boundary contact type? Also open: the transport of contact orders by H_t.
- Is closure(V_0) psh-isolated, or at least non-moving, among compact surfaces in M̄_g? This is a strengthening of Q2. The bielliptic locus in M̄_2 is a test case.
- Q1/Q2 of the earlier rounds remain open.

Overall: **not proved; open.**

=== END OF ANSWER round11_q10 ===
