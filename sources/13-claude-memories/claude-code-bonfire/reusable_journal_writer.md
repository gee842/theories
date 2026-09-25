---
name: reusable-journal-writer
description: Use the phase-neutral architecture journal writer only when a structure-map claim changes
metadata:
  node_type: memory
  type: project
  originSessionId: 9f844dd8-aa5f-4f1a-bf9f-5d6eb466d23d
  modified: 2026-08-15T00:00:00.000Z
---

`scripts/architecture-shadow/write-architecture-change.mjs` is the reusable,
phase-neutral append writer:

```bash
node scripts/architecture-shadow/write-architecture-change.mjs \
  --change=<repository-relative-descriptor.json> --dry-run
```

Use it **only when a structure-map claim changes** (for example, an exact root
grant or another journal projection fact changes). A normal landing that does
not change such a claim writes no journal entry. Always dry-run first; publish
only after reviewing the proposed append, then run:

```bash
pnpm check:architecture-shadow
```

The writer reads the current journal head and publishes append-only leaves.
`packages/core/regression-source-closures/` remains live journal data. The
checker still validates chain integrity, root-grant law, and closure-store
references, but it no longer dereferences journal-named evidence or prepared
archive mappings; those are recorded digests, not filesystem obligations.

Gate budgeting, evidence restrictions, and deletion rules follow
[[verification-regime-2026-08-14]]. Do not recreate one-shot writers,
per-landing entries, evidence quartets, digest reseal rituals, or a separate
contract checker for the closure store.
