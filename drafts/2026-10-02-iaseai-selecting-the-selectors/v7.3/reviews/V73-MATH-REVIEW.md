# V7.3 adversarial mathematical review

Reviewer: fresh internal mathematical reviewer, separate from the S17 author. Review scope: `src/supp/17_S17.md`, S16, core §11.6, and `verification/path_checks.py`. Independent calculations are in `reviews/v73_math_independent.py`; they import no candidate implementation and integrate the host in reciprocal coordinates. This is internal model review, not independent human review or empirical certification.

## Disposition

**The revised finite-transition construction supports a conditional V7.3 upgrade. No mathematical blocker remains in the reviewed S17 statement and proof.** The actual comparison proof supplies a nonempty, sufficient path into S16 from specified states outside its invariant region. It does not establish political adoption, preservation of implementation authority, human agency, or coverage of general AI hazards. The proof is an elementary but substantive composition of transient support control, capture reduction, selection reversal, host reserve, and fully stated resource constraints; it is not a new general control method. The domain clarification and numerical-check repairs below were incorporated and verified before this review closed.

## Findings and resolution

1. **Moderate in the initial statement; resolved.** The first saved S17 draft stated only `V_min < V_0 <= 1`. Together with `0 < E_* < e`, that does not exclude a nonpositive floor or `V_0=0`, while the host bound uses `1/V_0` and S16 requires a positive floor. The revised statement explicitly gives `0 < V_min < V_0 <= 1`. The revised proof also records invariance of the unit share intervals, nonnegative support, and `0 < V <= 1`, making all comparison prerequisites explicit. Neither clarification changes the intended proof.

2. **Major in the initial numerical interpretation; resolved in both prose and tests.** The original `insufficient_recurrent_support` check incorrectly asserted that removing maintenance after the successful pulse necessarily causes this self-coupled witness to recapture. Its support source is `b_1 x`, and after this pulse the remaining source is integrable. Both the candidate integrator and independent reciprocal-host integration give continued recovery, not relapse. The revised S17 explicitly distinguishes unavailability of the prescribed funded policy from proof of actual failure, and the replacement `defunding_does_not_itself_prove_recapture` check preserves the correct interpretation. A persistent external source could create another adverse model, but would need to be stated and tested separately.

3. **Moderate numerical-check defect; resolved.** The original order-of-convergence assertion compared maxima/minima sampled on different time meshes against an RK4 mesh. That conflates integration error with sampling error. It failed despite correct fixed-time convergence. The revised check compares order at common scheduled endpoints and retains extrema under separate absolute-tolerance checks. Entry-host errors for midpoint steps `0.001` and `0.0005` are approximately `1.2020e-6` and `3.0094e-7`, with a verified refinement ratio of `3.9941`, consistent with second order.

4. **Switching premise resolved in the saved theorem.** The release is an instantaneous downward change in correction; a two-sided slew bound would disallow it. S17 now explicitly permits deactivation and limits its construction-rate bound to upward building. It also permits the conversion change at installation and keeps the state continuous. That is a valid piecewise-classical model. A physical system requiring slow ramp-down would need a different schedule and cost calculation.

No other analytic blocker was found in the actual proposition and proof.

## Proof audit

- **Installation comparison.** Nonnegative support and `d(t) >= d_0`, together with `x <= 1`, give `z' <= epsilon (b_0-d_0 z)`. The stated `Z_0` and its integral `I_0` are correct, including when support starts below `b_0/d_0`.
- **Support phase and zero-duration branch.** From `d_B >= d_infinity` and `b_1/d_infinity < z_dagger < c/a`, the booster equilibrium satisfies `z_B < z_dagger`. The logarithm defining `T_z` is finite and nonnegative when used. If `Z_L <= z_dagger`, taking `T_z=0` is valid and support remains below the threshold. In the positive-duration case the comparison reaches equality at `T_z`, which suffices.
- **Capture phase.** The identity `logit(x)'=zeta(az-c)` is exact. Integrating the two support comparisons yields the stated upper bound, and division by the strict margin `zeta(c-a z_dagger)` gives sufficient finite `T_x`. The positive part correctly permits a zero capture phase. The dates are scheduled bounds, not claimed first hitting times.
- **Release and liability.** At the support threshold the post-release derivative is strictly negative, so its upper bound persists under ordinary correction. Consequently capture cannot rise above `xbar`, and the effective liability margin is at least `Delta`. The strict post-release gain inequality allows an S16 row margin in `(0,1)`, including `b_1=0` by choosing a smaller margin rather than setting it equal to one.
- **Load phase.** For binary fixed loads and common background payoffs, `logit(y)'=se[nu-tau(1-x)]`. The pre-release upper rate `se nu` and post-release upper rate `-se Delta` give the stated `T_y`. The assumptions `0<y_0<1` and `0<E_*<e` make all logits meaningful. If the safe low-load type were absent (`y_0=1`), no such finite entry result would follow without mutation or entry; S17 correctly excludes that boundary.
- **Host reserve.** Since `ey <= e`, the maximum-load logistic trajectory is a valid lower comparison. Its reciprocal solves `u'=rho-Au`; both the `A != 0` and `A=0` formulas are correct. Because `e>E_*`, this worst trajectory decreases whenever it is above the floor. The terminal reserve condition therefore protects the whole preceding interval, not merely the endpoint. S16 supplies continuation once the capture, support, load and host conditions are simultaneous.
- **Costs and implementation.** The integral is the full ramp average `(d_0+d_B)L/2`, plus all booster and ordinary operations until the entry deadline. It does not omit baseline correction. Capital cost and the other running cost are included, and ordinary recurring funding is distinct from the finite budget. Peak and upward build-rate restrictions are consistent with the expressly admitted switches. These are feasibility conditions for the specified production relation; they do not produce the authority, resources or reliable response capacity endogenously.

## Independent numerical reproduction

The standalone reviewer script independently reconstructs the bound and uses RK4 on capture/load logits, support, and reciprocal host viability. The adverse short-pulse trajectory was also refined from step `0.0008` to `0.0004`. Both the independent reviewer script and the revised candidate's six-check `path_checks.py` run completed successfully. Sampled extrema below are approximate numerical summaries, not the analytic certificate.

| Quantity | Independent result |
|---|---:|
| Scheduled booster release `T_F` | 1.6437417941 |
| Conservative S16 entry deadline `T_*` | 2.6065034993 |
| Maximum-load host lower bound at entry | 0.3219986980 |
| Protected host floor | 0.3 |
| Full transition cost | 10.6307401729 |
| Ordinary recurring requirement | 0.6 |
| Positive witness sampled minimum host | approximately 0.665465 |
| Positive witness capture/support at release | approximately 4.713e-6 / 2.828e-7 |
| Positive witness load at entry | approximately 1.589e-14 |
| Early withdrawal without the conversion cut: host at time 30 | 0.1046903981 |
| Early withdrawal without the conversion cut: final capture | approximately 1 |
| `zeta=8`: lower bound / actual minimum host | 0.2965249217 / approximately 0.646420 |

The positive witness starts outside S16 in all three relevant coordinates: `x_0=0.9>xbar=0.3`, `z_0=1.8>c/a=1`, and `E_0=0.765>E_*=0.7`. Its initial gain is 2 and initial effective liability is only 0.4. Its post-reform ordinary gain is 0.4. This is not a restatement of S16's safe-initial-state premise.

The defunded self-coupled trajectory is independently retained as a guard against overclaiming necessity. After release its support is approximately `8.482e-7`, capture tends to zero, and the host stays safe. Analytically, while `z<=1/2`, `x'<=-5x(1-x)` for these parameters. Thus subsequent support growth is at most `1.2[-log(1-x(T_F))]/5`, keeping total support far below `1/2` and closing the bootstrap. A positive recurring-maintenance premise is sufficient for the stated robust construction; it is not necessary for every special self-coupled trajectory.

## Scope of the recommended upgrade

Accept a **conditional reduced-model reachability result**, with the assembled files refreshed from the reviewed source. Preserve the distinction between a specified, executable programme and a theory of how institutions acquire or keep those powers. The construction does not compute the maximal correctable kernel, prove a necessary or optimal reform, calibrate a real budget, or show that legitimate correction survives unrestricted amendment. Core §11.6 and the final S17 scope paragraph appropriately maintain those limits.
