---
name: MetaInterp Phase A foundation (2026-05-08)
description: YiInstr 通用元解释器之 Phase A foundation — state layout / prologue / counted-loop combinator (def 已定，simulation 待证)
type: project
originSessionId: 54a0fbda-ac51-4eaf-976e-6e5ed0b8890c
---
2026-05-08 启动 [Foundation/Wen/MetaInterp.lean](formal/SSBX/Foundation/Wen/MetaInterp.lean) — `metaInterpProg : List YiInstr` 之构造，目标是 discharge `KleeneCarrier.universalInterpExists` 公理。

**Plan agent calibrated 估计**：~2800 LOC 总（550 YiInstr + 2250 Lean 证明），5–7 天 with parallel subagents. 原"700 行"低估 3-4 倍——主要在 per-block simulation lemmas。

**Phase A 完成度**（391 LOC, 32 defs+theorems, 0 sorry, 0 axiom — pushed to `claude/nice-golick-d43a28` as commits e923dfb + 4d72c16, 2026-05-08）：
- ✅ A.1 state layout: Shi-tagged encoding（jin=data, wei=marker, ji=halted）+ encCounter/decCounter + encMetaHistory + 7 lemmas
- ✅ A.2 prologue: 5-instr `setShi wei; push×3; setShi jin` + 6 correctness theorems（cur/history/pc/halted/prog 各 + 主 `afterPrologue_history_eq_encMetaHistory`）
- ⏳ A.3 counted-loop combinator: def + 4 structural lemmas done; **simulation lemma (induction on n) — Wave 1 subagent in flight**
- ⏳ A.4 skip-one-instr subroutine: **Wave 1 subagent in flight** (creates new file `MetaInterp/SkipInstr.lean`)
- ⏳ Phase B contract: **Wave 1 subagent in flight** (creates `MetaInterp/ExecuteBlock.lean` with nop+halt as worked examples)

**关键设计决策**（cuo-equivariance ceiling 之解）：
- META.cur ≡ sim.cur 直接镜像（无编码开销，6 个 cur-变换指令 hu/cuo/zong/flipYao/setShi 直接复用）
- 所有 register cells 仅靠 **Shi** 区分类型（Hex 部分依输入 cur，cuo-不变性自动满足）
- META.history 布局 (top→bottom): `pc-data×pc | pc-marker(wei) | halted-flag | simhist-len-data×|simhist| | simhist-len-marker(wei) | sim.history(raw) | encProg sim.prog(raw)`

**Why:** 原 `kleene_recursion_axiom` 不仅是工程债——它在 Lean+Classical 里**逻辑不一致**（[SoundnessProbe.lean](formal/SSBX/Foundation/Bagua/SoundnessProbe.lean) 之 `kleene_recursion_inconsistent : False` 已证）。本 interpreter 是过渡到 sound `YiKleeneInverter` API 之必经工程。

**How to apply:**
- 接续工作从 A.3 simulation lemma 开始 — induction on Counter, body fuel + 3 per iteration
- A.4 skip-one-instr 用 12-way dispatch on tag → cell-pop arity table，~ 50 LOC
- Phase B（12 executeBlocks + fetch/dispatch/writeback）可分给 7 subagents 并行；接口契约见 MetaInterp.lean §7 docstring
- Plan blueprint 完整见对话历史：state layout / fetch protocol / dispatch tree / per-block strategy / risk analysis / order of attack
