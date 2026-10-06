import FiniteExposureKernel

namespace StochasticPrediction

/-- Stronger source-domain condition. The bounded natural-state algebra allows
more states; Python correspondence uses physically coherent live gate codes. -/
def SourceCoherent (s : State) : Prop := 0 < s.gateLife → s.gate < 2

def SourceParameters (p : Parameters) : Prop :=
  Admissible p ∧ 0 < p.gateAssembly ∧ 0 < p.base ∧ 0 < p.retrofit ∧
  0 < p.rent ∧ 0 < p.trial ∧ 0 < p.writing ∧ 0 < p.renewal ∧ 0 < p.gateRenewal

theorem formation_preserves_coherence (p : Parameters) (a : Arm) (b : Seed)
    (s : State) (h : SourceCoherent s) : SourceCoherent (prepared p a b s) := by
  have hg : SourceCoherent (formGate p a b.gate s) := by
    unfold formGate
    split
    · intro _
      dsimp only
      unfold gateKind
      split <;> (try split) <;> (try split) <;> omega
    · exact h
  have hb : SourceCoherent (formBase p b.prior (formGate p a b.gate s)) := by
    unfold formBase
    split <;> exact hg
  unfold prepared retrofit
  split <;> exact hb

theorem exposure_preserves_coherence (p : Parameters) (a : Arm) (z : Bool) (b : Seed)
    (s : State) (h : SourceCoherent s) : SourceCoherent (exposure p a z b s).state := by
  have hp := formation_preserves_coherence p a b s h
  unfold exposure
  dsimp only
  generalize prepared p a b s = t at *
  unfold operate
  split
  · exact hp
  · split
    · exact hp
    · dsimp only
      split
      · exact hp
      · rename_i hl hr hw
        have hg : 0 < t.gateLife := by omega
        have hh := hp hg
        unfold trial
        dsimp only
        intro _
        exact hh

def exampleParameters : Parameters := ⟨2,1,3,1,3,6,1,1,10,6,2⟩
def liveExample : State := ⟨8,1,2,2,6,0,false,false⟩
def seed (available : Bool) : Seed := ⟨false,false,available⟩

theorem example_source_domain : SourceParameters exampleParameters ∧
    Valid exampleParameters liveExample ∧ SourceCoherent liveExample := by
  unfold SourceParameters Admissible Valid SourceCoherent
  decide

/-- The first lost opportunity does not become an absorbing death. The later
capture and paid write occur on its actual continuing fuel/lifetime state. -/
theorem unpaid_then_paid_continuation :
    let r₁ := exposure exampleParameters .variable false (seed false) liveExample
    let r₂ := exposure exampleParameters .variable false (seed true) r₁.state
    r₁.status = .workedUnpaid ∧ r₁.state.fuel = 4 ∧ r₁.state.q = 0 ∧
    r₁.state.gateLife = 1 ∧ r₁.state.life = 5 ∧
    r₂.status = .workedPaid ∧ r₂.captured = true ∧ r₂.state.fuel = 2 ∧
    r₂.state.q = 0 := by decide

def counted (rs : Weighted (List Result)) (accept : List Result → Bool) : Nat :=
  mass (rs.filter (fun (xs,_) => accept xs))

def secondCapture (rs : List Result) : Bool :=
  match rs with | [_,r] => r.captured | _ => false

def paidFirstAndSecondCapture (rs : List Result) : Bool :=
  match rs with | [r₁,r₂] => r₁.wrote && r₂.captured | _ => false

theorem discarded_unpaid_loses_future_mass :
    let ps := paths exampleParameters .variable 1 2 liveExample [false,false]
    mass ps = 64 ∧ counted ps secondCapture = 32 ∧
    counted ps paidFirstAndSecondCapture = 16 := by decide

theorem no_work_still_loses_packet :
    let r := exposure exampleParameters .variable false (seed true) {liveExample with fuel := 1}
    r.status = .noWork ∧ r.worked = false ∧ r.state.fuel = 0 ∧
    r.state.life = 6 ∧ r.state.gateLife = 2 ∧ r.spent = 1 ∧ r.waste = 10 := by decide

theorem failed_rent_resets_operative_memory :
    let r := exposure exampleParameters .variable true (seed true)
      {liveExample with fuel := 0, q := 4, last := true, written := true}
    r.status = .rentFailed ∧ r.state.stage = 0 ∧ r.state.life = 0 ∧
    r.state.q = 2 ∧ r.state.last = false ∧ r.state.written = false ∧
    r.state.gate = 1 ∧ r.state.gateLife = 2 ∧ r.waste = 10 := by decide

def wroteOutcome (rw : Result × Nat) : Bool := rw.1.wrote

def capturedOutcome (rw : Result × Nat) : Bool := rw.1.captured

/-- A write-conditioned report discards half the outcomes in this example and
reports receipt frequency one where the actual exposure frequency is one half. -/
theorem paid_write_selection_bias :
    let ks := kernel exampleParameters .variable false 1 2 liveExample
    mass ks = 8 ∧ mass (ks.filter wroteOutcome) = 4 ∧
    mass (ks.filter capturedOutcome) = 4 ∧
    mass (ks.filter (fun rw => wroteOutcome rw && capturedOutcome rw)) = 4 := by decide

/-- Fixed support can disappear without q changing: the previous example is
productive continuation and later writing, not evidence of a changed score. -/
theorem zero_score_retained_across_the_example :
    (exposure exampleParameters .variable false (seed true)
      (exposure exampleParameters .variable false (seed false) liveExample).state).state.q =
      liveExample.q := by decide

end StochasticPrediction

#print axioms StochasticPrediction.formation_preserves_coherence
#print axioms StochasticPrediction.exposure_preserves_coherence
#print axioms StochasticPrediction.example_source_domain
#print axioms StochasticPrediction.unpaid_then_paid_continuation
#print axioms StochasticPrediction.discarded_unpaid_loses_future_mass
#print axioms StochasticPrediction.no_work_still_loses_packet
#print axioms StochasticPrediction.failed_rent_resets_operative_memory
#print axioms StochasticPrediction.paid_write_selection_bias
#print axioms StochasticPrediction.zero_score_retained_across_the_example
