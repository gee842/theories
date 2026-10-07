import Std

/-
Completion-warrant W3--W6, 7 October 2026.
All quantification over traces is over Nat -> A, with no finite carrier bound.
The explicit prefix topology below is independent of the property being tested.
'Safety' is a technical trace classification, not an ethical appraisal.
-/
namespace CompletionWarrant.PrefixSafety

universe u v
abbrev Trace (A : Type u) := Nat → A
abbrev Property (A : Type u) := Trace A → Prop

def SamePrefix {A : Type u} (n : Nat) (a b : Trace A) : Prop :=
  ∀ i, i < n → a i = b i

theorem samePrefix_refl {A : Type u} (n : Nat) (a : Trace A) : SamePrefix n a a :=
  fun _ _ => rfl

theorem samePrefix_symm {A : Type u} {n : Nat} {a b : Trace A}
    (h : SamePrefix n a b) : SamePrefix n b a :=
  fun i hi => (h i hi).symm

theorem samePrefix_trans {A : Type u} {n : Nat} {a b c : Trace A}
    (h : SamePrefix n a b) (g : SamePrefix n b c) : SamePrefix n a c :=
  fun i hi => (h i hi).trans (g i hi)

theorem samePrefix_mono {A : Type u} {m n : Nat} {a b : Trace A}
    (hmn : m ≤ n) (h : SamePrefix n a b) : SamePrefix m a b :=
  fun i hi => h i (Nat.lt_of_lt_of_le hi hmn)

/-- Basic neighborhoods require agreement at finitely many initial positions. -/
def PrefixOpen {A : Type u} (U : Property A) : Prop :=
  ∀ a, U a → ∃ n, ∀ b, SamePrefix n a b → U b

/-- Closedness means that the complement is open in the specified topology. -/
def PrefixClosed {A : Type u} (K : Property A) : Prop :=
  PrefixOpen (fun a => ¬ K a)

theorem prefixOpen_empty {A : Type u} : PrefixOpen (fun _ : Trace A => False) := by
  intro a ha
  exact False.elim ha

theorem prefixOpen_univ {A : Type u} : PrefixOpen (fun _ : Trace A => True) := by
  intro a _
  exact ⟨0, fun _ _ => True.intro⟩

theorem prefixOpen_union {A : Type u} {J : Type v} (U : J → Property A)
    (h : ∀ j, PrefixOpen (U j)) : PrefixOpen (fun a => ∃ j, U j a) := by
  intro a ha
  obtain ⟨j, hj⟩ := ha
  obtain ⟨n, hn⟩ := h j a hj
  exact ⟨n, fun b hab => ⟨j, hn b hab⟩⟩

theorem prefixOpen_inter {A : Type u} {U V : Property A}
    (hU : PrefixOpen U) (hV : PrefixOpen V) :
    PrefixOpen (fun a => U a ∧ V a) := by
  intro a ha
  obtain ⟨n, hn⟩ := hU a ha.1
  obtain ⟨m, hm⟩ := hV a ha.2
  refine ⟨max n m, fun b hab => ?_⟩
  exact ⟨hn b (samePrefix_mono (Nat.le_max_left _ _) hab),
    hm b (samePrefix_mono (Nat.le_max_right _ _) hab)⟩

theorem cylinder_open {A : Type u} (n : Nat) (a : Trace A) :
    PrefixOpen (fun b => SamePrefix n a b) := by
  intro b hab
  exact ⟨n, fun c hbc => samePrefix_trans hab hbc⟩

/-- A violation has a finite prefix that no admitted trace extends. -/
def FiniteRefutable {A : Type u} (K : Property A) : Prop :=
  ∀ a, ¬ K a → ∃ n, ∀ b, SamePrefix n a b → ¬ K b

/-- Every finite prefix occurs in some admitted trace. -/
def PrefixClosure {A : Type u} (K : Property A) : Property A :=
  fun a => ∀ n, ∃ b, K b ∧ SamePrefix n a b

theorem finiteRefutable_iff_closed {A : Type u} (K : Property A) :
    FiniteRefutable K ↔ PrefixClosed K := Iff.rfl

theorem subset_prefixClosure {A : Type u} {K : Property A} {a : Trace A}
    (ha : K a) : PrefixClosure K a :=
  fun n => ⟨a, ha, samePrefix_refl n a⟩

theorem prefixClosure_mono {A : Type u} {K L : Property A}
    (h : ∀ a, K a → L a) : ∀ a, PrefixClosure K a → PrefixClosure L a := by
  intro a ha n
  obtain ⟨b, hb, hab⟩ := ha n
  exact ⟨b, h b hb, hab⟩

theorem finiteRefutable_iff_prefixClosure {A : Type u} (K : Property A) :
    FiniteRefutable K ↔ ∀ a, PrefixClosure K a ↔ K a := by
  classical
  constructor
  · intro h a
    constructor
    · intro hc
      apply Classical.byContradiction
      intro ha
      obtain ⟨n, hn⟩ := h a ha
      obtain ⟨b, hb, hab⟩ := hc n
      exact hn b hab hb
    · exact subset_prefixClosure
  · intro h a ha
    apply Classical.byContradiction
    intro hbad
    apply ha
    apply (h a).mp
    intro n
    apply Classical.byContradiction
    intro hnone
    apply hbad
    refine ⟨n, fun b hab hb => ?_⟩
    exact hnone ⟨b, hb, hab⟩

theorem prefixClosure_closed {A : Type u} (K : Property A) :
    PrefixClosed (PrefixClosure K) := by
  classical
  intro a ha
  apply Classical.byContradiction
  intro hbad
  apply ha
  intro n
  apply Classical.byContradiction
  intro hnone
  apply hbad
  refine ⟨n, fun b hab hb => ?_⟩
  obtain ⟨c, hc, hbc⟩ := hb n
  exact hnone ⟨c, hc, samePrefix_trans hab hbc⟩

theorem prefixClosure_least {A : Type u} {K L : Property A}
    (hKL : ∀ a, K a → L a) (hL : PrefixClosed L) :
    ∀ a, PrefixClosure K a → L a := by
  intro a ha
  exact ((finiteRefutable_iff_prefixClosure L).mp hL a).mp
    (prefixClosure_mono hKL a ha)

theorem prefixClosure_idempotent {A : Type u} (K : Property A) (a : Trace A) :
    PrefixClosure (PrefixClosure K) a ↔ PrefixClosure K a := by
  constructor
  · exact prefixClosure_least (fun _ h => h) (prefixClosure_closed K) a
  · exact subset_prefixClosure

/-- The intersection of all closed supersets: independently specified closure. -/
def TopologicalClosure {A : Type u} (K : Property A) : Property A :=
  fun a => ∀ L, PrefixClosed L → (∀ b, K b → L b) → L a

theorem topologicalClosure_iff_prefixClosure {A : Type u} (K : Property A)
    (a : Trace A) : TopologicalClosure K a ↔ PrefixClosure K a := by
  constructor
  · intro h
    exact h (PrefixClosure K) (prefixClosure_closed K) (fun _ => subset_prefixClosure)
  · intro h L hL hKL
    exact prefixClosure_least hKL hL a h

/-- A finite-prefix rule need not have an infinite extension. -/
def AllPrefixesIn {A : Type u} (H : Nat → Trace A → Prop) : Property A :=
  fun a => ∀ n, H n a

theorem boundary_closed {A : Type u} (H : Nat → Trace A → Prop)
    (hlocal : ∀ n a b, SamePrefix n a b → H n a → H n b) :
    PrefixClosed (AllPrefixesIn H) := by
  classical
  intro a ha
  apply Classical.byContradiction
  intro hbad
  apply ha
  intro n
  apply Classical.byContradiction
  intro hn
  apply hbad
  refine ⟨n, fun b hab hb => ?_⟩
  exact hn (hlocal n b a (samePrefix_symm hab) (hb n))

/- Infinite recurrence and a termination-event property on full infinite traces. -/
def Recurs (a : Trace Bool) : Prop := ∀ n, ∃ m, n ≤ m ∧ a m = true

def EventuallyTrue (a : Trace Bool) : Prop := ∃ n, a n = true

def allFalse : Trace Bool := fun _ => false

def allTrue : Trace Bool := fun _ => true

/-- A finite proof term establishes the genuinely infinitary recurrence property. -/
theorem allTrue_recurs : Recurs allTrue :=
  fun n => ⟨n, Nat.le_refl n, rfl⟩

theorem allFalse_not_recurs : ¬ Recurs allFalse := by
  intro h
  obtain ⟨m, _, hm⟩ := h 0
  cases hm

theorem allFalse_not_eventuallyTrue : ¬ EventuallyTrue allFalse := by
  rintro ⟨n, hn⟩
  cases hn

/-- Retain exactly the first n symbols, then append true forever. -/
def trueTail (a : Trace Bool) (n : Nat) : Trace Bool :=
  fun i => if i < n then a i else true

theorem trueTail_prefix (a : Trace Bool) (n : Nat) : SamePrefix n a (trueTail a n) := by
  intro i hi
  simp [trueTail, hi]

theorem trueTail_recurs (a : Trace Bool) (n : Nat) : Recurs (trueTail a n) := by
  intro k
  refine ⟨max k n, Nat.le_max_left _ _, ?_⟩
  have h : ¬ max k n < n := Nat.not_lt.mpr (Nat.le_max_right _ _)
  simp [trueTail, h]

theorem trueTail_eventuallyTrue (a : Trace Bool) (n : Nat) :
    EventuallyTrue (trueTail a n) := by
  exact ⟨n, by simp [trueTail]⟩

theorem recurrence_closure_all (a : Trace Bool) : PrefixClosure Recurs a :=
  fun n => ⟨trueTail a n, trueTail_recurs a n, trueTail_prefix a n⟩

theorem terminationEvent_closure_all (a : Trace Bool) : PrefixClosure EventuallyTrue a :=
  fun n => ⟨trueTail a n, trueTail_eventuallyTrue a n, trueTail_prefix a n⟩

theorem recurrence_not_finiteRefutable : ¬ FiniteRefutable Recurs := by
  intro h
  exact allFalse_not_recurs
    (((finiteRefutable_iff_prefixClosure Recurs).mp h allFalse).mp
      (recurrence_closure_all allFalse))

theorem recurrence_not_closed : ¬ PrefixClosed Recurs := recurrence_not_finiteRefutable

theorem terminationEvent_not_finiteRefutable : ¬ FiniteRefutable EventuallyTrue := by
  intro h
  exact allFalse_not_eventuallyTrue
    (((finiteRefutable_iff_prefixClosure EventuallyTrue).mp h allFalse).mp
      (terminationEvent_closure_all allFalse))

/- Exact unary finite/infinite prefix-length space: some n is a^n; none is a^∞.
This is not the carrier of the preceding infinite-only topology. -/
abbrev UnaryHistory := Option Nat

def UnaryLE (x y : UnaryHistory) : Prop :=
  match x, y with
  | some n, some m => n ≤ m
  | some _, none => True
  | none, some _ => False
  | none, none => True

def UnaryFinite (x : UnaryHistory) : Prop := ∃ n, x = some n

def UnaryPrefix (n : Nat) (x : UnaryHistory) : Prop := UnaryLE (some n) x

def UnaryFiniteRefutable (C : UnaryHistory → Prop) : Prop :=
  ∀ x, ¬ C x → ∃ n, UnaryPrefix n x ∧ ∀ y, C y → ¬ UnaryPrefix n y

def UnaryDirected (C : UnaryHistory → Prop) : Prop :=
  (∃ x, C x) ∧ ∀ x, C x → ∀ y, C y →
    ∃ z, C z ∧ UnaryLE x z ∧ UnaryLE y z

def UnarySupremum (C : UnaryHistory → Prop) (s : UnaryHistory) : Prop :=
  (∀ x, C x → UnaryLE x s) ∧
    ∀ y, (∀ x, C x → UnaryLE x y) → UnaryLE s y

def UnaryDirectedClosed (C : UnaryHistory → Prop) : Prop :=
  ∀ D, UnaryDirected D → (∀ x, D x → C x) →
    ∀ s, UnarySupremum D s → C s

theorem unary_finite_not_infinity : ¬ UnaryFinite none := by
  rintro ⟨n, hn⟩
  cases hn

theorem unary_finite_directed : UnaryDirected UnaryFinite := by
  constructor
  · exact ⟨some 0, 0, rfl⟩
  · intro x hx y hy
    obtain ⟨n, rfl⟩ := hx
    obtain ⟨m, rfl⟩ := hy
    exact ⟨some (max n m), ⟨max n m, rfl⟩,
      Nat.le_max_left _ _, Nat.le_max_right _ _⟩

theorem unary_finite_supremum_infinity : UnarySupremum UnaryFinite none := by
  constructor
  · intro x hx
    obtain ⟨n, rfl⟩ := hx
    trivial
  · intro y hy
    cases y with
    | none => trivial
    | some m =>
      have h := hy (some (m + 1)) ⟨m + 1, rfl⟩
      change m + 1 ≤ m at h
      omega

theorem unary_finite_not_directedClosed : ¬ UnaryDirectedClosed UnaryFinite := by
  intro h
  exact unary_finite_not_infinity
    (h UnaryFinite unary_finite_directed (fun _ h => h) none
      unary_finite_supremum_infinity)

theorem unary_finite_not_finiteRefutable : ¬ UnaryFiniteRefutable UnaryFinite := by
  intro h
  obtain ⟨n, _, hn⟩ := h none unary_finite_not_infinity
  exact hn (some n) ⟨n, rfl⟩ (Nat.le_refl n)

/- General effective-admission obstruction. The enumeration may be partial,
noncomputable, redundant or empty; the proof makes no assumption that totality
of a finite program is decidable. A program interpretation is supplied below. -/
def Represented (E : Nat → Option (Trace Bool)) : Property Bool :=
  fun a => ∃ n, E n = some a

def diagonal (E : Nat → Option (Trace Bool)) : Trace Bool :=
  fun n => match E n with
    | none => false
    | some a => !(a n)

theorem bool_ne_neg (b : Bool) : b ≠ !b := by
  cases b <;> decide

theorem diagonal_not_represented (E : Nat → Option (Trace Bool)) :
    ¬ Represented E (diagonal E) := by
  rintro ⟨n, hn⟩
  have heq : diagonal E n = !(diagonal E n) := by
    conv => lhs; unfold diagonal; rw [hn]
  exact bool_ne_neg (diagonal E n) heq

/-- An explicit realization requirement, not built into Represented. -/
def RealizesEveryFinitePrefix (E : Nat → Option (Trace Bool)) : Prop :=
  ∀ a n, ∃ b, Represented E b ∧ SamePrefix n a b

theorem represented_closure_all (E : Nat → Option (Trace Bool))
    (h : RealizesEveryFinitePrefix E) (a : Trace Bool) :
    PrefixClosure (Represented E) a := h a

theorem represented_not_finiteRefutable (E : Nat → Option (Trace Bool))
    (h : RealizesEveryFinitePrefix E) : ¬ FiniteRefutable (Represented E) := by
  intro hs
  exact diagonal_not_represented E
    (((finiteRefutable_iff_prefixClosure (Represented E)).mp hs (diagonal E)).mp
      (represented_closure_all E h (diagonal E)))

/-- Finite instructions have natural-number codes with a left inverse.
No computability definition is replaced by this premise; any concrete machine
model must supply this coding and an interpretation of its total outputs. -/
structure ProgramCoding (Program : Type) where
  encode : Program → Nat
  decode : Nat → Option Program
  decode_encode : ∀ p, decode (encode p) = some p

def programEnumeration {Program : Type} (code : ProgramCoding Program)
    (output : Program → Option (Trace Bool)) : Nat → Option (Trace Bool) :=
  fun n => match code.decode n with
    | none => none
    | some p => output p

theorem programOutput_iff_represented {Program : Type} (code : ProgramCoding Program)
    (output : Program → Option (Trace Bool)) (a : Trace Bool) :
    (∃ p, output p = some a) ↔ Represented (programEnumeration code output) a := by
  constructor
  · rintro ⟨p, hp⟩
    refine ⟨code.encode p, ?_⟩
    simp [programEnumeration, code.decode_encode, hp]
  · rintro ⟨n, hn⟩
    cases he : code.decode n with
    | none => simp [programEnumeration, he] at hn
    | some p => exact ⟨p, by simpa [programEnumeration, he] using hn⟩

theorem some_trace_not_programOutput {Program : Type} (code : ProgramCoding Program)
    (output : Program → Option (Trace Bool)) :
    ∃ a, ¬ ∃ p, output p = some a := by
  refine ⟨diagonal (programEnumeration code output), ?_⟩
  intro h
  exact diagonal_not_represented _ ((programOutput_iff_represented code output _).mp h)

/- Countability is checked for genuinely finite binary instruction strings. -/
def bitCode : List Bool → Nat
  | [] => 0
  | false :: p => 2 * bitCode p + 1
  | true :: p => 2 * bitCode p + 2

theorem bitCode_injective (p q : List Bool) (h : bitCode p = bitCode q) : p = q := by
  induction p generalizing q with
  | nil =>
    cases q with
    | nil => rfl
    | cons b q =>
      cases b <;> simp [bitCode] at h <;> omega
  | cons b p ih =>
    cases q with
    | nil => cases b <;> simp [bitCode] at h <;> omega
    | cons c q =>
      cases b <;> cases c
      · have hp : bitCode p = bitCode q := by simp [bitCode] at h; omega
        exact congrArg (List.cons false) (ih q hp)
      · simp [bitCode] at h
        omega
      · simp [bitCode] at h
        omega
      · have hp : bitCode p = bitCode q := by simp [bitCode] at h; omega
        exact congrArg (List.cons true) (ih q hp)

noncomputable def bitDecode (n : Nat) : Option (List Bool) := by
  classical
  exact if h : ∃ p, bitCode p = n then some (Classical.choose h) else none

theorem bitDecode_bitCode (p : List Bool) : bitDecode (bitCode p) = some p := by
  classical
  have h : ∃ q, bitCode q = bitCode p := ⟨p, rfl⟩
  simp only [bitDecode, dif_pos h]
  exact congrArg some (bitCode_injective _ _ (Classical.choose_spec h))

noncomputable def finiteBitProgramCoding : ProgramCoding (List Bool) where
  encode := bitCode
  decode := bitDecode
  decode_encode := bitDecode_bitCode

/-- Every semantics of finite binary programs misses an infinite binary trace.
The semantics is arbitrary and may identify many programs or leave them undefined. -/
theorem finitePrograms_miss_some_trace (output : List Bool → Option (Trace Bool)) :
    ∃ a, ¬ ∃ p, output p = some a :=
  some_trace_not_programOutput finiteBitProgramCoding output

/-- Prefix realization is an extra, explicit property of the program semantics. -/
def ProgramRealizesPrefixes (output : List Bool → Option (Trace Bool)) : Prop :=
  ∀ a n, ∃ p b, output p = some b ∧ SamePrefix n a b

theorem programRealization_implies_dense (output : List Bool → Option (Trace Bool))
    (h : ProgramRealizesPrefixes output) :
    RealizesEveryFinitePrefix (programEnumeration finiteBitProgramCoding output) := by
  intro a n
  obtain ⟨p, b, hp, hab⟩ := h a n
  exact ⟨b, (programOutput_iff_represented finiteBitProgramCoding output b).mp ⟨p, hp⟩,
    hab⟩

theorem finitePrograms_not_finiteRefutable (output : List Bool → Option (Trace Bool))
    (h : ProgramRealizesPrefixes output) :
    ¬ FiniteRefutable (fun a => ∃ p, output p = some a) := by
  intro hs
  have he : FiniteRefutable (Represented (programEnumeration finiteBitProgramCoding output)) := by
    intro a ha
    have hna : ¬ ∃ p, output p = some a := by
      intro hp
      exact ha ((programOutput_iff_represented finiteBitProgramCoding output a).mp hp)
    obtain ⟨n, hn⟩ := hs a hna
    refine ⟨n, fun b hab hb => ?_⟩
    exact hn b hab ((programOutput_iff_represented finiteBitProgramCoding output b).mpr hb)
  exact represented_not_finiteRefutable _ (programRealization_implies_dense output h) he

/-- Finite literal output followed by zeros: a concrete prefix-realizing semantics. -/
def emitLiteral : List Bool → Trace Bool
  | [], _ => false
  | b :: _, 0 => b
  | _ :: p, i + 1 => emitLiteral p i

def prefixLiteral : Nat → Trace Bool → List Bool
  | 0, _ => []
  | n + 1, a => a 0 :: prefixLiteral n (fun i => a (i + 1))

theorem emitLiteral_matches_prefix (n : Nat) (a : Trace Bool) :
    SamePrefix n a (emitLiteral (prefixLiteral n a)) := by
  induction n generalizing a with
  | zero => intro i hi; omega
  | succ n ih =>
    intro i hi
    cases i with
    | zero => rfl
    | succ i =>
      exact ih (fun j => a (j + 1)) i (by omega)

def literalOutput (p : List Bool) : Option (Trace Bool) := some (emitLiteral p)

theorem literalOutput_realizes_prefixes : ProgramRealizesPrefixes literalOutput := by
  intro a n
  exact ⟨prefixLiteral n a, emitLiteral (prefixLiteral n a), rfl,
    emitLiteral_matches_prefix n a⟩

theorem literalOutput_not_finiteRefutable :
    ¬ FiniteRefutable (fun a => ∃ p, literalOutput p = some a) :=
  finitePrograms_not_finiteRefutable literalOutput literalOutput_realizes_prefixes

/-- Any program interpretation containing literal-then-zero traces realizes prefixes.
For a standard computable-trace interpretation this is the precise interface to check. -/
theorem contains_literals_realizes_prefixes
    (output : List Bool → Option (Trace Bool))
    (hlit : ∀ p, ∃ q, output q = some (emitLiteral p)) :
    ProgramRealizesPrefixes output := by
  intro a n
  obtain ⟨q, hq⟩ := hlit (prefixLiteral n a)
  exact ⟨q, emitLiteral (prefixLiteral n a), hq, emitLiteral_matches_prefix n a⟩

/-- Finite dead ends do not imply an infinite boundary member. -/
theorem deadEnd_boundary_empty {A : Type u} (a : Trace A) :
    ¬ AllPrefixesIn (fun n _ => n ≤ 1) a := by
  intro h
  have hh := h 2
  omega

end CompletionWarrant.PrefixSafety

/- Kernel dependency audit for every named theorem. -/
#print axioms CompletionWarrant.PrefixSafety.samePrefix_refl
#print axioms CompletionWarrant.PrefixSafety.samePrefix_symm
#print axioms CompletionWarrant.PrefixSafety.samePrefix_trans
#print axioms CompletionWarrant.PrefixSafety.samePrefix_mono
#print axioms CompletionWarrant.PrefixSafety.prefixOpen_empty
#print axioms CompletionWarrant.PrefixSafety.prefixOpen_univ
#print axioms CompletionWarrant.PrefixSafety.prefixOpen_union
#print axioms CompletionWarrant.PrefixSafety.prefixOpen_inter
#print axioms CompletionWarrant.PrefixSafety.cylinder_open
#print axioms CompletionWarrant.PrefixSafety.finiteRefutable_iff_closed
#print axioms CompletionWarrant.PrefixSafety.subset_prefixClosure
#print axioms CompletionWarrant.PrefixSafety.prefixClosure_mono
#print axioms CompletionWarrant.PrefixSafety.finiteRefutable_iff_prefixClosure
#print axioms CompletionWarrant.PrefixSafety.prefixClosure_closed
#print axioms CompletionWarrant.PrefixSafety.prefixClosure_least
#print axioms CompletionWarrant.PrefixSafety.prefixClosure_idempotent
#print axioms CompletionWarrant.PrefixSafety.topologicalClosure_iff_prefixClosure
#print axioms CompletionWarrant.PrefixSafety.boundary_closed
#print axioms CompletionWarrant.PrefixSafety.allTrue_recurs
#print axioms CompletionWarrant.PrefixSafety.allFalse_not_recurs
#print axioms CompletionWarrant.PrefixSafety.allFalse_not_eventuallyTrue
#print axioms CompletionWarrant.PrefixSafety.trueTail_prefix
#print axioms CompletionWarrant.PrefixSafety.trueTail_recurs
#print axioms CompletionWarrant.PrefixSafety.trueTail_eventuallyTrue
#print axioms CompletionWarrant.PrefixSafety.recurrence_closure_all
#print axioms CompletionWarrant.PrefixSafety.terminationEvent_closure_all
#print axioms CompletionWarrant.PrefixSafety.recurrence_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.recurrence_not_closed
#print axioms CompletionWarrant.PrefixSafety.terminationEvent_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.unary_finite_not_infinity
#print axioms CompletionWarrant.PrefixSafety.unary_finite_directed
#print axioms CompletionWarrant.PrefixSafety.unary_finite_supremum_infinity
#print axioms CompletionWarrant.PrefixSafety.unary_finite_not_directedClosed
#print axioms CompletionWarrant.PrefixSafety.unary_finite_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.bool_ne_neg
#print axioms CompletionWarrant.PrefixSafety.diagonal_not_represented
#print axioms CompletionWarrant.PrefixSafety.represented_closure_all
#print axioms CompletionWarrant.PrefixSafety.represented_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.programOutput_iff_represented
#print axioms CompletionWarrant.PrefixSafety.some_trace_not_programOutput
#print axioms CompletionWarrant.PrefixSafety.bitCode_injective
#print axioms CompletionWarrant.PrefixSafety.bitDecode_bitCode
#print axioms CompletionWarrant.PrefixSafety.finitePrograms_miss_some_trace
#print axioms CompletionWarrant.PrefixSafety.programRealization_implies_dense
#print axioms CompletionWarrant.PrefixSafety.finitePrograms_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.emitLiteral_matches_prefix
#print axioms CompletionWarrant.PrefixSafety.literalOutput_realizes_prefixes
#print axioms CompletionWarrant.PrefixSafety.literalOutput_not_finiteRefutable
#print axioms CompletionWarrant.PrefixSafety.contains_literals_realizes_prefixes
#print axioms CompletionWarrant.PrefixSafety.deadEnd_boundary_empty
