# Machine-checked typed renewal and support accounting

5 October 2026. These proof-assistant developments cover the ledger and typed forward reactions of the current CF-storage and paid-access branch. They accompany the [formal specification](../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMAL-SPECIFICATION.md), not the whole proposed theory.

[RenewalLedger.lean](RenewalLedger.lean) compiles with the pinned Lean 4.29.1 toolchain and its standard library. The [execution record](lean-verification.json) and [compiler output](lean-output.txt) preserve the actual successful compilation, source hashes and printed theorem dependencies. No additional package installation was needed.

## What is checked

The file declares 27 aggregate reaction events, including reactants, retained catalysts and products. It represents nonnegative counts, enabled reactions, arbitrary finite event traces, and event tallies. It proves:

- Every enabled reaction preserves nonnegative counts and total material.
- The assigned work ledger changes by fresh captures minus leakage, construction and wear losses; A and G birth/wear balances hold.
- Without the three new paid-access channels, the availability count never increases. From A=CF=YG=1 it therefore remains impossible to enable any free-packet A formation, A copying or G fabrication, even after scaffold wear.
- For any return restoring work, A count and total G count, with at least n wear events in each A/G/C/Y role, at least 6n fresh captures are necessary. The one-turnover lower bound is six.

The last theorem applies to every allowed subset of the declared forward event vocabulary. Its hypotheses are explicit; it does not assume a favorable probability or direction. The ledger is an assigned accounting quantity, not identified chemical free energy.

## What the projection does and does not justify

Corresponding A/G types are summed. [TypedRenewal.lean](TypedRenewal.lean) now declares all 42 concrete event instances over 14 coordinates and machine-checks their input/output projection, enabled steps and arbitrary finite traces. It transfers the bare-storage obstruction and turnover lower bound and proves the exact-six loss-budget consequences. The [typed record](typed-lean-verification.json) and [compiler output](typed-lean-output.txt) preserve the successful compilation and dependency hashes. The table was separately inspected against every channel in the full-entry producer; that comparison is not a proof of Python semantics. This is an overapproximation for ledger invariants and impossibility/lower-bound arguments, **not a kinetic quotient**. In particular, it can permit aggregate fabricator/gate combinations that the typed network does not. A positive aggregate path would not by itself establish typed reachability.

The compiler checks the declared table and deductions. It does not verify that the table describes a molecule. [CarrierTurnover.lean](CarrierTurnover.lean) now encodes the implication from full original-carrier loss to the four role-wear premises in an explicit permissive observer, as detailed below. A proof that the complete material-slot implementation refines that observer remains open. Neither the typed stochastic generator, probability certificate, finite-source coupling, capability semantics nor ethical/universal claims are machine-checked by this file. Added thermodynamic reverse reactions are outside this vocabulary and can invalidate its forward-only capture and availability conclusions.

There are no `sorry` placeholders or custom axiom declarations. The printed dependencies include Lean's standard `propext`, `Quot.sound`, and, for the obstruction and final carrier accounting proofs, `Classical.choice`. The appropriate claim is a completed proof checked by Lean under those foundations, not “axiom-free.”

## Reproduction and next formal obligations

From this directory, run `lean RenewalLedger.lean`; elan selects the version in [lean-toolchain](lean-toolchain). The saved run completed successfully on 5 October 2026. This README was added after that run without changing the proof source; an organization-only recompilation is not counted as extra scientific evidence.

[ReserveTurnover.lean](ReserveTurnover.lean) extends the bound to captures ≥ 6n + final work − initial work. For organizational states with inherited reserve m and successor reserve m′, one turnover therefore needs at least 6+m′−m captures; depletion changes the fresh-support requirement. The [reserve record](reserve-lean-verification.json) and [compiler output](reserve-lean-output.txt) preserve its successful check. Run `python3 typed-check.py` or `python3 reserve-check.py` here to build frozen dependencies in temporary directories and check the extensions with the pinned toolchain; these commands replace the corresponding records. Earlier sources and logs remain unchanged.

[CarrierTurnover.lean](CarrierTurnover.lean) declares permanent original-carrier updates for the typed vocabulary, including separate bound G/Y constituents. It derives all four role-wear premises on arbitrary marked enabled histories in which all four originals are lost and composes them with captures ≥6+m′−m. Later enabled histories remain allowed after all originals are gone. The observer forgets allocation and bond pairing, so it supplies necessary bounds rather than positive physical paths. The [scope note](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/CARRIER-TURNOVER-FORMALIZATION.md), [execution record](carrier-lean-verification.json), and [compiler output](carrier-lean-output.txt) preserve the result. Run `python3 carrier-check.py` to build frozen dependencies and check this extension; it replaces only its dedicated records.

Next: refine actual labelled slot transitions into the observer and formalize stochastic event construction; prove fixed-budget pruning and finite-generator probability/error certificates; then connect these to paid protocols and the common joint-capability definition. A proof of a favorable scalar event must remain distinct from a proof ordering every permitted joint task.
