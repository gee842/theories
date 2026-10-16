# Migration map: configurations-alike-by-relation

Old record sha256 `97ead96868c7a72410ac410e542ad6ed43bae3acbd45011774207e02d744f6a5`; snapshot `_process/architecture/history/97ead96868c7a724/configurations-alike-by-relation.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Unfolding.lean` (with `Determined` in `Joint.lean`, `Frame` in `Frame.lean`, `carries_law_iff` in `Mechanism.lean`, `FactorsThrough` in `Experiment.lean`, `Law.orbit`, `Law.orbit_shift` and `Law.process` in `Recurrence.lean`, and the bridge declarations in `Bridge.lean`; bytes bound by the record's references). The laws keep their theorems' conditions: `Bisimulation` and `Alike` compare frames `Frame S A C` and `Frame S' A C` with the same move and claim types; `DeterminedAt.goAlike` takes determinacy up to likeness at the second configuration, which by `DeterminedAt.transfer` holds at the first as well, so “where it holds” is unchanged; `IdentifiesAlike.carries` takes `∀ s, DeterminedAt F s` (law 8, “everywhere”); `Law.IdentifiesAlike.carries` needs no further condition, the registered law being determined (`Law.registered_determined`). No law is wider than its theorem.

The statement was narrowed to the theorem's condition. The old statement (the former title) said a description that makes sense “then carries a law”; `IdentifiesAlike.carries` proves it where the frame is determined up to likeness at every configuration, so the statement now says “and carries a law where the frame is determined up to likeness”.

| Old text | Type | New place |
|---|---|---|
| T0 “A configuration is how it relates” | title | title (unchanged) |
| S0 “Configurations related by a bisimulation are alike and pass the same tests;” | statement | statement (unchanged) |
| S1 “a description makes sense where it identifies exactly the alike ones, and then carries a law;” | statement | statement (“and carries a law where the frame is determined up to likeness”, see above) |
| S2 “determinacy as equality depends on names.” | statement | statement (unchanged) |
| C0 “Let F and G be frames on configurations S and S′ with the same moves A and claims C.” | framing | law 1 (Frame among the declarations) |
| C1 “A relation B is a bisimulation between them (Bisimulation F G B) where …” | definition | law 1 |
| C2 “s and s′ are alike (Alike F G s s′) where some bisimulation relates them.” | definition | law 1 |
| C3 “Equality is a bisimulation, the converse of a bisimulation is one, and two compose (Bisimulation.eq, Bisimulation.converse, Bisimulation.comp);” | law | law 2 |
| C4 “so likeness is reflexive, symmetric and transitive (Alike.refl, Alike.symm, Alike.trans), stated as a relation since a quotient needs Quot.sound.” | law | law 2 |
| C5 “Alike configurations realize the same claims (Alike.realized), match each other's steps … (Alike.step) and every course of moves into alike configurations (Bisimulation.trace, Alike.trace), and pass the same tests, a course of moves followed by a claim (Alike.tests).” | law | law 3 |
| C6 “A frame is determined up to likeness at s (DeterminedAt F s) where any two outcomes of one move at s are alike;” | definition | law 4 |
| C7 “a determined frame is so everywhere (Determined.at);” | law | law 4 (Determined among the declarations) |
| C8 “determinacy up to likeness passes along likeness (DeterminedAt.transfer), and where it holds the same move takes alike configurations to alike ones (DeterminedAt.goAlike).” | law | law 4 |
| C9 “In Twins a start has two successors by one move: they are alike (Twins.left_alike_right), the frame is not determined (Twins.not_determined), and … (Twins.alike_one).” | law (witness) | law 5 (the Twins frames, bisimulations and lemmas among the declarations); counterexamples[0] (unchanged) |
| C10 “Under the law of exchange read through the claims that a relatum stands at an amount (exchangeFrame), agreeing at every relatum is a bisimulation (exchange_pointwise_bisimulation);” | law | law 6 |
| C11 “standings are alike exactly where they agree at every relatum (exchange_alike_iff, exchange_alike_of_pointwise, exchange_pointwise_of_alike), and the law is determined up to likeness at every standing (exchange_determinedAt).” | law | law 6 |
| C12 “A description π of configurations makes sense (IdentifiesAlike F π) where it identifies exactly the alike configurations;” | definition | law 7 |
| C13 “it does exactly where being identified by it is a bisimulation and it identifies every alike pair (identifiesAlike_iff);” | law | law 7 |
| C14 “descriptions that make sense identify the same configurations (IdentifiesAlike.unique);” | law | law 7 |
| C15 “where the frame is determined up to likeness everywhere, a description that makes sense carries a law (IdentifiesAlike.carries, through carries_law_iff of Becoming.Mechanism);” | law | law 8 (FactorsThrough and carries_law_iff among the declarations) |
| C16 “naming the configurations makes sense exactly where alike configurations are one (identifiesAlike_id_iff), and the twins' naming does not (Twins.naming_not_identifiesAlike).” | law | law 8 |
| C17 “For a determined law read through a registration (Law.registered next o, the claims being what is registered), configurations are alike exactly where their registered futures are the same (…), and there a description that makes sense carries a law (Law.IdentifiesAlike.carries).” | law | law 9 (Law.orbit, Law.orbit_shift and Law.process among the declarations) |
| C18 “In the periphery bridge (Becoming.Bridge): Deeper.Bisimulation of RelationalDynamics is the core's bisimulation of frames with no claims (Frame.bare, deeper_bisimulation_iff), so in static and toggle … (static_toggle_alike);” | law | law 10 |
| C19 “ExplanatoryBranching.Bisimulation is the core's bisimulation of frames whose claims are a model's conditions (Frame.ofModel, branching_bisimulation_iff), and alike configurations pass every branching test, negation and conjunction included (Alike.same, through bisimulation_implies_same).” | law | law 11 |
| C20 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for the cited core and bridge declarations) |
| H0–H4 | premise | hypotheses[0]–[4] (unchanged) |
| R0 “The fourth item of P69 (work board), following Ren's “yes, put it on the board and start” of 12 October 2026: the split “configurations prior to their relation” stated from the world's side.” | provenance + round narration | correspondence (“Following Ren's “yes, put it on the board and start”: …”, Ren's words verbatim); “The fourth item of P69 (work board)” and the date → history (the first history note already records “2026-10-12 P69: added, following Ren's ‘yes, put it on the board and start’”) |
| R1–R3 “It brings into the core the periphery's relational identity of configurations (…). There a step leaving the configuration unchanged … so does determinacy as equality (Twins).” | provenance | correspondence (unchanged) |
| R4–R5 “Readings (the AI's; Ren agreed): the names of configurations, … function extensionality adding only that alike standings are one and the same.” | reading | correspondence (unchanged; the attribution “Readings (the AI's; Ren agreed)” is kept exactly) |
| R6 “Descriptions that make sense restate on this module's definitions … (its Saying.lean, answering Ren's questions on framing and pairs).” | provenance | correspondence (unchanged) |
| R7 “See §91 of the integration note.” | provenance | validation_scope (“Author counterreview in §91 of the integration note”) |
| L0 “That configurations passing the same tests are alike is stated in tests-fix-likeness-where-determined, for linear tests where both frames are determined up to likeness and for branching tests where both are finite and decided;” | converse | does_not_show[0] (kind converse, “its conditions are in tests-fix-likeness-where-determined”); the conditions themselves are in the existing related link to tests-fix-likeness-where-determined (unchanged) and hypotheses[1] |
| L1 “the Part I theorems stated with Determined are restated up to likeness in determinacy-up-to-likeness;” | cross-reference | hypotheses[2] (duplicate); the existing related link to determinacy-up-to-likeness (unchanged) |
| L2 “bisimulation compares only frames with the same move and claim types;” | scope | hypotheses[1] (duplicate); law 1 (“with the same moves A and claims C”) |
| L3 “that a description making sense exists is not stated (describing each configuration by what it is alike to makes sense given function and propositional extensionality, and the quotient by likeness needs Quot.sound);” | scope | does_not_show[1]; hypotheses[3] (that one exists is not derived) |
| L4 “likeness takes no quotient, so “alike configurations are one and the same” is not stated here;” | scope | does_not_show[2] |
| L5 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional (“readings remain Ren's”); the correspondence keeps “Readings (the AI's; Ren agreed)”, the attribution written with Ren's likeness readings of 14 October |
| L6 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Bridge, Becoming.Mechanism, Becoming.Unfolding, Becoming.Joint are bound to consolidated receipt 20261013T221720.428753Z (passed: …).” | evidence | validation_scope (Unfolding, Joint and Mechanism bound by 20261013T221720.428753Z); Bridge has since been rebound to 20261014T141427.442103Z (batch 5, the history note before the migration note), so the paragraph names that receipt, as the proof bindings do; the counts stay in the receipt and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | history (the rename note) + snapshot |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 67 theorems of Becoming.Unfolding all have empty axiom reports, among them …” | evidence | validation_scope (the theorems of Becoming.Unfolding, receipt 20261013T094743.528770Z, which binds Frame, Experiment and Recurrence); the count and the list stay in the receipt and the snapshot |
| V3 “In the same receipt the periphery bridge Becoming.Bridge's deeper_bisimulation_iff, static_toggle_alike, branching_bisimulation_iff and Alike.same have empty axiom reports.” | evidence | validation_scope (“the bridge theorems cited here”) |
| V4 “The same receipt covers the package's 75 modules … and 22 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V5 “periphery receipt 20261011T232716.311380Z passed.” | evidence | snapshot; named in the migration history note |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V7–V8 “The author's counterreview is in §91 of the integration note; there is no independent review yet.” | evidence | validation_scope |
| V9–V12 “P89 (13 October 2026): prior Bridge declarations remain; four added adapters are checked with empty axiom reports. This record binds Bridge to the new frozen receipt while other proofs retain their original receipts; adapters are not independent results.” | evidence (adapters) | validation_scope (“Bridge by 20261014T141427.442103Z, its added adapters not being separate results”); “P89 (13 October 2026)” and the adapter count → history (P89 notes) + snapshot |
| N0 “Counting configurations up to likeness on finite frames where likeness is decided, joined to relata-counted-up-to-indiscernibility.” | next step | next_delta (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |

Remaining lint warning: the correspondence is 16 characters over its English cap (1216 > 1200). It keeps Ren's words, the provenance of the relational identity and the readings with their attribution as written on 14 October; only the round label, the date already in history and the section reference already in the evidence moved out.
