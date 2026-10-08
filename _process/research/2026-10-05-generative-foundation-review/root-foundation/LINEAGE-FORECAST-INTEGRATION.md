# Forecasting recorded continuation from inherited life-cycle histories

8 October 2026. AI-authored numerical study and author self-review for [The Theory of Evolution](../../../../theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md). The preceding goal turn restated the completion map and was **no progress** toward scientific completion. This study executes the next comparison instead of repeating that status. It advances recovery of evolutionary mechanisms, actual lineage continuation and comparative assessment; all six full completion requirements remain in force.

**Result.** In retrospective chronological validation, retaining recorded ancestry improves predictions of phase viability over a changing population-average stage model in all four experimental treatments. The largest Brier-score improvement is in the large, initially switch-negative treatment: **0.218869 → 0.206472**. Predicted next-phase viable representation per recorded donor also has lower root-mean-square error in all four treatments. These gains belong to a conventional Bayesian lineage model. Our present generative articulation supplies no independently calibrated alternative probability law, so this is evidence for the usefulness of inherited history, **not demonstrated superiority of our theory over that conventional model**.

**中文结论。** 在按时间遮蔽结果的回顾性预测中，保留实际谱系的贝叶斯模型，在四个处理中都比变化的阶段平均模型更准确；最大 Brier 改善为0.218869降至0.206472。既定替换分配下的下一阶段存活后继数，其均方根误差也均降低。该增益属于已有常规谱系模型可表达的机制；当前生成论没有另行校准的概率规律，不能把同一个模型改名后算作比较胜利。稳定处理中简单恒定模型的局部优势、缺失及实验事故保持可见。

## What is predicted, and what is already known

The [previous reconstruction](LINEAGE-CONTINUATION-INTEGRATION.md) verified 3,808 non-missing observations, 3,600 recorded parent links and a separately linked mutation-reversion assay. The new calculation uses the genealogy only. It never imports terminal coalescence, inferred mutation assignments, full-tree fitted survival estimates or the later reversion outcomes as forecast features.

At the start of each phase, its incoming culture assignments have already been set by the preceding phase's recorded death–replacement procedure. All 48 planned culture slots are forecast simultaneously. Only earlier phase outcomes enter inference. Current condition flags and viability are attached **after** the forecast to evaluate it; missing outcomes remain unscored. Each phase type has its own survival propensity, with same-phase ancestry obtained by following two actual parent links. Interrupted ancestry is left unresolved and given a new uniform root, not retrospectively repaired from surviving descendants.

The output contains **3,840 planned-slot forecasts**, including 32 without observed outcomes. The primary comparison scores **3,424 observed outcomes in cycles 2–10**; the first cycle's 384 forecasts remain available but are excluded from headline scores because neither phase yet has within-treatment training data. A second time window uses cycles 6–10. All experimental condition codes enter the primary observed-viability target; an additional condition-zero sensitivity changes scoring eligibility only, leaving forecasts and training unchanged.

For each donor at the preceding phase, forecasts are summed over its already assigned cultures. The target is how many of those cultures are viable at the end of the next phase. It is conditional on recorded incoming assignments, not a forecast of the next replacement lottery or eventual fixation. Donors with no assigned cultures are retained as structural zeros in the output. Headline donor errors use donors with at least one assignment and fully observed assigned outcomes. The resulting 2,506 donor/phase cases are related through genealogy, not 2,506 independent biological replicates.

## Explicit conventional models

The [analysis specification](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/FORECAST-PROTOCOL.md) was written before executing these forecast scores. The genealogies and their main biological outcomes had already been inspected, so this is not preregistration or an untouched external holdout. It is a reproducible chronology-restricted reanalysis.

| Model | Retained history and supplied commitments |
|---|---|
| Constant stage frequency | All past observations of that treatment and phase, with a Beta(1,1) starting prior; no time change or ancestry. |
| Changing stage propensity | A shared latent probability for each phase batch; beta transitions between batches and all preceding batch outcomes. |
| Inherited lineage propensity | A latent probability per culture, inherited along recorded same-phase ancestry; inference includes the entire past branching forest, including past siblings. Initial cultures share a latent founder. |

The latter two use 100 probability midpoints and transition-bin probabilities from Beta(1+σp, 1+σ(1−p)). An equal prior over σ = 1, 2, 5, 10, 25, 50, 100, 250, 500, 1500 is updated using earlier observations only. Probabilities and σ are integrated rather than selected from test performance. Initial roots are uniform. These are transparent modelling premises; the generative foundation does not derive them. Root structure, phase independence, conditional observation independence and homogeneous transition form limit the interpretation.

The transition family is credited to the inspected colgen source. The author's published analysis fits the complete genealogy using a latent MAP/parameter-optimization procedure. Our implementation is a chronological sum-product adaptation with a finite parameter prior, not a reproduction of those fitted values. The [software reading record](../../../../sources/evolutionary-selection/doulcier-2025/colgen/README.md) preserves a material provenance limitation: the currently retrieved 2.0 ZIP differs from the dependency's pinned SHA-256; the publisher-verified Zenodo archive is version 1.0 and its implementation differs. Neither was installed or executed.

The lineage model has access to every ancestry/viability input used by the generative interpretation. Other available measurements, such as detailed cell counts and inferred genotypes, are not supplied to either. This is an adequate comparator for the current history-based claim, not an assertion that every possible conventional predictor has been exhausted. Calling the same probability calculation generative does not produce an additional competitor or an independent forecast.

## Measured predictive performance

Brier score is the mean squared error of the viability probability; lower is better. Every row below uses the same observations for all three models.

| Treatment | Scored outcomes | Constant stage | Changing stage | Inherited lineage |
|---|---:|---:|---:|---:|
| Standard, initially switch-negative | 848 | 0.247821 | 0.247789 | **0.240287** |
| Large, initially switch-negative | 848 | 0.233962 | 0.218869 | **0.206472** |
| Standard, initially switch-positive | 864 | 0.057283 | 0.058238 | **0.057148** |
| Large, initially switch-positive | 864 | 0.129290 | 0.127627 | **0.125486** |

Negative log-probability likewise improves against the changing-stage model: respectively **0.689838 → 0.674592**, **0.628767 → 0.602841**, **0.232770 → 0.226414**, and **0.410415 → 0.403778**. The gains persist in the later-cycle and condition-zero aggregate scoring sensitivities. These descriptive comparisons are not culture-independent significance tests, intervention forecasts or evidence of a generally superior theory.

There are genuine limits. In the standard switch-positive treatment, the constant model has a slightly better Brier score than the lineage model in phase II and in the cycles 6–10 aggregate. It also has lower donor-count mean absolute error there. More history and a more flexible model do not guarantee improvement on every loss function or subset. The full phase, time-window, flag-sensitivity and loss results remain in the output rather than selecting only favorable summaries.

| Treatment | Scored donor/phase cases | Changing-stage donor-count RMSE | Lineage donor-count RMSE |
|---|---:|---:|---:|
| Standard, switch-negative | 492 | 0.861814 | 0.847532 |
| Large, switch-negative | 480 | 0.819445 | 0.787482 |
| Standard, switch-positive | 811 | 0.248809 | 0.246186 |
| Large, switch-positive | 723 | 0.400537 | 0.396115 |

These are expected counts conditional on known transfers. They neither identify mutation origins nor measure the distribution of future offspring under an unobserved replacement lottery. The primary data still concern one recorded evolutionary history per treatment, with related blocks and chance amplification; no additional independent mutation origins were created by reanalysis.

## Numerical verification and correspondence

The [implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/forecast_lineages.py), [separate checker](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/check_forecast.py) and [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/forecast-verification.json) expose the computation. The checker enumerates small latent forests independently, uses separate numerical quadrature for selected transition bins, recomputes scores and donor sums, checks temporal input boundaries, and binds forecasts to the previously verified raw-workbook reading. Full calculations at 50 and 200 states assess discretization against the specified 100-state analysis.

**Executed checks pass:** 49 enumerated forest cases agree within 1.34×10⁻¹⁵; 51 separately integrated transition bins agree within 2.04×10⁻¹⁴. The checker verifies 11,520 forecast rows and 10,848 donor rows across the three grids. Changing future records at three forecast cutoffs leaves all 48 earlier predictions at each cutoff unchanged. The largest 100-to-200-state lineage-probability change is 0.000843, and the largest Brier change across the reported scoring subsets is 0.0000172. These numerical tolerances do not measure uncertainty about the biological model.

The checks concern numerical inference and empirical accounting. They do not prove the latent biological model, causality, generalization or the foundation. **No new theorem is claimed and no Lean result is added.** The prior six checked lifecycle identities and all earlier proofs retain their original scope. Altering future outcomes, flags and future parent records must leave an earlier forecast unchanged; rejecting an unfiltered future-containing input is checked separately. The ledger records actual results, not merely this intended procedure.

## Consequence for the theory and the next test

The affirmative contribution is now a measured predictive connection: recorded reconstruction histories carry useful information about later viability and conditional descendant representation beyond a changing treatment average. This strengthens the account's insistence on actual inherited relations, and advances requirements 2, 3 and 5 beyond retrospective ancestry and observed cycle completion alone. The mechanism operates within one experimental history: living development, supplied medium, transfer activity and later viability jointly determine continuation. Analytical roles do not become independent substances.

The substantive counterreview is equally consequential. The improvement is already expressible in a conventional model using those relations. A claim that ordinary evolutionary models cannot handle this connection would now contradict our own evidence. The present foundation also leaves a phenomenological beta transition, phase factorization, initial priors and laboratory support supplied. These are specific unresolved explanatory commitments, not evidence that the whole account is impossible.

The comparison changes latent heterogeneity and pooling as well as ancestry: it is not an isolated intervention on ancestral information alone. Related cultures also share experimental blocks. A model of changing block conditions is therefore a substantive further comparator before attributing the gain specifically to inherited genotype. Discretization sensitivity does not test prior sensitivity, unmeasured shared exposure, omitted cross-phase dependence or alternative transition families. The current result supports the specified history-sensitive predictor, while the previous genetic-reversion evidence supplies a different, scoped causal argument. Neither substitutes for the other.

The next central connection is **an independently calibrated inherited switching/development mechanism → a transition law → forecasts under genetic or transfer changes**. Use separate phenotype or reversion assays to constrain that law, and evaluate outcomes not used to fit it. Give the conventional comparator the same measurements. A stronger contribution could be less reliance on separately fitted survival parameters, justified transfer across conditions, or additional tested predictions; it need not be a calculation that conventional mathematics is incapable of expressing. Retrospectively inventing a different kernel until it wins this genealogy would not meet that requirement.

For the normative programme, improved prediction concerns whether capacities actually support further life and how that support can be assessed. It neither turns reproductive advantage into ethical authority nor derives G0. The axiom-based practical-judgment candidate remains completed at its declared scope; calibrated recognition and implementation remain separate obligations. This is author self-review, with independently coded numerical checks, not independent agent review or completion of the full theory.
