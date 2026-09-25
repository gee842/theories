# User prompts from Claude Code project -Users-ren-repos-context-runtime-product

sessions: 3  long prompts (>=200 chars): 1  chars: 976

---
[2026-08-24T20:56] session 4650f593

In the context-runtime-product repo, packages/dsh-product-client/src/client/tree-view.tsx has a stale doc comment on NodeDetail (around lines 543-547): "The shipped `explain` surface sits in the per-message action row and its own header records the compromise: …". That per-message explain seat (ExplainAction) was deleted in the WP4 "chrome shrinks to one chip" pass (commit dbc2337); PRODUCT_SURFACES now has three rows and the tree is the only surface with a per-node read. Rephrase the sentence historically, matching the package's existing idiom — see packages/dsh-product-client/src/client/node-actions.ts lines 12-17 ("v1's `explain` surface…") and the just-fixed comment in packages/dsh-product-client/test/node-actions.test.ts around line 135 ("v1's `explain` seat was the per-message action row…"). Comment only, no behaviour change. Gate: pnpm test (18 files / 108 tests), pnpm typecheck, pnpm exec biome check . (0 errors, 4 pre-existing noUnusedImports warnings).
