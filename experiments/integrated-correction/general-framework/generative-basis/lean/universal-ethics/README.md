# Universal meta-ethics: checked warrant and coverage interfaces

7 October 2026. This package supports the active goal of proving universal meta-ethics of all intelligence. **The universal ethical ground is not yet proved.** These modules verify declared inference and composition requirements; they do not introduce a moral truth by definition.

## Verified scope

- `WholeGroundCoverage.lean`: 27 theorems. Arbitrary-type, Prop-valued least-closure semantics; exact target coverage; compatible local reason claims composing across scopes; exact projection to one history; explicit failures of scope coverage and isolated-scope analysis.
- `CutCoverageAudit.lean`: 12 theorems. Reverse-closed anchor-free cuts, their constructive relation to reachability, decidable upgrades, and equivalence of the unrestricted upgrade to double-negation elimination.

The fresh Lean 4.29.1 run checks **39 theorems and audits all 61 top-level declarations, with empty axiom dependencies**. See [the receipt](verification.json); its referenced retained run includes exact source snapshots, compilation logs and generated declaration audits. This is a statement about logical dependencies of those declarations. Their explicit seed, transport, compatibility and target hypotheses still require interpretation and justification.

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_universal.py
```

The checker pins `leanprover/lean4:v4.29.1`, uses a fresh temporary build directory, snapshots source bytes, audits each named declaration and checks that source did not change during verification. It does not reuse project `.olean` files. Its lightweight source scanner is scoped to these modules' syntax; kernel compilation and declaration audits are the proof checks.

## What the representations preserve

Positions can represent fixed reason claims at occurrences within a generative history. They must retain reason kind, ground, response and applicability context; physical occurrence equality alone does not establish sameness of reason. History indices prevent splicing in another history's seed, but the intended reference of an index remains an interpretation obligation.

`Seed` means an independently warranted instance, not whatever an agent currently values. `Edge` means a justified implication preserving the complete ground at its stated scope, not mere causal contact. `CompatibleGrounds` states agreement about the same claim on an overlap, not agreement about every different concern that can occur there. Target membership must be specified independently of what the proof reaches.

All main theorems admit infinite types. The finite examples are counterexamples to proposed logical shortcuts, not empirical models or the scope of the universal theorem. Unary rules do not replace conjunction: arguments requiring multiple independent premises need their actual inference structure preserved.

## Genealogy and logical qualification

The least-closure/coverage theorem formalizes the inherited [reason-transport argument](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/HUIGEN-REASON-TRANSPORT.md). The new integration interface checks local agreement, alternating scopes and same-history reference together. The constructive audit distinguishes Prop-valued interpretation from the old Boolean-valued formulation and absence of reverse-closed cuts from the old explicit incoming-crossing condition. It does not announce a failure of the earlier classical theorem.

The [research integration](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md) states the remaining normative obligations and the next substantive argument. Ethical warrant, all-intelligence correspondence and the full goal remain unresolved.
