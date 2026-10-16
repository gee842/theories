import KnowledgeCorrespondence

/-!
A bounded whole-activity construction for the normative-structure investigation.
The coordinates describe one local history, not independently given mind/world
substances. The question is whether the present specimen is within a reference.
This stipulates measurement semantics and an exact inspection channel. It does
not define knowledge, normative authority, neural implementation or moral good.
`work` counts only overt production events, not all activity or cognition.
-/
namespace Generative.NormativeActivity

structure Receipt where
  specimen : Nat
  reference : Nat
  report : Bool
  deriving DecidableEq, Repr

structure State where
  specimen : Nat
  reference : Nat
  receipt : Option Receipt
  judgment : Option Bool
  inspectionOpen : Bool
  budget : Nat
  work : Nat
  repetitions : Nat
  deriving DecidableEq, Repr

def target (s : State) : Bool := decide (s.specimen ≤ s.reference)

def sample (s : State) : Receipt := ⟨s.specimen, s.reference, target s⟩

def memoryAnswer (s : State) : Option Bool := s.receipt.map Receipt.report

-- A causal inspection, with declared open access and one unit of finite support.
def inspect (s : State) : State :=
  if s.inspectionOpen && decide (0 < s.budget) then
    {s with receipt := some (sample s), budget := s.budget - 1}
  else s

inductive Event where
  | inspect
  | takeUp
  | changeReference (r : Nat)
  | close
  | reopen
  | repeat
  | produce
  | suspend
  | rest
  deriving DecidableEq, Repr

def step (e : Event) (s : State) : State :=
  match e with
  | .inspect => inspect s
  | .takeUp => {s with judgment := memoryAnswer s}
  | .changeReference r => {s with reference := r}
  | .close => {s with inspectionOpen := false}
  | .reopen => {s with inspectionOpen := true}
  | .repeat => {s with repetitions := s.repetitions + 1}
  | .produce => {s with work := s.work + 1}
  | .suspend => {s with judgment := none}
  | .rest => s

def run : List Event → State → State
  | [], s => s
  | e :: es, s => run es (step e s)

-- The operative view excludes the actual uninspected reference and specimen.
-- It includes retained measurement content, not a hidden true-current label.
def view (s : State) : Option Receipt × Option Bool × Bool × Nat × Nat × Nat :=
  (s.receipt, s.judgment, s.inspectionOpen, s.budget, s.work, s.repetitions)

def ClosedLocal : Event → Prop
  | .inspect | .takeUp | .close | .repeat | .produce | .suspend | .rest => True
  | _ => False

def ReceiptSound (s : State) : Prop :=
  ∀ r, s.receipt = some r → r.report = decide (r.specimen ≤ r.reference)

def ClosedDomain (s : State) : Prop := s.inspectionOpen = false

def CurrentCorrect (s : State) : Prop := s.judgment = some (target s)

-- The name means extensional correctness for this declared question. It does
-- not imply that the holder possesses warrant, cognition or a moral reason.

def initial : State := ⟨1, 0, none, none, true, 2, 0, 0⟩
def learned : State := run [.inspect, .takeUp] initial
def settled : State := run [.close] learned
def changed : State := run [.changeReference 1] settled

theorem run_append (xs ys : List Event) (s : State) :
    run (xs ++ ys) s = run ys (run xs s) := by
  induction xs generalizing s with
  | nil => rfl
  | cons x xs ih => exact ih (step x s)

theorem exact_inspection (s : State) (opened : s.inspectionOpen = true)
    (funded : 0 < s.budget) :
    (inspect s).receipt = some (sample s) ∧
    (inspect s).budget + 1 = s.budget := by
  simp [inspect, opened, funded]
  omega

theorem closed_inspection (s : State) (closed : s.inspectionOpen = false) :
    inspect s = s := by simp [inspect, closed]

theorem exhausted_inspection (s : State) (empty : s.budget = 0) :
    inspect s = s := by simp [inspect, empty]

theorem fresh_uptake_correct (s : State) (opened : s.inspectionOpen = true)
    (funded : 0 < s.budget) :
    CurrentCorrect (run [.inspect, .takeUp] s) := by
  simp [CurrentCorrect, run, step, inspect, opened, funded, memoryAnswer, sample, target]

theorem step_preserves_receipt_sound (e : Event) (s : State)
    (h : ReceiptSound s) : ReceiptSound (step e s) := by
  cases e <;> simp only [step]
  case inspect =>
    unfold inspect
    split
    · intro r hr
      simp only at hr
      cases Option.some.inj hr
      rfl
    · exact h
  all_goals exact h

theorem history_preserves_receipt_sound (es : List Event) (s : State)
    (h : ReceiptSound s) : ReceiptSound (run es s) := by
  induction es generalizing s with
  | nil => exact h
  | cons e es ih => exact ih (step e s) (step_preserves_receipt_sound e s h)

-- A closed local event cannot acquire the uninspected present relation.
-- This is proved for the supplied event family, not all possible cognition.
theorem closed_local_preserves (e : Event) (localEvent : ClosedLocal e)
    (s : State) (closed : s.inspectionOpen = false) :
    (step e s).inspectionOpen = false ∧
    (step e s).reference = s.reference ∧ (step e s).specimen = s.specimen := by
  cases e <;> simp_all [ClosedLocal, step, inspect]

theorem closed_local_view_congr (e : Event) (localEvent : ClosedLocal e)
    (s t : State) (cs : s.inspectionOpen = false) (ct : t.inspectionOpen = false)
    (same : view s = view t) : view (step e s) = view (step e t) := by
  have fields := same
  simp only [view, Prod.mk.injEq] at fields
  rcases fields with ⟨hr, hj, ho, hb, hw, hn⟩
  cases e <;> simp_all [ClosedLocal, step, inspect, view, memoryAnswer]

theorem closed_history_preserves (es : List Event)
    (localHistory : ∀ e ∈ es, ClosedLocal e) (s : State)
    (closed : s.inspectionOpen = false) :
    (run es s).inspectionOpen = false ∧
    (run es s).reference = s.reference ∧ (run es s).specimen = s.specimen := by
  induction es generalizing s with
  | nil => exact ⟨closed, rfl, rfl⟩
  | cons e es ih =>
    have he := closed_local_preserves e (localHistory e (by simp)) s closed
    have ht := ih (fun x hx => localHistory x (by simp [hx])) (step e s) he.1
    exact ⟨ht.1, ht.2.1.trans he.2.1, ht.2.2.trans he.2.2⟩

theorem closed_history_view_congr (es : List Event)
    (localHistory : ∀ e ∈ es, ClosedLocal e) (s t : State)
    (cs : s.inspectionOpen = false) (ct : t.inspectionOpen = false)
    (same : view s = view t) : view (run es s) = view (run es t) := by
  induction es generalizing s t with
  | nil => exact same
  | cons e es ih =>
    have he := localHistory e (by simp)
    exact ih (fun x hx => localHistory x (by simp [hx])) (step e s) (step e t)
      (closed_local_preserves e he s cs).1 (closed_local_preserves e he t ct).1
      (closed_local_view_congr e he s t cs ct same)

theorem learned_without_production :
    learned.judgment = some false ∧ CurrentCorrect learned ∧ learned.work = 0 := by
  decide

theorem historical_truth_present_error :
    ReceiptSound changed ∧ changed.judgment = some false ∧
    target changed = true ∧ ¬ CurrentCorrect changed := by
  constructor
  · intro r h
    simp [changed, settled, learned, initial, run, step, inspect, sample, target] at h
    subst r
    rfl
  · decide

theorem retained_distinction_does_not_select_production :
    (step .produce learned).judgment = (step .rest learned).judgment ∧
    (step .produce learned).work ≠ (step .rest learned).work := by decide

theorem same_production_can_have_different_judgment :
    (step .suspend learned).work = learned.work ∧
    (step .suspend learned).judgment ≠ learned.judgment := by decide

theorem reachable_closed_disagreement :
    view settled = view changed ∧ target settled ≠ target changed ∧
    settled = run [.inspect, .takeUp, .close] initial ∧
    changed = run [.inspect, .takeUp, .close, .changeReference 1] initial := by decide

theorem closed_domain_not_resolving :
    ¬ KnowledgeCorrespondence.Resolves ClosedDomain view target := by
  intro h
  have bad := h settled changed rfl rfl reachable_closed_disagreement.1
  exact reachable_closed_disagreement.2.1 bad

theorem sound_closed_answer_abstains
    (answer : (Option Receipt × Option Bool × Bool × Nat × Nat × Nat) → Option Bool)
    (sound : KnowledgeCorrespondence.SoundOn ClosedDomain view target answer) :
    answer (view settled) = none := by
  exact KnowledgeCorrespondence.conflicting_fibre_forces_abstention sound
    (show ClosedDomain settled from rfl) (show ClosedDomain changed from rfl)
    reachable_closed_disagreement.1 reachable_closed_disagreement.2.1

-- Arbitrarily many supplied local events, including repetition and production,
-- cannot distinguish these reachable histories without a newly opening event.
theorem closed_continuations_remain_unresolved (es : List Event)
    (localHistory : ∀ e ∈ es, ClosedLocal e) :
    view (run es settled) = view (run es changed) ∧
    target (run es settled) ≠ target (run es changed) := by
  constructor
  · exact closed_history_view_congr es localHistory settled changed rfl rfl
      reachable_closed_disagreement.1
  · have hs := closed_history_preserves es localHistory settled rfl
    have ht := closed_history_preserves es localHistory changed rfl
    simpa only [target, hs.2.1, hs.2.2, ht.2.1, ht.2.2] using
      reachable_closed_disagreement.2.1

theorem reopening_and_inspection_repair :
    CurrentCorrect (run [.reopen, .inspect, .takeUp] changed) ∧
    (run [.reopen, .inspect, .takeUp] changed).judgment = some true ∧
    (run [.reopen, .inspect, .takeUp] changed).budget = 0 ∧
    (run [.reopen, .inspect, .takeUp] changed).work = 0 := by decide

theorem reopening_without_inspection_does_not_repair :
    ¬ CurrentCorrect (run [.reopen, .takeUp] changed) := by decide

theorem exhausted_reopening_does_not_repair :
    ¬ CurrentCorrect (run [.reopen, .inspect, .takeUp] {changed with budget := 0}) := by decide

theorem suspension_retains_relation_and_record :
    (step .suspend changed).judgment = none ∧
    (step .suspend changed).reference = changed.reference ∧
    (step .suspend changed).receipt = changed.receipt ∧
    target (step .suspend changed) = target changed := by decide

end Generative.NormativeActivity
