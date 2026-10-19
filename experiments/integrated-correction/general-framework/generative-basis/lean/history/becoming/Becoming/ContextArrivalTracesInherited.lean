import Becoming.ContextArrivalTraces
import BecomingCompatibility

/-!
# Where the changed history ends, through the periphery's proof

`BecomingCompatibility.changed_history_really_ends` states that `changingRelation` has no step
from context `true` at 2. This module states it of the traces of the evolving process: no trace
of positive length leaves context `true` at 2 (`changed_history_ends`). `Becoming.Bridge` proves
the relation itself without axioms (`changed_history_really_ends_by_core`); this join goes
through the periphery theorem.

This module inherits `propext` from `Generative.BecomingCompatibility.changed_history_really_ends`
and adds no axiom of its own. No ethical predicate or ranking occurs.
-/

namespace Becoming

namespace ContextArrivalTracesInherited

open Generative Generative.BecomingCompatibility

/-- **The changed history ends**: no trace of the evolving process of positive length leaves
context `true` at 2. -/
theorem changed_history_ends (a : Unit) (word : List Unit) (finish : Bool × Nat) :
    ¬ Trace (evolving changingRelation) (true, 2) (a :: word) finish :=
  fun trace => match trace_cons_iff.mp trace with
    | ⟨(j, t), step, _⟩ => changed_history_really_ends j t step

end ContextArrivalTracesInherited

end Becoming
