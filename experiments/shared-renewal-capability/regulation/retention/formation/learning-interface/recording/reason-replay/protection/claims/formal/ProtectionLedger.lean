import ReasonProtection
import ClaimLedger

/-!
Verification annotations for the unchanged paid ReasonProtection process.
The addressed claims and interval identifier below are logical specifications,
not newly installed runtime memory or freely observed information. A fixed
contract is preserved through the chosen history; legitimate revision of that
contract requires a separate justification and is outside this annotation.

The claim checked here is no increase in a named patient's harm counter over a
specified interval. It is not positive assistance, absence of all prior harm,
or ethical justification. Such interval claims compose by intersection, whereas
the generic ledger's monotone certificates refer to one fixed claim instance.
Ground, calibrated evidence, authority and permission remain explicit premises.
-/
namespace ProtectionLedger

open ReasonProtection

set_option maxHeartbeats 2000000
set_option maxRecDepth 8192

def harm (s : ReasonProtection.State) : Patient → Nat
  | .p => s.harmP
  | .q => s.harmQ

def NoNewHarm (s t : ReasonProtection.State) (i : Patient) : Prop :=
  harm t i = harm s i

instance (s t : ReasonProtection.State) (i : Patient) : Decidable (NoNewHarm s t i) :=
  inferInstanceAs (Decidable (harm t i = harm s i))

/-- Every actual event retains earlier recorded harm, including retraction,
turnover, refusal and observation/control obstruction. -/
theorem step_harm_monotone {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {a : Event}
    (h : ReasonProtection.Step M g truth s a t) (i : Patient) :
    harm s i ≤ harm t i := by
  rcases h with ⟨_,_,rfl⟩
  cases a <;> cases i <;> simp [harm,ReasonProtection.advance]

theorem trace_harm_monotone {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {as : List Event}
    (h : ReasonProtection.Trace M g truth s as t) (i : Patient) :
    harm s i ≤ harm t i := by
  induction h with
  | nil => exact Nat.le_refl _
  | cons hs _ ih => exact Nat.le_trans (step_harm_monotone hs i) ih

/-- Persistent protection across adjacent actual intervals requires both.
An earlier successful episode cannot discharge a later interval's protection. -/
theorem no_new_harm_compose_iff {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s u t : ReasonProtection.State}
    {as bs : List Event}
    (ha : ReasonProtection.Trace M g truth s as u)
    (hb : ReasonProtection.Trace M g truth u bs t) (i : Patient) :
    NoNewHarm s t i ↔ NoNewHarm s u i ∧ NoNewHarm u t i := by
  have h₁ := trace_harm_monotone ha i
  have h₂ := trace_harm_monotone hb i
  unfold NoNewHarm
  omega

theorem no_new_harm_three_intervals_iff {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s u v t : ReasonProtection.State}
    {as bs cs : List Event}
    (ha : ReasonProtection.Trace M g truth s as u)
    (hb : ReasonProtection.Trace M g truth u bs v)
    (hc : ReasonProtection.Trace M g truth v cs t) (i : Patient) :
    NoNewHarm s t i ↔ NoNewHarm s u i ∧ NoNewHarm u v i ∧ NoNewHarm v t i := by
  have hab : ReasonProtection.Trace M g truth s (as ++ bs) v :=
    Generative.trace_append_iff.mpr ⟨u,ha,hb⟩
  rw [no_new_harm_compose_iff hab hc i, no_new_harm_compose_iff ha hb i]
  exact and_assoc

/- This product is an erasing verification annotation. Its projections have
exactly the parent's actual events, bills and inventories. -/
structure ScopedState where
  physical : ReasonProtection.State
  addressed : Patient → Prop
  interval : Nat

def withScope (K : Patient → Prop) (interval : Nat) (s : ReasonProtection.State) : ScopedState :=
  ⟨s,K,interval⟩

def ScopedStep (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool)
    (s : ScopedState) (a : Event) (t : ScopedState) : Prop :=
  ReasonProtection.Step M g truth s.physical a t.physical ∧
  t.addressed = s.addressed ∧ t.interval = s.interval

def scopedProcess (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) :
    Generative.Process ScopedState Event := ⟨ScopedStep M g truth⟩

def ScopedTrace (M : Nat) (g : ReasonReplay.Graph) (truth : Bool → Nat → Bool) :=
  Generative.Trace (scopedProcess M g truth)

theorem actual_trace_lifts {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {as : List Event}
    (h : ReasonProtection.Trace M g truth s as t) (K : Patient → Prop) (interval : Nat) :
    ScopedTrace M g truth (withScope K interval s) as (withScope K interval t) := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons ⟨hs,rfl,rfl⟩ ih

theorem scoped_trace_projects {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ScopedState} {as : List Event}
    (h : ScopedTrace M g truth s as t) :
    ReasonProtection.Trace M g truth s.physical as t.physical := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs.1 ih

theorem scoped_trace_preserves_addressed_interval {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ScopedState} {as : List Event}
    (h : ScopedTrace M g truth s as t) :
    t.addressed = s.addressed ∧ t.interval = s.interval := by
  induction h with
  | nil => exact ⟨rfl,rfl⟩
  | cons hs _ ih => exact ⟨ih.1.trans hs.2.1,ih.2.trans hs.2.2⟩

theorem scoped_trace_preserves_actual_accounts {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ScopedState} {as : List Event}
    (h : ScopedTrace M g truth s as t) :
    energy t.physical + tally as = energy s.physical ∧
    material t.physical = material s.physical :=
  ⟨ReasonProtection.trace_energy (scoped_trace_projects h),
   ReasonProtection.trace_material (scoped_trace_projects h)⟩

/-- Only the selected admitted claims are certified. A claim outside I is
unresolved by this certificate even when another route happens to avoid harm.
The certificate is issued by this proof, not a new physical action event. -/
def actionLedger (K : Patient → Prop) (I : Mask) : ClaimLedger.Ledger Patient :=
  ClaimLedger.record (ClaimLedger.initial K) (fun i => member I i = true)

theorem action_ledger_keeps_addressed (K : Patient → Prop) (I : Mask) :
    (actionLedger K I).admitted = K := rfl

theorem action_ledger_certificate_iff (K : Patient → Prop) (I : Mask) (i : Patient) :
    (actionLedger K I).certified i ↔ K i ∧ member I i = true := by
  simp [actionLedger,ClaimLedger.record,ClaimLedger.initial]

theorem action_ledger_unresolved_iff (K : Patient → Prop) (I : Mask) (i : Patient) :
    ClaimLedger.unresolved (actionLedger K I) i ↔ K i ∧ member I i ≠ true := by
  change (K i ∧ ¬ (False ∨ (K i ∧ member I i = true))) ↔ _
  constructor
  · rintro ⟨hk,hn⟩
    exact ⟨hk,fun hm => hn (Or.inr ⟨hk,hm⟩)⟩
  · rintro ⟨hk,hn⟩
    exact ⟨hk,fun hc => hc.elim False.elim (fun hm => hn hm.2)⟩

/-- Factual/evaluative justification is not inferred from these physical facts.
This theorem supplies the inherited action's causal no-new-harm guarantee. -/
theorem paid_action_certificates_are_actual {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {G I : Mask}
    (K : Patient → Prop) (hf : Fresh M s) (hcover : Covers G I)
    (hact : ReasonProtection.Trace M g truth s (actionWord G) t) :
    (∀ i, (actionLedger K I).certified i → NoNewHarm s t i) ∧
    energy t + actionCost G = energy s := by
  have hn := protected_action_has_no_new_admitted_harm hf hcover hact
  constructor
  · intro i hi
    have hm := (action_ledger_certificate_iff K I i).mp hi
    cases i with
    | p => exact hn.1 hm.2
    | q => exact hn.2 hm.2
  · simpa only [action_cost_exact] using ReasonProtection.trace_energy hact

/-- The generic ledger trace and the actual process have exactly the same paid
step relation. This changes proof representation, never the event history. -/
theorem actual_trace_to_claim_trace {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {as : List Event}
    (h : ReasonProtection.Trace M g truth s as t) :
    ClaimLedger.Trace (ReasonProtection.Step M g truth) s as t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs ih

theorem claim_trace_to_actual_trace {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {s t : ReasonProtection.State} {as : List Event}
    (h : ClaimLedger.Trace (ReasonProtection.Step M g truth) s as t) :
    ReasonProtection.Trace M g truth s as t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs ih

/-- Direct partial-evidence instantiation on the existing paid action process.
H and its soundness are supplied; no evidence producer or ethical permission is
created here. The common harm baseline identifies this fixed interval's claim.
Execution is required for the actual state; this does not assert that the action
is runnable in every possible state, nor does it need an additional full audit. -/
theorem paid_partial_evidence_action {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {actual final : ReasonProtection.State} {G I : Mask}
    (H : ReasonProtection.State → Prop) (K : Patient → Prop)
    (Permitted : ReasonProtection.State → Mask → Prop) (baseline : Patient → Nat)
    (containsActual : H actual)
    (fresh : ∀ h, H h → Fresh M h)
    (initialHarm : ∀ h, H h → ∀ i, harm h i = baseline i)
    (authority : ∀ h, H h → Permitted h G)
    (cover : Covers G I)
    (execution : ReasonProtection.Trace M g truth actual (actionWord G) final) :
    Permitted actual G ∧
    ReasonProtection.Trace M g truth actual (actionWord G) final ∧
    (actionLedger K I).admitted = K ∧
    (∀ i, (actionLedger K I).certified i → harm final i = baseline i) ∧
    (∀ i, ClaimLedger.unresolved (actionLedger K I) i → K i) ∧
    energy final + actionCost G = energy actual := by
  have certificate : ∀ h, H h → ∀ t,
      ClaimLedger.Trace (ReasonProtection.Step M g truth) h (actionWord G) t →
      ∀ i, K i → member I i = true → harm t i = baseline i := by
    intro h hh t ht i _ hi
    have hn := protected_action_has_no_new_admitted_harm (fresh h hh) cover
      (claim_trace_to_actual_trace ht)
    have he : harm t i = harm h i := by
      cases i with
      | p => exact hn.1 hi
      | q => exact hn.2 hi
    exact he.trans (initialHarm h hh i)
  have result := ClaimLedger.partial_evidence_actual_execution H K
    (fun i => member I i = true) Permitted (fun t i => harm t i = baseline i)
    actionWord G containsActual authority (actual_trace_to_claim_trace execution)
    certificate
  exact ⟨result.1,claim_trace_to_actual_trace result.2.1,result.2.2.1,
    result.2.2.2.1,result.2.2.2.2,
    (paid_action_certificates_are_actual K (fresh actual containsActual) cover execution).2⟩

/-- This wrapper exposes, rather than supplies, the ground, calibration,
relevance and permission premises required for reasons plus actual action. -/
theorem grounded_paid_action_contract {M : Nat} {g : ReasonReplay.Graph}
    {truth : Bool → Nat → Bool} {r s t : ReasonProtection.State} {I G : Mask}
    (K : Patient → Prop)
    (hauth : ReasonReplay.Authentic truth r.core)
    (haudit : ReasonProtection.Trace M g truth r auditWord s)
    (hpub : s.core.installed = some (r.core.context,I))
    (hf : Fresh M s) (hcover : Covers G I)
    (hact : ReasonProtection.Trace M g truth s (actionWord G) t)
    (Fact : Nat → Prop) (Reason : ReasonReplay.Node → Prop) (anchor : Reason .root)
    (calibrated : ∀ i, i < 3 → truth r.core.context i = true → Fact i)
    (relevant : ∀ i, i < 3 → Fact i → Reason (ReasonReplay.endpoints g i).1 → Reason (ReasonReplay.endpoints g i).2)
    (Permissible : Mask → Prop) (permission : Permissible G) :
    Permissible G ∧
    (∀ i, (actionLedger K I).certified i → Reason (patientNode i) ∧ NoNewHarm s t i) ∧
    (actionLedger K I).admitted = K ∧
    energy t + (11 + actionCost G) = energy r := by
  have hr := reached_reason_and_protection hauth haudit hpub hf hcover hact
    Fact Reason anchor calibrated relevant Permissible permission
  refine ⟨hr.1,?_,rfl,?_⟩
  · intro i hi
    have hm := (action_ledger_certificate_iff K I i).mp hi
    cases i with
    | p => exact hr.2.1 hm.2
    | q => exact hr.2.2 hm.2
  · have he₁ := ReasonProtection.trace_energy haudit
    have he₂ := (paid_action_certificates_are_actual K hf hcover hact).2
    rw [audit_tally] at he₁
    omega

def addressedBoth : Patient → Prop := fun _ => True
def revisedLedger := actionLedger addressedBoth qOnly

/-- This is an actual paid published-action history, not an arbitrary state
chosen because it carries a desired publication. Both addressed patients remain. -/
theorem actual_revised_action_and_ledger :
    ScopedTrace 17 primary truth (withScope addressedBoth 1 secondPublished)
      (actionWord qOnly) (withScope addressedBoth 1 secondFinal) ∧
    secondPublished.core.installed = some (true,qOnly) ∧
    (revisedLedger.certified .q) ∧ ClaimLedger.unresolved revisedLedger .p ∧
    secondFinal.harmP = 1 ∧ secondFinal.harmQ = 0 ∧
    energy secondFinal + 3 = energy secondPublished := by
  refine ⟨actual_trace_lifts actual_revised_action addressedBoth 1,by decide,?_,?_,
    by decide,by decide,?_⟩
  · exact (action_ledger_certificate_iff addressedBoth qOnly .q).mpr ⟨trivial,rfl⟩
  · exact (action_ledger_unresolved_iff addressedBoth qOnly .p).mpr ⟨trivial,by decide⟩
  · simpa [actionCost,card,qOnly,empty,FormedSelection.bit] using
      (paid_action_certificates_are_actual addressedBoth (by decide)
        (covers_self qOnly) actual_revised_action).2

def afterFirst := secondBeforeAuditEvents ++ auditWord ++ actionWord qOnly

theorem actual_second_interval :
    ReasonProtection.Trace 17 primary truth firstFinal afterFirst secondFinal := by
  have h := ReasonProtection.runnable_trace
    (M := 17) (g := primary) (truth := truth) (s := firstFinal)
    (as := afterFirst) (by decide)
  simpa only [afterFirst,ReasonProtection.run_append,secondBeforeAudit,
    secondPublished,secondFinal] using h

/-- The first p certificate cannot be recycled for the longer horizon.
The old and later harm counts are physical parent outputs. -/
theorem actual_protection_intersects_across_horizons :
    NoNewHarm firstPublished firstFinal .p ∧
    NoNewHarm firstPublished firstFinal .q ∧
    ¬ NoNewHarm firstFinal secondFinal .p ∧
    NoNewHarm firstFinal secondFinal .q ∧
    ¬ NoNewHarm firstPublished secondFinal .p ∧
    NoNewHarm firstPublished secondFinal .q := by
  decide

def obstructedWord : List Event := [.arm full,.core (.setDelivery false),.release]

theorem actual_obstructed_interval :
    ReasonProtection.Trace 17 primary truth firstPublished obstructedWord unsafeReleased := by
  have h := actual_delivery_cut_preserves_reasons_but_allows_harm
  exact .cons h.1 (.cons h.2.1 (.cons h.2.2.1 (.nil _)))

/-- Obstruction changes realizable control, not the reason publication or
addressed scope. Paid release still records both patients' actual harm. -/
theorem obstruction_preserves_claims_and_costs :
    ScopedTrace 17 primary truth (withScope addressedBoth 2 firstPublished)
      obstructedWord (withScope addressedBoth 2 unsafeReleased) ∧
    deliveryCut.core.installed = firstPublished.core.installed ∧
    unsafeReleased.harmP = 1 ∧ unsafeReleased.harmQ = 1 ∧
    energy unsafeReleased + 2 = energy firstPublished ∧
    ¬ NoNewHarm firstPublished unsafeReleased .p ∧
    ¬ NoNewHarm firstPublished unsafeReleased .q := by
  refine ⟨actual_trace_lifts actual_obstructed_interval addressedBoth 2,
    by decide,by decide,by decide,?_,by decide,by decide⟩
  simpa [obstructedWord,tally,spending] using
    ReasonProtection.trace_energy actual_obstructed_interval

/-- The missing certificate need not signify actual harm: an allowed withdrawal
has no release, no added harm, and no certification of the selected q action. -/
theorem withdrawal_can_leave_uncertified_claim_without_harm :
    ReasonProtection.Trace 17 primary truth freshFinal [.withdraw]
      (advance primary freshFinal .withdraw) ∧
    ClaimLedger.unresolved (ClaimLedger.initial addressedBoth) .q ∧
    NoNewHarm freshFinal (advance primary freshFinal .withdraw) .q ∧
    energy (advance primary freshFinal .withdraw) = energy freshFinal := by
  have hf := reasons_remain_when_next_audit_unfunded.2.2.2.1
  have hs : ReasonProtection.Step 17 primary truth freshFinal .withdraw
      (advance primary freshFinal .withdraw) :=
    ⟨hf.1,⟨hf.2.2.1,hf.2.2.2.1⟩,rfl⟩
  refine ⟨.cons hs (.nil _),?_,rfl,rfl⟩
  simp [ClaimLedger.unresolved,ClaimLedger.initial,addressedBoth]

/-- Lack of the eleven-unit audit does not refute the retained publication and
does not prove all protective or withdrawing actions impossible. -/
theorem low_funds_preserve_reason_and_allow_withdrawal :
    freshFinal.core.installed = some (true,qOnly) ∧
    freshFinal.core.record.plant.fuel = 3 ∧ freshFinal.core.record.plant.source = 18 ∧
    (¬ ∃ t, ReasonProtection.Trace 17 primary truth freshFinal auditWord t) ∧
    Enabled truth freshFinal .withdraw := by
  have h := reasons_remain_when_next_audit_unfunded
  exact ⟨h.1,h.2.1,h.2.2.1,h.2.2.2.2.2.2.2.2,by decide⟩

/-- This imported counterexample prevents treating a prescribed armed-word
price as the minimum cost of every way to protect the patient. -/
theorem actual_voluntary_route_remains_available :
    ReasonProtection.Trace 17 primary truth voluntaryStart voluntaryWord voluntaryFinal ∧
    voluntaryStart.core.record.plant.fuel = 13 ∧
    NoNewHarm voluntaryStart voluntaryFinal .q ∧
    (¬ ∃ t, ReasonProtection.Trace 17 primary truth voluntaryStart
      (auditWord ++ actionWord qOnly) t) := by
  have h := voluntary_protection_is_strictly_cheaper_than_armed_word
  refine ⟨h.1,h.2.1,by decide,?_⟩
  exact h.2.2.2.2.2.2.2.2.2.2

end ProtectionLedger

#print axioms ProtectionLedger.step_harm_monotone
#print axioms ProtectionLedger.trace_harm_monotone
#print axioms ProtectionLedger.no_new_harm_compose_iff
#print axioms ProtectionLedger.no_new_harm_three_intervals_iff
#print axioms ProtectionLedger.actual_trace_lifts
#print axioms ProtectionLedger.scoped_trace_projects
#print axioms ProtectionLedger.scoped_trace_preserves_addressed_interval
#print axioms ProtectionLedger.scoped_trace_preserves_actual_accounts
#print axioms ProtectionLedger.action_ledger_keeps_addressed
#print axioms ProtectionLedger.action_ledger_certificate_iff
#print axioms ProtectionLedger.action_ledger_unresolved_iff
#print axioms ProtectionLedger.paid_action_certificates_are_actual
#print axioms ProtectionLedger.grounded_paid_action_contract
#print axioms ProtectionLedger.actual_revised_action_and_ledger
#print axioms ProtectionLedger.actual_second_interval
#print axioms ProtectionLedger.actual_protection_intersects_across_horizons
#print axioms ProtectionLedger.actual_obstructed_interval
#print axioms ProtectionLedger.obstruction_preserves_claims_and_costs
#print axioms ProtectionLedger.withdrawal_can_leave_uncertified_claim_without_harm
#print axioms ProtectionLedger.low_funds_preserve_reason_and_allow_withdrawal
#print axioms ProtectionLedger.actual_voluntary_route_remains_available

#print axioms ProtectionLedger.actual_trace_to_claim_trace
#print axioms ProtectionLedger.claim_trace_to_actual_trace
#print axioms ProtectionLedger.paid_partial_evidence_action
