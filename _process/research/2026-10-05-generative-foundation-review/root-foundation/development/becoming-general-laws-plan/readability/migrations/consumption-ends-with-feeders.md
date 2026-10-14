# Migration map: consumption-ends-with-feeders

Old record sha256 `0a96edd6f1b0c8e2dcc7c9592c07ae3e1d6ca81210c11efe2d6f9f668767e9dc`; snapshot `_process/architecture/history/0a96edd6f1b0c8e2/consumption-ends-with-feeders.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh R0 holds en R0–R2, because the English quotation has full stops, so later zh correspondence labels run two behind; zh V13 holds en V13–V14).

Each law was read against its declarations in `Becoming/Interdependence.lean`, `Becoming/Feeding.lean`, `Becoming/Flow.lean`, `Becoming/Regions.lean` and `Becoming/Dependence.lean`; none states more than the declaration. Law 7 states less than `Overshoot.steady_continues`, which also gives `Flow.Acting`, `Flow.Taking` and `Web.Dependent` for the steady flow, as the old text did. Law 3 is newly written. The old record held these local laws only in its references, its history (the entry that added them) and the evidence sentence V8. The law now states them from `Flow.unfed_consumption_ends_at` and `Flow.consumption_ends_with_feeders_at`: balance at `c` (`Flow.BalancesOn [c]`) and `Flow.GiversSupported` at `c` are asked only at the `n` consecutive steps counted. The `unfed` or `requires`/`unsupported` and `consumes` premises are those of laws 1–2. Law 1 keeps “derived from Flow.excess_bounded”. The current proof reaches it through the local form `Flow.excess_bounded_at` (law 3); the name is kept as it stands in the source.

| Old text | Type | New place |
|---|---|---|
| T0 “Consumption ends with its feeders” | title | title (unchanged) |
| S0–S1 “Under balance, … stays active at most as many consecutive steps as that level; keeping its own support, it can still end through its feeder.” | statement | statement (unchanged) |
| C0 “Let the flow balance (Flow.Balances), with only active formations giving (Flow.Acting) and activity needing support (Web.Dependent).” | premises of the law | law 1 (the names in parentheses are among the law's declarations) |
| C1 “If a formation g is present and takes from a condition c at every step from T at which it is active, … (Flow.Balances.unfed_consumption_ends, derived from Flow.excess_bounded), so it is not active at every step from T (Flow.Balances.unfed_consumption_not_continuing).” | law | law 1 (the theorem names are the law's declarations; “derived from Flow.excess_bounded” kept) |
| C2 “If g requires c while active and everything feeding its continuation from T on is unsupported, nothing supported gives to c (Flow.unfed_of_feeders_unsupported), so the same bound holds (Flow.Balances.consumption_ends_with_feeders).” | law | law 2 (theorem names → declarations) |
| C3–C4 “The witness Overshoot: … so the feeding closure of either is the whole (Overshoot.closure_whole).” | law (witness) | law 4 (theorem name → declarations) |
| C5–C6 “The flow balances, only active formations give, … and false feeds true's condition at step 0;” | law (witness) | law 5 (“There” added: these are Overshoot's; Web.RenewingOver and Web.UnderminingAt → declarations) |
| C7 “false is unsupported from step 1 on, true is active for at most one consecutive step from step 1, and from step 2 on nothing is supported (Overshoot.ends_through_feeder).” | law (witness) | law 6 (“In Overshoot” added; split from law 5 to stay under the item cap) |
| C8 “With the same dependences, each taking only from its own condition (Overshoot.steadyFlow, Overshoot.steadyWeb), the flow balances and both are active and supported at every step (Overshoot.steady_continues).” | law (witness) | law 7 (names → declarations) |
| C9 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| C10 “P86 gives exact conditions for meeting needs under local balance: … (Flow.meets_after_iff_at), with every-step and stretch forms (Flow.stays_met_iff_at, Flow.meets_over_iff_at);” | law | law 8 (“P86 gives exact conditions …:” → “Exact conditions …:”; P86 → history (existing entry) + snapshot) |
| C11 “this does not make support sufficient for activity.” | non-implication | does_not_show[1] (“this” → “The exact conditions”; zh “不是支持充分推出活动” → “精确条件不使支持足以推出活动”) |
| C12–C13 “When givers are supported and none supported gives, … (Flow.unfed_meets_iff_at). Requiring and taking for more steps than the initial level exhibits a supported feeder at one of them (Flow.fed_beyond_level_at).” | law | law 9 |
| C14 “Withholding a part taking nothing from the condition … (Flow.meets_without_iff_at).” | law | law 10 |
| C15–C18 “Either feeder suffices in Redundant; … withholding both with remaining taking fixed leaves no balancing path (Redundant.withheld_either, Redundant.withheld_both).” | law (witness) | law 11 |
| L0 “Loss does not always return: Redundant explicitly gives either feeder’s sufficiency and the stock bound.” | non-implication | does_not_show[2], witness Redundant.either_suffices |
| L1 “Meeting needs does not imply continued actual activity;” | non-implication | does_not_show[1] |
| L2 “witness activity is specified and shown consistent with balance and dependence.” | scope | does_not_show[1] |
| L3 “Overshoot still compares two flows;” | scope | does_not_show[3] (hypotheses[2] states the two-flow comparison too) |
| L4 “P86 adds withholding within one flow, but withholding both with the original taking fixed proves no balancing path, not a dynamically adjusted activity.” | scope | does_not_show[3] (“P86 adds withholding within one flow” → “withholding within one flow is added”), witness Redundant.withheld_both |
| L5 “Existing reserve-ending bounds are reused.” | scope | does_not_show[4] |
| L6 “Across-step feeding characterizes possible carrying only, leaving actual origin open.” | scope | does_not_show[5] |
| L7 “No ethical predicate or ought follows;” | standard boundary + non-implication | standard_boundaries: no-evaluation; does_not_show[0] (“No ought follows.”) |
| L8 “the constraint reading remains the AI’s, pending Ren.” | reading | correspondence (appended to the constraint sentence: “this reading remains the AI's, pending Ren”) |
| V0 “14 October 2026: the current bytes of Becoming.Feeding, Becoming.Continuation are bound to consolidated receipt 20261013T221720.428753Z (passed: 91 package modules, …)” | evidence | validation_scope (the binding receipt); the date and the counts stay in the receipt, the history entry of that binding and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence | validation_scope (“Earlier receipts checked the same statements under former names”); “plan section 10” → snapshot |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 30 theorems of Becoming.Interdependence all have empty axiom reports;” | evidence | validation_scope; the count (30) stays in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “The author's counterreview is in §56 of the integration note;” | evidence | validation_scope (“in the integration note”); §56 stays in history (the entry that added the record) and the snapshot |
| V7 “not yet independently reviewed.” | evidence | validation_scope |
| V8 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence + round label | law 3 states the local laws; validation_scope (“the local forms included”); P50 → history (existing entry) |
| V9 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence + round labels | validation_scope (“the local forms included”); P57–P61 → history (existing entries) + snapshot |
| V10 “P86 checked addition: core receipt 20261013T094743.528770Z checks Becoming.Feeding’s 41 theorems and all source declarations with empty axiom reports;” | evidence | validation_scope (Becoming.Feeding's theorems, with the binding of its current bytes from V0); P86 and the count → history + snapshot |
| V11 “periphery 20261013T095049.338744Z passes;” | evidence (duplicate of V4) | as V4 |
| V12 “study §107.” | provenance | history (the P86 entry names study §107) + snapshot |
| V13 “Historical scope is retained;” | evidence | validation_scope (“Earlier receipts checked the same statements under former names”) and the snapshot (the earlier record is the last text_versions entry) |
| V14 “the integration text has no independent review yet.” | evidence (duplicate of V7) | validation_scope (“not yet independently reviewed”) |
| R0–R2 “Route (b) is the AI's wording, which Ren quoted: “No axiom. … beyond them.” Ren chose: “let's aim for a first, then try to archive b”.” | Ren's words | correspondence (verbatim) |
| R3 “The author's reading (an AI argument, pending Ren): the feeding closure reads “what it actually depends on”.” | reading | correspondence (unchanged) |
| R4 “P40 also read it as Ren's “the system that one is in”, the system reached from a center along dependence;” | reading | correspondence (“P40 also read it” → “It was also read”; zh “P40 也把它读作” → “它也曾被读作”; P40 → history (existing entry) + snapshot) |
| R5 “P42 withdraws that reading: the feeding closure lies within the influence closure, … (see levels-of-closure; the AI's reading, pending Ren).” | reading | correspondence (“P42 withdraws that reading” → “that reading is withdrawn”; zh “这一读法由 P42 撤回” → “这一读法已撤回”; P42 → history + snapshot) |
| R6 “The names (FedClosed, WithinFeeding, Overshoot and others) are the AI's, chosen by Ren's naming standard.” | names | correspondence (unchanged) |
| R7 “The AI's second mechanism, “constraint: a part that degrades its whole removes its own supply”, is read here as a loss returning through a feeder.” | reading | correspondence (L8 appended) |
| R8 “Ren answered: “there could be the whole realizes itself … needs more thoughts”.” | Ren's words | correspondence (verbatim) |
| N0 “P86 adds exact boundaries for redundant giving, stock coverage and withholding within one flow;” | completed (not a next step) | laws 8–11; P86 → history (existing entry) |
| N1 “counterfactuals with responsive taking or activity, the origin relation for actual carrying, and a center’s recognition of the across-step closure remain open;” | next step | next_delta (stated as tasks: “State counterfactuals in which the remaining taking or activity responds; give the origin relation for actual carrying and how a center recognizes the across-step closure”, following the zh “其余取用或活动会回应的反事实”) |
| N2 “a model of selection between wholes (populations, replication);” | next step | next_delta (“model selection between wholes (populations, replication)”) |
| N3 “Ren’s judgment of the constraint reading.” | next step | next_delta (“The constraint reading is Ren's to judge.”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| H4 “P86 meets_after/over/stays_met supply balance … meets_without supplies WithheldLevels, local balance and no taking by the withheld part at that condition.” | premise | hypotheses[4] (up to “actual dependence.”) and hypotheses[5] (from “unfed_meets”), split to stay under the item cap; the round label “P86” (zh “P86 的”) dropped and kept in history and the snapshot; wording otherwise unchanged |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |

Remaining lint findings: the correspondence is over its length guide (en 1403/1200, zh 972/500). It quotes Ren's two English passages verbatim in both languages, about 550 characters each time, and the remaining sentences are attributions of AI readings. They are kept rather than moved out of the record.
