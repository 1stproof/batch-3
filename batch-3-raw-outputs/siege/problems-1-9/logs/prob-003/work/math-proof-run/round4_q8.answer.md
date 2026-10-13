# Answer to round4_q8: closing GAP-1 and proving MS

**Plan.**
1. A geometric "bigon trick" shows that the cross relation in $\mathcal S_n(\mathfrak B^*)$ has the same coefficient tensor as a reordering identity in $\mathcal O_q(SL_n)$. The counit then forces the right-edge tensor to be the inverse of the left-edge tensor.
2. Validity in $\mathcal O_q(SL_n)$ forces the cross relation into MS form with $\mathcal R=\mathcal R_0$, the RTT matrix of the bigon.
3. Matching. In a mismatched configuration a *good* corner arc becomes $0$ in $\bar{\mathcal S}$. This contradicts Lê–Yu's nonvanishing of good corner arcs, transported to $\mathfrak B^*$ by cutting. Reversed arcs are handled by a counting argument that uses the same nonvanishing fact.
4. MS then follows from the run's earlier Theorem 7, which was conditional only on facts now established here.

**Ground ring.** A field $\Bbbk\ni q^{\pm1/n}$ with $q$ not a root of unity. In fact $q^2\neq1$ together with the cited structure results suffices. Notation: $\mathcal O=\mathcal O_q(SL_n)$, $U=(u_{ij})$, and $\phi_{top},\phi_{bot}:\mathcal S_n(\mathfrak B)\to\mathcal S_n(\mathfrak B^*)$ as in the prior work. Matrix-entry convention: $(X_1Y_2)_{(ik),(jl)}=x_{ij}y_{kl}$.

---

## 0. Cited inputs (from memory; flagged)

**(S1) Lê–Sikora, bigon.**
- $\mathcal S_n(\mathfrak B)\cong\mathcal O_q(SL_n)$ as Hopf algebras, with $u_{ij}\mapsto$ the matrix generators.
- The generators satisfy $\mathcal R_0U_1U_2=U_2U_1\mathcal R_0$ and $\det_q U=1$, where $\mathcal R_0\in\{R,R^{-1}\}$. Here $R$ is the matrix of the query. Note that $R(q^{-1})=R^{-1}$ (compare entries), so the $q$-versus-$q^{-1}$ convention ambiguity is exactly $\mathcal R_0\in\{R,R^{-1}\}$.
- Transposing $U$ is harmless, because $U\mapsto U^T$ is an automorphism of $\mathcal O_q(M_n)$.
- Counit: $\varepsilon(u_{ij})=\delta_{ij}$.
- Reversed arcs: the reversed arc $\bar u_{ab}$ (right to left, state $a$ on $e_l$, $b$ on $e_r$) equals $\lambda_{ab}\,S(u)_{\pi(a,b)}$. Here $\lambda_{ab}\in\Bbbk^\times$ and $\pi$ is a bijection of $[n]^2$. Lê–Sikora's formula is of this shape, with $\pi$ involving $i\mapsto\bar i=n+1-i$ and a transpose; only "nonzero scalar times a bijection" is used below.
- $\mathcal O$ is a domain with a PBW basis. This is standard.

**(S2) Fusion (Lê–Sikora; Costantino–Lê for $n=2$).** $m:\mathcal O\otimes\mathcal O\to\mathcal S_n(\mathfrak B^*)$, $x\otimes y\mapsto\phi_{top}(x)\phi_{bot}(y)$, is a linear isomorphism. This is GAP B of the prior work: I am confident of the statement but cannot check the general-$n$ reference.

**(E) Lê–Sikora height exchange.** Take two strands ending on one boundary edge, with the same orientation relative to the edge, and a crossing between them next to the edge. This configuration equals $\sum(\text{coefficients})\times(\text{uncrossed diagram with permuted states})$. The coefficient tensor is a nonzero scalar multiple (a power of $q^{1/n}$) of one of $R^{\pm1}$ or $R_{21}^{\pm1}$, where $R$ is taken at $q$ or at $q^{-1}$. That set equals $\{R^{\pm1},R_{21}^{\pm1}\}$, and it is closed under transposition and leg swap ($R^T=R_{21}$). So the uncertainty about exact index conventions is absorbed.

**(LY0) Lê–Yu, definition of bad arcs.**
- At each boundary ideal point, and for each orientation of corner arcs, the bad corner arcs are those whose state pair lies in a fixed strict order: "$i<j$" or "$i>j$" for the pair read in some fixed manner.
- So for each corner and orientation, the bad set is a strict triangle with $n(n-1)/2$ elements.
- Badness is a local property of the corner. It is preserved by embeddings and cuttings that keep the corner and its two edges.

**(LY1) Lê–Yu, reduced bigon.** $\bar{\mathcal S}_n(\mathfrak B)$ is commutative. I recall it as the Laurent algebra $\Bbbk[u_{11}^{\pm1},\dots,u_{nn}^{\pm1}]/(\prod u_{ii}-1)$. Alternative justification: if Lê–Yu's bad condition reads the two states in counterclockwise order around the corner, independent of the arc's orientation, then complementarity (Lemma 4 below) is immediate. The forward $b$ is counterclockwise around $v_t$ from $e_l$ to $e_r$, and the forward $c$ is clockwise around $v_b$, so their ccw readings are $(i,j)$ and $(l,k)$ respectively.

**(LY2) Lê–Yu, cutting.** The Lê–Sikora splitting homomorphism along an ideal arc is an algebra map. It descends to the reduced algebras (Lê–Yu use this to build the quantum trace from the triangle case). It sends a web disjoint from the cut arc to itself.

**(LY3) Lê–Yu, triangle.** In $\bar{\mathcal S}_n(\tau)$, for an ideal triangle $\tau$, every good corner arc (of either orientation) is nonzero. I recall this from the triangle quantum trace, whose image of a corner arc is $0$ exactly for bad arcs. In particular $\bar{\mathcal S}_n(\tau)\ne0$.

**Status.** These are the only inputs taken on trust. (E), (LY0) and (LY1) are convention-free *in the form stated*. That is the point: below, the *matching* of conventions is derived and not read off figures. The nonvanishing (LY3), a theorem proved by Lê–Yu in their own conventions, certifies the match.

---

## 1. The bigon trick: the cross relation (PROVED from S1, E)

**Lemma 1.** There is an invertible tensor $A$, a nonzero scalar multiple of one of $R^{\pm1},R_{21}^{\pm1}$, such that for all $i,j,k,l$:
$$c_{kl}\,b_{ij}=\sum A_{(ik),(i'k')}\,b_{i'j'}\,c_{k'l'}\,(A^{-1})_{(j'l'),(jl)}\quad\text{in }\mathcal S_n(\mathfrak B^*),\tag{1}$$
$$u_{kl}\,u_{ij}=\sum A_{(ik),(i'k')}\,u_{i'j'}\,u_{k'l'}\,(A^{-1})_{(j'l'),(jl)}\quad\text{in }\mathcal O.\tag{2}$$
In matrix form these read $C_2B_1=AB_1C_2A^{-1}$ and $U_2U_1=AU_1U_2A^{-1}$.

*Proof.*

*Step 1: the isotopy in $\mathfrak B^*$.*
- $c_{kl}b_{ij}$ is the diagram $b\cup c$ in which $c$ is at greater height at both edges. Geographically, $b$'s endpoints are nearer $v_t$.
- Slide $c$'s endpoint on $e_l$ along $e_l$, past $b$'s endpoint, keeping it at greater height. This is an isotopy of stated tangles, since the heights stay distinct. Do the same on $e_r$.
- Now $c$ starts at the geographically upper point of $e_l$, crosses over $b$ next to $e_l$, runs below the puncture, crosses over $b$ again next to $e_r$, and ends at the upper point of $e_r$. At each edge, the geographically upper endpoint is the higher one.

*Step 2: resolving the crossings.*
- Apply (E) to the crossing at $e_l$ (two outgoing strands) and to the one at $e_r$ (two incoming strands). Call the coefficient tensors $A$ and $A'$; each is of the form in (E).
- After resolution, the strand joining the two upper endpoints passes above the puncture and is the higher one at both edges. The other strand passes below and is lower. The projections are disjoint, so each resulting diagram is a product $b_{i'j'}c_{k'l'}$.
- This gives (1) with $A'$ in place of $A^{-1}$, where $A$ acts on the $e_l$ states (b-state, c-state) and $A'$ on the $e_r$ states.

*Step 3: the same computation in the bigon.*
- Start from $u_{kl}u_{ij}$ in $\mathcal S_n(\mathfrak B)$ and perform the same two endpoint slides.
- This produces literally the same local crossings at $e_l$ and $e_r$, so the same $A$ and $A'$ appear.
- Resolving gives (2) with $A'$. The local pictures agree because (E) is a local relation.

*Step 4: $A'=A^{-1}$.*
- Apply the algebra map $\varepsilon$ (S1) to (2):
$$\delta_{ij}\delta_{kl}=\sum_{i',k'}A_{(ik),(i'k')}A'_{(i'k'),(jl)}.$$
- So $AA'=I$, i.e. $A'=A^{-1}$. $\square$

## 2. Validity selects $A\in\{\mathcal R_0,\ \mathcal R_{0,21}^{-1}\}$ (PROVED from S1, E)

**Lemma 2.** Up to a scalar, $A=\mathcal R_0$ or $A=\mathcal R_{0,21}^{-1}$.

*Proof.* Take $\mathcal R_0=R$; the case $\mathcal R_0=R^{-1}$ is the same computation with $q\leftrightarrow q^{-1}$. Evaluate (2) at $(i,j)=(1,1)$, $(k,l)=(1,2)$, using the explicit supports below:
- $R$ has off-diagonal entries $(q-q^{-1})$ at row $(a,b)$, column $(b,a)$ for $a>b$.
- $R^{-1}=q^{-1}\sum e_{aa}\otimes e_{aa}+\sum_{a\ne b}e_{aa}\otimes e_{bb}-(q-q^{-1})\sum_{a>b}e_{ab}\otimes e_{ba}$. This follows from Hecke, and its support is the same as that of $R$.
- $R_{21}^{\pm1}$ is obtained by swapping legs. Its off-diagonal entries sit at row $(b,a)$, column $(a,b)$ with $a>b$.

For each candidate $A$, row $(11)$ of $A$ has only the diagonal entry. Column $(12)$ of $A^{-1}$ has an off-diagonal entry exactly when $A^{-1}\in\{R^{-1},R\}$; that entry sits at row $(21)$. The four cases give:
- $A=R$: $u_{12}u_{11}=q\big(u_{11}u_{12}-(q-q^{-1})u_{12}u_{11}\big)$, i.e. $u_{11}u_{12}=q\,u_{12}u_{11}$.
- $A=R^{-1}$: $u_{12}u_{11}=q^{-1}\big(u_{11}u_{12}+(q-q^{-1})u_{12}u_{11}\big)$, i.e. $u_{11}u_{12}=q^{-1}u_{12}u_{11}$.
- $A=R_{21}$: $u_{12}u_{11}=q\,u_{11}u_{12}$, i.e. $u_{11}u_{12}=q^{-1}u_{12}u_{11}$.
- $A=R_{21}^{-1}$: $u_{12}u_{11}=q^{-1}u_{11}u_{12}$, i.e. $u_{11}u_{12}=q\,u_{12}u_{11}$.

In $\mathcal O$ the true relation is $u_{11}u_{12}=q\,u_{12}u_{11}$; the case $A=R$ is just the RTT relation. If $u_{11}u_{12}=q^{-1}u_{12}u_{11}$ also held, we would get $(q-q^{-1})u_{12}u_{11}=0$, which is impossible in the domain $\mathcal O$ because $q^2\ne1$. So $A\in\{R,R_{21}^{-1}\}$ up to scalar. $\square$

**Corollary 3 (MS form).** Let $\mathcal R:=\mathcal R_0$. Then:
- **Case I** ($A\propto\mathcal R_0$): (1) reads $\mathcal R X_1Y_2=Y_2X_1\mathcal R$ with $(X,Y)=(B,C)$.
- **Case II** ($A\propto\mathcal R_{0,21}^{-1}$): (1) reads $C_2B_1=\mathcal R_{0,21}^{-1}B_1C_2\mathcal R_{0,21}$. Conjugating by the flip $P$ gives $C_1B_2=\mathcal R_0^{-1}B_2C_1\mathcal R_0$, i.e. $\mathcal R X_1Y_2=Y_2X_1\mathcal R$ with $(X,Y)=(C,B)$.

In both cases $X$ and $Y$ each satisfy $\mathcal R X_1X_2=X_2X_1\mathcal R$ (likewise for $Y$), by (S1) applied through $\phi_{top}$ and $\phi_{bot}$. $\mathcal R$ has "R-pattern": $\mathcal R_{(ik),(i'k')}\ne0$ only if $(i',k')=(i,k)$, or $i>k$ and $(i',k')=(k,i)$, and the swap entries equal $\pm(q-q^{-1})\neq0$. $\mathcal R^{-1}$ has the same pattern. $\square$

So the geometry fixes the side of the braiding: the matrix is $\mathcal R_0$ itself, and the *only* remaining convention bits are (a) Case I versus Case II, and (b) which triangles are bad. Section 3 shows that (b) is forced by (a).

## 3. Matching (PROVED from §1–2, S1, S2, LY0–LY3)

Write $T_X$ for the set of index pairs $(i,j)$ such that the forward arc $x_{ij}$ is bad at its corner, and define $T_Y$ likewise. By (LY0) each is $\{i<j\}$ or $\{i>j\}$.

**Lemma N (nonvanishing in $\bar{\mathcal S}_n(\mathfrak B^*)$).** Every good corner arc of $\mathfrak B^*$, at $v_t$ or $v_b$ and of either orientation, is nonzero in $\bar{\mathcal S}_n(\mathfrak B^*)$.

*Proof.* Take a corner arc at $v_b$ first.
- Let $d$ be the ideal arc from $v_t$ to $v_t$ encircling the puncture $p$ tightly, and $a_1$ the ideal arc from $v_t$ to $p$.
- Cutting along $d$ and $a_1$ gives two ideal triangles: $\tau_1$ with edges $e_l,e_r,d$ and its corner at $v_b$, and $\tau_2$ with edges $d,a_1',a_1''$.
- A corner arc $\gamma$ at $v_b$ is disjoint from $d\cup a_1$. By (LY2) it maps to $\gamma\otimes1\in\bar{\mathcal S}_n(\tau_1)\otimes\bar{\mathcal S}_n(\tau_2)$, where $\gamma$ is a corner arc at the same corner with the same edges, states and orientation. So it is still good (LY0).
- By (LY3), $\gamma\ne0$ and $\bar{\mathcal S}_n(\tau_2)\ne0$. Over a field this gives $\gamma\otimes1\ne0$, hence $\gamma\ne0$ in $\bar{\mathcal S}_n(\mathfrak B^*)$.

For corner arcs at $v_t$, use instead the loop at $v_b$ around $p$ and the arc from $p$ to $v_b$. $\square$

**Lemma 4 (reversed arcs; complementarity).**
(a) For each corner, the bad reversed arcs there lie in the ideal generated by the bad forward arcs there. Precisely: $\phi_{top}^{-1}$ of the bad reversed arcs at $v_t$ lies in $J_{top}:=(u_{ij}:(i,j)\in T_B)$, and likewise at $v_b$.
(b) $T_B$ and $T_C$ are opposite triangles.

*Proof of (a).*
1. **$J:=J_{top}$ is a Hopf ideal.** For $(i,j)$ in the strict triangle $T$, every $k$ satisfies $(i,k)\in T$ or $(k,j)\in T$, by transitivity of the strict order. Hence $\Delta(J)\subset J\otimes\mathcal O+\mathcal O\otimes J$, and $\varepsilon(J)=0$.
2. **$S(J)\subseteq J$.** In $\mathcal O/J$, $U$ is triangular. Its diagonal entries commute: RTT gives $u_{ii}u_{jj}-u_{jj}u_{ii}=\pm(q-q^{-1})u_{ij}u_{ji}\in J$. Their product is $\det_q U=1$, since every $\sigma\neq\mathrm{id}$ contributes a factor $u_{i\sigma(i)}$ with $(i,\sigma(i))\in T$. So $U$ is invertible in $\mathcal O/J$, with inverse triangular of the same shape. Since $S(U)=U^{-1}$, we get $S(u_{ij})\in J$ for $(i,j)\in T$, and therefore $S(J)\subseteq J$.
3. **Many reversed arcs vanish.** By (S1), the reversed arcs $\bar u_{ab}$ with $\pi(a,b)\in T$ lie in $J$. This set $Z$ has $n(n-1)/2$ elements, and its $\phi_{top}$-images are $0$ in $\bar{\mathcal S}_n(\mathfrak B^*)$.
4. **Counting.** By Lemma N, every element of $Z$ is bad. By (LY0), the bad reversed arcs at $v_t$ also number $n(n-1)/2$. So $Z$ is exactly the set of bad reversed arcs, and all of them lie in $J$. The same argument works at $v_b$.

*Proof of (b).*
- By (a), applied in the bigon (bad reversed arcs at each corner of $\mathfrak B$ are the same state pairs as at the corresponding corner of $\mathfrak B^*$, by locality in LY0), $\bar{\mathcal S}_n(\mathfrak B)=\mathcal O/(J_{T_B}+J_{T_C})$.
- Suppose $T_B=T_C$, say $=\{i<j\}$. Then $\bar{\mathcal S}_n(\mathfrak B)=\mathcal O/J_+$. This algebra is isomorphic to the lower-triangular algebra $P_-$ (prior Lemma 6), hence to $U_q(\mathfrak b_-)$ with its PBW basis (Theorem D(b)).
- In that algebra $u_{11}u_{21}=q^{\pm1}u_{21}u_{11}$ with $u_{21}u_{11}\neq0$. So the algebra is not commutative, contradicting (LY1). The case $\{i>j\}$ is symmetric. $\square$

**Proposition 5 (the match is forced).** In the MS form of Corollary 3, $T_X=\{i<j\}$ and $T_Y=\{i>j\}$. That is, $X$ is lower triangular and $Y$ upper triangular in $\bar{\mathcal S}$.

*Proof.* By Lemma 4(b), the only alternative is $T_X=\{i>j\}$ and $T_Y=\{i<j\}$. Assume it.
- Evaluate $Y_2X_1=\mathcal R X_1Y_2\mathcal R^{-1}$ at $y_{11}x_{21}$, using the R-pattern of $\mathcal R$ and $\mathcal R^{-1}$:
  - row $(21)$ of $\mathcal R$ has entries at $(21)$ and at $(12)$, the latter $=\pm(q-q^{-1})$;
  - column $(11)$ of $\mathcal R^{-1}$ has only the diagonal entry $\rho\neq0$.
- This gives
$$y_{11}x_{21}=\rho\big(\mathcal R_{(21),(21)}\,x_{21}y_{11}\pm(q-q^{-1})\,x_{11}y_{21}\big).$$
- In $\bar{\mathcal S}$ we have $x_{21}=0$, since $(2,1)\in T_X$. Also $x_{11}$ is a unit: in $\mathcal O/J_{T_X}$ the diagonal entries commute and their product is $1$, as in Lemma 4.
- Hence $y_{21}=0$ in $\bar{\mathcal S}$. But $(2,1)\notin T_Y=\{i<j\}$, so $y_{21}$ is a good forward corner arc. This contradicts Lemma N. $\square$

## 4. Proof of MS

**Theorem (MS).** Take $\mathcal R=\mathcal R_0\in\{R,R^{-1}\}$, and $(Z,W)=(B,C)$ in Case I or $(C,B)$ in Case II. Then:
1. $z_{ij}=0$ for $i<j$ and $w_{ij}=0$ for $i>j$ in $\bar{\mathcal S}$;
2. $x_{ij}\mapsto z_{ij}$, $y_{ij}\mapsto w_{ij}$ defines an algebra map $P(\mathcal R)\to\bar{\mathcal S}$;
3. this map is bijective.

*Proof.*
1. Property 1 is Proposition 5.
2. **The ideal.** By Lemma 4(a), the bad-arc ideal is generated by $\phi_{top}(J_{T_B})\cup\phi_{bot}(J_{T_C})$. Here $J$ is triangular-shaped as in Proposition 5.
3. **Relations hold.** In $\bar{\mathcal S}$ the following hold:
   - $\mathcal R$-RTT for $Z$ and for $W$ ((S1) through $\phi$);
   - the mixed relation (Corollary 3);
   - $\prod z_{ii}=\prod w_{ii}=1$ (Lemma 4 step 2).

   This gives Property 2.
4. **Bijectivity.** The prior worker's argument applies verbatim, with $\mathcal R$ in place of $R$:
   - Lemma 3 (index movement) uses only the R-pattern support, which $\mathcal R^{\pm1}$ share.
   - Proposition 4 then gives that $V=m(J_{T_B}\otimes\mathcal O+\mathcal O\otimes J_{T_C})$ is an ideal equal to the bad-arc ideal. Case II is treated below.
   - Corollary 5 (with S2) and Lemma 6 give the linear isomorphism $P_-\otimes P_+\cong\bar{\mathcal S}$.
   - In $P(\mathcal R)$ the diagonal entries commute (triangular RTT) and have product $1$, so they are units.
   - $P(\mathcal R)$ is spanned by ordered products $(\text{X-word})(\text{Y-word})$, using the mixed relation.
   - Theorem 7 then gives bijectivity.

**Case II needs no other-order fusion.** Keep the $b$-left basis of (S2) and use (1) directly. (1) rewrites $c\cdot b$ as $\sum b\cdot c$, with $A=\mathcal R_{0,21}^{-1}$ and $A^{-1}=\mathcal R_{0,21}$, which have the $R_{21}$-pattern.

Index movement for this pattern is checked as follows. A nonzero term of (1) has
- $i'\ge i$ and $k'\le k$ (from $A$);
- $j'\le j$ and $l'\ge l$ (from $A^{-1}$).

So a bad $b_{ij}$ with $i>j$ gives $i'\ge i>j\ge j'$, and the new $b$-entry is bad. A bad $c_{kl}$ with $k<l$ gives $k'\le k<l\le l'$, and the new $c$-entry is bad. Here $B$ is upper and $C$ lower in Case II, by Proposition 5. This is the $(R_{21}^{-1},R_{21})$ line of the query's robustness facts.

Proposition 4 therefore holds with $V=m(J_{T_B}\otimes\mathcal O+\mathcal O\otimes J_{T_C})$ exactly as written. The rest of Theorem 7 goes through after renaming via the flip of Corollary 3. $\square$

**Consequences.** Chain steps 2–5 of the query, already proved in this run, now give:
- Part (1): $\bar{\mathcal S}_n(\mathfrak B^*)\cong U_q(\mathfrak b_-)\bowtie U_q(\mathfrak b_+)$ via $X\mapsto L^-$, $Y\mapsto L^+$ if $\mathcal R_0=R$, and $X\mapsto(L^-)^{-1}$, $Y\mapsto(L^+)^{-1}$ if $\mathcal R_0=R^{-1}$.
- Part (2): $\bar{\mathcal S}_n(\mathfrak B^*)/I\cong U_q^{ext}(\mathfrak{sl}_n)$.

Which of Case I/II and which $\mathcal R_0$ occur is not determined here. As the query states, this is not part of MS.

## 5. Status summary

**Proved here, from the cited inputs (S1), (S2), (E), (LY0)–(LY3):**
- Lemma 1 (bigon trick and counit);
- Lemma 2 (the side of the braiding: $A\in\{\mathcal R_0,\mathcal R_{0,21}^{-1}\}$);
- Corollary 3;
- Lemma N;
- Lemma 4 (reversed bad arcs, i.e. GAP C closed by counting; complementarity);
- Proposition 5 (the matching, i.e. GAP-1/GAP A closed intrinsically);
- MS.

Nothing in the argument reads conventions off figures. The match is forced by the nonvanishing (LY3) together with commutativity of the reduced bigon (LY1).

**Remaining dependencies and gaps, stated explicitly:**
- **GAP B.** (S2) for general $n$, with exact reference. It is used only in the $b$-left form.
- **Citation precision of (LY1)–(LY3).**
  - (LY1) is used only to exclude $T_B=T_C$. The ccw-reading form of Lê–Yu's definition would also suffice.
  - (LY3) is the key external nonvanishing. If only the forward-arc version were available, Lemma 4(a) would need a separate argument; it is the only place reversed arcs enter.
- **(E) and S1's reversed-arc formula.** These are used only in the weak forms stated (R-type up to scalar; a nonzero scalar times a bijection onto antipode entries).
- **Open (not required by MS).** Which of Case I/II and which of $\mathcal R_0=R^{\pm1}$ hold under the literal Lê–Sikora/Lê–Yu conventions. Settling this needs the exact figures.

=== END OF ANSWER round4_q8 ===
