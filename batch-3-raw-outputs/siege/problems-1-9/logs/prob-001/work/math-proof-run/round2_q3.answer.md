# round2_q3: partial answer (little progress made)

I did not settle any of the test cases. Everything below is either a small observation or a plan.

## Observation 1 (proved): the identity valuation of a valuative P
Let P = V be valuative, and suppose a covering family contains a member f : V -> Q that is birhizomic at g : Q -> V with gf = id_V. Take the factorization V -id-> V -id-> V. Here id is infinitesimal, since it is injective (R1). So there is a unique u : Q -> V with u f = id and u = g. Hence **g = u is a retraction of f.** In particular f is injective and V is a retract of Q.

This does not by itself show that the family can be refined to {id}. That step also needs control of the valuations to V that are not injective.

## Observation 2 (proved): B_P for a valuative V of rank one
Take V = Q_{>=0}, or Z[sqrt2] intersected with R_{>=0}. The only faces are 0 and V. So B_V has two objects:
- id_V;
- V -> 0, which equals V[-x]^sharp for every x != 0.

A presheaf F on B_V^op is therefore just a map F(V) -> F(0). The left Kan extension of F to an object f : V -> Q of A_V is F(V) if f is injective, and F(0) if f = 0. Since V has rank one, ker f is either 0 or all of V, so these are the only two cases.

## Open
- The claim for every test case (1)-(3), in particular H^0 and H^1.
- Whether every birhizomic cover of N^(infinity) can be refined to a finite cover.

My guess, which I have not proved, is that the expected answer YES is correct.

=== END OF ANSWER round2_q3 ===
