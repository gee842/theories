import ProtocolCompletion
import ProtocolExamples

/-! Applications to the unchanged paid first-return example. No new event,
resource, abort report, scheduler or source restoration is supplied. -/

namespace Generative.Learning.Protocols.Completion.Examples

open Generative.Learning.Protocols.Examples

def fundedLive (_ : Unit) (s : Inventory) : Prop :=
  match s.phase with
  | .ready => 0 < s.fuel ∧ 0 < s.source
  | .busy => 0 < s.source

def phaseRank (s : Inventory) : Nat :=
  match s.phase with
  | .ready => 1
  | .busy => 0

theorem nonstall_contract :
    CompletionContract (protocol false) fundedLive phaseRank := by
  constructor
  · intro a s hs
    rcases s with ⟨phase, fuel, source⟩
    cases phase with
    | ready =>
      cases fuel with
      | zero => simp [fundedLive] at hs
      | succ fuel => exact ⟨.pay, busy fuel source, ⟨.pay fuel source, trivial⟩⟩
    | busy =>
      cases source with
      | zero => simp [fundedLive] at hs
      | succ source => exact ⟨.tick, ready (fuel + 1) source, ⟨.replenish fuel source, trivial⟩⟩
  · intro a s e t hs step inside
    cases step.1 <;> simp_all [fundedLive, protocol, ready, busy]
  · intro a s e t hs step inside
    cases step.1 <;> simp_all [phaseRank, protocol, ready, busy]

/-- General progress gives completion within two actual micro-events. -/
theorem funded_completion (fuel source : Nat) :
    ∃ word t, BlockPath (protocol false) () (ready (fuel + 1) (source + 1)) word t ∧
      word.length ≤ 2 := by
  exact completion_exists nonstall_contract (by simp [fundedLive, ready])

theorem all_funded_blocks_bounded (fuel source : Nat) {word : List MicroEvent} {t : Inventory}
    (block : BlockPath (protocol false) () (ready (fuel + 1) (source + 1)) word t) :
    word.length ≤ 2 := by
  exact completed_block_bound nonstall_contract block (by simp [fundedLive, ready])

/-- The actual source-depleted endpoint cannot finance a further issued block. -/
theorem completion_does_not_restore_admission :
    BlockPath (protocol false) () (ready 1 1) [.pay, .tick] (ready 1 0) ∧
      ¬ fundedLive () (ready 1 0) := by
  exact ⟨paid_block false () 0 0, by simp [fundedLive, ready]⟩

/-- Entry refusal cannot satisfy the required initial enabled-next-event premise. -/
theorem refused_entry_excludes_contract
    (Live : Unit → Inventory → Prop) (rank : Inventory → Nat)
    (entry : Live () (ready 0 1)) :
    ¬ CompletionContract (protocol false) Live rank := by
  intro law
  obtain ⟨e, t, step⟩ := law.next () (ready 0 1) entry
  cases step.1

/-- A real paid deadlock is not an implemented failure report or a free reset. -/
theorem paid_deadlock_excludes_contract
    (Live : Unit → Inventory → Prop) (rank : Inventory → Nat)
    (unfinished : Live () (busy 0 0)) :
    ¬ CompletionContract (protocol false) Live rank := by
  intro law
  obtain ⟨e, t, step⟩ := law.next () (busy 0 0) unfinished
  exact nonstall_exhausted_deadlock e ⟨t, step.1⟩

/-- The admitted busy self-loop defeats every strict internal rank. -/
theorem stalling_excludes_contract
    (Live : Unit → Inventory → Prop) (rank : Inventory → Nat)
    (unfinished : Live () (busy 0 1)) :
    ¬ CompletionContract (protocol true) Live rank := by
  intro law
  have lower := law.descend () (busy 0 1) .tick (busy 0 1) unfinished
    ⟨PaidStep.spin 0 1 rfl, trivial⟩ (by simp [protocol, busy])
  exact Nat.lt_irrefl _ lower

/-- Completion and existing resource accounting concern the same paid history. -/
theorem funded_completion_keeps_accounts :
    BlockPath (protocol false) () (ready 1 2) [.pay, .tick] (ready 1 1) ∧
      Conditional.SupportTrace (world false) demand credit
        (ready 1 2) [.pay, .tick] (ready 1 1) 1 1 1 ∧
      Conditional.SupportTrace (world false) demand credit
        (ready 1 1) [.pay, .tick] (ready 1 0) 1 1 1 ∧
      ¬ fundedLive () (ready 1 0) := by
  exact ⟨paid_block false () 0 1, paid_cycle_account false 0 1,
    paid_cycle_account false 0 0, by simp [fundedLive, ready]⟩

end Generative.Learning.Protocols.Completion.Examples

#print axioms Generative.Learning.Protocols.Completion.Examples.nonstall_contract
#print axioms Generative.Learning.Protocols.Completion.Examples.funded_completion
#print axioms Generative.Learning.Protocols.Completion.Examples.all_funded_blocks_bounded
#print axioms Generative.Learning.Protocols.Completion.Examples.completion_does_not_restore_admission
#print axioms Generative.Learning.Protocols.Completion.Examples.refused_entry_excludes_contract
#print axioms Generative.Learning.Protocols.Completion.Examples.paid_deadlock_excludes_contract
#print axioms Generative.Learning.Protocols.Completion.Examples.stalling_excludes_contract
#print axioms Generative.Learning.Protocols.Completion.Examples.funded_completion_keeps_accounts
