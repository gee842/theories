# Migration map: census-balance-under-continuation

Old record sha256 `0161ea12b835d5d372d89320c4091008855d7149a9786e245b23b058d7901e00`; snapshot `_process/architecture/history/0161ea12b835d5d3/census-balance-under-continuation.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `Web.Continues`, `ArisesFrom`, `Continued`, `CeasesFrom`, `NoSplit` and `NoMerge` (definitions), `self_one_to_one`, `ceasesFrom_self`, `arisesFrom_self`, `Census.balanceFrom` (census; decided activity, continuation and `R`; each half under its own premise) and `balanceFrom_eq`, `mark_le_total`, `total_le_mark`, `total_swap`, `le_over_stretch`, `ge_over_stretch`, `gaining_of_losing`, `losing_of_gaining` (bounded from `T` by `B`), `Census.arisingFrom_of_ceasingFrom` and `Census.ceasingFrom_of_arisingFrom` (at most `B` from `T` on), `Tandem.kept`, `Tandem.budding`, `Tandem.joining`, the local forms `Census.balanceFrom_at`, `balanceFrom_eq_at`, `arisingFrom_of_ceasingFrom_from`, `ceasingFrom_of_arisingFrom_from`, and the covering forms `not_not_arisingFrom_covered`, `arisingFrom_not_stopping_covered` and `ceasingFrom_not_stopping_covered` (no census and no decision). Three laws were aligned with the Lean statement and none widened:

- Law 8, `Tandem.budding`, states `¬ web.UnceasingFrom buds`, so the law says arising does not recur. The old claim said “nothing ever arises”, which the proof establishes (`still`) but the theorem does not state. The unchanged counterexample keeps the old words.
- Law 4, the proof route, says “the formations after the step that continue one before it”, as the Lean docstring of `Census.balanceFrom` reads. The old text said “that are continued”.
- Law 10 writes out “and no splits from some step on” for `arisingFrom_not_stopping_covered`, a hypothesis that the old next step carried only by context.

The Chinese of laws 10 and 11 uses the family's 止息 for `CeasesFrom`, where the old next step had 不再存在.

| Old text | Type | New place |
|---|---|---|
| T0 “The census balance under a continuation” | title | title (unchanged) |
| S0 “Under a continuation the census balance holds in two halves: …; with neither the balance is exact.” | statement | statement (unchanged) |
| C0 “The census laws (ceasing-needs-arising, bounded-census-keeps-pace, census-balance) read arising and ceasing under the identity the names stipulate: each formation continues only itself.” | law | law 2 (second sentence) |
| C1 “Under any continuation R, … (ArisesFrom), and g ceases … (Web.CeasesFrom);” | law | law 1 |
| C2 “a split is one formation continuing as two (NoSplit excludes it), a merge two continuing as one (Web.NoMerge excludes it).” | law | law 2 (first sentence) |
| C3 “Under a census, with activity and the continuation decided, across each step: … (Web.Census.balanceFrom, balanceFrom_eq).” | law | law 3 |
| C4 “The proof goes through the continuing pairs: … (mark_le_total, total_le_mark, total_swap).” | law (proof route) | law 4 (“that are continued” → “that continue one before it”, as in Lean) |
| C5 “Each formation continuing only itself splits none and merges none (Web.self_one_to_one), and ceasing and arising under it are ceasing and arising (Web.ceasesFrom_self, arisesFrom_self).” | law | law 2 |
| C6 “The inequalities across each step add up over any stretch (le_over_stretch, ge_over_stretch): … (gaining_of_losing, losing_of_gaining).” | law | law 5 |
| C7 “So without splits, … (Web.Census.arisingFrom_of_ceasingFrom); without merges, with at most B formations active from some step on, … (Web.Census.ceasingFrom_of_arisingFrom).” | law | law 6 |
| C8 “Each condition is needed: in Tandem formations t and t + 1 are active at step t; read with each continuing only itself, one arises and one ceases across every step (Tandem.kept);” | law | law 7 |
| C9 “read as budding, … the census holds without merges, one ceases across every step and nothing ever arises (Tandem.budding);” | law + counterexample | law 8 (“nothing ever arises” → “arising does not recur”, the Lean statement); counterexamples[0] (unchanged) |
| C10 “read as joining, … one arises across every step and nothing ever ceases (Tandem.joining).” | law + counterexample | law 8; counterexamples[0] (unchanged) |
| C11 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and activity finite at each step;” | standard boundary + premise | standard_boundaries: discrete-steps; hypotheses[1] (a census lists the active formations at each step) |
| L1 “needs decided activity and continuation (hypotheses of the theorems);” | logical commitment | standard_boundaries: decidability; hypotheses[1] (unchanged) |
| L2 “the continuation is given by a reading, and which one is identity is not said;” | premise | hypotheses[0] (unchanged) |
| L3 “the balance is a count, not a mechanism, and says not which formation arises or ceases;” | non-implication | does_not_show[0] |
| L4 “over a run, no split and no merge are only sufficient;” | converse | does_not_show[1]; next_delta (conditions on continuations over a run) |
| L5 “formation classes, tenure and undermining under a continuation are not stated;” | scope | does_not_show[2]; next_delta |
| L6 “evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| L7 “the names (CeasesFrom, NoMerge, Tandem) are the AI's wording, for Ren to choose.” | names | standard_boundaries: names-provisional; next_delta (names, Ren); the list of names → snapshot |
| V0–V1 “14 October 2026: the current bytes of Becoming.Identity are bound to consolidated receipt 20261013T204910.042715Z (passed: …). Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence | validation_scope (receipt; former names “tabulated in the unification plan”); counts → receipt + snapshot; date and section number → history (migration note) |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of Becoming.Population (…) and the 119 theorems of Becoming.Identity (…) all have empty axiom reports;” | evidence | validation_scope (modules and receipt); counts and lists → receipt + snapshot |
| V3 “the same receipt covers the package's 75 modules …; periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); counts → receipt + snapshot |
| V4–V5 “The author's counterreview is in §43 of the integration note; no independent review yet.” | evidence | validation_scope; §43 → history (migration note) |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V7–V9 “This record's local laws (P50) … (P57–P61) … (P63, P61b) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“this record's local laws included”); labels → history (migration note) |
| R0 “identity-across-steps shows that readings following a formation … depend on who continues whom, while the count (more) does not.” | correspondence | correspondence (unchanged) |
| R1 “This result says how the census laws hold as who continues whom changes: …” | correspondence | correspondence (unchanged) |
| R2 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R3 “This is a count of activity; whether it is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘…’, …);” | reading + Ren's words | correspondence (unchanged; Ren's words verbatim and attributed) |
| R4 “it evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| R5 “budding and merging have biological cases (fission, fusion), which are applications, not the content of the theorems.” | correspondence | correspondence (unchanged) |
| N0 “The converse from one covering list too (P61b): … (Web.ceasingFrom_not_stopping_covered); no census, no decision.” | law | law 11; label P61b → history (migration note) |
| N1 “The exact existential forms of both directions still need listings after each step;” | next step | next_delta (opening clause) |
| N2 “under a continuation from one covering list (P61): … (Web.not_not_arisingFrom_covered); with covering lists at arbitrarily late steps, arising does not stop (Web.arisingFrom_not_stopping_covered); no census, no decision.” | law | law 10 (the no-split hypothesis written out); label P61 → history (migration note) |
| N3 “The converse (arising recurring needs ceasing recurring) from covering lists with a bound, and the decision needed for the exact existential form, remain open;” | next step | next_delta |
| N4–N6 “the exact restatement for every world is this record's Web.Census.balanceFrom_at, balanceFrom_eq_at, arisingFrom_of_ceasingFrom_from, ceasingFrom_of_arisingFrom_from (P50), …; … are their corollaries;” | law | law 9; label P50 → history (migration note) |
| N7 “formation classes, tenure and undermining read under a continuation;” | next step | next_delta |
| N8 “conditions on continuations over a run (the step characterization is in identity-across-steps);” | next step | next_delta (“one step: identity-across-steps”) |
| N9–N10 “a version with rates; names (Ren).” | next step | next_delta (unchanged) |
| H0 “The continuation is a reading: …” | premise | hypotheses[0] (unchanged) |
| H1 “A census: the formations active at each step are listed, each once. Decided activity, …” | premise | hypotheses[1] (unchanged) |
| H2 “The bounded half also needs at most B formations active from some step on.” | premise | hypotheses[2] (unchanged) |
| X0 “Tandem.budding: …; Tandem.joining: …” | counterexample | counterexamples[0] (unchanged) |

N3 is kept as the old record had it. Law 11 (one list covering every step from some step on, nothing merging) gives the converse where one fixed list covers. Covering lists of bounded length at each step, which N3 leaves open, are a wider case. The migration does not decide whether N3 was written before law 11 and is partly stale.
