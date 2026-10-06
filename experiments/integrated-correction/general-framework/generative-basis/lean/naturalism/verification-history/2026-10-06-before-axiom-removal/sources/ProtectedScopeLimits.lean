import ProtectedScope

/-!
# Limits of the derived protected scope

Counterexamples found by the independent review of `ProtectedScope` and preserved here.

* With the scope the restraining history exercises, restraint registers as damage
  again: the one-shot act `restrain` is protected and exhausts itself
  (`restraint_damage_exercised`). So the scope that rescues commitment (`exercised`)
  does not rescue restraint, and the scope that rescues restraint (`allActivities`)
  does not rescue commitment.
* If the victim's activity can move to a state where harm is impossible, that activity
  removes `harm`, nothing is protected, and harm registers no damage even with every
  activity in scope (`escape_harm_unregistered`). The earlier restraint verdict depends
  on modelling the victim's activity as removing nothing.
* An unrecovered fall in `dip` is not damage either (`dip_fall_zero_not_damage`): damage
  compares two states and ignores whether recovery actually occurs.
-/

namespace Generative.Naturalism

/-- The restraining history. -/
def restrainRun : Run restraint .open .restrained :=
  .cons .restrain (show Situation.open = .open ∧ Situation.restrained = .restrained from ⟨rfl, rfl⟩) (.nil _)

theorem restraint_damage_exercised : Damages restraint (exercised restrainRun) .open .restrained :=
  ⟨.restrain, ⟨List.Mem.head _, fun c hc hne => by
      cases hc with
      | head => exact absurd rfl hne
      | tail _ h => cases h⟩,
    open_can .restrain, fun ⟨w, u, hu, v, hv⟩ => by
      have e := restrained_stuck w u hu; subst e; exact absurd hv.1 (by decide)⟩

/-- The victim's `live` may stay or escape to where `harm` is impossible. -/
inductive S2 | op | esc | hurt deriving DecidableEq
inductive D2 | live | harm deriving DecidableEq
def escape : Process S2 D2 where
  step s a t := match a with
    | .live => (s = .op ∧ (t = .op ∨ t = .esc)) ∨ (s = .esc ∧ t = .esc)
    | .harm => s = .op ∧ t = .hurt

theorem hurt_stuck : (w : List D2) → (u : S2) → Trace escape .hurt w u → u = .hurt
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: _, _, h => by
    obtain ⟨m, hs, _⟩ := trace_cons_iff.mp h
    cases a with
    | live => rcases hs with ⟨e, _⟩ | ⟨e, _⟩ <;> exact absurd e (by decide)
    | harm => exact absurd hs.1 (by decide)
theorem esc_stuck : (w : List D2) → (u : S2) → Trace escape .esc w u → u = .esc
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: rest, u, h => by
    obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
    cases a with
    | live =>
      rcases hs with ⟨e, _⟩ | ⟨_, e⟩
      · exact absurd e (by decide)
      · subst e; exact esc_stuck rest u hr
    | harm => exact absurd hs.1 (by decide)

theorem escape_live_removes_harm : Removes escape .live .harm :=
  ⟨.op, .esc, Or.inl ⟨rfl, Or.inr rfl⟩, can_of_enabled ⟨.hurt, show S2.op = .op ∧ S2.hurt = .hurt from ⟨rfl, rfl⟩⟩,
   fun ⟨w, u, hu, v, hv⟩ => by have e := esc_stuck w u hu; subst e; exact absurd hv.1 (by decide)⟩

theorem escape_harm_unregistered : ¬ Damages escape allActivities .op .hurt := by
  rintro ⟨b, ⟨_, hp⟩, _, _⟩
  cases b with
  | live => exact hp .harm True.intro (by decide) escape_live_removes_harm
  | harm =>
    exact hp .live True.intro (by decide) ⟨.op, .hurt, ⟨rfl, rfl⟩,
      can_of_enabled ⟨.op, Or.inl ⟨rfl, Or.inl rfl⟩⟩,
      fun ⟨w, u, hu, v, hv⟩ => by
        have e := hurt_stuck w u hu; subst e
        rcases hv with ⟨e, _⟩ | ⟨e, _⟩ <;> exact absurd e (by decide)⟩

theorem dip_fall_zero_not_damage (O : DipAct → Prop) : ¬ Damages dip O 2 0 := by
  rintro ⟨b, _, _, ht⟩
  apply ht
  cases b with
  | go => exact can_of_enabled ⟨2, show (2:Nat) ≤ 2 ∧ (0:Nat) ≤ 2+1 by decide⟩
  | use => exact ⟨[DipAct.go], 2, .cons (show (2:Nat) ≤ 2 ∧ (0:Nat) ≤ 2+1 by decide) (.nil 2),
      ⟨2, show (2:Nat) = 2 ∧ (2:Nat) = 2 from ⟨rfl, rfl⟩⟩⟩
end Generative.Naturalism

#print axioms Generative.Naturalism.restraint_damage_exercised
#print axioms Generative.Naturalism.hurt_stuck
#print axioms Generative.Naturalism.esc_stuck
#print axioms Generative.Naturalism.escape_live_removes_harm
#print axioms Generative.Naturalism.escape_harm_unregistered
#print axioms Generative.Naturalism.dip_fall_zero_not_damage
