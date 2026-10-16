# Migration map: bounded-census-keeps-pace

Old record sha256 `29c7149c9522c8000addc585ee57acb86a199d6e54bf63ebd7d086e1aa215196`; snapshot `_process/architecture/history/29c7149c9522c800/bounded-census-keeps-pace.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `Listed.ceasing_of_coming` (bounded from `T` by `B`), `Listed.ceasing_of_returning` (within `K` at arbitrarily late steps), `Listed.coming_iff_ceasing`, `Web.ceasing_of_arising` and `Web.unceasing_iff_bounded` (decided activity), `World.CountedBy`/`CountedWithin` (a census with `length ≤ B t`), `CountedWithin.arising_iff_ceasing`, `Finite.census_bounded` (no decidability), `Finite.countedWithin` and `Finite.arising_iff_ceasing` (decided activity), `procession_world` (`CountedWithin 1`, both recur, not finite), `accretion_unbounded` (no `CountedWithin B` for any `B`), `CountedBy.arising_iff_ceasing`, `slow_world` (non-decreasing, unbounded `B`: `CountedBy B`, arising recurs, nothing ceases), `Listed.ceasing_of_outpacing`, `Web.StandingCensus.coming_iff_ceasing`, `Web.DependenceCensus.forming_iff_dissolving`. None is narrower or wider than the old text.

| Old text | Type | New place |
|---|---|---|
| T0 “Keeping pace under a bounded census” | title | title (unchanged) |
| S0–S1 “Where the list returns within some number …; under a bound growing without end, however slowly, arising can go on without ceasing.” | statement | statement (unchanged) |
| C0 “Where the members of which a determination holds are listed at each step, each once, from some step T on at most B at each step (Listed, with lists from then on no longer than B), and the determination is decided at each step, … (Listed.ceasing_of_coming).” | law | law 1 |
| C1–C2 “The proof goes through the census balance (census-balance): with coming to be recurring, the comings … accumulate past B (recurring_accumulates); where the list returns within B, … something ceases between (Listed.ceasing_iff_shortfall).” | law (proof route) | law 2; dependency on census-balance unchanged |
| C3 “So the bound need not hold at every step from some step on: the list need only return within some number K at arbitrarily late steps (Listed.ceasing_of_returning).” | law | law 3 |
| C4–C5 “P27 proved it from the lengths of the lists directly …; P30 proves it through the balance, and the three lemmas of that route, no longer used, are removed from the core.” | round narration | history (migration note) + snapshot; law 2 states the route through the balance |
| C6 “With the census law (ceasing-needs-arising), the two recur together (Listed.coming_iff_ceasing).” | law | law 4 (the bound from some step on, which `coming_iff_ceasing` takes, written in) |
| C7 “Read of activity: …(Web.ceasing_of_arising, Web.unceasing_iff_bounded).” | law | law 5 |
| C8 “Read of worlds: … (World.CountedWithin), arising recurs exactly when ceasing does (World.CountedWithin.arising_iff_ceasing);” | law | law 6 |
| C9 “every census of a finite world is bounded, with no decidability (World.Finite.census_bounded), and where activity is decided one exists (World.Finite.countedWithin), so the law of finite worlds, World.arising_iff_ceasing, is a case (World.Finite.arising_iff_ceasing);” | law | law 7 |
| C10 “in procession, … (World.procession_world), so the law reaches beyond finite worlds;” | law + counterexample | law 8; counterexamples[0] (unchanged) |
| C11 “accretion has a census without a bound, and arising recurs there while ceasing does not (World.accretion_unbounded).” | law + counterexample | law 8; counterexamples[0] (unchanged) |
| C12 “The bound may vary with the steps: … (World.CountedBy, of which CountedWithin is the case of a constant bound), … (World.CountedBy.arising_iff_ceasing).” | law | law 9 |
| C13–C15 “A bound growing without end, however slowly, does not keep the two together: … (World.slow_world); so under logarithmic growth, for instance, arising can still go on without ceasing.” | law + counterexample | law 10; counterexamples[1] (unchanged) |
| C16–C17 “Where the list grows without end, ceasing to be recurs where … (Listed.ceasing_of_outpacing); this is sufficient, not necessary, and in slow the comings never outnumber the bound.” | law | law 11 |
| C18 “Read of standing: … (Web.StandingCensus.coming_iff_ceasing).” | law | law 12 |
| C19 “Read of dependence: … (Web.DependenceCensus.forming_iff_dissolving).” | law | law 12 |
| C20 “For the form with rates, see census-balance.” | pointer | related (census-balance: “The form with rates …”, unchanged) |
| C21 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0–L1 “The bound must return within one number at arbitrarily late steps; it fails where the bound grows without end, however slowly (accretion, slow);” | scope | does_not_show[0] (witness World.slow_world) |
| L2 “that a non-decreasing bound either stays within some number or grows without end is classical;” | scope | does_not_show[1] (with R6–R7) |
| L3 “for a bound that is not monotone and eventually exceeds every number no corresponding world is given (its construction needs data from existence);” | scope | does_not_show[2] |
| L4 “stated for discrete steps;” | standard boundary | standard_boundaries: discrete-steps |
| L5 “needs decidability (a logical commitment);” | logical commitment | standard_boundaries: decidability; hypotheses[2] (unchanged) |
| L6 “says neither which member comes to be or ceases nor that the two are causally linked: the law is a count, not a mechanism;” | non-implication | does_not_show[3] |
| L7 “evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| L8 “the names (bounded census, procession, slow) are Ren's to choose.” | names | standard_boundaries: names-provisional; next_delta; the list of names → snapshot |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of Becoming.Population (added in P27: …; P30 adds …, removes ceases_or_kept, ceases_or_more and ceases_within, which receipt 20261009T163512.365801Z checked) and the 85 theorems of Becoming.Openness (added in P27: …; added in P30: …) all have empty axiom reports;” | evidence | validation_scope (modules and receipt); counts and per-round lists → receipt + snapshot; removed names and their receipt → history (migration note) |
| V1–V2 “the same receipt covers the package's 75 modules …; periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); counts → receipt + snapshot |
| V3 “The intermediate receipt 20261009T141236.619967Z (periphery 20261009T141402.494945Z) checked the version before the generalization.” | evidence (history) | history (migration note) + snapshot |
| V4–V5 “The author's counterreview is in §36, §37 and §40 of the integration note; no independent review yet.” | evidence | validation_scope (“three sections”); section numbers → history (migration note); “no independent review yet” is superseded within the same old paragraph by V7 |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V7–V8 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and its corrections are handled in §42 …; those corrections are not yet independently reviewed.” | evidence | validation_scope; review file stays in references; §42 → history (migration note) |
| V9 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Becoming.Locality); count and label → snapshot |
| (references, proof_bindings) Dependence.lean and Generation.lean bound to receipt 20261014T091930.724493Z | evidence | validation_scope now names that receipt, which the proof bindings already used |
| R0–R1 “Section 26's law of a finite family (coming_recurs_iff, Web.unceasing_iff) needs one fixed finite family holding every member; here only the list at each step needs a bound …” | correspondence | correspondence (“section 26's law” → “the law of a finite family (coming-and-ceasing-keep-pace: …)”) |
| R2 “So what section 30's law, that in a finite world whose activity is decided arising recurring and ceasing recurring are one part, needs is a bound on the count, not finiteness.” | correspondence | correspondence (“section 30's law” → “the law of finite worlds (space-and-its-parts: …)”) |
| R3–R5 “With the census law, the relation of arising and ceasing falls into three tiers by counting: …” | correspondence | correspondence (unchanged) |
| R6–R7 “That the first two tiers exhaust the counts finite at each step is classical; the pure core states the two sides separately.” | scope | does_not_show[1] (joined with L2) |
| R8–R10 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R11–R12 “This is a reading of activity and standing, arising and ceasing being names Ren confirmed (…); whether it is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘…’ …).” | reading + Ren's words | correspondence (unchanged; Ren's words verbatim and attributed) |
| R13 “It evaluates neither arising nor ceasing.” | standard boundary | standard_boundaries: no-evaluation |
| N0 “Names (Ren).” | next step | next_delta |
| N1 “What remains where the bound grows slowly is answered in P30: however slowly it grows, arising can go on without ceasing (World.slow_world);” | answered next step | law 10; label → history (migration note) |
| N2 “the exact criterion is the shortfall (Listed.ceasing_iff_shortfall);” | law | law 11 (last clause) |
| N3 “the rate form (Listed.ceasing_of_outpacing) is sufficient, and slow never meets it.” | law | law 11 |
| H0 “A listing bounded from some step on: …; there may be infinitely many members in all. The world premise CountedWithin … The more general form …” | premise | hypotheses[0] and [1] (split, wording unchanged; one item exceeded the item cap) |
| H1 “Decidability: …” | premise | hypotheses[2] (unchanged) |
| H2 “procession_world, accretion_unbounded and Finite.countedWithin …” | premise | hypotheses[3] (unchanged) |
| H3 “slow_world asks …; ceasing_of_outpacing asks …” | premise | hypotheses[4] (unchanged) |
| X0 “accretion: …; procession: …” | counterexample | counterexamples[0] (unchanged) |
| X1 “slow: …” | counterexample | counterexamples[1] (unchanged) |
