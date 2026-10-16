# Migration map: closing-needs-net-draw

Old record sha256 `0af4518fde9bfcb072da26bbd2f67924acaf769c9bd5cdc5ccdde173ba662602`; snapshot `_process/architecture/history/0af4518fde9bfcb0/closing-needs-net-draw.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C11–C12 hold en C11, so later zh claim labels run one ahead; zh R0–R1 hold en R0, so later zh correspondence labels run one ahead).

Each law was read against its declarations in `Becoming/Admission.lean` (with `Becoming/Flow.lean` for `Flow.Balances` and `Flow.BalancesOn`); none states more than the declaration. Law 6, the reading by negation, is the old sentence C11 unchanged; it cites the two theorems it negates. Law 7 is written more exactly than the old next step N0, to match the theorems. N0 said “balance only at the conditions the formation requires, across the steps before t” for all four local laws. `Flow.withheld_at` asks balance only at the one condition compared (`∀ s, s < t → L.BalancesOn W [c] s`). The three boundary laws ask it at each condition `f` requires. The law now says “balance only at the condition compared, or at the conditions the formation requires”. This is neither narrower nor wider than the Lean statements.

| Old text | Type | New place |
|---|---|---|
| T0 “Closing needs a net draw” | title | title (unchanged) |
| S0–S2 “A part closes what can form only by a net draw on a required condition, …; a formation is supported exactly while its net draw is within the margin.” | statement | statement (unchanged) |
| C0–C1 “Levels l admit a formation f at t (Web.Admits) when …; support is admission by the levels that stand (Web.supported_iff_admits), and levels no lower admit whatever lower levels admit (Web.Admits.mono).” | definition + laws | law 1 (theorem names → declarations) |
| C2 “A part is a decided family of formations (part : F → Bool), a single formation or a system of them.” | definition | law 2 (unchanged); hypotheses[1] states it as a premise |
| C3–C4 “In the flow with the part withheld (Flow.withhold) …; the levels without the part (Flow.WithheldLevels) are the level path that balances this flow from the same start, unique where it exists (Flow.WithheldLevels.unique).” | definitions + law | law 2 (names → declarations) |
| C5 “Each step's taking and giving split into the rest's and the part's (Flow.taken_withhold, Flow.given_withhold; the part's are Flow.partTaken and Flow.partGiven).” | law | law 3 (names → declarations) |
| C6 “In a balanced flow the difference is exact (Flow.Balances.withheld): …” | law | law 3 (name → declarations) |
| C7–C8 “So the boundary is exact (Flow.Balances.supported_iff_within_margin): …; the part's cumulative net draw must stay within the margin by which the levels without it meet the need.” | law | law 4 (name → declarations) |
| C9–C10 “Hence where, up to t, the part has given each condition f requires at least what it took from it, … (Flow.Balances.supported_of_net_give); where the part has taken … (Flow.Balances.admits_of_net_draw).” | law | law 5 (names → declarations) |
| C11 “A part closes a formation that could form without it only through a net draw beyond the margin … (negating the equivalence; finding that condition uses classical logic), and opens one only through a net give.” | law (reading by negation) | law 6 (unchanged) |
| C12 “The comparison holds the rest of the exchange fixed, as the but-for test of Becoming.Joint holds the move fixed.” | relation to another result | related entry joint-difference-making (“Its but-for test holds the move fixed; this comparison holds the rest of the exchange fixed.”) and hypotheses[1] (“withholding it leaves the rest of the exchange unchanged”) |
| C13 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipt reports empty axioms) |
| L0 “Compares only the formations admitted at each step, not reachability over several steps, renewal capacity or richness of relations (which Ren also named: “renewal capacity, or richness of relations”);” | scope (with Ren's words) | does_not_show[0] (Ren's words verbatim) |
| L1 “the counterfactual does not let the rest adjust;” | scope | does_not_show[1] (hypotheses[1] states the premise) |
| L2 “where no level path balances the flow without the part there is nothing to compare;” | scope | does_not_show[1] (hypotheses[1] and counterexamples[1] state it too) |
| L3 “a part must be a decided family;” | premise (duplicate of H1) | hypotheses[1] (“A part is a decided family (part : F → Bool)”) |
| L4 “discrete steps and natural-number amounts;” | standard boundary + premise (duplicate of H3) | standard_boundaries: discrete-steps; hypotheses[3] (natural-number levels, needs and amounts) |
| L5 “contains no ethical predicate and does not say which part should be withheld;” | standard boundary + non-implication | standard_boundaries: no-evaluation; does_not_show[2] |
| L6 “names such as admission, withholding and net draw are the AI's wording, for Ren to choose.” | names | correspondence (joined to R5: “The reading and the names, such as admission, withholding and net draw, are the AI's; the names are for Ren to choose.”) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 46 theorems of Becoming.Admission and the 26 of Becoming.Regions all have empty axiom reports;” | evidence | validation_scope (with the binding receipt of the current Becoming.Dependence bytes, 20261014T091930.724493Z, from proof_bindings); the counts stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The author's counterreview is in §51 of the integration note;” | evidence | validation_scope (“in the integration note”); §51 stays in history (the entry that added the record) and the snapshot |
| V5 “not yet independently reviewed.” | evidence | validation_scope |
| V6 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence + round label | validation_scope (“the local forms included”); law 7 states the local laws; P50 → history (existing entry) |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence + round labels | validation_scope (“the local forms included”); P57–P61 → history (existing entries) + snapshot |
| R0 “Ren's first confirmed reading: possibilities are what can form next from what exists, and a formation's contribution is the future with it minus the future without it.” | Ren's confirmed reading | correspondence (unchanged) |
| R1–R2 | correspondence | correspondence (unchanged) |
| R3 “Ren said that “not harm” is “a phase transition with a clear boundary, not some "outside will or belief"”.” | Ren's words | correspondence (verbatim) |
| R4 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R5 “The reading and the names are the AI's.” | names | correspondence (L6 joined, see above) |
| N0 “The exact restatement for every world is this record's Flow.withheld_at, supported_of_net_give_at, admits_of_net_draw_at, supported_iff_within_margin_at (P50), the local condition inside the law: balance only at the conditions the formation requires, across the steps before t (Flow.BalancesOn);” | local laws appended to next | law 7 (local condition written as in the Lean statements, see above); P50 → history (existing entry) |
| N1 “the boundary stays an exact iff;” | law | law 7 (unchanged) |
| N2 “Flow.Balances.withheld, supported_of_net_give, admits_of_net_draw, supported_iff_within_margin are their corollaries;” | corollaries | law 7 (“the forms with balance everywhere are their corollaries”) |
| N3 “the margin where the rest adjust (the others' taking responding to the levels without the part; P65 states where the difference can go when the rest responds through its registration, comparison-where-the-rest-responds, and the exact margin under such a response is open);” | next step | next_delta (“State the margin where the rest adjust (…): comparison-where-the-rest-responds states where the difference can go …, not the exact margin under such a response.”); P65 → history (existing entry) |
| N4 “comparison of reachability over several steps;” | next step | next_delta (“Compare reachability over several steps”) |
| N5 “a formal link to the but-for test of Becoming.Joint.” | next step | next_delta (“link the comparison formally to the but-for test of Becoming.Joint”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |
