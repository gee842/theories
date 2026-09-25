---
name: e2-two-commit-law-mechanism
description: "Operational core of check:kind-legacy-root-transition: watched-path dirtiness selects HEAD or HEAD^1 and clean-tree debt self-heals after one later commit"
metadata:
  node_type: memory
  type: project
  originSessionId: c62ec623-0222-46a3-86bd-9b9cbfb4d35b
  modified: 2026-08-15T00:56:41.847Z
---

`check:kind-legacy-root-transition` is live. In
`scripts/yi49/kind-legacy-root-transition/classification-archive.mjs`, Git
status over the classification record/tree and the three legacy roots
(`packages/core/src/compiler/declarations`,
`packages/core/src/compiler/relations`, and `packages/core/src/model/kinds`)
selects the comparison commit:

- a dirty watched path means `priorCommit = HEAD`;
- a clean watched surface means `priorCommit = HEAD^1`.

For each unresolved row within the current lifecycle horizon,
`assertLegacyUnresolvedConsumers` requires current reverse consumers to be a
subset of both the prior committed set and `baseline + authorized
replacements`. Authorization affects only the second predicate. Therefore a
landing that adds a consumer can fail when the tree becomes clean; one later
commit makes that consumer part of `HEAD^1` and self-heals the first predicate,
while a genuinely new or unauthorized edge continues to fail the second.

Diagnose the two comparisons separately. Admit only a real path relocation in
`scripts/yi49/kind-legacy-root-transition/consumer-replacements.mjs`; that
module enforces sorted, unique entries and no public replacements. Its former
provenance, digest, and count self-pins are gone. Do not restore those pins;
preserve the consumer behavior under [[verification-regime-2026-08-14]].
