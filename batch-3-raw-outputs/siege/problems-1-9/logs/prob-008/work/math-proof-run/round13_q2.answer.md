# round13_q2: answer

## 0. Verdict
I could **not** prove (PE0), and I found **no counterexample** to it. (PE0) stays open. Below is what this attempt adds:
- §1: the chain checked once more;
- §2: one small new lemma, fully proved (no conformal exponent other than 0 when every invariant measure has mu(d) = 0). It explains why tilted Patterson / conformal-measure constructions (Mechanism E) cannot work unless the cocycle is changed;
- §3: a literature route to the volume case, cited from memory with explicit doubts. It must be checked before anyone relies on it;
- §4: two routes I tried, and why they are dead;
- §5: the open questions, stated explicitly.

Conventions are those of the task file: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi, Gamma_t phi = e^{J_t} (phi o g_t), and (F1) is "T o P = 0 implies T = c nu" (that is, GH through L1).

## 1. The chain
Step 1 (variational principle, ergodic decomposition, Jacobs) and step 3 are elementary and correct. Step 2 (entry 113) depends on the cited Pesin / Ledrappier-Strelcyn / normal-form inputs [NF']. I did not re-derive it, and I have no objection to it. Given (PE0), the chain does derive the claim: h_top(g_t) = |t| h_top(g_1) = 0. I see no gap in the logic of the chain apart from (PE0) itself and the cited inputs of step 2.

## 2. Lemma Z (new, proved): in the "balanced" regime every conformal exponent is 0
**Lemma Z.** Let X be any smooth vector field (GH not needed). Suppose every flow-invariant Borel probability mu has mu(d) = 0. Let T be a nonzero complex Borel measure with T o P = z T for some complex z. Then Re z = 0. Under GH, the only Borel probability m with m o P = c m (for any real c) is nu-hat = nu/nu(M).

*Proof.*
1. For smooth phi, t -> Gamma_t phi is C^1 into C^inf with derivative Gamma_t P phi = P Gamma_t phi. The two expressions agree because both equal d/dt of e^{J_t}(phi o g_t) (direct computation, using J_{t+s}(x) = J_s(x) + J_t(g_s x)).
2. Let m = |T|. By Lemma 1 of Block R9-g (modulus lemma), m o P = c m with c = Re z. Put F(t) = m(Gamma_t 1) = int e^{J_t} dm. Then F'(t) = m(P Gamma_t 1) = c F(t), so F(t) = e^{ct} m(M).
3. By Lemma 3 of [R5-a] (balanced case, proved there), for every eps > 0 there is C_eps with |J_t(x)| <= eps|t| + C_eps for all x and t. Hence e^{ct} m(M) = F(t) <= e^{eps|t| + C_eps} m(M) for all real t. Letting t -> +inf and t -> -inf gives |c| <= eps. Since eps was arbitrary, c = 0.
4. Under GH, a probability m with m o P = 0 is nu-hat by (F1). ∎

**Consequence for Mechanism E (the planner's suggestion (2)).** Suppose the flow has positive entropy and all mu(d) = 0 (this includes the volume case). Then every positive or complex measure that is an eigen-density of P^T is either nu-hat or has eigenvalue 0 and equals c·nu. Patterson sums over exponentially many orbit segments of a positive-entropy measure produce a growth exponent, but by step 3 that exponent cannot show up as a conformal exponent for the cocycle J. So the "second conformal density" can only come from a construction whose Jacobian is exactly e^{J_t} with no normalising exponent. On a horseshoe, Lemma S of Block R12-d provides this through the pressure equation P(G) = P(G - d) and a product of one-sided eigenmeasures. With a centre direction, the transverse factor would itself have to carry the centre part of the Jacobian with exponent 0. Lemma Z says this cannot be arranged by any tilting of the cocycle J alone. It has to be engineered in the centre direction itself, and that is exactly where no Markov structure exists. This narrows Mechanism E but does not refute it.

## 3. A possible literature route to the volume case (cited from memory; NOT verified; flagged)
In the volume case (X preserves a smooth positive density omega), (O2) and the duality consequence of Text A show that X is **cohomology-free**: every smooth f equals omega(f) + Xu with u smooth.

[FP] (cited from memory, uncertain). L. Flaminio and M. Paternain, "Linearization of cohomology-free vector fields", Discrete Contin. Dyn. Syst. (around 2011). My recollection of the abstract is: *"if the vector field is cohomology free, then it can be embedded continuously in a linear flow on an Abelian group."*

**Conditional deduction.** Suppose [FP] gives the following: a continuous injective map Phi: M -> G, with G a compact abelian topological group, and v in Lie(G), such that Phi(g_t x) = Phi(x) + t v. Then:
- Fix a translation-invariant metric on G (one exists for compact metrisable G; if G is not metrisable, use a countable family of characters). Phi is a homeomorphism onto its image because M is compact.
- So the family {g_t} is equicontinuous on M.
- An equicontinuous flow has zero topological entropy. Given eps > 0, pick delta > 0 with d(x,y) < delta implying d(g_t x, g_t y) < eps for all t. Then a finite delta-net is an (n, eps)-spanning set for every n, so h_top(g_1) = 0.

Hence the **volume case of (PE0), and of the problem, would follow**.

**Reasons to doubt the recollection.**
- If such an injective equivariant embedding into a compact group always existed, the flow would be minimal and equicontinuous. M would then be a coset of a compact connected abelian group that is also a manifold, i.e. a torus, with a topologically linear flow. That would be the **topological Katok conjecture** in every dimension. As far as I remember, this is not stated as known: Katok's conjecture is settled only in low dimensions (Kocsard, Forni, F. and J. Rodriguez Hertz for dim 3; cited from memory).
- So either the "embedding" in [FP] is weaker (not injective, a non-compact group, or an embedding of the operator group rather than of M), or my memory is wrong.

I could not reconstruct a proof of equicontinuity from cohomology-freeness (see §4). The orchestrator should check [FP] before relying on it.

[RH] (cited from memory). F. and J. Rodriguez Hertz, "Cohomology free systems and the first Betti number". As I recall, a cohomology-free flow has a smooth factor map onto a Diophantine linear flow on T^{b}, with b = b_1(M) (or related to it).

*Proof idea, verified here.* For an integral basis [beta_i] of H^1(M,Z) mod torsion:
- beta_i(X) - c_i = X u_i, with c_i the omega-average of beta_i(X);
- so beta_i' = beta_i - du_i is closed and beta_i'(X) = c_i;
- integrating the beta_i' gives F: M -> T^b with dF(X) = c.

This gives zero entropy only when F is a finite covering map, for example when b = dim M and the beta_i' are pointwise independent. In general it does not.

## 4. Routes tried here, and why they are dead
(a) **Equicontinuity from the tame inverse (volume case).**
- Let R = X^{-1} on C^inf_0. For x, y, the functional D_{x,y} = (delta_x - delta_y) o R satisfies D_{g_t x, g_t y}(f) = D_{x,y}(f) + int_0^t (f(g_s x) - f(g_s y)) ds.
- The set R(unit ball of C^m_0) is bounded in C^1. But it is not invariant under composition with g_t (u o g_t = R(f o g_t) + const, and ||f o g_t||_{C^m} grows exponentially).
- So no uniform-in-t modulus of continuity follows. Same obstruction as Corollary O (#124).

(b) **Bounded discrepancy plus counting (volume case).**
- Cohomology-freeness gives sup_{x,T} |int_0^T f(g_t x) dt - T omega(f)| <= C||f||_{C^m} for every smooth f.
- Symbolically, though, sequences whose letter counts stay within a band of fixed width W around the mean on every factor have exponential growth rate (the number of +-1/2-step paths confined to a strip of width W grows like (2 cos(pi/(W+2)))^n). So bounded discrepancy at a fixed scale is compatible with positive entropy.
- This is consistent with Theorem B0 of round12_q10. Dead.

(c) **Currents from the centre direction.**
- Take v in E^c(x) at a mu-generic x, where the centre exponent is 0. Patterson normalisation of t -> |Dg_t v| delta_{hat g_t v} gives a measure S on SM, an invariant dimension-1 current C_S, and boundary T_S with T_S o X = 0.
- In the volume case T_S = 0, because T_S(1) = 0 and invariant densities are c·omega. So C_S is a closed invariant dimension-1 current.
- To make it smooth (and so obtain a smooth vector field commuting with X) one needs GH of L_X on closed (n-1)-currents. By de Rham this reduces to functions only when n = 2 (Lemma B of R4-q10 is the degree-1 analogue). For n >= 3 it would need GH of L_X on (n-2)-currents, which GH does not give.
- Dead as it stands. Recorded as (Q-c) below.

## 5. Open questions (explicit)
- **(PE0)** itself: open.
- **(Q-FP)**: check [FP]. If it really gives an equivariant injective continuous map into a compact abelian group, the volume case of (PE0) follows (§3).
- **(V)** (does GH give a smooth invariant volume?): open. Together with (Q-FP) it would settle the problem.
- **(Q-c)**: under GH (or GH plus a volume), is every closed L_X-invariant (n-1)-current smooth? A positive answer would turn zero centre exponents into smooth commuting vector fields (§4(c)). Open.

=== END OF ANSWER round13_q2 ===
