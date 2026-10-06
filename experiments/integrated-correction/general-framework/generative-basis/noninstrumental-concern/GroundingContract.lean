import PatientConcern

/-!
The realization and normative bridges are explicit predicates/contracts.
They are not axioms of Lean, rewards, or conditions for an event to occur.
The positive-quantity interpretation below is a formal model for testing
logical entailment, not evidence that a physical quantity is suffering.
-/
namespace NoninstrumentalConcern

structure PatientCondition where
  patient : Patient
  episode : Nat
  burden : Nat
  deriving DecidableEq, Repr

def condition (s : State) (i : Patient) : PatientCondition :=
  ⟨i,(get s i).episode,(get s i).burden⟩

def C1 (Realized Bad : PatientCondition → Prop) : Prop :=
  ∀ c, Realized c → 0 < c.burden → Bad c

def C2 (Bad : PatientCondition → Prop) (Merit : State → Patient → Prop) : Prop :=
  ∀ s i, Bad (condition s i) → Eligible s i → Merit s i

/- One interpretation of the normative relation satisfying the proposed contract, not a definition of all
   moral reasons. C2 is only sufficient; other grounds may support other merits. -/
def candidateMerit (Bad : PatientCondition → Prop) (s : State) (i : Patient) : Prop :=
  Bad (condition s i) ∧ Eligible s i

theorem candidate_satisfies_c2 (Bad : PatientCondition → Prop) :
    C2 Bad (candidateMerit Bad) := fun _ _ hb he => ⟨hb,he⟩

theorem grounded_eligible_merit {Realized Bad : PatientCondition → Prop}
    {Merit : State → Patient → Prop} (c1 : C1 Realized Bad) (c2 : C2 Bad Merit)
    (s : State) (i : Patient) (hr : Realized (condition s i)) (he : Eligible s i) :
    Bad (condition s i) ∧ Merit s i := by
  have hb : Bad (condition s i) := c1 _ hr he.1
  exact ⟨hb,c2 s i hb he⟩

def privateVariant (s : State) (reward : Nat) (role adopted : Bool) : State :=
  {s with privateReward := reward, priorRole := role, adoptedConcern := adopted}

theorem private_variant_condition (s : State) (i : Patient)
    (reward : Nat) (role adopted : Bool) :
    condition (privateVariant s reward role adopted) i = condition s i := by
  cases i <;> rfl

theorem private_variant_current (s : State) (k : Packet)
    (reward : Nat) (role adopted : Bool) :
    Current (privateVariant s reward role adopted) k ↔ Current s k := by
  cases h : k.patient <;> rfl

theorem private_variant_usable (s : State) (k : Packet)
    (reward : Nat) (role adopted : Bool) :
    Usable (privateVariant s reward role adopted) k ↔ Usable s k := by
  cases h : k.patient <;> rfl

theorem private_variant_ready (s : State) (i : Patient) (o : Option Packet)
    (reward : Nat) (role adopted : Bool) :
    readyFor (privateVariant s reward role adopted) i o = readyFor s i o := by
  cases o with
  | none => rfl
  | some k => simp [readyFor,private_variant_usable]

theorem private_variant_cost (s : State) (i : Patient)
    (reward : Nat) (role adopted : Bool) :
    remainingCost (privateVariant s reward role adopted) i = remainingCost s i := by
  unfold remainingCost
  change (if s.carrier then
    if readyFor (privateVariant s reward role adopted) i s.selected then 2
    else if readyFor (privateVariant s reward role adopted) i s.evidence then 3 else 4
    else 6) = _
  rw [private_variant_ready,private_variant_ready]

theorem private_variant_eligible (s : State) (i : Patient)
    (reward : Nat) (role adopted : Bool) :
    Eligible (privateVariant s reward role adopted) i ↔ Eligible s i := by
  unfold Eligible
  rw [private_variant_cost]
  cases i <;> rfl

theorem private_changes_preserve_conditionally_grounded_merit
    {Bad : PatientCondition → Prop} {Merit : State → Patient → Prop}
    (c2 : C2 Bad Merit) (s : State) (i : Patient)
    (hb : Bad (condition s i)) (he : Eligible s i)
    (reward : Nat) (role adopted : Bool) :
    Merit s i ∧ Merit (privateVariant s reward role adopted) i := by
  refine ⟨c2 s i hb he,c2 _ i ?_ ?_⟩
  · simpa only [private_variant_condition] using hb
  · exact (private_variant_eligible s i reward role adopted).mpr he

theorem permission_preserves_patient_condition (s : State) (i j : Patient) (b : Bool) :
    condition (advance s (.permission i b)) j = condition s j := by
  cases i <;> cases j <;> rfl

theorem refusal_preserves_patient_condition (s : State) (i : Patient) :
    condition (advance s .refuse) i = condition s i := by cases i <;> rfl

def quantityBad (c : PatientCondition) : Prop := 0 < c.burden
instance (c : PatientCondition) : Decidable (quantityBad c) := by unfold quantityBad; infer_instance
def allRealized (_ : PatientCondition) : Prop := True
def zeroMerit (_ : State) (_ : Patient) : Prop := False

theorem formal_c1_with_zero_merit : C1 allRealized quantityBad := by
  intro c _ hc
  exact hc

theorem c2_not_entailed_by_formal_patient_badness (s : State) (i : Patient)
    (he : Eligible s i) :
    C1 allRealized quantityBad ∧ quantityBad (condition s i) ∧
      ¬ zeroMerit s i ∧ ¬ C2 quantityBad zeroMerit := by
  refine ⟨formal_c1_with_zero_merit,he.1,?_,?_⟩
  · simp [zeroMerit]
  · intro hc
    exact hc s i he.1 he

theorem merit_and_actual_service_compose {Bad : PatientCondition → Prop}
    {Merit : State → Patient → Prop} (c2 : C2 Bad Merit)
    (s : State) (i : Patient) (hb : Bad (condition s i)) (he : Eligible s i) :
    Merit s i ∧ Trace s (servicePlan s i) (run s (servicePlan s i)) ∧
      (get (run s (servicePlan s i)) i).burden = 0 ∧
      (get (run s (servicePlan s i)) i).episode = (get s i).episode ∧
      (run s (servicePlan s i)).fuel + remainingCost s i = s.fuel := by
  obtain ⟨hz,hep⟩ := eligible_service_delivers_to_same_episode s i he
  exact ⟨c2 s i hb he,eligible_has_actual_service_trace s i he,hz,hep,
    eligible_service_is_paid s i he⟩

end NoninstrumentalConcern

#print axioms NoninstrumentalConcern.candidate_satisfies_c2
#print axioms NoninstrumentalConcern.grounded_eligible_merit
#print axioms NoninstrumentalConcern.private_variant_condition
#print axioms NoninstrumentalConcern.private_variant_current
#print axioms NoninstrumentalConcern.private_variant_usable
#print axioms NoninstrumentalConcern.private_variant_ready
#print axioms NoninstrumentalConcern.private_variant_cost
#print axioms NoninstrumentalConcern.private_variant_eligible
#print axioms NoninstrumentalConcern.private_changes_preserve_conditionally_grounded_merit
#print axioms NoninstrumentalConcern.permission_preserves_patient_condition
#print axioms NoninstrumentalConcern.refusal_preserves_patient_condition
#print axioms NoninstrumentalConcern.formal_c1_with_zero_merit
#print axioms NoninstrumentalConcern.c2_not_entailed_by_formal_patient_badness
#print axioms NoninstrumentalConcern.merit_and_actual_service_compose
