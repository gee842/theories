# Frozen comparison: does the outcome-to-turnover arrow earn its place?

5 October 2026 task date. AI-assisted synthetic model comparison. Frozen before computing the new rival. The earlier full-model results are already known; this is not a blind forecast or empirical validation.

## Models and calibration information

Reuse the finite formation kernel in `../../gap-resolution/formation-coupled/analyze.py`. Its feedback model has turnover probability `.05+.20*(realized harms/cases)` after each round. Construct one specific rival with constant turnover probability `.15`; every other physical, work, complaint, nomination, ratification, appointment and transmission rule remains the same.

The rival's sole parameter is calibrated to the exact population mean turnover probability under an **execution-blocked** baseline. In that regime ordinary actions are zero and experimental actions are randomized, so expected harm proportion is .5 at every underlying state. Thus mean turnover is exactly .15. This is population-level synthetic calibration, not parameter estimation from a real finite sample or a claim of perfect fit to all observables.

Calibration channels are the complete projected histories of skill `k`, installed volume/adaptive practice `q`, and turnover events. Do not include complaint, linked records, chosen work portfolios, realized harm, or service-volume histories in a claim of equivalence. The models can differ on those channels before the intervention.

## Fixed predictions and controls

1. Prove and check that execution-blocked models have the same event-labeled projected kernel on `(k,q,turnover)`, for every compatible reachable underlying state. Training before turnover and successor appointment depend only on `(k,q)` and the event; mean turnover is .15. Consequently they have equal projected path laws and skill-retention curves from the same initial projection.
2. Beginning from the same original full initial state, separately run execution enabled and blocked in both models for 25 rounds. Primary diagnostic: the enabled-minus-blocked difference in probability that skill remains at round 25. The constant-turnover rival predicts zero; the feedback model can differ. Report both within-model contrasts and their difference, not only an unpaired difference between model outputs.
3. A second declared intervention changes linked inquiry to the supplied uniform-nomination aggregate procedure. Compare linked-minus-aggregate skill retention within each model. It does not compare the best possible aggregate learner or force equal realized total work.
4. Report probability of a retained compliant ordinary-service response, frame retention, and ordinary/inquiry service and harm counts separately. The ordinary-response endpoint excludes the harm of randomized inquiry; it is not whole-behavior safety or a normative ranking of the models.
5. Check one-round turnover forecasts from common full states with correct, reversed and irrelevant-feature frames, enabled and blocked execution. Under enabled execution, full-model expected turnover should be .08, .22 and .15; rival .15 in all three. Under blocked execution both predict .15.

No parameter sweep, fitted extra correction term, alternative horizon or outcome selection after seeing the results. Preserve any failed predictions. The comparison distinguishes these two specified models, not every conceivable explanation without this arrow.

## Verification and scope

The new transition code imports the original physical and decision helpers but writes out the joint transition calculation explicitly, changing only the turnover function. Reproduce all six saved full-model endpoint vectors and cumulative rewards; this checks that the adaptation did not change other mechanisms. Verify probability mass and work accounting. Check the projected transition identity against an independently constructed six-state/event kernel and all execution-blocked reachable states, including states appearing after period 25 until the graph closes.

Save the original source hash, protocol, code and numeric output. This is an identifiability/design result under supplied models. Real data would additionally require trustworthy measurements, intervention assignment and control for other pathways. Joint harm–turnover association alone does not rule out shared severity or workload causes. A test of both arrows in a feedback loop needs corresponding time-ordered interventions, as specified in the separate study-design analysis.
