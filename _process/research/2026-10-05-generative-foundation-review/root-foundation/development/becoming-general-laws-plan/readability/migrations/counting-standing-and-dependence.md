# Migration map: counting-standing-and-dependence

Old record sha256 `6bcd7abe2a747e79378ecb08598e83a008804b677890702b987416f7c58366dc`; snapshot `_process/architecture/history/6bcd7abe2a747e79/counting-standing-and-dependence.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

| Old text | Type | New place |
|---|---|---|
| T0–T2 “The laws of counting what stands and what depends: under each selection the laws of counti…” | title (statement of the result) | title (short name) + statement; T0 → law 4, T1 → laws 5–11, T2 → law 13 |
| C0–C1 “Read of standing (Web.StandingCensus): a census of what stands lists at each step, once ea…” | definition | law 1 |
| C2 “Where every relatum is embodied, what stands is what is active: a census of what stands is…” | law | law 2 |
| C3–C4 “Where embodiment is not selected, a queue fed from a source meets every other premise what…” | witness | law 3 (“the driven queue” → “a queue fed from a source … its driver”; balance and dissipation kept) |
| C5–C6 “its census of what stands counts what the queue counts (World.sourcedQueue_standing, World…” | law | law 4 |
| C7 “Enclosure bounds what stands with no premise on activity: under a balanced, dissipative fl…” | law | law 5 |
| C8 “A selection bounds what stands where it selects balance and dissipation (World.BoundsStand…” | definition | law 6 |
| C9 “So with every step from some step on enclosed, a property of the counts holds of every cen…” | law | law 7 |
| C10 “a change bound is a law there exactly where balance and dissipation are selected (World.en…” | law | law 8 |
| C11 “Where balance is selected without embodiment the witnesses are waiting queues: closing que…” | witness | law 9 |
| C12–C13 “closing at the first step a waiting queue is enclosed at every step and meets every premis…” | witness | law 10 |
| C14 “Every step of a finite world is enclosed, so under each selection the laws of counting wha…” | law | law 11 |
| C15 “the new witness is a ring each of whose places is active throughout and stands while held,…” | witness | law 12 (“the new witness” → “the finite witness”) |
| C16 “Read of dependence (Web.DependenceCensus): with requiring decided, the premises add nothin…” | law | law 13 (World.DependsObey, already in references, names the counts of dependence) |
| C17 “in a finite world dependences are pairs of relata, at most the square of their number (pai…” | law | law 14 |
| C18 “Members of a queue, or places of a ring, depending on a common condition while in it, each…” | witness | law 15 |
| C19 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps, with finitely many standing and finitely many dependences at ea…” | representation | standard_boundaries: discrete-steps; hypotheses[0] (finitely many standing and dependences at each step) |
| L1 “needs decidability (a logical commitment) and pointwise properties (in place of function e…” | standard boundaries | standard_boundaries: decidability, pointwise-properties (also hypotheses[0], [1]) |
| L2 “the laws of counting what stands and what depends where each selected premise binds are no…” | scope | does_not_show[0] |
| L3 “joint laws of the three counts are not stated;” | scope | does_not_show[1] |
| L4 “the witnesses use members standing without acting and a source acting without standing, wh…” | scope | does_not_show[2] |
| L5 “it does not evaluate coming to stand, ceasing to stand, forming or dissolving;” | standard boundary | standard_boundaries: no-evaluation (“forming or dissolving” is covered by “contains no ethical predicate”; correspondence R7 keeps the full sentence) |
| L6 “the names (StandsObey, DependsObey, BoundsStanding, sourcedQueue, waitingQueue, activeRing…” | standard boundary | standard_boundaries: names-provisional; the names are the declarations of the laws; “chosen by the AI” stays in the P47 history entry and the snapshot |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 37 theorems of Be…” | evidence | validation_scope (receipt; the modules with empty axiom reports); counts and named theorems stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules (including the import-only root and the b…” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt) |
| V3–V4 “There is no independent review yet;” | evidence | validation_scope |
| V5 “The checker also verifies core purity: the import closure of the core (GenerativeCore, Inq…” | evidence (core purity) | validation_scope (one clause); the injEq/propext detail stays in the receipt and the snapshot |
| V6 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Locality listed); the round label P48 stays in history |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | round labels | history (P57–P61 entries) + snapshot |
| R0–R7 “The laws of counting activity (whole-law-of-counting, counting-under-enclosure) read what …” | correspondence | correspondence (unchanged) |
| N0 “The exact restatement for every world is laws-of-one-step (P48), of which this record's bo…” | cross-reference | law 5 (“both are corollaries of the laws of one step”); the round label P48 stays in history |
| N1–N2 “the local restatements of the laws of dependence and the other laws of what stands follow …” | next step | next_delta |
| H0 “Listing and decidability: as in whole-law-of-counting; read of standing, a positive level …” | premise | hypotheses[0] (with L0's finitely many at each step) |
| H1–H2 “Pointwise: as in whole-law-of-counting, in place of function extensionality, a hypothesis …” | premise | hypotheses[1], [2] (unchanged) |
| X0–X2 “World.sourcedQueue: without embodiment what stands and what is active part, and a relatum …” | counterexamples | counterexamples (unchanged) |
