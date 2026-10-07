import Std

/-!
Classical finite-branching lifting (A4b). The transition relation may be the
extension relation on full admitted concrete histories. In that application,
prefix-closed obligations and a fixed requested label sequence are retained in
the history nodes and their extension relation; projection to labels alone is
not substituted for this concrete relation. No effective branch-selection or
physical execution of infinity is inferred.
-/
namespace CompletionLifting
universe u

/-- There is a run of exactly n transitions beginning at a. -/
def Reach {α : Type u} (R : α → α → Prop) (a : α) : Nat → Prop
  | 0 => True
  | n + 1 => ∃ b, R a b ∧ Reach R b n

theorem reach_mono {α : Type u} {R : α → α → Prop} {a : α}
    {m n : Nat} (hmn : m ≤ n) (hn : Reach R a n) : Reach R a m := by
  induction m generalizing n a with
  | zero => trivial
  | succ m ih =>
    cases n with
    | zero => omega
    | succ n =>
      obtain ⟨b, hab, hb⟩ := hn
      exact ⟨b, hab, ih (by omega) hb⟩

/-- On a finite list, arbitrarily deep candidates include one unbounded candidate. -/
theorem finite_unbounded {α : Type u} (L : List α) (F : α → Nat → Prop)
    (down : ∀ a m n, m ≤ n → F a n → F a m)
    (allDepths : ∀ n, ∃ a, a ∈ L ∧ F a n) :
    ∃ a, a ∈ L ∧ ∀ n, F a n := by
  classical
  induction L with
  | nil =>
    obtain ⟨a, ha, _⟩ := allDepths 0
    simp at ha
  | cons a L ih =>
    by_cases ha : ∀ n, F a n
    · exact ⟨a, by simp, ha⟩
    · have hn : ∃ n, ¬ F a n := Classical.not_forall.mp ha
      obtain ⟨n, hn⟩ := hn
      have htail : ∀ m, ∃ b, b ∈ L ∧ F b m := by
        intro m
        obtain ⟨b, hb, hbm⟩ := allDepths (n + m)
        have hne : b ≠ a := by
          intro hba
          subst b
          exact hn (down a n (n+m) (by omega) hbm)
        have hbl : b ∈ L := by simpa [List.mem_cons, hne] using hb
        exact ⟨b, hbl, down b m (n+m) (by omega) hbm⟩
      obtain ⟨b, hb, hfb⟩ := ih htail
      exact ⟨b, by simp [hb], hfb⟩

def Unbounded {α : Type u} (R : α → α → Prop) (a : α) : Prop :=
  ∀ n, Reach R a n

theorem unbounded_child {α : Type u} (R : α → α → Prop)
    (children : α → List α) (enumerates : ∀ a b, R a b ↔ b ∈ children a)
    (a : α) (ha : Unbounded R a) : ∃ b, R a b ∧ Unbounded R b := by
  have h : ∀ n, ∃ b, b ∈ children a ∧ Reach R b n := by
    intro n
    obtain ⟨b, hab, hb⟩ := ha (n+1)
    exact ⟨b, (enumerates a b).mp hab, hb⟩
  obtain ⟨b, hb, hu⟩ := finite_unbounded (children a) (Reach R)
    (fun _ _ _ hle hp => reach_mono hle hp) h
  exact ⟨b, (enumerates a b).mpr hb, hu⟩

/-- A4b in rooted-transition form: an unbounded finitely branching node has a ray. -/
theorem infinite_from_unbounded {α : Type u} (R : α → α → Prop)
    (children : α → List α) (enumerates : ∀ a b, R a b ↔ b ∈ children a)
    (a : α) (ha : Unbounded R a) :
    ∃ path : Nat → α, path 0 = a ∧ ∀ n, R (path n) (path (n+1)) := by
  classical
  let U := {x : α // Unbounded R x}
  let next : U → U := fun x =>
    ⟨Classical.choose (unbounded_child R children enumerates x.val x.property),
      (Classical.choose_spec (unbounded_child R children enumerates x.val x.property)).2⟩
  have next_edge : ∀ x : U, R x.val (next x).val := fun x =>
    (Classical.choose_spec (unbounded_child R children enumerates x.val x.property)).1
  let seq : Nat → U := Nat.rec ⟨a, ha⟩ (fun _ x => next x)
  refine ⟨fun n => (seq n).val, rfl, ?_⟩
  intro n
  exact next_edge (seq n)

/-- Finite initial states plus finite branching suffice, exactly as in A4b. -/
theorem finite_initial_lifting {α : Type u} (R : α → α → Prop)
    (initial : List α) (children : α → List α)
    (enumerates : ∀ a b, R a b ↔ b ∈ children a)
    (arbitraryDepth : ∀ n, ∃ a, a ∈ initial ∧ Reach R a n) :
    ∃ path : Nat → α, path 0 ∈ initial ∧ ∀ n, R (path n) (path (n+1)) := by
  obtain ⟨a, ha, hu⟩ := finite_unbounded initial (Reach R)
    (fun _ _ _ hle hp => reach_mono hle hp) arbitraryDepth
  obtain ⟨path, hp, he⟩ := infinite_from_unbounded R children enumerates a hu
  exact ⟨path, hp ▸ ha, he⟩


/-- Retain the requested-label position in the transition state. -/
def RequestedStep {α : Type u} {σ : Type v} (step : α → σ → α → Prop)
    (word : Nat → σ) (p q : Nat × α) : Prop :=
  q.1 = p.1 + 1 ∧ step p.2 (word p.1) q.2

/-- The fixed-label formulation of A4b, with concrete states retained. -/
theorem labelled_lifting {α : Type u} {σ : Type v} (step : α → σ → α → Prop)
    (word : Nat → σ) (initial : List α) (children : α → σ → List α)
    (enumerates : ∀ a label b, step a label b ↔ b ∈ children a label)
    (arbitraryDepth : ∀ n, ∃ a, a ∈ initial ∧ Reach (RequestedStep step word) (0,a) n) :
    ∃ path : Nat → α, path 0 ∈ initial ∧
      ∀ n, step (path n) (word n) (path (n+1)) := by
  let roots : List (Nat × α) := initial.map (fun a => (0,a))
  let nexts : (Nat × α) → List (Nat × α) := fun p =>
    (children p.2 (word p.1)).map (fun a => (p.1+1,a))
  have hen : ∀ p q, RequestedStep step word p q ↔ q ∈ nexts p := by
    intro p q
    constructor
    · rintro ⟨ht, he⟩
      apply List.mem_map.mpr
      exact ⟨q.2, (enumerates _ _ _).mp he, Prod.ext ht.symm rfl⟩
    · intro h
      obtain ⟨a, ha, hq⟩ := List.mem_map.mp h
      cases hq
      exact ⟨rfl, (enumerates _ _ _).mpr ha⟩
  have harb : ∀ n, ∃ p, p ∈ roots ∧ Reach (RequestedStep step word) p n := by
    intro n
    obtain ⟨a, ha, hr⟩ := arbitraryDepth n
    exact ⟨(0,a), List.mem_map.mpr ⟨a, ha, rfl⟩, hr⟩
  obtain ⟨path, hroot, hedge⟩ := finite_initial_lifting
    (RequestedStep step word) roots nexts hen harb
  obtain ⟨a, ha, hzero⟩ := List.mem_map.mp hroot
  have clock : ∀ n, (path n).1 = n := by
    intro n
    induction n with
    | zero => exact congrArg Prod.fst hzero.symm
    | succ n ih => exact (hedge n).1.trans (congrArg (fun k => k+1) ih)
  refine ⟨fun n => (path n).2, ?_, ?_⟩
  · have hs := congrArg Prod.snd hzero
    change (path 0).2 ∈ initial
    rw [← hs]
    exact ha
  · intro n
    have hh := (hedge n).2
    rw [clock] at hh
    exact hh

end CompletionLifting

/- Kernel axiom audit for every named theorem in this module. -/
#print axioms CompletionLifting.reach_mono
#print axioms CompletionLifting.finite_unbounded
#print axioms CompletionLifting.unbounded_child
#print axioms CompletionLifting.infinite_from_unbounded
#print axioms CompletionLifting.finite_initial_lifting
#print axioms CompletionLifting.labelled_lifting
