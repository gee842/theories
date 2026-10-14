# Migration map: necessarily-drawn-is-not-returning

Old record sha256 `5fe270fea40c93bb2cc5b2c0bfc88a7c86a7b06acc42ddb0da2fb38b1e58b020`; snapshot `_process/architecture/history/5fe270fea40c93bb/necessarily-drawn-is-not-returning.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C0–C1 hold en C0, so later zh claim labels run one ahead).

Each law was read against its declarations in `Becoming/Branching.lean` (which also holds Capture's rule-region laws and `Captured`), with `Law.DrawnInto` and `Law.drawn_iff_not_returns` in `Becoming/Attraction.lean`, `Law.Returns` in `Becoming/Recurrence.lean` and `Invariant` and `Run` in `Becoming/Frame.lean`. None states more than the declaration. `NecessarilyDrawn.not_lossless` keeps its list of every configuration and its given run beginning at the configuration, and its conclusion stays “rules out that the process merges nothing”, with no merge supplied (as history entry 2 corrected). `Law.perturbation_drawnInto` keeps its condition that the perturbed configuration differs from the one the rule holds (“a perturbed state, differing from it”).

Flag for the record's owner: the claim cites four declarations that exist in the current sources but are not among this record's references: `Branching.Returns.run` (an alias of this record), `Branching.Determined.moves_decide`, `Run.enters_returning` and `Branching.Transit.returning_not_invariant`. References are not changed by this migration, so the laws and the item that state them keep the names in their text; law 6 cites the referenced instance `Branching.OneWay.moves_decide`, which is proved by `Determined.moves_decide`. Adding the four to the Branching.lean reference would let the laws cite them directly.

| Old text | Type | New place |
|---|---|---|
| T0 “Possibly and necessarily drawn” | title | title (unchanged) |
| S0–S1 | statement | statement (unchanged) |
| C0–C1 “A configuration outside a region is possibly drawn into it (PossiblyDrawnInto) where some course from it enters it, and necessarily drawn (NecessarilyDrawnInto) where every run from it does; drawn (PossiblyDrawn, NecessarilyDrawn) where some region the process never leaves (Frame.Invariant) so draws it.” | definitions | law 1 |
| C2 “Under a determined law both are P67's (law_possibly_iff, law_necessarily_iff, law_drawn_iff).” | laws + work-item label | law 2 (“in the sense of attraction-is-not-returning”, the record of that work item, a dependency, unchanged; the three equivalences written out as the declarations state them) |
| C3 “A configuration that returns has a run that never loses it, going round its course back to it forever (Branching.Returns.run, constructively).” | law | law 3 (first sentence; see the flag above) |
| C4 “So every process necessarily draws exactly what does not return (…, the instance of Law.drawn_iff_not_returns): what is necessarily drawn never returns (…), and what does not return is necessarily drawn into what lies ahead of it at the first step (…).” | laws | law 3 (“with no premise”, from C15 and the declaration's docstring) |
| C5 “Possibly drawn is losing oneself on some course (possiblyDrawn_iff), locked in along that course (PossiblyDrawnInto.never_back);” | laws | law 4 (the equivalence written out: some course leads where the configuration cannot be had again) |
| C6 “a configuration possibly drawn may return on another course: OneWay's false is possibly but not necessarily drawn into {true}, and returns (OneWay.possibly_not_necessarily).” | law (witness) | law 5; counterexamples[0] (unchanged) |
| C7 “Under a determined process the moves decide whether a run is drawn in (Determined.moves_decide).” | law | law 6 (the theorem's content written out; see the flag above) |
| C8 “Under every process the future narrows: …” | laws | law 7 (“every run entering at step n”, as `lost_necessarily_drawn` states) |
| C9 “within finitely many configurations every run enters what returns (Run.enters_returning), and … (NecessarilyDrawn.not_lossless, concluding ¬ Lossless P rather than supplying a witness of Merges).” | laws | law 8 (see the flag above) |
| C10 “What fails for processes: what returns is not a region the process never leaves (Transit.returning_not_invariant);” | non-implication | does_not_show[0] (“need not be … as it is for determined laws”); counterexamples[0] (unchanged, Transit) |
| C11 “a merge need draw neither of the two (OneWay.merge_keeps).” | non-implication | does_not_show[1] (witness OneWay.merge_keeps, written out as the declaration states) |
| C12–C13 “In Capture, where the rule keeps itself, … (Law.rule_absorbing); where the next configuration also depends on the rule alone, … (Law.held_absorbing), and a perturbed state is drawn into it at the first step (Law.perturbation_drawnInto);” | laws | law 9 |
| C14 “the instances in Captured (…).” | laws (instances) | law 10 (what the instances state, written out) |
| C15 “No premise.” | premise | law 3 (“with no premise”); standard_boundaries: no-ethical-premise |
| L0 “Being drawn in within a bound is not stated;” | scope | does_not_show[2]; next_delta keeps the step |
| L1 “no measure on branching courses is given (see P82);” | scope + work-item label | does_not_show[3] (P82 → Becoming.Weighted, the module of weighted histories) |
| L2 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “Reading (the AI's, pending Ren)” |
| L3 “no ethical predicate occurs.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Attraction, Becoming.Branching, Becoming.Capture are bound to consolidated receipt 20261013T204910.042715Z (passed: …).” | evidence | validation_scope (the binding receipt, without the date; counts in the receipt and the snapshot) |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | validation_scope (“which checked them under the current names”); the rename table stays in the plan |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 119 theorems of Becoming.Branching …” | evidence | validation_scope (20261013T094743.528770Z binds Becoming.Recurrence and Becoming.Frame, as the proof bindings have it); the count and the list stay in the receipt and the snapshot |
| V3–V4 counts and periphery receipt | evidence | receipt + snapshot |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the detail stays in the receipt and the snapshot |
| V6 “The author's counterreview is in §99 of the integration note;” | evidence | validation_scope (“in the integration note”); §99 is in history entry 0 |
| V7 “there is no independent review yet.” | evidence | validation_scope |
| R0 “P81 (work board), as above;” | work-item label | history entry 0 (existing: P81, following Ren's ‘move towards 100%’) |
| R1 “P67's attraction for processes that are not determined.” | provenance | correspondence (“This answers attraction for processes that are not determined, a next step of attraction-is-not-returning”) |
| R2–R4 readings | reading | correspondence (unchanged) |
| R5 “See the integration document §99.” | provenance | history entry 0 (existing: “see §99 of the integration note”) |
| N0 “Being drawn in within a bound;” | next step | next_delta |
| N1 “use P82's weightings for a measure of being drawn in.” | next step | next_delta (P82 → Becoming.Weighted) |
| H0 | premise | hypotheses[0] (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |
