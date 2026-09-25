---
name: ren-prefers-lean-process
description: "Ren pushes back on process ceremony — keep working docs minimal, put rationale in archives"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0d12c725-8d2a-4f05-9b71-22745c997f04
  modified: 2026-08-07T10:26:51.036Z
---

On the Context Runtime project (2026-08-07), after a review cycle grew CLAUDE.md from 64 to 81 lines of
governance (decision tiers, precedence rules, ratification ceremony), Ren said "I feel we are
overcomplicating this, aren't we? especially the CLAUDE.md." The slimmed 49-line version was the right call.

**Why:** It's a solo project; the real risks are agents re-litigating settled decisions or building ahead
of the current stage. Fixing doc inconsistencies by adding clauses is a ratchet — each review round adds
process unless actively resisted.

**How to apply:** When editing instruction files (CLAUDE.md especially), prefer deleting rules to adding
qualifiers. Keep rationale in archive files (decisions.md, ADRs, review records), not in per-session
instructions. Before adding a governance rule, ask whether the failure it prevents has ever actually
happened here.
