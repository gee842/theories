---
name: sdk-elegance-core-resolution-2026-09
description: Plan 53 (docs/yi/53-lean-core-and-elegant-sdk) is the active work order as of 2026-09-02 — lean Core + elegant SDK; Plans 49–52 done; two audit findings drive it
metadata:
  type: project
---

As of 2026-09-02, Plans 49–52 are complete (protocol 168, Core/SDK 0.3.0,
commit 1953aa710). Plan 53 is the active work order:
`docs/yi/53-lean-core-and-elegant-sdk/README.md` plus eleven numbered
sub-plans (01 World product service, 02 one Authority lane, 03 Core public
constitution, 04 Core leanness, 05 SDK grammar, 06 authoring compression,
07 SDK entrypoints, 08 remote capabilities, 09 Server adapters, 10 Std
purity, 11 cutover to protocol 169 / 0.4.0, 12 semantic core: Yi row,
Kinds, compiler, manifestation). The exploration ledger it
distills is `docs/architecture/sdk-elegance-exploration.md`.

Two audit findings the owner should keep in mind: World product semantics
have two diverging owners (`packages/sdk/src/world/runtime-product.ts`,
`packages/server/src/methods/world/catalog.ts`), and the older certificate
evaluator `resolveDelegation` ignores conjunctive selectors and audience,
so narrowed certificates are World-wide on RPC reads, manifestation,
API-key auth, and typing signals until sub-plan 02 lands.

Revised 2026-09-03 after two independent reviews (coherence; adversarial
verification). Fixed decisions now in the README: Core shell `world`
(`@bonfire/core/world`, `bindWorld`, `WorldAccess` with one certificate);
every World operation, reads included, runs under the certificate envelope
with per-row selector filtering for listing reads; `define`/`undefine` live on
an opened namespace and upsert by family (no `update`, no `retire` verb);
`extends` lowers to `composes`; portable certificates (no "token" naming);
registry keys (`KindFamilyKey`, `KindActionKey`); action schema once on the
definition, handlers attach by key; 12 keeps the immutable record store
(`adapters/kinds/revision-binding/pg.ts`, `memory.ts`) and deletes only the
rollout control plane and its eight tables. Sub-plan 12 defaults to option C
unless the owner records otherwise. Effort estimates roughly doubled.

**Why:** the owner wants one semantic implementation under both transports
and an SDK whose elegance is not a façade over duplicated Authority law.

**How to apply:** execute sub-plans one per agent session in the README's
phase order; keep every landing green; stage only owned paths; the owner
commits. See [[feedback-owner-manages-commits]], [[shared-repo-concurrent-sessions]],
[[verification-regime-2026-08-14]].
