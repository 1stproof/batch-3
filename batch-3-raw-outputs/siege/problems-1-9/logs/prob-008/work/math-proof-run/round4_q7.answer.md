# round4_q7: claim (U), GH implies unique ergodicity

## 0. Plan, and a note on the brief

Plan:
- (a) verify the planner lemmas C–F that I use;
- (b) prove new partial results toward (U)/(V);
- (c) state exactly where the argument stops.

**Note on the brief.** The paragraph headed "THE MISSING STATEMENT (M)" is about L-space knots and lens-space surgeries. It has nothing to do with this problem (vector fields, global hypoellipticity, entropy) and looks like a paste from another task. I ignore it. The task actually worked on here is Claim (U), and then (V).

**Outcome in one line.** I did NOT prove (U) or (V). What I did prove, rigorously:
- a new equivalence: under GH, (V) holds iff the transposed operator P = X + d has closed range on C^∞, iff X(D') is weak*-closed, iff C^∞ ⊂ X(D') + R;
- a sign/dimension lemma: smooth invariant signed densities have constant sign, and they form a space of dimension ≤ 1;
- tilted conformal measures attached to each ergodic measure;
- checks of Lemmas C, D, D1, E and F.

Conventions are those of the brief: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, and P = X + d. Pairing ⟨u, φ⟩ = ∫ uφ ν. Then ∫(Xu)φν = −∫u(Pφ)ν, so the transpose of X on C^∞ is −P, and the transpose of P is −X.

## 1. Verification of the planner lemmas

I checked each lemma line by line.

**Lemma C: correct.**
- The bound c(t) ≥ c(s)e^{−‖d‖|t−s|} follows from (log c)' = d(g_t x).
- Integrability then forces c → 0 at ±∞.
- The boundary identity is ∫_{−R}^{R} c·(Xφ + dφ)(g_t x) dt = [cφ(g_t x)]_{−R}^{R} → 0. So u = T/ν satisfies Xu = 0 (Observation 0), and by L1, T = Kν.
- T is carried by one orbit. An orbit is a ν-null set when dim M ≥ 2, so K = 0, which contradicts T(M) > 0.
- Corollary C1, first sentence: correct, since then ∫e^{J_t} dt < ∞.
- Corollary C1, the heteroclinic/horseshoe claims: only sketched. I have not checked them and do not use them.

**Lemma D: correct.**
- c_s is Lipschitz with (log c_s)' = d(g_t x) − s·sign t, and c_s → 0 at ±∞ as in Lemma C.
- Integrating d/dt[c_s φ(g_t x)] = c_s·(Xφ + dφ − s·sign t·φ)(g_t x) over R gives |T_s(Xφ + dφ)| ≤ s‖φ‖_∞.
- Any weak* limit T is a probability with T(Xφ + dφ) = 0. Hence T = ν̂ by Observation 0 and L1. Compactness then gives convergence of the whole family.
- About the hypothesis: limsup_{|t|→∞} J_t/|t| ≤ 0 is sufficient for P(s) < ∞ for every s > 0, and that is all the lemma uses.

**Corollary D1: correct.**
- Take x ∈ supp μ that is generic in both time directions.
- Then J_t(x)/t → μ(d) = 0 as t → ±∞. The backward limit uses the Birkhoff theorem for g_{−t}.
- Each T_s is supported in the closure of the orbit of x, which lies in supp μ. Their limit ν̂ has full support.

**Lemma E: correct.**
- (i) Under UE, J_t/t → μ(d) uniformly. Combine this with ∫ e^{J_t} dν = ν(g_t M) = ν(M) for every real t.
- (ii) follows from D1.
- (iii) uses the Gottschalk–Hedlund theorem for flows, cited from memory: for a minimal flow on a compact metric space and a continuous d, if sup_{t≥0} |∫_0^t d(g_s x0) ds| < ∞ for one x0, then there is a continuous a with ∫_0^t d∘g_s ds = a∘g_t − a. Then ρ = e^{−a} satisfies ρ∘g_t·e^{J_t} = ρ. So ρν is invariant with a continuous positive density, and R3-q1 §2(a) together with (N3) gives a smooth invariant volume.

**Lemma F: correct.**
- (⇒): P(ρw) = ρXw + w(Xρ + dρ) = ρXw.
- (⇐) uses GH of P for invariant measures, and GH of X through N1.

**A small correction to R3-q1, dead end 4.** S = 0 does *not* solve S(Xu) = μ1(u) − μ2(u). The S given by (O1) is a genuine order-m distribution density with L_X S = μ2 − μ1. Their conclusion still stands: such an S exists and yields no contradiction.

## 2. Two elementary facts about the exponent of d

**Proposition 2.1 (proved).** There are ergodic invariant probabilities μ_+ and μ_− with μ_+(d) ≥ 0 ≥ μ_−(d). This needs no GH.

*Proof.*
1. Standard fact: limsup_{t→+∞} sup_x J_t(x)/t = max_μ μ(d) over invariant probabilities.
   - Take x_t and t → ∞ achieving the sup. The empirical measures (1/t)∫_0^t δ_{g_s x_t} ds have invariant weak* limits μ, and μ(d) equals the limit of J_t(x_t)/t.
   - The maximum is attained at an ergodic measure, since μ ↦ μ(d) is affine and continuous.
2. If max_μ μ(d) < 0, then J_t ≤ −ct on all of M for large t, so ∫ e^{J_t} dν → 0. But this integral equals ν(M) for every t, a contradiction.
3. The case t → −∞ is the same and gives μ_−. ∎

**Proposition 2.2 (tilted conformal measures; proved, assuming only that X is a smooth vector field).** Let μ be ergodic with λ = μ(d). Then there is a Borel probability T with supp T ⊂ supp μ and
T(Xφ + dφ) = λ·T(φ) for all smooth φ.
Equivalently, u = T/ν is a nonnegative measure-distribution with Xu = −λu.

*Proof.*
1. Take x μ-generic in both time directions. Then J_t(x) − λt = o(|t|) as t → ±∞. For t < 0 this holds because J_t = −∫_t^0 d∘g_s ≈ λt.
2. So c_s(t) = e^{J_t(x) − λt − s|t|} is integrable for every s > 0 and tends to 0 at ±∞, as in Lemma C.
3. Integrating d/dt[c_s φ(g_t x)] = c_s·(Xφ + dφ − λφ − s·sign t·φ) shows that the normalised measures T_s satisfy |T_s(Xφ + dφ − λφ)| ≤ s‖φ‖_∞.
4. Take a weak* limit as s → 0. The support claim holds because supp T_s lies in the orbit closure of x, which lies in supp μ. ∎

When λ = 0 this is Lemma D, and GH then forces T = ν̂. When λ ≠ 0, GH does not visibly exclude a positive eigen-distribution Xu = −λu. This is one of the places where I am stuck (see §4).

## 3. New reduction: (V) is equivalent to closed range of the transposed operator

Let K = {ρ ∈ C^∞(M; R) : Pρ = 0}. Since L_X(ρν) = (Pρ)ν, K is the space of smooth X-invariant signed densities ρν.

For ρ ∈ K, invariance holds pointwise: ρ(g_t x)·e^{J_t(x)} = ρ(x). To see this:
- d/dt g_t^*ν = g_t^*(dν) gives g_t^*ν = e^{J_t}ν;
- d/dt g_t^*(ρν) = g_t^*(L_X(ρν)) = 0.

**Lemma 3.1 (sign lemma; proved under GH).** Every ρ ∈ K has constant sign, and dim K ≤ 1.

*Proof.*
1. By the pointwise identity, U_+ = {ρ > 0} and U_− = {ρ < 0} are open and invariant.
2. By N1 each is ν-null or ν-conull. They are disjoint, so at least one is null. A null open set is empty, so ρ has constant sign.
3. Now suppose ρ1, ρ2 ∈ K are linearly independent. Changing signs, assume ρ1 ≥ 0, ρ2 ≥ 0, and both are nonzero.
4. Let t* = sup{t ≥ 0 : ρ1 − tρ2 ≥ 0}. This is finite because ρ2(y) > 0 at some y, and ρ1 − t*ρ2 ≥ 0 by closedness.
5. For t > t*, ρ1 − tρ2 ∈ K is not ≥ 0, so by constant sign it is ≤ 0. Letting t ↓ t* gives ρ1 − t*ρ2 ≤ 0.
6. Hence ρ1 = t*ρ2, which contradicts independence. ∎

**Theorem 3.2 (proved; uses GH and the closed range theorem for Fréchet spaces, cited from memory).** Let M be compact and connected, and assume X is GH. The following are equivalent:
- (a) (V): X preserves a smooth positive density.
- (b) P = X + d : C^∞ → C^∞ has closed range. Equivalently, L_X has closed range on smooth densities.
- (c) X(D') is weak*-closed in D'.
- (d) C^∞ ⊂ X(D') + R, i.e. for every smooth f there is a constant c with f − c = Xu for some distribution u.

**Cited theorem** (closed range theorem, Fréchet version). Let A : E → F be a continuous linear map between Fréchet spaces. If A(E) is closed, then A'(F') = (ker A)^⊥; in particular A'(F') is weak*-closed. Also, for any continuous A, the bipolar theorem gives: the weak*-closure of A'(F') equals (ker A)^⊥.

*Proof of the theorem.*

**(a)⇒(b).** If ω = ρν is smooth, positive and invariant, then P(ρw) = ρXw. Multiplication by ρ is a topological isomorphism of C^∞, and X(C^∞) is closed (Text A, L2). So P(C^∞) = ρ·X(C^∞) is closed.

**(b)⇒(c).** Apply the cited theorem to A = −P on E = F = C^∞. Its transpose, with respect to the ν-pairing, is X : D' → D'. So X(D') = K^⊥ := {f ∈ D' : ⟨f, ρ⟩ = 0 for all ρ ∈ K}, which is weak*-closed.

**(c)⇒(d).**
1. By the bipolar statement, X(D') = K^⊥, because the pre-annihilator of X(D') is {φ : Pφ = 0} = K.
2. By Lemma 3.1, K = 0 or K = Rρ with ρ ≥ 0 and ρ ≠ 0.
3. Suppose K = 0. Then X(D') = D' ∋ 1, so Xu = 1 for some u ∈ D'. GH makes u smooth, and at a maximum point of u we get Xu = 0 ≠ 1. This is a contradiction.
4. So K = Rρ, and ⟨1, ρ⟩ = ∫ρν > 0. For smooth f, put c = ⟨f, ρ⟩/⟨1, ρ⟩. Then f − c ∈ K^⊥ = X(D').

**(d)⇒(a).** Apply (d) to f = d: d − c = Xa with a ∈ D'. GH makes a smooth, and (O3) shows that e^{−a}ν is a smooth invariant positive density. ∎

**Remarks.**
1. With Lemma F, (V) ⇔ P is GH ⇔ P has closed range on C^∞ ⇔ X has closed range on D'. GH supplies exactly the "dual" halves of these: closed range of X on C^∞, and (by (O1)) P(D') = {τ : ⟨τ, 1⟩ = 0}. The missing halves are the regularity and closed-range statements for P on C^∞.
2. By (d)⇒(a), already "C^∞ ⊂ X(D') + R" gives (V), and with it (U). So (U) and (V) would follow from a *solvability in distributions* statement, with no regularity needed. Conversely, (U) under GH is equivalent to: for every smooth f there is c with μ(f) = c for all invariant probabilities μ. This is weaker than (d), since (d) controls all invariant distributions.

**Corollary 3.3 (proved).** Assume GH and that (V) fails. Then either
- (α) K = 0, and X(D') is weak*-dense in D' but not closed; or
- (β) K = Rρ with ρ ≥ 0 smooth and Z = {ρ = 0} a nonempty closed invariant ν-null set. In this case the flow is not uniquely ergodic: Z carries an invariant probability that differs from ρν/∫ρν. Also log ρ ∉ L^1(ν), by Lemma B.

*Proof.*
- If K = Rρ with ρ > 0 everywhere, then (V) holds. So in case K = Rρ we must have Z ≠ ∅.
- In case K = 0, the bipolar theorem shows that X(D') is weak*-dense, and it is not closed by Theorem 3.2. ∎

So (U) would rule out (β). A proof of (V) from (U) would then still have to rule out (α).

**Addendum to (β) (proved, citing the Malgrange preparation theorem from memory).** In case (β), ρ vanishes to infinite order at some point of Z.

*Proof.*
1. Suppose ρ vanished to finite order at every point of Z.
2. At each z ∈ Z some directional derivative ∂_v^N ρ(z) is nonzero. Malgrange preparation then writes, near z, ρ = q·(x_n^N + a_{N−1}(x')x_n^{N−1} + … + a_0(x')), with q smooth and nonvanishing and the a_j smooth.
3. For monic polynomials of fixed degree with bounded coefficients, ∫_{−1}^{1} log|p(s)| ds is bounded below. So log ρ ∈ L^1 near z.
4. By compactness of Z, log ρ ∈ L^1(ν). Lemma B then gives (V), which contradicts the standing assumption of Corollary 3.3. ∎

## 4. Where the attempt on (U) stops

Every object that GH controls is a solution of X·(something) = smooth. Through Observation 0 these are ν-conformal objects: Lemma C, Lemma D, D1, N1, N2, and the weighted ratio limits. Invariant measures are instead solutions of P·w = 0. Theorem 3.2 shows that the bridge between the two is exactly a closed-range or solvability property of X on D' (equivalently of P on C^∞), and GH does not give that.

Concretely, to prove (U) along the routes I tried, one would need one of the following, and I could prove none of them:
1. **(Eigen-distribution exclusion.)** Under GH, no nonzero nonnegative measure-distribution u satisfies Xu = −λu with λ ≠ 0. By Proposition 2.2 this would force μ(d) = 0 for every ergodic μ. Then D1 gives full support of all ergodic measures, and hence minimality (every closed invariant set carries an ergodic measure of full support).
   - Even granted this, a second statement is needed: two distinct ergodic measures, both of full support and both with μ(d) = 0, cannot coexist under GH. Lemma D shows that J-weighted orbit averages from either measure's generic points converge to ν. That is consistent with the unweighted averages converging to different μ_i, provided J_t(x) fluctuates by o(|t|) but unboundedly. I found no contradiction in this.
2. **(Solvability.)** C^∞ ⊂ X(D') + R, i.e. (d) of Theorem 3.2. This would give (V), and hence (U). The natural candidates for distribution solutions are:
   - u = ∫_0^∞ f∘g_t dt in D', which needs decay of correlations;
   - orbit measures as in Lemma C, which have δ-type right-hand sides;
   - limits of the resolvents R_s f = −∫_0^∞ e^{−st} f∘g_t dt, which satisfy (X − s)R_s f = f with ‖sR_s f‖_∞ ≤ ‖f‖_∞, but are not controlled in D' as s → 0.

   None of these converges without information that GH does not visibly supply.
3. **(Dual estimate.)** (O1) gives S with L_X S = μ2 − μ1 of order m. This is a genuine object (it is not S = 0, contrary to R3-q1), but its existence is consistent with non-unique ergodicity, so it gives no contradiction.

## 5. On the chain

- I re-checked steps 2–3 of the chain as quoted, given (V):
  - (O2) gives UE, no zeros and no periodic orbits;
  - the duality consequence gives H;
  - in dim 2, the single transverse exponent is 0;
  - in dim 3, the transverse exponents are λ and −λ, so Katok's theorem (C^{1+α} flows, cited) applies.

  I found no flaw. The chain still needs (V) and R3-q4's Missing Lemma for dim ≥ 4.
- (U) alone does not give (V). By Lemma E, under (U) the statement (V) is equivalent to boundedness of J_t(x0) for t ≥ 0. By Corollary 3.3 it is also equivalent to excluding case (α), i.e. to closedness of X(D').

## 6. Summary

**Proved:**
- Lemmas C, D, D1, E, F are verified. The heteroclinic part of C1 is not checked and not used.
- Proposition 2.1: some ergodic μ has μ(d) ≥ 0 and some has μ(d) ≤ 0.
- Proposition 2.2: tilted conformal measures.
- Lemma 3.1: smooth invariant signed densities have constant sign and form a space of dimension ≤ 1 under GH.
- Theorem 3.2: under GH, (V) ⇔ P has closed range on C^∞ ⇔ X(D') is weak*-closed ⇔ C^∞ ⊂ X(D') + R.
- Corollary 3.3 with its addendum: if (V) fails, either K = 0, or K = Rρ with ρ vanishing to infinite order on a nonempty invariant null set, and in that case the flow is not uniquely ergodic.

**Open:**
- Claim (U), i.e. unique ergodicity under GH.
- (V).
- In particular, under GH:
  - excluding positive eigen-distributions Xu = −λu with λ ≠ 0;
  - excluding two distinct full-support ergodic measures with μ(d) = 0;
  - proving closedness of X(D').
- The downstream Missing Lemma of R3-q4.

=== END OF ANSWER round4_q7 ===
