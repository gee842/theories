# Migration map: feeding-closure

Old record sha256 `e62a92e786475ad00e2d45d7680275ec25b227970c9dcb8a65568da4a543c4dd`; snapshot `_process/architecture/history/e62a92e786475ad0/feeding-closure.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C17 holds en C17–C18, so zh C18 is en C19; zh L0 holds en L0–L1, so later zh limitation labels run one behind, and zh L6–L7 hold en L7; zh V11 holds en V11–V12; zh H4.3 holds en H4.3–H4.4).

Each law was read against its declarations in `Becoming/Interdependence.lean`, `Becoming/Feeding.lean` and `Becoming/Standpoints.lean` (for `Flow.FedBy`). Two laws are narrower in wording than the old text, to match the theorems. C4 said a formation beyond the closure “gives nothing, at any step”; `Flow.beyond_gives_nothing` asks that formation to take part at the step (`present : h ∈ L.present t`), and law 3 says so. C14 said the same of the closure across steps; `Flow.beyond_gives_nothing_across` also asks it (`present : h ∈ L.present s`), and law 10 says so. In the model a formation not taking part at a step contributes nothing to what is given there (`Flow.given` sums over `L.present t`), so the statement's “nothing beyond it gives” is kept. Law 6 adds the definitions the old text named only (`Flow.FollowsGiven`, `Flow.carriedTo_of_le`), in the words of their docstrings. Law 7 states the depletion law that C17 summarized (`Flow.depleted_keeps_nothing`: no following keeps any of what is given standing). No law states more than its declaration.

| Old text | Type | New place |
|---|---|---|
| T0 “The feeding closure” | title | title (unchanged) |
| S0–S2 “What a continuation depends on is the least region holding it that is closed under feeding; … each formation's feeding closure.” | statement | statement (unchanged) |
| C0 “The continuation of a formation is fed by another at a step (Flow.FedBy) when …” | definition | law 1 (name → declarations) |
| C1–C2 “A region of formations is closed under feeding (Flow.FedClosed) …; g lies within f's feeding closure (Flow.WithinFeeding) when …” | definitions | law 1 (names → declarations) |
| C3 “The closure holds f (…refl), is transitive (…trans), holds every feeder of f at any step (…of_fedBy) and is itself closed under feeding (Flow.fedClosed_within), so it is the least region …” | law | law 2 (names → declarations) |
| C4 “A formation beyond the closure gives nothing, at any step, to a condition a member then requires (Flow.beyond_gives_nothing).” | law | law 3 (narrowed to the theorem: the formation takes part at the step; see above) |
| C5 “In Clearing the region along dependence (Clearing.dependenceRegion: …) is closed under feeding and holds its formation (…), and is exactly each formation's feeding closure (Clearing.dependenceRegion_iff).” | law (witness) | law 4 (names → declarations) |
| C6–C7 “The dweller lies beyond the clearer's closure (Clearing.dweller_beyond); everything within that closure is supported …, while the dweller is unsupported from step 2 on (Clearing.closure_supported).” | law (witness) | law 5 (names → declarations) |
| C8 “No premise and no Lean axiom is used.” | premise + standard boundary | law 2 (“With no premise”) and the statement (“reached with no premise”); standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| C9 “P86 adds the across-step form: Flow.CarriedTo requires balance on the condition over the stretch and positive standing after giving through the required step.” | definition | law 6 (written out from the definition); P86 → history (existing entries) + snapshot |
| C10 “Some nonincreasing following of a positive amount given can remain positive exactly where all those intermediate levels are positive (Flow.can_stand_iff, Flow.carriedTo_iff_stands).” | law | law 7 (with the conditions of the two theorems: s < t, and for carrying a positive amount given and balance across the stretch) |
| C11–C12 “Flow.FedAcross links giving no later than the need through this carrying relation; Flow.fedBy_iff_fedAcross makes same-step feeding its zero-delay case.” | definition + law | law 9 |
| C13–C14 “Flow.WithinFeedingAcross is the least region …; it contains the original closure (Flow.WithinFeeding.across), and nothing beyond it gives to a condition carried to a member’s need (Flow.beyond_gives_nothing_across).” | law | law 10 (narrowed to the theorem: the formation takes part at the step of giving; see above) |
| C15 “If nothing given stands after its step, the closures agree (Flow.withinFeedingAcross_iff_of_unheld);” | law | law 11 (first sentence) |
| C16 “Provision.through_store shows strict inclusion when a parent at step 0 feeds a young active at step 2 through storage.” | law (witness) | law 11 (second sentence, with the conjuncts of Provision.through_store) |
| C17 “An exhausted intermediate step rules carrying out;” | law | law 7 (last sentence, Flow.depleted_keeps_nothing) |
| C18 “giving more than the stretch’s total taking suffices.” | law | law 8 (Flow.carried_of_given_exceeds, with its conditions) |
| C19 “The actual attribution of origin is not fixed.” | non-implication | does_not_show[2] |
| L0 “The original same-step closure and P42 hierarchy retain their scope;” | scope | does_not_show[0] (“The levels of closure (levels-of-closure) are stated for same-step feeding”); P42 → history + snapshot |
| L1 “P86 does not show that the across-step closure lies within the same-step influence closure.” | non-implication | does_not_show[0] |
| L2 “It remains a formation-level closure: each link has a temporal direction, but the whole chain is not an event path joined in temporal order.” | scope | does_not_show[1] |
| L3 “Quantities have no origin marks: a possible retained following does not establish actual retention of that amount.” | non-implication | does_not_show[2] |
| L4 “Carrying however taking is attributed has a sufficient condition only, no exact iff.” | converse | does_not_show[3], witness Flow.carried_of_given_exceeds |
| L5 “A center’s formation or representation of the closure is not modeled.” | scope | does_not_show[4] |
| L6 “No ethical predicate or ought follows;” | standard boundary + non-implication | standard_boundaries: no-evaluation; does_not_show[5] (“No ought follows.”) |
| L7 “readings remain the AI’s, pending Ren, and P42’s withdrawn system reading is not restored.” | reading | standard_boundaries: names-provisional; correspondence (“The author's reading (an AI argument, pending Ren)” and its last clause, “it does not restore the withdrawn system reading”) |
| V0 “14 October 2026: the current bytes of Becoming.Feeding, Becoming.Continuation are bound to consolidated receipt 20261013T221720.428753Z (passed: …)” | evidence | validation_scope (the Feeding binding); Continuation is now bound to 20261014T141427.442103Z (proof_bindings, batch-5 history entry), as the validation scope states; the counts stay in the receipts and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence | validation_scope (“Earlier receipts checked the same statements under former names”); “plan section 10” → snapshot |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 30 theorems of Becoming.Interdependence all have empty axiom reports;” | evidence | validation_scope; the count stays in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “The author's counterreview is in §56 of the integration note;” | evidence | validation_scope (“in the integration note”); §56 stays in history (the entry that added the record) and the snapshot |
| V7 “not yet independently reviewed.” | evidence | validation_scope |
| V8 “P86 checked addition: core receipt 20261013T094743.528770Z checks Becoming.Feeding’s 41 theorems …” | evidence | validation_scope (Becoming.Feeding's theorems, with the binding of its current bytes); P86 and the count → history + snapshot |
| V9 “periphery 20261013T095049.338744Z passes;” | evidence (duplicate of V4) | as V4 |
| V10 “study §107.” | provenance | history (the P86 entry names study §107) + snapshot |
| V11 “Historical scope is retained;” | evidence | validation_scope (“Earlier receipts checked the same statements under former names”) and the snapshot |
| V12 “the integration text has no independent review yet.” | evidence (duplicate of V7) | validation_scope |
| R0 Route (b) and Ren's two quotations | Ren's words | correspondence (verbatim) |
| R1 “The author's reading (an AI argument, pending Ren): the feeding closure reads “what it actually depends on”.” | reading | correspondence (unchanged) |
| R2 “P40 also read it as Ren's “the system that one is in”, …;” | reading | correspondence (“P40 also read it” → “It was also read”; zh “P40 也把它读作” → “它也曾被读作”); P40 → history + snapshot |
| R3 “P42 withdraws that reading: …” | reading | correspondence (“P42 withdraws that reading” → “that reading is withdrawn”; zh “这一读法由 P42 撤回” → “这一读法已撤回”); P42 → history + snapshot |
| R4 “The names (FedClosed, WithinFeeding, Overshoot and others) are the AI's, chosen by Ren's naming standard.” | names | correspondence (unchanged); standard_boundaries: names-provisional |
| R5 “P86 reads earlier giving possibly retained through a condition as feeding across steps;” | reading | correspondence (“P86 reads … as” → “… is read as”); P86 → history + snapshot |
| R6 “quantities bear no origin marks, so this does not identify actual origin or derive a center’s recognition.” | reading | correspondence (with L7's last clause appended) |
| N0 “What additional relation fixes the actual following of an amount given;” | next step | next_delta (“Give the relation that fixes the actual following of an amount given”) |
| N1 “an exact criterion for carrying however taking is attributed;” | next step | next_delta (“and an exact criterion for carrying however the taking is attributed”) |
| N2 “an event closure joined in temporal order;” | next step | next_delta (“join the dependence closure as events in temporal order”, following the zh “按事件与时间相接的依存闭包”) |
| N3 “how a center forms and represents its closure;” | next step | next_delta (“model how a center forms and represents its closure”) |
| N4 “Ren’s judgment of the across-step feeding reading.” | next step | next_delta (“The across-step feeding reading is Ren's to judge.”) |
| H0.0 “The original Flow.FedBy counts giving at a common step;” | premise | hypotheses[0] (“The original” dropped; zh “原” dropped) |
| H0.1 “P86 Flow.FedAcross includes earlier giving …” | premise | hypotheses[0] (the round label “P86” (zh “P86 的”) dropped and kept in history and the snapshot; wording otherwise unchanged) |
| H1–H4 | premises | hypotheses[1]–[4] (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |

Remaining lint finding: the Chinese correspondence is over its length guide (zh 625/500). It quotes Ren's English passages verbatim (about 280 characters), and the remaining sentences are attributions of AI readings. They are kept rather than moved out of the record.
