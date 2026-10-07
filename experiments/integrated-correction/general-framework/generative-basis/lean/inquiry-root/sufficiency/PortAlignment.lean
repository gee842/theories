import AcquiredContact
import InquiryWarrant

/-!
# The inquiry-warrant package read on the port's own response table

The alignment modules `InquiryRelevance` and `InquiryWarrant` reason about a
two-setting Boolean response table (`Pair Bool`), a faithful test that reveals
one entry, and continuations that rely on one entry. They take every one of the
four tables as possible. This module reads those notions on the packet port,
where the table is not supplied: it is the port's transfer-response profile,
and the port's own inquiry records it.

Matched, with proofs:

* the port's table is a `Pair Bool`, and the inquiry's recorded arrivals are its
  two entries (`inquiry_reads_table`): the package's faithful test is the port's
  probe;
* the package's relevance result holds on the port's own family: one entry
  settles whether another output arrives only when it is that output
  (`port_query_sufficient_iff`);
* a transfer that relies on output `r` can be carried out adequately after a
  test exactly when the test is at `r` (`transfer_adequate_iff`).

Located mismatches, also proved:

* the package's premise that all four tables remain possible fails here: no
  contact makes both outputs arrive (`table_never_both`). The port's family has
  three tables, and in it an arrival at one output settles the whole table
  (`arrival_settles_table`), which the four-table family does not allow
  (`four_tables_leave_other_free`);
* the decision to form is not a continuation of the package's form. Every such
  continuation relies on one entry, and none acts on blockage
  (`formation_outside_continuations`). The decision needs both entries, as
  `RevisingPort.one_output_cannot_decide` shows from the port's side.

The package's own theorems are not invoked: several of them use `propext` or
`Quot.sound`, and each statement used here is proved directly with empty axiom
reports. Only its definitions are shared.
-/

namespace Generative.InquirySufficiency.PortAlignment

open Generative NativePacketProcess PacketLawDerivation AcquiredContact
open RemainingDependency InquiryRelevance InquiryWarrant

/-- The port's response table: whether each output arrives. -/
def table (tau blocked : Bool) : Pair Bool :=
  ⟨arrivalAt false tau blocked, arrivalAt true tau blocked⟩

theorem table_get (tau blocked o : Bool) : (table tau blocked).get o = arrivalAt o tau blocked := by
  cases o <;> rfl

/-- The inquiry's recorded arrivals are the table's two entries. -/
theorem inquiry_reads_table {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) :
    q.reading.arrived0 = (table s.tau s.blocked).get false ∧
      q.reading.arrived1 = (table s.tau s.blocked).get true := by
  obtain ⟨a0, a1, _⟩ := inquiry_reveals q intact
  exact ⟨a0, a1⟩

/-! ## Mismatch: three tables, not four -/

theorem table_never_both (tau blocked : Bool) : table tau blocked ≠ ⟨true, true⟩ := by
  cases tau <;> cases blocked <;> decide

/-- On the port, an arrival at one output settles every entry. -/
theorem arrival_settles_table (tau blocked q r : Bool)
    (arrived : (table tau blocked).get q = true) : (table tau blocked).get r = (r == q) := by
  rw [table_get] at arrived
  rw [table_get]
  cases tau <;> cases blocked <;> cases q <;> cases r <;>
    first | rfl | exact Bool.noConfusion arrived

/-- In the four-table family an arrival at one entry leaves the other free. -/
theorem four_tables_leave_other_free :
    (⟨false, true⟩ : Pair Bool).get true = true ∧ (⟨true, true⟩ : Pair Bool).get true = true ∧
      (⟨false, true⟩ : Pair Bool).get false ≠ (⟨true, true⟩ : Pair Bool).get false :=
  ⟨rfl, rfl, fun same => Bool.noConfusion same⟩

/-! ## Match: relevance on the port's own family -/

/-- `QuerySufficient` restricted to tables the port can have. -/
def PortQuerySufficient (r f q : Bool) : Prop :=
  ∀ tau blocked tau' blocked', (table tau blocked).get q = (table tau' blocked').get q →
    (LocalAgreement (table tau blocked) r f ↔ LocalAgreement (table tau' blocked') r f)

theorem used_output_sufficient (r f : Bool) : PortQuerySufficient r f r := by
  intro tau blocked tau' blocked' same
  unfold LocalAgreement
  rw [same]

/-- One entry settles whether output `r` arrives exactly when it is entry `r`. The
witness: a blocked contact and a contact open at `r` agree at every other output. -/
theorem port_query_sufficient_iff (r f q : Bool) : PortQuerySufficient r f q ↔ q = r := by
  constructor
  · intro sufficient
    cases q <;> cases r
    · rfl
    · have h := sufficient false true false false rfl
      unfold LocalAgreement at h
      cases f
      · exact Bool.noConfusion (h.mp rfl)
      · exact Bool.noConfusion (h.mpr rfl)
    · have h := sufficient true true true false rfl
      unfold LocalAgreement at h
      cases f
      · exact Bool.noConfusion (h.mp rfl)
      · exact Bool.noConfusion (h.mpr rfl)
    · rfl
  · intro same
    subst same
    exact used_output_sufficient q f

/-! ## Match: a transfer that relies on one output -/

/-- A transfer at output `r`, borne by the port itself: carry it out when `r`
arrives, withhold it otherwise. -/
def transferAt (r : Bool) (requirement : Nat) : Continuation :=
  { other := false, setting := r, expected := true, adequate := fun agree => agree,
    requirement := requirement }

/-- `InquiryAdequate` restricted to tables the port can have. -/
def PortInquiryAdequate (q : Bool) (c : Continuation) : Prop :=
  ∃ policy : Bool → Bool, ∀ tau blocked,
    policy ((table tau blocked).get q) = c.adequate (agrees c (table tau blocked))

theorem transfer_adequate_iff (q r : Bool) (n : Nat) :
    PortInquiryAdequate q (transferAt r n) ↔ q = r := by
  constructor
  · rintro ⟨policy, adequate⟩
    cases q <;> cases r
    · rfl
    · have blockedCase := adequate false true
      have openCase := adequate false false
      exact Bool.noConfusion (blockedCase.symm.trans openCase)
    · have blockedCase := adequate true true
      have openCase := adequate true false
      exact Bool.noConfusion (blockedCase.symm.trans openCase)
    · rfl
  · intro same
    subst same
    refine ⟨fun reading => reading, fun tau blocked => ?_⟩
    cases q <;> cases tau <;> cases blocked <;> rfl

/-! ## Mismatch: the decision to form is not a one-entry continuation -/

/-- No continuation of the package's form acts on blockage: each relies on one
entry, and a blocked contact and a contact open away from that entry agree there. -/
theorem formation_outside_continuations (c : Continuation) :
    ¬ ∀ tau blocked, c.adequate (agrees c (table tau blocked)) = blocked := by
  intro acts
  have blockedCase := acts c.setting true
  have openCase := acts c.setting false
  have same : agrees c (table c.setting true) = agrees c (table c.setting false) := by
    unfold agrees
    rw [table_get, table_get]
    cases c.setting <;> rfl
  rw [same] at blockedCase
  exact Bool.noConfusion (blockedCase.symm.trans openCase)

end Generative.InquirySufficiency.PortAlignment

#print axioms Generative.InquirySufficiency.PortAlignment.table
#print axioms Generative.InquirySufficiency.PortAlignment.table_get
#print axioms Generative.InquirySufficiency.PortAlignment.inquiry_reads_table
#print axioms Generative.InquirySufficiency.PortAlignment.table_never_both
#print axioms Generative.InquirySufficiency.PortAlignment.arrival_settles_table
#print axioms Generative.InquirySufficiency.PortAlignment.four_tables_leave_other_free
#print axioms Generative.InquirySufficiency.PortAlignment.PortQuerySufficient
#print axioms Generative.InquirySufficiency.PortAlignment.used_output_sufficient
#print axioms Generative.InquirySufficiency.PortAlignment.port_query_sufficient_iff
#print axioms Generative.InquirySufficiency.PortAlignment.transferAt
#print axioms Generative.InquirySufficiency.PortAlignment.PortInquiryAdequate
#print axioms Generative.InquirySufficiency.PortAlignment.transfer_adequate_iff
#print axioms Generative.InquirySufficiency.PortAlignment.formation_outside_continuations
