The document below is a draft proof. Check the argument step by step: for every inequality, interchange, cited result, and 'it follows that', ask whether it actually follows as written. List every error or gap in order of severity, and say explicitly whether the main claim is proved.

## The draft proof

# An explicit Dehn twist with an infinite orbit on the components of $\mathcal D_f$

## Theorem

Let $f$ be a quadratic rational map with critical points $c_1,c_2$, where $c_1$ has exact period 4 and $v=f(c_2)$ is not on the cycle of $c_1$. Put $a_i=f^{i}(c_1)$ (indices mod 4), $A=\{a_0,a_1,a_2,a_3\}$ and $B=A\cup\{v\}$. The critical values of $f$ are $a_1=f(c_1)$ and $v$.

**(a) Model case.** Take $f=f_{1/4}(z)=1-\dfrac{11}{12z}+\dfrac{1}{6z^2}$. Its 4-cycle is $c_1=0\to\infty\to1\to\tfrac14\to0$, its second critical point is $c_2=4/11$, and $v=-25/96$. On $\hat{\mathbb R}$ the order is
$$v<c_1=0<f^{3}(c_1)=\tfrac14<f^{2}(c_1)=1<f(c_1)=\infty .$$
Let $\alpha$ be a simple arc from $v$ to $f(c_1)=\infty$ with the following crossing pattern with $\hat{\mathbb R}$:
1. leave $v$ into the lower half-plane and cross $\mathbb R$ upward at a point $x_1\in(1,\infty)$;
2. run in the upper half-plane and cross $\mathbb R$ downward at a point $x_2\in(0,\tfrac14)$;
3. run in the lower half-plane and cross $\mathbb R$ upward at a point $x_3\in(v,0)$;
4. stay in the upper half-plane until $\infty$.

A concrete choice is: the lower semicircle from $v$ to $2$; then the upper semicircle over $[\tfrac18,2]$; then the lower semicircle over $[-\tfrac18,\tfrac18]$; then the vertical ray from $-\tfrac18$ up to $\infty$.

Let $\gamma=\partial N(\alpha)$ be the boundary of a thin closed regular neighbourhood of $\alpha$. Then $\gamma$ is a simple closed curve in $S^2\setminus B$. It bounds a disc containing exactly $v$ and $f(c_1)$, and the complementary disc contains $c_1,f^2(c_1),f^3(c_1)$.

The Dehn twist $T_\gamma$ (power $k=1$) satisfies $f^*\circ T_\gamma=f^*$ and $i_*\circ T_\gamma=i_*$, so $T_\gamma(\mathcal D_f)=\mathcal D_f$. For every component $D_0$ of $\mathcal D_f$ and every $m\neq0$ we have $T_\gamma^m(D_0)\ne D_0$. So every orbit of $\langle T_\gamma\rangle$ on $\pi_0(\mathcal D_f)$ is infinite, and in particular $\mathcal D_f$ has infinitely many components.

**Equivalent mapping-class description (§10).** $\gamma=T_c^{-1}(\gamma_0)$. Here $c$ is the round circle $|z-\tfrac12|=\tfrac35$, which surrounds $c_1,f^3(c_1),f^2(c_1)$ but not $v$. And $\gamma_0=\partial N(\alpha_0)$, where $\alpha_0$ leaves $v$ into the upper half-plane, crosses $\mathbb R$ downward in $(0,\tfrac14)$, and then runs in the lower half-plane to $\infty$.

**(b) Every $f$.** Let $f$ be arbitrary. By Proposition 1 there are a unique $t\in W$ and a unique Möbius map $M$ with $M\circ f\circ M^{-1}=f_t$ and $M(c_1)=0$. Choose a path $t_s$ in $W$ from $\tfrac14$ to $t$ and let $h_1$ be the endpoint of an isotopy that follows the marked points (§9). Then
$$\gamma_f:=M^{-1}(h_1(\gamma))$$
has the same property for $f$: $T_{\gamma_f}$ preserves $\mathcal D_f$ and has infinite orbits on $\pi_0(\mathcal D_f)$.

When $t\in(0,\tfrac{3-\sqrt5}{2})$ this is explicit. The five points of $B$ lie on the circle $C=M^{-1}(\hat{\mathbb R})$ in the cyclic order $v,\,c_1,\,f^3(c_1),\,f^2(c_1),\,f(c_1)$. Call the "upper" side of $C$ the image under $M^{-1}$ of the upper half-plane. Then $\gamma_f=\partial N(\alpha_f)$, where $\alpha_f$ runs from $v$ to $f(c_1)$ as follows:
- it leaves $v$ into the lower side and crosses $C$ between $f^2(c_1)$ and $f(c_1)$;
- it crosses back between $c_1$ and $f^3(c_1)$;
- it crosses again between $v$ and $c_1$;
- it then runs on the upper side to $f(c_1)$.

The proof is complete except for the standard facts listed as (F1)–(F6) in §2, which are quoted from the literature and not reproved here.

---

## 1. Normal form

**Proposition 1.** Put $f_t(z)=1+\dfrac bz+\dfrac c{z^2}$, with $b=\dfrac{t^2+t-1}{1-t}$ and $c=\dfrac{t(1-2t)}{1-t}$. Let $E$ be the set of 9 points
$$E=\{0,1,\tfrac12\}\cup\{t^2-3t+1=0\}\cup\{t^2+t-1=0\}\cup\{3t^2-3t+1=0\},$$
and put $W=\mathbb C\setminus E$. For $f$ as in the Theorem there is exactly one pair $(t,M)$ with $t\in W$, $M$ Möbius, $M f M^{-1}=f_t$ and $M(c_1)=0$. Conversely, for every $t\in W$ the map $f_t$ is as in the Theorem, with cycle $0\to\infty\to1\to t\to0$. Finally, $W$ is connected.

*Proof.*

*Existence.* Let $M$ be the Möbius map with $M(a_0,a_1,a_2)=(0,\infty,1)$, put $t=M(a_3)$ and $g=MfM^{-1}$.
- $0$ is a critical point of $g$ with $g(0)=\infty$, so $0$ is a double pole and the only pole. Hence $g=P(z)/z^2$ with $\deg P\le2$ and $P(0)\ne0$.
- $g(\infty)=1$ forces $g=1+b/z+c/z^2$ with $c\neq0$.
- The conditions $g(1)=t$ and $g(t)=0$ read $1+b+c=t$ and $t^2+bt+c=0$. Substituting $c=t-1-b$ into the second gives $b(t-1)=1-t-t^2$. Hence $b$ and $c$ are as stated. As checks, $b+c=t-1$, and $(1-t)(t^2+bt+c)=0$ identically.

*Uniqueness.* Any other such $M'$ maps the orbit $(a_0,a_1,a_2)$ to $(0,\infty,1)$, so $M'=M$.

*Which $t$ occur.*
- $t=\tfrac12$ gives $c=0$, so the degree drops. For $t\notin\{0,1,\tfrac12\}$ the map $f_t$ has degree 2 and $0$ is critical of exact period 4.
- Since $f_t'=-(bz+2c)/z^3$, we have $c_2=-2c/b$, or $c_2=\infty=a_1$ if $b=0$, i.e. if $t^2+t-1=0$.
- Otherwise
$$v(t)=1-\frac{b^2}{4c}=-\frac{(t^2-3t+1)^2}{4t(1-t)(1-2t)},$$
using $(t^2+t-1)^2-(t^2-3t+1)^2=4t(1-t)(1-2t)$.
- $v=0\iff t^2-3t+1=0$. $v=1\iff b=0$. $v=t\iff(3t^2-3t+1)^2=0$, after expanding $4t(1-t)^2(1-2t)=(t^2+t-1)^2$.

So $W$ is exactly the admissible set. It is $\mathbb C$ minus finitely many points, hence connected. ∎

At $t=\tfrac14$: $b=-\tfrac{11}{12}$, $c=\tfrac16$, $c_2=\tfrac4{11}$ and $v=-\tfrac{25}{96}$. These were checked in exact rational arithmetic.

**Factorisation (used in §9).** Put $N_t(z)=z/(z-c_2(t))$ and $M_t(y)=v(t)+(1-v(t))/y$. Then
$$f_t(z)=v+(1-v)(1-c_2/z)^2=M_t\big(N_t(z)^2\big).$$
To check it, compare coefficients: $-2(1-v)c_2=b$ and $(1-v)c_2^2=c$. Both $M_t$ and $N_t$ depend continuously on $t\in W$. Also $N_t(0)=0$, $N_t(c_2)=\infty$, $M_t(0)=\infty$ and $M_t(\infty)=v$.

---

## 2. Teichmüller preliminaries

**Conventions.** A marking of $(S^2,X)$, with $|X|\ge3$, is an orientation-preserving homeomorphism $\varphi:S^2\to\hat{\mathbb C}$. $\mathrm{Teich}(X)$ is the set of markings modulo the relation $\varphi_1\sim\varphi_2$, which holds iff $M\varphi_1=\varphi_2$ on $X$ and $M\varphi_1\simeq\varphi_2$ rel $X$ for some Möbius $M$. $\mathrm{PMod}(S^2,X)$ acts by $g\cdot[\varphi]=[\varphi g^{-1}]$. The pullback $f^*[\varphi]=[\psi]$ is defined by requiring $\varphi\circ f\circ\psi^{-1}$ to be rational.

**Standard facts quoted, not reproved.**
- **(F1)** The modular function $\lambda:\mathbb H\to\mathbb C\setminus\{0,1\}$ is a holomorphic universal covering whose fibres are the $\Gamma(2)$-orbits. Moreover:
  - $\lambda(\tau+2)=\lambda(\tau)$ and $\lambda(-1/\tau)=1-\lambda(\tau)$;
  - $\lambda(\tau)=16e^{i\pi\tau}+O(e^{2\pi i\tau})$ as $\operatorname{Im}\tau\to\infty$;
  - $y\mapsto\lambda(iy)$ is a decreasing bijection $(0,\infty)\to(0,1)$.
- **(F2)** (Teichmüller) $\mathrm{Teich}(X)$ is homeomorphic to $\mathbb R^{2(|X|-3)}$. In particular it is contractible. $\mathrm{PMod}(S^2,X)$ acts properly discontinuously, and the quotient is the moduli space.
- **(F3)** (Bers fibration and Birman exact sequence) The forgetful map $i_*:\mathrm{Teich}(B)\to\mathrm{Teich}(A)$ is surjective. Normalise $a_0,a_1,a_2$ to $0,\infty,1$, and let the fibre over $p$ sit over the configuration $A_p$. Recording the position $v'$ of the fifth point identifies this fibre with the universal cover of $\hat{\mathbb C}\setminus A_p$. The point-push subgroup $\ker\big(\mathrm{PMod}(S^2,B)\to\mathrm{PMod}(S^2,A)\big)\cong\pi_1(S^2\setminus A,v)$ acts on each fibre as the deck group.
- **(F4)** (Push formula) The push of $v$ along a simple loop $\delta$ is $T_{\delta_L}T_{\delta_R}^{-1}$, where $\delta_L,\delta_R$ are the two boundary curves of a regular neighbourhood of $\delta$.
- **(F5)** $f^*$ is well defined and continuous; indeed it is holomorphic (Douady–Hubbard).
- **(F6)** Isotopy extension: a motion of finitely many labelled distinct points extends to an ambient isotopy. In this proof (F6) is in fact constructed explicitly (Lemma 9.1).

**Lemma 2.1 (free action).** $\mathrm{PMod}(S^2,X)$ acts freely on $\mathrm{Teich}(X)$.

*Proof.* Suppose $[\varphi g^{-1}]=[\varphi]$. Then $M\varphi=\varphi g^{-1}$ on $X$ for some Möbius $M$. Since $g$ fixes $X$ pointwise, $M$ fixes the $\ge3$ points of $\varphi(X)$, so $M=\mathrm{id}$. Then $\varphi g^{-1}\simeq\varphi$ rel $X$, so $g=1$. ∎

By (F1), (F2) and Lemma 2.1, the modulus map $\mathrm{mod}:\mathrm{Teich}(A)\to\mathbb C\setminus\{0,1\}$ is a universal covering. It sends $[\varphi]$ to the $t$ for which some Möbius map takes $\varphi(a_0,a_1,a_2,a_3)$ to $(0,\infty,1,t)$. Hence there is a biholomorphism $\Theta:\mathrm{Teich}(A)\cong\mathbb H$ with $\lambda\circ\Theta=\mathrm{mod}$, and we use it to identify $\mathrm{Teich}(A)$ with $\mathbb H$. For $f=f_{1/4}$ the base point $\tau_0=[\mathrm{id}]\in\mathrm{Teich}(B)$ lies in $\mathcal D_f$, because $f^*[\mathrm{id}]=[\mathrm{id}]$, $f$ being rational. We normalise $\Theta$ so that $i_*\tau_0=p_0:=iy_0$, where $\lambda(iy_0)=\tfrac14$. Numerically $y_0\approx1.2793$.

Put $\Psi=(i_*,f^*):\mathrm{Teich}(B)\to\mathbb H\times\mathbb H$. Then $\mathcal D_f=\Psi^{-1}(\Delta)$, where $\Delta$ is the diagonal.

**Lemma 2.2 (equivariance for a lift fixing $A$).** Let $\varphi$ be a homeomorphism fixing $B$ pointwise, and $\tilde\varphi$ a homeomorphism fixing $A$ pointwise with $f\tilde\varphi=\varphi f$. Then $f^*(\varphi\cdot\tau)=\tilde\varphi\cdot f^*(\tau)$.

*Proof.* Let $\tau=[\psi_0]$ and suppose $\psi_0 f=F\psi$ with $F$ rational. Then $\psi_0\varphi^{-1}f=\psi_0 f\tilde\varphi^{-1}=F(\psi\tilde\varphi^{-1})$. ∎

*Caution.* A lift of an element of $\mathrm{PMod}(S^2,B)$ need not fix $A$ pointwise: it may exchange $a_i$ with the other preimage of $a_{i+1}$. So Lemma 2.2 has to be applied to an explicitly constructed lift, as in Lemma 2.3.

**Lemma 2.3 (lift of $T_\gamma$).** Let $\alpha$ be a simple arc from $v$ to $a_1$ with interior in $S^2\setminus B$. Let $\gamma=\partial N(\alpha)$, and realise $T_\gamma$ in a collar $R\subset S^2\setminus N(\alpha)$ disjoint from $B$. Then:
- $f^{-1}(R)=R_1\sqcup R_2$, with each $R_j$ mapped homeomorphically onto $R$;
- the map $\tilde T$ defined as $(f|_{R_j})^{-1}T_\gamma f$ on $R_j$ and the identity elsewhere is a homeomorphism with $f\tilde T=T_\gamma f$;
- $\tilde T$ fixes $f^{-1}(B)\supset A$ pointwise.

Hence $f^*\circ T_\gamma=[\tilde T]\cdot f^*$ with $[\tilde T]\in\mathrm{PMod}(S^2,A)$.

*Proof.*
- $R$ contains no critical value, so $f^{-1}(R)\to R$ is a 2-sheeted covering.
- Its monodromy around the core of $R$ is the product of the monodromies around the two critical values $v,a_1$ inside $\gamma$. Each of these is the sheet transposition, so the product is trivial. Hence the covering splits into two annuli, each mapped homeomorphically.
- $T_\gamma=\mathrm{id}$ on $\partial R$, so $\tilde T$ is continuous and bijective, hence a homeomorphism of $S^2$.
- $f^{-1}(B)$ is disjoint from $f^{-1}(R)$, so $\tilde T$ fixes it.
- Lemma 2.2 gives the last statement. ∎

---

## 3. The fibre formula and the obstruction (★)

**Lemma 3.1.** Let $\tau'\in\mathrm{Teich}(B)$ be represented, after normalising, by $(\hat{\mathbb C};a_0,a_1,a_2,a_3,v)=(0,\infty,1,t,v')$. Then $w:=\lambda(f^*\tau')$ satisfies
$$V_t(w)=v',\qquad V_t(w)=-\frac{\big((w-1)^2-t\big)^2}{4w(w-1)(w+t-1)} .$$

*Proof.*
- The pulled-back structure carries a degree-2 rational map $F$ whose critical values are the images of the critical values $a_1=\infty$ and $v'$. Up to a Möbius change in the source, $F(z)=v'+z^2$.
- Since $a_0=c_1$ is the critical point over $a_1$, its marked image is $a_0'=\infty$. The other points satisfy $F(a_i')=a_{i+1}$, so $a_1'=s_2$, $a_2'=s_3$, $a_3'=s_0$ with $s_2^2=1-v'$, $s_3^2=t-v'$, $s_0^2=-v'$. The marking determines the signs.
- The map $z\mapsto(s_3-s_2)/(z-s_2)$ sends $(\infty,s_2,s_3,s_0)$ to $(0,\infty,1,w)$, so $w=(s_3-s_2)/(s_0-s_2)$.
- Put $u=s_2-s_0$ and $U=u^2$. From $s_2^2-s_0^2=1$ we get $s_2=(u+u^{-1})/2$ and $s_0=(u^{-1}-u)/2$. Also $s_3=s_2-wu$.
- The relation $s_3^2-s_0^2=t$ becomes $1-w(U+1)+w^2U=t$, so $U=\dfrac{w+t-1}{w(w-1)}$.
- Then $v'=-s_0^2=-(1-U)^2/(4U)$, which is the stated formula.

Spot checks with random complex $t,v'$ confirm the identity to about $10^{-14}$. Also $V_t(t)=v(t)$. ∎

**Corollary 3.2 (★).** $V_t^{-1}(\infty)=\{0,1,\infty,1-t\}$, and at $w=1-t$ the numerator equals $(t^2-t)^2\neq0$. Since $v'\ne a_1=\infty$, we get $w\ne1-t$. Thus
$$\lambda(f^*\tau')\ne1-\lambda(i_*\tau')\quad\text{for all }\tau'\in\mathrm{Teich}(B). \tag{★}$$
By (F1), $\lambda(q)=1-\lambda(p)=\lambda(-1/p)$ holds iff $q=g(p)$ for some $g\in\Gamma(2)S$, where $S(\tau)=-1/\tau$. So $\Psi(\mathrm{Teich}(B))$ avoids every graph $\Gamma_g=\{(p,g(p))\}$ with $g\in\Gamma(2)S$.

**Lemma 3.3 (branching of $V_t$).** For $t\in W$, $V_t$ has degree 4 and is unbranched over $\hat{\mathbb C}\setminus\{0,1,t\}$.

*Proof.*
- Fix $v'\notin\{0,1,t,\infty\}$. The solutions $w$ of $V_t(w)=v'$ come from the sign choices of $(s_2,s_3,s_0)$ modulo a global sign, so there are at most 4.
- They are distinct. If two sign classes gave the same $w$, an affine map $L$ would satisfy $L(s_j)=\pm s_j$ with a sign pattern that is not constant. Then $L(z)^2-z^2$, of degree at most 2, would vanish at the three distinct points $s_2,s_3,s_0$, forcing $L=\pm\mathrm{id}$, a contradiction.
- Over $\infty$ there are 4 simple preimages $0,1,1-t,\infty$. ∎

**Fibre lemma.** Fix $p\in\mathrm{Teich}(A)$ with $\lambda(p)=t$, and let $\tilde U=i_*^{-1}(p)$. By (F3), $\tilde U$ is the universal cover of $\hat{\mathbb C}\setminus A_p$ via $\tau'\mapsto v'(\tau')$.
- By (F5) and Lemma 3.1, $w=\lambda\circ f^*$ is continuous on $\tilde U$ and satisfies $V_t\circ w=v'$. So $w$ is the lift of $v'$ through the covering $V_t:\hat{\mathbb C}\setminus V_t^{-1}(A_p)\to\hat{\mathbb C}\setminus A_p$ (Lemma 3.3).
- $f^*|_{\tilde U}$ is in turn the lift of $w$ through $\lambda$.
- Both lifts are determined by their value at one point.

---

## 4. $\mathcal D_f$ is a smooth curve

**Lemma 4.1.** $\mathcal D_f$ is a one-dimensional complex submanifold of $\mathrm{Teich}(B)$. Hence its connected components are path components.

*Proof.*
- The map $\mathrm{Teich}(B)\to\mathcal M_{0,5}$, $\tau'\mapsto(t',v')$, is a covering by (F2) and Lemma 2.1. So $(t',v')$ are local coordinates.
- Let $\tau_1\in\mathcal D_f$ have coordinates $(t_1,v_1)$. Then $w(\tau_1)=t_1$, so $v_1=V_{t_1}(t_1)=v(t_1)$.
- Since $v_1\notin\{0,1,t_1,\infty\}$, Lemma 3.3 makes $V_{t_1}$ a local biholomorphism at $w=t_1$. By continuity, $w(t',v')$ near $\tau_1$ is the holomorphic branch of $V_{t'}^{-1}(v')$ through $t_1$.
- $\lambda$ is injective near $i_*\tau_1=f^*\tau_1$. So near $\tau_1$ the condition $f^*\tau'=i_*\tau'$ is equivalent to $w(t',v')=t'$, i.e. to $v'=v(t')$, which is a holomorphic graph. ∎

---

## 5. The linking criterion

**Proposition 5.1.** Let $T\in\mathrm{PMod}(S^2,B)$ satisfy $\Psi\circ T=\Psi$, so that $T^{\pm1}(\mathcal D_f)=\mathcal D_f$. Let $g\in\Gamma(2)S$ have no fixed point in $\mathbb H$. Let $\tau\in\mathcal D_f$ with $p_0=i_*\tau$, and let $D_0$ be its component. Suppose that for each $m\neq0$ there is a path $\sigma'_m$ in the fibre $i_*^{-1}(p_0)$ from $\tau$ to $T^m\tau$ such that the loop $f^*\circ\sigma'_m$ has winding number $\neq0$ about $g(p_0)$. Then $T^m D_0\ne D_0$ for every $m\ne0$.

*Proof.*
- Let $X_g=\mathbb H\times\mathbb H\setminus\Gamma_g$. The map $(p,q)\mapsto\big(p,(q-\operatorname{Re}g(p))/\operatorname{Im}g(p)\big)$ identifies $X_g$ with $\mathbb H\times(\mathbb H\setminus\{i\})$, and is orientation-preserving affine on each fibre. So $H_1(X_g)\cong\mathbb Z$, and the class of a loop in $\{p\}\times\mathbb H$ is its winding number about $g(p)$.
- By (★), $\Psi(\mathrm{Teich}(B))\subset X_g$. Since $g$ has no fixed point, $\Delta\subset X_g$.
- Suppose $T^mD_0=D_0$. By Lemma 4.1 there is a path $\sigma\subset D_0$ from $\tau$ to $T^m\tau$.
- $\mathrm{Teich}(B)$ is contractible (F2), so $\sigma\simeq\sigma'_m$ rel endpoints. Applying $\Psi$, the two loops $\Psi\sigma$ and $\Psi\sigma'_m$ are homotopic in $X_g$. They are loops because $\Psi(T^m\tau)=\Psi(\tau)$.
- $\Psi\sigma\subset\Delta$, which is contractible, so $\Psi\sigma$ is null-homologous in $X_g$.
- But $\Psi\sigma'_m=(p_0,f^*\sigma'_m)$ has nonzero class, a contradiction. ∎

---

## 6. The computation at $t_0=\tfrac14$

From now on $f=f_{1/4}$ and $V=V_{1/4}$. Since $(w-1)^2-\tfrac14=(w-\tfrac12)(w-\tfrac32)$,
$$V(w)=-\frac{(w-\frac12)^2(w-\frac32)^2}{4w(w-1)(w-\frac34)} .$$

**Deck group.** Put $g_0(w)=\dfrac{w-3/4}{w-1}$, $g_2(w)=\dfrac3{4w}$ and $g_3=g_0g_2=\dfrac{3(w-1)}{4(w-3/4)}$. Direct substitution gives $V\circ g_0=V\circ g_2=V$:
- under $g_2$: $w-\tfrac12\mapsto-(w-\tfrac32)/(2w)$, $w-\tfrac32\mapsto-3(w-\tfrac12)/(2w)$, and $4w(w-1)(w-\tfrac34)\mapsto 9(w-\tfrac34)(w-1)/(4w^3)$;
- under $g_0$: $w-\tfrac12\mapsto(w-\tfrac12)/(2(w-1))$, $w-\tfrac32\mapsto-(w-\tfrac32)/(2(w-1))$, and the denominator becomes $w(w-\tfrac34)/(4(w-1)^3)$.

So $V$ is Galois with Klein four deck group. The 6 critical points are the fixed points:
- $\tfrac12,\tfrac32$, which lie over $0$;
- $\pm\tfrac{\sqrt3}2$, which lie over $1$;
- $P,\bar P=\tfrac34\pm\tfrac{\sqrt3}4 i$, which lie over $\tfrac14$.

The critical values are therefore $0,1,\tfrac14\in A$.

**Real locus.** $V$ has real coefficients, so $V(w)\in\hat{\mathbb R}$ iff $\bar w=h(w)$ for some deck map $h$:
- $h=\mathrm{id}$ gives $\hat{\mathbb R}$;
- $h=g_0$ gives $C_1:|w-1|=\tfrac12$;
- $h=g_2$ gives $C_2:|w|=\tfrac{\sqrt3}2$;
- $h=g_3$ gives $|w-\tfrac34|^2=-\tfrac3{16}$, which is empty.

$C_1\cap C_2=\{P,\bar P\}$.

**Faces.** All critical values of $V$ are real. So $V$ restricted to $\hat{\mathbb C}\setminus V^{-1}(\hat{\mathbb R})$ is a covering of the two open half-planes, and each complementary component (face) maps homeomorphically onto one half-plane. Adjacent faces map to opposite half-planes, because $V$ is a local homeomorphism along each edge. We need four faces, all inside $C_2$ and hence avoiding $w=1$:
- $L_2=\{\operatorname{Im}w<0,\ |w|<\tfrac{\sqrt3}2,\ |w-1|>\tfrac12\}$;
- $U_2=\overline{L_2}$ (complex conjugate);
- $U_{12}=\{\operatorname{Im}w>0,\ |w|<\tfrac{\sqrt3}2,\ |w-1|<\tfrac12\}$;
- $L_{12}=\overline{U_{12}}$.

**Boundary values.** Each boundary edge contains no point of $V^{-1}(\{0,1,\tfrac14,\infty\})$ except at its ends, so it maps homeomorphically onto the arc of $\hat{\mathbb R}$ between the images of its ends that avoids the other marked values.
- On $(-\tfrac{\sqrt3}2,0)$, $V$ increases from $1$ to $+\infty$. Here $V\approx-3/(16w)$ near $0$, and $V(-\tfrac{\sqrt3}2)=1$.
- On $(0,\tfrac12)$, $V$ increases from $-\infty$ to $0$, with $V(\tfrac14)=v$.
- On $(\tfrac12,\tfrac34)$, $V$ decreases from $0$ to $-\infty$, with $V(\tfrac23)=v$, since $\tfrac23=g_0(\tfrac14)$.
- The $C_1$-arcs from $\tfrac12$ to $P$ and from $\tfrac12$ to $\bar P$ map onto $(0,\tfrac14)$. The alternative arc from $0$ to $\tfrac14$ would pass through $\infty$ and $1$, whose preimages $0,1,\tfrac34,\pm\tfrac{\sqrt3}2$ are not on these arcs.
- $V'(\tfrac14)>0$ and $V$ is real on $\mathbb R$, so $U_2$, which lies just above $\tfrac14$, maps to the upper half-plane.

Hence $U_2$ and $L_{12}$ map to the upper half-plane, and $L_2$ and $U_{12}$ to the lower.

**Lift of $\alpha$.** Let $\beta$ be the lift of $\alpha$ through $V$ starting at $w=\tfrac14$, which lies over $v$.
1. $\alpha$ leaves $v$ downward. Since $V'(\tfrac14)>0$, $\beta$ enters $L_2$. On $\partial L_2$ the preimage of $(1,\infty)$ is $(-\tfrac{\sqrt3}2,0)$, so $\beta$ crosses $\mathbb R$ there, upward, into $U_2$.
2. On $\partial U_2$ the preimage of $(0,\tfrac14)$ is the $C_1$-arc from $\tfrac12$ to $P$. $\beta$ crosses it into $U_{12}$.
3. On $\partial U_{12}$ the preimage of $(v,0)$ is $(\tfrac12,\tfrac23)$. $\beta$ crosses it downward into $L_{12}$.
4. The only preimage of $\infty$ in $\overline{L_{12}}$ is $\tfrac34$ (the poles $0$ and $1$ lie outside $C_1$ and $C_2$ respectively). So $\beta$ ends at $w=\tfrac34=1-t_0$.

$\beta$ lies in the disc $|w|<\tfrac{\sqrt3}2$, which avoids $1$. It crosses the negative real axis once upward and $(\tfrac12,\tfrac23)$ once downward. So, in $\mathbb C\setminus\{0,1\}$,
$$\beta\simeq(\text{clockwise loop about }0\text{ based at }\tfrac14)\cdot[\tfrac14,\tfrac34].$$
In a disc minus one point, the homotopy class is determined by the winding number, which is $-1$.

*Numerical check.* Newton continuation of the explicit semicircle realisation of $\alpha$ through $V$ ends at $w=0.75$, approached from below. The closed loop "$\beta$ followed by $[\tfrac34,\tfrac14]$" has winding number $-1$ about $0$ and $0$ about $1$.

**Lift through $\lambda$.**
- The clockwise loop about $0$ is homotopic to: go from $\tfrac14$ to $\varepsilon$ along $\mathbb R$, around the small clockwise circle, and back. By (F1) its $\lambda$-lift from $p_0=iy_0$ goes up the imaginary axis, decreases $\operatorname{Re}\tau$ by $2$ (as $\lambda\approx16e^{i\pi\tau}$), and comes back down. It ends at $p_0-2$.
- By $\lambda(-1/\tau)=1-\lambda(\tau)$ and $\lambda(\tau-2)=\lambda(\tau)$, the segment $[\tfrac14,\tfrac34]$ then lifts vertically to $-2+i/y_0$.

So the endpoint is
$$q^*=g(p_0),\qquad g=T^{-2}S=\begin{pmatrix}-2&-1\\1&0\end{pmatrix}\in\Gamma(2)S,\quad \operatorname{tr}g=-2 .$$
Here $T$ denotes $\tau\mapsto\tau+1$. So $g$ is parabolic, with no fixed point in $\mathbb H$. A numerical continuation with theta functions gives the endpoint $-2+0.78170\,i=-2+i/y_0$, confirming this.

---

## 7. Conclusion for $f_{1/4}$

**$\alpha$ is simple and $\gamma$ is as claimed.** In the concrete realisation:
- The lower semicircle from $v$ to $2$ has centre $\approx0.870$ and radius $\approx1.130$. The small lower semicircle over $[-\tfrac18,\tfrac18]$ lies within distance $0.995$ of that centre, so strictly inside it.
- The upper semicircle over $[\tfrac18,2]$ has real parts in $[\tfrac18,2]$, so it misses the vertical ray at $\operatorname{Re}z=-\tfrac18$.
- The arc meets $\hat{\mathbb R}$ only at $v,2,\tfrac18,-\tfrac18,\infty$.

So $\alpha$ is simple and meets $B$ only at its ends. Hence $\gamma=\partial N(\alpha)$ bounds a disc containing exactly $v$ and $a_1$.

Any arc with the crossing pattern of the Theorem is isotopic to this one rel $B$. Disjoint chord systems with the same endpoints in each closed half-plane are isotopic rel boundary (Schoenflies). The lifting argument of §6 also used only the crossing pattern.

**$T_\gamma$ is a point push.** Let $\ell$ be the lasso: follow $\alpha$ to near $a_1$, go once around $a_1$, and return. A regular neighbourhood of $\ell$ is an annulus. One of its boundary curves bounds a disc containing only $a_1$ (a trivial twist), and the other is $\gamma$. So by (F4), $\mathrm{Push}(\ell)=T_\gamma^{\pm1}$. In particular $i(T_\gamma)=1$ in $\mathrm{PMod}(S^2,A)$, so $i_*\circ T_\gamma=i_*$.

**$T_\gamma$ preserves $\mathcal D_f$.** Work in the fibre over $p_0$ through $\tau_0$.
- By (F3), a path $\sigma'$ from $\tau_0$ to $T_\gamma^{\pm1}\tau_0$ projects to $\ell$ under $v'$.
- Truncate $\alpha$ to $\alpha'$, stopping just before $a_1$. By the fibre lemma, $w\circ\sigma'$ is the $V$-lift of $\ell$, which is $\beta'\cdot c\cdot\beta'^{-1}$. Here $\beta'$ is the truncation of $\beta$, and $c$ is a small loop about $\tfrac34$; this uses that $\tfrac34$ is a simple preimage of $\infty$.
- Since $\tfrac34\notin\{0,1\}$, $c$ is null-homotopic in $\mathbb C\setminus\{0,1\}$. So its $\lambda$-lift is a small closed loop $\tilde c$ about $q^*$, and $f^*\sigma'=\tilde\beta'\cdot\tilde c\cdot\tilde\beta'^{-1}$ is closed.
- Hence $f^*(T_\gamma^{\pm1}\tau_0)=f^*(\tau_0)$. By Lemma 2.3, $[\tilde T]$ fixes the point $f^*\tau_0$, so $[\tilde T]=1$ by Lemma 2.1.
- Therefore $f^*\circ T_\gamma=f^*$ on all of $\mathrm{Teich}(B)$. Together with $i_*\circ T_\gamma=i_*$ this gives $\Psi\circ T_\gamma=\Psi$, and so $T_\gamma^{\pm1}(\mathcal D_f)=\mathcal D_f$.

**Infinite orbit.** Fix $m\neq0$.
- Let $\sigma'_m$ be the fibre path from $\tau_0$ to $T_\gamma^m\tau_0$ lying over the loop $\ell^{\pm m}$. Then $f^*\sigma'_m=\tilde\beta'\tilde c^{\,m}\tilde\beta'^{-1}$.
- This loop lies in $\{p_0\}\times(\mathbb H\setminus\{g(p_0)\})$ by (★), and its winding number about $q^*=g(p_0)$ is $\pm m\neq0$.
- So the class of $\Psi\circ\sigma'_m$ in $H_1(X_g)\cong\mathbb Z$ is $\pm m$.

Now let $\tau_1\in\mathcal D_f$ be arbitrary and $D_1$ its component. Choose a path $\rho$ from $\tau_0$ to $\tau_1$. Then $\rho^{-1}\cdot\sigma'_m\cdot T_\gamma^m\rho$ is a path from $\tau_1$ to $T_\gamma^m\tau_1$. Since $\Psi\circ T_\gamma^m=\Psi$, its $\Psi$-image is the conjugate loop $(\Psi\rho)^{-1}(\Psi\sigma'_m)(\Psi\rho)$, which lies in $X_g$ and has class $\pm m$.

Suppose $T_\gamma^mD_1=D_1$. Let $\sigma\subset D_1$ be a path from $\tau_1$ to $T_\gamma^m\tau_1$ (Lemma 4.1).
- Contractibility of $\mathrm{Teich}(B)$ makes the two paths homotopic rel endpoints. So their $\Psi$-images are homotopic in $X_g$.
- But $\Psi\sigma\subset\Delta$, which is contractible, so its class is $0$. This is a contradiction.

This is the argument of Proposition 5.1, with the base point moved to $\tau_1$. Hence $T_\gamma^mD_1\neq D_1$ for every component $D_1$ and every $m\neq0$: every orbit of $\langle T_\gamma\rangle$ on $\pi_0(\mathcal D_f)$ is infinite. ∎

---

## 8. Remark on what was used

The argument for $f_{1/4}$ uses only:
- the exact algebra of §§1, 3, 6;
- Lemmas 2.1–2.3, 4.1 and Proposition 5.1;
- the standard facts (F1)–(F5).

The face-by-face lift was checked independently by three separate audits during the attempt, and numerically as recorded above.

---

## 9. Transport to an arbitrary $f$

Fix $t\in W$ and a path $t_s$ in $W$ from $t_0=\tfrac14$ to $t$. Write:
- $f_s=f_{t_s}$;
- $B_s=\{0,\infty,1,t_s,v_s\}$ with $v_s=v(t_s)$;
- $A_s=B_s\setminus\{v_s\}$.

**Lemma 9.1 (isotopy).** There is a jointly continuous isotopy $h_s$ of $\hat{\mathbb C}$ with $h_0=\mathrm{id}$, fixing $0,1,\infty$, with $h_s(t_0)=t_s$ and $h_s(v_0)=v_s$.

*Proof.*
- For $|q|<1$ the map $P_q(z)=z+(1-|z|)q$ is a homeomorphism of the closed unit disc that is the identity on the boundary and sends $0\mapsto q$.
  - It is injective, since $|z-z'|\le|z-z'||q|$.
  - It is surjective, by invariance of domain plus the boundary being fixed.
  - $(q,z)\mapsto(q,P_q(z))$ is a continuous bijection of a compact Hausdorff space, hence jointly a homeomorphism.
- By uniform continuity, cut $[0,1]$ into short intervals on which $t_s$ and $v_s$ stay in small disjoint discs avoiding $0$ and $1$. Compose affine conjugates of $P_q$ in those discs, interval by interval. ∎

**Lemma 9.2 (lift).** There is a continuous family of homeomorphisms $\tilde h_s$ with $f_s\tilde h_s=h_sf_0$, $\tilde h_0=\mathrm{id}$, and $\tilde h_s=h_s$ on $A_0$.

*Proof.* Write $f_s=M_sQN_s$ with $Q(z)=z^2$ (§1).
- Put $k_s=M_s^{-1}h_sM_0$. Then $k_s$ fixes $0$ and $\infty$.
- $K(s,z)=k_s(z^2)$ on $[0,1]\times\mathbb C^*$ lifts through $Q$, because the domain retracts to $s=0$, where $K=Q$. This gives $\tilde k_s$ with $\tilde k_0=\mathrm{id}$.
- By uniqueness of lifts $\tilde k_s$ is odd, hence injective. It is surjective, and it extends by $0\mapsto0$, $\infty\mapsto\infty$ to a homeomorphism.
- Put $\tilde h_s=N_s^{-1}\tilde k_sN_0$. Then $f_s\tilde h_s=h_sf_0$.
- On $A_0$:
  - $\tilde h_s(0)$ is the unique preimage of $h_s(a_1)=\infty$, namely $0$.
  - For $i=1,2,3$, $\tilde h_s(a_i)$ is a continuous selection from the two distinct preimages of $a_{i+1}(s)$, which is not a critical value. These preimages move continuously, and the selection starts at $a_i$. So it equals $a_i(s)=h_s(a_i)$ for all $s$. ∎

Therefore $\kappa_s=h_s^{-1}\tilde h_s$ is an isotopy rel $A_0$ from the identity, so $\tilde h_1\simeq h_1$ rel $A_0$.

**Proposition 9.3.** Let $h=h_1$ and $\tilde h=\tilde h_1$, and define $h^*[\varphi]=[\varphi h]$ from $\mathrm{Teich}(B_t)$ to $\mathrm{Teich}(B_0)$, and likewise on $\mathrm{Teich}(A)$. Then:
- $i_*h^*=h^*i_*$ and $f_0^*h^*=h^*f_t^*$;
- hence $h^*(\mathcal D_{f_t})=\mathcal D_{f_0}$, with components mapping to components;
- $h^*\circ T_{h(\gamma)}=T_\gamma\circ h^*$.

*Proof.*
- If $\varphi f_t=F\psi$, then $\varphi hf_0=\varphi f_t\tilde h=F\psi\tilde h$. So $f_0^*[\varphi h]=[\psi\tilde h]=[\psi h]$ by $\tilde h\simeq h$ rel $A_0$.
- $h^*$ is a homeomorphism with inverse $(h^{-1})^*$.
- $h^*(hgh^{-1}\cdot[\varphi])=g\cdot h^*[\varphi]$, and $hT_\gamma h^{-1}=T_{h(\gamma)}$. ∎

Hence $T_{h_1(\gamma)}$ preserves $\mathcal D_{f_t}$ with infinite orbits on its components.

For an abstract $f$, take $M$ from Proposition 1. The map $M^*:[\varphi]\mapsto[\varphi M]$ satisfies the same identities, with $h=\tilde h=M$, because $f_tM=Mf$. So $\gamma_f=M^{-1}h_1(\gamma)$ works.

**Real $t\in I=(0,\tfrac{3-\sqrt5}2)$.** On $I$, $v(t)<0$, so the order $v_s<0<t_s<1<\infty$ persists along the segment from $\tfrac14$ to $t$. Take $h_s(x+iy)=\phi_s(x)+iy$, where $\phi_s$ is the increasing piecewise-linear map of $\mathbb R$ fixing $0$, $1$ and everything outside a large interval, with $t_0\mapsto t_s$ and $v_0\mapsto v_s$. It preserves $\mathbb R$, both half-planes, and the intervals between marked points. So $h_1(\alpha)$ has the same crossing pattern, with $\tfrac14$ replaced by $t$. Pulling back by $M$ gives the description in Theorem (b).

For non-real $t$ the curve is still $M^{-1}h_1(\gamma)$ with the explicit $h_1$ of Lemma 9.1, but I did not produce a picture-level description independent of the path.

---

## 10. Mapping-class description, and other routes

**$\gamma=T_c^{-1}(\gamma_0)$.**
- The real segment $[\tfrac14,\tfrac34]$, pushed slightly above the critical point $\tfrac12$, maps under $V$ to an arc homotopic to $\alpha_0$, which goes from $v$ up, down through $(0,\tfrac14)$, and below to $\infty$.
- $\beta\simeq\ell_0^{cw}\cdot\sigma^+$, where $\ell_0^{cw}$ is the circle $|w|=\tfrac14$ traversed clockwise. Its image is the loop $L$ at $v$: it goes down, up through $(1,\infty)$, and over back to $v$, i.e. counterclockwise around $\{0,\tfrac14,1\}$.
- So $\alpha\simeq L\cdot\alpha_0$, i.e. $\alpha=\mathrm{Push}(L^{-1})(\alpha_0)$. By (F4), $\mathrm{Push}(L)=T_c$ with $c=\{|z-\tfrac12|=\tfrac35\}$, the other boundary curve being trivial.

A parity check in the coordinate $s=1/z-\tfrac{11}4$, where $f-v=s^2/6$, independently shows that both preimage discs of $S^2\setminus N(\alpha)$ put $f(c_1),f^2(c_1),f^3(c_1)$ on one side (a 3/0 split). This confirms $[\tilde T]=1$.

The same check shows:
- $T_{\gamma_0}$ also preserves $\mathcal D_f$, but for it the element is $g=S$, which is elliptic, so the linking argument gives nothing;
- $T_c$ itself does not preserve $\mathcal D_f$ (the split is 2/1).

**Other routes recorded, not needed.**
- For curves around $\{v,a_j\}$ with $j\in\{0,2,3\}$, $T^2$ preserves $\mathcal D_f$, but no proof of an infinite orbit was found.
- Abelian obstructions cannot work. The image of $H_1(W)$ in $H_1(\mathcal M_{0,5})$ has full rank, so homology classes cannot detect an infinite orbit.
- The cusp $t=\tfrac12$ gives a twist about a $\{a_1,v\}$-curve lying in a component stabiliser, so its orbit is finite.

---

## Status

**Proved.** The Theorem (a) for $f_{1/4}$ and (b) for every $f$, relying on the standard facts (F1)–(F5) and the Schoenflies/chord isotopy remark.

The argument was audited twice. Each audit found and repaired three gaps, now included here:
- the lift must be the explicit $A$-fixing lift of Lemma 2.3;
- components are path components (Lemma 4.1);
- transport to all $f$ (§9).

**Not done / caveats.**
1. (F1)–(F5) are quoted, not proved.
2. For non-real parameters $t$, the curve is described only as the transport $M^{-1}h_1(\gamma)$ along a chosen path in $W$. This is explicit given the path, but the result depends on the homotopy class of the path, and every choice works.
