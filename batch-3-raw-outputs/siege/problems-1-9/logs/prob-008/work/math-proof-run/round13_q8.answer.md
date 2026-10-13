# round13_q8 answer — (PE0) attempted; NOT proved, no counterexample found

## Summary of outcome
- I did **not** prove (PE0), and I did not find a counterexample. The problem's claim is therefore still established
  only in the cases listed in the ledger: dim M <= 3; every hyperbolic measure; lambda != 0 (modulo the cited [NF']).
- §1: I checked the chain. It is logically sound. Variational principle, then #113, then (PE0), gives the goal.
  Its only non-elementary inputs besides (PE0) are the citations inside #113 (Pesin theory, Ledrappier–Strelcyn, [NF']).
- §2: Two small observations with complete proofs, for the volume-preserving case. Both follow directly from the
  background. I record them because they say exactly what GH gives spectrally, but **they do not settle (PE0)**:
  (2.1) under GH + volume, no nonzero mean-zero distribution has two-sided exponential decay of correlations;
  (2.2) under GH + volume, the spectral projections near frequency 0 satisfy a quantitative flatness bound, together with its dual.
- §3: For each mechanism I examined, I give the precise point where it fails (dead ends). This includes Mechanisms C and E of the planner.
- §4: Open questions, stated precisely.

---

## 1. Check of the chain (the derivation of the goal from (PE0))

1. Suppose h_top(g_1) > 0. The variational principle for the homeomorphism g_1 gives a g_1-invariant μ' with h_{μ'}(g_1) > 0.
   Ergodic decomposition with respect to g_1 and Jacobs' formula h_{μ'} = ∫ h_{μ_e} dτ(e) then give a
   g_1-ergodic μ with h_μ(g_1) > 0. This is correct.
2. #113 asserts ∫ J_1 dμ = 0 for such μ under GH. I did not re-derive it. It rests on Pesin unstable manifolds,
   the Ledrappier–Strelcyn partition (with Lemma 6.0, whose proof I checked: correct) and the cited normal forms
   [NF']. The logical form of the conclusion is exactly the hypothesis negated in (PE0).
3. (PE0) is stated for g_1-ergodic μ (not flow-ergodic). This matches the output of step 1, so there is no mismatch.
   Since h_top(g_t) = |t| h_top(g_1), the goal follows.

**Verdict:** the chain derives the goal from (PE0) + #113. Nothing is missing apart from (PE0) itself and the
citations inside #113.

---

## 2. Two observations (proved), volume-preserving case

Standing assumption in this section: GH holds and X preserves a smooth positive probability density ω.
Take ν = ω, so d = 0 and J_t = 0.

**Proposition 2.1 (no exponentially decaying correlations).** Let S be a distribution density. Suppose there are
ε > 0, k and C with |S(φ∘g_t)| <= C e^{-ε|t|} ||φ||_{C^k} for all real t and all smooth φ. Then S = 0.
In particular, no smooth h with ∫ h dω = 0 and h ≠ 0 has two-sided exponential decay of correlations
∫ h·(φ∘g_t) dω = O(e^{-ε|t|}) ||φ||_{C^k}. A smooth volume-preserving flow that is exponentially mixing for smooth
observables is therefore never GH.

*Proof.* With J = 0, F_φ(t) = S(e^{J_t} φ∘g_t) = S(φ∘g_t). The hypothesis is exactly (*) of Theorem J (R6-a),
so S = 0. For the second statement take S = hω. ∎

**Proposition 2.2 (spectral flatness at 0, quantitative).** Let U_t φ = φ∘g_t be the Koopman group on L²(ω).
Write U_t = e^{itA} with A self-adjoint (Stone), and let E(·) be the spectral measure of A. Then there are m and C such that:
(a) ||E([-ε, ε]) f||_2 <= C ε ||f||_{C^m} for all ε > 0 and all smooth f with ω(f) = 0;
(b) every g in E([-ε, ε]) L² with ∫ g dω = 0 satisfies |∫ g f dω| <= 2Cε ||g||_2 ||f||_{C^m} for all smooth f.
So unit vectors of the spectral subspace near 0 are O(ε)-small in (C^m)'.

*Proof.* (a) Lemma 2 of Text B with k = 0 and ν = ω gives a smooth u with ∫ u dω = 0, Xu = f and
||u||_{L²} <= ||u||_{C^0} <= C ||f||_{C^m}. (Solvability holds by (O2): f is annihilated by the only invariant
distribution density ω, and X(C^∞) is closed.) For smooth u, (U_t u − u)/t → Xu in L², so u ∈ Dom(A) and
iAu = Xu = f. Hence ||E_ε f||² = ∫_{[-ε,ε]} ξ² dσ_u(ξ) <= ε² ||u||², where E_ε := E([-ε, ε]).
(b) g = E_ε g and E_ε is self-adjoint. Since ∫ g dω = 0, ⟨g, f⟩ = ⟨g, f − ω(f)⟩ = ⟨g, E_ε(f − ω(f))⟩.
Apply (a) to f − ω(f), using ||f − ω(f)||_{C^m} <= 2||f||_{C^m}. ∎

**Why 2.2 does not give (PE0).** Suppose h_ω(g_1) > 0. Then the flow has (countable) Lebesgue spectrum on
L² ⊖ L²(Pinsker). (This is the Rokhlin–Sinai theorem for automorphisms, cited from memory; for flows I recall the
analogous statement but have not checked it.) So E_ε L²_0 is infinite-dimensional for every ε. But an
infinite-dimensional subspace of L² can consist entirely of vectors that are small in (C^m)' (vectors of high
Laplace frequency), so (b) gives no contradiction. A spectral-type contradiction would need a link between the
Lebesgue-spectrum generators (wandering subspaces built from the unstable partition, which are only measurable
transversally) and Sobolev regularity. I see no such link; this agrees with round12_q6 (#126).

---

## 3. Mechanisms examined and why each stops

**3.1 Mechanism C (weighted chains, exact closing up to a flow shift).**
I re-derived the bookkeeping. Take a chain z_0 →u z_1 →s z_2 ... →s z_{2L} = g_τ z_0 of distinct points.
The classes are {z_{2i}, z_{2i+1}} (unstable) and {z_{2i+1}, z_{2i+2}} (stable). The homogeneous system (G) of
Theorem G has 2L equations in 2L+1 unknowns, so there is a one-dimensional solution line; normalise w_0 = 1.
Let G_φ(t) = e^{J_t(z_0)} φ(g_t z_0) and S = Σ w_i δ_{z_i}. Then:
- for t → +∞: F_φ(t) = G_φ(t) + O(e^{-(θ−η)t}) ||φ||_{C^1};
- for t → −∞: F_φ(t) = w' G_φ(t + τ) + O(e^{-(θ−η)|t|}) ||φ||_{C^1}, where w' = w_{2L} e^{-J_τ(z_0)}.

If w' = 1 (the holonomy condition), then G(t + τ) − G(t) = Seg(Pφ)(t), where Seg = ∫_0^τ e^{J_s(z_0)} δ_{g_s z_0} ds
(transported). So S − δ_{z_0} decays forward and differs from Seg∘P by a decaying term backward. This is the
planner's identity, and it confirms that the analytic part is sound. The whole difficulty lies in the
**existence of the chain**:
- for a non-hyperbolic μ, T W^{ws} + T W^{wu} = E^s ⊕ E^u ⊕ RX has codimension c − 1 >= 1, where c = dim E^c >= 2;
- so an exact closing (up to a flow shift) is a codimension-(c − 1) event on Pesin leaves, which pass only through
  μ-typical points and depend only measurably on the point;
- measure theory (Ledrappier–Young: the measurable hulls of W^u and W^s are both the Pinsker σ-algebra) controls
  su-classes only modulo null sets, while exact closing is a statement about a null set.

So conjecture (a) of the planner is not reachable by the tools available. Without (a), parts (b) and (c) have nothing to act on.

**3.2 Smeared (continuous) su-rectangles.** Suppose S = ∫∫ w(a,b) δ_{z(a,b)} da db with ∫ w(a,b) db = 0 along
stable fibres and ∫ w(a,b) da = 0 along unstable fibres. This needs z(a,b) ∈ W^{ss}(p_a) ∩ W^{uu}(q_b), i.e. a local
product structure. For non-hyperbolic μ that structure fails, by the same codimension count as in 3.1. So smearing does not avoid
the closing problem.

**3.3 Averaged pairs / measurable leafwise maps.** Take S = ω|_A − y_*(ω|_A), with y(x) ∈ W^u_loc(x). Backward decay
holds on a Pesin block. If y preserves the leafwise conditionals, then S = 0. If it does not, forward decay of
∫ φ∘g_t dS is a rate of equidistribution of unstable discs, and no such rate is available. This is the
known obstruction (R6-d), seen from a different angle.

**3.4 Mechanism E (a second ν-conformal measure).** A finite measure σ with σ(Xφ + dφ) = 0 must have
g_t-Jacobian e^{J_t}, the same as ν. Leafwise, on unstable leaves, this forces SRB-type (leaf-volume-like)
conditionals. In the centre directions there is no thermodynamic construction of conditionals with a prescribed
Jacobian without hyperbolicity. Natural limiting constructions, i.e. Abel-weighted orbit averages, converge to ν
itself by Lemma D. I found no construction of a ν-singular σ.

**3.5 Eigen-distributions (E1).** By R5-a, positive Lyapunov growth always produces real eigen-distributions
Xu = κu with κ ≠ 0, without GH. So (E1) implies the goal. I could not exploit GH on Xu = κu: the right-hand side κu is not
known to be smooth, so GH cannot be applied, and the a priori estimate loses derivatives when one tries to absorb κu.

**3.6 Dissipative compact invariant pieces.** Let K ≠ M be closed and invariant. Under GH every ergodic measure on
K has m(d) ≠ 0 (Corollary D1, contrapositive). If one could approximate μ by transitive compact invariant sets on
which the ergodic averages of d take both signs, the intermediate-value property of ergodic averages on such sets
would produce an ergodic m with m(d) = 0 on K ≠ M, a contradiction. For non-hyperbolic μ no such approximation
theorem is available. Isometric extensions of horseshoes show that there may be no periodic orbits at all.

---

## 4. What is proved and what remains open

**Proved here:**
- the chain check (§1);
- Propositions 2.1 and 2.2, in the volume-preserving case, using only the background (Theorem J, Text B Lemma 2, (O2));
- the bookkeeping identity of 3.1, i.e. the analytic half of Mechanism C, assuming the chain exists.

**Not proved (open):**
- **(PE0)** itself, including its volume-preserving case. In the volume case (PE0) says: under GH + smooth invariant volume, h_ω(g_1) = 0.
- (CH) / planner (a): existence, for a non-hyperbolic positive-entropy μ with λ = 0, of exactly closing su-chains
  (up to a flow shift) through μ-typical points.
- (E1): under GH, no nonzero u ∈ D' with Xu = κu for real κ ≠ 0. This would imply the goal via R5-a.
- A ν-singular finite measure σ with σ(Xφ + dφ) = 0 built from μ (Mechanism E). Lemma A would then give a contradiction.

The problem's claim therefore remains established only for dim M <= 3 and for hyperbolic positive-entropy
measures (unconditionally, modulo the classical cited theorems), and for λ ≠ 0 (modulo [NF']). The general case
reduces to (PE0), which I could not settle.

=== END OF ANSWER round13_q8 ===
