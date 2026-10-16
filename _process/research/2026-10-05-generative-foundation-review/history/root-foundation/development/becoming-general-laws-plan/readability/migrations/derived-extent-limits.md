# Migration map: derived-extent-limits

Old record sha256 `5232f6c27c4429c7d9b4f6482057944e4ddd137d3b4cad0e2a02ecfd6dcf4779`; snapshot `_process/architecture/history/5232f6c27c4429c7/derived-extent-limits.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Continuation.lean` (Downstream, Lone, Mortal and the Clearing flow), `Becoming/Standpoints.lean` (`Flow.FedBy`, the Clearing valuation and `Web.held_by_formations`) and `Becoming/Dependence.lean` (`Web.Supported`, `Web.UnderminingAt`). None states more than the declaration. Laws 1, 3 and 4 now say that each witness balances and that activity needs support (`balances`, `dependent`, which the old claim stated once for all four limits in C1); law 4 adds that Clearing's flow is dissipative, as C8 said. Law 2 keeps the Lone flow's balance and dissipation, which `Lone.fed_not_recurring` states.

The evidence paragraph is rebound to the receipts of the proof bindings. The old evidence named receipt 20261013T221720.428753Z for Becoming.Continuation and Becoming.Standpoints; the proof bindings now bind Becoming.Continuation to 20261014T141427.442103Z (rebound in the batch-5 history entry, the last before this migration), Becoming.Dependence to 20261014T091930.724493Z and Becoming.Standpoints to 20261013T094743.528770Z, each a reference of the record. The old receipt and its counts stay in the snapshot.

| Old text | Type | New place |
|---|---|---|
| T0 “Limits of the derived extent” | title | title (unchanged) |
| S0–S2 | statement | statement (unchanged) |
| C0 “Following a want for one's continuation gives reason to secure what that continuation needs;” | premise | hypotheses[0] (unchanged, which states it as a disclosed premise) |
| C1 “the extent so derived from the dynamics has four limits, each with a witness meeting balance and activity needing support.” | framing | laws 1–4 (one per limit, each naming the balance and the support of activity its witness states); the correspondence keeps “witnesses of these four limits” |
| C2–C3 “One way: in Downstream …” | law (witness) | law 1; counterexamples[1] (unchanged) |
| C4 “No source condition need recur: being fed is needed, and no source condition need recur (Lone.fed_not_recurring, see continuing-self-fed-from-beyond; the one source does all the conveying, so this does not show that no particular source formation is needed).” | law + non-implication | law 2 (written out as the declaration states it); the parenthetical limit → does_not_show[1] (witness Lone.fed_not_recurring) |
| C5–C6 “The horizon of the want: in Mortal …; without it the renewer and the successor continue at every step (Mortal.without_continues).” | law (witness) | law 3; counterexamples[1] (unchanged) |
| C7–C9 “The clearer: in Clearing … (Clearing.undermines_within_renewal).” | law (witness) | law 4; counterexamples[0] (unchanged) |
| C10 “The source requires nothing by stipulation;” | premise | hypotheses[3] (unchanged, which says the same) |
| C11 “the endings in these witnesses are stipulated in their activity, the witnesses show them consistent with balance, support and dependence, and the general theorems are where endings are derived.” | premise + scope | first clause → hypotheses[2] (unchanged); the rest → does_not_show[4] |
| C12–C13 “Along dependence the center is not derived from the dynamics: … (Flow.FedBy); only the clearer's continuation is fed, and only by the source (Clearing.fedBy_source).” | definition + law | law 5; the line itself → law 7 and statement S2 |
| C14 “With each formation holding and valuing its own events … so N_std and G0 fail;” | laws | law 6 |
| C15 “in the same valuation the clearer's event at step zero is related to it through the habitat, and transmission out of the clearer's own region along the formed relations fails (Clearing.center_not_derived).” | law | law 7 (“related to the dweller's”, the event `it` names) |
| C16 “So the line holds for an extent derived along dependence and fails for one derived along every formed relation.” | law | law 7 (“the line that the center is not derived from the dynamics”) |
| C17 “S0 ranges over living claims: … (Clearing.clearer_not_living).” | law | law 8 |
| C18 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “The witnesses are minimal;” | scope | does_not_show[0] |
| L1 “‘requirements derived here’ are those of this group of results, and stronger requirements (such as counting others' dependence) are not excluded, only not derived from wanting one's own continuation;” | scope | first clause → hypotheses[1] (unchanged, which defines them); the rest → does_not_show[2] (“only not among those derived here from wanting one's own continuation”) |
| L2 “the line on the center holds only for an extent derived along dependence, and not in a whole where dependence links every two lives;” | scope | does_not_show[3] (with R10; witness Clearing.center_not_derived) |
| L3 “that the source requires nothing is stipulated;” | premise | hypotheses[3] (unchanged) |
| L4 “the witnesses' endings are stipulated in their activity, and Mortal's ending is supplied;” | premise | hypotheses[2] (unchanged, which says both) |
| L5 “evaluates no clearer and does not infer that it ought to protect others;” | non-implication | does_not_show[5] |
| L6 “at which level harm is read is Ren's choice;” | correspondence | does_not_show[6]; next_delta keeps the level of harm as a step |
| L7 “the names (Downstream, Mortal, Clearing, clearer, dweller, successor and others) are the AI's choice under Ren's naming criteria of 10 October (…), and readings remain Ren's.” | standard boundary | standard_boundaries: names-provisional (“Names follow Ren's naming criteria of 10 October 2026; readings remain Ren's”); the names are the laws' declarations |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 52 theorems of Becoming.Continuation, the 22 theorems of Becoming.Standpoints all have empty axiom reports;” | evidence | validation_scope (rebound to the proof bindings' receipts; see above); the old receipt and counts → snapshot |
| V1–V2 counts and periphery receipt | evidence | receipt + snapshot |
| V3 “The author's counterreview is in §47 of the integration note;” | evidence | validation_scope (“in the integration note”); §47 is in history entry 0 |
| V4 “the independent review (CONTINUATION-GROUNDING-REVIEW.md) accepts its Lean, and its corrections are handled in §47.1–47.4 of the integration note.” | evidence | validation_scope (the review is listed under sources; §47.1–47.4 are in history entry 1) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the detail stays in the receipt and the snapshot |
| R0–R3 Ren's words, the AI analysis, “This result gives witnesses of these four limits.” | Ren's words + reading | correspondence (unchanged) |
| R4 “The plan took the fourth witness as a test: had the derived requirements forced standpoint neutrality, the center would follow from the dynamics.” | provenance | correspondence (“Taken as a test (…)”, the condition unchanged) |
| R5–R6 “The independent review (W8) found that the first witness's transmission conjunct follows from S0 and that flow and web predicates never constrain significance, so the test as posed could not fail; ‘the witness exists’ as a passed test is withdrawn.” | provenance + work-item label | correspondence (“the first witness could not fail: flow and web predicates never constrain significance, and its transmission conjunct follows from S0, as the independent review found; …”); W8 is in history entry 1 |
| R7 “The present witness includes closure along dependence: the clearer's significance passes to the events feeding it and still does not reach the dweller.” | reading | correspondence (“the present witness includes closure along dependence”); law 6 states the rest |
| R8 “Read along every formed relation, transmission out of the clearer's own region fails in the same witness;” | law (restated) | law 7 |
| R9 “in a whole where dependence links every two lives, S0 with N_rel along dependence gives G0 (…).” | reading | correspondence (unchanged) |
| R10 “So ‘the center is not derived’ holds where the derived extent runs along dependence and some living claim lies outside some wanting formation's dependence closure.” | scope | does_not_show[3] |
| R11 “The clearer is one form of the self the meta-attractor selects: …” | reading | correspondence (unchanged, with R12's “(an AI reading)”) |
| R12 “This is not a moral verdict on it (an AI reading).” | non-implication | does_not_show[5] (“It evaluates no clearer …”), which says the same; “(an AI reading)” stays on R11 |
| N0–N3, N5 | next steps | next_delta (“(a lineage's continuation)” dropped as a gloss on “a want across generations”, “the horizon of the want” → “its horizon”, “taken away” → “removed”) |
| N4 “a witness still fed at every step with one source formation taken away from the same world (the witness in which no source formation recurs is given: Successive.relay, see continuing-self-fed-from-beyond);” | next step + completed connection | next_delta (first part); the parenthesis is the completed connection held by history entry 34 (existing, Successive.relay) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X2 | counterexamples | counterexamples[0]–[2] (unchanged) |
