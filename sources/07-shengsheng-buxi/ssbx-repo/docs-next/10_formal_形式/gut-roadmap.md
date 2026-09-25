# GUT Implementation Roadmap

> 从「R-family 满足 universal substrate 的 P1-P7」走到「R-family **就是** universal substrate of all sayable systems」(GUT claim) 的实施路径。
>
> v0.2 · 2026-05-16 · 起草 + minimum-viable GUT-A claim achieved one session later
>
> **Status snapshot (2026-05-21)**: Scoped GUT-A is closed at the F₂/GUT-A boundary. The public R-layer aggregate is `scoped_gut_a_closed`, which packages `scoped_phase_zero_closed`, `scoped_phase_one_closed`, `T5_A_aggregator`, `T5_A_full_side_obligations`, and the concrete F₂ D5/D6 package. `FullGUTFrontier.current_full_gut_frontier` now bundles the theorem-grade scoped frontier through Tier 1/2/3 plus the scoped G11 cut-1 field package and the finite-coordinate Hilbert tensor/unit, tensor/unit reindexing isometry, tensor coherence, dagger/tensor, Kronecker morphism, algebraic tensor-product comparison, and isometric tensor-product comparison boundaries. This is not absolute FullGUT, automatic semantic-witness construction, raw-core all-split coherent T5, raw non-canonical finite-field satisfier synthesis, or global D6 exhaustiveness; coherent T5 for split-coherent satisfiers, split-coordinate finite-field cores, and canonical finite fields is closed in the separate GUT-B/G11 frontier.
>
> **Status authority**: For row-by-row reading rules and the "scoped vs absolute" wording policy, see [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 (2026-05-21). For the Heisenberg-Weyl G11 odd-prime narrative referenced in G11 below, see [`heisenberg-weyl-narrative.md`](heisenberg-weyl-narrative.md).

## 一、Context（当前状态）

我们已经有：

- **数学根**：R-family δ-polymorphic carrier（`Foundation/R/Basic.lean`），4-level abstraction tower（distinction → operation → algebraic → canonical F₂）全部 Lean 实现
- **Phase 0 sub-theorems**：T_P3 / T_P6 / T_P7a / T_P7b 在 scoped F₂/GUT-A boundary 已闭合；public anchor 是 `Foundation/R/PhaseZero/Closure.lean` 的 `scoped_phase_zero_closed`，并汇总 `T_P3_arf_surjective`, `T_P3_sigma_uniqueness_R2`, `T_P6_minimality_packaged`, `T_P6_lorentzian_bridge`, `T_P7b_full`, `T_P7b_form_b_packaged`, and `R4_structurally_minimal_full`
- **Strategy A** (T4 step 3 partial)：classical-Boolean 范围内「why F₂?」已闭合（`StrategyA.lean`）
- **Conditional UG**：X²-256 lattice 在 6 个 Lean 文件中 0-sorry（`Wen/X2Codes.lean` + 5 配套）
- **One-core 桥接**：V4 ≃ R 2, Mode16 ≃ R 4, Word64 ≃ R 6, RootCell256 ≃ R 8 explicit equivalences
- **Falsification 结构**：D1 / P-closure / D5 / D6 在 `ClaimZ.lean` 中是 Lean structures
- **125,559 LOC** 的应用层（Wen.Core / Atlas / Modern / Lang / Text）

我们目前**能合法 claim** 的：

- R-family satisfies P1-P7（formal）
- **Scoped GUT-A closed**: F₂/GUT-A boundary has both analytic and synthetic sides packaged by `scoped_gut_a_closed`
- F₂-Boolean classical articulation lands in R-family-over-F₂ within the scoped theorem stack
- Conditional UG: if UG exists in some structural sense, it is ≅ X²-256 lattice
- 4-level abstraction tower 是 Lean-verified 现实

我们**还不能 strict claim** 的：

- unrestricted Claim Z / T0 / absolute FullGUT
- automatic semantic preservation witnesses for all admissible formal systems
- raw-core all-split coherent T5 without supplied split-coordinate/coherence data
- global D6 exhaustiveness

## 二、Goal（精确的 GUT claim 形式）

实施完所有任务后，可 claim 的**最强陈述**：

> **Theorem (Universal Sayability)**. Any formal articulation S of sayable / abstractable content satisfies P1-P7 ⟹ S ≃ R-family-over-δ for an appropriate realisation δ of the primitive binary distinction, where ≃ is structure-preserving equivalence (categorical / Morita / bi-interpretable, depending on framework).

这个 theorem 等价于 Claim Z 的两个方向都形式化：
- **Analytic**: D1 ⟹ P1-P7（任何 D1-articulation 满足 P-properties）
- **Synthetic**: P1-P7 ⟹ R-family-over-δ（任何 P1-P7 satisfier 等价于 R-family）

**最小可 publishable 版本**（minimum defensible GUT claim）：上面的 theorem 限定到 **F₂-Boolean classical scope** + **至少一个 non-algebraic δ instance 作为 sibling witness**。

## 三、Gap Inventory（按 claim 影响排序）

### Tier 1 — 真正的形式 gap（不补 claim 站不住）

| ID | Item | Status | 估算 |
|---|---|---|---|
| **G1** | D1 ⟹ P1-P7 完整证明（analytic direction） | ✅ closed at F₂-Boolean scope via `R/ClaimZ/Analytic.lean` and public aggregate `R/ClaimZ/Analytic/Closure.lean`; polymorphic/non-F₂ analytic extension remains open | scoped closed |
| **G2** | T5-A: P1-P7 ⟹ R-family-over-F₂ uniqueness（synthetic, F₂ scope） | ✅ closed in tractable layerwise/ring-anchor form via `R/UniquenessF2.lean` and `R/T5AClosure.lean`; arbitrary-satisfier coherent strengthening remains open | scoped closed |
| **G3** | T2 universality case study（至少 1-2 个外部 system 形式化嵌入） | ✅ closed at scoped case-study boundary via `FullGUTTier1Frontier.current_tier1_G3_case_studies`: propositional/FOL syntax round-trip, stabilizer/Pauli R-family embedding, and small-category/Lawvere D1 entry points | scoped closed |
| **G4** | 至少一个 non-algebraic δ-realisation 完整实例化（Prop / Quantum / Semantic） | ✅ closed at scoped sibling-witness boundary via `R/Distinction/Prop.lean` and `FullGUTTier1Frontier.current_tier1_G4_non_algebraic` | scoped closed |

### Tier 2 — 二阶 gap（claim 站住但说服力 up 一档）

| ID | Item | Status | 估算 |
|---|---|---|---|
| **G5** | D6 falsification 实跑（即使失败也行） | ✅ closed for the current scoped D5/F₂-D6 pair via `FullGUTTier2Frontier.current_tier2_G5_D6_audit`; global D6 exhaustiveness remains open | scoped closed |
| **G6.1** | T_P3 scoped uniqueness anchors（Arf surjectivity + `R 2` σ uniqueness） | ✅ closed | `PhaseZero.lean`, `PhaseZero/Closure.lean` |
| **G6.2** | T_P6 minimality + Lorentzian-4-region 连接 | ✅ closed | `TP6Minimality.lean`, `TP6Lorentzian.lean`, `PhaseZero/Closure.lean` |
| **G6.3** | T_P7b Wedderburn/R4 scoped uniqueness + Mathlib bridge | ✅ closed | `TP7bUniqueness.lean`, `TP7bFormB.lean`, `R4Minimality.lean`, `PhaseZero/Closure.lean` |
| **G7** | 跨 base functor library（mod-phase Hilbert→Pauli, representation 反向） | ✅ closed for the F₂/stabilizer-Hilbert branch via `FullGUTTier2Frontier.current_tier2_G7_cross_base_stabilizer_hilbert`; native finite-Hilbert dagger plus coordinate tensor/unit, Kronecker morphism, algebraic tensor-product comparison, and isometric tensor-product comparison boundaries are exposed by the native frontier; odd-prime Heisenberg-Weyl phase-space/R-coordinate and supplied-character operator boundaries have moved into G11, where the scoped concrete finite-Hilbert operator, object-action, and dagger boundaries are closed; full `FdHilb` categorical semantics remains G11/GUT-C work | scoped closed |

### Tier 3 — 三阶 gap（不影响 mathematical claim，但影响 scientific 接受度）

| ID | Item | Status | 估算 |
|---|---|---|---|
| **G8** | 可证伪的经验预测被独立检验 | ✅ protocol/readiness closed via `FullGUTTier3Frontier.current_tier3_G8_empirical_readiness`; external experiments remain outside Lean | scoped readiness closed |
| **G9** | Peer engagement / 外部 critique | ✅ adversarial-review protocol closed via `FullGUTTier3Frontier.current_tier3_G9_peer_engagement_readiness`; external review/endorsement remains outside Lean | scoped readiness closed |
| **G10** | Inductive V4 → abbrev R 2 完成（~90 proof-level cases 重写） | ✅ migration boundary closed via `FullGUTTier3Frontier.current_tier3_G10_v4_migration_boundary`; repository-wide mechanical rewrite remains optional polish | scoped boundary closed |

### Out-of-scope（GUT-A 之后再考虑）

| ID | Item | 说明 |
|---|---|---|
| **G11** | T5-B parametric over k (algebraic class) | ✅ scoped cut-1 closed for canonical finite fields, prime fields, structure-gated arbitrary field satisfiers, odd-prime discriminant classification, odd-prime Heisenberg-Weyl phase-space/R-coordinate symplectic boundary, primitive complex additive phase, one-site clock/shift commutation, multi-site zero phase-point matrix identity, multi-site projective multiplication, symplectic commutator phase, left/right unitarity, phase-point matrix faithfulness, pure-shift coordinate reachability, pure-clock coordinate projectors, coordinate matrix-unit Fourier sums, phase-point matrix span/top, invariant-subspace irreducibility, the scoped concrete finite-Hilbert operator boundary, the scoped concrete finite-Hilbert object action boundary, the scoped finite-Hilbert dagger boundary, and finite-coordinate algebraic/isometric tensor-product comparison/naturality. See [`heisenberg-weyl-narrative.md`](heisenberg-weyl-narrative.md) for the consolidated odd-prime narrative; the package lives in `Foundation/Wen/Embeddings/{HeisenbergWeylZModP, HeisenbergWeylOperators, StabilizerQM, HilbertPauliFunctor, PauliRingIso, PhasedPauli}.lean` plus `Doctrine/Instance/HilbertEnriched.lean`. Arbitrary raw non-canonical finite-field satisfier synthesis, full `FdHilb` categorical semantics, and an explicit bridge from the odd-prime Heisenberg-Weyl package to the `Cell256 = R 8 (over Bool)` carrier remain open |
| **G12** | T5-C full δ-realisation (incl. non-algebraic) | research-level；可能需新 categorical framework — 12+ 月 |
| **G13** | Per-base bridges for ℝ / ℂ / ℂ_p R-family instances | Mathlib classical foundations 桥接 — 数月每个 |

## 四、Dependency Graph

```
                              [G6.1 T_P3 uniq]──┐
                              [G6.2 T_P6 Lor]───┤
                              [G6.3 T_P7b Wed]──┴──► [G2 T5-A] ◄──┐
                                                          ▲       │
                                                          │       │
       ┌──[G1.P1 (Strategy A done)]─────────────────────────┐     │
       ├──[G1.P2 composition]────────────────────────────────┤     │
       ├──[G1.P3 relations]──────────────────────────────────┤     │
       ├──[G1.P4 scale]──────────────────────────────────────┤     │
       ├──[G1.P5 self-ref]───────────────────────────────────┤     │
       ├──[G1.P6 modality (conditional D1' item 8)]──────────┤     │
       ├──[G1.P7a aspect alphabet]───────────────────────────┤     │
       └──[G1.P7b atomic ops]────────────────────────────────┘     │
                                                                   │
       [G3.C4 propositional/FOL syntax] ──────────────────────────┤
       [G3.C3 stabilizer-QM] ─────────────────────────────────────┤
       [G3 category/Lawvere D1 entry] ────────────────────────────┤
                                                                   │
       [G4 non-algebraic δ instance (e.g. Prop)]─────────────────┐ │
                                                                 │ │
       [G7 cross-base functor library] ←── (needs G4) ───────────┘ │
                                                                   │
       [G5 D6 falsification test] ──── (ongoing, ne dep) ──────────┤
                                                                   │
       [G8 empirical predictions] ──── (no formal dep) ────────────┤
       [G9 peer engagement] ───────── (no formal dep) ─────────────┤
       [G10 V4 inductive elim] ───── (orthogonal polish) ──────────┤
                                                                   │
                                                                   ▼
                                                       ┌───────────────────┐
                                                       │  GUT-A claim 可发 │
                                                       │  (Minimum viable) │
                                                       └───────────────────┘
                                                                  │
                                                                  ▼
                                          [G11 T5-B] ──► [G13 per-base bridges]
                                                                  │
                                                                  ▼
                                          [G12 T5-C distinction-monism scope]
                                                                  │
                                                                  ▼
                                                       ┌───────────────────┐
                                                       │  Full GUT claim   │
                                                       │  (strongest form) │
                                                       └───────────────────┘
```

### 依赖关系总结

- **G6.{1,2,3}** 是 T5-A 的前置（uniqueness clauses 给 T5-A 提供 Wedderburn 和 BA 唯一性）
- **G1** (D1 ⟹ P 分析方向) 与 **G2** (T5-A 综合方向) **互相独立**，可平行
- **G3** case studies 与 G1/G2 独立，当前 scoped case-study boundary 已由 `current_tier1_G3_case_studies` 打包
- **G4** non-algebraic δ instance 已由 δ=Prop sibling witness 关闭；它仍是 G7 (cross-base functor library) 的前置
- **G5** D6 testing、**G8** 经验预测、**G9** peer engagement、**G10** V4 polish 完全独立，可任何时候做
- **G11/G12/G13** 都在 G2 (T5-A) 之后

## 五、Phased Plan（6-12 个月到 minimum viable GUT claim）

总体思路：先做能并行的、依赖少的工作；T5-A 是 critical path 的核心节点。

### Phase 0 — Closed scoped F₂/GUT-A closure

**Status**：closed for the scoped F₂/GUT-A path. G6.1 / G6.2 / G6.3 are no longer blockers for `T5_A`.

Closed anchors:

- **Stream P0-A / G6.1**：`T_P3`, `T_P3_arf_surjective`, `T_P3_sigma_uniqueness_R2`.
- **Stream P0-B / G6.2**：`T_P6`, `T_P6_card_ge_four`, `T_P6_minimality_packaged`, `T_P6_lorentzian_bridge`.
- **Stream P0-C / G6.3**：`T_P7b_ring_equiv`, `T_P7b_full`, `T_P7b_form_b_packaged`, `R4_structurally_minimal_full`.

**Public theorem**：[`Foundation/R/PhaseZero/Closure.lean`](../../formal/SSBX/Foundation/R/PhaseZero/Closure.lean) exposes `scoped_phase_zero_closed`.

**Boundary**：full all-dimensional characteristic-2 Witt-Arf orbit classification, arbitrary simple finite F₂-algebra uniqueness, arbitrary finite-field satisfier coherence, and semantic GUT-C upgrades are no longer Phase 0 blockers; they are separate later obligations.

### Phase 1 — D1 ⟹ P_i 分析方向（closed at F₂-Boolean scope）

**目标**：完成 G1 — analytic step D1 ⟹ P1-P7 的逐项证明。

**Status**：F₂-Boolean / GUT-A scope 已闭合。`ClaimZ.lean` 保留 interface-level
combinator `d1_implies_P`；`R/ClaimZ/Analytic.lean` 给出具体 `Phase1Closure_F2`,
`D1_implies_Phase1Closure_F2`, `D1_implies_PClosure_at_F2`, and
`D1_restricted_implies_Phase1Closure_F2`；`R/ClaimZ/Analytic/Closure.lean`
提供 public anchor `scoped_phase_one_closed`。剩余工作是 polymorphic/non-F₂
analytic extension，不是 GUT-A Phase 1 blocker。

**8 sub-streams**（每个 P_i 一个，均已在 F₂ scope 闭合）：

- **Stream A1**：P1 — `R/ClaimZ/Analytic/P1.lean`
- **Stream A2**：P2 — `R/ClaimZ/Analytic/P2.lean`
- **Stream A3**：P3 — `R/ClaimZ/Analytic/P3.lean`
- **Stream A4**：P4 — `R/ClaimZ/Analytic/P4.lean`
- **Stream A5**：P5 — `R/ClaimZ/Analytic/P5.lean`
- **Stream A6**：P6 — `R/ClaimZ/Analytic/P6.lean`
- **Stream A7**：P7a — `R/ClaimZ/Analytic/P7a.lean`
- **Stream A8**：P7b — `R/ClaimZ/Analytic/P7b.lean`

**输出**：`Foundation/R/ClaimZ.lean` 不改成 F₂-only theorem；它继续承载 reusable
interface。完整 F₂ theorem 位于 `Foundation/R/ClaimZ/Analytic.lean`，public
aggregate 位于 `Foundation/R/ClaimZ/Analytic/Closure.lean`。

**测试**：`scoped_phase_one_closed` bundles the full, existential, and restricted
Phase 1 forms with 0 sorry / 0 axiom.

### Phase 2 — T5-A: P1-P7 ⟹ R-family-over-F₂（closed at scoped F₂ boundary）

**Status**：closed at scoped F₂/GUT-A boundary. Core anchors:
`T5_A`, `T5_A_ringEquiv_at_4`, `T5_A_squaring_compatible`,
`T5_A_bilinear_natural`, `T5_A_hom_natural`, `T5_A_aggregator`, and
`T5_A_full_side_obligations`. Public aggregate: `scoped_gut_a_closed`.

**目标**：在 F₂-Boolean classical scope 内证明 uniqueness — 任何满足 P1-P7 的结构都 ≃ R-family-over-F₂（in F₂-algebra category）。

**证明骨架**（5 steps）：

1. P1+P2 + Boolean ring 公理 ⟹ 结构 S 同构于某个 Boolean algebra
2. Stone duality / Birkhoff representation ⟹ finite BA ≃ F₂^N
3. P3-P5 + Wedderburn uniqueness（来自 G6.3）⟹ 结构 ring 部分由 R₄ ≅ M₂(F₂) pinned
4. P4 squaring tower 唯一性（来自 G6.{1,2,3}） ⟹ 整个 R_N 塔由 R₁ + squaring 唯一确定
5. 12-item D2 aggregator 闭合 ⟹ S 的全部结构 ≃ R-family-over-F₂

**文件**：`Foundation/R/UniquenessF2.lean`, `Foundation/R/T5AClosure.lean`,
`Foundation/R/GUTAClosure.lean`.

**风险**：可能发现 P1-P7 当前形式化不够紧 — 即有结构满足现行 PClosure 但不 ≃ R-family。处理：
- 选项 a：**强化 P1-P7**（补充约束）；这是标准 foundational revision
- 选项 b：**弱化 T5-A 陈述**（≃ Morita / bi-interp 替代 strict iso）
- 选项 c：**改 PClosure 的形式化**

**测试**：`scoped_gut_a_closed : Nonempty ScopedGUTAClosure` is the current
R-layer citation point. It packages transported atomic action semantics; equality
with an independently supplied native/intended action remains an explicit extra
interface.

### Phase 3 — T2 case studies（1-2 月每个，可并行）

**目标**：至少形式化 1-2 个外部 system 嵌入 R-family，作为 universality demonstration。

**并行可选 sub-streams**（选 1-2 个）：

- **Stream C1**：ZFC fragment 嵌入。Hereditarily-finite sets ↪ R-family（finite-set 部分）。难度：中等；Mathlib 有 set theory 工具。
- **Stream C2**：MLTT fragment 嵌入。Inductive types ↪ R-family（W-types + finite-cases）。难度：高；HoTT 桥接是 open 问题。
- **Stream C3**：Stabilizer-QM 嵌入。Pauli group / 𝒫_n / ⟨iI⟩ ≅ R_{2n}^{(F₂)}。难度：中等；已部分写在 Hierarchy/Operators/V4 + R/Bilinear。
- **Stream C4**：First-order logic with finite signatures ↪ R-family（语法树编码）。难度：低；标准 Gödel coding。

**建议选 C3 + C4** 作为最小集 — C3 给 quantum-side witness，C4 给 logic-side witness，工作量合理。

**输出**：`Foundation/Wen/Embeddings/StabilizerQM.lean` + `Foundation/Wen/Embeddings/FOL.lean`（或类似命名）。

### Phase 4 — Non-algebraic δ instance + D6 testing（并行，2-4 周）

**并行 2 streams**：

- **Stream NA-1**：G4 — δ=Prop instance file `Foundation/R/Distinction/Prop.lean`，给 propositional / proof-relevance 一个 P1-P7 instance（即使 P3 形态不同，必须显式说明）
- **Stream NA-2**：G5 — D6 falsification test。挑 2-3 个 candidate counterexamples（HoTT / ETCS / Synthetic Differential Geometry），尝试在 Lean 中 instantiate `D6_ClaimZFalsified`。即使失败也获得 evidence 表 — 该 claim 经得起对手攻击。

**输出**：
- `Foundation/R/Distinction/Prop.lean`（至少 carrier-level instantiation）
- `Foundation/R/D6_Tests.lean`（记录 attempted falsifications + 为什么失败）

### Phase 5 — Empirical prediction + peer engagement（持续，并行）

**Stream E-1**：G8 经验预测 — 选 1 个具体可测 prediction（如「R-family 5 preservation invariants 在 frontier LLM 的 attention pattern 中可观察」），写 prediction protocol + 找 collaborator。

**Stream E-2**：G9 peer engagement — 把 wen-substrate/ folder 发出去给 Awodey / Shulman (HoTT) / Lawvere lineage / Spencer-Brown 后继 (Kauffman, Varela)，吸收 critique，更新 D6 test set。

**不在 critical path** — 在 Phase 2 (T5-A) 通过后做最高效（claim 已 publishable 形态）。

### Phase 6 — Inductive V4 elim 收尾（2-3 月，可推迟）

**目标**：G10 — 把 90+ 处 proof-level `cases g <;> rfl` 重写为 `funext + fin_cases`，然后 `inductive V4` → `abbrev V4 := R 2`。结构整洁的最后一步。

**不影响 GUT claim**，但完成后**Lean 类型层面也只有 R-family 一个核**（当前是「数学层面一个核 + V4 作为 ergonomic surface」）。

---

## 六、Critical Path Analysis

**Critical path**（必须 sequential 的链）：

```
G6.{1,2,3}  ──►  G2 T5-A  ──►  GUT-A claim publishable
(Phase 0)        (Phase 2)
```

**Min duration on critical path**：historical estimate superseded for the scoped
F₂ branch. Phase 0, Phase 1, and the tractable T5-A branch are now closed at
the GUT-A boundary; remaining estimates apply to polymorphic/non-F₂ analytic
extension, arbitrary-satisfier coherence, and absolute semantic automation.

**Parallel side branches**（不在 critical path，但 GUT-A claim 需要）：

```
G1 D1 ⟹ P 8 sub-streams   →  Phase 1 F₂ scope ✅ → 满足 scoped Tier 1 G1
G3 case studies            →  `current_tier1_G3_case_studies` ✅ → 满足 scoped Tier 1 G3
G4 + G5                    →  G4 δ=Prop ✅ / G5 global D6 open → 满足 scoped Tier 1 G4
```

**Parallelized total**：historical estimate superseded for Scoped GUT-A. Future
estimates now apply to non-F₂/polymorphic analytic extension, arbitrary-satisfier
coherent T5, automatic semantic witnesses, and GUT-C.

**Optimistic**：3 个月（如 Phase 0 工程平稳、T5-A 未撞 P1-P7 强化需求、并行 streams 顺畅）
**Realistic**：6 个月
**Pessimistic**：9-12 个月（如 T5-A 撞 P1-P7 revision 需求，需迭代）

## 七、Risk Mitigation

| 风险 | 概率 | 影响 | 应对 |
|---|---|---|---|
| **T5-A 撞 P1-P7 不够紧** — 发现存在满足 PClosure 但不 ≃ R-family 的结构 | **中等** | **大**（需 revise P-properties） | 接受这是 foundational revision 的正常一环；做 incremental — 先找出反例，再决定加约束 vs 弱化 claim |
| Mathlib categorical equivalence library 在某处不够（如 Morita over F₂） | 中等 | 中 | Plan B：用 strict iso 替代 Morita；牺牲一些 generality 换 tractability |
| Strategy A 的 Stone-Birkhoff 链反向用需 non-trivial 适配 | 低 | 小 | 直接复用 + 加 transfer lemma |
| Phase 1 的 8 个 D1⟹P sub-streams 中某个 P 太难 | 已消除于 F₂ scope | 中 | F₂-Boolean branch 已由 `scoped_phase_one_closed` 汇总；剩余风险转移到 polymorphic/non-F₂ analytic extension |
| Non-algebraic δ instance 发现 P3 form 在 δ=Prop 上不平凡 | 中 | 中 | 这其实是 expected — non-algebraic δ 的 relational structure 不同；写 instance 时即把这一发现 documented；不影响 GUT-A claim |
| Peer 提了一个有效 D6 falsification | **低** | **极大**（claim 倒掉） | 拥抱 — falsifiability 是 strength 不是 weakness；按 v0.7+ Part VIII 的预案处理 |
| 6-12 月期间发现 v1.4 distinction-monism 的某个 sub-claim 需 revise | 低 | 中 | 文档分层结构允许 surgical revision；不重写整个 claim |

## 八、Out of Scope（GUT-A 之后再考虑）

这些都不在 6-12 月 minimum viable claim 路径上：

- **G11 T5-B** — parametric over algebraic class k（char(k)≠2 case + 完整 Wedderburn over rings）
- **G12 T5-C** — full δ-realisation including non-algebraic（research-level；可能需新 categorical framework）
- **G13 per-base bridges** — R/ℝ, R/ℂ, R/ℂ_p 完整 instance files
- **G10 V4 inductive elim** — Lean 层「one type」的最后一步；纯结构整洁
- **完整 6 个 universal claims 形式化** — currently 5/6 还是 programmatic（仅 UG 形式化）

完成 GUT-A 后再启动其中任意一项。**重点**：GUT-A 已是远超 Tegmark MUH / Wolfram Ruliad / 其他 GUT candidates 的 formal 严肃程度，stop 在那里 publish 是合理的。

## 九、Decision Points / What To Do First

**最高优先级（应该立即启动）**：

1. **Cite `scoped_gut_a_closed`** as the R-layer Scoped GUT-A entry point.

**第二优先级（Phase 0 启动后并行）**：

2. **Finite-field / non-canonical satisfier coherence** — keep the canonical field branch closed while deriving more coherence rather than supplying it.
3. **Automatic semantic witnesses** — class-by-class: Heyting, stabilizer/FdHilb boundary, frame/locale, enriched/Lawvere.

**第三优先级**：

4. **D6 exhaustiveness** — global route coverage remains open; current F₂ D6 exactness is scoped.

**与上面所有 streams 并行（不在 critical path）**：

5. **Phase 4 Stream NA-2**（D6 falsification testing）— ongoing
6. **Phase 3 Stream C3 + C4**（stabilizer-QM + FOL 嵌入）— 1-2 月每个；推荐至少做 C3 因为已经部分写在 Bilinear

**何时启动 Phase 5 / 6**：等 T5-A 通过后。Phase 5（empirical / peer）需要 publishable artifact；Phase 6（V4 inductive elim）是 polish，没紧迫性。

## 十、一句话总结

**Historical estimate superseded**：minimum viable GUT-A 已完成；原 critical path（Phase 0 → Phase 2 T5-A）已经闭合在 scoped F₂/GUT-A 范围。后续风险不在 Phase 0，而在更强的 automatic semantic witnesses、raw-core all-split coherent T5、finite-field/non-canonical coherence、D6 exhaustiveness、以及 GUT-C（full δ-realisation）。Split-coherent satisfiers 的 coherent T5 已由 `T5_split_coherent_GUT_B_package` 闭合。

---

## 附：与 wen-substrate v0.6 § 7.4 "What Remains" 的关系

v0.6 当时说 What Remains 是「engineering and refinement tasks, not foundation tasks」。本路线图是把那份 informal 承诺**升级成具体可执行的 6-12 月 implementation plan**：

| v0.6 "What Remains" | 本路线图对应 |
|---|---|
| Implementation: Build out R-Family in Lean 4 | ✅ 已经完成（125k LOC）；本路线图是 *next* implementation |
| Application: 加密 / 量子 / AI alignment | Phase 3 (case studies) + Phase 4 (non-algebraic δ) |
| Refinement: 5-fold virtues / character inventory | 已在 Atlas/ 完成；本路线图不再列 |
| Engagement | Phase 5 Stream E-2 |

v0.6 不曾 articulate T5 — 这是 v0.7+ Part VIII 加入的 obligation。本路线图把 T5（Tier 1 G2）放在 critical path 中央，因为没有 T5，GUT claim 就只是 "R-family 满足 P1-P7"，不是 "R-family **就是** universal substrate"。

---

## 十一、Achieved status (2026-05-16)

Single-session batch execution closed the **minimum viable GUT-A claim** with 0 sorry / 0 new axioms across all critical files. Status by gap:

| Gap ID | Item | Status | Lean file(s) | Commit |
|---|---|---|---|---|
| **G6.1** | T_P3 uniqueness (6/6 clauses) | ✅ closed | `R/PhaseZero.lean` § 1.1 | `0e18361` |
| **G6.2** | T_P6 Lorentzian bridge | ✅ closed | `R/PhaseZero/TP6Lorentzian.lean` | `55cfe40` |
| **G6.3** | T_P7b Wedderburn uniqueness + Mathlib bridge | ✅ closed | `R/PhaseZero/TP7bUniqueness.lean` | `924f583` |
| **G4** | δ=Prop non-algebraic instance | ✅ closed | `R/Distinction/Prop.lean` | P3/P5b/P6/P7b non-algebraic outcomes are now explicit `PropObligationStatus` tags, not vacuous `True` notes |
| **G1.A1** | D1 ⟹ P1 analytic | ✅ closed | `R/ClaimZ/Analytic/P1.lean` | `d575e81` |
| **G1.A2** | D1 ⟹ P2 analytic | ✅ closed | `R/ClaimZ/Analytic/P2.lean` | `f05807a` |
| **G1.A3** | D1 ⟹ P3 analytic | ✅ closed | `R/ClaimZ/Analytic/P3.lean` | `4f5bc5f` |
| **G1.A4** | D1 ⟹ P4 analytic | ✅ closed | `R/ClaimZ/Analytic/P4.lean` | `93d2fa2` |
| **G1.A5** | D1 ⟹ P5 analytic | ✅ closed | `R/ClaimZ/Analytic/P5.lean` | `023c92a` |
| **G1.A6** | D1 ⟹ P6 analytic | ✅ closed | `R/ClaimZ/Analytic/P6.lean` | `29b0fb0` |
| **G1.A7** | D1 ⟹ P7a analytic | ✅ closed | `R/ClaimZ/Analytic/P7a.lean` | `c8f69a7` |
| **G1.A8** | D1 ⟹ P7b analytic | ✅ closed | `R/ClaimZ/Analytic/P7b.lean` | `b486acb` |
| **G1.integration** | Phase 1 packaged into `D1_implies_Phase1Closure_F2` | ✅ closed | `R/ClaimZ/Analytic.lean` | `7c2a125` |
| **G2** | T5-A: P1-P7 ⟹ R-family-over-F₂ uniqueness (layerwise) | ✅ closed (tractable form) | `R/UniquenessF2.lean` | `23441fc` |
| **G2'** | T5 polymorphic: P1+P2 over any Fintype δ ⟹ R N δ layerwise | ✅ closed | `R/UniquenessGeneral.lean` | `a980e92` |
| **G2''** | T5 algebraic-class: P1+P2+P7b over any Field k ⟹ R N k layerwise + ring iso at carrier 4 | ✅ closed | `R/UniquenessAlgebraic.lean` | `821a2f3` |
| **G2'''** | Concrete polymorphic T5 demos at Distinction, ZMod 3, Fin 5 + Bool↔ZMod 2 cross-instance | ✅ closed | `R/UniquenessGeneral/Demos.lean` | `3e47cd7` |
| **G3.C3** | Stabilizer-QM (Pauli group) ↪ R 2n | ✅ closed | `Wen/Embeddings/StabilizerQM.lean` | `975104d` |
| **G3.C4** | FOL syntax tree ↪ R N | ✅ closed | `Wen/Embeddings/FOL.lean` | `f87c40f` |
| **G5** | D6 falsification record (HoTT/ETCS/SDG attempts) + concrete F₂ D6 exactness | ✅ closed, scoped | `R/ClaimZ.lean`, `R/D6_Tests.lean`, `R/ClaimZF2.lean` | D6 soundness/exhaustiveness/exactness are explicit interfaces; `claim_z_F2_D6_exact_for_D5` closes the current concrete F₂ D5/D6 pair; `F2_recorded_candidates_do_not_falsify` refutes the current recorded candidate predicates for that F₂ bundle; global D6-exhaustiveness remains open |
| **FullGUT.scoped-coordinate** | Scoped / Coordinate FullGUT theorem package | ✅ closed, scoped only | `Doctrine/FullGUT.lean` | `ScopedCoordinateFullGUT` / `scoped_coordinate_full_gut`; not absolute FullGUT |
| **FullGUT.conditional-absolute** | Conditional Absolute FullGUT theorem package | ✅ closed, conditional | `Doctrine/FullGUT.lean` | `absolute_conditional_full_gut` / `conditional_absolute_full_gut`; semantic-preservation witnesses remain explicit inputs |
| **FullGUT.T6-self-syntax** | R-family self-articulation syntax | ✅ closed, scoped syntax/stream level | `Doctrine/FullGUT.lean` | `rFamilySelfPresentation`, `rFamilySelfPresentation_satisfiesD1`, `rFamilySelfPresentation_stream_realisation`, `rFamily_self_articulation`; not a semantic evaluator for every native category |
| **FullGUT.native-Heyting-finite** | Automatic native Heyting semantic witness | ✅ closed, finite/encodable scope; posetal currying/end-action and strong internal-Hom obstruction closed | `Doctrine/Instance/HeytingNative.lean`, `Doctrine/Instance/HeytingCategoryNative.lean`, `Order/HeytingInternalHom.lean`, `Order/HeytingBimorphism.lean` | `NativeHeytAlg.finite_full_gut` / `encodable_stream_full_gut`, `NativeHeytAlg.HomPresentation` morphism packages, `heytAlg_posetal_closed_end_action_nonempty`, finite/encodable indexed bundled-`HeytAlg` category packages, `HeytingPosetalClosed`, and `IsHeytingBilinear₂.codomain_trivial`; bundled `HeytAlg` cartesian-closed category semantics remains open |
| **FullGUT.native-Quantum-stabilizer** | Automatic stabilizer semantic witness | ✅ closed, finite/encodable scope | `Doctrine/Instance/QuantumNative.lean`, `Doctrine/Instance/QuantumNativeDagger.lean`, `Doctrine/Instance/HilbertEnriched.lean`, `Wen/Embeddings/StabilizerQM.lean`, `Wen/Embeddings/HilbertPauliFunctor.lean`, `Wen/Embeddings/PhasedPauli.lean`, `Wen/Embeddings/PauliRingIso.lean` | `concrete_single_qubit_stabilizer_matrix_full_gut`, n-qubit `PauliN.commutesModPhase_iff_sigma_false` and reverse `R → Pauli` commutation transport, projective Pauli multiplication, exact same-width retained phase multiplication through `PhasedPauliN.toHilbert_compose`, phase-bearing tensor append through `PhasedPauliN.toHilbert_tensor`, phase/sigma swap law `pauliNPhase_swap`, concrete signed Hilbert commutation `pauliToHilbert_signed_commutation`, packaged `PhasedPauliN.HilbertCoherence`, presentation-level `NQubitMatrixDaggerWitness.signed_commutation` governed by `coordinateSymplectic`, `concrete_single_qubit_matrix_dagger_full_gut`, nonempty `NQubitPresentation n` coordinate packages, `concreteZeroQubitPresentation` as the matrix tensor-unit carrier only, `concrete_n_qubit_matrix_dagger_full_gut` for n-qubit matrix faithfulness plus self-adjoint/unitary dagger semantics, `NQubitMatrixOperatorFullGUT` / `n_qubit_matrix_operator_full_gut_nonempty` for generic finite native n-qubit operator packages, `concrete_n_qubit_matrix_operator_full_gut` for the concrete all-n operator branch, `concrete_n_qubit_phased_matrix_operator_full_gut` for retained-phase Hilbert coherence, `concrete_n_qubit_phased_monoidal_matrix_operator_full_gut` for phased operator packages plus binary tensor splits and three-factor associativity, `concrete_n_qubit_matrix_tensor_unit_boundary` and `concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary` for concrete 0-qubit unit coherence, `FinHilbObject`, `FinHilbCoordinateTensorBoundary`, `FinHilbCoordinateTensorIsometryBoundary`, `FinHilbCoordinateTensorCoherenceBoundary`, `FinHilbCoordinateKroneckerMorphismBoundary`, and `QuantumToHilbertBridge` for the concrete qubit Hilbert-object category bridge, `pauliHilbertTensorCoherence` for Pauli-word coordinate tensor split/unit/associativity, `concrete_n_qubit_matrix_tensor_full_gut` for presentation-level coordinate matrix tensor splits, `concrete_n_qubit_matrix_tensor_assoc_full_gut` for three-factor coordinate tensor associativity, and `pauli_n_qubit_spans n` for all-n Pauli vector-space spanning; 0-qubit D1/FullGUT and full `FdHilb` dagger-SMCC remain open |
| **FullGUT.native-Frame-cube** | Native Sierpinski-cube frame/locale witness | ✅ closed, scoped frame-cube/locale/braided-symmetric/tensor-bilinear boundary | `Doctrine/Instance/TopologicalNativeFrame.lean`, `Order/FrmBraided.lean`, `Order/FrmClosed.lean`, `Order/FrmClosedBraided.lean`, `Doctrine/Instance/TopologicalNativeLocale.lean` | `topological_native_frame_witness`, concrete `frmBraiding` iso/naturality/hexagons, `BraidedCategory Frm`, `SymmetricCategory Frm`, `frmTensorHomEquivJTBilin`, `FrmJTBilin.postcomp` / `precomp` with packaged functorial laws, `FrmJTBilin.swap_postcomp` / `swap_precomp`, `FrmJTBilinBraidedBoundary`, `frmTensorClosedHomEquiv_of_exponentialData_braiding_symm_eq_braiding_tensor_eval`, `FrmRepresentedClosedBoundary` right/left uncurrying-evaluation laws, and `topological_native_locale_witness`; exponential-frame / `MonoidalClosed Frm` and non-cartesian `Frm` tensor-exponential T_GUT remain open |

**Aggregate for the GUT-A/polymorphic closure rows**: 20 closures, 0 sorry / 0 axioms across all GUT-A + polymorphic files. Full library `lake build SSBX` = 3830 jobs clean. The scoped-coordinate FullGUT row records a later boundary package and is not counted in that historical closure total.

### 十一·1 Polymorphic T5 update (2026-05-16, `a980e92`)

Per user direction *"让我们把它推广到general，而不是只有bool"*, the layerwise T5 statement is now **δ-polymorphic** (works for any `[Fintype δ] [DecidableEq δ] [Inhabited δ]`):

```
theorem T5_general (S : P1P7_Core δ) (N : ℕ) : Nonempty (S.carrier N ≃ R N δ)
```

`R/UniquenessGeneral.lean` delivers:

- `P1P7_Core δ` — polymorphic minimum-data structure (carrier family + Fintype/decEq + zero-card + base-card + direct-sum), no ring requirements.
- `R.card_eq_general` — `|R N δ| = (|δ|)^N` polymorphic cardinality.
- `T5_general` — layerwise type-equiv for any δ with Fintype + DecidableEq + Inhabited.
- Four canonical δ-corollaries: `T5_general_at_Bool`, `T5_general_at_Distinction`, `T5_general_at_Fin n`, `T5_general_at_ZMod p`.
- `forgetF2ToCore` + `T5_A_from_general` — the F₂-Boolean `T5_A` is now a derived corollary at δ=Bool.
- `T5_general_squaring_compatible` — polymorphic squaring tower.
- `canonicalRFamily δ : P1P7_Core δ` — the R-family itself as a canonical instance (non-vacuous sanity check).
- `GUT_B_layerwise` — aggregator packaging the polymorphic content.

**What this re-positions**: the framework is no longer "F₂-Boolean classical" specifically; F₂-Boolean is the δ=Bool **specialization** of a polymorphic uniqueness claim. The minimum viable GUT claim is therefore:

> **GUT-B (layerwise)**: any structure satisfying the *core P1+P2* closure conditions over any `[Fintype δ] [DecidableEq δ] [Inhabited δ]` substrate is layerwise type-equivalent to R-family-over-δ.

What remains δ-specific (post-this-update):

- **Ring iso at carrier 4** (`T5_A_ringEquiv_at_4`) — requires δ with ring structure; F₂ + char(k)=2 fields extend trivially, char(k)≠2 needs Wedderburn-over-k.
- **Bilinear classification (P3)** — Arf invariant is char(k)=2 specific; discriminant replaces it for char(k)≠2.
- **P6/P7a alphabet pinning** — uses 4-element / 8-element cardinality, which generalize as `(|δ|)² = 4` only for δ = Bool.

These are the remaining items for the **full** GUT claim (T5-B + T5-C scope).

### 十一·2 Polymorphic completion update (2026-05-16, batch 5)

Three parallel agents in batch 5 completed the algebraic-class extension + concrete demos + doc updates:

**G2'' Algebraic-class T5** (`R/UniquenessAlgebraic.lean`, commit `821a2f3`):
- `P1P7_Satisfier_Algebraic (k : Type) [Field k] [Fintype k] [DecidableEq k]` — extends `P1P7_Core k` with `p7b_ring_equiv : Nonempty (carrier 4 ≃+* Matrix (Fin 2) (Fin 2) k)` + Mul/Add instances.
- `T5_algebraic` — combines T5_general (layerwise) with the ring iso at carrier 4 for any field k.
- F₂-Boolean lift via the **ZMod 2 bridge** (`forgetF2ToAlgebraic_ZMod2`): the existing `P1P7_Satisfier_F2`'s `p7b_mat2F2_equiv` composes with `Mat2F2 ≃+* Matrix (Fin 2) (Fin 2) (ZMod 2)` (from G6.3's TP7bUniqueness) to give a `P1P7_Satisfier_Algebraic (ZMod 2)`.
- Char(k)=2 demo at `ZMod 2` proves layerwise + ring-iso for F₂'s natural algebraic-class cousin.

**G2''' Concrete polymorphic demos** (`R/UniquenessGeneral/Demos.lean`, commit `3e47cd7`):
- δ=Distinction non-canonical instance via `Distinction.equivBool` transport.
- δ=ZMod 3 (`|R 2 (ZMod 3)| = 9`, `|R 3 (ZMod 3)| = 27`, ternary substrate).
- δ=Fin 5 (`|R 2 (Fin 5)| = 25`, 5-ary non-field substrate).
- Cross-instance: `R N Bool ≃ R N (ZMod 2)`, `R N Bool ≃ R N Distinction`, `R N Distinction ≃ R N (ZMod 2)`.
- `concrete_polymorphic_T5_demo` — 7-tuple aggregator packaging all witnesses.

**Doc updates** (`wen-substrate/02-parametric.md`, `07-claim.md`, `08-obligations.md`, commit `3edbeb7`):
- 02-parametric: added "Polymorphic T5" section documenting the four δ-corollaries.
- 07-claim: refined direct claim from "R-Family over F₂" to "δ-polymorphic R-Family; F₂ canonical not restriction".
- 08-obligations: 3-row T5 status table (T5 layerwise ✅, T5-A F₂ ring iso ✅, T5-B/C ring iso polymorphic ✅ via UniquenessAlgebraic).

**Aggregate (post-batch-5)**: 22 closures total, 0 sorry / 0 axioms, lake build 3830+ jobs clean. The polymorphic generalization is **complete** at the layerwise + ring-iso (over Field k) level.

What remains for the **strongest** GUT claim form:

- **Char(k)≠2 bilinear classification**: discriminant-based P3 for non-char-2 fields.
- **Non-algebraic δ (Prop, Heyting algebra, etc.)**: requires constructive/non-Fintype handling; T5-C territory.
- **D1 ⟹ P-closure over polymorphic δ**: currently `D1_implies_Phase1Closure_F2` is δ=Bool specific; polymorphic D1 analytic direction is an open extension.
- **Native semantic upgrades**: bundled `HeytAlg` cartesian-closed category semantics, full Hilbert/dagger `FdHilb` semantics, and exponential-frame / non-cartesian `Frm` tensor-exponential semantics remain open. Ordinary indexed bundled-`HeytAlg` category witnesses, Heyting posetal currying, the strong `HeytAlg` internal-Hom obstruction, and the concrete `Frm` braided/symmetric/tensor-bilinear boundary are closed separately.
- **Power/enriched all-semantics**: current enriched work is scoped bridge/data transport, not all V-enriched SMCCs or Power 1999.
- **Arbitrary-satisfier coherent T5**: all-split coherence and finite-field satisfier derivations still need explicit structure beyond raw `P1P7_Core`.
- **D6 exhaustiveness**: the concrete F₂ D6 falsification bundle is refuted, but the meta-level exhaustiveness of the three routes is not closed.

These are research-level extensions; the **minimum viable polymorphic GUT claim** is now formally proven for any Fintype + DecidableEq + Inhabited δ at the layerwise level, and for any Field k at the ring-iso level.

### What "minimum viable GUT-A" means at this status

**Analytic direction** (Claim Z 's D1 ⟹ P-closure side):

> `theorem D1_implies_Phase1Closure_F2` — given a `D1Articulation S` satisfying the eight D1 atomic conditions, the `Phase1Closure_F2` record carries witnesses for P1-P7 (8 fields including P7a + P7b sub-properties), all derived from the eight `Analytic/P*.lean` modules with no PClosure assumption.

**Synthetic direction** (Claim Z's P-closure ⟹ R-family side):

> `theorem T5_A` — for any `P1P7_Satisfier_F2 S`, every layer `S.carrier N ≃ R N` as a type. Plus `T5_A_ringEquiv_at_4` (ring-iso at the smallest non-trivial layer), `T5_A_squaring_compatible` (squaring tower respected), `T5_A_aggregator` (the satisfier-level aggregate), and `T5_A_full_side_obligations` in `T5AClosure.lean` (canonical R∞, external-overlay transport, satisfier-level R₄ ring/cardinality, canonical R₄ action laws, transported atomic action semantics).

**Falsifiability**: three independent candidate falsifications (HoTT / ETCS / SDG) formally documented as non-instantiators of `D6_ClaimZFalsified` with structural reasons (univalence is δ-enrichment, ETCS↔BZC, SDG = R-Family-over-`k[ε]/(ε²)`).

**Universality witnesses**: F₂-Boolean classical R-Family + δ=Prop non-algebraic instance (G4) + Pauli-stabilizer QM (G3.C3) + propositional logic (G3.C4) — four explicit articulation cases.

### What remains (post-GUT-A refinement)

| Gap | Status | Note |
|---|---|---|
| **T5-A items 4, 6** | closed, scoped | Bilinear / Hom naturality under `p2_directSum`; fields and canonical witnesses are in `UniquenessF2.lean` |
| **T5-A items 8, 9, 11** | closed at current scoped boundary | `T5AClosure.lean` packages canonical R∞, external-overlay transport, satisfier-level R₄ ring/cardinality, canonical R₄ action laws, and transported atomic action semantics; native intended-action identification still needs action/coherence fields |
| **FullGUT D1 bridge** | closed, scoped | `FullGUT.formalPresentation_satisfiesD1_to_D1Articulation` bridges concrete `FormalPresentation.SatisfiesD1` into ClaimZ `D1Articulation`; `FullGUT.categoryFormalPresentation_satisfiesD1` gives a concrete D1 presentation for every small category with decidable object equality and a chosen base object, and `lawvereFormalPresentation_satisfiesD1` specializes this to ordinary Lawvere theories via their generator; `PhiOperator.ArticulationCandidate.ClaimZBridge.D1_toD1Articulation_fields_hold` projects the fixed-point `D1` candidate into a witnessed ClaimZ D1 interface; recursion remains explicit data for arbitrary presentations |
| **FullGUT translation API** | closed, infrastructure | `FormalTranslation.id` and `FormalTranslation.comp` make structure-preserving translations composable; `FormalTranslation.ExtEq`, `id_comp`, `comp_id`, `comp_assoc`, and `category_laws` prove the expected extensional category laws on the six syntactic maps without claiming semantic naturality beyond the explicit finite/encodable code squares |
| **FullGUT finite + encodable T3** | closed, scoped | `FullGUT.finite_formal_translation_code_naturality` and `FullGUT.encodable_formal_translation_code_naturality` prove `FormalTranslation` maps induce commuting R-code maps on all six syntactic sorts, respectively for finite layers and Boolean streams; finite/stream code maps preserve identity and composition on valid codes; full semantic T3 remains per-system work |
| **FullGUT T3 code functoriality packages** | closed, scoped | Finite and encodable `FormalTranslation` identity/composition now have package theorems, not only raw sort-map lemmas |
| **FullGUT finite/encodable admissible corollaries** | closed, scoped | `full_gut_for_finite_admissible_formal_systems` and `full_gut_for_encodable_admissible_formal_systems` remove the extra semantic-witness argument for finite D1 systems and encodable D1 systems respectively |
| **GUT-B coherent-core direct sums** | closed for split-coherent satisfiers; raw-core successor/gated | `P1P7_SplitCoherentCore` records coordinate split laws, `P1P7_SplitCoherentCore.split_coherent_directSumStructuralIso` constructs the all-split witness, and `T5_split_coherent_GUT_B_package` closes coherent T5 for split-coherent satisfiers. For field-valued split-coherent cores, `splitCoherentFieldSatisfier`, `T5_field_split_coherent_direct_sum_GUT_B_package`, and `T5_field_split_coherent_coherent_GUT_B_package` also synthesize the carrier-4 matrix-ring data by coordinate transport. `P1P7_CoherentCore.direct_sum_structural_iso`, `ofDirectSumStructuralIso`, and `coherent_GUT_B_package` remain the low-level supplied-direct-sum path; raw `P1P7_Core` is packaged separately at successor-structural strength |
| **T5-A native atomic action interface** | closed, conditional | `T5ANativeAtomicActionData` records independent native action data plus transport compatibility with canonical `R 4 = End(R 2)`; `T5_A_item11_native_atomic_action_coherence` derives unit/composition action laws |
| **FullGUT scoped D5/D6 package** | closed, scoped | `current_scoped_D5_holds` packages the current finite/encodable, F₂, GUT-B, and primary-TypeCat branches into the D5 shape; `current_scoped_D6_exact_for_D5` proves exactness of the concrete F₂ D6 bundle against that current scoped D5 package; `current_scoped_D6_of_not_D5` gives the fixed-pair exhaustiveness direction; `current_scoped_D6_refuted_from_exactness` re-derives the concrete refutation from exactness plus the proved scoped D5 package; `current_full_gut_theorem_stack` bundles the scoped D5 proof and scoped D6 exactness with the substrate certificate without claiming unrestricted Claim Z |
| **ScopedCoordinateFullGUT package** | closed, scoped/coordinate only | `ScopedCoordinateFullGUT` / `scoped_coordinate_full_gut` is the stable Lean theorem package for the current boundary: finite/encodable representation, code-level T3, F₂/GUT-A, GUT-B structural boundaries, primary TypeCat coordinate packages, R-scope boundary, concrete F₂ D6 refutation, and small-category/Lawvere D1 entry points. It is not absolute FullGUT |
| **ConditionalAbsoluteFullGUT package** | closed, conditional absolute | `absolute_conditional_full_gut` proves faithful R-realisation for every admissible D1 formal system with supplied `SemanticsPreservable`; `absolute_conditional_full_gut_stream` is the stream analogue; `conditional_absolute_full_gut` packages both with the scoped-coordinate closure. It does not automatically construct semantic-preservation witnesses |
| **Native finite/encodable Heyting witness** | closed, scoped native | `NativeHeytAlg.Presentation` ties a formal system's object sort to native Heyting operations; `HeytingInternalHom.lean` proves posetal currying `a ⊓ b ≤ c ↔ b ≤ a ⇨ c`; `FiniteClosedFullGUT` and `EncodableClosedStreamFullGUT` now package the finite/stream native Heyting FullGUT branches with that bare posetal closed witness before the morphism layer; `NativeHeytAlg.HomPresentation` adds syntax morphisms represented by native `HeytingHom`s with source/target, identity, and composition laws; `HeytingCategoryNative.lean` lifts hom presentations to bundled `HeytAlg` end-actions, adds the posetal-closed end-action package, and closes finite/encodable indexed bundled-`HeytAlg` category packages. `IndexedPosetalClosedSemantics` now threads per-object Heyting evaluation/currying through those indexed category packages. `NativeHeytAlg.finite_semantics_preservable`, `encodable_stream_semantics_preservable`, `finite_closed_full_gut_nonempty`, `encodable_closed_stream_full_gut_nonempty`, `finite_hom_closed_full_gut_nonempty`, `encodable_hom_closed_stream_full_gut_nonempty`, `finite_indexed_category_full_gut_nonempty`, and `encodable_indexed_category_stream_full_gut_nonempty` feed these through the conditional-absolute stack. `IsHeytingBilinear₂.codomain_trivial` rules out strong separately-`HeytingHom` evaluation into nontrivial codomains. Bundled `HeytAlg` cartesian-closed category semantics remains open |
| **Native stabilizer witness** | closed, scoped native | `NativeStabilizerQuantum.SingleQubitPresentation` ties a formal system's object sort to `PauliBase`, names phase-quotient compose/identity/dagger tokens, and carries a faithful `2 × 2` complex Pauli matrix representation. `concrete_single_qubit_stabilizer_matrix_full_gut` gives a no-parameter concrete package plus Pauli spanning/independence for `Mat₂(ℂ)`, `StabilizerQM.PauliN.commutesModPhase_iff_sigma_false` and `HilbertPauliFunctor.reverse_commutesModPhase_iff_sigma_false` close the n-qubit mod-phase σ/commutation bridge, `pauliBaseToHilbert_compose_projective` proves phase-quotient composition agrees with matrix multiplication up to `{1,-1,I,-I}`, `pauliBaseToHilbert_mul_phase` proves exact single-qubit multiplication with retained central phases, `pauliToHilbert_mul_phase` proves exact same-width n-qubit retained multiplication, `pauliNPhase_swap` identifies phase swap with `R.sigma`, `pauliToHilbert_signed_commutation` proves the concrete matrices commute/anticommute by that same bit, `PhasedPauliN.toHilbert_compose` packages a phase-bearing representation whose Hilbert matrices multiply exactly, and `PhasedPauliN.toHilbert_tensor` proves the phase-bearing representation respects tensor append. `NQubitMatrixDaggerWitness.signed_commutation` lifts the same signed commutation law to native presentation objects via `coordinateSymplectic`. `concrete_single_qubit_matrix_dagger_full_gut` adds the single-qubit matrix-level self-adjoint/unitary dagger witness. `NativeStabilizerQuantum.NQubitPresentation n` closes the nonempty finite/encodable `n`-qubit Pauli-coordinate branch via `coordinateRep : Obj → R (2*n)`, and `concrete_n_qubit_matrix_dagger_full_gut` adds recursive Hilbert-matrix faithfulness plus self-adjoint/unitary semantics for those n-qubit presentations. `concreteZeroQubitPresentation` supplies the singleton 0-qubit matrix tensor unit but intentionally has no D1/FullGUT theorem. `NQubitMatrixOperatorFullGUT` / `n_qubit_matrix_operator_full_gut_nonempty` add all-n operator spanning to any finite native n-qubit presentation; `concrete_n_qubit_matrix_operator_full_gut` remains the concrete specialization, `concrete_n_qubit_phased_matrix_operator_full_gut` adds retained-phase Hilbert coherence to that package, `concrete_n_qubit_phased_monoidal_matrix_operator_full_gut` bundles phased operator witnesses with binary matrix tensor splits and three-factor associativity for nonempty blocks, and `concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary` adds concrete 0-qubit unit coherence. `HilbertEnriched.lean` now provides `FinHilbObject`, coordinate Hilbert spaces, coordinate Kronecker morphism laws, matrix linear maps, `QuantumToHilbertBridge`, `ConcreteSingleQubitHilbertDaggerBridge`, all-`n` `NQubitQuantumToHilbertBridge`, direct `RToHilbertQuantumWitness`, and `NQubitPresentationHilbertDaggerOperatorBridge` for generic finite native presentations, and `ConcreteNQubitHilbertDaggerOperatorBridge`. `pauliHilbertTensorCoherence` closes arbitrary Pauli-word coordinate tensor split/unit/associativity; `nQubitMatrixRep_appendObj` and `concrete_n_qubit_matrix_tensor_full_gut` close presentation-level coordinate matrix tensor splits; `concrete_n_qubit_matrix_tensor_assoc_full_gut` closes three-factor presentation-level coordinate tensor associativity; `concrete_n_qubit_matrix_tensor_unit_boundary` closes concrete 0-qubit tensor-unit coherence; `pauli_n_qubit_spans n` closes all-n Pauli vector-space spanning of `Mat_{2^n}(ℂ)`. Full `FdHilb` / dagger-SMCC semantics remains open |
| **Native frame-cube witness** | closed, scoped native | `TopologicalNativeFrameWitness` packages represented TypeCat topological sayability together with the native Sierpinski-cube frame coproduct iso and strong JT `FrameHom` universal property. `FrmBraided.lean` proves the concrete Joyal-Tierney braiding iso, left/right naturality squares, braided hexagons, and symmetric coherence, registering `BraidedCategory Frm` and `SymmetricCategory Frm`. `FrmClosed.lean` proves `(frmTensorObj X Y ⟶ Z) ≃ FrmJTBilin X Y Z` and the `FrmJTBilin.postcomp` / `precomp` functorial API. `FrmClosedBraided.lean` proves that this tensor-to-bilinear equivalence respects the concrete braiding by variable swap, that swap commutes with the pre/post composition API, and that supplied exponential data has right and braided-left uncurrying/evaluation laws packaged by `FrmRepresentedClosedBoundary`. `TopologicalNativeLocaleWitness` additionally records the Joyal-Tierney monoidal/braided/symmetric structure on `Frm`, the tensor-to-bilinear equivalence, its functorial and braided boundary packages, the represented exponential currying/uncurrying boundary, the opposite-category monoidal structure on `Frmᵒᵖ`, the `topToLocale ⊣ Locale.pt` adjunction, and compact-Hausdorff-to-locale faithfulness. `FrameVsHeytingMorphismDifferentialData` keeps the Frm-vs-Heyting strict morphism-class separation as an explicit witness obligation. Exponential-frame / `MonoidalClosed Frm` and non-cartesian `Frm` tensor-exponential T_GUT remain open |
| **Native semantic witness frontier** | closed, scoped aggregator | `SemanticWitnessFrontier` bundles already-closed bare native Heyting posetal-closed packages, native Heyting hom/indexed packages, finite-coordinate Hilbert tensor/unit, tensor/unit reindexing isometry, tensor coherence, dagger/tensor, and Kronecker morphism boundaries, direct R-to-Hilbert/all-`n` stabilizer quantum-Hilbert, generic finite native n-qubit Hilbert/operator, concrete 0-qubit stabilizer tensor-unit boundary, phased unital monoidal stabilizer matrix boundary, and topological locale/frame witness families under `semantic_witness_frontier_nonempty`; its topological fields now expose right and braided-left represented uncurrying/evaluation laws for supplied `FrmExponentialData`; it deliberately excludes the still-open categorical/exponential/enriched targets |
| **FullGUT native frontier package** | closed, scoped aggregator | `CurrentNativeSemanticFullGUTFrontier` combines the conditional/scoped FullGUT theorem stack with `SemanticWitnessFrontier` in a downstream module, avoiding an import cycle back into `FullGUT.lean`; direct accessors expose the R-to-Hilbert substrate action boundary, finite-coordinate Hilbert tensor/unit, tensor/unit reindexing isometry, tensor coherence, dagger/tensor, and Kronecker morphism boundaries, stabilizer Hilbert coherence boundary, concrete stabilizer matrix tensor-unit boundary, and phased unital monoidal matrix boundary without unpacking the aggregate |
| **FullGUT R/T5 frontier package** | closed, scoped aggregator | `CurrentRT5Frontier` combines `CurrentScopedT5` with the automatic-characteristic canonical finite-field all-split package, the split-coherent generic all-split package, and the structure-gated field coherent-direct-sum bridge in a downstream module, keeping field/Wedderburn dependencies out of `FullGUT.lean`; direct accessor theorems expose the canonical all-split/coherent field branches, compact canonical/gated noncanonical finite-field boundary, raw-core gated branch, split-coherent branch, generic/algebraic/field supplied-direct-sum coherent bridges, field char-class dispatcher, and F₂ side-obligation package |
| **FullGUT combined frontier package** | closed, scoped aggregator | `CurrentFullGUTFrontier` combines the Tier-1, Tier-2, Tier-3, and G11 cut-1 closure certificates, native-semantic frontier, ordinary/enriched Lawvere frontier accessors, and R/T5 frontier. It exposes direct R/T5, native finite-Hilbert stabilizer coherence/substrate-action/tensor-unit plus coordinate Kronecker morphism boundaries, enriched-Lawvere ordinary-D1 bridge, finite `Type` ordinary/enriched model-category equivalence, finite-`Type` bridge fully-faithful / `Functor.IsEquivalence` projections, G11, odd-prime Heisenberg-Weyl coordinate/operator boundaries including the scoped concrete finite-Hilbert operator package and object-action boundary, and scoped D5/F₂-D6 audit accessors while keeping dependency-heavy branches out of `FullGUT.lean` |
| **FullGUT R-scope certificate field** | closed, scoped | `full_gut_r_scope_boundary` exposes the generic R-kernel scope boundary at the FullGUT layer, and `UniversalFormalSubstrateCertificate.r_scope_boundary` carries it alongside the existing theorem-stack fields |
| **T6 self-articulation syntax** | closed, scoped syntax/stream | `rFamilySelfPresentation` gives a D1 `FormalPresentation` for R-family layer, morphism, relation, operation, rule, and proof syntax; `rFamilySelfPresentation_stream_realisation` proves a faithful Boolean-stream R-realisation; `rFamily_self_articulation` is carried by `CurrentScopedT6` |
| **Primary TypeCat scope-aware packages** | closed, scoped | `PrimaryTypeCatCompletePackages` now includes `ScopeAwareUniversalSayability` for algebraic/F₂, Witt, Heyting, Quantum, and Topological instances by reusing each instance's complete law packages plus the generic R-scope boundary |
| **GUT-C ordinary-law bridge** | closed, scoped | `EnrichedTGUTRealisation.core_full_of_plain_adequate_transport` / `core_natural_of_plain_adequate_transport` reuse the ordinary full-core and core-natural theorems from adequacy plus canonical transport; `complete_of_plain_law_packages` / `scope_aware_of_plain_law_packages` and `EnrichedUniversalSayabilityScopedStatement` / `enriched_universal_sayability_statement` reuse the existing ordinary complete and scope-aware T_GUT law packages inside an enriched ambient category; `enriched_universal_sayability_at_Hilbert_statement` supplies the concrete finite-Hilbert qubit bridge; ordinary `LawvereTheory` now exposes power projection helpers, full/faithful model forgetful functor, theory-morphism/model-pullback composition API, supplied monad/theory data in both directions, and explicit `LawvereTheoryFinitaryMonadComparisonData`; `EnrichedLawvereTheory` now has explicit arity objects, iso-carrying arity existence, chosen arity isomorphisms via `arityIso`, the canonical ordinary `Type` enrichment bridge, a plain-to-Type arity skeleton projection, ordinary `Model` object/morphism/functor transport into finite `Type`-enriched models, the reverse finite `Type`-enriched model to ordinary model functor, both round-trip natural isomorphisms, named equivalence functor/inverse/unit/counit projections, the scoped finite-`Type` model-category equivalence with fully-faithful / `Functor.IsEquivalence` projections, a cartesian-to-plain signature projection, explicit `EnrichedLawvereFinitaryMonadComparisonData`, and supplied-data boundaries for additive, linear, 2-Lawvere, symmetric-tensor, and GUT-C sketch declarations; `Cotensor.lean`, `Weighted.lean`, `Monad.lean`, and `Finitary.lean` now require supplied cotensor, universal-property, naturality, monad-law, preservation, and Type-specialisation data instead of hidden `True` fields; `Power.lean` now projects supplied forward/reverse/comparison data rather than fake `True` statements; `HasFreeVModels`, `FreeForgetfulAdjunctionData`, and `TheoryMonadData`/`MonadTheoryData` replace former fake free/adjunction/Power constructors with explicit data |
| **GUT-B successor-structural coherence** | closed, scoped | `P1P7_Core.successor_structural_iso` recursively chooses `carrier N ≃ R N δ` and proves every successor split commutes with canonical R; `P1P7_Core.successor_GUT_B_package` bundles that witness with layerwise equivalence and cardinality recovery; arbitrary `(n,m)` split coherence still needs extra coherence laws |
| **HeytAlg internal-Hom / FdHilb / Frm semantics** | open at categorical/exponential level | Finite/encodable native Heyting-algebra presentations now include explicit `HeytingHom` morphisms, posetal-closed end-action packages, and ordinary indexed bundled-`HeytAlg` category witnesses; posetal Heyting currying is closed by `HeytingPosetalClosed`; strong separately-`HeytingHom` evaluation into nontrivial codomains is ruled out by `IsHeytingBilinear₂.codomain_trivial`; stabilizer presentations include the single-qubit matrix anchor, same-width retained phase multiplication, nonempty Pauli-string coordinate packages, n-qubit matrix faithfulness/self-adjoint/unitary witnesses, all-n Pauli vector-space spanning, and a concrete finite-Hilbert object category bridge; Sierpinski-cube frame coproduct/JT packages and concrete `Frm` braided/symmetric/tensor-bilinear/functorial/braiding-compatibility boundary class instances have automatic witnesses, and supplied `FrmExponentialData` now carries right and braided-left represented β-style uncurrying/evaluation laws. Bundled `HeytAlg` cartesian-closed category semantics, full Hilbert/dagger semantics, exponential-frame / `MonoidalClosed Frm`, and full non-cartesian `Frm` tensor-exponential T_GUT are not closed |
| **Power/enriched all-semantics** | open | Enriched files provide scoped bridges, finite Type-enriched Lawvere/model APIs including ordinary/finite-enriched model functor transport in both directions, Type/Type cotensor, weighted-limit bridge accessors, raw supplied theory/monad package accessors, and supplied-law frontier packages; this is still not all-semantics or Power 1999 universal sayability |
| **Raw-core all-split coherent T5** | open for raw cores; split-coherent field synthesis closed | Coherent T5 is closed for split-coherent satisfiers by `T5_split_coherent_GUT_B_package`. Raw `P1P7_Core` has the packaged successor theorem `successor_GUT_B_package`; supplied all-split packages convert into `P1P7_CoherentCore` and feed `coherent_GUT_B_package`; `T5_field_coherent_GUT_B_package_of_direct_sum` packages the field coherent-core consequences when that direct-sum witness is supplied; `T5_field_split_coherent_direct_sum_GUT_B_package` synthesizes a field satisfier and all-split field package from split-coordinate laws. Deriving arbitrary all-split/direct-sum coherence and arbitrary finite-field satisfier equivalence from raw hypotheses remains open |
| **D6 exhaustiveness** | open globally; scoped F₂ exactness closed | D6 soundness/exhaustiveness/exactness are explicit interfaces and the current concrete F₂ D5/D6 pair is exact; the claim that every possible Claim Z failure is captured by the three D6 routes remains global work |
| **G7** cross-base functor library | closed, scoped | F₂/stabilizer-Hilbert branch closed by `FullGUTTier2Frontier.current_tier2_G7_cross_base_stabilizer_hilbert`; the native frontier exposes scoped finite-Hilbert dagger plus coordinate tensor/unit and Kronecker morphism boundaries; odd-prime Heisenberg-Weyl coordinate symplectic and supplied-character operator boundaries are now in G11, with the scoped concrete finite-Hilbert operator, object-action, and dagger boundaries closed and full `FdHilb` categorical semantics remaining G11/GUT-C work |
| **G8** empirical predictions | readiness closed | Protocol/catalogue fixtures closed by `FullGUTTier3Frontier.current_tier3_G8_empirical_readiness`; external experiments remain outside Lean |
| **G9** peer engagement | readiness closed | Adversarial question catalogue closed by `FullGUTTier3Frontier.current_tier3_G9_peer_engagement_readiness`; external review/endorsement remains outside Lean |
| **G10** V4 inductive → abbrev | boundary closed | `FullGUTTier3Frontier.current_tier3_G10_v4_migration_boundary` pins the current V4 surface to `R 2`; repository-wide rewrite remains optional polish |
| **G11** arbitrary finite-field satisfier T5 | scoped cut-1 closed | `FullGUTG11Frontier.current_g11_closure` packages canonical finite-field and prime-field branches, structure-gated arbitrary field consequences, odd-prime discriminant classification, the `HeisenbergWeylZModP` coordinate symplectic boundary, and the `HeisenbergWeylOperators` primitive complex additive phase / one-site clock-shift / multi-site zero-operator / projective multiplication / commutator-phase / unitarity / phase-point faithfulness / pure-shift reachability / pure-clock projector / matrix-unit Fourier / matrix-span / invariant-subspace irreducibility / finite-Hilbert operator, object-action, and dagger boundaries (see [`heisenberg-weyl-narrative.md`](heisenberg-weyl-narrative.md) for the consolidated narrative); deriving ring/direct-sum data for arbitrary raw non-canonical satisfiers, full `FdHilb` categorical semantics, and an explicit Heisenberg-Weyl ↔ `Cell256 = R 8 (over Bool)` bridge remain open |
| **G12** T5-C full δ-realisation | open | Research-level; may need new categorical framework |
| **G13** per-base ℝ/ℂ/ℂ_p bridges | open | Mathlib classical foundations |

### Recommended next moves

1. **Raw finite-field satisfier synthesis**: the split-coordinate branch now constructs `p7b_ring_equiv` and direct-sum coherence from explicit split laws; the remaining harder target is deriving comparable structure for arbitrary raw / pre-existing finite-field satisfiers without weakening the hypotheses.
2. **Odd-prime Heisenberg-Weyl bridge**: the `ZMod p` phase-space/R-coordinate equivalence and alternating symplectic laws are closed by `HeisenbergWeylZModP`; `HeisenbergWeylOperators` now supplies the Mathlib additive-character bridge, primitive complex additive phase, one-site clock/shift commutation law, multi-site zero phase-point matrix identity, projective multiplication, symplectic commutator-phase representation, left/right unitarity, phase-point faithfulness, pure-shift reachability, pure-clock coordinate projectors, coordinate matrix-unit Fourier sums, full coordinate matrix-algebra span, invariant-subspace irreducibility, and the scoped concrete finite-Hilbert operator, object-action, and dagger boundaries; `HilbertEnriched` now lifts those matrices to projective unitary endomorphisms of the concrete coordinate finite-Hilbert object and separately exposes native coordinate tensor/unit objects and coordinate Kronecker morphism laws. The next quantum target is a genuine bundled `FdHilb`/dagger-category layer, then monoidal Hilbert functor data; the current dagger plus coordinate tensor/unit and Kronecker morphism boundaries are local to `FinHilbObject` coordinate/linear morphism data.
3. **Native action identification**: add intended satisfier action data where needed and compare it to `T5_A_item11_transport_atomic_action`.
4. **External workstreams**: use the G8/G9 protocol fixtures for experiments and adversarial review without treating those external outcomes as Lean theorems.

The original 3-6 月 estimate now applies to residual GUT-B/G11+ synthesis work — raw non-canonical finite-field satisfier data, infinite-field/per-base bridges, and supplied-data removal where possible — plus **GUT-C** full δ-realisation, not GUT-A or the already closed layerwise/algebraic-class GUT-B branches.

---

## 十二、G11 cut-1 plan — char(k)≠2 finite fields (2026-05-17)

Per `docs-next/00_start/lawvere-identification.md` v0.4 status — metalogic identification done, GUT-A polish path identified. Next major milestone: extend the scoped GUT-B finite-field frontier: canonical finite fields, prime fields, char-class dispatch, split-coordinate finite-field synthesis, and structure-gated arbitrary finite-field satisfiers, while leaving arbitrary raw non-canonical satisfier synthesis open.

### Why cut-1 over full G11

Full G11 (任意 field k, 含 ℝ/ℂ/ℚ_p) requires Brauer group machinery, Witt theory over arbitrary fields, Hasse-Minkowski local-global — **research-level, 4-8 月**.

**Cut-1 scope**: canonical finite fields, prime-field branches `ZMod p`, odd-prime discriminant classification, and structure-gated arbitrary finite-field satisfiers. Skips:
- Infinite fields (ℝ, ℂ, ℚ_p) — left to G11+ / GUT-C
- Brauer group infrastructure (over finite fields Br(F_q) = 0 trivially via Wedderburn's little theorem)
- Unified char-agnostic treatment — char 2 stays Arf-based, char ≠ 2 gets parallel disc-based

⟹ Cut-1 compressible to **~2-3 月** (vs full G11 4-8 月) via parallel execution.

### Cut-1 sub-tasks

| Sub-task | Status | File | Owner |
|---|---|---|---|
| **G11-A** Install `IsSimpleRing`/`IsArtinianRing` on Mat₂(F_q) | ✅ closed | `Foundation/R/Algebra/MatFqInstances.lean` | matrix rings over fields/division rings have the needed simple-Artinian and Wedderburn-applied anchors |
| **G11-B** Discriminant-based P3 for char(k)≠2 finite fields | ✅ closed at prime-field classification scope | `Foundation/R/Bilinear/DiscriminantCharNeq2.lean` | odd-prime bilinear recovery, discriminant classes, and finite-field quadratic-form uniqueness are proved for `ZMod p` |
| **G11-C** Polymorphic UniquenessGeneralField scaffold + char-class dispatch | ✅ scoped cut-1 closed | `Foundation/R/UniquenessGeneralField.lean`; `Foundation/Doctrine/FullGUTG11Frontier.lean` | canonical finite-field, prime-field, char-dispatch, and structure-gated arbitrary-field packages are closed; arbitrary satisfier derivation remains structure-gated |
| **G11-D** T5-A items 4+6 closing (GUT-A polish, orthogonal) | ✅ closed | `Foundation/R/UniquenessF2.lean`; included in `scoped_gut_a_closed` via `T5_A_aggregator` | closed |

**Current Lean aggregate**: `FullGUTG11Frontier.current_g11_closure` packages the closed cut-1 boundary. G11-A unblocks Wedderburn application; G11-B provides the char ≠ 2 bilinear/discriminant classifier; G11-C ties canonical finite fields, prime fields, char-class dispatch, and structure-gated arbitrary satisfiers together; G11-D was already absorbed into scoped GUT-A.

### Cut-1 completion criteria

- G11 frontier and its imported source files pass targeted Lean checks
- `Foundation/R/UniquenessGeneralField.lean` provides `T5_field` over any `[Field k] [Fintype k]` with char-class dispatch
- Canonical prime-field packages `T5_field_at_ZMod p` plus concrete demos at `ZMod 3` and `ZMod 5` produce non-trivial layerwise + ring-iso witnesses; `T5_field_direct_sum_GUT_B_package_at_ZMod` upgrades the generic prime-field branch to all-split GUT-B using canonical split-coordinate coherence
- T5-A items 4+6 closed; remaining caveat is native/intended action identification for independently supplied action data, not Scoped GUT-A closure.

### Post-cut-1 remaining (deferred to G11+ / GUT-C)

| Item | Estimate |
|---|---|
| Infinite fields ℝ / ℂ / ℚ_p | 6-12 月 (Brauer + Witt + Hasse) |
| Discriminant-Arf unified treatment | 1-2 月 |
| Per-base bridges (G13) | 月-each |

These are no longer blocking scoped GUT publication; cut-1 brings a publishable finite-field frontier for canonical finite fields, prime fields, split-coordinate finite-field cores, and structure-gated arbitrary finite-field satisfiers, while raw non-canonical satisfier synthesis remains open.

### Status snapshot — what's already closed

(Per §十一 + this cut-1 session, post-2026-05-17)

| Layer | Status |
|---|---|
| GUT-A (F₂-Boolean classical) | ✅ closed (2026-05-16) |
| GUT-A items 4+6 (T5-A naturality residuals) | ✅ closed |
| GUT-A items 8/9/11 side boundary | ✅ scoped closure; native-action identification remains separate |
| FullGUT D1 bridge | ✅ closed, recursion explicit |
| FullGUT translation API | ✅ closed |
| FullGUT finite + encodable T3 code naturality | ✅ closed |
| FullGUT T3 code functoriality packages | ✅ closed |
| FullGUT finite/encodable admissible corollaries | ✅ closed |
| GUT-B coherent-core direct sums | ✅ closed conditionally |
| T5-A native atomic action interface | ✅ closed conditionally |
| FullGUT scoped D5 package | ✅ closed scoped |
| ScopedCoordinateFullGUT / `scoped_coordinate_full_gut` | ✅ closed scoped/coordinate only |
| ConditionalAbsoluteFullGUT / `conditional_absolute_full_gut` | ✅ closed conditional absolute |
| GUT-C ordinary-law bridge | ✅ closed scoped |
| Canonical `Type` ordinary enrichment | ✅ closed scoped; ordinary hom-type enrichment only, not full Type-enriched Lawvere/Power semantics |
| `Type`/`Type` cotensor | ✅ closed scoped; function-space cotensor in `Type u`, not arbitrary V-cotensors or weighted limits |
| Cotensor terminal-weight bridge | ✅ closed scoped; derived from `HasCotensor`, not arbitrary weighted limits |
| Constant-weight conical bridge | ✅ closed scoped; derived from existing `HasConicalLimit`, not arbitrary weighted limits |
| Cotensor/weighted comparison frontier | ✅ closed scoped; selected-object equalities, comparison-data constructor, and cotensor naturality/lift/coev classification accessors, not arbitrary weighted limits or Power 1999 |
| Finite-scoped `Type` enriched Lawvere | ✅ closed scoped; plain Lawvere finite products and arity data, not arbitrary conical products |
| Finite-scoped enriched model category | ✅ closed scoped; model/morphism category and frontier accessors for finite-scoped enriched theories, not V-natural model equivalence |
| Plain Lawvere models ↔ finite `Type` enriched models | ✅ closed scoped category equivalence; ordinary product-preserving models and finite `Type`-enriched models transport through `ForgetEnrichment` with functors, both round-trip natural isomorphisms, `finiteTypeModelBridgeEquivalence`, and fully-faithful / `IsEquivalence` projections |
| Enriched monad/finitary supplied-law frontier | ✅ closed scoped; frontier accessors for supplied unit/multiplication naturality, monad, finitary, Type-specialisation laws, and ordinary monad payloads |
| Power raw theory/monad data accessors | ✅ closed scoped; frontier forwards supplied `TheoryMonadData` and `MonadTheoryData` payloads, not a construction of Power 1999 |
| Plain Lawvere → `Type` enriched Lawvere | ✅ closed with supplied conical-products hypothesis; finite products alone are not enough |
| GUT-B successor-structural coherence | ✅ closed for successor splits |
| GUT-B layerwise (any Fintype δ) | ✅ closed (2026-05-16) |
| GUT-B algebraic-class (any Field k, ring-iso assumed) | ✅ closed (2026-05-16); successor and supplied all-split packages closed (2026-05-19) |
| GUT-B algebraic-class (finite-field G11 cut-1) | ✅ scoped cut-1 closed; `FullGUTG11Frontier.current_g11_closure` bundles canonical finite fields, prime fields, structure-gated arbitrary field satisfiers, odd-prime discriminant classification, and the scoped odd-prime finite-Hilbert operator/object-action boundaries; arbitrary raw non-canonical satisfier synthesis remains open |
| GUT-B over infinite fields (ℝ/ℂ/ℚ_p) | ⏳ deferred to GUT-C |
| GUT-C (non-algebraic δ realisation) | ⏳ open (research-level) |
| Bundled HeytAlg CCC / FdHilb / full Frm semantics | ⏳ open; Heyting posetal currying, strong HeytAlg evaluation obstruction, and concrete `Frm` braided/symmetric/tensor-bilinear boundary closed |
| Power/enriched all-semantics | ⏳ open; scoped enriched bridges, finite Type-enriched Lawvere/model APIs with the ordinary/finite-enriched model category equivalence, Type/Type cotensor, weighted-limit bridge accessors, and supplied-law/raw-Power frontier packages are closed |
| Raw-core all-split coherent T5 | ⏳ open; split-coherent satisfiers closed |
| D6 exhaustiveness | ⏳ open |
| Metalogic identification (D1 = lfp(Φ)) | ✅ closed (2026-05-17) — see `lawvere-identification.md` v0.4 |
