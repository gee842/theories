import FiniteAdmission

/-!
Sections of a supplied dependent family are represented by total functional
ideals of finite subsets of its dependent sum. The base, fibers, all ideals and
global totality remain explicit. Fiberwise equivalences preserve this base.
This is a semantic representation, not a dependent syntax or admission result
without the stated premises.
-/
namespace DependentCompletion
open CompletionWarrant CompletionExamples TypedTruth
universe u v w
variable {A : Type u} {B : A → Type v} {D : A → Type w}

def GraphIdeal (B : A → Type v) := Ideal (finiteOrder (Sigma B))

def Functional (I : GraphIdeal B) : Prop :=
  ∀ a (b c : B a), unionContents I ⟨a, b⟩ → unionContents I ⟨a, c⟩ → b = c

def Total (I : GraphIdeal B) : Prop := ∀ a, ∃ b : B a, unionContents I ⟨a, b⟩

def FiniteFunctional (F : FinitePart (Sigma B)) : Prop :=
  ∀ a (b c : B a), F.mem ⟨a, b⟩ → F.mem ⟨a, c⟩ → b = c

theorem functional_iff_finite (I : GraphIdeal B) :
    Functional I ↔ ∀ F, I.mem F → FiniteFunctional F := by
  constructor
  · intro h F hF a b c hb hc
    exact h a b c ⟨F, hF, hb⟩ ⟨F, hF, hc⟩
  · intro h a b c hb hc
    obtain ⟨F, hF, hb⟩ := hb
    obtain ⟨G, hG, hc⟩ := hc
    obtain ⟨H, hH, hFH, hGH⟩ := I.directed hF hG
    exact h H hH a b c (hFH _ hb) (hGH _ hc)

theorem total_iff_finite_coverage (I : GraphIdeal B) :
    Total I ↔ ∀ a, ∃ F, I.mem F ∧ ∃ b : B a, F.mem ⟨a, b⟩ := by
  constructor
  · intro h a
    obtain ⟨b, F, hF, hb⟩ := h a
    exact ⟨F, hF, b, hb⟩
  · intro h a
    obtain ⟨F, hF, b, hb⟩ := h a
    exact ⟨b, F, hF, hb⟩

structure SectionIdeal (B : A → Type v) where
  ideal : GraphIdeal B
  functional : Functional ideal
  total : Total ideal

theorem sectionIdeal_ext {F G : SectionIdeal B} (h : F.ideal = G.ideal) : F = G := by
  cases F
  cases G
  cases h
  rfl

def graph (f : (a : A) → B a) : Sigma B → Prop := fun p => f p.1 = p.2

def encodeSection (f : (a : A) → B a) : SectionIdeal B where
  ideal := partsOf (graph f)
  functional := by
    intro a b c hb hc
    have hb' := (union_partsOf (graph f) ⟨a, b⟩).mp hb
    have hc' := (union_partsOf (graph f) ⟨a, c⟩).mp hc
    exact hb'.symm.trans hc'
  total := fun a => ⟨f a, (union_partsOf (graph f) ⟨a, f a⟩).mpr rfl⟩

noncomputable def decodeSection (F : SectionIdeal B) (a : A) : B a :=
  Classical.choose (F.total a)

theorem decode_mem (F : SectionIdeal B) (a : A) :
    unionContents F.ideal ⟨a, decodeSection F a⟩ := Classical.choose_spec (F.total a)

theorem graph_decode (F : SectionIdeal B) (a : A) (b : B a) :
    decodeSection F a = b ↔ unionContents F.ideal ⟨a, b⟩ := by
  constructor
  · intro h
    rw [← h]
    exact decode_mem F a
  · intro h
    exact F.functional a _ b (decode_mem F a) h

theorem decode_encode (f : (a : A) → B a) : decodeSection (encodeSection f) = f := by
  funext a
  exact ((union_partsOf (graph f) ⟨a, decodeSection (encodeSection f) a⟩).mp
    (decode_mem (encodeSection f) a)).symm

theorem encode_decode (F : SectionIdeal B) : encodeSection (decodeSection F) = F := by
  apply sectionIdeal_ext
  have h : graph (decodeSection F) = unionContents F.ideal := by
    funext p
    exact propext (graph_decode F p.1 p.2)
  change partsOf (graph (decodeSection F)) = F.ideal
  rw [h, partsOf_union]

noncomputable def sectionMap (B : A → Type v) : BiMap ((a : A) → B a) (SectionIdeal B) where
  forward := encodeSection
  backward := decodeSection
  backward_forward := decode_encode
  forward_backward := encode_decode

theorem graph_finite (h : FiniteAdmission.FiniteCarrier A) (f : (a : A) → B a) :
    PredicateAdmission.Finite (graph f) := by
  obtain ⟨l, hl⟩ := h
  refine ⟨l.map (fun a => Sigma.mk a (f a)), ?_⟩
  intro p
  constructor
  · intro hp
    apply List.mem_map.mpr
    refine ⟨p.1, hl p.1, ?_⟩
    cases p with
    | mk a b =>
      change f a = b at hp
      cases hp
      rfl
  · intro hp
    obtain ⟨a, _, ha⟩ := List.mem_map.mp hp
    cases ha
    rfl

theorem finite_base_graph_admitted (h : FiniteAdmission.FiniteCarrier A)
    (C : (Sigma B → Prop) → Prop) (hf : PredicateAdmission.IncludesFinite C)
    (f : (a : A) → B a) : C (graph f) := hf ⟨graph f, graph_finite h f⟩

def sigmaMap (e : (a : A) → BiMap (B a) (D a)) : BiMap (Sigma B) (Sigma D) where
  forward p := ⟨p.1, (e p.1).forward p.2⟩
  backward p := ⟨p.1, (e p.1).backward p.2⟩
  backward_forward p := by cases p; simp only [BiMap.backward_forward]
  forward_backward p := by cases p; simp only [BiMap.forward_backward]

def piMap (e : (a : A) → BiMap (B a) (D a)) :
    BiMap ((a : A) → B a) ((a : A) → D a) where
  forward f a := (e a).forward (f a)
  backward g a := (e a).backward (g a)
  backward_forward f := funext (fun a => (e a).backward_forward (f a))
  forward_backward g := funext (fun a => (e a).forward_backward (g a))

noncomputable def completedSectionMap (e : (a : A) → BiMap (B a) (D a)) :
    BiMap ((a : A) → B a) (SectionIdeal D) :=
  FunctionGraphReconstruction.compose (piMap e) (sectionMap D)

theorem transported_evaluation (e : (a : A) → BiMap (B a) (D a))
    (f : (a : A) → B a) (a : A) :
    decodeSection ((completedSectionMap e).forward f) a = (e a).forward (f a) := by
  change decodeSection (encodeSection ((piMap e).forward f)) a = _
  rw [decode_encode]
  rfl

def sigmaPredicateMap (e : (a : A) → BiMap (B a) (D a)) :
    BiMap (Sigma B → Prop) (Ideal (finiteOrder (Sigma D))) := predicateMap (sigmaMap e)

noncomputable def sectionPredicateMap (e : (a : A) → BiMap (B a) (D a)) :
    BiMap (((a : A) → B a) → Prop) (Ideal (finiteOrder (SectionIdeal D))) :=
  predicateMap (completedSectionMap e)

theorem sigma_predicate_membership (e : (a : A) → BiMap (B a) (D a))
    (P : Sigma B → Prop) (p : Sigma B) :
    unionContents ((sigmaPredicateMap e).forward P) ((sigmaMap e).forward p) ↔ P p :=
  predicateMap_membership (sigmaMap e) P p

theorem section_predicate_membership (e : (a : A) → BiMap (B a) (D a))
    (P : ((a : A) → B a) → Prop) (f : (a : A) → B a) :
    unionContents ((sectionPredicateMap e).forward P) ((completedSectionMap e).forward f) ↔ P f :=
  predicateMap_membership (completedSectionMap e) P f

theorem bimap_quantifiers (e : BiMap X Y) (P : X → Prop) (Q : Y → Prop)
    (h : ∀ x, P x ↔ Q (e.forward x)) :
    ((∀ x, P x) ↔ ∀ y, Q y) ∧ ((∃ x, P x) ↔ ∃ y, Q y) := by
  constructor
  · constructor
    · intro hp y
      have hy := (h (e.backward y)).mp (hp _)
      simpa only [e.forward_backward] using hy
    · exact fun hq x => (h x).mpr (hq _)
  · constructor
    · rintro ⟨x, hx⟩
      exact ⟨e.forward x, (h x).mp hx⟩
    · rintro ⟨y, hy⟩
      refine ⟨e.backward y, (h _).mpr ?_⟩
      simpa only [e.forward_backward] using hy

theorem section_predicate_quantifiers (e : (a : A) → BiMap (B a) (D a))
    (P : (((a : A) → B a) → Prop) → Prop)
    (Q : Ideal (finiteOrder (SectionIdeal D)) → Prop)
    (h : ∀ p, P p ↔ Q ((sectionPredicateMap e).forward p)) :
    ((∀ p, P p) ↔ ∀ i, Q i) ∧ ((∃ p, P p) ↔ ∃ i, Q i) :=
  bimap_quantifiers (sectionPredicateMap e) P Q h

theorem empty_fiber_not_total (a : A) (h : ∀ _b : B a, False) (I : GraphIdeal B) : ¬ Total I := by
  intro ht
  obtain ⟨b, _⟩ := ht a
  exact h b

theorem no_section_ideal_of_empty_fiber (a : A) (h : ∀ _b : B a, False) :
    ¬ Nonempty (SectionIdeal B) := by
  rintro ⟨F⟩
  exact empty_fiber_not_total a h F.ideal F.total

def zeroSection (n : Nat) : Fin (n+1) := ⟨0, Nat.zero_lt_succ n⟩

def zeroIdeal : SectionIdeal (fun n : Nat => Fin (n+1)) := encodeSection zeroSection

theorem zero_ideal_membership (n : Nat) (b : Fin (n+1)) :
    unionContents zeroIdeal.ideal ⟨n, b⟩ ↔ b.val = 0 := by
  change unionContents (partsOf (graph zeroSection)) ⟨n, b⟩ ↔ _
  rw [union_partsOf]
  change zeroSection n = b ↔ b.val = 0
  constructor
  · intro h
    exact (congrArg Fin.val h).symm
  · intro h
    exact Fin.ext h.symm

theorem zero_ideal_evaluation (n : Nat) : (decodeSection zeroIdeal n).val = 0 :=
  (zero_ideal_membership n _).mp (decode_mem zeroIdeal n)

theorem fin_zero_fiber_no_total (I : GraphIdeal (fun n : Nat => Fin n)) : ¬ Total I :=
  empty_fiber_not_total 0 (fun b => Fin.elim0 b) I

end DependentCompletion
