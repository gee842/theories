# Deeper generative root: checked construction and underdetermination

**Now included in the main model build, 6 October 2026:** run the parent [check.py](../check.py) for the integrated twelve-module verification, including [GenerativeModel.lean](../GenerativeModel.lean), [DynamicConsequences.lean](DynamicConsequences.lean) and [DynamicClassification.lean](DynamicClassification.lean). These connect primitive laws to endpoint-sensitive traces, classify the existing Boolean structural package and derive two redundant requirements. The new public composition theorem preserves word-feasibility ambiguity under the core's synchronous product. All 20 new audits are empty; the original deeper checker and its four-module result below retain their historical scope. [Full integration and limits](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/LEAN-MODEL-INTEGRATION.md).

**Separate symmetry extension, 6 October 2026:** [DynamicSymmetry.lean](DynamicSymmetry.lean) strengthens the two-state countermodel: totality, determinism, unique predecessors, same-label step reversal and invariance under every Boolean bijection still permit both static and alternating laws. Read [DYNAMIC-SYMMETRY.md](DYNAMIC-SYMMETRY.md) for exact scope and reproduction, and the [separate receipt](dynamic-symmetry-verification.json) for its build. The original four-module checker and receipt below are preserved. This extension follows [Ren's no-assumptions directive](../../../../../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-directive.md); it establishes a finite obstruction, not an assumption-free generative foundation.

**Status, 6 October 2026:** four new Lean modules, 32 new audited declarations, all compiled with Lean 4.29.1 and empty reported axiom dependencies. The frozen build also recompiles the existing `GenerativeCore` and its 18 audited declarations: 50 total. These are conditional mathematical results, not a proof that reality has no starting commitments. This package is AI-assisted research developed in response to Ren's request to finish the deeper layer of the candidate foundation.

The named bridge is **supplied distinctions and admissible events → composed finite histories → exact declared continuation descriptions**. The proofs close this finite mathematical interface and exclude deriving nontrivial differences or a unique event law from binary product construction alone. They do not derive the supplied event law, its physical realization, learning, concern or a universally favorable direction.

## What is established

| Module | Exact contribution | Supplied inputs and limits |
|---|---|---|
| [ProductTower.lean](ProductTower.lean) | For every finite depth, iterating `X ↦ X × X` yields an inhabited type iff the seed is inhabited, and a subsingleton type iff the seed is subsingleton. The seed is a retract of each level through diagonal insertion and leftmost-leaf extraction; any seed distinction persists. | A seed type and binary-product construction. The result does not deny that a nontrivial seed can support more structured combinations; it excludes creation of inhabitants from an empty seed and multiple values from a subsingleton seed by this construction. Depth is a mathematical index, not derived physical time. |
| [DynamicUnderdetermination.lean](DynamicUnderdetermination.lean) | On identical `Bool` states and `Unit` event labels, an idle law permits no events, an identity law permits events without state change, and a toggle law always changes state and permits two-event return. A singleton carrier also supports a declared event without distinct endpoints. | These are explicitly supplied alternative laws on the same carrier, hence also on the same carrier's product tower. They show carrier/product information underdetermines these laws. They do not exclude deriving a law from additional premises. |
| [GeneratedPaths.lean](GeneratedPaths.lean) | The existing root's finite labelled traces induce the unique pointwise least reflexive-transitive endpoint relation containing the supplied primitive steps. Any state interpretation taking primitive steps into a reflexive-transitive target relation preserves reachability. With no primitive steps, the entire reachability relation is equality. | Supplied `Process.step`. The zero-length identity is a no-event history, not a spontaneous physical event. `Trace` retains the event word and enforces actual intermediate states; endpoint `Reach` then existentially forgets the word. The uniqueness claim concerns endpoint relations, not a free category or distinct path witnesses. |
| [HistoryRealization.lean](HistoryRealization.lean) | Any prefix-closed finite event-word language containing the empty word has a process realization using complete declared event-label histories as states. Its traces end at exactly the appended word, and its feasible words are exactly the supplied language. Every existing root process's finite-word language has such a realization. | The language is supplied. Full event-label history can be retained without a finite-memory assumption. Preservation is only finite existential word feasibility; original hidden states, branch identities, probabilities, observation capabilities and intervention powers are not claimed to be preserved. |

The two elementary list lemmas in `HistoryRealization` use direct structural proofs so the final dependency reports remain empty rather than inheriting `propext` through the standard library's versions. Empty dependency reports still presuppose Lean's underlying type theory, inference rules, definitions and theorem hypotheses.

## Integration with the existing root

The three dynamic modules import the current [GenerativeCore.lean](../GenerativeCore.lean); they do not introduce a competing definition of process or trace. `Reach` is defined as existence of an actual root `Trace`, so the least-closure theorem applies directly to that same interface. The history realization theorem is also stated in terms of the existing `Feasible` and `Trace`.

The earlier [operation/distinction monism proposal](../../../../../../sources/07-shengsheng-buxi/ssbx-repo/docs-next/10_formal_形式/wen-substrate/03-operation-monism.md) is preserved as source genealogy. This package checks new, explicit theorems about the product iteration; it does not certify older unlocated proof artifacts or promote all of the source's ontological interpretations into mathematical results.

The [governing research goal](../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md) remains broader. The next explanatory obligation is to identify the justified primitive transformations and causal state distinctions of actual mechanisms, then use their actual successors to derive regulation, competing response formation/retention and revision of selectors. A word-language realization certifies representability after the permitted words are supplied; it does not discover those words or supply their causal explanation.

## Reproduce and audit

From this directory:

```sh
python3 check.py
```

The checker pins `leanprover/lean4:v4.29.1`, freezes all four modules plus the current parent `GenerativeCore.lean`, and compiles them into a fresh temporary directory. It does not consume preexisting local object files. It rejects source-level proof holes, custom axioms, unchecked computational proof shortcuts and nonempty audited axiom dependencies. It verifies that the compiled sources did not change during the check.

[verification.json](verification.json) records the compiler, checker, toolchain, source and log SHA-256 digests, every audited declaration, and the result. Individual compiler reports are in [verification/](verification/). The checker and reports are evidence of the stated finite formal contracts; they do not establish interpretation in an empirical domain or the completion of the unified foundation.
