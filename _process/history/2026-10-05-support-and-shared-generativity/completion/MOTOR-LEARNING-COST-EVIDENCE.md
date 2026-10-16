# Cost-sensitive adaptation and the updater-identification boundary

6 October 2026. AI-authored empirical audit for Ren's generative-grounding program. The addressed transition is **consequence-sensitive behavior → changed learning → empirical identification of a retained operative updater**. This study performs a bounded analysis of public human data; it does not treat that data as validation of the repository's complete physical route-revision construction.

The [preceding comparator audit](ROUTE-REVISION-COMPARATORS.md) established why configuration changes, operative update-class changes and productive retention are distinct in the finite model. Here the external evidence lacks a directly measured route variable. The analysis therefore starts from observable responses and asks how far they support the proposed connection.

## 1. Source and prospective boundary

Sedaghat-Nejad and Shadmehr's [2021 primary article](https://www.pnas.org/doi/10.1073/pnas.2101717118) studies corrective saccades that consume time available for a motion judgment. Coherence changes the consequences of lost viewing time. EXP2 exchanges both side/coherence assignments at trial 951; EXP1 retains its assignments. A separate control removes the viewing-time competition. The reported state-space modeling distinguishes retention and error sensitivity, subject to its model assumptions. This is an opportunity-cost manipulation, not a measurement of metabolic reserves or the material cost of changing a learning mechanism.

We preserve the original public [OSF workbook and metadata](../../../../sources/29-motor-learning-cost-2026-10-06/README.md), including exact bytes, request URLs, dates and hashes. Workbook SHA256 is `0cd6ae5b0f159531f2442f49a474c5ecfda23a1fcf0965598da99df5d84891cc`. It contains participant-level binned adaptation and decision series, not raw trial events. Listed stimulus/filter code and large MATLAB fit files were not downloaded or analyzed. The article is linked, not republished; no license or extra data content is inferred from public access.

The [retrospective protocol](../../../../experiments/motor-learning-cost/PROTOCOL.md) was fixed before our numerical contrasts but after the source's conclusions were known. It is not a preregistration. Its original adjacent nine-bin proposal remains in [development](../../../../experiments/motor-learning-cost/development/PROTOCOL-before-boundary-guard.md). Before calculation, metadata review introduced a 20-trial center guard, yielding 8/8/9 bins in pre/early/late windows. Another precomputation correction removed an erroneous suggestion that the opposite side was untreated: both sides switch. Neither amendment followed outcome inspection.

## 2. What the workbook identifies securely

The `ADAPTATION` sheet provides two literal series, `LARGE COST` and `SMALL COST`, for each of EXP1 and EXP2, with 20 IDs per series. We pair within each cohort and retain literal series names. Identical ID numerals across cohorts do not establish repeated participants. Data cells remain traceable in the [extraction](../../../../experiments/motor-learning-cost/extracted.json).

The primary observation is a difference of changes in those source series. Let \(\bar Y_{icw}\) average the available bins for participant \(i\), literal series \(c\), and window \(w\). Then

\[
C_{iw}=(\bar Y_{i,\mathrm{SMALL},w}-\bar Y_{i,\mathrm{SMALL},\mathrm{pre}})
 -(\bar Y_{i,\mathrm{LARGE},w}-\bar Y_{i,\mathrm{LARGE},\mathrm{pre}}).
\]

Windows are fixed by the workbook's **mean trial coordinates**, not unreported raw bin edges: pre 801–931 (AZ:BG), early 971–1100 (BJ:BQ), late 1101–1250 (BR:BZ). Equal-weight bin averages are not exact trial-weighted epoch means. A guard band reduces proximity to the switch but cannot prove that no constituent raw trial crosses it. The analysis checks 2,000 finite cells and 40 paired participants; it excludes and imputes none.

Reading the EXP2 series as fixed *initial physical sides* makes \(C\) an opposed-switch contrast: initially cheap becomes costly and initially costly becomes cheap. **That reading is conditional.** Public labels and the published design do not independently supply raw side tags or an explicit post-switch grouping dictionary. If data were regrouped by current condition, the same arithmetic would remain a valid literal-series contrast but would not track the same physical-side histories. Continuity or the expected sign cannot settle this labeling question. Within-series subtraction removes a fixed baseline offset; it cannot repair a changed series identity.

## 3. Fixed results, including the uncertain primary

Source amplitude sign is retained: more negative change corresponds to greater gain-down adaptation. Values are degrees; intervals are two-sided 95% sampling-model intervals.

| Contrast | Mean | 95% interval | Design status |
|---|---:|---:|---|
| EXP2 early | −0.181722 | [−0.453318, 0.089873] | **Primary**, 20 paired participants |
| EXP2 late | −0.340414 | [−0.593631, −0.087197] | Secondary, same 20 participants |
| EXP1 early | 0.206334 | [−0.015941, 0.428609] | Secondary no-switch cohort |
| EXP1 late | 0.252509 | [−0.029550, 0.534569] | Secondary no-switch cohort |
| EXP2 minus EXP1, early | −0.388056 | [−0.727942, −0.048171] | Secondary, independent cohorts |
| EXP2 minus EXP1, late | −0.592923 | [−0.959680, −0.226166] | Secondary, independent cohorts |

For the primary, the SMALL series changes by −0.398970° and LARGE by −0.217248°. Their paired difference points in the expected opposed-switch direction under the conditional label mapping, but its interval includes zero. The later contrast and cohort differences are more separated from zero under the stated models. They remain secondary; the study has not replaced the uncertain primary with a selected stronger result.

These intervals use participant-level variability, not bins as independent subjects. Within-cohort intervals are Student-t with 19 degrees of freedom; between-cohort intervals use Welch–Satterthwaite. They describe sampling uncertainty under those models. They do not settle cohort exchangeability, carryover, labeling, internal error encoding or mechanism. The EXP2–EXP1 comparison is descriptive; identifying a causal difference of differences requires counterfactual assumptions not established by this workbook.

The [producer](../../../../experiments/motor-learning-cost/analyze.py) uses `openpyxl` and independently inverted Student-t CDFs. The separate [XML estimator](../../../../experiments/motor-learning-cost/independent_check.py) was fixed before inspecting producer outputs. [Results](../../../../experiments/motor-learning-cost/results.json) retain all participant and component contrasts. Source hashes and the [producer receipt](../../../../experiments/motor-learning-cost/verification.json) confirm no workbook mutation. The [independent comparison](../../../../experiments/motor-learning-cost/independent-verification.json) passes: 2,000 source values, 2,000 coordinate occurrences, 240 means, 160 component changes, 80 participant contrasts and 112 aggregate fields agree, with maximum absolute discrepancy 7.1×10⁻¹⁵. The [scientific figure](../../../../experiments/motor-learning-cost/paired-contrasts.png) displays all fixed contrasts. The [independent scope review](MOTOR-LEARNING-COST-REVIEW.md) accepts the bounded source-series analysis and its identification limits. Independent arithmetic agreement is not a causal identification result.

## 4. What changed in the evidence account

This is actual external data rather than another favorable finite construction. It supplies a reproducible observation of different source-series trajectories across a cost-switch design, with an uncertain prespecified early within-cohort contrast and stronger fixed secondary contrasts. It gives a bounded empirical test of the proposed dependence of adaptation on consequences. The remaining uncertainty is part of the finding, not an unfinished search for a favorable window.

It does **not** reproduce the paper's trial-level sensitivity fits, estimate a biological update kernel from raw errors, or show that an acquired component replaced its own updater. The public bins do not expose internal teaching input, completed write opportunities, hidden memory decomposition or a candidate material learning-rule state. The source's retention controls constrain some explanations; nonsignificant retention contrasts do not prove equality. Changing task coherence also changes sensory demands and consequences, so our contrast is not a measured isolated resource effect.

The [companion identification note](UPDATER-IDENTIFICATION-MATH.md) supplies precise alternatives. A condition-dependent gain \(b(C)e\) can be pathwise identical to a fixed gain \(\beta\) receiving encoded input \(b(C)e/\beta\). Matching geometric errors or externally clamping them does not by itself match internal evidence. A stochastic writing gate can reproduce a conditional mean gain while differing in variance, and hidden fast/slow memory can match current output yet diverge later. These are logical countermodels, not claims about the participants' actual physiology.

Nor does the fixed augmented-state representation make operative updater revision incoherent. A retained route can change its causal role under one unchanged physical law, as in the repository's construction. The empirical question is which retained organization was changed, by what mechanism and at what interface—not whether nature replaced its fundamental law.

## 5. Observable discriminator and next evidence requirement

The next stronger result would identify a retained candidate component longitudinally in the same continuing carrier, then intervene on or rescue it while matching the relevant memory, delivered teaching signal, writable opportunity and later readout. Record incomplete updates and resource/timing costs rather than conditioning them away. A changed next-memory response under those controls would distinguish operative update classes at that interface. Mere persistence after restoring common task conditions still permits retained context memory; equal output does not prove equal latent memory.

For this dataset, an author-supplied grouping dictionary or raw side-tagged trial export would first settle whether the literal series track fixed physical sides. Raw error and timing records could support a declared sensitivity/retention reanalysis and test some distributional gate alternatives. They would still not by themselves locate a retained physical updater. A selective component intervention, adequate input/write calibration and exclusion of direct readout effects would address that further claim.

Evidence of a cost effect on delivered input, write availability or action expression would revise the attribution while preserving the broader consequence-sensitive adaptation observation. A well-controlled component intervention with no subsequent update difference would weaken that component's proposed causal role at the tested interface. Neither outcome would establish or refute universal favorable direction. This round advances empirical identification and exposes its limits; formation of the relevant sensing, calibration, mechanism and retention remains an open part of the unified derivation.
