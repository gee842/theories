# Migration map: determinacy-up-to-likeness

Old record sha256 `6025cce14a75d45f4e4a5e305811138ec803276e97c7f999c3652964032da998`; snapshot `_process/architecture/history/6025cce14a75d45f/determinacy-up-to-likeness.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

The migration goes with a content change. `Becoming.Likeness` answers the record's next step: laws 5–9 and the Parting counterexample are new, and the old text saying what was not yet restated is superseded by them. Rows marked *superseded* say which law replaces them.

| Old text | Type | New place |
|---|---|---|
| T0 “Determinacy up to likeness” | title | title (unchanged) |
| S0 “With configurations named, determinacy is determinacy up to likeness.” | statement | statement (first clause, “the named case of determinacy up to likeness”) |
| S1 “The theorems on how configurations relate hold up to likeness, while an intervention on one of alike configurations, an unregistered past and an unregistered description need equality.” | statement | statement (second clause; “including when a description carries a law” added for laws 6–8) |
| C0 “Determinacy is determinacy up to likeness where the claims name the configurations (determined_iff_named, alike_configurations), so each theorem stated with Determined is the named instance of one stated with DeterminedAt.” | law | law 1 (“with Determined”/“with DeterminedAt” → “with determinacy”/“up to likeness”; the names are its declarations) |
| C1 “These hold up to likeness: going alike through likeness is determinacy up to likeness (goesAlike_iff, after goAlike_id_iff);” | law | law 2 (“after goAlike_id_iff” → “the counterparts stated with equality are their named instances”; goAlike_id_iff among the declarations) |
| C2 “runs alike stay alike (DeterminedAt.stays_alike, after GoAlike.runs_agree);” | law | law 2 (GoAlike.runs_agree among the declarations) |
| C3 “what the step does not depend on is re-absorbed up to likeness (DependsOnlyOnAlike.reabsorbed);” | law | law 3 |
| C4 “with the noise forgotten, the standard model is determined up to likeness exactly where the noise makes no difference up to likeness (forget_inputs_determinedAt_iff);” | law | law 3 |
| C5 “a move taken is fixed up to likeness (Run.fixesAlike_of_takes) and one occasion stands for its class (Run.generalizesAlike);” | law | law 4 |
| C6 “a move taken at no configuration alike to the one named is not fixed, for outcomes that differ in a claim (Run.not_fixesAlike_of_untaken), through an intervention on a whole likeness class (retargetAlike, retargetAlike_determinedAt).” | law | law 4 |
| C7 “These need equality, or claims registering what equality tells apart: retargeting one of two alike configurations breaks determinacy up to likeness (Twins.retarget_breaks);” | law + counterexample | law 10 (first clause); counterexamples[0] (Twins.retarget_breaks, unchanged); the framing “need equality” is in the statement |
| C8 “a kept history returns up to likeness where its present does and nothing registers the past (keepFrame_alike_iff, keepHistory_returns_alike), so keepHistory_new needs the past registered (keepHistory_new_named);” | law | law 10 (“so keepHistory_new needs the past registered” → “so a kept history is new only with its past registered”; keepHistory_new_named among the declarations) |
| C9 “with nothing claimed, every description carries a law and no confound is refuted (carries_unregistered, Confound.refutes_registered).” | law | law 7 (every description carries a law, carries_unregistered); law 11 (no confound is refuted) |
| C10 “No premise.” | premise | hypotheses[0]; standard_boundaries: no-ethical-premise |
| L0 “The main theorems of Experiment and Mechanism on how configurations relate are restated;” | scope | statement (“the laws on how configurations relate hold up to likeness”) |
| L1 “not restated: Mechanism's characterization of determinacy through a projection (Image, FactorsThrough), Experiment's not_fixes_other_of_new and Joint's determined_dichotomy;” | scope | *superseded*: law 8 (Image: image_determinedAt_iff, with Parting for Image.least), laws 6–7 (FactorsThrough: carries_law_alike_iff, carries_law_named_iff), law 5 (not_fixes_other_of_new), law 9 (determined_dichotomy) |
| L2 “carries_law_iff has no two-way form up to likeness;” | scope | *superseded*: laws 6–7 |
| L3 “instances stating that a process is determined give determinacy up to likeness directly through Determined.at;” | scope | does_not_show[1] |
| L4 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; correspondence keeps “Reading (the AI's, pending Ren)” |
| L5 “no ethical predicate occurs.” | standard boundary | standard_boundaries: no-evaluation (and no-ethical-premise) |
| V0–V1 “14 October 2026: the current bytes of Becoming.Branching, Becoming.Mechanism, Becoming.Unfolding, Becoming.Joint are bound to consolidated receipt 20261013T221720.428753Z (passed: …; the 90-module core closure compiles from the prelude).” | evidence | validation_scope (the binding receipt); the counts stay in the receipt and the snapshot |
| V2 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | snapshot; the rename table stays in the plan |
| V3 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 119 theorems of Becoming.Branching all have empty axiom reports, among them …” | evidence | validation_scope (the theorems of Becoming.Branching, receipt 20261013T094743.528770Z); the count and the list stay in the receipt and the snapshot |
| V4 “The same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V5 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + snapshot (the record cites no peripheral declaration) |
| V6–V7 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V8 “The author's counterreview is in §99 of the integration note;” | evidence | validation_scope (“in the integration note”); §99 is in the correspondence |
| V9 “there is no independent review yet.” | evidence | validation_scope |
| R0 “P81 (work board), as above;” | round narration | history (the P81 note, unchanged) |
| R1 “answering the next_delta of configurations-alike-by-relation.” | provenance | history; the dependency on configurations-alike-by-relation is unchanged |
| R2–R4 “Reading (the AI's, pending Ren): likeness is the unfolding's own identity of configurations; … What nothing registers is neither fixed nor refuted (compare the registers of Becoming.Testing).” | reading | correspondence (unchanged; one sentence added on carrying a law up to likeness) |
| R5 “See the integration document §99.” | provenance | correspondence (“See §99 of the integration note and its section on Becoming.Likeness”) |
| N0 “Give the exact form of carries_law_iff up to likeness (through registered descriptions);” | next step | *answered*: laws 6–7 |
| N1 “restate up to likeness the characterization through Image and FactorsThrough, not_fixes_other_of_new and Joint's determined_dichotomy, or give witnesses that they need equality.” | next step | *answered*: laws 5, 8, 9 and the Parting counterexample; next_delta now names what is left, not_fixesThrough_* |
| H0 “carries_law_iff has no two-way form up to likeness, only the triviality witness;” | premise | *superseded*: laws 6–7 (the triviality witness is law 7's second clause) |
| H0 “not_fixesThrough_* are not restated.” | scope | does_not_show[0]; next_delta |
| X0 “Twins.retarget_breaks: retargeting one of two alike twins breaks determinacy up to likeness.” | counterexample | counterexamples[0] (unchanged) |
