# Acquired evidence, calibration, revision and supported reuse

8 October 2026, Asia/Bangkok. AI-authored continuation of [Ren’s research direction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md), following the [variation and recovery study](EXPLANATORY-VARIATION-INTEGRATION.md). The [current account](../../../../theories/becoming/history/EXPLANATORY-NECESSITY.md) integrates these results into the explanatory-necessity investigation. This is a same-agent constructive study and counterreview, not an independent review.

**Five conditional bridges are joined:** available supported operations → acquired positive/negative evidence → calibrated judgment → invalidation under change → supported reuse/correction and actual continuation. **40 new Lean theorems pass; 128 empty axiom-dependency audits include 88 inherited declarations.** The result is a connected finite-history mechanism with explicit failure rivals, not universal epistemology or unique ontological grounding.

## 1. Target, genealogy and method

The previous study distinguished a complete response profile from actually acquiring it, and constructed records preserving pre-change differences. Its next open connection was the acquisition of negative as well as positive evidence, calibration and reuse after change. This study closes that connection for a specified noiseless gate/signal mechanism. It directly reuses `KnowledgeCorrespondence.calibrated_pair_exact` from the [existing knowledge formalization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/KnowledgeCorrespondence.lean); the XOR decoder is not a new discovery. See the [knowledge correspondence account](KNOWLEDGE-CORRESPONDENCE.md) and [current knowledge theory](../../../../theories/becoming/chapters/KNOWLEDGE.md).

The existing [semantic-calibration study](../../../../theories/becoming/history/SEMANTIC-CALIBRATION.md) already distinguishes acquired evidence from copied agreement, and identifies silent relation change and common corruption as failures. Those insights are credited, not claimed as first discovered here. Its original updater, correspondence and validation scopes remain unchanged. This study supplies a new joined gate mechanism and checked from-valid-start failure histories at the present interface. The concurrent [knowledge revision account](KNOWLEDGE-REVISION-AND-OBJECTIVITY.md) also distinguishes historical truth, present grounds and changed questions; it is a philosophical integration, not a new theorem counted in this package.

What is new is the connection of that supplied pair to events that produce it, revision-sensitive preservation over arbitrary finite histories, resource-limited reuse, and concrete altered mechanisms that break correctness. Earlier learning, selector revision and inquiry/judgment studies retain their results: this mechanism does not derive a new learning algorithm, discover its own decoder or justify an ethical standard.

Following the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md), gates, signal orientation, prepared reference, record effects, judgment and support are coordinates of one unfolding. Reading and acting are event roles within it. There is no independently supplied observer/environment split. Their separation preserves the declared dependencies and omits microscopic implementation, noise, uncontrolled drift in the lawful model, reference manufacturing, resource replenishment and the origin of the decoding organization. The model does not claim that these omissions are absent from reality.

## 2. Exact model contract

`State` extends the preceding gate configuration with a Boolean channel orientation, natural-number revision, optional reference state, optional target/reference/judgment receipts and inquiry fuel. A receipt contains a revision and a Boolean. Revision is an ideal change counter, not wall-clock time, and is not a universal prerequisite for knowledge.

| Input or law | Exact content | What it does not establish |
|---|---|---|
| Target and correspondence | Target is the current left-gate Boolean; right gate and passage status are separately represented | All relevant properties of a real apparatus have been represented |
| Reference preparation | `prepare` forms `some false`; `readReference` samples whatever reference is actually present | Real reference production or independent empirical certification |
| Shared channel | Target and reference signals use the same XOR orientation while that orientation is unchanged | Noise tolerance or unrelated sensor channels |
| Revision coverage | Every native gate event and channel reversal increments the revision; receipts remain stored | Detection of every real change; selective minimal invalidation |
| Judgment operation | Two receipts of the current revision are XOR-decoded; the operation does **not** test truth or `Valid` | Formation of the decoder, rational agency or automatic choice to judge |
| Supported execution | Each prepare/read/judge consumes one natural-number unit; native gate support remains the preceding separate support relation | A universal positive cost, money, a common physical unit or a replenishment law |
| Initial validity | Initial receipts/reference are absent; gate values and orientation may be arbitrary | Every possible initial state is trustworthy |

The decoding operation has an ordinary syntactic revision guard. `Valid` is a proved invariant, never a truth guard on allowed events. `RecordValid epoch value record` requires (i) no future-stamped receipt and (ii) correctness when the receipt revision equals the current revision. Old receipts may remain stored without being asserted to describe the present. The no-future-stamp clause is essential to the induction: a fabricated future stamp must not become certified merely because revisions advance.

## 3. The five bridges and exact proof map

All declarations below are in [ExplanatoryInquiry.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryInquiry.lean). The counts cover all 40 new named theorems, including supporting lemmas and explicit witnesses, not 40 separate philosophical discoveries.

| Bridge / support | Theorems (new count) | Checked result |
|---|---|---|
| Record validity and inherited decoding (6) | `empty_record_valid`, `new_record_valid`, `revision_invalidates_old`, `standard_is_false`, `inherited_pair_decode`, `fresh_pair_decodes` | Valid reference/target receipts of one revision decode the current target; aging a previously bounded receipt removes its current claim |
| Arbitrary lawful histories (3) | `valid_step`, `valid_trace`, `initial_valid` | All finite traces beginning with valid records preserve validity, including arbitrary interleavings and repeated changes |
| Positive/negative evidence and operational meaning (4) | `current_judgment_correct`, `current_negative_is_evidence`, `current_positive_allows_pass`, `current_negative_blocks_pass` | A current false judgment excludes immediate passage; a current true judgment enables passage when the right gate is open and passage has not occurred |
| Actual acquisition and repair (5) | `no_reference_before_preparation`, `no_judgment_without_readings`, `acquisition_realized`, `acquired_record_exact`, `acquisition_repairs_records` | Reference/records must actually be formed; four supported events produce exact receipts and repair arbitrary supplied malformed records by overwriting them |
| Resource accounting (4) | `fuel_step`, `fuel_trace`, `acquisition_requires_four`, `insufficient_fuel_blocks_acquisition` | Exact conservation for every finite history; the specified four-event acquisition requires four units |
| Change and retained-reference reuse (4) | `stale_reference_blocks_judgment`, `reversal_realized`, `reversal_blocks_old_pair`, `reference_reuse_realized` | Tracked reversal blocks judgment from the old pair; with a still-current reference, target reading plus judgment suffices in two events |
| Connected correction and real losses (8) | `cycle_first_acquisition`, `cycle_changes_target`, `old_negative_retained_but_stale`, `cycle_restores_positive`, `cycle_realized`, `cycle_preserves_validity`, `cycle_actual_losses`, `correction_cycle_requires_eight` | One actual history acquires false, releases the left gate, retains an obsolete false judgment, reacquires true and passes; it exhausts eight inquiry units and the native release support |
| Concrete failure mechanisms (6) | `untracked_drift_can_mislead`, `fresh_stamp_is_not_sufficient`, `wrong_reference_can_mislead`, `lawful_history_retained`, `untracked_failure_from_valid_start`, `bad_preparation_from_valid_start` | A same-stamped false conclusion can arise from untracked channel reversal or incorrect reference preparation; both failures have traces from valid starts in an explicit weakened process |

`acquisition_realized` proves existence of the fixed path when `fuel = n + 4`; it does not prove execution despite arbitrary interference, inevitable inquiry, controllability or a strategy that detects unknown faults. `acquisition_repairs_records` is coupled to that actual path; its conclusion for the named endpoint alone does not cause the endpoint to occur.

`current_negative_blocks_pass` excludes immediate passage in this process. It does not establish permanent impossibility: the joined correction cycle is a checked counterexample to that overreach. Likewise a true left-gate judgment alone does not supply an open right gate or erase an already-passed status.

Four units is a lower bound for the specified four-event word, not all ways of knowing. `reference_reuse_realized` constructs a two-event alternative under stronger initial evidence conditions. Eight units belongs to the stated full correction word, not a universal minimal repair cost. The second full preparation is a sufficient robust reset, not asserted optimal.

## 4. Why the failure tests are substantive

`FaultyStep` preserves every lawful transition and adds two concrete events: reversal of the channel without updating the revision, and preparation of a true reference where the decoder expects a false reference. It changes actual acquisition conditions; it does not freely toggle a detached correctness predicate. `lawful_history_retained` proves inclusion of all lawful histories.

The first failure starts from the same valid eight-unit initial state, lawfully acquires negative evidence, undergoes an untracked reversal, reads the target again and combines that new reading with the old reference. Both receipts bear the same stamp; the resulting true judgment is false of the still-closed gate. The second starts from an empty valid four-unit state and uses erroneous preparation before otherwise lawful reading and judgment. These are counterexamples to extending the correctness guarantee to those weakened laws. They do not contradict the theorem under its declared coverage/reference assumptions.

Conversely, changing the gate with the lawful release event preserves the old negative record while the gate becomes open. The old assertion concerns the earlier revision and remains historically correct. Its loss of present authority is not falsification of its earlier content. Reacquisition forms a new positive judgment; actual passage follows under the other gate conditions, and all costs remain in the same history.

## 5. Counterreview and disposition

- **Was truth smuggled into allowed judgment?** No: the judge checks equality of revisions, then applies the inherited decoder. Semantic validity is proved from formation/preservation laws. Those laws themselves remain supplied premises.
- **Is timestamp agreement enough?** No: the fully realized untracked-drift counterexample defeats this stronger claim. Revision coverage must be implemented and justified for the relevant changes.
- **Does resetting records create truth by definition?** The endpoint definition displays the intended result; the four explicit transitions prove its realization using the supplied sensing/reference laws. Those laws require a further physical correspondence.
- **Does this explain failure by failure-to-pass observation?** No. The negative evidence is a generated Boolean target reading calibrated against a reference. This avoids treating absence of an admissible path as an already-acquired observation. Failure sensing by timeout remains unmodeled.
- **Does every gate event really require full recalibration?** Not necessarily. The single revision conservatively invalidates even unchanged target content. This is safe within the model but may waste evidence and support. The two-event reuse result applies only when the reference remains current; it does not yet derive selective validity under partially changed dependencies.
- **Has a global explanatory rival been eliminated?** No. A whole-history description containing these acquisition, revision and failure relations can preserve the same answers. It cannot be dismissed by comparing it with a bare unchanging answer table. The question of explanatory priority remains open.
- **Has the universal ethics objective advanced by another local dynamics construction?** This authorized explanatory branch supplies a precise correspondence requirement for reliable factual premises used in practical judgment. It does not justify G0, comparisons, universal normative force or action compliance. It leaves the independent ethical route intact.

The outcome is a stronger conditional content requirement: explaining reliable, reusable judgment requires accounting for the relevant formation and preservation of its evidence, not just exhibiting a currently correct output. This is an inference from the specified contrasts, not a proof that all possible explanations must use this formulation.

## 6. Primary sources and evidence assessment

The inherited [knowledge source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/KnowledgeCorrespondence.lean) provides the exact shared-orientation decoding theorem. We import and audit that declaration directly. The whole knowledge module contains some other results using classical axioms; this study makes no claim that its entire theorem inventory has empty dependencies. The printed audit of the exact declaration used here and every new theorem is empty.

[NIST’s policy on metrological traceability](https://www.nist.gov/calibrations/traceability), read 8 October 2026 local time, introduction and policy items 1, 3 and 5, distinguishes supported calibration chains from mere provenance labels and states that traceability alone does not ensure fitness for a measurement purpose, including adequate uncertainty. This is a primary-source comparison of scope, not empirical validation of the Boolean model. Our exact model has no uncertainty budget, laboratory standard or measured apparatus; it must not be presented as a verified metrological implementation. Link-only reference; no source bytes imported or translated edition substituted.

The prior [source assessment](EXPLANATORY-VARIATION-INTEGRATION.md#8-primary-source-assessment) concerning Pearl, Peters and Adlam retains its earlier reading scope. No new uniqueness or absence-of-predecessors claim is made. Same-content global accounts remain substantive rivals. The affirmative mechanism, the two actual failure processes and this source assessment jointly motivate the next bridge below.

## 7. Actual verification and dependency audit

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_inquiry.py
```

Final immutable [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-inquiry-checks/20261007T212138.087503Z/receipt.json): Lean 4.29.1; seven source modules compiled in a fresh temporary directory. **40 new theorem audits + 87 inherited core/necessity/variation/recovery audits + one reused knowledge theorem = 128 empty audits.** The knowledge module emits no inherited audit list; its one used theorem is explicitly printed in the new module. Empty lists mean no Lean axiom dependencies, not zero mathematical or correspondence premises.

The checker rejects explicit proof holes, nonempty printed axiom dependencies, warnings and mismatched audit counts, and binds frozen source/log snapshots with SHA-256. Intermediate failed and successful receipts remain historical development records; their counts are not added together. The final receipt binds the final code. The [document/index checks](EXPLANATORY-INQUIRY-CHECKS.json) and [owned index edit record](EXPLANATORY-INQUIRY-INDEX-EDITS.json) separately cover integration and preservation, not new scientific evidence.

## 8. Integrated conclusion and next unresolved bridge

The previous outstanding acquisition/calibration/reuse connection is now complete **for this mechanism and its stated laws**. The next connection is **dependency-sensitive evidence validity → selective recalibration after change → generated monitoring of those dependencies**. Reuse existing learning/inquiry results where applicable. A blanket revision counter should be replaced by a justified account of which retained relationships still support which claim; detection cannot merely be assumed complete.

A result would change the account if it showed an equally accurate supported method requiring less supplied revision knowledge, or a concrete failure in which the proposed dependency test certified a misleading combination. Compare a global description retaining the same dependencies, resource conditions and counterexamples. This advances the missing explanation of calibration coverage; another proof for an assumed perfect change detector alone would leave that bridge open.

## Subsequent direction: direct uniqueness test

Ren next authorized testing the universal-uniqueness route against matched global and mathematical explanations. [The new study](EXPLANATORY-STRUCTURE-INTEGRATION.md) adds 32 checked theorems on relative reduced-presentation uniqueness and local/global coverage, with an explicit standard-logic dependency audit. This preserves the present acquisition study and its 40-theorem receipt. Its proposed monitoring continuation remains available; the newly authorized central test now concerns composition-sensitive uniqueness rather than another calibration mechanism.
