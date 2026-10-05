# Recurrent paid repair: an exact finite model

5 October 2026. This study executes the recurrent-repair target in a deliberately small model. It derives a reserve–delay–disturbance-spacing frontier for two prescribed routes, solves the full allowed finite control game, and preserves both winning controllers and losing counterstrategies. Infinite guarantees follow from invariants and a greatest fixed point, not from long simulated survival.

The results are conditional mathematical constructions. The action grammar, costs, perfect diagnostics, protected service duty, and disturbance class are supplied. They neither establish a universal preference for standby nor solve alignment. No files in the parent research workspace were changed.

## 1. What the model makes endogenous

A productive function yields support only while healthy. Every new fault stops that output. A successful diagnosis, authorization, and implementation restores the function; without repair, its support source does not continue producing in the background. Investigation apparatus can be retained in paid standby, suspended, rebuilt while healthy, rebuilt after a fault, or replaced by a paid alternative diagnostic provider in a control case.

What remains fixed is just as consequential. The possible faults and repairs are a supplied binary grammar. Passive fault detection is immediate and free. There are no competing purposes, strategic manipulation, noisy reports, or discovered new interpretations. The apparatus is **diagnostic-specific**: it is not the whole institution and is not required for authorization or implementation once the needed bit is known.

## 2. Parameters and exact chronology

Primitive output, fees, reserves, and delays below are nonnegative integers. Operating cost and the deadline are positive integers, and episode cost is positive in the theorems. The derived net surplus `p` and net cycle balances may be negative.

| Symbol | Meaning |
|---|---|
| `B` | Maximum reserve carried from one slot to the next |
| `b₀` | Initial accessible reserve, independently varied from zero to `B` |
| `y` | Gross healthy-slot support output, requiring supplied external feedstock |
| `c` | Operating support spent in every slot, including outage slots |
| `p=y−c` | Healthy net output before apparatus expense |
| `m` | Standby expense for carrying a ready diagnostic apparatus through a healthy slot |
| `K,L` | Rebuilding fee and extra fault slots before a rebuilt apparatus can diagnose |
| `d,a,x` | Diagnostic, authorization, and implementation fees |
| `Δ` | Minimum separation between fault onsets, measured in slots |
| `D` | Maximum permitted outage duration for each fault |

The state at a slot boundary contains reserve, elapsed time since the previous onset (clipped at `Δ`), current healthy/diagnose/authorize/execute phase, completed fault-slot count, and apparatus status. The apparatus is absent, ready, or rebuilding with an integer remaining delay. The fixed-fault control also carries a free remembered diagnostic bit.

Each slot has the following order:

1. If the function is healthy and at least `Δ` slots have elapsed since its previous onset, the environment may cause a new fault or remain quiet. A first fault may occur immediately at the initial boundary. The occurrence of a fault is publicly visible before the controller acts. Its cause `θ∈{0,1}` is hidden.
2. A quiet healthy slot produces `y` support units from the declared external feedstock. Every fault slot, including the slot in which repair completes, produces zero.
3. The controller selects its action using the visible event, state, and any acquired diagnostic report. Current receipts are available before current operating expense and action fees. The action is unaffordable if these available funds cannot pay it.
4. Rebuilding and the selected action complete their one-slot progress. Diagnosis reveals the current bit; authorization and implementation each require their own later slot. A correct implementation restores health at the end of its slot. A wrong implementation would fail irreversibly.
5. Remaining funds above `B` are spilled, and clocks update. Output resumes only in the next healthy slot. An unresolved fault after its `D`th slot is a violation; completion exactly in that slot is allowed.

The transaction identity is checked on every generated affordable transition:

`b_after + operating + fee + spill = b_before + gross_receipt`.

**Cap convention:** `B` caps carried reserve after receipts and billing. Current receipts can flow directly to current expenses before surplus is deposited or spilled. It is not a hard bound on the instantaneous amount of cash immediately after a gross receipt. Imposing such a peak bound or moving output after payment would define a different model and could change the reserve thresholds. Fault-period fees never use future restored output.

During healthy periods, absent apparatus can remain absent or start a proactive rebuild. A ready apparatus can be suspended without a refund or retained at cost `m`. An unfinished rebuild can continue or be cancelled. Completing a rebuild in a healthy slot incurs that slot's ready-carry fee. During faults, local rebuilding incurs `K` at its start and `L` extra zero-output slots; if `L=0`, rebuilding and the diagnostic occur in the same slot. Authorization and execution remain separate. At execution, the controller can retain or suspend the apparatus for future episodes.

New faults occur only while healthy; they do not interrupt an already unresolved fault. Under an earliest-onset adversary, a repair lasting `τ` slots is followed by exactly

`g(τ)=max(0,Δ−τ)`

healthy earning slots. If `τ≥Δ`, the next fault can start immediately after recovery and there is no healthy earning interval.

### Information and memory

Every ordinary episode has a fresh hidden bit, unconstrained by earlier bits. This is an adversarial uncertainty class, not an iid probability assertion. Seeing that output stopped reveals the onset but not the correct repair. The diagnostic supplies a perfect report. A realizable controller retains its reported bit through authorization and applies that reported repair. Its storage is explicitly free in this first model.

The solver collapses the two report values into one symmetric information state. Before diagnosis the two causes share the same available action; after diagnosis, their continuation graphs are isomorphic under exchanging `apply 0` and `apply 1`. The abstract action `apply_reported` means the concrete rule `apply(report)`. It is not an oracle that sees the hidden cause. Incorrect guesses cannot provide a sure guarantee and are not added as winning alternatives. The fixed supplied workflow requires diagnosis, then authorization, then implementation; it does not claim all real repair processes have this order.

The environment's observable branch is **fault versus quiet**, never `θ=0` versus `θ=1`. Consequently the predecessor order `for every observed event, there exists a controller response` does not leak the hidden cause. A free finite report register suffices for the witness controller; allowing perfect recall supplies no information about unconstrained fresh future bits.

## 3. Exact route frontier

These theorems concern local diagnostics required anew every episode, an always available authorization service at the stated per-episode fee, no alternative provider, and positive episode expense. The no-hazard, full-information, and retained-fixed-bit cases are separate controls.

### Route S: keep a ready apparatus in paid standby

Start with the apparatus ready. Always retain it, diagnose each fault immediately, then authorize and implement. Put

`τ_S=3`, `C_S=3c+d+a+x`, `g_S=max(0,Δ−τ_S)`.

The route satisfies the indefinite service-and-budget duty against every admitted disturbance history **if and only if**

`b₀≥C_S`, `B≥C_S`, `τ_S≤D`, `p−m≥0`, and `g_S(p−m)≥C_S`.

When these conditions hold, the least initial credit for this **ready** start is `C_S`.

### Route R: remain suspended while healthy and rebuild after a fault

Start with the apparatus absent. Never rebuild or maintain it while healthy; rebuild immediately on each fault, diagnose, authorize, implement, and suspend again. Put

`τ_R=L+3`, `C_R=K+(L+3)c+d+a+x`, `g_R=max(0,Δ−τ_R)`.

The route satisfies the same duty **if and only if**

`b₀≥C_R`, `B≥C_R`, `τ_R≤D`, `p≥0`, and `g_R p≥C_R`.

Its least initial credit for this **cold** start is `C_R`. No larger finite reserve repairs a violated recurrent-flow inequality: additional credit can only postpone exhaustion. Immediate rebuild is best within this reserve-only route, since fault-period delay generates neither income nor additional information. The unrestricted game below additionally permits proactive healthy-period rebuilding and suspension choices, so the route comparison is not presented as the global optimum.

### Proof of both claims

Let `C,τ,g` be the chosen route's episode expense, duration, and minimum healthy gap, and let `q` be its healthy net accumulation rate (`p−m` or `p`). A first immediate fault requires `b₀≥C`; a recurrent episode requires the storage bound `B≥C`. Since every fault expense is paid before any restored output, this total also suffices for every prefix of that fixed repair sequence. Duration must not exceed `D`.

If `q≥0` and `gq≥C`, the reserve at successive onsets satisfies

`b_next = min(B, b_onset−C+hq) ≥ C`, for every `h≥g` and `b_onset≥C`.

Thus onset reserve at least `C` is an inductive invariant. Healthy delays cannot reduce it. Every fault is completed within `τ≤D`, and all intermediate bills are affordable. This proves the infinite guarantee, including histories with indefinitely many faults and histories that eventually remain quiet.

Conversely, if `q<0`, an arbitrarily long quiet interval exhausts every finite reserve under that prescribed route. If `gq<C`, an adversary choosing each earliest allowed onset creates a strict deficit each cycle; finite reserve is eventually exhausted. If the deadline fails, the first fault cannot be completed on time. The storage and initial-credit failures follow from the unpaid episode prefix. This exhausts the stated cases.

With authority supplied freely and instantaneously, the same local-diagnostic argument removes the authorization slot and fee: `τ_S=2`, `C_S=2c+d+x`; add `L` slots and `K+Lc` for the cold route. The implementation checks this variant as well. The analytic helper explicitly refuses full-information, fixed-bit, and alternative-provider configurations, whose routes differ.

## 4. Exact game over all allowed apparatus decisions

The unrestricted controller can keep, suspend, initiate a proactive rebuild, continue or cancel it, rebuild during a fault, and retain or release the apparatus after repair. The alternative-provider control also permits paid external diagnosis. No comparison assumes the controller must preserve the incumbent.

For each fixed `B` the graph is finite. It records cash `0,…,B`, clipped onset clock, finite repair phase and deadline age, finite rebuild delay, and the fixed-bit memory flag where relevant. All initial credits and both initial apparatus states are included in one solved graph.

Let `W` be the greatest set such that, for every state in `W` and every admitted **observable** environment event, at least one affordable controller action has its successor in `W` and does not miss a deadline. This is the greatest fixed point of the safety predecessor, computed by eliminating states whose environment can force all controller replies outside the current set.

**Why this certifies indefinite recurrent repair.** Select one surviving action for each state and event. The exported finite controller keeps the state in `W` forever. Since an unfinished fault violates safety after `D` slots, the controller must finish every onset within that deadline; it cannot preserve safety by waiting forever. Quiet states continue the specified operating process. This is a proof by a finite inductive invariant.

For every eliminated state, the program also exports an environment event for which **every** controller reply either violates a constraint immediately or enters a strictly smaller losing rank. That rank decreases to a violation in finitely many steps. It proves the negative side and the minimum initial credits, rather than merely reporting that one searched controller failed.

The environment can choose onset times adaptively from the current state subject to the spacing rule. The solver does not enumerate only stationary disturbance patterns. There is no stochastic almost-sure inference or simulation extrapolation.

The controller's selected action within the winning set is a witness, not an optimized long-run burden policy. A lower current fee is used only to break ties. Capacity and burden should not be conflated.

## 5. Discriminating results

Unless a row says otherwise, `B=24`, `c=d=a=x=1`, `y=5` (so `p=4`), `m=1`, `K=2`, `L=2`, `Δ=5`, `D=5`. Each number is the exact least initial credit among **all allowed policies** for the stated initial apparatus. “None” means every initial credit through the declared cap loses; where an analytic argument proves failure for every finite cap, that is stated separately.

| Case | Ready start | Cold start | Mechanism isolated |
|---|---:|---:|---|
| Base: expensive delayed restart | 6 | 16 | Readiness prevents recurrent zero-earning repair cycles |
| Expensive standby: `p=3,m=4,K=1,L=1,Δ=7,D=4` | 6 | 8 | Suspension and restart succeed; forced standby fails in a long quiet interval |
| Free instantaneous rebuilding: `K=L=0` | 6 | 6 | Standby is unnecessary for feasibility |
| No faults admitted | 0 | 0 | No inquiry is required; suspension avoids its expense |
| Current cause supplied on each onset | 4 | 4 | Diagnostic apparatus is unnecessary; authorization and execution remain paid |
| Constant cause with retained bit, before first diagnosis | 6 | 14 | One-time discovery has a transient financing burden |
| Same constant-cause control, bit already known | 4 | 4 | Recurrent diagnostic expense is informationally redundant |
| Authorization supplied | 4 | 9 | Discovery and physical implementation remain; one gate and slot disappear |
| Alternative diagnostic provider, surcharge 2 | 6 | 8 | A paid substitute supports the function without maintaining the local apparatus |
| More frequent faults: `Δ=4` | None | None | The earlier disturbance-class promise matters |
| Healthy feedstock/output removed: `y=0` | None | None | No perpetual support is created by the repair label |
| Longer spacing: `Δ=9` | 6 | 10 | Sufficient healthy earning time makes cold rebuilding feasible |

### Base: a bridge reserve is larger than either repair bill

With ready apparatus, a fault costs six and lasts three slots. The two healthy slots before the next earliest onset each accumulate `p−m=3`, restoring the six. Thus reserve six and storage cap six suffice indefinitely for standby.

Cold rebuilding costs ten and lasts five slots. In the base spacing class, an earliest next fault begins immediately on completion. A pure suspend-and-rebuild route therefore pays ten repeatedly with no healthy output and fails with **every finite reserve**.

An adaptive cold-start controller can rebuild once and then keep the apparatus. Its first repair costs ten, followed immediately by a ready repair costing six. No healthy receipt lies between them. Hence **sixteen** initial units are necessary, independently of the solver. Sixteen are sufficient: after these two repairs, the apparatus is ready and the ordinary two-slot healthy gap restores six for each later ready repair. A longer quiet interval adds nonnegative support. This is a startup bridge requirement, not a steady-state repair cost.

This comparison treats initial assets honestly: a ready apparatus is an endowed noncash asset. Ready and cold columns are not said to be matched total wealth. Within each column all compared policies receive the same starting state and cash. Proactive building and its actual fee and delay are part of the game.

### Opposite regime: standby is not always the solution

For `p=3,m=4,K=1,L=1,Δ=7,D=4`, forced standby spends one more unit than it earns on every quiet slot, so an arbitrarily long quiet interval defeats it for any finite reserve.

A suspended episode costs eight, lasts four slots, and is followed by at least three healthy earning slots. Those yield nine, so suspended repair is indefinitely feasible with cold initial credit eight and cap at least eight. From an initially ready state, credit six suffices: an immediate first fault uses the endowed apparatus; subsequent operation can suspend and rebuild. If the first slot is quiet and the on-demand controller suspends, its three units of net output already raise credit six to at least the eight needed for a cold fault. These are distinct histories that the same policy must handle.

**Storage and initial credit are not interchangeable.** The full game verifies:

| Regime and storage cap | Least ready credit | Least cold credit |
|---|---:|---:|
| Base, `B=6` | 6 | None |
| Base, `B=15` | 6 | None |
| Base, `B=16` | 6 | 16 |
| Expensive standby, `B=6` | None | None |
| Expensive standby, `B=7` | None | None |
| Expensive standby, `B=8` | 6 | 8 |

The last three rows include proactive rebuilding and every other allowed apparatus policy, not merely a comparison of two fixed schedules.

### Controls that distinguish mechanisms

**Known cause and fixed cause differ initially.** When every new cause is supplied, only authorization and implementation remain, costing four over two slots. With a constant initially unknown cause, the first diagnosis still costs money and time. Thereafter a free retained bit makes the recurrent problem identical to the known-cause version for its relevant phase. The cold initial threshold fourteen equals the ten-unit initial cold repair plus an immediately following four-unit informed repair. The diagnostic apparatus can then be discarded, while per-episode authority and execution remain necessary. Thus the control does not falsely erase all corrective needs when information is free.

**A substitute can be better than rebuilding the incumbent.** The external diagnostic surcharge makes an apparatus-free episode cost eight over three slots. Two healthy slots at net four replace that cost exactly. Hence cold initial credit eight works without rebuilding local apparatus. The forced-standby class needs nine from cold in this control because it spends some recovery income establishing and maintaining the local apparatus; preserving that particular provider is not the protected objective.

**The spacing violation is substantive.** At `Δ=4`, each fault requires at least three zero-output slots and six support units. There is at most one healthy earning slot before the next earliest onset, worth at most four before any apparatus fees. Thus every cycle loses at least two units even under this optimistic bound. No finite reserve can sustain the specified service against that onset pattern; this strengthens the numerical cap-24 negative result.

**The external boundary is indispensable.** With `y=0`, every slot consumes at least one and receives nothing. Finite initial reserve fails regardless of the policy. The positive results assume a reliable, indefinitely supplied external feedstock that the healthy productive function converts to the stated support output. The alternative-provider control similarly assumes that paid diagnostic service remains available. Neither model closes the entire physical economy.

**No hazard is not an ineffective-repair case.** If no fault is admitted, there is no recurring correction duty. A controller can suspend the apparatus, earn `p`, and perform no investigation. Forced standby is also feasible in the base prices but pays a needless unit each quiet slot. The model therefore does not make inquiry permanent by definition.

## 6. Saved frontier, controllers, and verification

The [checker](verification/check_recurrent_repair.py) uses only the Python standard library. Running it regenerates:

- [Complete results](verification/recurrent-repair-results.json), including exact initial-credit minima, finite-game counts, losing ranks, and illustrative traces;
- [Route frontier CSV](verification/route-frontier.csv), containing every pair `Δ=3,…,10` and `L=0,…,4` at the base costs;
- [Winning controllers and negative certificates](verification/witnesses/standby_advantage-all.json), with analogous files for every unrestricted selected case and each storage-cap check.

The CSV reports duration, episode cost, minimum earning gap, net cycle balance, and feasible minimum credit for each prescribed route. All **40 grid points** were checked against separate exact finite games for both prescribed routes. At the base prices, ready standby requires `Δ≥5`; cold on-demand repair requires `Δ≥5,7,8` for `L=0,1,2`, respectively. For `L≥3`, the cold route misses the five-slot deadline regardless of reserve. These are route-specific frontiers, not claims about every possible interface.

Eleven selected configurations were each solved under unrestricted, forced-standby, and on-demand policies, giving **33 selected games**. Six further unrestricted games distinguish storage cap from initial credit. For all these games, the program verifies the greatest-fixed-point equation on every generated state. A second descending-set implementation independently reaches the same fixed point from bounded safety sets. The 33 selected games also receive 110 un-memoized bounded policy-tree comparisons each (credits zero through ten, both initial assets, and horizons zero through four), totaling **3,630 comparisons**. These implementations share the transition table, so this cross-check is not independent validation of the modeling assumptions.

Every affordable generated transition is checked for budget conservation. Winning certificate rows specify one allowed action for each possible observed event and a successor within the invariant. Losing rows specify a permitted environment event and strictly decreasing rank for **every** controller reply. Forty-slot example traces are included only for inspecting chronology; no infinite result is inferred from them. All assertions passed.

The selected controller's tie break does not minimize burden over all disturbance histories. A burden-optimal tradeoff would require another stated ordering or objective and a further game optimization. This study reports feasibility, timing, initial credit, cap, and explicit fees separately rather than quietly substituting one scalar welfare measure.

## 7. What has and has not been established

The completed result is an exact conditional separation: money, maintained diagnostic access, rebuild latency, inherited information, and outside provider access can substitute for one another in some regions and fail to substitute in others. A favorable recurrent balance is insufficient without a payable initial bridge and deadline compatibility. Conversely, paying indefinitely to keep a particular diagnostic apparatus can be worse than suspending it or replacing its service.

The proofs use established accounting and finite safety-game reasoning. No mathematical novelty is claimed. The positive recurrence statement is relative to an explicitly bounded disturbance class and an external feedstock assumption. The protected duty—keep operating when healthy and repair every admitted fault by `D`—is supplied; the model does not determine whether this duty is ethical, whether the outputs are beneficial, or who should bear the costs.

The next substantive extension would price or restrict retained evidence and institutional access while preserving this verified chronology. It should keep the fresh-cause and constant-cause controls, because otherwise recurrent inquiry may be made artificially necessary. That extension is not included in the present solved model.
