# State audit for branching at the demand shift

An exact branch can be taken immediately before epoch 80 production, after epoch 79 governance, using three mutable arrays and the absolute epoch index. All branches must inherit the same submissions, rubric, and authority stock. Their future random draws are already indexed by purpose and absolute epoch, so no mutable random-generator state needs to be restored.

This audit inspects [benchmark.py](benchmark.py), [the original protocol](PROTOCOL.md), [the original report](REPORT.md), [the structural tests](test_benchmark.py), and [the sealed input manifest](results-v1/input_manifest.json). It specifies a refactor and required regression checks. It does not run a branching experiment, report new outcomes, or modify the original inputs.

## Exact intervention boundary

The existing code uses zero-based epochs 0 through 159. In the shift context, independent usefulness changes from alpha 0.75 to 0.25 at epoch 80. The desired state is after every operation at epoch 79 and before the first production round at epoch 80.

Epoch 79 is a correction-opportunity day because `(epoch + 1) % 20 == 0`. Its evidence and amendment are evaluated with the old alpha, 0.75, and its resulting rubric is inherited by every branch. Branching before that amendment would be a different intervention. The next scheduled evidence opportunity is epoch 99; the final opportunity that can govern a subsequent production epoch is 139. Epoch 159 has production and updates the internal authority average, but has no governance or correction event.

Do not obtain the prefix by changing the configuration’s total epoch count to 80. That would move the demand change to epoch 40 and make epoch 79 terminal, suppressing the amendment that the intended branches should inherit. Execution boundaries must be separate from the unchanged total horizon of 160.

## State that must be preserved

| State or input | Exact source at the boundary | Why it matters |
|---|---|---|
| `next_epoch` | Integer 80 | Controls the environmental shift, evidence schedule, random indexing, and terminal condition. |
| `rubric` | Copy of `after_rubric[:, 79, :]` | This is the rule applied during epoch 80 production. |
| `outputs` | Copy of `frozen_outputs[:, 79, :, :]` | The next simultaneous production response uses rivals’ previous submissions. Resetting these changes the initial strategic state. |
| `authority` | The exponential moving average after updating with epoch 79 mean contract shares | Endogenous appointment depends on the full inherited authority stock, not only the last observed shares. |
| Configuration and context | The unchanged sealed configuration and context `shift` | Several timing and decision rules depend on the total horizon and context. |
| World identities and immutable arrays | The same seeds, skills, features, and precomputed random arrays in the same row order | They determine abilities, action outputs, and the coupled future exogenous shocks. |
| Replay path, if replay is included | Explicitly specified before and after rubrics and administrative costs, indexed by original epoch | Replay has an additional externally supplied path and overwrites the rubric before each epoch. |

There is no additional learned policy, wealth balance, amendment debt, pending event, or persistent private observation in the current implementation. Temporary values such as scores, `true`, `p`, and candidate utilities are recomputed within the next epoch. History arrays are receipts, not state used by subsequent decisions.

The authority stock is not logged directly, but it can be reconstructed exactly from archived mean shares. Start with the same float array `np.full((worlds, agents), 1 / agents)` and apply, in order for epochs 0 through 79,

```python
authority = (1 - cfg["authority_memory"]) * authority + cfg["authority_memory"] * history["shares"][:, epoch]
```

This repeats the original arithmetic on the same stored doubles. Do not substitute a closed-form weighted sum, parallel reduction, or a library moving-average filter: different summation order can change floating-point bits. Do not replace the stock by epoch 79 shares or a uniform distribution. Archive the reconstructed stock explicitly in the new snapshot, along with its provenance and checksum.

The endogenous and independent branches should retain the same stock even when independent appointment does not use it to choose a governor. This keeps the intervention confined to the appointment rule. Similarly, a branch called fixed should freeze the inherited rubric; resetting it to the original initial rubric is a different treatment.

## Minimal implementation approach

Keep `benchmark.py`, `config.json`, `PROTOCOL.md`, their archived copies, and all original results unchanged. Add a separate branching module and new protocol/configuration. It can reuse the unchanged functions for action construction, world generation, evaluation, production, candidates, softmax, and sampling.

The smallest reliable extraction separates initialization and the epoch loop:

1. A snapshot object holds `next_epoch`, `rubric`, `outputs`, and `authority`, plus references or hashes identifying the immutable configuration and worlds.
2. A segment runner accepts a snapshot and independent `stop_epoch`, preserving the original loop body and arithmetic order. Its loop uses absolute epochs, and all shift, evidence, and terminal tests continue to use the original total horizon.
3. Each treatment receives deep copies of the mutable snapshot arrays. The runner returns the next snapshot and receipts. Immutable world arrays may be shared read-only.
4. Saved suffix traces include an explicit absolute epoch vector. If a full-length receipt layout is retained for implementation simplicity, either merge the unchanged prefix explicitly or clearly mark unexecuted prefix slots. Zero-filled slots must never enter outcome summaries as observations.

The fixed and replay paths currently return early from governance processing, leaving some receipt fields at their initialized values. Preserve that behavior in the regression comparison. Candidate values contain NaNs where no candidate calculation occurred. Preserve the original rubric cleanup tolerance and operation order, including the authority update before appointment and the frozen-submission rescore before amendments.

An implementation should reject mismatched state dimensions, epoch bounds, seed order, context, or input hashes. It should not silently reinterpret an incompatible snapshot. The saved snapshot format should carry a schema version and the code version that generated or reconstructed it.

## Matched randomness and timing invariants

`make_worlds` precomputes separate streams for skills, production responses, appointments, amendment choices, and rotation. Continuation must reuse `prod[:, epoch, round]`, `appointment[:, epoch]`, `amendment[:, epoch]`, and `rotation[:, epoch]` at their absolute indexes. Do not reseed, restart arrays at zero, or draw sequentially from a new shared generator after branching. Treatment-specific paths must not consume or shift other streams.

The same appointment uniform does not imply the same appointed governor when appointment probabilities change. The same amendment uniform does not imply the same choice when the governor or utilities differ. These are the intended treatment responses. Balanced rotation must retain the precomputed schedule at the original epoch, not begin a newly shuffled rotation cycle merely because execution resumes.

For branches that do not override the inherited rubric before epoch 80 production, the following must be identical at that epoch: starting rubric, every production-round submission, gross usefulness, mean shares, frozen outputs, and the authority update computed from those shares. Appointment differences first occur after epoch 80 production. Their effects on gross usefulness can therefore begin at epoch 81. Net usefulness may differ at epoch 80 because the governance packages have different modeled administrative costs.

Replay requires special care. The current replay arm replaces its rubric before epoch production with the donor’s rule. Applying an unmatched donor’s epoch 80 rubric would immediately break the identical-state intervention. Either exclude replay from the primary matched-state comparison or specify a donor path compatible with the exact inherited state. A new mechanism for reconciling incompatible donor paths would be an additional intervention, not ordinary replay.

The original manifest records Python 3.11.2, NumPy 2.4.6, and SciPy 1.17.1. Use the same available runtime and preserve NumPy array dtype and arithmetic order for the bitwise regression gate. If exact reproduction fails across a different runtime or numerical backend, report the mismatch and resolve it before interpreting new treatment effects; a tolerance check should not silently replace the promised exact regression.

## Required regression checks

These are requirements for the branch implementation, not tests executed by this audit.

| Check | Required result |
|---|---|
| Original artifact integrity | Every original sealed input hash still matches the archived manifest; original result files are unchanged. |
| Initialization equivalence | Starting the extracted engine at epoch zero reproduces the original runner on a small structural fixture, with every arm tested and the original total horizon preserved. |
| Direct snapshot versus reconstruction | The authority array captured after epoch 79 equals the sequential reconstruction from saved shares bitwise; rubric and outputs equal the matching archived arrays. |
| Same-arm continuation | Restore the endogenous epoch-80 snapshot and continue with endogenous appointment. Every suffix receipt equals `results-v1/shift-endogenous.npz` from epoch 80 onward, including rubric paths, shares, candidate values and validity, proposals, governors, outcomes, and costs. Compare shape, dtype, and raw array bytes, not merely aggregate means. |
| General segment equivalence | For small fixtures, a run split at several boundaries reproduces the unsplit run for each supported arm. Include a boundary immediately before the shift, after an evidence day, and before the terminal epoch. |
| Serialization round trip | Saving and reloading a snapshot preserves every mutable array bitwise and produces the same suffix as continuing the in-memory snapshot. |
| Branch isolation | Running one treatment leaves the shared source snapshot and immutable random arrays unchanged. Treatment execution order does not change any arm’s output. |
| First production epoch | All matched non-replay branches have identical epoch-80 production receipts and gross output. Differences before the first postbranch governance action fail the test. |
| Calendar preservation | Alpha is 0.25 from epoch 80 onward; the first postbranch evidence day is 99; terminal epoch 159 has no governance; the inherited epoch-79 amendment remains present. |
| Wrong-clock negative test | A deliberately restarted clock or truncated total horizon must fail equivalence. This ensures the regression can detect the most consequential boundary error. |

Compare uncompressed arrays. The bytes of an NPZ container can differ for packaging reasons while its arrays are identical. Ordinary approximate equality is too weak for the promised bitwise regression. Conversely, numerical equality alone can ignore signed-zero or NaN-payload differences: require identical shape and dtype and compare the C-order raw array bytes, or hashes of those bytes. For diagnostic messages, report the first differing receipt and epoch as well as whether the difference changes a discrete choice.

The same-arm suffix gate uses already observed outcomes solely to check implementation identity. It should not be used to choose new hypotheses, endpoints, sample exclusions, or parameter settings. Seal the new branching protocol and code before running novel treatment continuations.

## Interpretation limits

This design estimates the effect of changing postshift governance from a common inherited state distribution. If all prefixes are endogenous, its conclusion is conditional on states produced by endogenous pre-shift governance. It does not estimate the effect of the appointment constitution over an institution’s entire history, nor does it erase the original stable-demand reversals.

All intended worlds should branch, including worlds without a qualifying correction opportunity. After the branch, opportunity sets and future submissions can diverge because treatments act differently. Conditional correction rates then remain selected, descriptive measures; they do not become causal measures merely because the initial state was matched. A primary outcome should use the same fixed postbranch time window for every world, with correction-response receipts reported separately.

Uniform independent appointment changes who is selected and the distribution of tenure. Protected correction additionally supplies a veto and mandatory oracle-backed correction. Fixed governance removes adaptation rights. These are distinct packages. Matched starting states remove inherited-state differences from their postshift comparison but do not identify every component or establish a mediated effect through evaluator identity alone.

The world remains the independent statistical unit. Treatment worlds share their prefix, skills, and future exogenous uniforms, so paired world-level contrasts are appropriate. Reusing the original seeds and already inspected state distribution makes this a planned follow-up to a known result, not an independent replication. New predictions must be labeled prospective for this follow-up; their selection was informed by the original run.

Finally, this finite synthetic experiment continues to assume myopic logit choice, a guaranteed allocation floor, exact external evidence, and externally enforced appointment constitutions. It cannot establish endogenous protection of the auditor, long-horizon strategic capture, human behavior, permanent lock-in, or an attractor. Those limitations are unchanged by an exact branch.
