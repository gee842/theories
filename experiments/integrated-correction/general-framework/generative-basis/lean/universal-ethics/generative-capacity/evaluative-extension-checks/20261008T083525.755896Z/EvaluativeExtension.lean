import ConcernExtension

/- Extension of a situated evaluative description, not the discovery or proof of
new ethical axioms. Old and added indices are analytical distinctions within the
same continuation. Actual relevance, protected status and feasible alternatives
require the explicit G0/J correspondence argument accompanying this module. -/
namespace EvaluativeExtension
open PracticalJudgment

open ConcernExtension

/-- Sufficient transport when no newly represented protection or secondary gain
of b is lost by a. This is not the assertion that every extension meets that test. -/
theorem better_survives_no_new_loss {H C N G K : Type}
    (p : H → C → Prop) (q : H → N → Prop)
    (g : H → G → Prop) (k : H → K → Prop) (a b : H)
    (old : Better p g a b) (addedProtection : Included (q b) (q a))
    (secondary : Included (k b) (k a)) :
    Better (extend p q) (extend g k) a b := by
  classical
  rcases old with old | old
  · exact Or.inl ((strict_extension_transfer_iff p q b a old).2 addedProtection)
  · have forward := (included_extension_iff p q b a).2 ⟨old.1,addedProtection⟩
    by_cases reverse : Included (q a) (q b)
    · exact Or.inr ⟨forward, (included_extension_iff p q a b).2 ⟨old.2.1,reverse⟩,
        (strict_extension_transfer_iff g k b a old.2.2).2 secondary⟩
    · exact Or.inl ⟨forward, fun h => reverse ((included_extension_iff p q a b).1 h).2⟩

/-- Equal additional profiles preserve the exact old comparison, in both directions. -/
theorem equal_additions_preserve_exact_comparison {H C N G K : Type}
    (p : H → C → Prop) (q : H → N → Prop)
    (g : H → G → Prop) (k : H → K → Prop) (a b : H)
    (qab : Included (q a) (q b)) (qba : Included (q b) (q a))
    (kab : Included (k a) (k b)) (kba : Included (k b) (k a)) :
    Better (extend p q) (extend g k) a b ↔ Better p g a b := by
  constructor
  · intro h
    rcases h with h | h
    · refine Or.inl ⟨((included_extension_iff p q b a).1 h.1).1, ?_⟩
      intro reverse
      exact h.2 ((included_extension_iff p q a b).2 ⟨reverse,qab⟩)
    · refine Or.inr ⟨((included_extension_iff p q b a).1 h.1).1,
        ((included_extension_iff p q a b).1 h.2.1).1,
        ((included_extension_iff g k b a).1 h.2.2.1).1, ?_⟩
      intro reverse
      exact h.2.2.2 ((included_extension_iff g k a b).2 ⟨reverse,kab⟩)
  · intro h
    exact better_survives_no_new_loss p q g k a b h qba kba

theorem new_protection_loss_defeats_old_verdict {H C N G : Type}
    (p : H → C → Prop) (q : H → N → Prop) (g : H → G → Prop)
    (a b : H) (n : N) (held : q b n) (lost : ¬ q a n) :
    ¬ Better (extend p q) g a b :=
  no_protection_trade_by_count (.inr n) held lost

inductive Plan where
  | output | maintain
  deriving DecidableEq

inductive Stage where
  | prior | formed
  deriving DecidableEq

/-- The developed activity creates a represented support need. Its classification
as a basic claim and the legitimacy of its formation are separate questions. -/
def need : Stage → Nat
  | .prior => 0
  | .formed => 1

def supply : Plan → Nat
  | .output => 0
  | .maintain => 1

def oldProtection (_ : Plan) (_ : Unit) : Prop := True
def outputCount : Plan → Nat
  | .output => 2
  | .maintain => 1
def oldGain (p : Plan) (i : Nat) : Prop := i < outputCount p
def formedProtection (t : Stage) (p : Plan) (_ : Unit) : Prop := need t ≤ supply p
def protection (t : Stage) := extend oldProtection (formedProtection t)
def comparison (t : Stage) := Better (protection t) oldGain

theorem prior_output_favored : comparison .prior .output .maintain := by
  apply Or.inr
  refine ⟨?_,?_,?_,?_⟩
  · intro i h; cases i <;> simp [protection, extend, oldProtection, formedProtection, need, supply]
  · intro i h; cases i <;> simp [protection, extend, oldProtection, formedProtection, need, supply]
  · intro i hi; simp only [oldGain,outputCount] at *; omega
  · intro h
    have bad := h 1 (by simp [oldGain,outputCount])
    simp [oldGain,outputCount] at bad

theorem formation_creates_a_differentiating_need :
    formedProtection .prior .output () ∧ formedProtection .prior .maintain () ∧
    ¬ formedProtection .formed .output () ∧ formedProtection .formed .maintain () := by simp [formedProtection,need,supply]

theorem formed_maintenance_favored : comparison .formed .maintain .output := by
  apply protection_anchor (c := Sum.inr ())
  · intro i h
    cases i <;> simp_all [protection, extend, oldProtection, formedProtection, need, supply]
  · simp [protection,extend,formedProtection,need,supply]
  · simp [protection,extend,formedProtection,need,supply]

theorem formed_output_no_longer_favored : ¬ comparison .formed .output .maintain :=
  new_protection_loss_defeats_old_verdict oldProtection (formedProtection .formed)
    oldGain .output .maintain () (by simp [formedProtection,need,supply]) (by simp [formedProtection,need,supply])

theorem reversal_keeps_real_output_loss :
    oldGain .output 1 ∧ ¬ oldGain .maintain 1 ∧
    comparison .formed .maintain .output := by
  exact ⟨by simp [oldGain,outputCount], by simp [oldGain,outputCount], formed_maintenance_favored⟩

theorem no_unrestricted_preservation_of_verdicts :
    ¬ (∀ a b, comparison .prior a b → comparison .formed a b) := by
  intro preserve
  exact formed_output_no_longer_favored (preserve _ _ prior_output_favored)

/-- Only a stage-insensitive exact ranking is excluded; a fixed rule on an
adequate changing description remains possible and is the rule used here. -/
theorem no_one_stage_blind_exact_ranking :
    ¬ ∃ rank : Plan → Plan → Prop,
      (∀ a b, rank a b ↔ comparison .prior a b) ∧
      (∀ a b, rank a b ↔ comparison .formed a b) := by
  rintro ⟨rank,old,new⟩
  exact formed_output_no_longer_favored ((new _ _).1 ((old _ _).2 prior_output_favored))

theorem one_unchanged_rule_handles_both_stages :
    Better (protection .prior) oldGain .output .maintain ∧
    Better (protection .formed) oldGain .maintain .output :=
  ⟨prior_output_favored,formed_maintenance_favored⟩

/-- A different new secondary realization can defeat a former strict comparison
without producing its reverse. Incomparability is retained. -/
def addedGain (p : Plan) (_ : Unit) : Prop := p = .maintain

theorem added_secondary_gain_can_leave_incomparability :
    ¬ Better oldProtection (extend oldGain addedGain) .output .maintain ∧
    ¬ Better oldProtection (extend oldGain addedGain) .maintain .output := by
  constructor
  · intro h
    rcases h with h | h
    · exact h.2 (fun _ _ => True.intro)
    · have bad := h.2.2.1 (.inr ()) rfl
      cases bad
  · intro h
    rcases h with h | h
    · exact h.2 (fun _ _ => True.intro)
    · have bad := h.2.2.1 (.inl 1) (by simp [extend,oldGain,outputCount])
      simp [extend,oldGain,outputCount] at bad


/-- Common comparison and common undefeatedness have different quantifier order.
The live applications share the explicit comparator; their admission is not
certified by quantification over an analyst's supplied family. -/
def CommonBetter {W H C G : Type} (live : W → Prop)
    (p : W → H → C → Prop) (g : W → H → G → Prop) (a b : H) : Prop :=
  ∀ w, live w → Better (p w) (g w) a b

def EveryApplicationDefeats {W H C G : Type} (live : W → Prop)
    (menu : H → Prop) (p : W → H → C → Prop) (g : W → H → G → Prop)
    (a : H) : Prop := ∀ w, live w → ∃ b, menu b ∧ Better (p w) (g w) b a

theorem common_defeat_implies_each_defeat {W H C G : Type}
    (live : W → Prop) (menu : H → Prop)
    (p : W → H → C → Prop) (g : W → H → G → Prop) (a b : H)
    (hb : menu b) (h : CommonBetter live p g b a) :
    EveryApplicationDefeats live menu p g a :=
  fun w hw => ⟨b,hb,h w hw⟩

theorem each_defeat_excludes_actual_frontier {W H C G : Type}
    (live : W → Prop) (menu : H → Prop)
    (p : W → H → C → Prop) (g : W → H → G → Prop) (a : H) (actual : W)
    (covered : live actual) (h : EveryApplicationDefeats live menu p g a) :
    ¬ Frontier menu (Better (p actual) (g actual)) a := by
  obtain ⟨b,hb,hba⟩ := h actual covered
  exact dominated_excluded hb hba

theorem one_application_blocks_uniform_undefeatedness {W H C G : Type}
    (live : W → Prop) (menu : H → Prop)
    (p : W → H → C → Prop) (g : W → H → G → Prop) (a b : H) (w : W)
    (hw : live w) (hb : menu b) (h : Better (p w) (g w) b a) :
    ¬ Robust live (fun v => Frontier menu (Better (p v) (g v))) a :=
  fun uniform => dominated_excluded hb h (uniform w hw)

theorem uniformly_undefeated_is_common_frontier {W H C G : Type}
    (live : W → Prop) (menu : H → Prop)
    (p : W → H → C → Prop) (g : W → H → G → Prop) (a : H)
    (inhabited : ∃ w, live w)
    (h : Robust live (fun w => Frontier menu (Better (p w) (g w))) a) :
    Frontier menu (CommonBetter live p g) a := by
  obtain ⟨w,hw⟩ := inhabited
  exact ⟨(h w hw).1, fun b hb common => (h w hw).2 b hb (common w hw)⟩

inductive Response where
  | left | right | skip
  deriving DecidableEq

/-- Competing warranted applications must be justified outside this model.
Here the unresolved issue is which of two actual support routes protects a
newly recognized condition. Omission protects neither. -/
def routeProtection (w : Bool) (a : Response) (_ : Unit) : Prop :=
  (w = false ∧ a = .left) ∨ (w = true ∧ a = .right)
def routeGain (_ : Bool) (_ : Response) (_ : Unit) : Prop := False

theorem route_comparison_iff (w : Bool) (a b : Response) :
    Better (routeProtection w) (routeGain w) a b ↔
      routeProtection w a () ∧ ¬ routeProtection w b () := by
  classical
  constructor
  · intro h
    rcases h with h | h
    · constructor
      · by_cases ha : routeProtection w a ()
        · exact ha
        · exact False.elim (h.2 (fun _ hx => False.elim (ha hx)))
      · intro hb
        exact h.2 (fun _ _ => hb)
    · exact False.elim (h.2.2.2 (fun _ hx => hx))
  · rintro ⟨ha,hb⟩
    exact protection_anchor (fun _ hx => False.elim (hb hx)) () ha hb

theorem omission_defeated_in_every_application :
    EveryApplicationDefeats (fun _ : Bool => True) (fun _ : Response => True)
      routeProtection routeGain .skip := by
  intro w hw
  cases w with
  | false => exact ⟨.left,True.intro,(route_comparison_iff _ _ _).2 (by simp [routeProtection])⟩
  | true => exact ⟨.right,True.intro,(route_comparison_iff _ _ _).2 (by simp [routeProtection])⟩

theorem omission_survives_common_comparison :
    Frontier (fun _ : Response => True)
      (CommonBetter (fun _ : Bool => True) routeProtection routeGain) .skip := by
  refine ⟨True.intro, ?_⟩
  intro b hb common
  cases b with
  | left =>
    have h := ((route_comparison_iff true .left .skip).1 (common true True.intro)).1
    simp [routeProtection] at h
  | right =>
    have h := ((route_comparison_iff false .right .skip).1 (common false True.intro)).1
    simp [routeProtection] at h
  | skip => exact better_irrefl _ _ _ (common false True.intro)

theorem no_uniformly_undefeated_response :
    ¬ ∃ a : Response, Robust (fun _ : Bool => True)
      (fun w => Frontier (fun _ : Response => True) (Better (routeProtection w) (routeGain w))) a := by
  rintro ⟨a,h⟩
  cases a with
  | left =>
    exact (h true True.intro).2 .right True.intro
      ((route_comparison_iff _ _ _).2 (by simp [routeProtection]))
  | right =>
    exact (h false True.intro).2 .left True.intro
      ((route_comparison_iff _ _ _).2 (by simp [routeProtection]))
  | skip =>
    exact (h false True.intro).2 .left True.intro
      ((route_comparison_iff _ _ _).2 (by simp [routeProtection]))

end EvaluativeExtension
