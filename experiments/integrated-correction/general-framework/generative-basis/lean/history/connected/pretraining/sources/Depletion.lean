import GenerativeCore

/-!
# A finite-reserve constraint on continuation

The relation alone does not guarantee continuation. If a particular process
has a natural-number reserve and EVERY allowed transition strictly decreases
that reserve, its finite traces have bounded length and it has no infinite
execution. This is a conditional obstruction, not a universal claim that all
activity depletes one scalar resource. Replenishment, externally supplied inputs,
or reserve-preserving steps invalidate the strict-decrease premise.
-/

namespace Generative

universe u v

variable {State : Type u} {Action : Type v} {P : Process State Action}

/-- Every permitted step consumes at least one unit of the specified discrete
    reserve, so trace length and remaining reserve cannot exceed its start. -/
theorem trace_reserve_bound (reserve : State → Nat)
    (decreases : ∀ s a t, P.step s a t → reserve t < reserve s)
    {s t : State} {as : List Action} (h : Trace P s as t) :
    as.length + reserve t ≤ reserve s := by
  induction h with
  | nil s => simp
  | cons hstep _ ih =>
    have stepBound := decreases _ _ _ hstep
    simp only [List.length_cons]
    omega

theorem trace_length_bound (reserve : State → Nat)
    (decreases : ∀ s a t, P.step s a t → reserve t < reserve s)
    {s t : State} {as : List Action} (h : Trace P s as t) :
    as.length ≤ reserve s := by
  have totalBound := trace_reserve_bound reserve decreases h
  omega

/-- An actual return to the same condition state cannot coexist with strict
    depletion on every step of a nonempty cycle. -/
theorem no_nonempty_cycle_under_depletion (reserve : State → Nat)
    (decreases : ∀ s a t, P.step s a t → reserve t < reserve s)
    {s : State} {as : List Action} (h : Trace P s as s) (nonempty : as ≠ []) : False := by
  have totalBound := trace_reserve_bound reserve decreases h
  cases as with
  | nil => exact nonempty rfl
  | cons a rest =>
    simp only [List.length_cons] at totalBound
    omega

/-- An infinite sequence cannot keep strictly reducing a natural reserve. -/
theorem infinite_execution_contradicts_depletion (reserve : State → Nat)
    (decreases : ∀ s a t, P.step s a t → reserve t < reserve s)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1))) : False := by
  have bound : ∀ n, n + reserve (states n) ≤ reserve (states 0) := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      have stepBound := decreases _ _ _ (steps n)
      omega
  have exceeded := bound (reserve (states 0) + 1)
  omega

theorem no_infinite_execution_under_depletion (reserve : State → Nat)
    (decreases : ∀ s a t, P.step s a t → reserve t < reserve s) :
    ¬ ∃ states : Nat → State, ∃ actions : Nat → Action,
      ∀ n, P.step (states n) (actions n) (states (n + 1)) := by
  rintro ⟨states, actions, steps⟩
  exact infinite_execution_contradicts_depletion reserve decreases states actions steps

#print axioms trace_reserve_bound
#print axioms trace_length_bound
#print axioms no_nonempty_cycle_under_depletion
#print axioms infinite_execution_contradicts_depletion
#print axioms no_infinite_execution_under_depletion

end Generative
