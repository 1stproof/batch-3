The document below is a draft proof. Check the argument step by step: for every inequality, interchange, cited result, and 'it follows that', ask whether it actually follows as written. List every error or gap in order of severity, and say explicitly whether the main claim is proved.

## The draft proof

# Holomorphic normal-crossings charts for symplectic SC divisors

## 0. Conventions and the answer

Throughout, $\dim_{\mathbb R}M=2n$. Following Tehrani–McLean–Zinger (TMZ), a **symplectic simple normal crossings (SC) divisor** in $(M,\omega)$ is a finite union $D=\bigcup_{i\in S}D_i$ of closed, real codimension-2 submanifolds with the following properties:
- the $D_i$ intersect transversally, meaning every subcollection meets transversally;
- every stratum $D_I=\bigcap_{i\in I}D_i$ is a symplectic submanifold;
- **(positivity)** on every stratum, the symplectic orientation equals the intersection orientation. Each $D_i$ is oriented symplectically, and its normal bundle gets the induced orientation.

Write $\mathrm{Symp}^+(M,D)$ for the set of symplectic forms for which $D$ is SC in this sense. A **permitted deformation** is a path in $\mathrm{Symp}^+(M,D)$ consisting of forms cohomologous to $\omega$.

**Answer.** YES, with positivity included in the definition (Theorem 1). The proof relies on published results (TMZ, Donaldson, Auroux), which are quoted from memory; see §1 and §7. Positivity cannot be dropped: without it the answer is NO (Proposition 0).

**Proposition 0 (positivity is necessary).** Suppose $J$ is $\omega$-tame and there are coordinates near $p$ in which $z_1,\dots,z_r$ are $J$-holomorphic and $D=\{z_1\cdots z_r=0\}$. Then near $p$ every stratum is $J$-complex, and positivity holds.

*Proof.*
- $(z_1,\dots,z_n)$ is a real chart, so $d z_1,\dots,dz_r$ are $\mathbb R$-independent. Each is $J$-complex-linear, since $dz_i\circ J=i\,dz_i$.
- Hence $TD_I=\bigcap_{i\in I}\ker dz_i$ is $J$-invariant, and the normal directions carry complex orientations coming from $dz_i$.
- For a tame $J$, the complex orientation of a $J$-complex subspace $V$ equals its $\omega$-orientation, because $\omega|_V$ tames $J|_V$.
- So the intersection orientation of $D_I$ is a product of complex orientations, which is its complex orientation, which equals its $\omega$-orientation. ∎

**Example.** Take $\mathbb C^2$ with $\omega_{std}$, $D_1=\{z_2=0\}$ and $D_2=\{z_2=\varepsilon\bar z_1\}$, where $0<\varepsilon<1$.
- $D_2$ is parametrized by $z_1$, with tangent vectors $(1,0,\varepsilon,0)$ and $(0,1,0,-\varepsilon)$ in coordinates $(x_1,y_1,x_2,y_2)$.
- $\omega|_{D_2}=(1-\varepsilon^2)dx_1\wedge dy_1>0$, so $D_2$ is symplectic.
- $D_1,D_2$ are transverse, but $\det[(1,0,0,0),(0,1,0,0),(1,0,\varepsilon,0),(0,1,0,-\varepsilon)]=-\varepsilon^2<0$. So the intersection point is negative.
- These two values were checked symbolically.
- The intersection sign is locally constant along any path of forms keeping the configuration transverse with symplectic components. So no permitted deformation can repair it, and by Proposition 0 no such $J$ exists.
- The example embeds in a Darboux chart of any closed 4-manifold, giving closed counterexamples once it is completed to closed components. Doing that completion is not needed for the point being made, and is not carried out here.

So the question is answered for the TMZ notion, in which positivity is part of "symplectic SC divisor".

**Theorem 1.** Let $(M,\omega)$ be closed symplectic and $D\subset M$ a symplectic SC divisor. After a permitted deformation of $\omega$ to $\omega'$, there is an $\omega'$-tame $J$ with the following property. Every $p\in M$ has a neighbourhood with smooth complex coordinates $(z_1,\dots,z_n)$ in which $z_1,\dots,z_r$ are $J$-holomorphic and $D=\{z_1\cdots z_r=0\}$. Here $r$ is the number of components through $p$; $r=0$ off $D$.

The proof has two parts:
- **Part I** (§2, configuration lemma): enlarge $D$ to an SC divisor $C$ with "partner" components, chosen so that every normal bundle class is an integral difference of divisor classes.
- **Part II** (§3–§6, assembly theorem): build $J$ deepest-stratum-first. Every holomorphic structure needed on normal bundles is written down explicitly as a divisor-induced structure, so no relative extension problem for holomorphic structures arises.

The trivial cases:
- $n=1$: $D$ is a finite set of points and every $J$ is integrable, so a local holomorphic coordinate vanishing at $p$ works.
- $D=\emptyset$: take $r=0$ everywhere.

## 1. Cited inputs (from memory; numbering unverified)

**(TMZ)** M. F. Tehrani, M. McLean, A. Zinger, *Normal crossings singularities for symplectic topology*, Adv. Math. 339 (2018).

*Regularization.* An $\omega$-regularization of an SC divisor $C=\{C_a\}_{a\in A}$ assigns to each $I$ with $C_I\neq\emptyset$:
- Hermitian structures $(\rho_{I;a},\nabla_{I;a})$ on $N_a|_{C_I}$, $a\in I$, where $N_a=N_{C_a}$;
- an embedding $\Psi_I$ of a disc-bundle neighbourhood of the zero section of $N_I=\bigoplus_{a\in I}N_a|_{C_I}$ onto an open set $U_I\supset C_I$. Write $\pi_I:U_I\to C_I$ for the projection.

These satisfy:
- **(R1)** $\Psi_I=\mathrm{id}$ on the zero section, $d\Psi_I$ induces the identity on normal bundles, and $\Psi_I^{-1}(C_a)=\{z_a=0\}$ for $a\in I$.
- **(R2)** $\Psi_I^*\omega=\pi^*\omega|_{C_I}+\tfrac12\sum_a d(\rho_a\alpha_a)$, with $\alpha_a$ the connection 1-forms. In particular, along $C_I$ the splitting $TM=TC_I\oplus\bigoplus_a d\Psi_I(N_a)$ is $\omega$-orthogonal, and $\omega$ is positive on each $d\Psi_I(N_a)$ for its complex orientation.
- **(R3)** For $I\subset I'$, near $C_{I'}$ one has $N_I|_{C_I}\cong\pi^*(N_I|_{C_{I'}})$ with pulled-back metrics. Under $N_{I'}=N_{I'-I}C_I|_{C_{I'}}\oplus N_I|_{C_{I'}}$, $\Psi_{I'}$ is $\Psi_I$ composed with the induced map. Also $\pi_{I'}=\pi_{I'}\circ\pi_I$ on $U_I\cap U_{I'}$.

*Deformation theorem.* The forgetful map from pairs (form, regularization) to $\mathrm{Symp}^+(M,C)$ is a weak homotopy equivalence. In particular, every $\omega\in\mathrm{Symp}^+(M,C)$ is joined inside $\mathrm{Symp}^+(M,C)$ to a form admitting a regularization.

*Cohomologous clause.* I recall the deformation has the form $\omega+d\mu_t$ with $\mu_t$ supported near $C$. The reason: near $C$, the orthogonalized model form and $\omega$ agree on $TC_I$, so their difference is exact on a tube, $d\mu$ with $\mu|_{C_I}=0$. This clause is not verified against the paper. The problem statement itself presupposes deformations of this type.

*Domain conventions (R4).* These follow from (R3) by shrinking the tubes (compactness and transversality):
- $U_I\cap U_{I'}\subset U_{I\cup I'}$, and $U_I\cap U_{I'}=\emptyset$ if $C_{I\cup I'}=\emptyset$;
- $U_K\cap C_c$ is the tube of $C_{K\cup c}$ in $C_c$;
- for $c\notin K$, $\pi_K$ preserves the fibre coordinate $z_c$ on $U_K\cap U_c$. In $N_{K\cup c}$-coordinates, $\pi_K(z_K,z_c,x)=(0,z_c,x)$.

Restricting a regularization to a stratum $C_I$ gives a regularization of the induced SC divisor $\{C_b\cap C_I\}$ in $(C_I,\omega|)$. Shrinking the radius functions of tubes preserves all of (R1)–(R4).

**[D]** S. K. Donaldson, *Symplectic submanifolds and almost-complex geometry*, J. Differential Geom. 44 (1996).

**[A1]** D. Auroux, *Asymptotically holomorphic families of symplectic submanifolds*, GAFA 7 (1997). This covers sections of $E\otimes L^k$ for a fixed Hermitian bundle $E$, and $\eta$-transversality: at each point, either $|s|\ge\eta$, or $\nabla s$ is surjective with a right inverse of norm $\le1/\eta$. It also has a perturbative form: any asymptotically holomorphic (AH) sequence becomes $\eta(\delta)$-transverse after an AH perturbation of $C^1$-size $<\delta$, where $\eta(\delta)=\delta(\log 1/\delta)^{-p}$.

**[A2]** D. Auroux, *A remark about Donaldson's construction of symplectic submanifolds*, J. Symplectic Geom. 1 (2002). This is the globalization principle for local, $C^1$-open properties that are achievable locally with polynomial-log estimates.

## 2. Part I: the configuration lemma

### Lemma 0 (compatible $J$ making a regularized SC divisor complex)

**Statement.** Suppose $C$ admits an $\omega$-regularization. Then there is an $\omega$-compatible $J$ for which every $C_a$, and hence every stratum, is $J$-complex.

**Proof.**
1. At $p$ in the open part of $C_I$, put $W=T_pC_I$. Let $\mathcal S_p$ be the set of compatible $J$ on $T_pM$ that preserve every $T_pC_i$, $i\in I$.
2. Such a $J$ preserves $W$. Being compatible, it also preserves $W^\omega$, and hence it preserves $N_i:=T_pC_{I-i}\cap W^\omega$.
3. By (R2), $T_pM=W\oplus\bigoplus N_i$ is $\omega$-orthogonal with symplectic blocks, and $T_pC_i=W\oplus\bigoplus_{j\neq i}N_j$. So $\mathcal S_p$ is the product of the spaces of compatible complex structures on the blocks, which is nonempty and contractible.
4. This orthogonality holds at every point of $C_I$, including points inside tubes of deeper strata, because (R2) holds on the zero section of each tube.
5. For $I'\subset I$ we have $\mathcal S^{I}_p\subset\mathcal S^{I'}_p$, and $p\mapsto\mathcal S^{I'}_p$ is a locally trivial bundle with contractible fibres over $C_{I'}$.
6. Construct sections from the deepest strata upward, extending each time from a closed subset with contractible fibres. Finally extend over $M$ through the contractible space of compatible structures. ∎

### Proposition AH (Donaldson–Auroux with fixed twist, non-integral class, complex submanifolds)

**Statement.** Assume:
- $(M,\omega)$ is closed, $J$ is $\omega$-compatible, and $g=\omega(\cdot,J\cdot)$;
- $E=\bigoplus_bE_b$ is a fixed Hermitian bundle;
- $P_k$ are Hermitian line bundles with connections whose curvature satisfies $|F_k+2\pi ik\omega|_{C^r(g)}=O(1)$;
- $\Sigma_1,\dots,\Sigma_m$ are closed, exactly $J$-complex submanifolds. $M$ itself may be one of them.

Then for $k\gg0$ there are AH sections $s_k=(s_b)$ of $E\otimes P_k$ and an $\eta>0$, independent of $k$, such that for every subset $S$ of summands and every $j$, the restriction $(s_b|_{\Sigma_j})_{b\in S}$ is $\eta$-transverse to $0$ on $\Sigma_j$.

**Proof.**
- *Step A (the curvature error is invisible).*
  - In Darboux coordinates at $p$ with $J_p$ standard, choose a gauge on the ball of radius $Rk^{-1/2}$ with connection form $A=A_0+A_{err}$. Here $A_0$ is the standard form for $-2\pi ik\omega$, and $A_{err}=O(|x|)$ in radial gauge, since $dA_{err}=O(1)$.
  - In rescaled coordinates $y=\sqrt k\,x$ this gives $A_{err}=O(|y|/k)\,dy$, with all $y$-derivatives $O(1/k)$.
  - Donaldson's local estimates tolerate errors of size $O(k^{-1/2})\cdot\mathrm{poly}(|y|)$. So all local estimates of [D] and [A1] hold verbatim.
  - Integrality of $[\omega]$ is used only to have the bundle $P_k$, which is given. Twisting by a fixed $E$ is the setting of [A1].
- *Step B (one condition $(S,\Sigma)$).*
  - $\Sigma$ is $J$-complex and symplectic. By Weinstein's neighbourhood theorem and linear algebra at $p$, there are Darboux coordinates in which $\Sigma=\mathbb C^d\times0$ and $J_p$ is standard.
  - In these coordinates, the Gaussian reference sections $\sigma_{k,p}$ restrict to the reference sections of $P_k|_\Sigma$.
  - Restrictions of AH sections are AH, because $J$ preserves $T\Sigma$, so $\bar\partial_\Sigma(s|_\Sigma)=(\bar\partial s)|_\Sigma$.
  - The curvature of $P_k|_\Sigma$ is $-2\pi ik\omega|_\Sigma+O(1)$.
  - So the local step of [A1] on $\Sigma$ applies. It uses Yomdin's quantitative Sard lemma for approximately holomorphic $\mathbb C^{r}$-valued maps. The perturbations are global sections localized near points of $\Sigma$.
  - The globalization of [A1]/[A2] uses a $k$-independent number of colours of balls, together with Gaussian decay, which holds on $M$.
  - Hence the condition $(S,\Sigma)$ holds after an AH perturbation of $C^1$-size $\le\delta$, with constant $\eta(\delta)$.
- *Step C (finitely many conditions).*
  - List the pairs $(S,\Sigma_j)$ as $\mathcal P_1,\dots,\mathcal P_N$.
  - $\eta$-transversality is $C^1$-open: a $C^1$-perturbation of size $<\eta/2$ keeps it with constant $\eta/2$, by a Neumann series for the right inverse. Restriction to $\Sigma$ does not increase norms.
  - Inductively, apply Step B to $\mathcal P_{i+1}$ with $\delta=\eta_i/4$, and set $\eta_{i+1}=\min(\eta_i/2,\eta(\eta_i/4))$.
  - Then $\eta_N>0$ is independent of $k$. Sub-tuples are listed separately because transversality of a tuple does not imply transversality of its sub-tuples. ∎

### Lemma AH′ (near-complex strata are symplectic and positive)

**Statement.** Work in the rescaled metric. Let $V$ be a $J$-complex subspace, and let $A+B:V\to\mathbb C^r$ satisfy:
- $A=\partial s$ is complex linear;
- $|B|=|\bar\partial s|\le ck^{-1/2}$;
- $A+B$ is surjective with a right inverse of norm $\le1/\eta$.

Then for $k$ large:
- (a) $\ker(A+B)$ lies within angle $O(k^{-1/2}/\eta)$ of the complex subspace $\ker A$;
- (b) $\ker(A+B)$ is $\omega$-symplectic, and its zero-set orientation equals its symplectic orientation.

**Proof.**
- For $t\in[0,1]$, $A+tB$ has a right inverse of norm $\le2/\eta$ by a Neumann series. So the kernels $K_t$ form a continuous family of subspaces of constant dimension, each within angle $O(k^{-1/2}/\eta)$ of $K_0=\ker A$.
- On $K_0$, $\omega(v,Jv)=|v|^2$. So $\omega|_{K_t}$ is nondegenerate for all $t$ once $k$ is large.
- The zero-set orientation and the symplectic orientation of $K_t$ both vary continuously in $t$. They agree at $t=0$, where both are complex orientations, so they agree at $t=1$.
- All factors in the iterated intersection have even codimension, so no ordering signs arise. ∎

### Lemma 1 (configuration lemma)

**Statement.** After a permitted deformation of $\omega$ there is an SC divisor $C=\{C_a\}_{a\in A}\supseteq D$ with the following properties:
- $C$ is transverse, and every stratum is symplectic and positive;
- there is a level function $\ell:A\to\{0,\dots,n-1\}$ with $\ell^{-1}(0)=$ the components of $D$;
- each $a$ with $\ell(a)\le n-2$ has two partners $a^+\neq a^-$ of level $\ell(a)+1$;
- every component of level $\ge1$ is a partner of exactly one parent $p(b)$;
- $\mathrm{PD}[C_a]=\mathrm{PD}[C_{a^+}]-\mathrm{PD}[C_{a^-}]$ in $H^2(M;\mathbb Z)$, torsion included;
- the final form admits a regularization of $C$.

**Proof.** By induction on the level. Suppose $C_{\le l}$ is SC for the current form $\omega_l$.

1. *Regularize.* Apply (TMZ) to $C_{\le l}$. This is a permitted deformation: the class is fixed, and $C_{\le l}$ stays SC, so its subcollection $D$ stays SC. Lemma 0 then gives an $\omega_l$-compatible $J_l$ for which all strata of $C_{\le l}$ are exactly $J_l$-complex.
2. *Integrality.* The image $\Lambda$ of $H^2(M;\mathbb Z)$ in $H^2(M;\mathbb R)$ is a full lattice.
   - Choose $c_k\in H^2(M;\mathbb Z)$ whose image lies within bounded distance of $k[\omega_l]$.
   - Let $\eta_k$ be the harmonic representative of $(c_k-k[\omega_l])/k$, so $|\eta_k|_{C^r}=O(1/k)$.
   - Let $P_k$ be a line bundle with $c_1(P_k)=c_k$ and a connection of curvature $-2\pi ik(\omega_l+\eta_k)$.
3. *Sections.* For each $a$ of level $l$, let $L_a$ be a line bundle with $c_1(L_a)=\mathrm{PD}[C_a]$.
   - Apply Proposition AH with $E=\bigoplus_a(L_a\oplus\underline{\mathbb C})$, $J=J_l$, $\omega=\omega_l$, and $\Sigma$ ranging over $M$ and all strata of $C_{\le l}$.
   - This gives sections $s_a^+$ of $L_a\otimes P_k$ and $s_a^-$ of $P_k$. Set $C_{a^\pm}:=Z(s_a^\pm)$, oriented so that $\mathrm{PD}[Z(s)]=c_1$.
   - Then $\mathrm{PD}[C_{a^+}]-\mathrm{PD}[C_{a^-}]=c_1(L_a)+c_k-c_k=\mathrm{PD}[C_a]$ integrally.
4. *Transversality.* Transversality of every sub-tuple restricted to every old stratum is exactly the transversality of $C_{\le l+1}$. Transverse hypersurfaces cannot share components, so the new hypersurfaces are distinct from each other and from the old ones.
5. *Symplectic and positive.*
   - Each new stratum is cut out on an exactly $J_l$-complex old stratum by an $\eta$-transverse AH tuple.
   - By Lemma AH′ it is $\omega_l$-symplectic, and its intersection orientation equals its symplectic orientation.
   - The zero-set orientation of $C_{a^\pm}$ is also its symplectic orientation, so the orientation used in the PD identity is the symplectic one.
   - Only $\omega_l$ serves as the symplectic form. The form $\omega_l+\eta_k$ only shapes the curvature of $P_k$.
6. *Iteration.* Each level gets its own TMZ step, its own $J_l$, and its own $k$. Stop at level $n-1$.
   - Concatenated TMZ paths form a permitted deformation, and $D$ stays SC along them.
   - The PD relations are topological, so they survive later deformations.
   - A last application of TMZ to the whole of $C$ produces a regularization. ∎

## 3. Part II: setting and local lemmas

From now on, $\omega$ denotes the final form, and $C$ carries a regularization satisfying (R1)–(R4).

**Lemma A.** Let $(B,J_B)$ be almost complex, $E=\bigoplus L_i\to B$ a sum of line bundles with connection $\nabla$, $s_i$ frames with $\nabla s_i=\theta_is_i$, and $z_i$ the corresponding fibre coordinates. Define $J_\nabla$ on the total space of $E$ as the horizontal lift of $J_B$ on horizontal spaces and $i$ on the fibres. Then:
- $z_i$ is $J_\nabla$-holomorphic if and only if $\theta_i$ is of type $(1,0)$;
- $\pi$ is $(J_\nabla,J_B)$-holomorphic.

**Proof.**
- A section $zs_i$ is parallel iff $(dz+z\theta_i)s_i=0$. So the horizontal space is $\ker(dz_i+z_i\theta_i)_i$.
- On vertical vectors $dz_i$ is $\mathbb C$-linear. On horizontal lifts, $dz_i=-z_i\pi^*\theta_i$, so $dz_i\circ J_\nabla=i\,dz_i$ there iff $\theta_i\circ J_B=i\theta_i$.
- $d\pi$ kills vertical vectors and maps horizontal lifts identically, which gives the second claim. ∎

**Lemma Ch (Chern connection on an almost complex base).** Let $L\to(B,J_B)$ have a holomorphic atlas: frames $s_\alpha=g_{\alpha\beta}s_\beta$ with $J_B$-holomorphic $g$. Let $h$ be a Hermitian metric and $h_\alpha=|s_\alpha|^2$. Then:
- $\theta_\alpha:=\partial\log h_\alpha$ defines a unitary connection, with $(1,0)$ connection forms in holomorphic frames;
- if $\pi:(B',J')\to(B,J_B)$ is pseudo-holomorphic, the Chern connection of $(\pi^*L,\pi^*h)$ with the pulled-back atlas is $\pi^*\nabla^{Ch}$.

**Proof.**
- *Transition rule.* $\log h_\alpha=\log h_\beta+\log g+\log\bar g$. Since $g$ is holomorphic, $d\log g$ is $(1,0)$; and $\partial\log\bar g=\overline{(d\log g)^{0,1}}=0$. So $\theta_\alpha=\theta_\beta+d\log g$, which is the transformation rule of $\nabla s_\alpha=\theta_\alpha s_\alpha$, because $\nabla(gs_\beta)=(dg/g+\theta_\beta)gs_\beta$.
- *Unitary.* $\theta+\bar\theta=d\log h_\alpha$.
- *Pullback.* $\pi^*$ preserves types when $d\pi\circ J'=J_B\circ d\pi$.
- No integrability is used. ∎

**Lemma D (iterated connection structures).** For connections $\nabla_1,\nabla_2$ on $E_1,E_2\to(B,J_B)$, put $J_1=J_{\nabla_1}$. Then the structure on the total space of $\pi_1^*E_2\to(E_1,J_1)$ built from $\pi_1^*\nabla_2$ equals $J_{\nabla_1\oplus\nabla_2}$.

**Proof.** Write $w\in T_{e_1}E_1$ as $w=h_1(v)+u$ with $u$ vertical.
- The $\pi_1^*\nabla_2$-horizontal lift of $h_1(v)$ is the $(\nabla_1\oplus\nabla_2)$-lift of $v$.
- The lift of $u$ is $(u,0)$.
- Since $J_1w=h_1(J_Bv)+iu$, the two structures agree on horizontal spaces. Both are $i$ on the $E_2$-fibres. ∎

**Lemma B′ (tameness for any connection).** Let $B\subset(X,\omega)$ be a symplectic submanifold with a tubular map $\Psi$ whose splitting along $B$ is $\omega$-orthogonal and $\omega$-positive on the normal lines, as in (R2). Then for every connection $\nabla$ and every $\omega|_B$-tame $J_B$, $\Psi_*J_\nabla$ is $\omega$-tame near $B$.

**Proof.**
- At the zero section, horizontal spaces are tangent to $B$, so $J_\nabla=J_B\oplus i\oplus\dots\oplus i$ there, independently of $\nabla$.
- For $v=b+\sum n_a\neq0$, $\omega(v,Jv)=\omega(b,J_Bb)+\sum\omega(n_a,in_a)>0$.
- Tameness is open and $B$ is compact. ∎

## 4. Bookkeeping and global bundles

**Needed index sets.** Call $I\subset A$ *needed* if $C_I\ne\emptyset$ and $p(b)\in I$ for every $b\in I$ with $\ell(b)\ge1$. Here $\emptyset$ is needed, with $C_\emptyset=M$. For needed $I$, put
$$B_I=\{b\notin I:\ C_{I\cup b}\neq\emptyset,\ \ell(b)=0\text{ or }p(b)\in I\}.$$

Facts:
- $I\cup b$ is needed for $b\in B_I$.
- If $b,c\in B_I$ and $C_{I\cup\{b,c\}}\neq\emptyset$, then $c\in B_{I\cup b}$ and $I\cup\{b,c\}$ is needed.
- If $a\in I$ and $C_{I\cup a^\pm}\neq\emptyset$, then $I\cup a^\pm$ is needed.
- A needed $I$ containing a level-$(n-1)$ element contains its whole ancestor chain, which has $n$ elements. Then $|I|=n$ by transversality, and $C_I$ is finite. Consequently, if $\dim C_I>0$, every $a\in I$ has $\ell(a)\le n-2$ and therefore has partners.

**Global divisor bundles.** For $c\in A$, let $\mathcal O_M(c)$ be $\pi_c^*N_c$ on $U_c$, glued to the trivial bundle on $M-C_c$ by the tautological section. Its canonical section $s_c$ vanishes transversally exactly on $C_c$, and $c_1=\mathrm{PD}[C_c]$.

By (R3)/(R4) there are canonical isomorphisms $\mathcal O_M(c)|_{U_K}\cong\pi_K^*(\mathcal O_M(c)|_{C_K})$:
- for $c\in K$, via $N_c|_{C_c}\cong\pi^*(N_c|_{C_K})$;
- for $c\notin K$, as bundles with section, via $z_c\mapsto z_c$; if $C_{K\cup c}=\emptyset$, via the frame $s_c$.

These isomorphisms are compatible for $K\subset K'$. Restricted to $C_I$:
- if $c\in I$, $\mathcal O_M(c)|_{C_I}=N_c|_{C_I}$;
- if $c\notin I$, $\mathcal O_M(c)|_{C_I}$ is the divisor bundle of $C_{I\cup c}\subset C_I$ with section $s_c$.

Complex line bundles are classified by $c_1\in H^2(M;\mathbb Z)$. So the integral relation of Lemma 1 gives smooth isomorphisms $\Phi^0_a:\mathcal O_M(a)\to\mathcal O_M(a^+)\otimes\mathcal O_M(a^-)^*$ for every $\ell(a)\le n-2$.

**Lemma F.** After shrinking tubes, $\Phi_a$ can be chosen *pulled back*: $\Phi_a|_{U_K}=\pi_K^*(\Phi_a|_{C_K})$ for every $K$.

**Proof.** Order strata by decreasing codimension, and assume $\Phi$ is pulled back near all strata deeper than $C_K$. Set $u=\Phi/\pi_K^*(\Phi|_{C_K}):U_K\to\mathbb C^*$.
- $u=1$ on $C_K$.
- On $U_K\cap U_{K'}$ for deeper $K'\supset K$, both maps are pulled back from $C_{K'}$, because $\pi_{K'}\circ\pi_K=\pi_{K'}$. Here thin tubes ensure $\pi_K(x)\in U_{K'}$. So $u=1$ there.
- The fibres of $U_K$ are discs, so $f=\log u$ is defined by continuation from the zero section, and $f=0$ on $C_K$ and near deeper strata.
- Replace $\Phi$ by $e^{-\chi f}\Phi$, where $\chi$ is a radial cutoff equal to $1$ on a thinner tube.
- This leaves $\Phi$ unchanged near deeper strata. Tubes of other strata of the same codimension meet $U_K$ only inside deeper tubes (R4), where $f=0$. ∎

## 5. The induction over needed strata

We construct, for needed $I$ by decreasing $|I|$:
- (a) an $\omega|_{C_I}$-tame $J_I$ on $C_I$;
- (b) holomorphic structures (atlases with $J_I$-holomorphic transitions) $\mathcal H_{I;a}$ on $N_a|_{C_I}$, $a\in I$.

On 0-dimensional strata everything is vacuous.

**Invariants.**
- **(C1)** For $b\in B_I$, near $C_{I\cup b}$ in $C_I$: $J_I=J_\nabla$ built from $J_{I\cup b}$ and the Chern connection of $(\mathcal H_{I\cup b;b},\rho)$ on $N_b|_{C_{I\cup b}}$.
- **(C2)** For $a\in I$ and $b\in B_I$: near $C_{I\cup b}$, $\mathcal H_{I;a}=\pi^*\mathcal H_{I\cup b;a}$.
- **(C3)** For $a\in I$ (with $\dim C_I>0$), $\mathcal H_{I;a}=(\Phi_a|_{C_I})^*\big(\text{holomorphic structure of }\mathcal O_I(a^+)\otimes\mathcal O_I(a^-)^*\big)$. Here $\mathcal O_I(\cdot)$ is defined in Step (b).

**Tube-radius convention** (a repair found by audit). The construction proceeds from deep to shallow strata. After $J_{I\cup b}$ has been fixed for all $b\in B_I$, shrink the radius functions of the tubes of the $C_{I\cup b}$ in $C_I$ so that $U_{I\cup b}\cap U_{I\cup c}$ projects into the region of $C_{I\cup b}$ where $J_{I\cup b}$ already has its $C_{I\cup\{b,c\}}$-model form.
- This is possible: as the radii tend to $0$, the intersection shrinks to $C_{I\cup\{b,c\}}$ by compactness.
- Regularizations restrict to smaller radii and stay compatible.
- The $J_\nabla$ model is defined on the whole disc bundle, so shrinking never breaks (C1).

**Step (a): $J_I$.** (C1) prescribes $J_I$ near each $C_{I\cup b}$.

*Agreement on overlaps.* Tubes of $C_{I\cup b}$ and $C_{I\cup c}$ meet only near $C_K$, $K=I\cup\{b,c\}$, which is needed. There:
- by (C1) at stage $I\cup b$, $J_{I\cup b}$ is $J_\nabla$ over $(C_K,J_K)$ for $N_c$, so $\pi:C_{I\cup b}\supset\text{tube}\to C_K$ is pseudo-holomorphic (Lemma A);
- by (C2) at stage $I\cup b$, $\mathcal H_{I\cup b;b}=\pi^*\mathcal H_{K;b}$, and the metrics are pulled back (R3);
- Lemma Ch makes the Chern connection on $N_b|_{C_{I\cup b}}$ the pullback of the Chern connection on $N_b|_{C_K}$;
- Lemma D identifies the prescribed structure with $J_\nabla$ for $N_b\oplus N_c$ over $(C_K,J_K)$ with Chern connections.

This description is symmetric in $b$ and $c$, so the two prescriptions agree. Compatibility of the charts $\Psi$ is (R3).

*Extension.* By Lemma B′ inside $(C_I,\omega|)$, using (R2) and the tameness of $J_{I\cup b}$, the prescribed structure is tame near the deeper strata. Tame structures form a bundle with contractible fibres, so after shrinking, $J_I$ extends to an $\omega|_{C_I}$-tame structure on all of $C_I$. This is the only extension performed, and it is unobstructed.

**Step (b): the bundles $\mathcal O_I(c)$.**

*Case $c\notin I$ with $I\cup c$ needed.* Let $\mathcal O_I(c)$ be the divisor bundle of $C_{I\cup c}$ in $C_I$ with the atlas:
- the frame $s_c$ on $C_I-C_{I\cup c}$;
- on the thin tube, frames $e_\alpha$ with $s_c=z^{(\alpha)}e_\alpha$. Here $z^{(\alpha)}$ is the fibre coordinate with respect to a holomorphic frame $\sigma_\alpha$ of $\mathcal H_{I\cup c;c}$.

All transition functions are $J_I$-holomorphic:
- each $z^{(\alpha)}$ is $J_I$-holomorphic, by (C1), Lemma A and Lemma Ch;
- each ratio $z^{(\alpha)}/z^{(\beta)}=\pi^*g_{\beta\alpha}$ is $J_I$-holomorphic.

As a smooth bundle with section, $\mathcal O_I(c)$ is $\mathcal O_M(c)|_{C_I}$. No removable-singularity argument is needed, since the transitions are explicit.

*Case $c\notin I$ with $C_{I\cup c}=\emptyset$* (repair found by audit). Then $s_c$ is nowhere zero on $C_I$. Let $\mathcal O_I(c)$ be the trivial bundle with the single global frame $s_c$; it is trivially holomorphic.

*Case $c\in I$.* Set $\mathcal O_I(c)=(N_c|_{C_I},\mathcal H_{I;c})$.

**Step (b): the structures $\mathcal H_{I;a}$.** Define $\mathcal H_{I;a}$ by (C3), proceeding through $a\in I$ in decreasing level. The definition uses:
- $\mathcal H_{I;a^\pm}$ only when $a^\pm\in I$, which has higher level and is already defined;
- otherwise data from $I\cup a^\pm$, which is needed and deeper, or nothing at all (the empty case).

Tensor products and duals of holomorphic atlases are holomorphic atlases.

**Verification of (C2).** Fix $b\in B_I$. Near $C_{I\cup b}$ we show $\mathcal O_I(c)\cong\pi^*\mathcal O_{I\cup b}(c)$ holomorphically, under the identifications restricted from $\mathcal O_M(c)|_{U_{I\cup b}}\cong\pi^*\mathcal O_M(c)|_{C_{I\cup b}}$.
- **$c=b$.** The divisor bundle of the zero section of a line bundle $N$ is $\pi^*N$ with the tautological section $\tau=z^{(\alpha)}\pi^*\sigma_\alpha$. So $e_\alpha\leftrightarrow\pi^*\sigma_\alpha$.
- **$c\notin I\cup b$.** Near $C_{I\cup b}$, $C_{I\cup c}=\pi^{-1}(C_{I\cup b\cup c})$, by (R3)/(R4).
  - If this stratum is nonempty, then $c\in B_{I\cup b}$ and $b\in B_{I\cup c}$. By (C2) at stage $I\cup c$, $\mathcal H_{I\cup c;c}=\pi^*\mathcal H_{K;c}$, so the frames may be taken pulled back. Since $z_c$ is preserved by $\pi$, the frames $e_\alpha$ are pulled back, and the two atlases generate the same maximal atlas.
  - If it is empty, both sides are trivialized by $s_c$.
- **$c\in I$.** This is (C2) for $c$, which has higher level, by induction on level.

By Lemma F, $\Phi_a|_{C_I}=\pi^*(\Phi_a|_{C_{I\cup b}})$ near $C_{I\cup b}$ under the same identifications. Hence (C2) holds for $a$.

No holomorphic structure is ever produced by solving a $\bar\partial$-equation or extended from a neighbourhood of deeper strata. Every $\mathcal H_{I;a}$ is given globally by the explicit formula (C3). Agreement with deeper data, (C2), is verified, not imposed. The only global input is the integral identity of Chern classes, which Part I supplies.

## 6. Conclusion (stage $I=\emptyset$)

On $M$, $B_\emptyset$ is the set of components of $D$. Let $J:=J_\emptyset$; it is $\omega$-tame by Lemma B′ near $D$ and by the extension elsewhere.

Fix $K\subset A_0$ with $D_K\neq\emptyset$. Applying (C1), (C2), Lemma Ch and Lemma D repeatedly along $K$ shows that near $D_K$, $J$ is $J_\nabla$ on $N_K=\bigoplus_{k\in K}N_k|_{D_K}$ over $(D_K,J_K)$, with the Chern connections of the $\mathcal H_{K;k}$.

Let $p\in D_K$ lie on no other $D_j$, and put $r=|K|$.
- Take $z_k$, $k\in K$, to be the fibre coordinates with respect to local holomorphic frames of $\mathcal H_{K;k}$. They are $J$-holomorphic by Lemmas A and Ch, and $D_k=\{z_k=0\}$ by (R1).
- The other components of $D$ avoid a neighbourhood of $p$, so $D=\{z_1\cdots z_r=0\}$ there.
- Complete the chart by $\pi_K^*$ of arbitrary smooth complex coordinates on $D_K$. This gives a chart because $\Psi_K$ is a diffeomorphism and the $z_k$ are $\mathbb C$-linear coordinates on the fibres.
- Off $D$ take $r=0$.

The partner components of $C$ play no role in the final charts. The only change to $\omega$ is the concatenation of TMZ deformations, which is permitted. ∎ (Theorem 1)

## 7. Status

- **Main claim (Theorem 1): proved, modulo published results quoted from memory.** Two independent referee passes found no genuine gap in the chain of Lemma 1 plus §§3–6. They found two small omissions, both repaired above: the tube-radius convention in §5, and the trivial bundle used when $C_{I\cup c}=\emptyset$. I re-checked each step while writing this document; the lemmas were re-derived and the counterexample arithmetic was checked by computer.
- **Clearly marked hedges (citation level, not mathematical gaps found):**
  1. **(TMZ) exact statement.** The weak homotopy equivalence and the regularization axioms are as recalled in §1. The **cohomologous clause** (the deformation is $\omega+d\mu_t$ supported near $C$) is recalled and sketched, not verified against the paper. The domain conventions (R4) are derived by shrinking.
  2. **[D], [A1], [A2] in the forms stated.** Proposition AH is derived from them in §2. That derivation depends on the recalled perturbative form of [A1] and the globalization principle of [A2]. The combined statement (fixed twist, $O(1)$ curvature error, all sub-tuples on finitely many complex submanifolds) is, to my knowledge, not published as one theorem.
- **Proposition 0 / the example:** proved. Positivity is necessary, and without it the answer is NO.

## 8. Other routes recorded

- **Necessity.** If $J$ admits such charts, the ratio of two $J$-holomorphic defining functions of $D_i$ extends to a nonvanishing $J$-holomorphic function across $D_i$. So $N_{D_i}$ carries a cocycle of $J|_{D_i}$-holomorphic transition functions. For $n\ge3$ this fails for generic $J$, so the deformation and the special choice of $J$ are essential.
- **Smooth divisor reduction.** For a single smooth $D$, the problem reduces to finding an $\omega_D$-tame $J_D$ for which $N_D$ has a holomorphic cocycle (a "line bundle lemma"). This was proved when $\dim_{\mathbb R}D=2$. It is subsumed by Theorem 1, whose partner construction supplies divisor-induced structures.
- **Dimension 4.** Here the strata $D_i$ are surfaces, on which every almost complex structure is integrable. Chern connections of integrable $\bar\partial$-operators, standard near the crossing points, give the result directly after TMZ. This serves as a sanity check of Theorem 1.
- **Relative line bundle route.** Extend holomorphic cocycles relative to deeper strata. This was abandoned (not refuted) because of a possible $\mathrm{Pic}^0$-type relative obstruction, which the configuration route avoids entirely.
- **Weakening of (R).** The assembly uses $\omega$ only through Lemma B′. Orthogonality and positivity of the normal directions at the zero sections suffice, together with a compatible smooth regularization; the metrics $\rho$ may be arbitrary but compatible.
