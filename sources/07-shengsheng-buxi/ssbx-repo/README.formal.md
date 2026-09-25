# SSBX · Formal Specification

> Status: v3 snapshot (2026-05-11) — strict (Z/2)ⁿ uniform R₀..R₈ ladder; V₄ Klein time-modes (Shi) at R₈; Cell256 = 64 hex × 4 Shi; 道 = R₈ origin = (Z/2)⁸ identity. v3-snapshot numerics: lake build 3686/3686 jobs; 0 sorry / 0 project-custom axioms across migrated files + Foundation/Squaring; 1 opaque (theOne) + 1 partial def (BaguaTuring.run).
>
> **Current formal status (2026-05-21)**: this document is a v3-era specification. Since then `Foundation/Bagua/` has been retired (contents moved under `Foundation/Atlas/Yi/`), Doctrine / Order / Enriched / R / wen-substrate research clusters carry the current open obligations, repository-wide `sorry` is ~150 documenting research debt (mostly in `Foundation/Order/FrameBimorphism.lean` (19), `Foundation/Doctrine/Instance/*`, `Foundation/Enriched/Power.lean`), and project axioms are ≥ 1 (in `Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean`). The single honest current source is [docs-next/10_formal_形式/claim-status-ledger.md](./docs-next/10_formal_形式/claim-status-ledger.md) v0.8 (2026-05-21).

> [中文](./README.md) · [English](./README.en.md) · **形式 / Formal**

```
package        : ssbx
language       : Lean 4 v4.30.0-rc2
upstream       : Mathlib master @ ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa
build target   : @[default_target] lean_lib SSBXCore (srcDir = "formal", roots = #[`SSBX.Core])
full library   : lean_lib SSBX (srcDir = "formal", entry index in formal/SSBX.lean)
build status   : v3 snapshot 3686 jobs ✓ (current scale larger; see ledger)
                  sorry : v3 snapshot 0 — current ~150 documenting research debt (Order/FrameBimorphism.lean 19, Doctrine/Instance/*, Enriched/Power.lean, etc.)
                  project axiom : v3 snapshot 0 — current ≥ 1 in Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean
                  opaque : 1
partial defs   : 1 top-level executable definition (not an additional axiom)
trust base     : Lean kernel + Mathlib HEAD
namespace root : SSBX
binaries       : wenyan-surface (WenSurface 受控文言 CLI)
                 wenyan         (字文 / ziwen v0 CLI)
```

This document is the **formal-layer** companion to [`README.md`](./README.md) (中文) and [`README.en.md`](./README.en.md) (English prose). It catalogs modules, theorem statuses, and trust-base invariants — *not an introduction*. For the doctrinal motivation see the top-level READMEs and [docs-next/10_formal_形式/yi-RO-hierarchy.md](./docs-next/10_formal_形式/yi-RO-hierarchy.md) (the canonical v3 doctrine).

---

## 1 · Trust Base

### 1.1 Sole Opaque (foundational seal)

```lean
opaque theOne : One
-- Foundation/Wen/Kernel.lean § Layer 0
-- structure One carries (state : Type) (dong : state → state)
--                       (origin : state) (alive : dong origin ≠ origin)
-- Preserves Field/dong/origin abstraction.
```

### 1.2 Derived from theOne (not axioms)

```lean
abbrev Field           : Type           := theOne.state
noncomputable def dong : Field → Field  := theOne.dong
noncomputable def origin : Field        := theOne.origin
theorem origin_alive   : dong origin ≠ origin := theOne.alive
-- Encodes: "the One moves, and self comes to be" (一动而有自).
-- All in Foundation/Wen/Kernel.lean.
```

### 1.3 Project-axiom count: 0 (v3 snapshot)

In v3 the `kleene_recursion_axiom` previously stated in `Foundation/Bagua/GodelLi.lean` was internalised behind cuo-equivariance machinery in `Foundation/Bagua/CuoInvariance.lean § unrestricted_kleene_inverter_inconsistent` (current paths: `Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean` and `Foundation/Atlas/Yi/Classical/Algebra/CuoInvariance.lean`). The boundary it formerly marked (universal-`compileTm` undefinable) was witnessed without an explicit `axiom` declaration in migrated paths.

> **Current formal status**: as of 2026-05-21 the repository contains at least one explicit `axiom` declaration in `Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean`. See [docs-next/10_formal_形式/claim-status-ledger.md](./docs-next/10_formal_形式/claim-status-ledger.md) v0.8 for the up-to-date axiom inventory.

### 1.4 Machine-checked facts and executable boundary

Machine-checked theorem claims reduce to Lean kernel + `Mathlib master` reduction rules, plus the single opaque seal above. Documentation, roster, DAG, operator and cross-volume correspondence claims are ledger-dependent sync claims; they are not silently promoted to closed-theorem status.

No `#allow_unsafe`. The repository contains exactly 1 top-level `partial def` in `formal/`:

```
Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean     YiState.run
```

It forms the executable nontermination boundary. It is tracked as an implementation boundary, not as an additional `axiom` or `opaque` constant; proof-critical total behaviour is stated through total / fueled variants or finite `native_decide` witnesses where applicable (`runFuel` is the total-recursive Bagua interpreter used in proofs; `WenyanParser` and `WenDefEval` are now total).

---

## 2 · v3 R-Hierarchy (R₀..R₈ strict (Z/2)ⁿ uniform)

### 2.1 Doctrine layers and their Lean realisations

| R-layer | Size | Name | Lean type | Key file |
|---|---|---|---|---|
| R₀ | 1 | 太极 (Taiji) | `Unit` | (Lean stdlib) — referenced via `Foundation/Hierarchy/R0_Taiji.lean` shim |
| R₁ | 2 | 爻 / 两仪 (Yao) | `Yao` (= `Bool`-flavoured) | `Foundation/Atlas/Yi/Classical/Core/Yi.lean` |
| R₂ | 4 | 四象 (SiXiang) | `SiXiang` | `Foundation/Atlas/Yi/Classical/Algebra/BaguaAlgebra.lean` |
| R₃ | 8 | 八卦 (Trigram) | `Trigram` | `Foundation/Atlas/Yi/Classical/Core/Yi.lean` |
| R₄ | 16 | 面 Mian = Ben × Zheng | `Ben × Zheng` | `Foundation/Atlas/Yi/Classical/Algebra/BenZheng.lean` (and `Foundation/Atlas/Yi/BenZheng.lean`) |
| R₅ | 32 | 五爻 (Wuyao, provisional) | `Mian × Bool` | `Foundation/Hierarchy/R5_Wuyao.lean` |
| R₆ | 64 | 重卦 (Hexagram) | `Hexagram` | `Foundation/Atlas/Yi/Classical/Core/Yi.lean` |
| R₇ | 128 | 因卦 (Cell128 = Hex × YinBit) | `Hexagram × YinBit` | `Foundation/Atlas/Yi/Cell128.lean` |
| R₈ | 256 | 果卦 (Cell256 = Hex × Shi) | `Hexagram × Shi` | `Foundation/Atlas/Yi/Cell256.lean` |

The **umbrella entry** is [`Foundation/Hierarchy/RHierarchy.lean`](./formal/SSBX/Foundation/Hierarchy/RHierarchy.lean), which re-exports R0_Taiji..R8_GuoHex aliases plus the cross-cutting LiftProject and Operators modules.

### 2.2 Cross-cutting structure

| Concept | File |
|---|---|
| 8 uniform Lift_n / Project_n pairs + retract `proj_lift_id_Rn` | `Foundation/Hierarchy/LiftProject.lean` |
| XOR subgroup atomic generators (yin/tou/flipᵢ/hexCuo) | `Foundation/Hierarchy/Operators/Atomic.lean` |
| V₄ Klein outer (zong/cuoZong/hu) | `Foundation/Hierarchy/Operators/V4.lean` (formerly `V4Outer.lean`) |
| `OX["xxxxxxxx"]` 8-char Cell256 string-literal macro | `Foundation/Notation/OXNotation.lean` |

### 2.3 Algebraic spine on R₇ / R₈

Both `Cell128` and `Cell256` carry `Add` / `Zero` / `Neg` / `Sub` instances with origin = (qian, dao) = V₄ identity, plus a `SMul` self-action via XOR (Cayley regular representation). At R₈:

```lean
abbrev R8 := Cell256

instance : Add  Cell256 := ⟨Cell256.xor⟩
instance : Zero Cell256 := ⟨Cell256.origin⟩       -- = (Hexagram.qian, Shi.dao)
instance : Neg  Cell256 := ⟨id⟩                   -- (Z/2)ⁿ self-inverse
instance : Sub  Cell256 := ⟨Cell256.xor⟩
instance : SMul Cell256 Cell256 := ⟨Cell256.xor⟩

-- Cayley
def cayley (c : Cell256) : Cell256 → Cell256 := fun s => xor c s
def epsAtOrigin (f : Cell256 → Cell256) : Cell256 := f origin
@[simp] theorem epsAtOrigin_cayley (c) : epsAtOrigin (cayley c) = c
theorem cayley_inj : Function.Injective cayley
theorem cayley_hom (c1 c2) : cayley (xor c1 c2) = cayley c1 ∘ cayley c2
```

(See `Foundation/Atlas/Yi/Cell256.lean § 7`.)

### 2.4 印 / 投 as XOR masks (Phase A)

```lean
def yin_mask : Cell256 := (Hexagram.qian, Shi.ji)   -- only YinBit set
def tou_mask : Cell256 := (Hexagram.qian, Shi.wei)  -- only GuoBit set

def yin (c : Cell256) : Cell256 := xor c yin_mask
def tou (c : Cell256) : Cell256 := xor c tou_mask

theorem yin_yin (c) : yin (yin c) = c
theorem tou_tou (c) : tou (tou c) = c
theorem yin_tou_comm (c) : yin (tou c) = tou (yin c)
theorem yin_tou_eq_central (c) : yin (tou c) = xor c (Hexagram.qian, Shi.jin)
theorem yin_mask_xor_tou_mask : xor yin_mask tou_mask = (Hexagram.qian, Shi.jin)
```

The two masks XOR to `(qian, jin)` = the V₄ central element ("PT").

### 2.5 V₄ Shi at R₈

```lean
inductive Shi
  | dao   -- (false, false) — V₄ identity
  | ji    -- (true,  false) — past, P-like
  | jin   -- (true,  true)  — present, PT central
  | wei   -- (false, true)  — future, T-like

def toYinGuo : Shi → Bool × Bool
def ofYinGuo : Bool × Bool → Shi
theorem ofYinGuo_toYinGuo (s) : ofYinGuo (toYinGuo s) = s
theorem toYinGuo_ofYinGuo (yg) : toYinGuo (ofYinGuo yg) = yg

def Shi.cuo / Shi.zong / Shi.cuoZong  : Shi → Shi   -- V₄ Klein involutions
theorem cuo_cuo / zong_zong / cuoZong_cuoZong       -- each is involutive
theorem cuo_zong_comm                               -- V₄ abelian
theorem cuoZong_eq_compose                          -- cuoZong = cuo ∘ zong
```

(See `Foundation/Atlas/Yi/Cell256.lean § 1`.)

---

## 3 · «一»-DAG (Single-Root Generation Tree)

> Source-of-truth: `formal/SSBX/diagrams/MonadDAG.mmd` (1533 lines, generated by `scripts/generate_monad_dag.py` from Lean sources). Below is the compressed listing — *unique-root, acyclic, fully covered.*

### 3.1 Layer 0 — Root

```
一元    (the One; the unique root of all generation)
```

### 3.2 Layer 1 — 12 Faces (面)

```
一元
  ├─ 文面          (语言 / 字 / 解 / 印 / 自宿主)
  ├─ 物面          (象 / 物理 / 量子 / SU(N))
  ├─ 生面          (生 / 续 / 仁 / 共开 / 道)
  ├─ 理面          (推 / 算 / 数 / 测 / 范畴)
  ├─ 心面          (识 / 知 / 注意 / 神经)
  ├─ 人面          (天之子 / 意识 / 做人 / 向齐生)
  ├─ 模面          (Model / Γ-Process / DaoCriteria)
  ├─ 审校面        (审 / 校 / 验 / 反诛心)
  ├─ 价值面        (好 / 坏 / 自由 / 繁荣)
  ├─ 证明面        (claim / 公示 / 见证 / 反例)
  ├─ 注意面        (聚焦 / 门控 / 维持 / 转焦 / 抑制)
  └─ 真理面        (真 / 真道 / 度期周 / 所是)
```

### 3.3 Layer 2 — 43 Core Single Characters (核心单字)

```
一  之  人  仁  做  元  共  动  变  场
天  夺  子  审  序  度  开  形  心  意
成  控  期  校  模  正  法  注  焦  物
理  生  真  算  续  聚  行  证  识  道
邪  闭  齐
```

Each is registered as `AtomName` in `Roster.lean § AtomName` and projected to its layer-1 face by `MonadDAG.mmd` edges. Total atoms in registry: 350+ (see `Roster.lean § allAtoms`); **43 of these are core**.

### 3.4 Layer 3 — generated compounds + recursive items + primitives + pending

```
GenName   :   134 compound names      (Roster.lean § GenName)
RecName   :    13 recursive items     (Roster.lean § RecName)
PrimName  :     5 primitive operators (Roster.lean § PrimName)
PendName  :     6 pending interfaces  (Roster.lean § PendingName)
```

**Five Primitive Operators (PrimName)** — note that the carrier moved from `Cell192` to `Cell256` in v3 (`P .«格»` now denotes the 256-cell carrier):

| Symbol | Lean | Domain | Reading |
|---|---|---|---|
| 域 | `P .«域»` | `Type` | universe / domain |
| 格 | `P .«格»` | `Cell256` | 256-cell carrier (was `Cell192` in v2) |
| 权 | `P .«权»` | `Nat` | weight |
| 生 | `P .«生»` | `Field → Field` | becoming (= `dong`) |
| 校 | `P .«校»` | `Prop → Bool` | audit / verify |

**Thirteen Recursive Items (RecName)**

```lean
-- Roster.lean § recDeps
开  := [未, 可, 应, 转]                stratified
闭  := [断, 机, 成, 元, 夺, 蔽, 伪]    threeValued
正  := [开, 合, 法, 审校不败]          threeValued
邪  := [偏, 伪, 夺, 闭]                threeValued
共开 := [开, 共, 存]                   threeValued
好  := [平, 和, 正危]                  threeValued
坏  := [闭, 夺, 伪]                    threeValued
自由 := [自, 由, 可择, 可识, 可达, 被迫]  threeValued
义  := [机, 择, 正]                    threeValued
善  := [义, 正筛]                      threeValued
仁  := [己续, 共续]                    threeValued
道  := [正续, 共开, 夺共续, 坏]        gfp           ← greatest fixed point
真  := [所是, 相关度期, 审校不败]      externalAudit
```

**Six Pending Interfaces (PendingName)**

```
邪续 · 开势投影 · 审校数据 · 正邪阈值 · 度期计算 · 经验校准
-- All have kind = .pending; sort = .truth; await empirical calibration.
```

### 3.5 Layer 4 — 16 Construction Stages (构造阶段)

```
yuanTriad      → gammaFieldRoot   → openCloseCore     → systemDynamics
ssbxTheory     → cicAsFormalModel → modelAdequacyCore → universalProofPrinciple
truthCore      → auditCore        → valueCore         → actionCore
attentionCore  → aspectTriad      → humanAlignmentCore → jianRoot
```

These are stages in the layered construction (`Foundation/Core/AtomDerivation.lean` et al.).

### 3.6 Layer 5 — claims (公示)

Selected (full set in `Roster.lean § allEntries.filter (·.kind = .claim)`):

```
名册文字完备                 (rosterCompleteness)
生成项有根                   (generatedRootsDiscipline)
recursiveSemanticDiscipline
文言算子表完备               (wenyanOperatorTableComplete)
semanticAdequacyClaim
kernelToShengshengClosure
trueDaoDefinition / trueDaoPathAxiom
道 / 仁 / 善 / 正 / 好 / 坏 / 闭 / 开 / 自由 / 繁荣  definitions
openValueAxiom / auditReliabilityAxiom / auditUndefeatedDefinition
threeValuedConservativity / absoluteTruthInSystem
Ω / Ω_B / Π_开 sufficiency axioms + interfaces
recommended cases i1/i2/i3
thresholdProtocol / textualClaimMapping
```

---

## 4 · Operator Catalogue

### 4.1 L0 — 12-Instruction ISA (`Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean § YiInstr`)

> Note: PR #37 (universal-ISA upgrade) added `branchYaoYang` and lifted the cuo-equivariance ceiling of the v3 ISA; the 12-instr table below remains accurate as a historical reference but does not capture the current universal ISA. See [docs-next/10_formal_形式/claim-status-ledger.md](./docs-next/10_formal_形式/claim-status-ledger.md) v0.8.

| Token | Lean ctor | Type signature | Operational |
|---|---|---|---|
| 不动 | `nop` | `YiInstr` | pc ← pc+1 |
| 设时 | `setShi (s : Shi)` | `Shi → YiInstr` | cur.2 ← s |
| 翻爻 | `flipYao (i : Fin 6)` | `Fin 6 → YiInstr` | cur.1.flipPos i |
| 互 | `hu` | `YiInstr` | cur.1 ← Hexagram.hu cur.1 |
| 错 | `cuo` | `YiInstr` | cur.1 ← Hexagram.cuo cur.1 |
| 综 | `zong` | `YiInstr` | cur.1 ← Hexagram.zong cur.1 |
| 比爻 | `branchYaoEq (i j : Fin 6) (t : Nat)` | `Fin 6 → Fin 6 → Nat → YiInstr` | if y_i = y_j then pc ← t else pc ← pc+1 |
| 比时 | `branchShiEq (s : Shi) (t : Nat)` | `Shi → Nat → YiInstr` | if cur.2 = s then pc ← t else pc ← pc+1 |
| 跳 | `jump (t : Nat)` | `Nat → YiInstr` | pc ← t |
| 推 | `push` | `YiInstr` | history ← cur :: history |
| 取 | `pop` | `YiInstr` | (cur, history) ← head/tail history (∅ ⇒ halt) |
| 终 | `halt` | `YiInstr` | halted ← true |

```
Carrier (v3):
  Hexagram        := Yao⁶                                (Atlas/Yi/Classical/Core/Yi.lean)
  Shi             := V₄ {dao, ji, jin, wei}              (Atlas/Yi/Cell256.lean § 1)
  Cell256         := Hexagram × Shi                      (Atlas/Yi/Cell256.lean § 2)
  YiState         := { cur, history, pc, prog, halted }  (Atlas/Yi/Classical/Computation/BaguaTuring.lean)

Frozen surface tokens (BaguaWenSpec.lean § reservedTokens, |·| = 22):
  primaryTokens   = [不动 设时 翻爻 互 错 综 比爻 比时 跳 推 取 终]   (12)
  shiTokens       = [已 今 未]                                       (3, dao implicit)
  yaoTokens       = [初爻 二爻 三爻 四爻 五爻 上爻]                  (6)
  atKeyword       = [至]                                             (1)

Numeral range: 1..64 (parseNumeral covers full range; round-trip witnessed
on numeralRange = (List.range 64).map (·+1)).
```

#### 4.1.1 Expressive ceiling

```lean
theorem sheng_not_cuo_equivariant :
    ¬ ∃ (p : List YiInstr) (init : Hexagram),
        ∀ h : Hexagram, runHex p init h = h.shengSucc
-- Foundation/Wen/WenDefCompile.lean
-- The 12-instr ISA cannot compute non-cuo-equivariant Hex→Hex functions.
-- «生», «一» are structurally unreachable; Hex→Hex computability ceiling = cuo-equivariance.
```

### 4.2 L1 — Typed Lambda Layer (`Foundation/Wen/WenDef.lean § Tm`)

```lean
inductive Ty  | hex | bool | arr (dom cod : Ty)
inductive Tm
  | var | abs | app | hexLit | boolLit
  | jia    -- 加  : Hex → Hex → Hex
  | yi     -- 一  : Hex
  | notB   -- 不  : Bool → Bool
  | andB   -- 並  : Bool → Bool → Bool
  | orB    -- 或  : Bool → Bool → Bool
  | eqHex  -- 同  : Hex → Hex → Bool
  | forallH -- 凡 : (Hex → Bool) → Bool        (64-fold ∧, decidable)

typeCheck : Ctx → Tm → Option Ty                        -- total
eval      : Tm → Tm                                      -- structural
```

### 4.3 Root-native operators and legacy catalogue quarantine

L1 type-layer is in `WenDef.lean § Stdlib` (representative constructors: {tui, bi, bu, biModal, tong, fan, sun, yiBenefit, cuo, zong, hu, fanReverse, imp, neqHex, existsH, noneH, endoComp}); a subset of the surface particles (之 / 者 / 而 / 也 / 不 / 凡 / 自 / 相 / 似 / 要 etc.) is named in `Foundation/Wen/Operators.lean` with ASCII aliases. The v3 structural entry is `Foundation/Wen/RootOperator.lean`: root-native operators are `mask`, `program`, `projection`, or `alias`.

The historical operator catalogue remains machine-tracked in `Text/WenyanOperators.lean` and related Text modules as legacy inventory. It may supply aliases, corpus rows, or evidence notes, but catalogue size is not root ontology and not a completeness proof.

### 4.4 Controlled Wenyan (M1 grammar)

```ebnf
程       ::= 句*
句       ::= 命 sep
sep      ::= "；" | ";"
命       ::= 不动 | 互 | 错 | 综 | 推 | 取 | 终
           | 设时 时
           | 翻爻 爻
           | 比爻 爻 爻 至 数
           | 比时 时 至 数
           | 跳 至 数
时       ::= 已 | 今 | 未
爻       ::= 初爻 | 二爻 | 三爻 | 四爻 | 五爻 | 上爻
数       ::= ⟨1..64⟩
```

Round-trip witness:

```lean
theorem daoJudgeProg_roundtrip :
    «解程» («印程» daoJudgeProg) = some daoJudgeProg     -- by native_decide

theorem testPrograms_roundtrip :
    testPrograms.all (fun p => «解程» («印程» p) = some p) = true
                                                          -- by native_decide
```

---

## 5 · Module Path → Theorem (Compressed Inventory)

### 5.1 Foundation/Atlas/Yi (algebra of 易; merged successor of v3 `Foundation/Yi/` + `Foundation/Bagua/`)

```
Classical/Core/Yi.lean             v4_orders, hu_fixed_point, oplus_not_comm, pi_ne_tai
Classical/Core/YiCore.lean         «微核之至», «周而复始», «生生不息», «法即卦», «道生一也»
```

### 5.2 Foundation/Atlas/Yi (continued: 256 / Turing / Gödel / cuo / etc.)

```
Classical/Algebra/BaguaAlgebra.lean         Boolean algebra of trigrams + V₄ orders
Classical/Algebra/BenZheng.lean             4 Ben / 4 Zheng / Mian = R₄ (16) / Quadrant 4 partitions
                                            (also re-exported at Atlas/Yi/BenZheng.lean)
Atlas/Yi/Cell128.lean                       R₇: Hexagram × YinBit (128 cells) + YinBit / 印 atom
Atlas/Yi/Cell256.lean                       R₈: Hexagram × Shi (256) + Shi V₄ + (Z/2)⁸ algebra (Add/Zero/Neg/Sub + SMul + Cayley ι/ε) + 印/投 mask + 序卦 (King Wen) order
Classical/Cells/R8Stratify.lean             R₀..R₈ explicit stratification + R8_complete bundle (was Cell256Stratify.lean in v3, was R6_complete in v2)
Classical/Computation/BaguaTuring.lean      12-instr ISA Turing-completeness; daoJudge_correct, loopProg_unbounded
Classical/Computation/BaguaWenSpec.lean     reservedTokens.length = 22, primaryToken_in_primaryTokens
Classical/Diagonal/GodelLi.lean             halts_undecidable_internally; halts_cuo_invariant
                                            (contains the repository's only explicit `axiom`; see ledger)
Classical/Diagonal/KleeneInternal.lean      Kleene fixpoint internalised
Classical/Algebra/Newman.lean               Newman's lemma local form
Classical/Algebra/CuoInvariance.lean        cuo-equivariance machinery; unrestricted_kleene_inverter_inconsistent
Classical/Computation/ChunkedDecide.lean    decision-procedure budget framework
Classical/Computation/FuelDiscipline.lean   runFuel monotonicity + fuel-extension lemmas
```

### 5.3 Foundation/Hierarchy (R₀..R₈ index alias + cross-cutting)

```
RHierarchy.lean             umbrella: re-exports R0_Taiji..R8_GuoHex, LiftProject, Operators/*
R0_Taiji.lean   .. R8_GuoHex.lean   thin re-export shims giving R-index naming (no new logic)
LiftProject.lean            8 uniform Lift_n / Project_n pairs + proj_lift_id_Rn retract lemmas
Operators/Atomic.lean       XOR-subgroup atomic gens (yin/tou/flipᵢ/hexCuo) re-exported from Cell{128,256}
Operators/V4.lean           V₄ Klein outer (zong/cuoZong/hu) at every R₃+ layer (formerly V4Outer.lean)
ZoneClassifier/             任意位 oxox 全轴判定 + 道/理/可理/墙 子集化（第二轮收紧）
  Types.lean                Zone / WallTag / RiceQuadrant / OperatorTag / Classification (5 字段)
  WallCitations.lean        11 条 cited_* 单行 wrap 既证墙定理（证据流入口）
  Operators.lean            applyUnary (每 op 之结构性一元行动) + apply (Option 签名) + composeZone (Zone.level + max) + sheng_no_fixed_point
  Axes.lean                 extractShi only (Behavior/Claim/Modality 已删除——无诚实派生)
  Classify.lean             classify 5-step priority + detectWalls (cell-independent) + 阈值由 op.applicable n 派生
  Subsets.lean              daoSubset/liSubset/keLiSubset/wallSubset + subsets_partition + dao_via_shengshengbuxi
  Interaction.lean          interact (apply Option-aware) + wall-absorption theorems
  Examples.lean             5 条 #eval smoke tests
ZoneClassifier.lean         顶层入口（re-exports 全部子模块）
```

**核心定理**（在 `ZoneClassifier/Subsets.lean`）：
- `dao_via_shengshengbuxi : daoSubset 6 .yiCore_step = Finset.univ`
  —— 证明严格通过 `orbit_witness`（= `«生生不息»`）+ `sheng_no_fixed_point` 派生，
     非定义型真值赋予；`#print axioms` 之依赖图含 YiCore.«生生不息»
- `subsets_partition / subsets_disjoint_*` —— 由 Zone 构造子互斥性派生
- `WallCitations.all_citations_typecheck` —— 同时引用 11 条墙定理强制 type-check
- `composeZone` —— 由 `Zone.level + max` 派生，**不依赖任何公理**（#print axioms 显示 empty）

**证据流第二轮收紧**（消灭 11 处定义型真值）：
- 删除 `encodesSheng`、`extractBehavior`、`extractClaim`、`extractModality`、`Lift.lean`（全为定义型默认）
- `detectWalls` 改为 cell-independent；每 op→walls 之映射在 Classify.lean docstring 有结构理由表
- `composeZone` 由 5×5 硬编码表改为 `Zone.level + max` 之派生
- `apply` 改为 `Option (BitSpace n)`，无自然二元行动者返回 `none`（非任意 fst fallback）
- `classify` 阈值 `n < 8` 改为 `op.applicable n` 派生
- 实际 dao_axiom 子集（256/0/1/64/2/8/1/0）从规则**自动算出**，无显式枚举

### 5.4 Foundation/Notation

```
OXNotation.lean             `OX["xxxxxxxx"]` term macro: 8-char `o`/`x` → Cell256 literal,
                             with parse-time length and charset validation; `OX["oooooooo"]` = Cell256.origin = dao
```

### 5.5 Foundation/Squaring (L-tower after R₈ closure)

```
V4Tensor.lean        Cell256 ≃+ (V₄ × V₄ × V₄ × V₄), with Mathlib Fintype/AddCommGroup instances
L1.lean              L₁ = Cell256 × Cell256, swap/diag/proj, atomic flips, octant partition
RetractTower.lean    R₀..R₈ retracts into L₁; generic square retracts for lower R-layers
StreamCarrier.lean   TrajCell = Stream' Cell256, step/unfold/bisim anchors
ProfiniteLimit.lean  L∞ coherent prefixes, L∞ ≃+ Stream' Cell256, terminal Endofunctor.Coalgebra package
```

### 5.6 Foundation/Wen (Path 丙: self-compilation, self-validation)

```
BaguaWenSpec → WenyanParser → WenyanParserGeneral
              ↘             ↘
                WenEval → WenDef → WenDefEval → WenDefCompile
                       ↘                              ↘
                         WenyanSyntax → WenyanSelfInterp → Atlas/Yi/DaoSource
                                            ↘
                                            AntiSchmitt, AlignmentFailures, EconGame

Note: WenyanReflect.lean / WenyanSelfHost.lean / Demo.lean were retired after v3; their
content («文核同源», «微核自验», «微核自释_total», daojudge_{qian,kun,pi,tai}) was
reorganised into adjacent modules. See ledger.

WenyanParser.lean         daoJudgeProg_{print,roundtrip}, allKindReprs_singleton_roundtrip
WenyanParserGeneral.lean  parseProgN_tokensOfProg (full generality, non-partial);
                          M1 v3.1 lexN_printProg_thm + parseN_printProg_inverse_universal
WenEval.lean              «端到端_乾», «端到端_坤», «端到端_否»
WenDef.lean               typeCheck total + 17-body Stdlib (core Hex/Bool + logic aliases)
WenDefEval.lean           tui_eq_sheng + exact Hex transforms + promoted logic examples
WenDefCompile.lean        {idProg, add32Prog, cuoProg}_correct, sheng_not_cuo_equivariant
                          (cuo-equivariance ceiling — see PR #37 universal-ISA upgrade in ledger)
WenyanSelfInterp.lean     Tier 3 partial: Quine.quine{3,5,16}_history (uniform [push]^N);
                          Tier 3 ground: ProgEnc.{encFramedProg, decFramedProg, ...};
                          (future) universal buildEmitProg + diagonal: roadmap construction, not yet written in any carrier
Foundation/Atlas/Yi/DaoSource.lean   «道之自指» (form / parse / print / halt / semantics 5-fold)
WenSurface/Lex.lean        controlled-wenyan lex
WenSurface/Reading.lean    operator readings table
WenSurface/Semantics.lean  executableSemanticsFor? — legacy catalogue inventory; implementation only, not ontology
WenSurface/Syntax.lean     surface syntax
WenSurface/Elaborate.lean  surface elaboration
WenSurface/EndToEnd.lean   canonicalHexNames_interpret_to_xuGua + CLI integration
WenSurface/Coverage.lean   coverage inspection
Kernel.lean                45-layer doctrine in-source (incl. Layer 46 doctrinal refinements)
AntiSchmitt.lean           friend-enemy / decisionism / exception ⊨ ¬universalisable
AlignmentFailures.lean     Goodhart / mesa / wireheading ⊨ Kernel-invariant violation
EconGame.lean              coase_internalizes_externality, prisoners_dilemma_refuted_under_tongGen

MetaInterp/                Phase 2.3 series (~40 modules; up from v3's 16):
  SkipInstr / ExecuteBlock / Block_HuCuoZong / Block_SetShi_FlipYao /
  Block_Jump / Block_Branches / Block_PushPop /
  Fetch / Dispatch / SubDispatch_BranchShiEq / SubDispatch_BranchYaoEq /
  OuterLoop / TargetContract / Assembly / PrologueProg / FullUniversalBoundary /
  R4Carry* (R4 carry sub-tree) / Universal / GodelR8 / Fetch* + Dispatch* extensions
  → v3 snapshot: 12/12 cur-effect + dispatch + universal compose proven
                 (native_decide + Lean-parametric). Current proof status of the
                 R4-carry / FullUniversal extensions: see ledger.

Embeddings/                Heisenberg-Weyl G11 (parametric over any odd prime p):
  HeisenbergWeylZModP.lean       G11 over Z/pZ (additive / multiplicative laws)
  HeisenbergWeylOperators.lean   shift / clock operators
  StabilizerQM.lean              stabiliser code formalism
  HilbertPauliFunctor.lean       Hilbert ↦ Pauli functor (1 sorry, currently)
  PauliRingIso.lean              ring isomorphism witness
  PhasedPauli.lean               phased Pauli construction
  FOL.lean                       first-order language sketch
  → G11 closed at the abstract level. **Not yet bridged to Cell256 / R₈ / 易卦.**
    See [docs-next/10_formal_形式/heisenberg-weyl-narrative.md](./docs-next/10_formal_形式/heisenberg-weyl-narrative.md) (in draft).
```

### 5.7 Foundation/Core (alignment / sincerity / human / community)

```
Yuan.lean                Yuan := Yao; yi := Yao.neg; 元/爻/易 identifications
Monism.lean              proof-principle: 一切回 一; explicit (no Lean axiom)
MonadRoot.lean           single-root proof-shape lemmas
AtomDerivation.lean      every AtomName ∈ allAtoms (decide)
ShengshengBuxi.lean      ShengshengBuxi 主公示
Alignment.lean           T1–T6: ProcessAligned + Open → Dao → ShengshengBuxi; ShengshengBuxi → Dao; Denier 自毁
Sincerity.lean           T1–T8: 信/诚 = alignment(化(T), 化(E)) + 反诛心五律
HumanAlignment.lean      structure HumanDefinition / DoingHumanDefinition; 12 stages
Attention.lean           注意机制 5 components (动态权重分配/门控/维持/转焦/抑制)
EvolutionDao.lean        scale/value/reflexive 三视: σ_F ⊉ Σ_真道
Renlei.lean              «人类命运共同体_之证» (3-axis CommunityState, iff-aligned)
Li.lean                  理之分层
MissingGlyphs.lean       missing-character coverage
MathAxiomMap.lean        ZFC↔SSBX axiom mapping
```

### 5.8 Foundation/Eight (eight expansions)

```
ShuSuan.lean             algebra of computation
LuoJi.lean               logic / deduction
TongJi.lean              statistics
XingWei.lean             geometric position
LeiYing.lean             category / isomorphism
DongLi.lean              dynamics / ODE
XinZhi.lean              mind / neuroscience
WuXiang.lean             physics / quantum
```

### 5.9 Foundation/Modern (Mathlib bridge)

```
RCauchy / RCauchyExt          Real Cauchy-completeness
Kolmogorov / KolmogorovExt    Kolmogorov measure
Lebesgue / LebesgueDepth      MCT / DCT / Fubini
ODESmoothness                 ODE smoothness
PicardLindelofGen / BochnerPL Picard-Lindelöf (incl. Mathlib instance)
NaturalDeduction              K3/NK collapse + Curry-Howard
Quantum / SUN                 quantum mechanics + SU(N)
Neuro                         neuroscience integration
HexagramPosition              中/应/比/当位/承乘
CatExt / CatOp / YonedaFull   category theory + Yoneda functor
IIDWlln                       WLLN (Chebyshev + IID-aware)
DaoLi                         道-理 bifurcation, cross-cutting
HistoryTapeStructure
WuJianShiTrinity              物 / 间 / 事 三位一体
QuantumRelativity*Bridge      60+ stepwise unification bridges (Markov-bridge composition)
UnityBoundary / KnowableBoundary / KeBoundary / QuantumSpacetime    boundary refinements
```

### 5.10 Truth / Model / Text / Pending

```
Truth/SelfDescription.lean    Cell256OperatorComplete (was Cell192-version), full self-description closure
Truth/Basic / ClaimLedger / Semantics / Adequacy / Absolute   claim grading machinery
Model/Adequacy / ConcreteLedger                                model-side ledger
Text/Glyph                                                     glyph layer
Text/WenyanOperators                                           legacy operator catalogue inventory
Text/OperatorReadings / OperatorSignatures                     operator readings + signatures
Text/OperatorFamilySemantics / OperatorReachabilitySemantics   family / reachability semantics
Text/OperatorInstructionSemantics                              operator → ISA instruction semantics
Text/OperatorCellCandidateSemantics / OperatorCellSemantics    candidate + cell-level semantics (Cell256-indexed)
Text/OperatorCellMap                                           legacy operator × Cell256 index; audit inventory, not ontology
Text/OperatorAnchors                                           xuGua-aligned operator anchors
Text/Completeness                                              legacy inventory consistency theorems
Pending/Interfaces / Examples                                  6 PendingName interfaces with kind = .pending
```

---

## 6 · Headline Theorems (one-liner statements)

```lean
-- A. micro-kernel
theorem «微核之至»    : YiCore covers 64 hexagrams in ≤ 64 steps      (YiCore.lean)
theorem «生生不息»    : ∀ h₁ h₂ : Hexagram, ∃ n < 64, step^n h₁ = h₂  (YiCore.lean)

-- B. 易 algebra
theorem v4_orders     : ∀ h, h.cuo.cuo = h ∧ h.zong.zong = h ∧ h.cuoZong.cuoZong = h
theorem hu_fixed_point: h.hu = h ↔ h = qian ∨ h = kun

-- C. R₈ algebraic spine (Foundation/Atlas/Yi/Cell256.lean § 7-9)
theorem cell256_phaseA_summary : (Z/2)⁸ identity + group laws + Cayley fusion + 印/投 mask involutions all ✓

theorem cayley_inj          : Function.Injective Cell256.cayley
theorem cayley_hom (c1 c2)  : cayley (c1 ⊕ c2) = cayley c1 ∘ cayley c2
theorem epsAtOrigin_cayley c : epsAtOrigin (cayley c) = c

-- D. Cell256 enumeration
theorem Cell256.all_length  : Cell256.all.length = 256
theorem Cell256.all_nodup   : Cell256.all.Nodup
theorem Cell256.mem_all     : ∀ c, c ∈ Cell256.all
theorem xuGua_length        : xuGua.length = 64

-- E. Self-description completeness (Truth/SelfDescription.lean)
theorem cell256_operator_complete : ∀ a b : Cell256, ∃ f, f a = b
theorem root_operator_summary                                         -- root-native operator + legacy quarantine boundary
theorem self_description_summary                                      -- complete self-description + position semantics + claim-boundary current

-- F. Turing-completeness
theorem loopProg_unbounded : ∀ n, ¬ (...runFuel n...).halted = true   (Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean)

-- G. Gödel-Li
theorem halts_undecidable_internally :
    ¬ ∃ (decide : List YiInstr → Hexagram → Bool),
        ∀ P h, decide P h = true ↔ Halts P h                          (Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean)

-- H. cuo-equivariance ceiling (v3 statement; affected by PR #37 universal-ISA upgrade — see ledger)
theorem sheng_not_cuo_equivariant : ¬ ∃ p, runHex p init = sheng       (Foundation/Wen/WenDefCompile.lean)
theorem unrestricted_kleene_inverter_inconsistent                       (Foundation/Atlas/Yi/Classical/Algebra/CuoInvariance.lean)
                                                                       -- internalises the v2 kleene_recursion_axiom

-- I. self-host (Tier 2 quine PoC)
theorem «微核自验»            (formerly WenyanSelfHost.lean; module retired post-v3; theorem content reorganised — see ledger)
theorem «微核自释_total»

-- I2. Tier 3 partial — uniform N-cell quine + framed round-trip
theorem Quine.quine_history (N) : ...history of [push]^N at fuel N        (WenyanSelfInterp.lean)
theorem ProgEnc.framed_round_trip_witness :
    decFramedProg ∘ encFramedProg = some

-- J. dao source (5-fold self-reference)
theorem «道之自指» :
    («判型良» «道程» = true) ∧
    («解程» «道源» = some «道程») ∧
    («印程» «道程» = «道源») ∧
    (∀ h, ((YiState.init h «道程»).runFuel 64).halted = true) ∧
    (∀ h, ((YiState.init h «道程»).runFuel 64).cur.2 = .ji ↔ h.y3 = h.y4)
                                                                       (Foundation/Atlas/Yi/DaoSource.lean)

-- K. alignment
theorem process_alignment_dao_shengshengbuxi_summary
    : (ProcessAligned + Open → Dao) ∧ (Dao → ShengshengBuxi) ∧
      (ShengshengBuxi → Dao)                                                   (Alignment T2)
theorem denier_breaks_shengshengbuxi
    : Denier.policy 之 step 破 ShengshengBuxi                                  (Alignment T3)

-- L. sincerity (anti-conjecture)
theorem sincerity_main_theorem : T1 ∧ T2 ∧ T3 ∧ T4 ∧ T5 ∧ T6 ∧ T7 ∧ T8        (Sincerity.lean)

-- M. human community
theorem «人类命运共同体_之证» :
    (∃ g, TrueDao communityModel communityDao communityPath g) ∧
    (∃ g, ¬ TrueDao ...) ∧
    (∀ g, TrueDao ... ↔ g = aligned) ∧
    ((entryOf (R .«道»)).deps = [G .«正续», R .«共开», G .«夺共续», R .«坏»])
                                                                       (Renlei.lean)

-- N. dao-li bifurcation
theorem dao_proves_about_li : ¬ ∃ decide, ∀ P h, decide P h = true ↔ Halts P h
theorem li_cannot_encode_dao : ∀ N, ∃ n > N, Nonempty (Sheng n)        (DaoLi.lean)

-- O. R8_complete bundle (was R6_complete in v2)
theorem R8_complete : {Cell256 cardinality + group laws + Cayley + V₄ outer + 印/投 + xuGua}      (Foundation/Atlas/Yi/Classical/Cells/R8Stratify.lean; formerly Cell256Stratify.lean)
```

---

## 7 · Build Invariants (v3 snapshot 2026-05-11; current numerics in ledger)

```
∀ commit ∈ main (v3 snapshot):
  lake build                  ⇒  smoke target exit 0
  lake build SSBX             ⇒  full library exit 0  (3686 jobs; current scale larger)
  count(sorry, migrated+Squaring) = 0       (v3 snapshot only; current ~150 documenting research debt, see ledger)
  count(axiom, migrated+Squaring) = 0       (v3 snapshot only; current ≥ 1 in Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean)
  count(opaque, formal/)      =  1          (theOne; carries Field/dong/origin/alive)
  count(partial def, formal/) =  1          (BaguaTuring.run)
```

> **Current formal status**: see [docs-next/10_formal_形式/claim-status-ledger.md](./docs-next/10_formal_形式/claim-status-ledger.md) v0.8 (2026-05-21).

### 7.1 Continuous regression check

```bash
$ lake build SSBX                                            # full library
$ lake build +SSBX.Foundation.Atlas.Yi.Cell256               # single module (was Foundation.Bagua.Cell256 in v3)
$ lake build +SSBX.Foundation.Hierarchy.RHierarchy
$ lake build +SSBX.Foundation.Atlas.Yi.DaoSource             # (was Foundation.Wen.DaoSource; DaoSource now under Atlas/Yi/)
$ scripts/generate_monad_dag.py                              # regen «一»-DAG
$ scripts/render_monad_dag.sh                                # render to SVG
```

### 7.2 New module checklist

```
☐ axiom count not silently increased (within ledger-recorded allowance)
☐ opaque count unchanged (= 1)
☐ no new sorries introduced; any `sorry` retained must document research debt
☐ all theorems machine-witnessed (native_decide / by exact / by rfl / by induction)
☐ added to formal/SSBX.lean import index
☐ if Roster-touching: regen MonadDAG.mmd, MonadTree.txt, ConceptDAG*.{mmd,svg}
☐ if Cell-carrier-touching: confirm Cell256 (not Cell192); update OperatorCellMap if needed
☐ if a new Hierarchy/R*.lean: import it from Hierarchy/RHierarchy.lean
☐ Foundation/Bagua/* and Foundation/Yi/* are retired — point at Foundation/Atlas/Yi/* instead
```

---

## 8 · Cross-Reference Index

```
Doctrine layer → Lean module          Foundation/Wen/Kernel.lean § Layer N
Lean module → doctrine layer          Wen/Kernel.lean inverse (in-source comments)
AtomName → registry entry             Roster.lean § entryOf
GenName → roots + deps                Roster.lean § rootsOfGenerated, depsOfGenerated
RecName → recursive semantics         Roster.lean § recDeps, recSemOf
PrimName / PendingName                Roster.lean § allPrimitives, allPending

R-layer alias                         Foundation/Hierarchy/R{0..8}_*.lean
R-layer cross-cut: Lift / Project     Foundation/Hierarchy/LiftProject.lean
R-layer atomic ops (XOR subgroup)     Foundation/Hierarchy/Operators/Atomic.lean
R-layer V₄ outer                      Foundation/Hierarchy/Operators/V4.lean
8-char string literal → Cell256       Foundation/Notation/OXNotation.lean

Surface wenyan → 12-instr ISA          Foundation/Wen/WenyanParser.lean § parseInstr
ISA → wenyan                          same § printInstr
Tm → ISA (cuo-equivariant subset)     Foundation/Wen/WenDefCompile.lean
ISA → YiState transition              Foundation/Atlas/Yi/Classical/Computation/BaguaTuring.lean § execute / step / runFuel
Cell256 ↔ List Cell256 (encoding)     Foundation/Wen/WenyanSelfInterp.lean § ProgEnc (R8-native; Phase F.1 migration complete)

V₄ Shi ↔ (因, 果) ∈ Bool²              Foundation/Atlas/Yi/Cell256.lean § Shi.toYinGuo / ofYinGuo
Cell256 algebraic spine               Foundation/Atlas/Yi/Cell256.lean § 7
印 / 投 mask                            Foundation/Atlas/Yi/Cell256.lean § 8
xuGua (King Wen) order                Foundation/Atlas/Yi/Cell256.lean § 4
```

---

## 9 · v3 doctrine-source citations

The v3 algebraic spine documented above corresponds 1-to-1 with the doctrinal text:

| Doctrine doc | Lean correspondence |
|---|---|
| [`docs-next/10_formal_形式/yi-RO-hierarchy.md`](./docs-next/10_formal_形式/yi-RO-hierarchy.md) (v3 historical doctrine) | this document § 2 + § 5.2 + § 5.3 |
| [`docs-next/10_formal_形式/claim-status-ledger.md`](./docs-next/10_formal_形式/claim-status-ledger.md) v0.8 (canonical current status) | repository-wide axiom / sorry / proof-strength accounting |
| `docs-next/10_formal_形式/cell256-algebra.md` | `Foundation/Atlas/Yi/Cell256.lean § 7` (Phase A algebraic spine) |
| `docs-next/10_formal_形式/cell256-grid.md` | `Foundation/Atlas/Yi/Cell256.lean § 1`-`§ 5` (Shi V₄ + Cell256 enumeration + xuGua order) |
| `docs-next/10_formal_形式/v4-shi.md` | `Foundation/Atlas/Yi/Cell256.lean § 1` + `Foundation/Hierarchy/Operators/V4.lean` |
| `docs-next/10_formal_形式/heisenberg-weyl-narrative.md` (in draft) | `Foundation/Wen/Embeddings/{HeisenbergWeylZModP, HeisenbergWeylOperators, StabilizerQM, HilbertPauliFunctor, PauliRingIso, PhasedPauli}.lean` |
| `docs-next/10_formal_形式/lift-project.md` (forthcoming) | `Foundation/Hierarchy/LiftProject.lean` |
| `docs-next/10_formal_形式/operator-split.md` (forthcoming) | `Foundation/Hierarchy/Operators/Atomic.lean` + `V4.lean` |
| [`六表_实虚史真/表六_256格全表.md`](./六表_实虚史真/表六_256格全表.md) | `Foundation/Atlas/Yi/Cell256.lean` + `Foundation/Notation/OXNotation.lean` |

---

## 10 · Two Conjectures (out-of-scope, marked)

Documented in prose at `README.md § 9.2 / 9.3` and `README.en.md § 9.2 / 9.3`.

```
ConjOne   Dao-attainability via reading-and-recitation
          not formally claimed; compatible with proven kernel

ConjTwo   大同 (Great Concord) as historical residue
          not formally claimed; tongGen-favouring environment
          consistent with EconGame.lean § coase_internalizes_externality
```

Scope sieve:

| Status | Included | Excluded |
|---|---|---|
| machine-proven | closed Lean declarations accepted by the build, under the trust base in §1 and the executable boundary above | prose extrapolations; ledger sync claims; the six pending interfaces |
| ledger-dependent | generated DAG / roster summaries, operator counts, layer-to-essay mappings, module counts, cross-volume correspondences | not single closed theorems unless separately named by a Lean declaration |
| pending | §§ 3.4 six `PendingName` interfaces awaiting empirical calibration | not used as established truth |
| conjecture | ConjOne / ConjTwo and the historical or practice claims in prose | no Lean term inhabits these |

The reality-scope claim in `README.md § 9.1` / `README.en.md § 9.1` is a defended philosophical extrapolation from machine-proven invariants plus ledger-dependent correspondences. It is not a theorem named by this formal specification.

---

## 11 · Ledger (v3 snapshot 2026-05-11; current state in claim-status-ledger)

```
Foundation Lean LOC       ~45000+ (v3 snapshot; current larger) across 100+ Foundation modules
Foundation/Core modules   14    (incl. Alignment, Sincerity, HumanAlignment, EvolutionDao, Renlei)
Foundation/Wen modules    38+   (incl. WenSurface, DaoSource [now under Atlas/Yi/], AntiSchmitt,
                                 AlignmentFailures, EconGame, MetaInterp/* now ~40 modules,
                                 Embeddings/* 7 modules for Heisenberg-Weyl G11)
Foundation/Atlas/Yi       (replaces v3 Foundation/Bagua + Foundation/Yi)
                          Cell128/Cell256 + Hexagrams/BenZheng/DaoSource + Classical/{Core, Algebra,
                          Computation, Diagonal, Cells}/* (incl. Yi, YiCore, BaguaAlgebra, BenZheng,
                          BaguaTuring, BaguaWenSpec, GodelLi, KleeneInternal, Newman, CuoInvariance,
                          FuelDiscipline, ChunkedDecide, R7, R8, R8Stratify)
Foundation/Hierarchy      11    (RHierarchy umbrella + R0_Taiji..R8_GuoHex shims + LiftProject + Operators/{Atomic, V4})
Foundation/Notation        1    (OXNotation)
Foundation/Squaring        5    (V4Tensor, L1, RetractTower, StreamCarrier, ProfiniteLimit)
Foundation/Jian            6    (JianOntology, Jian, JianSTLC, JianMinimality, JianModeKernel, JianYiBridge)
Foundation/Eight           8    (ShuSuan, LuoJi, TongJi, XingWei, LeiYing, DongLi, XinZhi, WuXiang)
Foundation/Modern modules 19+   (Mathlib bridge core) + 60+ QuantumRelativity*Bridge
Foundation/{Order, Doctrine, Enriched, R, ...}  post-v3 research clusters (GUT / SMCC instances /
                          Lawvere theory / Claim Z). Most current sorries / axioms live here.
Path-丙 modules           11    (M1 → M4-甲)
MetaInterp                v3: 16; current: ~40 modules (Phase 2.3 series, see §5.6)
Kernel layers             45+   (元 → 非道之形式 + Layer 46 doctrinal refinements)
义理 essays               90+   (义理/A_..Z_*.md, Eight-Expansions, 60+ Markov-bridge essays, 共同体)
六表 tables               6     (六表_实虚史真/, including v3 表六_256格全表.md)
wenyan operators          legacy inventory (`Text/WenyanOperators.lean`; not root ontology)
operator × cell pairs     legacy audit inventory (`Text/OperatorCellMap.lean`; not root ontology)
```

```
trust:    Lean kernel (v4.30.0-rc2) + Mathlib HEAD
machine:  v3 snapshot — 3686 build jobs · 0 sorry · 0 project-custom axioms in migrated+Squaring
          current — see claim-status-ledger.md v0.8 (sorry ~150 documenting research debt;
                    axiom ≥ 1 in Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean)
opaque:   1 (theOne)
partial:  1 top-level executable partial def (BaguaTuring.run nontermination boundary)
ledger:   DAG / roster / operator / layer / essay correspondences are sync claims
pending:  6 PendingName interfaces; WenyanSelfInterp universal buildEmitProg + diagonal (roadmap, not yet written)
open:     universal composition closure ("all compositions = R-tower ops") — no universal theorem;
          only subclasses (R₄ bilinear forms, etc.) proven. universal_sayability proven on Core that
          factors out 3 generators (square_mor / relate_mor / modal_V4_mor) with no canonical SMCC
          definition. enriched_universal_sayability_statement now a scoped bridge — full V-natural
          Power-1999 §4.5 still open. Heisenberg-Weyl G11 closed at the abstract level
          but not yet bridged to Cell256 / R₈ / 易卦.
conj:     ConjOne / ConjTwo, no Lean term claimed
boundary: cuo-equivariance ceiling (v3 statement; PR #37 universal-ISA upgrade affects scope),
          universal-compileTm undefinable
          (halts_cuo_invariant + unrestricted_kleene_inverter_inconsistent),
          halting-undecidability, dao-li bifurcation
```

— *EOF · this is a specification, not an introduction. For prose, see `README.md` (中文) or `README.en.md` (English).*
