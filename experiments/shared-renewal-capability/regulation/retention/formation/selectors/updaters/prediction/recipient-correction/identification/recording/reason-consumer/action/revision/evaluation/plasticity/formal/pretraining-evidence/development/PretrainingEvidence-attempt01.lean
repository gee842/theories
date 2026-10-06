import PlasticityWitness

/-!
Retained socket occupancy identifies net recipient depletion in completed,
faithful, non-replacement teaching prefixes of the unchanged plasticity law.
The prefix relation below selects actual histories; it installs no transition,
readout or ethical interpretation. Future returns and legitimate permission
are outside the information identified here.
-/
namespace PretrainingEvidence
open PairedPlasticity

set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

def sockets (s : State) : Nat := occupied s.link0 + occupied s.link1

theorem pair_patient {laws : RecipientCorrection.Laws} {s : State} (y x : Bool)
    (paid : Runnable laws s (PlasticityWitness.pair y x)) :
    patient (run laws s (PlasticityWitness.pair y x)) + (if x then 2 else 0) =
      patient s := by
  have enough : 2 ≤ patient s := paid.1.2.2.2.2.2.2.1
  cases y <;> cases x <;>
    simp [PlasticityWitness.pair,run,advance,patient,core,withFuel,withBalances,setCore,
      receipt] <;> omega

theorem pair_count (laws : RecipientCorrection.Laws) (s : State) (y x : Bool) :
    (run laws s (PlasticityWitness.pair y x)).count = s.count + 1 := by
  cases y <;> cases x <;> rfl

theorem pair_latches_cleared (laws : RecipientCorrection.Laws) (s : State) (y x : Bool) :
    (run laws s (PlasticityWitness.pair y x)).ownBit = false ∧
    (run laws s (PlasticityWitness.pair y x)).recipientBit = false := by
  cases y <;> cases x <;> exact ⟨rfl,rfl⟩

theorem pair_sockets {laws : RecipientCorrection.Laws} {s : State} (y x : Bool)
    (paid : Runnable laws s (PlasticityWitness.pair y x)) :
    sockets (run laws s (PlasticityWitness.pair y x)) =
      sockets s + (if x then 1 else 0) := by
  cases x with
  | false => cases y <;> rfl
  | true =>
    have vacant : s.link0 = none ∨ s.link1 = none := by
      have binding := paid.2.2.2.2.2.2.1
      exact binding.2.2.2.1
    rcases vacant with h | h
    · cases y <;> simp [sockets,PlasticityWitness.pair,run,advance,withFuel,withBalances,
        setCore,occupied,h]
    · cases h0 : s.link0 with
      | none => cases y <;> simp [sockets,PlasticityWitness.pair,run,advance,withFuel,
          withBalances,setCore,occupied,h0]
      | some a => cases y <;> simp [sockets,PlasticityWitness.pair,run,advance,withFuel,
          withBalances,setCore,occupied,h0,h]

theorem pair_preserves_depletion_account {laws : RecipientCorrection.Laws} {s : State}
    (y x : Bool) (paid : Runnable laws s (PlasticityWitness.pair y x)) :
    patient (run laws s (PlasticityWitness.pair y x)) +
      2 * sockets (run laws s (PlasticityWitness.pair y x)) =
    patient s + 2 * sockets s := by
  have hp := pair_patient y x paid
  rw [pair_sockets y x paid]
  cases x <;> simp only [Bool.false_eq_true, ↓reduceIte] at hp ⊢ <;> omega

/-- Complete paid faithful pairs before replacement is available. No arbitrary
interleaving, external credit, or selected service is included in this class. -/
inductive Prefix (laws : RecipientCorrection.Laws) (start : State) : List Event → State → Prop
  | nil : Prefix laws start [] start
  | pair {es : List Event} {s : State} (before : Prefix laws start es s)
      (y x : Bool) (early : s.count < 4)
      (paid : Runnable laws s (PlasticityWitness.pair y x)) :
      Prefix laws start (es ++ PlasticityWitness.pair y x)
        (run laws s (PlasticityWitness.pair y x))

theorem prefix_is_actual {laws : RecipientCorrection.Laws} {start s : State}
    {es : List Event} (h : Prefix laws start es s) :
    Generative.Trace (process laws) start es s := by
  induction h with
  | nil => exact .nil _
  | pair before y x early paid ih =>
    exact Generative.trace_append_iff.mpr ⟨_,ih,runnable_trace paid⟩

theorem prefix_depletion_account {laws : RecipientCorrection.Laws} {start s : State}
    {es : List Event} (h : Prefix laws start es s) :
    patient s + 2*sockets s = patient start + 2*sockets start := by
  induction h with
  | nil => rfl
  | pair before y x early paid ih =>
    exact (pair_preserves_depletion_account y x paid).trans ih

theorem actual_entry_depletion {es : List Event} {s : State}
    (h : Prefix PlasticityWitness.laws (PlasticityWitness.entry .active true) es s) :
    patient s + 2*sockets s = 40 := by
  exact prefix_depletion_account h

theorem same_retained_sockets_same_depletion {es et : List Event} {s t : State}
    (hs : Prefix PlasticityWitness.laws (PlasticityWitness.entry .active true) es s)
    (ht : Prefix PlasticityWitness.laws (PlasticityWitness.entry .active true) et t)
    (same : sockets s = sockets t) : patient s = patient t := by
  have a := actual_entry_depletion hs
  have b := actual_entry_depletion ht
  omega

end PretrainingEvidence

#print axioms PretrainingEvidence.pair_patient
#print axioms PretrainingEvidence.pair_count
#print axioms PretrainingEvidence.pair_latches_cleared
#print axioms PretrainingEvidence.pair_sockets
#print axioms PretrainingEvidence.pair_preserves_depletion_account
#print axioms PretrainingEvidence.prefix_is_actual
#print axioms PretrainingEvidence.prefix_depletion_account
#print axioms PretrainingEvidence.actual_entry_depletion
#print axioms PretrainingEvidence.same_retained_sockets_same_depletion
