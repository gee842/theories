# Migration map: map-of-premises

Old record sha256 `2ab3f527b5e911d01f6b16323bd1143871561e7e2a9695096c0b628b95d9559a`; snapshot `_process/architecture/history/2ab3f527b5e911d0/map-of-premises.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T1 “The map of premises: which premises follow from which, the remaining eight independent rel…” | title (statement of the result) | title (short name) + statement |
| C0 “A census (Counted: the relata active at each step are listed, each once, so finitely many …” | definition | law 1 |
| C1 “What follows: activity needing support makes activity carried, by the zero reserve (Depend…” | law | law 2 |
| C2 “every relatum embodied makes whatever arises embodied (Embodied.arising);” | law | law 3 |
| C3 “a finite world whose activity is decided has a census (Finite.counted);” | law | law 4 |
| C4 “and where only active relata take, and only from what they draw on, and the flow dissipate…” | law | laws 5 (the local law and its reason) and 6 (the enclosed and finite corollaries) |
| C5 “The remaining eight premises, activity needing support, balance, only active relata giving…” | law | law 7 |
| C6 “The worlds are a relatum whose standing does not support its activity (strained), the side…” | witnesses | laws 8 and 9 (four witnesses each) |
| C7–C9 “So no premise follows from the others (none_follows).” | law + witness | law 10 |
| C10 “Mutualists active throughout meet all eight (mutualism_premised), and in a finite world wh…” | law | law 11 |
| C11 “A premise binds where something meets its condition (Premise.Binds; every premise binding …” | definition | laws 12 (binding), 13 and 14 (the condition of each premise) |
| C12–C13 “In hatch all eight hold and each binds (hatch_binds): a parent takes two units of food and…” | witness | law 15 |
| C14–C16 “The world is not finite, though only the food, the parent and the child are ever active (h…” | law | law 16 |
| C17 “So a census binds only in that the world is not finite: in every world that comes to rest …” | law | law 17 (World.rest_few is not among this record's references; the name stays in the law text with its record) |
| C18–C19 “No finite world binds every premise (World.Finite.not_binds);” | law | law 18 (World.finiteHatch_premised, already in references, binds “meeting the eight”) |
| C20–C21 “Activity needing support binds without being tight, the food never falling below the need,…” | law | law 19 (World.hatch_rests_unrefuted is not among this record's references; the name stays in the law text) |
| C22 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0–L1 “Maps only the eight premises stated of worlds;” | scope | does_not_show[0]; next_delta |
| L2 “independence is relative to these eight and does not exclude new implications once further…” | non-implication | does_not_show[1] |
| L3 “the implications for finite worlds need decidable activity;” | premise (decidability) | hypotheses[0] (duplicate); standard_boundaries: decidability |
| L4 “stated for the reading across discrete steps;” | standard boundary | standard_boundaries: discrete-steps |
| L5 “binding says only that some condition is met, and for a census only that the world is not …” | non-implication | does_not_show[2] |
| L6 “evaluates no part;” | standard boundary | standard_boundaries: no-evaluation (judgment: “evaluates no part” read as containing no ethical predicate and evaluating nothing) |
| L7 “the names of premises and worlds are Ren's to choose.” | standard boundary | standard_boundaries: names-provisional; correspondence R15 keeps “the AI's formulations, and Ren's to choose” |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 61 theorems of Be…” | evidence | validation_scope; the count (61) and the round labels (P25b, P29, P29b) stay in the receipt, the history and the snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3 “The author's counterreview is in §32 of the integration note;” | evidence | snapshot (author counterreview in §32 of the integration note; the paragraph cites the reviews instead) |
| V4–V5 “the tenth independent review (BECOMING-P23C-P24-P25-REVIEW.md) accepts its mathematics, an…” | evidence (review) | validation_scope (“two independent reviews … accept its mathematics; their corrections … not yet independently reviewed”); the review files stay under sources, §38 in the snapshot |
| V6 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V7–V8 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and…” | evidence (review) | validation_scope (as V4–V5); §42 in the snapshot |
| V9–V10 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | round labels | history (P57–P61, P63, P61b entries) + snapshot |
| R0–R15 “The plan's third part of completeness asks that each dynamical premise carve a proper part…” | correspondence | correspondence (unchanged) |
| N0–N1 “The exact restatement for every world is this record's Web.carries_zero_across (P63), the …” | local restatement appended to next | law 2 (Web.carries_zero_across and its corollary Web.carries_zero); round label P63 → history |
| N2–N3 “the exact restatement for every world is this record's World.acting_across_on, keep_lists …” | local restatement appended to next | laws 4 (keep_lists) and 5 (acting_across_on); round label P60 → history |
| N4 “World.acting_across (and through it acting_of_enclosed, Finite.acting), World.Finite.count…” | corollaries | laws 4 (Finite.counted) and 6 (acting_across, acting_of_enclosed, Finite.acting) |
| N5–N6 “a map of the premises stated relative to a further reading (a continuation relation, a ren…” | next step | next_delta |
| N7–N9 “Rest under censuses and enclosure is answered by P25 and P26 (continued-change-needs-openn…” | answered items with round labels | laws 11, 15–17 (their content); history (P25, P26, P29, P29b) + snapshot |
| H0 “What follows: Finite.counted needs whether each relatum is active at each step to be decid…” | premise | hypotheses[0] (“, P58” → history) |
| H1 “Independence and meeting all of them are statements about particular worlds, with no premi…” | premise | hypotheses[1] (unchanged) |
| X0–X1 “Eight independence witnesses, strained, unbalanced, scatter, morsel, lossless, latent, mul…” | counterexamples | counterexamples (unchanged) |
