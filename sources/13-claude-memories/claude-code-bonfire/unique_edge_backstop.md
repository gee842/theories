---
name: unique-edge-backstop
description: "Relation multiplicity is enforced by declared policy plus a reservations table; the core:unique-edge marker family is retired"
metadata:
  node_type: memory
  type: project
  modified: 2026-08-29
---

`core:unique-edge`, `core:unique-outgoing-edge`, `core:unique-incoming-edge`,
and `core:mutual-edge` are **retired**. They survive only inside
`RETIRED_ROUTE_MARKERS` in
`packages/core/src/compiler/declaration-ingress/compile-one.ts`, which
rejects a declaration that names them.

Multiplicity is now declared on the Relation itself and lowered to
reservations:

- `relationReservationPlan` in
  `packages/core/src/relations/service/relations.ts` reads
  `definition.policy.unextinguished.perPair / perFrom / perTo` and
  `policy.activePerTo`, and returns the reservation kinds to hold.
- PostgreSQL enforces them with the `relation_reservations` table in
  `packages/server/migrations/001_init.sql` — primary key
  `(binding_id, reservation_kind, reservation_key)`, kinds `pair`, `from`,
  `to`, `active-to`, cascading from `relation_occurrences`.
- `canonicalRelationCreateEndpoints` orders mutual endpoints before effect
  preparation so an unordered pair reserves one key.

There is a single baseline migration (`001_init.sql`); the old numbered
migrations, `packages/core/src/engine/`, and `packages/core/src/model/`
paths this memory used to name no longer exist.
