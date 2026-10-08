# Recurrent assembly verification

[RecurrentAssembly.lean](../RecurrentAssembly.lean) connects the previous routing output to actual end attachment, retained fragments and repeated rebuilding. [check.py](check.py) compiles the eight actual modules in a fresh temporary directory using Lean 4.29.1, rejects placeholders, added axioms, unsafe/native shortcuts and warnings, and checks source stability during compilation.

[verification.json](verification.json) records **31 new theorems / 47 new declaration audits / 373 closure audits**. Eleven new declaration reports are empty; all other dependencies are among standard `propext`, `Classical.choice` and `Quot.sound`. The 326 inherited declarations are rebuilt and counted separately. Sources, toolchain, checker and logs are bound by hashes.

General results establish material/support conservation, token-multiplicity preservation during attachment, structural-path preservation, the actual preparation interface and arbitrarily many finitely supported rounds. Finite kernel checks retain partial failure, missing component types and an ineligible structure. Native operations never assign the `mature` target graph to an output; it is a theorem's comparison state.

Run `python3 check.py` from this directory. The [existing study continuation](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GROWN-FRAGMENTATION-INTEGRATION.md#recurrent-assembly-from-prepared-material) specifies the structural input correspondence, supplied local attachment and cleavage laws, operation order and finite materials. It does not prove a force law, autonomous feed generation, variable inherited organizing laws, calendar-time growth or empirical superiority.
