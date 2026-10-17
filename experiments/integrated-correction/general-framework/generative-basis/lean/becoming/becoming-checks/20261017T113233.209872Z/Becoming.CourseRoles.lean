import Becoming.Runs

/-!
# One course, one kind or two roles

A law of exchange generates one course: its flow (`ExchangeLaw.course`) and its web, the web with
the levels the law generates (`ExchangeLaw.courseWeb`). Over one kind of relatum (`ExchangeLaw R R`)
the course reads as a world in two ways, each by definition a reading of that one flow and web:
with one kind of relatum (`World.ofKind`; `ExchangeLaw.world`, `Becoming.Counterfactual`), and with
formations and conditions as roles of one relatum (`World.ofRoles`; `ExchangeLaw.courseWorld`,
`Becoming.Runs`) (`world_eq`, `courseWorld_eq`). The two worlds have different relata (`R` and
`R ⊕ R`), so they are two readings, not one term. This module states that the readings agree, for
every flow and web of one kind and so for every course, with no premise beyond what each theorem
names.

* **The same standings and exchanges.** For every flow and web of one kind, the two-role world's
  conditions stand where the one-kind world's relata stand (`World.roles_level`), and its
  formations take from and give to its conditions exactly what the relata take and give
  (`World.roles_take`, `World.roles_give`); so for every course (`level_eq`, `take_eq`,
  `give_eq`).
* **They balance together**, with no premise: the one-kind world balances exactly where the
  two-role world does (`World.kind_balanced_iff_roles`); so for every course (`balanced_iff`).
  Under a law of what has stood each balances exactly where the course is feasible
  (`ExchangeLaw.world_balances_iff`, `ExchangeLaw.courseWorld_balanced_iff`).
* **One run of exchange.** Where the course is feasible, the run of the law of exchange read from
  the one-kind world and the run read from the two-role world stand at the same levels at every
  step (`runs_agree`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace World

variable {R : Type} (L : Flow R R) (W : Web R R)

/-- **The two-role world's conditions stand where the one-kind world's relata stand**, for every
flow and web of one kind. -/
theorem roles_level (t : Nat) (c : R) : (ofRoles L W).web.level t (.inr c) = (ofKind L W).web.level t c :=
  rfl

/-- **A formation of the two-role world takes from a condition what the relatum takes from it in
the one-kind world.** -/
theorem roles_take (t : Nat) (f c : R) :
    (ofRoles L W).flow.take t (.inl f) (.inr c) = (ofKind L W).flow.take t f c :=
  rfl

/-- **A formation of the two-role world gives to a condition what the relatum gives to it in the
one-kind world.** -/
theorem roles_give (t : Nat) (f c : R) :
    (ofRoles L W).flow.give t (.inl f) (.inr c) = (ofKind L W).flow.give t f c :=
  rfl

/-- **The two readings of a flow and a web of one kind balance together**, with no premise. -/
theorem kind_balanced_iff_roles : (ofKind L W).Balanced ↔ (ofRoles L W).Balanced :=
  (L.roles_balances (W := W)).symm

end World

namespace CourseRoles

variable {R : Type} {law : ExchangeLaw R R} {present : Nat → List R} {start : R → Nat}
  {W : Web R R}

/-- **The one-kind course world reads the course's flow and web with one kind of relatum.** -/
theorem world_eq :
    law.world present start W = World.ofKind (law.course present start) (law.courseWeb present start W) :=
  rfl

/-- **The two-role course world reads the same flow and web with formations and conditions as
roles of one relatum.** -/
theorem courseWorld_eq :
    law.courseWorld present start W =
      World.ofRoles (law.course present start) (law.courseWeb present start W) :=
  rfl

/-- **The two-role world's conditions stand where the one-kind world's relata stand.** -/
theorem level_eq (t : Nat) (c : R) :
    (law.courseWorld present start W).web.level t (.inr c) = (law.world present start W).web.level t c :=
  World.roles_level _ _ t c

/-- **A formation of the two-role world takes from a condition what the relatum takes from it in
the one-kind world.** -/
theorem take_eq (t : Nat) (f c : R) :
    (law.courseWorld present start W).flow.take t (.inl f) (.inr c) =
      (law.world present start W).flow.take t f c :=
  World.roles_take _ _ t f c

/-- **A formation of the two-role world gives to a condition what the relatum gives to it in the
one-kind world.** -/
theorem give_eq (t : Nat) (f c : R) :
    (law.courseWorld present start W).flow.give t (.inl f) (.inr c) =
      (law.world present start W).flow.give t f c :=
  World.roles_give _ _ t f c

/-- **The two readings of one course balance together**, with no premise. -/
theorem balanced_iff : (law.world present start W).Balanced ↔ (law.courseWorld present start W).Balanced :=
  World.kind_balanced_iff_roles _ _

/-- **One run of exchange.** Where the course is feasible, the run of exchange read from the
one-kind world and the run read from the two-role world stand at the same levels at every step. -/
theorem runs_agree (na : law.Nonanticipating) (feasible : law.Feasible present start) (t : Nat)
    (c : R) :
    ((ExchangeLaw.courseRun (W := W) na feasible).state t).level (.inr c) =
      (ExchangeLaw.worldRun na W feasible).state t c :=
  rfl

end CourseRoles

end Becoming
