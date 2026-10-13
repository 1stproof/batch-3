# prob-003 trace (resp_08288c3a0bfd8ad8006abfcf6ef9c487d180d6a59cde67a51a)

- **web search** (search): ['stated SL_n skein algebra punctured bigon quantum group U_q(sl_n) generalized quantum double', 'SL_n stated skein algebra punctured bigon quantum double Borel subalgebras', 'bigon punctured stated skein algebra U_q(sl_n) b_ij c_ij']

## Reasoning

**Searching for theorem details**

I need to find the exact theorem in the preprint "Quantum traces for SL_n-skein algebras." It seems I should include information about punctured bigons and their relation to Borel and U_q. This might require a specific search to gather the right details on these concepts. It's intriguing to explore how these elements fit into the broader context of the study, so I'll make sure to focus my search effectively on that topic.

- **web search** (search): ['"punctured bigon" "U_q" "sl_n" "skein"', '"punctured bigon" "Borel" "skein" "SL_n"', '"S_n(\\mathfrak{B}^*)" "U_q"']

## Reasoning

**Searching mathematical terms**

The search results aren’t direct, so I’m thinking maybe there’s a specific term like "Frohman-Kania-Bartoszynska" related to punctured bigons. I want to drill down deeper and confirm what I can find. I plan to search for the exact phrase, "\bcS_n", to see if that yields clearer results. There's definitely more to explore here to clarify what I’m looking for!

- **web search** (search): ['"\\mathcal{S}_n(\\mathfrak{B}^*)"', '"\\mathscr{S}_n(\\mathfrak{B}^*)"', '"BigonPGens"']

## Reasoning

**Searching for formulas**

I’ve found Lê-Sikora, which is a great start! Now, I need to dig into the article for the exact formulas regarding bigon and possibly Borel too. I’m thinking it might be useful to check specific lines in the PDF to find what I need. I hope the information is clear and accessible! Let’s see what I can uncover from those lines. This could really help clarify things!

- **web search** (open_page): https://londmathsoc.onlinelibrary.wiley.com/doi/pdfdirect/10.1112/topo.12350

- **web search** (open_page): https://arxiv.org/abs/2201.00045

- **web search** (open_page): https://arxiv.org/pdf/2201.00045

- **web search** (open_page): https://arxiv.org/pdf/2201.00045

- **web search** (open_page): https://arxiv.org/pdf/2303.08082

## Reasoning

**Considering Borel coordinate algebra**

I'm thinking this paper might define a Borel coordinate algebra, which could be useful for working with triangular arcs. It seems like I need to refer to sections 3.6 and 5 for more details. I wonder how these sections will provide clarity on the topic and the implications of using the Borel coordinate algebra in this context. Overall, there’s a lot to unpack here! I'll dive into those sections and see what insights await.

- **web search** (open_page): https://arxiv.org/pdf/2303.08082

- **web search** (search): ['"once-punctured bigon" "Drinfeld double" Borel skein algebra', '"punctured bigon" "Drinfeld double" "Borel" "stated skein"', '"reduced stated skein algebra" "once-punctured bigon" "Drinfeld double"']

## Reasoning

**Researching algebraic structures**

I need to dive into the Korinman finite presentations, which probably includes an explicit Drinfeld double for n=2. The user is interested in SL_n, but I'm not sure if there’s a published theorem for that. I might need to produce a proof using known techniques like LS and FRT/RT. It could be helpful to search for \(\mathfrak B^*\) in the context of "A stated skein algebra" for n=2 to gather more insights.

- **web search** (search): ['"\\mathfrak{B}^*" "stated skein"', '"B^*" "punctured bigon" "stated skein" "Drinfeld"', '"\\mathbb{B}^*" "stated skein"']

## Reasoning

**Examining punctured bigon B**

I'm thinking about the "punctured bigon B dot figure" in relation to Stated skein modules, possibly with n=2. I need to take a closer look at Korinman's paper to clarify this concept. It seems like there might be important details there that could help me understand it better. I want to make sure I'm getting the right information, so checking the source is essential!

- **web search** (open_page): https://arxiv.org/pdf/1907.01732

## Reasoning

**Considering quantum groups**

I'm thinking about this n=2 result and how it might relate to a general case where n is the variable. It feels analogous, possibly to "Bigelow" skein construction in the context of quantum groups, maybe type A? It makes me curious to do a bit more searching to understand how these concepts connect and if there's more clarity to find. I want to dive deeper into this topic!

- **web search** (search): ['Bigelow skein construction quantum groups sl_n punctured disk bigon', '"Skein construction of Quantum Groups" "SL_n"', '"stated skein" "U_q(sl_n)" "punctured bigon" "Drinfeld double"']

## Reasoning

**Deciding on proofs**

I'm considering how to present the necessary information using local relations. It's crucial to decide on a strategy since the user wants complete proofs or citations. We could provide an algebraic proof defining \(\bar S_n(B^*)\) as a known presentation, but we must justify this presentation from skein relations. Citing LS for the bigon, and Lê-Yu for the Borel monogon and gluing over triangles could be essential. I'll need to inspect Lê-Sikora sections carefully.

- **web search** (open_page): https://arxiv.org/pdf/2201.00045

## Reasoning

**Resolving citation conflicts**

I need to figure out the proper citation format, as the user wants a compilable LaTeX document without web citations. Raw web citations won't compile in LaTeX, but system mandates them for factual statements. I think I should use standard bibliographic citations like \(\cite{}\) and avoid any web citation tokens. It’s essential to reference sources properly, such as LS 2024 arXiv and others. Plus, I'll need to ensure my proof aligns with conventions regarding pairing and skein reductions.

## Reasoning

**Building a proof outline**

I think the user's \(\bcS\) probably means reduced, so I'll need to construct a proof. Let's outline the LaTeX document structure: starting with the preamble including theorems and definitions, and then define the ground field as \(\Bbb k=\mathbb Q(q^{1/2n})\) where \(q\) is indeterminate. 

In Section 1, I'll cover algebraic conventions, defining \(V=\Bbb k^n\) and the type A R-matrix. It’s critical to get the definitions right, especially concerning simply connected normalization. After that, I’ll define the FRT Borel double and ensure I choose the correct cross relations to align with skein and double conventions.

## Reasoning

**Defining L matrices**

I'm working with L matrices and laid out some standard relations: \(R L_1^\epsilon L_2^\epsilon = L_2^\epsilon L_1^\epsilon R\) and \(R L_1^+ L_2^- = L_2^- L_1^+ R\). I’ve set \(C = L^+\) (upper) and \(B = L^-\) (lower), leading to the relation \(R C_1 B_2 = B_2 C_1 R\). I need to ensure consistency with \(q\)-commutation and will test it for \(n=2\) to work through the lower B relationship. 

The R matrix can be defined in a specific basis, and using FRT gives relations like \(a b = q b a\) and others. I’ll delve into those without the \(q^{-1/n}\) complication.

## Reasoning

**Analyzing lower relations**

For the lower relation where \(b=0\), I have the equations \(a c = q c a\), \(c d = q d c\), and \(a d = d a\), with the determinant of \(a d\) equal to 1. I'm considering mapping to \(U_q(b_-)\) and might choose \(a = \hat K_1\) and \(d = \hat K_2\). 

In sl2, it looks like \(\hat K_1 \hat K_2 = 1\) and there’s also a connection with how \(F\) behaves with these mappings. I need to ensure \(c\) aligns with this definition as well. If \(c\) is defined correctly, it seems like the simplifying adjustments will help clarify these relationships in the lower diagonal elements.

## Reasoning

**Defining upper and lower relations**

I'm examining the upper C FRT with the structure \([[a,e],[0,d]]\) where \(a e = q e a\). The weight \(E\) follows the relation \(\hat K_1 E = q E \hat K_1\), allowing me to set \(a = \hat K_1\) and find that \(e\) aligns with it as well.

I realize that \(c_{ii}\) maps to \(\hat K_i\) in the upper structure, and that \(b_{ii} c_{ii}\) leads us to identify the lower \(\hat K_i\) with the upper \(\hat K_i\) without needing an inverse. I need to confirm that the off-diagonal elements align correctly, especially for \(n=2\) with the relation \(a c = q c a\).

## Reasoning

**Establishing relationships**

I need to clarify whether I should use \(F \hat K_1^{-1}\) or \(\hat K_2^{-1} F\) in my calculations. I've set \(a = b_{11} = K_1^{-1}\) and \(d = K_2^{-1}\). So, if I let \(c = \lambda F K_1^{-1}\), I find that \(a c = K_1^{-1} F K_1^{-1} = q F K_1^{-2}\) holds. 

Next, with \(d = K_2^{-1}\), I consider the relation \(K_2 F K_2^{-1} = q F\). This leads me to deduce that \(c d = F K_1^{-1} K_2^{-1}\), and since \(K_1\) and \(K_2\) commute, \(c d = q d c\). 

For the lower relations, I conclude \(B_{21} = \lambda F_1 \hat K_1^{-1}\) might work. The upper structure is similar, and I explore allowing \(e\) to equal something like \(K_1 E\), confirming that \(a e = q e a\) still holds true.

## Reasoning

**Clarifying relationships and constants**

Alright, I see that I have the relation \(e d = q d e\) with \(d = K_2\). This leads me to \(K_2 E K_2^{-1} = q^{-1} E\) and rearranging gives \(d e = K_2 K_1 E\), allowing \(e d = K_1 E K_2\). I wonder if this is equal to \(q K_1 K_2 E\). The adjustment of constants is also something I need to finalize. 

For \(C_{12}\), I'm thinking it could be \(\lambda K_1 E\). The constants derived, particularly \(\lambda = (q - q^{-1})\), should align nicely with the standard relations in FRT for \(L^+\) and \(L^-\). Lastly, I plan to delve deeper into cross relations to ensure all components match correctly.

## Reasoning

**Defining quantum root vectors**

I'm working on the quantum root vectors \(C_{ij}\) for \(i < j\). They can be expressed as:

\[
C_{ij} = (q - q^{-1}) \hat K_i E_{ij}^{(+)} + \text{(polynomial in lower simple?)}.
\]

I need to clarify that the \(L^+\) entries for \(j > i\) don't just consist of \(K_i E_{ij}\). For instance, \(L^+_{13}\) has \((q - q^{-1})K_1 E_{13}\), where \(E_{13} = E_1E_2 - q^{-1}E_2E_1\).

To summarize the definitions: for \(i < j\):

\[
E_{i,i+1} = E_i, \quad E_{i,j} = E_{i,j-1}E_{j-1} - q^{-1}E_{j-1}E_{i,j-1}.
\]

For \(i > j\), it could be \(F_{j,i} = F_{i-1}F_{j,i-1} - q F_{j,i-1}F_{i-1}\). I'm pondering whether this \(C_{ij}\) definition satisfies the expected results, particularly for \(C_{13}\).

## Reasoning

**Testing universal R expansion**

I’m examining the universal R expansion with the q-exponential product over roots, which includes terms for composite roots and products of simple root terms. The matrix coefficient in position (1,3) in the natural representation comes from the product \(E_{12}E_{23} = E_{13}\). 

I think the coefficient may involve both the root vector and the product but likely focuses on a single root vector. However, I wonder if the FRT \(L^+\) truly represents the universal R product across all root factors. 

In fundamental representations with nilpotent matrices, the (1,3) entry captures contributions from \(E_{\alpha1+\alpha2}\) and \(E_{\alpha1}E_{\alpha2}\). But with the right choice of root vector and q-commutator, the sum simplifies down to the q-exponential coefficient. It seems defining \(C_{ij}\) through iterated q-commutators and stating them in terms of the \(L^\pm\) matrix coefficients might help provide clarity. 

To formalize this, I’ll define \(L^\pm\) with respect to the universal \(R\)-matrix and consider \(\mathcal R\) as that normalized universal \(R\)-matrix paired appropriately.

## Reasoning

**Defining L-operators in U_q**

I’m looking to define \(L^-\) and \(L^+\) in the respective algebras \(U_q(b_-)\) and \(U_q(b_+)\). For \(L^-\), I'll use the expression \((\pi \otimes \text{id})(\mathcal{R}_{21}^{-1})\) and for \(L^+\), \((\pi \otimes \text{id})(\mathcal{R})\). 

The entries should be explicit and standard. However, the pairing alone isn’t enough; I aim to define things using \(l\)-functionals from the dual coordinate algebra. 

Starting with \(O_q(SL_n)\), I'm exploring its Hopf pairing with \(U_q\). The functionals, \(l^+_{ij}(x) = \rho(x, u^i_j)\), seem crucial in the FRT dual setup.

For proof, I intend to examine the lower and upper \(L\)-operators within the FRT presentation. Here, I need to outline how these operators work, ensuring I avoid any invalid recursion in my definitions.

## Reasoning

**Defining Root-Vectors and Skein Arcs**

I want to define things using the standard root-vector formula, along with references. Then I'll map skein arcs, with \(\Phi(b_{ij}) = \ell^-_{ij} \bipr 1\) and \(\Phi(c_{ij}) = 1 \bipr \ell^+_{ij}\). This looks explicit enough, showing diagonal and simple root formulas, and possibly even composite ones through q-minors. 

Next, I need to prove that \(\Phi\) is an algebra isomorphism. To do this, I will show that \(\bar{\mathcal S}_n(B^*)\) presentation equates to the FRT double. 

I'll start with a helpful lemma discussing the reduced skein algebra of the punctured bigon, where elements \(b_{ij}\) and \(c_{ij}\) generate the relations. I can reference elements like the Lê-Sikora splitting and the Lê-Yu reduced Borel, applying the LS gluing theorem to demonstrate the braided tensor product structure.

## Reasoning

**Analyzing Cross Products and Theorems**

Under the mapping \(\Psi\), the cross product in the braided tensor product is expressed as \(cb = \sum \rho(...)\, b' c'\). When looking at matrix coefficients using \(\rho(u^i_j,u^k_l) = R^{ik}_{jl}\), it simplifies to \(R C_1 B_2 = B_2 C_1 R\), which feels rigorous.

Next, I need to cite the LS Theorem 8.2 about gluing over a triangle, and Theorems 6.3 and 6.4 for the bigon associated with \(O_q\) and coR. I might also refer to the Lê-Yu Theorem for reduced monogons and the Borel algebra representation. 

It could make sense to discuss the topology precisely, looking at the once-punctured bigon as a disk with boundary vertices \(v_-\) and \(v_+\), along with an interior point \(p\) to enhance our understanding.

## Reasoning

**Examining Horizontal Arcs and Monogons**

I’m considering two horizontal arcs: \(b\) above point \(p\) and \(c\) below. If I cut along an ideal arc from \(p\) to the top boundary vertex, it might separate the neighborhoods. Each neighborhood could serve as a once-punctured monogon with one boundary edge. 

I realize that a once-punctured monogon features one boundary edge and one interior puncture, and its skein algebra connects to \(O_q(SL_n\), but not to Borel unless it's reduced. 

If we specifically look at the reduced monogon in Lê-Yu’s context, it operates like a disk with a boundary ideal point and an interior point. Overall, examining whether cutting \(B^*\) along a horizontal line influences the situation is intriguing!

## Reasoning

**Exploring B* Construction**

I’m pondering whether \(B^*\) can be obtained by gluing two copies of \(P_{1,1}\) along their boundary edges. Instead, it seems more accurate to think of \(B^*\) as two reduced monogons glued over an ideal triangle along their boundaries. If I take a disjoint union of these monogons and attach the triangle, the resulting surface ends up with one boundary edge. 

I should avoid relying too much on topology in my final statements, so I'll outline a lemma with proof highlights and citations. However, I note that the reduced skein algebra \(\bar S_n(B^*)\) may fit better in Lê-Yu’s work than Lê-Sikora's. For the proof of the generalized quantum double \(D\) mapping to \(U=U_q(sl_n)\), there are canonical inclusions to consider for the lower torus as well.

## Reasoning

**Analyzing Kernel in Double Lower Diagonal**

I'm examining the double lower diagonal where \(L^-_{ii}=(\hat K_i^-)^{-1}\). The lower Borel generator \(\hat K_i^-\) maps to \(\hat K_i\) while the upper \(\hat K_i^+\) also maps to \(\hat K_i\). So, when I look at \(\pi(B_{ii}C_{ii})\), it results in \(\hat K_i^{-1}\hat K_i=1\), meaning it's an ideal in the kernel. 

To confirm the kernel's generation, I need to show that the quotient by the ideal is \(U_q(sl_n)\). I'll demonstrate that the map is surjective, as the images include \(E_i, F_i, \hat K_i\). For instance, \(E_i\) comes from \(C_{i,i+1}\) times diagonal inverse, and \(F_i\) from \(B_{i+1,i}\) with a similar process. The kernel fits exactly with the ideal, and I’ll clarify that while there are linear product constraints, we're still generating all \(n\).

## Reasoning

**Clarifying Algebraic Double Relations**

I’m noticing a potential issue: the simply-connected \(U_q(sl_n)\) has a torus weight lattice of rank \(n-1\) and uses \(\hat K_i\) where the product \(\prod \hat K_i = 1\). In the double, each Borel has this product relation meaning the product of all \(b_{ii}c_{ii}=1\) is redundant. Okay, now I want to focus on the cross relation and the algebraic double.

To prove that \(D_{\rm FRT} \cong D\), I’ll reference the standard theorem about the "RLL presentation of quantum double," stating it based on works by Faddeev, Reshetikhin, and Takhtajan. I'll frame this as a lemma with proof that includes how the \(L^\pm\) entries satisfy the RLL relations due to quasitriangularity. The RLL entries generate Borels, and their relations serve as a presentation from the PBW/triangular decomposition. 

Since the user is looking for a complete rigorous proof, I’ll prepare a complete LaTeX document, probably aiming for 200-300 lines of content, including a bibliography but keeping verbosity to a manageable level.

## Reasoning

**Defining Quantum Parameters Clearly**

I need to carefully consider the convention around symbols like \(q\) and \(\hat q\). Let's avoid ambiguity here: Lê-Sikora uses \(v=q^{1/(2n)}\), while Lê-Yu uses \(\hat q\), with \(q=\hat q^{2n}\). The user is pairing with \(q\), so I’ll stick to that while working over \(\Bbb k=\mathbb Q(q^{1/n})\) where \(q\) is the quantum group parameter.

Also, the R-matrix includes \(q^{-1/n}\), and if someone opts for a different normalization, diagonal arcs may be scaled. Given that the pairing includes \(q^{1/n-\delta}\), it looks like our R is accurate. I should define the differences between \(O_q(B^-)\) and \(U_q(b_-)\) as well. The reduced skein Borel’s lower triangular coordinate algebra, \(\mathcal O_q(B^-)\), aligns with FRT lower. It appears to be isomorphic to \(U_q(b_-)\) through \(L^-\) but in the algebraic sense, not Hopf. 

I’ll prepare a detailed finite presentation with matrices \(B=(b_{ij})\) and \(C=(c_{ij})\), defining \(B_1=B\otimes I\) and so forth, keeping the entries in \(M_n(\bar S)\).

## Reasoning

**Clarifying Relations and Determinants**

I’m looking at these relations:  
\[
R B_1B_2=B_2B_1R,\quad R C_1C_2=C_2C_1R,\quad R C_1B_2=B_2C_1R.
\]  
If \(B\) is a lower triangular matrix with diagonal \(K^{-1}\), the RTT relation still holds; likewise for \(C\) with \(K\) as upper triangular. 

Now, since we have a triangular structure, the quantum determinant is expressed as \(\prod \text{diag}=1\). Each diagonal element like \(b_{ii}\) and \(c_{ii}\) is considered invertible. However, I need to ensure that although the product is 1, it doesn’t guarantee each element is independently invertible. If they commute, each element can be expressed in terms of the product of the others.

The "bad arc" reductions dictate:
\[
b_{ij}=0 \ (i<j),\quad c_{ij}=0\ (i>j.
\]  
I need to ensure how we set the upper and lower triangular forms. For the arcs below, they might actually work as upper arcs, depending on orientation. If both horizontal arcs point to the right, the boundary orientation could reverse the state order, possibly causing it to be classified as upper.

## Reasoning

**Defining Arc Conventions and Mappings**

I’ll start by setting conventions for the figure: the \(b\)-arcs, which are above the puncture, are considered lower arcs, while the \(c\)-arcs below are upper arcs. If the figure is different, perhaps rotated, it's likely that the question is assuming this setup. I might need to clarify with boundary ordering as shown in \(\BigonPGens\).

When both arcs in \(\mathfrak B^*\) are directed to the right, we can state that \(b_{ij}=0\) for \(i<j\) and \(c_{ij}=0\) for \(i>j\).  

Next, I’ll define the mapping:  
\[
\Phi:\bcS_n(\mathfrak B^*)\to U_q(b_-)\bipr U_q(b_+)
\]  
with:  
\[
\Phi(b_{ij})=\ell^-_{ij}\bipr 1,\quad \Phi(c_{ij})=1\bipr\ell^+_{ij}.
\]

Here, \(\ell^-_{ij}=0\) for \(i<j\) and \(\ell^+_{ij}=0\) for \(i>j\). I want to define \(\ell^-_{ii}=(\hat K_i^-)^{-1}\) and \(\ell^+_{ii}=\hat K_i^+\), along with \(\ell^-_{i+1,i}\) and \(\ell^+_{i,i+1}\).

I need to remember that \(\hat K_i^\pm\) are copies in the two Borels, and I can recursively define the other entries using \(q\)-commutator root vectors. We can express:  
\[
\ell^+_{ij}=(q-q^{-1})\hat K_i^+ E_{ij} \ (i<j)
\]  
and  
\[
\ell^-_{ij}=(q^{-1}-q)F_{ij}(\hat K_j^?)^{-?}.
\]

For the lower index \(i>j\), I may consider an appropriate diagonal factor.

## Reasoning

**Clarifying Entries and Relations**

I’m considering the expression for \(\ell^-_{ij}\), which I’ve defined as:  
\[
\ell^-_{ij}=(q^{-1}-q)F_{ij}(\hat K_j^-)^{-1}, \quad \text{for } i>j.
\]  
Here, \(F_{ij}\) represents the root vector for the negative root \(\epsilon_j-\epsilon_i\). I’m checking the relationship with \(d = b_{ii} = K_i^{-1}\). In this case, for the entry \(c = B_{ij} = F_{ij}K_j^{-1}\), I need to confirm the commutation of diagonal \(K_a^{-1}\) elements.

If \(a=i\) (at the bottom row), I wonder about how \(K_i^{-1} F_{ij}\) relates to the weight involving \(\epsilon_i-\epsilon_j\). The weight of \(F_{ij}\) leads to discussions about negative roots and \(K_i\) acting on it.

For the upper entries, I’ve defined \(\ell^+_{ij}=(q-q^{-1})\hat K_i E_{ij}\). However, I realize that additional \(q\) powers might arise from the universal \(R\) matrix, though only if \(E_{ij}\) is normalized correctly.

Finally, to clarify, I’ll define \(E_{ij}\) through the \(\ell^+\) formula:  
\[
E_{ij}:=(q-q^{-1})^{-1}(\hat K_i)^{-1}\ell^+_{ij}.
\]  
But I need to be careful not to introduce false composites. So I’ll mention only the super/subdiagonal formula first, and for \(|i-j|>1\) entries, I’ll state they’re standard FRT root vectors defined by previous values and relevant references.

## Reasoning

**Defining Elements and Multiplication**

I need to ensure that the “explicit map” is still connected to the \(\ell\) entries. It might be good to mention that if desired, I can take \(E_{ij}=T_i\cdots\) as the Lusztig root vector and \(F_{ij}=\omega(E_{ij})\); with this normalization, the formula should hold. But I want to be careful, so let’s keep things clear.

I’ll define \(\ell^\pm_{ij}\) as the entries of the FRT \(L\)-operators, detailing the diagonal and simple root entries. For generalized quantum double multiplication between \(x, y \in U_q(b_-)\) and \(a, b \in U_q(b_+)\), I’ll include the relevant formula. I could say, “the generalized quantum double” is known, but I'll include the precise formula for completeness.

Furthermore, I plan to refer back to Majid's double cross product when discussing the skew pairing \(\tau:A\otimes B\to k\).

## Reasoning

**Defining Product Relations in Quantum Algebras**

If I have \(A = U_q(b_+)\) and \(B = U_q(b_-)\), the product in \(B \bowtie A\) can be expressed as:

\[
(b \otimes a)(b' \otimes a') = \sum \tau(a_{(1)}, b'_{(1)}) \tau(a_{(3)}, S b'_{(3)})\, b b'_{(2)} \otimes a_{(2)} a'.
\]

Alternatively, I could use another variant:

\[
(1 \otimes a)(b \otimes 1) = \sum \langle a_{(1)}, b_{(1)} \rangle b_{(2)} \otimes a_{(2)} \langle a_{(3)}, S(b_{(3)}) \rangle.
\]

I also want to consider the cross relation and the sign of \(S\). For the standard Drinfeld double finite \(H\), the relation is 

\[
h f = \sum f_{(2)} h_{(2)} \langle f_{(1)}, S^{-1} h_{(3)} \rangle \langle f_{(3)}, h_{(1)} \rangle.
\]

I might also express the multiplication in terms of \(B \otimes A\):

\[
(1 \otimes a)(b \otimes 1) = \sum b_{(2)} \otimes a_{(2)} \langle a_{(1)}, S^{-1}b_{(3)} \rangle \langle a_{(3)}, b_{(1)} \rangle.
\]

While this may not yield a commutator directly, I can simply state: "Multiplication is the standard one; the only property used is the RLL presentation of Lemma...". 

For completeness, I’ll include the relevant formulas and citations in a LaTeX document. I’ll format it like this:

```
\documentclass[11pt]{article}
...
\newcommand{\biprod}{\bowtie_\langle}
...
\begin{document}
\title{...}
...
\begin{abstract}
...
\end{abstract}
```

I'll ensure no extraneous commentary is present since the user requested it to be a LaTeX document.

## Reasoning

**Drafting a LaTeX Document**

I’ll prepare a code block with the LaTeX content without any unnecessary markdown fences, ensuring it’s just the raw text as it should be compilable. The final output will include all necessary details like theorem statements and proofs for lemmas. Here’s a skeleton of the document:

```
\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,amsthm,mathrsfs}
\usepackage[margin=1in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}

\newtheorem{theorem}{Theorem}[section]...
\newcommand{\k}{\Bbbk}
\newcommand{\Sbar}{\overline{\mathcal S}}
...
\begin{document}
\title{The once-punctured bigon and the Drinfeld--Tanisaki double}
...

Throughout \(q\) is an indeterminate and \(\Bbbk=\mathbb Q(q^{1/n})\). All skein algebras are reduced stated \(SL_n\)-skein algebras with skein parameter normalized as in Lê-Sikora; \(\bcS\) in the question is denoted \(\overline{\mathcal S}\).
``` 

This structure should meet the requirements for a compilable LaTeX document.

## Reasoning

**Defining Section Conventions**

In the section on conventions, the R-matrix is defined as:

```
R=q^{-1/n}( q\sum_i E_{ii}\otimes E_{ii}+\sum_{i\ne j}... +(q-q^{-1})\sum_{i<j}E_{ij}\otimes E_{ji})
```

This R aligns with coR values, and the scalar \(q^{-1/n}\) might be significant for pairing. However, since the scalar cancels in the RTT framework, it's consistent across both sides. The entries for \(\rho\) come from LS line 3790. I should define \(D_q\) and consider using matrices \(B\) and \(C\) in the theorem. 

For Lemma 1 (the skein presentation), I'll state:

```
The algebra \Sbar_n(B^*) is generated by b_{ij},c_{ij} and the matrices B,C satisfy...
```

The proof will indicate that bad arcs imply a triangular structure.

## Reasoning

**Explaining Boundary Relations**

I need to explain that at the two boundary vertices, the reduced relation eliminates a boundary-parallel arc when its initial state is smaller than the terminal state in positive boundary order. For the upper corridor, this results in \(b_{ij}=0\) for \(i<j\) and for the lower corridor, \(c_{ij}=0\) for \(i>j\).

By cutting off each corridor, I identify a subalgebra linked to the reduced skein algebra of \(P_{1,1}\). Lê-Yu Theorem 5.1 connects this to lower/upper Borel FRT algebras, maintaining the same \(RBB\) and \(RCC\) products.

The splitting and gluing theorem (LS Theorem 8.2) indicate that the entire algebra is a braided tensor product. I should mention how the braided tensor product's cross relation is represented by \(C_1B_2\), and with coR \(\rho(u^i_j,u^k_l)=R^{ik}_{jl}\) (as per LS Theorem 6.4). This establishes the generation of the algebra.

Additionally, the PBW/quasimonomial bases in Lê-Yu demonstrate the absence of further relations, confirming that the braided tensor product operates like a tensor product vector space. I need to cite the "no further relations" statement from Lê-Yu's quasimonomial basis and LS's gluing linear isomorphism for rigor.

## Reasoning

**Explaining Isomorphism in Algebra**

If \(\bar S(B^*)\) represents a braided tensor product of two Borel monogon algebras, then it follows that the vector space acts as a tensor product with no further relations. 

Now, in Lemma 2, the assignment \(B \rightarrow L^-, C \rightarrow L^+\) establishes an isomorphism from the algebra represented by relations to \(D\). The proof shows that elements satisfy the RLL relations and generate \(D\) since simple entries can recover \(\hat K, E, F\).

Wait, it seems that \(B_{i+1,i}\) connects with \(F_i\) correctly. I also need to ensure that I maintain clarity on the inverse mappings for the explicit transformation. Overall, this structure appears solid!

## Reasoning

**Explaining the Quotient Theorem**

Let's define \(J\) as the ideal in \(D\) generated by the expression \(B_{ii}C_{ii}-1 = (\hat K_i^-)^{-1}\hat K_i^+-1\). I’ll create a mapping \(\pi:D\to U\), where \(\pi(x^-\bipr x^+)=\iota_-(x^-)\iota_+(x^+)\). The mappings \(\iota_-\) and \(\iota_+\) translate specific elements between the algebras.

I need to show that the relations of cross commutations in \(U\) align with the double after torus identification due to the Drinfeld-Tanisaki pairing, which is standard practice. Also, \(J\) is included in the kernel of \(\pi\).

By proving the equality of the kernel using PBW, I illustrate how double PBW as a vector space identifies the two lattice algebras, confirming the relation \(B_i C_i=1\) with proper identification of \(K_i\). I’ll conclude with ensuring the quotient corresponds to \(U_q(sl_n)\), not \(U_q(gl_n)\). That sounds good!

## Reasoning

**Mapping from Skein Quotient to \(U\)**

Since each torus copy has a product equal to \(1\), the quotient torus has a rank of \(n-1\. I can create an explicit mapping from the skein quotient to \(U\) like this:

- \(b_{ii}\) maps to \(\hat K_i^{-1}\)
- \(c_{ii}\) maps to \(\hat K_i\)
- \(b_{i+1,i}\) becomes \((q^{-1}-q)F_i\hat K_i^{-1}\)
- \(c_{i,i+1}\) goes to \((q-q^{-1})\hat K_i E_i\)

I’ll also identify higher arcs to their corresponding \(L^\pm\) entries in \(U\). The inverse mappings include:

- \(\hat K_i\) mapping to \(c_{ii}=b_{ii}^{-1}\)
- Entries for \(E_i\) and \(F_i\) derived from \(c_{ii}^{-1}\) and \(b_{ii}^{-1}\)

It’s essential to consider that the images of diagonal relations \(b_{ii}c_{ii}=1\) generate similar ideals as the entire set from \(n-1\). In the quotient, I expect the cross relation to reproduce \([E,F]\).

Lastly, if there’s a different convention for \(R\) or the diagram, I might need to adjust the orientations accordingly, although that’s likely not necessary.

## Reasoning

**Creating the Bibliography**

I need to include a bibliography section, which will look like this:

```
\begin{thebibliography}{99}
\bibitem[CP]{CP} V. Chari and A. Pressley, A Guide...
\bibitem[FRT]{FRT} L. D. Faddeev, N. Reshetikhin, L. Takhtajan, Quantization of Lie groups...
\bibitem[KS]{KS} A. Klimyk and K. Schmudgen...
\bibitem[LS]{LS} T. T. Q. Lê and A. S. Sikora, Stated SL(n)-skein modules and algebras, J. Topology 2024 / arXiv.
\bibitem[LY]{LY} T. T. Q. Lê and T. Yu, Quantum traces for SL_n-skein algebras, arXiv:2303.08082.
\bibitem[Maj]{Maj} Majid, Foundations...
\end{thebibliography}
```

Next, I should cite the exact theorem numbers like LS Theorem 6.3 for the bigon, Theorem 6.4 for cobraiding, and Theorem 8.2 for gluing.

I’ll also need to reference LY Section 3.6 and Proposition 3.9 about the coordinate Borel, along with Theorem 5.1 regarding the reduced punctured monogon and its quotient. Specifically, I should mention that "Theorem 5.1 of Lê-Yu concerns \(P_{1,1}\) and \(\overline{\mathcal F}\)." 

I'm mulling over whether they might want proof of isomorphism for \(\mathcal S_n(B^*)\) leading to the double, instead of the reduced form.

## Reasoning

**Defining the Skein Algebra**

It seems the double dimension of the Borel algebra suggests a reduced form. The full skein algebra for a punctured bigon would actually be larger, possibly involving two copies of the full \(O_q(SL_n)\).

Quotienting by the ideal generated by \(b_{ii} c_{ii} - 1\) leads to \(U_q\), but if I don't reduce the bad arcs, those extra arcs won't cancel out. So, it's clear that \(\bcS\) is indeed reduced. 

I'll define "reduced" in the document as meaning it is quotiented by the ideal generated by bad boundary-parallel arcs, which enforces triangularity relations. 

Additionally, I should clarify the horizontal arcs \(b, c\) by stating that \(b_{ij}\) denotes the arc above the puncture from left state \(i\) to right state \(j\), while \(c_{ij}\) is below the puncture, oriented left to right. Boundary states follow the standard positioning used in LS, where \(b\) is positioned lower. If the orientation is reversed, adjustments will be necessary.

I’ll compile this into a final answer written in LaTeX, complete with a proof.

## Reasoning

**Refining the Bibliography and Lemmas**

I see there’s a potential issue with the term "compilable" and using Unicode in the bibliography, specifically for Schmüdgen. To avoid confusion, I need to use ASCII or a LaTeX accent: Schm\"udgen, L\^e.

Also, I’ll define \newcommand{\bipr}{\mathbin{\bowtie}} to avoid undefined terms like "\bipr". 

Now, for formulating lemmas elegantly, my proof of "RLL double" might start by letting \(A\) be an algebra with FRT relations. There’s a homomorphism \(A \to D\) via \(B,C\), which is surjective. 

For injectivity, if I order monomials by lower root entries for \(B\), diagonal \(B\), diagonal \(C\), and upper root entries for \(C\), the RLL relations act as rewriting rules. The Diamond lemma and PBW theorem for FRT Borel doubles yield a basis indexed by \(\mathbb N^{\Phi^+}\times \Lambda\times \Lambda\times \mathbb N^{\Phi^+}\), which matches the PBW basis of \(D\). This means there’s no kernel.

For the proof of the skein presentation, I can simply state that "This is the presentation delivered by the cited theorems", without rehashing detailed local derivations, since the user allows citations. It’s important to ensure I cite all intermediate sources.

## Reasoning

**Clarifying Notation and Theorems**

I think I need to add a footnote mentioning that the normalization of \(R\)'s scalar isn't relevant in RLL; it's there just to align with the pairing. 

As I write the final version, I’ll ensure that all commands are properly defined, like \operatorname and \mathbb. I might not need \Upsilon; that’s fine.

For the theorem, I'm thinking of stating: 

\[
\begin{theorem}[Main isomorphism]
...
\Phi(b_{ij})=L^-_{ij}\bipr 1, \Phi(c_{ij})=1\bipr L^+_{ij}.
\]

Actually, I should use \(L^-_{ij}\bipr 1\) within the double because \(L^-_{ij}\) belongs to \(U_q(b_-)\), and \(L^+_{ij}\) belongs to \(U_q(b_+)\).

At the inverse, I have: 

\[
\Phi^{-1}((\hat K_i^-)^{-1}\bipr1)=b_{ii},...
\]

For \(F_i\), it follows that \(\Phi(b_{i+1,i})=(q^{-1}-q)F_i(\hat K_i^-)^{-1}\bipr1\). Thus, in the inverse: 

\(F_i\bipr 1\mapsto (q^{-1}-q)^{-1} b_{i+1,i} b_{ii}^{-1}\). 

Since \(b_{ii}\) q-commutes with \(b_{i+1,i}\), order matters here. 

Next, for \(E\), I have \(c=(q-q^{-1})K_i E = (q-q^{-1}) c_{ii} E\). By multiplying left with \(c_{ii}^{-1}\): 

\(E=(q-q^{-1})^{-1}c_{ii}^{-1} c_{i,i+1}\). 

Finally, I need to clarify my notation for \(\hat K_i^-\) and \(K_i^{-}\), potentially using \(\hat K_i^{(-)}\) and \(\hat K_i^{(+)}\) to avoid confusion with exponents. I'll define \(K_i^-:=\hat K_i\in U_q(b_-)\) and \(K_i^+:=\hat K_i\in U_q(b_+)\), but I realize \(K_i^-\) could imply a negative power, so I’ll be cautious with that.

## Reasoning

**Defining Generators and Relations**

I’m deciding between using \(\widehat K_i^{\rm l}\) and \(\widehat K_i^{\rm r}\). I think I’ll define \(H_i^-\) and \(H_i^+\) as the toral generators in the lower and upper Borel. This means \(L^-_{ii}=(H_i^-)^{-1}\) and \(L^+_{ii}=H_i^+\). The quotient relation gives us \((H_i^-)^{-1}H_i^+=1\).

For clarity, I’ll use \(H\) in the formulas:

\[
L^-_{i+1,i}=(q^{-1}-q)F_i(H_i^-)^{-1};\quad L^+_{i,i+1}=(q-q^{-1})H_i^+E_i.
\]

In the quotient, \(H_i^-=H_i^+=\hat K_i\). I also need to mention that \(H_1^\pm\cdots H_n^\pm=1\). I’ll define the Borel \(U_q(b_+)\) generated by \(E_i,H_i^{+\pm1}\) and \(U_q(b_-)\) generated by \(F_i,H_i^{-\pm1}\). 

The \(H_i\) satisfy the product equals 1. For pairing, I can express it as:

\[
\langle H_i^+,H_j^-\rangle=q^{1/n-\delta_{ij}}, \langle E_i,F_j\rangle=...
\]

It’s important to ensure this matches the standard skew pairing. One subtlety is whether the lower Borel includes \(H_i\) or \(H_i^{-1}\) in the comultiplication. In \(U_q\), \(\Delta(F_i)=F_i\otimes K_i^{-1}+1\otimes F_i\), or it might be \(F_i\otimes1+K_i^{-1}\otimes F_i\), depending on the pairing sign.

Now, thinking about the final aspects: The quotient by \(b_{ii}c_{ii}-1\) sends \(b_{ii}\mapsto c_{ii}^{-1}\). However, if \(c_{ii}=H_i\), then \(b_{ii}=H_i^{-1}\). 

The explicit quotient map from skein to \(U\) looks like this:

\[
b_{ij}\mapsto L^-_{ij}\in U,\quad c_{ij}\mapsto L^+_{ij}\in U,
\]

with \(L^-_{ii}=\hat K_i^{-1}\) and \(L^+_{ii}=\hat K_i\). Great!

## Reasoning

**Finalizing Quotient Map and Lemma Clarifications**

I need to clarify in my notes that "this quotient map is \(\Phi\) followed by \(\pi\)" and "the ideal is exactly generated by diagonal relations." I also want to make sure my final write-up doesn’t say "complete proof;" instead, I can say, "The cited PBW theorem..." 

I could include a note like, "For completeness, we spell out why the algebra in Lemma 2 is \(D\), not just the quotient," along with the PBW theorem details. Now, it's time to write the final version in raw LaTeX!

