# Mathematical and statistical audit of integrated report

5 October 2026. Read-only review of `outputs/scientific-principles-investigation.md`, initial version with closure paragraph at line 135 and sequential discussion at line 185. Numbers were not rechecked in this pass; earlier independent verification is retained in `root-audit.md`. The report itself was not modified by this reviewer.

## Corrections to make

1. **Random commitment time in the closure theorem (line 135).** As written, the event W can include entry into permanent error at different, unbounded random times. Therefore the finite-time bound is not necessarily P(error at t) ≥ P(W). Let τ be entry time, with τ finite on W. The correct bound is

   \[
   P(\mathrm{error}_t)\ge P(W\cap\{\tau\le t\}),\qquad
   \liminf_{t\to\infty}P(\mathrm{error}_t)\ge P(W)>0.
   \]

   This still rules out vanishing error. Alternatively, explicitly require that permanent wrong commitment occurs by one common fixed time t₀ on W; then P(error at t) ≥ P(W) for every t≥t₀ is correct. Keep the target fixed and error asserted permanently, as already specified. A counterexample to the current finite-time wording is a random τ with unbounded support and an investigator correct until τ: early error probability is smaller than P(W), though its limiting lower bound is unchanged.

2. **Equality of observational kernels under adaptive actions (line 97).** Replace the broad sentence about every reachable action having the same observation kernel with: “If the initial transcript laws agree and, at each common history and permitted action, the conditional law of the complete next accessible transcript agrees in both worlds, induction shows that adaptive action selection cannot distinguish them.” Include resource and action-availability cues where these are observable. Equality of the state-conditional emission kernels Oθ alone is insufficient if state-transition kernels Kθ differ: identical sensors can observe different state trajectories. The intended transcript theorem and the D(B,d) necessary condition are otherwise correct.

3. **Incorrect Howard DOI (line 185).** The link `https://doi.org/10.1214/18-AOS1804` names Bertsimas and Van Parys, *Sparse high-dimensional regression: Exact scalable algorithms and phase transitions*, not Howard et al. Replace it with `https://doi.org/10.1214/18-PS321` for Howard, Ramdas, McAuliffe and Sekhon (2020), *Time-uniform Chernoff bounds via nonnegative supermartingales*. The inspected primary author version is `https://arxiv.org/pdf/1808.03204v7`. The mismatch was verified against the publisher's complete issue and the MIT author manuscript, not inferred from the DOI string.

## Small clarity improvements

- At line 185 define Kₙ as the number of heads among the first n tosses and use math notation `E_n=(1.5)^{K_n}(0.5)^{n-K_n}`. The current Unicode superscripts visually suggest K raised to n, making a correct martingale harder to parse.
- At line 23 replace “expected squared probability error” with “expected Brier loss for a binary outcome.” The later proof correctly minimizes squared forecast-versus-outcome error, not an unspecified squared distance to an unknown true probability.
- The likelihood adversity statement is correct, including the common-positive-support qualification. For maximal clarity one optional sentence can say: “Without common support, an event adverse to a model need not have positive probability under that model.” No substantive correction is needed here.

## Checked interpretations that do not need correction

- The finite-space total variation inequality, equal-prior optimum and resource-feasible supremum bound are correct. The report rightly states that satisfying the scalar lower bound need not achieve a requested separate pair of errors. This also avoids assuming the supremum is attained.
- Likelihood adversity uses fixed normalized mass functions and event/complement reasoning; it does not misstate a probability-zero continuous point as logical contradiction. Both models may be misspecified.
- The Brier identity and calibration counterexample are correct. Aggregate calibration can coexist with unexploited subgroup predictability. No claim is made that proper scoring alone establishes empirical calibration.
- The sequential rules are correctly interpreted under the simple iid fair-coin null. Deterministic alpha spending uses valid fixed-prefix p-values and needs no independence among the tests. The likelihood ratio is a null martingale; stopping at the threshold or a finite horizon and taking an increasing-horizon limit gives an anytime bound. No composite-null claim is needed.
- Conditional independence in the repeated-check model and its shared-failure mixture are explicit. The report correctly distinguishes an error-conditional miss probability from posterior correctness.
- The free-information argument explicitly excludes resource costs and system changes when asserting weak improvement, then acknowledges them when discussing disclosure in practice.
- The stronger simulated laboratory study is appropriately labeled prospective and unrun. Its predictions do not treat a violation of the mathematical theorem as an ordinary empirical falsification of the theorem.

**Disposition:** two local mathematical qualifications and one citation replacement are required; no changes to validated numerical results or the report's central conditional conclusion are needed.
