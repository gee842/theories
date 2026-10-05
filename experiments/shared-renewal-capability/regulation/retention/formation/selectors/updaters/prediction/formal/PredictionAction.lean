import Std
import GenerativeCore
import FormedSelection
import SelectorRevision
import UpdaterFormation

/- A paid predictive retrofit of actual formed machinery. This relation checks
the payable-write, deterministic-capture subprocess. Circuit rebuild, skipped
writes and stochastic outage comparisons have separate executable semantics. -/
namespace PredictionAction

structure Parameters where
  base : UpdaterFormation.Parameters
  retrofit : Nat
  rent : Nat
  writing : Nat
deriving DecidableEq, Repr

inductive Phase where
  | ready | rented | observed | written
deriving DecidableEq, Repr

structure State where
  physical : UpdaterFormation.State
  score : Nat
  receipt : Bool
  phase : Phase
deriving DecidableEq, Repr

inductive Event where
  | formUpdater (fast : Bool)
  | rent | work | write | finish | reverse
deriving DecidableEq, Repr

def command (s : State) : Bool :=
  if s.score < 2 then false else if 2 < s.score then true else s.physical.core.selector

def receiptOf (action regime available : Bool) : Bool := (action == regime) && available
def decode (action receipt : Bool) : Bool := if receipt then action else !action
def label (s : State) : Bool := decode s.physical.core.selector s.receipt

def revisedScore (fast : Bool) (score : Nat) (target : Bool) : Nat :=
  if fast then (if target then 4 else 0)
  else if target then min 4 (score+1) else score-1

def forecastNumerator (s : State) : Nat := if command s then s.score else 4-s.score
def capture (s : State) : Bool := receiptOf (command s) s.physical.core.regime true
def maintenance (p : Parameters) : Nat := p.base.selector.renewal+p.base.moduleRenewal

def Enabled (p : Parameters) (s : State) : Event → Prop
  | .formUpdater u => s.phase = .ready ∧ UpdaterFormation.Enabled p.base s.physical (.formModule u)
  | .rent => s.phase = .ready ∧ 0 < s.physical.core.lease ∧ 0 < s.physical.moduleLease ∧ p.rent ≤ s.physical.core.fuel
  | .work => s.phase = .rented ∧ 0 < s.physical.core.lease ∧ 0 < s.physical.moduleLease ∧ p.base.selector.trial ≤ s.physical.core.fuel ∧ 0 < s.physical.core.packets
  | .write => s.phase = .observed ∧ p.writing ≤ s.physical.core.fuel
  | .finish => s.phase = .written ∧ 0 < s.physical.core.lease ∧ 0 < s.physical.moduleLease
  | .reverse => s.phase = .ready

def advance (p : Parameters) (s : State) : Event → State
  | .formUpdater u => { s with physical := UpdaterFormation.advance p.base s.physical (.formModule u) }
  | .rent => { s with phase := .rented, physical := { s.physical with core := { s.physical.core with fuel := s.physical.core.fuel-p.rent } } }
  | .work => { s with phase := .observed, receipt := capture s, physical := { s.physical with core := { s.physical.core with selector := command s, packets := s.physical.core.packets-1, fuel := if capture s then s.physical.core.fuel-p.base.selector.trial+p.base.selector.packet-maintenance p else s.physical.core.fuel-p.base.selector.trial } } }
  | .write => { s with phase := .written, score := revisedScore s.physical.directed s.score (label s), physical := { s.physical with core := { s.physical.core with fuel := s.physical.core.fuel-p.writing } } }
  | .finish => { s with phase := .ready, receipt := false, physical := { s.physical with moduleLease := if s.receipt then p.base.moduleLifetime else s.physical.moduleLease-1, core := { s.physical.core with lease := if s.receipt then p.base.selector.lifetime else s.physical.core.lease-1 } } }
  | .reverse => { s with physical := UpdaterFormation.advance p.base s.physical .reverse }

def Step (p : Parameters) (s : State) (a : Event) (t : State) : Prop :=
  Enabled p s a ∧ t = advance p s a

instance (p : Parameters) (s : State) (a : Event) : Decidable (Enabled p s a) := by
  cases a <;> unfold Enabled <;> infer_instance
instance (p : Parameters) (s : State) (a : Event) (t : State) : Decidable (Step p s a t) := by
  unfold Step; infer_instance

def process (p : Parameters) : Generative.Process State Event := ⟨Step p⟩
def Trace (p : Parameters) := Generative.Trace (process p)
def energy (p : Parameters) (s : State) : Nat := UpdaterFormation.energy p.base s.physical

def expenditure (p : Parameters) (s : State) : Event → Nat
  | .formUpdater _ => p.base.moduleAssembly
  | .rent => p.rent
  | .work => p.base.selector.trial + if capture s then maintenance p else 0
  | .write => p.writing
  | .finish | .reverse => 0

def waste (p : Parameters) (s : State) : Event → Nat
  | .work => if capture s then 0 else p.base.selector.packet
  | _ => 0

def spentAlong (p : Parameters) (s : State) : List Event → Nat
  | [] => 0
  | a :: as => expenditure p s a + waste p s a + spentAlong p (advance p s a) as

theorem noiseless_receipt_decodes_target (action regime : Bool) :
    decode action (receiptOf action regime true) = regime := by
  cases action <;> cases regime <;> decide

theorem outage_record_is_ambiguous :
    receiptOf false true true = receiptOf false false false ∧
    receiptOf true true true ≠ receiptOf true false false := by decide

theorem changing_memory_changes_command (s : State) :
    command { s with score := 0 } = false ∧ command { s with score := 4 } = true := by
  simp [command]

theorem command_does_not_read_hidden_regime (s : State) (z : Bool) :
    command { s with physical := { s.physical with core := { s.physical.core with regime := z } } } = command s := by
  rfl

theorem revised_score_bounded (fast target : Bool) (q : Nat) (hq : q ≤ 4) :
    revisedScore fast q target ≤ 4 := by
  cases fast <;> cases target <;> simp [revisedScore] <;> omega

theorem step_score_bounded {p : Parameters} {s t : State} {a : Event}
    (h : Step p s a t) (hq : s.score ≤ 4) : t.score ≤ 4 := by
  rcases h with ⟨_, rfl⟩
  cases a <;> try exact hq
  exact revised_score_bounded _ _ _ hq

theorem trace_score_bounded {p : Parameters} {s t : State} {as : List Event}
    (h : Trace p s as t) (hq : s.score ≤ 4) : t.score ≤ 4 := by
  induction h with
  | nil => exact hq
  | cons hs _ ih => exact ih (step_score_bounded hs hq)

theorem updater_reformation_retains_memory (p : Parameters) (s : State) (u : Bool) :
    (advance p s (.formUpdater u)).score = s.score := rfl

theorem reversal_retains_memory_and_resources (p : Parameters) (s : State) :
    (advance p s .reverse).score = s.score ∧
    (advance p s .reverse).physical.core.fuel = s.physical.core.fuel ∧
    (advance p s .reverse).physical.core.packets = s.physical.core.packets ∧
    (advance p s .reverse).physical.core.selector = s.physical.core.selector := by
  exact ⟨rfl,rfl,rfl,rfl⟩

theorem step_energy_ledger {p : Parameters} {s t : State} {a : Event}
    (hp : UpdaterFormation.Admissible p.base) (h : Step p s a t) :
    energy p t + expenditure p s a + waste p s a = energy p s := by
  rcases h with ⟨he, rfl⟩
  have hr : maintenance p ≤ p.base.selector.packet := hp.1.2.2.2.1
  cases a with
  | formUpdater u =>
    have hf : p.base.moduleAssembly ≤ s.physical.core.fuel := he.2.2
    simp only [energy, UpdaterFormation.energy, SelectorRevision.energy,
      advance, UpdaterFormation.advance, expenditure, waste]
    omega
  | rent =>
    have hf := he.2.2.2
    simp only [energy, UpdaterFormation.energy, SelectorRevision.energy, advance, expenditure, waste]
    omega
  | work =>
    have hf := he.2.2.2.1
    have hs := he.2.2.2.2
    have hpack : (s.physical.core.packets-1)*p.base.selector.packet+p.base.selector.packet = s.physical.core.packets*p.base.selector.packet := by
      rw [← Nat.succ_mul]; congr 1; omega
    cases hc : capture s <;>
      simp [energy, UpdaterFormation.energy, SelectorRevision.energy,
        UpdaterFormation.effective, advance, expenditure, waste, hc] <;> omega
  | write =>
    have hf := he.2
    simp only [energy, UpdaterFormation.energy, SelectorRevision.energy, advance, expenditure, waste]
    omega
  | finish => simp [energy, UpdaterFormation.energy, SelectorRevision.energy, advance, expenditure, waste]
  | reverse => simp [energy, UpdaterFormation.energy, SelectorRevision.energy, advance, UpdaterFormation.advance, SelectorRevision.advance, expenditure, waste]

theorem trace_energy_ledger {p : Parameters} {s t : State} {as : List Event}
    (hp : UpdaterFormation.Admissible p.base) (h : Trace p s as t) :
    energy p t + spentAlong p s as = energy p s := by
  induction h with
  | nil => simp [spentAlong]
  | @cons s u t a as hs ht ih =>
    have hh := step_energy_ledger hp hs
    have hu : u = advance p s a := hs.2
    subst u
    simp only [spentAlong]
    omega

def RetrofitEnabled (p : Parameters) (s : UpdaterFormation.State) : Prop :=
  2 ≤ s.material ∧ 0 < s.moduleLease ∧ 0 < s.core.lease ∧ s.selectorSeen = true ∧ p.retrofit ≤ s.core.fuel

def retrofit (p : Parameters) (s : UpdaterFormation.State) : State :=
  { physical := { s with core := { s.core with fuel := s.core.fuel-p.retrofit } },
    score := 2, receipt := false, phase := .ready }

theorem retrofit_preserves_actual_memory_reference (p : Parameters) (s : UpdaterFormation.State) :
    (retrofit p s).physical.core.selector = s.core.selector ∧
    (retrofit p s).physical.core.packets = s.core.packets ∧
    (retrofit p s).physical.material = s.material ∧
    (retrofit p s).score = 2 := by exact ⟨rfl,rfl,rfl,rfl⟩

theorem paid_retrofit_energy {p : Parameters} {s : UpdaterFormation.State}
    (h : RetrofitEnabled p s) : energy p (retrofit p s)+p.retrofit = UpdaterFormation.energy p.base s := by
  have hf := h.2.2.2.2
  simp only [energy, retrofit, UpdaterFormation.energy, SelectorRevision.energy]
  omega

def cycleEvents : List Event := [.rent,.work,.write,.finish]
def cycleEnd (p : Parameters) (s : State) : State :=
  advance p (advance p (advance p (advance p s .rent) .work) .write) .finish

def CycleEnabled (p : Parameters) (s : State) : Prop :=
  Enabled p s .rent ∧ Enabled p (advance p s .rent) .work ∧
  Enabled p (advance p (advance p s .rent) .work) .write ∧
  Enabled p (advance p (advance p (advance p s .rent) .work) .write) .finish

instance (p : Parameters) (s : State) : Decidable (CycleEnabled p s) := by
  unfold CycleEnabled; infer_instance

theorem paid_cycle (p : Parameters) (s : State) (h : CycleEnabled p s) :
    Trace p s cycleEvents (cycleEnd p s) :=
  .cons ⟨h.1,rfl⟩ (.cons ⟨h.2.1,rfl⟩ (.cons ⟨h.2.2.1,rfl⟩ (.cons ⟨h.2.2.2,rfl⟩ (.nil _))))

theorem cycle_then {p : Parameters} {s u t : State} {rest : List Event}
    (h : CycleEnabled p s) (he : cycleEnd p s = u) (ht : Trace p u rest t) :
    Trace p s (cycleEvents ++ rest) t := by
  apply Generative.trace_append_iff.mpr
  refine ⟨u, ?_, ht⟩
  rw [← he]
  exact paid_cycle p s h

def correctiveCosts (rent work writing gate : Nat) : List Nat :=
  [rent,work,writing,rent,work,writing,gate,rent,work,writing,rent,work]

theorem three_evidence_then_action_affordable_iff (rent work writing gate F : Nat) :
    (∃ x, SelectorRevision.Paid F (correctiveCosts rent work writing gate) x) ↔
    3*(rent+work+writing)+gate+rent+work ≤ F := by
  rw [SelectorRevision.paid_exists_iff]
  simp only [correctiveCosts, List.sum_cons, List.sum_nil]
  omega

theorem slow_needs_three_false_writes_from_four :
    revisedScore false 4 false = 3 ∧ revisedScore false 3 false = 2 ∧
    revisedScore false 2 false = 1 := by decide

theorem fast_one_false_write_from_four : revisedScore true 4 false = 0 := by decide

end PredictionAction

#print axioms PredictionAction.noiseless_receipt_decodes_target
#print axioms PredictionAction.outage_record_is_ambiguous
#print axioms PredictionAction.changing_memory_changes_command
#print axioms PredictionAction.command_does_not_read_hidden_regime
#print axioms PredictionAction.revised_score_bounded
#print axioms PredictionAction.step_score_bounded
#print axioms PredictionAction.trace_score_bounded
#print axioms PredictionAction.updater_reformation_retains_memory
#print axioms PredictionAction.reversal_retains_memory_and_resources
#print axioms PredictionAction.step_energy_ledger
#print axioms PredictionAction.trace_energy_ledger
#print axioms PredictionAction.retrofit_preserves_actual_memory_reference
#print axioms PredictionAction.paid_retrofit_energy
#print axioms PredictionAction.paid_cycle
#print axioms PredictionAction.cycle_then
#print axioms PredictionAction.three_evidence_then_action_affordable_iff
#print axioms PredictionAction.slow_needs_three_false_writes_from_four
#print axioms PredictionAction.fast_one_false_write_from_four
