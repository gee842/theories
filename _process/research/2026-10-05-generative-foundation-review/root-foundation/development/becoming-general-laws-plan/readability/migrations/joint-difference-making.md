# Migration map: joint-difference-making

Old record sha256 `a74418f91c42e2fbe9064840e312e4ebc3a16f46301252d9b91b9b4dfe3b7238`; snapshot `_process/architecture/history/a74418f91c42e2fb/joint-difference-making.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0 “Difference-making in joint activity: but-for and relational participation come apart under overdetermination” | title (statement of the result) | title (short name) + statement (second sentence) |
| C0 “In every process with observables of dependence, the but-for test, which holds the move actually taken fixed, extends from one party's part to parts withheld together, and a difference made only together has an exact law (differenceOnlyTogether_iff): …” | framing + law | statement (first sentence); law 2 (parts withheld together); law 7 (the joint law, unchanged wording) |
| C1 “The direction from right to left holds in every process (DifferenceOnlyTogether.of_breaks);” | law | law 8 |
| C2 “the other needs, at each member's withheld configuration, the move to be available (Blocked) and the need to be met (NeedRises).” | non-implication | counterexamples[6] (unchanged; it states exactly this) and law 7's conditions |
| C3 “A difference made only together needs at least two parts, and when the loss is overdetermined every set of parts whose withholding keeps the dependence makes it only together.” | law | law 8 (two parts); law 6 (overdetermination) |
| C4 “For one part, in every process and without determinacy, where the move can be taken with the part withheld and the dependence holds and is met there, the part makes the difference exactly when the same move no longer breaks the dependence (makesDifference_iff);” | law | law 3; the theorem's hypothesis that the step breaks the dependence is now written in (judgment call, see history) |
| C5 “when the move determines the step, breaking is the reached level falling below the need (breaksBy_iff_level).” | law | law 4; the theorem's hypothesis that the dependence holds and is met is now written in |
| C6 “So when the move determines the step and is available after withholding, and the dependence still holds and is met at the withheld configuration, the test is a dichotomy: …” | law | law 5 (determined_dichotomy, its hypothesis that the step breaks the dependence written in) |
| C7 “when withholding the part itself leaves the dependence unmet (the part is a support), the test is silent.” | scope | does_not_show[3] |
| C8 “The terms: keeping and breaking between configurations are, along a run, exactly those of Becoming.Dependence, and they are exclusive;” | definition + law | law 1 (“of Becoming.Dependence” → “of the dependence dynamics”; the module is among the declarations) |
| C9 “a party's part makes the difference when the step from a configuration by a move breaks a dependence and, with that part withheld, …” | definition | law 2 |
| C10 “parts make it together when this holds with all of them withheld;” | definition | law 2 |
| C11 “the loss is overdetermined when withholding any single part still leaves a breaking step by the same move.” | definition | law 6 |
| C12 “The test reads as intended when the move determines the step (Determined): with a shock written into the step relation of a single move, the loss is overdetermined again … (Hidden);” | premise + counterexample | hypotheses[1] (reads as intended when the move determines the step); counterexamples[3] (Hidden, unchanged) |
| C13 “a move unavailable after withholding decides nothing (Tagged).” | counterexample | counterexamples[4] (Tagged, unchanged) |
| C14 “Without the move held fixed, the move decides: from one configuration a lone drawer's part makes the difference under a calm move, while under an exogenous shock the loss is overdetermined.” | counterexample | counterexamples[1] (Shock.move_decides; same content, unchanged) |
| C15 “The processes of Pool and Shock are determined by the move.” | law | law 9 (Pool.determined, Shock.determined) |
| C16 “Pool is an instance of the joint law: in one process at one level with the first drawer taking the same amount, with one other drawer its part makes the difference;” | instance | law 9 |
| C17 “with two others the loss is overdetermined, its part makes none, and the first two drawers make the difference only together (first_two_only_together), so the difference belongs to the joint activity.” | instance | law 9 |
| C18 “In both runs the relational reading counts it as consuming, and a formation that takes nothing is not.” | instance | law 10 (“it” → “the first drawer”) |
| C19 “Across a formation's own events the run-level and step-level tests come apart: drawing two units at every step in the renewable process consumes the condition;” | law (witness) | law 11 |
| C20 “the first event's step keeps the dependence and undermines for no positive cycle;” | law (witness) | law 11 |
| C21 “with any single event's draw withheld, indeed with every draw before any step withheld, the condition is still consumed, the run-level outcome being fixed by the tail;” | law (witness) | law 11 |
| C22 “at the breaking step, drawing nothing from the same configuration keeps the dependence, so the breaking event makes the step-level difference.” | law (witness) | law 12 |
| C23 “The stepwise reading does not track difference-making: in Pool a drawer taking exactly the renewal, whose part makes no difference, undermines at the break another causes.” | non-implication | does_not_show[2], witness Pool.within_share_undermines |
| C24 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (hypotheses hold no ethical premise; the receipt reports empty axioms for Becoming.Joint) |
| L0–L1 “Proposes no causal theory; finer attribution (the NESS test, actual causation in structural equations) is not added.” | scope | does_not_show[0] |
| L2 “Yields no responsibility, duty or ranking.” | non-implication | does_not_show[1] |
| L3 “Pool, Shock and depleting are minimal witnesses;” | scope | does_not_show[4] |
| L4 “the test holds the move fixed, and an application with exogenous shocks must write them into the move, not into the step relation (Hidden).” | premise (duplicate of H2–H3) | hypotheses[1] |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): all 34 theorems of Becoming.Joint have empty axiom reports;” | evidence | validation_scope |
| V1 “the same receipt covers the package's 91 modules … 4983 theorems/7020 declaration audits, and 39 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §8.6 of the integration note;” | evidence | validation_scope (“in the integration note”; §8.6 stays in the snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-P7-REVIEW.md), and its corrections are handled in §11;” | evidence (review) | validation_scope (second independent review, listed under sources); reviewer identity and §11 stay in the review file and the snapshot |
| V4 “a third independent review (BECOMING-P8-P9-P7B-REVIEW.md) found that but-for needs the move to be available and to determine the step, corrected in §12;” | evidence (review) | validation_scope; §12 → snapshot |
| V5 “a fourth (BECOMING-P9B-P10-P11-REVIEW.md) found that the dichotomy also needs the dependence to hold and be met at the withheld configuration, corrected in §15.” | evidence (review) | validation_scope; §15 → snapshot |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and injEq/propext detail stay in the receipt and the snapshot |
| V7 “The joint law, the single-part laws, Pool's instance and the Blocked and NeedRises counterexamples, added on 14 October 2026 (13 theorems; Becoming.Joint now has 34), are checked in consolidated receipt …” | evidence + round narration | validation_scope (the laws and counterexamples among the 34 theorems); the date and the count of 13 are in the L2 history note and the snapshot |
| R0–R5 “The but-for test and the relational reading answer different questions: …” | correspondence | correspondence (unchanged) |
| N0–N1 “Add finer attribution as another reading and compare it with the relational reading; explain how, under overdetermination, …” | next step | next_delta (unchanged) |
| H0–H1 “Withholding is a supplied map on configurations: … Whether withholding leaves the rest unchanged is a modelling duty of each application.” | premise | hypotheses[0] (merged with H8–H9, the same modelling duty) |
| H2–H4 “The test holds the move actually taken fixed: … In Pool the next level does not depend on the move, so the conclusions are unaffected.” | premise | hypotheses[1] (“must write them into the move” as in L4 → “belong in the move”, the old H3 wording) |
| H5 “The relational reading is the whole-run reading of relational-reading-comparison, read through Web.ConsumingIn.” | premise | hypotheses[2] (unchanged) |
| H6–H7 “The run-level test … and MakesDifference … are different tests; … so depletion_is_joint uses the former.” | premise | hypotheses[3] (unchanged) |
| H8–H9 “Withholding several parts applies the supplied withholding one part after another in the listed order (withholdAll); whether the order matters belongs to the same modelling duty.” | premise | hypotheses[0] |
| X0, X1, X3, X4, X6 | counterexamples | counterexamples[0], [1], [3], [4], [6] (unchanged) |
| X2 “Second independent review: the mathematics of P7 is accepted; … the §8.5 table was unfair … (corrected, integration note §11).” | counterexample (review summary) | counterexamples[2] (“of P7” → “under review”; “the §8.5 table” → “the integration note's comparison table”; “integration note §11” dropped; §8.5 and §11 stay in the snapshot) |
| X5 “Third independent review: every P8, P9 and P7b declaration is accepted …; … (corrected, integration note §12).” | counterexample (review summary) | counterexamples[5] (“every P8, P9 and P7b declaration” → “every declaration under review”; “integration note §12” → “in the integration note”) |
