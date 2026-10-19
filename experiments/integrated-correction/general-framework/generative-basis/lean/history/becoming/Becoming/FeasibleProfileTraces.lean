import Becoming.Frame
import ContinuationConditions

/-!
# Continuation profiles of a process's feasible words

`ContinuationConditions` compares finite histories of a supplied language by the
continuations each admits (`SameFuture`), calls a language stable when no admitted history
changes the profile, and shows that for a prefix-closed language containing the empty word
stability is exactly letterwise admission; a letterwise word that is not admitted refutes
stability, and a decided obstruction locates an admitted prefix whose profile changed. The
language of a process from a configuration, the words of its traces from there
(`Feasible P s`), is prefix-closed and contains the empty word
(`Deeper.process_language_prefix_closed`). This module states those laws of every process's
traces.

* **Stable exactly where letterwise.** The feasible words from `s` keep one profile after every
  feasible history exactly when a word is feasible from `s` exactly when each of its letters is
  (`stable_iff_letterwise`).
* **Joint obstruction.** A word whose letters are each feasible from `s` while the word is not
  refutes stability (`joint_obstruction_refutes_stability`); where feasibility from `s` is
  decided, the obstruction locates a feasible prefix after which the next letter is blocked and
  whose profile differs from the start's (`obstruction_locates_changed_profile`).
* **Same futures extend.** Two histories with the same continuations from `s` keep the same
  continuations after any common extension (`same_future_extends`).
* **The unrestricted language.** The process realizing every word over `Bool` has the same
  profile after every history (`unrestricted_stable`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace FeasibleProfileTraces

open Generative Generative.ContinuationConditions

universe u v

variable {S : Type u} {A : Type v}

/-- The empty word is feasible from every configuration. -/
theorem feasible_nil (P : Process S A) (s : S) : Feasible P s [] :=
  ⟨s, .nil s⟩

/-- Stability passes to a language with the same words. -/
theorem stable_of_same {L L' : List A → Prop} (same : ∀ w, L w ↔ L' w) (stable : Stable L) :
    Stable L' :=
  fun h held suffix =>
    (same (h ++ suffix)).symm.trans ((stable h ((same h).mpr held) suffix).trans (same ([] ++ suffix)))

/-- **The feasible words from `s` keep one profile after every feasible history exactly when a
word is feasible from `s` exactly when each of its letters is.** -/
theorem stable_iff_letterwise (P : Process S A) (s : S) :
    Stable (Feasible P s) ↔ ∀ word, Feasible P s word ↔ Letterwise (Feasible P s) word :=
  ContinuationConditions.stable_iff_letterwise _ (Deeper.process_language_prefix_closed P s)
    (feasible_nil P s)

/-- **A word whose letters are each feasible from `s`, while the word is not, refutes
stability.** -/
theorem joint_obstruction_refutes_stability (P : Process S A) (s : S) {word : List A}
    (letters : Letterwise (Feasible P s) word) (blocked : ¬ Feasible P s word) :
    ¬ Stable (Feasible P s) :=
  ContinuationConditions.joint_obstruction_refutes_stability _
    (Deeper.process_language_prefix_closed P s) (feasible_nil P s) word letters blocked

/-- **A decided obstruction locates a changed profile**: a feasible prefix of the word, whose
next letter is feasible from `s` alone but blocked after it, and whose continuations differ
from those of `s`. -/
theorem obstruction_locates_changed_profile (P : Process S A) (s : S)
    [DecidablePred (Feasible P s)] {word : List A}
    (letters : Letterwise (Feasible P s) word) (blocked : ¬ Feasible P s word) :
    ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ Feasible P s pre ∧ Feasible P s [a] ∧
      ¬ Feasible P s (pre ++ [a]) ∧ ¬ SameFuture (Feasible P s) pre [] :=
  ContinuationConditions.obstruction_locates_changed_profile _ (feasible_nil P s) word letters
    blocked

/-- **Histories with the same continuations from `s` keep them after a common extension.** -/
theorem same_future_extends (P : Process S A) (s : S) {h k : List A}
    (same : SameFuture (Feasible P s) h k) (extension : List A) :
    SameFuture (Feasible P s) (h ++ extension) (k ++ extension) :=
  ContinuationConditions.same_future_extends _ same extension

/-- **The process realizing every word over `Bool` has the same profile after every
history.** -/
theorem unrestricted_stable :
    Stable (Feasible (Deeper.historyProcess unrestricted) []) :=
  stable_of_same (fun word => ⟨fun _ => unrestricted_realized word, fun _ => True.intro⟩)
    ContinuationConditions.unrestricted_stable

end FeasibleProfileTraces

end Becoming
