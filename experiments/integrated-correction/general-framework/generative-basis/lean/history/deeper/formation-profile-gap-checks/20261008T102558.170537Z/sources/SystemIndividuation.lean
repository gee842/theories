import GenerativeCore

/-!
# Explanatory supports within an admitted joint domain

Support here means sufficiency for a specified response, not causal constitution,
operative use, ownership, or a universal definition of systemhood. Coordinates
are readings of one state; their recombinability is proved only where available.
In a correlated admitted domain two incomparable minimal supports can exist.
An explicit formation step establishes such a domain inside one fixed process.
No world law, empirical correspondence, or unique physical boundary is derived.
-/
namespace SystemIndividuation

universe u v w z

variable {S : Type u} {I : Type v} {R : Type w} {V : Type z}

def Agree (read : S → I → R) (B : I → Prop) (s t : S) : Prop :=
  ∀ i, B i → read s i = read t i

def Supports (admitted : S → Prop) (read : S → I → R)
    (response : S → V) (B : I → Prop) : Prop :=
  ∀ s t, admitted s → admitted t → Agree read B s t → response s = response t

/-- Recombination is a property of the admitted domain, not a default permission
    to vary correlated readings independently. -/
def Recombines (admitted : S → Prop) (read : S → I → R)
    (B C : I → Prop) : Prop :=
  ∀ s t, admitted s → admitted t → Agree read (fun i => B i ∧ C i) s t →
    ∃ m, admitted m ∧ Agree read B s m ∧ Agree read C m t

theorem support_mono {admitted : S → Prop} {read : S → I → R}
    {response : S → V} {B C : I → Prop}
    (h : Supports admitted read response B) (included : ∀ i, B i → C i) :
    Supports admitted read response C := by
  intro s t hs ht same
  exact h s t hs ht (fun i hi => same i (included i hi))

theorem support_restrict_domain {admitted narrower : S → Prop} {read : S → I → R}
    {response : S → V} {B : I → Prop}
    (h : Supports admitted read response B) (inside : ∀ s, narrower s → admitted s) :
    Supports narrower read response B := by
  intro s t hs ht same
  exact h s t (inside s hs) (inside t ht) same

/-- Realizability of the intermediate reading combination suffices to intersect
    supports. This condition need not be necessary for a particular response. -/
theorem intersection_support_of_recombination
    {admitted : S → Prop} {read : S → I → R} {response : S → V}
    {B C : I → Prop} (hb : Supports admitted read response B)
    (hc : Supports admitted read response C) (hr : Recombines admitted read B C) :
    Supports admitted read response (fun i => B i ∧ C i) := by
  intro s t hs ht same
  obtain ⟨m, hm, sm, mt⟩ := hr s t hs ht same
  exact (hb s m hs hm sm).trans (hc m t hm ht mt)

/-- In a full coordinate product the required recombination is constructed.
    A decidable selected region permits the explicit splice; no choice axiom. -/
theorem full_product_recombines (B C : I → Prop) [DecidablePred B] :
    Recombines (fun _ : I → R => True) (fun s => s) B C := by
  intro s t _ _ same
  refine ⟨fun i => if B i then s i else t i, trivial, ?_, ?_⟩
  · intro i hi
    exact (if_pos hi).symm
  · intro i hi
    by_cases hb : B i
    · exact (if_pos hb).trans (same i ⟨hb, hi⟩)
    · exact if_neg hb

theorem full_product_support_intersection (B C : I → Prop) [DecidablePred B]
    (response : (I → R) → V)
    (hb : Supports (fun _ => True) (fun s => s) response B)
    (hc : Supports (fun _ => True) (fun s => s) response C) :
    Supports (fun _ => True) (fun s => s) response (fun i => B i ∧ C i) := by
  exact intersection_support_of_recombination hb hc (full_product_recombines B C)

/-- An admitted response contrast must cross every sufficient support. This
    does not identify a unique causal contributor among correlated readings. -/
theorem contrast_excludes_agreement {admitted : S → Prop} {read : S → I → R}
    {response : S → V} {B : I → Prop} (h : Supports admitted read response B)
    {s t : S} (hs : admitted s) (ht : admitted t) (different : response s ≠ response t) :
    ¬ Agree read B s t := by
  intro same
  exact different (h s t hs ht same)

inductive Position where
  | left
  | right
  deriving DecidableEq, Repr

def jointRead (s : Bool × Bool) : Position → Bool
  | .left => s.1
  | .right => s.2

def diagonal (s : Bool × Bool) : Prop := s.1 = s.2

def leftRegion (i : Position) : Prop := i = .left

def rightRegion (i : Position) : Prop := i = .right

def response (s : Bool × Bool) : Bool := s.1

theorem left_supports_on_diagonal :
    Supports diagonal jointRead response leftRegion := by
  intro s t _ _ same
  exact same .left rfl

theorem right_supports_on_diagonal :
    Supports diagonal jointRead response rightRegion := by
  intro s t hs ht same
  exact hs.trans ((same .right rfl).trans ht.symm)

theorem empty_does_not_support_on_diagonal :
    ¬ Supports diagonal jointRead response (fun _ => False) := by
  intro h
  have impossible : false = true := h (false, false) (true, true) rfl rfl
    (fun _ hi => False.elim hi)
  exact Bool.noConfusion impossible

theorem intersection_does_not_support_on_diagonal :
    ¬ Supports diagonal jointRead response (fun i => leftRegion i ∧ rightRegion i) := by
  intro h
  apply empty_does_not_support_on_diagonal
  apply support_mono h
  intro i hi
  have impossible : Position.left = Position.right := hi.1.symm.trans hi.2
  exact Position.noConfusion impossible

theorem diagonal_does_not_recombine :
    ¬ Recombines diagonal jointRead leftRegion rightRegion := by
  intro h
  exact intersection_does_not_support_on_diagonal
    (intersection_support_of_recombination left_supports_on_diagonal
      right_supports_on_diagonal h)

/-- There is no sufficient region included in every sufficient region. This
    refutes a least support for this question/domain, not physical boundaries. -/
theorem diagonal_has_no_least_support :
    ¬ ∃ B, Supports diagonal jointRead response B ∧
      ∀ C, Supports diagonal jointRead response C → ∀ i, B i → C i := by
  rintro ⟨B, hb, least⟩
  apply intersection_does_not_support_on_diagonal
  apply support_mono hb
  intro i hi
  exact ⟨least leftRegion left_supports_on_diagonal i hi,
    least rightRegion right_supports_on_diagonal i hi⟩

/-- Minimality here ranges over regions with a supplied decision procedure.
    Finite left/right regions have such procedures without classical axioms. -/
def MinimalSupport (admitted : S → Prop) (read : S → I → R)
    (value : S → V) (B : I → Prop) : Prop :=
  Supports admitted read value B ∧
    ∀ C, DecidablePred C → Supports admitted read value C →
      (∀ i, C i → B i) → ∀ i, B i → C i

theorem left_is_minimal_support :
    MinimalSupport diagonal jointRead response leftRegion := by
  refine ⟨left_supports_on_diagonal, ?_⟩
  intro C decides hc inside i hi
  letI := decides
  cases i with
  | right => exact Position.noConfusion hi
  | left =>
    apply Decidable.byContradiction
    intro missing
    apply empty_does_not_support_on_diagonal
    apply support_mono hc
    intro j hj
    have located := inside j hj
    cases j with
    | left => exact missing hj
    | right => exact Position.noConfusion located

theorem right_is_minimal_support :
    MinimalSupport diagonal jointRead response rightRegion := by
  refine ⟨right_supports_on_diagonal, ?_⟩
  intro C decides hc inside i hi
  letI := decides
  cases i with
  | left => exact Position.noConfusion hi
  | right =>
    apply Decidable.byContradiction
    intro missing
    apply empty_does_not_support_on_diagonal
    apply support_mono hc
    intro j hj
    have located := inside j hj
    cases j with
    | right => exact missing hj
    | left => exact Position.noConfusion located

/-- An isolated-coordinate contrast is restricted to admitted states. -/
def IsolatedContrast (admitted : S → Prop) (read : S → I → R)
    (value : S → V) (i : I) : Prop :=
  ∃ s t, admitted s ∧ admitted t ∧
    (∀ j, j ≠ i → read s j = read t j) ∧ value s ≠ value t

theorem no_isolated_contrast_on_diagonal (i : Position) :
    ¬ IsolatedContrast diagonal jointRead response i := by
  rintro ⟨s, t, hs, ht, same, different⟩
  cases i with
  | left =>
    exact different (hs.trans ((same .right (by decide)).trans ht.symm))
  | right => exact different (same .left (by decide))

theorem joint_contrast_on_diagonal :
    diagonal (false, false) ∧ diagonal (true, true) ∧
      response (false, false) ≠ response (true, true) := by
  exact ⟨rfl, rfl, by decide⟩

/-! ## Formation and subsequent possibilities inside one fixed law -/

inductive Event where
  | correlate
  | flip
  | pulse
  deriving DecidableEq, Repr

def process : Generative.Process (Bool × Bool) Event where
  step s a t := match a with
    | .correlate => t = (s.1, s.1)
    | .flip => t = (!s.1, !s.2)
    | .pulse => s.1 = true ∧ t = s

theorem correlate_establishes_diagonal (s : Bool × Bool) :
    ∃ t, process.step s .correlate t ∧ diagonal t := by
  exact ⟨(s.1, s.1), rfl, rfl⟩

theorem diagonal_preserved_by_step {s t : Bool × Bool} {a : Event}
    (hs : diagonal s) (step : process.step s a t) : diagonal t := by
  cases a with
  | correlate => cases step; rfl
  | flip =>
    cases step
    exact congrArg Bool.not hs
  | pulse =>
    obtain ⟨_, rfl⟩ := step
    exact hs

theorem diagonal_preserved_by_trace {s t : Bool × Bool} {word : List Event}
    (hs : diagonal s) (trace : Generative.Trace process s word t) : diagonal t := by
  induction trace with
  | nil => exact hs
  | cons step _ ih => exact ih (diagonal_preserved_by_step hs step)

def PossibilitySupport (admitted : S → Prop) (read : S → I → R)
    {A : Type z} (P : Generative.Process S A) (B : I → Prop) : Prop :=
  ∀ s t, admitted s → admitted t → Agree read B s t → ∀ word,
    Generative.Feasible P s word ↔ Generative.Feasible P t word

theorem diagonal_right_identifies_state {s t : Bool × Bool}
    (hs : diagonal s) (ht : diagonal t) (same : Agree jointRead rightRegion s t) : s = t := by
  have right := same .right rfl
  exact Prod.ext (hs.trans (right.trans ht.symm)) right

theorem diagonal_left_identifies_state {s t : Bool × Bool}
    (hs : diagonal s) (ht : diagonal t) (same : Agree jointRead leftRegion s t) : s = t := by
  have left := same .left rfl
  exact Prod.ext left (hs.symm.trans (left.trans ht))

theorem right_supports_all_possibilities_on_diagonal :
    PossibilitySupport diagonal jointRead process rightRegion := by
  intro s t hs ht same _
  cases diagonal_right_identifies_state hs ht same
  exact Iff.rfl

theorem left_supports_all_possibilities_on_diagonal :
    PossibilitySupport diagonal jointRead process leftRegion := by
  intro s t hs ht same _
  cases diagonal_left_identifies_state hs ht same
  exact Iff.rfl

theorem right_does_not_support_all_possibilities_before_restriction :
    ¬ PossibilitySupport (fun _ => True) jointRead process rightRegion := by
  intro h
  have available : Generative.Feasible process (true, true) [.pulse] :=
    ⟨(true, true), .cons ⟨rfl, rfl⟩ (.nil _)⟩
  have matched := (h (false, true) (true, true) trivial trivial
    (fun i hi => by cases hi; rfl) [.pulse]).mpr available
  obtain ⟨t, tr⟩ := matched
  have impossible : false = true := (Generative.trace_singleton_iff.mp tr).1
  exact Bool.noConfusion impossible

theorem formation_and_possibility_change_same_history :
    Generative.Trace process (false, true) [.correlate, .flip, .pulse] (true, true) := by
  exact .cons rfl (.cons rfl (.cons ⟨rfl, rfl⟩ (.nil _)))

theorem pulse_unavailable_immediately_after_formation :
    ¬ Generative.Enabled process (false, false) .pulse := by
  rintro ⟨_, h, _⟩
  exact Bool.noConfusion h

theorem pulse_available_after_flip :
    Generative.Enabled process (true, true) .pulse := by
  exact ⟨(true, true), rfl, rfl⟩

end SystemIndividuation
