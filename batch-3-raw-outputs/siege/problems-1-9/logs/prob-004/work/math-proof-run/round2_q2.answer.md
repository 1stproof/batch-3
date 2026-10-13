# round2_q2: dim 4 (proved, modulo cited TMZ) and dim 6 (reduced to one relative lemma; partial)

Conventions as in the task file. Cited from memory: TMZ regularization theorem (as stated in Result 3 of the task file; hypothesis: D is an SC divisor with positive strata — this is the convention assumed). Also: every almost complex structure on a surface is integrable; a d-bar operator on a complex line bundle over a Riemann surface is integrable (local holomorphic frames exist, because one can locally solve the scalar equation d-bar f = alpha). On a surface, the orientation-compatible complex structures form a contractible space, and each of them is tame for any area form of that orientation.

## (a) dim_R M = 4: YES

**Step 0.** Apply TMZ. This is a permitted deformation. Afterwards omega admits a regularization (rho, nabla, Psi_I) for every I. The strata are: the surfaces D_i, and finite sets of crossing points D_ij, i ≠ j (there are no triple points when n = 2, since by transversality D_ijk is empty).

**Structure near a crossing point p in D_ij.** By TMZ condition 3 with I = {i} and I' = {i,j}: near p, the Hermitian structure (rho_i, nabla_i) on N_{D_i}|_{D_i} is pulled back from the single fibre N_{D_i}|_p by the projection of the model. In the fibre coordinate z_j of N_{D_j}|_p, which is a local coordinate on D_i near p, this means two things: there is a frame s_i of N_{D_i} that is constant (unit length) with nabla_i s_i = 0, and rho_i is constant. Moreover Psi_{ij}^* omega = omega_std on C^2 with coordinates (z_i, z_j), and D_i = {z_i = 0}, D_j = {z_j = 0}.

**Step 1 (complex structure on D_i).** Pick a complex structure j_i on D_i such that j_i is the standard structure (z_j holomorphic) near every crossing point p in D_i. Such a j_i exists because the space is contractible, so a relative extension is possible. Positivity at p ensures that the orientation of z_j agrees with the omega-orientation of D_i. Then j_i is omega|_{D_i}-tame.

**Step 2 (holomorphic structure and Chern connection).** Let dbar_i := nabla_i^{0,1} with respect to j_i. This is integrable, so N_{D_i} becomes a holomorphic line bundle, and near each p the frame s_i is holomorphic. Let nabla_i' be the Chern connection of (dbar_i, rho_i). In a holomorphic frame s with h = |s|^2 it has connection form theta = ∂ log h, which is of type (1,0). Both connections are rho_i-unitary, so nabla_i' = nabla_i + i·beta_i with beta_i a real 1-form. Near p, h is constant in the frame s_i, so nabla_i' s_i = 0 = nabla_i s_i. Hence beta_i vanishes near every crossing point.

**Step 3 (changing the connection).** Apply Lemma C in the chart Psi_i, with K a neighbourhood of D_i ∩ (union of the other D_j). This is a permitted deformation: it is exact, it keeps D SC, and it is supported in the region where beta_i ≠ 0, away from the charts Psi_ij. Afterwards Psi_i^* omega = omega_{(rho_i, nabla_i')} near D_i, and the Psi_ij are unchanged. Do this for each i (the supports are disjoint).

**Step 4 (J near D).** On Psi_i(nbhd) put J_i := J_{nabla_i'} built from j_i (Lemma A).
- *Consistency at crossings.* Near p, Psi_i agrees with Psi_ij (TMZ condition 3). In those coordinates the base is (z_j, standard j_i) and the connection is trivial in the constant frame, so J_i = standard i on C^2. The same holds for J_j. Shrink the tubes so that Psi_i(U_i) ∩ Psi_j(U_j) lies inside the Psi_ij-chart region where both structures are standard. Then the J_i glue to a structure J on a neighbourhood U of D.
- *Tameness.* By Lemma B, J is tame near each D_i. Near p, J is standard and omega is standard, so J is tame there too.
- *Extension.* The space of omega-tame structures at a point is contractible (nonempty and convex-like, a fibre bundle with contractible fibres). So J restricted to a smaller closed neighbourhood extends to an omega-tame J on M.

**Step 5 (coordinates).**
- *Near p in D_ij:* (z_i, z_j) are standard holomorphic, and D = {z_i z_j = 0}. Here r = 2.
- *Near q in D_i, away from crossings:* take a j_i-holomorphic coordinate w on D_i and a holomorphic frame, with fibre coordinate z_1. By Lemma A, z_1 is J-holomorphic because theta is (1,0), and pi^*w is J-holomorphic. Then (z_1, pi^*w) are coordinates, D = {z_1 = 0}, and r = 1.
- *Away from D:* r = 0, with any smooth coordinates.

This proves YES in dimension 4. ∎

## (b) dim_R M = 6: reduction and partial proof

**Strata.** The D_i are 4-manifolds, the D_ij are surfaces, and the D_ijk are points.

**Reduction (proved by the same scheme as (a)).** YES follows from the data below. In it, each structure that is "pulled back" is pulled back via the TMZ model projections, and the D_ij-level data are shared by D_i and D_j.
- (i) Complex structures j_ij on the curves D_ij, standard near triple points.
- (ii) Holomorphic structures S_k^{ij} on N_{D_k}|_{D_ij}, for k in {i,j}, flat near triple points. These exist by the argument of (a), Steps 1–2.
- (iii) For each i, an omega_{D_i}-tame J_i on D_i that equals J_nabla built from (j_ij, Chern connections of S^{ij}) near each D_ij. Here D_ij is J_i-holomorphic with holomorphic normal coordinate. In addition, a J_i-holomorphic structure on N_{D_i}|_{D_i} which, near D_ij, is the pullback of S_i^{ij}.

Given (i)–(iii), the remaining steps are as in (a):
- Do the Chern-connection changes by Lemma C, deepest stratum first. Changes near D_ij are made on N_{D_i}|_{D_ij} as part of the I = {i,j} regularization, and they are pulled back. TMZ condition 3 is preserved because every new connection equals the pulled-back one near deeper strata.
- Then glue J_{nabla} on the tubes, check tameness with Lemma B, extend, and read off the coordinates (fibre coordinates of the models).

I have checked this reduction only at the level of detail above. The consistency claim, that the Lemma C changes for I = {i} and I = {i,j} stay compatible, is the planner's snag (ii). It holds because the I = {i} change is made with beta supported away from D_ij (both connections agree there, by (iii)).

**The relative line bundle lemma, (iii).** This is the hard step, and it is open in this answer. Here is the route, with its gap marked.
- Suppose there are closed symplectic hypersurfaces P_i^+, P_i^- in M such that C = D ∪ {P^±} is an SC divisor with positive strata, PD[D_i] = PD[P_i^+] − PD[P_i^-], and the P's do not meet the triple points.
- Then apply TMZ to C, and fix a global smooth isomorphism Phi_i: O(D_i) ≅ O(P_i^+) ⊗ O(P_i^-)^{-1} on M. Homotope it near each stratum to be pulled back along the tubular retractions; this is possible because maps to C* deform along retractions.
- Choose S_i^{ij} to be the divisor structure of the points (P_i^+ − P_i^-) ∩ D_ij on the curve D_ij, transported by Phi_i. This makes the structure coincide from the D_i side and the D_j side, since both are restrictions of the same global object.
- On D_i, let E^± = P_i^± ∩ D_i, which are symplectic surfaces. By the regularization of C they are fibres of the D_ij-tube near D_ij. Build J_i by J_nabla near D_ij and near E^± and near E^+ ∩ E^-, then extend tamely. The divisor cocycle of E^+ − E^- is then J_i-holomorphic, and near D_ij it equals the pullback of S_i^{ij}. This gives (iii).

**Gap (unproved).** The existence of the configuration P^±, i.e. Donaldson–Auroux hypersurfaces in classes k[omega'] + PD[D_i] and k[omega'] for a nearby rational omega', transverse to all strata, with all new strata symplectic and positive for omega. I believe this follows from Auroux's asymptotically holomorphic transversality relative to approximately holomorphic submanifolds, but I have not verified the precise statements (snag (iv)), nor the integrality bookkeeping after the deformation to a rational form.

## Summary
- Proved: YES for dim_R M = 4 (given TMZ, cited from memory).
- Proved: in dim_R M = 6, YES reduces to the relative line bundle lemma (iii). That lemma in turn follows from the existence of the Donaldson–Auroux partner configuration.
- Open: the existence of that partner configuration, with positivity of all new strata; general dimension.

=== END OF ANSWER round2_q2 ===
