import IdealWarrant

/-!
The compact-basis representation and free extension theorems for nonempty ideals.
All orders, full directed completeness, and interpretations are explicit inputs.
These are conditional mathematical results, not proofs of ethical or metaphysical
priority. They use the same ideal definition as the completion-warrant theorem.
-/
namespace CompletionRole
open CompletionWarrant
universe u v w

structure Directed {α : Type u} (P : Poset α) (S : α → Prop) : Prop where
  nonempty : ∃ a, S a
  directed : ∀ a, S a → ∀ b, S b → ∃ c, S c ∧ P.le a c ∧ P.le b c

structure Dcpo {α : Type u} (P : Poset α) where
  sup : (S : α → Prop) → Directed P S → α
  upper : ∀ S h a, S a → P.le a (sup S h)
  least : ∀ S h b, (∀ a, S a → P.le a b) → P.le (sup S h) b

def Monotone {α : Type u} {β : Type v} (P : Poset α) (Q : Poset β)
    (f : α → β) : Prop := ∀ a b, P.le a b → Q.le (f a) (f b)

def Image {α : Type u} {β : Type v} (f : α → β) (S : α → Prop) : β → Prop :=
  fun b => ∃ a, S a ∧ f a = b

def Compact {α : Type u} {P : Poset α} (D : Dcpo P) (k : α) : Prop :=
  ∀ S h, P.le k (D.sup S h) → ∃ a, S a ∧ P.le k a

theorem image_directed {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {f : α → β} (hf : Monotone P Q f) {S : α → Prop} (hS : Directed P S) :
    Directed Q (Image f S) := by
  constructor
  · obtain ⟨a, ha⟩ := hS.nonempty
    exact ⟨f a, a, ha, rfl⟩
  · intro a ha b hb
    obtain ⟨x, hx, rfl⟩ := ha
    obtain ⟨y, hy, rfl⟩ := hb
    obtain ⟨z, hz, hxz, hyz⟩ := hS.directed x hx y hy
    exact ⟨f z, ⟨z, hz, rfl⟩, hf x z hxz, hf y z hyz⟩

theorem sup_congr {α : Type u} {P : Poset α} (D : Dcpo P)
    {S T : α → Prop} (hS : Directed P S) (hT : Directed P T)
    (h : ∀ a, S a ↔ T a) : D.sup S hS = D.sup T hT := by
  apply P.antisymm
  · exact D.least S hS _ (fun a ha => D.upper T hT a ((h a).mp ha))
  · exact D.least T hT _ (fun a ha => D.upper S hS a ((h a).mpr ha))

theorem sup_mono {α : Type u} {P : Poset α} (D : Dcpo P)
    {S T : α → Prop} (hS : Directed P S) (hT : Directed P T)
    (h : ∀ a, S a → T a) : P.le (D.sup S hS) (D.sup T hT) :=
  D.least S hS _ (fun a ha => D.upper T hT a (h a ha))

/-- Scott continuity stated through the supplied directed-supremum operation. -/
structure Continuous {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo P) (E : Dcpo Q) (f : α → β) : Prop where
  monotone : Monotone P Q f
  preserves : ∀ S h, f (D.sup S h) = E.sup (Image f S) (image_directed monotone h)


def idealPoset {α : Type u} (P : Poset α) : Poset (Ideal P) where
  le := Ideal.LE
  refl := Ideal.le_refl
  trans := Ideal.le_trans
  antisymm := Ideal.le_antisymm

theorem toDirectedFamily {α : Type u} {P : Poset α} {S : Ideal P → Prop}
    (h : Directed (idealPoset P) S) : DirectedFamily P S :=
  ⟨h.nonempty, fun hI hJ => h.directed _ hI _ hJ⟩

theorem fromDirectedFamily {α : Type u} {P : Poset α} {S : Ideal P → Prop}
    (h : DirectedFamily P S) : Directed (idealPoset P) S :=
  ⟨h.nonempty, fun _ hI _ hJ => h.directed hI hJ⟩

def idealDcpo {α : Type u} (P : Poset α) : Dcpo (idealPoset P) where
  sup S h := familyUnion P S (toDirectedFamily h)
  upper S h _ hi := le_familyUnion P S (toDirectedFamily h) hi
  least S h b hb := familyUnion_le P S (toDirectedFamily h) b hb

theorem principal_embedding {α : Type u} (P : Poset α) (p q : α) :
    Ideal.LE (principal P p) (principal P q) ↔ P.le p q := by
  constructor
  · intro h; exact h p (P.refl p)
  · exact principal_mono P

theorem principal_compact {α : Type u} (P : Poset α) (p : α) :
    Compact (idealDcpo P) (principal P p) := by
  intro S h hp
  obtain ⟨I, hI, hip⟩ := hp p (P.refl p)
  exact ⟨I, hI, (principal_le_iff P p I).mpr hip⟩

theorem principal_generation {α : Type u} (P : Poset α) (I : Ideal P) :
    (idealDcpo P).sup (principalFamily P I)
      (fromDirectedFamily (principalFamily_directed P I)) = I :=
  union_principalFamily P I

theorem compact_iff_principal {α : Type u} (P : Poset α) (I : Ideal P) :
    Compact (idealDcpo P) I ↔ ∃ p, I = principal P p := by
  constructor
  · intro hI
    have hle : Ideal.LE I ((idealDcpo P).sup (principalFamily P I)
        (fromDirectedFamily (principalFamily_directed P I))) := by
      rw [principal_generation]; exact Ideal.le_refl I
    obtain ⟨J, ⟨p, hp, rfl⟩, hIJ⟩ := hI _ _ hle
    exact ⟨p, Ideal.le_antisymm hIJ ((principal_le_iff P p I).mpr hp)⟩
  · rintro ⟨p, rfl⟩; exact principal_compact P p

theorem ideal_directed {α : Type u} {P : Poset α} (I : Ideal P) :
    Directed P I.mem :=
  ⟨I.nonempty, fun _ hp _ hq => I.directed hp hq⟩

def extend {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P) : β :=
  D.sup (Image f I.mem) (image_directed hf (ideal_directed I))

theorem extend_upper {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P)
    (p : α) (hp : I.mem p) : Q.le (f p) (extend D f hf I) :=
  D.upper _ _ _ ⟨p, hp, rfl⟩

theorem extend_least {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P)
    (b : β) (hb : ∀ p, I.mem p → Q.le (f p) b) :
    Q.le (extend D f hf I) b := by
  apply D.least
  rintro a ⟨p, hp, rfl⟩
  exact hb p hp

theorem extend_monotone {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) :
    Monotone (idealPoset P) Q (extend D f hf) := by
  intro I J h
  exact extend_least D f hf I _ (fun p hp => extend_upper D f hf J p (h p hp))

theorem extend_principal {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) (p : α) :
    extend D f hf (principal P p) = f p := by
  apply Q.antisymm
  · exact extend_least D f hf _ _ (fun q hq => hf q p hq)
  · exact extend_upper D f hf _ p (P.refl p)

theorem extend_continuous {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f) :
    Continuous (idealDcpo P) D (extend D f hf) := by
  refine ⟨extend_monotone D f hf, ?_⟩
  intro S hS
  apply Q.antisymm
  · apply extend_least
    intro p hp
    obtain ⟨I, hI, hip⟩ := hp
    exact Q.trans (extend_upper D f hf I p hip) (D.upper _ _ _ ⟨I, hI, rfl⟩)
  · apply D.least
    rintro b ⟨I, hI, rfl⟩
    apply extend_monotone D f hf I _
    exact (idealDcpo P).upper S hS I hI

theorem extend_unique {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo Q) (f : α → β) (hf : Monotone P Q f)
    (g : Ideal P → β) (hg : Continuous (idealDcpo P) D g)
    (he : ∀ p, g (principal P p) = f p) (I : Ideal P) :
    g I = extend D f hf I := by
  apply Q.antisymm
  · have hgen := hg.preserves (principalFamily P I)
      (fromDirectedFamily (principalFamily_directed P I))
    rw [principal_generation] at hgen
    rw [hgen]
    apply D.least
    rintro b ⟨J, ⟨p, hp, rfl⟩, rfl⟩
    rw [he]
    exact extend_upper D f hf I p hp
  · apply extend_least
    intro p hp
    rw [← he]
    exact hg.monotone _ I ((principal_le_iff P p I).mpr hp)

/-- The complete A2 existence-and-uniqueness statement, pointwise in the map. -/
theorem unique_continuous_extension {α : Type u} {β : Type v}
    {P : Poset α} {Q : Poset β} (D : Dcpo Q) (f : α → β)
    (hf : Monotone P Q f) :
    ∃ g : Ideal P → β, Continuous (idealDcpo P) D g ∧
      (∀ p, g (principal P p) = f p) ∧
      ∀ h, Continuous (idealDcpo P) D h →
        (∀ p, h (principal P p) = f p) → ∀ I, h I = g I := by
  exact ⟨extend D f hf, extend_continuous D f hf, extend_principal D f hf,
    fun h hh he I => extend_unique D f hf h hh he I⟩


/-- A named approximation role: embedding, compactness, and full generation. -/
structure BasisRole {α : Type u} {β : Type v} (P : Poset α) (Q : Poset β)
    (D : Dcpo Q) (e : α → β) : Prop where
  embedding : ∀ p q, Q.le (e p) (e q) ↔ P.le p q
  compact : ∀ p, Compact D (e p)
  approximants : ∀ x, Directed P (fun p => Q.le (e p) x)
  generates : ∀ x, D.sup (Image e (fun p => Q.le (e p) x))
    (image_directed (fun p q h => (embedding p q).mpr h) (approximants x)) = x

theorem basis_monotone {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) : Monotone P Q e :=
  fun p q h => (R.embedding p q).mpr h

def profile {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) (x : β) : Ideal P where
  mem p := Q.le (e p) x
  nonempty := (R.approximants x).nonempty
  lower hpq hqx := Q.trans (basis_monotone R _ _ hpq) hqx
  directed hp hq := (R.approximants x).directed _ hp _ hq

theorem profile_monotone {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) :
    Monotone Q (idealPoset P) (profile R) :=
  fun _ _ h _ hp => Q.trans hp h

theorem profile_extend {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) (I : Ideal P) :
    profile R (extend D e (basis_monotone R) I) = I := by
  apply Ideal.ext
  intro p
  constructor
  · intro hp
    obtain ⟨b, ⟨q, hq, rfl⟩, hpq⟩ := R.compact p _ _ hp
    exact I.lower ((R.embedding p q).mp hpq) hq
  · intro hp
    exact extend_upper D e (basis_monotone R) I p hp

theorem extend_profile {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) (x : β) :
    extend D e (basis_monotone R) (profile R x) = x := R.generates x

structure OrderIso {α : Type u} {β : Type v} (P : Poset α) (Q : Poset β) where
  forward : α → β
  backward : β → α
  forward_mono : Monotone P Q forward
  backward_mono : Monotone Q P backward
  backward_forward : ∀ x, backward (forward x) = x
  forward_backward : ∀ y, forward (backward y) = y

theorem orderIso_continuous {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    (D : Dcpo P) (E : Dcpo Q) (F : OrderIso P Q) :
    Continuous D E F.forward := by
  refine ⟨F.forward_mono, ?_⟩
  intro S hS
  apply Q.antisymm
  · have h : P.le (D.sup S hS)
        (F.backward (E.sup (Image F.forward S) (image_directed F.forward_mono hS))) := by
      apply D.least
      intro a ha
      have hb := F.backward_mono _ _ (E.upper (Image F.forward S)
        (image_directed F.forward_mono hS) (F.forward a) ⟨a, ha, rfl⟩)
      rw [F.backward_forward] at hb
      exact hb
    have hh := F.forward_mono _ _ h
    rw [F.forward_backward] at hh
    exact hh
  · apply E.least
    rintro b ⟨a, ha, rfl⟩
    exact F.forward_mono _ _ (D.upper S hS a ha)

def basisIso {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) :
    OrderIso (idealPoset P) Q where
  forward := extend D e (basis_monotone R)
  backward := profile R
  forward_mono := extend_monotone D e (basis_monotone R)
  backward_mono := profile_monotone R
  backward_forward := profile_extend R
  forward_backward := extend_profile R

theorem basisIso_preserves {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e) (p : α) :
    (basisIso R).forward (principal P p) = e p :=
  extend_principal D e (basis_monotone R) p

theorem basisIso_unique {α : Type u} {β : Type v} {P : Poset α} {Q : Poset β}
    {D : Dcpo Q} {e : α → β} (R : BasisRole P Q D e)
    (F : OrderIso (idealPoset P) Q) (hF : ∀ p, F.forward (principal P p) = e p)
    (I : Ideal P) : F.forward I = (basisIso R).forward I :=
  extend_unique D e (basis_monotone R) F.forward
    (orderIso_continuous (idealDcpo P) D F) hF I

theorem basisIso_backward_unique {α : Type u} {β : Type v}
    {P : Poset α} {Q : Poset β} {D : Dcpo Q} {e : α → β}
    (R : BasisRole P Q D e) (F : OrderIso (idealPoset P) Q)
    (hF : ∀ p, F.forward (principal P p) = e p) (x : β) :
    F.backward x = (basisIso R).backward x := by
  have h := congrArg (basisIso R).backward (basisIso_unique R F hF (F.backward x))
  rw [F.forward_backward, (basisIso R).backward_forward] at h
  exact h.symm

theorem ideal_basis_role {α : Type u} (P : Poset α) :
    BasisRole P (idealPoset P) (idealDcpo P) (principal P) := by
  refine ⟨principal_embedding P, principal_compact P, ?_, ?_⟩
  · intro I
    constructor
    · obtain ⟨p, hp⟩ := I.nonempty
      exact ⟨p, (principal_le_iff P p I).mpr hp⟩
    · intro p hp q hq
      obtain ⟨r, hr, hpr, hqr⟩ := I.directed
        ((principal_le_iff P p I).mp hp) ((principal_le_iff P q I).mp hq)
      exact ⟨r, (principal_le_iff P r I).mpr hr, hpr, hqr⟩
  · intro I
    apply Ideal.ext
    intro p
    constructor
    · rintro ⟨J, ⟨q, hq, rfl⟩, hp⟩
      exact hq p hp
    · intro hp
      exact ⟨principal P p, ⟨p, (principal_le_iff P p I).mpr hp, rfl⟩, P.refl p⟩

/-- A3: existence and uniqueness, for both directions, of the basis-fixing iso. -/
theorem unique_basis_representation {α : Type u} {β : Type v}
    {P : Poset α} {Q : Poset β} {D : Dcpo Q} {e : α → β}
    (R : BasisRole P Q D e) :
    ∃ F : OrderIso (idealPoset P) Q,
      (∀ p, F.forward (principal P p) = e p) ∧
      ∀ G : OrderIso (idealPoset P) Q,
        (∀ p, G.forward (principal P p) = e p) →
        (∀ I, G.forward I = F.forward I) ∧ (∀ x, G.backward x = F.backward x) :=
  ⟨basisIso R, basisIso_preserves R,
    fun G hG => ⟨basisIso_unique R G hG, basisIso_backward_unique R G hG⟩⟩


/-- Logical truth values ordered by implication, equivalent classically to 0 < 1. -/
def truthPoset : Poset Prop where
  le p q := p → q
  refl _ h := h
  trans h k x := k (h x)
  antisymm h k := propext ⟨h, k⟩

def truthDcpo : Dcpo truthPoset where
  sup S _ := ∃ p, S p ∧ p
  upper _ _ p hp ht := ⟨p, hp, ht⟩
  least _ _ _ hb := by
    rintro ⟨p, hp, ht⟩
    exact hb p hp ht

theorem positive_reading_monotone {α : Type u} (P : Poset α) (p : α) :
    Monotone P truthPoset (fun q => P.le p q) :=
  fun _ _ h hp => P.trans hp h

/-- A2a: the extended positive reading holds exactly at ideals containing p. -/
theorem positive_reading_membership {α : Type u} (P : Poset α) (p : α) (I : Ideal P) :
    extend truthDcpo (fun q => P.le p q) (positive_reading_monotone P p) I ↔ I.mem p := by
  constructor
  · rintro ⟨b, ⟨q, hq, rfl⟩, hpq⟩
    exact I.lower hpq hq
  · intro hp
    exact ⟨P.le p p, ⟨p, hp, rfl⟩, P.refl p⟩

theorem positive_readings_separate {α : Type u} (P : Poset α) (I J : Ideal P)
    (h : ∀ p, extend truthDcpo (fun q => P.le p q) (positive_reading_monotone P p) I ↔
      extend truthDcpo (fun q => P.le p q) (positive_reading_monotone P p) J) : I = J := by
  apply Ideal.ext
  intro p
  exact (positive_reading_membership P p I).symm.trans
    ((h p).trans (positive_reading_membership P p J))

end CompletionRole

/- Kernel axiom audit for every named theorem in this module. -/
#print axioms CompletionRole.image_directed
#print axioms CompletionRole.sup_congr
#print axioms CompletionRole.sup_mono
#print axioms CompletionRole.toDirectedFamily
#print axioms CompletionRole.fromDirectedFamily
#print axioms CompletionRole.principal_embedding
#print axioms CompletionRole.principal_compact
#print axioms CompletionRole.principal_generation
#print axioms CompletionRole.compact_iff_principal
#print axioms CompletionRole.ideal_directed
#print axioms CompletionRole.extend_upper
#print axioms CompletionRole.extend_least
#print axioms CompletionRole.extend_monotone
#print axioms CompletionRole.extend_principal
#print axioms CompletionRole.extend_continuous
#print axioms CompletionRole.extend_unique
#print axioms CompletionRole.unique_continuous_extension
#print axioms CompletionRole.basis_monotone
#print axioms CompletionRole.profile_monotone
#print axioms CompletionRole.profile_extend
#print axioms CompletionRole.extend_profile
#print axioms CompletionRole.orderIso_continuous
#print axioms CompletionRole.basisIso_preserves
#print axioms CompletionRole.basisIso_unique
#print axioms CompletionRole.basisIso_backward_unique
#print axioms CompletionRole.ideal_basis_role
#print axioms CompletionRole.unique_basis_representation
#print axioms CompletionRole.positive_reading_monotone
#print axioms CompletionRole.positive_reading_membership
#print axioms CompletionRole.positive_readings_separate
