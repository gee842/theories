import InquirySufficiency

/-!
# Exact finite successor enumeration discharges branch classification

The process is unchanged. Its states are represented by `Fin size`, with an
executable decision for its actual transition relation. Initial membership is
also executable; the final interface accepts a Boolean membership table. These
are representation inputs, not a new event law or an oracle claiming an exact
successor list. The list is constructed here and its exactness proved.
The final Boolean-table adapter also derives the transition decisions from
executable representation data; it does not infer an arbitrary process's law.

All nondeterministic successors and all retained state coordinates survive the
enumeration. A native infinite state space cannot be truncated to this carrier
without a separate faithful representation argument. Finite observation and
state sets do not make arbitrary proposition-valued relations decidable.

This discharges `ClassifiedThrough` in the existing policy characterization.
It does not search an arbitrary action/response space, install a planner, form
an observation channel, or derive a criterion's meaning or authority.
-/

namespace Generative.InquirySufficiency.FiniteClassification

universe u v

theorem mem_cons_constructive {α : Type u} {x first : α} {rest : List α} :
    x ∈ first :: rest ↔ x = first ∨ x ∈ rest := by
  constructor
  · intro h
    cases h with
    | head => exact Or.inl rfl
    | tail _ h => exact Or.inr h
  · intro h
    rcases h with same | member
    · subst x
      exact List.Mem.head rest
    · exact List.Mem.tail first member

theorem mem_map_constructive {α : Type u} {β : Type v}
    (f : α → β) (xs : List α) (y : β) :
    y ∈ xs.map f ↔ ∃ x, x ∈ xs ∧ f x = y := by
  induction xs with
  | nil =>
    constructor
    · intro h
      cases h
    · rintro ⟨x, h, _⟩
      cases h
  | cons first rest ih =>
    constructor
    · intro h
      rcases mem_cons_constructive.mp h with same | member
      · exact ⟨first, List.Mem.head rest, same.symm⟩
      · obtain ⟨x, hx, same⟩ := ih.mp member
        exact ⟨x, List.Mem.tail first hx, same⟩
    · rintro ⟨x, hx, same⟩
      rcases mem_cons_constructive.mp hx with head | member
      · subst x
        exact mem_cons_constructive.mpr (Or.inl same.symm)
      · exact mem_cons_constructive.mpr (Or.inr (ih.mpr ⟨x, member, same⟩))

/-- Exhaust the entire declared finite carrier; no coverage certificate is input. -/
def states : (size : Nat) → List (Fin size)
  | 0 => []
  | size + 1 => ⟨0, Nat.zero_lt_succ size⟩ :: (states size).map Fin.succ

theorem states_complete (size : Nat) (s : Fin size) : s ∈ states size := by
  induction size with
  | zero => exact Fin.elim0 s
  | succ size ih =>
    obtain ⟨value, bound⟩ := s
    cases value with
    | zero => exact List.Mem.head _
    | succ value =>
      exact List.Mem.tail _
        ((mem_map_constructive Fin.succ _ _).mpr
          ⟨⟨value, Nat.lt_of_succ_lt_succ bound⟩,
            ih ⟨value, Nat.lt_of_succ_lt_succ bound⟩, rfl⟩)

def collect {α : Type u} (test : α → Bool) : List α → List α
  | [] => []
  | first :: rest =>
      match test first with
      | false => collect test rest
      | true => first :: collect test rest

theorem mem_collect_iff {α : Type u} (test : α → Bool) (xs : List α) (x : α) :
    x ∈ collect test xs ↔ x ∈ xs ∧ test x = true := by
  induction xs with
  | nil =>
    constructor
    · intro h
      cases h
    · intro h
      cases h.1
  | cons first rest ih =>
    cases value : test first with
    | false =>
      rw [collect, value]
      constructor
      · intro h
        have got := ih.mp h
        exact ⟨List.Mem.tail first got.1, got.2⟩
      · rintro ⟨member, truth⟩
        rcases mem_cons_constructive.mp member with same | later
        · subst x
          exact False.elim (Bool.noConfusion (value.symm.trans truth))
        · exact ih.mpr ⟨later, truth⟩
    | true =>
      rw [collect, value]
      constructor
      · intro h
        rcases mem_cons_constructive.mp h with same | later
        · subst x
          exact ⟨List.Mem.head rest, value⟩
        · have got := ih.mp later
          exact ⟨List.Mem.tail first got.1, got.2⟩
      · rintro ⟨member, truth⟩
        rcases mem_cons_constructive.mp member with same | later
        · exact mem_cons_constructive.mpr (Or.inl same)
        · exact mem_cons_constructive.mpr (Or.inr (ih.mpr ⟨later, truth⟩))

def decisionBit {p : Prop} : Decidable p → Bool
  | .isFalse _ => false
  | .isTrue _ => true

theorem decisionBit_true_iff {p : Prop} (decision : Decidable p) :
    decisionBit decision = true ↔ p := by
  cases decision with
  | isFalse no =>
    constructor
    · intro impossible
      cases impossible
    · intro yes
      exact False.elim (no yes)
  | isTrue yes => exact ⟨fun _ => yes, fun _ => rfl⟩

/-- Construct an exact list from executable membership over the entire carrier. -/
def enumerate {size : Nat} (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) : List (Fin size) :=
  collect (fun s => decisionBit (membership s)) (states size)

theorem mem_enumerate_iff {size : Nat} (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) (s : Fin size) :
    s ∈ enumerate B membership ↔ B s := by
  constructor
  · intro member
    exact (decisionBit_true_iff (membership s)).mp
      ((mem_collect_iff _ _ _).mp member).2
  · intro member
    exact (mem_collect_iff _ _ _).mpr
      ⟨states_complete size s, (decisionBit_true_iff (membership s)).mpr member⟩

def beliefDecision {size : Nat} (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) : Decidable (InhabitedBelief B) :=
  nonemptyDecisionFromList B (enumerate B membership)
    (fun s => (mem_enumerate_iff B membership s).symm)

variable {size observations : Nat} {Action : Type u} {Response : Type v}
variable (P : Process (Fin size) Action)
variable (transition : ∀ s a t, Decidable (P.step s a t))
variable (sense : Fin size → Action → Fin size → Fin observations)

/-- Search all predecessors of the proposed endpoint under the native law. -/
def afterMembership (B : Fin size → Prop) (membership : ∀ s, Decidable (B s))
    (a : Action) (o : Fin observations) (t : Fin size) :
    Decidable (After P sense B a o t) :=
  beliefDecision (fun s => B s ∧ P.step s a t ∧ sense s a t = o)
    (fun s => by
      letI := membership s
      letI := transition s a t
      infer_instance)

/-- Enumerate every actual successor compatible with the acquired observation. -/
def successors (B : Fin size → Prop) (membership : ∀ s, Decidable (B s))
    (a : Action) (o : Fin observations) : List (Fin size) :=
  enumerate (After P sense B a o) (afterMembership P transition sense B membership a o)

theorem mem_successors_iff (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) (a : Action) (o : Fin observations) (t : Fin size) :
    t ∈ successors P transition sense B membership a o ↔
      ∃ s, B s ∧ P.step s a t ∧ sense s a t = o :=
  mem_enumerate_iff _ _ t

theorem actual_successor_retained {B : Fin size → Prop}
    (membership : ∀ s, Decidable (B s)) {s t : Fin size} {a : Action}
    (member : B s) (actual : P.step s a t) :
    t ∈ successors P transition sense B membership a (sense s a t) :=
  (mem_successors_iff P transition sense B membership a _ t).mpr
    ⟨s, member, actual, rfl⟩

include transition

/-- Branch classification is derived at every finite depth, not assumed. No
finiteness or enumeration of the action space is required for this property. -/
theorem classifiedThrough (depth : Nat) (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) : ClassifiedThrough P sense depth B := by
  induction depth generalizing B with
  | zero => exact True.intro
  | succ depth ih =>
    intro a o
    let nextMembership := afterMembership P transition sense B membership a o
    exact ⟨empty_or_inhabited_of_decidable
        (beliefDecision (After P sense B a o) nextMembership),
      ih (After P sense B a o) nextMembership⟩

theorem implication_iff_bounded_policy
    (safe : Fin size → Action → Fin size → Prop) (goal : Fin size → Prop)
    (response : Response → List Action) (depth : Nat) (B : Fin size → Prop)
    (membership : ∀ s, Decidable (B s)) :
    ImplicationSufficient P safe goal sense response depth B ↔
      InhabitedBelief B ∧ ∃ policy,
        Within depth policy ∧ Sound P safe goal sense response policy B :=
  (sufficiency_iff_implication_form depth B
      (classifiedThrough P transition sense depth B membership)).symm.trans
    (sufficiency_iff_bounded_policy depth B)

/-- Initial membership is executable input data. Neither a classification proof
nor a claimed exact successor enumeration is an argument to this interface. -/
theorem boolean_initial_iff_bounded_policy
    (safe : Fin size → Action → Fin size → Prop) (goal : Fin size → Prop)
    (response : Response → List Action) (depth : Nat) (initial : Fin size → Bool) :
    ImplicationSufficient P safe goal sense response depth (fun s => initial s = true) ↔
      InhabitedBelief (fun s => initial s = true) ∧ ∃ policy,
        Within depth policy ∧
          Sound P safe goal sense response policy (fun s => initial s = true) :=
  implication_iff_bounded_policy P transition sense safe goal response depth _
    (fun _ => inferInstance)

omit transition

/-- Interpret an executable transition table as a relation. This generic
representation adapter asserts no particular table as a physical law. -/
def tableProcess (table : Fin size → Action → Fin size → Bool) :
    Process (Fin size) Action :=
  ⟨fun s a t => table s a t = true⟩

/-- For Boolean model data, both transition and initial-membership decisions
are derived internally. A faithful encoding of any separately given native
process remains an application obligation, not a hidden theorem premise. -/
theorem boolean_model_iff_bounded_policy
    (table : Fin size → Action → Fin size → Bool)
    (safe : Fin size → Action → Fin size → Prop) (goal : Fin size → Prop)
    (response : Response → List Action) (depth : Nat) (initial : Fin size → Bool) :
    ImplicationSufficient (tableProcess table) safe goal sense response depth
        (fun s => initial s = true) ↔
      InhabitedBelief (fun s => initial s = true) ∧ ∃ policy,
        Within depth policy ∧ Sound (tableProcess table) safe goal sense response policy
          (fun s => initial s = true) :=
  boolean_initial_iff_bounded_policy (tableProcess table)
    (fun s a t => inferInstanceAs (Decidable (table s a t = true)))
    sense safe goal response depth initial

end Generative.InquirySufficiency.FiniteClassification

#print axioms Generative.InquirySufficiency.FiniteClassification.mem_cons_constructive
#print axioms Generative.InquirySufficiency.FiniteClassification.mem_map_constructive
#print axioms Generative.InquirySufficiency.FiniteClassification.states_complete
#print axioms Generative.InquirySufficiency.FiniteClassification.mem_collect_iff
#print axioms Generative.InquirySufficiency.FiniteClassification.decisionBit_true_iff
#print axioms Generative.InquirySufficiency.FiniteClassification.mem_enumerate_iff
#print axioms Generative.InquirySufficiency.FiniteClassification.beliefDecision
#print axioms Generative.InquirySufficiency.FiniteClassification.afterMembership
#print axioms Generative.InquirySufficiency.FiniteClassification.mem_successors_iff
#print axioms Generative.InquirySufficiency.FiniteClassification.actual_successor_retained
#print axioms Generative.InquirySufficiency.FiniteClassification.classifiedThrough
#print axioms Generative.InquirySufficiency.FiniteClassification.implication_iff_bounded_policy
#print axioms Generative.InquirySufficiency.FiniteClassification.boolean_initial_iff_bounded_policy
#print axioms Generative.InquirySufficiency.FiniteClassification.tableProcess
#print axioms Generative.InquirySufficiency.FiniteClassification.boolean_model_iff_bounded_policy
