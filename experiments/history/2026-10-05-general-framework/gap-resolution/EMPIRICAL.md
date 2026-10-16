# Institutional intervention evidence: causal component support, transfer still open

5 October 2026. An original reanalysis of public human experimental data is complete. **Randomly improving an authority's information accuracy increased contribution by an estimated 10.07 percentage points in this experiment.** This supports a bounded institutional response under the declared assignment assumptions. It does not validate the entire framework, explain all intrinsic motivation, or establish that the same causal mechanism operates in ecosystems or AI.

The primary source is Dickson, Gordon and Huber, [*Identifying legitimacy: Experimental evidence on compliance with authority*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8856613/), Science Advances 8:eabj7377 (18 February 2022). Its [author replication archive](https://doi.org/10.7910/DVN/SPIMAV), version 1, is publicly accessible through the Dataverse API and licensed CC0. The paper's findings were already known; the analysis below is a secondary reanalysis, not a new experiment or a novelty claim. The [protocol](empirical/PROTOCOL.md) was frozen before reading numerical data rows.

## The causal contrast

Experiment 1 randomizes information accuracy after an authority chooses investment and before it chooses enforcement. We use the higher-versus-lower accuracy draw conditional on that prior choice. We retain all subsequent enforcement rules: selecting only a favored rule would condition on a post-treatment choice. This identifies a total contemporaneous information effect, including resulting enforcement and incentive changes; it is not a pure nonmaterial legitimacy effect. [Primary experimental sequence](https://pmc.ncbi.nlm.nih.gov/articles/PMC8856613/).

The deposited files contain 90 participants, six laboratory sessions and 360 group-periods. Each group-period has one authority and four citizens. We verified that all five records agree on group treatment and outcomes, and that the recorded total equals the four citizen decisions. Outcomes are group contribution fractions. Repeated participants and four citizens sharing an intervention are not counted as independent experimental clusters.

For randomized indicator Z and outcome Y, the frozen estimator averages the centered Horvitz–Thompson score

\[
2(2Z-1)(Y-0.5)
\]

within each session, then weights the six independent sessions equally. Because the documented assignment probability is one half conditional on pre-draw conditions, centering at the fixed constant 0.5 does not change its target. The estimand averages immediate treatment effects over the experiment's naturally occurring histories and investments. It is not the cumulative effect of forcing all future rounds to use higher accuracy. Standard consistency, correct assignment recording and no cross-session interference are required; within-session history dependence is allowed in the causal target.

The interval below is based on variation among session estimates using Student-t with five degrees of freedom. With six sessions, coverage is approximate. No exact randomization p-value or population-wide institutional effect is claimed.

| Frozen primary measure | Result |
|---|---:|
| Equal-session information effect | **+10.07 percentage points** |
| Approximate session-based 95% interval | **+1.57 to +18.57 points** |
| Leave-one-session-out range | +7.92 to +11.92 points |
| Group-period weighted HT sensitivity | +9.31 points |
| Ordinary unadjusted difference in means | +11.21 points |

All six session point estimates are positive. This is a real intervention contrast in people, not a relabeled simulation or another ecological prediction exercise. The contribution outcome is task-specific; increased compliance alone is not a general measure of moral alignment or legitimate governance.

## Limits and negative evidence retained

The prespecified investment strata do not show equally precise responses. Under small prior investment, the information effect is +16.74 points, interval +5.49 to +27.98. Under big prior investment it is +2.78, interval −12.97 to +18.54. These are secondary conditional estimates, not a newly selected main result; chosen investment is not itself randomized. Later subgroup membership can depend on earlier rounds, making subgroup sample counts random; these ratio-type sequential summaries do not inherit a blanket finite-sample unbiasedness claim from the complete primary sample.

Experiment 2 provides a distinct randomized boundary contrast: after the authority's choices, compensation is randomized between benefiting from contributions and a fixed payment. Citizens' own material payoff rule stays fixed. It contains 110 participants, seven sessions and 440 group-periods. [Primary design description](https://pmc.ncbi.nlm.nih.gov/articles/PMC8856613/).

| Prespecified boundary contrast | Equal-session effect | Approximate 95% interval |
|---|---:|---:|
| Authority benefits rather than receives fixed payment, all rules | **−4.85 points** | **−11.93 to +2.23** |
| Same contrast in pre-treatment PATS subgroup | −2.87 points | −8.77 to +3.03 |
| Beneficiary-effect difference: big versus small prior investment | +3.02 points | −16.64 to +22.69 |

These data do not support a simple positive reciprocity effect under this estimator. They also do not establish that the effect is exactly zero, that the two conditions are equivalent, or that reciprocity never matters. Negative estimates and wide intervals are preserved rather than explained away.

For comparison with the original paper, the raw big-minus-small investment gap under identical medium accuracy and PATS enforcement is +10.13 points. Investment is chosen rather than randomized; we label this an identification-qualified/descriptive comparison and do not promote it to the primary intervention. One session has no small-investment observation in this restricted cell. Its within-session difference is missing, not imputed; only five sessions permit that descriptive contrast. The equal-session descriptive estimate is +15.93 points, illustrating that aggregation choices matter. The primary randomized analysis has no missing groups or outcomes.

## A closer feedback test: the next investment choice

After the contemporaneous findings, a separately [frozen exploratory protocol](empirical/SUCCESSION-PROTOCOL.md) tested one additional link in the same experiment: whether randomly better information at round t changes a person's big-investment choice if externally assigned authority at t+1. The documented role rerandomization makes this eligible selection defensible only if assignments ignore prior accuracy and behavior; it is not endogenous successor selection.

The result is **−0.29 percentage points**, approximate six-session 95% interval **−10.60 to +10.02**, from 342 complete eligible opportunities. No further lag or endpoint was searched. This is inconclusive, not proof of zero effect, and leaves the proposed one-round experience→later maintenance-choice link unsupported at this precision. Immediate improvement cannot be presented as evidence that actors reproduce its enabling conditions. [Full lagged results and limits](empirical/SUCCESSION-RESULTS.md).

## What gap this closes

The work now contains causal intervention evidence in a human institutional setting: changing evidence quality within an implemented authority process affects contemporaneous behavior. The mechanisms after the draw are part of that process. This is evidence against strict behavioral irrelevance of information quality in this specified setting. The additional next-investment test does not demonstrate the reproduction of that benefit.

The paper already studied institutional legitimacy and information effects. Our contribution here is transparent reanalysis with a stated total-effect estimand, no post-treatment rule selection in the primary comparison, conservative session-level reporting, and explicit boundary results. It is not the first discovery that institutional information matters.

Several stronger claims remain untested:

- The apparatus supplying accuracy, enforcement and experimental compensation is externally installed. The dataset does not demonstrate its endogenous renewal, capture resistance or preservation through succession.
- It does not identify how represented goals or new concepts emerge. An immediate compliance change is not evidence that an agent's goals have been durably transformed.
- It does not prove normatively legitimate authority. The selected behavioral outcome and the experimental payoff environment do not settle which real-world practices should be protected.
- It does not identify a shared cross-domain transition model or uniformly bounded transition error.

The earlier [microbial analysis](../closure-study/external-test/RESULTS.md) asked whether current composition improves future biomass prediction under serial passage. That is a different endpoint and design. It contains no matched manipulation of institutional information, authority or legitimacy. Similar qualitative relevance of “context” is insufficient to establish transfer; no common intervention coefficient is estimated here. A genuine bridge requires justified state/event mappings and corresponding interventions, with their predictions tested separately in each domain. Until then, the empirical evidence supports domain-specific components of the framework, not a validated universal mechanism.

## Reproducibility

The [frozen protocol](empirical/PROTOCOL.md), [source URLs, CC0 license and file hashes](empirical/data/provenance.json), [analysis code](empirical/analyze.py), [full results](empirical/results/analysis.json), [session estimates](empirical/results/session_effects.csv), and grouped [Experiment 1](empirical/results/groups_1.csv) / [Experiment 2](empirical/results/groups_2.csv) records are saved. Run `python analyze.py` with NumPy and SciPy. The protocol SHA-256 is `56b47bca7bf364c96e664c9e12ed5071c710fdda6e31a18a67418c3585171219`.

The initial implementation stopped when a descriptive session lacked one comparison cell. The mechanical repair reports that cell as missing and summarizes only estimable descriptive sessions; no primary data, outcomes, models or treatment definitions changed. No additional dataset was sought after the observed primary or boundary results.
