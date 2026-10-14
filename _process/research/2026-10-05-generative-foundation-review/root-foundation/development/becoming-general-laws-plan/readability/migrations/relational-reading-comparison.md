# Migration map: relational-reading-comparison

Old record sha256 `4fe6bb1f04e142dda4e6f4fbd67468f722af056767de93cdd233e56b5f98ebc7`; snapshot `_process/architecture/history/4fe6bb1f04e142dd/relational-reading-comparison.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0 “Read relationally, comparison ranks consuming formation below its absence” | title | title (unchanged; already a short name); statement |
| C0 “For every family of courses, a course that renews every condition extends another under the relational (whole-run) reading exactly when … (Ranking.renewed_extends_iff);” | law | law 1 |
| C1 “where every formation is active at every step of it, exactly when the other withholds some event (Ranking.renewed_active_extends_iff).” | law | law 1 |
| C2 “Read relationally, so that the active events of formations not consuming … are the generative grounds, G0 credits exactly those events and is silent on a consumer's events.” | law | law 2 (g0_relational) |
| C3 “For every law of the relational-renewal family in which the focal formation draws beyond renewal from some step on, the same unfolding without that formation renews every condition and is a generative extension …, an instance of that law (SupportGated.overdraw_extension), so the comparison principle C ranks it strictly higher and no asymmetric comparison satisfying C prefers the overdraw;” | law | law 3 (extension), law 4 (ranking); statement |
| C4 “this holds for a dependent (malignant) and an independent (winning) focal formation alike.” | law | law 3 |
| C5 “Read event by event, the two unfoldings are incomparable by extension, and an irreflexive, transitive comparison satisfying C prefers the overdraw.” | law | law 5; statement (“read event by event, C does not decide”) |
| C6 “Sharing is a generative extension of winning by consumption under both readings, an instance of the same law and, under the event-by-event reading, of Ranking.extendsUnder_iff_of_exact (SupportGated.contest_extensions).” | law | law 6 (“of Ranking.extendsUnder_iff_of_exact” → “of the law of extension for a reading exact on the extending course”; the theorem is among the declarations) |
| C7 “The comparisons use C, not G0;” | premise | hypotheses[0] |
| C8 “no Lean axiom is used.” | evidence | validation_scope (“every axiom set empty”, “empty axiom reports”); the standard key no-ethical-premise is not cited, since the old record did not state the absence of an ethical premise and C is a comparison premise |
| L0 “The law of comparison holds for every family of courses where the extending course renews every condition;” | law (restated condition) | law 1 |
| L1 “the comparisons here are its instances in one law family and its absent course.” | scope | does_not_show[0] |
| L2 “Classification is per whole continuation, so a consuming formation's events before its overdraw are not grounds;” | scope | does_not_show[1] |
| L3 “a stepwise reading is not settled.” | scope | does_not_show[1] (“this record settles no stepwise reading”); related ranking-under-readings treats it |
| L4 “It does not rank mixed cases, decide fluctuating ones, establish feasibility or obligation, or establish real correspondence.” | scope + non-implication | does_not_show[2] (mixed, fluctuating), does_not_show[3] (feasibility, obligation, real correspondence) |
| L5–L6 “As in renewing-consuming-formation's event_comparison_ranks_rest_below, a law that omits rest's restorative role makes C rank rest below … ; rest is not consumption, but this comparison does not represent its value.” | scope | does_not_show[4] (the theorem name event_comparison_ranks_rest_below, not among this record's references, stays in the snapshot; the record is named) |
| V0 “Lean 4.29.1 check passed in the shared relational-renewal receipt: RenewalComparison 15 theorems / 24 declaration audits, every axiom set empty;” | evidence | validation_scope (unchanged) |
| V1 “GenerativeComparison compiled unchanged as a hashed dependency (audited by its own checker);” | evidence | validation_scope (unchanged) |
| V2 “4 further compiled application examples.” | evidence | validation_scope (unchanged) |
| V3–V4 “Author counterreview; no independent-agent review.” | evidence | validation_scope (unchanged) |
| V5 “The law of comparison with a renewing course (Becoming.Ranking) and the instance theorems in the new bridge module Becoming.RenewalBridge, 14 October 2026, are checked in consolidated receipt 20261013T221720.428753Z with empty axiom reports.” | evidence + date | validation_scope (“new” and the date dropped; both are in the L2 history note) |
| R0–R3 | correspondence | correspondence (unchanged) |
| N0 “Stepwise, cycle and relation-level readings are now defined on the Becoming spine (becoming-stepwise-reading, becoming-return-grades).” | another record's scope | history note + snapshot; the related result becoming-stepwise-reading carries the stepwise and relation-level readings |
| N1 “ranking-under-readings proves on the core that under the stepwise reading this record's ranking of an overdraw below its absence no longer follows from C alone, while the ranking of sharing above winning by consumption survives.” | another record's result | related ranking-under-readings (its detail says the same) + snapshot |
| N2–N3 “Remaining: several conditions with substitution (…); which mixed cases a stronger comparison or J commitment ranks, and with what premise.” | next step | next_delta (“Remaining:” dropped) |
| H0–H1 “C (ComparisonPrinciple) is a hypothesis of the ranking theorems; G0 appears only in the interface theorem g0_relational. Both are imported unchanged from GenerativeComparison.” | premise | hypotheses[0] (C7 folded in) |
| H2–H4 | premise | hypotheses[1] (unchanged) |
| H5–H6 | premise | hypotheses[2] (unchanged) |
| X0–X1 | counterexamples | counterexamples (unchanged) |
