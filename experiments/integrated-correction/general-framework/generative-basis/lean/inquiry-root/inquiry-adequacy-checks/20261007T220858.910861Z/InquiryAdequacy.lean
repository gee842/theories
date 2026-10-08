import Std

/-!
Inquiry relative to supplied whole-history requirements. `admissible` is an
input, not an ethical definition or a derivation of G0. The general result is
a familiar choice-per-information-class criterion. The finite examples retain
elapsed inquiry time; more informative evidence need not preserve the response
relation. No probability, scalar welfare or unlimited inquiry is assumed.
-/
namespace Generative.InquiryAdequacy

universe u v w z

def Adequate {H : Type u} {E : Type v} {A : Type w}
    (domain : H → Prop) (evidence : H → E)
    (admissible : H → A → Prop) (policy : E → A) : Prop :=
  ∀ h, domain h → admissible h (policy (evidence h))

theorem adequate_policy_iff_common_choice {H : Type u} {E : Type v} {A : Type w}
    (domain : H → Prop) (evidence : H → E) (admissible : H → A → Prop) :
    (∃ policy, Adequate domain evidence admissible policy) ↔
      ∀ e, ∃ a, ∀ h, domain h → evidence h = e → admissible h a := by
  constructor
  · rintro ⟨policy, good⟩ e
    refine ⟨policy e, ?_⟩
    intro h hd he
    rw [← he]
    exact good h hd
  · intro common
    classical
    refine ⟨fun e => Classical.choose (common e), ?_⟩
    intro h hd
    exact Classical.choose_spec (common (evidence h)) h hd rfl

theorem recoverable_evidence_preserves_adequacy
    {H : Type u} {E : Type v} {F : Type z} {A : Type w}
    {domain : H → Prop} {old : H → E} {new : H → F}
    {admissible : H → A → Prop} {policy : E → A}
    (recover : F → E) (faithful : ∀ h, domain h → recover (new h) = old h)
    (good : Adequate domain old admissible policy) :
    Adequate domain new admissible (fun e => policy (recover e)) := by
  intro h hd
  change admissible h (policy (recover (new h)))
  rw [faithful h hd]
  exact good h hd

def All (_ : Bool) : Prop := True
def Blind (_ : Bool) : Unit := ()

-- `none` represents one stipulated protective response fitting either case.
def Protective (deadline elapsed : Nat) (h : Bool) (a : Option Bool) : Prop :=
  elapsed ≤ deadline ∧ (a = none ∨ a = some h)

-- This task has only case-specific responses; the same elapsed-time law holds.
def Targeted (deadline elapsed : Nat) (h a : Bool) : Prop :=
  elapsed ≤ deadline ∧ a = h

theorem blind_target_not_identifiable :
    ¬ ∃ answer : Unit → Bool, ∀ h : Bool, answer (Blind h) = h := by
  rintro ⟨answer, correct⟩
  have clash : false = true := (correct false).symm.trans (correct true)
  cases clash

theorem protection_without_identification (deadline : Nat) :
    Adequate All Blind (Protective deadline 0) (fun _ => none) := by
  intro h _
  exact ⟨Nat.zero_le deadline, Or.inl rfl⟩

theorem blind_targeted_response_impossible (deadline elapsed : Nat) :
    ¬ ∃ policy, Adequate All Blind (Targeted deadline elapsed) policy := by
  rintro ⟨policy, good⟩
  apply blind_target_not_identifiable
  exact ⟨policy, fun h => (good h trivial).2⟩

-- A truthful probe reports h and consumes the stated elapsed time.
theorem truthful_probe_adequate_iff_timely (deadline elapsed : Nat) :
    (∃ policy, Adequate All (fun h : Bool => h)
      (Targeted deadline elapsed) policy) ↔ elapsed ≤ deadline := by
  constructor
  · rintro ⟨policy, good⟩
    exact (good false trivial).1
  · intro timely
    refine ⟨fun e => e, ?_⟩
    intro h _
    exact ⟨timely, rfl⟩

theorem late_probe_loses_even_common_protection {deadline elapsed : Nat}
    (late : deadline < elapsed) :
    ¬ ∃ policy, Adequate All (fun h : Bool => h)
      (Protective deadline elapsed) policy := by
  rintro ⟨policy, good⟩
  exact (Nat.not_le_of_lt late) (good false trivial).1

theorem probe_enables_previously_unavailable_targeted_response
    {deadline elapsed : Nat} (timely : elapsed ≤ deadline) :
    (¬ ∃ policy, Adequate All Blind (Targeted deadline 0) policy) ∧
    (∃ policy, Adequate All (fun h : Bool => h)
      (Targeted deadline elapsed) policy) := by
  exact ⟨blind_targeted_response_impossible deadline 0,
    (truthful_probe_adequate_iff_timely deadline elapsed).2 timely⟩

end Generative.InquiryAdequacy
