# Migration map: rising-and-falling-in-one-exchange

Old record sha256 `0c62b41ed9709556aabbad575ffae31394d136f233fa7ffe1b8dc04a721fd927`; snapshot `_process/architecture/history/0c62b41ed9709556/rising-and-falling-in-one-exchange.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `Flow.Balances.fall_taken` (`0 < L.taken t c` where `c` falls), `Flow.Balances.takenBy` (some present active formation takes from and draws on the falling condition, given `Taking`), `Flow.Balances.falls_cover` (`risen + takers ≤ fallen` across a step dissipated on), `Balances.falls_of_taking`, `Balances.depletes` (yields `Web.Depletes`), `rise_with_fall` and `standing_with_fall` (another member `d ≠ c` falls), `rise_alone_opens` (`¬ ClosedAt`, family without repetition, under `Dissipative`), `rise_exchange` (an active formation gives to the rising member and takes from the family; another member falls, taken from by an active formation drawing on it), `Web.Embodied.arising_with_fall`, `Brood.rise_without_fall` (closed, arises, no generation ever falls, not dissipated on), and the local forms `BalancesOn.falls_cover`, `BalancesOn.falls_of_taking`, `depletes_at`, `BalancesOn.rise_with_fall`, `BalancesOn.rise_exchange` (activity of givers and takers at the step only), `Web.Embodied.arising_with_fall_at`. None is wider than the old text. In law 5 the English “the formation giving to the rising member is active” became “an active formation gives to the rising member”, as `rise_exchange` states it. That is an existential, and the old Chinese already read so (给予上升成员的是一个活跃形成).

| Old text | Type | New place |
|---|---|---|
| T0 “Rising and falling in one exchange” | title | title (unchanged) |
| S0 “Across a step at which a family is dissipated on, a member rising comes with another member of the family falling.” | statement | statement (unchanged) |
| C0 “In a balanced flow every fall is taken from (Flow.Balances.fall_taken);” | law | law 1 |
| C1 “where only active formations take, … (Flow.Balances.takenBy).” | law | law 1 |
| C2 “These are the duals of rise_given and renewedBy.” | law (remark) | law 1 |
| C3 “In a balanced flow, across a step dissipated on, … (Flow.Balances.falls_cover).” | law | law 2 |
| C4 “So a formation taking from the family makes some member fall, whether or not another rises (Flow.Balances.falls_of_taking);” | law | law 3 |
| C5 “an event at each of whose steps the family is dissipated on and taken from depletes it, … (Flow.Balances.depletes);” | law | law 3 |
| C6 “a member rising, as in coming to stand, comes with another member falling across the same step (Flow.rise_with_fall, Flow.standing_with_fall);” | law | law 4 |
| C7 “and under dissipation, a family without repetition in which a member rises while none falls is open across that step (Flow.rise_alone_opens).” | law | law 4 |
| C8 “Where only active formations give and take, … (Flow.rise_exchange).” | law | law 5 (“the formation giving … is active” → “an active formation gives”, as in Lean) |
| C9 “Read with one kind of relatum, … (Web.Embodied.arising_with_fall).” | law | law 6 |
| C10 “Without dissipation it need not: … (Brood.rise_without_fall).” | law + counterexample | law 7; counterexamples[0] (unchanged) |
| C11 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “a fall is not a ceasing, and the member that falls may still stand;” | non-implication | does_not_show[0] |
| L2 “says that some member falls, not which;” | scope | does_not_show[2] |
| L3 “‘one exchange’ means giving and taking in one flow across one step and does not attribute a particular fall to a particular rise;” | scope | does_not_show[2] |
| L4 “stated for the reading across discrete steps with natural-number amounts;” | standard boundary + premise | standard_boundaries: discrete-steps; hypotheses[0] (natural numbers, unchanged) |
| L5 “balance, dissipation and only active formations taking are correspondence premises;” | correspondence | does_not_show[3]; hypotheses[0]–[2] (unchanged) |
| L6 “neither rising nor falling is evaluated;” | standard boundary | standard_boundaries: no-evaluation |
| L7 “names are Ren's.” | names | standard_boundaries: names-provisional; next_delta (names, Ren) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 2 new theorems of Becoming.Flow, 7 of Becoming.Dissipation and 3 of Becoming.Roles all have empty axiom reports;” | evidence | validation_scope (modules and receipt); counts → history (migration note) + snapshot |
| V1 “the same receipt covers the package's 75 modules …” | evidence | receipt + snapshot |
| V2 “The author's counterreview is in §28 of the integration note;” | evidence | validation_scope; §28 → history (migration note) |
| V3 “the ninth independent review (BECOMING-P18B-P23-REVIEW.md) accepts its mathematics, and its corrections are handled in §34 …” | evidence | validation_scope; review file stays in references; §34 → history (migration note) |
| V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V5 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record's local laws”); label → history (migration note) |
| R0 “Plan P20 was first titled ‘coming to be and ceasing to be in one exchange’.” | process history | history (migration note) |
| R1 “What is proved is rising and falling: a fall is not a ceasing, and the member that falls may still stand;” | non-implication | does_not_show[0] (with L1) |
| R2 “the title and the plan's row are corrected accordingly.” | process history | history (migration note) |
| R3 “Ren's proposal asks to explain formation, … (2026-10-08-theory-of-becoming-priority).” | correspondence | correspondence (unchanged) |
| R4 “coming-and-ceasing-keep-pace proves, with no premise, …; this result proves …” | correspondence | correspondence (unchanged) |
| R5 “The author reads this as one formal content of that scope within a single step (an AI argument): …” | reading | correspondence (unchanged) |
| R6 “This does not show that one arising is bought with another's loss: a fall is not undermining, … fuel that no formation depends on;” | non-implication | does_not_show[1] (“is bought with” → “comes through”: a market word; zh 换来 unchanged) |
| R7 “neither rising nor falling is evaluated.” | standard boundary | standard_boundaries: no-evaluation |
| R8 “Read through flows, the two correspondence premises of Becoming.Generation (RenewedBy, Depletes) reduce to …; whether actual unfoldings meet them is an empirical question.” | correspondence | correspondence (unchanged) |
| R9 “‘Rising’, ‘falling’ and ‘one exchange’ are the AI's terms, and names are Ren's.” | names | correspondence (unchanged); standard_boundaries: names-provisional |
| N0–N1 “The exact restatement for every world is this record's Flow.BalancesOn.falls_cover, … (P57), the local condition inside the law: …; … are their corollaries;” | law | law 8; label P57 → history (migration note) |
| N2 “a one-step form for when a fall is a ceasing to stand (the level reaching zero);” | next step | next_delta (unchanged) |
| N3–N6 “a version with rational amounts; whether arising that is not embodied has its own form of the one exchange; the empirical correspondence …; names (Ren).” | next step | next_delta (unchanged) |
| H0 “Balance (Balances): …” | premise | hypotheses[0] (unchanged) |
| H1 “The family is dissipated on across the step (DissipatesOn): …” | premise | hypotheses[1] (unchanged) |
| H2 “Read of formations, also: …” | premise | hypotheses[2] (unchanged) |
| X0 “Without dissipation: generation t+1 arises … (Brood.rise_without_fall).” | counterexample | counterexamples[0] (unchanged) |
| X1 “Without dissipation: a condition rises and is given to at every step and never falls (Growing).” | counterexample | counterexamples[1] (unchanged) |
