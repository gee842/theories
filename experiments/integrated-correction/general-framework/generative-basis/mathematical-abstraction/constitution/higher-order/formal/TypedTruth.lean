import CompletionExamples

/-!
Finite simple types with full arrows and full predicate completion.
Direct predicates are interpreted by full functions into Prop; completed
predicates are ideals of finite subsets of the recursively interpreted carrier.
The supplied base bijection transports atomic identity, not formula truth.
No dependent types, internal universe, or unrestricted internal truth predicate
are represented. Full external function/predicate spaces remain explicit.
-/
namespace TypedTruth
open CompletionWarrant CompletionExamples
universe u v w

structure BiMap (A : Type u) (B : Type v) where
  forward : A → B
  backward : B → A
  backward_forward : ∀ a, backward (forward a) = a
  forward_backward : ∀ b, forward (backward b) = b

theorem forward_injective (e : BiMap A B) {a b : A}
    (h : e.forward a = e.forward b) : a = b := by
  have := congrArg e.backward h
  simpa [e.backward_forward] using this

theorem forward_surjective (e : BiMap A B) (b : B) : ∃ a, e.forward a = b :=
  ⟨e.backward b, e.forward_backward b⟩

def identity (A : Type u) : BiMap A A where
  forward := id
  backward := id
  backward_forward _ := rfl
  forward_backward _ := rfl

def arrowMap (e : BiMap A B) (f : BiMap C D) : BiMap (A → C) (B → D) where
  forward g := fun b => f.forward (g (e.backward b))
  backward h := fun a => f.backward (h (e.forward a))
  backward_forward g := by
    funext a
    simp [e.backward_forward, f.backward_forward]
  forward_backward h := by
    funext b
    simp [e.forward_backward, f.forward_backward]

def predicateMap (e : BiMap A B) : BiMap (A → Prop) (Ideal (finiteOrder B)) where
  forward P := partsOf (fun b => P (e.backward b))
  backward I := fun a => unionContents I (e.forward a)
  backward_forward P := by
    funext a
    apply propext
    simpa [e.backward_forward] using
      (union_partsOf (fun b => P (e.backward b)) (e.forward a))
  forward_backward I := by
    have h : (fun b => unionContents I (e.forward (e.backward b))) = unionContents I := by
      funext b
      rw [e.forward_backward]
    change partsOf (fun b => unionContents I (e.forward (e.backward b))) = I
    rw [h]
    exact partsOf_union I

theorem predicateMap_membership (e : BiMap A B) (P : A → Prop) (a : A) :
    unionContents ((predicateMap e).forward P) (e.forward a) ↔ P a := by
  simpa [predicateMap, e.backward_forward] using
    (union_partsOf (fun b => P (e.backward b)) (e.forward a))

inductive Ty where
  | base
  | arr : Ty → Ty → Ty
  | pred : Ty → Ty

def Direct (A : Type u) : Ty → Type u
  | .base => A
  | .arr s t => Direct A s → Direct A t
  | .pred s => Direct A s → Prop

def Completed (B : Type v) : Ty → Type v
  | .base => B
  | .arr s t => Completed B s → Completed B t
  | .pred s => Ideal (finiteOrder (Completed B s))

def typeMap (e : BiMap A B) : (t : Ty) → BiMap (Direct A t) (Completed B t)
  | .base => e
  | .arr s t => arrowMap (typeMap e s) (typeMap e t)
  | .pred s => predicateMap (typeMap e s)

theorem type_forward_backward (e : BiMap A B) (t : Ty) (b : Completed B t) :
    (typeMap e t).forward ((typeMap e t).backward b) = b :=
  (typeMap e t).forward_backward b

theorem type_backward_forward (e : BiMap A B) (t : Ty) (a : Direct A t) :
    (typeMap e t).backward ((typeMap e t).forward a) = a :=
  (typeMap e t).backward_forward a

theorem type_membership (e : BiMap A B) (s : Ty) (P : Direct A (.pred s))
    (a : Direct A s) :
    unionContents ((typeMap e (.pred s)).forward P) ((typeMap e s).forward a) ↔ P a :=
  predicateMap_membership (typeMap e s) P a

inductive Var : List Ty → Ty → Type where
  | here : Var (t :: Γ) t
  | there : Var Γ t → Var (s :: Γ) t

def Env (E : Ty → Type u) (Γ : List Ty) := ∀ t, Var Γ t → E t

def extend (ρ : Env E Γ) (a : E s) : Env E (s :: Γ)
  | _, .here => a
  | _, .there i => ρ _ i

def mapEnv (e : BiMap A B) (ρ : Env (Direct A) Γ) : Env (Completed B) Γ :=
  fun t i => (typeMap e t).forward (ρ t i)

theorem mapEnv_extend (e : BiMap A B) (ρ : Env (Direct A) Γ) (a : Direct A s) :
    mapEnv e (extend ρ a) = extend (mapEnv e ρ) ((typeMap e s).forward a) := by
  funext t i
  cases i <;> rfl

inductive Term : List Ty → Ty → Type where
  | var : Var Γ t → Term Γ t
  | app : Term Γ (.arr s t) → Term Γ s → Term Γ t
  | lam : Term (s :: Γ) t → Term Γ (.arr s t)

def directEval (ρ : Env (Direct A) Γ) : Term Γ t → Direct A t
  | .var i => ρ _ i
  | .app f x => directEval ρ f (directEval ρ x)
  | .lam body => fun a => directEval (extend ρ a) body

def completedEval (ρ : Env (Completed B) Γ) : Term Γ t → Completed B t
  | .var i => ρ _ i
  | .app f x => completedEval ρ f (completedEval ρ x)
  | .lam body => fun a => completedEval (extend ρ a) body

theorem term_transport (e : BiMap A B) (t : Term Γ s) (ρ : Env (Direct A) Γ) :
    completedEval (mapEnv e ρ) t = (typeMap e s).forward (directEval ρ t) := by
  induction t with
  | var i => rfl
  | @app Γ s t f x ihf ihx =>
    change completedEval (mapEnv e ρ) f (completedEval (mapEnv e ρ) x) = _
    rw [ihf, ihx]
    change (typeMap e t).forward
      (directEval ρ f ((typeMap e s).backward ((typeMap e s).forward (directEval ρ x)))) = _
    rw [type_backward_forward]
    rfl
  | @lam s Γ t body ih =>
    funext b
    change completedEval (extend (mapEnv e ρ) b) body =
      (typeMap e t).forward (directEval (extend ρ ((typeMap e s).backward b)) body)
    have h := ih (extend ρ ((typeMap e s).backward b))
    rw [mapEnv_extend, type_forward_backward] at h
    exact h

inductive Formula : List Ty → Type where
  | equal : Term Γ t → Term Γ t → Formula Γ
  | member : Term Γ (.pred t) → Term Γ t → Formula Γ
  | neg : Formula Γ → Formula Γ
  | conj : Formula Γ → Formula Γ → Formula Γ
  | ex : (t : Ty) → Formula (t :: Γ) → Formula Γ

def DirectHolds (ρ : Env (Direct A) Γ) : Formula Γ → Prop
  | .equal t s => directEval ρ t = directEval ρ s
  | .member P t => directEval ρ P (directEval ρ t)
  | .neg p => ¬ DirectHolds ρ p
  | .conj p q => DirectHolds ρ p ∧ DirectHolds ρ q
  | .ex t p => ∃ a : Direct A t, DirectHolds (extend ρ a) p

def CompletedHolds (ρ : Env (Completed B) Γ) : Formula Γ → Prop
  | .equal t s => completedEval ρ t = completedEval ρ s
  | .member P t => unionContents (completedEval ρ P) (completedEval ρ t)
  | .neg p => ¬ CompletedHolds ρ p
  | .conj p q => CompletedHolds ρ p ∧ CompletedHolds ρ q
  | .ex t p => ∃ a : Completed B t, CompletedHolds (extend ρ a) p

theorem formula_transport (e : BiMap A B) (p : Formula Γ) (ρ : Env (Direct A) Γ) :
    CompletedHolds (mapEnv e ρ) p ↔ DirectHolds ρ p := by
  induction p with
  | @equal Γ t x y =>
    change completedEval (mapEnv e ρ) x = completedEval (mapEnv e ρ) y ↔ _
    rw [term_transport, term_transport]
    exact ⟨forward_injective (typeMap e t), congrArg (typeMap e t).forward⟩
  | @member Γ t P x =>
    change unionContents (completedEval (mapEnv e ρ) P)
      (completedEval (mapEnv e ρ) x) ↔ _
    rw [term_transport, term_transport]
    exact type_membership e t (directEval ρ P) (directEval ρ x)
  | neg p ih => exact not_congr (ih ρ)
  | conj p q ihp ihq => exact and_congr (ihp ρ) (ihq ρ)
  | @ex Γ t p ih =>
    constructor
    · rintro ⟨b, hb⟩
      refine ⟨(typeMap e t).backward b, ?_⟩
      have h := ih (extend ρ ((typeMap e t).backward b))
      rw [mapEnv_extend, type_forward_backward] at h
      exact h.mp hb
    · rintro ⟨a, ha⟩
      refine ⟨(typeMap e t).forward a, ?_⟩
      have h := ih (extend ρ a)
      rw [mapEnv_extend] at h
      exact h.mpr ha

def emptyEnv (E : Ty → Type u) : Env E [] := fun _ i => nomatch i

theorem emptyEnv_map (e : BiMap A B) :
    mapEnv e (emptyEnv (Direct A)) = emptyEnv (Completed B) := by
  funext t i
  nomatch i

theorem sentence_transport (e : BiMap A B) (p : Formula []) :
    CompletedHolds (emptyEnv (Completed B)) p ↔ DirectHolds (emptyEnv (Direct A)) p := by
  simpa [emptyEnv_map] using formula_transport e p (emptyEnv (Direct A))

theorem full_predicate_completion (A : Type u) (s : Ty)
    (P : Direct A (.pred s)) (a : Direct A s) :
    unionContents ((typeMap (identity A) (.pred s)).forward P)
      ((typeMap (identity A) s).forward a) ↔ P a :=
  type_membership (identity A) s P a

/-- Every formula extension, including formulas quantifying over higher types,
has an ideal presentation. This uses the supplied full predicate interpretation;
it is not a construction from finite evidence or an effective decision rule. -/
theorem formula_comprehension (e : BiMap A B) (s : Ty)
    (p : Formula (s :: Γ)) (ρ : Env (Direct A) Γ) :
    ∃ I : Completed B (.pred s), ∀ b : Completed B s,
      unionContents I b ↔ CompletedHolds (extend (mapEnv e ρ) b) p := by
  refine ⟨(typeMap e (.pred s)).forward (fun a => DirectHolds (extend ρ a) p), ?_⟩
  intro b
  obtain ⟨a, rfl⟩ := forward_surjective (typeMap e s) b
  have h := formula_transport e p (extend ρ a)
  rw [mapEnv_extend] at h
  exact (type_membership e s (fun x => DirectHolds (extend ρ x) p) a).trans h.symm

def Formula.all (t : Ty) (p : Formula (t :: Γ)) : Formula Γ := .neg (.ex t (.neg p))

theorem direct_all (ρ : Env (Direct A) Γ) (t : Ty) (p : Formula (t :: Γ)) :
    DirectHolds ρ (.all t p) ↔ ∀ a : Direct A t, DirectHolds (extend ρ a) p := by
  classical
  simp [Formula.all, DirectHolds]

theorem completed_all (ρ : Env (Completed B) Γ) (t : Ty) (p : Formula (t :: Γ)) :
    CompletedHolds ρ (.all t p) ↔ ∀ a : Completed B t, CompletedHolds (extend ρ a) p := by
  classical
  simp [Formula.all, CompletedHolds]

/-- A closed formula exercises higher-type quantification, lambda binding and
application. Substituting predicate types gives the mixed higher-type case. -/
def etaSentence (s t : Ty) : Formula [] :=
  .all (.arr s t)
    (.equal (.lam (.app (.var (.there .here)) (.var .here))) (.var .here))

theorem eta_direct (A : Type u) (s t : Ty) :
    DirectHolds (emptyEnv (Direct A)) (etaSentence s t) := by
  apply (direct_all _ _ _).mpr
  intro f
  change (fun a => f a) = f
  rfl

theorem eta_completed (A : Type u) (s t : Ty) :
    CompletedHolds (emptyEnv (Completed A)) (etaSentence s t) :=
  (sentence_transport (identity A) (etaSentence s t)).mpr (eta_direct A s t)

def higherEtaSentence : Formula [] := etaSentence (.pred .base) (.pred (.pred .base))

theorem higher_eta_completed (A : Type u) :
    CompletedHolds (emptyEnv (Completed A)) higherEtaSentence :=
  eta_completed A (.pred .base) (.pred (.pred .base))

end TypedTruth
