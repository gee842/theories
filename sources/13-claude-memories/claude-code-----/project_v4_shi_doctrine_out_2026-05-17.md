---
name: v4-shi-doctrine-out-2026-05-17
description: "V₄ Shi 不作 first-class primitive — squaring tower 派生 Cell. 任何\"时态\"操作从 R-tower 投影获得."
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

User directive 2026-05-17: **V₄ Shi (时, {道/已/今/未}) 不再作独立 first-class axis** — Cell 全部从 squaring tower 派生.

## What this means

- R-tower (R₀/R₁/R₂/R₄/R₈, T_{k+1}=T_k²) 是 cardinality 来源:
  - R₀ = 1 (道)
  - R₁ = 2 (阴/阳)
  - R₂ = 4 (四象)
  - R₄ = 16
  - R₈ = R₄² = 256 = "Cell"
- Cell256 不再写作 `Hex × Shi`；写作 R₈ (= R₄²) 即可
- 任何 "时态" surface 写法都应从 R-tower 投影获得，**不加独立 Shi axis**

## Affected items

| 事 | 状态 |
|---|---|
| Wen 2.0 spec ⑬ Cell-level operations (V₄ Shi binding) | **删除** — PR #49 (2026-05-17) |
| `Cell256` 类型仍存在 | OK — 是 R₈ 之名，不是 Hex×Shi |
| project_v4_migration_complete.md (2026-05-10) | **历史 record**, 不再表示当前 doctrine. 80-file migration 是 Cell192→Cell256 重排 (cardinality 维护), shi-as-separate-axis 之 reify 已弃 |
| project_final_theory_2026-05-10.md "V₄ Shi {道,已,今,未}" | **过时** — Cell256 仍是 256，但 axis 由 R₄² 给出，不是 Shi |
| project_squaring_tower.md | **doctrine** — 这就是 V₄ Shi 之上位 |

## Why

Operation monism (§3.7, [[project_operation_monism]]): "操作≡位≡被操作内容". 引入独立 Shi axis 会破单一 substrate. Squaring tower 已 universal — Cell 是 R₈ 之实例化, 不需 Hex × 任何额外结构.

## How to apply

- **不要** spec/code 中引入新 "时" 之 surface 写法 (无 `卦·时`, 无 `(乾, 已)`, 无 `设时 X`)
- 写 Cell256 时, 解作 R₈ = R₄² (squaring tower), **不**解作 Hex × Shi
- 旧 V₄ migration 文件之"shi axis"措辞是 deprecated; 引用 squaring tower 取代
- 见 [[project_squaring_tower]] / [[project_operation_monism]] 为正本 doctrine
