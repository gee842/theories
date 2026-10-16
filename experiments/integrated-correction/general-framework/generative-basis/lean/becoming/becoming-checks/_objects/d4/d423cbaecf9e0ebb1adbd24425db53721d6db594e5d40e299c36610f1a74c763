import Becoming
import GenerativeComparison
import PositionedPositiveReason
import PracticalJudgment
import RenewalComparison
import JointContinuationClassification
import WholeGroundCoverage
import CutCoverageAudit
import EvaluatorGrounding
import PracticalReach
import StandardsBridge
import CorrectionInfrastructure

/-!
# Existing interfaces as instances of the spine

Generic ethics modules are polymorphic over small interfaces. This module gives
each interface from the spine, or proves that a module's own combinator is the
spine's, so their theorems apply to one unfolding without copying them. The core
imports none of these modules; the dependency runs from them to the core.

* The core's G0, C, secured positive ground and positioned articulation D are, by
  definition, those of `GenerativeComparison` and `PositionedPositiveReason` on the
  frame's inventory; the relational reading of `living` is `RenewalComparison`'s, and
  so is the whole-run reading of courses in `Becoming.Ranking`, with the same
  undisturbed levels.
  J1/J2 on configurations, `BetterAt`, is `PracticalJudgment.Better`.
* Seed–edge closures (`WholeGroundCoverage.Reached`, `CutCoverageAudit.Reach`)
  and finite chains (`EvaluatorGrounding.Chain`) are reachability on the process
  whose steps are the edges. The core's closure under a relation (`WithinClosure`,
  `Becoming.Feedback`) is the seed–edge closure from one seed.
* Joint-continuation spaces are the configurations reachable in a frame; their
  faithful transports are the core's `trace_map` and `trace_lift`.
* `PracticalJudgment.Robust` is `CommonResponse`; `PracticalReach.Guarantees` is
  one-step `Completes`; `StandardsBridge.revise` is `After` on a pure
  observation; `CorrectionInfrastructure.LiveStep` is `Enabled`.
* `GenerativeComparison.Situation` realizes each option functionally. On a frame
  a response may have several outcomes, so comparing responses needs the lifting
  rule L. The functional articulation is exactly the deterministic case of the
  lifted one, and the lifted comparison, reason and selection results hold for
  every frame. Two countermodels show that the choice of lifting rule is
  substantive and that transitivity needs a live middle response.
* Under the axiom of `Becoming.Significance`, `GenerativeComparison.G0` holds for
  every inventory with positive relevance read from significance, which on a frame's
  inventory is the core's `Frame.relevance`. The periphery's theorems taking G0 as a
  hypothesis for an arbitrary positive relevance follow from the axiom with it: a new
  realization of a generative extension, contingent generation, and the universal
  address of positioned articulation with D read on it.

Direction conventions differ and are kept: in `GenerativeComparison`,
`Better first second` says the second is better; in `PracticalJudgment` and
`LiftBetter`, `better x y` says `x` is better. Every declaration has an empty
axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v w

/-! ## Seed–edge closures are reachability -/

/-- A one-label process whose steps are the given edges. -/
def edgeProcess {X : Type u} (edge : X → X → Prop) : Process X Unit :=
  ⟨fun x _ y => edge x y⟩

/-- Everything reached from a seed along edges. -/
def Closure {X : Type u} (seed : X → Prop) (edge : X → X → Prop) (x : X) : Prop :=
  ∃ p, seed p ∧ Reach (edgeProcess edge) p x

namespace Closure

variable {X : Type u} {seed : X → Prop} {edge : X → X → Prop}

theorem base {x : X} (held : seed x) : Closure seed edge x :=
  ⟨x, held, Reach.refl _ _⟩

theorem step {x y : X} : Closure seed edge x → edge x y → Closure seed edge y
  | ⟨p, held, path⟩, e => ⟨p, held, path.trans (Reach.of_step (a := ()) e)⟩

/-- Any property holding at seeds and preserved along edges holds on the closure. -/
theorem induction {motive : X → Prop} (start : ∀ x, seed x → motive x)
    (carry : ∀ x y, motive x → edge x y → motive y) {x : X} :
    Closure seed edge x → motive x
  | ⟨p, held, path⟩ =>
    Invariant.reach (P := edgeProcess edge) (fun x _ y e m => carry x y m e) path (start p held)

end Closure

theorem reached_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    WholeGroundCoverage.Reached seed edge x ↔ Closure seed edge x := by
  constructor
  · intro h
    induction h with
    | seed held => exact Closure.base held
    | step _ e ih => exact ih.step e
  · exact Closure.induction (fun _ held => .seed held) (fun _ _ r e => .step r e)

theorem cutReach_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    UniversalEthics.CutCoverageAudit.Reach seed edge x ↔ Closure seed edge x := by
  constructor
  · intro h
    induction h with
    | root held => exact Closure.base held
    | step _ e ih => exact ih.step e
  · exact Closure.induction (fun _ held => .root held) (fun _ _ r e => .step r e)

/-- The core's closure under a relation, what lies in every region closed under it that holds a
formation (`Becoming.Feedback`), is the seed–edge closure from that formation alone. -/
theorem withinClosure_iff_closure {X : Type} {rel : X → X → Prop} {f g : X} :
    WithinClosure rel f g ↔ Closure (fun x => x = f) rel g :=
  ⟨fun within => within (Closure (fun x => x = f) rel) (fun _ _ held e => held.step e)
      (Closure.base rfl),
   Closure.induction (motive := WithinClosure rel f)
      (fun x (same : x = f) => same.symm ▸ WithinClosure.refl f)
      (fun _ _ within e => within.trans (WithinClosure.of_rel e))⟩

theorem chain_iff_reach {X : Type} {step : X → X → Prop} {p q : X} :
    EvaluatorGrounding.Chain step p q ↔ Reach (edgeProcess step) p q := by
  constructor
  · intro h
    induction h with
    | refl => exact Reach.refl _ _
    | tail _ last ih => exact ih.trans (Reach.of_step (a := ()) last)
  · intro path
    exact Invariant.reach (P := edgeProcess step) (I := EvaluatorGrounding.Chain step p)
      (fun _ _ _ e c => .tail c e) path (.refl p)

/-! ## Continuations of a frame -/

section Continuations

variable {S : Type u} {A : Type v} {C : Type w}

/-- The joint-continuation space of a frame from a root: reachable configurations
with their realized claims. -/
def Frame.continuations (F : Frame S A C) (root : S) :
    JointContinuationClassification.Continuations S C :=
  ⟨Reach F.P root, F.realized⟩

/-- A step- and claim-preserving map carries every jointly realizable bundle. -/
theorem Frame.map_preserves_bundles {S' : Type u} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (step : ∀ s a t, F.P.step s a t → G.P.step (q s) a (q t))
    (claim : ∀ s c, F.realized s c → G.realized (q s) c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (F.continuations root) (G.continuations (q root)) :=
  JointContinuationClassification.faithful_history_transport_preserves_joint_bundles q
    (fun _ reached => reached.map step) (fun s c _ held => claim s c held)

/-- A summary whose steps lift and whose claims reflect loses no bundle. -/
theorem Frame.lift_reflects_bundles {S' : Type u} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (lift : ∀ s a r, G.P.step (q s) a r → ∃ t, F.P.step s a t ∧ q t = r)
    (claim : ∀ s c, G.realized (q s) c → F.realized s c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (G.continuations (q root)) (F.continuations root)
  | _, ⟨_, reached, all⟩ => match Reach.lift lift reached with
    | ⟨t, path, same⟩ => ⟨t, path, fun c held => claim t c (same ▸ all c held)⟩

/-! ## Robust responses, guarantees, evidence narrowing and live steps -/

/-- A common response is a robust response whose admissibility is completion. -/
theorem commonResponse_is_robust {S R : Type} {A : Type v} (P : Process S A)
    (safe : S → A → S → Prop) (goal : S → Prop) (response : R → List A)
    (B : S → Prop) (r : R) :
    CommonResponse P safe goal response B r ↔
      PracticalJudgment.Robust B (fun s r => Completes P safe goal s (response r)) r :=
  Iff.rfl

/-- Every robust response is a common response of the judgment process. -/
theorem robust_iff_commonResponse {W H : Type} (live : W → Prop) (admissible : W → H → Prop)
    (a : H) :
    PracticalJudgment.Robust live admissible a ↔
      CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees live) a :=
  commonResponse_judge_iff.symm

/-- A guarantee is one-step completion. -/
theorem guarantees_iff_completes {S A : Type} (P : Process S A) (s : S) (a : A)
    (goal : S → Prop) :
    PracticalReach.Guarantees (fun a t => P.step s a t) a goal ↔
      Completes P (fun _ _ _ => True) goal s [a] :=
  ⟨fun ⟨live, all⟩ => ⟨live, fun t step => ⟨trivial, all t step⟩⟩,
   fun ⟨live, all⟩ => ⟨live, fun t step => (all t step).2⟩⟩

theorem liveStep_iff_enabled {S A : Type} (step : S → A → S → Prop) (s : S) (a : A) :
    CorrectionInfrastructure.LiveStep step s a ↔ Enabled (⟨step⟩ : Process S A) s a :=
  Iff.rfl

/-- A pure observation: the configuration is unchanged and the outcome is read. -/
def observe {Q : Type v} : Process S Q :=
  ⟨fun s _ t => t = s⟩

theorem after_observe_iff {Q : Type v} {k : Nat} (obs : S → Q → Fin k)
    (B : S → Prop) (q : Q) (o : Fin k) (t : S) :
    After observe (fun s q _ => obs s q) B q o t ↔ B t ∧ obs t q = o :=
  ⟨fun ⟨_, believed, same, read⟩ => by cases same; exact ⟨believed, read⟩,
   fun ⟨believed, read⟩ => ⟨t, believed, rfl, read⟩⟩

/-- Booleans as two observation outcomes, written without numeric literals. -/
def encode : Bool → Fin 2
  | false => ⟨0, Nat.zero_lt_succ 1⟩
  | true => ⟨1, Nat.succ_lt_succ (Nat.zero_lt_succ 0)⟩

theorem encode_inj : ∀ {a b : Bool}, encode a = encode b → a = b
  | false, false, _ => rfl
  | true, true, _ => rfl
  | false, true, h => Nat.noConfusion (congrArg Fin.val h)
  | true, false, h => Nat.noConfusion (congrArg Fin.val h)

theorem mem_filter {α : Type} (p : α → Bool) (x : α) :
    ∀ l : List α, x ∈ l.filter p ↔ x ∈ l ∧ p x = true
  | [] => ⟨fun h => (nomatch h), fun ⟨h, _⟩ => (nomatch h)⟩
  | a :: l => by
    have ih := mem_filter p x l
    unfold List.filter
    cases hp : p a with
    | true =>
      refine ⟨fun h => ?_, fun ⟨m, px⟩ => ?_⟩
      · cases h with
        | head => exact ⟨.head _, hp⟩
        | tail _ h => exact ⟨.tail _ (ih.mp h).1, (ih.mp h).2⟩
      · cases m with
        | head => exact .head _
        | tail _ m => exact .tail _ (ih.mpr ⟨m, px⟩)
    | false =>
      refine ⟨fun h => ⟨.tail _ (ih.mp h).1, (ih.mp h).2⟩, fun ⟨m, px⟩ => ?_⟩
      cases m with
      | head => exact absurd (hp.symm.trans px) Bool.false_ne_true
      | tail _ m => exact ih.mpr ⟨m, px⟩

theorem beq_true_iff : ∀ x b : Bool, (x == b) = true ↔ x = b
  | false, false => ⟨fun _ => rfl, fun _ => rfl⟩
  | true, true => ⟨fun _ => rfl, fun _ => rfl⟩
  | false, true => ⟨fun h => (nomatch h), fun h => (nomatch h)⟩
  | true, false => ⟨fun h => (nomatch h), fun h => (nomatch h)⟩

/-- Revising a list of rules by one observation is `After` on a pure observation. -/
theorem revise_is_after {Q : Type} (hs : List (StandardsBridge.Rule Q)) (q : Q) (b : Bool)
    (h : StandardsBridge.Rule Q) :
    h ∈ StandardsBridge.revise hs (q, b) ↔
      After observe (fun (g : StandardsBridge.Rule Q) q _ => encode (g q)) (· ∈ hs) q
        (encode b) h :=
  (mem_filter _ h hs).trans <|
    (Iff.intro (fun ⟨m, e⟩ => ⟨m, congrArg encode ((beq_true_iff _ _).mp e)⟩)
      (fun ⟨m, e⟩ => ⟨m, (beq_true_iff _ _).mpr (encode_inj e)⟩)).trans
    (after_observe_iff (fun (g : StandardsBridge.Rule Q) q => encode (g q)) _ q _ h).symm

end Continuations

/-! ## The core's definitions are those of the existing modules -/

section Definitions

variable {S A C Pos : Type}

/-- The frame's configurations as an inventory under a reading. -/
def Frame.inventory (F : Frame S A C) (reading : C → Prop) : GenerativeComparison.Inventory S C :=
  ⟨F.realized, reading⟩

theorem g0_iff (F : Frame S A C) (living : C → Prop) (positive : S → C → Prop) :
    G0 F living positive ↔ GenerativeComparison.G0 (F.inventory living) positive :=
  Iff.rfl

theorem extension_iff (F : Frame S A C) (living : C → Prop) (s t : S) :
    Extension F living s t ↔ GenerativeComparison.GenerativeExtension (F.inventory living) s t :=
  Iff.rfl

theorem comparison_iff (F : Frame S A C) (living : C → Prop) (Better : S → S → Prop) :
    Comparison F living Better ↔
      GenerativeComparison.ComparisonPrinciple (F.inventory living) Better :=
  Iff.rfl

theorem securesPositiveGround_iff {H R : Type} (admitted : R → H → Prop)
    (before : H → C → Prop) (positive : H → C → Prop) (r : R) :
    SecuresPositiveGround admitted before positive r ↔
      PositionedPositiveReason.SecuresPositiveGround admitted before positive r :=
  Iff.rfl

theorem positionedArticulation_iff {H R : Type} (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → C → Prop) (positive : H → C → Prop)
    (Reason : Pos → R → Prop) :
    PositionedArticulation access admitted before positive Reason ↔
      PositionedPositiveReason.PositionedArticulation access admitted before positive Reason :=
  Iff.rfl

/-- J1/J2 on configurations: basic conditions first, then living gains. -/
def BetterAt (F : Frame S A C) (basic living : C → Prop) : S → S → Prop :=
  PracticalJudgment.Better (fun s c => basic c ∧ F.realized s c)
    (fun s c => living c ∧ F.realized s c)

/-- The spine's `living` is the recorded relational reading. -/
theorem Conditions.living_iff_relational {F Cond : Type} {P : Process S A}
    (K : Conditions S F Cond) (r : Run P) (own sig : Pos → F × Nat → Prop) (e : F × Nat) :
    (K.valuation r own sig).living e ↔
      (RenewalComparison.relationalInventory (fun _ : Unit => K.along r)).realized () e :=
  Iff.rfl

/-- The core's whole-run reading of courses is `RenewalComparison`'s relational inventory. -/
theorem Ranking.wholeRun_iff {W F Cond : Type} (U : W → RelationalRenewal.Unfolding F Cond)
    (w : W) (e : F × Nat) :
    Ranking.wholeRun U w e ↔ (RenewalComparison.relationalInventory U).realized w e :=
  Iff.rfl

/-- The core's course without the focal formation has `RenewalComparison`'s levels. -/
theorem Ranking.undisturbed_eq (L : RelationalRenewal.Law) :
    ∀ t, Ranking.undisturbed L t = RenewalComparison.undisturbed L t
  | 0 => rfl
  | t + 1 =>
    congrArg (fun x => if L.needG ≤ x then x + L.renew else x) (Ranking.undisturbed_eq L t)

end Definitions

/-! ## The axiom discharges G0 in the existing modules -/

section Discharge

/-- Under the axiom `GenerativeComparison.G0` holds for every inventory, with positive relevance
read from significance: realized generative content whose continuation has significance from
every standpoint. Every theorem taking G0 as a hypothesis for an arbitrary positive relevance
holds with this one. -/
theorem inventory_g0_of_unrestricted {H Q F Pos : Type}
    (inventory : GenerativeComparison.Inventory H Q) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) :
    GenerativeComparison.G0 inventory
      (fun h q => inventory.generative q ∧ inventory.realized h q ∧
        ∀ p, sig p (step q) (formation q)) :=
  fun _ q generative realized => ⟨generative, realized, fun p => unrestricted (p, step q, formation q)⟩

/-- On a frame's inventory it is the core's positive relevance read from significance. -/
theorem relevance_inventory_iff {S A Q F Pos : Type} (M : Frame S A Q) (living : Q → Prop)
    (sig : Pos → Nat → F → Prop) (formation : Q → F) (step : Q → Nat) (s : S) (c : Q) :
    M.relevance living sig formation step s c ↔
      (M.inventory living).generative c ∧ (M.inventory living).realized s c ∧
        ∀ p, sig p (step c) (formation c) :=
  Iff.rfl

/-- From the axiom, a new realization of a generative extension has positive relevance read from
significance (`GenerativeComparison.new_realization_has_positive_relevance`). -/
theorem new_realization_of_unrestricted {H Q F Pos : Type}
    {inventory : GenerativeComparison.Inventory H Q} {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) {first second : H}
    (extension : GenerativeComparison.GenerativeExtension inventory first second) :
    ∃ q, (inventory.generative q ∧ inventory.realized second q ∧
        ∀ p, sig p (step q) (formation q)) ∧ ¬ inventory.realized first q :=
  GenerativeComparison.new_realization_has_positive_relevance
    (inventory_g0_of_unrestricted inventory unrestricted formation step) extension

/-- From the axiom, contingent generation secures positive ground read from significance
(`PositiveGroundUncertainty.contingent_generation_has_positive_ground`). -/
theorem contingent_generation_of_unrestricted {H Q F Pos : Type} (admitted : H → Prop)
    (before : H → Q → Prop) (inventory : GenerativeComparison.Inventory H Q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat)
    (formed : ∀ h, admitted h → ∃ q, inventory.generative q ∧ inventory.realized h q ∧
      ¬ before h q) :
    ∀ h, admitted h → ∃ q, (inventory.generative q ∧ inventory.realized h q ∧
      ∀ p, sig p (step q) (formation q)) ∧ ¬ before h q :=
  PositiveGroundUncertainty.contingent_generation_has_positive_ground admitted before inventory _
    (inventory_g0_of_unrestricted inventory unrestricted formation step) formed

/-- Universal address from the axiom: with D read on positive relevance from significance,
formation correspondence gives every position with access the reason
(`PositionedPositiveReason.every_situated_position_has_reason`). -/
theorem every_situated_position_has_reason_of_unrestricted {Pos H Q R F : Type}
    (access : Pos → R → Prop) (admitted : R → H → Prop) (before : H → Q → Prop)
    (inventory : GenerativeComparison.Inventory H Q) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat)
    (Reason : Pos → R → Prop)
    (articulate : PositionedPositiveReason.PositionedArticulation access admitted before
      (fun h q => inventory.generative q ∧ inventory.realized h q ∧
        ∀ p, sig p (step q) (formation q)) Reason)
    (a : R)
    (formed : ∀ h, admitted a h → ∃ q, inventory.generative q ∧ inventory.realized h q ∧
      ¬ before h q) :
    ∀ p, access p a → Reason p a :=
  PositionedPositiveReason.every_situated_position_has_reason access admitted before inventory _
    Reason (inventory_g0_of_unrestricted inventory unrestricted formation step) articulate a formed

end Discharge

/-! ## Situations of a frame and the lifting rule -/

section Lifting

open GenerativeComparison

variable {S A C : Type}

/-- Every outcome of `b` generatively extends every outcome of `a`. -/
def LiftExtension (F : Frame S A C) (living : C → Prop) (s : S) (a b : A) : Prop :=
  ∀ t, F.P.step s a t → ∀ t', F.P.step s b t' → Extension F living t t'

/-- C lifts: a lifted extension is a conservative lifted comparison. `Better first
second` follows `GenerativeComparison`: the second is better. -/
theorem comparison_lifts {F : Frame S A C} {living : C → Prop} {Better : S → S → Prop}
    (comparison : Comparison F living Better) {s : S} {a b : A}
    (extension : LiftExtension F living s a b) : LiftBetter F (fun x y => Better y x) s b a :=
  fun t' ht' t ht => comparison t t' (extension t ht t' ht')

/-- P with L: a lifted comparison between live responses supplies a reason to move. -/
def LiftedArticulation (F : Frame S A C) (Better : S → S → Prop) (s : S)
    (Reason : A → A → Prop) : Prop :=
  ∀ a b, Enabled F.P s a → Enabled F.P s b → LiftBetter F (fun x y => Better y x) s b a →
    Reason a b

theorem lifted_comparison_supplies_reason {F : Frame S A C} {living : C → Prop}
    {Better : S → S → Prop} {s : S} {Reason : A → A → Prop}
    (comparison : Comparison F living Better) (practical : LiftedArticulation F Better s Reason)
    {a b : A} (liveA : Enabled F.P s a) (liveB : Enabled F.P s b)
    (extension : LiftExtension F living s a b) : Reason a b :=
  practical a b liveA liveB (comparison_lifts comparison extension)

/-- A live response no live response liftedly extends. -/
def LiftSurvives (F : Frame S A C) (living : C → Prop) (s : S) (a : A) : Prop :=
  Enabled F.P s a ∧ ∀ b, Enabled F.P s b → ¬ LiftExtension F living s a b

/-- N with L: a selected response is live and liftedly dominated by no live one. -/
def LiftCoherence (F : Frame S A C) (Better : S → S → Prop) (s : S)
    (Selected : A → Prop) : Prop :=
  ∀ a, Selected a → Enabled F.P s a ∧
    ∀ b, Enabled F.P s b → ¬ LiftBetter F (fun x y => Better y x) s b a

theorem lift_coherent_selection_survives {F : Frame S A C} {living : C → Prop}
    {Better : S → S → Prop} {s : S} {Selected : A → Prop}
    (comparison : Comparison F living Better) (coherence : LiftCoherence F Better s Selected)
    {a : A} (selected : Selected a) : LiftSurvives F living s a :=
  match coherence a selected with
  | ⟨live, undominated⟩ =>
    ⟨live, fun b liveB extension => undominated b liveB (comparison_lifts comparison extension)⟩

theorem lift_continual_improvement_has_no_survivor {F : Frame S A C} {living : C → Prop}
    {s : S} (improvement : ∀ a, Enabled F.P s a → ∃ b, Enabled F.P s b ∧ LiftExtension F living s a b)
    (a : A) : ¬ LiftSurvives F living s a
  | ⟨live, survives⟩ => match improvement a live with
    | ⟨b, liveB, extension⟩ => survives b liveB extension

/-- A functional situation as one frame step at a configuration. -/
def situationProcess (situation : Situation S A) (s : S) : Process S A :=
  ⟨fun x a t => x = s ∧ situation.feasible a ∧ t = situation.realize a⟩

theorem situation_enabled_iff (situation : Situation S A) (s : S) (a : A) :
    Enabled (situationProcess situation s) s a ↔ situation.feasible a :=
  ⟨fun ⟨_, _, feasible, _⟩ => feasible, fun feasible => ⟨_, rfl, feasible, rfl⟩⟩

theorem situation_lift_iff (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (better : S → S → Prop) {a b : A} (feasibleA : situation.feasible a)
    (feasibleB : situation.feasible b) :
    LiftBetter ⟨situationProcess situation s, realized⟩ better s a b ↔
      better (situation.realize a) (situation.realize b) :=
  ⟨fun lifted => lifted _ ⟨rfl, feasibleA, rfl⟩ _ ⟨rfl, feasibleB, rfl⟩,
   fun held _ ⟨_, _, ha⟩ _ ⟨_, _, hb⟩ => by subst ha; subst hb; exact held⟩

/-- The functional articulation P is exactly the deterministic case of P with L. -/
theorem articulation_iff_lifted (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (Better : S → S → Prop) (Reason : A → A → Prop) :
    PracticalArticulation situation Better Reason ↔
      LiftedArticulation ⟨situationProcess situation s, realized⟩ Better s Reason :=
  ⟨fun practical a b liveA liveB lifted =>
    let fa := (situation_enabled_iff situation s a).mp liveA
    let fb := (situation_enabled_iff situation s b).mp liveB
    practical a b fa fb ((situation_lift_iff situation s realized _ fb fa).mp lifted),
   fun lifted a b fa fb better =>
    lifted a b ((situation_enabled_iff situation s a).mpr fa)
      ((situation_enabled_iff situation s b).mpr fb)
      ((situation_lift_iff situation s realized (fun x y => Better y x) fb fa).mpr better)⟩

namespace LiftModel

inductive Act where
  | low | high | mixed | dead

/-- From configuration 0: `low` reaches 1, `high` 3, `mixed` 0 or 4, `dead` nothing.
A larger configuration is better. -/
def options : Nat → Act → Nat → Prop
  | s, .low, t => s = 0 ∧ t = 1
  | s, .high, t => s = 0 ∧ t = 3
  | s, .mixed, t => s = 0 ∧ (t = 0 ∨ t = 4)
  | _, .dead, _ => False

def frame : Frame Nat Act Unit := ⟨⟨options⟩, fun _ _ => True⟩

def larger (x y : Nat) : Prop := y < x

/-- The lifting rule is substantive: a response with one better and one worse
outcome is not comparable by the conservative rule, yet some outcome beats. -/
theorem some_outcome_does_not_lift :
    (∃ t t', frame.P.step 0 .mixed t ∧ frame.P.step 0 .high t' ∧ larger t t') ∧
    ¬ LiftBetter frame larger 0 .mixed .high ∧ ¬ LiftBetter frame larger 0 .high .mixed :=
  ⟨⟨4, 3, ⟨rfl, Or.inr rfl⟩, ⟨rfl, rfl⟩, Nat.lt_succ_self 3⟩,
    fun lifted => Nat.not_lt_zero 3 (lifted 0 ⟨rfl, Or.inl rfl⟩ 3 ⟨rfl, rfl⟩),
    fun lifted => Nat.lt_asymm (Nat.lt_succ_self 3) (lifted 3 ⟨rfl, rfl⟩ 4 ⟨rfl, Or.inr rfl⟩)⟩

/-- Transitivity needs a live middle response: through a response with no outcome
both lifted comparisons hold vacuously, while the composite fails. -/
theorem lift_needs_live_middle :
    LiftBetter frame larger 0 .low .dead ∧ LiftBetter frame larger 0 .dead .high ∧
    ¬ LiftBetter frame larger 0 .low .high :=
  ⟨fun _ _ _ never => (nomatch never), fun _ never => (nomatch never),
    fun lifted => Nat.lt_asymm (lifted 1 ⟨rfl, rfl⟩ 3 ⟨rfl, rfl⟩)
      (Nat.lt_trans (Nat.lt_succ_self 1) (Nat.lt_succ_self 2))⟩

end LiftModel

end Lifting

end Becoming
