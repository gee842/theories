import IdealWarrant
import PrefixSafety

/-! A4: finite/infinite history classification of prefix-tree ideals. Finite words
are finite coordinate functions; no finite alphabet or effective presentation is
assumed. The complete boundary consists of mathematical paths, not enacted runs. -/
namespace CompletionWarrant.HistoryIdeals

universe u
variable {A : Type u}

structure Word (A : Type u) where
  length : Nat
  letter : Fin length → A

def Prefix (v w : Word A) : Prop :=
  v.length ≤ w.length ∧ ∀ i (hi : i < v.length) (hj : i < w.length),
    v.letter ⟨i, hi⟩ = w.letter ⟨i, hj⟩

theorem word_ext (v w : Word A) (hlen : v.length = w.length)
    (h : ∀ i (hi : i < v.length) (hj : i < w.length), v.letter ⟨i, hi⟩ = w.letter ⟨i, hj⟩) :
    v = w := by
  cases v with
  | mk n a =>
    cases w with
    | mk m b =>
      dsimp at hlen
      cases hlen
      have hab : a = b := by
        funext i
        exact h i.val i.isLt i.isLt
      cases hab
      rfl

def wordPoset : Poset (Word A) where
  le := Prefix
  refl v := ⟨Nat.le_refl _, fun _ _ _ => rfl⟩
  trans := by
    intro v w z hvw hwz
    refine ⟨Nat.le_trans hvw.1 hwz.1, ?_⟩
    intro i hi hz
    have hw := Nat.lt_of_lt_of_le hi hvw.1
    exact (hvw.2 i hi hw).trans (hwz.2 i hw hz)
  antisymm := by
    intro v w hvw hwv
    exact word_ext v w (Nat.le_antisymm hvw.1 hwv.1) hvw.2

def tracePrefix (a : Nat → A) (n : Nat) : Word A := ⟨n, fun i => a i.val⟩

def PrefixTrace (w : Word A) (a : Nat → A) : Prop :=
  ∀ i (hi : i < w.length), w.letter ⟨i, hi⟩ = a i

theorem tracePrefix_prefix (a : Nat → A) {m n : Nat} (h : m ≤ n) :
    Prefix (tracePrefix a m) (tracePrefix a n) := ⟨h, fun _ _ _ => rfl⟩

theorem tracePrefix_trace (a : Nat → A) (n : Nat) : PrefixTrace (tracePrefix a n) a :=
  fun _ _ => rfl

theorem prefixTrace_lower {v w : Word A} {a : Nat → A}
    (hvw : Prefix v w) (hwa : PrefixTrace w a) : PrefixTrace v a := by
  intro i hi
  have hw := Nat.lt_of_lt_of_le hi hvw.1
  exact (hvw.2 i hi hw).trans (hwa i hw)

theorem prefixTrace_eq (w : Word A) (a : Nat → A) (h : PrefixTrace w a) :
    w = tracePrefix a w.length :=
  word_ext w (tracePrefix a w.length) rfl (fun i hi _ => h i hi)

def traceIdeal (a : Nat → A) : Ideal (wordPoset (A := A)) where
  mem w := PrefixTrace w a
  nonempty := ⟨tracePrefix a 0, tracePrefix_trace a 0⟩
  lower := prefixTrace_lower
  directed := by
    intro v w hv hw
    refine ⟨tracePrefix a (max v.length w.length), tracePrefix_trace a _, ?_, ?_⟩
    · exact ⟨Nat.le_max_left _ _, fun i hi _ => hv i hi⟩
    · exact ⟨Nat.le_max_right _ _, fun i hi _ => hw i hi⟩

theorem compatible_prefix {v w z : Word A} (hv : Prefix v z) (hw : Prefix w z)
    (hlen : v.length ≤ w.length) : Prefix v w := by
  refine ⟨hlen, ?_⟩
  intro i hi hj
  have hz := Nat.lt_of_lt_of_le hj hw.1
  exact (hv.2 i hi hz).trans (hw.2 i hj hz).symm

theorem ideal_comparable_by_length (I : Ideal (wordPoset (A := A)))
    {v w : Word A} (hv : I.mem v) (hw : I.mem w) (hlen : v.length ≤ w.length) :
    Prefix v w := by
  obtain ⟨z, _, hvz, hwz⟩ := I.directed hv hw
  exact compatible_prefix hvz hwz hlen

theorem bounded_has_max (I : Ideal (wordPoset (A := A))) (N : Nat)
    (hbound : ∀ w, I.mem w → w.length ≤ N) :
    ∃ w, I.mem w ∧ ∀ v, I.mem v → Prefix v w := by
  classical
  induction N with
  | zero =>
    obtain ⟨w, hw⟩ := I.nonempty
    refine ⟨w, hw, fun v hv => ?_⟩
    apply ideal_comparable_by_length I hv hw
    have hv0 := hbound v hv
    omega
  | succ N ih =>
    by_cases hex : ∃ w, I.mem w ∧ w.length = N + 1
    · obtain ⟨w, hw, hlen⟩ := hex
      refine ⟨w, hw, fun v hv => ?_⟩
      apply ideal_comparable_by_length I hv hw
      have hvb := hbound v hv
      omega
    · apply ih
      intro w hw
      have hwb := hbound w hw
      have hne : w.length ≠ N + 1 := fun h => hex ⟨w, hw, h⟩
      omega

theorem bounded_is_principal (I : Ideal (wordPoset (A := A)))
    (hbound : ∃ N, ∀ w, I.mem w → w.length ≤ N) :
    ∃ w, I = principal wordPoset w := by
  obtain ⟨N, hN⟩ := hbound
  obtain ⟨w, hw, hmax⟩ := bounded_has_max I N hN
  refine ⟨w, Ideal.ext (fun v => ?_)⟩
  exact ⟨fun hv => hmax v hv, fun hv => I.lower hv hw⟩

def Unbounded (I : Ideal (wordPoset (A := A))) : Prop :=
  ∀ n, ∃ w, I.mem w ∧ n < w.length

noncomputable def unboundedWord (I : Ideal (wordPoset (A := A))) (h : Unbounded I)
    (n : Nat) : Word A := Classical.choose (h n)

theorem unboundedWord_mem (I : Ideal (wordPoset (A := A))) (h : Unbounded I) (n : Nat) :
    I.mem (unboundedWord I h n) := (Classical.choose_spec (h n)).1

theorem unboundedWord_long (I : Ideal (wordPoset (A := A))) (h : Unbounded I) (n : Nat) :
    n < (unboundedWord I h n).length := (Classical.choose_spec (h n)).2

noncomputable def unionTrace (I : Ideal (wordPoset (A := A))) (h : Unbounded I) : Nat → A :=
  fun n => (unboundedWord I h n).letter ⟨n, unboundedWord_long I h n⟩

theorem mem_unionTrace (I : Ideal (wordPoset (A := A))) (h : Unbounded I)
    (w : Word A) (hw : I.mem w) : PrefixTrace w (unionTrace I h) := by
  intro i hi
  obtain ⟨z, _, hwz, huz⟩ := I.directed hw (unboundedWord_mem I h i)
  have hz := Nat.lt_of_lt_of_le hi hwz.1
  exact (hwz.2 i hi hz).trans (huz.2 i (unboundedWord_long I h i) hz).symm

theorem unionTrace_prefix_mem (I : Ideal (wordPoset (A := A))) (h : Unbounded I)
    (n : Nat) : I.mem (tracePrefix (unionTrace I h) n) := by
  let w := unboundedWord I h n
  have hw := unboundedWord_mem I h n
  have hp := mem_unionTrace I h w hw
  apply I.lower (q := w) _ hw
  refine ⟨Nat.le_of_lt (unboundedWord_long I h n), ?_⟩
  intro i hi hj
  exact (hp i hj).symm

theorem unbounded_is_trace (I : Ideal (wordPoset (A := A))) (h : Unbounded I) :
    I = traceIdeal (unionTrace I h) := by
  apply Ideal.ext
  intro w
  constructor
  · exact mem_unionTrace I h w
  · intro hw
    have heq := prefixTrace_eq w (unionTrace I h) hw
    rw [heq]
    exact unionTrace_prefix_mem I h w.length

/-- A4's complete finite/infinite classification for the full prefix tree. -/
theorem ideal_classification (I : Ideal (wordPoset (A := A))) :
    (∃ w, I = principal wordPoset w) ∨ (∃ a, I = traceIdeal a) := by
  classical
  by_cases hb : ∃ N, ∀ w, I.mem w → w.length ≤ N
  · exact Or.inl (bounded_is_principal I hb)
  · apply Or.inr
    have hu : Unbounded I := by
      intro n
      apply Classical.byContradiction
      intro hn
      apply hb
      refine ⟨n, ?_⟩
      intro w hw
      have hnot : ¬ n < w.length := fun h => hn ⟨w, hw, h⟩
      omega
    exact ⟨unionTrace I hu, unbounded_is_trace I hu⟩

theorem principal_order_iff (v w : Word A) :
    Ideal.LE (principal wordPoset v) (principal wordPoset w) ↔ Prefix v w :=
  principal_le_iff wordPoset v (principal wordPoset w)

theorem finite_infinite_order_iff (w : Word A) (a : Nat → A) :
    Ideal.LE (principal wordPoset w) (traceIdeal a) ↔ PrefixTrace w a :=
  principal_le_iff wordPoset w (traceIdeal a)

theorem infinite_not_below_finite (a : Nat → A) (w : Word A) :
    ¬ Ideal.LE (traceIdeal a) (principal wordPoset w) := by
  intro h
  have hp := h (tracePrefix a (w.length + 1)) (tracePrefix_trace a _)
  have hl : w.length + 1 ≤ w.length := hp.1
  omega

theorem infinite_order_iff (a b : Nat → A) :
    Ideal.LE (traceIdeal a) (traceIdeal b) ↔ a = b := by
  constructor
  · intro h
    funext i
    have hp := h (tracePrefix a (i + 1)) (tracePrefix_trace a _)
    exact hp i (Nat.lt_succ_self i)
  · intro h
    cases h
    exact Ideal.le_refl _

inductive History (A : Type u) where
  | finite : Word A → History A
  | infinite : (Nat → A) → History A

def historyIdeal : History A → Ideal (wordPoset (A := A))
  | .finite w => principal wordPoset w
  | .infinite a => traceIdeal a

def HistoryPrefix : History A → History A → Prop
  | .finite v, .finite w => Prefix v w
  | .finite w, .infinite a => PrefixTrace w a
  | .infinite _, .finite _ => False
  | .infinite a, .infinite b => a = b

/-- All four finite/infinite order comparisons are reflected exactly. -/
theorem history_order_iff (h k : History A) :
    Ideal.LE (historyIdeal h) (historyIdeal k) ↔ HistoryPrefix h k := by
  cases h with
  | finite v =>
    cases k with
    | finite w => exact principal_order_iff v w
    | infinite a => exact finite_infinite_order_iff v a
  | infinite a =>
    cases k with
    | finite w => exact ⟨infinite_not_below_finite a w, False.elim⟩
    | infinite b => exact infinite_order_iff a b

theorem historyIdeal_injective {h k : History A} (heq : historyIdeal h = historyIdeal k) :
    h = k := by
  have hforward : HistoryPrefix h k := (history_order_iff h k).mp (by
    rw [heq]; exact Ideal.le_refl _)
  have hbackward : HistoryPrefix k h := (history_order_iff k h).mp (by
    rw [heq]; exact Ideal.le_refl _)
  cases h with
  | finite v =>
    cases k with
    | finite w =>
      have hvw : v = w := wordPoset.antisymm hforward hbackward
      cases hvw; rfl
    | infinite a => exact False.elim hbackward
  | infinite a =>
    cases k with
    | finite w => exact False.elim hforward
    | infinite b =>
      have hab : a = b := hforward
      cases hab; rfl

theorem historyIdeal_surjective (I : Ideal (wordPoset (A := A))) :
    ∃ h : History A, I = historyIdeal h := by
  cases ideal_classification I with
  | inl h =>
    obtain ⟨w, hw⟩ := h
    exact ⟨.finite w, hw⟩
  | inr h =>
    obtain ⟨a, ha⟩ := h
    exact ⟨.infinite a, ha⟩

def Boundary (H : Word A → Prop) (a : Nat → A) : Prop :=
  ∀ n, H (tracePrefix a n)

def Admitted (H : Word A → Prop) : History A → Prop
  | .finite w => H w
  | .infinite a => Boundary H a

theorem history_admitted_iff (H : Word A → Prop) (hH : LowerBasis wordPoset H)
    (h : History A) : Admits wordPoset H (historyIdeal h) ↔ Admitted H h := by
  cases h with
  | finite w => exact admits_principal_iff wordPoset H hH w
  | infinite a =>
    constructor
    · intro ha n; exact ha (tracePrefix a n) (tracePrefix_trace a n)
    · intro ha w hw
      have heq := prefixTrace_eq w a hw
      rw [heq]
      exact ha w.length

/-- A4 with an arbitrary prefix-closed finite-history language. -/
theorem admitted_history_classification (H : Word A → Prop) (hH : LowerBasis wordPoset H)
    (I : Ideal (wordPoset (A := A))) (hI : Admits wordPoset H I) :
    ∃ h : History A, Admitted H h ∧ I = historyIdeal h := by
  obtain ⟨h, heq⟩ := historyIdeal_surjective I
  refine ⟨h, ?_, heq⟩
  apply (history_admitted_iff H hH h).mp
  rw [← heq]
  exact hI

/-- Every ideal of H has exactly one admitted finite or infinite history, via the
checked lower-subtype identification in IdealWarrant. -/
theorem lower_history_classification (H : Word A → Prop) (hH : LowerBasis wordPoset H)
    (J : Ideal (lowerPoset wordPoset H)) :
    ∃ h : History A, Admitted H h ∧ liftIdeal wordPoset H hH J = historyIdeal h :=
  admitted_history_classification H hH _ (lift_admits wordPoset H hH J)

theorem admitted_history_unique (H : Word A → Prop)
    (I : Ideal (wordPoset (A := A))) {h k : History A}
    (_ : Admitted H h) (_ : Admitted H k)
    (hh : I = historyIdeal h) (hk : I = historyIdeal k) : h = k :=
  historyIdeal_injective (hh.symm.trans hk)

/-- Any class admitting every finite principal history has full finite content. -/
theorem all_finite_content (C : Ideal (wordPoset (A := A)) → Prop)
    (hc : ∀ w, C (principal wordPoset w)) (w : Word A) : Content wordPoset C w :=
  ⟨principal wordPoset w, hc w, wordPoset.refl w⟩

theorem all_finite_hull_full (C : Ideal (wordPoset (A := A)) → Prop)
    (hc : ∀ w, C (principal wordPoset w)) (I : Ideal (wordPoset (A := A))) :
    ScottHull wordPoset C I := fun w _ => all_finite_content C hc w

def FiniteOnly (I : Ideal (wordPoset (A := A))) : Prop := ∃ w, I = principal wordPoset w

theorem infinite_not_finiteOnly (a : Nat → A) : ¬ FiniteOnly (traceIdeal a) := by
  intro h
  obtain ⟨w, hw⟩ := h
  apply infinite_not_below_finite a w
  rw [hw]
  exact Ideal.le_refl _

theorem finiteOnly_not_refutable (a : Nat → A) :
    ¬ FiniteRefutable wordPoset (FiniteOnly (A := A)) := by
  intro h
  obtain ⟨w, _, hex⟩ := h (traceIdeal a) (infinite_not_finiteOnly a)
  exact hex (principal wordPoset w) ⟨w, rfl⟩ (wordPoset.refl w)

theorem finiteOnly_hull_full (I : Ideal (wordPoset (A := A))) :
    ScottHull wordPoset FiniteOnly I := all_finite_hull_full FiniteOnly (fun w => ⟨w, rfl⟩) I

theorem finiteOnly_lower {I J : Ideal (wordPoset (A := A))}
    (hi : FiniteOnly I) (hji : Ideal.LE J I) : FiniteOnly J := by
  obtain ⟨w, rfl⟩ := hi
  apply bounded_is_principal J
  exact ⟨w.length, fun v hv => (hji v hv).1⟩

theorem finiteOnly_not_scottClosed (a : Nat → A) :
    ¬ ScottClosed wordPoset (FiniteOnly (A := A)) :=
  fun hc => finiteOnly_not_refutable a (scottClosed_refutable wordPoset FiniteOnly hc)

/-- Finite partial histories together with infinite histories satisfying K. -/
def PropertyClass (K : (Nat → A) → Prop) (I : Ideal (wordPoset (A := A))) : Prop :=
  FiniteOnly I ∨ ∃ a, K a ∧ I = traceIdeal a

theorem propertyClass_trace_iff (K : (Nat → A) → Prop) (a : Nat → A) :
    PropertyClass K (traceIdeal a) ↔ K a := by
  constructor
  · intro h
    cases h with
    | inl hf => exact False.elim (infinite_not_finiteOnly a hf)
    | inr hi =>
      obtain ⟨b, hb, heq⟩ := hi
      have hab : a = b := (infinite_order_iff a b).mp (by
        rw [heq]; exact Ideal.le_refl _)
      rw [hab]
      exact hb
  · intro ha; exact Or.inr ⟨a, ha, rfl⟩

theorem propertyClass_lower (K : (Nat → A) → Prop)
    {I J : Ideal (wordPoset (A := A))} (hi : PropertyClass K I) (hji : Ideal.LE J I) :
    PropertyClass K J := by
  cases hi with
  | inl hf => exact Or.inl (finiteOnly_lower hf hji)
  | inr ha =>
    obtain ⟨a, ha, rfl⟩ := ha
    cases ideal_classification J with
    | inl hf => exact Or.inl hf
    | inr hb =>
      obtain ⟨b, rfl⟩ := hb
      have heq := (infinite_order_iff b a).mp hji
      cases heq
      exact Or.inr ⟨a, ha, rfl⟩

theorem propertyClass_hull_full (K : (Nat → A) → Prop) (I : Ideal (wordPoset (A := A))) :
    ScottHull wordPoset (PropertyClass K) I :=
  all_finite_hull_full (PropertyClass K) (fun w => Or.inl ⟨w, rfl⟩) I

theorem propertyClass_not_refutable (K : (Nat → A) → Prop) (a : Nat → A) (ha : ¬ K a) :
    ¬ FiniteRefutable wordPoset (PropertyClass K) := by
  intro hc
  have hexclude : ¬ PropertyClass K (traceIdeal a) :=
    fun hi => ha ((propertyClass_trace_iff K a).mp hi)
  obtain ⟨w, _, hw⟩ := hc (traceIdeal a) hexclude
  exact hw (principal wordPoset w) (Or.inl ⟨w, rfl⟩) (wordPoset.refl w)

theorem propertyClass_not_scottClosed (K : (Nat → A) → Prop) (a : Nat → A) (ha : ¬ K a) :
    ¬ ScottClosed wordPoset (PropertyClass K) :=
  fun hc => propertyClass_not_refutable K a ha
    (scottClosed_refutable wordPoset (PropertyClass K) hc)

/-- W5's exact finite-plus-infinite ideal class rejects the all-zero trace. -/
theorem recurrence_ideal_not_refutable :
    ¬ FiniteRefutable wordPoset (PropertyClass PrefixSafety.Recurs) :=
  propertyClass_not_refutable PrefixSafety.Recurs PrefixSafety.allFalse
    PrefixSafety.allFalse_not_recurs

theorem recurrence_ideal_hull_full (I : Ideal (wordPoset (A := Bool))) :
    ScottHull wordPoset (PropertyClass PrefixSafety.Recurs) I :=
  propertyClass_hull_full PrefixSafety.Recurs I

/-- W6's finite-plus-infinite ideal statement for any countable output enumeration. -/
theorem represented_ideal_not_refutable (E : Nat → Option (Nat → Bool)) :
    ¬ FiniteRefutable wordPoset (PropertyClass (PrefixSafety.Represented E)) :=
  propertyClass_not_refutable (PrefixSafety.Represented E) (PrefixSafety.diagonal E)
    (PrefixSafety.diagonal_not_represented E)

theorem represented_ideal_hull_full (E : Nat → Option (Nat → Bool))
    (I : Ideal (wordPoset (A := Bool))) :
    ScottHull wordPoset (PropertyClass (PrefixSafety.Represented E)) I :=
  propertyClass_hull_full (PrefixSafety.Represented E) I

theorem bounded_language_boundary_empty (H : Word A → Prop) (N : Nat)
    (hbound : ∀ w, H w → w.length ≤ N) (a : Nat → A) : ¬ Boundary H a := by
  intro h
  have hb := hbound (tracePrefix a (N + 1)) (h (N + 1))
  change N + 1 ≤ N at hb
  omega

/-- Finite prefixes realized by some admitted infinite trace. -/
def PrefixLanguage (K : (Nat → A) → Prop) (w : Word A) : Prop :=
  ∃ a, K a ∧ PrefixTrace w a

theorem prefixLanguage_lower (K : (Nat → A) → Prop) :
    LowerBasis wordPoset (PrefixLanguage K) := by
  intro v w hvw hw
  obtain ⟨a, ha, hwa⟩ := hw
  exact ⟨a, ha, prefixTrace_lower hvw hwa⟩

theorem boundary_prefixLanguage_iff (K : (Nat → A) → Prop) (a : Nat → A) :
    Boundary (PrefixLanguage K) a ↔ PrefixSafety.PrefixClosure K a := Iff.rfl

/-- W3's closed infinite language has exactly itself as its finite-prefix boundary. -/
theorem closed_language_boundary (K : (Nat → A) → Prop)
    (hK : PrefixSafety.PrefixClosed K) (a : Nat → A) :
    Boundary (PrefixLanguage K) a ↔ K a :=
  (boundary_prefixLanguage_iff K a).trans
    ((PrefixSafety.finiteRefutable_iff_prefixClosure K).mp hK a)

end CompletionWarrant.HistoryIdeals

/- Kernel dependency audit of every named theorem. -/
#print axioms CompletionWarrant.HistoryIdeals.word_ext
#print axioms CompletionWarrant.HistoryIdeals.tracePrefix_prefix
#print axioms CompletionWarrant.HistoryIdeals.tracePrefix_trace
#print axioms CompletionWarrant.HistoryIdeals.prefixTrace_lower
#print axioms CompletionWarrant.HistoryIdeals.prefixTrace_eq
#print axioms CompletionWarrant.HistoryIdeals.compatible_prefix
#print axioms CompletionWarrant.HistoryIdeals.ideal_comparable_by_length
#print axioms CompletionWarrant.HistoryIdeals.bounded_has_max
#print axioms CompletionWarrant.HistoryIdeals.bounded_is_principal
#print axioms CompletionWarrant.HistoryIdeals.unboundedWord_mem
#print axioms CompletionWarrant.HistoryIdeals.unboundedWord_long
#print axioms CompletionWarrant.HistoryIdeals.mem_unionTrace
#print axioms CompletionWarrant.HistoryIdeals.unionTrace_prefix_mem
#print axioms CompletionWarrant.HistoryIdeals.unbounded_is_trace
#print axioms CompletionWarrant.HistoryIdeals.ideal_classification
#print axioms CompletionWarrant.HistoryIdeals.principal_order_iff
#print axioms CompletionWarrant.HistoryIdeals.finite_infinite_order_iff
#print axioms CompletionWarrant.HistoryIdeals.infinite_not_below_finite
#print axioms CompletionWarrant.HistoryIdeals.infinite_order_iff
#print axioms CompletionWarrant.HistoryIdeals.history_order_iff
#print axioms CompletionWarrant.HistoryIdeals.historyIdeal_injective
#print axioms CompletionWarrant.HistoryIdeals.historyIdeal_surjective
#print axioms CompletionWarrant.HistoryIdeals.history_admitted_iff
#print axioms CompletionWarrant.HistoryIdeals.admitted_history_classification
#print axioms CompletionWarrant.HistoryIdeals.lower_history_classification
#print axioms CompletionWarrant.HistoryIdeals.admitted_history_unique
#print axioms CompletionWarrant.HistoryIdeals.all_finite_content
#print axioms CompletionWarrant.HistoryIdeals.all_finite_hull_full
#print axioms CompletionWarrant.HistoryIdeals.infinite_not_finiteOnly
#print axioms CompletionWarrant.HistoryIdeals.finiteOnly_not_refutable
#print axioms CompletionWarrant.HistoryIdeals.finiteOnly_hull_full
#print axioms CompletionWarrant.HistoryIdeals.finiteOnly_lower
#print axioms CompletionWarrant.HistoryIdeals.finiteOnly_not_scottClosed
#print axioms CompletionWarrant.HistoryIdeals.propertyClass_trace_iff
#print axioms CompletionWarrant.HistoryIdeals.propertyClass_lower
#print axioms CompletionWarrant.HistoryIdeals.propertyClass_hull_full
#print axioms CompletionWarrant.HistoryIdeals.propertyClass_not_refutable
#print axioms CompletionWarrant.HistoryIdeals.propertyClass_not_scottClosed
#print axioms CompletionWarrant.HistoryIdeals.recurrence_ideal_not_refutable
#print axioms CompletionWarrant.HistoryIdeals.recurrence_ideal_hull_full
#print axioms CompletionWarrant.HistoryIdeals.represented_ideal_not_refutable
#print axioms CompletionWarrant.HistoryIdeals.represented_ideal_hull_full
#print axioms CompletionWarrant.HistoryIdeals.bounded_language_boundary_empty
#print axioms CompletionWarrant.HistoryIdeals.prefixLanguage_lower
#print axioms CompletionWarrant.HistoryIdeals.boundary_prefixLanguage_iff
#print axioms CompletionWarrant.HistoryIdeals.closed_language_boundary
