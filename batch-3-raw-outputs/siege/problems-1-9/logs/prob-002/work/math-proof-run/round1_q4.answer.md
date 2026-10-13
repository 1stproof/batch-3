# round1_q4: M-estimation plus conditional stability

## 1. Isotropic stability estimate (proved for the model field V = x/d; sketched for general V)

Notation: h = f1 - f2, w = u_{f1} - u_{f2}, and V = grad u_{f2}. The exact identity
div(f1 grad w) = -div(h V) (from div(f_i grad u_i) = 1) gives the transport equation
div(hV) = G, where G := -div(f1 grad w).

**Lemma 1 (V = x/d).** For V = x/d the equation reads (x.grad h + d h)/d = G. The bounded solution is
h(x) = d ∫_0^1 t^{d-1} G(tx) dt, and ||h||_{L^2(D)} ≤ 2 ||G||_{L^2(D)}.

*Proof.* The function H(t) = t^d h(tx) satisfies d/dt H = t^{d-1}(x.grad h + d h)(tx) = d t^{d-1} G(tx). Integrating from 0 to 1 gives the formula. For the bound, apply Minkowski's integral inequality together with ||G(t·)||_{L^2(D)} ≤ t^{-d/2}||G||_{L^2(D)}. This gives ||h|| ≤ d ∫_0^1 t^{d/2-1} dt ||G|| = 2||G||. ∎

**Sketch (general V, r small).** V = grad u_{f2} is a C^α-small perturbation of x/d. It has a single hyperbolic source near 0 and div V ≥ c > 0. The characteristic formula carries over with the flow map; the Jacobian factors stay comparable to the model ones, so ||h||_2 ≤ C||G||_2. I have not written this out in full.

**Consequence.** Since G = -div(f1 grad w) and f1 ∈ C^α, α > 1, we get
||f1 - f2||_{L^2} ≤ C ||u_{f1} - u_{f2}||_{H^2}.

## 2. What least squares plus isotropic interpolation gives (proved modulo standard facts)

The step below uses standard facts recalled from memory: entropy bounds for Hölder balls, and the rate of the least-squares estimator in the white-noise model.

1. The class {u_f} lies in a bounded set of C^{α+1}, so its L^2 metric entropy is ≲ ε^{-d/(α+1)}.
2. The least-squares estimator therefore satisfies E||u_{f̂} - u_f||_2^2 ≲ n^{-2(α+1)/(2α+2+d)}.
3. Interpolation between L^2 and H^{α+1}, with the H^{α+1} norm bounded, gives ||w||_{H^2} ≲ ||w||_2^{(α-1)/(α+1)}.
4. Combining these: E||f̂ - f||_2^2 ≲ n^{-2(α-1)/(2α+d+2)}.

This rate is strictly slower than the conjectured n^{-2α/(2α+d+3)}. Cross-multiplying, (α-1)(2α+d+3) - α(2α+d+2) = -(α+d+3) < 0. So **plain isotropic M-estimation plus stability loses**. The loss comes from charging two full derivatives of w in every direction.

## 3. Anisotropic fix (heuristic, not proved)

In Lemma 1, h is a radial integral of G. Integrating along rays gains one derivative in the radial direction only. Formally this gives
||h||_2 ≲ ||G||_{H^{-1}_{rad} L^2_{ang}} ≲ ||w||_{(radial order 1, angular order 2)}.

That is, two derivatives are needed only across the flow, one along it. This matches the planner's symbol σ(ξ) ~ (1+|ξ_rad|)/|ξ|^2.

An anisotropic interpolation of this norm between L^2 and the a priori bound should replace the effective ill-posedness degree 2 by "2 across, 1 along". Under the heuristic spectral count (variance ~ n^{-1}2^{J(d+3)}, bias^2 ~ 2^{-2Jα}), this gives n^{-2α/(2α+d+3)}.

I have not proved that a global M-estimator attains this rate. The obstacle is that its prediction-error analysis is isotropic. I propose a two-step estimator instead:
1. Take a pilot plug-in estimate f̃.
2. Apply a flow-adapted spectral or wavelet regularisation of the linearised problem at f̃, with angular resolution 2^J and radial resolution 2^J, and n 2^{-J(2α+d+3)} ~ 1.

## Summary

- **Proved:** the L^2–H^2 stability estimate for the model field V = x/d (Lemma 1), and the conclusion that least squares plus isotropic interpolation achieves only n^{-2(α-1)/(2α+d+2)}, which is strictly slower than the conjectured rate. This second point depends on the general-V stability bound, which is only sketched, and on standard entropy and least-squares facts cited from memory.
- **Sketched:** the stability estimate for general V with r small.
- **Open:** a rigorous anisotropic stability estimate plus interpolation, and an estimator that provably attains the conjectured minimax rate n^{-2α/(2α+d+3)} (up to log factors).

=== END OF ANSWER round1_q4 ===
