import Std

/-!
Tarski--Vaught witness adequacy and finitary elementary hulls.
The ambient structure, classical interpretation and witness selectors are explicit.
This is an exact semantic sufficiency theorem, not an independent selection of
mathematical content or an exclusive metaphysical grounding theorem.
-/
namespace RootConstitution
universe u v w

structure Signature where
  Func : Nat → Type u
  Rel : Nat → Type u

inductive Term (L : Signature.{u}) (n : Nat) : Type u where
  | var : Fin n → Term L n
  | app {k : Nat} : L.Func k → (Fin k → Term L n) → Term L n

inductive Formula (L : Signature.{u}) : Nat → Type u where
  | equal {n} : Term L n → Term L n → Formula L n
  | relation {n k} : L.Rel k → (Fin k → Term L n) → Formula L n
  | neg {n} : Formula L n → Formula L n
  | conj {n} : Formula L n → Formula L n → Formula L n
  | exists_ {n} : Formula L (n+1) → Formula L n

structure Structure (L : Signature.{u}) (D : Type v) where
  function : ∀ {k}, L.Func k → (Fin k → D) → D
  relation : ∀ {k}, L.Rel k → (Fin k → D) → Prop

variable {L : Signature.{u}} {A : Type v} {B : Type w}

def Term.eval (M : Structure L A) (v : Fin n → A) : Term L n → A
  | .var i => v i
  | .app f ts => M.function f (fun i => (ts i).eval M v)

def cons (a : A) (v : Fin n → A) : Fin (n+1) → A := Fin.cases a v

def Formula.sat (M : Structure L A) {n : Nat} (v : Fin n → A) : Formula L n → Prop
  | .equal t s => t.eval M v = s.eval M v
  | .relation r ts => M.relation r (fun i => (ts i).eval M v)
  | .neg p => ¬ p.sat M v
  | .conj p q => p.sat M v ∧ q.sat M v
  | .exists_ p => ∃ a, p.sat M (cons a v)

structure Embedding (M : Structure L A) (N : Structure L B) where
  map : A → B
  injective : ∀ {a b}, map a = map b → a = b
  function : ∀ {k} (f : L.Func k) (v : Fin k → A),
    map (M.function f v) = N.function f (fun i => map (v i))
  relation : ∀ {k} (r : L.Rel k) (v : Fin k → A),
    M.relation r v ↔ N.relation r (fun i => map (v i))

theorem map_cons (f : A → B) (a : A) (v : Fin n → A) :
    (fun i => f (cons a v i)) = cons (f a) (fun i => f (v i)) := by
  funext i
  cases i using Fin.cases with
  | zero => rfl
  | succ j => rfl

theorem eval_embedding (M : Structure L A) (N : Structure L B) (e : Embedding M N)
    (v : Fin n → A) (t : Term L n) :
    e.map (t.eval M v) = t.eval N (fun i => e.map (v i)) := by
  induction t with
  | var i => rfl
  | app f ts ih =>
    change e.map (M.function f (fun i => (ts i).eval M v)) = _
    rw [e.function]
    change N.function f (fun i => e.map ((ts i).eval M v)) =
      N.function f (fun i => (ts i).eval N (fun j => e.map (v j)))
    exact congrArg (N.function f) (funext ih)

def Elementary (M : Structure L A) (N : Structure L B) (e : Embedding M N) : Prop :=
  ∀ n (p : Formula L n) (v : Fin n → A),
    p.sat M v ↔ p.sat N (fun i => e.map (v i))

/-- Ambient existential facts over internal finite parameters have internal witnesses.
The ambient formula is NOT assumed to have the same truth in the substructure. -/
def WitnessAdequate (M : Structure L A) (N : Structure L B) (e : Embedding M N) : Prop :=
  ∀ n (p : Formula L (n+1)) (v : Fin n → A),
    (∃ b, p.sat N (cons b (fun i => e.map (v i)))) →
    ∃ a, p.sat N (cons (e.map a) (fun i => e.map (v i)))

theorem elementary_witness (M : Structure L A) (N : Structure L B) (e : Embedding M N)
    (he : Elementary M N e) : WitnessAdequate M N e := by
  intro n p v h
  have hm : (Formula.exists_ p).sat M v := (he n (.exists_ p) v).mpr h
  obtain ⟨a, ha⟩ := hm
  refine ⟨a, ?_⟩
  have ht := (he (n+1) p (cons a v)).mp ha
  rw [map_cons] at ht
  exact ht

theorem witness_elementary (M : Structure L A) (N : Structure L B) (e : Embedding M N)
    (hw : WitnessAdequate M N e) : Elementary M N e := by
  intro n p
  induction p with
  | equal t s =>
    intro v
    change t.eval M v = s.eval M v ↔
      t.eval N (fun i => e.map (v i)) = s.eval N (fun i => e.map (v i))
    rw [← eval_embedding M N e v t, ← eval_embedding M N e v s]
    exact ⟨congrArg e.map, e.injective⟩
  | relation r ts =>
    intro v
    change M.relation r (fun i => (ts i).eval M v) ↔
      N.relation r (fun i => (ts i).eval N (fun j => e.map (v j)))
    rw [e.relation]
    have hargs : (fun i => e.map ((ts i).eval M v)) =
        (fun i => (ts i).eval N (fun j => e.map (v j))) :=
      funext (fun i => eval_embedding M N e v (ts i))
    rw [hargs]
  | neg p ih =>
    intro v
    exact ⟨fun h hn => h ((ih v).mpr hn), fun h hm => h ((ih v).mp hm)⟩
  | conj p q ihp ihq =>
    intro v
    exact ⟨fun h => ⟨(ihp v).mp h.1, (ihq v).mp h.2⟩,
      fun h => ⟨(ihp v).mpr h.1, (ihq v).mpr h.2⟩⟩
  | @exists_ n p ih =>
    intro v
    constructor
    · intro h
      obtain ⟨a, ha⟩ := h
      refine ⟨e.map a, ?_⟩
      have ht := (ih (cons a v)).mp ha
      rw [map_cons] at ht
      exact ht
    · intro h
      obtain ⟨a, ha⟩ := hw n p v h
      refine ⟨a, ?_⟩
      apply (ih (cons a v)).mpr
      rw [map_cons]
      exact ha

/-- Exact Tarski--Vaught criterion, all formulas and all finite parameter contexts. -/
theorem elementary_iff_witness (M : Structure L A) (N : Structure L B)
    (e : Embedding M N) : Elementary M N e ↔ WitnessAdequate M N e :=
  ⟨elementary_witness M N e, witness_elementary M N e⟩

def Formula.all (p : Formula L (n+1)) : Formula L n := .neg (.exists_ (.neg p))

theorem all_semantics (M : Structure L A) (p : Formula L (n+1)) (v : Fin n → A) :
    p.all.sat M v ↔ ∀ a, p.sat M (cons a v) := by
  classical
  change (¬ ∃ a, ¬ p.sat M (cons a v)) ↔ _
  constructor
  · intro h a
    apply Classical.byContradiction
    intro ha
    exact h ⟨a, ha⟩
  · intro h hn
    obtain ⟨a, ha⟩ := hn
    exact ha (h a)

/-- Supplied semantic selectors. Their correctness is an input, not a claim that
an arbitrary generative mechanism has discovered the ambient truth relation. -/
structure WitnessSelectors (M : Structure L A) where
  select : ∀ n, Formula L (n+1) → (Fin n → A) → A
  correct : ∀ n (p : Formula L (n+1)) (v : Fin n → A),
    (∃ a, p.sat M (cons a v)) → p.sat M (cons (select n p v) v)

theorem conditional_witness [Nonempty A] (P : A → Prop) :
    ∃ a, (∃ b, P b) → P a := by
  classical
  by_cases h : ∃ b, P b
  · obtain ⟨b, hb⟩ := h
    exact ⟨b, fun _ => hb⟩
  · exact ⟨Classical.choice (inferInstance : Nonempty A), fun hp => False.elim (h hp)⟩

noncomputable def classicalSelectors (M : Structure L A) [Nonempty A] : WitnessSelectors M where
  select _n p v := Classical.choose (conditional_witness (fun a => p.sat M (cons a v)))
  correct _n p v := Classical.choose_spec (conditional_witness (fun a => p.sat M (cons a v)))

/-- Least generated membership. Every constructor uses finitely many parameters. -/
inductive Hull (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop) : A → Prop where
  | seed (a : A) : Seed a → Hull M W Seed a
  | function {k} (f : L.Func k) (v : Fin k → A) :
      (∀ i, Hull M W Seed (v i)) → Hull M W Seed (M.function f v)
  | witness {n} (p : Formula L (n+1)) (v : Fin n → A) :
      (∀ i, Hull M W Seed (v i)) → Hull M W Seed (W.select n p v)

structure ClosedUnder (M : Structure L A) (W : WitnessSelectors M) (Seed C : A → Prop) : Prop where
  seeds : ∀ a, Seed a → C a
  functions : ∀ {k} (f : L.Func k) (v : Fin k → A), (∀ i, C (v i)) → C (M.function f v)
  witnesses : ∀ {n} (p : Formula L (n+1)) (v : Fin n → A),
    (∀ i, C (v i)) → C (W.select n p v)

theorem hull_closed (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop) :
    ClosedUnder M W Seed (Hull M W Seed) :=
  ⟨Hull.seed, Hull.function, Hull.witness⟩

theorem hull_least (M : Structure L A) (W : WitnessSelectors M) (Seed C : A → Prop)
    (hC : ClosedUnder M W Seed C) (a : A) (ha : Hull M W Seed a) : C a := by
  induction ha with
  | seed a hs => exact hC.seeds a hs
  | function f v _ ih => exact hC.functions f v ih
  | witness p v _ ih => exact hC.witnesses p v ih

theorem hull_iff_all_closed (M : Structure L A) (W : WitnessSelectors M)
    (Seed : A → Prop) (a : A) :
    Hull M W Seed a ↔ ∀ C, ClosedUnder M W Seed C → C a := by
  constructor
  · intro ha C hC; exact hull_least M W Seed C hC a ha
  · intro h; exact h (Hull M W Seed) (hull_closed M W Seed)

def hullStructure (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop) :
    Structure L {a : A // Hull M W Seed a} where
  function f v := ⟨M.function f (fun i => (v i).val),
    Hull.function f (fun i => (v i).val) (fun i => (v i).property)⟩
  relation r v := M.relation r (fun i => (v i).val)

def hullEmbedding (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop) :
    Embedding (hullStructure M W Seed) M where
  map := Subtype.val
  injective := Subtype.ext
  function _ _ := rfl
  relation _ _ := Iff.rfl

theorem hull_witnessAdequate (M : Structure L A) (W : WitnessSelectors M)
    (Seed : A → Prop) :
    WitnessAdequate (hullStructure M W Seed) M (hullEmbedding M W Seed) := by
  intro n p v hex
  let a := W.select n p (fun i => (v i).val)
  have ha : Hull M W Seed a := Hull.witness p (fun i => (v i).val) (fun i => (v i).property)
  exact ⟨⟨a, ha⟩, W.correct n p (fun i => (v i).val) hex⟩

/-- Positive bridge: least finitary witness closure preserves every first-order formula. -/
theorem hull_elementary (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop) :
    Elementary (hullStructure M W Seed) M (hullEmbedding M W Seed) :=
  witness_elementary _ _ _ (hull_witnessAdequate M W Seed)

theorem hull_contains_seeds (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop)
    (a : A) (ha : Seed a) : Hull M W Seed a := Hull.seed a ha

theorem hull_nonempty (M : Structure L A) (W : WitnessSelectors M) (Seed : A → Prop)
    (h : ∃ a, Seed a) : Nonempty {a : A // Hull M W Seed a} := by
  obtain ⟨a, ha⟩ := h
  exact ⟨⟨a, Hull.seed a ha⟩⟩

def Term.rename (ρ : Fin n → Fin m) : Term L n → Term L m
  | .var i => .var (ρ i)
  | .app f ts => .app f (fun i => (ts i).rename ρ)

def liftRename (ρ : Fin n → Fin m) : Fin (n+1) → Fin (m+1) :=
  Fin.cases 0 (fun i => (ρ i).succ)

def Formula.rename (ρ : Fin n → Fin m) : Formula L n → Formula L m
  | .equal t s => .equal (t.rename ρ) (s.rename ρ)
  | .relation r ts => .relation r (fun i => (ts i).rename ρ)
  | .neg p => .neg (p.rename ρ)
  | .conj p q => .conj (p.rename ρ) (q.rename ρ)
  | .exists_ p => .exists_ (p.rename (liftRename ρ))

theorem eval_rename (M : Structure L A) (t : Term L n) (ρ : Fin n → Fin m)
    (v : Fin m → A) : (t.rename ρ).eval M v = t.eval M (fun i => v (ρ i)) := by
  induction t with
  | var i => rfl
  | app f ts ih =>
    exact congrArg (M.function f) (funext ih)

theorem cons_liftRename (a : A) (v : Fin m → A) (ρ : Fin n → Fin m) :
    (fun i => cons a v (liftRename ρ i)) = cons a (fun i => v (ρ i)) := by
  funext i
  cases i using Fin.cases with
  | zero => rfl
  | succ j => rfl

theorem sat_rename (M : Structure L A) (p : Formula L n) (ρ : Fin n → Fin m)
    (v : Fin m → A) : (p.rename ρ).sat M v ↔ p.sat M (fun i => v (ρ i)) := by
  induction p generalizing m with
  | equal t s =>
    change (t.rename ρ).eval M v = (s.rename ρ).eval M v ↔ _
    rw [eval_rename, eval_rename]
    exact Iff.rfl
  | relation r ts =>
    change M.relation r (fun i => ((ts i).rename ρ).eval M v) ↔ _
    have h := funext (fun i => eval_rename M (ts i) ρ v)
    rw [h]
    exact Iff.rfl
  | neg p ih =>
    exact ⟨fun h hp => h ((ih ρ v).mpr hp), fun h hp => h ((ih ρ v).mp hp)⟩
  | conj p q ihp ihq =>
    exact ⟨fun h => ⟨(ihp ρ v).mp h.1, (ihq ρ v).mp h.2⟩,
      fun h => ⟨(ihp ρ v).mpr h.1, (ihq ρ v).mpr h.2⟩⟩
  | exists_ p ih =>
    have h : ∀ a, (p.rename (liftRename ρ)).sat M (cons a v) ↔
        p.sat M (cons a (fun i => v (ρ i))) := by
      intro a
      have hi := ih (liftRename ρ) (cons a v)
      rw [cons_liftRename] at hi
      exact hi
    exact ⟨fun ⟨a, ha⟩ => ⟨a, (h a).mp ha⟩, fun ⟨a, ha⟩ => ⟨a, (h a).mpr ha⟩⟩

def emptyAssignment : Fin 0 → A := Fin.elim0

theorem empty_assignment_unique (v : Fin 0 → A) : v = emptyAssignment := by
  funext i; exact Fin.elim0 i

def Formula.or (p q : Formula L n) : Formula L n := .neg (.conj (.neg p) (.neg q))

theorem or_semantics (M : Structure L A) (p q : Formula L n) (v : Fin n → A) :
    (p.or q).sat M v ↔ p.sat M v ∨ q.sat M v := by
  classical
  change (¬ (¬ p.sat M v ∧ ¬ q.sat M v)) ↔ _
  constructor
  · intro h
    by_cases hp : p.sat M v
    · exact Or.inl hp
    · apply Or.inr
      apply Classical.byContradiction
      intro hq
      exact h ⟨hp, hq⟩
  · intro h hn
    cases h with
    | inl hp => exact hn.1 hp
    | inr hq => exact hn.2 hq

/-- A tagged existential query uses two distinct closed named values. -/
def tagged (z o : Term L 0) (p : Formula L 0) : Formula L 1 :=
  Formula.or
    (.conj (.equal (.var 0) (z.rename Fin.elim0)) (p.rename Fin.elim0))
    (.conj (.equal (.var 0) (o.rename Fin.elim0)) (.neg (p.rename Fin.elim0)))

theorem tagged_semantics (M : Structure L A) (z o : Term L 0) (p : Formula L 0) (a : A) :
    (tagged z o p).sat M (cons a emptyAssignment) ↔
      (a = z.eval M emptyAssignment ∧ p.sat M emptyAssignment) ∨
      (a = o.eval M emptyAssignment ∧ ¬ p.sat M emptyAssignment) := by
  rw [tagged, or_semantics]
  have hp := sat_rename M p (Fin.elim0 : Fin 0 → Fin 1) (cons a emptyAssignment)
  have hz := eval_rename M z (Fin.elim0 : Fin 0 → Fin 1) (cons a emptyAssignment)
  have ho := eval_rename M o (Fin.elim0 : Fin 0 → Fin 1) (cons a emptyAssignment)
  rw [empty_assignment_unique (fun i => cons a emptyAssignment (Fin.elim0 i))] at hp hz ho
  change ((a = (z.rename Fin.elim0).eval M (cons a emptyAssignment) ∧
      (p.rename Fin.elim0).sat M (cons a emptyAssignment)) ∨
    (a = (o.rename Fin.elim0).eval M (cons a emptyAssignment) ∧
      ¬ (p.rename Fin.elim0).sat M (cons a emptyAssignment))) ↔ _
  rw [hz, ho, hp]

theorem tagged_has_witness (M : Structure L A) (z o : Term L 0) (p : Formula L 0) :
    ∃ a, (tagged z o p).sat M (cons a emptyAssignment) := by
  classical
  by_cases hp : p.sat M emptyAssignment
  · exact ⟨z.eval M emptyAssignment, (tagged_semantics M z o p _).mpr (Or.inl ⟨rfl, hp⟩)⟩
  · exact ⟨o.eval M emptyAssignment, (tagged_semantics M z o p _).mpr (Or.inr ⟨rfl, hp⟩)⟩

/-- Exact informational converse: unrestricted correct witness selection determines
EVERY sentence truth when two distinct closed values are available. No algorithm
for selection or impossibility-of-computation theorem is claimed. -/
theorem selector_recovers_sentence (M : Structure L A) (W : WitnessSelectors M)
    (z o : Term L 0) (hne : z.eval M emptyAssignment ≠ o.eval M emptyAssignment)
    (p : Formula L 0) :
    W.select 0 (tagged z o p) emptyAssignment = z.eval M emptyAssignment ↔
      p.sat M emptyAssignment := by
  have h := W.correct 0 (tagged z o p) emptyAssignment (tagged_has_witness M z o p)
  have ht := (tagged_semantics M z o p _).mp h
  constructor
  · intro hz
    cases ht with
    | inl hp => exact hp.2
    | inr hp => exact False.elim (hne (hz.symm.trans hp.1))
  · intro hp
    cases ht with
    | inl h => exact h.1
    | inr h => exact False.elim (h.2 hp)

/-! A concrete failure of ordinary compositional closure: the natural numbers
embed in the integers with exactly the same zero and successor operations, but
only the ambient integers contain a predecessor of zero. No predicate is toggled. -/
inductive IterationFunction : Nat → Type where
  | zero : IterationFunction 0
  | next : IterationFunction 1

def iterationLanguage : Signature where
  Func := IterationFunction
  Rel _ := Empty

def natIteration : Structure iterationLanguage Nat where
  function f v := match f with
    | .zero => 0
    | .next => (v 0) + 1
  relation r _ := Empty.elim r

def intIteration : Structure iterationLanguage Int where
  function f v := match f with
    | .zero => 0
    | .next => (v 0) + 1
  relation r _ := Empty.elim r

def naturalEmbedding : Embedding natIteration intIteration where
  map := Int.ofNat
  injective := Int.ofNat.inj
  function := by
    intro k f v
    cases f with
    | zero => rfl
    | next => exact Int.natCast_succ (v 0)
  relation r _ := Empty.elim r

def predecessorBody : Formula iterationLanguage 1 :=
  .equal (.app .next (fun _ => .var 0)) (.app .zero Fin.elim0)

def predecessorSentence : Formula iterationLanguage 0 := .exists_ predecessorBody

theorem integer_predecessor_truth : predecessorSentence.sat intIteration emptyAssignment := by
  refine ⟨(-1 : Int), ?_⟩
  change (-1 : Int) + 1 = 0
  decide

theorem natural_predecessor_false : ¬ predecessorSentence.sat natIteration emptyAssignment := by
  intro h
  obtain ⟨a, ha⟩ := h
  change a + 1 = 0 at ha
  omega

theorem compositional_embedding_not_elementary :
    ¬ Elementary natIteration intIteration naturalEmbedding := by
  intro h
  have ht := (h 0 predecessorSentence emptyAssignment).mpr (by
    rw [empty_assignment_unique (fun i : Fin 0 => naturalEmbedding.map (emptyAssignment i))]
    exact integer_predecessor_truth)
  exact natural_predecessor_false ht

theorem compositional_embedding_not_witnessAdequate :
    ¬ WitnessAdequate natIteration intIteration naturalEmbedding :=
  fun h => compositional_embedding_not_elementary
    (witness_elementary natIteration intIteration naturalEmbedding h)

end RootConstitution

/- Kernel dependency audit of every named theorem. -/
#print axioms RootConstitution.map_cons
#print axioms RootConstitution.eval_embedding
#print axioms RootConstitution.elementary_witness
#print axioms RootConstitution.witness_elementary
#print axioms RootConstitution.elementary_iff_witness
#print axioms RootConstitution.all_semantics
#print axioms RootConstitution.conditional_witness
#print axioms RootConstitution.hull_closed
#print axioms RootConstitution.hull_least
#print axioms RootConstitution.hull_iff_all_closed
#print axioms RootConstitution.hull_witnessAdequate
#print axioms RootConstitution.hull_elementary
#print axioms RootConstitution.hull_contains_seeds
#print axioms RootConstitution.hull_nonempty
#print axioms RootConstitution.eval_rename
#print axioms RootConstitution.cons_liftRename
#print axioms RootConstitution.sat_rename
#print axioms RootConstitution.empty_assignment_unique
#print axioms RootConstitution.or_semantics
#print axioms RootConstitution.tagged_semantics
#print axioms RootConstitution.tagged_has_witness
#print axioms RootConstitution.selector_recovers_sentence
#print axioms RootConstitution.integer_predecessor_truth
#print axioms RootConstitution.natural_predecessor_false
#print axioms RootConstitution.compositional_embedding_not_elementary
#print axioms RootConstitution.compositional_embedding_not_witnessAdequate
