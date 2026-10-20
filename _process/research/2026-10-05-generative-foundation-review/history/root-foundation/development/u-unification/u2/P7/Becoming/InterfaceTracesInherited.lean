import Becoming.InterfaceTraces

/-!
# Selecting a listed plan on a probing interface's process (periphery-join ring)

`AlignmentInquiry` selects the first listed plan valid for a listed belief
(`AlignmentInquiry.choose`): some plan is selected exactly when some listed plan is valid
(`chosen_exists_iff`), none is exactly when every listed plan is invalid
(`no_listed_policy_iff`), and a selected plan completes from every configuration believed
(`chosen_sound`). `Becoming.InterfaceTraces` reads the interface as a process and a plan's
validity as completion by a trace of its two moves from every configuration of a nonempty belief
(`valid_iff`). This module states the selection laws of that process.

* **Some plan is selected exactly when some listed plan completes from every configuration of a
  nonempty belief**, its execution a trace of the interface's process (`selected_iff_completes`).
* **No plan is selected exactly when no listed plan does** (`none_selected_iff`).
* **A selected plan is listed and completes from every configuration believed**
  (`selected_completes`).

No ethical predicate or ranking occurs. Axioms inherited: `propext` and `Quot.sound`, from
`AlignmentInquiry.chosen_exists_iff`, `AlignmentInquiry.no_listed_policy_iff` and
`AlignmentInquiry.chosen_sound`; nothing else.
-/

namespace Becoming

open Generative AlignmentInquiry InterfaceTraces

namespace InterfaceTracesInherited

variable {S Q A : Type}

theorem false_iff_not : ∀ {b : Bool}, b = false ↔ ¬ b = true
  | true => ⟨fun e => (nomatch e), fun n => absurd rfl n⟩
  | false => ⟨fun _ e => (nomatch e), fun _ => rfl⟩

/-- **Some plan is selected exactly when some listed plan completes from every configuration of
a nonempty belief**, each completion a trace of the interface's process. -/
theorem selected_iff_completes (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    (choose m states plans).isSome = true ↔
      ∃ p, p ∈ plans ∧ states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s :=
  (chosen_exists_iff m states plans).trans
    ⟨fun ⟨p, mem, v⟩ => ⟨p, mem, (valid_iff m states p).mp v⟩,
     fun ⟨p, mem, completes⟩ => ⟨p, mem, (valid_iff m states p).mpr completes⟩⟩

/-- **No plan is selected exactly when no listed plan completes from every configuration of a
nonempty belief.** -/
theorem none_selected_iff (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    choose m states plans = none ↔
      ∀ p, p ∈ plans → ¬ (states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s) :=
  (no_listed_policy_iff m states plans).trans
    ⟨fun all p mem completes => false_iff_not.mp (all p mem) ((valid_iff m states p).mpr completes),
     fun none p mem => false_iff_not.mpr fun v => none p mem ((valid_iff m states p).mp v)⟩

/-- **A selected plan is listed and completes from every configuration believed**, by a trace of
the interface's process reaching an achieved configuration. -/
theorem selected_completes (m : Interface S Q A) (states : List S) (plans : List (Plan Q A))
    {p : Plan Q A} (selected : choose m states plans = some p) :
    states ≠ [] ∧ p ∈ plans ∧ ∀ s, s ∈ states → Completes m p s :=
  match chosen_sound m states plans p selected with
  | ⟨nonempty, mem, all⟩ => ⟨nonempty, mem, fun s believed =>
      match all s believed with
      | ⟨t, ran, achieved⟩ => match (run_iff_trace m p s t).mp ran with
        | ⟨answer, path⟩ => ⟨answer, t, path, achieved⟩⟩

end InterfaceTracesInherited

end Becoming
