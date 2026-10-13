# round12_q3 — attempt on MS11♭

Plan/status: (1) read the spliced material on the chain (round11_q9 §§2,5) and the
planner's Mechanism G; (2) try to prove MS11♭ via (1L_X) / lift-curve stabilisers;
(3) if not possible, check the chain and record precisely what is and is not proved.
Statement being attempted: MS11♭ exactly as in the task file.

**Outcome: MS11♭ is NOT proved here and no counterexample is given.** What follows is a
partial result on the planner's Mechanism G, item 4: the claimed "2-dimensional analogue of
Lemma D3". It holds exactly when the t = 0 fibre of X is generically reduced along S. When
that fails it is false, already in a local model, and I identify the global meaning of the
failure. I did not re-check the chain beyond what is used here.

## 1. Setting
- X is an irreducible component of the germ of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) at (0,0) with
  X ⊃ S × {0}.
- g ∈ Aut(Q) acts on B × Δ_ε by g × id, and gX = X.
- X_0 := X ∩ {t = 0}, with its scheme structure, i.e. with ideal I_X + (t).
- dim X = 3. Indeed every fibre of closure 𝒱 over Δ has dimension 2, so no 3-dimensional
  component lies in {t = 0}. Hence t ≢ 0 on X, and S is an irreducible component of X_0.

## 2. Lemma G1 (proved)
Assume g fixes S × {0} pointwise. Then at least one of the following holds:
- (a) g acts as the identity on X. Then g fixes every lift-curve in X (in fact every point of X).
- (b) The scheme X_0 is non-reduced at every point of a dense open subset of S. Moreover
  Fix(g) ∩ X is a proper analytic subset of X; it contains S × {0} and has dimension 2. So
  for small t ≠ 0, the generic point of X_t is not fixed by g.

*Proof.* Suppose X_0 is reduced at some point p of S that is a smooth point of S and lies on
no other component of X_0. Such points form a dense open subset of S as soon as one of them
exists. Then O_{X,p}/(t) = O_{S,p} is regular of dimension 2, and t lies in the maximal ideal.
So the embedding dimension of O_{X,p} is at most 3 = dim O_{X,p}, and X is smooth at p with
local coordinates (s_1, s_2, t), where s_1, s_2 restrict to coordinates on S.

Now g fixes p and preserves X, so g is a finite-order automorphism of the smooth germ (X,p).
- By Cartan's linearisation (cited from memory), g is conjugate to its linear part dg_p.
- dg_p is the identity on T_pS, because g fixes S pointwise.
- dt_p ∘ dg_p = dt_p, because t ∘ g = t. Since T_pS = ker dt_p, dg_p induces the identity on
  T_pX / T_pS.
- So dg_p is unipotent and of finite order, hence the identity, and g = id near p.

The set {x ∈ X : gx = x} is analytic and contains a nonempty open subset of X_reg. The regular
locus of an irreducible germ (on a suitable representative) is connected, so this set is all
of X. That is (a).

So if g ≠ id on X, no such p exists, i.e. X_0 is non-reduced at generic points of S. In that
case Fix(g) ∩ X is a proper analytic subset of the irreducible 3-fold X,
so it has dimension ≤ 2, and it contains S × {0}. ∎

(The two cases can overlap only formally: (a) can hold with X_0 non-reduced. The content is
that "g ≠ id on X" forces non-reducedness along S.)

## 3. Global meaning of case (b)
If g fixes S pointwise, then g lies in the automorphism group of the curve at a generic point
of S, i.e. g is a generic automorphism of the curves of V_0 near Q. Case (b) says that V_t
(t ≠ 0) leaves the locus of curves admitting g. Concretely:
- If 𝒱 is read as an orbifold submanifold whose chart preimages are smooth with φ submersive,
  case (b) is impossible at generic interior points, since there X is smooth with t a
  coordinate. So under that (orbifold) reading, every g ∈ G_X fixing S pointwise fixes every
  lift-curve in X.
- Under the coarse reading (R2) adopted by the run, case (b) can occur. Example: coarse M_3
  is smooth along the hyperelliptic divisor, where the hyperelliptic involution ι acts on the
  1-dimensional normal direction by z ↦ −z, with coarse coordinate y = z². A family 𝒱 that is
  smooth in the coarse space, with V_0 inside the hyperelliptic locus and V_t = {y = t}, has
  chart preimage {z² = t}, which is non-reduced at t = 0. I have not checked whether a totally
  geodesic V_0 can actually sit in such a locus.

## 4. Local model: case (b) can exchange lift-curves
Work in chart coordinates (u, w, z, …), with g: z ↦ −z (other coordinates fixed), and let
X = {z² = t·u} (× fixed other coordinates).
- X is irreducible. Its fibre X_0 = {z² = 0} is the double plane S = {z = 0}, and g fixes S
  pointwise.
- X/g = {Z = t u}, with Z = z², is a smooth graph, so the coarse family is smoothly trivial
  near here.
- L_0 = {u = t, w = 0, z = t} and gL_0 = {u = t, w = 0, z = −t} both lie in X, are distinct,
  and have the same image Q_t in the quotient. So both are lift-curves.

Hence the planner's local evidence for item 4 is incomplete. The "t = b²" model has a single
lift-curve, but this variant of it has two lift-curves exchanged by an element fixing S
pointwise. So (1L_X) cannot be derived from item 4 by local arguments alone, consistent with
the run's general finding that MS11♭ needs global input. The global input that would close
this sub-case is "V_t keeps the generic automorphisms of V_0", which is not available under (R2).

## 5. Status
- **Proved:** Lemma G1, i.e. elements g ∈ G_X fixing S pointwise act trivially on X (hence on
  all lift-curves) unless X_0 is non-reduced along S. That non-reduced case happens only if
  V_t loses a generic automorphism of the curves of V_0. Under the orbifold reading of
  "submanifold 𝒱" it never happens.
- **Shown (local model):** under (R2) the non-reduced case can exchange two lift-curves, so
  item 4 of the planner's sketch is false as a local statement.
- **Not addressed:** the elements g ∈ G_X acting on S as non-trivial (anti-)reflections; second
  components gX ≠ X meeting X along a lift-curve; whether the exchanged lift-curves actually
  carry different persistence sets (and so violate MS11♭); the chain check.
- **Open:** MS11♭ itself; (Rig).

=== END OF ANSWER round12_q3 ===

