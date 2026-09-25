---
name: Sigil (miniapp runtime)
description: Current sandboxed miniapp runtime, React adapter, and Bonfire bridge
type: project
originSessionId: 9e42d102-57d4-4067-9ea6-cbaeebc08f71
---

Sigil is Bonfire's sandboxed miniapp runtime. The live packages are
`packages/sigil` (`@bonfire/sigil`), `packages/sigil-react`
(`@bonfire/sigil-react`), and `packages/sigil-bonfire`
(`@bonfire/sigil-bonfire`). `docs/sigil/README.md` is the entry point.

The host compiles a structured `SigilSource` envelope
`{ id, entry, files, sdks?, version?, meta? }` with `esbuild-wasm`, mounts it
in a sandboxed `srcdoc` iframe, and exposes only registered SDK calls over the
channel. Core transport is behind the `Channel` interface in
`packages/sigil/src/types.ts`; the React package owns mounting/lazy UI, and the
Bonfire package owns the host SDK bridge. `<LazySigil>` and `IdbCache` are
shipped, so the old deferred-feature list and scratch plan are not current.
Sigils ship both as message content blocks and as held first-class rows.
