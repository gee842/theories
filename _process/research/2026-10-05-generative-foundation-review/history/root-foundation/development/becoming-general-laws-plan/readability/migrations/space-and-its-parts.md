# Migration map: space-and-its-parts

Old record sha256 `3044c9aa0be7d800e677dfe701d7e81fbe6056701a274784a7112e31fc2b648f`; snapshot `_process/architecture/history/3044c9aa0be7d800/space-and-its-parts.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T1 “The whole and its parts: the laws with no premise hold of every world and premises carve p…” | title (statement of the result) | title (short name) + statement |
| C0–C2 “A world is its relata, read with one kind, with the flow among them and their web (World);” | definition + law | law 1 |
| C3 “The laws of Becoming.Change and the arithmetic identity of Becoming.Evolution (the countin…” | law | law 2 (module names kept in text; no declarations) |
| C4 “Read of parts: arising recurring (some relatum arising at arbitrarily late steps, ArisingR…” | law | law 3 |
| C5 “Decidedness is this law's own condition, not a commitment of the representation: asked of …” | law | law 4 |
| C6 “With infinitely many relata either can recur without the other (World.separate, from Accre…” | law | law 5 |
| C7 “Activity needing support, balance, only active relata giving, only active relata taking an…” | law | law 6 |
| C8 “Among finite worlds, arising recurring or not occurs both with every event living, not und…” | law + witnesses | law 7 (law) and law 8 (witnesses) |
| C9 “So neither arising nor ceasing decides whether events are living.” | law | law 7 (last clause) |
| C10 “grazing's verdict lies outside the verdict about drawing on a self-bearing relatum at its …” | law | law 9 (grazing) and law 10 (inactive_below, ceases_below, seedbank) |
| C11 “whether undermining that co-occurs with the relatum depending not being active after the s…” | scope (Ren’s choice) | does_not_show[4] |
| C12 “The same activity while each side draws on its own standing (selfDrawing) also has an even…” | law | law 11 |
| C13 “In a finite, balanced, dissipative world in which whatever arises is embodied, that the wo…” | law + witness | law 12 (rest) and law 13 (each premise needed, throughput) |
| C14–C15 “two sides handing a standing keep arising without dissipation (shuttle);” | witnesses | law 13 |
| C16 “and a relatum whose activity is not its standing keeps arising without embodiment (flicker…” | witness | law 14 |
| C17 “Which parts of the space Ren's ‘generative’ and ‘degenerative’ name is Ren's to choose: th…” | correspondence + law | does_not_show[3] (Ren’s choice); law 15 (reading of activity); Ren’s confirmation of the names → correspondence (appended sentence; the source id carries a date) |
| C18 “read as relations, renewing and consuming formations do not overlap (Web.renewing_not_cons…” | law | law 15 |
| C19 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| C20 “P58: rest needs no decision procedure.” | law (lead) | law 16 (“Rest needs no decision procedure”); round label P58 → history |
| C21 “For an amount that does not rise from some step on, that its falls stop from some step on …” | law | law 16 |
| C22 “In a family balanced and dissipated on from some step on, that the arising of the embodied…” | law | law 17 |
| C23–C24 “With a list covering what is active from some step on, ceasing recurring leaves a later ar…” | law | law 18 (“from Covers.not_not_coming_from of laws-of-one-step” → “through the covering law of laws-of-one-step”, its declaration); round labels P58, P58c and the renaming → history |
| L0 “Contains no ethical predicate and evaluates no part;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “does not prove that the theory of becoming needs no axiom;” | non-implication | does_not_show[0] (with R11’s clause) |
| L2 “Living is only the structural condition of the stepwise reading, not G0's valuation itself…” | correspondence | does_not_show[1] |
| L3 “the law for finite worlds needs decidable activity, and asked of every finite world withou…” | premise (decidability) | hypotheses[0] (duplicate); law 4; standard_boundaries: decidability |
| L4 “stated for the reading across discrete steps;” | standard boundary | standard_boundaries: discrete-steps |
| L5 “the parts listed are not exhaustive: combinations of premises and further parts, such as m…” | scope | does_not_show[2] |
| L6 “which parts Ren's ‘generative’ and ‘degenerative’ name is Ren's to choose, and this result…” | correspondence | does_not_show[3] |
| L7 “names are Ren's.” | names | next_delta (“names (Ren)”, duplicate of N8) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 65 theorems of Be…” | evidence | validation_scope; counts (65, 145) and the round labels of the additions stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3 “The author's counterreview is in §30 of the integration note;” | evidence | validation_scope (§30) |
| V4 “the ninth independent review (BECOMING-P18B-P23-REVIEW.md) accepts its mathematics, and it…” | evidence (review) | validation_scope (ninth review accepts); review file and §34 stay under sources and in the snapshot |
| V5–V6 “the tenth independent review (BECOMING-P23C-P24-P25-REVIEW.md) accepts the mathematics of …” | evidence (review) | validation_scope (tenth review accepts the mathematics it reviewed; its corrections not yet independently reviewed, kept as written); §38 and the work-item label stay in the snapshot |
| V7 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); injEq/propext detail stays in the receipt and the snapshot |
| V8–V9 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and…” | evidence (review) | validation_scope (eleventh review accepts; its corrections not yet independently reviewed); §42 stays in the snapshot |
| V10–V11 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record’s local laws”); round labels P50, P57–P61 → history + snapshot |
| R0–R13 “Ren's words (2026-10-08-theory-of-becoming-priority): ‘when we add axiom, we can define wh…” | correspondence | correspondence (unchanged; one sentence appended from C17) |
| N0–N2 “The exact restatement for every world is this record's World.arising_iff_ceasing_covering,…” | local restatement appended to next | law 19; round label P60 → history |
| N3–N4 “the exact restatement for every world is this record's Web.inactive_below_at, Web.ceases_b…” | local restatement appended to next | law 20; round label P50 → history |
| N5–N8 “the reading of the proposal's ‘generative, degenerative’ (Ren);” | next step | next_delta |
| H0–H3 “The law (arising_iff_ceasing): the world is finite, a list naming every relatum once; whet…” | premise | hypotheses (unchanged) |
| X0–X1 “With infinitely many relata arising and ceasing separate (Accretion, Attrition); without a…” | counterexamples | counterexamples (unchanged) |
