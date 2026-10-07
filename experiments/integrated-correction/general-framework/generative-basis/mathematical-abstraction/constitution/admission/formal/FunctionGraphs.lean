import TypedTruth
import Admission

/-!
Full functions represented by total functional ideals of finite relation graphs.
All relation ideals and the global totality condition are explicit resources.
The construction is semantic, not a finite procedure for finding every function.
-/
namespace FunctionGraphReconstruction
open CompletionWarrant CompletionExamples TypedTruth
universe u v w

def GraphIdeal (A : Type u) (B : Type v) := Ideal (finiteOrder (A × B))

def Functional (I : GraphIdeal A B) : Prop :=
  ∀ x y z, unionContents I (x, y) → unionContents I (x, z) → y = z

def Total (I : GraphIdeal A B) : Prop := ∀ x, ∃ y, unionContents I (x, y)

def FiniteFunctional (F : FinitePart (A × B)) : Prop :=
  ∀ x y z, F.mem (x, y) → F.mem (x, z) → y = z

theorem functional_iff_finite (I : GraphIdeal A B) :
    Functional I ↔ ∀ F, I.mem F → FiniteFunctional F := by
  constructor
  · intro h F hF x y z hy hz
    exact h x y z ⟨F, hF, hy⟩ ⟨F, hF, hz⟩
  · intro h x y z hy hz
    obtain ⟨F, hF, hy⟩ := hy
    obtain ⟨G, hG, hz⟩ := hz
    obtain ⟨H, hH, hFH, hGH⟩ := I.directed hF hG
    exact h H hH x y z (hFH _ hy) (hGH _ hz)

theorem total_iff_finite_coverage (I : GraphIdeal A B) :
    Total I ↔ ∀ x, ∃ F, I.mem F ∧ ∃ y, F.mem (x, y) := by
  constructor
  · intro h x
    obtain ⟨y, F, hF, hy⟩ := h x
    exact ⟨F, hF, y, hy⟩
  · intro h x
    obtain ⟨F, hF, y, hy⟩ := h x
    exact ⟨y, F, hF, hy⟩

structure FunctionIdeal (A : Type u) (B : Type v) where
  ideal : GraphIdeal A B
  functional : Functional ideal
  total : Total ideal

theorem functionIdeal_ext {F G : FunctionIdeal A B} (h : F.ideal = G.ideal) : F = G := by
  cases F
  cases G
  cases h
  rfl

def graph (f : A → B) : A × B → Prop := fun p => f p.1 = p.2

def encodeFunction (f : A → B) : FunctionIdeal A B where
  ideal := partsOf (graph f)
  functional := by
    intro x y z hy hz
    have hy' := (union_partsOf (graph f) (x, y)).mp hy
    have hz' := (union_partsOf (graph f) (x, z)).mp hz
    exact hy'.symm.trans hz'
  total := fun x => ⟨f x, (union_partsOf (graph f) (x, f x)).mpr rfl⟩

noncomputable def decodeFunction (F : FunctionIdeal A B) (x : A) : B :=
  Classical.choose (F.total x)

theorem decode_mem (F : FunctionIdeal A B) (x : A) :
    unionContents F.ideal (x, decodeFunction F x) := Classical.choose_spec (F.total x)

theorem graph_decode (F : FunctionIdeal A B) (x : A) (y : B) :
    decodeFunction F x = y ↔ unionContents F.ideal (x, y) := by
  constructor
  · intro h
    rw [← h]
    exact decode_mem F x
  · intro h
    exact F.functional x _ y (decode_mem F x) h

theorem decode_encode (f : A → B) : decodeFunction (encodeFunction f) = f := by
  funext x
  exact ((union_partsOf (graph f) (x, decodeFunction (encodeFunction f) x)).mp
    (decode_mem (encodeFunction f) x)).symm

theorem encode_decode (F : FunctionIdeal A B) : encodeFunction (decodeFunction F) = F := by
  apply functionIdeal_ext
  have h : graph (decodeFunction F) = unionContents F.ideal := by
    funext p
    exact propext (graph_decode F p.1 p.2)
  change partsOf (graph (decodeFunction F)) = F.ideal
  rw [h, partsOf_union]

noncomputable def functionMap (A : Type u) (B : Type v) : BiMap (A → B) (FunctionIdeal A B) where
  forward := encodeFunction
  backward := decodeFunction
  backward_forward := decode_encode
  forward_backward := encode_decode

def emptyGraph (A : Type u) (B : Type v) : GraphIdeal A B := partsOf (fun _ => False)

theorem empty_functional (A : Type u) (B : Type v) : Functional (emptyGraph A B) := by
  intro x y z hy _
  exact False.elim ((union_partsOf (fun _ : A × B => False) (x, y)).mp hy)

theorem empty_not_total (x : A) : ¬ Total (emptyGraph A B) := by
  intro h
  obtain ⟨y, hy⟩ := h x
  exact (union_partsOf (fun _ : A × B => False) (x, y)).mp hy

theorem functions_admitted_by_completion (C : (A × B → Prop) → Prop)
    (hf : PredicateAdmission.IncludesFinite C)
    (hd : PredicateAdmission.DirectedUnionClosed C) (f : A → B) : C (graph f) :=
  PredicateAdmission.full_of_finite_directed C hf hd (graph f)

def trueFiber (f : A → Bool) : A → Prop := fun a => f a = true

noncomputable def characteristic (P : A → Prop) : A → Bool := by
  classical
  exact fun a => if P a then true else false

theorem characteristic_fiber (P : A → Prop) : trueFiber (characteristic P) = P := by
  classical
  funext a
  apply propext
  simp [trueFiber, characteristic]

/-- Full Boolean-valued function admission already carries every predicate via its fiber. -/
theorem full_boolean_functions_iff_predicates (C : (A → Prop) → Prop) :
    (∀ f : A → Bool, C (trueFiber f)) ↔ PredicateAdmission.Full C := by
  constructor
  · intro h P
    have hp := h (characteristic P)
    rwa [characteristic_fiber] at hp
  · exact fun h f => h (trueFiber f)

/-- The selected finite type language now represents arrows by graph ideals too. -/
def GraphCompleted (A : Type u) : Ty → Type u
  | .base => A
  | .arr s t => FunctionIdeal (GraphCompleted A s) (GraphCompleted A t)
  | .pred s => Ideal (finiteOrder (GraphCompleted A s))

def compose (e : BiMap A B) (f : BiMap B C) : BiMap A C where
  forward a := f.forward (e.forward a)
  backward c := e.backward (f.backward c)
  backward_forward a := by rw [f.backward_forward, e.backward_forward]
  forward_backward c := by rw [e.forward_backward, f.forward_backward]

noncomputable def graphTypeMap (e : BiMap A B) : (t : Ty) → BiMap (Direct A t) (GraphCompleted B t)
  | .base => e
  | .arr s t => compose (arrowMap (graphTypeMap e s) (graphTypeMap e t)) (functionMap _ _)
  | .pred s => predicateMap (graphTypeMap e s)

noncomputable def graphEnv (e : BiMap A B) (ρ : Env (Direct A) Γ) : Env (GraphCompleted B) Γ :=
  fun t i => (graphTypeMap e t).forward (ρ t i)

theorem graphEnv_extend (e : BiMap A B) (ρ : Env (Direct A) Γ) (a : Direct A s) :
    graphEnv e (extend ρ a) = extend (graphEnv e ρ) ((graphTypeMap e s).forward a) := by
  funext t i
  cases i <;> rfl

noncomputable def graphEval (ρ : Env (GraphCompleted A) Γ) : Term Γ t → GraphCompleted A t
  | .var i => ρ _ i
  | .app f x => decodeFunction (graphEval ρ f) (graphEval ρ x)
  | .lam body => encodeFunction (fun a => graphEval (extend ρ a) body)

theorem graph_term_transport (e : BiMap A B) (t : Term Γ s) (ρ : Env (Direct A) Γ) :
    graphEval (graphEnv e ρ) t = (graphTypeMap e s).forward (directEval ρ t) := by
  induction t with
  | var i => rfl
  | @app Γ s t f x ihf ihx =>
    change decodeFunction (graphEval (graphEnv e ρ) f) (graphEval (graphEnv e ρ) x) = _
    rw [ihf, ihx]
    change decodeFunction (encodeFunction
      (fun b => (graphTypeMap e t).forward (directEval ρ f ((graphTypeMap e s).backward b))))
      ((graphTypeMap e s).forward (directEval ρ x)) = _
    rw [decode_encode, (graphTypeMap e s).backward_forward]
    rfl
  | @lam s Γ t body ih =>
    change encodeFunction (fun b => graphEval (extend (graphEnv e ρ) b) body) =
      encodeFunction (fun b => (graphTypeMap e t).forward
        (directEval (extend ρ ((graphTypeMap e s).backward b)) body))
    apply congrArg encodeFunction
    funext b
    have h := ih (extend ρ ((graphTypeMap e s).backward b))
    rw [graphEnv_extend, (graphTypeMap e s).forward_backward] at h
    exact h

def GraphHolds (ρ : Env (GraphCompleted A) Γ) : Formula Γ → Prop
  | .equal t s => graphEval ρ t = graphEval ρ s
  | .member P t => unionContents (graphEval ρ P) (graphEval ρ t)
  | .neg p => ¬ GraphHolds ρ p
  | .conj p q => GraphHolds ρ p ∧ GraphHolds ρ q
  | .ex t p => ∃ a : GraphCompleted A t, GraphHolds (extend ρ a) p

theorem graph_formula_transport (e : BiMap A B) (p : Formula Γ) (ρ : Env (Direct A) Γ) :
    GraphHolds (graphEnv e ρ) p ↔ DirectHolds ρ p := by
  induction p with
  | @equal Γ t x y =>
    change graphEval (graphEnv e ρ) x = graphEval (graphEnv e ρ) y ↔ _
    rw [graph_term_transport, graph_term_transport]
    exact ⟨forward_injective (graphTypeMap e t), congrArg (graphTypeMap e t).forward⟩
  | @member Γ t P x =>
    change unionContents (graphEval (graphEnv e ρ) P) (graphEval (graphEnv e ρ) x) ↔ _
    rw [graph_term_transport, graph_term_transport]
    exact predicateMap_membership (graphTypeMap e t) (directEval ρ P) (directEval ρ x)
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

theorem graph_empty_env (e : BiMap A B) :
    graphEnv e (emptyEnv (Direct A)) = emptyEnv (GraphCompleted B) := by
  funext t i
  nomatch i

theorem graph_sentence_transport (e : BiMap A B) (p : Formula []) :
    GraphHolds (emptyEnv (GraphCompleted B)) p ↔ DirectHolds (emptyEnv (Direct A)) p := by
  simpa [graph_empty_env] using graph_formula_transport e p (emptyEnv (Direct A))

theorem higher_eta_graph (A : Type u) :
    GraphHolds (emptyEnv (GraphCompleted A)) higherEtaSentence :=
  (graph_sentence_transport (identity A) higherEtaSentence).mpr
    (eta_direct A (.pred .base) (.pred (.pred .base)))

end FunctionGraphReconstruction
