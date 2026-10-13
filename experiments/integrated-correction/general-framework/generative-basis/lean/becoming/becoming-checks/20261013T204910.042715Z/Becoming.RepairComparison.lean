import Becoming.LossMatching
import GenerativeLossComparison

/-!
# Comparison anchors for complete basic episodes (peripheral spine application)

One supplied repair process produces all alternatives from the same initial state.
Repair `a` secures the two episodes of life `p`, with support available between them.
Repairs `b1`, `b2` and `b3` secure the episodes of one, two or three of the lives `q`,
`r` and `s`.
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
  | a | b1 | b2 | b3
  deriving DecidableEq

inductive Life where
  | p | q | r | s
  deriving DecidableEq

/-- The first and second episodes of `p` are different times of the same life. -/
inductive Claim where
  | first | second | q | r | s | backbone
  deriving DecidableEq

structure State where
  clock : Nat
  repair : Option Repair
  backbone : Bool

def start : State := ⟨0, none, true⟩

/-- In the failure control repair `b3` disconnects the backbone.
This is an alternative supplied law, not a free ethical predicate. -/
def backboneAfter (fragile : Bool) : Repair → Bool
  | .a => true
  | .b1 => true
  | .b2 => true
  | .b3 => !fragile

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
  | .first | .q | .r | .s => 1
  | .second => 3
  | .backbone => 0

def lifeOf : Claim → Option Life
  | .first | .second => some .p
  | .q => some .q
  | .r => some .r
  | .s => some .s
  | .backbone => none

def protects (r : Option Repair) : Claim → Bool
  | .backbone => true
  | .first | .second => match r with
    | none => false
    | some .a => true
    | some .b1 | some .b2 | some .b3 => false
  | .q => match r with
    | none | some .a => false
    | some .b1 | some .b2 | some .b3 => true
  | .r => match r with
    | none | some .a | some .b1 => false
    | some .b2 | some .b3 => true
  | .s => match r with
    | none | some .a | some .b1 | some .b2 => false
    | some .b3 => true

/-- Realized claims preserve their episode time; current recovery erases no history. -/
def frame (fragile : Bool) : Frame State Repair Claim where
  P := process fragile
  realized s c := episodeTime c ≤ s.clock ∧ s.backbone = true ∧ protects s.repair c = true

instance decidableRealized (fragile : Bool) (s : State) (c : Claim) :
    Decidable ((frame fragile).realized s c) :=
  inferInstanceAs (Decidable (episodeTime c ≤ s.clock ∧ s.backbone = true ∧ protects s.repair c = true))

def outageAt (t : Nat) : Life → Bool
  | .p => t == 1 || t == 3
  | .q | .r | .s => t == 1

def firstEpisodeOf : Life → Claim
  | .p => .first
  | .q => .q
  | .r => .r
  | .s => .s

/-- A supplied availability law: outside the specified fault episodes the common
backbone supplies support; during an episode the installed repair is needed. -/
def availableNow (s : State) (life : Life) : Bool :=
  s.backbone && (if outageAt s.clock life then protects s.repair (firstEpisodeOf life) else true)

/-- Actual availability now, not a vacuous statement about absent demand. -/
def supportedNow (s : State) (life : Life) : Prop := availableNow s life = true

instance decidableSupportedNow (s : State) (life : Life) : Decidable (supportedNow s life) :=
  inferInstanceAs (Decidable (availableNow s life = true))

def finalState (fragile : Bool) (r : Repair) : State := states fragile r 4

theorem common_start (fragile : Bool) (r : Repair) : (run fragile r).state 0 = start := rfl

theorem generated_trace (fragile : Bool) (r : Repair) :
    Trace (frame fragile).P start ((run fragile r).window 0 4) (finalState fragile r) := by
  exact (run fragile r).window_trace 4 0

theorem separated_same_life :
    lifeOf .first = lifeOf .second ∧ episodeTime .first = 1 ∧ episodeTime .second = 3 :=
  ⟨rfl, rfl, rfl⟩

theorem support_between_episodes (r : Repair) (life : Life) :
    supportedNow (states false r 2) life := by
  cases r <;> cases life <;> decide

theorem current_support_restored (r : Repair) (life : Life) :
    supportedNow (finalState false r) life := by
  cases r <;> cases life <;> decide

/-- The retained episode claim reads actual support at that episode in the same
produced course. Lives differentiate positions; they are not values to be summed. -/
theorem historical_claim_iff_support (fragile : Bool) (r : Repair) (c : Claim) (life : Life) :
    lifeOf c = some life →
    ((frame fragile).realized (finalState fragile r) c ↔
      supportedNow (states fragile r (episodeTime c)) life) := by
  cases fragile <;> cases r <;> cases c <;> cases life <;> decide

theorem recovery_retains_loss :
    supportedNow (finalState false .b3) .p ∧
    ¬ (frame false).realized (finalState false .b3) .first ∧
    ¬ (frame false).realized (finalState false .b3) .second := by decide

/-- The five episode contents are treated alike; backbone loss is distinct.
Actual adequacy of this reading is NOT established by its definition. -/
def sameEpisode (a b : Claim) : Prop :=
  (a = .backbone ∧ b = .backbone) ∨ (a ≠ .backbone ∧ b ≠ .backbone)

instance decidableSameEpisode (a b : Claim) : Decidable (sameEpisode a b) :=
  inferInstanceAs (Decidable ((a = .backbone ∧ b = .backbone) ∨
    (a ≠ .backbone ∧ b ≠ .backbone)))

def toB1 : Claim → Claim
  | .first => .first
  | .second => .second
  | .q => .first
  | .r => .r
  | .s => .s
  | .backbone => .backbone

theorem a_matches_b1 :
    (frame false).StrictLossMatch sameEpisode (finalState false .a) (finalState false .b1) := by
  refine ⟨toB1, ?_, ?_, ?_, .second, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c; cases c <;> decide
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def toA : Claim → Claim
  | .first => .q
  | .second => .r
  | .q => .q
  | .r => .r
  | .s => .s
  | .backbone => .backbone

theorem b3_matches_a :
    (frame false).StrictLossMatch sameEpisode (finalState false .b3) (finalState false .a) := by
  refine ⟨toA, ?_, ?_, ?_, .s, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c; cases c <;> decide
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def swapB2 : Claim → Claim
  | .first => .q
  | .second => .r
  | .q => .first
  | .r => .second
  | .s => .s
  | .backbone => .backbone

theorem b2_loss_correspondence (c : Claim) :
    (¬ (frame false).realized (finalState false .a) c) ↔
    ¬ (frame false).realized (finalState false .b2) (swapB2 c) := by
  cases c <;> decide

theorem b2_correspondence_involutive (c : Claim) : swapB2 (swapB2 c) = c := by
  cases c <;> rfl

/-- The ethical bridge is supplied; scope carries full-content, permission,
history and support correspondence. Strict matching alone does not justify it. -/
def SufficientMatching (scope : State → State → Prop) (Le : State → State → Prop) : Prop :=
  ∀ better worse, scope better worse →
    (frame false).StrictLossMatch sameEpisode better worse → Strict Le worse better

theorem conditional_lower_anchor {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le)
    (adequate : scope (finalState false .a) (finalState false .b1)) :
    Strict Le (finalState false .b1) (finalState false .a) :=
  sufficient _ _ adequate a_matches_b1

theorem conditional_upper_anchor {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le)
    (adequate : scope (finalState false .b3) (finalState false .a)) :
    Strict Le (finalState false .a) (finalState false .b3) :=
  sufficient _ _ adequate b3_matches_a

/-- The lower and upper anchors give a strict outer comparison only under the
existing explicitly supplied transitivity condition. -/
theorem conditional_outer_order {scope Le : State → State → Prop}
    (sufficient : SufficientMatching scope Le) (trans : Transitive Le)
    (lower : scope (finalState false .a) (finalState false .b1))
    (upper : scope (finalState false .b3) (finalState false .a)) :
    Strict Le (finalState false .b1) (finalState false .b3) :=
  strict_improvement_transport trans (conditional_lower_anchor sufficient lower)
    (conditional_upper_anchor sufficient upper).1

theorem fragile_b3_loses_backbone :
    ¬ (frame true).realized (finalState true .b3) .backbone := by decide

theorem fragile_a_keeps_backbone :
    (frame true).realized (finalState true .a) .backbone := by decide

/-- The very same episode counts cannot certify the larger repair when its actual
operation severs common support. No historical life is grouped away. -/
theorem fragile_b3_not_matching :
    ¬ (frame true).StrictLossMatch sameEpisode (finalState true .b3) (finalState true .a) := by
  intro matched
  obtain ⟨image, losses, contents, _⟩ := matched
  have related := contents .backbone fragile_b3_loses_backbone
  have imageIs : image .backbone = .backbone := by
    cases related with
    | inl same => exact same.2
    | inr different => exact False.elim (different.1 rfl)
  have missing := losses .backbone fragile_b3_loses_backbone
  rw [imageIs] at missing
  exact missing fragile_a_keeps_backbone


/-! ## The constructed process as an instance of the general laws -/

section Instances

open Frame

def allClaims : List Claim := [.first, .second, .q, .r, .s, .backbone]

theorem allClaims_distinct : Distinct allClaims :=
  @of_decide_eq_true _ (LossMatching.decideDistinct allClaims) rfl

theorem allClaims_every : ∀ c, c ∈ allClaims
  | .first => .head _
  | .second => .tail _ (.head _)
  | .q => .tail _ (.tail _ (.head _))
  | .r => .tail _ (.tail _ (.tail _ (.head _)))
  | .s => .tail _ (.tail _ (.tail _ (.tail _ (.head _))))
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
    lostCount .a = 3 ∧ lostCount .b1 = 4 ∧ lostCount .b2 = 3 ∧ lostCount .b3 = 2 := by
  decide

/-- `a_matches_b1` and `b3_matches_a` recovered from the general law. -/
theorem a_matches_b1_by_count :
    (frame false).StrictLossMatch sameEpisode (finalState false .a) (finalState false .b1) :=
  (matches_iff .a .b1).mpr (by decide)

theorem b3_matches_a_by_count :
    (frame false).StrictLossMatch sameEpisode (finalState false .b3) (finalState false .a) :=
  (matches_iff .b3 .a).mpr (by decide)

/-- `b2` against `a`: equal counts, no strict match either way (the loss correspondence of
`b2_loss_correspondence` is all there is). -/
theorem b2_a_neither :
    ¬ (frame false).StrictLossMatch sameEpisode (finalState false .b2) (finalState false .a) ∧
    ¬ (frame false).StrictLossMatch sameEpisode (finalState false .a) (finalState false .b2) :=
  ⟨fun m => (by decide : ¬ lostCount .b2 < lostCount .a) ((matches_iff .b2 .a).mp m),
   fun m => (by decide : ¬ lostCount .a < lostCount .b2) ((matches_iff .a .b2).mp m)⟩

/-- The converse of `strictLossMatch_of_extension` fails: the lower anchor is a strict loss
match that is no generative extension (course `a` loses `q`, which course `b1` keeps). -/
theorem a_b1_not_extension (living : Claim → Prop) :
    ¬ Extension (frame false) living (finalState false .b1) (finalState false .a) :=
  fun ⟨keeps, _⟩ => (by decide : ¬ (frame false).realized (finalState false .a) .q)
    (keeps .q (by decide))

/-- The fragile control from the general common-support law: every claim rests on the
backbone, so the fragile course `b3` is strictly matched below no course, under any
content relation. -/
theorem fragile_b3_below_nothing (same : Claim → Claim → Prop) (w : State) :
    ¬ (frame true).StrictLossMatch same (finalState true .b3) w :=
  not_strictLossMatch_of_base_lost (F := frame true) (base := .backbone)
    (fun (s : State) (c : Claim) (realized : (frame true).realized s c) =>
      (⟨Nat.zero_le _, realized.2.1, rfl⟩ : (frame true).realized s .backbone))
    allClaims_distinct allClaims_every fragile_b3_loses_backbone w

/-- The sufficiency commitment of this application is the general one on this frame. -/
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

theorem episodeTime_pos : ∀ (c : Claim) (life : Life), lifeOf c = some life → 0 < episodeTime c
  | .first, _, _ => Nat.succ_pos 0
  | .second, _, _ => Nat.succ_pos 2
  | .q, _, _ => Nat.succ_pos 0
  | .r, _, _ => Nat.succ_pos 0
  | .s, _, _ => Nat.succ_pos 0
  | .backbone, _, ofLife => nomatch ofLife

/-- **Every episode claim is read at its episode time** along every course: from then on it
is realized exactly where its life had support at that time (the general `ReadsAt`). -/
theorem reads_at_episode (fragile : Bool) (r : Repair) (c : Claim) (life : Life)
    (ofLife : lifeOf c = some life) :
    (frame fragile).ReadsAt (run fragile r) c (episodeTime c) (fun s _ => supportedNow s life) :=
  fun t le => match t, le with
  | 0, le => absurd (episodeTime_pos c life ofLife) (Nat.not_lt_of_le le)
  | t + 1, le =>
    (realized_succ fragile r c t).trans
      ((⟨fun h => ⟨episode_le_four c, h.2⟩, fun h => ⟨le, h.2⟩⟩ :
          (episodeTime c ≤ t + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true) ↔
          (episodeTime c ≤ 3 + 1 ∧ backboneAfter fragile r = true ∧ protects (some r) c = true)).trans
        ((realized_succ fragile r c 3).symm.trans (historical_claim_iff_support fragile r c life ofLife)))

/-- `recovery_retains_loss` at every later step, from the general law: the episodes of `p`
missed under repair `b3` stay lost whatever support returns. -/
theorem p_losses_retained (t : Nat) (le : 3 ≤ t) :
    ¬ (frame false).realized ((run false .b3).state t) .first ∧
    ¬ (frame false).realized ((run false .b3).state t) .second :=
  ⟨(reads_at_episode false .b3 .first .p rfl).loss_retained (by decide)
      (Nat.le_trans (by decide) le),
   (reads_at_episode false .b3 .second .p rfl).loss_retained (by decide) le⟩

end Instances

end RepairComparison
end Becoming
