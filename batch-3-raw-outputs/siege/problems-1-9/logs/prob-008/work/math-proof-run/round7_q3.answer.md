# round7_q3: answer (working file)

## Plan
Target: (PE-NH). Under GH, no ergodic flow-invariant mu has h_mu(g_1) > 0 together with a second zero exponent.
Steps:
(1) re-check chain steps 2 and 4;
(2) test the three mechanisms (i)-(iii) of the planner's sketch;
(3) write down with proof every new intermediate result;
(4) state precisely where the argument stops.

## 0. Outcome (summary, filled in at the end)
I did **not** prove (PE-NH), and I found no counterexample. The new material here is:
- §1: a re-check of chain steps 2 and 4. I found no flaw.
- §2: Theorem J_w, a quasi-analytic strengthening of Theorem J with full proof. This is mechanism (iii) made rigorous.
- §3: proofs that (iii), and the "moments" route, cannot by themselves handle mu(d) = 0. These are dead ends, with reasons.
- §4: the volume-preserving case. The Jacobian-cycle obstruction disappears there. The only remaining obstruction is temporal/center closing of su-paths, and I give a precise statement of what would suffice.
- §5: what remains open.

## 1. Re-check of chain steps 2 and 4
Step 4 (variational principle). Let m be g_1-invariant and put mbar = ∫_0^1 (g_s)_* m ds.
- mbar is flow-invariant, because (g_1)_* m = m.
- h_{(g_s)_* m}(g_1) = h_m(g_1), since g_s conjugates (g_1, m) to (g_1, (g_s)_* m).
- Entropy is affine and satisfies Jacobs' integral formula for every measurable decomposition into g_1-invariant measures. Reason: refine the decomposition by the g_1-ergodic decompositions of its pieces. The result is the g_1-ergodic decomposition of the total measure, where Jacobs applies.
- Hence h_m(g_1) = h_mbar(g_1) = ∫ h_{mu_ω}(g_1) dP(ω) over the flow-ergodic decomposition of mbar.
- So h_top(g_1) = sup over flow-ergodic mu of h_mu(g_1). Correct.

Step 2 (Theorem 5.1). Let mu be ergodic with h_mu(g_1) > 0.
- mu(Zero X) = 0.
- The flow direction gives the exponent 0, with multiplicity one if no other exponent vanishes.
- Ruelle's inequality for g_1 and for g_{-1} gives a positive and a negative exponent.
- If mu is hyperbolic transversally to X, Katok's theorem gives a horseshoe (Katok for 3-flows; Lian–Young for C^2 flows in finite dimension, cited from memory). The horseshoe contains a hyperbolic periodic orbit with a homoclinic point. Its asymptotic phase is exponential, by the stable manifold theorem for hyperbolic sets.
- That contradicts Corollary 4.2, i.e. Lemma K/K'. I re-checked the proof of Lemma K (Cayley–Hamilton on jets, steps 1–8) and found it correct.

So the chain is sound, and the only missing link is (PE-NH).

## 2. Theorem J_w: quasi-analytic decay suffices (proved)
Notation as in Theorem J. F_φ(t) = S(e^{J_t} φ∘g_t) and Pφ = Xφ + dφ, so F_φ' = F_{Pφ}.

**Theorem J_w.** Assume GH. Let S be a distribution density and W: R → (0, ∞) a measurable function. Put M_j := ∫_R |t|^j W(t) dt and assume:
- (a) M_j < ∞ for all j ≥ 0;
- (b) Σ_{j≥1} M_j^{-1/j} = ∞;
- (c) there are k and C with |F_φ(t)| ≤ C W(t) ‖φ‖_{C^k} for all real t and all smooth φ.

Then S = 0. Theorem J is the case W(t) = e^{-ε|t|}, where M_j ≤ C j!/ε^j and Σ M_j^{-1/j} ≥ c Σ 1/j = ∞.

*Proof.*
1. As in Theorem J, F_φ is C^1 with F_φ' = F_{Pφ}. By (c) applied to φ and to Pφ (note ‖Pφ‖_{C^k} ≤ C'‖φ‖_{C^{k+1}}), both t^j F_φ and its derivative j t^{j-1} F_φ + t^j F_{Pφ} lie in L^1(R) for every j.
2. A C^1 function g with g, g' ∈ L^1(R) has limits at ±∞, since g(t) = g(0) + ∫_0^t g'. These limits are 0, because g is integrable. Hence t^j F_φ(t) → 0 as |t| → ∞, for every j.
3. Put m_j(φ) := ∫ t^j F_φ(t) dt. Then |m_j(φ)| ≤ C M_j ‖φ‖_{C^k}, so m_j is a distribution density.
4. Integrating by parts, using step 2 for the boundary terms:
   m_0(Pφ) = 0 and m_j(Pφ) = -j m_{j-1}(φ) for j ≥ 1.
5. Exactly as in step 4 of Theorem J (using F1 and F2, i.e. L1 and GH for constant right-hand sides), m_j = 0 for all j.
6. Fix φ and put G(ξ) := ∫ e^{-iξt} F_φ(t) dt. By (a) and (c), G is C^∞ on R, with G^{(j)}(ξ) = ∫ (-it)^j e^{-iξt} F_φ(t) dt. Hence
   |G^{(j)}(ξ)| ≤ C‖φ‖_{C^k} M_j for all ξ and j, and G^{(j)}(0) = (-i)^j m_j(φ) = 0.
7. The sequence (M_j) is log-convex: M_j^2 ≤ M_{j-1} M_{j+1} by Cauchy–Schwarz for the measure W dt. So M'_j := M_j/M_0 is log-convex with M'_0 = 1. Hence (M'_j)^{1/j} is nondecreasing: (log M'_j)/j is the slope of a chord of a convex function issuing from (0, 0). Also Σ (M'_j)^{-1/j} = ∞ by (b), because M_0^{1/j} → 1.
8. *Denjoy–Carleman theorem* (cited from memory). Let N_j > 0 be such that N_j^{1/j} is nondecreasing and Σ N_j^{-1/j} = ∞. Let G ∈ C^∞(R) satisfy |G^{(j)}| ≤ A B^j N_j on R for all j, and G^{(j)}(0) = 0 for all j. Then G ≡ 0.
9. Apply step 8 with N_j = M'_j, A = C‖φ‖_{C^k} M_0 and B = 1. It gives G ≡ 0.
10. F_φ is continuous and in L^1, so Fourier uniqueness gives F_φ ≡ 0. In particular S(φ) = F_φ(0) = 0. ∎

**Example.** W(t) = exp(-|t|/log(e+|t|)) satisfies (a) and (b).
- The maximum of t^j W(t) is attained near t ≈ 4j log j. There W(t) ≈ e^{-j}, so M_j^{1/j} ≤ C j log(j+2).
- (Elementary check: f(s) = j log s − s/(4 log s) is increasing then decreasing on [e^2, ∞), and f(s) ≤ j log(8j log(j+3)) for large j. Also W(t) ≤ e^{-t/(2 log t)} for t ≥ 2.)
- Hence Σ M_j^{-1/j} ≥ c Σ 1/(j log j) = ∞.
- More generally, the classical Carleman–Ostrowski correspondence (cited, not needed above) gives the following. For W = e^{-w(|t|)} with w increasing and w(t)/log t → ∞, condition (b) holds iff ∫^∞ w(t) t^{-2} dt = ∞.

So mechanism (iii) of the planner's sketch is a theorem: Theorem J needs only two-sided quasi-analytic decay, uniform in C^k.

## 3. Why Theorem J_w alone does not reach mu(d) = 0 (dead end, explained, not a theorem)
Theorem J_w relaxes the *rate* of decay. It does not remove the need for decay in *both* directions.

Take S = Σ w_i δ_{y_i} with all y_i on one unstable leaf and forward-generic for mu, where mu(d) = 0. Then:
- backward, the transport decays exponentially (vanishing moments / pairs, as in Prop. 6.1 and 6.2);
- forward, F_φ(t) = Σ_i w_i e^{J_t(y_i)} φ(g_t y_i), with J_t(y_i) = o(t).

The forward orbits of distinct y_i are not asymptotic to each other, except for points that also share a stable manifold. So nothing cancels. For instance, φ ≥ 0 supported near g_t y_1 at a time when the other orbits are far away gives |F_φ(t)| ≈ e^{J_t(y_1)}, which is e^{o(t)} but not small.

Strictly, Theorem J_w needs a bound uniform in φ. The example shows that |F_φ(t)| ≤ C W(t)‖φ‖_{C^k} fails for any W → 0, as soon as at infinitely many times t_n:
- one orbit point g_{t_n} y_1 is separated from the others by a fixed distance, and
- J_{t_n}(y_1) is bounded below.

Both hold for typical forward-generic points.

So any S used at λ = 0 must cancel forward as well. Point masses can then only be combined along *stable* classes, and that is the su-cycle problem of §4. The relaxation from exponential to quasi-analytic decay helps only if one has, for example, forward cancellation with CLT-size Jacobian fluctuations, i.e. weights e^{J_t} = e^{O(√(t log log t))}. Such fluctuations are harmless against any exponential cancellation, and Theorem J already covers that case. **So Theorem J_w gives no new case of (PE-NH).**

## 4. Exponential su-cycles: a precise criterion (proved), and the volume-preserving case
For points x, y write:
- x ~s y if d(g_t x, g_t y) ≤ C e^{-θt} for all t ≥ 0;
- x ~u y if d(g_t x, g_t y) ≤ C e^{-θ|t|} for all t ≤ 0.

For x ~s y the limit B^s(x, y) := lim_{t→+∞} (J_t(x) − J_t(y)) exists, and |J_t(x) − J_t(y) − B^s(x, y)| ≤ (Lip d) C e^{-θt}/θ for t ≥ 0. Likewise, for x ~u y the limit B^u(x, y) := lim_{t→−∞} (J_t(x) − J_t(y)) exists.

**Proposition Q (closed weighted su-cycles are forbidden; proved).** Assume GH. Let L ≥ 1 and let a_1, ..., a_{2L} be points (indices mod 2L) with a_{2i−1} ~s a_{2i} and a_{2i} ~u a_{2i+1} for i = 1..L, with common constants C and θ. Define weights recursively by w_1 = 1 and
 w_{2i} = w_{2i−1} e^{B^s(a_{2i−1}, a_{2i})},  w_{2i+1} = w_{2i} e^{−B^u(a_{2i+1}, a_{2i})} (i < L).
Suppose:
- (H) the cycle closes consistently: w_1 = w_{2L} e^{−B^u(a_1, a_{2L})} (the Jacobian holonomy around the cycle vanishes);
- (G) for some θ' < θ: J_t(a_{2i−1}) ≤ C + θ' t for t ≥ 0, and J_t(a_{2i}) ≤ C + θ'|t| for t ≤ 0, for all i.

Then the distribution S := Σ_{j=1}^{2L} (−1)^{j+1} w_j δ_{a_j} is zero. Equivalently, the weighted multiset of the odd-indexed points equals that of the even-indexed points.

*Proof.* We have F_φ(t) = Σ_j (−1)^{j+1} w_j e^{J_t(a_j)} φ(g_t a_j).

*Forward (t ≥ 0).* Group the terms in the pairs (2i−1, 2i). Writing r = J_t(a_{2i}) − J_t(a_{2i−1}) + B^s(a_{2i−1}, a_{2i}), we get

 w_{2i−1} e^{J_t(a_{2i−1})} φ(g_t a_{2i−1}) − w_{2i} e^{J_t(a_{2i})} φ(g_t a_{2i}) = w_{2i−1} e^{J_t(a_{2i−1})} [φ(g_t a_{2i−1}) − e^{r} φ(g_t a_{2i})].

Here |r| ≤ C' e^{-θt}, so the bracket is at most C'' e^{-θt} ‖φ‖_{C^1}. By (G) the pair contributes at most C''' e^{-(θ−θ')t} ‖φ‖_{C^1}.

*Backward (t ≤ 0).* Group the terms in the pairs (2i, 2i+1), for i = 1..L, where the pair i = L is (2L, 1). For i < L the definition of w_{2i+1} gives w_{2i+1} = w_{2i} e^{−B^u(a_{2i+1}, a_{2i})}. For i = L, (H) gives w_1 = w_{2L} e^{−B^u(a_1, a_{2L})}. The signs are −w_{2i} on a_{2i} and +w_{2i+1} on a_{2i+1}. Writing r' = J_t(a_{2i+1}) − J_t(a_{2i}) − B^u(a_{2i+1}, a_{2i}), each pair equals

 −w_{2i} e^{J_t(a_{2i})} [φ(g_t a_{2i}) − e^{r'} φ(g_t a_{2i+1})].

Here |r'| ≤ C' e^{-θ|t|}. By (G) the pair contributes at most C e^{-(θ−θ')|t|} ‖φ‖_{C^1}.

So (*) of Theorem J holds with k = 1 and ε = θ − θ', and S = 0. ∎

*Remarks.*
- L = 1 is the homoclinic-pair case a_1 ~s a_2, a_2 ~u a_1, with S = δ_{a_1} − e^{B^s(a_1, a_2)} δ_{a_2}. There (H) reads B^s(a_1, a_2) = B^u(a_1, a_2), a genuine condition. When it fails, the pair alone gives nothing; Lemma K handles the periodic case differently.
- The bookkeeping above was checked as follows. With these weights, the exponents r and r' in the proof tend to 0, and do not tend to ±2B.
- Lemma K / Corollary 4.2 are the periodic analogues, where Cayley–Hamilton replaces exact pairing.

**Corollary Q_V (volume-preserving case).** Assume GH and that X preserves a smooth positive density ω. Take ν = ω, so d = 0, J ≡ 0 and all B vanish, and (H), (G) hold automatically. Then there is no closed exponential su-cycle a_1 ~s a_2 ~u a_3 ~s ... ~u a_{2L} ~u a_1 whose alternating sum Σ (−1)^{j+1} δ_{a_j} is nonzero. More generally, the following holds. Let finitely many distinct points carry real coefficients c_k such that, for the equivalence classes generated by ~s and by ~u among the chosen points (with uniform constants), the coefficients sum to 0 in every s-class and in every u-class. Then all c_k = 0, by the same proof: group forward by s-classes and backward by u-classes.

**What this means for (PE-NH) in the volume case.** Under (V) (smooth invariant volume) every invariant measure equals ω by (O2). So a positive-entropy ergodic mu must be ω itself, with mu(d) = 0. Then (PE-NH) in the volume case would follow from:

**(Q-cl)** If ω is a smooth invariant volume of a C^∞ flow, ergodic and non-hyperbolic with h_ω(g_1) > 0, then there are finitely many Pesin-regular points with coefficients satisfying the bipartite condition of Corollary Q_V, not all zero. For example, a non-degenerate closed su-cycle.

I could not prove (Q-cl). Here is the obstruction, made precise.
- Let n = dim M, and let s, u ≥ 1 be the stable and unstable dimensions.
- The center (zero-exponent) space has dimension c + 1 ≥ 2, flow direction included.
- An s-u-s path a → b → c' → e from a reaches a set of dimension ≤ 2s + u.
- Closing it by a final u-leg into a requires e ∈ W^u(a), a condition of codimension n − u = s + c + 1 in M.
- So closed quadrilaterals are expected only in families of dimension ≤ (s + u) − (c + 1), and these always contain the degenerate ones (a leg of length 0).
- Non-degenerate solutions need a transversality (non-joint-integrability) property of the measurable Pesin laminations, or exact joint integrability as in "suspension with constant roof × rotation". Neither is available in general.

Sanity checks (the criterion detects the classical non-GH examples).
- For (suspension of an Anosov diffeomorphism with constant roof) × (Diophantine rotation), closed su-quadrilaterals exist inside each su-leaf, by local product structure.
- For (contact Anosov flow) × rotation, the temporal-distance function of quadrilaterals takes both signs and vanishes on non-degenerate quadrilaterals. (This is the usual intermediate-value argument; sketched, not checked in detail.)

The planner's suggestion (i), to "spread over a center transversal", amounts to this. Average a family of su-cycles that close only up to a center/flow displacement H (the su-holonomy acting on a center transversal Σ) against a density ρ on Σ. The defect cancels exactly iff H_*(ρ) = ρ on the relevant part of Σ. If H_*ρ ≠ ρ, the defect term, transported, does not decay in either direction, because it is a difference of two measures carried by different center points. So (i) needs a *smooth-enough, compactly supported transversal measure invariant under su-holonomy*. That is a rigidity statement of the same depth as (Q-cl). It may even be false in general, e.g. for strictly twisting holonomy, where the quadrilateral holonomy angle behaves like κ·(s-length)(u-length) with κ ≠ 0. Dead end, as far as I can see.

On mechanism (ii) (continuation across Re z = 0). Lemma M needs the pair Laplace transform to continue to a neighbourhood of z = 0. I found no source of continuation for non-periodic Pesin points.
- Theorem B obtains continuation from exact self-similarity: the transfer operator on a contracting disc at a periodic point.
- For returns of a generic orbit to a Pesin block, the return maps differ from return to return. The "transfer operator" becomes a non-autonomous product, and there is no spectral theory (no Hennion bound for a single operator) to continue the resolvent.
- I see no way around this, so (ii) is also left open.

## 5. Final status

**Proved here (new, complete proofs):**
1. Theorem J_w (§2). Under GH, a distribution density whose weighted transport decays two-sidedly at any quasi-analytic rate (Σ M_j^{-1/j} = ∞), uniformly in C^k, vanishes. The proof cites only the Denjoy–Carleman theorem.
2. Proposition Q and Corollary Q_V (§4). Under GH, there is no closed exponential su-cycle with vanishing Jacobian holonomy and controlled Jacobian growth whose weighted alternating sum is nonzero. Under GH plus a smooth invariant volume, there is no nonzero finite configuration of points with coefficients summing to zero on every forward-exponential-asymptotic class and every backward one.
3. Re-check of chain steps 2 and 4 (§1): no flaw found.

**Reduction (proved).** In the volume-preserving case, (PE-NH) follows from the GH-free dynamical statement (Q-cl) of §4: a non-hyperbolic, ergodic, positive-entropy smooth volume admits a non-degenerate bipartite su-configuration. In general, (PE-NH) at λ = mu(d) = 0 would follow from the weighted analogue: points satisfying the hypotheses of Proposition Q, including the Jacobian-holonomy condition (H).

**Dead ends (explained in §3–§4).**
- Weaker decay (iii) does not help without forward cancellation.
- Spreading over center transversals (i) needs an su-holonomy-invariant transversal measure.
- Continuation (ii) needs exact self-similarity.

**Open (not settled here):**
- (PE-NH) itself, i.e. the case of a non-hyperbolic ergodic mu with h_mu(g_1) > 0, in particular with mu(d) = 0 (dim M ≥ 4).
- (Q-cl), even for smooth volumes.
- Whether GH excludes real eigen-distributions Xu = κu, κ ≠ 0 ((E1); this would imply the goal by round 5).

Hence the problem's claim h_top(g_1) = 0 remains proved only for dim M ≤ 3 (Theorem 5.2) and, in every dimension, for the measures covered by Theorem 5.1 and Propositions 6.1 and 6.2. No counterexample was found. Every known non-GH positive-entropy example I checked violates GH through the mechanisms above.

=== END OF ANSWER round7_q3 ===

