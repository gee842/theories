# When changed choice challenges unchanged evaluation

6 October 2026. AI-authored continuation of the [reward-learning identification study](REWARD-LEARNING-AND-RECIPIENT-CHOICE.md), addressing empirical support for the [generative foundation](GENERATIVE-GROUNDING.md). **Checked conditional result:** the mathematical contract passes separate internal review, and the fresh Lean 4.29.1 build passes 27 audited declarations in two additive modules. No new participant observations or empirical conclusion are claimed.

The named connection is learning history → acquired evaluative influence. The earlier analysis showed that changed target-directed choice can be explained by changed private-payoff expectations while evaluation stays fixed. It proposed a future contrast exceeding what independently bounded alternatives permit. This study supplies that quantitative bound, including nonresponse and a declared fraction of poorly characterized cases.

## The alternative must be specified first

Consider two potential training conditions for the same population of persons and offered contexts. Let `r_j` be a unit's probability of responding and `p_j` its probability of choosing the target-directed option conditional on responding. Its target-directed response probability per offered opportunity is `r_j p_j`. A timeout contributes no target-directed selection; it is not classified as selecting the opposite option. At zero response probability, `p_j` denotes an unobserved model extension.

A restricted logistic choice model writes its score as

\[
z_j=b_j+v_jq_j+\beta_je_j,\qquad p_j=\sigma(z_j).
\]

Here `q` represents factual expectations about the target consequence, `v` its effective evaluative coefficient, `e` expected personal payoff and `β` personal-payoff sensitivity. The remaining declared influences enter `b`. These variables and their decision scale are supplied model inputs, not measurements furnished by observed choice.

Under unchanged evaluation, separately justified bounds on changes in factual knowledge, private expectancy, payoff sensitivity and baseline influences can imply

\[
|z_1-z_0|\le D
\]

on at least a fraction `1−ε` of the **paired population**. The [mathematical account](../../../_process/research/2026-10-05-concern-theory/reward-association/BOUNDED-IDENTIFICATION-MATH.md) derives the full budget, including changed payoff sensitivity. Arbitrary baseline changes or unbounded sensitivity make this restriction uninformative. Assigned equal payment, a nonsignificant questionnaire difference and similar mean belief reports do not establish it.

## A sharp ceiling using response levels

Let `R_j` be the population response fraction and `L_j` the population target-directed response fraction, both per offered opportunity. Define

\[
m=\tanh(D/4),\qquad
H=\max(0,R_0+R_1-1-\varepsilon).
\]

Then the bounded unchanged-evaluation class implies

\[
\boxed{-R_0+(1-m)H\le L_1-L_0\le R_1-(1-m)H.}
\]

The bound permits response selection to depend on the person, their beliefs and their choice score. It requires no independence between responding and choosing. It also avoids requiring an observed counterfactual response gate for each person: the two marginal response levels suffice for this part of the bound.

The reasoning has two steps. A logistic score displacement of at most `D` changes conditional choice probability by at most `m`. At least `H` of the population must overlap in its response capacity and satisfy the score restriction. The bounded probability change applies on that overlap; all remaining contributions receive their most permissive bounds. A five-stratum construction reaches the endpoints for bounded probabilities and approaches them with finite logistic scores. Thus the inequality is sharp for the stated class, while a more restrictive psychological model could give a smaller region.

Equal response rates alone provide limited reassurance. Two equally sized groups can exchange which condition elicits their response, with unchanged individual scores. Both conditions then have response rate one half, yet the change in target-directed responses can approach one half. When everyone responds, the bound simplifies to `|L_1−L_0| ≤ ε+(1−ε)m`. High response levels constrain this ambiguity; a small difference between response levels does not eliminate it.

For illustration only, take `R_0=R_1=0.99`, `ε=0.01` and a score budget giving `m=0.10`. The upper ceiling is `0.117`, or 11.7 percentage points. These are mathematical inputs, not calibrated values from the existing experiment. A population contrast above that ceiling would contradict their conjunction with the restricted unchanged-evaluation model.

## What a test could establish

Sampling uncertainty belongs in the comparison. The response fractions and choice contrast are estimated together; their sample values cannot be inserted as known population constants. The companion provides a conservative simultaneous-confidence procedure for independent participant units with fixed arm counts and complete offered-opportunity outcomes. Uncertain calibration bounds require their own joint error allowance. Outcome-dependent exclusions or optional stopping need additional justification.

Rejecting this region establishes that at least one premise of the bounded alternative fails. Interpreting that failure as changed evaluation requires independent support for the factual, private-payoff, baseline, decision-scale and population assumptions. It does not uniquely identify concern, explain its ethical warrant, or establish actual recipient welfare. Failing to reject the region does not prove evaluation unchanged.

The current reward-learning archive supplies neither a validated score budget nor paired coverage. Its previously accepted estimates and exclusions remain unchanged. The proposed contingent-versus-yoked training comparison with a new recipient remains unrun. This result states what a properly characterized contrast could discriminate; it does not manufacture that evidence from the existing uncertain estimate.

## Contribution and verification boundary

The [formal package](../../../experiments/recipient-value-learning/formal/README.md) contains 27 audited Lean declarations, including algebra helpers. Its main theorem covers arbitrary finite rational weighted populations and a sharp five-stratum construction. A second module proves an exact rational-odds quadratic equivalence, a sufficient coefficient certificate and paired-gate consequences. The fresh build uses only the declared standard `propext`, `Quot.sound` and `Classical.choice` dependencies, with no custom axioms or proof holes.

The real-valued logistic calculus, general probability-space interpretation and simultaneous-confidence argument are separately reviewed mathematical proofs. They are not silently included in the Lean claim. [Independent checks](../../../experiments/recipient-value-learning/bounded-identification/checks.json) reconstruct sharp witnesses, boundary cases and the failures of mean-only inference without reading participant data. The [internal review](../../../_process/research/2026-10-05-concern-theory/reward-association/BOUNDED-IDENTIFICATION-REVIEW.md) and its [binding receipt](../../../_process/research/2026-10-05-concern-theory/reward-association/bounded-identification-review.json) preserve the accepted scope. No empirical observations are generated by a sharpness construction.

This advances the existing discriminating-support requirement by making a named alternative quantitatively testable. The remaining constructive connection—acquired evaluation through actual succession, fresh correction and justified action—continues in its existing study. The five foundation requirements remain unchanged. A future result outside a defensible bound would narrow the surviving explanations; a failure of calibration or a compatible result would preserve the alternative and restrict the evaluative interpretation.
