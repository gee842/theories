import FiniteInquiryClassification
import AttainableQuestions
import ReachedInquiryComposition

/-!
# Inquiry certificates calculated from finite executable relations

The search constructs a policy and its proof, or excludes every policy through
the requested depth. It calculates nonemptiness, progress, the specified prefix
condition and terminal agreement. Neither a successful inquiry nor a branch
classification certificate is supplied. Every branch uses the native `After`.

The Boolean transition, prefix-condition and question relations are still model
data. Finiteness and the depth are explicit representational scope. The search
does not assert that every question is attainable, identify a model with the
whole generative process, derive the provenance of its law, or install memory
or a physical planner. Its negative answer is exact within the declared depth.
-/

namespace Generative.InquirySufficiency.DerivedCertificates

open FiniteClassification AttainableQuestions

universe u

/-- A successful result contains actual data, not just an existential proof. -/
inductive WitnessResult (α : Type u) (property : α → Prop) : Type u where
  | found (value : α) (certificate : property value)
  | missing (exclusion : ∀ value, ¬ property value)

def hasWitness {α : Type u} {property : α → Prop} : WitnessResult α property → Bool
  | .found _ _ => true
  | .missing _ => false

theorem hasWitness_iff {α : Type u} {property : α → Prop}
    (result : WitnessResult α property) : hasWitness result = true ↔ ∃ x, property x := by
  cases result with
  | found value certificate => exact ⟨fun _ => ⟨value, certificate⟩, fun _ => rfl⟩
  | missing exclusion =>
    constructor
    · intro impossible
      cases impossible
    · rintro ⟨value, certificate⟩
      exact False.elim (exclusion value certificate)

theorem hasWitness_false_iff {α : Type u} {property : α → Prop}
    (result : WitnessResult α property) : hasWitness result = false ↔ ∀ x, ¬ property x := by
  cases result with
  | found value certificate =>
    constructor
    · intro impossible
      cases impossible
    · intro exclusion
      exact False.elim (exclusion value certificate)
  | missing exclusion => exact ⟨fun _ => exclusion, fun _ => rfl⟩

/-- Constructive finite universal decision, without function equality. -/
def allDecision : (n : Nat) → (property : Fin n → Prop) →
    (∀ i, Decidable (property i)) → Decidable (∀ i, property i)
  | 0, _, _ => .isTrue (fun i => Fin.elim0 i)
  | n + 1, property, decision =>
      match decision ⟨0, Nat.zero_lt_succ n⟩ with
      | .isFalse no => .isFalse (fun every => no (every _))
      | .isTrue first =>
          match allDecision n (fun i => property i.succ) (fun i => decision i.succ) with
          | .isFalse no => .isFalse (fun every => no (fun i => every i.succ))
          | .isTrue rest => .isTrue (fun ⟨i, bound⟩ => by
              cases i with
              | zero => exact first
              | succ i => exact rest ⟨i, Nat.lt_of_succ_lt_succ bound⟩)

/-- Assemble actual witnesses at every observation, or retain a failed branch. -/
def allWitness {α : Type u} : (n : Nat) → (property : Fin n → α → Prop) →
    (∀ i, WitnessResult α (property i)) →
    WitnessResult (Fin n → α) (fun values => ∀ i, property i (values i))
  | 0, _, _ => .found (fun i => Fin.elim0 i) (fun i => Fin.elim0 i)
  | n + 1, property, results =>
      match results ⟨0, Nat.zero_lt_succ n⟩ with
      | .missing no => .missing (fun values every => no (values _) (every _))
      | .found first firstProof =>
          match allWitness n (fun i => property i.succ) (fun i => results i.succ) with
          | .missing no =>
              .missing (fun values every => no (fun i => values i.succ) (fun i => every i.succ))
          | .found rest restProof => .found (finiteCons first rest) (fun ⟨i, bound⟩ => by
              cases i with
              | zero => exact firstProof
              | succ i => exact restProof ⟨i, Nat.lt_of_succ_lt_succ bound⟩)

/-- Search the entire finite action carrier and keep the successful data. -/
def someWitness {α : Type u} : (n : Nat) → (property : Fin n → α → Prop) →
    (∀ i, WitnessResult α (property i)) →
    WitnessResult (Fin n × α) (fun pair => property pair.1 pair.2)
  | 0, _, _ => .missing (fun pair => Fin.elim0 pair.1)
  | n + 1, property, results =>
      match results ⟨0, Nat.zero_lt_succ n⟩ with
      | .found value certificate => .found (⟨0, Nat.zero_lt_succ n⟩, value) certificate
      | .missing firstNo =>
          match someWitness n (fun i => property i.succ) (fun i => results i.succ) with
          | .found pair certificate => .found (pair.1.succ, pair.2) certificate
          | .missing restNo => .missing (fun ⟨⟨i, bound⟩, value⟩ certificate => by
              cases i with
              | zero => exact firstNo value certificate
              | succ i => exact restNo (⟨i, Nat.lt_of_succ_lt_succ bound⟩, value) certificate)

variable {size actions observations : Nat}
variable (table : Fin size → Fin actions → Fin size → Bool)
variable (condition : Fin size → Fin actions → Fin size → Bool)
variable (sense : Fin size → Fin actions → Fin size → Fin observations)
variable (question : Fin size → Fin size → Bool)

abbrev prefixCondition (s : Fin size) (a : Fin actions) (t : Fin size) : Prop :=
  condition s a t = true

abbrev questionRelation (s t : Fin size) : Prop := question s t = true

def homogeneousDecision (B : Fin size → Prop) (membership : ∀ s, Decidable (B s)) :
    Decidable (Homogeneous (questionRelation question) B) :=
  allDecision size (fun s => ∀ t, B s → B t → question s t = true) (fun s =>
    allDecision size (fun t => B s → B t → question s t = true) (fun t => by
      letI := membership s
      letI := membership t
      infer_instance))

def admissibleDecision (B : Fin size → Prop) (membership : ∀ s, Decidable (B s))
    (a : Fin actions) :
    Decidable (InquiryAdmissible (tableProcess table) (prefixCondition condition) B a) :=
  allDecision size (fun s => B s → Enabled (tableProcess table) s a ∧
    ∀ t, (tableProcess table).step s a t → prefixCondition condition s a t) (fun s => by
      letI := membership s
      letI : Decidable (Enabled (tableProcess table) s a) :=
        beliefDecision (fun t => table s a t = true) (fun _ => inferInstance)
      letI : Decidable (∀ t, (tableProcess table).step s a t → prefixCondition condition s a t) :=
        allDecision size _ (fun t => inferInstanceAs (Decidable (table s a t = true → condition s a t = true)))
      infer_instance)

abbrev Certified (depth : Nat) (B : Fin size → Prop)
    (policy : Policy (Fin actions) Unit observations) : Prop :=
  Within depth policy ∧
    Identifies (tableProcess table) (prefixCondition condition) sense
      (questionRelation question) policy B

/-- A complete constructive search at a declared depth. Empty branches receive
`abort`; a nonempty branch must actually respond or make admissible progress. -/
def search : (depth : Nat) → (B : Fin size → Prop) →
    (∀ s, Decidable (B s)) →
    WitnessResult (Policy (Fin actions) Unit observations)
      (Certified table condition sense question depth B)
  | depth, B, membership =>
      match beliefDecision B membership with
      | .isFalse empty => .found .abort ⟨by cases depth <;> exact True.intro,
          (fun s member => empty ⟨s, member⟩), True.intro⟩
      | .isTrue live =>
          match homogeneousDecision question B membership with
          | .isTrue same => .found (.respond ()) ⟨by cases depth <;> exact True.intro,
              ⟨live, fun _ _ => True.intro⟩, same⟩
          | .isFalse different =>
              match depth with
              | 0 => .missing (fun policy certificate => by
                  cases policy with
                  | abort =>
                      obtain ⟨s, member⟩ := live
                      exact certificate.2.1 s member
                  | respond _ => exact different certificate.2.2
                  | inquire _ _ => exact certificate.1)
              | depth + 1 =>
                  let choices := fun a =>
                    match admissibleDecision table condition B membership a with
                    | .isFalse no => WitnessResult.missing
                        (fun (next : Fin observations → Policy (Fin actions) Unit observations)
                          (certificate : InquiryAdmissible (tableProcess table)
                            (prefixCondition condition) B a ∧
                            ∀ o, Certified table condition sense question depth
                              (After (tableProcess table) sense B a o) (next o)) => no certificate.1)
                    | .isTrue admissible =>
                        match allWitness observations
                            (fun o policy => Certified table condition sense question depth
                              (After (tableProcess table) sense B a o) policy)
                            (fun o => search depth (After (tableProcess table) sense B a o)
                              (afterMembership (tableProcess table) (fun s a t => inferInstanceAs (Decidable (table s a t = true)))
                                sense B membership a o)) with
                        | .missing no => .missing (fun next certificate => no next certificate.2)
                        | .found next certificates => .found next ⟨admissible, certificates⟩
                  match someWitness actions _ choices with
                  | .found pair certificates => .found (.inquire pair.1 pair.2)
                      ⟨fun o => (certificates.2 o).1,
                        ⟨live, certificates.1, fun o => (certificates.2 o).2.1⟩,
                        fun o => (certificates.2 o).2.2⟩
                  | .missing no => .missing (fun policy certificate => by
                      cases policy with
                      | abort =>
                          obtain ⟨s, member⟩ := live
                          exact certificate.2.1 s member
                      | respond _ => exact different certificate.2.2
                      | inquire a next =>
                          exact no (a, next) ⟨certificate.2.1.2.1,
                            fun o => ⟨certificate.1 o,
                              (certificate.2.1.2.2 o), certificate.2.2 o⟩⟩)

/-- The public search rejects an empty starting configuration. Its successful
result derives both liveness and inquiry adequacy from the executable data. -/
def inquirySearch (depth : Nat) (initial : Fin size → Bool) :
    WitnessResult (Policy (Fin actions) Unit observations)
      (fun policy => InhabitedBelief (fun s => initial s = true) ∧
        Certified table condition sense question depth (fun s => initial s = true) policy) :=
  match beliefDecision (fun s => initial s = true) (fun _ => inferInstance) with
  | .isFalse empty => .missing (fun _ certificate => empty certificate.1)
  | .isTrue live =>
      match search table condition sense question depth (fun s => initial s = true)
          (fun _ => inferInstance) with
      | .found policy certificate => .found policy ⟨live, certificate⟩
      | .missing no => .missing (fun policy certificate => no policy certificate.2)

def canIdentify (depth : Nat) (initial : Fin size → Bool) : Bool :=
  hasWitness (inquirySearch table condition sense question depth initial)

theorem canIdentify_iff (depth : Nat) (initial : Fin size → Bool) :
    canIdentify table condition sense question depth initial = true ↔
      InhabitedBelief (fun s => initial s = true) ∧
        ∃ policy, Within depth policy ∧
          Identifies (tableProcess table) (prefixCondition condition) sense
            (questionRelation question) policy (fun s => initial s = true) := by
  constructor
  · intro accepted
    obtain ⟨policy, live, certificate⟩ :=
      (hasWitness_iff (inquirySearch table condition sense question depth initial)).mp accepted
    exact ⟨live, policy, certificate⟩
  · rintro ⟨live, policy, certificate⟩
    exact (hasWitness_iff (inquirySearch table condition sense question depth initial)).mpr
      ⟨policy, live, certificate⟩

theorem canIdentify_false_iff (depth : Nat) (initial : Fin size → Bool) :
    canIdentify table condition sense question depth initial = false ↔
      ¬ (InhabitedBelief (fun s => initial s = true) ∧
        ∃ policy, Within depth policy ∧
          Identifies (tableProcess table) (prefixCondition condition) sense
            (questionRelation question) policy (fun s => initial s = true)) := by
  constructor
  · intro rejected certificate
    have accepted := (canIdentify_iff table condition sense question depth initial).mpr certificate
    exact Bool.noConfusion (rejected.symm.trans accepted)
  · intro impossible
    cases answer : canIdentify table condition sense question depth initial with
    | false => exact rfl
    | true =>
      exact False.elim
        (impossible ((canIdentify_iff table condition sense question depth initial).mp answer))

/-- Extracting the policy is computational; no choice operator is involved. -/
def policyOption {α : Type u} {property : α → Prop} : WitnessResult α property → Option α
  | .found value _ => some value
  | .missing _ => none

theorem policyOption_certified {α : Type u} {property : α → Prop}
    (result : WitnessResult α property) {value : α}
    (selected : policyOption result = some value) : property value := by
  cases result with
  | found actual certificate =>
    have equal : actual = value := Option.some.inj selected
    subst value
    exact certificate
  | missing _ => cases selected

/-- A computationally accepted model therefore has an attainable question;
the depth remains part of the search's interface, not of `Attainable`. -/
theorem accepted_is_attainable (depth : Nat) (initial : Fin size → Bool)
    (accepted : canIdentify table condition sense question depth initial = true) :
    Attainable (tableProcess table) (prefixCondition condition) sense
      (questionRelation question) (fun s => initial s = true) := by
  obtain ⟨live, policy, _, identified⟩ :=
    (canIdentify_iff table condition sense question depth initial).mp accepted
  exact ⟨live, policy, identified⟩

/-- Assemble a dependent finite table directly; no equality of functions is
needed when different prefix branches have different continuation shapes. -/
def dependentCons {n : Nat} {α : Fin (n + 1) → Type u}
    (first : α ⟨0, Nat.zero_lt_succ n⟩) (rest : ∀ i : Fin n, α i.succ) : ∀ i, α i
  | ⟨0, _⟩ => first
  | ⟨i + 1, bound⟩ => rest ⟨i, Nat.lt_of_succ_lt_succ bound⟩

def allDependentWitness : (n : Nat) → (α : Fin n → Type u) →
    (property : ∀ i, α i → Prop) → (∀ i, WitnessResult (α i) (property i)) →
    WitnessResult (∀ i, α i) (fun values => ∀ i, property i (values i))
  | 0, _, _, _ => .found (fun i => Fin.elim0 i) (fun i => Fin.elim0 i)
  | n + 1, α, property, results =>
      match results ⟨0, Nat.zero_lt_succ n⟩ with
      | .missing no => .missing (fun values every => no (values _) (every _))
      | .found first firstProof =>
          match allDependentWitness n (fun i => α i.succ)
              (fun i => property i.succ) (fun i => results i.succ) with
          | .missing no =>
              .missing (fun values every => no (fun i => values i.succ) (fun i => every i.succ))
          | .found rest restProof => .found (dependentCons first rest) (fun ⟨i, bound⟩ => by
              cases i with
              | zero => exact firstProof
              | succ i => exact restProof ⟨i, Nat.lt_of_succ_lt_succ bound⟩)

def ContinuationsBounded (depth : Nat) : (policy : Policy (Fin actions) Unit observations) →
    LeafContinuations policy → Prop
  | .abort, _ => True
  | .respond _, continuation => Within depth continuation
  | .inquire _ next, continuations =>
      ∀ o, ContinuationsBounded depth (next o) (continuations o)

/-- Search separately where every actual prefix leaf ends. The returned object
contains the continuation trees and proofs; depletion and changed access remain
inside each native `After`. No continuation certificate is an input. -/
def continuationSearch (depth : Nat) :
    (policy : Policy (Fin actions) Unit observations) → (B : Fin size → Prop) →
    (∀ s, Decidable (B s)) → WitnessResult (LeafContinuations policy)
      (fun continuations => ContinuationsBounded depth policy continuations ∧
        ContinuationsIdentify (tableProcess table) (prefixCondition condition) sense
          (questionRelation question) policy continuations B)
  | .abort, _, _ => .found PUnit.unit ⟨True.intro, True.intro⟩
  | .respond _, B, membership => search table condition sense question depth B membership
  | .inquire a next, B, membership =>
      match allDependentWitness observations (fun o => LeafContinuations (next o))
          (fun o continuations => ContinuationsBounded depth (next o) continuations ∧
            ContinuationsIdentify (tableProcess table) (prefixCondition condition) sense
              (questionRelation question) (next o) continuations
              (After (tableProcess table) sense B a o))
          (fun o => continuationSearch depth (next o) (After (tableProcess table) sense B a o)
            (afterMembership (tableProcess table)
              (fun s a t => inferInstanceAs (Decidable (table s a t = true)))
              sense B membership a o)) with
      | .found continuations certificates => .found continuations
          ⟨fun o => (certificates o).1, fun o => (certificates o).2⟩
      | .missing no => .missing (fun continuations certificate =>
          no continuations (fun o => ⟨certificate.1 o, certificate.2 o⟩))

theorem continuationSearch_iff (depth : Nat)
    (policy : Policy (Fin actions) Unit observations)
    (B : Fin size → Prop) (membership : ∀ s, Decidable (B s)) :
    hasWitness (continuationSearch table condition sense question depth policy B membership) = true ↔
      ∃ continuations, ContinuationsBounded depth policy continuations ∧
        ContinuationsIdentify (tableProcess table) (prefixCondition condition) sense
          (questionRelation question) policy continuations B :=
  hasWitness_iff _

/-- Verify a specified prefix through every actual branch. A successful answer
derives its execution contract instead of receiving `InquirySound` as input. -/
def soundDecision : (policy : Policy (Fin actions) Unit observations) →
    (B : Fin size → Prop) → (∀ s, Decidable (B s)) →
    Decidable (InquirySound (tableProcess table) (prefixCondition condition) sense policy B)
  | .abort, B, membership =>
      match beliefDecision B membership with
      | .isFalse empty => .isTrue (fun s member => empty ⟨s, member⟩)
      | .isTrue live => .isFalse (fun empty => by
          obtain ⟨s, member⟩ := live
          exact empty s member)
  | .respond _, B, membership =>
      match beliefDecision B membership with
      | .isFalse empty => .isFalse (fun certificate => empty certificate.1)
      | .isTrue live => .isTrue ⟨live, fun _ _ => True.intro⟩
  | .inquire a next, B, membership => by
      change Decidable (InhabitedBelief B ∧
        InquiryAdmissible (tableProcess table) (prefixCondition condition) B a ∧
        ∀ o, InquirySound (tableProcess table) (prefixCondition condition) sense
          (next o) (After (tableProcess table) sense B a o))
      letI := beliefDecision B membership
      letI := admissibleDecision table condition B membership a
      letI := allDecision observations _ (fun o => soundDecision (next o)
        (After (tableProcess table) sense B a o)
        (afterMembership (tableProcess table)
          (fun s a t => inferInstanceAs (Decidable (table s a t = true))) sense B membership a o))
      infer_instance

abbrev ComposedCertificate (depth : Nat)
    (policy : Policy (Fin actions) Unit observations)
    (B : Fin size → Prop) (continuations : LeafContinuations policy) : Prop :=
  InhabitedBelief B ∧
    InquirySound (tableProcess table) (prefixCondition condition) sense policy B ∧
    ContinuationsBounded depth policy continuations ∧
    Identifies (tableProcess table) (prefixCondition condition) sense
      (questionRelation question) (continueAtLeaves policy continuations) B

/-- End-to-end interface: calculate prefix validity, initial liveness and all
reached continuation certificates. Neither global preservation, a prefix answer,
nor any of the execution/answer certificates is an argument. Rejection is exact
for this prefix and the declared bound at each continuation leaf. -/
def composedSearch (depth : Nat) (policy : Policy (Fin actions) Unit observations)
    (initial : Fin size → Bool) : WitnessResult (LeafContinuations policy)
      (ComposedCertificate table condition sense question depth policy (fun s => initial s = true)) :=
  match beliefDecision (fun s => initial s = true) (fun _ => inferInstance) with
  | .isFalse empty => .missing (fun _ certificate => empty certificate.1)
  | .isTrue live =>
      match soundDecision table condition sense policy (fun s => initial s = true)
          (fun _ => inferInstance) with
      | .isFalse no => .missing (fun _ certificate => no certificate.2.1)
      | .isTrue sound =>
          match continuationSearch table condition sense question depth policy
              (fun s => initial s = true) (fun _ => inferInstance) with
          | .found continuations certificate => .found continuations
              ⟨live, sound, certificate.1,
                (ReachedInquiryComposition.continued_identifies_iff
                  (tableProcess table) (prefixCondition condition) sense
                  (questionRelation question) policy continuations
                  (fun s => initial s = true) sound).mpr certificate.2⟩
          | .missing no => .missing (fun continuations certificate =>
              no continuations ⟨certificate.2.2.1,
                ReachedInquiryComposition.continuations_of_identified_composite
                  (tableProcess table) (prefixCondition condition) sense
                  (questionRelation question) policy continuations
                  (fun s => initial s = true) certificate.2.2.2⟩)

def canContinue (depth : Nat) (policy : Policy (Fin actions) Unit observations)
    (initial : Fin size → Bool) : Bool :=
  hasWitness (composedSearch table condition sense question depth policy initial)

theorem canContinue_iff (depth : Nat) (policy : Policy (Fin actions) Unit observations)
    (initial : Fin size → Bool) :
    canContinue table condition sense question depth policy initial = true ↔
      ∃ continuations, ComposedCertificate table condition sense question depth policy
        (fun s => initial s = true) continuations :=
  hasWitness_iff _

theorem canContinue_false_iff (depth : Nat)
    (policy : Policy (Fin actions) Unit observations) (initial : Fin size → Bool) :
    canContinue table condition sense question depth policy initial = false ↔
      ∀ continuations, ¬ ComposedCertificate table condition sense question depth policy
        (fun s => initial s = true) continuations :=
  hasWitness_false_iff _

theorem accepted_continuation_is_attainable (depth : Nat)
    (policy : Policy (Fin actions) Unit observations) (initial : Fin size → Bool)
    (accepted : canContinue table condition sense question depth policy initial = true) :
    Attainable (tableProcess table) (prefixCondition condition) sense
      (questionRelation question) (fun s => initial s = true) := by
  obtain ⟨continuations, certificate⟩ :=
    (canContinue_iff table condition sense question depth policy initial).mp accepted
  exact ⟨certificate.1, continueAtLeaves policy continuations, certificate.2.2.2⟩

end Generative.InquirySufficiency.DerivedCertificates

#print axioms Generative.InquirySufficiency.DerivedCertificates.WitnessResult
#print axioms Generative.InquirySufficiency.DerivedCertificates.hasWitness
#print axioms Generative.InquirySufficiency.DerivedCertificates.hasWitness_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.hasWitness_false_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.allDecision
#print axioms Generative.InquirySufficiency.DerivedCertificates.allWitness
#print axioms Generative.InquirySufficiency.DerivedCertificates.someWitness
#print axioms Generative.InquirySufficiency.DerivedCertificates.prefixCondition
#print axioms Generative.InquirySufficiency.DerivedCertificates.questionRelation
#print axioms Generative.InquirySufficiency.DerivedCertificates.homogeneousDecision
#print axioms Generative.InquirySufficiency.DerivedCertificates.admissibleDecision
#print axioms Generative.InquirySufficiency.DerivedCertificates.Certified
#print axioms Generative.InquirySufficiency.DerivedCertificates.search
#print axioms Generative.InquirySufficiency.DerivedCertificates.inquirySearch
#print axioms Generative.InquirySufficiency.DerivedCertificates.canIdentify
#print axioms Generative.InquirySufficiency.DerivedCertificates.canIdentify_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.canIdentify_false_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.policyOption
#print axioms Generative.InquirySufficiency.DerivedCertificates.policyOption_certified
#print axioms Generative.InquirySufficiency.DerivedCertificates.accepted_is_attainable
#print axioms Generative.InquirySufficiency.DerivedCertificates.dependentCons
#print axioms Generative.InquirySufficiency.DerivedCertificates.allDependentWitness
#print axioms Generative.InquirySufficiency.DerivedCertificates.ContinuationsBounded
#print axioms Generative.InquirySufficiency.DerivedCertificates.continuationSearch
#print axioms Generative.InquirySufficiency.DerivedCertificates.continuationSearch_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.soundDecision
#print axioms Generative.InquirySufficiency.DerivedCertificates.ComposedCertificate
#print axioms Generative.InquirySufficiency.DerivedCertificates.composedSearch
#print axioms Generative.InquirySufficiency.DerivedCertificates.canContinue
#print axioms Generative.InquirySufficiency.DerivedCertificates.canContinue_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.canContinue_false_iff
#print axioms Generative.InquirySufficiency.DerivedCertificates.accepted_continuation_is_attainable
