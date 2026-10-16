# Migration map: projection-carrying-a-law

Old record sha256 `2d1555429878cb3f4983e35e17ebf22ce2907c0cf66d9a35591ed739d079a933`; snapshot `_process/architecture/history/2d1555429878cb3f/projection-carrying-a-law.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh R0–R1 hold en R0, so later zh correspondence labels run one ahead).

Each law was read against its declarations in `Becoming/Mechanism.lean`, with `FactorsThrough`, `Run.StepsThrough`, `Run.FixesThrough`, `retarget` and `retarget_determined` in `Becoming/Experiment.lean`, `Determined` in `Becoming/Joint.lean`, and `Law.orbit` and `Law.process` in `Becoming/Recurrence.lean`. None states more than the declaration. Law 9 keeps every condition of `Run.not_fixesThrough_of_untaken`: some determined process admits the run's steps before the step read through π, the move untaken at a configuration projecting to k before it, and two different elements of the description. “Likewise where configurations alike go alike” keeps the move untaken and the two elements, as `Run.not_fixesThrough_of_goAlike` does.

Flag (kept as written, not resolved here): `Becoming.Unfolding` now proves `exists_law_iff`. Some determined law admits a whole history exactly where the history is consistent. That holds on the configurations themselves, through the identity, and for every step of the history. The record's next step asks for the iff through a projection π and up to a step along one run, and its limitation says that iff is not stated. Both are kept; whether `exists_law_iff`, applied to the history read through π, answers part of it is for the record's owner.

| Old text | Type | New place |
|---|---|---|
| T0 “A projection carrying a law” | title | title (unchanged) |
| S0–S2 “A projection carries a determined law exactly where configurations alike under it go alike; what the step does not depend on is re-absorbed in one step; a system changing its own rule has its law on the joint configuration.” | statement | statement (unchanged) |
| C0 “Let P be a process on configurations S with moves A, and π : S → K a projection (description) of the configuration.” | framing | law 1 (type names S, A, K left to the Lean statements) |
| C1–C2 “P read through π (Image P π) has a step a from k to κ exactly where …; P's step factors through π into its image (factors_image, with FactorsThrough from P53), and the image is the least process the step factors through (Image.least).” | definition + laws | law 1 (names → declarations; P53 → Becoming.Experiment, where FactorsThrough is declared, as hypothesis 2 says) |
| C3 “Configurations alike under π go alike (GoAlike P π) when …” | definition | law 2 |
| C4–C5 “With no premise: the image is determined exactly where configurations alike go alike (image_determined_iff); some determined process on K admits every step of P read through π exactly where configurations alike go alike (carries_law_iff);” | laws | law 2 (“with no premise” → hypotheses[0], unchanged) |
| C6–C8 “through the identity, going alike is determinacy (goAlike_id_iff); the description that distinguishes nothing always goes alike (goAlike_const); a description ρ of the image goes alike exactly where the composite ρ ∘ π does (goAlike_image_iff).” | laws | law 3 |
| C9 “Where configurations alike go alike, two runs with the same moves … stay alike under π at every step (GoAlike.runs_agree).” | law | law 4 |
| C10 “The next configuration depending only on π (DependsOnlyOn) implies going alike (DependsOnlyOn.goAlike), and two runs … are equal from the first step on (DependsOnlyOn.reabsorbed);” | law | law 5 |
| C11 “a determined law next depends only on π as a process exactly where … (Law.dependsOnlyOn_iff), and then their orbits agree from the next step on (Law.reabsorbed);” | law | law 6 |
| C12 “with the configuration read as (state, rule) and the next configuration depending on the rule and not the state, two configurations with the same rule have the same orbit from the next step on (Law.reabsorbed with the rule as the projection, which is P62's Law.perturbation_reabsorbed, proved in Becoming.Capture as this instance).” | law + provenance | law 6 (second sentence, declaration Law.reabsorbed); the name Law.perturbation_reabsorbed and its proof in Becoming.Capture → related entry target-capture (unchanged); P62 → that related entry and history |
| C13–C14 “In the system changing its own rule, adaptive F G, the state x … becomes F g x u by move u and the rule becomes G g x; it is a determined process on (state, rule) (adaptive_determined);” | definition + law | law 7 |
| C15 “the state's projection goes alike exactly where F agrees for every two rules at every state and move (adaptive_state_law_iff), equivalently where … (adaptive_state_carries_iff);” | law | law 7 |
| C16 “along its runs, on a stretch where the rule stays g, the state's steps are steps of the determined law ruleLaw F g of g (ruleLaw_determined, Run.steps_by_rule).” | law | law 8 |
| C17–C18 “Read through a projection: where the run has not taken a at a configuration projecting to k before some step (Run.TakesThrough), some determined process on K admits the run's steps read through π, and K has two different elements, the record so read fixes no outcome of a at k (…); likewise where configurations alike go alike (Run.not_fixesThrough_of_goAlike).” | law | law 9 (names → declarations) |
| C19 “In Coarse the configuration is two bits, …: the process is not determined (Coarse.not_determined), yet the first bit goes alike (Coarse.goAlike) and the step factors through it into the determined law of flipping (Coarse.carries).” | law (witness) | law 10; counterexamples[0] (unchanged) |
| C20 “In Switching the state becomes the rule and the rule flips at every step: …” | law (witness) | law 11; counterexamples[1] (unchanged) |
| C21 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for the cited modules) |
| L0 “Which projection an actual unfolding carries a law through, that any formation forms or uses a projection, and how a rule comes to change are not derived;” | non-implication | does_not_show[0] (“Does not show …”) |
| L1 “a law means a determined process, and structured undetermined laws and probabilities are not treated;” | scope | does_not_show[1] |
| L2 “the relation to GenerativeCore's exact projection of finite paths (projection_exact_iff) is not stated;” | scope | does_not_show[2]; related entry finite-trace-transport (unchanged) |
| L3 “the state-law criterion adaptive_state_law_iff ranges over all configurations, and the iff along one run is not stated;” | scope | does_not_show[3] (witness adaptive_state_law_iff); see the flag above |
| L4 “systems whose rule update depends on the move are not stated;” | scope | does_not_show[4] (“are not treated”); hypotheses[3] (unchanged) states the premise |
| L5 “the witnesses are minimal;” | scope | does_not_show[7] |
| L6 “the main theorems are near-definitional, the delta being the characterization and the least candidate;” | scope | does_not_show[5] |
| L7 “the reading of mechanism takes only the aspect “a law at a description” of the philosophy-of-science notion;” | scope of the reading | does_not_show[6] (kind correspondence) |
| L8 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “Readings (the AI's, pending Ren)” |
| L9 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Mechanism, Becoming.Joint are bound to consolidated receipt 20261013T221720.428753Z (passed: …; the 90-module core closure compiles from the prelude).” | evidence | validation_scope (the binding receipt); the counts stay in the receipt and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | snapshot; the rename table stays in the plan, and the history entry on the renames names it |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 30 theorems of Becoming.Mechanism all have empty axiom reports, among them …;” | evidence | validation_scope (the theorems of Becoming.Mechanism, receipt 20261013T094743.528770Z, which also binds Becoming.Experiment and Becoming.Recurrence); the count and the list stay in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules … and 22 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + snapshot (the record cites no peripheral declaration) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “The author's counterreview is in §88 of the integration note;” | evidence | validation_scope (“in the integration note”); §88 is in the first history entry |
| V7 “there is no independent review yet.” | evidence | validation_scope |
| R0 “On 12 October 2026 Ren asked “hows cause–effect system comparing to our theory?”, pasted an explanation whose author is not stated (not Ren's wording, not a premise), asked “…”, and to the AI's five proposals answered “…”.” | Ren's words | correspondence (verbatim) |
| R1 “This is the third proposal (a mechanism is a factoring, not a further kind of law), work-board item P66.” | provenance + round label | correspondence (first clause); P66 → history (first entry, existing) |
| R2 “Readings (the AI's, pending Ren): a mechanism is a projection that carries a law, and P53's model of what is irrelevant is characterized exactly by going alike;” | reading | correspondence (P53 → “(Becoming.Experiment)”) |
| R3–R4 “a projection of configuration is a third thing …; a law at a coarser description (emergence) is going alike there, …” | reading | correspondence (unchanged) |
| R5 “the rule holding the outcome (P62's B5) is dependence on the rule only;” | reading | correspondence (P62's B5 → “(Becoming.Capture)”) |
| R6 “a system that changes its own causality has its law on the joint configuration …” | reading | correspondence (unchanged) |
| R7 “on §72's reading of 理 as a projection, this says when 理 carries a law.” | reading | correspondence (“reading 理 as a projection (Becoming.Experiment), this says when 理 carries a law”; §72 is the integration note's section on Becoming.Experiment) |
| R8 “See §88 of the integration note.” | provenance | history (first entry, existing: “see §88 of the integration note”) |
| N0 “The iff along one run: some determined process admits the steps read through π up to a step exactly where two steps alike under π with the same move reach configurations alike under π (constructive);” | next step | next_delta (first sentence; see the flag above) |
| N1 “the instance with Becoming.Testing's registration as the projection (when an experiment through any projection is right is now given by P73's transfer_right_iff);” | next step + completed connection | next_delta (“The instance with Becoming.Testing's registration as the projection”); the parenthesis is a completed connection held by the existing P73 history entry (transfer_right_iff, generalization-through-lumping); related entry testing-within-registration (unchanged) |
| N2 “the bridge to GenerativeCore's exact projection;” | next step | next_delta |
| N3 “the state's law over long stretches where the rule changes slowly.” | next step | next_delta |
| H0 | premise | hypotheses[0] (unchanged) |
| H1 “A law is a determined process (Joint.Determined); carrying means the step factors through the projection into it (FactorsThrough, P53).” | premise | hypotheses[1] (“P53” → “from Becoming.Experiment”; meaning unchanged) |
| H2–H5 | premises | hypotheses[2]–[5] (unchanged) |
| X0–X2 | counterexamples | counterexamples[0]–[2] (unchanged) |
