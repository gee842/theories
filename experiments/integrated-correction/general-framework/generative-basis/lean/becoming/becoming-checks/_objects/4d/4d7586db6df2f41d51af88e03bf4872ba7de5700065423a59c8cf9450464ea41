import Becoming.Frame
import GenerativeLossComparison

/-!
# Comparison anchors for complete basic episodes (peripheral spine application)

One supplied repair process produces all alternatives from the same initial state.
A focal repair secures two episodes at the same living position, with support
available between them. Group repairs secure one, two, or three other episodes.
The historical frame retains missed episodes after current support has returned.

The process establishes support availability, not full experienced recovery or
ethical equivalence. Reading the five episodes as complete comparable basic losses
and making strict matching sufficient are explicit application and normative
premises. No clock-duration price, unconditional aggregation theorem, global FR
threshold, or general permission is proved. A backbone failure remains visible.
-/
namespace Becoming

namespace Frame

variable {S A C : Type}

/-- Each lost claim in the better configuration has a distinct corresponding lost
claim in the worse, which has another loss. `same` is a supplied content relation. -/
def StrictLossMatch (F : Frame S A C) (same : C → C → Prop) (better worse : S) : Prop :=
  ∃ image : C → C,
    (∀ c, ¬ F.realized better c → ¬ F.realized worse (image c)) ∧
    (∀ c, ¬ F.realized better c → same c (image c)) ∧
    (∀ c d, ¬ F.realized better c → ¬ F.realized better d → image c = image d → c = d) ∧
    ∃ extra, ¬ F.realized worse extra ∧
      ∀ c, ¬ F.realized better c → image c ≠ extra

end Frame

namespace RepairComparison

open Generative GenerativeLossComparison

inductive Repair where
  | focal | one | two | three
  deriving DecidableEq

inductive Person where
  | focal | peerOne | peerTwo | peerThree
  deriving DecidableEq

/-- The first and second focal episodes are different times of the same life. -/
inductive Claim where
  | first | second | peerOne | peerTwo | peerThree | backbone
  deriving DecidableEq

structure State where
  clock : Nat
  repair : Option Repair
  backbone : Bool

def start : State := ⟨0, none, true⟩

/-- In the failure control the three-branch repair disconnects the backbone.
This is an alternative supplied law, not a free ethical predicate. -/
def backboneAfter (fragile : Bool) : Repair → Bool
  | .focal => true
  | .one => true
  | .two => true
  | .three => !fragile

/-- Repair can be installed once; later changes retain it and advance time. -/
def advance (fragile : Bool) (s : State) (r : Repair) : State :=
  match s.repair with
  | none => ⟨s.clock + 1, some r, s.backbone && backboneAfter fragile r⟩
  | some old => ⟨s.clock + 1, some old, s.backbone⟩

def process (fragile : Bool) : Process State Repair :=
  ⟨fun s r t => t = advance fragile s r⟩

def states (fragile : Bool) (r : Repair) : Nat → State
  | 0 => start
  | t + 1 => advance fragile (states fragile r t) r

def run (fragile : Bool) (r : Repair) : Run (process fragile) where
  state := states fragile r
  act _ := r
  step _ := rfl

def episodeTime : Claim → Nat
  | .first | .peerOne | .peerTwo | .peerThree => 1
  | .second => 3
  | .backbone => 0

def owner : Claim → Option Person
  | .first | .second => some .focal
  | .peerOne => some .peerOne
  | .peerTwo => some .peerTwo
  | .peerThree => some .peerThree
  | .backbone => none

def protects (r : Option Repair) : Claim → Bool
  | .backbone => true
  | .first | .second => match r with
    | none => false
    | some .focal => true
    | some .one | some .two | some .three => false
  | .peerOne => match r with
    | none | some .focal => false
    | some .one | some .two | some .three => true
  | .peerTwo => match r with
    | none | some .focal | some .one => false
    | some .two | some .three => true
  | .peerThree => match r with
    | none | some .focal | some .one | some .two => false
    | some .three => true

/-- Realized claims preserve their episode time; current recovery erases no history. -/
def frame (fragile : Bool) : Frame State Repair Claim where
  P := process fragile
  realized s c := episodeTime c ≤ s.clock ∧ s.backbone = true ∧ protects s.repair c = true

instance decidableRealized (fragile : Bool) (s : State) (c : Claim) :
    Decidable ((frame fragile).realized s c) :=
  inferInstanceAs (Decidable (episodeTime c ≤ s.clock ∧ s.backbone = true ∧ protects s.repair c = true))

def needs (t : Nat) : Person → Bool
  | .focal => t == 1 || t == 3
  | .peerOne | .peerTwo | .peerThree => t == 1

def personClaim : Person → Claim
  | .focal => .first
  | .peerOne => .peerOne
  | .peerTwo => .peerTwo
  | .peerThree => .peerThree

/-- Availability of support now, separate from historical episode realization. -/
def supportedNow (s : State) (p : Person) : Prop :=
  s.backbone = true ∧ (needs s.clock p = true → protects s.repair (personClaim p) = true)

instance decidableSupportedNow (s : State) (p : Person) : Decidable (supportedNow s p) :=
  inferInstanceAs (Decidable (s.backbone = true ∧
    (needs s.clock p = true → protects s.repair (personClaim p) = true)))

def finalState (fragile : Bool) (r : Repair) : State := states fragile r 4

theorem common_start (fragile : Bool) (r : Repair) : (run fragile r).state 0 = start := rfl

theorem generated_trace (fragile : Bool) (r : Repair) :
    Trace (frame fragile).P start ((run fragile r).window 0 4) (finalState fragile r) := by
  exact (run fragile r).window_trace 4 0

theorem separated_same_life :
    owner .first = owner .second ∧ episodeTime .first = 1 ∧ episodeTime .second = 3 :=
  ⟨rfl, rfl, rfl⟩

theorem support_between_episodes (r : Repair) (p : Person) :
    supportedNow (states false r 2) p := by
  cases r <;> cases p <;> decide

theorem current_support_restored (r : Repair) (p : Person) :
    supportedNow (finalState false r) p := by
  cases r <;> cases p <;> decide

theorem recovery_retains_loss :
    supportedNow (finalState false .three) .focal ∧
    ¬ (frame false).realized (finalState false .three) .first ∧
    ¬ (frame false).realized (finalState false .three) .second := by decide

/-- The five episode contents are treated alike; backbone loss is distinct.
Actual adequacy of this reading is NOT established by its definition. -/
def sameEpisode (a b : Claim) : Prop :=
  (a = .backbone ∧ b = .backbone) ∨ (a ≠ .backbone ∧ b ≠ .backbone)

instance decidableSameEpisode (a b : Claim) : Decidable (sameEpisode a b) :=
  inferInstanceAs (Decidable ((a = .backbone ∧ b = .backbone) ∨
    (a ≠ .backbone ∧ b ≠ .backbone)))

def toOne : Claim → Claim
  | .first => .first
  | .second => .second
  | .peerOne => .first
  | .peerTwo => .peerTwo
  | .peerThree => .peerThree
  | .backbone => .backbone

theorem focal_matches_one :
    (frame false).StrictLossMatch sameEpisode (finalState false .focal) (finalState false .one) := by
  refine ⟨toOne, ?_, ?_, ?_, .second, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c; cases c <;> decide
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def toFocal : Claim → Claim
  | .first => .peerOne
  | .second => .peerTwo
  | .peerOne => .peerOne
  | .peerTwo => .peerTwo
  | .peerThree => .peerThree
  | .backbone => .backbone

theorem three_matches_focal :
    (frame false).StrictLossMatch sameEpisode (finalState false .three) (finalState false .focal) := by
  refine ⟨toFocal, ?_, ?_, ?_, .peerThree, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c; cases c <;> decide
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def swapTwo : Claim → Claim
  | .first => .peerOne
  | .second => .peerTwo
  | .peerOne => .first
  | .peerTwo => .second
  | .peerThree => .peerThree
  | .backbone => .backbone

theorem two_loss_correspondence (c : Claim) :
    (¬ (frame false).realized (finalState false .focal) c) ↔
    ¬ (frame false).realized (finalState false .two) (swapTwo c) := by
  cases c <;> decide

theorem two_correspondence_involutive (c : Claim) : swapTwo (swapTwo c) = c := by
  cases c <;> rfl

/-- The ethical bridge is supplied; scope carries full-content, permission,
history and support correspondence. Strict matching alone does not justify it. -/
def SufficientMatching (scope : State → State → Prop) (Le : State → State → Prop) : Prop :=
  ∀ better worse, scope better worse →
    (frame false).StrictLossMatch sameEpisode better worse → Strict Le worse better

theorem conditional_lower_anchor {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le)
    (adequate : scope (finalState false .focal) (finalState false .one)) :
    Strict Le (finalState false .one) (finalState false .focal) :=
  sufficient _ _ adequate focal_matches_one

theorem conditional_upper_anchor {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le)
    (adequate : scope (finalState false .three) (finalState false .focal)) :
    Strict Le (finalState false .focal) (finalState false .three) :=
  sufficient _ _ adequate three_matches_focal

/-- The lower and upper anchors give a strict outer comparison only under the
existing explicitly supplied transitivity condition. -/
theorem conditional_outer_order {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le) (trans : Transitive Le)
    (lower : scope (finalState false .focal) (finalState false .one))
    (upper : scope (finalState false .three) (finalState false .focal)) :
    Strict Le (finalState false .one) (finalState false .three) :=
  strict_improvement_transport trans (conditional_lower_anchor sufficient lower)
    (conditional_upper_anchor sufficient upper).1

theorem fragile_three_loses_backbone :
    ¬ (frame true).realized (finalState true .three) .backbone := by decide

theorem fragile_focal_keeps_backbone :
    (frame true).realized (finalState true .focal) .backbone := by decide

/-- The very same episode counts cannot certify the larger repair when its actual
operation severs common support. No historical life is grouped away. -/
theorem fragile_three_not_matching :
    ¬ (frame true).StrictLossMatch sameEpisode (finalState true .three) (finalState true .focal) := by
  intro matched
  obtain ⟨image, losses, contents, _⟩ := matched
  have related := contents .backbone fragile_three_loses_backbone
  have imageIs : image .backbone = .backbone := by
    cases related with
    | inl same => exact same.2
    | inr different => exact False.elim (different.1 rfl)
  have missing := losses .backbone fragile_three_loses_backbone
  rw [imageIs] at missing
  exact missing fragile_focal_keeps_backbone

end RepairComparison
end Becoming
