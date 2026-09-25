# Wen 语言栈 — 决策路线图

**状态**: 2026-05-18 · Yongxu Ren (native interpreter slice)

> 2026-05-18 update: this roadmap is now partly historical.  The current code
> has a single public interpreter entrypoint, `SSBX.Foundation.Wen.Interpreter`,
> backed by `SSBX.Foundation.Wen.Native`.  The live
> direction is not "5 evaluator 收敛到 1 with `WenDef.Tm` as core"; it is
> "`Wen.Native.Expr n` as the only interpreter kernel, with WenSurface /
> WenDef / Bagua-ISA / MetaInterp demoted to legacy adapters, historical
> backends, or proof targets."  Items below are useful as migration notes, not as an
> architecture with parallel layers.
>
> Current native slice: callers should import through `Wen.Interpreter`.
> `Wen.Native` now carries the language-independent kernel constructs needed
> for the next adapter pass: first-class `fix`, cell-tagged data, and
> `Wen.Native.Nominal` tagged-record hosting for constructors/catalogues,
> predicate sets, and flat pattern tests.  WenSurface namespaces, classes, and
> typed unquote stay in the adapter/lowering layer.  The `wen` REPL is now the
> active `Wen.Source -> Wen.Native` path; automatic WenSurface/WenDef fallback
> is disabled.  Legacy Hex/Yi behavior is not an optional active overlay; new
> glyph meaning must enter through rank-polymorphic `Wen.SourceLexicon`
> bindings over R-words.  The next active slice is the `R.Awareness` umbrella
> plus Wen Adapter described in
> [`wen-judgment-system-plan.md`](wen-judgment-system-plan.md): closed finite
> Bool reports first, then scope-aware descent reports, then a minimal
> ancient-Chinese logical grammar.  `Judgment` is the claim sublayer inside
> `R.Awareness`; it is not the whole report boundary.  Wen does not own truth
> semantics here; it compiles source into `R.Code` and renders R-native
> `R.Awareness` reports.  Bounded finite enumeration is diagnostic unless a
> named Lean theorem supplies soundness, and no user-facing path should be
> described as a universal truth oracle.
>
> 2026-05-20 update: the next frontend slice has started as a
> corpus-first Classical Reading AST.  Raw unspaced text is represented by
> `SSBX.Foundation.Wen.Text`; reading roles, candidate segmentations, and
> selected readings live in `SSBX.Foundation.Wen.Reading`.  The active
> `.wen` analyzer now accepts `篇` / `文` / `讀` / `訓` lines as textual
> reading evidence.  `篇` / `文` / `讀` may remain text-facing evidence with
> `unknown` / needs-reading diagnostics.  A bound `訓` may emit an R.Code
> term or predicate definition when its target resolves in the typed context;
> later checks can prove only that emitted definition, not the truth of the raw
> text, the selected reading, or a commentary interpretation.  See
> [`classical-reading-ast.md`](classical-reading-ast.md).
>
> 2026-05-21 update: for the live wording boundary on `wen --judge` /
> `:judge` reports and the "Wen does not own truth semantics" guardrail,
> see [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 row
> `R.Awareness` + `Judgment` sublayer + Wen Adapter.

## 现状（post-PR B' v2）

| 层 | 表面 | 实现 | 覆盖率 / 状态 |
|---|---|---|---|
| **Bagua-ISA** | 24-token 汇编 (v2: +「比阳」) | `wenyan` CLI + `BaguaTuring.YiInstr` (13 instr) | universal Hex → Hex (v2 doctrine break, 含 `branchYaoYang`) |
| **WenDef.Tm** | 类型化 lambda (Hex/Bool/Pair/List/Arr) | `WenDefEval` | legacy typed adapter/proof view；不得作为新 kernel |
| **WenSurface** | 文言级 prose + namespace/class/typed-unquote conveniences | `wenyanCompile + theoremBackedSemanticsFor?` | legacy adapter/lowering layer；desugar 100% (375/375, 形式见证 [Semantics.lean:1142-1153](../../formal/SSBX/Foundation/Atlas/Wen/SurfaceSemantics.lean#L1142)) |
| **Bridge WenSurface→ISA** | — | `wenyanCompileToYiInstr?` | ✓ universal Hex → Hex (v2, 含 `推`/`損` 等 non-equivariant) |

已落地的 4-步收顶进度：

| 修法 | 状态 |
|---|---|
| catalogue 改 desugar 表 | ✅ 100%（46 个学派关系算子 placeholder body — 是 domain caveat 不是 desugar gap） |
| `Wen.Interpreter` / `Wen.Native.Expr n` 立唯一 kernel；`Tm/CoreForm/R8` 作 adapter / proof view | ✅ public entrypoint、first-class `fix`、cell-tagged data、nominal tagged-data host 已落地；`WenDef.Tm → Native.Expr 8` 第一版 lowering 已在 adapter 内可验证 |
| Bagua-ISA 作 Tm 后端 | ✅ universal (v2, B' merged 2026-05-17) |
| WenSurface namespace/class/typed-unquote lowering 到 Native | ⏳ 部分完成；保持 adapter，不进入 Native kernel；userCtor/catalogue/set/match、Bool unquote、function-shaped fix 的 Native lowering smoke 已落地 |
| 多 evaluator 收敛到 `Wen.Native.evalFuelG` | ✅ public `wen` path 已切到 `Wen.Source -> Wen.Native`，不再自动 fallback 到 `WenDefEval`；旧 WenSurface/WenDef 仍是 legacy/proof line，待 rank-polymorphic source lowering |

## 近期状态 / 待决策项

C1 已进入实现线；其余项仍按下文状态推进。

---

### Slice C1 — 句末虚词 乎/矣/哉/兮 **【已进入真解析线，2026-05-18】**

#### 价值（已交付）

让文言可以自然收句，而不是停在函数链形态。现在可写：

- `推 一 矣`
- `一 同 一 乎`
- `凡 甲 同 甲 甲 哉`
- `推 一 兮`

#### 实现读法

`也/乎/矣/哉/兮` 是 sentence-final postfix particles。解析层把它们保留
为 `SurfaceExpr.marker tok body`；elaboration 擦除 marker，所以这些虚词
不会强制 carrier 变成 Bool，也不会改变 Hex/Bool denotation。

一个关键细节是“冒泡”：在解析必需参数时，句末虚词不会被子表达式吞掉。
因此 `一 同 一 矣` 被读作整个判断句的句末标记，而不是只标记右边的
`一`。

#### 当前边界

- 已有 375-row catalogue / glyph / operator-cell coverage。
- `S_21..S_24` 的 catalogue prefix row 仍存在，用于覆盖表；自然古文用法
  走 postfix marker。
- 这些虚词目前只表达 surface 语气/收句，不编码问句、完成、感叹、韵律的
  discourse semantics。

---

### Slice B' — 扩 YiInstr 破 complement-equivariance ceiling **【已完成 v2 doctrine, 2026-05-17】**

#### 价值（已交付）

让 `wenyanCompileToYiInstr?` 成为 **universal compile** —— `推/损` 等 non-equivariant 项现可桥到 Bagua-ISA。后端目标 ISA 覆盖 WenDef.Tm 全 Hex → Hex 子集。

#### Doctrine 变更

**v1 doctrine 已破**: [`WenDefCompile.lean` 文件头](../../formal/SSBX/Foundation/Wen/WenDefCompile.lean#L1) 之「未尽之业」改为 §「v2 扩展」。详 before / after 对比表见 `BaguaTuring.lean` 之 § 8 与 `WenDefCompile.lean` 文件头之表。

`BaguaTuring.lean` 加第 13 条原语 `branchYaoYang (i : Fin 6) (target : Nat)` —— absolute yao test (若 yao i = yang, 跳 target). 此原语 **不与 complement 通约**, 故 doctrine 破之.

#### 已交付清单

1. ✅ `formal/SSBX/Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean` 加 `branchYaoYang` + `complementEquivariantInstr` predicate + 12 v1 原语 之 equivariant 见证 + branchYaoYang 之 non-equivariant 反例
2. ✅ 12 v1 原语的"与 complement 通约"定理: 由全集事实改为子集事实, guard 为 `complementEquivariantProg` (子集 program). `halts_cuo_invariant` 加 `AllEquivariant P` hypothesis. `cuoState_step_equivariant` 加 instr-level equivariance guard.
3. ✅ `WenDefCompile.lean` 之 `compileHexFunCertified?` 扩 pattern: `.tuiBody` (mod-64 +1) 与 `.sunBody` (mod-64 -1) 经 propagate-carry/borrow adder (27 instr) 现可 compile
4. ✅ 64-Hex `compiledHexFunAgrees` 复用 (native_decide 见证)
5. ✅ **narrative 改完**：本文件之 § B' 章节 + `wen-substrate/03-operation-monism.md` 之 cuo-equivariance ceiling 段 + `WenDefCompile.lean` 文件头之 v2 doctrine 文档

#### 风险（mitigated）

- ✅ doctrine 改之 — 由 `complementEquivariantInstr` 谓词 + `AllEquivariant` 子集事实双重 guard 平滑迁移
- ✅ MetaInterp 之 universalMetaInterp dispatch: `branchYaoYang` 暂 route 到 `haltTag` slot (placeholder, 见 Dispatch.lean v2 注). 完整 self-interp 之 13 instr support 留作 follow-up
- ✅ Atlas/Yi 多处 narrative：通过 `complementEquivariantInstr` predicate 显式表达 v1 子集事实

#### 实现 highlights

**Propagate-carry adder 算法** (`tui` = +1 mod 64):
- bit 0 (y1, LSB) 起 propagate carry 向 bit 5 (y6, MSB)
- 每 level 5 instructions: `branchYaoYang i (P+3); flipYao i; jump next; flipYao i; halt`
- yang case (bit = 0): jump P+3, flip bit (now 1), halt
- yin case (bit = 1): flip bit (now 0), jump next level (carry up)
- 终层 y6 (MSB) 简化: `flipYao 5; halt` (mod-64 之 overflow 自然丢弃)
- Total: 5 × 5 + 2 = 27 instructions (含 wrapper appended halt)

`sun` (mod-64 -1) 算法 dual: bit yin → flip + halt; bit yang → flip + borrow propagate.

---

## "做完"的现实读法

A1 / B 已合并主线。C1 / B' 待明确授权。

若用户答 "全部跳过": 当前主线就是「Wen 1.0」可发布状态 —— desugar 100%, 错等变桥已证, 7+8 prose 样本上链。

若用户答 "执 C1 Path B": 会开 2-3 PR 序列（构造子 + 长度定理 + parser），耗时 1-2 工作日。

若用户答 "执 B'": 先改 doctrine narrative（v4-foundation.md 等），再扩 ISA，再扩 compile —— 3-4 工作日 + 重证若干形式 invariant。

---

**相关文件**

- [`samples/README.md`](../../formal/SSBX/Foundation/Wen/samples/README.md) — 双层 sample 总览
- [`Atlas/Wen/SurfaceSemantics.lean`](../../formal/SSBX/Foundation/Atlas/Wen/SurfaceSemantics.lean) — desugar 表 + length theorems
- [`Wen/WenDefCompile.lean`](../../formal/SSBX/Foundation/Wen/WenDefCompile.lean) — Bagua-ISA 桥 + 错等变 doctrine
- [`Wen/WenSurface/ISABridge.lean`](../../formal/SSBX/Foundation/Wen/WenSurface/ISABridge.lean) — String→YiInstr 端到端
- [`Wen/WenSurface/ProseSample.lean`](../../formal/SSBX/Foundation/Wen/WenSurface/ProseSample.lean) — 7-行文言 round-trip
