# Funded selection and population renewal

Continuation: the [sixth cycle](../cycle-6/README.md) now implements paid evaluator revision after a changed contract, alongside noisy finite-memory revision and a robust mixed-population control. The record below preserves the fifth cycle's findings and scope.

The [synthesis](synthesis.md) extends the cross-scale account to actual populations of decision rules. A rule can reach 100% of a population while no successor remains affordable. Better interpretation of evidence, inherited apparatus, and copying dependence change that outcome under explicit financing and timing assumptions.

## Read the findings

- [Synthesis](synthesis.md): the connected account and next discriminating test.
- [Funded selection](funded-selection.md): actual early/late/forecast copying, common physical calendar, paid births, exact renewal potential, stochastic survival bounds, and finite versus infinite horizons.
- [Paid evaluation](paid-evaluation.md): affordable observation, retained source address, donor asset transfer, and exact successor-reserve frontiers.
- [Population and scale](population-and-scale.md): funded succession, depletion, joint offspring dependence, and population-kernel correspondence.
- [Population audit](population-audit.md): independent accounting and transition review, primary-source connections, controls, and evidence limits.
- [Claim register](CLAIMS.md): what is proved, constructed, assumed, and still open.

The population experiment and one-successor evaluation experiment use the same repair plant but different declared funding boundaries. Their prices and endowed assets are kept separate. Continuing grants and production inputs are explicit; persistence is not independence from outside support.

## Verification

From this directory, run the standard-library checkers:

```text
python3 -B verification/check_funded_selection.py
python3 -B verification/check_paid_evaluation.py
python3 -B verification/check_population_scale.py
```

The funded-selection checker reads the preserved [cycle-four plant implementation](../cycle-4/verification/check_adoption_dynamics.py). Keep the relative cycle directories together. It does not modify that dependency.

All three passed in the coordinator's final runs. The [verification receipt](verification/verification-receipt.json) records hashes, counts, dependencies, and limits. Detailed evidence includes:

- [Funded-selection results](verification/funded-selection-results.json) and [population trajectories](verification/population-trajectories.csv).
- [Paid-evaluation results](verification/paid-evaluation-results.json), [reserve frontiers](verification/paid-evaluation-frontier.csv), and [closed invariants/failure ranks](verification/paid-evaluation-controller-certificates.json).
- [Population and scale results](verification/population-scale-results.json).

Proofs justify infinite conclusions; finite traces alone do not. Independent review and exact computations remain synthetic validation, not empirical evidence. All deliverables are local. The [previous cycle](../cycle-4/README.md) preserves infrastructure adoption, paid learning, and rule transmission.
