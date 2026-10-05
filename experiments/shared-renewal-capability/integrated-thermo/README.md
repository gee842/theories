# Exact thermodynamic certificate for formation plus full turnover

The [proof](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/INTEGRATED-THERMODYNAMICS.md) applies to the N=4 common A0/A1 generator and its entire eight-capture formation-and-turnover assay. It combines the integrated comparison's certified margin with finite-source depletion and new reverse-reaction error bounds.

The [protocol](PROTOCOL.md) precedes execution of [exact_check.py](exact_check.py). The [saved certificate](exact-check.json) records checks of 31 reversible reaction pairs, 38,133 original pre-stop count states, and 232,507 enabled detailed-balance edges. It preserves protocol/checker hashes and the integrated source artifacts' hashes before and after the run. Copying and template-free formation share their required equilibrium constant.

Run from the repository with Python 3 and its standard library:

```sh
python3 experiments/shared-renewal-capability/integrated-thermo/exact_check.py
```

The script writes only its adjacent JSON. It checks exact rational and monomial identities; it does not simulate, fit, or optimize outcomes. It reads the integrated formation result and verifies the inherited constants and source checker hash.

The certificate is deliberately extreme: source stock B=9783293481266747904000000 and potential scale M=299 preserve a gap greater than 1/3235216098302496000000 by model time 27. The inherited rate scale is about 2.43×10²¹, with some forward constants proportional to its cube. These establish a finite consistent parameter construction, not attainable molecular kinetics or reliable laboratory operation.

The finite source is part of both branches' common preparation. The bound covers the same capped eight-capture event and its wear-history marks; it cannot be reused for unlimited turnover. Reverse reactions remove old exact absorption and no-template boundaries. Observation marks do not constitute a free physical measurement implementation, and the assigned work ledger is not chemical free energy.
