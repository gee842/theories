---
name: feedback-verification-economics
description: Workflow policy — implementation agents verify their own units; batch semantic review and integration at meaningful boundaries
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f4f96fdc-ce92-435d-b161-eb6b149700cf
  modified: 2026-08-15T17:39:47+07:00
---

Owner observed that separate verify stages dominate workflow token spend.
The useful policy survives: split verification by cost and defect class, not
by a ritual frequency.

**Why:** A separate verify agent re-ingests context to check one claim, while
the implementer already holds that context. Type checking and focused tests
catch many local defects cheaply. Semantic review is valuable when it covers
a coherent diff, not when it duplicates every mechanical check.

**How to apply:**
- Implementation agents run focused unit tests and `pnpm typecheck` for their
  own changes. Run `pnpm typecheck:tests` after renames. Do not spawn a
  separate verifier for claims these commands directly test.
- `pnpm test` is the database-free unit loop. Keep integration out of the
  inner loop; at a meaningful boundary run
  `PG_URL=postgres:///bonfire_test pnpm test:integration` when the changed
  surface reaches PostgreSQL.
- At a phase or release boundary, batch the coherent checks: `pnpm test`,
  `pnpm check:release`, the integration suite when applicable, and only the
  surviving structure gates whose named defect class the diff can trigger.
  Do not run or recreate a broad gate panel as proof of diligence.
- Review the coherent diff and what its tests actually assert. Dedupe findings
  and use adversarial or multi-agent verification only for audits or
  rework-forcing semantic judgments, not routine compilable claims.

The former pin-heavy and all-gates rationale is superseded by
[[verification-regime-2026-08-14]].
