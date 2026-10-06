import GenerativeCore

/-!
# Conditional constraints on continued activity

A law class, quantified over arbitrary carriers and action alphabets. The
accounting premise concerns an identified supporting quantity, not welfare,
reward, or a universal value. Demand and credit are supplied, nonnegative,
edge-local quantities. The basic balance permits zero-demand transitions.
Event-count conclusions separately require at least one unit per event.

Credit can be internal regeneration, conversion from an untracked store, or
external provision at the declared boundary. Its necessity does not establish
which of those mechanisms supplies it, nor does it establish learning.
-/

namespace Generative.Conditional

universe u v w

variable {State : Type u} {Action : Type v} {P : Process State Action}

/-- An empirical or model premise about every permitted event. -/
def AccountLaw (P : Process State Action) (reserve : State → Nat)
    (demand credit : State → Action → State → Nat) : Prop :=
  ∀ s a t, P.step s a t → reserve t + demand s a t ≤ reserve s + credit s a t

/-- A forward simulation suffices to transfer a necessary accounting bound.
    It does not assert exactness of observation, control, or probability. -/
theorem account_law_pullback {Other : Type w} (Q : Process Other Action)
    (q : State → Other)
    (preserves : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (reserve : Other → Nat) (demand credit : Other → Action → Other → Nat)
    (law : AccountLaw Q reserve demand credit) :
    AccountLaw P (fun s => reserve (q s))
      (fun s a t => demand (q s) a (q t))
      (fun s a t => credit (q s) a (q t)) := by
  intro s a t hs
  exact law _ _ _ (preserves s a t hs)

/-- Counts a credit-bearing event once regardless of the amount delivered. -/
def credited (amount : Nat) : Nat := if amount = 0 then 0 else 1

/-- Account totals follow the actual intermediate states of a trace. They are
    not calculated from its event word without those states. -/
inductive SupportTrace (P : Process State Action)
    (demand credit : State → Action → State → Nat) :
    State → List Action → State → Nat → Nat → Nat → Prop where
  | nil (s : State) : SupportTrace P demand credit s [] s 0 0 0
  | cons {s m t : State} {a : Action} {as : List Action}
      {spent received count : Nat} :
      P.step s a m → SupportTrace P demand credit m as t spent received count →
      SupportTrace P demand credit s (a :: as) t
        (demand s a m + spent) (credit s a m + received)
        (credited (credit s a m) + count)

theorem support_trace_is_trace {demand credit : State → Action → State → Nat}
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    Trace P s as t := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih => exact .cons hs ih

/-- Every actual finite history admits exact totals for the supplied accounts. -/
theorem trace_has_support_account (demand credit : State → Action → State → Nat)
    {s t : State} {as : List Action} (h : Trace P s as t) :
    ∃ spent received count, SupportTrace P demand credit s as t spent received count := by
  induction h with
  | nil s => exact ⟨0, 0, 0, .nil s⟩
  | cons hs _ ih =>
    obtain ⟨spent, received, count, ht⟩ := ih
    exact ⟨_, _, _, .cons hs ht⟩

/-- Accounted paths compose only through the actual shared boundary state. -/
theorem support_trace_append {demand credit : State → Action → State → Nat}
    {s m t : State} {xs ys : List Action}
    {spent₁ received₁ count₁ spent₂ received₂ count₂ : Nat}
    (left : SupportTrace P demand credit s xs m spent₁ received₁ count₁)
    (right : SupportTrace P demand credit m ys t spent₂ received₂ count₂) :
    SupportTrace P demand credit s (xs ++ ys) t
      (spent₁ + spent₂) (received₁ + received₂) (count₁ + count₂) := by
  induction left with
  | nil s => simpa using right
  | cons hs _ ih =>
    simpa [Nat.add_assoc] using SupportTrace.cons hs (ih right)

def repeatWord (word : List Action) : Nat → List Action
  | 0 => []
  | times + 1 => word ++ repeatWord word times

/-- A genuinely closed, executable accounted cycle supplies arbitrarily many
    finite repetitions. Any external store relevant to executability must be
    included in the state or represented by the declared continuing event law. -/
theorem repeat_accounted_cycle {demand credit : State → Action → State → Nat}
    {s : State} {word : List Action} {spent received count : Nat}
    (cycle : SupportTrace P demand credit s word s spent received count)
    (times : Nat) :
    SupportTrace P demand credit s (repeatWord word times) s
      (times * spent) (times * received) (times * count) := by
  induction times with
  | zero =>
    simp only [repeatWord, Nat.zero_mul]
    exact .nil s
  | succ times ih =>
    simpa [repeatWord, Nat.succ_mul, Nat.add_comm] using support_trace_append cycle ih

theorem support_trace_balance (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    spent + reserve t ≤ reserve s + received := by
  induction h with
  | nil s => simp
  | cons hs _ ih =>
    have edge := law _ _ _ hs
    omega

/-- A closed state cycle must cover its declared demand with supplied credit. -/
theorem support_cycle_covers_demand (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    {s : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as s spent received count) :
    spent ≤ received := by
  have hb := support_trace_balance reserve law h
  omega

theorem support_trace_unit_demand
    {demand credit : State → Action → State → Nat}
    (unit : ∀ s a t, P.step s a t → 1 ≤ demand s a t)
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    as.length ≤ spent := by
  induction h with
  | nil s => simp
  | cons hs _ ih =>
    have edge := unit _ _ _ hs
    simp only [List.length_cons]
    omega

theorem amount_le_cap_times_credited {amount cap : Nat} (h : amount ≤ cap) :
    amount ≤ cap * credited amount := by
  by_cases hz : amount = 0
  · simp [credited, hz]
  · simpa [credited, hz] using h

theorem support_trace_credit_cap
    {demand credit : State → Action → State → Nat} (cap : Nat)
    (bounded : ∀ s a t, P.step s a t → credit s a t ≤ cap)
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    received ≤ cap * count := by
  induction h with
  | nil s => simp
  | cons hs _ ih =>
    have edge := amount_le_cap_times_credited (bounded _ _ _ hs)
    rw [Nat.mul_add]
    omega

/-- Frequency bound applies only when every event demands a positive discrete
    amount AND delivery per credit-bearing event is bounded. -/
theorem support_trace_length_bound (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (unit : ∀ s a t, P.step s a t → 1 ≤ demand s a t)
    (cap : Nat) (bounded : ∀ s a t, P.step s a t → credit s a t ≤ cap)
    {s t : State} {as : List Action} {spent received count : Nat}
    (h : SupportTrace P demand credit s as t spent received count) :
    as.length + reserve t ≤ reserve s + cap * count := by
  have hb := support_trace_balance reserve law h
  have hd := support_trace_unit_demand unit h
  have hc := support_trace_credit_cap cap bounded h
  omega

/-- Total of a quantity over a finite interval of event indices. -/
def intervalTotal (quantity : Nat → Nat) (start : Nat) : Nat → Nat
  | 0 => 0
  | length + 1 => intervalTotal quantity start length + quantity (start + length)

theorem interval_total_positive_witness {quantity : Nat → Nat} {start length : Nat}
    (positive : 0 < intervalTotal quantity start length) :
    ∃ offset, offset < length ∧ 0 < quantity (start + offset) := by
  induction length with
  | zero => simp [intervalTotal] at positive
  | succ length ih =>
    by_cases last : 0 < quantity (start + length)
    · exact ⟨length, Nat.lt_succ_self length, last⟩
    · have prior : 0 < intervalTotal quantity start length := by
        simp only [intervalTotal] at positive
        omega
      obtain ⟨offset, bound, hp⟩ := ih prior
      exact ⟨offset, by omega, hp⟩

theorem interval_total_le_of_pointwise {left right : Nat → Nat}
    (bound : ∀ n, left n ≤ right n) (start length : Nat) :
    intervalTotal left start length ≤ intervalTotal right start length := by
  induction length with
  | zero => simp [intervalTotal]
  | succ n ih =>
    have point := bound (start + n)
    simp only [intervalTotal]
    omega

theorem interval_total_unit_bound {quantity : Nat → Nat}
    (unit : ∀ n, 1 ≤ quantity n) (start length : Nat) :
    length ≤ intervalTotal quantity start length := by
  induction length with
  | zero => simp [intervalTotal]
  | succ n ih =>
    have point := unit (start + n)
    simp only [intervalTotal]
    omega

theorem interval_total_cap_bound {quantity : Nat → Nat} (cap : Nat)
    (bound : ∀ n, quantity n ≤ cap) (start length : Nat) :
    intervalTotal quantity start length ≤
      cap * intervalTotal (fun n => credited (quantity n)) start length := by
  induction length with
  | zero => simp [intervalTotal]
  | succ n ih =>
    have point := amount_le_cap_times_credited (bound (start + n))
    simp only [intervalTotal, Nat.mul_add]
    omega

/-- All suffixes preserve the actual state history; nothing is reset. -/
theorem execution_interval_balance (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    intervalTotal (fun n => demand (states n) (actions n) (states (n + 1))) start length +
      reserve (states (start + length)) ≤ reserve (states start) +
      intervalTotal (fun n => credit (states n) (actions n) (states (n + 1))) start length := by
  induction length with
  | zero => simp [intervalTotal]
  | succ n ih =>
    have edge := law _ _ _ (steps (start + n))
    simp only [intervalTotal, Nat.add_assoc] at *
    omega

/-- No aggregation of incomparable supports is required: the balance holds for
    each declared resource account independently. -/
theorem componentwise_execution_balance {Index : Type w}
    (reserve : Index → State → Nat)
    (demand credit : Index → State → Action → State → Nat)
    (laws : ∀ i, AccountLaw P (reserve i) (demand i) (credit i))
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    ∀ i, intervalTotal (fun n => demand i (states n) (actions n) (states (n + 1)))
        start length + reserve i (states (start + length)) ≤ reserve i (states start) +
      intervalTotal (fun n => credit i (states n) (actions n) (states (n + 1)))
        start length := by
  intro i
  exact execution_interval_balance (reserve i) (laws i) states actions steps start length

/-- Unlimited cumulative demand requires unlimited supplied credit. Infinite
    zero-cost stuttering is not excluded by this statement. -/
theorem unbounded_demand_requires_unbounded_credit (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (unbounded : ∀ bound, ∃ length, bound <
      intervalTotal (fun n => demand (states n) (actions n) (states (n + 1))) 0 length) :
    ∀ bound, ∃ length, bound <
      intervalTotal (fun n => credit (states n) (actions n) (states (n + 1))) 0 length := by
  intro bound
  obtain ⟨length, hd⟩ := unbounded (reserve (states 0) + bound)
  have hb := execution_interval_balance reserve law states actions steps 0 length
  exact ⟨length, by omega⟩

/-- Under positive discrete demand, each suffix must receive credit no later
    than its inherited reserve would be exhausted. This gives an explicit
    finite witness, stronger than a mere denial of eventual cessation. -/
theorem infinite_unit_execution_credit_window (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (unit : ∀ s a t, P.step s a t → 1 ≤ demand s a t)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + reserve (states start) ∧
      0 < credit (states n) (actions n) (states (n + 1)) := by
  let length := reserve (states start) + 1
  have hb := execution_interval_balance reserve law states actions steps start length
  have hd := interval_total_unit_bound (fun n => unit _ _ _ (steps n)) start length
  have positive : 0 < intervalTotal
      (fun n => credit (states n) (actions n) (states (n + 1))) start length := by
    dsimp [length] at *
    omega
  obtain ⟨offset, ho, hc⟩ := interval_total_positive_witness positive
  exact ⟨start + offset, by omega, by dsimp [length] at ho; omega, hc⟩

theorem infinite_unit_execution_unbounded_credit (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (unit : ∀ s a t, P.step s a t → 1 ≤ demand s a t)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1))) :
    ∀ bound, ∃ length, bound <
      intervalTotal (fun n => credit (states n) (actions n) (states (n + 1))) 0 length := by
  apply unbounded_demand_requires_unbounded_credit reserve law states actions steps
  intro bound
  refine ⟨bound + 1, ?_⟩
  have hd := interval_total_unit_bound (fun n => unit _ _ _ (steps n)) 0 (bound + 1)
  omega

theorem execution_interval_frequency_bound (reserve : State → Nat)
    {demand credit : State → Action → State → Nat}
    (law : AccountLaw P reserve demand credit)
    (unit : ∀ s a t, P.step s a t → 1 ≤ demand s a t)
    (cap : Nat) (bounded : ∀ s a t, P.step s a t → credit s a t ≤ cap)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    length + reserve (states (start + length)) ≤ reserve (states start) +
      cap * intervalTotal
        (fun n => credited (credit (states n) (actions n) (states (n + 1)))) start length := by
  have hb := execution_interval_balance reserve law states actions steps start length
  have hd := interval_total_unit_bound (fun n => unit _ _ _ (steps n)) start length
  have hc := interval_total_cap_bound cap (fun n => bounded _ _ _ (steps n)) start length
  omega

#print axioms support_trace_is_trace
#print axioms account_law_pullback
#print axioms trace_has_support_account
#print axioms support_trace_append
#print axioms repeat_accounted_cycle
#print axioms support_trace_balance
#print axioms support_cycle_covers_demand
#print axioms support_trace_unit_demand
#print axioms amount_le_cap_times_credited
#print axioms support_trace_credit_cap
#print axioms support_trace_length_bound
#print axioms interval_total_positive_witness
#print axioms interval_total_le_of_pointwise
#print axioms interval_total_unit_bound
#print axioms interval_total_cap_bound
#print axioms execution_interval_balance
#print axioms componentwise_execution_balance
#print axioms unbounded_demand_requires_unbounded_credit
#print axioms infinite_unit_execution_credit_window
#print axioms infinite_unit_execution_unbounded_credit
#print axioms execution_interval_frequency_bound

end Generative.Conditional
