---
name: Squaring tower {R0,R1,R2,R4,R8} self-similar rule
description: Conceptual doctrine that R8 = R4 × R4 = (R2)^4 — a self-similar sub-tower of R0..R8, complementing the incrementing main view
type: project
originSessionId: f901350d-e960-41a3-82c9-6ad6829f23b4
---
R₀..R₈ 之下标 ∈ {0, 1, 2, 4, 8} 之 5 层构成自相似平方子塔, 由 S(A) := A × A 递推生成:
- T₀ = R₀ = Unit (1, 太极, S 之不动点)
- T₁ = R₁ = T₀ + T₀ = Bool (2, 由奠基算子 O₀ 给出; 协积/动静/substance·field 三相同义)
- T_{k+1} = T_k × T_k for k ≥ 1: T₂=R₂=4, T₃=R₄=16, T₄=R₈=256

|T_k| = R_{2^(k-1)} for k ≥ 1. 塔层 {R₀,R₁,R₂,R₄,R₈} = {1,2,4,16,256}.

塔外层 R₃/R₅/R₆/R₇ = 多重平方路径之交叉点. R₆ 尤其富 (= R₃² = R₂×R₄ = R₁×R₅), 三路同构.

R₈ 有两等价主因式分解: (a) R₆×V₄ 时空视角 (codebase 主线), (b) R₄×R₄ 平方塔视角 (本规则).
两者皆 (Z/2)⁸ 同一群之坐标选择, 无形式冲突, 语义负重不同.

doctrine 落地: 义理/Z_平方塔自相似规则.md (新, ~300 LOC) + yi-RO-hierarchy.md 第十一部分 (增补) +
表六_256格全表.md § 12 (增补 16×16 dual 视角行).

**Why**: 用户 2026-05-11 conversation 提出 "R4 一次分叉自相似 = 宇宙" 假说. 经探讨,
此假说 = 选 R₄×R₄ 作为 R₈ 之主因式分解. 数学上自动成立 ((Z/2)⁸ = (Z/2)⁴ × (Z/2)⁴),
但语义上是 codebase 主线 (R₆ × V₄) 之 dual reading. 用户要求"先把自相似规则找出来" — 已找到并 doctrine 化.

**How to apply**: 后续讨论涉及 R₀..R₈ 结构时, 区分两视角:
- "incrementing" 视角 (R_n → R_{n+1} +1 bit): 用于 chain-of-reasoning, 时态群代数, Cayley fusion
- "squaring" 视角 (T_k → T_{k+1} = T_k²): 用于 fractal / 自相似几何 / R_4 ⊗ R_4 嵌套语义
codebase 已隐式支持二者; 无需新 Lean 代码 ((Z/2)ⁿ strict closure 已蕴含). 形式化扩展 (R8 ≃+ R4×R4 AddEquiv ~80 LOC) 是可选, 非必要.
