---
name: security_hardening_sweep_2026-06-24
description: "Current security invariants retained from the June sweep; old branch, count, ledger, and verification-ceremony claims removed."
metadata: 
  node_type: memory
  type: project
  originSessionId: f2e3c48a-74f6-4824-bb1a-20826a2d91fb
---

The old audit ledger, severity/count transcript, fail-pre/pass-post ritual, and
worker-cleanup advice are not standing process. Use ordinary regression tests
and the gate law in [[verification-regime-2026-08-14]].

Current verified security invariants:

- RPC handlers derive the effective caller from authenticated `CallCtx` via
  `requireCaller`; request options do not supply a replacement caller.
- Delegation-bearing holding mint resolves `delegation.subject` and calls
  `authorizeDelegationSubjectReach` before writing the certificate. The
  custody authority matrix covers peer denial and self/descendant admission.
- Migration import quarantines events for a foreign `yiUid`, pins imported
  event subjects to the migrating spirit, binds the signed `targetHost`, and
  checks source-side caller authority. These contracts live in
  `packages/core/src/operations/migration/` and its auth-hole tests.
- `core:sys-admin` and `core:license` are privileged authority kinds and never
  receive the built-in license bypass; see
  `packages/core/src/authority/service/licenses/policy.ts`.
- Full `yi.message` bodies on generic history/subscription paths are filtered
  per event against that event's session by
  `packages/core/src/runtime/invocation/message-floor.ts`. DAG sibling/path
  reads separately use the same membership policy through
  `callerMaySeeSession`.
- Initial and subscription replay are semaphore-limited and cursor-bounded;
  the live code is under `packages/server/src/ws/`, with DoS regressions in
  `packages/server/src/ws-dos-caps.fix.test.ts`.
- Sigil runner navigation, form, child-frame, and popup egress remain fenced by
  the CSP in `packages/sigil/src/runner.ts`, covered by
  `packages/sigil/src/navigation-fence.fix.test.ts`.

When an authorization defect is found, inspect sibling entry points and factor
the shared policy so runtime, RPC, replay, and read variants cannot drift.
