# Migration map: counterfactual-is-the-course

Old record sha256 `a913174fe2e04c50cdda91e2cf1520097450fae762ca7baf6fd315f0c66202ad`; snapshot `_process/architecture/history/a913174fe2e04c50/counterfactual-is-the-course.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T4 “The counterfactual is the course of the law: where the rest follows one law of exchange re…” | title (statement of the result) | title (short name) + statement; T0 → law 3, T1 → laws 5–7, T2 → laws 8–10, T3 → laws 12–13, T4 → laws 18–19 (“as P69’s unfolding” → “as an unfolding”) |
| C0 “Let L, L′ be two flows, W, W′ two webs and part a decided family of formations.” | setting | law 2 (two flows, two webs and a part) |
| C1–C2 “A law of exchange (ExchangeLaw) reads, off a level history, what each formation takes from…” | definition | law 1 |
| C3–C4 “A flow follows the law outside the part (Flow.Follows) when every formation outside the pa…” | definition | law 2 |
| C5 “(1) The counterfactual is fixed by the act: two balanced flows (Flow.Balances) with the sa…” | law | law 3 (“(1)” numbering dropped: laws are numbered by the list) |
| C6–C7 “(2) Generation and feasibility: the law generates a history, levels and a flow step by ste…” | law | law 4 |
| C8 “where the law reads what has stood, the generated flow balances exactly where the course i…” | law | law 5 |
| C9 “With the part acting by another law act reading what has stood and the rest by the law (Ex…” | law | law 6 |
| C10 “where every formation follows one law reading what has stood, a balanced flow is the cours…” | law | law 7 |
| C11 “the last two hold where the course is feasible.” | condition | laws 6, 7 (“where the course is feasible”); hypotheses[2] |
| C12–C13 “(3) Responding through registration follows: the law reads through a registration (Exchang…” | law | law 8 (“P65’s Flow.RespondsThroughRegistration” → a declaration of law 8) |
| C14–C15 “Every law of what has stood reads through registering everything (ExchangeLaw.Nonanticipat…” | law + definition | law 9 |
| C16 “With finitely many conditions (a list holding every condition) and decidable equality of c…” | law | law 10 |
| C17–C19 “conversely, every registration a law reads through, with what the formation depends on, le…” | law | law 11 |
| C20 “(4) The comparison: for two balanced courses of the law with the same formations present, …” | law | law 12 (“an application of Flow.Balances.comparison_within_response” → a declaration of law 12) |
| C21–C22 “with finitely many conditions the registration is the law's sensitivity (comparison_throug…” | law | law 13 |
| C23 “(5) The standard causal model: the history generated where the part makes a list of moves …” | law | law 14 |
| C24 “where a run of that model has not taken move a at x before step t, the record does not fix…” | law | law 15 |
| C25–C27 “(6) Witness: in P65's Loop the second formation's reply is a law, Loop.replyLaw (in the st…” | witness | law 16 (“P65’s Loop” → “the escalation loop”) |
| C28–C29 “(7) As P69's unfolding: where formations and conditions are one kind of relatum, the cours…” | law | law 17 (“P69’s World”, “P69’s exchange” → declarations World, exchange) |
| C30 “A determined law (Determined) steps from s by a beyond what a run of it shows (P69's Shown…” | law | law 18 (“P69’s Shown” → declaration Shown) |
| C31 “so for a run of the course's standard model, its history shows a determined law (Consisten…” | law | law 19 |
| C32 “Where the part's move is formed by a law act on the configuration, the stage and the histo…” | law | law 20 (“P69’s closedBy” → declaration closedBy; “law.withAct part act” → “the law with that act”) |
| L0 “The law itself is not derived (which law the rest follows), nor that it reads what has sto…” | non-implication | does_not_show[0]; hypotheses[0], [1] |
| L1 “ExchangeLaw.Through.responds is near-definitional, the substantive new content being that …” | scope | does_not_show[1] (“P68’s model” → “the causal-model instance”) |
| L2 “the premise moves onto the law: responding to what is not registered, noise and inputs not…” | scope | does_not_show[2] |
| L3 “whether sensitivity remains the least registration with infinitely many conditions is not …” | scope | does_not_show[3]; next_delta |
| L4 “a law sensitive to the level of a condition the formation only depends on does not read th…” | non-implication | does_not_show[4]; counterexample X1 |
| L5–L6 “an infeasible act has no course, and no other reading of it is given;” | scope | does_not_show[5] |
| L7–L8 “the responsive reach is still an upper bound, with no measure of how much difference arriv…” | scope | does_not_show[6] |
| L9 “the instances with P69 are near-definitional: world_balances_iff restates course_balances_…” | scope | does_not_show[7] (the four near-definitional instances, by what they say; their names are declarations of laws 17–20) |
| L10 “the world forms cover only formations and conditions of one kind of relatum, and a law ove…” | scope | hypotheses[7] (world forms ask one kind of relatum); next_delta (a law over two kinds) |
| L11 “the readings and names are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; correspondence keeps “Readings (the AI's, pending Ren)” |
| L12 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation (and no-ethical-premise) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 46 theorems of Be…” | evidence | validation_scope; the count (46) and the named theorems stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V4–V5 “The author's counterreview is in §100 of the integration note;” | evidence | validation_scope |
| R0 “After P64–P68 landed (bca9695b), Ren wrote: “another agent has got this far, maybe merge f…” | provenance (Ren's words) | correspondence (Ren's words verbatim; “After P64–P68 landed (bca9695b)” → history note) |
| R1–R4 “The AI claimed a further proof of the chapter's section 8 that joins P65: “a comparison in…” | provenance + process | correspondence (the open item and the division between the two records); “§8”, “work board P80, accepted by the integrator” and the integrator's request → history note + snapshot |
| R5–R7 “Readings (the AI's, pending Ren): a counterfactual is not a second world beside the actual…” | reading | correspondence (“at P69”, “P65’s premise” → without round labels) |
| R8 “The names (ExchangeLaw, Nonanticipating, Through, Sensitive, course, Feasible and others) …” | names | standard_boundaries: names-provisional |
| R9–R10 “P69 (da8f75a7) landed first;” | landing narration | history note + snapshot |
| R11–R12 “Run.beyond_shown_iff is a law about P69's Shown, kept in Counterfactual, its only user, as…” | code placement | history note |
| R13–R15 “Added readings (the AI's, pending Ren): the course of an act not taken has the form of eve…” | reading | correspondence (“(P69’s World)” dropped: the reading names the unfolding) |
| R16 “See section 100 of the integration note.” | pointer | validation_scope (§100) |
| N0–N2 “Whether sensitivity remains the least registration with infinitely many conditions (or a c…” | next step | next_delta |
| N3 “when a move is the part's own (P69's open item);” | next step | next_delta (“(P69’s open item)” → snapshot) |
| N4 “a law with noise (a move not represented) and its course;” | next step | next_delta |
| N5 “Ren's judgment whether the counterfactual as the course of the law and registration as sen…” | next step | next_delta (“the counterfactual as the course of the law and registration as sensitivity” → “the two readings”, which the correspondence names) |
| H0 “The law of exchange is supplied: which law the rest follows (ExchangeLaw, Flow.Follows) is…” | premise | hypotheses[0] (unchanged) |
| H1 “That the law reads what has stood (ExchangeLaw.Nonanticipating) is a hypothesis of the law…” | premise | hypotheses[1] (the fourteen theorem names → the numbers of the laws they bind; totals_under, bound by no law, keeps its name) |
| H2–H3 “Feasibility of the course (ExchangeLaw.Feasible) is a hypothesis of comparison_with_act, c…” | premise | hypotheses[2], [3] (unchanged) |
| H4 “The comparison laws as in P65: the actual flow balances throughout (Flow.Balances), the tw…” | premise | hypotheses[4] (“as in P65” → “as in comparison-where-the-rest-responds”) |
| H5–H6 “counterfactual_fixed and counterfactual_is_course ask the part to act alike value by value…” | premise | hypotheses[5], [6] (unchanged) |
| H7 “The instances of (7): the world forms ask that formations and conditions be one kind of re…” | premise | hypotheses[7] (“The instances of (7)” → “The instances in the unfolding”) |
| H8 “Discrete steps, counted from step 0; natural-number levels and amounts, with truncated sub…” | representation | hypotheses[8]; standard_boundaries: discrete-steps |
| X0–X1 “The record does not fix the counterfactual: where a run of the model whose input is the pa…” | counterexamples | counterexamples (unchanged) |
