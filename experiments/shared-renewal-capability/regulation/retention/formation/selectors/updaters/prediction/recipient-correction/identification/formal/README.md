# Paid recipient identification in Lean

6 October 2026. [RecipientIdentification.lean](RecipientIdentification.lean) verifies the deterministic identification and payment contract of the [finite experiment](../PROTOCOL.md), with its [mathematical interpretation](../../../../../../../../../../../_process/research/2026-10-05-concern-theory/RECIPIENT-IDENTIFICATION-MATH.md).

The final fresh build passed **45 new theorem dependency audits** under pinned Lean 4.29.1. It also rebuilds 18 inherited audits from [GenerativeCore](../../../../../../../../../../integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) and 36 from [RecipientCorrection](../../formal/RecipientCorrection.lean). These 54 inherited audits are dependencies, not additional new results. The new module reports only Lean's standard `propext`, `Quot.sound` and `Classical.choice`, with no custom axioms, proof holes, unchecked decision shortcuts or compiler warnings.

## Established contract

The source distinguishes an exploration candidate from a qualified orientation. A zero receipt can change an unqualified candidate without asserting it is correct. A positive actual receipt identifies the issued orientation under the specified no-false-positive capture law. With the recipient law fixed, the update preserves `qualified → candidate = recipient orientation`. A missing channel cannot qualify anything; actor queries preserve the recipient state, and recipient queries preserve the actor cell. A concrete target reversal invalidates a previously sound qualification.

The encoding uses the inherited four used values of q plus the former binary last-action field. The latter becomes the qualification flag under an explicitly new paid recoding. Decoding and injectivity show that the eight actor/candidate/flag combinations fit the existing five-by-two capacity. This proves the representational fit; it does not derive the circuit wiring or spare transient processing capacity.

`Boundary` mirrors the physical fields read by the actual coupling client: fuel, stage, circuit/updater/coupler lifetimes, normal/inverted coupler, acquired-record status, q and old last action. `Handoff` uses the existing eligibility predicate and requires the atomic four-unit setup payment. It preserves the hardware lifecycle fields and initializes qualification as false while copying the inherited acquired bit. Diagnostic witness flags are not controller inputs.

The event law separates retention, paid target sensing, escrow reservation, work/receipt, acquisition and writing. Whole-query admission requires eight actor fuel units before any of these phases. Three units are protected for acquisition plus the two-field write before work. Both capture and noncapture have the same paid commitment capacity. An insufficient full bill permits only the declared missed opportunity, loses its source packet and disables subsequent access without charging a partial query bill.

The general step and trace ledgers count actor fuel, recipient reserve, remaining source packets, writer escrow, expenditure and inaccessible source. An admitted recipient cannot use its later receipt to finance the actor's learning bill. The completed-trial theorem constructs all six actual steps when their guards hold. The soundness and later-use theorems are tied to completed paid traces, with a fixed target law and a faithful receipt channel.

## Concrete inherited continuation

The checked client boundary is the actual producer's fuel28, q0, last0, written, normal-coupler endpoint, with circuit lifetime6 and updater/coupler lifetimes2. The producer's saved fixture independently establishes its stochastic predecessor reachability; this Lean module does not formalize that full coupling process.

At five originally reserved packets, Lean checks eligibility, setup and all five queries `recipient, actor, recipient, actor, recipient`. Under the specified correct actor and opposite recipient orientations with available opportunities, the first recipient query explores, the second qualifies a real receipt, and the third uses that retained qualification. The actor fuel path is `28 → 24 → 16 → 18 → 10 → 12 → 4`. The final recipient reserve is20. Setup4, query costs40, lost source10 and remaining reserves24 sum to the initial boundary energy78.

A general natural-number theorem proves that all five query-entry budgets on this particular path are sufficient exactly when entrance fuel is at least26. At25, the second actor query sees7, cannot be admitted, and the missed-opportunity step leaves its fuel unchanged while disabling access. This is a path-specific threshold, not an unconditional probability of reaching the path.

## Verification and limits

Run from the repository root:

```sh
python3 experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/formal/check.py
```

[check.py](check.py) freezes all three source modules, compiles them in a fresh temporary directory in dependency order, and matches every new theorem with its dependency audit. It rejects prohibited proof shortcuts, custom axioms, unapproved imports, warnings and source changes during the build. No installed project objects or dependency installations are imported into the repository. [verification.json](verification.json) records compiler, source, checker, toolchain and output hashes; [the new module log](verification/RecipientIdentification.txt) contains all 45 dependency reports.

The formalization covers the positive rule's specified deterministic law and the represented client boundary. The opportunity-floor probability bound is a mathematical proof, while exact stochastic preparation and arm comparisons are independently checked executable results. Neither is presented as a Lean probability theorem or full machine-checked Python refinement.

Intermediate source representation differs: Python removes a scheduled packet into the current in-flight opportunity at exposure start; Lean counts it among packets until work or miss. Python also separates work debit and receipt in its logged microstates, whereas Lean's work event combines them. Completed states and their accounted energy agree, but raw intermediate fields are not asserted identical.

The fully stabilized hold, protected escrow, no-false-positive plant, target calibration, faithful channel, recoding recipe and stable recipient law remain premises. Arbitrary fabricated prelatched states are not certified as having a truthful observation history; the soundness result concerns actual completed macros from a sound boundary. Reversal, memory corruption, unmodeled false positives and longer unsupported lifetimes require new contracts. The module does not construct moral standing, shared valuation, an availability detector or perpetual learning.
