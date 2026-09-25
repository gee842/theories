---
name: session-schema-artifacts-are-generated
description: packages/session/schemas/*.schema.json are generated from ENCOUNTER_JSON_SCHEMAS; regenerate with REGEN_FIXTURES=1, never by hand.
metadata:
  type: project
---

`packages/session/schemas/*.schema.json` are generated artifacts, not hand-written. Source of
truth is `ENCOUNTER_JSON_SCHEMAS` in `packages/session/src/schema-export.ts`.

**Corrected 2026-08-22.** This note previously claimed the guard lived in
`packages/session/test/schema-export.test.ts` as `describe("committed encounter schemas")`. It
did not — that file only exercises the in-memory schemas, and **nothing read the directory at
all**, so `CommandEnvelope` and `EventEnvelope` had silently drifted from source. Do not trust a
remembered guard without grepping for it.

The guard now exists at `packages/session/test/committed-schemas.test.ts` and self-heals:

```bash
REGEN_FIXTURES=1 npx vitest run packages/session/test/committed-schemas.test.ts
```

Two sibling artifact sets, all three now with the same `REGEN_FIXTURES=1` escape (ADR-031: a
guard should be a live check or not exist, and regenerating should be a command rather than a
transcription):
- `packages/engine-wire/test/engine-wire.test.ts` — structural (`JSON.parse` + `toEqual`).
- `packages/domain/test/schemas.test.ts` — byte-exact text compare.

Note `ENCOUNTER_JSON_SCHEMAS` carries a non-schema `wire` key (the version string); skip it when
iterating. Related: [[worktree-node-modules-trap]], [[r0-reset-progress]]
