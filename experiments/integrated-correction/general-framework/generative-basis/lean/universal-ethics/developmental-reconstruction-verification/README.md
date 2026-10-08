# Checked reconstruction through sampled descendants

This package checks [DevelopmentalReconstruction.lean](../DevelopmentalReconstruction.lean), extending the existing developmental association model with actual single-cell transfer, inherited redevelopment and finite provision. The [research assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EVOLUTIONARY-ORGANIZATION-INTEGRATION.md) states biological correspondence and limitations.

Run from any directory:

```sh
python3 /Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/developmental-reconstruction-verification/check.py
```

The checker selects `leanprover/lean4:v4.29.1` explicitly without changing the global toolchain. It compiles the three-module closure in a fresh temporary directory, uses an isolated `LEAN_PATH`, checks every registered declaration's axiom dependencies and binds sources, audit files, compiler logs and the checker by SHA-256. Sources must remain unchanged during checking. The saved [receipt](verification.json) records **20 new theorems, 44 new declaration audits and 113 total closure audits**. Sixteen new declarations have empty axiom dependency lists; the others use only the allowed standard Lean dependencies `propext`, `Classical.choice` and `Quot.sound`. An empty list does not remove substantive assumptions embodied in definitions or theorem hypotheses.

| Results | What is checked |
|---|---|
| `transfer_accounts`, `transfer_carries_development`, `sampled_state_rebuilds_bonds` | An actual selected cell carries its developmental state; later division rebuilds bonds, while stocks are accounted for |
| `development_accounts`, `run_iff_core_trace`, `step_accounts`, `history_accounts`, `step_support_bound`, `history_support_bound` | Exact core correspondence, conservation accounts and a developmental-work bound for arbitrary finite actual histories |
| `local_step_preserves_retention`, `local_history_preserves_retention`, `world_step_preserves_retention`, `inherited_development_over_generations`, `acquired_developmental_state` | Homogeneous retention persists through admitted histories without operative revision; an acquired state supplies a nonempty witness |
| Six final theorems beginning with `formed_inherited_reconstruction_history` | Two reconstructions, changed sampling, relaxed requirement, inherited revision, insufficient provision and the insufficiency of cell count alone |

The work bound counts developmental operations, not all events: transfer and empty development can have zero modeled work cost. The module does not prove invasion stability, natural collective reproduction, indefinite resource renewal, measured kinetic rates or superiority over an equally informed conventional model. The occurrence of mutation, sampling rule, chosen cell, provision and local developmental laws remain declared inputs.
