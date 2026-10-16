# Institutional intervention reanalysis: frozen exploratory protocol

5 October 2026. Frozen before reading numerical rows from either experimental dataset. The published results and author analysis code have already been read; this is a post-selection secondary reanalysis, not a new preregistered experiment. No favorable result will be promoted from secondary to primary.

Source: Dickson, Gordon and Huber (2022), *Identifying legitimacy: Experimental evidence on compliance with authority*, Science Advances 8:eabj7377. Public author deposit DOI 10.7910/DVN/SPIMAV, version 1, CC0. Metadata, README, scripts and column headers have been inspected; data outcomes have not.

## Primary contrast: randomized information quality

Use Experiment 1. Each group-period has one authority and four citizens. The authority chooses small/big investment (`e_biginvestment` 0/1). A fair random draw then assigns accuracy to the lower/higher level available for that choice: small permits 0/1; big permits 1/2 (`g_accuracy`). Define randomized treatment Z=`g_accuracy-e_biginvestment`, verify it is binary, and retain **all enforcement rules**. Enforcement choice occurs after accuracy realization: selecting only the PATS rule would condition on a post-treatment variable and change identification.

One observation is a complete group-period, identified by session, period and group. Outcome Y is `g_totcontributedtopg/4`; verify against the four individual citizen decisions. All five group records must agree on investment, accuracy, authority choice and group contribution. Do not treat repeated citizens or the four group members as independent randomized units.

The causal target is the contemporaneous effect of the more accurate versus less accurate information draw under the experiment's installed response process, averaging over naturally chosen investment and history. It includes any consequent change in authority enforcement and citizens' expected punishment; it is not a pure fairness or nonmaterial legitimacy effect. The known assignment probability is one half conditional on investment/history.

For each session compute the centered Horvitz–Thompson contrast mean[2(2Z−1)(Y−0.5)]. Average these session effects equally as primary, giving each independent laboratory session equal weight. Report the group-period weighted contrast and ordinary difference in means as descriptive sensitivity, and report both investment strata. Approximate 95% interval: session-effect standard deviation divided by sqrt(number of sessions), multiplied by Student-t critical value with sessions−1 degrees of freedom. Report the number of sessions and leave-one-session-out effect range; few-session coverage is approximate. Do not use individual-row standard errors, label a large number of rounds as independent sessions, or turn a bootstrap into exact randomization inference.

## Prespecified boundary contrast: authority beneficiary

Use Experiment 2. `g_authoritypaidfrompg` is randomized after investment, accuracy and enforcement rule choice, before citizen decisions. It changes whether the authority benefits from contribution; citizen own payoff formula stays fixed. Use all group-periods for the main boundary contrast and PATS (`e_enforcementrule==2`) as a prespecified subgroup: that rule is pre-treatment for this contrast. Same group-level outcome and equal-session centered-HT estimator/interval.

Report the randomized compensation effect separately under big and small investment, and their difference, when every session contains both investment types. Investment is chosen rather than randomized, so this is modification of the randomized compensation effect by a pre-treatment observed subgroup, not a randomized causal effect of choosing investment. A null will not establish equivalence. We will not infer a universal intrinsic motivation from a weak compensation contrast.

## Descriptive matched-material contrast

For continuity with the paper, report Experiment 1 mean contribution under big versus small investment restricted to realized medium accuracy and PATS. This keeps the current material enforcement rule and accuracy equal, but investment was chosen; label it an identification-qualified/descriptive contrast, not the primary randomized intervention. Report by session, with the same small-cluster caution. Do not assume that random assignment to authorities makes every authority action independently randomized.

## Scope, exclusions and reproducibility

Inspect counts and missingness after freezing. Stop on unresolved assignment coding, inconsistent group records or missing main outcomes rather than invent values. Do not filter subjects by favorable quiz performance or groups by observed cooperation. Preserve all primary and boundary results, including nulls and sign differences. Do not fit extra models or search subgroups after seeing results.

This experiment changes authority information and beneficiary conditions, but does not manipulate endogenous renewal, succession, controller preservation or represented goals. The existing microbial test measured prediction after serial passage, not this same intervention. Therefore this analysis can validate a component response in a human institution; it cannot certify a matched causal mechanism or a quantitatively calibrated cross-domain transition map. Record that limitation regardless of results.

Save exact source files, source URLs, SHA-256 hashes, data license, grouped rows, session estimates, scripts and all outputs. Do not contact authors or transmit participant data anywhere. Public data are analyzed locally.
