**P81：超出确定的律。** 按 Ren 的“move towards 100%”，在发现 R6 的三方等价对不确定的律不成立之后，对每个过程陈述 R6 与 P67 的规律，并在相似之下重述用 `Determined` 陈述的定理。新的核心模块 `Becoming.Branching`（导入 `Unfolding`、`Attraction`、`Capture`），不用公理，不加前提，不改动已有模块。
- **回返。** 构型恰在它自己的进程下一步能得到它时回返（`returns_iff_fed_ahead`）；每个构型都回返，恰在过程从不离开的每个区域都保留它自己的每个可能时（`returns_iff_keepsWithin`）。保留每个可能不给回返（`Transit.keeps_not_returns`）；在有限多构型中，不合并沿运行给回返（`Branching.Lossless.returns`）；合并不必失去可能（`OneWay.merge_keeps`）。
- **被吸入。** 每个过程必然吸入的恰是不回返者（`necessarilyDrawn_iff_not_returns`）；可能被吸入是在某一进程中失去自身（`possiblyDrawn_iff`），可能被吸入的构型可以在另一进程中回返（`OneWay.possibly_not_necessarily`）。Capture 的规则区域是吸收区域，改革的状态被吸入规则所持之处（`Law.rule_absorbing`、`Captured.state_reform_drawn`）。
- **相似之下的确定。** 确定是相似之下的确定的命名情形（`determined_iff_named`）；关于构型如何相关的定理在相似之下成立（`DeterminedAt.stays_alike`、`Run.fixesAlike_of_takes`、`Run.not_fixesAlike_of_untaken`），而对两个相似构型之一的干预、未登记的过去与未登记的描述需要相等（`Twins.retarget_breaks`、`keepHistory_new_named`、`carries_unregistered`）。

读法是 AI 的，待 Ren。没有推出：从每个能动的构型出发的运行（一种选择）；在界内被吸入；分支进程上的度量（P82）。由本会话的一个 Opus 子代理构建（308 个常量，公理报告为空）。尚无独立审查。
