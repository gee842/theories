import PotentialTruth

/-!
Future witness coverage and its precise uniform existential test.
The converse tests all ambient unary predicates, not one fixed language.
A finite branching frame separates coverage somewhere from coverage in every
future cone, while retaining increasing domains and fixed interpretations.
-/
namespace CoverageBoundary
open PotentialTruth
universe u v
variable {A : Type u} {W : Type v}

def FutureExists (F : Frame A W) (w : W) (P : A → Prop) : Prop :=
  ∃ x, F.future w x ∧ ∃ a, F.domain x a ∧ P a

theorem future_exists_agreement (F : Frame A W) (hc : FutureCoverage F)
    (w : W) (P : A → Prop) : FutureExists F w P ↔ ∃ a, P a := by
  constructor
  · rintro ⟨_, _, a, _, ha⟩
    exact ⟨a, ha⟩
  · rintro ⟨a, ha⟩
    obtain ⟨x, hwx, hax⟩ := hc w a
    exact ⟨x, hwx, a, hax, ha⟩

theorem coverage_iff_all_unary_existentials (F : Frame A W) :
    FutureCoverage F ↔ ∀ w (P : A → Prop), (FutureExists F w P ↔ ∃ a, P a) := by
  constructor
  · exact fun hc => future_exists_agreement F hc
  · intro h w a
    obtain ⟨x, hwx, b, hbx, hba⟩ := (h w (fun b => b = a)).mpr ⟨a, rfl⟩
    exact ⟨x, hwx, hba ▸ hbx⟩

def GlobalCoverage (F : Frame A W) : Prop := ∀ a, ∃ w, F.domain w a

def JointExtensions (F : Frame A W) : Prop :=
  ∀ w x, ∃ y, F.future w y ∧ F.future x y

theorem coverage_of_joint_extensions (F : Frame A W)
    (hg : GlobalCoverage F) (hj : JointExtensions F) : FutureCoverage F := by
  intro w a
  obtain ⟨x, hax⟩ := hg a
  obtain ⟨y, hwy, hxy⟩ := hj w x
  exact ⟨y, hwy, F.monotone hxy hax⟩

inductive Fork where
  | start | left | right
  deriving DecidableEq

def forkFuture : Fork → Fork → Prop
  | .start, _ => True
  | .left, .left => True
  | .right, .right => True
  | _, _ => False

def forkDomain : Fork → Bool → Prop
  | .start, _ => False
  | .left, a => a = false
  | .right, a => a = true

def forkFrame : Frame Bool Fork where
  future := forkFuture
  domain := forkDomain
  refl w := by cases w <;> trivial
  trans := by intro w x y; cases w <;> cases x <;> cases y <;> simp [forkFuture]
  monotone := by intro w x a; cases w <;> cases x <;> simp [forkFuture, forkDomain]

theorem fork_global_coverage : GlobalCoverage forkFrame := by
  intro a
  cases a with
  | false => exact ⟨.left, rfl⟩
  | true => exact ⟨.right, rfl⟩

theorem fork_every_value_from_start : ∀ a, ∃ x, forkFrame.future .start x ∧ forkFrame.domain x a := by
  intro a
  obtain ⟨x, hx⟩ := fork_global_coverage a
  exact ⟨x, True.intro, hx⟩

theorem fork_left_misses_true : ¬ FutureExists forkFrame .left (fun a => a = true) := by
  rintro ⟨w, hw, a, ha, hp⟩
  cases w with
  | start => exact hw
  | left =>
    change a = false at ha
    cases ha
    cases hp
  | right => exact hw

theorem fork_not_future_coverage : ¬ FutureCoverage forkFrame := by
  intro hc
  exact fork_left_misses_true ((future_exists_agreement forkFrame hc .left _).mpr ⟨true, rfl⟩)

theorem fork_not_joint_extensions : ¬ JointExtensions forkFrame :=
  fun hj => fork_not_future_coverage (coverage_of_joint_extensions forkFrame fork_global_coverage hj)

def emptyInterpretation : Interpretation (fun _ => Empty) Bool := fun _ r => nomatch r

def anotherValue : Formula (fun _ => Empty) 0 :=
  .all (.ex (.neg (.eq 0 1)))

theorem another_global_true : sat emptyInterpretation anotherValue (emptyAssignment Bool) := by
  intro a
  cases a with
  | false => exact ⟨true, by change true ≠ false; decide⟩
  | true => exact ⟨false, by change false ≠ true; decide⟩

theorem another_potential_false_at_start :
    ¬ potentialSat forkFrame emptyInterpretation anotherValue .start (emptyAssignment Bool) := by
  intro h
  obtain ⟨w, hw, a, ha, hne⟩ := h .left True.intro false rfl
  cases w with
  | start => exact hw
  | left =>
    change a = false at ha
    exact hne ha
  | right => exact hw

end CoverageBoundary
