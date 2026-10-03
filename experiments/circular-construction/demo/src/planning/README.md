# Construction planning fixture

`scheduleTasks(graph)` is a deterministic, integer-second **planning** scheduler. It accepts task predecessors, safety gates, distinct part IDs, workfront capacities, finite equipment, tools and approach zones. Tasks reserve their direct resources for their duration. A `ResourceLease` holds resources across several tasks, so the example hoist and approach zone remain occupied from member placement through release. The scheduler releases completed tasks before starting new ones at the same simulation second and resolves simultaneous candidates by code-unit task ID order. Input array order has no effect.

The API is exported from `index.ts`:

```ts
import { createTwoByTwoFrameGraph, scheduleTasks } from './planning';

const graph = createTwoByTwoFrameGraph();
const result = scheduleTasks(graph);
if (result.status === 'complete') {
  console.log(result.report?.resourceLimitedMakespanS);
}
```

`createTwoByTwoFrameGraph({ injectedRecoveryBay: null })` omits the injected reseat path. `hoistCount` selects the number of interchangeable hoists; the default is one. The default graph includes recovery and repeat verification at `s1-x0-y0`. It contains eight bays across two storeys, with ground seed, temporary bracing, rail extension, member placement, capture, verification and release tasks. Every task has `mechanicalStatus: 'unverified'`. A scheduled verification operation is merely reserved work; it does not certify the connection, transfer load, or qualify the next structural state. Domain integration must wait for versioned motion, support, collision, structural and part validators before committing execution.

The planner reports `impossible` for malformed inputs such as an unavailable hoist, broken predecessor, cycle, missing brace gate or duplicate part allocation. It reports `blocked` when a valid DAG cannot advance because of live resource/part contention; a caller can also set a finite transition bound. Both cases return diagnostics and no throughput report. Runtime outcomes are proposals, not proof of construction feasibility.

## Illustrative throughput

For the default fixture with one hoist, one carrier, two robots, two workfronts and the injected recovery, the deterministic report is:

| Measure | Planned value |
|---|---:|
| Task count | 52 |
| Serial sum of task durations | 22,020 s (6 h 7 min) |
| Predecessor critical path with unlimited resources | 5,700 s (1 h 35 min) |
| Resource-limited makespan | 19,080 s (5 h 18 min) |
| Added time above predecessor critical path | 13,380 s |
| Sum of ready-task queue waits | 51,660 task-s |
| Peak ready queue / simultaneous tasks | 5 / 2 |
| Hoist busy time | 15,060 s (78.9% of makespan) |

Adding a second interchangeable hoist to the same fixture reduces the planned makespan to **17,520 s** (4 h 52 min), a 1,560 s improvement. The hoist pool is then busy for 18,300 unit-seconds across its two units, or 52.2% of available hoist time. The remaining contention is largely for the single carrier, two robots, one guide tool and workfront approach zones; a second hoist alone cannot remove those constraints.

The serial sum is an upper comparison in which only one task runs at a time. The predecessor critical path is a lower bound that ignores equipment and workfront capacity. The resource-limited makespan is the scheduler's output under these assumed durations and resources. Queue wait is summed across tasks and can exceed elapsed time. In the one-hoist case, east and west workfronts are busy for 10,680 s and 11,340 s respectively. The east front has 8,400 idle slot-seconds, with first blocking witnesses of tool availability for 4,680 s, robots for 1,620 s, hoist for 1,260 s and carrier for 840 s; west has 7,740 idle slot-seconds, including 3,600 with no ready work. These reasons describe the greedy schedule, not measured site productivity. They help locate bottlenecks and do not establish a days-scale construction claim.

The report's resource utilization counts all held lease intervals, including the time between placement, capture, verification and release. Workfront idle reasons are attributed to the first ready waiting task in stable ID order, then to the first unavailable requirement in deterministic matching order; several shortages may coexist. `dependency-or-no-work` means no ready task on that front. Durations, workfront capacities and equipment counts are assumed inputs for this fixture.
