# round10_q4: attempt to refute (JC)

## Plan
I first look for a counterexample of type (a) or a contradiction of type (b). If neither works, I record why each natural template fails and prove the partial results I can reach. All results below are proved unless they are explicitly labelled otherwise.

## 0. Verdict
I found no refutation of (JC). Every template I know is either (i) smoothly conjugate to a Diophantine linear flow, where (NJ) holds (Prop. 2 below), or (ii) not GH, for one of the reasons in §3. A refutation of type (a) would need a GH field outside the Diophantine class, and so would disprove the Katok / Greenfield–Wallach conjecture. I found none.

I also found no contradiction of type (b):
- (JC) holds in the whole known GH class.
- The chain is consistent. Theorem R yields its strip families only from positive-entropy measures, and (JC) is used only to rule those out.

Note: a soft argument of the form "chains at Re c ≠ 0 exist for every flow with ..." cannot use only the growth or eigen-density structure. Prop. 1 shows that chains are confined to a strip whose width is set by the exponential C^1-growth of the weighted transfer operator. When that growth is zero, there are no chains off the imaginary axis at all.

## 1. Proposition 1 (no GH used): an a priori bound on where chains can be
Notation is as in the task: ν is a smooth positive density, d = div_ν X, Pφ = Xφ + dφ, and J_t(x) = ∫_0^t d(g_s x) ds. Define S_t φ = e^{J_t}·(φ∘g_t). Then (S_tφ)ν = g_t^*(φν), since g_t^*ν = e^{J_t}ν.

**Lemma 1.1.** For smooth φ, S_tφ is smooth jointly in (t,x). Also d/dt S_tφ = S_t Pφ = P S_tφ.
*Proof.* Write d/dt g_t^*(φν) = g_t^* L_X(φν) = L_X g_t^*(φν). Then use L_X(ψν) = (Pψ)ν. ∎

Since (t,x) ↦ S_tφ(x) is smooth, the map t ↦ S_tφ is C^1 into the Banach space C^1(M). Its derivative is S_tPφ = PS_tφ, because difference quotients of a jointly smooth function converge in C^1 uniformly on compact t-intervals.

Note that ‖S_t‖_{C^1→C^1} ≤ C_0 e^{K|t|} for some finite K, because ‖Dg_t‖ and ‖∇J_t‖ grow at most exponentially. Put
Λ_+ = limsup_{t→+∞} t^{-1} log ‖S_t‖_{C^1→C^1},   Λ_- = limsup_{t→-∞} |t|^{-1} log ‖S_t‖_{C^1→C^1}.

**Proposition 1.** Suppose B ∈ (C^1)' satisfies B(Pφ) = cB(φ) for all smooth φ. If Re c > Λ_+ or Re c < -Λ_-, then B = 0. Hence a point c carrying an order-1 Jordan chain, or even a single order-1 eigen-density, satisfies -Λ_- ≤ Re c ≤ Λ_+. In particular, (JC) holds trivially for every strip (a,b) that is not contained in [-Λ_-, Λ_+]. If Λ_+ = Λ_- = 0, then (NJ) holds.

*Proof.*
1. Let f(t) = B(S_tφ). Then f'(t) = B(PS_tφ) = c f(t), so f(t) = e^{ct}B(φ).
2. Hence |B(φ)| ≤ ‖B‖ ‖φ‖_{C^1} exp(-t Re c + log‖S_t‖).
3. If Re c > Λ_+, let t → +∞. If Re c < -Λ_-, let t → -∞. In both cases the right side tends to 0.
4. So B vanishes on C^∞(M). Since C^∞ is dense in C^1, B = 0. ∎

For the A-member of a chain, the same computation gives A(S_tφ) = e^{ct}(A(φ) + tB(φ)). The polynomial factor t does not change the exponential bound.

Remarks.
- This is consistent with Theorem R: its strip lies at Re z ≈ λ + (0,θ), with θ below the smallest positive exponent. That strip lies inside [-Λ_-, Λ_+].
- For fields smoothly conjugate to Diophantine linear flows, Λ_± = 0. By Ruelle's inequality, Λ_± = 0 already forces zero entropy. So Prop. 1 is circular with respect to the goal. Its use is to show that a refutation of (JC) needs exponential growth of derivatives, i.e. hyperbolic-type behaviour.

## 2. Proposition 2: (NJ), hence (JC), holds for every field smoothly conjugate to a Diophantine linear flow
Let F: M → T^n be a diffeomorphism with F_*X = Y = Σ α_j ∂_j, where α is Diophantine.

The chain notion is natural under diffeomorphisms. Push A, B forward by F, and replace ν by F_*ν. The relations B(Pφ) = cB(φ) and A(Pφ) = cA(φ) + B(φ) transform into the same relations for Y. They are also independent of the density, by the remark in the task. So we may take ν to be Lebesgue measure on T^n. Then d = 0 and P = Y.

In the distribution form u = B/ν, the relation reads Yu = -cu. In Fourier coefficients this is (2πi α·k + c) û_k = 0 for all k ∈ Z^n.

**No eigen-densities off iR.** If Re c ≠ 0, every factor is nonzero, so û = 0 and B = 0.

**No chains at all, even on iR.**
1. Let c = -2πi α·k_0. Since α is rationally independent, k_0 is unique, and û is supported at k_0.
2. The equation for v = A/ν reads (2πi α·k + c) v̂_k = -û_k.
3. At k = k_0 the left side is 0, so û_{k_0} = 0. Hence u = 0.

So (NJ) holds, and with it (JC). This includes every time change hX of a Diophantine linear flow (h > 0 smooth). Such a time change is again smoothly conjugate to a Diophantine linear flow, by the classical argument: 1/h = m + Yb is solvable for Diophantine α. So time changes give no new template. ∎

## 3. Proposition 3 (no GH used): in the volume-preserving case, eigen-densities off iR are not L^2
Assume L_X ω = 0 for a smooth positive density ω, and take ν = ω, so that d = 0. Suppose u ∈ L^2(ω) and Xu = -cu in D' with Re c ≠ 0. Then u = 0.

*Proof.*
1. Let u_ε be Friedrichs mollifications, built in finitely many charts with a partition of unity.
2. By Friedrichs' lemma for first-order operators with smooth coefficients (cited), u_ε → u and Xu_ε → Xu in L^2.
3. Since div_ω X = 0, Re⟨Xw, w⟩_{L^2(ω)} = ½ ∫ X|w|^2 ω = 0 for smooth w.
4. Passing to the limit, 0 = Re⟨Xu, u⟩ = -Re c ‖u‖^2. ∎

So in the volume case, any chain at Re c ≠ 0 has u ∉ L^2. In every case u and v are non-smooth:
- Smooth u with Xu = -cu satisfies |u(g_t x)| = e^{-t Re c}|u(x)|. Boundedness in both time directions forces u = 0.
- If v were smooth, then u = -(X+c)v would be smooth, hence u = 0.

## 4. Proposition 4 (GH): no zero of X whose linear part has spectrum in an open half-plane
This removes the "zeros / Morse–Smale" template more strongly than P1 of the background (d(p) ≠ 0).

**Statement.** Assume GH. Then X has no zero p with all eigenvalues of A = DX(p) in {Re > 0}, and none with all eigenvalues in {Re < 0}. This holds in any dimension n ≥ 1.

*Proof.* By (O4), -X is GH, so it suffices to treat {Re > 0}.

1. **Lyapunov sphere.** In a chart at p, Lyapunov's theorem gives a positive definite quadratic form Q with DQ(x)·Ax ≥ 2a Q(x) for some a > 0. Since X(x) = Ax + O(|x|^2), for r > 0 small we get X Q ≥ aQ on B = {Q < r^2}. Fix 0 < s < r and let S = {Q = s^2}.
   - Backward orbits stay in B and satisfy Q(g_{-t}x) ≤ e^{-at}Q(x). So every orbit in B \ {p} is backward-asymptotic to p.
   - Q increases strictly along orbits in B. So each such orbit crosses S exactly once, transversally: at a time τ(x) that is positive if Q(x) < s^2 and negative if Q(x) > s^2.
2. **Invariant function.** By the implicit function theorem, the crossing time τ(x) and the crossing point π(x) = g_{τ(x)}x ∈ S are smooth on B \ {p}. Pick h ∈ C^∞(S) nonconstant; this is possible since S ≅ S^{n-1}, which has two points when n = 1. Put u = h∘π. Then u is smooth and bounded on B \ {p}, and Xu = 0 there.
3. **Cut-off.** Let χ be smooth with χ = 1 near p and supp χ ⊂ B, and set w = χu, with w(p) = 0. Then w ∈ L^∞(M).
4. **Xw is smooth.** For a test function φ,
   ∫ w (Xφ + dφ)ν = lim_{ε→0} ∫_{Q>ε^2} w L_X(φν) = -lim ∫_{Q>ε^2} (Xw)φν + (boundary term).
   The boundary term is bounded by ‖w‖_∞ ‖φ‖_∞ ∫_{Q=ε^2} |ι_X ν|. This is O(ε^{n-1}·ε) → 0, because |X| = O(ε) on {Q = ε^2}. Hence the distribution Xw equals the pointwise function (Xχ)u. That function is smooth, since supp Xχ is a compact subset of B \ {p}, where u is smooth.
5. **w is not continuous at p.** Every orbit in B \ {p} accumulates at p in backward time, and u is constant on orbits. So u takes every value of h in every neighbourhood of p. Since h is nonconstant, w is not continuous at p, hence not smooth.
6. This contradicts GH. ∎

(Hyperbolic saddles are not covered by Prop. 4. Whether GH excludes all zeros is not settled here.)

## 5. Templates for (a) and where each fails
1. **Diophantine linear flows, their smooth conjugates and time changes.** (JC) holds (Prop. 2).
2. **Products and skew products of such flows.** A product of linear flows is linear. It is GH exactly in the jointly Diophantine case, which is covered by Prop. 2. If it is not jointly Diophantine, there is a distribution u with Xu = 0 that is not constant, either a resonant character or a Liouville-type series, contradicting L1.
3. **Flows with zeros: Morse–Smale, gradient-like, north-south.** These fail GH:
   - a source or sink violates Prop. 4;
   - a zero with d(p) = 0 violates P1.
   Every compact gradient-like flow has a source and a sink (the maximum and minimum of the Lyapunov function, if nondegenerate). In the degenerate case Prop. 4 does not apply as stated; I flag this as unchecked.
4. **Volume-preserving parabolic flows (horocycle flows, Heisenberg nilflows).** By Flaminio–Forni (cited from memory), these have non-trivial invariant distributions D with D(Xf) = 0 for all f, besides volume. Taking ν = ω (so d = 0), D/ω is a non-constant distribution u with Xu = 0, contradicting L1. So they are not GH.
5. **Anosov and Axiom A flows, suspensions of horseshoes.** These have periodic orbits. Volume-preserving ones are excluded by Observation P (Jacobian-1 periodic orbits). Dissipative ones must keep all periodic orbits in a basic set with one sign of ∫_γ d (Cor. C1). Even then, these flows have strip families of eigen-densities in (C^1)' (Theorem R requires no GH), hence order-1 chains at every point of a strip (Cor 7.2). They are therefore exactly the objects (JC) must exclude. Proving them non-GH directly is equivalent to the problem in the hyperbolic case, which Theorem J settles: hyperbolic positive-entropy measures are excluded under GH. So no Anosov or Axiom A template can be GH.
6. **Isolated chains at zeros.** At a zero p with B = δ_p, a chain at c = d(p) exists iff some a ∈ ker DX(p)^T has a·∇d(p) = 1 (direct computation of A = Σ a_i ∂_iδ_p). Such chains are isolated, so they do not refute (JC). Zeros of this kind are moreover partly excluded under GH (Prop. 4, P1).
7. **Soft-argument template for (b): "a nonconstant divergence average forces chains".** This fails by Prop. 1. Chains need exponential C^1-growth of S_t, i.e. hyperbolicity-type behaviour (Λ_± > 0), not merely variation of μ(d). By Ruelle's inequality, positive entropy forces Λ_± > 0. So the only route to chains filling a strip is the Theorem R mechanism, and it is exactly the one (JC) is designed to exclude.

## 6. Summary: proved vs open
Proved:
- Prop. 1: order-1 eigen-densities and chains only exist in -Λ_- ≤ Re c ≤ Λ_+. No GH is used. As a consequence, (JC) holds for strips not inside that band, and (NJ) holds when Λ_± = 0.
- Prop. 2: (NJ), hence (JC), holds for every field smoothly conjugate to a Diophantine linear flow, including time changes.
- Prop. 3: in the volume-preserving case, eigen-densities off iR are not in L^2. Chain members are never smooth.
- Prop. 4: under GH there are no zeros whose linearisation has spectrum in an open half-plane.

Not achieved:
- No counterexample to (JC). Any counterexample must be a GH field outside the Diophantine class, so it would also refute the Katok / Greenfield–Wallach conjecture; I found none.
- No contradiction derived from (JC).

Open:
- (JC) itself, and the stronger (NJ), on strips inside [-Λ_-, Λ_+] not containing 0.
- (SO), the planner's tilted Lemma C.
- Whether GH excludes hyperbolic saddle zeros, and degenerate zeros.

=== END OF ANSWER round10_q4 ===
