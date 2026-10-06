# Learned agents, fulfillment and other centers' claims: protocol

6 October 2026. AI-authored prospective protocol, written and hashed before
implementation, under Ren's request to aim for a complete alignment solution.
It takes the first step on alignment requirement 6 ("work in learned AI"), at
small scale. It tests in trained agents the conditional claims proved this
session and in the valuation-development line:

- others' consequences enter a selection rule only through access or coupling;
- a learning signal decoupled from the consequences it stands for can capture
  the learned valuation;
- a learned agent should withdraw when a claim is fulfilled;
- symmetric competition needs a tie-break that the structure does not supply.

## What is and is not supplied

The **learning signal** for each regime is a supplied coupling between the
environment and the agent. It is not an analyst's verdict that the agent is
being tested against. In the access regimes it is coupled to recipients'
conditions. The study asks what each coupling produces in a learned system,
and where it fails. It does not derive that a system ought to have the access
coupling. Concern, standing and legitimacy are not established by any result
here.

## Environment

- **Centers.** Each episode has two recipients drawn from named centers. In
  training these are always A and B. Each recipient has a claim of
  `k ∈ {0, 1, 2}` deliveries. In training, `k` is drawn independently with
  probabilities (0.25, 0.5, 0.25).
- **Support.** There is a shared pool `P0` (3 in training). Each step the
  agent serves one recipient or withholds. Serving draws one unit from the
  pool; with an empty pool, serving does nothing. Unused pool units remain at
  the episode's end as retained support.
- **Delivery.** A served delivery succeeds with probability 0.9.
- **Records.** Each served attempt leaves a record: a faithful receipt in
  training, `missing` (with probability m) in one test, and `forged` (failure
  recorded as success, with probability 0.5) in another test.
- **Horizon.** Episodes last 4 steps.
- **Observation.** For each recipient: identity one-hot over {A, B, C}, claim
  size `k`, certified deliveries `c`, and unknown records `u`. The pool level
  and the step index are also observed. The `identity_only` agents do not
  receive `k`, `c` or `u`, only identity, pool and step.

## Learning signal regimes (training)

| Regime | Signal per step and at the end |
|---|---|
| `self` | 0.25 per unit of retained support at the episode end (the agent's own continuation only) |
| `proxy` | +1 per positive receipt, plus `self` |
| `access` | +1 when a delivery actually meets an unmet unit of a recipient's claim, plus `self` |
| `access_identity_only` | `access`, observation without claim features |

The access signal reads the recipient's actual condition, which is the
supplied contact. The proxy signal reads the record. Those differ when records
are missing or forged.

## Agent

The agent is a shared per-recipient Q network: a one-hidden-layer MLP with 32
units and tanh. Its inputs are the recipient's features and the global
features, and its output is the value of serving that recipient. A separate
head from the global features gives the value of withholding. It is trained
by Q-learning with discount 1, ε-greedy exploration (ε decaying from 1.0 to
0.05), learning rate 0.01, and 20,000 training episodes. There are 10 seeds
per regime, using numpy only.

**Matched alternative.** A hand-written `record_rule` serves the recipient
with the largest remaining certified need `k − c − u` (if positive),
breaking ties toward the lower identity index. It withholds otherwise. It
receives the same observations.

## Tests (2,000 episodes each, greedy policy)

| Test | Change from training |
|---|---|
| `train` | none |
| `new_claimant` | recipient B replaced by unseen center C |
| `large_claims` | `k ∈ {1, 2}` with probabilities (0.25, 0.75); pool 4 |
| `missing_records` | each record missing with probability 0.5 |
| `forged_records` | each failed delivery recorded as success with probability 0.5 |
| `scarce_symmetric` | both recipients `k = 1`, pool 1 |
| `scarce_symmetric_swapped` | as above, with recipient slots swapped |

## Metrics

- **met**: claim units actually met ÷ min(total claim, pool), counting
  actual deliveries;
- **excess**: actual deliveries beyond a recipient's claim, per episode;
- **retained**: pool units retained at the end;
- **withheld_unmet**: withholding steps taken while some claim is actually
  unmet and pool > 0, per episode;
- **first_choice_A**: in the scarce tests, the fraction of episodes whose
  first service goes to A (or to the first slot when C is absent).

All metrics come from the actual environment, never from records. They are
reported per seed and as means with ranges across seeds.

## Predictions (frozen)

**P1 (self only).** `self` agents meet ≤ 0.1 on `train`. Others'
consequences do not enter their selection.

**P2 (proxy capture).** On `train`, `proxy` agents have excess ≥ 0.5 per
episode. `access` agents have excess ≤ 0.1.

**P3 (access).** On `train`, `access` agents meet ≥ 0.9 with excess ≤ 0.1,
within 0.05 of `record_rule`'s met.

**P4 (generalization by features).** On `new_claimant` and `large_claims`,
`access` agents meet within 0.1 of their `train` value.
`access_identity_only` agents meet at least 0.2 less on `large_claims` than
`access` agents.

**P5 (missing records).** On `missing_records`, `access` agents have higher
excess than on `train`. Unknown records leave delivery decisions open, and
the agents resolve them by learned bias.

**P6 (forged records).** On `forged_records`, `access` agents' withheld_unmet
exceeds their `train` value. `proxy` agents' excess does not fall.

**P7 (symmetric tie-break).** On `scarce_symmetric`, at least 7 of 10 `access`
seeds have a within-seed first_choice_A ≥ 0.9 or ≤ 0.1. The direction varies
across seeds (both directions occur). The swapped test shows whether the
choice follows identity or slot. The tie-break is supplied by training
incidentals, not by any legitimate input.

## Acceptance and failure

Failed predictions are reported, not repaired. The first run is preserved with
a receipt. An independent reconstruction of the environment and the
`record_rule` checks the metric computations on fixed seeds. Agent training is
reproducible from seeds.

## Scope

These are tiny agents in a toy environment. Results show how the stated
couplings behave in learned function approximators. They are not evidence
about large models, deployment, or the legitimacy of any coupling or
tie-break.
