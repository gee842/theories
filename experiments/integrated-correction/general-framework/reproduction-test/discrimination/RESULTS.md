# An intervention that distinguishes a reproduction mechanism from a fitted rival

5 October 2026 task date. AI-assisted theory and exhaustive finite computation. [Protocol](PROTOCOL.md), [implementation](analyze.py), and [saved output](analysis.json). This is a synthetic identifiability result, not validation on real institutional outcomes.

## The models agree on the specified calibration histories

The full formation model links a round's harm proportion Z to subsequent turnover T:

\[
\Pr(T=1\mid Z,s)=.05+.20Z.
\]

Its restricted rival uses constant turnover probability .15. The rival retains the same learning, work allocation, training, appointment, and record-transmission mechanisms. It removes only dependence of turnover on current outcomes. It is therefore an **outcome-insensitive turnover rival**, not an institution with every rule fixed.

Calibrate while execution is blocked. Both ordinary blind action and randomized inquiry have mean harm proportion .5 at every underlying state. Hence the full model's mean turnover is .15, the rival's parameter. This is calibration to an exactly known synthetic population moment, not an estimate from finite empirical data.

More strongly, the entire event-labeled projected kernel for `(skill, installed practice, turnover)` is identical in both models. Before turnover, skill is determined solely by skill and practice: an adaptive practice trains at one carrier; other portfolios do not add a carrier. Once turnover occurs, loss and appointment depend only on that pre-turnover skill and the old practice. Marginalizing Z therefore supplies the same .15 turnover probability for every underlying state compatible with the projection. Induction yields equality of complete projected path laws, not merely equality of one mean.

The check exhausts 181 reachable underlying states in each execution-blocked model. Every projected row agrees with an independently constructed reduced kernel within `1.12e−16`; the 25-round skill curves differ by less than `1.12e−15`.

This equivalence excludes archive contents, complaint records, realized harms, inquiry timing and service counts. Those may differ even before restoration. It is a statement about specified observation channels, not all possible records.

## The models disagree on the effect of enabling correction

From the same original full initial state, the protocol separately enables and blocks execution in each model. The primary outcome is probability that skill remains at round 25:

| Model | Execution blocked | Execution enabled | Within-model intervention effect |
|---|---:|---:|---:|
| Outcome-dependent turnover | 57.94% | 67.93% | **+9.99 percentage points** |
| Calibrated constant turnover | 57.94% | 57.94% | **0 points** |

Both models can acquire a useful representation and benefit from acting on it. Their disagreement concerns whether that benefit changes the survival of the capacities needed later. In the full model, sufficiently effective response reduces harms and consequent turnover; this changes skill and practice continuation. In the rival, the corresponding arrow is absent.

The second declared intervention substitutes the supplied uniform-nomination aggregate procedure for linked inquiry. Linked-minus-aggregate skill retention is **+9.55 points** in the full model and **zero** in the rival. This is not a comparison against the best possible aggregate learner or a claim that raw records are universally indispensable.

The retained ordinary-service response meets all proposed expected constraints with probability 55.29% in the enabled full model and 43.17% in the enabled rival. That capability outcome is separate from survival and from all-round safety: randomized inquiry can violate the ordinary-service harm bound. All ordinary/inquiry volumes and harm counts are retained in the output; no single welfare score aggregates them.

## Which observations diagnose the missing arrow?

A common full starting state with an installed frame permits a direct one-round check:

| Installed frame, execution enabled | Full-model mean turnover | Rival mean turnover |
|---|---:|---:|
| Correct conditional response | .08 | .15 |
| Reversed response | .22 | .15 |
| Irrelevant attribute | .15 | .15 |

Blocking execution makes every row .15 in both models. The direction of the effect depends on whether the executed response actually improves physical outcomes; strengthening an erroneous response can accelerate capacity loss.

Joint harm and turnover records provide another exact diagnostic. Conditional on a fixed full starting state and a portfolio of n independent cases with harm probability μ, Z has variance `μ(1−μ)/n`. The full model implies

\[
\operatorname{Cov}(Z,T\mid s)=.20\operatorname{Var}(Z\mid s),
\]

because `E[T|Z,s]=.05+.20Z`. The rival's covariance is zero. Under blocked execution, μ=.5, giving .025 for a two-case ordinary portfolio and .05 for a one-case training or inquiry portfolio. These joint logs were excluded from the calibration-equivalence claim; they can distinguish the two supplied models even before restoration.

In real data, covariance alone would not identify this causal arrow. Workload, severity, workload reporting or shared disturbances could influence both harms and turnover. The separate [design analysis](../design/DESIGN.md) specifies timed interventions and measurements needed to distinguish these possibilities.

An additional structural check follows without fitting a new result: clamping turnover to .15 in both models makes their entire transition kernels identical from the same full starting state. Any model-specific restoration-effect difference must then disappear. The measured intervention in a real system would need to implement the stated clamp without changing other mechanisms, or disclose the bundled effects.

## Why the comparison is useful and where it stops

The programme now has a specific test on which a reproduction mechanism and a calibrated rival disagree, while agreeing on all their permitted calibration histories. Observed skill and leadership persistence under blocked correction cannot select between them. A prospective intervention and suitable measurements can.

This is a result about two specified causal models. It does not show that the richer model is true of actual institutions, that no different rival could match the intervention results, or that the proposed loss mechanism is universal. Physical failures need not increase attrition in every domain; some increase solidarity or attract external support. Each application must justify and test the sign and timing of its own response.

The new implementation reproduces every endpoint and cumulative reward from all six prior full-model arms within `3.56e−15`. It preserves source hashes and verifies probability mass, effort accounting, analytic reduced rows, and the declared one-round forecasts. The main new result is the testable distinction, not a claim that a synthetic model has confirmed its own premises.
