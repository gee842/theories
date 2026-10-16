# Manual classification of every core declaration that names `Distinct` (main tree, 12 Oct 2026).
# kind: H hypothesis of a law; C conclusion (construction or witness supplies listing once);
#       D definition; P only inside a proof.
# use: count, sum, enum, family, present, steps, tool, witness
# status: F0 free with no premise (refutation, membership-only hypotheses);
#         L local: decided identity among the members (law reads the sum/count once per member);
#         K kept: counts relata, local condition = decided identity among the counted;
#         O flow's list of what takes part: re-founded by occurrence for amounts;
#         N numbers / Fin / steps: identity decided by construction;
#         T toolkit or witness (not a law).
import collections, sys
C = {}
def add(mod, names, kind, use, status, note=""):
    for n in names.split():
        C[(mod, n)] = (kind, use, status, note)
add("Continuation", "Flow.fed_from_beyond_from Flow.rising_fed_from_beyond_from Flow.fed_from_beyond Flow.rising_fed_from_beyond", "H", "family", "F0", "conclusion a refutation; FedFromBeyond, Around, BalancesOn, takers>0 are membership-only; DecidableEq C already assumed")
add("Continuation", "Web.generation_fed_from_beyond", "H", "family", "F0", "as above")
add("Counting", "distinct_map_on placesBelow_distinct", "C", "tool", "T")
add("Counting", "EnclosedQueue.span_distinct places_listed", "C", "steps", "N", "lists of numbers / Fin K")
add("Counting", "World.enclosedQueue_dissipatesOn", "H", "family", "T", "shows a witness meets Dissipative (whose quantifier is over Distinct families)")
add("Counting", "World.finite_dissipation_binds", "C", "family", "T", "witness that dissipation binds (Premise.Binds .dissipative)")
add("Counting", "World.sheddingQueue_dissipative", "P", "family", "T", "proof that a witness is Dissipative")
add("Decidedness", "Counts.listing", "C", "tool", "T", "a count is a list's length; keeps listing once")
add("Decidedness", "length_eq_of_same", "H", "count", "T", "uniqueness of the count once per member (used by Numbers.unique)")
add("Decidedness", "Counts.listed_across Counts.listed_over_stretch", "H", "count", "K", "census lengths; local condition: decided identity among the listed (Numbers)")
add("Decidedness", "coming_steps_within ceasing_steps_within Recurs.steps_found", "H", "steps", "N", "Distinct lists of steps (Nat); the family `as` itself is not asked to be Distinct")
add("Dissipation", "total_le_at total_le_of_support", "H", "tool", "T", "sum once per member")
add("Dissipation", "insertNew_spec adjoin_spec", "C", "tool", "T", "listing once with DecidableEq")
add("Dissipation", "Flow.Dissipative", "D", "family", "L", "Flow.dissipative_iff: every closed family read once per member")
add("Dissipation", "Flow.Enclosed", "D", "family", "L", "Flow.enclosed_iff: some closed family with decided identity")
add("Dissipation", "Flow.Around", "D", "family", "L", "Flow.around_iff")
add("Dissipation", "Flow.enclosed_of_finite Flow.around_of_finite", "H", "enum", "L", "positive (∃ family); holds where identity among `all` is decided")
add("Dissipation", "Flow.Dissipative.gives_less", "H", "sum", "L", "sum once per member; fails with repetition (Lone.repeated_family)")
add("Dissipation", "Flow.Dissipative.opens", "H", "family", "F0", "proved: Flow.Dissipative.opens_listing")
add("Dissipation", "Flow.Dissipative.finite_ceases", "H", "enum", "F0", "proved: Flow.Dissipative.finite_ceases_listing")
add("Dissipation", "Flow.More.opens Flow.opens_of_arising Flow.rising_opens Flow.standing_opens Flow.rise_alone_opens", "H", "family", "F0", "refutation; as opens_listing")
add("Dissipation", "Flow.dissipatesOn_of_inward_at Flow.Dissipative.dissipatesOn_of_inward", "H", "sum", "L", "conclusion DissipatesOn ds t is a sum over ds")
add("Dissipation", "Flow.taking_draws_in", "H", "family", "F0", "proved: Flow.taking_draws_in_listing")
add("Dissipation", "Flow.taking_draws_in_from Flow.rising_draws_in_from Flow.rising_draws_in Flow.standing_draws_in", "H", "family", "F0", "refutation; as taking_draws_in_listing")
add("Dissipation", "Flow.standing_lowers", "H", "sum", "L", "proved: Flow.standing_lowers_listing, _decided; fails with repetition (Doubled.needs_once)")
add("Dissipation", "Flow.rising_ceases Flow.standing_ceases", "H", "enum", "F0", "refutation; as finite_ceases_listing")
add("Dissipation", "Frontier.frontier Lone.frontier", "H", "family", "F0", "refutation in a witness")
add("Dissipation", "Frontier.pool_fuel_distinct Rooted.growers_distinct Rooted.present_distinct", "C", "witness", "T")
add("Dissipation", "Rooted.rooted", "C", "witness", "T", "witness statement; its Distinct-quantified clause is a refutation")
add("Identity", "Flow.More.arising_never_stops_reidentified_covering Flow.More.unceasing_reidentified_covering Flow.More.unceasing_reidentified Flow.More.unceasingFrom", "H", "present", "K", "takers counted as relata; amounts re-founded by occurrence (O), counting relata keeps it (Repeated)")
add("Identity", "Web.arisesFrom_of_more forces_iff_noSplit paired_noSplit forced_iff_more", "H", "count", "K", "more listed after a step than before; forces_iff_noSplit already has DecidableEq F")
add("Identity", "Web.Census.balanceFrom_at Web.Census.balanceFrom_eq_at Web.Census.arisingFrom_of_ceasingFrom_from Web.Census.ceasingFrom_of_arisingFrom_from", "H", "count", "K", "census lengths under a continuation")
add("Identity", "Web.ceasingFrom_found Web.arisingFrom_found", "C", "steps", "N", "pairs at distinct steps")
add("Identity", "Dormant.no_split_without_arising", "C", "witness", "T")
add("Locality", "Web.StandingCensus.stock_eq", "H", "sum", "L", "total standing = stock over any family listed once holding what stands")
add("Locality", "Flow.RunsDownOn", "D", "sum", "L", "family holding what stands, once per member")
add("Locality", "ListsAt", "D", "count", "K", "census at one step; = Numbers of a listing")
add("Locality", "Covers.ceasing_steps_within ceasing_steps_found", "H", "steps", "N", "lists of steps")
add("Openness", "Web.StandingCensus.over_stretch_on", "H", "count", "K", "census of what stands")
add("Openness", "Flow.AroundStanding", "D", "family", "L", "as Around")
add("Openness", "Accretion.alive_distinct Few.distinct_pick Few.distinct_found", "C", "witness", "T")
add("Population", "Distinct", "D", "tool", "T", "the definition")
add("Population", "distinct_map length_le_of_matched length_le_of_sub count_le_of_sub distinct_remove marks_le_of_sub total_le_mark", "H", "tool", "T", "counting toolkit")
add("Population", "Listed", "D", "count", "K", "every census decides identity among the listed (Listed.identityDecided); any listing with a decision procedure gives one (Listed.of_listing)")
add("Population", "Listed.keeps_at Listed.across_at Listed.over_stretch_on Listed.ceasing_iff_shortfall_from Listed.coming_iff_excess_from", "H", "count", "K", "census lengths")
add("Population", "steps_distinct", "C", "steps", "N")
add("Population", "Web.DependenceCensus.over_stretch_on Web.Census.over_stretch_on Web.arises_of_more", "H", "count", "K", "census lengths")
add("Population", "Flow.takers_le_covering Flow.More.grows_covering Flow.More.grows Flow.More.arising_never_stops_covering Flow.More.unceasing_covering Flow.More.unceasing", "H", "present", "K", "takers counted as relata (Repeated shows it is needed); amounts re-founded by occurrence (O)")
add("Population", "Expansion.distinct Expansion.counted Cycle.distinct Cycle.counted Oscillation.pair Oscillation.counted Inactive.distinct Inactive.more_without_arising", "C", "witness", "T")
add("Population", "Repeated.more_without_arising", "C", "witness", "T", "boundary witness: without listing once, one formation counts as many")
add("Premises", "keep_distinct", "C", "tool", "T")
add("Premises", "listed_of_ever World.keep_lists World.counted_of_ever", "H", "enum", "L", "a census from a list covering all ever active; Listed.of_listing gives one from any listing with decided identity")
add("Premises", "World.Premise.Binds", "D", "family", "L", "dissipation binds: some family listed once closed and taken from")
add("Premises", "World.Hatch.kin_distinct World.FiniteHatch.kin_distinct", "C", "witness", "T")
add("Resolution", "Flow.quantum_bound Flow.uptake_bound Flow.replenishment_bound Flow.exchange_bound Flow.exchange_bound_of_least_loss", "H", "sum", "L", "bounds by the stock once per member")
add("Resolution", "Flow.quantum_not_recurring Flow.exchange_not_recurring Flow.exchange_not_recurring_of_least_loss", "H", "sum", "L", "refutation, but of an event stated by a sum over the family (stock or total take): reads the sum once per member")
add("Resolution", "Flow.taking_stops", "H", "family", "F0", "proved: Flow.taking_stops_listing")
add("Resolution", "Flow.taking_needs_refinement", "H", "family", "F0", "refutation; `split * stock = 0` is membership-only")
add("Resolution", "Flow.refinement_gives_nothing World.after_dissipative", "H", "family", "L", "premise quantifying over closed families once per member, as Dissipative")
add("Resolution", "Flow.DissipativeBy Flow.LosesAtEverySize", "D", "family", "L", "as Dissipative")
add("Resolution", "Flow.BalancesAt.gainers_lose Flow.BalancesAt.losers_lose", "H", "sum", "L", "counts of gainers/losers over a family once per member")
add("Resolution", "Asymptote.distinct Circulation.distinct Trickle.sides_distinct", "C", "witness", "T")
add("Resolution", "Emission.emitted_le_one Alternation.given_total Trickle.given_total Trickle.taken_le Trickle.loses_two", "H", "sum", "T", "sums over Distinct families inside witnesses")
add("Roles", "distinct_conditionsOf", "C", "tool", "T")
add("Roles", "Flow.roles_distinct", "H", "present", "T", "the role reading keeps listing once")
add("Roles", "Web.Embodied.arising_lowers", "H", "sum", "L", "stock once per member, as standing_lowers")
add("Roles", "Web.generation_opens Web.generation_draws_in_from Web.generation_draws_in Throughput.frontier", "H", "family", "F0", "refutation")
add("Roles", "Web.generation_ceases", "H", "enum", "F0", "proved: Web.generation_ceases_listing")
add("Roles", "Shuttle.distinct SprayShuttle.sides_distinct", "C", "witness", "T")
add("Roles", "Throughput.side_dissipates", "H", "sum", "T", "witness lemma")
add("Sampling", "total_gate", "H", "tool", "T")
add("Sampling", "Flow.unionPresent_spec", "C", "tool", "T")
add("Sampling", "Flow.Once", "D", "present", "O", "Flow.byOccurrence_once: every flow read by occurrence is Once")
add("Sampling", "Flow.sample_taken_on Flow.sample_given_on Flow.RunsDownOn.sample_of_fine Flow.sample_comesToStand_iff Flow.sample_ceasesToStand_iff", "H", "present", "O", "coarse amounts from fine ones")
add("Sampling", "Flow.BalancesOn.sample", "H", "present", "O", "proved: Flow.BalancesOn.sample_byOccurrence")
add("Sampling", "Flow.RunsDownOn.sample Flow.sample_changes_iff", "H", "present", "O", "also Distinct es: a family holding what stands, sum once per member (L)")
add("Sampling", "Strobe.alive_listed", "C", "witness", "T")
add("Space", "World.Finite", "D", "enum", "L", "World.finite_iff: enumeration + decided identity; refutations need only enumeration (World.Enumerated.rests)")
add("Space", "World.Seedbank.distinct", "C", "witness", "T")
add("Standpoints", "Flow.boundary_crossed Flow.region_not_a_cut", "H", "family", "F0", "refutation; membership-only")
add("Units", "Flow.RunsDownOnAt", "D", "sum", "L", "as RunsDownOn")

rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
decls = collections.OrderedDict()
for loc, kind, name, where, text in rows:
    mod = loc.split(':')[0].replace('.lean', '')
    short = name.replace('Becoming.', '', 1) if name.startswith('Becoming.') else name
    decls.setdefault((mod, short), loc)
missing = [k for k in decls if k not in C]
extra = [k for k in C if k not in decls]
print("MISSING", missing, file=sys.stderr)
print("EXTRA", extra, file=sys.stderr)
out = []
bymod = collections.OrderedDict()
for (mod, short), loc in decls.items():
    bymod.setdefault(mod, []).append((short, loc, C.get((mod, short), ("?", "?", "?", ""))))
stat = collections.Counter(); kindc = collections.Counter()
for mod, items in bymod.items():
    out.append(f"\n### {mod} ({len(items)})\n")
    out.append("| Declaration | Line | Kind | Use | Status | Note |")
    out.append("|---|---|---|---|---|---|")
    for short, loc, (k, u, s, note) in items:
        out.append(f"| `{short}` | {loc.split(':')[1]} | {k} | {u} | {s} | {note} |")
        stat[s] += 1; kindc[k] += 1
print("\n".join(out))
print("\nSTATUS", dict(stat), "KIND", dict(kindc), file=sys.stderr)
summary = collections.OrderedDict()
for mod, items in bymod.items():
    c = collections.Counter(x[2][2] for x in items); kc = collections.Counter(x[2][0] for x in items)
    summary[mod] = (len(items), kc, c)
print("\nSUMMARY", file=sys.stderr)
for mod, (n, kc, c) in summary.items():
    print(mod, n, dict(kc), dict(c), file=sys.stderr)
