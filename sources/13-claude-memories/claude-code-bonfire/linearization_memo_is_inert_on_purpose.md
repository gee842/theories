---
name: linearization-memo-is-inert-on-purpose
description: "Identity's cross-owner linearization cache port is intentionally inert; do not confuse it with the live legacy Engine cache"
metadata:
  node_type: memory
  type: project
  originSessionId: c62ec623-0222-46a3-86bd-9b9cbfb4d35b
  modified: 2026-08-13T09:50:40.267Z
---

`currentIdentityLinearizationCacheGet` and `currentIdentityLinearizationCacheSet` in `packages/core/src/runtime/composition/operations/identity.ts` deliberately return `undefined` / do nothing. Identity recomputes from committed state rather than reusing another owner's process-local cache.

Do not generalize this into “linearization has no cache.” The compatibility Engine cache in `packages/core/src/engine/resolution/linearization-cache.ts` is live and bounded, with invalidations on grant-bearing holding changes. Kind installation clears that cache after a committed compatibility projection in `packages/core/src/engine/deployment/kind-build.ts`.

Why the Identity port stays inert: the effective-linearization key in `packages/core/src/identity/service/principals/spirit-linearization.ts` contains the principal's origin Kind plus active grant source uid/timestamp/Kind triples, but not the definitions of those Kinds. A sibling process can observe redeployed durable Kind rows while a process-local memo still holds the old chain. That chain participates in authorization, so cross-process staleness is a security error.

If Identity gains memoization, bind it to a transaction/request or to a committed shared Domain/epoch that changes with Kind definitions. A process-local generation counter is insufficient.
