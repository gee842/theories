---
name: local_run_setup
description: Current local server/web startup — use a migration-compatible database and build before launching the web profile alone
metadata: 
  node_type: memory
  type: project
  originSessionId: 01e1a400-4c5f-45e5-bd78-6dbe85d3421f
---

Use `DATABASE_URL=<migration-compatible-local-db> pnpm dev`. The root `dev`
script runs `pnpm build` before starting the server and web app; the defaults
are server port 4100 and web port 5174. Set `PORT` for the web process if 5174
is occupied.

The ignored `.claude/launch.json` is local state, not repository truth. It
currently starts the profiles separately and points the server at
`postgres:///bonfire_v2_demo`; that database still has migration names the
current `packages/server/migrations/001_init.sql` through
`012_occasion_commit_log.sql` sequence does not recognize. The migration
runner refuses unknown recorded migrations, so select a fresh or compatible
database rather than dropping the seeded demo database.

When starting `pnpm dev:web` or the web launch profile alone in a clean tree,
run `pnpm build` first because several workspace exports resolve from `dist/`.
Vite proxies the app's HTTP, event, WebSocket, auth, and attachment routes to
`http://127.0.0.1:4100` by default. The current seed entry points are
`scripts/seed-hearth.ts` and `scripts/seed-mmorpg-demo.ts`.

This supersedes the July 2026 single-migration and `autoPort` claims.
