# Recipient preference transfer after reward training

Status: prospective computational analysis plan for a retrospective public-data study. This protocol is being written before this repository computes Experiment 3 outcome aggregates. The paper's published findings and original analysis scripts are already known. This is not a preregistration of the original experiment, a blind replication, or a new experiment.

## 1. Named connection and scope

The governing connection is acquired evaluation of another's state → later choice concerning that target. This study audits what the Experiment 3 assignment contrast in Zhang and Hackel (2025), *Reward Association With Mental States Shapes Empathy and Prosocial Behavior*, can establish. It does not model another synthetic learner or prove the emergence of ethical standing.

The original study, code and public data are at [OSF 58wsu](https://osf.io/58wsu/); the [primary paper](https://www.hackellab.org/media/zhang-hackel-2025-psych-science.pdf) gives the experiment and its published analyses. Original bytes are preserved in [source group 32](../../sources/32-mental-state-reward-learning-2026-10-06/). Inputs are its `originals/Experiment_3/data_raw_primary/Pavlovia/*.csv`, `data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv`, `data_clean/data_3.csv`, `code/cleaning_3.R` and `code/analysis_3.R`; task code is in `study_materials/psychopy_task_3.zip`. The source receipt binds exact paths and hashes before execution. Conceptual interpretation remains in the existing [concern evidence study](../../_process/research/2026-10-05-concern-theory/conceptual-evidence.md#7-four-primary-empirical-anchors-with-narrow-claims).

Only Experiment 3 is analyzed this round. There is no new Experiment 2 family, fitted reinforcement-learning model, causal mediation analysis, or subgroup selection by awareness. Existing publication results are source facts, not outcomes computed by this package.

## 2. Design and observational units

Let `P=1` denote congruent training (the participant's favorable monetary outcome associated with the target's favorable state), and `P=0` incongruent training. Let `I=1` denote the decision-phase contingency favoring choices of a target-liked option for private monetary outcomes, and `I=0` the opposite contingency. Original task codes are training A/B and decision C/D respectively. Both factors must be read from actual source assignments, not inferred from choices or feedback.

The decision phase offers 32 trials per participant, each with a target-liked and a target-disliked option. Task code and source audit govern the interpretation of choice keys and options. The randomized participant is the independent analysis unit. Repeated trials are never counted as independent participants. The source task's shuffled fixed 24/8 decision contingency schedule is retained as an experimental feature; the analysis does not replace it with an independent Bernoulli reward process.

The primary population is the original authors' 333 eligible participants, reconstructed from raw task and post-task survey data using their actual cleaning rules. Eligibility is determined before any new choice aggregate is computed. The source owner's metadata-only audit has already found 387 task files, 390 qualifying completed surveys (five without usable anonymous IDs), 385 matched saved respondents, and 333 eligible participants. These counts and 52 exclusions are source reconciliation targets, not rules that permit altering exclusion criteria until those totals appear. Discrepancies block execution pending review. This metadata audit did not aggregate choices by treatment or calculate the proposed effect.

## 3. Source reconstruction and exclusions

Reproduce the original cleaning script's removal of pilot survey responses by parsing its displayed `EndDate` and retaining dates at or after 5 December 2023, 00:00. Preserve the source's displayed-time convention; do not invent a timezone conversion. Require the original completed-survey and participant-ID checks, then join by the supplied identifier to task records. Report unmatched or duplicate records rather than silently choosing a row.

The authors' eligibility intersection requires fewer than eight missing conditioning acknowledgment response times, fewer than seven missing decision response times, and a recoded final attention-check value below four. The numeric attention threshold is the source script's coding, not an inferred verbal inversion. Audit these rules against the preserved original script and reconcile the saved cleaned participant/trial records where a source-valid identity mapping is available. Do not match people using their computed treatment effect.

For every matched participant, verify that all 32 offered trial identities occur exactly once, training and decision assignments are consistent, and each offered trial has one liked and one disliked option. A missing choice/timeout is distinct from a missing offered-trial record. Unexpected keys, inconsistent key/RT missingness, malformed option labels, missing assigned conditions and duplicate trials are reported as source errors. They are not silently recoded as dislikes or zero-valued observations.

Keep original sources unchanged. Prepared records carry source filename/hash, participant identity, original trial identifier, assignments, choice status and response time. Public output uses repository-specific or author-anonymous IDs rather than unnecessary survey identifiers. Source hashes, runtime version and analysis-code hash accompany results.

## 4. Primary outcome and estimand

For participant `j`, define:

```
L_j = number of offered trials with a valid choice of the target-liked option / 32
R_j = number of offered trials with a valid choice response / 32
```

A timeout contributes zero to `L_j` because there was **no liked response**. It is not coded as a choice of the disliked option. `R_j` is reported alongside `L_j` so a change in responsiveness cannot disappear behind the liked-response contrast. Raw response time below 0.2 seconds is retained in this primary outcome, as in the original all-response analysis branch.

For the four cell means `mu_pi = mean(L_j | P=p, I=i)`, the sole primary contrast is

```
delta = 0.5 * [(mu_11 - mu_01) + (mu_10 - mu_00)].
```

This gives the two current-contingency strata equal weight. Unequal cell sample sizes do not change those weights. Report all four participant counts, means, sample standard deviations, response fractions and offered-trial counts, together with both component differences. These are components of the one primary contrast, not additional selected primary tests.

The estimand is the standardized training-assignment contrast among the author-eligible observed sample. Post-assignment exclusions prevent an unconditional claim to the full randomized intention-to-treat effect without further missingness/selection assumptions. The full contrast may reflect target-directed value, transferred private reward expectations, knowledge, demand, or mixtures. Holding the objective current contingency fixed does not hold subjective expected private payoff fixed.

## 5. Uncertainty calculation

Use the four independent participant-cell sample means. In cell order `((1,1),(0,1),(1,0),(0,0))`, use weights `w=(+1/2,-1/2,+1/2,-1/2)` and let

```
v_c = w_c^2 * s_c^2 / n_c
V = sum(v_c)
SE = sqrt(V)
df = V^2 / sum(v_c^2 / (n_c - 1))
CI95 = delta +/- t_quantile(0.975, df) * SE.
```

This is a two-sided approximate Welch–Satterthwaite interval for the weighted contrast, with participant-level variability. It is not an exact randomization interval or the original mixed-logistic coefficient's interval. Require at least two observed participants per contributing cell. Report an explicitly degenerate zero-variance interval if every component variance is zero, rather than dividing by zero. Do not truncate an approximate interval to the outcome's theoretical contrast bounds.

The primary contrast has one nominal 95% interval. Sensitivity intervals are descriptive, individually nominal and not simultaneous. No outcome-dependent choice among methods, covariates, trial windows or signs is allowed.

## 6. Fixed sensitivity and descriptive outputs

Produce the same four-cell summary and standardized training contrast for these three planned sensitivity analyses:

1. **All matched saved respondents:** all 385 matched saved task/survey respondents, including author-excluded participants, using `liked / 32`. This is a saved-respondent sensitivity, not full intention-to-treat coverage of the original recruitment.
2. **Answered-trial denominator:** the primary eligible population, using `liked / answered`. Report participant counts with zero answered trials and exclude them only from this explicitly conditional sensitivity. Retain offered-response fractions.
3. **Response time at least 0.2 seconds:** the primary eligible population, counting only liked choices with `RT >= 0.2`, still dividing by 32. Report the qualifying-response fraction. This changes the response qualification while preserving the offered-trial denominator. It is distinct from the authors' row-filtered answered-choice model.

Report post-task awareness frequencies and missingness by the four assigned cells only. Do not select the primary sample by awareness, compute an awareness-conditioned causal effect, or treat post-task awareness as a pre-treatment confounder. No new moderator family is introduced.

Describe the authors' preregistered self-optimal-choice reversal question separately from our liked-response estimand. The original scripts include all-response and `RT >= 0.2` branches and a random-intercept binomial model; this package does not claim to reproduce that GLMM unless a separate explicitly authorized fit is later performed.

As a deterministic coding reconciliation, define each participant's offered-trial self-optimal fraction `O`: `O=L` under `I=1`, and `O=R-L` under `I=0`. Let `delta_R0 = mean(R|P=1,I=0) - mean(R|P=0,I=0)`. The equally standardized no-reversal minus reversal optimal fraction must satisfy

```
optimal_no_reversal_minus_reversal = delta - 0.5 * delta_R0.
```

This is an algebra check on our descriptive means, not replication of a mixed-logit coefficient. With an answered-trial denominator and at least one answer per included participant, the corresponding response fraction is one and the adjustment vanishes. Preserve this distinction wherever the old and new contrasts are compared. If an uncertainty interval for a descriptive optimal-choice contrast is reported, calculate it directly from the participant's `O` values; do not discard within-participant covariance by adding marginal `L` and `R` contrast variances.

## 7. Identification limits and what would change the account

A nonzero assignment contrast would support transfer from the training manipulation to later target-liked responding under the observed decision conditions. Its sign and uncertainty may support, weaken or leave unresolved that bounded behavioral claim. It would not by itself identify a newly acquired target-value coefficient, direct concern, durable ethical commitment, or transfer to a new recipient.

Raw task histories preserve actual feedback and can support a later model comparison, but subjective reward expectations are not independently observed at each choice. A fixed target weight with a changed private-reward prior can produce the same choice tendency as a changed target weight under a restricted choice model. The current analysis does not settle those mediating alternatives. Post-task awareness cannot repair this identification problem by conditioning on a selected subgroup.

An empirical result near zero or inconsistent across the fixed sensitivities remains a result and will be integrated as such. No additional analysis family will be selected to obtain a favorable conclusion. The foundation gains a bounded empirical discrimination or a clear nonidentification boundary, rather than another definition of favorable generativity.

## 8. Freeze, execution and review

Before outcome aggregation: preserve the source audit, finalize source paths, obtain parent and independent prospective review of this protocol, and save a SHA-256 freeze receipt. Known paper results, previously inspected cleaning/analysis code and the timing of this retrospective protocol must be disclosed. No claim that the plan predates all knowledge of outcomes is permitted.

Implement `analysis.py` using the bundled Python runtime at `/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`, with NumPy/SciPy available for numeric summaries and Student-t quantiles. No spreadsheet workbook is authored. Syntax checks and source-schema inspection may occur before freeze; no treatment-group outcome aggregates, effect estimates, confidence intervals or result-driven adaptations may be run before approval.

After approval, save prepared participant summaries, results and a reproducibility receipt. The independent checker should reconstruct source eligibility and liked-response coding independently where feasible, and recompute the participant-cell estimand and interval without importing the producer's calculation functions. Preserve discrepancies and their repairs. No shared canonical files or Git operations belong to this package owner.
