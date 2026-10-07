/-!
# Cyclic windows survive graph pruning

Independent general proof for the finite period-language certificate. A mask
keeps a window only when it also contains an allowed successor and predecessor.
Every window of a represented cyclic history has both witnesses, so no round
can remove it. Any finite number of rounds, including an early fixed-point
exit, therefore preserves the history.

The statement allows arbitrary index and window types. A concrete encoding of
binary windows must still prove the indicated adjacency and mask-operation
correspondences. Neither that correspondence nor strategy extraction from
`PhasePeriodSelection.knowsWithin` is silently supplied by this module.
-/

namespace Generative.InquirySufficiency.PeriodWindowPruning

universe u v w

variable {Index : Type u} {Window : Type v} {Mask : Type w}

/-- All represented windows belong to the mask. -/
def Covered (member : Mask → Window → Bool) (window : Index → Window) (mask : Mask) : Prop :=
  ∀ i, member mask (window i) = true

/-- One local in/out pruning round. The neighbors are the two possible binary
extensions in the intended application, but no coding convention is assumed. -/
def pruneAt (next0 next1 previous0 previous1 : Window → Window)
    (mask : Window → Bool) (word : Window) : Bool :=
  mask word && (mask (next0 word) || mask (next1 word)) &&
    (mask (previous0 word) || mask (previous1 word))

/-- Pruning is conservative: it cannot introduce an absent window. -/
theorem pruning_adds_nothing (next0 next1 previous0 previous1 : Window → Window)
    (mask : Window → Bool) (word : Window)
    (kept : pruneAt next0 next1 previous0 previous1 mask word = true) : mask word = true := by
  cases present : mask word with
  | false =>
    unfold pruneAt at kept
    rw [present] at kept
    cases kept
  | true => rfl

/-- The two witnessed neighbors may be the same window, and the index type may
contain any number of components. No finiteness or single-component assumption
is required for preservation. -/
theorem represented_windows_survive
    (next0 next1 previous0 previous1 : Window → Window)
    (window : Index → Window) (advance retreat : Index → Index)
    (nextWindow : ∀ i, window (advance i) = next0 (window i) ∨
      window (advance i) = next1 (window i))
    (previousWindow : ∀ i, window (retreat i) = previous0 (window i) ∨
      window (retreat i) = previous1 (window i))
    (mask : Window → Bool) (covered : ∀ i, mask (window i) = true) :
    ∀ i, pruneAt next0 next1 previous0 previous1 mask (window i) = true := by
  intro i
  have outgoing : (mask (next0 (window i)) || mask (next1 (window i))) = true := by
    cases nextWindow i with
    | inl same => rw [← same, covered]; rfl
    | inr same =>
      rw [← same, covered]
      cases mask (next0 (window i)) <;> rfl
  have incoming : (mask (previous0 (window i)) || mask (previous1 (window i))) = true := by
    cases previousWindow i with
    | inl same => rw [← same, covered]; rfl
    | inr same =>
      rw [← same, covered]
      cases mask (previous0 (window i)) <;> rfl
  unfold pruneAt
  rw [covered, outgoing, incoming]
  rfl

/-- Iteration without an early exit. -/
def rounds (cut : Mask → Mask) : Nat → Mask → Mask
  | 0, mask => mask
  | count + 1, mask => rounds cut count (cut mask)

/-- Representation-specific encodings need only supply the one-round lemma. -/
theorem rounds_preserve_coverage (member : Mask → Window → Bool) (window : Index → Window)
    (cut : Mask → Mask)
    (preserves : ∀ mask, Covered member window mask → Covered member window (cut mask))
    (count : Nat) (mask : Mask) (covered : Covered member window mask) :
    Covered member window (rounds cut count mask) := by
  induction count generalizing mask with
  | zero => exact covered
  | succ count ih => exact ih (cut mask) (preserves mask covered)

/-- Any early-exit test is safe for preservation: it returns either an already
covering mask or continues pruning. Correct fixed-point detection matters for
exhaustiveness or efficiency, not for this preservation claim. -/
def roundsUntil (stop : Mask → Mask → Bool) (cut : Mask → Mask) : Nat → Mask → Mask
  | 0, mask => mask
  | count + 1, mask =>
    if stop (cut mask) mask then mask else roundsUntil stop cut count (cut mask)

theorem early_rounds_preserve_coverage
    (member : Mask → Window → Bool) (window : Index → Window)
    (stop : Mask → Mask → Bool) (cut : Mask → Mask)
    (preserves : ∀ mask, Covered member window mask → Covered member window (cut mask))
    (count : Nat) (mask : Mask) (covered : Covered member window mask) :
    Covered member window (roundsUntil stop cut count mask) := by
  induction count generalizing mask with
  | zero => exact covered
  | succ count ih =>
    unfold roundsUntil
    cases stopped : stop (cut mask) mask with
    | true => exact covered
    | false => exact ih (cut mask) (preserves mask covered)

/-- Direct specialization: every finite number of local pruning rounds retains
all windows of the represented history. In particular, 128 rounds are safe. -/
theorem cyclic_pruning_preserves
    (next0 next1 previous0 previous1 : Window → Window)
    (window : Index → Window) (advance retreat : Index → Index)
    (nextWindow : ∀ i, window (advance i) = next0 (window i) ∨
      window (advance i) = next1 (window i))
    (previousWindow : ∀ i, window (retreat i) = previous0 (window i) ∨
      window (retreat i) = previous1 (window i))
    (count : Nat) (mask : Window → Bool) (covered : ∀ i, mask (window i) = true) :
    ∀ i, rounds (pruneAt next0 next1 previous0 previous1) count mask (window i) = true :=
  rounds_preserve_coverage (fun (mask : Window → Bool) (word : Window) => mask word) window
    (pruneAt next0 next1 previous0 previous1)
    (fun mask included => represented_windows_survive next0 next1 previous0 previous1
      window advance retreat nextWindow previousWindow mask included) count mask covered

end Generative.InquirySufficiency.PeriodWindowPruning

#print axioms Generative.InquirySufficiency.PeriodWindowPruning.Covered
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.pruneAt
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.pruning_adds_nothing
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.represented_windows_survive
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.rounds
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.rounds_preserve_coverage
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.roundsUntil
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.early_rounds_preserve_coverage
#print axioms Generative.InquirySufficiency.PeriodWindowPruning.cyclic_pruning_preserves
