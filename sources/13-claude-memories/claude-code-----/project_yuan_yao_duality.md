---
name: 元/爻 配对原则 — 平方步两因子之非对称语义
description: At each R_{2n} = R_n × R_n squaring step, the two R_n factors carry asymmetric semantics (carrier 元 vs dimension 爻); 实/虚 与 本/征 are dual pairings
type: project
originSessionId: f901350d-e960-41a3-82c9-6ad6829f23b4
---
平方步 R_{2n} = R_n × R_n 之两个 R_n 因子**形式同构但语义不对称**:
- 一个承担**元** (yuan / carrier / 被分类内容 / what-is-being-counted)
- 另一个承担**爻** (yao / dimension / 分类轴 / how-it-is-being-arranged)

具体 carrier/dimension 之分配是 doctrine 选择, **不由群结构本身决定**.

R₄ = R₂ × R₂ 处具体:
- 首选读法: 实/虚 (元) × 本/征 (爻) — 内层是 R₂ 实虚态, 外层是 R₂ 本征轴
- 对偶读法: 本/征 (元) × 实/虚 (爻) — 反向, 同样 doctrine 合法

R₆ = R₃² = R₂×R₄ = R₁×R₅ 塔外交叉点至少有 **6 种** 元/爻配对读法 (3 路径 × 2 方向),
故 R₆ Hexagram "富结构".

**Why**: 用户 2026-05-11 conversation 给出之关键洞察: "实/虚 与 本/征 应该是一对是元 一对是爻吧".
此前 codebase 把 Ben/Zheng 当作 R_4 之两个对称坐标 (Mian := Ben × Zheng); 用户洞察揭示
两个 R_2 因子角色非对称, 一为 carrier 一为 dimension. 这是 doctrine 层之新分类性质.

**How to apply**:
1. 在讨论 R_n × R_n 之具体语义时, **明确指出**两因子之 carrier/dimension 角色, 不要默认对称.
2. 当 codebase (如 BenZheng.lean:230 之 Mian) 用 Cartesian 积时, doctrine 解读可选 carrier-on-Ben 或 carrier-on-Zheng, 不强求.
3. 塔外层 (R_3, R_5, R_6, R_7) 之多重平方路径意味着它们可在不同路径下承担不同元/爻配对, 这是它们"富结构"之具体含义.
4. 形式化层 (Lean) 暂不直接表达 carrier vs dimension 之区分; 此为 doctrine-only 注解.

doctrine 落地: 义理/Z_平方塔自相似规则.md § 5 + yi-RO-hierarchy.md 第十一部分 11.3.
