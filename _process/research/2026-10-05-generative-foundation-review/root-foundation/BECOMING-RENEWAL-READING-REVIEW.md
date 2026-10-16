<a id="关系读法与依存动态的独立审查--independent-review-of-the-relational-reading-and-dependence-dynamics"></a>
# Independent review of the relational reading and dependence dynamics

> Some passages exist only in the [Chinese edition](BECOMING-RENEWAL-READING-REVIEW.zh.md): 224 passages in 30 sections, mainly “6. 须作的更正（未执行）”; “0. 范围与方法”; “2.6 被省略的对手读法（乙）”; “Independent review of the relational reading and dependence dynamics”; “2.5 共同参与过粗：连通来自条件清单（乙；对“由展开给出”为丙）”.

## English summary

**Verdicts.**

- **(A) Philosophical warrant of the relational reading: not established, and overstated in the study.** Both readings are acceptable only as *disclosed, stipulated explications* of one aspect of 生生: not undermining the conditions others depend on. Neither earns the identification with 生生. The exclusion of consumers' activity is an input of the definition, not a "conclusion" (study §4, response 3). Ren's direction supports excluding degeneration. It does not supply the unit of classification (a whole formation, or a whole event) or the specific predicates, and these carry most of the verdicts.
- **(B) `Becoming.Dependence`: mathematics accepted; three prose claims rejected as stated.** The rejected claims are: (1) "three ways through a loss" as an exhaustive or exclusive division; (2) "the issue is decided by later relations"; (3) `Dip` as a divergence between the two `living` readings. `loss_does_not_decide` is a valid but engineered witness, and its "same broken dependence" relies on the disclosed start-of-step convention for two of its three runs. The "formal instance of relational unity and differentiation" claim needs narrowing.
- **(C) Formal check: accepted.** The core recompiles from Lean's prelude with exit code 0. The current source hashes of all 22 modules match the receipt, and all 70 audited declarations, plus all 20 probe theorems, have empty axiom reports.
- **(D) Correspondence: corrections required.** Twenty corrections are listed in §6; none has been applied.

**Main findings (probes Q1–Q13, all axiom-free).**

1. *Unit of classification.* Both readings classify formations or formation-events, so any participation in a failing condition voids `living`. This conflicts with chapter §1 ("one activity can make a continuation actual while destroying another condition"). It also conflicts with the repository's own note that one occurrence can take part in both relations. On the whole-run reading, a later breaker condemns an earlier drawer that stayed within renewal, because `draws` is static (Q11).
2. *No generation.* An active formation that participates in nothing is `living` on both readings (Q3). Neither reading represents "further generation", "more", possibility or diversity, all of which are in Ren's wording of 生生.
3. *Stepwise pathologies.* These are undisclosed. The broken formation's own event at the breaking step is not living stepwise, although it is living on the whole-run reading (Q1). A never-met requirement of an inactive formation voids every participant at every step under both readings, with no change and no break (Q2). The cause is that `Consumed` does not require the dependence ever to have been met, contrary to its docstring. A draw-restricted stepwise variant keeps both published divergences and removes both pathologies (Q12).
4. *Connection is free.* For every web, adding a condition that everyone requires at need 0 leaves `living` unchanged and makes the whole connected (Q4). Co-requirement with no interaction already counts as `related` (Q5). Valuing *any* drawer transmits to every living dependent of the same condition, without consumption (Q5). A coarse common condition, such as the study's "biosphere, climate", empties `living` (Q10). Connection and non-vacuity therefore pull in opposite directions, and the ethical content sits on N_rel *and* on the unconstrained inventory of conditions.
5. *Three ways.* No theorem states exhaustiveness or exclusivity. Restoration (a fact about the condition) co-occurs with both ending and transformation (facts about the formation) (Q8). `continuing_restores` and `consumed_continues_transformed` are the contrapositive of `Dependent` for an arbitrary bound; the loss and `T` play no role (Q6). In `Crossing`, the issue is chosen by the move that constitutes the break (`fall m`). Under an end-of-step convention only the restoring run breaks anything (Q7). Whether a history is "transformation" or "ending plus a new formation" is fixed by the stipulated identity of formations in `F` (Q13).
6. *Run-relativity.* `Conditions.valuation K r` depends on the run, as `class_belongs_to_the_run` itself shows. The frame-level `living : C → Prop` used by `Novel`, `G0`, `Comparison` and `universal_reason` is run-independent. The claim that "the Becoming layer supplies `living` and `related`" therefore holds only for the one-run characterization `significant_iff_of_common`.
7. *Omitted rivals.* The study omits several serious rival readings: relation-level (aspect) readings; whole-direction readings (Ren's own phrase); counterfactual or difference-making readings; capability readings; autopoietic or metabolic readings, on which drawing down conditions is constitutive of living; and thermodynamic readings, on which the whole-run reading over an infinite run is empty in a run-down universe. The whole-run reading is also not decidable from any finite history.

---

<a id="0-范围与方法"></a>

<a id="1-总评"></a>

<!-- zh-only table: see BECOMING-RENEWAL-READING-REVIEW.zh.md -->

---

<a id="2-问题-a关系读法的哲学根据"></a>

```lean
-- 整段读法（Becoming.Metaethics, Conditions.valuation）
living e := (K.along r).active e.2 e.1 ∧ ¬ ConsumingIn (K.along r) e.1
related e e' := ∃ c, Participates (K.along r) e.1 c ∧ Participates (K.along r) e'.1 c

-- 逐步读法（Becoming.Dependence, Web.RenewingAt；Web.valuation 取 living e := W.RenewingAt e.2 e.1）
def RenewingAt (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∀ c, W.Participates t f c → ∀ g, W.requires t g c → W.Kept t g c
```

<a id="21-排除消耗者是读法的输入不是结论乙对研究措辞为丙"></a>

<a id="22-分类单位是形成或事件不是关系乙"></a>

<a id="23-读法里没有继续生成乙"></a>

Ren’s answer on ethical quality (verbatim; the surrounding section 2.3 is in the Chinese edition):

> 一种整体的，不断创造更多生的方向，而这个方向产生的可能性，多样性越高，复杂性/复杂结构的复杂度可以不断的上升，就是一个好的方向

<a id="24-逐步读法的两处未披露病理丁对读法可用为乙"></a>

<a id="25-共同参与过粗连通来自条件清单乙对由展开给出为丙"></a>

<a id="26-被省略的对手读法乙"></a>

<a id="27-公开的对应选择是否正当乙甲"></a>

   - “a dynamic source for `living` and `related` is now given”（metaethical-core-characterization 的 `next_delta`）；

<a id="28-最强反驳与会改变判断的结果"></a>

---

<a id="3-问题-bbecomingdependence"></a>

<a id="31-三条去路不是一个划分丙"></a>

- `continuing_restores`、`consumed_continues_transformed`、`consumed_ends_when_fixed`；

<a id="32-两条一般定理是-dependent-的逆否丙dependent-是承重的对应前提"></a>

```lean
theorem continuing_restores (dependent : W.Dependent) {T t : Nat} {g : F} {c : C}
    (active : W.active t g) (depends : W.requires t g c)
    (unchanged : W.need T g c ≤ W.need t g c) : W.need T g c ≤ W.level t c :=
  Nat.le_trans unchanged (dependent t g active c depends)
```

<a id="33-loss_does_not_decide存在性见证去路在断裂之步就由动作选定丙"></a>

```lean
def process : Process State Move where
  step s a t := match a with
    | .rest => t = s
    | .fall m => s.first = 1 ∧ t = ⟨0, m⟩
    | .renew => s.mode = .dormant ∧ t = ⟨1, .onFirst⟩
```

- 记录 `limitations`：“which issue occurs is decided by later relations”。

<a id="34-一步约定承载同一个断裂乙已披露但没有在承重处说明"></a>

<a id="35-consumed-不要求依存曾被满足丁"></a>

```lean
/-- A dependence holding at some step is never met again afterwards. -/
def Consumed (c : C) : Prop :=
  ∃ g T, W.requires T g c ∧ ∀ t, T < t → W.level t c < W.need T g c
```

<a id="36-两个方向都有分歧方向准确dip-不在其中丙另有一种未披露的分歧丁"></a>

- 记录 becoming-stepwise-reading 的 `claim`：“and a formation can be within renewal at each of its own active steps without renewing in the run”；

<a id="37-时间步引理与静态复原无问题"></a>

<a id="38-关系整体与分化的形式实例须收窄丙甲"></a>

---

<a id="4-问题-c形式复核"></a>

<a id="41-独立重新编译"></a>

```text
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 -o X.olean X.lean
  GenerativeCore        exit 0
  Becoming/Frame        exit 0
  InquirySufficiency    exit 0
  Becoming/Inquiry      exit 0
  RelationalRenewal     exit 0
  Becoming/Renewal      exit 0
  Becoming/Dependence   exit 0
  Becoming/Metaethics   exit 0
```

<a id="42-哈希"></a>

<!-- zh-only table: see BECOMING-RENEWAL-READING-REVIEW.zh.md -->

<a id="43-公理依赖"></a>

- Dependence 29 项；

<a id="44-探针"></a>

<!-- zh-only table: see BECOMING-RENEWAL-READING-REVIEW.zh.md -->

---

<a id="5-问题-d对应与超出汇总"></a>

| 位置 | 表述 |
|---|---|
| 研究 §4 反驳 3 回应 | 排除消耗者“是结论的要点” |
| 研究 §2、English summary；章节 §6.3；记录 becoming-renewal-reading `claim`；`consumption_relates` 说明 | “消耗本身是一种已形成的关系” |
| 章节 §0 前提卡“连通”行；§6.3；`significant_iff_of_common` 说明 | 连通“由展开给出，不再假设” |
| 章节 §0 前提卡“`living` 的读法”行 | 只列 `Conditions.valuation` |
| `Becoming.Metaethics` 模块说明第 9–12 行 | `related` 是 “nonzero formed relation (conditioning, dependence, descent, cooperation)”；`living` 对应 “renewing formation” |
| 章节 §6.3；metaethical-core-characterization `next_delta` | Becoming 层给出 `living` 与 `related` |
| `Dependence` 模块说明；记录 becoming-dependence-dynamics 标题与 `claim`；章节 §1；研究 §6.2 | “三条去路” |
| 研究 §6.4 反驳 1；记录 `limitations` | 去路“由后续关系决定” |
| `loss_does_not_decide` 说明；章节 §1；研究 §6.2 | “同一个断裂” |
| 模块说明结果列表；研究 §6.2 表；章节 §1 英文；研究 English summary | 三条一般定理没有写出 `Dependent` |
| `Web.Consumed`、`RelationalRenewal.Consumed` 的说明 | “never met again”“loses its support” |
| 模块说明；记录 becoming-stepwise-reading `claim` 与 `counterexamples[0]`；章节 §2 | 把 `Dip` 列为两种读法的分歧 |
| 研究 §6.4、§6.5；记录 becoming-stepwise-reading | 逐步读法唯一披露的严格性是季节性下降 |
| `Web.valuing_breaking_reaches` 说明（“values a breaking event”）；章节 §6.3“断裂本身是一种关系” | 暗示该事件造成了断裂 |
| 研究 §6.2 解读；记录 becoming-dependence-dynamics `related[2]` | “关系整体与分化的形式实例” |
| 研究 §2 L4 表 | 把 `living_iff_relational` 列在 `Becoming.Metaethics` 下 |
| 章节 §8 表 | “逐步读法：已完成” |

---

<a id="6-须作的更正未执行"></a>

---

<a id="7-仍然成立的部分"></a>

<a id="8-审查者自身的边界"></a>

- 本次没有新读任何外部文献。Maturana 与 Varela、Jonas、Thompson、Moreno 与 Mossio、Sen、Nussbaum、Lewis、Woodward、Schrödinger、Nicolis 与 Prigogine、Gunderson 与 Holling，都依据先前知识，细节须核对原文。

---

<a id="附录探针源码-reviewprobeslean"></a>

```lean
import Becoming.Metaethics

/-!
Review probes for the relational reading and `Becoming.Dependence`.
Independent reviewer's scratch file; imports the unmodified core.
-/

namespace ReviewProbes

open Generative Becoming RelationalRenewal

/-! ## Q1. The broken formation's own event at the breaking step

In the escalating run the sustaining formation is active at step 1 and its own
dependence is broken across that step. The whole-run reading counts this event
living; the stepwise reading does not. -/
theorem victim_not_living_stepwise {Pos : Type} (own sig : Pos → Commons.Formation × Nat → Prop) :
    Commons.conditions.active (Commons.escalating.state 1) .sustaining ∧
    (Commons.conditions.dependence.along Commons.escalating).Broken 1 .sustaining () ∧
    (Commons.conditions.valuation Commons.escalating own sig).living (.sustaining, 1) ∧
    ¬ ((Commons.conditions.dependence.along Commons.escalating).valuation own sig).living
      (.sustaining, 1) := by
  refine ⟨Nat.le_refl 1, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨Nat.le_refl 1, fun ⟨_, drawn, _⟩ => drawn⟩, fun ⟨_, keeps⟩ => ?_⟩
  exact Nat.not_succ_le_zero 0 (keeps () (Or.inl trivial) .sustaining trivial).2

/-! ## Q2. An unmet requirement condemns a drawer under both readings, with no change

`true` requires the condition at a level never available and is never active;
`false` draws on it and is active throughout. Levels never change and no dependence
is ever broken, yet neither reading counts any event of `false` living. -/
namespace Unmet

def conditions : Conditions Unit Bool Unit where
  level _ _ := 0
  active _ f := match f with
    | true => False
    | false => True
  requires f _ := match f with
    | true => True
    | false => False
  need f _ := match f with
    | true => 1
    | false => 0
  draws f _ := match f with
    | true => False
    | false => True

theorem no_break : ∀ t g, ¬ (conditions.dependence.along Separate.still).Broken t g ()
  | _, true, ⟨_, met, _⟩ => Nat.not_succ_le_zero 0 met
  | _, false, ⟨req, _, _⟩ => req

theorem dependent : RelationalRenewal.Dependent (conditions.along Separate.still)
  | _, true, act, _, _ => act.elim
  | _, false, _, _, req => req.elim

theorem poisons_both {Pos : Type} (own sig : Pos → Bool × Nat → Prop) :
    (∀ t, ¬ (conditions.valuation Separate.still own sig).living (false, t)) ∧
    (∀ t, ¬ ((conditions.dependence.along Separate.still).valuation own sig).living (false, t)) :=
  ⟨fun _ ⟨_, notConsuming⟩ =>
      notConsuming ⟨(), trivial, true, 0, trivial, fun _ _ => Nat.zero_lt_one⟩,
   fun _ ⟨_, keeps⟩ => Nat.not_succ_le_zero 0 (keeps () (Or.inr trivial) true trivial).1⟩

end Unmet

/-! ## Q3. An active formation participating in nothing is living on both readings

Neither reading contains any component of further generation. -/
def inert : Conditions Unit Unit Unit :=
  ⟨fun _ _ => 0, fun _ _ => True, fun _ _ => False, fun _ _ => 0, fun _ _ => False⟩

theorem inert_living {Pos : Type} (own sig : Pos → Unit × Nat → Prop) (t : Nat) :
    (inert.valuation Separate.still own sig).living ((), t) ∧
    ((inert.dependence.along Separate.still).valuation own sig).living ((), t) :=
  ⟨⟨trivial, fun ⟨_, drawn, _⟩ => drawn⟩, ⟨trivial, fun _ joins => (joins.elim id id).elim⟩⟩

/-! ## Q4. Connection is free: adjoin a condition every formation requires at need 0

The stepwise `living` is unchanged and the whole becomes connected, for every web. -/
def withCommon {F C : Type} (W : Web F C) : Web F (Option C) where
  level t c := match c with
    | none => 0
    | some c => W.level t c
  active := W.active
  requires t f c := match c with
    | none => True
    | some c => W.requires t f c
  need t f c := match c with
    | none => 0
    | some c => W.need t f c
  draws t f c := match c with
    | none => False
    | some c => W.draws t f c

theorem withCommon_living {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop)
    (e : F × Nat) :
    ((withCommon W).valuation own sig).living e ↔ (W.valuation own sig).living e :=
  ⟨fun ⟨act, keeps⟩ => ⟨act, fun c joins g dep => keeps (some c) joins g dep⟩,
   fun ⟨act, keeps⟩ => ⟨act, fun c => match c with
     | none => fun _ _ _ => ⟨Nat.le_refl 0, Nat.le_refl 0⟩
     | some c => fun joins g dep => keeps c joins g dep⟩⟩

theorem withCommon_connected {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop) :
    ((withCommon W).valuation own sig).Connected :=
  Web.connected_of_common (withCommon W) own sig none (fun _ _ => Or.inl trivial)

/-! The same for the whole-run reading on `Conditions`. -/
def Conditions.withCommon {S F C : Type} (K : Conditions S F C) : Conditions S F (Option C) where
  level s c := match c with
    | none => 0
    | some c => K.level s c
  active := K.active
  requires f c := match c with
    | none => True
    | some c => K.requires f c
  need f c := match c with
    | none => 0
    | some c => K.need f c
  draws f c := match c with
    | none => False
    | some c => K.draws f c

theorem conditions_withCommon_living {S A F C Pos : Type} {P : Process S A}
    (K : Conditions S F C) (r : Run P) (own sig : Pos → F × Nat → Prop) (e : F × Nat) :
    ((Conditions.withCommon K).valuation r own sig).living e ↔ (K.valuation r own sig).living e :=
  ⟨fun ⟨act, notConsuming⟩ => ⟨act, fun ⟨c, drawn, consumed⟩ =>
      notConsuming ⟨some c, drawn, consumed⟩⟩,
   fun ⟨act, notConsuming⟩ => ⟨act, fun ⟨c, drawn, consumed⟩ => match c, drawn, consumed with
      | none, drawn, _ => drawn
      | some c, drawn, consumed => notConsuming ⟨c, drawn, consumed⟩⟩⟩

theorem conditions_withCommon_connected {S A F C Pos : Type} {P : Process S A}
    (K : Conditions S F C) (r : Run P) (own sig : Pos → F × Nat → Prop) :
    ((Conditions.withCommon K).valuation r own sig).Connected :=
  Becoming.Conditions.connected_of_common (Conditions.withCommon K) r own sig none
    (fun _ _ => Or.inl trivial)

/-! ## Q5. Valuing any drawer reaches every living dependent of the same condition

No consumption is used: the relation through which N_rel transmits is co-participation. -/
theorem drawing_reaches {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop)
    (transmit : Neutral (K.valuation r own sig).transmits)
    {f g : F} {c : C} (drawn : K.draws f c) (depends : K.requires g c)
    (p : Pos) (t t' : Nat) (held : sig p (f, t))
    (alive : (K.valuation r own sig).living (g, t')) : sig p (g, t') :=
  transmit (p, (f, t), (g, t')) held ⟨c, Or.inr drawn, Or.inl depends⟩ alive

/-- Two formations that only require the same condition are related. -/
theorem co_requirement_relates {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop) {f g : F} {c : C}
    (df : K.requires f c) (dg : K.requires g c) (t t' : Nat) :
    (K.valuation r own sig).related (f, t) (g, t') :=
  ⟨c, Or.inl df, Or.inl dg⟩

/-! ## Q6. `consumed_continues_transformed` uses no loss: any bound will do -/
theorem transformed_any_bound {F C : Type} {W : Web F C} (dependent : W.Dependent)
    {N t : Nat} {g : F} {c : C} (below : W.level t c < N) (active : W.active t g) :
    ¬ (W.requires t g c ∧ N ≤ W.need t g c) :=
  fun ⟨dep, le⟩ => Nat.not_le_of_gt below (Nat.le_trans le (dependent t g active c dep))

example {F C : Type} {W : Web F C} (dependent : W.Dependent) {T : Nat} {g : F} {c : C}
    (below : ∀ t, T < t → W.level t c < W.need T g c) {t : Nat} (later : T < t)
    (active : W.active t g) : ¬ (W.requires t g c ∧ W.need T g c ≤ W.need t g c) :=
  transformed_any_bound dependent (below t later) active

/-! ## Q7. The "same broken dependence" depends on the start-of-step convention

Counting the fall against the dependence as it stands at the end of the step, only
the restoring run of `Crossing` breaks anything; in the ending run, too, the first
dependence dissolves across the step. -/
def BrokenAtEnd {F C : Type} (W : Web F C) (t : Nat) (g : F) (c : C) : Prop :=
  W.requires t g c ∧ W.requires (t + 1) g c ∧ W.need t g c ≤ W.level t c ∧
    W.level (t + 1) c < W.need (t + 1) g c

theorem convention_carries_the_same_break :
    ¬ BrokenAtEnd (Crossing.dependence.along Crossing.ending) 0 () .first ∧
    ¬ BrokenAtEnd (Crossing.dependence.along Crossing.transforming) 0 () .first ∧
    BrokenAtEnd (Crossing.dependence.along Crossing.restoring) 0 () .first ∧
    (Crossing.dependence.along Crossing.ending).Dissolves 0 () .first :=
  ⟨fun ⟨_, later, _⟩ => later, fun ⟨_, later, _⟩ => later,
   ⟨trivial, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, ⟨trivial, id⟩⟩

/-! ## Q8. The three ways are not exclusive issues

After the same break, one formation transforms and another ends, while the condition
returns: restoration of the condition co-occurs with both. -/
namespace Overlap

inductive G where
  | mover
  | stayer

inductive Src where
  | first
  | second

def firstLevel : Nat → Nat
  | 0 => 1
  | 1 => 0
  | _ + 2 => 1

def web : Web G Src where
  level t c := match c with
    | .first => firstLevel t
    | .second => 1
  active t g := match g, t with
    | .mover, _ => True
    | .stayer, 0 => True
    | .stayer, _ + 1 => False
  requires t g c := match g, t, c with
    | .mover, 0, .first => True
    | .mover, 0, .second => False
    | .mover, _ + 1, .first => False
    | .mover, _ + 1, .second => True
    | .stayer, 0, .first => True
    | .stayer, 0, .second => False
    | .stayer, _ + 1, _ => False
  need _ _ _ := 1
  draws _ _ _ := False

theorem overlap :
    web.Dependent ∧ web.Broken 0 .mover .first ∧ web.Broken 0 .stayer .first ∧
    web.Forms 0 .mover .second ∧ (∀ t, web.active t .mover) ∧
    (∀ t, 0 < t → ¬ web.active t .stayer) ∧ ¬ web.Consumed .first := by
  refine ⟨?_, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨id, trivial⟩, fun _ => trivial, ?_, ?_⟩
  · intro t g active c depends
    match g, t, c, active, depends with
    | .mover, 0, .first, _, _ => exact Nat.le_refl 1
    | .mover, 0, .second, _, d => exact d.elim
    | .mover, _ + 1, .first, _, d => exact d.elim
    | .mover, _ + 1, .second, _, _ => exact Nat.le_refl 1
    | .stayer, 0, .first, _, _ => exact Nat.le_refl 1
    | .stayer, 0, .second, _, d => exact d.elim
    | .stayer, _ + 1, _, a, _ => exact a.elim
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · intro ⟨_, T, _, below⟩
    exact Nat.lt_irrefl 1 (below (T + 2) (Nat.lt_of_lt_of_le (Nat.lt_succ_self T) (Nat.le_succ _)))

end Overlap

/-! ## Q9. `Dip` is not a divergence of the two `living` readings

The keeper draws nothing, so the whole-run reading (not consuming) credits its active
events, as the stepwise reading does. -/
theorem dip_keeper_credited_by_both :
    ¬ Dip.web.ConsumingIn .keeper ∧
    (∀ t, Dip.web.active t .keeper → Dip.web.RenewingAt t .keeper) :=
  ⟨fun ⟨_, _, drawn, _⟩ => drawn, Dip.renewing_at_each_step_not_in_run.2.1⟩

/-! ## Q10. A coarse common condition empties `living`

The condition that discharges connection is also the one whose loss voids every
participant. -/
theorem common_consumed_empties {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop) (c₀ : C) (allDraw : ∀ f, K.draws f c₀)
    (consumed : Consumed (K.along r) c₀) : ∀ e, ¬ (K.valuation r own sig).living e :=
  fun e ⟨_, notConsuming⟩ => notConsuming ⟨c₀, allDraw e.1, consumed⟩

theorem common_unkept_empties {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop)
    (c₀ : C) (t : Nat) (allJoin : ∀ f, W.Participates t f c₀) {g : F}
    (dep : W.requires t g c₀) (unkept : ¬ W.Kept t g c₀) :
    ∀ f, ¬ (W.valuation own sig).living (f, t) :=
  fun f ⟨_, keeps⟩ => unkept (keeps c₀ (allJoin f) g dep)

/-! ## Q11. On the whole-run reading a later breaker condemns an earlier drawer

`early` is active only at step 0 and its step keeps the condition; `late` is active
only at step 1, where the condition falls for good. Because `draws` is static, the
whole-run reading counts `early` consuming and withholds its only event. -/
namespace Late

inductive G where
  | early
  | late
  | dependent

def process : Process Nat Unit := ⟨fun s _ t => t = s + 1⟩

def clock : Run process := ⟨fun n => n, fun _ => (), fun _ => rfl⟩

def lvl : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

def conditions : Conditions Nat G Unit where
  level s _ := lvl s
  active s g := match g, s with
    | .early, 0 => True
    | .early, _ + 1 => False
    | .late, 0 => False
    | .late, 1 => True
    | .late, _ + 2 => False
    | .dependent, s => 1 ≤ lvl s
  requires g _ := match g with
    | .early => False
    | .late => False
    | .dependent => True
  need g _ := match g with
    | .early => 0
    | .late => 0
    | .dependent => 1
  draws g _ := match g with
    | .early => True
    | .late => True
    | .dependent => False

theorem early_condemned {Pos : Type} (own sig : Pos → G × Nat → Prop) :
    RelationalRenewal.Dependent (conditions.along clock) ∧
    (∀ t, 0 < t → ¬ conditions.active (clock.state t) .early) ∧
    ((conditions.dependence.along clock).valuation own sig).living (.early, 0) ∧
    ¬ (conditions.valuation clock own sig).living (.early, 0) := by
  refine ⟨?_, ?_, ⟨trivial, fun _ _ g dep => ?_⟩, fun ⟨_, notConsuming⟩ => notConsuming
    ⟨(), trivial, .dependent, 2, trivial, fun | _ + 2, _ => Nat.zero_lt_one⟩⟩
  · intro t f active c depends
    match f, depends with
    | .dependent, _ => exact active
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · match g, dep with
    | .dependent, _ => exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩

end Late

/-! ## Q12. A draw-restricted stepwise variant

An event is credited when it is active and no dependence on a condition it draws on is
broken across its step. It keeps both divergences from the whole-run reading, credits
the broken formation's own event, and is not voided by an unmet requirement. -/
def NotBreakingAt {F C : Type} (W : Web F C) (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∀ c, W.draws t f c → ∀ g, ¬ W.Broken t g c

theorem variant :
    NotBreakingAt (Commons.conditions.dependence.along Commons.escalating) 1 .sustaining ∧
    NotBreakingAt (Commons.conditions.dependence.along Commons.escalating) 0 .focal ∧
    ¬ NotBreakingAt (Commons.conditions.dependence.along Commons.dipping) 0 .focal ∧
    (∀ t, NotBreakingAt (Unmet.conditions.dependence.along Separate.still) t false) := by
  refine ⟨⟨Nat.le_refl 1, fun _ drawn => drawn.elim⟩, ⟨trivial, fun _ _ g broken => ?_⟩,
    fun ⟨_, nb⟩ => nb () trivial .sustaining ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    fun t => ⟨trivial, fun _ _ g => Unmet.no_break t g⟩⟩
  match g, broken with
  | .focal, ⟨req, _, _⟩ => exact req
  | .sustaining, ⟨_, _, fell⟩ => exact Nat.lt_irrefl 1 fell

/-! ## Q13. Ending versus transformation is carried by the index of formations

The transforming run of `Crossing`, re-indexed with two formations, has the same
levels and, at each step, the same active dependences when formations are not named.
Read this way the loss ends one formation while another forms: whether the history is a
"transformation" or an "ending" is fixed by the identity stipulated through `F`. -/
namespace Reindex

def T := Crossing.dependence.along Crossing.transforming

def web : Web Bool Crossing.Source where
  level t c := T.level t c
  active t f := match f, t with
    | true, 0 => True
    | true, _ + 1 => False
    | false, 0 => False
    | false, _ + 1 => True
  requires t f c := match f, t, c with
    | true, 0, .first => True
    | true, 0, .second => False
    | true, _ + 1, _ => False
    | false, 0, _ => False
    | false, _ + 1, .first => False
    | false, _ + 1, .second => True
  need _ _ _ := 1
  draws _ _ _ := False

theorem ends_and_forms :
    web.Dependent ∧ web.Lost .first ∧ (∀ t, 0 < t → ¬ web.active t true) ∧
    (∀ t, 0 < t → web.active t false) ∧ web.Forms 0 false .second ∧
    (∀ t, (∃ f, web.active t f) ↔ T.active t ()) ∧
    (∀ t c, (∃ f, web.active t f ∧ web.requires t f c) ↔ (T.active t () ∧ T.requires t () c)) := by
  refine ⟨?_, ⟨true, 0, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
      fun | _ + 1, _ => Nat.zero_lt_one⟩, ?_, ?_, ⟨id, trivial⟩, ?_, ?_⟩
  · intro t f active c depends
    match f, t, c, active, depends with
    | true, 0, .first, _, _ => exact Nat.le_refl 1
    | true, 0, .second, _, d => exact d.elim
    | true, _ + 1, _, a, _ => exact a.elim
    | false, 0, _, a, _ => exact a.elim
    | false, _ + 1, .first, _, d => exact d.elim
    | false, _ + 1, .second, _, _ => exact Nat.le_refl 1
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · intro t later
    match t, later with
    | _ + 1, _ => exact trivial
  · intro t
    match t with
    | 0 => exact ⟨fun _ => trivial, fun _ => ⟨true, trivial⟩⟩
    | _ + 1 => exact ⟨fun _ => trivial, fun _ => ⟨false, trivial⟩⟩
  · intro t c
    match t, c with
    | 0, .first => exact ⟨fun _ => ⟨trivial, trivial⟩, fun _ => ⟨true, trivial, trivial⟩⟩
    | 0, .second => exact ⟨fun ⟨f, a, d⟩ => match f, a, d with
        | true, _, d => d.elim
        | false, a, _ => a.elim, fun ⟨_, d⟩ => d.elim⟩
    | _ + 1, .first => exact ⟨fun ⟨f, a, d⟩ => match f, a, d with
        | true, a, _ => a.elim
        | false, _, d => d.elim, fun ⟨_, d⟩ => d.elim⟩
    | _ + 1, .second => exact ⟨fun _ => ⟨trivial, trivial⟩, fun _ => ⟨false, trivial, trivial⟩⟩

end Reindex

end ReviewProbes
```


## Ren’s words quoted in passages that exist only in the Chinese edition

The paragraphs below sit in Chinese-only passages of this study log ([Chinese edition](BECOMING-RENEWAL-READING-REVIEW.zh.md)). Only the quotation is repeated here, verbatim and in Ren’s original language, with the source link given in the passage (line numbers refer to the bilingual file before the split); the surrounding AI prose is in the Chinese edition. Nothing here is translated.

- Line 82, section “2.1 排除消耗者是读法的输入，不是结论（乙；对研究措辞为丙）”: “用关系结构把两种形成分开” “不overlap” ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md))
