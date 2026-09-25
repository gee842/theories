---
name: phase-gates-stay-narrow
description: "Ren: Phase 0 harness was overbuilt (target drift) — keep phase gates narrow; verification must not become the optimization target"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5b71429d-275b-4cb1-a410-4b3ca58a37d5
  modified: 2026-08-14T15:57:02.240Z
---

2026-08-14, reviewing History Core Phase 0: the implementing agent drifted from "establish the baseline"
to "maximize acceptance-evidence strength" — ~7.8k lines of bench harness including ~1.4k lines of
self-tests *of the harness*, a 405-line process-group supervisor, a disposable-PG-cluster manager with
internally versioned contracts (v3), per-symbol repo inventories (~40k lines JSON), and a 10k-line
evidence artifact. Ren: "overdid Phase 0 due to optimization target drift… I don't want too much
verification and testing slow down us too much." Decision was keep-don't-revert (Phase 1 consumes the
artifacts; revert costs more than it saves) but the *pattern* must not repeat.

**Why:** The execution plan itself already forbids this (§2.1: the runner grows "只在出现真实 gate 时增量扩展",
no pre-built generic sandbox/database-ownership/lineage systems; §14.4 stop rules). Acceptance machinery
is instrumental; every line of it is maintenance drag that must stay green through nine more phases.
Solo project — the marginal defect caught by harness self-tests is worth less than the phase it delays.

**How to apply:** In later History Core phases ([[history-core-program]]): extend the existing runner
minimally per real gate; write NO self-tests for harness code (test the product, not the tester); run
only the suites the plan's gate section names for that phase, not ceremony beyond it; reuse Phase 0's
cluster/publication machinery as-is rather than generalizing it; don't grow inventory granularity. When
an acceptance requirement and forward progress conflict, surface the tradeoff to Ren instead of silently
building more verification. Same instinct as [[ren-prefers-lean-process]], applied to test/gate code.

2026-08-14 addendum: Ren observed the same drift in another project of his (gate-like structures, slowing
progress, and comments that read as written to "game training rewards"). So treat this as a standing
agent failure mode, not a one-off: also avoid correctness-narrating/justification comments (comments
state constraints, not advocacy), don't let existing ceremony in the codebase serve as license to produce
more of it, and treat deleting never-firing gates as legitimate work to propose.