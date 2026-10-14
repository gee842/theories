# Migration map: living-on-and-descent

Old record sha256 `70824073777211730fa6baf8d74ff90f0cd63c7e97c6c25f0b1776718c6d2221`; snapshot `_process/architecture/history/7082407377721173/living-on-and-descent.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Descent.lean` (and `Evolution.lean` for `Flow.DescendsAt`), bytes bound by the record's references. `LivesOn.stands` and `LivesOn.active` take an active formation and `Dependent`, the latter also the relatum embodied, as law 2 and hypothesis 4 say; `living_on_reaches` relates an event to every living event of the relatum lived on, since `LivesOn` reads only the relatum of the second event; `Embodied.descends` gives another formation active at the step of arising. No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Living on and descent relate relata directly: two readings of related that the one-kind reading supplies” | title (statement of the result) | title “Living on and descent” (short name) + statement |
| C0 “On the stepwise reading of a web, keep living (active and not undermining) and add to interaction two relations that only a reading with one kind of relatum has.” | framing | statement (“each added to interaction on the stepwise reading of a web, with living (active and not undermining) kept”) |
| C1 “Living on: a formation draws at a step on a relatum and depends on it at a positive need there (LivesOn), and such an event is related to that relatum's events (sustenance).” | definition | law 1 (Web.Bearing, the positive-need dependence, among the declarations) |
| C2 “Like interaction it is not free: it needs an actual drawing and a dependence that can fail;” | law (framing) | law 2 (“it is not free: it needs” → “living on needs”; zh 不是免费的 is a market word, and the clause after the colon says what it meant) |
| C3 “under Dependent the relatum an active formation lives on stands at that step (LivesOn.stands), and where that relatum is embodied it is active there (LivesOn.active).” | law | law 2 |
| C4 “It need be neither: an eater can live on a relatum that stands while dormant, living on connecting them where interaction does not (Drowsy.drowsy).” | counterexample | counterexamples[3] (unchanged; it states exactly this) |
| C5 “It connects a bee and a flower that depend only on each other (Mutualism.apart_sustenance_connected), which neither co-participation nor interaction connects.” | law | law 3 (“It” → “Living on”; Mutualism.apart_not_connected among the declarations) |
| C6 “Under N_rel, valuing an event that lives on a relatum reaches every living event of that relatum, and conversely (living_on_reaches, lived_on_reaches): valuing the fox's eating reaches the hare's living.” | law | law 4 |
| C7 “Descent: a relatum descends from a formation that takes part in a step at which it gives to the relatum and across which the relatum comes to stand (Descends);” | definition | law 5 |
| C8 “a give entry of a formation taking no part enters no level and makes no descent (Unrelated.unrelated, Brood.not_descends);” | law (witness) | law 5; counterexamples[4] (unchanged) |
| C9 “and descent relates every event of the one relatum to every event of the other (descent).” | definition | law 5 |
| C10 “In a balanced flow in which only active formations give, an embodied relatum that arises descends from another formation active at that step (Embodied.descends), which need not be embodied;” | law | law 6 |
| C11 “so under N_rel, valuing any event of that formation reaches every living event of the relatum descending from it, and conversely (descent_reaches, ancestry_reaches, arisen_reached).” | law | law 6 |
| C12 “Generations each given by the one before are connected by descent and by neither co-participation nor interaction, and G0 there is exactly a seed with N_rel and N_std (Brood.descended).” | law (witness) | law 7 (Brood.descends and Valuation.significant_iff among the declarations); counterexamples[0] (unchanged) |
| C13 “Descent follows coming to stand, not arising: a seed descends from the parent that provisioned it while dormant (Provisioned.descends), and waking from dormancy descends from nothing (Sleeper.no_descent).” | law (witness) | law 8; counterexamples[2] (unchanged) |
| C14 “Both readings use which condition is which relatum: relabelling the conditions … removes the connection by living on (Mutualism.relabel_sustenance).” | law (witness) | law 9; counterexamples[1] (unchanged); witness of does_not_show[5] |
| C15 “No ethical premise and no Lean axiom is used.” | premise | hypotheses[1] (“the record uses no ethical premise and no Lean axiom”); not the shared key no-ethical-premise, because N_rel, a normative premise of metaethical-core-characterization, is an antecedent of the reaching laws and the key's citing condition asks for hypotheses without an ethical premise (judgment call, see history) |
| L0 “Contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| L1 “changes neither living nor C, and does not show that arising is good or that new arising ought to be brought about” | non-implication | does_not_show[0] |
| L2 “sustenance and descent are candidate readings of related, and adopting them is Ren's choice” | premise | hypotheses[1] (“candidate” added to its first sentence, which already says Ren's choice) |
| L3 “descent relates every event of two relata and does not order them in time” | scope | does_not_show[1] |
| L4 “the formation that gives need not be embodied (a source giving to a seed is descent too)” | scope | does_not_show[2]; law 6 keeps “which need not be embodied” from C10 |
| L5 “living on does not ask about the effect of drawing, and the relatum lived on need be neither embodied nor active (Drowsy)” | scope + counterexample | does_not_show[3] (first clause); counterexamples[3] (second, Drowsy) |
| L6 “descent counts give entries, not net flow: a formation taking part that gives and takes back as much is still an ancestor, a further choice of reading” | scope | does_not_show[4] (unchanged) |
| L7 “both readings depend on the one-kind identification, which the two-kind readings cannot check” | correspondence | does_not_show[5], witness Mutualism.relabel_sustenance |
| L8 “stated for the stepwise reading only” | scope | does_not_show[1] (the stepwise reading is a reading of the web, not the discrete-steps boundary, so it stays written out) |
| L9 “the witnesses are minimal” | scope | does_not_show[6] |
| L10 “the final choice of names is Ren's” | standard boundary | standard_boundaries: names-provisional |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 41 theorems of Becoming.Descent all have empty axiom reports;” | evidence | validation_scope (the count stays in the receipt and the snapshot) |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §25 of the integration note;” | evidence | validation_scope (“in the integration note”); §25 is in the first history note and the snapshot |
| V3 “the eighth independent review (BECOMING-P16C-P17-P18-REVIEW.md) accepts its mathematics, and its corrections are handled in §27 of the integration note.” | evidence (review) | validation_scope (“listed under sources”, “in the integration note”); §27 stays in the snapshot |
| V4–V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| R0–R1 “Becoming.Metaethics reads related as formed relation and lists conditioning, dependence, descent and cooperation; the earlier readings relate only through a shared condition, … Mutualism.apart is its counterexample: …” | correspondence | correspondence (“and lists” → “:”) |
| R2 “This result gives two direct relations in the one-kind reading: living on corresponds to conditioning and dependence, descent to descent.” | correspondence | correspondence (unchanged) |
| R3 “Living on requires dependence at a positive need, keeping the discipline of interaction (connection is made by living use);” | correspondence | correspondence (“keeping interaction's discipline that connection is made by living use”) |
| R4 “descent requires a positive gift from a formation taking part in the step and coming to stand, so neither empty giving nor the give entry of a formation taking no part makes it.” | correspondence + law | correspondence (first clause); the “so neither …” clause is law 5's (C8) |
| R5 “Neither definition mentions embodiment: what first enters the valuation here is the one-kind identification, not embodiment, which enters only the conclusions of Embodied.descends and arisen_reached.” | premise (scope) | hypotheses[0] (“first … here” → “what enters the valuation is this identification”) |
| R6 “Ren's words are “生生不息 - 一种整体的，不断创造更多生的方向” (a whole direction of unceasingly creating more 生).” | Ren's words | correspondence (verbatim) |
| R7 “Taking embodied relata as 生, a reading that is Ren's (§23, K6, of the integration note), the author reads descent as one formal content …: … (an AI argument);” | reading | correspondence (“a reading that is Ren's (§23, K6, of the integration note)” → “Ren's reading (integration note §23, K6)”) |
| R8 “it does not replace Ren's words, does not show that arising is good, and does not decide whether Ren adopts these relations.” | non-implication | correspondence (first and third clauses); does_not_show[0] (the second) |
| N0 “Whether Ren adopts living on and descent as relations along which N_rel transmits; …; connecting to universal_reason's ‘new living content’.” | next step | next_delta (unchanged) |
| H0 “The one-kind reading: conditions and formations share an index, …” | premise | hypotheses[0] (unchanged, with R5) |
| H1 “sustenance and descent are two readings of related, correspondence premises: …; N_rel itself remains a premise (metaethical-core-characterization).” | premise | hypotheses[1] (with L2's “candidate”, “an antecedent of the reaching laws” and C15) |
| H2 “Embodied.descends and arisen_reached need the flow to balance the web, …” | premise | hypotheses[2] (unchanged) |
| H3 “LivesOn.stands needs Dependent; LivesOn.active also needs the relatum lived on to be embodied.” | premise | hypotheses[3] (unchanged) |
| X0–X4 | counterexamples | counterexamples[0]–[4] (unchanged) |
