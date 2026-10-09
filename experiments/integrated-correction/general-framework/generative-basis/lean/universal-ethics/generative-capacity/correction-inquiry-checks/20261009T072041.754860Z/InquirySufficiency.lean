import GenerativeCore

/-!
# Bounded sufficient inquiry through actual changing configurations

This is a contract over the existing Process law, not a new event law or an
installed planner. States must retain every effect and historical target needed
by the question. `safe` and `goal` are independently declared local contracts;
their meaning, authority and acquisition are not established here. A response
is one common finite event word, with progress and safety at every possible
prefix. The observation interface includes all information available to branch.

On arbitrary predicate-valued beliefs, finiteness of observations does not
decide whether a branch is empty. The constructive recurrence explicitly carries
an empty/live alternative. A later theorem recovers the usual implication form
when those alternatives are available; finite enumeration supplies them without
a logical axiom. Empty initial belief is never usable sufficiency.
-/

namespace Generative.InquirySufficiency

universe u v w

variable {State : Type u} {Action : Type v} {Response : Type w}

def InhabitedBelief (B : State → Prop) : Prop := ∃ s, B s
def EmptyBelief (B : State → Prop) : Prop := ∀ s, ¬ B s

/-- Every prescribed event is available, every admitted successor is safe and
continues, and every completed endpoint meets the declared requirement. -/
def Completes (P : Process State Action) (safe : State → Action → State → Prop)
    (goal : State → Prop) : State → List Action → Prop
  | s, [] => goal s
  | s, a :: rest => Enabled P s a ∧
      ∀ t, P.step s a t → safe s a t ∧ Completes P safe goal t rest

inductive SafeTrace (P : Process State Action) (safe : State → Action → State → Prop) :
    State → List Action → State → Prop
  | nil (s) : SafeTrace P safe s [] s
  | cons {s middle t a rest} (step : P.step s a middle) (condition : safe s a middle)
      (tail : SafeTrace P safe middle rest t) : SafeTrace P safe s (a :: rest) t

variable {P : Process State Action} {safe : State → Action → State → Prop}
variable {goal : State → Prop}

theorem completes_has_actual_endpoint {s : State} {word : List Action}
    (h : Completes P safe goal s word) :
    ∃ t, Trace P s word t ∧ goal t := by
  induction word generalizing s with
  | nil => exact ⟨s, .nil s, h⟩
  | cons a rest ih =>
    obtain ⟨middle, hstep⟩ := h.1
    obtain ⟨t, ht, hg⟩ := ih (h.2 middle hstep).2
    exact ⟨t, .cons hstep ht, hg⟩

theorem completes_every_actual_endpoint {s t : State} {word : List Action}
    (h : Completes P safe goal s word) (actual : Trace P s word t) : goal t := by
  induction actual with
  | nil => exact h
  | cons step tail ih => exact ih (h.2 _ step).2

theorem completes_all_actual_steps_safe {s t : State} {word : List Action}
    (h : Completes P safe goal s word) (actual : Trace P s word t) :
    SafeTrace P safe s word t := by
  induction actual with
  | nil => exact .nil _
  | cons step tail ih => exact .cons step (h.2 _ step).1 (ih (h.2 _ step).2)

/-- Every actual prefix retains the sufficient remaining continuation. Thus a
favorable complete path cannot conceal a different admitted deadlocked prefix. -/
theorem completes_after_actual_prefix {s current : State}
    {past future : List Action} (h : Completes P safe goal s (past ++ future))
    (actual : Trace P s past current) : Completes P safe goal current future := by
  induction actual with
  | nil => exact h
  | cons step tail ih => exact ih (h.2 _ step).2

theorem completes_append_iff (s : State) (past future : List Action) :
    Completes P safe goal s (past ++ future) ↔
      Completes P safe (fun t => Completes P safe goal t future) s past := by
  induction past generalizing s with
  | nil => exact Iff.rfl
  | cons a rest ih =>
    constructor
    · intro h
      exact ⟨h.1, fun t step => ⟨(h.2 t step).1, (ih t).mp (h.2 t step).2⟩⟩
    · intro h
      exact ⟨h.1, fun t step => ⟨(h.2 t step).1, (ih t).mpr (h.2 t step).2⟩⟩

variable {k : Nat} {sense : State → Action → State → Fin k}

/-- Possibilities are transported to actual successors before evidence filters
them. Any relevant initial label must remain a coordinate of State. -/
def After (P : Process State Action) (sense : State → Action → State → Fin k)
    (B : State → Prop) (a : Action) (o : Fin k) (t : State) : Prop :=
  ∃ s, B s ∧ P.step s a t ∧ sense s a t = o

def InquiryAdmissible (P : Process State Action) (safe : State → Action → State → Prop)
    (B : State → Prop) (a : Action) : Prop :=
  ∀ s, B s → Enabled P s a ∧ ∀ t, P.step s a t → safe s a t

def CommonResponse (P : Process State Action) (safe : State → Action → State → Prop)
    (goal : State → Prop) (response : Response → List Action)
    (B : State → Prop) (r : Response) : Prop :=
  ∀ s, B s → Completes P safe goal s (response r)

/-- Finite syntax independent of the sufficiency recurrence. Fin k branches
make each node finite; `abort` denotes only an unreachable branch. -/
inductive Policy (Action : Type v) (Response : Type w) (k : Nat) where
  | abort
  | respond (r : Response)
  | inquire (a : Action) (next : Fin k → Policy Action Response k)

def Within : Nat → Policy Action Response k → Prop
  | _, .abort => True
  | _, .respond _ => True
  | 0, .inquire _ _ => False
  | n + 1, .inquire _ next => ∀ o, Within n (next o)

def Sound (P : Process State Action) (safe : State → Action → State → Prop)
    (goal : State → Prop) (sense : State → Action → State → Fin k)
    (response : Response → List Action) : Policy Action Response k → (State → Prop) → Prop
  | .abort, B => EmptyBelief B
  | .respond r, B => InhabitedBelief B ∧ CommonResponse P safe goal response B r
  | .inquire a next, B => InhabitedBelief B ∧ InquiryAdmissible P safe B a ∧
      ∀ o, Sound P safe goal sense response (next o) (After P sense B a o)

def Sufficient (P : Process State Action) (safe : State → Action → State → Prop)
    (goal : State → Prop) (sense : State → Action → State → Fin k)
    (response : Response → List Action) : Nat → (State → Prop) → Prop
  | 0, B => InhabitedBelief B ∧ ∃ r, CommonResponse P safe goal response B r
  | n + 1, B => InhabitedBelief B ∧
      ((∃ r, CommonResponse P safe goal response B r) ∨
        ∃ a, InquiryAdmissible P safe B a ∧ ∀ o,
          EmptyBelief (After P sense B a o) ∨
            Sufficient P safe goal sense response n (After P sense B a o))

variable {response : Response → List Action}

/-- Direct finite-table construction avoids the standard Fin.cases helper's
propositional-extensionality dependency. This is not a new physical updater. -/
def finiteCons {α : Type u} {n : Nat} (first : α) (rest : Fin n → α) : Fin (n + 1) → α
  | ⟨0, _⟩ => first
  | ⟨i + 1, bound⟩ => rest ⟨i, Nat.lt_of_succ_lt_succ bound⟩

/-- Constructive finite choice of policy witnesses; no infinite choice or
decidability of an arbitrary proposition is used. -/
theorem finite_choice {α : Type u} {n : Nat} (R : Fin n → α → Prop)
    (h : ∀ i, ∃ x, R i x) : ∃ f : Fin n → α, ∀ i, R i (f i) := by
  induction n with
  | zero => exact ⟨fun i => Fin.elim0 i, fun i => Fin.elim0 i⟩
  | succ n ih =>
    obtain ⟨first, hfirst⟩ := h ⟨0, Nat.zero_lt_succ n⟩
    obtain ⟨rest, hrest⟩ := ih (fun i x => R i.succ x) (fun i => h i.succ)
    refine ⟨finiteCons first rest, ?_⟩
    intro ⟨i, hi⟩
    cases i with
    | zero => exact hfirst
    | succ i => exact hrest ⟨i, Nat.lt_of_succ_lt_succ hi⟩

theorem bounded_sound_empty_or_sufficient (n : Nat) (policy : Policy Action Response k)
    (B : State → Prop) (bound : Within n policy)
    (sound : Sound P safe goal sense response policy B) :
    EmptyBelief B ∨ Sufficient P safe goal sense response n B := by
  induction n generalizing policy B with
  | zero =>
    cases policy with
    | abort => exact Or.inl sound
    | respond r => exact Or.inr ⟨sound.1, r, sound.2⟩
    | inquire a next => exact False.elim bound
  | succ n ih =>
    cases policy with
    | abort => exact Or.inl sound
    | respond r => exact Or.inr ⟨sound.1, Or.inl ⟨r, sound.2⟩⟩
    | inquire a next =>
      exact Or.inr ⟨sound.1, Or.inr ⟨a, sound.2.1,
        fun o => ih (next o) _ (bound o) (sound.2.2 o)⟩⟩

theorem sufficient_has_bounded_policy {n : Nat} {B : State → Prop}
    (h : Sufficient P safe goal sense response n B) :
    ∃ policy, Within n policy ∧ Sound P safe goal sense response policy B := by
  induction n generalizing B with
  | zero =>
    obtain ⟨r, hr⟩ := h.2
    exact ⟨.respond r, True.intro, h.1, hr⟩
  | succ n ih =>
    rcases h.2 with terminal | ⟨a, admissible, branches⟩
    · obtain ⟨r, hr⟩ := terminal
      exact ⟨.respond r, True.intro, h.1, hr⟩
    · have each : ∀ o, ∃ policy : Policy Action Response k,
          Within n policy ∧ Sound P safe goal sense response policy (After P sense B a o) := by
        intro o
        rcases branches o with empty | live
        · exact ⟨.abort, by cases n <;> exact True.intro, empty⟩
        · exact ih live
      obtain ⟨next, hnext⟩ := finite_choice _ each
      exact ⟨.inquire a next, fun o => (hnext o).1,
        h.1, admissible, fun o => (hnext o).2⟩

theorem sufficiency_iff_bounded_policy (n : Nat) (B : State → Prop) :
    Sufficient P safe goal sense response n B ↔
      InhabitedBelief B ∧ ∃ policy,
        Within n policy ∧ Sound P safe goal sense response policy B := by
  constructor
  · intro h
    have nonempty : InhabitedBelief B := by cases n <;> exact h.1
    exact ⟨nonempty, sufficient_has_bounded_policy h⟩
  · rintro ⟨⟨s, hs⟩, policy, bound, sound⟩
    rcases bounded_sound_empty_or_sufficient n policy B bound sound with empty | enough
    · exact False.elim (empty s hs)
    · exact enough

theorem empty_belief_not_sufficient (n : Nat) {B : State → Prop}
    (empty : EmptyBelief B) : ¬ Sufficient P safe goal sense response n B := by
  intro h
  obtain ⟨s, hs⟩ := ((sufficiency_iff_bounded_policy n B).mp h).1
  exact empty s hs

/-- The usual mathematical implication form. On arbitrary predicates this does
not itself provide the empty/live classification needed to fill a finite tree. -/
def ImplicationSufficient (P : Process State Action) (safe : State → Action → State → Prop)
    (goal : State → Prop) (sense : State → Action → State → Fin k)
    (response : Response → List Action) : Nat → (State → Prop) → Prop
  | 0, B => InhabitedBelief B ∧ ∃ r, CommonResponse P safe goal response B r
  | n + 1, B => InhabitedBelief B ∧
      ((∃ r, CommonResponse P safe goal response B r) ∨
        ∃ a, InquiryAdmissible P safe B a ∧ ∀ o,
          InhabitedBelief (After P sense B a o) →
            ImplicationSufficient P safe goal sense response n (After P sense B a o))

/-- An explicit constructive interface, required only to the declared depth.
It is tested/supplied for the representation, not asserted of every process. -/
def ClassifiedThrough (P : Process State Action)
    (sense : State → Action → State → Fin k) : Nat → (State → Prop) → Prop
  | 0, _ => True
  | n + 1, B => ∀ a o,
      (EmptyBelief (After P sense B a o) ∨ InhabitedBelief (After P sense B a o)) ∧
      ClassifiedThrough P sense n (After P sense B a o)

theorem empty_or_inhabited_of_decidable {B : State → Prop}
    (decision : Decidable (InhabitedBelief B)) : EmptyBelief B ∨ InhabitedBelief B := by
  cases decision with
  | isTrue h => exact Or.inr h
  | isFalse h => exact Or.inl (fun s hs => h ⟨s, hs⟩)

/-- Exact finite enumeration decides nonemptiness without equality testing or
excluded middle. Finding such an enumeration is a separate model obligation. -/
def nonemptyDecisionFromList (B : State → Prop) (states : List State)
    (enumerates : ∀ s, B s ↔ s ∈ states) : Decidable (InhabitedBelief B) := by
  cases states with
  | nil =>
    exact isFalse (fun ⟨s, hs⟩ => by cases (enumerates s).mp hs)
  | cons first rest =>
    exact isTrue ⟨first, (enumerates first).mpr (List.Mem.head rest)⟩

theorem sufficiency_iff_implication_form (n : Nat) (B : State → Prop)
    (classified : ClassifiedThrough P sense n B) :
    Sufficient P safe goal sense response n B ↔
      ImplicationSufficient P safe goal sense response n B := by
  induction n generalizing B with
  | zero => exact Iff.rfl
  | succ n ih =>
    constructor
    · intro h
      refine ⟨h.1, ?_⟩
      rcases h.2 with terminal | ⟨a, admissible, branches⟩
      · exact Or.inl terminal
      · refine Or.inr ⟨a, admissible, ?_⟩
        intro o live
        rcases branches o with empty | enough
        · obtain ⟨s, hs⟩ := live
          exact False.elim (empty s hs)
        · exact (ih _ (classified a o).2).mp enough
    · intro h
      refine ⟨h.1, ?_⟩
      rcases h.2 with terminal | ⟨a, admissible, branches⟩
      · exact Or.inl terminal
      · refine Or.inr ⟨a, admissible, ?_⟩
        intro o
        rcases (classified a o).1 with empty | live
        · exact Or.inl empty
        · exact Or.inr ((ih _ (classified a o).2).mpr (branches o live))

/-- Actual policy execution uses the very same native steps. It assumes their
occurrence; later existence/safety results do not impose a scheduler. -/
inductive Execution (P : Process State Action) (sense : State → Action → State → Fin k)
    (response : Response → List Action) : Policy Action Response k → State → List Action → State → Prop
  | respond {r s t} (actual : Trace P s (response r) t) :
      Execution P sense response (.respond r) s (response r) t
  | inquire {a next s middle tail t}
      (step : P.step s a middle)
      (later : Execution P sense response (next (sense s a middle)) middle tail t) :
      Execution P sense response (.inquire a next) s (a :: tail) t

theorem execution_is_actual_trace {policy : Policy Action Response k}
    {s t : State} {word : List Action}
    (h : Execution P sense response policy s word t) : Trace P s word t := by
  induction h with
  | respond actual => exact actual
  | inquire step later ih => exact .cons step ih

theorem sound_execution_meets_goal {policy : Policy Action Response k}
    {B : State → Prop} {s t : State} {word : List Action}
    (sound : Sound P safe goal sense response policy B) (member : B s)
    (actual : Execution P sense response policy s word t) : goal t := by
  induction actual generalizing B with
  | respond trace => exact completes_every_actual_endpoint (sound.2 _ member) trace
  | @inquire a next s middle tail t step later ih =>
    exact ih (sound.2.2 _) ⟨s, member, step, rfl⟩

theorem sound_execution_preserves_every_prefix_condition {policy : Policy Action Response k}
    {B : State → Prop} {s t : State} {word : List Action}
    (sound : Sound P safe goal sense response policy B) (member : B s)
    (actual : Execution P sense response policy s word t) : SafeTrace P safe s word t := by
  induction actual generalizing B with
  | respond trace => exact completes_all_actual_steps_safe (sound.2 _ member) trace
  | @inquire a next s middle tail t step later ih =>
    exact .cons step ((sound.2.1 s member).2 middle step)
      (ih (sound.2.2 _) ⟨s, member, step, rfl⟩)

theorem sound_has_actual_execution {policy : Policy Action Response k}
    {B : State → Prop} {s : State}
    (sound : Sound P safe goal sense response policy B) (member : B s) :
    ∃ word t, Execution P sense response policy s word t ∧ goal t := by
  induction policy generalizing B s with
  | abort => exact False.elim (sound s member)
  | respond r =>
    obtain ⟨t, actual, reached⟩ := completes_has_actual_endpoint (sound.2 s member)
    exact ⟨response r, t, .respond actual, reached⟩
  | inquire a next ih =>
    obtain ⟨middle, step⟩ := (sound.2.1 s member).1
    obtain ⟨word, t, actual, reached⟩ :=
      ih (sense s a middle) (sound.2.2 _) ⟨s, member, step, rfl⟩
    exact ⟨a :: word, t, .inquire step actual, reached⟩

end Generative.InquirySufficiency

#print axioms Generative.InquirySufficiency.completes_has_actual_endpoint
#print axioms Generative.InquirySufficiency.completes_every_actual_endpoint
#print axioms Generative.InquirySufficiency.completes_all_actual_steps_safe
#print axioms Generative.InquirySufficiency.completes_after_actual_prefix
#print axioms Generative.InquirySufficiency.completes_append_iff
#print axioms Generative.InquirySufficiency.finite_choice
#print axioms Generative.InquirySufficiency.bounded_sound_empty_or_sufficient
#print axioms Generative.InquirySufficiency.sufficient_has_bounded_policy
#print axioms Generative.InquirySufficiency.sufficiency_iff_bounded_policy
#print axioms Generative.InquirySufficiency.empty_belief_not_sufficient
#print axioms Generative.InquirySufficiency.empty_or_inhabited_of_decidable
#print axioms Generative.InquirySufficiency.nonemptyDecisionFromList
#print axioms Generative.InquirySufficiency.sufficiency_iff_implication_form
#print axioms Generative.InquirySufficiency.execution_is_actual_trace
#print axioms Generative.InquirySufficiency.sound_execution_meets_goal
#print axioms Generative.InquirySufficiency.sound_execution_preserves_every_prefix_condition
#print axioms Generative.InquirySufficiency.sound_has_actual_execution
