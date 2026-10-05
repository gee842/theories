# Independent finite service queue target

5 October 2026. Target specification for a prospective synthetic transfer test. The parameters below were supplied before integrated evaluation. They are illustrative simulator laws, **not measured real service parameters**. No integrated queue outcome or policy has been evaluated at creation. The evaluation protocol, cases, controller and prediction must be frozen separately before such evaluation.

## Physical and information interface

- One or two unit-work jobs, represented by a sorted tuple of positive integer remaining deadlines. A live queue has at least one job; an empty queue is successful completion. Any unfinished job reaching deadline zero causes absorbing failure.
- A persistent hidden binary fault is static except during restart. The controller sees the job deadlines, accounts, permission regimes, action history and listed signals. It never sees the true fault or whether restart cleared it.
- `serve` works on the earliest-deadline job for one slot. Completion probability is1 if healthy and1/4 if faulty. A successful job is removed and earns1 unit afterward; the signal is `complete` or `incomplete`. There are no new arrivals.
- `inspect` costs1 and consumes a whole slot without service. Sensitivity and specificity are3/4. Signal is `positive` or `negative`; the fault itself is unchanged.
- `restart` costs2 and consumes a whole slot without service. It clears a present fault with probability3/4 under enabled enactment or1/4 under restricted enactment. A healthy device remains healthy. The only public signal is `restart`; its success is hidden.
- `wait` costs0, consumes a slot and does no work. It is included so the action grammar is explicit even where it is unhelpful.
- Restart and service are available directly without requiring diagnosis. There is no strict recommendation→enactment gate in this target.

## Accounts and chronology

Cash cap3; nonnegative treasury; no borrowing. In immediate finance, living decision points automatically transfer as much treasury as possible into cash before the action. In barred finance, no transfer is allowed. Regimes are known and fixed in a run. Successful completions credit cash to cap and retain all overflow in treasury. Neither account has fees, interest or external support.

Each slot proceeds as follows:

1. Apply the declared free start-of-slot normalization; the resulting accounts are visible.
2. Choose an affordable action using the operational information history and prepay its cost.
3. Draw that action's primitive outcome. Service may complete a job; inspect produces a signal; restart may change hidden fault.
4. Credit completion income.
5. Decrement every unfinished deadline by1. Any zero deadline causes failure. A completion at a deadline of1 is timely because that job is removed first.

An empty queue and a failed state admit no further actions. Terminal accounts are retained without additional normalization. Branches expose end-of-slot accounts before the next start normalization. `normalize` is deterministic and public, so a controller may apply it before choosing its next action. On failure, the slot's completed work and income remain recorded, even if another unfinished job expires simultaneously.

`step` accepts a true hidden state because it is a simulator transition oracle; this is not permission for the controller to use the hidden field. Belief-based evaluation must combine branches with the same public observation and update the posterior from all public cues. In particular service failure proves a present fault in this technology, whereas restart leaves a probabilistic fault belief. Queue status and accounts must not be discarded from that update by convention.

## Isolated synthetic calibration interface

`calibration_table()` returns exact primitive laws from separate component fixtures:

- one-slot completion given fixture-set healthy/faulty state;
- inspection signal given fixture-set healthy/faulty state;
- hidden state after restart given fixture-set initial fault and enactment regime.

Those fixtures contain no queue, deadline, cash process or integrated recovery outcome. The fixture may verify true fault to estimate component behavior; the operating controller does not receive fixture labels. Timing, price, capacity, earnings and observation definitions are public structural specifications. Component probabilities are returned as exact fraction strings.

This is exact synthetic component calibration from a supplied target generator, not statistical estimation or empirical measurement. A separate composed predictor should receive this table and the frozen structural interface, then predict integrated outcomes without calling `target.step`. The target does not import the reservoir model or that predictor.

## Python API

- `State(jobs, cash, treasury, fault, access='barred', enactment='enabled', failed=False)`.
- `normalize(state)` and `state.public()` define living-start public accounts.
- `legal_actions(state)` returns affordable actions, or an empty tuple if terminal.
- `step(state, action)` returns exact `Branch(probability, state, observation, expense, income)` values.
- `calibration_table()` returns isolated primitive trials only.

No initial prior, integrated starting cases, optimization criterion, policy tie rule, held-out schedule or statistical success threshold is chosen here. Those belong in the root evaluator's protocol before evaluation. The intended challenge is that equal queue length, current earnings, funds and fault belief can conceal different deadline pressure; a serious full-queue comparator must retain the deadline tuple and receive the same calibration information.
