# Planner notes (after finalize step; rounds 1-14, refine_2/3, commit wave r3 done)

## Final state
- GOAL (ledger entry 1) remains OPEN; no other [GOAL] line exists, so the main claim of proof.md is the problem itself, NOT PROVED.
- Final proof.md (574 lines) = previous draft (§§0-6, 8 kept, minor verify fixes applied) + NEW §7 replacing the old volume section:
  - Theorem V (GH + smooth invariant density => h_top = 0, all dims, polynomial growth of separated sets). Confirmed independently by r3_q1 and r3_q2; I rechecked every step and the constants (python check of Step B mass/count bounds and Step D exponent conditions). Uses only Lemma 1.1, Lemma 1.4 (statement extended to include the tame estimate), [An], [Bo]. Used linear F = sum of bumps (r3_q2) and crude bump bound rho^{-2m} (r3_q1); K = (2m+1)/(n-1), B = (2m+1)(K+2).
  - §7.4: Corollary 7.10 ((V) => problem), Lemma 7.11 (coboundary criterion), Theorem W ((V) <=> sup_{t>=0,x} J_t < inf ... ), Theorem W' ((V) <=> limsup J_t in L^1). From r3_q3 §§2-4, rechecked.
  - Old Theorem D / Theorem 7.5 / Prop 7.3 / Lemmas 7.2-7.4 dropped (superseded by Theorem V; this also removes verify gap S1).
- Verify report (r3_verify): no fatal errors in old draft; minor fixes applied (dependency summary, numeric 'Check' line replaced by derivation, [KLY] attribution, [NF] local form note, Lemma 1.2 complex constants, Prop 7.1 c(f) = int f dω).

## What remains open
- (V): GH => smooth invariant density. Equivalent under GH to a one-sided uniform bound on J_t (Theorem W). r3_q3 could not prove it; possible literature (Forni 2008, Kocsard) unverified.
- (PE0)/(SC) for the general case in dim >= 4.
- r3_q4: no-go — Anosov flows satisfy all closed-range/tame estimates (Livsic + dLMM), so the Theorem V route must use distributional GH via smallness of the invariant-distribution space I; conditional theorem with dim I < infinity + "no long repeats" (unproved).
