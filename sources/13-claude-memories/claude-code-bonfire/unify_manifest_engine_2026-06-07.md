# Manifest routing

`rt.yi.manifest({ kind: ... })` is the unified public row-authoring surface.
`packages/core/src/runtime/composition/yi-runtime-manifest.ts` resolves the
durable `core:kind` row, derives its write shape from composed traits, and then
selects distinct implementations because the routes have different authority
and row-shape rules:

- Spirit manifestation lives in
  `packages/core/src/runtime/composition/yi-runtime-manifest-spirit.ts`. The
  non-seed path uses Identity creation, subtree authority, and the durable kind's
  license; it has no process-local declaration fallback.
- Holding manifestation lives in
  `packages/core/src/runtime/composition/yi-runtime-manifest-holding.ts`. It
  selects the holding route from the resolved kind and sends every holding write
  through the canonical holding builder and mint chokepoint.
- Seed-only spirit and holding writes share the atomic row + `yi.manifested`
  helper in
  `packages/core/src/runtime/composition/occasion-manifest-write.ts`.

Do not revive the old claim that register-only kinds are universally
license-exempt. Current route-specific authority is the law. The former commit,
LOC, suite-count, and byte-identity history is not an operational contract;
verification follows [[verification-regime-2026-08-14]].
