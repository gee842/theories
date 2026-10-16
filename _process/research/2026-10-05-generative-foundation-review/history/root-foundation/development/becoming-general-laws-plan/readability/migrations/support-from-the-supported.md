# Migration map: support-from-the-supported

Old record sha256 `15742fd50cfedc408f792de8e7872aa20023580e8fb5adf4000f6cbc2ac166fb`; snapshot `_process/architecture/history/15742fd50cfedc40/support-from-the-supported.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (the labels align in both languages).

Each law was read against its declarations in `Becoming/Admission.lean` (with `Becoming/Flow.lean` for `Flow.Balances`, `Flow.Acting`, `Flow.BalancesOn`, `Flow.Balances.on`, `Flow.GiversSupported` and `Flow.Acting.giversSupported`, `Becoming/Dependence.lean` for `Web.Supported` and `Web.Dependent`, and `Becoming/Generation.lean` for `Web.Rises` and `Web.Falls`). Two wordings were made exact:

- C4–C5 said a formation “gains support only if a condition it requires rises” and “loses support only if a condition it requires falls”. `Web.GainsSupport.rises` concludes `¬ ∀ c, W.requires t f c → ¬ W.Rises t c`, and `Web.LosesSupport.falls` concludes `¬ ∀ c, W.requires (t + 1) f c → ¬ W.Falls t c`: not every required condition fails to rise (fall). Read as naming a condition that rises, the old wording is the classical form. Law 3 states the theorems' form (“cannot gain support with no condition it requires rising”), says that picking out the condition uses classical logic, and says “after the step” for the falling case, as the theorem quantifies over the requirements at t+1.
- C7 said the formation “gains support only where a supported formation taking part gives to a condition it requires”. `Flow.gains_from_supported` concludes the negated universal in the same way; law 5 says “cannot gain support while no supported formation taking part gives to a condition it requires”.

C8 said “no member is supported at any later step”; `Flow.unsupported_stays` concludes this for every `T + n`, step T included, and law 6 says “at T or any later step”. Law 7 adds “under the same premises” (`Flow.nothing_supported_stays` takes balance, Acting and Dependent, as C9's “of the whole” left implicit after C8). No law states more than its declaration.

The validation scope follows the current proof bindings: Admission, Change, Flow and Space are bound to receipt 20261013T094743.528770Z, Dependence and Generation to 20261014T091930.724493Z. The old V0 also counted the 26 theorems of Becoming.Regions, a module this record does not cite; that count belongs to the receipt.

| Old text | Type | New place |
|---|---|---|
| T0 “Support from the supported” | title | title (unchanged) |
| S0–S2 | statement | statement (unchanged) |
| C0–C1 “A formation gains support across the step from t (Web.GainsSupport) when …; it loses support (Web.LosesSupport) in the converse case.” | law | law 1 (names → declarations) |
| C2–C3 “Its requirements do not loosen across the step (Web.Unloosened) when …; they do not tighten (Web.Untightened) when …” | law | law 2 (names → declarations) |
| C4–C5 “Where its requirements do not loosen, it gains support only if a condition it requires rises (Web.GainsSupport.rises); where they do not tighten, it loses support only if a condition it requires falls (Web.LosesSupport.falls).” | law | law 3 (theorems' form, see above) |
| C6 “In a balanced flow where only active formations give (Acting) and activity needs support (Dependent), every rise is given by a supported formation taking part in the step (Flow.rise_given_by_supported);” | law | law 4 (names → declarations) |
| C7 “so a formation whose requirements do not loosen gains support only where a supported formation taking part gives to a condition it requires (Flow.gains_from_supported).” | law | law 5 (theorem's form, see above) |
| C8 “Under the same premises, if no member of a family is supported at T, …, then no member is supported at any later step (Flow.unsupported_stays);” | law | law 6 (“at T or any later step”) |
| C9 “of the whole, once nothing is supported, while requirements do not loosen, nothing is supported or active again (Flow.nothing_supported_stays).” | law | law 7 (“under the same premises” made explicit) |
| C10–C14 “Each premise is needed, with a witness for each (Restoring) in which a formation unsupported at step zero is supported at step one: a requirement dissolves (Adapting, requirements loosen); something beyond the family gives (Inflow, a giver requiring nothing gives to the required condition); a giver is not active (Idle, Acting fails); an active giver is not supported (Carried, Dependent fails); a rise is given by nothing (Spontaneous, balance fails).” | law (witnesses) | laws 9 (C10–C11: “Each premise of the absorbing end is needed …”; Adapting and Inflow) and 10 (C12–C14: Idle, Carried, Spontaneous), each witness named in the sentence with the premise that fails; the witness names and the restores theorems → declarations. The statements match the theorems: Adapting `¬ web.Unloosened 0 false`, Inflow `0 < flow.give 0 true ()` with `true` requiring nothing, Idle `¬ flow.Acting web`, Carried `¬ web.Dependent`, Spontaneous `¬ … Balances web`; each has a formation unsupported at step zero and `web.Supported 1 false` |
| C15 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses contain no ethical premise; the bound receipts report empty axiom lists) |
| L0 “Stated for discrete steps and natural-number amounts;” | standard boundary + premise | standard_boundaries: discrete-steps; hypotheses[3] (unchanged, natural-number amounts) |
| L1 “the threshold results compare one step, and the absorbing end needs requirements not loosening and, for a family, only members giving to what members require;” | premise (duplicate of H2) | hypotheses[2] |
| L2 “the witnesses are minimal, their activity and requirements stipulated, and are shown consistent with balance, support and dependence, or each missing one premise;” | scope | does_not_show[0] |
| L3 “the whole is all the formations of a web, the represented whole;” | scope | does_not_show[1]; correspondence (R4, unchanged) |
| L4 “contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L5 “reading support gained only from the supported as the continuation of becoming continuing itself, and the absorbing end as the irreversible side of degeneration, is the AI's reading, pending Ren;” | reading | correspondence (R1–R2 give both readings as “The author's reading (an AI argument, pending Ren)”); standard_boundaries: names-provisional |
| L6 “the names (GainsSupport, Unloosened, Restoring and others) are the AI's wording, for Ren to choose.” | names | standard_boundaries: names-provisional; correspondence (R7) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 46 theorems of Becoming.Admission and the 26 of Becoming.Regions all have empty axiom reports;” | evidence | validation_scope (current bindings, see above); the counts stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The author's counterreview is in §51 of the integration note;” | evidence | validation_scope (“in the integration note”); §51 stays in history (the entry that added the record) and the snapshot |
| V5 “not yet independently reviewed.” | evidence | validation_scope |
| V6–V7 “This record's local laws (P50) are in the same receipt, with empty axiom reports. This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“the local forms included”); P50 and P57–P61 → history (the P50, P57 and P63 entries) + snapshot |
| R0–R7 | Ren's words + readings | correspondence (unchanged) |
| N0 “The exact restatement for every world is this record's Flow.rise_given_by_supported_at, gains_from_supported_at, unsupported_stays_at, nothing_supported_stays_at (P50), the local condition inside the law: balance at the required conditions across the steps used (Flow.BalancesOn) and their givers supported there (Flow.GiversSupported);” | completed result | law 8 (names → declarations; “the required conditions” made exact as “the conditions concerned (the condition that rises, or those the members require)”, since `Flow.rise_given_by_supported_at` takes balance at the rising condition; the whole's local form takes activity needing support only of the formation and step concluded, which law 8 says); P50 → history + snapshot |
| N1 “Flow.rise_given_by_supported, gains_from_supported, unsupported_stays, nothing_supported_stays are their corollaries;” | completed result | law 8 (“The global forms are their corollaries”; `Flow.Balances.on` and `Flow.Acting.giversSupported` in declarations); dependency laws-of-one-step (unchanged) |
| N2 “reachability and recovery over several steps (the conditions of transformation by a dissolved requirement and of giving from beyond);” | next step | next_delta (“Give reachability …”) |
| N3 “an instance theorem to the support-gated law of RelationalRenewal;” | next step | next_delta (unchanged; no such instance theorem was found among the records or the spine modules) |
| N4 “comparisons of renewal capacity and richness of relations.” | next step | next_delta (unchanged) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |

Remaining lint findings: the Chinese correspondence is over its length guide (547/500; the English is within it, 1195/1200). It quotes Ren's English phrases verbatim (192 characters), without which it is within the guide (355); the remaining sentences are the attributed AI readings. It is kept rather than moved out of the record.
