<a id="零前提的规律--laws-with-zero-premises"></a>
# Laws with zero premises

> Some passages exist only in the [Chinese edition](ZERO-PREMISE-PLAN.zh.md): sections “Method”.

> stop extending the premise-selection tables. New goal: remove premises and derive the most general versions, zero premises first.

2026-10-11, Asia/Bangkok. A plan and inventory written by the AI (Claude Opus 5.5) following Ren's redirect. Nothing enters the core and no result is registered. The classification and the proposed “Y iff Z” forms are the AI's, pending Ren; the items in class (b) need Ren's decision.

<a id="0-方向--the-direction"></a>
## 0. The direction

**English.** Up to P45 the work advanced by selection tables: for each of the 256 selections of the eight premises, the laws holding exactly where it is selected. The direction is now reversed. Each law is taken, its premises are removed, and it is stated for every world, with the condition its proof actually uses written into the law itself as a condition Z on that world at those steps and relata. The law takes the exact form “Y iff Z”. The selection theorems should follow as corollaries: a premise holding at every step makes Z hold at every step. Within the representation the premises are proved contingent and independent (`World.contingent`, `World.independent`). So no premise is ever claimed as derived as a law; what is derived is the law with its local condition. Each move is named as one of three: localize; re-found the representation (Ren's decision); or generalize the representation.

<a id="1-清点--the-inventory"></a>
## 1. The inventory

<a id="11-方法--method"></a>
### 1.1 Method

**English.** The scope is the main theorems of Part I: those listed by the 39 result records whose canonical source is a Becoming core module outside Part II (Significance, Metaethics, Standpoints, Ranking, Renewal, Bridge and Correspondence are excluded). A script found the declarations listed by those records whose signatures use any of the eight premises, finiteness, enclosure or decidability: 355 in all, 339 of them theorems ([script](ZERO-PREMISE-INVENTORY.py)); witness worlds such as `Shuttle.shuttle` and `Brood.brood` are not laws and are not counted. Each proof was then read to see at which step, and for which relata or family, it uses the premise. The classes are:
- (a) localizable to those steps and relata;
- (b) belonging to the representation, which needs Ren's decision;
- (c) genuinely needed globally.

Notation: `t` a step; `x` a relatum whose standing or activity changes across `t`; `f` a relatum present in the flow at `t`; `c` a condition; `es_t` the family closed at `t`; `[T, ∞)` the steps from `T` on. “Bal(t, c)” is balance at one step and condition: `level (t+1) c + taken t c = level t c + given t c`. “Diss(es, t)” is `Flow.DissipatesOn es t`. “Emb(x, t)” is `active t x ↔ 0 < level t x`. “Act(t, f, c)” and “Take(t, f, c)” are the instances of only active relata giving and taking. “Dep(t, g)” is `active t g → Supported t g`.

<a id="12-结论--findings"></a>
### 1.2 Findings

**English.**
- **Every use of the eight premises is in class (a).** Each proof uses a premise only at particular steps and for particular relata or families:
  - balance at `(t, c)`, where `c` is a condition whose level changes or a member of the enclosing family;
  - only active relata giving or taking, at the `f` that gives to or takes from `x`;
  - dissipation, on the family `es_t` closed at that step;
  - embodiment, at the `x` that arises or ceases, at `t` and `t+1`;
  - activity needing support, at the `g` active at that step;
  - a census, at the steps counted;
  - bounded transmission, at the condition `c` the lineage concerns.

  No proof uses a premise in its universal form, over every step and every relatum.
- **Finiteness and enclosure are in class (a) too.** Finiteness is used only through its local consequences: a closed family at each step (all relata), a census at each step, and bounded counts. Enclosure is a condition on a step. The rest theorem asks for enclosure at every step from `T` on. That is a condition on each step of the tail `[T, ∞)`, still local: it is used only at those steps.
- **Class (b), the commitments of the representation, has five items.**
  1. Amounts in whole units. Rest relies on the total standing being a natural number, which cannot fall infinitely often (`falls_not_recurring`). The `sign` term of dissipation, at least a unit lost whenever something is taken, is the least difference. Ren chose A for the least difference: it belongs to becoming itself ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)). R4 counts the refinement of the unit as a giving. Whether the least loss can be derived is the entropy session's question and is not duplicated here.
  2. Decidability where counted (`mark`, tallies).
  3. Discrete steps and a shared time index.
  4. Each relatum taking part in the flow listed once, and families without repetition (`Distinct`).
  5. Pointwise properties (`Pointwise`, in place of function extensionality).
- **Class (c): none among the eight premises.** The only needs proved not to localize are logical, not premises about worlds:
  - an explicit step after which nothing arises, asked of every finite world, gives the limited principle of omniscience (`World.lpo_of_finite_ends`, `Listed.lpo_of_few`, `Web.lpo_of_ending`);
  - asking of finite worlds without decidability that arising recurs exactly when ceasing does is excluded middle (`World.law_iff_em`).

  These mark the boundary of item 2 of class (b). Without decidability, statements naming an explicit end step cannot be kept; statements that something does not recur can.

<a id="13-逐条--theorem-by-theorem"></a>
### 1.3 Theorem by theorem

“Where” gives the step and the relata or family at which the proof uses the premise; “Class” is a, b or c.

| Theorem (record) | Premise | Where | Class |
|---|---|---|---|
| Counting** | | | |
| `Web.arising_of_ceasing`, `World.arising_of_ceasing` (ceasing-needs-arising) | census | listing at the steps of `[N, N+n]` for each `N`; only `\|alive N\|` and the census balance on the stretch are used | a — a finite list holding the active at one step `N` after which nothing arises suffices (with nothing arising, later activity is within it) |
| same | decidability | `mark (Ceases t a)`, `mark (Arises t a)` on the listed relata | b (2) |
| `Web.unceasing_iff_bounded`, `CountedBy.arising_iff_ceasing` (bounded-census-keeps-pace) | census; bound `B`/`K` | listing on the stretch; `\|alive t\| ≤ K` at arbitrarily late `t` | a — already an exact iff without a bound: `Listed.ceasing_iff_shortfall`, `Listed.coming_iff_excess` |
| `Listed.tally`, `counting_laws`, `tally_iff_counted` (whole-law-of-counting) | decidability | the marks counted | b (2); no premise on worlds |
| `counting_binds_jointly`, `Web.Embodied.arises_given` (whole-law-of-counting, life-as-condition-of-life) | balance | `Bal(t, x)` for the `x` arising across `t` | a |
| same | acting | `Act(t, f, x)` for the `f` present giving to `x` | a |
| same | embodiment | `Emb(x, t)`, `Emb(x, t+1)` | a |
| same | census | only to turn “`f` active at `t`” into a positive count at `t` | a |
| `World.taking_binds_counting` | taking | `Take(t, f, c)` for each `f` present at `t` (nothing active, so nothing taken) | a |
| same | balance | `Bal(t, c)` for `x` and for the members of the family active after `t` | a |
| same | dissipation | `Diss(alive (t+1), t)`: the family active after the step | a |
| same | embodiment, census | `Emb(c, t)`, `Emb(c, t+1)` on that family; listing at `t`, `t+1` | a |
| `World.enclosed_binds_counting` | balance, dissipation | `Bal(t, x)`; `Diss(cs, t)` for the `cs` closed at `t` | a |
| same | embodiment | `Emb(c, t)` for `c ∈ cs`; `Emb(x, t)`, `Emb(x, t+1)` | a |
| `counting_under`, `counting_binds_iff`, `enclosed_counting_under`, `finite_counting_under`, `binding_*` (selection tables) | all | through the laws above and B3 | a, b (2) — become corollaries |
| Rest and openness** | | | |
| `Flow.standing_runs_down`, `standing_never_rises`, `change_lowers`, `exchange_lowers`, `fall_lowers_on`, `rise_lowers_on` (continued-change-needs-openness, rising-and-falling-in-one-exchange) | balance | `Bal(t, c)`, `c ∈ es_t` (`Balances.over` sums them) | a |
| same | dissipation | `Diss(es_t, t)` | a; its `sign` term is b (1) |
| same | standing census | `stand t`, `stand (t+1)` only to equate the total standing with `stock es_t` | a — removable: `es_t` already holds what stands |
| `Flow.change_stops_unrefuted_around`, `exchange_not_recurring_around`, `World.arising_stops_unrefuted`, `comes_to_rest_unrefuted`, `rests_unrefuted_around`, `rests_unrefuted_enclosed`, `arising_opens`, `Finite.comes_to_rest_unrefuted`, `World.rests_unrefuted` (continued-change-needs-openness, space-and-its-parts) | balance, dissipation, enclosure | the step law above at each `t ∈ [T, ∞)` | a |
| same | embodiment | `Emb(x, t)`, `Emb(x, t+1)` for the `x` arising or ceasing in the tail | a |
| same | census of activity | only for ceasing, through the census law | a |
| same | decidability | `comes_to_rest_unrefuted`'s ceasing half; `rests_unrefuted_enclosed` needs none (¬¬ enclosure) | b (2) |
| same | whole units | `falls_not_recurring` on the total standing | b (1) |
| same | finiteness | supplies a closed family at each step (all relata) and the census | a |
| `World.enclosure_bounds_change`, `ChangeBound.not_recurring` (counting-under-enclosure) | balance, dissipation, enclosure, embodiment, census | as in the rest theorem, at each `t ≥ T` | a |
| same | decidability, whole units | marks; `falls_by_occurrences` | b (1), b (2) |
| `Balances.runs_down`, `takers_within`, `taking_not_recurring`, `Dissipative.opens`, `finite_taking_not_recurring`, `More.opens`, `opens_of_arising` (no-finite-part-bears-taking) | balance, dissipation | `Bal(t, c)`, `c ∈ cs`; `Diss(ds, t)` for the families containing `cs` at the late steps | a |
| same | finiteness | `finite_taking_not_recurring`: the family of all conditions, closed at every step | a |
| `Flow.rise_with_fall`, `standing_with_fall`, `rise_alone_opens` (rising-and-falling-in-one-exchange) | balance, dissipation | already stated on `ds` at `t` | a — already local |
| `generation_needs_replenishment`, `Embodied.given_of_arises`, `generation_opens`, `generation_not_recurring`, `generation_draws_in` (generation-is-replenishment) | balance, embodiment, dissipation, finiteness | `Bal(t, c)` on the family from `T`; `Emb(x, ·)` for the arising `x`; `Diss` on the closed families; finiteness as above | a |
| `Flow.fed_from_beyond`, `rising_fed_from_beyond`, `generation_fed_from_beyond` (continuing-self-fed-from-beyond) | balance, dissipation, embodiment | at the step and family | a |
| same | decidability | inward or fed decided | b (2) |
| `Flow.replenishment_recurs`, `renewing_recurs`, `uptake_needs_replenishment` (unceasing-generation-needs-renewal) | balance, taking | `Bal(t, c)` on the depleted family over the stretch; `Take(t, f, c)` for the arising formations taking from it | a |
| `Balances.replenished_over`, `renewers_over`, `More.replenishment_unbounded` (more-needs-renewers) | balance | `Bal(t, c)`, `c ∈ cs`, over the stretch | a |
| `More.unceasing`, `More.grows`, `unceasing_of_growth` | taking, census, decidability | `Take` at the first step of the arising formations; listing on the stretch; marks | a, a, b (2) |
| Dependence, reserve and support** | | | |
| `continuing_restores`, `consumed_continues_transformed`, `static_dependent` (becoming-dependence-dynamics) | dependent | `Dep(t, g)` for the `g` active at the steps considered | a — `Kept` and `Broken` are already local |
| `Web.Dependent.inactive_below`, `ceases_below`, `Downstream.one_way`, `Mortal.after_its_end` (space-and-its-parts, derived-extent-limits) | dependent, balance | `Dep(t, g)` for the one `g` whose condition falls below its need; `Bal` on that condition | a |
| `Web.Census.over_stretch`, `Census.balanceFrom`, `arisingFrom_of_ceasingFrom` (census-balance, census-balance-under-continuation) | census; decidability | listing on the stretch compared; marks | a; b (2) |
| `Web.carries_zero`, `Carries.lasts`, `lasts_within` (reserve-defers-ending) | dependent; decidability | `Dep` as the zero reserve; marks of `f`'s activity | a; b (2) |
| `Carries.chain_ends_of_em`, `Web.lpo_of_ending` | excluded middle, LPO | the explicit end of a chain | b (2), with the proved boundary |
| `rise_given_by_supported`, `gains_from_supported`, `unsupported_stays`, `nothing_supported_stays` (support-from-the-supported) | balance, acting, dependent | `Bal(t, c)` for the required `c` that rise; `Act(t, g, c)` and `Dep(t, g)` for the givers `g` | a |
| `Balances.supported_iff_within_margin`, `supported_of_net_give`, `admits_of_net_draw`, `closes_nothing`, `opens_nothing` (closing-needs-net-draw, four-cases-of-a-part) | balance | `Bal(s, c)` for `s < t` and the `c` that `f` requires (through `Balances.withheld`) | a; the withheld levels are a disclosed choice of the representation |
| `Balances.consumption_ends_with_feeders`, `unfed_consumption_ends`, `Overshoot.ends_through_feeder` (consumption-ends-with-feeders) | balance, acting, dependent | `Bal(T+k, c)`; `Act(T+k, f, c)`, `Dep(T+k, f)` for the givers `f` of `c`, `k < n` | a |
| `joint_excess_ends`, `stays_below`, `excess_bounded` (own-count-misses-joint-excess) | balance, acting, dependent | as above, on `c` over the stretch | a |
| `DescendsAt.supported`, `unsupported_childless`, `selected_le`, `selection_within` (evolution-on-descent) | acting, dependent | `Act(t, g, x)` for the parent giving at descent; `Dep(t, g)` | a |
| `transmitted_supported`, `transmitted_within` | transmitting | `TransmitsWithin c δ` for the one `c` concerned; the uniform `δ` over all `c` is not used | a |
| `Mortal.without_continues`, `Clearing.undermines_within_renewal` (derived-extent-limits) | balance, dissipation, dependent | at the steps and conditions of the formation considered | a |
| The whole, the map of premises, and logic** | | | |
| `World.arising_iff_ceasing`, `World.rests_unrefuted` (space-and-its-parts) | finiteness | a closed family at each step; a listing of every relatum | a |
| same | decidability | the finite-world law | b (2); `World.law_iff_em` proves it cannot be dropped from this statement |
| `World.lpo_of_finite_ends`, `Listed.lpo_of_few` (counting-under-enclosure, continued-change-needs-openness) | decidability | an explicit end step for every finite world | b (2), the proved boundary |
| `World.acting_across`, `acting_of_enclosed`, `Finite.acting`, `Finite.counted` (map-of-premises) | taking, dissipation, enclosure, finiteness, decidability | `Take(t, f, c)` and `Diss(es_t, t)` at the enclosed step; the finite list | a; b (2) for `Finite.counted` |
| `Flow.More.unceasing_reidentified` (identity-across-steps) | taking, census, decidability | as in `More.unceasing` | a, a, b (2) |
| Every resolution** (R-line, another session) | | | |
| `Flow.quantum_bound`, `uptake_bound`, `World.not_recurring_at_resolution`, `World.rests_unrefuted_refinement_counted` (rest-at-every-resolution, rest-with-refinement-counted) | balance, dissipation (`DissipatesBy`), enclosure, embodiment, census | at each step of the tail and the enclosing family | a; the loss in proportion and the counted refinement are b (1), already put to Ren and decided as A |

<a id="14-ren-的决定--for-ren-to-decide"></a>
### 1.4 For Ren to decide

**English.** These change the representation itself and so are Ren's:
- **(b1) The least difference.** Decided: A, it belongs to becoming. Whether it can be derived is the entropy session's question.
- **(b2) Decidability.** Keep it, or drop it in the forms stating that something does not recur. In the second case, statements naming an explicit end step are given up, as the proved boundary requires. Decided (Ren, 11 October 2026: “too dualist”, then “please”, [words](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)): made local. Decidability is no longer a commitment of the representation; the laws that count or name a step state decidedness where they count as their own condition, and the laws that do not need it are stated without it (P58, `Becoming.Decidedness`, study section 84, [inventory](DECIDABILITY-INVENTORY.md)). What still uses it: 368 theorems whose statements depend on it (77 count, 291 concern objects built by deciding) and 226 that use it only in proofs (87 find a step or a member, 89 tell same from different, 16 build a list, 29 split on a case, 5 build an indicator), each with its reason; the rest theorems no longer use it, except the learner's (P73): the learner moves on where its claim is refuted, so their statements depend on telling values apart.
- **(b3) Time.** Test only coarser steps (sampling), or also continuous time. Another session's worktree holds an uncommitted `Sampling` module (section 4). Decided (Ren, 12 October 2026, [words](../../../../sources/15-codex-theory-conversations/2026-10-12-unit-of-need-and-tower-of-time.md)): coarser steps are tested (`Becoming.Sampling`); continuous time is read in the core as a tower of ever finer discrete readings linked by `Sampling`, a law of continuous time being a law at every level; real-valued time is a later periphery correspondence. Loss stays counted per exchange, not per fine step.
- **(b4) The unit of need.** Decided (same source): at a finer unit a need is counted in the same unit as the level; an unchanged need scales with the split, with `r > 0` the reading's condition, so support does not depend on the grain of measurement. This is a commitment of the representation about how need is measured, stated openly, not a premise on worlds.
- **Two possible re-foundings, proposed by the AI.**
  - Count imbalance as a relatum. An imbalance at a step and condition can be counted as the exchange of a relatum that only gives or only takes, as R4 counts the refinement as a giving. Balance then holds by the representation, and its local failure becomes a visible exchange. Decided (Ren, 11 October 2026, “please”): proved first as a representation equivalent to the current one (P59, `Becoming.Imbalance`, study section 85): every flow balances, balance is exactly the added relatum idle, and the activity premises are equivalent step by step; whether to adopt it is Ren's. Decided (Ren, 14 October 2026: “please, finish all”, [words](../../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md)): adopted. `Becoming.Reading` counts the rest in every world (`World.withRest`) and reads activity and drawing off the exchange: balance, only active relata giving and taking, and activity needing support under a law of exchange hold by reading, and closure reads as the rest idle; the landed laws keep their statements (P107, study section 125).
  - Read embodiment as a definition: to be active is to stand. This loses the distinction between the two roles of formation and condition, so the AI does not recommend it. Decided (same source): not read as a definition; embodiment stays a premise, made local at the relata that arise or cease.

  Both re-found the representation; Ren's decisions of 11 October 2026 are above, and the imbalance relatum was adopted by Ren on 14 October 2026 (above).

**Tests of the representation (P77, P78, P88).** Listing once is re-founded: a list can be listed once exactly where identity among its members is decided; refutation laws need no such premise, and fixing every list's number up to relational indiscernibility in every world is equivalent to excluded middle (`Becoming.Listing`, study §101). This preserves the distinction between names and relations and does not choose Ren's reading of identity. Time is tested beyond coarsening: stuttering and removing idle steps keep the named laws; for a supplied footprint, the partial order of joined exchanges characterizes the orders reached by commuting unjoined neighbouring exchanges (`Becoming.Order`, study §102). P88 constructs a normal form on finite named stretches with symmetric joining and decided apartness; a natural-number-valued complete invariant exists exactly where apartness on that stretch is decided. Every commutation carries a census forward; split-sided reorderings and independent reorderings of a containing footprint carry it both ways, without asserting the same population at each intermediate step. A supplied idleness decision at every step and relatum constructs the least Boolean footprint; its converse existence characterization additionally needs decidable equality of relata (`Becoming.OrderNormal`, study §109). Unnamed forms, Foata simultaneous layers, normal forms for unbounded runs, least footprints without the stated decisions, a concrete undecidable-idleness witness and actual continuous-time correspondence remain open. These proofs do not choose the fixed naming or footprint readings for Ren.

<a id="2-零前提的重述--zero-premise-restatements"></a>
## 2. Zero-premise restatements

**Status (P77–P79).** P77's listing once and P78's step order are stated above. P79 adds to P48's localization: realizing a specified one-step pattern is exactly obeying the laws of the named conditions (`OneStep.every_iff`, `OneStep.laws`). It supplies the missing nonzero-taking/taker and nonzero-giving/giver laws, characterizes exactly what givers, capacity and activity add, and the chaining on one family or continuity on families chosen step by step (study §103). This closes completeness for those patterns, not universal completeness for becoming or every law. Counts of active relata and capacity and activity over runs remain open. The earlier inventory, proposals and historical status below retain their original scope.

**Status (P48).** The four laws below are checked in `Becoming.Locality` and registered as [laws-of-one-step](../../../../theories/becoming/results/records/laws-of-one-step.md) ([study section 66](BECOMING-RENEWAL-READING.md#66-一步的规律条件在规律之内p48)); what follows keeps the proposals as they stood before the check. The check changed three things: law 1's condition needs no closure (`Flow.RunsDownOn`: a family holding what stands, balanced and dissipated on, suffices, closure entering only the iff for the exchange); law 3 needs no embodiment for what stands; law 2's form that ceasing does not recur needs no decision (`Covers.ceasing_not_recurring`), while the exact count does. The proposed `stock es (t+1) + takers es t ≤ stock es t` is `Flow.RunsDownOn.takers_le_fall`.

**Status (P50).** Group C of the inventory (dependence, reserve and support, section 1.3) and the census balance are restated for every world with their condition inside them, drafted and verified by the session “0 axiom completeness” ([study section 71](BECOMING-RENEWAL-READING.md#71-依存储备支持与普查平衡的规律条件在规律之内p50)). What the proofs need of activity appears in one way only: whatever gives to the condition used is supported across the step used (`Flow.GiversSupported`). No decision of class (b) was needed. What remains is the rest of group B (the laws in `Dissipation` and `Flow`) and group D.

**Status (P57, P60, P61).** The rest of group B (the laws in `Dissipation` and `Flow`), group D and the census law under a continuation are restated for every world, drafted and verified by the session “0 axiom completeness” (study sections [74](BECOMING-RENEWAL-READING.md#74-静止开放与补给的规律条件在规律之内p57), [75](BECOMING-RENEWAL-READING.md#75-整体的规律条件在规律之内p60), [76](BECOMING-RENEWAL-READING.md#76-延续之下的普查定律只用一个覆盖列表p61)). Shared lemmas move to the lowest module that needs them (`Flow.BalancesOn` into `Flow`), names and statements unchanged. Every group of the inventory is now localized. What remains is not localization: the representation decisions of class (b) (the least difference, decided A by Ren; decidability, inventoried by P58; time, tested by `Sampling`) and the test with amounts finer than whole units.

**Status (P63, P61b, Sampling).** The reserve row of group C missed in P50 is restated locally (P63, study section 79); the converse of P61 is proved (P61b). Time: coarser steps are tested (`Becoming.Sampling`, study section 80): balance (with each relatum listed once), dissipation, closure and running down compose across a coarse step, nothing composes back to the fine steps, and acting, taking and transmission are step-relative. Whole units: the laws of one step hold with change read in the unit and fail read in raw counts; a need is counted in the same unit as the level (`Becoming.Units`).

**Status (P58, P59).** Decidability is made local (P58, study section 84): a count is a relation, existing exactly where what it counts is decided; the census between counts, the never-stopping forms of recurrence in finite families and the rest theorems need no decidedness; the theorems still using it each have a reason, listed in the [inventory](DECIDABILITY-INVENTORY.md). The imbalance relatum is proved equivalent to the current representation (P59, study section 85) and not adopted.

**Status (P58c).** The rest family is named by the strength proved (Ren, 12 October 2026: “agree with you”, [source](../../../../sources/15-codex-theory-conversations/2026-10-12-rest-family-strengths.md), study section 111): that resting from some step on cannot be refuted (`World.RestsFrom`, `World.rests_unrefuted` and others, statements strengthened) is kept apart from non-recurrence only (`…_not_recurring`); the former needs no decision procedure either, the ceasing half using a finite pigeonhole inside the double negation (`Covers.ceasing_stops_unrefuted`). The tables use the current names.

**English.** In Ren's order, four laws come first. Each is stated for every world, with its local condition inside it. The move in each is “localize”. The forms below are proposals, not results until checked in Lean.

1. The law of one exchange, and rest.** Let `es` be a family without repetition, closed across `t`, holding whatever stands at `t` or `t+1`, balanced on its members across `t` and dissipated on across `t`. Then `stock es (t+1) + takers es t ≤ stock es t`, and the following are equivalent (“Y iff Z”):
   - some condition's standing changes across `t`;
   - the total standing falls across `t`;
   - some relatum taking part takes or gives across `t`.

   Rest is the corollary over a tail: if this holds at every step of `[T, T+N)`, the steps there at which some standing changes number at most `stock(T) − stock(T+N)`. Continued change needs openness: change recurs only where the local condition fails at arbitrarily late steps. With what stands finite at each step, so that the total standing is a number, the count is exact: from `T`, the changes at steps meeting the condition number at most the total standing at `T` plus the rises of the total standing at the steps not meeting it. The selection results follow, since the eight premises with enclosure give the condition at every step.
2. Ceasing needs arising.** If a finite list holds the relata active at step `N` and nothing arises from `N` on, then at each later step the relata active, with those that ceased since `N`, number exactly those active at `N`. So ceasing recurs with arising stopped at `N` only if no finite list holds what is active at any step from `N`. The census law is the corollary under a census. The exact iffs `Listed.ceasing_iff_shortfall` and `Listed.coming_iff_excess` remain, with a listing needed only at the steps they compare.
3. Closure bounds change.** Over steps `[T, T+N)` each meeting the condition of item 1, the relata standing at `T+N`, with the steps at which some standing changed, number at most the total standing at `T`. This needs no embodiment. For activity, embodiment is needed only at the relata that arise or cease at those steps. `World.enclosure_bounds_change` and P47's `World.enclosure_bounds_standing` are corollaries.
4. Arising needs an active giver.** This recasts the three lemmas of the withdrawn P48. With balance at `(t, x)`, each of the following is an exact iff:
   - (i) `x` comes to stand across `t` iff `level t x = 0` and `taken t x < given t x`;
   - (ii) `x` ceases to stand across `t` iff `0 < level t x` and `taken t x = level t x + given t x`;
   - (iii) across a step at which nothing is taken from a family holding what stands after it, balanced on its members across the step, some member rises iff some relatum taking part gives to the family without taking from it; coming to stand is such a rise. Where the family is also closed across the step, dissipation on it at that step excludes exactly this, so nothing comes to stand.

   Corollaries:
   - with `Emb(x, t)` and `Emb(x, t+1)`, an `x` arising across `t` is given to by a relatum other than `x`; with `Act(t, f, x)` for its givers, something is active at `t`;
   - `Web.Embodied.arises_given`, `counting_binds_jointly`, `taking_binds_counting` and the three P48 lemmas.

*Commitments each law needs (step 4, to be tested).**
- Law 4 (i)–(iii) needs no whole unit: it is ordered-sum arithmetic of one step. It needs no decidability. It concerns one step, so whether it survives coarser steps turns on balance composing, which the uncommitted `Sampling` module reports it does.
- Laws 1 and 3 need the least difference, b (1). With finer units they fail unless the refinement is counted (R4) or the loss is proportional (R3). They need no decidability in their “does not recur” form, and they need discrete steps.
- Law 2 needs decidability for the count; whether a ¬¬ or pigeonhole form avoids it is to be tested. It needs discrete steps.

*As checked (P48).**
- Decidability: laws 1, 3 and 4 decide no predicate of the world, their proofs deciding only the order of numbers; law 2's exact count needs marks, its form that ceasing does not recur none.
- Whole units: the one-step iffs of laws 1 and 4 use addition and order only; the recurrence of law 1 and the bounds of law 3 use the least difference (A). Amounts finer than whole units are not yet tested; rest is covered by R4 (`World.rests_unrefuted_refinement_counted`, `World.arising_opens_refinement_counted`).
- Time: coarser steps are tested by the localized `Sampling` (landing queue).
- Finiteness: the census of what stands is used only by law 1's recurrence and by law 3, to make the total standing a number at each step.

<a id="3-不主张什么--what-is-not-claimed"></a>
## 3. What is not claimed

**English.** No premise is claimed derived as a law. The least difference is not claimed derived; that is the entropy session's question. It is not claimed that no premise beyond the eight is used. The logic, `Std` and the pure-core rules are unchanged. The selection theorems already landed remain results at their scope.

<a id="4-协调--coordination"></a>
## 4. Coordination

- **The entropy session** (“Derive entropy: is a lossless exchange possible?”). A message on 2026-10-11 asked which definitions and files it is changing, and whether it will produce a local law of the form “dissipation at step `t` on family `F` iff …”. The message expired undelivered because the two sessions run in different permission modes. Until it is answered:
  - this work states dissipation only as `Flow.DissipatesOn es t` at the steps used;
  - it does not touch `Becoming/Dissipation.lean`, `Becoming/Flow.lean` or `Becoming/Resolution.lean`;
  - it does not take up the derivability of the least loss.

  Update (as P48 lands): the message was delivered and the entropy session replied. Its R5 `Becoming.Entropy` imports only `Becoming.Resolution` and changes no existing module; it is item 8 of the landing queue. It reports its result on b(1) as a decomposition, not a derivation (not yet landed).
- **Another session's uncommitted modules.** A worktree under session `858b224e` holds uncommitted modules:
  - `StandingCounting`, `DependenceCounting` and `FiniteBinding`, which overlap P47 and P46;
  - `Sampling`, coarser steps, which bears on the time test of step 4;
  - `Determination`, standing fixed by the exchange and one cross-section.

  P46 and P47 land first, as Ren directed. Where those modules land, step 4 reuses `Sampling` rather than rebuilding it.

  Update (as P48 lands): P46 and P47 have landed; the same session (“0 axiom completeness”) drafted law 2, folded into `Becoming.Locality`; it localized `Sampling` (queue item 7) and delivered the local restatements of the inventory's group C (item 5, P50).
- **P42–P44** of the peer session land before P46 and P47, as agreed.

<a id="5-连续时间范围ai-的提议待-ren-continuous-time-scope-ai-proposal-awaits-ren"></a>
## 5. Continuous time: scope (AI proposal, awaits Ren)

Update (12 October 2026): Ren decided that continuous time is read in the core as a tower of ever finer discrete readings (see section 1.4, b3); the scope below is kept as the proposal it was.

2026-10-11, written by the session “0 axiom completeness” at the integrator's request. There is no Lean and no result. Ren: “let's finish one first, then another”. Coarser steps come first (`Sampling`, verified in scratch, awaiting landing), then continuous time. What follows is scope only.

**English.**
- **What can be said inside the core.** The core uses only Lean's prelude and has no reals. So inside the core, continuous time can only be read as a refinement of the step: a fine world of which the given world is the sampling at some times. This is the converse direction of `Sampling`. `Sampling` proved that the local conditions compose from fine steps to a coarse step:
  - balance, where each relatum is listed once at each step;
  - dissipation;
  - closure, exactly;
  - running down, which needs only the two ends.

  `Cancelling` and `Averaging` proved that the converse does not hold automatically. Continuous time then reads as a tower of worlds, each the sampling of the next, with no finest level. A model with real-valued time would sit in the periphery, which may use Mathlib, joined to the core by correspondence theorems. Which to choose is a matter of the representation, so it is Ren's decision (the second half of b3).
- **Questions on a tower (to prove; all conjectures).**
  1. A refinement always exists: put all of a coarse step's exchange at its first fine step, with nothing at the others. Then every local condition passes down. So mere existence says nothing; the question is which conditions hold in every refinement.
  2. A condition holding at level k+1 holds at level k (by `Sampling`). So a condition holding at arbitrarily fine levels holds at every coarser one.
  3. The interaction with the least difference (b1, where Ren chose A). Every taking under dissipation loses at least a unit. If a continuous exchange counts as a taking at ever finer steps, the loss in finite time has no bound. Conjecture: under A and dissipation, the steps of change at every level of a tower are bounded by the same total standing, since the unit does not change with the step. A dissipating becoming in continuous time would then have only finitely many events of change, with no Zeno-like infinite subdivision. If so, the least difference makes change in continuous time discrete, which links b1 and b3.
  4. Only active relata giving, only active relata taking, and bounded transmission depend on the step (`Strobe`, `Delay`). In a tower they need activity held on the intervals (`Web.Held`) at every level, or a restatement for the case with no finest level.
- **For Ren.**
  - A tower in the core, or real time in the periphery, or both joined by correspondence theorems.
  - Whether events of exchange are counted per fine step or per exchange. This settles question 3.
