---
name: Phase γ progress (2026-05-15)
description: Foundation/{Yi,Bagua}/ retired; Atlas/Yi/ has 18 modules + Classical/ in 5 clusters; 4 commits, 6/53 consumers migrated
type: project
originSessionId: cf6a07ef-8ca3-4a88-8fcd-004cad5499d5
---
Phase γ of v0.6 R-Family restructure — 4 commits this session, **substantial but not complete**:

**`835ce29`** — relocate Foundation/{Yi,Bagua}/ → Atlas/YiLegacy/
**`a386a11`** — reorganize YiLegacy/ → Atlas/Yi/Classical/{Core, Algebra, Cells, Computation, Diagonal}/
**`e780941`** — port Cell128/Cell256/Sheng + Positions/legacy aliases (1230 LOC)
**`5f69769`** — Wave 1+2: 7 new R-Family modules + 6 consumer migrations (2891 LOC)

**Current Atlas/Yi/ shape**:
```
Atlas/Yi/                              ← R-Family side (18 modules)
├── Names, Bagua, Hexagrams (64), 
│   ShiV4, Operators, DaoSource, 
│   Diagonal, Positions, Sheng,
│   Cell128, Cell256, BenZheng,
│   Stratify, YiCore, Tradition, 
│   ShiBridge, WenSpec, YiInstr
└── Classical/                         ← Classical side (15 modules, 5 clusters)
    ├── Core/      Yi.lean (1985 LOC), YiCore.lean
    ├── Algebra/   BaguaAlgebra, BenZheng, CuoInvariance, Newman
    ├── Cells/     R7, R8, R8Stratify
    ├── Computation/ BaguaTuring (YiInstr 12-instr), BaguaWenSpec,
    │              ChunkedDecide, FuelDiscipline
    └── Diagonal/  GodelLi (kleene_recursion_axiom), KleeneInternal
```

**Consumers migrated to R-Family (6/53)**:
- `Foundation/Lang/{L2_SiXiang, L6_Hexagram, L7_Cell128, DaoJudge, Wuchang}.lean` (γ2-Lang)
- `Foundation/Wen/WenyanSyntax.lean` (γ2-Wen)
- Plus 10 import prunings in Modern/Text/Truth

**Build**: 3809 jobs, 0 errors, 0 sorry.

**Why Classical/ not deleted**:
4 parallel γ2 migration agents (Wen 19f, Lang 7f, Modern+Text+Truth 12f, Eight+Hierarchy+Jian+Core 14f) found that 47 remaining consumers have **cross-cluster downstream coupling**: each agent's scope blocked because consumers outside their cluster (Confucian, V4/Orbit/Atlas/Turing, Bridges/V4Time, RootRuleKernel, MetaInterp/*, etc.) pin to Classical types via transitive imports. Per-cluster agents revert when downstream breaks.

**Specific blockers remaining**:
- Classical `structure Hexagram` vs R-Family `Hexagram = Fin 6 → Bool` — pattern `cases h with | mk y₁..y₆ =>` (~40 occurrences per file) needs rewriting to `Hexagram.ext + decide`
- YiInstr constructor names: Classical `.interlace/.complement/.reverse` vs R-Family `.hu/.cuo/.zong`
- 4 Classical types missing R-Family equivalents: Yuan `.inDao/.toDuoYuan`, JianModeKernel `cases m`, R5_Wuyao.Mian inductive shape, BenZheng `.thing/.motion/.interval/.event` constructor names

**How to apply**:
- New code: import from clean `Atlas/Yi/` (R-Family side, 18 modules)
- Full 64-hexagram lookup: use `Atlas.Yi.Hexagram.fromName`
- Cell algebra: `Atlas.Yi.Cell128.Cell128` (R₇) and `Cell256.Cell256` (R₈)
- 12-instr ISA: `Atlas.Yi.YiInstr.Instr` (replaces classical BaguaTuring.YiInstr)
- Shi bridge: `Atlas.Yi.ShiBridge.toNew/fromNew` for `YinBit × GuoBit` ↔ `R 2`

**Remaining work (multi-session)**:
- 47 consumer files need coordinated cross-cluster rewrites (~5-10 hours of careful work, NOT parallelizable due to cross-cluster coupling)
- Atlas/Yi.lean umbrella needs the 7 new modules added (currently blocked by `Hexagram.allHex` dedup; trivial fix)
- Classical/Core/Yi.lean (1985 LOC) needs rewriting to use R-Family types underneath
- Then delete Classical/

main HEAD: `5f69769`. 15 v0.6 restructure commits total.
