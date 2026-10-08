# Independent review: measured feedback and physical correspondence

8 October 2026, Asia/Bangkok. AI-authored independent completion-stage review of the measured-feedback addition, not a new hardware experiment and not a completion certificate for the wider three-part objective. Reviewed the [canonical account](../../../../theories/becoming/chapters/MEASURED-FEEDBACK-CORRESPONDENCE.md), [empirical integration](INQUIRY-JUDGMENT-EMPIRICAL.md), [completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md), formal source/checker/receipt, numerical implementations/results, original archive members and provenance. The project-wide nondual method and explicit G0 route remain applicable.

**Substantive verdict: accepted at the bounded archival-correspondence and conditional-composition scope.** Independent controller reconstruction, an independently implemented regression solver, provenance checks and a fresh Lean build all pass. One minor prose repair was requested: the Chinese phrase “真实消耗” must identify recorded command exposure rather than imply measured physical energy. Final wording verification is recorded below. No additional physical experiment is demanded for this local conclusion.

## Preserved independent evidence

- [Lean review runner](development/measured-feedback-review/check_lean_review.py), [Lean receipt](development/measured-feedback-review/verification.json), [complete axiom audit](development/measured-feedback-review/axioms.txt) and [audit source](development/measured-feedback-review/Audit.lean). Five compiler logs are preserved in the same directory. The runner reuses the inspected author's import-closure parser but executes its own compilation and audit, not the author's main runner.
- [Numerical review runner](development/measured-feedback-review/check_numerical_review.py), [numerical receipt](development/measured-feedback-review/numerical-verification.json) and [full numerical output](development/measured-feedback-review/numerical-log.txt). This implementation imports neither numerical producer nor alternate checker and uses no NumPy. It reconstructs controller memory independently with exact rational arithmetic and fits ARX coefficients using a standard-library Householder QR solver instead of the producer's SVD least-squares routine.

No source originals, author receipts or unrelated files were edited. Lean build products stayed in temporary scratch; no `.olean`, upstream package or cache was added to the review evidence.

| Reviewed artifact | SHA-256 |
|---|---|
| `MeasuredFeedback.lean` | `cdc9881f5929d1713f051305f3817329ee90ed12a05a323df330bb5df817972e` |
| `check_measured_feedback.py` | `2cb58e80e77463a268850db83fc13bcd2b1d657cb73da4e7d91a9c4c256ef7b5` |
| Numerical producer | `8e0f917554a47960d73f5afeba6a2dde612c4c2089ef464486618c6b5dfbc92d` |
| Producer results | `1a1d6022ec5d06fb7f18a4fc966277d52a9d1144ccb44e4f69001ebe53ad67d7` |
| Author's alternate rational checker | `378bf14203654fc970bb47b2376e5abb1d0a2663976d6cd533b79d1f398646a0` |
| Author's rational receipt | `39622230d9d52aaa47eaf30cb9c882516e65f360fa12e1ea5b5c288230df28e4` |

The author's formal snapshot is `measured-feedback-checks/20261007T210939.617450Z` under the analysis directory. Current source, preserved source, checker, executable, logs, manifest and recorded absolute direct-import fingerprints match its receipt. Independent compilation at `2026-10-07T21:15:55.504356+00:00` passes all five repository modules and all 147 explicit-declaration audits, including the 26 new declarations and 13 new theorems. The new declarations permit only recorded standard logical dependencies. Mathlib's pinned cache is reused; no full upstream rebuild or hermetic linked-runtime attestation is claimed. The executable-only fingerprint limitation from the previous review still applies.

## Physical provenance and what replay establishes

I independently fetched the pinned remote archive and preprint into memory and compared their hashes with the preserved originals. Both match. All 14 selected extracted members also match their original archive bytes and manifest sizes/hashes. This is a strong provenance check for the cited publication's archived files, not independent witnessing of the historical laboratory work. Duplicated archive/member bytes are not multiple observations.

I read relevant preprint text on physical-model fitting/validation, ARX versus free prediction, controller retuning, engineering objective and the reported physical validation (PDF pages 9–13, 15–16, 19, 21 and 27), along with the original acquisition and PI scripts. The paper reports a physical benchmark and separate measured validation; the source imports `tclab`, reads the temperatures, calculates the command, and sends it to the device. [Preserved primary preprint](../../../../sources/tclab-benchmark/CACE_2020_Preprint.pdf), [pinned source provenance](../../../../sources/tclab-benchmark/PROVENANCE.json).

The logs supply 599 records per PI run. The 598 subsequent commands in each run are reconstructed from current recorded temperature, recorded target, previous retained integral and actual logged interval. This is 1,794 checked commands, not 1,797 reconstructed updates. My implementation retains integrated error before gain multiplication, independently of the producer's gain-weighted memory. All commands agree within the stated numerical scale; the largest exact-rational discrepancy is `7.42842058890256e-14` percentage points. The author's separate rational checker implements the same mathematical saturation/retention rule without NumPy, and its scope is accurately described as an alternate same-agent implementation rather than independent physical replication.

The original code reads time before temperature acquisition and actuator transmission. Thus logged intervals support replaying its integral update, but are not complete sensor-to-actuator latency records or exact actuator switching timestamps. `Q1` is a recorded command; the files do not independently verify analog output, each firmware instruction or delivered heat. The first sample is an initial state; the source's saved slicing omits its last loop index, and the reanalysis uses every preserved row rather than reconstructing an absent final sample.

The two-heater acquisition scripts use nominal integer indices and delayed reads. Moreover, `gen_data.py` names `ambient.csv`, whereas the fitting artifact is `initial_models.csv`; the archive does not itself certify an exact byte-for-byte generation execution. Publication provenance and archived data support the bounded historical interpretation, not a fully instrumented execution trace of file creation. The current analysis appropriately presents a recorded-index model and does not infer calibrated continuous-time latency from those indices.

## Independent numerical results and preserved losses

My exact-rational metrics reproduce the initial and validation objectives: `6.09082785736046`, `5.7645812616881615`, and `5.558065516961002`. Absolute command movement increases from `0.712674` to `0.900749` and `0.952225` percent per recorded sample. The first validation's left-held commanded exposure rises from `27292.4835767` to `28565.1409403` percent-seconds; the second is `26504.0480814`. These figures support the limited claim that the weighted objective improves while some costs rise. They do not measure electrical energy, and switching-time uncertainty also limits literal physical interpretation of the left-held exposure estimate.

The original optimization source genuinely sums signed increments. Its objective therefore differs from the paper's absolute-movement formula. The Lean telescoping theorem and bounded `[100,0]` counterexample identify the structural defect without pretending that the physical improvement disappears. The comparison-order example further shows that even bounded commands do not repair the discrepancy. The observed validation performance is supported; minimization of the stated absolute objective by the archived search remains uncertified. No source cleanup or favorable reinterpretation is needed to retain both conclusions.

The weighting `1` for tracking and `0.5` for movement remains a supplied engineering comparison. More movement is a real recorded change, but its ethical importance and any basic claim on the consumed support are not numerically established. This prevents the performance table from secretly supplying G0, J2, living standing or authority.

## Independent regression and leakage audit

I reconstructed the design matrices from the two raw CSVs and independently solved all four ordinary least-squares fits with Householder QR. The largest coefficient difference from the producer's NumPy least-squares output is `4.76e-14`; all reported training, held-out and free-rollout error summaries agree within `1e-7` °C, with much smaller observed differences. The model family and second-order lag counts match the identified archived example. This is verification of the new OLS study, not a reproduction of the original GEKKO output-error fit.

| Model | Held-out one-step RMSE | Free-rollout RMSE |
|---|---:|---:|
| T1, heater 1 | 0.22370126 | 5.93346115 |
| T1, both heaters | 0.22345590 | 5.77756178 |
| T2, heater 1 | 0.19409427 | 8.19072664 |
| T2, both heaters | 0.16886217 | 3.93388930 |

Each fit uses only the initial CSV's 598 eligible indices. The validation data do not enter coefficient estimation. One-step prediction deliberately uses the prior measured validation temperatures; that is its stated information condition, not leakage into the fitted coefficients. Free rollout instead starts from two measured temperatures and recursively predicts all later temperatures, using the recorded input schedule. The large gap between one-step and rollout errors is preserved.

Both T1 fits exceed their respective training maximum residual at zero-based validation data indices **37 and 38**. The T2 fits have none in this file. The training maxima are neither distribution-free guarantees nor calibrated future error bounds, and the two outliers remain in all metrics. The code contains no validation-driven model-order search; this is evidence about the inspected fixed comparison, not proof that every historical modeling decision was preregistered or blind to the archive. The coupling result supports this limited model comparison, not unique explanatory superiority of the generative theory.

## Formal composition and remaining assumptions

The command bound is mathematically appropriate: with target and elapsed interval held equal, reading error and retained-integral difference bound raw-command difference; clipping is nonexpansive. Gains need not be positive for the absolute-value statement. Saturation's anti-windup retention and the interior update are separately proved. The real-arithmetic retention equals subtraction of the attempted increment in the original mathematical controller; floating-point cancellation is assessed by numerical replay, not a verified compiler refinement.

`measured_feedback_one_step` directly uses the existing `EmbodiedChoiceScales.controlled_one_step`, supplying a command discrepancy term and retaining the explicit physical response sensitivity. This is a genuine consumer of an established theorem. The horizon theorem uses the existing closed-loop recurrence with a casewise command bound `C`; inserting the derived PI expression requires its reading/memory conditions at each time. It does not prove those conditions emerge automatically from the initial state.

In particular, nonexpansive command clipping does not itself give an invariant retained-memory error bound through all saturation switches. Nor do the archive fits establish plant sensitivity `B`, every defect term, future disturbances or absolute sensor truth. The documents identify these as separate inputs rather than treating a maximum training residual as their warrant. The unresolved-prediction theorem is a conditional nonidentification fact; it does not claim that every fuller physical account permits arbitrary future toggling.

The interpretation keeps measurements, memory, commands and physical response as related aspects of one thermal process. Their analytical separation does not make observation and actuation ontologically independent. Correspondence of commands can be established even while absolute sensor truth and normative standing remain unresolved. Conversely, the thermal record is not falsely identified with the earlier additive-dose toy process or its abstract work tariff.

## Scope of acceptance and next work

This addition establishes a concrete archived feedback correspondence, explains a formerly supplied command-discrepancy premise through an actual controller mechanism, and composes the resulting conditional bound into existing scale results. Independent numerical fitting is now complete at the declared OLS scope. The archive's tuning-objective defect, physical timing contracts, justified future uncertainty, response bounds and practical meaning remain substantive open work.

The broader [three-part completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md) must stay active. This review accepts the local addition; it neither treats source checking as another physical experiment nor converts successful retrospective reconstruction into future protection guarantees.


## Final repair verification

Read the corrected Chinese paragraph: it now names **记录的命令暴露量**, consistent with the English limitation to commanded exposure rather than electrical energy. Read the updated independent-fitting paragraph and final review attribution; they correctly distinguish the new QR verification from physical replication and keep the wider goal active. No required repair remains. No mathematical or numerical source changed for this wording repair, so no additional scientific run was needed.

**Final local verdict: accepted.** Reviewed empirical integration SHA-256 after this repair: `2f948ff17e1efdaa8f4be0fe4074598721a91c8c3390bf84ceb1dce26649e7e5`. All exact source/result bindings in the independent receipts remain applicable. This acceptance does not complete the governing three-part goal.
