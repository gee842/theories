---
name: 生生不息 corpus file map
description: Where the key files live in /Users/ren/repos/生生不息/ — saves grep time on this large multi-file philosophy-formal-Lean corpus
type: reference
originSessionId: 7ac48d64-9a82-4a7e-8052-ee6ef59f8d2c
---
## /Users/ren/repos/生生不息/真理/ — today's distill (道理/Daoli v11/v12)

- `daoli-v11.md`, `daoli-v11.1.md` — v11 + frame-connectedness keystone refinement
- `daoli-v12-main.md` — main spec; §3 三面一道 (lines ~207-277)
- `daoli-v12-fa-ze.md` — 62 法则; 法则 12 (自指) at line 713; 法则 60 (三名一道) at line 3227
- `daoli-v12-frames.md` — 8 primary frames (系统/因果/时刻/式量/阴阳/生灭/名实/体用)
- `daoli-v12-theories.md` — 19 theory mappings
- `daoli-v12-verifications.md` — 5 verifications substantiating 法则 53
- `daoli-v12-lean-verifier.md` — Lean 4 verifier blueprint
- `daoli-v12-cross-cultural.md`, `daoli-v12-physics-emergence.md`
- `daoli-v12-he.md` — 完备自指之核 (added in 2026-05-06 milestone)

## /Users/ren/repos/生生不息/ root — yesterday's work (kernel layers)

- `wenyan-operators.md` (126KB) — 算子 catalogue, §24 atomic core, §26 fixed-point, §28 64 hexagrams ↔ operators
- `生生不息论_v13.2_形式项总清与类型校正版.md` — 卷〇 单字根律, 卷一 字元 13 类 (lines 306-541), 卷〇三 DAG
- `生生不息论_v14_形式证明骨架版.md` — §二 8 sorts (78-104), §三 三值 (107-152), §六-§十二 6 metatheorems
- `生生不息论_间开本_致知版.md` — §16 格物致知 (line 786), §17 四校 (line 860)
- `间生论_主篇.md` — 间 ontology, 自显 (lines 13-27), 自相似 §八
- `docs/monad-root-plan.md` — 一元 architecture, 12 面, 43 核心, 221 字元
- `docs/atom-derivation-report.md`

## /Users/ren/repos/生生不息/formal/SSBX/ — Lean 4 formalization

- `Core.lean`, `Roster.lean` — syntax, three-valued logic, 121 registered symbols
- `Foundation/Monism.lean` — ConstructionId 12 faces + 43 cores
- `Foundation/MonadRoot.lean` — 一元 single root, 43 CoreAtom inductive, atom_reachable_to_root, ssbx_reachable_from_root, monad_dag_acyclic
- `Foundation/Kernel.lean` — kernel theorem stubs (added 2026-05-06)
- `Foundation/MathAxiomMap.lean` — math axiom interface contracts
- `Foundation/ShengshengBuxi.lean`, `Foundation/JianOntology.lean`, `Foundation/Li.lean`, `Foundation/HumanAlignment.lean`
- `Truth/Basic.lean` — 三值 truth domain
- `Truth/Absolute.lean` — ledger-dependent absolute truth
- `Text/Completeness.lean`, `Text/WenyanOperators.lean`

## Build

```
cd /Users/ren/repos/生生不息 && lake build
```

Lakefile: `lakefile.lean`; default target = `SSBX` lean_lib with srcDir "formal".

## Plan files

- `/Users/ren/.claude/plans/distill-v11-adaptive-creek.md` — 完备自指之核 plan (approved 2026-05-06)
