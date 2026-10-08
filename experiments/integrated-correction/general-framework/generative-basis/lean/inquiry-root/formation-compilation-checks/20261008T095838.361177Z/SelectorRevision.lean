import Std
import GenerativeCore

/-!
Costed selector replacement within one continuing compartment. The supplied
event law distinguishes a hidden plant regime from the selector's material
state. Analytical probabilities and Python refinement are outside this file.
-/

namespace SelectorRevision

structure Parameters where
  assembly : Nat
  trial : Nat
  renewal : Nat
  packet : Nat
  lifetime : Nat
deriving DecidableEq, Repr

def Admissible (p : Parameters) : Prop :=
  0 < p.assembly ∧ 0 < p.trial ∧ 0 < p.renewal ∧
  p.renewal ≤ p.packet ∧ 0 < p.lifetime

structure State where
  fuel : Nat
  packets : Nat
  selector : Bool
  lease : Nat
  regime : Bool
deriving DecidableEq, Repr

inductive Event where
  | assemble (selector : Bool)
  | trial (signal : Bool)
  | reverse
  | expire
deriving DecidableEq, Repr

def response (s : State) (signal : Bool) : Bool := signal.xor s.selector
def productiveResponse (s : State) (signal : Bool) : Bool := signal.xor s.regime

def Enabled (p : Parameters) (s : State) : Event → Prop
  | .assemble _ => s.lease = 0 ∧ p.assembly ≤ s.fuel
  | .trial _ => 0 < s.lease ∧ p.trial ≤ s.fuel ∧ 0 < s.packets
  | .reverse => True
  | .expire => 0 < s.packets

def advance (p : Parameters) (s : State) : Event → State
  | .assemble m => { s with fuel := s.fuel - p.assembly,
                            selector := m, lease := p.lifetime }
  | .trial _ =>
    if s.selector = s.regime then
      { s with fuel := s.fuel - p.trial + p.packet - p.renewal,
               packets := s.packets - 1, lease := p.lifetime }
    else
      { s with fuel := s.fuel - p.trial,
               packets := s.packets - 1, lease := s.lease - 1 }
  | .reverse => { s with regime := !s.regime }
  | .expire => { s with packets := s.packets - 1 }

def expenditure (p : Parameters) (s : State) : Event → Nat
  | .assemble _ => p.assembly
  | .trial _ => p.trial + if s.selector = s.regime then p.renewal else 0
  | .reverse | .expire => 0

def waste (p : Parameters) (s : State) : Event → Nat
  | .trial _ => if s.selector = s.regime then 0 else p.packet
  | .expire => p.packet
  | _ => 0

def energy (p : Parameters) (s : State) : Nat := s.fuel + s.packets * p.packet

def Step (p : Parameters) (s : State) (a : Event) (t : State) : Prop :=
  Enabled p s a ∧ t = advance p s a

instance (p : Parameters) (s : State) (a : Event) : Decidable (Enabled p s a) := by
  cases a <;> unfold Enabled <;> infer_instance

instance (p : Parameters) (s : State) (a : Event) (t : State) :
    Decidable (Step p s a t) := by
  unfold Step
  infer_instance

def process (p : Parameters) : Generative.Process State Event := ⟨Step p⟩

def Trace (p : Parameters) := Generative.Trace (process p)

def spentAlong (p : Parameters) (s : State) : List Event → Nat
  | [] => 0
  | a :: as => expenditure p s a + waste p s a + spentAlong p (advance p s a) as

theorem response_matches_iff (s : State) (b : Bool) :
    response s b = productiveResponse s b ↔ s.selector = s.regime := by
  cases b <;> cases hs : s.selector <;> cases hz : s.regime <;>
    simp [response, productiveResponse, hs, hz]

/-- Changing the hidden regime changes consequences, not command eligibility. -/
theorem commands_do_not_read_regime (p : Parameters) (s : State) (z : Bool) (a : Event) :
    Enabled p { s with regime := z } a ↔ Enabled p s a := by
  cases a <;> rfl

theorem step_energy_ledger {p : Parameters} {s t : State} {a : Event}
    (hp : Admissible p) (h : Step p s a t) :
    energy p t + expenditure p s a + waste p s a = energy p s := by
  rcases h with ⟨he, rfl⟩
  have hr := hp.2.2.2.1
  have packetEq (hs : 0 < s.packets) :
      (s.packets - 1) * p.packet + p.packet = s.packets * p.packet := by
    rw [← Nat.succ_mul]
    congr 1
    omega
  cases a with
  | assemble m =>
    simp only [Enabled] at he
    simp only [advance, energy, expenditure, waste]
    omega
  | trial b =>
    simp only [Enabled] at he
    have hh := packetEq he.2.2
    by_cases hm : s.selector = s.regime <;>
      simp [advance, energy, expenditure, waste, hm] <;> omega
  | reverse => simp [advance, energy, expenditure, waste]
  | expire =>
    have hh := packetEq he
    simp only [advance, energy, expenditure, waste]
    omega

theorem trace_energy_ledger {p : Parameters} {s t : State} {as : List Event}
    (hp : Admissible p) (h : Trace p s as t) :
    energy p t + spentAlong p s as = energy p s := by
  induction h with
  | nil => simp [spentAlong]
  | @cons s u t a as hs ht ih =>
    have hh := step_energy_ledger hp hs
    have hu : u = advance p s a := hs.2
    subst u
    simp only [spentAlong]
    omega

theorem trial_preserves_selector (p : Parameters) (s : State) (b : Bool) :
    (advance p s (.trial b)).selector = s.selector := by
  by_cases hm : s.selector = s.regime <;> simp [advance, hm]

theorem renewal_inherits_selector (p : Parameters) (s : State) (b : Bool)
    (hm : s.selector = s.regime) :
    (advance p s (.trial b)).selector = s.selector ∧
    (advance p s (.trial b)).lease = p.lifetime := by
  simp [advance, hm]

theorem failed_trial_wears_selector (p : Parameters) (s : State) (b : Bool)
    (hm : s.selector ≠ s.regime) :
    (advance p s (.trial b)).lease = s.lease - 1 := by
  simp [advance, hm]

theorem changed_selector_requires_paid_assembly {p : Parameters} {s t : State} {a : Event}
    (h : Step p s a t) (hc : t.selector ≠ s.selector) :
    ∃ m, a = .assemble m ∧ s.lease = 0 ∧ p.assembly ≤ s.fuel ∧
      t.fuel + p.assembly = s.fuel := by
  rcases h with ⟨he, rfl⟩
  cases a with
  | assemble m =>
    have hf : p.assembly ≤ s.fuel := he.2
    refine ⟨m, rfl, he.1, he.2, ?_⟩
    simp only [advance]
    omega
  | trial b => exact False.elim (hc (trial_preserves_selector p s b))
  | reverse => exact False.elim (hc rfl)
  | expire => exact False.elim (hc rfl)

theorem reversal_preserves_actual_resources_and_selector (p : Parameters) (s : State) :
    (advance p s .reverse).fuel = s.fuel ∧
    (advance p s .reverse).packets = s.packets ∧
    (advance p s .reverse).selector = s.selector ∧
    (advance p s .reverse).lease = s.lease := by
  exact ⟨rfl, rfl, rfl, rfl⟩

theorem trace_composition_uses_actual_state {p : Parameters} {s t : State}
    {xs ys : List Event} :
    Trace p s (xs ++ ys) t ↔ ∃ u, Trace p s xs u ∧ Trace p u ys t :=
  Generative.trace_append_iff

def exampleParameters : Parameters := ⟨1, 2, 1, 4, 2⟩
def exampleInitial : State := ⟨7, 4, false, 0, false⟩
def exampleFinal : State := ⟨3, 0, true, 2, true⟩
def exampleEvents : List Event :=
  [.assemble false, .trial false, .reverse, .trial false, .trial true,
   .assemble true, .trial true]

/-- Paid formation, successful use, reversal, wear and different reconstruction
all occur on the same actual state history, with no budget reset. -/
theorem revised_selector_witness :
    Trace exampleParameters exampleInitial exampleEvents exampleFinal := by
  apply Generative.Trace.cons (m := ⟨6, 4, false, 2, false⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨7, 3, false, 2, false⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨7, 3, false, 2, true⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨5, 2, false, 1, true⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨3, 1, false, 0, true⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := ⟨2, 1, true, 2, true⟩) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := exampleFinal) (by change Step _ _ _ _; decide)
  exact .nil _

theorem witness_changes_response_mapping :
    response exampleInitial false ≠ response exampleFinal false := by decide

/- The following exact resource theorem concerns the pre-return payment
prefix. It is connected to the selector law by the explicitly stated event
decomposition in the mathematical note; no probability theorem is asserted. -/

inductive Paid : Nat → List Nat → Nat → Prop where
  | nil (f : Nat) : Paid f [] f
  | cons {f g : Nat} {c : Nat} {cs : List Nat} :
      c ≤ f → Paid (f - c) cs g → Paid f (c :: cs) g

theorem paid_ledger {f g : Nat} {cs : List Nat} (h : Paid f cs g) :
    g + cs.sum = f := by
  induction h with
  | nil => simp
  | cons hc _ ih => simp only [List.sum_cons]; omega

theorem paid_exists_iff (f : Nat) (cs : List Nat) :
    (∃ g, Paid f cs g) ↔ cs.sum ≤ f := by
  constructor
  · rintro ⟨g, h⟩
    have hh := paid_ledger h
    omega
  · intro h
    induction cs generalizing f with
    | nil => exact ⟨f, .nil f⟩
    | cons c cs ih =>
      simp only [List.sum_cons] at h
      have hc : c ≤ f := by omega
      obtain ⟨g, hg⟩ := ih (f-c) (by omega)
      exact ⟨g, .cons hc hg⟩

def failureCosts (c d L : Nat) : Nat → List Nat
  | 0 => []
  | j+1 => (c :: List.replicate L d) ++ failureCosts c d L j

def recoveryCosts (c d L k j : Nat) : List Nat :=
  List.replicate k d ++ failureCosts c d L j ++ [c,d]

def recoveryCost (c d L k j : Nat) : Nat := k*d + c + d + j*(c+L*d)
def recoveryTrials (L k j : Nat) : Nat := k + 1 + j*L

theorem failure_cost_sum (c d L j : Nat) :
    (failureCosts c d L j).sum = j*(c+L*d) := by
  induction j with
  | zero => simp [failureCosts]
  | succ j ih => simp [failureCosts, ih, Nat.succ_mul]; omega

theorem recovery_cost_sum (c d L k j : Nat) :
    (recoveryCosts c d L k j).sum = recoveryCost c d L k j := by
  simp [recoveryCosts, failure_cost_sum, recoveryCost]
  omega

/-- Exact threshold, including every unsuccessful assembly and trial. -/
theorem recovery_prefix_affordable_iff (c d L k j f : Nat) :
    (∃ g, Paid f (recoveryCosts c d L k j) g) ↔ recoveryCost c d L k j ≤ f := by
  rw [paid_exists_iff, recovery_cost_sum]

theorem no_recovery_below_first_cost (c d L k j f : Nat)
    (h : f < k*d+c+d) :
    ¬ ∃ g, Paid f (recoveryCosts c d L k j) g := by
  rw [recovery_prefix_affordable_iff]
  unfold recoveryCost
  omega

theorem each_failed_candidate_adds_full_block (c d L k j : Nat) :
    recoveryCost c d L k (j+1) = recoveryCost c d L k j + c + L*d := by
  simp [recoveryCost, Nat.succ_mul]
  omega

theorem each_failed_candidate_adds_lifetime_trials (L k j : Nat) :
    recoveryTrials L k (j+1) = recoveryTrials L k j + L := by
  simp [recoveryTrials, Nat.succ_mul]
  omega

/-- No observation or environment oracle can overcome an unpaid first trial. -/
theorem source_horizon_obstruction (L k j H : Nat) (h : H < k+1) :
    ¬ recoveryTrials L k j ≤ H := by
  unfold recoveryTrials
  omega

end SelectorRevision

#print axioms SelectorRevision.response_matches_iff
#print axioms SelectorRevision.commands_do_not_read_regime
#print axioms SelectorRevision.step_energy_ledger
#print axioms SelectorRevision.trace_energy_ledger
#print axioms SelectorRevision.trial_preserves_selector
#print axioms SelectorRevision.renewal_inherits_selector
#print axioms SelectorRevision.failed_trial_wears_selector
#print axioms SelectorRevision.changed_selector_requires_paid_assembly
#print axioms SelectorRevision.reversal_preserves_actual_resources_and_selector
#print axioms SelectorRevision.trace_composition_uses_actual_state
#print axioms SelectorRevision.revised_selector_witness
#print axioms SelectorRevision.witness_changes_response_mapping
#print axioms SelectorRevision.paid_ledger
#print axioms SelectorRevision.paid_exists_iff
#print axioms SelectorRevision.failure_cost_sum
#print axioms SelectorRevision.recovery_cost_sum
#print axioms SelectorRevision.recovery_prefix_affordable_iff
#print axioms SelectorRevision.no_recovery_below_first_cost
#print axioms SelectorRevision.each_failed_candidate_adds_full_block
#print axioms SelectorRevision.each_failed_candidate_adds_lifetime_trials
#print axioms SelectorRevision.source_horizon_obstruction
