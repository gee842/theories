---
name: extension-model-tier-a
description: "Shipped Tier-A loader for trusted, operator-selected in-process handler modules"
metadata:
  node_type: memory
  type: project
  originSessionId: 362516f7-53e1-4cb3-ae71-75deaa9ae5d6
---

`packages/server/src/extensions.ts` is the shipped trusted extension loader.
`extensionSpecifiersFromEnv()` parses comma-separated `BONFIRE_EXTENSIONS`;
`loadExtensions(rt, { specifiers })` imports modules in order, resolves an
extension shape, and calls `register(rt)` fail-fast. `packages/server/src/cli/serve.ts`
runs it after `installPlatform`, and the loader plus `BonfireExtension` are
exported from `@bonfire/server`.

This is a deployment surface, not a wire surface or sandbox. Operator-selected
modules run in-process with full handler authority. Untrusted wire-authored
behavior remains restricted to validated DSL programs; `kind:'js'` is reserved
and rejected by the current handler registry.

Current references are `docs/operations/extensions.md`,
`docs/operations/env.example`, `packages/server/src/extensions.fixture.ts`, and
`packages/server/src/extensions.test.ts`. The DSL implementation now lives
under `packages/core/src/engine/dsl/`. These current paths and behavior
supersede the earlier branch status, fixed test counts, and moved-file
references under [[verification-regime-2026-08-14]].
