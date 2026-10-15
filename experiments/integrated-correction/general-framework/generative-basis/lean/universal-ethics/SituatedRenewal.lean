import GenerativeCore -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Stock.trace_falls`, `Becoming.Run.renewal_recurs`, `ContinuationRenewal.renewal_within_rank_plus_one_steps` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md
import ContinuationRenewal

/-!
Actual continuation under indexed support dependencies requires timely support
addition or route replacement when demand exceeds inherited support. Idle and
unrelated steps may have zero demand. The accounting law is an independently
identified model premise, not the desired recurrence conclusion.

No agent, ethical predicate, particular repair recipe, infinite resource source,
or common scalar objective is introduced. Adequacy of the changed route and
the actual meaning of the support coordinates require separate correspondence.
-/

namespace Generative.SituatedRenewal

universe u v w x

/-- Coordinates of one process, indexed by its differentiated dependencies.
When a route persists, required use must be paid by remaining or added support.
Changing routes does not by itself certify that the new route is adequate. -/
structure DependencyLaw {State : Type u} {Action : Type v}
    (P : Process State Action) (Index : Type w) (Route : Type x) where
  route : Index → State → Route
  remaining : Index → State → Nat
  demand : Index → State → Action → State → Nat
  added : Index → State → Action → State → Nat
  account : ∀ i s a t, P.step s a t → route i t = route i s →
    remaining i t + demand i s a t ≤ remaining i s + added i s a t

variable {State : Type u} {Action : Type v} {Index : Type w} {Route : Type x}
variable {P : Process State Action}

/-- A response is an actual positive support addition or changed provision route.
It is necessary under depletion, but is not defined to be sufficient or ethical. -/
def Response (law : DependencyLaw P Index Route) (i : Index)
    (s : State) (a : Action) (t : State) : Prop :=
  0 < law.added i s a t ∨ law.route i t ≠ law.route i s

/-- Every intermediate transition of the selected finite window is retained. -/
def Window (P : Process State Action) (states : Nat → State) (actions : Nat → Action)
    (start length : Nat) : Prop :=
  ∀ k, k < length → P.step (states (start + k)) (actions (start + k))
    (states (start + k + 1))

def windowWord (actions : Nat → Action) (start : Nat) : Nat → List Action
  | 0 => []
  | n + 1 => windowWord actions start n ++ [actions (start + n)]

/-- The time-indexed window is an actual core trace with all its reached states. -/
theorem window_is_trace (states : Nat → State) (actions : Nat → Action)
    (start length : Nat) (actual : Window P states actions start length) :
    Trace P (states start) (windowWord actions start length) (states (start + length)) := by
  induction length with
  | zero => exact .nil _
  | succ length ih =>
    refine trace_append_iff.mpr ⟨states (start + length), ?_, ?_⟩
    · exact ih (fun k before => actual k (Nat.lt_trans before (Nat.lt_succ_self _)))
    · exact .cons (actual length (Nat.lt_succ_self _)) (.nil _)

def sumWindow (amount : Nat → Nat) (start : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => sumWindow amount start n + amount (start + n)

def totalDemand (law : DependencyLaw P Index Route) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat) : Nat :=
  sumWindow (fun n => law.demand i (states n) (actions n) (states (n + 1))) start length

/-- Actual usage composes without resetting any intermediate support state. -/
theorem sumWindow_append (amount : Nat → Nat) (start left right : Nat) :
    sumWindow amount start (left + right) =
      sumWindow amount start left + sumWindow amount (start + left) right := by
  induction right with
  | zero => rfl
  | succ right ih =>
    change sumWindow amount start (left + right) + amount (start + (left + right)) =
      sumWindow amount start left +
        (sumWindow amount (start + left) right + amount ((start + left) + right))
    rw [ih, Nat.add_assoc start left right, Nat.add_assoc]

/-- A finite window either retains its inherited route and pays all demand
from its initial remaining support, or contains a response while the route
before that response is still the inherited one. -/
theorem window_account_or_response [DecidableEq Route]
    (law : DependencyLaw P Index Route) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length) :
    (law.route i (states (start + length)) = law.route i (states start) ∧
      law.remaining i (states (start + length)) +
        totalDemand law i states actions start length ≤ law.remaining i (states start)) ∨
    ∃ k, k < length ∧ law.route i (states (start + k)) = law.route i (states start) ∧
      Response law i (states (start + k)) (actions (start + k)) (states (start + k + 1)) := by
  induction length with
  | zero => exact Or.inl ⟨rfl, Nat.le_refl _⟩
  | succ length ih =>
    have historyPrefix : Window P states actions start length :=
      fun k before => actual k (Nat.lt_trans before (Nat.lt_succ_self _))
    cases ih historyPrefix with
    | inr response =>
      obtain ⟨k, before, inherited, happened⟩ := response
      exact Or.inr ⟨k, Nat.lt_trans before (Nat.lt_succ_self _), inherited, happened⟩
    | inl bounded =>
      have step := actual length (Nat.lt_succ_self _)
      by_cases same : law.route i (states (start + length + 1)) =
          law.route i (states (start + length))
      · cases added : law.added i (states (start + length)) (actions (start + length))
            (states (start + length + 1)) with
        | zero =>
          have stepBound := law.account i _ _ _ step same
          rw [added, Nat.add_zero] at stepBound
          refine Or.inl ⟨same.trans bounded.1, ?_⟩
          change law.remaining i (states (start + length + 1)) +
            (totalDemand law i states actions start length +
              law.demand i (states (start + length)) (actions (start + length))
                (states (start + length + 1))) ≤ law.remaining i (states start)
          have prior := bounded.2
          omega
        | succ amount =>
          exact Or.inr ⟨length, Nat.lt_succ_self _, bounded.1,
            Or.inl (added ▸ Nat.zero_lt_succ amount)⟩
      · exact Or.inr ⟨length, Nat.lt_succ_self _, bounded.1, Or.inr same⟩

/-- Demand beyond inherited support forces some actual response before the
window ends. No particular contributor or repair recipe is selected. -/
theorem response_before_exhaustion [DecidableEq Route]
    (law : DependencyLaw P Index Route) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length)
    (needed : law.remaining i (states start) < totalDemand law i states actions start length) :
    ∃ k, k < length ∧ law.route i (states (start + k)) = law.route i (states start) ∧
      Response law i (states (start + k)) (actions (start + k)) (states (start + k + 1)) := by
  cases window_account_or_response law i states actions start length actual with
  | inr response => exact response
  | inl bounded =>
    have h := bounded.2
    have impossible : False := by omega
    exact False.elim impossible

/-- If the inherited provision route cannot add support on any actual step
that retains it, continued demand forces an actual replacement of that route.
Failure need only hold during this situated window, not for every state. -/
theorem inherited_failure_requires_replacement [DecidableEq Route]
    (law : DependencyLaw P Index Route) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length)
    (needed : law.remaining i (states start) < totalDemand law i states actions start length)
    (failed : ∀ k, k < length →
      law.route i (states (start + k)) = law.route i (states start) →
      law.route i (states (start + k + 1)) = law.route i (states (start + k)) →
      law.added i (states (start + k)) (actions (start + k)) (states (start + k + 1)) = 0) :
    ∃ k, k < length ∧ law.route i (states (start + k)) = law.route i (states start) ∧
      law.route i (states (start + k + 1)) ≠ law.route i (states start) := by
  obtain ⟨k, before, inherited, response⟩ :=
    response_before_exhaustion law i states actions start length actual needed
  refine ⟨k, before, inherited, ?_⟩
  intro unchanged
  have same := unchanged.trans inherited.symm
  cases response with
  | inl addition =>
    rw [failed k before inherited same] at addition
    exact Nat.not_lt_zero _ addition
  | inr replaced => exact replaced same

/-- Dependency-indexed, demand-timed recurrence on one actual continuing history.
Different indices may be served by different events and distributed roles. -/
theorem every_required_dependency_recurrently_responds [DecidableEq Route]
    (law : DependencyLaw P Index Route) (states : Nat → State) (actions : Nat → Action)
    (actual : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (required : ∀ i start, ∃ length,
      law.remaining i (states start) < totalDemand law i states actions start length) :
    ∀ i start, ∃ n, start ≤ n ∧ P.step (states n) (actions n) (states (n + 1)) ∧
      Response law i (states n) (actions n) (states (n + 1)) := by
  intro i start
  obtain ⟨length, needed⟩ := required i start
  obtain ⟨k, _, _, response⟩ := response_before_exhaustion law i states actions start length
    (fun k _ => actual (start + k)) needed
  exact ⟨start + k, Nat.le_add_right _ _, actual _, response⟩

/-- Link to the earlier strict-depletion theorem when this dependency is used
on every actual event. The general window result also allows zero-demand gaps. -/
theorem no_response_strictly_depletes (law : DependencyLaw P Index Route) (i : Index)
    {s t : State} {a : Action} (actual : P.step s a t)
    (used : 1 ≤ law.demand i s a t) (same : law.route i t = law.route i s)
    (noAddition : law.added i s a t = 0) : law.remaining i t < law.remaining i s := by
  have account := law.account i s a t actual same
  rw [noAddition, Nat.add_zero] at account
  omega

/-- With positive demand on every event, a response occurs within reached
remaining-support plus one actual steps, by ContinuationRenewal's theorem. -/
theorem response_within_remaining_bound [DecidableEq Route]
    (law : DependencyLaw P Index Route) (i : Index)
    (states : Nat → State) (actions : Nat → Action)
    (actual : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (used : ∀ n, 1 ≤ law.demand i (states n) (actions n) (states (n + 1))) (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + law.remaining i (states start) ∧
      Response law i (states n) (actions n) (states (n + 1)) := by
  letI : DecidablePred (fun n => Response law i (states n) (actions n) (states (n + 1))) :=
    fun n => inferInstanceAs
      (Decidable (0 < law.added i (states n) (actions n) (states (n + 1)) ∨
        law.route i (states (n + 1)) ≠ law.route i (states n)))
  apply ContinuationRenewal.renewal_within_rank_plus_one_steps
    (fun n => law.remaining i (states n))
    (fun n => Response law i (states n) (actions n) (states (n + 1))) ?_ start
  intro n absent
  have same : law.route i (states (n + 1)) = law.route i (states n) := by
    by_cases h : law.route i (states (n + 1)) = law.route i (states n)
    · exact h
    · exact False.elim (absent (Or.inr h))
  have noAddition : law.added i (states n) (actions n) (states (n + 1)) = 0 := by
    cases amount : law.added i (states n) (actions n) (states (n + 1)) with
    | zero => rfl
    | succ k => exact False.elim (absent (Or.inl (amount ▸ Nat.zero_lt_succ k)))
  exact no_response_strictly_depletes law i (actual n) (used n) same noAddition

/-- An idle process shows why continuation alone, without a dependence/use law,
does not entail renewal. This is not offered as a model of living activity. -/
def idle : Process Unit Unit where
  step _ _ _ := True

def idleDependencies : DependencyLaw idle Unit Unit where
  route _ _ := ()
  remaining _ _ := 0
  demand _ _ _ _ := 0
  added _ _ _ _ := 0
  account _ _ _ _ _ _ := Nat.le_refl _

theorem continuation_without_required_use_has_no_response :
    (∀ _ : Nat, idle.step () () ()) ∧ ¬ Response idleDependencies () () () () := by
  refine ⟨fun _ => True.intro, ?_⟩
  intro response
  cases response with
  | inl positive => exact Nat.not_lt_zero _ positive
  | inr changed => exact changed rfl

end Generative.SituatedRenewal

#print axioms Generative.SituatedRenewal.DependencyLaw
#print axioms Generative.SituatedRenewal.Response
#print axioms Generative.SituatedRenewal.Window
#print axioms Generative.SituatedRenewal.windowWord
#print axioms Generative.SituatedRenewal.window_is_trace
#print axioms Generative.SituatedRenewal.sumWindow
#print axioms Generative.SituatedRenewal.totalDemand
#print axioms Generative.SituatedRenewal.sumWindow_append
#print axioms Generative.SituatedRenewal.window_account_or_response
#print axioms Generative.SituatedRenewal.response_before_exhaustion
#print axioms Generative.SituatedRenewal.inherited_failure_requires_replacement
#print axioms Generative.SituatedRenewal.every_required_dependency_recurrently_responds
#print axioms Generative.SituatedRenewal.no_response_strictly_depletes
#print axioms Generative.SituatedRenewal.response_within_remaining_bound
#print axioms Generative.SituatedRenewal.idle
#print axioms Generative.SituatedRenewal.idleDependencies
#print axioms Generative.SituatedRenewal.continuation_without_required_use_has_no_response
