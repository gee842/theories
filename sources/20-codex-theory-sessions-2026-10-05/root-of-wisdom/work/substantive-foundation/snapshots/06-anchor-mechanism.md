# A wrong dynamics anchor can stabilize the wrong physical zero

Post-evaluation analytic explanation, 5 October 2026. No frozen algorithm, parameter or result was changed. The exact calculations below explain a possible mechanism; they are not a new fitted model or a proof of finite-horizon convergence of every filter run.

## Exact change of coordinates and the required signs

Let the true system be

\[
x_{t+1}=a x_t+u_t+g+w_t,\qquad
y_t=x_t+b_t+\epsilon_t,\qquad z_t=x_t+d+\eta_t,
\]

where g is constant and a!=1. Define r=g/(1-a), and write

\[
\widetilde x=x-r,\qquad \widetilde b=b+r,\qquad
\widetilde d=d+r.
\]

The bias signs are **plus**: y=(x-r)+(b+r)+epsilon. Using minus r for both transformed state and transformed bias would not preserve the observation.

In these coordinates,

\[
\widetilde x_{t+1}=a\widetilde x_t+u_t+w_t,\qquad
y_t=\widetilde x_t+\widetilde b_t+\epsilon_t,\qquad
z_t=\widetilde x_t+\widetilde d+\eta_t.
\]

These are exactly the transition and observation equations of the filter that assumes g=0 while allowing both sensor biases to vary in its state space. This is the previous shift transformation with c=-r. If b changes, adding the same constant r preserves its change increments, although its transformed sign-reversal values are no longer centered on zero.

The relative bias is preserved:

\[
\widetilde b-\widetilde d=b-d.
\]

Thus an estimator can represent relative sensor discrepancy correctly while representing the absolute physical state with the wrong origin.

## Conditional control equilibrium

Suppose the estimator tracks this transformed coordinate exactly, and clipping is inactive. With the study's common controller u=-k*x_hat, taking x_hat=tilde x gives

\[
\widetilde x_{t+1}=(a-k)\widetilde x_t+w_t.
\]

In the noiseless case, |a-k|<1 implies tilde x tends to zero. Hence

\[
x^*=r=\frac{g}{1-a},\qquad u^*=0.
\]

For a=.8, k=.5 and g=+/-.15, the physical equilibrium is x*=+/-.75, even though the estimated coordinate approaches zero. The estimator need not openly revise its zero-forcing assumption: it can absorb the discrepancy into both inferred sensor biases.

This equilibrium is also the true system's passive equilibrium under u=0. The controller stabilizes deviations around that location; it need not create the entire displacement. The precise failure is regulating a shifted coordinate instead of the supplied absolute target x=0.

At this equilibrium, squared-state loss is .75^2=.5625 per step. Sixty steps *already at equilibrium* give 33.75. This is a scale comparison, not the exact expected loss of an episode starting with the study's initial prior. Under the idealized noiseless perfect-coordinate controller,

\[
x_t=r+(a-k)^t(x_0-r).
\]

For x_0 with mean zero and variance one, the exact expected state loss over t=1,...,60 is

\[
60r^2-2r^2\sum_{t=1}^{60}(a-k)^t
+(r^2+1)\sum_{t=1}^{60}(a-k)^{2t}.
\]

At these parameters it is approximately 33.4224, before process noise, imperfect filtering or clipping. The evaluated filter's observed state losses around 30 need not equal either figure: its estimate begins at the declared prior and acquires the coordinate shift over time.

## Contrast with retained scalar reference correction

For constant b and d, a noiseless converged scalar update based on y-z learns h=b-d. Its state estimate becomes

\[
x_{hat}=y-h=x+d.
\]

The same unsaturated proportional controller then gives

\[
x_{t+1}=(a-k)x_t+g-kd,
\qquad x^*=\frac{g-kd}{1-a+k}.
\]

With a=.8 and k=.5, the denominator is .7. If d=0 and g=+/-.15, the equilibrium is +/-.214286. With g=.15 and d=.25 it is .035714; with g=.15 and d=-.25 it is .392857. Reference bias and forcing can partially cancel or reinforce one another. A lower state cost in a particular sign combination does not establish more accurate understanding.

These are converged constant-regime formulas. Six noisy references, a changing bias, adaptive gains and finite time need not produce a fully converged h. They explain a baseline mechanism rather than predict every scalar-policy result.

## What the finite priors allow—and what they do not

The simulation has a fixed x_0~N(0,1) generating prior. The transformed initial state instead has distribution N(-r,1). Also, the filter's supplied zero-centered priors for b and d are not the generating priors shifted by r. Therefore the full finite-episode probability model is **not** exactly invariant under this transformation while keeping those priors fixed.

The code uses soft Gaussian priors with positive variance, not exact constraints fixing x_0 or a sensor bias. Shifted latent values remain possible under its assumed model, with different prior weights. Its transition/measurement equations can consequently fit data in the shifted coordinate, but the prior affects the transient and finite-horizon result. No claim that its posterior must converge to that coordinate is proved here; proving that for this time-varying filter would require a separate analysis.

The actual three-state filter also supplies a random-walk bias variance and observation/process noise, while g is omitted entirely. Its posterior covariance is conditional on those assumptions. A small reported covariance does not account for uncertainty about an excluded forcing term. Observational consistency inside that model can coexist with a large error against the evaluator's absolute state.

An exactly known initial state, a truly known unbiased reference, or a correct model for g can supply information against the shifted interpretation. A fixed known initial distribution can provide a statistical anchor across episodes, but does not give the exact initial state from one noisy run. The stochastic factorial experiment is not the unrestricted shift-closed class used in the earlier impossibility argument.

## Connection to the saved results

In the saved constant-bias worlds with nonzero forcing, the anchor filter's mean squared-state episode losses are 30.0827 for d=0 and 30.1372 for nonzero d. Their nominal 90% coverage rates are approximately 2.57% and 2.47%. The g=0 counterparts have state losses .5240 and .5892 and coverage approximately 91.10% and 90.24%. These figures are read from the existing evaluation summary; they are descriptive benchmark results, not new primary contrasts.

The exact shifted-coordinate construction explains why allowing the reference bias to be inferred does not guarantee a better physical anchor when the dynamics are fixed incorrectly. Protected references can all arrive, and relative sensor calibration can remain useful, while the model and controller agree on the wrong absolute zero. The evidence supports this mechanism as an interpretation of the observed failure; exact per-run convergence or exclusive causal attribution would require further testing.
