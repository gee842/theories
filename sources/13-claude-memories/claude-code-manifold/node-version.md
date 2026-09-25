---
name: node-version
description: "This machine's default Node 23.11 is unsupported; prefix repo commands with the nvm v22.22.2 PATH"
metadata:
  type: reference
---

The repo needs node `^22.19 || >=24`; the machine default is Homebrew v23.11.0 (outside the range, and its `node:sqlite` lacks fts5). Prefix every node/pnpm command with `export PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH"`. Known residual on v22.22.2: `ExperimentalWarning: SQLite` on stderr, and `import-without-cache@0.4.0`'s loader hook fails (blocks dev-web/HMR — documented skip). Related: [[manifold-project-state]].
