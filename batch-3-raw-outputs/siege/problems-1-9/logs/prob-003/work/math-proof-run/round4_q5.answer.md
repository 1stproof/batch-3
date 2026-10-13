# Answer to round4_q5: gap A (the mixed B–C relation and its compatibility with bad arcs)

## 0. Summary of what is proved
I do not try to reproduce the Lê–Sikora coefficients letter for letter. My recollection of them is not reliable enough for that. The coefficient matrices are instead pinned down structurally. The only inputs are the following.

- **(H1) CITED, Lê–Sikora; form only.** Height exchange is a local relation. Take two endpoints on one boundary edge that are adjacent in height, with both strands oriented away from the edge. The diagram with one height order equals a linear combination of the same diagrams with the opposite height order and the two states changed. The coefficients depend only on the two states and on the local configuration. (In LS it is $q^{-1/n}$ times an R-matrix, but I do not use the explicit values.)
- **(S1) CITED, Lê–Sikora.** $\mathcal S_n(\mathfrak B)\cong\mathcal O_q(SL_n)$ with $u_{ij}\mapsto s\,t_{ij}$, where $s$ is a uniform nonzero scalar. Here $T=(t_{ij})$ satisfies FRT relations $R_0T_1T_2=T_2T_1R_0$ and $\det_qT=1$, with $R_0\in\{R,R_{21}\}$ up to RTT-equivalence.
  - The binary parameter $\epsilon$ ($R_0=R$ or $R_{21}$) absorbs all of the following convention ambiguities: $q\leftrightarrow q^{-1}$ (since $R(q^{-1})=R^{-1}$, RTT-equivalent to $R_{21}$), transposition $u_{ij}\leftrightarrow t_{ji}$ ($R^{t\otimes t}=R_{21}$), the state reversal $i\mapsto n+1-i$ (conjugation by $w_0\otimes w_0$ maps $R$ to $R_{21}$), and replacing $R_0$ by $R_{0,21}^{-1}$.
- **(LY) CITED, Lê–Yu.**
  - (a) A left-to-right corner arc at $v_t$ with states $(i,j)$ ($i$ on the left edge) is bad iff $(i,j)\in T_t$. Here $T_t$ is a STRICT triangle: $T_t=U:=\{i<j\}$ or $T_t=L:=\{i>j\}$; this is the binary parameter $\tau$. Likewise $T_b\in\{U,L\}$ at $v_b$. Badness depends only on the corner, the rotational sense of the arc and its states, so the same $T_t,T_b$ apply in every surface with the same local picture.
  - (b) The reduced algebra $\bar{\mathcal S}_n(\mathfrak T)$ of the ideal triangle is NONZERO. This follows from Lê–Yu's reduced quantum trace, a unital algebra homomorphism $\bar{\mathcal S}_n(\mathfrak T)\to$ a quantum torus.

**Main Theorem (PROVED from H1, S1, LY).** Write $B=(b_{ij})$ and $C=(c_{ij})$.

1. In $\mathcal S_n(\mathfrak B^*)$, already before reduction,
$$c_{kl}b_{ij}=\sum A_{(ik),(i'k')}\,b_{i'j'}c_{k'l'}\,(A^{-1})_{(j'l'),(jl)},\qquad\text{i.e. }A B_1C_2=C_2B_1A,$$
with $A=\alpha P+\beta R_0$ for some scalars $\alpha,\beta$. The same $A$ governs the bigon: $AU_1U_2=U_2U_1A$ in $\mathcal O_q(SL_n)$.
2. The bad triangles are complementary: $T_b=$ the complement of $T_t$ among the off-diagonal entries. In terms of the parameters:
   - If $T_t=U$, then $\alpha=0$ and $A\propto R_0$ ($A\propto R$ if $\epsilon$: $R_0=R$; $A\propto R^{-1}$ if $R_0=R_{21}$). In $\bar{\mathcal S}$, $B$ is lower and $C$ upper triangular.
   - If $T_t=L$, then $A\propto R_{0,21}^{-1}$ (that is, $R_{21}^{-1}$ or $R_{21}$). $B$ is upper and $C$ lower triangular.
3. In every case the configuration is compatible: the span of monomials containing a bad letter is stable under the rewriting by the mixed relation (Lemma 3 of the prior work applies).
4. The MS label is $Z=$ the lower-triangular one of $B,C$, and $\mathcal R\in\{R,R^{-1}\}$ is the representative of the RTT class of $R_0$:
   - $\mathcal R=R$ if $R_0\simeq R$;
   - $\mathcal R=R^{-1}$ if $R_0\simeq R_{21}$.

   The mixed relation reads $\mathcal R X_1Y_2=Y_2X_1\mathcal R$ with $X$ lower and $Y$ upper.

An incompatible combination cannot arise: it would force a product of two invertible diagonal corner arcs in $\bar{\mathcal S}_n(\mathfrak T)$ to vanish, contradicting LY(b).

Item 1 of the theorem is §2–§3, item 2 is §4, items 3–4 are §5, and the consequences for MS are in §6.

---

## 1. Notation
- $\lambda=q-q^{-1}$, and $q$ is generic (in particular $q^2\neq1$ and $q^2\neq-1$).
- $R=q\sum e_{aa}\otimes e_{aa}+\sum_{a\ne b}e_{aa}\otimes e_{bb}+\lambda\sum_{a>b}e_{ab}\otimes e_{ba}$.
- $P=\sum e_{ab}\otimes e_{ba}$ is the flip, and $\check R_0=PR_0$.
- Matrix entries: $(X_1Y_2)_{(ik),(jl)}=x_{ij}y_{kl}$.

Hecke facts:
- $\check R-\check R^{-1}=\lambda$, hence $R^{-1}=R_{21}-\lambda P$ and $R_{21}^{-1}=R-\lambda P$.
- The eigenvalues of $\check R$ are $q$ and $-q^{-1}$, and both eigenspaces are nonzero for $n\ge2$.

Entries of $\alpha P+\beta R$ for $i\ne k$:
$$(\alpha P+\beta R)_{(ik),(ik)}=\beta,\qquad (\alpha P+\beta R)_{(ik),(ki)}=\alpha+\beta\lambda[i>k],$$
and all other entries in row $(ik)$ are $0$. For $R_{21}$ replace $[i>k]$ by $[i<k]$.

Geometry: $\mathfrak B^*$ is drawn with $v_t$ on top, $v_b$ at the bottom, $e_l$ on the left, $e_r$ on the right, and the interior to the right of $e_l$.
- $\Pi(i,j;k,l)$ is the crossing-free diagram: the $b$-arc above the puncture with states $(i,j)$, the $c$-arc below with states $(k,l)$, and endpoint heights in POSITIVE order on both edges.
- $D_l(i,j;k,l)$ is the same diagram with the height order on $e_l$ reversed (non-positive), positive on $e_r$.
- $D_r$ is the same with the height order on $e_r$ reversed.

## 2. Locality: the two products are height exchanges of one planar diagram
**Lemma 2.1.** $\{b_{ij}c_{kl},\ c_{kl}b_{ij}\}=\{D_l(i,j;k,l),\ D_r(i,j;k,l)\}$. Which product is which depends only on the positive-order convention, a binary parameter. Precisely:
- Case I: $b c=D_l$ and $c b=D_r$;
- Case II: $b c=D_r$ and $c b=D_l$.

*Proof.* In $b_{ij}c_{kl}$ the $b$-endpoints are higher on both edges.
- The two arcs are disjoint in projection, $b$ above the puncture and $c$ below. Hence $b$'s endpoint is the one nearer $v_t$ on both edges.
- The boundary orientation runs from $v_t$ to $v_b$ along one of $e_l,e_r$ and from $v_b$ to $v_t$ along the other.
- So "nearer $v_t$ and higher" is positive order on exactly one of the two edges. That edge is $e_r$ if positive order means heights increase along the boundary orientation with $e_l$ oriented downwards; otherwise it is $e_l$.
- $c_{kl}b_{ij}$ has the reversed heights on both edges.

$\square$

By H1 there are matrices $H$ (at $e_l$: both strands leave the edge, and the $b$-strand turns toward $v_t$) and $G$ (at $e_r$: both strands enter) such that
$$D_l(i,j;k,l)=\sum_{i',k'}H^{ik}_{i'k'}\,\Pi(i',j;k',l),\qquad D_r(i,j;k,l)=\sum_{j',l'}G^{jl}_{j'l'}\,\Pi(i,j';k,l').$$

**Same computation in the bigon.** In $\mathfrak B$, $u_{ij}u_{kl}$ is two disjoint arcs, with the arc $(i,j)$ drawn nearer $v_t$ and higher on both edges. This is legitimate because heights are recorded only at endpoints. So, with $\Pi_{\mathfrak B}$ the analogous planar diagram, the same Lemma and the same $H,G$ apply with $u$ in place of both $b$ and $c$. The local pictures at the edges are identical, and H1 says the coefficients depend only on these.

**Lemma 2.2 ($H,G$ are invertible).** Suppose $v^TH=0$ for some vector $v$. Then $\sum_{i,k}v_{ik}D_l(i,j;k,l)=0$ in $\mathfrak B$ for all $j,l$.
- In Case I this reads $\sum v_{ik}u_{ij}u_{kl}=0$; in Case II it reads $\sum v_{ik}u_{kl}u_{ij}=0$.
- By §3 (the degree-2 duality), a relation $\sum v_{ik}t_{ij}t_{kl}=0$ in $\mathcal O_q(M_n)_2$ means $\sum_{ik}v_{ik}x_{(ik),(jl)}=0$ for all $x$ in the commutant $\mathcal U$. Taking $x=1$ gives $v=0$. Case II is the same with $x$ replaced by $PxP$.
- The argument for $G$ is the same.

$\square$

**Corollary 2.3.** Set $(A,A')=(H^{-1},G)$ in Case I and $(A,A')=(H,G^{-1})$ in Case II. Then
$$c_{kl}b_{ij}=\sum A_{(ik),(i'k')}\,b_{i'j'}c_{k'l'}\,A'_{(j'l'),(jl)}\quad\text{in }\mathcal S_n(\mathfrak B^*),\qquad U_2U_1=A\,U_1U_2\,A'\quad\text{in }\mathcal S_n(\mathfrak B)\cong\mathcal O.$$

*Proof (Case I).*
- Write $c b=D_r=G\cdot\Pi$, where $G$ acts on the right states.
- Write $\Pi=H^{-1}\cdot D_l=H^{-1}\cdot(b c)$, where $H^{-1}$ acts on the left states. This is legitimate because $H$ only touches the $e_l$ states.
- Combining, $c_{kl}b_{ij}=\sum_{j',l'}G^{jl}_{j'l'}\sum_{i',k'}(H^{-1})^{ik}_{i'k'}\,b_{i'j'}c_{k'l'}$.
- The bigon is word for word the same.

Case II is symmetric. $\square$

## 3. The double-commutant lemma
**Lemma 3.1.** $A'=A^{-1}$ and $A=\alpha P+\beta R_0$ for some scalars $\alpha,\beta$.

*Proof.*
1. **Transfer to $\mathcal O_q(M_n)$.** By S1, the bigon relation of Cor. 2.3 holds for $T$; the uniform scalar $s^2$ cancels. It is homogeneous of degree 2. A homogeneous degree-2 element of the ideal $(\det_q-1)$ of the graded domain $\mathcal O_q(M_n)$ is $0$:
   - such an element is $(\det_q-1)g$ with $g\ne0$, because $\det_q$ is central;
   - its top degree is $n+\deg_{top}g$ and its bottom degree is $\deg_{bot}g$;
   - homogeneity of degree 2 forces $n+\deg_{top}g=2=\deg_{bot}g$, which is impossible for $n\ge2$.

   So the relation holds in $\mathcal O_q(M_n)_2$.
2. **Duality.** Pair $\langle t_{ij}t_{kl},x\rangle=x_{(ik),(jl)}$ for $x\in\mathrm{End}(V^{\otimes2})$. Then $\langle T_2T_1,x\rangle=PxP$. The FRT relations are annihilated by $x$ iff $\check R_0x=x\check R_0$. So $\mathcal O_q(M_n)_2^*=\mathcal U:=\{\check R_0\}'$. This is standard for the FRT construction, and the computation just given proves it.
3. **The relation in dual form.** The relation $U_2U_1=AU_1U_2A'$ holds iff $PxP=AxA'$ for all $x\in\mathcal U$.
4. **$A'=A^{-1}$.** Take $x=1$: $AA'=1$.
5. **$PA$ lies in the double commutant.** Then $x=(PA)x(PA)^{-1}$ for all $x\in\mathcal U$, so $PA\in\mathcal U'$.
6. **Identify $\mathcal U'$.** $\check R_0$ is diagonalizable with the two distinct eigenvalues $q$ and $-q^{-1}$. So $\mathbb C[\check R_0]=\mathrm{span}(1,\check R_0)$ is a semisimple subalgebra of $\mathrm{End}(V^{\otimes2})$. By the double commutant theorem, $\mathcal U'=\mathbb C[\check R_0]$.
7. **Conclusion.** $PA=\alpha+\beta\check R_0$, that is, $A=\alpha P+\beta PPR_0=\alpha P+\beta R_0$. $A$ is invertible by Lemma 2.2.

$\square$

So $A$ has support in $\{(ik)\to(ik),(ki)\}$, and the mixed relation is $C_2B_1=AB_1C_2A^{-1}$, i.e. $AB_1C_2=C_2B_1A$. This is item 1 of the Main Theorem.

**Remark.** The bigon alone cannot fix $\alpha:\beta$, because $A=P$ makes the bigon relation a tautology. Fixing it needs the reduction, as follows.

## 4. The diagonal test in the reduced triangle
Let $\mathfrak T$ be the ideal triangle with vertices $v_t$ (top), $v_b$ (bottom) and $w$ (right). Its edges are $e=v_tv_b$ (on the left, interior to its right, oriented like $e_l$), $f_t=v_tw$ and $f_b=v_bw$.
- $\beta_{ij}$ is the corner arc at $v_t$ from $e$ (state $i$) to $f_t$ (state $j$).
- $\gamma_{kl}$ is the corner arc at $v_b$ from $e$ (state $k$) to $f_b$ (state $l$).

These are the images $\phi_t(u_{ij})$ and $\phi_b(u_{kl})$ under the embeddings of a bigon onto neighbourhoods of the corners. Embeddings sending boundary edges into boundary edges induce algebra maps (LS). By LY(a), $\beta_{ij}$ is bad iff $(i,j)\in T_t$ and $\gamma_{kl}$ is bad iff $(k,l)\in T_b$, with the same $T_t,T_b$ as in $\mathfrak B^*$, because the local picture at each corner is the same.

**Lemma 4.1.** $\gamma_{kl}\beta_{ij}=\sum_{i',k'}A_{(ik),(i'k')}\beta_{i'j}\gamma_{k'l}$ in $\mathcal S_n(\mathfrak T)$, with the SAME $A$ as in §2.

*Proof.* Only $e$ is shared, and near $e$ the picture is identical to $\mathfrak B^*$ near $e_l$.
- In Case I, $\beta\gamma$ has $\beta$ higher on $e$, which is non-positive, so $\beta\gamma=H\cdot\Pi_{\mathfrak T}$. And $\gamma\beta=\Pi_{\mathfrak T}$. Hence $\gamma\beta=H^{-1}(\beta\gamma)$, and $A=H^{-1}$.
- In Case II, $\gamma\beta=H\Pi_{\mathfrak T}$ and $\beta\gamma=\Pi_{\mathfrak T}$, so $A=H$.

$\square$

**Lemma 4.2.** In $\bar{\mathcal S}_n(\mathfrak T)$ every diagonal corner arc $\beta_{mm}$ and $\gamma_{mm}$ is invertible. Hence $\beta_{kk}\gamma_{ii}\neq0$, using LY(b).

*Proof.*
- Let $J$ be the ideal of $\mathcal O$ generated by the $t_{ij}$ with $(i,j)$ in a strict triangle.
- The FRT relation gives $[t_{ii},t_{jj}]=\pm\lambda\,t_{ij}t_{ji}\in J$.
- The quantum determinant satisfies $\det_qT\equiv\prod t_{ii}$ modulo $J$, because every non-identity permutation contains an entry above the diagonal and one below.
- So modulo $J$ the diagonal entries commute and $\prod_m t_{mm}=1$, hence $t_{mm}^{-1}=\prod_{m'\neq m}t_{m'm'}$.
- The unital algebra map $\phi_t:\mathcal O\to\bar{\mathcal S}(\mathfrak T)$ kills $J$ for $T_t$, by the definition of bad arcs; the scalar $s$ only changes $\prod=1$ to $\prod=s^n$. So $\beta_{mm}$ is invertible.
- The same argument applies to $\gamma$ with $T_b$.
- A product of invertible elements in a nonzero ring is nonzero.

$\square$

**Proposition 4.3 (diagonal test).** For $i\neq k$: if $(i,k)\in T_t$ or $(k,i)\in T_b$, then $A_{(ik),(ki)}=0$.

*Proof.*
- Apply Lemma 4.1 with $j=k$ and $l=i$. Since the support of $A$ is in $\{(ik),(ki)\}$,
$$\gamma_{ki}\beta_{ik}=A_{(ik),(ik)}\beta_{ik}\gamma_{ki}+A_{(ik),(ki)}\beta_{kk}\gamma_{ii}.$$
- In $\bar{\mathcal S}(\mathfrak T)$ one of $\beta_{ik},\gamma_{ki}$ is $0$. So the left side and the first term on the right vanish, leaving $A_{(ik),(ki)}\beta_{kk}\gamma_{ii}=0$.
- By Lemma 4.2, $A_{(ik),(ki)}=0$.

$\square$

**Theorem 4.4 (determination of $A$ and complementarity).** Take $\epsilon$: $R_0=R$; the case $R_0=R_{21}$ is in brackets. Recall $A=\alpha P+\beta R_0$ with $\beta\ne0$ (otherwise $A=\alpha P$, and Prop. 4.3 with $T_t\neq\emptyset$ forces $\alpha=0$, contradicting invertibility).

- **$T_t=U$.** For $i<k$ we have $(i,k)\in T_t$, so
  - $0=A_{(ik),(ki)}=\alpha$ (respectively $\alpha+\beta\lambda$);
  - hence $A=\beta R$ (respectively $A=\beta(R_{21}-\lambda P)=\beta R^{-1}$).
  - For $i>k$: $A_{(ik),(ki)}=\beta\lambda$ (respectively $\alpha=-\beta\lambda$), which is $\neq0$.
  - So $(k,i)\notin T_b$ for all $k<i$, i.e. $T_b\cap U=\emptyset$, and $T_b=L$.
- **$T_t=L$.** For $i>k$:
  - $0=\alpha+\beta\lambda$ (respectively $\alpha$), so $A=\beta R_{21}^{-1}$ (respectively $A=\beta R_{21}$);
  - for $i<k$ the entry is $-\beta\lambda$ (respectively $\beta\lambda$), which is $\neq0$;
  - so $T_b\cap L=\emptyset$, and $T_b=U$.

$\square$

This is item 2. Note that it only uses the $e_l$-test. The $e_r$ matrix is then forced to be $A^{-1}$ by Lemma 3.1.

## 5. Compatibility and the label
**Case $T_t=U$.** Here $A\in\{R,R^{-1}\}$ up to a scalar, which cancels against $A^{-1}$. $B$ has bad set $\{i<j\}$ (so it is lower triangular in $\bar{\mathcal S}$), and $C$ has bad set $\{k>l\}$ (upper).
- The relation $c_{kl}b_{ij}=\sum A_{(ik),(i'k')}b_{i'j'}c_{k'l'}A^{-1}_{(j'l'),(jl)}$ has $A\in\{R,R^{-1}\}$ and $A^{-1}\in\{R^{-1},R\}$.
- All of these have the support described in Lemma 3 of the prior work: $R$ and $R^{-1}=R_{21}-\lambda P$ have the same support. This support gives $i'\le i$, $k'\ge k$, $j'\ge j$ and $l'\le l$.
- If $i<j$ then $i'\le i<j\le j'$; if $k>l$ then $k'\ge k>l\ge l'$. So bad letters stay bad: compatibility holds.
- The relation is $\mathcal R B_1C_2=C_2B_1\mathcal R$ with $\mathcal R=A/\beta$: $\mathcal R=R$ if $R_0=R$, and $\mathcal R=R^{-1}$ if $R_0=R_{21}$.
- MS label: $(Z,W)=(B,C)$ and $X=B$, $Y=C$.
- RTT for $X,Y$ with $\mathcal R$: they satisfy RTT with $R_0$ (as images of $\mathcal O$), and RTT with $R_{21}$ is equivalent to RTT with $R^{-1}$ (Hecke). So they satisfy RTT with $\mathcal R$.

**Case $T_t=L$.** Here $A\propto R_{0,21}^{\mp}$ (that is, $R_{21}^{-1}$ or $R_{21}$), $B$ is upper and $C$ is lower.
- Conjugate $AB_1C_2=C_2B_1A$ by $P$. This gives $A_{21}B_2C_1=C_1B_2A_{21}$, that is, $A_{21}^{-1}C_1B_2=B_2C_1A_{21}^{-1}$.
- So with $X=C$ (lower) and $Y=B$ (upper), $\mathcal R=A_{21}^{-1}/\beta^{-1}$, which is $R$ (if $R_0=R$) or $R^{-1}$ (if $R_0=R_{21}$).
- Compatibility holds by the same support argument after the relabelling.
- MS label: $(Z,W)=(C,B)$.

In all four parameter combinations $(\epsilon,\tau)$ the result is compatible, and $\mathcal R$ is the representative of the RTT class of $R_0$. No incompatible combination can occur, by Prop. 4.3 / Thm 4.4.

## 6. Consequences for MS
Combine the above with the prior work (Prop. 1, Prop. 4, Lemma 6, Thm 7, the reduction lemma) and Theorem D.
- MS items 1–2 hold: the bad entries vanish, and $P(\mathcal R)\to\bar{\mathcal S}$ is a homomorphism. The relations of $P(\mathcal R)$ hold as follows:
  - RTT holds via $\phi_{top},\phi_{bot}$;
  - the mixed relation holds by §2–§5;
  - $\prod x_{ii}=\prod y_{ii}=1$ holds after rescaling by $s$ (Lemma 4.2 argument in $\mathfrak B^*$).
- Item 3 (bijectivity) holds given:
  - **GAP B:** S2, the fusion linear isomorphism $\mathcal O\otimes\mathcal O\cong\mathcal S_n(\mathfrak B^*)$ for general $n$; cited from memory of Lê–Sikora, not verified.
  - **GAP C:** Lê–Yu's bad REVERSED corner arcs at $v_t$ lie in the ideal generated by the bad left-to-right ones. The span-stability argument (Prop. 4 of the prior work) needs the full bad ideal to equal $V$.

  With Gaps B and C granted, the argument is: compatibility (§5) makes $V$ an ideal equal to the bad ideal; Corollary 5 and Theorem 7 of the prior work then give bijectivity.

  Consistency check for Gap C, from memory: the reversed arc with states $(i,j)$ is, by LS, a scalar times an antipode entry $S(t)_{\bar j\bar i}$ with $\bar i=n+1-i$. Modulo $J_t$ with $T_t=U$, $S(T)=T^{-1}$ is lower triangular, so this entry vanishes iff $i<j$. That is the same triangle as $T_t$, matching Lê–Yu's orientation-independent reading. This check rests on remembered formulas and is not proved.
- Then the chain (steps 2–5 of the query) gives part (1). The explicit isomorphism uses whichever of $B,C$ is lower triangular:
  - the lower-triangular one maps to $L^-$, the upper-triangular one to $L^+$, when $\mathcal R=R$;
  - the lower-triangular one maps to $(L^-)^{-1}$, the upper-triangular one to $(L^+)^{-1}$, when $\mathcal R=R^{-1}$;
  - the matrices are rescaled by $s^{-1}$ if needed.

  For example, if $T_t=U$ and $\mathcal R=R$: $b_{ii}\mapsto\hat K_i'^{-1}$, $b_{i+1,i}\mapsto(q^{-1}-q)F_i\hat K'^{-1}_{i+1}$, $c_{ii}\mapsto\hat K_i$, $c_{i,i+1}\mapsto(q-q^{-1})\hat K_{i+1}E_i$, with the higher entries as in Theorem D.
- Part (2): $b_{ii}c_{ii}\mapsto(\hat K_i\hat K_i'^{-1})^{\pm1}$, and Theorem D(c) applies.

## 7. What remains open
1. **The exact values of $(\epsilon,\tau)$** under the published LS/LY conventions. These are needed only to say WHICH of the four explicit formulas is the isomorphism; existence (MS) does not depend on them.
2. **GAP B** (S2 citation for general $n$).
3. **GAP C** (reversed bad arcs). Note that the method of §4 does not settle C: a mismatch there would shrink the corner image to a torus rather than produce a vanishing product of invertible elements.
4. **The cited inputs H1 (form of the height exchange) and LY(b)** (the reduced triangle algebra is nonzero, via Lê–Yu's unital quantum trace) are quoted from memory. H1's form (same strands, states changed, local coefficients) is the only property of the boundary relations used.

**Proved here, given H1, S1, LY:** Lemmas 2.1–2.2, Cor. 2.3, Lemma 3.1, Lemmas 4.1–4.2, Prop. 4.3, Thm 4.4 and §5. This settles gap A: the form of the mixed relation, complementarity of the bad triangles, compatibility in all convention variants, and the MS label as a function of $(\epsilon,\tau)$.

=== END OF ANSWER round4_q5 ===
