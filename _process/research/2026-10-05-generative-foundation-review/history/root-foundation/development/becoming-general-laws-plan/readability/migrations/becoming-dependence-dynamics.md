# Migration map: becoming-dependence-dynamics

Old record sha256 `df070b67d73609e4e890682a8f821c5ec1a07812e32409bcccfe7c4eb4d15122`; snapshot `_process/architecture/history/df070b67d73609e4/becoming-dependence-dynamics.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The old record had no `statement`. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (its sentence breaks differ slightly: zh C0 holds en C0–C1, zh C4–C5 hold en C5, zh N4–N5 hold en N4).

Each law was read against its declarations in `Becoming/Dependence.lean`; none states more than the declaration. `Web.Dependent` and `Web.Supported` are not among this record's referenced declarations, so law 4 names only the theorems.

| Old text | Type | New place |
|---|---|---|
| T0 “Dependence that forms, holds, breaks and transforms: three outcomes of a loss” | title (statement of the result) | title (short name, the module's own heading) + statement (“three outcomes of a loss”) |
| C0–C1 “Let which conditions a formation depends on, at what level, and which it draws on be observables of the configuration; every run then reads as a web of dependence.” | definition + law | law 1; statement (first sentence) |
| C2 “Across each step a dependence is kept, broken, formed or dissolved;” | definition | law 2; statement (first sentence) |
| C3 “with constant dependence this reading recovers the static renewing/consuming classification exactly.” | law | law 1 |
| C4 “Change is made at a step: … (stated without excluded middle).” | law | law 3 (unchanged) |
| C5 “Every met dependence is exactly one of kept or broken across each step, and renewal and consumption remain exclusive.” | law | law 2 |
| C6–C8 “In a web where a formation is active only where … (Dependent), theorems connect three outcomes of a loss, which are neither exhaustive nor exclusive: … with fixed dependence it ends.” | law | law 4 (unchanged); statement (second sentence) |
| C9 “All three occur: in one process from one configuration, three runs break the same dependence at the first step … and then end, transform and restore.” | law (witness) | law 6; statement (“one process shows all three”) |
| C10 “The reading of the break does not fix the next configuration;” | non-implication | counterexamples[0] (Crossing.loss_does_not_decide, which states exactly this; unchanged) |
| C11 “in this witness the move that makes the break selects the outcome.” | law (witness) | law 6 |
| C12 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for Becoming.Dependence) |
| L0 “Contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| L1 “The general theorems on the three outcomes only constrain them, and the outcomes are neither exhaustive nor exclusive;” | non-implication | does_not_show[0] |
| L2 “the reading of the break does not fix the next configuration.” | non-implication (duplicate of C10) | counterexamples[0] |
| L3 “Dependent excludes buffers, reserves and lags;” | scope (duplicate of H1) | does_not_show[1]; hypotheses[1] keeps it |
| L4 “it is the zero reserve, and with a reserve these outcomes are deferred, not removed, see reserve-defers-ending.” | scope | does_not_show[1] |
| L5 “Does not complete the whole deduction.” | non-implication | does_not_show[2] |
| L6 “Difference-making, cycle-level renewal and substitution are in joint-difference-making, becoming-return-grades and substitution-preserves-consumption.” | scope | does_not_show[3] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): all 62 theorems of Becoming.Dependence have empty axiom reports, the stepwise ones (including P7b's NewNeed and Pinned theorems, P9b's …, and P11b's …) belonging to becoming-stepwise-reading;” | evidence | validation_scope (the receipt, the theorems of Becoming.Dependence, the stepwise ones belonging to becoming-stepwise-reading; the binding receipt of the current bytes, 20261014T091930.724493Z, from proof_bindings, named alongside); the count (62) and the round labels stay in the receipt, the history entries of those rounds and the snapshot |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §§4 and 6 of the integration note;” | evidence | validation_scope (“in the integration note”; §§4 and 6 stay in the snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-RENEWAL-READING-REVIEW.md), and its corrections are handled in §7.” | evidence (review) | validation_scope (“a separate agent, not an author … listed under sources … handled in the integration note”); the reviewer's model, the file name and §7 stay under sources and in the snapshot |
| V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V5 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence + round label | validation_scope (the theorems of Becoming.Dependence include them); P50 → history (its existing entry) + snapshot |
| V6 “This record's local laws (P63, P61b) are in the same receipt, with empty axiom reports.” | evidence + round labels | validation_scope; P63, P61b → history (existing entries) + snapshot |
| R0–R4 “Formations and conditions are analytic roles in one unfolding, not independent entities. …” | correspondence | correspondence (unchanged) |
| N0 “The exact restatement for every world is this record's Web.consumed_ends_when_fixed_at (P63), the local condition inside the law: only that the formation is supported where active at that step;” | local law appended to next | law 5 (ending); P63 → history (existing entry) |
| N1 “Web.consumed_ends_when_fixed is its corollary;” | corollary | law 5 (“the forms under Dependent are their corollaries”) |
| N2 “the exact restatement for every world is this record's Web.continuing_restores_at, Web.consumed_continues_transformed_at (P50), the local condition inside the law: only the formation's support at that step;” | local law appended to next | law 5 (restoration and transformation); P50 → history (existing entry) |
| N3 “Web.continuing_restores, Web.consumed_continues_transformed are their corollaries;” | corollary | law 5 |
| N4 “relaxing Dependent is stated in reserve-defers-ending (Dependent is the zero reserve, and a reserve defers the end without escaping it), with lagged coextinction along chains of dependence stated there too where the reserve decays (P31);” | completed connection (not a next step) | does_not_show[1] (merged with L3–L4); P31 → snapshot |
| N5 “the individuation of formations: identity-across-steps proves that the distinction between ending and transformation, arising and undermining depend on identity across steps, and that continuity of activity and dependence constrains it up to succession;” | context of the next step | next_delta (second clause) |
| N6 “deriving identity from relations, and representing splits and merges, remain open.” | next step | next_delta (first clause, stated positively: “Derive … and represent …”) |
| H0, H1, H2 | premises | hypotheses[0]–[2] (unchanged) |
| X0–X3 | counterexamples | counterexamples[0]–[3] (unchanged) |
