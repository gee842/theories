# Migration map: entropy-history-and-record

Old record sha256 `5c9bdd32fa588faee2e84e71776e789563198ea3273e8d87e60a02dea4f06c10`; snapshot `_process/architecture/history/5c9bdd32fa588fae/entropy-history-and-record.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T2 “Entropy, history and record: lossless exchange can continue and return;” | title (statement of the result) | title (short name) + statement |
| C0 “History-count monotonicity uses no balance premise;” | premise scope | law 1 (“uses no balance premise”); hypotheses[0] |
| C1 “the following change and reversal results use balance: in a balanced flow every change of …” | premise scope + law | hypotheses[0] (balance used); law 2 |
| C2 “the history of the family's exchanges since T (Flow.history) never shrinks (Flow.history_m…” | law | law 1 |
| C3 “an exchange with its reverse (Flow.Reverses: the same formations, each taking what it gave…” | law | law 3 |
| C4 “Zero: the first law at a fixed unit is nothing from nothing (Flow.Gainless), losing nothin…” | law | law 4 |
| C5 “under the first law a reverse is within the law exactly where the exchange is lossless (Fl…” | law | law 5 |
| C6 “Passing is finite, balanced, lossless and enclosed at every step, each exchange reversed a…” | law | law 6 |
| C7 “The record: with the record of the exchanges counted as a condition given to and never tak…” | law | laws 7 (record counted, balance kept) and 8 (dissipation exactly as conservation with a record) |
| C8–C9 “both parts are needed (Passing.record_needs_both);” | law | law 9 |
| C10 “The amount dissipated (Flow.dissipated) never falls, with the stock it is conserved under …” | law | law 10 (Flow.dissipated_mono, already in references, binds “never falls”) |
| C11 “Configurations: under the first law the family's configuration stays among its stock's con…” | law | law 11 (Web.config_within, already in references, binds the first clause) |
| C12 “never revisiting (Web.Revisits), it changes at most that many times and rests (Flow.Balanc…” | law | law 12 |
| C13 “The arrow: a quantity of the configuration that never falls and rises at every change (Web…” | law | law 13 |
| C14 “Merging: where change is a function of the configuration (Web.Determined), rest after a ch…” | law | law 14 |
| C15–C16 “merging none, change never stops (Web.changes_persist) and under the first law revisits (F…” | law | law 15 |
| C17 “Holding the history: where the configuration carries the history (Flow.CarriesHistory), it…” | law | law 16 |
| C18 “Gathering: under exact conservation, every step enclosed, a record's level rises without e…” | law | law 17 |
| C19 “Instances of the laws of change (R6, Becoming.Recurrence): revisiting after a change is re…” | law | law 18 (“(R6, Becoming.Recurrence)” → “the laws of change”; the plan label stays in history) |
| C20 “the first law keeps the configurations among those within the stock at T (Flow.Balances.he…” | law | laws 19 and 20 (“Law.succ_open” → “the successor law”, a declaration of law 20) |
| L0 “Discrete steps, natural-number amounts at a fixed unit;” | representation | standard_boundaries: discrete-steps; hypotheses[1] (natural-number amounts at a fixed unit) |
| L1 “whether ‘entropy’ names the history or the record in the conserved amount is Ren's decisio…” | scope (reading) | does_not_show[0]; next_delta |
| L2 “the least loss is decomposed, not derived;” | non-implication | does_not_show[1] |
| L3 “determined change is a hypothesis of the merging theorems, and the conclusions of merges_o…” | premise + scope | hypotheses[2] (determined change a hypothesis); does_not_show[2] (double negations) |
| L4 “only the dichotomy of merging or not is stated;” | scope | does_not_show[2] |
| L5 “that the reachable configurations shrink step by step is R6's (Law.Reachable.earlier, Law.…” | scope | does_not_show[3] (witness Law.lost_stays; “R6's” → “holds for any determined law”) |
| L6 “a coarse-grained entropy rising from an ordered start needs a premise about the start and …” | scope | does_not_show[4] |
| L7 “the flow with the record counted has Option conditions and is not a world of one kind of r…” | scope | does_not_show[5] |
| L8 “the correspondences to thermodynamics are readings, not physical derivations;” | correspondence | does_not_show[6] |
| L9 “no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation (and no-ethical-premise: no ethical premise, empty axiom reports) |
| L10 “not yet independently reviewed.” | evidence | validation_scope (“no independent review”) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 185 theorems of B…” | evidence | validation_scope; the count (185) and the named theorems stay in the receipt and the snapshot |
| V1 “The same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V4–V5 “The author's counterreview is in §110 of the integration note;” | evidence | validation_scope |
| R0–R16 “Answers to Ren's three questions (the AI's reading, pending Ren).” | correspondence | correspondence (unchanged) |
| N0 “Ren's decision on the reading of ‘entropy’ (the history or the record in the conserved amo…” | next step | next_delta |
| N1 “the count of reachable configurations within the first law's list (their shrinking is R6's…” | next step | next_delta; “(their shrinking is R6's Law.lost_stays)” → does_not_show[3] |
| N2–N5 “the record as a relatum in the census, so the counted flow is itself a world;” | next step | next_delta |
| H0–H2 “Flow.history_mono itself uses no balance premise; connecting a level change to an exchange…” | premise | hypotheses[0]–[2] (unchanged) |
| H3 “Counting the record as a condition is a reading, following Ren on 11 October 2026: ‘I know…” | premise (reading, Ren's words) | hypotheses[3] (reading and Ren's words, verbatim) and hypotheses[4] (the author's reading; theorems hold under either) |
| X0–X3 “Passing: finite, balanced, lossless and enclosed, each exchange reversed at the next step,…” | counterexamples | counterexamples (unchanged) |
