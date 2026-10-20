universe u v

/-- Same shape as `Learning.Lumped`: `g` reads nothing that `π` does not. -/
def Lumped {I : Sort u} {K : Sort v} {V : Sort v} (π : I → K) (g : I → V) : Prop :=
  ∀ i i', π i = π i' → g i = g i'

/-- (A) propext is exactly: every reading of a proposition respects interderivability. -/
theorem readings_respect_iff_propext :
    (∀ (g : Prop → Prop) (a b : Prop), (a ↔ b) → g a = g b) ↔ (∀ a b : Prop, (a ↔ b) → a = b) :=
  ⟨fun all a b h => all id a b h, fun ext g a b h => congrArg g (ext a b h)⟩

/-- Formulas built by relations alone: atoms, connectives, quantifiers over any type. -/
inductive Form (α : Type u) : Type (u+1) where
  | atom : α → Form α
  | top : Form α
  | bot : Form α
  | and : Form α → Form α → Form α
  | or : Form α → Form α → Form α
  | imp : Form α → Form α → Form α
  | all {β : Type u} : (β → Form α) → Form α
  | ex {β : Type u} : (β → Form α) → Form α

def Form.eval {α : Type u} (ρ : α → Prop) : Form α → Prop
  | .atom x => ρ x
  | .top => True
  | .bot => False
  | .and p q => p.eval ρ ∧ q.eval ρ
  | .or p q => p.eval ρ ∨ q.eval ρ
  | .imp p q => p.eval ρ → q.eval ρ
  | .all f => ∀ b, (f b).eval ρ
  | .ex f => ∃ b, (f b).eval ρ

/-- (B) Every reading built by relations respects interderivability, with no propext. -/
theorem Form.eval_congr {α : Type u} {ρ σ : α → Prop} (h : ∀ x, ρ x ↔ σ x) :
    ∀ φ : Form α, φ.eval ρ ↔ φ.eval σ
  | .atom x => h x
  | .top => Iff.rfl
  | .bot => Iff.rfl
  | .and p q =>
    have hp := eval_congr h p; have hq := eval_congr h q
    ⟨fun ⟨x, y⟩ => ⟨hp.1 x, hq.1 y⟩, fun ⟨x, y⟩ => ⟨hp.2 x, hq.2 y⟩⟩
  | .or p q =>
    have hp := eval_congr h p; have hq := eval_congr h q
    ⟨fun t => t.elim (fun x => .inl (hp.1 x)) (fun y => .inr (hq.1 y)),
     fun t => t.elim (fun x => .inl (hp.2 x)) (fun y => .inr (hq.2 y))⟩
  | .imp p q =>
    have hp := eval_congr h p; have hq := eval_congr h q
    ⟨fun f x => hq.1 (f (hp.2 x)), fun f x => hq.2 (f (hp.1 x))⟩
  | .all f =>
    ⟨fun k b => (eval_congr h (f b)).1 (k b), fun k b => (eval_congr h (f b)).2 (k b)⟩
  | .ex f =>
    ⟨fun ⟨b, x⟩ => ⟨b, (eval_congr h (f b)).1 x⟩, fun ⟨b, x⟩ => ⟨b, (eval_congr h (f b)).2 x⟩⟩

/-- (D) The relation identified carries nothing further: any two witnesses of `a ↔ b` agree. -/
theorem iff_witness_unique {a b : Prop} (h h' : a ↔ b) : h = h' := rfl

/-- Contrast: between types, the relation carries content (two different equivalences). -/
def swap : Bool → Bool := fun x => !x
theorem two_equivalences : (id : Bool → Bool) ≠ swap := fun e => Bool.noConfusion (congrFun e true)

/-- (E) What is lost: the course. A value transported along propext does not compute. -/
def viaPropext : Nat :=
  @Eq.rec Prop (True ∧ True) (fun _ _ => Nat) 0 True
    (propext ⟨fun _ => trivial, fun _ => ⟨trivial, trivial⟩⟩)

/-- The value is still 0: the identification keeps the outcome, only the course stops. -/
theorem rec_const {a b : Prop} (e : a = b) : @Eq.rec Prop a (fun _ _ => Nat) 0 b e = 0 := by
  cases e; rfl

theorem viaPropext_eq : viaPropext = 0 := rec_const _

#print axioms readings_respect_iff_propext
#print axioms Form.eval_congr
#print axioms iff_witness_unique
#print axioms two_equivalences
#print axioms viaPropext_eq
#reduce viaPropext
