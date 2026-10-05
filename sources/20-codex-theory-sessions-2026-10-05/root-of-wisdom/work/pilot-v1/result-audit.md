# Independent result audit

Date: 5 October 2026, Asia/Bangkok. Internal research-team verification, not external review.

## Verification method

Read all six saved response JSON files directly. Recomputed scores using a separate short calculation that did not import or execute `score.py` or use its result rows. The independent gold sequence for R01–R12 was C,C,B,B,B,A,D,D,D,A,A,C, previously checked against the case facts. Independently specified the six matched pairs and primary overclaim-option sets: R02 A/B, R03 A/D, R09 A/C, R11 C. Compared the resulting counts with `results.json` and inspected all 72 rationales.

All files listed in `run-freeze.json` still match their recorded SHA-256 hashes. The pre-run amendment authorizes one assigned-file read to load the frozen prompt, followed by a tool ban. Its recorded timestamp precedes the first dispatch record. This audit verifies the saved permission record; raw response JSONs do not contain participant tool traces, so this note does not independently certify absence of later tool use.

## Recomputed results

| Condition | Batches | Exact choices correct | Primary scope errors | Matched pairs correct | Revision cases correct | Retention cases correct |
| --- | --- | --- | --- | --- | --- | --- |
| Ordinary | 2 | 24/24 | 0/8 | 12/12 | 12/12 | 12/12 |
| Reflection | 2 | 24/24 | 0/8 | 12/12 | 12/12 | 12/12 |
| Discipline | 2 | 24/24 | 0/8 | 12/12 | 12/12 | 12/12 |

Every batch contains exactly one valid answer for each of the twelve IDs, with no missing, duplicate, or unknown IDs. Every batch has 12 correct choices, zero primary overclaims, and six correct matched pairs. There are no false scope rejections. These counts agree with the saved results.

All confidence entries are the valid integer 100. Their chosen-answer binary Brier scores therefore equal zero on these all-correct responses. This fact does not demonstrate calibration on uncertain tasks, discriminate the conditions, or justify general certainty.

All reasons are present and nonempty. Under the declared whitespace word-count convention, lengths range from 17 to 26 words, with no violation of the 30-word limit. Batch ranges are p01 19–25, p02 20–26, p03 17–25, p04 20–25, p05 19–25, p06 19–24.

## Rationale inspection

No substantive contradiction between a selected option, its reason, and the case facts was found. Reasons use the decisive cost, deadline, probability, or scope distinction and do not retract the selected warranted conclusion.

Minor wording imprecision appears in several R08 reasons: “signatures arrived” substitutes for the case's statement that the people signed by the deadline. The charter depends on signing time, and both relevant signatures were timely in that case. This wording does not alter the keyed choice or primary endpoint and does not warrant a scoring change. Preserve the raw text.

Some reasons omit a separate explicit disclaimer about unassessed future models; the chosen options already restrict the relevant conclusion to the current class. This is not an overclaim under the frozen option-based primary measure. The measure detects endorsement of the provided overclaim options, not every possible spontaneous completeness claim in unconstrained reasoning.

## Interpretation

**“A ceiling on these cases; no comparative advantage demonstrated” is defensible.** All conditions attained the maximum observed exact-choice and pair scores, and the minimum scope-error count. The cases therefore failed to discriminate the three prompts on these outcomes.

This is not a demonstration of equivalence or evidence that the discipline can never help. It also provides no support for its added practical advantage on this set. Do not replace the behavioral outcomes with stylistic preferences after seeing the tie. The fact that ordinary prompting solved every explicit case should constrain claims that the discipline was needed to make these particular deductions.

The six batches share a deliberately selected twelve-case set, and each batch's answers share context. The 72 responses are not 72 independent treatment replications. Different amounts of hidden reasoning may have been used; matched instructions, input-loading permission, and response limits do not establish equal compute.

The narrow positive finding is feasibility: the frozen prompts, case presentation, and scoring format yielded complete valid responses, and the internal recount agrees with the saved scores. No further v1 participants should be added. A separately frozen future version should test unprompted discovery or evidence selection with less explicit cues and a stronger comparison method; it must not be presented as an extension that rescues a positive result from this completed pilot.
