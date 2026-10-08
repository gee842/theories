import GoalFormationRevision

/-!
Goal-attainment data can omit relations required by the supplied practical
comparison. The same inherited outcome law supports opposed recommendations,
while one fixed relation-sensitive rule remains adequate throughout this family.
This checks a conditional representation requirement, not the warrant of J2,
all-things-considered authority, or a definition of wisdom.
-/

namespace WisdomGoalGrounds
open PracticalJudgment GoalFormationRevision

def achievementProfile (c : Conditions) : Goal → Practice → Nat :=
  fun g p => attainment g (perform c p)

def Acceptable (c : Conditions) (p : Practice) : Prop :=
  Frontier (fun _ => True) (Better (protects c) (gains c)) p

def retentionCase : Conditions := ⟨false, true, false⟩

def fixedRule (c : Conditions) : Practice :=
  if callsForRevision ⟨.attendance, c.accessLoss, c.transitionLoss⟩
  then .learning else .attendance

theorem achievement_profiles_equal (c d : Conditions) :
    achievementProfile c = achievementProfile d := by
  funext g p
  cases g <;> cases p <;> rfl

theorem retaining_goal_preferred (c : Conditions)
    (access : c.accessLoss = false) (loss : c.transitionLoss = true) :
    Better (protects c) (gains c) .attendance .learning := by
  apply protection_anchor (c := true)
  · intro claim h
    cases claim <;> simp_all [protects, perform]
  · simp [protects, perform]
  · simp [protects, perform, loss]

theorem revision_frontier_iff (p : Practice) :
    Acceptable harmful p ↔ p = .learning := by
  constructor
  · intro h
    cases p with
    | attendance => exact False.elim (h.2 .learning trivial (warranted_revision harmful rfl rfl))
    | learning => rfl
  · intro h
    subst p
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | learning => exact better_irrefl _ _ _
    | attendance =>
      apply no_protection_trade_by_count (c := false)
      · simp [protects, perform]
      · simp [protects, perform, harmful]

theorem retention_frontier_iff (p : Practice) :
    Acceptable retentionCase p ↔ p = .attendance := by
  constructor
  · intro h
    cases p with
    | attendance => rfl
    | learning => exact False.elim (h.2 .attendance trivial (retaining_goal_preferred retentionCase rfl rfl))
  · intro h
    subst p
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | attendance => exact better_irrefl _ _ _
    | learning =>
      apply no_protection_trade_by_count (c := true)
      · simp [protects, perform]
      · simp [protects, perform, retentionCase]

theorem adequate_goal_selector_distinguishes {O : Type}
    (describe : Conditions → O) (select : O → Practice)
    (adequate : ∀ c, Acceptable c (select (describe c))) :
    describe harmful ≠ describe retentionCase := by
  intro same
  have revise := (revision_frontier_iff _).mp (adequate harmful)
  have retain := (retention_frontier_iff _).mp (adequate retentionCase)
  rw [same, retain] at revise
  cases revise

theorem attainment_only_selector_insufficient
    (select : (Goal → Practice → Nat) → Practice) :
    ¬ ∀ c, Acceptable c (select (achievementProfile c)) := by
  intro adequate
  exact adequate_goal_selector_distinguishes achievementProfile select adequate
    (achievement_profiles_equal harmful retentionCase)

theorem fixed_ground_rule_adequate (c : Conditions) :
    Acceptable c (fixedRule c) := by
  obtain ⟨access, loss, reversed⟩ := c
  cases access <;> cases loss
  · change Acceptable ⟨false, false, reversed⟩ .attendance
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | attendance => exact better_irrefl _ _ _
    | learning => exact (harmless_practices_incomparable _ rfl rfl).2
  · change Acceptable ⟨false, true, reversed⟩ .attendance
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | attendance => exact better_irrefl _ _ _
    | learning =>
      apply no_protection_trade_by_count (c := true)
      · simp [protects, perform]
      · simp [protects, perform]
  · change Acceptable ⟨true, false, reversed⟩ .learning
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | learning => exact better_irrefl _ _ _
    | attendance =>
      apply no_protection_trade_by_count (c := false)
      · simp [protects, perform]
      · simp [protects, perform]
  · change Acceptable ⟨true, true, reversed⟩ .attendance
    refine ⟨trivial, ?_⟩
    intro other _
    cases other with
    | attendance => exact better_irrefl _ _ _
    | learning => exact (crossed_losses_incomparable _ rfl rfl).1

end WisdomGoalGrounds
