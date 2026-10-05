# Machine-checked renewal ledger

5 October 2026. This is the first proof-assistant kernel for the current CF-storage and paid-access branch. It accompanies the [formal specification](../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMAL-SPECIFICATION.md), not the whole proposed theory.

[RenewalLedger.lean](RenewalLedger.lean) compiles with the pinned Lean 4.29.1 toolchain and its standard library. The [execution record](lean-verification.json) and [compiler output](lean-output.txt) preserve the actual successful compilation, source hashes and printed theorem dependencies. No additional package installation was needed.

## What is checked

The file declares 27 aggregate reaction events, including reactants, retained catalysts and products. It represents nonnegative counts, enabled reactions, arbitrary finite event traces, and event tallies. It proves:

- Every enabled reaction preserves nonnegative counts and total material.
- The assigned work ledger changes by fresh captures minus leakage, construction and wear losses; A and G birth/wear balances hold.
- Without the three new paid-access channels, the availability count never increases. From A=CF=YG=1 it therefore remains impossible to enable any free-packet A formation, A copying or G fabrication, even after scaffold wear.
- For any return restoring work, A count and total G count, with at least n wear events in each A/G/C/Y role, at least 6n fresh captures are necessary. The one-turnover lower bound is six.

The last theorem applies to every allowed subset of the declared forward event vocabulary. Its hypotheses are explicit; it does not assume a favorable probability or direction. The ledger is an assigned accounting quantity, not identified chemical free energy.

## What the projection does and does not justify

Corresponding A/G types are summed. Every typed reaction used by the physical model maps to one of these aggregate events; the reaction-table correspondence was inspected by the physical reviewer. The mapping itself is not yet machine-checked. This is an overapproximation for ledger invariants and impossibility/lower-bound arguments, **not a kinetic quotient**. In particular, it can permit aggregate fabricator/gate combinations that the typed network does not. A positive aggregate path would not by itself establish typed reachability.

The compiler checks the declared table and deductions. It does not verify that the table describes a molecule. Original-carrier tagging implies the four role-wear hypotheses by the separately reviewed assay construction; that implication is not encoded here. Neither the typed stochastic generator, probability certificate, finite-source coupling, capability semantics nor ethical/universal claims are machine-checked by this file. Added thermodynamic reverse reactions are outside this vocabulary and can invalidate its forward-only capture and availability conclusions.

There are no `sorry` placeholders or custom axiom declarations. The printed dependencies include Lean's standard `propext`, `Quot.sound`, and, for the obstruction proof, `Classical.choice`. The appropriate claim is a completed proof checked by Lean under those foundations, not “axiom-free.”

## Reproduction and next formal obligations

From this directory, run `lean RenewalLedger.lean`; elan selects the version in [lean-toolchain](lean-toolchain). The saved run completed successfully on 5 October 2026. This README was added after that run without changing the proof source; an organization-only recompilation is not counted as extra scientific evidence.

Next: encode the typed-to-ledger projection and original-carrier semantics; prove the fixed-budget pruning; certify finite-generator probability bounds and event-preserving approximation; then connect these to paid protocols and the common joint-capability definition. A proof of a favorable scalar event must remain distinct from a proof ordering every permitted joint task.
