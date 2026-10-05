# Material construction of a supplied selector mechanism

[ConstructedSelector.lean](ConstructedSelector.lean) composes actual paid formation with material assembly and the existing consequence-sensitive selector law. The principal result is an exact conditional refinement: an existing `SelectorRevision` history lifts into the material process **if and only if** it is feasible under that existing law and its total demands for each part orientation fit the stocks inherited at handoff. Each assembly consumes two corresponding free parts. Fuel affordability remains in the existing selector law; neither resource substitutes for the other.

The compiled source contains **40 new theorem declarations**. A fresh isolated Lean **4.29.1** build passed, including the unchanged source bytes of `GenerativeCore` (18 audits), `FormedSelection` (43), and `SelectorRevision` (21): **122 dependency audits total**. Two new declarations report empty axiom dependencies; the remaining new proofs use subsets of Lean's standard `propext` and `Quot.sound`. There are no proof holes, custom axioms, native proof shortcuts, or choice dependencies. This is conditional mathematics with explicit model premises, not an axiom-free ontology.

## Construction and resource interfaces

- The formation phase is the existing sixteen-event `FormedSelection` law, lifted without changing its states or transitions. A separate hidden regime field is carried unchanged.
- Handoff is a bookkeeping denomination of actual remaining source units: `source = packets * packet_size + remainder`, with `remainder < packet_size`. It preserves common fuel, local fuel, resident, site condition, free parts, and total source energy. It creates no energy or physical packaging process. The new controller starts with zero lease and no assembled parts.
- `assemble false` consumes two free A parts; `assemble true` consumes two free H parts. Both pay the existing assembly cost. Incorporated and spent parts remain in `boundA`/`boundH`; lease expiry and replacement never erase them, reopen precursor capacity, or make them reusable.
- Operational traces project to the unchanged selector law. `material_trace_lift_iff` supplies the converse under exactly the cumulative part budgets. The same event sequence and actual selector/resource states are retained.
- Formation and operation compose through the actual handoff state. `composed_energy_ledger` includes both stages' expenditures; `composed_material_ledger` includes inherited precursor and all free, resident, incorporated, and spent parts.
- `active_reachable_selector_has_consumed_parts` proves that a positive-lease selector reached from the dormant handoff has at least two retained parts. Initial trial cannot run before assembly.

## Constructive and failed histories

The main witness starts with no A/H/resident particles, a damaged site, five units of precursor capacity, twelve common-fuel units, and eighteen source-energy units. Actual formation, association, repair, capture and local copying yield two free A parts, two free H parts, one active resident, seven common-fuel units and sixteen source units. Handoff yields exactly the previous selector example's initial state: seven fuel units and four packets of four units.

Its subsequent history assembles the first mapping, uses it successfully, reverses the environment, incurs two failed trials, consumes the other part pair to assemble the changed mapping, and succeeds again. Every transition projects to the earlier selector witness. Total initial energy is 30; formation spends 7 and operation spends 20; the final common reserve is 3. All five material units remain accounted for.

Both mapping recipes are available from the same handoff state; neither construction eligibility nor the recipe reads the hidden regime. Favorable choice is not guaranteed. A checked wrong-first construction history consumes both part pairs and finishes with the correct mapping and two remaining source packets, but only one common-fuel unit: the next trial requires two and is blocked. Separate counterexamples establish insufficient parts despite abundant fuel, insufficient fuel despite suitable parts, no reuse of spent parts, and failure of the earlier fully exhausted formation witness to fund assembly.

## Scope

This is a staged, finite material refinement. After handoff the old formation reaction repertoire is suspended; inherited site/resident/local-store fields remain inert. The bookkeeping denomination does not prove physical packetization or recover otherwise stranded source remainders. The two-part assembly recipes, their response wiring, the trial/retention transduction, and the phase boundary are supplied local laws. The construction pays for and restricts instances of a declared mechanism; it does not derive those laws from generic matter, construct an independently changing updater architecture, give stochastic selection probabilities, or establish inevitable adaptation or unlimited renewal. The witnessed event schedule is existential, not a controller policy theorem.

The independent finite enumerations, when present, are bounded model checks rather than additional quantified Lean theorems. In particular, any reported named-word funding threshold grid should not be read as a separately formalized all-natural-number threshold.

## Verification

Run from any working directory:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/check.py
```

The checker pins the toolchain, captures all imported source bytes, scans for forbidden declarations and proof shortcuts, recompiles into a fresh temporary directory, audits every new theorem, records compiler/source/checker/log hashes, and verifies that sources did not change during the build. [verification.json](verification.json) records results; [verification/ConstructedSelector.txt](verification/ConstructedSelector.txt) contains the new declaration audits. Generated compiler objects are not stored in the repository.

Read the [integrated theory](../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATERIAL-SELECTOR-COMPOSITION.md), [mathematical companion](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONSTRUCTED-LEARNING-MATH.md), and [independent internal review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONSTRUCTED-LEARNING-REVIEW.md).
