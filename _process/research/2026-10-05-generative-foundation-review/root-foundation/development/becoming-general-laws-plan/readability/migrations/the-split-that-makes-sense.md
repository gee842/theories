# Migration map: the-split-that-makes-sense

Old record sha256 `f8f654707fd426b847912e916cdb8bbbd946bb92d6339293c1f608602c2e898f`; snapshot `_process/architecture/history/f8f654707fd426b8/the-split-that-makes-sense.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C0 holds en C0–C1, so zh claim labels run one behind until zh C12–C14, which hold en C13, after which they run one ahead).

Each law was read against its declarations in `Becoming/Description.lean`, with `Alike`, `Bisimulation`, `IdentifiesAlike`, `identifiesAlike_iff`, `identifiesAlike_id_iff`, `Law.registered`, `Law.SameFuture` and `Law.alike_iff_sameFuture` in `Becoming/Unfolding.lean`, `GoAlike`, `adaptive` and `adaptive_state_law_iff` in `Becoming/Mechanism.lean`, `Law.orbit` and `Law.Returns` in `Becoming/Recurrence.lean`, `Diagonal.revision_never_rests` and `Diagonal.flip_moves` in `Becoming/Diagonal.lean`, and `Learning.goAlike_iff_lumped` and `Learning.Lasso` in `Becoming/Learning.lean`. None states more than the declaration. `Law.identifiesAlike_of_law` keeps its three conditions (keeping what is registered, going alike, coarsest) and `Law.Returns.states` its returning configuration, as hypotheses[1] says. Symbolic forms are written in words where the statement says the same: `∀ x c c′, (next (x, c)).1 = (next (x, c′)).1` as “the rest makes no difference to its next value” (the statement's wording), `o = id` as “registering everything”, and `Learning.Lasso o i q` as “Learning's lasso from moment i with period q + 1”.

| Old text | Type | New place |
|---|---|---|
| T0 “The split that makes sense, and states read off a history” | title | title (unchanged) |
| S0–S1 | statement | statement (unchanged) |
| C0 “With P69's definitions: a determined law next read through a registration o is the frame Law.registered next o;” | definition + work-item label | law 1 (P69 → Becoming.Unfolding, where these definitions are) |
| C1 “a description π makes sense (IdentifiesAlike) when it identifies exactly the alike configurations, and alike is the same registered future (Law.alike_iff_sameFuture).” | definition | law 1 |
| C2–C3 “Under a determined law, π goes alike with the law exactly where …; a split keeping what is registered and going alike relates configurations by a bisimulation (…), loses nothing registered (…), and the coarsest such split makes sense (…).” | laws | law 2 |
| C4–C5 “The split lumping everything makes sense exactly where …; registering everything (o = id), the configuration itself makes sense (…).” | laws | law 3 |
| C6 “What is registered now, o, makes sense by itself exactly where … (Law.sameFuture_of_goAlike, Law.now_identifiesAlike_iff_goAlike).” | laws | law 4 |
| C7–C8 “For a law on X × C registering the first part, …; where the next value is set by a rule changing with it (…), exactly where ∀ x c c′, F c x = F c′ x (…), the condition of adaptive_state_law_iff of Becoming.Mechanism.” | laws | law 5 (“pairs (x, c)” for X × C) |
| C9–C11 “Motion.move (x, v) = (x + v, v) is an adaptive process (…); registering x, the pair makes sense (…), …; under the still law x alone makes sense (…).” | laws (witness) | law 6; counterexamples[0] (unchanged) |
| C12 “In a registered sequence o : ℕ → O, moments t and t′ are one state (SameAhead o t t′) when ∀ n, o (t + n) = o (t′ + n);” | definition | law 7 |
| C13 “this is an equivalence that goes on as itself (…), is the same registered future read along an orbit (…), and where every moment is registered differently each moment is its own state (…).” | laws | law 7 |
| C14 “Under the law of moments Law.registered Nat.succ o, t and t′ are alike exactly where SameAhead o t t′ (alike_moments_iff).” | law | law 8 (with the statement's “every registered history is a determined law read through a registration”, as the declaration's docstring says) |
| C15 “A pigeonhole up to a relation with no decision (split_top, shared_below) gives: o has finitely many states (…, StatesBelow) exactly where SameAhead o i j for some i < j (…);” | laws | law 9 |
| C16 “a configuration that returns has finitely many states under every registration (Law.Returns.states).” | law | law 9 |
| C17 “The registration of the two-valued negation (Negation.register) has exactly two states: …” | law (witness) | law 10 |
| C18 “Law.goAlike_process_iff is the instance of Becoming.Learning's goAlike_iff_lumped;” | law | law 11 (with R5's “written independently, with the same proof”) |
| C19 “Learning.Lasso o i q holds exactly where SameAhead o i (i + (q + 1)) (…), so there are finitely many states exactly where there is a lasso (…).” | laws | law 11 |
| C20 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| L0 “Only determined laws are stated;” | scope | hypotheses[3] (which says the same; its work-item label P69 is now Becoming.Unfolding) |
| L1 “that a description making sense exists as values is not stated (naming in general needs a quotient, Quot.sound);” | scope | does_not_show[0]; hypotheses[4] (unchanged) |
| L2 “whether a finite record fixes the states is not stated here (P73);” | scope + work-item label | does_not_show[1] (P73 → “see Becoming.Learning”, its module) |
| L3 “in alike_moments_iff the determinacy of the law of moments is trivial, the content being that likeness is being one state;” | scope | does_not_show[2] (witness alike_moments_iff) |
| L4 “it is not stated that any actual unfolding has finitely many states;” | non-implication | does_not_show[3] |
| L5 “the readings are the AI's;” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “Readings (the AI's, pending Ren; …)” |
| L6 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Description, Becoming.Diagonal, Becoming.Mechanism, Becoming.Unfolding are bound to consolidated receipt 20261013T204910.042715Z (passed: …).” | evidence | validation_scope (the binding receipt, without the date; counts in the receipt and the snapshot) |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | validation_scope (“which checked them under the current names”); the renames are in history entry 18 |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 53 theorems of Becoming.Description …” | evidence | validation_scope (20261013T094743.528770Z binds Becoming.Recurrence and Becoming.Learning, as the proof bindings have it); the count and the list stay in the receipt and the snapshot |
| V3–V4 counts and periphery receipt | evidence | receipt + snapshot |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the detail stays in the receipt and the snapshot |
| V6 “The author's counterreview is in §94 of the integration note, with the scope of the independent review.” | evidence | validation_scope (“in the integration note, which also states the scope of the independent review”); §94 is in history entry 0 |
| R0 “The second part of P70 (work board), answering Ren's “…” and “…”: relative to what is registered, the split that makes sense is unique and given by the law;” | Ren's words + reading | correspondence (“Answering Ren's …”, verbatim); P70 is in history entry 0 |
| R1–R4 | Ren's words + reading | correspondence (unchanged) |
| R5 “P73 landed first, so the identities are stated here: Law.goAlike_process_iff is the instance of Becoming.Learning's goAlike_iff_lumped (written independently, with the same proof), and finitely many states is P73's lasso.” | law (restated) + provenance | law 11 (the two identities, with “written independently with the same proof”); the order of landing → snapshot |
| R6 “The one-step forms come from the review by P66's owner.” | provenance | correspondence (“by the owner of Becoming.Mechanism”, the module of that work item) |
| R7–R8 readings | reading | correspondence (unchanged) |
| R9 “See §94 of the integration note.” | provenance | history entry 0 (existing: “see §94 of the integration note”) |
| N0–N2 | next steps | next_delta (unchanged) |
| H0–H2, H4 | premises | hypotheses[0]–[2], [4] (unchanged) |
| H3 “Only determined laws are stated; frames that branch are stated by P69's Alike.” | premise + work-item label | hypotheses[3] (“Becoming.Unfolding's Alike”) |
| X0 | counterexample | counterexamples[0] (unchanged) |
