import Admission

/-!
An explicit successor construction of parity is distinguished from closure over
every ambient Nat-indexed finite chain. On Nat, the latter still entails full
predicate admission once every finite predicate is admitted. Arbitrary target
predicates enter that proof through their predicate-dependent bounded prefixes.
-/
namespace IndexedAssembly
open CompletionWarrant CompletionExamples PredicateAdmission
universe u

structure FiniteChain (A : Type u) where
  stage : Nat → FinitePart A
  increasing : ∀ {i j}, i ≤ j → Included (stage i).mem (stage j).mem

def ChainUnion (T : FiniteChain A) : A → Prop := fun a => ∃ n, (T.stage n).mem a

def FiniteChainClosed (C : (A → Prop) → Prop) : Prop :=
  ∀ T : FiniteChain A, (∀ n, C (T.stage n).mem) → C (ChainUnion T)

def ChainFamily (T : FiniteChain A) : (A → Prop) → Prop :=
  fun P => ∃ n, P = (T.stage n).mem

theorem chainFamily_directed (T : FiniteChain A) : NonemptyDirected (ChainFamily T) := by
  constructor
  · exact ⟨(T.stage 0).mem, 0, rfl⟩
  · rintro P Q ⟨i, rfl⟩ ⟨j, rfl⟩
    exact ⟨(T.stage (Nat.max i j)).mem, ⟨Nat.max i j, rfl⟩,
      T.increasing (Nat.le_max_left i j), T.increasing (Nat.le_max_right i j)⟩

theorem union_chainFamily (T : FiniteChain A) : PredicateUnion (ChainFamily T) = ChainUnion T := by
  funext a
  apply propext
  constructor
  · rintro ⟨P, ⟨n, rfl⟩, hn⟩
    exact ⟨n, hn⟩
  · rintro ⟨n, hn⟩
    exact ⟨(T.stage n).mem, ⟨n, rfl⟩, hn⟩

theorem directed_implies_chain_closed (C : (A → Prop) → Prop)
    (h : DirectedUnionClosed C) : FiniteChainClosed C := by
  intro T ht
  have hc := h (ChainFamily T) (chainFamily_directed T) (by
    rintro P ⟨n, rfl⟩
    exact ht n)
  rwa [union_chainFamily] at hc

def parityStages : Nat → FinitePart Nat
  | 0 => emptyPart Nat
  | n+1 => unionPart (parityStages n) (singletonPart (2*n))

theorem parity_zero (a : Nat) : ¬ (parityStages 0).mem a := fun h => h

theorem parity_successor (n a : Nat) :
    (parityStages (n+1)).mem a ↔ (parityStages n).mem a ∨ a = 2*n := Iff.rfl

theorem parity_stage_membership (n a : Nat) :
    (parityStages n).mem a ↔ ∃ k, k < n ∧ a = 2*k := by
  induction n with
  | zero =>
    constructor
    · exact fun h => False.elim (parity_zero a h)
    · rintro ⟨k, hk, _⟩
      omega
  | succ n ih =>
    rw [parity_successor]
    constructor
    · intro h
      rcases h with h | h
      · obtain ⟨k, hk, ha⟩ := ih.mp h
        exact ⟨k, Nat.lt_succ_of_lt hk, ha⟩
      · exact ⟨n, Nat.lt_succ_self n, h⟩
    · rintro ⟨k, hk, ha⟩
      by_cases hkn : k < n
      · exact Or.inl (ih.mpr ⟨k, hkn, ha⟩)
      · have he : k = n := by omega
        exact Or.inr (he ▸ ha)

theorem parity_stages_finite (n : Nat) : Finite (parityStages n).mem :=
  (parityStages n).finite

theorem parity_stages_increasing {i j : Nat} (hij : i ≤ j) :
    Included (parityStages i).mem (parityStages j).mem := by
  intro a ha
  obtain ⟨k, hk, hka⟩ := (parity_stage_membership i a).mp ha
  exact (parity_stage_membership j a).mpr ⟨k, Nat.lt_of_lt_of_le hk hij, hka⟩

def parityChain : FiniteChain Nat where
  stage := parityStages
  increasing := parity_stages_increasing

theorem parity_union : ChainUnion parityChain = Even := by
  funext a
  apply propext
  constructor
  · rintro ⟨n, hn⟩
    obtain ⟨k, _, hk⟩ := (parity_stage_membership n a).mp hn
    unfold Even
    omega
  · intro ha
    have he : a = 2 * (a / 2) := by unfold Even at ha; omega
    exact ⟨a / 2 + 1, (parity_stage_membership _ _).mpr
      ⟨a / 2, Nat.lt_succ_self _, he⟩⟩

theorem parity_admitted (C : (Nat → Prop) → Prop) (hf : IncludesFinite C)
    (hc : FiniteChainClosed C) : C Even := by
  have h := hc parityChain (fun n => hf (parityStages n))
  rwa [parity_union] at h

theorem finiteOrCofinite_parity_stages (n : Nat) : FiniteOrCofinite (parityStages n).mem :=
  Or.inl (parity_stages_finite n)

theorem finiteOrCofinite_parity_union_excluded : ¬ FiniteOrCofinite (ChainUnion parityChain) := by
  rw [parity_union]
  exact even_not_admitted

theorem finiteOrCofinite_not_chain_closed :
    ¬ FiniteChainClosed (FiniteOrCofinite (A := Nat)) :=
  fun h => finiteOrCofinite_parity_union_excluded (h parityChain finiteOrCofinite_parity_stages)

/-- This chain explicitly depends on the arbitrary target predicate. -/
noncomputable def prefixChain (S : Nat → Prop) : FiniteChain Nat where
  stage := boundedPart S
  increasing := boundedPart_increasing S

theorem prefix_stage_membership (S : Nat → Prop) (n a : Nat) :
    ((prefixChain S).stage n).mem a ↔ S a ∧ a < n := Iff.rfl

theorem prefix_union (S : Nat → Prop) : ChainUnion (prefixChain S) = S := by
  funext a
  exact propext (boundedParts_cover S a)

theorem full_of_finite_chain (C : (Nat → Prop) → Prop)
    (hf : IncludesFinite C) (hc : FiniteChainClosed C) : Full C := by
  intro S
  have h := hc (prefixChain S) (fun n => hf (boundedPart S n))
  rwa [prefix_union] at h

theorem full_iff_finite_chain (C : (Nat → Prop) → Prop) :
    Full C ↔ IncludesFinite C ∧ FiniteChainClosed C := by
  constructor
  · intro h
    exact ⟨fun F => h F.mem, fun T _ => h (ChainUnion T)⟩
  · intro h
    exact full_of_finite_chain C h.1 h.2

theorem chain_iff_full_given_finite (C : (Nat → Prop) → Prop) (hf : IncludesFinite C) :
    FiniteChainClosed C ↔ Full C :=
  ⟨full_of_finite_chain C hf, fun h => (full_iff_finite_chain C).mp h |>.2⟩

theorem chain_iff_directed_given_finite (C : (Nat → Prop) → Prop) (hf : IncludesFinite C) :
    FiniteChainClosed C ↔ DirectedUnionClosed C :=
  (chain_iff_full_given_finite C hf).trans (directed_iff_full_given_finite C hf).symm

end IndexedAssembly
