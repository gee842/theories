# V7 mathematics changes

Completed in the five assigned source files only: `src/core/20_s2.md`, `30_s3.md`, `src/supp/00_S0.md`, `02_S2.md`, `03_S3.md`. No edits to V6.2. Stable result and equation keys are unchanged.

## Changes made

- **`standprice`:** explicitly a deterministic-share result. A general nonlinear prize needs finite nearby discounted winnings and uniformly negligible discounted difference-quotient tails. S3 defines the condition, proves why it permits differentiation of the infinite sum, and retains the quadratic-prize counterexample showing that a stationary Jacobian and both gains below one do not suffice.
- **Preserved cases:** fixed-prize values on their finite-price domain; the proportional-prize one-stock ratio model. S3 explains that the latter reduces to bounded normalized winnings with effective discount `delta*Lambda_com`, whose product with the relative multiplier is `delta*Lambda_rel`. The local/common comparison and instability threshold remain unchanged. Strict forward-looking comparison now explicitly uses `0<delta<1`; the myopic case stays in the scope paragraph.
- **`loopgain` / `eqgain`:** deterministic local price, linearized expected-deviation calculation and finite-jump lottery premium are distinct throughout §§2–3 and S0–S3. The deterministic strategic price now expressly assumes differentiable continuation value, nonnegative private derivatives and its finite-gain domain, matching its proof. No claim that the lottery's approximation boundary is `Gamma_eq=1` remains. Small-jump comparisons remain numerical, and the exact fixed-opponent equality is limited to the specified linear-strength lottery.
- **Strategic working objectives:** S3 no longer infers a working-objective derivative from a finite winner–loser lottery premium. Full strategic continuation payoffs need their own common/relative derivatives; a fixed prize eliminates common prize growth but need not eliminate equilibrium effort-cost or shared-loss changes. This interface remains open rather than silently identifying the objects.
- **Catch-up:** reversal of a win-share elasticity correction is distinguished from reversal of the total standing-price correction, since the added penalty itself values standing.
- **`onegroup`:** deleted the heterogeneous-background alternative and made the common background payoff explicit in the statement and proof. The scope retains the correct covariance formula. The following prose now says that the common benefit alone supplies no relative selective advantage.
- **S0:** V7 title, current `checks_v7.py` paths, provenance from Claude's V6.2 revised by Codex at Ren's direction, no human review. Historical V6.2 symbol changes remain historical. A6 is explicitly the field-model payoff convention, not an unstated restriction on the general prize.

## Propagation needed in root-owned files

The following are ready-to-use replacement texts for the affected cells/clauses, without requiring wholesale rewrites of historical entries.

### S13 interface table

For **Structural and equilibrium gain**, premise cell:

> A differentiable symmetric Markov equilibrium whose win share rises with each own stock; for the deterministic local price, differentiable continuation value, nonnegative private derivatives and the private finite-gain domain.

Its status cell:

> **Proved:** equilibrium win-share elasticity decides local stability. In the deterministic share model, the private elasticity gives the local price calculation under the additional premises of {{loopgain}}(4). **Numerical, held for outside review:** finite-jump lottery premiums, their amplification at parity, the laggard's falling price, and a winner-take-all fixed point beside the smooth one ({{eqgain}}) [num: MP]. Catch-up can reverse the win-share elasticity correction without reversing the total price correction. **Open:** which contests discourage or encourage catching up; whether the concentrated fixed point survives in the continuous-state game; a derivative-based objective reduction for the full strategic lottery.

For **Loop gain and working objectives**, premise cell:

> Deterministic shares; first order along a symmetric reference path with constant linearized coefficients; fixed opposing conduct; both gains below one; net payoff reinvested; finite nearby discounted winnings and the discounted-tail condition for nonlinear lifetime values.

Its status cell:

> **Proved** under those premises ({{standprice}}; {{growprize}}) [thm∣prem]. Fixed prizes and proportional-prize ratio models satisfy the tail condition on their stated finite-price domains. **Numerical:** the separate lottery premiums in the preceding row [num: MP]; the narrower working objective in the checked gross-reinvestment case [num: SP]. **Open:** the common and relative derivatives of full strategic continuation payoffs, including cost responses; the stochastic objective reduction; and general time-varying reference coefficients. Local gains alone do not certify nonlinear lifetime values.

### CLAIMS current-status cells

- `loopgain`: “Proved in the deterministic stock model; the lottery statement concerns the linearized expected deviation. The strategic local price requires deterministic shares, differentiable continuation value, nonnegative private derivatives and its finite-gain domain. Finite-jump lottery premiums are separate numerical results. Relative-shift derivative definition retained.”
- `standprice`: “Proved for deterministic shares under fixed opposing conduct, constant reference coefficients, both gains in [0,1), net reinvestment and the discounted-tail condition. Fixed-prize and proportional-prize ratio cases retained. A stationary nonlinear prize need not yield a finite continuation value despite both local gains being below one. Full strategic continuation reduction remains open.”
- `onegroup`: “Proved for carriers with a common background payoff. Total and within-group selection terms are nonpositive; the between-group term is nonpositive for affine fitness. Correlated background advantages can carry the trait and are outside that premise.”
- Any current open-interface summary should replace “the common return when rivals respond to a growing prize” with “the common and relative derivatives of full strategic continuation payoffs, including cost responses, and their stochastic objective reduction”. A fixed prize does not alone remove those cost effects.

### S14 and S15 verification registration

Suggested S14 row:

> `n=2`, `kappa=d=delta=1/2`, `r=1`, no sharing/provision/diffusion, `Omega(S)=S^2`: at stationary `S=1` the local gains are `1/3` and `2/3`, but any positive common perturbation gives infinite lifetime winnings | That constant reference coefficients and local gains below one guarantee nonlinear continuation derivatives | `standprice` | V7 mathematical regression.

Suggested S15 entry:

> `verification/math_checks.py`: independent standard-library Bellman iteration distinguishes nonlinear finite-jump value from the local expression, with two-grid convergence and a linear control; verifies the quadratic-prize escape bound; compares actual nonlinear proportional-prize trajectory derivatives with preserved closed forms; checks homogeneous versus correlated-background Price covariance.

The self-contained script exposes `run_checks()` and returns a JSON-serializable result. Root can import it from the V7 suite or run it separately; no dependency on V6.2 scripts or review folders. `verification/math-results.json` records the passing run.

### Other propagation worth retaining

- In TESTS Study 7 and any table using the catch-up numbers, call the reversed quantity the **win-share elasticity correction**, not the whole standing-price premium.
- Test Γ in the core and TESTS should retain its channel condition: provision lowers the gain in ratio channels, or more generally where decisiveness has level elasticity below one; diffusion lowers it in every reinforcing channel. Suggested replacement: “The ratio rises with diffusion and, in ratio channels or other channels whose decisiveness grows less than in proportion to the stock, with provision relative to the stakes, because those changes lower the discounted gain.”
- Do not overwrite historical review claims in the V6.2 changelog as though they were originally correct; record these as V7 corrections.

## Verification

`python3 verification/math_checks.py` passed. Nonlinear lottery premium: 1.03110642 on 1,000 cells and 1.03111035 on 2,000, versus 1.08178439 locally; linear control agrees. Proportional-prize nonlinear trajectory derivatives agree with formulas for `r=.7,1,1.5`, preserving both narrowing and widening. The quadratic-prize and background-covariance counterexamples reproduce.
