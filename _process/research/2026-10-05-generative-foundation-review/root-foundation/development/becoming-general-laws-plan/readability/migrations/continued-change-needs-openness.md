# Migration map: continued-change-needs-openness

Old record sha256 `cc75eaea2fc1125646ec48c411e22758376d04a2b0cab1ca8f1114c92cada3bf`; snapshot `_process/architecture/history/cc75eaea2fc11256/continued-change-needs-openness.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T3 “Openness and the rest theorem: across steps enclosed around what stands, the total standin…” | title (statement of the result) | title (short name) + statement; T0’s “never rises” → law 2; T1’s “need not be finite though not unboundedly many” → law 10; T3 → law 22 |
| C0 “Where what stands at each step is listed, each once (Web.StandingCensus), a step is enclos…” | definition | law 1 |
| C1–C2 “Under balance and dissipation, across such a step the total standing falls by at least the…” | law | law 2 |
| C3–C4 “So where every step from some step on is enclosed around what stands, no condition's stand…” | law | law 3 (“(stills)” → history note; declaration Flow.change_stops_unrefuted_around) |
| C5 “Read of worlds: where what stands is listed, whatever arises is embodied, the flow balance…” | law | law 4 |
| C6 “The rest theorem: a world with a census of what is active and of what stands, whose arisin…” | law | law 5 |
| C7 “That standing stops changing from some step on cannot be refuted, so that embodied arising…” | law | law 6 |
| C8 “the census is a list covering what is active, under which ceasing recurring leaves a later…” | law | law 7; label P58 → history |
| C9 “Both censuses are needed: in attrition nothing stands and nothing flows, every other premi…” | law | law 8 |
| C10–C11 “in throughput what is active is listed, whatever arises is embodied, the flow balances and…” | law | law 9 |
| C12–C13 “So the world itself need not be finite, but finitely many must stand and finitely many be …” | law | law 10 |
| C14 “The stronger form, some list holding every member that ever holds, needs omniscience in ge…” | law | law 11 (“the twelfth review’s probe” → history, P33b entry) |
| C15–C16 “The exchange does not recur either: across a step enclosed around what stands, a formation…” | law | law 12 |
| C17 “This needs only the census of what stands, balance, dissipation and enclosure, neither the…” | law | law 13 |
| C18–C20 “without dissipation in the cycle of Becoming.Flow, its one condition standing throughout, …” | law | law 14 |
| C21 “Its cases: a finite world lists what stands and is enclosed around it at every step (World…” | law | law 15 |
| C22–C23 “where every relatum is embodied, the census of what is active lists what stands (World.res…” | law | law 16 |
| C24 “Read the other way, arising without end in such a world is incompatible with every step fr…” | law | law 17 |
| C25–C26 “The eight premises decide neither enclosure nor openness: the sides of Shuttle, also takin…” | law | law 18 |
| C27 “its total standing is one at every step, the holder falling across each, and the ground re…” | law | law 19 |
| C28–C29 “nor does openness with the eight give arising without end: a holder taking a unit from eac…” | law | law 20 |
| C30 “in hatch, where every premise binds (hatch_binds of map-of-premises), the child arises and…” | law | law 21 |
| C31 “every premise binding does not bring rest: in a queue closed once in which one member repl…” | law | law 22 |
| C32 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “The exchange coming to rest is stated as no exchange at arbitrarily late steps (a negated …” | non-implication | does_not_show[0] |
| L1 “the rest theorem needs only whatever arises to be embodied, but needs a census of what is …” | premise | hypotheses[1] (duplicate; label P58 there) |
| L2 “rests_unrefuted_around, rests_unrefuted_enclosed and arising_opens need every relatum embo…” | premise | hypotheses[1] (duplicate) |
| L3 “in a world that comes to rest not unboundedly many relata ever stand or act (rest_few), a …” | scope | does_not_show[1] (witness Listed.lpo_of_few) |
| L4 “openness with the eight premises does not suffice (holding), nor does every premise bindin…” | non-implication | does_not_show[2] (witness World.holding_world) |
| L5 “in exposed three premises hold vacuously, a feature of representing dissipation as binding…” | correspondence | does_not_show[3] |
| L6 “stated for discrete steps and natural-number amounts;” | scope | standard_boundaries: discrete-steps; does_not_show[4] (natural-number amounts) |
| L7 “evaluates neither openness nor rest;” | evaluation | standard_boundaries: no-evaluation; correspondence R16 (duplicate, “neither openness nor rest”) |
| L8 “names are Ren's to choose.” | names | correspondence R15 and next_delta (“names (Ren)”), duplicates |
| L9 “The premises are one way of supplying the local condition: the exact form for every world …” | law | law 24 |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 85 theorems of Be…” | evidence | validation_scope (modules); counts and the round labels of each addition stay in the receipt, history and the snapshot |
| V1–V2 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence | validation_scope (receipt, periphery); counts in the receipt and the snapshot |
| V3 “The author's counterreview is in §33 and §35 of the integration note;” | evidence | validation_scope (§33, §35) |
| V4–V5 “the tenth independent review (BECOMING-P23C-P24-P25-REVIEW.md) reviewed the P25 part and a…” | evidence (review) | validation_scope (tenth review; “the P26 part” → “the rest-theorem part”); review file under sources, §38 in the snapshot |
| V6 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause) |
| V7–V8 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and…” | evidence (review) | validation_scope (eleventh review); §42 in the snapshot |
| V9 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Locality); count 44 and label P48 → receipt + snapshot |
| V10 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record’s local laws”); labels P57–P61 → snapshot |
| R0–R16 “Section 30's rests brings a world to rest through finiteness;” | correspondence | correspondence (R0, R4, R9, R14: section and round labels replaced by the records they name; otherwise unchanged) |
| N0–N3 “The exact restatement for every world is this record's Flow.change_not_recurring_from, exc…” | local restatement appended to next | law 23; label P57 → history |
| N4 “the exact restatement for every world is laws-of-one-step (P48), of which this record's st…” | local restatement appended to next | law 24; label P48 → history |
| N5–N7 “total standing with rates or continuous amounts;” | next step | next_delta |
| H0, H2 “The standing law (stills): balance; dissipation; a census of what stands (the conditions s…” | premise | hypotheses (unchanged) |
| H1 “Read of worlds. Arising stopping unrefuted (arising_stops_unrefuted): a census of what sta…” | premise | hypotheses[1]–[3] (split at its sentences, wording unchanged) |
| X0–X6 “exposed: meets all eight premises, no step enclosed, and arising never ceases; so the cond…” | counterexamples | counterexamples (unchanged) |
