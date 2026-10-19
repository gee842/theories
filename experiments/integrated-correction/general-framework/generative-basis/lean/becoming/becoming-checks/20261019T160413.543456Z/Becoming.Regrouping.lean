import Becoming.Significance
import Becoming.Counterfactual
import Becoming.Frame
import Becoming.ValuationFrames

/-!
# Comparison under regrouping

A regrouping reads the claims of one frame; its process does not change. A group is
realized when a member is. Recovering each original claim from that reading is exactly
constancy of realization within its group at the configuration. Under that local
condition at the compared configurations, extension is unchanged, with no enumeration,
weights or normative axiom. On Web.paths, sameness of actual requirements and thresholds
within each group supplies the condition. When requirements are decidable, the exact
all-level condition is equality of their least required level profiles. This preserves admission only: it does not
identify distinct lives, supply their requirements, or establish joint feasibility from
marginal admission. Joint possibilities must themselves be among the claims if compared.

Transfer gives the boundary using existing dynamics: moving or withholding the conveyor
generates two feasible courses from the same start under one rest-law. Each gains and
loses an admitted formation. Merging the two differentiated formations hides both. This
is a loss in a reading, not a refutation of the fuller account or an ethical verdict.
-/

namespace Becoming

namespace Frame

variable {S A C D : Type}

/-- Read claims in groups, without changing the unfolding's process. -/
def regroup (F : Frame S A C) (q : C → D) : Frame S A D :=
  ⟨F.P, fun s d => ∃ c, q c = d ∧ F.realized s c⟩

/-- At this configuration, grouping hides no difference in realization. -/
def RespectsAt (F : Frame S A C) (q : C → D) (s : S) : Prop :=
  ∀ c e, q c = q e → F.realized s c → F.realized s e

theorem respectsAt_iff {F : Frame S A C} {q : C → D} {s : S} :
    F.RespectsAt q s ↔ ∀ c, (F.regroup q).realized s (q c) ↔ F.realized s c :=
  ⟨fun h c => ⟨fun ⟨e, eq, yes⟩ => h e c eq yes, fun yes => ⟨c, rfl, yes⟩⟩,
   fun h c e eq yes => (h e).mp ⟨c, eq, yes⟩⟩

/-- Inclusion always passes to groups. -/
theorem regroup_retains {F : Frame S A C} {q : C → D} {s t : S}
    (keeps : ∀ c, F.realized s c → F.realized t c) :
    ∀ d, (F.regroup q).realized s d → (F.regroup q).realized t d :=
  fun _ ⟨c, eq, yes⟩ => ⟨c, eq, keeps c yes⟩

/-- Recovering inclusion needs fidelity at the proposed successor only. -/
theorem regroup_retains_iff {F : Frame S A C} {q : C → D} {s t : S}
    (at_t : F.RespectsAt q t) :
    (∀ d, (F.regroup q).realized s d → (F.regroup q).realized t d) ↔
      (∀ c, F.realized s c → F.realized t c) :=
  ⟨fun keeps c yes => (respectsAt_iff.mp at_t c).mp (keeps (q c) ⟨c, rfl, yes⟩),
   regroup_retains⟩

/-- A newly realized group has a newly realized member, without a fidelity premise. -/
theorem regroup_gain_reflects {F : Frame S A C} {q : C → D} {s t : S}
    (gain : ∃ d, (F.regroup q).realized t d ∧ ¬ (F.regroup q).realized s d) :
    ∃ c, F.realized t c ∧ ¬ F.realized s c :=
  match gain with
  | ⟨_, ⟨c, eq, yes⟩, no⟩ => ⟨c, yes, fun old => no ⟨c, eq, old⟩⟩

/-- Keeping a gain visible needs fidelity at the baseline only. -/
theorem regroup_gain_iff {F : Frame S A C} {q : C → D} {s t : S}
    (at_s : F.RespectsAt q s) :
    (∃ d, (F.regroup q).realized t d ∧ ¬ (F.regroup q).realized s d) ↔
      (∃ c, F.realized t c ∧ ¬ F.realized s c) :=
  ⟨regroup_gain_reflects,
   fun ⟨c, yes, no⟩ => ⟨q c, ⟨c, rfl, yes⟩, fun old => no ((respectsAt_iff.mp at_s c).mp old)⟩⟩

/-- Lossless regrouping preserves and reflects the existing extension comparison. -/
theorem regroup_extension_iff {F : Frame S A C} {q : C → D} {s t : S}
    (at_s : F.RespectsAt q s) (at_t : F.RespectsAt q t) :
    Extension (F.regroup q) (fun _ => True) s t ↔ Extension F (fun _ => True) s t :=
  ⟨fun ⟨keeps, d, _, yes, no⟩ =>
    match regroup_gain_reflects ⟨d, yes, no⟩ with
    | ⟨c, fresh, absent⟩ => ⟨(regroup_retains_iff at_t).mp keeps, c, trivial, fresh, absent⟩,
   fun ⟨keeps, c, _, yes, no⟩ =>
    match (regroup_gain_iff at_s).mpr ⟨c, yes, no⟩ with
    | ⟨d, fresh, absent⟩ => ⟨regroup_retains keeps, d, trivial, fresh, absent⟩⟩

end Frame

namespace Web

variable {F C D : Type}

/-- The least level a formation requires on each condition; an unrequired condition
requires zero. The decision of each requirement is supplied, not a classical axiom. -/
def requiredLevel (W : Web F C) (decides : ∀ t f c, Decidable (W.requires t f c))
    (t : Nat) (f : F) (c : C) : Nat :=
  @ite Nat (W.requires t f c) (decides t f c) (W.need t f c) 0

/-- Admission is exactly meeting this least profile. -/
theorem admits_iff_requiredLevel {W : Web F C}
    (decides : ∀ t f c, Decidable (W.requires t f c))
    (t : Nat) (f : F) (l : C → Nat) :
    W.Admits l t f ↔ ∀ c, W.requiredLevel decides t f c ≤ l c := by
  constructor
  · intro admits c
    cases h : decides t f c with
    | isTrue req => exact (show W.requiredLevel decides t f c = W.need t f c from if_pos req) ▸ admits c req
    | isFalse no => exact (show W.requiredLevel decides t f c = 0 from if_neg no).symm ▸ Nat.zero_le (l c)
  · intro enough c req
    exact (show W.requiredLevel decides t f c = W.need t f c from if_pos req) ▸ enough c

theorem admits_requiredLevel {W : Web F C}
    (decides : ∀ t f c, Decidable (W.requires t f c)) (t : Nat) (f : F) :
    W.Admits (W.requiredLevel decides t f) t f :=
  (W.admits_iff_requiredLevel decides t f _).mpr fun _ => Nat.le_refl _

/-- Exact operative content: identical admission under every level test is equivalent
to identical minimum requirements. Differences about zero needs add no admission content. -/
theorem same_admission_iff_requiredLevel {W : Web F C}
    (decides : ∀ t f c, Decidable (W.requires t f c)) (t : Nat) (f g : F) :
    (∀ l, W.Admits l t f ↔ W.Admits l t g) ↔
      ∀ c, W.requiredLevel decides t f c = W.requiredLevel decides t g c := by
  constructor
  · intro same c
    have fg := (W.admits_iff_requiredLevel decides t f _).mp
      ((same _).mpr (W.admits_requiredLevel decides t g)) c
    have gf := (W.admits_iff_requiredLevel decides t g _).mp
      ((same _).mp (W.admits_requiredLevel decides t f)) c
    exact Nat.le_antisymm fg gf
  · intro eq l
    constructor
    · intro yes
      exact (W.admits_iff_requiredLevel decides t g l).mpr fun c =>
        eq c ▸ (W.admits_iff_requiredLevel decides t f l).mp yes c
    · intro yes
      exact (W.admits_iff_requiredLevel decides t f l).mpr fun c =>
        (eq c).symm ▸ (W.admits_iff_requiredLevel decides t g l).mp yes c

/-- Group formations while retaining their step. -/
def groupEvent (q : F → D) (e : F × Nat) : D × Nat := (q e.1, e.2)

/-- With requirements decidable, the exact all-level fidelity condition is equality of
the groups' minimum requirements. Local fidelity can hold on fewer tested courses. -/
theorem regroup_faithful_iff_requiredLevel {W : Web F C} (q : F → D)
    (decides : ∀ t f c, Decidable (W.requires t f c)) :
    (∀ l, W.paths.RespectsAt (groupEvent q) l) ↔
      ∀ f g, q f = q g → ∀ t c,
        W.requiredLevel decides t f c = W.requiredLevel decides t g c := by
  constructor
  · intro faithful f g eq t
    apply (W.same_admission_iff_requiredLevel decides t f g).mp
    intro l
    exact ⟨fun yes => faithful (fun _ => l) (f, t) (g, t)
        (congrArg (fun d => (d, t)) eq) yes,
      fun yes => faithful (fun _ => l) (g, t) (f, t)
        (congrArg (fun d => (d, t)) eq.symm) yes⟩
  · intro same l e d eq yes
    have time : e.2 = d.2 := congrArg (fun x : D × Nat => x.2) eq
    have group : q e.1 = q d.1 := congrArg (fun x : D × Nat => x.1) eq
    have admitted := ((W.same_admission_iff_requiredLevel decides e.2 e.1 d.1).mpr
      (same e.1 d.1 group e.2) (l e.2)).mp yes
    change W.Admits (l d.2) d.2 d.1
    exact time ▸ admitted

/-- The compared content has the same operative requirements within each group. -/
def SameRequirements (W : Web F C) (q : F → D) : Prop :=
  ∀ f g, q f = q g → ∀ t c,
    (W.requires t f c ↔ W.requires t g c) ∧
      (W.requires t f c → W.need t f c = W.need t g c)

theorem SameRequirements.admits {W : Web F C} {q : F → D}
    (same : W.SameRequirements q) {f g : F} (eq : q f = q g)
    (t : Nat) (l : C → Nat) : W.Admits l t f ↔ W.Admits l t g :=
  ⟨fun yes c req =>
      let h := same f g eq t c
      (h.2 (h.1.mpr req)) ▸ yes c (h.1.mpr req),
   fun yes c req =>
      let h := same f g eq t c
      (h.2 req).symm ▸ yes c (h.1.mp req)⟩

/-- Actual requirements supply the frame's fidelity condition on every level path. -/
theorem SameRequirements.respects {W : Web F C} {q : F → D}
    (same : W.SameRequirements q) (l : Nat → C → Nat) :
    W.paths.RespectsAt (groupEvent q) l := by
  intro e d eq yes
  have time : e.2 = d.2 := congrArg (fun x : D × Nat => x.2) eq
  have group : q e.1 = q d.1 := congrArg (fun x : D × Nat => x.1) eq
  have admitted := (same.admits group e.2 (l e.2)).mp yes
  change W.Admits (l d.2) d.2 d.1
  exact time ▸ admitted

/-- Existing comparison-by-widening survives regrouping under its exact local fidelity
conditions; no favorable rank is supplied by a definition of the groups. -/
theorem regroup_extension_iff_widens {W : Web F C} {q : F → D}
    {l l' : Nat → C → Nat}
    (at_l : W.paths.RespectsAt (groupEvent q) l)
    (at_l' : W.paths.RespectsAt (groupEvent q) l') :
    Extension (W.paths.regroup (groupEvent q)) (fun _ => True) l' l ↔ W.Widens l l' :=
  (Frame.regroup_extension_iff at_l' at_l).trans (W.paths_extension_iff_widens)

theorem SameRequirements.extension_iff_widens {W : Web F C} {q : F → D}
    (same : W.SameRequirements q) {l l' : Nat → C → Nat} :
    Extension (W.paths.regroup (groupEvent q)) (fun _ => True) l' l ↔ W.Widens l l' :=
  regroup_extension_iff_widens (same.respects l) (same.respects l')

end Web

namespace Transfer

/-- Both alternatives keep the same inactive rest-law. Only the conveyor's act changes. -/
def quietLaw : ExchangeLaw Formation Bool := ExchangeLaw.ofMoves fun _ _ _ => (0, 0)

def conveyorAct (move : Bool) : ExchangeLaw Formation Bool :=
  ExchangeLaw.ofMoves fun t f c =>
    if move then (flow.take t f c, flow.give t f c) else (0, 0)

def courseLaw (move : Bool) : ExchangeLaw Formation Bool :=
  quietLaw.withAct conveyorPart (conveyorAct move)

theorem courseLaw_nonanticipating (move : Bool) : (courseLaw move).Nonanticipating :=
  fun _ _ _ _ _ _ => ⟨rfl, rfl⟩

theorem move_levels (t : Nat) (c : Bool) :
    (courseLaw true).levels flow.present (withheldLevel 0) t c = web.level t c := by
  induction t with
  | zero => cases c <;> rfl
  | succ t ih =>
    rw [ExchangeLaw.levels_succ, ih]
    cases t <;> cases c <;> rfl

theorem wait_levels (t : Nat) (c : Bool) :
    (courseLaw false).levels flow.present (withheldLevel 0) t c = withheldLevel t c := by
  induction t with
  | zero => rfl
  | succ t ih =>
    rw [ExchangeLaw.levels_succ, ih]
    cases t <;> cases c <;> rfl

theorem courses_feasible (move : Bool) :
    (courseLaw move).Feasible flow.present (withheldLevel 0) := by
  intro t c
  cases move with
  | false =>
    cases t <;> cases c <;> exact Nat.zero_le _
  | true =>
    rw [move_levels]
    cases t <;> cases c <;> first | exact Nat.le_refl _ | exact Nat.zero_le _

/-- Feasibility supplies balance for each generated alternative. -/
theorem courses_balanced (move : Bool) :
    ((courseLaw move).course flow.present (withheldLevel 0)).Balances
      (web.withLevel ((courseLaw move).levels flow.present (withheldLevel 0))) :=
  (ExchangeLaw.course_balances_iff (courseLaw_nonanticipating move) web).mpr
    (courses_feasible move)

/-- The alternatives change only the conveyor; the rest follows the same law. -/
theorem courses_follow_same_rest (move : Bool) :
    ((courseLaw move).course flow.present (withheldLevel 0)).Follows quietLaw conveyorPart
      ((courseLaw move).levels flow.present (withheldLevel 0)) :=
  ExchangeLaw.withAct_follows flow.present (withheldLevel 0)

/-- Group the distinct first and second formations; keep the conveyor separate. -/
def merged : Formation → Bool
  | .conveyor => false
  | .first => true
  | .second => true

theorem move_group_realized (d : Bool × Nat) :
    (web.paths.regroup (Web.groupEvent merged)).realized web.level d := by
  rcases d with ⟨b, t⟩
  cases b with
  | false => exact ⟨(.conveyor, t), rfl, fun c no => nomatch no⟩
  | true =>
    cases t with
    | zero => exact ⟨(.first, 0), rfl, fun c req => by cases c; exact Nat.le_refl 1; exact False.elim req⟩
    | succ t => exact ⟨(.second, t + 1), rfl, fun c req => by cases c; exact False.elim req; exact Nat.le_refl 1⟩

theorem wait_group_realized (d : Bool × Nat) :
    (web.paths.regroup (Web.groupEvent merged)).realized withheldLevel d := by
  rcases d with ⟨b, t⟩
  cases b with
  | false => exact ⟨(.conveyor, t), rfl, fun c no => nomatch no⟩
  | true => exact ⟨(.first, t), rfl, fun c req => by cases c; exact Nat.le_refl 1; exact False.elim req⟩

/-- This grouping hides an actual difference, rather than just changing names. -/
theorem merged_not_respects : ¬ web.paths.RespectsAt (Web.groupEvent merged) web.level :=
  fun same => (mixed withheld).2.2 0 |>.2.2.2
    (same (.second, 1) (.first, 1) rfl ((mixed withheld).2.2 0).2.2.1)

/-- Alternatives produced from the same initial relations have real opposed gains;
the coarse reading makes both courses realize exactly the same groups. -/
theorem generated_mixed_hidden :
    web.Mixed ((courseLaw true).levels flow.present (withheldLevel 0))
      ((courseLaw false).levels flow.present (withheldLevel 0)) ∧
    ∀ d, (web.paths.regroup (Web.groupEvent merged)).realized
        ((courseLaw true).levels flow.present (withheldLevel 0)) d ↔
      (web.paths.regroup (Web.groupEvent merged)).realized
        ((courseLaw false).levels flow.present (withheldLevel 0)) d := by
  have move_admits (t : Nat) (f : Formation) :
      web.Admits ((courseLaw true).levels flow.present (withheldLevel 0) t) t f ↔
        web.Admits (web.level t) t f :=
    ⟨fun h c r => move_levels t c ▸ h c r, fun h c r => (move_levels t c).symm ▸ h c r⟩
  have wait_admits (t : Nat) (f : Formation) :
      web.Admits ((courseLaw false).levels flow.present (withheldLevel 0) t) t f ↔
        web.Admits (withheldLevel t) t f :=
    ⟨fun h c r => wait_levels t c ▸ h c r, fun h c r => (wait_levels t c).symm ▸ h c r⟩
  have old := mixed withheld
  constructor
  · rcases old.1 with ⟨t, f, yes, no⟩
    rcases old.2.1 with ⟨s, g, yes', no'⟩
    exact ⟨⟨t, f, (move_admits t f).mpr yes, fun h => no ((wait_admits t f).mp h)⟩,
      ⟨s, g, (wait_admits s g).mpr yes', fun h => no' ((move_admits s g).mp h)⟩⟩
  · intro d
    rcases move_group_realized d with ⟨e, eq, yes⟩
    rcases wait_group_realized d with ⟨f, eq', yes'⟩
    exact ⟨fun _ => ⟨f, eq', (wait_admits f.2 f.1).mpr yes'⟩,
      fun _ => ⟨e, eq, (move_admits e.2 e.1).mpr yes⟩⟩

end Transfer

end Becoming
