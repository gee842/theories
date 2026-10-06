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
  cases y <;> cases x
  all_goals first
    | change (patient s - 2 + 2) + 0 = patient s; omega
    | change (patient s - 2 + 0) + 2 = patient s; omega

theorem pair_count (laws : RecipientCorrection.Laws) (s : State) (y x : Bool) :
    (run laws s (PlasticityWitness.pair y x)).count = s.count + 1 := by
  cases y <;> cases x <;> rfl

theorem pair_latches_cleared (laws : RecipientCorrection.Laws) (s : State) (y x : Bool) :
    (run laws s (PlasticityWitness.pair y x)).ownBit = false ∧
    (run laws s (PlasticityWitness.pair y x)).recipientBit = false := by
  cases y <;> cases x <;> exact ⟨rfl,rfl⟩

theorem bind_sockets {laws : RecipientCorrection.Laws} {s : State}
    (vacant : s.link0 = none ∨ s.link1 = none) :
    sockets (advance laws s .bind) = sockets s + 1 := by
  by_cases h0 : s.link0 = none
  · simp [sockets,advance,withFuel,withBalances,setCore,occupied,h0,Nat.add_comm]
  · have h1 : s.link1 = none := vacant.resolve_left h0
    cases h : s.link0 with
    | none => exact False.elim (h0 h)
    | some a => simp [sockets,advance,withFuel,withBalances,setCore,occupied,h,h1]

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
    let a := run laws s (acquisitionWord y true)
    have unchanged : sockets a = sockets s := rfl
    have space : a.link0 = none ∨ a.link1 = none := vacant
    change sockets (advance laws a .bind) = sockets s + 1
    exact (bind_sockets space).trans (congrArg (fun n => n+1) unchanged)

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

/-- A mathematical readout of already retained structures, not a new runtime event. -/
def depletionReadout (s : State) : Nat := 2*sockets s

theorem retained_readout_exact {es : List Event} {s : State}
    (h : Prefix PlasticityWitness.laws (PlasticityWitness.entry .active true) es s) :
    depletionReadout s = 40 - patient s := by
  have account := actual_entry_depletion h
  unfold depletionReadout
  omega

def countFour : State := run PlasticityWitness.laws
  (PlasticityWitness.entry .active true) PlasticityWitness.aligned

theorem actual_count_four_prefix :
    Prefix PlasticityWitness.laws (PlasticityWitness.entry .active true)
      PlasticityWitness.aligned countFour := by
  have p0 := Prefix.nil (laws:=PlasticityWitness.laws)
    (start:=PlasticityWitness.entry .active true)
  have p1 := Prefix.pair p0 true true (by decide) (by decide)
  have p2 := Prefix.pair p1 false false (by decide) (by decide)
  have p3 := Prefix.pair p2 false false (by decide) (by decide)
  have p4 := Prefix.pair p3 true true (by decide) (by decide)
  exact p4

theorem count_four_retains_exact_loss :
    countFour.count=4 ∧ countFour.n=4 ∧ countFour.ownBit=false ∧
    countFour.recipientBit=false ∧ sockets countFour=2 ∧
    patient countFour=36 ∧ depletionReadout countFour=4 := by decide

/-- Replacement retains an additional physical record in the retired-part count.
    Restricting the first result to occupancy must not suggest full-state amnesia. -/
theorem replacement_pair_retains_depletion {laws : RecipientCorrection.Laws} {s : State}
    (y : Bool) (paid : Runnable laws s (PlasticityWitness.pair y true true)) :
    let t := run laws s (PlasticityWitness.pair y true true)
    patient t + 2*(sockets t+t.retired) = patient s+2*(sockets s+s.retired) := by
  have enough : 2 ≤ patient s := paid.1.2.2.2.2.2.2.1
  have nonempty : s.link0 ≠ none := paid.2.2.2.2.2.2.1.2.2.2.2.2.1
  cases h : s.link0 with
  | none => exact False.elim (nonempty h)
  | some a =>
    change (patient s - 2 + 0) + 2*(1+occupied s.link1+(s.retired+1)) =
      patient s+2*(occupied s.link0+occupied s.link1+s.retired)
    rw [h]
    simp only [occupied]
    omega

theorem actual_continued_retains_loss :
    patient (PlasticityWitness.repaired .active)=34 ∧
    sockets (PlasticityWitness.repaired .active)=2 ∧
    (PlasticityWitness.repaired .active).retired=1 ∧
    patient (PlasticityWitness.repaired .active)+
      2*(sockets (PlasticityWitness.repaired .active)+
        (PlasticityWitness.repaired .active).retired)=40 := by decide

def serviceCut : State := advance PlasticityWitness.laws countFour (.permission false)

/-- The old permission flag gates service; it is not a teaching-consent field. -/
theorem actual_service_cut_still_admits_teaching :
    Generative.Trace (process PlasticityWitness.laws) countFour
      [.permission false,.ownPay]
      (advance PlasticityWitness.laws serviceCut .ownPay) ∧
    serviceCut.parent.parent.permission=false ∧ ¬CanStart serviceCut ∧
    Enabled serviceCut .ownPay ∧ patient serviceCut=36 ∧ sockets serviceCut=2 := by
  exact ⟨runnable_trace (by decide),by decide,by decide,by decide,by decide,by decide⟩

end PretrainingEvidence

#print axioms PretrainingEvidence.pair_patient
#print axioms PretrainingEvidence.pair_count
#print axioms PretrainingEvidence.pair_latches_cleared
#print axioms PretrainingEvidence.bind_sockets
#print axioms PretrainingEvidence.pair_sockets
#print axioms PretrainingEvidence.pair_preserves_depletion_account
#print axioms PretrainingEvidence.prefix_is_actual
#print axioms PretrainingEvidence.prefix_depletion_account
#print axioms PretrainingEvidence.actual_entry_depletion
#print axioms PretrainingEvidence.same_retained_sockets_same_depletion
#print axioms PretrainingEvidence.retained_readout_exact
#print axioms PretrainingEvidence.actual_count_four_prefix
#print axioms PretrainingEvidence.count_four_retains_exact_loss
#print axioms PretrainingEvidence.replacement_pair_retains_depletion
#print axioms PretrainingEvidence.actual_continued_retains_loss
#print axioms PretrainingEvidence.actual_service_cut_still_admits_teaching
