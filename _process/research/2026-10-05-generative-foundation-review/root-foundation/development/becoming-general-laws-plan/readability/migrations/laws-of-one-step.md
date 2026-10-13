# Migration map: laws-of-one-step

Old record sha256 `d9ab8f141df087225b80866f79ea67d7dda911c2b478ce6e5abeee4bc96c797e`; snapshot `_process/architecture/history/d9ab8f141df08722/laws-of-one-step.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T4 “The laws of one step, with their condition inside them: balance at a step fixes coming to …” | title (statement of the result) | title (short name) + statement; each clause is a law (T0 → laws 1–2; T1 → law 6; T2 → law 7; T3 → laws 9–10; T4 → law 13) |
| C0–C1 “Each law holds of every world;” | framing | statement (first clause); hypotheses[0] |
| C2 “The move made is localization: a premise selected for every step makes the condition hold …” | move made + corollary | law 15 (premise for every step → corollaries); does_not_show[0] (no premise derived) |
| C3–C4 “Balance at a step: the flow balances on a family across a step where each member's level a…” | law | law 1 |
| C5 “Arising needs an active giver: with balance at a condition across a step, it comes to stan…” | law | law 2 (its heading “Arising needs an active giver” leads law 4) |
| C6 “across a step at which nothing is taken from a balanced family, a member rises exactly whe…” | law | law 3 |
| C7 “a relatum embodied at both ends of the step and given to only by active formations arises …” | law | law 4 |
| C8 “nothing comes to stand from nothing across a step at which a family holding it is balanced…” | law | law 5 |
| C9–C10 “Rest: a family runs down across a step where it holds, without repetition, whatever stands…” | law | law 6 |
| C11 “Continued change needs openness, exactly: under a census of what stands, standing changes …” | law | law 7 |
| C12 “the general form is recurs_iff_unmet: where under a condition an event lowers an amount, t…” | law | law 8 |
| C13 “Running down bounds change: over any stretch, with no condition, what stands at its end wi…” | law | law 9 |
| C14 “the total rises only across steps that do not run down, so across steps that run down what…” | law | law 10 |
| C15–C16 “Ceasing needs arising: a list covers what holds at a step where every member holding there…” | law | law 11 |
| C17 “with a list holding exactly what holds at N (ListsAt) and nothing coming to be after N, wh…” | law | law 12 |
| C18 “ceasing recurring needs coming to be recurring wherever some list covers what holds at arb…” | law | law 13 |
| C19 “with no decision, where a list covers step N and nothing comes to be after it, ceasing doe…” | law | law 14 |
| C20 “Corollaries, their statements unchanged and their proofs now through these laws: the rest …” | corollaries | law 15 (the named corollaries are its declarations; “Becoming.Openness” → “the openness module”) |
| C21 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (hypotheses hold no ethical premise; receipt reports empty axioms for every cited declaration) |
| L0–L1 “No premise is derived: within the representation the premises remain contingent and indepe…” | non-implication | does_not_show[0]; the witnesses World.contingent, World.independent are not among this record's references, so the names stay in the snapshot |
| L2 “Running down bounding change is an inequality, its exact form being the identity of over_s…” | converse | does_not_show[1] (also X1 first sentence) |
| L3 “the recurrence laws and the bound use a census of what stands, and dropping it where infin…” | scope (representation) | does_not_show[2]; hypotheses[1] |
| L4 “the recurrence of law 1 and the bounds of law 3 use the least difference (option A), and w…” | premise + scope | “least difference (option A)” → hypotheses[2]; untested finer amounts → does_not_show[3]; “rest covered by the resolution line (R4)” → does_not_show[3] + related rest-at-every-resolution; next_delta |
| L5 “stated for discrete steps, coarser steps awaiting the localized Sampling and continuous ti…” | scope | standard_boundaries: discrete-steps; does_not_show[4]; “awaiting the localized Sampling” → next_delta |
| L6 “law 2's exact count needs a decision, its form that ceasing does not recur none;” | premise (representation) | hypotheses[2] (duplicate) |
| L7 “the name ‘closure bounds change’ is Ren's, and the proof shows that what bounds change is …” | non-implication | does_not_show[5] |
| L8 “the section on law 2 was drafted and verified by another session (0 axiom completeness);” | provenance | history (already in the P48 entry: drafted and verified by the session ‘0 axiom completeness’) |
| L9 “evaluates neither arising, ceasing nor rest;” | standard boundary | standard_boundaries: no-evaluation (“nor rest” is covered by “contains no ethical predicate”) |
| L10 “the names (BalancesOn, RunsDownOn, RunsDown, RunsDownClosed, Covers, ListsAt, NoneComes, r…” | standard boundary | standard_boundaries: names-provisional; the names themselves are the declarations of the laws and aliases; “the AI's choice” stays in the P48 history entry and the snapshot |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 57 theorems of th…” | evidence | validation_scope (receipt, the five modules, empty axiom reports); the per-module theorem counts stay in the receipt and the snapshot (the English 57 for Locality disagreed with the Chinese 44 and the receipt; noted in history) |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3 “It was first compiled from the prelude in a scratch tree, with no warnings and every #prin…” | evidence (scratch compile) | snapshot (the retained receipt carries the check); history P48 entry |
| V4–V5 “There is no independent review yet;” | evidence | validation_scope (“no independent review”, “author counterreview in §66”) |
| V6 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | round labels | history (P57–P61 entries) + snapshot |
| R0–R7 “The selection theorems ask which laws the counts obey under a selection of the eight premi…” | correspondence | correspondence (unchanged) |
| N0–N1 “Following the zero-premise plan: test whether each law survives amounts finer than whole u…” | next step | next_delta |
| N2 “the local restatements of the other class (a) laws (dependence, reserve and support), deli…” | next step + process instruction | next_delta (the laws to restate); “delivered by the session that claimed them and integrated here” is board process → snapshot |
| N3–N4 “the representation decisions of class (b) (Ren);” | next step | next_delta |
| H0–H1 “No global premise: the condition of each law is stated inside it, as a fact about the worl…” | premise | hypotheses[0], [1] (unchanged) |
| H2 “Representation: discrete steps and natural-number amounts; the least difference in dissipa…” | premise | hypotheses[2] (“law 2” → “ceasing needing arising”; L4 option-A use folded in) |
| X0 “World.sourcedQueue: the flow balances and is dissipative (which binds only closed families…” | counterexample | counterexamples[0] (unchanged) |
| X1 “Boundary: running down bounding change is an inequality, not an iff; what is exact is the …” | boundary (not a counterexample) | does_not_show[1] (inequality, exact identity), does_not_show[2] (census at the steps of a tail, representation of amounts), hypotheses[1] (laws of one step need no census; total standing a number) |
| X2 “Listed.lpo_of_few: the form in which ceasing does not recur needs no decision, but naming …” | counterexample | counterexamples[1] (“laws 1 and 2” → the two laws by name) |
