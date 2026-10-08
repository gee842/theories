# Formed capacity and continued structural formation

**Maintenance baseline，2026-10-08。** [MaintenanceBaseline.lean](MaintenanceBaseline.lean) checks an intervention-dependent target error and genuine completion before retirement: 4 new theorems / 13 audits, with 21 inherited theorems / 55 audits separate. [Passing receipt](maintenance-baseline-verification.json); [proof and scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MAINTENANCE-BASELINE-PROOF.md). Retirement disables actual routes; a recomputed empty target is distinct from delivered protection. Completed records concern one delivery, not continuing capacity.

**Wisdom goal grounds, 8 October 2026.** [WisdomGoalGrounds.lean](WisdomGoalGrounds.lean) imports the unchanged formed-goal model and checks opposed protection frontiers with identical attainment profiles, a necessary representation distinction, and an adequate fixed comparison rule. Run `python3 check_wisdom_goal_grounds.py`; [receipt](wisdom-goal-grounds-verification.json) records seven new theorems / eleven audits and 93 inherited theorems / 165 audits. New proof dependencies are `propext` and `Quot.sound`; inherited imports also use `Classical.choice`. No universal wisdom, normative-premise proof or permission to implement is inferred.

**Observable continuation，2026-10-08。** [ObservableContinuation.lean](ObservableContinuation.lean) joins selected actual execution to an explicit support-effect correspondence and the existing chance bound: 4 new theorems / 24 declaration audits, with 17 imported theorems / 31 audits separate. [Actual receipt](observable-continuation-verification.json); [proof and scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/OBSERVABLE-CONTINUATION-PROOF.md). Funded sensing and real parallel support have checked outcomes; old maintenance remains executable in the limited-budget control. This is single-delivery support, not a proof of uninterrupted supply.

**Actual support to chance, 8 October 2026.** [ChanceAdequacy.lean](ChanceAdequacy.lean) and [checked receipt](chance-adequacy-verification.json) add 8 theorems/14 declaration audits, Std-only with 11 retained artifacts. Pointwise task coverage gives a common-law mass bound; all-natural-weight preservation characterizes coverage, while one actual law need not. [Proof scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CHANCE-ADEQUACY-PROOF.md).

**Initial-chance implementation diagnostic, 8 October 2026.** [ChanceGrounding.lean](ChanceGrounding.lean) and [actual receipt](chance-grounding-verification.json) add 4 theorems/10 declaration audits, importing only Std. Positive tickets plus headcount maximization have no maximum in the unbounded ticket domain; fixed N≥2 selects (N−1,1), without grounding fairness. [Scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CHANCE-GROUNDING-PROOF.md).

**Crossed claims and joint opportunities, 8 October 2026.** [CrossedClaims.lean](CrossedClaims.lean) and [retained verification](crossed-claims-verification.json) add 8 theorems/23 declaration audits: coupled protection and floor preservation, an equality control and a specific unsatisfied-anchor filter. Thirty practical theorems/46 audits and one example are separate. [Scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CROSSED-CLAIMS-PROOF.md): finite rational tickets; no proof of ethical LR, justified floors or actual route feasibility.

**Joint unequal-loss comparison, 8 October 2026.** [UnequalBasicLosses.lean](UnequalBasicLosses.lean), [checker](check_unequal_basic_losses.py) and [receipt](unequal-basic-losses-verification.json): 14 new theorems/23 declaration audits, with 30 inherited PracticalJudgment theorems/46 audits separate. Two application controls are not new theorem counts. The cumulative diagnostic, crossing reversal and representation controls do not derive LC's ethical warrant or decisive allocation. [Scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/UNEQUAL-BASIC-LOSSES-PROOF.md).

**Status, 7 October 2026:** [FormativeCapacity.lean](FormativeCapacity.lean) passes Lean 4.29.1. The current [proof receipt](verification.json) records 38 new theorems and dependency audits of all 75 explicit declarations; its reused [GenerativeCore](../../GenerativeCore.lean) contributes 23 theorems / 28 declaration audits. The new module's only recorded axioms are Lean's `propext` and `Quot.sound`; no `Classical.choice`, custom axioms, proof placeholders, unsafe declarations, or unchecked proof evaluators occur in the checked dependency sets/source.

This supplies one precise distinction needed when interpreting Ren's 生生不息 direction: **arbitrarily large completed finite formations across different histories do not by themselves yield continued completed formation along one history.** It also makes the next usable formation condition an actual position in the formed tree. It proves no ethical ranking. The broader integration and rival assessment belong to the [current research argument](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md).

## Represented unfolding and supplied law

The fixed feed, its consumed prefix, stored parts/work, and formed tree jointly describe the represented process. There is no primitive agent or independent environment. `Feed : Nat → Bool` specifies successive source lots; `cursor` identifies the next unconsumed lot. The source comment's “schedule” means this **indexed availability**, not availability at a clock time. A false next entry blocks transfer; this model has no bypass operation. Source existence and accessibility are supplied relations, not an explanation of how the source arose.

The initial tree is one supplied input socket, with zero raw parts, zero stored work, cursor zero, and the gathering phase. A tree has atoms, sockets, and binary branches. The only accessible socket follows the rightmost branch path; `socketAddress` returns its address length. The transition law uses that structural socket, not the phase alone, to allow input.

| Event | Enabling condition | Actual change and cost |
|---|---|---|
| `capture` | Accessible socket and available next lot | Transfers two raw parts and one work unit; advances the source cursor once. |
| `commissionClosed` | Gathering phase and at least one work unit | Converts the terminal socket into an ordinary atom, spends one work unit, enters building. |
| `commissionOpen` | Gathering phase and at least one work unit | Retains the socket, spends one work unit, enters building. |
| `build` | Building phase, at least two raw parts and one work unit | Incorporates the old terminal as a branch and forms an atom plus a replacement terminal; spends two raw parts and one work unit. |

For the open route, the replacement terminal is a newly formed socket at the next deeper address. The former terminal has become a branch and no longer serves as that socket. The fixed recipe permits reconstruction; the model does not discover the recipe. For the closed route the new terminal remains an atom, so later builds cannot restore input. Both routes have the same initial configuration, source, commissioning cost, and build cost.

Structural material is `parts(tree) + raw`. Every actual capture adds exactly two to this local total; all other transitions conserve it. Work is a separate ledger quantity, gained once per captured lot and spent once per commission/build. No claim about chemistry, energy units, thermodynamic feasibility, or the physical cost of an arbitrarily deep manipulation follows from these toy accounting units. Each transition is one discrete event; elapsed physical time is unmodeled.

## Checked results

| Theorem(s) | Exact contribution |
|---|---|
| `finite_branching` | Every state's successors are exactly the enabled successors drawn from four event constructors. No arbitrary input amount or unbounded branching is hidden in one step. |
| `step_accounts`, `trace_accounts` | Material, work, and source-cursor accounting hold for every lawful step and finite trace. |
| `build_reconstructs_next_interface` | An actual build following a socket at address length `a` leaves its replacement at `a+1`, adds two tree parts, and pays both specified costs. |
| `arbitrary_finite_terminal_depth` | For every natural `n`, one finite history captures `n+1` lots, commissions closed, and completes `n` builds. Its terminal tree has depth `n`, two raw parts remain, work is zero, and no event is enabled. The large initial stock is not supplied for free. |
| `closed_no_infinite` | Starting without an accessible socket, no infinite lawful history exists: each available transition spends one unit of a finite stored work quantity. This statement covers arbitrary feeds. |
| `one_shot_infinite_only_gathers` | Any infinite history from the initial configuration that never commissions open consists entirely of capture events and retains the initial socket tree. Thus the arbitrary terminal depths are achieved in separate finite histories; they cannot be joined into a one-shot history with infinitely many builds. |
| `continuing_formation_run`, `completed_formations_recur` | Under the constant available feed, one explicit infinite history commissions open and alternates capture/build; build events occur at every time `2n+3`. |
| `actual_growth_milestones`, `actual_depth_unbounded` | In that same history, at time `2n+2` the formed tree has depth `n`, its socket is at address `n`, and exactly `n+1` lots have entered. Depth exceeds every finite bound along this one history. |
| `infinite_gathering_without_formation` | The same constant feed permits an infinite capture-only history with tree depth zero. Feasible continued formation is not inevitable execution. Accumulation/preparation still occurs; the theorem is specifically about absence of the selected tree builds. |
| `finite_feed_trace_bound` | With only the first `L` input lots available, every finite trace from the initial state has cursor at most `L`, material at most `1+2L`, and total work spent at most `L`. |

The arithmetic clock expressions describe actual states/events in the explicitly checked infinite run. They do not infer an infinite run merely from a list of individually attainable large outputs. All states at finite times contain finite trees and finite stores.

## Increment over existing work

[RenewalExamples](../../conditional/RenewalExamples.lean) already distinguishes repeated renewal from depletion and compares arbitrarily large finite resource provision with continuation. [ContinuationRenewal](../ContinuationRenewal.lean) addresses general necessity under a well-founded progress relation. This module adds a concrete four-event instance with a growing tree, a structural input position, source transfer, paid construction, arbitrary finite terminal depth, and an explicit continuing formation history. It does not replace those general results.

[RegenerativeDiversity](../RegenerativeDiversity.lean) already proves coherent finite circuit-growth cycles with retained functionally distinct taps, paid reconstruction, and a nonregenerative depth bound. Here the increment is the **arbitrary-depth terminal alternative versus one compatible infinite history of completed builds**, while keeping source transfer finite per step and rebuilding the next accessible terminal within the actual tree. Conversely, this module proves no tap distinguishability or increasing functional diversity. Its binary comb repeats one supplied grammar; unbounded tree depth alone is not unbounded semantic variety, life, new purposes, new recipes, or worthwhile complexity.

The ethical question this tests is whether “can attain ever larger finished formations” suffices to express the proposed ongoing direction. The instance distinguishes those claims and locates a recurring enabling condition. Whether this capability constitutes an ethically favorable realization, and how it compares with terminal fulfillment, harm, closure, plural formation, or other scope interpretations of 生, requires the substantive whole-process argument. No `Good`, utility, ethical priority, normative obligation, or independent subject is inserted in the Lean model.

## Reproduce and inspect

From the repository root, using the already installed toolchain:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check.py
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_correspondence.py
```

[check.py](check.py) copies exact core/model bytes into a fresh temporary directory, builds their `.olean` files, then kernel-checks generated `#print axioms` audits for every explicit declaration. Its retained runs include source snapshots, checker bytes, version/build/audit logs, hashes, and receipts. It scans the supported source syntax for proof escapes and records exact standard-axiom dependencies. The declaration audit does not separately enumerate all generated constructors, recursors, projections, or deriving declarations; dependencies reachable from the audited declarations are included by Lean. The current receipt replaces earlier receipts only as the latest status; earlier snapshots remain preserved under `checks/`.

The independent [correspondence checker](check_correspondence.py), supplied by the integrating researcher, represents nodes, child edges, and the socket position explicitly, then compares its finite replay with [Lean samples](CorrespondenceSamples.lean). Its [receipt](correspondence-verification.json) binds the same model hash and records 174 matched state records across 54 frontiers, terminal depths 0–12, and renewal milestones 0–64. This is a finite implementation/correspondence check, not an extra theorem or empirical validation. The two receipts are complementary; the arbitrary-natural and infinite-history claims rest on the Lean proofs.

## Continuation: formed coupling and jointly effective formation routes

**Second checked model, 7 October 2026:** [FormationRoutes.lean](FormationRoutes.lean) passes Lean 4.29.1 with **35 new theorems and 79 explicit declaration audits**. The [separate proof receipt](routes-verification.json) records only `propext` and `Quot.sound`, without `Classical.choice`, custom axioms or proof placeholders. The first model and its receipts retain their original scope.

The new inference concerns **joint realizability under common support**. A manual route can form either `L=((a,b),c)` or `R=(a,(b,c))` separately within three work units. Forming a reusable coupling permits both to be completed in one history within the same total budget, including the coupling's construction. This goes beyond counting individually possible products or increasing the depth of a single fixed tree.

### Parts, connections, histories and law

The state includes an optional finite source lot, unassembled parts, remaining/spent work, a coupling bar, a pending partial assembly, and the list of completed assemblies. Source material/work remain in the whole ledger before transfer. Two supplied assembly ports are included in the material total. `Bar.span p q` is an actual placement with two endpoints; only unequal endpoints span the two ports. An absent, loose, or same-port bar does not enable synchronized formation.

Each tree's atoms have fixed roles `a,b,c`. The two products differ at common addressed positions: inspecting root-left-left reaches `a` in `L` and finds no atom at that address in `R`. Tree joints represent binding relationships; raw material counts the leaf atoms. **This differs from the earlier socket tree's node-count convention** and is not a silent common material interpretation or a claim of chemical equivalence.

| Operation | Effect | Work and material |
|---|---|---|
| `receive` | Transfers the one remaining source lot into current stores; consumes the lot's availability. | No new material/work is created in the whole ledger. |
| `attach` | Forms a bar spanning the two ports from absence. | One raw part becomes the bar; one work unit is spent. |
| `repair` | Repositions the existing loose bar across the ports. | No added material; one work unit is spent. |
| `startAB` / `startBC` | Makes the corresponding dyad in the sole pending-assembly position. | Two raw parts; one work unit. Requires no existing pending assembly. |
| `finishLeft` / `finishRight` | Adds the third atom to the matching dyad and moves the completed tree into the product list. | One raw part; one work unit. The intermediate is consumed, never counted twice. |
| `syncLeft` / `syncRight` | Forms either complete tree while the reusable bar spans the ports. | Three raw parts; one work unit. No pending assembly; bar remains present. |

The two-joints-in-one-operation contact/actuation law is **supplied**. These units represent assembly work in this model, not measured physical energy or a derivation of efficiency from first principles. Fixed ports, atom-role recipes, and the two product forms are also supplied. No observed catalyst, tool, organism, intelligence, or ethical preference is identified with this model merely by analogy.

### Checked comparison and controls

- `step_accounts` and `trace_accounts` conserve the whole material count and `source work + remaining work + spent work`. `finite_branching` lists the exact successors among nine operation constructors.
- `formed_joint_history` constructs a history for **any finite list of the two forms**. For `k` products, the source contains `3k+1` parts and `k+1` work units. One part and one work unit form the bar; every subsequent product uses three parts and one work unit. `formed_joint_costs` retains all `k` products and the bar, with zero remaining work/raw material and exactly `k+1` work spent.
- `bypass_output_bound` proves that **every trace that bypasses the synchronized operations** has `2 × completed products ≤ initial work`. The bypass control still allows source transfer, manual interleavings, and even spending on attaching/repairing an unused bar. Such operations cannot evade the bound. `disconnected_step_is_bypass` connects this control to actual absence of a spanning relation.
- `multiple_completions_exceed_bypass` establishes the strict completion advantage for `k≥2` under the common `k+1` work budget. The source parts, setup cost and persistent bar remain counted. This is a longer-history result, not an assertion of an advantage at every step.
- `either_form_without_coupling` proves that either `L` or `R` alone is manually achievable from the source of seven parts and three work units. `both_forms_in_one_history` constructs `receive → attach → L → R` from that same source. `both_forms_unreachable_by_bypass` rules out completing that pair on every bypass trace. Thus the gain is joint completion, while the two individually available product kinds were already present.
- `disconnection_preserves_support` compares a connected bar with the same bar stored loose, retaining material, raw stock, remaining/spent work and products. At the matched state of three raw parts and one remaining work unit, `matched_connected_can_finish` completes either tree; `matched_disconnected_cannot_finish` proves that **no lawful continuation** completes any product. Repair is allowed in this latter comparison: `repair_uses_last_work` shows it consumes the last work unit without producing a tree.
- `connected_underfunded_cannot_finish` retains the connection but sets remaining work to zero. `redundant_for_single_target_with_two_work` gives the disconnected state two work units and completes either form manually. These are separately labeled budget controls, not members of the matched one-work comparison.

`disconnect` is a matched configuration intervention, **not a lawful zero-cost dismantling event**. Its support-preservation theorem assumes an existing spanning bar; it does not turn absence into a free bar. The intervention comparison retains historical spent work but does not derive a physical dismantling cost. The full-history pair comparison independently includes actual `attach` formation from an absent bar.

No theorem claims that coupling enlarges the unrestricted set of all future attainable states, the number of individually achievable product kinds, biological diversity, or arbitrary innovation. The bounded work resource and supplied actuation law are essential. The positive contribution to the ethical inquiry is a concrete realization of **a formed common relation converting competing formation routes into jointly realizable formations under the same finite support**. Whether and how that realization has ethical significance remains the substantive whole-process question; no `Good` predicate or prior favorable-product filter is introduced.

Run the additional checks from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_routes.py
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_routes_correspondence.py
```

[check_routes.py](check_routes.py) snapshots the model, reused core, its own code and the reused scanner from `check.py`; fresh compilation and complete explicit-declaration dependency audits are retained under `route-checks/`. The integrating researcher's [independent route replay](check_routes_correspondence.py) and [Lean samples](RoutesCorrespondenceSamples.lean) passed **1,109 matched state records**, covering 108 source-budget/process families and 16 post-intervention families across 650 frontiers. The [route correspondence receipt](routes-correspondence-verification.json) binds the same model bytes as the proof receipt. Neither finite replay nor the constructive proofs establish empirical or ethical correspondence.

## Continuation: actual release and formation of a third structure

**Third checked model, 7 October 2026:** [ReconfigurableRoutes.lean](ReconfigurableRoutes.lean) passes fresh Lean 4.29.1 compilation with **45 new theorems and 66 explicit declaration audits**. The [reconfiguration proof receipt](reconfiguration-verification.json) also records fresh compilation and audits of the unchanged `GenerativeCore` and `FormationRoutes` dependencies. Only `propext` and `Quot.sound` occur in the audited dependency union; no custom axiom, proof placeholder, `native_decide`, or `Classical.choice` is used. These counts cover explicit declarations, not an additional count of Lean-generated constructors, projections, or deriving declarations.

The new connection is **formed specialization → actual transformation into further formation**, under the same material and work history. This supplies a concrete test of the ethical inference that generation may continue through ending and transforming a particular enabling relation. It also makes specialization's limits and the alternatives to transformation explicit. The mathematics does not itself warrant an ethical preference for repetition, diversity, retaining the bar, or dismantling it.

### Extension of the existing history

The extension imports the old state, material/work accounts, nine events, and the supplied two-port actuation law. Every old step and history embeds through `old_step` and `old_trace`. It adds three events:

| Event | Actual effect | Required support |
|---|---|---|
| `release` | Removes an existing spanning bar and returns its one material part to raw stock. Earlier products and any pending assembly persist; spent work increases. | A spanning bar and one remaining work unit. |
| `startAC` | Forms the `AC` dyad in the pending position. | No pending assembly, two raw parts and one work unit. |
| `finishZ` | Adds `b`, completing `Z=((a,c),b)` and retaining all earlier products. | The matching `AC` dyad, one raw part and one work unit. |

`Z` differs from both old forms at a common addressed position: root-left-right contains `c` in `Z`, `b` in `L`, and no atom in `R`. This is a third prescribed structural form, not a proof of open-ended innovation or biological diversity. The intact recovery of the bar part and its one-work release cost are new **local law premises**, alongside the supplied old recipes and ports. They are not claims that every real transformation has this cost or is reversible. Completed products cannot be disassembled in this law.

`step_accounts` and `trace_accounts` retain the existing whole material total and `source work + remaining work + spent work`. `release_preserves_products_and_history` records exactly what release changes and retains; no sunk work is refunded. `finite_branching` checks the exact twelve-event successor list. Old impossibility theorems do not transfer automatically when new events are admitted; the relevant bounds below are proved for this enlarged event repertoire.

### Checked positive construction and countercomparisons

`formed_then_reconfigured_history` works for any finite chronological list of `k` old forms. From **`3k+3` raw parts and `k+4` work units**, the history receives the source, constructs the bar, completes the list through synchronized operations, releases the bar, and forms `Z`. All `k` earlier products persist. The endpoint has `k+1` completed products, no bar/raw/work left, and exactly `k+4` work spent. The accounting includes both bar construction and release.

The following comparisons constrain its interpretation:

- **Repeated use can cover the transformation overhead.** The enlarged bypass process forbids only the two synchronized operations. It still permits release, every ordinary recipe, and spending on attachment or repair. `bypass_output_bound` proves that every such trace satisfies `2 × completed products ≤ initial work`. With the same `k+4` work budget, `repeated_use_strict_threshold` rules out `k+1` completed products for **`k≥3`**, while the coupled-and-reconfigured history completes them. This is a strict comparison under the supplied law, not a general theorem that novelty or a longer physical time horizon improves outcomes.
- **Two prior uses give an exact tie.** `two_uses_then_reclaim` and `two_use_ordinary_tie` start from the same nine parts and six work units and finish in the exact same full state containing `[Z,R,L]`, no bar, and zero remaining stocks. The ordinary history constructs all three products manually. A blanket preference for first forming and later releasing the bar is therefore false even in this model.
- **Specialization can prevent an otherwise supported completion.** From three parts and two work units, `direct_z_from_small_source` completes `Z`. If the bar is formed first, `premature_coupling_loses_completion` proves that *every* subsequent lawful history completes no product. Release returns the part but exhausts the last work unit. This is a same-initial-source countercomparison, not an unsupported alternative future.
- **Ending this relation can be necessary for further formation in a stated configuration.** After the synchronized prefix, `coupled 0 products` has two raw parts, a spanning bar, and three work units. `retained_material_cannot_complete` proves that every continuation that forbids release leaves the product list unchanged. `reclaim_then_z` releases the bar and completes `Z`, preserving earlier products. This necessity depends on the specified stock and event repertoire.
- **The same release also permits repetition.** `reclaim_then_existing` starts from that very same configuration and releases the bar before manually completing either `L` or `R`. `reconfigured_alternatives_match_support` proves that this endpoint and the `Z` endpoint agree in source/raw/work/spent/bar/pending, preserve the same earlier product-list tail, and have the same number of products, while their new products differ. Thus novelty versus repetition is not secretly settled by an unmatched resource advantage.
- **With another raw part, release is unnecessary for `Z`.** `common_choice_actual_history` reaches three raw parts, three work units and earlier `[R,L]` from a source of ten parts and six work units. `common_can_form_z_without_release` completes `Z` while keeping the bar and one work unit. `common_can_release_then_z` also completes it, ending with one raw part but no bar or work. `ordinary_z_keeps_more_work_and_bar` records this tradeoff rather than claiming whole dominance; the released route retains one more raw part.
- **The choices can still exclude one another.** At the last configuration, `common_can_reuse_coupling` completes another `L`, but `common_cannot_add_two_completions` bounds every lawful continuation at three total products. Conserved material prevents obtaining both additional completions in that history. Neither reconfiguration nor retention eliminates the actual conflict.

The two supplied ports, the work-saving coupling law, fixed roles and recipes, intact material recovery, and finite source remain explicit inputs. There are no deadlines, decay, uncertain arrivals, self-modifying intelligent agents, or an ethical ordering of the products. “Longer use” here means a finite family of supported construction histories; it does not mean that time alone provides resources or makes future use certain. The result concerns actual later formation, not an intrinsic value assigned to capacity stipulated never to be exercised.

Run the new formal check from the repository root:

```sh
python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_reconfiguration.py
```

[check_reconfiguration.py](check_reconfiguration.py) snapshots the three modules, its own code, and the inherited scanner from `check.py`; it validates the exact import chain before scanning. Fresh compilation, explicit-declaration axiom audits and output logs are retained under `reconfiguration-checks/`. Source and checker hashes must remain unchanged during the check. Earlier model and receipt files are preserved at their original scope; the reconfiguration receipt is a separate result.

## Generative premise and situated comparison

[GenerativeComparison.lean](GenerativeComparison.lean) audits the inference route approved after Ren's [generation-and-future proposal](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-generation-axiom-and-future.md). It adds **11 checked theorems and 27 explicit declaration audits**, with only `propext` and `Quot.sound` among the audited axiom dependencies. It does not add another assembly law. The [derivation](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-PREMISE-DERIVATION.md) explains and defends the proposed premises; the code checks their stated inferential consequences.

`Inventory Whole Claim` describes actual relational realizations and proposed favoring grounds across whole continuations. Its `generative` subset is not filtered through an independent prior test of worth. G0 supplies positive ethical relevance for actual generative realizations. Other favorable grounds, if included, need their own stated provenance. The inventory must retain relevant intermediate histories and actual losses; matching endpoint resources does not establish that requirement. Claim meanings must be shared and stable, with truthful realization: adding labels to an unchanged history cannot create a generative gain. None of this correspondence is guaranteed by the structure's Lean type.

`GenerativeExtension first second` retains every represented claim and includes an actual generative realization absent from the first continuation. This relation is irreflexive and transitive, without using a scalar measure or assuming every pair is comparable. It does not require preservation of the same material parts or configuration; a ground may continue through actual replacement. Conversely, an omitted adverse effect cannot be declared absent because it has no field in this representation.

The dependency ledger is explicit:

| Premise | Formal consequence checked | What remains supplied |
|---|---|---|
| G0: actual generative realizations have positive relevance | A new realization in a generative extension has that positive relevance. | The substantive normative warrant of G0 and faithful identification of its realizations. |
| C: a completely covered no-loss generative extension warrants strict comparison | The represented extension is admitted by `Better`. | C's defense as an articulation of G0, full-history coverage, and adequacy of the intended strict comparison. |
| C and P: strict comparison among feasible situated responses supplies a reason | `comparison_supplies_situated_reason`. | Actual feasibility/influence, correspondence and the practical articulation P. A reason alone does not establish an obligation or authority. |
| C and N: selection is feasible and excludes strict domination | `coherent_selection_survives_filter`. | The stronger selection-coherence N. Surviving the filter is not sufficient for final permission or selection. |

The C/P/N theorems have **no unused G0 parameter**: the audit does not pretend to derive the comparison principle from the thinner relevance premise. Distinguishing the commitments exposes the argument; it does not assert separate causal and ethical realities or prove that these commitments are irreducible independent axioms.

N does not ensure a selection exists: an empty `Selected` predicate satisfies its implication vacuously. More substantively, `continual_improvement_has_no_survivor` proves that when every feasible option has a feasible generative extension, **no option survives this filter**. Even a nonempty feasible domain can therefore have no permitted selection under N plus C. The positive direction must not be silently converted into an impossible demand to choose a final maximum; G0 and P alone do not impose N.

`feasible_restriction_preserves_survivor` checks only a one-way property of the filter: removing rivals while retaining a feasible option cannot newly disqualify that option through this rule. It neither improves whole realizations by deleting alternatives nor guarantees justified reason preservation after substantive self-modification. Faithful redescription is already handled in [WholePracticalRestriction.lean](../WholePracticalRestriction.lean); this module does not duplicate that result or claim that all future revisions are faithful redescriptions.

The finite control uses four profiles over two dimensions of actual generation, with both `(true,false)` and `(false,true)` feasible. Two strictly positive appraisals, `2a+b` and `a+2b`, respect every represented no-loss extension. They rank those two conflicting realizations in opposite directions and admit different coherent selections, while both options survive the generative-extension filter. Thus the partial rule leaves this tradeoff open. The coordinates and weights are an inference illustration, not measured ethical quantities, a proposed utility function, or a substantive refutation of the fuller whole-generative theory.

Run the fresh check:

```sh
python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_comparison.py
```

[check_comparison.py](check_comparison.py) snapshots the source, itself and the inherited declaration scanner. [comparison-verification.json](comparison-verification.json) binds the checked source and Lean binary hashes; retained `comparison-checks/` logs contain fresh compilation, every explicit declaration's axiom audit and all eleven theorem signatures. No custom Lean axiom, admitted proof or unchecked native decision procedure is allowed. The standard Lean dependencies and normative premises remain different things; their disclosure does not complete the stronger no-assumptions or universal ethical-grounding objective.

## Necessary loss and correction of its identification

[GenerativeTradeoff.lean](GenerativeTradeoff.lean) adds a descriptive interface for applying the generative comparison to mixed gains and losses. **Eleven theorems and 28 explicit declaration audits pass Lean 4.29.1, with no axiom dependencies in the audited declarations.** This checks represented necessity and uncertainty; it does not prove that a necessary loss is ethically permitted, required or outweighed by the target.

`Problem` relates differentiated circumstances and responses to their full represented histories. `NecessaryLoss` requires both a feasible route that attains the specified target and loss on **every** represented feasible route that attains it. An unattainable target therefore does not acquire a supposed necessary price through a vacuous universal statement. The response repertoire, relevant history and loss identification remain correspondence obligations; an unlisted alternative is not thereby impossible. A real lossless alternative refutes the stated necessity claim, even if a previously considered response incurs loss.

The finite control supplies the following three-stage histories. “Lossless” means no interruption of this specifically represented support relation, not an established absence of all ethical losses. Other actual costs or effects require representation before applying a whole comparison.

| Response | Feasibility | Opening / middle / closing support | Target formed |
|---|---|---|---|
| Keep the existing realization | All three circumstances | true / true / true | false |
| Interrupt and restore | All three circumstances | true / false / true | true |
| Continuous left handover | Left handover support is ready | true / true / true | true |
| Continuous right handover | Right handover support is ready | true / true / true | true |

The circumstances are left support ready, right support ready, and no handover support ready. The two handover routes are mutually unavailable in the opposite circumstances. The total continuation function also has values at infeasible entries, but those values never count as actual routes: every success and uniform guarantee includes feasibility.

The checked controls establish these distinctions:

- **Restoration retains the history.** Restored and continuous handover histories have the same explicitly defined endpoint projection—closing support and target formation—but only the restored history contains a middle interruption. This is not equality of complete physical endpoint states, nor a claim that restoration removes every loss.
- **Necessity is conditional.** When neither handover is supported, successful target formation necessarily interrupts the selected support. Keeping the old realization remains feasible and uninterrupted while not attaining that target. The theorem does not require pursuing the target.
- **Certainty needs retained actuality.** A universal necessity judgment over candidate circumstances applies to the actual circumstance when that circumstance is included. Narrowing a candidate set preserves an already universal certificate; subset inclusion alone does not warrant the narrowed set's truthfulness.
- **Evidence can resolve uncertainty, while exclusion can manufacture certainty.** The set of all three circumstances does not certify necessary interruption. If the actual circumstance is no handover, identifying that singleton does certify it. If the actual circumstance is left-ready but inquiry retains only no-handover, the same formal certificate is false of actuality. The counterexample changes actual route coverage, not an arbitrary ethical verdict.
- **Pointwise routes are not one available response.** Each of the left-ready and right-ready circumstances admits an uninterrupted successful handover, but no single response works successfully without interruption in both. A real contingent policy would need a feasible and accurate observation, the observation's intermediate history and cost, and a subsequent response mechanism. None is silently inferred here from the pointwise existence statements.

These definitions do not require permanent continuation of every old organization. The support relation and target are specific to the comparison. The module contains no scalar aggregation, new ethical ranking, empirical observation or proof that a represented history realizes its intended biological or experiential counterpart. Its universal quantifiers range over the declared correspondence interface; they do not establish universal ethical grounding.

In particular, `keep` maintains the selected support at all three represented stages while leaving the target unrealized. It does **not** implement a history that achieves a finite gain and then permanently ends a shared practice. The philosophical proposal to compare irreplaceable generative conditions with postponable gains needs its own whole-history identification; this finite table supplies necessity and knowledge checks, not a complete dynamic instance or proof of that ethical priority.

Run the fresh source and dependency check:

```sh
python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_tradeoff.py
```

[check_tradeoff.py](check_tradeoff.py) snapshots the module, checker and inherited scanner; [tradeoff-verification.json](tradeoff-verification.json) binds their hashes and the Lean executable hash. The retained `tradeoff-checks/` run contains fresh compilation, all explicit declaration axiom audits and theorem signatures. Existing comparison and construction modules retain their earlier checked scope. Absence of Lean axiom dependencies does not discharge this module's supplied targets, route laws, correspondence or the ethical premises of the wider investigation.


## Matched loss comparison, 8 October 2026

[GenerativeLossComparison.lean](GenerativeLossComparison.lean) audits transport of independently warranted mixed comparisons across matched loss changes. It separates that result from a first mixed anchor and a finite sacrifice bound. The [philosophical integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-LOSS-COMPARISON-INTEGRATION.md) includes the affirmative argument, substantive author counterreview, primary-source scope and complete-goal audit. The requested post-completion independent agent verification remains pending.

Fresh Lean 4.29.1 checking passes 16 new theorems / 23 explicit declaration audits, depending only on standard `propext` and `Quot.sound`. Run from the repository root:

```sh
python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_loss_comparison.py
```

The [receipt](loss-comparison-verification.json) binds exact sources, checker bytes, dependency/signature logs and retained snapshots. The finite `Route` family is an illustrative comparison control; its interruption index is not a universal ethical score, a physical implementation or a demonstrated sacrifice threshold. Kernel success supplies neither first ethical warrant nor practical authority.

## Request histories through versioned route updates

`CorrectionVersioned.lean` adds 33 checked theorems / 62 audits, with 62 inherited theorems / 100 audits rebuilt separately. Two retained banks support incremental preparation and per-request traversal; mixed histories, early reuse and delayed pin registration retain explicit failures. Run `python3 check_correction_versioned.py` for Lean and `python3 compare_correction_versioned.py` for the finite graphs and controlled thread trials. [Integration and exact scope](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/VERSIONED-CORRECTION-INTEGRATION.md).
