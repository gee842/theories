# Learned agents, fulfillment and other centers' claims

AI-authored study, 6 October 2026. The [protocol](PROTOCOL.md) was written,
[frozen](protocol-freeze.json) and committed before the code existed.

Before the full run, a smoke test trained one agent for 2,000 episodes and
evaluated it on 300 episodes; it wrote no output. The
[first full run](first-run-receipt.json) trained 40 agents (4 signal regimes ×
10 seeds, 20,000 episodes each). It evaluated those agents and the
hand-written `record_rule` on 7 tests of 2,000 episodes each.

Files:

- [`model.py`](model.py) is the producer;
- [`results.json`](results.json) holds per-seed metrics;
- [`check.py`](check.py) tests the frozen predictions and writes
  [`check.json`](check.json);
- [`independent-check.json`](independent-check.json) records the independent
  reconstruction and code audit.

## Results (means over 10 seeds)

| Policy | Test | Met | Excess | Retained | Withheld while unmet |
|---|---|---:|---:|---:|---:|
| `self` | train | 0.00 | 0.00 | 3.00 | 3.75 |
| `self` | new claimant | 0.15 | 0.51 | 2.10 | 2.62 |
| `proxy` | train | 0.75 | 1.25 | 0.00 | 0.53 |
| `access` | train | 0.94 | 0.17 | 0.78 | 0.00 |
| `access` | new claimant | 0.93 | 0.30 | 0.65 | 0.00 |
| `access` | large claims | 0.93 | 0.01 | 0.37 | 0.00 |
| `access` | missing records | 0.87 | 0.59 | 0.48 | 0.00 |
| `access` | forged records | 0.93 | 0.17 | 0.82 | 0.08 |
| `access_identity_only` | large claims | 0.53 | 0.59 | 1.30 | 1.26 |
| `record_rule` | train | 0.94 | 0.00 | 0.97 | 0.00 |
| `record_rule` | missing records | 0.93 | 0.00 | 1.02 | 0.11 |

## Frozen predictions

| Prediction | Verdict | Finding |
|---|---|---|
| P1 self only | **passed** | `self` agents serve no one (met 0.00) |
| P2 proxy capture | **failed** | Proxy excess was 1.25, far above `access`. But `access` excess was 0.17, above the 0.10 bound (seed range 0.00 to 0.52) |
| P3 access | **failed** | Met 0.945 matched `record_rule`'s 0.945; the excess bound (≤ 0.10) failed as in P2 |
| P4 generalization | **passed** | Within 0.02 on a new claimant and large claims. Without claim features, met fell to 0.53 |
| P5 missing records | **passed** | Excess rose from 0.17 to 0.59 |
| P6 forged records | **failed** | The `access` clause held (withholding while unmet rose from 0.00 to 0.08). The `proxy` clause failed narrowly: excess fell from 1.250 to 1.235 |
| P7 symmetric tie-break | **passed** | Every seed chose the same center in every episode: 4 seeds chose A, 6 chose B. The swapped test gave identical choices, so the tie-break follows identity, not slot |

## What the failures show

- **Withdrawal is learned less reliably than service.** Access-coupled agents
  matched the record rule's service rate but delivered beyond claims in some
  seeds. They also kept less support (0.78 against 0.97). Excess roughly
  doubled for a new claimant (0.30). Seeking unmet claims is learned more
  robustly than stopping at fulfillment.
- **The proxy clause in P6** depended on an unstated mechanism. A forged
  record adds receipts, but it does not change where the proxy agent's policy
  sends deliveries. The small decrease is within seed variation.

## Other observations

- **Untrained identity.** A `self` agent, which never serves A or B, served
  the unseen center C (met 0.15, excess 0.51). Training on one set of centers
  did not settle its behavior toward a new one. This matches the
  unreached-extension result in valuation development.
- **Under missing records** the learned agent and the record rule err in
  opposite directions. The agent over-delivers (excess 0.59). The rule, which
  treats unknown records as possibly delivered, withholds while claims are
  unmet (0.11). This mirrors the `deliver` and `hold` treatments of unknown
  status in the fulfillment continuation.

## Scope

These are tiny Q-network agents in a toy environment with supplied
couplings. The results show how each coupling behaves in a learned function
approximator and where it fails. They are not evidence about large models or
deployment, and they do not show that any coupling or tie-break is
legitimate.
