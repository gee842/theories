# Migration map: becoming-return-grades

Old record sha256 `0cb1f8709352d845b641944d219b269c7da7308bbfcfe8572ec3410f07d5b4bf`; snapshot `_process/architecture/history/0cb1f8709352d845/becoming-return-grades.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C1–C2 hold en C1 and zh C9–C10 hold en C8, so the zh claim labels run up to two ahead).

Each law was read against its declarations in `Becoming/Return.lean` (and `RelationalRenewal.fluctuating_neither` for law 3); none states more than the declaration.

| Old text | Type | New place |
|---|---|---|
| T0 “Return grades” | title | title (unchanged) |
| S0 “Consumption is exactly a dependence that never returns, and recovery can slow without bound.” | statement | statement (unchanged) |
| C0–C1 “On a web of dependence, a dependence holding at a step returns within p steps when …; a condition is renewed within p when …, and it returns when …” | definitions | law 1 (unchanged) |
| C2–C4 “The grades are ordered: renewal implies renewal within one step; renewal within p implies renewal within any longer cycle and implies return; a condition that returns is not consumed.” | law | law 2 (unchanged) |
| C5 “Consumption is exactly a dependence that never returns.” | law | law 2 (joined with “and”); statement |
| C6 “The seasonal condition of RelationalRenewal, neither renewed nor consumed, is renewed within two steps and not within one.” | law (witness) | law 3 (unchanged) |
| C7 “Recovery can slow without bound: …” | law (witness) | law 4 (unchanged); statement |
| C8 “Readings over cycles extend the stepwise readings: …” | definitions | law 5 (unchanged) |
| C9–C11 “Undermining for one step is exactly undermining at the step; a longer cycle includes more; a formation renewing over some cycle is not consuming, and none of its events undermines for that cycle.” | law | law 6 (unchanged) |
| C12 “Renewal implies renewal within one step, not conversely: …” | law (witness) | law 7 (unchanged); counterexamples[1] states it too |
| C13 “Cycle length 0 is degenerate: …” | law | law 8 (unchanged); counterexamples[2] and hypotheses[2] state it too |
| C14–C15 “Over cycles of two, a dip and a dependent broken while inactive are included; after an escalation the condition never returns, and the escalating event undermines for every cycle.” | law (witnesses) | law 9 (unchanged) |
| C16 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for Becoming.Return) |
| L0 “Contains no ethical predicate, chooses no cycle length and does not decide which reading is the reading of 生生.” | standard boundary + non-implication | standard_boundaries: no-evaluation (“contains no ethical predicate”); does_not_show[0] (the rest) |
| L1 “Slowing and Dip are minimal witnesses;” | scope | does_not_show[1] |
| L2 “the grades involve no amounts of what is drawn.” | scope | does_not_show[2] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): all 29 theorems of Becoming.Return have empty axiom reports;” | evidence | validation_scope (with the binding receipt of the current bytes, 20261014T091930.724493Z, from proof_bindings); the count (29) stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §8.6 of the integration note;” | evidence | validation_scope (“in the integration note”; §8.6 stays in the snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-P7-REVIEW.md), and its corrections are handled in §11;” | evidence (review) | validation_scope (“the second independent review … is handled there”; counterexamples[3] names it the second); reviewer, file and §11 stay under sources and in the snapshot |
| V4 “a fourth independent review (BECOMING-P9B-P10-P11-REVIEW.md) changed undermining to the minimum form, which the cycle readings follow, see §15.” | evidence (review) | validation_scope; §15 → snapshot |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| R0–R1 | correspondence | correspondence (unchanged) |
| N0–N1 | next step | next_delta (unchanged) |
| H0–H2 | premises | hypotheses[0]–[2] (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |
| X2 “Cycle length 0 is degenerate (…): … undermines for zero steps (from P11b), even in a renewing run (second independent review F10).” | counterexample | counterexamples[2] (“(from P11b)” dropped: Web.undermining_for_zero states it of the current definition without condition; the round label stays in the snapshot) |
| X3 “Second independent review: the mathematics of P7 is accepted; … the §8.5 table … (corrected, integration note §11).” | counterexample (review summary) | counterexamples[3] (the rewrite of joint-difference-making: “of P7” → “under review”; “the §8.5 table” → “the integration note's comparison table”; “integration note §11” dropped) |
