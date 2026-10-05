# How a decision rule adopts or loses sustainable repair

This experiment adds an actual, repeatedly executed selection rule to the [third-cycle repair process](../cycle-3/scale-and-renewal.md). It explains infrastructure adoption **conditional on that rule**, its horizon, the known process, and available funds. It does not explain the origin of the rule or horizon. No infinite-viability test is used by the implemented planner.

The main finding is stronger than a short-horizon planner eventually running out of money. Its first successful repair can move the process outside the set from which **any** permitted policy can continue indefinitely. The same short-horizon rule can nevertheless maintain a sustainable apparatus if it inherits that apparatus already installed.

## The physical process and what changes

Retain eight modules, perfect paid diagnosis, and the strict diagnose–authorize–execute pipeline. Each required stage takes one slot and costs one unit per module. The selected channel count `k` limits simultaneous diagnoses. All production stops until all modules are repaired. Per-slot operating cost is one per module, healthy surplus before channel upkeep is four per module, and every installed channel costs two per slot to maintain. Repair must finish in six slots.

For this experiment, fault waves occur exactly eight slots apart. This is a specified deterministic timing law, and one of the histories admitted by the previous robust model. Fresh hidden fault bits remain arbitrary; the diagnostic pipeline corrects each assignment. Its within-episode report registers remain supplied infrastructure. The separate paid-learning model studies a different information problem and is not silently inserted into this pipeline.

There is now a design decision at every fault boundary. If `k` channels are installed, choosing `j>k` costs `30(j−k)` before repair. Removing channels costs zero and yields no resale proceeds. Removed channels must be bought again if needed later. Installation has zero modeled latency. These are new physical intervention rules; the earlier fixed-infrastructure theorem did not permit them.

The model starts with 240 cash units, no diagnostic channels, and carried-cash cap 240. Production modules and other apparatus are supplied assets. At each boundary the sequence is:

1. Choose the channel count and prepay any additions.
2. Execute the repair pipeline, prepaying every slot. No income arrives during repair, including its completion slot.
3. Receive healthy gross production before paying each healthy slot's operating and channel expenses; cap carried cash afterward.
4. Begin the next scheduled fault wave eight slots after the preceding onset.

The fixed model, planning program, public clock, and computation are supplied without a further price here. The existing costs cover installation, operating support, and diagnosis; this is not a claim that deliberation is free in the world.

## The boundary transition and its physical implementation

For a chosen design `j`, define

\[
T_j=\lceil8/j\rceil+2,
\quad C_j=24+(8+2j)T_j,
\quad q_j=32-2j,
\quad g_j=(8-T_j)q_j-C_j.
\]

Only designs finishing by the six-slot deadline are admitted. From current state `(b,k)`, let `I(k,j)=30\max(j-k,0)`. The next complete cycle is payable precisely when

\[
b-I(k,j)\ge C_j.
\]

The healthy increments in this parameter regime are nonnegative. Thus every paid pipeline and healthy-slot prefix is safe exactly when the displayed first-episode guard holds. The boundary transition is

\[
(b,k)\longmapsto
\left(\min\{240,b-I(k,j)+g_j\},j\right).
\]

The program independently expands this transition into installation, diagnostic stages, operating payments, gross receipts, and overflow. It checks the compressed transition against that physical sequence rather than assuming that endpoint solvency proves the prefixes.

| Channels | Repair slots | Episode expense | Net cash change per cycle before new installation |
|---:|---:|---:|---:|
| 1 | 10 | 124 | Inadmissible: misses deadline |
| 2 | 6 | 96 | −40 |
| 3 | 5 | 94 | −16 |
| 4 | 4 | 88 | +8 |
| 5 | 4 | 96 | −8 |
| 6 | 4 | 104 | −24 |
| 7 | 4 | 112 | −40 |
| 8 | 3 | 96 | −16 |

Four channels are the only design with nonnegative recurrent net cash change in this supplied regime. That fact is used in the analyst's capacity proof below. It is **not** an admissibility filter in the actual planner.

## The implemented selection rule

For an integer planning horizon `h≥1`, the rule enumerates every sequence of design choices that can complete the next `h` cycles without missing a payment or repair deadline. It chooses the sequence with the greatest terminal carried cash. Ties use the lexicographically smaller sequence of channel counts. It executes only the first choice, observes the new cash and installed apparatus, and replans with horizon `h` at the next boundary.

Write the finite forecast recursively as

\[
V_0(b,k)=b,
\qquad
V_h(b,k)=\max_{j\text{ with payable cycle}}
V_{h-1}(F_j(b,k)),
\]

where branches that cannot complete all remaining cycles are excluded. This is an implemented finite cash objective, not an invocation of indefinite viability. Terminal cash is counted once; receipts and expenses enter through the transition. There is no terminal salvage value or extra continuation bonus.

If no complete `h`-cycle plan exists, the rule uses the greatest smaller positive depth that is feasible. It fails the continuing-duty test when no complete next repair can be implemented. This fallback matters: an empty two-cycle forecast does not mean that the current physical system cannot complete one more cycle.

The role of the horizon is therefore precise. It is the period over which the rule credits future financial consequences. It is not automatically a person's lifespan, institutional tenure, time preference, or competence. Those interpretations would require a measured mechanism mapping them to this rule.

## A short horizon loses capacity before reserves are exhausted

Starting from `(240,0)`, the feasible first designs are two, three, and four channels. Their one-cycle final cash values are 140, 134, and 128. A one-cycle planner therefore installs two channels.

| Boundary or completed cycle | One-cycle planner | Two-cycle planner |
|---|---|---|
| Initial state | Cash 240, channels 0 | Cash 240, channels 0 |
| First installed design | 2 | 4 |
| After first complete repair and replenishment | Cash 140, channels 2 | Cash 128, channels 4 |
| After second cycle | Cash 100, channels 2 | Cash 136, channels 4 |
| After third cycle | Cash 60, channels 2 | Cash 144, channels 4 |
| Fourth fault | No payable complete repair | Continues with four channels |

The two-cycle forecast chooses four channels immediately: completing two cycles leaves 136, compared with at most 118 after first choosing three and at most 100 after first choosing two. The one-cycle rule replans repeatedly and still chooses two. With adequate cash, upgrading from two to four costs 60 and improves one cycle's return by only 48. In the displayed run there is an additional obstruction: after the first cycle, its 140 cash cannot pay the 60 upgrade **and** the 88-unit first repair with four channels.

### Exact continuation capacity with movable infrastructure

In this deterministic periodic model, the set of states from which some admissible policy can complete every future cycle is exactly

\[
\boxed{b\ge88+30\max(4-k,0),\qquad b\le240.}
\]

**Sufficiency.** Install enough channels to reach four, or discard any excess. The displayed cash pays the additions and the 88-unit repair. Retaining four then maps cash to `min(240,b+8)` at every boundary, preserving the 88-unit repair reserve.

**Necessity.** If `k≥4` and `b<88`, no design has an affordable first complete episode: 88 is the smallest episode expense and additional installation is nonnegative. For `k<4`, consider capital-adjusted support `P=b+30k` until four channels are first reached. A transition among smaller admissible designs either preserves installed capital through purchase or discards it without refund; both designs two and three have strictly negative cycle cash changes. Hence such complete cycles cannot increase `P`. An attempted first transition to design `j≥4` requires

`P ≥ 30j+C_j ≥ 208`.

If initially `b+30k<208`, no detour among smaller designs can make that transition payable. Remaining among them forever is also impossible with finite cash because every cycle has a strictly negative change. Designs above four likewise have negative changes, and reaching them from below four requires at least as much initial support as reaching four. Thus the threshold is necessary.

The program also computes the exact greatest fixed point over all 2,169 cash/design states and confirms this entire threshold, independently of which planning rule is used. A separate descending-set implementation agrees on the full winning set; both implementations use the declared boundary transition.

Initially `(240,0)` is viable because 240 exceeds 208. After the one-cycle planner's first successful cycle, `(140,2)` is **not** viable because it needs at least 148. After the two-cycle choice, `(128,4)` is viable because it needs only 88.

Changing the horizon after the first short-horizon choice cannot rescue the displayed state under the admitted physical rules. Its problem is no longer only which policy is selected. No policy can produce indefinite continuation from that state without a new resource, a cheaper route, or a changed physical mechanism.

More generally, if the cap accommodates the initial cash, initial wealth between 208 and 247 inclusive permits direct sustainable installation but the one-cycle rule's first choice loses that possibility. It installs two and leaves `b=W−100<148`. Larger finite starting wealth can postpone the trap; it does not make this repeatedly applied one-cycle preference sustainable.

## Adoption and inheritance have different thresholds

Once four channels are installed, both the one-cycle and two-cycle planners retain them for every cash state from 88 through 240. The checker verifies all 153 states for each rule; the transition `b'=min(240,b+8)` proves continuation indefinitely.

Consequently a successor using the short horizon can continue successfully if it inherits four channels and sufficient reserve. Inheriting a longer planning horizon is not necessary in this particular regime. Starting from no channels with the same short-horizon rule produces the failure above.

This separates **constructing an apparatus**, **maintaining an inherited apparatus**, and **transmitting a decision rule**. We hold physical assets fixed when replacing the horizon. Resetting the channel count to zero would destroy real capital and define a different succession intervention. Changing the decision rule at a boundary has no extra modeled handoff fee in this comparison; the companion transmission model explicitly charges its own succession process.

No general preference for inherited institutions follows. An inherited apparatus can become unnecessary, costly, or harmful in another regime. The claim is about the supplied financial process and continuing-duty test.

## A conditional horizon threshold

Consider the two-design restriction `{L,R}` with constant cycle returns `g_R>g_L`, added initial installation expense `A` for `R`, ample prefix finance, no binding cash cap, no resale, and the same terminal-cash criterion. Suppose `R` is physically available immediately. Over a horizon `h`, selecting it rather than retaining `L` improves terminal cash exactly when

\[
\boxed{h(g_R-g_L)>A.}
\]

Equality retains `L` under the supplied tie rule. Any profitable eventual switch to `R` is weakly improved by making it immediately: the installation expense is the same and more high-return cycles follow. Reverting to `L` saves no already-paid installation expense and reduces the return. These assumptions justify comparing the constant-design plans; they do not hold for arbitrary lumpy finance, changing returns, or reversible resale.

For designs two and four here, `g_R−g_L=48` and `A=60`, so one cycle rejects the investment and two cycles favor it when both can be financed. A longer horizon cannot override a missing first payment. With initial cash 207 and no channels, indefinite continuation is impossible regardless of horizon; the exact initial requirement is 208.

This is an infrastructure-adoption mechanism under a supplied objective. It does not require an infinite optimizer, but it does use correct forecasts. Learning those forecasts, paying for the information, and passing it to successors are additional causal tasks.

## Controls where continuation is not the selected duty

**No fault.** Remove the fault mechanism and allow zero diagnostic channels. The same terminal-cash rule selects zero channels: no repair interface is required and maintaining one reduces healthy income. For this check the cap is raised to 2,000 to prevent early saturation from hiding the financial differences. This is a declared no-hazard control, not a causal claim that every existing institution should disappear when one task is removed.

**Permitted ending after one cycle.** Keep the fault and start at `(240,0)`, but declare the duty complete after one successful cycle and permit a costless, harmless exit then. Two channels meet that finite duty and leave the largest cash balance, 140. The fact that the same action would later lose indefinite capacity is not a violation of this different duty. Real closure obligations or harms would need their own costs and tests.

**Insufficient initial finance.** Correct knowledge and a longer forecast do not create support. The wealth/horizon grid separately records the number of completed cycles and entry into the independently certified viable region. It never calls a merely long simulated survival trace an infinite proof.

## What transfers under physical replication

Replicate modules, cash, installed channels, and the cash cap by a positive integer factor `a`. Keep the price per added channel and the per-module production parameters fixed. Crucially, the new admissible design menu is the **scaled image** `{aj:j in the original menu}`. This excludes additional intermediate designs from an alleged exact comparison.

Repair duration is unchanged, and installation, repair expenses, healthy inflows, and carried cash scale by `a`. Therefore every feasible design sequence maps to a feasible replicated sequence and conversely. Every terminal cash objective scales by the same positive factor; feasibility depth and tie order agree. The actual rolling selector, including its fallback, chooses correspondingly scaled designs. Hence both the short-horizon failure and the longer-horizon continuation transfer to the replicated process.

Allowing every intermediate channel count after replication changes the action menu. That may be a useful larger system, but exact selector equivalence then requires a new argument. Likewise, different forecasting, copying, or environmental probabilities cannot be dismissed as a change of scale.

## Verification and remaining limits

The [checker](verification/check_adoption_dynamics.py) and [results](verification/adoption-dynamics-results.json) preserve:

- 120 horizon-planning comparisons against exhaustive design-word enumeration using expanded slot ledgers;
- 17,352 compressed-transition comparisons with explicit installation, stage, receipt, and payment steps;
- the full 2,169-state continuation kernel and 153-state invariant for both actual horizons;
- a [1,446-row wealth/horizon frontier](verification/adoption-frontier.csv), with minimum viable initial cash 208 for the tested horizons two through six;
- 180 exact replication checks and 120 two-design horizon-threshold checks, including exact ties.

All assertions passed. The horizon-one planner never enters the viable invariant in that wealth grid. The horizon-two continuation claim comes from the invariant and proof, not from its forty-cycle trace.

The experiment remains conditional on periodic faults, correct model knowledge, free planning computation, fixed objectives, zero installation delay, and the specified channel purchase/removal rules. It establishes actual infrastructure adoption under an explicit mechanism and demonstrates a loss of future capacity. It does not establish that longer horizons always improve behavior, explain the evolutionary origin of the horizon, or provide empirical evidence about a real institution.
