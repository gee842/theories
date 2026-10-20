import Becoming.World

/-!
# Witnesses: the models the spine builds again and again

Many laws of the spine are shown exact by a small model: a process with no step or with one
step, a level that takes a few values and then stays, a flow in which nothing takes part, a
renewer feeding two takers. Each module used to build its own copy. This module states each
model once, with the choices that vary as parameters, and the modules' witnesses are its
instances: a witness states only what is special about it.

* **Processes.** The process that admits every step is `everyStep` of `Becoming.World`; the
  process that admits no step is `Witnesses.halted`; the process with one step, from `a` to `b`,
  is `Witnesses.single`. The process moving each configuration by a map is `Law.process` of
  `Becoming.Recurrence` (the flip is `Law.process not`).
* **Profiles.** A course of values that takes the values of a list and then stays at one value
  (`Witnesses.profile`): the levels, activities and amounts of the witnesses, over any type of
  values. `Witnesses.profile [1] 0` is one at the first step and zero after.
* **Flows and webs.** The flow in which nothing takes part (`Witnesses.emptyFlow`); one formation
  giving a fixed amount at every step and taking nothing (`Witnesses.giving`); a web with given
  levels and activity in which nothing requires, needs or draws on anything
  (`Witnesses.unrequired`).
* **A renewer and two takers.** One condition, a renewer giving to it and two takers drawing on
  it (`Witnesses.Member`, `Witnesses.relay`, `Witnesses.relayWeb`), with what each gives and
  takes, the level and the activity as parameters.

Nothing here is a law: the module holds definitions only, so that it lies below every module
that builds a witness. It imports only `Becoming.World`.
-/

namespace Becoming

universe u v

open Generative

namespace Witnesses

/-! ## Processes -/

/-- The process that admits no step. -/
def halted (S : Type u) (A : Type v) : Process S A := ⟨fun _ _ _ => False⟩

/-- The process with one step, from `a` to `b`, by any move. -/
def single {S : Type u} (A : Type v) (a b : S) : Process S A := ⟨fun s _ t => s = a ∧ t = b⟩

/-! ## Profiles -/

/-- The course that takes the values of `values` in order and then stays at `rest`. -/
def profile {α : Type u} : List α → α → Nat → α
  | [], rest, _ => rest
  | value :: _, _, 0 => value
  | _ :: values, rest, n + 1 => profile values rest n

/-! ## Flows and webs -/

/-- The flow in which nothing takes part. -/
def emptyFlow (F C : Type) : Flow F C := ⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- The formation `f` takes part at every step, taking nothing and giving `k` to every
condition. -/
def giving {F C : Type} (f : F) (k : Nat) : Flow F C := ⟨fun _ => [f], fun _ _ _ => 0, fun _ _ _ => k⟩

/-- The web with levels `level` and activity `active` in which nothing requires, needs or draws on
anything. -/
def unrequired {F C : Type} (level : Nat → C → Nat) (active : Nat → F → Prop) : Web F C :=
  ⟨level, active, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩

/-! ## A renewer and two takers -/

/-- A renewer and two takers sharing one condition. -/
inductive Member where
  | renewer
  | first
  | second

/-- The members in `present t` take part across the step from `t`: the renewer gives `gives`
units and takes nothing, the first takes `first` units and the second `second`, and neither
gives. -/
def relay (present : Nat → List Member) (gives first second : Nat) : Flow Member Unit where
  present := present
  take _ f _ := match f with
    | .renewer => 0
    | .first => first
    | .second => second
  give _ f _ := match f with
    | .renewer => gives
    | .first => 0
    | .second => 0

/-- The condition stands at `level t`, and the members active at `active t` each depend on it at
need one, the renewer included; the takers draw on it and the renewer does not. -/
def relayWeb (level : Nat → Nat) (active : Nat → Member → Prop) : Web Member Unit where
  level t _ := level t
  active := active
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => True

end Witnesses

end Becoming
