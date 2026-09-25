---
name: occasion-pg-representation-is-a-stub
description: "Superseded: the Occasion commit spine is live — production writes now commit through it in memory and PostgreSQL"
metadata:
  node_type: memory
  type: project
  modified: 2026-08-29
---

The old caution — that Occasion's PostgreSQL representation existed but no
production code called it — no longer holds. As of 2026-08-29
`commitOccasion` is called from
`packages/core/src/occasion/service/atomic-commit/coordinator.ts`, and every
normalized durable change (manifestation, Kinds binding mutations,
authored-state patches, Stream appends, workflow activation, package
operations) prepares effects and commits through that one Domain-scoped
coordinator. A live runtime probe shows real commits with `yi:<uid>` and
`kinds:<uid>/<binding>` effects.

Current source map: `packages/server/migrations/001_init.sql` defines
`occasion_commits`, `occasion_domain_heads`, `occasion_effects`, and
`occasion_checkpoints` (the numbered migration series is gone — there is one
baseline file). `packages/server/src/pg-occasion.ts` implements atomic
commit, head reads, checkpoint/replay, consumer positions, and retention;
query validation lives beside it in `pg-occasion-observation-query.ts`. The
integration suite is
`packages/server/src/occasion-commit-log-pg.integration.test.ts`.

The PG store still serializes commits with an `occasion:<domainId>` lock,
persists the canonical envelope uninterpreted, and lets Occasion's service
own decoding. Do not add value exports to the adapter SPI to move
canonicalization into the server adapter.

Reading committed history back is a separate matter — see
[[event-time-yi-fold-coverage-gap]].
