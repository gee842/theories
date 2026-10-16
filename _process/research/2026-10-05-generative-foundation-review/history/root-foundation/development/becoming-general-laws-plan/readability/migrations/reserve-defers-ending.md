# Migration map: reserve-defers-ending

Old record sha256 `0cb44d6e77dbd5b85eba3e7334e6e2ea51adcaf44067fc0deb3e6b49be27282a`; snapshot `_process/architecture/history/0cb44d6e77dbd5b8/reserve-defers-ending.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0 “A reserve defers the end and does not escape it: Dependent is the zero reserve, a reserve …” | title (statement of the result) | title (short name) + statement |
| C0–C1 “On webs, a reserve is an amount for each formation that does not rise across a step at whi…” | definition + law | law 1 |
| C2–C3 “A reserve can be a held condition: in a balanced flow, a condition nothing gives to at ste…” | law | law 2 |
| C4 “Where no held condition is represented, the reserve is supplied: no condition of the two s…” | law | law 3 |
| C5 “An active formation whose dependences fail has a positive reserve (Carries.pos), so where …” | law | law 4 |
| C6 “This re-describes the reserve and is no further fact about the unfolding.” | non-implication | does_not_show[4] |
| C7 “The two readings differ in which events undermine: the fox's event at step one undermines …” | law | law 5 |
| C8 “A reserve defers the end and does not escape it: a formation unsupported from some step on…” | law | law 6 |
| C9–C10 “So after a loss without return with the dependence unchanged (Carries.consumed_lasts), and…” | law | law 7 (consumed_ends_when_fixed, coextinct → “ending when fixed and coextinction”, its declarations) |
| C11–C12 “Dormancy defers in the same way: unsupported, a formation does not arise at arbitrarily la…” | law | law 8 |
| C13 “Where the reserve so decays, coextinction runs down a chain of dependence of any length li…” | law | law 9 |
| C14–C15 “with the zero reserve every link ends at T, coextinction at once (chainEnd_zero).” | law | law 10 |
| C16–C17 “A food chain is a finite chain;” | law | law 11 |
| C18 “Without excluded middle that end step does not follow in general: if every formation never…” | law | law 12 (“the twelfth review's probe” → history, P33b entry) |
| C19–C20 “Witnesses: a seed in the dark wakes twice on its reserve and never again, awake exactly as…” | witnesses | law 13 |
| C21 “a fox depending on the embodied hare outlives it by exactly two steps on its fat, a condit…” | witness | law 14 |
| C22–C23 “in a chain in which each relatum depends at need one on the one before it, the bound along…” | witnesses | law 15 |
| C24 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “Carries and the held condition are representational premises;” | premise | hypotheses[0], [2] (duplicate) |
| L2 “the conclusions bind a formation unsupported from some step on, not whether support return…” | non-implication | does_not_show[0] |
| L3 “under Carries dormancy uses no reserve, and the time of dormancy is bounded only under the…” | scope | does_not_show[1] (witness Seed.not_decays) |
| L4 “the quantitative bound needs decidable activity;” | premise (decidability) | hypotheses[0] (duplicate); standard_boundaries: decidability |
| L5 “lagged coextinction along chains of dependence is bounded only where the reserve decays: w…” | non-implication | does_not_show[2] (witness Web.lpo_of_ending) |
| L6 “the bound along each finite chain reaching a relatum is given by chain_ends, while the for…” | scope | does_not_show[3]; next_delta |
| L7 “the general construction of the transformed reading needs decidable support;” | premise (decidability) | hypotheses[4] (duplicate); standard_boundaries: decidability |
| L8 “carries_of_held counts any uptake by the formations taking part, not only the holder's (th…” | scope | does_not_show[5] (“the review's Larder probe” → history) |
| L9 “the two readings differ in living, and which is used is a correspondence premise;” | correspondence | does_not_show[6] |
| L10 “the witnesses are minimal.” | scope | does_not_show[7] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): this record's theorem…” | evidence | validation_scope; the count (72) stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §24 of the integration note;” | evidence | validation_scope (§24) |
| V3 “the eighth independent review (BECOMING-P16C-P17-P18-REVIEW.md) accepts its mathematics, a…” | evidence (review) | validation_scope (independent reviews listed under sources accept the earlier mathematics); the review file and §27 stay under sources and in the snapshot |
| V4 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V5 “The periphery bridge reran successfully (20261013T095049.338744Z).” | evidence | validation_scope (periphery bridge) |
| V6 “The chain coextinction and Cascade added in P31 have the author's counterreview in §41 of …” | evidence (review) | validation_scope (§41; “not yet independently reviewed” kept as written, though the P33b history entry records the twelfth review’s probes of the chain laws: left for the integrator) |
| V7 “This record's local laws (P63, P61b) are in the same receipt, with empty axiom reports.” | round labels | history (P63, P61b entries) + snapshot |
| R0–R10 “Since P6 the open programme has listed ‘relax Dependent (buffers, reserves, lag)’;” | correspondence | correspondence (unchanged) |
| N0–N2 “The exact restatement for every world is this record's Web.CarriesAcross, DecaysAcross, ca…” | local restatement appended to next | law 16; round label P63 → history |
| N3 “Web.carries_zero, Carries.pos, active_not_recurring, step, lasts, arising_not_recurring, d…” | corollaries | law 16 (“the global forms above are its corollaries”) |
| N4–N7 “the least bound over the chains of a graph;” | next step | next_delta |
| H0–H4 “Carries, like Dependent, is a representational premise: which amount carries a formation, …” | premise | hypotheses[0]–[4] (unchanged) |
| H5 “chain_ends and chain_ends_of_em further use, for a chain of n links: the relata depended o…” | premise | hypotheses[5] and [6] (split at “The conclusion holds of the relata up to the nth”, wording unchanged) |
| X0–X5 “A seed in the dark fails Dependent and its reserve carries it: it arises twice and is neve…” | counterexamples | counterexamples (unchanged) |
