---
name: yiinstr-cuo-equivariance-ceiling-v1-superseded-by-pr
description: Historical record — v1 12-instr ISA was cuo-equivariance-bounded. v2 (PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

> **⚠️ HISTORICAL — SUPERSEDED**
>
> This memory describes the v1 ISA doctrine (12 instructions, cuo-equivariance-bounded). It was **superseded by PR #37** (B' universal ISA, 2026-05-17, commit `7cb62e7`).
>
> **Current state (v2)**: YiInstr has 13 instructions (added `branchYaoYang (i target)` for absolute yao test). The cuo-equivariance ceiling is broken. ISA is now **universal Hex → Hex** compile via `WenDefCompile.compileHexFunCertified?` — `Stdlib.tuiBody` / `Stdlib.sunBody` / etc. now compile via propagate-carry/borrow adder (~26 instr each).
>
> The v1 "cuo-symmetry" theorem series in `BaguaTuring.lean` survives as **subset theorems** guarded by `complementEquivariantInstr` predicate / `AllEquivariant` program predicate. The 12 v1 originals satisfy these; `branchYaoYang` does not.
>
> See [[wen-restructure-complete-2026-05-17]] for the full migration story.

---

## v1 (historical, do not act on)

The 12-instruction `YiInstr` ISA in `Foundation/Bagua/BaguaTuring.lean` was **structurally constrained** to compute only cuo-equivariant Hexagram → Hexagram functions: every program `f` satisfied `f(h.cuo) = (f h).cuo`. Proven by structural induction (each primitive commutes with `Hexagram.cuo`).

Consequence (v1): constants like «一» and the successor function «生» = «加» «一» were **not implementable** in pure YiInstr.

**Why broken in v2 (PR #37)**: `branchYaoYang` does absolute yao test — its branch decision changes under `cuo` (yang ↔ yin flips affect the test outcome). This is the doctrine `WenDefCompile.lean` §「未尽之业」 v1 once warned against, now explicitly authorized.
