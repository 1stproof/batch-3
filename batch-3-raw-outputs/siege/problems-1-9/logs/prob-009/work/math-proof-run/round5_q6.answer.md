# Answer to round5_q6 (MS4)

**Summary of outcome.** MS4 is neither proved nor disproved here. What is established:

1. (§1) The reduction "MS4 + holomorphy ⇒ problem" is checked, with one precise caveat about the readings: (R2) is *stronger* than the literal hypotheses (i),(ii). So MS4 implies the problem's claim only for families that satisfy (R2). Holomorphy, on the other hand, follows from (R1) alone; a proof is given.
2. (§2) **New first move: global forgetful fibrations.** I build an explicit family (Proposition A) that satisfies *every* hypothesis of the problem/MS4 (smooth triviality, (i), (ii) read literally, (R1), (R2), dim ∂V_t = 1, constancy on one factor of a product stratum). In this family Y_t is a **nonconstant** holomorphic arc. The only hypothesis that fails is that V_0 is totally geodesic (and the ambient space is M_{0,7} rather than M_g; a transfer to M_g is only sketched). Consequence, which is proved: no argument that uses only (i), (ii), (R1), (R2), the boundary dimension count and holomorphy can prove MS4. Any proof has to use the total geodesicity of V_0 in an essential, global way. In effect it must be a rigidity theorem for closures of totally geodesic surfaces. This sharpens the earlier observation that "no local argument works".
3. (§3) A toy positive result (Proposition B). For an explicit totally geodesic surface V_0 ⊂ M_{0,11} (a Z/3 covering locus) whose constant boundary factor Y_0 lies in a positive-dimensional moduli space M_{0,5}, Y_t is forced to be constant for every deformation through *affine-linear planes* in the standard chart. The rigidity comes from the combinatorics of collisions, which (i) preserves. This is evidence for MS4, not a proof.
4. (§4) An exact reformulation of what is left open, and the open questions.

---

## §1. The reduction, and the readings (R1)/(R2)

**1.1 MS4 + holomorphy ⇒ the problem's conclusion.** MS4 says t ↦ Y_t is constant on Δ, and 0 ∈ Δ. So Y_t = Y_0 for all t, i.e. π_i(∂V_t) = {Y_0}. That is literally the problem's conclusion. Holomorphy is not even needed for this step, because MS4 already asserts constancy. Holomorphy is the natural first step towards proving MS4.

**1.2 Do the problem's hypotheses give (R1), (R2)?**

* (R1) (the closure of 𝒱 in M̄_g × Δ is analytic with fibres closure(V_t)) is not stated literally. It is the natural reading of "holomorphic family of subvarieties", and I accept it.
* (R2) asks for a *single* homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ that respects *all* strata simultaneously. Hypothesis (i) only gives, for each stratum G separately, a smooth trivialisation of the family closure(V_t) ∩ Δ_G. Hypothesis (ii) only transports the incidence relations "the boundary of V_0 in a smaller stratum arises from its boundary in a larger stratum". Gluing the separate trivialisations into one stratum-preserving homeomorphism is an extra assumption: a Thom–Mather-type local triviality. **So (R2) strengthens the hypotheses.**

  Consequently, a proof of MS4 settles the problem only for families that satisfy (R2). A counterexample to MS4 automatically satisfies (R2), so it would also be a counterexample to the problem.
* Remark on (ii) as literally stated: the open set U is fixed and does not move with t. If some set closure(V_t) ∩ Δ_{G'} had several pieces, some in the closure of the G-stratum and some not, then a fixed U could separate them at t = 0 but not at a later t. The natural reading transports U along the trivialisation. In the example of §2 this issue does not arise: every relevant intersection is either a single point or a single connected stratum piece with its own labelled dual graph.

**1.3 Holomorphy from (R1) alone (proof).** Let Z = closure(𝒱) ∩ (closure(Δ_Γ) × Δ), an analytic set that is proper over Δ. The projection π_i extends to the closure of Δ_Γ (via the normalisation of closure(Δ_Γ), which is the product of the M̄_{g_j,n_j}), giving a proper holomorphic map Π = π̄_i × id : Z̃ → M̄_{g_i,n_i} × Δ.

By Remmert's proper mapping theorem, Π(Z̃) is analytic. Consider a point of Z̃ that lies over a deeper stratum but whose i-th factor is still smooth. Its i-th factor is a limit of points with i-th factor Y_t, so it equals Y_t. Hence Π(Z̃) ∩ (M_{g_i,n_i} × Δ) is the graph G_Y = {(Y_t, t)}, which is closed and analytic of pure dimension 1.

Let ν: G̃ → G_Y be the normalisation (a Riemann surface). The map pr_Δ ∘ ν is holomorphic. It is injective off the finitely many non-normal points over each compact set, and since G_Y is a graph it is in fact bijective onto Δ. A bijective holomorphic map between Riemann surfaces is biholomorphic. Hence t ↦ Y_t = pr_1 ∘ ν ∘ (pr_Δ ∘ ν)^{-1}(t) is holomorphic. ∎

(Neither (R2) nor total geodesicity is used.)

---

## §2. New first move: forgetful fibrations. The hypotheses other than total geodesicity do not force constancy

### Proposition A
Let f : M̄_{0,7} → M̄_{0,5} forget the markings 6 and 7. Let y : Δ → M_{0,5} be a nonconstant holomorphic disc with small image, e.g. y(t) = (0, 1, ∞, λ_0 + εt, μ_0). Put V_t := f^{-1}(y(t)) ∩ M_{0,7}, a 2-dimensional smooth closed subvariety of M_{0,7}. Let Γ be the dual graph with two vertices: v' carries the labels {1,6,7} and v'' carries {2,3,4,5}, joined by one edge. Then Δ_Γ ≅ M_{0,4} × M_{0,5} is a product with no finite quotient, since the labels are distinct. The following hold:

(a) 𝒱 = {(C,t) : f(C) = y(t)} ⊂ M_{0,7} × Δ is a complex submanifold, and its closure {(C,t) ∈ M̄_{0,7} × Δ : f(C) = y(t)} is analytic. So (R1) holds.
(b) The family is smoothly trivial, and (R2), (i) and (ii) hold, with (ii) holding even in its literal fixed-U form.
(c) dim ∂V_t = 1. Moreover ∂V_t = M_{0,4} × {y(t)'}, where y(t)' ∈ M_{0,5} is y(t) with label 1 renamed as the node. So π_2(∂V_t) = {Y_t} with Y_t = y(t)', and **Y_t is not constant.**

So every hypothesis of the problem holds except the total geodesicity of V_0 (and M_{0,7} replaces M_g).

### Proof
*Fibre description (standard, quoted from memory).* For y = (P^1; p_1,…,p_5) ∈ M_{0,5}, the fibre X_y := f^{-1}(y) ⊂ M̄_{0,7} is isomorphic to the blow-up of P^1 × P^1 (coordinates x_6, x_7) at the five points (p_i, p_i). The reason: M̄_{0,7} → M̄_{0,6} is the universal curve. Over the fibre P^1 of M̄_{0,6} → M̄_{0,5} above y (the position x_6), the curve is P^1 itself, except above x_6 = p_i, where it is P^1 ∪ (a bubble carrying i, 6).

X_y is irreducible and smooth, and its open part V_y is dense, so closure(V_y) = X_y. Its boundary consists of the following pieces:
* the strict transforms D_{i6} of {x_6 = p_i}, D_{i7} of {x_7 = p_i}, and D_{67} of the diagonal;
* the exceptional curves E_i.

The lines x_6 = p_i, x_7 = p_i and the diagonal pass through (p_i, p_i) with three distinct tangent directions. So E_i meets them at three distinct points, and E_i° := E_i minus those points ≅ M_{0,4}. On E_i° the stable curve consists of a bubble with markings {i,6,7} and a node, whose cross-ratio is the coordinate on E_i°, attached to the main component (P^1; p_j (j ≠ i), node at p_i). Taking i = 1 gives (c): X_y ∩ Δ_Γ = E_1° × {y'}.

The 0-dimensional strata of X_y are the points (p_i, p_j) for i ≠ j, and the three points on each E_i. (D_{i6} is disjoint from D_{i7}, from D_{67} and from D_{j6}, because the only common points of the original curves were the blown-up points or there were none.) Each 1- or 0-dimensional stratum of X_y has its own *labelled* dual graph. So for every G, X_y ∩ Δ_G is either empty, a single point, or a single connected curve E_i°, D_{ij}°.

*Trivialisation.* For |t| ≤ 1, choose diffeomorphisms φ_t of P^1, smooth in (t, z), with φ_0 = id and φ_t(p_i(0)) = p_i(t), and such that φ_t is the translation z ↦ z + p_i(t) − p_i(0) in a fixed chart near each p_i(0). This is possible because the image of y is small, so the points move only slightly. Then Φ_t = φ_t × φ_t maps (p_i(0), p_i(0)) to (p_i(t), p_i(t)) and is holomorphic near these points. Hence it lifts to a diffeomorphism X̃_t : X_{y(0)} → X_{y(t)} of the blow-ups (acting on each E_i through its derivative, which is a translation, so it is the "identity" on the projectivised tangent spaces).

Φ_t maps {x_6 = p_i(0)} to {x_6 = p_i(t)}, and similarly for x_7, and it preserves the diagonal. Therefore X̃_t maps each stratum piece (D_{i6}, D_{i7}, D_{67}, E_i, the points) onto the piece with the same labelled graph. This gives (R2) and smooth triviality, and (i) follows.

For (ii): since each X_t ∩ Δ_{G'} is empty, a point, or one connected piece, and X̃_t preserves closures, the truth value of "closure(X_t ∩ Δ_G) ∩ Δ_{G'} = X_t ∩ Δ_{G'}" is the same for all t, globally. Hence it is the same on any U as well. ∎

**Consequence (proved).** Any proof of MS4 must use that V_0 is totally geodesic, and not only "at the boundary". Proposition A satisfies every structural hypothesis, the boundary dimension count, holomorphy and product-stratum constancy, and still lets Y_t move freely. Together with the recorded fact that every local constraint is compatible with any arc Y_t, this shows that MS4 is equivalent to a **global rigidity property of closure(V_0)**; see §4.

**Remarks.**
* Whether some fibre X_{y_0} ∩ M_{0,7} is itself totally geodesic in M_{0,7} I could not decide. If it were, Proposition A would be an honest counterexample in M_{0,7}. I expect it is not: a Teichmüller disc tangent to a "vertical" direction should change the cross-ratios of p_1,…,p_5. Not proved.
* *Transfer to M_g (sketch only).* The same phenomenon occurs inside some M_g. Take double covers of a fixed pointed curve (C, q_1, q_2) of genus h, branched over {q_1, q_2, x, y}, with (x, y) varying; this gives a surface in M_{2h+1}. When x, y → q_1, the boundary lies in the product stratum M_{2h,1} × M_{1,1}. The M_{2h,1}-factor (the double cover of C branched at q_2 and at the node point over q_1) is constant, and it moves when (C, q_1, q_2) moves. Smoothness of the image surface and the conditions (i)/(ii) were not checked in detail.

---

## §3. Toy positive result: rigidity for affine-linear deformations of a Z/3 covering locus

Setting. In M_{0,11} take the labels 0, ∞, a_k, b_k, c_k (k = 0, 1, 2), and let

V_0 = {(P^1; 0, ∞, aω^k, bω^k, cω^k)}, with ω = e^{2πi/3}.

V_0 is the image of the covering construction z ↦ z^3 over M_{0,5}(0, ∞, A, B, C). By the standard lifting of integrable quadratic differentials (quoted from memory), Teich_{0,5} embeds isometrically and totally geodesically, so V_0 is totally geodesic. V_0 is also the fixed locus of the order-3 relabelling a_k ↦ a_{k+1} (and likewise for b_k, c_k), hence smooth.

Let b, c → ∞ with a fixed. Then ∂V_0 lies in a product stratum M_{0,5} × M_{0,8}. The component (0, a_0, a_1, a_2, node) is constant, equal to the configuration (0, 1, ω, ω², ∞), and the other component varies with b/c. So Y_0 is a point of the positive-dimensional space M_{0,5}.

**Proposition B.** Use the affine chart that normalises 0, ∞, a_0 to 0, ∞, 1, so that V_0 is the plane P_0 = {x_{a_1} = ω, x_{a_2} = ω², x_{b_k} = ω^k b, x_{c_k} = ω^k c}. Let P_t be a family of affine planes (with V_t = P_t ∩ M_{0,11}) satisfying (i). Then x_{a_1}, x_{a_2} are constant in t, and therefore Y_t = Y_0.

*Proof.*
* Constancy of x_{a_1}, x_{a_2} on P_t: if x_{a_1} were a nonconstant affine function on P_t, the collision x_{a_1} = x_{a_0} = 1 would create a 1-dimensional boundary piece whose collision type does not occur for V_0. That contradicts (i). Write α(t) := x_{a_1}, β(t) := x_{a_2}, and ℓ_k := x_{b_k}|_{P_t}.
* The line {b = 0} of P_0 carries the stratum where all three b_k collide with 0 simultaneously. By (i), P_t contains a line on which all ℓ_k vanish, so ℓ_k = λ_k L for a common affine function L. Normalise λ_0 = 1.
* The line {b = 1} carries the simultaneous collisions b_0 = a_0, b_1 = a_1, b_2 = a_2. Its persistence gives λ_1 = α and λ_2 = β.
* The line {b = ω} carries b_0 = a_1, b_1 = a_2, b_2 = a_0. On L = α this gives α·α = β and β·α = 1.
* Hence α^3 = 1 with α ≠ 1, and β = α². So α(t) lies in the discrete set {ω, ω²}, and by continuity α ≡ ω. Then Y_t, the configuration (0, 1, α, β, ∞), equals Y_0. ∎

This shows the mechanism one would hope drives MS4: the collision pattern preserved by (i) encodes the symmetry of V_0. But it only holds for linear deformations, and general holomorphic V_t can be nonlinear. It is evidence, not a proof.

---

## §4. What remains open

**Reformulation (immediate from the definitions together with §1.3).** Fix V_0, Γ and i. MS4 holds for V_0 if and only if the holomorphic function Y, defined on the germ at [closure(V_0)] of the space of (R2)-type equisingular deformations of closure(V_0) in M̄_g, is constant on every holomorphic disc through [closure(V_0)].

* Checking first order is not enough: a family with Y_t = Y_0 + c t² + … has dY(0) = 0.
* One cannot "recentre" at t_0 ≠ 0, because V_{t_0} is not totally geodesic.

In particular, MS4 would follow from **equisingular rigidity of closures of totally geodesic surfaces**, i.e. that closure(V_0) admits no nontrivial (R2)-deformations. This would be the analogue of Möller's rigidity of Teichmüller curves, which I quote from memory. By Proposition A, the hypotheses (i), (ii), (R1), (R2) cannot replace this in general.

**Open questions.**
1. Is MS4 true? Equivalently: is Y constant on the equisingular deformation space of closure(V_0) for every 2-dimensional totally geodesic V_0 ⊂ M_g?
2. (Would make Proposition A a genuine counterexample.) Is any fibre of a forgetful map M_{0,n+2} → M_{0,n}, or of a covering-construction analogue in M_g, totally geodesic?
3. Does Proposition B extend from affine-linear planes to arbitrary holomorphic deformations of the Z/3 covering locus? For instance, via logarithmic normal-bundle cohomology H^0(N'_{S/M̄}) of S = closure(V_0), where N' = T_{M̄}(−log ∂)|_S / T_S(−log ∂S).
4. Do the problem's literal hypotheses (i), (ii) imply (R2)?

=== END OF ANSWER round5_q6 ===
