kind: attempt
Open question attempted: the missing statement (V) of this attempt's chain (ledger entry 19): global hypoellipticity (GH) forces a smooth invariant volume.

## Statement (V)
Let M be a compact connected smooth manifold and X a smooth vector field on M such that every distribution u in D'(M) with Xu in C^infinity(M) lies in C^infinity(M) (global hypoellipticity, GH). Then there is a smooth density omega on M, positive everywhere, with L_X omega = 0. Equivalently: for one (hence every) smooth positive density nu, div_nu X = Xa for some a in C^infinity(M).

## Results already established in this attempt (statements only; you may use them)
Notation: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (log nu-Jacobian of g_t), I = space of X-invariant distribution densities (T with T(X phi) = 0 for all smooth phi).
- E2. Under GH, every distribution u with Xu = 0 is constant.
- E3. Under GH, for every k there are m, C with ||u - mean(u)||_{C^k} <= C ||Xu||_{C^m} for smooth u; X(C^infinity) is closed and equals the annihilator of I.
- E4. Under GH (dim M >= 2), no periodic orbit has a Poincare return map with Jacobian determinant 1.
- E8. Under GH, at each zero p of X, d(p) != 0.
- E11. Under GH, invariant Borel sets are Lebesgue-null or conull; the flow is conservative (dim M >= 2); any L^1 solution u of u o g_t - u = int_0^t f o g_s ds with f smooth is smooth; and (V) holds iff d - c lies in X(D') for some constant c.
- E12. Under GH, an absolutely continuous invariant probability whose density rho has rho^{-eps} integrable for some eps > 0 gives (V).
- E13. Under GH (dim M >= 2), no zero or periodic orbit is a Lyapunov-stable attractor or repeller with open basin.
- E14. Under GH, (V) holds iff dim I = 1; and (V) implies unique ergodicity, no zeros, no periodic orbits (dim M >= 2), and that every volume-mean-zero smooth function is Xu with u smooth.
- E15. Under GH + a smooth invariant volume omega: h_top = h_omega, and h_omega = 0 whenever omega has no zero transverse Lyapunov exponent (Pesin's formula, Katok's horseshoe theorem for flows); hence zero entropy when dim M <= 3.
- E16 (OPEN, not established). Under GH + a smooth invariant volume omega, omega cannot have a positive Lyapunov exponent together with a zero transverse exponent.

## Task
1. First derive for yourself, step by step, that (V) together with E14, E15 and E16 would prove that the flow of a GH vector field has zero topological entropy (the problem below). If the derivation does not go through, or if (V) looks implausible to you, say so precisely — that is a valuable result.
2. Then attack (V): prove it, or refute it by an explicit GH vector field without smooth invariant volume. Earlier attempts used: local analysis at zeros and periodic orbits; nonsingular ergodic theory (Maharam extension, Krieger type, Hopf ratio theorem, truncations and mollification of log-densities); microlocal propagation of singularities with a commutator construction (found circular); and, in parallel with you, conformal/Patterson measures along orbits, a reduction through unique ergodicity and the Gottschalk-Hedlund theorem, and GH of the transposed operator X + d. Make a FIRST MOVE that none of these used (for instance: a perturbation or index argument in a family of operators; an argument on M x M or on a covering or bundle over M; spectral theory of X - lambda for real or complex lambda near 0; a Baire-category or Fredholm-type argument on the space I; a variational/convexity argument on the set of invariant measures; or anything else you judge better), and pursue it as far as it goes.
A proof of (V) only for a sub-class of vector fields (e.g. uniquely ergodic ones, or low dimension) does not answer the question, though it should be reported, with full proof, if it is all you found. Do not answer by recalling a proof from the literature: reason it out. Deliverable: a complete proof, a counterexample, or the strongest rigorously proved partial result with the exact point where the argument stops.
