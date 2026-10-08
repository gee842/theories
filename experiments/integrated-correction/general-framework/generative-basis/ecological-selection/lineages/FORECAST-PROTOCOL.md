# Chronological lineage forecasting: analysis specification

8 October 2026. AI-authored specification written before executing the forecast scores below. This is **retrospective chronological validation**, not a preregistered experiment or an untouched external test: these genealogies and their major outcomes have already been inspected. The preceding goal turn only restated completion requirements and was no progress toward their scientific completion.

## Target and information boundary

At the start of each phase, predict each recorded culture's probability of being recorded viable at its end. Predict every culture in a phase simultaneously, before assimilating any outcome or condition flag from that phase. Treatments are fitted separately. The primary score includes every non-missing recorded outcome; a condition-zero scoring sensitivity retains exactly the same forecasts. Missing observations stay missing. This tests the observation labelled `Extinct`, including experimental mishaps, not a purified genetic fitness.

The incoming parent assignments are already determined by the preceding phase's replacement record. For a given phase type, follow two recorded edges to its preceding occurrence. Train only on earlier occurrences of that phase. Initial cultures share an unobserved founder propensity; a broken observed ancestry starts a separate unobserved root. No gap is filled from future coalescence. A shared root is a modelling commitment motivated by the common starting genotype, not a measured identical phenotype. Distinct phase propensities are modelled separately; cross-phase dependence beyond actual transmission is omitted.

Exclude the first occurrence of each phase from headline scores, since it has no within-treatment training outcome. Preserve its forecasts and report cycles 2–10 separately from cycles 6–10. For each observed donor at time t−1, also sum the forecasts of its assigned cultures at time t and compare with the number actually viable. This is **next-phase viable representation given recorded incoming replacement**, not a forecast of the lottery at the end of t, terminal fixation, or an independently replicated offspring distribution. Give zero-assignment donors a zero expectation.

## Models fixed before scores

1. **Constant stage frequency:** Beta(1,1) posterior predictive using all previous outcomes of that treatment and phase. It is a diagnostic, not the strongest rival.
2. **Changing stage propensity:** a hidden probability shared by each phase batch, with a beta transition between occurrences. All observations in that batch inform its propensity together.
3. **Inherited lineage propensity:** a hidden probability at each observed culture, with beta transitions along recorded same-phase ancestry. Sum-product inference uses the entire *past* branching forest, including past siblings. It is a conventional Bayesian lineage model, not a new generative-theory invention.

For models 2–3, use 100 midpoint probability states and transition-bin probabilities from Beta(1+σp, 1+σ(1−p)). Give equal initial weight to σ in [1,2,5,10,25,50,100,250,500,1500]. Integrate σ using past-data likelihood; do not select it from evaluation scores. Roots have uniform midpoint priors. Bernoulli emissions use the midpoint. This follows the retrieved colgen 2.0 beta-kernel form, but replaces its full-genealogy hard-MAP/parameter optimization with chronological posterior averaging. It is not a replication of colgen's published fitted values. The retrieved archive does not match the dependency's pinned SHA; that distinction must be preserved.

The generative interpretation identifies reconstructed lineages and their changing continuation conditions. At this point it supplies no independently calibrated alternative transition kernel. Reusing model 3 under that interpretation produces the **same numerical forecast**, not a fourth independent competitor. No superiority will be credited merely for renaming it. Likewise, any benefit over model 1 must survive comparison with model 2 and remains conventional-model credit.

## Evaluation and checks

Report Brier score and negative log probability, treatment by treatment; lower is better. Retain phase and cycle summaries and both headline time windows. Do not count correlated cultures as independent evolutionary replicates, compute a culture-level significance test, select a winning treatment, or claim intervention validation. Report the sign of every treatment's contrast.

Check inference against independent exhaustive enumeration on small branching forests; compare its discretized beta kernel against separate numerical quadrature; independently recompute scores and donor sums; and perturb evaluation outcomes, condition flags and later parent records to confirm that earlier forecasts do not change. Compare the 100-state primary calculation with 50 and 200 states as numerical sensitivity, without selecting the most favorable result. Bind receipts to source, protocol, code and outputs. These are numerical and empirical checks, with no new universal proof claim or new Lean theorem.

The test advances completion requirements 2, 3 and 5. It does not finish organization origins, new inherited units, ethical warrant, or the full evolutionary theory. A next study must address whichever substantive model limitation the results actually reveal.
