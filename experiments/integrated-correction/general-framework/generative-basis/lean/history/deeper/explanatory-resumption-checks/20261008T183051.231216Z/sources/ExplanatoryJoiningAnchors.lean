import ExplanatoryJoiningRefinement

/-! A precise limitation of unanchored incidence questions, tested on the
repository's admitted histories and actual inability to reuse one event.
The coarser account is exact for the new language, not for full joining.
This is a representation failure, not a refutation of generative grounding. -/
namespace Generative.ExplanatoryJoiningAnchors
open ExplanatoryBranching ExplanatoryLocalUnits ExplanatoryJoining
open ExplanatoryJoiningIncidence ExplanatoryJoiningRefinement ExplanatoryUniqueness
universe u v
variable {F : Type u} {G : Type v}

def RoleTotal (J : Join F) : Prop := ∀ x r, ∃ e : Occurrence J, e.at r = x
def coarseJoin : Join Unit := fun _ _ _ => True

theorem units_role_total {J : Join F} (hu : HasUnits J) : RoleTotal J := by
  intro x r
  cases r with
  | first =>
    obtain ⟨e, he⟩ := hu.2 x
    exact ⟨⟨x, e, x, he.2⟩, rfl⟩
  | second =>
    obtain ⟨e, he⟩ := hu.1 x
    exact ⟨⟨e, x, x, he.2⟩, rfl⟩
  | result =>
    obtain ⟨e, he⟩ := hu.1 x
    exact ⟨⟨e, x, x, he.2⟩, rfl⟩

/-- Every role-total law has this open coarse account; no finiteness or
classical selection is needed for the existence witnesses in this proof. -/
theorem role_total_collapse_open {J : Join F} (total : RoleTotal J) :
    OpenMap J coarseJoin (fun _ => ()) := by
  refine ⟨fun _ _ _ _ => True.intro, ?_⟩
  intro x e r he
  obtain ⟨f, hf⟩ := total x r
  exact ⟨f.at, f.formed, hf, fun _ => Subsingleton.elim _ _⟩

theorem units_collapse_open {J : Join F} (hu : HasUnits J) :
    OpenMap J coarseJoin (fun _ => ()) := role_total_collapse_open (units_role_total hu)

theorem units_same_incidence_questions {J : Join F} {K : Join G}
    (hj : HasUnits J) (hk : HasUnits K) (x : F) (y : G) : Related J K x y :=
  same_trans (open_map_preserves_questions (units_collapse_open hj) x)
    (same_symm (open_map_preserves_questions (units_collapse_open hk) y))

def coarseAccount (_J : Join F) : Presentation F Question Unit where
  encode _ := ()
  read _ q := Holds (model coarseJoin) (.inl ()) q

theorem coarse_account_exact {J : Join F} (hu : HasUnits J) :
    Exact (fun x q => Holds (model J) (.inl x) q) (coarseAccount J) := by
  intro x q
  exact (open_map_preserves_questions (units_collapse_open hu) x q).symm

theorem coarse_account_reduced (J : Join F) :
    Reduced (fun x q => Holds (model J) (.inl x) q) (coarseAccount J) := fun _ _ _ => rfl

theorem every_admitted_history_collapses {S : Type u} {A : Type v}
    (P : Process S A) (x : Admitted P) : Related (traceJoin P) coarseJoin x () :=
  open_map_preserves_questions (units_collapse_open (trace_has_units P)) x

def spent : Admitted budgetProcess := ⟨spend, spend_valid⟩

theorem spent_has_no_self_result : ¬ ∃ z, traceJoin budgetProcess spent spent z := by
  rintro ⟨z, hz⟩
  exact spend_cannot_self_join hz.1

theorem coarse_self_join_loses_real_failure :
    Related (traceJoin budgetProcess) coarseJoin spent () ∧ coarseJoin () () () ∧
    ¬ ∃ z, traceJoin budgetProcess spent spent z :=
  ⟨every_admitted_history_collapses budgetProcess spent, True.intro, spent_has_no_self_result⟩

/-- The same exact account of incidence questions is insufficient for fixed
input joining. The failure concerns continuation, not arbitrary token names. -/
def PairLifting (J : Join F) (K : Join G) (p : F → G) : Prop :=
  ∀ x y z, K (p x) (p y) z → ∃ w, J x y w ∧ p w = z

theorem open_map_does_not_force_pair_lifting :
    OpenMap (traceJoin budgetProcess) coarseJoin (fun _ => ()) ∧
    ¬ PairLifting (traceJoin budgetProcess) coarseJoin (fun _ => ()) := by
  refine ⟨units_collapse_open (trace_has_units budgetProcess), ?_⟩
  intro h
  obtain ⟨z, hz, _⟩ := h spent spent () True.intro
  exact spent_has_no_self_result ⟨z, hz⟩

theorem same_incidence_distinct_boundary_probes :
    Related (traceJoin budgetProcess) (traceJoin budgetProcess)
      (traceIdle budgetProcess false) (traceIdle budgetProcess true) ∧
    ¬ SameAnswers (probeTarget budgetProcess) (idle false) (idle true) :=
  ⟨units_same_incidence_questions (trace_has_units budgetProcess) (trace_has_units budgetProcess) _ _,
    boundary_idles_distinguished⟩

/-- A name-independent question retaining the SAME focused fragment in both
input slots distinguishes the actual spent fragment from its coarse code. -/
def SelfJoinable (J : Join F) (x : F) : Prop := ∃ z, J x x z

theorem retained_anchor_separates :
    SelfJoinable coarseJoin () ∧ ¬ SelfJoinable (traceJoin budgetProcess) spent :=
  ⟨⟨(), True.intro⟩, spent_has_no_self_result⟩

end Generative.ExplanatoryJoiningAnchors

#print axioms Generative.ExplanatoryJoiningAnchors.units_role_total
#print axioms Generative.ExplanatoryJoiningAnchors.role_total_collapse_open
#print axioms Generative.ExplanatoryJoiningAnchors.units_collapse_open
#print axioms Generative.ExplanatoryJoiningAnchors.units_same_incidence_questions
#print axioms Generative.ExplanatoryJoiningAnchors.coarse_account_exact
#print axioms Generative.ExplanatoryJoiningAnchors.coarse_account_reduced
#print axioms Generative.ExplanatoryJoiningAnchors.every_admitted_history_collapses
#print axioms Generative.ExplanatoryJoiningAnchors.spent_has_no_self_result
#print axioms Generative.ExplanatoryJoiningAnchors.coarse_self_join_loses_real_failure
#print axioms Generative.ExplanatoryJoiningAnchors.open_map_does_not_force_pair_lifting
#print axioms Generative.ExplanatoryJoiningAnchors.same_incidence_distinct_boundary_probes
#print axioms Generative.ExplanatoryJoiningAnchors.retained_anchor_separates
