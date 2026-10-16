# Formation and apparent loss in an observed developmental history

8 October 2026. Continuation of Ren's evolutionary-organization study. **One predefined microscopic field now has a measured 91-frame history.** Bright structures grow, move and sometimes disappear locally. The analysis also identifies a concrete failure of an unqualified loss interpretation: a structure can remain visible after its assigned track ends because it touches the analysis boundary. This distinction is necessary before formation and loss measurements can constrain evolutionary continuation.

**中文结论。** 已将一个预先固定视野的91帧接成真实发育观察史：可见结构增长、移动及局部骤然消失，也查到“轨迹结束而结构仍在”的边界删失。自动轨迹结束不能直接当作坍塌、死亡或繁殖失败。该结果推进实际形成史的测量，对后继及新条件预测的共同数据连接仍须保留。

## What the observed history establishes

The [prospective protocol](DEVELOPMENTAL-HISTORY-PROTOCOL.md) fixed the central 512 × 512 pixels of scene 0/P6 in the 23 November 2023 acquisition before inspection of interior images. The complete first and last fields had already been viewed. Thus this is an exploratory measurement study with predefined interior selection, not an untouched confirmatory test.

The [original bands](../../../../sources/evolutionary-selection/karita-2026/microscopy-history/README.md) support all 91 captures. Recorded scale makes the analyzed square about **726.4 µm per side**. Image-specific times span 15.000018 hours, with intervals of 599.900–600.148 seconds. Stage and focus tags are constant throughout the inspected sequence; acquisition time is the only varying subblock metadata field. Global settings record exposure and auto-exposure configuration, but per-frame metadata is not an independent photometric calibration. Increasing image brightness is not equated with increasing biomass.

The [raw montage](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/raw-history.png) shows sparse bright structures becoming larger, followed by a denser, changing field. Three prespecified local-contrast thresholds produce similar broad changes in resolved-region counts: approximately 8–9 initially, maxima of 54–58, about 20–23 at twelve hours, and 41–45 at the final capture. These are image regions. Merging, changed contrast, entry, exit and physical loss can each change their count.

Four longest assigned trajectories were selected for [endpoint inspection](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/endpoint-inspection.png), using the recorded selection rule. The [review record](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/endpoint-review.json) distinguishes the observations:

| Assigned trajectory | What the images and checks show | Warranted interpretation |
|---|---|---|
| Track 2 | A large bright structure remains through T48 and is absent from the same window at T49 and T50. Last segmented equivalent diameter is 57.3–59.0 µm across thresholds | Abrupt local image loss following an assigned growth history; its three-dimensional fate and viability are not identified |
| Track 10 | A large structure remains through T45 and is absent from the same window at T46 and T47. Last diameter is 53.2–54.4 µm | A second local-loss candidate, subject to the same motion, depth and identity limits |
| Track 3 | The track ends at T46, but the structure is still visible at T47. Its T47 thresholded region reaches column 512 and is excluded by the boundary rule | A verified case of boundary censoring; track termination is not contemporaneous structural disappearance |
| Track 9 | A small feature near the terminal assigned position remains weakly visible, and the strongest threshold does not resolve the same feature | Insufficient evidence to classify this track ending as structural loss |

These selected cases are not an unbiased sample of event sizes or durations. The two last-region diameters are detector-based planar measurements, not a fitted collapse threshold, mass estimate or independent test of the source's approximate colony scale. A ten-minute interval can conceal motion or an intermediate transformation. No fall direction or death is recovered from a disappearing two-dimensional signal alone.

## The identity uncertainty is consequential

The protocol uses local-contrast thresholds of 4, 6 and 8 robust noise units and a baseline 40 µm adjacent-frame displacement limit, with area ratios from one quarter to four. Threshold-6 matching is also evaluated at 20 and 80 µm. The same observations are given to each setting; none is selected as biologically correct because it creates a preferred history.

| Threshold and movement bound | Assigned adjacent links | Links with another admissible partner | Unmatched preceding regions |
|---|---:|---:|---:|
| 4, 40 µm | 2,177 | 209 (9.60%) | 333 |
| 6, 40 µm | 2,074 | 179 (8.63%) | 276 |
| 8, 40 µm | 1,967 | 222 (11.29%) | 316 |
| 6, 20 µm | 2,033 | 26 (1.28%) | 317 |
| 6, 80 µm | 2,098 | 1,066 (50.81%) | 252 |

Widening the movement bound adds relatively few assignments while creating many alternative partners. Narrowing it removes alternatives but can sever true movement. Even one admissible partner does not prove identity. Unmatched regions therefore cannot be converted directly into a collapse hazard, and a longest algorithmic track is not automatically a longest-lived colony. The [sensitivity figure](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/measurement-sensitivity.png) makes this tradeoff visible.

The boundary example is a diagnostic success of the review, not evidence that the detector violated its specification: it deliberately excludes objects touching the crop. The invalid inference would be to label every termination as physical loss. This distinction preserves the failure without treating a stated observation boundary as a defect in the underlying biology.

## Verification and provenance

The [analysis package](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/README.md) preserves code, all measurements, source-bound frame records and the inspected figures. An additional 251,170,816 original bytes are saved as conditional HTTP ranges. Existing source bytes and prior receipts remain unchanged.

The [measurement receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history/measurement-verification.json) records independent decoding of **91 subblock records and 23,855,104 crop pixels**, plus separate full-frame decoding at both endpoints. It also checks 7,272 region records and 10,349 assigned links across the sensitivity analyses. These are software and measurement checks on one field, not independent biological replications. The pinned source reader requires Python 3.12; the initial attempt under 3.11 failed on its syntax and was rerun successfully under 3.12 without modifying that reader.

No new general mathematical proposition is asserted, so no new Lean theorem is claimed. The previous developmental reconstruction proofs and the concurrently completed comparison retain their exact hypotheses and checking scope. This study adds numerical measurement and substantive author counterreview, not independent-agent acceptance.

The [documentary receipt](DEVELOPMENTAL-HISTORY-CHECKS.json) binds the executed results, preserved originals, local links and paired C14 update. The [reproduction checker](DEVELOPMENTAL-HISTORY-CHECK.py) preserves all six broader requirements and reports concurrent source-review obligations separately.

## What this changes in the evolutionary account

The explanatory connection is now more concrete: an activity can form a structure and enlarge it while its later persistence remains contingent. The observation that a structure was produced cannot supply its later availability for sampling, support or reproduction. A joint evolutionary model must represent the actual formation and loss history relevant to those operations, and must distinguish that history from the process by which it was imaged and tracked. Both processes are differentiated relations within the same unfolding.

This is a measurement contribution, not a new biological discovery that colonies can grow and fall. The original Karita study already supplies a conventional physical and developmental account. The [matched network comparison](EVOLUTION-NETWORK-COMPARISON.md), completed concurrently, additionally establishes exact conventional realization of our current reconstruction mechanism. Those results rule out presenting either explicit organization or these image-analysis tools as an exclusive predictive advantage.

The affirmative contribution survives at a narrower scope: a previously missing interior history is now source-bound, and a specific false route from observation to a fitted loss law has been exposed. The ordinary mechanistic rival receives the same history, boundary censoring, uncertainty and support information. A generative advantage would still need a further independently justified restriction connecting these measurements to later outcomes.

## The next comparison and its actual requirements

The next empirical connection is **validated structural fate → identified terminal sampling → viable descendants under recorded support**. The current field supplies neither a treatment-to-culture endpoint key nor a link to the separate six-day lineage experiment. Those relationships cannot be inferred from a scene number or assembled from unrelated cultures.

Before fitting a physical loss law, retain object-level annotations for motion, merging, splitting, boundary contact and local disappearance; establish the relevant plane or obtain an independent indicator of vertical loss. Validate the resulting observation model across fields and reserve whole cultures or batches for the later comparison. More automatically assigned tracks alone will not resolve biological identity. The original two-dimensional local-loss candidates remain useful targets for this validation, with their uncertainty preserved.

The immediate trajectory-measurement study is complete. The full evolutionary objective and empirical comparative advantage remain open. Its six requirements are unchanged; neither a finished source decoder nor a descriptive image curve supplies a complete-cycle forecast.
