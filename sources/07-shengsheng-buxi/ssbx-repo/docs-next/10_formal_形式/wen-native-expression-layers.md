# 文之 native 构造层

> 状态：v1.1 (2026-05-18)
> Lean anchor: `SSBX.Foundation.Wen.Native.Reader`, `SSBX.Foundation.Wen.SourceLexicon`, `SSBX.Foundation.Wen.Native.Reader.ReaderLexicon`, `SSBX.Foundation.Atlas.Wen.NativeLexicon`, `SSBX.Foundation.Atlas.Wen.NativeAliases`, `SSBX.Foundation.Atlas.Wen.SurfaceLexicon`
> 作用：固定 native Wen 中「式、行、列、文、值、集」之构造口径；native reader/compiler 默认采用 ASCII / o-x 语法；active glyph meaning 通过 `Wen.SourceLexicon` 显式绑定到 R-word；旧中文 / classical alias 只作 legacy Atlas 兼容。

## Decision

文构造层采用 native Wen，而不是旧 V4 Lisp spine：

```text
名 / 元 / 算子
  -> 式
  -> 行
  -> 行列
  -> 文
  -> 运行
  -> 值
  -> 值列
  -> 集
```

这条链的关键点是：`文` 是可执行行之列，不是单个表达式；`集` 是列上附加去重判准，不是塞回单个 R₈ cell 的幂集对象。

native Wen 的默认读入边界是 ASCII S-expression + o/x cell/name 字符串。中文 / classical 词形不属于默认 compiler/kernel 语法。active glyph meaning 通过 `Wen.SourceLexicon` 显式绑定到 R-word；旧 `ReaderLexicon`/Atlas aliases 保留为 legacy 兼容，不是 public `wen` 的默认语义。

## Terms

| 中文 | Lean anchor | 说明 |
|---|---|---|
| 元 | `Cell n = Layered.Rn n` | rank-polymorphic cell；R₈ 时为 Cell256 视角 |
| 算子 | `Prim n` / `Layered.Vn n` | native primitive 或层内 action |
| 名 | `Expr.ref : Cell n -> Expr n` | native name 是 cell 名；human/global name 需经 Atlas lexicon 或 `.wen` surface 映射 |
| 式 | `Native.Expr n` | native core expression |
| 核式 | `RootRuleKernel.CoreForm` | root-rule kernel 之保守 R₈-visible core form |
| 行 | `TopForm n` | 可执行 top form：表达式行或定义行 |
| 行列 | `List (TopForm n)` | 多行有序列 |
| 文 | `List (TopForm n)` | 程序文本之形式锚；等同于行列 |
| 值 | `Value n` | native runtime value |
| 值列 | `List (Value n)` 或 `Value.list` | 值之有限序列；运行结果可保留顺序与重复 |
| 集 | `List α + Nodup` | 列加无重复证明；遗忘顺序/重复时才进入集合口径 |

`史` 与这里的 `集` 不同。`史` 保留次序、重复与过程痕迹；把 `史` 投成 `集` 是有损的 support 操作。

## Atlas Native Alias Surface

默认 native reader 只承认 ASCII / o-x 语法；下列中文 primitive 是 Atlas 层 reader/surface 边界别名，全部落到既有 native constructor 或 `Prim`：

| 中文 | native |
|---|---|
| 函 | `lambda` / `Expr.lam` |
| 施 | `app` / `Expr.app` |
| 结 | `cons` / `Prim.cons` |
| 空 | `nil` / `Expr.nil` / `Value.nil` |
| 首 | `car` / `Prim.car` |
| 余 | `cdr` / `Prim.cdr` |
| 若 | `if` / `Expr.if0` |
| 空乎 | `null` / `Prim.null` |
| 判空 | `null` / `Prim.null` |
| 不大于 | `numLe` / `Prim.numLe` |
| 大于 | `numLt` / `Prim.numLt` |
| 引 | `quote` / `Expr.quote` |
| 解 | `eval` / `Prim.eval` |
| 定 | `define` / `TopForm.define` |

这些字在显式启用 Atlas `ReaderLexicon` 后，才在 reader 边界降低到 native core。`不大于/大于` 与递归闭包是为了让纯文言快速排序跑在 native evaluator 上加入的最小 native core 支持；它们不改变 R₀..R₈ carrier，也不把汉字语义推入 compiler/kernel。

## Lists And Sets

列用 `空` 与 `结` 生成：

```text
列:
  空
  结 x xs
```

在 Lean core 中，表达式列用 `Expr.list` 展开为 `Expr.nil / Expr.cons`；值列用 `Value.list` 展开为 `Value.nil / Value.cons`。默认 reader 中 `(cons a b)` 作为 ASCII primitive application 读入；启用 Atlas Wen lexicon 后，`(结 a b)` 降低为同一 primitive application，求值后得到同一值层 cons。

集不是新的 cell carrier：

```text
集 α:
  items : List α
  nodup : items.Nodup
```

因此：

```text
值列 -> 集
```

必须显式给出去重判准。若以后需要 quotient set 或 finite set API，应作为值列上的外延视图加入，而不是把 `P(R₈)` 声称为一个 R₈ 元。

## Functor Boundary

`函` 只是映射候选。`函子` 需要再加保结构律：

```text
函子 = 函 + 保结构律
```

list-map 的理论式可以写作：

```text
映 f 空 = 空
映 f (结 x xs) = 结 (施 f x) (映 f xs)
```

这里的 `施 f x` 是 native application；若 `f` 是 core lambda，则经 `Expr.app` 运行；若 `f` 是 primitive，则经 `Prim` arity 与 `applyPrim` 运行。

## Boundaries

- 本页只固定 native Wen 的构造词表，不改 R₀..R₈ strict `(Z/2)^n` 层级。
- native reader/compiler 默认边界是 ASCII / o-x：`#oooooooo` 作 cell literal，`oooooooo` / `@oooooooo` 作 cell name，`cons` / `lambda` / `define` 等作 native form。
- 中文 / classical token 不是 compiler/kernel 默认语法；本体层仍是 `Expr n`, `TopForm n`, `Value n`, `Prim n`。
- 语义 glyph meaning 走 `Wen.SourceLexicon` 显式绑定到 native target；默认表位于 `formal/SSBX/Foundation/Wen/lexicons/default.wen`，当前只含 R1-R4 `名 #word alias...` bindings。native compiler/kernel 只接收降低后的 constructor、primitive、cell 与 top form。
- `R₈` 可承载有限编码、路径或投影，但不能把 `P(R₈)` 当作单个 R₈ cell 无损容纳。
- `Cell256` 是当前 R₈ carrier；不引入 `Cell192`。
- `核式` 指向 `RootRuleKernel.CoreForm`，与 native `Expr n` 并列为理论锚；二者不在本页合并。
- `WenSurface` 旧执行 / 文言 surface 管线保留为 legacy/historical surface；classical vocabulary、glyph meaning 与 catalogue semantics 由 legacy Atlas tables / registries 承接，不能作为 public `wen` 默认语义。

## Lean Placement

- `formal/SSBX/Foundation/Wen/Native/Reader.lean`：native reader；默认 ASCII / o-x，定义 `ReaderLexicon` 扩展点，并提供 `read*With` 显式 lexicon API。
- `formal/SSBX/Foundation/Wen/SourceLexicon.lean`：active glyph-to-native-source 入口；解析 `.wen` lexicon 文件，并只把 `名 #word/@word alias...` 绑定降低为 native source token，不新增 evaluator case。
- `formal/SSBX/Foundation/Wen/lexicons/default.wen`：默认 active source lexicon；R1-R4 的 `名 #word alias` table，可被 CLI `--lexicon` 替换。
- `formal/SSBX/Foundation/Atlas/Wen/NativeLexicon.lean`：Atlas Wen reader lexicon；提供中文 / classical token 到 native primitive / constructor 的 lowering 数据。
- `formal/SSBX/Foundation/Atlas/Wen/NativeAliases.lean`：中文 `abbrev/def` 与小定理，证明别名与 native core 同义；不新增 evaluator case、primitive constructor 或 carrier layer。
- `formal/SSBX/Foundation/Atlas/Wen/SurfaceLexicon.lean`：旧 WenSurface 词表、卦名/Bool literal、syntax marker、namespace label 与 pretty-print glyph 的 Atlas-side 数据源。
- `formal/SSBX/Foundation/Atlas/Wen/SurfaceDomainLaw.lean` / `SurfaceSemantics.lean`：classical catalogue 的 domain-law ledger 与 375-row executable semantics registry；它们不是 native compiler/kernel。
- `docs-next/10_formal_形式/wenyan-native-syntax-spec.md`：纯文言 algorithm parser 的规范语法；先固定结构，再扩实现。
- `formal/SSBX/Foundation/Wen/WenyanAlgorithms.lean`：不用 Lisp surface 的文言算法 parser；先把 `法曰/受/若/取/令/归/试以` 小文法读成 `Function / Stmt / Expr`，再降低到 `Native.SurfaceTopForm 8 / TopForm 8` 并用 native evaluator 运行，以 Lean 小定理验证快速排序语义。
- `WenyanAlgorithm.lean` / `wenyan-algorithm`：运行 `examples/wenyan-native/` 中的纯文言算法文件，不经 Lisp reader。
- 后续如果扩 reader，应保持同一策略：ASCII/o-x default 不变；中文 / classical token 做 Atlas parse-time lowering；只有确需表达新可计算能力时才补最小 native primitive。
