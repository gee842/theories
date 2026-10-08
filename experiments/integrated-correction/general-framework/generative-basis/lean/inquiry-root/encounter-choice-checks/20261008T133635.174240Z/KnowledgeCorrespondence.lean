import Std

/-!
A correspondence component for the knowledge investigation. Histories are
whole local configurations; evidence and targets are projections from them.
These definitions concern exact answers, not a definition of knowledge.
Domain adequacy, semantic interpretation and cognitive uptake are not proved.
-/
namespace Generative.KnowledgeCorrespondence

universe u v

def SoundOn {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) (answer : E → Option Bool) : Prop :=
  ∀ h, D h → ∀ b, answer (evidence h) = some b → b = target h

def ExactOn {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) (answer : E → Option Bool) : Prop :=
  ∀ h, D h → answer (evidence h) = some (target h)

def Resolves {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) : Prop :=
  ∀ h k, D h → D k → evidence h = evidence k → target h = target k

theorem exact_is_sound {H : Type u} {E : Type v} {D : H → Prop}
    {evidence : H → E} {target : H → Bool} {answer : E → Option Bool}
    (h : ExactOn D evidence target answer) : SoundOn D evidence target answer := by
  intro x hx b hb
  have he : some b = some (target x) := hb.symm.trans (h x hx)
  exact Option.some.inj he

theorem exact_requires_resolution {H : Type u} {E : Type v} {D : H → Prop}
    {evidence : H → E} {target : H → Bool} {answer : E → Option Bool}
    (h : ExactOn D evidence target answer) : Resolves D evidence target := by
  intro x y hx hy he
  have hh := (h x hx).symm.trans ((congrArg answer he).trans (h y hy))
  exact Option.some.inj hh

noncomputable def decoder {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) (e : E) : Option Bool := by
  classical
  exact if h : ∃ x, D x ∧ evidence x = e then some (target (Classical.choose h)) else none

theorem resolution_admits_decoder {H : Type u} {E : Type v} {D : H → Prop}
    {evidence : H → E} {target : H → Bool} (h : Resolves D evidence target) :
    ExactOn D evidence target (decoder D evidence target) := by
  intro x hx
  have he : ∃ y, D y ∧ evidence y = evidence x := ⟨x, hx, rfl⟩
  simp only [decoder, dif_pos he]
  exact congrArg some (h _ x (Classical.choose_spec he).1 hx (Classical.choose_spec he).2)

theorem exact_possible_iff_resolves {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) :
    (∃ answer, ExactOn D evidence target answer) ↔ Resolves D evidence target := by
  constructor
  · rintro ⟨answer, h⟩
    exact exact_requires_resolution h
  · intro h
    exact ⟨decoder D evidence target, resolution_admits_decoder h⟩

theorem conflicting_fibre_forces_abstention {H : Type u} {E : Type v}
    {D : H → Prop} {evidence : H → E} {target : H → Bool}
    {answer : E → Option Bool} (sound : SoundOn D evidence target answer)
    {x y : H} (hx : D x) (hy : D y) (same : evidence x = evidence y)
    (different : target x ≠ target y) : answer (evidence x) = none := by
  cases he : answer (evidence x) with
  | none => rfl
  | some b =>
    have hb := sound x hx b he
    have hc := sound y hy b ((congrArg answer same).symm.trans he)
    exact False.elim (different (hb.symm.trans hc))

theorem sound_restricts_domain {H : Type u} {E : Type v} {D D' : H → Prop}
    {evidence : H → E} {target : H → Bool} {answer : E → Option Bool}
    (h : SoundOn D evidence target answer) (sub : ∀ x, D' x → D x) :
    SoundOn D' evidence target answer := by
  intro x hx b hb
  exact h x (sub x hx) b hb

theorem refinement_preserves_resolution {H : Type u} {E : Type v} {F : Type}
    {D : H → Prop} {evidence : H → E} {target : H → Bool}
    (h : Resolves D evidence target) (extra : H → F) :
    Resolves D (fun x => (evidence x, extra x)) target := by
  intro x y hx hy he
  exact h x y hx hy (congrArg Prod.fst he)

theorem preserved_record_preserves_exactness {H : Type u} {E : Type v} {M : Type}
    {D : H → Prop} {evidence : H → E} {target : H → Bool}
    {answer : E → Option Bool} (h : ExactOn D evidence target answer)
    (retain : E → M) (read : M → E)
    (faithful : ∀ x, D x → read (retain (evidence x)) = evidence x) :
    ExactOn D (fun x => retain (evidence x)) target (fun m => answer (read m)) := by
  intro x hx
  change answer (read (retain (evidence x))) = some (target x)
  rw [faithful x hx]
  exact h x hx

-- A stipulated family of histories containing both a target and channel state.
structure History where
  value : Bool
  reversed : Bool

def signal (h : History) : Bool := Bool.xor h.value h.reversed
def target (h : History) : Bool := h.value
def allHistories (_ : History) : Prop := True
def normal (h : History) : Prop := h.reversed = false

-- A reference intervention stipulated to have value false exposes orientation.
def reference (h : History) : Bool := Bool.xor false h.reversed
def pairedEvidence (h : History) : Bool × Bool := (signal h, reference h)
def decodePair (e : Bool × Bool) : Option Bool := some (Bool.xor e.1 e.2)
def direct (b : Bool) : Option Bool := some b

theorem calibrated_pair_exact : ExactOn allHistories pairedEvidence target decodePair := by
  intro h _
  cases h with
  | mk v r => cases v <;> cases r <;> rfl

theorem raw_signal_not_resolving : ¬ Resolves allHistories signal target := by
  intro h
  have bad := h ⟨false, false⟩ ⟨true, true⟩ trivial trivial rfl
  cases bad

theorem no_exact_raw_decoder : ¬ ∃ answer, ExactOn allHistories signal target answer := by
  rintro ⟨answer, h⟩
  exact raw_signal_not_resolving (exact_requires_resolution h)

theorem every_sound_raw_decoder_abstains (answer : Bool → Option Bool)
    (h : SoundOn allHistories signal target answer) (e : Bool) : answer e = none := by
  cases e with
  | false =>
    exact conflicting_fibre_forces_abstention h (x := ⟨false, false⟩)
      (y := ⟨true, true⟩) trivial trivial rfl (by decide)
  | true =>
    exact conflicting_fibre_forces_abstention h (x := ⟨true, false⟩)
      (y := ⟨false, true⟩) trivial trivial rfl (by decide)

theorem direct_exact_on_normal : ExactOn normal signal target direct := by
  intro h hn
  cases h with
  | mk v r =>
    simp only [normal] at hn
    subst r
    cases v <;> rfl

theorem direct_fails_on_expanded_domain : ¬ SoundOn allHistories signal target direct := by
  intro h
  have bad := h ⟨false, true⟩ trivial true rfl
  cases bad

theorem lucky_actual_correct : direct (signal ⟨false, false⟩) = some (target ⟨false, false⟩) := rfl

-- Exactness can survive compression; preserving every raw datum is unnecessary.
theorem parity_record_exact :
    ExactOn allHistories (fun h => Bool.xor (pairedEvidence h).1 (pairedEvidence h).2)
      target direct := calibrated_pair_exact

theorem double_reversal_exact :
    ExactOn allHistories (fun h => !h.value) target (fun b => some (!b)) := by
  intro h _
  cases h with
  | mk v r => cases v <;> rfl

-- Fixed-content truth alone cannot distinguish a proof from a repeated guess.
def FixedContentSafe {H : Type u} (D : H → Prop) (p : Prop)
    (asserts : H → Prop) : Prop := ∀ h, D h → asserts h → p

theorem true_content_trivially_safe {H : Type u} (D asserts : H → Prop)
    {p : Prop} (hp : p) : FixedContentSafe D p asserts := by
  intro _ _ _
  exact hp

theorem abstention_sound {H : Type u} {E : Type v} (D : H → Prop)
    (evidence : H → E) (target : H → Bool) :
    SoundOn D evidence target (fun _ => none) := by
  intro _ _ _ h
  cases h

theorem abstention_not_exact {H : Type u} {E : Type v} {D : H → Prop}
    (evidence : H → E) (target : H → Bool) {x : H} (hx : D x) :
    ¬ ExactOn D evidence target (fun _ => none) := by
  intro h
  have bad := h x hx
  cases bad

end Generative.KnowledgeCorrespondence
