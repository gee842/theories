---
name: SSBX project state — Phase 4 终章 + Kleene axiom split (2026-05-08)
description: Phase 4 完成基线 + kleene_recursion_axiom 拆为 4 件具名原子公理 (2026-05-08)
type: project
originSessionId: c55c7f11-0b44-438a-8520-1b94e91d9763
---
As of commit `61acb9b` (2026-05-07), Phase 4 终章 was complete: 19 modules, ~5746 lines, 2823 build jobs, 0 sorry across the entire project.

**2026-05-08 update — Kleene axiom decomposition**: 原 monolithic `axiom kleene_recursion_axiom : KleeneInverter` (in `GodelLi.lean`) 已拆为 4 件具名原子公理 (in new `Foundation/Bagua/KleeneCarrier.lean`):
- `universalInterpExists` (~700-line YiInstr U engineering)
- `smnExists` (~50-line s-m-n compiler engineering)
- `kleeneFromPrimitives` (~100-line diagonal compiler engineering)
- `allDecidersAreYiComputable` (genuine Church-Turing meta-axiom for cuo-invariant Bool deciders — NOT eliminable in Lean)

`kleene_recursion : KleeneInverter` 现为派生定理 (via `KleeneInternal.path_to_zero_axiom`)，原 `kleene_recursion_axiom` 名以 `@[deprecated]` alias 保留向后兼容. 所有原"无条件"下游定理 (`halts_undecidable_internally` / `rice_four_images` / `rice_uniform` / `daoJudge_not_universal*`) 已移至 KleeneCarrier 命名空间。GodelLi.lean 仅保留 0-axiom 之 `*_under_kleene` 条件版定理。

Verified via `#print axioms kleene_recursion` returns the 4 named atomic axioms (no monolithic axiom).

**Why:** Net axiom count went 1 → 4, but each axiom is a precise, independently-削减able engineering target. Three of the four are concretely implementable in YiInstr; only `allDecidersAreYiComputable` is the genuine Church-Turing meta-axiom (cuo-restricted under 道理二分).

**How to apply:**
- Treat any new sorry/axiom as a regression — 0 sorry is the baseline; the 4 atomic axioms are now the audit surface.
- New code referencing `KleeneInverter`-derived results should `import KleeneCarrier` (not just `GodelLi`).
- Reducing the engineering debt: build `WenyanSelfInterp § 6b` further (currently ~15% scaffold) → discharges `universalInterpExists`. The path is mechanical but ~700 lines.
- The 4th axiom (`allDecidersAreYiComputable`) is **philosophically intentional** under 道-理二分, not technical debt — do not propose to "remove" it without re-reading `Foundation/Bagua/CuoInvariance.lean`.
- Phase-4 终章 batch added: `CatOp.lean` (Yoneda embedding as functor C^op → SetCat^C), `IIDWlln.lean` (IID-aware WLLN via Mathlib's `iIndepFun` + `IdentDistrib`), `BochnerPL.lean` (Bochner anchor + `IsPicardLindelof` instance).
