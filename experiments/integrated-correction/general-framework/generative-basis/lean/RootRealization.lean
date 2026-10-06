import GenerativeCore

/-!
# A finite realization of the proposed root

This is an explicit satisfiability witness for the stated causal commitments,
not a derivation of the transition rules or of learning, concern, or ethics.
`supplied = true` means a continuing external provision is available for every
restoration. The model does not produce unlimited work from a finite reserve.
Actions denote possible events, not powers granted to an omniscient controller.
The event named `revise` is a supplied consequence-triggered rule change; its
existence is demonstrated, not explained from more primitive physics.
-/

namespace Generative.Realization

inductive Phase where
  | initial
  | depleted
  | revised
  | ready
  | terminal
  deriving DecidableEq, Repr

inductive Event where
  | use
  | revise
  | restore
  | abandon
  deriving DecidableEq, Repr

inductive Selector where
  | useOnly
  | repairCapable
  | inactive
  deriving DecidableEq, Repr

def selector : Phase → Selector
  | .initial | .depleted => .useOnly
  | .revised | .ready => .repairCapable
  | .terminal => .inactive

def supported : Phase → Bool
  | .initial => true
  | .depleted => false
  | .revised => false
  | .ready => true
  | .terminal => false

/-- This exhaustive, non-overlapping presentation keeps the original finite
transition table while avoiding extensional dependencies in a generated matcher. -/
def law (supplied : Bool) : Phase → Event → Phase → Bool
  | .initial => fun
    | .use => fun
      | .depleted => true
      | .initial | .revised | .ready | .terminal => false
    | .revise | .restore | .abandon => fun _ => false
  | .depleted => fun
    | .revise => fun
      | .revised => true
      | .initial | .depleted | .ready | .terminal => false
    | .abandon => fun
      | .terminal => true
      | .initial | .depleted | .revised | .ready => false
    | .use | .restore => fun _ => false
  | .revised => fun
    | .restore => fun
      | .ready => supplied
      | .initial | .depleted | .revised | .terminal => false
    | .use | .revise | .abandon => fun _ => false
  | .ready => fun
    | .use => fun
      | .revised => true
      | .initial | .depleted | .ready | .terminal => false
    | .revise | .restore | .abandon => fun _ => false
  | .terminal => fun _ _ => false

def process (supplied : Bool) : Process Phase Event where
  step s a t := law supplied s a t = true

theorem use_initial : Enabled (process true) .initial .use :=
  ⟨.depleted, rfl⟩

theorem no_use_depleted : ¬ Enabled (process true) .depleted .use := by
  rintro ⟨t, h⟩
  cases t <;> cases h

/-- A realized event changes a later permission, not just an observer's label. -/
theorem activity_changes_its_continuation_conditions :
    (process true).step .initial .use .depleted ∧
      Enabled (process true) .initial .use ∧
      ¬ Enabled (process true) .depleted .use :=
  ⟨rfl, use_initial, no_use_depleted⟩

theorem no_restore_depleted : ¬ Enabled (process true) .depleted .restore := by
  rintro ⟨t, h⟩
  cases t <;> cases h

/-- The two stated coordinates distinguish all phases; no further hidden
phase difference is required by this finite encoding. -/
theorem phase_determined_by_support_and_selector {s t : Phase}
    (hs : supported s = supported t) (hm : selector s = selector t) : s = t := by
  cases s <;> cases t <;> first | rfl | (cases hs <;> cases hm)

/-- The selector is operative for restoration admissibility at fixed support.
This characterizes a supplied rule, not how that rule was physically built. -/
theorem restoration_guard (s : Phase) :
    Enabled (process true) s .restore ↔
      supported s = false ∧ selector s = .repairCapable := by
  cases s <;> constructor
  all_goals solve
    | (intro _; exact ⟨rfl, rfl⟩)
    | (intro _; exact ⟨.ready, rfl⟩)
    | (rintro ⟨t, h⟩; cases t <;> cases h)
    | (rintro ⟨hs, hm⟩; cases hs <;> cases hm)

/-- A supplied internal revision changes which restoring event is possible.
The resource condition is equally depleted on both sides of the revision. -/
theorem consequential_internal_revision :
    Trace (process true) .initial [.use, .revise] .revised ∧
      supported .depleted = supported .revised ∧
      selector .depleted ≠ selector .revised ∧
      ¬ Enabled (process true) .depleted .restore ∧
      Enabled (process true) .revised .restore := by
  refine ⟨.cons (m := .depleted) (by rfl) (.cons (m := .revised) (by rfl) (.nil _)),
    rfl, ?_, no_restore_depleted,
    ⟨.ready, rfl⟩⟩
  intro h
  cases h

theorem revision_guard_requires_depletion {s t : Phase}
    (h : (process true).step s .revise t) :
    s = .depleted ∧ t = .revised := by
  cases s <;> cases t <;> first | exact ⟨rfl, rfl⟩ | cases h

theorem restoration_requires_external_provision :
    ¬ Enabled (process false) .revised .restore := by
  rintro ⟨t, h⟩
  cases t <;> cases h

theorem reaches_renewable_state :
    Trace (process true) .initial [.use, .revise, .restore] .ready :=
  .cons (m := .depleted) (by rfl)
    (.cons (m := .revised) (by rfl) (.cons (m := .ready) (by rfl) (.nil _)))

theorem nonempty_cycle : Trace (process true) .ready [.use, .restore] .ready :=
  .cons (m := .revised) (by rfl) (.cons (m := .ready) (by rfl) (.nil _))

def cycleState (n : Nat) : Phase :=
  if n % 2 = 0 then .ready else .revised

def cycleEvent (n : Nat) : Event :=
  if n % 2 = 0 then .use else .restore

/- These arithmetic lemmas replay the kernel definition of natural remainder.
The standard convenience lemmas use extensional proof dependencies; the cycle
itself and its modulo-two definitions remain unchanged. -/
private theorem mod_go_fuel_congr (x y f1 f2 : Nat) (hy : 0 < y)
    (h1 : x < f1) (h2 : x < f2) :
    Nat.modCore.go y hy f1 x h1 = Nat.modCore.go y hy f2 x h2 := by
  induction f1 generalizing x f2 with
  | zero => exact False.elim (Nat.not_lt_zero x h1)
  | succ f1 ih =>
    cases f2 with
    | zero => exact False.elim (Nat.not_lt_zero x h2)
    | succ f2 =>
      rw [Nat.modCore.go, Nat.modCore.go]
      by_cases h : y ≤ x
      · rw [dif_pos h, dif_pos h]
        exact ih _ _ _ _
      · rw [dif_neg h, dif_neg h]

private theorem modCore_eq (x y : Nat) : Nat.modCore x y =
    if 0 < y ∧ y ≤ x then Nat.modCore (x - y) y else x := by
  unfold Nat.modCore
  by_cases hy : 0 < y
  · rw [dif_pos hy, Nat.modCore.go]
    by_cases h : y ≤ x
    · rw [dif_pos h, if_pos ⟨hy, h⟩, dif_pos hy]
      exact mod_go_fuel_congr _ _ _ _ _ _ _
    · rw [dif_neg h, if_neg (fun hp => h hp.2)]
  · rw [dif_neg hy, if_neg (fun hp => hy hp.1)]

private theorem modCore_eq_mod (n m : Nat) : Nat.modCore n m = n % m := by
  cases n with
  | zero =>
    rw [modCore_eq]
    exact if_neg (fun hp => Nat.not_le_of_gt hp.1 hp.2)
  | succ n =>
    change Nat.modCore (n + 1) m = if m ≤ n + 1 then Nat.modCore (n + 1) m else n + 1
    by_cases h : m ≤ n + 1
    · exact (if_pos h).symm
    · rw [if_neg h, modCore_eq]
      exact if_neg (fun hp => h hp.2)

private theorem mod_eq (x y : Nat) : x % y =
    if 0 < y ∧ y ≤ x then (x-y) % y else x := by
  rw [← modCore_eq_mod, ← modCore_eq_mod]
  exact modCore_eq x y

private theorem mod_two_add_two (n : Nat) : (n + 2) % 2 = n % 2 := by
  rw [mod_eq, if_pos ⟨Nat.zero_lt_succ 1, Nat.le_add_left 2 n⟩]
  rfl

private theorem parity_transition (n : Nat) :
    (n % 2 = 0 ∧ (n + 1) % 2 = 1) ∨
    (n % 2 = 1 ∧ (n + 1) % 2 = 0) := by
  induction n with
  | zero => exact .inl ⟨rfl, rfl⟩
  | succ n ih =>
    cases ih with
    | inl h => exact .inr ⟨h.2, (mod_two_add_two n).trans h.1⟩
    | inr h => exact .inl ⟨h.2, (mod_two_add_two n).trans h.1⟩


/-- A particular supported infinite trajectory; no claim that all paths renew. -/
theorem recurrent_execution (n : Nat) :
    (process true).step (cycleState n) (cycleEvent n) (cycleState (n + 1)) := by
  cases parity_transition n with
  | inl h =>
    have hn : (n + 1) % 2 ≠ 0 := fun hz => Nat.noConfusion (h.2.symm.trans hz)
    unfold cycleState cycleEvent
    rw [if_pos h.1, if_pos h.1, if_neg hn]
    rfl
  | inr h =>
    have hn : n % 2 ≠ 0 := fun hz => Nat.noConfusion (h.1.symm.trans hz)
    unfold cycleState cycleEvent
    rw [if_neg hn, if_neg hn, if_pos h.2]
    rfl

theorem reaches_terminal :
    Trace (process true) .initial [.use, .abandon] .terminal :=
  .cons (m := .depleted) (by rfl) (.cons (m := .terminal) (by rfl) (.nil _))

theorem terminal_has_no_action (supplied : Bool) (a : Event) :
    ¬ Enabled (process supplied) .terminal a := by
  rintro ⟨t, h⟩
  cases a <;> cases t <;> cases h

theorem no_continuation_after_loss {a : Event} {as : List Event} {t : Phase} :
    ¬ Trace (process true) .terminal (a :: as) t := by
  intro h
  obtain ⟨m, hs, _⟩ := trace_cons_iff.mp h
  exact terminal_has_no_action true a ⟨m, hs⟩

/-- Both regimes start from the same state under the same transition relation. -/
theorem same_law_admits_renewal_and_loss :
    Trace (process true) .initial [.use, .revise, .restore] .ready ∧
      Trace (process true) .ready [.use, .restore] .ready ∧
      Trace (process true) .initial [.use, .abandon] .terminal ∧
      (∀ a, ¬ Enabled (process true) .terminal a) :=
  ⟨reaches_renewable_state, nonempty_cycle, reaches_terminal,
    terminal_has_no_action true⟩

/-- Add a changing coordinate which does not affect any permitted phase step. -/
def decoratedProcess (supplied : Bool) : Process (Phase × Bool) Event where
  step s a t := (process supplied).step s.1 a t.1 ∧ t.2 = !s.2

theorem decoration_local_exact (supplied : Bool) :
    ∀ s a r, (process supplied).step s.1 a r ↔
      ∃ t, (decoratedProcess supplied).step s a t ∧ t.1 = r := by
  intro s a r
  constructor
  · intro h
    exact ⟨(r, !s.2), ⟨h, rfl⟩, rfl⟩
  · rintro ⟨t, h, ht⟩
    have edge := h.1
    exact ht ▸ edge

/-- A non-injective, instantiated exact summary discards the changing badge.
Every finite word and projected endpoint is preserved from EACH original state. -/
theorem decoration_trace_exact (supplied : Bool) :
    ∀ s word r, Trace (process supplied) s.1 word r ↔
      ∃ t, Trace (decoratedProcess supplied) s word t ∧ t.1 = r :=
  local_exact_iff_trace_exact.mp (decoration_local_exact supplied)

/-- Keeping support alone loses the operative setting and cannot preserve all
feasible words for ANY proposed process on those coarse Boolean states. -/
theorem support_alone_is_incomplete :
    ¬ ∃ Q : Process Bool Event,
      ∀ s word, Feasible (process true) s word ↔ Feasible Q (supported s) word := by
  rintro ⟨Q, hexact⟩
  have yes : Feasible (process true) .revised [.restore] :=
    ⟨.ready, .cons (m := .ready) (by rfl) (.nil _)⟩
  have no : ¬ Feasible (process true) .depleted [.restore] := by
    intro h
    exact no_restore_depleted (enabled_iff_singleton_trace.mpr h)
  have differs := feasible_difference_implies_projection_difference hexact yes no
  exact differs rfl

#print axioms mod_go_fuel_congr
#print axioms modCore_eq
#print axioms modCore_eq_mod
#print axioms mod_eq
#print axioms mod_two_add_two
#print axioms parity_transition

end Generative.Realization

#print axioms Generative.Realization.activity_changes_its_continuation_conditions
#print axioms Generative.Realization.phase_determined_by_support_and_selector
#print axioms Generative.Realization.restoration_guard
#print axioms Generative.Realization.consequential_internal_revision
#print axioms Generative.Realization.revision_guard_requires_depletion
#print axioms Generative.Realization.restoration_requires_external_provision
#print axioms Generative.Realization.reaches_renewable_state
#print axioms Generative.Realization.nonempty_cycle
#print axioms Generative.Realization.recurrent_execution
#print axioms Generative.Realization.reaches_terminal
#print axioms Generative.Realization.terminal_has_no_action
#print axioms Generative.Realization.no_continuation_after_loss
#print axioms Generative.Realization.same_law_admits_renewal_and_loss
#print axioms Generative.Realization.decoration_local_exact
#print axioms Generative.Realization.decoration_trace_exact
#print axioms Generative.Realization.support_alone_is_incomplete

#print axioms Generative.Realization.use_initial
#print axioms Generative.Realization.no_use_depleted
#print axioms Generative.Realization.no_restore_depleted
#print axioms Generative.Realization.supported
#print axioms Generative.Realization.law
#print axioms Generative.Realization.process
#print axioms Generative.Realization.selector
#print axioms Generative.Realization.cycleState
#print axioms Generative.Realization.cycleEvent
#print axioms Generative.Realization.decoratedProcess
