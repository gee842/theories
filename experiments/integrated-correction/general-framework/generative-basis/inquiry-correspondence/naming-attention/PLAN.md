# Naming and selective-attention correspondence

8 October 2026. AI-authored exploratory secondary analysis for Ren's continuing cognition, learning and evolutionary-psychology objective.

## Question fixed before outcome aggregation

Reuse `acquired-binding-compositional-use`, `enacted-scene-binding` and `encounter-selection-and-revision`. Their correct binding histories require that admitted encounters include the intended referent. Test the proposed empirical correspondence **every naming encounter → gaze access to the intended object** using the public coded data accompanying Yu, Zhang, Slone and Smith (2021), DOI [10.1073/pnas.2107019118](https://doi.org/10.1073/pnas.2107019118), [OSF mvz78](https://osf.io/mvz78/).

The published bimodal finding and the authors' README were read before this plan. No CSV outcome rows or aggregated results have yet been inspected. This is not a preregistered or blinded confirmation of that finding. The analysis changes a model-to-measurement correspondence, not the validity of the earlier conditional Lean proofs.

## Measures and analysis

- Preserve original downloaded bytes and verify the deposited SHA-256 hashes. Keep source CSVs unchanged. Inspect seven-field schema, units, bounds, finite values, participant/event keys and cross-window membership before combining anything.
- Use the published three-second window as primary; analyze every deposited duration (0.5, 1, 1.5, 2, 3, 4 and 5 seconds) as sensitivity. Windows are repeated measurements of naming events, not independent replications.
- Field 6 measures time on the named target, field 7 time on other objects. Determine whether stored units are fractions or percentage points from the values and metadata. Keep the denominator specified by the source; do not silently renormalize gaze to target-plus-other time.
- Count zero recorded target gaze; separate zero target with some other-object gaze from zero on both. Separately count strictly greater than half of the window on target and on other objects, exact full-window target and exact full-window other gaze. The half-window threshold has a direct duration interpretation; it is not a fitted learning threshold.
- Report event-weighted proportions and participant-level distributions/equal-participant averages. Use participants as the unit if estimating uncertainty; no independent-event standard errors or causal tests. Describe the actual sample without implying population representativeness.
- Report the unassigned fraction `1 - target - other` only when the unit/bounds audit permits it. It combines measurement failure, off-object looking and any other uncategorized time; it is not a measured wrong referent or absent perception. Do not discard zero-gaze rows or count them as observed target errors.
- Compare event identities across windows and verify nested-window target/other durations only if their identity and time definitions support pairing. Report any inconsistency before interpreting temporal changes.

## Limits and decision rule

Nonzero target gaze is an operational access proxy, not proof of word acquisition, memory, covert attention or represented candidates. Zero recorded target gaze does not prove the target was never optically visible or never represented. The data do not include a measured learning outcome or a randomized coordination intervention in these files. They cannot identify a child's exact algorithm, causal development of coordination, the origin of the choice criterion, consciousness or an evolutionary genealogy.

If recorded target gaze is sometimes absent while other-object gaze is present, automatic naming-to-attended-target coverage cannot be retained as an unrestricted measurement correspondence. That finding would require an explicit encounter-admission or error-tolerant learning connection, with independent calibration evidence. If no such cases occur, this sample still cannot establish universal coverage. Preserve the earlier formal coverage-failure counterexamples in either outcome.

## Verification and review

Use a reproducible Python analysis with original files, a source manifest and fixed definitions. Independently recompute headline counts with exact decimal arithmetic; inspect participant and window sensitivity. A substantive author counterreview must distinguish physical visibility, recorded gaze, admission, retention and learned reference. No new mathematical theorem is claimed, so unchanged Lean proofs are reused at their existing receipts. Record the analysis source and output hashes. Integrate the result into the existing acquired-segmentation study and cognition chapter.
