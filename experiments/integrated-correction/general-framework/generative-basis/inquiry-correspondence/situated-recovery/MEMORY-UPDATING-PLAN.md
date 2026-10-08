# Acquired context and subsequent updating: analysis plan

9 October 2026. Exploratory secondary analysis, written after reading the published claim and author Fig3 code but before extracting this experiment's observations. This is not a preregistration or independent replication.

Reuse `situated-recovery-empirical-correspondence`: the preceding analysis measured retained expression. The new question concerns how relationships formed during training change the subsequent effect of a perturbation. Movement, cue, imposed field, retained adaptation and channel measurement belong to one experimental history. The selected contrasts preserve those relationships, without identifying a primitive independent observer or a directly observed latent memory.

## Source and correspondence fixed before extraction

Use all 24 `memory_updating_participant*.mat` files from [the deposited data](https://doi.org/10.5061/dryad.m63xsj42r), retrieved through the public [Zenodo mirror](https://zenodo.org/records/5516490). Verify each original against retained Dryad size and SHA-256 metadata. Preserve the original [Fig3_data_figure.m](https://zenodo.org/records/5512855) and README.

Translate the author's mapping: cue 1 is the control point on the first Triplet1 channel; P+ is the sign paired with that cue during Exposure. The four conditions are P+ cue1, P+ cue2, P− cue1, P− cue2. Single-trial update is the second minus first channel coefficient, multiplied by the actual exposure-field sign, so a positive value follows that perturbation. Check exact triplet adjacency, missed trials, channel type, matching flank cues and serialized-table agreement before analysis. Unexpected schedules require a documented correction, never silent filtering.

Author windows: first four triplets of each condition for pre-training; triplets 29–36 for congruent P+ cue1/P− cue2 and 5–12 for the other conditions for post-training. Expected total triplets per condition: 36,12,12,36. Keep intervening observations; the endpoint comparison does not make their omission disappear. Reproduce author participant means and SEM; do not claim to refit COIN or independently reconstruct raw force preprocessing.

## Estimands and uncertainty

For each participant, compute the four condition means at each phase. Report all means, then three paired factorial contrasts: cue effect = mean(cue1) − mean(cue2); perturbation effect = mean(P+) − mean(P−); interaction = (P+cue1 − P+cue2) − (P−cue1 − P−cue2). The perturbation contrast concerns the direction associated with the subsequently measured context, after sign alignment; it is not raw signed force.

Primary analysis: change of each contrast from pre to post. Also retain phase-specific contrasts and cue contrasts within each perturbation direction. Use participants as the independent resampling unit, 20,000 percentile bootstrap samples, fixed seed 20261009, and two-sided paired t tests with Holm adjustment across the three primary contrast changes. This is exploratory inference conditional on participant independence and this measurement. Do not treat many trials as many people or treat failure to reject as equivalence.

Check participant signs and leave-one-participant-out group means. Examine first and second halves of the post window as a declared sensitivity to ongoing change; finite stability does not establish asymptotic convergence. Reproduce the author grouping through a separate channel-sequence implementation and compare with direct triplet extraction. Preserve negative/ambiguous results.

## What would change the account

A missing acquired cue effect, sign reversal, extraction mismatch or strong dependence on a few participants would narrow the connection. Even a robust cue effect identifies a context-sensitive expressed update, not a uniquely identified latent learning-rate mechanism, conscious awareness, arbitrary new concepts, self-chosen goals, ethical warrant or general convergence. A stronger mechanism comparison needs predictions distinguishing memory change from expression/retrieval change. This work tests a particular formed relationship within the broader Theory of Becoming; it supplies no zero-axiom foundation.

## Retrieval amendment before observation extraction

Full downloads exposed a large transport cost from unused high-frequency trajectories. Before reading trial values, switch to the public server's HTTP Range facility: the MAT5 header specifies the MCOS subsystem offset; preserve its exact 128-byte header and complete compressed subsystem through end of file. Check HTTP 206 Content-Range and original size against the official metadata, compressed block length, decoded table copies and the experimental schedule. These are explicitly labelled original-byte fragments. Their SHA-256 values are locally verified; the deposited whole-file SHA-256 is retained as source identity and is **not** claimed verified from fragments. The previously downloaded recovery files remain whole-file verified. Preserve one additional full memory-updating file if feasible for a direct range/full extraction cross-check. This changes transport and provenance strength, not participant selection, measurement, contrasts or windows. Incomplete raw-trajectory download temporaries carry no unique analysis and are removed.

## Schedule reconciliation before group contrasts

The first extraction halted on a numbering gap. Participant 13's deposited table jumps from TrialNumber 1666 to 1669 between Exposure blocks; both flanking rows are non-channel trials. All 24 tables have 292 channel measurements and the complete 96-triplet count. No retained row is marked MissTrial. Preserve the two absent trial numbers as a provenance limitation; do not impute their contents or infer why they are absent. Check that every analysed triplet has consecutive actual TrialNumbers and retain participant 13 in the planned complete-sample analysis. Add an explicitly post-plan omission sensitivity, and save actual trial numbers rather than assuming row number equals trial number. No outcomes were compared to choose this correction.
