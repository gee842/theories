
/-!
# The one unfolding: its records

The records every reading of the unfolding is stated in, with no premise among them. A `Web`
says, at each step, how far each condition stands, which formations are active, and what each
formation requires, needs and draws; a `Flow` says which formations take part in each step and
how much each takes from and gives to each condition. A `World` is one kind of relatum with a
flow and a web among its own relata, so formations and conditions are roles of one relatum
(`Becoming.Roles`), not two kinds. An `Exchange` is what the relata take and give across one
step, with nothing said of what they stand at; `World.move` is a world's exchange at a step, and
`total` sums a list of amounts.

Nothing here ties one record to another: balance, activity needing support and the other
premises of `Becoming.Premises` are gluings or local states, stated where they are used. A world
is not the starting point in the sense the relation-first re-founding retired (Ren, 14 October
2026: "why do we need "World"? wasn't this about the whole and its parts, about everything?"):
the readings of one unfolding, in context and with nothing glued, are one world
(`Contextual.world` of `Becoming.Readings`, and `Frame.world`), and `World` with its balance is the
case where two readings of change glue. What the records do commit to is a shared index of steps
and amounts counted in `Nat` (`Becoming.Sampling`, `Becoming.Interleavings`).

These are records over `Nat` and `Prop`, and this module imports nothing, so the core's import
tree starts here. The labelled process (`Generative.Process`) and the frame (`Becoming.Frame`)
enter as readings (`Becoming.Labelled`). The definitions moved here unchanged, with their names,
from `Becoming.Dependence` (`Web`), `Becoming.Flow` (`Flow`), `Becoming.Generation` (`total`),
`Becoming.Space` (`World`) and `Becoming.Unfolding` (`Exchange`, `Exchange.taken`,
`Exchange.given`, `World.move`). Every declaration has an empty axiom report.
-/

namespace Becoming

/-- One unfolding read through conditions and the dependences among them, all of
which may change from step to step. -/
structure Web (F C : Type) where
  level : Nat → C → Nat
  active : Nat → F → Prop
  requires : Nat → F → C → Prop
  need : Nat → F → C → Nat
  draws : Nat → F → C → Prop

/-- Amounts flowing between formations and conditions across each step: the formations
taking part in the step, and how much each takes from and gives to each condition. -/
structure Flow (F C : Type) where
  present : Nat → List F
  take : Nat → F → C → Nat
  give : Nat → F → C → Nat

/-- The total of a quantity over a finite list. -/
def total {α : Type} : List α → (α → Nat) → Nat
  | [], _ => 0
  | a :: as, q => q a + total as q

/-- A world: its relata, read with one kind of relatum, with the flow among them and their
web. -/
structure World where
  Relatum : Type
  flow : Flow Relatum Relatum
  web : Web Relatum Relatum

section Exchange

variable {R : Type}

/-- What the relata present take and give across a step, read as a move. -/
structure Exchange (R : Type) where
  present : List R
  take : R → R → Nat
  give : R → R → Nat

/-- What the relata present take from `c`. -/
def Exchange.taken (m : Exchange R) (c : R) : Nat :=
  total m.present fun f => m.take f c

/-- What the relata present give to `c`. -/
def Exchange.given (m : Exchange R) (c : R) : Nat :=
  total m.present fun f => m.give f c

/-- The world's move across the step from `t`: its relata's exchange. -/
def World.move (w : World) (t : Nat) : Exchange w.Relatum :=
  ⟨w.flow.present t, w.flow.take t, w.flow.give t⟩

end Exchange

end Becoming
