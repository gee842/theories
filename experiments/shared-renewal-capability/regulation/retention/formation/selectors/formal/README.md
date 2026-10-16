# Checked selector revision and recovery costs

6 October 2026. [SelectorRevision.lean](SelectorRevision.lean) supplies **21 checked theorem declarations** for a costed response-routing selector within one continuing compartment. Its proof interface directly uses the repository's existing `Generative.Trace`; the existing root module's 18 audits are recorded separately. The [verification record](verification.json) and [compiler logs](verification/) preserve the exact check.

The mathematical argument and its scope are in [SELECTOR-REVISION-MATH.md](../../../../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/SELECTOR-REVISION-MATH.md). The executable study's [protocol](../PROTOCOL.md) additionally specifies stochastic assembly, exposure scheduling and comparator interventions. The Lean module does not prove that the Python program refines the relation or verify its stochastic calculations.

## Supplied event law

The state is `(fuel, packets, selector, lease, regime)`. A positive lease gives the selector routing power; at zero it must be reconstructed before another trial. A sensory bit is mapped to `signal XOR selector`; the plant permits packet capture when that equals `signal XOR regime`. Assembly, sensing/response work and successful template renewal each have declared positive costs. The packet has enough energy to pay renewal. Assembly may produce either selector; its probability belongs to the separate stochastic law.

The events are assembly with a selected orientation, a trial with a sensory bit, externally supplied condition reversal, and source-packet expiry. The trial outcome follows physical compatibility. A success captures one packet and pays same-type renewal; a failure spends its trial cost, wastes one packet and wears the selector. Expiry represents a source opportunity unused by the compartment. The relation allows arbitrary event sequencing; the executable round scheduler is an additional restriction, not a theorem inferred from this permissive relation.

## What is checked

- The XOR response matches the plant exactly when selector and hidden condition agree. Command eligibility is independent of the hidden condition. This guards eligibility; the separate unbiased stochastic policy establishes which command is selected without a condition oracle.
- Every valid finite trace preserves **remaining internal/source energy + paid expenditure + wasted packets**. External reversal retains fuel, source inventory, selector and lease.
- Every selector-type change requires an enabled, paid assembly at zero lease. Successful renewal inherits the same selector type, whereas unsuccessful trials wear it.
- A complete witness starts without a selector, pays its formation, captures a packet, carries a condition reversal, pays two unsuccessful trials, forms a different selector and captures again. The final response mapping differs. No state or fuel reset occurs.
- Trace concatenation uses the actual intermediate state because this is a `Generative.Trace` directly.
- A separate sequential-payment relation proves that a pre-return prefix is affordable exactly when its total cost does not exceed inherited fuel. For a residual lifetime k and j unsuccessful assembled candidates, the explicit prefix sum is `k*d+c+d+j*(c+L*d)`. Each unsuccessful candidate adds its entire assembly/work block and L exposures. The first-cost and first-opportunity obstructions follow.

The last results check exact payment-prefix arithmetic and sequential solvency. The decomposition of a recovery history into those prefixes is established in the mathematical note; it is not an automated refinement theorem between the full event relation and that prefix representation. The exact probability `1-2^(-N)` is a separate analytical result, checked against finite enumeration by the executable study. It is not Lean-certified here.

The construction makes a routing rule change through its consequences. The two routing rules, cost laws, template inheritance, wear, return access and replacement architecture remain supplied. Its connection to the preceding formed molecular-response study is a shared causal interface, not an exact chemical refinement. The persistent compartment, physical identification, open-ended learning, evaluative representations, concern, wisdom and historical novelty are outside these theorems.

## Reproduce and dependency audit

Run `python3 check.py` in this directory. The checker selects `lean +leanprover/lean4:v4.29.1`, freezes the new module and [existing root source](../../../../../../integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean), and compiles both in a fresh temporary build. It records source, checker, compiler, toolchain and log hashes. No prebuilt project objects are reused.

Every new theorem has an axiom audit. The checker rejects custom axioms, proof placeholders, native proof shortcuts, unsafe declarations, unexpected dependencies and compiler warnings. The new audits use only standard Lean `propext` and `Quot.sound`; several declarations, including the concrete revision witness, have empty axiom lists. Therefore this package is not described as having universally empty axiom dependencies. Its claim is mechanically checked conditional deductions with the listed proof foundations and explicit local laws.
