import Becoming.LossMatching
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

-- `Frame.StrictLossMatch` now lives in `Becoming.LossMatching` with its general laws.

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

def outageAt (t : Nat) : Person → Bool
  | .focal => t == 1 || t == 3
  | .peerOne | .peerTwo | .peerThree => t == 1

def personClaim : Person → Claim
  | .focal => .first
  | .peerOne => .peerOne
  | .peerTwo => .peerTwo
  | .peerThree => .peerThree

/-- A supplied availability law: outside the specified fault episodes the common
backbone supplies support; during an episode the installed repair is needed. -/
def availableNow (s : State) (p : Person) : Bool :=
  s.backbone && (if outageAt s.clock p then protects s.repair (personClaim p) else true)

/-- Actual availability now, not a vacuous statement about absent demand. -/
def supportedNow (s : State) (p : Person) : Prop := availableNow s p = true

instance decidableSupportedNow (s : State) (p : Person) : Decidable (supportedNow s p) :=
  inferInstanceAs (Decidable (availableNow s p = true))

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

/-- The retained episode claim reads actual support at that episode in the same
produced course. Owners differentiate positions; they are not values to be summed. -/
theorem historical_claim_iff_support (fragile : Bool) (r : Repair) (c : Claim) (p : Person) :
    owner c = some p →
    ((frame fragile).realized (finalState fragile r) c ↔
      supportedNow (states fragile r (episodeTime c)) p) := by
  cases fragile <;> cases r <;> cases c <;> cases p <;> decide

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


/-! ## The constructed process as an instance of the general laws (scratch draft) -/

section Instances

open Frame

def allClaims : List Claim := [.first, .second, .peerOne, .peerTwo, .peerThree, .backbone]

theorem allClaims_distinct : Distinct allClaims :=
  @of_decide_eq_true _ (LossMatching.decideDistinct allClaims) rfl

theorem allClaims_every : ∀ c, c ∈ allClaims
  | .first => .head _
  | .second => .tail _ (.head _)
  | .peerOne => .tail _ (.tail _ (.head _))
  | .peerTwo => .tail _ (.tail _ (.tail _ (.head _)))
  | .peerThree => .tail _ (.tail _ (.tail _ (.tail _ (.head _))))
  | .backbone => .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))

/-- Every final configuration lists its losses (the general `lossesListed_lostOf`). -/
theorem listed (fragile : Bool) (r : Repair) :
    (frame fragile).LossesListed (finalState fragile r)
      ((frame fragile).lostOf (finalState fragile r) allClaims) :=
  lossesListed_lostOf allClaims_distinct allClaims_every

def lostCount (r : Repair) : Nat :=
  ((frame false).lostOf (finalState false r) allClaims).length

theorem lost_not_backbone (r : Repair) :
    ∀ c, ¬ (frame false).realized (finalState false r) c → c ≠ .backbone := by
  intro c; cases r <;> cases c <;> decide

/-- With the backbone kept, every loss is an episode, so all losses are alike. -/
theorem losses_alike (x y : Repair) : ∀ c d, ¬ (frame false).realized (finalState false x) c →
    ¬ (frame false).realized (finalState false y) d → sameEpisode c d :=
  fun c d lc ld => Or.inr ⟨lost_not_backbone x c lc, lost_not_backbone y d ld⟩

/-- **The instance of the counting law**: between any two repair courses, a strict loss match
exists exactly when the better loses fewer episodes. -/
theorem matches_iff (x y : Repair) :
    (frame false).StrictLossMatch sameEpisode (finalState false x) (finalState false y) ↔
      lostCount x < lostCount y :=
  strictLossMatch_iff_length_of_alike (listed false x) (listed false y) (losses_alike x y)

theorem lost_counts :
    lostCount .focal = 3 ∧ lostCount .one = 4 ∧ lostCount .two = 3 ∧ lostCount .three = 2 := by
  decide

/-- `focal_matches_one` and `three_matches_focal` recovered from the general law. -/
theorem focal_matches_one_by_count :
    (frame false).StrictLossMatch sameEpisode (finalState false .focal) (finalState false .one) :=
  (matches_iff .focal .one).mpr (by decide)

theorem three_matches_focal_by_count :
    (frame false).StrictLossMatch sameEpisode (finalState false .three) (finalState false .focal) :=
  (matches_iff .three .focal).mpr (by decide)

/-- Two against two: equal counts, no strict match either way (the loss correspondence of
`two_loss_correspondence` is all there is). -/
theorem two_focal_neither :
    ¬ (frame false).StrictLossMatch sameEpisode (finalState false .two) (finalState false .focal) ∧
    ¬ (frame false).StrictLossMatch sameEpisode (finalState false .focal) (finalState false .two) :=
  ⟨fun m => (by decide : ¬ lostCount .two < lostCount .focal) ((matches_iff .two .focal).mp m),
   fun m => (by decide : ¬ lostCount .focal < lostCount .two) ((matches_iff .focal .two).mp m)⟩

/-- The converse of `strictLossMatch_of_extension` fails: the lower anchor is a strict loss
match that is no generative extension (the focal course loses `peerOne`, which the other keeps). -/
theorem focal_one_not_extension (living : Claim → Prop) :
    ¬ Extension (frame false) living (finalState false .one) (finalState false .focal) :=
  fun ⟨keeps, _⟩ => (by decide : ¬ (frame false).realized (finalState false .focal) .peerOne)
    (keeps .peerOne (by decide))

/-- The fragile control from the general common-support law: every claim rests on the
backbone, so the fragile three-branch course is strictly matched below no course, under any
content relation. -/
theorem fragile_three_below_nothing (same : Claim → Claim → Prop) (w : State) :
    ¬ (frame true).StrictLossMatch same (finalState true .three) w :=
  not_strictLossMatch_of_base_lost (F := frame true) (base := .backbone)
    (fun (s : State) (c : Claim) (realized : (frame true).realized s c) =>
      (⟨Nat.zero_le _, realized.2.1, rfl⟩ : (frame true).realized s .backbone))
    allClaims_distinct allClaims_every fragile_three_loses_backbone w

/-- P100's sufficiency commitment is the general one on this frame. -/
theorem sufficientMatching_iff (scope Le : State → State → Prop) :
    SufficientMatching scope Le ↔ (frame false).SufficientMatching sameEpisode scope Le :=
  Iff.rfl

/-! ### Episode claims are read at their time -/

theorem states_succ (fragile : Bool) (r : Repair) :
    ∀ t, states fragile r (t + 1) = ⟨t + 1, some r, backboneAfter fragile r⟩
  | 0 => rfl
  | t + 1 => congrArg (fun s => advance fragile s r) (states_succ fragile r t)

theorem realized_succ (fragile : Bool) (r : Repair) (c : Claim) (t : Nat) :
    (frame fragile).realized (states fragile r (t + 1)) c ↔
      (episodeTime c ≤ t + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true) :=
  Eq.subst (motive := fun s => (frame fragile).realized s c ↔
      (episodeTime c ≤ t + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true))
    (states_succ fragile r t).symm Iff.rfl

theorem episode_le_four : ∀ c : Claim, episodeTime c ≤ 4 := by
  intro c; cases c <;> decide

theorem owned_time_pos : ∀ (c : Claim) (p : Person), owner c = some p → 0 < episodeTime c
  | .first, _, _ => Nat.succ_pos 0
  | .second, _, _ => Nat.succ_pos 2
  | .peerOne, _, _ => Nat.succ_pos 0
  | .peerTwo, _, _ => Nat.succ_pos 0
  | .peerThree, _, _ => Nat.succ_pos 0
  | .backbone, _, owned => nomatch owned

/-- **Every episode claim is read at its episode time** along every course: from then on it
is realized exactly where its owner had support at that time (the general `ReadsAt`). -/
theorem reads_at_episode (fragile : Bool) (r : Repair) (c : Claim) (p : Person)
    (owned : owner c = some p) :
    (frame fragile).ReadsAt (run fragile r) c (episodeTime c) (fun s _ => supportedNow s p) :=
  fun t le => match t, le with
  | 0, le => absurd (owned_time_pos c p owned) (Nat.not_lt_of_le le)
  | t + 1, le =>
    (realized_succ fragile r c t).trans
      ((⟨fun h => ⟨episode_le_four c, h.2⟩, fun h => ⟨le, h.2⟩⟩ :
          (episodeTime c ≤ t + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true) ↔
          (episodeTime c ≤ 3 + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true)).trans
        ((realized_succ fragile r c 3).symm.trans (historical_claim_iff_support fragile r c p owned)))

/-- `recovery_retains_loss` at every later step, from the general law: the focal episodes
missed under the three-branch repair stay lost whatever support returns. -/
theorem focal_losses_retained (t : Nat) (le : 3 ≤ t) :
    ¬ (frame false).realized ((run false .three).state t) .first ∧
    ¬ (frame false).realized ((run false .three).state t) .second :=
  ⟨(reads_at_episode false .three .first .focal rfl).loss_retained (by decide)
      (Nat.le_trans (by decide) le),
   (reads_at_episode false .three .second .focal rfl).loss_retained (by decide) le⟩

end Instances

end RepairComparison
end Becoming
