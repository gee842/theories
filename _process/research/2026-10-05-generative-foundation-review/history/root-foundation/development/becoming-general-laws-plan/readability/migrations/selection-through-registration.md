# Migration map: selection-through-registration

Old record sha256 `fd2401d67871101a248fc5263054ef4302584c4289fdbac4bb16b1d145bf1969`; snapshot `_process/architecture/history/fd2401d67871101a/selection-through-registration.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Selection.lean` and, for the responsive form, `Flow.alike_within_registration` in `Becoming/Testing.lean` (bytes bound by the record's references). Law 7 writes in the balance of both flows on the registered conditions (`balanced`, `balanced'`), which the old text named only as “the hypotheses of alike_within_registration”; law 3 says “the level of an observed condition at such a step”, as `Web.observed_scores` takes `s ≤ t`. No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Selection through registration” | title | title (unchanged) |
| S0–S1 “Every selection through a registration selects two histories alike exactly when they register alike. With the rest fixed, selection is blind …; pooled registration selects …, and a flow reaching beyond to raise what registers is selected.” | statement | statement (unchanged) |
| C0 “Let W be a web, obs an observation, g a formation and t a step.” | notation | dropped as notation: the laws say “a formation” and “a step” |
| C1–C3 “A selection is any claim select about level histories; it goes through g's registration up to t when … (Web.SelectsThrough); a score goes through it when they score alike (Web.ScoresThrough).” | definition | law 1 |
| C4 “Registering alike is transitive, so an equivalence (Web.RegistersAlike.trans, Web.RegistersAlikeUpTo.trans).” | law | law 1 |
| C5 “With no premise, two histories l, l' are selected alike by every selection through g's registration exactly when g registers them alike up to t (Web.selects_alike_iff);” | law | law 2 |
| C6 “g's belief (Web.Belief) is such a selection (Web.belief_selects), so where g registers them apart … (Web.separates).” | law | law 2 |
| C7 “A selection through registration is refuted by its selector exactly where it fails (Web.SelectsThrough.refutes_iff);” | law | law 3 (Web.Refutes among the declarations) |
| C8 “admission at a step up to t is a selection through registration, the level of an observed condition a score through it, and a score's threshold a selection through it (…);” | law | law 3 (“at such a step” written in, see above) |
| C9 “going through registration survives later steps, more observation, negation and conjunction (…).” | law | law 3 |
| C10 “Where registering alike with l is decidable (the named hypothesis decided), l and l' are scored alike … (Web.scores_alike_iff).” | law | law 4 (“with l” → “with the first history”); the hypothesis name stays in hypotheses[3] |
| C11–C13 “For a group, histories every member registers alike are selected alike (Web.SelectsThroughAll); the same equivalence holds (…); a member's selection is a group selection, and group selections are closed under conjunction (…).” | law | law 5 (“the same equivalence and separation hold”, as the cited separates_all says) |
| C14 “Blindness beyond the registration closure: under the conditions of unregistered_beyond_registration (…), every selection and every score … treats W.level and l alike (…), and so does every group whose members lie within the closure (…);” | law | law 6 (the conditions in the parenthesis written into the law; “W.level and l” → “the levels with and without the part”) |
| C15 “under the hypotheses of alike_within_registration (the same formations present in both flows, the same start on what is registered, members responding only through their own registration), every selection … selects the two flows' levels alike (Flow.unselected_beyond_registration_responsive).” | law | law 7 (both flows' balance written in, see above) |
| C16 “Share among descendants (an application): where select holds for the history of every parent in ms and for none in es, … (share_rises_through, that is share_rises).” | law | law 8 (“ms”, “es” → “one non-empty list”, “another”) |
| C17 “Witness Clearing: every selection through the clearer's registration (support only) selects the cleared and the spared world alike … (Clearing.unselected);” | law (witness) | law 9; counterexamples[0] (unchanged) |
| C18 “the dweller lies within the clearer's reach closure and beyond its registration closure, and the clearer does not register the habitat (Clearing.dweller_within_reach);” | law (witness) | law 9 |
| C19 “the dweller's admission at the third step goes through the dweller's registration and separates the two worlds (Clearing.selected_by_dweller);” | law (witness) | law 10 |
| C20 “both being admitted at the third step goes through the pooled registration of the two, separates the worlds, and goes through neither registration alone (Clearing.selected_pooled).” | law (witness) | law 10; counterexamples[1] (unchanged) |
| C21–C22 “Witness Diversion: the diverting flow takes a unit from the source … reaching the dweller beyond the registration closure; that the store stands at least one at the second step goes through the taker's registration, holds in the diverting flow and fails in the undiverted one;” | law (witness) | law 11 |
| C23 “the dweller is unsupported from the second step on in the diverting flow and supported at every step in the undiverted one (Diversion.favours);” | law (witness) | law 12 |
| C24 “every selection through the taker's registration selects the diverting flow alike with a supplying flow that only gives to the store and reaches nothing beyond (Diversion.blind_to_source).” | law (witness) | law 12; counterexamples[2] (unchanged) |
| C25 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for Becoming.Selection) |
| L0 “Who selects, what the selector registers, whether an actual selection goes through registration, whether offspring follow the selection, and whether reaching beyond is chosen are not derived” | non-implication | does_not_show[0] (“The laws do not derive …”) |
| L1 “the more is registered, the larger the registration closure and the smaller the gap, so the law's force lies entirely in what the selector actually registers” | scope | does_not_show[1] |
| L2 “the main law is near-definitional and the blindness is a one-line corollary of P49's theorems, so the delta is conceptual” | scope | does_not_show[2] (“P49's theorems” → “the theorems of testing-within-registration”, the dependency that holds them; “the delta” → “the contribution”) |
| L3 “the gap for one's own act (…) has no separate general theorem, and in Clearing comes from an instance of alike_within_closed” | scope | does_not_show[3] |
| L4 “favouring reaching beyond is stated only in the minimal witness Diversion” | scope | does_not_show[4], witness Diversion.favours |
| L5 “share_rises_through is an application, and its combination with transmission and an open world is a reading” | scope | does_not_show[5] |
| L6 “where others respond to the stock a selection rests on, the response hypotheses can fail” | scope | does_not_show[5] |
| L7 “the readings are the AI's, pending Ren” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “Readings (the AI's, pending Ren)” |
| L8 “contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Capture, Becoming.Selection are bound to consolidated receipt 20261013T204910.042715Z (passed: …; the 86-module core closure compiles from the prelude).” | evidence | validation_scope (the binding receipt); the counts stay in the receipt and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | snapshot; the rename table stays in the plan |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 43 theorems of Becoming.Selection all have empty axiom reports, among them …;” | evidence | validation_scope (the theorems of Becoming.Selection, receipt 20261013T094743.528770Z); the count and the list stay in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules …;” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration) |
| V5–V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V7 “The author's counterreview is in §86 of the integration note;” | evidence | validation_scope (“in the integration note”); §86 is in the correspondence |
| V8 “there is no independent review yet.” | evidence | validation_scope |
| (proof bindings) | evidence | validation_scope also names Testing's binding receipt 20261014T091930.724493Z, already in the references and proof bindings |
| R0 “On 12 October 2026 Ren asked “hows cause–effect system comparing to our theory?” and pasted an explanation of causal systems whose author is not stated (…); after the AI's comparison and its five proposals, Ren wrote “…”.” | provenance + Ren's words | correspondence (Ren's words verbatim; “whose author is not stated” → “of unstated authorship”) |
| R1 “This record is the first of them (P64); the five proposals are the AI's.” | provenance | correspondence (“This record is the first of them”; that the proposals are the AI's is said by “the AI's comparison and its five proposals”, zh unchanged); P64 is in the first history note |
| R2–R5 “Readings (the AI's, pending Ren): any selection decided by what a selector registers … reaches exactly what that selector registers, and is blind …; the gap …; where reaching beyond raises what registers …; read for AI training, …” | reading | correspondence (condensed wording, same content) |
| R6 “The AI connects this with the title of Ren's paper “When Capability Outruns Correction”; the connection is the AI's.” | reading | correspondence (“The AI, on its own account, connects …”) |
| R7 “See §86 of the integration note.” | provenance | correspondence (unchanged) |
| N0 “The gap for one's own act as a general theorem: …;” | next step | next_delta |
| N1 “a general form of favouring reaching beyond: when a part raising what registers must reach beyond the registration closure;” | next step | next_delta (“favouring reaching beyond in general”) |
| N2 “combined with transmission, descent and openness (Capture's descent_needs_unrun), the rise of the share of what reaches beyond;” | next step | next_delta |
| N3 “P93 now supplies choice preservation/loss under changing registration and a local executed reconstruction;” | completed connection | history (the migration note); the related link selection-under-registration-revision (unchanged) says the same |
| N4 “P99/P103 further join consequence-driven reference-construction methods, acquired candidates, actual observation/use and supported recurring revision.” | completed connection | history (the migration note) and the P99/P103 history notes |
| N5 “Formation of arbitrary physical primitives and more general rule-changing capture retain their own scope.” | scope | does_not_show[6] |
| H0 “That a selection goes through registration … is a supplied condition …” | premise | hypotheses[0] (unchanged) |
| H1 (first sentence) “Blindness beyond the registration closure further assumes the conditions of unregistered_beyond_registration: …” | premise | hypotheses[1] (unchanged) |
| H1 (second sentence) “The responsive form assumes the hypotheses of alike_within_registration: …” | premise | hypotheses[2] (both flows' balance written in) |
| H2 “The converse of the law for scores takes the decidability … (decided); the law for selections needs no decision.” | premise | hypotheses[3] (unchanged) |
| H3 “share_rises_through: the parents' histories, …; transmission is not part of it.” | premise | hypotheses[4] (unchanged) |
| H4 “For the witnesses: Clearing's flows and webs (P40, P42, P49), and Diversion's three flows and webs.” | premise | hypotheses[5] (P40, P42, P49 → “from the modules of feeding closure, feedback and testing”) |
| H5 “Discrete steps, counted from step 0; natural-number levels, needs and amounts.” | premise | hypotheses[6] (unchanged) |
| X0–X2 | counterexamples | counterexamples[0]–[2] (unchanged) |
