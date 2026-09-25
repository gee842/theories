# 生生不息新文档集 — current doctrine map

> 状态：v1.5+ reading map (2026-05-18; honesty 校准 2026-05-21) — current doctrine lives in `wen-substrate/`: R-Family as universal formal substrate, four-level abstraction tower (distinction -> operation -> algebraic class -> canonical F₂), scoped GUT-A/B progress, and explicit open obligations for full Claim Z / T0 / coherent T5 / GUT-C.
>
> **Honesty pointer**: 形式状态的唯一当前 honest 来源是 [`claim-status-ledger.md`](10_formal_形式/claim-status-ledger.md) v0.8 (2026-05-21)。本页与下文其他 staging 文档若仍引用 "3656 jobs / 0 sorry" 等 v3 定本快照，仅作历史参照；当前工作树 sorry 数约 150-170 (非零)、有 3 个 axiom 文件。具体闭合层级（closed / scoped / schema / placeholder / open）以 ledger 为准。

本目录是新的文档集暂存区。旧文档暂不删除；待本目录稳定后，再整体替换根 README、`formal/SSBX/README.md`、`义理/README.md` 与 web 索引入口。

## Current Doctrine (必读)

- [**wen-substrate/00-README.md**](10_formal_形式/wen-substrate/00-README.md) — current foundational document set and reading map.
- [**wen-substrate/08-obligations.md**](10_formal_形式/wen-substrate/08-obligations.md) — T0, D1-D6, T1-T8, proof obligations, and version history through v1.5.1.
- [**claim-status-ledger.md**](10_formal_形式/claim-status-ledger.md) — current human ledger: what is closed, scoped, schema, placeholder, or open.
- [**code-promise-gap.md**](10_formal_形式/code-promise-gap.md) — transparency map between doctrine claims and Lean backing.

## Historical Foundation Layers

- [**wen-algebra.md**](10_formal_形式/wen-algebra.md) v0.6 — tower algebra + Lean compiler/interpreter foundation. Important historical layer, no longer the latest canonical pointer.
- [**v4-foundation.md**](10_formal_形式/v4-foundation.md) v0.5, [**r4.md**](10_formal_形式/r4.md), [**r8.md**](10_formal_形式/r8.md) — R₀–R₈ / R₄ / R₈ structure references retained for local details.

## v3.0 historical (superseded)

- [final-theory.md](00_start/final-theory.md) — v3.0 one-page map (Cell256-centered, Yi-named atoms)
- [yi-RO-hierarchy.md](10_formal_形式/yi-RO-hierarchy.md) — v3.0 R-uniform strict (Z/2)ⁿ R₀..R₈ doctrine
- [yi-calculus-theorem.md](10_formal_形式/yi-calculus-theorem.md) — Theorems A–K (survive intact; positioned as Yi-Atlas theorems now)
- [yi-as-meta-framework.md](10_formal_形式/yi-as-meta-framework.md) — meta-categorical framework (Yi reframed as one Atlas binding among many)

## 三条阅读路径

- [起步](00_start/README.md)：快速选择形式、义理或维护路径。
- [形式层](10_formal_形式/README.md)：从 Lean 代码、构建、信任边界、模块索引与 claim ledger 进入。
- [义理层](20_theory_义理/README.md)：从 R₀..R₈ 阶梯、六征体系、传统/现代论证与对齐主题进入。

英文读者先看 [overview.en.md](overview.en.md)。英文只维护总览，不作为第二套规范。

## 机器口径

- 下面几条是 v3 定本时期的历史构建快照，不代表当前工作树最新 GUT / WenSurface 状态。
- `lake build SSBX` 通过：**3656 jobs**（v3 定本，commit `1c76a55`），0 sorry, 0 warning。**注意**: 当前工作树并非 0-sorry — 见 [claim-status-ledger.md](10_formal_形式/claim-status-ledger.md) v0.8 (2026-05-21)。当前 `Foundation/` 下仍含 ~150-170 处 `sorry`（包括 `Truth/`, `Order/`, `Doctrine/`, `Wen/`, `Atlas/Yi/Classical/Diagonal/`, `Hierarchy/ZoneClassifier/` 等模块），不再宣称工作树 0 sorry。
- `R8_complete` axiom audit (v3 历史): `{propext, native_decide}`。当前工作树仍含 3 个 axiom 文件: `Foundation/Modern/Quantum.lean`, `Foundation/Order/FrmMonoidal.lean`, `Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean` (后者保留 `kleene_recursion_axiom`)。
- live trust boundary 以 [trust-boundary](./_generated/trust-boundary.md) 为准（生成索引目录 `_generated/` 当前未在仓库工作树中实体化；恢复脚本以 `50_maintenance/` 为入口）。
- claim 状态以 [claim-status-ledger.md](10_formal_形式/claim-status-ledger.md) v0.8 (2026-05-21) 为唯一当前 honest 来源；生成 [claim-index](./_generated/claim-index.md) 在恢复 `_generated/` 后再启用。
- 模块与声明索引以 [lean-index](./_generated/lean-index.md) 为准（同上，待 `_generated/` 恢复）。

## 最近变更 (Latest)

| 日期 | 内容 |
|---|---|
| 2026-05-18 | Added `SSBX.Foundation.Wen.Interpreter` as the single public Wen interpreter entrypoint plus direct `wen-kernel` CLI. Heavy legacy adapters are kept outside the entrypoint under explicit adapter/boundary paths. |
| 2026-05-18 | Wen interpreter policy updated: `SSBX.Foundation.Wen.Interpreter` is the public single-kernel entrypoint, backed by `SSBX.Foundation.Wen.Native`; `WenSurface`, `WenDef`, `RKernel`, `YiInstr`, and `MetaInterp` are migration adapters / backend proof targets, not peer interpreter strata. |
| 2026-05-18 | `Foundation/Atlas/DaoPrimeBridge.lean`: documented Atlas Dao/non-dao reading of `0` / `x ≠ 0`, proved non-dao layer cardinality `2^N - 1`, and connected it to existing `EulerBridge` prime visibility. Core `Foundation/R/` remains language-independent. |
| 2026-05-18 | **current doctrine pointer update**: `wen-substrate/` + `08-obligations.md` + `claim-status-ledger.md` become the reading entry for R-Family / Claim Z / GUT status. `wen-algebra.md` v0.6 is retained as a historical foundation layer. Full Claim Z / T0 / T3 / coherent T5 / GUT-C are explicitly not marked complete. |
| 2026-05-15 | **v0.6 foundation layer**: `wen-algebra.md` v0.6 + `v4-foundation.md` v0.5 + `r4.md` + `r8.md` 入档. 弃 𝕏/𝕐/矩/象/Frame 等历史层名; 改用 R-Family `R_N := F_2^N` parametric tower. R₄/R₈ 双中心. 语义命名（Yi/Pauli/Boolean）下放至 Atlas application layer. Lean 4 为唯一形式语言 (Clojure 弃用). |
| 2026-05-14 | v0.4 Xiang module shipped (`762a618`); since superseded by v0.6 R-Family. |
| 2026-05-11 | v3.0 `1c76a55`: 9 个 R-index 命名 alias 文件 + `RHierarchy.lean` umbrella；3656 jobs build 干净. (v3.0 superseded by v0.6.) |
| 2026-05-10 | v3.0 `7de5064`/`0003224`/`8e4406e`: Cell192 → Cell256 migration, V₄ Klein Shi, Modern/* upgrade, Cell192.lean deletion. (v3.0 superseded by v0.6.) |

详见 [`30_crosswalk_互证/old-to-new.md`](30_crosswalk_互证/old-to-new.md) 之 **Cell192 → Cell256 transition** 节。注意：当前 Cell256/Cell128 实体源已迁出 `Bagua-cluster/`，落到 `formal/SSBX/Foundation/Atlas/Yi/Cell{128,256}.lean`；`Bagua-cluster/` 目录已删除。

## 读法

1. 先看 [wen-substrate/00-README.md](10_formal_形式/wen-substrate/00-README.md) 拿到当前 doctrine 地图。
2. 再看 [claim-status-ledger.md](10_formal_形式/claim-status-ledger.md)，确认 Claim Z / T0 / T5 / GUT 哪些已经闭合、哪些只是 scoped 或 placeholder。
3. 然后看 [形式层信任边界](10_formal_形式/trust-boundaries.md)，确认 axiom、opaque、partial 与生成索引口径。
4. 查证时回到 Lean 源文件、[_generated](./_generated/) 和 [code-promise-gap.md](10_formal_形式/code-promise-gap.md)，不要从散文 headline 读取证明强度。
5. 需要追溯旧稿时，看 [archive-pointers.md](archive-pointers.md)；`史料/` 与 `史/docs-next-v2/`（v2 frozen 副本）保持 frozen。

## 覆盖面

本目录不是四个顶层文件；主体在各分区内：

- `00_start/`：读者路径与范围。旧 `final-theory.md` 是 v3.0 superseded 一页速览；GUT-C / Lawvere / representation closure 相关草案在此分区。
- `10_formal_形式/`：形式化、模块簇、信任边界、构建。当前 doctrine 入口是 [`wen-substrate/00-README.md`](10_formal_形式/wen-substrate/00-README.md)；证明强度以 [`claim-status-ledger.md`](10_formal_形式/claim-status-ledger.md) 与 Lean 源为准。
- `20_theory_义理/`：旧义理文档的分类重排（**[core-framework.md](20_theory_义理/core-framework.md)** 已升级至 R₀..R₈）。
- `30_crosswalk_互证/`：Lean 与义理互证；**[old-to-new.md](30_crosswalk_互证/old-to-new.md)** 含 Cell192→Cell256 完整迁移记录。
- `40_reference_参考/`：算子、字根、六表、字文与术语。
- `50_maintenance/`：生成、检查、发布与归档策略。
- `_generated/`：脚本生成的事实索引（当前未在工作树中实体化，恢复入口在 `50_maintenance/`）。

## 维护原则

- 一个事实只保留一个权威来源：Lean/ledger 为形式事实，生成索引为可定位目录，人工文档只做解释和路径。
- 不在 README 里堆长表；长表进入 `_generated` 或 `40_reference_参考/`。
- 不把 `史料/` 改写成现规范；只记录它们被哪里取代。
- R-Family / Claim Z / GUT 相关主张必须按 [`claim-status-ledger.md`](10_formal_形式/claim-status-ledger.md) 的闭合层级书写：closed、scoped、schema、placeholder、open 不得混写。
