# round3_q1: does GH imply (V), a smooth invariant volume?

**Outcome.** I did NOT prove (V), and I did not refute it. Below I check (N1)–(N4); all four are correct, with small precisions noted. I then prove two small new statements that sharpen the reduction. Last, I state the exact remaining gap and record the dead ends.

Conventions are those of Text B: ν is a smooth positive density, d = div_ν X, and J_t = ∫_0^t d∘g_s ds. A density ρν is invariant iff L_X(ρν) = 0, i.e. Xρ + dρ = 0 in D', i.e. ρ∘g_t · e^{J_t} = ρ a.e.

## 1. Verification of (N1)–(N4)

**(N1) Correct.** For an invariant Borel set B and a test function φ:
⟨X1_B, φν⟩ = −∫_B L_X(φν) = −(d/dt)|_{0} ∫_B g_t^*(φν) = −(d/dt)|_0 ∫_{g_tB} φν = 0.
L1 then makes 1_B a.e. constant. For a measurable invariant F, apply this to the sets {F > c}.

**(N2) Correct.** The Hopf decomposition is invariant, so by (N1) the flow is either conservative or totally dissipative. In the totally dissipative case the flow is measurably a translation flow on R × Y. Ergodicity then forces Y to be a single atom, so ν would live on one orbit. That is impossible when dim M ≥ 2, since an orbit is a ν-null C^1 curve. (When dim M = 1 we have M = S^1. GH then excludes zeros by P1 and by the sink/source argument of §2(b), so X has no zeros and (V) is trivial on S^1.)

**(N3) Correct.** Assume u ∈ L^1 and u∘g_{−t} − u = −∫_{−t}^0 f∘g_s ds a.e. Then
⟨Xu, φν⟩ = −⟨u, L_X(φν)⟩ = −(d/dt)|_0 ∫ (u∘g_{−t}) φν = ∫ fφν.
Differentiation under the integral is allowed because the difference quotient (1/t)∫_{−t}^0 f∘g_s converges uniformly to f.
For an invariant ρν, put a = log ρ. Then a∘g_t − a = −J_t, so Xa = −d. If a ∈ L^1, GH makes a smooth, and ρ = e^a is a smooth positive invariant density.

**(N4) Correct.**
- Suppose d − c = Xa with a ∈ D'. Then a is smooth by GH, e^{−a}ν is invariant, and c = 0 (O3).
- The C^m-closure version: use the C^0 case (k = 0) of Lemma 2 on the normalised u_n.
- The duality version: X(C^∞) is closed and equals the annihilator of the space I of invariant distribution densities.

## 2. New (small) results

**(a) Proposition.** Under GH, suppose some absolutely continuous invariant probability ρν has ν-density ρ with ρ^{−ε} ∈ L^1(ν) for some ε > 0. Then (V) holds.

*Proof.*
1. ρ > 0 a.e. by (N1), since {ρ > 0} is invariant and has positive measure.
2. We have |log ρ| ≤ ε^{−1}(ρ^{ε} + ρ^{−ε}).
3. ρ^ε ∈ L^1 by Hölder, because ν is finite and ρ ∈ L^1. So log ρ ∈ L^1.
4. Conclude by (N3). ∎

In particular (V) follows as soon as there is an invariant a.c. probability whose density is bounded below by a positive constant.

**(b) Proposition.** Under GH with dim M ≥ 2, X has no zero or periodic orbit that is a Lyapunov-stable attractor or repeller with an open basin. (For example, it has no hyperbolic sink or source, and no attracting or repelling periodic orbit.)

*Proof.*
1. Let K be such an attractor. Its basin W is open and invariant, so by (N1) it has full volume.
2. Pick a small closed ball A ⊂ W \ K of positive volume, at positive distance from K.
3. Every x ∈ A satisfies g_t x → K, so x returns to A only for t in a bounded set.
4. This contradicts conservativity (N2): Halmos recurrence says a.e. point of A returns to A at arbitrarily large times.
5. For repellers, apply the same argument to −X, which is GH by (O4). ∎

This is strictly more than P1 and Observation P. Those results exclude only zeros with d(p) = 0 and periodic orbits whose return map has Jacobian 1. Saddle-type zeros and saddle periodic orbits are still not excluded.

## 3. The remaining gap, stated exactly

By (N3), (N4) and §2(a), (V) is equivalent to each of the following:
- (G1) some invariant measure ρν ≪ ν has log ρ ∈ L^1(ν);
- (G2) every invariant distribution density T satisfies T(d) = c·T(1).

What is missing is any mechanism that turns GH, which is a statement about the operator X on functions, into regularity information for the transposed operator X + d, which acts on densities. Every invariant object (μ, ρ, a Maharam-invariant function) satisfies an equation of the form Xv = −dv or Xv = −iλdv. The right-hand side is not smooth, so GH does not apply.

**Dead ends checked.**
1. *Truncations.* Replacing a by a_N, or by e^{iλa} or ρ^s, gives X(·) = (bounded measurable function), not a smooth one.
2. *Smoothing.* Friedrichs mollification controls the error of Xρ_ε + dρ_ε only in L^1, never in C^m. So Lemma 2 cannot be invoked.
3. *Time changes.* hX has invariant densities I/h and divergence hd + Xh. Making that divergence vanish is (V) itself, so time changes give nothing new.
4. *The dual estimate (O1).* Applied to μ1 − μ2 for two invariant measures, it is satisfied by S = 0, so it gives no contradiction. For the same reason, unique ergodicity is not obtained here.
5. *Averaging.* The functions u_T = (1/T)∫_0^T J_t dt satisfy Xu_T = A_T d − d. But ||A_T d||_{C^m} is not controlled.

**Literature note (from memory, unverified).** I recall that Forni ("On the Greenfield–Wallach and Katok conjectures", c. 2008) and Kocsard (dimension 3) relate GH to unique ergodicity with a smooth invariant volume. I cannot reconstruct their proofs and do not rely on them.

**Open:**
- (V) itself;
- unique ergodicity under GH;
- the absence of saddle-type zeros under GH.

=== END OF ANSWER round3_q1 ===
