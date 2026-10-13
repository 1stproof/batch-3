# Answer to round3_q3

## Status
- **Checked by hand:** the Step 0 normal form (f_t(0)=∞, f_t(∞)=1, f_t(1)=t, f_t(t)=0; at t=1/4: β=−11/12, γ=1/6, c_2=4/11, v=−25/96), and V_t(t)=v(t).
- **Proved, given Step 1:** the topological criterion (Steps 2–3) and its use for the twist T_γ (Step 4).
- **Not proved, only numerically supported (planner's numerics, which I have not re-checked):** that the explicit arc α=V_{1/4}∘β is simple, and the description of where it crosses the real axis.
- **Not done:** parts (1) (that Ψ is a covering onto U) and (3) (the k=2 family) of the query. The argument below does not need them; they remain open.

## Setting and normal form
Write a_0=c_1 and a_{i+1}=f(a_i). Normalize a_0=0, a_1=∞, a_2=1, a_3=t. Then
f_t(z)=1+β/z+γ/z², with β=(t²+t−1)/(1−t) and γ=t(1−2t)/(1−t).

Check:
- f_t has a double pole at 0, so c_1=0 is critical and f(a_0)=∞=a_1.
- f(∞)=1=a_2.
- f(1)=1+β+γ=1+(t−1)=t=a_3, because β+γ=−(1−t)²/(1−t)=t−1.
- f(t)=0=a_0, because t²+βt+γ=[t²(1−t)+t³+t²−t+t−2t²]/(1−t)=0.

At t=1/4: β=−11/12, γ=1/6, c_2=−2γ/β=4/11, and v=1−121/48+121/96=−25/96. On the real line the order is v<a_0=0<a_3=1/4<a_2=1, with a_1=∞.

## Step 1 (fibre model)
This step is taken from the planner and not re-derived here. Fix t, so the configuration A is (0,∞,1,t), and let the fifth point be v'. Then the pulled-back modulus of A is w, where
v' = V_t(w) = −((w−1)²−t)² / (4w(w−1)(w+t−1)).

- At w=t this gives −(t²−3t+1)²/D, with D=4t(1−2t)(1−t). This equals v(t), which I checked.
- The fibre of V_t over a_1=∞ is {0,1,∞,1−t}, and all four points are simple.
- Consequence: w≠1−t whenever v'≠a_1. So Ψ=(i_*,f^*) never meets the graphs Γ_g={(p,g(p))}, for g∈Γ(2)S, which lie over {q=1−t}.

## Step 2–3 (criterion), proved
Let g∈Γ(2)S be non-elliptic, i.e. it has no fixed point in H. Then Γ_g∩Δ=∅.

The space X_g=(H×H)∖Γ_g is homotopy equivalent to a circle, so H_1(X_g)=Z. The generator is a fibre loop around g(p), and the diagonal Δ≅H is contractible inside X_g.

Let T∈ker(i) satisfy f^*∘T=f^*. Then Ψ∘T=Ψ, so T preserves D_f=Ψ^{-1}(Δ). Suppose T^m fixes the component D_0 of D_f through τ, with m≠0.
1. Choose a path σ⊂D_0 from τ to T^mτ. Then Ψσ is a loop in Δ, so it is null-homologous in X_g.
2. Choose a path σ' in the fibre i_*^{-1}(p_0) with the same endpoints. Teich(B) is contractible, so σ≃σ' rel endpoints.
3. Ψ(Teich B)⊂X_g, so Ψσ and Ψσ' have the same class in H_1(X_g).
4. Ψσ' is a fibre loop. If it winds ±m times around g(p_0), this contradicts step 1.

So the ⟨T⟩-orbit of D_0 is infinite.

## Step 4 (the curve)
Fibre loop: let T be the point-push of v around the lasso α·(circle around a_1)·α^{-1}, where α is an arc from v to a_1. Then T=T_γ^{±1}, where γ=∂N(α) is the curve enclosing exactly {v,a_1}.

Lift α from w=t_0 to an arc β. If β ends at w=1−t_0, then the lasso lifts to a closed loop β·(circle around 1−t_0)·β^{-1}. This loop avoids 0, 1 and ∞, so it lifts through λ to a closed loop in H winding once around q*=g(p_0). Hence:
- **T preserves D_f.** f^*∘T=f^* on the fibre. The lift T~ fixes a point of Teich(A), and pure mapping classes act freely there, so T~ is trivial.
- **The orbit is infinite.** T^m winds m times around q*, so Step 3 applies as soon as g is not elliptic.

Choice at t_0=1/4: take β to be a loop around w=0 based at 1/4, followed by the segment [1/4,3/4].
- The loop around 0 lifts to a translation by ±2.
- The segment lifts along the imaginary axis to S(p_0).
- So g=τ↦±2−1/τ, which has trace ±2. It is parabolic, not elliptic, so the orbit is infinite.
- For contrast, the bare segment gives g=S, which is elliptic. That is the cusp curve at t=1/2, and its twist stabilizes a component.

An explicit β:
1. the lower half of |w|=1/4, from 1/4 to −1/4;
2. the upper half of |w−5/32|=13/32, from −1/4 to 9/16;
3. the lower half of |w−21/32|=3/32, from 9/16 to 3/4.

## Answer (for f=f_{1/4})
γ is the boundary of a thin regular neighbourhood of the arc α from v=−25/96 to a_1=f(c_1)=∞. The arc α:
1. starts at v and runs in the lower half-plane;
2. crosses the real axis upward in (a_2,a_1)=(1,∞);
3. runs in the upper half-plane and crosses downward in (a_0,a_3)=(0,1/4);
4. crosses upward in (v,a_0);
5. stays in the upper half-plane and goes to ∞.

So γ separates {v,a_1} from {a_0,a_2,a_3}. The twist T_γ itself (power 1) preserves D_f, and the ⟨T_γ⟩-orbit of the component through the base point is infinite. The proof of this is complete, apart from Step 1, which is the planner's computation, and the numerically supported claim that α is simple.

Open: rigorous simplicity of α, part (1) (the covering-map structure of Ψ), and part (3) (the k=2 family).

=== END OF ANSWER round3_q3 ===
