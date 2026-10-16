# Migration map: becoming-finite-horizon

Old record sha256 `36892d100c6c20b1a0ba59818e70d786386290ba0dc48f1ffba04ac25d2be124`; snapshot `_process/architecture/history/36892d100c6c20b1/becoming-finite-horizon.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Horizon.lean` and `Becoming/Testing.lean`; none states more than the declaration. Law 1 says the two runs' configurations and actions “agree before h”, as the old text did; `Run.AgreeUpTo h` also has the configurations agree at h, so the law is, if anything, weaker than the theorem, never wider.

| Old text | Type | New place |
|---|---|---|
| T0 “Finite horizon” | title | title (unchanged) |
| S0 “Whether drawing renews or consumes is left open by every finite history.” | statement | statement (unchanged) |
| C0 “In the renewable process of Becoming.Renewal, for every horizon h there are two runs whose configurations and actions agree before h: …” | law (witness) | law 1 (unchanged) |
| C1–C2 “Afterwards one run draws within renewal and the focal formation renews in it; the other keeps exceeding and the focal formation consumes.” | law (witness) | law 1 (unchanged) |
| C3 “Hence any reading fixed by the configurations and actions of the first h steps that includes every renewing run includes some consuming run.” | law | law 2 (unchanged) |
| C4 “The classification is a function neither of the initial configuration nor of any finite prefix.” | law | law 2 (joined with a semicolon) |
| C5–C6 “The same holds with feedback: … the stopping schedule never reaches the support threshold.” | law (witness) | law 3 (unchanged) |
| C7 “The force of the conclusion lies in “includes every renewing run”: …” | law (witness) | law 4 (unchanged; Renewable.whole_run_includes_overdraw is its declaration) |
| C8 “an amount reading (taking no more than is renewed at the step) is fixed by finite prefixes and withholds every event before h in both runs, failing only to include every whole-run-renewing run.” | law | law 5 (“an” → “An”); counterexamples[1] states it too |
| C9 “The formation-level cycle reading is fixed by no finite prefix.” | law | law 6 (unchanged); counterexamples[0] states it too |
| C10 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for Becoming.Horizon and the two Testing corollaries) |
| C11 “Corollaries (P49, Becoming.Testing): no reading decided by the first h steps is the whole-run classification (Renewable.no_exact_finite_reading);” | law | law 7 (“(P49, Becoming.Testing)” → “Corollaries:”; the module is in the declarations and the evidence paragraph; P49 → history (its existing entry) + snapshot) |
| C12 “such a reading including no consuming run excludes some renewing run (Renewable.finite_reading_withholds_renewal).” | law | law 7 (English unchanged; the Chinese “不认可任何消耗的运行的这种读法，不认可某个更新的运行” → “不记入任何消耗运行的这种读法，必不记入某次更新运行”, matching the English “includes” and the record's other uses of 记入; judgment call, see history) |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “proved once in the renewable process without feedback and once in the support-gated law with feedback;” | scope | does_not_show[0] |
| L2 “does not say how to inquire into a run's continuation;” | non-implication | does_not_show[1] |
| L3 “does not treat webs of dependence with amounts and renewal rates.” | scope | does_not_show[2] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): all 12 theorems of Becoming.Horizon have empty axiom reports;” | evidence | validation_scope (with the binding receipt of the current bytes, 20261014T091930.724493Z, from proof_bindings); the count (12) stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §8.6 of the integration note;” | evidence | validation_scope (“in the integration note”; §8.6 stays in the snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-P7-REVIEW.md), and its corrections are handled in §11.” | evidence (review) | validation_scope (“the second independent review … is handled there”; counterexamples[2] names it the second); reviewer, file and §11 stay under sources and in the snapshot |
| V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V5 “The two corollaries are in Becoming.Testing (the same receipt 20261013T094743.528770Z, all 92 theorems with empty axiom reports), recorded as corollaries of this record following the seventeenth independent review (F9).” | evidence | validation_scope (the corollaries' empty axiom reports and the seventeenth review); the count (92) stays in the receipt and the snapshot |
| R0–R5 | correspondence | correspondence (unchanged) |
| N0–N1 | next step | next_delta (unchanged) |
| H0–H2 | premises | hypotheses[0]–[2] (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |
| X2 “Second independent review: the mathematics of P7 is accepted; … the §8.5 table … (corrected, integration note §11).” | counterexample (review summary) | counterexamples[2] (the rewrite of joint-difference-making: “of P7” → “under review”; “the §8.5 table” → “the integration note's comparison table”; “integration note §11” dropped) |
