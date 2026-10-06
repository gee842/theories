# Sensor adequacy and the use relation it does not determine

6 October 2026. AI-authored source reconstruction under the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). Named connection: **consequences for continuing activity → acquired revision of what the undertaking requires**. This note locates that connection in existing histories; it adds no controller, dynamical run or theorem. The original acquisition and access studies already establish the sensor/use distinction. The contribution here is to identify exactly what their successful abstractions preserve, what subsequent use requires, and where the outcome does or does not enter further learning.

## 1. The use relation was specified before the outcome

The original [acquisition protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/PROTOCOL.md) describes a three-phase device, a sensor reading positive at phase two, and later routing of an existing ten-unit packet through that phase's port. Capture consumes the packet; a positive phase reading does not supply an inexhaustible source. The question of productive use therefore precedes the comparison results. It is not an analyst's favorable score invented after observing them.

The [implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/model.py) differentiates two operations within this apparatus. `TargetPort.query` returns the raw phase output, complemented when `invert=True`. `TargetPort.use` tests the raw phase output after the commanded word: success transfers ten units into the reported continuing fuel; failure wastes the ten-unit packet. `Learner.plan_novel_use` chooses the first sufficiently long word its retained model predicts as positive. This last positive-reading-to-capture interpretation is supplied by the local recipe. Its truth is not entailed merely by learning the readings.

Both saved cases inherit the same route-conditioned preparation: fuel 36, source 20, and the declared initially present 256-cell workspace. The prior preparation and ten-exposure path remain those recorded in `inherited`; their total path probability is `1/36`. These are alternative continuations of that boundary, not two uses of one stock. Installation and the selected tariffs remain supplied local mechanisms, not generative primitives.

## 2. Exact sensory prediction can coexist with failed use

The [saved acquisition results](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/results.json), `cases.primary_unary` and `cases.inverted_sensor`, give:

| Coordinate | Ordinary sensor | Inverted sensor |
|---|---|---|
| Learned output table, states 0, 1, 2 | `0,0,1` | `1,1,0` |
| Learned transition | `0→1→2→0` | `0→1→2→0` |
| Acquired endpoint words | empty, `a`, `aa`, `aaa`, `aaaa` | The same words |
| Later selected word | `aaaaa` | `aaaaaa` |
| Model prediction for that word | 1 | 1 |
| Actual phase / raw readiness | 2 / 1 | 0 / 0 |
| Transfer / waste | 10 / 0 | 0 / 10 |
| Acquisition, retention, planning and use expenditure | `1984289/65536` | `2021681/65536` |
| Final reported fuel, including actual return | `1030367/65536` | `337615/65536` |
| Remaining source / peak cells | 10 / 114 | 10 / 114 |

Both results are `complete`, `certified` and `retained`. All-word sensory correspondence can be established directly from the saved tables, without another execution: after any unary word of length `k`, both the apparatus and learned machine are in state `k mod 3`; the inverted machine's output is exactly the complement of the raw target's output at that state. Thus the inverted model predicts every actual endpoint reading under this fixed sensor law, not merely the five acquired readings.

Preserve the original `analyst_model_exact=false` and empty distinguishing word for the inverted case. That audit compares the learned model with the **raw target table**, so its failure is correct. The sensory correspondence just stated uses a different, explicitly identified observation map. A certificate interpreted as raw-readiness correctness lacks its calibration premise here; the certificate flag cannot validate that premise.

The accounts also remain distinct. In the ordinary case, `36 + 20 = spent + final fuel + remaining source`. In the inverted case the equality additionally includes ten wasted units. The recorded `fuel` field before the separately reported successful return is `375007/65536` in the ordinary case. No return is inserted into the earlier sensing history.

This is an existing result, explicitly described in [ABSTRACTION-ACQUISITION](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ABSTRACTION-ACQUISITION.md): systematic sensor error can be learned perfectly while its productive interpretation fails. It does not show that the fixed ordinary target's three learned phase classes merge distinct phases. It shows that exactness for a particular observation map does not validate its interpretation as readiness.

## 3. The existing access twins make the limit exact

The later [access protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/PROTOCOL.md) supplies transformations of the retained ordinary model `h`. At matched current phase `q`, sensor output is `h(q) ⊕ τ ⊕ σ`, while actual readiness is `h(q) ⊕ τ`. Consider its two admitted open-channel configurations:

| Configuration | τ | σ | Sensor at every matched phase | Readiness at learned phase 2 |
|---|---|---|---|---|
| Sensor complemented | 0 | 1 | `1 − h(q)` | 1 |
| Readiness complemented | 1 | 0 | `1 − h(q)` | 0 |

Action and reset propagate matched phases identically, and sensor-only operations have equal charges. Therefore every adaptive sensor-only transcript agrees, although the same available extraction has opposite consequences. This is exactly [EXPERIMENTAL-ACCESS-MATH, D5–D6](EXPERIMENTAL-ACCESS-MATH.md#4-an-exact-limit-indistinguishable-access-channels), not a new impossibility theorem. A complete sensor-behavior description cannot uniformly determine that use outcome over this admitted family: any decoder receives the same sensor description for both rows and would have to return different answers. The missing relation concerns a particular productive continuation, not generic lack of information about every property.

The saved [access fixtures](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/results.json) realize the contrast. `primary_sensor_flip` and `readiness_change` execute the same `read,a,read,a,read,reset,a,read,a,probe` sequence. Their readings agree until the probe receipt, which is respectively 1 and 0. Each expends `934043/65536`; final fuel is respectively `187921/16384` and `24081/16384`, and remaining source is zero. The sensor-only fixture retains the two alternatives, leaves source ten, and ends with fuel `88177/32768` after expenditure `854013/65536`.

These access histories start from the **successful ordinary** acquisition's actual retained model, phase two and fuel `1030367/65536`, with declared transformations at the continuation boundary. They are not continuations of the inverted acquisition endpoint, which has a different model, phase and reserve. Neither their outcome receipt nor their funding can be silently grafted onto that failed-use history.

## 4. What actually becomes available for revision

In original `acquisition`, the sequence is `learner.run`, `plan_novel_use`, then `port.use`. The use-result dictionary is returned to the outer experiment. There is no subsequent learner call consuming success, waste or changed fuel, and audit logs are explicitly excluded from learner decisions. Final compaction has also discarded `S`, `E` and the answer cache. The result establishes a mismatch visible to the audit, not acquired revaluation by this learner.

The access extension supplies a real positive relation: `Port.command('probe')` changes the stock, obtains an arrival receipt through its additional sensing operation, and returns it to `Diagnoser.step`, which updates and retains its current alternatives. Consequence can therefore revise interpretation within ongoing activity. Actual arrival can support later recording; anticipated arrival cannot support the preceding operation. Yet `Diagnoser.run(probe)` receives the probe-versus-sensor-only choice as an argument. The supplied transformation repertoire and diagnostic undertaking are not thereby acquired. Its last packet is consumed, so it establishes no further productive use after diagnosis.

This local omission is not a general absence of criterion revision. [Discriminator acquisition](DISCRIMINATION-REVISION-INTEGRATION.md) already changes the operative comparison and next table experiments; [inquiry revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/INQUIRY-REVISION.md) now has accepted actual and formal histories changing an encounter limit from six to four. Earlier acquired evaluation and updater/generator replacement retain their separate achievements. Fixed encompassing laws do not make their operative organizations fixed.

## 5. The resulting adequacy obligation

An abstraction's adequacy must name the continuation or claim it supports. Sensory all-word correctness remains a real achievement in the inverted case; productive applicability additionally concerns the relation between acquired prediction, enacted operation and actual consequence. Revising the unsupported positive-reading-to-capture inference would preserve the sensory result while qualifying its use. It need not lower the original all-word task or declare arbitrary new success.

This does not require collecting maximum generic information first. The existing [attainable-question result](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ATTAINABLE-MATHEMATICAL-QUESTIONS.md) shows that the one-packet apparatus can separately answer two questions whose joint answer is unattainable. Which distinction matters, when it is needed, and what inquiry changes must remain related to the continuing activity. No universal information-maximization rule follows.

The missing same-history connection here is **acquired evidence of failed applicability → changed operative requirement or question scope → subsequent inquiry and use governed by that change**. It must preserve the original predictive achievement and account for the actual changed conditions. The present sources locate and partially realize that relation; they do not yet supply its whole acquisition in this learner.

A stronger account must survive the already preserved blocked-transfer, inverted-receipt, outside-family, exhausted-source and interrupted-record controls. A failed arrival alone need not identify sensor inversion; a misleading receipt can cause inappropriate revision; a correct diagnosis can arrive after further use is impossible. These are substantive limits of the given channels and histories. Successful capture also supplies no universal ethical warrant, general welfare score or completed foundation.

## Source binding

Read-only reconstruction of the existing files; no model was imported or rerun. The three producer bindings in each saved result file were checked against current source bytes. This does not revalidate all inherited scientific results or their entire ancestry. SHA-256:

| Source, relative to `mathematical-abstraction/acquisition/` | SHA-256 |
|---|---|
| `PROTOCOL.md` | `c1d2e249afde5a1a0d68bba22243e024d22e2d929990d8b173441e1abf79e6b8` |
| `model.py` | `18bff69c94f65a5fa9b91c3369f04ba73b5ee705ed5ad5a97ad514c2bd8db135` |
| `results.json` | `ec5cdff0257d02111c0747cfa00e5a13ffbd280a7424f07a68809e8432d64e4e` |
| `access/PROTOCOL.md` | `20e5a322515ca6434d82301953d2175dd5d511f1be1fd276a812b7659cc154e6` |
| `access/diagnosis.py` | `a45e7cafa2b9f0568fdb2c593a17d56625d8e409dcc4f27c5b4fb755e2eec910` |
| `access/results.json` | `778b575c0f8f489aca6583e29f50a2bd707cddb851a27071831df4bac59e891b` |
