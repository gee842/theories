import GenerativeCore

/-!
# Conditional constraints on continued activity

A law class, quantified over arbitrary carriers and action alphabets. Three
quantities describe one continuing activity: what each state `held` available
for further activity, what each event `enacted`, and what `arrived` during it.
They concern an identified supporting quantity, not welfare, reward or a
universal value. The law `SustainLaw` says no event enacts more than was held
plus what arrived; nothing appears from nowhere. Losses are permitted, and so
are events that enact nothing. Event-count conclusions separately require each
event to enact at least one unit.

What arrives can be internal regeneration, conversion from an untracked store,
or provision across the declared boundary. That arrival is necessary does not
establish which of these supplies it, nor does it establish learning.

Vocabulary renamed on 6 October 2026 at Ren's direction, replacing an exchange
picture (account, reserve, demand, credit); statements and proofs are unchanged.
-/

namespace Generative.Conditional

universe u v w

variable {State : Type u} {Action : Type v} {P : Process State Action}

/-- U1: every permitted event is sustained by what was held and what arrived.
    An empirical or model premise, not a consequence. -/
def SustainLaw (P : Process State Action) (held : State → Nat)
    (enacted arrived : State → Action → State → Nat) : Prop :=
  ∀ s a t, P.step s a t → held t + enacted s a t ≤ held s + arrived s a t

/-- A forward simulation suffices to transfer this necessary bound.
    It does not assert exactness of observation, control, or probability. -/
theorem sustain_law_pullback {Other : Type w} (Q : Process Other Action)
    (q : State → Other)
    (preserves : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (held : Other → Nat) (enacted arrived : Other → Action → Other → Nat)
    (law : SustainLaw Q held enacted arrived) :
    SustainLaw P (fun s => held (q s))
      (fun s a t => enacted (q s) a (q t))
      (fun s a t => arrived (q s) a (q t)) := by
  intro s a t hs
  exact law _ _ _ (preserves s a t hs)

/-- Counts an event in which something arrived once, whatever the amount. -/
def arrivalEvent (amount : Nat) : Nat := if amount = 0 then 0 else 1

/-- Constructive left cancellation; the library version depends on `propext`. -/
theorem le_cancel_left {a b c : Nat} (h : a + b ≤ a + c) : b ≤ c := by
  induction a with
  | zero => rw [Nat.zero_add, Nat.zero_add] at h; exact h
  | succ a ih =>
    rw [Nat.succ_add, Nat.succ_add] at h
    exact ih (Nat.le_of_succ_le_succ h)

/-- One sustained step composed with a sustained remainder. -/
theorem step_then_rest {e E ht hm hs r R : Nat}
    (edge : hm + e ≤ hs + r) (rest : E + ht ≤ hm + R) :
    (e + E) + ht ≤ hs + (r + R) :=
  calc (e + E) + ht = e + (E + ht) := Nat.add_assoc e E ht
    _ ≤ e + (hm + R) := Nat.add_le_add_left rest e
    _ = (hm + e) + R := by rw [Nat.add_comm hm e, Nat.add_assoc]
    _ ≤ (hs + r) + R := Nat.add_le_add_right edge R
    _ = hs + (r + R) := Nat.add_assoc hs r R

/-- A sustained prefix followed by one sustained step. -/
theorem rest_then_step {T e h' hm hs R r : Nat}
    (rest : T + hm ≤ hs + R) (edge : h' + e ≤ hm + r) :
    (T + e) + h' ≤ hs + (R + r) :=
  calc (T + e) + h' = T + (h' + e) := by rw [Nat.add_assoc, Nat.add_comm e h']
    _ ≤ T + (hm + r) := Nat.add_le_add_left edge T
    _ = (T + hm) + r := (Nat.add_assoc T hm r).symm
    _ ≤ (hs + R) + r := Nat.add_le_add_right rest r
    _ = hs + (R + r) := Nat.add_assoc hs R r

/-- Enacted and arrived totals follow the actual intermediate states of a trace. They are
    not calculated from its event word without those states. -/
inductive SupportTrace (P : Process State Action)
    (enacted arrived : State → Action → State → Nat) :
    State → List Action → State → Nat → Nat → Nat → Prop where
  | nil (s : State) : SupportTrace P enacted arrived s [] s 0 0 0
  | cons {s m t : State} {a : Action} {as : List Action}
      {enactedTotal arrivedTotal count : Nat} :
      P.step s a m → SupportTrace P enacted arrived m as t enactedTotal arrivedTotal count →
      SupportTrace P enacted arrived s (a :: as) t
        (enacted s a m + enactedTotal) (arrived s a m + arrivedTotal)
        (arrivalEvent (arrived s a m) + count)

theorem support_trace_is_trace {enacted arrived : State → Action → State → Nat}
    {s t : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count) :
    Trace P s as t := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih => exact .cons hs ih

/-- Every actual finite history has exact totals for the supplied quantities. -/
theorem trace_has_support_totals (enacted arrived : State → Action → State → Nat)
    {s t : State} {as : List Action} (h : Trace P s as t) :
    ∃ enactedTotal arrivedTotal count, SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count := by
  induction h with
  | nil s => exact ⟨0, 0, 0, .nil s⟩
  | cons hs _ ih =>
    obtain ⟨enactedTotal, arrivedTotal, count, ht⟩ := ih
    exact ⟨_, _, _, .cons hs ht⟩

/-- Supported paths compose only through the actual shared boundary state. -/
theorem support_trace_append {enacted arrived : State → Action → State → Nat}
    {s m t : State} {xs ys : List Action}
    {enactedTotal₁ arrivedTotal₁ count₁ enactedTotal₂ arrivedTotal₂ count₂ : Nat}
    (left : SupportTrace P enacted arrived s xs m enactedTotal₁ arrivedTotal₁ count₁)
    (right : SupportTrace P enacted arrived m ys t enactedTotal₂ arrivedTotal₂ count₂) :
    SupportTrace P enacted arrived s (xs ++ ys) t
      (enactedTotal₁ + enactedTotal₂) (arrivedTotal₁ + arrivedTotal₂) (count₁ + count₂) := by
  induction left with
  | nil s => simpa using right
  | cons hs _ ih =>
    simpa [Nat.add_assoc] using SupportTrace.cons hs (ih right)

def repeatWord (word : List Action) : Nat → List Action
  | 0 => []
  | times + 1 => word ++ repeatWord word times

/-- A genuinely closed, executable supported cycle supplies arbitrarily many
    finite repetitions. Any external store relevant to executability must be
    included in the state or represented by the declared continuing event law. -/
theorem repeat_supported_cycle {enacted arrived : State → Action → State → Nat}
    {s : State} {word : List Action} {enactedTotal arrivedTotal count : Nat}
    (cycle : SupportTrace P enacted arrived s word s enactedTotal arrivedTotal count)
    (times : Nat) :
    SupportTrace P enacted arrived s (repeatWord word times) s
      (times * enactedTotal) (times * arrivedTotal) (times * count) := by
  induction times with
  | zero =>
    simp only [repeatWord, Nat.zero_mul]
    exact .nil s
  | succ times ih =>
    simpa [repeatWord, Nat.succ_mul, Nat.add_comm] using support_trace_append cycle ih

theorem support_trace_bound (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    {s t : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count) :
    enactedTotal + held t ≤ held s + arrivedTotal := by
  induction h with
  | nil s => rw [Nat.zero_add, Nat.add_zero]; exact Nat.le_refl _
  | cons hs _ ih => exact step_then_rest (law _ _ _ hs) ih

/-- Around a closed state cycle, what arrived covers what was enacted. -/
theorem support_cycle_arrival_covers_enactment (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    {s : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as s enactedTotal arrivedTotal count) :
    enactedTotal ≤ arrivedTotal := by
  have hb := support_trace_bound held law h
  rw [Nat.add_comm enactedTotal] at hb
  exact le_cancel_left hb

theorem support_trace_unit_enactment
    {enacted arrived : State → Action → State → Nat}
    (unit : ∀ s a t, P.step s a t → 1 ≤ enacted s a t)
    {s t : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count) :
    as.length ≤ enactedTotal := by
  induction h with
  | nil s => exact Nat.zero_le _
  | cons hs _ ih =>
    show _ + 1 ≤ _
    rw [Nat.add_comm]
    exact Nat.add_le_add (unit _ _ _ hs) ih

theorem amount_le_cap_times_arrival_events {amount cap : Nat} (h : amount ≤ cap) :
    amount ≤ cap * arrivalEvent amount := by
  unfold arrivalEvent
  cases Nat.decEq amount 0 with
  | isTrue hz => rw [if_pos hz, hz]; exact Nat.zero_le _
  | isFalse hz => rw [if_neg hz, Nat.mul_one]; exact h

theorem support_trace_arrival_cap
    {enacted arrived : State → Action → State → Nat} (cap : Nat)
    (bounded : ∀ s a t, P.step s a t → arrived s a t ≤ cap)
    {s t : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count) :
    arrivedTotal ≤ cap * count := by
  induction h with
  | nil s => exact Nat.zero_le _
  | cons hs _ ih =>
    rw [Nat.mul_add]
    exact Nat.add_le_add (amount_le_cap_times_arrival_events (bounded _ _ _ hs)) ih

/-- The frequency bound applies only when every event enacts a positive discrete
    amount AND the amount arriving in any one event is bounded. -/
theorem support_trace_length_bound (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (unit : ∀ s a t, P.step s a t → 1 ≤ enacted s a t)
    (cap : Nat) (bounded : ∀ s a t, P.step s a t → arrived s a t ≤ cap)
    {s t : State} {as : List Action} {enactedTotal arrivedTotal count : Nat}
    (h : SupportTrace P enacted arrived s as t enactedTotal arrivedTotal count) :
    as.length + held t ≤ held s + cap * count :=
  Nat.le_trans (Nat.add_le_add_right (support_trace_unit_enactment unit h) _)
    (Nat.le_trans (support_trace_bound held law h)
      (Nat.add_le_add_left (support_trace_arrival_cap cap bounded h) _))

/-- Total of a quantity over a finite interval of event indices. -/
def intervalTotal (quantity : Nat → Nat) (start : Nat) : Nat → Nat
  | 0 => 0
  | length + 1 => intervalTotal quantity start length + quantity (start + length)

theorem interval_total_positive_witness {quantity : Nat → Nat} {start length : Nat}
    (positive : 0 < intervalTotal quantity start length) :
    ∃ offset, offset < length ∧ 0 < quantity (start + offset) := by
  induction length with
  | zero => exact absurd positive (Nat.lt_irrefl 0)
  | succ length ih =>
    cases Nat.decEq (quantity (start + length)) 0 with
    | isFalse last => exact ⟨length, Nat.lt_succ_self length, Nat.pos_of_ne_zero last⟩
    | isTrue last =>
      have prior : 0 < intervalTotal quantity start length := by
        have p : 0 < intervalTotal quantity start length + quantity (start + length) := positive
        rw [last, Nat.add_zero] at p
        exact p
      obtain ⟨offset, bound, hp⟩ := ih prior
      exact ⟨offset, Nat.lt_succ_of_lt bound, hp⟩

theorem interval_total_le_of_pointwise {left right : Nat → Nat}
    (bound : ∀ n, left n ≤ right n) (start length : Nat) :
    intervalTotal left start length ≤ intervalTotal right start length := by
  induction length with
  | zero => exact Nat.le_refl 0
  | succ n ih => exact Nat.add_le_add ih (bound (start + n))

theorem interval_total_unit_bound {quantity : Nat → Nat}
    (unit : ∀ n, 1 ≤ quantity n) (start length : Nat) :
    length ≤ intervalTotal quantity start length := by
  induction length with
  | zero => exact Nat.le_refl 0
  | succ n ih => exact Nat.add_le_add ih (unit (start + n))

theorem interval_total_cap_bound {quantity : Nat → Nat} (cap : Nat)
    (bound : ∀ n, quantity n ≤ cap) (start length : Nat) :
    intervalTotal quantity start length ≤
      cap * intervalTotal (fun n => arrivalEvent (quantity n)) start length := by
  induction length with
  | zero => exact Nat.zero_le _
  | succ n ih =>
    show _ + _ ≤ cap * (_ + _)
    rw [Nat.mul_add]
    exact Nat.add_le_add ih (amount_le_cap_times_arrival_events (bound (start + n)))

/-- All suffixes preserve the actual state history; nothing is reset. -/
theorem execution_interval_bound (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    intervalTotal (fun n => enacted (states n) (actions n) (states (n + 1))) start length +
      held (states (start + length)) ≤ held (states start) +
      intervalTotal (fun n => arrived (states n) (actions n) (states (n + 1))) start length := by
  induction length with
  | zero =>
    show 0 + held (states (start + 0)) ≤ held (states start) + 0
    rw [Nat.zero_add, Nat.add_zero]; exact Nat.le_refl _
  | succ n ih => exact rest_then_step ih (law _ _ _ (steps (start + n)))

/-- No aggregation of incomparable supports is required: the bound holds for
    each declared supporting quantity independently. -/
theorem componentwise_execution_bound {Index : Type w}
    (held : Index → State → Nat)
    (enacted arrived : Index → State → Action → State → Nat)
    (laws : ∀ i, SustainLaw P (held i) (enacted i) (arrived i))
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    ∀ i, intervalTotal (fun n => enacted i (states n) (actions n) (states (n + 1)))
        start length + held i (states (start + length)) ≤ held i (states start) +
      intervalTotal (fun n => arrived i (states n) (actions n) (states (n + 1)))
        start length := by
  intro i
  exact execution_interval_bound (held i) (laws i) states actions steps start length

/-- Unlimited cumulative enactment requires unlimited arrival. Infinite
    stuttering that enacts nothing is not excluded by this statement. -/
theorem unbounded_enactment_requires_unbounded_arrival (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (unbounded : ∀ bound, ∃ length, bound <
      intervalTotal (fun n => enacted (states n) (actions n) (states (n + 1))) 0 length) :
    ∀ bound, ∃ length, bound <
      intervalTotal (fun n => arrived (states n) (actions n) (states (n + 1))) 0 length := by
  intro bound
  obtain ⟨length, hd⟩ := unbounded (held (states 0) + bound)
  have hb := execution_interval_bound held law states actions steps 0 length
  refine ⟨length, ?_⟩
  have h1 : held (states 0) + bound <
      held (states 0) + intervalTotal (fun n => arrived (states n) (actions n) (states (n + 1))) 0 length :=
    Nat.lt_of_lt_of_le hd (Nat.le_trans (Nat.le_add_right _ _) hb)
  exact Nat.lt_of_add_lt_add_left h1

/-- When every event enacts at least one unit, something must arrive in each
    suffix no later than what it inherited as held would be exhausted. This gives an explicit
    finite witness, stronger than a mere denial of eventual cessation. -/
theorem infinite_unit_execution_arrival_window (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (unit : ∀ s a t, P.step s a t → 1 ≤ enacted s a t)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + held (states start) ∧
      0 < arrived (states n) (actions n) (states (n + 1)) := by
  let length := held (states start) + 1
  have hb := execution_interval_bound held law states actions steps start length
  have hd := interval_total_unit_bound (fun n => unit _ _ _ (steps n)) start length
  have positive : 0 < intervalTotal
      (fun n => arrived (states n) (actions n) (states (n + 1))) start length := by
    -- held(start) + 1 ≤ enacted total + final held ≤ held(start) + arrived total
    have h1 : held (states start) + 1 ≤ held (states start) + intervalTotal
        (fun n => arrived (states n) (actions n) (states (n + 1))) start length :=
      Nat.le_trans (Nat.le_trans hd (Nat.le_add_right _ _)) hb
    exact le_cancel_left h1
  obtain ⟨offset, ho, hc⟩ := interval_total_positive_witness positive
  exact ⟨start + offset, Nat.le_add_right _ _,
    Nat.add_le_add_left (Nat.le_of_lt_succ ho) _, hc⟩

theorem infinite_unit_execution_unbounded_arrival (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (unit : ∀ s a t, P.step s a t → 1 ≤ enacted s a t)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1))) :
    ∀ bound, ∃ length, bound <
      intervalTotal (fun n => arrived (states n) (actions n) (states (n + 1))) 0 length := by
  apply unbounded_enactment_requires_unbounded_arrival held law states actions steps
  intro bound
  exact ⟨bound + 1, interval_total_unit_bound (fun n => unit _ _ _ (steps n)) 0 (bound + 1)⟩

theorem execution_interval_frequency_bound (held : State → Nat)
    {enacted arrived : State → Action → State → Nat}
    (law : SustainLaw P held enacted arrived)
    (unit : ∀ s a t, P.step s a t → 1 ≤ enacted s a t)
    (cap : Nat) (bounded : ∀ s a t, P.step s a t → arrived s a t ≤ cap)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (start length : Nat) :
    length + held (states (start + length)) ≤ held (states start) +
      cap * intervalTotal
        (fun n => arrivalEvent (arrived (states n) (actions n) (states (n + 1)))) start length := by
  have hb := execution_interval_bound held law states actions steps start length
  have hd := interval_total_unit_bound (fun n => unit _ _ _ (steps n)) start length
  have hc := interval_total_cap_bound cap (fun n => bounded _ _ _ (steps n)) start length
  exact Nat.le_trans (Nat.add_le_add_right hd _)
    (Nat.le_trans hb (Nat.add_le_add_left hc _))

#print axioms le_cancel_left
#print axioms step_then_rest
#print axioms rest_then_step
#print axioms support_trace_is_trace
#print axioms sustain_law_pullback
#print axioms trace_has_support_totals
#print axioms support_trace_append
#print axioms repeat_supported_cycle
#print axioms support_trace_bound
#print axioms support_cycle_arrival_covers_enactment
#print axioms support_trace_unit_enactment
#print axioms amount_le_cap_times_arrival_events
#print axioms support_trace_arrival_cap
#print axioms support_trace_length_bound
#print axioms interval_total_positive_witness
#print axioms interval_total_le_of_pointwise
#print axioms interval_total_unit_bound
#print axioms interval_total_cap_bound
#print axioms execution_interval_bound
#print axioms componentwise_execution_bound
#print axioms unbounded_enactment_requires_unbounded_arrival
#print axioms infinite_unit_execution_arrival_window
#print axioms infinite_unit_execution_unbounded_arrival
#print axioms execution_interval_frequency_bound

end Generative.Conditional
