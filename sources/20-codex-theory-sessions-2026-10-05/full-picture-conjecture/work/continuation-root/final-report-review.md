# Final report: mathematical and evidential review

Reviewed 2026-10-05: `outputs/conditions-for-continued-generation.md`, the current safety and progress proof memos, saved solver results, the hidden-progress review, queue calibration/comparison records, prediction freeze, and the conceptual bridge audit. No report or reference-source edits were made. No solver enumeration was rerun in this review. Output proof links were intentionally awaiting the parent's packaging step and are not treated as missing research.

## Verdict

The central result is supported: the finite declared game class admits an exact constructive characterization of sure protected recurrence, including hidden progress under partial observation. The separate arbitrary-set theorem concerns safety. The report distinguishes mathematical generality from a law selecting the world's mechanisms, and recurrence from semantic novelty. The queue comparison is correctly described as stipulated synthetic composition and implementation evidence, not empirical transport or a completed test of the earlier two-gate protocol.

Two local technical corrections are needed before delivery; neither changes the proved result.

### 1. State the safe domain in the displayed recurrence formula

At the paragraph defining CPre and the following equation, require the current state itself to lie in K and make the fixed-point domains explicit:

    CPre_K(T) = {s∈K : ∃ available a, ∅≠F(s,a)⊆T},
    W = νZ⊆K μY⊆K [(P∩CPre_K(Z)) ∪ CPre_K(Y)].

The current abbreviated display omits these restrictions. Taken literally on all states, it would include an unsafe current state that can immediately enter a winning safe region. The later sentence that unsafe states lose expresses the intention, but the exact formula should itself implement it. The proof memo and implementation already do.

### 2. Rank decreases between completed obligation rounds under hidden progress

Numbered certificate item 4 currently says that rank decreases between progress events and a progress event permits reset. Replace “progress events” there with “completed progress rounds,” and make clear that a hidden-progress round completes when all outstanding compatible histories have visited P. Equivalently, say rank decreases while the obligation set is nonempty and may reset after it becomes empty.

Under hidden progress, different actual paths can visit P at different times; rank reset at O=∅ need not coincide with a physical P visit on each individual path. The following report paragraph correctly explains the obligation mechanism, but the initial certificate should not suggest synchronized physical visits. Every completed round contains a P visit along each compatible path, which is enough for recurrence.

## Completed-result agreement

- Safety: 12,005 finite games and 100,842 explicit observation-policy-tree queries match `formal_continuation_checks.json`.
- Fully observed progress: two exhaustive classes contain 2,304 and 9,604 cases, plus 500 seeded cases and four edge examples; the report's qualitative count description matches `progress-check-results.json`.
- Hidden progress: 4,608 exhaustive plant/observation/safety/progress cases match `partial-progress-results.json`. The report accurately says extracted controllers were checked against concrete plant-and-memory cycles. General arbitrary-history strategy equivalence rests on the proof, not direct enumeration of all such strategies.
- Queue: 864 cells and 6,048 coordinates match exactly. The selected one-slot and three-slot failure probabilities are 3/4 versus 1 and 27/64 versus 9/64 respectively. The 132 of 144 coarse-state/policy comparisons exclude the deadline-aware fourth policy as stated. The saved freeze identifies the predictions as fixed before integrated target execution.
- The finite-label novelty claim is appropriately restricted. The report explicitly allows a finite controller to write indefinitely growing outputs into an unbounded medium. It does not infer semantic newness from recurring P or infer eventual universal exhaustion from a finite model.

## Source and assumption checks

The three main-report source links support the limited lineage claims made around them. Chatterjee–Doyen–Henzinger–Raskin was checked in its actual paper body, including its game definition and distinction between sure and almost-sure winning; the Grädel–Lücking–Naaf and Boker–Kupferman–Rosenberg bodies were read during the proof work. The report does not attribute the philosophical or empirical conclusion to those papers, does not claim historical priority, and uses no direct quotations. Source capsules in the supporting progress memo remain below 200 words each.

The proof memo's arbitrary-set postfixed-family/selector argument is valid under its declared choice and nonempty-transition assumptions. Its finite-action horizon interchange correctly uses nested nonempty subsets of a fixed finite action set, rather than requiring finite observation branching. Its losing-rank statement has the correct policy-dependent counterexample-path quantifiers. Its exact obligation-state memory count and finite-branching recurrence proof are consistent with the current report.

Physical affordability, computational realizability and the meaning of protection/progress remain explicit application premises. The report does not turn the queue coding agreement into evidence that these premises hold universally. No further material correction was found.
