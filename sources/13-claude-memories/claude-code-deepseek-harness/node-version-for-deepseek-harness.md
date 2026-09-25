---
name: node-version-for-deepseek-harness
description: "This machine's default Node 23.11 is unsupported by the repo; use nvm's v22.22.2 for generators/tests"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2821d33d-4056-4b0b-a667-30e526437804
  modified: 2026-08-26T10:17:18.291Z
---

The deepseek-harness repo requires Node `^22.19 || >=24`. This machine's default `node` is Homebrew v23.11.0 (`/opt/homebrew/bin/node`) — outside the range, and its `node:sqlite` lacks the fts5 module, which crashes `gen-tool-catalog` and anything opening the session-query SQLite index (`SessionQueryError ... no such module: fts5`).

**How to apply:** prefix repo commands with `export PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH"`. Known residual on v22.22.2: `ExperimentalWarning: SQLite` on stderr makes 3 `examples/acp-agent` snapshot tests fail (they assert empty stderr) — environmental, not a code defect. Related: [[deepseek-harness-working-style]]
