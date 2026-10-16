# Migration map: generation-is-replenishment

Old record sha256 `fc40c6fd2dc8ed87d6225cd58b6ccb2f3f5b90ef8081132a3bf9fbcff682e203`; snapshot `_process/architecture/history/fc40c6fd2dc8ed87/generation-is-replenishment.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0 “Generation is replenishment: the arising of an embodied relatum itself needs replenishment…” | title (statement of the result) | title (short name) + statement |
| C0–C1 “Read webs and flows with one kind of relatum.” | law | law 1 |
| C2–C3 “Its arising therefore replenishes every family containing it, and where embodied members o…” | law | law 2 |
| C4–C5 “A formation giving to a family dissipated on takes from it, so the arising of an embodied …” | law | law 3 |
| C6 “So under dissipation a finite family without repetition in which embodied members arise at…” | law | law 4 |
| C7 “That exchange need not touch the family: with a sink exchanging with ever new relata, no s…” | witness | law 5 |
| C8–C9 “Where the family is enclosed around from some step on, some finite family without repetiti…” | law | law 6 |
| C10 “The premise of dissipation_generation_not_recurring (a quantity that never rises and is lo…” | law | law 7 (“dissipation_generation_not_recurring” → “the general law that generation does not recur”, its declaration) |
| C11 “Each premise is needed: two sides handing one standing back and forth generate, embodied a…” | witness | law 8 |
| C12 “when the holder also burns a fresh fuel at every step, the handing goes on under dissipati…” | witness | law 9 |
| C13–C14 “a relatum whose activity is not its standing arises without end in a dissipative world of …” | witnesses | law 8 |
| C15 “These requirements follow the rise of standing, not activity: in a balanced flow every ris…” | law | law 10 |
| C16–C17 “Coming to stand (the level zero before a step and positive after, Web.ComesToStand) is the…” | law + witness | law 11 |
| C18 “A member of a family dissipated on rising lowers the family's stock (Flow.rise_lowers_on, …” | law | law 12 |
| C19–C20 “under dissipation, a finite family without repetition whose members rise at arbitrarily la…” | law | law 13 |
| C21 “An embodied relatum comes to stand as it arises (Embodied.comesToStand), and the conclusio…” | law | law 14 |
| C22 “A relatum standing as a condition while active, absent at some step and active later, came…” | law + witness | law 15 |
| C23 “a relatum standing as a condition throughout wakes without end with nothing given to it, n…” | witness | law 16 |
| C24 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “the conclusions about embodiment constrain only the arising of embodied relata, and arisin…” | scope | does_not_show[0] (witness Flicker.flicker) |
| L2 “the general conclusions constrain coming to stand, not waking from dormancy (Sleeper);” | scope | does_not_show[1] (witness Sleeper.sleeper) |
| L3 “Embodied is a representational premise, and remains, seed banks and inactive conditions ar…” | correspondence | does_not_show[2] (“came_to_stand, Provisioned and Sleeper” → “coming to stand before activity and waking”, laws 15–16); hypotheses[1] |
| L4 “dissipation is a physical premise with commensurable units;” | correspondence | does_not_show[3]; hypotheses[4] |
| L5 “generation_opens constrains only generation recurring in one finite family, its conclusion…” | non-implication + scope | does_not_show[4] (witness SprayShuttle.opens_anyway) and does_not_show[5] |
| L6–L7 ““finite” means a finite family of relata;” | scope | does_not_show[6] |
| L8 “the final choice of names is Ren's.” | standard boundary | standard_boundaries: names-provisional |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 28 theorems added…” | evidence | validation_scope (the modules and kinds of theorems, empty axiom reports); counts and round labels (P17, P18b) stay in the receipt, history and snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §20 and §24 of the integration note;” | evidence | validation_scope (§20, §24) |
| V3 “the part in §24 was examined by the eighth independent review (BECOMING-P16C-P17-P18-REVIE…” | evidence (review) | validation_scope (an independent review, listed under sources, accepts the mathematics; corrections handled in the integration note); the review file and §27 stay under sources and in the snapshot |
| V4 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V5 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | round labels | history (P57–P61 entries) + snapshot |
| R0–R7 “The fifth independent review (I3) found that in the flow form arising contributes only the…” | correspondence | correspondence (unchanged) |
| N0 “The exact restatement for every world is this record's Flow.BalancesOn.standing_given, Bal…” | local restatement appended to next | law 17 (its thirteen declarations); round label P57 → history |
| N1 “Flow.Balances.standing_given, Balances.rise_replenishes, rising_needs_replenishment, stand…” | corollaries | law 17 (“the global forms above are its corollaries”; their names are declarations of laws 1–13) |
| N2–N5 “how far generation must be read as embodied (Ren);” | next step | next_delta |
| H0 “The flow balances the web; families and the relata taking part at each step are finite lis…” | premise | hypotheses[0] (unchanged) |
| H1 “Embodied is a representational premise about the arising relata: each stands as a conditio…” | premise | hypotheses[1]–[3] (split at “Arising that is not embodied” and “It is read under”, wording unchanged) |
| H2 “Dissipation (Dissipative, see no-finite-part-bears-taking) is a physical premise, used onl…” | premise | hypotheses[4] and [5] (split at “The conclusion of generation_opens”, wording unchanged) |
| X0–X5 “Without dissipation, embodied generation can be unceasing in a closed finite world (Shuttl…” | counterexamples | counterexamples (unchanged) |
