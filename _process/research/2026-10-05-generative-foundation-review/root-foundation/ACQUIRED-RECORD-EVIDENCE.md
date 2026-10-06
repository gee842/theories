# Acquired record, continuation profile and enacted consequence

6 October 2026. AI-authored internal identification check for the named connection **acquired experience → retained representation → later action**. The computation analyzes an existing finite predictor; it adds no event law, reward, observation channel, updater, primitive axiom, selfhood claim or ethical ground.

## What was checked

The [new checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_acquired_record_profiles.py) imports the existing [independent finite implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_model.py) of the typed deterministic payable-write predictor. It does not change that implementation or its preserved [verification record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/model-verification.json). The [new output](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/acquired-record-profiles.json) records exact input hashes, the complete graph, profile assignments and replayable counterexamples.

The existing model physically represents a five-state register, the last executed command, an updater, finite component stocks, leases, fuel, source packets, a receipt and the current phase. The supplied plant is noiseless and complementary: the executed command together with receipt/no receipt identifies its current target. A paid write updates the register. A later work event reads the command decoded from that register and its tie-breaking last command. Formation recipes, the register architecture, inference rule and update rule remain supplied. The conceptual record is consequently neither free memory nor a newly derived learning architecture.

Two scopes were retained:

1. The preserved 42-event operating witness has ten actual paid writes. Its full intermediate states were replayed unchanged against the saved artifact. Each write's executed command, actual receipt and updater mode reconstruct the register update; non-write events preserve its value. This is a check of the existing operational history, not an independent empirical observation.
2. The already reported four-packet initial condition closes at **180 states and 222 enabled labelled edges**, including 68 ready states. The new check recovers those exact counts and the saved initial state. It computes the complete finite graph to exhaustion, with no depth cutoff. Infinite repetition of reversible labels does not create further states, but all finite continuations through those cycles remain covered.

## Three questions require different profiles

For each reached state, the checker compares all finite continuations in the same event alphabet. It separates:

- **Feasibility:** whether the continuation can execute.
- **Command-marked continuation:** whether it can execute and which command the existing decoder returns at its endpoint.
- **Receipt-marked continuation:** whether it can execute and its actual post-work receipt; a distinct absent marker is used outside the observed phase.

These are analytical questions. The model receives neither a profile identifier nor an externally assigned success score. In particular, the evaluator's access to the complete graph and hidden regime is not an operational input to the learner.

| Exact question | Classes among all 180 states | Classes among 68 ready states |
| --- | ---: | ---: |
| Feasible continuations | 44 | 16 |
| Continuations with endpoint command | 72 | 26 |
| Continuations with endpoint work receipt | 48 | 18 |

Stable partition refinement was crosschecked by a separate product-graph breadth-first search for **every one of the 16,110 unordered state pairs, for each question**. Every split has a finite distinguishing word; pairs in a common class exhaust the pair graph without a difference. Stored counterexamples use shortest distinguishing words. Refusal is retained as a difference, so a difference in an output-marked profile need not be an output discrepancy on a word executable from both sides.

The new [history-profile account](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean) concerns existential continuation feasibility. In this deterministic finite implementation, the reached state after an admitted history is unique, so the graph's feasibility classes instantiate that analytical question. This comparison does not assert that the register is an exact summary of it. The Python graph is the existing separate finite implementation; this run did not compile Lean or prove a new runtime-refinement theorem.

## A retained predictor is not an exact future model

Among ready states, the following pairs share a proposed record but differ on the specified question. Counts describe this one graph, not error rates or samples from an environment.

| Proposed actual readout | Distinct values | Pairs differing in immediate command | Pairs differing in feasible continuations |
| --- | ---: | ---: | ---: |
| Register score | 5 | 168 | 340 |
| Score and last executed command | 8 | 0 | 200 |
| Current decoded command | 2 | 0 | 828 |

The positive result is narrow and exact: **score plus last command suffices for the next decoded command** in this supplied implementation. Score alone fails at its neutral value because the decoder uses the last command to break the tie. Even score plus last command omits resources, component availability, leases and the plant regime. It therefore does not determine which longer histories remain executable, much less their physical consequences.

This is not a failure of the predictor merely because it lacks a complete world representation. An acquired response selector and an exact all-continuation interpreter answer different questions. Adequacy must be stated relative to the actual task and available inputs.

## The analytical profile is not the acquired predictor either

Among ready-state pairs with the same complete feasibility profile, **316 pairs issue different current commands**. A short example compares two successful cycles from the initial state with reversal followed by two cycles. Both endpoints have two source packets and the same available event language; one retains score 4 and command true, the other score 0 and command false. The analytical possibility class does not identify the installed command.

More strongly, **25 same-profile ready pairs produce different receipts under the identical `rent, work` suffix**. One particularly clear pair is entirely within the preserved law:

- After three completed trials: score 4, command true, fuel 24, one source packet, regime true.
- Execute the existing zero-cost `reverse` event: the score, command, fuel and packet count remain the same, while the regime becomes false.
- Both reached states have the same full feasible continuation language.
- `rent, work` executes from both and uses command true. The first receives the packet and reaches fuel 28; the second does not and reaches fuel 20. The actual receipts differ.

The output contains both complete reached states, their entrance histories, shortest receipt-distinguishing suffix and replay endpoints. Thus a same-action-word comparison alone can miss a consequential difference even after full continuation feasibility has been matched. Endpoint or output-sensitive comparison is required for the stronger question.

## What acquisition actually changes in the preserved witness

The ten-write transcript records the score path

\[
2\to3\to4\to4\to4\to4\to4\to3\to2\to0\to0.
\]

After reversal, two ordinary failed trials lower the score to 2 while retaining command true. Updater replacement preserves that acquired score. The next failed trial's paid fast write changes the score from 2 to 0 and changes the later command to false; it does not rewrite the command already executed in that trial. The subsequent false-command trial receives a packet. This connects actual evidence, retained representation and later action without treating retrospective evaluation as a cause.

The register's update still depends on the supplied complementary plant and decoder. Corrupted sensing, other plant structures, arbitrary unobserved changes, missing write funds and absent machinery require separate analysis. The unchanged older record already includes paid work followed by write insolvency. The transcript is an analytical reconstruction of actual writes, not an additional physically retained log inside the model.

## Connection and remaining work

This advances the comparison promised by [V7.3's integration](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-SELECTION.md): factual acquisition, held evaluation, effective incentives and institutional authority cannot be inferred from the same observed action. Here a smaller causal distinction is directly inspectable: a paid acquired score influences a later decoded command, while a coarse action-language profile can erase that difference or a changed consequence. There is no strategic sender, relative-payoff selection or ethical evaluation in this particular predictor, so this check does not formalize those V7.3 mechanisms.

The companion [Lean bridge](ACQUIRED-RECORD-INTEGRATION.md) now supplies exact transport between the actual write-record fold, operational readout and the parent study's [endpoint-sensitive continuation criterion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/OutcomeContinuation.lean). A generic structural criterion constrains adequate records; an installed learner must separately acquire, retain, afford and use its record. The present finite computation tests those distinctions in the existing local law. The next mechanism connection is formation and warranted revision of the still-supplied sensing, decoding and action-coupling rules. It does not complete an assumption-free foundation, identify selfhood, derive concern or establish superiority over an ordinary controller.

Reproduce from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_acquired_record_profiles.py
```

This writes only the new `acquired-record-profiles.json`. Existing scientific receipts and law files remain unchanged. Source hashes are checked against the preserved operational verification artifact and checked again at the end of the new run.
