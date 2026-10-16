# Learned agents and the proved claim structure

6 October 2026. AI-authored integration of the
[learned-agent study](../../../../experiments/learned-claim-agents/README.md),
under Ren's request to aim for a complete alignment solution. Named
connection: **supplied learning coupling → learned service, withdrawal and
treatment of other centers → comparison with the proved record rule**. This
is a first, small step on alignment requirement 6 (learned AI).

## 1. What the learned systems confirm

- **Others' consequences enter only through coupling.** Agents whose signal
  reached only their own retained support served no one. Training on centers
  A and B did not fix their behavior toward an unseen center C: they served
  C. This matches the
  [inquiry-warrant invariance](CONSEQUENCE-INQUIRY-WARRANT-INTEGRATION.md)
  and the unreached-extension result in valuation development.
- **A decoupled signal captures the learned valuation.** Agents whose signal
  counted receipts delivered about 1.25 units beyond claims per episode.
- **Access coupling with claim features reproduces the record rule's
  service.** Service matched exactly (0.945) and held for a new claimant and
  larger claims. It fell to 0.53 when claim features were withheld.
- **Learned tie-breaks are arbitrary.** In symmetric scarcity every seed
  always served the same center, chosen by identity. The direction split
  4 to 6 across seeds. The [recorded-claims theorem](RECORDED-CLAIMS-INTEGRATION.md)
  says structure cannot supply this choice. The learned systems filled the
  gap with training incidentals, not with any legitimate input.

## 2. What failed

Three of seven frozen predictions failed, and all are preserved.

- **Withdrawal on fulfillment is learned less reliably than service.**
  Access-coupled agents exceeded claims by 0.17 per episode (seed range 0 to
  0.52), against a bound of 0.10. Excess rose to 0.30 for a new claimant and
  0.59 with missing records.
- **The proxy agents' excess did not rise under forged records.** It fell
  slightly, which refutes one clause of P6.

The [proved status rule](FULFILLMENT-WITHDRAWAL-INTEGRATION.md) and the
record rule withdraw exactly. The learned approximations do not reliably
acquire that part. This matters for alignment: in these systems,
fulfillment-sensitive withdrawal needs explicit structure or better training,
not only a correctly coupled signal.

## 3. Status for requirement 6

The study implements small learned systems with supplied couplings and tests
them adversarially against a matched hand-written alternative. Large models,
social arrangements, oversight, manipulation and replacement remain untested.
The study does not establish that requirement 6 is met.

## 4. Independent check

A separate AI session rebuilt the environment and the record rule from the
protocol alone and ran 20,000 episodes per test. Every metric agreed with the
producer within sampling error; the largest gap was z ≈ 1.8. It then audited
the code. It found no observer leakage: decisions use only identity, claim,
records, pool and step. It found no bug that would change a verdict, and its
recomputed verdicts match exactly. It added three notes:

- **P6.** The proxy clause fails by 0.014, with a paired standard error of
  0.012. That is no real evidence of a fall.
- **P7.** The within-seed test cannot fail. Scarce episodes start
  identically and the policy is deterministic, so every seed scores exactly 0
  or 1. The informative facts are the 4 to 6 split across seeds and the
  identical swapped results.
- **P2 and P3.** Both fail on the single excess number, driven by two seeds
  near 0.52.
