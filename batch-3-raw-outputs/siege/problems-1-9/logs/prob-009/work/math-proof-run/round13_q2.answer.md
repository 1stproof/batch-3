# round13_q2 — attempt on MS11♭

**Status: NOT PROVED, no counterexample. This report is partial and mostly an audit.**

Plan: (1) re-check the logical frame (chain ⇒ goal); (2) look for a global mechanism that forces t ↦ Y_t to be constant; (3) report.

## 1. Logical frame (re-checked)

- The chain proves at most: (Rig) + MS11♭ ⇒ problem's claim. (Rig) (entry 82) is still OPEN. So even a complete proof of MS11♭ would not settle the problem unconditionally. This is not a flaw in the chain, since the task file says so itself. It does mean that the problem's claim, as posed, is not established by the run.
- Step 1 ("Goal ⇐ MS8 + (Rig) + entry 19") is correct as stated. MS8 gives that Y is constant in t, and Y_0 is its value at t = 0. Entry 19 (holomorphy) is not even needed for this step: a constant function is constant. It is needed only inside step 2(d).
- Step 2 is a proof by contradiction that assumes Y is non-constant. Every invocation of MS11♭ in steps (c) and (d) occurs under that assumption. So including "Y non-constant" in MS11♭'s hypotheses is legitimate. I found no new flaw in the chain wording quoted in the task file (steps (a)–(d) and the Gap A / Gap B repairs as spliced). I did **not** re-derive the walk chain's marking details, Lemma PA, Lemma PT, Lemma J, Theorem N, or the round-12 lemmas S63–S65. I read only the parts of the task file reproduced in its header and in the round10 audit section.

## 2. Search for a global mechanism (dead ends, with reasons)

- **Rigidity of V_0 as a subvariety.** If V_0 admitted no non-trivial deformations satisfying (i), (ii), the claim would be vacuous. No such rigidity theorem is known to me for deformations that are **not** totally geodesic. Known rigidity results only cover deformations that stay totally geodesic or stay Teichmüller curves: McMullen's rigidity of Teichmüller curves, and the Q̄-definability and finiteness results of Eskin–Filip–Wright and Eskin–McMullen–Mukamel–Wright, all cited from memory. These do not apply to V_t for t ≠ 0. **Dead end.**
- **Countability of the possible values Y_t.** The natural route to "Y constant" is to show that Y_t lies in a countable set, e.g. that it is defined over Q̄ or is a rigid puncture value, and then use continuity. For t = 0 this holds for the relevant objects, because totally geodesic data are defined over Q̄. For t ≠ 0 nothing forces it, since V_t is an arbitrary holomorphic deformation. Hypotheses (i) and (ii) constrain only the incidence and topology of strata, and they are preserved by moving Y_t continuously. **Dead end** unless a further global input is found. This agrees with the run's earlier no-go results (counting; arithmetic of fields of definition).
- **Teichmüller-curve rigidity on other factors.** By Lemma PA and Prop. C, π_j(∂V_0) is a Teichmüller curve for a positive-area vertex j. But π_j(∂V_t) need not be one for t ≠ 0. So McMullen rigidity gives information only at t = 0. Round10 Prop. 3.2 already exploited the one place where rigidity applies, under the extra hypothesis (Eq). **No new information.**
- **Reflection case (R-a) of the planner's sketch.** The proposed step is: "the side-swap should force φ(t) and Y_0 to be values of the same constant vertex along a connected family". The two sides of c̃ in S are glued by H_t only **coarsely** (reading (R2)). In the coarse quotient the two sides are one sheet, and the label x on one side is identified with y = a^{-1}x on the other. So continuity of H_t on the coarse space gives exactly the twin identification that is already present. It does not give a single constant vertex carrying both values. The proposed contradiction therefore assumes what is to be proved, i.e. a label-level (orbifold) lift of H_t, which is the excluded reading (R2^orb). I could not repair this step. **Not established.**

## 3. Summary

**Proved here:** nothing new beyond the re-check in §1: the chain's step 1 is correct, and so is the legitimacy of the hypothesis "Y non-constant" in MS11♭.

**Not proved:**
- MS11♭ in any of the required generality;
- the (NRT) exclusion;
- the reflection-case conjecture (R-a): its key step relies on a label-level continuity that holds only under (R2^orb).

**Open:**
- (O1) MS11♭ (equivalently, under (Rig), the problem's claim).
- (O2) (Rig) (entry 82).
- (O3) Whether some totally geodesic smooth surface V_0 admits any non-trivial deformation satisfying (i) and (ii). If none does, the problem is vacuous. No such rigidity statement is known to me.
- (O4) Whether a global constraint (for example from total geodesy at t = 0 combined with the coarse homeomorphism H) forces label-level continuity of H_t at the boundary. This would reduce everything to the (R2^orb) case, which the run reports as settled.

=== END OF ANSWER round13_q2 ===
