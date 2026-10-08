# Actual change bounds and response tolerances

8 October 2026. AI-authored continuation of [Ren's request to finish the remaining work](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md). This assesses the empirical premise left by [changing dependency](CHANGING-DEPENDENCY-INTEGRATION.md); it does not replace the broader biological completion request with a temperature example.

**Result:** the available-data test is complete, with a negative outcome for the tested certification route. Calibration-period maxima do not always bound later readout changes. Every tested uncertainty interval is wider than the source controller's final ±0.2°C target band. Moreover, that band is a soft optimization target, not a validated limit on true-temperature error or harm. The remaining empirical validation is therefore **not complete**. Its missing measurements cannot be supplied by another conditional proof.

**中文结论：** 已完成现有记录所能支持的变化界、目标含义、留出检验及数值复核。旧数据的最大变化率在两个通道的后段被突破；跨记录迁移也保留失败。所试区间均宽于控制器设定的目标带。这里得到的是对这一认证办法的实际否定结果，不是所有控制都不可能，也不是整个细胞—器官—身体—生态循环已经验证。新增经验计算不计作新 Lean 定理。

## 1. Connection being tested

The derivation is organization and retained effects → acquired description → consequential prediction → feasible response. The previous Lean result states exactly what follows **if** acquisition error, subsequent change and response correspondence have warranted bounds. This study tests whether the retained empirical records supply those premises.

Heating, sensing, retained readings, computation and commands are differentiated operations within one material history. The split between calibration and test observations separates evidential roles within that history; it does not introduce an independent observer/world ontology. The archive records sensor readouts and commands, omitting parts of the acquisition and thermal history. We distinguish that representational omission from the observed failure of a particular envelope.

No favorable ethical direction follows from meeting a controller target. The contribution to normative inquiry is an implementation requirement: justified practical claims must keep actual consequences, uncertainty and the warrant for a target connected. G0 and substantive ethical comparisons remain in their own argument.

## 2. Fixed analysis and reproducibility

The [analysis plan](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/BOUND-CALIBRATION-PLAN.md) was saved before this analysis's rates and outcomes were computed. Earlier studies had examined the same archives, so this is an exploratory analysis, not external preregistration or an untouched dataset.

Use three distinct Summary MPC runs from the [preserved TCLab benchmark](../../../../sources/tclab-benchmark/README.md). All eleven source members match [the existing timing manifest](../../../../sources/tclab-benchmark/TIMING-PROVENANCE.json). Duplicate Physics/ANN files are not replications. Exclude initialization row zero and the known unacquired ARX terminal row. The acquired/calibration/test counts are Physics 299/149/150, ARX 599/299/300 and ANN 299/149/150.

For each run and each temperature channel, freeze the maximum and nearest-rank 95th percentile of consecutive absolute readout change divided by elapsed recorded time in the first half. Predict a later readout by retaining the origin reading, with radius equal to the frozen rate times elapsed time. Test lags of 1, 2 and 5 acquired observations, with both endpoints entirely in the second half. Also transfer Physics calibration rates to the ARX and ANN test partitions. The calendar ordering of different runs is not established; only within-run tests are chronologically later than their calibration.

The [producer](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_bound_calibration.py) uses exact rational arithmetic on the archived decimal strings. The [separate checker](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/check_bound_calibration.py) independently parses the source and uses 80-digit Decimal arithmetic, checking rates, interval membership, uniqueness, expected counts and summaries. Three perturbations of test readings leave calibration rates unchanged. Results preserve [all 12,440 interval evaluations](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/bound-calibration-intervals.csv), [60 grouped summaries](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/bound-calibration-results.json), and the [passing computation receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/bound-calibration-checks.json). The same agent wrote both implementations; this is not independent-agent review or new physical replication.

## 3. Outcomes that constrain the account

One-observation lag, each run's own calibration maximum:

| Run | Channel | Tested intervals | Bound violations | Frozen rate, °C/s | Median radius, °C | Largest excess, °C |
|---|---|---:|---:|---:|---:|---:|
| Physics | T1 | 149 | 0 | 0.483675 | 0.971232 | 0 |
| Physics | T2 | 149 | 0 | 0.418227 | 0.839811 | 0 |
| ARX | T1 | 299 | 0 | 0.740174 | 0.740960 | 0 |
| ARX | T2 | 299 | 1 | 0.918183 | 0.919159 | 0.119709 |
| ANN | T1 | 149 | 0 | 0.483835 | 0.972021 | 0 |
| ANN | T2 | 149 | 1 | 0.324753 | 0.652427 | 0.056744 |

With Physics maxima transferred to ARX, T1 has 3/299 violations and T2 has 16/299, the latter reaching 0.615368°C beyond the interval. Physics-to-ANN transfer has no one-lag violations in either channel. Neither outcome establishes transfer to arbitrary changed conditions. With each run's own 95th-percentile envelope, one-lag violations are 0/149 and 3/149 for Physics, 5/299 and 14/299 for ARX, and 0/149 and 2/149 for ANN. A calibration percentile is not automatically future coverage at that percentage.

Across all 12,440 evaluations, including both envelope choices, all lags and transfers, **zero radii are at most 0.2°C**. Thus none of these symmetric retained-reading intervals fits wholly inside a band of total width 0.4°C. This is a width diagnostic; zero certificates does not imply zero actual readings inside the target band. Intervals overlap and observations are serially dependent, so these counts are not 12,440 independent trials and receive no binomial confidence interval.

## 4. Primary-source assessment: what the target means

The archived Physics script sets `DT = 0.2` at line 167, ANN at line 263, and ARX sets `db1`/`db2 = 0.2` at lines 164/168. These values set upper/lower desired temperatures. The retained [paper](../../../../sources/tclab-benchmark/CACE_2020_Preprint.pdf), PDF pages 22–23, equation 13, penalizes slack outside that band and describes a reference trajectory. It therefore corroborates a soft objective, including temporary approach to a changed setpoint. The analysis's band-containment columns concern the final setpoint band, not a reconstruction of the full internal reference trajectory. [Author-hosted paper](https://apm.byu.edu/prism/uploads/Members/2020_park_tclab.pdf).

Current [GEKKO tuning documentation](https://gekko.readthedocs.io/en/latest/tuning_params.html) likewise describes SPHI/SPLO as the range for the L1 error objective and WSPHI/WSPLO as penalties. This is a corroborating current reading, not verification of the historical installed solver version. The archived code and paper carry the historical inference.

The paper identifies TMP36GZ sensors on PDF page 4. The manufacturer's [TMP35/36/37 Rev. H datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf), Table 1 on printed page 3, distinguishes typical accuracy from grade-specific maxima: for G grade, ±3°C maximum at 25°C and ±4°C over the specified range under stated conditions, excluding self-heating errors. These are component specifications, not measured errors in these particular units. They neither validate the full sensor/ADC/acquisition chain nor rule out better relative precision or calibration. The archive supplies no traceable reference comparison establishing ±0.2°C true-temperature accuracy. Manufacturer and GEKKO readings are link-only; no external publication bytes have been imported this round.

## 5. Substantive counterreview and scope

1. **The tested predictor discards thermal dynamics.** Ordinary model-based prediction may yield tighter residual bounds than retaining the last reading. The outcome rejects this tested route to a certificate; it does not refute predictive control or the relational account. Existing [feedback correspondence](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md) already preserved held-out residual-bound failures; this extension connects a separately fixed change envelope to the source target, rather than treating that general warning as new.
2. **Observed changes combine process change and readout variation.** They are not a bound on the continuous physical temperature derivative. Commands in the test history are the original closed-loop commands. This is not an experiment in omitting sensing, changing control, or applying the earlier additive correction rule to a heater.
3. **Timestamps do not identify every hardware delay.** The existing source-order audit constrains ordering but does not recover hardware acquisition instants. Rate units use the logged clock; no exact physical record-expiry time is claimed.
4. **A finite maximum has limited evidential scope.** Within-run violations directly reject these candidate envelopes as bounds for the retained test observations. Successful cases do not independently warrant a hard bound on every future history. No post-test inflation or removal of inconvenient observations is used.
5. **Targets require their own grounds.** Source code establishes the chosen engineering objective. It does not establish physiological safety, acceptable loss, or universal ethical authority. Narrow target width and absolute measurement accuracy are different questions.
6. **Biological correspondence remains separate.** The [completed public-data continuation](BIOLOGICAL-CONTINUATION-INTEGRATION.md) supports history-dependent behavior and separately measured pathogen burden. It does not contain a jointly calibrated cellular–organ–learning–response–microbial-renewal history. Temperature records cannot close that obligation.

## 6. Completion audit and the next discriminating evidence

| Obligation | Status after this round |
|---|---|
| Conditional scale, revision, inquiry and changing-dependency mathematics | Existing checked results retained, including supplied hypotheses and failures; no new theorem this round |
| Derive candidate readout-change bounds from actual archived records | Completed for the declared three runs, split, rates and horizons |
| Identify the source and meaning of the response band | Completed: chosen soft engineering target, not hard accuracy/safety warrant |
| Test frozen bounds on later observations and separate-run transfer | Completed; violations and zero width-compatible intervals preserved |
| Establish a hard future physical-change bound and calibrated action certificate | Not established by these records |
| Certify the complete biological loop and sustained ecological renewal | Not established by the available joint evidence |

The [measurement protocol](BOUND-CALIBRATION-PROTOCOL.md) specifies the missing evidence and acceptance criteria. It calls for traceable unit-level measurement calibration, acquisition/actuation timing, a declared domain of commands and changed conditions, and independently justified application tolerances. A mechanism-backed hard certificate and a statistical empirical reliability claim are distinct possible outcomes and must be labelled accordingly. Biological completion requires connected cohorts/interventions and later viable microbial renewal measurements, without inventing correspondence between unrelated datasets.

This closes the available-data assessment and changes the next step from another supplied-bound construction to acquiring the missing correspondence evidence. It does **not** close Ren's broader remaining validation request. The [document checks](BOUND-CALIBRATION-CHECKS.json) and [scoped bilingual table check](BOUND-CALIBRATION-TABLE-CHECKS.json) verify integration and retained bindings, not those absent empirical premises.
