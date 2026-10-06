# Reward association with mental states: original Experiment 3 sources

**Status:** exact source preservation and schema/eligibility audit. This directory does not contain a new effect estimate or a completed reproduction of the paper's statistical models. The planned retrospective analysis is in [recipient-value-learning](../../experiments/recipient-value-learning/PROTOCOL.md).

Yi Zhang and Leor Hackel (2025), *Reward Association With Mental States Shapes Empathy and Prosocial Behavior*, Psychological Science. The [author-hosted paper](https://www.hackellab.org/media/zhang-hackel-2025-psych-science.pdf) is preserved as [original PDF](originals/zhang-hackel-2025-psych-science.pdf). The [public OSF registration](https://osf.io/58wsu/) is explicitly a **post-study** preservation registration, dated 12 May 2025, rather than the study's preregistration. Its metadata reports independent computational reproducibility review by the journal's STAR team; that statement is source metadata, not a new check by this repository.

## Original bytes and retrieval

The OSF registration's archived storage contains [osf_materials.zip](https://osf.io/download/367m5/), 54,540,908 bytes, SHA-256 `069107e3ebeb7d3aa71314edf40a85123192823aa52ab09ca9befb02fdafb376`. The downloaded bytes match the OSF file metadata's hash. This outer archive remains outside the repository. Its exact selected members are preserved under `originals/`, with their archive paths, byte counts and hashes in [manifest.json](manifest.json).

There are 397 selected archive entries: the original Experiment 3 raw data, cleaned data, analysis/cleaning/visualization scripts, study task and survey, plus the general codebook, ReadMe and R dependency lock. Other experiments, editor caches and operating-system metadata were not extracted into the repository. The original task ZIP is retained unchanged, including its internal archive contents. The dependency lock is historical source metadata; no R dependency installation is imported or executed.

[OSF registration metadata](metadata/registration.json), [storage listing](metadata/osf-files.json), [archive listing](metadata/archive-files.json) and [file metadata](metadata/file-metadata.json) are preserved separately. The manifest records retrieval time and the paper's byte hash. No selected original is rewritten by this audit.

The registration explicitly links to OSF's **CC0 1.0 Universal** license record, preserved in [license.json](metadata/license.json). This is the source's declared license for its OSF materials, not an inference from public accessibility. The separately downloaded paper states “© The Author(s) 2025” and points to SAGE reuse permissions; the preserved paper does not display an open-license grant. The OSF license is not silently applied to that separate PDF or to rights held by third parties. [metadata-verification.json](metadata-verification.json) records the separately retrieved metadata hashes, including this license addition; the original data manifest is unchanged.

The paper links the Experiment 3 preregistration at <https://aspredicted.org/zb4cs.pdf>. A direct request returned HTTP 406, and the web reader could not retrieve it. No preregistration PDF is present in the data archive. Consequently the preregistration's full contents, including the disclosed early inspection and deviations, have **not** been independently read here. Statements about it below are attributed to the paper or author scripts. A failed retrieval is not verification.

## Exact source paths

| Role | Preserved source |
| --- | --- |
| Raw task records | `originals/Experiment_3/data_raw_primary/Pavlovia/*.csv` (387 files) |
| Raw survey | [post_task_survey_3_anonymized.csv](originals/Experiment_3/data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv) |
| Author cleaned choice data | [data_3.csv](originals/Experiment_3/data_clean/data_3.csv) |
| Author sample and variable construction | [cleaning_3.R](originals/Experiment_3/code/cleaning_3.R) |
| Author models | [analysis_3.R](originals/Experiment_3/code/analysis_3.R) |
| Codebook | [codebook.xlsx](originals/codebook.xlsx), sheet `Experiment 3` |
| Executable task source and stimuli | [psychopy_task_3.zip](originals/Experiment_3/study_materials/psychopy_task_3.zip), especially `psychopy_task_3/pav_emp_3.psyexp` |
| Post-task survey instrument | [qualtrics_survey_2.docx](originals/Experiment_3/study_materials/qualtrics_survey_2.docx) (original filename retained) |

The raw task CSVs contain the two assigned conditions, trial number, offered left/right pictures, chosen key, reaction time, realized decision feedback and decision congruence state. Conditioning records retain the stimulus, target outcome, self outcome and response. They can support a raw-data audit; they do not measure a participant's trial-level subjective payoff expectation.

The cleaned CSV contains participant ID, the initial and current condition codes, reversal code, trial number, personally optimal choice, reaction time and post-task covariates. It omits unanswered choice trials and does not preserve the original offered alternatives or realized feedback. It cannot alone recover an all-offered-trials denominator without the task design/raw records.

## Assignment, outcome and timing meanings

The task XML's JavaScript independently chooses initial `A/B` and current `C/D` conditions using separate uniform `Math.random()` calls. The author cleaning maps `A/C` to congruent (`+1`) and `B/D` to incongruent (`−1`). This is a 2×2 randomized task design. The current feedback schedule shuffles a fixed 24/8 allocation over 32 choice trials; it is not 32 independent Bernoulli draws. The raw `n_trial` is the decision trial index.

`optimal=1` denotes the choice with the higher expected **personal** reward under the current condition. It means a liked-target choice in the current congruent condition and a disliked-target choice in the current incongruent condition. Target-liked and self-optimal outcomes must therefore remain separately labeled. A timeout is no recorded choice, not a recorded dislike. A proposed `liked choices / 32 offered` outcome counts timeout as no liked selection; an answered-trial proportion answers a different question.

The transferred scenarios concern the same trained target. The task instructions describe stock points entered into a gift-card lottery and state that a selected choice will determine a recipient gift. The preserved analysis package contains no identified fulfillment ledger proving actual own or recipient payment. A stated incentive, recorded choice, expected personal monetary consequence and observed recipient benefit are different evidence claims.

Contingency awareness and other questionnaire measures are collected after the decision phase. Awareness-defined contrasts are descriptive post-treatment subgroups, not randomized effects of awareness or a basis for restricting the primary sample.

## Eligibility audit, without choice aggregation

[audit_sources.py](audit_sources.py) verifies every selected original's saved byte count/hash and reconstructs the author eligibility rules from raw metadata and missing-response indicators. Its saved output is [source-schema-audit.json](source-schema-audit.json). It does not aggregate choices or fit models.

1. Select completed surveys (`Progress=100`) dated at or after 5 December 2023 00:00 using the source's `%m/%d/%y %H:%M` date format.
2. Retain public anonymous P-number task identifiers. There are 390 completed post-cutoff survey responses; five have no such identifier, leaving 385 saved complete responders matched to task records.
3. Apply the author rules: fewer than eight missed conditioning responses, fewer than seven missed decision responses, and the leading numeric attention response below four.
4. Their intersection reproduces **333 eligible participants**. The author cleaned file also contains 333 participants and 10,532 answered choice rows.

Every one of the 385 saved complete responders has 40 conditioning records and 32 offered decision records in the raw source. This is a schema/count check, not a choice analysis; trial identity, assignment and raw-to-clean correspondence are separately checked by the analysis implementation.

Among the 385 saved complete responders, the respective individual-rule pass counts are 349, 377 and 360. Some comments in the original script use 349, 379 and 364 without a common denominator. The audit preserves those comments unchanged and does not infer a new exclusion rule from them. The exact intersection, not those comments, yields 333.

The survey file has 498 rows after its CSV header, including two Qualtrics metadata rows; 105 completed survey rows precede the date cutoff. The script comments mention 106 early records. This accounting difference does **not** establish a contradiction with the paper's separate disclosure that the authors inspected an early batch of 50 participants before preregistration. These concern different selection/accounting phases. With the preregistration unavailable, the relationship is not reconstructed beyond the explicit source rules.

The eligible sample uses post-assignment response and attention exclusions and is not an intention-to-treat population. A sensitivity using all 385 saved complete responders can describe the effect of those exclusions, but still excludes unsaved/noncompleted responses. Anonymous clean-file IDs follow the author script's file-order mapping; the map in the source audit remains provisional until the separate analysis checks raw-to-clean correspondence.

## Author model and analysis boundaries

The author script fits `glmer(factor(optimal) ~ condition_change_recode + (1 | ID_anonymous), family="binomial")`. It runs both an RT ≥0.2-second subset and the original cleaned response data, labeled as the preregistration version. The paper describes the extra very-fast-trial filtering as exploratory and reports that including those trials changes the reaction-time inference. Awareness interactions and further moderators are secondary. The script's header calls this Experiment 2, although its paths and variables are Experiment 3; the original is retained.

The paper's reported main choice result is already known before this repository's reanalysis. Any new protocol is retrospective, and a new probability-scale factorial contrast must not be called a preregistered replication of the author's mixed-logit coefficient. Neither contrast isolates acquired moral value from learned expectations, demand or other unmeasured mediators.

## Privacy and reproduction

The public survey's recipient-name, recipient-email and external-reference fields are blank in actual response rows; their only nonempty entries are the two Qualtrics metadata rows. There is no IP-address field in the preserved schema. The string `IP Address` in `Status` is a survey status label, not an IP address. Public task IDs use anonymous P-number strings. No email-pattern match was found in the actual survey rows. Public response identifiers, timestamps, demographics and free text remain in the original bytes. These structural checks do not prove that every free-text response is nonidentifying; reports should not quote participant text or expose identifiers unnecessarily.

Run only the byte/schema audit with `python3 sources/32-mental-state-reward-learning-2026-10-06/audit_sources.py`. This uses the Python standard library and writes only its audit JSON. It is not a scientific effect-estimation run.
