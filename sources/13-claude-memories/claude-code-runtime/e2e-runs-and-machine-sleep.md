---
name: e2e-runs-and-machine-sleep
description: This Mac sleeps during unattended Playwright e2e runs; wrap them in caffeinate -dimsu or failures are misread as flakes
metadata: 
  node_type: memory
  type: project
  originSessionId: adc2d69a-d287-4dcb-92b3-1363ae94d27d
  modified: 2026-08-14T04:09:39.548Z
---

Ren's Mac sleeps during long/unattended runs of the Encounter e2e suite
(`cd apps/web && node ./e2e/run-playwright.mjs`). A suspended run keeps counting
wall clock, so tests die on Playwright's 120s per-test timeout with **no assertion
failure**, and the suite reports an implausible duration — seen 34.9m and 3.9h for
a suite that takes ~1.1m.

**Why:** the symptom mimics a real flake. On 2026-08-14 a sleep-induced timeout in
`tenancy.spec.ts` ("attachments and independently bound surfaces stay scoped")
looked like a regression from an unrelated `apps/web` change; it was sleep.

**How to apply:** run the suite as `caffeinate -dimsu node ./e2e/run-playwright.mjs`
(plain `caffeinate -i` is not enough). Before believing any e2e failure, check the
reported suite duration first — anything far above ~1.1m means the run slept and the
result is void; re-run before diagnosing. When killing a stuck run, send SIGINT (not
SIGKILL) to the `@playwright/test/cli` process so global teardown removes the Next
server, effect worker, Temporal test server, and the `context_runtime_e2e_*` database.

Related: [[history-core-program]].
