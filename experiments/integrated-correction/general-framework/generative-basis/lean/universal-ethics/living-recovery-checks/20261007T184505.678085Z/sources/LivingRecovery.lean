import LivingRealization

/-!
Gross passive transport and endpoint restoration on actual process histories.
All fluxes are nonnegative quantities. Passive inward and passive outward
transport are retained separately; neither signed load nor an excursion is
clipped away. Active export alone has the supplied work-coupling lower bound.

No operative bound is required at intermediate states. A bound on the final
amount supplies a necessary accounting condition for that actual return. It
does not establish physiological recovery, retained repair machinery, viability,
continuous interstep safety, or refinement of a stochastic concentration model.
Amount units, geometry correspondence, constant indexed cost, the transport law
and work coupling remain supplied physical-model premises.
-/

namespace Generative.LivingRecovery

open SituatedRenewal

universe u v w

structure TransportLaw {State : Type u} {Action : Type v}
    (P : Process State Action) (Index : Type w) where
  inside : Index → State → Nat
  work : Index → State → Nat
  inward : Index → State → Action → State → Nat
  passiveOut : Index → State → Action → State → Nat
  exported : Index → State → Action → State → Nat
  supplied : Index → State → Action → State → Nat
  cost : Index → Nat
  transport : ∀ i s a t, P.step s a t →
    inside i t + exported i s a t + passiveOut i s a t =
      inside i s + inward i s a t
  coupling : ∀ i s a t, P.step s a t →
    work i t + cost i * exported i s a t ≤ work i s + supplied i s a t

variable {State : Type u} {Action : Type v} {Index : Type w}
variable {P : Process State Action}

def fluxSum (amount : State → Action → State → Nat)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat) : Nat :=
  sumWindow (fun n => amount (states n) (actions n) (states (n + 1))) start length

theorem fluxSum_succ (amount : State → Action → State → Nat)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat) :
    fluxSum amount states actions start (length + 1) =
      fluxSum amount states actions start length +
        amount (states (start + length)) (actions (start + length))
          (states (start + length + 1)) := rfl

/-- A positive actual total has an actual positive contributing transition. -/
theorem positive_flux_has_event (amount : State → Action → State → Nat)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (positive : 0 < fluxSum amount states actions start length) :
    ∃ k, k < length ∧ 0 < amount (states (start + k))
      (actions (start + k)) (states (start + k + 1)) := by
  induction length with
  | zero => exact False.elim (Nat.not_lt_zero _ positive)
  | succ length ih =>
    by_cases earlier : 0 < fluxSum amount states actions start length
    · obtain ⟨k, before, event⟩ := ih earlier
      exact ⟨k, Nat.lt_trans before (Nat.lt_succ_self _), event⟩
    · refine ⟨length, Nat.lt_succ_self _, ?_⟩
      rw [fluxSum_succ] at positive
      omega

/-- Exact cumulative transport; no intermediate-state bound is assumed. -/
theorem window_transport (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length) :
    law.inside i (states (start + length)) +
        fluxSum (law.exported i) states actions start length +
        fluxSum (law.passiveOut i) states actions start length =
      law.inside i (states start) + fluxSum (law.inward i) states actions start length := by
  induction length with
  | zero => simp [fluxSum, sumWindow]
  | succ length ih =>
    have windowPrefix : Window P states actions start length :=
      fun k before => actual k (Nat.lt_trans before (Nat.lt_succ_self _))
    have prior := ih windowPrefix
    have last := law.transport i _ _ _ (actual length (Nat.lt_succ_self _))
    simp only [fluxSum_succ, Nat.add_assoc]
    simp only [Nat.add_assoc] at last
    omega

/-- Work coupling telescopes independently of where the amount goes. -/
theorem window_work (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length) :
    law.work i (states (start + length)) +
        law.cost i * fluxSum (law.exported i) states actions start length ≤
      law.work i (states start) + fluxSum (law.supplied i) states actions start length := by
  induction length with
  | zero => simp [fluxSum, sumWindow]
  | succ length ih =>
    have windowPrefix : Window P states actions start length :=
      fun k before => actual k (Nat.lt_trans before (Nat.lt_succ_self _))
    have prior := ih windowPrefix
    have last := law.coupling i _ _ _ (actual length (Nat.lt_succ_self _))
    simp only [fluxSum_succ, Nat.mul_add, Nat.add_assoc]
    simp only [Nat.add_assoc] at last
    omega

/-- A subtraction-free necessary budget for actual return to a final bound.
The initial state and every intermediate state may exceed that bound. -/
theorem recovery_account (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length bound : Nat)
    (actual : Window P states actions start length)
    (returned : law.inside i (states (start + length)) ≤ bound) :
    law.cost i * law.inside i (states start) +
        law.cost i * fluxSum (law.inward i) states actions start length +
        law.work i (states (start + length)) ≤
      law.cost i * bound + law.work i (states start) +
        fluxSum (law.supplied i) states actions start length +
        law.cost i * fluxSum (law.passiveOut i) states actions start length := by
  have transport := congrArg (fun n => law.cost i * n)
    (window_transport law i states actions start length actual)
  simp only [Nat.mul_add] at transport
  have work := window_work law i states actions start length actual
  have finalBound := Nat.mul_le_mul_left (law.cost i) returned
  omega

/-- Passive outward relief is included before concluding export is necessary. -/
theorem compensation_required (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length bound : Nat)
    (actual : Window P states actions start length)
    (returned : law.inside i (states (start + length)) ≤ bound)
    (excess : bound + fluxSum (law.passiveOut i) states actions start length <
      law.inside i (states start) + fluxSum (law.inward i) states actions start length) :
    ∃ k, k < length ∧ 0 < law.exported i (states (start + k))
      (actions (start + k)) (states (start + k + 1)) := by
  apply positive_flux_has_event (law.exported i) states actions start length
  have transport := window_transport law i states actions start length actual
  omega

/-- Input is forced only after both inherited work and passive relief are
credited. This is actual input to the coordinate, not proof of novel formation. -/
theorem support_input_required (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length bound : Nat)
    (actual : Window P states actions start length)
    (returned : law.inside i (states (start + length)) ≤ bound)
    (excess : law.cost i * bound + law.work i (states start) +
        law.cost i * fluxSum (law.passiveOut i) states actions start length <
      law.cost i * law.inside i (states start) +
        law.cost i * fluxSum (law.inward i) states actions start length) :
    ∃ k, k < length ∧ 0 < law.supplied i (states (start + k))
      (actions (start + k)) (states (start + k + 1)) := by
  apply positive_flux_has_event (law.supplied i) states actions start length
  have account := recovery_account law i states actions start length bound actual returned
  omega

/-- A finite included provision coordinate pays all actual support transfers. -/
theorem window_store (law : TransportLaw P Index) (i : Index)
    (store : State → Nat)
    (transfer : ∀ s a t, P.step s a t → store t + law.supplied i s a t ≤ store s)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window P states actions start length) :
    store (states (start + length)) +
      fluxSum (law.supplied i) states actions start length ≤ store (states start) := by
  induction length with
  | zero => simp [fluxSum, sumWindow]
  | succ length ih =>
    have windowPrefix : Window P states actions start length :=
      fun k before => actual k (Nat.lt_trans before (Nat.lt_succ_self _))
    have prior := ih windowPrefix
    have last := transfer _ _ _ (actual length (Nat.lt_succ_self _))
    simp only [fluxSum_succ, Nat.add_assoc]
    simp only [Nat.add_assoc] at last
    omega

/-- Including finite upstream provision does not turn transfer into an
unlimited source. No limit on passive outward relief is invented. -/
theorem included_store_bounds_recovery (law : TransportLaw P Index) (i : Index)
    (store : State → Nat)
    (transfer : ∀ s a t, P.step s a t → store t + law.supplied i s a t ≤ store s)
    (states : Nat → State) (actions : Nat → Action) (start length bound : Nat)
    (actual : Window P states actions start length)
    (returned : law.inside i (states (start + length)) ≤ bound) :
    law.cost i * law.inside i (states start) +
        law.cost i * fluxSum (law.inward i) states actions start length +
        law.work i (states (start + length)) + store (states (start + length)) ≤
      law.cost i * bound + law.work i (states start) + store (states start) +
        law.cost i * fluxSum (law.passiveOut i) states actions start length := by
  have account := recovery_account law i states actions start length bound actual returned
  have provision := window_store law i store transfer states actions start length actual
  omega

/-- Recurrence needs actual successful-return windows with excess net load.
Neither returns nor persistent load are inferred from mere passage of time. -/
theorem recurrent_input_at_returns (law : TransportLaw P Index)
    (states : Nat → State) (actions : Nat → Action)
    (actual : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (returnLoad : ∀ i start, ∃ length bound,
      law.inside i (states (start + length)) ≤ bound ∧
      law.cost i * bound + law.work i (states start) +
          law.cost i * fluxSum (law.passiveOut i) states actions start length <
        law.cost i * law.inside i (states start) +
          law.cost i * fluxSum (law.inward i) states actions start length) :
    ∀ i start, ∃ n, start ≤ n ∧ P.step (states n) (actions n) (states (n + 1)) ∧
      0 < law.supplied i (states n) (actions n) (states (n + 1)) := by
  intro i start
  obtain ⟨length, bound, returned, excess⟩ := returnLoad i start
  obtain ⟨k, _, input⟩ := support_input_required law i states actions start length bound
    (fun k _ => actual (start + k)) returned excess
  exact ⟨start + k, Nat.le_add_right _ _, actual _, input⟩

/-- The prior nonnegative-net model embeds with no separately recorded passive
outward amount. Existing source files and proved scopes remain unchanged. -/
def fromRealization (law : LivingRealization.TransportLaw P Index) : TransportLaw P Index where
  inside := law.inside
  work := law.work
  inward := law.inward
  passiveOut := fun _ _ _ _ => 0
  exported := law.exported
  supplied := law.supplied
  cost := law.cost
  transport := fun i s a t actual => by simpa using law.transport i s a t actual
  coupling := law.coupling

theorem embedded_passive_total_zero (law : LivingRealization.TransportLaw P Index)
    (i : Index) (states : Nat → State) (actions : Nat → Action) (start length : Nat) :
    fluxSum ((fromRealization law).passiveOut i) states actions start length = 0 := by
  induction length with
  | zero => rfl
  | succ length ih => rw [fluxSum_succ, ih]; rfl

theorem old_maintained_window_is_unrestricted
    (law : LivingRealization.TransportLaw P Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window (LivingRealization.maintained law) states actions start length) :
    Window P states actions start length :=
  fun k before => (actual k before).1

/-- Finite witnesses: state=(inside,work), action=(inward,passiveOut,activeOut,input).
They are structural examples, not estimates or empirical recovery models. -/
def exampleProcess : Process (Nat × Nat) (Nat × Nat × Nat × Nat) where
  step s a t :=
    t.1 + a.2.2.1 + a.2.1 = s.1 + a.1 ∧
      t.2 + a.2.2.1 ≤ s.2 + a.2.2.2

def exampleLaw : TransportLaw exampleProcess Unit where
  inside := fun _ s => s.1
  work := fun _ s => s.2
  inward := fun _ _ a _ => a.1
  passiveOut := fun _ _ a _ => a.2.1
  exported := fun _ _ a _ => a.2.2.1
  supplied := fun _ _ a _ => a.2.2.2
  cost := fun _ => 1
  transport := fun _ _ _ _ actual => actual.1
  coupling := fun _ _ _ _ actual => by simpa using actual.2

/-- Passive outward relief can restore the amount with zero work and input. -/
theorem passive_relief_without_work :
    exampleProcess.step (4, 0) (0, 2, 0, 0) (2, 0) ∧
      exampleLaw.inside () (2, 0) ≤ 3 ∧
      exampleLaw.exported () (4, 0) (0, 2, 0, 0) (2, 0) = 0 ∧
      exampleLaw.supplied () (4, 0) (0, 2, 0, 0) (2, 0) = 0 := by
  simp [exampleProcess, exampleLaw]

/-- An actual excursion and passive return, retaining both signs of transfer. -/
theorem passive_excursion_then_return :
    exampleProcess.step (2, 0) (3, 0, 0, 0) (5, 0) ∧
      3 < exampleLaw.inside () (5, 0) ∧
      exampleProcess.step (5, 0) (0, 3, 0, 0) (2, 0) ∧
      Trace exampleProcess (2, 0) [(3, 0, 0, 0), (0, 3, 0, 0)] (2, 0) := by
  have up : exampleProcess.step (2, 0) (3, 0, 0, 0) (5, 0) := by simp [exampleProcess]
  have down : exampleProcess.step (5, 0) (0, 3, 0, 0) (2, 0) := by simp [exampleProcess]
  exact ⟨up, by decide, down, Trace.cons up (Trace.cons down (Trace.nil _))⟩

/-- Retained work can support actual return after an excursion, without input.
The high intermediate amount is not removed from the composed history. -/
theorem retained_work_restores_after_excursion :
    exampleProcess.step (2, 3) (3, 0, 0, 0) (5, 3) ∧
      3 < exampleLaw.inside () (5, 3) ∧
      exampleProcess.step (5, 3) (0, 0, 3, 0) (2, 0) ∧
      Trace exampleProcess (2, 3) [(3, 0, 0, 0), (0, 0, 3, 0)] (2, 0) := by
  have up : exampleProcess.step (2, 3) (3, 0, 0, 0) (5, 3) := by simp [exampleProcess]
  have down : exampleProcess.step (5, 3) (0, 0, 3, 0) (2, 0) := by simp [exampleProcess]
  exact ⟨up, by decide, down, Trace.cons up (Trace.cons down (Trace.nil _))⟩

end Generative.LivingRecovery
