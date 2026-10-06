# Integration into the Lean generative model

6 October 2026. AI-authored implementation and review under [Ren's exact continuation request](../../../../sources/15-codex-theory-conversations/2026-10-06-lean-integration-no-added-assumptions.md). This extends the existing root study in place.

**Completed connection:** existing primitive event laws ↔ their endpoint-sensitive finite histories, with the Boolean structural classification expressed through the same Process/Trace API and tested under the existing synchronous composition. **No new primitive law, physical or ethical premise, or axiom is declared.** The original four model sources are unchanged. The complete assumption-free foundation and all six V7.3 mechanisms remain unresolved.

## What is now integrated

[GenerativeModel.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeModel.lean) is the public entry point. It imports the original model and the deeper-root proofs, and proves the combined statements rather than merely collecting imports.

[DynamicConsequences.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicConsequences.lean) introduces pointwise step equivalence and proves:

- two processes on the same carriers have the same primitive steps exactly when all finite traces with their starting and ending states agree;
- totality constructs a witness for each finite action word, without asserting totality of all processes;
- the already defined static and toggle processes have identical feasible words but different singleton endpoint traces.

[DynamicClassification.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicClassification.lean) uses that same step-equivalence predicate. It classifies the existing Boolean package exactly as the static or toggle description, and proves the alternatives exclusive. On these two states and one action, totality, determinism and invariance under all Boolean renamings already imply same-label reversal and unique predecessors. Those last two properties therefore need not be separate premises in this finite characterization.

The public module transports the classification into endpoint-history descriptions. It also proves a composition result: synchronizing either static or toggle with any other process on the common action alphabet still gives identical feasible action words. This follows from the core's existing product theorem; it does not claim that every possible coupling loses the state distinction. A coupling that observes actual state or consequences is not just the specified synchronization on action words.

This integrates a positive identification result, an exact finite classification, local premise reduction and a limit on what word-only information can recover. It neither chooses one physical dynamics nor excludes static systems from the general theory.

## What “no assumptions/axioms added” means in this change

No existing event law was altered. No target capacity, payoff rule, competence law, corrective authority or ethical ground was installed as a structure field or global assertion. The new definitions are a pointwise relation between existing processes and the public proof interface; the finite witness processes were already present.

The characterization theorems do not assert that all processes satisfy totality or the Boolean property package. They prove exact equivalences. Helper implications retain visible hypotheses; the concrete counterexample discharges the relevant properties using the existing static/toggle proofs. This is valid structural mathematics, not elimination of every condition in the broader explanatory theory.

Every newly audited theorem has an empty named-axiom dependency list. The original Depletion and RootRealization developments retain their historical use of propext and Quot.sound; those dependencies were neither added nor silently represented as absent. Lean's underlying type theory and the model's interpretation remain outside an empty dependency report. The [stronger no-assumptions requirement](ASSUMPTION-ELIMINATION-AUDIT.md) remains unmet.

## Verification and review

The default [check.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/check.py) now freezes and compiles twelve modules under pinned Lean 4.29.1. It includes the public entry point and all deeper-root modules. It checks:

- original four source hashes against the preserved earlier receipt;
- imports only from Std or earlier frozen modules;
- no proof placeholders, unsafe declarations, unchecked native shortcuts or custom axioms;
- an explicit dependency audit for every new theorem;
- no newly named axiom dependency for any audited theorem;
- source stability across the fresh build.

The [new receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification.json) reports **119 audited declarations: 20 new and 99 inherited**, zero new axiom dependencies, no warnings and successful compilation of all twelve modules. All 20 new lists are empty. The total includes the earlier 20-theorem symmetry extension. It is not a count of 119 newly derived foundation claims.

The [prior checker, receipt and logs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification-history/2026-10-06-before-model-integration/manifest.json) are preserved byte-for-byte with original paths and hashes. The deeper four-module receipt and the separate symmetry receipt remain untouched.

Separate source reviews checked the classification, law/history bridge and scope of the feasible-word counterexample. The main-entry/checker review is recorded in the accompanying integration checks. No prior market, learning or empirical study was rerun.

## V7.3 and the next unresolved connection

The [six-mechanism Lean interface audit](V73-LEAN-INTERFACES.md) identifies real reusable declarations and the missing mathematics. The present structural integration supports faithful treatment of continuation and retained distinctions; it does not derive V7.3's selection law, compounding returns, network dynamics, competence decay, strategic equilibrium or reform guarantees.

An inspected route to rational common-return cancellation through installed library lemmas would introduce named dependencies into a new theorem. It was not included. This is a limit of that inspected proof route, not a claim that constructive rational cancellation is impossible.

**Next root connection:** which occurrence and transformation claims the proposed generative root actually entails, now with exact distinctions between primitive laws, endpoint-sensitive histories and feasible words. **Next V7.3 bridge:** an exact common-return/selection interface for an existing selector with every dependency discharged at its advertised scope; generic composition alone does not produce that law. The patient-significance → independent-actor-reason investigation remains a separate unresolved justificatory connection.

A proposed account changes this assessment only by deriving additional explanatory content or by narrowing its claim in response to a counterexample. Ren's full requirement is not replaced by the completed local integration.
