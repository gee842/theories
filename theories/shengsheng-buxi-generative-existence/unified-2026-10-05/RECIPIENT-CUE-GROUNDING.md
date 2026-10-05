# External social cues and recipient-directed action

AI-authored research, 6 October 2026. This study follows Ren's [clarification](../../../sources/15-codex-theory-conversations/2026-10-06-alignment-governance-and-future.md) that external integration is needed for cognition even before an actor thinks about what lies beyond its boundary. It supports the transition **external information → interpretation of an affected center → effective action** in [generative grounding](GENERATIVE-GROUNDING.md). It is a retrospective reanalysis of published observations, not a new animal experiment, a test of the whole foundation or an established AI-alignment solution.

**Result:** the displayed experiment-4 data contain a stable positive paired difference in food-access actions between two remote-donor conditions. All 24 available focal animals are retained; every single-animal omission preserves a positive mean difference. This supports a bounded external-cue/action connection. It does not identify a recipient-specific representation, future-oriented concern or warranted practical reasons. The same observable behavior admits several mechanisms. The useful advance is therefore both empirical and restrictive: external context affects provision in this apparatus, while provision alone cannot establish the stronger cognitive and normative connection.

## The source and what was actually analyzed

Gerber, Schweinfurth and Taborsky's 2020 study, [*The smell of cooperation*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7739497/), manipulates odor access in a rat food-provisioning apparatus. In experiment 4, a focal rat can pull a tray to make food accessible to a nearby rat. Meanwhile it receives odor from a different room. The same remote donor is tested in a cooperating situation, where it can pull for its cage mate, and a neutral situation without access to the pulling stick. Cue delivery and focal action occur together. The [supplement](../../../sources/27-rat-cue-grounding-2026-10-06/supplement/rspb20202327_si_001.pdf), Figure S4, documents randomized condition order and 24 planned focal rats.

| Role | What the experiment supplies or observes |
|---|---|
| Remote donor | Same donor identity across the paired situations; changed pulling opportunity and associated state |
| Focal actor | Trained pulling response; repeated measurement in the two conditions |
| Local recipient | The sole nearby beneficiary of focal pulling, distinct from the odor donor |
| Outcome | Number of food-access pulls during seven minutes |
| Unmeasured continuation | Ingestion, physiological benefit, sustained renewal and preservation of a future |

The [Dryad deposit](https://datadryad.org/dataset/doi:10.5061/dryad.h18931zjd) lists original CSV files, but our download attempts did not retrieve those bytes. A parallel study preserved all 48 data rows of the displayed experiment-4 preview as a [derived TSV](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/experiment4-preview.tsv). The root independently read the visible browser cells and matched its canonical fingerprint. That validates this transcription against the display; it does not authenticate the display against the original CSV or prove original-file completeness. Exact source boundaries, licenses and hashes are in [source record 27](../../../sources/27-rat-cue-grounding-2026-10-06/README.md).

The paper's results say n=23, while the methods, supplement and displayed table indicate 24 planned/available pairs. This is an unexplained sample-size discrepancy: an exclusion, reporting error or version difference has not been established as its cause. We retain all pairs and show every possible single-animal omission. None is chosen to reproduce the publication. This is not a replication of its fitted analyses.

The [computational plan](../../../experiments/recipient-cue-grounding/PROTOCOL.md) was frozen before these new calculations, but after the published findings and a parallel study's descriptive totals were known. It is explicitly retrospective, not preregistered or outcome-blind. Its limited scope was also reviewed before execution. Experiment 3's displayed preview was truncated, so it was not treated as a complete dataset.

## Paired results and their assumptions

The animal is the unit; repeated pulls are not independent replications. Define each difference as cooperating-donor count minus neutral-donor count. The [executable analysis](../../../experiments/recipient-cue-grounding/README.md) retains all source strings, zero counts and explicit missing timing values.

| Quantity | Result |
|---|---:|
| Complete focal-animal pairs | 24 |
| Neutral / cooperating total pulls | 21 / 53 |
| Neutral / cooperating mean pulls | 0.875 / 2.2083 |
| Mean paired difference | +1.3333 pulls per session |
| Median paired difference | +1 pull |
| Animals with more / fewer / equal pulls | 17 / 4 / 3 |
| Exploratory paired percentile bootstrap interval | +0.6667 to +2.0000 |
| Mean difference across all 24 single-animal omissions | +1.1739 to +1.4783 |

The bootstrap uses 20,000 complete-animal resamples with a fixed seed. Its population interpretation assumes approximately independent comparable animal units. The preview lacks donor and recipient identifiers, treatment sequence and session dates; shared influences, donor reuse, carryover and period effects cannot be estimated from these columns. The interval does not correct historical study selection or multiple endpoints.

Two assumption-conditional reference calculations are preserved, rather than used as acceptance thresholds. Equiprobable independent paired sign flips yield a two-sided tail count of 24,496 / 16,777,216, about .001460. The conditional binomial sign calculation among the 21 nonties yields 15,094 / 2,097,152, about .007197. The sign-flip probabilities across all omissions range from .000351 to .002918. These are exact arithmetic under specified reference assumptions, **not recovered assignment-exact probabilities**: the original assignment probabilities and restrictions are unavailable. Sign symmetry or corresponding randomization assumptions are stronger than a bare zero-mean null.

The [independent checker](../../../experiments/recipient-cue-grounding/check_analysis.py) reads the preserved TSV separately. It counts half-sequences of signs and uses sorted searches, instead of the analysis program's dynamic programming; it also independently reconstructs paired arithmetic and the declared bootstrap. [Its receipt](../../../experiments/recipient-cue-grounding/independent-verification.json) checks all 48 rows, 24 pairs, 24 omissions and 50 exact reference calculations. Agreement validates those computations, not their sampling or causal assumptions.

Latency receives a coding audit only. All 14 zero-pull rows display 420 for first-pull latency; these are not counted as observed events at that instant. Two later-timing cells contain `NA` and remain missing. The main article reports latency Wilcoxon p=.003, whereas supplementary Table S6 reports Cox p=.048. This methodological/reporting discrepancy remains unresolved. No latency effect or survival-model replication is claimed.

Related published contrasts are not silently converted into uniformly favorable evidence. Supplementary Table S5 reports experiment-3 count probabilities of .197 for experience-only odor and .022 for concurrent odor; its latency probabilities differ again. Those are source reports, not our calculations. The [methods audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CUE-GROUNDING-METHODS.md) preserves their different timing, endpoints and remaining interpretations.

## What helpful action does not identify

The cue source and beneficiary are physically distinct. That does not prove the focal animal confused them. A response could correctly track a remote cooperative event while increasing help toward another animal. Cue potentiation, generalized reciprocity, associative state changes and a richer recipient model remain compatible with the measured count contrast. No alternative beneficiary is available to reveal whether the animal selects among recipients by their independently varied histories or needs.

Holding donor identity constant constrains an identity-only account of the paired difference. It does not isolate a cooperation-specific chemical signal from activity, arousal or other consequences of having access to the stick. Supplementary Figure S6's pooled null correlation between provider and focal pulling does not experimentally match all those alternatives or identify the active chemical cause. Likewise, an apparatus-imposed noncooperator label in related experiments does not establish voluntary refusal or hostile intention.

There is a simple identification result behind this caution. Let O be observed cue condition, H the complete observed past, Y the next measured action, and R a hidden recipient representation. Any richer model induces an observable kernel

\[
K(y\mid o,h)=\sum_r P(y\mid o,h,r)P(r\mid o,h),
\]

with an integral replacing the sum when needed. This is defined on positive-probability observed contexts; choose arbitrary values off that support. A descriptive response process using the same K has the same conditional distribution of Y. If H contains the full observed past across relevant units and the same observed assignment law is retained, multiplying the successive conditional kernels reproduces the whole observed joint law as well. A current-trial marginal alone would not suffice for that stronger repeated-data statement.

Consequently, these observations cannot by themselves distinguish the hidden representational explanation from a saturated observable response description. This is an existence argument, not a fitted alternative or proof that a simple memoryless mechanism explains the animals. It does not imply that recipient understanding is absent, that every form of concern requires explicit representation, or that equivalence persists under new source/beneficiary interventions. It identifies the extra evidence required before inferring the stronger mechanism.

## Consequence for the foundation and alignment research

Ren's clarification distinguishes actual external integration from consciously recognizing that integration. This experiment provides a concrete, limited case in which a distant social condition changes local provision. Conscious recognition is unmeasured. A cue intervention of this kind neither proves nor refutes the general constitutive necessity claim about cognition; it tests one informational route within an already trained, externally supported organism.

Three connections therefore remain distinct:

1. **External conditions enter action regulation.** The paired observations support sensitivity to the assigned donor situation in this apparatus, conditional on its implementation and design assumptions.
2. **Evidence tracks the relevant affected center and effective means.** This requires discriminating behavior under changes to cue source, beneficiary and delivery consequences. More helpful actions under a fixed arrangement are insufficient to establish it.
3. **Those consequences warrant and sustain concern.** A valid reason, motivation to act, available resources, legitimate authority and actual beneficiary outcomes remain separate explanatory obligations. Their relation is the continuing research problem, not a label attached to pull counts.

The [semantic calibration study](SEMANTIC-CALIBRATION.md) supplies a parallel formal lesson: agreement after overwriting an acquired anchor cannot independently warrant the claim used to overwrite it. The present empirical study adds a different limit: even accurately measured helping cannot by itself identify what the actor understands. Neither result substitutes for a paid physical evidence/action join or justifies a supplied support objective.

The next discriminating interface is **independently acquired source information → preserved beneficiary identity → effective delivery under mismatch and change**. A useful empirical design would independently vary source and beneficiary histories, permit meaningful alternative beneficiaries, separate cue acquisition from later action when testing retention, match competing activity/state explanations, and measure delivery separately from recipient consequences. These are identification requirements; no such new experiment was conducted here. In a learned-AI test, analogous interventions would have to keep information and action opportunities comparable across strong simpler policies, and evaluate consequences separately from favorable descriptions or evaluator scores.

A stable effect that disappears when these alternatives are controlled would narrow the causal account. Successful transfer across independently varied source, beneficiary and delivery conditions would support a stronger functional bridge, without uniquely establishing an internal representation or supplying ethical authority. The full [alignment completion requirements](ALIGNMENT-COMPLETION.md) remain active. This round contributes empirical constraint, an explicit nonidentification argument and reproducible secondary arithmetic; it introduces no new Lean proof, new animal study or demonstrated governance solution.

## Research record

- [Frozen protocol and analysis](../../../experiments/recipient-cue-grounding/README.md), including complete paired outcomes and sensitivity family.
- [Methods and comparator audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CUE-GROUNDING-METHODS.md).
- [Independent interpretation and implementation review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CUE-GROUNDING-REVIEW.md), preserving the original review contract and subsequent findings.
- [Source originals and preview provenance](../../../sources/27-rat-cue-grounding-2026-10-06/README.md).
- [Integration receipt](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CUE-GROUNDING-INTEGRATION.json).
