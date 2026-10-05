import Std

/-!
An interface for checking addressed claims against actual action histories.

The ledger below is mathematical verification state, not newly constructed
memory, a free observer, a source of moral reasons, or an autonomous selector.
Admission, authority, evidence adequacy and causal certificate soundness are
independent hypotheses. An episode's admitted claims stay fixed in these
theorems; normative revision requires a different justified operation.

`Trace paidStep` must be instantiated with the actual enabled, charged event
law. The theorem does not establish that an arbitrary relation pays its bills.
The exported event word must include selection/evidence expenses if those are
claimed; otherwise those activities are outside the theorem's execution scope.
No complete audit, expected reward, or repeated inspection module is required.
-/

namespace ClaimLedger

universe u v w x y

structure AddressedClaim (Patient : Type u) (Context : Type v)
    (Episode : Type w) (Ground : Type x) (Actor : Type y) where
  patient : Patient
  context : Context
  episode : Episode
  ground : Ground
  addressee : Actor

structure Ledger (Claim : Type u) where
  admitted : Claim → Prop
  certified : Claim → Prop

def initial {Claim : Type u} (K : Claim → Prop) : Ledger Claim :=
  ⟨K, fun _ => False⟩

def record {Claim : Type u} (s : Ledger Claim) (D : Claim → Prop) : Ledger Claim :=
  ⟨s.admitted, fun c => s.certified c ∨ (s.admitted c ∧ D c)⟩

def unresolved {Claim : Type u} (s : Ledger Claim) (c : Claim) : Prop :=
  s.admitted c ∧ ¬ s.certified c

def WellFormed {Claim : Type u} (s : Ledger Claim) : Prop :=
  ∀ c, s.certified c → s.admitted c

theorem distinct_patient_keeps_claim_distinct
    {Patient : Type u} {Context : Type v} {Episode : Type w}
    {Ground : Type x} {Actor : Type y}
    {a b : AddressedClaim Patient Context Episode Ground Actor}
    (h : a.patient ≠ b.patient) : a ≠ b := by
  intro hab
  exact h (congrArg AddressedClaim.patient hab)

theorem distinct_episode_keeps_claim_distinct
    {Patient : Type u} {Context : Type v} {Episode : Type w}
    {Ground : Type x} {Actor : Type y}
    {a b : AddressedClaim Patient Context Episode Ground Actor}
    (h : a.episode ≠ b.episode) : a ≠ b := by
  intro hab
  exact h (congrArg AddressedClaim.episode hab)

theorem initial_wellFormed {Claim : Type u} (K : Claim → Prop) :
    WellFormed (initial K) := by
  intro _ impossible
  exact False.elim impossible

theorem record_admitted {Claim : Type u} (s : Ledger Claim) (D : Claim → Prop) :
    (record s D).admitted = s.admitted := rfl

theorem record_wellFormed {Claim : Type u} {s : Ledger Claim}
    (hs : WellFormed s) (D : Claim → Prop) : WellFormed (record s D) := by
  intro c hc
  exact hc.elim (hs c) And.left

theorem unresolved_partition {Claim : Type u} {s : Ledger Claim}
    (hs : WellFormed s) (c : Claim) :
    s.admitted c ↔ s.certified c ∨ unresolved s c := by
  constructor
  · intro ha
    classical
    by_cases hc : s.certified c
    · exact Or.inl hc
    · exact Or.inr ⟨ha,hc⟩
  · intro h
    exact h.elim (hs c) And.left

theorem certified_disjoint_unresolved {Claim : Type u} (s : Ledger Claim) (c : Claim) :
    ¬ (s.certified c ∧ unresolved s c) := by
  rintro ⟨hc,_,hn⟩
  exact hn hc

theorem record_unresolved_exact {Claim : Type u} (s : Ledger Claim)
    (D : Claim → Prop) (c : Claim) :
    unresolved (record s D) c ↔ unresolved s c ∧ ¬ D c := by
  constructor
  · rintro ⟨ha,hn⟩
    exact ⟨⟨ha,fun hc => hn (Or.inl hc)⟩,fun hd => hn (Or.inr ⟨ha,hd⟩)⟩
  · rintro ⟨⟨ha,hn⟩,hd⟩
    exact ⟨ha,fun hc => hc.elim hn (fun h => hd h.2)⟩

theorem no_new_certificate_preserves_unresolved {Claim : Type u}
    (s : Ledger Claim) (D : Claim → Prop) (c : Claim) (unknown : ¬ D c) :
    unresolved (record s D) c ↔ unresolved s c := by
  rw [record_unresolved_exact]
  exact ⟨And.left,fun h => ⟨h,unknown⟩⟩

theorem unresolved_retains_independently_admitted_reason {Claim : Type u}
    {s : Ledger Claim} {Reason : Claim → Prop}
    (grounded : ∀ c, s.admitted c → Reason c) {c : Claim}
    (pending : unresolved s c) : Reason c := grounded c pending.1

/- Soundness is about the actual addressed effect at the assessment horizon.
It is not established by recording a token. Old certificates need their own
soundness at that same horizon even when every new certificate is sound. -/
theorem recorded_certificates_sound {Claim : Type u} (s : Ledger Claim)
    (D Met : Claim → Prop)
    (oldSound : ∀ c, s.certified c → Met c)
    (newSound : ∀ c, s.admitted c → D c → Met c) :
    ∀ c, (record s D).certified c → Met c := by
  intro c hc
  exact hc.elim (oldSound c) (fun h => newSound c h.1 h.2)

theorem recorded_sound_iff_old_sound {Claim : Type u} (s : Ledger Claim)
    (D Met : Claim → Prop)
    (newSound : ∀ c, s.admitted c → D c → Met c) :
    (∀ c, (record s D).certified c → Met c) ↔
      (∀ c, s.certified c → Met c) := by
  constructor
  · intro h c hc
    exact h c (Or.inl hc)
  · intro h
    exact recorded_certificates_sound s D Met h newSound

inductive Trace {World : Type u} {Event : Type v}
    (paidStep : World → Event → World → Prop) : World → List Event → World → Prop where
  | nil (s : World) : Trace paidStep s [] s
  | cons {s m t : World} {e : Event} {es : List Event} :
      paidStep s e m → Trace paidStep m es t → Trace paidStep s (e::es) t

theorem traces_compose {World : Type u} {Event : Type v}
    {paidStep : World → Event → World → Prop} {s m t : World}
    {as bs : List Event} (first : Trace paidStep s as m)
    (second : Trace paidStep m bs t) : Trace paidStep s (as++bs) t := by
  induction first with
  | nil => exact second
  | cons head _ ih => exact Trace.cons head (ih second)

/- The choice is an input. Partial evidence need only contain the actual state;
no number of consistent labels is taken as a proof of that membership.
Actual execution, permission and certificate soundness are separate premises. -/
theorem partial_evidence_actual_execution
    {World : Type u} {Event : Type v} {Action : Type w} {Claim : Type x}
    {paidStep : World → Event → World → Prop}
    (possible : World → Prop) (K D : Claim → Prop)
    (Permitted : World → Action → Prop) (Met : World → Claim → Prop)
    (word : Action → List Event) {actual final : World} (choice : Action)
    (containsActual : possible actual)
    (authority : ∀ h, possible h → Permitted h choice)
    (execution : Trace paidStep actual (word choice) final)
    (certificate : ∀ h, possible h → ∀ t,
      Trace paidStep h (word choice) t → ∀ c, K c → D c → Met t c) :
    Permitted actual choice ∧ Trace paidStep actual (word choice) final ∧
      (record (initial K) D).admitted = K ∧
      (∀ c, (record (initial K) D).certified c → Met final c) ∧
      (∀ c, unresolved (record (initial K) D) c → K c) := by
  refine ⟨authority actual containsActual,execution,rfl,?_,?_⟩
  · apply recorded_certificates_sound
    · intro _ impossible
      exact False.elim impossible
    · exact certificate actual containsActual final execution
  · intro _ hp
    exact hp.1

/- Accumulating episode certificates across two actual segments requires an
explicit persistence condition. This is appropriate for permanently attained
historical service, not automatically for no-harm over an expanding interval. -/
theorem successive_execution_with_persistent_claims
    {World : Type u} {Event : Type v} {Claim : Type w}
    {paidStep : World → Event → World → Prop}
    {s m t : World} {as bs : List Event}
    (first : Trace paidStep s as m) (second : Trace paidStep m bs t)
    (ledger : Ledger Claim) (D : Claim → Prop) (Met : World → Claim → Prop)
    (oldSound : ∀ c, ledger.certified c → Met m c)
    (persists : ∀ c, ledger.certified c → Met m c → Met t c)
    (newSound : ∀ c, ledger.admitted c → D c → Met t c) :
    Trace paidStep s (as++bs) t ∧
      (record ledger D).admitted = ledger.admitted ∧
      (∀ c, (record ledger D).certified c → Met t c) := by
  refine ⟨traces_compose first second,rfl,?_⟩
  exact recorded_certificates_sound ledger D (Met t)
    (fun c hc => persists c hc (oldSound c hc)) newSound

/- A complete small menu of two positive services. These are not the parent
protection law's harmless-withdrawal options. The fixture claims only that
one unit cannot purchase two unit services in this declared episode. -/
inductive Patient where | p | q
deriving DecidableEq, Repr

inductive Service where | wait | serveP | serveQ | serveBoth
deriving DecidableEq, Repr

def serviceCost : Service → Nat
  | .wait => 0
  | .serveP | .serveQ => 1
  | .serveBoth => 2

def services : Service → Patient → Prop
  | .wait,_ => False
  | .serveP,patient => patient=.p
  | .serveQ,patient => patient=.q
  | .serveBoth,_ => True

structure ServiceState where
  cash : Nat
  suppliedP : Bool
  suppliedQ : Bool
deriving DecidableEq, Repr

def serviceAdvance (s : ServiceState) (a : Service) : ServiceState :=
  ⟨s.cash-serviceCost a,
   s.suppliedP || (a==.serveP || a==.serveBoth),
   s.suppliedQ || (a==.serveQ || a==.serveBoth)⟩

def serviceStep (s : ServiceState) (a : Service) (t : ServiceState) : Prop :=
  serviceCost a ≤ s.cash ∧ t=serviceAdvance s a

theorem service_step_is_paid {s t : ServiceState} {a : Service}
    (h : serviceStep s a t) :
    serviceCost a ≤ s.cash ∧ t.cash+serviceCost a=s.cash := by
  rcases h with ⟨hpay,rfl⟩
  exact ⟨hpay,by simp only [serviceAdvance]; omega⟩

theorem one_unit_cannot_deliver_both_positive_services :
    ∀ a : Service, serviceCost a ≤ 1 → ¬ (∀ patient, services a patient) := by
  intro a
  cases a with
  | wait => intro _ h; exact h .p
  | serveP => intro _ h; have bad := h .q; cases bad
  | serveQ => intro _ h; have bad := h .p; cases bad
  | serveBoth => intro h; simp [serviceCost] at h

theorem paid_service_preserves_unfulfilled_claim :
    let K : Patient → Prop := fun _ => True
    let before : ServiceState := ⟨1,false,false⟩
    let after := serviceAdvance before .serveP
    Trace serviceStep before [.serveP] after ∧ after.cash=0 ∧
      after.suppliedP=true ∧ after.suppliedQ=false ∧
      (record (initial K) (services .serveP)).certified .p ∧
      unresolved (record (initial K) (services .serveP)) .q ∧
      (record (initial K) (services .serveP)).admitted .q := by
  refine ⟨Trace.cons ⟨by decide,rfl⟩ (Trace.nil _),rfl,rfl,rfl,?_,?_,True.intro⟩
  · exact Or.inr ⟨True.intro,rfl⟩
  · refine ⟨True.intro,?_⟩
    intro h
    rcases h with impossible | ⟨_,bad⟩
    · exact impossible
    · cases bad

theorem no_funding_does_not_erase_admitted_claims :
    let K : Patient → Prop := fun _ => True
    let D : Patient → Prop := fun patient => ∃ a, serviceCost a ≤ 0 ∧ services a patient
    (∀ patient, unresolved (record (initial K) D) patient) ∧
      (∀ patient, (record (initial K) D).admitted patient) := by
  constructor
  · intro patient
    refine ⟨True.intro,?_⟩
    intro h
    rcases h with impossible | ⟨_,a,hcost,hserves⟩
    · exact impossible
    · cases a <;> simp [serviceCost,services] at hcost hserves
  · intro _
    exact True.intro

theorem missing_certificate_does_not_prove_missing_effect :
    ∃ (s : Ledger Patient) (Met : Patient → Prop),
      WellFormed s ∧ unresolved s .p ∧ Met .p := by
  exact ⟨initial (fun _ => True),fun _ => True,initial_wellFormed _,
    ⟨True.intro,id⟩,True.intro⟩

theorem prior_certificate_without_persistence_can_be_false :
    ∃ (s : Ledger Patient) (Met : Bool → Patient → Prop),
      WellFormed s ∧ (∀ c, s.certified c → Met false c) ∧
      s.certified .p ∧ ¬ Met true .p := by
  refine ⟨record (initial (fun _ => True)) (fun c => c=.p),
    fun later c => later=false ∧ c=.p,record_wellFormed (initial_wellFormed _) _,?_,
    Or.inr ⟨True.intro,rfl⟩,?_⟩
  · intro c hc
    rcases hc with impossible | ⟨_,hp⟩
    · exact False.elim impossible
    · exact ⟨rfl,hp⟩
  · intro h
    cases h.1

end ClaimLedger

#print axioms ClaimLedger.distinct_patient_keeps_claim_distinct
#print axioms ClaimLedger.distinct_episode_keeps_claim_distinct
#print axioms ClaimLedger.initial_wellFormed
#print axioms ClaimLedger.record_admitted
#print axioms ClaimLedger.record_wellFormed
#print axioms ClaimLedger.unresolved_partition
#print axioms ClaimLedger.certified_disjoint_unresolved
#print axioms ClaimLedger.record_unresolved_exact
#print axioms ClaimLedger.no_new_certificate_preserves_unresolved
#print axioms ClaimLedger.unresolved_retains_independently_admitted_reason
#print axioms ClaimLedger.recorded_certificates_sound
#print axioms ClaimLedger.recorded_sound_iff_old_sound
#print axioms ClaimLedger.traces_compose
#print axioms ClaimLedger.partial_evidence_actual_execution
#print axioms ClaimLedger.successive_execution_with_persistent_claims
#print axioms ClaimLedger.service_step_is_paid
#print axioms ClaimLedger.one_unit_cannot_deliver_both_positive_services
#print axioms ClaimLedger.paid_service_preserves_unfulfilled_claim
#print axioms ClaimLedger.no_funding_does_not_erase_admitted_claims
#print axioms ClaimLedger.missing_certificate_does_not_prove_missing_effect
#print axioms ClaimLedger.prior_certificate_without_persistence_can_be_false
