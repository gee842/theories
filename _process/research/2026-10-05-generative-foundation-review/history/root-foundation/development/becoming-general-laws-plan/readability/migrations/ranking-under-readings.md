# Migration map: ranking-under-readings

Old record sha256 `1ab73d2d36b29892d73d2453dad74eb7fdd558410d90170b28adec9fdf378541`; snapshot `_process/architecture/history/1ab73d2d36b29892/ranking-under-readings.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Law numbers count from 1 in the new `laws` list.

| Old text | Type | New place |
|---|---|---|
| T0a “What C ranks under each reading” | title | title (“What comparison principle C ranks under each reading”) |
| T0b “the stepwise reading keeps “sharing is better than winning by consumption” and restraint that meets every need above overdraw, and loses “better without the overdrawing formation” when that formation has a credited event before the loss” | result | statement (second sentence); laws 7, 8, 10 |
| T1 “under the possibility reading C ranks the absence of overdraw, restraint and sharing as the whole-run reading does while withholding no event, extension under it being retaining and adding under the axiom” | result | statement (“the possibility reading keeps all three”); laws 14, 15, 17 (“withholding no event”: law 16, the first event credited as the stepwise reading credits it) |
| T2 “a presence adding no possibility ties with its absence, and possibilities first ranks that presence higher and a rest below activity (P44)” | result + round label | laws 18, 20, 21; “(P44)” in history |
| C0 “Taking two continuations as the configurations of a frame … C is Comparison on that frame.” | definition | law 1 |
| C1 “Two laws hold for every family of courses.” | frame | laws 2 and 3 (“for every family of courses”); statement |
| C2–C3 “The law of comparison with a renewing course (renewed_extends_iff): … (renewed_active_extends_iff).” | law | law 2; statement (first sentence) |
| C4 “The whole-run law of easing (wholeRun_extends_iff_of_eases): …” | law | law 3 |
| C5 “Under the stepwise reading the renewal in the first law cannot be dropped (ThirdParty.renewal_needed), and there is no law of easing (ThirdParty.stepwise_not_monotone).” | law (negative) | law 4 (“the first law” → “the law of comparison”) |
| C6 “For any reading that credits only active events, the continuation without a formation extends … only if the reading withholds every event of that formation.” | law | law 5 |
| C7 “Under the whole-run reading (active and not consuming in that continuation), for every law of the support-gated family …, an instance of the first law, so every comparison satisfying C ranks the former higher.” | law (instance) | law 6; the parenthesis defining the reading → law 1 |
| C8–C9 “Under the stepwise reading (active and not undermining), an event of the focal formation is credited when …; the two continuations then do not extend each other, and an irreflexive, transitive comparison satisfying C prefers the continuation with the formation.” | law | law 7; the parenthesis defining the reading → law 1 |
| C10 “Malignant growth and winning by consumption are instances.” | instance | law 7 |
| C11 “Under the stepwise reading the winner's events before the loss are credited … so sharing still extends winning by consumption, an instance of the first law.” | law (instance) | law 8; statement |
| C12 “Under both readings a continuation in which every need stays met and every formation is active (restraint) extends every continuation that withholds some event, an instance of the first law;” | law (instance) | law 9 |
| C13–C14 “in the two-part family meeting every need makes every formation active, … so every comparison satisfying C ranks restraint higher, even though …; so it is for malignant growth against the same formation stopping after its first step, before the threshold.” | law | law 10; statement |
| C15a “So in the two-part family the stepwise reading loses the comparison with absence,” | conclusion | statement; law 7 |
| C15b “while in every family a course that meets every need at every step extends another under it exactly as the first law states.” | conclusion (restated law) | law 2 (“renews every condition (meets every need at every step)”) |
| C16 “When no focal event is credited, … the stepwise reading too ranks the absence higher (Immediate);” | law (instance) | law 11 |
| C17–C18 “when a third formation shares the condition, … (ThirdParty); that restrained course leaves the third formation's need unmet, and under the whole-run reading it still extends overdraw, by the law of easing.” | law (instance) | law 12 |
| C19 “P44 (Becoming.Relevance) adds a third reading.” | frame + round label | law 13 (“A third reading”); the module is named by the declarations; “P44” in history |
| C20–C21 “The possibility reading (Ranking.possible) credits a formation where a course's levels admit it, active or not; in a dependent course it credits every active formation (possible_of_active).” | definition + law | law 13 |
| C22–C23 “The course without the focal formation admits every formation at every step (absent_admits_all); … (possible_extends), so every comparison satisfying C ranks the former higher (possible_ranks).” | law | law 14 |
| C24 “Both courses of a law have the same requirements (possible_course_iff), so under the axiom extension under this reading is retaining and adding what has significance on the law's web (possible_extends_iff).” | law | law 15 (“the axiom (Unrestricted)”, as hypotheses[3] names it; “this reading” → “the possibility reading”) |
| C25 “Malignant growth: the possibility reading ranks the absence higher and credits the first event, … (malignant_possible).” | law (instance) | law 16 |
| C26–C28 “Sharing extends winning by consumption (possible_contest); … (possible_restraint); … (ThirdParty.possible_extends), where the stepwise reading leaves them unranked.” | law | law 17 (prefixed “Under the possibility reading”) |
| C29–C30 “A formation drawing within renewal adds no possibility: … (possible_tie), while both readings of living rank its presence higher (readings_rank_presence); sharing is an instance (sharing_presence).” | law | law 18 |
| C31 “Generally a level path nowhere lower includes the other (Web.Includes.of_le) and is never ranked below by retaining and adding (Web.not_added_of_le).” | law | law 19 |
| C32–C33 “Possibilities first (…) satisfies C under the possibility reading and is irreflexive and transitive (possibleFirst_order); …” | definition + law | law 20 |
| C34 “in a witness a supported formation resting at step 0 … possibilities first ranks the rest below (Rest.rest_ranked_below).” | instance | law 21 |
| C35 “No Lean axiom is used;” | evidence | validation_scope (“empty axiom reports”) |
| C36 “C occurs only as a hypothesis or a definition.” | premise | hypotheses[0] |
| L0 “The laws of comparison and easing hold for every family of courses;” | scope (restated law) | laws 2 and 3 (“for every family of courses”); does_not_show[0] |
| L1 “the comparisons of absence with presence, sharing with winning and stopping with overdraw are proved in the support-gated family (two parts …) as their instances;” | scope | does_not_show[0] |
| L2 “under the stepwise reading the restraint conclusion needs the restrained course to meet every need (ThirdParty: with several co-drawers it can fail);” | premise (duplicate of H4–H5) | hypotheses[2]; counterexamples[2] |
| L3 “the relation-level reading also credits the focal formation's first relation but is not formalized separately;” | scope | does_not_show[1] |
| L4 “yields no responsibility, duty or feasibility;” | non-implication | does_not_show[2] |
| L5 “chooses no reading.” | non-implication | does_not_show[3] |
| L6 “The possibility reading of P44 coincides with retaining and adding only for two courses of one law;” | premise (duplicate of H8) | hypotheses[3]; “of P44” in history |
| L7 “it counts what can form, not what does, so it leaves a presence adding no possibility unranked;” | scope | does_not_show[4], witness possible_tie |
| L8 “possibilities first is a further premise, at the cost of ranking a rest below activity;” | scope | does_not_show[5], witness Rest.rest_ranked_below |
| L9 “it chooses no reading.” | non-implication (repeats L5) | does_not_show[3] |
| V0 “14 October 2026: the current bytes of Becoming.Bridge, Becoming.Ranking are bound to consolidated receipt 20261013T221720.428753Z (passed: 91 package modules, 4983 theorems, 7020 declaration audits, …; the 90-module core closure compiles from the prelude).” | evidence + date | validation_scope (“checked in”; the Bridge proof binding, unchanged, points to receipt 20261013T204910.042715Z with the same bytes; see history); counts and the date → receipt + snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | provenance | snapshot; the rename table is in the unification plan, and the rename history note records it |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 27 theorems of Becoming.Ranking, the 19 of Becoming.Relevance belonging to this result and the bridge's Ranking.wholeRun_iff and Ranking.undisturbed_eq all have empty axiom reports;” | evidence | validation_scope (the 19 Relevance theorems, the binding receipt for Relevance); the earlier Ranking count → snapshot |
| V3 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V4 “The author's counterreview is in §9 of the integration note.” | evidence | validation_scope (“Author counterreview (integration note)”); §9 → snapshot |
| V5 “The second independent review (BECOMING-P7-REVIEW.md) read this result only as far as its question 4 required and anticipated the restraint result, which this record added as restraint_ranks and malignant_restraint.” | evidence (review) | validation_scope; the theorem names → laws 10 and the snapshot (named in history) |
| V6 “A third independent review (BECOMING-P8-P9-P7B-REVIEW.md, by a separate agent, Claude Opus 5.5, not an author) reviewed the whole result, accepted its mathematics, scoped the restraint conclusion to the two-part family and supplied the credited-event hypothesis to the stepwise cost;” | evidence (review) | validation_scope; reviewer identity → review file + snapshot |
| V7 “its corrections are handled in §12.” | evidence | counterexamples[3] (“corrected in the integration note”); §12 → snapshot |
| V8 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); details → receipt + snapshot |
| V9 “The author's counterreview of P44 is in §64 of the integration note;” | evidence | validation_scope (author counterreview in the integration note); P44 and §64 → snapshot |
| V10 “P44 has not yet been independently reviewed.” | evidence | validation_scope (“The possibility reading awaits independent review”) |
| V11–V12 “P89 (13 October 2026): prior Bridge declarations remain; four added adapters are checked with empty axiom reports.” | evidence + round narration | validation_scope (Bridge checked, empty axiom reports); the P89 note is in the 13 October history entry |
| V13 “This record binds Bridge to the new frozen receipt while other proofs retain their original receipts;” | binding note | proof_bindings (unchanged) + validation_scope (one receipt per module) |
| V14 “adapters are not independent results.” | evidence | validation_scope |
| R0–R4, R8–R9 | correspondence | correspondence (unchanged) |
| R5–R6 “In the two-part family C ranks restraint before the threshold above overdraw under both readings, so the cost of the stepwise reading there is the comparison with absence, and only for a formation with a credited event before the loss; with a third formation sharing the condition the comparison with restraint can be lost too (ThirdParty).” | restated laws | laws 10 and 12, statement, counterexamples[1] (the cost only for a formation with a credited event before the loss) and counterexamples[2]; the passage stays in the snapshot |
| R7 “P44's reading (an AI argument, pending Ren): the possibility reading reads “what has significance is what can form” and Ren's “more possibilities of becoming”;” | correspondence + round label | correspondence (“The interpretation of the possibility reading (an AI argument, pending Ren): it reads …”; quotations verbatim) |
| R10 “Ren left the comparison of courses to the AI on 11 October 2026 (“Comparing courses - you decide”): courses are compared on possibilities, for the reasons in chapter section 6.12 (P54).” | correspondence + round label | correspondence (Ren's words verbatim; “(P54)” dropped) |
| N0 “Ren's choice of the reading of 生生 (courses being compared on possibilities, using no reading of living, which answers whether G0 and C share one reading, P54);” | next step | next_delta (“P54” dropped) |
| N1–N3 | next steps | next_delta (N1 shortened: “co-drawers, or amounts so taking nothing does not undermine”; N3 “under the stepwise reading” → “stepwise”) |
| H0–H1 | premises | hypotheses[0] (with C36) |
| H2–H3, H4–H5 | premises | hypotheses[1], hypotheses[2] (unchanged) |
| H6–H8 “P44: the possibility reading and possibilities first are definitions; …” | premises + round label | hypotheses[3] (“P44:” dropped) |
| X0–X2, X4–X5 | counterexamples | counterexamples (unchanged) |
| X3 “Third independent review: every P8, P9 and P7b declaration is accepted …; … (corrected, integration note §12).” | counterexample (review summary) | counterexamples[3] (same rewrite as in joint-difference-making) |
