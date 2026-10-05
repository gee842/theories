# Prospective finite service queue challenge

5 October 2026. This locally frozen protocol precedes execution of integrated target policies. The service laws and expected deadline counterexample were chosen deliberately and are not blind discoveries. This is a new synthetic challenge to a proposed sufficient description, not completion of the earlier two-gate transport study and not a real service experiment.

## Question

Does a description retaining job count, fault belief, accounts, finance and enactment settings, and time, while omitting the deadlines of unfinished jobs, preserve recovery predictions? Can a separate composition of isolated component laws reproduce the full target's exact finite outcomes when deadlines are retained?

The first question is a sufficiency challenge. The second is an implementation and compositional check; both predictors with the full mechanism specification can be equally accurate, so agreement does not demonstrate an additional law or compression advantage over conventional queue control.

## Target and calibration

The independently coded target has one or two unit-work jobs, observed integer deadlines, a hidden persistent healthy/fault mode, cap-three cash and a treasury. Actions are serve, inspect, and restart. Serve costs zero and succeeds with probability one when healthy and one-quarter when faulty; it completes the earliest-deadline job and earns one unit after the action. Inspect costs one, consumes the slot, and reports the mode with accuracy three-quarters. Restart costs two, consumes the slot, and clears a fault with probability three-quarters under enabled enactment or one-quarter under restricted enactment; the success is hidden. Healthy mode stays healthy. Mode is otherwise unchanged. Immediate finance normalizes accounts before each action; barred finance never transfers. Bills precede output receipts. Overflow is retained in treasury.

After each action, decrement every unfinished job's deadline; an unfinished job reaching zero fails the episode. Completion and failure are absorbing. The target's isolated component calibration returns distributions for serving each mode, diagnosis in each mode, and restarting each mode under each enactment setting. These are exhaustive observations of stipulated component kernels, not empirical estimates and not integrated recovery rates. A separate predictor composes them with the declared queue and payment chronology.

## Frozen evaluation cells

Initial queues are the nine sorted tuples of one or two deadlines in 1 through 3: (1), (2), (3), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3). Initial fault priors are 0, 1/2, and 1. Total funds are three, initially either cash0/treasury3 or cash3/treasury0. Cross finance barred/immediate and enactment restricted/enabled. Evaluate four fixed observation-admissible policies over at most three slots:

1. Serve every slot.
2. Attempt restart in the first slot, then serve.
3. Attempt inspection in the first slot; if a paid first-slot inspection reported positive, attempt restart in the second slot; otherwise serve. Serve subsequently.
4. Deadline-aware: serve whenever the earliest remaining deadline is one; otherwise follow policy3.

Whenever a paid action is unaffordable after the declared finance rule, serve instead. This fallback is part of each policy, not an invalid-action repair selected after seeing results. The policies do not see the hidden mode or whether restart succeeded.

There are 9×3×2×2×2×4 = 864 cells. Outcomes are exact failure probability, completion probability, expected spending, tests, restarts, and terminal cash and treasury. No scalar ethical score is imposed. No optimization or superiority claim over the full policy class is made.

## Predictions and decision rules

The coarse state is expected to fail because restarting consumes time needed by urgent jobs. The first-slot restart policy from a known-fault, cash-three start with one deadline-one job must fail; a deadline-three job admits time for restart and service. The same coarse initial state therefore can have different outcome laws under the same policy.

Before target policy execution, freeze the separate predictor and all 864 predicted outcome vectors and their hashes. Then run the target's separately implemented transition function through an independent evaluator. Exact disagreement in any outcome coordinate rejects the composition as implemented; investigate and report corrections openly rather than changing a prediction silently. At least one same-projection/different-outcome pair rejects the coarse sufficient-state claim.

Also compare the first two policies on urgent versus slack jobs. A change in their ranking would demonstrate that the omitted deadline matters to a choice, not just to a descriptive outcome. Report whether this occurs, without requiring it as a condition for the primary abstraction test.

No sampling interval is required because every branch is evaluated with exact rational arithmetic. Original frozen studies and reference repositories remain unchanged. A corrected state retaining deadlines is an independently specified comparator here, not a repaired hypothesis counted as the original coarse model succeeding.
