import ExplanatoryJointness

/-! Joint tests are motivated by declared support access and exclusive holding.
The ordinary step records completion and release, so it intentionally omits
overlapping holding intervals. This is a scoped formal mechanism, not a claim
that all generative activity consumes exclusive reusable support. -/
namespace Generative.ExplanatorySharedSupport
open ExplanatoryJointness ExplanatoryUniqueness

inductive Node where
  | whole
  | held : Bool → Bool → Node
  deriving DecidableEq

/-- Within one configuration, two activity roles either reach one common slot
or two distinct slots. The second role parameter is a support position. -/
def Access (shared task slot : Bool) : Prop := slot = if shared then false else task

def Can (shared task : Bool) : Prop := ∃ slot, Access shared task slot

def Joint (shared : Bool) : Node → Node → Node → Prop
  | .whole, .held task slot, .held task' slot' =>
      task = false ∧ task' = true ∧ Access shared task slot ∧
        Access shared task' slot' ∧ slot ≠ slot'
  | _, _, _ => False

def model (shared : Bool) : Model Node Bool Bool where
  process.step s task t := s = .whole ∧ t = .whole ∧ Can shared task
  condition s task := match s with
    | .whole => Can shared task
    | .held role _ => role = task
  joint := Joint shared

theorem either_activity_possible (shared task : Bool) : Can shared task :=
  ⟨if shared then false else task, rfl⟩

theorem shared_joint_impossible (s l r : Node) : ¬ Joint true s l r := by
  intro h
  cases s <;> cases l <;> cases r <;> try exact h
  rcases h with ⟨_, _, hi, hj, ne⟩
  exact ne (hi.trans hj.symm)

theorem separate_joint_witness :
    Joint false .whole (.held false false) (.held true true) := by
  exact ⟨rfl, rfl, rfl, rfl, Bool.false_ne_true⟩

theorem separate_joint_iff (s l r : Node) :
    Joint false s l r ↔ s = .whole ∧ l = .held false false ∧ r = .held true true := by
  constructor
  · intro h
    cases s <;> cases l <;> cases r <;> try exact False.elim h
    rcases h with ⟨rfl, rfl, hi, hj, _⟩
    change _ = false at hi
    change _ = true at hj
    subst_vars
    exact ⟨rfl, rfl, rfl⟩
  · rintro ⟨rfl, rfl, rfl⟩
    exact separate_joint_witness

theorem both_capabilities_hold (shared : Bool) :
    Holds (model shared) .whole (.conj (.atom false) (.atom true)) :=
  ⟨either_activity_possible shared false, either_activity_possible shared true⟩

def simultaneous : Test Bool Bool := .together (.atom false) (.atom true)

theorem separate_support_joint_answer : Holds (model false) .whole simultaneous :=
  ⟨.held false false, .held true true, separate_joint_witness, rfl, rfl⟩

theorem shared_support_joint_answer : ¬ Holds (model true) .whole simultaneous := by
  rintro ⟨l, r, joint, _, _⟩
  exact shared_joint_impossible _ _ _ joint

theorem ordinary_bisimulation :
    ExplanatoryBranching.Bisimulation (sequential (model true)) (sequential (model false))
      (fun s t => s = .whole ∧ t = .whole) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · rintro s t a s' ⟨rfl, rfl⟩ ⟨_, eq, _⟩
    subst s'
    exact ⟨.whole, ⟨rfl, rfl, either_activity_possible false a⟩, rfl, rfl⟩
  · rintro s t a t' ⟨rfl, rfl⟩ ⟨_, eq, _⟩
    subst t'
    exact ⟨.whole, ⟨rfl, rfl, either_activity_possible true a⟩, rfl, rfl⟩
  · rintro s t ⟨rfl, rfl⟩ task
    exact ⟨fun _ => either_activity_possible false task, fun _ => either_activity_possible true task⟩

theorem all_ordinary_questions_agree :
    ExplanatoryBranching.Same (sequential (model true)) (sequential (model false)) .whole .whole :=
  ExplanatoryBranching.bisimulation_implies_same ordinary_bisimulation ⟨rfl, rfl⟩

theorem joint_questions_separate : ¬ Same (model true) (model false) .whole .whole := by
  intro same
  exact shared_support_joint_answer ((same simultaneous).mpr separate_support_joint_answer)

theorem step_finitely_branching (shared : Bool) :
    ∀ s a, ∃ xs : List Node, ∀ t, (model shared).process.step s a t ↔ t ∈ xs := by
  intro s a
  cases s with
  | whole =>
    refine ⟨[.whole], ?_⟩
    intro t
    simp [model, either_activity_possible]
  | held task slot =>
    refine ⟨[], ?_⟩
    intro t
    simp [model]

theorem joint_finitely_branching (shared : Bool) :
    ∀ s, ∃ xs : List (Node × Node), ∀ p, (model shared).joint s p.1 p.2 ↔ p ∈ xs := by
  intro s
  cases shared with
  | true =>
    refine ⟨[], ?_⟩
    intro p
    exact iff_of_false (shared_joint_impossible _ _ _) (by simp)
  | false =>
    cases s with
    | whole =>
      refine ⟨[(.held false false, .held true true)], ?_⟩
      rintro ⟨l, r⟩
      simp [model, separate_joint_iff]
    | held task slot =>
      refine ⟨[], ?_⟩
      intro p
      simp [model, Joint]

theorem both_models_compact (shared : Bool) : StepCompact (model shared) ∧ JointCompact (model shared) :=
  ⟨finite_steps_compact (step_finitely_branching shared), finite_joints_compact (joint_finitely_branching shared)⟩

/-- Fixed concrete slots can remain behaviorally interchangeable in isolation.
Their inability to be held twice is a relation, not an intrinsic label. -/
inductive Piece where
  | whole
  | slot : Bool → Piece
  deriving DecidableEq

def slotJoint : Piece → Piece → Piece → Prop
  | .whole, .slot a, .slot b => a ≠ b
  | _, _, _ => False

def slotModel : Model Piece Unit Empty where
  process.step _ _ _ := False
  condition _ o := nomatch o
  joint := slotJoint

theorem slots_same_all_joint_tests : Same slotModel slotModel (.slot false) (.slot true) := by
  intro f
  induction f with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg f ih => exact not_congr ih
  | conj f g ihf ihg => exact and_congr ihf ihg
  | after a f _ => simp [Holds, slotModel]
  | together f g _ _ => simp [Holds, slotModel, slotJoint]

theorem distinct_slots_join : slotModel.joint .whole (.slot false) (.slot true) := Bool.false_ne_true

theorem duplicate_slot_fails : ¬ slotModel.joint .whole (.slot false) (.slot false) := fun h => h rfl

theorem no_reduced_exact_native_join {C : Type} (p : Presentation Piece (Test Unit Empty) C)
    (reduced : Reduced (Holds slotModel) p) :
    ¬ ∃ K, ExplanatoryUniversality.RelExact p slotModel.joint K := by
  apply ExplanatoryUniversality.separating_relation_blocks_descent reduced
    (a := .whole) (a' := .whole) (b := .slot false) (b' := .slot false)
    (c := .slot true) (c' := .slot false)
  · exact fun _ => Iff.rfl
  · exact fun _ => Iff.rfl
  · exact same_symm slots_same_all_joint_tests
  · exact distinct_slots_join
  · exact duplicate_slot_fails

def Fits (x y : Piece) : Prop := ∃ s, slotModel.joint s x y

theorem fits_slots_iff (a b : Bool) : Fits (.slot a) (.slot b) ↔ a ≠ b := by
  constructor
  · rintro ⟨s, h⟩
    cases s with
    | whole => exact h
    | slot c => exact False.elim h
  · intro h
    exact ⟨.whole, h⟩

theorem fixed_partner_separates :
    Fits (.slot true) (.slot false) ∧ ¬ Fits (.slot false) (.slot false) :=
  ⟨(fits_slots_iff true false).mpr (fun h => Bool.false_ne_true h.symm),
    fun h => (fits_slots_iff false false).mp h rfl⟩

theorem partner_answers_recover_slot (a b : Bool) :
    (∀ partner, Fits (.slot a) (.slot partner) ↔ Fits (.slot b) (.slot partner)) ↔ a = b := by
  constructor
  · intro same
    cases a <;> cases b <;> simp_all [fits_slots_iff]
  · intro eq
    subst b
    exact fun _ => Iff.rfl

theorem slot_model_compact : StepCompact slotModel ∧ JointCompact slotModel := by
  constructor
  · apply finite_steps_compact
    intro s a
    exact ⟨[], fun t => by simp [slotModel]⟩
  · apply finite_joints_compact
    intro s
    cases s with
    | whole =>
      refine ⟨[(.slot false, .slot true), (.slot true, .slot false)], ?_⟩
      rintro ⟨l, r⟩
      cases l with
      | whole => simp [slotModel, slotJoint]
      | slot a =>
        cases r with
        | whole => simp [slotModel, slotJoint]
        | slot b => cases a <;> cases b <;> simp [slotModel, slotJoint]
    | slot b =>
      exact ⟨[], fun p => by simp [slotModel, slotJoint]⟩

def slotAccount : Presentation Piece (Test Unit Empty) Bool where
  encode s := match s with | .whole => false | .slot _ => true
  read c f := Holds slotModel (if c then .slot false else .whole) f

theorem slot_account_exact : Exact (Holds slotModel) slotAccount := by
  intro s f
  cases s with
  | whole => exact Iff.rfl
  | slot b =>
    cases b with
    | false => exact Iff.rfl
    | true => exact slots_same_all_joint_tests f

theorem whole_not_slot_same (b : Bool) : ¬ Same slotModel slotModel .whole (.slot b) := by
  intro same
  have yes : Holds slotModel .whole (.together .top .top) :=
    ⟨.slot false, .slot true, distinct_slots_join, True.intro, True.intro⟩
  have impossible := (same (.together .top .top)).mp yes
  simpa [Holds, slotModel, slotJoint] using impossible

theorem slot_account_reduced : Reduced (Holds slotModel) slotAccount := by
  intro s t same
  cases s with
  | whole =>
    cases t with
    | whole => rfl
    | slot b => exact False.elim (whole_not_slot_same b same)
  | slot a =>
    cases t with
    | whole => exact False.elim (whole_not_slot_same a (same_symm same))
    | slot b => rfl

theorem code_joint_does_not_validate_duplicate_piece :
    codeJoint slotModel slotAccount (slotAccount.encode .whole)
      (slotAccount.encode (.slot false)) (slotAccount.encode (.slot false)) ∧
    ¬ slotModel.joint .whole (.slot false) (.slot false) :=
  ⟨⟨.whole, .slot false, .slot true, rfl, rfl, rfl, distinct_slots_join⟩, duplicate_slot_fails⟩

end Generative.ExplanatorySharedSupport

#print axioms Generative.ExplanatorySharedSupport.either_activity_possible
#print axioms Generative.ExplanatorySharedSupport.shared_joint_impossible
#print axioms Generative.ExplanatorySharedSupport.separate_joint_witness
#print axioms Generative.ExplanatorySharedSupport.separate_joint_iff
#print axioms Generative.ExplanatorySharedSupport.both_capabilities_hold
#print axioms Generative.ExplanatorySharedSupport.separate_support_joint_answer
#print axioms Generative.ExplanatorySharedSupport.shared_support_joint_answer
#print axioms Generative.ExplanatorySharedSupport.ordinary_bisimulation
#print axioms Generative.ExplanatorySharedSupport.all_ordinary_questions_agree
#print axioms Generative.ExplanatorySharedSupport.joint_questions_separate
#print axioms Generative.ExplanatorySharedSupport.step_finitely_branching
#print axioms Generative.ExplanatorySharedSupport.joint_finitely_branching
#print axioms Generative.ExplanatorySharedSupport.both_models_compact
#print axioms Generative.ExplanatorySharedSupport.slots_same_all_joint_tests
#print axioms Generative.ExplanatorySharedSupport.distinct_slots_join
#print axioms Generative.ExplanatorySharedSupport.duplicate_slot_fails
#print axioms Generative.ExplanatorySharedSupport.no_reduced_exact_native_join
#print axioms Generative.ExplanatorySharedSupport.fits_slots_iff
#print axioms Generative.ExplanatorySharedSupport.fixed_partner_separates
#print axioms Generative.ExplanatorySharedSupport.partner_answers_recover_slot
#print axioms Generative.ExplanatorySharedSupport.slot_model_compact
#print axioms Generative.ExplanatorySharedSupport.slot_account_exact
#print axioms Generative.ExplanatorySharedSupport.whole_not_slot_same
#print axioms Generative.ExplanatorySharedSupport.slot_account_reduced
#print axioms Generative.ExplanatorySharedSupport.code_joint_does_not_validate_duplicate_piece
