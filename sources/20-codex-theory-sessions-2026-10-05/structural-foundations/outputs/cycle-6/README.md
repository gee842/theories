# Paid revision and the recovery window

The [synthesis](synthesis.md) extends the research to an evaluator that revises its own forecast after conditions change. Revision can consume the resources needed to put its corrected rule into operation before the unrevised population would disappear. Noisy belief accuracy and usable execution can diverge, while a funded mixed population can sometimes avoid diagnosis altogether.

## Read the results

- [Synthesis](synthesis.md): integrated findings, scale implications, and remaining assumptions.
- [Evaluator revision](evaluator-revision.md): changed settlement contract, physical report and archive, exact recovery deadlines, unknown-onset periodic monitoring, and robust quota control.
- [Paid noisy revision](paid-revision.md): finite retained evidence, paid implementation, optimal reserve/deadline frontier, and expected versus sure success.
- [Revision and scale](revision-and-scale.md): actual revision certificate, information/response criterion, funding window, stale evidence, and complete-path correspondence.
- [Revision audit](revision-audit.md): inspected primary sources, independent accounting, controls, and scope review.
- [Claim register](CLAIMS.md): proofs, supplied examples, assumptions, and open hypotheses.

The population inspector is perfect within a known two-contract family. The separate noisy model is a finite handoff with its own prices and deadline. Their conceptual integration does not claim an implemented noisy population monitor.

## Reproduce the checks

From this directory:

```text
python3 -B verification/check_evaluator_revision.py
python3 -B verification/check_paid_revision.py
python3 -B verification/check_revision_scale.py
```

All use only the Python standard library and passed the coordinator's final runs. Keep the cycle directories together: the population checker reads the preserved cycle-five population implementation, which imports the cycle-four plant. Neither dependency is modified.

The [verification receipt](verification/verification-receipt.json) records hashes, counts, dependencies, and limits. Detailed artifacts are the [population results](verification/evaluator-revision-results.json), [population recovery frontier](verification/revision-window.csv), [noisy revision results](verification/paid-revision-results.json), [noisy financing frontier](verification/paid-revision-frontier.csv), and [formal countermodel results](verification/revision-scale-results.json).

Infinite and all-onset conclusions use invariants, decreasing potentials, or finite phase reductions. Exact synthetic checks and independent review do not establish empirical universality. The [previous cycle](../cycle-5/README.md) preserves funded population selection and succession.
