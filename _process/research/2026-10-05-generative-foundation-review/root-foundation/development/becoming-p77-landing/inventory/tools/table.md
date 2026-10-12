
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
