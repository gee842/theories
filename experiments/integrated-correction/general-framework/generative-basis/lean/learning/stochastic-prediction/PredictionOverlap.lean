import Exposure
import PredictionAction

set_option linter.unusedSimpArgs false
set_option maxHeartbeats 2000000

namespace StochasticPrediction

def oldParameters (p : PredictionAction.Parameters) : Parameters :=
  {gateAssembly := p.base.moduleAssembly, base := 1, retrofit := p.retrofit,
   rent := p.rent, trial := p.base.selector.trial, writing := p.writing,
   renewal := p.base.selector.renewal, gateRenewal := p.base.moduleRenewal,
   packet := p.base.selector.packet, lifetime := p.base.selector.lifetime,
   gateLifetime := p.base.moduleLifetime}

def oldState (s : PredictionAction.State) (written : Bool) : State :=
  {fuel := s.physical.core.fuel, gate := if s.physical.directed then 1 else 0,
   gateLife := s.physical.moduleLease, stage := 2, life := s.physical.core.lease,
   q := s.score, last := s.physical.core.selector, written := written}

theorem old_command_agrees (s : PredictionAction.State) (written : Bool) :
    command (oldState s written) = PredictionAction.command s := by
  unfold command oldState PredictionAction.command
  dsimp only
  split <;> split <;> simp_all <;> omega

theorem old_update_agrees (fast target : Bool) (q : Nat) :
    updated fast q target = PredictionAction.revisedScore fast q target := rfl

theorem installed_preparation_identity (p : Parameters) (a : Arm) (b : Seed) (s : State)
    (hg : 0 < s.gateLife) (hl : 0 < s.life) (hs : s.stage = 2) :
    prepared p a b s = s ∧ preparationCost p a b s = 0 := by
  have hgn : s.gateLife ≠ 0 := by omega
  have hln : s.life ≠ 0 := by omega
  simp [prepared, preparationCost, formGate, gateCost, formBase, baseCost,
    retrofit, retrofitCost, hgn, hln, hs]

/-- The old payable cycle is exactly the deterministic-availability operational
exposure on its installed hardware domain. The old stage guards remain real
hypotheses; non-work and unpaid-write exposures are not covered. -/
theorem payable_cycle_overlap (p : PredictionAction.Parameters) (s : PredictionAction.State)
    (written : Bool) (b : Seed) (hb : b.available = true)
    (h : PredictionAction.CycleEnabled p s)
    (hm : PredictionAction.maintenance p ≤ p.base.selector.packet) :
    (exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)).state =
      oldState (PredictionAction.cycleEnd p s) true := by
  rcases h with ⟨hr,hw,hwrite,hfinish⟩
  have hg : 0 < (oldState s written).gateLife := hr.2.2.1
  have hl : 0 < (oldState s written).life := hr.2.1
  have hp := installed_preparation_identity (oldParameters p) .variable b (oldState s written) hg hl rfl
  have hf : p.rent ≤ s.physical.core.fuel := hr.2.2.2
  have ht : p.base.selector.trial ≤ s.physical.core.fuel-p.rent := hw.2.2.2.1
  have hgate : s.physical.moduleLease ≠ 0 := Nat.ne_of_gt hr.2.2.1
  have hlife : s.physical.core.lease ≠ 0 := Nat.ne_of_gt hr.2.1
  have hpay : p.writing ≤
      s.physical.core.fuel-p.rent-p.base.selector.trial+
      (if PredictionAction.capture s then p.base.selector.packet-PredictionAction.maintenance p else 0) := by
    have hh := hwrite.2
    change p.writing ≤ (if PredictionAction.capture s then
      s.physical.core.fuel-p.rent-p.base.selector.trial+p.base.selector.packet-PredictionAction.maintenance p
      else s.physical.core.fuel-p.rent-p.base.selector.trial) at hh
    cases hc : PredictionAction.capture s <;> simp_all [Nat.add_sub_assoc hm]
  have hnf := Nat.not_lt.mpr hf
  have hnt := Nat.not_lt.mpr ht
  have hcash : s.physical.core.fuel-p.rent-p.base.selector.trial+p.base.selector.packet-
      (p.base.selector.renewal+p.base.moduleRenewal) =
      s.physical.core.fuel-p.rent-p.base.selector.trial+
      (p.base.selector.packet-(p.base.selector.renewal+p.base.moduleRenewal)) := by
    change p.base.selector.renewal+p.base.moduleRenewal ≤ p.base.selector.packet at hm
    omega
  simp only [exposure, hp.1]
  have hq : s.score < 2 ∨ s.score = 2 ∨ 2 < s.score := by omega
  obtain hq | hq | hq := hq
  all_goals (try have heq : s.score ≠ 2 := by omega)
  all_goals (try have hlow : ¬ s.score < 2 := by omega)
  all_goals (try have hhigh : ¬ 2 < s.score := by omega)
  all_goals (try have hle : s.score ≤ 2 := by omega)
  all_goals (try have hge : 2 ≤ s.score := by omega)
  all_goals
    cases hd : s.physical.directed <;> cases hz : s.physical.core.regime <;>
      cases hs : s.physical.core.selector <;>
      simp_all [operate, trial, issued, oldState, oldParameters, command,
        PredictionAction.cycleEnd, PredictionAction.advance, PredictionAction.capture,
        PredictionAction.command, PredictionAction.label, PredictionAction.decode,
        PredictionAction.receiptOf, PredictionAction.revisedScore, updated,
        maintenance, PredictionAction.maintenance, hcash]

  all_goals (split <;> try omega)
  all_goals (split <;> try omega)
  all_goals dsimp only
  all_goals congr 1
  all_goals try rfl
  all_goals simp (disch := omega) [*]
  all_goals (try intro hn)
  all_goals first | omega | (split <;> omega)

/-- Trial receipts and scheduled loss agree on the same payable domain. A
false receipt here is an actual attempted mismatch, not a no-work label. -/
theorem payable_receipt_overlap (p : PredictionAction.Parameters) (s : PredictionAction.State)
    (written : Bool) (b : Seed) (hb : b.available = true)
    (h : PredictionAction.CycleEnabled p s) :
    let r := exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)
    r.worked = true ∧ r.captured = PredictionAction.capture s ∧
      r.waste = PredictionAction.waste p s .work := by
  have hg : 0 < (oldState s written).gateLife := h.1.2.2.1
  have hl : 0 < (oldState s written).life := h.1.2.1
  have hp := installed_preparation_identity (oldParameters p) .variable b (oldState s written) hg hl rfl
  have hgate : s.physical.moduleLease ≠ 0 := Nat.ne_of_gt h.1.2.2.1
  have hlife : s.physical.core.lease ≠ 0 := Nat.ne_of_gt h.1.2.1
  have hf : ¬s.physical.core.fuel < p.rent := Nat.not_lt.mpr h.1.2.2.2
  have ht : ¬s.physical.core.fuel-p.rent < p.base.selector.trial := Nat.not_lt.mpr h.2.1.2.2.2.1
  have hc := old_command_agrees s written
  have hc' : command { (oldState s written) with fuel := s.physical.core.fuel-p.rent } =
      PredictionAction.command s := hc
  simp only [exposure, hp.1]
  simp [operate, oldState, oldParameters, hlife, hgate, hf, ht, trial, issued, hb,
    PredictionAction.waste, PredictionAction.capture, PredictionAction.receiptOf,
    ← hc, command]

theorem payable_cycle_packet_debit (p : PredictionAction.Parameters) (s : PredictionAction.State)
    (h : PredictionAction.CycleEnabled p s) :
    (PredictionAction.cycleEnd p s).physical.core.packets+1 = s.physical.core.packets := by
  have hn : 0 < s.physical.core.packets := h.2.1.2.2.2.2
  change s.physical.core.packets-1+1 = s.physical.core.packets
  omega

theorem old_cycle_marked_account (p : PredictionAction.Parameters) (s : PredictionAction.State) :
    PredictionAction.spentAlong p s PredictionAction.cycleEvents =
      p.rent+PredictionAction.expenditure p s .work+p.writing+
      PredictionAction.waste p s .work := by
  change p.rent+0+(p.base.selector.trial+
    (if PredictionAction.capture s then PredictionAction.maintenance p else 0)+
    (if PredictionAction.capture s then 0 else p.base.selector.packet)+
    (p.writing+0+(0+0+0))) =
    p.rent+(p.base.selector.trial+
    (if PredictionAction.capture s then PredictionAction.maintenance p else 0))+p.writing+
    (if PredictionAction.capture s then 0 else p.base.selector.packet)
  omega

theorem payable_total_account_overlap (p : PredictionAction.Parameters) (s : PredictionAction.State)
    (written : Bool) (b : Seed) (hb : b.available = true)
    (h : PredictionAction.CycleEnabled p s) (hp : UpdaterFormation.Admissible p.base) :
    let r := exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)
    r.spent+r.waste = PredictionAction.spentAlong p s PredictionAction.cycleEvents := by
  have hm : PredictionAction.maintenance p ≤ p.base.selector.packet := hp.1.2.2.2.1
  have he := exposure_account (oldParameters p) .variable s.physical.core.regime b (oldState s written) hm
  have ht := payable_cycle_overlap p s written b hb h hm
  have old := PredictionAction.trace_energy_ledger hp (PredictionAction.paid_cycle p s h)
  have hn := payable_cycle_packet_debit p s h
  have hpack : (PredictionAction.cycleEnd p s).physical.core.packets*p.base.selector.packet+
      p.base.selector.packet = s.physical.core.packets*p.base.selector.packet := by
    simpa only [Nat.add_mul, Nat.one_mul] using congrArg (fun k => k*p.base.selector.packet) hn
  have rem : (PredictionAction.cycleEnd p s).physical.remainder = s.physical.remainder := rfl
  have hstate := congrArg State.fuel ht
  change (exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)).state.fuel =
    (PredictionAction.cycleEnd p s).physical.core.fuel at hstate
  change (exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)).state.fuel +
    (exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)).spent +
    (exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)).waste =
    s.physical.core.fuel+p.base.selector.packet at he
  rw [hstate] at he
  change (PredictionAction.cycleEnd p s).physical.core.fuel+
    (PredictionAction.cycleEnd p s).physical.core.packets*p.base.selector.packet+
    (PredictionAction.cycleEnd p s).physical.remainder+
    PredictionAction.spentAlong p s PredictionAction.cycleEvents =
    s.physical.core.fuel+s.physical.core.packets*p.base.selector.packet+s.physical.remainder at old
  rw [rem] at old
  dsimp only
  omega

theorem payable_spent_and_waste_overlap (p : PredictionAction.Parameters) (s : PredictionAction.State)
    (written : Bool) (b : Seed) (hb : b.available = true)
    (h : PredictionAction.CycleEnabled p s) (hp : UpdaterFormation.Admissible p.base) :
    let r := exposure (oldParameters p) .variable s.physical.core.regime b (oldState s written)
    r.spent = p.rent+PredictionAction.expenditure p s .work+p.writing ∧
      r.waste = PredictionAction.waste p s .work := by
  have h1 := payable_total_account_overlap p s written b hb h hp
  have h2 := (payable_receipt_overlap p s written b hb h).2.2
  rw [old_cycle_marked_account] at h1
  dsimp only at *
  exact ⟨by omega,h2⟩

/-- The existing phase law blocks at observed when writing is unaffordable;
the exposure law returns the continuing worn state. Both comparisons use the
same initial stock, genuine mismatch and existing primary tariffs. -/
theorem unpaid_write_is_not_old_completed_cycle :
    let s := PredictionAction.exampleState 4 1 0 false 6 true true 2
    let observed := PredictionAction.advance PredictionAction.primary
      (PredictionAction.advance PredictionAction.primary s .rent) .work
    let r := exposure (oldParameters PredictionAction.primary) .variable true
      ⟨false,false,true⟩ (oldState s false)
    observed.phase = .observed ∧ ¬ PredictionAction.Enabled PredictionAction.primary observed .write ∧
    r.status = .workedUnpaid ∧ r.state.life = 5 ∧ r.state.gateLife = 1 ∧
    observed.physical.core.lease = 6 ∧ observed.physical.moduleLease = 2 := by decide

/-- An unworked old partial cycle retains its packet; a scheduled exposure loses
that packet. No proof identifies these different boundaries. -/
theorem no_work_is_not_old_source_boundary :
    let s := PredictionAction.exampleState 1 1 0 false 6 true true 2
    let rented := PredictionAction.advance PredictionAction.primary s .rent
    let r := exposure (oldParameters PredictionAction.primary) .variable true
      ⟨false,false,true⟩ (oldState s false)
    ¬ PredictionAction.Enabled PredictionAction.primary rented .work ∧
    rented.physical.core.packets = 1 ∧ r.status = .noWork ∧
    r.worked = false ∧ r.waste = 10 := by decide

end StochasticPrediction

#print axioms StochasticPrediction.old_command_agrees
#print axioms StochasticPrediction.old_update_agrees
#print axioms StochasticPrediction.installed_preparation_identity
#print axioms StochasticPrediction.payable_cycle_overlap
#print axioms StochasticPrediction.payable_receipt_overlap
#print axioms StochasticPrediction.payable_cycle_packet_debit
#print axioms StochasticPrediction.old_cycle_marked_account
#print axioms StochasticPrediction.payable_total_account_overlap
#print axioms StochasticPrediction.payable_spent_and_waste_overlap
#print axioms StochasticPrediction.unpaid_write_is_not_old_completed_cycle
#print axioms StochasticPrediction.no_work_is_not_old_source_boundary
