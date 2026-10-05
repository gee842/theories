# Measured systems: no demonstrated intervention superiority

5 October 2026. **The available evidence does not establish that this theory predicts interventions better than existing approaches. A newly frozen exploratory comparison on measured microbial data finds no incremental predictive advantage under its primary rule.** The gap is now more precisely located: the framework must supply a specified, identifiable model and a usable decision rule, then succeed against comparators that also model the deterioration and repair of observation and execution capacity.

This assessment does three things: inventories the actual evidence, executes one stricter external-data comparison without replacing an unfavorable result, and specifies the next decisive causal comparison. It does not turn simulations into measured systems, reuse into independent replication, or forecasts into intervention effects.

## 1. New measured-data comparison

The source is Huisman, Dal Bello and Gore's [2026 microbial study](https://www.nature.com/articles/s41564-026-02422-3). We reuse the archived condition-level dataset from four aquatic source inocula, three salinities and two temperatures. The original authors' ecological discoveries and mechanistic explanations precede this project. The forecast target is measured next-cycle biomass, not growth computed from composition.

The [protocol](benchmark/PROTOCOL.md) was saved and hashed before this new run. Previous analyses had already used all outcomes and their mixed findings were known. This is **post-publication, outcome-reused exploratory analysis**, not a fresh untouched test set or a preregistration. The new procedure addresses two concrete weaknesses in interpreting previous gains: future-cycle training and a limited baseline family.

Each outer fold trains on cycles 1→2 and 3→4 from three sources and predicts cycle 5→6 in the fourth. All 24 held-out conditions enter once. Each fold has 36 training rows and six test rows. No observation from its held-out source enters model fitting or tuning; all training outcomes precede test inputs in propagation-cycle order. Source identities are not model features, so unseen fixed-effect categories cannot manufacture an extrapolation problem.

The baseline has current biomass, salinity, temperature and cycle. The augmented version adds mean 16S copy number and Shannon diversity. These are composition summaries, **not direct renewal or corrective-capacity measurements**. Both have the same 18-candidate library: persistence, training mean, four ridge regularizations, and twelve Gaussian kernel-ridge configurations. The nonlinear model is an established flexible regression comparator. Selection uses nested earlier-cycle, unseen-source validation from the outer training pool only, with identical tuning opportunities. The primary expectation requires the selected augmented library to improve both RMSE and MAE.

### Result

Both libraries selected persistence in all four source folds. Their 24 predictions are identical. The primary incremental-prediction expectation is not met.

| Frozen comparison | Baseline RMSE | Augmented RMSE | Baseline MAE | Augmented MAE |
|---|---:|---:|---:|---:|
| **Primary: inner-selected full library** | **0.047725** | **0.047725** | **0.032974** | **0.032974** |
| Descriptive: inner-selected ridge only | 0.111677 | 0.088052 | 0.077239 | 0.070177 |
| Descriptive: inner-selected kernel ridge only | 0.079840 | 0.082420 | 0.064162 | 0.065891 |

Training-mean prediction has RMSE 0.081576 and MAE 0.066108. Errors are in blank-corrected OD600 units. The ridge-only improvement must not replace the failed primary comparison: both ridge variants perform much worse than persistence. The flexible kernel comparison worsens with augmentation. These fixed descriptive comparisons show why a favorable addition to one restricted model is insufficient to establish incremental usefulness against competitive baselines.

The four source blocks have paired primary gains of exactly zero because both selected predictors are the same function. All 256 ordered source-block bootstrap resamples and all leave-one-test-source-out calculations therefore also give zero. This is an **algorithmic identity on these observations**, not a tightly estimated biological equivalence or proof that composition carries no information. Four reused source blocks with overlapping training fits cannot support a confident population superiority or equivalence claim. The source-specific RMSEs are 0.053965, 0.037387, 0.040130 and 0.056481; no source favors either selected library.

### What the result does and does not decide

It answers the declared narrow question adversely: the added summaries provide no selected-library gain for late-cycle biomass forecasting under this source-and-time split. The claim “adding latent-condition proxies gives a robust measured prediction improvement” is not supported by this available example. The result does not falsify the conditional mathematical root theorems, prove the summaries irrelevant, or exclude gains on new disturbances or other endpoints. None of those alternatives was tested, and no favorable substitute was searched.

The previous repaired comparison had a condition-holdout RMSE gain but a slightly worse MAE; its prespecified source-holdout sensitivity improved both. Those analyses trained on other trajectories' later cycles and used a narrower baseline. They remain preserved in the [original microbial report](../../../../experiments/integrated-correction/general-framework/closure-study/external-test/RESULTS.md). Their numeric scores are not directly comparable to this report's scores because the test observations and training opportunities differ. They jointly demonstrate model- and task-dependence, not a resolved general advantage.

The present check accepts deposited sequence processing and the earlier audited per-sample composition reconstruction. It removes neither the original dataset's batch dependencies nor uncertainty suppressed by averaging three replicates per condition. It tests cross-source and later-cycle generalization in one experiment, not a new environmental perturbation, sensor renewal, institutional succession, AI alignment, or causal intervention. The archived data were selected after reading the paper, and all outcomes have now been repeatedly used; further tuning on them would be development, not confirmation.

## 2. Evidence ledger across the existing programme

| Evidence | Actual empirical content | Relevance and unresolved gap |
|---|---|---|
| [Human information experiment reanalysis](../../../../experiments/integrated-correction/general-framework/gap-resolution/EMPIRICAL.md) | Randomly higher information accuracy: contemporaneous contribution estimate +10.07 percentage points, approximate six-session interval +1.57 to +18.57 | A domain-specific response to information, under stated assignment assumptions. No tested advantage over established institutional models and no endogenous renewal of the apparatus. |
| [Next-round investment test](../../../../experiments/integrated-correction/general-framework/gap-resolution/empirical/SUCCESSION-RESULTS.md) | Better information at t → later investment if assigned authority at t+1: −0.29 points, approximate interval −10.60 to +10.02; six sessions | Inconclusive for a closer feedback arrow. Immediate benefit cannot be promoted to evidence of reproducing its conditions. |
| [Institutional agreement reanalysis](../../../../experiments/integrated-correction/general-framework/reproduction-test/empirical/RESULTS.md) | Facilitation contrast on retained permission to sanction +42.59 points; 66/72 groups retain an unchanged code | Initial formation plus static persistence remains a strong rival. Treatment scheduling across 31 sessions is not independently verified, so the contrast is not an unconditional causal estimate. No actual apparatus-renewal measure. |
| Previous microbial reanalysis | Actual biomass outcomes; mixed primary feature-addition result | Observational forecasting, weak connection from composition to renewal, and baseline dependence. |
| New benchmark in this report | Actual measured biomass; strict source/time split and matched nonlinear model opportunity | Primary gain absent. A concrete restriction on claims of predictive superiority. |
| Formation, closure, viability and handoff simulations | Outputs generated by stipulated mathematical models | Valid internal discrimination and implementation tests; not empirical evidence that the real-world mechanism or policy advantage holds. |
| [AI selector pilot](../../../../drafts/2026-10-02-iaseai-selecting-the-selectors/experiment/pilot.log) | Synthetic lineage/rubric dynamics; P1 fails | It is not measured deployment behavior or a real AI intervention study. Its negative simulation outcome must remain visible. |

No inspected dataset contains all of: independently measured degradation of information and execution capacity, randomized action on their renewal, endogenous later renewal decisions, actual successor replacement, held-out novel conditions, and a fair comparison with a jointly optimizing established controller. The current records therefore cannot identify the full claimed causal advantage, even if their individual component results were all favorable.

## 3. Why the theory needs stronger competitors

The comparison cannot stop at fixed maintenance, no feedback, or myopic output maximization. [Van Oosterom, Maillart and Kharoufeh (2017)](https://research.tue.nl/en/publications/optimal-maintenance-policies-for-a-safety-critical-system-and-its/) already jointly optimize a deteriorating sensor and its monitored system using a partially observed decision model. [Lao and colleagues (2015)](https://doi.org/10.1002/aic.14960) combine preventive sensor maintenance with robust state estimation and economic model predictive control. These are directly relevant comparator families; their cited demonstrations are not empirical validation of our theory.

There is also a logical ceiling on a superiority claim. Fix a true dynamical model, a task loss J, information access, intervention set, budget and admissible policy class Π. If the established controller solves

\[
\pi^*\in\arg\min_{\pi\in\Pi}J(\pi),
\]

then any proposed policy \(\pi_{\rm root}\in\Pi\) satisfies \(J(\pi^*)\le J(\pi_{\rm root})\). This follows from the definition of optimality. A new vocabulary cannot strictly outperform that exact optimum under identical premises.

The scientifically meaningful comparative claims are therefore narrower: the framework identifies omitted state variables or causal dependencies, guides useful measurements or perturbations, predicts transfer with fewer fitted parameters, selects justified constraints, or provides an effective approximation at lower data/computation cost. These are genuine potential contributions, but each needs its own measured comparison. A correctly specified standard control model may implement the framework's insights rather than serve as an incompatible rival. With plural constraints, compare policies on the same declared feasible set and Pareto criteria; do not invent a common scalar after seeing the outcomes.

## 4. Concrete prospective test that can answer the remaining question

The already developed [handoff design](../../../../experiments/integrated-correction/general-framework/reproduction-test/design/DESIGN.md) provides the best local starting point. It studies benign tasks with independently scored correct answers, real maintenance choices under limited time, a sealed correction package, actual replacement by a successor, and new cases. The following additions make its scientific comparison decisive. This is a prospective specification, not an already executed or fully powered experiment.

### A. Identify the mechanism before claiming policy superiority

1. Collect founder work and independent error reports before assignment. Randomize report availability **before versus after** a consequential maintenance decision (A), preserving equal task/maintenance resources.
2. Seal the founder's actual package. Randomize operative successor access to that package versus a specified generic orientation (B). Do not select only founders who chose maintenance or successors who used it.
3. Replace the founders and score all assigned successors on a fixed new-case distribution, including absent or late responses. Log maintenance allocation, delivered content, availability, actual use, error type, response time and remaining execution resources separately.
4. Repeat one additional handoff with recorded fresh outcomes and renewed randomized report timing. This tests repeated reproduction over a finite stated horizon; it does not establish indefinite persistence.

The A effect on delivered maintenance identifies a first assignment-induced response. The B effect on independently scored successor performance identifies the effect of the specified operative handoff. Their factorial interaction is a complementarity estimand, not automatically a mediated effect or a universal signature of feedback. The existing design already states this distinction. If mechanism identification requires a particular delivered maintenance quantity, add a separately randomized standardized package/maintenance intervention; regressing the outcome on a chosen post-treatment quantity does not identify its causal effect.

### B. Lock competing intervention forecasts

Before confirmatory observations, freeze three model families trained only on an independent development cohort:

- A strong history-based predictive model using all allowed past outputs and interventions.
- A standard jointly estimated observation/execution maintenance model with state estimation and POMDP or constrained predictive-control planning, including the same information degradation, capacity repair and resource restrictions available to the proposed model.
- The specific root-theory instantiation, with its proposed structural restrictions, state mapping, and parameters. State exactly which predictions differ from the standard joint model. If they coincide, report an embedding or interpretation result, not a scientific prediction contest.

All receive the same usable records, action permissions, computational budget and opportunity to tune. The root model cannot receive hidden capacity measurements that are withheld from its comparator. Cost measurement includes gathering and preserving the records. Complexity, fitting failures and unsupported extrapolations remain visible.

For each held-out lineage and random intervention, record forecast distributions before seeing successor outcomes. Declare one primary proper predictive score in advance, such as the Brier score for failure to provide a correct response by the deadline. Use whole lineages as held-out units and reserve entire prespecified disturbance/turnover regimes for transport tests. Compare paired lineage scores; individual cases are not independent organizations. This can test superior *intervention prediction* because the intervention is randomized and predicted prospectively, although accurate mean forecasts alone do not prove every proposed mediator.

### C. Separately randomize policy choice

On a new confirmatory cohort, randomly assign entire lineages to the locked root policy or the strongest eligible standard joint-maintenance policy. Both act within identical resources, observations and permitted interventions. The primary outcome should be prespecified successful responses by deadline over two handoffs, with explicit resource, error-burden and availability constraints retained separately. A policy that improves its aggregate score while violating a protected constraint does not pass.

Define the smallest worthwhile improvement before confirmatory data. Determine the required number of independent lineages from a blinded or independent pilot's lineage-level variation and delivery rates; do not count many within-lineage cases as the sample size. Freeze exclusions, missing-output handling, stopping rules, multiplicity treatment and the selected comparator before recruitment. No numerical sample-size claim is justified until these inputs and the required effect size are set.

This test can fail in informative ways: the proposed measurement adds no forecast information; a first feedback arrow is absent; a package increases confident errors; the standard joint model matches the root model; or a beneficial intervention costs more than its incremental value. Any of these results narrows a substantive claim rather than requiring another interpretation of the word “alignment.”

## 5. Audit and reproducibility

The frozen protocol SHA256 is `4858ec20a8a1d194d51b3c0d72d6c043f563e4370972791dfbad0dbd4f596e66`. The input CSV SHA256 is `87da93d948f63aeea11d3ef14fdcd39c81d00fae20afaa8d43027b7ab68e2c11`. No existing studies, raw records, protocols or outputs were modified.

- [Analysis implementation](benchmark/analyze.py), [complete fitted choices and inner scores](benchmark/analysis.json), [24 saved predictions](benchmark/predictions.csv), and [paired source errors](benchmark/paired_source_errors.csv).
- [Separate saved-output verifier](benchmark/verify_outputs.py) and [71 passing arithmetic, selection and provenance checks](benchmark/VERIFICATION.json). This checks the saved output independently with the Python standard library; it is not independent empirical replication or a second model implementation.
- [Root agent's independent assessment audit](INDEPENDENT-CHECKS.json) separately recalculates all eight prediction metrics and checks the fold ordering and primary selections; its eight check groups also cover mathematical results elsewhere in this assessment.

Run the analysis with Python and NumPy, then run the verifier with Python's standard library. The local run used Python 3.11.2 and NumPy 2.4.6. No parameter or endpoint changes followed the result. The next contribution cannot be another declaration of universal validation: it must be a specified prediction or intervention that survives the comparison above.
