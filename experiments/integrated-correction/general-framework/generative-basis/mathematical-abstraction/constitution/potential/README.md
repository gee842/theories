# Potentialist truth and future coverage

8 October 2026. Two checked `Std`-only Lean modules investigate a future-stage interpretation of relational first-order truth. See the [research integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-POTENTIAL-INTEGRATION.md), [primary-source assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-POTENTIAL-SOURCES.md) and [verification receipt](verification.json).

## Reproduce

From this directory, run `python3 check.py`. It selects `leanprover/lean4:v4.29.1`, copies frozen sources to a fresh temporary directory, compiles both modules in order with an isolated `LEAN_PATH`, and runs `#print axioms` on every named top-level declaration counted by the checker. The package requires the installed toolchain and bundled `Std`; no third-party Lean library is imported. A failed run removes the previous receipt before compilation.

## Checked correspondence

| Source | Principal declarations | Scope |
|---|---|---|
| [PotentialTruth.lean](formal/PotentialTruth.lean) | `potential_iff_global`, `sentence_agreement`, `future_invariance` | Future quantifiers preserve ordinary ambient relational first-order truth under growing domains, stable meanings and coverage from every stage. |
| Same | `prefix_coverage`, `prefix_domain_finite`, `prefix_no_full_world` | Supplied natural-number prefixes satisfy the contract, every stage is finite, no stage is full. |
| Same | `unbounded_potential`, `unbounded_current_false`, `unbounded_current_empty` | The larger-number sentence holds under future quantifiers; current-stage quantifiers fail at positive finite stages and are vacuous at zero. |
| [CoverageBoundary.lean](formal/CoverageBoundary.lean) | `coverage_iff_all_unary_existentials` | Exact converse when testing every ambient unary predicate at every stage; no fixed-signature necessity claim. |
| Same | `coverage_of_joint_extensions` | Global union coverage plus common accessible extensions suffices. |
| Same | `fork_every_value_from_start`, `another_global_true`, `another_potential_false_at_start` | A finite fork covers each Boolean value from its start but already fails a nested universal–existential sentence there. |

The receipt reports **22 theorems / 45 declaration audits**: 12 / 26 in `PotentialTruth`, 10 / 19 in `CoverageBoundary`. Generated recursors and deriving auxiliaries are not separately counted; Lean checks their use and dependency closure. No proof holes or custom axioms occur. Standard printed dependencies across the package are `propext`, `Quot.sound`, `Classical.choice`; the main correspondence uses only `propext`.

## Exact limits

The ambient carrier, stage range, fixed atomic interpretation and continuation hypotheses are supplied. Availability applies to parameters. Syntax includes equality, relation symbols, negation, conjunction and first-order quantifiers, with arbitrary nesting. There is no function-term grammar, separate modal syntax, proof-system completeness result, finite truth algorithm or full higher-order admission theorem here. This conditional representation does not justify its modal commitments or establish universal mathematical coverage or exclusive root grounding. Its metatheory is also not imposed as the ontology of every potentialist foundation.
