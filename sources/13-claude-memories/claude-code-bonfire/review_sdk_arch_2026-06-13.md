---
name: review-sdk-arch-2026-06-13
description: "Historical SDK architecture review; retain only its review-discipline lesson and current-use caveat"
metadata: 
  node_type: memory
  type: project
  originSessionId: f486b9fc-8c69-47a1-9027-76951ac0859c
  modified: 2026-08-15T00:00:00.000Z
---

This is a point-in-time review of `@bonfire/sdk` at commit `66c0aa84`, not a
current architecture map. Its adoption counts, file offsets, surface widths,
gate inventory, test totals, branch state, verdict, and remediation status are
intentionally omitted. Re-run the architecture review before using those
conclusions. Repository `CLAUDE.md` now governs verification; see
[[verification-regime-2026-08-14]].

**Durable review lesson:** an apparently unused, inert, or redundant contract
is a hypothesis, not a deletion finding. Trace every consumer and dispatch
path and attempt the change before classifying it; the original implementation
pass disproved several review findings that had inspected only one path.
