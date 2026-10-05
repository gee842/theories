# Necessity of an entire generated inquiry theory

6 October 2026. AI-authored continuation of Ren's 慧根 claim under the governing generative foundation. [Research argument and exact scope](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/HUIGEN-GENERATIVE-CLOSURE.md).

**Status:** a fresh Lean 4.29.1 build passes 27 new declaration audits and rebuilds 23 inherited declarations. This establishes the explicit conditional mathematical claims below. It does not establish that the full proposed philosophical basis is necessary for every scientific philosophy.

| Module | Checked content |
|---|---|
| [GenerativeClosure.lean](GenerativeClosure.lean) | Soundness of finite derivations with root and local premises; necessity of the entire generated closure iff necessity of every basis premise; conditional conclusions with undischarged locals; justified local discharge; rejection by countermodel; safe reuse of proved lemmas; one-premise negative witness. |
| [InquiryFamilies.lean](InquiryFamilies.lean) | Exact clipped-observation threshold answerability; pairwise distinct capability predicates; exact spending traces on the inherited process core; reserve/horizon exclusions; joined implication with two explicit local hypotheses; two universal formulas and every threshold/horizon instance in their generated theory. |
| [GenerativeCore.lean](../GenerativeCore.lean), [Depletion.lean](../Depletion.lean) | Existing process, trace and strict-depletion results rebuilt from recorded source bytes; not counted as new results. |

The eight finite inference constructors are basis use, local assumption, implication introduction/elimination, conjunction introduction/two eliminations and natural-number universal instantiation. Formulas are semantic predicates `World → Prop`; this selected sound fragment is not an effective syntax, complete proof search or characterization of every scientific inference. The formula interpretation and the necessity of a philosophical basis are not hidden inside a definition of scientific inquiry. A substantive necessity application requires a nonempty independently identified inquiry class; otherwise necessity is vacuous. Standard axiom dependencies (`propext`, `Classical.choice`, `Quot.sound`) are reported per module in [verification.json](verification.json), with exact per-declaration output in [verification/](verification/).

The operational families use explicitly supplied observation and spending laws. A threshold decoder exists exactly when its query threshold is below the clipped channel's capacity. One is exhibited in the sufficiency proof; its material construction is a separate task. A spending word is feasible exactly when its length is no greater than starting fuel. The finite root has two quantified formulas; their instances concern distinct tasks and capacities at arbitrarily large finite indices. No one finite agent is asserted to execute infinitely many inquiries.

## Reproduce

Run `python3 check.py` in this directory. The checker uses the already installed pinned compiler, freezes current source bytes, compiles all four modules in a new temporary directory and checks the reported declaration dependencies. It rejects proof holes, custom axiom declarations, unsafe declarations, unchecked native decisions and compiler warnings. It verifies that source bytes did not change during the check. It writes only this package's report and compiler logs; no dependency is installed.

## Genealogy and limits

The prior [root-of-wisdom synthesis](../../../../../../sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/root-of-wisdom-synthesis.md) already supplies sound unbounded extension and the qualified arithmetic-incompleteness argument. This package does not reprove incompleteness or claim that deductive soundness is newly discovered. Its contribution is a premise-tracked necessity interface and a concrete unbounded operational family on the current generative core.

Local hypotheses remain in the consequence's antecedent until justified. The entire theory cannot inherit necessity from an unsupported root, and no causal production of a belief certifies its truth. The source and machine checks establish no empirical calibration, ethical standing, physical infinity, unique ontology or completed wisdom.
