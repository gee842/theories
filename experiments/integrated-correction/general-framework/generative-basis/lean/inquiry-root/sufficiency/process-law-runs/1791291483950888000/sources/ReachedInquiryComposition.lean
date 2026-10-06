import AttainableQuestions

/-!
# Composition at reached leaves without global agreement preservation

The inherited composition theorem gave a sufficient global retention condition.
Here the actual continuations are characterized exactly. The prefix need not
already answer either question, and events absent from its realized histories
need not preserve either answer. This removes excessive hypotheses, while
retaining the necessary native execution and terminal-information obligations.

The final finite witness uses a nontrivial admissibility condition: alteration
is excluded, and the admitted observation event retains the original readout.
Its historical target is proved unchanged along every admitted trace. Failure
of global preservation concerns the unselected alteration event, not a silent
substitution of a different historical target.
-/

namespace Generative.InquirySufficiency.ReachedInquiryComposition

open AttainableQuestions

universe u v

section General

variable {State : Type u} {Action : Type v} {observations : Nat}
variable (P : Process State Action)
variable (safe : State → Action → State → Prop)
variable (sense : State → Action → State → Fin observations)

/-- A sound non-abort policy already entails a nonempty starting possibility.
Thus a separate `live` input duplicates information for such a policy. -/
theorem sound_live_iff_nonabort (policy : Policy Action Unit observations)
    (B : State → Prop) (sound : InquirySound P safe sense policy B) :
    InhabitedBelief B ↔ policy ≠ .abort := by
  cases policy with
  | abort =>
    constructor
    · rintro ⟨s, hs⟩
      exact False.elim (sound s hs)
    · intro impossible
      exact False.elim (impossible rfl)
  | respond r =>
    constructor
    · intro _ impossible
      cases impossible
    · intro _
      exact sound.1
  | inquire a next =>
    constructor
    · intro _ impossible
      cases impossible
    · intro _
      exact sound.1

/-- Exact replacement of the separate nonemptiness witness by the executable
policy's non-abort shape. It does not assert that any such policy exists. -/
theorem attainable_iff_nonabort_policy (question : Question State) (B : State → Prop) :
    Attainable P safe sense question B ↔
      ∃ policy, policy ≠ .abort ∧ Identifies P safe sense question policy B := by
  constructor
  · rintro ⟨live, policy, identified⟩
    exact ⟨policy, (sound_live_iff_nonabort P safe sense policy B identified.1).mp live,
      identified⟩
  · rintro ⟨policy, active, identified⟩
    exact ⟨(sound_live_iff_nonabort P safe sense policy B identified.1).mpr active,
      policy, identified⟩

/-- Every continuation of a sound identifying composite is itself sound and
identifying at the exact belief reached by the prefix. -/
theorem continuations_of_identified_composite (question : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop)
    (identified : Identifies P safe sense question
      (continueAtLeaves policy continuations) B) :
    ContinuationsIdentify P safe sense question policy continuations B := by
  induction policy generalizing B with
  | abort => exact True.intro
  | respond r => exact identified
  | inquire a next ih =>
    exact fun o => ih o (continuations o) _ ⟨identified.1.2.2 o, identified.2 o⟩

/-- Necessary and sufficient reached-leaf criterion. Only prefix executability
is retained; neither global answer preservation nor an already answered prefix
is required. The leaf obligation is derived to be exact, not declared absent. -/
theorem continued_identifies_iff (question : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : InquirySound P safe sense policy B) :
    Identifies P safe sense question (continueAtLeaves policy continuations) B ↔
      ContinuationsIdentify P safe sense question policy continuations B := by
  constructor
  · exact continuations_of_identified_composite P safe sense question policy continuations B
  · intro later
    exact ⟨continueAtLeaves_sound P safe sense question policy continuations B first later,
      continueAtLeaves_refines_later P safe sense question policy continuations B later⟩

/-- The same reached continuation answers a join exactly when it answers each
component. This is not an inference from separately realizable continuations. -/
theorem continuations_join_iff (left right : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) :
    ContinuationsIdentify P safe sense (Join left right) policy continuations B ↔
      ContinuationsIdentify P safe sense left policy continuations B ∧
        ContinuationsIdentify P safe sense right policy continuations B := by
  induction policy generalizing B with
  | abort => exact ⟨fun _ => ⟨True.intro, True.intro⟩, fun _ => True.intro⟩
  | respond r => exact shared_policy_join_iff P safe sense left right continuations B
  | inquire a next ih =>
    constructor
    · intro both
      exact ⟨fun o => ((ih o (continuations o) _).mp (both o)).1,
        fun o => ((ih o (continuations o) _).mp (both o)).2⟩
    · intro each
      exact fun o => (ih o (continuations o) _).mpr ⟨each.1 o, each.2 o⟩

/-- Exact joint inquiry criterion with no global preservation premise and no
prefix answer certificate. Native conditions and final distinctions are checked
where they participate in the continuing inquiry. -/
theorem continued_join_iff (left right : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : InquirySound P safe sense policy B) :
    Identifies P safe sense (Join left right) (continueAtLeaves policy continuations) B ↔
      ContinuationsIdentify P safe sense left policy continuations B ∧
        ContinuationsIdentify P safe sense right policy continuations B :=
  (continued_identifies_iff P safe sense (Join left right) policy continuations B first).trans
    (continuations_join_iff P safe sense left right policy continuations B)

/-- General single-target form for a synthesized continuation certificate.
The initial nonemptiness is extracted from the existing prefix contract. -/
theorem attainable_from_reached_continuation (question : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (active : policy ≠ .abort)
    (first : InquirySound P safe sense policy B)
    (later : ContinuationsIdentify P safe sense question policy continuations B) :
    Attainable P safe sense question B :=
  ⟨(sound_live_iff_nonabort P safe sense policy B first).mpr active,
    continueAtLeaves policy continuations,
    (continued_identifies_iff P safe sense question policy continuations B first).mpr later⟩

/-- A non-abort sound prefix discharges the duplicate starting-live input. The
continuations themselves supply the final joint distinction at reached leaves. -/
theorem attainable_from_reached_continuations (left right : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (active : policy ≠ .abort)
    (first : InquirySound P safe sense policy B)
    (leftLater : ContinuationsIdentify P safe sense left policy continuations B)
    (rightLater : ContinuationsIdentify P safe sense right policy continuations B) :
    Attainable P safe sense (Join left right) B :=
  ⟨(sound_live_iff_nonabort P safe sense policy B first).mpr active,
    continueAtLeaves policy continuations,
    (continued_join_iff P safe sense left right policy continuations B first).mpr
      ⟨leftLater, rightLater⟩⟩

end General

namespace Witness

/-- `false` observes without changing the readout; `true` permits alteration.
This is a finite counterexample to a globally quantified retention requirement,
not an origin law proposed for all generative activity. -/
def zero : Fin 2 := ⟨0, Nat.zero_lt_succ 1⟩

def one : Fin 2 := ⟨1, Nat.lt_succ_self 1⟩

def process : Process (Fin 2) Bool where
  step s a t := match a with
    | false => t = s
    | true => True

/-- Only the observation event belongs to this inquiry's admitted history. -/
def safe (_ : Fin 2) (a : Bool) (_ : Fin 2) : Prop := a = false

def sense (_ : Fin 2) (_ : Bool) (t : Fin 2) : Fin 2 := t

def initial (_ : Fin 2) : Prop := True

def question : Question (Fin 2) := Agreement (fun s => s)

def startPolicy : Policy Bool Unit 2 := .respond ()

def observe : Policy Bool Unit 2 := .inquire false (fun _ => .respond ())

theorem prefix_sound : InquirySound process safe sense startPolicy initial :=
  ⟨⟨zero, True.intro⟩, fun _ _ => True.intro⟩

/-- The prefix has not yet acquired the readout distinction. -/
theorem prefix_does_not_identify : ¬ Identifies process safe sense question startPolicy initial := by
  intro identified
  have impossible : zero = one := identified.2 zero one True.intro True.intro
  exact Nat.noConfusion (congrArg Fin.val impossible)

/-- Observation forms the needed distinction under the actual native law. -/
theorem observe_identifies : Identifies process safe sense question observe initial := by
  constructor
  · refine ⟨⟨zero, True.intro⟩, ?_, ?_⟩
    · intro s _
      exact ⟨⟨s, rfl⟩, fun _ _ => rfl⟩
    · intro o
      exact ⟨⟨o, o, True.intro, rfl, rfl⟩, fun _ _ => True.intro⟩
  · intro o s t hs ht
    rcases hs with ⟨_, _, _, left⟩
    rcases ht with ⟨_, _, _, right⟩
    exact left.trans right.symm

/-- The global condition fails for an alteration event outside the certified
inquiry. Thus its removal strictly enlarges the theorem's application scope. -/
theorem global_preservation_fails : ¬ PreservesAgreement process question := by
  intro preserved
  have impossible : zero = one :=
    preserved zero zero true zero one rfl True.intro True.intro
  exact Nat.noConfusion (congrArg Fin.val impossible)

/-- Every admitted actual event keeps the original readout, rather than merely
replacing an earlier question by one about a changed current value. -/
theorem admitted_step_retains_original {s t : Fin 2} {a : Bool}
    (step : process.step s a t) (condition : safe s a t) : t = s := by
  cases a with
  | false => exact step
  | true => exact Bool.noConfusion condition

theorem every_admitted_trace_retains_original {s t : Fin 2} {word : List Bool}
    (actual : SafeTrace process safe s word t) : t = s := by
  induction actual with
  | nil => rfl
  | cons step condition tail ih =>
    exact ih.trans (admitted_step_retains_original step condition)

/-- A concrete completed inquiry discharges all its application premises.
It needs neither global preservation nor prior acquisition of the answer. -/
theorem attained_without_global_preservation :
    Attainable process safe sense question initial := by
  exact attainable_from_reached_continuation process safe sense question
    startPolicy observe initial (by intro impossible; cases impossible)
    prefix_sound observe_identifies

end Witness
end Generative.InquirySufficiency.ReachedInquiryComposition

#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.sound_live_iff_nonabort
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.attainable_iff_nonabort_policy
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.continuations_of_identified_composite
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.continued_identifies_iff
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.continuations_join_iff
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.continued_join_iff
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.attainable_from_reached_continuation
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.attainable_from_reached_continuations
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.zero
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.one
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.process
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.safe
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.sense
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.initial
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.question
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.startPolicy
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.observe
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.prefix_sound
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.prefix_does_not_identify
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.observe_identifies
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.global_preservation_fails
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.admitted_step_retains_original
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.every_admitted_trace_retains_original
#print axioms Generative.InquirySufficiency.ReachedInquiryComposition.Witness.attained_without_global_preservation
