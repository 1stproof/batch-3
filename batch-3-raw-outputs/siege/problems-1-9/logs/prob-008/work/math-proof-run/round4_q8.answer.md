# round4_q8: attempt on Claim (B) (GH + unique ergodicity => bounded Jacobian cocycle / smooth invariant volume)

## 0. Preliminary remark on the brief
The task file contains a paragraph headed "THE MISSING STATEMENT (M)" about hyperbolic L-space knots and surgeries S^3_{2g-1}(K).
It has nothing to do with the problem (vector fields, GH, entropy) and is evidently pasted in from a different task.
I ignore it. The task I work on is Claim (B) as stated in the brief.

## Plan (written first, updated as I go)
1. Check planner Lemmas C, D, E, F (used below).
2. Prove new reformulations of (V)/(B) under GH+UE (closed-range of X+d; resolvent-type approximate transfer functions F_s = log P_s).
3. Try to close the gap; record exactly where each route stops.

Conventions as in the brief: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds,
nu^ = nu/nu(M), I = space of X-invariant distribution densities, K_s = {rho in C^infinity : X rho + d rho = 0}
(smooth signed invariant densities rho nu). "(V)" = X preserves a smooth positive density.

## 1. Check of the planner lemmas C-F (all verified)

- **Lemma C: correct.** c(t) = e^{J_t(x)} satisfies c' = d(g_t x) c, so c(t) >= c(s) e^{-||d|| |t-s|}. Hence integrability forces c -> 0 at +-infinity. Then T(X phi + d phi) = lim [c(t) phi(g_t x)]_{-R}^{R} = 0. So u = T/nu satisfies Xu = 0, u is constant by L1, and T = K nu with K > 0. But T is carried by an orbit, which is nu-null when dim M >= 2. Contradiction. The zero and periodic cases are as stated.
- **Lemma D: correct.** Integration by parts gives |T_s(X phi + d phi)| <= s ||phi||_infinity. Any weak* limit is a probability T with T(X phi + d phi) = 0, so T = nu^ (Observation 0 + L1). Compactness then gives convergence of the whole family.
- **Lemma E: correct.**
  - (i) int e^{J_t} d nu = nu(M), and under UE J_t/t -> mu(d) uniformly.
  - (ii) Under UE, J_t(x)/|t| -> 0 uniformly as t -> +-infinity for every x. So Lemma D applies to every x, and nu^ (full support) is a weak* limit of measures carried by the closure of the orbit of x. Hence every orbit is dense (this is slightly more direct than going through D1).
  - (iii) If J_t = a o g_t - a with a continuous (Gottschalk-Hedlund, cited), then rho = e^{-a} satisfies rho o g_t e^{J_t} = rho. So rho nu is invariant, log rho is bounded, and N3 makes it smooth.
- **Lemma F: correct.** If K_s contains rho != 0, then {rho > 0} and {rho < 0} are open invariant sets. By N1 one of them is nu-null, hence empty. So WLOG rho >= 0. Positivity everywhere needs UE (or the argument of F): Z = {rho = 0} is closed and invariant, so if Z is nonempty it carries an invariant probability, which under UE is rho nu / int rho nu, and that gives Z measure 0.

## 2. New results (all proved)

Throughout, assume GH, dim M >= 2, and UE with invariant probability mu. By Lemma E the flow is minimal, X has no zeros and mu(d) = 0.

### Proposition 1 (positivity is free). Under GH+UE, K_s != 0 implies (V). More generally, if mu = rho nu with rho continuous, then (V) holds.
*Proof.*
1. Take rho in K_s, rho != 0. Then rho nu is a signed invariant measure, so by UE it equals c mu with c != 0.
2. Hence mu = rho' nu with rho' continuous and rho' >= 0.
3. Z = {rho' = 0} is closed and invariant. If Z were nonempty it would carry an invariant probability, which must be mu. But mu(Z) = int_Z rho' nu = 0. So Z is empty.
4. Thus rho' > 0 is continuous on a compact manifold, so log rho' is bounded, hence in L^1. By N3 (Lemma B of R3-q2), rho' is smooth and rho' nu is a smooth invariant volume. ∎

### Proposition 2 (closed-range reformulation). Under GH+UE, (V) holds iff (X+d)(C^infinity) is closed in C^infinity.
Here X + d acting on functions is exactly L_X acting on densities phi nu, and it is minus the transpose of X with respect to the nu-pairing.

*Proof.*
- (=>) Suppose omega = rho nu is invariant and smooth with rho > 0. Then X rho = -d rho, so (X+d)(rho w) = rho Xw. Hence (X+d)(C^infinity) = rho X(C^infinity), which is closed by Text A/B.
- (<=) Put A = X + d : C^infinity -> C^infinity. Suppose A has closed range, and suppose (V) fails. By Proposition 1, ker A = K_s = 0.
  - A is a continuous injection of the Fréchet space C^infinity onto the closed (hence Fréchet) subspace R = A(C^infinity). By the open mapping theorem, A^{-1}: R -> C^infinity is continuous.
  - So the functional l(A phi) := int phi nu is continuous on R. By Hahn-Banach it extends to a continuous functional on C^infinity, i.e. a distribution density, written u nu with u in D'.
  - Then for every phi, <u, (X phi + d phi) nu> = int phi nu. The left side is -<Xu, phi nu>, so Xu = -1 in D'.
  - By GH, u is smooth. At a maximum point x of u we get (Xu)(x) = 0 != -1. Contradiction. ∎

### Proposition 3 (what failure of (V) forces). Assume GH+UE and that (V) fails. Then:
(a) For every m there is a smooth phi with int phi nu = 1 and ||(X+d)phi||_{C^m} <= 1/m. In other words, there are smooth densities of total mass 1 that are almost invariant in the C^infinity topology.
(b) Any such sequence phi_n (int phi_n nu = 1, (X+d)phi_n -> 0 in C^infinity) satisfies ||phi_n||_{C^1} -> infinity.
(c) X(D') is weak*-dense in D' but does not contain 1. Moreover X(D') ∩ C^infinity = X(C^infinity).

*Proof.*
(a) By Proposition 1, K_s = 0, so the functional l(A phi) = int phi nu is well defined on R = A(C^infinity). If it were bounded by C ||.||_{C^m} on R for some m, then Hahn-Banach would extend it to C^infinity, and the proof of Proposition 2 would give a distribution u with Xu = -1, contradicting GH. So l is unbounded for every C^m seminorm.

(b) Suppose a subsequence is bounded in C^1. By Arzelà-Ascoli a further subsequence converges in C^0 to some phi. Then:
- int phi nu = 1;
- (X+d)phi = 0 in D', i.e. phi nu is a signed invariant measure, so phi nu = mu;
- hence mu has a continuous density, and Proposition 1 gives (V). Contradiction.

(c) The weak*-closure of X(D') is the annihilator of the kernel of the transpose, i.e. of K_s = 0. So X(D') is dense. It does not contain 1 by GH plus the maximum argument above. The last equality is GH. ∎

So under (not V), the obstruction is concrete: the mass functional is not continuous on the range of L_X. Equivalently, there are C^infinity-almost-invariant smooth densities of mass 1, and they necessarily blow up in C^1.

### Proposition 4 (canonical approximate transfer functions; reformulation of (B)).
For s > 0 put P_s(x) = int_R e^{J_t(x) - s|t|} dt and F_s = log P_s. Under GH+UE:
(i) P_s is finite, positive and continuous. Moreover int P_s d nu = 2 nu(M)/s, and (s/2) P_s nu^ -> mu weak* as s -> 0.
(ii) Along orbits F_s(g_r x) - F_s(x) = -J_r(x) + eps, with |eps| <= s|r|. Distributionally X F_s = -d + E_s, where E_s is continuous and ||E_s||_infinity <= s.
(iii) If (V) holds with omega = rho nu, then F_s - log(2/s) -> log rho + const uniformly.
(iv) Conversely, (V) holds as soon as, for some sequence s_n -> 0 and constants c_n, the sequence F_{s_n} - c_n is bounded in L^1(nu), or merely bounded in some Sobolev space H^{-sigma}.

*Proof.*
(i) Finiteness and continuity:
- UE gives |J_t(x)| <= C_eps + eps|t| uniformly in x. So for eps < s the integrand is dominated by C e^{(eps-s)|t|}.
- Continuity then follows by dominated convergence.

Mass identity: int e^{J_t} d nu = nu(M) (change of variables), and integrating over t gives the formula.

Almost invariance: P_s nu = int e^{-s|t|} (g_t)_* nu dt, since int phi e^{J_t} d nu = int phi o g_{-t} d nu. Hence
L_X(P_s nu) = int e^{-s|t|} (-(d/dt)(g_t)_* nu) dt = -s int sign(t) e^{-s|t|} (g_t)_* nu dt,
which has total variation <= s int P_s nu. So the probability measures (s/2)P_s nu^ are almost invariant, every weak* limit is invariant, and by UE it equals mu.

(ii) By the cocycle identity, P_s(g_r x) = e^{-J_r(x)} int e^{J_tau(x) - s|tau - r|} d tau. Since | |tau - r| - |tau| | <= |r|, the stated bound follows. Differentiating in r at r = 0:
X P_s = -d P_s + s Q_s, with Q_s(x) = int sign(t) e^{J_t(x) - s|t|} dt and |Q_s| <= P_s.
So E_s = s Q_s / P_s is continuous with |E_s| <= s. Because F_s is differentiable along orbits with continuous derivative, the distributional derivative X F_s equals the orbit derivative (as in N3).

(iii) Write J_t = a o g_t - a with a = -log rho smooth. Then s P_s(x) = e^{-a(x)} s int e^{a(g_t x) - s|t|} dt.
- Under UE, Abel means converge uniformly whenever Cesàro means do: s int_0^infinity e^{-st} psi(g_t x) dt = s^2 int_0^infinity e^{-st} (int_0^t psi o g) dt.
- The same holds backward in time.
- Hence s P_s -> 2 e^{-a} mu(e^{a}) uniformly.

(iv) L^1 is contained in H^{-sigma} for sigma > n/2. A bounded sequence in the Hilbert space H^{-sigma} has a weakly convergent subsequence, converging to some F. Since X F_{s_n} = -d + E_{s_n} -> -d uniformly, we get XF = -d in D'. GH makes F smooth, and then e^{F} nu is invariant (O3). ∎

**Remark.** Proposition 4 recasts (B) as follows: the logarithms of the densities of the canonical smooth-in-time approximants (s/2)P_s nu^ of mu must stay bounded modulo constants in some negative Sobolev norm. This is again the log-integrability condition N3, now attached to a canonical family. GH controls X F_s only in C^0 (|E_s| <= s). The a priori estimates of GH need C^m control. This is exactly the derivative-loss gap (N4) seen from another side.

### Proposition 5 (dual picture of the almost-invariant densities). Assume GH+UE and not (V). Let phi_n be as in Proposition 3(a), with eps_n = ||(X+d)phi_n||_{C^0} -> 0. Let m be such that ||w||_{C^0} <= C ||Xw||_{C^m} for nu-mean-zero smooth w (Text B, Lemma 2 with k = 0). Then phi_n nu = T_n + S_n with:
- T_n in I ∩ (C^m)';
- ||S_n||_{(C^m)'} <= C eps_n;
- T_n(1) -> 1.

*Proof.*
1. For smooth w, phi_n nu(Xw) = -int w (X+d)phi_n nu. Its absolute value is at most eps_n nu(M) ||w - c(w)||_{C^0}, because X c = 0. By Lemma 2 this is at most C eps_n ||Xw||_{C^m}.
2. Extend the functional Xw -> phi_n nu(Xw) from X(C^infinity) to C^m by Hahn-Banach, with the same norm. Call the extension S_n. Then T_n := phi_n nu - S_n annihilates X(C^infinity), i.e. T_n lies in I.
3. Finally T_n(1) = 1 - S_n(1), and |S_n(1)| <= C eps_n. ∎

**Consequence.** If I ∩ (C^m)' were one-dimensional (= R mu), then phi_n nu -> mu in (C^m)'. Under not (V), however, I ∩ (C^{m'})' must contain some T with T(d) != 0 for m' large, by the duality of Text A. I could not turn this into a contradiction.

## 3. Where the argument stops (exact gap)

Every reformulation above reduces (B) to one of the following equivalent statements. Under GH+UE each is equivalent to (V), by Propositions 1-4, N3 and Lemma A.
- (G-a) The range of L_X on smooth densities, (X+d)(C^infinity), is closed. Equivalently there is an a priori estimate ||phi||_{C^k} <= C ||(X+d)phi||_{C^m} for X+d, the transpose of X.
- (G-b) The mass functional phi -> int phi nu is C^m-continuous on (X+d)(C^infinity) for some m.
- (G-c) mu has a continuous density, or more generally a density with integrable logarithm.
- (G-d) The canonical approximate transfer functions F_s = log P_s stay bounded mod constants in some H^{-sigma} as s -> 0.
- (G-e) dim I = 1 (Lemma A).

The common obstruction: GH gives estimates for X (Text A/B), losing derivatives. The objects carrying the obstruction (mu, I, F_s, phi_n) satisfy equations for the transpose X + d, or equations for X with right-hand sides controlled only in C^0 (|E_s| <= s; (X+d)phi_n small only after blow-up of phi_n in C^1). No step converts C^0-smallness into C^m-smallness without controlling derivatives of g_t. That control is equivalent to (B) itself, or to the Missing Lemma of R3-q4. The equidistribution tension (Lemma D: weighted orbit averages tend to nu^; UE: unweighted ones tend to mu) is not contradictory by itself. It occurs, as far as I know, for minimal circle diffeomorphisms with Liouville rotation number and singular invariant measure (statement from memory, not used). There it is GH that should fail, and the mechanism that makes GH fail (Liouville small divisors) is not visible in the soft estimates.

**Dimension 2 (only a reduction, partly from memory).** Under GH+UE with dim M = 2, the flow is minimal without zeros, so chi(M) = 0. The Klein bottle carries no minimal flow (Kneser, cited from memory), so M = T^2. A minimal flow on T^2 has a closed global transversal, so up to a smooth time change it is a suspension of a C^infinity circle diffeomorphism F with irrational rotation number alpha. (B) then holds iff F preserves a smooth positive measure, i.e. iff F is C^infinity-conjugate to R_alpha. By the Herman-Yoccoz theorem (cited), this holds if alpha is Diophantine. So in dimension 2, (B) reduces to: "if the suspension is GH then alpha is Diophantine, or F is conjugate to R_alpha". I did not prove this. The Liouville case with F not conjugate to R_alpha is the obstacle.

**On the chain.** I found no flaw in steps 1-3 of the chain. Given (V), observation (O2) gives UE together with the full cohomological package H, as stated. I note only that (V) is equivalent to closed range of the transpose L_X (Proposition 2), so step 1 is genuinely a statement about L_X, not about X.

## 4. Status
- **Proved:**
  - verification of planner Lemmas C-F;
  - Propositions 1-5: under GH+UE, (V) is equivalent to each of (G-a)-(G-d), and the failure of (V) forces C^infinity-almost-invariant mass-one densities that blow up in C^1;
  - positivity of a continuous invariant density is automatic.
- **Not proved:** Claim (B) itself. No counterexample was found either. A counterexample would also be a counterexample to the Greenfield-Wallach conjecture (from memory, GW predicts that GH fields are smoothly conjugate to Diophantine linear flows on tori, which preserve volume), so none should be expected.
- **Open questions:**
  1. (B), equivalently (G-a)-(G-e) under GH+UE.
  2. Whether GH forces I ∩ (C^m)' to be finite-dimensional for each m.
  3. In dimension 2: whether GH of a suspension forces a Diophantine rotation number.
- **Literature (from memory, unverified, not used):** I believe Forni (c. 2008) and Kocsard treat "GH ⟹ smooth invariant volume / cohomological rigidity" in connection with the Greenfield-Wallach and Katok conjectures. I could not reconstruct their arguments.

=== END OF ANSWER round4_q8 ===
