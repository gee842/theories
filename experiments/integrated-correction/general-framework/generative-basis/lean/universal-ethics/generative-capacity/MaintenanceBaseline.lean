import ObservableContinuation

/-
An intervention-relative target can shrink when the intervention disables its
old support. The original warranted task must be compared from the same origin,
not silently replaced by the remaining capability after that very intervention.
The normative standing of that finite task is supplied, not proved here.

This application retains the previous single-delivery window and actual route
costs. Retiring the old left line disables left and parallel execution; right is
independent. Delivery records arise only from enabled respond operations and
survive retirement. Completed delivery is not continuing support capacity.
No new installation, continuous-service invariant, real deadline, or legitimate
release procedure is claimed. Natural failure does not by itself settle a duty.
-/
namespace MaintenanceBaseline

/-- Transport permits actual completed work as well as still-live requirements.
Both the target correspondence and the meaning of completion remain explicit. -/
theorem target_transport_with_completion_gives_bound {Ω : Type}
    (domain : List Ω) (weight : Ω → Nat)
    (originDemand originOld currentDemand currentOld completed actualDelivery : Ω → Bool)
    (transport : ∀ h ∈ domain, ChanceAdequacy.target originDemand originOld h = true →
      completed h = true ∨ ChanceAdequacy.target currentDemand currentOld h = true)
    (recordMeaning : ∀ h ∈ domain, completed h = true → actualDelivery h = true)
    (currentFulfilled : ChanceAdequacy.Fulfilled domain currentDemand currentOld actualDelivery)
    (positive : 0 < ChanceAdequacy.total domain weight) :
    ChanceAdequacy.Fulfilled domain originDemand originOld actualDelivery ∧
    0 < ChanceAdequacy.total domain weight ∧
    ChanceAdequacy.mass domain weight (ChanceAdequacy.target originDemand originOld) ≤
      ChanceAdequacy.mass domain weight actualDelivery ∧
    ChanceAdequacy.mass domain weight actualDelivery ≤ ChanceAdequacy.total domain weight := by
  have original : ChanceAdequacy.Fulfilled domain originDemand originOld actualDelivery := by
    intro h member required
    rcases transport h member required with done | remains
    · exact recordMeaning h member done
    · exact currentFulfilled h member remains
  exact ⟨original, ChanceAdequacy.fulfillment_gives_chance_floor domain weight
    originDemand originOld actualDelivery positive original⟩

structure Frame where
  plant : ObservableContinuation.State
  oldLive : Bool
  delivered : Bool
  deriving DecidableEq, Repr

def initial (budget : Nat) (mode : Bool) : Frame :=
  ⟨ObservableContinuation.initial budget mode, true, false⟩

/-- One delivery is owed. This is not a continuous demand or a release flag. -/
def demand (s : Frame) : Bool := !s.delivered

def oldSupport (s : Frame) : Bool :=
  s.oldLive && ObservableContinuation.oldWorks s.plant.mode

def retire (s : Frame) : Frame := {s with oldLive := false}

def enabled (s : Frame) : ObservableContinuation.Action → Bool
  | .left => s.oldLive
  | .right => true
  | .parallel => s.oldLive

def deliver (a : ObservableContinuation.Action) (s : Frame) : Option Frame := do
  if enabled s a then
    let after ← ObservableContinuation.respond s.plant a
    pure {s with plant := after, delivered := s.delivered || after.supported}
  else none

def deliverThenRetire (a : ObservableContinuation.Action) (s : Frame) : Option Frame :=
  (deliver a s).map retire

def actualDelivery (a : ObservableContinuation.Action) (budget : Nat) (mode : Bool) : Bool :=
  (deliverThenRetire a (initial budget mode)).any Frame.delivered

/-- Retirement changes physical availability. Recomputing oldWorks afterwards
makes the current antecedent empty although the original delivery is absent. -/
theorem retirement_can_erase_recomputed_target_without_fulfilling_origin :
    oldSupport (initial 1 false) = true ∧
    (∀ mode, demand (retire (initial 1 mode)) = true ∧
      oldSupport (retire (initial 1 mode)) = false ∧
      (retire (initial 1 mode)).delivered = false) ∧
    ChanceAdequacy.Fulfilled [false, true]
      (fun mode => demand (retire (initial 1 mode)))
      (fun mode => oldSupport (retire (initial 1 mode)))
      (fun mode => (retire (initial 1 mode)).delivered) ∧
    ¬ ChanceAdequacy.Fulfilled [false, true] (fun _ => true) ObservableContinuation.oldWorks
      (fun mode => (retire (initial 1 mode)).delivered) ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) ObservableContinuation.oldWorks = 1 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1)
      (fun mode => (retire (initial 1 mode)).delivered) = 0 := by
  refine ⟨rfl, ?_, ?_, ?_, rfl, rfl⟩
  · intro mode
    cases mode <;> exact ⟨rfl, rfl, rfl⟩
  · intro mode _ required
    cases mode <;> cases required
  · intro fulfilled
    have impossible := fulfilled false (by simp) (by rfl)
    cases impossible

/-- The existing funded parallel action actually delivers before retirement.
Its successful delivery record, not the vanished current target, fulfills the
original undertaking and the extended single-delivery profile. -/
theorem actual_extended_delivery_survives_retirement :
    (∀ mode, deliverThenRetire .parallel (initial 2 mode) =
      some ⟨⟨mode, 0, true⟩, false, true⟩) ∧
    ChanceAdequacy.Fulfilled [false, true] (fun _ => true) ObservableContinuation.oldWorks
      (actualDelivery .parallel 2) ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) ObservableContinuation.oldWorks = 1 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) (actualDelivery .parallel 2) = 2 := by
  refine ⟨?_, ?_, rfl, rfl⟩
  · intro mode
    cases mode <;> rfl
  · intro mode _ _
    cases mode <;> rfl

/-- Fulfilled one-shot maintenance can end: no perpetual old device or unused
future route is required by this already-delivered task. Other needs remain
outside this particular obligation, including the unserved true-mode case. -/
theorem completed_single_delivery_allows_retirement :
    (∀ mode, deliverThenRetire .left (initial 1 mode) =
      some ⟨⟨mode, 0, !mode⟩, false, !mode⟩) ∧
    ChanceAdequacy.Fulfilled [false, true] (fun _ => true) ObservableContinuation.oldWorks
      (actualDelivery .left 1) ∧
    (deliverThenRetire .left (initial 1 false)).map
      (fun s => (demand s, s.oldLive, s.delivered, s.plant.budget)) =
        some (false, false, true, 0) := by
  refine ⟨?_, ?_, rfl⟩
  · intro mode
    cases mode <;> rfl
  · intro mode _ required
    cases mode <;> exact required

end MaintenanceBaseline
