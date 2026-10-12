# P77 inventory: every use of `Distinct` in the Becoming core

Scope: `Becoming/*.lean` on main at `193c5511`. The scan looks for the token `Distinct`
outside comments, using `tools/occ.py` (output in `tools/occ.tsv`). The classification is
done by hand in `tools/classify.py`, which reproduces the table below in `tools/table.md`.
The indirect uses come from `tools/indirect.py`, with output in `tools/indirect.tsv`.
Status claims marked "proved" are theorems in [`Becoming.Listing`](../lean/Becoming/Listing.lean). The other status
claims are classified from the statements, and their notes give the reason.

## Totals

There are **169 declarations in 15 modules**.

| Kind | Meaning | Count |
|---|---|---|
| (i) H | hypothesis in the statement of a law | 114 |
| (ii) P | only inside a proof | 1 |
| (iii) D | in a definition | 14 |
| C | the statement *asserts* `Distinct`: a construction or a witness supplies listing once | 40 |

| Use | Meaning |
|---|---|
| count | the law reads a number of relata (a list's length) |
| sum | the law reads a sum over a family (`total`, `stock`, `DissipatesOn`) |
| enum | a list holding every relatum (finite enumeration) |
| family | the law quantifies over or names a family of conditions; its conclusion reads membership only |
| present | `L.present t`, the list of what takes part in a step |
| steps | lists of step numbers, `Fin`, or pairs at distinct steps |
| tool | a list lemma |
| witness | a finite witness |

| Status | Meaning | Count |
|---|---|---|
| F0 | **Free, no premise.** The hypotheses read membership only and the conclusion is a refutation, so listing once is doubly-negated available (`not_not_listsOnce`) and is discharged by `not_of_listsOnce`. | 30 |
| L | **Local: a sum once per member.** The law reads a sum over a family once per member. Its local condition is that identity is decided among the family's members (`IdentityDecided`). Any listing with decided identity gives a listing once (`listsOnce_of_decided`), and every sum once per member agrees (`ListsOnce.total_eq`). | 33 |
| K | **Kept: a count of relata.** The local condition is that identity is decided among the counted (`numbers_iff_decided`). Every census already carries it (`Listed.identityDecided`), and any listing with a decision procedure gives one (`Listed.of_listing`). | 31 |
| O | **The flow's list of what takes part.** For amounts, this list is re-founded by occurrence: `L.byOccurrence` is `Once` with no premise and keeps every amount. Where a K or L law counts or sums relata, that part stays K or L. | 9 |
| N | **Numbers.** Steps, `Fin` or pairs at distinct steps, whose identity is already decided. This is no commitment about relata. | 10 |
| T | **Tool or witness.** Not a law about the world. | 56 |

## Per module

| Module | Decls | Kinds | Status |
|---|---|---|---|
| Continuation | 5 | H 5 | F0 5 |
| Counting | 7 | C 5, H 1, P 1 | T 5, N 2 |
| Decidedness | 7 | H 6, C 1 | K 2, N 3, T 2 |
| Dissipation | 33 | H 24, C 6, D 3 | F0 16, L 9, T 8 |
| Identity | 15 | H 12, C 3 | K 12, N 2, T 1 |
| Locality | 5 | H 3, D 2 | L 2, K 1, N 2 |
| Openness | 5 | H 1, D 1, C 3 | K 1, L 1, T 3 |
| Population | 33 | H 21, C 10, D 2 | K 15, N 1, T 17 |
| Premises | 7 | H 3, C 3, D 1 | L 4, T 3 |
| Resolution | 24 | H 19, C 3, D 2 | L 14, F0 2, T 8 |
| Roles | 11 | H 8, C 3 | F0 5, L 1, T 5 |
| Sampling | 12 | H 9, C 2, D 1 | O 9, T 3 |
| Space | 2 | D 1, C 1 | L 1, T 1 |
| Standpoints | 2 | H 2 | F0 2 |
| Units | 1 | D 1 | L 1 |
| **Total** | **169** | H 114, C 40, D 14, P 1 | F0 30, L 33, K 31, O 9, N 10, T 56 |

## What each module's uses become

### Free with no premise (F0)

These modules' uses become free with no premise:

- Continuation: all five.
- Standpoints: both.
- Dissipation: the 16 refutation laws.
- Roles: 5 laws.
- Resolution: `taking_stops` and `taking_needs_refinement`.

Representatives proved in `Listing.lean`:

- `Flow.Dissipative.opens_listing`
- `Flow.Dissipative.finite_ceases_listing`
- `Flow.taking_draws_in_listing`
- `Web.generation_ceases_listing`
- `Flow.taking_stops_listing`
- `World.Enumerated.rests`

The rest follow by the same two steps:

1. `not_of_listsOnce`.
2. Invariance under the same members, using `Around.of_same`, `Inward.of_same`,
   `ClosedAt.widen` and `total_pos_of_within`.

### Local: decided identity among a family read once per member (L)

These uses become local conditions:

- Dissipation:
  - `Dissipative`, `Enclosed` and `Around`, proved equivalent by `dissipative_iff`, `enclosed_iff` and `around_iff`;
  - `enclosed_of_finite`, `around_of_finite`, `gives_less`, `dissipatesOn_of_inward(_at)`;
  - `standing_lowers`, proved by `standing_lowers_listing` and `standing_lowers_decided`.
- Resolution: 14 uses (stock bounds, exchange and quantum laws, `DissipativeBy`, `LosesAtEverySize`, `gainers_lose` and `losers_lose`).
- Roles: `arising_lowers`.
- Locality: `stock_eq` and `RunsDownOn`.
- Openness: `AroundStanding`.
- Premises: `listed_of_ever`, `keep_lists`, `counted_of_ever` and `Premise.Binds`.
- Space: `World.Finite`. By `finite_iff` it is an enumeration together with decided identity.
- Units: `RunsDownOnAt`.

The repetition cannot simply be dropped. `Doubled.needs_once` gives a dissipative, balanced
flow where the step is closed on `[true, true, false]` and `true` comes to stand, yet:

- the stock over the repeated family does not fall;
- the flow does not dissipate on that family;
- over `[true, false]` the stock falls.

In `Dissipative`, `Distinct` restricts the quantifier, so it *weakens* the premise. Without
it, `Doubled.flow` would not be dissipative.

### Kept as a count of relata (K)

These uses stay as counts of relata, with the local condition that identity is decided among
the counted:

- Population: 15 uses (`Listed` and its laws, the `Census` and `DependenceCensus` over-stretch laws, `arises_of_more`, and the `More.*` laws).
- Identity: 12 uses (the reidentified `More.*` laws, `arisesFrom_of_more`, `forces_iff_noSplit`, `paired_noSplit`, `forced_iff_more`, and the `Census.balanceFrom` laws).
- Decidedness: `listed_across` and `listed_over_stretch`.
- Locality: `ListsAt`.
- Openness: `StandingCensus.over_stretch_on`.

### Re-founded by occurrence (O)

The Sampling uses are re-founded by occurrence:

- `Once` holds with no premise for `L.byOccurrence` (`byOccurrence_once`).
- Every amount, balance, dissipation and `More` is the same (`byOccurrence_*`).
- Balance composes under sampling with no `Once` premise (`BalancesOn.sample_byOccurrence`).

### Nothing to free (N)

Counting, Decidedness, Locality, Population and Identity have step or `Fin` lists. Their
identity is decided by construction, so there is nothing to free.

## What cannot be freed, as witnesses or equivalences

1. **Counts of relata (K).** A count is fixed exactly where identity among the counted is decided (`numbers_iff_decided`). Per type, every list has a listing once exactly when identity on the type is decided (`listsOnce_all_iff`). Read relationally, with likeness taken as indiscernibility in a world, every list of every world has a number exactly under excluded middle (`World.numbers_indiscernible_iff_em`). Counting by names can count twice what no relation tells apart (`World.probe_named_apart`). The `Repeated` witness (Population) and `repeated_same` show a count by listing doubling under repetition with the same members.
2. **Sum laws with a positive conclusion (L).** `Doubled.needs_once` is the witness. The local condition, decided identity among the family, cannot be removed for these laws. It can only be located.
3. **`World.Finite` in positive counting laws.** The decided-identity half is needed there. Refutations need only `World.Enumerated` (`Enumerated.rests`).
4. **Census laws with a positive recurrence conclusion.** One example is `Web.arising_of_ceasing`. Besides decided identity among the listed, these laws need activity decided at every step. `Web.arising_of_ceasing_listing` states this with exactly those two local conditions.
5. **Identity by name.** For Lean's `=` there is no equivalence with excluded middle in the pure core. A type whose equality carries an arbitrary proposition needs `propext`, `funext` or quotients. Only the per-type equivalence `listsOnce_all_iff` is given.

## Indirect uses

These are statements that mention a definition that carries `Distinct`. They are counted by
a regular-expression scan of statements, so the counts are approximate. 535 of 4126
declarations are affected. They reach Capture, Reserve, Seeking, Standing, Tower and Wholes,
which have no direct use. These statements inherit the status of the definition:

- `Dissipative`, `DissipativeBy`, `LosesAtEverySize`, `Enclosed`, `Around`, `AroundStanding` and `RunsDownOn` are L, by the `_iff` equivalences.
- `Listed`, the censuses, `ListsAt` and `Counted` are K.
- `Once` is O.
- `Finite` is L, with only `Enumerated` needed for refutations.

| module | decls | with-any | Listed | Census | StandingCensus | DependenceCensus | ListsAt | Counted | CountedBy/Within | Dissipative | DissipativeBy | Enclosed | Around | AroundStanding | RunsDownOn(At) | Once | World.Finite | LosesAtEverySize | Distinct(direct) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capture | 13 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Continuation | 83 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 5 |
| Counting | 315 | 62 | 0 | 10 | 0 | 0 | 0 | 7 | 0 | 17 | 0 | 19 | 0 | 0 | 0 | 0 | 14 | 0 | 6 |
| Decidedness | 59 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 7 |
| Dissipation | 133 | 49 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 26 | 0 | 9 | 12 | 0 | 0 | 0 | 0 | 0 | 30 |
| Identity | 183 | 25 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| Locality | 49 | 25 | 1 | 0 | 17 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 3 |
| Openness | 117 | 65 | 4 | 10 | 27 | 0 | 0 | 8 | 8 | 18 | 0 | 10 | 1 | 18 | 0 | 0 | 8 | 0 | 4 |
| Population | 157 | 63 | 17 | 18 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| Premises | 133 | 32 | 1 | 0 | 0 | 0 | 0 | 9 | 0 | 12 | 0 | 4 | 0 | 0 | 0 | 0 | 13 | 0 | 6 |
| Reserve | 123 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Resolution | 265 | 70 | 0 | 7 | 2 | 0 | 0 | 16 | 0 | 22 | 26 | 22 | 0 | 2 | 0 | 0 | 0 | 4 | 22 |
| Roles | 189 | 23 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 11 |
| Sampling | 119 | 27 | 0 | 1 | 1 | 0 | 0 | 3 | 0 | 4 | 0 | 0 | 0 | 0 | 2 | 9 | 2 | 0 | 11 |
| Seeking | 16 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Space | 131 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 26 | 0 | 1 |
| Standing | 54 | 20 | 0 | 2 | 5 | 2 | 0 | 3 | 0 | 4 | 0 | 5 | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| Standpoints | 36 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| Tower | 8 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Units | 41 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 |
| Wholes | 52 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| TOTAL | 4126 | 535 | 34 | 67 | 57 | 7 | 2 | 46 | 8 | 135 | 26 | 71 | 24 | 20 | 11 | 10 | 72 | 4 | 155 |

## Full table of direct uses

### Continuation (5)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Flow.fed_from_beyond_from` | 124 | H | family | F0 | conclusion a refutation; FedFromBeyond, Around, BalancesOn, takers>0 are membership-only; DecidableEq C already assumed |
| `Flow.rising_fed_from_beyond_from` | 132 | H | family | F0 | conclusion a refutation; FedFromBeyond, Around, BalancesOn, takers>0 are membership-only; DecidableEq C already assumed |
| `Flow.fed_from_beyond` | 145 | H | family | F0 | conclusion a refutation; FedFromBeyond, Around, BalancesOn, takers>0 are membership-only; DecidableEq C already assumed |
| `Flow.rising_fed_from_beyond` | 153 | H | family | F0 | conclusion a refutation; FedFromBeyond, Around, BalancesOn, takers>0 are membership-only; DecidableEq C already assumed |
| `Web.generation_fed_from_beyond` | 349 | H | family | F0 | as above |

### Counting (7)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `distinct_map_on` | 215 | C | tool | T |  |
| `EnclosedQueue.span_distinct` | 1011 | C | steps | N | lists of numbers / Fin K |
| `World.enclosedQueue_dissipatesOn` | 1090 | H | family | T | shows a witness meets Dissipative (whose quantifier is over Distinct families) |
| `placesBelow_distinct` | 1212 | C | tool | T |  |
| `places_listed` | 1232 | C | steps | N | lists of numbers / Fin K |
| `World.finite_dissipation_binds` | 1387 | C | family | T | witness that dissipation binds (Premise.Binds .dissipative) |
| `World.sheddingQueue_dissipative` | 4318 | P | family | T | proof that a witness is Dissipative |

### Decidedness (7)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Counts.listing` | 406 | C | tool | T | a count is a list's length; keeps listing once |
| `length_eq_of_same` | 433 | H | count | T | uniqueness of the count once per member (used by Numbers.unique) |
| `Counts.listed_across` | 443 | H | count | K | census lengths; local condition: decided identity among the listed (Numbers) |
| `Counts.listed_over_stretch` | 479 | H | count | K | census lengths; local condition: decided identity among the listed (Numbers) |
| `coming_steps_within` | 544 | H | steps | N | Distinct lists of steps (Nat); the family `as` itself is not asked to be Distinct |
| `ceasing_steps_within` | 564 | H | steps | N | Distinct lists of steps (Nat); the family `as` itself is not asked to be Distinct |
| `Recurs.steps_found` | 583 | H | steps | N | Distinct lists of steps (Nat); the family `as` itself is not asked to be Distinct |

### Dissipation (33)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `total_le_at` | 133 | H | tool | T | sum once per member |
| `total_le_of_support` | 147 | H | tool | T | sum once per member |
| `insertNew_spec` | 184 | C | tool | T | listing once with DecidableEq |
| `adjoin_spec` | 196 | C | tool | T | listing once with DecidableEq |
| `Flow.Dissipative` | 231 | D | family | L | Flow.dissipative_iff: every closed family read once per member |
| `Flow.Enclosed` | 236 | D | family | L | Flow.enclosed_iff: some closed family with decided identity |
| `Flow.Around` | 242 | D | family | L | Flow.around_iff |
| `Flow.enclosed_of_finite` | 272 | H | enum | L | positive (∃ family); holds where identity among `all` is decided |
| `Flow.Dissipative.gives_less` | 292 | H | sum | L | sum once per member; fails with repetition (Lone.repeated_family) |
| `Flow.Dissipative.opens` | 446 | H | family | F0 | proved: Flow.Dissipative.opens_listing |
| `Flow.Dissipative.finite_ceases` | 455 | H | enum | F0 | proved: Flow.Dissipative.finite_ceases_listing |
| `Flow.More.opens` | 479 | H | family | F0 | refutation; as opens_listing |
| `Flow.opens_of_arising` | 485 | H | family | F0 | refutation; as opens_listing |
| `Flow.around_of_finite` | 494 | H | enum | L | positive (∃ family); holds where identity among `all` is decided |
| `Flow.dissipatesOn_of_inward_at` | 530 | H | sum | L | conclusion DissipatesOn ds t is a sum over ds |
| `Flow.Dissipative.dissipatesOn_of_inward` | 555 | H | sum | L | conclusion DissipatesOn ds t is a sum over ds |
| `Flow.taking_draws_in_from` | 563 | H | family | F0 | refutation; as taking_draws_in_listing |
| `Flow.taking_draws_in` | 580 | H | family | F0 | proved: Flow.taking_draws_in_listing |
| `Flow.standing_lowers` | 604 | H | sum | L | proved: Flow.standing_lowers_listing, _decided; fails with repetition (Doubled.needs_once) |
| `Flow.rising_opens` | 644 | H | family | F0 | refutation; as opens_listing |
| `Flow.standing_opens` | 652 | H | family | F0 | refutation; as opens_listing |
| `Flow.rising_draws_in_from` | 659 | H | family | F0 | refutation; as taking_draws_in_listing |
| `Flow.rising_draws_in` | 676 | H | family | F0 | refutation; as taking_draws_in_listing |
| `Flow.standing_draws_in` | 684 | H | family | F0 | refutation; as taking_draws_in_listing |
| `Flow.rising_ceases` | 692 | H | enum | F0 | refutation; as finite_ceases_listing |
| `Flow.standing_ceases` | 701 | H | enum | F0 | refutation; as finite_ceases_listing |
| `Flow.rise_alone_opens` | 809 | H | family | F0 | refutation; as opens_listing |
| `Frontier.frontier` | 976 | H | family | F0 | refutation in a witness |
| `Frontier.pool_fuel_distinct` | 995 | C | witness | T |  |
| `Rooted.growers_distinct` | 1067 | C | witness | T |  |
| `Rooted.present_distinct` | 1074 | C | witness | T |  |
| `Rooted.rooted` | 1122 | C | witness | T | witness statement; its Distinct-quantified clause is a refutation |
| `Lone.frontier` | 1208 | H | family | F0 | refutation in a witness |

### Identity (15)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Flow.More.arising_never_stops_reidentified_covering` | 352 | H | present | K | takers counted as relata; amounts re-founded by occurrence (O), counting relata keeps it (Repeated) |
| `Flow.More.unceasing_reidentified_covering` | 368 | H | present | K | takers counted as relata; amounts re-founded by occurrence (O), counting relata keeps it (Repeated) |
| `Flow.More.unceasing_reidentified` | 384 | H | present | K | takers counted as relata; amounts re-founded by occurrence (O), counting relata keeps it (Repeated) |
| `Web.arisesFrom_of_more` | 591 | H | count | K | more listed after a step than before; forces_iff_noSplit already has DecidableEq F |
| `Flow.More.unceasingFrom` | 622 | H | present | K | takers counted as relata; amounts re-founded by occurrence (O), counting relata keeps it (Repeated) |
| `forces_iff_noSplit` | 663 | H | count | K | more listed after a step than before; forces_iff_noSplit already has DecidableEq F |
| `paired_noSplit` | 696 | H | count | K | more listed after a step than before; forces_iff_noSplit already has DecidableEq F |
| `forced_iff_more` | 724 | H | count | K | more listed after a step than before; forces_iff_noSplit already has DecidableEq F |
| `Web.Census.balanceFrom_at` | 787 | H | count | K | census lengths under a continuation |
| `Web.Census.balanceFrom_eq_at` | 876 | H | count | K | census lengths under a continuation |
| `Web.Census.arisingFrom_of_ceasingFrom_from` | 899 | H | count | K | census lengths under a continuation |
| `Web.Census.ceasingFrom_of_arisingFrom_from` | 927 | H | count | K | census lengths under a continuation |
| `Web.ceasingFrom_found` | 1013 | C | steps | N | pairs at distinct steps |
| `Web.arisingFrom_found` | 1138 | C | steps | N | pairs at distinct steps |
| `Dormant.no_split_without_arising` | 1671 | C | witness | T |  |

### Locality (5)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Web.StandingCensus.stock_eq` | 156 | H | sum | L | total standing = stock over any family listed once holding what stands |
| `Flow.RunsDownOn` | 204 | D | sum | L | family holding what stands, once per member |
| `ListsAt` | 464 | D | count | K | census at one step; = Numbers of a listing |
| `Covers.ceasing_steps_within` | 616 | H | steps | N | lists of steps |
| `ceasing_steps_found` | 643 | H | steps | N | lists of steps |

### Openness (5)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Web.StandingCensus.over_stretch_on` | 177 | H | count | K | census of what stands |
| `Flow.AroundStanding` | 198 | D | family | L | as Around |
| `Accretion.alive_distinct` | 425 | C | witness | T |  |
| `Few.distinct_pick` | 791 | C | witness | T |  |
| `Few.distinct_found` | 796 | C | witness | T |  |

### Population (33)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Distinct` | 102 | D | tool | T | the definition |
| `distinct_map` | 127 | H | tool | T | counting toolkit |
| `length_le_of_matched` | 142 | H | tool | T | counting toolkit |
| `length_le_of_sub` | 165 | H | tool | T | counting toolkit |
| `count_le_of_sub` | 172 | H | tool | T | counting toolkit |
| `distinct_remove` | 301 | H | tool | T | counting toolkit |
| `marks_le_of_sub` | 309 | H | tool | T | counting toolkit |
| `total_le_mark` | 350 | H | tool | T | counting toolkit |
| `Listed` | 471 | D | count | K | every census decides identity among the listed (Listed.identityDecided); any listing with a decision procedure gives one (Listed.of_listing) |
| `Listed.keeps_at` | 479 | H | count | K | census lengths |
| `Listed.across_at` | 515 | H | count | K | census lengths |
| `Listed.over_stretch_on` | 532 | H | count | K | census lengths |
| `Listed.ceasing_iff_shortfall_from` | 563 | H | count | K | census lengths |
| `Listed.coming_iff_excess_from` | 598 | H | count | K | census lengths |
| `steps_distinct` | 766 | C | steps | N |  |
| `Web.DependenceCensus.over_stretch_on` | 1165 | H | count | K | census lengths |
| `Web.arises_of_more` | 1188 | H | count | K | census lengths |
| `Web.Census.over_stretch_on` | 1235 | H | count | K | census lengths |
| `Flow.takers_le_covering` | 1258 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Flow.More.grows_covering` | 1269 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Flow.More.grows` | 1283 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Flow.More.arising_never_stops_covering` | 1296 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Flow.More.unceasing_covering` | 1328 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Flow.More.unceasing` | 1359 | H | present | K | takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O) |
| `Expansion.distinct` | 1369 | C | witness | T |  |
| `Expansion.counted` | 1394 | C | witness | T |  |
| `Cycle.distinct` | 1402 | C | witness | T |  |
| `Cycle.counted` | 1419 | C | witness | T |  |
| `Oscillation.pair` | 1435 | C | witness | T |  |
| `Oscillation.counted` | 1452 | C | witness | T |  |
| `Repeated.more_without_arising` | 1517 | C | witness | T | boundary witness: without listing once, one formation counts as many |
| `Inactive.distinct` | 1570 | C | witness | T |  |
| `Inactive.more_without_arising` | 1579 | C | witness | T |  |

### Premises (7)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `keep_distinct` | 111 | C | tool | T |  |
| `listed_of_ever` | 124 | H | enum | L | a census from a list covering all ever active; Listed.of_listing gives one from any listing with decided identity |
| `World.keep_lists` | 159 | H | enum | L | a census from a list covering all ever active; Listed.of_listing gives one from any listing with decided identity |
| `World.counted_of_ever` | 175 | H | enum | L | a census from a list covering all ever active; Listed.of_listing gives one from any listing with decided identity |
| `World.Premise.Binds` | 870 | D | family | L | dissipation binds: some family listed once closed and taken from |
| `World.Hatch.kin_distinct` | 958 | C | witness | T |  |
| `World.FiniteHatch.kin_distinct` | 1103 | C | witness | T |  |

### Resolution (24)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Flow.quantum_bound` | 400 | H | sum | L | bounds by the stock once per member |
| `Flow.quantum_not_recurring` | 410 | H | sum | L | refutation, but of an event stated by a sum over the family (stock or total take): reads the sum once per member |
| `Flow.taking_stops` | 429 | H | family | F0 | proved: Flow.taking_stops_listing |
| `Flow.refinement_gives_nothing` | 577 | H | family | L | premise quantifying over closed families once per member, as Dissipative |
| `Flow.taking_needs_refinement` | 598 | H | family | F0 | refutation; `split * stock = 0` is membership-only |
| `World.after_dissipative` | 644 | H | family | L | premise quantifying over closed families once per member, as Dissipative |
| `Flow.DissipativeBy` | 742 | D | family | L | as Dissipative |
| `Flow.BalancesAt.gainers_lose` | 840 | H | sum | L | counts of gainers/losers over a family once per member |
| `Flow.uptake_bound` | 893 | H | sum | L | bounds by the stock once per member |
| `Flow.replenishment_bound` | 903 | H | sum | L | bounds by the stock once per member |
| `Flow.exchange_bound` | 955 | H | sum | L | bounds by the stock once per member |
| `Flow.exchange_not_recurring` | 967 | H | sum | L | refutation, but of an event stated by a sum over the family (stock or total take): reads the sum once per member |
| `Flow.LosesAtEverySize` | 989 | D | family | L | as Dissipative |
| `Flow.exchange_bound_of_least_loss` | 1051 | H | sum | L | bounds by the stock once per member |
| `Flow.exchange_not_recurring_of_least_loss` | 1064 | H | sum | L | refutation, but of an event stated by a sum over the family (stock or total take): reads the sum once per member |
| `Flow.BalancesAt.losers_lose` | 1106 | H | sum | L | counts of gainers/losers over a family once per member |
| `Asymptote.distinct` | 1501 | C | witness | T |  |
| `Circulation.distinct` | 1693 | C | witness | T |  |
| `Emission.emitted_le_one` | 1825 | H | sum | T | sums over Distinct families inside witnesses |
| `Alternation.given_total` | 1985 | H | sum | T | sums over Distinct families inside witnesses |
| `Trickle.sides_distinct` | 2180 | C | witness | T |  |
| `Trickle.given_total` | 2230 | H | sum | T | sums over Distinct families inside witnesses |
| `Trickle.taken_le` | 2239 | H | sum | T | sums over Distinct families inside witnesses |
| `Trickle.loses_two` | 2261 | H | sum | T | sums over Distinct families inside witnesses |

### Roles (11)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `distinct_conditionsOf` | 162 | C | tool | T |  |
| `Flow.roles_distinct` | 366 | H | present | T | the role reading keeps listing once |
| `Web.Embodied.arising_lowers` | 671 | H | sum | L | stock once per member, as standing_lowers |
| `Web.generation_opens` | 709 | H | family | F0 | refutation |
| `Web.generation_draws_in_from` | 718 | H | family | F0 | refutation |
| `Web.generation_draws_in` | 731 | H | family | F0 | refutation |
| `Web.generation_ceases` | 739 | H | enum | F0 | proved: Web.generation_ceases_listing |
| `Shuttle.distinct` | 1241 | C | witness | T |  |
| `Throughput.side_dissipates` | 1369 | H | sum | T | witness lemma |
| `Throughput.frontier` | 1404 | H | family | F0 | refutation |
| `SprayShuttle.sides_distinct` | 1496 | C | witness | T |  |

### Sampling (12)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `total_gate` | 359 | H | tool | T |  |
| `Flow.unionPresent_spec` | 406 | C | tool | T |  |
| `Flow.Once` | 432 | D | present | O | Flow.byOccurrence_once: every flow read by occurrence is Once |
| `Flow.sample_taken_on` | 442 | H | present | O | coarse amounts from fine ones |
| `Flow.sample_given_on` | 452 | H | present | O | coarse amounts from fine ones |
| `Flow.BalancesOn.sample` | 476 | H | present | O | proved: Flow.BalancesOn.sample_byOccurrence |
| `Flow.RunsDownOn.sample` | 605 | H | present | O | also Distinct es: a family holding what stands, sum once per member (L) |
| `Flow.RunsDownOn.sample_of_fine` | 616 | H | present | O | coarse amounts from fine ones |
| `Flow.sample_changes_iff` | 631 | H | present | O | also Distinct es: a family holding what stands, sum once per member (L) |
| `Flow.sample_comesToStand_iff` | 644 | H | present | O | coarse amounts from fine ones |
| `Flow.sample_ceasesToStand_iff` | 658 | H | present | O | coarse amounts from fine ones |
| `Strobe.alive_listed` | 862 | C | witness | T |  |

### Space (2)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `World.Finite` | 172 | D | enum | L | World.finite_iff: enumeration + decided identity; refutations need only enumeration (World.Enumerated.rests) |
| `World.Seedbank.distinct` | 849 | C | witness | T |  |

### Standpoints (2)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Flow.boundary_crossed` | 273 | H | family | F0 | refutation; membership-only |
| `Flow.region_not_a_cut` | 295 | H | family | F0 | refutation; membership-only |

### Units (1)

| Declaration | Line | Kind | Use | Status | Note |
|---|---|---|---|---|---|
| `Flow.RunsDownOnAt` | 271 | D | sum | L | as RunsDownOn |
