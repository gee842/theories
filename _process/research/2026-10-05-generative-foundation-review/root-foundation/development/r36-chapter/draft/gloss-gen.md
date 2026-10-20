| Term (Chinese name) | Meaning | Lean anchor |
|---|---|---|
| keeps moving, of a family (保持运动) | From every member some step leads to a member. | `KeepsMoving`, `KeepsMoving.run` |
| dependent choice (依赖选择) | A total relation has, from every starting point, a sequence along it. | `DependentChoice`, `runs_iff_dependentChoice` |
| reach (可达) | A finite admissible path. | `Reach` |
| invariant (不变量) | A property kept at every step. | `Invariant` |
| absorbing region (吸收区域) | A region a law never leaves. | `Law.Absorbing`, `Law.absorbing_iff_invariant`, `AbsorbingUnder`, `invariant_iff_every_move` |
| drawn into, basin (被吸入、吸引域) | A configuration outside an absorbing region whose orbit enters it is drawn into it; those drawn into an absorbing region form its basin. | `Law.DrawnInto`, `Law.Drawn`, `Law.drawn_iff_not_returns` |
| attractor (吸引子) | An absorbing region that configurations from outside enter. | `Law.returning_absorbing`, `Law.drawnInto_returning` |
| lock-in (锁定) | What is drawn in never comes back. | `Law.DrawnInto.never_back`, `Invariant.locks_out`, `Run.locked_in`, `Run.leaving_needs` |
| novel realization (新实现) | A claim not realized before, under some reading. | `Novel` |
| scope (所见范围) | The configurations a policy's actual executions reach. | `Scope` |
| judgment process (判断过程) | Takes one admissible response at the configuration judged and then ends; its common response is the robust judgment. | `judgeProcess` |
| conditions (条件) | The observables of condition levels, activity, dependence and drawing. | `Conditions` |
| kept / broken (维持／断裂) | Across a step, a satisfied dependence is still satisfied / no longer satisfied. | `Kept`, `Broken` |
| comes to be / ceases to be (开始成立／不再成立) | A specification goes, across a step, from not holding to holding / from holding to not holding. | `ComesToBe`, `CeasesToBe`, `Web.change_readings` |
| forms / dissolves, of a dependence (形成／消解) | A dependence appears / disappears across a step. | `Forms`, `Dissolves` |
| renewal at a step (步内更新) | The step of the event keeps every dependence on the conditions it takes part in; the stepwise classification of renewal. | `RenewingAt` |
| breaking, of an event (断裂) | Drawing on a condition at a step at which some dependence on it breaks. | `BreakingOn`, `BreakingAt` |
| keeping pace (同步) | In a finite family, over any stretch of steps the numbers of comings-to-be and ceasings-to-be differ by at most the number of members; what holds at the end together with what ceased in between is exactly what held at the start together with what came to be in between. | `keep_pace`, `held_over_stretch` |
| unceasing arising (不息) | Some formation arises at arbitrarily late steps; the same formation may arise again. | `Unceasing` |
| depletion, of a finite family (消耗) | At the event's steps at which no condition of the family rises, some condition in it falls; it says only that a condition in the family changes. | `Depletes`, `Balances.depletes` |
| one exchange (同一交换) | At a dissipated step, one member's rise with another member's fall. | `rise_with_fall`, `rise_exchange` |
| closed (封闭) | At a step no formation taking part exchanges with a condition outside the family. | `ClosedAt` |
| enclosed step (封闭的步) | Across the step some finite family without repetition is closed; where the conditions are finitely many in all, every step is. | `Enclosed` |
| balance at a step (一步的平衡) | A flow balances on a family across a step: each member's level after the step together with what was taken equals its level before together with what was given. | `Flow.BalancesOn`, `Flow.balances_iff_on` |
| imbalance relatum (不平衡关系项) | Where a flow does not balance, the difference is counted as the exchange of one more relatum that is never active and requires nothing. | `Flow.withImbalance`, `Flow.balancesOn_iff_idle`, `Flow.withImbalance_acting_taking_on_iff` |
| rest of the whole (整体的其余) | The imbalance counted as the relatum `none`: it gives each condition the part by which its level rises beyond the flow's net exchange, takes the part by which it falls beyond it, and never requires anything. | `Flow.withImbalance`, `World.withRest`, `World.withRest_closed_iff` |
| running down (下降) | Across a step a family contains, without repetition, every condition standing before or after the step, and the flow balances and dissipates on it (closure is not needed). | `Flow.RunsDownOn`, `Flow.RunsDown`, `Flow.change_recurs_iff` |
| laws of one step (一步的规律) | Laws holding for every world, with the conditions their proofs use written into the law. | `Becoming.Locality` |
| enclosed around (围住) | Across the step some finite family without repetition containing the given family is closed. | `Around`, `Enclosed.around`, `Enclosed.around_not_not` |
| drawing in (汲入) | The family cannot be inward from any step on: it is not the case that from some step on no formation gives to the family while taking from outside it. | `Inward`, `taking_draws_in`, `embodiedArising_draws_in` |
| conveying (输送) | Where a formation taking part takes from one condition and gives to another, something is conveyed from the first to the second. | `Conveys`, `conveyance` |
| cut (切口) | No formed relation leaves a region. | `Cut`, `region_not_a_cut` |
| fed by (供给延续) | At the same step, one event's formation gives to a condition that another event's formation needs. | `FedBy` |
| uptake / replenishment (取用／补充) | The total that the formations taking part take from / give to the family at a step; the two balance with the change of level. | `uptake`, `replenishment` |
| takers / renewers (取用者／补充者) | The formations that take from / give to the family at a step. | `takers`, `renewers` |
| arising taking (取用而生起) | A formation takes from the family at its first active step. | `ArisesTaking` |
| covers (覆盖) | A list contains every member that holds at a step. | `Covers`, `coming_of_ceasing_covered` |
| decided (已定) | A proposition holds or does not hold; a decision procedure gives this as data. | `Decided`, `not_not_decided` |
| count (计数) | A number counts the members of a list at which a specification holds: it is the sum of their indicators. | `Indicates`, `Counts`, `CountsAcross`, `counts_iff_decided`, `Counts.over_stretch` |
| tally (计数表) | The number listed at each step, with the numbers that cease and come to be across steps: across each step some members are kept, which with those that cease are the list before and with those that come to be are the list after. | `Tally`, `Listed.keeps`, `tally_iff`, `Queue.counts`, `counting_laws`, `tally_iff_counted`, `World.counting_free`, `World.counting_binds_jointly`, `World.premised_counting`, `World.counting_under`, `World.counting_binds_iff`, `World.binding_counting`, `World.binding_counting_under`, `World.finite_binding_counting_under`, `World.enclosed_binding_counting_under`, `World.standing_counting_under`, `World.dependence_counting` |
| change bound (变化界) | From some step on, the number listed at each step together with the steps since then at which something ceased or came to be is at most a number. | `ChangeBound`, `occurrences`, `World.enclosure_bounds_change`, `World.enclosed_counting`, `World.finite_counting`, `World.enclosed_counting_under`, `World.finite_change_bound_iff`, `World.enclosure_bounds_standing`, `World.enclosed_standing_bound_iff`, `World.finite_standing_bound_iff` |
| taking (取用即汲取) | Only active formations take, and only from conditions they draw on. | `Taking` |
| more without end (不止地更多) | For every number, from some step on at least that many formations take from the finite family of conditions. | `More` |
| re-identification / renaming (改认／改名) | A one-to-one correspondence between two namings at each step that leaves each step's relations unchanged; a re-identification that is the same at every step is a renaming. | `Reidentify`, `Reidentify.rename`, `Web.reidentify` |
| continuity (连续) | A formation that stays active, or stays dependent on some condition, across a step keeps its name. | `KeepsActive`, `KeepsTenure`, `Reidentify.back` |
| succession (接续) | Joining a formation that ends at some step with one that begins at or after that step as one and the same (with steps between that are inactive and dependent on nothing, for example dormancy). | `Lineage`, `Succession`, `Dormancy` (witness) |
| continuation (延续关系) | Which formation before a step a formation after it continues. | `Web.Continues`, `ArisesFrom`, `NoSplit`, `CeasesFrom`, `NoMerge`, `Census.balanceFrom` |
| whole / parts (整体／部分) | A whole is active exactly while some part is: a coincidence of activity. | `Whole`, `Covered`, `Brief`, `Ends`, `Listed` |
| embodied (体现) | A relatum stands as a condition, at a positive level, exactly while it is active: a reading under the one correspondence. | `Embodied`, `Embodied.comesToStand`, `Embodied.replenishes`, `Mutualism.apart_embodied` |
| coming to stand (开始作为条件而在) | A condition's level goes from zero to positive across a step: a rise from zero. | `Web.ComesToStand`, `ComesToStand.rises`, `Balances.rise_given`, `standing_given`, `rising_draws_in` |
| ceasing to stand (不再作为条件而在) | A condition's level goes from positive to zero across a step. | `Web.CeasesToStand`, `Web.standing_recurs_iff` |
| bearing on itself (承担自身) | A relatum, while active, depends with positive need on its own level. | `SelfBearing` |
| coextinction (共灭) | Under `Dependent`, a relatum inactive at some step ends, at that step, every formation that a chain of dependence (with positive need, through embodied relata) leads to it from. | `coextinct`, `Carries.coextinct_lasts`, `Carries.chain_ends`, `Carries.chain_ends_of_em` |
| reserve (储备) | An amount that does not rise while the formation is unsupported and falls while it is active then. | `Web.Carries`, `carries_zero`, `Flow.carries_of_held`, `Carries.lasts` |
| undermining (侵蚀) | Drawing on a condition at a step after which the condition is below both what some dependence now requires and what that dependence required at some step of its unbroken holding when it was satisfied. | `MetAbove`, `UnderminingOn`, `UnderminingAt` |
| return (回程) | A dependence holding at some step is satisfied again at some later step (or within `p` steps). | `Returns`, `RestoredWithin`, `RenewedWithin` |
| horizon (视界) | A finite prefix; two runs agree before it. | `Run.AgreeUpTo` |
| making a difference (差别制造) | With one side's part removed, the dependence is kept at every step with the same move (and that move is available). | `MakesDifference`, `Overdetermined` |
| interaction (交互) | One side draws on a condition on which the other depends at a positive level, at any step: `related` under the discipline of correspondence. | `Interacts`, `Web.interaction` |
| living on (以之为生) | In a reading of one kind, a formation at some step draws on a relatum and depends on it with positive need; under `Dependent` what it depends on stands as a condition at that step. | `Web.LivesOn`, `LivesOn.stands`, `Web.sustenance` |
| descent (世系) | In a reading of one kind, a relatum comes from a formation taking part at the step at which it comes to stand, if given by it. | `Flow.DescendsAt`, `Flow.Descends`, `Flow.descent` |
| transmission (传递) | Offspring inherit the parent's dependences with requirements at most δ more. | `Flow.TransmitsWithin`, `Flow.transmitsWithin_iff`, `World.transmitting_of_drawn`, `raised`, `lowered` |
| selection (选择) | Where only the active give and activity needs support, only supported formations leave offspring. | `unsupported_childless`, `selected`, `selected_le`, `selected_uniform` |
| alike / bisimulation (相同／互模拟) | Configurations related by a bisimulation realize the same claims and go by the same moves to configurations that are alike. | `Bisimulation`, `Alike`, `Alike.tests` |
| determined up to likeness (相同之下确定) | Any two outcomes of the same move are alike. | `DeterminedAt`, `DeterminedAt.transfer`, `Twins.alike_one` |
| holds its splices / live steps (含有拼接／活的步) | A family of histories contains every sequence made of its own steps; a law's live steps are those some history of it takes. | `SpliceClosed`, `family_iff`, `live`, `same_histories_iff` |
| possibly / necessarily drawn (可能／必然被吸入) | Some path / every run from the configuration enters a region the process never leaves. | `PossiblyDrawnInto`, `NecessarilyDrawnInto`, `necessarilyDrawn_iff_not_returns`, `possiblyDrawn_iff` |
| juncture (关节; 机, AI reading) | A configuration with a step after which a given configuration can still be had and a step after which it cannot. | `Branching.Juncture`, `Branching.loss_passes_juncture`, `Branching.lpo_of_junctures_found` |
| keeping / losing (护闭 / 成闭 at a juncture, AI reading) | The sub-process of the steps after which a configuration can still be had, and that of the others. | `Branching.keeping`, `Branching.keeping_greatest`, `Branching.losing_not_returns` |
| commuting law | A law `T` with `T (σ x) = σ (T x)` for every `x`. | `Law.Commutes`, `Law.Commutes.apart`, `Law.Commutes.breaks` |
| undecided (未定; the third value, 疑 in the earlier texts) | A value below true and false in information: what revision has not decided. | `Undecided.Value`, `Undecided.least_fixed`, `Undecided.undecided_of_moves` |
| description that makes sense (有意义的描述) | A description that identifies exactly the configurations that are alike. | `IdentifiesAlike`, `identifiesAlike_iff`, `IdentifiesAlike.carries` |
| rectangular whole / separated description (矩形的整体／分离) | Whatever goes with one part goes with every item of the other part. | `Rectangular`, `Separated`, `separation_faithful_iff` |
| one state, same ahead (同一状态) | Two moments of a history of values after which every value is the same. | `SameAhead`, `alike_moments_iff`, `finitely_many_states_iff` |
| gap / completing unfolding (缺口／补全的展开) | For a family of readings indexed by what it reads, the reading obtained by moving each member's value at itself through a map, which no member says. | `Diagonal.gap`, `Diagonal.gap_unsaid`, `Diagonal.Unfolds` |
| claims in context / gluing (语境中的主张／粘合) | Claims are shown in contexts. | `Contextual`, `Contextual.Glues`, `Contextual.glues_iff_agree`, `Contextual.fitsFree_iff` |
| parity system / contradiction (奇偶系统／矛盾) | Claims are listed, and each context is given the claims it counts and the parity it requires; an assignment meets a context where the values of the claims it counts have the required parity. | `ParitySystem`, `ParitySystem.Contradicts`, `ParitySystem.global_or_contradicts`, `ParitySystem.glues_iff`, `ParitySystem.mixture_le` |
| bound on states (状态数的界) | A history of values has at most N states: every moment is in the same state as one of the N moments before it; exactly where it is a lasso within N. | `StatesBelow`, `Identification.statesBelow_iff_lasso` |
| identification / extrapolation given the bound (辨识／给定界的外推) | A finite prefix fixes the whole course. | `Identification.prefix_fixes`, `Identification.withBound` |
| runs part (运行分开) | Two runs take one value through the map before some step and different values at it. | `Parting.PartAt`, `Parting.Unparted` |
| free branching (自由分支) | The process in which every configuration can be followed by every configuration; every course is the course of one of its runs. | `Parting.free`, `Parting.freeRun` |
| typical, by counting (典型) | A course whose squared deviation (q·a − p·b)² is less than d. | `Typicality.offBy`, `Typicality.typical` |
| extrapolation built from the process (依过程所建之外推) | Reads off the prefix the configurations the run may be at, takes the first from which it can go on without end, and proposes its value through the map. | `Parting.fromProcess`, `Parting.world_right_iff` |
| situation, of a step (情境) | One way of taking a step; with it as the move the law is determined. | `Situations.finerLaw`, `Situations.finer`, `Situations.situations_of_course` |
| arising recurs / ceasing recurs (生起复现／止息复现) | Some relatum arises / ceases at arbitrarily late steps. | `World.ArisingRecurs`, `World.CeasingRecurs`, `World.arising_iff_ceasing`, `World.law_decides`, `World.law_iff_em` |
| stopping unrefuted (停止不能被否证) | That something stops from some step on cannot be refuted; equivalently, it is not the case that after every step a later occurrence cannot be refuted (`stop_unrefuted_iff`). | `stop_unrefuted_iff`, `falls_stop_unrefuted`, `amount_still_unrefuted`, `Web.embodiedArising_stops_unrefuted`, `Flow.change_stops_unrefuted`, `World.comes_to_rest_unrefuted_from` |
| net giver / gain (净给予者／增益) | A relatum taking part across a step that gives the family more than it takes from it. | `Flow.NetGiver`, `Flow.rise_netGiver`, `Flow.rise_given`, `Flow.rise_from_rest_or_open` |
| law of transmission (传递律) | With no premise: the offspring's total plus what transmission lowered equals the parents' amounts weighted by their numbers of offspring plus what transmission raised. | `price` |
| bearing (承担) | Depending at a positive level on a condition that can fail it. | `Bearing` |
| idle condition (惰性条件) | A condition no activity draws on, or on which no dependence can fail. | `Idle` |
| formation event (形成事件) | (formation, step): the claims of the whole-run and stepwise readings. | `F × Nat` |
| relation, at the level of readings (关系) | (formation, condition, step): the claims of the relation-level readings. | `Web.relations` |
| valuation (评价) | Living, relation, region, significance. | `Valuation` |
| own region (自身区域) | The region of formed relations; not an owner. | `own` |
| seed (种子) | Some living claim has significance from some standpoint. | `Seed` |
| self-significance | A standpoint's own living continuation has significance for it; read as wanting one's continuation (§6.2). | `Valuation.SelfSignificance` |
| relational neutrality / standpoint neutrality | Significance passes along every formed relation to living content / what has significance from one standpoint has it from every standpoint. | `Valuation.transmits` / `Valuation.shares` |
| held (持有) | A living claim lies in some standpoint's own region. | `Held`, `Unheld`, `significant_iff_held` |
| center (中心) | Whose continuation counts. | `SelfSignificance` (self-significance), `shares` (standpoint neutrality) |
| a part withheld (扣留一个部分) | The part (a formation or a system) neither takes nor gives, and the rest of the exchange goes on as before. | `Flow.withhold`, `Flow.WithheldLevels`, `Flow.Balances.withheld` |
| includes / exceeds (包含／超出) | One path of levels admits at every step every formation the other admits / at some step admits a formation the other does not. | `Web.Includes`, `Web.Exceeds` |
| within / beyond a region (区域之内／之外) | Within a region of formations, these levels admit every formation those levels admit / beyond the region some formation is admitted by those levels and not by these. | `Web.AdmitsWithin`, `Web.LosesBeyond`, `Web.not_losesBeyond_whole` |
| retains / adds (保留／增加) | From a standpoint, one path of levels admits every significant continuation the other admits / admits a significant continuation the other does not. | `Web.Retains`, `Web.Adds` |
| preemption (先占) | Taking a condition away before any dependence on it forms: not undermining on the stepwise reading, yet closing off formations that could form later. | `Preemption.not_undermining_yet_loses` |
| closure (闭包) | One formation lies within another's closure under a relation: every region containing the latter and closed under the relation contains it. | `ClosedUnder`, `WithinClosure` |
| selector (选择者) | The formation, or group of formations taken together, whose couplings fix a selection; taken as what actually couples into it. | `Web.SelectsThrough`, `Web.SelectsThroughAll`, `Web.SelectsThrough.widen` |
| gap, of selection (缺口) | The candidate's reach closure less the selector's coupling closure. | `Clearing.dweller_within_reach`, `Clearing.unselected`, `Clearing.selected_pooled`, `Diversion.favours` |
| exclusion (排除) | No history satisfying the claim is alike with the actual one through the formation's couplings up to some step. | `Web.Excludes`, `Web.ExcludesWithin`, `Web.excludesWithin_iff_conjunction` |
| course / prefix (经映射的历程／前段) | A sequence of values, for example a determined law's orbit read through a map; the prefix is the values before step t, latest first. | `prefixOf`, `back_prefix` |
| extrapolation by elimination (逐除外推) | Candidates are put in order, and the extrapolation moves to the next exactly where the one it holds misses. | `indexOn`, `byElimination`, `index_le_of_accords`, `missed_before` |
| lasso (套索) | A sequence that repeats periodically from some step on: exactly the course, through a map, of a world a list holds. | `Lasso`, `lasso_of_held`, `lasso_realized`, `lasso_byElimination_bounded`, `rest_unrefuted` |
| diagonal course (对角序列) | A sequence that at every step answers the extrapolation's proposed value so that it misses. | `diagonal`, `diagonal_misses`, `diagonal_open` |
| merged enumeration, at the meta level (合并枚举) | Classes of candidates merged along pairs into one enumeration. | `merged`, `merged_bound`, `merged_unrested` |
| subthreshold (阈下) | A condition coupled in by threshold only passes only whether the requirement is met. | `Web.alike_of_threshold`, `Flow.subthreshold_alike`, `Flow.difference_changes_after_divergence` |
| experiment (实验) | Varying one's own move where the configuration (as the experimenter reads it) returns. | `Run.Fixes`, `Run.fixes_of_takes`, `Run.not_fixes_of_untaken`, `Run.fixes_on_return` |
| control (对照) | The model that what differs between two occasions is irrelevant to the change: the steps factor, through the reading, into a determined process. | `FactorsThrough`, `Run.generalizes`, `Confound` |
| description / carries a law (描述／承载规律) | A projection π of configurations is a description. | `GoAlike`, `Image`, `carries_law_iff`, `image_determined_iff` |
| lumping / generalization (归并／推广) | A function π of inputs. | `Lumped`, `Determines`, `determines_lumped_iff`, `lumped_right_iff` |
| free, beyond the data (自由) | Every member's values on the data combine with every member's value at x. | `Free`, `free_determines_iff`, `every_determines_nothing` |
| training (训练) | Selection through the data: functions agreeing on the data are selected alike. | `Training.Through`, `Training.loss_through`, `Training.fit_right_iff` |
| depends only on / re-absorbed (只依于／重新吸收) | The next configuration depends wholly on π; then differences of the starting point outside π vanish within one step. | `DependsOnlyOn`, `DependsOnlyOn.reabsorbed`, `Law.reabsorbed`, `Law.perturbation_reabsorbed` |
| adaptive system (改变自身规则的系统) | The state goes on under the rule, and the rule itself goes on too: one determined process on the joint configuration. | `adaptive`, `adaptive_state_law_iff`, `Run.steps_by_rule`, `Switching` |
| intervention / noise (干预／噪声) | In the standard model x′ = F(x, u, ε), an intervention is a move not taken, fixed by the model and not by the record; noise is a move not represented, and forgetting it the process stays determined exactly where the noise makes no difference. | `inputs`, `inputs_intervention_unfixed`, `inputs_model_fixes`, `forget_inputs_determined_iff` |
| enough (够) | A goal is met at a state the unfolding leaves unchanged. | `Law.rests_iff`, `Law.fixed_rests` |
| hijacking (劫持) | An AI reading: a goal formed by a selection that rewards what cannot rest, and kept by the rules the winners write. | `share_rises`, `Law.perturbation_reabsorbed` |
| what a part reaches (部分所及) | The part's members exchange with a condition a formation depends on; reaching before a step is exchanging, at an earlier step, with a condition it requires at that step. | `Flow.Reaches`, `Flow.ReachesBefore`, `Flow.Balances.comparison_within_reach` |
| responsive reach (回应所及) | The part's closure, between two flows, under being affected through what couples in: a member exchanges in one of the two flows with a condition coupled into another formation, which exchanges with one coupled into a third, and so on link by link. | `Flow.WithinResponse`, `Flow.withinResponse_iff_coupling`, `Flow.withinResponse_thresholdOnly_iff`, `Flow.Balances.comparison_within_response` |
| responds through the couplings (经耦合而应) | Every formation outside the part through whose couplings the two flows are alike up to a step exchanges alike at that step in the two flows. | `Flow.RespondsThroughCoupling`, `Flow.respondsThroughCoupling_withhold` |
| law of exchange / reads what has stood (交换律／读已立者) | Reads off the history of levels how much each formation takes from and gives to each condition at each step. | `ExchangeLaw`, `ExchangeLaw.Nonanticipating`, `Flow.Follows` |
| sensitive (敏感) | A formation's exchange is sensitive to a condition: changing only that condition's level at some step changes what it exchanges. | `ExchangeLaw.Sensitive`, `ExchangeLaw.ReadsFinitely.through_sensitive`, `ExchangeLaw.Nonanticipating.through_sensitive`, `ExchangeLaw.Through.couples_of_sensitive`, `tailLaw_no_least_coupling`, `wlpo_of_not_through_sensitive` |
| reads finitely many conditions (读有限多个条件) | At every step, for every formation and under every history, the law's exchange is fixed by the levels, up to that step, of some finite list of conditions, and the list may vary with the history (continuity). | `ExchangeLaw.ReadsWithin`, `ExchangeLaw.ReadsFinitely`, `ExchangeLaw.ReadsFinitely.nonanticipating`, `Pointer.no_list` |
| changed by no condition, a whole and no part (没有一个条件改变) | A number read off levels that is the same for levels differing in one condition only; exactly one that is the same for levels agreeing from some condition on, fixed by the tail alone. | `ChangedByNoCondition`, `ChangedByNoCondition.eq_of_agree_from`, `wholeLaw`, `wholeLaw_no_least_coupling` |
| rule deciding false throughout (规则) | Decides, of every Boolean sequence, whether it is false throughout: the weak limited principle of omniscience as a rule, which gives `WLPO`. | `changedByNoCondition_iff_rule`, `not_through_sensitive_iff_rule`, `WLPO.of_rule`, `vanishDecision_iff_lpoRule` |
| coupling strength (耦合强度) | A formation's exchange with a condition is coupled at a step to a condition's level with strength at most k: under two histories differing only in that level, the differences in what is taken and given add up to at most k times the difference of the level. | `ExchangeLaw.RespondsWithin`, `ExchangeLaw.insensitiveAt_iff_strength_zero`, `ExchangeLaw.exchangeGap_le_strengths`, `ExchangeLaw.exchangeGap_le_shares`, `Propagation.Square.not_respondsWithin` |
| order, of the carried amount (阶) | What routes of at most j responses carry: what the strengths do to the next order. | `carriedWithin`, `carriedFrom`, `carriedWithin_exact`, `carriedWithin_exact_of_no_loop`, `carried_le_carriedWithin_add` |
| what a cut loses (截断所失) | What of the carried amount is not carried when cut at order j: exactly what j + 1 responses in turn carry from the carried amount. | `responses`, `carried_eq_carriedWithin_add`, `responses_antitone`, `carriedWithin_lt_iff` |
| chain of couplings in time order (按时间次序的耦合链) | A chain in which each coupling reads the level after the previous coupling has arrived. | `CoupledIntoBy`, `exact_every_start_iff`, `finite_order_iff_bounded` |
| settled, of a schedule of couplings (安定) | Every coupling from some step on recurs. | `SettledFrom`, `strengthsFrom`, `CouplingRecurs`, `finite_order_iff_no_loop_from` |
| route back in time (沿时间往回的路线) | From a condition's level at some step back, one response per step to an earlier level, with the level held in between, or ending at a source. | `RoutePoint`, `routeWeight`, `routeSum`, `routeSum_eq_carriedWithin`, `carried_eq_courses` |
| closing, the formation of a loop (闭合) | The loops formed by a step are the loops of the couplings acting before it. | `strengthsBefore`, `onLoop_iff_formed`, `onLoop_succ_iff`, `forms_by_closing`, `responds_to_own_level` |
| what a law reads, a schedule (律所读) | For every formation outside the part, the law gives alike under histories agreeing on the marked conditions. | `ExchangeLaw.ReadsAt`, `restrictReads`, `ExchangeLaw.ReadsAt.respondsWithin_unread`, `couples_reads`, `onLoop_succ_reads` |
| break, of a stock read only below a threshold (断裂) | Where the stock stands at the threshold, the law reads only that it stands. | `ExchangeLaw.ReadsBelow`, `ExchangeLaw.standing`, `break_carried_nowhere`, `ExchangeLaw.ReadsBelow.standing_no_loop`, `Thresholds.Draw` |
| reading into, each condition, a schedule (读入) | A formation's exchange with a condition is fixed only by the levels marked for that condition. | `ExchangeLaw.ReadsInto`, `readCouplings`, `restrictInto`, `ExchangeLaw.ReadsAt.readsInto` |
| downstream, of a stock's difference (下游) | The conditions reachable from the stock by routes of reading formed by some step. | `Upstream`, `conveyed_upstream`, `apart_only_downstream`, `upstream_succ_iff`, `Observation.Measure` |
| return, around a loop (返回) | A chain of couplings in time order from a condition back to it: the first coupling reads the level from the starting step, and each later one reads the level after the previous one acted. | `ChainInTime`, `Returns`, `carried_doubles_roundTrip`, `carried_roundTrip`, `runaway_of_roundTrip` |
| how often couplings act (耦合的频度) | The count a of steps at which some coupling acts. | `Frequency.count`, `Frequency.coupling`, `carried_le_count`, `carried_le_of_rare`, `Frequency.SelfLoop.polynomial_iff` |
| recurs or stops (复现或停止) | The dichotomy that, for every decided two-place family, either every row is true somewhere or some row is false throughout. | `RecursOrStops`, `StopsBy`, `settled_iff_recursOrStops`, `settled_every_iff`, `lpo_of_settled` |
| counterfactual, of a course (反事实) | The course the same law of exchange generates where the part acts otherwise. | `counterfactual_fixed`, `ExchangeLaw.course_balances_iff`, `counterfactual_is_course` |
| boundary of a self (自身的边界) | Along a relation, a region containing the formation and closed under the relation; the closure is the least, the whole the greatest. | `Boundary` |
| super-true / sub-true (超真／次真) | Holds however the boundary is drawn among the admissible ones / holds under some way of drawing it; taken from supervaluation (Fine 1975) and subvaluation (Hyde 1997). | `SuperTrue`, `SubTrue` |
| positive relevance read from significance (从意义读出的正面相关) | Realized living content whose continuation has significance from every standpoint. | `Frame.relevance`, `livingSignificance_of_unrestricted`, `relevance_least` |
| possibility reading (可能性读法) | Counts a formation where a continuation's levels admit it, active or not. | `Ranking.possible`, `Ranking.possible_extends_iff` |
| possibilities first (可能性优先) | Compare possibilities first, then the events a reading counts. | `Ranking.possibleFirst`, `Ranking.Pause.pause_ranked_below` |
| renewing over a region (在区域上更新) | Active, and the step keeps every dependence on every condition it takes part in within a region of conditions. | `Web.RenewingOver`, `Web.RenewingOver.at`, `Web.RenewingOver.keeps_own` |
| boundary neutrality (边界中立) | The rule is limited by no formed boundary. | `Neutral` (contrast `Within`) |
| connected (连通) | Living claims are linked through formed relations. | `Connected` |
| contributory reason (支持理由) | A reason supporting a response; not an obligation or a ranking. | `Reason` |

<!-- tail -->
<a id="retired-labels"></a>
### (c) Retired labels and Lean names

Earlier records, studies, sources and Lean docstrings use the labels below. They keep them as history; this chapter uses the current terms, and Lean names are unchanged except those of the next two tables. This table is the only place in the chapter that explains the old labels.

| Retired label | Current term | Lean name |
|---|---|---|
| G0 | living significance: every living claim has significance from every standpoint (on a frame, realized living content falls under the relevance read from significance) | `LivingSignificance`, `Valuation.Significant`, `livingSignificance_of_unrestricted` |
| S0 | self-significance | `Valuation.SelfSignificance` |
| N_rel / N_std | relational neutrality / standpoint neutrality | `Valuation.transmits` / `Valuation.shares` |
| the one axiom; Ren's proposed axiom | the continuation condition, stated in §6.4 and not asserted | `Unrestricted` |
| G0/J route; G0 axiom route; explicit axiom route | the conditional alignment route: living significance with the practical commitments (§7) | — |
| J1–J4 | the practical commitments | `PracticalJudgment`, `BetterAt` (periphery, superseded); now `Lexical.BasicPriority` and `Requirement.Frontier`, on frames `FrontierFrames.Priority` |
| Part I; Part I stated whole | the theory without axiom; the theory stated whole | — |
| Part II | the conditional section, §6.4 | — |
| Universal Metaethical Core | section 6, Significance, comparison and practical judgment | `Becoming.Metaethics` |
| folding (of G0, of Part II) | the restatement of an axiom as a condition (dated note in §6.4) | — |
| 归于静止, 静止定理 (Chinese terms for coming to rest and the rest theorem) | 停息, 停息定理 (D45, 19 October 2026) | — |


**Retired Lean names (18 October 2026).**

On 18 October 2026 the Lean names that carried "registration" and the learning vocabulary of a knower facing an external world were renamed by the vocabulary the [naming study](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/REGISTRATION-VOCABULARY-STUDY.md#8-applied-n5-18-october-2026) adopted (couples into, alike through, excludes, prefix, misses and accords, extrapolation by elimination). The statements and proofs are unchanged. The definitions are below; the theorem names follow them (for example `Web.RegistersAlike.trans` is `Web.AlikeThrough.trans`, `Learning.record_length` is `Learning.prefix_length`). The full table of 175 declarations is [RENAME-TABLE.json](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/development/n1-migration/RENAME-TABLE.json). Earlier studies, sources and receipts keep the old names as history. The prose words of this chapter were then changed by reading, not by this renaming (N6): registration closure is the coupling closure, selection through registration is selection through the couplings, responds through registration is responds through the couplings, contextual registration is claims in context, refutation (of a claim at a formation) is exclusion, course / record is course / prefix, learning by refutation is extrapolation by elimination, the learner given the bound or the world is the extrapolation given the bound or built from the process. 识 is kept for a formation's own course through the lumping its couplings make.

| Retired Lean name | Current Lean name |
|---|---|
| `Web.Registers` | `Web.CoupledInto` |
| `Web.RegistersAlike`, `…UpTo`, `…All` | `Web.AlikeThrough`, `…UpTo`, `…All` |
| `Web.Belief` | `Web.ClassThrough` |
| `Web.Refutes`, `…Within`, `…By` | `Web.Excludes`, `…Within`, `…By` |
| `Flow.RegisteredFrom`, `…Either`; `Flow.WithinRegistration` | `Flow.CoupledFrom`, `…Either`; `Flow.WithinCoupling` |
| `Flow.RespondsThroughRegistration`; `TimedResponse.RegistersAt` | `Flow.RespondsThroughCoupling`; `TimedResponse.CoupledIntoAt` |
| `supportOnly` | `thresholdOnly` |
| `Registers` (Likeness) | `RespectsClaims` |
| `Law.registered` | `Law.frameBy` |
| `Learning.record`; `recordThen` | `Learning.prefixOf`; `prefixThen` |
| `Learning.Refuted`, `Learning.RefutedAt`; `Learning.Holds` | `Learning.Misses`, `Learning.MissesAt`; `Learning.Accords` |
| `Learning.learner` | `Learning.byElimination` |
| `Learnable.withWorld`, `…At`; `Parting.worldLearner` | `Learnable.fromLaw`, `…At`; `Parting.fromProcess` |
| `Viability.Answering.registers`; `Viability.Matching.registered`, `…blind` | `Viability.Answering.keeps`; `Viability.Matching.keepsBit`, `…keepsNothing` |
| `Negation.register`; `Revising.registration`; `ReferencePlan.registered` | `Negation.course`; `Revising.linkProcess`; `ReferencePlan.alikeOnInstalled` |

**Retired Lean names (20 October 2026).**

On 20 October 2026 (board item R30, one notion, one name) the declarations whose name stated a meaning the statement does not have, or collided with another declaration's name, were renamed by one table: 336 declarations (199 of them members moved with their namespace), 11 namespaces and 4 modules, with the binder `positive` read as relevance. The statements and proofs are unchanged; there are no aliases. The rows below give the definitions and families; the theorem names follow them (for example `Web.generation_opens` is `Web.embodiedArising_opens`, `g0_of_unrestricted` is `livingSignificance_of_unrestricted`). The full table, with each reason and the rows judged and left, is [RENAME-TABLE.json](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/development/r30-names/RENAME-TABLE.json). Kept by decision: `World.RestsFrom` and `Enough.RestsFrom`, `Enough.Settles` (停息 and D42), `Narrowing.Settles`, `GuardHorizon.Closed`, `Branching.Keeps`, the witness `Generations` and Slowing's event names. Earlier studies, sources and receipts keep the old names as history; the prose words (generation, return, rest, free rider) change by reading, not by this renaming.

| Retired Lean name | Current Lean name |
|---|---|
| `Web.Returns`, `…Within`; `Becoming.Return` (module) | `Web.Restored`, `…Within`; `Becoming.Restoration` |
| `Returns` (Frequency); `carried_returns`, `runaway_of_returns` | `RoundTrip`; `carried_roundTrip`, `runaway_of_roundTrip` |
| `Flow.Lossless`, `…On` | `Flow.Conserving`, `…On` |
| `HistoryIdeals.Settles`; `Stretches.Settles` | `HistoryIdeals.HasLongest`; `Stretches.HasLatest` |
| `Learnable.RestsFrom`, `…Rests`; `LearnableRuns.RestsFrom`, `…Rests` | `Learnable.PredictsFrom`, `…Predicts`; `LearnableRuns.PredictsFrom`, `…Predicts` |
| `Ranking.Rest` | `Ranking.Pause` |
| `Ideals.Closed` | `Ideals.ScottClosed` |
| `ReferencePlan.Alike`; `Contacts.Alike` | `ReferencePlan.AgreeOn`; `Contacts.AgreeOn` |
| `Becoming.Generation` (module); `Web.generation_*`; `Web.Regenerating` | `Becoming.Arising`; `Web.embodiedArising_*`; `Web.ActiveRenewer` |
| `ExchangeLaw.generation`; `SharedCodes.generation`; `ResponseLearning.*generation*` | `ExchangeLaw.process`; `SharedCodes.nextCohort`; `ResponseLearning.*cohort*` |
| `G0`, `g0_*` | `LivingSignificance`, `livingSignificance_*` |
| `SecuresPositiveGround`; `Becoming.PositiveGround` (module and namespace); `contingent_generation*`, `Handoff.generation_by_bound*` | `SecuresNewContent`; `Becoming.SecuredContent`; `contingent_newContent*`, `Handoff.newContent_by_bound*` |
| the binder `positive` (the relevance read from significance) | `relevance` |
| `Valuation.SelfGood`; `ProfileReach.SelfGood` | `Valuation.SelfSignificance`; `ProfileReach.SelfSignificance` |
| `Becoming.Coupling` (module and namespace) | `Becoming.MoveFormation` |
| `Onward.DependentSelection`, `runs_iff_selection` | `Onward.DependentChoice`, `runs_iff_dependentChoice` |
| `Joining.Neutral` | `Joining.TwoSidedUnit` |
| `Clearing.free_rider_loses` | `Clearing.clearer_loses_dweller` |
| `RuleCapture.Counts`; `Countdown.Counts` | `RuleCapture.CarrierCounts`; `Countdown.CountedWork` |
| `SharedCodes.Image` | `SharedCodes.Relabels` |
| `Activation.History`; `Registration.History`; `Flow.history` | `Activation.TwoSteps`; `Registration.AlikeUpTo`; `Flow.exchangeCount` |
| the witnesses `Crossing`, `Arising`, `Halving` (Order), `Cycle` (Gluing), `Loop` (Weighted), `Copying` (Pace), `Settling` (Entropy), `Parting` (Likeness), `Fork` (Identity), `Circulation` (Labelled) | `Order.Crossing`, `Order.Arising`, `Order.Halving`, `Gluing.Cycle`, `Weighted.Loop`, `Pace.Copying`, `Entropy.Settling`, `Likeness.Parting`, `Identity.Fork`, `Labelled.Circulation` |

<a id="crosswalk-to-the-corpus-glossary"></a>
### (d) Crosswalk to the corpus glossary

The root [GLOSSARY.md](../../../GLOSSARY.md) is the vocabulary of the whole corpus, with provenance marks and dated first uses; it has no entries for the spine's formal terms. The terms below appear in both. Each row gives the corpus sense in brief and how it stands to the terms above. The corpus entry remains the source for its sense and provenance, and the relations stated here are the AI's reading, not a ruling by Ren. Where the two senses differ, they are not to be merged.

| Term (Chinese name) | Corpus sense, and its relation to this chapter | Lean anchor |
|---|---|---|
| 生生不息 (shēngshēng bùxī) | Ren's reading of the inherited phrase: the source of further generation is unexhausted and the way of transformation unsealed; not the persistence of any form, nor rising complexity or growth. The corpus breaks it into 生 (a possible structure entering actuality), 生生 (that entry also preserving, restoring or creating the next round's conditions and generators) and 不息 (the pattern keeps being realized again through metabolism, death and transmission). This chapter's 生生 is the object of the ethical direction. The chapter reads 不息 as arising that recurs through renewal and 生生不息 as 生生 going on at the whole with more still able to form, so return into copies of existing forms falls short (D5). The formal `Unceasing` ("unceasing arising") is much weaker: some formation arises at arbitrarily late steps. | none; compare `Unceasing` |
| 成生 / 绝生 (generative / degenerative) | Ren's act-level test: does an act preserve, restore or extend the affected party's capacity to keep perceiving, acting, relating, correcting and generating, or close it. The corpus's "destructive" became "degenerative" on 28 April 2026 (Ren's correction): destruction can serve further generation, as decomposition and succession after a death do, so "destructive" would misclass them. This chapter's "generative / degenerative" row formalizes the part-level widening and narrowing of what can form (D2). | `Web.Widens`, `Clearing.narrows` |
| 开 (open) | Ren's process-state with four conditions holding together (未, 可, 应, 转: an unexhausted domain remains, becoming is still reachable, it can still respond, it can still revise and transform); explicitly not a quantity. This chapter's "openness" is narrower and different: exchange beyond every finite family. The two must not be identified: openness is the mark 未 only, and the crosswalk below places each of the four marks. | none; compare `World.arising_opens` |
| 闭 / 成闭 (closure / achieved closure) | Ren's typed closure, in which closure as such is not evil; 成闭 is closing that does not reopen, which the corpus names bad. The nearest formal terms here are lock-in and being drawn in (what is drawn in never comes back). They state the dynamics only and carry no valuation. The crosswalk below places the whole typology. | none; compare `Law.DrawnInto.never_back`, `Run.locked_in` |
| possibility space (可能性空间) | Ren's: not the number of options but whether genuinely different futures remain materially reachable. Here the possibility reading counts what can form next, and widening compares paths of levels by inclusion. Reading possibility as what can form next adds no premise, since it compares what the levels admit (row "generative / degenerative"; D1). | `Ranking.possible`, `Web.Widens` |
| 理 (lǐ) | In the corpus's 化/理 dual, the invariant of a trajectory, both pattern and type. Ren's reading of 12 October 2026, used here, is the modeling of the laws of structure and change (row 理 above). The two senses differ; the corpus also holds 道含理，理不含道 (the Way contains pattern, pattern does not contain the Way). | `Lumped`, `goAlike_iff_lumped` |
| 道 (dào) | Inherited, used in the corpus in three registers that are not to be merged: compass, formal predicate, and algebra. This chapter defines no formal 道. | — |
| 善 / 恶 (the good / evil) | Ren's: the good does not lie in maximizing anything but in what one does not close; evil is the knowing conversion of a shared condition into capture, closure that does not reopen. This chapter states no formal predicate for either; its ethical direction is living significance under the condition of §6.4 (§6, §7). | — |
| 智 (zhì) | Ren's: the capacity to stay in contact with reality; capability and optimization power are not intelligence in this sense. This chapter's open target "the core as the root of wisdom" (§8.1) concerns wisdom, which is related but not the same. | — |
| point of enough | Ren's line that growth is bounded by need: "the problem is the mind not the approach". The nearest formal term is enough: a goal met at a state the unfolding leaves unchanged, at which seeking rests. | `Law.rests_iff` |
| meta-attractor (元吸引子) | The corpus's self-reinforcing pattern that gains power over the rule by which states are selected. Its valence varies across texts, as the corpus entry records. The nearest formal terms here are hijacking (a goal kept by the rules the winners write), re-absorption under a rule, and runaway. | `share_rises`, `Law.perturbation_reabsorbed` |
| relational self (关系之我) | Ren's: a self is what a knot of relations is doing at a place, an action center formed by relations gathering. Here a center is a formation in the dynamics, and the boundary of a self is drawn along a relation, from its closure to the whole. | `Boundary`, `own` |
| 位 / 际 (locus / relation) | The structural dual of the 間 project: a locus is exhausted by its relations. Here formation and condition are two roles of one relatum, and relations are read at the level of readings. | `Web.roles`, `Web.relations` |
| Yi (一) | Ren's one primitive, of which subject, object, container and agent are roles read off context facts. The nearest term here is roles: formation and condition as two roles of one relatum. | `Web.roles` |
| lineage (相续) | In the context runtime, the parent-child path through the moment graph in which identity lives. This chapter's succession and lineage (接续) join a formation that ends with one that begins; the senses are related but not the same. | `Lineage`, `Succession` |
| membrane (膜) | Ren's self-managed boundary that admits, exchanges and can be corrected through, unlike a wall. The nearest formal terms are a cut (no formed relation leaves a region) and being fed from beyond. | `Cut`, `FedFromBeyond` |

The corpus glossary records that three closure vocabularies (成闭/护闭/元闭/伪开, 成生之限/绝生之限, and English "close / keep open") circulated without a crosswalk. The next subsection gives it.

<a id="closing-and-opening-a-crosswalk"></a>
### (e) Closing and opening: a crosswalk

The earlier texts type closure and define openness in the 间生论 ([§四 开闭](../../../sources/07-shengsheng-buxi/ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/06_四、开闭.md)), in its first supplement ([§十 开闭 and §十一 伪开三型](../../../sources/07-shengsheng-buxi/ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/04_卷三_判准.md)) and in the treatise's main text ([卷六 开、闭、稳、真](../../../sources/07-shengsheng-buxi/ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/08_卷六_开、闭、稳、真.md)). The two tables below place each type of closure and each mark of openness on landed laws of the spine, and place the other two vocabularies with them. Two things in the earlier definitions are left out. One is the openness of each focus (开 indexed by a focus, with the measure O_F = Ω(U, A, R, T) and a threshold), which distributes openness over separate owners. The other is the verdict written into the definitions: 成闭 named evil, 护闭 the middle, 伪开 a deceit. Only the structure is mapped: how a course goes on, comes back, is drawn in or responds. Whether a closing supports, enriches or damages 生生 is for the comparison to say under the condition of §6.4 (row generative / degenerative, D2), not for the type. The correspondences are the AI's readings ([D49](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#d49-闭与开的对照九句的归与不归--closing-and-opening-on-the-spine)), first proposed in the [review of the earlier repository](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SSBX-REPOSITORY-REVIEW.md), §2.

**Closure.**

| Earlier term | Structure on the spine | Lean anchor |
|---|---|---|
| 闭 (closure), in general | The negation of 开 below: none of 未, 可, 应 and 转 remains. Closing as such is a region the law never leaves (an absorbing region; under a process, an invariant), and every determined law draws in exactly the configurations that do not return. What returns is itself an absorbing region, so a closed region can hold what is kept, and closing is not a loss by its form. This is the structure of the corpus's "closure as such is not evil". | `Law.Absorbing`, `Law.drawn_iff_not_returns`, `Law.returning_absorbing` |
| 成闭 (achieved closure: 闭而不复开) | Lock-in. What is drawn into an absorbing region never comes back, and a drawn configuration never returns. What can be had n steps on is an absorbing region, and every possibility lost by step n is drawn into it. Under every process, once inside an invariant region, what lies outside cannot be had again. | `Law.DrawnInto.never_back`, `Law.Drawn.not_returns`, `Law.lost_drawn`, `Invariant.locks_out`, `Run.locked_in` |
| 护闭 (protective closure: 暂闭一处以护更大之开) | Removing, where the course branches, the steps after which a configuration can no longer be had, so that it stays reachable. Proved as keeping at a juncture (`Becoming.Junctures`, D52; §1, “Where a configuration is lost”). A configuration is a juncture for s where s can be had again from it and it has both a step after which s can be had again and one after which it cannot. Where s returns, every loss of s passes through a juncture (in double-negation form; as existence where the configurations are enumerated and the steps decided), and keeping only the steps after which s can be had again keeps s and is the largest sub-process that does on its course from s. Also landed: a configuration possibly drawn in can return on another course, and leaving an invariant region needs a move that does not keep it. Read so, 护闭 and 成闭 are one operation at a juncture, removing the losing steps or the keeping ones, and neither carries a valuation. Which configuration is worth keeping (a membrane, refusing an assault, isolating a contagion, in the earlier examples) is not in the law. | `Branching.Juncture`, `Branching.keeping`, `Branching.keeping_greatest`, `Branching.keeping_removes_at_juncture`; compare `Branching.possiblyDrawn_iff`, `Branching.OneWay.possibly_not_necessarily`, `Run.leaving_needs` |
| 元闭 (meta-closure: 生间之法源冻结) | A rule that holds the outcome (`Becoming.Capture`). Where the rule keeps itself, the configurations with a given rule are a region the law never leaves. Where the next configuration depends on the rule and not on the state, perturbing the state alone is drawn back into what the rule holds, and from the next step on the course is as if it had not been perturbed; perturbing the rule changes the outcome. So a lasting change, and a counter-loop, has to reach the rule (§4, §7.3). Where the rule is itself read from the share the selection gives, its value is re-set at every reading step, and what holds the outcome is how it reads: a change of the value alone is absorbed where it keeps the direction, and only a change of the reading leaves (`Becoming.RuleCapture`, §4). | `Law.rule_absorbing`, `Captured.state_perturbation_drawn`, `Law.perturbation_reabsorbed`, `Captured.rule_perturbation_drawn`, `RuleCapture.perturbation_absorbed`, `RuleCapture.uniform_locks` |
| 伪开 (pseudo-openness: 外显为开，内成其闭) | Openness read off a part, a stretch or the state that the whole course does not have. The three types below are three places where such a reading is taken. The earlier capture (夺: one focus's openness rising as the others' falls) is stated through the openness of each focus and is not mapped; capture as a selection is the row hijacking. | the three rows below |
| 伪开 I: 局部开，整体闭 (open at a part, closed at the whole) | What holds at a part does not decide what holds at the whole. Each formation can take within what the step gives it while together they take more. Where renewal depends on what it renews, joint excess that brings the level below a need ends the renewal and every formation depending on the condition at that need, the takers included (`Becoming.Continuation`). A part of the configuration can carry a law that the whole does not (`Coarse`), and a whole can have a law that no reading of its state alone has (`Switching`). | `Pair.own_not_joint`, `Flow.joint_excess_ends`, `Coarse.carries`, `Switching.no_state_law` |
| 伪开 II: 短期开，长时闭 (open over a short horizon, closed over a long one) | No finite stretch decides the class of a run. For every horizon, two runs agree up to it, with every event of the focal formation there within renewal in both, and then one renews over the whole run while the other consumes (`Becoming.Horizon`). Before a break, where a stock couples into a formation by threshold only, nothing that couples into the formation bounds how near the break is (`Becoming.Runaway`). | `Renewable.prefix_does_not_decide`, `Web.break_not_bounded` |
| 伪开 III: 表层开，元间闭 (open at the state, closed at the rule) | 元闭 seen from the state. The state can change and can be perturbed, and every perturbation of it alone is drawn back into what the rule holds; only a change that reaches the rule changes the outcome. | `Law.rule_absorbing`, `Captured.state_perturbation_drawn`, `Law.perturbation_reabsorbed` |
| 成生之限／绝生之限 (limits that build and limits that foreclose; [corpus glossary of September 2026](../../../_process/history/2026-09-consolidation/GLOSSARY.md)) | A limit restricts steps. A limit that forecloses (in the corpus's examples, monopolizing the entrance, eliminating alternatives, keeping latecomers dependent on one controller) is a 成闭: what it encloses cannot leave, and what lies outside cannot be had again. A limit that builds (a promise, training, stopping an assault) restricts some steps while what it restricts can still be had, the structure of 护闭. Which of the two a limit is depends on what it does to what can be had again, not on its name. | as 成闭 and 护闭 |
| close / keep open (English) | The corpus's English for 闭 and 护开. They take the rows above and the marks below. This chapter's "openness" is another term (row openness) and corresponds to the mark 未 only. | — |

**Openness.** The earlier texts define 开 as four marks holding together: 未 (an unformed domain remains), 可 (becoming remains possible), 应 (response remains possible) and 转 (revision, return and turning remain possible), with “开之四相不可缺一” and “开非更多，闭非更少” ([间生论 §四](../../../sources/07-shengsheng-buxi/ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/06_四、开闭.md)).

| Mark | Structure on the spine | Lean anchor |
|---|---|---|
| 未 (an unformed domain remains; the open dimension, 开维) | More can still come. In a world with a census whose relata are embodied and whose flow balances and dissipates, arising without end is incompatible with every step from some step on being enclosed. Under the first law, where a family is new at every step, every bounded family holding it is given more than it takes, by the rest or across its boundary, at arbitrarily late steps. This chapter's openness is this mark. | `World.arising_opens`, `Flow.new_beyond_every` |
| 可 (becoming remains possible) | A course goes on. Within finitely many configurations, a run starts at a configuration exactly where a course as long as the list does, with no decision and no selection. | `Onward.run_iff_continues` |
| 应 (response remains possible) | An exchange responds to a level: two histories differing at most in that level give a positive gap in the exchange (`Becoming.LevelCoupling`). Coupling bounds a response without fixing it. | `ExchangeLaw.RespondsTo`, `ExchangeLaw.response_not_fixed_by_coupling` |
| 转 (仍能修正、回返、变通: revision, return, turning remain possible) | One structure for each word. Return: a configuration returns where some step from it leads to a configuration from which it can be had again, and a dependence returns where it is met again (row return). Turning: after a loss without return, a formation that stays active has weakened or dissolved its dependence (`Becoming.Dependence`). Revision of what an act did: the courses with and without the act rejoin only through a formation that exchanges differently in them and couples them apart (`Becoming.Rejoining`). | `Branching.Returns`, `Web.Restored`, `Becoming.Dependence`, `Flow.closes_through_coupling_apart` |
| 开非更多 (openness is not more) | How much can be had does not decide 转. In three configurations, each of which can move, every configuration can be had at every step, and one never returns. | `Branching.Transit.keeps_not_returns` |

The four marks are not independent on the spine, as “不可缺一” takes them to be. 转 read as return gives 可, with no premise: from a configuration that returns, a run starts (`Onward.run_of_returning`). Within finitely many configurations the converse holds too: a run starts exactly where a course leads to a return (`Onward.run_iff_returning`). There, then, 可 is reaching a return, and 未 needs an open world (`unheld_of_new`); the reading of the 九句 in §1 states the three cases this gives.

稳 and 元闭 are one structure. The treatise counts 稳 (“扰后不坍、回观不败、仍续”, 卷六 §六四) as a good and 元闭 as a closure. On the spine both are a perturbation drawn back into what a rule holds (`Law.perturbation_reabsorbed`): the one law reads as stability from the side of what the rule holds, and as a frozen rule from the side of a change that would reach it. The verdicts differ while the structure does not, which is why valuation enters only through the comparison under the condition of §6.4, never through a definition.

<a id="11-既有章节的位置--where-the-earlier-chapters-stand"></a>

