---
name: 2026-05-21-large-scale-doc-sync-merge-094db61
description: "Multi-agent doc audit + sync; 36 .md updated, 3 new files, merged into main; claims preserved verbatim, paths/counts/status annotations corrected"
metadata: 
  node_type: memory
  type: project
  originSessionId: 60cba10e-e303-4834-b561-ccbb9850a7f1
---

Multi-agent review + doc sync ran 2026-05-21 (commit `dbb0758`, merged to main as `094db61`).

**What triggered it**: user asked "我们都曾经设下过哪些目标？实现的都怎么样了；我们可以claim所有可说的都可以用这个框架表示，以及它们的组合可以用R tower operation表达？"

**Why**: docs were heavily stale (v3 1c76a55-era), referencing deleted `Foundation/Bagua/` paths, "0 sorry" / "3686 jobs" snapshots, etc. claim-status-ledger.md v0.8 (2026-05-21) is the only honest live status doc.

**Scope**: 10 parallel agents covered:
- root READMEs (3 files)
- docs-next/ nav (5 files)
- docs-next/00_start/{phase-status, 5 claim docs, 9 roadmap docs}
- docs-next/10_formal_形式/{module-map rewrite, 6 gap docs, 10 plan docs}
- docs-next/30_crosswalk_互证/* (6 files)
- NEW: `docs-next/10_formal_形式/heisenberg-weyl-narrative.md` (868 lines)
- Also new (from concurrent work): `power-4.5-{progress,scope-decision}.md` tracking Power 1999 §4.5 Path A

**Net diff**: 48 files, +3276 / -517 lines.

**Two key claim findings**:
1. **「可说 → 可表示」** holds only in T_GUT Core (3 ops factored out: square_mor / relate_mor / modal_V4_mor); `complete_*_of_adequate` is conditional on 4 hypotheses; 5 SMCC instances (Algebraic F₂ / Heyting / Topological / Witt / Quantum) closed; **Power 1999 §4.5 V-natural form still open** (scaffolding via PR #70).
2. **「组合 = R tower op」** has **no universal theorem** in code — only subclasses (R₄ bilinear forms, identity decompositions, RTower structural uniqueness via squaring law). User confirmed: claim sentences stay verbatim because they express **final target**.

**Crucial corrections to prior memory**:
- `Atlas/YiLegacy/` **never finalised** — code lives in `Atlas/Yi/` directly with `Classical/` subdir.
- Real `axiom` keyword declarations: ≤ 1 (only `kleene_recursion_axiom` in `Atlas/Yi/Classical/Diagonal/GodelLi.lean`). Prior framings of "3 axiom files (Quantum + FrmMonoidal + GodelLi)" conflated comment mentions with declarations.
- `~150-170 sorry` real count (top: `Order/FrameBimorphism.lean` 19, `Doctrine/Instance/Topological.lean` 7, `Enriched/Power.lean` 7).
- `Foundation/Squaring/` directory deleted; content split into `R/Squaring.lean` + `R8/Squaring.lean` + `Hierarchy/Operators/V4/` (10 sub-files).
- `V4Outer.lean` → `V4.lean` + `V4/` subdir.
- `theOne` is now `def`, not `opaque` (`Wen/Kernel.lean:189`).
- PR #70 scaffolding landed real enriched-Lawvere data structures; the plan's "Phase 1-4 Not Started" was outdated.

**How to apply**: For future sessions, **start with `docs-next/10_formal_形式/claim-status-ledger.md` v0.8** to get honest status before trusting any README/phase-status/roadmap. See [[reference-claim-status-ledger]] and [[reference-hw-narrative]].

Edit nuance: agent E wrote some edits to the wrong worktree (main repo on codex/gut instead of my worktree). Recovery via `git -C main diff > patch && git apply --3way`. See [[feedback-agent-worktree-discipline]].
