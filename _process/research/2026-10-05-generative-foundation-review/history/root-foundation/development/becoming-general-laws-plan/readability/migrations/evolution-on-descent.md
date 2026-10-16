# Migration map: evolution-on-descent

Old record sha256 `fbfbd7a4d4de465fabff850da4b720867a03d7aba3255d04977d00deef325e65`; snapshot `_process/architecture/history/fbfbd7a4d4de465f/evolution-on-descent.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Evolution.lean` (bytes bound by the record's references). Laws 6 and 8 now say “under the same conditions”: `Flow.transmitted_supported` and `Flow.transmitted_within` take `Acting` and `Dependent`, which the old claim left to the context of the preceding selection sentence. Law 5 writes in the descent and dependence conditions of `Flow.selected_le` and `Flow.selection_within`, formerly only in hypothesis 2. No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Evolution on descent” | title | title (unchanged) |
| S0 “Evolution on descent rests on a premise-free arithmetic identity; only supported formations leave descendants, what is transmitted within a bound was selected within it, and activity sets later selection.” | statement | statement (unchanged) |
| C0 “Read with one kind of relatum, a relatum descends from a formation across a step when the formation takes part in the step and gives to it, and it comes to stand across the step (Flow.DescendsAt, Flow.Descends).” | definition | law 1 (“it” → “the relatum”; Web.ComesToStand added to the declarations, already a declared reference) |
| C1 “With no premise: over any finite family of parents … with what transmission raised (price).” | law | law 2 (unchanged wording; price among the declarations) |
| C2 “This is the counting form of Price's equation (Price 1970), an arithmetic identity: it divides the offspring's total into …” | law | law 3 (the citation “Price 1970” moved to the correspondence, where the identity is discussed) |
| C3 “The weighted total is not the selection term proper: where every parent has k offspring it is k times the parents' total (selected_uniform), and with one parent and one unchanged offspring it is the parent's amount (unselected).” | law | law 3 |
| C4 “The selection term proper, the covariance of offspring number and amount, is not stated here.” | scope | does_not_show[0] |
| C5 “Where only active formations give (Acting) and activity needs support (Dependent), a formation that a relatum descends from across a step is supported at that step (Flow.DescendsAt.supported);” | law | law 4 |
| C6 “a formation unsupported at a step leaves no descendant across it (Flow.unsupported_childless), and one never supported leaves none (Flow.never_supported_childless);” | law | law 4 |
| C7 “read of needs on a condition every parent depends on, the parents' needs weighted … (Flow.selected_le), so the offspring's total of any amount … (Flow.selection_within).” | law | law 5 (“under the same conditions”; the descent-across-one-step and dependence conditions of hypothesis 2 written in) |
| C8 “Where the flow transmits a dependence on a condition c within δ (Flow.TransmitsWithin: …; supplied as a premise), what is transmitted was selected within δ: … plus δ (Flow.transmitted_supported);” | law + premise | law 6 (“under the same conditions” written in, see above); “supplied as a premise” → hypotheses[2] |
| C9 “with δ zero the need was met there, and with δ one a descendant's need can exceed its condition's level at the giving step and at every step (Slack.slack).” | law (witness) | law 7 (“there” → “at the giving step”) |
| C10 “In a balanced flow, a descendant's need with everything taken … plus δ (Flow.transmitted_within): what formations take and give between enters what can be transmitted later.” | law | law 8 (“under the same conditions” written in, see above) |
| C11–C13 “Witness: a parent depending on a pool at need two … (Drawdown); the one inheriting its need is unsupported …; transmission, variation, selection and the feedback of activity on selection occur in one unfolding.” | law (witness) | law 9 (Drawdown.drawdown, Drawdown.same_unsupported) |
| C14 “Without Dependent it need not hold: a formation active beyond its support transmits a need above the level at the step it gives (Unchecked).” | counterexample | counterexamples[0] (unchanged; it states exactly this) |
| C15 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipt reports empty axioms for Becoming.Evolution) |
| L0 “Contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| L1 “fitness is not defined, and no need is said to be better” | non-implication | does_not_show[1] |
| L2 “transmission (TransmitsWithin) is a premise here” | premise | hypotheses[2] (it already said so) |
| L3 “P84 proves it independent wherever it binds and derives it from a reading of drawing with drawing being depending (see transmission-independent-where-it-binds)” | premise (scope) | hypotheses[2] (“P84 proves” → “it is independent … and follows from”; P84 stays in the history note of 12 October) |
| L4 “price is an arithmetic identity, stated only in additive counting form with natural-number amounts and without the covariance form” | scope | does_not_show[0] |
| L5 “selection is read only as the constraint of support on giving, without reproductive rates, mutation, drift, movement or population dynamics” | scope | does_not_show[2] (unchanged) |
| L6 “stated for the reading across discrete steps” | standard boundary | standard_boundaries: discrete-steps |
| L7 “no correspondence to the theory of evolution's existing mechanisms is proved” | correspondence | does_not_show[4] (the mechanisms named from R7) |
| L8 “names are Ren's” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “names are Ren's” |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 25 theorems of the new module Becoming.Evolution all have empty axiom reports;” | evidence | validation_scope (“the theorems of Becoming.Evolution”; the old English said 25, the Chinese 31, the 25 of the first landing and the six local laws: the count stays in the receipt and the snapshot) |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration) |
| V3 “The author's counterreview is in §29 of the integration note;” | evidence | validation_scope (“in the integration note”); §29 is in the first history note and the snapshot |
| V4 “the ninth independent review (BECOMING-P18B-P23-REVIEW.md) accepts its mathematics, and its corrections are handled in §34 of the integration note.” | evidence (review) | validation_scope (“listed under sources”, “in the integration note”); §34 is in the P23c history note and the snapshot |
| V5–V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V7 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“the local forms of the laws among them”) |
| R0 “Plan P21 asks for transmission, variation and selection through descent on the spine, with differences entering later activity through transmission and changing the conditions of later selection.” | provenance + correspondence | correspondence (“Plan P21” → “The unification plan”; its second half is said by the candidate's sentence that follows); P21 is in the first history note |
| R1 “The theory of evolution's central candidate says …” | correspondence | correspondence (unchanged) |
| R2 “This result gives that candidate its minimal formal content on the spine: selection is …; transmission is …; variation is …; and activity changes …” | correspondence | correspondence (“on the spine” dropped as said in R0; “support, a level meeting a need” in parentheses) |
| R3 “price is an arithmetic identity: two existing research notes derive its covariance form by hand and say so (the direction-frontier math-note; GENERATED-SELECTION-RECURRENCE-INTEGRATION, crediting Frank 2012).” | correspondence | correspondence (with C2's citation “Price 1970”; “crediting” → “citing”, zh 引 unchanged) |
| R4 “This result does not improve Price's equation; it checks it in counting form in the pure core.” | correspondence | correspondence |
| R5 “Dividing by the number of parents and rewriting as a covariance needs rationals and is not stated here.” | scope | does_not_show[0] |
| R6 “The substantive content is in the selection and transmission theorems: fitness is not defined, the number of offspring enters only as the weight in price, and support only as the condition of giving.” | correspondence + non-implication | correspondence (first clause); does_not_show[1] (the rest, “in price” → “in the identity”) |
| R7 “The theory of evolution's independent programme (structural copying, reconstruction, development and the inheritance of organizational rules, for example inherited-structural-copying and organizational-rule-inheritance) keeps its scope; no correspondence to it is proved here.” | correspondence | does_not_show[4]; the two records stay as related links (unchanged) |
| R8 “To its completion requirement 2, the recovery of established evolutionary explanations, this contributes only Price's equation in counting form; mutation, drift, movement and population dynamics are not covered.” | scope | does_not_show[3]; second clause does_not_show[2] |
| R9 “The readings of ‘descent’, ‘transmission’, ‘selection’ and ‘variation’ here are the AI's formulations, and names are Ren's.” | reading | correspondence; standard_boundaries: names-provisional |
| N0–N3 “The exact restatement for every world is this record's Flow.DescendsAt.supported_at, … transmitted_within_at (P50), the local condition inside the law: …; … are their corollaries;” | law (not a next step) | law 10 (the six local theorems as its declarations); P50 is in its history note |
| N4 “whether TransmitsWithin can be derived is answered by transmission-is-inheritance-and-need and transmission-independent-where-it-binds (P84): not from the other premises, and from a reading of drawing with drawing being depending;” | answered | hypotheses[2]; the P84 history note keeps the answer's provenance |
| N5 “a law of forming that is also necessary;” | next step | next_delta |
| N6–N10 “rational amounts and the covariance form; how the number of offspring is bounded by the amounts given (a reading of reproduction); the accumulation of selection and transmission over many steps; correspondence theorems to structural copying, reconstruction and the inheritance of organizational rules (periphery); names (Ren).” | next step | next_delta (unchanged) |
| H0 “price has no premise: …” | premise | hypotheses[0] (unchanged) |
| H1 “Selection: only active formations give (Acting) …” | premise | hypotheses[1] (unchanged); its conditions are also written into law 5 |
| H2 “Transmission: TransmitsWithin is a premise supplied by the application …; transmitted_within also uses balance (Balances).” | premise | hypotheses[2] (with L3 and N4 added) |
| X0 “Without Dependent: a parent active beyond its support … (Unchecked.unchecked).” | counterexample | counterexamples[0] (unchanged) |
