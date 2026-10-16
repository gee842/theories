import Becoming.Frame
import InquirySufficiency

/-!
# The visible scope of an inquiry, defined by the dynamics

`InquirySufficiency` already supplies common responses, evidence narrowing (`After`),
sound bounded policies and their actual executions over the core process. This
module does not redefine them. It adds one notion that the ethics layer otherwise
supplies as a free parameter, the scope a response is judged over, and shows that
a static judgment needs no notion of its own.

The scope of a policy from a belief is the set of configurations its actual
executions reach from believed configurations. It is fixed by the process, the
observations and the policy, not chosen after the conclusion. A sound policy secures
its goal on every configuration of its scope, the scope is reached by actual paths,
it is nonempty whenever the belief is inhabited, and it shrinks as belief narrows.
A judgment under uncertainty, a response admissible at every configuration
believed possible, is a one-step inquiry: judging takes an admissible response at
the configuration under judgment and closes, and a common response of that process
is exactly a response admissible at every believed configuration.
Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v w

variable {S : Type u} {A : Type v} {R : Type w} {k : Nat}

/-- Configurations reached by actual executions of the policy from believed ones. -/
def Scope (P : Process S A) (sense : S → A → S → Fin k) (response : R → List A)
    (B : S → Prop) (policy : Policy A R k) (t : S) : Prop :=
  ∃ s word, B s ∧ Execution P sense response policy s word t

variable {P : Process S A} {sense : S → A → S → Fin k} {response : R → List A}

/-- A sound policy secures its goal on its whole scope. -/
theorem Scope.secures {safe : S → A → S → Prop} {goal : S → Prop}
    {B : S → Prop} {policy : Policy A R k}
    (sound : Sound P safe goal sense response policy B) :
    ∀ t, Scope P sense response B policy t → goal t
  | _, ⟨_, _, believed, actual⟩ => sound_execution_meets_goal sound believed actual

/-- The scope is reached from the belief by actual paths of the process. -/
theorem Scope.reached {B : S → Prop} {policy : Policy A R k} {t : S} :
    Scope P sense response B policy t → ∃ s, B s ∧ Reach P s t
  | ⟨s, word, believed, actual⟩ => ⟨s, believed, word, execution_is_actual_trace actual⟩

/-- A sound policy has a nonempty scope from every believed configuration. -/
theorem Scope.nonempty {safe : S → A → S → Prop} {goal : S → Prop}
    {B : S → Prop} {policy : Policy A R k} {s : S}
    (sound : Sound P safe goal sense response policy B) (believed : B s) :
    ∃ t, Scope P sense response B policy t ∧ goal t :=
  match sound_has_actual_execution sound believed with
  | ⟨word, t, actual, reached⟩ => ⟨t, ⟨s, word, believed, actual⟩, reached⟩

/-- Narrowing belief narrows the scope. -/
theorem Scope.antitone {B B' : S → Prop} {policy : Policy A R k}
    (narrower : ∀ s, B' s → B s) {t : S} :
    Scope P sense response B' policy t → Scope P sense response B policy t
  | ⟨s, word, believed, actual⟩ => ⟨s, word, narrower s believed, actual⟩

/-- A common response survives narrowing of belief. -/
theorem commonResponse_antitone {safe : S → A → S → Prop} {goal : S → Prop}
    {B B' : S → Prop} {r : R} (narrower : ∀ s, B' s → B s)
    (common : CommonResponse P safe goal response B r) :
    CommonResponse P safe goal response B' r :=
  fun s believed => common s (narrower s believed)

/-! ## A judgment is a one-step inquiry -/

/-- Judging: at a configuration under judgment, an admissible response closes the judgment. -/
def judgeProcess {W : Type u} {H : Type v} (admissible : W → H → Prop) : Process (Option W) H where
  step s a t := ∃ w, s = some w ∧ admissible w a ∧ t = none

/-- Belief over the configurations under judgment. -/
def sees {W : Type u} (B : W → Prop) : Option W → Prop :=
  fun s => ∃ w, B w ∧ s = some w

/-- A response is common to a judgment exactly when it is admissible at every
believed configuration. -/
theorem commonResponse_judge_iff {W : Type u} {H : Type v} {admissible : W → H → Prop}
    {B : W → Prop} {a : H} :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees B) a ↔ ∀ w, B w → admissible w a :=
  ⟨fun common w believed =>
    match common (some w) ⟨w, believed, rfl⟩ with
    | ⟨⟨_, _, same, held, _⟩, _⟩ => Option.some.inj same ▸ held,
   fun all => fun
    | _, ⟨w, believed, rfl⟩ => ⟨⟨none, w, rfl, all w believed, rfl⟩, fun _ _ => ⟨trivial, trivial⟩⟩⟩

end Becoming
