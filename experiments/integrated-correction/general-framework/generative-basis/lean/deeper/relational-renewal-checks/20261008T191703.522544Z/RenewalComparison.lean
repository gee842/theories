import GenerativeComparison
import RelationalRenewal

/-!
# What the comparison principle decides once generation is read relationally

`GenerativeComparison` keeps G0 (positive relevance of realized generation) and C (a
fully covered no-loss generative extension warrants strict comparison) as separate,
visible premises, and leaves open which realizations its inventory lists as grounds.
`RelationalRenewal` separates renewing from consuming formation without any premise.
This module connects the two. It adds no premise and no axiom: G0 and C occur only as
hypotheses or as definitions imported from `GenerativeComparison`.

Claims are formation events `(formation, step)` within continuations of one unfolding.
The broad reading lists every active formation event as a ground, including those of
formations that consume conditions of the relations they participate in. The
relational reading lists the active events of formations that are not consuming in
that continuation. A formation that loses its support to another's consumption is not
consuming, so its events before the loss remain grounds. Consumption appears, as
`GenerativeComparison` requires of adverse effects, as the loss of other formations'
grounds. The classification of a formation is over the whole continuation, not step
by step: events of a consuming formation before its drawing exceeds renewal are not
grounds in this reading. A finer, stepwise reading is not settled here.

Results. Under the relational reading, G0 credits exactly the active events of
non-consuming formations. For a malignant formation compared with the same unfolding
without it, the relational reading makes the continuation without it a generative
extension, so C ranks it strictly better, and an asymmetric comparison cannot prefer
the malignant course. The broad reading makes the two incomparable by extension, and a
strict comparison that satisfies C can then prefer the malignant course. For a
formation that wins by consuming the other side's condition, compared with the same
formation within renewal, both readings make sharing a generative extension, because
the winner's own events are identical in both continuations; only the relational
reading withholds G0's credit from the winner's events where it consumes.

These comparisons use C, not G0: as in `GenerativeComparison`, there is no unused G0
parameter disguising a derivation of C. The defense of C as an articulation of the
whole direction of generation, and of the relational reading as the content of G0's
"generation", are philosophical arguments outside this audit. Mixed cases, where each
continuation realizes grounds the other lacks, are not decided by C here.
-/

namespace RenewalComparison

open GenerativeComparison RelationalRenewal RelationalRenewal.Law

variable {W F C : Type}

/-- Broad reading: every active formation event is a ground. -/
def broadInventory (U : W → Unfolding F C) : Inventory W (F × Nat) where
  realized w e := (U w).active e.2 e.1
  generative _ := True

/-- Relational reading: the active events of formations not consuming, in that
continuation, conditions of the relations they participate in. -/
def relationalInventory (U : W → Unfolding F C) : Inventory W (F × Nat) where
  realized w e := (U w).active e.2 e.1 ∧ ¬ ConsumingIn (U w) e.1
  generative _ := True

theorem consumer_events_not_grounds (U : W → Unfolding F C) {w : W} {f : F}
    (consuming : ConsumingIn (U w) f) (t : Nat) :
    ¬ (relationalInventory U).realized w (f, t) :=
  fun ground => ground.2 consuming

/-- Under the relational reading, G0 says exactly that the active events of
non-consuming formations are positively relevant. It says nothing about consumers'
events; this is silence, not a negative verdict. -/
theorem g0_relational (U : W → Unfolding F C) (PositiveRelevant : W → F × Nat → Prop) :
    G0 (relationalInventory U) PositiveRelevant ↔
      ∀ w f t, (U w).active t f → ¬ ConsumingIn (U w) f → PositiveRelevant w (f, t) :=
  ⟨fun g0 w f t active notConsuming => g0 w (f, t) trivial ⟨active, notConsuming⟩,
    fun h w e _ ground => h w e.1 e.2 ground.1 ground.2⟩

/-! ## The same unfolding without the focal formation -/

/-- The condition under the sustaining formation's renewal alone. -/
def undisturbed (L : Law) : Nat → Nat
  | 0 => L.start
  | t + 1 => if L.needG ≤ undisturbed L t then undisturbed L t + L.renew else undisturbed L t

theorem undisturbed_sustains (L : Law) (gStart : L.needG ≤ L.start) :
    ∀ t, L.start ≤ undisturbed L t
  | 0 => Nat.le_refl _
  | t + 1 => by
    have ih := undisturbed_sustains L gStart t
    show L.start ≤ (if L.needG ≤ undisturbed L t then undisturbed L t + L.renew
      else undisturbed L t)
    rw [if_pos (Nat.le_trans gStart ih)]
    exact Nat.le_trans ih (Nat.le_add_right _ _)

/-- The law's unfolding in which the focal formation does not occur and draws nothing. -/
def absent (L : Law) : Unfolding Part Unit where
  level t _ := undisturbed L t
  active t p := match p with
    | .focal => False
    | .sustaining => L.needG ≤ undisturbed L t
  requires p _ := L.requiresPart p
  need p _ := L.need p
  draws _ _ := False

theorem absent_dependent (L : Law) : Dependent (absent L) := by
  intro t p active c _
  cases p with
  | focal => exact False.elim active
  | sustaining => exact active

theorem absent_not_consuming (L : Law) (p : Part) : ¬ ConsumingIn (absent L) p :=
  fun ⟨_, draws, _⟩ => draws

/-! ## Malignant growth compared with its absence -/

inductive Growth where
  | occurs
  | absent

def tumor : Growth → Unfolding Part Unit
  | .occurs => malignant.unfolding
  | .absent => absent malignant

theorem malignant_consumes :
    ConsumingIn malignant.unfolding .focal ∧
      ∃ T, ∀ t, T ≤ t → ¬ malignant.unfolding.active t .sustaining :=
  overdraw_consuming malignant (Nat.succ_pos 1) (Nat.le_succ 1) (T0 := 0)
    (fun _ _ => Nat.lt_succ_of_le (Nat.le_succ 1))

theorem absent_malignant_sustains (t : Nat) :
    (relationalInventory tumor).realized .absent (.sustaining, t) :=
  ⟨Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 2))
      (undisturbed_sustains malignant (Nat.le_succ_of_le (Nat.le_succ 2)) t),
    absent_not_consuming malignant .sustaining⟩

/-- Relationally, the course without the malignant formation keeps every ground of the
course with it and adds the sustaining formation's continuation after the loss. -/
theorem tumor_relational_extension :
    GenerativeExtension (relationalInventory tumor) .occurs .absent := by
  obtain ⟨consuming, T, lost⟩ := malignant_consumes
  refine ⟨?_, (.sustaining, T), trivial, absent_malignant_sustains T,
    fun ground => lost T (Nat.le_refl T) ground.1⟩
  intro e ground
  match e, ground with
  | (.focal, _), ⟨_, notConsuming⟩ => exact absurd consuming notConsuming
  | (.sustaining, t), _ => exact absent_malignant_sustains t

/-- Read event by event, neither course extends the other: the malignant formation's
events are grounds the course without it lacks. -/
theorem tumor_broad_incomparable :
    ¬ Extends (broadInventory tumor) .occurs .absent ∧
      ¬ Extends (broadInventory tumor) .absent .occurs := by
  obtain ⟨_, T, lost⟩ := malignant_consumes
  refine ⟨fun covers => ?_, fun covers => ?_⟩
  · have formsFirst : (broadInventory tumor).realized .occurs (.focal, 0) :=
      show 1 ≤ 4 from Nat.le_succ_of_le (Nat.le_succ_of_le (Nat.le_succ 1))
    exact covers (.focal, 0) formsFirst
  · exact lost T (Nat.le_refl T) (covers (.sustaining, T) (absent_malignant_sustains T).1)

/-- With the relational reading, C ranks the course without the malignant formation
strictly above the course with it; an asymmetric comparison cannot prefer the latter. -/
theorem relational_comparison_ranks (Better : Growth → Growth → Prop)
    (comparison : ComparisonPrinciple (relationalInventory tumor) Better) :
    Better .occurs .absent ∧
      ((∀ a b, Better a b → ¬ Better b a) → ¬ Better .absent .occurs) := by
  have ranked := comparison _ _ tumor_relational_extension
  exact ⟨ranked, fun asymmetric preferred => asymmetric _ _ ranked preferred⟩

/-- A strict comparison preferring the malignant course, alongside every generative
extension of the broad reading. -/
def preferMalignant (first second : Growth) : Prop :=
  GenerativeExtension (broadInventory tumor) first second ∨
    (first = .absent ∧ second = .occurs)

theorem preferMalignant_only {a b : Growth} (better : preferMalignant a b) :
    a = .absent ∧ b = .occurs := by
  cases better with
  | inr pair => exact pair
  | inl ext =>
    obtain ⟨covers, _, _, realized, notRealized⟩ := ext
    cases a with
    | occurs =>
      cases b with
      | occurs => exact absurd realized notRealized
      | absent => exact absurd covers tumor_broad_incomparable.1
    | absent =>
      cases b with
      | occurs => exact absurd covers tumor_broad_incomparable.2
      | absent => exact absurd realized notRealized

/-- With the broad reading, C does not decide: an irreflexive, transitive comparison
satisfying C prefers the malignant course. -/
theorem broad_comparison_admits_malignant :
    ComparisonPrinciple (broadInventory tumor) preferMalignant ∧
      preferMalignant .absent .occurs ∧ ¬ preferMalignant .occurs .absent ∧
      (∀ a, ¬ preferMalignant a a) ∧
      (∀ a b c, preferMalignant a b → preferMalignant b c → preferMalignant a c) := by
  refine ⟨fun _ _ ext => Or.inl ext, Or.inr ⟨rfl, rfl⟩, ?_, ?_, ?_⟩
  · intro better
    exact Growth.noConfusion (preferMalignant_only better).1
  · intro a better
    have pair := preferMalignant_only better
    exact Growth.noConfusion (pair.1.symm.trans pair.2)
  · intro a b c first second
    exact Growth.noConfusion ((preferMalignant_only first).2.symm.trans
      (preferMalignant_only second).1)

/-! ## Winning by consumption compared with sharing -/

inductive Contest where
  | shares
  | wins

def contest : Contest → Unfolding Part Unit
  | .shares => sharing.unfolding
  | .wins => winning.unfolding

theorem sharing_grounds (e : Part × Nat) : (relationalInventory contest).realized .shares e := by
  have share := within_renewal_renewing sharing (fun _ => Nat.le_refl 1)
    (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
  have kept := within_renewal_sustains sharing (fun _ => Nat.le_refl 1)
    (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
  match e with
  | (.focal, t) => exact ⟨share.2.1 t, renewing_not_consuming share.1⟩
  | (.sustaining, t) =>
    exact ⟨Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t),
      fun ⟨_, draws, _⟩ => draws⟩

theorem winning_persists :
    (∀ t, winning.unfolding.active t .focal) ∧ (∀ t, winning.formed t = t) ∧
      ConsumingIn winning.unfolding .focal :=
  independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
    (fun _ _ => Nat.lt_succ_self 1)

/-- Both readings make sharing a generative extension of winning by consumption: the
winner's own events are the same in both continuations, and the other side continues
only in sharing. Under the broad reading every winning event is still a G0 ground;
under the relational reading none is. -/
theorem contest_comparison :
    GenerativeExtension (relationalInventory contest) .wins .shares ∧
      GenerativeExtension (broadInventory contest) .wins .shares ∧
      (∀ t, (broadInventory contest).realized .wins (.focal, t)) ∧
      (∀ t, ¬ (relationalInventory contest).realized .wins (.focal, t)) := by
  obtain ⟨_, T, lost⟩ := overdraw_consuming winning (Nat.succ_pos 0) (Nat.zero_le 1)
    (T0 := 0) (fun _ _ => Nat.lt_succ_self 1)
  have win := winning_persists
  exact ⟨⟨fun e _ => sharing_grounds e, (.sustaining, T), trivial, sharing_grounds _,
      fun ground => lost T (Nat.le_refl T) ground.1⟩,
    ⟨fun e _ => (sharing_grounds e).1, (.sustaining, T), trivial, (sharing_grounds _).1,
      lost T (Nat.le_refl T)⟩,
    win.1, fun t => consumer_events_not_grounds contest (w := .wins) win.2.2 t⟩

end RenewalComparison
