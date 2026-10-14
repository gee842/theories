# Migration map: levels-of-closure

Old record sha256 `4d338b9e139797e9bfb6ed623033cc1e3d2ea7f4a3673e2ad5bfd16641e521da`; snapshot `_process/architecture/history/4d338b9e139797e9/levels-of-closure.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C2 holds en C2–C3, so zh C3–C11 are en C4–C12; zh C12 holds en C13–C14 and zh C14 holds en C16–C17, so zh C13 is en C15 and zh C15–C22 are en C18–C25; zh V9 holds en V9–V10 and zh V10 holds en V11–V12).

Each law was read against its declarations in `Becoming/Feedback.lean`, `Becoming/Bridge.lean` (`withinClosure_iff_closure`, `Closure`), `Becoming/Interdependence.lean` and `Becoming/Significance.lean`. Three laws are narrower in wording than the old text, to match the theorems:

- C21 said every feeding closure is the whole “where at one step every formation requires it and gives to it”. `Flow.feeding_whole_of_common` (and `Flow.feeding_unrestricted_of_common`) also ask every formation to take part at that step (`g ∈ L.present t`); law 10 says so.
- C17 said the dweller's reach closure “holds only itself”. `Clearing.reach_centred` states `¬ flow.WithinReach web .dweller .clearer` (its docstring says more than its statement); law 8 says the dweller's reach closure does not hold the clearer, which is what makes reach centred rather than a class.
- C18 said that in Static “neither affects the other”. `Static.shares_unaffected` states one direction, `¬ flow.AffectedBy web true false` and `¬ flow.WithinInfluence web true false`; law 9 states that direction. The two formations are alike in the witness, but the other direction is not a stated theorem.

No law states more than its declaration.

| Old text | Type | New place |
|---|---|---|
| T0 “Five levels of closure” | title | title (unchanged) |
| S0–S1 “The feeding closure lies within the influence closure, …; one common condition makes the system the whole.” | statement | statement (unchanged) |
| C0–C2 “A region is closed under a relation (ClosedUnder) …; g lies within f's closure … (WithinClosure) …. The closure is reflexive and transitive, … (WithinClosure.refl, trans, of_rel, mono, symm, not_rel);” | definitions + laws | law 1 (names → declarations) |
| C3–C4 “it is itself closed (closedUnder_withinClosure), so it is the least closed region holding f; it is exactly the seed–edge closure of Becoming.Bridge from the one seed f (withinClosure_iff_closure).” | law | law 2 (names → declarations, with `Closure`) |
| C5 “P40's feeding closure is the closure under being fed at some step (Flow.FedFrom, Flow.withinFeeding_iff, Flow.fedClosed_iff).” | law | law 3 (“P40's” dropped; the feeding closure's record is the dependency feeding-closure); P40 → history + snapshot |
| C6–C8 “A formation is affected by another (Flow.AffectedBy) when …; the influence closure (Flow.WithinInfluence) …; the reach closure (Flow.Affects, Flow.WithinReach) …” | definitions | law 4 (names → declarations; what exchanging is, from `Flow.Exchanges`, written in) |
| C9–C11 “A formation takes part in a condition (Flow.TakesPart) …; two formations … share it (Flow.Shares); the system (Flow.WithinSystem) is the closure under sharing, a class (…)” | definitions + laws | law 5 (names → declarations) |
| C12 “The feeding closure lies within the influence closure (…), the influence and reach closures lie within the system (…), and the system is closed under affecting (Flow.withinSystem_closed).” | law | law 6 (names → declarations; “With no premise” from C24) |
| C13 “Each inclusion can be strict, and the influence and reach closures point in opposite directions.” | law (summary of witnesses) | statement; law 7 (“Each inclusion can be strict.”) and law 8 (“so the two closures point in opposite directions”) |
| C14–C15 “In Trophic, a trophic cascade, both flows balance, …; the wolves give to nothing, … (Trophic.mediates, Trophic.near_closed).” | law (witness) | law 7 (names → declarations) |
| C16–C17 “In Clearing the source lies within the clearer's feeding closure … (Clearing.alongDependence_closed, Clearing.levels); the clearer's reach closure holds the dweller and not the source (…), and the dweller's holds only itself (Clearing.reach_centred).” | law (witness) | law 8 (names → declarations; the dweller's reach closure narrowed to the theorem, see above; that the source lies within the clearer's influence closure, from Clearing.reach_middle, written in) |
| C18 “Two formations depending on a condition that nothing exchanges with share a system and neither affects the other (Static.shares_unaffected).” | law (witness) | law 9 (narrowed to the direction the theorem states, see above) |
| C19–C20 “Where every formation takes part in one condition, every system is the whole (…); where every formation depends on it and exchanges with it, every reach closure is (…);” | law | law 10 (names → declarations) |
| C21 “where at one step every formation requires it and gives to it, every feeding closure is (Flow.feeding_whole_of_common), and significance bounded by each center's feeding closure, P40's route without axiom, is the axiom (Flow.feeding_unrestricted_of_common);” | law | law 10 (first clause, with “takes part” written in, see above); law 11 (second clause; “P40's route without axiom” → “the route without axiom of Becoming.Interdependence”, as the theorem's docstring says) |
| C22–C23 “where each center's system is the whole, significance bounded by the system is the axiom (Flow.bounded_system_whole). Clearing is one system (Clearing.clearer_system, Clearing.system_whole).” | law | law 11 (names → declarations) |
| C24 “No premise and no Lean axiom is used;” | premise + standard boundary | law 6 (“With no premise”); standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| C25 “Unrestricted appears here only as a conclusion, that some bounded significance is exactly it.” | scope | law 11 (last sentence, unchanged) |
| L0 “The closures are at the level of formations and not ordered in time, so they are safe upper bounds, not present relations;” | scope | does_not_show[0] |
| L1 “the common condition is Boolean and does not measure the strength of coupling, and Ren's “highly entangled system” is not read as that condition;” | scope + correspondence | does_not_show[1] (first clause); does_not_show[2] (second clause, kind correspondence, Ren's words verbatim) |
| L2 “reading the reach closure as “the system that one is in” is the AI's reading, pending Ren;” | reading | correspondence (R4 says it, under “The author's reading (an AI argument, pending Ren)”); standard_boundaries: names-provisional; next_delta (Ren's judgment) |
| L3 “how a center represents its closure is not modelled;” | scope | does_not_show[3] |
| L4 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Bridge, Becoming.Continuation are bound to consolidated receipt 20261013T221720.428753Z (passed: …)” | evidence | validation_scope; Bridge and Continuation are now bound to 20261014T141427.442103Z (proof_bindings, batch-5 history entry), as the validation scope states; the counts stay in the receipts and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence | validation_scope (“Earlier receipts checked the same statements under former names”); “plan section 10” → snapshot |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 100 theorems of Becoming.Feedback all have empty axiom reports;” | evidence | validation_scope; the count stays in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “The author's counterreview is in §61 of the integration note;” | evidence | validation_scope (“in the integration note”); §61 stays in history (the entry that added the record) and the snapshot |
| V7 “reviewed before integration by the sixteenth independent review (BECOMING-P42-P43-REVIEW.md), whose treatment is in §62.1;” | evidence | validation_scope (“the sixteenth independent review read it before integration”); the review file is the record's `review` reference; §62.1 stays in history (the entry that added the record) and the snapshot |
| V8 “the text after that treatment is not yet independently reviewed.” | evidence | validation_scope |
| V9–V10 “P89 (13 October 2026): prior Bridge declarations remain; four added adapters are checked with empty axiom reports.” | evidence | validation_scope (“the closure adapter of Becoming.Bridge … ha[s] empty axiom reports”); P89, the date and the count → history (existing P89 entry) + snapshot |
| V11–V12 “This record binds Bridge to the new frozen receipt while other proofs retain their original receipts; adapters are not independent results.” | evidence | validation_scope (the Bridge binding; “not an independent result”); proof_bindings |
| R0–R2 Ren's long-term objectives, “pursue the strongest claims and complete proof”, Ren's levels | Ren's words | correspondence (verbatim) |
| R3 “The author's reading (an AI argument, pending Ren): the influence closure reads …;” | reading | correspondence (unchanged) |
| R4 “the reach closure reads Ren's intermediate “the system that one is in” (P40 read the feeding closure as the system one is in; that reading is withdrawn);” | reading | correspondence (parenthesis → “the feeding closure was earlier read as the system one is in; that reading is withdrawn”; zh “P40 把供给闭包读作所在系统，这一读法撤回” → “供给闭包曾被读作所在系统，这一读法已撤回”); P40 → history + snapshot |
| R5–R6 “the system, … bounds every effect but does not read that level: …; “situational awareness” reads as …” | reading | correspondence (unchanged) |
| R7–R8 “The names (…) are the AI's, chosen by Ren's naming standard; trophic cascade is the ecological term.” | names | correspondence (unchanged); standard_boundaries: names-provisional |
| N0 “Closures step by step;” | next step | next_delta (“Give the closures step by step”) |
| N1 “a measure of coupling;” | next step | next_delta (“and a measure of coupling”) |
| N2 “Ren's judgment whether the reach closure reads “the system that one is in”.” | next step | next_delta (“Whether the reach closure reads “the system that one is in” is Ren's to judge.”) |
| H0–H2 | premises | hypotheses[0]–[2] (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |

Remaining lint findings: the correspondence is over its length guide (en 1299/1200, zh 740/500). It quotes Ren's three passages verbatim in both languages (about 320 characters each time), without which it is within the guide; the remaining sentences are attributions of AI readings and names. It is kept rather than moved out of the record.
