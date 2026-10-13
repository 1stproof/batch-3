# Running summary after round 4 planning (rounds 1-3 folded in) — CONCLUDED

## Interpretation
- "Symplectic SC divisor" = Tehrani-McLean-Zinger (TMZ) sense: components D_i closed symplectic codim-2,
  transverse, every stratum D_I symplectic with symplectic orientation = intersection orientation
  (positivity). Without positivity the answer is NO: round3_q1 §0 gives the explicit example
  D_1={z_2=0}, D_2={z_2 = eps zbar_1} in (C^2, omega_std), 0<eps<1, both symplectic, transverse, negative
  intersection (determinant -eps^2), and the sign is invariant along any path keeping D transverse. The final
  proof must state this convention and may include this example.
- Required: near p in exactly r components, coordinates with z_1..z_r J-holomorphic, D_i={z_i=0};
  z_{r+1..n} merely smooth. Permitted deformation = TMZ deformation to an omega-regularization.

## Standing results (never drop)
- #4 Necessity (round1_q4): ratio of J-holomorphic defining functions extends to nonvanishing
  J-holomorphic function; N_{D_i} gets J|D_i-holomorphic cocycle; generic J fails for n>=3.
- #5 Smooth-case reduction to the line bundle lemma (round1_q4).
- #6 Line bundle lemma in real dim 2, Prop A (round1_q2).
- #7 Lemma A (round1_q3): fibre coordinate of J_nabla holomorphic iff connection form (1,0).
- #10 dim_R M = 4: YES citing TMZ only (round2_q2).
- #11 Disjoint-difference reduction (round2_q1), side result.
- #12 Configuration lemma (round2_q3).
- #13 Assembly theorem (round2_q4).
- #16 [GOAL] PROVED: YES, chain #12 + #13.
- Round-4 entries: two [AUDIT] lines (round3_q1, round3_q2) certifying #16; (AH) proved from
  Donaldson/Auroux (round3_q3, supersedes #14); (R) supplied by TMZ with (R4) by shrinking (round3_q4,
  supersedes #15).

## The proof chain (for the final document)
Part 1, configuration lemma (round2_q3): after a permitted deformation there is a positive SC divisor C
containing D with levels 0..n-1, each component a of level <= n-2 having partners a^+, a^- of the next level
with PD[C_a] = PD[C_{a^+}] - PD[C_{a^-}] integrally. Proof: induction on level; TMZ re-regularization;
Lemma 0 (compatible J_l making all strata exactly complex, via omega-orthogonal splitting); integral class
c_k near k[omega_l], bundle P_k with curvature -2 pi i k(omega_l+eta_k); Donaldson-Auroux sections s_a^+ of
L_a (x) P_k, s_a^- of P_k, all sub-tuples eta-transverse on all old strata (proved in round3_q3 from
[D], [A1], [A2]); new strata near-complex hence symplectic and positive (round3_q3 §4 Lemma).
Part 2, assembly theorem (round2_q4): needed index sets, induction by decreasing |I|, J_I tame on C_I with
(C1) J_I = J_nabla near deeper strata, (C2) holomorphic structures pulled back, (C3) H_{I;a} =
Phi_a^*(O_I(a^+) (x) O_I(a^-)^*) divisor-induced; Lemmas Ch, D, B', F; conclusion via Lemma A.
Repairs to include (from the audits): (1) choose/shrink shallower tube radii after deeper J's are fixed, so
U_{I u b} ∩ U_{I u c} projects into the region where J_{I u b} has K-model form (round3_q1); (2) if
C_{I u a^±} is empty, O_I(a^±) is the trivial bundle with global frame s_{a^±} (round3_q1, round3_q2).
Cited published inputs: TMZ (Tehrani-McLean-Zinger, Adv. Math. 2018) weak homotopy equivalence, deformation
of form omega + d mu supported near D (cohomologous: sketch in round3_q1 §1, round3_q4 §1); Donaldson 1996,
Auroux 1997/2002. round3_q4 notes the assembly uses omega only via Lemma B' (R2' suffices).

## Audit status
Both verify queries returned V2 ("proves YES modulo cited published results, no genuine gap"):
round3_q1 and round3_q2. Remaining hedges are citation-level only: exact TMZ statement/numbering and the
cohomologous clause (which the problem statement itself presupposes), and the combined AH form (now argued
in round3_q3).

## Dead ends / superseded
- RLB_m relative line bundle route (#8): superseded by configuration route (not refuted).
- Lemma C (connection change deformation): unnecessary.

## Open gaps
None blocking. Citation hedges as above; the final document should mark them as cited inputs.

## Target
Goal #16 proved and certified by two verify queries (round3_q1, round3_q2): CONCLUDE this round
(round4_DONE.md). No queries.
