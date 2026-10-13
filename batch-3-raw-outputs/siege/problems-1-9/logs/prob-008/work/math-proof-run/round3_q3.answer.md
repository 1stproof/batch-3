# round3_q3: answer (partial; the core is NOT settled)

Plan: check the facts F1–F3 listed in the query, try directions (i) and (ii), and record what is proved and what fails.

## 1. Correction: (F2) is false as stated
(F2) claims that x -> I_T f(x) := ∫_0^T f(g_t x) dt is Lipschitz with a constant that does not depend on T. But I_T f = u∘g_T − u, so
Lip(I_T f) ≤ Lip(u)·Lip(g_T) + Lip(u),
and Lip(g_T) is exactly the quantity that grows exponentially when entropy is positive (Ruelle's inequality). The identity gives no bound uniform in T. The correct uniform statement is only the C^0 bound P1/F1:
|I_T f − Tω(f)| ≤ 2C_0‖f‖_{C^m}.
Direction (i), as proposed, depends on F2, so it collapses. Writing out the same difference along two orbits gives
u_i(g_t x) − u_i(g_t y) = [u_i(x) − u_i(y)] + ∫_0^t (f_i(g_s x) − f_i(g_s y)) ds.
This is a tautology, and its integral term is bounded only by 2 sup|u_i|. That bound is O(1), not O(d(x,y)). So it gives no control of separation at scales below the diameter.

## 2. Verified: (F1) gives polynomial uniform return times. Dead end for entropy
**Lemma R (proved).** There are m and C such that, for every z and every ε < 1, every orbit segment of length T ≥ C ε^{-m-n} meets B(z,ε). Here n = dim M.

*Proof.* Take a bump function f with 0 ≤ f ≤ 1, support in B(z,ε), f = 1 on B(z,ε/2), and ‖f‖_{C^m} ≤ C ε^{-m}. Then ω(f) ≥ c ε^n. By P1, ∫_0^T f(g_t x) dt ≥ T c ε^n − 4C_0 C ε^{-m}, and this is > 0 once T ≥ C' ε^{-m-n}. ∎

**Why this is a dead end (checked).** Polynomial return times do not imply zero entropy. In a minimal uniquely ergodic subshift with entropy h > 0, a cylinder of length k has measure about e^{-hk}. The metric ball of radius ε = 2^{-k} is such a cylinder, and its return time is about e^{hk} = ε^{-h/log 2}. That is polynomial in 1/ε. Uniform discrepancy at the level of one-point statistics (visit frequencies of balls) is therefore compatible with positive entropy. Entropy is a statement about the *order* of visits, i.e. about joint statistics of (g_t x, g_{t+s} x). Those statistics involve the functions a·(b∘g_s), whose C^m norms grow like e^{mLs}. This is the same loss of derivatives as dead end 4 of R-c. So direction (ii) only goes through if one can control visit patterns at scale ε over time T using a fixed number of smooth observables. Pigeonholing over ~e^{hT} separated segments needs about e^{hT} distinct test functions, and the O(ε^{-m}) error then accumulates. I could not close this gap.

## 3. Attempted route via periodic orbits and invariant non-smooth functions (GH only)
Suppose γ is a hyperbolic periodic orbit with Poincaré map P (positive entropy plus a hyperbolic measure gives such orbits by Katok's horseshoe theorem, cited from memory, for C^{1+α} flows). Take a 1-dimensional unstable eigenvalue λ_u > 1 and stable eigenvalue 0 < λ_s < 1. Then w = y_u^{2k} |y_s|^b, with b = 2k log λ_u / |log λ_s|, is invariant under the linear P. It is continuous, and it is not smooth if b is not an even integer. This would produce a non-smooth distribution solution of Xu = 0 locally. **Obstruction (checked):** w is singular along the whole local unstable manifold {y_s = 0}. Cutting off with χ gives Xu = (Xχ)w, which is singular where supp Xχ meets W^u(γ). Every function of w that is nonzero near γ is also nonzero along the axes, which leave the box. So no global distribution with smooth Xu results. Distributions supported on γ (transverse derivatives of δ) satisfy Xu = 0 only under the resonance Π|λ_i|^{α_i+1} = 1, which is not available in general. The no-volume case already appears in R-b (∫_γ d = 0).

## 4. Status
- Proved here: Lemma R. Also the correction that F2 is false, together with the reason (Lip(g_T) enters).
- Not proved: the core claim. It remains open in this run that H (+GH) implies h_ω = 0, i.e. that ω has no positive Lyapunov exponent.
- Precise missing lemma (equivalent to (M) of R-d, restated): *if g_t preserves a smooth volume ω with h_ω > 0, then for every m, sup over smooth mean-zero f of ‖P_ε f‖_{L²} / (ε‖f‖_{C^m}) = ∞ as ε → 0.* Equivalently: some C^∞ observable has ergodic integrals ∫_0^T f∘g_t that are not uniformly bounded (for instance, it has positive Green–Kubo variance). Proving this needs a CLT-type, or merely unbounded-deviation, result for smooth observables of general nonuniformly hyperbolic volume-preserving flows. I do not know such a result in that generality.
- Dead ends added: (a) direction (i), because it relies on the false F2; (b) direction (ii) through one-point discrepancy, by the subshift example; (c) local invariant functions at hyperbolic periodic orbits, because cut-offs fail along W^u.

=== END OF ANSWER round3_q3 ===
