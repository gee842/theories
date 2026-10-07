import CoupledOccurrence

/-!
# Correction relative to actual continuation

A local continuation contract supplies a condition `K` that must hold along the
activity and a terminal condition `G`. They describe the selected activity;
neither is an ethical score, an actor's reward, or a newly derived purpose.

The productive restriction retains exactly those original transitions whose
actual next state still admits a finite contract-fulfilling continuation. Its
exactness theorem preserves the original transitions and their actual joining
states. Restriction cannot create missing capability. Capacity extension can
preserve existing completions without ensuring that they are selected.

Occurrence descriptions additionally retain the full before/after states. A
later successful suffix cannot erase an earlier contract violation from that
same described history. This is an audit interface, not an internal recorder.
-/

namespace Generative.PurposeCorrection

universe u v

variable {State : Type u} {Event : Type v}

/-- Restrict a declared process without inventing a replacement transition. -/
def guarded (P : Process State Event) (K : State → Prop) : Process State Event where
  step s e t := P.step s e t ∧ K s ∧ K t

/-- The source condition matters even for the empty continuation. -/
def ContractTrace (P : Process State Event) (K G : State → Prop)
    (s : State) (events : List Event) (t : State) : Prop :=
  K s ∧ Trace (guarded P K) s events t ∧ G t

/-- Existence of an actual finite completion, not termination of every run. -/
def Viable (P : Process State Event) (K G : State → Prop) (s : State) : Prop :=
  ∃ events t, ContractTrace P K G s events t

/-- Pointwise inclusion: the larger process retains each old transition. -/
def Extends (P Q : Process State Event) : Prop :=
  ∀ s e t, P.step s e t → Q.step s e t

variable {P Q : Process State Event} {K G : State → Prop}

theorem guarded_trace_underlying {s t : State} {events : List Event}
    (h : Trace (guarded P K) s events t) : Trace P s events t := by
  exact trace_map (P := guarded P K) (Q := P) (f := id)
    (fun _ _ _ hs => hs.1) h

theorem guarded_trace_terminal {s t : State} {events : List Event}
    (hs : K s) (h : Trace (guarded P K) s events t) : K t := by
  induction h with
  | nil => exact hs
  | cons hstep _ ih => exact ih hstep.2.2

theorem contract_trace_underlying {s t : State} {events : List Event}
    (h : ContractTrace P K G s events t) : Trace P s events t :=
  guarded_trace_underlying h.2.1

theorem terminal_is_viable {s : State} (hk : K s) (hg : G s) :
    Viable P K G s := ⟨[], s, hk, .nil s, hg⟩

/-- A remaining completion must start at the state actually reached. -/
theorem viable_after_guarded_prefix {s t : State} {events : List Event}
    (hk : K s) (h : Trace (guarded P K) s events t)
    (ht : Viable P K G t) : Viable P K G s := by
  obtain ⟨future, final, _, hfuture, hg⟩ := ht
  exact ⟨events ++ future, final, hk,
    trace_append_iff.mpr ⟨t, h, hfuture⟩, hg⟩

/-- The exact finite continuation contract composes at an actual full state. -/
theorem contract_append_iff {s t : State} {past future : List Event} :
    ContractTrace P K G s (past ++ future) t ↔
      K s ∧ ∃ current, Trace (guarded P K) s past current ∧
        ContractTrace P K G current future t := by
  constructor
  · rintro ⟨hk, h, hg⟩
    obtain ⟨current, hpast, hfuture⟩ := trace_append_iff.mp h
    exact ⟨hk, current, hpast,
      guarded_trace_terminal hk hpast, hfuture, hg⟩
  · rintro ⟨hk, current, hpast, _, hfuture, hg⟩
    exact ⟨hk, trace_append_iff.mpr ⟨current, hpast, hfuture⟩, hg⟩

/-- A mathematical restriction by finite productive possibility. An endogenous
implementation of this restriction requires additional formation evidence. -/
def productiveRestriction (P : Process State Event) (K G : State → Prop) :
    Process State Event where
  step s e t := P.step s e t ∧ K s ∧ Viable P K G t

theorem viable_has_condition {s : State} (h : Viable P K G s) : K s := by
  obtain ⟨_, _, hk, _⟩ := h
  exact hk

theorem productive_trace_guarded {s t : State} {events : List Event}
    (h : Trace (productiveRestriction P K G) s events t) :
    Trace (guarded P K) s events t := by
  exact trace_map (P := productiveRestriction P K G) (Q := guarded P K) (f := id)
    (fun _ _ _ hs => ⟨hs.1, hs.2.1, viable_has_condition hs.2.2⟩) h

theorem productive_trace_terminal_viable {s t : State} {events : List Event}
    (hs : Viable P K G s)
    (h : Trace (productiveRestriction P K G) s events t) : Viable P K G t := by
  induction h with
  | nil => exact hs
  | cons hstep _ ih => exact ih hstep.2.2

/-- No intermediate dead end is hidden by a merely successful endpoint:
the actual suffix from each intermediate state supplies its completion. -/
theorem guarded_trace_to_viable_is_productive {s t : State} {events : List Event}
    (h : Trace (guarded P K) s events t) (ht : Viable P K G t) :
    Trace (productiveRestriction P K G) s events t := by
  induction h with
  | nil s => exact .nil s
  | @cons s current t e es hstep htail ih =>
    have hc := viable_after_guarded_prefix hstep.2.2 htail ht
    exact .cons ⟨hstep.1, hstep.2.1, hc⟩ (ih ht)

/-- Exact characterization, not only a sufficient correctness filter. -/
theorem productive_trace_exact {s t : State} {events : List Event}
    (hs : Viable P K G s) :
    Trace (productiveRestriction P K G) s events t ↔
      Trace (guarded P K) s events t ∧ Viable P K G t := by
  constructor
  · intro h
    exact ⟨productive_trace_guarded h, productive_trace_terminal_viable hs h⟩
  · rintro ⟨h, ht⟩
    exact guarded_trace_to_viable_is_productive h ht

/-- The restriction loses no finite completion of the same supplied contract. -/
theorem productive_contract_exact {s t : State} {events : List Event} :
    ContractTrace (productiveRestriction P K G) K G s events t ↔
      ContractTrace P K G s events t := by
  constructor
  · rintro ⟨hk, h, hg⟩
    exact ⟨hk, trace_map (P := guarded (productiveRestriction P K G) K)
      (Q := guarded P K) (f := id) (fun _ _ _ hs => ⟨hs.1.1, hs.2⟩) h, hg⟩
  · rintro ⟨hk, h, hg⟩
    have hterminal : K t := guarded_trace_terminal hk h
    have hp := guarded_trace_to_viable_is_productive h
      (terminal_is_viable hterminal hg)
    exact ⟨hk, trace_map (P := productiveRestriction P K G)
      (Q := guarded (productiveRestriction P K G) K) (f := id) (fun _ _ _ hs =>
      ⟨hs, hs.2.1, viable_has_condition hs.2.2⟩) hp, hg⟩

/-- Maximality is among subrelations with this target and productive endpoints.
It does not claim that arbitrary infinite paths eventually complete. -/
theorem productive_restriction_largest
    (hsub : Extends Q P)
    (hsource : ∀ s e t, Q.step s e t → K s)
    (hcompletion : ∀ s e t, Q.step s e t → Viable P K G t) :
    Extends Q (productiveRestriction P K G) := by
  intro s e t h
  exact ⟨hsub s e t h, hsource s e t h, hcompletion s e t h⟩

theorem contract_extension (hextends : Extends P Q)
    {s t : State} {events : List Event} (h : ContractTrace P K G s events t) :
    ContractTrace Q K G s events t := by
  exact ⟨h.1, trace_map (P := guarded P K) (Q := guarded Q K) (f := id)
    (fun s e t hs => ⟨hextends s e t hs.1, hs.2⟩) h.2.1,
    h.2.2⟩

theorem viable_extension (hextends : Extends P Q) {s : State}
    (h : Viable P K G s) : Viable Q K G s := by
  obtain ⟨events, t, h⟩ := h
  exact ⟨events, t, contract_extension hextends h⟩

/-- Correctness filtering cannot generate a continuation absent from P. -/
theorem no_restriction_creates_completion (hsub : Extends Q P) {s : State}
    (h : ¬ Viable P K G s) : ¬ Viable Q K G s := by
  intro hq
  exact h (viable_extension hsub hq)

/-- Newly available capacity preserves each old productive transition for the
same target; this does not assert adoption, selection, or universal safety. -/
theorem productive_capacity_extension (hextends : Extends P Q) :
    Extends (productiveRestriction P K G) (productiveRestriction Q K G) := by
  intro s e t h
  exact ⟨hextends s e t h.1, h.2.1, viable_extension hextends h.2.2⟩

/-- Full-state occurrence descriptions prevent replacing an unsafe actual
history by a safe alternative having the same unannotated event word. -/
def stateOccurrences (P : Process State Event) : Process State (Event × (State × State)) :=
  CoupledOccurrence.described P (fun s _ t => (s, t))

theorem guarded_occurrence_conditions {s t : State}
    {occurrences : List (Event × (State × State))}
    (h : Trace (stateOccurrences (guarded P K)) s occurrences t)
    {occurrence : Event × (State × State)} (hm : occurrence ∈ occurrences) :
    K occurrence.2.1 ∧ K occurrence.2.2 := by
  induction h with
  | nil => simp at hm
  | @cons s current t label labels hstep htail ih =>
    rcases List.mem_cons.mp hm with hhead | hrest
    · subst occurrence
      have heq := hstep.2
      change label.2 = (s, current) at heq
      exact heq ▸ hstep.1.2
    · exact ih hrest

/-- A corrected future does not retrospectively remove an earlier actual
violation from a contract that covers the whole described history. -/
theorem earlier_violation_survives_suffix
    {s t : State} {past future : List (Event × (State × State))}
    {occurrence : Event × (State × State)} (hm : occurrence ∈ past)
    (hbad : ¬ (K occurrence.2.1 ∧ K occurrence.2.2)) :
    ¬ Trace (stateOccurrences (guarded P K)) s (past ++ future) t := by
  intro h
  exact hbad (guarded_occurrence_conditions h (List.mem_append.mpr (Or.inl hm)))

/-- Here the violating prefix and its continuation are both witnessed in P.
The positive conjunct retains their actual composition; the negative conjunct
rules out certifying that same full occurrence history as condition-preserving. -/
theorem actual_violation_not_erased
    {s current t : State} {past future : List (Event × (State × State))}
    {occurrence : Event × (State × State)}
    (hpast : Trace (stateOccurrences P) s past current)
    (hfuture : Trace (stateOccurrences P) current future t)
    (hm : occurrence ∈ past)
    (hbad : ¬ (K occurrence.2.1 ∧ K occurrence.2.2)) :
    Trace (stateOccurrences P) s (past ++ future) t ∧
      ¬ Trace (stateOccurrences (guarded P K)) s (past ++ future) t := by
  exact ⟨trace_append_iff.mpr ⟨current, hpast, hfuture⟩,
    earlier_violation_survives_suffix hm hbad⟩

end Generative.PurposeCorrection

#print axioms Generative.PurposeCorrection.guarded_trace_underlying
#print axioms Generative.PurposeCorrection.guarded_trace_terminal
#print axioms Generative.PurposeCorrection.contract_trace_underlying
#print axioms Generative.PurposeCorrection.terminal_is_viable
#print axioms Generative.PurposeCorrection.viable_after_guarded_prefix
#print axioms Generative.PurposeCorrection.contract_append_iff
#print axioms Generative.PurposeCorrection.viable_has_condition
#print axioms Generative.PurposeCorrection.productive_trace_guarded
#print axioms Generative.PurposeCorrection.productive_trace_terminal_viable
#print axioms Generative.PurposeCorrection.guarded_trace_to_viable_is_productive
#print axioms Generative.PurposeCorrection.productive_trace_exact
#print axioms Generative.PurposeCorrection.productive_contract_exact
#print axioms Generative.PurposeCorrection.productive_restriction_largest
#print axioms Generative.PurposeCorrection.contract_extension
#print axioms Generative.PurposeCorrection.viable_extension
#print axioms Generative.PurposeCorrection.no_restriction_creates_completion
#print axioms Generative.PurposeCorrection.productive_capacity_extension
#print axioms Generative.PurposeCorrection.guarded_occurrence_conditions
#print axioms Generative.PurposeCorrection.earlier_violation_survives_suffix
#print axioms Generative.PurposeCorrection.actual_violation_not_erased
