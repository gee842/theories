import ExplanatoryJoiningAnchors
import ExplanatoryJoiningBranches

/-! Repair loss of joint reference: a finite retained configuration remembers
its fragments, and questions address two slots in THAT same configuration.
An answer appends a witnessed result without replacing earlier slots.
Indices are internal reference positions, not shared native fragment names.
This is relational formation/query semantics, not a resource-copying license. -/
namespace Generative.ExplanatoryJoiningRegisters
open ExplanatoryBranching ExplanatoryLocalUnits
open ExplanatoryJoiningBranches (FiniteOutcomes)
universe u v
variable {F : Type u} {G : Type v}

abbrev Command := Nat × Nat

def Step (J : Join F) (xs : List F) (ij : Command) (ys : List F) : Prop :=
  ∃ a b z, xs[ij.1]? = some a ∧ xs[ij.2]? = some b ∧ J a b z ∧ ys = xs ++ [z]

def model (J : Join F) : Model (List F) Command Empty where
  process.step := Step J
  condition _ o := nomatch o

def Related (J : Join F) (K : Join G) := Same (model J) (model K)

theorem finite_outcomes_image_finite {J : Join F} (hf : FiniteOutcomes J) :
    ImageFinite (model J) := by
  intro xs ij
  cases ha : xs[ij.1]? with
  | none =>
    refine ⟨[], ?_⟩
    intro ys
    simp [model, Step, ha]
  | some a =>
    cases hb : xs[ij.2]? with
    | none =>
      refine ⟨[], ?_⟩
      intro ys
      simp [model, Step, hb]
    | some b =>
      obtain ⟨zs, hz⟩ := hf a b
      refine ⟨zs.map (fun z => xs ++ [z]), ?_⟩
      intro ys
      simp only [model, Step, ha, hb, Option.some.injEq, List.mem_map]
      constructor
      · rintro ⟨a', b', z, rfl, rfl, hj, he⟩
        exact ⟨z, (hz z).mp hj, he.symm⟩
      · rintro ⟨z, hj, he⟩
        exact ⟨a, b, z, rfl, rfl, (hz z).mpr hj, he.symm⟩

/-- Both selected slots are fixed BEFORE finding the result. The matched
configuration keeps those slots when appending its matched result. -/
theorem retained_pair_result_matches {J : Join F} {K : Join G} (fk : FiniteOutcomes K)
    {xs : List F} {ys : List G} (h : Related J K xs ys)
    (slots : xs.length = ys.length)
    {i j : Nat} {a b z : F} (ha : xs[i]? = some a) (hb : xs[j]? = some b) (hj : J a b z) :
    ∃ a' b' z', ys[i]? = some a' ∧ ys[j]? = some b' ∧ K a' b' z' ∧
      (xs ++ [z]).length = (ys ++ [z']).length ∧ Related J K (xs ++ [z]) (ys ++ [z']) := by
  have st : (model J).process.step xs (i, j) (xs ++ [z]) := ⟨a, b, z, ha, hb, hj, rfl⟩
  obtain ⟨next, hn, hs⟩ := same_forces_successor_match (finite_outcomes_image_finite fk) h st
  obtain ⟨a', b', z', ha', hb', hj', rfl⟩ := hn
  exact ⟨a', b', z', ha', hb', hj', by simp [slots], hs⟩

theorem step_retains_configuration {J : Join F} {xs ys : List F} {ij : Command}
    (h : Step J xs ij ys) : ∃ z, ys = xs ++ [z] := by
  obtain ⟨_, _, z, _, _, _, he⟩ := h
  exact ⟨z, he⟩

theorem trace_retains_configuration {J : Join F} {xs ys : List F} {commands : List Command}
    (h : Trace (model J).process xs commands ys) : ∃ added, ys = xs ++ added := by
  induction h with
  | nil xs => exact ⟨[], (List.append_nil xs).symm⟩
  | @cons xs middle ys ij rest hs ht ih =>
    obtain ⟨z, rfl⟩ := step_retains_configuration hs
    obtain ⟨added, he⟩ := ih
    exact ⟨[z] ++ added, he.trans (List.append_assoc xs [z] added)⟩

theorem trace_length {J : Join F} {xs ys : List F} {commands : List Command}
    (h : Trace (model J).process xs commands ys) : ys.length = xs.length + commands.length := by
  induction h with
  | nil xs => simp
  | @cons xs middle ys ij rest hs ht ih =>
    obtain ⟨z, rfl⟩ := step_retains_configuration hs
    simpa [List.length_append, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using ih

/-- A whole finite reference-sharing formation plan has a matched plan using
the same slot commands, including reuse of earlier results in later joins. -/
theorem retained_history_matches {J : Join F} {K : Join G}
    (fj : FiniteOutcomes J) (fk : FiniteOutcomes K)
    {xs : List F} {ys : List G} (h : Related J K xs ys)
    (slots : xs.length = ys.length)
    {commands : List Command} {finish : List F} (trace : Trace (model J).process xs commands finish) :
    ∃ finish', Trace (model K).process ys commands finish' ∧
      Related J K finish finish' ∧ finish.length = finish'.length ∧
      ∃ added, finish' = ys ++ added := by
  obtain ⟨finish', ht, hs⟩ := bisimulation_lifts_trace
    (same_is_bisimulation (finite_outcomes_image_finite fj) (finite_outcomes_image_finite fk)) h trace
  refine ⟨finish', ht, hs, ?_, trace_retains_configuration ht⟩
  rw [trace_length trace, trace_length ht, slots]

theorem singleton_self_question (J : Join F) (x : F) :
    Holds (model J) [x] (.after (0, 0) .top) ↔ ExplanatoryJoiningAnchors.SelfJoinable J x := by
  constructor
  · rintro ⟨ys, hs, _⟩
    obtain ⟨a, b, z, ha, hb, hj, _⟩ := hs
    have ea : x = a := Option.some.inj ha
    have eb : x = b := Option.some.inj hb
    subst a; subst b
    exact ⟨z, hj⟩
  · rintro ⟨z, hz⟩
    exact ⟨[x] ++ [z], ⟨x, x, z, rfl, rfl, hz, rfl⟩, True.intro⟩

theorem retained_question_corrects_coarse_failure :
    Holds (model ExplanatoryJoiningAnchors.coarseJoin) [()] (.after (0, 0) .top) ∧
    ¬ Holds (model (traceJoin ExplanatoryJoining.budgetProcess)) [ExplanatoryJoiningAnchors.spent]
      (.after (0, 0) .top) := by
  constructor
  · exact (singleton_self_question _ _).mpr ExplanatoryJoiningAnchors.retained_anchor_separates.1
  · intro h
    exact ExplanatoryJoiningAnchors.retained_anchor_separates.2 ((singleton_self_question _ _).mp h)

theorem coarse_failure_not_related :
    ¬ Related (traceJoin ExplanatoryJoining.budgetProcess) ExplanatoryJoiningAnchors.coarseJoin
      [ExplanatoryJoiningAnchors.spent] [()] := by
  intro h
  exact retained_question_corrects_coarse_failure.2
    ((h (.after (0, 0) .top)).mpr retained_question_corrects_coarse_failure.1)

theorem idle_self_question {S : Type u} {A : Type v} (P : Process S A) (s : S) :
    Holds (model (traceJoin P)) [traceIdle P s] (.after (0, 0) .top) := by
  apply (singleton_self_question _ _).mpr
  exact ⟨traceIdle P s, ExplanatoryJoining.joined_idle_left (ExplanatoryJoining.idle_valid P s)⟩

/-- Within ONE admitted process, exact accounts must retain this difference.
No minimality, finite-fiber premise or independent success predicate is used. -/
theorem every_exact_account_retains_real_difference {C : Type}
    (p : ExplanatoryUniqueness.Presentation
      (List (Admitted ExplanatoryJoining.budgetProcess)) (Test Command Empty) C)
    (hp : ExplanatoryUniqueness.Exact (Holds (model (traceJoin ExplanatoryJoining.budgetProcess))) p) :
    p.encode [traceIdle ExplanatoryJoining.budgetProcess false] ≠
      p.encode [ExplanatoryJoiningAnchors.spent] := by
  intro h
  have same := ExplanatoryUniqueness.equal_codes_same_answers hp h
  exact retained_question_corrects_coarse_failure.2
    ((same (.after (0, 0) .top)).mp (idle_self_question ExplanatoryJoining.budgetProcess false))

end Generative.ExplanatoryJoiningRegisters

#print axioms Generative.ExplanatoryJoiningRegisters.finite_outcomes_image_finite
#print axioms Generative.ExplanatoryJoiningRegisters.retained_pair_result_matches
#print axioms Generative.ExplanatoryJoiningRegisters.step_retains_configuration
#print axioms Generative.ExplanatoryJoiningRegisters.trace_retains_configuration
#print axioms Generative.ExplanatoryJoiningRegisters.trace_length
#print axioms Generative.ExplanatoryJoiningRegisters.retained_history_matches
#print axioms Generative.ExplanatoryJoiningRegisters.singleton_self_question
#print axioms Generative.ExplanatoryJoiningRegisters.retained_question_corrects_coarse_failure
#print axioms Generative.ExplanatoryJoiningRegisters.coarse_failure_not_related
#print axioms Generative.ExplanatoryJoiningRegisters.idle_self_question
#print axioms Generative.ExplanatoryJoiningRegisters.every_exact_account_retains_real_difference
