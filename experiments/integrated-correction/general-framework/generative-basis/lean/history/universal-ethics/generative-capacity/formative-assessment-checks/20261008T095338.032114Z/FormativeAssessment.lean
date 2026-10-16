import ClassificationRevision

/- Assessment is an event in the same process as the capacity assessed.
The finite circuit below models retained request-sensitive routing, not full
understanding, consciousness, ethical standing, or a human developmental law. -/
namespace FormativeAssessment

def BackwardStable {S : Type} (change : S → S) (target : S → Prop) : Prop :=
  ∀ s, target (change s) → target s

theorem retrospective_sound_iff_backward_stable {S : Type}
    (change : S → S) (target : S → Prop) (read : S → Bool)
    (current : ∀ s, read s = true ↔ target s) :
    (∀ s, read (change s) = true → target s) ↔ BackwardStable change target := by
  constructor
  · intro h s hs
    exact h s ((current (change s)).2 hs)
  · intro h s hs
    exact h s ((current (change s)).1 hs)

theorem contradictory_undated_records_not_faithful {H : Type}
    (records : List (H × Bool)) (a : H) (target : H → Prop)
    (positive : (a, true) ∈ records) (negative : (a, false) ∈ records) :
    ¬ ClassificationRevision.Faithful records target := by
  intro h
  have yes := (h a true positive).1 rfl
  have impossible := (h a false negative).2 yes
  cases impossible

inductive Inquiry (A O R : Type) where
  | finish : R → Inquiry A O R
  | ask : A → (O → Inquiry A O R) → Inquiry A O R

def execute {S A O R : Type} (step : S → A → S × O) :
    Inquiry A O R → S → S × R
  | .finish r, s => (s,r)
  | .ask a next, s =>
    let out := step s a
    execute step (next out.2) out.1

theorem equal_successors_defeat_every_later_inquiry {S A O R : Type}
    (step : S → A → S × O) (left right : S) (a : A)
    (same : step left a = step right a) (next : O → Inquiry A O R) :
    execute step (.ask a next) left = execute step (.ask a next) right := by
  simp only [execute, same]

structure State where
  linked : Bool
  credits : Nat
  deriving DecidableEq

inductive Action where
  | request : Bool → Action
  | prompt : Bool → Action
  | form
  deriving DecidableEq

inductive Reading where
  | reply : Bool → Reading
  | acknowledged
  | unavailable
  deriving DecidableEq

/-- An actual request-to-response route. With the link absent, the default is
false. A prompt supplies the response by a separate path without adding a link. -/
def response (s : State) (request : Bool) : Bool :=
  if s.linked then request else false

def Capacity (s : State) : Prop := ∀ request, response s request = request

def step (s : State) (a : Action) : State × Reading :=
  match s.credits with
  | 0 => (s, .unavailable)
  | n+1 =>
    match a with
    | .request q => (⟨s.linked,n⟩, .reply (response s q))
    | .prompt q => (⟨s.linked,n⟩, .reply q)
    | .form => (⟨true,n⟩, .acknowledged)

theorem capacity_iff_linked (s : State) : Capacity s ↔ s.linked = true := by
  rcases s with ⟨b,n⟩
  cases b <;> simp [Capacity,response]

theorem no_credit_no_formation (b : Bool) (a : Action) :
    step ⟨b,0⟩ a = (⟨b,0⟩,.unavailable) := rfl

theorem acquired_unprompted_reading_exact (b : Bool) (n : Nat) :
    (step ⟨b,n+1⟩ (.request true)).2 = .reply true ↔ Capacity ⟨b,n+1⟩ := by
  cases b <;> simp [step,response,Capacity]

theorem prompted_success_without_retained_capacity (n : Nat) :
    (step ⟨false,n+1⟩ (.prompt true)).2 = .reply true ∧
    ¬ Capacity (step ⟨false,n+1⟩ (.prompt true)).1 := by
  simp [step,Capacity,response]

theorem supported_formation_establishes_capacity (b : Bool) (n : Nat) :
    Capacity (step ⟨b,n+1⟩ .form).1 := by
  simp [step,Capacity,response]

theorem formation_is_not_backward_stable :
    ¬ BackwardStable (fun s => (step s .form).1) Capacity := by
  intro h
  have bad := h ⟨false,1⟩ (supported_formation_establishes_capacity false 0)
  have nope : ¬ Capacity ⟨false,1⟩ := by simp [Capacity,response]
  exact nope bad

theorem formation_coalesces_distinct_initial_routes (n : Nat) :
    step ⟨false,n+1⟩ .form = step ⟨true,n+1⟩ .form := rfl

theorem formation_first_cannot_recover_initial_route
    (n : Nat) (next : Reading → Inquiry Action Reading Bool) :
    ¬ ((execute step (.ask .form next) ⟨false,n+1⟩).2 = false ∧
       (execute step (.ask .form next) ⟨true,n+1⟩).2 = true) := by
  rintro ⟨hf,ht⟩
  have same := equal_successors_defeat_every_later_inquiry step
    (State.mk false (n+1)) (State.mk true (n+1)) Action.form
    (formation_coalesces_distinct_initial_routes n) next
  have outputs := congrArg Prod.snd same
  rw [hf,ht] at outputs
  cases outputs

def formThenRead : Inquiry Action Reading Reading :=
  .ask .form (fun _ => .ask (.request true) Inquiry.finish)

theorem formation_then_unprompted_probe_succeeds (b : Bool) (n : Nat) :
    execute step formThenRead ⟨b,n+2⟩ = (⟨true,n⟩,.reply true) := rfl

theorem one_credit_forms_but_cannot_fund_assessment (b : Bool) :
    execute step formThenRead ⟨b,1⟩ = (⟨true,0⟩,.unavailable) := rfl

/-- Retaining the earlier acquired answer is an actual additional access route.
The target is the initial link, not the link after formation. -/
def baselineFirst : Inquiry Action Reading Bool :=
  .ask (.request true) (fun before =>
    .ask .form (fun _ => .finish (before == .reply true)))

theorem baseline_record_recovers_initial_route (b : Bool) (n : Nat) :
    (execute step baselineFirst ⟨b,n+2⟩).2 = b ∧
    Capacity (execute step baselineFirst ⟨b,n+2⟩).1 := by
  cases b <;> simp [execute,baselineFirst,step,response,Capacity]

def pairedReadings (s : State) : Reading × Reading :=
  let prompted := step s (.prompt true)
  let unprompted := step prompted.1 (.request true)
  (prompted.2,unprompted.2)

def assistanceContrast (r : Reading × Reading) : Bool :=
  r.1 == .reply true && r.2 == .reply false

theorem acquired_contrast_tracks_missing_route (b : Bool) (n : Nat) :
    assistanceContrast (pairedReadings ⟨b,n+2⟩) = !b := by
  cases b <;> rfl

theorem positive_prompt_alone_does_not_identify (n : Nat) :
    (step ⟨false,n+1⟩ (.prompt true)).2 =
    (step ⟨true,n+1⟩ (.prompt true)).2 ∧
    (¬ Capacity ⟨false,n+1⟩ ∧ Capacity ⟨true,n+1⟩) := by
  simp [step,Capacity,response]

def changedRecords : List (Bool × Bool) := [(true,false),(true,true)]

theorem truthful_change_cannot_fit_one_undated_target (target : Bool → Prop) :
    ¬ ClassificationRevision.Faithful changedRecords target :=
  contradictory_undated_records_not_faithful changedRecords true target
    (by simp [changedRecords]) (by simp [changedRecords])

def stagedRecords : List ((Nat × Bool) × Bool) :=
  let before := step ⟨false,3⟩ (.request true)
  let formed := step before.1 .form
  let after := step formed.1 (.request true)
  let retain (stage : Nat) (reading : Reading) :=
    match reading with
    | .reply b => [((stage,true),b)]
    | _ => []
  retain 0 before.2 ++ retain 1 after.2

def stagedTarget (q : Nat × Bool) : Prop :=
  if q.1 = 0 then response ⟨false,3⟩ q.2 = true
  else response (step (step ⟨false,3⟩ (.request true)).1 .form).1 q.2 = true

theorem dated_records_preserve_both_true_observations :
    ClassificationRevision.Faithful stagedRecords stagedTarget := by
  intro a b h
  simp [stagedRecords,step,response] at h
  rcases h with h | h
  · cases h
    simp [stagedTarget,response]
  · cases h
    simp [stagedTarget,response,step]

end FormativeAssessment
