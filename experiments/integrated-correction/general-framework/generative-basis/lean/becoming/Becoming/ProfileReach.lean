import Becoming.EdgeClosure
import Becoming.Metaethics
import Becoming.ValuationFrames

/-!
# How a standpoint's own good reaches beyond its own region, through formed profiles

One unfolding. An evaluating position is a formation within it, not a primitive owner.
Occurrences `Gen` of living and further generation carry profiles `Prof`, their formed relations
to this evaluating (organizational continuity, formative contribution, dependence ...). "Own" is
a region of those relations, not a primitive index. `sig` is this standpoint's reason-giving
significance, with no valence: contributory, not weight, permission or duty.

Supplied, and kept visible: S0 (`SelfGood`), the standpoint's own living and further generation
is reason-giving for it; `Monotone`, an occurrence at least as connected in the grounding
relations is at least as significant; `Supervenes`, significance of living content depends only
on the profile; `Tolerant`, an indiscernibly small step between profiles does not turn positive
significance into none. S0 and tolerance are the substantive premises; no theorem here proves
them.

* **Step one, no tolerance.** S0 with monotonicity gives significance to any living occurrence
  at least as connected as an own valued one (`self_good_reaches_at_least_as_connected`), so a
  standpoint that values only its own cannot hold both once its own generation is matched by
  another's (`strict_indexed_rival_inconsistent`).
* **Step two is N_rel on profiles.** A standpoint is the core's `Valuation` on its profiles
  (`valuation`); tolerance is relational neutrality there (`tolerant_iff_neutral`), S0 under
  supervenience is S0 there (`selfGood_valuation`), and chains of small steps are reach along
  the edges (`Reach (edgeProcess step)`, `reach_relations_iff`). So every reachable living
  occurrence linked to an own one has significance by the core's `Valuation.reaches`
  (`tolerant_chain_reaches`), and this is living significance on the frame of the reachable
  occurrences (`reach_is_g0`, `self_good_derives_reachable_g0`).
* **Boundaries, in one finite unfolding.** A threshold rival is consistent without tolerance
  (`threshold_rival_is_consistent_without_tolerance`); with tolerance the reach includes the
  stranger (`tolerant_standpoint_reaches_stranger`); a present-aim evaluator without S0 escapes
  (`present_aim_evaluator_escapes`); a closed self, whose small steps never cross, blocks reach
  (`closed_self_blocks_reach`); a self-good grounded in persistence alone escapes step one
  (`persistence_rival_escapes_self_transcendence`).

Ported from `EvaluatorGrounding`, with the bridge's profile valuation (`profileValuation`,
`tolerant_iff_neutral`, `chain_iff_reach_profiles`, `selfGood_profiles`,
`tolerant_chain_reaches_by_core`) and the join `SeedReachProcesses.reachable_living_significance`
(F3J, 18 October 2026). The periphery's `Chain` is reach along the edges (`Reach (edgeProcess
step)`), its `Inventory` the frame with no moves realizing the reachable occurrences. Its `simp`
and `omega` proofs are constructive here. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

namespace ProfileReach

/-- A standpoint within the unfolding: each occurrence's profile, the own region, the living
occurrences, the reachable ones, and this standpoint's significance. -/
structure Standpoint (Gen Prof : Type) where
  prof : Gen → Prof
  own : Gen → Prop
  living : Gen → Prop
  reach : Gen → Prop
  sig : Gen → Prop

variable {Gen Prof : Type}

/-- S0 at the standpoint. -/
def SelfGood (s : Standpoint Gen Prof) : Prop :=
  ∀ g, s.own g → s.living g → s.sig g

def Monotone (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop) : Prop :=
  ∀ g g', s.living g → s.living g' → atLeast (s.prof g) (s.prof g') → s.sig g → s.sig g'

def Supervenes (s : Standpoint Gen Prof) (val : Prof → Prop) : Prop :=
  ∀ g, s.living g → (s.sig g ↔ val (s.prof g))

def Tolerant (val : Prof → Prop) (step : Prof → Prof → Prop) : Prop :=
  ∀ p q, step p q → val p → val q

/-- **Self-transcendence**: S0 with monotonicity gives significance to any living occurrence at
least as connected as an own valued one. No tolerance is used. -/
theorem self_good_reaches_at_least_as_connected (s : Standpoint Gen Prof)
    (atLeast : Prof → Prof → Prop) (self : SelfGood s) (mono : Monotone s atLeast) {g g' : Gen}
    (ownG : s.own g) (livingG : s.living g) (livingG' : s.living g')
    (connected : atLeast (s.prof g) (s.prof g')) : s.sig g' :=
  mono g g' livingG livingG' connected (self g ownG livingG)

/-- **The strictly indexed rival is inconsistent** with S0 and monotonicity once another living
occurrence is at least as connected as one of its own. -/
theorem strict_indexed_rival_inconsistent (s : Standpoint Gen Prof)
    (atLeast : Prof → Prof → Prop) (self : SelfGood s) (mono : Monotone s atLeast)
    (onlyOwn : ∀ g, s.sig g → s.own g)
    (differentiates : ∃ g g', s.own g ∧ s.living g ∧ s.living g' ∧ ¬ s.own g' ∧
      atLeast (s.prof g) (s.prof g')) : False :=
  match differentiates with
  | ⟨_, g', ownG, livingG, livingG', other, connected⟩ =>
    other (onlyOwn g'
      (self_good_reaches_at_least_as_connected s atLeast self mono ownG livingG livingG' connected))

/-- **Tolerance carries a value along chains of small steps.** -/
theorem chain_preserves (val : Prof → Prop) (step : Prof → Prof → Prop) (tol : Tolerant val step)
    {p q : Prof} (chain : Reach (edgeProcess step) p q) (start : val p) : val q :=
  Invariant.reach (fun x _ y e held => tol x y e held) chain start

/-! ## Step two is relational neutrality on profiles -/

/-- **A standpoint's valuation of its profiles.** The claims are the profiles, each counted
living; a profile is related to those one small step from it, is the standpoint's own where an
own living occurrence has it, and is significant where `val` holds of it. -/
def valuation (s : Standpoint Gen Prof) (val : Prof → Prop) (step : Prof → Prof → Prop) :
    Valuation Unit Prof :=
  ⟨fun _ => True, step, fun _ q => ∃ g, s.own g ∧ s.living g ∧ s.prof g = q, fun _ q => val q⟩

/-- **Tolerance is N_rel on profiles.** -/
theorem tolerant_iff_neutral {s : Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} : Tolerant val step ↔ Neutral (valuation s val step).transmits :=
  ⟨fun tol ⟨_, p, q⟩ held related _ => tol p q related held,
   fun neutral p q related held => neutral ((), p, q) held related True.intro⟩

/-- **Reach along related profiles is reach along the small steps.** -/
theorem reach_relations_iff {s : Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} {p q : Prof} :
    Reach (valuation s val step).relations p q ↔ Reach (edgeProcess step) p q :=
  ⟨fun path => Invariant.reach (P := (valuation s val step).relations) (I := Reach (edgeProcess step) p)
      (fun _ _ _ e r => r.trans (Reach.of_step (a := ()) e.1)) path (Reach.refl _ _),
   fun path => Invariant.reach (P := edgeProcess step) (I := Reach (valuation s val step).relations p)
      (fun _ _ _ e r => r.trans (Reach.of_step (a := ()) ⟨e, True.intro⟩)) path (Reach.refl _ _)⟩

/-- **S0 under supervenience is S0 on profiles.** -/
theorem selfGood_valuation {s : Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} (sup : Supervenes s val) (self : SelfGood s) :
    (valuation s val step).SelfGood () :=
  fun _ ⟨g, own, alive, same⟩ _ => same ▸ (sup g alive).1 (self g own alive)

/-- **Reach**: under supervenience, S0 and tolerance, every reachable living occurrence whose
profile a chain of small steps links to an own living one has significance, by the core's N_rel
carrying significance along related profiles (`Valuation.reaches`). -/
theorem tolerant_chain_reaches (s : Standpoint Gen Prof) (val : Prof → Prop)
    (step : Prof → Prof → Prop) (sup : Supervenes s val) (self : SelfGood s)
    (tol : Tolerant val step)
    (chain : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ Reach (edgeProcess step) (s.prof g) (s.prof g')) :
    ∀ g', s.reach g' → s.living g' → s.sig g' :=
  fun g' reached alive' => match chain g' reached alive' with
  | ⟨g, own, alive, linked⟩ => (sup g' alive').2
      (Valuation.reaches (tolerant_iff_neutral (s := s).mp tol)
        (reach_relations_iff (s := s) (val := val).mpr linked)
        (selfGood_valuation (step := step) sup self (s.prof g) ⟨g, own, alive, rfl⟩ True.intro))

/-- The reachable occurrences of one continuation, as a frame with no moves. -/
def reachableFrame (s : Standpoint Gen Prof) : Frame Unit Unit Gen :=
  ⟨⟨fun _ _ _ => False⟩, fun _ g => s.reach g⟩

/-- **The reached conclusion is living significance** on the frame of the reachable occurrences,
with this standpoint's significance as positive relevance. -/
theorem reach_is_g0 (s : Standpoint Gen Prof) :
    (∀ g', s.reach g' → s.living g' → s.sig g') ↔
      G0 (reachableFrame s) s.living (fun _ g => s.sig g) :=
  ⟨fun reached _ g alive realized => reached g realized alive,
   fun g0 g reached alive => g0 () g alive reached⟩

theorem self_good_derives_reachable_g0 (s : Standpoint Gen Prof) (val : Prof → Prop)
    (step : Prof → Prof → Prop) (sup : Supervenes s val) (self : SelfGood s)
    (tol : Tolerant val step)
    (chain : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ Reach (edgeProcess step) (s.prof g) (s.prof g')) :
    G0 (reachableFrame s) s.living (fun _ g => s.sig g) :=
  (reach_is_g0 s).1 (tolerant_chain_reaches s val step sup self tol chain)

/-! ## A finite unfolding and its boundaries

Degrees of formed connection to this evaluating: `changedSelf` is the evaluator's own transformed
further generation; `formedOther` another life formed through this activity and at least as
connected; `stranger` reachable but weakly connected; `beyond` not reachable. The numbers are
illustrative orderings only. -/

inductive Occ where
  | nearSelf | changedSelf | formedOther | stranger | beyond

def degree : Occ → Nat
  | .nearSelf => 9
  | .changedSelf => 4
  | .formedOther => 5
  | .stranger => 1
  | .beyond => 0

def ownOcc : Occ → Prop
  | .nearSelf => True
  | .changedSelf => True
  | .formedOther => False
  | .stranger => False
  | .beyond => False

def reachOcc : Occ → Prop
  | .nearSelf => True
  | .changedSelf => True
  | .formedOther => True
  | .stranger => True
  | .beyond => False

def adjacent (p q : Nat) : Prop := q + 1 = p ∨ p + 1 = q

def standpoint (val : Nat → Prop) : Standpoint Occ Nat :=
  ⟨degree, ownOcc, fun _ => True, reachOcc, fun g => val (degree g)⟩

/-- **Any monotone self-good standpoint here gives the formed other significance.** -/
theorem formed_other_has_significance (val : Nat → Prop) (self : SelfGood (standpoint val))
    (mono : Monotone (standpoint val) (· ≤ ·)) : (standpoint val).sig .formedOther :=
  self_good_reaches_at_least_as_connected (standpoint val) (· ≤ ·) self mono
    (g := .changedSelf) True.intro True.intro True.intro (show 4 ≤ 5 by decide)

theorem threshold_selfGood : SelfGood (standpoint (4 ≤ ·))
  | .nearSelf, _, _ => (by decide : 4 ≤ 9)
  | .changedSelf, _, _ => Nat.le_refl 4
  | .formedOther, own, _ => nomatch own
  | .stranger, own, _ => nomatch own
  | .beyond, own, _ => nomatch own

/-- **The threshold rival is consistent without tolerance**: S0, monotone and supervenient, it
reaches the formed other, not the stranger, and violates tolerance exactly at its cut. -/
theorem threshold_rival_is_consistent_without_tolerance :
    SelfGood (standpoint (4 ≤ ·)) ∧ Monotone (standpoint (4 ≤ ·)) (· ≤ ·) ∧
    Supervenes (standpoint (4 ≤ ·)) (4 ≤ ·) ∧
    (standpoint (4 ≤ ·)).sig .formedOther ∧ ¬ (standpoint (4 ≤ ·)).sig .stranger ∧
    ¬ Tolerant (4 ≤ ·) adjacent :=
  ⟨threshold_selfGood, fun _ _ _ _ le held => Nat.le_trans held le, fun _ _ => Iff.rfl,
   (by decide : 4 ≤ 5), (by decide : ¬ 4 ≤ 1),
   fun tol => (by decide : ¬ 4 ≤ 3) (tol 4 3 (.inl rfl) (Nat.le_refl 4))⟩

/-- **With tolerance along adjacent degrees, the same S0 reaches the stranger.** The same
premises give `sig .beyond`, since degree 0 is adjacent to 1: the `reach` field limits what this
theorem states, not what tolerance implies. -/
theorem tolerant_standpoint_reaches_stranger (val : Nat → Prop) (self : SelfGood (standpoint val))
    (tol : Tolerant val adjacent) :
    (standpoint val).sig .stranger ∧ (standpoint val).sig .formedOther :=
  have four : val 4 := self .changedSelf True.intro True.intro
  have one : val 1 := tol 2 1 (.inl rfl) (tol 3 2 (.inl rfl) (tol 4 3 (.inl rfl) four))
  ⟨one, tol 4 5 (.inr rfl) four⟩

/-- **A present-aim evaluator escapes**: without S0 it satisfies monotonicity, supervenience and
tolerance and assigns no significance anywhere. Universality over every possible evaluator is
not derived. -/
theorem present_aim_evaluator_escapes :
    ¬ SelfGood (standpoint (fun _ => False)) ∧
    Monotone (standpoint (fun _ => False)) (· ≤ ·) ∧
    Supervenes (standpoint (fun _ => False)) (fun _ => False) ∧
    Tolerant (fun _ => False) adjacent ∧
    ¬ (standpoint (fun _ => False)).sig .formedOther :=
  ⟨fun self => self .nearSelf True.intro True.intro, fun _ _ _ _ _ held => held,
   fun _ _ => Iff.rfl, fun _ _ _ held => held, id⟩

/-- Small steps that never leave the own positive region. -/
def closedStep (p q : Nat) : Prop := 4 ≤ p ∧ 4 ≤ q ∧ adjacent p q

/-- **A closed self blocks reach**: where no small step crosses between own and other, tolerance
holds yet nothing reaches the stranger. Continuity and autopoietic closure are formations of
the one unfolding with exactly this closed structure. -/
theorem closed_self_blocks_reach :
    SelfGood (standpoint (4 ≤ ·)) ∧ Tolerant (4 ≤ ·) closedStep ∧
    ¬ (standpoint (4 ≤ ·)).sig .stranger :=
  ⟨threshold_selfGood, fun _ _ step _ => step.2.1, (by decide : ¬ 4 ≤ 1)⟩

/-! ## Persistence-grounded rival

Profiles of two dimensions: (organizational continuity, formative contribution). The formed
other is more formed by this activity yet less organizationally continuous than the changed
self, so the product order does not make it at least as connected: step one binds a self-good
led by formative contribution, not self-good as such. -/

def profile2 : Occ → Nat × Nat
  | .nearSelf => (9, 9)
  | .changedSelf => (8, 2)
  | .formedOther => (1, 7)
  | .stranger => (0, 1)
  | .beyond => (0, 0)

def productLe (p q : Nat × Nat) : Prop := p.1 ≤ q.1 ∧ p.2 ≤ q.2

def persistence : Standpoint Occ (Nat × Nat) :=
  ⟨profile2, ownOcc, fun _ => True, reachOcc, fun g => 5 ≤ (profile2 g).1⟩

/-- **The persistence rival escapes self-transcendence.** -/
theorem persistence_rival_escapes_self_transcendence :
    SelfGood persistence ∧ Monotone persistence productLe ∧
    ¬ productLe (profile2 .changedSelf) (profile2 .formedOther) ∧
    ¬ persistence.sig .formedOther :=
  ⟨fun g own _ => match g, own with
    | .nearSelf, _ => (by decide : 5 ≤ 9)
    | .changedSelf, _ => (by decide : 5 ≤ 8),
   fun _ _ _ _ le held => Nat.le_trans held le.1,
   fun le => (by decide : ¬ 8 ≤ 1) le.1, (by decide : ¬ 5 ≤ 1)⟩

end ProfileReach

end Becoming
