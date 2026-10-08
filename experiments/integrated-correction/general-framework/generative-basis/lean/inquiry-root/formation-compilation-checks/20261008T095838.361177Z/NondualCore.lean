import GenerativeCore

/-!
The existing Generative.Process is already free of primitive actor/patient
types. This module gives derived descriptions of the SAME transition system.
Readouts and history completion are mathematical constructions, not acquired
internal models or new ontological substances. Actual role feedback must be
implemented as an actual state/transition mechanism. The finite signal example
forms overlapping causal supports under a supplied non-ethical law.
-/
namespace NondualCore

open Generative
universe u v w
variable {S : Type u} {E : Type v} {D : Type w}

/-- A realized start/word/end record, not a readable list of intermediate states.
    The Trace proof can witness a nondeterministic execution in Prop. -/
structure ActualHistory (P : Process S E) where
  start : S
  word : List E
  finish : S
  actual : Trace P start word finish

def emptyHistory (P : Process S E) (s : S) : ActualHistory P :=
  ⟨s,[],s,.nil s⟩

def extendHistory {P : Process S E} (h : ActualHistory P)
    (e : E) (t : S) (step : P.step h.finish e t) : ActualHistory P :=
  ⟨h.start,h.word ++ [e],t,
    trace_append_iff.mpr ⟨h.finish,h.actual,trace_singleton_iff.mpr step⟩⟩

def historyProcess (P : Process S E) : Process (ActualHistory P) E where
  step h e k := ∃ step : P.step h.finish e k.finish,
    k = extendHistory h e k.finish step

theorem history_step_preserves {P : Process S E}
    (h k : ActualHistory P) (e : E) (hs : (historyProcess P).step h e k) :
    P.step h.finish e k.finish := hs.1

theorem history_step_lifts {P : Process S E} (h : ActualHistory P)
    (e : E) (t : S) (hs : P.step h.finish e t) :
    ∃ k, (historyProcess P).step h e k ∧ k.finish = t := by
  exact ⟨extendHistory h e t hs,⟨hs,rfl⟩,rfl⟩

theorem history_continuations_exact {P : Process S E} (h : ActualHistory P)
    (word : List E) (t : S) :
    Trace P h.finish word t ↔
      ∃ k, Trace (historyProcess P) h word k ∧ k.finish = t :=
  projected_trace_iff
    (fun h e k hs => history_step_preserves h k e hs)
    (fun h e t hs => history_step_lifts h e t hs)

/-- A coherent descriptive presentation of any state. The description is
    supplied as a readout; this construction adds no physical feedback. -/
def Presentation (describe : S → D) := {pair : S × D // pair.2 = describe pair.1}

def present (describe : S → D) (s : S) : Presentation describe :=
  ⟨(s,describe s),rfl⟩

def forget {describe : S → D} (x : Presentation describe) : S := x.val.1

theorem forget_present (describe : S → D) (s : S) :
    forget (present describe s) = s := rfl

theorem present_forget (describe : S → D) (x : Presentation describe) :
    present describe (forget x) = x := by
  rcases x with ⟨⟨s,d⟩,hd⟩
  change d = describe s at hd
  subst d
  rfl

theorem forget_injective (describe : S → D) :
    Function.Injective (@forget S D describe) := by
  intro x y heq
  exact (present_forget describe x).symm.trans
    ((congrArg (present describe) heq).trans (present_forget describe y))

def presentedProcess (P : Process S E) (describe : S → D) :
    Process (Presentation describe) E where
  step x e y := P.step (forget x) e (forget y)

theorem presented_trace_exact (P : Process S E) (describe : S → D)
    (x y : Presentation describe) (word : List E) :
    Trace (presentedProcess P describe) x word y ↔
      Trace P (forget x) word (forget y) := by
  apply trace_faithful_iff
  · exact fun _ _ _ h => h
  · intro x e t hs
    exact ⟨present describe t,hs,rfl⟩
  · exact fun _ _ h => forget_injective describe h

/-- In particular any readout of realized history can be attached without
    changing the finite continuations or creating new causal capacities. -/
theorem described_history_continuations_exact {P : Process S E}
    (describe : ActualHistory P → D) (h k : ActualHistory P) (word : List E) :
    Trace (presentedProcess (historyProcess P) describe)
      (present describe h) word (present describe k) ↔
      Trace (historyProcess P) h word k :=
  presented_trace_exact (historyProcess P) describe
    (present describe h) (present describe k) word

/-- Locus here is a queried aspect/readout, not a patient or controller. -/
def Affected {P : Process S E} {Value : Type w}
    (readout : S → Value) (h : ActualHistory P) : Prop :=
  readout h.start ≠ readout h.finish

theorem presentation_preserves_affected {P : Process S E}
    {Value : Type w} (readout : S → Value) (describe : S → D)
    (h : ActualHistory P) :
    readout (forget (present describe h.start)) ≠
      readout (forget (present describe h.finish)) ↔ Affected readout h := Iff.rfl

/- An application/generalization of GeneratedSelf's exact-summary criterion:
   the selected role/effect questions, rather than feasibility alone, determine
   which distinctions a lossless report must preserve. -/
def ExactRoleReport {H R L : Type} (report : H → R)
    (profile : H → L → Prop) (read : R → L → Prop) : Prop :=
  ∀ h l, read (report h) l ↔ profile h l

theorem exact_role_report_iff_fibers {H R L : Type}
    (report : H → R) (profile : H → L → Prop) :
    (∃ read, ExactRoleReport report profile read) ↔
      ∀ h k, report h = report k → ∀ l, profile h l ↔ profile k l := by
  constructor
  · rintro ⟨read,hexact⟩ h k heq l
    exact (hexact h l).symm.trans (heq ▸ hexact k l)
  · intro hfiber
    refine ⟨fun r l => ∃ h, report h = r ∧ profile h l,?_⟩
    intro h l
    constructor
    · rintro ⟨k,hk,hp⟩
      exact (hfiber k h hk l).mp hp
    · intro hp
      exact ⟨h,rfl,hp⟩

theorem profile_difference_forbids_report_collision {H R L : Type}
    {report : H → R} {profile : H → L → Prop} {read : R → L → Prop}
    (hexact : ExactRoleReport report profile read) (h k : H) (l : L)
    (hyes : profile h l) (hno : ¬ profile k l) : report h ≠ report k := by
  intro heq
  exact hno (((exact_role_report_iff_fibers report profile).mp ⟨read,hexact⟩ h k heq l).mp hyes)

end NondualCore

#print axioms NondualCore.history_step_preserves
#print axioms NondualCore.history_step_lifts
#print axioms NondualCore.history_continuations_exact
#print axioms NondualCore.forget_present
#print axioms NondualCore.present_forget
#print axioms NondualCore.forget_injective
#print axioms NondualCore.presented_trace_exact
#print axioms NondualCore.described_history_continuations_exact
#print axioms NondualCore.presentation_preserves_affected
#print axioms NondualCore.exact_role_report_iff_fibers
#print axioms NondualCore.profile_difference_forbids_report_collision
