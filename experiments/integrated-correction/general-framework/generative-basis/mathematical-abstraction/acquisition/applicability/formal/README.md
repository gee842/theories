# Acquired applicability: formal law and execution correspondence

This formalizes the [accepted native continuation](../README.md) under the [research contract](../../../../../../../../_process/research/2026-10-05-generative-health/succession/ACQUIRED-APPLICABILITY-FORMAL-CONTRACT.md).

**Status:** [accepted combined closure](runs/20261006T090706Z-1791277626988980000/receipt.json), with six fresh-compiled modules, 454 audited explicit declarations with empty axiom dependencies, 21 stable source bindings and all 65 finite correspondence certificates. See the [independent review](../../../../../../../../_process/research/2026-10-05-generative-health/succession/ACQUIRED-APPLICABILITY-FORMAL-REVIEW.md) for interpretation and trust boundaries.

- [AcquiredApplicability.lean](AcquiredApplicability.lean) defines exact resource charges, source effects, acquired evidence, committed updates, the selected next encounter and the actual scheduling policy.
- [ApplicabilityProofs.lean](ApplicabilityProofs.lean) proves the general preservation, conservation, evidence-update, interruption and selection claims and connects histories to the existing generative `Process`/`Trace` framework.
- [ApplicabilityGrounding.lean](ApplicabilityGrounding.lean) derives the true family member from the declared sensor/extraction coupling and connects it to faithful updates. This witness is not supplied to the controller.
- [check_correspondence.py](check_correspondence.py) reads saved results and accepted native bindings, reconstructs the formal projection, generates 65 kernel-checked certificates, and performs a fresh isolated build and complete named-declaration audit.
- [Research integration](../../../../../../../../_process/research/2026-10-05-generative-health/succession/ACQUIRED-APPLICABILITY-FORMAL-INTEGRATION.md) states the result, projection and supplied premises.

From the repository root, reproduce the formal check with:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/applicability/formal/check_correspondence.py
```

The checker requires the recorded Lean 4.29.1 binary and verifies its hash. It does not run the Python producer or overwrite the earlier native receipt. Every run creates a distinct `runs/` directory with frozen source, finite fixtures, projection, build logs and a receipt. Failed runs remain available.

The finite certificates check guarded event words, exact policy selection, projected state and observation histories, final error and termination. They cover 1,008 operations and 1,073 state points in the 65 saved continuations. They are distinct from the earlier Python reconstruction of 2,033 complete native snapshots. Thirty-five extraction endpoints require an explicit reconstruction before the next receipt charge; 973 operation endpoints are directly recorded. All 916 saved native charge equations are checked separately by the correspondence script.

General theorems concern the declared Lean law. Finite execution correspondence does not prove refinement of every Python input, re-prove earlier acquisition, establish empirical adequacy, or derive the applicability family and evidence calibration. The broader foundation remains open at its own completion scope.
