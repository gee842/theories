# Finite material evidence records in Lean

6 October 2026. [RecordedEvidence.lean](RecordedEvidence.lean) verifies the deterministic recording contract specified by the [experiment](../PROTOCOL.md) and analyzed in [the mathematical note](../../../../../../../../_process/research/2026-10-05-concern-theory/RECORDING-FIDELITY-MATH.md). It constructs a concrete recorder from the prior formation law, then proves general event and trace properties for any state satisfying the recorder's explicit invariants.

The saved fresh-source build passed **33 new theorem dependency audits**, inheriting 18 audits from [GenerativeCore](../../../../../../../integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) and 43 from [FormedSelection](../../../formal/FormedSelection.lean). The new module's only reported foundational dependencies are Lean's `propext`, `Quot.sound` and `Classical.choice`; there are no custom axioms, proof holes or unchecked decision shortcuts. The inherited audits are dependencies, not 61 newly discovered results.

## What is proved

- A slot incorporates one A and one H. Material counts include every assembled slot, the remaining free variants and the resident. Slot phase accounting is preserved: slots = blanks + busy slot + written bits.
- An admitted trial reserves a slot and two common fuel units before its outcome. One unit is burnt for operation and one held as write escrow. Both outcome branches are source-backed; neither removes the write escrow. Busy states cannot admit another trial.
- Event and finite-trace ledgers preserve material and account for all energy, including the local store, finite external source, partial-trial escrow and assembly costs. The ledger composes with the prior formation trace.
- Across every trace, committed records plus any latched pending bit equal the initial observation word plus the actual observed bits in order. At idle endpoints this is exact committed-word preservation.
- The three-event reserve/observe/commit trace exists **if and only if** the initial state is valid, its capacity/source admission guard holds and its complete physical successor is the stated macro update. Fuel/source and decoded count updates match the old teacher on such admitted calls. This does not erase slots, pending phase or physical state from the macro.
- An actual nine-event `FormedSelection` trace starts with absent variants and a damaged site at material 5, fuel 12, source 18, and reaches free A2/H2 with an active resident. Two paid assembly events create two blanks. Two completed observations `[0,1]` leave fuel 3 and source 14 but no blank slot, so the recorder cannot admit a third trial despite sufficient fuel and source. The whole witness has spent 13 of its initial 30 energy units and retains all five material units.

## Boundaries of the result

The bit encoding, assembly and receipt recipes, source access, escrow protection and no-erasure retention law are supplied. Formation is suspended after handoff; recorder traces do not silently include the earlier wear, damage, formation or copying events. A future combined law must account for those additional events.

The formalization proves that commitment is enabled for either admitted outcome and what a completed trace does. It does not guarantee a scheduler eventually performs commitment. Completed-word equality needs idle endpoints; an unfinished observed bit remains explicitly in the latched phase.

No probability theorem, assay calibration, confidence arithmetic, material updater, recorder survival under wear, empirical identification or action coupling is established in Lean. The mathematical note explains how a declared iid source and faithful prefix contract transfer the existing confidence guarantee. The Python experiment supplies a separately checked implementation, not a formally proved refinement of this source.

The source guard is stronger than the old teacher's realized-outcome failure guard. Projection therefore holds on recorder-admitted completed trials; not every old teacher path can be lifted. Finite slots also do not supply the unbounded retained sequence needed for asymptotic learning. Renewal, growing records and their continued support remain open.

## Reproduce and inspect

From the repository root:

```sh
python3 experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/formal/check.py
```

[check.py](check.py) pins [Lean 4.29.1](lean-toolchain), freezes the bytes of all three modules, compiles them in dependency order in a fresh temporary directory, and requires all new theorems to have matching dependency audits. It rejects unapproved imports, proof holes, custom axioms, compiler warnings and source changes during the build. It does not import prebuilt project objects or store dependency installations in the repository.

[verification.json](verification.json) records the source, checker, toolchain, compiler and output hashes; [the new module log](verification/RecordedEvidence.txt) lists all 33 dependency audits. The other two logs preserve the inherited module audits. The source hashes certify exactly the checked files; they do not convert this scoped mechanism into an empirical or universal adequacy proof.
