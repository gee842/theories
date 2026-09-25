# 信任边界

> Last verified: 2026-05-21. 当前文件位置 / 信任边界数量请同时参考 [claim-status-ledger.md](claim-status-ledger.md) v0.8 (2026-05-21) 与 `../_generated/trust-boundary.md`。

形式层的信任边界必须明示，避免把工程事实、经验校准或文档同步误读为 Lean 已闭合证明。

## 已知边界

| 边界 | 位置 | 口径 |
|---|---|---|
| `kleene_recursion_axiom` | `formal/SSBX/Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean` | 项目层 axiom 之一；用于 cuo-restricted Kleene/Rice/GodelLi 结论。`KleeneInternal.lean` 跟踪去公理化路线。 |
| `Doctrine/Instance/Quantum.lean` | `formal/SSBX/Foundation/Doctrine/Instance/Quantum.lean` | 量子 SMCC instance 的 axiom 边界文件。 |
| `Order/FrmMonoidal.lean` | `formal/SSBX/Foundation/Order/FrmMonoidal.lean` | Frm 张量结构 axiom 边界文件。 |
| `theOne` | `formal/SSBX/Foundation/Wen/Kernel.lean` | 「一」的见证；refactor 后已改为 `def theOne : One`，下游通过其投影 `state` / `motion` / `origin` / `alive` 引用。详见文件内的 namespace 说明。 |
| `YiState.run` | `formal/SSBX/Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean` | 顶层 `partial def`；表示无界执行可能不返回。证明路径使用 `runFuel`。 |

## 非边界但常被误读的项

- `Field := theOne.state`、`dong := theOne.dong`、`origin := theOne.origin`、`origin_alive := theOne.alive` 是 `theOne` 的投影，不是新增公理。
- `runFuel` 是结构递归总函数，可用于 theorem-level 执行证明；`run` 是 executable boundary。
- 文档中的「claim」「ledger」「DAG」是审计对象；只有 Lean theorem 才是机器闭合命题。
- 经验校准、阈值、正邪判定等 pending interface 不能冒称已由 Lean 证明为真。

## 当前 sorry / axiom 状态

具体数字与定位以 `../_generated/trust-boundary.md` 与 [claim-status-ledger.md](claim-status-ledger.md) v0.8 为准；不在本页手工硬编码。整体口径（2026-05-21 核对）：

- 当前 live `sorry` 余量集中在 `Foundation/Order/FrameBimorphism`, `Foundation/Doctrine/Instance/Topological`, `Foundation/Enriched/Power`, `Foundation/Order/FrameCoproduct`, `Foundation/Doctrine/EnrichedLawvereTheory` 等模块；具体计数请查生成索引。
- 项目层 axiom 文件已收敛到三处（详见上表）。
- partial boundary 仍以 `YiState.run` 为主入口，并以 `runFuel` 做证明侧承载。

新增 `sorry` / `axiom` / `partial` / `unsafe` 必须在维护记录里解释；批量上升应同步触发 ledger v0.x 升版。

## `kleene_recursion_axiom` 的读法

`kleene_recursion_axiom` 不应被描述成「Lean 已证明的 Church-Turing 定理」。更准确的口径是：

- 它是当前 BaguaTuring 对角化路线的单一形式假设，定义在 `formal/SSBX/Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean`。
- 它已经收窄到 cuo-invariant decider 相关口径；具体讨论见 `Foundation/Atlas/Yi/Classical/Algebra/CuoInvariance.lean`。
- `formal/SSBX/Foundation/Atlas/Yi/Classical/Diagonal/KleeneInternal.lean` 与 `formal/SSBX/notes/zero-axiom-roadmap.md` 记录了去公理化路线。
- 在相关 witness/compiler/interfaces 未闭合前，依赖它的无条件 Godel/Rice 结论都应标注为「在此 axiom 下」。

## `theOne` 的读法

`theOne` 现在已是 `def`（而非 `opaque`），定义在 `Foundation/Wen/Kernel.lean`。它的作用是保留「一」的抽象 facade：下游可以使用 `state`、`dong` / `motion`、`origin` 与 `alive`，但不应展开其内部构造。Pre-refactor 的 `opaque theOne` 口径已被取代；详见文件内 namespace 注释。

## `YiState.run` 的读法

`YiState.run` 定义在 `Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean`，是 partial，因为 BaguaTuring 允许真实非停机。若强行改成普通总函数，会把非停机伪装成某个最终状态。证明和审计应优先使用：

- `runFuel`：有 fuel 的总执行。
- 有限 `native_decide` 见证：用于具体小例。
- `run-boundary.md`：说明为何保留 `partial def run`。

## 生成索引

若 `../_generated/` 已生成，应优先引用其中的 trust-boundary、declaration、module index 来核对统计。本页维护语义口径，不手写替代机器统计。具体 closed/scoped/open 状态参考 [claim-status-ledger.md](claim-status-ledger.md) v0.8 (2026-05-21)。
