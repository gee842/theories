import SituatedRenewal

/-!
An explicitly scoped realization of maintenance demand through transport.
Inside amount, actual net unpowered inward transport, active compensatory
export, and work support
are coordinates of one process. This is a discrete nonnegative-quantity model,
not a formal reduction of a stochastic concentration equation or a definition
of life. Geometry, integer units, export cost and physical transport laws are
supplied. The maintained ceiling is an operative condition, not a death rule.
`inward` is the net unpowered transport over a modeled transition, restricted
to transitions where that net is nonnegative. Unpowered outward transport must
be included in the net, never discarded or truncated to manufacture demand.
This is not an account of every stochastic sample path or net-outward step.

The support account used by SituatedRenewal is DERIVED from transport balance
and work coupling. Demand is actual inward transport, not elapsed clock time.
Supply can come from previously formed support elsewhere in the same history;
its occurrence is not by itself novel formation or unlimited whole renewal.
-/

namespace Generative.LivingRealization

open SituatedRenewal

universe u v w

structure TransportLaw {State : Type u} {Action : Type v}
    (P : Process State Action) (Index : Type w) where
  inside : Index → State → Nat
  ceiling : Index → Nat
  work : Index → State → Nat
  inward : Index → State → Action → State → Nat
  exported : Index → State → Action → State → Nat
  supplied : Index → State → Action → State → Nat
  cost : Index → Nat
  transport : ∀ i s a t, P.step s a t →
    inside i t + exported i s a t = inside i s + inward i s a t
  coupling : ∀ i s a t, P.step s a t →
    work i t + cost i * exported i s a t ≤ work i s + supplied i s a t

variable {State : Type u} {Action : Type v} {Index : Type w}
variable {P : Process State Action}

def Within (law : TransportLaw P Index) (s : State) : Prop :=
  ∀ i, law.inside i s ≤ law.ceiling i

/-- Restriction to the operative regime; leaving it is not defined as death. -/
def maintained (law : TransportLaw P Index) : Process State Action where
  step s a t := P.step s a t ∧ Within law s ∧ Within law t

def ionHeadroom (law : TransportLaw P Index) (i : Index) (s : State) : Nat :=
  law.ceiling i - law.inside i s

def supportedHeadroom (law : TransportLaw P Index) (i : Index) (s : State) : Nat :=
  law.cost i * law.ceiling i - law.cost i * law.inside i s + law.work i s

/-- Transport balance alone derives an account for compensatory export. -/
theorem ion_account (law : TransportLaw P Index) (i : Index)
    {s t : State} {a : Action} (actual : (maintained law).step s a t) :
    ionHeadroom law i t + law.inward i s a t =
      ionHeadroom law i s + law.exported i s a t := by
  have balance := law.transport i s a t actual.1
  have before := actual.2.1 i
  have after := actual.2.2 i
  simp only [ionHeadroom]
  omega

/-- The maintenance-demand account is derived, not a field of TransportLaw. -/
theorem support_account (law : TransportLaw P Index) (i : Index)
    {s t : State} {a : Action} (actual : (maintained law).step s a t) :
    supportedHeadroom law i t + law.cost i * law.inward i s a t ≤
      supportedHeadroom law i s + law.supplied i s a t := by
  have balance := congrArg (fun n => law.cost i * n)
    (law.transport i s a t actual.1)
  simp only [Nat.mul_add] at balance
  have before := Nat.mul_le_mul_left (law.cost i) (actual.2.1 i)
  have after := Nat.mul_le_mul_left (law.cost i) (actual.2.2 i)
  have work := law.coupling i s a t actual.1
  simp only [supportedHeadroom]
  omega

def transportDependency (law : TransportLaw P Index) :
    DependencyLaw (maintained law) Index Unit where
  route := fun _ _ => ()
  remaining := ionHeadroom law
  demand := law.inward
  added := law.exported
  account := fun i _ _ _ actual _ => Nat.le_of_eq (ion_account law i actual)

def supportDependency (law : TransportLaw P Index) :
    DependencyLaw (maintained law) Index Unit where
  route := fun _ _ => ()
  remaining := supportedHeadroom law
  demand := fun i s a t => law.cost i * law.inward i s a t
  added := law.supplied
  account := fun i _ _ _ actual _ => support_account law i actual

/-- Actual inward transport beyond initial headroom requires actual export. -/
theorem compensation_required (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window (maintained law) states actions start length)
    (excess : ionHeadroom law i (states start) <
      totalDemand (transportDependency law) i states actions start length) :
    ∃ k, k < length ∧
      0 < law.exported i (states (start + k)) (actions (start + k))
        (states (start + k + 1)) := by
  obtain ⟨k, before, _, response⟩ :=
    response_before_exhaustion (transportDependency law) i states actions start length actual excess
  refine ⟨k, before, ?_⟩
  cases response with
  | inl added => exact added
  | inr changed => exact False.elim (changed rfl)

/-- Work support can compensate initially; only excess beyond both sources
forces an actual support input. No claim that input has just been created. -/
theorem support_input_required (law : TransportLaw P Index) (i : Index)
    (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window (maintained law) states actions start length)
    (excess : supportedHeadroom law i (states start) <
      totalDemand (supportDependency law) i states actions start length) :
    ∃ k, k < length ∧
      0 < law.supplied i (states (start + k)) (actions (start + k))
        (states (start + k + 1)) := by
  obtain ⟨k, before, _, response⟩ :=
    response_before_exhaustion (supportDependency law) i states actions start length actual excess
  refine ⟨k, before, ?_⟩
  cases response with
  | inl added => exact added
  | inr changed => exact False.elim (changed rfl)

/-- Indexed recurrence is conditional on actual cumulative inward transport,
not on positive use on each step or a universal lifetime. -/
theorem recurrent_support_input (law : TransportLaw P Index)
    (states : Nat → State) (actions : Nat → Action)
    (actual : ∀ n, (maintained law).step (states n) (actions n) (states (n + 1)))
    (persistentLoad : ∀ i start, ∃ length,
      supportedHeadroom law i (states start) <
        totalDemand (supportDependency law) i states actions start length) :
    ∀ i start, ∃ n, start ≤ n ∧ P.step (states n) (actions n) (states (n + 1)) ∧
      0 < law.supplied i (states n) (actions n) (states (n + 1)) := by
  intro i start
  obtain ⟨n, later, step, response⟩ :=
    every_required_dependency_recurrently_responds (supportDependency law)
      states actions actual persistentLoad i start
  refine ⟨n, later, step.1, ?_⟩
  cases response with
  | inl added => exact added
  | inr changed => exact False.elim (changed rfl)

/-- Moving a finite provision store inside the account preserves its depletion.
The store can stand for already formed support, including recyclable material. -/
theorem included_store_account (law : TransportLaw P Index) (i : Index)
    (store : State → Nat) {s t : State} {a : Action}
    (actual : (maintained law).step s a t)
    (transfer : store t + law.supplied i s a t ≤ store s) :
    (supportedHeadroom law i t + store t) + law.cost i * law.inward i s a t ≤
      supportedHeadroom law i s + store s := by
  have account := support_account law i actual
  omega

def storeDependency (law : TransportLaw P Index) (store : Index → State → Nat)
    (transfer : ∀ i s a t, P.step s a t →
      store i t + law.supplied i s a t ≤ store i s) :
    DependencyLaw (maintained law) Index Unit where
  route := fun _ _ => ()
  remaining := fun i s => supportedHeadroom law i s + store i s
  demand := fun i s a t => law.cost i * law.inward i s a t
  added := fun _ _ _ _ => 0
  account := fun i s a t actual _ => by
    simpa using included_store_account law i (store i) actual (transfer i s a t actual.1)

/-- Any actual maintained window respects the total initially available
support once internal provision is explicitly included. -/
theorem included_store_bounds_load (law : TransportLaw P Index)
    (store : Index → State → Nat)
    (transfer : ∀ i s a t, P.step s a t →
      store i t + law.supplied i s a t ≤ store i s)
    (i : Index) (states : Nat → State) (actions : Nat → Action) (start length : Nat)
    (actual : Window (maintained law) states actions start length) :
    totalDemand (storeDependency law store transfer) i states actions start length ≤
      supportedHeadroom law i (states start) + store i (states start) := by
  cases window_account_or_response (storeDependency law store transfer)
      i states actions start length actual with
  | inl bounded =>
    have account := bounded.2
    exact Nat.le_trans (Nat.le_add_left _ _) account
  | inr response =>
    obtain ⟨_, _, _, response⟩ := response
    cases response with
    | inl added => exact False.elim (Nat.not_lt_zero _ added)
    | inr changed => exact False.elim (changed rfl)

/-- Explicit finite witnesses use (inside, work) and
(inward, exported, supplied). They are not biological parameter estimates. -/
def exampleProcess : Process (Nat × Nat) (Nat × Nat × Nat) where
  step s a t := t.1 + a.2.1 = s.1 + a.1 ∧ t.2 + a.2.1 ≤ s.2 + a.2.2

def exampleLaw : TransportLaw exampleProcess Unit where
  inside := fun _ s => s.1
  ceiling := fun _ => 3
  work := fun _ s => s.2
  inward := fun _ _ a _ => a.1
  exported := fun _ _ a _ => a.2.1
  supplied := fun _ _ a _ => a.2.2
  cost := fun _ => 1
  transport := fun _ _ _ _ actual => actual.1
  coupling := fun _ _ _ _ actual => by simpa using actual.2

/-- Existing headroom permits inward transport without immediate export. -/
theorem headroom_can_accommodate_ingress :
    (maintained exampleLaw).step (2, 3) (1, 0, 0) (3, 3) ∧
      exampleLaw.exported () (2, 3) (1, 0, 0) (3, 3) = 0 ∧
      exampleLaw.supplied () (2, 3) (1, 0, 0) (3, 3) = 0 := by
  simp [maintained, exampleLaw, exampleProcess, Within]

/-- Retained work permits compensation without new support on that step. -/
theorem retained_work_can_compensate :
    (maintained exampleLaw).step (2, 3) (1, 1, 0) (2, 2) ∧
      0 < exampleLaw.exported () (2, 3) (1, 1, 0) (2, 2) ∧
      exampleLaw.supplied () (2, 3) (1, 1, 0) (2, 2) = 0 := by
  simp [maintained, exampleLaw, exampleProcess, Within]

/-- An inactive interval and later supported compensation share actual states.
The retained work consumed later is not silently reset after the idle step. -/
theorem inactive_then_compensating_history :
    Trace (maintained exampleLaw) (2, 3) [(0, 0, 0), (1, 1, 0)] (2, 2) := by
  apply Trace.cons (m := (2, 3))
  · simp [maintained, exampleLaw, exampleProcess, Within]
  · exact Trace.cons retained_work_can_compensate.1 (Trace.nil _)

end Generative.LivingRealization
