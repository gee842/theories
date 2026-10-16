# Checked formation of updaters and paid historical composition

6 October 2026. [UpdaterFormation.lean](UpdaterFormation.lean) has **25 new checked declarations** under Lean 4.29.1. It imports the existing causal root, formed-variant process and selector-revision process from their actual repository files. Their audits are recorded as dependencies, not new theorems. The [verification record](verification.json) and [logs](verification/) identify the exact source and compiler bytes.

The governing mathematical argument is [UPDATER-FORMATION-MATH.md](../../../../../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/UPDATER-FORMATION-MATH.md). The [experiment protocol](../PROTOCOL.md) additionally supplies rates, probabilities, clocks and comparisons.

## New event law

The state extends the previous selector state with updater type, updater lifetime, whether a selector has ever existed, an unusable source remainder and the total inherited material inventory. The random updater permits either selector orientation. A directed updater with a prior orientation permits only its opposite. Module formation costs energy and is enabled only after updater expiry. Both active modules are required for a trial. Actual capture pays both renewal prices and maintains the current types; failure wears both structures. A paid module replacement changes the available selector-assembly rule.

The elementary energy ledger includes the full source stock, assembly, work, maintenance and packet waste. The source remainder and total material inventory are preserved in the new phase. The inventory is a supplied coarse two-slot representation, not a molecular stoichiometric derivation.

## Exact historical interfaces

The phase-tagged combined relation preserves every original `FormedSelection.Step` between old states exactly. A paid connection requires actual A and H, an intact site, captured local fuel and enough common fuel for the adapter. Its new reserve is old common fuel minus adapter cost plus the old local unit. Source energy becomes full packets plus an explicitly retained remainder. At least two material units must actually exist before they can be reassigned to the backing slots.

The package proves:

- The paid bridge conserves energy after its declared adapter expenditure; material can fund the two backing slots. The previously exhausted copied witness cannot fund it.
- An actual predecessor trace, that paid bridge and a new updater trace compose into one `Generative.Trace`, passing every resource-bearing boundary state.
- Whole-history expenditure and source waste balance against the original pre-formation energy, including the predecessor costs.
- Every new non-module-formation event projects to an old selector event with its renewal price changed to the **combined selector-plus-updater renewal bill**. A segment containing no module formation projects to a corresponding old trace.
- Module formation is an additional paid event and is not erased from a whole-process projection. The projection does not establish kinetic equivalence, equal stochastic kernels for all updater states, or a Python refinement.

A concrete witness starts in the old process with no A/H, common fuel 18 and source energy 97. Paid formation, association, repair and capture reach an actual interface state. The adapter supplies reserve 14 and sixteen six-unit packets, with both new structures absent. An R updater is formed, governs a selector, survives four captured opportunities and a condition reversal, then governs an unsuccessful reassembly. After further failures it expires; a newly paid D updater governs the opposite selector, whose productive trial renews both. Final reserve is 9 with seven packets remaining. The checked whole ledger is **115 = 4 + 1 + 59 + 51**, representing old costs, adapter cost, new costs/waste and remaining energy.

## Deterministic bounds and unformalized claims

The synchronized-expiry diagnostic reuses the previous sequential-payment theorem. If both structures have residual lifetime k, then j unsuccessful newly formed bundles before first recovery require exactly `k*d+g+c+d+j*(g+c+L*d)` pre-return fuel. Adjacent g and c charges are grouped; the mathematical note justifies this because no return intervenes. The theorem checks the payment-prefix equivalence, not an automated decomposition of every full event history.

The same law cannot pay its first trial from an absent-updater/absent-selector entrance with less than `g+c+d` reserve. An anticipated return cannot fund startup. The stochastic recovery formula `1-4^(-N)`, the conditional first-success D share `2/3`, first-passage preparation probability and executable comparisons are analytical/computational claims, not Lean probability theorems.

The formal trial relation uses deterministic capture when the response matches the plant. Noisy-capture comparisons add failed-return outcomes even after a matching response; those extra outcome channels are not included in this Lean relation. Their accounting and comparisons require the separate executable and independent checks.

The adapter's functionality, recycled backing slots, two updater algorithms, meta-proposal rule, inherited residue, physical maintenance and retooled scaffold remain supplied premises. Actual composition under those premises is checked. Their natural emergence or empirical realization, richer representations, concern and wisdom are not proved by these declarations.

## Reproduce

Run `python3 check.py` here. It freezes and compiles this module and all three source dependencies in a fresh temporary directory using `lean +leanprover/lean4:v4.29.1`. Every new theorem is required to have a dependency audit. The checker rejects unproved declarations, proof placeholders, native proof shortcuts, unsafe declarations, warnings and unexpected proof dependencies. It records source, checker, compiler, toolchain and log hashes.

The accepted standard proof foundations appearing in the new audits are `propext`, `Quot.sound` and `Classical.choice`. Several declarations, including the local updater-revision witness, have empty axiom lists. We do not describe this package as having uniformly empty axiom dependencies. Its results are checked conditional theorems with explicit local laws and disclosed proof foundations.
