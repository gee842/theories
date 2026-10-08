# Executable comparison of inherited reconstruction and a conventional network

The actual Lean network implementation and a separately written finite-array Python simulator agree in **34,768 synthetic cases**: 18,768 bounded primitive cases, 8,000 successful history prefixes and 8,000 prefixes with a final disabled action. The deterministic seed is 20261008 and histories reach 80 events. There are 11,680 successful outcomes, 23,088 disabled outcomes and zero mismatches. [Receipt](verification.json).

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/integrated-correction/general-framework/generative-basis/ecological-selection/network-comparison/check.py
```

[Driver.lean](Driver.lean) parses generated records and executes the network transition implementation. [check.py](check.py) independently calculates results using finite cell arrays, preserves ordered bonds, and compares all operative cell states, genealogy and seven stock/account fields. Missing or disabled operations return failure in both accounts. The temporary input/output files are reproducible from the fixed generator; their hashes and source hashes are retained instead of redundant generated archives.

The bounded set contains every specified combination of 0–2 cells, binary retention, valid directed ordered edges without repeats or self-loops, and binary precursor, available support and two reserves. Founder labels equal initial cell positions; used and removed accounts start at zero. The 51 primitive choices include all index-0–2 operations and binary transfer allocations. Longer histories exercise changing accounts, inherited states, repeated transfers and mixing; prefixes are related observations, not independent replications.

The [general Lean correspondence](../../lean/universal-ethics/EvolutionNetworkComparison.lean) additionally quantifies over arbitrary finite histories and shared state-dependent selectors. Its [proof receipt](../../lean/universal-ethics/evolution-network-comparison-verification/verification.json) is separate from this numerical check. Neither run uses new biological measurements or fits parameters. The network comparator is authored here and is not a reproduction of Watson's neural or regulatory learning simulations.

The [protocol](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EVOLUTION-COMPARISON-PROTOCOL.md) and [full assessment](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EVOLUTION-NETWORK-COMPARISON.md) state the assumptions, literature comparison, counterreview and unresolved empirical join.
