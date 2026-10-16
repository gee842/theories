# Migration map: exchanges-commute-unless-joined

Old record sha256 `21189426f2e0dadd9bb446c57e61d3ed184c5aeb4c170b30bd557c21a94c3c5a`; snapshot `_process/architecture/history/21189426f2e0dadd/exchanges-commute-unless-joined.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement:

- `Flow.Commuted` and `Web.Commuted`, with their `symm`.
- `Flow.swap_commuted` and `Web.commute_commuted` (under `Web.Split`).
- `World.commute_laws`: balance, dissipation and embodiment as iffs; `Dependent` where no dependence crosses the sides; `Acting` where no giver's activity is begun or ended by the other step.
- `Flow.Commuted.balances_iff`, `dissipative_iff` and `Web.Commuted.embodied`.
- `World.commute_counts`, over a stretch holding both steps. It needs `Decidable` activity in both worlds.
- `Reorders`, `Reorders.laws` and `Reorders.totals`.
- `Web.commute_dependent`, `Crossing.order_registers`, `Flow.Commuted.acting` and `Arising.order_registers`.
- `Footprinted`, `Footprinted.Contains`, `Footprinted.split` (exchanges not joined) and `Footprinted.reorder_premises`. The last covers seven premises as iffs, including `Transmitting`.
- `Reorders.counts` (decided activity in both worlds).
- `Crossing.reorders_joined` and `Arising.reorders_joined`.
- `listed_splice`, `Web.commute_census` and `Web.commute_standingCensus` (any sides), and `World.commute_counted_iff` (split sides).
- `Reorders.census` and `Footprinted.reorder_census`.

No law is wider than the old text. Law 4 writes out the decided activity in both worlds that `World.commute_counts` asks for; the old claim wrote it only for `Reorders.counts`. The `decidability` key is cited for both.

| Old text | Type | New place |
|---|---|---|
| T0 “Independent exchanges commute” | title | title (unchanged) |
| S0–S1 “Where sides split two steps, …; the order registers through a shared relatum or a dependence.” | statement | statement (unchanged) |
| C0–C1 “Flow.Commuted L L' t: …; Web.Commuted W W' t: … (Moved).” | law | law 1 |
| C2 “Both relations are symmetric (…) and are realized by Flow.swap and Web.commute … (Web.Split, Flow.swap_commuted, Web.commute_commuted).” | law | law 2 |
| C3 “Balance, dissipation and embodiment hold of the commuted world exactly where they hold of the world (…): the standing amounts exchange (Exchanged), …” | law | law 3 |
| C4 “Over any stretch holding both steps, the counts … are those of the world (World.commute_counts).” | law | law 4 (decided activity in both worlds written out, as in Lean) |
| C5 “Repeated, the commutations generate Reorders, … Mazurkiewicz trace equivalence, …” | law | law 5 |
| C6 “The order registers through dependence and through a shared relatum, each with a witness: … (Web.commute_dependent), and in Crossing … (Crossing.order_registers);” | law + counterexample | law 6; counterexamples[0] (unchanged) |
| C7 “only active relata giving holds after commuting … (Flow.Commuted.acting), and in Arising … (Arising.order_registers).” | law + counterexample | law 7; counterexamples[0] (unchanged) |
| C8 “With a footprint … (Footprinted, Footprinted.Contains), … (Footprinted.split), … (Footprinted.reorder_premises).” | law | law 8 |
| C9 “Along any Reorders, joined commutations included, … (Reorders.counts).” | law | law 9 |
| C10 “Plain Reorders, … (Crossing.reorders_joined) … (Arising.reorders_joined): these two premises carry exactly along commutations of exchanges not joined.” | law | law 10 |
| C11 “No premise.” | claim | law 10, closing sentence (“No premise is added.”; zh 不加前提 unchanged) |
| C12 “P88 continuation: listed_splice constructs the intermediate list …” | law | law 11; label → history (migration note) |
| C13–C14 “Every commutation preserves activity and standing censuses forward (…); the reverse direction requires split sides (World.commute_counted_iff).” | law | law 11 |
| C15–C17 “Thus every Reorders, … (Reorders.census). Arbitrary Footprinted.reorder preserves them forward; … (Footprinted.reorder_census).” | law | law 12 |
| C18 “This preserves census existence, not population at every intermediate step, and does not preserve the other premises under joined commutations.” | non-implication | does_not_show[3] (“does not preserve” read as the census law's non-implication: “it does not show the other premises preserved”; zh 也不推出 unchanged) |
| L0 “The original footprint reading is supplied;” | scope | does_not_show[0] |
| L1 “P88 constructs the least footprint with decided idleness (…), see least-footprint-where-idleness-decided.” | scope | does_not_show[0]; next_delta (pointer); label → history (migration note) |
| L2 “Running down is shown only at the two steps;” | scope | does_not_show[1] |
| L3 “census existence carries both ways along split-sided reorderings and only forward under arbitrary commutation;” | scope | does_not_show[2] |
| L4 “the readings are the AI's, pending Ren;” | names / readings | standard_boundaries: names-provisional; next_delta (the readings, Ren); correspondence (“Reading (the AI's, pending Ren)”) |
| L5 “no ethical predicate occurs.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 266 theorems of Becoming.Order all have empty axiom reports, among them …” | evidence | validation_scope (module and receipt); count and list → history (migration note) + snapshot |
| V1–V2 “The same receipt covers the package's 75 modules …; periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); counts → receipt + snapshot |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V4–V5 “The author's counterreview is in §102 of the integration note; there is no independent review yet.” | evidence | validation_scope; §102 → history (migration note) |
| V6–V7 “P88 census delta actually checked: all 101 OrderNormal theorems have empty axiom reports …; Reorders.census and its census constructions are bound to current source.” | evidence | validation_scope (Becoming.OrderNormal, “the census along reorderings included”); count and label → history (migration note); binding unchanged in proof_bindings |
| V8–V9 “Scope review is in §109; no independent full proof review.” | evidence | validation_scope (“a scope review of the census delta in the integration note; no independent review yet”); §109 → history (migration note) |
| (references, proof_bindings) Dependence.lean bound to receipt 20261014T091930.724493Z | evidence | validation_scope now names that receipt, which the proof bindings already used |
| R0 “P78 (work board), as above.” | process note | history (migration note) |
| R1–R3 “Reading (the AI's, pending Ren): …” | reading | correspondence (unchanged) |
| R4 “the converse that makes this exact is in order-of-exchanges-is-the-invariant.” | correspondence | correspondence (unchanged in English; the Chinese 使之精确的逆方向没有证明 corrected to 见 order-of-exchanges-is-the-invariant, matching the English and hypotheses[1]) |
| R5 “See the integration document §102.” | pointer | history (migration note); validation_scope (integration note) |
| N0 “The census along reorderings is incorporated here by P88;” | process note | laws 11–12; label → history (migration note) |
| N1 “the least footprint is in least-footprint-where-idleness-decided.” | pointer | next_delta; does_not_show[0] |
| N2 “Unbounded reorderings and continuous-time correspondence remain open.” | next step | next_delta (unchanged) |
| H0 “Commutation is of consecutive steps; …” | premise | hypotheses[0] (unchanged) |
| H1 “P78b already characterizes the converse … (order-of-exchanges-is-the-invariant); this is not a Foata simultaneous-layer normal form. The census reverse direction requires split sides, already part of Reorders.” | premise | hypotheses[1] (label P78b → the record name order-of-exchanges-is-the-invariant, which the sentence already cited) |
| X0 “Crossing and Arising: …” | counterexample | counterexamples[0] (unchanged) |
