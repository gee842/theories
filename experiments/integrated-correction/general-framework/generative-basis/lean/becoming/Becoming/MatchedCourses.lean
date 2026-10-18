import Becoming.LossMatching
import Becoming.StrictTransport

/-!
# Matched courses: loss matching between the courses of one constructed process

One constructed process produces four courses from one start. Each course installs one of four
moves once (`Move`); a move covers some of the claims of four positions (`Position`), and every
claim rests on a common base. Claim `first` and claim `second` are two times of position `p`;
`q`, `r` and `s` are the claims of the other positions. A claim is realized once its time has
come, while the base holds and the installed move covers it, so a claim missed at its time stays
missed after support returns. Board item F3R (18 October 2026) states here, in the core's names,
what the bridge module `RepairComparison` stated of this process (its group (e) of the fold
study, kept in the bridge by F1's decision 1 because its names were an application's): moves
`a`, `b1`, `b2`, `b3` were repairs, positions were lives, claims at their time were episodes,
and the base was a backbone.

**The reading is a premise, not a definition.** `RepairComparison` read the five non-base
claims as complete comparable basic losses by defining one content relation (`sameEpisode`).
Here every comparison theorem takes an arbitrary content relation `same` with the premise that
it relates the non-base claims (`BasicAlike`), and, where the base matters, that it relates the
base only to itself (`BaseApart`). Sufficiency of matching is the core's
`Frame.SufficientMatching`, a hypothesis of the anchors, as in `Becoming.LossMatching`.

* **The course.** All courses start alike (`common_start`), their windows are traces
  (`generated_trace`); in the course without the fragile base, support holds between the two
  times of `p` and returns at the end (`support_between`, `support_restored`), and each claim at
  the end reads support at its time (`claim_iff_support`, `reads_at_time`), so the claims of `p`
  missed under `b3` stay missed (`recovery_retains_loss`, `first_losses_retained`).
* **Matching.** Under `BasicAlike`, `a` matches `b1` strictly and `b3` matches `a`
  (`a_matches_b1`, `b3_matches_a`); `b2` and `a` lose corresponding claims
  (`b2_loss_correspondence`) and neither matches the other (`b2_a_neither`). These are the
  counting law of `Becoming.LossMatching` at this frame: a strict match exists exactly when the
  better course loses fewer claims (`matches_iff`, `lost_counts`).
* **Anchors under sufficiency.** With sufficiency of matching for a supplied comparison and the
  pairs in its scope, `a` is strictly above `b1` and `b3` strictly above `a`
  (`conditional_lower_anchor`, `conditional_upper_anchor`), and with transitivity `b3` is
  strictly above `b1` (`conditional_outer_order`).
* **The base.** If `b3` cuts the base, it loses the base claim (`fragile_b3_loses_base`), so it
  matches no course under any content relation (`fragile_b3_matches_nothing`), and under
  `BaseApart` it does not match `a`, which keeps the base (`fragile_b3_not_matching`). The lower
  anchor is a strict match without extension (`a_b1_not_extension`).

No ethical premise is asserted; the reading of the claims and the sufficiency of matching are
hypotheses. Every declaration has an empty axiom report.
-/

namespace Becoming

namespace MatchedCourses

open Generative StrictTransport Frame

/-- The four moves. -/
inductive Move where
  | a | b1 | b2 | b3
  deriving DecidableEq

/-- The four positions. -/
inductive Position where
  | p | q | r | s
  deriving DecidableEq

/-- Two times of `p`, the claims of `q`, `r`, `s`, and the base. -/
inductive Claim where
  | first | second | q | r | s | base
  deriving DecidableEq

/-- Time, the installed move, and whether the base holds. -/
structure State where
  clock : Nat
  installed : Option Move
  base : Bool

def start : State := ⟨0, none, true⟩

/-- Under the fragile law, move `b3` cuts the base. -/
def baseAfter (fragile : Bool) : Move → Bool
  | .a => true
  | .b1 => true
  | .b2 => true
  | .b3 => !fragile

/-- A move is installed once; later steps keep it and advance time. -/
def advance (fragile : Bool) (s : State) (m : Move) : State :=
  match s.installed with
  | none => ⟨s.clock + 1, some m, s.base && baseAfter fragile m⟩
  | some old => ⟨s.clock + 1, some old, s.base⟩

def process (fragile : Bool) : Process State Move := ⟨fun s m t => t = advance fragile s m⟩

def states (fragile : Bool) (m : Move) : Nat → State
  | 0 => start
  | t + 1 => advance fragile (states fragile m t) m

def run (fragile : Bool) (m : Move) : Run (process fragile) where
  state := states fragile m
  act _ := m
  step _ := rfl

/-- The time of each claim. -/
def time : Claim → Nat
  | .first | .q | .r | .s => 1
  | .second => 3
  | .base => 0

/-- The position of each claim. -/
def positionOf : Claim → Option Position
  | .first | .second => some .p
  | .q => some .q
  | .r => some .r
  | .s => some .s
  | .base => none

/-- Which claims an installed move covers. -/
def covers (m : Option Move) : Claim → Bool
  | .base => true
  | .first | .second => match m with
    | none => false
    | some .a => true
    | some .b1 | some .b2 | some .b3 => false
  | .q => match m with
    | none | some .a => false
    | some .b1 | some .b2 | some .b3 => true
  | .r => match m with
    | none | some .a | some .b1 => false
    | some .b2 | some .b3 => true
  | .s => match m with
    | none | some .a | some .b1 | some .b2 => false
    | some .b3 => true

/-- A claim is realized once its time has come, while the base holds and the move covers it. -/
def frame (fragile : Bool) : Frame State Move Claim where
  P := process fragile
  realized s c := time c ≤ s.clock ∧ s.base = true ∧ covers s.installed c = true

instance decidableRealized (fragile : Bool) (s : State) (c : Claim) :
    Decidable ((frame fragile).realized s c) :=
  inferInstanceAs (Decidable (time c ≤ s.clock ∧ s.base = true ∧ covers s.installed c = true))

/-- The gaps in support of each position. -/
def gapAt (t : Nat) : Position → Bool
  | .p => t == 1 || t == 3
  | .q | .r | .s => t == 1

def firstClaimOf : Position → Claim
  | .p => .first
  | .q => .q
  | .r => .r
  | .s => .s

/-- Outside its gaps a position has the base's support; in a gap it needs the move. -/
def supportedAt (s : State) (pos : Position) : Bool :=
  s.base && (if gapAt s.clock pos then covers s.installed (firstClaimOf pos) else true)

/-- Support now. -/
def Supported (s : State) (pos : Position) : Prop := supportedAt s pos = true

instance decidableSupported (s : State) (pos : Position) : Decidable (Supported s pos) :=
  inferInstanceAs (Decidable (supportedAt s pos = true))

def final (fragile : Bool) (m : Move) : State := states fragile m 4

/-- The content relation relates the non-base claims: the reading of them as alike losses. -/
def BasicAlike (same : Claim → Claim → Prop) : Prop :=
  ∀ c d, c ≠ .base → d ≠ .base → same c d

/-- The content relation relates the base only to itself. -/
def BaseApart (same : Claim → Claim → Prop) : Prop := ∀ d, same .base d → d = .base

/-! ## The course -/

theorem common_start (fragile : Bool) (m : Move) : (run fragile m).state 0 = start := rfl

theorem generated_trace (fragile : Bool) (m : Move) :
    Trace (frame fragile).P start ((run fragile m).window 0 4) (final fragile m) :=
  (run fragile m).window_trace 4 0

theorem separated_same_position :
    positionOf .first = positionOf .second ∧ time .first = 1 ∧ time .second = 3 := ⟨rfl, rfl, rfl⟩

theorem support_between (m : Move) (pos : Position) : Supported (states false m 2) pos := by
  cases m <;> cases pos <;> decide

theorem support_restored (m : Move) (pos : Position) : Supported (final false m) pos := by
  cases m <;> cases pos <;> decide

/-- **The claim at the end reads support at its time** in the same course. -/
theorem claim_iff_support (fragile : Bool) (m : Move) (c : Claim) (pos : Position) :
    positionOf c = some pos →
      ((frame fragile).realized (final fragile m) c ↔ Supported (states fragile m (time c)) pos) := by
  cases fragile <;> cases m <;> cases c <;> cases pos <;> decide

theorem recovery_retains_loss :
    Supported (final false .b3) .p ∧ ¬ (frame false).realized (final false .b3) .first ∧
      ¬ (frame false).realized (final false .b3) .second := by decide

/-! ## Matching under the reading -/

def matchB1 : Claim → Claim
  | .first => .first
  | .second => .second
  | .q => .first
  | .r => .r
  | .s => .s
  | .base => .base

/-- **Under the reading, `a` matches `b1` strictly.** -/
theorem a_matches_b1 {same : Claim → Claim → Prop} (alike : BasicAlike same) :
    (frame false).StrictLossMatch same (final false .a) (final false .b1) := by
  refine ⟨matchB1, ?_, ?_, ?_, .second, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c lost
    cases c <;> first
      | exact (lost (by decide)).elim
      | exact alike _ _ (by decide) (by decide)
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def matchA : Claim → Claim
  | .first => .q
  | .second => .r
  | .q => .q
  | .r => .r
  | .s => .s
  | .base => .base

/-- **Under the reading, `b3` matches `a` strictly.** -/
theorem b3_matches_a {same : Claim → Claim → Prop} (alike : BasicAlike same) :
    (frame false).StrictLossMatch same (final false .b3) (final false .a) := by
  refine ⟨matchA, ?_, ?_, ?_, .s, ?_, ?_⟩
  · intro c; cases c <;> decide
  · intro c lost
    cases c <;> first
      | exact (lost (by decide)).elim
      | exact alike _ _ (by decide) (by decide)
  · intro c d; cases c <;> cases d <;> decide
  · decide
  · intro c; cases c <;> decide

def swapB2 : Claim → Claim
  | .first => .q
  | .second => .r
  | .q => .first
  | .r => .second
  | .s => .s
  | .base => .base

theorem b2_loss_correspondence (c : Claim) :
    (¬ (frame false).realized (final false .a) c) ↔
      ¬ (frame false).realized (final false .b2) (swapB2 c) := by
  cases c <;> decide

theorem b2_correspondence_involutive (c : Claim) : swapB2 (swapB2 c) = c := by cases c <;> rfl

/-! ## Anchors under sufficiency -/

theorem conditional_lower_anchor {same : Claim → Claim → Prop} (alike : BasicAlike same)
    {scope Le : State → State → Prop} (sufficient : (frame false).SufficientMatching same scope Le)
    (adequate : scope (final false .a) (final false .b1)) :
    Strict Le (final false .b1) (final false .a) :=
  sufficient _ _ adequate (a_matches_b1 alike)

theorem conditional_upper_anchor {same : Claim → Claim → Prop} (alike : BasicAlike same)
    {scope Le : State → State → Prop} (sufficient : (frame false).SufficientMatching same scope Le)
    (adequate : scope (final false .b3) (final false .a)) :
    Strict Le (final false .a) (final false .b3) :=
  sufficient _ _ adequate (b3_matches_a alike)

/-- **The two anchors give the outer strict comparison under transitivity.** -/
theorem conditional_outer_order {same : Claim → Claim → Prop} (alike : BasicAlike same)
    {scope Le : State → State → Prop} (sufficient : (frame false).SufficientMatching same scope Le)
    (trans : Transitive Le) (lower : scope (final false .a) (final false .b1))
    (upper : scope (final false .b3) (final false .a)) :
    Strict Le (final false .b1) (final false .b3) :=
  strict_above_trans trans (conditional_lower_anchor alike sufficient lower)
    (conditional_upper_anchor alike sufficient upper).1

/-! ## The base -/

theorem fragile_b3_loses_base : ¬ (frame true).realized (final true .b3) .base := by decide

theorem fragile_a_keeps_base : (frame true).realized (final true .a) .base := by decide

/-- **Where the content relation keeps the base apart, the fragile `b3` does not match `a`.** -/
theorem fragile_b3_not_matching {same : Claim → Claim → Prop} (apart : BaseApart same) :
    ¬ (frame true).StrictLossMatch same (final true .b3) (final true .a)
  | ⟨image, losses, contents, _⟩ =>
    have imageIs : image .base = .base := apart _ (contents .base fragile_b3_loses_base)
    (imageIs ▸ losses .base fragile_b3_loses_base) fragile_a_keeps_base

/-! ## The counting law at this frame -/

def allClaims : List Claim := [.first, .second, .q, .r, .s, .base]

theorem allClaims_distinct : Distinct allClaims :=
  @of_decide_eq_true _ (LossMatching.decideDistinct allClaims) rfl

theorem allClaims_every : ∀ c, c ∈ allClaims
  | .first => .head _
  | .second => .tail _ (.head _)
  | .q => .tail _ (.tail _ (.head _))
  | .r => .tail _ (.tail _ (.tail _ (.head _)))
  | .s => .tail _ (.tail _ (.tail _ (.tail _ (.head _))))
  | .base => .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))

theorem listed (fragile : Bool) (m : Move) :
    (frame fragile).LossesListed (final fragile m) ((frame fragile).lostOf (final fragile m) allClaims) :=
  lossesListed_lostOf allClaims_distinct allClaims_every

def lostCount (m : Move) : Nat := ((frame false).lostOf (final false m) allClaims).length

theorem lost_not_base (m : Move) :
    ∀ c, ¬ (frame false).realized (final false m) c → c ≠ .base := by
  intro c; cases m <;> cases c <;> decide

/-- With the base kept, every loss is a non-base claim, so the reading relates all losses. -/
theorem losses_alike {same : Claim → Claim → Prop} (alike : BasicAlike same) (x y : Move) :
    ∀ c d, ¬ (frame false).realized (final false x) c →
      ¬ (frame false).realized (final false y) d → same c d :=
  fun c d lc ld => alike c d (lost_not_base x c lc) (lost_not_base y d ld)

/-- **The counting law at this frame**: under the reading, a strict match between two courses
exists exactly when the better loses fewer claims. -/
theorem matches_iff {same : Claim → Claim → Prop} (alike : BasicAlike same) (x y : Move) :
    (frame false).StrictLossMatch same (final false x) (final false y) ↔ lostCount x < lostCount y :=
  strictLossMatch_iff_length_of_alike (listed false x) (listed false y) (losses_alike alike x y)

theorem lost_counts : lostCount .a = 3 ∧ lostCount .b1 = 4 ∧ lostCount .b2 = 3 ∧ lostCount .b3 = 2 := by
  decide

/-- **`b2` and `a` lose as many claims; neither matches the other.** -/
theorem b2_a_neither {same : Claim → Claim → Prop} (alike : BasicAlike same) :
    ¬ (frame false).StrictLossMatch same (final false .b2) (final false .a) ∧
      ¬ (frame false).StrictLossMatch same (final false .a) (final false .b2) :=
  ⟨fun m => (by decide : ¬ lostCount .b2 < lostCount .a) ((matches_iff alike .b2 .a).mp m),
   fun m => (by decide : ¬ lostCount .a < lostCount .b2) ((matches_iff alike .a .b2).mp m)⟩

/-- **The lower anchor is a strict match without extension**: `a` loses `q`, which `b1` keeps. -/
theorem a_b1_not_extension (living : Claim → Prop) :
    ¬ Extension (frame false) living (final false .b1) (final false .a) :=
  fun ⟨keeps, _⟩ => (by decide : ¬ (frame false).realized (final false .a) .q) (keeps .q (by decide))

/-- **The fragile `b3` matches no course under any content relation**: every claim rests on the
base, which it loses (`not_strictLossMatch_of_base_lost`). -/
theorem fragile_b3_matches_nothing (same : Claim → Claim → Prop) (w : State) :
    ¬ (frame true).StrictLossMatch same (final true .b3) w :=
  not_strictLossMatch_of_base_lost (F := frame true) (base := .base)
    (fun (s : State) (c : Claim) (realized : (frame true).realized s c) =>
      (⟨Nat.zero_le _, realized.2.1, rfl⟩ : (frame true).realized s .base))
    allClaims_distinct allClaims_every fragile_b3_loses_base w

/-! ## Claims are read at their time -/

theorem states_succ (fragile : Bool) (m : Move) :
    ∀ t, states fragile m (t + 1) = ⟨t + 1, some m, baseAfter fragile m⟩
  | 0 => rfl
  | t + 1 => congrArg (fun s => advance fragile s m) (states_succ fragile m t)

theorem realized_succ (fragile : Bool) (m : Move) (c : Claim) (t : Nat) :
    (frame fragile).realized (states fragile m (t + 1)) c ↔
      (time c ≤ t + 1 ∧ baseAfter fragile m = true ∧ covers (some m) c = true) :=
  Eq.subst (motive := fun s => (frame fragile).realized s c ↔
      (time c ≤ t + 1 ∧ baseAfter fragile m = true ∧ covers (some m) c = true))
    (states_succ fragile m t).symm Iff.rfl

theorem time_le_four : ∀ c : Claim, time c ≤ 4 := by intro c; cases c <;> decide

theorem time_pos : ∀ (c : Claim) (pos : Position), positionOf c = some pos → 0 < time c
  | .first, _, _ => Nat.succ_pos 0
  | .second, _, _ => Nat.succ_pos 2
  | .q, _, _ => Nat.succ_pos 0
  | .r, _, _ => Nat.succ_pos 0
  | .s, _, _ => Nat.succ_pos 0
  | .base, _, ofPos => nomatch ofPos

/-- **Every claim of a position is read at its time** along every course (`Frame.ReadsAt`). -/
theorem reads_at_time (fragile : Bool) (m : Move) (c : Claim) (pos : Position)
    (ofPos : positionOf c = some pos) :
    (frame fragile).ReadsAt (run fragile m) c (time c) (fun s _ => Supported s pos) :=
  fun t le => match t, le with
  | 0, le => absurd (time_pos c pos ofPos) (Nat.not_lt_of_le le)
  | t + 1, le =>
    (realized_succ fragile m c t).trans
      ((⟨fun h => ⟨time_le_four c, h.2⟩, fun h => ⟨le, h.2⟩⟩ :
          (time c ≤ t + 1 ∧ baseAfter fragile m = true ∧ covers (some m) c = true) ↔
          (time c ≤ 3 + 1 ∧ baseAfter fragile m = true ∧ covers (some m) c = true)).trans
        ((realized_succ fragile m c 3).symm.trans (claim_iff_support fragile m c pos ofPos)))

/-- **The claims of `p` missed under `b3` stay missed** at every later step, whatever support
returns. -/
theorem first_losses_retained (t : Nat) (le : 3 ≤ t) :
    ¬ (frame false).realized ((run false .b3).state t) .first ∧
      ¬ (frame false).realized ((run false .b3).state t) .second :=
  ⟨(reads_at_time false .b3 .first .p rfl).loss_retained (by decide) (Nat.le_trans (by decide) le),
   (reads_at_time false .b3 .second .p rfl).loss_retained (by decide) le⟩

end MatchedCourses

end Becoming
