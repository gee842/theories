---
name: verification-regime-2026-08-14
description: "OWNER RULE — Bonfire's gate budget, behavior-not-bytes law, consumed-evidence rule, and unit/integration split"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2d43a652-e83f-4f1d-8236-4648e37788c6
  modified: 2026-08-15
---

`CLAUDE.md`'s **Gates** and **Build / test** sections are authoritative. This
regime supersedes older memories that require gate registries, evidence
quartets, checker fixtures, byte resealing, or red-suite ledgers.

## Standing rule

- Every gate names the defect class it prevents and who acts when it fails. If
  either answer is missing, delete it; do not create a retirement ledger.
- Adding a `check:*` name requires retiring one or the owner's explicit
  approval in that session. Derive the live namespace from `package.json`.
- Pin observable coverage and behavior, never source bytes, provenance,
  transcripts, or diagnostic counts. Derive structure facts from their owning
  record instead of duplicating them in a checker.
- No meta-gates, checker fixtures, or unconsumed evidence. Review enforces this.
- Journal only when a structure-map claim changes, never for an ordinary
  landing.

## Surviving machinery

`check:architecture-shadow` still validates the append-only chain, root-grant
law, and the live `packages/core/regression-source-closures/` store. It does not
open journal-named evidence paths or historical archive mappings. For a real
structure-map change, dry-run
`scripts/architecture-shadow/write-architecture-change.mjs`, publish the
append, then run `pnpm check:architecture-shadow`.

`pnpm test` is unit-only and database-free. Run PostgreSQL suites separately
with `PG_URL=postgres:///bonfire_test pnpm test:integration`; the integration
runner is serial and fails when `PG_URL` is absent. Fix or delete a suite the
series makes red; never maintain a red-suite ledger. Use `pnpm typecheck` and
`pnpm typecheck:tests` after renames, and read `package.json` for the current
`check:release` composite.

Current work starts at `docs/yi/49-structural-arc/HANDOFF.md`. Other numbered
Yi documents are under `docs/yi/archive/`; former plans, proposals, and design
notes are under `docs/archive/`.
