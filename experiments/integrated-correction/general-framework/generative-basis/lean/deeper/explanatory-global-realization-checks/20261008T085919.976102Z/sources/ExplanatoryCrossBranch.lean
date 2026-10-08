import ExplanatoryCoexistence

/-! Real failures and limits of local certificates. Omitting the support used
below an intermediate node can hide a repeated leaf. Exclusive-slot laws do not
cover every form of joint realization: a finite shared-capacity process shows
why pairwise successes alone do not settle larger joint demands. -/
namespace Generative.ExplanatoryCrossBranch
open ExplanatoryJointness ExplanatoryFootprints ExplanatoryCoexistence

/-- Only immediate sibling supports are compared; descendant containment is
not recorded. This is deliberately a weaker certificate, not a full division. -/
def weakJoint (_s l r : List Bool) : Prop := Apart l r

def crossing : Plan (List Bool) :=
  .pair (.pair (.leaf [false]) (.leaf [true])) (.leaf [false])

theorem weak_local_certificate : Realizes weakJoint (Supported support) [false, true] crossing := by
  refine ⟨[], [false], ?_, ?_, ?_⟩
  · simp [weakJoint, Apart]
  · refine ⟨[false], [true], ?_, ?_, ?_⟩
    · simp [weakJoint, Apart]
    · simp [Realizes, Supported, support]
    · simp [Realizes, Supported, support]
  · simp [Realizes, Supported, support]

theorem weak_has_local_separation : Separate (@support Bool) weakJoint := fun _ _ _ h => h

theorem weak_lacks_inheritance : ¬ Within (@support Bool) weakJoint := by
  intro h
  have joint : weakJoint [] [false] [true] := by simp [weakJoint, Apart]
  have impossible := (h [] [false] [true] joint).1 false (by simp [support])
  simp [support] at impossible

theorem crossing_requests_conflict : ¬ (Requests crossing).Nodup := by
  simp [Requests, crossing, List.nodup_cons]

theorem crossing_no_holding_history :
    ¬ ∃ final, Trace (process [false, true]) [] (Requests crossing) final := by
  intro h
  exact crossing_requests_conflict ((exists_trace_iff ..).mp h).1

/-- This relation records containment but omits competition between siblings. -/
def withinOnly (s l r : List Bool) : Prop :=
  (∀ a, a ∈ l → a ∈ s) ∧ (∀ a, a ∈ r → a ∈ s)

def duplicate : Plan (List Bool) := .pair (.leaf [false]) (.leaf [false])

theorem within_only_inheritance : Within (@support Bool) withinOnly := fun _ _ _ h => h

theorem within_only_accepts_duplicate :
    Realizes withinOnly (Supported support) [false] duplicate := by
  refine ⟨[false], [false], ⟨fun _ h => h, fun _ h => h⟩, ?_, ?_⟩ <;>
    simp [Realizes, Supported, support]

theorem within_only_no_holding_history :
    ¬ ∃ final, Trace (process [false]) [] (Requests duplicate) final := by
  intro h
  have nodup := ((exists_trace_iff ..).mp h).1
  simp [Requests, duplicate, List.nodup_cons] at nodup

theorem repaired_rejects_crossing :
    ¬ Realizes joint (Supported support) [false, true] crossing :=
  fun h => crossing_requests_conflict ((realize_iff_supported ..).mp h).1

def threeDistinct : Plan (List Nat) :=
  .pair (.pair (.leaf [0]) (.leaf [1])) (.leaf [2])

theorem repaired_positive_and_holds :
    Realizes joint (Supported support) [0, 1, 2] threeDistinct ∧
    Trace (process [0, 1, 2]) [] (Requests threeDistinct) (Requests threeDistinct) := by
  have supported : Supported support [0, 1, 2] (Requests threeDistinct) := by
    simp [Supported, support, Requests, threeDistinct, List.nodup_cons]
  exact ⟨(realize_iff_supported ..).mpr supported, (empty_trace_iff_supported ..).mpr supported⟩

/-- Every occurrence is another held activity. Each acquisition raises the
shared load by one, and none releases during the episode. -/
def capacityProcess (capacity : Nat) : Process Nat Unit where
  step load _ next := load < capacity ∧ next = load + 1

theorem capacity_trace_iff (capacity : Nat) (actions : List Unit) :
    ∀ load final, load ≤ capacity →
      (Trace (capacityProcess capacity) load actions final ↔
        load + actions.length ≤ capacity ∧ final = load + actions.length) := by
  induction actions with
  | nil =>
    intro load final bound
    constructor
    · intro h; cases h; exact ⟨by simpa, by simp⟩
    · rintro ⟨_, eq⟩
      have same : final = load := by simpa using eq
      rw [same]; exact Trace.nil load
  | cons a actions ih =>
    intro load final bound
    constructor
    · intro h
      cases h with
      | cons step tail =>
        rcases step with ⟨less, rfl⟩
        obtain ⟨size, same⟩ := (ih _ _ (by omega)).mp tail
        simp only [List.length_cons]
        constructor <;> omega
    · rintro ⟨size, same⟩
      simp only [List.length_cons] at size same
      apply Trace.cons (m := load + 1)
      · exact ⟨by omega, rfl⟩
      · exact (ih _ _ (by omega)).mpr ⟨by omega, by omega⟩

theorem capacity_admission_iff (capacity : Nat) (actions : List Unit) :
    (∃ final, Trace (capacityProcess capacity) 0 actions final) ↔ actions.length ≤ capacity := by
  constructor
  · rintro ⟨final, h⟩
    simpa using ((capacity_trace_iff capacity actions 0 final (Nat.zero_le _)).mp h).1
  · intro h
    exact ⟨actions.length, (capacity_trace_iff capacity actions 0 _ (Nat.zero_le _)).mpr
      ⟨by simpa, by simp⟩⟩

theorem same_single_and_pair_admission (actions : List Unit) (short : actions.length ≤ 2) :
    (∃ final, Trace (capacityProcess 2) 0 actions final) ∧
    (∃ final, Trace (capacityProcess 3) 0 actions final) :=
  ⟨(capacity_admission_iff ..).mpr short, (capacity_admission_iff ..).mpr (by omega)⟩

theorem triple_capacity_distinguishes :
    (¬ ∃ final, Trace (capacityProcess 2) 0 [(), (), ()] final) ∧
    (∃ final, Trace (capacityProcess 3) 0 [(), (), ()] final) := by
  simp [capacity_admission_iff]

theorem any_finite_arity_can_miss_next (n : Nat) :
    (∀ actions : List Unit, actions.length ≤ n →
      (∃ final, Trace (capacityProcess n) 0 actions final) ∧
      ∃ final, Trace (capacityProcess (n + 1)) 0 actions final) ∧
    (¬ ∃ final, Trace (capacityProcess n) 0 (List.replicate (n + 1) ()) final) ∧
    (∃ final, Trace (capacityProcess (n + 1)) 0 (List.replicate (n + 1) ()) final) := by
  constructor
  · intro actions short
    exact ⟨(capacity_admission_iff ..).mpr short, (capacity_admission_iff ..).mpr (by omega)⟩
  · simp [capacity_admission_iff]

end Generative.ExplanatoryCrossBranch

#print axioms Generative.ExplanatoryCrossBranch.weak_local_certificate
#print axioms Generative.ExplanatoryCrossBranch.weak_has_local_separation
#print axioms Generative.ExplanatoryCrossBranch.weak_lacks_inheritance
#print axioms Generative.ExplanatoryCrossBranch.crossing_requests_conflict
#print axioms Generative.ExplanatoryCrossBranch.crossing_no_holding_history
#print axioms Generative.ExplanatoryCrossBranch.within_only_inheritance
#print axioms Generative.ExplanatoryCrossBranch.within_only_accepts_duplicate
#print axioms Generative.ExplanatoryCrossBranch.within_only_no_holding_history
#print axioms Generative.ExplanatoryCrossBranch.repaired_rejects_crossing
#print axioms Generative.ExplanatoryCrossBranch.repaired_positive_and_holds
#print axioms Generative.ExplanatoryCrossBranch.capacity_trace_iff
#print axioms Generative.ExplanatoryCrossBranch.capacity_admission_iff
#print axioms Generative.ExplanatoryCrossBranch.same_single_and_pair_admission
#print axioms Generative.ExplanatoryCrossBranch.triple_capacity_distinguishes
#print axioms Generative.ExplanatoryCrossBranch.any_finite_arity_can_miss_next
