# Migration map: counting-under-enclosure

Old record sha256 `d9fbce244cb4e3803237deacfd4789efe1f64caf59a4987919fde6822c11a078`; snapshot `_process/architecture/history/d9fbce244cb4e380/counting-under-enclosure.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T6 “Enclosure bounds change: with every step from some step on enclosed, the relata active tog…” | title (statement of the result) | title (short name) + statement; T0 → law 3; T1 → laws 6–7; T2 → law 14; T3 → law 22; T4 → law 24; T5 → laws 26–27; T6 → laws 31–32 |
| C0 “Say that B bounds change from step T (ChangeBound T B n c a) when at every step t from T o…” | definition | law 1 (ChangeBound’s arguments T B n c a → the declaration) |
| C1–C2 “Within a change bound change does not recur (ChangeBound.not_recurring);” | law | law 2 |
| C3 “Enclosure bounds change: in a world with a census of activity whose relata are all embodie…” | law | law 3 |
| C4–C5 “Conversely an enclosed queue (EnclosedQueue, World.enclosedQueue) has natural numbers as m…” | witness | law 4 (EnclosedQueue → its world World.enclosedQueue) |
| C6 “Every step is enclosed by its span (World.enclosedQueue_enclosed), and the queue meets all…” | witness | law 5 |
| C7 “So a pointwise property of the counts holds of the census of every world meeting all eight…” | law | law 6 |
| C8 “Such a queue never reaches past its B + B * B-th member (Queue.reached, ChangeBound.joins,…” | law | law 7 (FiniteQueue → World.finiteQueue) |
| C9 “In the finite queue dissipation binds and the bound is attained: with one member replaced …” | law | law 8 |
| C10 “That change does not recur cannot be strengthened to an end step: if every tally with a ch…” | law | law 9 (Swap kept in the text) |
| C11 “Under each selection of the premises: at an enclosed step balance, dissipation and embodim…” | law | law 10 |
| C12 “Whatever its counts, the enclosed queue takes only while active (World.enclosedQueue_takin…” | law | law 11 |
| C13–C14 “A queue closing at step T (EnclosedQueue.closing, World.closingQueue) has every relatum ex…” | witness | law 12 |
| C15 “Say a selection bounds change (World.BoundsChange) when it selects balance, embodiment and…” | definition | law 13 |
| C16–C17 “So in worlds with every step from some step on enclosed, under each selection of the eight…” | law | law 14 |
| C18 “The second condition carries its step: that change does not recur within the bound (Change…” | law | law 15 |
| C19–C20 “Without dissipation enclosure leaves counting free: the enclosed queue with bound zero cou…” | law | law 16 |
| C21 “So under enclosure a change bound from some step, with nothing arising from then on across…” | law | law 17 |
| C22 “Every step of a finite world is enclosed (World.Finite.enclosed), so there balance, embodi…” | law | law 18 |
| C23–C24 “Conversely, seat the members of a queue in turn round a ring of N places (Ring.slot: membe…” | construction | law 19 |
| C25 “Where at most M are in the queue at each step, a ring of 2M + 1 places (Ring.size) holds t…” | construction | law 20 |
| C26–C28 “A ring with nothing standing meets every premise but embodiment (World.ring, World.ring_me…” | witnesses | law 21 |
| C29–C31 “So in finite worlds, under each selection of the eight premises, a pointwise property of t…” | law | law 22 |
| C32–C34 “That nothing arises across a step at which nothing is active is a law in finite worlds und…” | law | law 23 |
| C35–C36 “Finite worlds and worlds enclosed from some step on have the same laws of counting under a…” | law | law 24 |
| C37 “With enclosure from some step on, in worlds meeting the eight in which every premise binds…” | law | law 25 |
| C38 “More generally, with enclosure from some step on, under each selection S, a pointwise prop…” | law | law 26 (characterization) and law 27 (the iff clause) |
| C39–C40 “The witnesses: the relay is enclosed at every step and the lossy queue from the step after…” | witnesses | law 28 |
| C41–C42 “with balance, embodiment and dissipation but neither only active relata giving nor only ac…” | witnesses | law 29 |
| C43 “No finite world binds the census, so under a selection with the census every property is a…” | law | law 30 |
| C44–C46 “Under each selection S without it, a pointwise property of the counts holds of every censu…” | law | law 31 |
| C47 “So in finite worlds binding adds exactly that something is active (where activity needing …” | law | law 32 (characterization) and law 33 (its reason) |
| C48 “The witnesses are finite rings with saturated webs: without embodiment, a relay beside a r…” | witness | law 34 |
| C49 “with embodiment, without balance and with dissipation or only active relata giving, a loss…” | witness | law 35 |
| C50–C51 “with embodiment, without dissipation, and without only active relata giving where balance …” | witnesses | law 36 |
| C52 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and activity finite at each step;” | scope | standard_boundaries: discrete-steps; does_not_show[0] |
| L1 “needs decidability (a logical commitment) and pointwise properties (in place of function e…” | logical commitments | standard_boundaries: decidability, pointwise-properties |
| L2 “speaks only of the counting of activity, the counts of standing and dependence under the p…” | scope | does_not_show[1] |
| L3 “the change bound is the total standing at enclosure, which can be attained but is not the …” | scope | does_not_show[2] (witness World.replaced_attains) |
| L4 “the bound counts steps of change, not events;” | scope | does_not_show[3] |
| L5 “in the enclosed queue activity needing support and bounded transmission hold vacuously (no…” | correspondence | does_not_show[4]; the World.binding_counting/World.Binds pointer stays in whole-law-of-counting; the enclosed binding clause → law 25 (duplicate) |
| L6 “no finite world binds every premise (World.Finite.not_binds), the laws in finite worlds wh…” | scope | does_not_show[5]; the per-selection finite clause → laws 31, 34–36 (duplicate) |
| L7 “the laws under enclosure from some step on where the premises of each selection bind are t…” | law (positive) | laws 26–29 (duplicate) |
| L8 “change does not recur, and an end step needs omniscience in general;” | non-implication | does_not_show[6] (witness ChangeBound.lpo_of_ends) |
| L9 “the laws under each selection with enclosure are given, the condition where change is boun…” | law (positive) | laws 14–15 (duplicate) |
| L10 “the laws under each selection in finite worlds are given, the finite witnesses being rings…” | law (positive) | laws 20–22 (duplicate) |
| L11 “evaluates neither arising, ceasing nor rest;” | standard boundary | standard_boundaries: no-evaluation; correspondence R10 (duplicate, “nor rest”) |
| L12 “the names (occurrences, ChangeBound, EnclosedQueue, enclosedQueue, FiniteQueue, finiteQueu…” | names | standard_boundaries: names-provisional (the list of names and the gloss → snapshot; see the history note) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of B…” | evidence | validation_scope (modules); counts and the named theorems stay in the receipt and the snapshot |
| V1–V2 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence | validation_scope |
| V3 “The drafts were checked by the thirteenth independent review (BECOMING-P32-P34-REVIEW.md) …” | evidence (review) | validation_scope (thirteenth review, listed under sources; U4–U6 → history note) |
| V4 “the rebuilt result has no independent review yet, and the author's counterreview is in §49…” | evidence | validation_scope (“no independent review yet”; “four sections”, numbers → history note) |
| V5 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause) |
| V6 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Locality); count 44 and label P48 → snapshot |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record’s local laws”); labels P57–P61 → snapshot |
| R0–R10 “The rest theorem (ceasing-needs-arising, continued-change-needs-openness) says change does…” | correspondence | correspondence (unchanged) |
| N0 “The exact restatement for every world is laws-of-one-step (P48), of which this record's en…” | local restatement appended to next | law 37; label P48 → history |
| N1 “the other laws follow the zero-premise plan;” | next step | next_delta (“local forms of the other laws, by the zero-premise plan”) |
| N2 “names (Ren).” | next step | next_delta |
| H0–H2 “Listing and decidability: as in whole-law-of-counting; read of worlds, decided activity. I…” | premise | hypotheses (unchanged) |
| X0–X3, X5 “Swap with ChangeBound.lpo_of_ends: replacing one member at the first true of a Boolean seq…” | counterexamples | counterexamples (unchanged) |
| X4 “World.finite_binding_joint_iff and World.finite_binding_census: with embodiment selected b…” | counterexample | counterexamples[4] (“than in P45” → “than where nothing is enclosed (whole-law-of-counting)”) |
