# Reconstruction leaves differentiated requirements for continuation

6 October 2026. AI-authored analysis under the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). Named connection: **completion of one transformation → requirements that remain for further activity**. This characterizes the material dependency a learner would have to acquire and use. It does not install another controller or claim that the relation has already become learned understanding.

The [earlier restoration result](NONDUAL-APPLICABILITY-MECHANISM.md) already proves that actual repair changes its own applicability, and that consumption can reopen capture without undoing the repair. The [inquiry-completion study](INQUIRY-COMPLETION-INTEGRATION.md) separately demonstrates acquired knowledge of completion governing further inquiry in its own lineage. Its endpoint has no autonomous post-return maintenance law. Arbitrarily scheduling additional retention calls would add an undertaking, rather than derive it. The present continuation returns to the original material process, where capture, copying, damage and repair have explicit effects on one another's conditions.

## The unchanged material question

Use the full sixteen-event [FormedSelection law](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean). A configuration contains free A/H parts, one resident, an intact/damaged site, a one-unit local store, common fuel and incident source. Copying through the local route consumes local support; bulk copying consumes common fuel. Capture transfers source into the local store. Neither capture nor any other event replenishes common fuel. These are differentiated relations in one process, not interchangeable labels for a scalar resource.

Fix a valid starting state after independently occurring wear, with an active resident. Write:

- `A` and `H` for total A and H counts, including the resident of the relevant type;
- `F` for common fuel, `E` for incident source, and `L` for the local-store bit, zero or one;
- `n` for the required increase in A relative to this start, with `0 ≤ n ≤ M−population(start)`.

The terminal contract is `A(end) ≥ A(start)+n`, `H(end)=H(start)`, and an active resident at the end. It does **not** additionally demand restoration of the starting intact/local-store values. It represents replacement of a specified prior A loss, rather than a reward assigned to any increase in population. The baseline loss and role of reconstruction remain supplied by the declared finite undertaking.

All sixteen event kinds remain available in the reachability question. Wear and damage are not made desirable operations by calling them inquiry. A controller's authority to select events and an independently imposed turnover schedule are additional distinctions, not fields already present in this Lean law.

## Exact least common-support requirement

For the declared reconstruction contract, the minimum initial common fuel is

\[
F_{\min}^{\mathrm{intact}}=\max(n-L-E,0),
\]

and, if the starting site is damaged,

\[
F_{\min}^{\mathrm{damaged}}
=\min\left(\max(n-L,0),\;1+\max(n-L-E,0)\right).
\]

The other starting coordinates are held fixed, with enough precursor capacity as above. These are exact finite reachability statements. They are not stochastic success probabilities, frequency advantages, universal energy prices, or a claim that one route is always preferable.

### Necessity across all sixteen events

Let `G` count `formA`, `localCopyA` and `bulkCopyA`, and `R` count repairs in an arbitrary admitted finite history. No other event increases total A. Association moves an A from the free pool into the resident without increasing that total; wear can reduce it. Hence

`A(end) ≤ A(start)+G`, so the target requires `n ≤ G`.

Every counted A-growth event expends one energy unit, as does every repair. These event sets are disjoint. The existing energy ledger therefore gives

\[
n+R\le G+R\le\text{expenditure}\le F+L+E.
\]

This immediately yields the intact lower bound. It does not assume that the route used only the favorable events in a proposed construction; extra formation, association, H copying, leaks, wear and damage are included and cannot defeat it.

If no capture occurs, source remains unchanged in the exact source balance. Source cannot fund expenditure by an unrepresented transfer, so

\[
n\le F+L.
\]

If a capture occurs from a damaged start, at least one earlier repair must have occurred. Capture requires an intact site, and repair is the only event that changes damaged to intact. Repair consumes common fuel, whose amount never increases. Consequently `F≥1` and

\[
n+1\le F+L+E.
\]

Together these imply `F ≥ 1+max(n−L−E,0)`. Every actual history is either a no-capture history or a history containing capture, so it must meet at least the smaller of those two thresholds. This proves the damaged lower bound without suppressing bulk copying or alternative material events.

The [new Lean module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeReconstructionRequirement.lean) formalizes this general necessary bound over the unchanged sixteen-event trace law. Its necessity theorem does not require the extra initial-active or endpoint-H-preservation conditions; these enter the constructive sufficiency argument below.

### Constructive sufficiency

An active resident supplies the template for every local A copy and ensures a nonzero total A count for bulk copying. First use an initially available local unit if `n>0` and `L=1`. With an intact site, repeat `capture → localCopyA` for as many remaining copies as the source can supply, then perform any remaining copies through `bulkCopyA`.

The local route provides at most `L+E` copies. Each remaining copy consumes exactly one common unit, so the required common reserve is `max(n−L−E,0)`. Every intermediate A count is at most `A(start)+n`; H and the resident stay unchanged. The precursor bound therefore supplies every copy's capacity guard. Capture has an empty local store because the preceding copy consumed its unit. No hidden source refill or common transfer is used.

From a damaged start, there are two constructive options. Use the initial local unit, then bulk-copy the remainder without repairing; this requires `max(n−L,0)` common fuel and may leave the site damaged. The unchanged local-copy guard requires an active resident, local support and precursor capacity, not an intact site. Alternatively spend one common unit on repair and follow the intact construction, requiring `1+max(n−L−E,0)`. Select an affordable option at the smaller threshold. The case `n=0` admits the empty history and requires no fuel.

These constructions prove sufficiency for every admissible `n` and complete the mathematical characterization. They preserve the full native alternatives rather than proving a cost only for a prescribed capture-first protocol. The general sufficiency argument is given here in mathematics; the current Lean addition proves the all-trace necessary bound and the concrete continuation contrast below, rather than a fully formalized general iff.

## Same completed reconstruction, same energy, different further activity

The existing 94-event formation ancestor reaches

`(freeA,freeH,resident,intact,local,F,E)=(38,39,active,true,true,293,216)`

at material capacity78. Its repaired history remains a historical fact. A specified continuation of 292 common leaks, one local leak and one externally imposed free-A wear reaches

`s=(37,39,active,true,false,1,216)`.

The leak and wear events are real expenditure and turnover in this alternative history. They are not a reset of the original ancestor or an intervention the learner is instructed to cause. This is a possible finite continuation under the law; the Lean event system supplies no rates or likelihood for it.

The immediate target is to replace the lost A. Both routes accomplish it:

| Route from `s` | Endpoint | Total energy |
|---|---|---:|
| `capture → localCopyA` | `(38,39,active,true,false,1,215)` | 216 |
| `bulkCopyA` | `(38,39,active,true,false,0,216)` | 216 |

The endpoints have the same A/H counts, resident, intact site, empty local store and total energy. Their immediate reconstruction is equally real. Neither undoes the ancestor's repair. The difference is the distribution of the remaining energy between common fuel and incident source.

Now impose the same later damage event in both histories. From the local route's endpoint, `repair` is enabled and returns the site to intact, consuming its final common unit. From the bulk route's endpoint, repair is disabled. Moreover, no arbitrary sequence of the sixteen native events can restore that repair capacity: common fuel starts at zero and never increases under this law. Capture can replenish only local fuel, and after damage it is itself unavailable until repair. A source unit cannot silently change compartments.

The module proves both reconstruction traces, equality of their aggregate energy and other listed coordinates, the successful damage/repair suffix, and permanent inability to enable repair from the bulk endpoint. The full 94-event ancestor is the existing established trace; the new root-owned finite check binds the longer leak/wear continuation to that original source. The new small Lean module does not reprove the whole ancestral assembly chain.

This is an exact failure of aggregate energy as an adequate continuation abstraction. It is not a failure of energy conservation. If the undertaking includes responding to the stated later damage, the local route preserves a required condition that the bulk route consumes. If the undertaking only replaces the present A loss, both remain adequate. The broader scope must be declared independently; the later requirement is not inferred merely because one selected route happens to preserve it.

## What this supplies for learning, and what it does not

The [support-loss teacher](../../2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-TO-LEARNING-MATH.md#5-exact-support-loss-teacher-and-a-censoring-counterexample) already derives an operational learning target from the actual prerequisites of another operation/update round. The [material recorder](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/README.md) already forms records from actual parts under its separate observation kernel. The present result identifies a differentiated dependence that such an acquired model must preserve: equal total support and completed current work need not imply equal future action possibilities.

A new physical learning join would have to authenticate native capture/copy effects, retain the relevant common/local/source distinctions, and let those acquired relations govern an actual continuation. It must account for its own parts and operations in this same material configuration. Memory assembled from free A/H parts occupies capacity; those parts cannot simultaneously count as available copying precursor. The existing generic archive interface can derive a payload from an authenticated native successor, but its contact, encoding, assembly and later reading still need a specific realization here.

This study constructs neither that learner nor an autonomous subgoal planner. It also does not derive the reconstruction undertaking, a mandate to preserve this organization at others' expense, universal beneficial direction, or ethical worth from material copying. It gives an exact requirement relation and a substantive rival-route test before any such implementation is introduced. The next genuine acquisition claim must demonstrate that the learner obtains and uses this relation, rather than being handed the correct capture-first sequence or a global success score.

## Verification scope

The [independent review](CONTINUING-DEPENDENCY-REVIEW.md) accepts the mathematical characterization, finite reconstruction and scoped Lean addition. It retains the separate obligation to construct an acquired dependency model and its effective use.

The [isolated Lean verification](development/continuing-dependency/VERIFICATION.json) passes all twenty new theorem audits under Lean 4.29.1. Seven depend on `propext`; thirteen depend on `propext` and `Quot.sound`. There are no custom axioms, proof placeholders or `Classical.choice` dependencies in these twenty reports. The module's source hash is `5c86c940d1eb408a310cb2cedb4c7332ad130d7544a60508e1fc7fc75c6d92b0`; the unchanged FormedSelection source hash is `a7bdce34f00ab07edd8b234eb1a7abd435a0cfe8034257ff3928209d0966bf37`. This is not an empty-dependency proof chain, and the stronger no-axioms objective remains unmet here.

The first unsuccessful draft, repaired source, build logs and hash-bound receipts are preserved by [the isolated build procedure](development/continuing-dependency/build.py). Its [receipt verifier](development/continuing-dependency/verify.py) checks every declared theorem audit and the preserved attempt bindings without rerunning the scientific model.

The [new finite study](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/continuing-dependency/results.json) checks 4,800 finite configurations over their complete native reachable graphs: 34,744 states and 217,030 edges. It records 4,096 constructive witnesses comprising 11,584 events and the explicit 94-event ancestor continuation. The formula has no mismatch in that grid. The [independent reconstruction](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/continuing-dependency/independent-check.json) passes all these cases and witnesses without importing the producer or native model. It also checks the blocked continuation graph and binds nine source files. These finite checks complement the general mathematical argument; they are neither empirical observations nor an installed learner/planner.

The conditional physical law and the supplied finite undertaking remain explanatory inputs regardless of the proof-system dependency audit. A reachable counterexample below the threshold, a failure of the stated constructive route at or above it, or a native event replenishing common fuel would revise the result. An actual acquired controller would address a further connection rather than retroactively become part of this proof.
