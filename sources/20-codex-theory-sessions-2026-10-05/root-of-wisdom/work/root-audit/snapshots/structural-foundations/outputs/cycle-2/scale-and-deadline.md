# Scale and shared correction capacity

This checked finite model addresses Ren's conjecture that the structural constraint applies across scale. Its result is that a counting and precedence constraint transfers across every size in the declared model class, while numerical recovery capacity changes when the shared interface changes. This is conditional universality, not an empirical finding that real systems at all scales have this architecture.

## Model and exact frontier

There are `n >= 1` operating modules. Each has developed a fresh hidden binary fault, and all `2^n` joint assignments are admitted; no probabilistic independence assumption is needed. Each correct response depends on its own fault, and a wrong response is irreversibly unsuccessful. A controller must guarantee successful correction of every module. Each module has a supplied three-stage protocol: diagnose, authorize, execute the indicated correction. Diagnosis is perfect and must occur before its authorized response; no alternative response or informative side channel exists in this model.

Each stage occupies one whole time slot and costs one resource unit. Authorization can start only in a slot after diagnosis finishes, and execution only after authorization finishes. A stage cannot consume another stage's result within the same slot. At most `k >= 1` diagnoses run simultaneously. Authorization and execution have separate adequate capacity and may run in parallel across modules. The controller retains diagnoses without a retention charge in this scheduling example; it does not purport to model paid memory.

The total initial reserve is `3n`, so every required payment is covered, without borrowing, transfers, or productive inflow during repair. Costs and diagnosis reliability are identical for every module. The comparison changes diagnostic parallelism, not per-module funding or current nominal service capacity.

The minimum completion time is exactly

\[
H_{\min}(n,k)=\left\lceil\frac{n}{k}\right\rceil+2.
\]

Equivalently, meeting an integer deadline `H` is feasible precisely when

\[
H\ge3\quad\text{and}\quad n\le k(H-2).
\]

**Necessity.** Without a diagnostic, the final action for at least one hidden binary fault cannot be guaranteed correct; different faults require incompatible actions. Thus all `n` diagnoses are required. No more than `k` can finish per slot, so the last diagnosis finishes no earlier than slot `ceil(n/k)`. That module still needs its authorization and execution in two subsequent slots. This argument allows arbitrary adaptive scheduling and randomization; neither can create an earlier guaranteed diagnostic result or remove a mandatory stage.

**Sufficiency.** Diagnose the next batch of up to `k` modules each slot. Simultaneously authorize every module diagnosed in the previous slot and execute every module authorized in the previous slot. The last batch completes exactly two slots after its diagnosis. Every payment decreases the prepaid reserve by one, so no prefix deficit occurs. This pipeline attains the lower bound.

## A replacement that changes scale behavior

One module with its own diagnostic channel completes in three slots. Two independently equipped modules also complete in three slots, in parallel. Replacing their channels with one shared channel preserves each isolated module's diagnostic procedure and leaves the total reserve at six, but joint correction now requires four slots.

| Configuration | Modules | Parallel diagnostic channels | Reserve | Earliest all-module correction |
|---|---:|---:|---:|---:|
| One equipped module | 1 | 1 | 3 | 3 slots |
| Two independently equipped modules | 2 | 2 | 6 | 3 slots |
| Two modules sharing one channel | 2 | 1 | 6 | 4 slots |

The shared-channel system can still reach complete recovery with enough time. It fails the tighter deadline even though endpoint reachability, per-module expense, and each isolated module's protocol look adequate. The omitted relation is contention for a timed interface.

This is not a comparison at equal diagnostic infrastructure: the number of parallel channels is deliberately the manipulated cause. Nor does it establish an economic preference for separate channels. The model has no installation or idle-maintenance prices. Those would be needed to compare the tradeoff between capacity and its cost.

## What remains invariant across scale

Multiplying the accounting unit by a positive factor changes the numeric reserve and all costs by that factor without changing feasibility. Uniformly changing the time unit changes stage durations and the deadline together, without changing which schedules meet it. These are changes of description.

Increasing `n` at fixed `k` is a physical change in the workload-to-interface relation. It is not a change of units. Increasing both proportionally preserves some ratios but still requires respecting integer batches and stage order. The invariant is the relation between required work, accessible throughput, and deadline, not a claim of identical recovery time at every size.

The useful cross-domain question is therefore: which independently measured process corresponds to a stage, what makes it necessary, which resource or relationship limits simultaneous execution, and what deadline matters? If a domain admits an alternative repair route, overlapping stages, a common informative signal, or a different protected duty, this exact frontier need not apply. Such a case challenges the mapping rather than the algebra.

## Checks and evidential status

The [checker](verification/check_scale_deadline.py) enumerates all reachable count states and all non-idle stage allocations for `n=1,...,8` and `k=1,...,n`. Every enumerated shortest completion time matches the formula. It also checks deadlines zero through twelve and verifies payment balance on every enumerated transition. There are 36 frontier cases and 468 deadline cases; [all assertions passed](verification/scale-deadline-results.json).

The enumeration aggregates interchangeable modules by stage. Interchangeability is justified by identical durations, costs, interfaces, and independent hidden faults; it would fail if modules had different deadlines or resource needs. Correct downstream action selection is justified by the supplied perfect diagnostic. This is a proved scheduling result with finite checks, not a discovery model, an empirical law, or a novel scheduling theorem.
