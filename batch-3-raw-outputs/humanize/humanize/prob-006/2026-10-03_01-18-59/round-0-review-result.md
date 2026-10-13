# Round 0 Review Result

Reviewer: Kimi-k3 (max effort). Scope: plan.md, problem.tex, solution.tex,
goal-tracker.md, round-0-contract.md, round-0-summary.md, git history, and a
fresh independently-run build audit.

## Verdict

Mainline Progress Verdict: ADVANCED

The question in `problem.tex` ("Does a 3-manifold obtained by Dehn surgery on
an L-space knot have at most two prime summands?") is answered affirmatively
and the answer is fully proved in `solution.tex` modulo explicitly and
precisely declared external theorems, which is exactly what plan AC-2
requires. The proof is mathematically correct; I verified every load-bearing
step line by line (see "Mathematical audit" below). The document compiles
cleanly (re-run by me: 2x pdflatex, no errors, no undefined references,
7 pages <= 16, only allowed packages, no markdown/workflow text).
No mainline gap, no blocking side issue. A small set of
accuracy/consistency issues remains; all are queued, none touches the
logical chain. Round-1 task created in the goal tracker for those fixes.

## Goal Alignment Summary

ACs: 5/5 addressed | Forgotten items: 0 | Unjustified deferrals: 0

Capability anchor: N/A (plan has no Feature Map / Capability Map) | Dependency gaps: 0 | Scope drift: no

## Part 1 -- Implementation review

### Mathematical audit (line by line)

Main theorem (Thm 1.1) verification:
- Conventions: slope normalization p>=0, q>=1, gcd=1 with mirroring is
  correct (mirroring preserves the number t of prime factors).
- Case coverage: r=infinity (S^3); unknot (lens spaces incl. S^1xS^2);
  q>=2; q=1 with p=0, p=+-1, p>=2 irreducible, p>=2 reducible. Complete.
- Lemma 2.1 (homology of p/q-surgery): correct, Z/pZ incl. half-integer
  slopes (p odd), p=0 gives Z.
- Lemma 2.2 (lens spaces prime): correct via sphere theorem + b1; the
  "prime lens space with H1=0 is S^3" clause fine (L(1,q)=S^3).
- Lemma 2.3 (non-integral slopes prime): correct via Gordon-Luecke
  integrality (stated with the right 1987 reference) + Property P + b1.
- Lemma 2.4 (cabling surgery splits S^3_{uv}(C_{u,v}(C)) = S^3_{v/u}(C) # L,
  pi1(L)=Z/u): the compression step (compressible boundary torus W = J # X,
  J solid torus, X closed; iterated sphere-capping) is correct for torus
  boundary; the reduction of X to the unknot case (X depends only on the
  intrinsic pair (V,K), i.e. X_C ~ X_U, equivalently the change-of-surgery-
  picture argument) is valid; the torus-knot computation pi1 = Z/u * Z/v
  from <x,y | x^u=y^v> by killing the fiber h is correct; Kneser-Milnor
  uniqueness correctly forces X ~ M_u (lens, pi1=Z/u); the matching uses
  that L(v,.) # X = M_u # M_v are prime decompositions of manifolds without
  S^1xS^2 summands (b1=0, |H1|=uv finite). Checked: u>=2 makes X nontrivial;
  v=+-1 gives X ~ L(u,v')-type lens consistent with E1.
- Sec 3, Case 2 (0-surgery): fibredness of L-space knots (declared Thm 1.6)
  + mapping torus of closed genus-g>=1 surface is aspherical + sphere
  theorem -> irreducible; not S^3 (b1=1) -> prime. Correct.
- Case 3 (+-1): Ni--Wu forces cable with uv=+-1, but |uv|>=2, contradiction.
  Correct and complete (alternative via Berge not needed).
- Case 4 (p>=2 reducible): both summands nontrivial prime; the C=unknot
  (torus) subcase with |v|>=2 (since K nontrivial) handled. Correct.
- Sharpness: S^3_6(right-hand trefoil) = L(2,3) # L(3,2). Correct
  (sign conventions consistent: uv=+6).

External inputs: Kneser-Milnor (incl. the pi1 free-product splitting),
Gordon-Luecke integrality of reducing slopes (correct citation, 1987),
Kronheimer-Mrowka Property P (2004), the cabling theorem for L-space knots
(attribution issue below), fibredness of L-space knots, sphere theorem,
classification of closed orientable prime 3-manifolds with finite cyclic pi1
as lens spaces. All stated with hypotheses; the complete list is honestly
collected in Remark 4.5. Section 4's mechanism sketch is explicitly labeled
"not used in the proof of Theorem 1.1"; the main chain does not rely on it.

Conclusion: AC-1 (every implication proved or externally declared), AC-2
(precise external statements), AC-3 (quantifiers/constants/degeneracies
checked; re-verified by me), AC-4 (assertion is true and proved; no
conjecture presented as fact in the load-bearing chain), AC-5 (format):
all met.

### Contract vs. delivered

The round-0 contract's "Mainline Objective" and success criterion 3 demand
"full proofs of the two load-bearing lemmas (the Schubert/Scharlemann
closed-incompressible-surface theorem ... and the HFK-epsilon obstruction
...)". The delivered document does NOT prove these; it cites the cabling
theorem for L-space knots as a stated external theorem (plus Scharlemann's
reduction stated inside the optional Section 4) and gives only an
explicitly optional heuristic sketch.

Assessment: the contract overstated the deliverable. Full re-proofs of those
inputs are research-level developments and are not feasible in a 16-page
note; the plan's own AC-2 permits "precisely states any external theorem it
invokes," and the contract itself elsewhere lists "cabling characterization
of reducible surgeries" as an external statement. I logged this as a
plan-evolution entry (Round 0) and as a queued issue: the worker should
have amended the contract text rather than leaving it self-contradictory.
This does not block AC progress.

### Claims vs. reality in the worker summary

All factual build claims verified independently (compiles twice, 7 pages,
package list, no markdown). The summary's description of the mathematical
content matches the document. One overstatement: "complete, self-contained
proof" -- accurate only relative to declared external theorems (which AC-2
allows); no correction needed to the deliverable.

## Part 2 -- Goal alignment

Goal tracker review: ACs and Ultimate Goal initialized correctly in the
immutable section. All 5 original active tasks were done; I updated their
statuses, added the review-verification evidence, logged the plan-evolution
entry, and created one Round-1 mainline-polish task for the queued
corrections below. No forgotten items; no unjustified deferrals.

## Part 4 -- Findings by lane

### Mainline Gaps

None. The original problem is solved and the solution satisfies AC-1..AC-5.
One small mainline-polish task spawned from the review findings (queued
issues 2-4 below, folded into a single Round-1 task).

### Blocking Side Issues

None.

### Queued Side Issues (all non-blocking; fix in one small Round-1 pass)

1. Contract hygiene (see above): contract promised full proofs of two
   research-level inputs; resolved by plan-evolution entry. No text change
   required to solution.tex; optionally annotate contract as superseded.

2. Citation/attribution accuracy for Theorem 1.4 (the "cabling conjecture
   for L-space knots"). The document attributes it to "Ni--Wu, 2014" and
   cites Y. Ni and Z. Wu, Heegaard Floer correction terms and rational genus
   bounds (Adv. Math. 267, 2014). That paper proves the rational-genus /
   d-invariant bounds; the precise statement used here (reducible surgery on
   an L-space knot => cabled with the cabling slope; the cabling conjecture
   for L-space knots) was completed by Z. Wu (2014) building on Ni--Wu.
   Fix: relabel Theorem 1.4 as "Ni--Wu and Wu (2014)" or "proved by Ni--Wu
   and completed by Z. Wu"; keep Section 4's attribution of the d-invariant
   mechanism to Ni--Wu.

3. Definition 1.2 wording: "the infimum ... equals the Thurston norm
   x(gamma)/2 = g(K) - 1/2 when K is a knot in S^3 with an incompressible
   Seifert surface" -- replace the clause with "for every nontrivial knot
   K in S^3" (the minimal-genus Seifert surface is always incompressible).
   The remark about Calegari-Gordon applying to arbitrary knots may stay.

4. Cosmetic consistency: set the optional-sketch paragraph in Section 4.2
   in slanted/italic type so the "not part of the proof" status is
   typographically visible (the prose already states it twice); repair the
   garbled formula fragment in Remark 4.4 ("the two forces the equality");
   add the missing word "Theorem" before the cross-reference at the start
   of Section 4.2; delete the doubled word "rational" in "The (rational)
   rational genus"; optionally trim duplicated notation between
   Definition 1.2 and the optional subsection. None of these can mislead
   a specialist.

## Round-1 directive

Single small polish pass implementing queued items 2-4 (citation relabel,
one sentence in Definition 1.2, typographic labeling of the optional sketch
plus the garbled-line fix), recompile, re-verify pages <= 16, commit.
Do NOT restructure the proof; the mathematics is final. After that pass the
deliverable is done.
