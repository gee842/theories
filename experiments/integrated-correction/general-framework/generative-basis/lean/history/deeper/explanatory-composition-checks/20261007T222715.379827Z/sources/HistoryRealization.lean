import GenerativeCore

/-!
# A supplied prefix-closed finite history language has an exact realization

The state is the complete declared event-label history, so no finite-memory
assumption is needed. The language remains an input; this theorem generates no physical law,
probability, observation policy or hidden-state interpretation from nothing.
-/

namespace Generative.Deeper

universe v

variable {Action : Type v}

/-- Direct structural proofs make this package's dependency boundary explicit. -/
theorem append_nil_constructive (xs : List Action) : xs ++ [] = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => exact congrArg (fun tail => x :: tail) ih

theorem append_assoc_constructive (xs ys zs : List Action) :
    (xs ++ ys) ++ zs = xs ++ (ys ++ zs) := by
  induction xs with
  | nil => rfl
  | cons x xs ih => exact congrArg (fun tail => x :: tail) ih

def PrefixClosed (Allowed : List Action → Prop) : Prop :=
  ∀ pre suffix, Allowed (pre ++ suffix) → Allowed pre

def historyProcess (Allowed : List Action → Prop) : Process (List Action) Action where
  step before a after := after = before ++ [a] ∧ Allowed after

theorem history_trace_iff {Allowed : List Action → Prop}
    (hclosed : PrefixClosed Allowed) {before word after : List Action}
    (hbefore : Allowed before) :
    Trace (historyProcess Allowed) before word after ↔
      after = before ++ word ∧ Allowed after := by
  induction word generalizing before with
  | nil =>
    constructor
    · intro h
      have heq := trace_nil_iff.mp h
      subst after
      exact ⟨(append_nil_constructive before).symm, hbefore⟩
    · rintro ⟨heq, _⟩
      apply trace_nil_iff.mpr
      exact (heq.trans (append_nil_constructive before)).symm
  | cons a rest ih =>
    constructor
    · intro h
      obtain ⟨middle, hs, ht⟩ := trace_cons_iff.mp h
      obtain ⟨heq, hafter⟩ := (ih hs.2).mp ht
      have hx : (before ++ [a]) ++ rest = before ++ (a :: rest) :=
        append_assoc_constructive before [a] rest
      exact ⟨heq.trans ((congrArg (fun xs => xs ++ rest) hs.1).trans hx), hafter⟩
    · rintro ⟨heq, hafter⟩
      have hx : (before ++ [a]) ++ rest = before ++ (a :: rest) :=
        append_assoc_constructive before [a] rest
      have hmiddle : Allowed (before ++ [a]) := by
        apply hclosed (before ++ [a]) rest
        exact hx.symm ▸ (heq ▸ hafter)
      apply trace_cons_iff.mpr
      exact ⟨before ++ [a], ⟨rfl, hmiddle⟩,
        (ih hmiddle).mpr ⟨heq.trans hx.symm, hafter⟩⟩

theorem history_from_empty_iff {Allowed : List Action → Prop}
    (hclosed : PrefixClosed Allowed) (hempty : Allowed [])
    (word after : List Action) :
    Trace (historyProcess Allowed) [] word after ↔
      after = word ∧ Allowed word := by
  constructor
  · intro h
    obtain ⟨heq, ha⟩ := (history_trace_iff hclosed hempty).mp h
    have heq' : after = word := heq
    exact ⟨heq', heq' ▸ ha⟩
  · rintro ⟨heq, hw⟩
    apply (history_trace_iff hclosed hempty).mpr
    exact ⟨heq, heq.symm ▸ hw⟩

theorem history_feasible_iff {Allowed : List Action → Prop}
    (hclosed : PrefixClosed Allowed) (hempty : Allowed []) (word : List Action) :
    Feasible (historyProcess Allowed) [] word ↔ Allowed word := by
  constructor
  · rintro ⟨after, ht⟩
    exact ((history_from_empty_iff hclosed hempty word after).mp ht).2
  · intro hw
    exact ⟨word, (history_from_empty_iff hclosed hempty word word).mpr ⟨rfl, hw⟩⟩

/-- Every supplied process's finite word language meets the realization
conditions; the reconstructed process preserves word feasibility, not original
hidden states, branch identities, intervention powers or probabilities. -/
theorem process_language_prefix_closed {State : Type u}
    (P : Process State Action) (initial : State) :
    PrefixClosed (Feasible P initial) := by
  intro pre suffix h
  exact feasible_prefix h

theorem process_language_exact_history_realization {State : Type u}
    (P : Process State Action) (initial : State) (word : List Action) :
    Feasible (historyProcess (Feasible P initial)) [] word ↔ Feasible P initial word := by
  apply history_feasible_iff (process_language_prefix_closed P initial)
  exact ⟨initial, .nil initial⟩

end Generative.Deeper

#print axioms Generative.Deeper.append_nil_constructive
#print axioms Generative.Deeper.append_assoc_constructive
#print axioms Generative.Deeper.history_trace_iff
#print axioms Generative.Deeper.history_from_empty_iff
#print axioms Generative.Deeper.history_feasible_iff
#print axioms Generative.Deeper.process_language_prefix_closed
#print axioms Generative.Deeper.process_language_exact_history_realization
