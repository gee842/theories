# Biological continuation: history, selected activity and subsequent conditions

**Later empirical continuation:** [molecular memory, viable-count calibration and finite ecological return](BIOLOGICAL-RENEWAL-INTEGRATION.md) supplies specific previously missing evidence and preserves replication/source discrepancies. Its [joint experiment specification](BIOLOGICAL-JOINT-VALIDATION.md) remains unexecuted. The dated results and completion assessment below retain their original scope.

8 October 2026. AI-authored continuation of [Ren's request to finish the remaining work](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md). The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) and earlier [organized-scale construction](ORGANIZED-SCALES-INTEGRATION.md) govern the interpretation.

**The public-data prediction comparison and the activity-to-later-burden analysis are completed.** Previous food history improves conditional prediction for held-out worms even against an equally sized nonlinear model. A separate preparation links tissue-dependent pathogen adherence and neural integration to avoidance, and restricted avoidance to greater later pathogen fluorescence. These are actual numerical constraints on the account. **A quantitatively validated cellular–organ–learning–ecological-renewal loop is still not completed.** No available table examined here measures that whole loop, and these studies cannot be joined by inventing individual identities or transport laws.

**本轮完成了已有数据可执行的预测比较与后续病原负荷分析。** 历史食物密度在同容量对手下仍改善平均预测，但并非对每只动物都更好；活动改变后续接触与负荷的连接也有实验数据。分类概率不等于神经状态，多个实验不等于同一条联合历史。全尺度定量校准、持续生态更新及一般有效性保持未完成状态。

## What is now connected

Earlier activity leaves bodily effects that participate in later discrimination and movement; movement changes contact and therefore later bodily and microbial conditions. The coordinates distinguish roles within this shared history. They do not posit a cognitive chooser outside the body or a passive external world. An epithelial cell's polarity, adherence and signaling matter through organized relations; an organ total or a current food-density value can omit those relations.

The new investigation tests two empirical consequences of that description: whether retaining earlier encounter information helps predict later activity, and whether changed access to avoidance changes later microbial burden. This supplies factual correspondence for practical judgments about consequences. Avoidance, exploitation and predictive accuracy do not themselves establish ethical goodness, G0 or a universal practical reason.

## A real prediction comparison

Haley et al. (2025), [*Accept–reject decision-making revealed via a quantitative and ethological study of C. elegans foraging*](https://doi.org/10.7554/eLife.103191), published behavioral tracks, classifier-derived encounter probabilities and models. We preserved their original Figure 4 source-data-3 workbook and the exact published analysis-code revision. The [experiment record](../../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/continuation/README.md) provides sources, plan, code, numerical results and reproduction instructions.

The analyzed mixed-density table contains **198 animals and 172,463 rows across 100 imputations**. Imputation selects likely sensed encounters and samples prior exploitation events; it does not create new animals. The number of included encounters ranges from 1,702 to 1,745 per imputation. All 2,242,019 analyzed numeric cells agree between openpyxl and direct worksheet-XML decoding. The 19,797 available worm/imputation groups omit three combinations with no selected encounter.

The soft target is a GMM-derived exploitation probability. Predictors are current log food density, time off food since a previous inferred exploitation, previous sensed density and last exploited density. The time quantity is a satiety proxy, not a calorimetric observation. The authors' actual code resolves the prose ambiguity: cumulative off-food time is reset at the preceding simulated exploitation. The prior density terms begin at the acclimation density. The source's growth-based food-density calibration is retained; we have not independently measured its error or depletion by the worms.

### Frozen predictions across preparations

The source's coefficients were fitted on single-density conditions, then used without refitting on mixed-density encounters. Recomputing both models reproduces every supplied prediction to within `2e-14` and the published summed log likelihoods within `1e-6`.

| Frozen published predictor | Equal-worm soft cross entropy ↓ | Squared error against soft target ↓ | Mean prediction |
|---|---:|---:|---:|
| Current density + time off food | 0.748349 | 0.252046 | 0.239623 |
| Above + previous encounter/exploitation densities | 0.678027 | 0.218068 | 0.316897 |

The mean soft target is **0.458404**. History improves average loss by **0.070322**, but substantial underprediction remains. It improves the score for 154 of 198 animals. Paired worm resampling of these fixed scores gives exploratory 2.5–97.5 percentiles **0.048865–0.089351** for the improvement. These are conditional descriptive intervals, not plate-independent coverage guarantees. We do not treat the workbook's 100 imputations as 100 independent datasets or reuse its reported zero p-value as such a test.

### A same-capacity conventional rival

New five-fold fits hold out entire worms, keeping all their encounters and imputations together. Scaling uses training animals only. The fixed exploratory plan compares five ordinary logistic models; no result determines which model is retained or reported. Each animal is equally weighted, then each available imputation, then its encounters. The unpenalized optimizer checks its gradient and objective. This is new within-preparation cross-validation, distinct from the frozen cross-preparation test above.

| Model | Parameters | Held-out soft cross entropy ↓ | Squared error against soft target ↓ |
|---|---:|---:|---:|
| Constant | 1 | 0.690592 | 0.228596 |
| Current density | 2 | 0.626326 | 0.198753 |
| Current density + time off food | 3 | 0.622831 | 0.197054 |
| Above + their separate quadratic terms | 5 | 0.621669 | 0.196751 |
| Density + time + two prior densities | 5 | **0.605695** | **0.189007** |

The five-parameter history model improves on the five-parameter nonlinear rival by **0.015974** in average cross entropy; conditional paired-worm percentiles are **0.004598–0.026781**. It wins for **125 animals**, while the nonlinear rival wins for **73**. Thus the aggregate advantage does not warrant a pointwise claim that adding history always helps. The successful model is conventional logistic regression, and conventional learning theory receives full credit. This is evidence for retaining relevant relational history in this task, not for the exclusive necessity of our terminology or ontology.

The simpler density/time models already retain historical information through time since exploitation. The comparison specifically tests **earlier food-density information**, not an entirely memoryless body against a disembodied memory. Plate/date identities are absent from the supplied table, so whole-worm splitting cannot certify separation of all experimental dependencies. The behavior classifiers and imputations were supplied before splitting; this is conditional prediction under those measurements, not end-to-end out-of-sample classifier validation. Inclusion depends on inferred sensing, so we have not predicted every encounter's sensing and action from pre-encounter measurements alone. Causal learning and the cellular storage mechanism remain additional questions.

## Tissue, neural organization and subsequent microbial burden

Anderson and McMullan (2018), [*Neuronal and non-neuronal signals regulate Caernorhabditis elegans avoidance of contaminated food*](https://doi.org/10.1098/rstb.2017.0255), supplies a complementary causal-intervention preparation. Pathogenic *M. nematophilum* adheres at rectal epithelial cells; cell-promoter rescue, neuronal disruptions and avoidance-access manipulations test successive relationships. This is not the same pathogen or learned-foraging preparation as the Haley data.

The supporting workbook's original size and MD5 match its Figshare metadata. The secondary descriptive extraction preserves all numeric values and cell references for five strain groups under pathogenic and nonpathogenic mixtures. For pathogenic lawns, BUS-1 mutant avoidance averages **30.065%** over nine measurements; the `egl-5p::BUS-1` rescue averages **60.480%** over nine. The promoter also acts in three posterior body-wall muscles, so the intervention is not strictly epithelial-only. Wild-type pooled measurements are not matched contemporaneous pairs for those columns; we do not manufacture such a pairing or derive a new causal effect size from it.

ASE-only TAX-2 expression fails to restore avoidance in the published experiment. The source shows that combined sensory-neuron expression can restore it. This directly constrains the interpretation of the old positive serial relay: a generic product of three gains must not substitute for actual multi-neuron integration, inhibition or pathogen specificity. The failed rescue is preserved alongside the successful one.

For the effect on later microbial conditions, the experiment compares ordinary lawns with lawns covering the plate, restricting avoidance. All numeric fluorescence observations yield:

| Preparation | Individual measurements | Mean rectal SYTO13 fluorescence | Sample SD |
|---|---:|---:|---:|
| Standard lawn; avoidance available | 33 | 3022.642 | 2101.681 |
| Full lawn; avoidance restricted | 37 | 4633.858 | 1648.634 |

The standard-lawn mean is **34.77% lower**. These recover the article's approximately 3023 and 4634 arbitrary units. Lawn geometry changes exposure opportunity as well as movement access; the contrast is not an isolated intervention on a cognitive command. Plate identities are missing, so individual-level confidence intervals would overstate what can be warranted about independent experimental replication. Fluorescence at the rectal opening is not a count of all living pathogens or sustained community renewal. We also preserve the article's finding that some developmental endpoints do not differ under the avoidance manipulation: a lower burden is not a guarantee of improvement on every endpoint.

![Verified prediction comparison and separate pathogen burden measurements](../../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/continuation/continuation-results.png)

## Completion audit and the next discriminating experiment

| Remaining obligation from the preceding turn | Current result |
|---|---|
| Actual fitted predictions with a conventional rival and held-out observations | **Completed for conditional foraging prediction.** Both frozen transfer and new grouped fits are reproduced; calibration bias and individual rival wins remain. |
| Activity changes subsequent microbial conditions | **Empirically constrained in a fixed pathogen preparation.** Tissue/neural interventions and avoidance-access/burden evidence are connected at the assay level, without fabricated individual joins. |
| Calibrated cell/organ signals → acquired response → motion → subsequent microbial conditions | **Still incomplete.** Signal, retention, sensing selection and movement are not jointly estimated by these tables. |
| Sustained ecological reproduction, renewal and consequences for other participants | **Still incomplete.** Fluorescence and food density do not identify microbial reproduction, community composition or wider renewal. |
| Entire general cell–organ–body–ecosystem account certified | **Not established.** A finite preparation cannot alone justify the universal account. |

The required remaining experiment is now specified rather than left as “more evidence.” Use a single defined worm–bacterial preparation with identified plate, cohort and time records. Matched destructive cohorts are acceptable where simultaneous measurement is impossible; their correspondence must be tested rather than requiring every variable from one animal. Measure regional burden and tissue state, identified signaling activity, retained response after matched current exposure, motion/contact, and later viable bacterial abundance. Add repeated cycles and explicit nutrient/replenishment measurements for the renewal question. Fluorescence-to-viable-count calibration and measurement disturbance require their own controls.

Train observation and transition maps on complete plates/days; hold out entire plates/days and specified interventions. Compare current-condition, acquired-history and equally expressive conventional coupled models using the same inputs and training data. Test the failed single-neuron rescue and the successful combined rescue as separate interventions. Predict both action/contact and later burden, rather than treating a behavior-classifier score as a complete trajectory. Retain actual costs, loss, delays and failed histories. Use empirical uncertainty for empirical claims; only invoke the existing Lean error theorem after its containing domains, drift/regularity and action-coupling premises are justified.

No such experiment was run here, and no new mathematical theorem is claimed. The existing 26-theorem organized-loop construction remains checked at its original hypotheses and source hashes. The sources inspected here do not establish that no suitable dataset exists anywhere; they establish exactly which required variables our retained evidence supplies and which it lacks. The pending work is a substantive empirical obligation, not something that can be finished by adding another toy model or changing a completion label.

## Substantive self-review

This is the implementing author's review, not independent agent review. The strongest alternative is an ordinary embodied learning and coupled-physiology account retaining the same relations. It fits these results without additional generative vocabulary. The present contribution is an accountable synthesis, reproducible correspondence and an explicit test of omitted history. Better prediction does not identify the unique physical memory, establish ethical warrant or prove every scale relation. Conversely, absent joint variables in this representation are not themselves evidence that the reconstructed biological relation fails. The documented underprediction and individual rival wins are actual empirical limitations and remain in the theory's revised scope.
