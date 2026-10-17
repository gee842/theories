import Becoming.OneStep

/-!
# Passage worlds: what the stated laws of one step and the following of passages give of worlds

`Becoming.OneStep` reads what a step of a flow shows of a condition as its passage
(`Flow.passage`), states the law of a family running down closed on a pattern of passages
(`OneStep.RunsDownClosed`), shows that the laws of one step as `Becoming.Locality` states them,
with the law that something taken has a taker, are that whole law
(`OneStep.runsDownClosed_iff_stated`), and that passages following one another position by
position continue up to order (`OneStep.Chained.continues`). A pattern is shown by a world when some step of its flow on some
family shows it (`OneStep.Realized`, `OneStep.RunRealized`). This module states those laws of the
steps of flows and of the worlds showing patterns, and proves them through the laws of patterns.

* **The stated laws are the whole law of a world's step.** A pattern is shown by some world across
  some step on a family running down closed exactly when it obeys the stated laws and the law that
  something taken has a taker (`runsDownClosed_realized_iff`). Across a step of a flow at which a
  family runs down closed, the pattern the step shows obeys the stated laws
  (`stated_of_runsDownClosed`).
* **What a flow shows on one family continues.** The passages a flow shows on one family across
  every step continue, at every positive level, as many members standing at it after each step as
  before the next (`passages_continue`); so does every run of patterns some world shows on one
  family (`RunRealized.continues`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace PassageWorlds

open OneStep

variable {F C : Type}

/-- **The stated laws with the taker law are the whole law of a world's step.** A pattern of
passages, takers and exchange is shown by some world across some step on a family running down
closed, listing each relatum taking part once, exactly when it obeys the laws of one step as
`Becoming.Locality` states them together with the law that something taken from the family has a
relatum taking it. -/
theorem runsDownClosed_realized_iff (P : List Passage) (k : Nat) (e : Prop) :
    Realized (fun w t es => w.flow.RunsDownOn w.web es t ∧ w.flow.ClosedAt es t) P k e ↔
      Stated P k e ∧ sign (total P Passage.taken) ≤ k :=
  (runsDownClosed_iff P k e).trans (runsDownClosed_iff_stated P k e)

/-- **A flow's step running down closed obeys the stated laws.** Across a step at which a family
runs down and is closed, the passages of its members, the number of relata taking from it and
whether something exchanges obey the laws of one step as `Becoming.Locality` states them. -/
theorem stated_of_runsDownClosed {L : Flow F C} {W : Web F C} {es : List C} {t : Nat}
    (runs : L.RunsDownOn W es t) (closed : L.ClosedAt es t) :
    Stated (es.map (L.passage W t)) (L.takers es t) (L.ExchangesAt t) :=
  ((runsDownClosed_iff_stated _ _ _).mp
    (Flow.Realizes.runsDownClosed ⟨rfl, rfl, Iff.rfl⟩ runs closed)).1

/-- **What a flow shows on one family continues.** Across every step, what stands after it at
each member of the family is what stands before the next step there, so at every positive level as
many members stand at it after each step as before the next. -/
theorem passages_continue (L : Flow F C) (W : Web F C) (es : List C) :
    Continues fun t => es.map (L.passage W t) :=
  Chained.continues fun t =>
    (map_comp_eq (L.passage W t) Passage.after es).trans
      (map_comp_eq (L.passage W (t + 1)) Passage.before es).symm

/-- **Every run some world shows on one family continues.** -/
theorem RunRealized.continues {cond : (w : World) → Nat → List w.Relatum → Prop}
    {P : Nat → List Passage} {k : Nat → Nat} {e : Nat → Prop}
    (realized : RunRealized cond P k e) : Continues P :=
  realized.chained.continues

end PassageWorlds

end Becoming
