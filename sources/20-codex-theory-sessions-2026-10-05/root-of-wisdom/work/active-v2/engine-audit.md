# Pre-dispatch engine and scoring audit

Audited 2026-10-05 after the initial design audit. This phase inspected engine.py, the v2.1 environment and public cases, protocol.json, and the independent verifier. No participant material or responses were inspected, and no participant was dispatched. Fixtures were run in memory without modifying cases, engine, or verification results.

**Result:** the public-belief oracle and mechanical feedback passed the checks below. One parsing-boundary issue should be settled before dispatch; the aggregate scorer has not yet been implemented or audited.

## Exact checks passed

- Engine Q-values match the independently implemented verifier at all **74 reachable ordered public histories**, including suboptimal query paths. Initial optimal values are exactly **3, 7, 3, 8, 5, 2**. All initial ties are retained.
- The oracle uses priors, deterministic-response conditioning, completed queries, cash, and time. Changing the selected private world leaves initial Q-values unchanged. Inspection found no use of the private world in oracle calculations; only mechanical query realization and terminal realized loss use it.
- Fees enter both cash feasibility and the loss objective. Residual loss enters only the objective. Query durations and terminal duration enter deadline feasibility, including equality at the deadline. Prerequisites and nonrepetition are enforced.
- Separate in-memory cash-boundary fixtures passed: after two fee-1 queries, a fee-1 terminal action is infeasible at budget 2 and feasible at budget 3. The six actual cases' cash caps do not bind, so these cases do not independently test sensitivity to hard cash affordability; they test fees in the objective and a binding deadline.
- Missing/blank reason, unknown target, wrong command kind, duplicate episode commands, unmet prerequisites, and repeated queries force the zero-fee/time fallback. Already paid query fees remain charged. Reasons over 35 whitespace-delimited words execute the selected command and separately record the cap violation, as requested.
- Query feedback contains exactly the selected query answer and mechanically determined public bookkeeping. It does not return oracle values, optimality labels, posterior calculations, or realized terminal losses. Closing a terminal episode reveals no new private outcome.
- Public rendering matches the environment's public model. The v2.1 seed reproduces the declared six sequential independent draws exactly. Reusing a draw across conditions/repetitions preserves pairing; coincidentally equal draws within the three matched case pairs do not create a public dependence.

## Resolve before dispatch

`apply_saved_round` calls `json.loads` without catching malformed JSON. A syntactically invalid full response therefore raises an exception rather than applying the common fallback policy. Preserve the exact raw response and freeze a common parse-failure policy. One consistent implementation is to record the parse error and pass an empty response to `step`, causing every then-open episode to take fallback. Do not manually repair one participant's substantive commands.

Clarify that extra commands for unknown/already-closed episode IDs are logged and ignored when valid commands for the open episodes are also present. An unknown ID that replaces a required open-episode command leaves that required command missing and triggers its fallback. This is what the engine currently implements; blanket wording that every unknown ID invalidates the whole batch would describe a different policy.

## Scorer requirements

Count initial optimal commands using `optimal_command`, accepting all exact ties. A formatting-invalid command is invalid even if its forced fallback happens to be optimal; its effective Bellman gap can consequently be zero while initial command success is false. Preserve those two meanings rather than treating this as a scorer contradiction.

Report initial Bellman gaps and per-case outcomes alongside aggregate counts. Count strict unnecessary continuation only when the chosen query's public-belief Q-value exceeds the best immediately feasible terminal action. The engine's comparison correctly includes optimal continuation and costs; it does not mistake an unchanged realized action for wasted inquiry.

Keep terminal conditional excess loss, actual resource spending, and private-world realized loss separate. Sum visited-state gaps only as a trajectory-local diagnostic. Different conditions can reach different beliefs, so terminal conditional expected losses alone are not a common-state causal comparison. Resource accounting should include terminal action fees/time as well as queries.

The public finite grammar supports active query selection under known models. It does not test discovery of unspecified distinctions or validate the stipulated purposes. The six cases are three closely related constructed pairs and the two contexts per condition are the replication unit for order/carryover concerns.

## Reviewed content hashes

These identify the inspected snapshot; later changes require a narrow recheck.

```text
engine.py        4b5422ec5c6a7475428436ae177108f3ceae8e9a1e8af151ddb3b5786d5bc33d
environment.json 00a7f187c2b86c4a5847545b6bf2b1488741151579dca30ded96534e60403e1e
public-cases.json 0c224b081f19785eb588eb84cea1c37b91c2b7a73c6703fea59cd8561259af2c
protocol.json    93067f7643316912d93de5a09f6ba4f5fbf1fd888e32526cf493227a93c51c1b
```
