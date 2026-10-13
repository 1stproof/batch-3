# Round 3 Summary

## Mainline status: the (EF)->(EF') gap is REAL and machine-pinpointed

The round's contracted objective was to resolve the three-round defect at prop:EF.
That defect is now CONFIRMED by derivation-from-axioms engines (built fresh this
round; nothing cross-related hard-coded):

1. (EF) raw first channel: the printed `-delta th cK_s^{(-)-1}` is WRONG; the (SK)
   value is `-delta th q^{-2} cK_s^{(-)-1}` (the two-letter word
   S^{-1}(E_r)=-E_r cK_r^{-1} in the second pairing argument, first-line (PA)).
   vrf.py, vrf2.py, vtrue.py all agree. This is the reviewer A1 finding. The
   uncommitted round-3 patch setting (EF) to the q^{-2} form is CORRECT but is
   REVERTED this round because (EF) and (EF') are NOT at present both derivable,
   and printing the corrected (EF) beside the unproved conversion is an
   unresolved internal inconsistency. (The display cannot be set honestly until
   the conversion is fixed; see 3.)

2. The conversion (EF)->(EF') does NOT follow from (EF) alone. Mechanism,
   machine-isolated in scratch/vdecide.py: the conversion right-multiplies by the
   unit cK_s^{(-)}; the term F_s E_r cK_s^{(-)} is the DOUBLE-internal cross
   product cross(F_s cK_s^{(-)}, E_r) whose FE-channel scalar is q^{+2}, not 1
   (driven by <F_s, S^{-1}(E_r cK_s^{(-)})> = q^{+2} <F_s,S^{-1}(E_r)> after the
   minus-side canonicalisation), while its grouplike terms are exactly those of
   (EF').cK. Hence (EF).cK = (EF').cK holds only at e=0, i.e. only if the printed
   -th first channel were right, which it is not. The antipode-covariance
   recasting <F g, S^{-1}(E)> = <S(F g),E> (which avoids <F,Eg> entirely) does
   NOT remove the FE-channel q^2 once Delta^2(F_s g) is enumerated fully.

3. RESOLUTION DIRECTION (next round, reviewer D1a). The q^{-2} is removable by the
   q-normalisation E'_r = q^{-1} E_r (equivalently a different (P0')-normalised
   choice / a different cK extension), which untwists the cross commutator to the
   classical [E'_r,F_s] = delta th(cK^{-1}-cK) = printed (H2) in the diagonal
   quotient. def:phi, the minors, (M2) and every arc relation must be re-derived
   in the rescaled world (scalables: arc images with an upper E carry one extra
   q^{-1}; vcheck.py's rule world is to be re-derived, NOT re-asserted).
   vcheck.py currently ASSERTS (EF') as a step rule (the exact circular step the
   reviewer flagged): it must be regenerated from the rescaled rules, and the
   battery must FAIL loudly on a coefficient mismatch.

## What was verified-correct this round (unchanged)
lem:T(a)-(d), lem:compat (incl. Serre descent, co-op (PA) second line justified),
lem:cross(a),(b),(c), the PBW basis, Omega centrality, lem:split, the D/J -> H
presentation comparison GIVEN (EF'), (M0)/(M1)/(M3) scalars. These do not depend
on the broken conversion step.

## Hygiene
- False claim in def:D ("two variants agree ... cross calculus insensitive")
  identified; to be removed/reworded in the rescaled rewrite.
- New exact engines committed (vtrue/vprint/vstraight/vdecide + probes).
- Contract round-3 written; goal tracker updated (round-3 row).
- AC-5 stays green (14 pp, 0 undefined refs) throughout.

## BitLesson Delta
add: BL-20261003-product-slot-antipode (see .humanize/bitlesson.md).
