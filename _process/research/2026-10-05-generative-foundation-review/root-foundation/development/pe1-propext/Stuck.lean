def viaPropext : Nat :=
  @Eq.rec Prop (True ∧ True) (fun _ _ => Nat) 0 True
    (propext ⟨fun _ => trivial, fun _ => ⟨trivial, trivial⟩⟩)
example : viaPropext = 0 := rfl
example : viaPropext = 0 := by decide
