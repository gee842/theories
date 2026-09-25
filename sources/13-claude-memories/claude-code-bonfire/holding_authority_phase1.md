---
name: holding-authority-phase1
description: "Current holding lifecycle authority decision boundary"
metadata:
  node_type: memory
  type: project
  originSessionId: 7a569679-3abb-47b9-a15a-ed062aa43592
---

Current facts, verified 2026-08-15:

- `decideHoldingLifecycleAuthority` is the pure decision law for burn,
  transfer, activate, and deactivate. Enforcement assertions and
  `explainWriteAuthz` consume the same resolved decision.
- `writeAuthzGate` represents holding lifecycle authority as a typed
  `holding-lifecycle` plan node, not synthetic Gate-ADT leaves.
- Mint remains multi-factor and I/O-backed through
  `resolveHoldingMintDecision`: authored add authority or license/builtin
  authority, issuer reach, and delegation-subject reach are resolved there;
  an opaque kit mint floor stays downstream.
- An authored relation `remove` gate is a distinct terminal burn-authority lane.

The design records now live at
`docs/yi/archive/25-structural-unification-execution-plan.md` and
`docs/yi/archive/26-holding-authority-contract.md`. Old branch/phase status and
suite counts are superseded by [[verification-regime-2026-08-14]].
