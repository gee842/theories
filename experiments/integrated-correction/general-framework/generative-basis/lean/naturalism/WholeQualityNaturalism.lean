import EthicalOrientation

/-!
# Whole-history quality as a natural property: supervenience, structure, explanation

Four standard arguments for ethical naturalism are given formal counterparts over
the unchanged `Process`/`Trace` semantics.

* Supervenience (Jackson). `supervenes_factors` proves that a property `M`
  supervening on a base `N` is a function on the classes of `N`-identical cases;
  `base_defined_supervenes` gives the converse for functions of the base. That is the formal step from global supervenience to a
  necessarily coextensive base-defined property. Identity of properties, as
  opposed to coextension, is not a theorem here.
* The base is the whole history. `Run` keeps every intermediate state as data.
  `Along R r` says that `R` holds across each actual transition of `r`. It is a
  function of the visited-state list (`along_supervenes_on_states`). For the
  conditions-of-continuation relation, it is not a function of the endpoints and
  action word (`quality_not_fixed_by_endpoints_and_word`).
* Structure rather than a shapeless disjunction. The quality composes over
  concatenation through the shared boundary state (`along_append`), and is
  invariant under exact re-representation (`along_continuation_transport`).
* Explanation and knowledge. A damage-free history keeps every activity that was
  realizable at its start realizable at every later state (`preserved_throughout`).
  Conversely, every loss of a realizable activity occurs at an actual transition
  of the history (`loss_localizes`, and `loss_localizes_nn` without a decidability
  hypothesis). A loss has a finite witness (`witness_refutes_preservation`).

`ContinuationLe` is the existing objective comparison of finite feasible action
words from `EthicalOrientation`. Nothing in this module names it good. The
companion `NaturalismIdentity` shows that all of these properties hold equally
for the opposite orientation, and states what further premise selects one.
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v w

/-! ## 1. Supervenience and Jackson's factorization -/

/-- `M` cannot vary without variation in `N`. -/
def Supervenes {X : Sort u} {B : Sort v} {V : Sort w} (M : X → V) (N : X → B) : Prop :=
  ∀ x y, N x = N y → M x = M y

/-- Two cases are base-identical. -/
def SameBase {X : Sort u} {B : Sort v} (N : X → B) (x y : X) : Prop := N x = N y

/-- Supervenience yields a function on the base-identity classes. -/
theorem supervenes_factors {X : Sort u} {B : Sort v} {V : Sort w}
    (M : X → V) (N : X → B) (h : Supervenes M N) :
    ∃ f : Quot (SameBase N) → V, ∀ x, M x = f (Quot.mk _ x) :=
  ⟨Quot.lift M (fun x y hxy => h x y hxy), fun _ => rfl⟩

/-- For propositions, supervenience as co-variation: base-identical cases agree. -/
def Covaries {X : Sort u} {B : Sort v} (M : X → Prop) (N : X → B) : Prop :=
  ∀ x y, N x = N y → (M x ↔ M y)

theorem covaries_of_supervenes {X : Sort u} {B : Sort v} (M : X → Prop) (N : X → B)
    (h : Supervenes M N) : Covaries M N :=
  fun x y hxy => h x y hxy ▸ Iff.rfl

/-- A property defined from the base supervenes on it. -/
theorem base_defined_supervenes {X : Sort u} {B : Sort v} {V : Sort w}
    (g : B → V) (N : X → B) : Supervenes (fun x => g (N x)) N := by
  intro x y h
  show g (N x) = g (N y)
  rw [h]

/-- Supervenience is inherited by any finer base. -/
theorem supervenes_of_finer {X : Sort u} {B : Sort v} {C : Sort w} {V : Sort u}
    (M : X → V) (N : X → B) (N' : X → C) (coarse : ∀ x y, N' x = N' y → N x = N y)
    (h : Supervenes M N) : Supervenes M N' :=
  fun x y hxy => h x y (coarse x y hxy)

/-! ## 2. Histories with their intermediate states -/

variable {State : Type u} {Action : Type v}

/-- A finite history kept as data: every actual intermediate state is retained. -/
inductive Run (P : Process State Action) : State → State → Type (max u v) where
  | nil (s : State) : Run P s s
  | cons {s m t : State} (a : Action) (h : P.step s a m) (r : Run P m t) : Run P s t

namespace Run

variable {P : Process State Action}

def word : {s t : State} → Run P s t → List Action
  | _, _, nil _ => []
  | _, _, cons a _ r => a :: r.word

/-- The visited states, starting state included. -/
def states : {s t : State} → Run P s t → List State
  | _, _, nil s => [s]
  | s, _, cons _ _ r => s :: r.states

/-- The actual transitions, as pairs of consecutive visited states. -/
def steps : {s t : State} → Run P s t → List (State × State)
  | _, _, nil _ => []
  | s, _, cons (m := m) _ _ r => (s, m) :: r.steps

def append : {s m t : State} → Run P s m → Run P m t → Run P s t
  | _, _, _, nil _, r' => r'
  | _, _, _, cons a h r, r' => cons a h (append r r')

theorem toTrace : {s t : State} → (r : Run P s t) → Trace P s r.word t
  | _, _, nil s => .nil s
  | _, _, cons _ h r => .cons h r.toTrace

theorem word_append : {s m t : State} → (r : Run P s m) → (r' : Run P m t) →
    (r.append r').word = r.word ++ r'.word
  | _, _, _, nil _, _ => rfl
  | _, _, _, cons a _ r, r' => by
    show a :: (r.append r').word = a :: (r.word ++ r'.word)
    rw [word_append r r']

theorem start_mem_states : {s t : State} → (r : Run P s t) → s ∈ r.states
  | _, _, nil s => List.Mem.head _
  | _, _, cons _ _ _ => List.Mem.head _

end Run

/-- Consecutive pairs of a list. -/
def Chain {α : Type u} (R : α → α → Prop) : List α → Prop
  | [] => True
  | [_] => True
  | x :: y :: rest => R x y ∧ Chain R (y :: rest)

/-- The step quality: `R` holds across every actual transition of the history. -/
def Along {P : Process State Action} (R : State → State → Prop) :
    {s t : State} → Run P s t → Prop
  | _, _, .nil _ => True
  | s, _, .cons (m := m) _ _ r => R s m ∧ Along R r

theorem along_iff_steps {P : Process State Action} (R : State → State → Prop) :
    {s t : State} → (r : Run P s t) → (Along R r ↔ ∀ p ∈ r.steps, R p.1 p.2)
  | _, _, .nil _ => by
    constructor
    · intro _ p hp
      cases hp
    · intro _
      exact True.intro
  | s, _, .cons (m := m) _ _ r => by
    have ih := along_iff_steps R r
    constructor
    · rintro ⟨hsm, hr⟩ p hp
      cases hp with
      | head => exact hsm
      | tail _ hp => exact ih.mp hr p hp
    · intro h
      exact ⟨h (s, m) (List.Mem.head _), ih.mpr (fun p hp => h p (List.Mem.tail _ hp))⟩

/-- The step quality is literally a function of the visited-state list. -/
theorem along_iff_chain {P : Process State Action} (R : State → State → Prop) :
    {s t : State} → (r : Run P s t) → (Along R r ↔ Chain R r.states)
  | _, _, .nil _ => Iff.intro (fun _ => True.intro) (fun _ => True.intro)
  | s, _, .cons (m := m) _ _ r => by
    have ih := along_iff_chain R r
    cases r with
    | nil t =>
      exact Iff.intro (fun h => ⟨h.1, True.intro⟩) (fun h => ⟨h.1, True.intro⟩)
    | cons a h r' =>
      exact Iff.intro (fun h => ⟨h.1, ih.mp h.2⟩) (fun h => ⟨h.1, ih.mpr h.2⟩)

/-! ## 3. Supervenience on the whole history and its structure -/

/-- A history taken with its endpoints, so histories of different spans can be compared. -/
def History (P : Process State Action) : Type (max u v) := Σ s t, Run P s t

def History.states {P : Process State Action} (h : History P) : List State := h.2.2.states

/-- Any step quality co-varies with the visited states of the history. -/
theorem along_supervenes_on_states (P : Process State Action) (R : State → State → Prop) :
    Covaries (fun h : History P => Along R h.2.2) History.states := by
  intro x y hxy
  have hx := along_iff_chain R x.2.2
  have hy := along_iff_chain R y.2.2
  have hs : x.2.2.states = y.2.2.states := hxy
  exact Iff.intro (fun h => hy.mpr (hs ▸ hx.mp h)) (fun h => hx.mpr (hs ▸ hy.mp h))

/-- The quality composes through the shared actual boundary state. -/
theorem along_append {P : Process State Action} (R : State → State → Prop) :
    {s m t : State} → (r : Run P s m) → (r' : Run P m t) →
    (Along R (r.append r') ↔ Along R r ∧ Along R r')
  | _, _, _, .nil _, r' => Iff.intro (fun h => ⟨True.intro, h⟩) (fun h => h.2)
  | _, _, _, .cons _ _ r, r' => by
    have ih := along_append R r r'
    constructor
    · rintro ⟨h1, h2⟩
      exact ⟨⟨h1, (ih.mp h2).1⟩, (ih.mp h2).2⟩
    · rintro ⟨⟨h1, h2⟩, h3⟩
      exact ⟨h1, ih.mpr ⟨h2, h3⟩⟩

/-- Weakening the step relation weakens the quality. -/
theorem along_mono {P : Process State Action} {R S : State → State → Prop}
    (hRS : ∀ s t, R s t → S s t) :
    {s t : State} → (r : Run P s t) → Along R r → Along S r
  | _, _, .nil _, _ => True.intro
  | s, _, .cons (m := m) _ _ r, h => ⟨hRS s m h.1, along_mono hRS r h.2⟩

theorem chain_map {α : Type u} {β : Type w} (R : β → β → Prop) (q : α → β) :
    (xs : List α) → (Chain (fun x y => R (q x) (q y)) xs ↔ Chain R (xs.map q))
  | [] => Iff.rfl
  | [_] => Iff.rfl
  | x :: y :: rest => by
    have ih := chain_map R q (y :: rest)
    exact Iff.intro (fun h => ⟨h.1, ih.mp h.2⟩) (fun h => ⟨h.1, ih.mpr h.2⟩)

theorem chain_congr {α : Type u} {R S : α → α → Prop} (h : ∀ x y, R x y ↔ S x y) :
    (xs : List α) → (Chain R xs ↔ Chain S xs)
  | [] => Iff.rfl
  | [_] => Iff.rfl
  | x :: y :: rest => by
    have ih := chain_congr h (y :: rest)
    exact Iff.intro (fun c => ⟨(h x y).mp c.1, ih.mp c.2⟩) (fun c => ⟨(h x y).mpr c.1, ih.mpr c.2⟩)

/-- Exact re-representation of feasible words preserves and reflects the quality. -/
theorem along_continuation_transport {Other : Type w}
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    (hexact : ∀ s word, Feasible P s word ↔ Feasible Q (q s) word)
    {s t : State} (r : Run P s t) :
    Along (ContinuationLe P) r ↔ Chain (ContinuationLe Q) (r.states.map q) :=
  (along_iff_chain _ r).trans ((chain_congr (fun x y => continuation_projection_iff hexact x y)
    r.states).trans (chain_map _ q r.states))

/-! ## 4. Explanation and knowledge of losses -/

variable {P : Process State Action}

/-- An activity stays realizable at every state the history actually visits. -/
def AvailableThroughout (word : List Action) {s t : State} (r : Run P s t) : Prop :=
  ∀ x ∈ r.states, Feasible P x word

/-- A damage-free history keeps every initially realizable activity realizable throughout. -/
theorem preserved_throughout (word : List Action) :
    {s t : State} → (r : Run P s t) → Along (ContinuationLe P) r →
    Feasible P s word → AvailableThroughout word r
  | _, _, .nil _, _, hw => by
    intro x hx
    cases hx with
    | head => exact hw
    | tail _ hx => cases hx
  | _, _, .cons _ _ r, h, hw => by
    intro x hx
    cases hx with
    | head => exact hw
    | tail _ hx => exact preserved_throughout word r h.2 (h.1 word hw) x hx

/-- An activity realizable at `x` but not at `y`. -/
def LostAt (P : Process State Action) (word : List Action) (x y : State) : Prop :=
  Feasible P x word ∧ ¬ Feasible P y word

/-- A single finite witness refutes preservation of conditions. -/
theorem witness_refutes_preservation {word : List Action} {s t : State}
    (h : LostAt P word s t) : ¬ ContinuationLe P s t :=
  fun hle => h.2 (hle word h.1)

/-- Where realizability of the activity is decidable, every loss occurs at an
actual transition of the history. -/
theorem loss_localizes (word : List Action)
    (hdec : ∀ x, Feasible P x word ∨ ¬ Feasible P x word) :
    {s t : State} → (r : Run P s t) → Feasible P s word → ¬ Feasible P t word →
    ∃ p ∈ r.steps, LostAt P word p.1 p.2
  | _, _, .nil _, hs, ht => absurd hs ht
  | s, _, .cons (m := m) _ _ r, hs, ht => by
    cases hdec m with
    | inl hm =>
      obtain ⟨p, hp, hl⟩ := loss_localizes word hdec r hm ht
      exact ⟨p, List.Mem.tail _ hp, hl⟩
    | inr hm => exact ⟨(s, m), List.Mem.head _, hs, hm⟩

/-- Without decidability, a loss cannot fail to occur at some actual transition. -/
theorem loss_localizes_nn (word : List Action) :
    {s t : State} → (r : Run P s t) → Feasible P s word → ¬ Feasible P t word →
    ¬¬ ∃ p ∈ r.steps, LostAt P word p.1 p.2
  | _, _, .nil _, hs, ht => fun _ => ht hs
  | s, _, .cons (m := m) _ _ r, hs, ht => by
    intro hno
    have notLostHere : ¬¬ Feasible P m word :=
      fun hm => hno ⟨(s, m), List.Mem.head _, hs, hm⟩
    apply notLostHere
    intro hm
    apply loss_localizes_nn word r hm ht
    rintro ⟨p, hp, hl⟩
    exact hno ⟨p, List.Mem.tail _ hp, hl⟩

/-- A located loss is incompatible with a damage-free history. -/
theorem located_loss_breaks_quality {word : List Action} {s t : State}
    (r : Run P s t) {p : State × State} (hp : p ∈ r.steps) (hl : LostAt P word p.1 p.2) :
    ¬ Along (ContinuationLe P) r :=
  fun h => witness_refutes_preservation hl ((along_iff_steps _ r).mp h p hp)

/-! ## 5. A dip that endpoints and action words cannot see -/

inductive DipAct where
  | go
  | use
  deriving DecidableEq

/-- Levels 0–2. `go` may fall by at most one level and stay within range;
`use` requires level 2. Supplied for illustration only. -/
def dip : Process Nat DipAct where
  step s a t := match a with
    | .go => t ≤ 2 ∧ s ≤ t + 1
    | .use => s = 2 ∧ t = 2

theorem dip_use_at_two : Feasible dip 2 [DipAct.use] :=
  ⟨2, .cons (show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩) (.nil 2)⟩

theorem dip_no_use_at_one : ¬ Feasible dip 1 [DipAct.use] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs _ =>
    have h12 : (1 : Nat) = 2 := hs.1
    exact absurd h12 (by decide)

/-- Stay at level 2. -/
def steady : Run dip 2 2 :=
  .cons .go (show (2 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 2 + 1 by decide)
    (.cons .go (show (2 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 2 + 1 by decide) (.nil 2))

/-- Fall to level 1 and return. -/
def dipped : Run dip 2 2 :=
  .cons (m := 1) .go (show (1 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 1 + 1 by decide)
    (.cons .go (show (2 : Nat) ≤ 2 ∧ (1 : Nat) ≤ 2 + 1 by decide) (.nil 2))

/-- Same endpoints, same action word; one history damages a realizable activity
on the way and the other does not. -/
theorem quality_not_fixed_by_endpoints_and_word :
    steady.word = dipped.word ∧
      Along (ContinuationLe dip) steady ∧ ¬ Along (ContinuationLe dip) dipped := by
  refine ⟨rfl, ?_, ?_⟩
  · exact ⟨fun _ h => h, fun _ h => h, True.intro⟩
  · exact located_loss_breaks_quality dipped (p := (2, 1)) (List.Mem.head _)
      ⟨dip_use_at_two, dip_no_use_at_one⟩

/-- The quality does not supervene on the action word of histories with fixed endpoints. -/
theorem quality_not_supervenient_on_word :
    ¬ Covaries (fun r : Run dip 2 2 => Along (ContinuationLe dip) r) Run.word := by
  intro h
  obtain ⟨hw, hs, hd⟩ := quality_not_fixed_by_endpoints_and_word
  exact hd ((h steady dipped hw).mp hs)

/-- The explained fact: continuous availability of `use` differs between the two
histories, though both start and end where `use` is available. -/
theorem availability_not_fixed_by_endpoints_and_word :
    steady.word = dipped.word ∧
      AvailableThroughout [DipAct.use] steady ∧ ¬ AvailableThroughout [DipAct.use] dipped := by
  refine ⟨rfl, ?_, ?_⟩
  · exact preserved_throughout _ steady quality_not_fixed_by_endpoints_and_word.2.1 dip_use_at_two
  · intro h
    exact dip_no_use_at_one (h 1 (List.Mem.tail _ (List.Mem.head _)))

end Generative.Naturalism

#print axioms Generative.Naturalism.supervenes_factors
#print axioms Generative.Naturalism.covaries_of_supervenes
#print axioms Generative.Naturalism.base_defined_supervenes
#print axioms Generative.Naturalism.supervenes_of_finer
#print axioms Generative.Naturalism.Run.toTrace
#print axioms Generative.Naturalism.Run.word_append
#print axioms Generative.Naturalism.Run.start_mem_states
#print axioms Generative.Naturalism.along_iff_steps
#print axioms Generative.Naturalism.along_iff_chain
#print axioms Generative.Naturalism.along_supervenes_on_states
#print axioms Generative.Naturalism.along_append
#print axioms Generative.Naturalism.along_mono
#print axioms Generative.Naturalism.chain_map
#print axioms Generative.Naturalism.chain_congr
#print axioms Generative.Naturalism.along_continuation_transport
#print axioms Generative.Naturalism.preserved_throughout
#print axioms Generative.Naturalism.witness_refutes_preservation
#print axioms Generative.Naturalism.loss_localizes
#print axioms Generative.Naturalism.loss_localizes_nn
#print axioms Generative.Naturalism.located_loss_breaks_quality
#print axioms Generative.Naturalism.dip_use_at_two
#print axioms Generative.Naturalism.dip_no_use_at_one
#print axioms Generative.Naturalism.quality_not_fixed_by_endpoints_and_word
#print axioms Generative.Naturalism.quality_not_supervenient_on_word
#print axioms Generative.Naturalism.availability_not_fixed_by_endpoints_and_word
