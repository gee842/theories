import Becoming.Frame
import Becoming.Prelude

/-!
# Contingent plans: probe, then respond by the answer

A contingent plan asks one question and responds by its answer. On an interface, probing a
query from a configuration may give an answer and the configuration after it, and responding
from a configuration may give the next one (`Interface`). A plan probes its query and responds
with the branch its answer selects (`Plan`, `branch`, `run`); it passes at a configuration where
its run reaches an achieved one (`passes`). Uncertainty about where the activity stands is a
listed set of configurations (a belief), a plan is valid for it where the belief is not empty
and the plan passes from each configuration listed (`valid`), and the selection takes the first
valid plan of a list (`choose`). The response follows the answer actually obtained; no hidden
index of the configuration selects it.

* **Execution is a trace.** The interface's moves form a process of the spine: probing a query
  with an answer, and responding (`process`). A plan's run ends at `t` exactly where a trace of
  its two moves, for the answer received, leads to `t` (`run_iff_trace`); it passes exactly
  where such a trace reaches an achieved configuration (`passes_iff_completes`), and it is valid
  exactly where the belief is not empty and the plan completes from every configuration listed
  (`valid_iff`).
* **Selection.** Some plan is selected exactly where some listed plan completes from every
  configuration of a nonempty belief (`selected_iff_completes`), none exactly where no listed
  plan does (`none_selected_iff`), and a selected plan is listed and completes from every
  configuration believed (`selected_completes`, `selected_executes`). An empty belief certifies
  no plan (`empty_belief_none`).
* **The repertoire.** Every plan whose query and responses are listed is in the repertoire of
  the lists (`mem_repertoire`).
* **The answer bounds the response.** Equal answers select the same response
  (`branch_congr`), so one response cannot meet two incompatible requirements
  (`branch_incompatible`).

This states `AlignmentInquiry` (8 October) and its joins `InterfaceTraces` and
`InterfaceTracesInherited` in the core (board item F3C, 18 October 2026). It is conventional
finite robust planning; no algorithmic novelty is claimed. No premise; every declaration has an
empty axiom report.
-/

namespace Becoming

open Generative ListTests

namespace ContingentPlans

/-- A plan: a query, and the responses to a negative and to a positive answer. -/
structure Plan (Q A : Type) where
  query : Q
  negative : A
  positive : A
  deriving DecidableEq

/-- The response an answer selects. -/
def branch {Q A : Type} (p : Plan Q A) (answer : Bool) : A :=
  if answer then p.positive else p.negative

/-- An interface: what probing a query and responding give, and which configurations are
achieved. -/
structure Interface (S Q A : Type) where
  probe : S → Q → Option (Bool × S)
  respond : S → A → Option S
  achieved : S → Bool

variable {S Q A : Type}

/-- A plan's run: probe, then respond by the branch of the answer. -/
def run (m : Interface S Q A) (p : Plan Q A) (s : S) : Option S := do
  let (answer, after) ← m.probe s p.query
  m.respond after (branch p answer)

/-- A plan passes at a configuration where its run reaches an achieved one. -/
def passes (m : Interface S Q A) (p : Plan Q A) (s : S) : Bool :=
  (run m p s).any m.achieved

/-- A plan is valid for a listed belief where the belief is not empty and the plan passes from
each configuration listed. -/
def valid (m : Interface S Q A) (states : List S) (p : Plan Q A) : Bool :=
  !states.isEmpty && states.all (passes m p)

/-- The first listed plan valid for the belief. -/
def choose (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    Option (Plan Q A) := plans.find? (valid m states)

/-- Every plan of listed queries and responses. -/
def repertoire (queries : List Q) (actions : List A) : List (Plan Q A) :=
  queries.flatMap (fun q => actions.flatMap (fun a => actions.map (fun b => ⟨q, a, b⟩)))

/-! ## The repertoire and the run -/

/-- **Every plan of listed queries and responses is in the repertoire.** -/
theorem mem_repertoire (qs : List Q) (as : List A) (p : Plan Q A)
    (q : p.query ∈ qs) (a : p.negative ∈ as) (b : p.positive ∈ as) : p ∈ repertoire qs as :=
  match p, q, a, b with
  | ⟨_, _, _⟩, q, a, b =>
    mem_flatMap_iff.mpr ⟨_, q, mem_flatMap_iff.mpr ⟨_, a, mem_map_of b⟩⟩

theorem run_none {m : Interface S Q A} {p : Plan Q A} {s : S}
    (h : m.probe s p.query = none) : run m p s = none := by
  unfold run
  rw [h]
  rfl

theorem run_some {m : Interface S Q A} {p : Plan Q A} {s after : S} {answer : Bool}
    (h : m.probe s p.query = some (answer, after)) :
    run m p s = m.respond after (branch p answer) := by
  unfold run
  rw [h]
  rfl

/-- **A plan passes exactly where its run reaches an achieved configuration.** -/
theorem passes_iff_run (m : Interface S Q A) (p : Plan Q A) (s : S) :
    passes m p s = true ↔ ∃ t, run m p s = some t ∧ m.achieved t = true :=
  option_any_true_iff

/-! ## Execution is a trace -/

/-- **The interface as a process.** Probing query `q` with answer `b` moves to the configuration
the probe returns with that answer; responding with `a` moves to the configuration the response
returns. -/
def process (m : Interface S Q A) : Process S (Sum (Q × Bool) A) :=
  ⟨fun s x t => match x with
    | .inl (q, b) => m.probe s q = some (b, t)
    | .inr a => m.respond s a = some t⟩

/-- The two moves of a plan given an answer. -/
def moves (p : Plan Q A) (answer : Bool) : List (Sum (Q × Bool) A) :=
  [.inl (p.query, answer), .inr (branch p answer)]

/-- A plan completes from a configuration: a trace of its two moves reaches an achieved one. -/
def Completes (m : Interface S Q A) (p : Plan Q A) (s : S) : Prop :=
  ∃ answer t, Trace (process m) s (moves p answer) t ∧ m.achieved t = true

/-- **A plan's run is a trace of the interface's process.** -/
theorem run_iff_trace (m : Interface S Q A) (p : Plan Q A) (s t : S) :
    run m p s = some t ↔ ∃ answer, Trace (process m) s (moves p answer) t :=
  match h : m.probe s p.query with
  | none =>
    ⟨fun ran => (nomatch (run_none h).symm.trans ran),
     fun ⟨_, .cons probed _⟩ => nomatch h.symm.trans probed⟩
  | some (answer, after) =>
    ⟨fun ran => ⟨answer, .cons h (.cons ((run_some h).symm.trans ran) (.nil t))⟩,
     fun ⟨answer', .cons (m := mid) probed (.cons responded rest)⟩ =>
      match rest with
      | .nil _ =>
        have same : (answer, after) = (answer', mid) := Option.some.inj (h.symm.trans probed)
        have sameAnswer : answer = answer' := congrArg Prod.fst same
        have sameAfter : after = mid := congrArg Prod.snd same
        (run_some h).trans (by subst sameAnswer; subst sameAfter; exact responded)⟩

/-- **A plan passes exactly where it completes.** -/
theorem passes_iff_completes (m : Interface S Q A) (p : Plan Q A) (s : S) :
    passes m p s = true ↔ Completes m p s :=
  (passes_iff_run m p s).trans
    ⟨fun ⟨t, ran, achieved⟩ => match (run_iff_trace m p s t).mp ran with
      | ⟨answer, path⟩ => ⟨answer, t, path, achieved⟩,
     fun ⟨answer, t, path, achieved⟩ => ⟨t, (run_iff_trace m p s t).mpr ⟨answer, path⟩, achieved⟩⟩

/-- **A plan is valid exactly where the belief is not empty and the plan completes from every
configuration listed.** -/
theorem valid_iff (m : Interface S Q A) (states : List S) (p : Plan Q A) :
    valid m states p = true ↔ states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s :=
  and_true_iff.trans
    ⟨fun ⟨nonempty, all⟩ => ⟨not_isEmpty_true_iff.mp nonempty,
        fun s m' => (passes_iff_completes m p s).mp (all_true_iff.mp all s m')⟩,
     fun ⟨nonempty, all⟩ => ⟨not_isEmpty_true_iff.mpr nonempty,
        all_true_iff.mpr fun s m' => (passes_iff_completes m p s).mpr (all s m')⟩⟩

/-- A plan is valid exactly where the belief is not empty and the plan passes from every
configuration listed. -/
theorem valid_iff_passes (m : Interface S Q A) (states : List S) (p : Plan Q A) :
    valid m states p = true ↔ states ≠ [] ∧ ∀ s, s ∈ states → passes m p s = true :=
  and_true_iff.trans ⟨fun ⟨n, all⟩ => ⟨not_isEmpty_true_iff.mp n, all_true_iff.mp all⟩,
    fun ⟨n, all⟩ => ⟨not_isEmpty_true_iff.mpr n, all_true_iff.mpr all⟩⟩

/-! ## Selection -/

/-- **Some plan is selected exactly when some listed plan is valid.** -/
theorem chosen_isSome_iff (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    (choose m states plans).isSome = true ↔ ∃ p, p ∈ plans ∧ valid m states p = true :=
  find_isSome_iff

/-- **No plan is selected exactly when every listed plan is invalid.** -/
theorem chosen_none_iff (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    choose m states plans = none ↔ ∀ p, p ∈ plans → valid m states p = false :=
  find_none_iff

/-- **A selected plan is listed, the belief is not empty, and the plan's run reaches an achieved
configuration from every configuration believed.** -/
theorem chosen_sound (m : Interface S Q A) (states : List S) (plans : List (Plan Q A))
    (p : Plan Q A) (h : choose m states plans = some p) :
    states ≠ [] ∧ p ∈ plans ∧ ∀ s, s ∈ states → ∃ t, run m p s = some t ∧ m.achieved t = true :=
  match (valid_iff_passes m states p).mp (find_some h) with
  | ⟨nonempty, all⟩ => ⟨nonempty, mem_of_find_some h,
      fun s m' => (passes_iff_run m p s).mp (all s m')⟩

/-- **An empty belief certifies no plan.** -/
theorem empty_belief_none (m : Interface S Q A) (plans : List (Plan Q A)) :
    choose m [] plans = none :=
  (chosen_none_iff m [] plans).mpr fun _ _ => rfl

/-- **A selected plan's execution from a believed configuration probes, receives an answer and
the configuration after it, responds by the branch of that answer and reaches an achieved
configuration.** -/
theorem selected_executes (m : Interface S Q A) (states : List S) (plans : List (Plan Q A))
    (p : Plan Q A) (s : S) (selection : choose m states plans = some p) (covered : s ∈ states) :
    ∃ answer after final, m.probe s p.query = some (answer, after) ∧
      m.respond after (branch p answer) = some final ∧ m.achieved final = true :=
  match (chosen_sound m states plans p selection).2.2 s covered with
  | ⟨t, ran, goal⟩ =>
    match hp : m.probe s p.query with
    | none => nomatch (run_none hp).symm.trans ran
    | some (answer, after) => ⟨answer, after, t, rfl, (run_some hp).symm.trans ran, goal⟩

/-- **Some plan is selected exactly when some listed plan completes from every configuration of
a nonempty belief.** -/
theorem selected_iff_completes (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    (choose m states plans).isSome = true ↔
      ∃ p, p ∈ plans ∧ states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s :=
  (chosen_isSome_iff m states plans).trans
    ⟨fun ⟨p, mem, v⟩ => ⟨p, mem, (valid_iff m states p).mp v⟩,
     fun ⟨p, mem, completes⟩ => ⟨p, mem, (valid_iff m states p).mpr completes⟩⟩

/-- **No plan is selected exactly when no listed plan completes from every configuration of a
nonempty belief.** -/
theorem none_selected_iff (m : Interface S Q A) (states : List S) (plans : List (Plan Q A)) :
    choose m states plans = none ↔
      ∀ p, p ∈ plans → ¬ (states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s) :=
  (chosen_none_iff m states plans).trans
    ⟨fun all p mem completes => false_iff_not.mp (all p mem) ((valid_iff m states p).mpr completes),
     fun none p mem => false_iff_not.mpr fun v => none p mem ((valid_iff m states p).mp v)⟩

/-- **A selected plan is listed and completes from every configuration believed.** -/
theorem selected_completes (m : Interface S Q A) (states : List S) (plans : List (Plan Q A))
    {p : Plan Q A} (selected : choose m states plans = some p) :
    states ≠ [] ∧ p ∈ plans ∧ ∀ s, s ∈ states → Completes m p s :=
  match chosen_sound m states plans p selected with
  | ⟨nonempty, mem, all⟩ => ⟨nonempty, mem, fun s believed =>
      match all s believed with
      | ⟨t, ran, achieved⟩ => match (run_iff_trace m p s t).mp ran with
        | ⟨answer, path⟩ => ⟨answer, t, path, achieved⟩⟩

/-! ## The answer bounds the response -/

/-- **Equal answers select the same response.** -/
theorem branch_congr (p : Plan Q A) {a b : Bool} (h : a = b) : branch p a = branch p b :=
  congrArg (branch p) h

/-- **One response cannot meet two incompatible requirements.** -/
theorem branch_incompatible (p : Plan Q A) (answer : Bool) (required₁ required₂ : A → Prop)
    (incompatible : ∀ a, required₁ a → ¬ required₂ a) :
    ¬ (required₁ (branch p answer) ∧ required₂ (branch p answer)) :=
  fun ⟨h₁, h₂⟩ => incompatible _ h₁ h₂

end ContingentPlans

end Becoming
