import PracticalJudgment

/- One history is appraised before its organizational roles are projected.
   G0/J and actual correspondence are philosophical inputs, not Lean axioms.
   `eligible` in the general theorem must already have its full practical warrant.
   No authorization flag, primitive owner or utility sum occurs in the example. -/
namespace RelationalOrganization
open PracticalJudgment

/-- A substantive improvement construction, rather than an assumed required goal,
    supplies the functional requirement on every undefeated eligible continuation. -/
theorem formation_required_of_improvable_absence {H : Type}
    (eligible : H → Prop) (better : H → H → Prop) (formed : H → Prop)
    (menu : List H) (nonempty : menu ≠ [])
    (exactMenu : ∀ a, eligible a ↔ a ∈ menu)
    (irreflexive : ∀ a, ¬ better a a)
    (transitive : ∀ {a b c}, better a b → better b c → better a c)
    (construction : ∀ a, eligible a → ¬ formed a →
      ∃ b, eligible b ∧ better b a) :
    Required (Frontier eligible better) formed := by
  classical
  obtain ⟨a, ha, unbeaten⟩ := finite_frontier better irreflexive
    (fun {_ _ _} hab hbc => transitive hab hbc) menu nonempty
  refine ⟨⟨a, (exactMenu a).mpr ha, ?_⟩, ?_⟩
  · intro b hb
    exact unbeaten b ((exactMenu b).mp hb)
  · intro x hx
    apply Classical.byContradiction
    intro absent
    obtain ⟨y, hy, hbetter⟩ := construction x hx.1 absent
    exact dominated_excluded hy hbetter hx

/- Four continuations of one shared support history. The available amount is six;
   retaining two units is necessary for the continuing basis. Formation spends
   two via either route; overbuilding spends five and breaks the basis.
   The no-formation alternative retains a real free occasion but fails renewal.
   These laws and the interpretation of basic claims are stipulated. -/
inductive Form where
  | idle | left | right | overbuild
  deriving DecidableEq

def spent : Form → Nat
  | .idle => 0
  | .left => 2
  | .right => 2
  | .overbuild => 5

def remaining (f : Form) : Nat := 6 - spent f

def linked : Form → Prop
  | .idle => False
  | _ => True

def basis (f : Form) : Prop := 2 ≤ remaining f

def renewed (f : Form) : Prop := basis f ∧ linked f

/-- The two indices describe actual contents of this history, not two owners. -/
def protect (f : Form) (c : Bool) : Prop :=
  if c then renewed f else basis f

def freeOccasion (f : Form) (_ : Unit) : Prop := spent f = 0

def better : Form → Form → Prop := Better protect freeOccasion

def eligible (f : Form) : Prop := spent f ≤ 6

def formed (f : Form) : Prop := linked f ∧ basis f

def menu : List Form := [.idle, .left, .right, .overbuild]

def usesLeft (f : Form) : Prop := f = .left

def usesRight (f : Form) : Prop := f = .right

theorem left_formation_retains_basis :
    remaining .left = 4 ∧ basis .left ∧ renewed .left := by
  change 4 = 4 ∧ (2 ≤ 4) ∧ ((2 ≤ 4) ∧ True)
  decide

theorem formation_has_a_real_loss :
    freeOccasion .idle () ∧ ¬ freeOccasion .left () := by
  change (0 = 0) ∧ ¬ (2 = 0)
  decide

theorem left_better_than_idle : better .left .idle := by
  apply protection_anchor (c := true)
  · intro c h
    cases c <;> simp_all [protect, renewed, basis, remaining, spent, linked]
  · change (2 ≤ 4) ∧ True
    decide
  · change ¬ ((2 ≤ 6) ∧ False)
    decide

theorem left_better_than_overbuild : better .left .overbuild := by
  apply protection_anchor (c := false)
  · intro c h
    cases c <;> simp_all [protect, renewed, basis, remaining, spent, linked]
  · change 2 ≤ 4
    decide
  · change ¬ (2 ≤ 1)
    decide

theorem every_unformed_continuation_has_a_better_one :
    ∀ a, eligible a → ¬ formed a → ∃ b, eligible b ∧ better b a := by
  intro a _ hn
  cases a with
  | idle => exact ⟨.left, by change 2 ≤ 6; decide, left_better_than_idle⟩
  | left => exact False.elim (hn ⟨True.intro, by change 2 ≤ 4; decide⟩)
  | right => exact False.elim (hn ⟨True.intro, by change 2 ≤ 4; decide⟩)
  | overbuild => exact ⟨.left, by change 2 ≤ 6; decide, left_better_than_overbuild⟩

theorem coordination_is_required : Required (Frontier eligible better) formed := by
  apply formation_required_of_improvable_absence eligible better formed menu
  · simp [menu]
  · intro a
    cases a <;> simp [eligible, spent, menu]
  · exact better_irrefl protect freeOccasion
  · exact better_trans protect freeOccasion
  · exact every_unformed_continuation_has_a_better_one

theorem frontier_exactly_the_two_working_routes (a : Form) :
    Frontier eligible better a ↔ a = .left ∨ a = .right := by
  constructor
  · intro h
    cases a with
    | idle => exact False.elim (h.2 .left (by change 2 ≤ 6; decide) left_better_than_idle)
    | left => exact Or.inl rfl
    | right => exact Or.inr rfl
    | overbuild => exact False.elim (h.2 .left (by change 2 ≤ 6; decide) left_better_than_overbuild)
  · intro h
    rcases h with h | h <;> subst a
    all_goals
      constructor
      · change 2 ≤ 6
        decide
      · intro b _
        cases b <;> simp [better, Better, StrictIncluded, Included, protect,
          freeOccasion, basis, renewed, remaining, spent, linked]

theorem neither_named_route_is_required :
    ¬ Required (Frontier eligible better) usesLeft ∧
    ¬ Required (Frontier eligible better) usesRight := by
  constructor
  · exact alternative_defeats_specific_duty
      ((frontier_exactly_the_two_working_routes .right).mpr (Or.inr rfl))
      (by simp [usesLeft])
  · exact alternative_defeats_specific_duty
      ((frontier_exactly_the_two_working_routes .left).mpr (Or.inl rfl))
      (by simp [usesRight])

theorem more_construction_can_defeat_its_own_basis :
    spent .left < spent .overbuild ∧ linked .overbuild ∧
    ¬ basis .overbuild ∧ ¬ Frontier eligible better .overbuild := by
  refine ⟨by change 2 < 5; decide, True.intro, by change ¬ (2 ≤ 1); decide, ?_⟩
  exact dominated_excluded (by change 2 ≤ 6; decide : eligible .left) left_better_than_overbuild

/-- The report is produced by whether a connection was constructed. Its omission
    is identifiable, not an independently toggled normatively relevant Boolean. -/
def constructionReport : Form → Bool
  | .idle => false
  | _ => true

theorem same_construction_report_different_living_basis :
    constructionReport .left = constructionReport .overbuild ∧
    basis .left ∧ ¬ basis .overbuild := by
  change true = true ∧ (2 ≤ 4) ∧ ¬ (2 ≤ 1)
  decide

theorem no_construction_report_only_basis_judge :
    ¬ ∃ judge : Bool → Prop, ∀ f, judge (constructionReport f) ↔ basis f := by
  rintro ⟨judge, correct⟩
  have positive : judge true := (correct .left).mpr (by change 2 ≤ 4; decide)
  have negative : ¬ judge true := fun h =>
    (by change ¬ (2 ≤ 1); decide : ¬ basis .overbuild) ((correct .overbuild).mp h)
  exact negative positive

/-- Once the retained amount is obtained faithfully, the local omitted relation
    is recovered. This identity is an audit of the supplied meaning, not a new
    theory of how a previously unfamiliar form acquires basic significance. -/
def repairedBasisJudgment (amount : Nat) : Prop := 2 ≤ amount

theorem amount_sensitive_repair_recovers_the_local_basis (f : Form) :
    repairedBasisJudgment (remaining f) ↔ basis f := Iff.rfl

end RelationalOrganization
