<a id="第二部分的清点--inventory-of-part-ii"></a>
# Inventory of Part II

> part i first, then consider second(maybe a lot in second will move to part i)

> if we don't need G0 as axiom, fold it, at least for part i, and commit

2026-10-11, Asia/Bangkok. An inventory written by the AI (Claude Opus 5.5, session Universal Metaethical Core) in answer to Ren's two messages quoted above. It is an inventory and a proposal: nothing enters the core and no result is registered. The classification is reproduced by a [script](PART-II-INVENTORY.py) from the sources the two receipts bind, and each use of the axiom was checked by reading the proof. The proposal to move material is the AI's, pending Ren.

<a id="0-问题--the-question"></a>
## 0. The question

**English.** After the fold of G0 (P51, study section 67), what Part II adds is one axiom, `Unrestricted`: from every standpoint, the continuation of anything has significance at every step. The question is which of Part II's theorems use it, and where; those that do not belong to Part I. The zero-premise inventory (ZERO-PREMISE-PLAN section 1) excluded Part II's modules (Significance, Metaethics, Standpoints, Ranking, Renewal, Bridge, Correspondence), and it predates the landing of P42–P44 (Feedback, Boundaries, Relevance). This inventory covers them and adds the dimension of the axiom and the evaluative conditions.

<a id="1-方法--method"></a>
## 1. Method

**English.** The scope is every declaration that Part II of the chapter names, from its heading to that of section 8 (sections 6 and 7): 197 names, which after removing module names, witness namespaces and variables are 182 declarations, 157 theorems and 25 definitions. Declarations are looked up in the sources bound by the core and periphery receipts (core `20261011T071749.484228Z`, periphery `20261011T071753.574921Z`, after `Becoming.Locality` landed; the result is the same under the receipts before R6, `20261011T003217.297180Z` and `20261011T003646.599930Z`).

The core has no axioms, so a theorem can use the axiom only by taking `Unrestricted sig` as a hypothesis. The same holds for G0 or its parts, the other evaluative conditions, the structural conditions and Part I's premises. A mention only in the statement, inside an iff or in the conclusion, is not a use. Hypotheses are read from the signature's binders and the antecedents of the statement's outermost implications. Section `variable`s introduce only data (flows, webs, parts, relations), never hypotheses; each was checked. The classes:
- **axiom**: takes `Unrestricted` as a hypothesis;
- **characterizes the axiom**: the axiom occurs only in the statement;
- **evaluative condition**: takes G0, the seed with both neutralities (`Grounds`), S0, N, A, the presupposition (`SubTrue`) or invariance (`BoundaryInvariant`) as a hypothesis;
- **Part I's premises**: takes only balance, dissipation, embodiment, census, taking, acting, dependence, enclosure, finiteness or decidability;
- **structural condition**: takes only connection or holding;
- **none**: takes none of these.

<a id="2-结论--findings"></a>
## 2. Findings

**English.**
- **Of 157 theorems, 22 use the axiom and 135 do not.** Of the 135, 85 take no premise at all, 18 take only Part I's premises, 12 take an evaluative condition, 2 take a structural condition, and 18 characterize the axiom without assuming it, for example `unrestricted_iff_g0`, `unrestricted_iff_presupposed`, `bounded_rival`.
- **Each of the 22 uses the axiom only at named points** (section 3.1). A point is the significance, from a standpoint, of a formation's continuation at a step. The points are of three kinds:
  - (i) one formation at one step of a witness: `Clearing.free_rider_loses` uses only the dweller at step 2, and `Preemption.not_undermining_yet_loses` only `false` at step 1;
  - (ii) the formations a compared path admits, or where it exceeds;
  - (iii) living realized claims, in the derivations of G0.
- **Each is a law holding for any significance, specialized at those points.**
  - For (ii) the general local form is already P42's: any significance covering what a part has reached before each step compares that part as the axiom does (`Flow.Balances.comparison_within_reach`).
  - For (iii) the local form is G0 itself: with positive relevance read from significance, G0 is exactly the axiom restricted to realized living content (the fold, section 67).
- **So Part II adds one assertion to Part I.** Each theorem of Part II is a Part I law with its conditions written inside it. The axiom, once asserted, meets the significance condition at the points named; for the comparison of a part it need only meet it where the part reaches (P42). A, C, L and J1–J4 stay disclosed conditions of the practical laws and are not asserted.
- **The statements themselves name the points needed.** That a universal hypothesis in Lean is always used at some points is trivial. What the inventory adds is which points: the compared paths, the part's reach, the living claims. So each theorem can be stated with a local condition.
- **Localizing the premises remains.** The 18 theorems that take only Part I's premises use global balance and the like; none of the 22 that use the axiom takes a Part I premise. By the zero-premise inventory's classes all 18 are localizable, two of them needing only decidability, class (b2). Four are already in that inventory (`Flow.fed_from_beyond`, `Flow.excess_bounded`, `Flow.joint_excess_ends`, `Flow.Balances.consumption_ends_with_feeders`). The other 14 are not: two need only decidability; `Flow.region_not_a_cut` goes through `Flow.fed_from_beyond`; and 11 lie in Part II's modules and use balance only at earlier steps, on the conditions the compared formations require (section 3.3).

<a id="3-逐条--theorem-by-theorem"></a>
## 3. Theorem by theorem

<a id="31-用到公理的-22-条--the-22-that-use-the-axiom"></a>
### 3.1 The 22 that use the axiom

“Via” means the proof uses the axiom through another of the 22.

| Theorem | § | Points used | The law for any significance it specializes |
|---|---|---|---|
| `Clearing.free_rider_loses` | II, 6.8 | `(p, 2, dweller)` | the witness's admission facts with `Web.Retains.not_added`; the bounded form is `Clearing.centers_disagree` |
| `Clearing.within_closure_yet_loses` | 6.9 | via `free_rider_loses` | as above; its other two parts hold for significance bounded by the closures |
| `Preemption.not_undermining_yet_loses` | 6.8 | `(p, 1, false)` | the witness's admission facts with `Web.Retains.not_added` |
| `Trophic.mediated_unregistered` | 6.10 | `(p, 1, deer)` | as above |
| `Transfer.unordered` | 6.8 | via `Web.adds_iff_exceeds`, at the two exceeding points | `Web.Adds.exceeds`，`Web.Retains.not_added` |
| `Trophic.responsive_mixed` | 6.10 | as above | as above |
| `Restoring.Inflow.retains_adds` | 6.8 | via `Web.adds_iff_exceeds`, at the exceeding point | its retaining part holds for any significance (`Web.Includes.retains`) |
| `Web.retains_iff_includes` | 6.8 | `(p, t, f)` for each `f` the compared path admits at `t` | `Web.Includes.retains` with the definition of `Web.Retains`; for a part's comparison, `Flow.Balances.comparison_within_reach` |
| `Web.adds_iff_exceeds` | 6.8 | the exceeding `(p, t, f)` | `Web.Adds.exceeds` |
| `Web.retains_agree` | 6.8 | via `Web.retains_iff_includes`, at `p` and `q` | as `Web.retains_iff_includes` |
| `Web.Retains.within` | 6.8 | `(p, t, f)` for `f` in the region | `Web.Retains.of_fewer` |
| `Web.retains_bounded_iff_retains` | 6.9 | via `Web.retains_iff_includes` | `Web.retains_bounded_iff_includes` |
| `Flow.within_closure_iff_retains` | 6.9 | via `Web.retains_bounded_iff_retains` | as above, with the feeding closure as the region |
| `Overshoot.within_closure_iff_retains` | 6.9 | via `Flow.within_closure_iff_retains` | as above |
| `Ranking.possible_extends_iff` | 6.12 | `(p, t, f)` at the credited events | `Ranking.possible_course_iff` (credit is admission) with the definitions of `Retains` and `Adds` |
| `Valuation.premises_of_unrestricted` | 6.8 | `(p, step c, formation c)` for each living claim `c` | the definitions of `Significant`, `SelfGood`, `Seed`, `Neutral` |
| `Web.significant_of_unrestricted` | 6.8 | as above, for events and relations | as above |
| `Conditions.significant_of_unrestricted` | 6.8 | as above, for whole-run events | as above |
| `Web.paths_g0_comparison` | 6.8 | as above, on level paths, and the added point | as above; the definitions of `Web.Retains`, `Web.Adds` |
| `g0_of_unrestricted` | 6.12 | `(p, step c, formation c)` for realized living `c` | the definition of `G0`: with positive relevance read from significance, G0 is the axiom at these points |
| `relevance_least` | 6.12 | as above | as above |
| `universal_reason_of_unrestricted` | 6.12 | via `Valuation.premises_of_unrestricted` | `universal_reason_living`, with `V.Significant` as a condition |

<a id="32-刻画公理的-18-条--the-18-that-characterize-the-axiom"></a>
### 3.2 The 18 that characterize the axiom

**English.** They say when the axiom holds, or whether it holds in a witness, without assuming it. They are Part I laws about the axiom.

- §6.8：`bounded_rival`
- §6.9：`bounded_whole`
- §6.10：`Clearing.system_whole`、`Flow.bounded_system_whole`、`Clearing.reach_counts_dweller`
- takes the presupposition and invariance）、`unrestricted_iff_presupposed`、`unrestricted_iff_presupposed_along`、`Clearing.without_presupposition`、`Clearing.without_invariance`、`Clearing.with_fixed_boundary`、`unrestricted_iff_presupposed_of_whole`、`Flow.unrestricted_iff_system_presupposed`、`Flow.unrestricted_iff_presupposed_of_common`、`Clearing.system_presupposition`
- §6.12：`unrestricted_iff_g0`、`Web.unrestricted_iff_paths_g0`

<a id="33-只用第一部分前提的-18-条--the-18-that-take-only-part-is-premises"></a>
### 3.3 The 18 that take only Part I's premises

| Theorem | § | Premises | Localization |
|---|---|---|---|
| `Flow.fed_from_beyond` | 6.7 | balance, dissipation, decidability | zero-premise inventory group B |
| `Flow.region_not_a_cut` | 6.7 | balance, dissipation, decidability | **Not in the inventory.** Through `Flow.fed_from_beyond` (group B) |
| `Flow.excess_bounded`、`Flow.joint_excess_ends` | 6.7 | balance (with acting, dependence) | group C |
| `Flow.Balances.consumption_ends_with_feeders` | 6.9 | balance, acting, dependence | group C |
| `Flow.inward_iff_not_fed`、`Valuation.significant_iff_reached` | 6.7 | decidability only | **Not in the inventory.** (b2), Ren's |
| `Flow.Balances.retains_iff_within_margin`、`loses_iff_beyond_margin`、`adds_iff_within_margin` | 6.8 | balance | **Not in the inventory.** Through `Balances.supported_iff_within_margin` and in the end `Balances.withheld`: balance at the steps before `t`, on the conditions `f` requires |
| `Flow.Balances.unregistered_beyond_influence`、`comparison_within_reach`、`closed_comparison`、`comparison_within_difference`、`comparison_local`、`adds_iff_exceeds_of_decidable` | 6.10 | balance (one with decidability) | **Not in the inventory.** Through `Balances.agrees_or_reaches_before` and in the end `Balances.withheld`: balance at the steps before `t`, on the conditions the compared formations require; `comparison_within_difference` goes through `Balances.differs_before`, using both flows' balance at earlier steps on that condition |
| `Flow.Balances.presupposed_comparison`、`presupposed_reach_comparison` | 6.11 | balance | **Not in the inventory.** Through `comparison_within_reach` |

<a id="34-以评价条件或结构条件为假设的-14-条--the-14-with-an-evaluative-or-structural-condition"></a>
### 3.4 The 14 with an evaluative or structural condition

**English.** They hold for every valuation meeting the condition; like G0 after the fold, they are Part I's conditional laws.

| Theorem | § | Condition |
|---|---|---|
| `Valuation.significant_iff` | 6.1 | connected |
| `Conditions.valuing_consumption_reaches`、`Web.valuing_breaking_reaches`、`Flow.valuing_reaches_source` | 6.3, 6.7 | N_rel |
| `universal_reason` | 6.3 | the seed with both neutralities, A, connected |
| `positioned_articulation_of_articulates` | 6.4 | A |
| `Valuation.significant_iff_held` | 6.7 | held |
| `Valuation.own_transmission` | 6.7 | S0 |
| `Valuation.significant_of_transmits` | 6.7 | S0, N_rel, connected |
| `subTrue_of_larger`、`boundaryInvariant_iff_all` | 6.11 | the presupposition |
| `not_subTrue_of_invariant` | 6.11 | invariance |
| `retains_agree_of_presupposed`、`Valuation.significant_of_presupposed` | 6.11 | the presupposition and invariance |

<a id="35-什么前提都不用的-85-条--the-85-that-take-no-premise"></a>
### 3.5 The 85 that take no premise

- II：`Clearing.loses_beyond`
- §6.1：`Mutualism.significant_iff`
- §6.3：`Conditions.significant_iff_of_common`、`Web.significant_iff_of_common`、`Separate.not_connected`、`Web.inert_connects`、`Web.connected_of_renewable`、`Shared.connection_by_living_use`、`Web.one_use_connects`、`Renewable.class_belongs_to_the_run`、`Renewable.readings_differ`、`Web.living_iff_relations`、`Renewable.finite_reading_credits_consumption`、`Renewable.amount_reading`、`Dependence.Overdetermined.no_difference`、`Renewable.no_finite_segment_makes_difference`
- §6.5：`articulation_iff_lifted`、`Ranking.restraint_ranks`、`Ranking.malignant_restraint`
- §6.7：`Lone.fed_not_recurring`、`Pair.own_not_joint`、`Exceeding.all_end`、`Alone.all_continue`、`Downstream.one_way`、`Mortal.after_its_end`、`Clearing.undermines_within_renewal`、`Apart.not_enough`、`Web.significant_iff_self`、`Clearing.clearer_not_living`、`Clearing.center_not_derived`、`Flow.conveyance_idle`、`Clearing.resource_not_cut_living_on`、`Clearing.conveyance_only`
- §6.8：`Web.Retains.not_added`、`Web.Retains.of_fewer`、`Web.retains_bounded_iff`、`Web.AdmitsWithin.narrow`、`Clearing.centers_disagree`、`Web.significance_undetermined`
- §6.9：`Flow.beyond_gives_nothing`、`Clearing.dependenceRegion_iff`、`Overshoot.ends_through_feeder`、`Clearing.closure_supported`、`Web.retains_bounded_iff_includes`、`Clearing.levels`、`Clearing.reach_middle`、`Trophic.mediates`
- §6.10：`Flow.system_whole_of_common`、`Clearing.unregistered`、`Clearing.reaches_dweller`、`Clearing.system_counts_dweller`、`Trophic.difference_reaches_forest`、`Clearing.no_levels_without_source`、`Margin.reach_without_misjudgment`、`Flow.reach_whole_of_common`
- §6.11：`Boundary.closure`、`Boundary.whole`、`Boundary.only_whole`、`superTrue_iff`、`boundaryInvariant_iff_determinate`、`superTrue_member_iff`、`subTrue_member`、`subTrue_significantWithin_iff`、`superTrue_significantWithin_iff_union`、`superTrue_level_free`、`subTrue_empty_iff`、`subTrue_total_iff`、`bounded_closure_iff`、`bounded_closure_least`、`presupposition_scopes`、`boundaryInvariant_iff_conditional`、`boundaryInvariant_iff_standpointInvariant`、`OneCounts.forms_apart`、`Clearing.without_standpoint_invariance`、`Flow.presupposition_order`、`Clearing.levels_differ`、`Clearing.own_presupposition`
- §6.12：`articulates_total`、`Widening.bare_forces_reason`、`Ranking.malignant_possible`、`Ranking.possible_tie`、`Ranking.readings_rank_presence`、`Ranking.possibleFirst_order`、`Ranking.possibleFirst_presence`、`Ranking.Rest.rest_ranked_below`

**English.** Theorems about witnesses (such as `Clearing.*`, `Trophic.*`) prove that their witness satisfies balance and the like; these premises occur in the conclusion, not as hypotheses.

<a id="4-提议待-ren-proposal-for-ren"></a>
## 4. Proposal (for Ren)

**English.**
1. **The chapter.** Move what in Part II does not use the axiom into Part I. After Part I's section 5 (how evaluation forms), add a section “Laws of significance”, stated for any significance:
   - retaining and adding, and the boundary of not harm (the margin);
   - the whole first and regions, route (b) (the feeding closure), feedback and reach;
   - the decomposition of the axiom (presupposition and invariance);
   - the characterizations of G0 and of the axiom (`significant_iff`, `significant_iff_held`, `unrestricted_iff_g0`, `unrestricted_iff_presupposed`);
   - centers and standpoints, the correspondence discipline and connection;
   - reasons (with A as a condition) and comparison (with the reading compared as a condition).

   Part II keeps three things: the assertion of the axiom; that it meets the significance condition at the points named, so that the 22 of section 3.1 no longer need that condition (their other conditions stay, as A stays for `universal_reason_of_unrestricted`); and the question of its warrant (section 8).
2. **Localizing the premises.** The 12 rows of section 3.3 outside the zero-premise inventory that use balance (`Flow.region_not_a_cut` and the 11 in Part II's modules) are re-proved in place as corollaries once their local forms land. The 11 go through `Balances.withheld`, whose local forms `withheld_at` and `supported_iff_within_margin_at` group C's patch provides (the zero-premise inventory places `supported_iff_within_margin` in group C through `Balances.withheld`); `comparison_within_difference` also goes through `Balances.differs_before`. `Becoming.Locality` has landed (12c7cb44). The integrator orders them.
3. **Lean (optional).** Most local forms of the 22 are already in Lean as laws for any significance: the margin laws, `comparison_within_reach`, `Retains.of_fewer`, `retains_bounded_iff_includes`. Where the chapter needs it, the witnesses of kind (i) can be stated with their local significance condition, with the axiom's forms as corollaries. This needs a claim and a core checker run, queued after Part I's items.

<a id="5-不主张什么--what-is-not-claimed"></a>
## 5. What is not claimed

**English.**
- No new theorem. The classes are read from signatures and the points from proofs; the axiom reports are unchanged.
- The axiom is not claimed derivable: the dynamics does not decide significance (`Web.significance_undetermined`). What moves into Part I are the laws that do not use the axiom, not the axiom.
- The move is not claimed adopted: the chapter's structure is Ren's, and Part I's order and interfaces are the integrator's.
- The periphery results that section 7 cites by record name (the correction sequences and the like) are outside this inventory.
- The readings are unchanged and still Ren's: positive relevance read from significance, and the possibility reading of C.

<a id="6-协调--coordination"></a>
## 6. Coordination

- **整合者 / The integrator.** 本清点是对第一部分结构的输入；§4 的第 1、2 项交整合者排序。 / This inventory is input to Part I's structure; items 1 and 2 of section 4 go to the integrator to order.
- **零前提清点 / The zero-premise inventory.** 本清点补上其所排除的第二部分模块；§3.3 中标“不在清点之内”的 14 条可并入其 §1.3。 / This inventory covers the Part II modules it excluded; the 14 rows of section 3.3 marked as outside it can join its section 1.3.
