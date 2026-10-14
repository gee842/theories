# Migration map: experiment-needs-return

Old record sha256 `45aaef17adb1820bad104761a9e8d8d5b6477b2c20fd8548a78cc72aa203929f`; snapshot `_process/architecture/history/45aaef17adb1820b/experiment-needs-return.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Experiment.lean` (with `Determined` in `Joint.lean`, `revisits_from` and `Law.withHistory` in `Recurrence.lean`, `Run` in `Frame.lean`; bytes bound by the record's references). Three laws now carry conditions of their theorems that the old claim left to context. Law 3: `not_fixes_other_of_new` takes `determined` and `two` (P determined, two different configurations), which the old text stated in hypotheses[0] only for “an untaken move is not fixed”. Law 4: `keepHistory_fixes_nothing_else` takes the same two conditions. Law 7: `misattributes` takes `first : moves 0 = left` and `second : moves 1 = right`; the law says “where the first two moves are left then right”. No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Experiment needs return” | title | title (unchanged) |
| S0–S1 “Relative to determinacy, the record fixes a move's outcome exactly where it was taken, and what one's act would have done otherwise is fixed only where the configuration returns. A kept history never returns, so experiment needs a model of what is irrelevant.” | statement | statement (unchanged) |
| C0–C1 “Let r be a run of a process P. Relative to determinacy, the record up to a step fixes the outcome of move a at configuration s to u when … (Run.Fixes).” | definition | law 1 |
| C2 “Once the run has taken a at s, the record fixes it to where the run went (Run.fixes_of_takes);” | law | law 2 |
| C3 “where P is determined, there are two different configurations and the run has not taken a at s, the record fixes no outcome of it, whatever registers: … (retarget, retarget_determined, Run.stepsOf_retarget, Run.not_fixes_of_untaken).” | law | law 2 (retarget_step among the declarations) |
| C4 “So where the configuration returns, another move's outcome is fixed (Run.fixes_on_return), and a run whose configurations never return fixes, at each configuration it passes, no move other than the one it takes (Run.not_fixes_other_of_new).” | law | law 3 (“with P determined and two different configurations” written in, see above; ordered_of_ne among the declarations) |
| C5 “In the process keeping the history of configurations and moves passed through (keepHistory, the counterpart with moves of Law.withHistory) the past grows by one at each step, so every step is new (keepHistory_length, keepHistory_new), determinacy is kept (keepHistory_determined), and nothing about one's own acts but what one did is fixed (keepHistory_fixes_nothing_else).” | law | law 4 (the same two conditions written in, see above) |
| C6 “Read through a projection π: once the run has taken a at a configuration projecting to k, the record so read fixes its outcome (Run.fixesThrough_of_takes);” | law | law 5 (Run.StepsThrough, Run.FixesThrough among the declarations) |
| C7 “where P's step factors through π into a determined process (FactorsThrough), the fixed outcome is the outcome, read through π, at every configuration projecting to k, passed by the run or not (Run.generalizes);” | law | law 5 (stepsThrough_of_factors among the declarations) |
| C8 “within finitely many projected configurations the projection returns from every step on (Run.projection_returns, an instance of revisits_from).” | law | law 6 (“a list holding every one”, the theorem's held) |
| C9 “In Confound the configuration is a hidden bit and an outcome, each step flips the hidden bit and sets the outcome to the hidden bit before the step, and the move makes no difference (Confound.move_idle);” | definition (witness) | law 7 |
| C10 “read through the outcome, the record up to the second step fixes left to false and right to true (Confound.misattributes);” | law (witness) | law 7 (“where the first two moves are left then right” written in, see above); counterexamples[0] (unchanged) |
| C11 “with the moves in step with the hidden bit, the determined model in which the move decides the outcome admits the projected steps at every step (Confound.confounded);” | law (witness) | law 8; counterexamples[0] (unchanged) |
| C12 “moving left again where the hidden bit differs from the first step, no determined process admits the projected steps up to the fifth (Confound.varied_refutes).” | law (witness) | law 8; counterexamples[0] (unchanged) |
| C13 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| H0–H3 | premise | hypotheses[0]–[3] (unchanged) |
| R0 “P49's open item (review F6): what an act does compares the history with it and the history without it.” | provenance | correspondence (“The open item of testing-within-registration (review F6)”) |
| R1 “After P49 landed Ren wrote “land and merge all, then continue”, and on the result “no extra review needed, merge, then continue”.” | Ren's words | correspondence (verbatim; “After that result landed”) |
| R2 “Readings (the AI's, pending Ren): an experiment is …; replication is that return; a control is …; variation independent of what is left out is …;” | reading | correspondence (unchanged) |
| R3 “with P49's registration as the reading, threshold and reach blindness are cases where the step does not factor.” | reading | correspondence (“with the registration of testing-within-registration as the reading”) |
| R4 “See §72 of the integration note.” | provenance | validation_scope (“author counterreview in the integration note”); §72 stays in the snapshot and the first history note |
| L0 “That a formation varies its acts, keeps or forgets its history, or forms a projection is not derived” | non-implication | does_not_show[0] (“The laws do not derive …”) |
| L1 “which projection the actual unfolding factors through is empirical” | correspondence | does_not_show[1] |
| L2 “random or undetermined processes are not treated” | scope | does_not_show[2] |
| L3 “whole configurations rarely return in practice, so the positive results in practice go through projections” | correspondence | does_not_show[3] |
| L4 “the formal bridge to Becoming.Testing's registration is not stated” | scope | does_not_show[4]; next_delta (its first item, unchanged in substance) |
| L5 “the general form of which correlation between moves and what is hidden leaves a model unrefuted is not stated” | scope | does_not_show[5]; next_delta (its second item, unchanged) |
| L6 “the readings are the AI's, pending Ren” | standard boundary | standard_boundaries: names-provisional; the correspondence says “Readings (the AI's, pending Ren)” |
| L7 “contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 25 theorems of Becoming.Experiment all have empty axiom reports, among them …;” | evidence | validation_scope (the receipt); the count and the list stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 91 modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration); named in the migration history note |
| V3–V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V5 “The author's counterreview is in §72 of the integration note; at Ren's “no extra review needed” there is no independent review.” | evidence | validation_scope (Ren's words verbatim); §72 stays in the snapshot |
| (proof bindings) | evidence | validation_scope names the receipts that bind each source, already in the references and proof bindings |
| N0 “The formal bridge with Becoming.Testing's registration as the projection (for any projection P66 states the condition: …, carries_law_iff; P73 states when an observed outcome transfers rightly: …, transfer_right_iff);” | next step + completed connections | next_delta (“(see projection-carrying-a-law and generalization-through-lumping)”); the P66 and P73 parentheses → history (the migration note, in full) |
| N1 “the general form of which correlation between moves and what is hidden leaves a model unrefuted;” | next step | next_delta (unchanged) |
| N2 “experiment where a forgotten part of the move makes a difference (P68: with the noise forgotten, the standard model is determined exactly where the noise makes no difference, forget_inputs_determined_iff).” | next step + completed connection | next_delta (“(see causal-models-as-processes)”); the P68 parenthesis → history (the migration note, in full) |
| X0 | counterexample | counterexamples[0] (unchanged) |
