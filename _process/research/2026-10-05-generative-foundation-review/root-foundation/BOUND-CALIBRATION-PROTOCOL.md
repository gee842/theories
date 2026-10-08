# Measurements needed to finish the remaining correspondence

8 October 2026. AI-authored protocol following the [negative available-data result](BOUND-CALIBRATION-INTEGRATION.md). This is an executable research specification for future measurement, not a record of a performed experiment. It preserves the completion target rather than declaring a further finite model sufficient.

## Temperature correspondence

Record the actual unit, sensor grade, firmware, ADC conversion, supply, geometry and operating range. Compare readout against a traceable reference through the intended range, including ramps, stable periods and both channels. Separate offset, repeatability, resolution, lag, self-heating and reference uncertainty. Preserve raw pairs and calibration uncertainty, not just a fitted mean correction. Component specifications alone do not establish an end-to-end guarantee.

Log acquisition start/end, returned reading, optimizer start/end, issued command and acknowledged actuation against a synchronized clock. Retain dropouts, timeout paths and failed solves. Measure timing bounds under declared load; distinguish logged computation timestamps from actual acquisition age.

Before evaluating new data, declare the command/horizon range, initial thermal conditions, ambient variation and geometry/intervention classes to which a proposed bound applies. Fit a physical or predictive model on identified calibration runs. Compare retained-reading and conventional model-based predictions at equal information and horizon. Freeze models and envelopes before collecting or revealing held-out runs; hold out complete runs and altered-condition classes, not shuffled rows. Preserve changed-condition failures even if a revised model later succeeds.

State who or what warrants the temperature band for the intended application. An optimization weight is not such a warrant. If ±0.2°C remains only a chosen benchmark, label it that way and report tracking performance, rather than claiming safety or ethical necessity.

Two distinct acceptance routes are possible:

- **Mechanism-backed bounded certificate:** supply measurement, timing, disturbance and actuation correspondences over the declared domain. Use the established mathematical interface only where its dynamics apply; otherwise formalize the required thermal interface and actually check new proof claims in Lean. Observed tests challenge the correspondence but do not alone prove a universal bound.
- **Empirical reliability claim:** preregister horizon, loss, allowable failure frequency and the assumptions required by the statistical method; choose independent sampling units and sample size accordingly. Report the resulting scope and uncertainty. Do not recast a percentile, finite maximum or statistical coverage claim as a deterministic guarantee.

No particular replication count is asserted here because the required reliability, effect size and independent-unit variation have not been supplied. Prespecifying those is a real design dependency, not permission to pick a sample size after results.

## Biological correspondence

Follow the missing interfaces identified in [the biological continuation](BIOLOGICAL-CONTINUATION-INTEGRATION.md): link measured cellular/tissue organization, sensory integration, retained encounter effects, selected activity and later viable microbial conditions through identified cohorts and interventions. Matched cohorts may provide correspondence where simultaneous assays are impossible; explicitly justify the match and preserve uncertainty. Do not join the existing unrelated datasets by invented animal or plate identifiers.

Retain plate/cohort identity, density and exposure history, intervention assignment, movement/feeding observations, assay timing, measurement uncertainty and failed/terminated histories. Separate fluorescence or density proxies from viable counts. Compare conventional embodied-learning/physiological accounts with the same evidence and complexity budget. Hold out plates and interventions. Follow repeated cycles sufficiently to measure microbial renewal and sustained consequences, rather than calling one later burden assay ecosystem renewal.

Completion would require those linked measurements to support the claimed correspondences at stated tolerances while preserving adverse histories and rival explanations. A failure would narrow or revise the biological claim. Neither outcome would establish universal ethical grounding by itself.

**未取得的证据不能由文档替代。** 本轮没有硬件接入、动物实验、追加原始观察或已获验证的完整闭环。协议把缺失的观察、判准与可能失败写清楚；它本身不算完成这些观察。
