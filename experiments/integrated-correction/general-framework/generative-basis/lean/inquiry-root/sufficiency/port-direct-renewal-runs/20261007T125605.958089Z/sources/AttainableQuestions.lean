import InquirySufficiency

/-!
# Questions acquired through one continuing inquiry

Reuse the existing finite `Policy` syntax, native `After` successor transport
and `Sound` progress/safety contract. A terminal `respond ()` ends an
informational inquiry; its complete observation-path distinguishes its leaf.
Leaf homogeneity certifies a logical answer, not an installed reporting action
or cost-free physical memory. Concrete reporting/retention needs its own law.

A question is represented by an agreement relation; actual answer functions
induce such relations through `Agreement`. The theorems need no stronger
partition axioms. A question about initial identity must read a retained target
coordinate, not silently switch to the changed current configuration. Generic
continuation preserves agreement within a leaf; its initial-key specialization
also requires the native law to preserve each key's value.

Downward closure and pairing at a shared leaf follow from the actual policy
semantics. Separately attainable questions are not combined. Sequential
composition needs sound continuations at the first policy's actual reached
leaves; it does not assume a reset restores consumed access or support.
-/

namespace Generative.InquirySufficiency.AttainableQuestions

universe u v w x

abbrev Question (State : Type u) := State → State → Prop

def Agreement {State : Type u} {Answer : Type w} (answer : State → Answer) :
    Question State := fun s t => answer s = answer t

/-- `coarse` requires no distinction beyond `fine`. -/
def Coarser {State : Type u} (coarse fine : Question State) : Prop :=
  ∀ s t, fine s t → coarse s t

def Join {State : Type u} (left right : Question State) : Question State :=
  fun s t => left s t ∧ right s t

def FamilyJoin {State : Type u} {Index : Type w}
    (questions : Index → Question State) : Question State :=
  fun s t => ∀ i, questions i s t

def Homogeneous {State : Type u} (question : Question State) (B : State → Prop) : Prop :=
  ∀ s t, B s → B t → question s t

variable {State : Type u} {Action : Type v} {observations : Nat}
variable (P : Process State Action)
variable (safe : State → Action → State → Prop)
variable (sense : State → Action → State → Fin observations)

abbrev InquirySound (policy : Policy Action Unit observations) (B : State → Prop) : Prop :=
  Sound P safe (fun _ => True) sense (fun _ : Unit => []) policy B

def RefinesLeaves (question : Question State) :
    Policy Action Unit observations → (State → Prop) → Prop
  | .abort, _ => True
  | .respond _, B => Homogeneous question B
  | .inquire a next, B =>
      ∀ o, RefinesLeaves question (next o) (After P sense B a o)

def Identifies (question : Question State) (policy : Policy Action Unit observations)
    (B : State → Prop) : Prop :=
  InquirySound P safe sense policy B ∧ RefinesLeaves P sense question policy B

def Attainable (question : Question State) (B : State → Prop) : Prop :=
  InhabitedBelief B ∧ ∃ policy, Identifies P safe sense question policy B

def IsGreatest (B : State → Prop) (greatest : Question State) : Prop :=
  Attainable P safe sense greatest B ∧
    ∀ question, Attainable P safe sense question B → Coarser question greatest

/-- Every execution of a certified inquiry follows the native law and keeps
the supplied prefix condition. This is a conditional execution guarantee, not
a claim that a physical scheduler selects or realizes the policy. -/
theorem identifies_every_actual_execution_safe {question : Question State}
    {policy : Policy Action Unit observations} {B : State → Prop}
    {s t : State} {word : List Action}
    (identified : Identifies P safe sense question policy B) (member : B s)
    (actual : Execution P sense (fun _ : Unit => []) policy s word t) :
    Trace P s word t ∧ SafeTrace P safe s word t :=
  ⟨execution_is_actual_trace actual,
    sound_execution_preserves_every_prefix_condition identified.1 member actual⟩

/-- Native progress in `Sound` supplies at least one complete execution from
each possible initial state; every possible execution is safe by the preceding
theorem. No favorable endpoint is substituted for inadmissible alternatives. -/
theorem identifies_has_actual_execution {question : Question State}
    {policy : Policy Action Unit observations} {B : State → Prop} {s : State}
    (identified : Identifies P safe sense question policy B) (member : B s) :
    ∃ word t, Execution P sense (fun _ : Unit => []) policy s word t ∧
      Trace P s word t ∧ SafeTrace P safe s word t := by
  obtain ⟨word, t, actual, _⟩ := sound_has_actual_execution identified.1 member
  exact ⟨word, t, actual,
    identifies_every_actual_execution_safe P safe sense identified member actual⟩

theorem coarser_refl (question : Question State) : Coarser question question :=
  fun _ _ same => same

theorem coarser_trans {first second third : Question State}
    (one : Coarser first second) (two : Coarser second third) : Coarser first third :=
  fun s t same => one s t (two s t same)

theorem join_projects_left (left right : Question State) : Coarser left (Join left right) :=
  fun _ _ same => same.1

theorem join_projects_right (left right : Question State) : Coarser right (Join left right) :=
  fun _ _ same => same.2

theorem join_least {left right upper : Question State}
    (one : Coarser left upper) (two : Coarser right upper) :
    Coarser (Join left right) upper :=
  fun s t same => ⟨one s t same, two s t same⟩

theorem agreement_pair_iff {First : Type w} {Second : Type x}
    (first : State → First) (second : State → Second) (s t : State) :
    Join (Agreement first) (Agreement second) s t ↔
      Agreement (fun x => (first x, second x)) s t := by
  constructor
  · intro same
    exact Prod.ext same.1 same.2
  · intro same
    exact ⟨congrArg Prod.fst same, congrArg Prod.snd same⟩

theorem answer_projection_coarser {First : Type w} {Second : Type x}
    (answer : State → First) (projection : First → Second) :
    Coarser (Agreement (fun s => projection (answer s))) (Agreement answer) :=
  fun _ _ same => congrArg projection same

theorem refines_coarser {coarse fine : Question State}
    (coarsens : Coarser coarse fine) (policy : Policy Action Unit observations)
    (B : State → Prop) (h : RefinesLeaves P sense fine policy B) :
    RefinesLeaves P sense coarse policy B := by
  induction policy generalizing B with
  | abort => exact True.intro
  | respond answer => exact fun s t hs ht => coarsens s t (h s t hs ht)
  | inquire a next ih => exact fun o => ih o _ (h o)

theorem identifies_coarser {coarse fine : Question State}
    (coarsens : Coarser coarse fine) {policy : Policy Action Unit observations}
    {B : State → Prop} (h : Identifies P safe sense fine policy B) :
    Identifies P safe sense coarse policy B :=
  ⟨h.1, refines_coarser P sense coarsens policy B h.2⟩

theorem attainable_downward {coarse fine : Question State}
    (coarsens : Coarser coarse fine) {B : State → Prop}
    (h : Attainable P safe sense fine B) : Attainable P safe sense coarse B := by
  obtain ⟨live, policy, identified⟩ := h
  exact ⟨live, policy, identifies_coarser P safe sense coarsens identified⟩

theorem refines_join_iff (left right : Question State)
    (policy : Policy Action Unit observations) (B : State → Prop) :
    RefinesLeaves P sense (Join left right) policy B ↔
      RefinesLeaves P sense left policy B ∧ RefinesLeaves P sense right policy B := by
  induction policy generalizing B with
  | abort => exact ⟨fun _ => ⟨True.intro, True.intro⟩, fun _ => True.intro⟩
  | respond answer =>
    constructor
    · intro h
      exact ⟨fun s t hs ht => (h s t hs ht).1, fun s t hs ht => (h s t hs ht).2⟩
    · intro h
      exact fun s t hs ht => ⟨h.1 s t hs ht, h.2 s t hs ht⟩
  | inquire a next ih =>
    constructor
    · intro h
      exact ⟨fun o => ((ih o _).mp (h o)).1, fun o => ((ih o _).mp (h o)).2⟩
    · intro h
      exact fun o => (ih o _).mpr ⟨h.1 o, h.2 o⟩

/-- Both certificates concern the same observation-contingent inquiry tree. -/
theorem shared_policy_join_iff (left right : Question State)
    (policy : Policy Action Unit observations) (B : State → Prop) :
    Identifies P safe sense (Join left right) policy B ↔
      Identifies P safe sense left policy B ∧ Identifies P safe sense right policy B := by
  constructor
  · intro h
    have parts := (refines_join_iff P sense left right policy B).mp h.2
    exact ⟨⟨h.1, parts.1⟩, ⟨h.1, parts.2⟩⟩
  · intro h
    exact ⟨h.1.1, (refines_join_iff P sense left right policy B).mpr ⟨h.1.2, h.2.2⟩⟩

theorem attainable_join_iff_shared_policy (left right : Question State) (B : State → Prop) :
    Attainable P safe sense (Join left right) B ↔
      InhabitedBelief B ∧ ∃ policy,
        Identifies P safe sense left policy B ∧ Identifies P safe sense right policy B := by
  constructor
  · rintro ⟨live, policy, identified⟩
    exact ⟨live, policy, (shared_policy_join_iff P safe sense left right policy B).mp identified⟩
  · rintro ⟨live, policy, both⟩
    exact ⟨live, policy, (shared_policy_join_iff P safe sense left right policy B).mpr both⟩

theorem refines_family_iff {Index : Type w} (questions : Index → Question State)
    (policy : Policy Action Unit observations) (B : State → Prop) :
    RefinesLeaves P sense (FamilyJoin questions) policy B ↔
      ∀ i, RefinesLeaves P sense (questions i) policy B := by
  induction policy generalizing B with
  | abort => exact ⟨fun _ _ => True.intro, fun _ => True.intro⟩
  | respond answer =>
    exact ⟨fun h i s t hs ht => h s t hs ht i, fun h s t hs ht i => h i s t hs ht⟩
  | inquire a next ih =>
    constructor
    · intro h i o
      exact (ih o _).mp (h o) i
    · intro h o
      exact (ih o _).mpr (fun i => h i o)

/-- One preparation supports every later question exactly when all its reached
terminal fibers refine their joint question. No later encounter is inserted. -/
theorem family_shared_policy_iff {Index : Type w} (questions : Index → Question State)
    (policy : Policy Action Unit observations) (B : State → Prop) :
    Identifies P safe sense (FamilyJoin questions) policy B ↔
      InquirySound P safe sense policy B ∧
        ∀ i, RefinesLeaves P sense (questions i) policy B := by
  exact ⟨fun h => ⟨h.1, (refines_family_iff P sense questions policy B).mp h.2⟩,
    fun h => ⟨h.1, (refines_family_iff P sense questions policy B).mpr h.2⟩⟩

theorem missing_join_no_greatest {left right : Question State} {B : State → Prop}
    (one : Attainable P safe sense left B) (two : Attainable P safe sense right B)
    (missing : ¬ Attainable P safe sense (Join left right) B) :
    ¬ ∃ greatest, IsGreatest P safe sense B greatest := by
  rintro ⟨greatest, achieved, upper⟩
  exact missing (attainable_downward P safe sense
    (join_least (upper left one) (upper right two)) achieved)

/-- The obstruction also excludes a greatest question inside any permitted
question family containing both questions: no attainable common upper exists.
It does not depend on quantifying over every binary relation on states. -/
theorem missing_join_no_attainable_common_upper {left right : Question State}
    {B : State → Prop} (missing : ¬ Attainable P safe sense (Join left right) B) :
    ¬ ∃ upper, Attainable P safe sense upper B ∧
      Coarser left upper ∧ Coarser right upper := by
  rintro ⟨upper, achieved, one, two⟩
  exact missing (attainable_downward P safe sense (join_least one two) achieved)

/-- Agreement survives a common native event, including every pair of its
possible successors. This preserves homogeneity, not an earlier answer's value:
a constant reset may satisfy it. The initial-key specialization below uses
actual key invariance for the stronger historical-target interpretation. -/
def PreservesAgreement (question : Question State) : Prop :=
  ∀ s t a s' t', question s t → P.step s a s' → P.step t a t' → question s' t'

theorem agreement_preserved_of_key_preserved {Answer : Type w}
    (key : State → Answer)
    (preserved : ∀ s a t, P.step s a t → key t = key s) :
    PreservesAgreement P (Agreement key) :=
  fun s t a s' t' same first second =>
    (preserved s a s' first).trans (same.trans (preserved t a t' second).symm)

theorem homogeneous_after {question : Question State}
    (preserved : PreservesAgreement P question) {B : State → Prop}
    (same : Homogeneous question B) (a : Action) (o : Fin observations) :
    Homogeneous question (After P sense B a o) := by
  rintro s' t' ⟨s, hs, first, _⟩ ⟨t, ht, second, _⟩
  exact preserved s t a s' t' (same s t hs ht) first second

theorem homogeneous_refines_every_continuation {question : Question State}
    (preserved : PreservesAgreement P question) (policy : Policy Action Unit observations)
    (B : State → Prop) (same : Homogeneous question B) :
    RefinesLeaves P sense question policy B := by
  induction policy generalizing B with
  | abort => exact True.intro
  | respond answer => exact same
  | inquire a next ih =>
    exact fun o => ih o _ (homogeneous_after P sense preserved same a o)

/-- One separately chosen finite continuation for each syntactic terminal leaf.
This is not a single continuation chosen at the original initial belief. -/
def LeafContinuations : Policy Action Unit observations → Type v
  | .abort => PUnit
  | .respond _ => Policy Action Unit observations
  | .inquire _ next => (o : Fin observations) → LeafContinuations (next o)

def continueAtLeaves (policy : Policy Action Unit observations)
    (continuations : LeafContinuations policy) : Policy Action Unit observations :=
  match policy with
  | .abort => .abort
  | .respond _ => continuations
  | .inquire a next => .inquire a (fun o => continueAtLeaves (next o) (continuations o))

/-- Each attached continuation is certified at the first inquiry's actual
successor belief. Its native safety, progress and all outcomes are retained. -/
def ContinuationsIdentify (question : Question State) :
    (policy : Policy Action Unit observations) → LeafContinuations policy → (State → Prop) → Prop
  | .abort, _, _ => True
  | .respond _, continuation, B => Identifies P safe sense question continuation B
  | .inquire a next, continuations, B =>
      ∀ o, ContinuationsIdentify question (next o) (continuations o) (After P sense B a o)

theorem continueAtLeaves_sound (question : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : InquirySound P safe sense policy B)
    (later : ContinuationsIdentify P safe sense question policy continuations B) :
    InquirySound P safe sense (continueAtLeaves policy continuations) B := by
  induction policy generalizing B with
  | abort => exact first
  | respond answer => exact later.1
  | inquire a next ih =>
    exact ⟨first.1, first.2.1, fun o => ih o (continuations o) _ (first.2.2 o) (later o)⟩

theorem continueAtLeaves_refines_later (question : Question State)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop)
    (later : ContinuationsIdentify P safe sense question policy continuations B) :
    RefinesLeaves P sense question (continueAtLeaves policy continuations) B := by
  induction policy generalizing B with
  | abort => exact True.intro
  | respond answer => exact later.2
  | inquire a next ih => exact fun o => ih o (continuations o) _ (later o)

theorem continueAtLeaves_retains_first {question : Question State}
    (preserved : PreservesAgreement P question)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : RefinesLeaves P sense question policy B) :
    RefinesLeaves P sense question (continueAtLeaves policy continuations) B := by
  induction policy generalizing B with
  | abort => exact True.intro
  | respond answer =>
    exact homogeneous_refines_every_continuation P sense preserved continuations B first
  | inquire a next ih => exact fun o => ih o (continuations o) _ (first o)

/-- K4: attach certified inquiries where the first inquiry actually ends. The
first question remains homogeneous within each leaf and the same native prefix
conditions continue to hold. Historical answer-value preservation uses the key
specialization below. Separate executability from the original start is not
the premise. -/
theorem continuing_inquiry_identifies_join {left right : Question State}
    (preserved : PreservesAgreement P left)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : Identifies P safe sense left policy B)
    (later : ContinuationsIdentify P safe sense right policy continuations B) :
    Identifies P safe sense (Join left right) (continueAtLeaves policy continuations) B := by
  refine ⟨continueAtLeaves_sound P safe sense right policy continuations B first.1 later, ?_⟩
  exact (refines_join_iff P sense left right (continueAtLeaves policy continuations) B).mpr
    ⟨continueAtLeaves_retains_first P sense preserved policy continuations B first.2,
      continueAtLeaves_refines_later P safe sense right policy continuations B later⟩

/-- An invariant target key retains its original value along the actual native
history, making the first component a question about that same target before
and after the continuation. Key invariance is a local law property to derive
in an application, not a law asserted of arbitrary changing readouts. -/
theorem continuing_initial_question_identifies_join {Answer : Type w}
    (key : State → Answer)
    (preserved : ∀ s a t, P.step s a t → key t = key s)
    {right : Question State}
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (first : Identifies P safe sense (Agreement key) policy B)
    (later : ContinuationsIdentify P safe sense right policy continuations B) :
    Identifies P safe sense (Join (Agreement key) right)
      (continueAtLeaves policy continuations) B :=
  continuing_inquiry_identifies_join P safe sense
    (agreement_preserved_of_key_preserved P key preserved)
    policy continuations B first later

theorem attainable_by_continuing_inquiry {left right : Question State}
    (preserved : PreservesAgreement P left)
    (policy : Policy Action Unit observations) (continuations : LeafContinuations policy)
    (B : State → Prop) (live : InhabitedBelief B)
    (first : Identifies P safe sense left policy B)
    (later : ContinuationsIdentify P safe sense right policy continuations B) :
    Attainable P safe sense (Join left right) B :=
  ⟨live, continueAtLeaves policy continuations,
    continuing_inquiry_identifies_join P safe sense preserved policy continuations B first later⟩

end Generative.InquirySufficiency.AttainableQuestions

#print axioms Generative.InquirySufficiency.AttainableQuestions.Question
#print axioms Generative.InquirySufficiency.AttainableQuestions.Agreement
#print axioms Generative.InquirySufficiency.AttainableQuestions.Coarser
#print axioms Generative.InquirySufficiency.AttainableQuestions.Join
#print axioms Generative.InquirySufficiency.AttainableQuestions.FamilyJoin
#print axioms Generative.InquirySufficiency.AttainableQuestions.Homogeneous
#print axioms Generative.InquirySufficiency.AttainableQuestions.InquirySound
#print axioms Generative.InquirySufficiency.AttainableQuestions.RefinesLeaves
#print axioms Generative.InquirySufficiency.AttainableQuestions.Identifies
#print axioms Generative.InquirySufficiency.AttainableQuestions.Attainable
#print axioms Generative.InquirySufficiency.AttainableQuestions.IsGreatest
#print axioms Generative.InquirySufficiency.AttainableQuestions.identifies_every_actual_execution_safe
#print axioms Generative.InquirySufficiency.AttainableQuestions.identifies_has_actual_execution
#print axioms Generative.InquirySufficiency.AttainableQuestions.PreservesAgreement
#print axioms Generative.InquirySufficiency.AttainableQuestions.LeafContinuations
#print axioms Generative.InquirySufficiency.AttainableQuestions.continueAtLeaves
#print axioms Generative.InquirySufficiency.AttainableQuestions.ContinuationsIdentify
#print axioms Generative.InquirySufficiency.AttainableQuestions.coarser_refl
#print axioms Generative.InquirySufficiency.AttainableQuestions.coarser_trans
#print axioms Generative.InquirySufficiency.AttainableQuestions.join_projects_left
#print axioms Generative.InquirySufficiency.AttainableQuestions.join_projects_right
#print axioms Generative.InquirySufficiency.AttainableQuestions.join_least
#print axioms Generative.InquirySufficiency.AttainableQuestions.agreement_pair_iff
#print axioms Generative.InquirySufficiency.AttainableQuestions.answer_projection_coarser
#print axioms Generative.InquirySufficiency.AttainableQuestions.refines_coarser
#print axioms Generative.InquirySufficiency.AttainableQuestions.identifies_coarser
#print axioms Generative.InquirySufficiency.AttainableQuestions.attainable_downward
#print axioms Generative.InquirySufficiency.AttainableQuestions.refines_join_iff
#print axioms Generative.InquirySufficiency.AttainableQuestions.shared_policy_join_iff
#print axioms Generative.InquirySufficiency.AttainableQuestions.attainable_join_iff_shared_policy
#print axioms Generative.InquirySufficiency.AttainableQuestions.refines_family_iff
#print axioms Generative.InquirySufficiency.AttainableQuestions.family_shared_policy_iff
#print axioms Generative.InquirySufficiency.AttainableQuestions.missing_join_no_greatest
#print axioms Generative.InquirySufficiency.AttainableQuestions.missing_join_no_attainable_common_upper
#print axioms Generative.InquirySufficiency.AttainableQuestions.agreement_preserved_of_key_preserved
#print axioms Generative.InquirySufficiency.AttainableQuestions.homogeneous_after
#print axioms Generative.InquirySufficiency.AttainableQuestions.homogeneous_refines_every_continuation
#print axioms Generative.InquirySufficiency.AttainableQuestions.continueAtLeaves_sound
#print axioms Generative.InquirySufficiency.AttainableQuestions.continueAtLeaves_refines_later
#print axioms Generative.InquirySufficiency.AttainableQuestions.continueAtLeaves_retains_first
#print axioms Generative.InquirySufficiency.AttainableQuestions.continuing_inquiry_identifies_join
#print axioms Generative.InquirySufficiency.AttainableQuestions.continuing_initial_question_identifies_join
#print axioms Generative.InquirySufficiency.AttainableQuestions.attainable_by_continuing_inquiry
