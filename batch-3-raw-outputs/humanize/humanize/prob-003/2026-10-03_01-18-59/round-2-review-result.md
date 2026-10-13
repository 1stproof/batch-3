# Round 2 Review Result — prob-003 (bigon algebra = generalized quantum double)

Reviewer: independent audit of `solution.tex` (commit f7347e3), the round-2/round-3
summaries, the goal tracker, both worker engines (vrf.py, vcheck.py — both re-run and
reproduced: `333 PASS, 0 FAIL` and `1208 PASS / docALL 84/84`), and three NEW exact
engines built by this reviewer from the PRINTED axioms verbatim (pairing `(PA)` with
the co-opposite second line as displayed, `(P)`, `(C)`, `(S)`, `(SK)` as printed;
`/tmp/rev3/*.py`, rational functions in t, q=t^12). Build state: pdflatex compiles,
14 pages, 0 undefined refs (AC-5 fine).

The headline: the convention churn of round 3 was a false alarm in one layer and
masking in another. lem:cross(a),(b),(c) are CORRECT in the printed world (I re-derived
them three ways and initially mis-flagged (b) with a doubly-flipped expectation; the
error was mine, not the paper's). But the decisive scalar of the whole paper — the
first channel of prop:EF — is FALSE as displayed under the paper's own printed
`(PA)`+`(SK)`, and the (EF)→(EF') conversion that the entire arc relation (M2),
Part-1 well-definedness, and Part-2 quotient stand on is NOT VALID in D. The mainline
is not established.

## Mainline Progress Verdict: STALLED

```
ACs: 1/5 met (AC-5 only) | Forgotten items: 0 | Unjustified deferrals: 0
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
```

## What is verified correct (reviewer-derived from the printed axioms)

- lem:T(a),(b) grouplike pairing and vanishing: PASS (my engine, all (i,r,s), n=2,3,4).
- lem:T(c),(d) as PRINTED in the co-op world: PASS — `<K^u F_s,E_r>=δθ`,
  `<F_s K^u,E_r>=δθ q^{+α_s(u)}`, `<F_s,K^v E_r>=δθ`, `<F_s,E_r K^v>=δθ q^{-α_s(v)}`.
- lem:compat(i),(ii),(iii) under the co-op second line: PASS, including the Serre
  relators at matching charge (0 fail, n=3) and charge grading. The co-op pairing
  descends consistently to both Borels; the round-3 justification paragraph is honest.
- lem:cross(a): `Ĥ_i^{(-)}E_r = q^{+α_r(i)}E_r Ĥ_i^{(-)}`, bulk
  `E_r Ĥ^{u(-)} = q^{-α_r(u)} Ĥ^{u(-)}E_r`, and (aInv): PASS at all (r,i), n=2,3
  (channel = (𝒦_r,E_r,1), scalar ⟨g,𝒦_r^{-1}⟩ = q^{-u·(-α_r)} ... = q^{-α_r(u)}).
- lem:cross(c) cross-Cartans commute: PASS.
- lem:cross(b): `Ĥ_i^{(+)}F_s = q^{-α_s(i)}F_s Ĥ_i^{(+)}` and (bInv): PASSES per the
  printed proof's own channel (1,F_s,𝒦_s^{-1}) with third scalar ⟨𝒦_s^{-1},g⟩ = q^{-α_s(μ)};
  my engine confirms at all (s,i). **The round-1 reviewer's claim that (b) flips was
  wrong, and the worker's round-3 "fix" of it was the correct non-action.**
- (A2)‑(bar∗) sign bookkeeping: coherent as printed.

## A. BLOCKING SIDE ISSUE (the fatal one)

### A1 (FATAL). prop:EF's displayed channel values do NOT follow from the printed `(PA)`+`(SK)`; (EF') is not a consequence of (EF) in D; (M2), Part 1 well-definedness, and Part 2 inherit the break

The first channel ((F_s,𝒦_s^{-1},𝒦_s^{-1}),(E_r,1,1)) of `(SK)` has scalar

  −⟨𝒦_s^{-1}F_s, E_r𝒦_r^{-1}⟩  (from ⟨x_1,S^{-1}(y_1)⟩, S^{-1}(E_r)=−E_r𝒦_r^{-1}).

The paper evaluates this with a SINGLE-letter second argument and gets −δθ. But
S^{-1}(E_r)=−E_r𝒦_r^{-1} is a **two-letter word**, and the pairing of the two-letter
first argument ⟨𝒦_s^{-1}F_s, ·⟩ against a two-letter second argument is EXACTLY where
the paper's co-opposite second line of `(PA)` matters. The claim in def:D that "the
two variants agree whenever the first argument is a single letter or grouplike ... hence
the entire cross calculus is insensitive to this choice" is FALSE: (x1,S^{-1}(y1))
routinely has a two-letter first argument with a two-letter second argument. My engine
prints, for the printed axioms, at all (r,s), n=2,3:

  ⟨𝒦_s^{-1}F_s, E_r𝒦_r^{-1}⟩ = δ_rs·θ·q^{-2}   (co-op world, S^{-1} print)

so the (SK)-true first channel is −δθ q^{-2} 𝒦_s^{(-)-1} and (EF) should read

  E_rF_s = F_sE_r + δ_rs θ ( 𝒦_r^{(+)} − q^{-2}𝒦_s^{(-)-1} ) ,

NOT the displayed `F_sE_r − δθ 𝒦_s^{(-)-1} + δθ 𝒦_r^{(+)}`. Independently, vrf.py's OWN
EF battery header records the same −θ q^{-2} (`RF.c(0) - TH * QE(-2)` trivially equals
−θq^{-2}), so the paper's displayed "−θ𝒦_s^{(-)-1}" first channel contradicts even
the worker's own axioms engine.

Consequence 1 — the (EFraw)→(EF') conversion is broken. The paper's prop:EF proof
asserts that right-multiplication by 𝒦_s^{(-)} turns both `(EF)` and `(EF')` into the
same normal form, "carried out in the exact model". This is FALSE in D. With θ′=θ on
the minus-Cartan (the paper's first channel) the conversion goes through; with the
(SK)-true coefficient −θq^{-2} it does not. Machine-exact reduction of both forms
against the CERTIFIED rule set (lem:cross(a),(b),(c) + internal (H1) + the raw (EF)
with coefficient −θq^{e}) gives, at every (r,s), n=2,3,4:

  (EF)·𝒦_s^{(-)}  normalizes to  {FE𝒦: q^{2}, 𝟙: −θq^{-2}, 𝒦^{(+)}𝒦^{(-)}: +θ}
  (EF')·𝒦_s^{(-)} normalizes to  {FE𝒦: q^{2}, 𝒦^{(-)2}: +θ, 𝒦^{(+)-1}𝒦^{(-)}: −θ}

— different grouplike content at e=−2 (they coincide only at e=0, i.e. only if the
printed first channel were correct, which it is not).

Consequence 2 — Part 2's quotient is not proved to be H. lem:diag specializes
prop:EF's (EF') to `(H2)` under Ĥ^{(+)}=Ĥ^{(-)}. The true cross commutator in the
printed world, evaluated honestly, is the q-TWISTED form

  F_sE_r − E_rF_s = δ_rs θ( q^{2}𝒦_s^{(-)} − 𝒦_r^{(+)-1} )·(unit shifts)  —

i.e. the classical Rosso/Tanisaki q²-twisted commutator (my co-op (SK) engine:
⟨F,S^{-1}(E)⟩ = −δθq^{-2} throughout, giving the q²-twist on one leg), whose diagonal
reduction is δθ(q²𝒦−𝒦^{-1}), NOT printed (H2) δθ(𝒦^{-1}−𝒦). The alternative the paper
pretends (assert (EF') directly) is precisely the relation that is not implied by (EF).

Consequence 3 — (M2) and Part 1 well-definedness. The arc face relation (M2) is
derived in thm:mixed(e) from (EF') via (EFrule); with (EF') unavailable in D, the
$\theta$-correction on the bigon face is not proved. The docALL/vcheck "84/84"
verification of (M2) shares the assert-(EF')-as-step-rule premise (vcheck's FE-step
IS (EF') rearranged), so it is circular for this purpose.

Root cause (now crisp across three rounds): rounds 0–3 keep obtaining
−θ·(grouplike) from a single-letter second argument either by (round 0-1) sign slips,
or (round 2 vrf) an internal inconsistency that its own EF battery records as
−θq^{-2}, or (round 3) the false "two variants agree on single letters or grouplikes
⇒ cross calculus insensitive" claim. The honest mathematics is that the DRINFEL'D–
TANISAKI pairing for these symmetric (P)-values is NOT a plain skew pairing: the
classical theorem (Tanisaki; Klimyk–Schmüdgen §8) derives

  F_sE_r − q^{α·?}E_rF_s = δ_rs θ(K-stuff)   with the q²-twist,

and the problem's SURFACE algebra is expected to reproduce the classical U_q^{ext}
(H1),(H2),(H3) in the quotient — which requires a DIFFERENT identification of the
two Borels' Cartans than Ĥ^{(+)}=Ĥ^{(-)}, or a q-rescaled embedding of the F's.
The paper never performs this reconciliation; it simply asserts the untwisted (EF')
and "verifies" it with an engine whose step rule is (EF').

## B. MAINLINE GAPS (vs plan ACs)

- G1 (AC-1): Part 1 not established — (M2) (the unique double-shared-mark relation)
  is unproved; well-definedness of Φ rests on it. Part 2 not established — lem:diag's
  (H2) specialization is false as derived from (SK); D/J is not shown to be H.
- G2 (AC-2): the two external inputs are stated precisely; the skew-pairing descent
  (co-op variant) is now honestly justified. This part is fine.
- G3 (AC-3): FAILED at prop:EF. The "machine-checked" rem:verify claims are
  internally inconsistent: vrf asserts −θq^{-2} in its EF battery while vcheck
  asserts (EF') (≡ −θ·1 minus-Cartan) as a step rule; both "pass" because neither
  checks the (EF)→(EF') step in D. This is the third consecutive round in which a
  verification battery's stated convention disagrees with the paper's display at the
  single scalar that decides the problem.
- G4 (AC-4): the paper asserts (and "verifies") a sign/q-power-wrong (EF).
- G5 (AC-5): OK (14 pp, standard packages, compiles, 0 undefined refs).

## C. QUEUED SIDE ISSUES (do NOT take over next round)

- Q1: The round-3 convention churn (co-op (PA) line 2, (bar-ast), lem:T(a) flips)
  should be KEPT — it is correct — but solution.tex should stop claiming the cross
  calculus is "insensitive" to the (PA) variant (the sentence in def:D is false).
- Q2: scratch/ tidying remains deferred to final submission.
- Q3: The redundant `(SK)` "extensive kernel enumeration" prose overstates what was
  enumerated; keep as one sentence.

## D. DIRECTIVE FOR ROUND 3 (execute in order)

The mathematics needed is now fully determined by three engines worth of evidence.
Implement exactly one of the following; verification must be from `(PA),(P),(C),(S),(SK)`
with the two-letter first-argument channels handled explicitly (NO single-letter
short-cuts in (x1,S^{-1}(y1))).

D1. Recompute prop:EF honestly in the printed world. Either
    (a) accept the q²-twisted commutator that `(SK)` gives (my engine:
        F_sE_r − q²E_rF_s-type form, coefficient δθ on (q²𝒦_s^{(-)} − 𝒦_r^{(+)-1})
        after the grouplike crossings are done correctly), and then re-derive (M2),
        thm:mixed(e), and lem:diag from THAT; the diagonal quotient will then be
        U_q^{ext} either via the standard q-rescaling E'_r = q^{-1}E_r (which untwists
        the commutator to (H2)) — in which case def:phi must be adjusted and the arc
        images and minors re-derived — or via the honest statement that the quotient
        is the q²-variant of H, in which case the problem as posed is answered by this
        variant and that must be said plainly; or
    (b) change ONE geometric input: use the Klimyk–Schmüdgen Rosso form of the
        pairing/co-product for the negative Borel (Δ(F)=F⊗1+𝒦^{-1}⊗F or the mirrored
        coproduct) so that the (SK) first channel genuinely evaluates to −θ (plain),
        and re-derive everything from there. State explicitly which book normalization
        is used and that it is a different (P0)-compatible choice. The problem
        statement FIXES (P0), (H1)–(H3), and the pairing values; the freedom is in the
        negative-Borel coproduct / mirror.
    Do NOT do what rounds 2-3 did: keep the printed world and quietly assume (EF').

D2. After D1, re-derive (M2), the minors, and lem:diag in the new world; re-check
    that lem:cross(a),(b) (which are correct NOW) survive the change (they will iff
    the grouplike channels are untouched by the D1 choice — they are, since those use
    single-letter/grouplike y1 only).

D3. Rebuild the verification: ONE engine computing (x1,S^{-1}(y1)) with full two-letter
    support; assert (EF) from it; assert the (EF)→(M2 raw) step BY REWRITE in D; then
    check the arc relations. The battery must FAIL loudly if the first channel comes
    out −θ (plain) when the world predicts −θq^{-2}, or vice versa. Remove the
    "insensitive to (PA) variant" claim.

D4. Update rem:verify, the goal-tracker, and the bitlesson. Commit.

## E. GOAL-TRACKER ACTIONS (applied by reviewer)

- Plan Evolution Log: added round-2-review correction row: (EF) first channel is
  −θq^{-2} not −θ; (EF') not implied; lem:cross(a),(b),(c) confirmed correct;
  vcheck/vrf internal inconsistency at the EF scalar documented.
- Active Tasks: reopened Part-1 well-definedness (M2), Part-2 quotient (lem:diag),
  and the EF/verification task; marked the round-3 "APPLIED (3)/(4)" fixes as
  resolving the wrong problem (the pairing-layer churn was correct but did not touch
  the EF first channel).
- Blocking: A1 above replaces the stale A1/A2 rows (those are resolved).

Reviewer verdict: NOT complete. The round claims that "every cross scalar verified"
and "D/J = H" do not survive audit at prop:EF. The good news: this is the SAME scalar
that has failed for three rounds, its true value is now engine-pinned in two
independent implementations, and the repair direction (D1a or D1b) is concrete.
