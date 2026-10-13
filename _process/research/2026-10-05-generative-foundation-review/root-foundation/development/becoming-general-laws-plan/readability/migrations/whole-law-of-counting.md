# Migration map: whole-law-of-counting

Old record sha256 `1cdcb3cc570a5e586113edb0e4e35822a9a96ee0c700915feb4c5360bb382bd2`; snapshot `_process/architecture/history/1cdcb3cc570a5e58/whole-law-of-counting.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T4 “The tally is the whole law of counting: the tally is exactly the balance with no more ceas…” | title (statement of the result) | title (short name) + statement; T0 → laws 3–4; T1 → law 17; T2 → law 18; T3 → law 26; T4 → law 24 |
| C0 “Where the members of which a determination holds are listed at each step, each once (Liste…” | law | law 1 |
| C1–C2 “Call counts n at each step, c ceasing and a coming across it a tally (Tally) when at each …” | definition + law | law 2 |
| C3 “The tally is strictly stronger than the census balance n (t + 1) + c t = n t + a t (Balanc…” | law | law 3 |
| C4–C5 “Conversely every tally is counted by a queue: with natural numbers as members, at step t t…” | law | law 4 |
| C6 “So the counts some listing has are exactly the tallies (Tally.congr, tally_iff_counted), a…” | law | law 5 |
| C7 “Read of the activity of worlds: relata queuing with nothing flowing meet every premise but…” | law | law 6 |
| C8 “so a property of the counts holds of every census of every world exactly when it holds of …” | law | law 7 |
| C9–C10 “With only active relata giving, the two bind it together: in a world whose flow balances, …” | law | law 8 |
| C11 “That is all the eight premises add: an open queue, whose front gives one unit to each rela…” | law | law 9 (main clause) and law 10 (the parenthesis on openQueue_not_binds) |
| C12 “so a property of the counts holds of the census of every world meeting all eight exactly w…” | law | law 11 |
| C13 “its range includes worlds in which premises hold vacuously: where every premise binds, eve…” | law | law 12 |
| C14 “A second route binds counting without asking the giver to be active: in a world whose flow…” | law | law 13 (the law) and law 14 (its reason, “By that route”) |
| C15–C16 “With the eight premises named (World.Premise, Premise.Holds), a selection is a function to…” | definitions | law 15 |
| C17–C18 “Whatever its counts, a queue driven by a ground relatum never active (OpenQueue.driven, Wo…” | law | law 16 |
| C19–C20 “So under each of the 256 selections of the eight premises, a pointwise property of the cou…” | law | law 17 |
| C21 “Where every premise binds, each premise's condition having an instance (World.Premise.Bind…” | law | law 18 |
| C22–C23 “Across every step but T at which a queue closed once (OnceClosedQueue, World.onceClosedQue…” | witness | law 19 |
| C24–C25 “every relatum depends on every relatum at what it stands at, so the conditions of activity…” | witness | law 20 |
| C26–C27 “With nothing joining an empty queue and E more than join across T it meets all eight premi…” | law | law 21 |
| C28 “So in worlds in which every premise binds, a pointwise property of the counts holds under …” | law | law 22 |
| C29–C30 “No finite world binds every premise (World.Finite.not_binds: a census binds only where the…” | law | law 23 |
| C31 “In finite worlds where every premise but the census binds, a pointwise property of the cou…” | law | law 24 |
| C32 “Under each selection S, a pointwise property of the counts holds of every census of every …” | law | law 25 |
| C33 “So binding adds exactly that something is active (where activity needing support, only act…” | law | law 26 |
| C34 “The witnesses: a saturated web, every relatum depending on every relatum at what it stands…” | witness | law 27 |
| C35–C37 “without embodiment, a relay beside a queue handing one of two units on to a ground relatum…” | witnesses | law 28 |
| C38–C39 “Under enclosure change is also bounded;” | pointer | law 29 |
| C40 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and holders finitely many at each step;” | scope | standard_boundaries: discrete-steps; does_not_show[0] (holders finitely many) |
| L1 “needs decidability (a logical commitment) and pointwise properties (in place of function e…” | logical commitments | standard_boundaries: decidability, pointwise-properties |
| L2 “speaks only of counts, saying neither which member enters or leaves nor anything of relati…” | scope | does_not_show[1] |
| L3 “the queue worlds have infinitely many relata, each arising once;” | scope | does_not_show[2] |
| L4 “the laws of counting in finite worlds and under enclosure are in counting-under-enclosure;” | scope | does_not_show[3] |
| L5 “read of worlds only the counting of activity is stated, the counts of standing and depende…” | scope | does_not_show[4] (witness counting_laws) |
| L6 “the laws of counting under all eight premises and under each selection of them are given;” | law (positive) | law 17 (duplicate) |
| L7 “the witnesses under the selections all have infinitely many relata, the laws under each se…” | scope | does_not_show[2] and [3] |
| L8 “the range includes worlds in which premises hold vacuously: in the open queue dissipation,…” | scope | does_not_show[5] (vacuous premises, witness openQueue_not_binds); “are given” clauses → laws 22, 24, 25 (duplicates); the finite-selection pointer → does_not_show[3] |
| L9 “binding is an instance of each condition: in the queue closed once activity needing suppor…” | scope | does_not_show[6] (witness OnceClosedQueue.dependent_any_activity); the instance clause is law 20 |
| L10 “the webs of the queue closed once and the other witnesses are saturated, the weakest (ever…” | scope | does_not_show[2]; Web.saturated is law 27 |
| L11 “evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| L12 “the names (Tally, Queue, Pointwise, CountsObey, openQueue, drivenQueue, onceClosedQueue, P…” | names | standard_boundaries: names-provisional (the list of names and the gloss of the criteria → snapshot; see the history note) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of B…” | evidence | validation_scope (modules); counts and the named theorems stay in the receipt and the snapshot |
| V1–V2 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence | validation_scope |
| V3 “The author's counterreview is in §46, §52, §55 and §60 of the integration note;” | evidence | validation_scope (“four sections”; the section numbers → history note) |
| V4 “no independent review yet.” | evidence | validation_scope (“no independent review yet”) |
| V5 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause) |
| V6 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Locality); count 44 and label P48 → snapshot |
| V7–V8 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record’s local laws”); labels P50, P57–P61 → snapshot |
| R0–R12 “The full statement (P23) says that the laws of the whole exclude no unfolding beyond what …” | correspondence | correspondence (unchanged) |
| N0–N1 “The exact restatement for every world is this record's Listed.keeps_at (P50), the local co…” | local restatement appended to next | law 30; label P50 → history |
| N2 “the exact restatement for every world is laws-of-one-step (P48), of which this record's bi…” | local restatement appended to next | law 31; label P48 → history |
| N3 “the other laws follow the zero-premise plan;” | next step | next_delta (“local forms of the other laws, by the zero-premise plan”) |
| N4–N5 “a reading of binding in which each premise excludes something the representation allows, a…” | next step | next_delta |
| H0–H1 “Listing and decidability: as in census-balance; read of worlds, decided activity. It is a …” | premise | hypotheses (unchanged) |
| X0–X6 “Queue.lone_tally with World.queue and World.embodiedQueue: one relatum arising from none, …” | counterexamples | counterexamples (unchanged) |
