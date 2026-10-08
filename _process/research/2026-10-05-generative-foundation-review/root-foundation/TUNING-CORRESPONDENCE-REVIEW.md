# Independent completion review: tuning correspondence

8 October 2026, Asia/Bangkok. AI-authored independent review by the completion-review agent. **Accepted at the stated local scope; no required repair.** This verdict covers the reconstructed tuning procedure, the checked conditional connections, and the constructive limitation on residual transfer. It does not complete the active three-part practical goal or certify all system theories. I reread the final integration, canonical account and completion audit after their acceptance paragraphs were added; those final bytes are bound below.

## What was independently checked

The review preserved its own code, logs, receipts and complete numerical reconstructions in [development/tuning-correspondence-review](development/tuning-correspondence-review/). Author files, historical sources and earlier accepted reviews were not changed. No hardware was operated and no archived hardware script was executed.

1. [Independent Lean runner](development/tuning-correspondence-review/check_lean_review.py) compiled all eight current repository modules in fresh scratch, then ran the complete explicit-declaration axiom audit. [Receipt](development/tuning-correspondence-review/verification.json), [audit source](development/tuning-correspondence-review/Audit.lean) and [axiom log](development/tuning-correspondence-review/axioms.txt) preserve **228 audited declarations**, including **10 new theorems / 14 new declarations**. Compilation was warning-free. Dependencies were limited to the disclosed standard logical axioms; no new custom axiom, proof hole or unsafe proof bypass was found. Current sources, author snapshot, author receipt, import/cache fingerprints and manifest agreed. The reviewer reused the inspected author closure parser, not its main build runner, and reused pinned upstream Mathlib artifacts. The executable fingerprint does not attest every linked runtime dependency; this is not a hermetic toolchain attestation.
2. [Independent grid implementation](development/tuning-correspondence-review/check_grid_review.py) imports no author implementation and uses the Python standard library. It reconstructs all **six × 256 = 1,536** candidate simulations, checks every score, all retained selected trajectories, winners, pair reversals, actual-input validation and the post-hoc diagnostic. Unlike the producer, it retains unweighted integrated error and uses `fsum` for metrics. [Full receipt/results](development/tuning-correspondence-review/grid-verification.json) and [log](development/tuning-correspondence-review/grid-log.txt) pass. The largest discrepancy across retained selected temperature, command and integral arrays was approximately **1.99×10⁻¹¹**.
3. [Independent local solver runner](development/tuning-correspondence-review/check_solver_review.py) repeated the fit with pinned GEKKO 1.3.2 and `remote=False`. Returned coefficients and training predictions were identical to the author values. It separately advanced **one candidate `(10,55)` through all 599 GEKKO ARX loop iterations**, plus initialization. [Solver receipt](development/tuning-correspondence-review/solver-verification.json), [fit log](development/tuning-correspondence-review/fit-log.txt) and [runtime log](development/tuning-correspondence-review/runtime-log.txt) preserve this execution. The absolute runtime objective was **5.606796078037204**; maximum temperature and command differences from the direct recurrence were **4.54×10⁻⁶ °C** and **3.61×10⁻⁵ percentage points**. This is a separate execution using the same fitting algorithm and solver, not an independent solver method or historical software reconstruction. My runtime check covers one candidate; the author's four-candidate runtime check and the complete direct-recurrence grid retain their distinct scopes.
4. [Binding checker](development/tuning-correspondence-review/check_bindings_review.py) verified the preserved archive, extracted optimizer and both validation members, duplicate training bytes, producer/receipt/log hashes, reviewer scripts and receipts, and inspected final prose. [Binding receipt](development/tuning-correspondence-review/bindings.json) passes. The 599-row optimizer training member is byte-identical to the initial-run file; its second-heater command is zero throughout. It is one observational source, not an additional experiment. This review checks local preserved provenance; it does not independently remeasure the physical apparatus.

## Formal content and its correspondence

The new objective results consume the earlier movement and exposure bounds with matching indexing. For 599 positions the formal objective uses 599 tracking terms and 598 command differences: `objective ... 598` contains `tracking ... 599`. The numerical objectives divide by the same positive 599, preserving the finite comparisons. `objective_error` needs both temperature and command error radii and retains the absolute value of the supplied movement weight. It does not manufacture those radii from a residual maximum.

`finite_model_minimum` genuinely specializes the imported finite-frontier theorem to a supplied scalar order and nonempty finite menu. It establishes existence in that menu, not physical feasibility or a global optimum. `estimated_minimum_actual_regret` requires warranted error bounds for both the selected candidate and its competitor. The separated-comparison theorem likewise consumes sufficiently separated warranted intervals. These are useful composition results whose premises remain visible.

The ARX family uses the same second-order recurrence, common initial values and gain-scaled input coefficients. The input-history difference theorem derives its scaling through that recurrence. Compensating each model by its own original-record residual then makes every corrected model agree with the original record, while distinct gain multipliers disagree where the changed-input response is nonzero. The exact-fit identity alone is simple; the substantive nonidentification is the coherent changed-input difference. This meets the nondual method's requirement for a rival preserving the specified target rather than freely toggling an unrelated success predicate.

The theorem concerns exact real sequences; the fitted floating coefficients, initialization and solver realization have separately checked numerical correspondence. In these data the first two training temperatures and first target equal 21.22, the first command is zero, and the stationary latent initialization agrees to roundoff. This accounts for the common-initial-value correspondence here; it is not a proof that arbitrary stationary and measured initializations coincide.

`calibrated_protection_at_actual` directly combines indexed protected-condition margins with the imported robust-at-actual implication. Actual-case inclusion and every relevant calibration are supplied. An engineering score supplies neither living standing nor G0/J application warrant, and the theorem does not hide a universal duty or weighting judgment in successful tracking. The review accepts the explicit axiom route and does not impose assumption-free normative grounding as a new local completion gate.

## Numerical findings, including failures

The reconstructed source contract selects `(10,55)` under both metrics. Signed-to-absolute correction reverses **8,454 of 32,640** candidate pairs while leaving that winner unchanged. The corrected objective is **5.6067968276**, with a gap of about **0.0006131212** to the next candidate. Thus the preserved metric discrepancy does not justify declaring the reported selected gains wrong. The independent GEKKO runtime check supports numerical realization at the checked candidate; it does not upgrade the complete grid to a full runtime replay.

All other disclosed contracts reproduce as well:

| Contract | Signed winner | Absolute winner | Absolute winning cost | Absolute excess from signed selection |
|---|---|---|---:|---:|
| Recorded PI intervals | (10,55) | (10,55) | 5.606947744 | 0 |
| No residual transfer | (25,80) | (10,60) | 5.553658236 | 0.297541935 |
| Compensated input gain ×0.8 | (10,50) | (10,50) | 5.529762010 | 0 |
| Compensated input gain ×1.0 | (10,55) | (10,55) | 5.606796837 | 0 |
| Compensated input gain ×1.2 | (20,80) | (5,80) | 5.606449323 | 0.269610089 |

The remaining pair-reversal counts are respectively 8,488; 9,368; 14,290; 8,454; and 4,818. The source grid order and last-tie rule are retained. The compensated family reconstructs the original observations exactly in the reported numerical calculation; the source residual uses rounded GEKKO predictions, accounting for the approximately **3.99×10⁻⁶ °C** direct-recurrence mismatch. The residual-free ablation is not mislabeled as another exact-fitting member. Neither ±20% nor exact historical fit establishes physical admissibility of the gain family.

The residual is added to the controller's readout, not propagated into latent ARX state. This distinction is essential and is implemented faithfully. The recorded-interval variant changes the PI update interval only; the ARX recurrence stays a discrete event model. It therefore does not test a variable-step physical heat law.

The validation computation holds fitted coefficients fixed and initializes from only the first two measured temperatures. Subsequent output prediction uses the actual recorded commands; later temperature observations enter error assessment, not recursive prediction. This is free output rollout conditional on known input histories, not an advance forecast of unknown future commands. Original training residual transfer raises RMSE from **0.2551230635 to 0.2953654864 °C** on validation 1 and **1.9507069162 to 1.9561025433 °C** on validation 2. The second run's MAE slightly improves, which the prose correctly preserves. These findings defeat exact transfer on the inspected records without identifying a unique physical cause or proving every residual model useless.

The post-hoc initial-reference adjustment changes only the intercept using the initial-reading difference. It worsens validation 1's residual-free RMSE to **1.0563956203 °C** while improving validation 2 to **1.7079378097 °C**. Initial reading is not established as ambient temperature. The failed general repair is retained rather than selected retrospectively only where favorable. Neither validation residuals nor fitting duration yield future sensor-error, plant-response or deadline certificates.

## Scope, bindings and acceptance

The final account preserves differentiated relations within the same feedback history: measurement, retained integral, command, latent response, fitted discrepancy and comparison. It distinguishes what these analytical representations preserve and omit. Physical action reconstruction remains positive evidence; model-generated responses are not relabeled as observed counterfactual interventions. More movement or commanded exposure remains a real engineering tradeoff; electrical energy, ecological burden and ethical significance require additional correspondence.

The local study explains the previously supplied finite candidate-generation mechanism and resolves the source metric discrepancy's effect in this reproduced setting. Its exact-fit family and held-out failures identify the next missing warrant more precisely. The current completion audit appropriately keeps justified measurement/model domains, actual timed feasibility and warranted common practical response open. Acceptance is therefore substantive local completion, not completion of that wider goal.

Exact SHA-256 bindings of the inspected final sources:

| File | SHA-256 |
|---|---|
| `TUNING-CORRESPONDENCE-INTEGRATION.md` | `b926da5dc5e53dd980d9e77e35c0041abe090efc8b8b8e28ffe49ac44b1a7049` |
| `THREE-CONNECTIONS-COMPLETION-AUDIT.md` | `99ce2ecec1825c6e6aa05f6daa084bff21c0dd46eb3ef46eca778d1f7e22f6d5` |
| Canonical `MEASURED-FEEDBACK-CORRESPONDENCE.md` | `55743873ca3a8187e35d86d38e188fb80abe25715b003c4b2650e5fcd60c0922` |
| `TuningCorrespondence.lean` | `7847db35b99929a4164e9e1327c4b20335a2f520598f63c032535f062444977a` |
| `check_tuning_correspondence.py` | `1a55d78e5cb1677138e9ae9c0879079c16a1384bd68be87cc286d397f01b13c4` |
| Author Lean receipt | `f6bc46877f6910e10d7876664e7b3f74081e746f47b33b2e6a987ed6110eb961` |
| `tuning-model.json` | `97b77bba763f59e2e9fe51c278dc0a1c30cf2ec0a2c90ee64ba5834b555ad8f6` |
| `tuning-results.json` | `7cd427c33013e2ef925fb480f85903af97b70454beb03288275079311af2c6b3` |

Machine-readable binding schema: `bindings.json` has `status`, `checked_at_utc`, `script_sha256`, `document_sha256` and `file_sha256`; both latter objects map repository-relative paths to SHA-256. `verification.json` contains `source_sha256`, declaration dependencies and build/log bindings. `grid-verification.json` contains the full independent comparisons, validation/diagnostic results and producer/input hashes. `solver-verification.json` contains `independent_refit`, `runtime`, package/solver/input hashes and log bindings. These preserve exactly which evidence supports the verdict; a later document-only binding check is not a new scientific rerun. Prior memory-review bindings remain historical and untouched.
