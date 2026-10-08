# Structural copying verification

[StructuralCopying.lean](../StructuralCopying.lean) connects a retained fragment, an actual support-consuming rearrangement, successive material transfers, release and inherited copying costs. [check.py](check.py) builds the actual nine-module closure in a fresh temporary directory with Lean 4.29.1. It rejects placeholders, added axioms, unsafe/native shortcuts and compiler warnings, then checks all declared dependencies and source stability.

[verification.json](verification.json) records **34 new theorem declarations / 57 new declaration audits / 430 closure audits**. The 373 inherited declarations are counted separately. Seventeen new dependency reports are empty; the others contain only standard `propext`, `Classical.choice` and `Quot.sound`. Counts describe declarations supporting one local composition, not 34 independent discoveries.

General results establish ordered copying, token preservation, formed paths, exact necessary/sufficient release budgets with declared material, and arbitrary finite lineages retaining parents and partial products. Local rearrangement changes inherited organization; two known structural costs constrain a third. Concrete failures preserve incomplete and unreleased products, local-law rank reversal and shared-supply order effects.

The [existing study continuation](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GROWN-FRAGMENTATION-INTEGRATION.md#inherited-arrangement-changes-copying) states the supplied copying/access mechanism, local costs, rearrangement and release rules, schedule and stock. The prior fragment matches the new template input structurally; its previous formation mechanism does not thereby produce a copying apparatus. Neither molecular calibration, autonomous provision, population invasion nor comparative superiority over equally detailed mechanisms is proved.

Run `python3 -B check.py` in this directory. Original sources, toolchain, checker and compiler/audit logs are hash-bound in the receipt.
