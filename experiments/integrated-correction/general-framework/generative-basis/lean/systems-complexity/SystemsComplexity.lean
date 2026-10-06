import SystemsOrganization
import FeedbackDynamics
import SymbolicDynamics

/-!
# Actual trajectory correspondence with the generative relational core

The bridge proves that each iterate is reached by the corresponding number of
actual steps in Generative.Trace. The binary shift is the very map whose
topological properties are proved in SymbolicDynamics. The delayed feedback
recurrence is proved equal to that common iteration before its trace is derived.
No empirical identification or ethical conclusion is supplied by these maps.
-/

namespace SystemsComplexity

theorem iterate_generative_trace {S : Type} (f : S → S) (s : S) (n : Nat) :
    Generative.Trace
      (SystemsOrganization.deterministic (fun state (_ : Unit) => f state))
      s (List.replicate n ()) (SymbolicDynamics.iterate f n s) := by
  induction n with
  | zero => exact .nil s
  | succ n ih =>
      rw [List.replicate_succ']
      apply Generative.trace_append_iff.mpr
      exact ⟨SymbolicDynamics.iterate f n s, ih, .cons rfl (.nil _)⟩

/-- This is the same infinite binary shift used in binary_shift_chaotic,
not a finite-state surrogate or a new interpretation of the action label. -/
theorem binary_shift_trace (s : SymbolicDynamics.Stream) (n : Nat) :
    Generative.Trace
      (SystemsOrganization.deterministic
        (fun state (_ : Unit) => SymbolicDynamics.shift state))
      s (List.replicate n ()) (SymbolicDynamics.iterate SymbolicDynamics.shift n s) := by
  exact iterate_generative_trace SymbolicDynamics.shift s n

theorem delayed_eq_iterate (k : Rat) (s : Rat × Rat) (n : Nat) :
    Feedback.delayed k s n = SymbolicDynamics.iterate (Feedback.delayedStep k) n s := by
  induction n with
  | zero => rfl
  | succ n ih => exact congrArg (Feedback.delayedStep k) ih

/-- The actual paired-state recurrence, including the stored previous value,
is a history in the same core; no projection discards that delay state. -/
theorem delayed_feedback_trace (k : Rat) (s : Rat × Rat) (n : Nat) :
    Generative.Trace
      (SystemsOrganization.deterministic
        (fun state (_ : Unit) => Feedback.delayedStep k state))
      s (List.replicate n ()) (Feedback.delayed k s n) := by
  rw [delayed_eq_iterate]
  exact iterate_generative_trace (Feedback.delayedStep k) s n

end SystemsComplexity

#print axioms SystemsComplexity.iterate_generative_trace
#print axioms SystemsComplexity.binary_shift_trace
#print axioms SystemsComplexity.delayed_eq_iterate
#print axioms SystemsComplexity.delayed_feedback_trace
