import ExplanatoryJointness

/-! When a footprint covers all support used below a part, local separation
propagates to all leaves. Footprints and exclusive support are local-model
premises, not universal primitives of generativity. -/
namespace Generative.ExplanatoryFootprints
open ExplanatoryJointness ExplanatoryUniqueness
universe u v w x y

variable {S : Type u} {R : Type v}

def Within (F : S → R → Prop) (J : S → S → S → Prop) : Prop :=
  ∀ s l r, J s l r → (∀ a, F l a → F s a) ∧ (∀ a, F r a → F s a)

def Separate (F : S → R → Prop) (J : S → S → S → Prop) : Prop :=
  ∀ s l r, J s l r → ∀ a, F l a → F r a → False

def Requests : Plan (List R) → List R
  | .leaf xs => xs
  | .pair p q => Requests p ++ Requests q

def Supported (F : S → R → Prop) (s : S) (xs : List R) : Prop :=
  xs.Nodup ∧ ∀ a, a ∈ xs → F s a

theorem realized_requests_within {F : S → R → Prop} {J : S → S → S → Prop}
    (within : Within F J) (p : Plan (List R)) :
    ∀ s, Realizes J (Supported F) s p → ∀ a, a ∈ Requests p → F s a := by
  induction p with
  | leaf xs => exact fun _ h => h.2
  | pair p q ihp ihq =>
    rintro s ⟨l, r, joint, hl, hr⟩ a mem
    rcases List.mem_append.mp mem with hp | hq
    · exact (within s l r joint).1 a (ihp l hl a hp)
    · exact (within s l r joint).2 a (ihq r hr a hq)

theorem realized_requests_nodup {F : S → R → Prop} {J : S → S → S → Prop}
    (within : Within F J) (separate : Separate F J) (p : Plan (List R)) :
    ∀ s, Realizes J (Supported F) s p → (Requests p).Nodup := by
  induction p with
  | leaf xs => exact fun _ h => h.1
  | pair p q ihp ihq =>
    rintro s ⟨l, r, joint, hl, hr⟩
    apply List.nodup_append.mpr
    refine ⟨ihp l hl, ihq r hr, ?_⟩
    intro a hp b hq eq
    subst b
    exact separate s l r joint a (realized_requests_within within p l hl a hp)
      (realized_requests_within within q r hr a hq)

theorem realized_requests_supported {F : S → R → Prop} {J : S → S → S → Prop}
    (within : Within F J) (separate : Separate F J) (p : Plan (List R)) (s : S)
    (h : Realizes J (Supported F) s p) : Supported F s (Requests p) :=
  ⟨realized_requests_nodup within separate p s h, realized_requests_within within p s h⟩

/-- List membership describes the footprint; duplication is tracked by the
request list, so taking one support twice is not erased by set union. -/
def support (s : List R) (a : R) : Prop := a ∈ s

def Apart (l r : List R) : Prop := ∀ a, a ∈ l → a ∈ r → False

def joint (s l r : List R) : Prop :=
  (∀ a, a ∈ l → a ∈ s) ∧ (∀ a, a ∈ r → a ∈ s) ∧ Apart l r

theorem joint_within : Within (@support R) joint := fun _ _ _ h => ⟨h.1, h.2.1⟩
theorem joint_separate : Separate (@support R) joint := fun _ _ _ h => h.2.2

theorem realize_from_supported (p : Plan (List R)) :
    ∀ s, Supported support s (Requests p) → Realizes joint (Supported support) s p := by
  induction p with
  | leaf xs => exact fun _ h => h
  | pair p q ihp ihq =>
    intro s h
    obtain ⟨hp, hq, hd⟩ := List.nodup_append.mp h.1
    refine ⟨Requests p, Requests q, ?_, ihp _ ⟨hp, fun _ ha => ha⟩,
      ihq _ ⟨hq, fun _ ha => ha⟩⟩
    exact ⟨fun a ha => h.2 a (List.mem_append_left _ ha),
      fun a ha => h.2 a (List.mem_append_right _ ha), fun a ha hb => hd a ha a hb rfl⟩

theorem realize_iff_supported (p : Plan (List R)) (s : List R) :
    Realizes joint (Supported support) s p ↔ Supported support s (Requests p) :=
  ⟨realized_requests_supported joint_within joint_separate p s, realize_from_supported p s⟩

theorem same_requests_same_realization (p q : Plan (List R)) (s : List R)
    (same : Requests p = Requests q) :
    Realizes joint (Supported support) s p ↔ Realizes joint (Supported support) s q := by
  rw [realize_iff_supported, realize_iff_supported, same]

theorem reassociation_preserves_realization (p q r : Plan (List R)) (s : List R) :
    Realizes joint (Supported support) s (.pair (.pair p q) r) ↔
      Realizes joint (Supported support) s (.pair p (.pair q r)) :=
  same_requests_same_realization _ _ s (List.append_assoc ..)

theorem permutation_preserves_realization (p q : Plan (List R)) (s : List R)
    (perm : (Requests p).Perm (Requests q)) :
    Realizes joint (Supported support) s p ↔ Realizes joint (Supported support) s q := by
  rw [realize_iff_supported, realize_iff_supported]
  constructor
  · intro h
    exact ⟨perm.nodup h.1, fun a ha => h.2 a (perm.mem_iff.mpr ha)⟩
  · intro h
    exact ⟨perm.symm.nodup h.1, fun a ha => h.2 a (perm.mem_iff.mp ha)⟩

/-- The previous code-plan lifting theorem now gains a checked global support
consequence, when its native relation satisfies the explicit footprint laws. -/
theorem code_plan_has_global_support {A : Type w} {O : Type x} {C : Type y}
    {m : Model S A O} {account : Presentation S (Test A O) C}
    (compact : JointCompact m) (exact : Exact (Holds m) account)
    (reduced : Reduced (Holds m) account) (F : S → R → Prop)
    (within : Within F m.joint) (separate : Separate F m.joint)
    (read : C → List R → Prop)
    (correct : ∀ s xs, read (account.encode s) xs ↔ Supported F s xs)
    (p : Plan (List R)) (s : S)
    (h : Realizes (codeJoint m account) read (account.encode s) p) :
    Supported F s (Requests p) :=
  realized_requests_supported within separate p s
    ((joint_plan_lifts compact exact reduced (Supported F) read correct p s).mp h)

end Generative.ExplanatoryFootprints

#print axioms Generative.ExplanatoryFootprints.realized_requests_within
#print axioms Generative.ExplanatoryFootprints.realized_requests_nodup
#print axioms Generative.ExplanatoryFootprints.realized_requests_supported
#print axioms Generative.ExplanatoryFootprints.joint_within
#print axioms Generative.ExplanatoryFootprints.joint_separate
#print axioms Generative.ExplanatoryFootprints.realize_from_supported
#print axioms Generative.ExplanatoryFootprints.realize_iff_supported
#print axioms Generative.ExplanatoryFootprints.same_requests_same_realization
#print axioms Generative.ExplanatoryFootprints.reassociation_preserves_realization
#print axioms Generative.ExplanatoryFootprints.permutation_preserves_realization
#print axioms Generative.ExplanatoryFootprints.code_plan_has_global_support
