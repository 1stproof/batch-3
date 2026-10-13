# round12_q5: answer

## 0. Summary of the outcome
(PE0) is NOT proved here. The planner's approach fails at step (3), and the failure has a proof (an obstruction).

**Obstruction (proved; GH is not used anywhere in it).** For every smooth flow and every g_1-ergodic mu, for mu-a.e. z:
- (O1) no nonzero distribution supported at {z} has two-sided exponentially decaying transport;
- (O2) hence any weak* limit of configurations S_n shrinking to z, with uniform two-sided decay on growing time windows, is 0;
- (O3) quantitatively, the decay constants C_n must satisfy C_n / ||S_n||_{(C^{k+1})'} -> infinity, whatever normalisation is used.

So difficulty (b) of the brief has a negative answer: the normalised limit is always zero, or the constants blow up. Theorem J (or J*) is never reached. GH cannot rescue the step, because the obstruction holds for all flows. For a GH flow, Theorem J gives the same conclusion S = 0 at every point.

What survives:
- (G) At FIXED scale, approximate grids whose defects tend to 0 converge to EXACT su-grids, and the decay bounds pass to the limit. So approximation adds nothing: this route to (PE0) is equivalent to producing exact su-structures, which is a joint-integrability property that is generically false.
- (Cl) (proved) Forward exponential decay of a finite Dirac configuration at points with J_t = o(t) forces exponential forward clustering of its points. This is why defects that the centre dynamics separates only subexponentially cannot be tolerated without a limit.
- An anisotropic variant (shrink only the stable scale) escapes (O2). It runs into the regularity of the stable foliation along unstable leaves; this is only sketched (Section 6).

Notation throughout:
- nu is a smooth positive density, d = div_nu X, and J_t(x) = int_0^t d(g_s x) ds.
- Gamma_t phi := e^{J_t} (phi o g_t). Gamma_{t+s} = Gamma_s Gamma_t, since e^{J_s(x)} e^{J_t(g_s x)} = e^{J_{t+s}(x)}.
- For a distribution density S: F^S_phi(t) := S(Gamma_t phi), and N^k_S(t) := sup{ |F^S_phi(t)| : ||phi||_{C^k} <= 1 }.
- S is "in (C^k)'" if |S(phi)| <= C ||phi||_{C^k}.
- "Two-sided decay at rate eps, order k, constant C on the window |t| <= T" means |F^S_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for |t| <= T.

## 1. Lemma O1: point-supported distributions never decay on both sides (at Oseledets-regular points)

**Setting.** Fix k >= 0. Let J^k_w be the space of k-jets at w of smooth functions, i.e. C^inf(M) modulo the functions vanishing to order k+1 at w. The J^k_w form a smooth vector bundle J^k over M. Fix a continuous family of norms |.|_w on the fibres; with finitely many charts, use the sup of the Taylor coefficients.

Gamma_t maps functions vanishing to order k+1 at g_t z to functions vanishing to order k+1 at z, because g_t is a diffeomorphism and e^{J_t} is smooth and positive. So it induces a linear isomorphism
A_t(z) : J^k_{g_t z} -> J^k_z.
This isomorphism is continuous in (t, z), being given by the k-jets of g_t and of e^{J_t} at z. From Gamma_{t+s} = Gamma_s Gamma_t we get A_{t+s}(z) = A_s(z) A_t(g_s z).

Put B_t(z) := A_t(z)^* : (J^k_z)^* -> (J^k_{g_t z})^*. Then B_{t+s}(z) = B_t(g_s z) B_s(z), so B is a continuous linear cocycle over the flow on the finite-dimensional bundle E := (J^k)^*.

**Fact 1 (jets of the C^k unit ball).** There are constants 0 < c <= C such that for every w in M and every v in (J^k_w)^*:
c |v| <= sup{ |<v, j^k_w phi>| : ||phi||_{C^k} <= 1 } <= C |v|.
*Proof.*
- Upper bound: |j^k_w phi| <= C ||phi||_{C^k}.
- Lower bound: every jet xi at w with |xi| <= 1 is j^k_w phi for some phi with ||phi||_{C^k} <= C'. Take the Taylor polynomial of xi in a chart around w, times a fixed cutoff. The charts and cutoffs come from a finite atlas with a Lebesgue number, so C' does not depend on w. ∎

**Fact 2 (point support of order k).** If S is in (C^k)' and supp S ⊂ {z}, then S = l o j^k_z for a unique linear functional l on J^k_z, and S != 0 iff l != 0.
*Proof.* Let psi in C^k(M) have j^k_z psi = 0. Fix a cutoff chi equal to 1 near 0, put chi_eta(x) := chi(x/eta) in a chart centred at z, and write psi = psi chi_eta + psi (1 - chi_eta).
- S(psi (1 - chi_eta)) = 0, because this function vanishes near z.
- By Taylor's formula, d^alpha psi(x) = o(|x|^{k-|alpha|}) for |alpha| <= k.
- So every term d^{alpha-beta} psi · eta^{-|beta|} (d^beta chi)(x/eta) of d^alpha(psi chi_eta) is o(eta^{k-|alpha|}) on |x| <= C eta. Hence psi chi_eta -> 0 in C^k, and S(psi) = lim S(psi chi_eta) = 0. ∎

**Lemma O1.** Let X be any smooth vector field (GH is not assumed) and mu any g_1-invariant ergodic Borel probability. Then there is a set R of full mu-measure with the following property. For z in R, k >= 0, eps > 0 and C < inf, the only distribution density S in (C^k)' with supp S ⊂ {z} and
|F^S_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and all smooth phi
is S = 0.

*Proof.*
1. By Fact 2, S = l o j^k_z. Then F^S_phi(t) = l(A_t(z) j^k_{g_t z} phi) = <B_t(z) l, j^k_{g_t z} phi>.
2. By Fact 1 at w = g_t z, N^k_S(t) is between c |B_t(z) l| and C |B_t(z) l|. So the hypothesis gives |B_t(z) l| <= (C/c) e^{-eps|t|} for all real t.
3. Apply Oseledets' theorem (invertible version, cited from memory) to the cocycle B_n(z), n in Z, over the invertible ergodic system (g_1, mu). The generator B_1 is continuous, so log^+ ||B_1^{±1}|| is bounded.
4. For k fixed, there is a full-measure set R_k on which E_z = ⊕_i E_i(z), with exponents chi_1 > ... > chi_p and lim_{n -> ±inf} (1/n) log |B_n(z) v| = chi_i for v in E_i(z) \ 0.
5. Consequently:
   - V^-(z) := { v : limsup_{n -> +inf} (1/n) log |B_n v| < 0 } = ⊕_{chi_i < 0} E_i(z);
   - V^+(z) := { v : limsup_{n -> +inf} (1/n) log |B_{-n} v| < 0 } = ⊕_{chi_i > 0} E_i(z);
   - V^-(z) ∩ V^+(z) = {0}.
6. Step 2 gives l in V^-(z) ∩ V^+(z), so l = 0 and S = 0.
7. Put R := ∩_k R_k, which still has full measure. ∎

*Remarks.*
(i) Only integer times are used, so continuous-time regularity is not needed.
(ii) The lemma is false at non-generic points. For the north–south flow, delta_y on a source-to-sink orbit decays on both sides (Remark (iii) after Theorem J). So Lemma O1 really uses regularity of z for the jet cocycle. Under GH, Theorem J gives the conclusion at EVERY z, but that is useless here, as explained in §3.
(iii) Heuristically: in normal-form coordinates, d_u^a d_s^b delta_z behaves forward like e^{(a chi^u - b|chi^s|) t} and backward like e^{-(a chi^u - b|chi^s|)|t|}. One sign is always >= 0, and centre derivatives contribute only e^{o(|t|)}.

## 2. Lemma O2 and Corollary O3: shrinking configurations

**Lemma O2 (limits are zero).** Let X, mu and R be as in Lemma O1, and let z be in R. Fix k >= 0, eps > 0 and C. Let S_n be distribution densities in (C^k)' such that:
- ||S_n||_{(C^k)'} <= A;
- supp S_n ⊂ B(z_n, r_n), with z_n -> z and r_n -> 0;
- |F^{S_n}_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for |t| <= T_n, with T_n -> inf.

If S_n -> S weak* in (C^k)', then S = 0.

*Proof.*
1. *Support.* If psi in C^k vanishes on a neighbourhood U of z, then U contains B(z_n, r_n) together with a neighbourhood of it for n large. So S_n(psi) = 0 for large n, and S(psi) = 0. Hence supp S ⊂ {z}, and S is in (C^k)' with norm <= A.
2. *Decay passes to the limit.* For fixed t and smooth phi, Gamma_t phi is smooth, so F^S_phi(t) = lim_n F^{S_n}_phi(t). For large n we have |t| <= T_n, so |F^S_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for every real t.
3. Lemma O1 gives S = 0. ∎

(Weak* limits exist along subsequences: C^k(M) is separable, so bounded sets of (C^k)' are weak* sequentially compact.)

**Corollary O3 (blow-up of the normalised constants).** Let z be in R and k >= 0. Let S_n != 0 be distribution densities supported in B(z_n, r_n), with z_n -> z and r_n -> 0. Suppose there are eps > 0, windows T_n -> inf and constants C_n with
|F^{S_n}_phi(t)| <= C_n e^{-eps|t|} ||phi||_{C^k} for |t| <= T_n.
Then C_n / ||S_n||_{(C^{k+1})'} -> inf. Since ||.||_{(C^{k+j})'} <= ||.||_{(C^{k+1})'} for j >= 1, the same holds with any j >= 1 in place of 1.

*Proof.*
1. Suppose not. Pass to a subsequence with C_n <= A ||S_n||_{(C^{k+1})'}, and rescale so that ||S_n||_{(C^{k+1})'} = 1. Then C_n <= A.
2. At t = 0 the hypothesis gives ||S_n||_{(C^k)'} <= C_n <= A.
3. *Compactness.* The inclusion C^{k+1}(M) -> C^k(M) is compact (Arzelà–Ascoli). By Schauder's theorem its adjoint (C^k)' -> (C^{k+1})' is compact. So a subsequence converges in the norm of (C^{k+1})' to some S'. A further subsequence converges weak* in (C^k)' to some S.
4. S and S' agree on C^{k+1}, which is dense in C^k. Hence S' extends to S, and ||S||_{(C^{k+1})'} = lim ||S_n||_{(C^{k+1})'} = 1. So S != 0.
5. But Lemma O2 applies, with constant A in place of C, and gives S = 0. Contradiction. ∎

## 3. Consequences for the planner's approach (steps (2)–(3))

**(3) is dead, whatever happens in (2).** The configurations S_r of the brief are finite Dirac combinations. They are supported in a ball of radius O(r) around the base point z_1. The base point can be, and must be, taken mu-generic, so we may take it in R and fixed; or z_1(r) -> z in R along a subsequence.

The brief's normalisation is sup_{|t| <= 1} N^k_{S_r}(t) = 1. This norm is equivalent to ||S_r||_{(C^k)'}, because Gamma_t is bounded on C^k with bounded inverse, uniformly for |t| <= 1. Under that normalisation:
- (a) if the decay constants are uniform, so that |F^{S_r}_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} on |t| <= T(r) with T(r) -> inf, then every weak* limit is 0 by Lemma O2;
- (b) whatever normalisation is chosen, Corollary O3 says the decay constant measured against ||S_r||_{(C^{k+1})'} tends to infinity.

So the brief's step "show S != 0" is impossible in every smooth flow, for every mu, at mu-a.e. base point. The test functions that see S_r at order one oscillate at scale r and leave every compact subset of C^k. Mass escapes to infinite frequency, and the weak* limit loses it.

**Why GH cannot help.**
- Everything in steps (1)–(3) before the appeal to Theorem J is GH-free: Pesin theory, normal forms, moment conditions, compactness.
- Lemmas O1 to O3 are GH-free too.
- Under GH, Theorem J would also give S = 0, for any z.
So a contradiction can never come out of step (3).

**The quasi-analytic variant (Theorem J*).** Lemma O1 as proved needs exponential decay at a positive rate. Suppose the decay is only quasi-analytic, for instance e^{-|t|/log|t|}. The Oseledets argument then gives limsup (1/n) log |B_{±n} l| <= 0, so l has no component in any E_i with chi_i != 0: l lies in E_0(z), the zero-exponent Oseledets space of the jet cocycle. E_0(z) is nonzero, since it contains the centre-derivative jets. **So with J* the obstruction is proved only for limits whose E_0-component vanishes. Whether a nonzero l in E_0(z) can have quasi-analytically decaying transport in both directions is left open (a GH-free question about the subexponential behaviour of a cocycle on its zero-exponent subspace).** For the configurations of the brief I see no mechanism that would produce such sub-exponential decay inside E_0. The planner's own estimates give at best e^{-eps|t|} up to defect errors, and these are covered by O3.

**Difficulty (c) (Jacobian weights).** This is irrelevant to the obstruction. In O1 the weight e^{J_t} is built into the cocycle A_t, and O1 to O3 hold for any nu.

**Difficulty (a) (defects versus moments).** This is moot for the limit procedure, by O3. At fixed scale, see Section 4.

## 4. What approximation can and cannot do: a finite-window Theorem J, and fixed-scale limits

**Proposition W (finite-window form of Theorem J; proved, uses GH only through Theorem J).** Assume GH. Fix k >= 0, eps > 0 and A. Then there is T* = T*(k, eps, A) < inf with the following property. If S is in (C^k)' and
|F^S_phi(t)| <= A ||S||_{(C^{k+1})'} e^{-eps|t|} ||phi||_{C^k} for all |t| <= T* and all smooth phi,
then S = 0.

*Proof.*
1. Suppose not. Then there are S_n != 0 and T_n -> inf with the bound on |t| <= T_n. Normalise ||S_n||_{(C^{k+1})'} = 1.
2. At t = 0 we get ||S_n||_{(C^k)'} <= A.
3. Exactly as in Corollary O3 (Schauder compactness of (C^k)' -> (C^{k+1})', and density of C^{k+1} in C^k), a subsequence converges in (C^{k+1})' to some S with ||S||_{(C^{k+1})'} = 1 and S in (C^k)'. The bound passes to the limit for every t.
4. Theorem J gives S = 0. Contradiction. ∎

*Meaning.*
- Every approximate version of the planner's construction must deliver configurations S_n with decay at a FIXED rate eps and order k, constants bounded by A ||S_n||_{(C^{k+1})'}, and windows T_n -> inf. Such a family is exactly what would contradict GH, by Proposition W.
- More to the point, by compactness any such family converges in (C^{k+1})' to an EXACT nonzero two-sided decaying distribution. The same proof without the last step shows this for every smooth flow.
- So approximation adds nothing: the task is always to produce, from mu, an exact nonzero S with two-sided decay.
- By Corollary O3, such S_n cannot concentrate at an Oseledets-regular point. Their (C^{k+1})'-mass must stay spread over a set that does not shrink to a regular point.

**Lemma G (fixed-scale approximate grids converge to exact grids; proved modulo the cited continuity of local manifolds on Pesin blocks).**
*Cited (Pesin theory, from memory).* For a Pesin block Lambda (compact, mu(Lambda) > 0) of g_1 and mu, there is rho > 0 such that the local unstable and local stable manifolds W^u_rho(z) and W^s_rho(z), z in Lambda, are embedded closed C^1 discs depending continuously on z in Lambda in the C^1 topology.

*Statement.* For each n, let y^n_{j,i} (1 <= i, j <= K) be points of Lambda such that:
- y^n_{j,i} is in W^u_rho(y^n_{j,1});
- dist(y^n_{j,i}, W^s_rho(y^n_{1,i})) <= delta_n, with delta_n -> 0;
- the pairwise distances are >= sigma > 0.
Then a subsequence converges to an exact su-grid in Lambda: y_{j,i} is in W^u_rho(y_{j,1}) ∩ W^s_rho(y_{1,i}), with pairwise distances >= sigma.

*Proof.* Lambda is compact, so pass to a subsequence along which all K^2 points converge. The set {(z, w) : z in Lambda, w in W^{u/s}_rho(z)} is closed, by continuity of the discs on Lambda. The defect conditions pass to the limit. ∎

So at fixed scale the brief's approximate grids yield exactly what exact grids yield. The configurations converge too, at least after normalising in (C^{k+1})' as in Proposition W: their limit is a distribution supported on the limit grid. (I have not checked whether the normalised weights stay bounded, which would make the limit again a Dirac combination.) By Proposition W, a fixed-scale family with defects -> 0 and uniform constants would give an exact grid configuration with two-sided decay. Exact grids in turn are what the R11-e §3.1 computation needs; I have not re-verified that computation, and Proposition W does not need it.

**The question left by the approach** (precise; open):
> (EG) Does the hypothetical mu of (PE0) admit, in some Pesin block, exact su-grids of size K x K with pairwise separation >= sigma > 0 and all vertices in Lambda ∩ (generic set), for K >= K_0(N)?
>
> Here K_0(N) > D_u(N) + D_s(N), the number of row and column moment conditions per line. This bound is needed by the counting in the brief: K^2 unknowns against K(D_u + D_s) conditions.

Why (EG) is not available in general:
- Fix the first row (K - 1 free points on a u-disc) and the first column (K - 1 free points on an s-disc). Then each remaining vertex must lie on W^s_rho(y_{1,i}) ∩ W^u_rho(y_{j,1}). This intersection is generically empty when there is a centre direction: dim s + dim u = n - c < n, and closing the quadrilateral is a codimension-c condition.
- So there are (K-1)^2 conditions of codimension c each, against (K-1)(u + s) parameters, and K - 1 <= (u+s)/c is forced for a generic system. This is incompatible with K >= K_0(N) once N is large, unless the su-structure is jointly integrable on a large set.
- Moreover the vertices must be mu-generic, which in addition needs positive conditional mass near the grid.
- This is only a heuristic dimension count. Joint integrability does occur in some systems, for example a product of an Anosov diffeomorphism with a rotation, and in such cases exact grids exist. Whether GH can force or forbid it is exactly the open point.

## 5. Lemma Cl: one-sided decay of a Dirac configuration forces exponential clustering (proved, no GH)

**Lemma Cl.** Let S = sum_{i=1}^n w_i delta_{y_i}, with distinct points y_i and all w_i != 0. Let k >= 1 and 0 <= eps' < eps. Suppose that for t >= 0:
- |F^S_phi(t)| <= C e^{-eps t} ||phi||_{C^k};
- J_t(y_i) >= -eps' t - C' for every i.

Put eta := (eps - eps')/(2k). Then there is t_0 such that for every t >= t_0 and every i there is j != i with d(g_t y_i, g_t y_j) <= e^{-eta t}.

*Proof.*
1. Suppose that for some t and i every other point g_t y_j is at distance > rho := e^{-eta t} from g_t y_i.
2. Let phi be a bump at g_t y_i of radius rho/2 in a chart, with phi(g_t y_i) = 1 and ||phi||_{C^k} <= C_b rho^{-k}, where C_b is uniform over the finite atlas. No other g_t y_j lies in its support.
3. Then F^S_phi(t) = w_i e^{J_t(y_i)}. So |w_i| e^{-eps' t - C'} <= C C_b e^{-eps t + k eta t} = C C_b e^{-(eps + eps') t / 2}.
4. Since -(eps + eps')/2 < -eps', this fails for t >= t_0(i). Take t_0 := max_i t_0(i). ∎

*Use.* At mu-generic points with mu(d) = 0 we have J_t(y) = o(t), so every eps' > 0 is admissible. Forward decay at any positive rate therefore forces every point of the configuration to be exponentially shadowed, at all large times, by another point of the configuration; the time-reversed statement holds for backward decay.

For the brief's approximate grids this has a direct consequence. Two points of a column that differ by a centre defect delta_0 separate or approach only subexponentially. So the decay at rate eps can hold only up to a time T = O(log(1/delta_0)), which is the brief's T(r). This confirms that a limit is unavoidable, and Sections 2–4 show what the limit gives.

A further consequence, sketched only: combined with Pesin theory, Lemma Cl and its reverse say that a finite configuration with two-sided decay is a union of forward clusters (pieces of stable leaves) and of backward clusters (pieces of unstable leaves).

Write the incidence structure as a bipartite graph whose vertices are the clusters and whose edges are the points. The number of points E must exceed the number of moment conditions, which is about (number of clusters) x D(N). So the first Betti number E - V + (number of components) of this graph is large. Each independent cycle of the graph is a closed su-polygon. This is the general form of the "exact grid" requirement (EG).

## 6. Variants the brief asks about (sketches, not proofs)

**(i) Smoothing the Dirac masses into densities on centre plaques.**
- If the whole support still shrinks to a point, Lemmas O2/O3 apply verbatim. They concern arbitrary distributions, not only Dirac combinations. So smoothing does not repair the shrinking limit.
- If the centre size is kept fixed while the su-scale shrinks, the limit is supported on a centre disc D. A transversal-jet version of the Oseledets argument of O1 is plausible. Write S = sum_beta T_beta(d^beta_normal psi |_D), with T_beta distributions on D. The forward and backward growth rates of the top transversal component are then determined by the u- and s-orders of beta, which are incompatible as in O1. Cancellations along D (centre moments) gain only e^{o(|t|)}, because the centre exponent is 0.
- I have not proved this. The difficulty is that centre discs are not canonical and the Oseledets data are only measurable along D.

**(ii) Anisotropic limit (shrink only the stable scale).**
- Let only the columns collapse. The limit is then of the form S = sum_i a_i d^m_{W^s(y_i)} delta_{y_i}, with y_i on one unstable disc W^u_rho(z), where d^m_{W^s(y_i)} is an m-th derivative along the stable leaf in its normal-form chart.
- Its support does not shrink to a point, so O2/O3 do not apply.
- Forward decay comes for free: m-th derivatives along stable leaves contract like e^{-(m chi_s - delta) t}.
- Backward decay needs the u-moment cancellation in the a_i. This requires the function y -> d^m_{W^s(y)}(Gamma_{-tau} phi)(y) on W^u_rho(z) to be C^N along the unstable disc, with norms about e^{(m|chi^s|_max - N chi^u_min + delta) tau}.
- That in turn requires the m-jets of the stable foliation to be C^N along unstable leaves. In general this is only Hölder (holonomies are not smooth). It is satisfied in algebraic examples, such as geodesic flows of constant curvature, possibly times a rotation; those are not GH, so there is no conflict there.
- So this variant reduces (PE0) to a regularity property, (SR): C^N-smoothness of the stable leaf-jets along unstable leaves, on a set of positive conditional measure. (SR) is not available from Pesin theory, and I cannot derive it from GH. This is an alternative open route. It is not a proof.

**(iii) A quantitative Theorem J with finite windows and derivative loss.** This was not pursued beyond Proposition W. A direct quantitative version would combine the GH tame estimate (Text B, Lemma 2), which loses m derivatives per Jordan step, with approximate moment identities.
- It seems to bound only S(phi) for fixed smooth phi, in terms of ||phi||_{C^{k + jm}}.
- For configurations at scale r that is automatically small, by the vanishing moments, so it carries no information.
- This is consistent with O3 and is a heuristic only.

## 7. Status

**Proved (no GH):**
- Lemma O1 (cites Oseledets).
- Lemma O2 and Corollary O3 (Arzelà–Ascoli and Schauder).
- Lemma Cl.

These show that step (3) of the brief cannot work. At mu-a.e. base point, any normalised limit of configurations shrinking to that point, with uniform exponential two-sided decay on growing windows, is zero, and the normalised decay constants blow up. This holds for every smooth flow, so GH cannot rescue it, and Theorem J or J* is never reached in a nontrivial way.

The J* case is not fully covered: limits lying in the zero-exponent Oseledets subspace of the jet cocycle are not excluded when the decay is only quasi-analytic.

**Proved (GH via Theorem J):** Proposition W, the finite-window Theorem J. Under GH there is T*(k, eps, A) such that no nonzero S has two-sided decay on |t| <= T* with constant A ||S||_{(C^{k+1})'}. Consequently every approximate scheme is equivalent to producing an exact nonzero two-sided decaying distribution. By O3, such a distribution cannot be obtained as a limit concentrating at a regular point.

**Proved modulo cited Pesin-block continuity:** Lemma G. Fixed-scale approximate grids with defects -> 0 converge to exact su-grids.

**Open:**
- (PE0) itself; this attempt does not prove it.
- (EG): existence of large exact su-grids, or more generally of su-polygon-rich configurations, for the hypothetical mu.
- (SR): smoothness of stable leaf-jets along unstable leaves, the anisotropic route of §6(ii).
- Whether a nonzero point-supported S with l in E_0(z) can have quasi-analytic two-sided decay (the J* gap in §3).
- The smoothing variant §6(i), with fixed centre size.

=== END OF ANSWER round12_q5 ===
