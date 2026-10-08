import Std

/-
Two draws within one allocation history. Bool labels two differentiated positions,
not independent ontological subjects. Four equiprobable tickets model two fair,
independent bits; that physical correspondence is supplied, not proved here.
Exactly one position receives the resource. The distribution of the final Bool
therefore determines the FULL terminal joint protection distribution in this
small model, not merely selected marginal probabilities.
Preserves expresses fidelity to a supplied earlier result, not ethical validity.
The warrant, settlement scope, release and defeat of that result are substantive.
-/
namespace ChanceRevision

abbrev Ticket := Bool × Bool

def keep (t : Ticket) : Bool := t.1
def redraw (t : Ticket) : Bool := t.2
def favorFalse (t : Ticket) : Bool := t.1 && t.2

def count (r : Ticket → Bool) (p : Bool) : Nat :=
  (if r (false, false) = p then 1 else 0) +
  (if r (false, true) = p then 1 else 0) +
  (if r (true, false) = p then 1 else 0) +
  (if r (true, true) = p then 1 else 0)

def terminalLaw (r : Ticket → Bool) : Nat × Nat := (count r false, count r true)

def branchCount (r : Ticket → Bool) (first p : Bool) : Nat :=
  (if r (first, false) = p then 1 else 0) +
  (if r (first, true) = p then 1 else 0)

def Preserves (r s : Ticket → Bool) : Prop := ∀ t, s t = r t

theorem terminal_distributions :
    terminalLaw keep = (2, 2) ∧ terminalLaw redraw = (2, 2) ∧
    terminalLaw favorFalse = (3, 1) := by decide

theorem keep_preserves : Preserves keep keep := fun _ => rfl

theorem redraw_changes_both :
    redraw (false, true) ≠ keep (false, true) ∧
    redraw (true, false) ≠ keep (true, false) ∧ ¬ Preserves keep redraw := by
  refine ⟨by decide, by decide, ?_⟩
  intro h
  have impossible : true = false := h (false, true)
  cases impossible

/-- Terminal-law summaries cannot characterize fidelity to the first result.
This does not refute accounts retaining history in their outcome description. -/
theorem no_terminal_law_characterization
    (accepts : (Nat × Nat) → Prop)
    (exact : ∀ r, accepts (terminalLaw r) ↔ Preserves keep r) : False := by
  have original : accepts (terminalLaw keep) := (exact keep).mpr keep_preserves
  have same : terminalLaw keep = terminalLaw redraw := rfl
  have revised : accepts (terminalLaw redraw) := same ▸ original
  exact redraw_changes_both.2.2 ((exact redraw).mp revised)

/-- Once the first result is supplied as settled, preserving it gives certainty
on each observed branch, not a fresh half chance on that same resource. -/
theorem settlement_forces_conditional_concentration
    (r : Ticket → Bool) (h : Preserves keep r) (first : Bool) :
    branchCount r first first = 2 ∧ branchCount r first (!first) = 0 := by
  unfold branchCount
  rw [h (first, false), h (first, true)]
  cases first <;> decide

theorem fresh_redraw_is_conditionally_equal (first : Bool) :
    branchCount redraw first false = 1 ∧ branchCount redraw first true = 1 := by
  cases first <;> decide

/-- Faithful revisions compose while the same warranted target remains live.
This does not prohibit justified releases or repairs of defective settlements. -/
theorem preservation_composes (r s u : Ticket → Bool)
    (hrs : Preserves r s) (hsu : Preserves s u) : Preserves r u := by
  intro t
  exact Eq.trans (hsu t) (hrs t)

end ChanceRevision
