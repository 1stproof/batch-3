# round1_q3 — partial answer (only a small part was worked out)

## Proved: the map N -> 0 is birhizomic at any v : 0 -> V
Take a factorization N -h-> M -p-> V of the zero map, with p infinitesimal. Put y = h(1) in M and x = -y in M^gp. Then p(x) = 0, which lies in V. Also x ≺ y: take m = -1 and n = 0, since -y <= x <= 0. And p(y) = 0 ≺ 0 = p(x). Because p is infinitesimal, x lies in M. So y is invertible, and since M is sharp, y = 0. Hence h factors uniquely through 0. The map N -> 0 is of finite presentation (one relation).

Consequence for P = N. Every valuation v : N -> V factors either through id_N (if v(1) > 0; the identity is trivially birhizomic) or through N -> 0 (if v(1) = 0). So the family {id_N} covers N.

## Claimed but not checked: the case P = N
I believe that {id_N}, together with families that refine to it, is the only kind of cover of N. If so, the site is local at the terminal object, and F -> R pi_* pi^{-1} F is an isomorphism with no higher cohomology. I did not verify the full classification of covers, so this is not proved.

## Not done
- (2) P = N^2 (blow-up charts, H^0 and H^1) was not computed. The director's heuristic (c) uses contractible open stars to predict "yes" for finitely generated P. It is plausible, but I did not verify it.
- (3) None of the non-finitely-generated cases were worked: Q_{>=0}, R_{>=0}, the irrational cone, the rank-two lexicographic monoid, and N^(infinity). For example, in the rank-two lexicographic monoid B_P has the three objects V, N (= V/(0×Z)) and 0. I did not check whether covers of it admit finite refinements.

## Verdict
Open. My conjecture is YES for every P, but nothing beyond the P = N lemma above is proved. No counterexample was found.

=== END OF ANSWER round1_q3 ===
