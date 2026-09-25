# Foundation/Wen

`Foundation/Wen` 是文、文言微核、自释、自举与 quine 路线的集中区域。它也包含当前唯一 opaque witness：`theOne`。

## Kernel 与 `theOne`

`Kernel.lean` 给出「一」的封装见证。`theOne` 是 opaque，不是 axiom；下游使用其投影：

- `Field`
- `dong`
- `origin`
- `origin_alive`

读法是「保留抽象见证」，不是「新增未说明公理」。当前 opaque 边界见 [../_generated/trust-boundary.md](../_generated/trust-boundary.md)。

## 文言微核

当前 public `wen` CLI 已收敛到 `Wen.Source -> Wen.Native`：显式
`#ox...` / `@ox...` / `(dsum ...)` 由 R-word 长度推 rank，直接进入
`Expr n`。它不再自动 fallback 到 `WenDef` / Hex / Yi。字义若要进入主线，
应通过 `Wen.SourceLexicon` 显式映射到 R-word，而不是让 kernel 或 CLI
内置中文语义。`wen` 启动时默认加载
`formal/SSBX/Foundation/Wen/lexicons/default.wen`；该默认表用 `名 #word alias...`
语法只把 R1-R4 的 `o/x` word 映射到对应 cell literal。用户可用
`--lexicon path/to/file.wen` 换表，或用 `--no-default-lexicon` 空表启动。
当前没有默认 CJK 字义表；裸 `一` 等字不会自动投到 Hex/R8。
候选 R1-R4 中文 glyph 的理据见
[`r1-r4-glyph-rationale.md`](./r1-r4-glyph-rationale.md)；第一轮反证测试见
[`r1-r4-glyph-test.md`](./r1-r4-glyph-test.md)。下一层 R5 `內` 的候选读法见
[`r5-glyph-rationale.md`](./r5-glyph-rationale.md)；R5/R6 作为 `內/外` 成对层的读法见
[`r5-r6-inner-outer-rationale.md`](./r5-r6-inner-outer-rationale.md)。对应的非默认实验字表在
`formal/SSBX/Foundation/Wen/lexicons/r5-candidate.wen` 和
`formal/SSBX/Foundation/Wen/lexicons/r6-candidate.wen`。这些都是可审计 lexicon
草案，不是 kernel 语义。

字词组合的等价、换序和信息丢失不应从中文直觉推出。先读
[`r-scope-information-flow.md`](./r-scope-information-flow.md)：它把 scope
定义为 R tower 的观察 map，用 projection/fiber/kernel 说明什么信息被丢掉，
并区分 full address、scoped equivalence、chart coherence、chart/focus loss。
glyph lexicon 只负责把字对齐到这些 R facts。

`WenDef*`、`WenEval`、`WenyanSyntax`、`WenyanParser*` 等文件组织文言表达、解析、求值与编译路线。它们的目标是让文言片段进入可检查结构，而不是宣称自然语言整体已被完全形式化。

## 自释与自举

`WenyanReflect`、`WenyanSelfHost`、`WenyanSelfInterp` 等模块处理自释、自解释与自举路线。读法应分层：

- 语法层：对象语言如何表示。
- 求值层：表达如何执行或解释。
- 反射层：系统如何谈论自身片段。
- 证明层：哪些性质已成 theorem。

## Quine 路线

`WenyanQuine*` 系列记录自指、构造、见证、搜索、历史与路线。它与 Bagua/GodelLi 的不完备边界相关，但不能被写成去公理化已经完成。

当前仍有唯一显式 axiom `kleene_recursion_axiom`。相关去公理化路线应看 `formal/SSBX/notes/zero-axiom-roadmap.md` 与 [trust-boundaries.md](./trust-boundaries.md)。

## 与 Text 的分工

Text 层维护算子、字、义位与覆盖表；Wen 层处理文言表达系统本身。查询算子总表看 [../_generated/operator-index.md](../_generated/operator-index.md)，查询 Wen 模块清单看 [../_generated/lean-index.md](../_generated/lean-index.md)。
