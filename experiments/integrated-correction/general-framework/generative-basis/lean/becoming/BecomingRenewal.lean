import BecomingFrame
import RelationalRenewal

/-!
# Renewal and consumption on runs

The relational classification of `RelationalRenewal` reads one unfolding through the
levels of conditions of further formation and the formations depending on them or
drawing on them. On the spine these are observables of configurations, so every run
of every process carries the classification: `Conditions.along` reads a run as a
`RelationalRenewal.Unfolding`, and every theorem of that module applies to it.

One principle bounds continuation without renewal: an observable that never rises
from some step on falls only finitely often. Three bounds proved separately before
are its cases along a run:
* depletion (`Depletion`): if every step lowers a reserve, no run exists;
* recurrent renewal (`ContinuationRenewal`, natural-number rank): if every step
  that is not a renewal lowers a rank, renewal recurs arbitrarily late;
* unrenewed drawdown (`RelationalRenewal`): a formation lowering an unrenewed
  condition at each active step is active only finitely often.
`ContinuationRenewal` also has a well-founded form, more general than the
natural-number rank used here.

The class belongs to the run, not to a configuration or to the formation's own
activity: in one process, from one configuration, with the focal formation active at
every step of both runs, one run renews and the other consumes.

No ethical predicate, ranking or axiom occurs. Which observables represent an actual
history is an application duty. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative RelationalRenewal

universe u v

variable {S : Type u} {A : Type v}

/-! ## Conditions as observables of configurations -/

/-- Levels of conditions of further formation at each configuration, the formations
active there, and which conditions each formation's continuation depends on (at what
level) and its activity draws on. -/
structure Conditions (S : Type u) (F C : Type) where
  level : S → C → Nat
  active : S → F → Prop
  requires : F → C → Prop
  need : F → C → Nat
  draws : F → C → Prop

/-- A run read through its conditions is one relational unfolding. -/
def Conditions.along {F C : Type} (K : Conditions S F C) {P : Process S A} (r : Run P) :
    Unfolding F C :=
  ⟨fun t => K.level (r.state t), fun t => K.active (r.state t), K.requires, K.need, K.draws⟩

/-! ## Continuation without renewal -/

/-- An observable that never rises from step `T` on falls only finitely often. -/
theorem falls_finitely (rank : Nat → Nat) (T : Nat)
    (noRise : ∀ n, T ≤ n → rank (n + 1) ≤ rank n) :
    ¬ ∀ N, ∃ n, N ≤ n ∧ rank (n + 1) < rank n :=
  unrenewed_drawdown_finite
    ⟨fun t _ => rank t, fun t _ => rank (t + 1) < rank t,
      fun _ _ => False, fun _ _ => 0, fun _ _ => False⟩ () () T noRise (fun _ _ falls => falls)

/-- Depletion: if every admissible step lowers a reserve, no run exists. -/
theorem Run.not_of_depletion {P : Process S A} (reserve : S → Nat)
    (lowers : ∀ s a t, P.step s a t → reserve t < reserve s) (r : Run P) : False :=
  falls_finitely (fun n => reserve (r.state n)) 0
    (fun n _ => Nat.le_of_lt (lowers _ _ _ (r.step n)))
    (fun N => ⟨N, Nat.le_refl N, lowers _ _ _ (r.step N)⟩)

/-- `Depletion.no_infinite_execution_under_depletion`, derived from the principle. -/
theorem no_execution_of_depletion {P : Process S A} (reserve : S → Nat)
    (lowers : ∀ s a t, P.step s a t → reserve t < reserve s) :
    ¬ ∃ states : Nat → S, ∃ actions : Nat → A,
      ∀ n, P.step (states n) (actions n) (states (n + 1))
  | ⟨states, actions, steps⟩ => Run.not_of_depletion reserve lowers ⟨states, actions, steps⟩

/-- Recurrent renewal: if every step that is not a renewal lowers a rank, no tail of a
run is free of renewal. -/
theorem Run.renewal_recurs {P : Process S A} (r : Run P) (rank : S → Nat)
    (renewal : Nat → Prop)
    (lowers : ∀ n, ¬ renewal n → rank (r.state (n + 1)) < rank (r.state n))
    (start : Nat) : ¬ ∀ n, start ≤ n → ¬ renewal n :=
  fun free => falls_finitely (fun n => rank (r.state n)) start
    (fun n after => Nat.le_of_lt (lowers n (free n after)))
    (fun N => ⟨N + start, Nat.le_add_right N start,
      lowers _ (free _ (Nat.le_add_left start N))⟩)

/-- Unrenewed drawdown along a run: a formation that lowers a condition at each active
step, while nothing renews it, is active only finitely often. -/
theorem Conditions.drawdown_finite {F C : Type} (K : Conditions S F C) {P : Process S A}
    (r : Run P) (f : F) (c : C) (T : Nat)
    (unrenewed : ∀ t, T ≤ t → K.level (r.state (t + 1)) c ≤ K.level (r.state t) c)
    (lowers : ∀ t, T ≤ t → K.active (r.state t) f →
      K.level (r.state (t + 1)) c < K.level (r.state t) c) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ K.active (r.state t) f :=
  unrenewed_drawdown_finite (K.along r) f c T unrenewed lowers

/-! ## The class belongs to the run -/

namespace Commons

/-- A shared condition renewed by one unit per step; the action is the amount drawn. -/
def process : Process Nat Nat := ⟨fun s d t => t = s + 1 - d⟩

inductive Formation where
  | focal
  | sustaining

/-- The sustaining formation depends on the condition at level one; the focal
formation draws on it and is active everywhere. -/
def conditions : Conditions Nat Formation Unit where
  level s _ := s
  active
    | _, .focal => True
    | s, .sustaining => 1 ≤ s
  requires
    | .focal, _ => False
    | .sustaining, _ => True
  need
    | .focal, _ => 0
    | .sustaining, _ => 1
  draws
    | .focal, _ => True
    | .sustaining, _ => False

/-- Drawing what is renewed. -/
def sharing : Run process := ⟨fun _ => 1, fun _ => 1, fun _ => rfl⟩

def winningState : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- Drawing one unit more than is renewed. -/
def winning : Run process :=
  ⟨winningState, fun _ => 2, fun | 0 => rfl | _ + 1 => rfl⟩

/-- One process, one initial configuration, the focal formation active at every step
of both runs: drawing within renewal is renewing, drawing beyond it consumes the
condition of the sustaining formation, which ends. -/
theorem class_belongs_to_the_run :
    sharing.state 0 = winning.state 0 ∧
    (∀ t, conditions.active (sharing.state t) .focal ∧
      conditions.active (winning.state t) .focal) ∧
    RenewingIn (conditions.along sharing) .focal ∧
    ConsumingIn (conditions.along winning) .focal ∧
    ∀ t, 1 ≤ t → ¬ conditions.active (winning.state t) .sustaining := by
  have lost : ∀ t, 1 ≤ t → winningState t < 1
    | 0, early => absurd early (Nat.not_succ_le_zero 0)
    | _ + 1, _ => Nat.zero_lt_one
  refine ⟨rfl, fun _ => ⟨trivial, trivial⟩, ?_, ⟨(), trivial, .sustaining, 1, trivial, lost⟩,
    fun t later active => Nat.not_le_of_gt (lost t later) active⟩
  intro _ _ _ g depends
  cases g with
  | focal => exact absurd depends id
  | sustaining => exact Nat.le_refl 1

end Commons

end Becoming
