# Minimax rate for Darcy's problem near the constant conductivity

## Answer

For every $\alpha>1$, $d\ge 2$ and every fixed $r\in(0,r_0]$ with $r_0=r_0(d,\alpha)>0$ small, the minimax rate up to logarithmic factors is

$$\inf_{\hat f}\sup_{f\in\mathcal F(\alpha,r)}E_f\|\hat f-f\|_{L^2(D)}^2\ \asymp\ n^{-2\alpha/(2\alpha+d+3)} .$$

**Theorem.** Fix $\alpha>1$ and $d\ge2$. There are constants $r_0>0$, $c,C>0$ and $n_0$, depending only on $d$, $\alpha$, $r$ and fixed auxiliary profiles and kernels, such that the following hold for $n\ge n_0$.

- **(Lower bound.)** For every $r\in(0,1)$,
  $\inf_{\hat f}\sup_{\mathcal F(\alpha,r)}E\|\hat f-f\|_2^2\ \ge\ c\,n^{-2\alpha/(2\alpha+d+3)}$.
- **(Upper bound.)** For every $r\in(0,r_0]$, an explicit estimator $\tilde f$ satisfies
  $\sup_{\mathcal F(\alpha,r)}E\|\tilde f-f\|_2^2\le C(\log n)^4\,n^{-2\alpha/(2\alpha+d+3)}$.
  When $\alpha$ is not an integer, the factor $(\log n)^4$ can be dropped.

**Where $d+3$ comes from.** Near $f=\mathbf 1$ we have $\nabla u_f\approx x/d$, a radial field with a single source. The linearised forward map $h\mapsto -L_f^{-1}\mathrm{div}(h\nabla u_f)$ therefore behaves like
- smoothing of order 2 for perturbations that oscillate across the rays (in the $d-1$ angular directions), and
- smoothing of order only 1 along the rays.

The Fourier symbol of the linearisation at $f=1$ is $\asymp(1+|\xi_{\rm rad}|)/|\xi|^2$. This gives $d+3$ in the denominator, between the isotropic $d+4$ and $d+2$.

**Conventions.** $C^s$ is the Hölder–Zygmund space $B^s_{\infty\infty}$. On $D$ it means restrictions with the quotient norm. Constants $c,C$ never depend on $j$, $J$, $n$ or on $f\in\mathcal F(\alpha,r)$. $u_1:=(|x|^2-1)/(2d)$ solves the problem for $f=\mathbf 1$, and $\nabla u_1=x/d$. In the white-noise model, $\mathrm{KL}(P_{f},P_{g})=\tfrac n2\|u_f-u_g\|_2^2$.

**Standard facts cited, not re-proved here** (all are textbook results):
- (E1) Global $H^2$ regularity (Gilbarg–Trudinger, Thms 8.12–8.13). Let $g\in C^{0,1}(\bar D)$ with $g\ge 1-r$. The solution $w\in H^1_0$ of $\mathrm{div}(g\nabla w)=F$ satisfies $\|w\|_{H^2}\le C\|F\|_2$, where $C$ depends on $\|g\|_{C^{0,1}}$ and $1-r$.
- (E2) $W^{2,p}$ theory, $1<p<\infty$ (GT Thm 9.15, Lemma 9.17). This applies to $g\Delta w+\nabla g\cdot\nabla w$ with $g\in C^1$, $g\ge1-r$, and Dirichlet data. The constant is uniform over the class $\mathcal F(\alpha,r)$, which is bounded in $C^\alpha$ and hence precompact in $C^1$.
- (GN) Gagliardo–Nirenberg on the ball. For $p>d$ and $t=(1+d/p)/2$,
  $\|\nabla w\|_\infty\le C\|w\|_{W^{2,p}}^t\|w\|_p^{1-t}+C\|w\|_p$.
- (As) Assouad's lemma (Tsybakov, *Introduction to Nonparametric Estimation*, Thm 2.12(ii)).
- (C1) Seeley extension. There is a linear $E$ with $Eg=g$ on $D$, bounded $C^s(D)\to C^s(\mathbb R^d)$ for $0<s\le S_0$ (with $S_0>\alpha+2$). It has the form
  $Eg(t)=\chi(|t|)\sum_i a_i\,g(R_it)$ for $|t|>1$, with $R_it=(1-\lambda_i(|t|-1))t/|t|$, $\lambda_i>0$, and $\chi$ a smooth cutoff vanishing for $|t|\ge1+\eta$.
- (C2) Kernel approximation. Let $k\in C_c^\infty$ with $\int k=1$ and vanishing moments of orders $1,\dots,S$, where $S\ge2\alpha+2$. Put $k_J=2^{Jd}k(2^J\cdot)$. Then
  $\|D^m(k_J*g-g)\|_\infty\le C2^{-J(s-m)}\|g\|_{C^s}$ for $0\le m<s$.
- (LP) Littlewood–Paley characterisation, $\|g\|_{C^s}\asymp\sup_j2^{js}\|\Delta_jg\|_\infty$ for $s>0$; the Bernstein inequality $\|D^m\Delta_jg\|_\infty\le C2^{jm}\|\Delta_jg\|_\infty$; and the embedding $C^s\subset C^{1,\beta}$ for $s>1$, with $\beta=\min(s-1,1/2)$.
- (C3) Zygmund Taylor formula and algebra property. Let $A\in C^a$, $a>0$, and $|h|\le1$. Then
  $\Delta_hA(x):=A(x+h)-A(x)=P_A(x,h)+r_A(x,h)$,
  where $P_A$ is the Taylor polynomial with monomials of degree $1\le|\gamma|<a$, and $|r_A|\le C|h|^a(1+\log(1/|h|))$; the logarithm is needed only when $a$ is an integer. Also $C^a\cdot C^a\subset C^a$.
- (S) Zygmund–Schauder for the Dirichlet Laplacian on the ball: $\Delta_D^{-1}:C^{\alpha-1}(D)\to C^{\alpha+1}(D)$ is bounded for $\alpha-1>0$.
- (ODE) $C^k$ dependence of flows on initial data, with the variational equations.
- (G) Gaussian facts:
  - smooth versions of Gaussian fields with smooth $L^2$-valued index maps, with $D^mW(\varphi_y)=W(\partial_y^m\varphi_y)$;
  - Bochner integrals commute with $W$;
  - Dudley's entropy bound and the Borell–TIS inequality.

---

# Part I. Lower bound (all $\alpha>1$, $d\ge2$, $r\in(0,1)$)

## I.1 The hypercube

**Directions and bumps.**
- Choose $\omega_1,\dots,\omega_M\in S^{d-1}$ with pairwise geodesic distance $\ge 2\cdot2^{-j}$ and $M\ge c_d2^{j(d-1)}$.
- Fix $\varphi_0\in C_c^\infty([0,1/2))$ that is constant near 0 and not identically 0.
- Let $\Phi_k(\omega)=\varphi_0(2^jd_S(\omega,\omega_k))$. These functions are smooth with pairwise disjoint supports, which are caps of radius $2^{-j}/2$. They are rotations of each other.

**Extension and scaling.**
- Extend $\Phi_k$ to $\mathbb R^d\setminus\{0\}$ as a function homogeneous of degree 0. Then $\Delta\Phi_k(x)=|x|^{-2}(\Delta_S\Phi_k)(x/|x|)$.
- Put $\chi_k:=2^{-2j}\Delta_S\Phi_k$. In rescaled normal coordinates this is the flat Laplacian of a fixed nonzero compactly supported bump, up to $O(2^{-j})$ metric corrections. Hence:
  - $\|\partial^m\chi_k\|_\infty\le C_m2^{jm}$;
  - for $j\ge j_0$, $c2^{-j(d-1)}\le\|\chi_k\|^2_{L^2(S)}\le C2^{-j(d-1)}$. The Laplacian of a nonzero compactly supported function is nonzero, and the value does not depend on $k$ by rotation invariance.

**The perturbations.** Fix $b\in C_c^\infty((1/4,3/4))$, not identically 0. Define
$$h_k(x):=\kappa2^{-j(\alpha+2)}b(|x|)\Delta\Phi_k(x)=\kappa2^{-j\alpha}b(|x|)|x|^{-2}\chi_k(x/|x|),$$
and for $\theta\in\{0,1\}^M$ put $f_\theta:=1+\sum_k\theta_kh_k$.

**Membership in $\mathcal F(\alpha,r)$.**
- Let $G_\theta=\sum\theta_k\chi_k$. Each point has a neighbourhood that meets at most one support, so $\|D^mG_\theta\|_\infty\le C2^{jm}$ and $\|G_\theta\|_\infty\le C$.
- Take an integer $m>\alpha$. Then $|\Delta_h^m(2^{-j\alpha}G_\theta)|\le C2^{-j\alpha}\min((2^j|h|)^m,1)\le C|h|^\alpha$.
- Hence $\|2^{-j\alpha}G_\theta\|_{C^\alpha(S)}\le C$ uniformly in $\theta$ and $j$. Multiplying by the smooth function $b(|x|)|x|^{-2}$, which is supported in the annulus, keeps this bounded.
- Choosing $\kappa=\kappa(r)$ small gives $\|f_\theta-1\|_{C^\alpha(D)}\le r$, i.e. $f_\theta\in\mathcal F(\alpha,r)$.

**Sizes.**
- The supports $S_k$ of the $h_k$ are disjoint, so $\|f_\theta-f_{\theta'}\|_2^2=\sum_{k:\theta_k\ne\theta'_k}\|h_k\|_2^2$.
- In polar coordinates, $\|h_k\|_2^2=\kappa^22^{-2j\alpha}\int b^2\rho^{d-5}d\rho\,\|\chi_k\|^2_{L^2(S)}\asymp2^{-j(2\alpha+d-1)}$.
- Also $\|\Phi_k\|_{L^2(1/4<|x|<3/4)}\asymp2^{-j(d-1)/2}$ and $\|\sum\theta_k\Phi_k\|_\infty\le\|\varphi_0\|_\infty$.

## I.2 Key estimate

**Claim.** If $\theta,\theta'$ differ only in coordinate $k$, then $\|u_{f_\theta}-u_{f_{\theta'}}\|_2\le C2^{-2j}\|h_k\|_2$.

**Exact identity.** Let $f=f_{\theta'}$, $g=f_\theta=f+h$ with $h=\pm h_k$, and $V=\nabla u_f$. Subtracting the two equations gives $\mathrm{div}(g\nabla(u_g-u_f))=-\mathrm{div}(hV)$. Hence $u_g-u_f=-L_g^{-1}\mathrm{div}(hV)$, where $L_g=\mathrm{div}(g\nabla\cdot)$ with Dirichlet conditions.

**(i) Duality.** $L_g$ is self-adjoint on $H^1_0$, so
$$\|L_g^{-1}F\|_2=\sup_{\|\phi\|_2\le1}\langle F,\psi\rangle,\qquad \psi:=L_g^{-1}\phi,$$
and $\|\psi\|_{H^2}\le C$ by (E1); note $g\ge1-r$ and $g$ is Lipschitz since $\alpha>1$. It therefore suffices to show $|\langle\mathrm{div}(h_kV),\psi\rangle|\le C2^{-2j}\|h_k\|_2\|\psi\|_{H^2}$ for $\psi\in H^2\cap H^1_0$. Split $V=x/d+W$ with $W=\nabla(u_f-u_1)$.

**(ii) Radial part.**
- For $G=b(|x|)\Delta\Phi_k$, homogeneity of degree $-2$ gives
  $$\mathrm{div}(G\,x/d)=\tfrac1d(\rho\partial_\rho+d)G=c(|x|)\Delta\Phi_k,\qquad c=\frac{\rho b'+(d-2)b}{d}\in C_c^\infty(1/4,3/4).$$
  *Proof (all $d$).* By Euler's relation for the $(-2)$-homogeneous $\Psi:=\Delta\Phi_k$, $x\cdot\nabla G=\rho b'\Psi-2b\Psi$; and $\mathrm{div}(G\,x)=x\cdot\nabla G+dG$. Dividing by $d$ gives the formula.
- $c\psi$ has compact support in the annulus, where $\Phi_k$ is smooth. Integrating by parts twice,
  $$|\langle\mathrm{div}(h_kx/d),\psi\rangle|=\kappa2^{-j(\alpha+2)}\Big|\int\Phi_k\Delta(c\psi)\Big|\le C2^{-j(\alpha+2)}2^{-j(d-1)/2}\|\psi\|_{H^2}\le C2^{-2j}\|h_k\|_2\|\psi\|_{H^2}.$$

**(iii) Drift part.**
- Since $h_k$ has compact support, $|\langle\mathrm{div}(h_kW),\psi\rangle|=|\int h_kW\cdot\nabla\psi|\le\|h_k\|_2\|W\|_\infty\|\psi\|_{H^1}$. It suffices to show $\|W\|_\infty\le C2^{-j(\alpha+1-d/p)}$ for every $p>d$, and then take $d/p\le\alpha-1$.
- **Equation for $w$.** Let $w=u_f-u_1$. Then $\mathrm{div}(f\nabla w)=-\mathrm{div}((f-1)x/d)=-q$, and by (ii) applied termwise,
  $q=\kappa2^{-j(\alpha+2)}c(|x|)\Delta\Phi_{\theta'}$, with $\Phi_{\theta'}=\sum\theta'_l\Phi_l$.
- **$W^{2,p}$ bound.** Since $q=\kappa2^{-j\alpha}c|x|^{-2}\sum\theta'_l\chi_l$ and the $\chi_l$ are bounded with disjoint supports, $\|q\|_p\le C2^{-j\alpha}$. Hence $\|w\|_{W^{2,p}}\le C2^{-j\alpha}$ by (E2).
- **$L^p$ bound.** Take $\phi$ with $\|\phi\|_{p'}\le1$ and $\psi=L_f^{-1}\phi\in W^{2,p'}\cap W^{1,p'}_0$, so $\|\psi\|_{W^{2,p'}}\le C$ by (E2). By Green's identity,
  $$\Big|\int w\phi\Big|=\Big|\int q\psi\Big|=\kappa2^{-j(\alpha+2)}\Big|\int\Phi_{\theta'}\Delta(c\psi)\Big|\le C2^{-j(\alpha+2)}.$$
  So $\|w\|_p\le C2^{-j(\alpha+2)}$.
- **Interpolation.** By (GN),
  $\|W\|_\infty\le C2^{-j\alpha t}2^{-j(\alpha+2)(1-t)}+C2^{-j(\alpha+2)}\le C2^{-j(\alpha+1-d/p)}$.

Combining (ii) and (iii) proves the Claim. With the sizes from I.1,
$$\|u_\theta-u_{\theta'}\|_2^2\le C2^{-j(2\alpha+d+3)}.$$

## I.3 Assouad

**Choice of $j$.** $\mathrm{KL}(P_\theta,P_{\theta'})\le Cn2^{-j(2\alpha+d+3)}$. Choose $2^j\asymp n^{1/(2\alpha+d+3)}$ with a constant large enough that $\mathrm{KL}\le1/8$ for all neighbours. Pinsker then gives $\mathrm{TV}\le1/4$.

**Reduction to testing.**
- Given $\hat f$, let $\hat\theta_k$ minimise $\|(\hat f-1-th_k)1_{S_k}\|_2$ over $t\in\{0,1\}$.
- If $\hat\theta_k\ne\theta_k$, the triangle inequality gives $\|h_k\|_2\le2\|(\hat f-f_\theta)1_{S_k}\|_2$.
- Hence $\|\hat f-f_\theta\|_2^2\ge\frac14\sum_k\|h_k\|_2^2\,1\{\hat\theta_k\ne\theta_k\}$.

**Conclusion.** By (As),
$$\max_\theta E_\theta\|\hat f-f_\theta\|_2^2\ge\tfrac14\min_k\|h_k\|_2^2\cdot\tfrac M2\cdot\tfrac34\ge c2^{j(d-1)}2^{-j(2\alpha+d-1)}=c2^{-2j\alpha}\asymp n^{-2\alpha/(2\alpha+d+3)}.$$

The condition $\alpha>1$ is used only in (iii), and to make $f\in C^1$ for (E1) and (E2). ∎

---

# Part II. Upper bound ($r\le r_0(d,\alpha)$)

## II.0 Schauder bound (C4)

Write $L_f=\Delta+\mathrm{div}((f-1)\nabla\cdot)$.
- By the algebra property (C3), $\|\mathrm{div}((f-1)\nabla v)\|_{C^{\alpha-1}}\le C_1\|f-1\|_{C^\alpha}\|v\|_{C^{\alpha+1}}\le C_1r\|v\|_{C^{\alpha+1}}$.
- Take $r_0$ with $C_1r_0\|\Delta_D^{-1}\|\le1/2$. A Neumann series using (S) then shows that $L_f^{-1}:C^{\alpha-1}(D)\to C^{\alpha+1}(D)$ (with Dirichlet data) has norm $\le2\|\Delta_D^{-1}\|$.
- As in I.2, $u_f-u_1=-L_f^{-1}\mathrm{div}((f-1)x/d)$, and the right side has $C^{\alpha-1}$ norm $\le Cr$.

Hence
$$\|u_f-u_1\|_{C^{\alpha+1}(D)}\le Cr,\qquad\|u_f\|_{C^{\alpha+1}(D)}\le C.\tag{C4}$$
This is the first place where smallness of $r$ enters.

## II.1 Smoother, noise and estimator

**Resolution and smoother.** Let $J:=\lfloor\log_2n/(2\alpha+d+3)\rfloor$, so that
$n^{-1/2}\le2^{-J(\alpha+(d+3)/2)}$ and $n^{-1}2^{J(d+3)}\le2^{-2J\alpha}$.
Put $K_Jg:=(k_J*Eg)|_D$. On data, $K_JY(x)=\langle Y,k_J(x,\cdot)\rangle$, where $k_J(x,\cdot):=E^*[k_J(x-\cdot)]\in L^2(D)$.

$E^*$ is the identity on $D$ plus finitely many terms of the form $(\chi\varphi)(R_i^{-1}z)|\det DR_i^{-1}(z)|$, supported on shells $\{1-\lambda_i\eta<|z|<1\}$, with bounded Jacobians. Hence the following kernel bounds hold.
- **(K1)** $|\partial^a_xk_J(x,z)|\le C2^{J(d+|a|)}$ for $|a|\le4$.
- **(K2)** $\partial_x^ak_J(x,z)=0$ unless $|x-z|\le C_02^{-J}$. Indeed, if $t=R_i^{-1}z$, $|t|>1$, $x\in D$ and $|x-t|\le C2^{-J}$, then $|t|-1\le C2^{-J}$ and $|z-t|=(1+\lambda_i)(|t|-1)\le C2^{-J}$.
- **(K3)** $\|\partial^a_xk_J(x,\cdot)\|_2^2\le C2^{J(d+2|a|)}$, and $x\mapsto\partial_x^ak_J(x,\cdot)$ is Lipschitz into $L^2$ with constant $C2^{J(d/2+|a|+1)}$, for $|a|\le3$.

**Notation.**
- $U=Eu$, $F=Ef$, $V=\nabla u$, $V^E=\nabla U$. By (C1) and (C4), $\|F\|_{C^\alpha}+\|V^E\|_{C^\alpha}\le C$.
- $V_J:=\nabla K_Ju=(k_J*V^E)|_D$, the restriction of a $C^\infty$ field on $\mathbb R^d$, and $b:=K_Ju-u$.
- $\xi:=n^{-1/2}K_J\mathbb W$, a smooth centred Gaussian field by (G). It does not depend on $f$.
- $\hat V:=\nabla K_JY=V_J+\nabla\xi$.

**Good event.**
$$A:=\{\max_{|a|=m}\sup_D|\partial^a\xi|\le Jn^{-1/2}2^{J(d/2+m)},\ m=1,2,3\}.$$
On $A$, after adjusting constants for operator norms,
$$\|\nabla\xi\|_\infty\le CJ2^{-J(\alpha+1/2)},\quad\|D^2\xi\|_\infty\le CJ2^{-J(\alpha-1/2)},\quad\|D^3\xi\|_\infty\le CJ2^{-J(\alpha-3/2)}.$$

**Estimator.** Let $\varepsilon_0:=1/(8d)$ and define the observable event $B:=\{\|\hat V-x/d\|_{C^1(D)}\le\varepsilon_0\}$.
- On $B$, set $\hat f:=T_{\hat V}^{-1}\mathbf 1$ (defined in II.3); off $B$, set $\hat f:=1$.
- Let $\tilde f:=\min(\max(\hat f,1-r),1+r)$.
- Since $\|f-1\|_\infty\le r$, clipping can only decrease $|\tilde f-f|$ pointwise.

The estimator uses only $Y$, $n$, $\alpha$, $r$ and fixed kernels. The event $A$ itself is **not** observable: $\xi=n^{-1/2}K_J\mathbb W$ does not depend on $f$, but $\xi=K_JY-K_Ju$ cannot be computed from the data because $u$ is unknown. This is why the estimator is defined on $B$, and Lemma 1 shows $A\subset B$.

## II.2 Lemma 1 (fields)

**Lemma 1.1.** Let $g\in C^s(\mathbb R^d)$, $s>0$, and let $m\ge1$ be an integer. Then $\|D^m(k_J*g)\|_\infty$ is at most
- $C2^{J(m-s)}\|g\|_{C^s}$ if $m>s$,
- $C(J+1)\|g\|_{C^s}$ if $m=s$,
- $C\|g\|_{C^s}$ if $m<s$.

*Proof.*
1. $D^m(k_J*g)=\sum_j(D^mk_J)*\Delta_jg$, and the series converges uniformly because each term is $\le\|D^mk_J\|_1\|\Delta_jg\|\le C2^{Jm}2^{-js}\|g\|$.
2. For $j\le J$, write the term as $k_J*D^m\Delta_jg$. By Bernstein it is $\le C2^{j(m-s)}\|g\|$.
3. For $j>J$, step 1 bounds the term by $C2^{Jm-js}\|g\|$. Summing over $j>J$ gives $C2^{J(m-s)}\|g\|$.
4. Summing step 2 over $j\le J$ gives the three cases. ∎

**Lemma 1.** Let $\varepsilon\le\varepsilon_0$. There are $r_0$ and $J_0$ such that for $r\le r_0$ and $J\ge J_0$:
1. $\|V_J-x/d\|_{C^1(D)}\le\varepsilon/2$;
2. on $A$, $\|\hat V-x/d\|_{C^1(D)}\le\varepsilon$, so $A\subset B$;
3. $\|D^mV_J\|_\infty\le CJ2^{J(m-\alpha)_+}$ for $m=2,3$ (no factor $J$ unless $\alpha=m$).

*Proof.*
- **Item 3.** Lemma 1.1 with $g=V^E$, $s=\alpha$.
- **Item 1.** On $D$, $V_J-x/d=(k_J*V^E-V^E)+\nabla(u-u_1)$.
  - $D^iV^E$ is $\beta$-Hölder for $i=0,1$, so $|D^i(k_J*V^E-V^E)|\le C\int|k_J(y)||y|^\beta dy\le C2^{-J\beta}$.
  - By (C4), $\|\nabla(u-u_1)\|_{C^1}\le Cr$.
  - Take $r_0$ and $J_0$ so that $C(2^{-J_0\beta}+r_0)\le\varepsilon/2$.
- **Item 2.** On $A$, $\|\nabla\xi\|_{C^1}\le CJ2^{-J(\alpha-1/2)}\le\varepsilon/2$ for $J\ge J_0$. ∎

## II.3 Lemma 2 (geometry) and Lemma 3 (transport inverse)

**Setting.** $X$ is the restriction to $D=\bar B$ of a $C^k$ field ($k\ge1$) on a neighbourhood of $D$, with $\|X-x/d\|_{C^1(D)}:=\max(\sup|X-x/d|,\sup\|DX-I/d\|)\le\varepsilon\le1/(8d)$. Put $a:=1/d-\varepsilon\ge7/(8d)$, let $\Phi_t$ be the flow of $X$, let $\gamma(s)=\Phi_{-s}x$, and let $w(s,x):=\exp(-\int_0^s\mathrm{div}X(\Phi_{-\sigma}x)d\sigma)$.

**Lemma 2.**
1. $X$ has exactly one zero $x_X\in D$, and $|x_X|\le d\varepsilon$.
2. With $\rho(y)=|y-x_X|$: $(y-x_X)\cdot X(y)\ge(1/d-\varepsilon)\rho^2$ and $|X(y)|\le(1/d+\varepsilon)\rho$.
3. For $x\in D$, $\Phi_{-s}x$ exists for all $s\ge0$ and stays in $D$. It lies in $B$ for $s>0$, and $B$ is invariant.
4. $r(s):=\rho(\gamma(s))$ satisfies $r(0)e^{-(1/d+\varepsilon)s}\le r(s)\le r(0)e^{-(1/d-\varepsilon)s}$. If $r(0)>0$, then $-(1/d+\varepsilon)r\le r'\le-ar$.
5. The propagator $P(s,\sigma)$ of $y'=-DX(\gamma)y$ satisfies $\|P(s,\sigma)\|\le e^{-a(s-\sigma)}$. In particular $\|D\Phi_{-s}\|\le e^{-as}$.
6. $1-d\varepsilon\le\mathrm{div}X\le1+d\varepsilon$, so $e^{-(1+d\varepsilon)s}\le w\le e^{-(1-d\varepsilon)s}\le e^{-7s/8}$.

*Proof.*
1. $G(x)=x-dX(x)=-d(X-x/d)$ maps $D$ into $B(0,d\varepsilon)$ and is a $d\varepsilon$-contraction on the convex set $D$. Its unique fixed point is the unique zero of $X$.
2. $X(y)=A(y)(y-x_X)$ with $A=\int_0^1DX(x_X+t(y-x_X))dt$, and $\|A-I/d\|\le\varepsilon$; the segment lies in $D$ by convexity.
3. For $|z|=1$, $z\cdot X(z)\ge1/d-\varepsilon>0$, so $\frac{d}{ds}|\gamma|^2<0$ whenever $|\gamma|=1$. A first-exit-time argument gives invariance of $D$ and of $B$, and shows that boundary points enter $B$ immediately. Global existence holds because $D$ is compact.
4. $(r^2)'=-2(\gamma-x_X)\cdot X(\gamma)$. Apply item 2 and Gronwall.
5. $v\cdot DX\,v\ge a|v|^2$ on $D$, so $(|y|^2)'\le-2a|y|^2$. Also $D\Phi_{-s}=P(s,0)$.
6. $\mathrm{div}X=1+\mathrm{tr}(DX-I/d)$. ∎

**Definition.** For $H\in C(D)$, put $T_Xg:=\mathrm{div}(gX)$ and
$$T_X^{-1}H(x):=\int_0^\infty H(\Phi_{-s}x)\,w(s,x)\,ds.$$
The integral converges absolutely and uniformly, and $T_X^{-1}H\in C(D)$.

**Semigroup identity.** $w(s,\Phi_{-t}x)=w(s+t,x)/w(t,x)$, so
$$w(t,x)\,T_X^{-1}H(\Phi_{-t}x)=\int_t^\infty H(\Phi_{-s}x)w(s,x)ds.\tag{SG}$$

**Lemma 3.**
- **(a) Uniqueness.** If $g\in C^1(D)$ and $\mathrm{div}(gX)=H$ on $B$, then $g=T_X^{-1}H$.
  *Proof.* For $s>0$, $\psi(s)=g(\gamma(s))w(s,x)$ satisfies $\psi'=-(X\cdot\nabla g+g\,\mathrm{div}X)(\gamma)w=-H(\gamma)w$. Integrate over $[\delta,S]$, then let $\delta\to0$ (continuity) and $S\to\infty$ ($|\psi(S)|\le\|g\|_\infty e^{-7S/8}$). ∎
- **(a′) Right inverse.** If $H\in C(D)$ and $g:=T_X^{-1}H\in C^1(D)$, then $\mathrm{div}(gX)=H$ on $D$.
  *Proof.* Fix $x\in B$ and differentiate (SG) at $t=0^+$. The right side gives $-H(x)$. The left side gives $-\nabla g(x)\cdot X(x)-g(x)\mathrm{div}X(x)$, using $w(0)=1$ and $\partial_tw(0)=-\mathrm{div}X(x)$. Extend to $D$ by continuity. ∎
- **(b)** $\|T_X^{-1}H\|_\infty\le\frac87\|H\|_\infty\le2\|H\|_\infty$.
- **(c) Boundary layer.** If $H=0$ on $\{|x|\le1-\delta\}$, then $\|T_X^{-1}H\|_\infty\le6d\delta\|H\|_\infty$.
  *Proof.* The case $\delta>1/2$ follows from (b), so let $\delta\le1/2$ and $\phi=|\gamma|^2$. Where $|\gamma|\ge1/2$, $\gamma\cdot X(\gamma)\ge|\gamma|(|\gamma|/d-\varepsilon)\ge3/(16d)$, so $\phi'\le-3/(8d)$. Hence $\phi$ drops below $(1-\delta)^2$ within time $\le(1-(1-\delta)^2)\cdot8d/3\le6d\delta$. It never returns, by the same sign argument. Use $w\le1$. ∎

**Lemma 3.1 (flow derivatives; uniform in $s$).** Let $M=D\Phi_{-s}$, $N=D^2\Phi_{-s}$ and $\ell=\log w$.
1. If $X\in C^2$: $\|N(s)\|\le\|D^2X\|_\infty e^{-as}/a$ and $|D_x\ell|\le\|D\,\mathrm{div}X\|_\infty/a$.
2. If $X\in C^3$: $\|D^2_x\ell\|\le\|D^2\mathrm{div}X\|_\infty/(2a)+\|D\,\mathrm{div}X\|_\infty\|D^2X\|_\infty/a^2$.

*Proof.*
- $N$ solves $N'=-DX(\gamma)N-D^2X(\gamma)[M\cdot,M\cdot]$ with $N(0)=0$. By Duhamel and Lemma 2.5,
  $\|N(s)\|\le\int_0^se^{-a(s-\sigma)}\|D^2X\|e^{-2a\sigma}d\sigma\le\|D^2X\|e^{-as}/a$.
- $D_x\ell[v]=-\int_0^sD\mathrm{div}X(\gamma)[Mv]d\sigma$, and $\int_0^\infty e^{-a\sigma}d\sigma=1/a$.
- $D_x^2\ell[v,u]=-\int_0^s\big(D^2\mathrm{div}X(\gamma)[Mv,Mu]+D\mathrm{div}X(\gamma)[N[v,u]]\big)d\sigma$; bound with the two previous items. ∎

**Differentiation under the integral.** Let the integrand be $F(s,x)=H(\Phi_{-s}x)w(s,x)$ or $w(s,x)$. Its $x$-derivatives up to the relevant order are jointly continuous on $[0,\infty)\times D$ (by (ODE); the flow is defined on a neighbourhood). They are dominated by $Ke^{-7s/8}$ by Lemma 3.1 and $D_xw=wD_x\ell$, $D_x^2w=w(D_x^2\ell+D_x\ell\otimes D_x\ell)$. Truncate the integral at $S$, differentiate, and pass to the uniform limit.

- **(d)** If $X\in C^2$ and $H\in C^1(D)$, then $T_X^{-1}H\in C^1(D)$ and
  $\|\nabla T_X^{-1}H\|_\infty\le C_d(\|\nabla H\|_\infty+\|H\|_\infty\|D\,\mathrm{div}X\|_\infty)$.
- **(e)** If $X\in C^3$, then $T_X^{-1}\mathbf 1\in C^2(D)$, $\|\nabla T_X^{-1}\mathbf1\|\le C_d\|D\mathrm{div}X\|$, and
  $\|D^2T_X^{-1}\mathbf1\|_\infty\le C_d(\|D^2\mathrm{div}X\|+\|D\mathrm{div}X\|^2+\|D\mathrm{div}X\|\,\|D^2X\|)$.

All constants depend only on $d$, uniformly over $\|X-x/d\|_{C^1}\le\varepsilon\le1/(8d)$.

## II.4 The centring function $f_0$ and the exact decomposition

**Bounds on $f_0$.** Let $f_0:=T_{V_J}^{-1}\mathbf 1$; Lemma 1 applies, with $V_J\in C^\infty$. Using $\|D^m\mathrm{div}V_J\|\le d\|D^{m+1}V_J\|$, Lemma 1(3) and (e):
$$\|f_0\|_\infty\le2,\qquad\|\nabla f_0\|_\infty\le CJ2^{J(2-\alpha)_+},\qquad\|D^2f_0\|_\infty\le CJ^22^{J(3-\alpha)_+}.$$
The last bound uses $2(2-\alpha)_+\le(3-\alpha)_+$ for $\alpha\ge1$. Moreover $f_0\in C^2(D)$, and $\mathrm{div}(f_0V_J)=1$ by (a′).

**Noise term.** Let $G_\xi:=\mathrm{div}(f_0\nabla\xi)=f_0\Delta\xi+\nabla f_0\cdot\nabla\xi\in C^1(D)$ and $Z:=T_{V_J}^{-1}G_\xi$. Then $Z$ is defined for every $\omega$ (since $V_J$ is deterministic), $Z\in C^1(D)$ by (d), and $T_{V_J}Z=G_\xi$ by (a′).

**Identity (★).** On $A$ (so $\hat V$ satisfies Lemma 2 and $\hat f=T_{\hat V}^{-1}\mathbf1$),
$$\hat f-f=(f_0-f)-Z+T_{\hat V}^{-1}\mathrm{div}(Z\nabla\xi).\tag{★}$$

*Proof.*
1. $\hat V$ is $C^\infty$, so $\hat f\in C^2$ by (e), and $T_{\hat V}\hat f=1$ by (a′).
2. Hence $T_{\hat V}(\hat f-f_0)=1-\mathrm{div}(f_0V_J)-\mathrm{div}(f_0\nabla\xi)=-G_\xi$.
3. Also $T_{\hat V}Z=T_{V_J}Z+\mathrm{div}(Z\nabla\xi)=G_\xi+\mathrm{div}(Z\nabla\xi)$.
4. So $T_{\hat V}(\hat f-f_0+Z)=\mathrm{div}(Z\nabla\xi)$, which is continuous. The function $\hat f-f_0+Z$ is $C^1$, so (a) with $X=\hat V$ gives the claim. ∎

## II.5 Bias: $\|f_0-f\|_\infty\le CJ^22^{-J\alpha}$

**Reduction.** $f\in C^1$ ($\alpha>1$), $\mathrm{div}(fV)=1$, and $V_J-V=\nabla b$ on $D$. So $T_{V_J}(f_0-f)=1-\mathrm{div}(fV_J)=-\mathrm{div}(f\nabla b)$, and by (a), $f_0-f=-T_{V_J}^{-1}\mathrm{div}(f\nabla b)$.

**Commutator.** Let $g:=F-k_J*F$ and $R(x):=-\int k_J(-h)\Delta_hF(x)\Delta_hV^E(x)dh$. A direct computation, writing $F(x)-F(x-y)=-\Delta_{-y}F(x)$ and $V^E(x-y)=V^E(x)+\Delta_{-y}V^E(x)$, gives
$$F\,(k_J*V^E)=k_J*(FV^E)+gV^E+R.$$
Let $G:=\mathrm{div}(FV^E)-1\in C^{\alpha-1}(\mathbb R^d)$ (algebra property); then $G=0$ on $D$. Since $\int k_J=1$, on $D$:
$$\mathrm{div}(f\nabla b)=\mathrm{div}(fV_J)-1=k_J*G+\mathrm{div}(gV)+\mathrm{div}R .$$

**(i) The term $\mathrm{div}(gV)$.**
- $V=V_J-\nabla b$, so $\mathrm{div}(gV)=T_{V_J}g-\mathrm{div}(g\nabla b)$, and $T_{V_J}^{-1}\mathrm{div}(gV)=g-T_{V_J}^{-1}\mathrm{div}(g\nabla b)$ by (a), since $g\in C^1$.
- By (C2): $\|g\|\le C2^{-J\alpha}$, $\|\nabla g\|\le C2^{-J(\alpha-1)}$, $\|\nabla b\|\le C2^{-J\alpha}$, $\|D^2b\|\le C2^{-J(\alpha-1)}$.
- By (b), the contribution is $\le C2^{-J\alpha}+C2^{-J(2\alpha-1)}$.

**(ii) The term $\mathrm{div}R$.**
- $\partial R=-\int k_J(-h)[\Delta_h\partial F\,\Delta_hV^E+\Delta_hF\,\Delta_h\partial V^E]dh$.
- Each product is $\Delta_hA\,\Delta_hB$ with $(a,b)=(\alpha-1,\alpha)$ or $(\alpha,\alpha-1)$.
- By (C3), the product equals a polynomial in $h$ with monomials of degree in $[2,a+b)=[2,2\alpha-1)$, plus a remainder $\le C|h|^{\min(1+a,1+b,a+b)}L^2=C|h|^\alpha L^2$, where $L=1+\log(1/|h|)$. When $a<1$, $P_A$ is empty.
- The polynomial terms integrate to 0 because $S\ge2\alpha+2$.
- So $\|\mathrm{div}R\|_\infty\le CJ^22^{-J\alpha}$, with no $J^2$ for non-integer $\alpha$. By (b), the contribution is $\le CJ^22^{-J\alpha}$.

**(iii) The term $k_J*G$.**
- On $D$, $k_J*G=k_J*G-G$, so by (C2) with $s=\alpha-1$, $m=0$, it is $O(2^{-J(\alpha-1)})$.
- It vanishes at points of $D$ at distance $>C2^{-J}$ from $\partial D$, by the support of $k_J$.
- By (c), the contribution is $\le C2^{-J}2^{-J(\alpha-1)}=C2^{-J\alpha}$.

**Total.** $\|f_0-f\|_\infty\le CJ^22^{-J\alpha}$, uniformly over $\mathcal F(\alpha,r)$.

## II.6 Variance: $E\|Z\|_2^2\le Cn^{-1}2^{J(d+3)}\le C2^{-2J\alpha}$

**Representation.** Let $\mathcal D_y:=f_0(y)\Delta_y+\nabla f_0(y)\cdot\nabla_y$. Then $G_\xi(y)=n^{-1/2}\mathbb W(\mathcal D_yk_J(y,\cdot))$. By (G),
$$Z(x)=n^{-1/2}\mathbb W(h_x),\qquad h_x=\int_0^\infty w(s)\,\mathcal D_yk_J(y,\cdot)|_{y=\gamma_x(s)}ds,$$
where $\gamma_x$ is the backward ray of $V_J$. Hence $EZ(x)^2=n^{-1}\|h_x\|_2^2$.

**Kernel bound.** $\|\nabla f_0\|\le CJ2^{J(2-\alpha)_+}\le C2^J$, because $(2-\alpha)_+<1$. With (K1) and (K2), $|\mathcal D_yk_J(y,z)|\le C2^{J(d+2)}1\{|y-z|\le\delta\}$, where $\delta:=C_02^{-J}$. With $\mu_x:=\int_0^\infty w(s)\delta_{\gamma_x(s)}ds$,
$$|h_x(z)|\le C2^{J(d+2)}\mu_x(B(z,\delta)),\qquad\|h_x\|_2^2\le C2^{2J(d+2)}\!\int\mu_x(B(z,\delta))^2dz\le C2^{2J(d+2)}\delta^d\!\int\mu_x(B(y,2\delta))\mu_x(dy).$$
The last step is Fubini: $\int\mu(B(z,\delta))^2dz=\iint|B(y,\delta)\cap B(y',\delta)|\,\mu(dy)\mu(dy')$.

**Ray measure.** Let $x_J$ be the zero of $V_J$, $\rho=|\cdot-x_J|$, and $\rho_x=\rho(x)>0$.
- By Lemma 2.4 and 2.6, $w(s)\le(r(s)/\rho_x)^\beta$ with $\beta=d(1-d\varepsilon)/(1+d\varepsilon)\ge7d/9>1$.
- $r(s)$ decreases strictly from $\rho_x$ to 0, with $|r'|\ge ar$. Changing variables, for $\varphi\ge0$,
  $$\int\varphi\,d\mu_x\le\frac1a\int_0^{\rho_x}\varphi(\gamma\text{ at radius }r')\,(r'/\rho_x)^\beta\frac{dr'}{r'}.\tag{M}$$
- **Small-ball mass.** If $|\gamma(s)-y|\le2\delta$, then $|r(s)-\rho(y)|\le2\delta$. Hence $m(y):=\mu_x(B(y,2\delta))$ satisfies
  - $m(y)\le C\delta\rho(y)^{\beta-1}\rho_x^{-\beta}$ if $\rho(y)\ge4\delta$;
  - $m(y)\le C\min(1,\delta/\rho_x)^\beta$ if $\rho(y)<4\delta$.
- **Integration.** Apply (M) once more.
  - The part with $r'\ge4\delta$ is $\le C\delta\rho_x^{-2\beta}\int_0^{\rho_x}r'^{2\beta-2}dr'\le C\delta/\rho_x$, since $2\beta-1>0$.
  - The part with $r'<4\delta$ is $\le C\min(1,\delta/\rho_x)^{2\beta}\le C\min(1,\delta/\rho_x)$.
  - Trivially $\int m\,d\mu_x\le\mu_x(D)^2\le4$.

Hence $\|h_x\|_2^2\le C2^{J(d+4)}\min(1,2^{-J}/\rho_x)\le C2^{J(d+3)}|x-x_J|^{-1}$. Since $\int_D|x-x_J|^{-1}dx\le C$ for $d\ge2$, Tonelli gives
$$E\|Z\|_2^2\le Cn^{-1}2^{J(d+3)}\le C2^{-2J\alpha}.$$

**Heuristic reading.** $\Delta\xi$ has pointwise variance $n^{-1}2^{J(d+4)}$ and correlation length $2^{-J}$. Integrating along a ray of length $O(1)$ gains one factor $2^{-J}$. This is the "one order along the flow" effect that produces $d+3$.

## II.7 Remainder and the bad event

**Remainder.** On $A$, using the f_0 bounds and $(2-\alpha)_+<1$, $(3-\alpha)_+\le2$:
- $\|G_\xi\|_\infty\le\|f_0\|\|\Delta\xi\|+\|\nabla f_0\|\|\nabla\xi\|\le CJ2^{-J(\alpha-1/2)}+CJ^22^{J(2-\alpha)_+-J(\alpha+1/2)}\le CJ^22^{-J(\alpha-1/2)}$.
- $\|\nabla G_\xi\|_\infty\le C(\|D^3\xi\|+\|\nabla f_0\|\|D^2\xi\|+\|D^2f_0\|\|\nabla\xi\|)\le CJ^32^{-J(\alpha-3/2)}$. Each cross term has exponent $\le-(\alpha-3/2)$ because $\alpha\ge1$.
- By (b) and (d) (with $\|D\,\mathrm{div}V_J\|\le d\|D^2V_J\|\le CJ2^{J(2-\alpha)_+}$ from Lemma 1(3)): $\|Z\|_\infty\le CJ^22^{-J(\alpha-1/2)}$ and $\|\nabla Z\|_\infty\le C(\|\nabla G_\xi\|+\|G_\xi\|J2^{J(2-\alpha)_+})\le CJ^32^{-J(\alpha-3/2)}$, using $(2-\alpha)_+<1$.
- Hence $\|\mathrm{div}(Z\nabla\xi)\|_\infty\le\|\nabla Z\|\|\nabla\xi\|+\|Z\|\|\Delta\xi\|\le CJ^42^{-J(2\alpha-1)}+CJ^32^{-J(2\alpha-1)}\le CJ^42^{-J(2\alpha-1)}$.
- By (b) for $\hat V$, $\|T_{\hat V}^{-1}\mathrm{div}(Z\nabla\xi)\|_\infty\le CJ^42^{-J(2\alpha-1)}$. This is $o(2^{-J\alpha})$ **because $\alpha>1$**.

**Bad event.**
- Each component $\partial^a\xi(x)=n^{-1/2}\mathbb W(\partial_x^ak_J(x,\cdot))$ has standard deviation $\le C\bar\sigma_m$, where $\bar\sigma_m:=n^{-1/2}2^{J(d/2+m)}$ (by (K3)).
- The canonical metric is $\le C\bar\sigma_m2^J|x-x'|$, so Dudley gives $E\sup_D|\partial^a\xi|\le C\bar\sigma_m\sqrt J\le J\bar\sigma_m/2$ for large $J$.
- Borell–TIS at deviation $J\bar\sigma_m/2$, plus a union bound over finitely many $a$, gives $P(A^c)\le Ce^{-cJ^2}$, uniformly in $f$.

## II.8 Assembly

**On $A$.** By (★), clipping, II.5–II.7 and $A\subset B$:
$$\|\tilde f-f\|_2^2\le3|D|(CJ^22^{-J\alpha})^2+3\|Z\|_2^2+3|D|(CJ^42^{-J(2\alpha-1)})^2.$$
**Off $A$.** $\|\tilde f-f\|_2^2\le4r^2|D|$.

Taking expectations,
$$E\|\tilde f-f\|_2^2\le CJ^42^{-2J\alpha}+C2^{-2J\alpha}+CJ^82^{-2J(2\alpha-1)}+Ce^{-cJ^2}\le CJ^42^{-2J\alpha}\le C(\log n)^4n^{-2\alpha/(2\alpha+d+3)}.$$
The finitely many $n$ with $J<J_0$ are covered by the trivial bound $4r^2|D|$. For non-integer $\alpha$, no logarithm appears anywhere (Lemma 1.1, (C3)), and the bound is $Cn^{-2\alpha/(2\alpha+d+3)}$. ∎

Combining Parts I and II proves the Theorem.

---

# Status

- **Main claim: PROVED.** The main claim is the Theorem: for small fixed $r$, the minimax rate is $n^{-2\alpha/(2\alpha+d+3)}$ up to logarithmic factors. The lower bound $c\,n^{-2\alpha/(2\alpha+d+3)}$ holds for every $r\in(0,1)$. The upper bound $C(\log n)^4n^{-2\alpha/(2\alpha+d+3)}$ holds for $r\le r_0(d,\alpha)$, with no logarithm when $\alpha$ is not an integer.
- **Review and repairs.** During the attempt the full argument was audited twice independently, and a final verification pass went through it line by line. The repairs from those checks are built into the text:
  - the exponent $(m-\alpha)_+$ in Lemma 1;
  - the observable event $B$;
  - the right inverse (a′);
  - the Neumann-series proof of (C4);
  - the general-$d$ proof of the radial identity;
  - the $J$-power bookkeeping in II.7.

  None of these changes a rate.
- **Dependence on cited facts.** The proof is complete relative to the standard results listed at the top: (E1), (E2), (GN), (As), (C1)–(C3), (S), (LP), (ODE), (G). They are quoted and not re-proved here. In particular this covers:
  - the Zygmund–Schauder estimate at integer $\alpha$;
  - boundedness of the reflection-type extension on Zygmund spaces;
  - the Zygmund Taylor formula with a logarithm at integer order;
  - uniformity of the Gilbarg–Trudinger constants over the class.

  This is the only respect in which the document is not self-contained.
- **Open, and not part of the claim:**
  - whether the $(\log n)^4$ factor for integer $\alpha$ can be removed;
  - the upper bound for $r$ that is not small. There, the Neumann series for (C4) and the single-source geometry of Lemma 2 can fail, and $\nabla u_f$ may have several critical points. The lower bound is unaffected.

# Other routes

- **Least squares plus isotropic stability.** This combines a stability estimate $\|f_1-f_2\|\lesssim\|u_{f_1}-u_{f_2}\|_{H^2}$ with interpolation. It only gives $n^{-2(\alpha-1)/(2\alpha+d+2)}$, which is suboptimal: it ignores the anisotropy.
- **Exact linearisation at $f=1$.** For $h=a(\rho)Y_l$, $\mathrm{div}(hx/d)=\frac1d\rho^{1-d}(\rho^da)'Y_l$. This yields the symbol $(1+|\xi_{\rm rad}|)/|\xi|^2$, and the heuristic rate was read off from it. It suggested both halves of the proof but is not used in it.
- **Sample-split one-step estimator.** Set aside, not refuted.
- **Alternative lemmas.** An alternative pointwise variance lemma and a bias-gradient lemma ($\|\nabla(f_0-f)\|_\infty\le CJ^32^{-J(\alpha-1)}$) were also proved. Linearising around the smooth $f_0$ rather than around $f$ makes them unnecessary.
- **Other lower-bound constructions.** A single bump at the source gives $n^{-(2\alpha+d)/(2\alpha+d+4)}$. Isotropic wavelets give $n^{-2\alpha/(2\alpha+d+2)}$. Adding radial oscillation does not help. All of these are weaker than the angular construction.
