import Std

/-!
Relational first-order semantics with future-domain quantifiers. Relation
meanings are read from one supplied ambient interpretation; negation is
classical complementation. Future coverage is separate from the frame laws.
The comparison does not derive the ambient carrier, whole frame, or stable
interpretation from a foundation.
-/
namespace PotentialTruth
universe u v r

structure Frame (A : Type u) (W : Type v) where
  future : W → W → Prop
  domain : W → A → Prop
  refl : ∀ w, future w w
  trans : ∀ {w x y}, future w x → future x y → future w y
  monotone : ∀ {w x a}, future w x → domain w a → domain x a

def FutureCoverage (F : Frame A W) : Prop :=
  ∀ w a, ∃ x, F.future w x ∧ F.domain x a

def extend (a : A) (v : Fin n → A) : Fin (n+1) → A := Fin.cases a v

def Available (F : Frame A W) (w : W) (v : Fin n → A) : Prop := ∀ i, F.domain w (v i)

theorem available_future (F : Frame A W) {w x : W} (h : F.future w x)
    {v : Fin n → A} (hv : Available F w v) : Available F x v :=
  fun i => F.monotone h (hv i)

theorem available_extend (F : Frame A W) {w : W} {a : A} {v : Fin n → A}
    (ha : F.domain w a) (hv : Available F w v) : Available F w (extend a v) := by
  intro i
  exact Fin.cases ha (fun j => hv j) i

inductive Formula (Rel : Nat → Type r) : Nat → Type r where
  | eq {n} : Fin n → Fin n → Formula Rel n
  | atom {n k} : Rel k → (Fin k → Fin n) → Formula Rel n
  | neg {n} : Formula Rel n → Formula Rel n
  | conj {n} : Formula Rel n → Formula Rel n → Formula Rel n
  | ex {n} : Formula Rel (n+1) → Formula Rel n
  | all {n} : Formula Rel (n+1) → Formula Rel n

def Interpretation (Rel : Nat → Type r) (A : Type u) :=
  ∀ k, Rel k → (Fin k → A) → Prop

def sat (M : Interpretation Rel A) : Formula Rel n → (Fin n → A) → Prop
  | .eq i j, v => v i = v j
  | .atom rel args, v => M _ rel (fun i => v (args i))
  | .neg p, v => ¬ sat M p v
  | .conj p q, v => sat M p v ∧ sat M q v
  | .ex p, v => ∃ a, sat M p (extend a v)
  | .all p, v => ∀ a, sat M p (extend a v)

def potentialSat (F : Frame A W) (M : Interpretation Rel A) :
    Formula Rel n → W → (Fin n → A) → Prop
  | .eq i j, _, v => v i = v j
  | .atom rel args, _, v => M _ rel (fun i => v (args i))
  | .neg p, w, v => ¬ potentialSat F M p w v
  | .conj p q, w, v => potentialSat F M p w v ∧ potentialSat F M q w v
  | .ex p, w, v => ∃ x, F.future w x ∧ ∃ a, F.domain x a ∧ potentialSat F M p x (extend a v)
  | .all p, w, v => ∀ x, F.future w x → ∀ a, F.domain x a → potentialSat F M p x (extend a v)

theorem potential_iff_global (F : Frame A W) (hc : FutureCoverage F)
    (M : Interpretation Rel A) (p : Formula Rel n) (w : W) (v : Fin n → A)
    (hv : Available F w v) : potentialSat F M p w v ↔ sat M p v := by
  induction p generalizing w with
  | eq i j => exact Iff.rfl
  | atom rel args => exact Iff.rfl
  | neg p ih => exact not_congr (ih w v hv)
  | conj p q ihp ihq => exact and_congr (ihp w v hv) (ihq w v hv)
  | ex p ih =>
    constructor
    · rintro ⟨x, hwx, a, ha, hp⟩
      exact ⟨a, (ih x _ (available_extend F ha (available_future F hwx hv))).mp hp⟩
    · rintro ⟨a, ha⟩
      obtain ⟨x, hwx, hax⟩ := hc w a
      exact ⟨x, hwx, a, hax, (ih x _ (available_extend F hax (available_future F hwx hv))).mpr ha⟩
  | all p ih =>
    constructor
    · intro h a
      obtain ⟨x, hwx, ha⟩ := hc w a
      exact (ih x _ (available_extend F ha (available_future F hwx hv))).mp (h x hwx a ha)
    · intro h x hwx a ha
      exact (ih x _ (available_extend F ha (available_future F hwx hv))).mpr (h a)

def emptyAssignment (A : Type u) : Fin 0 → A := fun i => Fin.elim0 i

theorem sentence_agreement (F : Frame A W) (hc : FutureCoverage F)
    (M : Interpretation Rel A) (p : Formula Rel 0) (w : W) :
    potentialSat F M p w (emptyAssignment A) ↔ sat M p (emptyAssignment A) :=
  potential_iff_global F hc M p w _ (fun i => Fin.elim0 i)

theorem future_invariance (F : Frame A W) (hc : FutureCoverage F)
    (M : Interpretation Rel A) (p : Formula Rel n) {w x : W} (hwx : F.future w x)
    (v : Fin n → A) (hv : Available F w v) :
    potentialSat F M p w v ↔ potentialSat F M p x v :=
  (potential_iff_global F hc M p w v hv).trans
    (potential_iff_global F hc M p x v (available_future F hwx hv)).symm

def prefixFrame : Frame Nat Nat where
  future w x := w ≤ x
  domain w a := a < w
  refl := Nat.le_refl
  trans := Nat.le_trans
  monotone h ha := Nat.lt_of_lt_of_le ha h

theorem prefix_coverage : FutureCoverage prefixFrame := by
  intro w a
  exact ⟨Nat.max w (a+1), Nat.le_max_left _ _,
    Nat.lt_of_lt_of_le (Nat.lt_succ_self a) (Nat.le_max_right _ _)⟩

theorem prefix_domain_finite (w : Nat) :
    ∃ l : List Nat, ∀ a, prefixFrame.domain w a ↔ a ∈ l :=
  ⟨List.range w, fun _a => (List.mem_range).symm⟩

theorem prefix_no_full_world (w : Nat) : ¬ ∀ a, prefixFrame.domain w a := by
  intro h
  exact Nat.lt_irrefl w (h w)

inductive OrderRelation : Nat → Type where
  | less : OrderRelation 2

def natOrder : Interpretation OrderRelation Nat := fun _ rel v => match rel with
  | .less => v 0 < v 1

def unboundedSentence : Formula OrderRelation 0 :=
  .all (.ex (.atom .less (fun i => if i = 0 then 1 else 0)))

theorem unbounded_global : sat natOrder unboundedSentence (emptyAssignment Nat) := by
  intro a
  exact ⟨a+1, Nat.lt_succ_self a⟩

theorem unbounded_potential (w : Nat) :
    potentialSat prefixFrame natOrder unboundedSentence w (emptyAssignment Nat) :=
  (sentence_agreement prefixFrame prefix_coverage natOrder unboundedSentence w).mpr unbounded_global

/-- Current-stage quantifiers are a different interpretation from future quantifiers. -/
def currentSat (F : Frame A W) (M : Interpretation Rel A) :
    Formula Rel n → W → (Fin n → A) → Prop
  | .eq i j, _, v => v i = v j
  | .atom rel args, _, v => M _ rel (fun i => v (args i))
  | .neg p, w, v => ¬ currentSat F M p w v
  | .conj p q, w, v => currentSat F M p w v ∧ currentSat F M q w v
  | .ex p, w, v => ∃ a, F.domain w a ∧ currentSat F M p w (extend a v)
  | .all p, w, v => ∀ a, F.domain w a → currentSat F M p w (extend a v)

theorem unbounded_current_false {w : Nat} (hw : 0 < w) :
    ¬ currentSat prefixFrame natOrder unboundedSentence w (emptyAssignment Nat) := by
  intro h
  obtain ⟨a, ha, hlt⟩ := h (w-1) (by change w-1 < w; omega)
  change a < w at ha
  change w-1 < a at hlt
  omega

theorem unbounded_current_empty :
    currentSat prefixFrame natOrder unboundedSentence 0 (emptyAssignment Nat) := by
  intro a ha
  change a < 0 at ha
  omega

end PotentialTruth
