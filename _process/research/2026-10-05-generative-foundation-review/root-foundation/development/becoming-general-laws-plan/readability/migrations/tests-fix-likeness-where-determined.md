# Migration map: tests-fix-likeness-where-determined

Old record sha256 `231c99bfa422412280f32ec0194aaf5acba845c4cc21df809c7a9c928d09b263`; snapshot `_process/architecture/history/231c99bfa4224122/tests-fix-likeness-where-determined.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

The migration goes with a content change. `Becoming.Likeness` answers the record's next step: laws 3–7, the third hypothesis and the OneLoop counterexample are new, and the limitation saying branching tests were not stated in the core is superseded by them. Rows marked *superseded* or *answered* say which law replaces them.

| Old text | Type | New place |
|---|---|---|
| T0 “Tests fix likeness where determined” | title | title “Tests that fix likeness” (the record now also holds branching tests on finite decided frames); the old title is in the history note |
| S0 “Where both frames' branching is determined up to likeness, configurations are alike exactly where they pass the same tests;” | statement | statement (first clause, “linear tests fix likeness where both frames are determined up to likeness”); law 2 |
| S1 “without determinacy up to likeness the tests need not fix likeness.” | non-implication | counterexamples[0] (Choosing); hypotheses[0] |
| C0 “Let F and G be frames with the same move and claim types.” | framing | dropped as framing: every law compares two frames by bisimulation, which needs the same move and claim types (stated in configurations-alike-by-relation's hypotheses) |
| C1 “Configurations s and s′ pass the same tests (SameTests F G s s′) where the same courses of moves are open from each and after each course the same claims can be realized;” | definition | law 1 |
| C2 “alike configurations do (Alike.sameTests).” | law | law 1 |
| C3 “Where both frames are determined up to likeness, passing the same tests survives a move (SameTests.after) and is a bisimulation (sameTests_bisimulation), so configurations are alike exactly where they pass the same tests (alike_iff_sameTests;” | law | law 2 |
| C4 “for one determined frame, Determined.alike_iff_sameTests).” | law | law 2 (“so too for one determined frame”) |
| C5 “Without determinacy up to likeness the tests need not fix likeness: a frame choosing after its first move and one choosing at it pass the same tests from their starts and are not alike (Choosing.sameTests, Choosing.not_alike), the second not determined (Choosing.early_not_determined).” | counterexample | counterexamples[0] (its detail now carries this sentence with the three names) |
| C6–C7 “No premise; constructive.” | premise | standard_boundaries: no-ethical-premise; statement (“by a constructive proof”); hypotheses[0] and [2] name the conditions |
| L0–L1 “That branching tests fix likeness is not stated in the core (the periphery's proof reasons classically; whether a constructive proof exists for frames with finitely many configurations is open here);” | scope | *superseded*: laws 3–6 (constructive, on finite decided frames); the periphery's classical proof is in the correspondence; what the proof uses is does_not_show[0] |
| L2 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; correspondence keeps “Reading (the AI's, pending Ren)” |
| L3 “no ethical predicate occurs.” | standard boundary | standard_boundaries: no-evaluation (and no-ethical-premise) |
| V0–V1 “14 October 2026: the current bytes of Becoming.Unfolding are bound to consolidated receipt 20261013T204910.042715Z (passed: …; the 86-module core closure compiles from the prelude).” | evidence | validation_scope (the binding receipt); the counts stay in the receipt and the snapshot |
| V2 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | snapshot; the rename table stays in the plan |
| V3 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 27 theorems of Becoming.Histories all have empty axiom reports, among them …” | evidence | validation_scope (the theorems of Becoming.Histories, receipt 20261013T094743.528770Z); the count and the list stay in the receipt and the snapshot |
| V4 “The same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V5 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + snapshot |
| V6–V7 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V8 “The author's counterreview is in §98 of the integration note;” | evidence | validation_scope (“in the integration note”); §98 is in the correspondence |
| V9 “there is no independent review yet.” | evidence | validation_scope |
| R0 “The second item of P76 (work board), following Ren's “move towards 100%” of 12 October 2026: it gives what configurations-alike-by-relation's next_delta names, a constructive condition in the core under which passing the same tests makes configurations alike: determinacy up to likeness.” | round narration + provenance | history (the P76 note, unchanged); the dependency on configurations-alike-by-relation is unchanged |
| R1–R2 “Reading (the AI's, pending Ren): what tests cannot see is when a choice is made; with branching, only tests that branch see it.” | reading | correspondence (unchanged); law 7 is its theorem in the core |
| R3 “In the periphery, branching tests fix likeness for image-finite models (same_iff_bisimilar, classically), joined to the core's bisimulation by P69's bridge section (branching_bisimulation_iff).” | correspondence | correspondence (“P69's bridge section” → “the bridge”; the core's constructive form and excluded middle added) |
| R4 “See the integration document §98.” | provenance | correspondence (“See §98 of the integration note and its section on Becoming.Likeness”) |
| N0 “A constructive proof that branching tests fix likeness on frames with finitely many configurations and decided steps and claims, or the boundary naming the logical principle it needs.” | next step | *answered*: laws 4–6 (the proof), law 6 and the OneLoop counterexample (excluded middle for deciding likeness); law 5 bounds the stopping depth by the number of pairs of configurations; next_delta now names the bridge to the periphery's Test |
| H0 “alike_iff_sameTests takes both frames determined up to likeness everywhere as its condition; without it, Choosing gives a counterexample.” | premise | hypotheses[0] (unchanged) |
| H1 “A test is a finite course of moves, possibly followed by one claim; branching tests with negation and conjunction are in the periphery (ExplanatoryBranching).” | premise | hypotheses[1] (second clause → “a branching test adds failure, conjunction and what some step by a move can lead to”, now in the core; the periphery's tests are in the correspondence and does_not_show[1]) |
| X0 “Choosing: frames choosing after and at the first move pass the same tests and are not alike.” | counterexample | counterexamples[0] (with C5's names and the second frame's indeterminacy) |
