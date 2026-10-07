import OnePacketQuestions

/-!
# Admissible inquiry from the existing one-packet activity

The inherited comparison interface grants depleted probes a denial response.
Here its actual packet coordinate discharges a stronger operational contract:
a probe is admissible only while that packet remains; common controls remain
admissible. The native process, initial labels, and observations are unchanged.

The same attainable-question classification holds under this nontrivial prefix
condition. The positive witnesses derive nonemptiness and probe availability
from the represented initial configuration. This does not derive every possible
meaning of safety, install a physical policy, or establish a full apparatus
refinement. It removes the previous witness's use of the unrestricted `safe`
contract while preserving the specified comparison and its negative results.
-/

namespace Generative.InquirySufficiency.OnePacketAdmissibility

open AttainableQuestions OnePacketQuestions

/-- The represented inquiry condition is consumed by a probe; no common control
requires or replenishes it. This is a contract over the unchanged native law. -/
def packetSafe (s : State) (a : Action) (_ : State) : Prop :=
  match a with
  | .probeA => s.packet = true
  | .probeB => s.packet = true
  | .control _ => True

/-- The nonempty starting configuration is exhibited, not a new hypothesis. -/
theorem initial_is_inhabited : InhabitedBelief initial := ⟨start .A, rfl⟩

theorem exhausted_probe_forbidden (target : Target) (which : Bool) (t : State) :
    ¬ packetSafe (spent target) (test which) t := by
  cases which <;> intro h <;> exact Bool.noConfusion h

/-- The stronger contract matches successful access to a test response, not its
positive/negative answer: both answer values remain permitted. -/
theorem probe_safe_iff_not_denied (s t : State) (which : Bool) :
    packetSafe s (test which) t ↔ sense s (test which) t ≠ denied := by
  cases s with
  | mk target packet =>
    cases packet with
    | false =>
      constructor
      · intro h
        cases which <;> exact False.elim (Bool.noConfusion h)
      · intro h
        exact False.elim (h (by cases which <;> rfl))
    | true =>
      constructor
      · intro _ eq
        cases which <;> cases target <;>
          first
          | exact Nat.noConfusion (congrArg Fin.val eq)
          | exact Nat.noConfusion (Nat.succ.inj (congrArg Fin.val eq))
      · intro _
        cases which <;> rfl

/-- Every first probe is enabled and satisfies the contract for every possible
native successor, directly from the existing initial packet coordinate. -/
theorem initial_probe_admissible (which : Bool) :
    InquiryAdmissible process packetSafe initial (test which) := by
  intro s member
  refine ⟨all_actions_enabled s _, ?_⟩
  intro t _
  cases which <;> exact member

/-- Safety forgetting changes no policy, observation branch or response. -/
theorem forget_packet_safety (policy : Policy Action Unit 3) (B : State → Prop)
    (h : InquirySound process packetSafe sense policy B) :
    InquirySound process safe sense policy B := by
  induction policy generalizing B with
  | abort => exact h
  | respond r => exact h
  | inquire a next ih =>
    exact ⟨h.1, (fun s member => ⟨(h.2.1 s member).1, fun _ _ => True.intro⟩),
      fun o => ih o _ (h.2.2 o)⟩

/-- The existing positive witness needs no depleted probe. Its live branches
terminate after one admitted experiment; the denial branch is unreachable. -/
theorem one_probe_packet_sound (which : Bool) :
    InquirySound process packetSafe sense (oneProbe which) initial := by
  refine ⟨initial_is_inhabited, initial_probe_admissible which, ?_⟩
  intro ⟨i, hi⟩
  cases i with
  | zero => exact (one_probe_sound which).2.2 ⟨0, hi⟩
  | succ i =>
    cases i with
    | zero => exact (one_probe_sound which).2.2 ⟨1, hi⟩
    | succ i => exact (one_probe_sound which).2.2 ⟨i + 2, hi⟩

/-- Exact classification is unchanged when every actual inquiry prefix must
respect the packet condition. No generic safety premise occurs in this result. -/
theorem attainable_iff_packet_safe {Value : Type} (f : Target → Value) :
    Attainable process packetSafe sense (Agreement (fun s => f s.initialTarget)) initial ↔
      f .B = f .C ∨ f .A = f .C := by
  constructor
  · rintro ⟨inhabited, policy, sound, leaves⟩
    exact (attainable_iff f).mp
      ⟨inhabited, policy, forget_packet_safety policy initial sound, leaves⟩
  · intro h
    refine ⟨initial_is_inhabited, ?_⟩
    cases h with
    | inl pair =>
      exact ⟨oneProbe true, one_probe_packet_sound true,
        (one_probe_identifies f true pair).2⟩
    | inr pair =>
      exact ⟨oneProbe false, one_probe_packet_sound false,
        (one_probe_identifies f false pair).2⟩

/-- An exhausted candidate rules out any policy whose next common action is a
probe, regardless of the branch continuations that the policy proposes. -/
theorem exhausted_candidate_forbids_probe {B : State → Prop} {target : Target}
    (member : B (spent target)) (which : Bool) (next : Fin 3 → Policy Action Unit 3) :
    ¬ InquirySound process packetSafe sense (.inquire (test which) next) B := by
  intro h
  exact exhausted_probe_forbidden target which _
    ((h.2.1 (spent target) member).2 _ (spent_step target (test which)))

/-- Both different initial-target questions have actual safe finite witnesses. -/
theorem separately_packet_attainable :
    Attainable process packetSafe sense (Agreement (fun s => isA s.initialTarget)) initial ∧
    Attainable process packetSafe sense (Agreement (fun s => isB s.initialTarget)) initial :=
  ⟨(attainable_iff_packet_safe isA).mpr (Or.inl rfl),
    (attainable_iff_packet_safe isB).mpr (Or.inr rfl)⟩

/-- Impossibility persists under the stronger operational contract; forgetting
that restriction would otherwise yield the already refuted common upper. -/
theorem no_packet_attainable_common_upper :
    ¬ ∃ upper : Question State,
      Attainable process packetSafe sense upper initial ∧
      Coarser (Agreement (fun s => isA s.initialTarget)) upper ∧
      Coarser (Agreement (fun s => isB s.initialTarget)) upper := by
  rintro ⟨upper, ⟨inhabited, policy, sound, leaves⟩, first, second⟩
  exact no_attainable_common_upper
    ⟨upper, ⟨inhabited, policy, forget_packet_safety policy initial sound, leaves⟩,
      first, second⟩

end Generative.InquirySufficiency.OnePacketAdmissibility

#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.packetSafe
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.initial_is_inhabited
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.exhausted_probe_forbidden
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.probe_safe_iff_not_denied
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.initial_probe_admissible
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.forget_packet_safety
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.one_probe_packet_sound
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.attainable_iff_packet_safe
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.exhausted_candidate_forbids_probe
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.separately_packet_attainable
#print axioms Generative.InquirySufficiency.OnePacketAdmissibility.no_packet_attainable_common_upper
