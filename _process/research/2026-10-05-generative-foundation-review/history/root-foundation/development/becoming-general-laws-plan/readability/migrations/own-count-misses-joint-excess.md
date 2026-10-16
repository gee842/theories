# Migration map: own-count-misses-joint-excess

Old record sha256 `24dd5753edc43fa167d6a750585d049ab4eda3cf79fe0bbe51c4a7dea4ca96d3`; snapshot `_process/architecture/history/24dd5753edc43fa1/own-count-misses-joint-excess.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement:

- `Flow.WithinOwn` (`∀ f ∈ present, take ≤ given`) and `Flow.WithinJoint` (`taken ≤ given`).
- `Pair.own_not_joint` and `Pair.no_web` (`¬ ∃ W, flow.Balances W`).
- `Flow.joint_keeps`, `excess_lowers` (`level (t+1) + 1 ≤ level t`) and `excess_bounded` (`level (T+n) + n ≤ level T`).
- `Flow.stays_below`, which needs balance, `Acting`, `Dependent` and the gate.
- `Flow.ends_below` and `Flow.joint_excess_ends`, which start from `level T < n + m`. A formation depending at a need of at least `m` is inactive at every `T + n + k`.
- `Exceeding.all_end` (`∀ n f, ¬ active (2 + n) f`) and `Alone.all_continue`.
- The local forms `joint_keeps_at`, `excess_lowers_at`, `excess_bounded_at`, `stays_below_at`, `ends_below_at` and `joint_excess_ends_at`.

None is wider than the old text. Law 1's English now states `WithinOwn` as a condition on every formation taking part, as Lean and the old Chinese do. The old English began “A formation's take … is within what is given when no formation taking part takes more”, which named one formation's take but defined the condition for all.

| Old text | Type | New place |
|---|---|---|
| T0 “Counting one's own draw misses joint excess” | title | title (unchanged) |
| S0–S2 “Formations each taking within what is given can together exceed it; …” | statement | statement (unchanged) |
| C0 “A formation's take from a condition across a step is within what is given when no formation taking part takes more than the step gives the condition (Flow.WithinOwn);” | law | law 1 (worded as a condition on every formation taking part, as in Lean and the Chinese) |
| C1 “the formations take jointly within what is given when … (Flow.WithinJoint).” | law | law 1 |
| C2 “Each can take within what is given while together they take more (Pair.own_not_joint).” | law | law 1 |
| C3 “In a balanced flow, taking jointly within what is given keeps the level (Flow.joint_keeps);” | law | law 2 |
| C4 “a step of joint excess lowers it by at least one (Flow.excess_lowers), so … (Flow.excess_bounded), and … no web balances the flow (Pair.no_web).” | law + counterexample | law 2; counterexamples[1] (unchanged) |
| C5 “Where every formation giving to the condition depends on it at a need of at least m, … (Flow.stays_below), and … (Flow.ends_below);” | law | law 3 |
| C6–C7 “so n consecutive steps of joint excess from a level below n + m end the renewers …; a taker not depending on it, or depending at a lower need, can continue (Flow.joint_excess_ends).” | law | law 4 |
| C8–C10 “In Exceeding a renewer gives two units …; … (Exceeding.all_end; the ending is also stipulated in its activity, …); with one taker … (Alone.all_continue).” | law + counterexample | law 5; counterexamples[0] (unchanged) |
| C11 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and natural-number amounts;” | standard boundary + scope | standard_boundaries: discrete-steps; does_not_show[1] (natural-number amounts) |
| L1 “the gated conclusions hold only for renewal that depends on what it renews, not for renewal given from an outside source such as a sun;” | scope | does_not_show[0] |
| L2 “excess compares totals at each step and treats neither reserves nor delayed renewal;” | scope | does_not_show[1]; next_delta (reserves and delayed renewal) |
| L3 “Exceeding and Alone are minimal witnesses, Exceeding's ending is stipulated in its activity and shown consistent with the laws;” | scope | does_not_show[2] (witness Exceeding.all_end) |
| L4 “the joint count binds only a want that outlasts what the condition holds, and a taker ends with it only where it depends at such a need;” | scope | does_not_show[3] |
| L5 “the link to the periphery's wear law is interpretive;” | correspondence | does_not_show[4] (joined with R3–R4) |
| L6 “contains no ethical predicate and does not say which taker ought to take less;” | standard boundary + non-implication | standard_boundaries: no-evaluation; does_not_show[5] |
| L7 “the names are the AI's wording, for Ren to choose (WithinOwn, WithinJoint, Exceeding, Alone and others).” | names | standard_boundaries: names-provisional; next_delta (names, Ren); the list of names → history (migration note) + snapshot |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 52 theorems of Becoming.Continuation all have empty axiom reports;” | evidence | validation_scope (module and receipt); count → receipt + snapshot |
| V1–V2 “the same receipt covers the package's 91 modules …; periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); counts → receipt + snapshot |
| (proof_bindings) Flow.lean bound to receipt 20261013T094743.528770Z | evidence | validation_scope now names that receipt, which the proof bindings already used |
| V3 “The author's counterreview is in §47 of the integration note;” | evidence | validation_scope; §47 → history (migration note) |
| V4 “the independent review (CONTINUATION-GROUNDING-REVIEW.md) accepts its Lean, and its corrections are handled in §47.1–47.4 …” | evidence | validation_scope (“the independent review of the continuation grounding”); review file stays in references; section numbers → history (migration note) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V6–V7 “This record's local laws (P50) … (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record's local laws”); labels → history (migration note) |
| R0 “Ren's proposal says that the self can become rigid and “has to count the dynamics …”.” | correspondence (Ren's words) | correspondence (unchanged; Ren's words verbatim and attributed) |
| R1–R2 “The periphery's wear law has the same phenomenon: …; This result states it on the spine, …” | correspondence | correspondence (unchanged) |
| R3–R4 “No instance theorem joins the two models; the link is interpretive.” | correspondence | does_not_show[4] (with L5) |
| R5–R7 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R8–R10 “A formation that wants its continuation … must count the joint draw …; … (Mortal, see derived-extent-limits). This is what the want requires, not a verdict passed on it.” | reading | correspondence (unchanged) |
| N0–N1 “The exact restatement for every world is this record's Flow.joint_keeps_at (P57), …; Flow.joint_keeps is its corollary;” | law | law 6; label → history (migration note) |
| N2–N3 “the exact restatement for every world is this record's Flow.excess_lowers_at, … (P50), …; … are their corollaries;” | law | law 7; label → history (migration note) |
| N4–N6 “instance theorems to RelationalRenewal's support-gated law and the periphery's wear law; joint excess under reserves and delayed renewal; shares and attribution (responsibility does not follow).” | next step | next_delta (unchanged), with “names (Ren)” from L7 |
| H0 “Balance: …” | premise | hypotheses[0] (unchanged) |
| H1 “The gate: …” | premise | hypotheses[1] (unchanged) |
| H2 “Excess is counted on totals at each step, not on shares; …” | premise | hypotheses[2] (unchanged) |
| X0 “Each within what is given is not enough to continue: …” | counterexample | counterexamples[0] (unchanged) |
| X1 “A description in which joint excess goes on for ever is the flow of no balanced web: …” | counterexample | counterexamples[1] (unchanged) |
