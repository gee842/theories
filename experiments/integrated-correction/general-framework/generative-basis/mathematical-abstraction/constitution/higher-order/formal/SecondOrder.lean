import CompletionExamples

/-!
Relational second-order semantics at arbitrary finite arities. The semantic
predicate ranges and ideal ranges are explicit inputs. The full-range result
uses every predicate and every ideal in Lean's supplied metatheory; it does not
derive that fullness from an independently restricted formation process.
-/
namespace SecondOrderReconstruction
open CompletionWarrant CompletionExamples
universe u

inductive RelVar : List Nat → Nat → Type where
  | here : RelVar (k :: Γ) k
  | there : RelVar Γ k → RelVar (l :: Γ) k

def Predicate (A : Type u) (k : Nat) := (Fin k → A) → Prop

def RelationIdeal (A : Type u) (k : Nat) := Ideal (finiteOrder (Fin k → A))

def PredicateEnv (A : Type u) (Γ : List Nat) := ∀ {k}, RelVar Γ k → Predicate A k

def IdealEnv (A : Type u) (Γ : List Nat) := ∀ {k}, RelVar Γ k → RelationIdeal A k

def extendIndividual (a : A) (v : Fin n → A) : Fin (n+1) → A := Fin.cases a v

def extendPredicate (R : Predicate A k) (ρ : PredicateEnv A Γ) : PredicateEnv A (k :: Γ) :=
  fun {_} r => match r with
    | .here => R
    | .there s => ρ s

def extendIdeal (I : RelationIdeal A k) (σ : IdealEnv A Γ) : IdealEnv A (k :: Γ) :=
  fun {_} r => match r with
    | .here => I
    | .there s => σ s

def encodeEnv (ρ : PredicateEnv A Γ) : IdealEnv A Γ := fun r => partsOf (ρ r)

def decodeEnv (σ : IdealEnv A Γ) : PredicateEnv A Γ := fun r => unionContents (σ r)

def EnvsRelated (ρ : PredicateEnv A Γ) (σ : IdealEnv A Γ) : Prop :=
  ∀ {k} (r : RelVar Γ k) (t : Fin k → A), ρ r t ↔ unionContents (σ r) t

theorem related_encode (ρ : PredicateEnv A Γ) : EnvsRelated ρ (encodeEnv ρ) :=
  fun r t => (union_partsOf (ρ r) t).symm

theorem related_decode (σ : IdealEnv A Γ) : EnvsRelated (decodeEnv σ) σ :=
  fun _ _ => Iff.rfl

theorem decode_encode (ρ : PredicateEnv A Γ) :
    @Eq (PredicateEnv A Γ) (decodeEnv (encodeEnv ρ)) ρ := by
  funext k r t
  exact propext (union_partsOf (ρ r) t)

theorem encode_decode (σ : IdealEnv A Γ) :
    @Eq (IdealEnv A Γ) (encodeEnv (decodeEnv σ)) σ := by
  funext k r
  exact partsOf_union (σ r)

theorem related_extend {ρ : PredicateEnv A Γ} {σ : IdealEnv A Γ}
    (h : EnvsRelated ρ σ) {R : Predicate A k} {I : RelationIdeal A k}
    (hi : ∀ t, R t ↔ unionContents I t) :
    EnvsRelated (extendPredicate R ρ) (extendIdeal I σ) := by
  intro l r t
  cases r with
  | here => exact hi t
  | there r => exact h r t

theorem related_relation_eq {ρ : PredicateEnv A Γ} {σ : IdealEnv A Γ}
    (h : EnvsRelated ρ σ) (r s : RelVar Γ k) : ρ r = ρ s ↔ σ r = σ s := by
  constructor
  · intro he
    have hu : unionContents (σ r) = unionContents (σ s) := by
      funext t
      exact propext ((h r t).symm.trans ((congrFun he t).to_iff.trans (h s t)))
    have heq := congrArg (fun R : Predicate A k => partsOf R) hu
    simpa only [partsOf_union] using heq
  · intro he
    funext t
    apply propext
    have hr := h r t
    change ρ r t ↔ unionContents (σ r) t at hr
    rw [he] at hr
    exact hr.trans (h s t).symm

inductive Formula : Nat → List Nat → Type where
  | equal {n Γ} : Fin n → Fin n → Formula n Γ
  | apply {n Γ k} : RelVar Γ k → (Fin k → Fin n) → Formula n Γ
  | relationEqual {n Γ k} : RelVar Γ k → RelVar Γ k → Formula n Γ
  | neg {n Γ} : Formula n Γ → Formula n Γ
  | conj {n Γ} : Formula n Γ → Formula n Γ → Formula n Γ
  | existsIndividual {n Γ} : Formula (n+1) Γ → Formula n Γ
  | existsRelation {n Γ k} : Formula n (k :: Γ) → Formula n Γ

def PredicateDomain (A : Type u) := ∀ k, Predicate A k → Prop

def IdealDomain (A : Type u) := ∀ k, RelationIdeal A k → Prop

def PredicateSat (C : PredicateDomain A) :
    Formula n Γ → (Fin n → A) → PredicateEnv A Γ → Prop
  | .equal i j, v, _ => v i = v j
  | .apply r args, v, ρ => ρ r (fun i => v (args i))
  | .relationEqual r s, _, ρ => ρ r = ρ s
  | .neg p, v, ρ => ¬ PredicateSat C p v ρ
  | .conj p q, v, ρ => PredicateSat C p v ρ ∧ PredicateSat C q v ρ
  | .existsIndividual p, v, ρ => ∃ a, PredicateSat C p (extendIndividual a v) ρ
  | @Formula.existsRelation n Γ k p, v, ρ =>
      ∃ R, C k R ∧ PredicateSat C p v (extendPredicate R ρ)

def IdealSat (D : IdealDomain A) :
    Formula n Γ → (Fin n → A) → IdealEnv A Γ → Prop
  | .equal i j, v, _ => v i = v j
  | .apply r args, v, σ => unionContents (σ r) (fun i => v (args i))
  | .relationEqual r s, _, σ => σ r = σ s
  | .neg p, v, σ => ¬ IdealSat D p v σ
  | .conj p q, v, σ => IdealSat D p v σ ∧ IdealSat D q v σ
  | .existsIndividual p, v, σ => ∃ a, IdealSat D p (extendIndividual a v) σ
  | @Formula.existsRelation n Γ k p, v, σ =>
      ∃ I, D k I ∧ IdealSat D p v (extendIdeal I σ)

def DomainsRelated (C : PredicateDomain A) (D : IdealDomain A) : Prop :=
  ∀ k (R : Predicate A k) (I : RelationIdeal A k),
    (∀ t, R t ↔ unionContents I t) → (C k R ↔ D k I)

theorem satisfaction_transport (C : PredicateDomain A) (D : IdealDomain A)
    (hd : DomainsRelated C D) (p : Formula n Γ) (v : Fin n → A)
    (ρ : PredicateEnv A Γ) (σ : IdealEnv A Γ) (h : EnvsRelated ρ σ) :
    PredicateSat C p v ρ ↔ IdealSat D p v σ := by
  induction p with
  | equal i j => exact Iff.rfl
  | apply r args => exact h r (fun i => v (args i))
  | relationEqual r s => exact related_relation_eq h r s
  | neg p ih => exact not_congr (ih v ρ σ h)
  | conj p q ihp ihq => exact and_congr (ihp v ρ σ h) (ihq v ρ σ h)
  | existsIndividual p ih =>
    exact exists_congr (fun a => ih (extendIndividual a v) ρ σ h)
  | @existsRelation n Γ k p ih =>
    constructor
    · rintro ⟨R, hR, hp⟩
      have hi : ∀ t, R t ↔ unionContents (partsOf R) t := fun t => (union_partsOf R t).symm
      exact ⟨partsOf R, (hd k R (partsOf R) hi).mp hR,
        (ih v _ _ (related_extend h hi)).mp hp⟩
    · rintro ⟨I, hI, hp⟩
      have hi : ∀ t, unionContents I t ↔ unionContents I t := fun _ => Iff.rfl
      exact ⟨unionContents I, (hd k (unionContents I) I hi).mpr hI,
        (ih v _ _ (related_extend h hi)).mpr hp⟩

def fullPredicates (A : Type u) : PredicateDomain A := fun _ _ => True

def fullIdeals (A : Type u) : IdealDomain A := fun _ _ => True

theorem full_domains_related : DomainsRelated (fullPredicates A) (fullIdeals A) :=
  fun _ _ _ _ => Iff.rfl

def FullPredicateSat (p : Formula n Γ) (v : Fin n → A) (ρ : PredicateEnv A Γ) : Prop :=
  PredicateSat (fullPredicates A) p v ρ

def FullIdealSat (p : Formula n Γ) (v : Fin n → A) (σ : IdealEnv A Γ) : Prop :=
  IdealSat (fullIdeals A) p v σ

theorem full_satisfaction_transport (p : Formula n Γ) (v : Fin n → A)
    (ρ : PredicateEnv A Γ) (σ : IdealEnv A Γ) (h : EnvsRelated ρ σ) :
    FullPredicateSat p v ρ ↔ FullIdealSat p v σ :=
  satisfaction_transport _ _ full_domains_related p v ρ σ h

theorem full_encode_truth (p : Formula n Γ) (v : Fin n → A) (ρ : PredicateEnv A Γ) :
    FullPredicateSat p v ρ ↔ FullIdealSat p v (encodeEnv ρ) :=
  full_satisfaction_transport p v ρ (encodeEnv ρ) (related_encode ρ)

theorem full_decode_truth (p : Formula n Γ) (v : Fin n → A) (σ : IdealEnv A Γ) :
    FullPredicateSat p v (decodeEnv σ) ↔ FullIdealSat p v σ :=
  full_satisfaction_transport p v (decodeEnv σ) σ (related_decode σ)

def representedIdeals (C : PredicateDomain A) : IdealDomain A :=
  fun k I => C k (unionContents I)

theorem represented_domains_related (C : PredicateDomain A) :
    DomainsRelated C (representedIdeals C) := by
  intro k R I hi
  have he : R = unionContents I := funext (fun t => propext (hi t))
  change C k R ↔ C k (unionContents I)
  rw [he]

theorem selected_encode_truth (C : PredicateDomain A) (p : Formula n Γ)
    (v : Fin n → A) (ρ : PredicateEnv A Γ) :
    PredicateSat C p v ρ ↔ IdealSat (representedIdeals C) p v (encodeEnv ρ) :=
  satisfaction_transport C _ (represented_domains_related C) p v ρ _ (related_encode ρ)

def AllPredicates (C : PredicateDomain A) : Prop := ∀ k R, C k R

def AllIdeals (D : IdealDomain A) : Prop := ∀ k I, D k I

theorem corresponding_fullness (C : PredicateDomain A) (D : IdealDomain A)
    (hd : DomainsRelated C D) : AllPredicates C ↔ AllIdeals D := by
  constructor
  · intro hc k I
    exact (hd k (unionContents I) I (fun _ => Iff.rfl)).mp (hc k _)
  · intro hi k R
    exact (hd k R (partsOf R) (fun t => (union_partsOf R t).symm)).mpr (hi k _)

def Formula.allIndividual (p : Formula (n+1) Γ) : Formula n Γ :=
  .neg (.existsIndividual (.neg p))

def Formula.allRelation (p : Formula n (k :: Γ)) : Formula n Γ :=
  .neg (.existsRelation (.neg p))

theorem predicate_allIndividual (C : PredicateDomain A) (p : Formula (n+1) Γ)
    (v : Fin n → A) (ρ : PredicateEnv A Γ) :
    PredicateSat C p.allIndividual v ρ ↔ ∀ a, PredicateSat C p (extendIndividual a v) ρ := by
  classical
  change (¬ ∃ a, ¬ PredicateSat C p (extendIndividual a v) ρ) ↔ _
  constructor
  · intro h a
    exact Classical.byContradiction (fun ha => h ⟨a, ha⟩)
  · rintro h ⟨a, ha⟩
    exact ha (h a)

theorem ideal_allIndividual (D : IdealDomain A) (p : Formula (n+1) Γ)
    (v : Fin n → A) (σ : IdealEnv A Γ) :
    IdealSat D p.allIndividual v σ ↔ ∀ a, IdealSat D p (extendIndividual a v) σ := by
  classical
  change (¬ ∃ a, ¬ IdealSat D p (extendIndividual a v) σ) ↔ _
  constructor
  · intro h a
    exact Classical.byContradiction (fun ha => h ⟨a, ha⟩)
  · rintro h ⟨a, ha⟩
    exact ha (h a)

theorem predicate_allRelation (C : PredicateDomain A) (p : Formula n (k :: Γ))
    (v : Fin n → A) (ρ : PredicateEnv A Γ) :
    PredicateSat C p.allRelation v ρ ↔
      ∀ R, C k R → PredicateSat C p v (extendPredicate R ρ) := by
  classical
  change (¬ ∃ R, C k R ∧ ¬ PredicateSat C p v (extendPredicate R ρ)) ↔ _
  constructor
  · intro h R hR
    exact Classical.byContradiction (fun hp => h ⟨R, hR, hp⟩)
  · rintro h ⟨R, hR, hp⟩
    exact hp (h R hR)

theorem ideal_allRelation (D : IdealDomain A) (p : Formula n (k :: Γ))
    (v : Fin n → A) (σ : IdealEnv A Γ) :
    IdealSat D p.allRelation v σ ↔ ∀ I, D k I → IdealSat D p v (extendIdeal I σ) := by
  classical
  change (¬ ∃ I, D k I ∧ ¬ IdealSat D p v (extendIdeal I σ)) ↔ _
  constructor
  · intro h I hI
    exact Classical.byContradiction (fun hp => h ⟨I, hI, hp⟩)
  · rintro h ⟨I, hI, hp⟩
    exact hp (h I hI)

theorem full_relation_exists (p : Formula n (k :: Γ)) (v : Fin n → A)
    (ρ : PredicateEnv A Γ) :
    FullPredicateSat (.existsRelation p) v ρ ↔ ∃ R, FullPredicateSat p v (extendPredicate R ρ) := by
  change (∃ R, True ∧ PredicateSat _ p v _) ↔ _
  exact ⟨fun ⟨R, _, h⟩ => ⟨R, h⟩, fun ⟨R, h⟩ => ⟨R, True.intro, h⟩⟩

theorem full_relation_forall (p : Formula n (k :: Γ)) (v : Fin n → A)
    (ρ : PredicateEnv A Γ) :
    FullPredicateSat p.allRelation v ρ ↔ ∀ R, FullPredicateSat p v (extendPredicate R ρ) := by
  change PredicateSat (fullPredicates A) p.allRelation v ρ ↔ _
  rw [predicate_allRelation]
  exact ⟨fun h R => h R True.intro, fun h R _ => h R⟩

def emptyIndividuals (A : Type u) : Fin 0 → A := fun i => Fin.elim0 i

def emptyPredicates (A : Type u) : PredicateEnv A [] := fun {_} r => nomatch r

def emptyIdeals (A : Type u) : IdealEnv A [] := fun {_} r => nomatch r

theorem full_sentence_reconstruction (p : Formula 0 []) :
    FullPredicateSat p (emptyIndividuals A) (emptyPredicates A) ↔
      FullIdealSat p (emptyIndividuals A) (emptyIdeals A) :=
  full_satisfaction_transport p _ _ _ (fun r => nomatch r)

/-- This selected range is not asserted to satisfy any comprehension principle. -/
def finitePredicates (A : Type u) : PredicateDomain A :=
  fun k R => ∃ F : FinitePart (Fin k → A), ∀ t, R t ↔ F.mem t

def totalUnarySentence : Formula 0 [] :=
  .existsRelation (Formula.allIndividual (.apply (RelVar.here (k := 1)) (fun _ => 0)))

theorem full_totalUnary (A : Type u) :
    FullPredicateSat totalUnarySentence (emptyIndividuals A) (emptyPredicates A) := by
  apply (full_relation_exists _ _ _).mpr
  refine ⟨fun _ => True, ?_⟩
  apply (predicate_allIndividual _ _ _ _).mpr
  exact fun _ => True.intro

def unaryBound : List (Fin 1 → Nat) → Nat
  | [] => 0
  | f :: fs => Nat.max (f 0) (unaryBound fs)

theorem unary_member_le (l : List (Fin 1 → Nat)) (f : Fin 1 → Nat) (h : f ∈ l) :
    f 0 ≤ unaryBound l := by
  induction l with
  | nil => simp at h
  | cons g l ih =>
    rcases List.mem_cons.mp h with rfl | h
    · exact Nat.le_max_left _ _
    · exact Nat.le_trans (ih h) (Nat.le_max_right _ _)

theorem finite_rejects_totalUnary :
    ¬ PredicateSat (finitePredicates Nat) totalUnarySentence
      (emptyIndividuals Nat) (emptyPredicates Nat) := by
  rintro ⟨R, ⟨F, hF⟩, hall⟩
  obtain ⟨l, hl⟩ := F.finite
  have hx := (predicate_allIndividual _ _ _ _).mp hall (unaryBound l + 1)
  change R (fun _ => unaryBound l + 1) at hx
  have hm := (hl (fun _ => unaryBound l + 1)).mp ((hF _).mp hx)
  have hb := unary_member_le l (fun _ => unaryBound l + 1) hm
  change unaryBound l + 1 ≤ unaryBound l at hb
  omega

theorem finite_not_full : ¬ AllPredicates (finitePredicates Nat) := by
  intro h
  obtain ⟨F, hF⟩ := h 1 (fun _ => True)
  obtain ⟨l, hl⟩ := F.finite
  have hm := (hl (fun _ => unaryBound l + 1)).mp ((hF _).mp True.intro)
  have hb := unary_member_le l (fun _ => unaryBound l + 1) hm
  change unaryBound l + 1 ≤ unaryBound l at hb
  omega

end SecondOrderReconstruction
