import Std

/-!
Learning, assessment and transfer of a standard relative to fixed content.
All candidates, acquisition laws, meanings and exact-answer scope are supplied.
The source does not define understanding or moral authority by a successful test.
No true-rule field is exposed to the answer procedure; acquired observations filter
its candidate repertoire. Actual law and observed answers belong to one history.
-/
namespace Generative.StandardsBridge

abbrev Observation (Q : Type) := Q × Bool
abbrev Rule (Q : Type) := Q → Bool

def Fits {Q : Type} (h : Rule Q) (evidence : List (Observation Q)) : Prop :=
  ∀ o ∈ evidence, h o.1 = o.2

def revise {Q : Type} (hs : List (Rule Q)) (o : Observation Q) : List (Rule Q) :=
  hs.filter (fun h => h o.1 == o.2)

def learn {Q : Type} : List (Rule Q) → List (Observation Q) → List (Rule Q)
  | hs, [] => hs
  | hs, o :: os => learn (revise hs o) os

-- Abstain both on conflict and on an empty (inconsistent) candidate repertoire.
def answer {Q : Type} (hs : List (Rule Q)) (q : Q) : Option Bool :=
  match hs with
  | [] => none
  | h :: tail => if tail.all (fun g => g q == h q) then some (h q) else none

-- These are answer-domain conditions, not definitions of knowledge or authority.
def Safe {Q : Type} (hs : List (Rule Q)) (a : Q → Option Bool) : Prop :=
  ∀ h ∈ hs, ∀ q b, a q = some b → b = h q

def Maximal {Q : Type} (hs : List (Rule Q)) (a : Q → Option Bool) : Prop :=
  ∀ other, Safe hs other → ∀ q b, other q = some b → a q = some b

theorem mem_revise {Q : Type} (h : Rule Q) (hs : List (Rule Q)) (o : Observation Q) :
    h ∈ revise hs o ↔ h ∈ hs ∧ h o.1 = o.2 := by simp [revise]

theorem mem_learn {Q : Type} (h : Rule Q) (hs : List (Rule Q))
    (evidence : List (Observation Q)) :
    h ∈ learn hs evidence ↔ h ∈ hs ∧ Fits h evidence := by
  induction evidence generalizing hs with
  | nil => simp [learn, Fits]
  | cons o os ih =>
    simp only [learn, ih, mem_revise, Fits, List.mem_cons, forall_eq_or_imp]
    exact and_assoc

theorem actual_rule_retained {Q : Type} (actual : Rule Q) (hs : List (Rule Q))
    (evidence : List (Observation Q)) (included : actual ∈ hs)
    (faithful : Fits actual evidence) : actual ∈ learn hs evidence := by
  exact (mem_learn actual hs evidence).2 ⟨included, faithful⟩

theorem eliminated_rule_has_counterevidence {Q : Type} (h : Rule Q)
    (hs : List (Rule Q)) (evidence : List (Observation Q))
    (included : h ∈ hs) (removed : h ∉ learn hs evidence) :
    ∃ o ∈ evidence, h o.1 ≠ o.2 := by
  classical
  have bad : ¬ Fits h evidence := fun fit => removed ((mem_learn h hs evidence).2 ⟨included, fit⟩)
  by_contra absent
  apply bad
  intro o ho
  by_contra mismatch
  exact absent ⟨o, ho, mismatch⟩

theorem repetition_does_not_change_candidates {Q : Type} (hs : List (Rule Q))
    (o : Observation Q) : revise (revise hs o) o = revise hs o := by
  simp [revise, List.filter_filter]

theorem answer_iff {Q : Type} (hs : List (Rule Q)) (q : Q) (b : Bool) :
    answer hs q = some b ↔ hs ≠ [] ∧ ∀ h ∈ hs, h q = b := by
  cases hs with
  | nil => simp [answer]
  | cons h tail =>
    simp only [answer]
    split
    · rename_i agree
      have allAgree : ∀ g ∈ tail, g q = h q := by simpa using agree
      simp only [Option.some.injEq, List.cons_ne_nil, ne_eq, not_false_eq_true,
        true_and, List.mem_cons, forall_eq_or_imp]
      constructor
      · intro hb
        exact ⟨hb, fun g hg => (allAgree g hg).trans hb⟩
      · intro hb
        exact hb.1
    · rename_i disagree
      have notAll : ¬ (∀ g ∈ tail, g q = h q) := by simpa using disagree
      constructor
      · intro impossible
        cases impossible
      · rintro ⟨_, common⟩
        exact False.elim (notAll (fun g hg => (common g (by simp [hg])).trans (common h (by simp)).symm))

theorem answer_safe {Q : Type} (hs : List (Rule Q)) : Safe hs (answer hs) := by
  intro h hh q b hb
  exact ((answer_iff hs q b).1 hb).2 h hh |>.symm

theorem safe_definite_requires_agreement {Q : Type} (hs : List (Rule Q))
    (a : Q → Option Bool) (safe : Safe hs a) (nonempty : hs ≠ []) (q : Q) (b : Bool)
    (asserts : a q = some b) : answer hs q = some b := by
  exact (answer_iff hs q b).2 ⟨nonempty, fun h hh => (safe h hh q b asserts).symm⟩

theorem answer_maximal {Q : Type} (hs : List (Rule Q)) (nonempty : hs ≠ []) :
    Maximal hs (answer hs) := by
  intro a safe q b hb
  exact safe_definite_requires_agreement hs a safe nonempty q b hb

theorem unique_maximal_safe {Q : Type} (hs : List (Rule Q)) (nonempty : hs ≠ [])
    (a : Q → Option Bool) (safe : Safe hs a) (maximal : Maximal hs a) : a = answer hs := by
  funext q
  cases h : a q with
  | some b => exact (safe_definite_requires_agreement hs a safe nonempty q b h).symm
  | none =>
    cases ha : answer hs q with
    | none => rfl
    | some b => have bad := maximal (answer hs) (answer_safe hs) q b ha; simp [h] at bad

theorem known_rule_makes_answer_correct {Q : Type} (actual : Rule Q)
    (hs : List (Rule Q)) (evidence : List (Observation Q))
    (included : actual ∈ hs) (faithful : Fits actual evidence) (q : Q) (b : Bool)
    (asserts : answer (learn hs evidence) q = some b) : b = actual q := by
  exact answer_safe _ actual (actual_rule_retained actual hs evidence included faithful) q b asserts

-- Actual acquisition consumes support; it does not admit invented labels.
def acquire {Q : Type} (actual : Rule Q) : Nat → List Q → List (Observation Q)
  | 0, _ => []
  | _ + 1, [] => []
  | fuel + 1, q :: qs => (q, actual q) :: acquire actual fuel qs

theorem acquired_evidence_faithful {Q : Type} (actual : Rule Q) (fuel : Nat) (qs : List Q) :
    Fits actual (acquire actual fuel qs) := by
  induction fuel generalizing qs with
  | zero => simp [acquire, Fits]
  | succ fuel ih =>
    cases qs with
    | nil => simp [acquire, Fits]
    | cons q qs =>
      intro o ho
      simp only [acquire, List.mem_cons] at ho
      rcases ho with rfl | ho
      · rfl
      · exact ih qs o ho

theorem acquired_answers_correct {Q : Type} (actual : Rule Q) (hs : List (Rule Q))
    (included : actual ∈ hs) (fuel : Nat) (qs : List Q) (q : Q) (b : Bool)
    (asserts : answer (learn hs (acquire actual fuel qs)) q = some b) : b = actual q := by
  exact known_rule_makes_answer_correct actual hs _ included
    (acquired_evidence_faithful actual fuel qs) q b asserts

-- Different tokens can carry the same question when an actual decoding relation
-- is supplied. This preserves a standard; it does not derive semantic content.
def transport {Q R : Type} (decode : R → Q) (h : Rule Q) : Rule R := h ∘ decode

theorem answer_transport {Q R : Type} (hs : List (Rule Q)) (decode : R → Q)
    (r : R) : answer (hs.map (transport decode)) r = answer hs (decode r) := by
  cases hs with
  | nil => rfl
  | cons h tail => simp [answer, List.all_map, transport, Function.comp_def]

theorem learning_transport {Q R : Type} (hs : List (Rule Q)) (e : List (Observation Q))
    (encode : Q → R) (decode : R → Q) (faithful : ∀ q, decode (encode q) = q) :
    learn (hs.map (transport decode)) (e.map (fun o => (encode o.1, o.2))) =
      (learn hs e).map (transport decode) := by
  induction e generalizing hs with
  | nil => rfl
  | cons o os ih =>
    simp only [List.map_cons, learn]
    have hr : revise (hs.map (transport decode)) (encode o.1, o.2) =
        (revise hs o).map (transport decode) := by
      simp [revise, List.filter_map, transport, Function.comp_def, faithful]
    rw [hr, ih]

theorem wrong_reencoding_breaks_transfer :
    answer ([(id : Rule Bool)].map (transport (fun b => !b))) true ≠
      answer [id] true := by decide

-- Concrete acquired comparison: four candidate rules over two observable cases.
def repertoire : List (Rule Bool) := [id, fun b => !b, fun _ => true, fun _ => false]
theorem bool_repertoire_complete (h : Rule Bool) : h ∈ repertoire := by
  cases hf : h false <;> cases ht : h true
  · have eqh : h = fun _ => false := by funext b; cases b <;> assumption
    simp [repertoire, eqh]
  · have eqh : h = id := by funext b; cases b <;> assumption
    simp [repertoire, eqh]
  · have eqh : h = fun b => !b := by funext b; cases b <;> assumption
    simp [repertoire, eqh]
  · have eqh : h = fun _ => true := by funext b; cases b <;> assumption
    simp [repertoire, eqh]

theorem full_bool_repertoire_correct (actual : Rule Bool) (fuel : Nat)
    (qs : List Bool) (q b : Bool)
    (asserts : answer (learn repertoire (acquire actual fuel qs)) q = some b) :
    b = actual q := by
  exact acquired_answers_correct actual repertoire (bool_repertoire_complete actual) fuel qs q b asserts

def oneSample : List (Observation Bool) := acquire id 1 [true, false]
def twoSamples : List (Observation Bool) := acquire id 2 [true, false]

theorem before_acquisition_abstains : answer repertoire true = none := by decide

theorem one_sample_leaves_other_case_unsettled :
    answer (learn repertoire oneSample) true = some true ∧
    answer (learn repertoire oneSample) false = none := by decide

theorem contrasting_acquisition_settles_both :
    answer (learn repertoire twoSamples) true = some true ∧
    answer (learn repertoire twoSamples) false = some false := by decide

theorem learned_response_differs_from_last_report :
    twoSamples.getLast? = some (false, false) ∧
    answer (learn repertoire twoSamples) true = some true := by decide

theorem repeated_same_case_does_not_settle_other :
    answer (learn repertoire (acquire id 2 [true, true])) false = none := by decide

theorem insufficient_support_retains_ambiguity :
    answer (learn repertoire (acquire id 1 [true, false])) false = none := by decide

theorem wrong_model_class_can_be_confidently_wrong :
    let restricted : List (Rule Bool) := [fun _ => true]
    answer (learn restricted (acquire id 1 [true])) false = some true ∧
    (id : Rule Bool) false = false := by decide

theorem inconsistent_evidence_yields_no_answer :
    answer (learn repertoire [(true, true), (true, false)]) false = none := by decide

-- Entirely faithful predictions and rule use do not establish cognitive grasp:
-- these definitions deliberately contain no such predicate or ethical verdict.
end Generative.StandardsBridge
