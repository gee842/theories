# Checked correspondence with a conventional network implementation

[EvolutionNetworkComparison.lean](../EvolutionNetworkComparison.lean) supplies **11 new theorems and 24 new top-level declaration audits**, with 137 audits including the inherited 113 declarations. Nine new declarations have no axiom dependencies; the remaining new declarations use only `propext` and `Quot.sound`. No new axioms or unchecked proof shortcuts are admitted. [Verification receipt](verification.json).

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-network-comparison-verification/check.py
```

[check.py](check.py) compiles the frozen dependency closure in a fresh temporary directory under `leanprover/lean4:v4.29.1`, audits every recorded top-level declaration, rejects placeholders and compiler warnings, and verifies unchanged sources before saving hashes, snapshots and logs. The original developmental sources are unchanged.

The theorem relates this particular authored dynamic-network implementation to the current reconstruction mechanism, including disabled actions, arbitrary finite histories, all state readouts and a shared adaptive selector. It does not establish equivalence to all connectionist models or reproduce Watson's learning equations. Local event laws and allocations remain supplied. The separate [executed comparison](../../../ecological-selection/network-comparison/README.md) checks the implementation against finite-array code.
