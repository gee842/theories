import Becoming.Runs

/-!
# One course, one kind or two roles

A law of exchange over one kind of relatum (`ExchangeLaw R R`) generates a course that reads as a
world in two ways: over its relata as one kind (`ExchangeLaw.world`, `Becoming.Counterfactual`),
and with formations and conditions as roles of one relatum (`ExchangeLaw.courseWorld`,
`Becoming.Runs`, through `World.ofRoles`). The two readings of one course had no theorem joining
them (the scope note of `worlds-are-runs`). This module states that they are one course, with no
premise beyond what each theorem names.

* **The same standings.** The two-role world's conditions stand where the one-kind world's relata
  stand, at the levels the law generates (`level_eq`), and its formations take from and give to
  its conditions exactly what the one-kind world's relata take and give (`take_eq`, `give_eq`).
* **They balance together.** Under a law of what has stood, the one-kind world balances exactly
  where the two-role world does (`balanced_iff`), each exactly where the course is feasible.
* **One run of exchange.** Where the course is feasible, the run of the law of exchange read from
  the one-kind world and the run read from the two-role world stand at the same levels at every
  step (`runs_agree`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CourseRoles

variable {R : Type} {law : ExchangeLaw R R} {present : Nat → List R} {start : R → Nat}
  {W : Web R R}

/-- **The two-role world's conditions stand where the one-kind world's relata stand.** -/
theorem level_eq (t : Nat) (c : R) :
    (law.courseWorld present start W).web.level t (.inr c) = (law.world present start W).web.level t c :=
  rfl

/-- **A formation of the two-role world takes from a condition what the relatum takes from it in
the one-kind world.** -/
theorem take_eq (t : Nat) (f c : R) :
    (law.courseWorld present start W).flow.take t (.inl f) (.inr c) =
      (law.world present start W).flow.take t f c :=
  rfl

/-- **A formation of the two-role world gives to a condition what the relatum gives to it in the
one-kind world.** -/
theorem give_eq (t : Nat) (f c : R) :
    (law.courseWorld present start W).flow.give t (.inl f) (.inr c) =
      (law.world present start W).flow.give t f c :=
  rfl

/-- **The two readings of one course balance together**, under a law of what has stood. -/
theorem balanced_iff (na : law.Nonanticipating) :
    (law.world present start W).Balanced ↔ (law.courseWorld present start W).Balanced :=
  (ExchangeLaw.world_balances_iff na present start W).trans
    (ExchangeLaw.courseWorld_balanced_iff na).symm

/-- **One run of exchange.** Where the course is feasible, the run of exchange read from the
one-kind world and the run read from the two-role world stand at the same levels at every step. -/
theorem runs_agree (na : law.Nonanticipating) (feasible : law.Feasible present start) (t : Nat)
    (c : R) :
    ((ExchangeLaw.courseRun (W := W) na feasible).state t).level (.inr c) =
      (ExchangeLaw.worldRun na W feasible).state t c :=
  rfl

end CourseRoles

end Becoming
