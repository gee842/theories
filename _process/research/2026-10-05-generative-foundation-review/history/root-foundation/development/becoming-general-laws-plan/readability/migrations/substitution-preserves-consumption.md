# Migration map: substitution-preserves-consumption

Old record sha256 `7c8df7d8b161c39ef3c74ea52a2d95bdc909977275eabc7082cc37881101d2a6`; snapshot `_process/architecture/history/7c8df7d8b161c39e/substitution-preserves-consumption.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0 “Substitution preserves consumption on the whole-run reading: a consumer that can substitute a condition persists by transforming its dependence and still consumes over the run” | title (statement of the result) | title (short name: the part before the colon) + statement |
| C0 “For every web, consumption is kept under every change of the consumer's own dependence from a step T₀ on (…) exactly when … (Web.consumingIn_kept_iff);” | law | law 1 |
| C1 “for a change from the start, exactly when another formation's dependence witnesses it (Web.consuming_survives_iff).” | law | law 2 |
| C2 “Where only the consumer's own dependence witnesses the loss, dissolving it removes the consumption (Lone.own_witness_lost).” | law (witness) | law 2 |
| C3 “And where activity needs support, a formation still active after a loss without return has weakened or dissolved its dependence on the condition (Web.consumed_continues_transformed).” | law | law 3 |
| C4 “So on the whole-run reading a consumer that persists by transforming its dependence still consumes exactly where the loss falls on a dependence other than the one it transforms.” | conclusion | statement |
| C5 “RelationalRenewal's support-gated law is an instance: … (consuming_through_sustaining).” | instance | law 4; statement (“of which the support-gated law … is an instance”) |
| C6–C7 “In the family, let the focal formation depend on the shared condition while it supports the focal formation and otherwise on an alternative that does, …; the shared condition's levels are still given by the law.” | setting (definition) | law 5 |
| C8–C11 “If the focal formation draws beyond renewal from the start, then it is active at every step; its dependence … dissolves …; it is consuming in the run …; and the sustaining formation loses support for ever from some step and ends.” | law | law 6 (persists_consuming) |
| C12–C13 “A concrete law (extracting) meets every premise; in it the stepwise reading credits the focal formation at every step except step 2, …” | instance | law 7 |
| C14a “In another law (slow) the shared condition still supports the focal formation for a step after it fails the sustaining formation, and the focal formation is withheld at steps 2 and 3:” | instance | law 8 |
| C14b “what is withheld are the steps after the sustaining formation loses support and before the focal formation switches (in general an argument, not formalized).” | scope | does_not_show[1] |
| C15 “With a decidable determination, the step at which it ceases can be found.” | law | law 9 (ceasing_step, with ceases_at_a_step, of which it is the decidable form) |
| C16 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (hypotheses hold no ethical premise; the receipt reports empty axioms for Becoming.Substitution) |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation (the module evaluates neither arising nor ceasing) |
| L1 “preservation holds on the whole-run reading only;” | scope | does_not_show[0], witness stepwise_credits_substitution |
| L2 “for every web it holds only where the loss is witnessed by a dependence the change leaves;” | converse (restated law) | law 1 (the “only if” half of its iff) and law 2 (Lone) |
| L3 “persistence by substitution, its timing and the sustaining formation's ending are proved in the support-gated law;” | scope | does_not_show[2] |
| L4 “the alternative's level is constant and its cost unmodelled;” | premise (duplicate of H2) | hypotheses[1] |
| L5 “the individuation of formations is not treated (…identity-across-steps).” | scope | does_not_show[3] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): all 12 theorems of Becoming.Substitution have empty axiom reports;” | evidence | validation_scope |
| V1 “the same receipt covers the package's 91 modules … 4983 theorems/7020 declaration audits, and 39 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §8.6 of the integration note;” | evidence | validation_scope (“in the integration note”; §8.6 → snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-P7-REVIEW.md), and its corrections are handled in §11;” | evidence (review) | validation_scope (second independent review, listed under sources; it accepted the mathematics, as counterexamples[2] says); reviewer identity and §11 → review file + snapshot |
| V4 “a third independent review (BECOMING-P8-P9-P7B-REVIEW.md) scoped “withheld at one step only” to extracting, corrected in §12.” | evidence (review) | validation_scope; §12 → snapshot |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details in the receipt and the snapshot |
| V6 “The law of kept consumption, its instance and the Lone counterexample, added on 14 October 2026 (5 theorems; Becoming.Substitution now has 12), are checked in consolidated receipt …” | evidence + round narration | validation_scope (among the 12 theorems); the date and the count of 5 are in the L2 history note and the snapshot |
| R0–R2 | correspondence | correspondence (unchanged) |
| N0 “That the chain of substitutions ends when the alternatives cost and none is renewed is proved in unceasing-generation-needs-renewal;” | another record's result | related unceasing-generation-needs-renewal (its detail says the same) + snapshot |
| N1 “whether consumption moves elsewhere when alternatives are renewed, and the same preservation for general laws with changing dependence, remain open.” | next step | next_delta (“remain open” dropped: the status field and the field itself say it) |
| H0, H1–H2 | premises | hypotheses (unchanged) |
| X0, X1, X3 | counterexamples | counterexamples[0], [1], [3] (unchanged) |
| X2 “Second independent review: the mathematics of P7 is accepted; … the §8.5 table … (corrected, integration note §11).” | counterexample (review summary) | counterexamples[2] (same rewrite as in joint-difference-making) |
| X4 “Third independent review: every P8, P9 and P7b declaration is accepted …; … (corrected, integration note §12).” | counterexample (review summary) | counterexamples[4] (same rewrite as in joint-difference-making) |
