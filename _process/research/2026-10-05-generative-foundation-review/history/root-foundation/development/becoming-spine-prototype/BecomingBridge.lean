import GenerativeCore
import InquirySufficiency
import JointContinuationClassification
import WholeGroundCoverage
import GenerativeComparison
import PracticalJudgment
import StandardsBridge
import PositionedPositiveReason
import PracticalReach

/-! Scratch bridge prototype (not a repository result). One declared process with
one realization valuation; evaluative predicates are further predicates on the
same configurations, constrained by supplied premises G0 and D. -/

namespace BecomingBridge
open Generative Generative.InquirySufficiency GenerativeComparison

universe u u' v w

/-- Proposed base: process plus realized claims; `generative` marks claims. -/
structure Frame (S : Type u) (A : Type v) (C : Type w) where
  P : Process S A
  realized : S → C → Prop
  generative : C → Prop

variable {S : Type u} {A : Type v} {C : Type w}

/-! ## (a) Ethics continuation spaces are trace spaces -/

def continuations (F : Frame S A C) (root : S) :
    JointContinuationClassification.Continuations (List A × S) C where
  feasible h := Trace F.P root h.1 h.2
  realized h c := F.realized h.2 c

def inventory (F : Frame S A C) : Inventory (List A × S) C where
  realized h c := F.realized h.2 c
  generative := F.generative

/-- Core `trace_map` gives the ethics-side faithful transport certificate. -/
theorem projection_carries_bundles {S' : Type u'} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (hstep : ∀ s a t, F.P.step s a t → G.P.step (q s) a (q t))
    (hclaim : ∀ s c, F.realized s c → G.realized (q s) c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (continuations F root) (continuations G (q root)) :=
  JointContinuationClassification.faithful_history_transport_preserves_joint_bundles
    (fun h => (h.1, q h.2)) (fun _ tr => trace_map hstep tr) (fun _ c _ r => hclaim _ c r)

/-- Core `trace_lift` gives the converse: a lifting summary loses no joint bundle. -/
theorem lifting_reflects_bundles {S' : Type u'} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (hlift : ∀ s a r, G.P.step (q s) a r → ∃ t, F.P.step s a t ∧ q t = r)
    (hclaim : ∀ s c, G.realized (q s) c → F.realized s c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (continuations G (q root)) (continuations F root) := by
  rintro bundle ⟨⟨w, r⟩, tr, all⟩
  obtain ⟨t, tr', hq⟩ := trace_lift hlift tr
  refine ⟨(w, t), tr', fun c hc => hclaim t c ?_⟩
  have := all c hc
  simp only [continuations] at this
  exact hq ▸ this

/-- `WholeGroundCoverage.Reached` is trace reachability of a one-label process. -/
def edgeProcess {X : Type u} (Edge : X → X → Prop) : Process X Unit := ⟨fun p _ q => Edge p q⟩

theorem reached_iff_trace {X : Type u} (Seed : X → Prop) (Edge : X → X → Prop) (q : X) :
    WholeGroundCoverage.Reached Seed Edge q ↔
      ∃ p w, Seed p ∧ Trace (edgeProcess Edge) p w q := by
  constructor
  · intro h
    induction h with
    | seed hs => exact ⟨_, [], hs, .nil _⟩
    | step _ he ih =>
      obtain ⟨p, w, hs, tr⟩ := ih
      exact ⟨p, w ++ [()], hs, trace_append_iff.mpr ⟨_, tr, trace_singleton_iff.mpr he⟩⟩
  · rintro ⟨p, w, hs, tr⟩
    have carry : ∀ {x y : X} {w : List Unit}, Trace (edgeProcess Edge) x w y →
        WholeGroundCoverage.Reached Seed Edge x → WholeGroundCoverage.Reached Seed Edge y := by
      intro x y w tr
      induction tr with
      | nil => exact id
      | cons st _ ih => exact fun hx => ih (.step hx st)
    exact carry tr (.seed hs)

/-! ## (b) Robust = CommonResponse, both directions -/

theorem commonResponse_is_robust {S R : Type} (P : Process S A)
    (safe : S → A → S → Prop) (goal : S → Prop) (response : R → List A)
    (B : S → Prop) (r : R) :
    CommonResponse P safe goal response B r ↔
      PracticalJudgment.Robust B (fun s r => Completes P safe goal s (response r)) r := Iff.rfl

/-- Any admissibility table is a one-step process into a closed endpoint. -/
def judgeProcess {W H : Type} (ad : W → H → Prop) : Process (Option W) H where
  step s a t := ∃ w, s = some w ∧ ad w a ∧ t = none

def sees {W : Type} (live : W → Prop) : Option W → Prop := fun s => ∃ w, live w ∧ s = some w

theorem robust_iff_commonResponse {W H : Type} (live : W → Prop) (ad : W → H → Prop) (a : H) :
    PracticalJudgment.Robust live ad a ↔
      CommonResponse (judgeProcess ad) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees live) a := by
  constructor
  · rintro h s ⟨w, hw, rfl⟩
    exact ⟨⟨none, w, rfl, h w hw, rfl⟩, fun _ _ => ⟨trivial, trivial⟩⟩
  · intro h w hw
    obtain ⟨⟨_, w', eq, adm, _⟩, _⟩ := h (some w) ⟨w, hw, rfl⟩
    cases eq
    exact adm

/-- `robust_under_refinement` is antitonicity of CommonResponse in the belief. -/
theorem commonResponse_antitone {R : Type w} {P : Process S A}
    {safe : S → A → S → Prop} {goal : S → Prop} {response : R → List A}
    {B B' : S → Prop} {r : R} (sub : ∀ s, B' s → B s)
    (h : CommonResponse P safe goal response B r) : CommonResponse P safe goal response B' r :=
  fun s hs => h s (sub s hs)

/-- Pure observation: a stuttering query whose outcome is read by `sense`. -/
def observe {Q : Type v} : Process S Q := ⟨fun s _ t => t = s⟩

theorem after_observe_iff {Q : Type v} {k : Nat} (obs : S → Q → Fin k)
    (B : S → Prop) (q : Q) (o : Fin k) (t : S) :
    After observe (fun s q _ => obs s q) B q o t ↔ B t ∧ obs t q = o := by
  constructor
  · rintro ⟨s, hs, rfl, ho⟩
    exact ⟨hs, ho⟩
  · rintro ⟨hs, ho⟩
    exact ⟨t, hs, rfl, ho⟩

/-- Explicit encoding: Fin literals `0`/`1` carry `propext` through `Fin.ofNat`. -/
def encode : Bool → Fin 2
  | false => ⟨0, Nat.zero_lt_succ 1⟩
  | true => ⟨1, Nat.succ_lt_succ (Nat.zero_lt_succ 0)⟩

theorem encode_inj : ∀ {a b : Bool}, encode a = encode b → a = b
  | false, false, _ => rfl
  | true, true, _ => rfl
  | false, true, h => Nat.noConfusion (congrArg Fin.val h)
  | true, false, h => Nat.noConfusion (congrArg Fin.val h)

theorem mem_filter_direct {α : Type} (p : α → Bool) (x : α) :
    ∀ l : List α, x ∈ l.filter p ↔ x ∈ l ∧ p x = true
  | [] => ⟨fun h => (nomatch h), fun ⟨h, _⟩ => (nomatch h)⟩
  | a :: l => by
    have ih := mem_filter_direct p x l
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
      | head => exact absurd (hp.symm.trans px) (by decide)
      | tail _ m => exact ih.mpr ⟨m, px⟩

theorem beq_true_iff : ∀ x b : Bool, (x == b) = true ↔ x = b := by decide

/-- StandardsBridge `revise` (list/Bool) is core `After` (predicate/Fin 2). -/
theorem revise_is_after {Q : Type} (hs : List (StandardsBridge.Rule Q)) (q : Q) (b : Bool)
    (h : StandardsBridge.Rule Q) :
    h ∈ StandardsBridge.revise hs (q, b) ↔
      After observe (fun (g : StandardsBridge.Rule Q) q _ => encode (g q)) (· ∈ hs) q
        (encode b) h :=
  (mem_filter_direct _ h hs).trans <|
    (Iff.intro (fun ⟨m, e⟩ => ⟨m, congrArg encode ((beq_true_iff _ _).mp e)⟩)
      (fun ⟨m, e⟩ => ⟨m, (beq_true_iff _ _).mpr (encode_inj e)⟩)).trans
    (after_observe_iff (fun (g : StandardsBridge.Rule Q) q => encode (g q)) _ q _ h).symm

/-- PracticalReach `Guarantees` is one-step `Completes`. -/
theorem guarantees_is_completes {S : Type} {A : Type} (P : Process S A) (s : S) (a : A)
    (goal : S → Prop) :
    PracticalReach.Guarantees (fun a t => P.step s a t) a goal ↔
      Completes P (fun _ _ _ => True) goal s [a] :=
  ⟨fun ⟨live, all⟩ => ⟨live, fun t st => ⟨trivial, all t st⟩⟩,
   fun ⟨live, all⟩ => ⟨live, fun t st => (all t st).2⟩⟩

/-! ## (c) Normative lift -/

/-- New generative content at a configuration, relative to a recorded `before`. -/
def Novel (F : Frame S A C) (before : S → C → Prop) (t : S) : Prop :=
  ∃ c, F.generative c ∧ F.realized t c ∧ ¬ before t c

/-- Visible scope of a policy from a belief: endpoints of its actual executions. -/
def Scope {R : Type w} {k : Nat} (F : Frame S A C) (sense : S → A → S → Fin k)
    (response : R → List A) (B : S → Prop) (policy : Policy A R k) (t : S) : Prop :=
  ∃ s word, B s ∧ Execution F.P sense response policy s word t

/-- Dynamic half: a sound bounded inquiry for novelty secures it over its scope. -/
theorem sound_inquiry_secures {R : Type w} {k : Nat} {F : Frame S A C}
    {safe : S → A → S → Prop} {before : S → C → Prop} {sense : S → A → S → Fin k}
    {response : R → List A} {B : S → Prop} {policy : Policy A R k}
    (sound : Sound F.P safe (Novel F before) sense response policy B) :
    ∀ t, Scope F sense response B policy t → Novel F before t :=
  fun _ ⟨_, _, hB, ex⟩ => sound_execution_meets_goal sound hB ex

/-- Generic lift, universe-polymorphic: G0 then D, for ANY securing scope. -/
theorem normative_lift {Pos : Type u} {H : Type u'} {Q : Type v} {Resp : Type w}
    (inv : Inventory H Q) (before positive : H → Q → Prop)
    (access : Pos → Resp → Prop) (scope : Resp → H → Prop) (Reason : Pos → Resp → Prop)
    (g0 : G0 inv positive)
    (D : ∀ p r, access p r → (∀ h, scope r h → ∃ q, positive h q ∧ ¬ before h q) → Reason p r)
    (r : Resp)
    (secured : ∀ h, scope r h → ∃ q, inv.generative q ∧ inv.realized h q ∧ ¬ before h q) :
    ∀ p, access p r → Reason p r :=
  fun p hp => D p r hp fun h hs =>
    (secured h hs).elim fun q ⟨g, real, new⟩ => ⟨q, g0 h q g real, new⟩

def stateInventory (F : Frame S A C) : Inventory S C := ⟨F.realized, F.generative⟩

/-- Instance through the AUDITED theorem (Type 0 only, as audited). -/
theorem sound_inquiry_gives_positioned_reason {S A C R Pos : Type} {k : Nat}
    (F : Frame S A C) (safe : S → A → S → Prop) (sense : S → A → S → Fin k)
    (response : R → List A) (B : S → Prop) (before positive : S → C → Prop)
    (access : Pos → Policy A R k → Prop) (Reason : Pos → Policy A R k → Prop)
    (g0 : G0 (stateInventory F) positive)
    (D : PositionedPositiveReason.PositionedArticulation access
      (fun pol t => Scope F sense response B pol t) before positive Reason)
    (policy : Policy A R k) (sound : Sound F.P safe (Novel F before) sense response policy B) :
    ∀ p, access p policy → Reason p policy :=
  PositionedPositiveReason.every_situated_position_has_reason access _ before
    (stateInventory F) positive Reason g0 D policy (sound_inquiry_secures sound)

/-! ## J1/J2 on the same configurations; lifting to nondeterministic responses -/

def BetterAt {S A C : Type} (F : Frame S A C) (basic : C → Prop) : S → S → Prop :=
  PracticalJudgment.Better (fun s c => basic c ∧ F.realized s c)
    (fun s c => F.generative c ∧ F.realized s c)

/-- Response `a` beats `b` at `s` when every outcome of `a` beats every outcome of `b`. -/
def LiftBetter {S A C : Type} (F : Frame S A C) (basic : C → Prop) (s : S) (a b : A) : Prop :=
  ∀ t, F.P.step s a t → ∀ t', F.P.step s b t' → BetterAt F basic t t'

/-- Transitivity needs a live middle response: the core's `Enabled` reappears. -/
theorem liftBetter_trans {S A C : Type} {F : Frame S A C} {basic : C → Prop} {s : S}
    {a b c : A} (hab : LiftBetter F basic s a b) (hbc : LiftBetter F basic s b c)
    (live : Enabled F.P s b) : LiftBetter F basic s a c := by
  intro t ht t'' ht''
  obtain ⟨m, hm⟩ := live
  exact PracticalJudgment.better_trans _ _ (hab t ht m hm) (hbc m hm t'' ht'')

theorem liftBetter_irrefl {S A C : Type} {F : Frame S A C} {basic : C → Prop} {s : S}
    {a : A} (live : Enabled F.P s a) : ¬ LiftBetter F basic s a a := by
  intro h
  obtain ⟨t, ht⟩ := live
  exact PracticalJudgment.better_irrefl _ _ t (h t ht t ht)

end BecomingBridge
