# Paid bound-fuel access and full succession

The [protocol](PROTOCOL.md) was declared before calculation. It fixes one common N=4 generator, the three proposed CF-access families, all positive constants at one, a type-neutral full formation-and-turnover event and deadline 10. Optional bound copying and CF-catalyzed free-F recycling are absent. No rate search was performed.

The [research note](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/PAID-ACCESS-SUCCESSION.md) gives the proof and its limits.

- [compute.py](compute.py) enumerates 1,393 transient states per branch and the complete success-compatible generator, while charging all other exits to failure. It computes exact shortest-path coefficients and exploratory floating probabilities saved in [results.json](results.json).
- [certify.py](certify.py) bounds the declared deadline probability through directed integer uniformization and rational exponential tails. [certificate.json](certificate.json) contains the rigorous probability intervals and positive difference bound. It reuses the first file's generator; it is not an independent reconstruction of the chemistry.
- [path_check.py](path_check.py) checks the displayed 21-event turnover path, identities, exit rates and exact ledger. [path-check.json](path-check.json) preserves its trace.

From the repository root, the two pure-Python exact checks are:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/paid-access/certify.py
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/paid-access/path_check.py
```

The exploratory generator calculation additionally requires NumPy and SciPy. Each script writes only its named JSON output in this directory. No bytecode cache is needed.

The whole event requires seven fresh captures: one during paid formation, six during full turnover. Formation starts at assigned work W6 and enters W5; turnover returns W5. The success probabilities by time10 are only about 2.7×10⁻¹³. Blocking wins at that deadline, while the exact leading short-time term favors nonblocking for the same event. This is a scoped model comparison, not likely operation, physical calibration, a universal ordering of possibilities or a prevalence theorem.

The separate [finite-source thermodynamic certificate](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/PAID-ACCESS-THERMODYNAMIC-CERTIFICATE.md) preserves only the time10 sign under its explicit source-depletion and reverse-channel bounds. It does not transfer the negative short-time asymptotic or identify a feasible chemistry.
