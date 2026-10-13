# Verification of the draft proof (r3)

## Verdict
I found no mathematical error that breaks the chain Lemma 1, then §§3–6. The main claim (Theorem 1: YES, for SC divisors whose definition includes positivity) is **proved conditionally**. It depends on two literature inputs that are quoted from memory and that I could not check against the sources. These are listed as G1 and G2 below. Proposition 0 and the local counterexample are correct. All checks below are by hand; I had no access to the papers.

## Step-by-step checks that passed
- **Prop. 0.**
  - $dz_i$ is $J$-linear and the $dz_i$ are independent, so the strata are $J$-complex.
  - For a tame $J$, the complex orientation equals the $\omega$-orientation, both on $TD_I$ and on $TM$.
  - The normal orientations therefore come from $dz_i$, and positivity follows.
- **Example.** The determinant is $\det\begin{pmatrix}\varepsilon&0\\0&-\varepsilon\end{pmatrix}=-\varepsilon^2<0$, and $\omega|_{D_2}=(1-\varepsilon^2)\,dx_1\wedge dy_1$. Both check. The sign is a deformation invariant.
- **Lemma 0.**
  - A compatible $J$ preserving $W$ also preserves $W^\omega$ and each $N_i$.
  - Conversely, a product structure on the $\omega$-orthogonal blocks (R2) preserves every $T C_i$.
  - Since the fibres are contractible, the deepest-first extension works.
- **Prop. AH.** The local logic is right: rescaling makes the curvature error $O(1/k)$, restriction to an exactly complex $\Sigma$ preserves the AH property, and the inductive constants in Step C are correct, with $C^1$-openness coming from a Neumann series. The proposition rests on G2.
- **Lemma AH′.**
  - $A$ is surjective because $|B|\ll\eta$.
  - The kernels deform continuously and stay close to the complex subspace $\ker A$.
  - Nondegeneracy and the agreement of orientations persist along the deformation.
  - Applied with $V=TC_I$ for an old, exactly $J_l$-complex stratum, this gives positivity of mixed old/new strata.
- **Lemma 1.**
  - The integral PD identity holds: $c_1(L_a\otimes P_k)-c_1(P_k)=c_1(L_a)$, torsion included.
  - Using all sub-tuples on all old strata gives exactly the SC transversality.
  - The bookkeeping of the iteration is consistent.
- **Lemmas A, Ch, D, B′.** All re-derived; they are correct.
  - Horizontal space $=\ker(dz+z\theta)$, so $z$ is holomorphic iff $\theta\circ J_B=i\theta$.
  - $\partial\log\bar g=0$ for $J$-holomorphic $g$, with no integrability needed.
  - $\theta+\bar\theta=d\log h$, so the connection is unitary.
  - At the zero section $J_\nabla=J_B\oplus i$, and tameness follows from (R2).
- **Needed sets.**
  - $I\cup b$ is needed for $b\in B_I$.
  - $I\cup a^\pm$ is needed for $a\in I$.
  - In the overlap step, $K=I\cup\{b,c\}$ is needed.
  - The chain argument shows that level $n-1$ elements occur only in 0-dimensional strata.
  - The ordering of the induction is consistent. $H_{I;a}$ uses $J_I$, which uses $H_{I\cup b;b}$; that is deeper. It also uses $H_{I;a^\pm}$, which has higher level. There is no circularity.
- **Step (b) atlas.** On the tube, the transitions $z^{(\alpha)}$ and $z^{(\alpha)}/z^{(\beta)}=\pi^*g_{\beta\alpha}$ are $J_I$-holomorphic by (C1), Lemma A and Lemma Ch. This is a genuine holomorphic atlas, and it is valid even for non-integrable $J_I$, because transitions are only needed on overlaps.
- **(C2) verification.** I checked all three cases, $c=b$, $c\notin I\cup b$ (nonempty and empty), and $c\in I$. Each relies on (R3)/(R4), meaning $\pi$ preserves $z_c$, together with Lemma F.
- **Lemma F.**
  - $u=1$ on $C_K$ and near deeper strata, by $\pi_{K'}\circ\pi_K=\pi_{K'}$.
  - $\log u$ is defined because the fibres are discs.
  - The cutoff modification only acts where same-codimension tubes meet inside deeper tubes, and there $f=0$.
- **§6.** Iterating (C1) with Lemma D along $K\subset A_0$ shows that $J$ equals $J_\nabla$ on $N_K$ over $D_K$. The fibre coordinates in holomorphic frames are then $J$-holomorphic, and $\Psi_K$ gives a chart.

## Gaps, in order of severity
- **G1 (citation, load-bearing).** The TMZ "cohomologous clause": the deformation to a regularizable form should be $\omega+d\mu_t$ inside $\mathrm{Symp}^+$. The draft does not verify this.
  - The problem statement permits exactly such deformations, but the existence of one with fixed cohomology class must come from TMZ.
  - The sketch "the difference is exact on a tube" is plausible but incomplete: it does not show that the path stays inside $\mathrm{Symp}^+$.
  - My recollection is that TMZ do state such a path, but I cannot confirm it.
- **G2 (citation/assembly, load-bearing).** Prop. AH combines three things into one statement that is not published as such: a non-integral class with an $O(1)$ curvature error, a fixed twist $E$, and simultaneous $\eta$-transversality of all sub-tuples on finitely many exactly $J$-complex submanifolds. The sketch is standard Donaldson–Auroux reasoning and I believe it, but it is a sketch.
  - The step "Gaussian reference sections restrict to reference sections on $\Sigma$" in particular needs care, since the coordinates are Darboux coordinates adapted to $\Sigma$ that only approximately linearize $J$.
  - The case $|S|>\dim_{\mathbb C}\Sigma$ needs to be handled explicitly: there transversality means nonvanishing.
- **G3 (minor, technical).** Repeatedly shrinking tube radii (the tube-radius convention, Lemma F, Step (a)) must preserve (R3)/(R4) simultaneously. This needs an ordering of the shrinkings: shallower tubes are shrunk after, and more than, deeper ones. The draft asserts this without detail, but it is routine.
- **G4 (peripheral).** Closed counterexamples without positivity: the draft explicitly does not complete the local example to closed components. This does not affect Theorem 1.
- **G5 (peripheral, unproved remark).** The §8 claim that "for $n\ge3$ this fails for generic $J$" is unsupported. It is not used.
- **G6 (presentation).** The statements that something was "checked by computer" or confirmed by "independent referee passes" carry no weight here. My hand checks above replace them.

## Conclusion
The main claim is proved, conditional on G1 and G2: after a permitted deformation, such a $J$ exists, with positivity included in the definition of a symplectic SC divisor. If positivity is not part of the definition, the draft correctly shows the answer is NO locally (Proposition 0 and the example).

**Open:**
- confirming the TMZ cohomologous-path statement against the paper (G1);
- writing out a complete proof of Prop. AH (G2);
- the closed counterexample (G4).

=== END OF ANSWER r3_verify ===
