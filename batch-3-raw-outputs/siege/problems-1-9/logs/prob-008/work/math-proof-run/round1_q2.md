kind: attempt
Open question attempted: the structural consequences of global hypoellipticity (GH) needed for the headline claim — in particular whether a GH vector field must preserve a smooth volume and be uniquely ergodic. This is an open gap in our attempt to prove that GH flows have zero topological entropy.

Setting: M compact connected smooth manifold, X a smooth vector field which is globally hypoelliptic in the sense of the problem statement below. Distributions = continuous linear functionals on smooth densities; L_X on distributions by duality <L_X u, rho> = -<u, L_X rho>.

Prove rigorously, each as a separate lemma with complete proof (no "well known"; if you invoke the closed graph / open mapping theorem for Frechet or (DF) spaces, Rellich compactness, or the closed range theorem, state the version used):
(L1) The kernel of L_X acting on distributions consists of the constant functions.
(L2) There is an estimate: for every s there are k = k(s) and C such that ||u - c(u)||_{H^s} <= C ||X u||_{H^k} for all smooth u (c(u) a suitable constant, e.g. the mean against a fixed volume); hence X: C^infinity -> C^infinity has closed range.
(L3) If dim M >= 2 then X has no zeros. (If you find this false or unprovable, say so; consider what a zero p implies, e.g. delta_p is an invariant measure.)
(L4) The space of X-invariant distribution densities (distribution densities T with L_X T = 0) is one-dimensional and spanned by a smooth positive volume form omega; consequently div_omega X = 0, the flow is uniquely ergodic, and (as omega has full support) minimal. Possible idea, to be checked: the range of X is closed; if [div X] lies in range(X) + constants, then for an invariant measure mu the generalized function v = e^{a} mu/omega lies in ker X. Find a correct argument; if L4 genuinely needs an extra idea, find it (e.g. time changes hX, h>0 smooth, preserve GH; transposed operators; Fredholm-type arguments).
(L5) Consequently every smooth f with integral 0 against omega equals X u for a unique zero-mean smooth u, with tame estimates ||u||_{C^r} <= C_r ||f||_{C^{k(r)}}, and dually: for every s there exist k and C such that for every distribution w with <w, omega> = 0, ||w||_{(C^k)'} <= C ||L_X w||_{(C^s)'} (dual norms).
(L6) If dim M >= 2 the flow has no periodic orbits.

Then, as a bonus only after L1-L6 are done: assess whether L1-L6 alone already imply zero topological entropy, or what further use of GH is needed, and try to supply it.

If any of L1-L6 is false, give a counterexample. Be explicit about every gap.
