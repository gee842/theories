---
name: lineage-tab-client-bundle
description: "Where the Lineage tab lives, how its bundle reaches the browser, and the tail-not-head rule for displaying ids"
metadata: 
  node_type: memory
  type: project
  originSessionId: fc7bad38-c77b-4fc8-b4f8-926b65b339de
  modified: 2026-08-24T10:18:20.715Z
---

The Lineage tab (and all Harness UI surfaces) live in
`context-runtime-product/packages/dsh-product-client`: `tree-layout.ts` is the pure
DOM-free layout (asserted over real boxes in `test/tree-layout.test.ts`),
`client/tree-view.tsx` the SVG view, `client/index.tsx` the cordis registration.
The browser is served the **prebuilt** `lib/client.js` — after editing, run
`pnpm bundle` in that package or the running app keeps the old UI. The product
server (product-web, port 4000) is often already running from Ren's own use;
attach a browser tab to it rather than restarting, and a freshly spawned boundary
runtime picks up the rebuilt bundle.

Display rule (v3, 2026-08-24, after Ren's "can't really make sense of this"): every
id in this system keeps its constant part at the **front** — ULIDs open with their
mint time, DSH session ids with `session-` — so short forms must slice the **tail**
(`shortId` in tree-layout.ts), and lanes are labelled by upstream's
`SessionSummary.displayTitle` (reached via `ctx.sessions.list.getSnapshot().byId`),
never by an id prefix. Fork edges are drawn git-style: swing into the child's lane
within one row, then a vertical rail — not full-span beziers.
