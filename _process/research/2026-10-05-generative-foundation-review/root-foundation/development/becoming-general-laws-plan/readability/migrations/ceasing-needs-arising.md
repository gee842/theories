# Migration map: ceasing-needs-arising

Old record sha256 `99c9b588486444406b41f355c557e044b8fee5fd1133d11bcd0aaa9fcc3e7574`; snapshot `_process/architecture/history/99c9b58848644440/ceasing-needs-arising.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `Listed.coming_of_ceasing` (with the section's decidability of the determination), `Web.arising_of_ceasing` (decided activity), `World.arising_of_ceasing`, `Web.StandingCensus.coming_of_ceasing` (no decision: a positive level is decidable), `Web.DependenceCensus.forming_of_dissolving` (decided requiring), `World.census_one_way`, `coming_of_ceasing_covered` with `Listed.covered`, and `Covers.ceasing_not_recurring` (undecided section). None is narrower or wider than the old text.

| Old text | Type | New place |
|---|---|---|
| T0 “The census law” | title | title (unchanged) |
| S0–S1 “Where what holds is listed at each step, ceasing to be recurring needs coming to be recurring; the converse fails.” | statement | statement (unchanged) |
| C0 “Where the members of which a determination holds are listed at each step, each once (Listed), and the determination is decided at each step, members ceasing to hold at arbitrarily late steps need …” | law | law 1 |
| C1 “The proof goes through the census balance (census-balance): with ceasing to be recurring, the ceasings from any step N on accumulate past the list at N …” | law (proof route) | law 2; the dependency on census-balance is unchanged |
| C2 “P26 and P27 proved it from the lengths of the lists directly …” | round narration | history (migration note) + snapshot |
| C3 “P30 proves it through the balance, and the three lemmas of that route, no longer used, are removed from the core.” | round narration | law 2 (the proof goes through the balance); the removal → history (migration note) + snapshot |
| C4 “A census is the listing of activity (Web.Census): under a census, ceasing recurring needs arising recurring (Web.arising_of_ceasing);” | law | law 3 |
| C5 “read of worlds, in a world with a census whose activity is decided, ceasing recurs only where arising recurs (World.arising_of_ceasing).” | law | law 3 (World.Counted among the declarations) |
| C6 “Read of standing: under a census of what stands …” | law | law 4 |
| C7 “Read of dependence: where the dependences of each step are listed …” | law | law 4 |
| C8 “Not conversely: accretion has a census, and arising recurs in it while nothing ever ceases;” | law + counterexample | law 5; counterexamples[0] (unchanged) |
| C9 “attrition keeps ceasing while nothing arises, so by this law it has no census (World.census_one_way).” | law + counterexample | law 5; counterexamples[0] (unchanged) |
| C10–C11 “The converse holds where the list is bounded; see bounded-census-keeps-pace.” | converse (pointer) | does_not_show[2] (kind converse, witness World.census_one_way); related (bounded-census-keeps-pace, unchanged) |
| C12 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and members finitely many at each step;” | scope | standard_boundaries: discrete-steps; finitely many at each step stays in hypotheses[0] |
| L1 “needs the determination decided (a logical commitment);” | logical commitment | standard_boundaries: decidability; hypotheses[1] (unchanged) |
| L2 “says neither which member comes to be nor that coming to be and ceasing to be are causally linked: the law is a count, not a mechanism;” | non-implication | does_not_show[0] |
| L3 “recurrence gives no frequency;” | scope | does_not_show[1] |
| L4 “evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| L5 “names are Ren's to choose.” | names | standard_boundaries: names-provisional; next_delta |
| L6 “Its form that ceasing does not recur needs no decision (Covers.ceasing_not_recurring in laws-of-one-step).” | law | law 7 (in the wording of laws-of-one-step) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of Becoming.Population (P27 generalizes …; P30 … removes comes_or_held …, which receipt 20261009T163512.365801Z checked) and the 85 theorems of Becoming.Openness (…) all have empty axiom reports;” | evidence | validation_scope (the modules and receipt); counts, the generalization and the removed names → snapshot; the removal receipt → history (migration note) |
| V1–V2 “the same receipt covers the package's 75 modules … periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); module and theorem counts → receipt + snapshot |
| V3 “The P26 version's receipt is 20261009T135303.461724Z.” | evidence (history) | history (migration note) + snapshot |
| V4–V5 “The author's counterreview is in §35, §36, §37 and §40 of the integration note; no independent review yet.” | evidence | validation_scope (“four sections of the integration note”); the section numbers → snapshot. “No independent review yet” is superseded within the same old paragraph by V7, which names the eleventh independent review; validation_scope keeps V7 |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail → receipt + snapshot |
| V7–V8 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and its corrections are handled in §42 of the integration note; those corrections are not yet independently reviewed.” | evidence | validation_scope; the review file stays in references; §42 → snapshot |
| V9 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Becoming.Locality); count and label → snapshot |
| (references, proof_bindings) Dependence.lean and Generation.lean bound to receipt 20261014T091930.724493Z | evidence | validation_scope now names that receipt, which the proof bindings already used |
| R0–R1 “Section 26's law says that in a finite family coming to be recurs exactly when ceasing to be does (coming_recurs_iff, Web.unceasing_iff); with infinitely many relata the two separate (Accretion, Attrition).” | correspondence | correspondence (“section 26's law” → “the law of a finite family (coming-and-ceasing-keep-pace)”, the record that holds it) |
| R2 “This result shows that the separation needs infinity in one direction only: …, while recurring coming to be does not need recurring ceasing to be.” | correspondence | correspondence (last clause → “but not conversely”) |
| R3–R4 “The law holds of any determination whose holders are listed at each step; activity and standing are two readings of it, matching section 26's one change read of activity, dependence and standing.” | correspondence | correspondence (“section 26's” → “that record”) |
| R5–R6 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R7–R8 “This is a reading of activity and standing, arising and ceasing being names Ren confirmed (2026-10-09-arising-ceasing-names); whether it is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘…’ …).” | reading + Ren's words | correspondence (“This is a reading of activity and standing” folded into R4's sentence; Ren's words verbatim and attributed, the AI's gloss unchanged) |
| R9 “It does not make ceasing good or bad.” | standard boundary | standard_boundaries: no-evaluation |
| R10 “One use of the result is the rest theorem (World.comes_to_rest_unrefuted of continued-change-needs-openness): …, neither of which can be dropped (World.rest_needs_census, World.rest_needs_standing).” | application | related (continued-change-needs-openness: “The rest theorem uses this law to stop ceasing, so only whatever arises needs to be embodied.”, unchanged); the two censuses being needed are that record's laws; the sentence → snapshot |
| N0 “The exact restatement for every world is laws-of-one-step (P48), of which this record's world and standing readings (World.arising_of_ceasing, Web.StandingCensus.coming_of_ceasing) are corollaries;” | local form appended to next | law 6 (in the wording of laws-of-one-step); dependency on laws-of-one-step unchanged; label P48 → snapshot |
| N1 “names (Ren).” | next step | next_delta |
| N2 “The reading of dependence and the version with rates are given in P28 (…; census-balance), and the derivation from the balance in P30.” | round narration | law 4 (dependence), law 2 (through the balance), related (census-balance, unchanged); labels → history (migration note) |
| H0 “Listing: …” | premise | hypotheses[0] (unchanged) |
| H1 “Decidability: …” | premise | hypotheses[1] (unchanged) |
| H2 “census_one_way is a statement about two particular worlds, with no premise.” | premise | hypotheses[2] (unchanged) |
| X0 “accretion: …; attrition: …” | counterexample | counterexamples[0] (unchanged) |
