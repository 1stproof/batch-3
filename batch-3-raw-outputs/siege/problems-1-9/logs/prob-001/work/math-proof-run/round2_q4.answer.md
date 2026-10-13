# round2_q4: attempt at the structural route

## Status
This is NOT RESOLVED. I do not have a proof of YES for all P, and I have no counterexample.

## What I checked
- R1, R2 and R4 from the background: I re-checked the arguments. They are correct as stated; R4 needs the finite-presentation hypothesis.
- Step (a), the injective resolution: for a presheaf F on the poset of principal faces, the map F -> prod_tau I_{tau,F(tau)} is a monomorphism. Here I_{tau,A}(b) = A when tau is a localization of b, and 0 otherwise. Its tau-component is the evaluation at tau, so it is injective objectwise. I_{tau,A} is injective when A is injective, because Hom(G, I_{tau,A}) = Hom(G(tau), A). This step is fine.
- Step (a)(1) is open: does pi^{-1} commute with infinite products? Sheafification does not commute with infinite products in general. Unless the birhizomic site is shown to be coherent (finitary covers), this step fails. Finite presentation of each P -> Q_i does not by itself bound the number of members in a cover.
- Step (b) is open: identify pi^{-1} I_{tau,A} as the pushforward of a constant sheaf from the slice A_tau. This needs a computation of the left Kan extension followed by sheafification, and I did not carry it out. It also needs the acyclicity of the constant sheaf on the birhizomic site, which nobody has proved. R2 (the zero valuation factors birhizomically everywhere) does not give a splitting of covers, so it does not give flasqueness.

## Open questions, stated precisely
1. Is the birhizomic site of every monoid coherent? Does pi^{-1} commute with products?
2. Is pi^{-1} I_{tau,A} equal to j_* of the constant sheaf A on A_tau^op?
3. Does the constant sheaf A on A_{P'}^op satisfy H^0 = A and H^{>0} = 0, for every monoid P'?

A YES answer to 1, 2 and 3 would give YES to the main question. 3 alone does not.

Conclusion: the answer is conjecturally YES, as in the background, but this is unproved.

=== END OF ANSWER round2_q4 ===
