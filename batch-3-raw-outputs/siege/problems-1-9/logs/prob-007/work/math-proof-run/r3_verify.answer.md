# Verification of the draft proof (r3_verify)

## Verdict

**The main claim is proved for the model map $f_{1/4}$, and by transport for every $f$, assuming the standard facts (F1)–(F5).** Those facts are the modular function $\lambda$, Teichmüller theory, the Bers fibration with point-pushes as deck transformations, the push formula, and continuity of $f^*$. They are quoted correctly.

The claim is: $T_\gamma$ (power 1), with $\gamma=\partial N(\alpha)$ for the explicit arc $\alpha$, preserves $\mathcal D_f$, and every $\langle T_\gamma\rangle$-orbit on $\pi_0(\mathcal D_f)$ is infinite.

I recomputed every algebraic identity by hand, redid the face-by-face lifting in §6, and checked the key topological fact behind "$T_\gamma$ preserves $\mathcal D_f$" by a separate method (item C below). I found no error that breaks the argument. The problems listed under "Errors and gaps" are minor or concern side remarks that the main claim does not use.

## Checks performed (all passed)

**A. Algebra (§1, §3, §6).**
- $b=(t^2+t-1)/(1-t)$ and $c=t(1-2t)/(1-t)$ follow from $1+b+c=t$ and $t^2+bt+c=0$.
- At $t=\tfrac14$: $b=-\tfrac{11}{12}$, $c=\tfrac16$, $c_2=\tfrac4{11}$, $v=1-b^2/4c=-\tfrac{25}{96}$.
- The identity $(t^2+t-1)^2-(t^2-3t+1)^2=4t(1-t)(1-2t)$ holds, so the formula for $v(t)$ is right.
- $v=t$ is equivalent to $(t^2-3t+1)^2+4t^2(1-t)(1-2t)=0$. Expanding gives $9t^4-18t^3+15t^2-6t+1=(3t^2-3t+1)^2$, so the conclusion is correct. (The parenthetical identity printed in the draft is garbled; see E2.)
- The factorisation $f_t=M_t(N_t^2)$ holds: $-2(1-v)c_2=b$ and $(1-v)c_2^2=c$.
- **Lemma 3.1.** Every step is correct:
  - the cross-ratio map $z\mapsto(s_3-s_2)/(z-s_2)$;
  - $s_2^2-s_0^2=1$ and $2us_2=U+1$;
  - $1-w(U+1)+w^2U=t$, hence $U=(w+t-1)/(w(w-1))$;
  - $1-U=((w-1)^2-t)/(w(w-1))$, giving the stated $V_t$.
  - In addition, $V_t(t)=v(t)$.
- **Corollary 3.2 (★).**
  - $V_t$ has degree 4, with simple poles at $0,1,1-t,\infty$.
  - The numerator at $1-t$ is $(t^2-t)^2\ne0$.
  - Since $v'\neq\infty$, we get $w\ne 1-t$.
  - With $\lambda(-1/\tau)=1-\lambda(\tau)$ and fibres of $\lambda$ equal to $\Gamma(2)$-orbits, this gives (★).
- **Lemma 3.3.** The sign-class argument works: $L(z)^2-z^2$ has degree at most 2 and vanishes at 3 distinct points.
- **§6 deck group.** I checked $V\circ g_2=V$ and $V\circ g_0=V$ term by term; both are involutions, and $g_0g_2=g_3$.
- **§6 fixed points.**
  - $g_0$ fixes $\tfrac12,\tfrac32$.
  - $g_2$ fixes $\pm\tfrac{\sqrt3}2$, and $V(\pm\tfrac{\sqrt3}2)=1$ exactly: here $(w-\tfrac12)(w-\tfrac32)=\tfrac32-2w$ and $4w(w-1)(w-\tfrac34)=6w-\tfrac{21}4$.
  - $g_3$ fixes $P,\bar P=\tfrac34\pm\tfrac{\sqrt3}4 i$.
- **§6 real locus.** It is $\hat{\mathbb R}\cup\{|w-1|=\tfrac12\}\cup\{|w|=\tfrac{\sqrt3}2\}$, and the $g_3$ locus is empty. The two circles meet at $P,\bar P$.

**B. Lifting $\alpha$ through $V$ (§6).**
- The 8 faces map homeomorphically onto the half-planes.
- I traced the boundary of each face used. The images of the vertices run monotonically around $\hat{\mathbb R}$:
  - $\partial U_2$, $\partial L_2$: $1,\infty,0,\tfrac14$;
  - $\partial U_{12}$, $\partial L_{12}$: $0,\infty,1,\tfrac14$.
- $V$ increases on $(0,\tfrac12)$, so $U_2$ maps to the upper half-plane.
- The crossing sequence of $\beta$ is $L_2\to U_2$ (across $(-\tfrac{\sqrt3}2,0)$), then $\to U_{12}$ (across the $C_1$-arc from $\tfrac12$ to $P$), then $\to L_{12}$ (across $(\tfrac12,\tfrac23)$, where $\tfrac23=g_0(\tfrac14)$).
- $\beta$ ends at $\tfrac34=1-t_0$.
- The argument of $w$ along $\beta$ decreases by $2\pi$, so $\beta\simeq(\text{clockwise loop about }0)\cdot[\tfrac14,\tfrac34]$ in $\mathbb C\setminus\{0,1\}$.
- The $\lambda$-lift ends at $-2+i/y_0=T^{-2}S(iy_0)$.
- The matrix $\begin{pmatrix}-2&-1\\1&0\end{pmatrix}$ has determinant 1 and trace $-2$, so it is parabolic, has no fixed point in $\mathbb H$, and lies in $\Gamma(2)S$. All correct.

**C. A separate check that $T_\gamma$ commutes with $f^*$ (the 3/0 split).**
- Write $s=1/z-\tfrac{11}4$. Then $f=v+s^2/6$.
- The relevant points are $a_1=\infty\mapsto s=-\tfrac{11}4$, $a_2=1\mapsto-\tfrac74$, $a_3=\tfrac14\mapsto\tfrac54$, and $a_0=0\mapsto s=\infty$.
- Put $Y=f-v$. Along $\alpha$, $\arg Y$ stays in $(-\pi,\pi)$, because all three crossings are with the positive $Y$-axis ($Y=x-v>0$ for $x\in(v,\infty)$).
- So $f^{-1}(\alpha)=\alpha_+\cup(-\alpha_+)$, where $\alpha_+=\sqrt{6\alpha}$ lies in $\operatorname{Re}s>0$.
- In the slit $Y$-plane:
  - the real segment from $Y(a_0)\approx0.26$ to $Y(a_3)\approx0.51$ crosses $\alpha$ once (at $x_2$);
  - the segment from $0.51$ to $Y(a_2)\approx1.26$ does not cross it.
- So $s=\tfrac54$ is separated from $\tfrac74$ and from $\tfrac{11}4$. The involution $s\mapsto-s$ swaps the two sides, so $\tfrac54,-\tfrac74,-\tfrac{11}4$ all lie on one side.
- Both lifts of $\gamma$ are therefore trivial or peripheral in $(S^2,A)$: one bounds $\{a_1,a_2,a_3\}$ against $\{a_0\}$, the other bounds no point of $A$. Hence the lift $\tilde T$ of Lemma 2.3 is isotopic to the identity rel $A$.
- This agrees with the draft's fibre-lifting argument (§7) and with its own parity remark (§10).

**D. Logic of the remaining sections.**
- Lemma 2.2 checks out: $\varphi^{-1}f=f\tilde\varphi^{-1}$. So does Lemma 2.3: the monodromy around $\gamma$ is a product of two transpositions, hence trivial.
- Lemma 4.1 (implicit function theorem at $w=t_1$) is correct.
- Prop. 5.1 is correct, and so is its re-basing in §7: the conjugate loop has the same $H_1$ class.
- In §7, $\gamma=\partial N(\ell)$ for the lasso $\ell$, so $\mathrm{Push}(\ell)=T_\gamma^{\pm1}$. The $V$-lift of $\ell$ is $\beta'c\beta'^{-1}$, because $\tfrac34$ is a simple preimage of $\infty$. The $\lambda$-lift then winds $\pm m$ times about $g(p_0)$, and (★) keeps it off that point.
- The explicit semicircle arc is simple: the small lower semicircle lies within $0.995<1.130$ of the big circle's centre. It meets $\hat{\mathbb R}$ only at $v,2,\tfrac18,-\tfrac18,\infty$, and the crossing pattern is as claimed.
- Lemma 9.2 checks out:
  - $k_s$ fixes $0$ and $\infty$;
  - the lift $\tilde k_s$ exists because the image of $K_*$ lies in $2\mathbb Z$;
  - $\tilde k_s$ is odd by uniqueness of lifts;
  - $\tilde h_s$ fixes $A_0$ by continuous selection, since $a_2,a_3,a_0$ are not critical values.
- Prop. 9.3 checks out: $f_0^*[\varphi h]=[\psi\tilde h]=[\psi h]$, and $h^*T_{h(\gamma)}=T_\gamma h^*$. The $M$-conjugation step is correct too.
- For real $t\in(0,\tfrac{3-\sqrt5}2)$: $v(t)<0$, and the interval avoids $E$, so the order $v<0<t<1<\infty$ persists.

## Errors and gaps, most severe first

1. **(Minor; side claim only.) The identity $\gamma=T_c^{-1}(\gamma_0)$ in §10 is only sketched, and its sign depends on conventions.**
   - I verified topologically that $\alpha\simeq L\cdot\alpha_0$ as arcs from $v$ to the puncture $a_1$. The loop $\alpha\cdot(L\alpha_0)^{-1}$ encloses $\{0,\tfrac14,1\}$ and touches $a_1$, so the two arcs differ only by spinning around the endpoint.
   - I also verified that $c=\{|z-\tfrac12|=\tfrac35\}$ is the nontrivial boundary curve of $N(L)$.
   - Whether the result is $T_c^{-1}$ or $T_c$ depends on the push and twist conventions in (F4), which the draft does not pin down.
   - The further claims in §10 are asserted without proof: that $T_{\gamma_0}$ yields the elliptic element $S$, that $T_c$ gives a 2/1 split, and the "other routes" remarks.
   - None of this is used for the main claim.
2. **(Minor, presentational.)** In Prop. 1 the phrase "after expanding $4t(1-t)^2(1-2t)=(t^2+t-1)^2$" is not a valid identity. The correct computation is the one in A above. The conclusion $v=t\iff(3t^2-3t+1)^2=0$ is right.
3. **(Minor.)** Lemma 9.1's proof ("compose affine conjugates of $P_q$ interval by interval") is a sketch. The discs must be chosen to contain the current positions of $t_s$ and $v_s$ throughout each subinterval. The result is standard isotopy extension (F6), so nothing is at stake.
4. **(Minor.)** The claim that any arc with the stated crossing pattern is isotopic rel $B$ to the concrete arc is only sketched. The appeal to Schoenflies and chord systems is correct in substance: in each half-plane the chords join distinct boundary intervals, so their combinatorics is forced.
5. **(Expository.)** The numerical checks and "three audits" in §§6–8 are not proof. However, every fact they support is also proved by exact algebra or the face analysis, and I re-derived these by hand.
6. **(Scope, not an error.)** For non-real $t$ the curve is given only as $M^{-1}h_1(\gamma)$, which depends on the homotopy class of the chosen path in $W$. Every choice works. A picture-level description is given only for $t\in(0,\tfrac{3-\sqrt5}2)$. This answers "explicitly describe" fully for the model map and the real family, and only up to transport elsewhere. The draft states this caveat itself.
7. **(Conventions.)** The deck action of $\pi_1$ on the Bers fibre and the formula $\mathrm{Push}=T_{\delta_L}T_{\delta_R}^{-1}$ are used only up to sign ($\pm$). This is harmless, since the argument is symmetric under $m\mapsto-m$.

## Conclusion

- **Proved, modulo (F1)–(F5):**
  - $T_\gamma$ preserves $\mathcal D_{f_{1/4}}$;
  - every orbit of $\langle T_\gamma\rangle$ on $\pi_0(\mathcal D_{f_{1/4}})$ is infinite, so there are infinitely many components;
  - the transported curve $M^{-1}h_1(\gamma)$ has the same properties for every $f$ in the family.
- **Not proved / only sketched:**
  - the sign in $\gamma=T_c^{-1}(\gamma_0)$;
  - the side remarks of §10;
  - a path-independent description for non-real $t$.

=== END OF ANSWER r3_verify ===
