# Developed association and measured ecological retention

8 October 2026, Asia/Bangkok. AI-authored continuation of [The Theory of Evolution](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md).

**A reanalysis of 30 published culture observations supplies a measured constraint on differential continuation. For the day-28 and day-65 snowflake-yeast isolates, the new transfer regimes retained approximately 43% and 49% as many clusters as the old regimes. The day-7 comparison shows no comparable reduction.** This reproduces an existing experimental finding. It advances empirical correspondence for ecological retention; it does not establish a novel biological result, a complete reproductive cycle or comparative superiority of the generative theory.

**已形成的组织能否进入后续活动，必须结合实际筛选关系来说明。三十项培养观察约束了这个连接：改变传代条件，可以明显改变同一分离株的群体留存。其结构如何形成这些差异、留存后如何产生后继，以及支持怎样更新，仍须接成同一历史。**

## The evolutionary connection

The [developmental-association study](DEVELOPMENTAL-ASSOCIATION-INTEGRATION.md) explains how inherited local division forms bonds and reconstructs association. Its state deliberately omits physical shape, fluid interaction and differential survival. The present study tests the next explanatory relationship against measured retention, rather than attaching an unmeasured favorable fitness to association.

The relevant whole includes the developing clusters, liquid, culture conditions, transfer apparatus and the laboratory activity that changes them. Parent, propagule, medium and selector name differentiated relations within that history. Supplying the laboratory protocol to a local model does not put it outside generative reality. Conversely, its actual human-directed alteration must not be relabeled as a demonstrated endogenous evolutionary change of the selector.

## Evidence and protocol

Ratcliff, Pentz and Travisano (2013), [*Tempo and mode of multicellular adaptation in experimentally evolved Saccharomyces cerevisiae*](https://doi.org/10.1111/evo.12101), describes isolates along one evolutionary lineage. Its survival assay used five cultures per old/new regime for each of three isolates. Cultures experienced a growth-and-selection passage followed by further growth before the measured transfer. Cluster counts before and after selection determined retention. These are separate cultures, not paired observations of the same clusters under two treatments. The protocols compared were:

| Isolate day | Old regime | New regime |
|---|---|---|
| 7 | 45 minutes at 1g in the culture tube | 10 seconds at 100g in a microcentrifuge tube |
| 28 | 10 seconds at 100g | 5 minutes at 1g, introduced on day 30 |
| 65 | 5 minutes at 1g | 1.25 minutes at 1g |

Retained material was transferred to fresh medium in the evolution experiment. The article also identifies changes in size and settling efficiency. Our selected main-text reading covers the culture, selection and survival methods and relevant results; it is not a new experiment or full supplementary-data replication.

The [Dryad dataset](https://doi.org/10.5061/dryad.2hr77) supplies the 30 survival values. The retained CSV matches its published 643-byte size and MD5. [Preservation and access record](../../../../sources/evolutionary-selection/ratcliff-2013/README.md) distinguishes the verified original-byte reconstruction, normalized preview transcription and unretrieved tables. The velocity/area preview ends in an incomplete record, so no velocity/area fit uses it.

## Reanalysis

The observation is a culture's fraction of clusters retained by its transfer. It is not a cell-survival fraction, biomass yield, individual cluster probability conditional on measured geometry, or full-cycle reproductive fitness. Each isolate/regime group has five cultures. Isolates along the historical lineage are not independent evolutionary replicates.

| Isolate day | Old mean retention | New mean retention | New / old means | Exploratory bootstrap ratio percentiles |
|---|---:|---:|---:|---:|
| 7 | 3.6768% | 3.8105% | 1.0364 | 0.8113–1.3009 |
| 28 | 6.1058% | 2.6300% | 0.4307 | 0.3300–0.5297 |
| 65 | 2.4689% | 1.2198% | 0.4941 | 0.3988–0.6002 |

The intervals are 2.5th and 97.5th percentiles of 40,000 resamples of cultures separately within each group, with a recorded seed. With five cultures per group they are exploratory sampling summaries; they do not quantify uncertainty across evolutionary lineages or establish guaranteed coverage. The complete results also enumerate all 252 five-versus-five label allocations as a sensitivity calculation. Its inferential interpretation requires exchangeability, and random assignment is not documented in the selected methods. No three-comparison confirmatory claim is made.

Exact means and differences use rational arithmetic. A separately implemented JavaScript checker verifies the published checksum, group sizes, means, contrasts, complete allocation enumeration and holdout losses. Bootstrap percentiles are produced by the reproducible Python calculation; the second implementation checks their form, not their full independent recomputation. [Results](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/survival-results.json) and the [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/verification.json) bind the claims to their inputs and code. These are empirical computations, with no new mathematical theorem or Lean proof claim.

## What the comparison establishes

An exploratory prediction comparison holds out every possible old/new culture pair at each isolate day. Both models receive the same eight training outcomes in each of 25 folds. One uses a common mean, discarding the regime distinction; the other uses separate regime means. The reused holdouts do not become 50 independent cultures.

| Isolate day | Common-rate prediction RMSE | Regime-conditional prediction RMSE |
|---|---:|---:|
| 7 | 0.7974 percentage points | 0.8775 percentage points |
| 28 | 1.8548 percentage points | 0.7157 percentage points |
| 65 | 0.7197 percentage points | 0.3950 percentage points |

Keeping the regime distinction helps prediction in the latter two comparisons and slightly worsens it in the first. Extra distinctions do not automatically improve held-out prediction. This is a diagnostic of a deliberately reduced description. Conventional stratified estimation gives exactly the conditional predictor used here; it receives full credit. The diagnostic is not a comparison against the strongest conventional evolutionary explanation and does not satisfy the full theory's comparative-strength requirement.

The measured difference concerns the whole assay history, including prior conditioning. It cannot isolate an instantaneous sorting effect while holding every cluster's physical state fixed. Nor can separate morphology and retention tables be joined as though they recorded the same identified clusters. Those restrictions govern the next mechanistic model and its validation.

## Consequences for the generative account

An adequate evolutionary account must connect developed association to its relevant physical form, that form and the realized transfer to retained propagules, and those propagules to subsequent development and reproduction. It must also follow how the resources for that development are supplied and changed. The bond-history construction currently represents the first part at a limited resolution. This reanalysis constrains the transfer part. Their conjunction is not yet a calibrated, composed history.

We therefore retain three distinctions in the explanation. Formation of association is different from the physical consequences through which it is retained. Transfer retention is different from later descendant production. Repeated laboratory provision is a real supporting activity whose wider renewal cannot be inferred from the cultures' survival percentages. These are relations within one unfolding, not fundamentally independent organism and environment domains.

For the normative programme, this work tests a premise of the proposed connection between selection and continued generativity. Retention under a protocol does not measure whole generative quality or the ethical validity of an evolved disposition. G0 and additional practical commitments retain their explicit scope. This empirical continuation neither proves nor refutes the universal ethical proposal.

## Substantive self-review

This is the implementing author's counterreview, not independent agent review.

**Could the results merely repeat established biology?** Yes. Reproduction of this published pattern supplies correspondence and a numerical constraint; it is not a discovery of ecological selection. The new repository contribution is a verified data import, reproducible reanalysis, an explicit account of what the existing formal state omits, and a fair comparison boundary.

**Has organization caused the measured survival difference?** The records compare protocols within an isolate, including different conditioning histories. They do not identify a causal geometry-to-survival function. A stronger claim needs linked measurements or a separately tested physical model. Positive survival numbers alone cannot discharge that requirement.

**Does the model defeat a conventional rival?** No. The successful predictor is itself conventional. A rival retaining the same developmental and ecological relations must be tested at that resolution; suppressing its regime information would manufacture an advantage.

**Have renewal and long-term evolutionary prevalence been established?** Neither is identified by this table. The source experiment's medium transfers give an actual recurrence protocol, but the table lacks the descendant and resource records needed to explain that recurrence within the formal history. Cultural, institutional and ethical generalizations require their own correspondences.

## Next decisive test

The next central connection remains **developed structure → physical differential continuation → descendant redevelopment with accounted support**. The evidence now sharpens its acceptance conditions:

1. Obtain complete, identifiable morphology/settling observations or an independent physical dataset, retaining culture and imaging-run nesting. Do not estimate from a truncated preview.
2. Calibrate the physical interaction before testing survival. Include the actual transfer geometry, force, duration and conditioning history; morphology alone cannot silently stand for them.
3. Follow retained propagules through measured descendant production and renewed inputs. Determine which records can actually be joined and keep separately measured quantities separate.
4. Give a conventional developmental/ecological model the same observations, information and support mechanisms. Use independent or prospectively withheld outcomes for a consequential comparison. Agreement narrows the comparative claim; failure revises the proposed mechanism.

The previous goal turn was a status explanation and added no research result. This turn makes empirical progress at a specified connection. The six completion requirements and the full objective remain unchanged and unfinished.
