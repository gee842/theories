import GenerativeCore

/-!
# The same carrier admits incompatible supplied event laws

All three processes have exactly the same state and action types. Thus their
product towers also agree; the processes differ only in supplied admissibility.
This is an underdetermination result relative to carrier/product information,
not an impossibility theorem for deriving laws from richer premises.
-/

namespace Generative.Deeper

def idle : Process Bool Unit where
  step _ _ _ := False

def static : Process Bool Unit where
  step s _ t := s = t

def toggle : Process Bool Unit where
  step s _ t := t = !s

theorem idle_no_event (s : Bool) : ¬ Enabled idle s () := by
  rintro ⟨_, h⟩
  exact h

theorem static_event (s : Bool) : static.step s () s := rfl

theorem static_never_changes {s t : Bool} (h : static.step s () t) : s = t := h

theorem toggle_event (s : Bool) : toggle.step s () (!s) := rfl

theorem toggle_always_changes {s t : Bool} (h : toggle.step s () t) : s ≠ t := by
  cases s <;> cases t <;> cases h <;> intro heq <;> cases heq

theorem static_history_never_changes {s t : Bool} {word : List Unit}
    (h : Trace static s word t) : s = t := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact hs.trans ih

theorem toggle_two_event_cycle (s : Bool) : Trace toggle s [(), ()] s := by
  have back : toggle.step (!s) () s := by cases s <;> rfl
  exact .cons (toggle_event s) (.cons back (.nil s))

theorem same_carrier_incompatible_laws :
    ¬ idle.step false () true ∧ toggle.step false () true ∧
      static.step false () false ∧ ¬ toggle.step false () false := by
  refine ⟨fun h => h, rfl, rfl, ?_⟩
  intro h
  cases h

def singletonLoop : Process Unit Unit where
  step _ _ _ := True

theorem event_without_state_distinction :
    singletonLoop.step () () () ∧ (∀ s t : Unit, s = t) := by
  constructor
  · trivial
  · intro s t
    cases s
    cases t
    rfl

end Generative.Deeper

#print axioms Generative.Deeper.idle_no_event
#print axioms Generative.Deeper.static_event
#print axioms Generative.Deeper.static_never_changes
#print axioms Generative.Deeper.toggle_event
#print axioms Generative.Deeper.toggle_always_changes
#print axioms Generative.Deeper.static_history_never_changes
#print axioms Generative.Deeper.toggle_two_event_cycle
#print axioms Generative.Deeper.same_carrier_incompatible_laws
#print axioms Generative.Deeper.event_without_state_distinction
