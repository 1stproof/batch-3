# round4_q10: answer (work in progress)

Plan: attempt Statement (C) (GH + smooth invariant volume omega => h_omega(g_1) = 0) in the remaining case
(positive exponent and zero transverse exponent). First record rigorous new lemmas that make
GH usable on non-smooth objects (approach (1) of the query): measurable invariant vector fields, closed currents.
Then test whether they bite in the zero-centre-exponent case.

## Status

I did not prove Statement (C), and I found no counterexample. Below are three rigorously proved lemmas
that let GH act on non-smooth objects, and the exact points where they stop short of (C).

Standing setting: (C)'s hypotheses. X is GH and preserves a smooth positive probability density omega.
We use L1 from the background in the form "an invariant distribution density is c·omega". Proof: T = u·omega
with L_X T = (Xu) omega because div_omega X = 0, so Xu = 0 and u is constant by L1.
Fix a Riemannian metric on M.

## Lemma A (proved). Measurable invariant vector fields are divergence-free.
Let V be a measurable vector field with |V| in L^1(omega) and Dg_t V(x) = V(g_t x) for omega-a.e. x, for each t.
Then ∫ dφ(V) omega = 0 for every smooth φ. That is, div_omega V = 0 in the sense of distributions.

*Proof.* T(φ) := ∫ dφ(V) dω is a distribution of order 1, since |T(φ)| ≤ ||dφ||_∞ ||V||_{L^1}.
We have d(φ∘g_t)_x(V(x)) = dφ_{g_t x}(Dg_t V(x)) = (dφ(V))(g_t x).
So T(φ∘g_t) = ∫ (dφ(V))∘g_t dω = T(φ), by invariance of ω.
As t → 0, (φ∘g_t − φ)/t → Xφ in C^1, so T(Xφ) = 0. Thus T is an invariant distribution density, T = cω,
and T(1) = 0 forces c = 0. ∎

## Lemma B (proved). GH extends to closed 1-currents.
Let α be a closed 1-current (a 1-form with distribution coefficients, dα = 0) such that L_X α is smooth. Then α is smooth.

*Proof.* By de Rham–Hodge theory for currents, α = h + du with h a smooth harmonic 1-form and u in D'.
(A closed current is cohomologous to its smooth harmonic representative, by de Rham's theorem for currents.)
Cartan's formula gives L_X α = d i_X α, and the same for h. So L_X α − L_X h = d(Xu), and this is a smooth exact form.
A distribution w with dw smooth is smooth up to a constant. (Locally dw = β smooth and closed; write β = dw_0 with
w_0 smooth; then d(w − w_0) = 0, so w − w_0 is locally constant.) Hence Xu is smooth. By GH, u is smooth, and so is α. ∎

## Lemma C (proved). Conformal measures on the unit tangent bundle and eigen-distributions.
Let SM be the unit sphere bundle. Define ĝ_t(v) = Dg_t v / |Dg_t v|, A_t(v) = log|Dg_t v|, and
a(v) = d/dt|_{t=0} A_t(v) = ⟨∇_v X, v⟩, which is smooth on SM. The cocycle identity is A_{s+t}(v) = A_t(v) + A_s(ĝ_t v).

(i) There are a Borel probability measure S on SM and a real P with
 ∫ e^{A_t} (Ψ∘ĝ_t) dS = e^{Pt} ∫ Ψ dS for all continuous Ψ and all t ≥ 0.
(ii) P = ∫ a dS, and P lies in [λ_min, λ_max], the range of the Lyapunov exponents of ω (the flow exponent 0 included).
(iii) The distribution T_S(φ) := ∫ dφ(v) dS(v) satisfies T_S(φ∘g_t) = e^{Pt} T_S(φ) and T_S(Xφ) = P·T_S(φ),
 i.e. L_X T_S = −P T_S. Also T_S(1) = 0.
(iv) If P = 0, then T_S = 0, i.e. the 1-current C_S(β) = ∫ β(v) dS(v) is closed.

*Proof.* (i) Let K = Prob(SM) with the weak* topology. K is compact and convex.
Define Φ_t(m)(Ψ) = ∫ e^{A_t} Ψ∘ĝ_t dm / ∫ e^{A_t} dm. This is continuous on K, because e^{A_t} > 0 and both
e^{A_t} and Ψ∘ĝ_t are continuous. The cocycle identity gives Φ_s∘Φ_t = Φ_{s+t}.
By Schauder–Tychonoff, F_k = Fix(Φ_{2^{-k}}) is nonempty and compact. Since Φ_{2^{-k}} = Φ_{2^{-k-1}}∘Φ_{2^{-k-1}},
we have F_{k+1} ⊂ F_k. So ∩F_k is nonempty, and any S in it is fixed by Φ_t for every dyadic t ≥ 0.
The map t ↦ Φ_t(S)(Ψ) is continuous, so S is fixed by every t ≥ 0.
Put c_t = ∫ e^{A_t} dS. Then c_{s+t} = c_t · Φ_t(S)(e^{A_s}) = c_t c_s. Since c is continuous and positive,
c_t = e^{Pt}, and differentiating at t = 0 gives P = ∫ a dS.
(ii) For every t, P = (1/t) log ∫ e^{A_t} dS lies between min_v A_t(v)/t and max_v A_t(v)/t.
Let v_t be a maximiser. Any weak* limit point of the empirical measures (1/t)∫_0^t δ_{ĝ_s v_t} ds is ĝ-invariant;
call it m. Then ∫ a dm = lim (1/t) A_t(v_t). Decompose m into ergodic components. Each component projects to an
invariant measure on M, which is ω by unique ergodicity (O2). By Birkhoff and Oseledets, its integral of a is a
Lyapunov exponent of ω. So lim sup max_v A_t/t ≤ λ_max. The lower bound is symmetric.
(iii) For unit v we have e^{A_t(v)} dφ(ĝ_t v) = dφ(Dg_t v) = d(φ∘g_t)(v). Apply (i) with Ψ(v) = dφ(v).
Then differentiate at t = 0, using (φ∘g_t − φ)/t → Xφ in C^1.
(iv) If P = 0, T_S is an invariant distribution density with T_S(1) = 0, so T_S = 0 as in Lemma A. ∎

## Where this stops (the precise gaps)
Two further statements would be needed to obtain h_ω = 0 by this route, and I could prove neither.
(E1) GH excludes real eigen-distributions: if L_X T = κT with κ real and nonzero, then T = 0.
Diophantine linear flows satisfy E1, by Fourier series.
What I checked: the tame estimate only gives T(Rφ) = T(φ)/κ on mean-zero φ, where R = X^{-1}.
Iterating this produces no contradiction, because R^j loses derivatives as j grows and time rescaling
X → cX (which preserves GH) changes κ arbitrarily.
Flow-direction growth gives |T(φ∘g_{−t})| = e^{−κt}|T(φ)|, which is also consistent.
(E2) Positive exponents force some conformal measure S (on SM, or on a Grassmann/k-vector bundle, by the same
construction with Jacobian cocycles) with T_S ≠ 0.
What fails: S may be symmetric under v ↦ −v, and then T_S = 0 automatically.
If both E1 and E2 held, Lemma C(iii) would contradict GH. Even then this would only show that some S has T_S ≠ 0,
not h_ω = 0 directly, so the route is at best a reduction attempt and is incomplete.
Other checks:
- Suppose C_S happens to be closed while P ≠ 0. Then (g_t)_*C_S = e^{−Pt}C_S, but g_t is isotopic to the
  identity and so acts trivially on homology. Hence the homology class of C_S is 0, i.e. C_S is exact.
  No contradiction arises.
- For (n−1)-currents paired with the invariant form i_Xω, the same construction gives an invariant positive measure,
  hence ω. No information.

## Summary
- **Proved:** Lemmas A, B and C. These are new tools by which GH constrains measurable invariant vector fields,
  closed 1-currents, and conformal measures with P = 0.
- **Not proved:** Statement (C). The case of a positive exponent together with a zero transverse exponent remains open.
- **Open questions:** (E1) and (E2) above, together with the Missing Lemma of R3-q4 and lemma (M) of R-d.

=== END OF ANSWER round4_q10 ===

