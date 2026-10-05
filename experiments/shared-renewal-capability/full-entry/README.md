# Complete entrance and occupation under the paid-access law

The [declared protocol](PROTOCOL.md) replaces the earlier selected-entry condition with all first arrivals to A_i=CF=YG_j=1 at any free reserve. All42 typed unit-rate channels and all competing formation/loss histories remain. Read the [theory and successor interface](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-ENTRY-SUCCESSOR.md).

- [compute.py](compute.py) builds the complete reachable count-state graph under free-packet cap90 and computes first entrance, actual occupation and occupation integrals. [results.json](results.json) retains all four type pairs and the entry-reserve distribution. Its floating roundoff is not certified.
- [certify.py](certify.py) rigorously bounds the primary H10 first-entry gate totals with outward integer uniformization and relative Poisson weights. [certificate.json](certificate.json) records exact rational endpoints, all hashes and the int64 no-overflow bound. It reuses the producer's generator; this is not an independent chemical reconstruction.

Both calculations ran successfully. The complete graph contains34,196 live states. Packet-overflow probability is bounded by2.474e−18 through time10. The certified blocking-gate entrance probability is approximately0.00122046147713, versus0.00117785304333 for the nonblocking gate. The whole-family event is therefore still uncommon. Entry advantage is not sustained operation; the separate floating occupation calculation is tiny at time10.

Reproduce from the repository root with a Python environment containing NumPy and SciPy:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/full-entry/compute.py
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/full-entry/certify.py
```

Each command replaces its corresponding JSON and records the current producer/protocol hashes. No rate fitting or outcome search occurs. The protocol fixed H10 and diagnostic times1,3 before calculation. The second command supplies a stronger arithmetic certificate for the already declared primary observable, not a new empirical validation.

The machine-checked typed table was independently compared with all42 producer channels and matched. Python-to-Lean semantics, original-carrier successor tagging, physical identification and the full capability order remain distinct obligations.
