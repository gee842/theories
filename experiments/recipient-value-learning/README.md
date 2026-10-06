# Reward training and later target-liked responses

This retrospective analysis of Zhang and Hackel's Experiment 3 estimates a small, uncertain training-assignment contrast: **+0.50 percentage points**, with a participant-level approximate 95% interval of **−4.25 to +5.24 points**. The three fixed sensitivity analyses also have intervals containing zero. This neither establishes equivalence nor identifies the psychological mechanism of acquired concern.

The [independent numerical check](independent-check.json) accepts the computation: it reconstructs 385 participants, 12,320 offered trials and all 10,532 published cleaned responses. It matches 6,160 participant fields, 98,560 offered-trial fields, 200 aggregate fields, 16 awareness fields and 412 hashes; the largest numerical difference is 1.14 × 10⁻¹³. This numerical acceptance is distinct from the scientific interpretation and causal-identification review. The [protocol](PROTOCOL.md) was reviewed and frozen before this package aggregated outcomes, with the paper's findings and original scripts already known. It is a prospective computational plan for a retrospective reanalysis, not a preregistration of the experiment.

## Question and observed population

The analysis addresses a bounded connection in the generative account: can prior reward training change later responses concerning the trained target? It compares congruent versus incongruent training within each current private-payoff condition, then weights those two differences equally. The outcome is each participant's number of target-liked selections divided by **32 offered decisions**. Timeouts mean no liked response; they are not classified as choices of a disliked option.

The [preserved sources](../../sources/32-mental-state-reward-learning-2026-10-06/README.md) contain 387 raw task files. Date/completion/identity matching yields 385 saved task-and-survey respondents. The authors' attention and missing-response rules retain 333 and exclude 52. We reconstruct those rules from source and reconcile all 10,532 answered rows in the published cleaned data using a fixed source-filename-order identity mapping. The five completed surveys without usable IDs are not recovered. Neither the primary nor the all-saved sensitivity is a full recruitment intention-to-treat analysis.

## Results

Here congruent training associates favorable target states with favorable private outcomes. During the decision phase, a congruent current condition makes target-liked selections more favorable for private payment; the incongruent current condition does the opposite.

| Training | Current condition | Participants | Liked responses / 32 | Responses / 32 |
|---|---|---:|---:|---:|
| Congruent | Congruent | 89 | 84.41% | 99.02% |
| Incongruent | Congruent | 68 | 84.79% | 98.85% |
| Congruent | Incongruent | 94 | 53.89% | 98.80% |
| Incongruent | Incongruent | 82 | 52.52% | 98.67% |

| Fixed analysis | Participants | Standardized training contrast | Approximate 95% interval |
|---|---:|---:|---:|
| Primary: author-eligible, 32 offered trials | 333 | +0.50 points | [−4.25, +5.24] |
| All saved matched respondents, 32 offered trials | 385 | −0.31 points | [−4.90, +4.29] |
| Author-eligible, answered-trial denominator | 333 | +0.34 points | [−4.40, +5.09] |
| Author-eligible, RT ≥ 0.2 seconds, 32 offered trials | 333 | +1.47 points | [−3.47, +6.40] |

The primary difference is −0.38 points within the current congruent condition and +1.37 points within the current incongruent condition; their equally weighted average is +0.50. Participants are the independent units. The interval uses the four participant-cell variances and Welch–Satterthwaite degrees of freedom. Sensitivity intervals are individually nominal, not simultaneous. Exact values, response fractions and the fixed coding reconciliation are in [results.json](results.json).

The original paper's self-optimal-choice reversal question and mixed-logistic analysis are separate. This package does not reproduce that GLMM. With the offered denominator, optimal fraction is `L` in the current congruent condition and `R−L` in the current incongruent condition, where `R` is response fraction. Consequently the standardized no-reversal minus reversal optimal contrast is **+0.43 points**, not the primary +0.50 points. The recorded response adjustment reconciles them. Its uncertainty is calculated from participant optimal fractions directly, preserving covariance.

## What this evidence identifies

The contrast concerns assignment-related target-liked responding among the stated observed sample. It remains uncertain around zero and does not warrant a directional behavioral claim from this reanalysis alone. The interval is not an equivalence test, and no meaningful equivalence margin was selected.

Even a well-established behavioral transfer would not alone identify a changed target-value coefficient. Acquired private-payoff expectations, target-state knowledge, task demands and target-directed valuation remain possible pathways. Actual feedback histories exist in the raw records, but trial-level subjective expectations are not independently measured. A fixed concern weight with changed reward beliefs can also affect choices. No new reinforcement-learning fit or mediation analysis is performed.

Awareness was measured after the decision task. We report its assigned-cell frequencies descriptively, without selecting the primary sample or inferring an awareness-conditioned causal effect. Familiar-target transfer, direct concern, new-recipient generalization, durability and justified ethical standing remain separate questions. This updates the empirical boundary of the existing [concern evidence study](../../_process/research/2026-10-05-concern-theory/conceptual-evidence.md), rather than supplying a new synthetic mechanism.

The released eligible records give 145 aware and 188 unaware participants, with no missing awareness fields. The paper's rendered page 16 reports 187 unaware. The RT filter does not explain the difference; the one-person descriptive discrepancy remains unresolved. It changed no eligibility rule, coding or outcome analysis.

## Reproduction and provenance

The immutable [protocol freeze](protocol-freeze.json) records approval and pre-output hashes. [analysis.py](analysis.py) reads original CSVs, reconstructs raw eligibility and responses, validates the published cleaned records, and then computes the specified summaries. [verification.json](verification.json) binds the code, protocol, source bytes, environment and outputs. Prepared outputs are [participant summaries](participants.json) and [trial records](prepared-trials.csv).

The first authorized run failed while importing SciPy, before reading data. The [failure record](development/first-run-failure.txt) preserves that environment mismatch. Installing SciPy 1.15.3 in an external temporary dependency directory repaired execution; the frozen code, protocol and estimand were unchanged. Bundled Python 3.12.14 and NumPy 2.3.5 were retained. Run from this study directory:

```sh
PYTHONPATH=/tmp/ren-recipient-value-deps /Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 analysis.py --run
```

If that temporary directory is unavailable, provision SciPy 1.15.3 outside the repository and point `PYTHONPATH` to it. Do not modify preserved sources or bundled dependency directories. The installed dependency is computational infrastructure, not part of the scientific observations.
