# round3_q3: establishing (AH), (AH') and the Step 5 positivity claim

Verdict: option (a). (AH) follows from published results. Three points need a short extra argument, and each is supplied below: the O(1) curvature error, restriction to exactly J-complex Sigma, and the finitely many simultaneous conditions. The Step 5 positivity claim is correct; a proof is given in Section 4. With these inputs the configuration lemma holds as stated, still modulo (TMZ), which is outside this task.

All citations are from memory. They are stated in the precise form used here and should be checked against the papers.

## 1. Published inputs (from memory)

**[D]** Donaldson, *Symplectic submanifolds and almost-complex geometry*, J. Diff. Geom. 44 (1996). Assume (M, omega) with [omega/2pi] integral, L Hermitian with curvature -i omega, and J omega-compatible. Then there are asymptotically holomorphic (AH) sections of L^k that are eta-transverse to 0, with eta independent of k. The proof uses only:
- (i) local reference sections sigma_{k,p}, which are Gaussian in Darboux-type coordinates rescaled by sqrt(k);
- (ii) a quantitative Sard (Yomdin) lemma for approximately holomorphic functions on a ball;
- (iii) a globalization over a k-independent number of colours of well-separated balls.

**[A1]** Auroux, *Asymptotically holomorphic families of symplectic submanifolds*, GAFA 7 (1997). This is the same result for sections of E (x) L^k, where E is a fixed Hermitian vector bundle of any rank r. It also covers families. For rank r it gives eta-transversality: at each point, either |s| >= eta or nabla s is surjective with a right inverse of norm <= 1/eta. If r > n, this just means |s| >= eta. The theorem also has a perturbative form: any AH sequence s_k can be changed by an AH perturbation of C^1-size < delta to become eta(delta)-transverse, with eta(delta) = delta (log 1/delta)^{-p}.

**[A2]** Auroux, *A remark about Donaldson's construction of symplectic submanifolds*, J. Symplectic Geom. 1 (2002). This is a general globalization principle. Let P be a property of sections that is
- local,
- open under C^1-perturbations: if s satisfies P(eta) at x, then any s' with |s'-s|_{C^1} < c eta satisfies P(eta/2) at x;
- achievable locally: near each x there is a perturbation of size <= delta, built from AH reference sections localized near x, giving P(eta(delta)) on a ball with a polynomial-log estimate.

Then P holds globally for an AH perturbation of size <= delta, with eta independent of k.

## 2. Statement established

**Proposition (AH).** Assume the following:
- (M^{2n}, omega) is closed and J is omega-compatible, with g = omega(., J .).
- E = ⊕_b E_b is a fixed Hermitian bundle.
- P_k are Hermitian line bundles with connections whose curvature F_k satisfies |F_k + 2 pi i k omega|_{C^r(g)} = O(1).
- Sigma_1, ..., Sigma_m are closed submanifolds that are exactly J-complex. M itself is allowed as one of them.

Then for k >> 0 there are AH sections s_k = (s_b) of E (x) P_k and an eta > 0, independent of k, such that for every subset S of the summands and every j, the restriction (s_b|Sigma_j)_{b in S}, a section of (⊕_{b in S} E_b) (x) P_k over Sigma_j, is eta-transverse to 0 on Sigma_j.

## 3. Proof

**Step A (the O(1) curvature error is invisible).** Fix p in M and Darboux coordinates for omega centred at p, with J_p standard. On a ball of radius k^{-1/2} R, pick a unitary gauge in which the connection form is A = A_0 + A_err. Here A_0 is the standard form for -2 pi i k omega, and dA_err = O(1), so A_err = O(|x|) can be chosen in radial gauge.

In the rescaled coordinates y = sqrt(k) x, A_err = O(|x|) dx = O(|y|/k) dy. Its derivatives in y are also O(1/k). Donaldson's estimates for sigma_{k,p} = exp(-|y|^2/4) need errors of O(k^{-1/2}) times polynomial factors in |y|, and this error is smaller. So every local estimate of [D] and [A1] holds verbatim, with the same constants up to O(k^{-1/2}).

Integrality of the class is used only to have the bundle P_k, and that bundle is given. No step of the globalization uses the curvature beyond these local estimates. Twisting by a fixed E is the setting of [A1]: locally, choose a unitary frame of E and multiply it by sigma_{k,p}.

**Step B (one condition (S, Sigma)).** Take Sigma exactly J-complex and of real dimension 2d. Since Sigma is symplectic, at each p in Sigma there are Darboux coordinates for omega on M in which Sigma is the complex linear subspace C^d x 0 and J_p is standard. These come from Weinstein's symplectic neighbourhood theorem together with a linear-algebra normalization at p.

In these coordinates:
- The restriction of sigma_{k,p} to Sigma is the Gaussian reference section of P_k|Sigma for (Sigma, omega|, J|).
- Restrictions of AH sections are AH on Sigma, because J preserves T Sigma, so dbar_Sigma(s|Sigma) = (dbar s)|Sigma.
- The curvature of P_k|Sigma is -2 pi i k omega|Sigma + O(1).

So Step A applies on Sigma. Hence the local step of [A1] on Sigma holds: for x in Sigma and rank r = rank E_S, it produces coefficients w with |w| <= delta such that s_S + sum_q w_q sigma_{k,q} (x) e_q (q ranging over points of Sigma near x) is eta(delta)-transverse on the ball of Sigma around x. This uses Yomdin's lemma for C^r-valued approximately holomorphic maps on a d-ball, which is [A1]'s local lemma.

The perturbations are global sections on M, localized near Sigma. Off Sigma they are irrelevant for this condition. Their effect on the other conditions is controlled in Step C.

The globalization in [A1]/[A2] runs over a covering of Sigma by balls coloured with N colours, where N is independent of k. Its only global ingredient is Gaussian decay of the sigma_{k,q}, and that decay holds on M. So the condition (S, Sigma) holds after an AH perturbation of C^1-size <= delta, with constant eta(delta).

**Step C (finitely many conditions, simultaneously).** List the finitely many pairs (S, Sigma_j) as P_1, ..., P_N. Start from s = 0 and suppose P_1, ..., P_i hold with constant eta_i.

Eta-transversality is C^1-open. If s satisfies it with constant eta and |s' - s|_{C^1} < eta/2, then s' satisfies it with constant eta/2. The reason is that a right inverse of nabla s with norm 1/eta stays a right inverse up to a Neumann series. These are the norms of sections of the bundle E_S restricted to Sigma, and the restriction does not increase them.

Apply Step B for P_{i+1} with delta = eta_i/4. This preserves P_1, ..., P_i with constant eta_i/2 and gives P_{i+1} with constant eta(eta_i/4). Set eta_{i+1} = min(eta_i/2, eta(eta_i/4)).

After N steps, eta = eta_N > 0 depends only on the geometry, not on k. The AH bounds of the sum hold because each perturbation is AH with bounded coefficients. ∎

Remark. Transversality of a full tuple does not imply transversality of its sub-tuples. That is why every S is listed as a separate condition, and the list is finite.

## 4. (AH') and the Step 5 positivity claim

**Lemma.** Work in the rescaled metric. Let V = T_x Sigma be complex and let A + B : V -> C^r, where:
- A = (partial s)_x is complex-linear;
- B = (dbar s)_x has |B| <= c k^{-1/2};
- A + B is surjective with a right inverse of norm <= 1/eta.

Then:
- (a) ker(A + B) is within angle O(k^{-1/2}/eta) of the complex subspace ker A.
- (b) For k large, ker(A + B) is omega-symplectic, and its intersection orientation equals its symplectic orientation.

**Proof.** For t in [0, 1], A + tB has a right inverse of norm <= 2/eta once c k^{-1/2} < eta/2 (Neumann series). So the kernels K_t form a continuous family of subspaces of constant dimension, each within angle O(k^{-1/2}/eta) of K_0 = ker A, which is complex. This proves (a).

For (b):
- Since J is compatible, omega(v, Jv) = |v|^2 on K_0. By closeness, omega restricted to K_t is nondegenerate for all t once k is large. In particular the strata are symplectic.
- Orient K_t from the orientation of V and the complex orientation of C^r (the zero-set convention). This orientation varies continuously in t.
- So does the symplectic orientation, given by omega^{dim/2} restricted to K_t, which is nonzero for every t.
- The two orientations agree at t = 0, where both are complex orientations. By continuity they agree at t = 1.

The real stratum Z_S ∩ Sigma is cut out transversally by the sub-tuple restricted to Sigma, so its tangent space is ker(A + B), and the Lemma applies. Its orientation as an iterated transverse intersection of the oriented hypersurfaces Z(s_b) with the complex-oriented Sigma agrees with the zero-set orientation, up to the standard ordering convention. All factors have even codimension, so ordering signs do not arise. ∎

So the Step 5 claim is correct. Uniformity of the angle in k is exactly the bound O(k^{-1/2}/eta), with eta fixed.

The orientation convention for P_a^± = Z(s_a^±) is the one for which PD[Z(s)] = c_1. This is the convention needed in Step 3's identity PD[P_a^+] - PD[P_a^-] = PD[C_a].

## 5. Verdict on the configuration lemma

With the Proposition (Section 2) and the Lemma (Section 4), Steps 3–5 of Lemma 1 are justified. The family Sigma consists of all strata of C_{<=l}, which are exactly J_l-complex by Lemma 0, together with M.

The lemma therefore holds as stated, modulo:
- (TMZ), quoted from memory;
- the from-memory precise forms of [A1]/[A2] given in Section 1.

Remaining hedges:
- Whether [A1] states the perturbative form with an arbitrary small delta explicitly. I believe [A2] does.
- The Weinstein-chart normalization making Sigma linear while J_p is standard. This is standard linear algebra, since T_p Sigma is J-complex and symplectic.

No obstruction was found.

=== END OF ANSWER round3_q3 ===
