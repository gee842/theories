# Source-ordered timing, acquired records and warranted historical comparison

8 October 2026. AI-authored continuation of the active request to **compose existing results, explain a supplied premise, and establish real-world correspondence**. The preceding [tuning study](TUNING-CORRESPONDENCE-INTEGRATION.md) received independent acceptance and was progress. This round addresses its named remaining inference: where a justified timing/uncertainty domain can come from, and what comparison it actually supports. It uses further original members of the same physical benchmark archive, not a new hardware experiment.

## What this establishes

Source event order and recorded timestamps supply a finite uncertainty domain for **when a requested command was issued**, even though exact issue timestamps are absent. The resulting exposure intervals are sufficiently separated to establish a real comparison between the archived runs: on the same time window, the ARX summary run requests more integrated command on **each heater** than either nonlinear-controller run, for every switch-time history admitted by that domain. The proof consumes the existing exposure and separated-comparison results. It does not turn commanded percent-seconds into electrical energy or a total ethical burden.

The archive also contains an implementation distinction relevant to inquiry versus earlier response. The ARX loop computes a new plan and stores it for the next iteration, then issues the plan retained from the previous one. The nonlinear loops issue the result just computed. A one-second sampling period therefore does not itself prove a one-second sensor-to-command age or a faster effective response. Acquired rows, initialized array entries, plan formation and issued requests must remain distinct relations in the same execution.

**Eight new Lean theorems / nine declarations pass; the nine-module closure has 237 declaration audits.** Exact rational calculations retain 1,788 timing intervals across four distinct logs and 2,378 heater/window exposure pieces for the primary three-run comparison. The [independent completion review](TIMED-FEEDBACK-REVIEW.md) separately rebuilt the proofs and reproduced every exact interval and comparison. The three requested kinds of integration are complete together at this historical-comparison scope; future latency and thermal-calibration guarantees remain further application questions.

## Original sources and which records are actually comparable

[Additional source manifest](../../../../sources/tclab-benchmark/TIMING-PROVENANCE.json) · [byte-preserving extraction runner](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/extract_timing_sources.py) · [numerical runner](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_timing.py) · [complete exact results](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/timing-results.json).

Eleven source/log members were extracted byte-for-byte from the previously pinned `CACE_2020_source.zip`; the old provenance manifest and every earlier result remain unchanged. The primary comparison uses the three files actually consumed by `3_TCLab/Summary/results.py`. The physics and ANN copies in their model directories are identical to their Summary copies. The ARX directory's illustration log is **different** from the ARX Summary log. It is separately examined, never substituted or counted as a duplicate confirmation of the same run. The two ARX scripts differ in plotting while preserving the examined control-loop logic.

The original paper is Park, Martin, Kelly and Hedengren, *Benchmark Temperature Microcontroller for Process Dynamics and Control*, [DOI](https://doi.org/10.1016/j.compchemeng.2020.106736), preserved as the original [preprint](../../../../sources/tclab-benchmark/CACE_2020_Preprint.pdf). Sections 5–6 and Table 3 specify differing cycle times and compare tracking and movement. The source's tracking calculation is `sum(abs(error))/number_of_rows`, with units °C, despite the table labeling it as °C/sec. Its movement calculation divides summed absolute changes by elapsed seconds. This distinction follows the supplied computation and dimensions; it is not a change to the physical observations.

The Summary script reproduces the paper's rounded tracking values 11.5, 11.6 and 11.4 and movement rates approximately 2.0, 3.3 and 2.5. Its ARX record has 601 rows, but the loop acquires readings only at indices 1–599. Index 0 was initialized before the clocked loop; index 600 retains initialized temperatures while holding a newly computed command that the loop never issues. The final timestamp is written after plotting and shutdown. Both ARX logs retain this terminal pattern. The original files and original calculation remain intact; the new analysis marks these positions explicitly instead of treating the final row as a sudden physical cooling event.

| Primary record | Original mean sample error | Mean over acquired loop rows only | What changed in the calculation |
|---|---:|---:|---|
| Physics | 11.515500 °C | 11.554013 °C | Excludes initialization index 0 |
| ARX Summary | 11.587354 °C | 11.546912 °C | Excludes initialization 0 and unacquired terminal 600 |
| ANN | 11.351500 °C | 11.389465 °C | Excludes initialization index 0 |

This small correction reverses the physics/ARX ordering in that sampled-error calculation. It does not overturn the source's broad observation of similar tracking, establish statistically different performance, or isolate a controller's causal advantage. There is no randomized replication here; initial readings, schedules and implementation details differ.

## Deriving the timing domain from the execution

All examined loops record `tm[i]` before acquiring the two temperatures, solving and issuing their heater requests. In a successful serial iteration, each request therefore occurs after `tm[i]` and before the next loop's timestamp. The domain relies on the archived execution contract, an order-preserving clock over these intervals and successful serial progression; there is no separate trace attestation of the historical binary. A delayed hardware response after a request is not measured by these files.

For the physics and ANN loops, the current command uses the current record. Its record-timestamp age at issue lies between zero and the next recorded interval. The ARX loop instead assigns `Q1s[i+1] = Q1.NEWVAL` but calls `a.Q1(Q1s[i])`, likewise for heater 2. Command `i` uses record `i−1`. Its timestamp age lies between the preceding interval and the sum of the preceding and following intervals. The lower endpoint is **not** a lower bound on readout-retrieval age: the retrieval call occurs after its timestamp. The upper endpoint also bounds retrieval-to-request delay under the same ordering. The archived scripts do not preserve the historical driver, firmware or hardware conversion timestamps. Interpreting this bound as age since physical sampling additionally requires sampling within the retrieval bracket, or an added bound on prior internal age. The formal acquisition theorem states its ordering hypothesis explicitly; the archive alone does not establish that additional sampling correspondence.

| Record | Inspected command-age intervals | Largest warranted historical upper endpoint |
|---|---:|---:|
| Physics | 297 | 2.028092 s |
| ARX Summary | 597 | 2.643852 s |
| ANN | 297 | 2.939591 s |
| Separate ARX illustration | 597 | 2.325789 s |

Thus all 1,788 inspected requests have a source-ordered upper endpoint below three seconds. This is a retrospective result, not a newly chosen safety deadline or a future worst-case execution time. At a two-second timestamp-age deadline, 310 ARX Summary intervals are certified within it and 287 are undetermined; the physics and ANN intervals are all undetermined. An interval crossing a deadline does not prove the request missed it. Likewise, a long recorded period may include reading, solving, writing, sleeping or plotting; it does not isolate optimizer duration.

The source exposes an actual alternative for subsequent testing: the ARX command to be issued is already retained before the next inquiry/solve. It need not logically wait for that new result to become known. Issuing it earlier would, however, change the future physical readings and possibly later plans. The archived temperatures cannot be reused as observed outcomes of that reordered intervention. This round explains the dependency and timing premise without claiming an unperformed alternative hardware trial.

## A comparison that remains valid throughout the timing domain

Let a segment have duration `d`, previous requested command `u`, new requested command `v`, and unknown switch delay `s`, with `0 ≤ s ≤ d`. Its commanded exposure is

`u*s + v*(d−s)`.

Its midpoint estimate is `d*(u+v)/2`, with radius `d*abs(u−v)/2`. Lean derives this enclosure and its endpoints `d*min(u,v)` and `d*max(u,v)`. Clipping to a shared time window preserves the same form: the portion spent at the old command is still between zero and the clipped width. Each channel is enclosed separately. Possible correlations between the channels' issue times are not assumed away to claim attainability; the product of these intervals is a conservative containing domain.

The common window is determined by the records: **4.169826746 to 600.572573662 seconds**, duration 596.402746916 seconds. Its start is the latest second loop timestamp among the three primary records, ensuring an earlier successful command request is already known in each. Its end is the earliest last acquired timestamp. Unacquired terminal values, initialization timing and undocumented post-loop holding are excluded by provenance, not because their outcomes are unfavorable.

| Primary run | Heater 1 exposure interval | Heater 2 exposure interval | Combined exposure interval |
|---|---:|---:|---:|
| Physics | [18,744.037, 20,093.682] | [16,222.501, 17,281.183] | [34,966.538, 37,374.865] |
| ARX Summary | [22,050.604, 23,103.936] | [18,704.036, 19,578.325] | [40,754.640, 42,682.261] |
| ANN | [18,117.141, 19,826.479] | [16,069.082, 17,521.243] | [34,186.224, 37,347.722] |

Units are requested-command **percentage-point seconds**, summed across heaters only in the last column. Each nonlinear run's upper endpoint is below the ARX run's lower endpoint on **each heater**, so the combined comparison does not hide an opposing heater-specific exposure. The combined separating margins are approximately 3,379.775 and 3,406.918 percentage-point seconds. Physics and ANN exposure intervals overlap; this method does not order those two. Tracking, actual electrical energy, hardware delivery and effects on living conditions remain additional quantities, not synonyms for this command measure.

For transparency, the results also contain a time-weighted held-sample error over that common window: physics 11.622785°C, ARX 11.576421°C and ANN 11.472726°C. These use the disclosed convention of holding a sampled error until the next timestamp. They are not exact continuous-temperature integrals or calibrated true-temperature errors. No physical performance guarantee is inferred from that reconstruction choice.

## The checked composition and what remains supplied

[TimedFeedback.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/TimedFeedback.lean) · [fresh build checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_timed_feedback.py) · [passed receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/timed-feedback-verification.json).

| Checked result | Explained/consumed relation |
|---|---|
| `acquisition_age_bound`, `queued_timestamp_age` | Derive the age domain from the stated acquisition/issue ordering. The archive supports timestamp and retrieval ordering; underlying hardware sampling requires the separate correspondence above. |
| `source_ordered_calibration` | Combines readout calibration and a supplied physical drift rate with the derived age upper bound to obtain error at the time of issue. |
| `timed_protection_at_actual` | Directly consumes the preceding calibrated-protection theorem. It substitutes the derived time-dependent radius while retaining actual-case inclusion, calibration, drift and every indexed margin. |
| `segment_midpoint_bound`, `segment_interval_endpoints` | Derive the segment exposure domain from unknown switch position, rather than supplying an arbitrary global exposure error. |
| `history_exposure_bound` | Consumes `FeedbackMemory.exposure_error` to propagate those segment domains through the whole declared history. |
| `separated_history_exposure` | Directly consumes `TuningCorrespondence.separated_model_comparison`, using the whole-history bounds to establish comparison for every admitted switch sequence. |

The fresh build checks all nine repository modules from source; it records the pinned Mathlib cache and standard logical dependencies. No new custom axiom, proof hole or unchecked decision procedure is used. Rational archive calculations and actual Lean proofs retain separate validation scopes.

The useful new premise explanation is **serial event order and acquired records → a containing timing domain → a robust historical comparison**. Its physical and informational relations are reconstructed within the actual feedback activity. A clock bracket is not an external metaphysical law, and a solver result is not an independently existing action. Their distinctions preserve when each result can affect what follows.

The [completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md) now credits all three requested kinds of work in this single connected inference. It explicitly corrects an earlier assistant-authored expansion of the stopping criterion: the preserved audits elevated a next research direction—selection of inquiry versus earlier response—to a requirement for calling any integration complete. That stronger comparison has not been achieved. It remains a substantive direction, with future latency, true-temperature drift/calibration, consequences of reordering and basic living claims still requiring their own evidence. G0/J are not replaced by engineering performance or required to be proved without axioms; the repository-wide foundation objectives retain their separate scopes.

Independent review accepted the scientific continuation and the disclosed completion scope. Its [proof receipt](development/timed-feedback-review/verification.json), [separately implemented exact reconstruction](development/timed-feedback-review/numerical-verification.json) and [final evidence bindings](development/timed-feedback-review/bindings.json) preserve what was checked. A final correspondence clarification distinguishes readout retrieval from underlying hardware sampling; no proof or numerical formula was changed. Earlier review bindings remain attached to their exact accepted historical prose.
