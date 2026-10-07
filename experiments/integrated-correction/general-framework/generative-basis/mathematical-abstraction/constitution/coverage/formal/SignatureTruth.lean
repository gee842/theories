import FunctionGraphs

/-!
Arbitrary named typed signatures, arbitrary theories and semantic consequence
in the declared finite simple-type language. Base carriers and full semantic
domains remain supplied. No universal metaphysical admission is inferred.
-/
namespace SignatureTruth
open CompletionExamples TypedTruth FunctionGraphReconstruction
universe u v w

abbrev Interpretation (S : Ty → Type w) (E : Ty → Type u) := ∀ t, S t → E t

noncomputable def transportInterpretation (e : BiMap A B)
    (M : Interpretation S (Direct A)) : Interpretation S (GraphCompleted B) :=
  fun t c => (graphTypeMap e t).forward (M t c)

def Compatible (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) : Prop :=
  ∀ t c, N t c = (graphTypeMap e t).forward (M t c)

theorem transported_compatible (e : BiMap A B) (M : Interpretation S (Direct A)) :
    Compatible e M (transportInterpretation e M) := fun _ _ => rfl

noncomputable def backInterpretation (e : BiMap A B)
    (N : Interpretation S (GraphCompleted B)) : Interpretation S (Direct A) :=
  fun t c => (graphTypeMap e t).backward (N t c)

theorem backward_compatible (e : BiMap A B) (N : Interpretation S (GraphCompleted B)) :
    Compatible e (backInterpretation e N) N :=
  fun t c => ((graphTypeMap e t).forward_backward (N t c)).symm

inductive Term (S : Ty → Type w) : List Ty → Ty → Type w where
  | var : Var Γ t → Term S Γ t
  | symbol : S t → Term S Γ t
  | app : Term S Γ (.arr s t) → Term S Γ s → Term S Γ t
  | lam : Term S (s :: Γ) t → Term S Γ (.arr s t)

def directEval (M : Interpretation S (Direct A)) (ρ : Env (Direct A) Γ) :
    Term S Γ t → Direct A t
  | .var i => ρ _ i
  | .symbol c => M _ c
  | .app f x => directEval M ρ f (directEval M ρ x)
  | .lam body => fun a => directEval M (extend ρ a) body

noncomputable def completedEval (N : Interpretation S (GraphCompleted B))
    (ρ : Env (GraphCompleted B) Γ) : Term S Γ t → GraphCompleted B t
  | .var i => ρ _ i
  | .symbol c => N _ c
  | .app f x => decodeFunction (completedEval N ρ f) (completedEval N ρ x)
  | .lam body => encodeFunction (fun a => completedEval N (extend ρ a) body)

theorem term_transport (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) (hc : Compatible e M N)
    (t : Term S Γ s) (ρ : Env (Direct A) Γ) :
    completedEval N (graphEnv e ρ) t = (graphTypeMap e s).forward (directEval M ρ t) := by
  induction t with
  | var i => rfl
  | symbol c => exact hc _ c
  | @app Γ s t f x ihf ihx =>
    change decodeFunction (completedEval N (graphEnv e ρ) f)
      (completedEval N (graphEnv e ρ) x) = _
    rw [ihf, ihx]
    change decodeFunction (encodeFunction (fun b => (graphTypeMap e t).forward
      (directEval M ρ f ((graphTypeMap e s).backward b))))
      ((graphTypeMap e s).forward (directEval M ρ x)) = _
    rw [decode_encode, (graphTypeMap e s).backward_forward]
    rfl
  | @lam s Γ t body ih =>
    change encodeFunction (fun b => completedEval N (extend (graphEnv e ρ) b) body) =
      encodeFunction (fun b => (graphTypeMap e t).forward
        (directEval M (extend ρ ((graphTypeMap e s).backward b)) body))
    apply congrArg encodeFunction
    funext b
    have h := ih (extend ρ ((graphTypeMap e s).backward b))
    rw [graphEnv_extend, (graphTypeMap e s).forward_backward] at h
    exact h

inductive Formula (S : Ty → Type w) : List Ty → Type w where
  | equal : Term S Γ t → Term S Γ t → Formula S Γ
  | member : Term S Γ (.pred t) → Term S Γ t → Formula S Γ
  | neg : Formula S Γ → Formula S Γ
  | conj : Formula S Γ → Formula S Γ → Formula S Γ
  | ex : (t : Ty) → Formula S (t :: Γ) → Formula S Γ

def DirectHolds (M : Interpretation S (Direct A)) (ρ : Env (Direct A) Γ) :
    Formula S Γ → Prop
  | .equal x y => directEval M ρ x = directEval M ρ y
  | .member P x => directEval M ρ P (directEval M ρ x)
  | .neg p => ¬ DirectHolds M ρ p
  | .conj p q => DirectHolds M ρ p ∧ DirectHolds M ρ q
  | .ex t p => ∃ a : Direct A t, DirectHolds M (extend ρ a) p

def CompletedHolds (N : Interpretation S (GraphCompleted B))
    (ρ : Env (GraphCompleted B) Γ) : Formula S Γ → Prop
  | .equal x y => completedEval N ρ x = completedEval N ρ y
  | .member P x => unionContents (completedEval N ρ P) (completedEval N ρ x)
  | .neg p => ¬ CompletedHolds N ρ p
  | .conj p q => CompletedHolds N ρ p ∧ CompletedHolds N ρ q
  | .ex t p => ∃ b : GraphCompleted B t, CompletedHolds N (extend ρ b) p

theorem formula_transport (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) (hc : Compatible e M N)
    (p : Formula S Γ) (ρ : Env (Direct A) Γ) :
    CompletedHolds N (graphEnv e ρ) p ↔ DirectHolds M ρ p := by
  induction p with
  | @equal Γ t x y =>
    change completedEval N (graphEnv e ρ) x = completedEval N (graphEnv e ρ) y ↔ _
    rw [term_transport e M N hc, term_transport e M N hc]
    exact ⟨forward_injective (graphTypeMap e t), congrArg (graphTypeMap e t).forward⟩
  | @member Γ t P x =>
    change unionContents (completedEval N (graphEnv e ρ) P)
      (completedEval N (graphEnv e ρ) x) ↔ _
    rw [term_transport e M N hc, term_transport e M N hc]
    exact predicateMap_membership (graphTypeMap e t) (directEval M ρ P) (directEval M ρ x)
  | neg p ih => exact not_congr (ih ρ)
  | conj p q ihp ihq => exact and_congr (ihp ρ) (ihq ρ)
  | @ex Γ t p ih =>
    constructor
    · rintro ⟨b, hb⟩
      refine ⟨(graphTypeMap e t).backward b, ?_⟩
      have h := ih (extend ρ ((graphTypeMap e t).backward b))
      rw [graphEnv_extend, (graphTypeMap e t).forward_backward] at h
      exact h.mp hb
    · rintro ⟨a, ha⟩
      refine ⟨(graphTypeMap e t).forward a, ?_⟩
      have h := ih (extend ρ a)
      rw [graphEnv_extend] at h
      exact h.mpr ha

theorem sentence_transport (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) (hc : Compatible e M N)
    (p : Formula S []) :
    CompletedHolds N (emptyEnv (GraphCompleted B)) p ↔
      DirectHolds M (emptyEnv (Direct A)) p := by
  simpa [graph_empty_env] using formula_transport e M N hc p (emptyEnv (Direct A))

theorem formula_comprehension (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) (hc : Compatible e M N)
    (s : Ty) (p : Formula S (s :: Γ)) (ρ : Env (Direct A) Γ) :
    ∃ I : GraphCompleted B (.pred s), ∀ b : GraphCompleted B s,
      unionContents I b ↔ CompletedHolds N (extend (graphEnv e ρ) b) p := by
  refine ⟨(graphTypeMap e (.pred s)).forward (fun a => DirectHolds M (extend ρ a) p), ?_⟩
  intro b
  obtain ⟨a, rfl⟩ := forward_surjective (graphTypeMap e s) b
  have h := formula_transport e M N hc p (extend ρ a)
  rw [graphEnv_extend] at h
  exact (predicateMap_membership (graphTypeMap e s)
    (fun x => DirectHolds M (extend ρ x) p) a).trans h.symm

abbrev Theory (S : Ty → Type w) := Formula S [] → Prop

def DirectModels (M : Interpretation S (Direct A)) (T : Theory S) : Prop :=
  ∀ p, T p → DirectHolds M (emptyEnv (Direct A)) p

def CompletedModels (N : Interpretation S (GraphCompleted B)) (T : Theory S) : Prop :=
  ∀ p, T p → CompletedHolds N (emptyEnv (GraphCompleted B)) p

theorem theory_transport (e : BiMap A B) (M : Interpretation S (Direct A))
    (N : Interpretation S (GraphCompleted B)) (hc : Compatible e M N) (T : Theory S) :
    CompletedModels N T ↔ DirectModels M T := by
  constructor
  · intro h p hp
    exact (sentence_transport e M N hc p).mp (h p hp)
  · intro h p hp
    exact (sentence_transport e M N hc p).mpr (h p hp)

def DirectEntails (S : Ty → Type w) (T : Theory S) (p : Formula S []) : Prop :=
  ∀ (A : Type u) (M : Interpretation S (Direct A)),
    DirectModels M T → DirectHolds M (emptyEnv (Direct A)) p

def CompletedEntails (S : Ty → Type w) (T : Theory S) (p : Formula S []) : Prop :=
  ∀ (B : Type u) (N : Interpretation S (GraphCompleted B)),
    CompletedModels N T → CompletedHolds N (emptyEnv (GraphCompleted B)) p

theorem entailment_transport (S : Ty → Type w) (T : Theory S) (p : Formula S []) :
    CompletedEntails.{u,w} S T p ↔ DirectEntails.{u,w} S T p := by
  constructor
  · intro h A M hm
    let e := identity A
    let N := transportInterpretation e M
    have hc : Compatible e M N := transported_compatible e M
    exact (sentence_transport e M N hc p).mp
      (h A N ((theory_transport e M N hc T).mpr hm))
  · intro h B N hn
    let e := identity B
    let M := backInterpretation e N
    have hc : Compatible e M N := backward_compatible e N
    exact (sentence_transport e M N hc p).mpr
      (h B M ((theory_transport e M N hc T).mp hn))

def DirectSatisfiable (S : Ty → Type w) (T : Theory S) : Prop :=
  ∃ (A : Type u) (M : Interpretation S (Direct A)), DirectModels M T

def CompletedSatisfiable (S : Ty → Type w) (T : Theory S) : Prop :=
  ∃ (B : Type u) (N : Interpretation S (GraphCompleted B)), CompletedModels N T

theorem satisfiability_transport (S : Ty → Type w) (T : Theory S) :
    CompletedSatisfiable.{u,w} S T ↔ DirectSatisfiable.{u,w} S T := by
  constructor
  · rintro ⟨B, N, hn⟩
    exact ⟨B, backInterpretation (identity B) N,
      (theory_transport (identity B) _ N (backward_compatible _ N) T).mp hn⟩
  · rintro ⟨A, M, hm⟩
    exact ⟨A, transportInterpretation (identity A) M,
      (theory_transport (identity A) M _ (transported_compatible _ M) T).mpr hm⟩

def Formula.all (t : Ty) (p : Formula S (t :: Γ)) : Formula S Γ := .neg (.ex t (.neg p))

theorem direct_all (M : Interpretation S (Direct A)) (ρ : Env (Direct A) Γ)
    (t : Ty) (p : Formula S (t :: Γ)) :
    DirectHolds M ρ (.all t p) ↔ ∀ a : Direct A t, DirectHolds M (extend ρ a) p := by
  classical
  simp [Formula.all, DirectHolds]

inductive NatSymbols : Ty → Type where
  | zero : NatSymbols .base
  | add : NatSymbols (.arr .base (.arr .base .base))

def natInterpretation : Interpretation NatSymbols (Direct Nat)
  | _, .zero => (0 : Nat)
  | _, .add => Nat.add

def addTerm (x y : Term NatSymbols Γ .base) : Term NatSymbols Γ .base :=
  .app (.app (.symbol .add) x) y

def addAssocSentence : Formula NatSymbols [] :=
  .all .base (.all .base (.all .base (.equal
    (addTerm (addTerm (.var (.there (.there .here))) (.var (.there .here))) (.var .here))
    (addTerm (.var (.there (.there .here))) (addTerm (.var (.there .here)) (.var .here))))))

theorem nat_add_assoc_direct :
    DirectHolds natInterpretation (emptyEnv (Direct Nat)) addAssocSentence := by
  apply (direct_all _ _ _ _).mpr
  intro x
  apply (direct_all _ _ _ _).mpr
  intro y
  apply (direct_all _ _ _ _).mpr
  intro z
  change Nat.add (Nat.add x y) z = Nat.add x (Nat.add y z)
  exact Nat.add_assoc x y z

theorem nat_add_assoc_completed :
    CompletedHolds (transportInterpretation (identity Nat) natInterpretation)
      (emptyEnv (GraphCompleted Nat)) addAssocSentence :=
  (sentence_transport (identity Nat) natInterpretation _
    (transported_compatible _ _) addAssocSentence).mpr nat_add_assoc_direct

inductive PairSymbols : Ty → Type where
  | first : PairSymbols .base
  | second : PairSymbols .base

def sameInterpretation : Interpretation PairSymbols (Direct Bool)
  | _, .first => false
  | _, .second => false

def splitInterpretation : Interpretation PairSymbols (GraphCompleted Bool)
  | _, .first => false
  | _, .second => true

def pairEquality : Formula PairSymbols [] := .equal (.symbol .first) (.symbol .second)

theorem mismatched_symbols_change_truth :
    DirectHolds sameInterpretation (emptyEnv (Direct Bool)) pairEquality ∧
      ¬ CompletedHolds splitInterpretation (emptyEnv (GraphCompleted Bool)) pairEquality := by
  constructor
  · rfl
  · change ¬ ((false : Bool) = true)
    exact Bool.false_ne_true

end SignatureTruth
