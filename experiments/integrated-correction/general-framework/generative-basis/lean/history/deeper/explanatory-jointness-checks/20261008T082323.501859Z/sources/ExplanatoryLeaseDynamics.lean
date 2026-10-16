import ExplanatorySharedSupport

/-! An actual acquisition/release law supports the joint distinction. A closed
activity episode may return the same support while overlap remains impossible.
Exclusive holding is a stated local law, not a universal account of resources. -/
namespace Generative.ExplanatoryLeaseDynamics
open ExplanatoryJointness ExplanatorySharedSupport ExplanatoryUniqueness

abbrev Occupancy := Bool → Bool
def vacant : Occupancy := fun _ => false
def mark (busy : Occupancy) (slot : Bool) : Occupancy :=
  fun other => if other = slot then true else busy other
def clear (busy : Occupancy) (slot : Bool) : Occupancy :=
  fun other => if other = slot then false else busy other

def Acquire (shared : Bool) (busy : Occupancy) (task : Bool) (next : Occupancy) : Prop :=
  ∃ slot, Access shared task slot ∧ busy slot = false ∧ next = mark busy slot

def Release (busy : Occupancy) (slot : Bool) (next : Occupancy) : Prop :=
  busy slot = true ∧ next = clear busy slot

theorem mark_at_slot (busy : Occupancy) (slot : Bool) : mark busy slot slot = true := by
  simp [mark]

theorem mark_at_other (busy : Occupancy) {slot other : Bool} (h : other ≠ slot) :
    mark busy slot other = busy other := by simp [mark, h]

theorem clear_after_fresh_mark (busy : Occupancy) (slot : Bool) (fresh : busy slot = false) :
    clear (mark busy slot) slot = busy := by
  funext other
  by_cases h : other = slot
  · subst other; simp [clear, fresh]
  · simp [clear, mark, h]

theorem activity_round (shared task : Bool) :
    ∃ middle slot, Acquire shared vacant task middle ∧ Release middle slot vacant := by
  let slot := if shared then false else task
  refine ⟨mark vacant slot, slot, ⟨slot, rfl, rfl, rfl⟩, mark_at_slot _ _, ?_⟩
  exact (clear_after_fresh_mark vacant slot rfl).symm

theorem ordinary_step_has_native_round (shared task : Bool) :
    (model shared).process.step .whole task .whole ↔
      ∃ middle slot, Acquire shared vacant task middle ∧ Release middle slot vacant :=
  ⟨fun _ => activity_round shared task,
    fun ⟨_, _, ⟨slot, access, _, _⟩, _⟩ => ⟨rfl, rfl, slot, access⟩⟩

theorem joint_answer_iff_overlapping_acquisitions (shared : Bool) :
    Holds (model shared) .whole simultaneous ↔
      ∃ first final, Acquire shared vacant false first ∧ Acquire shared first true final := by
  constructor
  · rintro ⟨l, r, joint, _, _⟩
    cases l <;> cases r <;> try exact False.elim joint
    rcases joint with ⟨rfl, rfl, leftAccess, rightAccess, distinct⟩
    rename_i i j
    refine ⟨mark vacant i, mark (mark vacant i) j,
      ⟨i, leftAccess, rfl, rfl⟩, j, rightAccess, ?_, rfl⟩
    exact mark_at_other vacant (fun h => distinct h.symm)
  · rintro ⟨first, final, ⟨i, hi, _, rfl⟩, ⟨j, hj, fresh, _⟩⟩
    have distinct : i ≠ j := by
      intro eq
      subst j
      rw [mark_at_slot] at fresh
      cases fresh
    exact ⟨.held false i, .held true j, ⟨rfl, rfl, hi, hj, distinct⟩, rfl, rfl⟩

theorem shared_overlap_impossible :
    ¬ ∃ first final, Acquire true vacant false first ∧ Acquire true first true final :=
  fun h => shared_support_joint_answer ((joint_answer_iff_overlapping_acquisitions true).mpr h)

theorem separate_overlap_realized :
    ∃ first final, Acquire false vacant false first ∧ Acquire false first true final :=
  (joint_answer_iff_overlapping_acquisitions false).mp separate_support_joint_answer

inductive Event where
  | acquire : Bool → Event
  | release : Bool → Event

def process (shared : Bool) : Process Occupancy Event where
  step busy event next := match event with
    | .acquire task => Acquire shared busy task next
    | .release slot => Release busy slot next

def episode (shared task : Bool) : List Event :=
  [.acquire task, .release (if shared then false else task)]

theorem episode_returns_vacant (shared task : Bool) :
    Trace (process shared) vacant (episode shared task) vacant := by
  let slot := if shared then false else task
  apply Trace.cons (t := mark vacant slot)
  · exact ⟨slot, rfl, rfl, rfl⟩
  · apply Trace.cons (t := vacant)
    · exact ⟨mark_at_slot _ _, (clear_after_fresh_mark vacant slot rfl).symm⟩
    · exact Trace.nil vacant

theorem arbitrary_serial_episodes (shared : Bool) (requests : List Bool) :
    Trace (process shared) vacant (requests.flatMap (episode shared)) vacant := by
  induction requests with
  | nil => exact Trace.nil vacant
  | cons task requests ih =>
    apply trace_append_iff.mpr
    exact ⟨vacant, episode_returns_vacant shared task, ih⟩

theorem serial_success_does_not_remove_overlap_conflict :
    (∀ requests : List Bool, Trace (process true) vacant (requests.flatMap (episode true)) vacant) ∧
    ¬ ∃ first final, Acquire true vacant false first ∧ Acquire true first true final :=
  ⟨arbitrary_serial_episodes true, shared_overlap_impossible⟩

end Generative.ExplanatoryLeaseDynamics

#print axioms Generative.ExplanatoryLeaseDynamics.mark_at_slot
#print axioms Generative.ExplanatoryLeaseDynamics.mark_at_other
#print axioms Generative.ExplanatoryLeaseDynamics.clear_after_fresh_mark
#print axioms Generative.ExplanatoryLeaseDynamics.activity_round
#print axioms Generative.ExplanatoryLeaseDynamics.ordinary_step_has_native_round
#print axioms Generative.ExplanatoryLeaseDynamics.joint_answer_iff_overlapping_acquisitions
#print axioms Generative.ExplanatoryLeaseDynamics.shared_overlap_impossible
#print axioms Generative.ExplanatoryLeaseDynamics.separate_overlap_realized
#print axioms Generative.ExplanatoryLeaseDynamics.episode_returns_vacant
#print axioms Generative.ExplanatoryLeaseDynamics.arbitrary_serial_episodes
#print axioms Generative.ExplanatoryLeaseDynamics.serial_success_does_not_remove_overlap_conflict
