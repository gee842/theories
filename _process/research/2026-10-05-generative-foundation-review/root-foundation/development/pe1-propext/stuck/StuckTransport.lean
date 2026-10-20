import Becoming.PropositionIdentity

/-! PE1 kernel observation (not a core module; it uses `propext` on purpose). A value transported
along `propext` keeps its outcome (`viaPropext_eq`, by the core's `transport_const`, with
`propext` reported) but does not reduce: `#reduce` stops at the transport, and `rfl` and
`decide` fail. The two failing `example`s below are expected errors. -/

open Becoming.PropositionIdentity

def viaPropext : Nat :=
  @Eq.rec Prop (True ∧ True) (fun _ _ => Nat) 0 True
    (propext ⟨fun _ => trivial, fun _ => ⟨trivial, trivial⟩⟩)

theorem viaPropext_eq : viaPropext = 0 := transport_const _ 0

/-- Along `rfl` the same transport computes. -/
def viaRefl : Nat := @Eq.rec Prop True (fun _ _ => Nat) 0 True rfl

#print axioms viaPropext_eq
#print axioms transport_const
#reduce viaPropext
#reduce viaRefl
example : viaRefl = 0 := rfl
example : viaPropext = 0 := rfl
example : viaPropext = 0 := by decide
