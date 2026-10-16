# Migration map: wisdom-root-part-one

Schema 1 → schema 2, 14 October 2026 (Asia/Bangkok). Old record sha256 `d52bca486d126519252c5ace6a04776c77b5f7385faf78a79c91b660cc7435e3`; exact bytes in [the snapshot](../../../../../../../architecture/history/d52bca486d126519/wisdom-root-part-one.json). [New record](../../../../../../../../theories/becoming/results/records/wisdom-root-part-one.json).

Each English sentence is listed; its Chinese counterpart follows the same route. Unchanged fields (`hypotheses`, `dependencies`, `related`, `references`, `proof_bindings`, earlier `history`) are not repeated. Declaration names in `laws` are the fully qualified names already declared in `references`; none was renamed.

| Old text | Type | New place |
|---|---|---|
| title.0 “The root of wisdom in Part I: the laws of registration, 理, … hold of every learner and every representation, with no axiom” | title + statement | first clause → `title`; the rest → `statement` (“hold axiom-free of every learner and representation keeping the same content”) |
| claim.0 “The formal support for wisdom-root (the universal laws and routes of formation within Part I's scope) is completed;” | claim + status | `claim` (second sentence) and `statement` (“the formal support of the wisdom-root target”); “is completed” → `status: reviewed-scoped` (unchanged) |
| claim.1 “Section 16 of the main study connects independently described wisdom content to these laws, while full coverage still requires argument: the following checked laws are each stated for every formation, learner, lumping, selection or determined law, with no axiom and their conditions written into the theorems, so no representation keeping the same content escapes them.” | completed connection + non-implication + quantifier | content connection → `progress[1]`; “full coverage still requires argument” → `does_not_show[0]`; quantifier clause → `claim` (first sentence); “Section 16” → `history` |
| claim.2 Registration … 理 (Ren's reading …) … | laws | `laws[0]` (registration), `laws[1]` (理, Ren’s reading verbatim) |
| claim.3 Testing … | law | `laws[2]` |
| claim.4 Learning … 明 (others' registration) … | laws | `laws[3]` (learning), `laws[4]` (明, selection through registration) |
| claim.5 Enough … | law | `laws[5]` |
| claim.6 Runaway … | law | `laws[6]` |
| claim.7 Proxies … | law | `laws[7]` |
| claim.8 Judgment … | law | `laws[8]` |
| claim.9 The meta level … | law | `laws[9]` |
| claim.10 The formal routes of formation … | law | `laws[10]` |
| limitations.0 “Completed formal laws and routes of formation do not automatically prove exhaustive wisdom coverage, universal necessity of every core commitment or sufficiency of the relations.” | non-implication | `does_not_show[0]` |
| limitations.1 “Actual formation, concern and affect, and historical correspondence have separate evidential burdens.” | correspondence | `does_not_show[1]` (verbatim) |
| limitations.2 “P71 has landed with its local conditions retained;” | status of another result | `history` (its conditions stay in its own theorems, as the claim says of every law) |
| limitations.3 “P83’s bounded identification excludes a universal perpetual-revision reading.” | non-implication | `does_not_show[2]`, witness `Becoming.Identification.held_learner_rests`; “P83” → `history` |
| limitations.4 “The pooled-registration examples cited for 明 do not require every improvement to add external information; …” | scope | `does_not_show[3]` |
| limitations.5 “Ethical warrant belongs to Part II.” | scope | `does_not_show[4]` (“The ethical warrant of judgment belongs to Part II.”) |
| limitations.6 “This record adds no Lean; original formal credit stays with the modules and P73/P74, and the added P83 citation is a scope check.” | evidence | “adds no Lean” and modules’ receipts → `validation_scope`; credit and P73/P74 → `history`; P83 scope check → `does_not_show[2]` witness and `history` |
| correspondence.0 “Ren’s reading of 理 and P75’s formal integration are retained.” | correspondence | `correspondence` (first sentence, “the formal integration of the laws”); “P75” → `history` |
| correspondence.1 “Main-study Section 16 connects … risk judgment need not guarantee success. diagonal_refutes and merged_unrested give a refuting course for each learner, not perpetual revision in every actual world.” | completed connection + non-implication | first part → `progress[1]`; refuting course → `does_not_show[2]` (with `laws[3]`, `laws[9]`) |
| correspondence.2 “P83 supplies bounded stable correctness, and P71 has landed.” | completed connection + status | `progress[2]` (`#97-…`); labels and “P71 has landed” → `history` |
| correspondence.3 “Correspondence to aspects of wisdom is an interpretive dependency, not a new Lean composition.” | correspondence | `correspondence` (verbatim) |
| validation_scope.0 “The author's counterreview is in §93 of the integration note …; there is no independent review yet.” | evidence | `validation_scope`; “§93” → `progress[0]` anchor and `history` |
| validation_scope.1 “This record adds no Lean: every theorem it cites is in its module's passed receipt (…), each module bound to its receipt by source hash.” | evidence | `validation_scope` (checker, Lean versions, axiom reports, source-hash binding); receipt timestamps → `history` |
| validation_scope.2 “What is checked is the statements of these theorems and their matching to the four connections of the target wisdom-root; the matching itself … is an argument, not a theorem; 理 is read as Ren reads it, the other readings are the AI's, pending Ren.” | evidence + correspondence | first clause → `validation_scope` and `progress[0]`; the rest → `correspondence` (verbatim) |
| validation_scope.3 “On 13 October 2026, main-study Section 16 adds content correspondence and quantifier counterreview; three checked P83 declarations delimit scope without new proof.” | completed connection + evidence | `progress[1]`; P83 declarations → `does_not_show[2]` witness; date and labels → `history` |
| validation_scope.4 “Dependency types are interpretive, so the wisdom readings are not labeled verified formal adapters.” | correspondence | `correspondence` (“an interpretive dependency”); the unchanged dependency types |
| next_delta.0 “Complete the coverage argument … at their distinct scopes.” | next step | `next_delta` (verbatim) |
| next_delta.1 “Reuse landed P71 and P83 results without listing them as awaiting integration or proof.” | process instruction | `history` |
| counterexamples[0] “Section 8.2: being jointly constrained does not explain wisdom; …” | scope countercase | `counterexamples[0]`, label “Section 8.2” → `history` |

Destination counts (31 old sentences; a sentence split across fields counts once per field): title 1; statement 2; claim 2; status 1; laws 9 (into 11 laws); does_not_show 9; progress 6; correspondence 4; validation_scope 4; next_delta 1; counterexamples 1; unchanged dependency types 1; history 11 (wholly only limitations.2 and next_delta.1; the rest labels, dates and receipts).

Judgments for review: (1) the title keeps its first clause; the quantified law list moves to the statement and `laws`; (2) the bounded identification (three declarations) is cited as a witness and a progress line, not as a law, because the old record used it only as a scope check; (3) “P71 has landed” and the instruction to reuse P71 and P83 are process status, kept in `history`.
