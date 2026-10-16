# Indexed assembly and relational abstraction

7 October 2026. This continuation tests a concrete route toward mathematical admission: form a whole witness relation, then abstract witnesses having the same output. It also tests whether restricting completion to naturally indexed finite stages lowers the full-admission requirement.

The [fresh verification receipt](verification.json) records **31 new Lean theorems and 48 named declaration audits**, with only `propext`, `Quot.sound` and `Classical.choice`. Earlier proof packages remain unchanged. These are scoped mathematical results supporting a philosophical proposal; full admission and unique root constitution remain unresolved.

| Module | Theorems / audits | Result |
| --- | --- | --- |
| [IndexedAssembly.lean](formal/IndexedAssembly.lean) | 19 / 26 | Explicit finite parity recurrence and exact union; on `Nat`, finite admission plus closure under every increasing finite chain is equivalent to fullness. |
| [RelationalAssembly.lean](formal/RelationalAssembly.lean) | 12 / 22 | Witness quotient corresponds inversely to projected support, retaining its output map; conditional admission and direct parity connection. |

`parityStages` has no arbitrary target-predicate parameter. In contrast, `prefixChain S` explicitly depends on `S`, exposing how the unrestricted family range carries full strength even with countable indexing. The general theorem `parity_admitted` assumes that full-strength chain closure; it is not a weaker local admission proof.

The abstraction theorem assumes admission of the whole witness presentation, output-abstraction closure and inverse correspondence preserving the output map. It concludes admission of the support with its inclusion into the base. Membership in a separately specified predicate domain is a further correspondence obligation. All types in this interface occupy the declared universe `Type u`.

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/check.py
```

The checker rebuilds `IdealWarrant`, `CompletionRole`, `CompletionExamples` and `Admission` from receipt-matching frozen bytes, compiles both new modules, and checks each new named declaration's axiom dependencies. Warnings, errors, holes and unapproved axioms fail the run. Inherited declarations are not counted as new.

Read the [integrated assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-INTEGRATION.md), [indexed correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-LEAN.md), [abstraction correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-ABSTRACTION.md), [affirmative argument](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-ARGUMENT.md), [counterreview](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-REVIEW.md) and [primary-source assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ASSEMBLY-SOURCES.md).
