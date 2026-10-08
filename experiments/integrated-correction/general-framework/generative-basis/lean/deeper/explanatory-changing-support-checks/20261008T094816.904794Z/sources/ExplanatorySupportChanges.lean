import ExplanatoryStablePlans

/-! Concrete reachable changes invalidate, restore or create support for a
fixed target. A real occupation/release loop preserves readiness forever but
never schedules the target's progress. -/
namespace Generative.ExplanatorySupportChanges
open ExplanatoryChangingSupport ExplanatoryStablePlans ExplanatoryCoexistence
open ExplanatoryJointness ExplanatoryFootprints

def ready : Position Nat := ⟨⟨[0, 1], []⟩, [], [0, 1]⟩
def stolen : Position Nat := ⟨after ready.configuration (.take 0), [], [0, 1]⟩
def partlyHeld : Position Nat := ⟨⟨[0, 1], [0]⟩, [0], [1]⟩
def lost : Position Nat := ⟨after partlyHeld.configuration (.release 0), [0], [1]⟩

theorem ready_valid : Valid ready := by
  simp [Valid, Certificate, Admissible, ready, List.nodup_cons]

theorem competing_acquisition_occurs : raw.step ready (.change (.take 0)) stolen := by
  exact ⟨by simp [enabled, ready], rfl⟩

theorem competing_acquisition_invalidates : ¬ Valid stolen := by
  simp [Valid, Certificate, Admissible, stolen, ready, after]

def snapshot (s : Position Nat) := (s.configuration.available, s.done, s.remaining)

theorem static_snapshot_unchanged : snapshot ready = snapshot stolen := rfl

theorem no_snapshot_certificate_reader :
    ¬ ∃ read : (List Nat × List Nat × List Nat) → Prop,
      ∀ s : Position Nat, read (snapshot s) ↔ Valid s := by
  rintro ⟨read, correct⟩
  have yes := (correct ready).mpr ready_valid
  have same : read (snapshot stolen) := static_snapshot_unchanged ▸ yes
  exact competing_acquisition_invalidates ((correct stolen).mp same)

theorem stale_plan_cannot_advance : ¬ ∃ next, raw.step stolen .advance next := by
  rintro ⟨next, a, rest, eq, en, _⟩
  have ha : a = 0 := (List.cons.inj eq).1.symm
  subst a
  simp [enabled, stolen, ready, after] at en

theorem release_restores : guarded.step stolen (.change (.release 0)) ready := by
  constructor
  · constructor
    · simp [enabled, stolen, ready, after]
    · rfl
  · simp [Guard, stolen]

theorem restored_plan_completes : ∃ final : Position Nat,
    Trace guarded stolen [.change (.release 0), .advance, .advance] final ∧
      final.remaining = [] ∧ ∀ a, a ∈ [0, 1] → a ∈ final.configuration.busy := by
  obtain ⟨final, tail, empty, done, valid⟩ := complete_by_advancing ready.remaining
    ready.configuration ready.done ready_valid
  refine ⟨final, Trace.cons release_restores tail, empty, ?_⟩
  intro a mem
  have same : final.done = [0, 1] := done
  exact valid.2.1 a (same.symm ▸ mem)

theorem completed_support_can_be_lost :
    Valid partlyHeld ∧ raw.step partlyHeld (.change (.release 0)) lost ∧ ¬ Valid lost := by
  constructor
  · simp [Valid, Certificate, Admissible, partlyHeld, List.nodup_cons]
  · constructor
    · exact ⟨by simp [enabled, partlyHeld], rfl⟩
    · simp [Valid, Certificate, Admissible, lost, partlyHeld, after, without]

theorem pending_success_omits_completed_loss :
    Admissible lost.configuration.available lost.configuration.busy lost.remaining ∧ ¬ Valid lost := by
  exact ⟨by simp [Admissible, lost, partlyHeld, after, without], completed_support_can_be_lost.2.2⟩

def unformed : Position Nat := ⟨⟨[0], []⟩, [], [1]⟩
def formed : Position Nat := ⟨after unformed.configuration (.form 0 1), [], [1]⟩

theorem formation_creates_readiness :
    (¬ Valid unformed) ∧ guarded.step unformed (.change (.form 0 1)) formed ∧ Valid formed := by
  constructor
  · simp [Valid, Certificate, Admissible, unformed]
  · constructor
    · exact ⟨⟨by simp [enabled, unformed], rfl⟩, True.intro⟩
    · simp [Valid, Certificate, Admissible, formed, unformed, after, List.nodup_cons]

theorem formation_then_acquisition : ∃ final : Position Nat,
    Trace guarded unformed [.change (.form 0 1), .advance] final ∧
      final.remaining = [] ∧ 1 ∈ final.configuration.busy := by
  obtain ⟨final, tail, empty, done, valid⟩ := complete_by_advancing formed.remaining
    formed.configuration formed.done formation_creates_readiness.2.2
  refine ⟨final, Trace.cons formation_creates_readiness.2.1 tail, empty, ?_⟩
  have same : final.done = [1] := done
  exact valid.2.1 1 (same.symm ▸ List.mem_cons_self)

def waiting : Position Nat := ⟨⟨[0, 1], []⟩, [], [0]⟩
def unrelatedHeld : Position Nat := ⟨after waiting.configuration (.take 1), [], [0]⟩

theorem unrelated_cycle :
    Valid waiting ∧ guarded.step waiting (.change (.take 1)) unrelatedHeld ∧
      guarded.step unrelatedHeld (.change (.release 1)) waiting := by
  constructor
  · simp [Valid, Certificate, Admissible, waiting, List.nodup_cons]
  · constructor
    · exact ⟨⟨by simp [enabled, waiting], rfl⟩, by simp [Guard, waiting]⟩
    · exact ⟨⟨by simp [enabled, unrelatedHeld, waiting, after], rfl⟩,
        by simp [Guard, unrelatedHeld]⟩

theorem never_finishing_schedule :
    ∃ states : Nat → Position Nat, ∃ events : Nat → Event Nat,
      Valid (states 0) ∧
      (∀ n, guarded.step (states n) (events n) (states (n + 1))) ∧
      ∀ n, (states n).remaining = [0] := by
  let states := fun n => if n % 2 = 0 then waiting else unrelatedHeld
  let events := fun n => if n % 2 = 0 then Event.change (.take 1) else Event.change (.release 1)
  refine ⟨states, events, unrelated_cycle.1, ?_, ?_⟩
  · intro n
    by_cases even : n % 2 = 0
    · have odd : (n + 1) % 2 ≠ 0 := by omega
      simpa [states, events, even, odd] using unrelated_cycle.2.1
    · have even' : (n + 1) % 2 = 0 := by omega
      simpa [states, events, even, even'] using unrelated_cycle.2.2
  · intro n
    by_cases even : n % 2 = 0 <;> simp [states, even, waiting, unrelatedHeld]

end Generative.ExplanatorySupportChanges

#print axioms Generative.ExplanatorySupportChanges.ready_valid
#print axioms Generative.ExplanatorySupportChanges.competing_acquisition_occurs
#print axioms Generative.ExplanatorySupportChanges.competing_acquisition_invalidates
#print axioms Generative.ExplanatorySupportChanges.static_snapshot_unchanged
#print axioms Generative.ExplanatorySupportChanges.no_snapshot_certificate_reader
#print axioms Generative.ExplanatorySupportChanges.stale_plan_cannot_advance
#print axioms Generative.ExplanatorySupportChanges.release_restores
#print axioms Generative.ExplanatorySupportChanges.restored_plan_completes
#print axioms Generative.ExplanatorySupportChanges.completed_support_can_be_lost
#print axioms Generative.ExplanatorySupportChanges.pending_success_omits_completed_loss
#print axioms Generative.ExplanatorySupportChanges.formation_creates_readiness
#print axioms Generative.ExplanatorySupportChanges.formation_then_acquisition
#print axioms Generative.ExplanatorySupportChanges.unrelated_cycle
#print axioms Generative.ExplanatorySupportChanges.never_finishing_schedule
