# Reversible allocation embedding: exact audit

The [proof](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/THERMODYNAMIC-EMBEDDING.md) embeds the paid allocation theorem in a finite reversible mass-action network with explicit charged and spent fuel carriers. It preserves the first-forward-capture reliability comparison through a finite-horizon coupling bound.

The [protocol](PROTOCOL.md) was written before the first execution of [exact_check.py](exact_check.py). The [saved output](exact-check.json) records all assertions passing: two conserved moieties, 16 reaction pairs, 1,915 local detailed-balance edges over 512 states, and reverse-rate bounds over 96 pre-capture states per arm. It records hashes of the protocol and checker.

Run with Python 3 and its standard library:

```sh
python3 experiments/shared-renewal-capability/thermo-embedding/exact_check.py
```

The script overwrites only its adjacent result JSON. It performs exact rational/monomial calculations, with no parameter search, simulation, fit, or external dependency. The protocol is prospective only relative to this algebraic check: the original probability bounds and model were already known.

At the chosen finite potential scale, the new reverse-event error is below 3/400 per arm by time 3. The perturbed reference upper bound is below 0.068707, and the constructed lower bound exceeds 0.112345. Both still straddle reliability 0.1.

These are formal probability bounds, not measured chemical performance. The finite high-potential carrier supply matches only the stopped first-capture assay. Reverse wear allows restart from states that were absorbing in the old model; the old infinite-time absorption theorem does not transfer. The construction-disabled reference can also acquire a gate through rare reverse reactions. Chemical identities, catalytic specificity and achievable rate magnitudes remain unverified.
