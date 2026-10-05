# Cue acquisition, beneficiary binding and actual food provision

AI-authored methods audit, 6 October 2026. This supports the named connection **acquired evidence → recipient-specific interpretation → effective, costly delivery** in [generative grounding](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md). It audits an existing experiment; it does not run a new animal experiment or derive evaluative concern from observed helping. The companion [candidate search](REASON-ACTION-EMPIRICAL-CANDIDATES.md) remains unchanged.

**Decision:** Gerber, Schweinfurth and Taborsky's experiment 4 is suitable for a paired reanalysis of a remote cue's effect on local provisioning. It cannot identify correct binding of cue source to beneficiary. Its simultaneous cue and action also cannot establish retained evidence used later. Experiment 3a supplies the relevant temporal separation, under a different treatment comparison. These distinctions should govern what the reanalysis claims before numerical results are inspected.

## Primary evidence and preservation

The [main article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7739497/) is *The smell of cooperation*, DOI `10.1098/rspb.2020.2327`. Its focal subjects were trained female wild-type rats, not food-deprived. Training established tray pulling before the tests. Recorded outcomes were pull count and first-pull latency during seven-minute sessions. Pulling moved food within reach of the nearby animal. Experiment 4's remote odour provider could either help its cage mate or lacked access to its stick. The main results report 23 subjects for experiments 3/4 despite 24 in methods; for experiment 4 they report both count and latency as Wilcoxon tests with `p=.003`. These are reported results, known before the proposed reanalysis, not results produced here. The article also acknowledges not directly measuring general physical activity.

The licensed [supplement](https://doi.org/10.6084/m9.figshare.13213518.v2) is independently retrieved through the public Figshare API and preserved in [the source directory](../../../../sources/27-rat-cue-grounding-2026-10-06/supplement/), with exact PDF/API bytes, a labeled portable text extraction, license and [hash manifest](../../../../sources/27-rat-cue-grounding-2026-10-06/supplement/manifest.json). Figshare declares CC BY 4.0. All ten pages were read as extracted text; pages 4 and 6–9 were additionally rendered and visually checked. The PDF's SHA256 is `cf0ec691c7699fbbadb12e2c06edce4c03fb4ef0ad82717b571b8b2dc9ed1fa4`.

At this audit's design stage, the Dryad file contents have not been inspected by this author. The root and implementation agent separately own retrieval and numerical analysis. Consequently, proposed field names below describe information requirements, not columns asserted to exist.

## Experimental units and contrasts

The following reconstruction uses supplementary Figures S1–S4 and Tables S1–S6. `F` denotes the focal actor, `P` an odour provider, `S` the nearby stooge, and `CM` the provider's cage mate. These are experimental roles, not inferred internal representations.

| Experiment | Assignment and observed unit | Contrast that the design can support | Boundary for the present theory |
|---|---|---|---|
| 1, direct | Each focal rat repeatedly encounters four partner-role × odour-access conditions, with randomized order. The same partner appears in experience and test; four hours separate the phases. An empty-compartment control is also described. Caption `n=23`. | How the effect of assigned partner experience differs with odour access; social-compartment control in its specified condition. | Partner identity, prior provision and received cues require separate causal interpretation; no independently crossed cue-source/recipient identity manipulation. |
| 1, generalized | Three experience partners on successive days; a fourth partner at test. Caption `n=21`. Role × odour access again varies. | Provision toward a new recipient following the assigned experience history. | Already accommodates responses extending beyond the individual source of earlier provision. Do not pool with the direct schedule as identical replications. |
| 2 | Four repeated conditions cross cooperative/non-cooperative partner role with odour present in experience only or test only. Three experience days precede a fourth-day test. Randomized order; `n=23`. | Role contrast within each cue-timing condition, and their interaction. | It does not cross each cue timing independently with both absence and presence of the other timing within this experiment. |
| 3a | Remote `P` cooperates or does not; local `S` does not provide help. Odour arrives during a seven-minute experience phase; after a diagrammed one-minute interval, `F` can provision `S` for seven minutes without that odour stream. Two randomized conditions; caption `n=24`. | Difference in subsequent local provision following different remote cue exposure. | A retained effect is testable; a learned recipient-specific proposition is not uniquely identified. Persistent arousal or an associative state remains possible. |
| 3b | No experience phase; remote cue arrives during the seven-minute test while `F` can provision local `S`. Two randomized conditions; caption `n=24`. | Concurrent remote-cue contrast in local provision. | Does not identify memory retention or a recipient-specific interpretation. |
| 4 | Same remote `P` in helping versus neutral situations, with randomized order for each focal animal. Figure S4 explicitly depicts **test phase only**, seven minutes. `F→S` food route and `P→CM` food route remain distinct; caption `n=24`. | Within-focal response to a changed situation of the same odour provider. | Rules out a fixed provider-identity-only explanation of this contrast, conditional on assignment and implementation; it does not isolate helping from every state/activity difference. |

The repeated unit is the **focal animal**, with sessions nested within it. Individual pulls within a session are outcomes, not independently assigned experimental units. The main article says experiments 1/2 and 3/4 use different batches. Cross-experiment identities must therefore be namespaced and verified rather than automatically merged or assumed independent.

The supplementary S1 caption places the empty-compartment control in direct reciprocity, consistent with the main methods. The small S1 treatment-grid label instead says generalized reciprocity. This labeling discrepancy should be preserved if experiment 1 is analyzed; the raw field definitions must decide actual membership. It does not affect the primary experiment-4 contrast.

## Reporting discrepancies that the reanalysis must retain

Table S6 reports the count comparison as Wilcoxon `V=27, p=.003`, consistent with the main count result. Its latency result is instead a Cox model: neutral-minus-cooperative coefficient `−.695`, standard error `.352`, chi-square `3.9`, `p=.048`. This differs in both method and probability from the main article's latency statement. Both were visually checked; do not silently substitute either version for the other.

For experiment 3, Table S5 reports count `p=.197` in the experience-only condition and `.022` in the concurrent condition, while latency Cox probabilities are `.013` and `.057`. Endpoint-specific evidence is therefore already known before reanalysis. Choosing the favorable endpoint separately in each experiment and presenting the collection as uniformly positive replications would be misleading.

Sample-size declarations also need reconciliation. Figures S3/S4 and Table S1 say 24; the main results say 23. Neither source inspected here supplies an exclusion explanation. Retain every documented valid pair under a declared data rule, report exclusions and incomplete pairs, and do not drop a subject merely to reproduce a published probability.

## What the experiment identifies, and what remains equivalent

Let `O` be the assigned situation of the remote odour provider, `I` its identity, `R` the local recipient, and `Y` local provisioning. Experiment 4 compares `Y(O=helping)` with `Y(O=neutral)` while holding the provider's identity constant within its paired comparison. A successful contrast establishes sensitivity to something changed by that assignment. It cannot, by itself, say which chemical component changed or what the focal animal represents.

This interpretation needs no claim that the focal animal makes an identity error. The cue can be informative about an event at the remote source and still cause an identity-independent increase in local provision. A correct belief about `P` followed by generalized helping, a conditioned response to the odour stream, and misattribution to `S` can predict the same recorded outcome. The design supplies no choice between recipients with independently varied identity histories that distinguishes these possibilities.

Simple strong comparators are therefore:

1. **Cue-potentiated provision:** a learned or immediate odour response increases pulling whenever a social recipient is present. No recipient-indexed proposition is required.
2. **Generalized reciprocity or generalized social readiness:** source-associated experience changes willingness to help another individual. This can be compatible with accurate source recognition.
3. **Activity or state response:** odour associated with the provider's available action, arousal or related state alters focal pulling. Experiment 4's no-stick condition does not match these variables by design.
4. **Recipient-indexed inference plus action:** the focal animal interprets evidence about a particular beneficiary and selects an effective command for it. This remains a hypothesis needing a discriminating manipulation, rather than the default explanation of an increased count.

Supplementary Figure S6 reports a pooled correlation of provider and focal pull counts (`N=159`, `r=.014`, `p=.88`). This is a useful reported null association under those sampled conditions. It does not independently manipulate activity, establish equal activity across conditions, identify a chemical component, or demonstrate the absence of a threshold/nonlinear response. A failure to find that correlation cannot make comparator 3 impossible.

No measured force gradient, mechanical displacement or calorimetry is supplied by these outcome variables. Performed pulling is an actual action, but an abstract fuel debit cannot be quantitatively inferred from the count. Accessible food, ingestion, physiological benefit and longer-term renewal also remain separate outcomes. Combining this dataset with a separate cost experiment does not create observations of a joint cost × cue-validity × recipient-identity intervention.

## Reanalysis contract before numerical inspection

This is a **retrospective, design-informed reanalysis**, not an outcome-blind preregistration: the published count result and its probability are already known. Its purpose is to expose unit structure, reproduce a transparent contrast and test how far the evidence reaches.

For experiment 4, let `C_i` and `N_i` be subject `i`'s count under the cooperative and neutral provider situations. The primary transparent estimate is `mean_i(C_i−N_i)` over all documented complete pairs. Also report median paired difference, each direction's subject count, zero differences, raw paired outcomes, and a subject-level bootstrap interval. Each resample selects complete animals with all their conditions. Do not resample individual pulls or fit a population-wide effect whose only replication is the number of pulls.

A paired sign-flip calculation can be supplied as a clearly labeled sensitivity analysis. Randomized order is documented, but the actual allocation probabilities, balance restrictions and sequence identifiers may not be recoverable. Without that information, independent equiprobable flips are an **assumption**, not a reconstructed exact randomization distribution. Period effects, interference through reused partners and carryover deserve separate sensitivity treatment. The treatment comparison cannot be made assignment-exact merely by calling a software routine exact.

First-pull latency is secondary. Required information is the observation horizon, units, actual first-event indicator and coding of no-pull sessions. If a session with no pull is recorded at the horizon, that observation is right-censored for event-time analysis, not a measured pull at that instant. A bounded endpoint `min(T,420)` is different: it intentionally measures waiting time accumulated within the seven-minute session and can equal 420 when no event occurs. Report it as capped waiting, not uncensored first-pull time. Analyze neither endpoint until the coding is checked against count and documentation; do not infer an event indicator from the latency alone at the boundary.

The audit should enumerate:

- original file hashes, delimiter, column names, treatment labels and units;
- unique focal IDs, condition counts per ID, duplicate keys, missing outcomes and all exclusion decisions;
- any treatment-order, date, provider, recipient or cage IDs actually supplied;
- zero-count rows, corresponding latency values, out-of-range times and contradictory combinations;
- whether 24 subjects form complete pairs, and whether a documented rule explains the published 23;
- the limited family of primary/secondary estimates, disclosed analytical choices, and any failure to reproduce published values.

If experiment 3a is added, keep its contrast separate and report why it is being added: it concerns persistence after cue removal, while experiment 4 concerns contemporaneous exposure with fixed provider identity. Cross-experiment magnitude comparisons require their differing schedules and samples to remain explicit. A null or imprecise reanalysis would revise confidence in the cue effect; it would not, by itself, establish recipient binding.

## The next discriminating connection

The present evidence can advance the foundation by challenging a shortcut: **external cue → helpful output does not uniquely identify external cue → warranted recipient-specific interpretation → helpful output**. Removing that shortcut improves the proposed account even when the observed behavior is favorable.

A discriminating future design would need independently varied source identity, beneficiary identity, current evidence validity and action efficacy, with at least two possible beneficiaries or commands. Preserving identical cues while rerouting actual delivery would distinguish a policy attached to a signal from one tracking the affected center and effective means. Separating observation, delay and later choice would test retained use. Matched activity controls would test the simpler state-response explanation. Such requirements are identification criteria, not a request to conduct an animal experiment.

What would change the account is evidence that a simple cue response explains the full measured behavior equally well, or that animals track actual recipient consequences across cue/source/action mismatch. The former limits how much cognition can be inferred from provisioning; the latter would support a stronger behavioral bridge. Neither alone supplies moral justification, derivation of the training history, universal concern, or a completed alignment/governance solution.
