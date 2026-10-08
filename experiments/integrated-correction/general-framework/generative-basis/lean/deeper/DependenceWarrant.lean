import Std

/-!
An audit of one grounding passage: from an observed joint formation to a
particular dependence attributed to it. This is an explicitly supplied finite
comparison, not a theory of all causes. Input, mode and output are coordinates
of one realization; no external acting subject is a primitive.
-/

namespace DependenceWarrant

inductive Route where
  | mediated
  | common
  deriving DecidableEq

inductive Mode where
  | ordinary
  | resetFirst
  deriving DecidableEq

def first (u : Bool) : Mode → Bool
  | .ordinary => u
  | .resetFirst => false

def realize (r : Route) (u : Bool) (m : Mode) : Bool × Bool :=
  let x := first u m
  (x, match r with
    | .mediated => x
    | .common => u)

def record (r : Route) (us : List Bool) : List (Bool × Bool) :=
  us.map (fun u => realize r u .ordinary)

/-- All ordinary histories agree, including changing ones. The specified
    reset distinguishes the routes. Nothing here shows that a physical reset
    actually has the interpretation assigned to it by `realize`. -/
theorem history_agreement_and_separation :
    (∀ us, record .mediated us = record .common us) ∧
    (∀ r, realize r false .ordinary ≠ realize r true .ordinary) ∧
    realize .mediated true .resetFirst = (false, false) ∧
    realize .common true .resetFirst = (false, true) := by
  refine ⟨?_, ?_, rfl, rfl⟩
  · intro us
    rfl
  · intro r
    cases r <;> decide

/-- Positive identification is exact within this two-route class, with the
    supplied reset semantics and identification of the inherited input. -/
theorem reset_identifies_route (r : Route) :
    (realize r true .resetFirst).2 = false ↔ r = .mediated := by
  cases r with
  | mediated => exact ⟨fun _ => rfl, fun _ => rfl⟩
  | common =>
    constructor
    · intro h
      exact Bool.noConfusion h
    · intro h
      exact Route.noConfusion h

/-- A simultaneous relational presentation of the same whole realization.
    This does not assume a metaphysically separate law or an external agent. -/
def joint (r : Route) (u : Bool) (m : Mode) (v : Bool × Bool) : Prop :=
  v.1 = first u m ∧
    (match r with
      | .mediated => v.2 = v.1
      | .common => v.2 = u)

/-- The joint account retains the whole declared interface, including resets.
    It is therefore an equivalent presentation, not an opposing countercase. -/
theorem joint_iff_realization (r : Route) (u : Bool) (m : Mode)
    (v : Bool × Bool) : joint r u m v ↔ v = realize r u m := by
  cases r with
  | mediated =>
    constructor
    · intro h
      exact Prod.ext h.1 (h.2.trans h.1)
    · intro h
      cases h
      exact ⟨rfl, rfl⟩
  | common =>
    constructor
    · intro h
      exact Prod.ext h.1 h.2
    · intro h
      cases h
      exact ⟨rfl, rfl⟩

#print axioms history_agreement_and_separation
#print axioms reset_identifies_route
#print axioms joint_iff_realization

end DependenceWarrant
