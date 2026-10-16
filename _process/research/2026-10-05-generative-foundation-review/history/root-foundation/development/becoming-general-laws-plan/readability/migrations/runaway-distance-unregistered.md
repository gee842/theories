# Migration map: runaway-distance-unregistered

Old record sha256 `612f374f274312a228ca2c34754bc473d3771b7844f604657fd3b7f169a848c9`; snapshot `_process/architecture/history/612f374f274312a2/runaway-distance-unregistered.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Runaway.lean` (with `Flow.ExchangeFollows` and the registration definitions in `Testing.lean`, `Web.Supported` and `Web.Dependent` in `Dependence.lean`, `Flow.BalancesOn` in `Flow.lean`; bytes bound by the record's references). Two places were rewritten against the Lean. Law 2 says “the same formations present”: `policy_keeps_difference` takes `present`, which the old claim set only in the sentence before. Law 6: `break_not_bounded` states `∃ d`, some raise of c; the raise by the sum of the needs up to u (`needUpTo`) is the witness its proof gives. The old sentence stated that specific raise as the result; the law says “some raise of c (in the proof, by the sum of the needs up to u)”, so the theorem's statement is not widened to its proof's value. No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Runaway and the unregistered distance to the break” | title | title (unchanged) |
| S0 “Every policy through registration, with the rest fixed, that keeps its support leaves any larger unobserved stock unused; before the break, how far off the break is does not register.” | statement | statement (unchanged) |
| C0 “A formation g's policy goes through its registration when … (Flow.PolicyThrough);” | definition | law 1 |
| C1 “the rest is fixed when … (Flow.OthersFixed).” | definition | law 1 |
| C2 “With the same formations present, the two give exchange following registration (Flow.exchangeFollows_of_policy).” | law | law 1 (Flow.ExchangeFollows among the declarations) |
| C3 “So, balancing at each step on what g registers, with the starts differing only in a stock g depends on and does not observe, d higher in the second web, for every policy through registration with the rest fixed: where the first web supports g at every step, the stock stands d higher and g registers alike at every step (Flow.policy_keeps_difference);” | law | law 2 (“the same formations present” written in, see above) |
| C4 “where the second web starts at least as high and alike on what g observes, and a difference on a condition g registers has changed by a step, the first web did not support g at every earlier step (Flow.policy_uses_after_failure).” | law | law 3 (“at least as high on what g registers”, the theorem's higher; “under the same policy, rest, presence and balance”) |
| C5 “The web with stock c raised by d at every step, all else as it is (Web.raise), stands at least as high, supports whatever the web supports and stands alike elsewhere (Web.le_raise, Web.Supported.raise, Web.raise_other);” | law | law 4 |
| C6 “it is dependent where the web is (Web.Dependent.raise), and a flow balancing on a family balances there on it (Flow.BalancesOn.raise).” | law | law 4 |
| C7 “At every step at which the web supports g, a raise of a stock g does not observe registers alike for g (Web.registersAlike_raise);” | law | law 5 |
| C8 “observing it, every positive raise registers at every step (Web.observed_raise_registers).” | law | law 5 |
| C9 “Where g does not observe c and c is the only requirement of g that may be unmet up to a horizon u, raising c by the sum of the needs up to u (Web.needUpTo) registers alike at every step at which the web supports g and supports g at every step up to u (Web.break_not_bounded).” | law | law 6 (“some raise of c (in the proof, by …)”, see above; need_le_needUpTo among the declarations; the statement's “before the break, how far off it is does not register” closes the law) |
| C10 “In SupportDrawn the lower web fails the formation at the third step, and a raise registers alike at every step at which the lower web supports it, supports it at the third step and keeps the flow balanced (SupportDrawn.break_unregistered).” | law (witness) | law 7 (the Chinese “原网” became “较低的网”, as the English and the theorem have it) |
| C11 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| H0 “Balance is assumed only on the conditions registered, at each step (Flow.BalancesOn); the policy going through registration and the rest being fixed are supplied hypotheses, from which exchange following registration is derived.” | premise | hypotheses[0] (with L1 appended) |
| H1–H2 | premise | hypotheses[1]–[2] (unchanged) |
| R0 “Ren's “wisdoms to avoid run away feedbacks”;” | Ren's words | correspondence (verbatim, unchanged) |
| R1 “P49 read a runaway as a loop running inside a blindness and marked it a heuristic;” | provenance | correspondence (“testing-within-registration read …”) |
| R2 “after P53 the AI proposed stating it at the level of policies, and Ren answered “no extra review needed, merge, then continue”.” | provenance + Ren's words | correspondence (“after experiment-needs-return”; Ren's words verbatim) |
| R3 “Readings (the AI's, pending Ren): a runaway is a loop …; its policy cannot use what it does not register; avoiding it … needs measurement, a model (理) or another formation's registration; this reads Ren's words of 4 October …” | reading | correspondence (unchanged) |
| R4 “See §73 of the integration note.” | provenance | validation_scope (“author counterreview in the integration note”); §73 stays in the snapshot and the first history note |
| L0 “That a formation draws more than is renewed, wants to keep its support or forms a policy is not derived” | non-implication | does_not_show[0] (“The laws do not derive …”) |
| L1 “what others respond to is supplied” | premise | hypotheses[0] |
| L2 “loops and gain are not defined, so a runaway remains a reading, and what is given here are the two theorems it rests on” | scope | does_not_show[1] |
| L3 “the raised world uses the same flow, which after the break need not be what the formation would do” | scope | does_not_show[2] |
| L4 “the readings are the AI's, pending Ren” | standard boundary | standard_boundaries: names-provisional; the correspondence says “Readings (the AI's, pending Ren)” |
| L5 “contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 13 theorems of Becoming.Runaway all have empty axiom reports, among them …;” | evidence | validation_scope (the receipt); the count and the list stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration); named in the migration history note |
| V3–V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V5 “The author's counterreview is in §73 of the integration note; at Ren's “no extra review needed” there is no independent review.” | evidence | validation_scope (Ren's words verbatim); §73 stays in the snapshot |
| V6 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“the theorems of Becoming.Runaway and this record's local laws”); P57–P61 stays in the snapshot and the history notes |
| (proof bindings) | evidence | validation_scope names the newer binding receipt of Testing and Dependence, 20261014T091930.724493Z, already in the references and proof bindings |
| N0 “Define a loop in general (levels affecting taking, and taking the levels; P65's Loop is one witness, …) and state a runaway itself as a theorem;” | next step | next_delta (“the Loop of Becoming.Response is one witness”) |
| N1–N2 “the policy form where others respond to the stock; measurement with error.” | next step | next_delta (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |
