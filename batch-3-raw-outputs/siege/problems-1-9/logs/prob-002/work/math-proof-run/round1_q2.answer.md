# round1_q2: upper bound n^{-2α/(2α+d+3)}: partial answer

## Status
- **Not proved:** I did not produce a rigorous proof of the upper bound n^{-2α/(2α+d+3)}.
- **Checked:** the planner's variance calculation (b) and the flux identity below, which gives an explicit route to an estimator.
- **Missing:** the obstructions are listed in Section 3.

**Working answer (conjectural):** n^{-2α/(2α+d+3)}, up to log factors.

## 1. Checking the heuristic variance computation (b)
The heuristic symbol is σ(ξ) = (1+|ξ_rad|)/|ξ|². Then

  ∫_{|ξ|≤2^J} σ^{-2} dξ = ∫ |ξ|⁴ (1+|ξ_rad|)^{-2} dξ ≤ 2^{4J} · (2^J)^{d-1} · ∫_R (1+t)^{-2} dt ≍ 2^{J(d+3)}.

The lower-order bound also holds, since the region where |ξ_ang| ≍ 2^J and |ξ_rad| ≤ 1 contributes ≍ 2^{J(d+3)}. So variance ≍ n^{-1}2^{J(d+3)} and bias² ≍ 2^{-2Jα}. Taking 2^J = n^{1/(2α+d+3)} gives the rate n^{-2α/(2α+d+3)}.

Near the source, the symbol becomes (1+ρ|ξ_rad|)/|ξ|². Then |ξ_rad| is effectively replaced by ρ|ξ_rad|, which costs a factor ρ^{-1} from the t-integral. Integrated against ρ^{d-1}dρ this stays finite for d ≥ 2, which confirms remark (b) at the heuristic level.

The computation is consistent with the lower bound (a): its angular perturbations sit exactly in the region |ξ_rad| ≲ 1, |ξ_ang| ≍ 2^J.

## 2. A concrete estimator route: the flux identity (exact, proved)
**Lemma.** Let V = ∇u_f. Let T_A be the union of the flow lines of V leaving the source x_f through a set A of initial directions. Let Ω_t = T_A ∩ {u_f < t}. Then

  ∫_{T_A ∩ {u_f = t}} f |∇u_f| dS = |Ω_t|.

**Proof.** Integrate div(f∇u) = 1 over Ω_t and use the divergence theorem.
- On the lateral boundary, ∇u is tangent, so ∂_ν u = 0.
- On the level set, ∂_ν u = |∇u|.
- The source point has measure zero, and its contribution vanishes because ∇u(x_f) = 0. ∎

Two consequences:
- Averages of f over patches of a level set are determined by u. The patches have angular width 2^{-J} and radial thickness O(1).
- Only first derivatives of u enter, through the flow geometry and |∇u|. They enter in averaged form, which is where the radial gain of one derivative should come from.

Estimator: plug a smoothed estimate û (resolution 2^J) into the identity at angular resolution 2^{-J}, then differentiate in t to recover pointwise-in-radius values.

The noise bookkeeping is not carried out here. At the heuristic level it reproduces the counting in Section 1:
- The angular localisation costs 2^{2J} relative to the volume (two angular derivatives through the inverse of L).
- The radial differentiation costs one derivative, matching the factor (1+|ξ_rad|).

## 3. Steps not established (open)
1. **Stochastic control of the flow geometry.** The flow lines of ∇û differ from those of ∇u_f by an amount that integrates ∇(û − u). Controlling the lateral flux error at angular scale 2^{-J} needs a uniform (sup-norm) bound on ∇(û − u) at resolution 2^J. That bound must be good to order 2^{-J(α+1)} relative to the patch size, and I have not shown that the white-noise suprema achieve it without losing more than log factors.
2. **Rigorous anisotropic stability.** The estimate ‖h‖_{L²} ≲ ‖L_f^{-1}div(hV_f)‖_Y has to hold with Y using two angular derivatives and one radial derivative, with weights near the source and uniformly over f ∈ F(α,r). This is a variable-coefficient microlocal statement. The only natural tool is a parametrix for the transport-plus-elliptic composition, and I have not carried it out. The boundary also needs treatment: there V·ν ≈ 1/d ≠ 0, so the flow is transversal to ∂D, which should be harmless.
3. **Nonlinear remainder.** The remainder is ‖u_g − u_f − Dh‖ ≲ ‖h‖_{C^1}‖h‖_{L^2}-type. It needs a pilot estimator consistent in C^1 at a polynomial rate. Such pilots exist (from memory: Nickl, van de Geer & Wang 2020 give polynomial C^1-type rates for Darcy-type problems by stability plus interpolation), so this step is likely routine, but I have not verified it.

## Conclusion
- **Best rate I can claim rigorously here:** none beyond what the literature already gives. I have not reproved any polynomial upper bound in this file.
- **Conjectured minimax rate:** n^{-2α/(2α+d+3)}, up to log factors. This matches the lower-bound heuristic (a) and the variance computation in Section 1.
- **Open:** items 1–3 of Section 3.

=== END OF ANSWER round1_q2 ===
