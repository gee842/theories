import Init

/-!
# A necessary constraint on the formation of joint possibility restrictions

Coordinates are analytical aspects of one admitted domain, not independent
substances. Rectangularity concerns recombination of possibilities, not
statistical independence. The theorem tests independent transition accounts;
it does not assume every actual process factorizes or derive modal warrant.
All types, domains and correspondences retain their stated mathematical scope.
-/
namespace RelationalFormation

universe u v w x
variable {A : Type u} {B : Type v} {C : Type w} {D : Type x}

def Rectangular (domain : A × B → Prop) : Prop :=
  ∀ a a' b b', domain (a, b) → domain (a', b') → domain (a, b')

def Post {S : Type u} {T : Type v} (step : S → T → Prop)
    (domain : S → Prop) (t : T) : Prop :=
  ∃ s, domain s ∧ step s t

def Separate (left : A → C → Prop) (right : B → D → Prop)
    (s : A × B) (t : C × D) : Prop :=
  left s.1 t.1 ∧ right s.2 t.2

def Factorizes (step : A × B → C × D → Prop) : Prop :=
  ∃ left right, ∀ s t, step s t ↔ Separate left right s t

theorem rectangular_transport {p q : A × B → Prop}
    (same : ∀ s, p s ↔ q s) (hp : Rectangular p) : Rectangular q := by
  intro a a' b b' hab ha'b'
  exact (same (a, b')).mp (hp a a' b b'
    ((same (a, b)).mpr hab) ((same (a', b')).mpr ha'b'))

theorem product_rectangular (p : A → Prop) (q : B → Prop) :
    Rectangular (fun s => p s.1 ∧ q s.2) := by
  intro _ _ _ _ hab ha'b'
  exact ⟨hab.1, ha'b'.2⟩

theorem separate_post_rectangular (left : A → C → Prop) (right : B → D → Prop)
    {domain : A × B → Prop} (h : Rectangular domain) :
    Rectangular (Post (Separate left right) domain) := by
  intro c c' d d' hcd hc'd'
  obtain ⟨⟨a, b⟩, hab, hac, _⟩ := hcd
  obtain ⟨⟨a', b'⟩, ha'b', _, hb'd'⟩ := hc'd'
  exact ⟨(a, b'), h a a' b b' hab ha'b', hac, hb'd'⟩

theorem factorized_post_rectangular {step : A × B → C × D → Prop}
    {domain : A × B → Prop} (h : Rectangular domain) (f : Factorizes step) :
    Rectangular (Post step domain) := by
  obtain ⟨left, right, same⟩ := f
  apply rectangular_transport (p := Post (Separate left right) domain)
    (q := Post step domain) _ (separate_post_rectangular left right h)
  intro t
  constructor
  · intro ht
    obtain ⟨s, hs, hst⟩ := ht
    exact ⟨s, hs, (same s t).mpr hst⟩
  · intro ht
    obtain ⟨s, hs, hst⟩ := ht
    exact ⟨s, hs, (same s t).mp hst⟩

/-- The newly restricted joint domain rules out every factorization, not just
    one chosen pair of local update functions. -/
theorem new_restriction_excludes_factorization {step : A × B → C × D → Prop}
    {domain : A × B → Prop} (initial : Rectangular domain)
    (formed : ¬ Rectangular (Post step domain)) : ¬ Factorizes step := by
  intro separate
  exact formed (factorized_post_rectangular initial separate)

/-- Faithful recoding of each already-identified aspect preserves the test in
    both directions. Mixing the aspects is a different question. -/
theorem rectangular_iff_under_injective_recoding (f : A → C) (g : B → D)
    (hf : ∀ a a', f a = f a' → a = a') (hg : ∀ b b', g b = g b' → b = b')
    (domain : A × B → Prop) :
    Rectangular (Post (Separate (fun a c => c = f a) (fun b d => d = g b)) domain) ↔
      Rectangular domain := by
  constructor
  · intro h a a' b b' hab ha'b'
    have first : Post (Separate (fun a c => c = f a) (fun b d => d = g b)) domain
        (f a, g b) := ⟨(a, b), hab, rfl, rfl⟩
    have second : Post (Separate (fun a c => c = f a) (fun b d => d = g b)) domain
        (f a', g b') := ⟨(a', b'), ha'b', rfl, rfl⟩
    obtain ⟨⟨x, y⟩, hxy, hx, hy⟩ := h (f a) (f a') (g b) (g b') first second
    have ax : a = x := hf a x hx
    have by' : b' = y := hg b' y hy
    cases ax
    cases by'
    exact hxy
  · exact separate_post_rectangular (fun a c => c = f a) (fun b d => d = g b)

def Reach (initial : A × B → Prop)
    (left : Nat → A → A → Prop) (right : Nat → B → B → Prop) :
    Nat → (A × B → Prop)
  | 0 => initial
  | n + 1 => Post (Separate (left n) (right n)) (Reach initial left right n)

theorem separate_reach_rectangular (initial : A × B → Prop)
    (left : Nat → A → A → Prop) (right : Nat → B → B → Prop)
    (h : Rectangular initial) (n : Nat) : Rectangular (Reach initial left right n) := by
  induction n with
  | zero => exact h
  | succ n ih => exact separate_post_rectangular (left n) (right n) ih

theorem restricted_target_has_no_separate_history
    (initial target : A × B → Prop) (h : Rectangular initial)
    (restricted : ¬ Rectangular target) :
    ¬ ∃ left right n, ∀ s, Reach initial left right n s ↔ target s := by
  intro ⟨left, right, n, same⟩
  exact restricted (rectangular_transport same (separate_reach_rectangular initial left right h n))

def Full : Bool × Bool → Prop := fun _ => True
def Diagonal (s : Bool × Bool) : Prop := s.1 = s.2
def Copy (s t : Bool × Bool) : Prop := t = (s.1, s.1)
def Identity (s t : Bool × Bool) : Prop := t = s
def Select (domain criterion : Bool × Bool → Prop) (s : Bool × Bool) : Prop :=
  domain s ∧ criterion s
def Reset (_s t : Bool × Bool) : Prop := t = (false, false)

theorem full_rectangular : Rectangular Full := by
  intro _ _ _ _ _ _
  exact True.intro

theorem diagonal_not_rectangular : ¬ Rectangular Diagonal := by
  intro h
  exact Bool.noConfusion (h false true false true rfl rfl)

theorem copy_post_iff_diagonal (t : Bool × Bool) : Post Copy Full t ↔ Diagonal t := by
  constructor
  · intro h
    obtain ⟨s, _, ht⟩ := h
    cases ht
    rfl
  · intro h
    refine ⟨(t.1, false), True.intro, ?_⟩
    cases t with
    | mk a b =>
      change a = b at h
      cases h
      rfl

theorem copy_does_not_factorize : ¬ Factorizes Copy := by
  apply new_restriction_excludes_factorization full_rectangular
  intro h
  exact diagonal_not_rectangular (rectangular_transport copy_post_iff_diagonal h)

theorem identity_post_iff (domain : Bool × Bool → Prop) (t : Bool × Bool) :
    Post Identity domain t ↔ domain t := by
  constructor
  · intro h
    obtain ⟨s, hs, ht⟩ := h
    cases ht
    exact hs
  · intro h
    exact ⟨t, h, rfl⟩

theorem identity_factorizes : Factorizes Identity := by
  refine ⟨(fun a c => c = a), (fun b d => d = b), ?_⟩
  intro s t
  constructor
  · intro h
    cases h
    exact ⟨rfl, rfl⟩
  · intro h
    cases s with
    | mk a b =>
      cases t with
      | mk c d =>
        obtain ⟨hc, hd⟩ := h
        cases hc
        cases hd
        rfl

/-- A final restriction can be inherited through entirely independent identity
    updates. It therefore does not by itself demonstrate new interaction. -/
theorem inherited_restriction_without_new_coupling :
    Factorizes Identity ∧ ¬ Rectangular (Post Identity Diagonal) := by
  refine ⟨identity_factorizes, ?_⟩
  intro h
  exact diagonal_not_rectangular (rectangular_transport (identity_post_iff Diagonal) h)

theorem selection_iff_diagonal (t : Bool × Bool) :
    Select (Post Identity Full) Diagonal t ↔ Diagonal t := by
  constructor
  · intro h
    exact h.2
  · intro h
    exact ⟨⟨t, True.intro, rfl⟩, h⟩

theorem selection_can_introduce_restriction :
    Rectangular (Post Identity Full) ∧
      ¬ Rectangular (Select (Post Identity Full) Diagonal) := by
  refine ⟨factorized_post_rectangular full_rectangular identity_factorizes, ?_⟩
  intro h
  exact diagonal_not_rectangular (rectangular_transport selection_iff_diagonal h)

theorem fixed_common_mode_rectangular (mode : Bool) :
    Rectangular (fun s : Bool × Bool => s.1 = mode ∧ s.2 = mode) :=
  product_rectangular (fun a => a = mode) (fun b => b = mode)

theorem varying_common_mode_not_rectangular :
    ¬ Rectangular (fun s : Bool × Bool => ∃ mode, s.1 = mode ∧ s.2 = mode) := by
  intro h
  obtain ⟨mode, hf, ht⟩ := h false true false true
    ⟨false, rfl, rfl⟩ ⟨true, rfl, rfl⟩
  exact Bool.noConfusion (hf.trans ht.symm)

theorem reset_erases_restriction : Rectangular (Post Reset Diagonal) := by
  intro a a' b b' hab ha'b'
  obtain ⟨s, _, hs⟩ := hab
  obtain ⟨s', _, hs'⟩ := ha'b'
  have ha : a = false := congrArg Prod.fst hs
  have hb' : b' = false := congrArg Prod.snd hs'
  cases ha
  cases hb'
  exact ⟨(false, false), rfl, rfl⟩

#print axioms Rectangular
#print axioms Post
#print axioms Separate
#print axioms Factorizes
#print axioms Reach
#print axioms Full
#print axioms Diagonal
#print axioms Copy
#print axioms Identity
#print axioms Select
#print axioms Reset
#print axioms rectangular_transport
#print axioms product_rectangular
#print axioms separate_post_rectangular
#print axioms factorized_post_rectangular
#print axioms new_restriction_excludes_factorization
#print axioms rectangular_iff_under_injective_recoding
#print axioms separate_reach_rectangular
#print axioms restricted_target_has_no_separate_history
#print axioms full_rectangular
#print axioms diagonal_not_rectangular
#print axioms copy_post_iff_diagonal
#print axioms copy_does_not_factorize
#print axioms identity_post_iff
#print axioms identity_factorizes
#print axioms inherited_restriction_without_new_coupling
#print axioms selection_iff_diagonal
#print axioms selection_can_introduce_restriction
#print axioms fixed_common_mode_rectangular
#print axioms varying_common_mode_not_rectangular
#print axioms reset_erases_restriction

end RelationalFormation
