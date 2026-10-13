# Running summary after round 1 planning (no results yet)

## Problem and interpretation
The problem uses undefined macros. Interpretation adopted by the run (stated in every query):
- `\bcS_n(\fB^*)` = reduced stated SL(n)-skein algebra (Lê–Sikora stated skein relations; Lê–Yu bad-arc quotient) of the punctured bigon B* (bigon with one interior puncture; two boundary edges left/right, ideal points top/bottom).
- b_{ij} (resp. c_{ij}) = horizontal left-to-right arc passing above (resp. below) the puncture, state i on left edge, j on right edge. In the reduced algebra one of B, C is upper, the other lower triangular, with invertible diagonals.
- Evidence: GK-dimension count n^2+n-2 = 2(n(n+1)/2 - 1) matches the double of Borels; the unreduced algebra would have dim 2n^2-2. The relation b_ii c_ii = 1 then identifies the two Cartan copies, matching Klimyk–Schmüdgen's description of U_q as a quotient of the double of the Borels.
- U_q(sl_n) = K–S U_q^{ext}(sl_n) with \hat K_1...\hat K_n = 1.

## Established
Nothing yet.

## Planned route
(A) Skein side: presentation of \bar S_n(B*) by triangular B, C with RTT relations RB1B2=B2B1R, RC1C2=C2C1R, a mixed exchange relation, quantum determinants =1; plus basis/linear independence.
(B) Double side: L-functional (FRT, K–S §8.5) presentation of U_q(b_-) ⋈ U_q(b_+) with the same relations but without l+_ii l-_ii = 1.
(C) Match on generators; part (2) is then the K–S quotient statement.
Alternative structural route (q4): twisted tensor product via splitting + Hopf duality O_q(B_±) ↔ U_q(b_∓).

## Open gaps
Everything: the GOAL; specifically Claim S (skein presentation + basis), Claim D (RLL presentation of the double), the matching.

## Next round should concentrate on
Round 1 wave (4 attempt queries): q1 full FRT route; q2 skein presentation (Claim S); q3 double presentation (Claim D); q4 structural gluing/duality route. Next plan: fold in results, check n=2 constants numerically where possible, and focus on whichever half is weakest (likely linear independence on the skein side and the exact form/normalisation of the mixed relation).
