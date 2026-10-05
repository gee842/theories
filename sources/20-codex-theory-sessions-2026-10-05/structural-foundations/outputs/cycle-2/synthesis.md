# Correction under replacement and repeated faults

Second research cycle, 5 October 2026. Ren requested execution of the next target and proposed that the underlying structure may be universal across scale, space, and time. This cycle turns that conjecture into several precise transfer tests. It combines a modular replacement experiment, a scale-and-deadline construction, and a recurrent resource model. Each isolates a different mechanism within the same operational language.

The emerging result is that **conditional constraints can transfer while numerical capacity changes**. Preserving current output or endpoint reachability is insufficient when a replacement changes information, action timing, or shared access. Conversely, a transformation that preserves transition behavior, admissible controller information, relevant interfaces, and tests preserves the corresponding correction guarantee. Changing units is one simple example; changing the number of users of a shared channel is a different physical operation.

## Replacement can remove affordable correction without changing the plant graph

The first experiment couples an operating process with a diagnostic and implementation interface. A binary fault has two incompatible corrections. The original and redacted providers have identical physical and authorized plant transitions, action costs, elapsed time, current service output, and reachable physical endpoints. The recoded provider has an isomorphic graph through its known adapter. The initial revision reserve is measured after installation; a common installation cost would be charged to each beforehand.

The original provider reveals the fault through a one-unit diagnostic. A replacement that invertibly recodes observations and command names preserves the same capacity: an explicit adapter translates the controller. A second replacement redacts the diagnostic before the controller acquires it. An independent fresh diagnostic remains available for two units. Authorization and execution each cost one unit and occupy one slot.

| Installed provider | Cheapest informative diagnostic | Minimum reserve for guaranteed authorized correction | Required slots |
|---|---:|---:|---:|
| Original | 1 | 3 | 3 |
| Invertibly recoded | 1 | 3 | 3 |
| Diagnostic redacted | 2 | 4 | 3 |

At equal reserve three, equal output, and the same three-slot deadline, only the redacted provider lacks an observation-based guarantee. Its physical correction paths still exist. The extra unit restores the guarantee through the substitute diagnostic. This separates information access from physical possibility without obtaining impossibility by deleting every substitute.

The lower bound is direct: authorized execution must pay for permission and implementation, and guaranteed success must pay for information distinguishing the two faults. Inspecting, authorizing, and applying the indicated response attain the bound. All other observed events are fault-independent until an informative diagnostic or final outcome. Prior acquired knowledge is not erased; this comparison begins before the controller has learned the fault.

The test also exposes a temporal error. If an abstraction commits all three commands before any diagnostic response can be used, it loses the guarantee even though each world has a successful command sequence. A feedback policy and a precommitted word have different quantifiers.

The [modular results](verification/modular-replacement-results.json) preserve exhaustive policy and plant checks. This example uses unpriced perfect recall within one short episode. It establishes neither paid inherited memory nor unrestricted candidate generation. Service output is financed by a declared separate feedstock and does not replenish the revision reserve during the episode.

## A constraint can hold at every size while performance changes

For `n` simultaneous hidden faults, assume each needs one diagnosis slot, then one authorization slot, then one execution slot, with strict precedence inside each module. This scheduling architecture requires authorization after diagnosis, whereas the preceding modular model permits authorization in advance. Admit all binary fault assignments, so an undiagnosed guess cannot guarantee success. Only `k` diagnostic operations can run at once; downstream stages have adequate parallel capacity. All three stages per module are prepaid from reserve `3n`.

The exact completion time is

\[
H_{\min}=\lceil n/k\rceil+2.
\]

The last diagnosis cannot finish before `ceil(n/k)` slots and needs two further stages. A batched pipeline attains that lower bound. Thus two independently equipped modules finish in three slots, while the same two modules with one shared diagnostic channel require four, despite equal repair funding.

The [scale proof and model](scale-and-deadline.md) distinguish this controlled topology change from a change of measurement units. The [enumeration](verification/scale-deadline-results.json) verifies 36 size-and-capacity combinations and 468 deadline comparisons. Infrastructure installation and idle costs are absent, so the result establishes a timing constraint rather than an economic preference for dedicated channels.

## A recurrent route needs both a bridge reserve and renewed support

Consider a prescribed repair route. A publicly visible fault stops production, but its cause is a fresh hidden binary condition. Correct repair takes `tau` slots, costs a total `C>0`, and restores production. The costs are nonnegative and prepaid along the route, with no inflow during repair. Healthy operation yields net accessible surplus `g` per slot after the route's declared operating and standby expenses.

The environment can initiate faults at least `Delta` slots apart, only when the system is healthy. It may also leave an arbitrarily long quiet interval. Each fault must be corrected by deadline `D`. Initial reserve `b0` and storage cap `B` are separate quantities, with `0 <= b0 <= B < infinity`; the first fault may occur immediately. Apparatus and institutional state at the initial fault must match the route being assessed.

For this prescribed route and fixed healthy behavior, indefinite solvency with every fault repaired by its deadline is possible exactly when

\[
b_0\ge C,\qquad B\ge C,\qquad D\ge\tau,\qquad g\ge0,
\qquad g\max(\Delta-\tau,0)\ge C.
\]

**Why these conditions are necessary.** The first immediate fault must be financed and completed in time. Negative healthy surplus allows a sufficiently long quiet interval to exhaust any finite reserve. Repeated earliest permitted faults allow only `max(Delta-tau,0)` healthy receipts per cycle. If these restore less than `C`, a positive deficit repeats until any finite initial stock fails.

**Why they suffice.** Suppose each fault begins with at least `C`. Repair consumes at most that amount. Before the next fault, the minimum healthy interval restores at least `C`; a cap of at least `C` retains enough. Longer quiet intervals cannot hurt when `g>=0`. Induction preserves the reserve available at every fault and the deadline condition. For nonnegative `g`, the reserve at successive faults obeys

\[
r_{j+1}=\min\{B,\ r_j-C+g h_j\},\qquad
h_j\ge\max(\Delta-\tau,0).
\]

This is an infinite-horizon invariant, with an explicit defeating schedule when a listed feasibility condition fails within the stated model assumptions. It is not an extrapolation from long simulations. It concerns the prescribed route. An adaptive controller may switch routes, rebuild proactively, or suspend an expensive apparatus; its optimum requires a separate game calculation.

Productive renewal is now coupled to correction: income stops during faults and resumes only after successful repair. The feedstock enabling healthy production remains an explicit external boundary input. The result therefore does not manufacture indefinite production from a closed finite store.

## Keeping ready and rebuilding are different ways to meet the constraint

The recurrent model implements three controller classes over the same declared operations: always maintain readiness, suspend during healthy operation and rebuild on demand, and an adaptive controller that may also rebuild proactively or cancel a rebuild. Fault onset is observed before the decision; the hidden fault type is not. A paid diagnostic supplies a bit that selects the correct implementation. The two decoded branches have identical cost and timing, allowing an exact symmetry reduction without giving the controller the hidden bit in advance.

Let `c` be baseline expense per slot, `p` healthy production net of that baseline, `m` standby expense, `K` rebuild expense, `L` rebuild slots, and `d,a,x` diagnostic, authorization, and implementation fees. In the base architecture,

\[
\tau_S=3,\quad C_S=3c+d+a+x,\quad g_S=p-m,
\]
\[
\tau_R=L+3,\quad C_R=K+(L+3)c+d+a+x,\quad g_R=p.
\]

Substituting these quantities into the route theorem gives explicit spacing and reserve frontiers. It does not optimize over mixed strategies. The adaptive comparison instead solves a finite safety game for every initial credit up to a stated storage cap. Deadline violations and unaffordable payments are losing transitions. A greatest fixed point identifies exactly the states from which some allowed controller can respond safely to every future admitted observable event. Saved policies keep the system inside that region indefinitely; the result does not depend on a sampled horizon or on restricting the environment to a stationary schedule.

The principal exact comparisons use cap **24**, baseline `c=1`, and fees `d=a=x=1`:

| Regime | Other parameters | Minimum initial credit if ready | Minimum initial credit if apparatus absent | What the comparison establishes |
|---|---|---:|---:|---|
| Frequent faults and affordable standby | `p=4,m=1,K=2,L=2,Delta=5,D=5` | 6 | 16 | Adaptive readiness succeeds; repeated on-demand rebuilding cannot sustain itself. |
| Expensive standby and cheaper rebuilding | `p=3,m=4,K=1,L=1,Delta=7,D=4` | 6 | 8 | Suspension and rebuilding succeed; forced permanent standby loses during a sufficiently long quiet interval. |
| Free instantaneous rebuilding | `p=4,m=1,K=0,L=0,Delta=5,D=5` | 6 | 6 | Preserving apparatus is unnecessary for this correction guarantee. |

Within each row, the controller classes are evaluated from the same actual apparatus state and initial credit. The ready and absent columns are deliberately different starting assets, not a resource-matched intervention comparison.

The first row gives a stronger bootstrap result than the cost of one repair. Ready repair costs six and lasts three slots; the two guaranteed healthy slots before the next earliest fault earn three each, restoring six. Starting without apparatus, the first repair costs ten and occupies all five slots before another fault may arrive. There is no healthy receipt before that second fault, whose ready repair costs six. Thus startup requires **sixteen**, even though one cold repair costs only ten. The two-fault schedule proves the lower bound, and the subsequently maintained loop proves sufficiency.

The second row supplies a counterweight to a blanket preservation rule. Standby spends four out of a healthy surplus of three, so an arbitrarily long quiet interval defeats it. On-demand repair costs eight, lasts four slots, and is followed by at least three healthy slots earning three each. An inherited ready apparatus reduces the first required payment to six; it does not justify perpetual maintenance for this duty. Additional exact checks show that this six-unit starting credit needs a storage cap of at least eight: caps six and seven fail. By contrast, the first row's ready loop works with cap six, while its cold start needs cap at least sixteen.

No hazard requires no diagnostic spending. Supplying the fault information reduces the adaptive initial threshold to four. Supplying standing authorization removes a different paid stage. An alternative diagnostic provider reduces the first regime's absent-apparatus threshold from sixteen to eight. A retained bit about a permanently fixed fault removes the need for repeated diagnosis after the first episode. These controls prevent recurring inquiry or preservation of one apparatus from becoming beneficial by definition.

The [recurrent model and proofs](recurrent-repair.md) and [verification record](verification/recurrent-repair-results.json) include exact winning regions, implementable policy witnesses, and decreasing-rank environmental counterstrategies for losing states. Its apparatus is diagnostic equipment; authorization and execution remain separately paid stages. The short-lived diagnostic register, public clock, and controller computations are unpriced. Paid long-term memory, unreliable evidence, candidate formation, and evolving legitimacy remain outside this model.

## What the universality conjecture now says precisely

The strongest supported statement is a universal implication over a declared class: accessible support, decision information, action control, and timing constrain which continuations a system can guarantee. The same implication can hold across implementations while giving different outcomes because the premises differ.

For example, if accessible reserve margin above the failure floor is `B>0`, unavoidable net depletion is at least `d` per unit time, and no admissible correction can finish sooner than `L`, then `dL<=B` is necessary to avoid depletion before correction. For zero margin use the inequality without dividing. The dimensionless ratio

\[
\chi=dL/B
\]

is unchanged by compatible changes of resource and time units. This invariance is exact. Applying it to a particular organism, institution, or AI system requires independently establishing what reserve is accessible, which alternatives exist, and what forces the delay. Authority and interpretation do not become conserved quantities merely by appearing in the same account.

Relabeling states or translating an interface can preserve the complete guarantee. Noninvertible summaries need a directional proof: every possible concrete outcome must be covered and the abstract controller must be implementable with concrete information. Matching interventions is also a precise established requirement for cross-resolution causal descriptions; [Rubenstein and colleagues](https://arxiv.org/html/1707.00819) provide a relevant formal precedent, with different model assumptions from our games.

The [universality memo](universality-and-sources.md) distinguishes mathematical universality, invariance under changes of description, sound abstraction, and empirical transfer across domains. Its primary-source additions on [energy games](https://arxiv.org/html/1007.1669), [consumption games](https://www.fi.muni.cz/usr/kucera/papers/cav2012.pdf), and [timed automata](https://doi.org/10.1016/0304-3975(94)90010-8) locate related established frameworks. The results do not establish mathematical novelty.

Ren's intuition has therefore become a sharper research proposition: a recurring constraint can be universal without imposing one trajectory, one scale-independent threshold, or one ethical objective. The empirical claim to test is whether measured prerequisite structure predicts interventions beyond current output and aggregate reserves. An incorrect prediction or an overlooked usable substitute must count against the proposed mapping rather than be absorbed by redefining “support” afterward.

## Next unresolved target

The completed models use supplied diagnostics and affordable computation; they do not explain how the system produces a new interpretation. The next bounded target is to make evidence retention and controller succession part of the recurrent resource loop. A successor should receive only paid retained records plus specified public signals, and a future fault may change whether the old diagnosis remains relevant.

The discriminating question is whether the winning region and replacement correspondence survive when the controller must pay for the information state on which its policy relies. Compare preservation, fresh inquiry, and a substitute provider at matched initial assets and fully recorded cash flows. Retain a fixed-fault control where one remembered bit suffices, so permanent investigation is not rewarded by construction. This extension is proposed work, not a result of the present cycle.
