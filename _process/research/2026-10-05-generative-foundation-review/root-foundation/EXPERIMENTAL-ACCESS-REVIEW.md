# Experimental access after acquired abstraction: interface review

6 October 2026. AI-authored independent review of **retained abstraction → unexpected response → revised apparatus hypotheses → warranted action or unresolved ambiguity**. This continues the [acquisition result](ABSTRACTION-ACQUISITION-REVIEW.md) and its [canonical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ABSTRACTION-ACQUISITION.md). The governing question is how an already acquired model can test the conditions of its own experimental access without receiving a correct diagnosis from the analyst.

**Status:** the predecessor's actual retained state and resources have been replayed independently. The following fixture and acceptance conditions are design recommendations; the extension's implementation and final numerical results have not yet been reviewed. No affordable new run or completed diagnosis is asserted here in advance.

## 1. What actually survives the preceding run

The unchanged acquisition [implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/model.py) was executed directly through its `Meter`, `TargetPort`, `Learner.run`, `plan_novel_use` and `TargetPort.use` interfaces. The resulting states are:

| Quantity | Successful primary acquisition/use | Inverted-sensor acquisition/use |
|---|---|---|
| Retained output table | `(0, 0, 1)` | `(1, 1, 0)` |
| Retained action table | `0→1→2→0` | `0→1→2→0` |
| Model initial label | 0 | 0 |
| Retained model cells | 7 | 7 |
| Model plus controller cells | 15 | 15 |
| Acquired access/suffix/cache sets | All discarded by paid compaction | All discarded by paid compaction |
| Retained maximum queried length | 4 | 4 |
| Executed later word | `aaaaa` | `aaaaaa` |
| Actual physical phase, auditor only | 2 | 0 |
| Fuel after the actual return | `1030367/65536` | `337615/65536` |
| Remaining original source | 10 | 10 |
| Previous extraction | Transferred 10 | Wasted 10 |

The second column is a genuine acquired model with the wrong productive interpretation, rather than a model that failed to fit its readings. Replacing it with the first column's correct output table would supply the repair being investigated.

The predecessor retains neither a current learned-state cursor nor its executed plan as explicit learner memory. Those values occur in the evaluator's audit records. A continuation may preserve the physical environment's actual phase while initializing the learner's possible phases to all retained model states. If an operation history or resource-outcome receipt is to become accessible memory, its acquisition and write must be explicit. A hidden physical-state identifier or retrospective import of the audit transcript is not an inherited observation.

`TargetPort.use` returns the updated fuel and source functionally; it does not add the returned packet to the preceding `Meter` object. A continuation must carry `fuel_after_return` exactly once. It must neither omit the real successful return nor add it a second time. Likewise, it must inherit 15 live storage cells rather than restart storage accounting at zero.

## 2. The adopted fixture uses the retained model

Use the successful primary handoff. Preserve its learned cycle and original source packet. At a declared boundary the evaluator chooses apparatus laws without revealing that choice to the learner. The learner receives a supplied hypothesis-generating recipe. An initial review sketch allowed one fault at a time; the adopted design removes that exclusion by using the complete cross of three binary parameters:

| Parameter | Two possible laws |
|---|---|
| Contact reversal \(\tau\) | Productive contact is \(o(q)\oplus\tau\) |
| Sensor reversal \(\sigma\) | Reading is \(o(q)\oplus\tau\oplus\sigma\) |
| Reset behavior | Return to model initial state, or leave current phase unchanged |

All eight templates share the retained action transition. Their phase coordinates begin as all three possible model states, producing 24 possible apparatus-state pairs. In particular, simultaneous reversals are allowed. This is a constrained diagnosis problem under a known candidate family; it does not derive that family or establish that every real fault lies inside it.

The environment must retain the actual phase from the predecessor even when it changes these laws. The learner propagates its possible states through each actual command and filters them using the resulting observations. Starting every candidate from its preferred reset state would assume precisely the reset validity being tested.

The native sequence read, action, read, action, read yields one cyclic rotation of `001` or its complement. Those six possible triples are distinct. Thus acquired readings identify the combined reversal bit \(\tau\oplus\sigma\) and the current model phase, without separately identifying contact and sensor reversals. Move to the model's phase 1 using the retained transition table, so every remaining candidate agrees on a noninitial state. A paid reset followed by the same read/action triple can then distinguish return-to-initial from ineffective reset. A reset attempted at initial phase 0 could not provide that separation.

After this experiment the state and reset law can be determined within the family, while two explanations with the same reversal parity remain. The experiment avoids a hidden known-state input and a single-fault assumption. It still supplies fixed action dynamics, the three-state structure and the above fault family. Its planned separation is a mathematical statement; its affordability requires the subsequent implementation review.

## 3. An exact ambiguity, not merely insufficient testing

For any common phase and reset law, the two templates related by \((\tau,\sigma)\mapsto(1-\tau,1-\sigma)\) have identical read laws, state transitions and reset laws. The familiar sensor-only and contact-only reversal pair is one example; unchanged sensing/contact and simultaneous reversal form another. They therefore produce the same complete observation trace under every sequence of reset, action and read commands, including adaptively chosen commands. Induction on the command history establishes this: equal observations lead the same deterministic policy to choose the same next command, and the candidates continue to return equal readings.

Their productive consequences disagree at every phase. If the final packet is offered at phase 2, sensor reversal transfers its ten units while contact reversal wastes them. At phases 0 and 1 the outcomes are reversed. More sensing cannot resolve this difference, and choosing the most likely diagnosis requires a supplied prior or other evidence.

This is a useful positive result about the learner's limits: it can acquire a warranted equivalence class of apparatus explanations and identify a separating kind of intervention. A singleton diagnosis is not the only successful epistemic outcome. The implementation should report the surviving set instead of resolving the tie by evaluator order and then calling that resolution evidence.

A productive operation can break the symmetry only if its consequence is accessible to the learner. A receipt reporting actual resource arrival is a legitimate new observation channel, not a correct fault label. Its availability, reliability, update law, acquisition cost and stored representation still require disclosure. Using the evaluator's hidden `success` Boolean without an implemented consequence channel would evade the experimental-access problem.

Even a trustworthy receipt does not ground all measurement from nothing. The diagnosis is conditional on that channel and the candidate laws connecting it to hypotheses. If both the contact sensor and resource receipt may be arbitrarily corrupted, this particular separation need not survive.

## 4. One packet changes the meaning of success

The actual primary continuation has one remaining packet. Under the preceding phase-port law, an extraction attempt consumes the entire packet whether it transfers productively or becomes waste. A useful distinguishing operation can therefore produce knowledge while eliminating the material possibility of another extraction.

The experiment must distinguish:

- A revised hypothesis set after affordable sensing.
- A safe productive action on which every surviving hypothesis agrees.
- A paid operation that distinguishes hypotheses through an actual consequence.
- A retained diagnosis that can govern a further affordable use with remaining material.

For the two reversal hypotheses, no phase guarantees successful capture in both. A conservative no-loss policy may preserve the last packet and report ambiguity. A diagnostic-use policy may spend it, gaining a distinguishing consequence and sometimes a productive return. Those are different policies with different supplied priorities; neither follows uniquely from the observations.

A fixed tie-breaking rule should be declared before evaluating which hidden case benefits. For example, selecting the old model's productive phase uses an inherited substantive preference; choosing the cheapest currently separating operation uses a cost preference. Neither can be justified by inspecting the actual fault label. Paired sensor/contact cases should expose their opposite outcomes under the same selected intervention.

Do not report a diagnosed-then-second-use success after consuming the final packet. A non-destructive assay, a further packet, replenishment or a new renewable source would be an additional material/interface premise. Such an extension can be studied explicitly, but is unnecessary for the minimal honest result.

## 5. The diagnosis recipe is an additional supplied capacity

The retained observation-table learner did not already implement a version-space apparatus diagnoser. Adding one is a supplied extension of its controller and action interface, even if it reuses the 256-cell cartridge and the acquired model. The adopted design declares a one-unit reprogramming fee, eight additional controller cells and two logical cells per candidate (template identifier and phase). All generated data, updates and filtering still require paid work and storage. The continuation should preserve the model as its actual input rather than retire it and install a new target-specific table.

The extension must identify the following costs and memory:

- Installing or loading its supplied controller recipe, with any material requirement stated.
- The still-live retained model and controller, candidate flags, possible-state sets and newly stored evidence.
- Simulating candidates, comparing predicted outcomes, selecting experiments and filtering surviving explanations.
- Live command buffers and candidate workspace throughout real reset/action/read/receipt operations.
- Retaining the revised result and any subsequent planning or productive operation.

Existing symbolic tariffs can be reused if the operation envelopes and storage encoding are declared. They remain local tariffs, not physical energy measurements. Capacity is already present; unused cells do not grant free computation, rewriting, retention or a previously absent diagnosis program.

For either inherited branch, the continuation's resource identity is

\[
F_0+10=C_{\mathrm{new}}+F_{\mathrm{final}}+S_{\mathrm{final}}+W_{\mathrm{new}},
\]

where \(F_0\) is that branch's actual post-use fuel, the ten is its remaining source, and all new costs are prepaid from accessible fuel. A prospective productive return cannot finance diagnosis required before that return. Every unsuccessful prefix preserves prior expenditure. Neither a physical reset nor resetting the learner's beliefs restores fuel, source, stored evidence or already spent packets.

The lower-fuel inverted-sensor continuation deserves separate treatment. Its learned table is `110`, its physical phase is 0, and its failed productive prediction is historical evidence only if an actual consequence receipt was made accessible and retained. Its roughly 5.15 fuel may or may not fund the newly supplied diagnostic recipe. Failure to afford it is a substantive result, not a reason to replace its reserve with the successful primary branch's larger stock.

## 6. Possibility, exclusion and out-of-family faults

An eliminated hypothesis is refuted relative to its explicit deterministic prediction and the trusted observation semantics. A surviving hypothesis is compatible with the paid evidence; it is not a posterior probability unless a probability model and prior are provided. Hypothesis names are analyst descriptions of structural alternatives, not native correctness signals.

The adopted family includes simultaneous reversals but excludes arbitrary action changes, new hidden phases, time-varying faults, faulty resource receipts and unmodeled source loss. These exclusions matter. Simultaneous sensor/contact reversal preserves the old read law while changing productive consequences, so an anomaly-triggered sensing procedure alone need not detect that permitted change. A delayed change outside the finite state bound can also preserve every experiment performed so far.

A proposed 48-world extension adds a binary availability/admission condition. It must distinguish the actual known remaining physical packet from its present accessibility through the port. A blocked route can leave source physically present, while a failed admitted extraction can waste it. If the intended observation is only arrival/nonarrival, internal source and waste audit fields must remain unavailable to the learner; otherwise those extra observations may resolve the claimed ambiguity. Nonarrival can then fit either unproductive contact or unavailable admission, whereas an arrival is stronger evidence. If this larger representation cannot be maintained with the actual stock, report the funding failure separately from any explicitly ample mathematical assay.

At least one deliberate out-of-family case should produce an empty version space or an explicit model-family limitation rather than an invented repair. Empty space signals that the combination of candidate family and trusted observations is inconsistent; it does not uniquely diagnose which premise failed. Some excluded cases will remain observationally compatible with an included one, so empty-space detection cannot establish completeness either.

## 7. Independent-check contract and stopping rule

An independent checker should reconstruct the actual predecessor handoff; verify the retained model, discarded archive, physical phase, live storage and fuel/source carry; and then replay every successor resource prefix. It should implement a small independent set-valued hypothesis update over explicit candidate states, comparing each learner elimination with the paid observation that supports it.

The finite experiment should include the paired reversal cases, ineffective reset, unchanged access, an out-of-family case, insufficient funds/capacity, and an unavailable or untrusted consequence channel. Two runs that differ only in the hidden sensor/contact explanation should generate identical reset/action/read evidence and policy choices until the first productive consequence. A checker may know the hidden label for assessment, but the learner and its experiment scheduler must not receive it.

Verify both directions of the central boundary: ordinary sensing cannot separate the reversal pair; a declared accessible productive receipt can separate them when that paid operation is feasible. Then verify what remains afterward—retained evidence, fuel and source—rather than inferring further operational capacity from a diagnosis flag.

**Accept the minimal bridge** if an actual retained model produces a paid mismatch, the system revises its apparatus possibilities from accessible consequences, its reported distinctions and ambiguities agree with the independent updater, and every completed step has an honest inherited resource account. At least one case may end in a warranted non-singleton set or an unaffordable intervention. The fixture does not need to manufacture a favorable diagnosis-and-reuse sequence to count as informative.

**Stop after these tests and integrate the exact result.** This closes a conditional access-revision interface if successful. It does not derive the candidate family, its completeness, all calibration or the origin of the diagnosis architecture. Final implementation acceptance remains pending.
